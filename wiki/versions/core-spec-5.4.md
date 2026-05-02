# Bluetooth Core Specification 5.4

**Release Date**: 2023-02-02
**Status**: Superseded by 6.0
**Spec Volume**: ~3869 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-4/) | [Local PDF](../../sources/specs/core-spec-5.4.pdf) | [Local Markdown](../../sources/specs/core-spec-5.4.md)

---

## Executive Summary

Bluetooth 5.4 introduced two major features for IoT and ESL (Electronic Shelf Label) use cases.

**Periodic Advertising with Responses (PAwR)** extends the 5.0 Periodic Advertising model
with a bidirectional component: devices can now respond to periodic advertising packets within
a defined response slot. This enables a single advertiser (coordinator) to communicate with
thousands of devices simultaneously without establishing individual connections — transforming
Bluetooth into a scalable broadcast protocol for retail, industry, and smart building applications.

**Encrypted Advertising Data (EAD)** adds privacy-preserving encryption to advertising payloads,
allowing only authorized scanners with the shared key to decrypt advertising content.

5.4 also superseded the withdrawn 5.3, incorporating all 5.3 features.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Periodic Advertising with Responses (PAwR) | Bidirectional periodic advertising; devices reply in assigned slots | Vol 6, Part B, §4.4.2.7 |
| Encrypted Advertising Data (EAD) | AES-128-CCM encrypted advertising payload | Vol 3, Part C, §11.8 |
| LE GATT Security Levels | New GATT characteristic for exposing LE security level | Vol 3, Part G |
| Advertising Data Types for PAwR | New AD type structures for PAwR coordination | Bluetooth Assigned Numbers |
| Connection Subrating (from 5.3) | Inherited from withdrawn 5.3 | Vol 6, Part B, §4.5.20 |
| LE Enhanced Connection Update (from 5.3) | Inherited from withdrawn 5.3 | Vol 6, Part B, §4.5.19 |

---

## Key Changes to Existing Mechanisms

### Periodic Advertising with Responses (PAwR)

Classic Periodic Advertising (5.0) was strictly one-way: one advertiser, many listeners.
PAwR adds **response slots** within each advertising interval:

```
Periodic Advertising Interval
├── Advertising Subevent 0
│   ├── Advertiser → Devices (broadcast)
│   └── Response slot 0..N (devices → advertiser)
├── Advertising Subevent 1
│   └── ...
└── Advertising Subevent M
```

Key properties:
- Each device is assigned a specific **subevent** and **response slot** to avoid collisions
- Up to 128 subevents, each with up to 128 response slots = up to 16,384 devices per coordinator
- Devices only wake up for their assigned subevent → ultra-low power
- **ESL (Electronic Shelf Labels)** are the primary use case: a gateway can update thousands of
  price tags with new prices, and tags acknowledge receipt — all without individual connections

PAwR uses new LL PDU types and HCI commands (`LE_Set_Periodic_Advertising_Parameters_v2`,
`LE_Periodic_Advertising_Response_Data`, etc.).

### Encrypted Advertising Data (EAD)

EAD uses **AES-128-CCM** to encrypt the advertising payload. Both the advertiser and
authorized scanners share a **Session Key** and **Initialization Vector** (derived from a
shared randomizer).

Unauthorized scanners see only an encrypted blob — they cannot decode the device's identity
or advertising data. This is important for:
- Privacy-sensitive applications (medical devices, personal tracking)
- Enterprise deployments where advertising data is proprietary

The AD type `0x31` (Encrypted Advertising Data) wraps the encrypted payload.
Key distribution uses existing SM procedures over a connection.

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
