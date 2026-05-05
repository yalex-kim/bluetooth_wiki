# Diff: Bluetooth Core Spec 5.2 → 5.3

**From**: [Core Spec 5.2](../versions/core-spec-5.2.md) (2019-12-31)
**To**: [Core Spec 5.3](../versions/core-spec-5.3.md) (2021-07-13)

> Note: 5.3 was later withdrawn by Bluetooth SIG and superseded by 5.4.
> All 5.3 features are present in 5.4.

---

## At a Glance

5.3 is an efficiency and coexistence release. The official new features per
`[Core 5.3, Vol 1, Part C, §12.1]` are: **AdvDataInfo in Periodic Advertising**,
**Host to Controller Encryption Key Control Enhancements**, **LE Enhanced Connection Update**,
and **LE Channel Classification** (which includes Connection Subrating as a sub-feature).

The practical headline is **Connection Subrating** `[Core 5.3, Vol 6, Part B, §4.6.35](../../sources/specs/5.3/Core_v5.3.md#L59528)`:
enables dramatic battery savings for peripherals by slowing connection events without disconnecting,
with fast return to active mode. **LE Channel Classification** `[Core 5.3, Vol 6, Part B, §4.6.36](../../sources/specs/5.3/Core_v5.3.md#L59537)`
adds Peripheral-observed channel quality reporting to complement host-side AFH input.

The **removal of AMP** `[Core 5.3, Vol 1, Part C, §12.2]` is the most architecturally significant
change: the 802.11 PAL and AMP subsystem are completely excised, leaving a cleaner BR/EDR + LE spec.
A **global terminology change** replaced "master/slave" with "Central/Peripheral" throughout
`[Core 5.3, Vol 1, Part C, §12.4]`.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **Connection Subrating** | LL feature: multiply effective connection interval by subrate factor | Vol 6, Part B, §4.6.35 |
| **Connection Subrate Update procedure** | Central sends LL_SUBRATE_IND; Peripheral immediately applies new subrate | Vol 6, Part B, §5.1.19 |
| **Connection Subrate Request procedure** | Peripheral sends LL_SUBRATE_REQ; Central accepts (→ Subrate Update) or rejects | Vol 6, Part B, §5.1.20 |
| **Subrate transition mode** | Central retransmits LL_SUBRATE_IND on both old and new subrated events during transition | Vol 6, Part B, §5.1.19 |
| **HCI_LE_Set_Default_Subrate** | Sets default acceptable subrate parameters for incoming Peripheral requests | Vol 4, Part E (C57) |
| **HCI_LE_Subrate_Request** | Triggers Connection Subrate Update (Central) or Subrate Request (Peripheral) | Vol 4, Part E (C57) |
| **LE_Subrate_Change event** | Subevent 0x23; reports new Subrate_Factor, Peripheral_Latency, Continuation_Number, Supervision_Timeout | Vol 4, Part E (C57) |
| **Connection Subrating (Host Support) feature bit** | Host-controlled feature bit; indicates Host supports subrating | Vol 6, Part B, §4.6.35 |
| **LE Channel Classification** | Peripheral reports observed channel quality to Central | Vol 6, Part B, §4.6.36 |
| **Channel Classification Enable procedure** | Central sends LL_CHANNEL_REPORTING_IND to enable/disable reporting | Vol 6, Part B, §5.1.21 |
| **Channel Classification Reporting procedure** | Peripheral sends LL_CHANNEL_STATUS_IND with channel quality map | Vol 6, Part B, §5.1.22 |
| **Periodic Advertising ADI Support** | ADI field added to AUX_SYNC_IND PDUs; allows duplicate detection for periodic advertising | Vol 6, Part B, §4.6.34 |
| **Advertising Coding Selection** | Host can explicitly select S=2 or S=8 coding for LE Coded PHY advertising sets, overriding Controller default | Vol 6, Part B, §4.6.37 |
| **Host-to-Controller Encryption Key Control** | Host can specify minimum encryption key size to Controller | Vol 4, Part E |
| **GAP Connection Subrate procedure** | Host-level procedure for initiating connection subrating | Vol 3, Part C, §9.3.16 |
| **Feature bit 4.6.35** | Connection Subrating (Controller) | Vol 6, Part B, §4.6.35 |
| **Feature bit 4.6.36** | Channel Classification | Vol 6, Part B, §4.6.36 |
| **HCI_LE_Set_Host_Channel_Classification** | Updated to work with Channel Classification feature (C58) | Vol 4, Part E |

---

## Modified

| What | Change |
|------|--------|
| **Connection Update procedure** | When subrate is changed via Connection Subrate Update procedure, HCI_LE_Connection_Update_Complete shall NOT be issued; LE_Subrate_Change event is used instead `[Vol 4, Part E]` |
| **Connection interval rules** | If connection interval changes via Connection Update, subrate factor resets to 1 and continuation number to 0 `[Vol 6, Part B, §5.1.1]` |
| **Supervision Timeout requirement** | Must satisfy `> 2 × connInterval × Subrate_Max × (Max_Latency + 1)` when using subrating `[Vol 4, Part E, §7.8.124]` |
| **LE Features (Vol 6, Part B, §4.6)** | Added feature bits 4.6.34 (Periodic Advertising ADI Support), 4.6.35 (Connection Subrating), 4.6.36 (Channel Classification) |
| **HCI LE Meta subevents** | New: LE Subrate Change (subevent 0x23) |
| **Vol 1, Part A architecture** | AMP section removed; alternate MAC/PHY references removed throughout |
| **Terminology throughout** | "master" → "Central", "slave" → "Peripheral"; many HCI command descriptions updated |
| **GAP connection modes** | Connection Subrate procedure added to GAP connection procedure table; C2 condition `[Vol 3, Part C, §9.3]` |
| **GATT/ATT** | References updated to use Central/Peripheral terminology |
| **Vol 0, Part B compliance** | High Speed Core Configuration removed; LE and BR/EDR+LE configurations updated |

---

## Removed / Deprecated

| What | Notes |
|------|-------|
| **Alternate MAC/PHY (AMP)** | Completely removed from spec `[Vol 1, Part C, §12.2]` |
| **AMP Manager Protocol (A2MP)** | Removed |
| **L2CAP Enhancements for AMP** | Removed |
| **802.11 PAL** | Volume 5 effectively gutted; 802.11 PAL removed |
| **802.11n Enhancements to 802.11 PAL** | Removed |
| **High Speed (HS) Core Configuration** | Removed from compliance requirements `[Vol 0, Part B]` |
| **"master/slave" terminology** | Replaced by "Central/Peripheral" throughout; HCI command names updated accordingly |
| **5.3 spec itself** | Withdrawn by Bluetooth SIG; superseded by 5.4 |

---

## Migration Guide

### Implementing Connection Subrating

Subrating delivers the most value for devices that alternate between "active" and "idle" states
(mice, keyboards, wearables, industrial sensors):

```
Fast mode (active):   interval=7.5ms, subrate=1   → 7.5ms effective
Slow mode (idle):     interval=7.5ms, subrate=100 → 750ms effective
Return to fast:       LL_SUBRATE_IND with subrate=1 → completes in 1–2 events
```

**Central-initiated subrate change** (most common):
1. Verify `Connection Subrating` feature (bit 4.6.35) on both sides via Feature Exchange
2. Central: use `HCI_LE_Set_Default_Subrate` to set acceptable Subrate_Min, Subrate_Max, Continuation_Number, Max_Latency, Supervision_Timeout
3. Central: use `HCI_LE_Subrate_Request` (on Central role) → Controller sends `LL_SUBRATE_IND`
4. Listen for `LE_Subrate_Change` event to confirm new effective parameters

**Peripheral-initiated subrate change**:
1. Check that `Connection Subrating (Host Support)` bit is set in Central's FeatureSet before requesting
2. Peripheral: use `HCI_LE_Subrate_Request` (on Peripheral role) → Controller sends `LL_SUBRATE_REQ`
3. Central accepts (by initiating Subrate Update) or rejects with error
4. Listen for `LE_Subrate_Change` event

**Key supervision timeout formula** (ensure no false timeout during slow mode):
`Supervision_Timeout > 2 × connInterval × Subrate_Max × (Max_Latency + 1)`

### Implementing LE Channel Classification

1. Verify `Channel Classification` feature (bit 4.6.36) on Peripheral via Feature Exchange
2. Central: send `LL_CHANNEL_REPORTING_IND` to enable reporting (Channel Classification Enable procedure `[Vol 6, Part B, §5.1.21]`)
3. Peripheral: internally monitor channel quality; when quality changes, send `LL_CHANNEL_STATUS_IND` (Channel Classification Reporting procedure `[Vol 6, Part B, §5.1.22]`)
4. Central: receive channel status data and factor it into the AFH channel map (combine with `HCI_LE_Set_Host_Channel_Classification` input from Host)
5. Periodic Advertising ADI: if both sides support feature bit 4.6.34, the ADI field in `AUX_SYNC_IND` can be used by receivers to determine if periodic advertising data changed since last sync

### AMP Removal Impact

If your implementation used AMP:
- Remove all A2MP protocol handling
- Remove 802.11 PAL integration
- The `High Speed (HS)` core configuration is no longer defined; any compliance based on HS must migrate to standard BR/EDR or LE configurations

### Terminology / API Changes

HCI command names are unchanged in 5.3 (terminology changes are in documentation text).
However, any host software using field names like "Master" or "Slave" in data structures
should check for updated names in 5.3 HCI parameter descriptions.

---

*Source: [Core 5.2](../../sources/specs/5.2/Core_v5.2.md) and [Core 5.3](../../sources/specs/5.3/Core_v5.3.md)*
