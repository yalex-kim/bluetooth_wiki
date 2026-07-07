"""Tools the agent loop can call.

The pure-logic helpers (``_list_index``, ``_search_wiki``, ``_read_page``,
``_read_source``) have no SDK dependency so they can be unit-tested against
real repo content. They produce plain strings; the caller wraps them in the
LLM client's expected format (OpenAI function schemas → handler map).

Search is pluggable: ``build_tools(strategy_name)`` wires the ``search_wiki``
tool to one of the strategies in the ``search`` package (v0 naive baseline /
v1 ripgrep / v2 hybrid+agentic). The tool's name, argument schema, and output
envelope are identical across strategies — only retrieval quality and latency
differ — so system_prompt.md and citations.py need no per-strategy changes.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

from .config import (
    INDEX_PATH,
    READ_PAGE_MAX_CHARS,
    REPO_ROOT,
    SEARCH_RESULT_LIMIT,
    SEARCH_SNIPPET_CHARS,
    SEARCH_STRATEGY,
    SOURCES_DIR,
    WIKI_DIR,
)


def _safe_path(rel: str) -> Path | None:
    rel = rel.lstrip("/")
    p = (REPO_ROOT / rel).resolve()
    try:
        p.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return None
    allowed_roots = (WIKI_DIR.resolve(), SOURCES_DIR.resolve())
    if p == INDEX_PATH.resolve():
        return p
    if not any(str(p).startswith(str(r)) for r in allowed_roots):
        return None
    if not p.is_file():
        return None
    return p


# ─── Pure-logic implementations (testable, no SDK required) ─────────────


def _list_index() -> str:
    return INDEX_PATH.read_text(encoding="utf-8")


def _search_wiki(query: str, scope: str = "both", strategy_name: str = SEARCH_STRATEGY) -> str:
    """Synchronous convenience wrapper (used by tests/scripts)."""
    return asyncio.run(_search_wiki_async(query, scope, strategy_name))


async def _search_wiki_async(query: str, scope: str = "both", strategy_name: str = SEARCH_STRATEGY) -> str:
    from search import get_strategy
    from search.render import render_result

    result = await get_strategy(strategy_name).search(query or "", scope or "both")
    return render_result(result)


def _read_page(path: str) -> str:
    p = _safe_path(path or "")
    if p is None:
        return f"Error: path {path!r} is not a readable wiki/source file."
    text = p.read_text(encoding="utf-8", errors="ignore")
    truncated = len(text) > READ_PAGE_MAX_CHARS
    if truncated:
        text = text[:READ_PAGE_MAX_CHARS] + f"\n\n…[truncated; full file is {len(text)} chars]"
    header = f"# {p.relative_to(REPO_ROOT).as_posix()}\n\n"
    return header + text


def _read_source(version: str, vol: str = "", part: str = "") -> str:
    """Read a Vol/Part slice of an original spec markdown.

    Part boundaries come from search.chunker's body-marker detection — the
    former '[Vol N]'/'Part X' tagged-heading walk only ever matched the
    front-matter acknowledgments and silently returned the wrong section.
    """
    from search.chunker import parse_part_spans, spec_path

    version = (version or "").strip()
    vol = (vol or "").strip()
    part = (part or "").strip().upper()
    if not version:
        return "Error: 'version' is required (e.g. '6.0')."

    path = spec_path(version)
    if not path.is_file():
        return f"No spec markdown found at {path.relative_to(REPO_ROOT).as_posix()}."
    text = path.read_text(encoding="utf-8", errors="ignore")
    spans = parse_part_spans(text)
    if not spans:
        return f"Could not detect Volume/Part structure in Core_v{version}.md."

    def _toc(rows) -> str:
        lines = [f"# Table of contents for Core_v{version}.md", ""]
        for s in rows:
            lines.append(f"- Vol {s.vol}, Part {s.part}: {s.part_title}  (lines {s.line_start + 1}-{s.line_end})")
        lines.append("")
        lines.append("Call read_source again with both 'vol' and 'part' to read a section.")
        return "\n".join(lines)

    if not vol and not part:
        return _toc(spans)
    if vol and not part:
        rows = [s for s in spans if s.vol == vol]
        return _toc(rows) if rows else f"No Vol {vol} found in v{version}."
    if part and not vol:
        rows = [s for s in spans if s.part == part]
        if not rows:
            return f"No Part {part} found in v{version}."
        if len(rows) > 1:
            return _toc(rows)
        vol = rows[0].vol

    span = next((s for s in spans if s.vol == vol and s.part == part), None)
    if span is None:
        return f"No 'Part {part}' found within Vol {vol} of v{version}."

    lines = text.split("\n")
    section = "\n".join(lines[span.line_start : span.line_end])
    if len(section) > READ_PAGE_MAX_CHARS:
        section = section[:READ_PAGE_MAX_CHARS] + f"\n\n…[truncated; full section is {len(section)} chars]"
    header = f"# sources/specs/{version}/Core_v{version}.md  (Vol {vol} Part {part}: {span.part_title})\n\n"
    return header + section


# ─── OpenAI function schema builders ────────────────────────────────────


def _fn(name: str, description: str, properties: dict, required: list[str]) -> dict:
    """Build an OpenAI function tool schema."""
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {"type": "object", "properties": properties, "required": required},
        },
    }


_LIST_INDEX = _fn(
    "list_index",
    "Read the wiki's index.md catalog. ALWAYS call this first to identify which pages are relevant.",
    {}, [],
)
_READ_PAGE = _fn(
    "read_page",
    "Read a wiki or source markdown file by repo-relative path "
    "(e.g. 'wiki/concepts/channel-sounding.md' or 'sources/specs/6.0/Core_v6.0.md'). "
    f"Truncated to {READ_PAGE_MAX_CHARS} characters; long source files should use read_source instead.",
    {"path": {"type": "string"}}, ["path"],
)
_READ_SOURCE = _fn(
    "read_source",
    "Read a slice of an original Bluetooth spec markdown. Provide 'version' (e.g. '6.0') "
    "plus 'vol' (e.g. '6') and 'part' (e.g. 'B') to read that Part's full text. "
    "Without vol/part, returns a table of contents of all Volumes/Parts.",
    {"version": {"type": "string"}, "vol": {"type": "string"}, "part": {"type": "string"}}, ["version"],
)


def build_tools(strategy_name: str = SEARCH_STRATEGY):
    """Return (openai_tool_schemas, name->async-handler) for the given strategy."""
    extra = " May take a few extra seconds when it expands into the original spec text." if strategy_name == "v2" else ""
    search_schema = _fn(
        "search_wiki",
        "Search wiki and/or original spec markdown for a query. "
        f"Returns up to {SEARCH_RESULT_LIMIT} hits with file paths and ~{SEARCH_SNIPPET_CHARS}-char snippets. "
        "scope: 'wiki' for curated content, 'sources' for original spec text, 'both' to search everything."
        + extra,
        {"query": {"type": "string"},
         "scope": {"type": "string", "enum": ["wiki", "sources", "both"]}},
        ["query"],
    )

    async def _h_list(args: dict) -> str:
        return _list_index()

    async def _h_search(args: dict) -> str:
        return await _search_wiki_async(args.get("query") or "", args.get("scope") or "both", strategy_name)

    async def _h_page(args: dict) -> str:
        return _read_page(args.get("path") or "")

    async def _h_source(args: dict) -> str:
        return _read_source(args.get("version") or "", args.get("vol") or "", args.get("part") or "")

    schemas = [_LIST_INDEX, search_schema, _READ_PAGE, _READ_SOURCE]
    handlers = {"list_index": _h_list, "search_wiki": _h_search, "read_page": _h_page, "read_source": _h_source}
    return schemas, handlers
