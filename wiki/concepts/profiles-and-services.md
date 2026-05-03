# Bluetooth Profiles and Services

**Last updated**: 2026-05-02
**Covers**: GATT-based profiles and key BR/EDR profiles through Core Spec 6.2

---

## Overview

**Profiles** define end-to-end behavior for specific use cases, built on top of the core spec.
The Bluetooth SIG maintains a library of standardized profiles and services at bluetooth.com.

Two profile systems exist in parallel:
- **GATT Profiles** (BLE): Defined in terms of Services and Characteristics
- **BR/EDR Profiles**: Defined in terms of L2CAP channels and protocol stacks (A2DP, HFP, HID, etc.)

---

## GATT Service/Characteristic Model

GATT(Generic Attribute Profile)는 ATT(Attribute Protocol)를 기반으로 데이터의 구조를 정의합니다. GATT 서버는 **Service**, **Characteristic**, **Descriptor**로 구성된 계층적 구조를 노출합니다. `[Core 6.2, Vol 3, Part G, §2](../../sources/specs/6.2/Core_v6.2.md#L29737)`

### Hierarchy structure

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

## Unified Profile Deep-Dive (BR/EDR)

`sources/specs/`의 프로파일 명세서들을 통합 분석한 결과입니다. 버전별 파편화를 방지하기 위해 최신 사양을 기준으로 기술합니다.

### Audio

#### A2DP (Advanced Audio Distribution Profile) v1.4
- **Role**: Source (Phone) / Sink (Headset)
- **Transport**: AVDTP (Audio/Video Distribution Transport Protocol) over ACL.
- **Codec Negotiation**: SBC (Mandatory), AAC, aptX, LDAC.
- **Evolution**: v1.3.2에서 v1.4로 넘어오며 상호운용성(Interoperability) 테스트 케이스와 지연 시간 제어 메커니즘이 강화되었습니다.

#### HFP (Hands-Free Profile) v1.8
- **Role**: Audio Gateway (AG) / Hands-Free Unit (HF)
- **Audio**: SCO/eSCO 링크 사용. 
- **Wideband Speech**: mSBC 코덱(16kHz) 지원 필수 (v1.6+).
- **v1.8 Update**: 배터리 레벨 보고 및 향상된 음성 인식 제어 기능이 표준화되었습니다.

#### AVRCP (Audio/Video Remote Control Profile) v1.6.2
- **Role**: Target / Controller
- **Features**: Metadata (제목/가수), Playback status, **Absolute Volume** (v1.4+ 필수), Browsing (v1.5+).
- **v1.6.2**: 커버 아트 전송(BIP 연동) 및 검색 효율성이 개선되었습니다.

### Data / HID

#### HID (Human Interface Device) v1.1.1
- **Stack**: L2CAP (PSM 0x0011/0x0013) 위에서 동작.
- **Protocol**: USB HID 클래스 사양을 블루투스로 확장.
- **Report Map**: 기기의 버튼/축 구성을 정의하는 기술서(Descriptor).

#### SPP (Serial Port Profile) v1.2
- **Stack**: RFCOMM 기반.
- **Legacy**: 가장 단순한 형태의 데이터 전송으로, 현대에는 대부분 BLE 전용 커스텀 서비스로 대체되는 추세입니다.

### Automotive / Phone

#### PBAP (Phone Book Access Profile) v1.2.3
- **Function**: 연락처 및 통화 내역 동기화.
- **Object**: vCard 2.1/3.0 포맷 사용.

#### MAP (Message Access Profile) v1.4.2
- **Function**: SMS/MMS 및 이메일 접근.
- **v1.4 Update**: 인스턴트 메시징(IM) 서비스 지원이 추가되었습니다.

---

## Standard GATT Services (BLE)

버전별 차이가 거의 없는 핵심 서비스들의 통합 데이터 모델입니다.

| Service | UUID | Key Attributes | Version Note |
|---------|------|----------------|--------------|
| **Device Information (DIS)** | 0x180A | Model, Serial, Manufacturer, Firmware | 정적 데이터, 변화 없음 |
| **Battery Service (BAS)** | 0x180F | Battery Level (0~100) | v1.1에서 다중 배터리 지원 추가 |
| **Heart Rate (HRS)** | 0x180D | HR Measurement, Sensor Location | v1.0 이후 표준으로 고착 |
| **Human Interface (HOGP)** | 0x1812 | HID Information, Report, Protocol Mode | BLE용 HID (Core 4.0+) |

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
