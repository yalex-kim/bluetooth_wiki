import json
import shutil

import pytest

pytestmark = pytest.mark.skipif(
    shutil.which("rg") is None, reason="ripgrep (rg) not on PATH"
)


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_rg_source_arm_returns_chunk_resolved_hits(tmp_path, monkeypatch):
    from search import v1_ripgrep, v2_hybrid, index_store

    repo = tmp_path
    lines = [
        "# Core v9.9",                        # 1
        "The widget mechanism is described.",  # 2
        "filler", "filler", "filler",          # 3-5
        "filler", "filler",                    # 6-7
        "Another widget appears far below.",   # 8
        "end",                                 # 9
    ]
    _write(repo / "sources/specs/9.9/Core_v9.9.md", "\n".join(lines) + "\n")
    chunks = [
        {"id": "9.9:1:A:1:1", "version": "9.9", "vol": "1", "part": "A",
         "part_title": "Architecture", "section": "1", "heading_title": "Overview",
         "line_start": 1, "line_end": 5, "text": "The widget mechanism is described."},
        {"id": "9.9:6:B:4:6", "version": "9.9", "vol": "6", "part": "B",
         "part_title": "Link Layer", "section": "4", "heading_title": "Widgets",
         "line_start": 6, "line_end": 9, "text": "Another widget appears far below."},
    ]
    idx = repo / "search/index/9.9"
    idx.mkdir(parents=True, exist_ok=True)
    (idx / "chunks.jsonl").write_text(
        "\n".join(json.dumps(c) for c in chunks), encoding="utf-8"
    )

    monkeypatch.setattr(v1_ripgrep, "REPO_ROOT", repo)
    monkeypatch.setattr(v1_ripgrep, "SOURCES_DIR", repo / "sources")
    monkeypatch.setattr(v2_hybrid, "SOURCES_DIR", repo / "sources")
    monkeypatch.setattr(index_store, "SEARCH_INDEX_DIR", repo / "search" / "index")
    index_store._index_cache.clear()

    hits = v2_hybrid._rg_source_arm("widget", ["9.9"])

    ids = sorted(h.chunk_id for h in hits)
    assert ids == ["9.9:1:A:1:1", "9.9:6:B:4:6"]
    assert all(h.source_tag == "ripgrep-source" for h in hits)
    # No duplicate chunks.
    assert len(ids) == len(set(ids))
