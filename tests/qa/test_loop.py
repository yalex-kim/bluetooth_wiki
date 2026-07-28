import json

import pytest

from qa.loop import AgenticLoop
from qa.retrieval.actions import ActionResult, Evidence


class _Call:
    def __init__(self, name, args, cid="c1"):
        self.id = cid
        self.type = "function"
        self.function = type("F", (), {"name": name, "arguments": json.dumps(args)})()


class _Msg:
    def __init__(self, content="", tool_calls=None):
        self.content = content
        self.tool_calls = tool_calls


class _Resp:
    def __init__(self, msg):
        self.choices = [type("C", (), {"message": msg, "finish_reason": "stop"})()]
        self.usage = None


class FakeActions:
    TOOL_SCHEMAS = [{"type": "function", "function": {
        "name": "vector_search", "description": "",
        "parameters": {"type": "object", "properties": {}}}}]

    def __init__(self):
        self.calls = []

    async def run(self, name, args):
        self.calls.append((name, args))
        return ActionResult(
            text="CONNECTION STATE — the peripheral shall use connSupervisionTimeout.",
            evidence=[Evidence(ref_id="core-6.0#4.5::s0", doc="Core Spec v6.0", section="4.5",
                               page=512, path="sources/specs/6.0/Core_v6.0.md",
                               kind="chunk", text="...")],
        )


ANSWER = json.dumps({
    "answer": "The peripheral uses connSupervisionTimeout.",
    "citations": [{"doc": "Core Spec v6.0", "section": "4.5"}],
    "related_entities": ["connSupervisionTimeout"],
    "confidence": "high",
})


def _chat_fn(scripted):
    seq = list(scripted)

    async def fake_chat(messages, *, model=None, tools=None, tool_choice="auto"):
        return _Resp(seq.pop(0))

    return fake_chat


@pytest.mark.asyncio
async def test_loop_calls_a_tool_then_answers():
    actions = FakeActions()
    loop = AgenticLoop(actions, chat_fn=_chat_fn([
        _Msg(tool_calls=[_Call("vector_search", {"query": "supervision timeout"})]),
        _Msg(content=ANSWER),
    ]))
    result = await loop.run("What is connSupervisionTimeout?")
    assert actions.calls[0][0] == "vector_search"
    assert result.answer.startswith("The peripheral")
    assert result.citations[0]["page"] == 512
    assert result.confidence == "high"
    assert result.budget_exhausted is False


@pytest.mark.asyncio
async def test_scope_filter_is_injected_into_the_first_vector_search():
    actions = FakeActions()
    loop = AgenticLoop(actions, chat_fn=_chat_fn([
        _Msg(tool_calls=[_Call("vector_search", {"query": "x"})]),
        _Msg(content=ANSWER),
    ]))
    await loop.run("q", scope_filter={"doc_type": ["Core"]})
    assert actions.calls[0][1]["scope_filter"] == {"doc_type": ["Core"]}


@pytest.mark.asyncio
async def test_model_supplied_scope_filter_is_not_overwritten():
    actions = FakeActions()
    loop = AgenticLoop(actions, chat_fn=_chat_fn([
        _Msg(tool_calls=[_Call("vector_search", {"query": "x", "scope_filter": {"doc_type": ["Mesh"]}})]),
        _Msg(content=ANSWER),
    ]))
    await loop.run("q", scope_filter={"doc_type": ["Core"]})
    assert actions.calls[0][1]["scope_filter"] == {"doc_type": ["Mesh"]}


@pytest.mark.asyncio
async def test_unverifiable_citations_are_dropped_and_confidence_downgraded():
    bad = json.dumps({"answer": "Made up.",
                      "citations": [{"doc": "Core Spec v6.0", "section": "99.9"}],
                      "related_entities": [], "confidence": "high"})
    loop = AgenticLoop(FakeActions(), chat_fn=_chat_fn([
        _Msg(tool_calls=[_Call("vector_search", {"query": "x"})]),
        _Msg(content=bad),
    ]))
    result = await loop.run("q")
    assert result.citations == []
    assert len(result.dropped_citations) == 1
    assert result.confidence == "low"


@pytest.mark.asyncio
async def test_budget_exhaustion_forces_low_confidence_and_a_final_synthesis_turn():
    always_tool = [_Msg(tool_calls=[_Call("vector_search", {"query": "x"}, cid=f"c{i}")])
                   for i in range(3)]
    loop = AgenticLoop(FakeActions(), max_iterations=3,
                       chat_fn=_chat_fn(always_tool + [_Msg(content=ANSWER)]))
    result = await loop.run("q")
    assert result.budget_exhausted is True
    assert result.confidence == "low"  # §7.2: never hide thin evidence
    assert result.answer  # but still return a real answer


@pytest.mark.asyncio
async def test_max_tool_calls_is_enforced_independently():
    many = [_Msg(tool_calls=[_Call("vector_search", {"query": "x"}, cid="a"),
                             _Call("vector_search", {"query": "y"}, cid="b")])
            for _ in range(5)]
    loop = AgenticLoop(FakeActions(), max_iterations=10, max_tool_calls=3,
                       chat_fn=_chat_fn(many + [_Msg(content=ANSWER)]))
    result = await loop.run("q")
    assert result.tool_calls <= 4  # an in-flight batch may finish; a new one may not start
    assert result.budget_exhausted is True


@pytest.mark.asyncio
async def test_non_json_final_answer_still_returns_text_with_low_confidence():
    loop = AgenticLoop(FakeActions(), chat_fn=_chat_fn([_Msg(content="just prose, no JSON")]))
    result = await loop.run("q")
    assert "just prose" in result.answer
    assert result.confidence == "low" and result.citations == []


@pytest.mark.asyncio
async def test_trace_records_each_action_for_debugging():
    loop = AgenticLoop(FakeActions(), chat_fn=_chat_fn([
        _Msg(tool_calls=[_Call("vector_search", {"query": "x"})]),
        _Msg(content=ANSWER),
    ]))
    result = await loop.run("q")
    assert result.trace[0]["action"] == "vector_search"
    assert "evidence" in result.trace[0]


@pytest.mark.asyncio
async def test_malformed_tool_arguments_surface_as_an_error_result_not_a_crash():
    class BadCall(_Call):
        def __init__(self):
            self.id = "c1"
            self.type = "function"
            self.function = type("F", (), {"name": "vector_search", "arguments": "{not json"})()

    loop = AgenticLoop(FakeActions(), chat_fn=_chat_fn([
        _Msg(tool_calls=[BadCall()]),
        _Msg(content=ANSWER),
    ]))
    result = await loop.run("q")
    assert result.answer  # loop survived and produced an answer
    assert any("malformed" in str(step.get("error", "")).lower() for step in result.trace)


@pytest.mark.asyncio
async def test_conversation_context_is_used_to_reinterpret_the_query():
    seen = {}

    async def capture_chat(messages, *, model=None, tools=None, tool_choice="auto"):
        seen.setdefault("messages", messages)
        return _Resp(_Msg(content=ANSWER))

    loop = AgenticLoop(FakeActions(), chat_fn=capture_chat)
    await loop.run("and in 5.4?", conversation_context=[
        {"role": "user", "content": "Tell me about LE Audio"}])
    assert "LE Audio" in str(seen["messages"])
