# Bluetooth Core Specification 5.1

**Release Date**: 2019-01-21
**Status**: Superseded by 5.2
**Spec Volume**: ~3256 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-1/) | [Local PDF](../../sources/specs/core-spec-5.1.pdf) | [Local Markdown](../../sources/specs/core-spec-5.1.md)

---

## Executive Summary

Bluetooth 5.1 introduced **Direction Finding** — the most significant new capability since BLE itself.
By adding hardware support for measuring the **Angle of Arrival (AoA)** and **Angle of Departure (AoD)**
of a Bluetooth signal, 5.1 enabled sub-meter indoor positioning for asset tracking and navigation.

Beyond Direction Finding, 5.1 improved **GATT caching** (reducing reconnection overhead for bonded devices),
added **Advertising Channel Index** in the ADI field to help scanners detect duplicate advertising packets,
and introduced several minor Link Layer and HCI clarifications.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Direction Finding (AoA/AoD) | Phase/amplitude analysis of CTE for angle measurement | Vol 6, Part B, §2.5.4 |
| Constant Tone Extension (CTE) | Special signal appended to packets for angle measurement | Vol 6, Part B, §2.5.4 |
| Connectionless CTE | CTE in periodic advertising for AoA/AoD without a connection | Vol 6, Part B, §4.4.2 |
| Connection CTE | CTE exchanged over a connection | Vol 6, Part B, §4.5.13 |
| IQ Sample Reporting | Controller reports I/Q samples from antenna array to host | Vol 4, Part E |
| GATT Caching | Bonded clients cache GATT database; server signals changes via hash | Vol 3, Part G, §2.5.2 |
| Advertising Channel Index in ADI | ADI field includes channel index to detect duplicates | Vol 6, Part B, §2.3.4 |
| Sleep Clock Accuracy (SCA) Update | New LL procedure to update SCA during a connection | Vol 6, Part B, §4.5.16 |
| HCI for Direction Finding | New HCI commands/events for CTE TX/RX configuration | Vol 4, Part E |

---

## Key Changes to Existing Mechanisms

### Direction Finding

Direction Finding uses an **antenna array** on the receiver (AoA) or transmitter (AoD):

- **AoA (Angle of Arrival)**: The receiver has multiple antennas. The transmitter sends a CTE.
  The receiver switches antennas and samples I/Q data to calculate the angle of the incoming signal.
- **AoD (Angle of Departure)**: The transmitter has multiple antennas. It switches antennas while
  transmitting the CTE. The receiver (single antenna) measures phase differences to calculate the angle.

The **Constant Tone Extension (CTE)** is a fixed-frequency tone (250 µs to 160 µs segments)
appended to the end of a packet after the CRC. It does not affect backward compatibility —
5.0 and earlier receivers ignore the CTE.

### GATT Caching

Prior to 5.1, bonded GATT clients had to re-discover services on every reconnection.
5.1 introduced a **Database Hash** characteristic: the server computes a hash of its GATT database.
Clients store this hash; on reconnect, if the hash matches, the cached database is valid.
Servers set the **Change Unaware** flag for clients with stale caches.

### Advertising Data Information (ADI)

The ADI field (introduced in 5.0 extended advertising) gained a **channel index** sub-field,
allowing scanners to detect whether they are seeing the same advertising event from multiple channels.

---

## Deprecated / Removed

- None — 5.1 is fully backward compatible with 5.0 and earlier

---

## Developer Impact

**High impact areas:**
- **Indoor positioning systems**: AoA/AoD enables centimeter-to-meter accuracy positioning.
  Hardware must have multi-antenna arrays with switching capability.
- **Asset tracking**: Use Connectionless CTE with Periodic Advertising for scalable, connectionless positioning.
- **GATT-heavy applications**: Implement Database Hash to dramatically speed up reconnection for bonded devices.

**Hardware requirements:**
- Direction Finding requires antenna array hardware support in the controller
- Check `LE Features` bitmask for `LE Connection CTE Request` and `Connectionless CTE Transmitter` bits
- Software-only stacks cannot implement Direction Finding; it requires hardware IQ sampling

---

## Cross-References

- Diff from 5.0: [diff-5.0-to-5.1](../version-diff/diff-5.0-to-5.1.md)
- Diff to 5.2: [diff-5.1-to-5.2](../version-diff/diff-5.1-to-5.2.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md)
