# Bluetooth Spec Wiki

> Bluetooth Core Specification knowledge base for LLMs — based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

A structured, LLM-maintained wiki for Bluetooth Core Specifications (5.0–6.2).
Provides accurate, source-cited answers to natural-language questions about Bluetooth without reading hundreds of pages of spec PDFs.
Includes per-version summaries, version-diff indexes, concept pages, developer reference tables, and full converted markdown sources with extracted figures.

---

## Quick Start

```bash
git clone https://github.com/yalex-kim/bluetooth_wiki.git
cd bluetooth_wiki
claude
```

```
> What is Channel Sounding in Bluetooth 6.0?
> What changed between 5.1 and 5.2?
> What is the difference between LE Audio and Classic Bluetooth audio?
> What is PAwR used for?
> Show me the HCI command to set up a CIS.
```

---

## Structure

```
bluetooth_wiki/
├── CLAUDE.md                    ← LLM schema: defines how the wiki is maintained
├── index.md                     ← Full page catalog + query routing guide
├── log.md                       ← Append-only activity log
│
├── wiki/
│   ├── overview.md              ← Bluetooth technology overview
│   ├── versions/                ← Per-version summaries (Core Spec 5.0–6.2)
│   ├── version-diff/            ← Pre-indexed version-to-version diffs
│   ├── concepts/                ← Concept pages (BLE architecture, security, LE Audio, profiles…)
│   └── reference/               ← Developer reference tables (HCI commands, parameters…)
│
├── sources/
│   ├── README.md                ← How to download spec PDFs
│   └── specs/
│       ├── X.Y/                 ← One folder per Core Spec version
│       │   ├── Core_vX.Y.md             ← Full spec text converted via PyMuPDF
│       │   └── Core_vX.Y_images/        ← Extracted figure PNGs (Vol{N}_Part{P}_Figure{X_Y}.png)
│       ├── profiles/            ← Profile spec MDs: A2DP, HFP, AVRCP, HID, BAP, CAP, MAP… (14 profiles)
│       ├── conformance-profiles/ ← ICS (Implementation Conformance Statement) docs
│       └── test-suites/         ← TS (Test Suite) docs
│
├── eval/
│   ├── dataset.json                ← 42-question evaluation dataset (6 categories)
│   ├── rubric.md                   ← Scoring rubric (5 dimensions + difficulty weights)
│   ├── judge_prompt.md             ← LLM-as-Judge prompt + Python run_evaluation() helper
│   ├── judge.py                    ← Shared judge/scoring module (imported by all runners)
│   ├── runner.py                   ← Shared eval-suite runner (CLI + server jobs)
│   ├── report_render.py            ← Strategy-comparison HTML renderer
│   ├── results_wiki.json           ← LLM-Wiki baseline results (95.8%, 2026-05-04)
│   ├── results_search_v{0,1,2}.json ← Per-search-strategy results (generated)
│   ├── report.html                 ← Visual evaluation dashboard (baseline)
│   └── report_search_compare.html  ← Search-strategy comparison report (generated)
│
├── agent/                          ← Embedded agent loop (Phase 1, Python)
│   ├── agent.py                    ← BluetoothWikiAgent.ask() — single entry point
│   ├── system_prompt.md            ← Citation rules + anti-hallucination prompt
│   ├── tools.py                    ← list_index, search_wiki (pluggable), read_page, read_source
│   ├── citations.py                ← Citation ↔ hosted-site URL mapping
│   ├── json_extract.py             ← Shared JSON extraction for LLM responses
│   └── config.py                   ← Env-driven config (model, paths, limits, search strategy)
│
├── search/                         ← Pluggable search strategies (v0/v1/v2)
│   ├── v0_naive.py                 ← v0: original substring scan (baseline)
│   ├── v1_ripgrep.py               ← v1: ripgrep ranked lexical search
│   ├── v2_hybrid.py                ← v2: agentic loop + hybrid (ripgrep+vector, RRF) fallback
│   ├── chunker.py                  ← Core spec Vol/Part-aware structural chunker
│   ├── embeddings.py / index_store.py / fusion.py / sufficiency.py / rg_util.py / render.py
│   └── index/                      ← Generated chunk/embedding indexes (gitignored)
│
├── server/                         ← FastAPI test server + web UI
│   ├── http.py                     ← Routes (/api/compare, /api/eval/run, …)
│   ├── jobs.py                     ← In-memory background eval jobs
│   ├── schemas.py                  ← Pydantic models
│   └── static/index.html           ← Single-page strategy comparison UI
│
├── scripts/
│   ├── download_spec_documents.py  ← Download PDFs from bluetooth.com
│   ├── convert_to_md.py            ← Convert PDF → Markdown + figure PNGs via PyMuPDF
│   ├── convert_pymupdf4llm.py      ← Alternative engine (PyMuPDF4LLM) for supplemental PDFs / A-B comparison
│   ├── ingest.py                   ← Workflow for reflecting new specs into the wiki
│   ├── eval_one.py                 ← Run one eval question through agent + LLM judge
│   ├── build_search_index.py       ← Build chunk/embedding index per spec version
│   ├── run_search_eval.py          ← Run eval dataset across search strategies
│   ├── generate_search_report.py   ← Render strategy-comparison HTML report
│   └── smoke_test_agent.py         ← End-to-end agent smoke test
│
└── guide/
    └── claude-code-integration.md  ← Claude Code integration guide
```

---

## Coverage

| Version | Release | Key Feature | Source |
|---------|---------|-------------|--------|
| [5.0](wiki/versions/core-spec-5.0.md) | 2016-12 | 2× speed (LE 2M PHY), 4× range (Coded PHY), 8× broadcast capacity | PDF + MD ✓ |
| [5.1](wiki/versions/core-spec-5.1.md) | 2019-01 | Direction Finding (AoA/AoD), GATT caching | PDF + MD ✓ |
| [5.2](wiki/versions/core-spec-5.2.md) | 2019-12 | LE Audio, LC3 codec, Isochronous Channels (CIS/BIS), EATT | PDF + MD ✓ |
| [5.3](wiki/versions/core-spec-5.3.md) | 2021-07 | Connection Subrating, Enhanced Connection Update | PDF + MD ✓ |
| [5.4](wiki/versions/core-spec-5.4.md) | 2023-02 | PAwR, Encrypted Advertising Data (EAD) | PDF + MD ✓ |
| [6.0](wiki/versions/core-spec-6.0.md) | 2024-08 | Channel Sounding (sub-meter ranging), DBAF | PDF + MD ✓ |
| [6.1](wiki/versions/core-spec-6.1.md) | 2025-04 | Randomized RPA Updates (enhanced BLE privacy) | PDF + MD ✓ |
| [6.2](wiki/versions/core-spec-6.2.md) | 2025-11 | Shorter Connection Intervals (375 µs), LE UTP, CS security hardening | PDF + MD ✓ |

Version diffs: [5.0→5.1](wiki/version-diff/diff-5.0-to-5.1.md) · [5.1→5.2](wiki/version-diff/diff-5.1-to-5.2.md) · [5.2→5.3](wiki/version-diff/diff-5.2-to-5.3.md) · [5.3→5.4](wiki/version-diff/diff-5.3-to-5.4.md) · [5.4→6.0](wiki/version-diff/diff-5.4-to-6.0.md) · [6.0→6.1](wiki/version-diff/diff-6.0-to-6.1.md) · [6.1→6.2](wiki/version-diff/diff-6.1-to-6.2.md)

---

## Evaluation

The `eval/` directory contains a quality-measurement suite for comparing LLM-Wiki against RAG-based systems.

| File | Purpose |
|------|---------|
| `dataset.json` | 30 test questions across 6 categories with reference answers and key facts |
| `rubric.md` | Scoring criteria: accuracy, completeness, citation, hallucination penalty, usability |
| `judge_prompt.md` | LLM-as-Judge prompt + `run_evaluation()` Python helper for automated scoring |
| `results_wiki.json` | LLM-Wiki baseline: **95.8%** overall (521.5 / 544.5 weighted, 2026-05-04) |
| `report.html` | Visual dashboard — open in browser to see category breakdown and improvement areas |

To run a RAG comparison: collect answers from your RAG system for all questions, call `run_evaluation()` from `judge_prompt.md`, and save results as `eval/results_rag.json`.

### Search-strategy comparison

The agent's `search_wiki` tool has three interchangeable backends (see [Search Strategies](#search-strategies)). To score them against each other on the same dataset:

```bash
# smoke run first — a full run is strategies × 42 agent calls + judge calls
.venv/bin/python scripts/run_search_eval.py --strategies v0 v1 v2 --limit 5
# → eval/results_search_v0.json, _v1.json, _v2.json (scores + latency/cost telemetry)

.venv/bin/python scripts/generate_search_report.py \
    --inputs eval/results_search_v0.json eval/results_search_v1.json eval/results_search_v2.json
# → eval/report_search_compare.html (side-by-side quality + latency/cost)
```

---

> **Maintenance rule**: Before committing any wiki changes, update `README.md` (Coverage table, Structure section) and `CLAUDE.md` (Directory Structure map, affected operation steps) to keep them in sync with the actual repo.

---

## Adding a New Version

When a new Core Spec is released:

```bash
# 1. Place the PDF in sources/specs/X.Y/
python scripts/download_spec_documents.py

# 2. Convert to Markdown + figure PNGs
pip install PyMuPDF
python scripts/convert_to_md.py X.Y
# → sources/specs/X.Y/Core_vX.Y.md
# → sources/specs/X.Y/Core_vX.Y_images/*.png

# 3. Check status
python scripts/ingest.py --status

# 4. Run INGEST in Claude Code
claude
> Ingest Core Spec X.Y from sources/specs/X.Y/Core_vX.Y.md into the wiki
```

---

## Agent (Phase 1)

The `agent/` package wraps the wiki in an embedded agentic loop so any client (HTTP, MCP, web sidebar) gets the same answer quality. Built on a hand-rolled OpenAI-compatible tool-calling loop, talking to a gpt-oss-120B endpoint.

```bash
python3 -m venv .venv --without-pip
curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python
.venv/bin/pip install -e .

cp .env.example .env  # fill in OPENAI_BASE_URL, OPENAI_API_KEY, SITE_BASE_URL
.venv/bin/python scripts/smoke_test_agent.py "Which version introduced Channel Sounding?"
```

Per-question evaluation:

```bash
.venv/bin/python scripts/eval_one.py Q027 --save
# → score breakdown + saves to eval/results_agent.json
```

Tunable env vars: `BT_AGENT_MODEL` (default `gpt-oss-120b`), `BT_AGENT_MAX_TURNS`, `SITE_BASE_URL`, plus the search-strategy knobs below.

The agent emits citations as `{label, file_path}` and `agent/citations.py` resolves them to deep-link URLs into a hosted MkDocs site (planned Phase 3).

---

## Search Strategies

The agent's `search_wiki` tool is pluggable — three backends live in `search/`, selected via `BT_AGENT_SEARCH_STRATEGY` or `BluetoothWikiAgent(search_strategy=...)`. Tool name/args/output format are identical across strategies, so they A/B/C-test cleanly:

| Strategy | Mechanism | Trade-off |
|----------|-----------|-----------|
| `v0` | Naive substring scan over all markdown (the original) | Baseline for evals |
| `v1` **(default)** | ripgrep multi-term search, ranked by term coverage / proximity / exact-phrase; source hits bucketed to Vol/Part chunks | Fast, much better lexical relevance; no ML deps |
| `v2` | v1 first → a gpt-oss-120b judge decides if hits suffice → if not, hybrid retrieval over `sources/specs/` (ripgrep + local-embedding vector search fused with Reciprocal Rank Fusion), with a bounded query-reformulation loop | Highest quality on deep spec questions (opcodes, PDU details); slower per call |

v2's sufficiency loop runs *inside* one tool call, so it never consumes the main agent's turn budget. Source hits are resolved to structural chunks (`search/chunker.py`) carrying correct `Vol/Part/§` metadata — this chunker also fixed `read_source`, which previously matched only front-matter `[Vol N]` tags and returned the wrong sections.

### Building the search index

v2's vector arm (and chunk-precise citations) needs a per-version index:

```bash
.venv/bin/pip install -e ".[embeddings]"     # sentence-transformers (+ torch)
.venv/bin/python scripts/build_search_index.py --version 6.0   # or --all
# → search/index/6.0/{chunks.jsonl, embeddings.npy, meta.json}   (gitignored)
```

First run downloads `BAAI/bge-small-en-v1.5` (~130 MB) from Hugging Face. Builds are idempotent (source sha256 + chunker version + model fingerprint). Without ML deps, `--chunks-only` still enables chunk-accurate lexical search; v2 then notes that its vector arm is off.

Search env vars: `BT_AGENT_SEARCH_STRATEGY` (v0|v1|v2), `BT_AGENT_EMBED_MODEL`, `BT_AGENT_RRF_K`, `BT_AGENT_SUFFICIENCY_MODEL`, `BT_AGENT_SUFFICIENCY_MAX_ITER`.

---

## Web UI (strategy test server)

`server/` implements the `bluetooth-wiki-agent-http` entry point: a FastAPI server with a single-page UI for comparing strategies live.

```bash
.venv/bin/pip install -e .
bluetooth-wiki-agent-http                 # or: .venv/bin/uvicorn server.http:app --port 8080
# → http://localhost:8080
```

- **Compare** — type a question, tick v0/v1/v2, get answers + citations + wall-time + cost side by side (strategies run concurrently).
- **Run eval** — trigger an eval-suite run (with a question limit) in the background, watch progress, then open the generated comparison report.

API: `POST /api/compare`, `POST /api/eval/run` → `{job_id}`, `GET /api/eval/status/{job_id}`, `GET /api/eval/report/{job_id}`, `GET /api/health`. Jobs are in-memory (single process; lost on restart). Env: `BT_AGENT_HTTP_HOST`, `BT_AGENT_HTTP_PORT` (default 8080).

---

## Using from Another Project

Register as an MCP Filesystem server in `~/.claude/claude.json` to use from any project:

```json
{
  "mcpServers": {
    "bluetooth-wiki": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/bluetooth_wiki"]
    }
  }
}
```

See [guide/claude-code-integration.md](guide/claude-code-integration.md) for details.

---

## Architecture

3-layer structure from [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern:

```
Layer 1  sources/specs/   Converted spec PDFs (.md + _images/) — read-only, source of truth
Layer 2  wiki/            LLM-maintained summaries, diffs, concepts, references — grows with each query
Layer 3  CLAUDE.md        Schema: defines how the LLM manages the wiki
```

### System Concept Diagram

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  Bluetooth SIG                                                   │
  │  ┌──────────────────────────────────────────────────────────┐    │
  │  │  Core Spec PDFs  ·  Profile PDFs  ·  ICS / TS Docs       │    │
  │  └───────────────────────────┬──────────────────────────────┘    │
  └──────────────────────────────│──────────────────────────────────-┘
                                 │ scripts/convert_to_md.py
                                 │ (PyMuPDF: text + figure PNGs)
                                 ▼
  ┌────────────────────────────────────────────────┐
  │  Layer 1 — sources/specs/  (read-only)         │
  │                                                │
  │  Core_vX.Y.md  ·  profiles/*.md                │
  │  conformance-profiles/  ·  test-suites/        │
  └────────────────────┬───────────────────────────┘
                       │  reads (source of truth)
                       │
         ┌─────────────▼───────────────┐
         │  LLM  (Claude + CLAUDE.md)  │◀──── Layer 3: CLAUDE.md
         │                             │      (schema: INGEST /
         │  INGEST   QUERY   LINT      │       QUERY / LINT rules)
         └──────┬─────────────┬────────┘
                │ writes      │ answers
                ▼             │
  ┌─────────────────────────────────────────────────────┐
  │  Layer 2 — wiki/  (LLM-maintained, ever-growing)    │
  │                                                     │
  │  versions/     per-version summaries (5.0 – 6.2)    │
  │  version-diff/ pre-indexed version diffs            │
  │  concepts/     concept pages (BLE, security, audio) │
  │  reference/    developer references (HCI commands…) │
  └──────────────────────────┬──────────────────────────┘
                             │ reads wiki
                             ▼
              ┌──────────────────────────┐
              │      Developer           │
              │                          │
              │  "How does Channel       │
              │   Sounding work?"        │
              │                          │
              │  "Which HCI command      │
              │   sets up a CIS?"        │
              └──────────────┬───────────┘
                             │ query reveals a gap
                             ▼
              ┌──────────────────────────────────────┐
              │  LLM creates a new page or enriches  │  ← Wiki growth loop
              │  an existing one on the spot         │
              └──────────────────────────────────────┘
```

**Wiki growth loop**: When a user asks a question and the LLM finds that the existing wiki pages don't fully cover the topic, it creates a new page or enriches an existing one in the same session. The wiki gets more complete with every query.

### LLM Operations

| Operation | Trigger | Action |
|-----------|---------|--------|
| **INGEST** | New spec PDF added | Read sources/ → create/update wiki pages → append to log.md |
| **QUERY** | User question | Read index.md → load relevant pages → answer → fill any gap found |
| **LINT** | Periodic health check | Detect contradictions, orphan pages, stale claims, broken links |
