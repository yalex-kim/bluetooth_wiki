# Bluetooth Security

**Last updated**: 2026-05-02
**Covers**: Security mechanisms across Core Spec 4.0–6.0

---

## Overview

Bluetooth security covers four areas:
1. **Authentication**: Verifying device identity
2. **Authorization**: Controlling access to services
3. **Confidentiality**: Encrypting data in transit
4. **Privacy**: Preventing device tracking

Each has evolved significantly from Classic Bluetooth through BLE 6.0.

---

## LE Security Modes

The Security Manager (SM) defines **Security Modes** and **Levels**:

### LE Security Mode 1 (Encryption required)
| Level | Requirement |
|-------|-------------|
| 1 | No security (open) |
| 2 | Unauthenticated pairing with encryption |
| 3 | Authenticated pairing with encryption |
| 4 | Authenticated LE Secure Connections pairing with 128-bit strength encryption |

### LE Security Mode 2 (Data signing only)
| Level | Requirement |
|-------|-------------|
| 1 | Unauthenticated pairing with data signing |
| 2 | Authenticated pairing with data signing |

### LE Security Mode 3 (Broadcast, added in 5.4)
| Level | Requirement |
|-------|-------------|
| 1 | No security |
| 2 | Use of Broadcast Code with authenticated encryption |
| 3 | Use of Broadcast Code with Bluetooth LE Secure Connections pairing |

---

## Pairing

Pairing establishes a shared secret between two devices.
BLE uses **Security Manager Protocol (SMP)** over L2CAP CID 0x0006.

### Pairing Methods

| Method | IO Capability Required | MITM Protection | Since |
|--------|----------------------|-----------------|-------|
| Just Works | None | No | 4.0 |
| Passkey Entry | Display or keyboard | Yes | 4.0 |
| Numeric Comparison | Display on both | Yes | 4.2 (LE SC) |
| OOB (Out of Band) | NFC, QR, or manual | Depends on OOB channel | 4.0 |

### IO Capability Matrix

The pairing method is determined by the combination of both devices' IO capabilities:

| Initiator \ Responder | DisplayOnly | DisplayYesNo | KeyboardOnly | NoInputNoOutput | KeyboardDisplay |
|----------------------|------------|-------------|-------------|----------------|----------------|
| DisplayOnly | Just Works | Just Works | Passkey Entry | Just Works | Passkey Entry |
| DisplayYesNo | Just Works | Numeric Comp | Passkey Entry | Just Works | Numeric Comp |
| KeyboardOnly | Passkey Entry | Passkey Entry | Passkey Entry | Just Works | Passkey Entry |
| NoInputNoOutput | Just Works | Just Works | Just Works | Just Works | Just Works |
| KeyboardDisplay | Passkey Entry | Numeric Comp | Passkey Entry | Just Works | Numeric Comp |

### Legacy Pairing (4.0–4.1) vs. LE Secure Connections (4.2+)

**Legacy Pairing**:
- Uses STK (Short Term Key) derived from TK (Temporary Key)
- TK is the shared secret from the pairing method (e.g., 6-digit passkey)
- Vulnerable to passive eavesdropping if TK is predictable (Just Works TK = 0)
- Uses AES-128 for key generation

**LE Secure Connections (4.2+)**:
- Uses **ECDH (Elliptic Curve Diffie-Hellman)** with P-256 curve
- Both devices generate ephemeral key pairs; exchange public keys
- Shared DHKey → LTK derivation
- **Immune to passive eavesdropping** (DHKey not derivable from observed public keys)
- **Numeric Comparison** method added (requires displays on both devices for MITM protection)
- Provides 128-bit security

---

## Bonding

**Bonding** = pairing + persistent key storage for future reconnections.

After bonding, devices store:
| Key | Description |
|-----|-------------|
| LTK (Long Term Key) | Used to re-encrypt future connections without re-pairing |
| IRK (Identity Resolving Key) | Resolves random private addresses to a known device |
| CSRK (Connection Signature Resolving Key) | Verifies signed data without encryption |
| BD_ADDR / Identity Address | For address resolution |

On reconnection, the **LTK** is used to encrypt the link via `HCI_LE_Long_Term_Key_Request`.

---

## Privacy (Address Randomization)

Bluetooth LE devices can advertise with **random addresses** to prevent tracking.

### Address Types

| Type | Description | Since |
|------|-------------|-------|
| Public | Fixed IEEE-assigned MAC | 4.0 |
| Static Random | Fixed random (changes on power cycle) | 4.0 |
| Non-Resolvable Private (NRPA) | Random, changes periodically, no bonding | 4.0 |
| Resolvable Private Address (RPA) | Derived from IRK; bonded peers can resolve it | 4.0 |

### Resolvable Private Addresses (RPA)

RPA = hash(IRK, Prand) where Prand is a 24-bit random number.
The RPA changes periodically (typically every 15 minutes, configurable).
Only devices with the shared IRK can resolve the RPA to the device's identity.

**Enhanced Privacy (4.2+)**: Controller-based address resolution.
The controller resolves RPAs internally without waking the host — more efficient.

---

## Link-Layer Encryption

Once pairing is complete and a connection is established:
1. Central sends `LL_ENC_REQ` with random value and EDIV
2. Peripheral uses LTK + EDIV + random → session key (SK)
3. Both devices enable AES-128-CCM encryption on the link
4. All L2CAP data is encrypted and integrity-protected (MIC)

**Key size**: 7–16 bytes, negotiated during pairing (Core Spec recommends 16 bytes).

---

## Encrypted Advertising Data (EAD, 5.4+)

Advertising payloads are normally unencrypted. EAD adds confidentiality:

- Advertiser encrypts AD structures using **AES-128-CCM**
- **Session Key** and **IV** derived from shared secret (exchanged over SM in a prior connection)
- **Randomizer** (3 bytes) included in advertising PDU to derive per-packet IV
- AD type `0x31` wraps the encrypted payload
- Unauthorized scanners cannot read the payload

Use cases: medical devices, employee badges, enterprise beacons.

See: [Core Spec 5.4](../versions/core-spec-5.4.md), [diff-5.3-to-5.4](../version-diff/diff-5.3-to-5.4.md)

---

## Channel Sounding Security (6.0+)

Channel Sounding includes built-in **anti-relay attack** protections:

- CS procedures exchange random nonces during ranging
- Relay attacks introduce measurable signal path delays
- Both sides verify timing consistency — inconsistency = relay detected
- Critical for **PACS (Physical Access Control)**: car keys, door locks

See: [Core Spec 6.0](../versions/core-spec-6.0.md)

---

## BR/EDR Security (Legacy vs. SSP)

### Legacy Pairing (pre-2.1)
- PIN-based (4–16 digits or alphanumeric)
- Vulnerable to brute force (4-digit PIN = 10,000 combinations)
- E0 stream cipher for encryption

### Secure Simple Pairing (SSP, 2.1+)
- ECDH key exchange (P-192)
- Methods: Just Works, Passkey Entry, Numeric Comparison, OOB
- Resists passive eavesdropping and MITM (with correct method)

### Secure Connections (4.1+)
- Upgraded to P-256 ECDH for BR/EDR
- AES-CCM encryption (replaces E0)
- Same security level as LE Secure Connections

---

## Common Security Pitfalls

| Pitfall | Risk | Mitigation |
|---------|------|-----------|
| Just Works pairing | No MITM protection | Use Passkey/Numeric Comparison when possible |
| Fixed static random address | Device trackable | Use RPA with periodic rotation |
| Short encryption key (< 16 bytes) | Brute-force vulnerable | Always negotiate 128-bit keys |
| Not using LE Secure Connections | Legacy pairing vulnerable to eavesdropping | Require LE SC (Security Mode 1, Level 4) |
| Unencrypted advertising | Payload visible to all scanners | Use EAD (5.4+) for sensitive payload data |
| No authentication on GATT characteristics | Unauthorized reads/writes | Set appropriate Permissions on attributes |
