"""§8 Tool interface — the only surface the Orchestrator sees.

The design doc's first constraint (§1.2) is a stable input/output contract, so
this module's job is narrow and deliberate: run the §7.0 gate, run the §7 loop,
and return exactly the six §8.1 keys. Everything else — how many retrieval
rounds ran, which store answered, whether the graph was consulted — stays inside
(§7.5). The agent holds no conversation state (§8.3); prior turns arrive per call
and are used only to re-read the question.
"""
from __future__ import annotations

import json
from pathlib import Path

from qa import config, prefilter

OUT_OF_SCOPE_ANSWER = (
    "This question does not appear to be about the Bluetooth specifications, so "
    "no specification search was run. Route it to a different tool."
)


class SpecQAService:
    def __init__(self, index_dir=None, *, loop=None, actions=None, scope_fn=None):
        self.index_dir = Path(index_dir) if index_dir else config.QA_INDEX_DIR
        self._loop = loop
        self._actions = actions
        # Seam for tests and for swapping the §12-undecided pre-filter implementation.
        self._scope_fn = scope_fn or prefilter.classify

    # ── construction ────────────────────────────────────────────────────
    @classmethod
    def from_index(cls, index_dir=None):
        """Build the service against an on-disk index written by scripts/qa_ingest.py."""
        from qa.loop import AgenticLoop
        from qa.retrieval.actions import RetrievalActions
        from qa.store.graph_sqlite import SqliteGraphStore
        from qa.store.vector_local import LocalVectorStore

        index_dir = Path(index_dir) if index_dir else config.QA_INDEX_DIR
        vector = LocalVectorStore.load(index_dir / "vectors")
        graph = SqliteGraphStore(index_dir / "graph.db")
        registry_path = index_dir / "registry.json"
        registry = (json.loads(registry_path.read_text(encoding="utf-8"))
                    if registry_path.is_file() else {})
        actions = RetrievalActions(vector, graph, doc_registry=registry)
        return cls(index_dir, loop=AgenticLoop(actions), actions=actions)

    @property
    def loop(self):
        if self._loop is None:
            built = self.from_index(self.index_dir)
            self._loop, self._actions = built._loop, built._actions
        return self._loop

    def health(self) -> dict:
        vector = getattr(self._actions, "vector", None)
        registry = getattr(self._actions, "doc_registry", {}) or {}
        return {
            "status": "ok" if vector is not None and vector.count() else "empty",
            "vector_count": vector.count() if vector is not None else 0,
            "documents": sorted(registry),
            "index_dir": str(self.index_dir),
        }

    # ── §8.1 contract ───────────────────────────────────────────────────
    async def ask(self, query, *, spec_scope=None, spec_version=None,
                  conversation_context=None, include_trace=False) -> dict:
        decision = await self._scope_fn(query, spec_scope=spec_scope,
                                        spec_version=spec_version)
        if decision.out_of_scope:
            # §8.2: signal clearly and cheaply so the Orchestrator can re-route.
            return _envelope(answer=OUT_OF_SCOPE_ANSWER, citations=[], related_entities=[],
                             confidence="low", out_of_scope=True, trace=None)

        result = await self.loop.run(query, scope_filter=decision.scope_filter,
                                     conversation_context=conversation_context)

        trace = None
        if include_trace:
            trace = {
                "scope_reason": decision.reason,
                "scope_filter": decision.scope_filter,
                "iterations": result.iterations,
                "tool_calls": result.tool_calls,
                "budget_exhausted": result.budget_exhausted,
                "dropped_citations": result.dropped_citations,
                "duration_ms": result.duration_ms,
                "steps": result.trace,
            }
        return _envelope(answer=result.answer, citations=result.citations,
                         related_entities=result.related_entities,
                         confidence=result.confidence, out_of_scope=False, trace=trace)


def _envelope(*, answer, citations, related_entities, confidence, out_of_scope, trace):
    """The §8.1 output shape. Key set is frozen — the Orchestrator depends on it."""
    return {
        "answer": answer,
        "citations": citations,
        "related_entities": related_entities,
        "confidence": confidence,
        "out_of_scope": out_of_scope,
        "retrieval_trace": trace,
    }
