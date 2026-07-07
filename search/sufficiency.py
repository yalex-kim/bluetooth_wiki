"""Agentic sufficiency judge for the v2 search pipeline.

A cheap/fast model (Haiku-class, distinct from the main answering model) looks
at the question plus previews of the current hits and decides whether they are
enough to answer — optionally proposing a reformulated query for the next
retrieval pass. Zero hits short-circuit to "insufficient" without an LLM call.
"""

from __future__ import annotations

from dataclasses import dataclass

from agent.config import SUFFICIENCY_MODEL
from agent.json_extract import extract_json_payload
from agent.llm import get_client

from .base import SearchHit

_MAX_PREVIEW_HITS = 10

_SYSTEM = (
    "You judge whether search results are sufficient to answer a question about "
    "Bluetooth Core Specifications.\n"
    "Sufficient means: the snippets (plus the pages they point to) plausibly contain "
    "the specific facts, numbers, or procedures the question asks for.\n"
    "Insufficient means: the results are off-topic, too generic, or clearly missing "
    "the asked-for detail (e.g. exact opcodes, PDU names, parameter ranges).\n"
    "Return ONLY a JSON object:\n"
    '{"sufficient": <bool>, "reason": "<one sentence>", "reformulated_query": <string or null>}\n'
    "Set reformulated_query only when insufficient AND you can propose a better search "
    "string (more specific spec terminology, exact feature/PDU/command names)."
)


@dataclass
class SufficiencyVerdict:
    sufficient: bool
    reason: str
    reformulated_query: str | None = None
    llm_called: bool = False


def _render_previews(hits: list[SearchHit]) -> str:
    lines = []
    for h in hits[:_MAX_PREVIEW_HITS]:
        loc = f" [Vol {h.vol}, Part {h.part}, §{h.section}]" if h.vol and h.part else ""
        lines.append(f"- {h.file_path}{loc}: {h.snippet[:160]}")
    return "\n".join(lines)


async def check_sufficiency(
    question: str,
    query: str,
    hits: list[SearchHit],
    *,
    model: str = SUFFICIENCY_MODEL,
) -> SufficiencyVerdict:
    if not hits:
        return SufficiencyVerdict(sufficient=False, reason="no hits at all", llm_called=False)

    client = get_client()
    user = (
        f"## Question\n{question or query}\n\n"
        f"## Search query used\n{query}\n\n"
        f"## Current results ({len(hits)} hits, top {min(len(hits), _MAX_PREVIEW_HITS)} shown)\n"
        f"{_render_previews(hits)}"
    )
    resp = await client.chat.completions.create(
        model=model,
        max_tokens=300,
        messages=[{"role": "system", "content": _SYSTEM}, {"role": "user", "content": user}],
    )
    text = resp.choices[0].message.content or ""
    data = extract_json_payload(text) or {}
    reformulated = data.get("reformulated_query")
    if isinstance(reformulated, str):
        reformulated = reformulated.strip() or None
    else:
        reformulated = None
    return SufficiencyVerdict(
        sufficient=bool(data.get("sufficient", True)),  # parse failure → assume sufficient (fail open, no loop)
        reason=str(data.get("reason", ""))[:300],
        reformulated_query=reformulated,
        llm_called=True,
    )
