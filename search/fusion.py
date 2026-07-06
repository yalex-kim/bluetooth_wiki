"""Reciprocal Rank Fusion of ranked hit lists.

Used by v2 to merge the ripgrep-source and vector-source ranked lists.
Deterministic: identical inputs always produce identical output order, which
keeps eval runs reproducible.
"""

from __future__ import annotations

from .base import SearchHit


def reciprocal_rank_fusion(ranked_lists: list[list[SearchHit]], k: int = 60) -> list[SearchHit]:
    """Fuse ranked lists: hit at 1-indexed rank r contributes 1/(k+r).

    Ties break by (1) number of lists the hit appeared in (hits found by both
    retrieval arms are preferred), (2) ascending line_start, (3) key string.
    """
    scores: dict[str, float] = {}
    appearances: dict[str, int] = {}
    best: dict[str, SearchHit] = {}

    for ranked in ranked_lists:
        for rank, hit in enumerate(ranked, start=1):
            key = hit.key()
            scores[key] = scores.get(key, 0.0) + 1.0 / (k + rank)
            appearances[key] = appearances.get(key, 0) + 1
            prev = best.get(key)
            # Keep the representative with the richest metadata (chunk hits
            # carry vol/part/section that plain rg line hits lack).
            if prev is None or (hit.chunk_id and not prev.chunk_id):
                best[key] = hit

    fused: list[SearchHit] = []
    for key, score in scores.items():
        hit = best[key]
        hit.score = round(score, 6)
        hit.source_tag = "fused" if appearances[key] > 1 else hit.source_tag
        fused.append(hit)

    fused.sort(
        key=lambda h: (
            -h.score,
            -appearances[h.key()],
            h.line_start if h.line_start is not None else 1 << 30,
            h.key(),
        )
    )
    return fused
