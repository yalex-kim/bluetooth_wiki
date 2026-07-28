"""§7.4 grounding check.

The model's citations are not trusted. Each claimed (doc, section) must match a
piece of evidence some action actually returned during this run. Matches are
enriched with the real page and path — so the Orchestrator gets a resolvable
pointer rather than the model's recollection of one — and non-matches are
dropped rather than shipped.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class VerifiedCitations:
    citations: list = field(default_factory=list)
    dropped: list = field(default_factory=list)


def _norm(value) -> str:
    """Collapse formatting noise: '§4.5' and '4.5' must compare equal."""
    return re.sub(r"[^a-z0-9.]+", "", str(value or "").lower())


def verify_citations(claimed, observed):
    index = {}
    for ev in observed:
        index.setdefault((_norm(ev.doc), _norm(ev.section)), ev)
        index.setdefault((None, _norm(ev.ref_id)), ev)

    result = VerifiedCitations()
    seen = set()
    for citation in claimed or []:
        match = (index.get((_norm(citation.get("doc")), _norm(citation.get("section"))))
                 or index.get((None, _norm(citation.get("ref_id")))))
        if match is None:
            result.dropped.append(dict(citation))
            continue
        key = (_norm(match.doc), _norm(match.section))
        if key in seen:
            continue
        seen.add(key)
        result.citations.append({"doc": match.doc, "section": match.section,
                                 "page": match.page, "path": match.path})
    return result
