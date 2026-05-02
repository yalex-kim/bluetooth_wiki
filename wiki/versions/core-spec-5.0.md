# Bluetooth Core Specification 5.0

**Release Date**: 2016-12-06
**Status**: Superseded by 5.1
**Spec Volume**: ~2822 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-0/) | [Local PDF](../../sources/specs/core-spec-5.0.pdf) | [Local Markdown](../../sources/specs/core-spec-5.0.md)

---

## Executive Summary

Bluetooth 5.0 was the most significant LE update since 4.0 introduced BLE itself.
Its headline improvements focused on **range**, **speed**, and **broadcast capacity** — each roughly doubling or quadrupling the previous generation.

The **LE 2M PHY** doubled throughput for connected devices (important for wearables and audio accessories).
The **LE Coded PHY** enabled 4× range by adding forward error correction, opening Bluetooth to long-range IoT
applications (smart city sensors, building automation, asset tracking).
**Extended Advertising** allowed 255-byte payloads on secondary channels, enabling 8× more data per broadcast
and preparing the foundation for Bluetooth Mesh Networking (standardized separately as a profile).

5.0 also introduced **Slot Availability Masks (SAM)** for improved BR/EDR/LE coexistence and a number of
Link Layer improvements that increased scheduling determinism.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| LE 2M PHY | 2 Mbps symbol rate on LE; doubles throughput for connected links | Vol 6, Part B, §1.2 |
| LE Coded PHY (S=2, S=8) | FEC-encoded PHY for 4× (S=2) or 8× (S=8) range at reduced data rate | Vol 6, Part B, §1.2 |
| Extended Advertising | Advertising data offloaded to 37 data channels; payloads up to 255 bytes | Vol 6, Part B, §2.3.4 |
| Extended Scanning | Scanner can receive extended advertising on secondary channels | Vol 6, Part B, §4.4.3 |
| Periodic Advertising | Synchronized, connectionless broadcast at precise intervals | Vol 6, Part B, §4.4.2 |
| Advertising Extension (HCI) | New HCI commands for extended/periodic advertising control | Vol 4, Part E |
| Slot Availability Mask (SAM) | Mechanism to signal BR/EDR slot availability for LE coexistence | Vol 2, Part B |
| LE Channel Selection Algorithm #2 | Improved channel selection for better coexistence | Vol 6, Part B, §4.5.8 |
| High Duty Cycle Non-Connectable Adv | Removed restriction on non-connectable advertising interval | Vol 6, Part B |

---

## Key Changes to Existing Mechanisms

### Physical Layer
- Added LE 2M PHY (GFSK at 2 Mbps): same channel map as LE 1M, increased throughput
- Added LE Coded PHY: uses FEC with two coding schemes:
  - **S=2** (500 kbps effective): 2 symbols per bit — moderate range extension
  - **S=8** (125 kbps effective): 8 symbols per bit — maximum range (~1 km line of sight)
- PHY negotiation via **LL_PHY_REQ / LL_PHY_RSP** procedure
- Both sides independently select TX and RX PHYs

### Advertising
- **Legacy advertising** (PDU types ADV_IND, ADV_NONCONN_IND, etc.) unchanged for backward compatibility
- **Extended advertising**: new PDU types with AuxPtr chaining, enabling multi-packet large payloads
- **Periodic advertising**: advertiser establishes a sync train; scanners can sync without a full connection

### Link Layer
- Channel Selection Algorithm #2 (CSA#2): pseudorandom with better distribution across channels
- New LL procedure for PHY update: `LL_PHY_REQ`, `LL_PHY_RSP`, `LL_PHY_UPDATE_IND`

---

## Deprecated / Removed

- None — 5.0 is fully backward compatible with 4.x devices

---

## Developer Impact

**High impact areas:**
- **Range-critical applications**: Switch to LE Coded PHY for indoor/outdoor sensors needing >100m range
- **High-throughput applications**: Use LE 2M PHY to reduce connection time for large data transfers
- **Beacons and proximity**: Leverage Extended Advertising for richer payloads (no more 31-byte limit)
- **Asset tracking / location**: Periodic Advertising enables precise synchronization for positioning systems

**Backward compatibility:**
- 5.0 controllers advertise PHY capabilities via `LE Features` bitmask
- Connections with 4.x devices default to LE 1M PHY (always supported)
- Extended advertising is optional; 4.x scanners only see legacy advertising PDUs

---

## Spec Structure (Volumes)

| Volume | Title | Notable Parts |
|--------|-------|---------------|
| Vol 1 | Architecture & Terminology | Overview, Profiles |
| Vol 2 | BR/EDR Controller | Baseband, LMP, Radio |
| Vol 3 | Host | L2CAP, SDP, GAP, SM, GATT, ATT |
| Vol 4 | HCI | HCI Commands & Events (incl. new LE extended adv HCI) |
| Vol 5 | AMP Controller | 802.11 PAL |
| Vol 6 | LE Controller | PHY, LL, DTM |

---

## Cross-References

- Diff from 4.2: [diff-4.2-to-5.0](../version-diff/) _(not yet created — ingest 4.2 spec to generate)_
- Diff to 5.1: [diff-5.0-to-5.1](../version-diff/diff-5.0-to-5.1.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md), [Overview](../overview.md)
