import json
import shutil

import pytest

pytestmark = pytest.mark.skipif(
    shutil.which("rg") is None, reason="ripgrep (rg) not on PATH"
)


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _fake_repo(tmp_path):
    """A minimal repo tree: one Core spec source file + a 2-chunk index.

    'widget' appears at line 2 (Vol 1 Part A) and line 8 (Vol 6 Part B),
    which fall into two different chunks.
    """
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
    return repo


def _point_modules_at(repo, monkeypatch):
    from search import v1_ripgrep, index_store
    monkeypatch.setattr(v1_ripgrep, "REPO_ROOT", repo)
    monkeypatch.setattr(v1_ripgrep, "SOURCES_DIR", repo / "sources")
    monkeypatch.setattr(index_store, "SEARCH_INDEX_DIR", repo / "search" / "index")
    index_store._index_cache.clear()


def test_two_chunks_same_file_yield_two_hits(tmp_path, monkeypatch):
    from search import v1_ripgrep
    repo = _fake_repo(tmp_path)
    _point_modules_at(repo, monkeypatch)

    hits = v1_ripgrep.ranked_rg_search(
        "widget", [repo / "sources/specs/9.9"], source_tag="ripgrep-source"
    )

    assert len(hits) == 2
    by_id = {h.chunk_id: h for h in hits}
    assert sorted(by_id) == ["9.9:1:A:1:1", "9.9:6:B:4:6"]
    assert (by_id["9.9:1:A:1:1"].vol, by_id["9.9:1:A:1:1"].part) == ("1", "A")
    assert (by_id["9.9:6:B:4:6"].vol, by_id["9.9:6:B:4:6"].part) == ("6", "B")
    assert by_id["9.9:1:A:1:1"].version == "9.9"


def test_non_indexed_file_stays_single_hit(tmp_path, monkeypatch):
    from search import v1_ripgrep
    repo = tmp_path
    _write(repo / "wiki/concepts/foo.md",
           "widget here\n\n\n\n\n\n\n\nwidget again\n")
    _point_modules_at(repo, monkeypatch)

    hits = v1_ripgrep.ranked_rg_search(
        "widget", [repo / "wiki"], source_tag="ripgrep-wiki"
    )

    assert len(hits) == 1
    assert hits[0].chunk_id is None


def test_core_spec_variant_not_chunk_resolved(tmp_path, monkeypatch):
    # A same-directory conversion variant (Core_v9.9.p4l3.md) must NOT resolve
    # against the real spec's chunk index — the anchored _CORE_SPEC_RE rejects it.
    from search import v1_ripgrep
    repo = _fake_repo(tmp_path)
    _write(repo / "sources/specs/9.9/Core_v9.9.p4l3.md",
           "# variant\nThe widget mechanism (variant copy).\n")
    _point_modules_at(repo, monkeypatch)

    hits = v1_ripgrep.ranked_rg_search(
        "widget", [repo / "sources/specs/9.9"], source_tag="ripgrep-source"
    )

    by_file = {h.file_path: h for h in hits}
    variant = next(h for f, h in by_file.items() if f.endswith("Core_v9.9.p4l3.md"))
    assert variant.chunk_id is None
    # The real spec's matches still resolve to chunks.
    assert any(h.chunk_id is not None for h in hits)
