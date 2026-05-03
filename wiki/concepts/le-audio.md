# LE Audio Framework

**Last updated**: 2026-05-04
**Covers**: LE Audio architecture introduced in Core Spec 5.2 through 6.2

---

## Overview

LE Audio is the next generation of Bluetooth audio, operating over the **Bluetooth Low Energy** radio. It replaces the legacy BR/EDR audio stack (A2DP/HFP) with a more efficient, high-quality, and flexible framework.

Key benefits:
- **Higher Quality**: Via the mandatory LC3 codec.
- **Lower Power**: Optimized for small battery devices like hearing aids and earbuds.
- **Multi-Stream**: Native support for synchronized independent audio streams.
- **Broadcast**: Auracast™ allows one transmitter to reach unlimited receivers.

---

## Core Architecture (The "Three Pillars")

LE Audio is built on three fundamental technical pillars introduced in **Core Spec 5.2**:

### 1. LC3 (Low Complexity Communication Codec)

LC3 is the mandatory codec for LE Audio, replacing SBC from Classic Bluetooth audio. It delivers higher audio quality at significantly lower bitrates.

- **Sampling Rates**: 8, 16, 24, 32, 44.1, 48 kHz.
- **Bitrates**: 16–320 kbps per channel (typical: 64–96 kbps for high-quality voice; 128–192 kbps for music).
- **Frame Durations**: 7.5 ms (low latency — preferred for gaming/calls) and 10 ms (higher efficiency — default for streaming profiles).
- **Efficiency**: At 160 kbps, LC3 provides perceived quality equivalent to SBC at 345 kbps, reducing radio bandwidth and device power consumption.
- **Robustness**: Built-in PLC (Packet Loss Concealment) suppresses audio glitches and pop noise in unstable RF environments.
- **Bit Depth**: 16, 24, and 32-bit signed integer input supported.

`[LC3 Specification v1.0, Bluetooth SIG]`

### 2. Isochronous Channels (Physical/Link Layer)

Provides timing-critical transport for audio data. `[Core 5.2, Vol 6, Part B]`

- **CIS (Connected Isochronous Stream)**: Point-to-point (e.g., Phone ↔ Earbud). Supports bidirectional data (voice calls). `[Core 6.2, Vol 6, Part B, §4.5.13](../../sources/specs/6.2/Core_v6.2.md#L61061)`
- **BIS (Broadcast Isochronous Stream)**: One-to-many (e.g., public display → all nearby listeners). Unidirectional. `[Core 6.2, Vol 6, Part B, §4.4.6](../../sources/specs/6.2/Core_v6.2.md#L60515)`
- **CIG/BIG**: Groups of streams (Connected/Broadcast Isochronous Groups) sharing a common timing reference for sub-millisecond synchronization across devices.

### 3. ISOAL (Isochronous Adaptation Layer)

Resides between the Upper Stack and the Link Layer. Fragments SDUs (Service Data Units) into PDUs (Protocol Data Units) to fit the radio's isochronous timing slots. `[Core 6.2, Vol 6, Part G]`

- **Unsegmented Framed Mode** (added in Core 6.0): An optimized SDU-to-PDU mapping for ISOAL where each PDU carries exactly one complete SDU with minimal framing overhead, improving efficiency for fixed-size audio frames. `[Core 6.0, Vol 6, Part G, §2](../../sources/specs/6.0/Core_v6.0.md#L74377)`

---

## Latency Budget

End-to-end audio latency in LE Audio is the sum of three configurable delays, negotiated via BAP:

```
Total Latency ≈ Presentation_Delay + SDU_Interval + Max_Transport_Latency
```

| Parameter | Typical Range | Notes |
|-----------|--------------|-------|
| `SDU_Interval` | 7.5 ms or 10 ms | LC3 frame duration |
| `Max_Transport_Latency` | 20–100 ms | Maximum allowed transit time across Isochronous Channel |
| `Presentation_Delay` | 10–40 ms | Renderer buffer time; allows CIG-synchronized devices to present in sync |

Gaming/TWS (True Wireless Stereo) targets: total < 40 ms. Broadcast/hearing loop targets: total < 100 ms.

---

## LE Audio Middleware and Profiles

Unlike Classic Audio, LE Audio uses a modular GATT-based architecture with clearly separated roles. All profiles below are Bluetooth SIG specifications.

### BAP — Basic Audio Profile v1.0.2

**Version Date**: 2024-10-01 | **Source**: [BAP_v1.0.2.md](../../sources/specs/profiles/BAP_v1.0.2.md)

Foundation profile for all LE Audio. Defines all procedures to set up, configure, and control unicast and broadcast audio streams. `[BAP v1.0.2, §1]`

**Roles** `[BAP v1.0.2, §3]`:

| Role | Description |
|------|-------------|
| **Unicast Client** | Central; discovers servers, configures ASEs, establishes CIS |
| **Unicast Server** | Peripheral; exposes ASEs via ASCS, accepts CIS |
| **Broadcast Source** | Creates BIG/BIS, transmits audio |
| **Broadcast Sink** | Synchronizes to BIG, receives BIS data |
| **Broadcast Assistant** | Scans for BIG on behalf of Scan Delegator |
| **Scan Delegator** | Offloads BIG scanning to an Assistant |

**GATT Services** `[BAP v1.0.2, §3.2]`:
- **ASCS** (Audio Stream Control Service) — per-device ASE state machines (Idle → Codec Configured → QoS Configured → Enabling → Streaming → Disabling → Releasing)
- **PACS** (Published Audio Capabilities Service) — codec capabilities and audio locations
- **BASS** (Broadcast Audio Scan Service) — Broadcast Source advertisement list

**Version History**: v1.0 (2021-09-14) → v1.0.1 (2022-06-21) → **v1.0.2** (2024-10-01, 28 errata)

---

### CAP — Common Audio Profile v1.0.1

**Version Date**: 2025-02-11 | **Source**: [CAP_v1.0.1.md](../../sources/specs/profiles/CAP_v1.0.1.md)

Orchestration layer that coordinates BAP, VCP, MICP, and CSIP operations across multiple devices simultaneously. `[CAP v1.0.1, §1]`

**Roles** `[CAP v1.0.1, §3]`:

| Role | Description |
|------|-------------|
| **Initiator** | Central; starts/updates/stops audio streams, commands multiple Acceptors |
| **Acceptor** | Peripheral; renders or captures audio, accepts commands |
| **Commander** | Controls audio inputs, volume, and broadcast scanning on behalf of Acceptors |

**Key Features** `[CAP v1.0.1, §5–6]`:
- Coordinated Set (CSIP) management: addresses a stereo earbud pair as one logical unit
- CAP Announcement in extended advertising for device discovery
- Procedures for unicast/broadcast start, update, stop across single or multiple devices
- Content Control ID (CCID) association for linking audio streams to call/media context

**Version History**: v1.0 (2022-03-22) → **v1.0.1** (2025-02-11, 28 errata)

---

### VCP — Volume Control Profile v1.0

**Version Date**: 2020-12-15 | **Source**: [VCP_v1.0.md](../../sources/specs/profiles/VCP_v1.0.md)

Unified volume control for LE Audio renderers (replaces per-device proprietary volume controls). `[VCP v1.0, §1]`

**Roles**: **Volume Controller** (GATT Client) ↔ **Volume Renderer** (GATT Server)

**GATT Services** `[VCP v1.0, §3]`:
- **VCS** (Volume Control Service, mandatory) — volume level (0–255), mute flag, change counter
- **VOCS** (Volume Offset Control Service, optional, multiple) — per-input/per-sink volume offset
- **AICS** (Audio Input Control Service, optional, multiple) — audio input gain, mute, mode

**Key Operations**: Absolute volume set, relative up/down, mute/unmute, volume-change counter for conflict detection, persistent volume flags `[VCP v1.0, §4]`

---

### MCP — Media Control Profile v1.0

**Version Date**: 2021-03-09 | **Source**: [MCP_v1.0.md](../../sources/specs/profiles/MCP_v1.0.md)

BLE-native replacement for AVRCP. Controls media playback on a remote player. `[MCP v1.0, §1]`

**Roles**: **Media Control Server** (player) ↔ **Media Control Client** (controller)

**GATT Services** `[MCP v1.0, §3]`:
- **GMCS** (Generic Media Control Service, mandatory single instance) — controls all media players on device
- **MCS** (Media Control Service, optional multiple) — per-player instance

**Key Operations** `[MCP v1.0, §4–5]`:
- Play, pause, stop, fast forward/rewind, skip
- Read track title, artist, album, duration, playback position
- Set playback speed (0.25× – 3.957×)
- Shuffle mode (Off / Tracks / Groups / AllTracks / AllGroups)
- Repeat mode (Off / Single / Track / Group)
- Object Transfer Profile (OTP) optional for icons and track metadata

---

### CCP — Call Control Profile v1.0

**Version Date**: 2021-03-09 | **Source**: [CCP_v1.0.md](../../sources/specs/profiles/CCP_v1.0.md)

BLE-native replacement for HFP call management. `[CCP v1.0, §1]`

**Roles**: **Call Control Server** (phone) ↔ **Call Control Client** (headset/carkit)

**GATT Services** `[CCP v1.0, §3]`:
- **GTBS** (Generic Telephone Bearer Service, mandatory) — unified view of all bearers on device
- **TBS** (Telephone Bearer Service, optional multiple) — per-app bearer (VoIP app, cellular, etc.)

**Key Features** `[CCP v1.0, §4]`:
- Accept, reject, terminate, hold, retrieve calls
- Dial a URI (tel:, sip:)
- Query bearer name, UCI (Uniform Caller Identifier), technology, signal strength
- Multiple concurrent calls with join/transfer
- Content Control ID (CCID) links bearer to audio stream

---

### HAP — Hearing Access Profile v1.0.1

**Version Date**: 2024-10-01 | **Source**: [HAP_v1.0.1.md](../../sources/specs/profiles/HAP_v1.0.1.md)

Defines interoperability for hearing aids with LE Audio sources, including binaural synchronization and preset management. `[HAP v1.0.1, §1]`

**Roles** `[HAP v1.0.1, §3]`:

| Role | Description |
|------|-------------|
| **Hearing Aid (HA)** | Monaural or part of a binaural set; renders audio |
| **Hearing Aid Unicast Client (HAUC)** | Phone/tablet sending/receiving audio to HA |
| **Hearing Aid Remote Controller (HARC)** | Controls volume, mic, preset without full audio |
| **Immediate Alert Client (IAC)** | Alerts wearer via HA buzzer/vibration |

**GATT Services**: HAS (Hearing Access Service) — preset list, active preset, preset record write/switch; VCS/VOCS for volume balance between binaural devices `[HAP v1.0.1, §3.3]`

**Key Features**: Binaural set coordination (CSIP), preset synchronization, ambient sound transparency mode, immediate alert `[HAP v1.0.1, §4]`

**Version History**: v1.0 (2022-06-07) → **v1.0.1** (2024-10-01, 3 errata)

---

### PBP — Public Broadcast Profile v1.0.2

**Version Date**: 2025-11-03 | **Source**: [PBP_v1.0.2.md](../../sources/specs/profiles/PBP_v1.0.2.md)

Defines Auracast™ broadcast audio discovery and reception without prior pairing. Extends CAP/BAP broadcast roles. `[PBP v1.0.2, §1]`

**Roles**:

| Role | Base Role | Description |
|------|-----------|-------------|
| **Public Broadcast Source (PBS)** | CAP Initiator + BAP Broadcast Source | Advertises and transmits broadcast audio |
| **Public Broadcast Sink (PBK)** | CAP Acceptor + BAP Broadcast Sink | Discovers and renders broadcast audio |
| **Public Broadcast Assistant (PBA)** | CAP Commander + BAP Broadcast Assistant | Assists PBK in discovering sources |

**Audio Quality Configurations** `[PBP v1.0.2, §3.4]`:
- **Standard Quality (SQ)**: LC3, 16 kHz or 24 kHz, 32 kbps per channel
- **High Quality (HQ)**: LC3, 48 kHz, 96 kbps per channel

**Key Features**: Public Broadcast Announcement in extended advertising, optional Broadcast_Code (out-of-band key), Broadcast Name metadata, Immediate Rendering Flag, Audio Active State `[PBP v1.0.2, §3]`

**Version History**: v1.0 (2022-07-05) → v1.0.1 (2024-10-01, 5 errata) → **v1.0.2** (2025-11-03, 4 errata)

---

### TMAP — Telephony and Media Audio Profile v1.0.1

**Version Date**: 2025-02-11 | **Source**: [TMAP_v1.0.1-1.md](../../sources/specs/profiles/TMAP_v1.0.1-1.md)

Defines minimum interoperability configurations for phone calls and media streaming over LE Audio. `[TMAP v1.0.1, §1]`

**Roles** `[TMAP v1.0.1, §3]`:

| Role | Description |
|------|-------------|
| **Call Gateway (CG)** | Phone/PC with telephone network connection |
| **Call Terminal (CT)** | Headset for conversational audio (uses CCP + BAP) |
| **Unicast Media Sender (UMS)** | Streams media to a UMR (phone, TV, PC) |
| **Unicast Media Receiver (UMR)** | Receives media audio (headphones, earbuds, speaker) |
| **Broadcast Media Sender (BMS)** | Broadcasts audio using BAP Broadcast Source |
| **Broadcast Media Receiver (BMR)** | Receives broadcast audio |

**Mandatory LC3 Configurations** `[TMAP v1.0.1, §3.2–3.7]`:
- CG/CT call: 16 kHz, 32 kbps per channel, 7.5 ms or 10 ms frame
- UMS/UMR media: 48 kHz, 96 kbps stereo, 10 ms frame
- BMS/BMR broadcast: 48 kHz, 96 kbps, PBP HQ config

**Dependencies**: CAP, BAP, VCP, MICP, CSIP, CCP (for CG/CT), MCP (for UMS/UMR)

**Version History**: v1.0 (2022-06-11) → **v1.0.1** (2025-02-11, 4 errata)

---

## Auracast™ (Broadcast Audio)

Auracast is the Bluetooth SIG marketing name for **Public Broadcast Audio** based on BIS.

- **Discovery**: Uses Periodic Advertising (PA) to broadcast audio metadata (BASE — Broadcast Audio Source Endpoint).
- **Encryption**: Open (no encryption) or secured with a shared **Broadcast_Code** distributed out-of-band.
- **PAwR (5.4+)**: Enables bidirectional broadcast control for large-scale deployments (e.g., hearing loops, digital signage with ESL tags).

---

## Developer Impact and Migration

| Feature | Implementation Detail |
|---------|-----------------------|
| **Latency** | Configurable via `Max_Transport_Latency` and `Presentation_Delay` in BAP QoS negotiation |
| **Synchronization** | All devices in a CIG/BIG are synchronized to within a few microseconds of each other |
| **USB (6.2)** | Core 6.2 normatively specified ISO data over USB transport `[Core 6.2, Vol 4, Part B]` |

### HCI Command Sequences

#### Unicast Audio (CIS) Setup

1. **Central**: `HCI_LE_Set_CIG_Parameters` → `HCI_LE_Create_CIS`
2. **Peripheral**: `HCI_LE_Accept_CIS_Request` (triggered by `HCI_LE_CIS_Request` event)
3. **Both**: `HCI_LE_Setup_ISO_Data_Path` (configures codec and data path direction)

#### Broadcast Audio (BIS) Setup

1. **Source**: `HCI_LE_Set_Extended_Advertising_Parameters` → `HCI_LE_Set_Periodic_Advertising_Parameters` → `HCI_LE_Create_BIG`
2. **Sink**: `HCI_LE_Periodic_Advertising_Create_Sync` → `HCI_LE_BIG_Create_Sync`
3. **Both**: `HCI_LE_Setup_ISO_Data_Path`

Key events:
- `HCI_LE_CIS_Established` — CIS connection ready
- `HCI_LE_BIG_Complete` — BIG created successfully
- `HCI_LE_BIG_Sync_Established` — Sink synchronized to BIG

---

## Version History

| Version | Change |
|---------|--------|
| **5.2** | LE Audio foundation: LC3 mandate, Isochronous Channels (CIS/BIS/CIG/BIG), ISOAL, EATT `[Core 5.2, Vol 6, Part B]` |
| **6.0** | ISOAL Unsegmented Framed Mode (lower framing overhead for fixed-size audio SDUs) `[Core 6.0, Vol 6, Part G, §2](../../sources/specs/6.0/Core_v6.0.md#L74377)` |
| **6.2** | Normative HCI USB LE Isochronous support (ISO data over USB transport) `[Core 6.2, Vol 4, Part B]` |

---

## References
- Isochronous Channels: `[Core 5.2, Vol 6, Part B]`
- ISOAL: `[Core 6.2, Vol 6, Part G]`
- EATT (Parallel GATT): `[Core 5.2, Vol 3, Part F, §3.2]`
- BAP/CAP/TMAP/HAP: Bluetooth SIG Profile Specification Repository (bluetooth.com/specifications)

## See Also
- [BLE Architecture](ble-architecture.md)
- [Profiles and Services](profiles-and-services.md)
- [Security](security.md)
