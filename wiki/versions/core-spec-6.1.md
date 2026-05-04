# Bluetooth Core Specification 6.1

**Release Date**: 2025-04-29
**Status**: Active
**Spec Volume**: ~3820 pages
**Source**: [Local Markdown](../../sources/specs/6.1/Core_v6.1.md)

---

## Executive Summary

Bluetooth Core Specification 6.1 is a focused, incremental release issued on 2025-04-29 that introduces a single new feature — **Randomized RPA (Resolvable Private Address) Updates** — along with a substantial batch of errata corrections applied across virtually every section of the specification.

The Randomized RPA Updates feature addresses a known privacy weakness in BLE device tracking. Prior to 6.1, the `HCI_LE_Set_Resolvable_Private_Address_Timeout [v1]` command set a fixed timeout for how long the controller would use a given RPA before generating and switching to a new one. Because this timeout was deterministic and identical across all packets from a device, an observer could correlate address rotations across advertising events to re-identify the device. Version 6.1 adds a new `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` command that replaces the single fixed timeout with a **randomized range** (`RPA_Timeout_Min` and `RPA_Timeout_Max`). The controller picks a fresh random timeout within that range each time a new RPA is generated, making temporal correlation attacks significantly harder.

Beyond this feature addition, 6.1 incorporates a comprehensive set of errata that collectively fix ambiguities and bugs across the Link Layer (V6B), HCI (V4E), Channel Sounding (V6H), GAP (V3C), ATT/GATT (V3F, V3G), Security Manager (V3H), and many other sections. No features were removed or deprecated in 6.1.

For most developers, the primary upgrade work is the optional adoption of the v2 RPA timeout command to improve the privacy of products that already implement LE privacy. Firmware and host stack updates should also incorporate errata fixes integrated in this release.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Randomized RPA Updates | Adds `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` command accepting `RPA_Timeout_Min` and `RPA_Timeout_Max` so the controller randomizes how long each RPA is used, defeating timing-based re-identification | Vol 4, Part E, §7.8.45 (v2 command, OCF 0x009E) |

---

## Key Changes to Existing Mechanisms

### Randomized RPA Updates

Prior to 6.1, the `HCI_LE_Set_Resolvable_Private_Address_Timeout [v1]` command (OCF 0x002E) accepted a single `RPA_Timeout` value (range 1 s to 3600 s, default 900 s / 15 min). The controller would generate a new RPA exactly every `RPA_Timeout` seconds.

The known privacy attack exploits the deterministic timing: an adversary recording BLE traffic can observe the precise moment an address changes and link the new address to the old one based on the exact timestamp, effectively negating address randomization.

**Version 6.1 change:** A new command `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` (OCF 0x009E) takes two parameters:

| Parameter | Range | Default |
|-----------|-------|---------|
| `RPA_Timeout_Min` | 1 s – 3600 s | 480 s (8 min) |
| `RPA_Timeout_Max` | 1 s – 3600 s | 900 s (15 min) |

The controller selects a uniformly random lifetime from `[RPA_Timeout_Min, RPA_Timeout_Max]` each time it generates a new RPA. This ensures that the time between address rotations is unpredictable to an external observer, making temporal re-identification attacks substantially harder.

The `[v1]` command remains fully supported for backward compatibility. A device that implements v2 reports the "Randomized RPA Updates" feature bit (feature type 2) in its LE feature set.

**Impacted sections in 6.1:**
- `[Vol 4] Part E, §7.8.45` — HCI command definition (both v1 and v2 variants)
- `[Vol 3] Part C` — GAP: privacy feature procedures updated to reference v2 command
- `[Vol 6] Part B` — Link Layer privacy: address rotation timing behavior

### Errata Corrections (selected highlights)

The 6.1 errata table (Table 15.1) includes corrections to the following specification sections. These are clarifications and bug fixes rather than behavioral feature changes:

- **V6B (LE Link Layer)**: Numerous corrections including errata 25333, 25633, 25847, 26814, 27211 — addressing ambiguities in advertising, connection procedures, and Channel Sounding step behavior
- **V4E (HCI)**: Large batch of corrections (40+ errata) covering command parameter validation, event generation conditions, and error code handling
- **V6H (Channel Sounding)**: Multiple corrections to tone quality, subevent handling, and FAE table procedures
- **V3C (GAP)**: Corrections to privacy mode procedures, connection parameter handling, and address resolution
- **V3F/V3G (ATT/GATT)**: Corrections to error response handling, characteristic discovery, and caching behavior
- **V3H (Security Manager)**: Corrections to key derivation and pairing procedure handling
- **V2C (LMP)**: Fixes including erratum 17738 (long-standing issue) and others
- **Global**: Erratum 26111 applied across multiple sections

---

## Deprecated / Removed

No features were deprecated or removed in v6.1. All 6.0 features remain fully supported.

---

## Developer Impact

**Privacy-sensitive applications (recommended action):**
- Implement `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` to enable randomized RPA lifetimes.
- Choose `RPA_Timeout_Min` and `RPA_Timeout_Max` values appropriate for your use case. The defaults (8–15 min) balance privacy with power consumption (RPA generation requires brief processing). For high-privacy applications, consider a narrower and shorter range.
- Advertise the "Randomized RPA Updates" feature bit in LE feature page 0 if your controller supports v2.
- If your host stack calls the v1 command, verify it is correctly mapped to v2 on controllers that support it. Both commands co-exist.

**All devices (errata compliance):**
- Apply errata incorporated in 6.1 to your Link Layer, HCI, GAP, ATT, GATT, and Security Manager implementations. The Channel Sounding corrections in V6H are particularly relevant for CS-capable devices.
- The large HCI errata set (V4E) may affect edge-case command behavior; review the errata list for commands your implementation uses.

**Host stack maintainers:**
- The new HCI v2 command (OCF 0x009E) must be added. It is in the same HCI OCF group as other LE commands (OGF 0x08).
- Feature detection: Check for LL feature bit "Randomized RPA Updates" (feature type 2) before issuing v2 command; fall back to v1 for older controllers.

---

## Cross-References

- See also: [diff-6.0-to-6.1](../version-diff/diff-6.0-to-6.1.md)
- Previous version: [core-spec-6.0](core-spec-6.0.md)
- Next version: [core-spec-6.2](core-spec-6.2.md)
- Concepts touched: [Security / Privacy](../concepts/security.md), [BLE Architecture](../concepts/ble-architecture.md)

---

*Source: [Core 6.1](../../sources/specs/6.1/Core_v6.1.md)*
