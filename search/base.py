"""Core datatypes for the pluggable search strategies.

Every strategy (v0 naive, v1 ripgrep, v2 hybrid) implements the same
``SearchStrategy`` protocol and returns a ``SearchResult`` so the agent's
``search_wiki`` tool can swap strategies without changing its contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@dataclass
class SearchHit:
    """One ranked search result.

    ``vol``/``part``/``section`` are populated for source-spec hits that were
    resolved to a chunk, so the agent can emit precise
    ``[Core X.Y, Vol N, Part P, §S]`` citations. Wiki hits carry only
    ``file_path`` + ``snippet`` (matching the v0 output shape).
    """

    file_path: str  # repo-relative posix path
    snippet: str
    score: float = 0.0
    version: str | None = None
    vol: str | None = None
    part: str | None = None
    section: str | None = None
    heading_title: str | None = None
    line_start: int | None = None  # 1-based, inclusive
    line_end: int | None = None  # 1-based, inclusive
    source_tag: str = ""  # "naive" | "ripgrep-wiki" | "ripgrep-source" | "vector-source" | "fused"
    chunk_id: str | None = None

    def key(self) -> str:
        """Identity used for RRF fusion / de-duplication."""
        if self.chunk_id:
            return self.chunk_id
        if self.line_start is not None:
            # Bucket nearby line hits in the same file together.
            return f"{self.file_path}:{self.line_start // 40}"
        return self.file_path


@dataclass
class SearchResult:
    """Hits plus strategy-level annotations rendered into the tool output."""

    query: str
    scope: str
    hits: list[SearchHit] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    meta: dict = field(default_factory=dict)  # e.g. {"fallback_triggered": True, "sufficiency_iterations": 2}


@runtime_checkable
class SearchStrategy(Protocol):
    name: str

    async def search(self, query: str, scope: str = "both", *, question: str | None = None) -> SearchResult:
        """Run the strategy. ``question`` is the user's original question when
        available (used by v2's sufficiency judge); ``query`` is the search string."""
        ...
