"""Tools the agent loop can call.

The pure-logic helpers (``_list_index``, ``_search_wiki``, ``_read_page``,
``_read_source``) have no external dependencies so they can be unit-tested
against real repo content without booting the SDK. The SDK ``@tool``-decorated
wrappers below adapt them into the MCP-style content envelope Claude expects.
"""

from __future__ import annotations

import re
from pathlib import Path

from claude_agent_sdk import tool

from .config import (
    INDEX_PATH,
    READ_PAGE_MAX_CHARS,
    REPO_ROOT,
    SEARCH_RESULT_LIMIT,
    SEARCH_SNIPPET_CHARS,
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


def _iter_markdown(scope: str):
    if scope in ("wiki", "both"):
        yield from WIKI_DIR.rglob("*.md")
    if scope in ("sources", "both"):
        yield from SOURCES_DIR.rglob("*.md")


def _make_snippet(text: str, query: str, span: int = SEARCH_SNIPPET_CHARS) -> str:
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


# ─── Pure-logic implementations (testable, no SDK required) ─────────────


def _list_index() -> str:
    return INDEX_PATH.read_text(encoding="utf-8")


def _search_wiki(query: str, scope: str = "both") -> str:
    query = (query or "").strip()
    scope = (scope or "both").lower()
    if scope not in ("wiki", "sources", "both"):
        scope = "both"
    if not query:
        return "Error: 'query' is required."

    needle = query.lower()
    hits: list[tuple[str, str]] = []
    for path in _iter_markdown(scope):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if needle not in text.lower():
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        hits.append((rel, _make_snippet(text, query)))
        if len(hits) >= SEARCH_RESULT_LIMIT:
            break

    if not hits:
        return f"No matches for {query!r} in scope={scope!r}."

    lines = [f"Found {len(hits)} match(es) for {query!r} in scope={scope!r}:", ""]
    for rel, snippet in hits:
        lines.append(f"### {rel}")
        lines.append(snippet)
        lines.append("")
    return "\n".join(lines)


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
    version = (version or "").strip()
    vol = (vol or "").strip()
    part = (part or "").strip().upper()
    if not version:
        return "Error: 'version' is required (e.g. '6.0')."

    spec_path = SOURCES_DIR / "specs" / version / f"Core_v{version}.md"
    if not spec_path.is_file():
        return f"No spec markdown found at {spec_path.relative_to(REPO_ROOT).as_posix()}."
    text = spec_path.read_text(encoding="utf-8", errors="ignore")

    if not vol and not part:
        toc_lines = [f"# Table of contents for Core_v{version}.md", ""]
        toc_re = re.compile(r"^#{1,4}\s+.*(?:\[Vols?\b|\bPart\s+[A-Z]\b)", flags=re.IGNORECASE)
        for line in text.splitlines():
            if toc_re.match(line):
                toc_lines.append(line)
        if len(toc_lines) <= 2:
            toc_lines.append("(no Volume/Part headings detected)")
        return "\n".join(toc_lines)

    # Spec markdown nests Vol/Part hierarchically:
    #   ### 2.7 [Vol 6] Low Energy Controller
    #     #### 2.7.2 Part B: Link Layer Specification
    # so vol+part lookups must scope the part search to the vol's heading scope.
    lines = text.splitlines()
    # Use the bracketed singular form '[Vol N]' for content headings; this
    # avoids accidentally matching aggregate/version-history entries like
    # '[Vols 2, 3, 5, 6 & 7]' that contain the right number but no real content.
    vol_rx = re.compile(rf"\[Vol\s+{re.escape(vol)}\]", re.IGNORECASE) if vol else None
    part_rx = re.compile(rf"\bPart\s+{re.escape(part)}\b", re.IGNORECASE) if part else None

    def _heading_level(ln: str) -> int:
        return len(ln) - len(ln.lstrip("#"))

    start_idx = None
    if vol and part:
        vol_idx = next(
            (i for i, ln in enumerate(lines) if ln.startswith("#") and vol_rx.search(ln)),
            None,
        )
        if vol_idx is None:
            return f"No heading matching Vol {vol} in v{version}."
        vol_level = _heading_level(lines[vol_idx])
        for j in range(vol_idx + 1, len(lines)):
            ln = lines[j]
            if not ln.startswith("#"):
                continue
            if _heading_level(ln) <= vol_level:
                break
            if part_rx.search(ln):
                start_idx = j
                break
        if start_idx is None:
            return f"No 'Part {part}' heading found within Vol {vol} of v{version}."
    elif vol:
        start_idx = next(
            (i for i, ln in enumerate(lines) if ln.startswith("#") and vol_rx.search(ln)),
            None,
        )
        if start_idx is None:
            return f"No heading matching Vol {vol} in v{version}."
    else:
        start_idx = next(
            (i for i, ln in enumerate(lines) if ln.startswith("#") and part_rx.search(ln)),
            None,
        )
        if start_idx is None:
            return f"No heading matching Part {part} in v{version}."

    start_level = len(lines[start_idx]) - len(lines[start_idx].lstrip("#"))
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        ln = lines[j]
        if ln.startswith("#"):
            lvl = len(ln) - len(ln.lstrip("#"))
            if lvl <= start_level:
                end_idx = j
                break

    section = "\n".join(lines[start_idx:end_idx])
    if len(section) > READ_PAGE_MAX_CHARS:
        section = section[:READ_PAGE_MAX_CHARS] + f"\n\n…[truncated; full section is {len(section)} chars]"
    header = f"# sources/specs/{version}/Core_v{version}.md  (Vol {vol or '?'} Part {part or '?'})\n\n"
    return header + section


# ─── SDK-decorated wrappers ─────────────────────────────────────────────


def _wrap(text: str) -> dict:
    return {"content": [{"type": "text", "text": text}]}


@tool(
    "list_index",
    "Read the wiki's index.md catalog. ALWAYS call this first to identify which pages are relevant.",
    {},
)
async def list_index(args: dict) -> dict:
    return _wrap(_list_index())


@tool(
    "search_wiki",
    "Search wiki and/or original spec markdown for a query. "
    f"Returns up to {SEARCH_RESULT_LIMIT} hits with file paths and ~{SEARCH_SNIPPET_CHARS}-char snippets. "
    "scope: 'wiki' for curated content, 'sources' for original spec text, 'both' to search everything.",
    {"query": str, "scope": str},
)
async def search_wiki(args: dict) -> dict:
    return _wrap(_search_wiki(args.get("query") or "", args.get("scope") or "both"))


@tool(
    "read_page",
    "Read a wiki or source markdown file by repo-relative path "
    "(e.g. 'wiki/concepts/channel-sounding.md' or 'sources/specs/6.0/Core_v6.0.md'). "
    f"Truncated to {READ_PAGE_MAX_CHARS} characters; long source files should use read_source instead.",
    {"path": str},
)
async def read_page(args: dict) -> dict:
    return _wrap(_read_page(args.get("path") or ""))


@tool(
    "read_source",
    "Read a slice of an original Bluetooth spec markdown. Provide 'version' (e.g. '6.0') "
    "and optionally 'vol' (e.g. '6') and 'part' (e.g. 'B') to scope the read. "
    "Without vol/part, returns a table of contents derived from headings.",
    {"version": str, "vol": str, "part": str},
)
async def read_source(args: dict) -> dict:
    return _wrap(_read_source(args.get("version") or "", args.get("vol") or "", args.get("part") or ""))


ALL_TOOLS = [list_index, search_wiki, read_page, read_source]
