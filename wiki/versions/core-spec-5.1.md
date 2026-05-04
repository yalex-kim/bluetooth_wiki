# Bluetooth Core Specification 5.1

**Release Date**: 2019-01-21
**Status**: Superseded by 5.2
**Spec Volume**: ~3256 pages
**Source**: [Local Markdown](../../sources/specs/5.1/Core_v5.1.md)

---

## Executive Summary

Bluetooth 5.1, released January 2019, introduced **Direction Finding** — the most significant new LE capability since BLE itself was introduced in 4.0. By specifying hardware-level support for measuring the **Angle of Arrival (AoA)** and **Angle of Departure (AoD)** of a Bluetooth signal using an antenna array, 5.1 enabled centimeter-to-meter-accuracy indoor positioning without requiring additional infrastructure technologies.

Beyond Direction Finding, 5.1 improved **GATT caching** (reducing reconnection overhead for bonded devices), added several Link Layer and HCI quality-of-life improvements, and incorporated **Periodic Advertising Sync Transfer (PAST)** — enabling a connected device to share its periodic advertising sync state with a peer, eliminating the need for the peer to scan and re-sync independently.

The spec also deprecated **Unit Keys** (a legacy BR/EDR security mechanism from the Bluetooth 1.x era) and incorporated over a hundred errata fixes from ESR11 and ESR12.

[Core 5.1, Vol 1, Part C, §10]

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Angle of Arrival (AoA) | Receiver with antenna array samples I/Q data during CTE; calculates incoming signal angle | Vol 1, Part A, §8.1; Vol 6, Part B, §2.5.4 |
| Angle of Departure (AoD) | Transmitter switches antennas during CTE; single-antenna receiver measures phase difference | Vol 1, Part A, §8.2; Vol 6, Part B, §2.5.4 |
| Constant Tone Extension (CTE) | Fixed-frequency tone appended after CRC for angle measurement; ignored by 5.0 and earlier | Vol 6, Part B, §2.5.1–2.5.3 |
| Connectionless CTE Transmitter/Receiver | CTE embedded in periodic advertising PDUs (AUX_SYNC_IND) for infrastructure positioning | Vol 6, Part B, §4.6.18–4.6.19 |
| Connection CTE Request/Response | CTE exchanged over an established connection via LL procedures | Vol 6, Part B, §4.6.16–4.6.17; §5.1.12 |
| IQ Sampling | Controller captures I/Q samples from antenna array during CTE reception; reports to host | Vol 6, Part B, §2.5.4 |
| GATT Caching / Database Hash | Server exposes a hash of its GATT database; bonded clients skip re-discovery if hash matches | Vol 3, Part G, §7.3; §7.3.1 |
| Advertising Channel Index in ADI | ADI field (Extended Advertising) gains a channel index sub-field for deduplication | Vol 6, Part B, §2.3.4 |
| Periodic Advertising Sync Transfer (PAST) | Connected device transfers its periodic advertising sync state to peer; eliminates re-scan | Vol 6, Part B, §4.6.23–4.6.24; §5.1.13 |
| Sleep Clock Accuracy (SCA) Update | New LL procedure to update SCA during a connection lifetime | Vol 6, Part B, §4.6.25; §5.1.14 |
| ADI Field in Scan Response Data | ADI field now permitted in scan response PDUs | Vol 6, Part B, §2.3 |
| HCI Support for DF Commands | ~15 new HCI commands for CTE TX/RX configuration and IQ sample reporting | Vol 4, Part E, §7.8.80–7.8.87 |
| HCI Debug Keys in LE Secure Connections | HCI command to enable debug keys for testing purposes | Vol 4, Part E |
| Host Channel Classification for Secondary Advertising | Host can specify channel classification for secondary advertising channels | Vol 4, Part E |
| Mesh-Based Model Hierarchy | Architecture overview updated to include Mesh model/property hierarchy | Vol 1, Part A, §6.6 |

---

## Key Changes to Existing Mechanisms

### Direction Finding (Vol 1, Part A, §8; Vol 6, Part B, §2.5)

Direction Finding uses an **antenna array** on either the receiver or transmitter side:

- **AoA (Angle of Arrival)**: The receiver has multiple antennas. The transmitter sends a **Constant Tone Extension (CTE)** using a single antenna. The receiver switches antennas during the CTE and collects I/Q samples; the phase differences across antennas determine the angle of the incoming signal. [Vol 1, Part A, §8.1; Vol 6, Part B, §4.6.21]
- **AoD (Angle of Departure)**: The transmitter has multiple antennas. It switches antennas during the CTE transmission. The receiver (single antenna) measures the phase variations in the received CTE to calculate the angle of departure. [Vol 1, Part A, §8.2; Vol 6, Part B, §4.6.20]

The **Constant Tone Extension** is a fixed-frequency continuous tone transmitted after the CRC of a packet. It does not contain data — its sole purpose is to allow antenna switching and I/Q sampling. CTE length ranges from 16 µs minimum (2 µs slots) to 160 µs maximum. The CTEInfo field in the PDU header indicates CTE type and length. [Vol 6, Part B, §2.5.1–2.5.2]

Because the CTE is appended **after** the CRC, legacy (5.0 and earlier) devices simply ignore the extra bytes — backward compatibility is fully preserved.

Two delivery modes:
- **Connectionless CTE**: Appended to `AUX_SYNC_IND` periodic advertising PDUs; no connection required; ideal for infrastructure positioning systems [Vol 6, Part B, §4.6.18–4.6.19]
- **Connection CTE**: Requested/provided via `LL_CTE_REQ` / `LL_CTE_RSP` procedures over an established connection [Vol 6, Part B, §4.6.16–4.6.17]

Controller reports I/Q samples to the host via new HCI events:
- `LE Connectionless IQ Report` subevent
- `LE Connection IQ Report` subevent
- `LE CTE Request Failed` subevent

### GATT Caching (Vol 3, Part G, §7.3)

Prior to 5.1, a bonded GATT client was required to perform full service discovery on every reconnection (or at least validate the `Service Changed` indication). With 5.1:

- The GATT server exposes a new **Database Hash** characteristic (`0x2B2A`) containing an AES-CMAC hash computed over all attributes in the GATT database [Vol 3, Part G, §7.3.1]
- A bonded client stores the hash after initial discovery. On reconnect, the client reads the hash; if it matches the stored value, the cached service discovery is still valid and can be used without re-discovery
- If the hash has changed, the server also sets the **Change Unaware** flag for that client, prompting re-discovery
- Clients that do not support caching continue to work normally — the `Database Hash` characteristic is optional to implement but standardizes the caching behavior

### Periodic Advertising Sync Transfer (PAST) (Vol 6, Part B, §5.1.13)

In 5.0, a device that wanted to sync to a periodic advertiser had to scan for the advertiser itself. PAST in 5.1 allows a device that already has an established periodic advertising sync to transfer that sync state to a connected peer via a new LL procedure (`LL_PERIODIC_SYNC_IND`). The recipient device can begin receiving the periodic advertising without needing to scan — reducing latency and scan energy.

### ADI Field Enhancements (Vol 6, Part B, §2.3.4)

The `ADI` (Advertising Data Information) field introduced in 5.0 Extended Advertising was augmented with a **channel index** sub-field. This allows a scanner receiving the same advertising event on multiple channels to identify and deduplicate reports from the same advertising event.

---

## Deprecated / Removed

| Feature | Reason |
|---------|--------|
| Unit Keys (BR/EDR) | Legacy 1.x-era security mechanism; superseded by Combination Keys since 2.0; formally deprecated [Core 5.1, Vol 1, Part C, §10.2] |

5.1 is otherwise fully backward compatible with 5.0 and all earlier LE versions. Devices that do not support Direction Finding continue to operate normally — the CTE is ignored.

---

## Developer Impact

**Indoor positioning systems (AoA — infrastructure anchors)**:
- Deploy 5.1 anchor devices (readers) with multi-element antenna arrays
- Tags can be simple 5.x advertisers using Connectionless CTE in Periodic Advertising
- Anchors collect IQ samples and run AoA algorithms on the host (or cloud) side
- Sub-meter accuracy achievable with well-calibrated multi-anchor systems

**Indoor positioning systems (AoD — tag-side antenna array)**:
- Tags carry the antenna array and switch during CTE transmission
- Readers have simple single-antenna hardware
- Better suited for large deployments where reader cost/complexity must be minimized

**Hardware requirements**: Direction Finding is a **hardware feature** — it requires antenna array switching circuitry integrated with the radio controller. Check `LE Features` bitmask for bits:
- `Connectionless CTE Transmitter` / `Connectionless CTE Receiver`
- `Connection CTE Request` / `Connection CTE Response`
- `Antenna Switching During CTE Transmission (AoD)` / `Antenna Switching During CTE Reception (AoA)`
- `Receiving Constant Tone Extensions` / `Sampling Received CTE`

**GATT-heavy applications**: Implement **Database Hash** in GATT servers. Bonded clients implementing GATT caching can reduce reconnection time from hundreds of milliseconds (full discovery) to under 10 ms (hash comparison only).

**Periodic advertising consumers**: Implement PAST support to allow connected peers to share sync state, avoiding redundant scanning in multi-device ecosystems.

---

## Cross-References

- Diff from 5.0: [diff-5.0-to-5.1](../version-diff/diff-5.0-to-5.1.md)
- Diff to 5.2: [diff-5.1-to-5.2](../version-diff/diff-5.1-to-5.2.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md)

---

*Source: [Core 5.1](../../sources/specs/5.1/Core_v5.1.md)*
