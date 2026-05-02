# Bluetooth Technology Overview

**Last updated**: 2026-05-02
**Covers**: All Core Spec versions 1.0 through 6.0

---

## What Is Bluetooth?

Bluetooth is a short-range wireless communication standard governed by the **Bluetooth Special Interest Group (SIG)**.
It operates in the **2.4 GHz ISM band** (2.400–2.4835 GHz) and supports two fundamentally different radio technologies
that share the Bluetooth brand but differ in architecture, power profile, and use cases.

---

## Two Radio Technologies

### Bluetooth Classic (BR/EDR)

**BR/EDR** = Basic Rate / Enhanced Data Rate

- Introduced in **Core Spec 1.0 (1998)**
- Uses **frequency-hopping spread spectrum (FHSS)**: 79 channels, 1 MHz spacing, 1600 hops/sec
- Data rates: 1 Mbps (BR), 2 Mbps, 3 Mbps (EDR)
- Designed for **continuous streaming**: audio (A2DP), headsets (HFP/HSP), serial ports (SPP)
- Connection topology: **piconets** (1 primary + up to 7 active secondaries)
- Higher power consumption than LE

### Bluetooth Low Energy (BLE / LE)

**LE** = Low Energy (also called Bluetooth Smart prior to 4.2)

- Introduced in **Core Spec 4.0 (2010)**
- Uses **frequency-hopping** over **40 channels** (2 MHz spacing): 3 advertising + 37 data
- Data rates: 1 Mbps (LE 1M PHY), 2 Mbps (LE 2M PHY, added in 5.0), 125/500 kbps (LE Coded PHY, added in 5.0)
- Designed for **low duty-cycle** IoT devices: sensors, wearables, beacons, health devices
- Supports **connectionless** (advertising/broadcasting) and **connection-oriented** communication
- Star topology or mesh (via Bluetooth Mesh Networking profile)

### Dual-Mode Devices

Most modern smartphones and laptops implement **Dual-Mode** Bluetooth (both BR/EDR and LE),
sharing a single antenna and radio hardware with a common HCI interface to the host.

---

## Protocol Stack

```
┌─────────────────────────────────────────────┐
│           Applications / Profiles           │
├────────────────┬────────────────────────────┤
│   BR/EDR Host  │        LE Host             │
│ ┌────────────┐ │ ┌──────────────────────┐   │
│ │ SDP / RFCOMM│ │ │ GATT  │ GAP  │ SM   │   │
│ │ AVDTP/AVCTP│ │ │       ATT            │   │
│ └────────────┘ │ └──────────────────────┘   │
│       L2CAP (shared)                        │
├─────────────────────────────────────────────┤
│                   HCI                       │
├────────────────┬────────────────────────────┤
│   BR/EDR       │         LE Controller      │
│   Controller   │  ┌─────────────────────┐  │
│                │  │ Link Layer (LL)      │  │
│                │  │ Physical Layer (PHY) │  │
└────────────────┴──┴─────────────────────────┘
```

Key protocol layers:
| Layer | Role |
|-------|------|
| PHY | Radio modulation, channel management |
| Link Layer (LL) | Packet format, connection state machine, scheduling |
| HCI | Host-Controller Interface; standardized command/event API |
| L2CAP | Logical Link Control; multiplexing, segmentation |
| ATT | Attribute Protocol; client-server data model |
| GATT | Generic Attribute Profile; services/characteristics framework |
| GAP | Generic Access Profile; device discovery, connection modes |
| SM | Security Manager; pairing, bonding, key distribution |

---

## Key Concepts

### Advertising vs. Connections (LE)

**Advertising**: A device broadcasts packets on 3 primary advertising channels (37, 38, 39) at configurable intervals.
No connection needed. Used for beacons, sensors, and device discovery.

**Extended Advertising** (added in 5.0): Advertising data can be offloaded to 37 secondary channels,
enabling much larger payloads (up to 255 bytes in auxiliary packets vs. 31 bytes in legacy advertising).

**Connections**: After discovery via advertising, a central device initiates a connection to a peripheral.
Data flows over 37 data channels using adaptive frequency hopping (AFH).

### Physical Layer Options (LE)

| PHY | Symbol Rate | Coding | Max Range | Throughput | Since |
|-----|------------|--------|-----------|------------|-------|
| LE 1M | 1 Msym/s | None | ~100m | ~0.7 Mbps | 4.0 |
| LE 2M | 2 Msym/s | None | ~100m | ~1.4 Mbps | 5.0 |
| LE Coded S=2 | 1 Msym/s | FEC 1/2 | ~400m | ~0.5 Mbps | 5.0 |
| LE Coded S=8 | 1 Msym/s | FEC 1/8 | ~1000m | ~0.125 Mbps | 5.0 |

### Isochronous Channels (LE Audio, added in 5.2)

- **CIS** (Connected Isochronous Stream): Isochronous audio between two connected devices
- **BIS** (Broadcast Isochronous Stream): Isochronous audio broadcast to unlimited receivers
- Enables synchronized multi-speaker audio, hearing aids, broadcast to audiences

---

## Bluetooth SIG & Specifications

The **Bluetooth Special Interest Group** (bluetooth.com) maintains all Bluetooth standards.
Core Specifications are freely downloadable after accepting a terms-of-use agreement.

Specifications are organized into:
- **Core Specification**: The foundational radio, link layer, and host stack spec
- **Profile Specifications**: Define end-to-end behavior for specific use cases (e.g., HID, A2DP, HRS)
- **Service Specifications**: Define GATT services and characteristics
- **Assigned Numbers**: Numeric codes for UUIDs, company IDs, appearance values, etc.

---

## Version Timeline

| Version | Year | Headline Feature |
|---------|------|-----------------|
| 1.0 | 1998 | Initial Bluetooth |
| 2.0+EDR | 2004 | 3 Mbps data rate |
| 3.0+HS | 2009 | High speed over Wi-Fi |
| 4.0 | 2010 | Bluetooth Low Energy |
| 4.1 | 2013 | LE/BR/EDR coexistence, IPv6 |
| 4.2 | 2014 | Privacy, 251-byte LE PDUs |
| **5.0** | **2016** | **2× speed, 4× range, 8× broadcast** |
| **5.1** | **2019** | **Direction Finding** |
| **5.2** | **2019** | **LE Audio, LC3 Codec** |
| **5.3** | **2021** | **Connection Subrating** |
| **5.4** | **2023** | **PAwR, Encrypted Advertising** |
| **6.0** | **2024** | **Channel Sounding** |

---

## See Also

- [BLE Architecture](concepts/ble-architecture.md) — Deep dive into the LE protocol stack
- [Classic Bluetooth](concepts/classic-bluetooth.md) — BR/EDR details
- [Security](concepts/security.md) — Pairing, bonding, privacy, encrypted advertising
- [Profiles and Services](concepts/profiles-and-services.md) — GATT profiles
