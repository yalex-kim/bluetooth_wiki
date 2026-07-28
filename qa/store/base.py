"""Storage protocols (§6).

§12 leaves the server-vs-embedded DB choice open, so nothing above this module
names a product. v0.1 ships dependency-free local backends; a Qdrant or Neo4j
adapter is a new class implementing the same protocol, and callers do not change.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass
class VectorRecord:
    id: str
    text: str
    embedding: list
    metadata: dict = field(default_factory=dict)


@dataclass
class VectorHit:
    id: str
    text: str
    score: float
    metadata: dict = field(default_factory=dict)


@dataclass
class GraphNode:
    id: str
    type: str
    name: str
    properties: dict = field(default_factory=dict)


@dataclass
class GraphEdge:
    source: str
    target: str
    type: str
    properties: dict = field(default_factory=dict)


@runtime_checkable
class VectorStore(Protocol):
    def upsert(self, records: list) -> None: ...
    def delete(self, ids: list) -> None: ...
    def search(self, embedding, *, top_k: int = 8, filters: dict | None = None) -> list: ...
    def get(self, id: str): ...
    def count(self) -> int: ...
    def persist(self) -> None: ...


@runtime_checkable
class GraphStore(Protocol):
    def add_nodes(self, nodes: list) -> None: ...
    def add_edges(self, edges: list) -> None: ...
    def get_node(self, node_id: str): ...
    def lookup(self, name: str, *, type: str | None = None, limit: int = 10) -> list: ...
    def neighbors(self, node_id: str, *, relation_types: list | None = None,
                  hops: int = 1, limit: int = 40) -> list: ...
    def delete_document(self, doc_id: str) -> None: ...
    def close(self) -> None: ...


def matches(metadata: dict, filters: dict | None) -> bool:
    """Equality match; a list/tuple/set filter value means 'any of'.

    This is the shape of §7.1's ``scope_filter`` — ``{"doc_type": ["Core", "GATT"]}``.
    """
    if not filters:
        return True
    for key, want in filters.items():
        got = metadata.get(key)
        if isinstance(want, (list, tuple, set)):
            if got not in want:
                return False
        elif got != want:
            return False
    return True
