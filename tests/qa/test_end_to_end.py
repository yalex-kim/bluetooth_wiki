"""End-to-end composition check: ingest -> index -> actions -> loop -> service.

The unit tests each stub their neighbours, so nothing else proves the real
classes fit together. This wires the actual pipeline, stores, actions, loop and
service with only the LLM faked, and asserts the §8.1 envelope comes out with a
citation that survived §7.4 verification.
"""
import json

import pytest
import pytest_asyncio

from qa.ingest.pipeline import Manifest, ingest_document
from qa.loop import AgenticLoop
from qa.prefilter import ScopeDecision
from qa.retrieval.actions import RetrievalActions
from qa.service import SpecQAService
from qa.store.graph_sqlite import SqliteGraphStore
from qa.store.vector_local import LocalVectorStore

SPEC = """# Core

## 4 LINK LAYER SPECIFICATION

The Link Layer defines the states below.

### 4.5 CONNECTION STATE

The peripheral shall use connSupervisionTimeout to detect a lost connection.

| Parameter | Min | Max |
|---|---|---|
| connInterval | 7.5 ms | 4 s |

Table 4.1: Connection parameters
"""


async def fake_embed(texts):
    """Crude lexical embedding: 3 dims keyed on marker terms, no endpoint needed."""
    out = []
    for t in texts:
        low = t.lower()
        out.append([
            float("connsupervisiontimeout" in low),
            float("conninterval" in low),
            float("link layer" in low),
        ])
    return out


class _Fn:
    def __init__(self, name, args):
        self.name = name
        self.arguments = json.dumps(args)


class _Call:
    def __init__(self, name, args, cid="c1"):
        self.id = cid
        self.type = "function"
        self.function = _Fn(name, args)


class _Msg:
    def __init__(self, content="", tool_calls=None):
        self.content = content
        self.tool_calls = tool_calls


class _Resp:
    def __init__(self, msg):
        self.choices = [type("C", (), {"message": msg, "finish_reason": "stop"})()]
        self.usage = None


@pytest_asyncio.fixture
async def service(tmp_path):
    src = tmp_path / "Core_v6.0.md"
    src.write_text(SPEC, encoding="utf-8")
    index = tmp_path / "index"

    vector = LocalVectorStore(index / "vectors")
    graph = SqliteGraphStore(index / "graph.db")
    manifest = Manifest(index / "manifest.json")

    stats = await ingest_document(
        src, doc_id="core-6.0", title="Core Spec v6.0", doc_type="Core", version="6.0",
        vector_store=vector, graph_store=graph, manifest=manifest, embed_fn=fake_embed,
    )
    assert stats.chunks > 0

    actions = RetrievalActions(
        vector, graph, embed_fn=fake_embed,
        doc_registry={"core-6.0": {"title": "Core Spec v6.0", "path": str(src),
                                   "doc_type": "Core", "version": "6.0"}},
    )
    yield actions, index
    graph.close()


async def _offline_scope(query, *, spec_scope=None, spec_version=None):
    return ScopeDecision(out_of_scope=False, scope_filter={"doc_type": ["Core"]},
                         reason="test", used_llm=False)


@pytest.mark.asyncio
async def test_search_then_answer_produces_a_verified_citation(service):
    actions, _ = service
    scripted = [
        _Msg(tool_calls=[_Call("vector_search", {"query": "connSupervisionTimeout"})]),
        _Msg(content=json.dumps({
            "answer": "The peripheral uses connSupervisionTimeout to detect a lost connection.",
            "citations": [{"doc": "Core Spec v6.0", "section": "4.5"}],
            "related_entities": ["connSupervisionTimeout"],
            "confidence": "high",
        })),
    ]

    async def chat_fn(messages, *, model=None, tools=None, tool_choice="auto"):
        # the retrieved spec text must actually reach the model
        if len(scripted) == 1:
            assert "connSupervisionTimeout" in str(messages)
        return _Resp(scripted.pop(0))

    svc = SpecQAService(loop=AgenticLoop(actions, chat_fn=chat_fn), actions=actions,
                        scope_fn=_offline_scope)
    out = await svc.ask("What detects a lost connection?")

    assert set(out) == {"answer", "citations", "related_entities", "confidence",
                        "out_of_scope", "retrieval_trace"}
    assert out["out_of_scope"] is False
    assert out["confidence"] == "high"
    assert out["citations"], "a real retrieved citation should survive verification"
    assert out["citations"][0]["section"] == "4.5"
    assert out["citations"][0]["path"].endswith("Core_v6.0.md")


@pytest.mark.asyncio
async def test_a_table_question_can_be_answered_through_get_table(service):
    actions, _ = service
    # find the table id the way the model would: via the section's relations
    section_id = "core-6.0#4.5"
    traverse = actions.graph_traverse(section_id, relation_types=["hasTable"], hops=1)
    assert "table" in traverse.text

    table = actions.get_table(section_id=section_id)
    assert "| connInterval | 7.5 ms | 4 s |" in table.text
    assert table.evidence[0].section == "4.5"


@pytest.mark.asyncio
async def test_hallucinated_citation_is_stripped_end_to_end(service):
    actions, _ = service
    scripted = [
        _Msg(tool_calls=[_Call("vector_search", {"query": "connSupervisionTimeout"})]),
        _Msg(content=json.dumps({
            "answer": "Invented.",
            "citations": [{"doc": "Core Spec v6.0", "section": "12.34"}],
            "related_entities": [],
            "confidence": "high",
        })),
    ]

    async def chat_fn(messages, *, model=None, tools=None, tool_choice="auto"):
        return _Resp(scripted.pop(0))

    svc = SpecQAService(loop=AgenticLoop(actions, chat_fn=chat_fn), actions=actions,
                        scope_fn=_offline_scope)
    out = await svc.ask("Something the spec does not say")
    assert out["citations"] == []
    assert out["confidence"] == "low"
