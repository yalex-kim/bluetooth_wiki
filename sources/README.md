# Bluetooth Spec Sources

This directory stores raw Bluetooth Core Specification PDF files and their
OpenDataLoader-converted Markdown versions.

## Directory structure

```
sources/
├── README.md          ← This file
└── specs/
    ├── core-spec-5.0.pdf    ← Downloaded from bluetooth.com
    ├── core-spec-5.0.md     ← Converted via OpenDataLoader PDF
    ├── core-spec-5.1.pdf
    ├── core-spec-5.1.md
    ├── ...
    ├── core-spec-6.0.pdf
    └── core-spec-6.0.md
```

## Step 1: Download PDFs

PDFs are freely downloadable from [bluetooth.com](https://www.bluetooth.com/specifications/specs/)
after accepting their Terms of Use.

**Option A — Automated script:**
```bash
./scripts/download_specs.sh           # All versions (5.0 – 6.0)
./scripts/download_specs.sh 6.0       # Single version
```

**Option B — Manual download:**

Visit each spec page, accept the Terms of Use, and save the PDF to `sources/specs/`:

| Version | Spec Page | File Name |
|---------|-----------|-----------|
| 5.0 | https://www.bluetooth.com/specifications/specs/core-specification-5-0/ | `core-spec-5.0.pdf` |
| 5.1 | https://www.bluetooth.com/specifications/specs/core-specification-5-1/ | `core-spec-5.1.pdf` |
| 5.2 | https://www.bluetooth.com/specifications/specs/core-specification-5-2/ | `core-spec-5.2.pdf` |
| 5.3 | https://www.bluetooth.com/specifications/specs/core-specification-5-3/ | `core-spec-5.3.pdf` |
| 5.4 | https://www.bluetooth.com/specifications/specs/core-specification-5-4/ | `core-spec-5.4.pdf` |
| 6.0 | https://www.bluetooth.com/specifications/specs/core-specification-6-0/ | `core-spec-6.0.pdf` |

## Step 2: Convert PDFs to Markdown

Use [OpenDataLoader PDF](https://opendataloader.org) to convert PDFs to LLM-ready Markdown.

**Install:**
```bash
pip install -U opendataloader-pdf

# For better table extraction (recommended for spec PDFs):
pip install -U "opendataloader-pdf[hybrid]"
```

**Convert:**
```bash
python scripts/convert_to_md.py           # Convert all downloaded PDFs
python scripts/convert_to_md.py 6.0       # Convert specific version
```

**With hybrid mode** (better table accuracy, requires Java 11+):
```bash
# Terminal 1: Start the hybrid server
opendataloader-pdf-hybrid --port 5002

# Terminal 2: Convert with hybrid mode
python scripts/convert_to_md.py --hybrid 6.0
```

## Step 3: Ingest into Wiki

Once you have the converted Markdown, use the INGEST operation (defined in `CLAUDE.md`) to
update the wiki pages with full spec details.

```bash
python scripts/ingest.py --status     # Check what's ready
python scripts/ingest.py 6.0          # Generate ingest prompt for version 6.0
```

Then open Claude Code in the repo root and use the generated prompt.

## Notes

- PDFs are **not committed to git** (listed in `.gitignore`) due to their size
- The `.md` converted files are also excluded from git to keep the repo lightweight
- The `wiki/` directory contains the curated, human+LLM maintained wiki pages
  which ARE committed to git — these are the primary artifact of this project

## File sizes (approximate)

| Version | PDF Size |
|---------|----------|
| 5.0 | ~15 MB |
| 5.1 | ~18 MB |
| 5.2 | ~20 MB |
| 5.3 | ~21 MB |
| 5.4 | ~22 MB |
| 6.0 | ~24 MB |
