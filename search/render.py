"""Render SearchResult into the text envelope the agent tool returns.

The envelope shape is the contract the system prompt and eval comparisons
rely on: header line, then '### {path}' blocks with snippets. v0 output is
byte-identical to the pre-refactor ``_search_wiki``; richer strategies add
vol/part/section context to the block header so the agent can cite precisely.
"""

from __future__ import annotations

from .base import SearchResult


def render_result(result: SearchResult) -> str:
    if result.notes and not result.hits and any(n.startswith("Error:") for n in result.notes):
        return "\n".join(result.notes)
    if not result.hits:
        lines = [f"No matches for {result.query!r} in scope={result.scope!r}."]
        lines += result.notes
        return "\n".join(lines)

    lines = [f"Found {len(result.hits)} match(es) for {result.query!r} in scope={result.scope!r}:", ""]
    for hit in result.hits:
        header = f"### {hit.file_path}"
        ctx: list[str] = []
        if hit.vol and hit.part:
            section = f", §{hit.section}" if hit.section else ""
            ctx.append(f"Vol {hit.vol}, Part {hit.part}{section}")
        if hit.heading_title:
            ctx.append(hit.heading_title)
        if hit.line_start and hit.line_end and hit.line_end != hit.line_start:
            ctx.append(f"lines {hit.line_start}-{hit.line_end}")
        elif hit.line_start:
            ctx.append(f"line {hit.line_start}")
        if ctx:
            header += f"  [{' — '.join(ctx)}]"
        lines.append(header)
        lines.append(hit.snippet)
        lines.append("")
    for note in result.notes:
        lines.append(f"note: {note}")
    return "\n".join(lines)
