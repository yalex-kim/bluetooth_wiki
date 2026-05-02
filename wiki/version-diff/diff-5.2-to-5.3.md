# Diff: Bluetooth Core Spec 5.2 → 5.3

**From**: [Core Spec 5.2](../versions/core-spec-5.2.md) (2019-12-31)
**To**: [Core Spec 5.3](../versions/core-spec-5.3.md) (2021-07-13)

> Note: 5.3 was later withdrawn by Bluetooth SIG and superseded by 5.4.
> All 5.3 features are present in 5.4.

---

## At a Glance

5.3 is an efficiency-focused release. **Connection Subrating** enables dramatic battery savings
for peripherals by slowing connection events without disconnecting. **Enhanced Connection Update**
makes parameter negotiation symmetric. **Advertising Coding Selection** gives precise control
over LE Coded PHY range/power tradeoffs. This is an important release for battery-powered IoT
even though it doesn't introduce a headline capability like LE Audio.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **Connection Subrating** | Multiply effective connection interval by subrate factor without parameter update | Vol 6, Part B, §4.5.20 |
| **Subrate Change procedure** | LL_SUBRATE_REQ / LL_SUBRATE_IND PDUs | Vol 6, Part B |
| **LE Enhanced Connection Update** | Symmetric connection parameter update (either side can propose) | Vol 6, Part B, §4.5.19 |
| **Advertising Coding Selection** | Advertiser specifies S=2 or S=8 preference in extended advertising | Vol 6, Part B, §2.3 |
| **Periodic Advertising ADI** | Advertising Data Info field added to periodic advertising PDUs | Vol 6, Part B, §2.3.4 |

---

## Modified

| What | Change |
|------|--------|
| **Connection Parameter Update** | Enhanced version replaces legacy; legacy still supported for backward compat |
| **Extended Advertising PDUs** | Coding Indication field added for LE Coded PHY selection |
| **LE Features** | New bits for Connection Subrating, Enhanced Connection Update |
| **HCI** | New commands for subrate configuration; updated connection update command |

---

## Deprecated / Removed

- Legacy Connection Parameter Update procedure still supported (backward compatibility)
- 5.3 spec itself was withdrawn (superseded by 5.4)

---

## Migration Guide

### Implementing Connection Subrating

Subrating is most valuable for devices that alternate between "active" and "idle" states:

```
Fast mode (e.g., mouse moving):    interval=7.5ms,  subrate=1   → 7.5ms  effective
Slow mode (e.g., mouse idle):      interval=7.5ms,  subrate=100 → 750ms  effective
Switch back to fast: LL_SUBRATE_REQ with subrate=1 (completes in 1-2 events vs full param update)
```

Steps:
1. Check `LE Features` for `Connection Subrating` support on both sides
2. Use `HCI_LE_Set_Default_Subrate` to set controller defaults
3. Use `HCI_LE_Subrate_Request` to request subrate change for a specific connection
4. Listen for `LE_Subrate_Change` event (subevent 0x23) to confirm new subrate

### Coding Selection for LE Coded PHY deployments

If you're deploying LE Coded PHY devices (introduced in 5.0):
- Use S=2 (500 kbps) when moderate range + battery life matters
- Use S=8 (125 kbps) for maximum range (~1 km line of sight)
- 5.3 allows the advertiser to express preference via `Coding_Selection` field
- Scanners can honor or override this preference
