# Bluetooth Security

**Last updated**: 2026-05-02
**Covers**: Security mechanisms across Core Spec 4.0–6.2

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

### LE GATT Security Levels Characteristic (5.4+)
A GATT server can expose the **LE GATT Security Levels** characteristic (UUID `0x2BF5`) to advertise its security requirements to clients. This allows a client to determine the required security level (Mode 1 Level 1–4) before accessing services and initiate the appropriate pairing procedure proactively. [Core 5.4, Vol 3, Part C, §12.7](../../sources/specs/5.4/Core_v5.4.md)

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

### Security Errata and Hardening (6.2)
Core Spec 6.2 incorporates 12 security errata addressing vulnerabilities in the pairing and key generation procedures:
- **Passkey Entry Vulnerability (Errata 24489–24491)**: Fixed a design flaw that could leak Passkey information during pairing.
- **Minimum Encryption Key Size (Errata 26039)**: Enforces a minimum key size of **7 octets** on all encrypted LE connections, preventing low-entropy key attacks. [Core 6.2, Vol 3, Part H, §3.2]
- **RNG & DHKey Quality (Errata 24557, 24558)**: Strengthened random number generator (RNG) requirements and DHKey validation logic to harden against cryptographic attacks.

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
The controller resolves RPAs internally without waking the host — more efficient. [Core 4.2, Vol 6, Part B, §4.7.1]

**Active connections are unaffected**: When the RPA rotation timer fires, only future advertising and scanning use the new RPA. An existing connection retains the address used during setup for its entire lifetime. [Core 6.2, Vol 6, Part B, §4.7.2]

### Resolving List and Controller-Based Address Resolution (4.2+)

The **Resolving List** is a Controller-side database mapping each bonded peer's identity address to the IRK pair (peer's IRK for resolving incoming RPAs, local IRK for generating outgoing RPAs). When address resolution is enabled, the Controller resolves RPAs autonomously without waking the Host.

| HCI Command | Opcode | Purpose |
|-------------|--------|---------|
| `HCI_LE_Read_Resolving_List_Size` | 0x202A | Query maximum number of entries the Controller supports |
| `HCI_LE_Clear_Resolving_List` | 0x2029 | Remove all entries |
| `HCI_LE_Add_Device_To_Resolving_List` | 0x2027 | Add `{Address_Type, Address, Peer_IRK[16], Local_IRK[16]}` |
| `HCI_LE_Remove_Device_From_Resolving_List` | 0x2028 | Remove a specific entry |
| `HCI_LE_Read_Peer_Resolvable_Address` | 0x202B | Read the current RPA being used for a specific peer |
| `HCI_LE_Read_Local_Resolvable_Address` | 0x202C | Read the local RPA being used for a specific peer |
| `HCI_LE_Set_Address_Resolution_Enable` | 0x202D | Enable (0x01) or disable (0x00) Controller-based resolution |

> The Resolving List **cannot be modified** while address resolution is enabled and any scanner, advertiser, or initiator is active. Disable the scanner/advertiser, make changes, then re-enable.

[Core 6.2, Vol 4, Part E, §7.8.38–7.8.44; Vol 6, Part B, §4.7.1]

### Privacy Modes (4.2+)

Privacy Mode controls how strictly a device checks the address type of incoming advertising packets from a peer that is in the Resolving List.

| Mode | Value | Behavior |
|------|-------|----------|
| **Network Privacy Mode** (default) | `0x00` | Only accept advertising from a peer in the Resolving List if the peer uses an RPA. Identity address packets from that peer are rejected. |
| **Device Privacy Mode** | `0x01` | Accept advertising from a peer in the Resolving List regardless of address type (RPA or identity). More permissive; used when the peer cannot generate RPAs. |

Set per-peer via `HCI_LE_Set_Privacy_Mode` (0x204E):
- Parameters: `Peer_Identity_Address_Type`, `Peer_Identity_Address`, `Privacy_Mode`
- The peer must already be in the Resolving List.
- Default mode for all newly added entries is **Network Privacy Mode**.

[Core 6.2, Vol 4, Part E, §7.8.77; Vol 6, Part B, §4.7.4]

---

## Filter Accept List (4.0+)

The **Filter Accept List** (previously called "White List" in pre-5.3 specs) is a Controller-side list of device addresses. When a filter policy that references the FAL is active, the Controller only processes advertising, scan, or connection requests from addresses in this list — without waking the Host.

### HCI Management

| HCI Command | Opcode | Purpose |
|-------------|--------|---------|
| `HCI_LE_Read_Filter_Accept_List_Size` | 0x201F | Query maximum number of entries |
| `HCI_LE_Clear_Filter_Accept_List` | 0x2010 | Remove all entries |
| `HCI_LE_Add_Device_To_Filter_Accept_List` | 0x2011 | Add `{Address_Type, Address}` |
| `HCI_LE_Remove_Device_From_Filter_Accept_List` | 0x2012 | Remove a specific entry |

> The FAL **cannot be modified** while any scanning, advertising, or initiating procedure that references it is active. Returns `Command Disallowed (0x0C)` if modified while active.

### Filter Policies

The FAL is referenced via the `Scanning_Filter_Policy`, `Advertising_Filter_Policy`, and `Initiator_Filter_Policy` parameters:

**Scanning (`HCI_LE_Set_Scan_Parameters`, `HCI_LE_Set_Extended_Scan_Parameters`):**

| Policy | Value | Effect |
|--------|-------|--------|
| Accept all | `0x00` | Process all advertising PDUs (default) |
| FAL only | `0x01` | Process only PDUs from devices in the FAL |
| Undirected + directed to own | `0x02` | Undirected + directed PDUs targeting this device (ignores FAL) |
| FAL + directed to own | `0x03` | FAL devices + directed PDUs targeting this device |

**Advertising (`HCI_LE_Set_Advertising_Parameters`, extended equivalent):**

| Policy | Value | Effect |
|--------|-------|--------|
| Process all SCAN_REQ and CONNECT_IND | `0x00` | Default; accept from any scanner/initiator |
| FAL for SCAN_REQ only | `0x01` | Only respond to SCAN_REQ from FAL devices |
| FAL for CONNECT_IND only | `0x02` | Only accept connections from FAL devices |
| FAL for both | `0x03` | Restrict both scan responses and connections to FAL devices |

**Connection Initiation (`HCI_LE_Create_Connection`, `HCI_LE_Extended_Create_Connection`):**

| Policy | Value | Effect |
|--------|-------|--------|
| Use Peer_Address | `0x00` | Connect to the specific address in the command (default) |
| Use FAL | `0x01` | Connect to any device in the FAL; `Peer_Address` field is ignored |

### FAL and RPA Interaction

The FAL matches **identity addresses**, not RPAs. If a bonded peer uses RPAs, the Controller must resolve the RPA to its identity address (via the Resolving List) before the FAL check occurs. This requires:
1. The peer's IRK in the Resolving List.
2. Address resolution enabled (`HCI_LE_Set_Address_Resolution_Enable = 0x01`).
3. The peer's identity address in the FAL.

Devices using RPAs with **unknown IRK** can be added to the FAL using `Address_Type = 0xFF` (anonymous entry — matches any RPA), but this effectively disables address filtering for that slot.

[Core 6.2, Vol 4, Part E, §7.8.15–7.8.17; Vol 6, Part B, §4.3.1]

---

## Link-Layer Encryption

Once pairing is complete and a connection is established:
1. Central sends `LL_ENC_REQ` with random value and EDIV
2. Peripheral uses LTK + EDIV + random → session key (SK)
3. Both devices enable AES-128-CCM encryption on the link
4. All L2CAP data is encrypted and integrity-protected (MIC)

**Key size**: 7–16 bytes, negotiated during pairing (Core Spec recommends 16 bytes).

[Core 6.2, Vol 3, Part H, §2.2; Vol 6, Part B, §5.1.3]

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

Channel Sounding (CS) provides multi-layer protection against relay attacks: [Core 6.0, Vol 6, Part H, §4.2]

- CS procedures exchange random nonces during ranging
- Relay attacks introduce measurable signal path delays
- Both sides verify timing consistency — inconsistency = relay detected
- **Amplitude-based Attack Resilience (6.2)**: Core Spec 6.2 added the ability to detect sophisticated relay devices that manipulate signal timing or phase, by analyzing amplitude (signal strength) variations across the measurement. [Core 6.2, Vol 6, Part H, §5]
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

---

*Source: [Core 6.2, Vol 3, Part H (Security Manager); Vol 6, Part B §4.7, §5.1](../../sources/specs/6.2/Core_v6.2.md)*
