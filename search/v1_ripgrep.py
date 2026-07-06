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

_STOPWORDS = frozenset(
    "a an and are as at be by for from has have how in is it its of on or that the this to was what when where which with".split()
)

_TERM_RE = re.compile(r"[A-Za-z0-9_]+(?:\.[0-9]+)*")


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

    # file -> term -> [(line_number, line_text)]
    per_file: dict[Path, dict[str, list[tuple[int, str]]]] = defaultdict(lambda: defaultdict(list))
    for term in terms:
        for m in rg_search(term, roots):
            per_file[m.path][term].append((m.line_number, m.line_text))

    # Exact-phrase pass (multi-word queries only) for a strong precision boost.
    phrase_files: dict[Path, tuple[int, str]] = {}
    if len(terms) > 1 and len(query.strip()) > 3:
        for m in rg_search(query.strip(), roots):
            phrase_files.setdefault(m.path, (m.line_number, m.line_text))

    hits: list[SearchHit] = []
    for path, term_map in per_file.items():
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
        if path in phrase_files:
            score += 2.0
            best_line = phrase_files[path][0]

        # Snippet: the densest matched line (falls back to first match).
        line_text = ""
        for pairs in term_map.values():
            for ln, text in pairs:
                if ln == best_line:
                    line_text = text
                    break
            if line_text:
                break
        if not line_text and path in phrase_files:
            line_text = phrase_files[path][1]
        snippet = line_text.strip()[:SEARCH_SNIPPET_CHARS]

        hits.append(
            SearchHit(
                file_path=path.resolve().relative_to(REPO_ROOT.resolve()).as_posix(),
                snippet=snippet,
                score=round(score, 4),
                line_start=best_line,
                line_end=best_line,
                source_tag=source_tag,
            )
        )

    hits.sort(key=lambda h: (-h.score, h.file_path))
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
