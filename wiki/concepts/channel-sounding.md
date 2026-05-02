# Channel Sounding (CS)

**Last updated**: 2026-05-02
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
Uses the phase of the carrier signal across multiple frequencies to calculate distance.
- **Mathematics**: Distance is derived from the rate of change of phase with respect to frequency ($d\phi/df$).
- **Ambiguity**: 150 m ambiguity at 1 MHz frequency spacing.
- **Precision**: Highly accurate (centimeter-level) in line-of-sight (LOS) conditions.
- `[Core 6.0, Vol 1, Part A, §9.2]`

### 2. RTT (Round Trip Time)
Measures the time of flight of specialized packets between two devices.
- **Formula**: $d = (T_{initiator} - 2 \cdot T_{reflector}) \cdot c / 2$.
- **Robustness**: Provides a "sanity check" for PBR and is effective in multi-path environments where phase may be noisy.
- `[Core 6.0, Vol 1, Part A, §9.3]`

---

## Architecture

CS runs over a dedicated **LE Channel Sounding physical channel** established on top of an existing ACL connection.

### Hierarchical Structure
1. **CS Procedure**: The high-level ranging operation.
2. **CS Event**: A window of time for CS activity.
3. **CS Subevent**: Contains a sequence of steps.
4. **CS Step**: The atomic unit of CS, occurring on a specific frequency.

### Step Modes (0-3)
- **Mode 0**: Calibration / Loopback.
- **Mode 1**: RTT packets only.
- **Mode 2**: PBR tones only.
- **Mode 3**: Combined RTT and PBR.
- `[Core 6.0, Vol 6, Part H, §4.3]`

---

## Physical Layer (PHY)

**LE 2M 2BT PHY**:
Channel Sounding introduces a specialized PHY variant. It uses a **BT=2.0** Gaussian filter (standard LE 2M uses 0.5) to improve tone quality and RTT pulse shaping.
- Used exclusively for CS tones and CS_SYNC packets.
- Not usable for general data logical transports.
- `[Core 6.0, Vol 6, Part A, §3.1.2]`

---

## Security and Resilience

Channel Sounding is specifically designed to resist **Relay Attacks** (Man-in-the-Middle).

### 1. Randomization (CS-DRBG)
A Deterministic Random Bit Generator is used to randomize channel hopping, step modes, antenna switching order, and even the CS Access Address to prevent predictability.

### 2. Anti-Relay Mechanisms
- **Timing Consistency**: Detects artificial delays introduced by relay hardware.
- **Amplitude Resilience (6.2)**: Core Spec 6.2 introduced **CS Amplitude-based Attack Resilience**. It analyzes signal amplitude to detect sophisticated relay attacks that attempt to manipulate phase/time without matching expected power profiles. `[Core 6.2, Vol 6, Part H, §5]`

---

## Developer Implementation

| Requirement | Spec Reference |
|-------------|----------------|
| **Role Negotiation** | LL_CS_CAPABILITIES_REQ/RSP |
| **Config Exchange** | LL_CS_CONFIG_REQ/RSP |
| **HCI Interface** | `HCI_LE_CS_Read_Local_Supported_Capabilities` |
| **Antenna Support** | Supports up to 4 antenna paths for phase-based directionality. |

---

## References
- **Architecture Overview**: `[Core 6.0, Vol 1, Part A, §9]`
- **Link Layer Procedures**: `[Core 6.0, Vol 6, Part B, §5.1.23]`
- **Physical Channel**: `[Core 6.0, Vol 6, Part H]`

---

## See Also
- BLE Architecture
- Security
- LE Audio