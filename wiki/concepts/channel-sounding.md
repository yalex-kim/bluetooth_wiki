# Channel Sounding (CS)

**Last updated**: 2026-05-03
**Covers**: Precise distance measurement introduced in Core Spec 6.0 through 6.2

---

## Overview

**Channel Sounding (CS)** is a feature introduced in **Bluetooth Core Specification 6.0** that enables high-accuracy distance measurement (ranging) between two Bluetooth LE devices. It achieves centimeter-level precision, significantly surpassing previous RSSI-based or Path Loss methods.

Key applications:
- **Digital Keys**: Secure vehicle access and building entry (PACS).
- **Find My**: High-precision item finding.
- **Indoor Navigation**: Accurate positioning in complex environments.
- **Proximity Services**: Real-time distance-based automation.

---

## Core Technologies

Channel Sounding utilizes two primary methods for distance calculation to ensure both accuracy and security:

### 1. PBR (Phase-Based Ranging)

Uses the phase of the unmodulated carrier signal (CS_TONE) across multiple frequencies to calculate distance.

- **Mathematics**: Distance is derived from the rate of change of phase with respect to frequency ($d\phi/df$). At the reflector and initiator, the measured amplitudes $A_{REFL}(f)$ and $A_{INIT}(f)$ are used together with phase to compute the range. `[Core 6.0, Vol 6, Part H, §4.3.3]`
- **Ambiguity**: 150 m at 1 MHz frequency spacing; reduced by combining multiple tones.
- **Precision**: Centimeter-level in line-of-sight (LOS) conditions.

### 2. RTT (Round Trip Time)

Measures the time of flight of **CS_SYNC** packets between the two devices.

- **Formula**: $d = (T_{initiator} - 2 \cdot T_{reflector}) \cdot c / 2$.
- **Robustness**: Provides a sanity check for PBR; effective in multi-path / NLOS where phase is noisy.
- `[Core 6.0, Vol 1, Part A, §9.3]`

---

## Architecture

CS runs over a dedicated **LE Channel Sounding physical channel** established on top of an existing ACL connection.

### Hierarchical Structure

| Level | Description |
|-------|-------------|
| **CS Procedure** | High-level ranging operation configured via HCI |
| **CS Event** | A window of time for CS activity (one per connection event slot) |
| **CS Subevent** | Contains an ordered sequence of steps; first steps are calibration (Mode 0) |
| **CS Step** | Atomic unit — one frequency, one mode |

### Step Modes 0–3

`[Core 6.0, Vol 6, Part H, §4.3]`

#### Mode 0 — Calibration

The **first steps of every CS subevent** are Mode-0 steps used to calibrate frequency offset and timing between initiator and reflector.

Structure: `CS_SYNC_0_I → T_RD → T_IP1 → CS_SYNC_0_R + CS_Tone → T_RD`

Timing components:
- **T_FCS** — Frequency change setup; devices may perform internal calibrations during this period.
- **T_IP1** — Inter-step idle period after Mode-0; devices may use this for additional internal calibrations.
- **T_FM = 80 µs** — Frequency measurement period embedded in the Mode-0 exchange.

Duration formula: `2×T_SY + 2×T_RD + T_GD + T_FM + T_IP1`

#### Mode 1 — RTT Only

Exchanges **CS_SYNC_1** packets (optionally carrying a sounding or random sequence payload) to measure round-trip time.

Duration formula: `2×T_SY + 2×T_RD + T_IP1`

#### Mode 2 — PBR Tones Only

Exchanges **CS_TONE** (unmodulated carrier) between initiator and reflector. The phase of each received tone is measured during the **T_PM** period.

**T_PM (Phase Measurement Period)**:
- Duration options: **10 µs** (optional), **20 µs** (conditional), **40 µs** (mandatory).
- Each T_PM period starts and ends with a ≥1 µs exclusion zone to compensate for peer device timing error.
- Devices perform **N_AP + 1** phase measurements per T_PM period — one per antenna path plus one extension slot.
- Total tone duration: `(T_SW + T_PM) × (N_AP + 1)`, where T_SW is the antenna switch duration.

Duration formula: `2×T_PM + T_SW×(N_AP + 1) + 2×T_RD + T_IP2`

`[Core 6.0, Vol 6, Part H, §4.3.3]`

#### Mode 3 — RTT + PBR Combined

Combines Mode-1 and Mode-2 in a single step: `(CS_SYNC + CS_Tone) → T_RD → T_IP2 → (CS_Tone + CS_SYNC) → T_RD`

Duration formula: `2×T_SY + T_GD + 2×T_PM + T_SW×(N_AP + 1) + 2×T_RD + T_IP2`

---

## Physical Layer

### LE 2M 2BT PHY

Channel Sounding introduces a specialized PHY variant using a **BT=2.0** Gaussian filter (standard LE 2M uses BT=0.5) to improve tone quality and RTT pulse shaping.
- Used exclusively for CS_SYNC and CS_TONE transmissions.
- Not usable for general data logical transports.
- `[Core 6.0, Vol 6, Part A, §3.1.2]`

### CS Packet Types

| Packet | Description |
|--------|-------------|
| **CS_SYNC** | GFSK-modulated packet (LE 1M or LE 2M 2BT PHY) used for RTT; carries Access Address and optional sounding/random sequence |
| **CS_TONE** | ASK-modulated unmodulated carrier used for PBR phase measurements |

Five CS_SYNC variants exist: `CS_SYNC_0_I`, `CS_SYNC_0_R`, `CS_SYNC_1`, `CS_SYNC_3_I`, `CS_SYNC_3_R`.

### Antenna Paths

CS supports **up to 4 antenna paths** (N_AP). Multiple antenna paths enable angular diversity and improve phase measurement accuracy in multi-path environments. The antenna switching pattern is controlled by the CS-DRBG and is exchanged during capability negotiation.

`[Core 6.0, Vol 6, Part H, §4.6]`

---

## Security and Resilience

CS is specifically designed to resist **Relay Attacks** (adversary physically placed between devices to inflate measured distance).

### 1. CS-DRBG (Randomization)

A Deterministic Random Bit Generator randomizes:
- Channel hopping sequence
- Step modes within a subevent
- Antenna switching order
- CS Access Address

This prevents an attacker from predicting upcoming step parameters. `[Core 6.0, Vol 6, Part H, §2]`

### 2. Timing Consistency (RTT Anti-Relay)

Relay hardware introduces an unavoidable propagation delay. CS RTT measurements detect this additional latency by requiring the reflector's turnaround time to fall within tight, agreed-upon bounds. Any deviation beyond the expected range indicates relay activity. `[Core 6.0, Vol 6, Part H, §5]`

### 3. Amplitude-based Attack Resilience (Core 6.2)

A sophisticated relay attack can synchronize an amplification pattern with the symbol timing grid to create **amplitude-to-phase distortion**, making the received signal appear time-advanced compared to the legitimate signal.

**Detection mechanism**: The receiver computes a **DFT (Discrete Fourier Transform) metric** over the received CS_SYNC waveform:

$$\text{DFT metric} = 20 \times \log_{10}\left[\frac{\varphi(f_1) + \varphi(f_2)}{\varphi(0)}\right]$$

where $f_1$ = symbol rate and $f_2$ = double symbol rate. A larger DFT metric value indicates higher probability of an active amplitude attack.

- Applies to **Mode-1 and Mode-3** CS steps (CS_SYNC with sounding or random sequence).
- The raw detector output is called **NADM (Normalized Attack Detector Metric)**.
- Reported in the `HCI_LE_CS_Subevent_Result` event via the PCT (Phase and Carrier Tone) amplitude field.
- Core 6.2 makes this a **Type 3 optional feature** mandatory for all CS-capable implementations.

`[Core 6.2, Vol 6, Part H, §5]`

---

## HCI Command Reference

`[Core 6.0, Vol 4, Part E, §7.8.x]`

| Command | Purpose |
|---------|---------|
| `HCI_LE_CS_Read_Local_Supported_Capabilities` | Query own CS capabilities (roles, modes, PHYs, antenna count) |
| `HCI_LE_CS_Read_Remote_Supported_Capabilities` | Query peer CS capabilities (async, triggers event) |
| `HCI_LE_CS_Write_Cached_Remote_Supported_Capabilities` | Cache previously read peer capabilities |
| `HCI_LE_CS_Security_Enable` | Initiate CS security handshake (CS-DRBG key agreement) |
| `HCI_LE_CS_Set_Default_Settings` | Set default roles, sync PHY, and antenna configuration |
| `HCI_LE_CS_Read_Remote_FAE_Table` | Read peer Frequency Actuation Error table (channel corrections) |
| `HCI_LE_CS_Write_Cached_Remote_FAE_Table` | Write cached FAE table for peer |
| `HCI_LE_CS_Create_Config` | Create a CS configuration (step modes, channel map, T_PM, etc.) |
| `HCI_LE_CS_Remove_Config` | Delete a CS configuration |
| `HCI_LE_CS_Set_Channel_Classification` | Mark channels as good/bad for CS channel map |
| `HCI_LE_CS_Set_Procedure_Parameters` | Set procedure timing (max duration, repetitions, intervals) |
| `HCI_LE_CS_Procedure_Enable` | Start or stop a CS procedure |
| `HCI_LE_CS_Test` | Run a single CS step for testing (no peer device required) |
| `HCI_LE_CS_Test_End` | Terminate an ongoing CS test |

Associated events: `HCI_LE_CS_Read_Remote_Supported_Capabilities_Complete`, `HCI_LE_CS_Read_Remote_FAE_Table_Complete`, `HCI_LE_CS_Security_Enable_Complete`, `HCI_LE_CS_Config_Complete`, `HCI_LE_CS_Procedure_Enable_Complete`, `HCI_LE_CS_Subevent_Result`, `HCI_LE_CS_Subevent_Result_Continue`, `HCI_LE_CS_Test_End_Complete`.

---

## Link Layer Procedures

| LL PDU | Purpose |
|--------|---------|
| `LL_CS_CAPABILITIES_REQ/RSP` | Negotiate supported CS roles, modes, PHY, antenna count |
| `LL_CS_CONFIG_REQ/RSP` | Exchange CS configuration parameters |
| `LL_CS_FAE_REQ/RSP` | Exchange Frequency Actuation Error tables |
| `LL_CS_SEC_REQ/RSP` | CS security key exchange |

`[Core 6.0, Vol 6, Part B, §5.1.23]`

---

## Version History

| Version | Change |
|---------|--------|
| **6.0** | Channel Sounding introduced: PBR, RTT, Modes 0–3, CS-DRBG, NADM baseline |
| **6.2** | CS Amplitude-based Attack Resilience (Type 3 mandatory for CS devices): DFT metric / NADM support for amplitude attack detection |

---

## References
- Architecture overview: `[Core 6.0, Vol 1, Part A, §9]`
- Physical channel and step timing: `[Core 6.0, Vol 6, Part H, §4.3]`
- T_PM and antenna measurements: `[Core 6.0, Vol 6, Part H, §4.6]`
- CS-DRBG security: `[Core 6.0, Vol 6, Part H, §2]`
- Amplitude resilience: `[Core 6.2, Vol 6, Part H, §5]`
- HCI commands: `[Core 6.0, Vol 4, Part E, §7.8]`

## See Also
- [BLE Architecture](ble-architecture.md)
- [Direction Finding](direction-finding.md)
- [Security](security.md)
