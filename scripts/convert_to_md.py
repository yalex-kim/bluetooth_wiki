#!/usr/bin/env python3
"""
Convert Bluetooth Core Spec PDFs to Markdown using OpenDataLoader PDF.

Usage:
    python scripts/convert_to_md.py                     # Convert all PDFs in sources/specs/
    python scripts/convert_to_md.py 6.0                 # Convert specific version
    python scripts/convert_to_md.py 5.2 5.4 6.0         # Convert multiple versions

Requirements:
    pip install -U opendataloader-pdf

    For better table extraction (recommended for spec PDFs):
    pip install -U "opendataloader-pdf[hybrid]"

Output:
    sources/specs/core-spec-X.Y.md  (Markdown)
    sources/specs/core-spec-X.Y.json (structured JSON with metadata, optional)
"""

import sys
import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SPECS_DIR = REPO_ROOT / "sources" / "specs"


def check_dependencies():
    try:
        import opendataloader_pdf
        return opendataloader_pdf
    except ImportError:
        print("ERROR: opendataloader-pdf not installed.")
        print("")
        print("Install with:")
        print("  pip install -U opendataloader-pdf")
        print("")
        print("For better table extraction (recommended):")
        print('  pip install -U "opendataloader-pdf[hybrid]"')
        sys.exit(1)


def convert_spec(version: str, odl, hybrid: bool = False, json_output: bool = False) -> bool:
    pdf_path = SPECS_DIR / f"core-spec-{version}.pdf"
    md_path = SPECS_DIR / f"core-spec-{version}.md"

    if not pdf_path.exists():
        print(f"  [SKIP] {pdf_path.name} not found. Run download_specs.sh first.")
        return False

    if md_path.exists():
        print(f"  [SKIP] {md_path.name} already exists. Delete to reconvert.")
        return True

    print(f"  Converting core-spec-{version}.pdf → core-spec-{version}.md ...")

    formats = "markdown,json" if json_output else "markdown"
    kwargs = {
        "input_path": [str(pdf_path)],
        "output_dir": str(SPECS_DIR),
        "format": formats,
        "image_output": "off",  # Skip images for wiki use — reduces noise
        "use_struct_tree": True,  # Use PDF structure tags for better heading detection
        "sanitize": True,        # Filter potential prompt injections from spec PDFs
    }

    # Hybrid mode uses AI for complex table extraction — recommended for spec PDFs
    # Start hybrid server first: opendataloader-pdf-hybrid --port 5002
    if hybrid:
        kwargs["hybrid"] = "docling-fast"
        print("  Using hybrid AI mode for better table extraction")

    try:
        odl.convert(**kwargs)
        print(f"  [OK] Saved: {md_path.name}")
        if json_output:
            print(f"  [OK] Saved: core-spec-{version}.json")
        return True
    except Exception as e:
        print(f"  [ERROR] Conversion failed: {e}")
        return False


def post_process_markdown(version: str):
    """Clean up common issues in converted spec PDFs."""
    md_path = SPECS_DIR / f"core-spec-{version}.md"
    if not md_path.exists():
        return

    print(f"  Post-processing core-spec-{version}.md ...")
    text = md_path.read_text(encoding="utf-8")

    # Add wiki header if not present
    header = f"""# Bluetooth Core Specification {version} — Full Text

> **Source**: Converted from official Bluetooth SIG PDF via OpenDataLoader PDF.
> **Note**: This is machine-converted text. Some tables and figures may be imperfect.
>           Refer to the original PDF for definitive spec language.
> **Wiki pages**: See [core-spec-{version}](../../wiki/versions/core-spec-{version}.md) for the curated summary.

---

"""
    if not text.startswith("# Bluetooth"):
        text = header + text
        md_path.write_text(text, encoding="utf-8")
        print(f"  [OK] Header added")
    else:
        print(f"  [OK] No changes needed")


def main():
    odl = check_dependencies()

    # Parse arguments
    if len(sys.argv) > 1:
        versions = sys.argv[1:]
        # Filter out flags
        hybrid = "--hybrid" in versions
        json_output = "--json" in versions
        versions = [v for v in versions if not v.startswith("--")]
    else:
        # Auto-detect: convert all PDFs that don't have a .md counterpart
        versions = []
        for pdf in sorted(SPECS_DIR.glob("core-spec-*.pdf")):
            version = pdf.stem.replace("core-spec-", "")
            md_file = SPECS_DIR / f"{pdf.stem}.md"
            if not md_file.exists():
                versions.append(version)
        hybrid = False
        json_output = False

    if not versions:
        print("No PDFs to convert. Either:")
        print("  - Run ./scripts/download_specs.sh to download PDFs first")
        print("  - Specify versions: python scripts/convert_to_md.py 6.0")
        sys.exit(0)

    print("=== Bluetooth Spec PDF → Markdown Converter ===")
    print(f"Input directory : {SPECS_DIR}")
    print(f"Versions        : {', '.join(versions)}")
    print(f"Hybrid mode     : {'ON (make sure hybrid server is running)' if hybrid else 'OFF'}")
    print(f"JSON output     : {'ON' if json_output else 'OFF'}")
    print("")

    if hybrid:
        print("NOTE: Hybrid mode requires the hybrid server to be running:")
        print("  Terminal 1: opendataloader-pdf-hybrid --port 5002")
        print("  Terminal 2: python scripts/convert_to_md.py --hybrid")
        print("")

    failed = []
    for version in versions:
        print(f"--- Version {version} ---")
        if convert_spec(version, odl, hybrid=hybrid, json_output=json_output):
            post_process_markdown(version)
        else:
            failed.append(version)
        print("")

    print("=== Summary ===")
    converted = [v for v in versions if v not in failed]
    if converted:
        print(f"Converted: {', '.join(converted)}")
    if failed:
        print(f"Failed   : {', '.join(failed)}")

    print("")
    print("Next step: Use INGEST operation in CLAUDE.md to update wiki pages from converted markdown")
    print("  Open Claude Code in this repo and run:")
    print("  > Ingest the converted Bluetooth Core Spec markdown files into the wiki")


if __name__ == "__main__":
    main()
