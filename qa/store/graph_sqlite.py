"""Graph store on stdlib SQLite (§6.2 stand-in while §12 is undecided).

Nodes and edges are two tables with an index on the lowercased name; traversal
is BFS in Python. That covers the §7.1 graph actions at Phase 1 volume and keeps
the deployment story to "one file on disk". A Neo4j or KuzuDB adapter is another
class against qa.store.base.GraphStore.
"""
from __future__ import annotations

import json
import sqlite3
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from qa.store.base import GraphEdge, GraphNode

_SCHEMA = """
CREATE TABLE IF NOT EXISTS nodes (
    id TEXT PRIMARY KEY, type TEXT NOT NULL, name TEXT NOT NULL,
    name_lc TEXT NOT NULL, doc_id TEXT, properties TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_nodes_name_lc ON nodes(name_lc);
CREATE INDEX IF NOT EXISTS idx_nodes_doc ON nodes(doc_id);
CREATE TABLE IF NOT EXISTS edges (
    source TEXT NOT NULL, target TEXT NOT NULL, type TEXT NOT NULL,
    properties TEXT NOT NULL, PRIMARY KEY (source, target, type)
);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target);
"""


@dataclass
class Neighbor:
    node: GraphNode
    edge: GraphEdge
    hop: int
    direction: str  # "out" | "in"


def _row_to_node(row) -> GraphNode:
    return GraphNode(id=row["id"], type=row["type"], name=row["name"],
                     properties=json.loads(row["properties"]))


class SqliteGraphStore:
    def __init__(self, path=":memory:"):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(path))
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(_SCHEMA)
        self._conn.commit()

    # ── writes ──────────────────────────────────────────────────────────
    def add_nodes(self, nodes) -> None:
        self._conn.executemany(
            "INSERT INTO nodes (id, type, name, name_lc, doc_id, properties) VALUES (?,?,?,?,?,?) "
            "ON CONFLICT(id) DO UPDATE SET type=excluded.type, name=excluded.name, "
            "name_lc=excluded.name_lc, doc_id=excluded.doc_id, properties=excluded.properties",
            [(n.id, n.type, n.name, n.name.lower(),
              (n.properties or {}).get("doc_id"), json.dumps(n.properties or {}))
             for n in nodes],
        )
        self._conn.commit()

    def add_edges(self, edges) -> None:
        self._conn.executemany(
            "INSERT INTO edges (source, target, type, properties) VALUES (?,?,?,?) "
            "ON CONFLICT(source, target, type) DO UPDATE SET properties=excluded.properties",
            [(e.source, e.target, e.type, json.dumps(e.properties or {})) for e in edges],
        )
        self._conn.commit()

    # ── reads ───────────────────────────────────────────────────────────
    def get_node(self, node_id):
        row = self._conn.execute("SELECT * FROM nodes WHERE id = ?", (node_id,)).fetchone()
        return _row_to_node(row) if row else None

    def lookup(self, name, *, type=None, limit=10):
        """§14.1 entity resolution, v0.1: exact (case-insensitive) -> alias -> prefix."""
        needle = (name or "").strip().lower()
        if not needle:
            return []
        clause, params = ("AND type = ?", [type]) if type else ("", [])

        rows = self._conn.execute(
            f"SELECT * FROM nodes WHERE name_lc = ? {clause} LIMIT ?",
            [needle, *params, limit],
        ).fetchall()
        if rows:
            return [_row_to_node(r) for r in rows]

        # Alias hit: narrow with LIKE on the serialised properties, then confirm
        # against the parsed alias list so a substring match cannot masquerade.
        alias_hits = []
        for row in self._conn.execute(
            f"SELECT * FROM nodes WHERE properties LIKE ? {clause} LIMIT ?",
            [f"%{name}%", *params, limit * 5],
        ):
            aliases = [a.lower() for a in (json.loads(row["properties"]).get("aliases") or [])]
            if needle in aliases:
                alias_hits.append(_row_to_node(row))
                if len(alias_hits) >= limit:
                    break
        if alias_hits:
            return alias_hits

        rows = self._conn.execute(
            f"SELECT * FROM nodes WHERE name_lc LIKE ? {clause} LIMIT ?",
            [f"{needle}%", *params, limit],
        ).fetchall()
        return [_row_to_node(r) for r in rows]

    def neighbors(self, node_id, *, relation_types=None, hops=1, limit=40):
        """BFS bounded by hops and by the §14.2 per-call node cap."""
        out: list[Neighbor] = []
        seen = {node_id}
        queue = deque([(node_id, 0)])
        while queue and len(out) < limit:
            current, depth = queue.popleft()
            if depth >= hops:
                continue
            for direction, own, other in (("out", "source", "target"),
                                          ("in", "target", "source")):
                sql = f"SELECT * FROM edges WHERE {own} = ?"
                params = [current]
                if relation_types:
                    sql += f" AND type IN ({','.join('?' * len(relation_types))})"
                    params += list(relation_types)
                for row in self._conn.execute(sql, params).fetchall():
                    nid = row[other]
                    if nid in seen:
                        continue
                    node = self.get_node(nid)
                    if node is None:
                        continue
                    seen.add(nid)
                    out.append(Neighbor(
                        node=node,
                        edge=GraphEdge(row["source"], row["target"], row["type"],
                                       json.loads(row["properties"])),
                        hop=depth + 1, direction=direction,
                    ))
                    queue.append((nid, depth + 1))
                    if len(out) >= limit:
                        return out
        return out

    # ── maintenance ─────────────────────────────────────────────────────
    def delete_document(self, doc_id) -> None:
        ids = [r["id"] for r in self._conn.execute(
            "SELECT id FROM nodes WHERE doc_id = ?", (doc_id,)).fetchall()]
        if not ids:
            return
        marks = ",".join("?" * len(ids))
        self._conn.execute(
            f"DELETE FROM edges WHERE source IN ({marks}) OR target IN ({marks})", ids + ids)
        self._conn.execute(f"DELETE FROM nodes WHERE id IN ({marks})", ids)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()
