# Bluetooth Spec Wiki — Schema & LLM Maintainer Instructions

> This file is the **schema document** for the Bluetooth Spec Wiki.
> It programs Claude (or any capable LLM) to act as a disciplined wiki maintainer.
> Based on the [LLM Wiki pattern by Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## 1. Wiki Purpose

This wiki is a **persistent, compounding knowledge base** for Bluetooth Core Specifications.
It is designed to be queried by LLMs (especially Claude via Claude Code) so that developers,
engineers, and researchers can ask natural-language questions about Bluetooth specs and receive
accurate, well-cited answers without reading hundreds of pages of spec PDFs.

---

## 2. Three-Layer Architecture

```
Layer 1 — sources/specs/          Raw, immutable Bluetooth spec PDFs (and their markdown conversions)
Layer 2 — wiki/                   LLM-maintained markdown pages (summaries, diffs, concepts)
Layer 3 — CLAUDE.md (this file)   Schema: structure, conventions, and maintainer workflows
```

**Rule**: The LLM reads Layer 1 as the source of truth. It writes and updates Layer 2. It never modifies Layer 1 or this file.

---

## 3. Directory Structure

```
bluetooth_wiki/
├── CLAUDE.md                          ← This file (schema)
├── index.md                           ← Content catalog (read first on every query)
├── log.md                             ← Append-only activity log
├── wiki/
│   ├── overview.md                    ← Bluetooth technology overview
│   ├── versions/
│   │   ├── core-spec-5.0.md           ← Per-version pages
│   │   ├── core-spec-5.1.md
│   │   ├── core-spec-5.2.md
│   │   ├── core-spec-5.3.md
│   │   ├── core-spec-5.4.md
│   │   ├── core-spec-6.0.md
│   │   ├── core-spec-6.1.md
│   │   └── core-spec-6.2.md
│   ├── version-diff/
│   │   ├── diff-5.0-to-5.1.md         ← Pre-indexed version differences
│   │   ├── diff-5.1-to-5.2.md
│   │   ├── diff-5.2-to-5.3.md
│   │   ├── diff-5.3-to-5.4.md
│   │   ├── diff-5.4-to-6.0.md
│   │   ├── diff-6.0-to-6.1.md
│   │   └── diff-6.1-to-6.2.md
│   ├── concepts/
│   │   ├── ble-architecture.md
│   │   ├── classic-bluetooth.md
│   │   ├── security.md
│   │   ├── profiles-and-services.md
│   │   ├── le-audio.md
│   │   ├── direction-finding.md
│   │   └── channel-sounding.md
│   └── reference/
│       └── hci-commands.md        ← HCI command lookup table (opcodes, params, events)
├── sources/
│   ├── README.md                      ← How to download spec PDFs
│   └── specs/
│       └── X.Y/
│           ├── Core_vX.Y.md           ← Full spec text converted via PyMuPDF
│           └── Core_vX.Y_images/      ← Extracted figure PNGs (Vol{N}_Part{P}_Figure{X_Y}.png)
├── scripts/
│   ├── download_spec_documents.py     ← Downloads PDFs from bluetooth.com
│   ├── convert_to_md.py               ← Converts PDFs → markdown + figure PNGs via PyMuPDF
│   └── ingest.py                      ← Ingests new source docs into the wiki
└── guide/
    └── claude-code-integration.md     ← How to use this wiki with Claude Code
```

---

## 4. Core Operations

### 4.1 INGEST — Adding a new spec version

When a new Bluetooth Core Spec PDF has been converted to markdown and placed in `sources/specs/`:

1. **Read** the markdown source completely.
2. **Create or update** the corresponding `wiki/versions/core-spec-X.Y.md` page:
   - Executive summary (≤300 words)
   - New features list with brief descriptions
   - Key changes to existing mechanisms
   - Deprecated features
   - Relevant part/section references from the spec
3. **Create or update** the diff page `wiki/version-diff/diff-X.W-to-X.Y.md`:
   - What was added
   - What was modified
   - What was deprecated/removed
   - Migration impact for developers
4. **Update** `index.md` to include the new page.
5. **Update** any affected concept pages in `wiki/concepts/`.
6. **Append** to `log.md` with timestamp and summary of changes.

### 4.2 QUERY — Answering user questions

When a user asks a question about Bluetooth specs:

1. **Read `index.md`** first to identify which pages are relevant.
2. **Read** the relevant wiki pages (version pages, diff pages, concept pages).
3. **Synthesize** a precise answer with citations like `[Core 6.0, Vol 6, Part B, §4.4.2]`.
4. If the answer reveals a gap, **create a new wiki page** or **update an existing one**.
5. **Append** to `log.md`.

### 4.3 LINT — Wiki health check

Periodically run a lint pass to:
- Find contradictions between version pages and diff pages
- Identify orphan pages (not linked from `index.md`)
- Flag stale claims (e.g., "new in 5.3" on a 5.3 page when 6.0 is now latest)
- Check that all versions in `sources/specs/` have corresponding wiki pages
- Verify all cross-references point to existing files

---

## 5. Writing Conventions

### Language

All wiki pages (`wiki/`) must be written in **English**. This applies to:
- Page titles, headings, body text, table content, notes
- Code comments within examples
- `log.md` entries and `index.md` descriptions

The only exception is content directly quoted or transcribed from a source spec (e.g., a table reproduced verbatim from the PDF), which may retain its original form.

---

### Source Links (all page types)

Every wiki page that was built from one or more source files **must** include a footer line linking back to those files:

```markdown
*Source: [Core 6.2, Vol 4, Part E, §7](../../sources/specs/6.2/Core_v6.2.md) and [HCI.ICS.p30](../../sources/specs/conformance-profiles/HCI.ICS.p30.md)*
```

- Use relative paths from the page's location (e.g. `../../sources/specs/…` from `wiki/reference/` or `wiki/concepts/`).
- For profile spec pages, link to the corresponding `sources/specs/profiles/<Name>.md`.
- This rule applies to version pages, diff pages, concept pages, and reference pages alike.
- The version page template already includes a `**Source**` header line — keep that in addition to the footer.

### Version Pages (`wiki/versions/core-spec-X.Y.md`)

```markdown
# Bluetooth Core Specification X.Y

**Release Date**: YYYY-MM-DD
**Status**: [Active | Withdrawn | Superseded by X.Z]
**Spec Volume**: ~N pages
**Source**: [PDF](../../sources/specs/core-spec-X.Y.pdf) | [Markdown](../../sources/specs/core-spec-X.Y.md)

## Executive Summary
(2–3 paragraph overview of what changed and why it matters)

## New Features
| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| ...     | ...              | Vol N, Part X  |

## Key Changes to Existing Mechanisms
...

## Deprecated / Removed
...

## Developer Impact
...

## Cross-References
- See also: [diff-X.W-to-X.Y](../version-diff/diff-X.W-to-X.Y.md)
- Concepts touched: [LE Audio](../concepts/ble-architecture.md), ...
```

### Diff Pages (`wiki/version-diff/diff-X.W-to-X.Y.md`)

```markdown
# Diff: Bluetooth Core Spec X.W → X.Y

## At a Glance
(one-paragraph TL;DR of the biggest changes)

## Added
- **Feature name** — description [Vol N, Part X, §Y.Z]

## Modified
- **Mechanism name** — what changed and why

## Deprecated / Removed
- ...

## Migration Guide
(practical guidance for developers updating implementations)
```

### Concept Pages (`wiki/concepts/*.md`)

```markdown
# [Concept Name]

**Last updated**: YYYY-MM-DD
**Covers**: Core Spec X.Y – X.Z

## Overview
## How It Works
## Version History (which spec version introduced/changed this)
## Related Features

---

## See Also
- [Related Page](../concepts/related.md)

---

*Source: [Core X.Y, Vol N, Part P](../../sources/specs/X.Y/Core_vX.Y.md)*
```

---

## 6. Citation Format

Always cite the Bluetooth Core Spec as:
```
[Core X.Y, Vol N, Part P, §S.S.S]
```

Example: `[Core 6.0, Vol 6, Part B, §4.4.2]`

For feature enhancement documents:
```
[BT Feature: "Feature Name", bluetooth.com, YYYY]
```

---

## 7. Ingesting Full Spec PDFs

Spec PDFs are converted to markdown using `scripts/convert_to_md.py` (PyMuPDF-based).
Each version produces:
- `sources/specs/X.Y/Core_vX.Y.md` — full spec text with headings, inline tables, and figure references
- `sources/specs/X.Y/Core_vX.Y_images/Vol{N}_Part{P}_Figure{X_Y}.png` — extracted figure images

The LLM should process the source markdown section by section:

1. Parse the document structure to identify volumes and parts (marked by headings like `## 1 ARCHITECTURE`).
2. For each Part, extract: purpose, key definitions, protocol descriptions.
3. Build the version wiki page from this structured reading.
4. Update concept pages where the spec introduces or modifies a concept.

Large specs (5.0 is ~2800 pages, 6.2 is ~3900 pages) should be processed in chunks by volume:
- Vol 1: Architecture & Overview
- Vol 2: BR/EDR Controller
- Vol 3: Host
- Vol 4: Host Controller Interface
- Vol 5: AMP Controller
- Vol 6: LE Controller
- Vol 7: Reserved

---

## 8. Source of Truth Priority

When information conflicts between pages:
1. `sources/specs/X.Y/Core_vX.Y.md` (converted PDF) — highest authority
2. `wiki/versions/core-spec-X.Y.md` — authoritative summary
3. `wiki/version-diff/` pages — derived from version pages
4. `wiki/concepts/` pages — synthesized across versions

Resolve conflicts by re-reading the source spec, then updating wiki pages accordingly.

---

## 9. Versioning Policy

- Wiki pages are updated in-place (no versioning of wiki files themselves).
- `log.md` serves as the audit trail.
- When a spec version is **Withdrawn** by Bluetooth SIG, mark it in the version page header
  but do not delete the page.

---

## 10. Quick Reference: Bluetooth Core Spec Versions

| Version | Release Date | Key Theme |
|---------|-------------|-----------|
| 1.0     | 1998-07     | Initial release |
| 2.0+EDR | 2004-11     | Enhanced Data Rate (3 Mbps) |
| 3.0+HS  | 2009-04     | High Speed via Wi-Fi |
| 4.0     | 2010-06     | Bluetooth Low Energy (BLE) introduced |
| 4.1     | 2013-12     | IPv6/6LoWPAN, coexistence |
| 4.2     | 2014-12     | Privacy, 251-byte LE packets |
| 5.0     | 2016-12     | 2× speed, 4× range, 8× broadcast |
| 5.1     | 2019-01     | Direction Finding (AoA/AoD) |
| 5.2     | 2019-12     | LE Audio, LC3 codec, EATT |
| 5.3     | 2021-07     | Connection Subrating, PAwR prep |
| 5.4     | 2023-02     | PAwR, Encrypted Advertising Data |
| 6.0     | 2024-08     | Channel Sounding, DBAF |
| 6.1     | 2025-04     | Randomized RPA Updates, privacy enhancements |
| 6.2     | 2025-11     | Shorter Connection Intervals (375 µs), LE UTP, CS security hardening |
