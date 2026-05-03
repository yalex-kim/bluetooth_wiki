# Diff: Bluetooth Core Spec 5.4 → 6.0

**From**: [Core Spec 5.4](../versions/core-spec-5.4.md) (2023-02-02)
**To**: [Core Spec 6.0](../versions/core-spec-6.0.md) (2024-08-27)

---

## At a Glance

6.0 is dominated by **Channel Sounding (CS)** — a precise distance measurement capability
that positions Bluetooth as a competitor to UWB (Ultra-Wideband) for ranging applications.
CS uses phase-based ranging and round-trip time to achieve centimeter accuracy, enabling
secure digital car keys, access control, and fine-grained asset location.
**DBAF** and **Monitoring Advertisers** are smaller but high-value additions for scanner power optimization.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **LE Channel Sounding (CS)** | New physical-layer ranging procedure using PBR (phase) and RTT (time-of-flight); defines CS physical channel and CS generic packet format | [Core 6.0, Vol 6, Part B, §4.6.41; Vol 6, Part H; Vol 1, Part A, §9] |
| **CS Step modes 0–3** | Mode-0: frequency/timing calibration; Mode-1: RTT via CS_SYNC packet; Mode-2: PBR tone exchange (IQ samples); Mode-3: combined RTT+PBR | [Core 6.0, Vol 1, Part A, §9.1; Vol 6, Part H, §4.3] |
| **CS Security / DRBG** | Cryptographic DRBG randomizes channel hop, step modes, antenna order, CS access address; key material never externally shared; relay attack detectable via RTT verification | [Core 6.0, Vol 1, Part A, §9.4; Vol 6, Part B, §5.1.23] |
| **CS Tone Quality Indication** | Optional sub-feature: per-tone quality measurement during T_PM interval | [Core 6.0, Vol 6, Part B, §4.6.42; Vol 6, Part H, §4.6] |
| **CS LL procedures** | Security Start, Capabilities Exchange, Configuration, CS Start, Repeat Termination, Channel Map Update, Mode-0 FAE Table Request | [Core 6.0, Vol 6, Part B, §5.1.23–5.1.29] |
| **LE Channel Sounding Physical Channel** | New LE physical channel type (alongside advertising, periodic, connection, isochronous); uses LE 2M 2BT PHY | [Core 6.0, Vol 1, Part A, §3.3.2; Vol 6, Part A, §3.1.2] |
| **Decision-Based Advertising Filtering (DBAF)** | Host programs decision instructions; advertisers include ADV_DECISION_IND PDUs with decision data; controller filters without host wakeup | [Core 6.0, Vol 6, Part B, §4.6.43](../../sources/specs/6.0/Core_v6.0.md#L62448) |
| **Monitoring Advertisers** | Controller notifies host when specific advertisers appear/disappear; operates independently from Filter Accept List; 4 new HCI commands | [Core 6.0, Vol 6, Part B, §4.6.45; Vol 4, Part E, §7.8.147–7.8.150] |
| **LE Frame Space Update** | Negotiate T_IFS, T_MSS_CIS, T_MCES below or above default 150 µs via LL_FRAME_SPACE_REQ/RSP | [Core 6.0, Vol 6, Part B, §4.6.46; §4.1; §5.1.30] |
| **ISOAL Unsegmented Framed Mode** | New unsegmented mode for framed ISO PDUs; reduces overhead for LE Audio streams | [Core 6.0, Vol 6, Part B, §4.6.44; Vol 6, Part G, §2.2; §3.2.1] |
| **LL Extended Feature Set** | Extended feature page exchange (LL_FEATURE_EXT_REQ/RSP) enabling >64 feature bits | [Core 6.0, Vol 6, Part B, §4.6.40](../../sources/specs/6.0/Core_v6.0.md#L62401) |

---

## Modified

| What | Change |
|------|--------|
| **Vol 0, Part B** | Replaced Compliance Requirements with Core Configurations (moved to Vol 0, Part D) |
| **Vol 1, Part A** | New §3.2.3 (CS generic packet structure), §3.3.2 (LE CS physical channel), §3.4.3 (CS physical link), Section 9 (Channel Sounding architecture) |
| **LE Features (Vol 6, Part B)** | New feature bits: CS (4.6.41), CS Tone Quality Indication (4.6.42), DBAF (4.6.43), ISOAL Unsegmented Framed Mode (4.6.44), Monitoring Advertisers (4.6.45), Frame Space Update (4.6.46), LL Extended Feature Set (4.6.40) |
| **HCI (Vol 4, Part E)** | New commands: HCI_LE_CS_* family (~15+ CS commands); HCI_LE_Set_Decision_Data; HCI_LE_Set_Decision_Instructions; HCI_LE_Add/Clear/Enable/Read Monitored Advertisers; HCI_LE_Frame_Space_Update |
| **LE Frame Space defaults** | T_IFS_150, T_MSS_150 remain fixed at 150 µs; T_IFS, T_MSS_CIS, T_MCES are negotiable per connection |
| **Scanning filter policies** | Bits 2–3 of Scanning_Filter_Policy now support DBAF mode; Initiator_Filter_Policy extended for DBAF |
| **LE physical channels** | New CS physical channel type (§3.3.2) added alongside advertising, periodic, isochronous |

---

## Deprecated / Removed

- Nothing removed. Full backward compatibility.

---

## Migration Guide

### Channel Sounding for car key / access control

CS is the most complex feature added to the Bluetooth spec to date.
[Core 6.0, Vol 6, Part B, §4.6.41; Vol 6, Part H; Vol 1, Part A, §9]

Required implementation steps:

1. **Check hardware support**: Read `LE Features` for Channel Sounding bit on local and peer controller
2. **Capabilities Exchange**: `HCI_LE_CS_Read_Remote_Supported_Capabilities` — learn peer's supported step types, antenna configurations, RTT payload types, etc. [Core 6.0, Vol 6, Part B, §5.1.24](../../sources/specs/6.0/Core_v6.0.md#L63085)
3. **Security Start** (for anti-relay): `HCI_LE_CS_Security_Enable` — initiates CS Security Start procedure; DRBG key material is exchanged under the encrypted link [Core 6.0, Vol 6, Part B, §5.1.23](../../sources/specs/6.0/Core_v6.0.md#L63067)
4. **Create CS Configuration**: `HCI_LE_CS_Create_Config` — define channel map, step modes, tone durations, RTT payload type, number of steps, main mode repetitions [Core 6.0, Vol 6, Part B, §5.1.25](../../sources/specs/6.0/Core_v6.0.md#L63094)
5. **Start procedure**: `HCI_LE_CS_Procedure_Enable` — begins CS events on the established connection [Core 6.0, Vol 6, Part B, §5.1.26](../../sources/specs/6.0/Core_v6.0.md#L63129)
6. **Process results**: `LE_CS_Subevent_Result` HCI events contain IQ samples (for PBR) and ToA/ToD values (for RTT) per step
7. **Compute distance**: Host-side algorithm applies the mathematical model (see [Core 6.0, Vol 1, Part A, §9.2–9.3]) to estimate distance

**CS measurement accuracy** depends on: [Core 6.0, Vol 1, Part A, §9.2](../../sources/specs/6.0/Core_v6.0.md#L6182)
- Number of channels and frequency span (more channels → more accurate phase unwrapping; 1 MHz spacing → 150 m ambiguity range)
- Step repetitions (main mode repetitions average out noise)
- Antenna configuration (multiple antennas improve spatial diversity)
- RTT payload type (sounding sequence or random sequence more accurate than access address only)
- RF environment (multipath reflections in indoor settings affect PBR accuracy)

**Anti-relay for PACS**: [Core 6.0, Vol 1, Part A, §9.4](../../sources/specs/6.0/Core_v6.0.md#L6229)
- CS step mode-1 and mode-3 allow detection of relay attacks via RTT; relay adds measurable propagation latency
- Mode-3 provides two independent estimates (RTT + PBR) simultaneously
- DRBG randomization prevents prediction of channel hop sequence by an attacker

### DBAF and Monitoring Advertisers for power-efficient scanning

**Before 6.0** (continuous scan in a retail environment with hundreds of BLE devices):
- Every advertising PDU wakes the host
- Host discards 99% of reports (wrong device, wrong RSSI, etc.)
- High CPU and radio duty cycle

**With DBAF**: [Core 6.0, Vol 6, Part B, §4.6.43; Vol 4, Part E]
- Advertiser includes decision data in `ADV_DECISION_IND` PDU via `HCI_LE_Set_Decision_Data`
- Scanner programs decision instructions via `HCI_LE_Set_Decision_Instructions`
- Controller must support at least 8 tests in the decision instructions
- Controller evaluates each decision PDU against the instructions; only matching PDUs wake the host
- Default behavior (on reset) is "No decisions" — controller ignores decision PDUs

```
// HCI commands for DBAF setup on scanner
HCI_LE_Set_Decision_Instructions(Num_Tests, Tests[...])
// Controller now only wakes host for PDUs passing decision tests
```

**With Monitoring Advertisers** (simpler use case: "is my device nearby?"):
[Core 6.0, Vol 6, Part B, §4.6.45; Vol 4, Part E, §7.8.147–7.8.150]
```
HCI_LE_Add_Device_To_Monitored_Advertisers_List(address)
HCI_LE_Enable_Monitoring_Advertisers(Enable)
// Host is notified only when the device first appears or disappears
// Works independently from the Filter Accept List
// Resolving List used to match Resolvable Private Addresses
```

**Key distinction**: DBAF requires advertisers to include `ADV_DECISION_IND` PDUs with
decision data — it is a cooperative filtering mechanism. Monitoring Advertisers works with
any advertising PDU from monitored devices — it is passive tracking.
