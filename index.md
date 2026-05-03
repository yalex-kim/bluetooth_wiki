# Bluetooth Spec Wiki — Content Index

> **LLM Instruction**: Read this file first on every query to identify which pages to load.
> Pages are organized by category. Each entry includes a one-line summary.

---

## Core Specification Versions

| Page | Version | Release | Summary |
|------|---------|---------|---------|
| [core-spec-5.0](wiki/versions/core-spec-5.0.md) | 5.0 | 2016-12 | 2× speed (2 Mbps), 4× range (LE Coded PHY), 8× broadcast capacity, mesh networking |
| [core-spec-5.1](wiki/versions/core-spec-5.1.md) | 5.1 | 2019-01 | Direction Finding via AoA/AoD, GATT caching, ADI field for advertising |
| [core-spec-5.2](wiki/versions/core-spec-5.2.md) | 5.2 | 2019-12 | LE Audio framework, LC3 codec, Isochronous Channels (CIS/BIS), EATT, LE Power Control |
| [core-spec-5.3](wiki/versions/core-spec-5.3.md) | 5.3 | 2021-07 | Connection Subrating, Enhanced Connection Update, Advertising Coding Selection |
| [core-spec-5.4](wiki/versions/core-spec-5.4.md) | 5.4 | 2023-02 | Periodic Advertising with Responses (PAwR), Encrypted Advertising Data (EAD) |
| [core-spec-6.0](wiki/versions/core-spec-6.0.md) | 6.0 | 2024-08 | Channel Sounding (CS) for precise ranging, Decision-Based Advertising Filtering |
| [core-spec-6.1](wiki/versions/core-spec-6.1.md) | 6.1 | 2025-04 | Randomized RPA Updates (v2 HCI command for randomized RPA rotation intervals) |
| [core-spec-6.2](wiki/versions/core-spec-6.2.md) | 6.2 | 2025-11 | Shorter Connection Intervals (375 µs min), LE UTP test mode, CS security hardening, 12 security errata |

---

## Version Difference Index

> Use these pages when asked "what changed between version X and Y?"

| Page | Versions | Key Changes |
|------|---------|-------------|
| [diff-5.0-to-5.1](wiki/version-diff/diff-5.0-to-5.1.md) | 5.0 → 5.1 | Direction Finding, GATT caching |
| [diff-5.1-to-5.2](wiki/version-diff/diff-5.1-to-5.2.md) | 5.1 → 5.2 | LE Audio, Isochronous Channels, EATT |
| [diff-5.2-to-5.3](wiki/version-diff/diff-5.2-to-5.3.md) | 5.2 → 5.3 | Connection Subrating, Advertising Coding |
| [diff-5.3-to-5.4](wiki/version-diff/diff-5.3-to-5.4.md) | 5.3 → 5.4 | PAwR, EAD, Adv Coding Selection (Verified via Redlines) |
| [diff-5.4-to-6.0](wiki/version-diff/diff-5.4-to-6.0.md) | 5.4 → 6.0 | Channel Sounding, DBAF, Frame Space, ISOAL Updates |
| [diff-6.0-to-6.1](wiki/version-diff/diff-6.0-to-6.1.md) | 6.0 → 6.1 | Randomized RPA Updates, Errata Batch 6.1 |
| [diff-6.1-to-6.2](wiki/version-diff/diff-6.1-to-6.2.md) | 6.1 → 6.2 | Shorter Connection Intervals (125µs units), 12 Security Errata, CS Resilience |

---

## Concept Pages

| Page | Summary |
|------|---------|
| [overview](wiki/overview.md) | Bluetooth technology overview: BR/EDR vs. LE, architecture, use cases |
| [ble-architecture](wiki/concepts/ble-architecture.md) | BLE protocol stack: PHY, LL, HCI, L2CAP, ATT, GATT, GAP, SM |
| [classic-bluetooth](wiki/concepts/classic-bluetooth.md) | BR/EDR: piconets, scatternets, profiles, audio (SCO/eSCO) |
| [security](wiki/concepts/security.md) | Pairing, bonding, LE Secure Connections, privacy, encrypted advertising |
| [profiles-and-services](wiki/concepts/profiles-and-services.md) | BR/EDR profiles (A2DP v1.4.1, HFP v1.10, AVRCP v1.6.3, HID v1.1.2, MAP v1.4.3, PBAP v1.2.3) with full source citations; GATT services and LE Audio profile overview |
| [le-audio](wiki/concepts/le-audio.md) | LC3 codec, Isochronous Channels (CIS/BIS), BAP/CAP/VCP/MCP/CCP/TMAP/HAP/PBP profiles, Auracast |
| [direction-finding](wiki/concepts/direction-finding.md) | AoA/AoD, CTE (Constant Tone Extension), IQ sampling, antenna arrays (5.1+) |
| [channel-sounding](wiki/concepts/channel-sounding.md) | PBR/RTT ranging, CS step modes 0–3, T_PM, HCI commands, relay attack resilience (6.0+) |

---

## Sources

| File | Description |
|------|-------------|
| [sources/README.md](sources/README.md) | How to download and convert Bluetooth spec PDFs |
| sources/specs/X.Y/ | Core Spec PDFs + PyMuPDF-converted markdown + extracted figure images |
| sources/specs/conformance-profiles/ | ICS (Implementation Conformance Statement) docs for all protocols (A2DP, AVRCP, GAP, GATT, HCI, HFP, HID, LL, SM, etc.) |
| sources/specs/test-suites/ | TS (Test Suite) docs + figure images for all protocols |
| sources/specs/profiles/ | Profile specification MDs: A2DP v1.4.1, AVRCP v1.6.3, HFP v1.10, HID v1.1.2, MAP v1.4.3, PBAP v1.2.3, BAP v1.0.2, CAP v1.0.1, VCP v1.0, MCP v1.0, CCP v1.0, HAP v1.0.1, PBP v1.0.2, TMAP v1.0.1 |

---

## Maintenance

| File | Description |
|------|-------------|
| [CLAUDE.md](CLAUDE.md) | Wiki schema and LLM maintainer instructions |
| [log.md](log.md) | Append-only activity log |

---

## Query Routing Guide

| If asked about... | Read these pages |
|------------------|-----------------|
| A specific version's features | `wiki/versions/core-spec-X.Y.md` |
| What changed between versions | `wiki/version-diff/diff-X.W-to-X.Y.md` |
| A specific protocol concept | `wiki/concepts/<concept>.md` |
| LE Audio / LC3 / Isochronous | `le-audio.md`, `core-spec-5.2.md`, `ble-architecture.md` |
| Direction Finding / AoA / AoD | `direction-finding.md`, `core-spec-5.1.md`, `diff-5.0-to-5.1.md` |
| Channel Sounding / ranging | `channel-sounding.md`, `core-spec-6.0.md`, `diff-5.4-to-6.0.md`, `diff-6.1-to-6.2.md` |
| Encrypted Advertising / EAD | `core-spec-5.4.md`, `security.md` |
| Short / ultra-low-latency BLE connections | `core-spec-6.2.md`, `diff-6.1-to-6.2.md` |
| RPA / BLE privacy / address rotation | `core-spec-6.1.md`, `diff-6.0-to-6.1.md`, `security.md` |
| LE Audio / isochronous / USB transport | `core-spec-5.2.md`, `core-spec-6.2.md` |
| PAwR / broadcast updates | `core-spec-5.4.md`, `diff-5.3-to-5.4.md` |
| Security / pairing / bonding | `wiki/concepts/security.md` |
| GATT / ATT / services | `wiki/concepts/profiles-and-services.md` |
| A2DP / HFP / AVRCP / HID profiles | `wiki/concepts/profiles-and-services.md` |
| MAP / message access / car messaging | `wiki/concepts/profiles-and-services.md` |
| PBAP / phone book access / contacts | `wiki/concepts/profiles-and-services.md` |
| BAP / CAP / TMAP / HAP / PBP (LE Audio) | `wiki/concepts/le-audio.md` |
| VCP / MCP / CCP (audio control, LE) | `wiki/concepts/le-audio.md` |
| BLE vs Classic Bluetooth | `wiki/overview.md`, `wiki/concepts/classic-bluetooth.md` |
