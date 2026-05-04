# Bluetooth Core Specification 5.0

**Release Date**: 2016-12-06
**Status**: Superseded by 5.1
**Spec Volume**: ~2822 pages
**Source**: [Local Markdown](../../sources/specs/5.0/Core_v5.0.md)

---

## Executive Summary

Bluetooth 5.0, released December 2016, was the most significant LE update since version 4.0 introduced BLE itself. Its headline improvements focused on **range**, **speed**, and **broadcast capacity** — making Bluetooth a viable option for a broader class of IoT applications.

The **LE 2M PHY** doubled LE throughput to 2 Mbps for connected devices (essential for wearables and audio accessories transferring bulk data). The **LE Coded PHY** enabled 4× or 8× range by adding forward error correction at the physical layer, opening Bluetooth to long-range IoT deployments such as smart city sensors, building automation, and asset tracking over hundreds of meters. **LE Advertising Extensions** offloaded advertising payloads to secondary data channels, allowing up to 255 bytes of advertising data — dramatically expanding use cases for beacons and connectionless broadcast, and laying the foundation for Bluetooth Mesh Networking.

5.0 also introduced **Slot Availability Mask (SAM)** to improve BR/EDR/LE coexistence scheduling, **Channel Selection Algorithm #2 (CSA#2)** for better channel distribution in connected links, and **Periodic Advertising** for synchronized connectionless broadcasts. Park State — a rarely-used BR/EDR power-saving mode — was deprecated in this version.

[Core 5.0, Vol 1, Part C, §9]

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| LE 2M PHY | 2 Msym/s symbol rate on LE; doubles throughput vs. LE 1M; uncoded only | Vol 6, Part B, §2.1 |
| LE Coded PHY (S=2, S=8) | FEC-encoded PHY at 1 Msym/s; S=2 = 500 kbps; S=8 = 125 kbps (~4–8× range) | Vol 6, Part B, §2.2 |
| LE Advertising Extensions | New PDU types offloading advertising data to secondary channels; up to 255 bytes | Vol 6, Part B, §2.3.4 |
| Extended Scanning | Scanner can receive extended advertising PDUs on secondary channels | Vol 6, Part B, §4.4.3 |
| Periodic Advertising | Synchronized connectionless broadcast at precise intervals; scanners sync via AUX_SYNC_IND | Vol 6, Part B, §4.4.2 |
| LE Channel Selection Algorithm #2 (CSA#2) | Pseudorandom channel selection with improved distribution across 37 data channels | Vol 6, Part B, §4.5.8 |
| Slot Availability Mask (SAM) | LMP mechanism to signal BR/EDR slot availability to LE scheduler for coexistence | Vol 2, Part B, §4.1.15; Vol 3, Part C, §4.18 |
| High Duty Cycle Non-Connectable Advertising | Removed previous minimum interval restriction on non-connectable advertising | Vol 6, Part B, §4.6.12 |
| HCI Extended Advertising Commands | New HCI commands for extended/periodic advertising set management | Vol 4, Part E, §7.8.52–7.8.69 |

---

## Key Changes to Existing Mechanisms

### Physical Layer (Vol 6, Part A; Vol 6, Part B, §2)

- **LE 1M PHY** (since 4.0): unchanged — 1 Msym/s GFSK, ~1 Mbps effective rate, always mandatory
- **LE 2M PHY** (new): same 2.4 GHz channel map as 1M, 2 Msym/s GFSK modulation, uncoded only
- **LE Coded PHY** (new): 1 Msym/s with FEC coding
  - **S=2** (rate 1/2 FEC): ~500 kbps effective — moderate range extension (~2× vs. 1M)
  - **S=8** (rate 1/8 FEC): ~125 kbps effective — maximum range (~4× vs. 1M, up to ~1 km line of sight)
  - Packet structure includes a SYNC word and FEC-encoded payload separated by a coded indicator (CI) field [Vol 6, Part B, §2.2]
- **PHY negotiation**: new LL procedures `LL_PHY_REQ` / `LL_PHY_RSP` / `LL_PHY_UPDATE_IND`; both ends select TX and RX PHYs independently

### Advertising (Vol 6, Part B, §2.3, §4.4)

- **Legacy advertising PDUs** (`ADV_IND`, `ADV_DIRECT_IND`, `ADV_NONCONN_IND`, `ADV_SCAN_IND`, `SCAN_RSP`) remain unchanged for backward compatibility; maximum payload 31 bytes [Vol 6, Part B, §2.3.1]
- **Extended advertising PDUs** (new): `ADV_EXT_IND` on primary channels carries only an `AuxPtr` + `ADI` field, chaining to secondary channel PDUs (`AUX_ADV_IND`, `AUX_CHAIN_IND`) with up to 255 bytes of actual advertising data [Vol 6, Part B, §2.3.4]
- **Primary advertising PHY**: can now be LE 1M or LE Coded for extended advertising; secondary channel can be LE 1M, LE 2M, or LE Coded
- **Periodic advertising** (`AUX_SYNC_IND`): advertiser establishes a sync train with a fixed interval; scanners establish synchronization via `LE Periodic Advertising Create Sync` without forming a connection [Vol 6, Part B, §4.4.2]

### Link Layer (Vol 6, Part B, §4.5)

- **CSA#2**: new pseudorandom channel selection algorithm coexists with CSA#1; connection establishment advertises which algorithm is used via `LE Channel Selection Algorithm` event [Vol 6, Part B, §4.5.8]
- Advertising extensions add new LL states: `Synchronizing`, `Synchronized` for periodic advertising

### BR/EDR Coexistence (Vol 2, Part B; Vol 3, Part C)

- **Slot Availability Mask (SAM)**: LMP-level mechanism allowing a device to inform its peer which BR/EDR time slots it will or will not use, enabling LE activity to be scheduled in those slots [Vol 2, Part B, §4.1.15]

---

## Deprecated / Removed

| Feature | Reason |
|---------|--------|
| Park State (BR/EDR) | Rarely used power-saving mode; superseded by sniff mode [Core 5.0, Vol 1, Part C, §9.2] |

5.0 is fully backward compatible with LE 4.x devices. All 5.0 LE features are optional; 4.x scanners continue to see legacy advertising PDUs normally.

---

## Developer Impact

**Range-critical applications**: Switch to LE Coded PHY (S=8) for indoor/outdoor sensors requiring >100 m range. Note: S=8 increases on-air time ~8× vs. LE 1M — factor into duty cycle and power budget calculations.

**High-throughput applications**: Use LE 2M PHY to reduce connection time for bulk transfers. Negotiate via `LL_PHY_REQ`; fall back to 1M automatically if peer does not support 2M.

**Beacon / proximity advertising**: Leverage Extended Advertising for richer payloads — no more 31-byte limit. Use `ADI` (Advertising Data Information) field to deduplicate scan reports across channels. Legacy beacons continue to work without changes.

**Asset tracking / synchronized sensors**: Periodic Advertising enables precise synchronization without requiring a connection. Combine with Extended Advertising for large sync metadata.

**Backward compatibility**:
- Controllers advertise PHY and feature support via `LE Features` bitmask (check bits for `LE 2M PHY`, `LE Coded PHY`, `LE Extended Advertising`)
- Connections with 4.x devices default to LE 1M PHY (always supported)
- Extended advertising requires both advertiser and scanner to be 5.0+

---

## Spec Structure (Volumes)

| Volume | Title | Notable Parts for 5.0 |
|--------|-------|-----------------------|
| Vol 1 | Architecture & Terminology | Part A (architecture overview incl. SAM §7.7), Part C (change history §9) |
| Vol 2 | BR/EDR Controller | Part B (Baseband, SAM §4.1.15), Part C (LMP) |
| Vol 3 | Host | Part C (GAP, SAM §4.18), Part F (ATT), Part G (GATT) |
| Vol 4 | HCI | Part E (new LE extended adv commands §7.8.52–7.8.69) |
| Vol 6 | LE Controller | Part A (PHY), Part B (LL: PHY §2.1–2.2, adv ext §2.3.4, periodic adv §4.4.2, CSA#2 §4.5.8) |

---

## Cross-References

- Diff to 5.1: [diff-5.0-to-5.1](../version-diff/diff-5.0-to-5.1.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md)

---

*Source: [Core 5.0](../../sources/specs/5.0/Core_v5.0.md)*
