# Chunk-precise lexical search for Core spec source files

**Date**: 2026-07-06
**Status**: Approved

## Problem

`ranked_rg_search` (in `search/v1_ripgrep.py`) is the shared ripgrep-backed
ranking function used by both the v1 strategy directly and by v2's
`_rg_source_arm`. It aggregates every ripgrep match **per file** into a
single `SearchHit`.

This is fine for `wiki/` — pages are already one file per topic, so
file-level grouping and chunk-level grouping are the same thing. It breaks
down for `sources/specs/<version>/Core_v<version>.md`: a single Core spec
version is one 3,000-4,000 page markdown file. No matter how many distinct
Vol/Part sections match a query, `ranked_rg_search` can only ever return
**one** hit for that entire file — whichever line has the locally densest
term co-occurrence. Relevant matches elsewhere in the same file (a different
Volume, a different Part) are invisible to the caller.

`search/v2_hybrid.py::_rg_source_arm` already resolves a hit's line number to
a `chunker.Chunk` via `index_store.load_index(version).find_chunk_for_line()`
so it can attach Vol/Part/§ metadata for precise citations — but that
resolution is starved: it only ever receives the single file-level hit
`ranked_rg_search` produced, so multiple relevant chunks in the same spec
version can never surface even though the chunk-resolution machinery to
identify them already exists and works.

This is orthogonal to the RAG/embedding path: `chunker.py` +
`index_store.py` already do Vol/Part-aware chunking for the vector search
arm regardless of the underlying file being monolithic. The gap is
specifically in the lexical (ripgrep) arm's aggregation step.

## Goal

When a matched path is a Core spec source file with a built chunk index
(`search/index/<version>/chunks.jsonl`, produced by
`scripts/build_search_index.py` with or without `--chunks-only`), group and
rank matches **per (file, chunk)** instead of per file, so multiple relevant
Vol/Part sections in the same physical file can each surface as their own
ranked hit.

Files without a built chunk index (wiki pages, un-indexed spec versions,
profile/test-suite markdown under `sources/specs/profiles/` etc.) keep
exactly today's per-file behavior. This is purely additive — nothing that
isn't indexed today changes behavior.

## Non-goals

- No physical splitting of source markdown files by Vol/Part. The single
  large `Core_v<version>.md` file remains the one authoritative source file
  per version (per `CLAUDE.md`'s Layer 1 convention).
- No changes to `search/chunker.py`'s parsing logic or `search/index_store.py`'s
  on-disk format — both already expose everything this change needs
  (`chunk_core_spec`, `VersionIndex.find_chunk_for_line`).
- No changes to the embedding/vector arm (`embeddings.py`, `fusion.py`).
- No requirement to (re)build any index as part of this change. The existing
  graceful degradation ("no index → note recommending
  `scripts/build_search_index.py`") is preserved.

## Approach

Modify `ranked_rg_search` directly, reusing `index_store.load_index` /
`VersionIndex.find_chunk_for_line`.

Alternatives considered and rejected:

- **Post-process file-level hits into multiple chunk hits after the fact.**
  Infeasible — by the time `ranked_rg_search` collapses a file's matches down
  to one row (one `best_line`, one snippet), the per-line detail needed to
  identify other relevant chunks in that file is already discarded.
- **Drop file-level aggregation entirely; return raw per-line hits.** Would
  throw away the coverage/total-matches/proximity/phrase scoring that is v1's
  entire value-add over the v0 naive substring scan.

## Changes

### 1. `search/v1_ripgrep.py` — `ranked_rg_search`

- Add a helper that recognizes paths matching
  `sources/specs/<version>/Core_v<version>.md` **exactly** (anchored on the
  filename, so `.p4l.md` / `.p4l2.md` test-conversion variants living in the
  same directory never accidentally resolve against the real file's chunk
  index), loads that version's index via `load_index`, and resolves a given
  match line to its containing `Chunk` via `find_chunk_for_line`.
- Change the aggregation key used when building `per_file` from `path` to
  `(path, chunk_id or None)`. Every match line is resolved to a chunk (if an
  index exists for that path) before bucketing; paths with no index keep
  today's single whole-file bucket.
- Apply the existing per-bucket scoring formula (term coverage, total match
  count, proximity/density, exact-phrase bonus) to each `(path, chunk)`
  bucket independently, instead of once per file. This also improves the
  proximity signal itself: term density is now measured within one Vol/Part
  instead of across an entire multi-thousand-page file, so density no longer
  gets diluted (or falsely inflated) by unrelated matches elsewhere in the
  document.
- Exact-phrase bonus: currently `setdefault`'s the *first* phrase match found
  per file. Generalize to resolve each phrase match to its bucket and
  `setdefault` per `(path, chunk)` instead, so the bonus lands on the correct
  chunk when a phrase appears in more than one part of the same file.
- Populate `vol` / `part` / `section` / `heading_title` / `chunk_id` on the
  returned `SearchHit` whenever a chunk was resolved. Today only v2's
  post-hoc step sets these fields — v1 used directly with `scope=sources`
  (or `scope=both`) currently returns source hits with no citation metadata
  at all.

### 2. `search/v2_hybrid.py` — `_rg_source_arm`

- Remove the manual re-resolution loop (`load_index` +
  `find_chunk_for_line` + rebuilding the hit via `_hit_from_chunk`), since
  `ranked_rg_search` now returns hits that are already chunk-resolved when an
  index exists. Keep the existing semantics: dedup by `chunk_id` when
  present, and pass raw hits through unchanged when no index exists for that
  version (unresolved hits simply won't have a `chunk_id`, matching today's
  fallback behavior).

## Testing

There is no existing test suite for `search/`. Add a focused unit test for
the new bucketing behavior in `ranked_rg_search`: build a small
`chunks.jsonl` fixture (or a `--chunks-only` index over a small slice of a
real spec) containing two chunks that share a search term, and assert that
`ranked_rg_search` returns two distinct hits with correct `chunk_id` / `vol`
/ `part` — not one hit for the whole file.
