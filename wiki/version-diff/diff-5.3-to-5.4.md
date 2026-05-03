# Diff: Bluetooth Core Spec 5.3 → 5.4

**From**: [Core Spec 5.3](../versions/core-spec-5.3.md) (withdrawn)
**To**: [Core Spec 5.4](../versions/core-spec-5.4.md) (2023-02-02)

> 5.3 was withdrawn by Bluetooth SIG. 5.4 supersedes it and includes all 5.3 features.

---

## At a Glance

5.4's two major additions target completely different markets. **PAwR (Periodic Advertising with
Responses)** enables scalable coordinator-to-device communication without connections —
directly enabling Bluetooth ESL (Electronic Shelf Labels) at retail scale.
**EAD (Encrypted Advertising Data)** adds privacy-preserving encryption to advertising payloads
for medical, enterprise, and access control applications.

---

## Added (net new in 5.4 beyond 5.3)

| What | Description | Reference |
|------|-------------|-----------|
| **Periodic Advertising with Responses (PAwR)** | Bidirectional periodic advertising with subevent + response slot structure; uses AUX_SYNC_SUBEVENT_IND/RSP PDUs | [Core 5.4, Vol 6, Part B, §4.6.38–4.6.39] |
| **PAwR Subevent structure** | Up to 0x80 (128) subevents per PA event; up to 0xFF (255) response slots per subevent | [Core 5.4, Vol 4, Part E — HCI_LE_Set_Periodic_Advertising_Parameters_v2] |
| **LL_PERIODIC_SYNC_WR_IND** | New LL PDU for transferring PAwR sync info to a connected peer (WR = With Responses) | [Core 5.4, Vol 6, Part B, §4.6.38](../../sources/specs/5.4/Core_v5.4.md#L60283) |
| **AUX_SYNC_SUBEVENT_IND / RSP** | New advertising PDU types for PAwR subevent broadcast and device responses | [Core 5.4, Vol 6, Part B, §2](../../sources/specs/5.4/Core_v5.4.md#L56754) |
| **Encrypted Advertising Data (EAD)** | Pre-shared session key encrypts advertising payload; prevents fingerprinting of devices via advertising data content | [Core 5.4, Vol 1, Part A, §5.4.6; Vol 3, Part C, §10.10] |
| **LE GATT Security Levels Characteristic** | New GATT characteristic (UUID 0x2BF5) exposing highest LE security requirement of GATT server | [Core 5.4, Vol 3, Part C, §12.7](../../sources/specs/5.4/Core_v5.4.md#L29050) |
| **Advertising Coding Selection** | Host selects S=2 or S=8 data coding for LE Coded PHY advertising | [Core 5.4, Vol 6, Part B, §4.6.37](../../sources/specs/5.4/Core_v5.4.md#L60276) |

---

## Modified (changes from 5.3 baseline)

| What | Change |
|------|--------|
| **Periodic Advertising** | Extended with subevent + response slot mechanism; PAwR is a new logical transport type alongside periodic advertising |
| **HCI LE Meta events** | New: `HCI_LE_Periodic_Advertising_Subevent_Data_Request` (controller requests subevent data from host), `HCI_LE_Periodic_Advertising_Response_Report` (reports device responses) |
| **HCI commands** | New: `HCI_LE_Set_Periodic_Advertising_Parameters_v2`, `HCI_LE_Set_Periodic_Advertising_Subevent_Data`, `HCI_LE_Set_Periodic_Advertising_Response_Data`, `HCI_LE_Set_Periodic_Sync_Subevent` |
| **HCI_LE_Periodic_Advertising_Report event** | Extended: new `Subevent` parameter (0xFF = no subevents); new `Data_Status` value 0x02 (failed to receive AUX_SYNC_SUBEVENT_IND) |
| **LE Features (Vol 6, Part B)** | New bits: Bit 40 Advertising Coding Selection; Bit 41 Advertising Coding Selection (Host Support); Bit 43 PAwR Advertiser; Bit 44 PAwR Scanner |

---

## Deprecated / Removed

- 5.3 withdrawn (administrative action — all 5.3 features preserved in 5.4)

---

## Migration Guide

### Electronic Shelf Label (ESL) / PAwR deployments

PAwR is the foundation of the Bluetooth ESL Profile:

```
ESL Access Point (PAwR Advertiser)
  ↓ Periodic Advertising Subevent (broadcast command/data)
ESL Tag (PAwR Scanner, synchronized to specific subevent)
  ↑ Response slot (acknowledgment / sensor data)
```

Key implementation considerations:
1. **Assign subevents and response slots** to each device during provisioning
2. **Tags only wake for their subevent** — critical for coin-cell battery lifetime
3. **ESL Profile** builds on top of PAwR: implements tag commands, image transfer, etc.
4. **Auracast + PAwR**: can coexist — BIS for audio, PAwR for control signaling to receivers

### Encrypted Advertising Data (EAD)

EAD is for scenarios where advertising content must be confidential:
[Core 5.4, Vol 1, Part A, §5.4.6; Vol 3, Part C, §10.10]

1. Establish a connection first (for Security Manager key distribution)
2. Exchange session key (SK) and nonce components via SM procedures
3. Advertiser encrypts payload; the pre-shared session key is communicated only to
   authorized peer devices
4. Encrypted payload uses the AD type **Encrypted Data** to wrap the advertising data
5. Unauthorized scanners receive only the encrypted blob — unreadable without the session key

**Note**: EAD protects payload privacy, not device identity. EAD is a **Type 4 feature**
(Host-only; does not involve the Controller directly). Address randomization (from 4.2)
is still required for full device identity privacy. [Core 5.4, Vol 0, Part D, Table 4.2]
