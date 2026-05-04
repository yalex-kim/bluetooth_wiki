# Bluetooth Profiles and Services

**Last updated**: 2026-05-03
**Covers**: Key BR/EDR and GATT profiles through latest versions

---

## Overview

**Profiles** define end-to-end behavior for specific use cases, built on top of the core spec.

Two profile systems exist in parallel:
- **GATT Profiles** (BLE): Defined in terms of Services and Characteristics — see [LE Audio](le-audio.md) for LE Audio profiles
- **BR/EDR Profiles**: Defined in terms of L2CAP channels and protocol stacks — described in detail below

---

## BR/EDR Classic Audio Profiles

### A2DP — Advanced Audio Distribution Profile v1.4.1

**Version Date**: 2025-06-30
**Source**: [A2DP_v1.4.1.md](../../sources/specs/profiles/A2DP_v1.4.1.md)

Defines high-quality stereo audio streaming from a Source to a Sink over BR/EDR.

**Roles**:
- **Source (SRC)**: Encodes and sends the audio stream (e.g., phone, PC)
- **Sink (SNK)**: Receives and decodes the audio stream (e.g., headphones, speaker)

**Protocol Stack**:
```
Application (codec encode/decode)
    └── AVDTP (Audio/Video Distribution Transport Protocol)
        └── L2CAP → ACL → Baseband
```
AVDTP handles both signaling (codec negotiation) and transport (streaming) over L2CAP. `[A2DP v1.4.1, §2]`

**Codec Support**:

| Codec | SRC | SNK | Notes |
|-------|-----|-----|-------|
| **SBC** | M | M | Mandatory baseline codec `[A2DP v1.4.1, §4.3]` |
| MPEG-1,2 Audio (mp1/2/3) | O | O | Optional |
| MPEG-2,4 AAC | O | O | If supported: MPEG-2 AAC LC is mandatory `[A2DP v1.4.1, §4.5]` |
| MPEG-D USAC | O | O | Optional (added v1.4) |
| Vendor Specific | O | O | Codec-specific negotiation |

**SBC Parameters** `[A2DP v1.4.1, §4.3.2]`:
- **SNK mandatory**: 44.1 kHz + 48 kHz sampling; all channel modes (Mono, Dual, Stereo, Joint Stereo); all block lengths (4/8/12/16); subbands 4 + 8; both allocation methods (SNR + Loudness)
- **SRC mandatory**: at least one of 44.1/48 kHz; Mono + one stereo mode; at least 8 subbands; Loudness allocation
- **Bitpool** (quality proxy): Max bit rate = 320 kbps (mono), 512 kbps (two-channel)

| Quality | Mode | 44.1 kHz bitpool | Bit rate |
|---------|------|-----------------|---------|
| High Quality | Joint Stereo | 53 | ~328 kbps |
| High Quality | Mono | 31 | ~193 kbps |
| Middle Quality | Joint Stereo | 35 | ~229 kbps |

**Connection Setup** (simplified):
1. SRC/SNK establish ACL connection (GAP)
2. SRC queries SNK AVDTP version via SDP
3. GAVDP Connection Establishment: AVDTP_DISCOVER → AVDTP_GET_ALL_CAPABILITIES → AVDTP_SET_CONFIGURATION
4. GAVDP Start Streaming: both devices enter STREAMING state
5. SRC sends encoded audio frames; SNK decodes and renders

**Version History**:

| Version | Date | Key Change |
|---------|------|-----------|
| v1.3.2 | 2019-01-21 | Adopted |
| **v1.4** | 2022-06-21 | Added AAC HE-AACv2, AAC-ELDv2, MPEG-D DRC, MPEG-D USAC |
| **v1.4.1** | 2025-06-30 | Errata fixes (23748, 25272, 22841, 27471) |

---

### HFP — Hands-Free Profile v1.10

**Version Date**: 2025-12-15
**Source**: [HFP_v1.10.md](../../sources/specs/profiles/HFP_v1.10.md)

Allows a mobile phone to be used with a hands-free device over BR/EDR. Provides bidirectional voice audio and AT command-based call control.

**Roles**:
- **Audio Gateway (AG)**: Gateway to the telephone network (e.g., mobile phone)
- **Hands-Free unit (HF)**: Remote audio I/O and call control (e.g., car kit, headset)

**Protocol Stack**:
```
AT Commands (call control)     SCO/eSCO (voice audio)
    └── RFCOMM                     └── Baseband
        └── L2CAP → ACL → Baseband
```

**Codec Support** `[HFP v1.10, §3 Table 3.3]`:

| Codec | Bandwidth | Mandatory condition |
|-------|-----------|-------------------|
| **CVSD** | Narrowband, 8 kHz | Always mandatory |
| **mSBC** (modified SBC) | Wideband, 16 kHz | Mandatory if Wideband Speech supported |
| **LC3-SWB** | Super Wideband, 32 kHz | Mandatory if Super Wideband Speech supported |

**Link configurations** `[HFP v1.10, §3 Table 3.4]`:
- D0/D1: CVSD on SCO link (HV1/HV3)
- S1–S4: CVSD on eSCO (EV3, 2-EV3)
- T1/T2: mSBC on eSCO (EV3, 2-EV3) — requires Codec Negotiation
- T1/T2: LC3-SWB on eSCO (EV3, 2-EV3) — requires Codec Negotiation

**Key Application Features** `[HFP v1.10, §3 Table 3.1]`:

| Feature | HF | AG |
|---------|----|----|
| Connection management | M | M |
| Phone status (service, signal, battery, call) | M | M |
| Audio Connection handling | M | M |
| Accept/Reject incoming call | M | O/M |
| Terminate call | M | M |
| Wideband Speech + Codec Negotiation | O | O |
| Voice Recognition (incl. Enhanced) | O | O |
| Super Wideband Speech (LC3-SWB) | O | O |
| Call Forwarding | O | O |
| Call Duration Information | O | O |

**Version History**:

| Version | Date | Key Change |
|---------|------|-----------|
| v1.7 | 2014-09 | HF Indicators |
| v1.8 | 2020-04-14 | Enhanced Voice Recognition Activation |
| **v1.9** | 2023-09-12 | Super Wideband Speech (LC3-SWB at 32 kHz) |
| **v1.10** | 2025-12-15 | Call Forwarding feature; Call Duration Information |

---

### AVRCP — Audio/Video Remote Control Profile v1.6.3

**Version Date**: 2024-10-01
**Source**: [AVRCP_v1.6.3.md](../../sources/specs/profiles/AVRCP_v1.6.3.md)

Defines remote control of audio/video devices. Complements A2DP by providing transport controls (play, pause, skip, volume) and metadata delivery.

**Roles**:
- **Controller (CT)**: Sends commands (e.g., headset, car kit, phone)
- **Target (TG)**: Receives and executes commands (e.g., phone, media player, amplifier)

**Protocol Stack**:
```
AVRCP Application
    ├── AV/C commands (primary AVCTP channel) — play/pause/volume/metadata
    ├── Browsing channel (second AVCTP channel) — folder/item navigation
    └── BIP over OBEX — Cover Art image transfer (v1.6+)
        └── L2CAP → ACL → Baseband
```

**Device Categories** `[AVRCP v1.6.3, §2.2.2]`:
- Category 1: Player/Recorder — basic play, pause, stop, record
- Category 2: Monitor/Amplifier — volume, mute
- Category 3: Tuner — channel selection
- Category 4: Menu — on-screen menu navigation

**Key Operations** `[AVRCP v1.6.3, §6]`:
- `SetAbsoluteVolume` — CT sets TG's volume level directly (0–127)
- `RegisterNotification` — CT subscribes to TG state changes (volume, track, playback status)
- `GetElementAttributes` — CT requests metadata (title, artist, album, duration, cover art handle)
- `SetBrowsedPlayer` / `GetFolderItems` — Browsing channel: navigate media library
- `NumberOfItems` — CT requests item count in current folder without full download

**Version History**:

| Version | Date | Key Change |
|---------|------|-----------|
| v1.6.0 | 2014-09 | Cover Art (BIP over OBEX), Number of Items |
| v1.6.2 | 2019-01-21 | Errata fixes |
| **v1.6.3** | 2024-10-01 | Errata fixes (10214, 13170, 18145, 23562, etc.) |

---

### HID — Human Interface Device Profile v1.1.2

**Version Date**: 2025-11-03
**Source**: [HID_v1.1.2.md](../../sources/specs/profiles/HID_v1.1.2.md)

Adapts the USB HID class specification for Bluetooth, enabling keyboards, mice, gamepads, and other input devices to communicate wirelessly.

**Roles**:
- **HID Device**: Provides input/output (e.g., keyboard, mouse, gamepad, sensor)
- **HID Host**: Consumes the HID service (e.g., PC, phone, game console)

**Protocol Stack**:
```
HID Application
    └── Bluetooth HID Protocol (HIDP)
        ├── Control Channel (L2CAP PSM 0x0011) — synchronous reports, protocol setup
        └── Interrupt Channel (L2CAP PSM 0x0013) — asynchronous Input/Output reports
            └── ACL → Baseband
```

**Report Types** `[HID v1.1.2, §2.1.1]`:

| Type | Direction | Channel | Use |
|------|-----------|---------|-----|
| **Input** | Device → Host | Interrupt (async) or Control | Key press, mouse movement, sensor data |
| **Output** | Host → Device | Interrupt (async) or Control | LED state, force feedback |
| **Feature** | Bidirectional | Control (synchronous) | Configuration, non-time-critical state |

**Report Protocols** `[HID v1.1.2, §2.1.2]`:
- **Report Protocol Mode** (default): Host parses device's Report Descriptor from SDP to understand arbitrary report formats. Supports all device types.
- **Boot Protocol Mode**: Simplified fixed format for keyboards and mice. Does not require Report Descriptor parsing. Required on devices with keyboard/mouse subclass bits set in SDP.

**SDP Key Attributes**:
- `HIDDescriptorList`: Contains the Report Descriptor defining the device's buttons, axes, LEDs, and feature reports
- `HIDDeviceSubclass`: Declares device type (Keyboard, Pointing Device, Gamepad, etc.)
- `HIDNormallyConnectable`: If TRUE, device enters page scan after disconnect so host can reconnect it

**Virtual Cable**: Persistent logical bond between one HID device and one HID host. Device may maintain multiple Virtual Cables but only one is active at a time.

**Version History**:

| Version | Date | Key Change |
|---------|------|-----------|
| v1.0 | 2003-05-22 | Initial adoption |
| v1.1 | 2012-02-21 | Secure Simple Pairing support, Sniff Subrating SDP attributes, Boot Protocol Mode guidance |
| v1.1.1 | 2015-12-15 | Errata fixes |
| **v1.1.2** | 2025-11-03 | Errata fixes (23462, 27927, 15796, 28229) |

---

### MAP — Message Access Profile v1.4.3

**Version Date**: 2025-02-11
**Source**: [MAP_v1.4.3-3.md](../../sources/specs/profiles/MAP_v1.4.3-3.md)

Defines procedures and protocols for exchanging messages (SMS, MMS, email, IM) between devices. Primary use case: car kit accessing phone messages over BR/EDR.

**Roles**:
- **MSE (Message Server Equipment)**: Provides the message repository — network access and message storage (e.g., mobile phone)
- **MCE (Message Client Equipment)**: Browses, retrieves, and uploads messages via the MSE (e.g., car kit, PC)

**Protocol Stack**:
```
MAP Application (bMessage objects)
    └── OBEX (MAS = Message Access Service, MNS = Message Notification Service)
        ├── GOEP v2.0+ → L2CAP (preferred)
        └── GOEP v1.1  → RFCOMM → L2CAP (legacy backward compat)
            └── ACL → Baseband
```

**Message Types** `[MAP v1.4.3, §2.3]`:

| Type | Description |
|------|-------------|
| EMAIL | RFC 5322 / MIME email |
| SMS_GSM | GSM short messages |
| SMS_CDMA | CDMA short messages |
| MMS | 3GPP MMS messages |
| IM | Instant messages (MIME-based) |

**Key Operations** `[MAP v1.4.3, §5]`:
- `GetFolderListing` — MCE browses message folders (inbox, outbox, sent, deleted, draft)
- `GetMessagesListing` — MCE retrieves a filtered list of message headers
- `GetMessage` — MCE downloads a specific message (by 64-bit handle)
- `PushMessage` — MCE sends a new message via the MSE
- `SetMessageStatus` — MCE marks message as read/unread or deletes it
- `SendEvent` — MSE notifies MCE of new or changed messages (via MNS connection)

**Message Object Format**: bMessage (BMSG) — an envelope format wrapping the actual message content, originator vCard, recipient vCard, and metadata (read status, type, folder path).

**Version History**:

| Version | Date | Key Change |
|---------|------|-----------|
| v1.4 | 2017-06-27 | Instant Messaging (IM) support |
| v1.4.1 | 2019-01-21 | Errata fixes |
| v1.4.2 | 2019-08-13 | Errata fixes |
| **v1.4.3** | 2025-02-11 | Errata fixes (18776, 18791, 23840, 11797, 22347) |

---

### PBAP — Phone Book Access Profile v1.2.3

**Version Date**: 2019-01-21
**Source**: [PBAP_v1.2.3.md](../../sources/specs/profiles/PBAP_v1.2.3.md)

Defines procedures for retrieving phone book objects from a remote device over BR/EDR. Read-only access; used by car kits and hands-free systems to download contacts and call histories.

**Roles**:
- **PSE (Phone Book Server Equipment)**: Contains the source phone book (e.g., mobile phone)
- **PCE (Phone Book Client Equipment)**: Retrieves phone book objects (e.g., car kit, HFP device)

**Protocol Stack**:
```
PBAP Application (vCard objects)
    └── OBEX
        ├── GOEP v2.0+ → L2CAP (preferred)
        └── GOEP v1.1  → RFCOMM → L2CAP (legacy)
            └── ACL → Baseband
```

**Phone Book Objects** `[PBAP v1.2.3, §3.1.2]`:

| Object | Description |
|--------|-------------|
| `pb` | Main phone book (contacts stored on device or SIM) |
| `ich` | Incoming calls history |
| `och` | Outgoing calls history |
| `mch` | Missed calls history |
| `cch` | Combined calls history (ich + och + mch) |
| `spd` | Speed-dial entries |
| `fav` | Favorite contacts |

**Entry Format**: vCard 2.1 or 3.0 (UTF-8 encoded). PSE must support both formats and deliver whichever the PCE requests. `[PBAP v1.2.3, §3.1.4]`

**Key Features** (added in v1.2):
- GOEP v2.0 (OBEX over L2CAP + Single Response Mode)
- Folder Version Counters — client detects phone book changes without full re-download
- vCard Selecting — filter entries by property, UID, or search string
- Enhanced Missed Calls — new missed-call counter with reset command
- Unique Caller Identifier (UCI) — persistent cross-device caller ID
- Contact UIDs — cross-reference contacts across folders

**Version History**:

| Version | Date | Key Change |
|---------|------|-----------|
| v1.2.0 | 2013-11-05 | GOEP v2.0, folder version counters, vCard selecting, UCI, contact UIDs |
| v1.2.1 | 2015-12-15 | Errata fix (E6220) |
| **v1.2.3** | 2019-01-21 | Errata fixes (E6492, E6503, E6819, E6820, E6877, E7799, E8539) |

---

## GATT Service/Characteristic Model

GATT defines a structured hierarchy of attributes:

```
Service (UUID e.g., Heart Rate Service 0x180D)
  └── Characteristic (UUID e.g., Heart Rate Measurement 0x2A37)
        ├── Value (actual data bytes)
        └── Descriptor (e.g., Client Characteristic Configuration Descriptor 0x2902)
```

**Characteristic Properties** (bitmask in Characteristic Declaration):

| Bit | Property | Meaning |
|-----|----------|---------|
| 0x02 | Read | Client can read |
| 0x04 | Write Without Response | Client can write, no confirmation |
| 0x08 | Write | Client can write, with confirmation |
| 0x10 | Notify | Server pushes updates, no ACK |
| 0x20 | Indicate | Server pushes updates, with ACK |

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
| Human Interface Device | 0x1812 | HID Info, Report Map, Report, Protocol Mode | BLE HID (HOGP) |
| Environmental Sensing | 0x181A | Temperature, Humidity, Pressure, etc. | Sensor nodes |

---

## Key BLE Profiles

### LE Audio Profiles (5.2+)

| Profile | Acronym | Function |
|---------|---------|---------|
| Basic Audio Profile | BAP | Foundation: unicast + broadcast audio over CIS/BIS |
| Common Audio Profile | CAP | Multi-device coordination (stereo earbud pairs) |
| Telephony and Media Audio | TMAP | Phone calls + media playback over LE Audio |
| Hearing Access Profile | HAP | Hearing aids and assisted listening |
| Public Broadcast Profile | PBP | Auracast™ broadcast without pairing |

See [LE Audio](le-audio.md) for detailed coverage.

### ESL Profile (5.4+)

Built on PAwR; connects an ESL Access Point to Electronic Shelf Label tags. Supports thousands of tags from one access point.

---

## Profile vs. Service

- **Service**: A GATT server-side collection of characteristics (server concept)
- **Profile**: End-to-end specification defining roles (client + server), procedures, and requirements
- A profile defines which services each role must implement and how to interact with them

---

## UUIDs

- **16-bit UUIDs** (SIG-assigned): Short form `0xXXXX`; full form `0000XXXX-0000-1000-8000-00805F9B34FB`
- **128-bit UUIDs** (custom): For proprietary services (generated as RFC 4122 UUIDs)

Assigned Numbers: [bluetooth.com/specifications/assigned-numbers](https://www.bluetooth.com/specifications/assigned-numbers/)

---

## See Also

- [BLE Architecture](ble-architecture.md)
- [LE Audio](le-audio.md)
- [Classic Bluetooth](classic-bluetooth.md)
- [Security](security.md)

---

*Source: [Core 6.2, Vol 3, Part G (GATT), Part C (GAP)](../../sources/specs/6.2/Core_v6.2.md)*
