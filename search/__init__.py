"""Pluggable search strategies for the Bluetooth wiki agent.

Strategies:
  v0 — naive substring scan (the original baseline, unchanged)
  v1 — ripgrep-backed ranked lexical search
  v2 — v1 + agentic sufficiency check + hybrid (ripgrep+vector, RRF) source fallback
"""

from __future__ import annotations

from .base import SearchHit, SearchResult, SearchStrategy

__all__ = ["SearchHit", "SearchResult", "SearchStrategy", "get_strategy", "STRATEGY_NAMES"]

STRATEGY_NAMES = ("v0", "v1", "v2")

_instances: dict[str, SearchStrategy] = {}


def get_strategy(name: str) -> SearchStrategy:
    """Return the (cached) strategy instance for ``name`` ('v0' | 'v1' | 'v2')."""
    name = (name or "").strip().lower()
    if name not in STRATEGY_NAMES:
        raise ValueError(f"Unknown search strategy {name!r}; expected one of {STRATEGY_NAMES}")
    if name not in _instances:
        if name == "v0":
            from .v0_naive import V0Naive

            _instances[name] = V0Naive()
        elif name == "v1":
            from .v1_ripgrep import V1Ripgrep

            _instances[name] = V1Ripgrep()
        else:
            from .v2_hybrid import V2Hybrid

            _instances[name] = V2Hybrid()
    return _instances[name]
