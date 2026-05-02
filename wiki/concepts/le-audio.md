# LE Audio Framework

**Last updated**: 2026-05-02
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
LC3는 LE Audio의 필수(Mandatory) 코덱으로, 기존 Classic Audio의 SBC를 대체합니다. 훨씬 낮은 비트레이트에서도 더 높은 음질을 제공하도록 설계되었습니다.

- **Sampling Rates**: 8, 16, 24, 32, 44.1, 48 kHz를 지원합니다.
- **Bitrates**: 채널당 16 kbps에서 최대 320 kbps까지 가변적으로 설정 가능합니다. (일반적으로 64~96 kbps에서 고음질 음성, 128~192 kbps에서 고품질 음악 전송)
- **Frame Durations**: 7.5 ms와 10 ms 두 가지 프레임 간격을 지원합니다.
  - **7.5 ms**: 지연 시간(Latency)을 최소화해야 하는 게이밍이나 통화에 유리합니다.
  - **10 ms**: 전송 효율이 높으며 대부분의 오디오 스트리밍 프로파일에서 기본으로 사용됩니다.
- **Efficiency**: LC3는 160 kbps 비트레이트에서 SBC 345 kbps 이상의 인지 음질을 제공합니다. 이는 라디오 대역폭 점유율을 줄여 장치의 전력 소비를 획기적으로 낮춥니다.
- **Robustness**: 강력한 **PLC (Packet Loss Concealment)** 알고리즘이 내장되어 있어, 패킷 손실이 발생하는 불안정한 RF 환경에서도 오디오 끊김이나 팝 노이즈를 효과적으로 억제합니다.
- **Bit Depth**: 16, 24, 32-bit signed integer 입력을 지원합니다.

`[LC3 Profile Specification v1.0]`

### 2. Isochronous Channels (Physical/Link Layer)
Provides the timing-critical transport for audio data.
- **CIS (Connected Isochronous Stream)**: Point-to-point (e.g., Phone to Left Earbud). Supports bi-directional data (voice calls). `[Core 6.2, Vol 6, Part B, §4.5.13]`
- **BIS (Broadcast Isochronous Stream)**: One-to-many (e.g., Public TV to all nearby listeners). Unidirectional. `[Core 6.2, Vol 6, Part B, §4.4.6]`
- **CIG/BIG**: Groups of streams (Connected/Broadcast Isochronous Groups) that share a common timing reference for synchronization.

### 3. ISOAL (Isochronous Adaptation Layer)
Resides between the Upper Stack and the Link Layer. It fragments/recombines SDU (Service Data Units) into PDU (Protocol Data Units) to fit the radio's timing requirements. `[Core 6.2, Vol 6, Part G]`

---
## LE Audio Middleware & Profiles

Unlike Classic Audio, LE Audio uses a modular GATT-based architecture:

### Basic Audio Profile (BAP)
LE Audio의 기반이 되는 프로파일로, 유니캐스트와 브로드캐스트 오디오 스트림의 설정 및 제어 절차를 정의합니다. `[BAP v1.0.1]`
- **Unicast Client/Server**: Managing CIS.
- **Broadcast Source/Sink**: Managing BIS.
- **Scan Delegator/Broadcast Assistant**: For Auracast coordination.
- **ASE (Audio Stream Endpoint)**: 스트림의 상태(Idle, Configuring, Streaming 등)를 관리하는 핵심 제어 단위입니다.

### Common Audio Profile (CAP)
다중 기기간의 오케스트레이션을 담당합니다. 이어버드 한 쌍(좌/우)이 하나의 시스템처럼 동작하도록 동기화된 명령 전송을 보장합니다. `[CAP v1.0]`
- **Commander Role**: 유니캐스트/브로드캐스트 오디오를 시작하거나 볼륨을 조절하는 제어 기기.
- **Coordinated Set Identification Service (CSIS)**: 여러 기기를 하나의 그룹으로 묶어 인식하게 합니다.

### TMAP & HAP
- **TMAP (Telephony and Media Audio Profile)**: 전화 통화와 미디어 재생 시의 최소 요구 사항 및 코덱 파라미터를 정의하여 상호운용성을 보장합니다. `[TMAP v1.0]`
- **HAP (Hearing Access Profile)**: 보청기 및 청각 보조 기기를 위한 최적화된 오디오 전송 사양입니다. `[HAP v1.0]`

### Audio Control Profiles
- **VCP (Volume Control Profile)**: 통합 볼륨 제어.
- **MCP (Media Control Profile)**: 재생, 일시정지, 탐색 명령.
- **CCP (Call Control Profile)**: 전화 수신/거절 및 통화 상태 관리.

---

## Auracast™ (Broadcast Audio)

Auracast is the marketing name for **Public Broadcast Audio** based on BIS.
- **Configuration**: Uses Periodic Advertising (PA) to broadcast audio metadata.
- **Encryption**: Can be open (no encryption) or secured with a Broadcast_Code.
- **PAwR (5.4+)**: Enables bi-directional broadcast control for complex setups like ESL or large-scale hearing loops.

---

## Developer Impact & Migration

| Feature | Implementation Detail |
|---------|-----------------------|
| **Latency** | Configurable via `Max_Transport_Latency` and `Presentation_Delay`. |
| **Sync** | Devices in the same CIG/BIG are synchronized to within a few microseconds. |
| **USB (6.2)** | Core 6.2 added native support for ISO data over USB transport. `[Core 6.2, Vol 4, Part B]` |

### HCI Command Sequences

#### Unicast Audio (CIS) Setup
1. **Central**: `HCI_LE_Set_CIG_Parameters` → `HCI_LE_Create_CIS`
2. **Peripheral**: `HCI_LE_Accept_CIS_Request` (after `HCI_LE_CIS_Request` event)
3. **Both**: `HCI_LE_Setup_ISO_Data_Path`

#### Broadcast Audio (BIS) Setup
1. **Source**: `HCI_LE_Set_Extended_Advertising_Parameters` → `HCI_LE_Set_Periodic_Advertising_Parameters` → `HCI_LE_Create_BIG`
2. **Sink**: `HCI_LE_Periodic_Advertising_Create_Sync` → `HCI_LE_BIG_Create_Sync`
3. **Both**: `HCI_LE_Setup_ISO_Data_Path`

Key Events:
- `HCI_LE_CIS_Established`
- `HCI_LE_BIG_Complete` / `HCI_LE_BIG_Sync_Established`

---

## References
- **Isochronous Channels**: `[Core 6.2, Vol 6, Part B, §4.5]`
- **EATT (Parallel GATT)**: `[Core 6.2, Vol 3, Part F, §3.2]`
- **BAP/CAP**: Refer to SIG Profile Specifications.

---

## See Also
- BLE Architecture
- Profiles and Services
- Security