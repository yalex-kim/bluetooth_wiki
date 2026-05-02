# Bluetooth Spec Wiki — Activity Log

> This is an **append-only** log. Never delete entries. Add new entries at the top.
> Format: `## [YYYY-MM-DD] [Operation] — [Summary]`

---

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
