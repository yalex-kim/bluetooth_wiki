# Diff: Bluetooth Core Spec 6.0 → 6.1

**From**: [Core Spec 6.0](../versions/core-spec-6.0.md) (2024-08-27)
**To**: [Core Spec 6.1](../versions/core-spec-6.1.md) (2025-04-29)

---

## At a Glance

Bluetooth 6.1 is a focused privacy-hardening release. The single new feature — **Randomized RPA Updates** — adds a new HCI command that replaces the fixed 15-minute Resolvable Private Address rotation timeout with a randomized range, preventing observers from tracking BLE devices by correlating the precise moment their addresses rotate. Beyond this, 6.1 is primarily an errata release, incorporating corrections across nearly every section of the specification without changing any feature behavior. No features were removed.

---

## Added

- **Randomized RPA Updates** — Adds `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` (OCF 0x009E) with `RPA_Timeout_Min` and `RPA_Timeout_Max` parameters. The controller randomizes each RPA's lifetime within the specified range, defeating timing-based re-identification attacks. Defaults: 480 s min, 900 s max. [Vol 4, Part E, §7.8.45; Vol 6, Part B (Link Layer privacy); Vol 3, Part C (GAP privacy)]

---

## Modified

- **`HCI_LE_Set_Resolvable_Private_Address_Timeout` command** — A new `[v2]` variant (OCF 0x009E) is added alongside the existing `[v1]` (OCF 0x002E). v1 accepts a single fixed `RPA_Timeout` (1–3600 s, default 900 s). v2 accepts `RPA_Timeout_Min` (default 480 s) and `RPA_Timeout_Max` (default 900 s). Controllers must support both variants; hosts detect v2 support via the "Randomized RPA Updates" feature bit. [Vol 4, Part E, §7.8.45]

- **LE Link Layer (V6B)** — Large batch of errata corrections (errata 25333, 25480, 25633, 25847, 26104, 26814, 27211, and many others) covering advertising procedures, connection event handling, Channel Sounding subevent behavior, and Link Layer control procedures. [Vol 6, Part B]

- **HCI (V4E)** — Over 40 errata applied to command parameter validation, error code handling, ISO data path, and power control events. [Vol 4, Part E]

- **Channel Sounding (V6H)** — Corrections to tone quality indication, FAE table request procedures, and subevent result reporting (errata 25633, 25847, 26062, 26063, 26078, 26082, 26112, 26116). [Vol 6, Part H]

- **GAP (V3C)** — Corrections to address resolution procedures, privacy mode, connection parameter negotiation, and advertising behavior (errata 18947, 19226, 25255, 25458, 25773, 26158, 27211). [Vol 3, Part C]

- **ATT (V3F) and GATT (V3G)** — Corrections to error response handling, characteristic discovery, caching, and long characteristic operations (errata 20421, 23409, 25193, 25394, 25611, 27211). [Vol 3, Parts F and G]

- **Security Manager (V3H)** — Corrections to key derivation, pairing confirm/random values, and IRK handling (errata 25086, 26548, 26814). [Vol 3, Part H]

- **L2CAP (V3A)** — Corrections to enhanced/credit-based channels, SDU segmentation (errata 24555, 25439, 26664). [Vol 3, Part A]

- **LMP (V2C)** — Corrections including the long-standing erratum 17738, plus 25502, 25832, 25833. [Vol 2, Part C]

- **LE PHY (V6A)** — Corrections to physical layer timing (errata 25847, 26162, 26439). [Vol 6, Part A]

---

## Deprecated / Removed

No features were deprecated or removed in v6.1.

---

## Migration Guide

**For devices that implement LE privacy (RPA generation):**

1. **Detect v2 support**: Check for the "Randomized RPA Updates" feature bit in the LE Supported Features before issuing the v2 command.
2. **Issue the new command**: Replace calls to `HCI_LE_Set_Resolvable_Private_Address_Timeout [v1]` with `[v2]` when supported. The new command OCF is 0x009E (in OGF 0x08 block; the v1 OCF was 0x002E).
3. **Choose range parameters**: The defaults (480 s min, 900 s max) are reasonable for most use cases. For higher-privacy applications, consider a shorter and/or narrower range. For battery-sensitive devices, a wider range reduces average rotation frequency.
4. **Fallback behavior**: Devices that issue v1 on a v2-capable controller will continue to use a fixed timeout. The privacy improvement requires using v2 explicitly.

**For all devices (errata):**

- Apply the errata incorporated in 6.1 to your implementation. The most impactful areas are:
  - V6B (Link Layer): Large number of corrections — review the errata table carefully for any that affect your LL procedures
  - V4E (HCI): Many command-level fixes — review for any commands your host stack uses
  - V6H (Channel Sounding): Required if your implementation supports CS from 6.0
  - V3C (GAP), V3F (ATT), V3G (GATT): Corrections to common host-layer procedures

**Testing:**
- Add conformance tests for the new v2 HCI command, including parameter boundary validation (Min > Max, Min = 0, Max = 3601 should all be rejected).
- Verify that the controller's RPA rotation interval is no longer deterministically predictable when v2 is in use.
