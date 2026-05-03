#!/usr/bin/env python3
"""
Build a section index from source MDs and add hyperlinks to wiki citations.

How it works
------------
Source MDs have no explicit Vol/Part boundary headings, but figure references
like  ![Figure 4.1](Core_v6.0_images/Vol6_PartH_Figure4_1.png)  carry that
information in the filename.  The script scans each source MD top-to-bottom:

  · When it sees a figure reference → updates current (vol, part) context.
  · When it sees a section heading  → records  (vol, part, §N) → line_num.

The citation linker then rewrites plain citations in wiki pages:

  [Core 6.0, Vol 6, Part H, §4.3]
  →
  [Core 6.0, Vol 6, Part H, §4.3](../../sources/specs/6.0/Core_v6.0.md#L75213)

Usage
-----
  python scripts/link_citations.py              # build index + link
  python scripts/link_citations.py --build      # build index only
  python scripts/link_citations.py --link       # link only (uses saved index)
  python scripts/link_citations.py --dry-run    # preview without writing
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SPECS_DIR  = REPO_ROOT / "sources" / "specs"
WIKI_DIR   = REPO_ROOT / "wiki"
INDEX_PATH = SPECS_DIR / "section_index.json"

# Figure reference: captures vol and part from the image filename
# Matches: ![Figure N.M](Core_vX.Y_images/Vol6_PartH_Figure4_1.png)
_FIG_REF_RE = re.compile(
    r"!\[Figure [^\]]*\]\([^)]*Vol(\d+)_Part([A-Z]+)_Figure[^)]*\)"
)

# Section heading: ## 4, ### 4.1, #### 4.1.1, etc. (h2–h6, first token is the number)
_HEADING_RE = re.compile(r"^(#{2,6})\s+(\d+(?:\.\d+)*)\b")

# Citation (NOT already a link): [Core 6.0, Vol 6, Part H, §4.3]
# Negative lookbehind for '](' to avoid double-linking.
_CITE_RE = re.compile(
    r"(?<!\]\()\[Core\s+([\d.]+),\s*Vol\s+(\d+),\s*Part\s+([A-Z]+),\s*§([\d.]+)\](?!\()"
)


# ─── Phase 1: build index ────────────────────────────────────────────────────

def build_index() -> dict:
    """
    Return {version: {"Vol{v}_Part{p}_§{sec}": line_num, ...}, ...}
    by scanning every Core_vX.Y.md in sources/specs/.
    """
    index: dict = {}

    for md_path in sorted(SPECS_DIR.glob("*/Core_v*.md")):
        version = md_path.parent.name          # e.g. "6.0"
        print(f"  Indexing {md_path.name}...", end=" ", flush=True)

        with open(md_path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()

        cur_vol: str | None = None
        cur_part: str | None = None
        sections: dict = {}

        for lineno, raw in enumerate(lines, 1):
            line = raw.rstrip()

            # Update Vol/Part context from figure filename
            fm = _FIG_REF_RE.search(line)
            if fm:
                cur_vol, cur_part = fm.group(1), fm.group(2)
                continue

            # Record section heading with current context
            if cur_vol is None:
                continue
            hm = _HEADING_RE.match(line)
            if hm:
                sec = hm.group(2)
                key = f"Vol{cur_vol}_Part{cur_part}_§{sec}"
                # First occurrence wins (TOC entries appear before body)
                if key not in sections:
                    sections[key] = lineno

        index[version] = sections
        print(f"{len(sections)} sections")

    return index


# ─── Phase 2: link citations ─────────────────────────────────────────────────

def link_citations(index: dict, dry_run: bool = False) -> int:
    """
    Rewrite wiki pages, replacing plain [Core ...] citations with markdown links.
    Returns the number of files changed.
    """
    changed = 0

    for wiki_path in sorted(WIKI_DIR.rglob("*.md")):
        content = wiki_path.read_text(encoding="utf-8")

        def _replace(m: re.Match) -> str:
            ver, vol, part, sec = m.group(1), m.group(2), m.group(3), m.group(4)
            key = f"Vol{vol}_Part{part}_§{sec}"
            lineno = index.get(ver, {}).get(key)
            if lineno is None:
                return m.group(0)          # no match → leave unchanged
            rel = f"../../sources/specs/{ver}/Core_v{ver}.md#L{lineno}"
            return f"[Core {ver}, Vol {vol}, Part {part}, §{sec}]({rel})"

        new_content = _CITE_RE.sub(_replace, content)

        if new_content != content:
            changed += 1
            rel = wiki_path.relative_to(REPO_ROOT)
            if dry_run:
                # Show a diff-style preview (first 5 changed lines)
                old_lines = content.splitlines()
                new_lines = new_content.splitlines()
                n_changes = sum(1 for a, b in zip(old_lines, new_lines) if a != b)
                def _safe(s):
                    return s.encode("ascii", "replace").decode("ascii")
                print(f"\n  {rel}  ({n_changes} citations to link)")
                shown = 0
                for i, (a, b) in enumerate(zip(old_lines, new_lines), 1):
                    if a != b and _CITE_RE.search(a):
                        print(f"    L{i}: {_safe(a[:100])}")
                        print(f"       -> {_safe(b[:100])}")
                        shown += 1
                        if shown >= 5:
                            if n_changes > 5:
                                print(f"    ... and {n_changes - 5} more")
                            break
            else:
                wiki_path.write_text(new_content, encoding="utf-8")
                # Count how many citations were linked
                n_links = sum(1 for a, b in zip(content.splitlines(),
                                                 new_content.splitlines()) if a != b)
                print(f"  {rel}  ({n_links} citations linked)")

    return changed


# ─── Stats helper ─────────────────────────────────────────────────────────────

def print_stats(index: dict) -> None:
    total = sum(len(v) for v in index.values())
    print(f"\nIndex summary: {len(index)} versions, {total} sections total")
    for ver in sorted(index):
        parts = set()
        for key in index[ver]:
            parts.add(key.split("_§")[0])   # e.g. "Vol6_PartH"
        print(f"  v{ver}: {len(index[ver])} sections across {len(parts)} parts "
              f"({', '.join(sorted(parts)[:6])}{'...' if len(parts) > 6 else ''})")


# ─── Entry point ─────────────────────────────────────────────────────────────

def main() -> None:
    args = set(sys.argv[1:])
    do_build = "--link"  not in args      # build unless --link-only
    do_link  = "--build" not in args      # link unless --build-only
    dry_run  = "--dry-run" in args

    if do_build:
        print("Phase 1 - Building section index from source MDs...")
        index = build_index()
        INDEX_PATH.write_text(json.dumps(index, indent=2, ensure_ascii=False),
                               encoding="utf-8")
        print(f"\nIndex saved → {INDEX_PATH.relative_to(REPO_ROOT)}")
        print_stats(index)
    else:
        if not INDEX_PATH.exists():
            print(f"ERROR: index not found at {INDEX_PATH}. Run without --link first.")
            sys.exit(1)
        print(f"Loading index from {INDEX_PATH.relative_to(REPO_ROOT)}...")
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        print_stats(index)

    if do_link:
        print(f"\nPhase 2 - {'Preview' if dry_run else 'Linking'} citations in wiki...")
        n = link_citations(index, dry_run=dry_run)
        verb = "Would update" if dry_run else "Updated"
        print(f"\n{verb} {n} wiki file(s).")
        if dry_run and n:
            print("Run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
