import pytest

from qa.ingest import pipeline
from qa.ingest.structure import parse_markdown
from qa.store.graph_sqlite import SqliteGraphStore
from qa.store.vector_local import LocalVectorStore

DOC = """# Core

## 4 LINK LAYER

Body of chapter four. See Section 4.5 for details.

### 4.5 CONNECTION STATE

Connection state body.

| Parameter | Min |
|---|---|
| connInterval | 7.5 ms |

Table 4.1: Connection parameters
"""


async def _fake_embed(texts):
    # deterministic 4-dim stand-in: no endpoint needed in tests
    return [[float(len(t) % 7), 1.0, 0.0, 0.0] for t in texts]


def _parsed():
    return parse_markdown(DOC, doc_id="core-6.0", title="Core 6.0",
                          doc_type="Core", version="6.0")


def test_skeleton_nodes_mirror_the_document_structure():
    nodes, edges = pipeline.build_skeleton(_parsed())
    kinds = {n.type for n in nodes}
    assert {"Document", "Section", "Table"} <= kinds
    partof = {(e.source, e.target) for e in edges if e.type == "partOf"}
    section_ids = {n.id for n in nodes if n.type == "Section"}
    assert any(src in section_ids for src, _ in partof)
    assert any(e.type == "references" for e in edges)
    assert any(e.type == "hasTable" for e in edges)


def test_tables_become_their_own_chunk_with_caption_prepended():
    chunks = pipeline.build_chunks(_parsed(), max_chars=3000)
    tables = [c for c in chunks if c["metadata"]["kind"] == "table"]
    assert len(tables) == 1
    assert "Table 4.1" in tables[0]["text"] and "connInterval" in tables[0]["text"]


def test_every_chunk_carries_scope_metadata_for_filtering():
    for chunk in pipeline.build_chunks(_parsed(), max_chars=3000):
        md = chunk["metadata"]
        assert md["doc_type"] == "Core" and md["version"] == "6.0"
        assert md["section"] and md["content_hash"]


@pytest.mark.asyncio
async def test_ingest_populates_both_stores(tmp_path):
    vec = LocalVectorStore(tmp_path / "vec")
    graph = SqliteGraphStore(":memory:")
    manifest = pipeline.Manifest(tmp_path / "manifest.json")
    src = tmp_path / "Core_v6.0.md"
    src.write_text(DOC, encoding="utf-8")

    stats = await pipeline.ingest_document(
        src, doc_id="core-6.0", title="Core 6.0", doc_type="Core", version="6.0",
        vector_store=vec, graph_store=graph, manifest=manifest, embed_fn=_fake_embed,
    )
    assert stats.chunks > 0 and vec.count() == stats.chunks
    assert graph.lookup("CONNECTION STATE")
    graph.close()


@pytest.mark.asyncio
async def test_reingest_only_embeds_changed_sections(tmp_path):
    vec = LocalVectorStore(tmp_path / "vec")
    graph = SqliteGraphStore(":memory:")
    manifest = pipeline.Manifest(tmp_path / "manifest.json")
    src = tmp_path / "Core_v6.0.md"
    src.write_text(DOC, encoding="utf-8")
    common = dict(doc_id="core-6.0", title="Core 6.0", doc_type="Core", version="6.0",
                  vector_store=vec, graph_store=graph, manifest=manifest,
                  embed_fn=_fake_embed)

    first = await pipeline.ingest_document(src, **common)
    second = await pipeline.ingest_document(src, **common)
    assert second.sections_changed == 0
    assert second.sections_skipped == first.sections_changed

    src.write_text(DOC.replace("Connection state body.", "Connection state body, revised."),
                   encoding="utf-8")
    third = await pipeline.ingest_document(src, **common)
    assert third.sections_changed == 1
    graph.close()
