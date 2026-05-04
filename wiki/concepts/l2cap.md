# L2CAP (Logical Link Control and Adaptation Protocol)

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> L2CAP sits directly above the Link Layer (LE) or Baseband (BR/EDR) and provides **channel multiplexing**, **segmentation/reassembly**, and **flow control** for all higher-layer protocols. ATT, SMP, and GATT all ride on top of L2CAP channels.

---

## Overview

```
Application / Profiles
     └── GATT (Vol 3, Part G)
          └── ATT  (Vol 3, Part F)   ── L2CAP CID 0x0004 (classic ATT bearer)
                                     └─ L2CAP CoC, PSM 0x0027 (EATT bearer, 5.2+)
     └── SMP  (Vol 3, Part H)        ── L2CAP CID 0x0006
     └── GAP signaling               ── L2CAP CID 0x0005 (LE signaling channel)
     └── Application CoC channels    ── dynamic PSM 0x0080–0x00FF
             └── L2CAP (Vol 3, Part A)
                      └── HCI ACL Data
                               └── Link Layer (LE) / Baseband (BR/EDR)
```

L2CAP PDUs are carried inside HCI ACL Data packets (handle + packet boundary + data length header). For LE, all L2CAP traffic uses the ACL data path; ISO audio uses a separate HCI ISO path and bypasses L2CAP entirely.

[Core 6.2, Vol 3, Part A]

---

## Fixed Channels (Always Available)

Fixed channels require no setup — they are available immediately after an LE connection is established.

| CID | Channel | Direction | Used For |
|-----|---------|-----------|----------|
| `0x0004` | ATT | Bidirectional | Classic ATT bearer; one per LE connection; sequential request/response |
| `0x0005` | LE L2CAP Signaling | Bidirectional | L2CAP control messages (connection parameter update, CoC setup, credit grants) |
| `0x0006` | SMP (LE) | Bidirectional | Security Manager Protocol (SMP) — pairing, key distribution |
| `0x0007` | SMP (BR/EDR) | Bidirectional | BR/EDR Security Manager (present on BR/EDR connections only) |

> For BR/EDR there is also CID 0x0001 (BR/EDR signaling) and 0x0002 (connectionless reception). These are not present on LE links.

---

## L2CAP Signaling Channel (CID 0x0005)

All L2CAP control messages on LE connections are sent on the **Signaling Channel (CID 0x0005)**. Each signal has a code byte, identifier (for request/response matching), and payload.

### Key Signal Codes

| Code | Name | Direction | Notes |
|------|------|-----------|-------|
| `0x01` | Command Reject | Both | Sent when a command is not understood or has an invalid identifier |
| `0x06` | Disconnection Request | Either | Tear down a dynamic CoC channel |
| `0x07` | Disconnection Response | Either | Acknowledge disconnection |
| `0x12` | Connection Parameter Update Request | Peripheral → Central | Peripheral-initiated connection parameter update (not HCI — pure L2CAP) |
| `0x13` | Connection Parameter Update Response | Central → Peripheral | Result 0x0000 = accepted, 0x0001 = rejected |
| `0x14` | LE Credit Based Connection Request | Either | Open a single LE CoC channel (4.2+) |
| `0x15` | LE Credit Based Connection Response | Either | — |
| `0x16` | Flow Control Credit Indication | Either | Grant additional credits on an existing channel |
| `0x17` | Credit Based Connection Request | Either | Open up to 5 ECBFC channels in one request (5.2+) |
| `0x18` | Credit Based Connection Response | Either | — |
| `0x19` | Credit Based Reconfigure Request | Either | Adjust MTU/MPS on existing ECBFC channels (5.2+) |
| `0x1A` | Credit Based Reconfigure Response | Either | — |

[Core 6.2, Vol 3, Part A, §4]

---

## LE Credit-Based Connection (CoC, 4.2+)

LE CoC (Connection-Oriented Channel) allows application data to flow over a **dynamic L2CAP channel** with credit-based flow control. This is the mechanism EATT and custom application protocols use.

### Credit Model

Each side grants the other a number of **credits** — each credit allows the peer to send one L2CAP PDU (called an **LE-frame** or **K-frame**). When credits run out, the sender must wait for a `Flow Control Credit Indication (0x16)` granting more.

```
Initiator                          Responder
    │                                  │
    │── LE_CREDIT_BASED_CONN_REQ ─────►│   (PSM, SCID, MTU, MPS, Initial_Credits)
    │◄── LE_CREDIT_BASED_CONN_RSP ─────│   (DCID, MTU, MPS, Initial_Credits, Result)
    │                                  │
    │── K-frame (data PDU) ───────────►│   [uses 1 credit from Responder's grant]
    │── K-frame ───────────────────────►│
    │ ... (until Responder's credits = 0)
    │◄── FLOW_CONTROL_CREDIT_IND ──────│   (SCID, Credits = N)   [grants N more]
    │── K-frame ───────────────────────►│
```

### Key Parameters

| Parameter | Range | Description |
|-----------|-------|-------------|
| PSM | 0x0001–0x007F (fixed), 0x0080–0x00FF (dynamic) | Protocol Service Multiplexer identifying the protocol |
| MTU | ≥ 23 bytes | Maximum SDU size the receiver can accept |
| MPS | ≥ 23 bytes, ≤ controller payload | Maximum PDU payload per L2CAP packet |
| Initial_Credits | 0–65535 | Credits granted at channel establishment |
| SCID / DCID | 0x0040–0x007F | Source/Destination CID, dynamically assigned |

**MTU vs. MPS**: MTU is the maximum **SDU** (application data unit) size. MPS is the maximum **PDU** payload size (per L2CAP frame). Large SDUs are segmented into multiple PDUs each ≤ MPS; the first PDU includes a 2-byte SDU_Length field. MPS ≤ (controller ATT_MTU - 4 bytes L2CAP header).

[Core 6.2, Vol 3, Part A, §3.4]

---

## Enhanced Credit-Based Flow Control (ECBFC, 5.2+)

5.2 introduced **Enhanced Credit-Based Flow Control** channels to support EATT. ECBFC improves on LE CoC:

- A **single** `Credit_Based_Connection_Request (0x17)` can request **up to 5 channels** simultaneously (all for the same PSM).
- All channels share the same MTU and MPS parameters.
- Channel MTU/MPS can be **reconfigured after establishment** via `Credit_Based_Reconfigure_Request (0x19)`.
- Used by EATT (PSM `0x0027`) to create multiple parallel ATT bearers.

### EATT Channel Setup Flow

```
Client                              Server
    │                                  │
    │── Credit_Based_Conn_Req ────────►│  (PSM=0x0027, SCIDs[0..4], MTU=247, MPS=247, Credits=N)
    │◄── Credit_Based_Conn_Rsp ────────│  (DCIDs[0..4], MTU, MPS, Credits, Result[5])
    │                                  │
    │ [Up to 5 parallel ATT bearers]   │
    │── ATT_Read_Req on bearer 0 ─────►│  [concurrent with bearer 1 operations]
    │── ATT_Write_Req on bearer 1 ────►│
    ...
```

An EATT bearer uses ECBFC channel semantics: the ATT PDU is the SDU, segmented per MPS. The minimum MTU for EATT is **64 bytes** (vs. 23 bytes for classic ATT). [Core 6.2, Vol 3, Part F, §3.2.5]

---

## Known PSM Assignments

| PSM | Protocol | Transport |
|-----|----------|-----------|
| `0x0001` | SDP | BR/EDR only |
| `0x0003` | RFCOMM (SPP, HFP, etc.) | BR/EDR only |
| `0x000F` | AVDTP (A2DP audio) | BR/EDR only |
| `0x0017` | AVCTP (AVRCP) | BR/EDR only |
| `0x0027` | EATT (Enhanced ATT bearer) | LE (5.2+) |
| `0x0080`–`0x00FF` | Dynamic (vendor / application) | LE (odd values only) |

Dynamic PSMs are negotiated out-of-band — typically the server exposes the PSM value via a GATT characteristic and the client reads it before initiating a CoC connection. [Core 6.2, Vol 3, Part A, §4.2]

---

## Segmentation and Reassembly (SAR)

L2CAP PDU sizes are constrained by the HCI buffer size and the LE data PDU size (max 251 bytes payload with DLE). For large SDUs:

1. First K-frame: 2-byte `SDU_Length` field + first fragment (up to MPS − 2 bytes of payload)
2. Subsequent K-frames: payload only (up to MPS bytes each)
3. Receiver reassembles all fragments into the original SDU

No explicit fragment count — reassembly is complete when cumulative bytes equal `SDU_Length`.

---

## L2CAP and BR/EDR

BR/EDR uses a different channel model:
- **Basic Mode** (legacy, pre-3.0): no flow control, no segmentation beyond HCI MTU
- **Enhanced Retransmission Mode (ERTM)**: retransmission + flow control, used by AVDTP
- **Streaming Mode**: no retransmission, flow control only (used by A2DP audio streaming)
- **BR/EDR signaling (CID 0x0001)**: equivalent of LE 0x0005; carries connection setup for BR/EDR dynamic channels

These modes are negotiated via `L2CAP_CONFIGURATION_REQ` signals on the BR/EDR signaling channel.

[Core 6.2, Vol 3, Part A, §6]

---

## Version History

| Version | L2CAP Change |
|---------|-------------|
| 4.0 | LE fixed channels introduced (ATT CID 0x0004, Signaling 0x0005, SMP 0x0006) |
| 4.2 | LE Credit-Based Connection (CoC) — dynamic channels over PSM 0x0040–0x00FF; 251-byte data PDU with DLE |
| 5.2 | Enhanced Credit-Based Flow Control (ECBFC) — multi-channel request, MTU/MPS reconfiguration; EATT PSM 0x0027 |

---

## See Also

- [ATT and GATT](att-gatt.md) — ATT fixed channel (CID 0x0004) and EATT bearers (PSM 0x0027)
- [Security](security.md) — SMP fixed channel (CID 0x0006) and pairing flows
- [Connection Management](connection-management.md) — L2CAP Signaling channel (CID 0x0005) for connection parameter updates
- [HCI Sequences](../reference/hci-sequences.md) — Section 8b: Peripheral-initiated parameter update via L2CAP signaling

---

*Source: [Core 6.2, Vol 3, Part A (L2CAP)](../../sources/specs/6.2/Core_v6.2.md)*
