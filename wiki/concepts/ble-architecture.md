# BLE Protocol Stack Architecture

**Last updated**: 2026-05-03
**Covers**: LE (Bluetooth Low Energy) stack from Core Spec 4.0 through 6.2

---

## Overview

The Bluetooth LE protocol stack is divided into a **Controller** (radio hardware + Link Layer)
and a **Host** (software stack), connected via the **HCI (Host Controller Interface)**.
This separation allows the host to run on an application processor while the controller runs
on a dedicated radio chip (or the two can be integrated into a single SoC).

---

## Layer-by-Layer Breakdown

```
┌──────────────────────────────────────────────────┐
│                  Application                     │
├──────────────────────────────────────────────────┤
│   GATT (Generic Attribute Profile)               │
├──────────────────────────────────────────────────┤
│   ATT (Attribute Protocol)                       │
├──────────────┬───────────────────────────────────┤
│   GAP        │   SM (Security Manager)           │
│ (Generic     │   - Pairing, bonding              │
│  Access      │   - Key distribution              │
│  Profile)    │   - LE Secure Connections         │
├──────────────┴───────────────────────────────────┤
│   L2CAP (Logical Link Control & Adaptation)      │
│   - Multiplexing                                 │
│   - Segmentation & Reassembly                    │
│   - Credit-Based Flow Control (CoC)              │
│   - EATT bearers (5.2+)                          │
├──────────────────────────────────────────────────┤
│                   HCI                            │  ← host/controller boundary
├──────────────────────────────────────────────────┤
│   Link Layer (LL)                                │
│   - Advertising, scanning, initiating, connected │
│   - Packet format, CRC, whitening                │
│   - AFH (Adaptive Frequency Hopping)             │
│   - ISO channels (5.2+)                          │
│   - Channel Sounding (6.0+)                      │
├──────────────────────────────────────────────────┤
│   Physical Layer (PHY)                           │
│   - LE 1M PHY (4.0+)                             │
│   - LE 2M PHY (5.0+)                             │
│   - LE Coded PHY S=2 / S=8 (5.0+)                │
└──────────────────────────────────────────────────┘
```

---

## Physical Layer (PHY)

Operates in the **2.4 GHz ISM band** using **Gaussian Frequency Shift Keying (GFSK)**.

| PHY | Modulation | Symbol Rate | FEC | Effective Rate | Since |
|-----|-----------|------------|-----|----------------|-------|
| LE 1M | GFSK | 1 Msym/s | None | ~1 Mbps | 4.0 |
| LE 2M | GFSK | 2 Msym/s | None | ~2 Mbps | 5.0 |
| LE Coded S=2 | GFSK | 1 Msym/s | Rate 1/2 | ~500 kbps | 5.0 |
| LE Coded S=8 | GFSK | 1 Msym/s | Rate 1/8 | ~125 kbps | 5.0 |

**Channels**: 40 channels, 2 MHz spacing (2402–2480 MHz)
- Channels 37, 38, 39: **Primary advertising channels** (spread across band to avoid Wi-Fi overlap)
- Channels 0–36: **Data channels** (37 channels for connections and secondary advertising)

**LE 2M 2BT PHY (6.0+)**: Uncoded at 2 Mb/s with BT=2.0 Gaussian filter — used exclusively
for Channel Sounding tone and RTT packet exchanges. Not usable for general data.
[Core 6.0, Vol 6, Part A, §3.1.2]

---

## Link Layer (LL)

The Link Layer implements the BLE state machine and all packet-level operations.

### LL State Machine

```
Standby ──→ Advertising ──→ Connected ──→ Channel Sounding (6.0+, over connection)
   │              │               │
   └──→ Scanning  │               │
   │              └──→ Initiating─┘
   └──→ Synchronizing (Periodic Advertising Sync / PAwR, 5.0+/5.4+)
   └──→ Isochronous Broadcasting (5.2+)
```

### Key LL Concepts

**Advertising PDU types:**
- `ADV_IND`: Connectable, scannable, undirected (legacy)
- `ADV_NONCONN_IND`: Non-connectable, non-scannable, undirected (legacy beacons)
- `ADV_EXT_IND`: Extended advertising header (5.0+, points to aux packets)
- `AUX_ADV_IND`, `AUX_SYNC_IND`, `AUX_CHAIN_IND`: Secondary channel packets (5.0+)

**Connection procedure:**
1. Peripheral advertises (`ADV_IND`)
2. Central sends `CONNECT_IND` with connection parameters
3. Both enter connected state; data flows on data channel using AFH

**Adaptive Frequency Hopping (AFH)**:
- 37 data channels, hopping pattern determined by `hop_increment` and `channel_map`
- Avoids interference (e.g., with Wi-Fi on 2.4 GHz)
- Channel map negotiated via `LL_CHANNEL_MAP_IND`

**Channel Sounding (CS, 6.0+)**:
CS runs over a dedicated **LE Channel Sounding physical channel** established over an existing
connection. A CS procedure contains CS events → CS subevents → CS steps. Steps use one of
four modes: calibration (0), RTT (1), PBR tones (2), or combined (3). CS operates on a
separate physical link alongside the ACL logical transport. [Core 6.0, Vol 1, Part A, §9;
Vol 6, Part B, §4.6.41; Vol 6, Part H]

**Decision-Based Advertising Filtering (DBAF, 6.0+)**:
Advertisers include decision data in `ADV_DECISION_IND` PDUs; scanners program decision
instructions into the controller via HCI. The controller evaluates PDUs against the instructions
and only wakes the host for matching advertisements. Requires LE Extended Advertising.
[Core 6.0, Vol 6, Part B, §4.6.43]

**Monitoring Advertisers (6.0+)**:
The controller tracks appearance/disappearance of specific advertiser addresses and notifies
the host on change, without requiring continuous host-level scanning. Operates independently
from the Filter Accept List; uses the Resolving List for RPA matching.
[Core 6.0, Vol 6, Part B, §4.6.45]

---

## HCI (Host Controller Interface)

HCI is the standardized API between host and controller.

### Physical Transports
- **UART (H4)**: Most common transport. A 1-byte type header distinguishes packet types: Command (0x01), ACL (0x02), SCO (0x03), Event (0x04), ISO (0x05). `[Core 6.2, Vol 4, Part A]`
- **UART (H5 / Three-Wire)**: SLIP-based transport with reliable framing, error detection, and retransmission.
- **USB**: High-throughput transport. Interface 0 carries Commands and Events; Bulk/Interrupt/Isochronous endpoints carry data.
  - **6.2 Update**: Normatively specifies dedicated USB endpoint configuration for LE Isochronous data (ISO data path over USB). `[Core 6.2, Vol 4, Part B]`

HCI message types:
- **Commands**: Host → Controller (e.g., `HCI_LE_Set_Advertising_Parameters`)
- **Events**: Controller → Host (e.g., `HCI_LE_Meta`, `HCI_Disconnection_Complete`)
- **ACL Data**: Bidirectional L2CAP data packets
- **ISO Data**: Bidirectional isochronous data packets (5.2+)

---

## L2CAP

L2CAP multiplexes multiple logical channels over one HCI ACL link.

Key channel types for LE:
| Channel | CID | Use |
|---------|-----|-----|
| ATT Bearer | 0x0004 | Classic ATT (single, since 4.0) |
| SM | 0x0006 | Security Manager protocol |
| LE Credit-Based CoC | Dynamic (0x0040+) | App-defined data channels |
| Enhanced ATT Bearer | Dynamic (EATT, 5.2+) | Parallel GATT transactions |

---

## ATT (Attribute Protocol)

ATT implements a **client-server model** for structured data access.

- **Server**: Holds a set of **Attributes** (key-value pairs with a 16-bit handle)
- **Client**: Reads/writes attributes using ATT PDUs
- Attribute = {Handle, Type (UUID), Value, Permissions}

ATT PDUs: `ATT_READ_REQ/RSP`, `ATT_WRITE_REQ/RSP`, `ATT_HANDLE_VALUE_NTF`, `ATT_HANDLE_VALUE_IND`, etc.

**EATT (Enhanced ATT, 5.2+)**: Multiple parallel ATT bearers over L2CAP CoC (PSM 0x0027).
Each bearer is an independent ATT channel — enables concurrent reads, writes, notifications.

---

## GATT (Generic Attribute Profile)

GATT defines a **structured hierarchy** of attributes:

```
Service (UUID e.g., Heart Rate Service 0x180D)
  └── Characteristic (UUID e.g., Heart Rate Measurement 0x2A37)
        ├── Value (actual data bytes)
        └── Descriptor (e.g., Client Characteristic Configuration Descriptor 0x2902)
```

GATT operations:
- **Read**: Client reads characteristic value
- **Write**: Client writes characteristic value (with/without response)
- **Notify**: Server pushes characteristic value (no ACK)
- **Indicate**: Server pushes characteristic value (with ACK)

**Service Discovery**: Client uses `ATT_READ_BY_GROUP_TYPE_REQ` to discover services,
then `ATT_READ_BY_TYPE_REQ` for characteristics. Cached after discovery (5.1+ with DB Hash).

---

## GAP (Generic Access Profile)

GAP defines **device roles**, **modes**, and **procedures** for discovery and connection.

LE roles:
- **Broadcaster**: Only advertises (beacons, sensors)
- **Observer**: Only scans (listeners)
- **Peripheral**: Advertises and accepts connections
- **Central**: Scans and initiates connections

Key GAP procedures:
- **Discovery**: Device discovery (active/passive scan) + name/service discovery
- **Connection Establishment**: Central initiates; peripheral accepts
- **Bonding**: Pairing + key storage for future reconnections

---

## SM (Security Manager)

SM handles **pairing** (key establishment) and **bonding** (key storage).

Pairing methods:
| Method | User interaction | Security |
|--------|-----------------|---------|
| Just Works | None | No MITM protection |
| Passkey Entry | PIN on one/both devices | MITM protection |
| Numeric Comparison | Verify 6-digit number on both | MITM protection |
| OOB (Out of Band) | Exchange keys via NFC/QR | MITM + device auth |

**LE Secure Connections (4.2+)**: Elliptic Curve Diffie-Hellman (P-256) for key exchange.
Provides protection against passive eavesdropping and MITM attacks.

Keys distributed after pairing: LTK (Long Term Key), IRK (Identity Resolving Key), CSRK (Signing Key).

See also: [Security](security.md) for full details.

---

## Version History of Key Stack Components

| Feature | Introduced | Version |
|---------|-----------|---------|
| BLE stack (LE 1M, 37 channels, ATT/GATT/GAP/SM) | 4.0 | 2010 |
| LE Secure Connections (P-256 ECDH) | 4.2 | 2014 |
| 251-byte LE Data PDU | 4.2 | 2014 |
| LE 2M PHY, LE Coded PHY | 5.0 | 2016 |
| Extended / Periodic Advertising | 5.0 | 2016 |
| Direction Finding (CTE, IQ Sampling) | 5.1 | 2019 |
| GATT Database Hash / Caching | 5.1 | 2019 |
| ISO Channels (CIS, BIS), EATT, Power Control | 5.2 | 2019 |
| Connection Subrating | 5.3/5.4 | 2021/2023 |
| PAwR, EAD | 5.4 | 2023 |
| Channel Sounding, DBAF, Monitoring Advertisers | 6.0 | 2024 |
| Randomized RPA Updates (v2 privacy hardening) | 6.1 | 2025 |
| Shorter Connection Intervals (375 µs), LE UTP, CS Amplitude Resilience | 6.2 | 2025 |
