# Bluetooth Core Specification 6.0

**Release Date**: 2024-08-27
**Status**: Active (superseded by 6.1 → 6.2)
**Spec Volume**: ~4114 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-6-0/) | [Local PDF](../../sources/specs/core-spec-6.0.pdf) | [Local Markdown](../../sources/specs/core-spec-6.0.md)

---

## Executive Summary

Bluetooth 6.0 introduced seven new features: **LE Channel Sounding**, **Decision-Based
Advertising Filtering**, **ISOAL Unsegmented Framed Mode**, **Monitoring Advertisers**,
**LE Frame Space Update**, **LL Extended Feature Set**, and **Channel Sounding Tone
Quality Indication**. [Core 6.0, Vol 1, Part C, §14.1; Vol 0, Part D, Table 4.2]

**LE Channel Sounding (CS)** is a new physical-layer technique for precise distance
measurement using Phase-Based Ranging (PBR) and Round-Trip Time (RTT). It achieves
centimeter-level ranging accuracy, enabling digital car keys, precise asset location, access
control, and anti-relay attack protection. CS is defined across Vol 1 (architecture), Vol 6 Part B
(Link Layer), Vol 6 Part A (PHY requirements), and Vol 6 Part H (CS physical layer).

**Decision-Based Advertising Filtering (DBAF)** gives the controller intelligence to evaluate
advertising PDUs against programmable decision instructions without waking the host,
dramatically reducing power consumption in scanner applications.

**Monitoring Advertisers** enables the controller to track the appearance and disappearance
of specific advertisers without continuous host involvement.

6.0 also updated Frame Space parameters (allowing sub-150 µs inter-frame spacing for
tighter scheduling) and improved the ISO Adaptation Layer (ISOAL) with unsegmented framed
mode support for LE Audio streams.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| LE Channel Sounding (CS) | Phase-based ranging (PBR) and RTT for centimeter accuracy distance measurement | [Core 6.0, Vol 6, Part B, §4.6.41; Vol 6, Part H] |
| CS Tone Quality Indication | Optional sub-feature: per-tone quality measurement during T_PM phase | [Core 6.0, Vol 6, Part B, §4.6.42; Vol 6, Part H, §4.6] |
| CS Step Types (mode-0 through mode-3) | Mode-0: calibration; Mode-1: RTT; Mode-2: PBR tones; Mode-3: RTT+PBR | [Core 6.0, Vol 1, Part A, §9.1; Vol 6, Part H, §4.3] |
| CS Security | DRBG-based cryptographic randomization; anti-relay via CS random value exchange | [Core 6.0, Vol 1, Part A, §9.4; Vol 6, Part B, §5.1.23] |
| Decision-Based Advertising Filtering (DBAF) | Programmable controller-side decision instructions for advertising PDU filtering | [Core 6.0, Vol 6, Part B, §4.6.43](../../sources/specs/6.0/Core_v6.0.md#L62448) |
| Monitoring Advertisers | Controller tracks appearance/disappearance of specific advertisers | [Core 6.0, Vol 6, Part B, §4.6.45](../../sources/specs/6.0/Core_v6.0.md#L62466) |
| LE Frame Space Update | Negotiate sub-150 µs inter-frame spacing (T_IFS, T_MSS_CIS, T_MCES) per connection | [Core 6.0, Vol 6, Part B, §4.6.46; §4.1; §5.1.30] |
| ISOAL Unsegmented Framed Mode | Unsegmented mode for framed ISO PDUs; improves LE Audio stream efficiency | [Core 6.0, Vol 6, Part B, §4.6.44; Vol 6, Part G, §2.2, §3.2.1] |
| LL Extended Feature Set | Extended feature page exchange using LL_FEATURE_EXT_REQ/RSP for >64 feature bits | [Core 6.0, Vol 6, Part B, §4.6.40](../../sources/specs/6.0/Core_v6.0.md#L62401) |

---

## Key Changes to Existing Mechanisms

### LE Channel Sounding (CS)

Channel Sounding is a **new physical layer measurement procedure** built on a dedicated
LE Channel Sounding physical link and CS generic packet structure.
[Core 6.0, Vol 1, Part A, §3.2.3; §3.4.3; §3.3.2]

**Architecture**: A CS procedure is divided into CS events, each containing CS subevents,
which contain CS steps. CS events are anchored from a common LE connection event.
[Core 6.0, Vol 1, Part A, §9.1](../../sources/specs/6.0/Core_v6.0.md#L6167)

**Four CS step modes** [Core 6.0, Vol 1, Part A, §9.1; Vol 6, Part H, §4.3]:
- **Mode-0**: Calibration — synchronizes frequency and timing between initiator and reflector
- **Mode-1**: RTT exchange — measures round-trip time using CS_SYNC packets (32-bit pseudo-noise access address, optional 96-bit sounding sequence or 128-bit random sequence payload)
- **Mode-2**: Phase-Based Ranging — exchanges tones; measures IQ (in-phase and quadrature) samples across channels
- **Mode-3**: Combined RTT + PBR in the same step

**Phase-Based Ranging (PBR) mathematics** [Core 6.0, Vol 1, Part A, §9.2](../../sources/specs/6.0/Core_v6.0.md#L6182):
- Both devices transmit tones; receiver measures phase/amplitude (IQ values)
- Channel transfer function estimated as H²(f) = PCT_REFL(f) × PCT_INIT(f)
- Distance x derived from: x = −(dφ/df) × c / (4π)
- 1 MHz channel spacing gives 150 m distance ambiguity; RTT disambiguates larger distances

**Round-Trip Time (RTT) measurement** [Core 6.0, Vol 1, Part A, §9.3](../../sources/specs/6.0/Core_v6.0.md#L6215):
- Initiator and reflector exchange CS_SYNC packets; both record ToD and ToA
- Distance: x = (T_initiator − 2·T_reflector) × c / 2
- Accuracy depends on RTT payload type (access address only vs. sounding/random sequence)

**CS Security** [Core 6.0, Vol 1, Part A, §9.4; Vol 6, Part B, §5.1.23]:
- A DRBG (Deterministic Random Bit Generator) randomizes: channel hop selection, step modes,
  tone modulation, antenna transmission order, CS Access Address and payload content
- DRBG key material is exchanged under an encrypted link and never externally shared
- CS step mode-1 and mode-3 allow detection of relay attacks via RTT verification
- CS step mode-3 provides two partially independent distance estimates (RTT + PBR) simultaneously

**LL control procedures for CS** [Core 6.0, Vol 6, Part B, §5.1.23–5.1.29]:
- Security Start procedure (§5.1.23)
- Capabilities Exchange procedure (§5.1.24)
- Configuration procedure (§5.1.25)
- CS Start procedure (§5.1.26)
- Procedure Repeat Termination (§5.1.27)
- Channel Map Update (§5.1.28)
- Mode-0 FAE Table Request (§5.1.29)

**New LE Feature bits** [Core 6.0, Vol 6, Part B]:
- Bit: Channel Sounding (feature bit 4.6.41)
- Bit: Channel Sounding Tone Quality Indication (feature bit 4.6.42)

**New HCI commands** [Core 6.0, Vol 4, Part E]:
- `HCI_LE_CS_Read_Remote_Supported_Capabilities`
- `HCI_LE_CS_Create_Config`
- `HCI_LE_CS_Procedure_Enable`
- `HCI_LE_CS_Security_Enable`
- Results reported via `LE_CS_Subevent_Result` HCI events

**PHY**: CS uses a dedicated LE Channel Sounding physical channel. The LE 2M 2BT PHY
(uncoded at 2 Mb/s with BT=2.0) is used exclusively for Channel Sounding.
[Core 6.0, Vol 6, Part A, §3.1.2; Vol 1, Part A, §3.3.2]

### Decision-Based Advertising Filtering (DBAF)

**Before 6.0**: The host specified address-based filter policies. The controller sent all
matching advertising reports to the host, which then discarded unwanted reports.

**With DBAF**: The host programs decision instructions into the controller via
`HCI_LE_Set_Decision_Instructions`. Advertisers include decision data in `ADV_DECISION_IND`
PDUs via `HCI_LE_Set_Decision_Data`. [Core 6.0, Vol 6, Part B, §4.6.43](../../sources/specs/6.0/Core_v6.0.md#L62448)

The controller must support at least 8 tests in the decision instructions.
[Core 6.0, Vol 4, Part E — HCI_LE_Set_Decision_Instructions]

Default behavior on reset: "No decisions" mode — the Link Layer ignores decision PDUs.
[Core 6.0, Vol 6, Part B — Decision PDU scanning]

**Extends scanning and initiating**: DBAF filter policies are applied via bits 2–3 of
`Scanning_Filter_Policy` and the `Initiator_Filter_Policy` parameter. Controllers that do
not support DBAF return an error if these bits are set non-zero.

**Feature type**: Type 3 (requires both Controller and Host). [Core 6.0, Vol 0, Part D, Table 4.2]

### Monitoring Advertisers

A new feature that enables the controller to track when specific advertisers appear or
disappear, without requiring continuous host scanning. [Core 6.0, Vol 6, Part B, §4.6.45](../../sources/specs/6.0/Core_v6.0.md#L62466)

New HCI commands [Core 6.0, Vol 4, Part E]:
- `HCI_LE_Add_Device_To_Monitored_Advertisers_List` (section 7.8.147)
- `HCI_LE_Clear_Monitored_Advertisers_List` (section 7.8.148)
- `HCI_LE_Enable_Monitoring_Advertisers` (section 7.8.149)
- `HCI_LE_Read_Monitored_Advertisers_List_Size` (section 7.8.150)

The Monitoring Advertisers feature operates independently from the Filter Accept List.
It is possible to monitor devices that are not in the Filter Accept List even when that
list is enabled. The Resolving List is used to resolve Resolvable Private Addresses for
monitored advertisers. [Core 6.0, Vol 6, Part B — Monitoring Advertisers section]

**Feature type**: Type 3 (requires both Controller and Host). [Core 6.0, Vol 0, Part D, Table 4.2]

### LE Frame Space Update

**Before 6.0**: All inter-frame spacing (T_IFS) values were fixed at 150 µs.

**With 6.0**: The Frame Space Update feature allows devices to negotiate a different
frame space value for a specific connection, enabling sub-150 µs or super-150 µs
inter-frame spacing for the following timing parameters:
[Core 6.0, Vol 6, Part B, §4.1; §5.1.30]

- `T_IFS` — Inter Frame Space (default 150 µs; can be negotiated below or above)
- `T_MSS_CIS` — Minimum CIS Subevent Space (default 150 µs)
- `T_MCES` — Minimum Connection Event Spacing (default 150 µs)

A Controller supports this feature by supporting either a minimum frame space ≤ 145 µs
or a maximum frame space ≥ 155 µs (or both). [Core 6.0, Vol 6, Part B, §4.6.46](../../sources/specs/6.0/Core_v6.0.md#L62471)

New LL PDUs: `LL_FRAME_SPACE_REQ` and `LL_FRAME_SPACE_RSP`
New HCI command: `HCI_LE_Frame_Space_Update` (section 7.8.151)
[Core 6.0, Vol 4, Part E]

**Feature type**: Type 2 (Controller feature configurable by Host). [Core 6.0, Vol 0, Part D, Table 4.2]

### ISOAL Unsegmented Framed Mode

Adds an unsegmented mode for framed ISO PDUs to the Isochronous Adaptation Layer.
[Core 6.0, Vol 6, Part G, §2.2; §3.2.1]

Improves efficiency for LE Audio streams by removing the per-PDU segmentation header
overhead when a single SDU fits in one PDU without segmentation. Affects all four ISO
logical transport types (CIS Central, CIS Peripheral, BIG Broadcaster, Synchronized Receiver).
[Core 6.0, Vol 6, Part B, §4.6.44](../../sources/specs/6.0/Core_v6.0.md#L62455)

**Feature type**: Type 2 (Controller feature). [Core 6.0, Vol 0, Part D, Table 4.2]

---

## Deprecated / Removed

- None — 6.0 is backward compatible; CS and DBAF are optional features

---

## Developer Impact

**High impact areas:**
- **Digital car keys / access control**: Channel Sounding enables "precise presence" detection
  (is the key fob in the car? at the door?). Complements PACS profile.
- **Anti-relay attack protection**: CS makes relay attacks detectable by measuring actual distance.
  Critical for NFC/BLE car key security.
- **Asset tracking with precision**: Upgrade from RSSI-based proximity to CS-based ranging for
  sub-meter accuracy without UWB hardware costs.
- **Scanner power optimization**: DBAF and Monitoring Advertisers for any application that
  scans for specific devices in a noisy environment (retail scanner, smartphone background scanning).

**Hardware requirements:**
- Channel Sounding requires specific RF hardware support (tone generation, phase measurement)
- Check `LE Features` bitmask for `LE Channel Sounding` bit
- Not all 6.0 controllers will implement CS — it's an optional feature

---

## Cross-References

- Diff from 5.4: [diff-5.4-to-6.0](../version-diff/diff-5.4-to-6.0.md)
- Diff to 6.1: [diff-6.0-to-6.1](../version-diff/diff-6.0-to-6.1.md)
- Related concepts: [Security](../concepts/security.md), [BLE Architecture](../concepts/ble-architecture.md)
