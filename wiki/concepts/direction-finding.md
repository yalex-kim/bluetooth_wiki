# Direction Finding (AoA / AoD)

**Last updated**: 2026-05-02
**Covers**: Bluetooth Direction Finding introduced in Core Spec 5.1

---

## Overview

**Direction Finding** is a major feature introduced in **Bluetooth Core Specification 5.1** that allows devices to determine the direction of a Bluetooth signal, not just its presence or signal strength (RSSI). This enables high-precision indoor positioning and proximity services with sub-meter accuracy.

Key applications:
- **Item Finding**: Locating lost keys or wallets with directional guidance.
- **Asset Tracking**: Real-time tracking of equipment in warehouses.
- **Indoor Navigation**: Precise turn-by-turn navigation inside buildings (malls, airports).
- **Wayfinding**: Point-of-interest information based on where a user is facing.

---

## Core Technologies

Direction Finding relies on measuring the phase difference of a signal as it arrives at or departs from an antenna array.

### 1. AoA (Angle of Arrival)
The transmitter (e.g., a simple beacon) sends a signal from a single antenna. The receiver (e.g., a fixed locator) has an **antenna array**. 
- The receiver switches between antennas to sample the signal's phase.
- By calculating the phase shift across the array, the receiver determines the angle of the incoming signal.
- `[Core 5.1, Vol 6, Part B, §6.1](../../sources/specs/5.1/Core_v5.1.md#L58386)`

### 2. AoD (Angle of Departure)
The transmitter (e.g., a fixed locator) has an **antenna array** and switches between them while sending the signal. The receiver (e.g., a smartphone) has a single antenna.
- The transmitter provides antenna switching information in the packet.
- The receiver samples the phase and calculates the angle at which the signal departed from the transmitter.
- `[Core 5.1, Vol 6, Part B, §6.2](../../sources/specs/5.1/Core_v5.1.md#L58392)`

---

## Constant Tone Extension (CTE)

Direction Finding requires a stable signal for phase sampling. This is achieved via the **Constant Tone Extension (CTE)**.

- **Structure**: A sequence of unwhitened "1"s appended to the end of a standard LE PDU (after the CRC).
- **Duration**: Configurable from 16 µs to 160 µs (in 8 µs increments).
- **PHY Support**: Available on **LE 1M** and **LE 2M** PHYs.
- **Format**: CTE is not encrypted or whitened, ensuring the carrier frequency remains constant for phase measurement.
- `[Core 5.1, Vol 6, Part B, §2.5](../../sources/specs/5.1/Core_v5.1.md#L56619)`

---

## IQ Sampling and Antenna Switching

The Link Layer manages the timing of IQ sampling relative to antenna switching.

### Sampling Slots
- **Switching Slot**: 1 µs or 2 µs window where the radio switches antennas (data is ignored).
- **Sample Slot**: 1 µs or 2 µs window where the receiver's ADC captures **I (In-phase)** and **Q (Quadrature)** components.
- The resulting IQ samples are passed to the Host for angle calculation (trigonometry based on antenna geometry).

### Reference Period
The first 8 µs of the CTE is the **Reference Period**. During this time, no antenna switching occurs, allowing the receiver to measure the baseline frequency and phase of the transmitter.

---

## Architectural Impact

| Layer | Responsibility |
|-------|----------------|
| **PHY** | Support for CTE transmission and IQ sampling hardware. |
| **Link Layer** | Managing CTE timing, antenna switching patterns, and IQ sample reporting. |
| **HCI** | New commands for configuring CTE and reporting IQ samples to the Host. |
| **Host/App** | Implementation of positioning algorithms (AoA/AoD calculation) based on raw IQ data. |

---

## HCI Commands (Selected)

- `HCI_LE_Set_Connectionless_IQ_Sampling_Enable`
- `HCI_LE_Set_Connection_IQ_Sampling_Enable`
- `HCI_LE_Set_Direction_Finding_Predictable_Configuration`
- `HCI_LE_Connectionless_IQ_Report` (Event)

---

## References
- **Direction Finding Overview**: `[Core 5.1, Vol 1, Part A, §7](../../sources/specs/5.1/Core_v5.1.md#L5318)`
- **Link Layer Specification**: `[Core 5.1, Vol 6, Part B, §6](../../sources/specs/5.1/Core_v5.1.md#L58381)`
- **HCI Specification**: `[Core 5.1, Vol 4, Part E, §7.8]`

---

## See Also
- BLE Architecture
- Channel Sounding
- Security

---

*Source: [Core 5.1, Vol 6, Part B, §4.4.5 (AoA/AoD)](../../sources/specs/5.1/Core_v5.1.md)*