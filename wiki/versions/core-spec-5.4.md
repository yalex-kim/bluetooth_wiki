# Bluetooth Core Specification 5.4

**Release Date**: 2023-01-31
**Status**: Superseded by 6.0
**Spec Volume**: ~3869 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-4/) | [Local PDF](../../sources/specs/core-spec-5.4.pdf) | [Local Markdown](../../sources/specs/core-spec-5.4.md)

---

## Executive Summary

Bluetooth 5.4 introduced four new features: **Periodic Advertising with Responses (PAwR)**,
**Encrypted Advertising Data (EAD)**, **Advertising Coding Selection**, and the
**LE GATT Security Levels Characteristic**. [Core 5.4, Vol 0, Part C, §13.1]

**PAwR** extends the 5.0 Periodic Advertising model with a bidirectional component: devices
can now respond to periodic advertising packets within assigned response slots. This enables
a single advertiser (coordinator) to communicate with thousands of devices simultaneously
without establishing individual connections, transforming Bluetooth into a scalable broadcast
protocol for retail (Electronic Shelf Labels), industrial IoT, and smart building applications.

**EAD** adds privacy-preserving encryption to advertising payloads using AES-128-CCM,
allowing only authorized scanners with the pre-shared session key to decrypt advertising content.

5.4 also incorporated all features from withdrawn Core Spec 5.3 (Connection Subrating,
Enhanced Connection Update, Advertising Coding Selection). The version date is 2023-01-31
per the spec header; the Bluetooth SIG Board adoption date is 2023-02-02.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Periodic Advertising with Responses (PAwR) | Bidirectional periodic advertising; devices reply in assigned slots using AUX_SYNC_SUBEVENT_IND/RSP PDUs | [Core 5.4, Vol 6, Part B, §4.6.38–4.6.39] |
| Encrypted Advertising Data (EAD) | AES-128-CCM encrypted advertising payload; AD type Encrypted Data wraps payload | [Core 5.4, Vol 1, Part A, §5.4.6; Vol 3, Part C, §10.10] |
| LE GATT Security Levels Characteristic | New GATT characteristic (UUID 0x2BF5) exposing server's highest LE security requirement | [Core 5.4, Vol 3, Part C, §12.7] |
| Advertising Coding Selection | Host control over S=2 or S=8 data coding for LE Coded PHY advertising | [Core 5.4, Vol 6, Part B, §4.6.37] |
| Connection Subrating (from 5.3) | Reduce connection event frequency while maintaining connection — inherited from withdrawn 5.3 | [Core 5.4, Vol 6, Part B] |
| LE Enhanced Connection Update (from 5.3) | Controller-initiated connection parameter updates — inherited from withdrawn 5.3 | [Core 5.4, Vol 6, Part B] |

---

## Key Changes to Existing Mechanisms

### Periodic Advertising with Responses (PAwR)

Classic Periodic Advertising (introduced in 5.0) was strictly one-way: one advertiser,
many listeners. PAwR adds **response slots** within each advertising interval.
[Core 5.4, Vol 1, Part A, §1.2 (LE Periodic Physical Link)]

**Logical transport**: A PAwR logical transport is created whenever an advertising device
begins periodic advertising configured to use subevents and responses. The PAwR logical
transport is identified by the advertiser's Bluetooth Device Address, timing, and advertising set.
[Core 5.4, Vol 1, Part A, §3.5.4 — PAwR logical transport]

**Structure**:
```
Periodic Advertising Interval
├── Advertising Subevent 0  (AUX_SYNC_SUBEVENT_IND PDU)
│   └── Response slot 0..N  (AUX_SYNC_SUBEVENT_RSP PDUs, devices → advertiser)
├── Advertising Subevent 1
│   └── ...
└── Advertising Subevent M  (up to 0x80 = 128 subevents)
```

Key parameters from `HCI_LE_Set_Periodic_Advertising_Parameters_v2`
[Core 5.4, Vol 4, Part E]:
- `Num_Subevents`: 0x01 to 0x80 (up to 128 subevents per periodic advertising event)
- `Num_Response_Slots`: 0 to 0xFF (up to 255 response slots per subevent)
- `Subevent_Interval`: time between subevents; must be ≤ Periodic_Advertising_Interval_Min / Num_Subevents
- `Response_Slot_Spacing`: time between consecutive response slots

New PDU types [Core 5.4, Vol 6, Part B, §2]:
- `AUX_SYNC_SUBEVENT_IND` — advertiser → devices (broadcast per subevent)
- `AUX_SYNC_SUBEVENT_RSP` — device → advertiser (in assigned response slot)
- `LL_PERIODIC_SYNC_WR_IND` — synchronization transfer for PAwR trains

New HCI commands [Core 5.4, Vol 4, Part E]:
- `HCI_LE_Set_Periodic_Advertising_Parameters_v2` — configures PAwR with subevents
- `HCI_LE_Set_Periodic_Advertising_Subevent_Data` — sets data for one or more subevents
- `HCI_LE_Set_Periodic_Advertising_Response_Data` — sets response data for a specific slot
- `HCI_LE_Set_Periodic_Sync_Subevent` — instructs controller to sync with a subset of subevents

New LE Feature bits [Core 5.4, Vol 6, Part B, §4.6.38–4.6.39]:
- Bit 43: Periodic Advertising with Responses — Advertiser
- Bit 44: Periodic Advertising with Responses — Scanner

**ESL (Electronic Shelf Labels)** are the primary use case: a gateway can update thousands
of price tags simultaneously, and tags acknowledge receipt — all without individual connections.

### Encrypted Advertising Data (EAD)

EAD prevents fingerprinting of devices based on advertising data content even when the
Bluetooth Device Address is being randomized. [Core 5.4, Vol 1, Part A, §5.4.6]

The encrypted advertising data uses a **pre-shared session key** communicated only to
peer devices that are authorized to receive such information. Only devices with the key
material can decrypt and authenticate advertising messages.

The AD type **Encrypted Data** wraps the encrypted payload. Key distribution leverages
existing Security Manager (SM) procedures over an established connection.
[Core 5.4, Vol 3, Part C, §10.10 — Encrypted Advertising Data procedure]

**Feature type**: Type 4 (Host feature — does not involve the Controller directly).
[Core 5.4, Vol 0, Part D, Table 4.2]

### LE GATT Security Levels Characteristic

A new GATT characteristic (UUID `0x2BF5`) that exposes the highest security requirements
of the GATT server when operating on a LE connection. [Core 5.4, Vol 3, Part C, §12.7]

The characteristic value is static during a connection and contains a sequence of one or
more Security Level Requirements (see Table 12.11 in the spec). A device shall have at
most one instance of a LE GATT Security Levels characteristic.

**Feature type**: Type 4 (Host feature). [Core 5.4, Vol 0, Part D, Table 4.2]

### Advertising Coding Selection

Allows the Host to explicitly select the coding scheme (S=2 for 2 Mbps effective data rate,
or S=8 for maximum range) for LE Coded PHY advertising, rather than leaving it to the
Controller. [Core 5.4, Vol 6, Part B, §4.6.37]

**Feature type**: Type 2 (Controller feature configurable by Host). Requires both LE Extended
Advertising and LE Coded PHY features. [Core 5.4, Vol 0, Part D, Table 4.2]

---

## Deprecated / Removed

- None — 5.4 is backward compatible; PAwR and EAD are optional features

---

## Developer Impact

**High impact areas:**
- **Electronic Shelf Labels (ESL)**: PAwR is the foundational spec for the Bluetooth ESL profile.
  Retailers deploying hundreds or thousands of price tags should target 5.4 hardware.
- **Smart building / industrial IoT**: PAwR's star topology at scale (1 coordinator → 16K devices)
  suits building management systems, factory sensor networks.
- **Privacy-sensitive advertising**: EAD for medical devices, employee badges, any device
  where advertising payload confidentiality matters.

**Auracast™ + PAwR complement**: Auracast uses BIS (from 5.2) for audio broadcast;
PAwR enables control/signaling alongside it.

---

## Cross-References

- Diff from 5.3: [diff-5.3-to-5.4](../version-diff/diff-5.3-to-5.4.md)
- Diff to 6.0: [diff-5.4-to-6.0](../version-diff/diff-5.4-to-6.0.md)
- Related concepts: [Security](../concepts/security.md), [BLE Architecture](../concepts/ble-architecture.md)
