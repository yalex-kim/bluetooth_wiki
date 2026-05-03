# LE Audio Framework

**Last updated**: 2026-05-03
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

Unlike Classic Audio, LE Audio uses a modular GATT-based architecture with clearly separated roles:

### Basic Audio Profile (BAP)

Foundation profile defining procedures for setting up and controlling both unicast and broadcast audio streams. `[BAP v1.0.1, Bluetooth SIG]`

- **Unicast Client**: Initiates CIS setup; configures ASEs on the Server.
- **Unicast Server**: Accepts CIS; exposes Audio Stream Endpoints (ASEs).
- **ASE (Audio Stream Endpoint)**: GATT characteristic representing a single audio stream slot with a state machine (Idle → Codec Configured → QoS Configured → Enabling → Streaming → Disabling → Releasing).
- **Broadcast Source**: Creates a BIG and transmits BIS data.
- **Broadcast Sink**: Synchronizes to a BIG and receives BIS data.
- **Scan Delegator / Broadcast Assistant**: Auracast coordination roles allowing a phone to delegate scanning to a hearing aid.

### Common Audio Profile (CAP)

Handles orchestration across multiple devices. Ensures synchronized command delivery so a pair of earbuds (left/right) behaves as a single system. `[CAP v1.0, Bluetooth SIG]`

- **Commander Role**: Controls device that initiates/stops unicast or broadcast audio and adjusts volume.
- **CSIS (Coordinated Set Identification Service)**: Groups multiple independent devices into a logical set (e.g., a stereo earbud pair) so the Commander can address them together.

### TMAP and HAP

- **TMAP (Telephony and Media Audio Profile)**: Defines minimum codec parameters and QoS settings for phone calls and media playback to ensure cross-vendor interoperability. `[TMAP v1.0, Bluetooth SIG]`
- **HAP (Hearing Access Profile)**: Specialized audio transport specification for hearing aids and assisted listening devices, optimized for ultra-low latency and reliability. `[HAP v1.0, Bluetooth SIG]`

### Audio Control Profiles

| Profile | Purpose |
|---------|---------|
| **VCP** (Volume Control Profile) | Unified volume control across LE Audio devices |
| **MCP** (Media Control Profile) | Playback, pause, seek commands |
| **CCP** (Call Control Profile) | Call accept/reject and call state management |

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
