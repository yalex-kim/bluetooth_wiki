"""v1 — ripgrep-backed ranked lexical search.

Improvements over v0's substring scan:
* multi-term queries (each term searched independently, not one literal string)
* ranking by term coverage, match volume, and term proximity
* exact-phrase bonus when the full query matches literally
* line-accurate hits (file + line number + matched-line snippet)
"""

from __future__ import annotations

import math
import re
from collections import defaultdict
from pathlib import Path

from agent.config import REPO_ROOT, SEARCH_RESULT_LIMIT, SEARCH_SNIPPET_CHARS, SOURCES_DIR, WIKI_DIR

from .base import SearchHit, SearchResult
from .rg_util import rg_search
from .index_store import load_index

_STOPWORDS = frozenset(
    "a an and are as at be by for from has have how in is it its of on or that the this to was what when where which with".split()
)

_TERM_RE = re.compile(r"[A-Za-z0-9_]+(?:\.[0-9]+)*")

# Matches sources/specs/<version>/Core_v<version>.md exactly (the \1
# backreference forces the dir version and filename version to be identical,
# and the anchored .md$ excludes .p4l/.p4l2 test-conversion variants).
_CORE_SPEC_RE = re.compile(r"sources/specs/([^/]+)/Core_v\1\.md$")


def _chunk_for(path, line, version_memo):
    """Chunk containing `line` if `path` is an indexed Core spec source, else None.

    `version_memo` caches path -> spec-version (or None) so the resolve/regex
    runs once per file rather than once per match line.
    """
    if path not in version_memo:
        try:
            rel = path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
        except ValueError:
            rel = path.as_posix()
        m = _CORE_SPEC_RE.search(rel)
        version_memo[path] = m.group(1) if m else None
    version = version_memo[path]
    if version is None:
        return None
    idx = load_index(version)
    if idx is None:
        return None
    return idx.find_chunk_for_line(line)


def tokenize(query: str) -> list[str]:
    """Split a query into searchable terms, dropping stopwords and dupes."""
    terms: list[str] = []
    for m in _TERM_RE.finditer(query):
        t = m.group(0)
        if t.lower() in _STOPWORDS or len(t) < 2:
            continue
        if t.lower() not in (x.lower() for x in terms):
            terms.append(t)
    return terms[:8]  # bound the number of rg invocations


def scope_roots(scope: str) -> list[Path]:
    roots: list[Path] = []
    if scope in ("wiki", "both"):
        roots.append(WIKI_DIR)
    if scope in ("sources", "both"):
        roots.append(SOURCES_DIR)
    return roots


def ranked_rg_search(
    query: str,
    roots: list[Path],
    *,
    limit: int = SEARCH_RESULT_LIMIT,
    source_tag: str = "ripgrep-wiki",
) -> list[SearchHit]:
    """Core v1 ranking logic, reused by v2 for its source-corpus lexical arm."""
    terms = tokenize(query)
    if not terms:
        return []

    version_memo: dict[Path, str | None] = {}
    # bucket key = (path, chunk_id or None); remember the resolved chunk per bucket.
    per_bucket: dict[tuple[Path, str | None], dict[str, list[tuple[int, str]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    bucket_chunk: dict[tuple[Path, str | None], object] = {}
    for term in terms:
        for m in rg_search(term, roots):
            chunk = _chunk_for(m.path, m.line_number, version_memo)
            key = (m.path, chunk.id if chunk else None)
            per_bucket[key][term].append((m.line_number, m.line_text))
            bucket_chunk.setdefault(key, chunk)

    # Exact-phrase pass (multi-word queries only) for a strong precision boost.
    phrase_buckets: dict[tuple[Path, str | None], tuple[int, str]] = {}
    if len(terms) > 1 and len(query.strip()) > 3:
        for m in rg_search(query.strip(), roots):
            chunk = _chunk_for(m.path, m.line_number, version_memo)
            key = (m.path, chunk.id if chunk else None)
            phrase_buckets.setdefault(key, (m.line_number, m.line_text))

    hits: list[SearchHit] = []
    for key, term_map in per_bucket.items():
        path, _chunk_id = key
        coverage = len(term_map) / len(terms)
        total_matches = sum(len(v) for v in term_map.values())
        score = 3.0 * coverage + 0.3 * math.log1p(total_matches)

        # Proximity: reward distinct terms co-occurring within a few lines.
        all_lines = sorted({ln for pairs in term_map.values() for ln, _ in pairs})
        best_line, best_density = all_lines[0], 1
        if len(term_map) > 1:
            for ln in all_lines:
                density = sum(
                    1 for pairs in term_map.values() if any(abs(line - ln) <= 3 for line, _ in pairs)
                )
                if density > best_density:
                    best_density, best_line = density, ln
            if best_density >= 2:
                score += 0.8 * (best_density / len(terms))
        if key in phrase_buckets:
            score += 2.0
            best_line = phrase_buckets[key][0]

        # Snippet: the densest matched line (falls back to first match / phrase).
        line_text = ""
        for pairs in term_map.values():
            for ln, text in pairs:
                if ln == best_line:
                    line_text = text
                    break
            if line_text:
                break
        if not line_text and key in phrase_buckets:
            line_text = phrase_buckets[key][1]
        snippet = line_text.strip()[:SEARCH_SNIPPET_CHARS]

        hit = SearchHit(
            file_path=path.resolve().relative_to(REPO_ROOT.resolve()).as_posix(),
            snippet=snippet,
            score=round(score, 4),
            line_start=best_line,
            line_end=best_line,
            source_tag=source_tag,
        )
        chunk = bucket_chunk.get(key)
        if chunk is not None:
            # Chunk-resolved source hit: attach Vol/Part/§ citation metadata and
            # widen the line span to the chunk (matched line stays as snippet).
            hit.version = chunk.version
            hit.vol = chunk.vol
            hit.part = chunk.part
            hit.section = chunk.section
            hit.heading_title = chunk.heading_title
            hit.chunk_id = chunk.id
            hit.line_start = chunk.line_start
            hit.line_end = chunk.line_end
            if not snippet:
                hit.snippet = " ".join(chunk.text.split())[:SEARCH_SNIPPET_CHARS]
        hits.append(hit)

    hits.sort(key=lambda h: (-h.score, h.file_path, h.line_start or 0))
    return hits[:limit]


class V1Ripgrep:
    name = "v1"

    async def search(self, query: str, scope: str = "both", *, question: str | None = None) -> SearchResult:
        query = (query or "").strip()
        scope = (scope or "both").lower()
        if scope not in ("wiki", "sources", "both"):
            scope = "both"
        result = SearchResult(query=query, scope=scope)
        if not query:
            result.notes.append("Error: 'query' is required.")
            return result
        result.hits = ranked_rg_search(query, scope_roots(scope), source_tag="ripgrep-wiki")
        return result
