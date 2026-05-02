# Classic Bluetooth (BR/EDR)

**Last updated**: 2026-05-02
**Covers**: BR/EDR as defined in Bluetooth Core Spec (all versions)

---

## Overview

**BR/EDR** (Basic Rate / Enhanced Data Rate) is the original Bluetooth radio technology,
introduced in Core Spec 1.0 (1998). Despite the marketing focus on BLE since 2010,
BR/EDR remains widely deployed for:
- **Wireless audio**: A2DP (stereo music), HFP (hands-free calling), HSP (headset)
- **Human Interface Devices**: HID profile (keyboards, mice, gamepads)
- **Serial Port**: SPP (serial port emulation)
- **File Transfer**: OPP, FTP profiles

---

## Radio Technology

- **Frequency**: 2.4 GHz ISM band (2402–2480 MHz)
- **Channeling**: 79 channels, 1 MHz spacing
- **Access method**: Frequency Hopping Spread Spectrum (FHSS): 1600 hops/second
- **Range**: Typically 10–100 m (Class 1: 100 mW / Class 2: 2.5 mW / Class 3: 1 mW)

### Data Rates

| Mode | Rate | Introduced |
|------|------|-----------|
| BR (Basic Rate) | 1 Mbps | 1.0 |
| EDR 2 Mbps | 2 Mbps | 2.0+EDR |
| EDR 3 Mbps | 3 Mbps | 2.0+EDR |

BR uses GFSK modulation. EDR uses DQPSK (2 Mbps) and 8DPSK (3 Mbps).

---

## Network Topology

### Piconet
- 1 **Primary** (formerly "master") + up to 7 active **Secondaries** (formerly "slaves")
- Primary controls channel hopping sequence and timing
- All secondaries synchronize to primary's clock
- Up to 255 additional **parked** secondaries (inactive but synchronized)

### Scatternet
- A device can be Primary in one piconet and Secondary in another
- Enables multi-hop networking (rarely used in practice)

---

## BR/EDR Protocol Stack

```
┌──────────────────────────────────────────────┐
│           Application Profiles               │
│   A2DP  │  HFP  │  HID  │  SPP  │  OPP     │
├──────────┴───────┴───────┴───────┴───────────┤
│  AVDTP  │  RFCOMM / SDP                      │
├──────────┴────────────────────────────────────┤
│   L2CAP                                       │
├───────────────────────────────────────────────┤
│   HCI                                         │
├───────────────────────────────────────────────┤
│   LMP (Link Manager Protocol)                 │
├───────────────────────────────────────────────┤
│   Baseband / Link Controller                  │
├───────────────────────────────────────────────┤
│   Radio (BR/EDR PHY)                          │
└───────────────────────────────────────────────┘
```

### Key Protocol Layers

**Baseband**: Packet format, frequency hopping, link establishment, power control.
Defines two link types:
- **ACL** (Asynchronous Connection-Less): Best-effort data; used for all non-audio traffic
- **SCO/eSCO** (Synchronous Connection-Oriented): Circuit-switched audio; reserved bandwidth

**LMP (Link Manager Protocol)**: Authentication, encryption, power management, role switching, QoS.

**L2CAP**: Channel multiplexing, segmentation. PSMs (Protocol/Service Multiplexers) route to:
- RFCOMM (serial), SDP (discovery), AVDTP (audio), AVCTP (audio/video control), HID

**SDP (Service Discovery Protocol)**: Discovers services on a remote device.
Each service has a Service Record with attributes (UUIDs, names, parameters).
Replaced by GATT in BLE devices.

**RFCOMM**: Emulates RS-232 serial ports over L2CAP. Used by HSP, HFP, SPP, DUN.

---

## Audio in BR/EDR

### SCO (Synchronous Connection-Oriented)
- Circuit-switched, 64 kbps, fixed slot allocation
- Codec: CVSD (telephony, 8 kHz narrowband)
- Used by: HSP (Headset Profile)

### eSCO (Enhanced SCO, introduced in 1.2)
- Retransmission support, wider codec support
- Codecs: CVSD, mSBC (wideband 16 kHz via HFP 1.6+), aptX, AAC (via A3DP extensions)
- Used by: HFP (Hands-Free Profile)

### A2DP (Advanced Audio Distribution Profile)
- Uses ACL (not SCO), transported via AVDTP over L2CAP
- Codec negotiation: SBC (mandatory), AAC, aptX, LDAC (optional)
- One-way (source → sink); control via AVCTP + AVRCP
- SBC: up to 328 kbps (stereo, 44.1 kHz, bitpool 53)

### LE Audio vs BR/EDR Audio

| | BR/EDR (A2DP/HFP) | LE Audio (5.2+) |
|--|---|---|
| Codec | SBC, AAC, aptX | LC3 |
| Latency | 100–200 ms (SBC) | 20–40 ms |
| Quality at low bitrate | Poor (SBC at 128 kbps) | Good (LC3 at 80 kbps) |
| Multi-stream sync | Limited | Native (CIG/BIG) |
| Broadcast | No | Yes (BIS/Auracast) |
| Power | High | Low |

---

## Common BR/EDR Profiles

| Profile | Full Name | Use Case |
|---------|-----------|---------|
| A2DP | Advanced Audio Distribution Profile | Stereo music streaming |
| AVRCP | Audio/Video Remote Control Profile | Play/pause/volume controls |
| HFP | Hands-Free Profile | Calling via headset/speakerphone |
| HSP | Headset Profile | Basic headset (legacy, replaced by HFP) |
| HID | Human Interface Device Profile | Keyboards, mice, gamepads |
| SPP | Serial Port Profile | Serial cable replacement |
| OPP | Object Push Profile | File exchange (vCard, vCal) |
| PAN | Personal Area Network Profile | IP networking over Bluetooth |
| PBAP | Phone Book Access Profile | Car kit phonebook access |
| MAP | Message Access Profile | SMS access from car kit |

---

## BR/EDR Security

**Pairing methods** (pre-4.0, "Legacy Pairing"):
- PIN-based (4- or 16-digit)
- Vulnerable to brute-force and eavesdropping

**Secure Simple Pairing (SSP, introduced in 2.1)**:
- ECDH-based key exchange
- Methods: Just Works, Passkey Entry, Numeric Comparison, OOB
- Significantly more secure than legacy PIN pairing

**Encryption**: E0 stream cipher (legacy) or AES-CCM (Secure Connections, 4.1+).

---

## Coexistence with BLE

Dual-mode devices share the 2.4 GHz band between BR/EDR and LE.
Key coexistence mechanisms (all in Core Spec):
- **Slot Availability Mask (SAM, 5.0+)**: BR/EDR Primary signals available/busy slots to LE scheduler
- **LE Channel Selection Algorithm #2 (5.0+)**: Better distribution to avoid BR/EDR busy slots
- Both radios typically share one antenna via time-multiplexing managed by a coexistence arbiter
