# Bluetooth Core Specification 5.3

**Release Date**: 2021-07-13
**Status**: Superseded by 5.4 (withdrawn by Bluetooth SIG, use 5.4)
**Spec Volume**: ~3698 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-3/) | [Local PDF](../../sources/specs/core-spec-5.3.pdf) | [Local Markdown](../../sources/specs/core-spec-5.3.md)

> **Note**: The Bluetooth SIG withdrew Core Specification 5.3. It is superseded by 5.4.
> The features introduced in 5.3 are retained in 5.4.

---

## Executive Summary

Bluetooth 5.3 was an incremental but important release focused on **connection efficiency**,
**coexistence**, and **terminology modernization**. The official new features per
`[Core 5.3, Vol 1, Part C, §12.1]` are: **AdvDataInfo (ADI) in Periodic Advertising**,
**Host to Controller Encryption Key Control Enhancements**, **LE Enhanced Connection Update**,
and **LE Channel Classification**.

The headline efficiency feature, **Connection Subrating** `[Core 5.3, Vol 6, Part B, §4.6.35]`,
allows connected devices to dramatically reduce the frequency of connection events without
disconnecting — critical for battery-powered devices. The **LL_SUBRATE_IND** and
**LL_SUBRATE_REQ** PDUs support Central-initiated and Peripheral-initiated subrate changes,
respectively `[Core 5.3, Vol 6, Part B, §5.1.19–5.1.20]`.

**LE Channel Classification** `[Core 5.3, Vol 6, Part B, §4.6.36]` is a new cooperative
mechanism where a Peripheral reports its observed channel quality to the Central via
`LL_CHANNEL_STATUS_IND`, enabling smarter AFH channel map selection.

5.3 also removed the Alternate MAC/PHY (AMP) subsystem entirely, simplifying the architecture.
A global terminology update replaced inappropriate terms (e.g., "master/slave" → "Central/Peripheral")
`[Core 5.3, Vol 1, Part C, §12.4]`.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Connection Subrating | Multiply effective connection interval by subrate factor without full parameter update | Vol 6, Part B, §4.6.35; §5.1.19–5.1.20 |
| Connection Subrate Update procedure | Central sends LL_SUBRATE_IND to update subrate factor | Vol 6, Part B, §5.1.19 |
| Connection Subrate Request procedure | Peripheral sends LL_SUBRATE_REQ to request subrate change | Vol 6, Part B, §5.1.20 |
| LE Channel Classification | Peripheral reports observed channel quality; LL_CHANNEL_REPORTING_IND / LL_CHANNEL_STATUS_IND | Vol 6, Part B, §4.6.36; §5.1.21–5.1.22 |
| Channel Classification Enable procedure | Central enables/disables classification reporting on Peripheral | Vol 6, Part B, §5.1.21 |
| Channel Classification Reporting procedure | Peripheral sends LL_CHANNEL_STATUS_IND to report channel quality | Vol 6, Part B, §5.1.22 |
| Periodic Advertising ADI | AdvDataInfo (ADI) field added to AUX_SYNC_IND PDUs | Vol 6, Part B, §4.6.34 |
| Host-to-Controller Encryption Key Control | Host can set minimum encryption key size; new security controls | Vol 4, Part E |
| LE Enhanced Connection Update | HCI_LE_Connection_Update aligned with Connection Parameters Request procedure | Vol 3, Part C; Vol 4, Part E |

---

## Key Changes to Existing Mechanisms

### Connection Subrating

Before 5.3, slowing down a connection required a full Connection Parameter Update
(negotiated at host level), changing the base interval. Connection Subrating adds a
**subrate factor** that multiplies the effective interval without changing the underlying one
`[Core 5.3, Vol 6, Part B, §4.6.35]`:

- A `connSubrateFactor` of N means the device only participates in every N-th connection event
- The **connSubrateBaseEvent** anchors which events are "subrated connection events"
- The **connContinuationNumber** specifies extra consecutive events after a subrated event (for burst traffic)
- The **Supervision_Timeout** must satisfy: `> 2 × connInterval × Subrate_Max × (Max_Latency + 1)`

**Two LL procedures** `[Core 5.3, Vol 6, Part B, §5.1.19–5.1.20]`:

1. **Connection Subrate Update** (Central-initiated): Central sends `LL_SUBRATE_IND` PDU. Peripheral immediately switches to new parameters when it receives the PDU. Central enters "subrate transition mode" and retransmits on both old and new subrated events until acknowledged.

2. **Connection Subrate Request** (Peripheral-initiated): Peripheral sends `LL_SUBRATE_REQ` PDU. Central either accepts (by initiating Subrate Update procedure) or rejects with `LL_REJECT_EXT_IND`.

**HCI commands** (new in 5.3):
- `HCI_LE_Set_Default_Subrate` — Central sets acceptable subrate parameters for incoming Peripheral requests
- `HCI_LE_Subrate_Request` — Host triggers Connection Subrate Request (on Peripheral) or Update (on Central)
- `HCI_LE_Subrate_Change` event — Controller notifies Host when subrate change completes
- Feature bits: C57 requirements `[Core 5.3, Vol 4, Part E]`

**Practical advantage**: Switching from slow mode (large subrate) to fast mode (subrate=1) completes
in 1–2 connection events — far faster than a full Connection Parameter Update negotiation.

`[Core 5.3, Vol 3, Part C, §9.3.16]` defines the GAP Connection Subrate procedure.

### LE Channel Classification

A new cooperative channel quality reporting mechanism `[Core 5.3, Vol 6, Part B, §4.6.36]`:

1. **Central** sends `LL_CHANNEL_REPORTING_IND` to enable or disable reporting on the Peripheral (Channel Classification Enable procedure `[Core 5.3, Vol 6, Part B, §5.1.21]`)
2. **Peripheral** monitors channel quality and sends `LL_CHANNEL_STATUS_IND` with a channel classification map to the Central (Channel Classification Reporting procedure `[Core 5.3, Vol 6, Part B, §5.1.22]`)
3. Peripheral shall not report if channel classification has not changed since the last report
4. Two consecutive reports must be spaced apart by at least the minimum reporting spacing

This complements the existing `HCI_LE_Set_Host_Channel_Classification` mechanism (host-side AFH input) with Controller-observed real-time channel data.

### Periodic Advertising ADI (AdvDataInfo)

The **ADI** (Advertising Data Info) field, already used in extended advertising PDUs to indicate
data content identity, is now added to `AUX_SYNC_IND` PDUs `[Core 5.3, Vol 6, Part B, §4.6.34]`.
This allows a scanner that receives a periodic advertising report to determine whether the payload
has changed since the last report, enabling more efficient duplicate filtering for periodic advertising.

A Controller not supporting ADI Support shall not transmit or interpret the ADI field in `AUX_SYNC_IND`.

### Host-to-Controller Encryption Key Control Enhancements

New HCI mechanism allowing the Host to communicate minimum encryption key size requirements
to the Controller, strengthening the security boundary between Host and Controller.

### LE Enhanced Connection Update

The `HCI_LE_Connection_Update` command behavior is aligned with the Connection Parameters
Request LL procedure, providing a more consistent host-level interface for connection parameter
updates `[Core 5.3, Vol 3, Part C]`.

### Removed: Alternate MAC/PHY (AMP)

5.3 completely removed the AMP subsystem `[Core 5.3, Vol 1, Part C, §12.2]`:
- Alternative MAC/PHY
- AMP Manager protocol (A2MP)
- L2CAP Enhancements for AMP
- 802.11 PAL
- 802.11n Enhancements to 802.11 PAL

This is a major architectural simplification: the Core Spec is now BR/EDR + LE only.

### Global Terminology Changes

`[Core 5.3, Vol 1, Part C, §12.4]` replaced inappropriate terms throughout the spec:
- "Master" → "Central"
- "Slave" → "Peripheral"
- HCI command names updated accordingly (e.g., `HCI_LE_Set_CIG_Parameters` now refers to "Central's Host")

---

## Deprecated / Removed

- **Alternate MAC/PHY (AMP)** and all related sub-features: removed from spec `[Core 5.3, Vol 1, Part C, §12.2]`
- Core Spec 5.3 itself was subsequently **withdrawn** by Bluetooth SIG (superseded by 5.4)
- Legacy Connection Parameter Update procedure still supported for backward compatibility

---

## Developer Impact

**High impact areas:**
- **Battery-powered peripherals** (mice, keyboards, wearables, IoT sensors): Connection Subrating enables aggressive duty cycling without sacrificing reconnection speed. A mouse idle at subrate=100 (750 ms effective interval) can switch back to subrate=1 (7.5 ms) in 1–2 events.
- **AFH / coexistence** improvements: Channel Classification gives Controllers real-time peer-observed data for better channel map selection, reducing interference
- **Auracast / Periodic Advertising**: ADI field enables smarter duplicate filtering for Periodic Advertising receivers
- **AMP removal**: Any implementation that used AMP (e.g., Wi-Fi coexistence via 802.11 PAL) must migrate; most modern implementations did not use AMP

**Implementation checklist for Connection Subrating:**
1. Check LE Feature `Connection Subrating` (bit 4.6.35) on both sides via Feature Exchange
2. Central: use `HCI_LE_Set_Default_Subrate` to set acceptable ranges
3. Central-initiated: `HCI_LE_Subrate_Request` → Controller sends `LL_SUBRATE_IND` → `LE_Subrate_Change` event
4. Peripheral-initiated: `HCI_LE_Subrate_Request` → Controller sends `LL_SUBRATE_REQ` → Central accepts/rejects → `LE_Subrate_Change` event

---

## Cross-References

- Diff from 5.2: [diff-5.2-to-5.3](../version-diff/diff-5.2-to-5.3.md)
- Diff to 5.4: [diff-5.3-to-5.4](../version-diff/diff-5.3-to-5.4.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md)
