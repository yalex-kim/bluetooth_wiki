import pytest

from qa import prefilter
from qa.loop import LoopResult
from qa.retrieval.actions import Evidence
from qa.service import SpecQAService

EV = [Evidence(ref_id="r", doc="Core Spec v6.0", section="4.5", page=512,
               path="sources/specs/6.0/Core_v6.0.md", kind="chunk", text="...")]


class FakeLoop:
    def __init__(self):
        self.seen = []

    async def run(self, query, *, scope_filter=None, conversation_context=None):
        self.seen.append({"query": query, "scope_filter": scope_filter,
                          "conversation_context": conversation_context})
        return LoopResult(
            answer="Answer.",
            citations=[{"doc": "Core Spec v6.0", "section": "4.5", "page": 512, "path": "p"}],
            related_entities=["L2CAP"], confidence="high", evidence=EV,
            trace=[{"action": "vector_search"}], iterations=2, tool_calls=2,
            budget_exhausted=False, dropped_citations=[], duration_ms=10,
        )


@pytest.mark.asyncio
async def test_ask_returns_exactly_the_frozen_output_keys():
    out = await SpecQAService(loop=FakeLoop()).ask("What is L2CAP?")
    assert set(out) == {"answer", "citations", "related_entities", "confidence",
                        "out_of_scope", "retrieval_trace"}
    assert out["out_of_scope"] is False
    assert out["retrieval_trace"] is None  # §7.5 default off
    assert set(out["citations"][0]) == {"doc", "section", "page", "path"}


@pytest.mark.asyncio
async def test_out_of_scope_short_circuits_before_the_loop():
    loop = FakeLoop()
    out = await SpecQAService(loop=loop).ask("What is the capital of France?")
    assert out["out_of_scope"] is True
    assert out["confidence"] == "low"
    assert out["citations"] == []
    assert loop.seen == []  # §7.0 cost defence


@pytest.mark.asyncio
async def test_scope_hint_is_passed_into_the_loop():
    loop = FakeLoop()
    await SpecQAService(loop=loop).ask("pairing?", spec_scope="Core-LE", spec_version="5.4")
    assert loop.seen[0]["scope_filter"]["doc_type"] == ["Core"]


@pytest.mark.asyncio
async def test_include_trace_exposes_the_retrieval_trace():
    out = await SpecQAService(loop=FakeLoop()).ask("What is L2CAP?", include_trace=True)
    assert out["retrieval_trace"]["iterations"] == 2
    assert out["retrieval_trace"]["steps"][0]["action"] == "vector_search"


@pytest.mark.asyncio
async def test_conversation_context_reaches_the_loop_but_is_not_persisted():
    async def offline_scope(query, *, spec_scope=None, spec_version=None):
        # These follow-ups carry no Bluetooth vocabulary, so the real gate would
        # reach for the LLM. Tests stay offline.
        return prefilter.ScopeDecision(out_of_scope=False, scope_filter=None,
                                       reason="test", used_llm=False)

    loop = FakeLoop()
    service = SpecQAService(loop=loop, scope_fn=offline_scope)
    await service.ask("and in 5.4?",
                      conversation_context=[{"role": "user", "content": "LE Audio"}])
    assert loop.seen[0]["conversation_context"]
    await service.ask("another")
    assert loop.seen[1]["conversation_context"] in (None, [])  # §8.3 stateless
