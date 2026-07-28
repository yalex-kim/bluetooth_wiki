"""Ingestion (§5): markdown -> graph skeleton + vector chunks, incrementally.

The skeleton (§5.1) is rebuilt deterministically on every run — it is cheap and
idempotent. Embedding is the expensive half, so it is gated on a per-section
content hash (§5.5): re-ingesting an unchanged document costs zero endpoint
calls, which is what makes the §10 version-update pipeline affordable.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path

from qa import config
from qa.ingest.structure import parse_markdown, section_hash
from qa.store.base import GraphEdge, GraphNode, VectorRecord


@dataclass
class IngestStats:
    doc_id: str
    sections: int = 0
    sections_changed: int = 0
    sections_skipped: int = 0
    chunks: int = 0
    tables: int = 0
    figures: int = 0
    edges: int = 0
    entities: int = 0
    elapsed_ms: int = 0


class Manifest:
    """Per-section content hashes from previous runs (§5.5 / §10)."""

    def __init__(self, path):
        self.path = Path(path)
        self._hashes: dict[str, str] = {}

    @classmethod
    def load(cls, path):
        m = cls(path)
        if m.path.is_file():
            m._hashes = json.loads(m.path.read_text(encoding="utf-8"))
        return m

    def hash_of(self, section_id):
        return self._hashes.get(section_id)

    def set(self, section_id, content_hash):
        self._hashes[section_id] = content_hash

    def prune(self, doc_id, live_ids):
        """Forget sections that no longer exist in this document; return their ids."""
        stale = [k for k in self._hashes
                 if k.split("#")[0] == doc_id and k not in live_ids]
        for k in stale:
            del self._hashes[k]
        return stale

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self._hashes), encoding="utf-8")


def build_skeleton(doc):
    """§5.1: transcribe document structure into ontology-typed nodes and edges."""
    nodes = [GraphNode(
        id=doc.doc_id, type="Document", name=doc.title,
        properties={"doc_id": doc.doc_id, "doc_type": doc.doc_type,
                    "version": doc.version, "path": doc.path},
    )]
    edges = []
    id_by_number = {}

    for section in doc.sections:
        if section.level <= 2:
            node_type = "Chapter"
        elif section.level == 3:
            node_type = "Section"
        else:
            node_type = "Subsection"
        nodes.append(GraphNode(
            id=section.id, type=node_type, name=section.title,
            properties={"doc_id": doc.doc_id, "doc_type": doc.doc_type,
                        "version": doc.version, "number": section.number,
                        "line_start": section.line_start, "line_end": section.line_end,
                        "page": section.page},
        ))
        edges.append(GraphEdge(section.id, section.parent_id or doc.doc_id, "partOf"))
        if section.number:
            id_by_number[section.number] = section.id

    for table in doc.tables:
        nodes.append(GraphNode(
            id=table.id, type="Table", name=table.caption,
            properties={"doc_id": doc.doc_id, "doc_type": doc.doc_type,
                        "version": doc.version, "section_id": table.section_id,
                        "markdown": table.markdown},
        ))
        edges.append(GraphEdge(table.section_id, table.id, "hasTable"))

    for figure in doc.figures:
        nodes.append(GraphNode(
            id=figure.id, type="Figure", name=figure.caption,
            properties={"doc_id": doc.doc_id, "doc_type": doc.doc_type,
                        "version": doc.version, "section_id": figure.section_id,
                        "image_path": figure.image_path},
        ))
        edges.append(GraphEdge(figure.section_id, figure.id, "hasFigure"))

    for ref in doc.crossrefs:
        if ref.target_kind == "section" and ref.target_ref in id_by_number:
            edges.append(GraphEdge(ref.source_section_id, id_by_number[ref.target_ref],
                                   "references", {"raw": ref.raw}))
    return nodes, edges


def _split(text, max_chars):
    if len(text) <= max_chars:
        return [text]
    pieces, current, size = [], [], 0
    for para in text.split("\n\n"):
        if size + len(para) > max_chars and current:
            pieces.append("\n\n".join(current))
            current, size = [], 0
        current.append(para)
        size += len(para) + 2
    if current:
        pieces.append("\n\n".join(current))
    return pieces


def build_chunks(doc, *, max_chars=None):
    """§6.1 chunking: one chunk per section, tables chunked separately (§14.12)."""
    max_chars = max_chars or config.CHUNK_MAX_CHARS
    tables_by_section: dict[str, list] = {}
    for table in doc.tables:
        tables_by_section.setdefault(table.section_id, []).append(table)

    chunks = []

    def _meta(section, kind, **extra):
        return {"doc_id": doc.doc_id, "doc_type": doc.doc_type, "version": doc.version,
                "path": doc.path, "section": section.number or section.title,
                "section_id": section.id, "title": section.title, "kind": kind,
                "page": section.page, "doc_title": doc.title, **extra}

    for section in doc.sections:
        content_hash = section_hash(section)
        body = section.text.strip()
        if body:
            header = f"[{doc.title} §{section.number} {section.title}]"
            for i, piece in enumerate(_split(body, max_chars)):
                chunks.append({
                    "id": f"{section.id}::s{i}",
                    "text": f"{header}\n{piece}",
                    "metadata": _meta(section, "section", content_hash=content_hash),
                })
        for table in tables_by_section.get(section.id, []):
            # §14.12: tables embed poorly inside prose, so they get their own
            # chunk with the caption prepended for lexical findability.
            chunks.append({
                "id": f"{table.id}::t",
                "text": f"{table.caption}\n\n{table.markdown}".strip(),
                "metadata": _meta(section, "table", table_id=table.id,
                                  content_hash=content_hash),
            })
    return chunks


async def ingest_document(path, *, doc_id, title, doc_type, version,
                          vector_store, graph_store, manifest,
                          extract=False, figures=False, embed_fn=None,
                          embed_batch=64):
    from qa import llm

    t0 = time.time()
    embed_fn = embed_fn or llm.embed
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    doc = parse_markdown(text, doc_id=doc_id, title=title, doc_type=doc_type,
                         version=version, path=str(path))
    stats = IngestStats(doc_id=doc_id, sections=len(doc.sections),
                        tables=len(doc.tables), figures=len(doc.figures))

    nodes, edges = build_skeleton(doc)
    graph_store.add_nodes(nodes)
    graph_store.add_edges(edges)
    stats.edges = len(edges)

    chunks = build_chunks(doc, max_chars=config.CHUNK_MAX_CHARS)
    changed_sections: set[str] = set()
    fresh = []
    for chunk in chunks:
        sid = chunk["metadata"]["section_id"]
        content_hash = chunk["metadata"]["content_hash"]
        if manifest.hash_of(sid) == content_hash and vector_store.get(chunk["id"]) is not None:
            continue  # §5.5: unchanged section, already embedded — skip the cost
        fresh.append(chunk)
        changed_sections.add(sid)

    for start in range(0, len(fresh), embed_batch):
        batch = fresh[start : start + embed_batch]
        vectors = await embed_fn([c["text"] for c in batch])
        vector_store.upsert([
            VectorRecord(id=c["id"], text=c["text"], embedding=v, metadata=c["metadata"])
            for c, v in zip(batch, vectors)
        ])

    for chunk in chunks:
        manifest.set(chunk["metadata"]["section_id"], chunk["metadata"]["content_hash"])

    removed = manifest.prune(doc_id, {s.id for s in doc.sections})
    if removed:
        # Chunk ids are section-id-prefixed, so a dropped section's chunks go too.
        prefixes = tuple(removed)
        stale_chunk_ids = [c["id"] for c in chunks if c["id"].startswith(prefixes)]
        vector_store.delete(list(removed) + stale_chunk_ids)

    stats.chunks = len(chunks)
    stats.sections_changed = len(changed_sections)
    stats.sections_skipped = len({c["metadata"]["section_id"] for c in chunks}) - len(changed_sections)

    if extract or figures:
        from qa.ingest.extract import enrich

        stats.entities = await enrich(
            doc, graph_store=graph_store,
            sections=[s for s in doc.sections if s.id in changed_sections],
            do_entities=extract, do_figures=figures,
        )

    manifest.save()
    vector_store.persist()
    stats.elapsed_ms = int((time.time() - t0) * 1000)
    return stats
