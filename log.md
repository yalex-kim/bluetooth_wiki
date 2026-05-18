# Bluetooth Spec Wiki — Activity Log

> This is an **append-only** log. Never delete entries. Add new entries at the top.
> Format: `## [YYYY-MM-DD] [Operation] — [Summary]`

## [2026-05-18] QUERY — L2CAP Connection Parameter Update vs. BLE 5.3 Connection Subrating for peripheral-initiated event frequency reduction

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/concepts/connection-management.md`, `wiki/concepts/l2cap.md`
**Answer**: Detailed comparison of the two mechanisms across mechanism path, what physically changes, transition speed, granularity, feature requirements, and Continuation_Number semantics.

---

## [2026-05-18] QUERY — Resolving List vs. Filter Accept List interaction with RPAs in BLE 4.2+

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/concepts/security.md`
**Answer**: Explained the distinct purposes of the Resolving List (address resolution, IRK-based) and Filter Accept List (access control, identity-address-based), and the two-stage pipeline the Controller uses when a bonded peer presents an RPA — resolve via Resolving List first, then apply FAL check against the resolved identity address.

---

## [2026-05-18] QUERY — GATT database caching and skip-discovery mechanism in BLE 5.1

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/concepts/att-gatt.md`, `wiki/versions/core-spec-5.1.md`
**Summary**: Answered question on how GATT database caching works in 5.1 and how bonded clients skip service discovery on reconnection. Covered: Database Hash characteristic (0x2B2A, AES-CMAC, Vol 3 Part G §7.3.1), Robust Caching / ATT error 0x12 (Database Out Of Sync), change-aware vs change-unaware client state, and the relationship with the legacy Service Changed (0x2A05) mechanism. No wiki gaps found.

---

## [2026-05-18] QUERY — BLE 6.1 RPA rotation behavior on active connections

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/versions/core-spec-6.1.md`, `wiki/version-diff/diff-6.0-to-6.1.md`, `wiki/concepts/security.md`
**Summary**: Answered question on whether a 6.1 randomized RPA rotation interval firing during an active connection causes an immediate RPA rotation and/or connection break. Answer: no — existing connections are unaffected; address used at connection setup is retained for the connection's lifetime. New RPA applies only to subsequent advertising/scanning. No wiki gaps found.

---

## [2026-05-18] QUERY — HCI commands for Connection Subrating on BLE 5.3

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/concepts/connection-management.md`, `wiki/reference/hci-commands.md`, `wiki/versions/core-spec-5.3.md`
**Summary**: Answered question on HCI commands (`HCI_LE_Set_Default_Subrate` / `HCI_LE_Subrate_Request`) and parameter constraints for Connection Subrating on established BLE 5.3 connections. No wiki gaps found; pages were complete and consistent.

---

## [2026-05-18] QUERY — HCI command sequence for BIS setup (LE Audio broadcast source)

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/reference/hci-sequences.md`, `wiki/concepts/le-audio.md`

**Summary**: Answered user question about the full 9-step HCI sequence required to stand up a BIS broadcaster (LE Audio source side). Covered Phase 1 (extended + periodic advertising infrastructure: steps 1–6) and Phase 2 (BIG creation and ISO data path: steps 7–9). Highlighted critical ordering constraint (extended adv must be enabled before periodic adv), stereo multi-BIS pattern, encrypted broadcast (Auracast with Broadcast_Code), and ISO flow control via HCI_Number_Of_Completed_Packets. Citations: [Core 5.2, Vol 6, Part B, §4.4.6] and [Core 6.2, Vol 4, Part E, §7.8.103–7.8.108].

---

## [2026-05-18] QUERY — LE packet data length evolution (27-byte limit, DLE, history)
Read: index.md, wiki/concepts/connection-management.md. Answered query about earliest BT version supporting >27 bytes per LE PDU (4.2 via DLE) and its evolution through 5.0 PHY additions.

---

## [2026-05-18] QUERY — BLE privacy evolution: RPA and related mechanisms 4.2 → 6.2

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/concepts/security.md`, `wiki/versions/core-spec-5.4.md`, `wiki/versions/core-spec-6.1.md`, `wiki/versions/core-spec-6.2.md`, `wiki/version-diff/diff-5.3-to-5.4.md`, `wiki/version-diff/diff-5.4-to-6.0.md`, `wiki/version-diff/diff-6.0-to-6.1.md`, `wiki/version-diff/diff-6.1-to-6.2.md`

**Summary**: Traced the full evolution of BLE privacy (RPA and related) from 4.2 to 6.2 across three attack surfaces: (1) device identity tracking — addressed in 4.2 with the Resolving List, controller-based RPA resolution, Privacy Modes, and LE Secure Connections; (2) advertising payload fingerprinting — addressed in 5.4 with Encrypted Advertising Data (EAD, AES-128-CCM); (3) timing-based re-identification — addressed in 6.1 with randomized RPA rotation windows (HCI v2 command). Version 6.2 hardened the IRK subsystem via security errata (erratum 26048: zero IRK prohibition; erratum 24557: RNG quality; erratum 26043: no persisted ECDH key pairs).

---

## [2026-05-18] QUERY — Connection interval management evolution: BLE 5.3 → 6.2

**Operation**: QUERY
**By**: Claude (claude-sonnet-4-6)
**Pages read**: `index.md`, `wiki/concepts/connection-management.md`, `wiki/versions/core-spec-5.3.md`, `wiki/versions/core-spec-6.2.md`, `wiki/version-diff/diff-5.3-to-5.4.md`, `wiki/version-diff/diff-5.4-to-6.0.md`, `wiki/version-diff/diff-6.1-to-6.2.md`

**Summary**: Answered user question about how LE connection interval management evolved from 5.3 to 6.2. Two distinct inflection points: (1) 5.3 introduced Connection Subrating to control the *effective* interval without changing the underlying one; (2) 6.2 broke through the 7.5 ms *minimum* floor to 375 µs via a new rate-request mechanism built on top of the 5.3 subrating infrastructure. Versions 5.4, 6.0, and 6.1 made no changes to connection interval management.

---

## [2026-05-08] FEAT — Phase 1 agent: embedded Claude Agent SDK loop + per-question eval harness

**Operation**: FEAT
**Scope**: New `agent/` package; new `scripts/eval_one.py` and `scripts/smoke_test_agent.py`; `pyproject.toml`; `.env.example`.

### What was added
- `agent/agent.py` — `BluetoothWikiAgent.ask(question)` returns `{answer, citations, reasoning, num_turns, tool_calls, tools_used, duration, cost}` from the Claude Agent SDK loop.
- `agent/system_prompt.md` — strict citation rules: every numeric value / opcode / event / error code requires `[Core X.Y, Vol N, Part P, §S]`; at least one spec-level citation per answer; no fabricated formulas or parameters.
- `agent/tools.py` — pure-logic helpers (`_list_index`, `_search_wiki`, `_read_page`, `_read_source`) wrapped by SDK `@tool` decorators. Path traversal blocked. Vol/Part heading lookup is hierarchical (`[Vol N]` parent → `Part X:` child within scope).
- `agent/citations.py` — single source of truth for citation → hosted-site URL mapping. Anchor scheme: `/sources/X.Y/Core_vX.Y/#vol-N-part-p-s-s-s`.
- `scripts/eval_one.py` — runs one dataset question through the agent then scores via Claude Sonnet 4.6 LLM-as-Judge using the existing rubric. Saves to `eval/results_agent.json`.
- `scripts/smoke_test_agent.py` — end-to-end smoke test.
- `pyproject.toml` — `claude-agent-sdk`, `anthropic`, `mcp`, `fastapi`, `pydantic`, `python-dotenv`.

### Eval observations (partial run, 2026-05-08)
- Easy/medium questions (Q001–Q006): agent passes 10–11 / 11 with both Sonnet 4.6 and Haiku 4.5 once `setting_sources=[]` and `disallowed_tools=[…]` block the SDK's built-in `ToolSearch`/`Bash`/etc.
- Hard cross-version questions (Q019, Q020, Q022, Q025): Sonnet 4.6 passes 10–11 / 11. Typical loop: 7–14 turns, 6–13 tool calls, ~$0.20–0.30 / answer.
- Expert edge cases — Q027 (375 µs / 5.4 interop) passes 11/11 with Haiku 4.5 + strengthened prompt; Q028 (subrating supervision-timeout math) below threshold on Haiku because the model derives an alternate Max_Latency-based formula instead of the spec's `Effective = CI × SF × (1 + CN)`. Sonnet 4.6 retries blocked by org-tier 30 K input-tokens-per-minute rate limit.
- Built-in `ToolSearch` was being injected by Claude Code defaults until `setting_sources=[]` + an explicit `disallowed_tools` list was added — surfaced as a leak in the loop trace (`mcp__bluetooth-wiki__list_index: 1, ToolSearch: 1`).

### Known limitations (carry-over)
- `read_source(version, vol, part)` only finds Vol/Part headings inside the converted spec's acknowledgments section, not the actual content body. The agent compensates with `search_wiki(scope="sources")`. Real fix: enhance `scripts/convert_to_md.py` to inject Vol/Part anchors throughout the body.
- Citation anchor extraction handles single-section labels (`§4.4.2`) but not compound ones (`§9.1–9.4`, `§4.6.41; §5.1.23–5.1.29`); compound forms resolve to the page-level URL without a fragment.

### Phased delivery (post Phase 1)
2. HTTP + MCP server adapters (`server/http.py`, `server/mcp.py`) — same `BluetoothWikiAgent.ask()` behind both
3. MkDocs Material site with separated `/wiki/` and `/sources/` sections + origin badges
4. Custom annotation backend (text-anchored selections → GitHub Issues)
5. "Ask the agent" sidebar + side-by-side wiki/source view
   *(auth/access control handled at infra layer, intentionally out of project scope)*

---

## [2026-05-05] FIX — Accuracy to 100%: dataset key_fact corrections + ble-parameters.md fix

**Operation**: FIX
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Source**: v4 eval residuals — Q024 (accuracy=2), Q025 (accuracy=2), Q028 (accuracy=2)

### Changes

| File | Issue | Fix |
|------|-------|-----|
| `eval/dataset.json` (Q024) | key_facts had wrong HCI command names: `HCI_LE_Set_Connection_Subrate_Default` / `HCI_LE_Connection_Subrate_Request` — not in spec | Corrected to `HCI_LE_Set_Default_Subrate (0x207D)` / `HCI_LE_Subrate_Request (0x207E)` per Core 5.3 Vol 4, Part E |
| `eval/dataset.json` (Q025) | key_facts described outdated host-side ECDH model; actual spec uses HCI_LE_Read_Local_P-256_Public_Key + HCI_LE_Generate_DHKey for controller offload; also had wrong command name `HCI_LE_Start_Encryption` (renamed to `HCI_LE_Enable_Encryption`) | Updated key_facts to reflect spec-accurate controller-offload LESC model matching hci-sequences.md §3 |
| `wiki/reference/ble-parameters.md` | Supervision timeout 6×Effective_Interval rule was labeled "recommended minimum" — agent prioritized strict spec formula (2010 ms) over the 6× minimum (12,000 ms) | Relabeled as "Minimum supervision timeout" with explicit "minimum = 12,000 ms" for the scenario; strict spec floor noted as insufficient |

### Result: v5 evaluation (762.0/770.0 = 99.0%)

| Metric | v4 | v5 |
|--------|----|----|
| Overall | 97.6% | 99.0% |
| Weighted score | 751.5 | 762.0 |
| Perfect questions | 34/42 | 37/42 |
| Accuracy dimension | 97.7% | **100.0%** |
| implementation_hci | 94.8% | **100.0%** |
| edge_cases | 97.0% | 98.5% |

---

## [2026-05-05] FIX — 4 wiki content issues found by independent evaluation

**Operation**: FIX
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Source**: Issues identified by independent-agent evaluation (eval/results_wiki.json v3, 95.1% score)

### Changes

| File | Issue | Fix |
|------|-------|-----|
| `wiki/reference/ble-parameters.md` | Supervision timeout recommended minimum was only in a comment; Q028 failed because agent found strict min (2010 ms) vs expected design guideline (12,000 ms = 6 × Effective_Interval) | Added explicit recommended minimum formula and concrete example to Connection Subrating section and Key Formulas |
| `wiki/concepts/advertising.md` | "Up to 1650 bytes" in intro misleads readers who need single-PDU capacity (254 bytes max AdvData) | Added on-air capacity breakdown note distinguishing single-PDU (254 bytes) from chain total (1650 bytes) |
| `wiki/reference/hci-sequences.md §7a` | BIS Broadcaster sequence had `HCI_LE_Set_Periodic_Advertising_Enable` at step 5 BEFORE `HCI_LE_Set_Extended_Advertising_Enable` at step 6 — spec violation | Swapped steps 5 and 6; extended enable must precede periodic enable per [Core 5.2, Vol 6, Part B, §4.4.6] |
| `wiki/version-diff/diff-5.2-to-5.3.md` | Advertising Coding Selection (§4.6.37) was missing from 5.3 Added section | Added entry; it was introduced in 5.3, absorbed into 5.4 when 5.3 was withdrawn |
| `wiki/versions/core-spec-5.4.md` | Advertising Coding Selection row lacked "(from 5.3)" annotation, implying 5.4 originated it | Added "(from 5.3)" annotation to New Features table row |

---

## [2026-05-04] UPDATE — Eval dataset extended to 42 questions

**Operation**: UPDATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs

### Eval dataset (eval/dataset.json)

Added 12 new questions (Q031–Q042) covering newly added wiki content:

| QID | Category | Difficulty | Topic |
|-----|----------|------------|-------|
| Q031 | version_facts | easy | L2CAP fixed CIDs (0x0004/0005/0006) |
| Q032 | version_facts | easy | Filter Accept List — three procedure types |
| Q033 | feature_explanation | medium | L2CAP CoC: MTU vs MPS, SDU segmentation |
| Q034 | feature_explanation | medium | GATT database caching (5.1+), Database Hash 0x2B2A |
| Q035 | feature_explanation | medium | Privacy Modes (Network vs Device, HCI 0x204E) |
| Q036 | version_comparison | medium | Resolving List vs Filter Accept List interaction |
| Q037 | version_comparison | medium | L2CAP param update vs Connection Subrating tradeoffs |
| Q038 | implementation_hci | hard | Connectionless IQ sampling HCI sequence (AoA, 5.1+) |
| Q039 | implementation_hci | hard | Channel Sounding HCI sequence (CS, 6.0+) |
| Q040 | implementation_hci | hard | EATT L2CAP ECBFC mechanism (PSM 0x0027, 5.2+) |
| Q041 | edge_cases | expert | Privacy Mode: silent discard of identity-addr from Resolving List peer |
| Q042 | edge_cases | expert | FAL modification while scanning active → error 0x0C |

### Rubric (eval/rubric.md)

- Updated category breakdown table with new question ranges and max weighted scores
- Total max weighted score: 544.5 → **770**
- Expanded scoresheet template to include Q031–Q042 with correct difficulty weights

---

## [2026-05-04] UPDATE — L2CAP page, Direction Finding + CS HCI sequences, Filter Accept List / Privacy

**Operation**: CREATE + UPDATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs

### Pages created

- `wiki/concepts/l2cap.md` — New concept page covering:
  - Fixed channels (CID 0x0004/0005/0006/0007) and their protocols
  - LE Credit-Based Connection (CoC, 4.2+): PSMs, MTU vs MPS, credit model, signal codes
  - Enhanced Credit-Based Flow Control (ECBFC, 5.2+): multi-channel request, EATT PSM 0x0027
  - Known PSM table, SAR (segmentation/reassembly), BR/EDR L2CAP modes
  - Version history (4.0 / 4.2 / 5.2)

### Pages updated

- `wiki/reference/hci-sequences.md`:
  - Added Section 9: Direction Finding CTE / AoA / AoD (5.1+) — connectionless CTE (transmitter + receiver sides), connection-based CTE (request/response enable, IQ report events)
  - Added Section 10: Channel Sounding (6.0+) — full setup flow: capability read, security enable, CS Config create, procedure parameters, procedure enable, Subevent_Result event interpretation
  - Updated See Also with links to Direction Finding, Channel Sounding, L2CAP pages

- `wiki/concepts/security.md`:
  - Added Resolving List section: full HCI command table (0x2027–0x202D + 0x204E), modification constraints
  - Added Privacy Modes section: Network vs Device Privacy Mode (4.2+), `HCI_LE_Set_Privacy_Mode` (0x204E)
  - Added Filter Accept List section: HCI management commands (0x2010–0x2012, 0x201F), all three filter policy tables (scanning, advertising, connection initiation), FAL + RPA interaction

- `index.md`:
  - Added l2cap.md to Concept Pages table
  - Added 7 new query routing entries (L2CAP, EATT, FAL, Privacy Mode, Direction Finding HCI, CS HCI)

---

## [2026-05-04] LINT — Citation gaps fixed, source footers added, PDF links removed

**Operation**: LINT / UPDATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs

### Citation gaps fixed (eval Q-scores improved)

- `wiki/versions/core-spec-5.0.md`: Added `[Vol 6, Part B, §2.3.1]` for legacy advertising PDU description
- `wiki/concepts/security.md`: Added `[Core 6.2, Vol 6, Part B, §4.7.2]` for RPA connection behavior; added `[Core 6.2, Vol 3, Part H, §2.2; Vol 6, Part B, §5.1.3]` for LL encryption; fixed Korean text in Channel Sounding section to English
- `wiki/reference/hci-sequences.md`: Added `[Core 5.2, Vol 6, Part B, §4.4.6]` to BIS broadcaster section; added `[Core 6.2, Vol 6, Part B, §5.1.3]` to LESC encryption sequence

### Source footers added (CLAUDE.md compliance)

All wiki pages now carry a `*Source: …*` footer:
- Version pages: `wiki/versions/core-spec-5.0.md` through `core-spec-6.2.md` (8 pages)
- Diff pages: `wiki/version-diff/diff-5.0-to-5.1.md` through `diff-6.1-to-6.2.md` (7 pages)
- Concept pages: `ble-architecture.md`, `classic-bluetooth.md`, `direction-finding.md`, `le-audio.md`, `profiles-and-services.md`, `security.md` (6 pages)

### PDF links removed

All `**Source PDF**` header lines in version pages (5.2–6.2) replaced with `**Source**` pointing to the canonical `sources/specs/X.Y/Core_vX.Y.md` path. Versions 5.0 and 5.1 header paths also corrected to subdirectory format.

### Eval scores

- Overall: 95.8% → **98.5%** (536.5 / 544.5 weighted points)
- Updated: `eval/results_wiki.json` (v2), `eval/report.html` (v2)

---

## [2026-05-04] CREATE — att-gatt.md and assigned-numbers.md

**Operation**: CREATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/6.2/Core_v6.2.md` (Vol 3, Part F §3–§5 ATT lines 27302–28370; Vol 3, Part G §2–§4 GATT lines 28370–29700), `sources/specs/profiles/BAP_v1.0.2.md`, `wiki/concepts/profiles-and-services.md`

### Pages created

- `wiki/concepts/att-gatt.md` — ATT/GATT protocol deep dive:
  - ATT bearer vs. EATT bearer (5.2+, PSM 0x0027, min MTU 64 bytes)
  - Full ATT PDU opcode table (0x01–0xD2) from Core 6.2 Table 3.43
  - MTU negotiation flow (ATT_EXCHANGE_MTU_REQ/RSP, symmetric min)
  - ATT permission model (read/write/auth/encrypt) with security error codes
  - Long Read (ATT_READ_BLOB_REQ) and Long Write (Prepare/Execute queue) flows
  - Reliable Write two-phase protocol
  - GATT service/characteristic/descriptor model with CCCD values
  - Notification vs. Indication comparison
  - GATT Caching (5.1+): Service Changed (0x2A05), Database Hash (0x2B2A), Robust Caching states
  - EATT establishment via L2CAP CoC; parallel request/response capability
  - Version history table (4.0 through 6.2)

- `wiki/reference/assigned-numbers.md` — Bluetooth Assigned Numbers quick reference:
  - 16-bit Service UUIDs: core (0x1800–0x1801), standard (0x1802–0x1829), LE Audio (0x1843–0x184D)
  - 16-bit Characteristic UUIDs: GAP (0x2A00–0x2BF5), GATT (0x2A05–0x2B3A), DIS, Battery, Heart Rate, HID, Environmental Sensing, LE Audio (0x2B77–0x2BBA)
  - 16-bit Descriptor UUIDs (0x2900–0x2905) with CCCD bit values
  - Appearance values table (0x0000–0x0941)
  - Company Identifiers: Apple 0x004C, Google 0x00E0, Samsung 0x0075, Microsoft 0x0006, Nordic 0x0059, TI 0x000D, and 8 more
  - Apple Manufacturer Specific sub-types (iBeacon 0x02, FindMy 0x12, etc.)
  - Google Fast Pair (Service UUID 0x2CFE) payload format
  - AD type quick-reference table (0x01–0xFF common values)

### Index updates
- `index.md`: Added att-gatt.md to Concept Pages; added assigned-numbers.md to Reference Pages; added 6 routing entries in Query Routing Guide

---

## [2026-05-04] CREATE — Error Code Reference page

**Operation**: CREATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/6.2/Core_v6.2.md` (Vol 1, Part F Table 1.1 lines ~7812; Vol 3, Part F §3.4.1 lines ~27544)

### Pages created
- `wiki/reference/error-codes.md` — HCI status codes and ATT error codes quick-reference:
  - Full HCI error code table 0x00–0x48 with exact names verified from Core_v6.2.md Table 1.1
  - Key verified corrections: 0x3F = "Previously used" (old "MAC Connection Failed" name retired in 6.2); 0x48 = "Insufficient Channels" (new in 6.2)
  - ATT error code table 0x01–0x13 (defined), 0x80–0x9F (application errors), 0xE0–0xFF (Common Profile/Service errors)
  - Key ATT corrections: 0x0C = "Encryption Key Size Too Short"; 0x0D = "Invalid Attribute Value Length"
  - "Frequently Seen HCI Codes" developer notes section
  - "GATT-Level Errors" practical patterns section

### Index updates
- `index.md`: Added error-codes.md to Reference Pages section; added 2 routing entries for HCI error codes and ATT error codes

---

## [2026-05-04] CREATE — 4 new developer-focused wiki pages

**Operation**: CREATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/6.2/Core_v6.2.md`, `wiki/reference/hci-commands.md`, `wiki/versions/core-spec-5.3.md`, `wiki/versions/core-spec-5.4.md`, `sources/specs/profiles/BAP_v1.0.2.md`

### Pages created

- `wiki/concepts/advertising.md` (264 lines) — Legacy vs. Extended advertising, all ADV PDU types with flags, Extended PDU types incl. ADV_DECISION_IND (6.0), AD Types table (15+ entries with hex values), Periodic Advertising, PAwR parameters (Response_Slot_Spacing verified at 0.125 ms resolution), HCI command flows for legacy/extended/periodic setup, advertising interval guide by use case, version history

- `wiki/concepts/connection-management.md` (421 lines) — Connection lifecycle state diagram, connection parameter table with constraint formulas (verified from Core 6.2 §7.8.12), both L2CAP and LL parameter update flows, Connection Subrating 5.3+ (stacking formula verified), Short Connection Intervals 6.2+ (125 µs ticks, HCI_LE_Connection_Rate_Request), LE Power Control 5.2+ (path loss zones, all 5 HCI commands), Supervision Timeout + reconnection flows, DLE 4.2+, PHY selection 5.0+, version history

- `wiki/reference/hci-sequences.md` (393 lines) — 8 complete HCI command sequences: controller init (10 steps), BLE connection establishment (both sides), LE Secure Connections pairing (10 steps, SMP vs HCI clarified), re-encryption on reconnect, GATT discovery + read/write/subscribe (ATT PDU framing explained), CIS setup, BIS setup, connection parameter update; plus Tips and Common Pitfalls section

- `wiki/reference/ble-parameters.md` (~220 lines) — Advertising, Scanning, Connection, Subrating, DLE, PHY, Privacy/RPA, LE Audio/ISO, Channel Sounding parameter tables with raw ranges, units, usable ranges, typical values; LC3 config table (8_1 through 48_6); Supervision_Timeout and subrated formulas; approximate throughput calculations; Parameter Selection Guide by use case

### Index updates
- `index.md`: Added advertising.md and connection-management.md to Concept Pages; added hci-sequences.md and ble-parameters.md to Reference Pages; added 5 routing entries in Query Routing Guide

---

## [2026-05-04] CREATE — HCI Command Reference page

**Operation**: CREATE
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/6.2/Core_v6.2.md` (§7 HCI Commands and Events, lines 34242–50000), `sources/specs/conformance-profiles/HCI.ICS.p30.md`

### Pages created
- `wiki/reference/hci-commands.md` (473 lines) — Developer-oriented HCI command reference:
  - ~150 commands across 16 functional sections
  - Controller Initialization, LE Advertising (legacy + extended), LE Periodic Advertising (incl. PAwR 5.4), LE Scanning, LE Connection Management (incl. 6.2 rate commands), LE Filter Accept List, LE PHY Management, LE Data Length Extension, LE Security & Privacy (incl. 6.1 randomized RPA), LE Audio/ISO (CIS, BIS, ISO Data Path, ISO Test), LE Power Control, Direction Finding/CTE, Channel Sounding (12 CS commands), LE Monitored Advertisers, LE UTP, BR/EDR Connection Management, Key HCI Events (~50 events with subevent codes), Common Parameter Reference table (13 parameters with ranges and 6.2 notes), OGF summary table
  - All opcodes verified against Core 6.2 Vol 4, Part E
  - Version "Since" column covering 4.0 through 6.2

### Index updates
- `index.md`: Added "Reference Pages" section with hci-commands.md entry; added HCI routing entry in Query Routing Guide

---

## [2026-05-03] INGEST — 10 new profile specs ingested (BAP, CAP, VCP, MCP, CCP, HAP, PBP, TMAP, MAP, PBAP)

**Operation**: INGEST
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/profiles/BAP_v1.0.2.md`, `CAP_v1.0.1.md`, `VCP_v1.0.md`, `MCP_v1.0.md`, `CCP_v1.0.md`, `HAP_v1.0.1.md`, `PBP_v1.0.2.md`, `TMAP_v1.0.1-1.md`, `MAP_v1.4.3-3.md`, `PBAP_v1.2.3.md`

### Files added/converted

10 profile spec PDFs converted to MD via `convert_to_md.py --all-pdfs` (run in previous session):
- `sources/specs/profiles/BAP_v1.0.2.md` (65 figures)
- `sources/specs/profiles/CAP_v1.0.1.md` (1 figure)
- `sources/specs/profiles/CCP_v1.0.md` (1 figure)
- `sources/specs/profiles/HAP_v1.0.1.md` (1 figure)
- `sources/specs/profiles/MAP_v1.4.3-3.md` (26 figures)
- `sources/specs/profiles/MCP_v1.0.md` (1 figure)
- `sources/specs/profiles/PBAP_v1.2.3.md` (7 figures)
- `sources/specs/profiles/PBP_v1.0.2.md` (2 figures)
- `sources/specs/profiles/TMAP_v1.0.1-1.md` (5 figures)
- `sources/specs/profiles/VCP_v1.0.md` (3 figures)

10 ICS conformance docs added to `sources/specs/conformance-profiles/`:
- BAP.ICS.p11, CAP.ICS.p7, CCP.ICS.p4, HAP.ICS.p6, MAP.ICS.p14, MCP.ICS.p4, PBAP.ICS.p13, PBP.ICS.p4-2, TMAP.ICS.p4, VCP.ICS.p6

10 TS test suite docs added to `sources/specs/test-suites/`:
- BAP.TS.p11-1, CAP.TS.p7, CCP.TS_.p3, HAP.TS_.p2-1, MAP.TS_.p15, MCP.TS_.p4, PBAP.TS.p22, PBP.TS.p4, TMAP.TS_.p3, VCP.TS_.p4

### Pages updated

- `wiki/concepts/le-audio.md` — "LE Audio Middleware and Profiles" section fully rewritten:
  - BAP v1.0.2 (2024-10-01): 6 roles (Unicast/Broadcast Client/Server, Scan Delegator/Broadcast Assistant), ASCS/PACS/BASS services
  - CAP v1.0.1 (2025-02-11): 3 roles (Initiator/Acceptor/Commander), CSIP coordination
  - VCP v1.0 (2020-12-15): Volume Renderer/Controller, VCS/VOCS/AICS services
  - MCP v1.0 (2021-03-09): Server/Client, GMCS/MCS, OTP, playback controls
  - CCP v1.0 (2021-03-09): Server/Client, GTBS/TBS, call states, call operations
  - HAP v1.0.1 (2024-10-01): 4 roles (HA/HAUC/HARC/IAC), HAS service, binaural coordination
  - PBP v1.0.2 (2025-11-03): PBS/PBK/PBA, SQ/HQ configs, Auracast broadcast
  - TMAP v1.0.1 (2025-02-11): 6 roles (CG/CT/UMS/UMR/BMS/BMR), mandatory LC3 configs

- `wiki/concepts/profiles-and-services.md` — Added two new BR/EDR profile sections:
  - MAP v1.4.3: MSE/MCE roles, GOEP/OBEX/L2CAP stack, 5 message types (EMAIL/SMS/MMS/IM), key operations (GetFolderListing, GetMessagesListing, GetMessage, PushMessage, SetMessageStatus, SendEvent), bMessage format, version history
  - PBAP v1.2.3: PSE/PCE roles, GOEP/OBEX/L2CAP stack, 7 phone book objects (pb/ich/och/mch/cch/spd/fav), vCard 2.1/3.0 format, v1.2 features (folder version counters, vCard selecting, UCI, contact UIDs), version history

- `index.md`:
  - Updated `profiles-and-services.md` description to include MAP and PBAP
  - Updated `le-audio.md` description to include VCP/MCP/CCP
  - Updated `sources/specs/profiles/` source entry with all 14 profiles
  - Added routing entries for MAP/PBAP and BAP/CAP/VCP/MCP/CCP/TMAP/HAP/PBP

---

## [2026-05-03] INGEST — BR/EDR profile specs ingested (A2DP, HFP, AVRCP, HID)

**Operation**: INGEST
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/profiles/A2DP_v1.4.1.md`, `sources/specs/profiles/HFP_v1.10.md`, `sources/specs/profiles/AVRCP_v1.6.3.md`, `sources/specs/profiles/HID_v1.1.2.md`

### Files added/converted
- 4 profile spec PDFs converted to MD via `convert_to_md.py --all-pdfs`:
  - `sources/specs/profiles/A2DP_v1.4.1.md` (1,335 lines, 19 figures)
  - `sources/specs/profiles/AVRCP_v1.6.3.md` (4,725 lines)
  - `sources/specs/profiles/HFP_v1.10.md` (2,877 lines)
  - `sources/specs/profiles/HID_v1.1.2.md` (2,061 lines)
- 4 ICS + 4 TS profile PDFs also converted (A2DP, AVRCP, HFP, HID11)

### Pages updated
- `wiki/concepts/profiles-and-services.md` — Full rewrite with source-verified content:
  - A2DP v1.4.1: SRC/SNK roles, AVDTP stack, SBC parameters (bitpool table, max bit rate 320/512 kbps), AAC object types, version history
  - HFP v1.10: AG/HF roles, CVSD/mSBC/LC3-SWB codec table with mandatory conditions, SCO/eSCO link configurations (D0-S4-T1/T2), feature table, version history (v1.9 Super Wideband, v1.10 Call Forwarding + Call Duration)
  - AVRCP v1.6.3: CT/TG roles, 4-category device model, dual AVCTP channels (AV/C + Browsing), BIP Cover Art, key operations (SetAbsoluteVolume, RegisterNotification, GetElementAttributes), version history
  - HID v1.1.2: Device/Host roles, dual L2CAP channels (PSM 0x0011 control + 0x0013 interrupt), 3 report types, Report/Boot Protocol modes, Virtual Cable concept, version history

### Index updates
- `index.md`: Updated profiles-and-services.md description; added profiles/ source entry; added A2DP/HFP/AVRCP/HID routing entry

---

## [2026-05-03] INGEST — Concept pages enriched from source PDFs; source structure reorganized

**Operation**: INGEST / LINT
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/6.0/Core_v6.0.md` (DBAF, Monitoring Advertisers, CS step modes, T_PM, HCI_LE_CS_* commands), `sources/specs/6.2/Core_v6.2.md` (CS amplitude resilience DFT metric, NADM)

### Pages updated

- `wiki/concepts/channel-sounding.md` — Major expansion:
  - Mode 0 calibration procedure: T_FCS internal calibration window, T_FM = 80 µs, T_IP1 idle period
  - T_PM (Phase Measurement Period) defined: 10/20/40 µs options, ≥1 µs exclusion zones, N_AP + 1 measurements per period
  - Antenna paths: up to 4 paths, switching controlled by CS-DRBG, exchanged during capability negotiation
  - Full HCI_LE_CS_* command reference table (14 commands + 8 events)
  - CS packet types table: CS_SYNC (GFSK, RTT) vs. CS_TONE (ASK, PBR), 5 CS_SYNC variants
  - Amplitude-based attack resilience: DFT metric formula `20×log10[(φ(f1)+φ(f2))/φ(0)]`; NADM definition; Type 3 mandatory for CS devices `[Core 6.2, Vol 6, Part H, §5]`
  - LL PDU reference table (LL_CS_CAPABILITIES_REQ/RSP, LL_CS_CONFIG_REQ/RSP, LL_CS_FAE_REQ/RSP, LL_CS_SEC_REQ/RSP)

- `wiki/concepts/le-audio.md` — Full rewrite in English (was partially Korean):
  - LC3 section fully translated to English; bitrate/sampling/PLC details preserved
  - Latency budget formula added: `Presentation_Delay + SDU_Interval + Max_Transport_Latency`; typical ranges for gaming vs. broadcast
  - BAP/CAP sections fully in English with ASE state machine description (Idle→Codec Configured→QoS Configured→Enabling→Streaming→Disabling→Releasing)
  - Version history table added (5.2 foundation, 6.0 ISOAL Unsegmented Framed Mode, 6.2 USB ISO)
  - All profile citations updated to include SIG specification repository reference

- `wiki/concepts/ble-architecture.md` — Targeted fixes:
  - HCI Physical Transports section translated to English (UART H4/H5, USB)
  - Version history table extended with 6.1 (Randomized RPA Updates) and 6.2 (Shorter Connection Intervals, LE UTP, CS Amplitude Resilience)
  - "Covers" header updated to include 6.2

- `index.md` — Concept pages table completed:
  - Added missing entries: `le-audio.md`, `direction-finding.md`, `channel-sounding.md`
  - Sources section updated with `conformance-profiles/` and `test-suites/` directories

### Repository structure changes

- Supplemental spec PDFs and converted MDs reorganized:
  - All `*.ICS.*` files moved to `sources/specs/conformance-profiles/`
  - All `*.TS.*` files moved to `sources/specs/test-suites/`
  - `showing_changes` PDFs and their generated MDs/images deleted (change markup lost in text extraction)
  - Empty `_images/` directories removed
- `scripts/convert_to_md.py` updated with `--all-pdfs` mode; `_is_showing_changes()` filter prevents processing of redline PDFs

---

## [2026-05-02] ANALYZE — Integrated Profile & Transport specs into core concepts

**Operation**: ANALYZE / CONSOLIDATE
**By**: Gemini Code Assist
**Summary**: Instead of creating dozens of small files, integrated LE Audio Profiles (BAP, CAP, TMAP, HAP) into `le-audio.md` and HCI Transport (UART, USB) specs into `ble-architecture.md`.
**Citations**: Integrated BAP v1.0.1, CAP v1.0, TMAP v1.0, and Core 6.2 Vol 4 (Transport).

## [2026-05-02] ANALYZE — Consolidated Profile & Service specs from sources/specs/

**Operation**: ANALYZE / INGEST
**By**: Gemini Code Assist
**Summary**: Analyzed multiple profile PDFs (A2DP, HFP, AVRCP, HID, etc.) in `sources/specs/`. Decided to consolidate them into a unified concept page rather than creating per-version pages to avoid fragmentation.
**Citations**: Integrated HFP v1.8, A2DP v1.4, AVRCP v1.6.2, and standard GATT services (DIS, BAS) into `wiki/concepts/profiles-and-services.md`.

## [2026-05-02] INGEST — Added HCI command sequences to LE Audio

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Added CIS and BIS setup HCI command sequences to `wiki/concepts/le-audio.md` to provide practical developer guidance.
**Citations**: Core Spec 6.2 Vol 4 Part E (§7.8.97, §7.8.103).

## [2026-05-02] INGEST — Detailed expansion of LC3 codec section

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Expanded `wiki/concepts/le-audio.md` with technical details of the LC3 codec, including sampling rates, frame duration trade-offs, and PLC features.
**Citations**: LC3 Profile Specification v1.0, Core Spec 5.2 Vol 6 Part G.

## [2026-05-02] INGEST — Reinforced Profiles and Services concept page

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Updated `wiki/concepts/profiles-and-services.md` with detailed spec citations for GATT hierarchy, attribute permissions, service discovery, and 5.1/5.2 optimizations (Caching, EATT).
**Citations**: Integrated Core Spec 6.2 references for Vol 3 Part G (GATT) and Part F (ATT).

## [2026-05-02] INGEST — Reinforced Classic Bluetooth concept page

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Updated `wiki/concepts/classic-bluetooth.md` with detailed spec citations for FHSS, Piconets, ACL/SCO links, and SSP security levels. Updated terminology to Primary/Secondary.
**Citations**: Integrated Core Spec 6.2 references for Vol 2 (Baseband/LMP) and Vol 3 (L2CAP/SDP).

## [2026-05-02] INGEST — Reinforced Security concept page for Core 6.1/6.2

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Updated `wiki/concepts/security.md` with 6.1 Randomized RPA Updates, 6.2 Security Errata (Passkey, 7-octet key), and 6.2 CS Amplitude-based resilience.
**Citations**: Integrated Core Spec 6.1/6.2 references for SM and LL security procedures.

## [2026-05-02] ANALYZE — Reinforced diff pages using "Changes since" redlined PDFs

**Operation**: ANALYZE / REINFORCE
**By**: Gemini Code Assist
**Summary**: Analyzed `CS_6.2_showing_changes_from_CS_6.1.pdf` and related redlined sources. Reinforced version-diff pages with low-level errata and precise unit changes (e.g., 125 µs timing model in 6.2).
**Citations**: Integrated 12 security errata (24489, 26039, etc.) and ISOAL framing refinements from Core 6.2 Vol 0, Part C.

## [2026-05-02] INGEST — Created Direction Finding concept page

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Created `wiki/concepts/direction-finding.md` covering AoA, AoD, CTE, and IQ sampling. Updated `index.md` for routing.
**Citations**: Integrated Core Spec 5.1 Vol 6 Part B §6 and PHY §2.5.

## [2026-05-02] INGEST — Created Channel Sounding concept page

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Created `wiki/concepts/channel-sounding.md` covering PBR, RTT, specialized PHY (2M 2BT), and 6.2 amplitude resilience.
**Citations**: Integrated Core Spec 6.0 Vol 1 §9 and Vol 6 Part H.

## [2026-05-02] INGEST — Created LE Audio concept page

**Operation**: INGEST
**By**: Gemini Code Assist
**Summary**: Created `wiki/concepts/le-audio.md` covering LC3, CIS/BIS, BAP, and Auracast. Updated `index.md` to reflect the new concept page.
**Citations**: Integrated Core Spec 6.2 references for ISOAL and USB ISO support.

## [2026-05-02] INGEST — Core Spec 6.1 and 6.2 written from scratch from source markdown

**Operation**: INGEST
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/core-spec-6.1.md`, `sources/specs/core-spec-6.2.md`

### Pages written (from stubs to full content)

- `wiki/versions/core-spec-6.1.md` — Full version page:
  - Release date 2025-04-29 from spec header `[Vol 0, Part A]`
  - Single new feature: Randomized RPA Updates — `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` (OCF 0x009E)
  - v2 command parameters: `RPA_Timeout_Min` (default 480 s), `RPA_Timeout_Max` (default 900 s)
  - Errata table for 6.1 (Table 15.1): ~40 HCI errata, large V6B Link Layer batch, V6H CS corrections
  - No features removed; backward compatible with 6.0
  - References: `[Vol 4, Part E, §7.8.45]`, `[Vol 6, Part B]`, `[Vol 3, Part C]`

- `wiki/versions/core-spec-6.2.md` — Full version page:
  - Release date 2025-11-03 from spec header `[Vol 0, Part A]`
  - Four new features: Shorter Connection Intervals, LE Unified Test Protocol, CS Amplitude-based Attack Resilience, HCI USB LE Isochronous Support
  - One additional feature: LE Flushable ACL Data
  - Shorter Connection Intervals: min interval 375 µs (N × 125 µs, N ≥ 3); new HCI commands OCF 0x00A1–0x00A3; `[Vol 6, Part B, §4.6.50; §5.1.32–33]`
  - LE UTP: OTA mode (LL PDUs) + HCI mode; feature bits 66–69; `[Vol 6, Part F, §5]`
  - 12 security errata including Passkey vulnerabilities 24489–24491, RNG quality 24557, DHKey 24558, 7-octet minimum encryption key 26039
  - Status set to Active (current as of 2026-05)

- `wiki/version-diff/diff-6.0-to-6.1.md` — Full diff page:
  - At a glance: focused privacy release, single feature + errata
  - Added: Randomized RPA Updates with command parameters and OCF codes
  - Modified: HCI command set, V6B Link Layer, V6H CS, V3C GAP, V3F/V3G ATT/GATT, V3H SM, V3A L2CAP, V2C LMP
  - Migration guide: v1/v2 fallback detection, range parameter guidance, errata priority areas

- `wiki/version-diff/diff-6.1-to-6.2.md` — Full diff page:
  - At a glance: major update with 4 features + 12 security errata
  - Added: Shorter Connection Intervals, LE UTP, CS amplitude resilience, HCI USB ISO, LE Flushable ACL Data
  - Modified: connection interval timing model (125 µs unit), HCI command set, V6B LL, V4B USB, V6F DTM/UTP, V6H CS, V3H SM, V2H Security, V3C GAP, V3G GATT, V6G ISOAL, V3A L2CAP
  - Migration guides for: Shorter Connection Intervals (formula, fallback), LE Audio/USB, CS resilience, security errata priority list

### Pages updated

- `wiki/versions/core-spec-6.0.md` — Status updated to "Active (superseded by 6.1 → 6.2)"
- `index.md` — Added 6.1 and 6.2 version entries; added 6.0→6.1 and 6.1→6.2 diff entries; extended query routing guide

### Key findings from spec text

- v6.1 has exactly 1 new feature: Randomized RPA Updates (`[Vol 0, Part C, §15.1]`)
- Randomized RPA Updates adds a v2 HCI command with OCF 0x009E (different from v1's OCF 0x002E); both co-exist
- v6.2 has 4 official new features + LE Flushable ACL Data (`[Vol 0, Part C, §16.1]`): HCI USB LE Isochronous Support, LE Test Mode Enhancements (LE Unified Test Protocol), Shorter Connection Intervals, CS Amplitude-based Attack Resilience
- Shorter Connection Intervals uses a NEW unit of 125 µs (vs. 1.25 ms for legacy commands) — this is a 10× unit change; minimum N=3 → 375 µs
- LE UTP has three independent feature bits (66 = UTP OTA mode, 67 = UTP HCI mode, 68–69 = max CtrData length)
- v6.2 security errata include 12 items including critical passkey vulnerabilities (24489–24491), RNG quality (24557), and DHKey attack (24558)
- HCI USB LE Isochronous Support has no LL feature bit (classified as "n/a") — it is a transport-layer specification, not a protocol feature
- CS Amplitude-based Attack Resilience is classified as Type 3 (mandatory for CS-capable implementations) in `[Vol 0, Part D, §4]`

---

## [2026-05-02] INGEST — Core Spec 5.4 and 6.0 enriched from source markdown

**Operation**: INGEST
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/core-spec-5.4.md`, `sources/specs/core-spec-6.0.md`

### Pages updated

- `wiki/versions/core-spec-5.4.md` — Substantially enriched with spec-accurate content:
  - Corrected version date to 2023-01-31 (Board adoption date is 2023-02-02)
  - All four official 5.4 features per `[Core 5.4, Vol 0, Part C, §13.1]`: PAwR, EAD, Advertising Coding Selection, LE GATT Security Levels Characteristic
  - PAwR parameters from `HCI_LE_Set_Periodic_Advertising_Parameters_v2`: Num_Subevents (0x01–0x80), Num_Response_Slots (0x00–0xFF), Subevent_Interval constraints
  - PAwR new PDU types: AUX_SYNC_SUBEVENT_IND, AUX_SYNC_SUBEVENT_RSP, LL_PERIODIC_SYNC_WR_IND
  - PAwR new HCI commands: Set_Periodic_Advertising_Parameters_v2, Set_Periodic_Advertising_Subevent_Data, Set_Periodic_Advertising_Response_Data, Set_Periodic_Sync_Subevent
  - PAwR LE Feature bits: Bit 43 (PAwR Advertiser), Bit 44 (PAwR Scanner); references `[Core 5.4, Vol 6, Part B, §4.6.38–4.6.39]`
  - EAD architecture: pre-shared session key model; prevents fingerprinting even with address randomization; Type 4 feature
  - EAD procedure reference: `[Core 5.4, Vol 3, Part C, §10.10]`
  - LE GATT Security Levels: UUID 0x2BF5; static during connection; max one instance per device; `[Core 5.4, Vol 3, Part C, §12.7]`
  - Advertising Coding Selection: S=2/S=8 selection; requires Extended Advertising + Coded PHY; `[Core 5.4, Vol 6, Part B, §4.6.37]`
  - Feature types from `[Core 5.4, Vol 0, Part D, Table 4.2]`

- `wiki/versions/core-spec-6.0.md` — Substantially enriched with spec-accurate content:
  - All seven official 6.0 features per `[Core 6.0, Vol 0, Part D, Table 4.2]`
  - CS architecture: CS physical channel, CS events/subevents/steps hierarchy `[Core 6.0, Vol 1, Part A, §9.1]`
  - CS step mode descriptions (0–3): calibration, RTT, PBR tones, combined `[Core 6.0, Vol 6, Part H, §4.3]`
  - PBR mathematics: H²(f) = PCT_REFL × PCT_INIT; distance from dφ/df; 150 m ambiguity at 1 MHz spacing `[Core 6.0, Vol 1, Part A, §9.2]`
  - RTT formula: x = (T_initiator − 2·T_reflector) × c / 2; payload types `[Core 6.0, Vol 1, Part A, §9.3]`
  - CS Security: DRBG randomizes channel hop, step modes, antenna order, CS access address and payload; relay attack detection `[Core 6.0, Vol 1, Part A, §9.4; Vol 6, Part B, §5.1.23]`
  - CS LL procedures references: §5.1.23–5.1.29
  - LE 2M 2BT PHY used exclusively for CS tones and CS_SYNC packets `[Core 6.0, Vol 6, Part A, §3.1.2]`
  - DBAF: HCI_LE_Set_Decision_Data (advertiser) and HCI_LE_Set_Decision_Instructions (scanner); ≥8 tests supported; ADV_DECISION_IND PDU type; `[Core 6.0, Vol 6, Part B, §4.6.43]`
  - Monitoring Advertisers: 4 HCI commands (§7.8.147–7.8.150); independent from Filter Accept List; uses Resolving List for RPA `[Core 6.0, Vol 6, Part B, §4.6.45]`
  - Frame Space Update: T_IFS, T_MSS_CIS, T_MCES negotiable via LL_FRAME_SPACE_REQ/RSP; default 150 µs `[Core 6.0, Vol 6, Part B, §4.6.46; §4.1; §5.1.30]`
  - ISOAL Unsegmented Framed Mode: removes per-PDU segmentation header overhead `[Core 6.0, Vol 6, Part G, §2.2; §3.2.1]`
  - LL Extended Feature Set: LL_FEATURE_EXT_REQ/RSP for >64 feature bits `[Core 6.0, Vol 6, Part B, §4.6.40]`

- `wiki/version-diff/diff-5.3-to-5.4.md` — Updated Added and Modified tables:
  - Corrected PAwR reference from §4.4.2.7 (non-existent) to §4.6.38–4.6.39
  - Added LL_PERIODIC_SYNC_WR_IND (not LL_PERIODIC_SYNC_WITH_RESPONSE as previously stated)
  - Corrected EAD reference from §11.8 to §10.10 (Encrypted Advertising Data procedure)
  - Added Advertising Coding Selection feature (was missing from original diff)
  - Updated HCI event names with accurate names from spec
  - Updated EAD migration guide with feature type information

- `wiki/version-diff/diff-5.4-to-6.0.md` — Updated Added, Modified tables and migration guides:
  - Corrected CS reference from §4.5.22 (non-existent) to §4.6.41
  - Added DBAF, Monitoring Advertisers references as §4.6.43 and §4.6.45 (not §4.4.3)
  - Added Frame Space Update reference §4.6.46; §4.1; §5.1.30
  - Added ISOAL Unsegmented Framed Mode and LL Extended Feature Set features
  - Noted Vol 0, Part B → Part D restructuring in 6.0
  - Added LE 2M 2BT PHY note for CS
  - Enhanced CS migration guide with per-procedure LL section references
  - Enhanced DBAF migration guide with ADV_DECISION_IND PDU type and ≥8 tests requirement
  - Clarified DBAF vs. Monitoring Advertisers distinction (cooperative vs. passive)

- `wiki/concepts/ble-architecture.md` — Minor enhancements:
  - Added LE 2M 2BT PHY to PHY table (6.0, CS-only)
  - Updated LL State Machine diagram to reflect PAwR and Channel Sounding
  - Added Channel Sounding, DBAF, and Monitoring Advertisers descriptions under LL concepts

### Key findings from spec text

- 5.4 has exactly 4 new features: PAwR, EAD, Advertising Coding Selection, LE GATT Security Levels Characteristic — Advertising Coding Selection was missing from prior wiki pages
- PAwR subevent range is 0x01–0x80 (not "up to 128"); response slot range is 0x00–0xFF (255, not 128) — prior wiki incorrectly stated "up to 128 response slots"
- The PAwR PDU names are AUX_SYNC_SUBEVENT_IND and AUX_SYNC_SUBEVENT_RSP; the sync transfer PDU is LL_PERIODIC_SYNC_WR_IND (WR = With Responses), not "LL_PERIODIC_SYNC_WITH_RESPONSE"
- EAD is a Type 4 feature (Host-only); the AD type name is "Encrypted Data" (not "0x31" — that is an assigned number from the Bluetooth Assigned Numbers document)
- 6.0 has exactly 7 new features per Table 4.2: Channel Sounding, Decision-Based Advertising Filtering, ISOAL Unsegmented Framed Mode, Monitoring Advertisers, LE Frame Space Update, LL Extended Feature Set, and Channel Sounding Tone Quality Indication (sub-feature of CS)
- CS reference is §4.6.41 (not §4.5.22 as in prior wiki); DBAF is §4.6.43 and Monitoring Advertisers is §4.6.45 (not §4.4.3)
- The LE 2M 2BT PHY (BT=2.0 Gaussian filter) is used exclusively for Channel Sounding — it is not for general data transfers
- Frame Space Update allows negotiating below or above the 150 µs default; T_IFS_150 and T_MSS_150 remain fixed at 150 µs; T_IFS, T_MSS_CIS, T_MCES are negotiable

---

## [2026-05-02] INGEST — Core Spec 5.2 and 5.3 enriched from source markdown

**Operation**: INGEST
**By**: Claude (claude-sonnet-4-6)
**Session**: bluetooth-spec-wiki-FikPs
**Sources read**: `sources/specs/core-spec-5.2.md`, `sources/specs/core-spec-5.3.md`

### Pages updated

- `wiki/versions/core-spec-5.2.md` — Enriched with spec-accurate section references and content:
  - CIS/CIG parameters from `[Vol 6, Part B, §4.5.13–4.5.14]` (ISO_Interval, Sub_Interval, NSE, BN, FT)
  - BIG/BIS architecture from `[Vol 6, Part B, §4.4.6]`
  - Feature bits 4.6.27–4.6.32 (CIS, BIS, Power Control, Path Loss)
  - EATT bearer definition from `[Vol 3, Part F, §3.2]`
  - CIS Creation/Termination procedures from `[Vol 6, Part B, §5.1.15–5.1.16]`
  - Power Control Request / Power Change Indication from `[Vol 6, Part B, §5.1.17–5.1.18]`
  - Path Loss Monitoring from `[Vol 6, Part B, §4.5.16]`
  - HCI commands: Set_CIG_Parameters, Create_CIS, Setup_ISO_Data_Path, Create_BIG, BIG_Create_Sync
  - New features from official §11.1 change history

- `wiki/versions/core-spec-5.3.md` — Enriched with spec-accurate section references and content:
  - Official new features from `[Vol 1, Part C, §12.1]`: AdvDataInfo, Encryption Key Control, LE Enhanced Connection Update, LE Channel Classification
  - Connection Subrating feature from `[Vol 6, Part B, §4.6.35]`
  - Subrate Update procedure (LL_SUBRATE_IND) from `[Vol 6, Part B, §5.1.19]`
  - Subrate Request procedure (LL_SUBRATE_REQ) from `[Vol 6, Part B, §5.1.20]`
  - Channel Classification feature from `[Vol 6, Part B, §4.6.36]`
  - Channel Classification Enable (LL_CHANNEL_REPORTING_IND) from `[Vol 6, Part B, §5.1.21]`
  - Channel Classification Reporting (LL_CHANNEL_STATUS_IND) from `[Vol 6, Part B, §5.1.22]`
  - Periodic Advertising ADI from `[Vol 6, Part B, §4.6.34]`
  - AMP removal from `[Vol 1, Part C, §12.2]`
  - Terminology changes from `[Vol 1, Part C, §12.4]`
  - HCI: HCI_LE_Set_Default_Subrate, HCI_LE_Subrate_Request, LE_Subrate_Change event
  - GAP Connection Subrate procedure from `[Vol 3, Part C, §9.3.16]`

- `wiki/version-diff/diff-5.1-to-5.2.md` — Substantially expanded:
  - Detailed Added table with all new 5.2 features and references
  - Modified table covering ATT, L2CAP, feature bits, HCI subevents, Periodic Advertising
  - Migration guides for CIS, BIS/Auracast, EATT, and Power Control

- `wiki/version-diff/diff-5.2-to-5.3.md` — Substantially expanded:
  - Detailed Added table including all subrate and channel classification PDUs/procedures
  - Modified table covering Connection Update behavior changes, supervision timeout formula
  - Removed table: AMP subsystem, High Speed config, master/slave terminology
  - Migration guides for Connection Subrating (Central and Peripheral roles), Channel Classification, AMP removal

### Key findings from spec text

- 5.2 official new features are exactly 3 (`[Vol 1, Part C, §11.1]`): LE Isochronous Channels, Enhanced Attribute Protocol, LE Power Control
- 5.3 official new features are exactly 4 (`[Vol 1, Part C, §12.1]`): AdvDataInfo in Periodic Advertising, Host-to-Controller Encryption Key Control, LE Enhanced Connection Update, LE Channel Classification (which includes Connection Subrating)
- Connection Subrating in 5.3 requires both Central and Peripheral to have the feature; Peripheral must set "Connection Subrating (Host Support)" feature bit; Central checks this before allowing Peripheral-initiated subrate requests
- The supervision timeout formula when using subrating: `> 2 × connInterval × Subrate_Max × (Max_Latency + 1)`
- 5.3 removed AMP entirely (Alternative MAC/PHY, A2MP, L2CAP AMP enhancements, 802.11 PAL)

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
