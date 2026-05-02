#!/usr/bin/env python3
"""
Ingest workflow orchestrator for the Bluetooth Spec Wiki.

This script does NOT update the wiki itself — that is done by the LLM (Claude).
Instead, it prepares context and generates prompts for Claude to perform the INGEST operation.

Usage:
    python scripts/ingest.py 6.0           # Prepare ingest prompt for version 6.0
    python scripts/ingest.py --all         # Prepare ingest for all unconverted versions
    python scripts/ingest.py --lint        # Prepare lint check prompt
    python scripts/ingest.py --status      # Show wiki coverage status

Workflow:
    1. Run download_specs.sh to get PDFs
    2. Run convert_to_md.py to convert to markdown
    3. Run ingest.py to generate Claude prompts
    4. Open Claude Code and paste/run the generated prompt
    5. Claude updates wiki pages based on the full spec text
"""

import sys
import os
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).parent.parent
SPECS_DIR = REPO_ROOT / "sources" / "specs"
WIKI_DIR = REPO_ROOT / "wiki"
VERSIONS = ["5.0", "5.1", "5.2", "5.3", "5.4", "6.0", "6.1", "6.2"]


def get_wiki_status() -> dict:
    """Return coverage status for each spec version."""
    status = {}
    for version in VERSIONS:
        pdf_exists = (SPECS_DIR / version / f"Core_v{version}.pdf").exists()
        md_source_exists = (SPECS_DIR / version / f"Core_v{version}.md").exists()
        wiki_exists = (WIKI_DIR / "versions" / f"core-spec-{version}.md").exists()
        status[version] = {
            "pdf": pdf_exists,
            "source_md": md_source_exists,
            "wiki_page": wiki_exists,
            "fully_ingested": wiki_exists and md_source_exists,
        }
    return status


def print_status():
    """Print current wiki coverage status."""
    status = get_wiki_status()
    print("=== Bluetooth Wiki Coverage Status ===")
    print("")
    print(f"{'Version':<10} {'PDF':<8} {'Source MD':<12} {'Wiki Page':<12} {'Status'}")
    print("-" * 60)
    for version, s in status.items():
        pdf = "✓" if s["pdf"] else "✗"
        src = "✓" if s["source_md"] else "✗"
        wiki = "✓" if s["wiki_page"] else "✗"
        if s["fully_ingested"]:
            st = "FULL SOURCE"
        elif s["wiki_page"] and not s["source_md"]:
            st = "SEED ONLY"
        elif s["source_md"] and not s["wiki_page"]:
            st = "NEEDS INGEST"
        elif not s["pdf"]:
            st = "NEEDS DOWNLOAD"
        else:
            st = "NEEDS CONVERT"
        print(f"{version:<10} {pdf:<8} {src:<12} {wiki:<12} {st}")
    print("")

    needs_download = [v for v, s in status.items() if not s["pdf"]]
    needs_convert = [v for v, s in status.items() if s["pdf"] and not s["source_md"]]
    needs_ingest = [v for v, s in status.items() if s["source_md"] and s["wiki_page"]]

    if needs_download:
        print(f"Run: ./scripts/download_specs.sh {' '.join(needs_download)}")
    if needs_convert:
        print(f"Run: python scripts/convert_to_md.py {' '.join(needs_convert)}")
    if needs_ingest:
        print(f"Ready to ingest: {', '.join(needs_ingest)}")
        print(f"Run: python scripts/ingest.py {' '.join(needs_ingest)}")


def generate_ingest_prompt(version: str) -> str:
    """Generate a Claude prompt for ingesting a converted spec."""
    source_md = SPECS_DIR / version / f"Core_v{version}.md"
    wiki_page = WIKI_DIR / "versions" / f"core-spec-{version}.md"

    if not source_md.exists():
        return f"ERROR: {source_md} does not exist. Run convert_to_md.py first."

    prompt = f"""# INGEST Operation: Bluetooth Core Spec {version}

Follow the INGEST procedure defined in CLAUDE.md.

## Source file
`sources/specs/{version}/Core_v{version}.md`

## Tasks

1. **Read** `sources/specs/{version}/Core_v{version}.md` (the full converted spec text)
2. **Update** `wiki/versions/core-spec-{version}.md`:
   - Enrich the Executive Summary with spec-specific language
   - Verify and expand the New Features table with exact spec references (Vol/Part/§)
   - Add any features found in the full spec that are missing from the seed page
   - Update Developer Impact with concrete implementation guidance from the spec
3. **Update affected diff pages** in `wiki/version-diff/`:
   - `diff-X.W-to-{version}.md` (incoming diff)
   - `diff-{version}-to-X.Z.md` (outgoing diff, if source available)
4. **Update concept pages** in `wiki/concepts/` that are touched by this version
5. **Update** `index.md` if any new entries are needed
6. **Append** to `log.md` with:
   - Date: {datetime.now().strftime('%Y-%m-%d')}
   - Operation: INGEST
   - Version: {version}
   - What was updated

## Citation format
Use `[Core {version}, Vol N, Part P, §S.S.S]` for all spec references.

## Start
Read CLAUDE.md first, then begin with the source file.
"""
    return prompt


def generate_lint_prompt() -> str:
    """Generate a Claude prompt for a wiki lint pass."""
    return """# LINT Operation: Bluetooth Wiki Health Check

Follow the LINT procedure defined in CLAUDE.md.

## Tasks

1. **Read** `index.md` — verify all listed files exist
2. **Check for contradictions**:
   - Version pages should agree with corresponding diff pages
   - Feature introduction dates should be consistent across all pages
   - "new in X.Y" claims should not appear in pages for earlier versions
3. **Check cross-references**: every `[link](path)` should resolve to an existing file
4. **Check orphan pages**: every file in `wiki/` should be listed in `index.md`
5. **Identify gaps**: versions with only seed data (no source PDF ingested) should be flagged
6. **Check stale claims**: if 6.0 is current, pages should say "latest" only for 6.0

## Report format
- List all issues found, categorized by type
- For each issue: file path, line reference, and recommended fix
- Summarize: N contradictions, N orphans, N stale claims, N broken links

## Start
Begin by reading CLAUDE.md, then index.md, then check each wiki page.
"""


def save_prompt(prompt: str, filename: str):
    """Save a prompt to a file for later use."""
    prompts_dir = REPO_ROOT / ".prompts"
    prompts_dir.mkdir(exist_ok=True)
    path = prompts_dir / filename
    path.write_text(prompt, encoding="utf-8")
    print(f"  Saved prompt to: {path}")
    return path


def main():
    args = sys.argv[1:]

    if not args or "--status" in args:
        print_status()
        if not args:
            print("\nUsage:")
            print("  python scripts/ingest.py --status        # Show coverage status")
            print("  python scripts/ingest.py 6.0             # Generate ingest prompt for 6.0")
            print("  python scripts/ingest.py --all           # Generate prompts for all ready versions")
            print("  python scripts/ingest.py --lint          # Generate lint prompt")
        return

    if "--lint" in args:
        prompt = generate_lint_prompt()
        print(prompt)
        save_prompt(prompt, "lint.md")
        return

    if "--all" in args:
        status = get_wiki_status()
        ready = [v for v, s in status.items() if s["source_md"]]
        if not ready:
            print("No versions ready for ingest. Run download_specs.sh and convert_to_md.py first.")
            return
        args = ready

    for version in args:
        if version.startswith("--"):
            continue
        if version not in VERSIONS:
            print(f"Unknown version: {version}. Valid: {', '.join(VERSIONS)}")
            continue

        print(f"\n=== Ingest Prompt for Core Spec {version} ===\n")
        prompt = generate_ingest_prompt(version)
        print(prompt)
        save_prompt(prompt, f"ingest-{version}.md")

    print("\n=== How to use these prompts ===")
    print("1. Open Claude Code in the bluetooth_wiki directory:")
    print("   cd bluetooth_wiki && claude")
    print("")
    print("2. Claude will read CLAUDE.md automatically as context.")
    print("")
    print("3. Paste the prompt above into Claude Code, or use:")
    print("   /read .prompts/ingest-X.Y.md")
    print("")
    print("4. Claude will update the wiki pages from the full spec text.")


if __name__ == "__main__":
    main()
