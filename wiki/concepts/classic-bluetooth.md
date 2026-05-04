# Classic Bluetooth (BR/EDR)

**Last updated**: 2026-05-02
**Covers**: BR/EDR as defined in Bluetooth Core Spec through 6.2

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

Classic Bluetooth는 **FHSS(Frequency Hopping Spread Spectrum)**를 사용하여 2.4 GHz 대역의 간섭을 최소화합니다.
- **Frequency & Channeling**: 2402 MHz부터 2480 MHz까지 1 MHz 간격으로 배치된 79개의 RF 채널을 사용합니다. `[Core 6.2, Vol 2, Part A, §2]`
- **Hopping**: 초당 1600번 채널을 전환하며, 이는 Primary 기기의 클럭에 의해 결정됩니다.
- **Modulation**: 
  - **Basic Rate (BR)**: GFSK (1 Mbps)
  - **Enhanced Data Rate (EDR)**: π/4-DQPSK (2 Mbps) 및 8DPSK (3 Mbps) `[Core 6.2, Vol 2, Part A, §3]`
  
### Data Rates

| Mode | Rate | Introduced |
|------|------|-----------|
| BR (Basic Rate) | 1 Mbps | 1.0 |
| EDR 2 Mbps | 2 Mbps | 2.0+EDR |
| EDR 3 Mbps | 3 Mbps | 2.0+EDR |

---

## Network Topology

### Piconet (피코넷)
피코넷은 공유 채널을 사용하는 기기들의 집합입니다. `[Core 6.2, Vol 1, Part A, §3.2.1]`
- **Primary/Secondary**: 1개의 Primary 기기가 홉 시퀀스와 타이밍을 결정하며, 최대 7개의 활성 Secondary 기기가 참여할 수 있습니다. (Core 5.3부터 Master/Slave 용어가 Primary/Secondary로 공식 변경됨)
- **Clock Synchronization**: 모든 Secondary 기기는 Primary의 클럭($CLK$)에 자신의 오프셋을 더해 동기화합니다. `[Core 6.2, Vol 2, Part B, §8.1](../../sources/specs/6.2/Core_v6.2.md#L10013)`
- **Physical Channel**: 피코넷 내의 통신은 Primary의 Bluetooth 기기 주소(BD_ADDR)에 의해 정의된 고유한 홉 시퀀스를 따릅니다.

### Scatternet
- 한 기기가 여러 피코넷에 참여하여 데이터를 중계할 수 있는 구조입니다. `[Core 6.2, Vol 2, Part B, §8.5](../../sources/specs/6.2/Core_v6.2.md#L10180)`
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

**Baseband (베이시밴드)**: 물리 채널 관리 및 링크 제어를 담당합니다. `[Core 6.2, Vol 2, Part B]`
- **ACL (Asynchronous Connection-Oriented)**: 패킷 재전송을 지원하는 데이터 링크입니다. 비대칭 대역폭을 지원하며 일반적인 데이터 통신에 사용됩니다. `[Core 6.2, Vol 2, Part B, §3.1.2]`
- **SCO/eSCO (Synchronous Connection-Oriented)**: 대칭형, 서킷 스위칭 방식의 포인트 투 포인트 링크입니다. 주로 음성 데이터 전송에 사용되며, eSCO는 재전송 윈도우를 지원하여 품질이 더 높습니다. `[Core 6.2, Vol 2, Part B, §3.1.1]`

**LMP (Link Manager Protocol)**: 기기 간의 링크 설정, 보안(인증/암호화), 전력 제어 및 역할 전환(Role Switch)을 제어하는 프로토콜입니다. `[Core 6.2, Vol 2, Part C]`

**L2CAP (Logical Link Control and Adaptation Protocol)**: 상위 프로토콜로의 데이터 멀티플렉싱과 세그멘테이션을 담당합니다. `[Core 6.2, Vol 3, Part A]`

**SDP (Service Discovery Protocol)**: 상대 기기가 제공하는 서비스(프로파일)와 그 속성(UUID, 프로토콜 파라미터 등)을 검색하는 데 사용됩니다. `[Core 6.2, Vol 3, Part B]`

**RFCOMM**: L2CAP 위에서 RS-232 시리얼 포트를 에뮬레이션합니다. HFP, SPP 등 전통적인 시리얼 기반 프로파일의 기반이 됩니다.

---

## Audio in BR/EDR
Classic Bluetooth 오디오는 엄격한 타이밍과 예약된 대역폭을 보장하는 동기식 링크를 사용합니다.

### CVSD & mSBC Codecs
- **CVSD**: 8 kHz 샘플링의 표준 텔레포니 코덱입니다.
- **mSBC**: 16 kHz 샘플링의 와이드밴드 음성을 지원하며, HFP 1.6 이상의 Hands-Free 기기에서 사용됩니다. `[HFP 1.6+ Spec]`

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

**Secure Simple Pairing (SSP)**: Core Spec 2.1부터 도입되었으며, ECDH(Elliptic Curve Diffie-Hellman)를 사용하여 수동적 도청(Passive Eavesdropping)을 방지합니다. `[Core 6.2, Vol 2, Part H]`
- Methods: Just Works, Passkey Entry, Numeric Comparison, OOB

**Security Levels**:
- **Level 1**: 보안 없음
- **Level 2**: MITM 보호 없는 암호화 (Just Works)
- **Level 3**: MITM 보호가 포함된 암호화 (Passkey/Numeric Comparison)
- **Level 4**: P-256 기반 Secure Connections (Core 4.1+) `[Core 6.2, Vol 3, Part C, §5.2.2]`

**Encryption**: 레거시 연결에서는 E0 스트림 암호를 사용하지만, **Secure Connections**가 활성화되면 AES-CCM을 사용합니다.

---

## See Also
- BLE Architecture
- Security
- LE Audio

---

## Coexistence with BLE

Dual-mode devices share the 2.4 GHz band between BR/EDR and LE.
Key coexistence mechanisms (all in Core Spec):
- **Slot Availability Mask (SAM, 5.0+)**: BR/EDR Primary signals available/busy slots to LE scheduler
- **LE Channel Selection Algorithm #2 (5.0+)**: Better distribution to avoid BR/EDR busy slots
- Both radios typically share one antenna via time-multiplexing managed by a coexistence arbiter

---

*Source: [Core 6.2, Vol 2 (BR/EDR Controller), Vol 3, Part C (GAP)](../../sources/specs/6.2/Core_v6.2.md)*
