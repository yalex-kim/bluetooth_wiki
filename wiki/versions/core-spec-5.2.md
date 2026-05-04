# Bluetooth Core Specification 5.2

**Release Date**: 2019-12-31
**Status**: Superseded by 5.3
**Spec Volume**: ~3544 pages
**Source**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-2/) | [Local Markdown](../../sources/specs/5.2/Core_v5.2.md)

---

## Executive Summary

Bluetooth 5.2 delivered the **LE Audio** framework — the most transformative update to Bluetooth
audio since A2DP. LE Audio replaces the BR/EDR-based audio stack (SCO/eSCO + SBC) with a
fully LE-based isochronous audio system, introducing the **LC3 (Low Complexity Communication Codec)**
for superior audio quality at lower bitrates.

The foundation of LE Audio is **LE Isochronous Channels** (`[Core 5.2, Vol 1, Part C, §11.1]`):
**CIS** (Connected Isochronous Streams) for one-to-one audio (e.g., earbuds) and **BIS** (Broadcast
Isochronous Streams) for one-to-many audio (e.g., TV audio broadcast to hearing aids). These are
specified in `[Core 5.2, Vol 6, Part B, §4.5.13–4.5.14]` (CIS/CIG) and `[Core 5.2, Vol 6, Part B, §4.4.6](../../sources/specs/5.2/Core_v5.2.md#L61723)`
(Isochronous Broadcasting State / BIG).

Additionally, 5.2 introduced **Enhanced ATT (EATT)** for parallel GATT transactions
(`[Core 5.2, Vol 3, Part F, §3.2]`) and **LE Power Control** for dynamic TX power optimization
(`[Core 5.2, Vol 6, Part B, §5.1.17–5.1.18]`). These three pillars — LE Isochronous Channels,
Enhanced ATT, and LE Power Control — are the official new features listed in
`[Core 5.2, Vol 1, Part C, §11.1]`.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| LE Isochronous Channels | New LL channel type with time-bounded delivery guarantees | Vol 1, Part C, §11.1; Vol 6, Part B, §4.4.6 & §4.5.13 |
| CIS (Connected Isochronous Stream) | Isochronous audio within a connection (point-to-point, bidirectional) | Vol 6, Part B, §4.5.13 |
| CIG (Connected Isochronous Group) | Groups multiple CIS streams for synchronized playback | Vol 6, Part B, §4.5.14 |
| BIS (Broadcast Isochronous Stream) | Isochronous audio broadcast (point-to-multipoint) | Vol 6, Part B, §4.4.6 |
| BIG (Broadcast Isochronous Group) | Groups BIS streams (e.g., left + right channel) | Vol 6, Part B, §4.4.6 |
| LE Isochronous Adaptation Layer (ISOAL) | Framing/segmentation of codec frames over ISO channels | Vol 6, Part G |
| CIS Creation procedure | LL_CIS_REQ / LL_CIS_RSP / LL_CIS_IND PDU exchange | Vol 6, Part B, §5.1.15 |
| CIS Termination procedure | LL_CIS_TERMINATE_IND PDU | Vol 6, Part B, §5.1.16 |
| Enhanced ATT (EATT) | Multiple parallel ATT bearers via L2CAP Enhanced Credit Based Flow Control | Vol 3, Part F, §3.2 |
| LE Power Control Request | Device requests peer to adjust TX power; LL_POWER_CONTROL_REQ/RSP | Vol 6, Part B, §4.6.31; §5.1.17 |
| LE Power Change Indication | Unsolicited notification of TX power change; LL_POWER_CHANGE_IND | Vol 6, Part B, §4.6.30; §5.1.18 |
| LE Path Loss Monitoring | RSSI-based zone tracking; host notified on zone change | Vol 6, Part B, §4.6.32; §4.5.16 |
| HCI ISO Commands/Events | Full HCI surface for CIG/CIS/BIG/BIS create, modify, destroy, data path | Vol 4, Part E |

---

## Key Changes to Existing Mechanisms

### Isochronous Channels Architecture

ISO channels guarantee **time-bounded delivery** by using a fixed isochronous schedule.
Unlike ACL connections (best-effort), ISO channels define:
- **ISO_Interval**: Period between isochronous events (5 ms to 4 s, multiples of 1.25 ms)
- **Sub_Interval**: Time between consecutive subevents within an event
- **NSE** (Number of Subevents): Up to 31 subevents per event for retransmission
- **BN** (Burst Number): Number of new payloads per event
- **FT** (Flush Timeout): How many events an SDU can wait before being flushed
- **Framing**: Framed (variable-length SDUs) or unframed (fixed-length)

`[Core 5.2, Vol 6, Part B, §4.5.13](../../sources/specs/5.2/Core_v5.2.md#L62259)`

**CIS** (Connected Isochronous Stream):
- Lives within an existing ACL connection `[Core 5.2, Vol 6, Part B, §4.5.13](../../sources/specs/5.2/Core_v5.2.md#L62259)`
- Supports bidirectional audio (BN may be non-zero in both directions)
- Creation uses `LL_CIS_REQ → LL_CIS_RSP → LL_CIS_IND` `[Core 5.2, Vol 6, Part B, §5.1.15](../../sources/specs/5.2/Core_v5.2.md#L63167)`
- Termination uses `LL_CIS_TERMINATE_IND` `[Core 5.2, Vol 6, Part B, §5.1.16](../../sources/specs/5.2/Core_v5.2.md#L63179)`
- A **CIG** groups multiple CIS streams for synchronized playback (e.g., left + right earbuds); maximum 31 CIS per CIG `[Core 5.2, Vol 6, Part B, §4.5.14](../../sources/specs/5.2/Core_v5.2.md#L62359)`
- CIS encryption follows the associated ACL's encryption status `[Core 5.2, Vol 6, Part B, §4.5.13](../../sources/specs/5.2/Core_v5.2.md#L62259)`

**BIS** (Broadcast Isochronous Stream):
- No ACL connection needed; operates in the **Isochronous Broadcasting State** `[Core 5.2, Vol 6, Part B, §4.4.6](../../sources/specs/5.2/Core_v5.2.md#L61723)`
- Unlimited receivers (Synchronized Receiver feature `[Core 5.2, Vol 6, Part B, §4.6.29](../../sources/specs/5.2/Core_v5.2.md#L62709)`)
- A **BIG** groups multiple BIS streams; BIG discovery uses Periodic Advertising as the sync mechanism
- BIGInfo advertising data carries BIG timing parameters for receivers to sync
- BIG Control procedures (`LL_BIG_CONTROL_PDU`) handle channel map updates and termination `[Core 5.2, Vol 6, Part B, §5.6](../../sources/specs/5.2/Core_v5.2.md#L63272)`
- Optional BIG encryption with a Broadcast Code

**Feature bits for ISO** `[Core 5.2, Vol 6, Part B, §4.6.27–4.6.29]`:
- Bit 4.6.27: Connected Isochronous Stream - Master / Slave
- Bit 4.6.28: Isochronous Broadcaster
- Bit 4.6.29: Synchronized Receiver
- Host sets "Isochronous Channels (Host Support)" via `HCI_LE_Set_Host_Feature`

### Enhanced ATT (EATT)

Classic ATT (pre-5.2) uses a single fixed L2CAP channel: only one transaction at a time per device pair.
EATT creates multiple **Enhanced ATT Bearers** over L2CAP Enhanced Credit Based Flow Control
channels `[Core 5.2, Vol 3, Part F, §3.2]`:
- An ATT bearer using Enhanced Credit Based Flow Control Mode is an **Enhanced ATT bearer**
- Enhanced ATT bearers provide reliable notification delivery (classic ATT bearers may discard notifications on buffer overflow; EATT bearers shall not)
- Multiple bearers allow concurrent read/write/notification transactions
- Negotiated via L2CAP Enhanced Credit Based Connection (PSM negotiated via GATT)
- EATT L2CAP interoperability requirements defined in `[Core 5.2, Vol 3, Part F, §5.3]`

### LE Power Control

Devices can request each other to adjust TX power to maintain optimal link quality
`[Core 5.2, Vol 6, Part B, §5.1.17](../../sources/specs/5.2/Core_v5.2.md#L63186)`:
- **Power Control Request procedure**: Either master or slave sends `LL_POWER_CONTROL_REQ`; peer adjusts TX power and replies with `LL_POWER_CONTROL_RSP` indicating actual change made `[Core 5.2, Vol 6, Part B, §5.1.17](../../sources/specs/5.2/Core_v5.2.md#L63186)`
- **Power Change Indication procedure**: Unsolicited `LL_POWER_CHANGE_IND` when a device changes its own TX power `[Core 5.2, Vol 6, Part B, §5.1.18](../../sources/specs/5.2/Core_v5.2.md#L63211)`
- **Power level management**: Controller manages power levels on all active PHYs for a given peer `[Core 5.2, Vol 6, Part B, §4.5.15](../../sources/specs/5.2/Core_v5.2.md#L62406)`
- **Path Loss Monitoring**: RSSI-based zone classification; Host sets high/low thresholds, Controller reports zone transitions via `HCI_LE_Path_Loss_Threshold` event `[Core 5.2, Vol 6, Part B, §4.5.16](../../sources/specs/5.2/Core_v5.2.md#L62413)`
- Feature bits: 4.6.30 (LE Power Change Indication), 4.6.31 (LE Power Control Request), 4.6.32 (LE Path Loss Monitoring)

---

## Deprecated / Removed

- None in 5.2 — all changes are additive
- BR/EDR audio (SCO/eSCO) still exists in the spec; LE Audio is additive
- Security erratum 11838 (encryption key size on BR/EDR) incorporated `[Core 5.2, Vol 1, Part C, §11.2]`

---

## Developer Impact

**High impact areas:**
- **True Wireless Stereo (TWS) earbuds**: CIS + CIG enables synchronized left/right audio with lower latency and better quality than Classic Bluetooth A2DP. Each earbud gets its own CIS within a CIG, locked to the same anchor timing.
- **Hearing aids**: BIS enables hearing loop broadcast; Auracast™ relies on BIS
- **Multi-room / broadcast audio**: BIS enables broadcasting to unlimited receivers simultaneously (Auracast™ brand). No pairing required.
- **GATT-heavy IoT**: EATT improves throughput for applications that read/write many characteristics; particularly useful during OTA firmware update + concurrent service reads
- **Power-constrained devices**: LE Power Control enables closed-loop TX power management, improving coexistence and battery life

**Key new profiles built on 5.2 ISO foundation:**
- **BAP** (Basic Audio Profile) — unicast (CIS) and broadcast (BIS) audio
- **CAP** (Common Audio Profile) — coordinator role for multi-device audio
- **TMAP** (Telephone and Media Audio Profile) — call + media audio
- **HAP** (Hearing Access Profile) — hearing aids
- **BASS** (Broadcast Audio Scan Service) — scan delegation for BIS

**HCI development:**
- New ISO data path: `HCI_LE_Set_CIG_Parameters` (master), `HCI_LE_Create_CIS`, `HCI_LE_Setup_ISO_Data_Path`
- New broadcast path: `HCI_LE_Create_BIG`, `HCI_LE_BIG_Create_Sync`
- ISO data transfer uses dedicated `HCI_ISO_Data_Packet` format (not ACL packets)

---

## Cross-References

- Diff from 5.1: [diff-5.1-to-5.2](../version-diff/diff-5.1-to-5.2.md)
- Diff to 5.3: [diff-5.2-to-5.3](../version-diff/diff-5.2-to-5.3.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md), [Profiles and Services](../concepts/profiles-and-services.md)

---

*Source: [Core 5.2](../../sources/specs/5.2/Core_v5.2.md)*
