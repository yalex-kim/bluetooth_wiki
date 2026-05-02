# Diff: Bluetooth Core Spec 5.1 → 5.2

**From**: [Core Spec 5.1](../versions/core-spec-5.1.md) (2019-01-21)
**To**: [Core Spec 5.2](../versions/core-spec-5.2.md) (2019-12-31)

---

## At a Glance

5.2 is the biggest update since BLE was introduced in 4.0. The **LE Audio** framework replaces
BR/EDR-based audio with a fully LE isochronous system (LC3 codec, CIS, BIS). **Enhanced ATT (EATT)**
removes the single-transaction bottleneck from GATT. **LE Power Control** adds closed-loop TX power
management. These three pillars each independently represent major capability increases.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **LC3 Codec** | Low Complexity Communication Codec — superior quality at 32–160 kbps vs SBC | Bluetooth LC3 spec |
| **Isochronous Channels (ISO)** | New Link Layer channel type with time-bounded guarantees | Vol 6, Part B |
| **CIS (Connected Isochronous Stream)** | Point-to-point isochronous audio within a connection | Vol 6, Part B, §4.5.14 |
| **CIG (Connected Isochronous Group)** | Groups CIS streams for synchronized multi-device audio | Vol 6, Part B |
| **BIS (Broadcast Isochronous Stream)** | Point-to-multipoint isochronous audio broadcast | Vol 6, Part B, §4.4.6 |
| **BIG (Broadcast Isochronous Group)** | Groups BIS streams (e.g., L+R audio channels) | Vol 6, Part B |
| **LE Isochronous Adaptation Layer (IAL)** | Framing/segmentation of codec frames over ISO | Vol 6, Part G |
| **Enhanced ATT (EATT)** | Multiple parallel ATT bearers via L2CAP CoC | Vol 3, Part F, §3.4.9 |
| **LE Power Control Request** | Device requests peer to adjust TX power | Vol 6, Part B, §4.5.17 |
| **LE Path Loss Monitoring** | RSSI-based zone tracking; host notified on zone change | Vol 6, Part B, §4.5.18 |
| **LE Enhanced Connection (v2)** | New HCI command for connection with PHY preferences | Vol 4, Part E |
| **HCI ISO Commands/Events** | Full set of HCI for CIG/CIS/BIG/BIS create/modify/destroy | Vol 4, Part E |

---

## Modified

| What | Change |
|------|--------|
| **ATT Protocol** | EATT adds L2CAP CoC bearer multiplexing; classic ATT Bearer still supported (backward compat) |
| **L2CAP** | New LE Credit-Based Connection PDUs supporting multiple bearers |
| **LE Features** | New bits for ISO channels, CIS, BIS, EATT, Power Control, Path Loss |
| **HCI LE Meta subevent** | ~15 new subevents for ISO data path, CIG, BIG events |
| **Periodic Advertising** | BIG sync uses periodic advertising as the discovery mechanism |

---

## Deprecated / Removed

- Nothing removed. BR/EDR audio (SCO/eSCO) still exists in the spec — LE Audio is additive.
  The Bluetooth SIG repositioned BR/EDR audio as legacy, but it remains in the spec.

---

## Migration Guide

### Adopting LE Audio

LE Audio is not a drop-in replacement for A2DP/HFP — it requires a full stack update:

1. **Controller**: Must support ISO channels (CIS and/or BIS). Check hardware.
2. **Host stack**: Must implement HCI ISO data path, CIG/BIG management.
3. **Profiles**: Implement BAP (Basic Audio Profile) which sits above ISO/LC3.
4. **Codec**: Integrate LC3 encoder/decoder (open-source reference implementation available from Bluetooth SIG).

**Use CIS for**: headsets, earbuds, hearing aids (point-to-point, bidirectional)
**Use BIS for**: Auracast broadcast, hearing loops, public address systems (one-to-many, unidirectional)

### Upgrading from classic ATT to EATT

EATT is negotiated via L2CAP CoC establishment (PSM 0x0027):
- Both sides must advertise `EATT Supported` in LE features
- After connection, either side initiates EATT bearer(s) via `L2CAP_CREDIT_BASED_CONNECTION_REQ`
- Classic ATT Bearer remains for backward compatibility

Benefits:
- Read multiple characteristics in parallel (each on its own bearer)
- Write and read simultaneously
- Notification delivery while Write Without Response is in progress

### LE Power Control

Implement the power control procedure to maintain link quality:
1. Periodically check RSSI vs. preferred RSSI range
2. If outside range: send `LL_POWER_CONTROL_REQ` to peer
3. Peer adjusts TX power and responds with current power level
4. Use Path Loss Monitoring events to track device proximity zones
