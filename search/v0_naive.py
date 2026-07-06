"""v0 — the original naive substring scan, relocated verbatim from agent/tools.py.

Kept unchanged as the baseline/control strategy for eval comparisons. The
rendered output (see search/render.py) is byte-identical to the pre-refactor
``_search_wiki`` tool output.
"""

from __future__ import annotations

from agent.config import REPO_ROOT, SEARCH_RESULT_LIMIT, SEARCH_SNIPPET_CHARS, SOURCES_DIR, WIKI_DIR

from .base import SearchHit, SearchResult


def iter_markdown(scope: str):
    if scope in ("wiki", "both"):
        yield from WIKI_DIR.rglob("*.md")
    if scope in ("sources", "both"):
        yield from SOURCES_DIR.rglob("*.md")


def make_snippet(text: str, query: str, span: int = SEARCH_SNIPPET_CHARS) -> str:
    lower = text.lower()
    q = query.lower()
    i = lower.find(q)
    if i < 0:
        return text[:span].strip()
    half = span // 2
    start = max(0, i - half)
    end = min(len(text), i + len(q) + half)
    snippet = text[start:end].replace("\n", " ").strip()
    if start > 0:
        snippet = "…" + snippet
    if end < len(text):
        snippet = snippet + "…"
    return snippet


class V0Naive:
    name = "v0"

    async def search(self, query: str, scope: str = "both", *, question: str | None = None) -> SearchResult:
        query = (query or "").strip()
        scope = (scope or "both").lower()
        if scope not in ("wiki", "sources", "both"):
            scope = "both"
        result = SearchResult(query=query, scope=scope)
        if not query:
            result.notes.append("Error: 'query' is required.")
            return result

        needle = query.lower()
        for path in iter_markdown(scope):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if needle not in text.lower():
                continue
            rel = path.relative_to(REPO_ROOT).as_posix()
            result.hits.append(SearchHit(file_path=rel, snippet=make_snippet(text, query), source_tag="naive"))
            if len(result.hits) >= SEARCH_RESULT_LIMIT:
                break
        return result
