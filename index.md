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
| [diff-5.3-to-5.4](wiki/version-diff/diff-5.3-to-5.4.md) | 5.3 → 5.4 | PAwR, Encrypted Advertising Data |
| [diff-5.4-to-6.0](wiki/version-diff/diff-5.4-to-6.0.md) | 5.4 → 6.0 | Channel Sounding, DBAF, Frame Space |
| [diff-6.0-to-6.1](wiki/version-diff/diff-6.0-to-6.1.md) | 6.0 → 6.1 | Randomized RPA Updates, errata batch |
| [diff-6.1-to-6.2](wiki/version-diff/diff-6.1-to-6.2.md) | 6.1 → 6.2 | Shorter Connection Intervals, LE UTP, CS amplitude resilience, security errata |

---

## Concept Pages

| Page | Summary |
|------|---------|
| [overview](wiki/overview.md) | Bluetooth technology overview: BR/EDR vs. LE, architecture, use cases |
| [ble-architecture](wiki/concepts/ble-architecture.md) | BLE protocol stack: PHY, LL, HCI, L2CAP, ATT, GATT, GAP, SM |
| [classic-bluetooth](wiki/concepts/classic-bluetooth.md) | BR/EDR: piconets, scatternets, profiles, audio (SCO/eSCO) |
| [security](wiki/concepts/security.md) | Pairing, bonding, LE Secure Connections, privacy, encrypted advertising |
| [profiles-and-services](wiki/concepts/profiles-and-services.md) | GATT profiles, common profiles (HID, HRS, BAS, etc.), service discovery |

---

## Sources

| File | Description |
|------|-------------|
| [sources/README.md](sources/README.md) | How to download and convert Bluetooth spec PDFs |
| sources/specs/ | Raw PDF files and OpenDataLoader-converted markdown |

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
| LE Audio / LC3 / Isochronous | `core-spec-5.2.md`, `ble-architecture.md` |
| Direction Finding / AoA / AoD | `core-spec-5.1.md`, `diff-5.0-to-5.1.md` |
| Channel Sounding / ranging | `core-spec-6.0.md`, `diff-5.4-to-6.0.md`, `diff-6.1-to-6.2.md` (CS amplitude resilience) |
| Encrypted Advertising / EAD | `core-spec-5.4.md`, `security.md` |
| Short / ultra-low-latency BLE connections | `core-spec-6.2.md`, `diff-6.1-to-6.2.md` |
| RPA / BLE privacy / address rotation | `core-spec-6.1.md`, `diff-6.0-to-6.1.md`, `security.md` |
| LE Audio / isochronous / USB transport | `core-spec-5.2.md`, `core-spec-6.2.md` |
| PAwR / broadcast updates | `core-spec-5.4.md`, `diff-5.3-to-5.4.md` |
| Security / pairing / bonding | `wiki/concepts/security.md` |
| GATT / ATT / services | `wiki/concepts/profiles-and-services.md` |
| BLE vs Classic Bluetooth | `wiki/overview.md`, `wiki/concepts/classic-bluetooth.md` |
