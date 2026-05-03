# Bluetooth Advertising

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> Advertising is the mechanism by which a BLE device broadcasts its presence and data on the three primary advertising channels (37, 38, 39). It is the entry point for discovery, connection establishment, and broadcast topologies. Legacy advertising (4.0) carries a maximum of 31 bytes and is limited to one active set; extended advertising (5.0+) supports up to 1650 bytes across multiple simultaneous sets, secondary channel offload, and the PDU chain used by periodic advertising and PAwR.

---

## Overview

**Legacy advertising** (introduced in Core 4.0) uses four PDU types on the primary advertising physical channels (LE 1M PHY only). The payload is limited to 31 bytes for both advertising data and scan response data. A device can run only one legacy advertising set at a time, and the HCI legacy commands (`HCI_LE_Set_Advertising_Parameters`, etc.) conflict with extended commands — do not mix the two.

**Extended advertising** (introduced in Core 5.0) introduces the `ADV_EXT_IND` PDU on the primary channel, which carries an `AuxPtr` pointing to secondary-channel PDUs (`AUX_ADV_IND`, `AUX_CHAIN_IND`, etc.). Up to 1650 bytes of advertising data can be carried across a PDU chain. Multiple advertising sets (up to 255, queried via `HCI_LE_Read_Number_of_Supported_Advertising_Sets`) can run concurrently, each with independent parameters, PHY, and identity address.

Use legacy advertising when targeting 4.x-only devices or when simplicity matters. Use extended advertising on all modern (5.0+) stacks for multi-set operation, larger payloads, secondary PHY (2M or Coded), periodic advertising, or PAwR.

[Core 6.2, Vol 6, Part B, §2.3]

---

## Advertising PDU Types

### Legacy PDUs (4.0+)

[Core 6.2, Vol 6, Part B, §2.3.1.1–2.3.1.4]

| PDU Type | Connectable | Scannable | Directed | Typical Use |
|----------|-------------|-----------|----------|-------------|
| `ADV_IND` | Yes | Yes | No | General connectable undirected advertising |
| `ADV_DIRECT_IND` | Yes | No | Yes | Directed connection to a known peer (high or low duty cycle) |
| `ADV_SCAN_IND` | No | Yes | No | Scannable non-connectable beacon with scan response |
| `ADV_NONCONN_IND` | No | No | No | Non-connectable, non-scannable broadcast beacon |

`ADV_IND`, `ADV_DIRECT_IND`, `ADV_NONCONN_IND`, and `ADV_SCAN_IND` are collectively referred to as "legacy advertising PDUs".

### Extended PDUs (5.0+)

[Core 6.2, Vol 6, Part B, §2.3.1.5–2.3.1.10]

| PDU Type | Channel | Direction | Used For |
|----------|---------|-----------|----------|
| `ADV_EXT_IND` | Primary (37/38/39) | Advertiser → Scanner | Pointer-only PDU; carries `AuxPtr` to secondary channel PDU. AdvMode field selects connectable/scannable/non-connectable. |
| `AUX_ADV_IND` | Secondary | Advertiser → Scanner | Main payload PDU on secondary channel; carries AdvA, AdvData, optional SyncInfo for periodic train. |
| `AUX_SCAN_RSP` | Secondary | Advertiser → Scanner | Scan response on secondary channel (extended scannable advertising). |
| `AUX_CHAIN_IND` | Secondary | Advertiser → Scanner | Continuation fragment of AdvData too large for a single PDU. Superior PDU is `AUX_ADV_IND`, `AUX_SYNC_IND`, `AUX_SCAN_RSP`, or another `AUX_CHAIN_IND`. |
| `AUX_SYNC_IND` | Secondary | Advertiser → Scanner | Periodic advertising train PDU (non-connectable, non-scannable). Carries `BIGInfo` in the ACAD field for Auracast. |
| `AUX_SYNC_SUBEVENT_IND` | Secondary | Advertiser → Devices | PAwR subevent packet sent by coordinator to assigned devices. [Core 6.2, Vol 6, Part B, §2.3.1.9] |
| `AUX_SYNC_SUBEVENT_RSP` | Secondary | Device → Advertiser | PAwR response from device to coordinator in an assigned response slot. [Core 6.2, Vol 6, Part B, §2.3.1.10] |
| `ADV_DECISION_IND` | Primary | Advertiser → Scanner | Decision-Based Advertising Filtering (DBAF, 6.0+); carries a Resolvable Tag or Arbitrary Data for scanner-side filtering. |

`ADV_EXT_IND`, `ADV_DECISION_IND`, `AUX_ADV_IND`, `AUX_SYNC_IND`, `AUX_CHAIN_IND`, `AUX_SYNC_SUBEVENT_IND`, and `AUX_SYNC_SUBEVENT_RSP` are collectively "extended advertising PDUs".

---

## Advertising Packet Structure

### Legacy Advertising Data (≤31 bytes)

[Core 6.2, Vol 3, Part C, §11]

The advertising payload (and scan response payload) is encoded as a sequence of **AD structures**:

```
| Length (1 byte) | AD Type (1 byte) | AD Data (Length-1 bytes) |
| Length (1 byte) | AD Type (1 byte) | AD Data (Length-1 bytes) |
...
| 0x00 or padding (non-significant part, all zeros) |
```

- **Length**: count of the remaining bytes in the AD structure, including the AD Type byte. Must be ≥ 1.
- **AD Type**: identifies the meaning of AD Data (values assigned in the Bluetooth Assigned Numbers document).
- **AD Data**: `Length - 1` bytes interpreted per the AD Type.

The **significant part** ends at the last non-zero Length byte. The non-significant padding (zeros) fills remaining space in a fixed-length field and is not transmitted unless needed to fill the field.

### Extended Advertising Data (≤1650 bytes)

Extended advertising data uses the same AD structure encoding as legacy but can be fragmented across multiple PDUs.

Fragmentation is controlled by the `Operation` parameter in `HCI_LE_Set_Extended_Advertising_Data` [Core 6.2, Vol 4, Part E, §7.8.54]:

| Operation | Meaning |
|-----------|---------|
| `0x00` | Intermediate fragment of fragmented extended advertising data |
| `0x01` | First fragment of fragmented extended advertising data |
| `0x02` | Last fragment of fragmented extended advertising data |
| `0x03` | Complete extended advertising data (most common) |
| `0x04` | Unchanged data — update Advertising DID only |

The `Fragment_Preference` hint (`0x00` = may fragment, `0x01` = minimize fragmentation) instructs the Controller but is not binding.

Each `HCI_LE_Set_Extended_Advertising_Data` call carries up to 251 bytes. For larger payloads, chain multiple calls with `Operation` 0x01 → 0x00 → ... → 0x02. The Controller assembles the chain into `AUX_ADV_IND` + `AUX_CHAIN_IND` PDUs on-air.

---

## AD Types (Assigned Numbers)

AD Type values are defined in the Bluetooth Assigned Numbers document (not in the Core Spec). AD data formats are defined in the Supplement to the Core Specification (CSS). [Core 6.2, Vol 3, Part C, §11]

| AD Type | Value | Description | Notes / Example |
|---------|-------|-------------|-----------------|
| Flags | `0x01` | LE/BR-EDR capability and discoverability flags | Bit 0: LE Limited Discoverable Mode; Bit 1: LE General Discoverable Mode; Bit 2: BR/EDR Not Supported |
| Incomplete List of 16-bit Service Class UUIDs | `0x02` | Partial list of 16-bit UUIDs | Use when list exceeds available space |
| Complete List of 16-bit Service Class UUIDs | `0x03` | Full list of 16-bit UUIDs | e.g., `0x1800` (GAP), `0x180F` (Battery) |
| Incomplete List of 128-bit Service Class UUIDs | `0x06` | Partial list of 128-bit UUIDs | Vendor-specific or proprietary services |
| Complete List of 128-bit Service Class UUIDs | `0x07` | Full list of 128-bit UUIDs | Vendor-specific or proprietary services |
| Shortened Local Name | `0x08` | Shortened UTF-8 device name | Used when full name doesn't fit |
| Complete Local Name | `0x09` | Full UTF-8 device name | Preferred when space allows |
| TX Power Level | `0x0A` | Signed 1-byte TX power in dBm | Used with RSSI for path-loss estimation |
| Slave Connection Interval Range | `0x12` | Min/Max connection interval hint | 4 bytes: MinInterval, MaxInterval (×1.25 ms) |
| Service Data — 16-bit UUID | `0x16` | Service-specific data associated with a 16-bit UUID | First 2 bytes = UUID little-endian; e.g., used in Eddystone |
| Appearance | `0x19` | 2-byte category/sub-category icon hint | e.g., `0x0180` (Generic Heart Rate Sensor) |
| Advertising Interval | `0x1A` | Advertising interval in units of 0.625 ms | Hint for scanner duty-cycle optimization |
| LE Bluetooth Device Address | `0x1B` | Public or random device address | For OOB address sharing |
| LE Role | `0x1C` | Supported GAP roles | Central, Peripheral, Observer, Broadcaster |
| LE Supported Features | `0x27` | Supported LE features bitmask | e.g., LE 2M PHY, LE Coded PHY |
| Service Data — 128-bit UUID | `0x21` | Service-specific data with a 128-bit UUID | First 16 bytes = UUID little-endian |
| Encrypted Advertising Data | `0x31` | AES-128-CCM encrypted payload (EAD, 5.4+) | Wraps other AD structures; requires pre-shared key |
| Manufacturer Specific Data | `0xFF` | Vendor-defined payload | First 2 bytes = Company Identifier Code (little-endian) |

> AD Type values not listed here (e.g., `0x0D`–`0x11`, `0x14`–`0x17`) are assigned to less common types (OOB data, URI, Indoor Positioning, etc.) and are documented in the Bluetooth Assigned Numbers document at bluetooth.com.

---

## Periodic Advertising (5.0+)

Periodic advertising establishes a **sync train**: the advertiser broadcasts `AUX_SYNC_IND` PDUs at a fixed interval, and scanners can synchronize to this train using `HCI_LE_Periodic_Advertising_Create_Sync`. Once synchronized, the scanner maintains a `Sync_Handle` and receives `LE_Periodic_Advertising_Report` events.

[Core 6.2, Vol 6, Part B, §4.4.2.12; Vol 4, Part E, §7.8.61–7.8.68]

Key parameters:
- **Periodic_Advertising_Interval**: `0x0006`–`0xFFFF` × 1.25 ms → **7.5 ms to 81.91875 s**
- **Sync_Handle**: 12-bit Controller-assigned handle returned in `LE_Periodic_Advertising_Sync_Established`

**PAST (Periodic Advertising Sync Transfer)** [Core 5.1+]: A device that is already synchronized to a periodic train can transfer synchronization information to a peer over an existing ACL connection using `HCI_LE_Periodic_Advertising_Sync_Transfer` (opcode `0x205A`) or `HCI_LE_Periodic_Advertising_Set_Info_Transfer` (opcode `0x205B`), eliminating the need for the peer to scan and synchronize independently.

A periodic advertising set must be backed by an **extended advertising set** configured as non-connectable, non-scannable (`Advertising_Event_Properties = 0x0000`). Periodic advertising cannot be layered on top of legacy advertising.

---

## PAwR — Periodic Advertising with Responses (5.4+)

PAwR extends the one-way periodic advertising model with **response slots**, enabling a single coordinator to communicate with up to thousands of devices without individual connections. It is the foundation of the Bluetooth ESL (Electronic Shelf Label) profile.

[Core 6.2, Vol 6, Part B, §2.3.1.9–2.3.1.10; Vol 4, Part E, §7.8.86–7.8.88]

### Structure

```
Periodic Advertising Interval
├── Subevent 0  → AUX_SYNC_SUBEVENT_IND  (coordinator → devices)
│   ├── Response slot 0  → AUX_SYNC_SUBEVENT_RSP  (device → coordinator)
│   ├── Response slot 1  → AUX_SYNC_SUBEVENT_RSP
│   └── ... (up to Num_Response_Slots)
├── Subevent 1  → AUX_SYNC_SUBEVENT_IND
│   └── ...
└── Subevent M  (up to Num_Subevents = 0x80 = 128 subevents)
```

### Key Parameters (`HCI_LE_Set_Periodic_Advertising_Parameters [v2]`, opcode `0x2086`)

| Parameter | Range | Resolution | Notes |
|-----------|-------|------------|-------|
| `Num_Subevents` | 0x01–0x80 | — | 0x00 = standard periodic advertising (no responses) |
| `Subevent_Interval` | 0x06–0xFF | × 1.25 ms | 7.5 ms – 318.75 ms between subevent starts |
| `Response_Slot_Delay` | 0x01–0xFE | × 1.25 ms | 1.25 ms – 317.5 ms from subevent IND to first response slot |
| `Response_Slot_Spacing` | 0x02–0xFF | × 0.125 ms | 0.25 ms – 31.875 ms between consecutive response slots |
| `Num_Response_Slots` | 0x01–0xFF | — | Response slots per subevent |

### Additional HCI Commands for PAwR

| Command | Opcode | Purpose |
|---------|--------|---------|
| `HCI_LE_Set_Periodic_Advertising_Subevent_Data` | `0x2082` | Set data for one or more subevents on the advertiser side |
| `HCI_LE_Set_Periodic_Advertising_Response_Data` | `0x2083` | Set response data for a specific response slot on the scanner side |
| `HCI_LE_Set_Periodic_Sync_Subevent` | `0x2084` | Instruct Controller to synchronize with a subset of subevents |

### ESL Use Case

An ESL gateway (coordinator) assigns each Electronic Shelf Label a specific subevent and response slot. The gateway broadcasts price/label updates in `AUX_SYNC_SUBEVENT_IND` PDUs; each tag acknowledges via `AUX_SYNC_SUBEVENT_RSP` in its assigned slot — all without individual ACL connections.

LE Feature bits: Bit 43 (PAwR Advertiser), Bit 44 (PAwR Scanner). [Core 5.4, Vol 6, Part B, §4.6.38–4.6.39]

---

## Advertising Intervals and Duty Cycle

[Core 6.2, Vol 3, Part C — GAP recommended timers; Bluetooth SIG Design Guidelines]

| Use Case | Typical Interval | Advertising Type | Notes |
|----------|-----------------|------------------|-------|
| Fast connectable (foreground) | 20–30 ms | `ADV_IND` / connectable extended | Used during initial pairing/connection window; high power |
| Slow connectable (background) | 100–500 ms | `ADV_IND` / connectable extended | Default for peripherals waiting for reconnection |
| Non-connectable beacon | 1–10 s | `ADV_NONCONN_IND` / non-connectable extended | Asset tracking, environmental sensors |
| iBeacon | 100–1000 ms | `ADV_NONCONN_IND` | Apple spec recommends 100 ms; most deploy at 200–1000 ms |
| Eddystone | 100–1000 ms | `ADV_NONCONN_IND` | Google spec: 100 ms recommended |
| ESL / PAwR | Sub-second (periodic) | `AUX_SYNC_SUBEVENT_IND` | Interval set by PAwR coordinator; sub-second acknowledgment via response slots |

The Bluetooth spec mandates a minimum advertising interval of 20 ms (`0x0020` × 0.625 ms) for legacy advertising. For connectable advertising the GAP recommended minimum is 100 ms to reduce interference. [Core 6.2, Vol 3, Part C, §9.3]

---

## HCI Command Flow

### Legacy advertising setup

[Core 6.2, Vol 4, Part E, §7.8.5–7.8.9]

1. [`HCI_LE_Set_Advertising_Parameters`](../reference/hci-commands.md#le-advertising-legacy) (opcode `0x2006`) — set interval, PDU type, address type, channel map, filter policy
2. [`HCI_LE_Set_Advertising_Data`](../reference/hci-commands.md#le-advertising-legacy) (opcode `0x2008`) — set up to 31 bytes of advertising data
3. [`HCI_LE_Set_Scan_Response_Data`](../reference/hci-commands.md#le-advertising-legacy) (opcode `0x2009`) — set up to 31 bytes of scan response data (if scannable)
4. [`HCI_LE_Set_Advertising_Enable`](../reference/hci-commands.md#le-advertising-legacy) (opcode `0x200A`) — enable advertising

### Extended advertising setup

[Core 6.2, Vol 4, Part E, §7.8.52–7.8.57]

1. [`HCI_LE_Set_Advertising_Set_Random_Address`](../reference/hci-commands.md#le-extended-advertising-50) (opcode `0x2035`) — assign a random address to the advertising set (if using random address)
2. [`HCI_LE_Set_Extended_Advertising_Parameters [v1]`](../reference/hci-commands.md#le-extended-advertising-50) (opcode `0x2036`) — configure `Advertising_Handle`, event properties bitmask, interval, PHY, SID, TX power
3. [`HCI_LE_Set_Extended_Advertising_Data`](../reference/hci-commands.md#le-extended-advertising-50) (opcode `0x2037`) — set advertising data (Operation `0x03` for complete data; use chained calls for >251 bytes)
4. [`HCI_LE_Set_Extended_Scan_Response_Data`](../reference/hci-commands.md#le-extended-advertising-50) (opcode `0x2038`) — set scan response data (if scannable; omit otherwise)
5. [`HCI_LE_Set_Extended_Advertising_Enable`](../reference/hci-commands.md#le-extended-advertising-50) (opcode `0x2039`) — enable one or more advertising sets

### Periodic advertising setup (layered on extended)

[Core 6.2, Vol 4, Part E, §7.8.61–7.8.63]

The underlying extended advertising set must be **non-connectable and non-scannable** (`Advertising_Event_Properties = 0x0000`).

1. `HCI_LE_Set_Extended_Advertising_Parameters` (opcode `0x2036`) — configure the extended set as non-connectable, non-scannable
2. [`HCI_LE_Set_Periodic_Advertising_Parameters [v1]`](../reference/hci-commands.md#le-periodic-advertising-50) (opcode `0x203E`) — set periodic interval and properties
   - For PAwR: use `[v2]` (opcode `0x2086`) and add `Num_Subevents`, `Subevent_Interval`, `Response_Slot_Delay`, `Response_Slot_Spacing`, `Num_Response_Slots`
3. [`HCI_LE_Set_Periodic_Advertising_Data`](../reference/hci-commands.md#le-periodic-advertising-50) (opcode `0x203F`) — set periodic advertising data
   - For PAwR: use `HCI_LE_Set_Periodic_Advertising_Subevent_Data` (opcode `0x2082`) per subevent
4. [`HCI_LE_Set_Extended_Advertising_Enable`](../reference/hci-commands.md#le-extended-advertising-50) (opcode `0x2039`) — enable the extended advertising set
5. [`HCI_LE_Set_Periodic_Advertising_Enable`](../reference/hci-commands.md#le-periodic-advertising-50) (opcode `0x2040`) — enable the periodic advertising train

---

## Version History

| Version | Feature Introduced |
|---------|--------------------|
| 4.0 | Legacy advertising PDUs (`ADV_IND`, `ADV_DIRECT_IND`, `ADV_NONCONN_IND`, `ADV_SCAN_IND`); AD structure format; 31-byte limit |
| 4.2 | No advertising changes; LE Privacy (RPA) affects advertiser address rotation |
| 5.0 | Extended advertising (`ADV_EXT_IND`, `AUX_ADV_IND`, `AUX_CHAIN_IND`, `AUX_SCAN_RSP`); up to 1650 bytes; multi-set; 2M and Coded PHY on secondary channel; Periodic Advertising (`AUX_SYNC_IND`) |
| 5.1 | PAST (Periodic Advertising Sync Transfer) — `HCI_LE_Periodic_Advertising_Sync_Transfer` and `Set_Info_Transfer` |
| 5.4 | PAwR (`AUX_SYNC_SUBEVENT_IND`, `AUX_SYNC_SUBEVENT_RSP`); Encrypted Advertising Data (EAD, AD type `0x31`); Advertising Coding Selection (S=2 / S=8 Host control) |
| 6.0 | Decision-Based Advertising Filtering (`ADV_DECISION_IND`); Monitored Advertisers list (`HCI_LE_Add_Device_To_Monitored_Advertisers_List`) |
| 6.1 | Randomized RPA timeout (`HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]`) — affects advertiser address rotation intervals |

---

## See Also

- [BLE Architecture](ble-architecture.md) — stack layers, roles (Broadcaster, Observer, Peripheral, Central)
- [HCI Command Reference](../reference/hci-commands.md) — full advertising command opcodes and parameters
- [Direction Finding](direction-finding.md) — CTE in advertising (connectionless AoA/AoD via periodic advertising)
- [Channel Sounding](channel-sounding.md) — HADM ranging, distinct from advertising

---

*Source: [Core 6.2, Vol 3, Part C §11 + Vol 6, Part B §2.3](../../sources/specs/6.2/Core_v6.2.md)*
