# Bluetooth Spec Wiki — Activity Log

> This is an **append-only** log. Never delete entries. Add new entries at the top.
> Format: `## [YYYY-MM-DD] [Operation] — [Summary]`

---

## [2026-05-02] INIT — Initial wiki scaffold created

**Operation**: INIT
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs

### What was created

- `CLAUDE.md` — Wiki schema and LLM maintainer instructions
- `index.md` — Content catalog with query routing guide
- `wiki/overview.md` — Bluetooth technology overview
- `wiki/versions/core-spec-5.0.md` through `core-spec-6.0.md` — Six version pages (5.0–6.0)
- `wiki/version-diff/diff-5.0-to-5.1.md` through `diff-5.4-to-6.0.md` — Five diff pages
- `wiki/concepts/ble-architecture.md` — BLE protocol stack
- `wiki/concepts/classic-bluetooth.md` — BR/EDR technology
- `wiki/concepts/security.md` — Pairing, bonding, privacy
- `wiki/concepts/profiles-and-services.md` — GATT profiles and services
- `sources/README.md` — Instructions for downloading spec PDFs
- `scripts/download_specs.sh` — Shell script to download PDFs from bluetooth.com
- `scripts/convert_to_md.py` — Python script to convert PDFs via OpenDataLoader
- `scripts/ingest.py` — Script to ingest converted markdown into the wiki
- `guide/claude-code-integration.md` — Guide for using this wiki with Claude Code

### Data sources

- Wiki pages seeded with knowledge from Bluetooth Core Spec feature enhancement documents
  and published Bluetooth SIG materials (Versions 5.0–6.0).
- Full spec PDFs not yet ingested. Run `scripts/download_specs.sh` to fetch PDFs,
  then `scripts/convert_to_md.py` to convert, then use INGEST operation to enrich pages.

### Next steps

1. Run `scripts/download_specs.sh` to download Core Spec PDFs from bluetooth.com
2. Run `scripts/convert_to_md.py` to convert PDFs to markdown via OpenDataLoader
3. Run INGEST operation on each converted spec to enrich wiki pages with full spec details
4. Run LINT to verify consistency across all pages

---

_Log entries are added by the LLM during INGEST, QUERY, and LINT operations._
_Human entries are also welcome._
