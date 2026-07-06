"""v2 — tiered hybrid search with an agentic sufficiency loop.

Pipeline (all inside ONE search_wiki tool call, so the main agent's turn
budget is untouched):

    iter 0: v1 ripgrep over wiki/            → sufficiency check → done if OK
    iter 1: hybrid over sources/specs        → sufficiency check → done if OK
            (ripgrep-source + vector-source, RRF-fused, chunk-resolved)
    iter 2: one more hybrid pass with the judge's reformulated query
            → return best-effort regardless of verdict (hard stop)

Source hits are resolved to chunker chunks so they carry Vol/Part/§ metadata
for precise citations. The vector arm degrades gracefully (note in output)
when the embedding index or sentence-transformers is unavailable.
"""

from __future__ import annotations

import re

from agent.config import RRF_K, SEARCH_RESULT_LIMIT, SEARCH_SNIPPET_CHARS, SOURCES_DIR, SUFFICIENCY_MAX_ITER

from .base import SearchHit, SearchResult
from .fusion import reciprocal_rank_fusion
from .index_store import available_versions, load_index
from .sufficiency import SufficiencyVerdict, check_sufficiency
from .v1_ripgrep import ranked_rg_search, scope_roots


async def _safe_sufficiency(question: str, query: str, hits: list[SearchHit], notes: list[str]) -> SufficiencyVerdict:
    """Sufficiency check that degrades instead of failing the whole search.

    If the judge model is unreachable (no API key, network error), fall back
    to a heuristic: non-empty hits are treated as sufficient (v1 behavior),
    empty hits as insufficient.
    """
    try:
        return await check_sufficiency(question, query, hits)
    except Exception as exc:
        note = f"sufficiency judge unavailable ({type(exc).__name__}); using hit-count heuristic"
        if note not in notes:
            notes.append(note)
        return SufficiencyVerdict(sufficient=bool(hits), reason="heuristic fallback", llm_called=False)

_SOURCE_TOPK = 30  # per retrieval arm, pre-fusion

_VERSION_RE = re.compile(r"\b([456]\.\d)\b")


def _versions_for(query: str, question: str | None) -> list[str]:
    """Spec versions to search: any mentioned in the query/question, else the
    latest indexed version (most questions concern current behavior)."""
    indexed = available_versions()
    if not indexed:
        return []
    mentioned = set(_VERSION_RE.findall(query)) | set(_VERSION_RE.findall(question or ""))
    hits = sorted(v for v in mentioned if v in indexed)
    return hits or [indexed[-1]]


def _hit_from_chunk(chunk, score: float, tag: str) -> SearchHit:
    snippet = " ".join(chunk.text.split())[:SEARCH_SNIPPET_CHARS]
    return SearchHit(
        file_path=f"sources/specs/{chunk.version}/Core_v{chunk.version}.md",
        snippet=snippet,
        score=score,
        version=chunk.version,
        vol=chunk.vol,
        part=chunk.part,
        section=chunk.section,
        heading_title=chunk.heading_title,
        line_start=chunk.line_start,
        line_end=chunk.line_end,
        source_tag=tag,
        chunk_id=chunk.id,
    )


def _rg_source_arm(query: str, versions: list[str]) -> list[SearchHit]:
    """Lexical arm: rg over the version's Core spec, hits resolved to chunks."""
    roots = [SOURCES_DIR / "specs" / v for v in versions]
    line_hits = ranked_rg_search(query, roots, limit=_SOURCE_TOPK, source_tag="ripgrep-source")
    out: list[SearchHit] = []
    seen: set[str] = set()
    for h in line_hits:
        m = re.search(r"sources/specs/([^/]+)/Core_v", h.file_path)
        idx = load_index(m.group(1)) if m else None
        if idx and h.line_start:
            chunk = idx.find_chunk_for_line(h.line_start)
            if chunk:
                if chunk.id in seen:
                    continue
                seen.add(chunk.id)
                ch = _hit_from_chunk(chunk, h.score, "ripgrep-source")
                ch.snippet = h.snippet or ch.snippet  # keep the matched line as snippet
                out.append(ch)
                continue
        out.append(h)  # no index for this version → raw line hit (still usable)
    return out


def _vector_source_arm(query: str, versions: list[str]) -> tuple[list[SearchHit], str | None]:
    """Semantic arm: cosine top-k over the chunk embedding index."""
    from .embeddings import embedding_available

    if not embedding_available():
        return [], "vector arm skipped: sentence-transformers not installed"
    from .embeddings import cosine_topk, encode

    hits: list[SearchHit] = []
    missing: list[str] = []
    qv = None
    for v in versions:
        idx = load_index(v)
        if idx is None or idx.matrix is None:
            missing.append(v)
            continue
        if qv is None:
            qv = encode([query], is_query=True)[0]
        for i, score in cosine_topk(qv, idx.matrix, _SOURCE_TOPK):
            hits.append(_hit_from_chunk(idx.chunks[i], round(score, 4), "vector-source"))
    hits.sort(key=lambda h: -h.score)
    note = f"vector arm skipped for {missing} (no embedding index; run scripts/build_search_index.py)" if missing else None
    return hits[:_SOURCE_TOPK], note


class V2Hybrid:
    name = "v2"

    async def search(self, query: str, scope: str = "both", *, question: str | None = None) -> SearchResult:
        query = (query or "").strip()
        scope = (scope or "both").lower()
        if scope not in ("wiki", "sources", "both"):
            scope = "both"
        result = SearchResult(query=query, scope=scope)
        if not query:
            result.notes.append("Error: 'query' is required.")
            return result

        meta = result.meta
        meta["fallback_triggered"] = False
        meta["sufficiency_iterations"] = 0
        meta["sufficiency_llm_calls"] = 0

        # ── iter 0: fast wiki tier ────────────────────────────────────
        wiki_hits = ranked_rg_search(query, scope_roots("wiki"), source_tag="ripgrep-wiki")
        if scope == "sources":
            wiki_hits = []  # agent explicitly asked for source text only
        verdict = await _safe_sufficiency(question or query, query, wiki_hits, result.notes)
        meta["sufficiency_iterations"] = 1
        meta["sufficiency_llm_calls"] += int(verdict.llm_called)
        if verdict.sufficient and scope != "sources":
            result.hits = wiki_hits
            return result

        # ── iter 1..N: hybrid source fallback ─────────────────────────
        meta["fallback_triggered"] = True
        versions = _versions_for(query, question)
        cur_query = query
        best_hits: list[SearchHit] = wiki_hits
        for it in range(max(1, SUFFICIENCY_MAX_ITER)):
            rg_hits = _rg_source_arm(cur_query, versions)
            vec_hits, vec_note = _vector_source_arm(cur_query, versions)
            if vec_note and vec_note not in result.notes:
                result.notes.append(vec_note)
            fused = reciprocal_rank_fusion([rg_hits, vec_hits], k=RRF_K)[:SEARCH_RESULT_LIMIT]

            # Keep the strongest wiki context alongside source hits (wiki pages
            # remain the preferred citation entry point when they cover the topic).
            combined = (fused + [h for h in wiki_hits[:5] if h.key() not in {f.key() for f in fused}])[:SEARCH_RESULT_LIMIT]
            best_hits = combined

            is_last = it == max(1, SUFFICIENCY_MAX_ITER) - 1
            if is_last:
                break
            verdict = await _safe_sufficiency(question or query, cur_query, combined, result.notes)
            meta["sufficiency_iterations"] += 1
            meta["sufficiency_llm_calls"] += int(verdict.llm_called)
            if verdict.sufficient:
                break
            if verdict.reformulated_query and verdict.reformulated_query.lower() != cur_query.lower():
                cur_query = verdict.reformulated_query
                result.notes.append(f"query reformulated to: {cur_query!r}")
            else:
                break  # judge unhappy but has no better idea → stop spending

        result.hits = best_hits
        if meta["fallback_triggered"] and any(h.source_tag in ("vector-source", "ripgrep-source", "fused") for h in best_hits):
            vlist = ", ".join(versions)
            result.notes.append(
                f"wiki coverage was thin for this query; expanded to source spec(s) {vlist} via hybrid (ripgrep+vector, RRF) search"
            )
        return result
