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

**Rule**: The LLM reads Layer 1 as the source of truth. It writes and updates Layer 2. It never modifies Layer 1.

> **Before committing any wiki changes**, update `README.md` and `CLAUDE.md` to reflect the new state:
> - `README.md` — update the Structure section, Quick Start examples, or any descriptive text that references changed pages or directories.
> - `CLAUDE.md` — update the Directory Structure map, Core Operations steps, or any rule that the change affects.
> These two files must stay in sync with the actual repo at all times.

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
├── eval/
│   ├── dataset.json                   ← 42-question test set for strategy/system comparison
│   ├── rubric.md                      ← 5-dimension scoring rubric with difficulty weights
│   ├── judge_prompt.md                ← LLM-as-Judge prompt + Python run_evaluation() helper
│   ├── judge.py                       ← Shared judge/scoring module (used by all eval runners)
│   ├── runner.py                      ← Shared eval-suite runner (CLI + server jobs)
│   ├── report_render.py               ← Strategy-comparison HTML renderer (f-strings, no Jinja)
│   ├── results_wiki.json              ← LLM-Wiki baseline scores (95.8% overall, 2026-05-04)
│   ├── results_search_v{0,1,2}.json   ← Per-strategy eval results (run_search_eval.py output)
│   ├── report.html                    ← Visual evaluation dashboard (LLM-Wiki baseline)
│   └── report_search_compare.html     ← Search-strategy comparison report (generated)
├── agent/
│   ├── agent.py                       ← BluetoothWikiAgent — hand-rolled OpenAI-compatible tool-calling loop
│   ├── system_prompt.md               ← Citation rules + anti-hallucination prompt
│   ├── tools.py                       ← list_index, search_wiki (pluggable strategy), read_page, read_source
│   ├── citations.py                   ← Citation ↔ hosted-site URL mapping (single source of truth)
│   ├── json_extract.py                ← Shared JSON-payload extraction for LLM responses
│   └── config.py                      ← Env-driven config (model, paths, limits, search strategy)
├── search/                            ← Pluggable search strategies (see §4.4)
│   ├── base.py                        ← SearchHit / SearchResult / SearchStrategy protocol
│   ├── v0_naive.py                    ← v0: original substring scan (baseline)
│   ├── v1_ripgrep.py                  ← v1: ripgrep-backed ranked lexical search
│   ├── v2_hybrid.py                   ← v2: v1 + sufficiency loop + hybrid source fallback (RRF)
│   ├── chunker.py                     ← Core spec Vol/Part-aware structural chunker
│   ├── embeddings.py                  ← Local embedding model (bge-small) + cosine top-k
│   ├── index_store.py                 ← On-disk chunk/embedding index build & load
│   ├── fusion.py                      ← Reciprocal Rank Fusion
│   ├── sufficiency.py                 ← gpt-oss-120b "are these hits enough?" judge
│   ├── rg_util.py                     ← ripgrep subprocess wrapper
│   ├── render.py                      ← SearchResult → tool-output text envelope
│   └── index/                         ← Generated chunk/embedding indexes (gitignored)
├── qa/                                ← Spec Q&A Agent — Vector+Graph RAG behind one Tool (see §4.5)
│   ├── config.py                      ← Env-driven settings (BT_QA_*: models, budgets, paths)
│   ├── llm.py                         ← Shared chat/embeddings + schema-validated structured calls
│   ├── ontology.py                    ← Fixed entity/relation schema for constrained extraction
│   ├── prefilter.py                   ← Out-of-scope gate + document-family scope hint
│   ├── prompts.py                     ← Loop + forced-synthesis system prompts
│   ├── loop.py                        ← Agentic retrieval loop (budget, context compaction)
│   ├── verify.py                      ← Citation ↔ observed-evidence grounding check
│   ├── service.py                     ← SpecQAService.ask() → frozen Tool response
│   ├── ingest/
│   │   ├── structure.py               ← Markdown → sections/tables/figures/cross-refs
│   │   ├── pipeline.py                ← Graph skeleton + chunking + incremental embedding
│   │   └── extract.py                 ← Opt-in LLM entity extraction + figure descriptions
│   ├── retrieval/actions.py           ← vector_search, graph_lookup, graph_traverse,
│   │                                     get_section_text, get_figure, get_table
│   ├── store/
│   │   ├── base.py                    ← VectorStore / GraphStore protocols
│   │   ├── vector_local.py            ← numpy cosine top-k with metadata filtering
│   │   └── graph_sqlite.py            ← SQLite nodes/edges, alias lookup, bounded BFS
│   └── index/                         ← Generated vectors/graph.db/manifest/registry (gitignored)
├── server/
│   ├── http.py                        ← FastAPI test server (bluetooth-wiki-agent-http)
│   ├── qa_http.py                     ← Spec Q&A HTTP API (bluetooth-spec-qa-http)
│   ├── qa_mcp.py                      ← Spec Q&A MCP server (bluetooth-spec-qa-mcp)
│   ├── jobs.py                        ← In-memory background eval jobs
│   ├── schemas.py                     ← Pydantic request/response models
│   └── static/index.html              ← Single-page strategy comparison UI
├── scripts/
│   ├── download_spec_documents.py     ← Downloads PDFs from bluetooth.com
│   ├── convert_to_md.py               ← Converts PDFs → markdown + figure PNGs via PyMuPDF
│   ├── ingest.py                      ← Ingests new source docs into the wiki
│   ├── eval_one.py                    ← Run one eval question through agent + LLM judge
│   ├── build_search_index.py          ← Build chunk/embedding index per spec version
│   ├── run_search_eval.py             ← Run eval dataset across search strategies
│   ├── generate_search_report.py      ← Render strategy-comparison HTML report
│   ├── qa_ingest.py                   ← Build the Spec Q&A index (qa/index/)
│   └── smoke_test_agent.py            ← End-to-end agent smoke test
├── pyproject.toml                     ← Python deps: openai, mcp, fastapi, numpy (+ embeddings extra: sentence-transformers)
├── .env.example                       ← Env template (OPENAI_BASE_URL, OPENAI_API_KEY, BT_AGENT_MODEL, BT_AGENT_SEARCH_STRATEGY, …)
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
7. **Update** `README.md` (Coverage table, Structure section if directories changed) and `CLAUDE.md` (Directory Structure map, any affected rules or operation steps).

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

### 4.4 SEARCH — Pluggable retrieval strategies

The agent's `search_wiki` tool is backed by one of three strategies in `search/`,
selected via `BT_AGENT_SEARCH_STRATEGY` (or `BluetoothWikiAgent(search_strategy=...)`).
The tool's name, arguments, and output envelope are identical across strategies —
only retrieval quality and latency differ:

| Strategy | Mechanism | When to use |
|----------|-----------|-------------|
| `v0` | Naive case-insensitive substring scan (original) | Baseline / control in evals |
| `v1` | ripgrep multi-term ranked search (coverage/proximity/phrase scoring) | Fast, better lexical relevance |
| `v2` | v1 → gpt-oss-120b sufficiency judge → hybrid source fallback: ripgrep + local-embedding vector search fused with RRF, bounded reformulation loop (max `BT_AGENT_SUFFICIENCY_MAX_ITER`) | Deep questions needing raw spec text (opcodes, PDU details) |

Supporting workflows:
- **Index build** (required for v2's vector arm and chunk-precise citations):
  `python scripts/build_search_index.py --version 6.0 [--all] [--chunks-only]`.
  First full build downloads the `BAAI/bge-small-en-v1.5` model (~130 MB).
  `--chunks-only` works without ML deps; v2 then runs lexical-only with a note.
- **Strategy eval**: `python scripts/run_search_eval.py --strategies v0 v1 v2 --limit 5`
  → `eval/results_search_v*.json`; then `python scripts/generate_search_report.py --inputs ...`
  → `eval/report_search_compare.html` (quality + latency/cost side by side).
- **Live comparison UI**: `bluetooth-wiki-agent-http` (or `uvicorn server.http:app`) —
  ask one question through multiple strategies concurrently, or trigger an eval run
  and open the generated report from the browser.
- `search/chunker.py` is also the authority for `read_source`'s Vol/Part slicing
  (the old `[Vol N]` tagged-heading walk only matched front-matter and returned
  wrong sections; do not reintroduce it).

### 4.5 SPEC Q&A AGENT — Vector + Graph RAG behind one Tool

The `qa/` package is a **separate system** from the LLM-Wiki agent above, built to the
design in `docs/superpowers/plans/Bluetooth_Spec_QA_Agent_Design.md`. Where the wiki agent
searches curated wiki pages, this one indexes the **raw spec corpus** up front — removing
the wiki's cold-start problem — and is exposed to orchestrators as a single stateless Tool.

**Do not mix the two.** `qa/` must not import from `agent/` or `search/`, and vice versa.

Workflow:

1. **Ingest** — `python scripts/qa_ingest.py --version 6.0`
   Parses markdown structure into a graph skeleton (sections/tables/figures/cross-refs),
   chunks it (tables get their own chunks), and embeds via the endpoint's embedding API.
   Re-runs are cheap: a per-section content hash skips unchanged sections.
   `--dry-run` reports counts without calling the endpoint.
   `--extract` / `--figures` add the LLM-cost stages (ontology-constrained entity
   extraction, figure descriptions) — off by default.
2. **Serve** — `bluetooth-spec-qa-http` (POST `/qa/ask`) or `bluetooth-spec-qa-mcp`
   (MCP tool `bluetooth_spec_qa`). Both return the identical frozen response.
3. **Ask** — the loop pre-filters out-of-scope questions, then repeatedly chooses among six
   actions (`vector_search`, `graph_lookup`, `graph_traverse`, `get_section_text`,
   `get_figure`, `get_table`) until the evidence supports an answer or the budget runs out.

Invariants to preserve when changing this package:

- **The response key set is frozen**: `answer`, `citations`, `related_entities`,
  `confidence`, `out_of_scope`, `retrieval_trace`. Citations are
  `{doc, section, page, path}`. Orchestrators depend on this shape.
- **Citations are verified, never trusted.** `qa/verify.py` drops any citation with no
  matching evidence actually returned by an action during that run.
- **Budget exhaustion must stay visible** — it forces `confidence: "low"` rather than
  presenting a thin answer as a confident one.
- **Storage stays behind the protocols** in `qa/store/base.py`. The choice between
  server-form (Qdrant/Neo4j) and embedded (Chroma/KuzuDB) is still open; today's numpy +
  SQLite backends are the zero-dependency stand-in, not a commitment.
- **Section ids must stay unique.** Core specs restart section numbering in every
  Volume/Part, so `qa/ingest/structure.py` disambiguates repeated numbers by line. Removing
  that makes graph nodes overwrite each other and citations point at the wrong volume.

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

An alternative engine `scripts/convert_pymupdf4llm.py` (PyMuPDF4LLM 2-pass hybrid) is available
for supplemental PDFs (errata, profiles, test suites) and documents whose formatting breaks the
caption-driven heuristics. It keeps real markdown tables while extracting vector diagrams as
images (caption safety net), and prints a quality-gate report (mojibake count, captions without
images) — escalate a document to a model-based converter (e.g. Marker) when the gate fails.
Use `--suffix .p4l` to keep both engines' outputs side by side for comparison.
Prefer `convert_to_md.py` for Core Specs — it produces semantic figure names.

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
