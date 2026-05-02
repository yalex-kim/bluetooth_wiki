# Bluetooth Profiles and Services

**Last updated**: 2026-05-02
**Covers**: GATT-based profiles and key BR/EDR profiles

---

## Overview

**Profiles** define end-to-end behavior for specific use cases, built on top of the core spec.
The Bluetooth SIG maintains a library of standardized profiles and services at bluetooth.com.

Two profile systems exist in parallel:
- **GATT Profiles** (BLE): Defined in terms of Services and Characteristics
- **BR/EDR Profiles**: Defined in terms of L2CAP channels and protocol stacks (A2DP, HFP, HID, etc.)

---

## GATT Service/Characteristic Model

Every GATT server exposes a hierarchy of **Services** containing **Characteristics**.

```
GATT Server
└── Primary Service: Heart Rate Service (UUID 0x180D)
    ├── Characteristic: Heart Rate Measurement (0x2A37)
    │   ├── Value: [flags=0x00, hr_value=72]
    │   └── Descriptor: CCCD (0x2902) [notify enabled]
    ├── Characteristic: Body Sensor Location (0x2A38)
    │   └── Value: [chest=1]
    └── Characteristic: HR Control Point (0x2A39)
        └── Value: [reset_energy_expended]
```

### Attribute Permissions

Each attribute has read/write permissions:
- **No Access**, **Read**, **Write**, **Read+Write**
- **Encrypted Read/Write** (requires link encryption)
- **Authenticated Read/Write** (requires authenticated pairing)
- **Authorized** (application-level authorization)

### Characteristic Properties

Bitmask in the Characteristic Declaration:
| Bit | Property | Meaning |
|-----|----------|---------|
| 0x01 | Broadcast | Value can be included in advertising |
| 0x02 | Read | Client can read |
| 0x04 | Write Without Response | Client can write, no confirmation |
| 0x08 | Write | Client can write, with confirmation |
| 0x10 | Notify | Server pushes updates, no confirmation |
| 0x20 | Indicate | Server pushes updates, with confirmation |
| 0x40 | Authenticated Signed Writes | Write with CSRK signature |
| 0x80 | Extended Properties | Additional properties in descriptor |

---

## Standard GATT Services (Selected)

| Service | UUID | Key Characteristics | Use Case |
|---------|------|--------------------|----|
| Generic Access | 0x1800 | Device Name, Appearance, Preferred Conn Params | All devices |
| Generic Attribute | 0x1801 | Service Changed (0x2A05), Client Supported Features | GATT management |
| Device Information | 0x180A | Manufacturer Name, Model, Firmware Rev, PnP ID | Device info |
| Battery Service | 0x180F | Battery Level (0x2A19) | Battery % reporting |
| Heart Rate | 0x180D | HR Measurement, Body Location, Control Point | Fitness HR monitors |
| Health Thermometer | 0x1809 | Temperature Measurement | Medical thermometers |
| Blood Pressure | 0x1810 | BP Measurement, Cuff Pressure | BP monitors |
| Human Interface Device | 0x1812 | HID Info, Report Map, Report, Protocol Mode | BLE HID devices |
| Nordic UART Service | 0x6E40... | RX/TX Characteristics | Custom serial (non-SIG) |
| Automation IO | 0x1815 | Digital, Analog | GPIO access |
| Environmental Sensing | 0x181A | Temperature, Humidity, Pressure, etc. | Sensor nodes |

---

## Key BLE Profiles

### GAP-based Profiles

**Proximity Profile**:
- Uses Link Loss Service (0x1803), Immediate Alert Service (0x1802), TX Power Service (0x1804)
- Alerts when connection drops (link loss) or RSSI falls below threshold
- Foundation for "find my device" use cases

**Find Me Profile**:
- Uses Immediate Alert Service
- Central writes Alert Level to make peripheral sound an alert

**Time Profile**:
- Current Time Service (0x1805), Reference Time Update Service
- Syncs RTC on peripheral to phone's time

### LE Audio Profiles (5.2+)

| Profile | Acronym | Function |
|---------|---------|---------|
| Basic Audio Profile | BAP | Foundation: unicast + broadcast audio over BIS/CIS |
| Common Audio Profile | CAP | Coordinator role; multi-device synchronization |
| Telephone and Media Audio | TMAP | Phone calls + media playback (replaces HFP+A2DP) |
| Hearing Access Profile | HAP | Hearing aids, hearing loss accommodations |
| Public Broadcast Profile | PBP | Auracast™ broadcast without pairing |
| Gaming Audio Profile | GAP (LE Audio) | Ultra-low latency for gaming headsets |

### ESL Profile (5.4+)

**Electronic Shelf Label (ESL) Profile**:
- Built on PAwR (Periodic Advertising with Responses)
- ESL Access Point ↔ ESL Tags (price tags, displays)
- Commands: set display image, set LED, read sensor
- Supports thousands of tags from one access point

---

## Key BR/EDR Profiles

### Audio

| Profile | Acronym | Function |
|---------|---------|---------|
| Advanced Audio Distribution | A2DP | Stereo audio streaming (SBC, AAC, aptX) |
| Audio/Video Remote Control | AVRCP | Play, pause, skip, volume control |
| Hands-Free | HFP | Calls via headset/speakerphone (SCO audio) |
| Headset | HSP | Legacy headset (superseded by HFP) |

### Data / HID

| Profile | Acronym | Function |
|---------|---------|---------|
| Human Interface Device | HID | Keyboards, mice, gamepads over Bluetooth |
| Serial Port | SPP | RS-232 serial cable replacement |
| Personal Area Network | PAN | IP networking (NAP, GN, PANU roles) |
| Object Push | OPP | File/vCard push (used in NFC handover) |

### Automotive / Phone

| Profile | Acronym | Function |
|---------|---------|---------|
| Phone Book Access | PBAP | Phone book sync for car kits |
| Message Access | MAP | SMS/MMS access from car kit |
| Car Connectivity | CCP | Generic Car Connectivity Consortium access |

---

## Profile vs. Service

Terminology clarification:
- **Service**: A GATT server-side collection of characteristics (server concept)
- **Profile**: End-to-end specification defining roles (client+server), procedures, and requirements
- A profile defines which services each role must implement and how to interact with them
- Example: Heart Rate Profile defines a **Heart Rate Sensor** (server with Heart Rate Service)
  and a **Collector** (client that subscribes to notifications)

---

## UUIDs

Bluetooth uses **UUIDs** to identify services, characteristics, and descriptors.

- **16-bit UUIDs** (SIG-assigned): Used for standardized services/characteristics
  - Full UUID: `0000XXXX-0000-1000-8000-00805F9B34FB`
  - Short form: `0xXXXX`
- **128-bit UUIDs** (custom/vendor): Used for proprietary services
  - Generated as standard UUIDs (e.g., via RFC 4122)

Assigned Numbers document: [https://www.bluetooth.com/specifications/assigned-numbers/](https://www.bluetooth.com/specifications/assigned-numbers/)

---

## GATT Service Discovery

Standard discovery procedure:
1. `ATT_READ_BY_GROUP_TYPE_REQ` (UUID=0x2800) → all Primary Services
2. `ATT_READ_BY_TYPE_REQ` (UUID=0x2803) → all Characteristics in a service
3. `ATT_FIND_INFO_REQ` → Descriptors for each characteristic
4. Check CCCD (0x2902) to enable Notify/Indicate

**Optimization (5.1+)**: Cache discovery results keyed by GATT Database Hash.
Eliminates re-discovery on reconnection if hash matches.

**EATT (5.2+)**: Run multiple discovery requests in parallel for faster initial connection setup.
