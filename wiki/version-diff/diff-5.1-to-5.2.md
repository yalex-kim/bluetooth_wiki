# Diff: Bluetooth Core Spec 5.1 → 5.2

**From**: [Core Spec 5.1](../versions/core-spec-5.1.md) (2019-01-21)
**To**: [Core Spec 5.2](../versions/core-spec-5.2.md) (2019-12-31)

---

## At a Glance

5.2 is the biggest update since BLE was introduced in 4.0. The three official new feature areas
(`[Core 5.2, Vol 1, Part C, §11.1]`) are:

1. **LE Isochronous Channels** — new Link Layer channel type with time-bounded delivery, enabling CIS (point-to-point) and BIS (broadcast) isochronous audio. Foundation of the LE Audio ecosystem.
2. **Enhanced Attribute Protocol (EATT)** — multiple parallel ATT bearers over L2CAP Enhanced Credit Based Flow Control, removing the single-transaction bottleneck.
3. **LE Power Control** — closed-loop TX power management with Power Control Request and Path Loss Monitoring procedures.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **LE Isochronous Channels** | New LL channel type; time-bounded, scheduled data delivery | Vol 1, Part C, §11.1 |
| **CIS (Connected Isochronous Stream)** | Bidirectional isochronous stream within an ACL connection | Vol 6, Part B, §4.5.13 |
| **CIG (Connected Isochronous Group)** | Groups CIS streams for synchronized multi-device audio (max 31 CIS) | Vol 6, Part B, §4.5.14 |
| **BIS (Broadcast Isochronous Stream)** | Unidirectional isochronous broadcast; no ACL needed | Vol 6, Part B, §4.4.6 |
| **BIG (Broadcast Isochronous Group)** | Groups BIS streams within the Isochronous Broadcasting State | Vol 6, Part B, §4.4.6 |
| **Isochronous Broadcasting State** | New LL state for BIG/BIS; uses Periodic Advertising for discovery | Vol 6, Part B, §4.4.6 |
| **Synchronization State for BIS** | Receiver syncs to a BIG via Periodic Advertising | Vol 6, Part B, §4.4.5 |
| **CIS Creation procedure** | LL_CIS_REQ → LL_CIS_RSP → LL_CIS_IND exchange | Vol 6, Part B, §5.1.15 |
| **CIS Termination procedure** | LL_CIS_TERMINATE_IND; does not affect associated ACL | Vol 6, Part B, §5.1.16 |
| **BIG Control procedures** | LL_BIG_CONTROL_PDU for channel map update, BIG termination | Vol 6, Part B, §5.6 |
| **LE Isochronous Adaptation Layer (ISOAL)** | Framing/segmentation of codec SDUs over ISO channels | Vol 6, Part G |
| **Enhanced ATT (EATT) bearer** | ATT bearer using L2CAP Enhanced Credit Based Flow Control Mode | Vol 3, Part F, §3.2 |
| **EATT reliable notifications** | EATT bearers shall process all notifications (no discard on overflow) | Vol 3, Part F, §3.2 |
| **EATT L2CAP interoperability** | ATT_MTU and channel requirements for EATT bearers | Vol 3, Part F, §5.3 |
| **LE Power Control Request procedure** | LL_POWER_CONTROL_REQ / LL_POWER_CONTROL_RSP | Vol 6, Part B, §4.6.31; §5.1.17 |
| **LE Power Change Indication procedure** | Unsolicited LL_POWER_CHANGE_IND | Vol 6, Part B, §4.6.30; §5.1.18 |
| **Power level management** | Controller manages power on all active PHYs per peer | Vol 6, Part B, §4.5.15 |
| **LE Path Loss Monitoring** | RSSI zone classification; HCI event on zone transition | Vol 6, Part B, §4.6.32; §4.5.16 |
| **HCI_LE_Set_CIG_Parameters** | Central's Host configures CIG/CIS parameters | Vol 4, Part E |
| **HCI_LE_Create_CIS** | Creates CIS(es) in the Controller | Vol 4, Part E |
| **HCI_LE_Setup_ISO_Data_Path** | Configures isochronous data path (incl. codec) | Vol 4, Part E |
| **HCI_LE_Create_BIG / BIG_Create_Sync** | Create BIG (broadcaster) or sync to BIG (receiver) | Vol 4, Part E |
| **HCI ISO Data Packets** | New HCI packet type for isochronous data (not ACL packets) | Vol 4, Part E |
| **HCI_LE_Read_Buffer_Size v2** | Returns ISO buffer size in addition to ACL buffer size | Vol 4, Part E |
| **HCI_LE_Set_Host_Feature** | Host sets/clears host-controlled feature bits (e.g., ISO Host Support) | Vol 4, Part E |
| **Feature bits 4.6.27–4.6.32** | CIS Master/Slave, Isochronous Broadcaster, Synchronized Receiver, Power Change Indication, Power Control Request, Path Loss Monitoring | Vol 6, Part B, §4.6.27–4.6.32 |

---

## Modified

| What | Change |
|------|--------|
| **ATT Protocol** | Added Enhanced ATT bearer concept; reliable notification delivery guaranteed on EATT bearers `[Vol 3, Part F, §3.2]` |
| **L2CAP** | Enhanced Credit Based Flow Control Mode added (used by EATT) |
| **LE Features (Vol 6, Part B, §4.6)** | Six new feature bits (4.6.27–4.6.32) for ISO channels and power control |
| **HCI LE Meta subevent** | Numerous new subevents: CIS established/request, BIG complete/sync established/lost, path loss threshold, TX power reporting |
| **Periodic Advertising** | BIG sync uses Periodic Advertising as the discovery/timing mechanism; BIGInfo added to ACAD in AUX_SYNC_IND |
| **Link Layer states** | New Isochronous Broadcasting State `[Vol 6, Part B, §4.4.6]`; Synchronization state extended for BIS |
| **Vol 1, Part A §3.7** | ISOAL added as new layer in the LE transport architecture |
| **Vol 1, Part A §3.8.2** | LE power control added to architecture overview |

---

## Deprecated / Removed

- Nothing removed. BR/EDR audio (SCO/eSCO + SBC) still exists in the spec — LE Audio is additive.
  The Bluetooth SIG repositioned BR/EDR audio as legacy, but it remains in the 5.2 spec.
- Security erratum 11838 (BR/EDR encryption key size requirements) incorporated `[Vol 1, Part C, §11.2]`

---

## Migration Guide

### Adopting LE Audio (CIS)

LE Audio is not a drop-in replacement for A2DP/HFP — it requires a full stack update:

1. **Controller**: Must support CIS (Connected Isochronous Stream - Master/Slave feature bits 4.6.27). Check hardware silicon.
2. **Host stack**: Implement HCI ISO data path commands/events (`HCI_LE_Set_CIG_Parameters`, `HCI_LE_Create_CIS`, `HCI_LE_Setup_ISO_Data_Path`, ISO data packets).
3. **ISO Host Support**: Host must set the "Isochronous Channels (Host Support)" bit via `HCI_LE_Set_Host_Feature` before using ISO channels.
4. **Profiles**: Implement BAP (Basic Audio Profile) which orchestrates CIS establishment, LC3 codec configuration, and audio stream setup.
5. **Codec**: Integrate LC3 encoder/decoder (reference implementation from Bluetooth SIG).

**Use CIS for**: Headsets, earbuds, hearing aids (point-to-point, bidirectional audio)
**Use BIS for**: Auracast™ broadcast, hearing loops, public address (one-to-many, unidirectional)

### Adopting LE Audio (BIS / Auracast)

1. **Controller**: Must support Isochronous Broadcaster (4.6.28) or Synchronized Receiver (4.6.29).
2. **Broadcaster**: Create Periodic Advertising train → Create BIG (`HCI_LE_Create_BIG`) → Transmit ISO data.
3. **Receiver**: Scan for Extended Advertising → Sync to Periodic Advertising → Sync to BIG (`HCI_LE_BIG_Create_Sync`) → Receive ISO data.
4. BIG termination: `HCI_LE_Terminate_BIG` (broadcaster) or `HCI_LE_BIG_Terminate_Sync` (receiver).

### Upgrading from Classic ATT to EATT

EATT is established via L2CAP Enhanced Credit Based Connection:
- Both sides must have EATT capability (Host-controlled; check with peer via GATT service)
- After connection, initiate EATT bearer(s) via Enhanced Credit Based Connection procedure
- Classic ATT Bearer (fixed L2CAP channel 0x0004) remains for backward compatibility

Benefits:
- Read multiple characteristics in parallel (one transaction per bearer)
- Write and read simultaneously
- Reliable notification delivery (no discard on overflow)

### LE Power Control

Enable closed-loop TX power management:
1. Initiate Power Control Request procedure: send `LL_POWER_CONTROL_REQ` with desired delta
2. Peer responds with `LL_POWER_CONTROL_RSP` reporting actual power change and current level
3. Configure Path Loss Monitoring via `HCI_LE_Set_Path_Loss_Reporting_Parameters` (high/low zone thresholds)
4. Enable reporting via `HCI_LE_Set_Path_Loss_Reporting_Enable`
5. Host receives `HCI_LE_Path_Loss_Threshold` events on zone transitions
