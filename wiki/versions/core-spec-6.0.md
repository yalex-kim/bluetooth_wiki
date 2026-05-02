# Bluetooth Core Specification 6.0

**Release Date**: 2024-08-27
**Status**: Active (current as of 2026-05)
**Spec Volume**: ~4114 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-6-0/) | [Local PDF](../../sources/specs/core-spec-6.0.pdf) | [Local Markdown](../../sources/specs/core-spec-6.0.md)

---

## Executive Summary

Bluetooth 6.0 introduced **LE Channel Sounding (CS)** — a new physical-layer technique for
**precise distance measurement** using phase-based ranging (PBR) and round-trip time (RTT).
Channel Sounding achieves centimeter-level ranging accuracy, enabling new classes of applications:
digital car keys, asset location with precision, access control, and anti-relay attack protection.

**Decision-Based Advertising Filtering (DBAF)** gave the controller intelligence to filter
advertising reports based on customizable criteria without waking the host, dramatically reducing
power consumption in scanner applications.

**Monitoring Advertisers** allows the host to track advertising activity (appearance and disappearance
of devices) at the controller level, again minimizing host wakeups.

6.0 also added Frame Space Updates for tighter timing control and improvements to the
Isochronous Adaptation Layer.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| LE Channel Sounding (CS) | Phase-based ranging and RTT for centimeter accuracy distance | Vol 6, Part B, §4.5.22 |
| CS Procedures | Initiator/reflector roles, step types (tone, RTT) | Vol 6, Part B, §4.5.22 |
| CS Security | Anti-spoofing, anti-relay via CS capabilities | Vol 6, Part H |
| Decision-Based Advertising Filtering (DBAF) | Controller-side filtering of advertising reports per custom rules | Vol 6, Part B, §4.4.3 |
| Monitoring Advertisers | Track appearance/disappearance of advertisers at controller level | Vol 6, Part B, §4.4.3 |
| Frame Space Updates | New minimum/maximum frame space values for tighter scheduling | Vol 6, Part B, §4.2.3 |
| LE L2CAP Enhancements | Credit-based connection improvements | Vol 3, Part A |
| ISO Adaptation Layer (IAL) updates | Segmentation/reassembly improvements for audio streams | Vol 6, Part G |

---

## Key Changes to Existing Mechanisms

### LE Channel Sounding (CS)

Channel Sounding is a **physical layer measurement procedure** that uses two techniques:

**Phase-Based Ranging (PBR)**:
- Both devices transmit tones on multiple channels
- The receiver measures phase differences across channels
- Phase difference → distance calculation (exploiting the relationship: phase = 2πd·f/c)
- Achieves ~10 cm accuracy under favorable conditions

**Round-Trip Time (RTT)**:
- Precise measurement of signal travel time (like radar)
- Both devices cooperate: initiator sends a tone, reflector responds
- Time of flight → distance

**CS Procedure**:
- Two roles: **Initiator** (starts measurement) and **Reflector** (responds)
- A **CS Configuration** defines: channel map, tone duration, RTT type, repetitions
- **CS Steps**: each step is either a RTT exchange, tone transmission, or both
- Results reported to host via `LE_CS_Subevent_Result` events

**Security features**:
- CS includes **anti-spoofing** (random timing jitter makes relay attacks measurable)
- Designed for **PACS (Physical Access Control Systems)** — digital car keys, door locks
- UWB (Ultra-Wideband) comparable accuracy but via Bluetooth radio

### Decision-Based Advertising Filtering (DBAF)

Pre-6.0: The host specified a simple filter (whitelist/blacklist by address).
The controller sent all matching advertising reports to the host.

DBAF allows the host to program a set of **decision rules** into the controller:
- Rules can reference RSSI thresholds, AD type content, address patterns
- The controller evaluates rules per advertising report
- Only reports that pass the rules (or trigger a threshold crossing) are sent to host
- Dramatically reduces host wakeups in dense advertising environments (e.g., airports, retail floors)

### Monitoring Advertisers

A new scanner state that tracks when a specific device (by address) starts or stops advertising.
The host registers a list of addresses to monitor. The controller:
- Notifies the host when a monitored device's advertising is first detected
- Notifies when a monitored device stops advertising (timeout-based)

Eliminates polling and dramatically reduces duty cycle for proximity detection applications.

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
- Related concepts: [Security](../concepts/security.md), [BLE Architecture](../concepts/ble-architecture.md)
