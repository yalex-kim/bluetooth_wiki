# Bluetooth Core Specification 5.2

**Release Date**: 2019-12-31
**Status**: Superseded by 5.3
**Spec Volume**: ~3544 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-2/) | [Local PDF](../../sources/specs/core-spec-5.2.pdf) | [Local Markdown](../../sources/specs/core-spec-5.2.md)

---

## Executive Summary

Bluetooth 5.2 delivered the **LE Audio** framework — the most transformative update to Bluetooth
audio since A2DP. LE Audio replaces the BR/EDR-based audio stack (SCO/eSCO + SBC) with a
fully LE-based isochronous audio system, introducing the **LC3 (Low Complexity Communication Codec)**
for superior audio quality at lower bitrates.

The foundation of LE Audio is **Isochronous Channels**: **CIS** (Connected Isochronous Streams) for
one-to-one audio (e.g., earbuds) and **BIS** (Broadcast Isochronous Streams) for one-to-many audio
(e.g., TV audio broadcast to hearing aids or headphones in a gym).

Additionally, 5.2 introduced **Enhanced ATT (EATT)** for parallel GATT transactions and
**LE Power Control** for dynamic TX power optimization.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| LE Audio Framework | Full LE-based audio system replacing BR/EDR SCO audio | Vol 3, Part G/H |
| LC3 Codec | Low Complexity Communication Codec; better quality at lower bitrates | Bluetooth LC3 spec (separate) |
| Isochronous Channels (ISO) | Time-synchronized data channels for audio streams | Vol 6, Part B, §4.4 |
| CIS (Connected Isochronous Stream) | Isochronous audio within a connection (point-to-point) | Vol 6, Part B, §4.5.14 |
| BIS (Broadcast Isochronous Stream) | Isochronous audio broadcast (point-to-multipoint) | Vol 6, Part B, §4.4.6 |
| LE Isochronous Adaptation Layer (IAL) | Framing/segmentation of codec frames over ISO channels | Vol 6, Part G |
| Enhanced ATT (EATT) | Multiple parallel GATT transactions over L2CAP CoC | Vol 3, Part F, §3.4.9 |
| LE Power Control | Dynamic TX power adjustment with feedback | Vol 6, Part B, §4.5.17 |
| LE Path Loss Monitoring | RSSI-based path loss estimation for power control | Vol 6, Part B, §4.5.18 |

---

## Key Changes to Existing Mechanisms

### Isochronous Channels Architecture

ISO channels guarantee **time-bounded delivery** by using a fixed schedule (isochronous interval).
Unlike ACL connections (best-effort), ISO channels define:
- **SDU Interval**: How often audio frames are generated
- **Transport Latency**: Maximum acceptable latency
- **Framing**: Framed (variable-length SDUs) or unframed (fixed-length)
- **Retransmission**: Optional RTN (retransmission number) for reliability vs. latency tradeoff

**CIS** (Connected Isochronous Stream):
- Lives within an ACL connection
- Supports bidirectional audio (e.g., microphone + speaker in a headset)
- A **CIG** (Connected Isochronous Group) groups multiple CIS for synchronized playback (e.g., left + right earbuds)

**BIS** (Broadcast Isochronous Stream):
- No ACL connection needed
- Unlimited receivers
- A **BIG** (Broadcast Isochronous Group) groups multiple BIS (e.g., left + right channel)
- Used for: hearing loop broadcast, public audio, TV audio

### Enhanced ATT (EATT)

Classic ATT (pre-5.2) is a single-channel protocol: only one transaction at a time.
EATT creates multiple **Enhanced ATT Bearers** over L2CAP Credit-Based Channels (CoC).
Each bearer allows independent concurrent transactions, dramatically improving GATT throughput
for multi-characteristic operations (e.g., reading many characteristics simultaneously).

### LE Power Control

Devices can request each other to adjust TX power to maintain optimal link quality.
New LL procedures: `LL_POWER_CONTROL_REQ / RSP / IND`.
Path loss monitoring uses RSSI measurements to classify link distance into zones
and triggers events when the device moves between zones.

---

## Deprecated / Removed

- None — 5.2 is backward compatible; ISO channels are optional controller features

---

## Developer Impact

**High impact areas:**
- **True Wireless Stereo (TWS) earbuds**: CIS + CIG enables synchronized left/right audio with lower latency and better quality than Classic Bluetooth A2DP
- **Hearing aids**: BIS enables hearing loop broadcast; AuraStream and Auracast rely on BIS
- **Multi-room / broadcast audio**: BIS enables broadcasting to unlimited receivers (Auracast™ brand)
- **GATT-heavy IoT**: EATT improves throughput for applications that read/write many characteristics

**Key new profiles built on 5.2:**
- **BAP** (Basic Audio Profile) — defines unicast and broadcast audio
- **CAP** (Common Audio Profile) — coordinator role for multi-device audio
- **TMAP** (Telephone and Media Audio Profile)
- **HAP** (Hearing Access Profile)

---

## Cross-References

- Diff from 5.1: [diff-5.1-to-5.2](../version-diff/diff-5.1-to-5.2.md)
- Diff to 5.3: [diff-5.2-to-5.3](../version-diff/diff-5.2-to-5.3.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md), [Profiles](../concepts/profiles-and-services.md)
