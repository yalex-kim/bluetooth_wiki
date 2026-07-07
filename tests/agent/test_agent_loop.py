import asyncio
import json
from types import SimpleNamespace


def _msg(content=None, tool_calls=None):
    return SimpleNamespace(content=content, tool_calls=tool_calls)


def _resp(message):
    return SimpleNamespace(
        choices=[SimpleNamespace(message=message, finish_reason="stop")],
        usage=SimpleNamespace(prompt_tokens=10, completion_tokens=5),
    )


def _tool_call(cid, name, args):
    return SimpleNamespace(id=cid, function=SimpleNamespace(name=name, arguments=json.dumps(args)))


class FakeClient:
    """Turn 1: model calls search_wiki. Turn 2: model returns the final JSON answer."""
    def __init__(self):
        self.calls = 0
        self.seen_messages = []
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    async def _create(self, *, model, messages, tools, tool_choice):
        self.calls += 1
        self.seen_messages = messages
        if self.calls == 1:
            return _resp(_msg(tool_calls=[_tool_call("c1", "search_wiki", {"query": "channel sounding", "scope": "wiki"})]))
        final = '```json\n{"answer": "CS measures distance.", "citations": [], "reasoning": "found it"}\n```'
        return _resp(_msg(content=final))


def test_agent_ask_runs_tool_then_parses_answer(monkeypatch):
    from agent import agent as agent_mod
    fake = FakeClient()
    monkeypatch.setattr(agent_mod, "get_client", lambda: fake)

    a = agent_mod.BluetoothWikiAgent(model="gpt-oss-120b", search_strategy="v1")
    resp = asyncio.run(a.ask("What is channel sounding?"))

    assert fake.calls == 2
    assert resp.answer == "CS measures distance."
    assert resp.reasoning == "found it"
    assert resp.tool_calls == 1
    assert resp.tools_used == {"search_wiki": 1}
    assert resp.num_turns == 2
    assert resp.usage == {"prompt_tokens": 20, "completion_tokens": 10}
    assert resp.total_cost_usd is None
    assert any(m.get("role") == "tool" and m.get("tool_call_id") == "c1" for m in fake.seen_messages)


class UnknownToolClient(FakeClient):
    async def _create(self, *, model, messages, tools, tool_choice):
        self.calls += 1
        self.seen_messages = messages
        if self.calls == 1:
            return _resp(_msg(tool_calls=[_tool_call("c9", "no_such_tool", {})]))
        return _resp(_msg(content='{"answer": "ok", "citations": [], "reasoning": ""}'))


def test_unknown_tool_call_is_fed_back_not_fatal(monkeypatch):
    from agent import agent as agent_mod
    fake = UnknownToolClient()
    monkeypatch.setattr(agent_mod, "get_client", lambda: fake)
    a = agent_mod.BluetoothWikiAgent(model="gpt-oss-120b", search_strategy="v1")
    resp = asyncio.run(a.ask("q"))
    assert resp.answer == "ok"
    tool_msgs = [m for m in fake.seen_messages if m.get("role") == "tool"]
    assert tool_msgs and "unknown tool" in tool_msgs[0]["content"].lower()


class MalformedArgsClient(FakeClient):
    async def _create(self, *, model, messages, tools, tool_choice):
        self.calls += 1
        self.seen_messages = messages
        if self.calls == 1:
            bad = SimpleNamespace(id="cbad", function=SimpleNamespace(name="search_wiki", arguments="{not valid json"))
            return _resp(_msg(tool_calls=[bad]))
        return _resp(_msg(content='{"answer": "recovered", "citations": [], "reasoning": ""}'))


def test_malformed_tool_args_fed_back_as_error(monkeypatch):
    from agent import agent as agent_mod
    fake = MalformedArgsClient()
    monkeypatch.setattr(agent_mod, "get_client", lambda: fake)
    a = agent_mod.BluetoothWikiAgent(model="gpt-oss-120b", search_strategy="v1")
    resp = asyncio.run(a.ask("q"))
    assert resp.answer == "recovered"
    tool_msgs = [m for m in fake.seen_messages if m.get("role") == "tool"]
    assert tool_msgs and "malformed arguments" in tool_msgs[0]["content"].lower()
