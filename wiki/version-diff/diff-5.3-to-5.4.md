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
| **Periodic Advertising with Responses (PAwR)** | Response slots in periodic advertising; coordinator-to-many bidirectional | Vol 6, Part B, §4.4.2.7 |
| **PAwR Subevent structure** | Up to 128 subevents × 128 response slots = 16,384 devices per coordinator | Vol 6, Part B |
| **LL_PERIODIC_SYNC_WITH_RESPONSE** | New LL PDU for PAwR synchronization | Vol 6, Part B |
| **Encrypted Advertising Data (EAD)** | AES-128-CCM encryption of advertising payload (AD type 0x31) | Vol 3, Part C, §11.8 |
| **EAD Key Distribution** | Session key and IV derivation over SM for shared advertising encryption | Vol 3, Part H |
| **LE GATT Security Levels** | New GATT characteristic to expose current LE security level | Vol 3, Part G |
| **AD Types for PAwR** | New Advertising Data types for ESL profile coordination | Bluetooth Assigned Numbers |

---

## Modified (changes from 5.3 baseline)

| What | Change |
|------|--------|
| **Periodic Advertising** | Extended with response slot mechanism (PAwR is a superset) |
| **HCI LE Meta events** | New subevents: LE_Periodic_Advertising_Subevent_Data_Request, LE_Periodic_Advertising_Response |
| **HCI commands** | LE_Set_Periodic_Advertising_Parameters_v2, LE_Set_Periodic_Advertising_Subevent_Data, LE_Set_Periodic_Advertising_Response_Data |
| **SM (Security Manager)** | Key distribution extended for EAD session key / IV |
| **LE Features** | New bits: PAwR Advertiser, PAwR Scanner, Encrypted Advertising Data |

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
1. Establish a connection first (for SM key distribution)
2. Exchange Session Key (SK) and IV via SM procedures
3. Advertiser encrypts payload with AES-128-CCM using SK + IV + randomizer
4. Randomizer is included in the advertising PDU (so authorized scanners can decrypt)
5. Unauthorized scanners receive AD type 0x31 blob — unreadable without SK

**Note**: EAD protects payload privacy, not device identity. Address randomization (from 4.2)
is still required for full device privacy.
