# Bluetooth Core Specification 6.2

**Release Date**: 2025-11-03
**Status**: Active (current as of 2026-05)
**Spec Volume**: ~3900 pages
**Source PDF**: [Local PDF](../../sources/specs/core-spec-6.2.pdf) | [Local Markdown](../../sources/specs/core-spec-6.2.md)

---

## Executive Summary

Bluetooth Core Specification 6.2, released on 2025-11-03, is a significant incremental release that introduces four new features alongside a comprehensive set of errata and security fixes. The four features span the low-latency connection layer, test and conformance infrastructure, Channel Sounding security hardening, and HCI transport improvements for LE Audio.

**Shorter Connection Intervals** is the highest-impact feature: it dramatically reduces the minimum LE ACL connection interval from the classic 7.5 ms down to 375 µs (a 20× reduction). This is achieved through two new LL PDUs (`LL_CONNECTION_RATE_REQ` / `LL_CONNECTION_RATE_IND`) and new HCI commands, requiring the Connection Subrating feature as a prerequisite. It enables ultra-low-latency BLE applications — gaming peripherals, haptic feedback, industrial control — that previously required proprietary approaches or competitor technologies.

**LE Test Mode Enhancements (LE Unified Test Protocol / UTP)** introduces a new over-the-air test framework that complements the existing Direct Test Mode (DTM). The Unified Test Protocol provides both an OTA mode (using new LL PDUs transmitted over a BLE connection) and an HCI mode, enabling richer, connection-oriented conformance testing without the setup complexity of DTM.

**Channel Sounding Amplitude-based Attack Resilience** hardens the Channel Sounding (CS) distance measurement feature introduced in 6.0 against a class of physical-layer attack that attempts to manipulate measured distances by injecting specially crafted amplitude signals. This security enhancement is classified as a Type 3 optional feature.

**HCI USB LE Isochronous Support** adds native support for transporting LE Isochronous data (CIS and BIS streams, used by LE Audio) over the USB HCI transport layer, addressing a gap that previously required workarounds for USB-attached Bluetooth controllers carrying audio data.

Version 6.2 also incorporates a substantial batch of security errata (12 items covering passkey generation vulnerabilities, DHKey validation, IRK zeroing attacks, and signing counter persistence) and a broad set of general errata across virtually all specification sections.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Shorter Connection Intervals | Reduces minimum LE ACL connection interval to 375 µs (from 7.5 ms); adds `LL_CONNECTION_RATE_REQ/IND` PDUs and new HCI commands | Vol 6, Part B, §4.6.50; §5.1.32–33; Vol 4, Part E, §7.8.154–156 |
| LE Unified Test Protocol (UTP) | New OTA and HCI test mode enabling connection-oriented conformance testing via LL PDUs and HCI commands | Vol 6, Part F, §5; Vol 4, Part E, §7.8.152–153; Vol 6, Part B, §4.6.47–49; §5.1.31 |
| Channel Sounding Amplitude-based Attack Resilience | Security hardening for CS distance measurement against amplitude manipulation attacks | Vol 6, Part H (CS security); Vol 0, Part D, §4 (feature type 3) |
| HCI USB LE Isochronous Support | Adds LE ISO data packet transport over the USB HCI transport layer, enabling CIS/BIS streams over USB-attached controllers | Vol 4, Part B (USB transport) |
| LE Flushable ACL Data | Allows LE ACL data packets to be marked flushable, enabling timeout-based discard of stale data from the transmission queue | Vol 6, Part B, §4.6.51; Vol 4, Part E, §6.19 |

---

## Key Changes to Existing Mechanisms

### Shorter Connection Intervals

Prior to 6.2, the minimum LE ACL connection interval was 7.5 ms (specified as N × 1.25 ms with N ≥ 6). This limit stemmed from baseband timing constraints defined when BLE was designed primarily for low-power sensor applications.

Version 6.2 adds a parallel connection rate negotiation path built on top of the existing Connection Subrating mechanism (introduced in 5.3). The key change is that the **connection interval unit is reduced from 1.25 ms to 125 µs**, and the minimum interval is now N × 125 µs with N ≥ 3, allowing intervals as short as **375 µs**.

**New LL PDUs:**
- `LL_CONNECTION_RATE_REQ` — either Central or Peripheral requests a new connection rate
- `LL_CONNECTION_RATE_IND` — Central sends confirmed parameters to Peripheral

**New HCI commands (Vol 4, Part E):**

| Command | OCF | Purpose |
|---------|-----|---------|
| `HCI_LE_Connection_Rate_Request` | 0x00A1 | Request a connection rate change (Central or Peripheral) |
| `HCI_LE_Set_Default_Rate_Parameters` | 0x00A2 | Set default acceptable rate parameters for incoming requests |
| `HCI_LE_Read_Minimum_Supported_Connection_Interval` | 0x00A3 | Query the controller's minimum supported interval |

**New HCI event:**
- `HCI_LE_Connection_Rate_Change` (subevent 0x37) — confirms updated parameters

The `HCI_LE_Connection_Rate_Request` command takes `Connection_Interval_Min/Max` (in units of 125 µs), `Subrate_Min/Max`, `Max_Latency`, `Continuation_Number`, and `Supervision_Timeout`. A controller advertises its minimum supported interval via `HCI_LE_Read_Minimum_Supported_Connection_Interval`, since the hardware capability varies.

**Prerequisites:** Controller must support Connection Subrating (feature bit from 5.3). Feature advertised as "Shorter Connection Intervals" (feature type 2) in LE Feature Set [Vol 6, Part B, §4.6.50].

### LE Unified Test Protocol (UTP)

The existing Direct Test Mode (DTM) requires a dedicated physical test interface and is limited to unconnected advertising/scanning mode testing. The Unified Test Protocol (UTP) introduces two complementary test paths:

**OTA mode** (Over The Air):
- Uses a BLE connection between the tester and the device under test (IUT)
- New LL PDUs: `LL_OTA_UTP_IND` (carrying test commands and data)
- New LL procedure: **UTP OTA mode procedure** ([Vol 6] Part B, §5.1.31)
- Supports variable CtrData lengths: 26, 80, 180, or 250 octets depending on feature bits 68 and 69

**HCI mode**:
- Uses HCI commands to inject test traffic
- New HCI commands: `HCI_LE_Enable_OTA_UTP_Mode`, `HCI_LE_UTP_Send`

Feature capability is reported via three feature bits in the LE feature set:
- Bit 66: UTP OTA mode
- Bit 67: UTP HCI mode
- Bits 68–69: `LL_OTA_UTP_IND` maximum CtrData length

**New sections:** [Vol 6] Part F, §5 (Unified Test Protocol); [Vol 6] Part B, §4.6.47–49 (feature requirements)

### Channel Sounding Amplitude-based Attack Resilience

Channel Sounding (introduced in 6.0) measures distances using two methods: phase-based ranging (PBR) and round-trip time (RTT). A theoretical attack class exploits the amplitude of received tones to bias distance measurements, potentially allowing an attacker to make a device appear closer (useful for relay attacks on PACS digital car keys).

This feature adds mandatory resilience mechanisms within the CS procedure to detect and mitigate amplitude manipulation attacks. Specific changes are in [Vol 6] Part H (CS Security). The feature is classified as **Type 3** (mandatory for CS-capable implementations) in [Vol 0] Part D, §4.

### HCI USB LE Isochronous Support

LE Audio (introduced in 5.2) uses isochronous channels (CIS for connected streams, BIS for broadcast) to carry audio data. The USB HCI transport ([Vol 4] Part B) previously only specified how to carry ACL, SCO/eSCO, and HCI event data over USB. LE ISO data packets were not covered by the USB transport specification, requiring implementations to use custom extensions.

Version 6.2 adds normative specification for carrying **LE Isochronous Data Packets** over the USB HCI transport layer, ensuring interoperability between USB-attached Bluetooth controllers and LE Audio host stacks.

This feature has no Link Layer feature bit; it is a transport-layer specification change classified as "n/a" in the feature type table.

---

## Deprecated / Removed

No features were deprecated or removed in v6.2. All features from v6.0 and v6.1 remain fully supported.

---

## Security Errata (Critical)

Version 6.2 incorporates 12 security errata that **SHALL** be addressed in conforming implementations. These are particularly significant and should be treated as security patches:

| Erratum | Summary |
|---------|---------|
| 24489 | SSP and BR/EDR Secure Connections may generate insecure Passkeys |
| 24490 | LE Legacy Pairing and LE Secure Connections may generate insecure Passkeys |
| 24491 | LE Legacy Pairing may be vulnerable to reflection attacks on pairing values |
| 24557 | Security procedures may use insufficiently secure random number generators |
| 24558 | Controller may offer valid DHKey in response to invalid peer public key |
| 24560 | SDP Server may accept invalid continuation state |
| 26039 | BR/EDR baseband encryption key size shall be at least 7 octets |
| 26041 | Implementations shall not permit user-configurable encryption key size |
| 26043 | Implementations shall not retain fixed public/private key pairs |
| 26047 | Implementations shall store last verified SignCounter if data signing is used |
| 26048 | Implementations shall not populate resolving list with zero IRK in device privacy mode |
| 26770 | Fix contradiction in legacy passkey entry security assessment |

These errata address vulnerabilities in pairing (both BR/EDR and LE), key generation, SDP, and privacy. All Bluetooth implementations should update to incorporate these fixes regardless of whether they implement the new 6.2 features.

---

## Developer Impact

**Ultra-low latency applications (Shorter Connection Intervals):**
- Call `HCI_LE_Read_Minimum_Supported_Connection_Interval` to determine controller capability before requesting short intervals.
- Intervals below 7.5 ms require new HCI commands (0x00A1–0x00A3); fall back to existing connection parameter request for 6.1 and earlier controllers.
- Supervision timeout constraints become critical at short intervals: `Connection_Interval_Max × Subrate_Max × (Max_Latency + 1) < Supervision_Timeout × 40`.
- Controllers supporting Shorter Connection Intervals must also support Connection Subrating (5.3+).
- Expected use cases: gaming peripherals targeting sub-1ms perceived latency over BLE, industrial control loops, audio synchronization below LE Audio latency targets.

**LE Audio / USB transport (HCI USB LE Isochronous Support):**
- Host stacks and drivers for USB-attached controllers (PC/laptop Bluetooth adapters) should update USB transport handling to use the new normative LE ISO packet transport.
- This unblocks USB LE Audio implementations that previously relied on implementation-specific behavior.

**Conformance testing (LE UTP):**
- Update test suites and IUT firmware to support UTP OTA mode and/or UTP HCI mode.
- Report UTP feature bits (66–69) correctly in the LE Feature Set.

**Channel Sounding implementations:**
- Implement Amplitude-based Attack Resilience if implementing CS (it is mandatory for CS-capable devices in 6.2).
- Review [Vol 6] Part H for the specific CS procedure changes.

**Security (all implementations — critical):**
- Apply all 12 security errata immediately. Erratum 24489–24491 address Passkey vulnerabilities in both BR/EDR and LE pairing. Erratum 26039 mandates minimum 7-octet BR/EDR encryption keys.
- Review erratum 24557 (RNG quality) and 26043 (key pair persistence) for hardware security implications.

---

## Cross-References

- See also: [diff-6.1-to-6.2](../version-diff/diff-6.1-to-6.2.md)
- Previous version: [core-spec-6.1](core-spec-6.1.md)
- Related concepts: [Security / Privacy](../concepts/security.md), [BLE Architecture](../concepts/ble-architecture.md)
- Channel Sounding: [core-spec-6.0](core-spec-6.0.md) (introduced), [diff-5.4-to-6.0](../version-diff/diff-5.4-to-6.0.md)
