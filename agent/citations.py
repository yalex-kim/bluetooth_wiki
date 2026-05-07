"""Single source of truth for citation ↔ URL mapping.

The agent emits citations as labels + file_paths. This module converts those
into deep links into the hosted MkDocs site so clients can render them as
clickable references back to the original wiki page or spec source.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import PurePosixPath

from .config import SITE_BASE_URL


@dataclass
class Citation:
    label: str
    file_path: str
    url: str


# [Core 6.0, Vol 6, Part B, §4.4.2]  →  groups: version, vol, part, section
_SPEC_RE = re.compile(
    r"\[Core\s+(?P<version>\d+\.\d+)"
    r"(?:\s*,\s*Vol\s+(?P<vol>\d+))?"
    r"(?:\s*,\s*Part\s+(?P<part>[A-Z]))?"
    r"(?:\s*,\s*§\s*(?P<section>[\d\.]+))?"
    r"\s*\]"
)

# [Wiki: <title>]  or  [Diff X.W → X.Y]
_WIKI_RE = re.compile(r"\[Wiki:\s*(?P<title>[^\]]+)\]")
_DIFF_RE = re.compile(r"\[Diff\s+(?P<from>\d+\.\d+)\s*[→\->]+\s*(?P<to>\d+\.\d+)\]")


def _slugify_section(section: str) -> str:
    return section.replace(".", "-")


def parse_citation(text: str) -> dict | None:
    """Parse a single bracketed citation string into structured fields."""
    m = _SPEC_RE.search(text)
    if m:
        return {"kind": "spec", **{k: v for k, v in m.groupdict().items() if v}}
    m = _WIKI_RE.search(text)
    if m:
        return {"kind": "wiki", "title": m.group("title").strip()}
    m = _DIFF_RE.search(text)
    if m:
        return {"kind": "diff", "from": m.group("from"), "to": m.group("to")}
    return None


def file_path_to_url(file_path: str, anchor: str | None = None) -> str:
    """Convert a repo-relative file path into a hosted-site URL.

    Mapping (matches MkDocs `use_directory_urls=true`):
      wiki/foo/bar.md          →  /wiki/foo/bar/
      sources/specs/6.0/X.md   →  /sources/6.0/X/
      index.md                 →  /
    """
    p = PurePosixPath(file_path.lstrip("/"))
    parts = p.parts

    if not parts or (len(parts) == 1 and parts[0] in {"index.md", "README.md"}):
        path = "/"
    elif parts[0] == "wiki":
        stem = p.stem
        path = "/" + "/".join(("wiki",) + parts[1:-1] + (stem,)) + "/"
    elif parts[0] == "sources":
        stem = p.stem
        # sources/specs/X.Y/Core_vX.Y.md  →  /sources/X.Y/Core_vX.Y/
        rest = parts[2:-1] if len(parts) >= 3 and parts[1] == "specs" else parts[1:-1]
        path = "/" + "/".join(("sources",) + rest + (stem,)) + "/"
    else:
        path = "/" + str(p)

    url = f"{SITE_BASE_URL}{path}"
    if anchor:
        url += f"#{anchor}"
    return url


def citation_to_url(label: str, file_path: str) -> str:
    """Resolve a citation label + file_path to a hosted URL with anchor."""
    parsed = parse_citation(f"[{label}]") if not label.startswith("[") else parse_citation(label)
    anchor = None
    if parsed and parsed.get("kind") == "spec":
        slug_parts = []
        if parsed.get("vol"):
            slug_parts.append(f"vol-{parsed['vol']}")
        if parsed.get("part"):
            slug_parts.append(f"part-{parsed['part'].lower()}")
        if parsed.get("section"):
            slug_parts.append(_slugify_section(parsed["section"]))
        if slug_parts:
            anchor = "-".join(slug_parts)
    return file_path_to_url(file_path, anchor=anchor)


def hydrate_citations(citations: list[dict]) -> list[Citation]:
    """Take the agent's [{label, file_path}] list and add resolved URLs."""
    out: list[Citation] = []
    for c in citations:
        label = c.get("label", "")
        file_path = c.get("file_path", "")
        url = citation_to_url(label, file_path) if file_path else ""
        out.append(Citation(label=label, file_path=file_path, url=url))
    return out
