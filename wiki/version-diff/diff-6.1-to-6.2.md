# Diff: Bluetooth Core Spec 6.1 → 6.2

**From**: [Core Spec 6.1](../versions/core-spec-6.1.md) (2025-04-29)
**To**: [Core Spec 6.2](../versions/core-spec-6.2.md) (2025-11-03)

---

## At a Glance

Bluetooth 6.2 is a substantial update that introduces four new features and a critical batch of security errata. The standout feature is **Shorter Connection Intervals**, which slashes the minimum LE ACL connection interval from 7.5 ms to 375 µs — a 20× improvement that opens BLE to latency-critical applications including gaming peripherals and industrial control. **LE Unified Test Protocol** overhauls conformance test infrastructure with a connection-oriented OTA test mode. **Channel Sounding Amplitude-based Attack Resilience** closes a security gap in the 6.0 CS feature, and **HCI USB LE Isochronous Support** normalizes LE Audio data transport over USB-attached controllers. Critically, 6.2 also integrates 12 security errata that all implementations should treat as mandatory security patches.

---

## Added

- **Shorter Connection Intervals** — Reduces minimum LE ACL connection interval to 375 µs via new `LL_CONNECTION_RATE_REQ`/`LL_CONNECTION_RATE_IND` PDUs and three new HCI commands. Connection intervals are now specified in units of 125 µs (down from 1.25 ms). Requires Connection Subrating feature (5.3+). [Vol 6, Part B, §4.6.50; §5.1.32–33; Vol 4, Part E, §7.8.154–156]

- **LE Unified Test Protocol (UTP)** — New connection-oriented over-the-air (OTA) and HCI test mode enabling richer conformance testing than DTM. New LL PDU `LL_OTA_UTP_IND` carries test commands over a BLE connection; new HCI commands `HCI_LE_Enable_OTA_UTP_Mode` and `HCI_LE_UTP_Send` provide HCI mode. Classified as Type 3 optional feature. [Vol 6, Part F, §5; Vol 6, Part B, §4.6.47–49; §5.1.31; Vol 4, Part E, §7.8.152–153]

- **Channel Sounding Amplitude-based Attack Resilience** — Security hardening for CS distance measurement against amplitude manipulation attacks. Mandatory for CS-capable implementations. Classified as Type 3 optional feature. [Vol 6, Part H; Vol 0, Part D, §4]

- **HCI USB LE Isochronous Support** — Normative specification for transporting LE Isochronous data packets (CIS/BIS for LE Audio) over the USB HCI transport layer. Transport-layer change only; no LL feature bit. [Vol 4, Part B (USB transport)]

- **LE Flushable ACL Data** — Allows LE ACL data to be marked flushable with an ACL Flush Timeout, enabling stale data discard from the transmission queue. [Vol 6, Part B, §4.6.51; Vol 4, Part E, §6.19]

---

## Modified

- **Connection interval timing model** — The unit of measurement for connection intervals in the new `HCI_LE_Connection_Rate_Request` command is 125 µs (vs. 1.25 ms for the existing `HCI_LE_Connection_Update` and `HCI_LE_Connection_Parameter_Request` commands). The two systems co-exist: existing commands continue to use 1.25 ms units. [Vol 4, Part E, §7.8.154; Vol 6, Part B, §5.1.32–33]

- **HCI command set (V4E)** — Large batch of errata (50+ items) applied: command parameter validation, ISO data path, event generation, and error codes. New commands added: `HCI_LE_Connection_Rate_Request` (0x00A1), `HCI_LE_Set_Default_Rate_Parameters` (0x00A2), `HCI_LE_Read_Minimum_Supported_Connection_Interval` (0x00A3), `HCI_LE_Enable_OTA_UTP_Mode`, `HCI_LE_UTP_Send`. [Vol 4, Part E]

- **LE Link Layer (V6B)** — Errata applied to advertising, connection procedures, BIG control, PAST, and CS procedures. New LL PDUs `LL_CONNECTION_RATE_REQ`, `LL_CONNECTION_RATE_IND`, `LL_OTA_UTP_IND` defined. [Vol 6, Part B]

- **Direct Test Mode / Unified Test Protocol (V6F)** — New Unified Test Protocol (§5) added. Over 20 errata applied to DTM procedures (errata 26201, 26204, 26412, 26441, 26464–26466, 26471, 26472, 26504, 26559, 26563–26565, 26627, 26774, 27268, 27402). [Vol 6, Part F]

- **USB transport (V4B)** — LE ISO data packet transport added (HCI USB LE Isochronous Support). [Vol 4, Part B]

- **Channel Sounding (V6H)** — Amplitude-based attack resilience procedures added. Errata applied (15163, 26387, 26389, 27246, 27650, 27846, 28022). [Vol 6, Part H]

- **Security Manager (V3H)** — Security errata applied: erratum 24490 (LE Legacy Pairing insecure Passkeys), 24491 (LE Legacy Pairing reflection attack), 24557 (RNG quality), 26047 (SignCounter persistence), 15163, 26309, 26387, 26535, 27504, 26770. [Vol 3, Part H]

- **BR/EDR Security (V2H)** — Security errata applied: erratum 24489 (SSP insecure Passkeys), 26039 (min 7-octet encryption key), 26041 (no user-configurable key size), 26043 (no fixed key pairs), 26389, 26535. [Vol 2, Part H]

- **GAP (V3C)** — Errata including 26048 (zero IRK in device privacy mode), 26341, 26387, 26389, 26449, 26535, 27129, 27246, 27436, 27668, 27848, 25701. [Vol 3, Part C]

- **GATT (V3G)** — Corrections to service discovery, notification procedures, caching (errata 15163, 19172, 26387, 26535, 26873, 27431, 27628, 27718). [Vol 3, Part G]

- **ISOAL (V6G)** — Corrections to isochronous adaptation layer segmentation/reassembly (errata 24326, 26389, 26521, 27187, 27827). [Vol 6, Part G]

- **L2CAP (V3A)** — Corrections to enhanced credit-based flow control and LE credit-based connections (errata 15163, 24985, 25037, 26387, 26389, 26535, 26667, 27718, 28009). [Vol 3, Part A]

- **Core Configurations (V0D)** — New feature entries for LE Unified Test Protocol, Shorter Connection Intervals, LE Flushable ACL Data, and Channel Sounding Amplitude-based Attack Resilience added to feature tables (errata 26943, 27478, 27500). [Vol 0, Part D]

---

## Deprecated / Removed

No features were deprecated or removed in v6.2. All 6.1 features remain fully supported.

---

## Migration Guide

### Shorter Connection Intervals (high impact for latency-sensitive applications)

1. **Check controller support**: Call `HCI_LE_Read_Minimum_Supported_Connection_Interval` (0x00A3) to determine the shortest interval your controller supports. Not all 6.2 controllers will reach 375 µs — hardware capability varies.

2. **New HCI commands**: Use `HCI_LE_Connection_Rate_Request` (0x00A1) to negotiate short intervals. Note the new 125 µs time unit — interval values are 20× larger than the same time expressed in 1.25 ms units. For example, 7.5 ms = 60 (in new units) vs. 6 (in old units).

3. **Supervision timeout**: Recalculate supervision timeouts carefully. The constraint is: `Connection_Interval_Max × Subrate_Max × (Max_Latency + 1) < Supervision_Timeout × 40`. Short intervals + large latency allowances can hit this limit quickly.

4. **Prerequisites**: Controller must implement Connection Subrating (5.3) before Shorter Connection Intervals can be used.

5. **Fallback**: On 6.1 and earlier controllers, the new commands will return an error; fall back to `HCI_LE_Connection_Parameter_Request` with 7.5 ms minimum.

### LE Audio / USB (HCI USB LE Isochronous Support)

- USB host drivers (e.g., on PC/laptop platforms) should update to use the normative USB ISO packet transport rather than any prior custom extensions.
- CIS/BIS setup procedures are unchanged; only the USB framing of LE ISO data PDUs is affected.

### Channel Sounding (CS Amplitude-based Attack Resilience)

- Implementations of CS (introduced in 6.0) must add amplitude resilience mechanisms as defined in [Vol 6] Part H. This is mandatory for CS-capable devices per 6.2 configuration requirements.
- Review CS security procedures for the specific changes required.

### Security errata (all implementations — critical)

All conforming Bluetooth implementations should apply the 12 security errata incorporated in 6.2 regardless of whether they implement new 6.2 features. Priority items:

- **Erratum 24489–24491**: If your device supports pairing (BR/EDR SSP, LE Legacy, or LE Secure Connections), update the Passkey generation to use a cryptographically secure random number generator. Review whether your RNG (erratum 24557) meets the quality requirements.
- **Erratum 26039**: BR/EDR implementations must refuse connections with encryption key sizes below 7 octets.
- **Erratum 26043**: Do not persist the same ECDH public/private key pair across resets if key pair generation is supported.
- **Erratum 26047**: If your implementation uses GATT data signing, persist the SignCounter to non-volatile storage.
- **Erratum 26048**: Do not add entries with all-zero IRK to the resolving list when operating in device privacy mode.

### LE Unified Test Protocol

- Update firmware to support UTP OTA mode (feature bits 66–69) if you need connection-oriented conformance testing.
- Update host test infrastructure to use `HCI_LE_UTP_Send` for HCI mode testing.

---

*Source: [Core 6.1](../../sources/specs/6.1/Core_v6.1.md) and [Core 6.2](../../sources/specs/6.2/Core_v6.2.md)*
