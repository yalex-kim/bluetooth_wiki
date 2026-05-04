# BLE Connection Management

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> This page is a developer reference for LE ACL connection management: lifecycle,
> parameter update procedures, power control, data path tuning, and the 6.2 short-interval
> feature. BR/EDR specifics are excluded unless directly relevant.

---

## Connection Lifecycle

```
Standby
   │
   │  HCI_LE_Create_Connection / HCI_LE_Extended_Create_Connection
   ▼
Initiating
   │
   │  Advertiser responds with CONNECT_IND / AUX_CONNECT_REQ
   ▼
Connection (Central role)          ◄── Peripheral role: Standby → Advertising → Connection
   │
   │  HCI_Disconnect / supervision timeout / LL_TERMINATE_IND
   ▼
Standby
```

- **Standby → Initiating**: Central issues `HCI_LE_Create_Connection` (legacy) or
  `HCI_LE_Extended_Create_Connection [v1/v2]`. Controller scans for the target advertiser.
- **Initiating → Connection**: Controller receives a connectable advertising PDU and sends
  `LL_CONNECTION_IND`. Both sides enter Connection state at the first connection event anchor point.
  The Peripheral's role is assigned; the Central drives connection events.
- **Connection → Standby**: Either side issues `HCI_Disconnect` (which generates
  `LL_TERMINATE_IND`), or the supervision timer expires on both sides independently.
  The `HCI_Disconnection_Complete` event notifies the Host.

[Core 6.2, Vol 6, Part B, §4.5; Vol 3, Part C, §9.3.5–9.3.6]

---

## Connection Parameters

### Standard LE ACL Parameters (4.0+)

| Parameter | Unit | Range | Constraint |
|-----------|------|-------|------------|
| Connection_Interval | 1.25 ms ticks | 0x0006–0x0C80 (7.5 ms–4 s) | Must be multiple of 1.25 ms; set by Central |
| Peripheral_Latency | subrated connection events | 0x0000–0x01F3 (0–499) | Must satisfy supervision constraint (see below) |
| Supervision_Timeout | 10 ms ticks | 0x000A–0x0C80 (100 ms–32 s) | See constraint formula |
| Min_CE_Length | 0.625 ms ticks | 0x0000–0xFFFF | Hint to Controller; not enforced |
| Max_CE_Length | 0.625 ms ticks | 0x0000–0xFFFF | Must be ≥ Min_CE_Length |

**Supervision_Timeout constraint** (mandatory):

```
Supervision_Timeout (ms) > (1 + Peripheral_Latency) × Connection_Interval (ms) × 2
```

When Connection Subrating is active, the formula extends to include the subrate factor
(see [Connection Subrating](#connection-subrating-53)):

```
Supervision_Timeout (ms) > (1 + Max_Latency) × Subrate_Factor × Connection_Interval_Max (ms) × 2
```

[Core 6.2, Vol 4, Part E, §7.8.12 (HCI_LE_Create_Connection); Vol 6, Part B, §4.5.2]

### Extended Interval Parameters (6.2+, Connection Rate)

When using `HCI_LE_Connection_Rate_Request`, the connection interval uses 125 µs ticks:

| Parameter | Unit | Range |
|-----------|------|-------|
| Connection_Interval (rate request) | 125 µs ticks | 0x0003–0x7D00 (375 µs–4 s) |

[Core 6.2, Vol 4, Part E, §7.8.154]

---

## Connection Parameter Update

Two distinct paths exist depending on initiator role and capability support.

### Path 1 — LL-initiated (Central only): `HCI_LE_Connection_Update`

The Central's Host issues [`HCI_LE_Connection_Update`](../reference/hci-commands.md) (opcode 0x2013)
directly to the Controller. The Controller runs the `LL_CONNECTION_UPDATE_IND` procedure:

```
Central Host                Central Controller              Peripheral Controller
     │                             │                                │
     │─ HCI_LE_Connection_Update ─►│                                │
     │                             │─── LL_CONNECTION_UPDATE_IND ──►│
     │                             │◄── (acknowledged in next CE) ──│
     │◄── LE_Connection_Update_    │                                │
     │    Complete event ──────────│◄── LE_Connection_Update_ ──────│
     │                             │    Complete event              │
```

Parameters take effect at the `Instant` field value (a future connEventCounter).
The Central controller may autonomously issue this if the interval is outside the requested range.

Note: `LE_Connection_Update_Complete` is **not** issued if the update used the Connection Subrate
Update procedure or Connection Rate Update procedure; those generate `LE_Subrate_Change` or
`LE_Connection_Rate_Change` events instead. [Core 6.2, Vol 4, Part E, §7.7.65.3]

### Path 2 — L2CAP signaling (Peripheral-initiated)

A Peripheral that cannot initiate an LL procedure directly uses L2CAP signaling channel (CID 0x0005)
to request parameter updates from the Central's Host:

```
Peripheral Host             Peripheral Controller    Central Controller    Central Host
      │                             │                       │                    │
      │─ HCI_LE_Connection_Update ─►│                       │                    │
      │  (or App triggers L2CAP)    │                       │                    │
      │                             │─ L2CAP_CONN_PARAM_ ──►│                    │
      │                             │  UPDATE_REQ            │──────────────────►│
      │                             │                        │  (Central decides) │
      │                             │◄─ L2CAP_CONN_PARAM_ ──│◄───────────────────│
      │                             │   UPDATE_RSP           │                    │
      │◄── LE_Remote_Connection_    │                        │                    │
      │    Parameter_Request event  │                        │                    │
```

The L2CAP `Connection_Parameter_Update_Request` (code 0x12) carries Interval_Min, Interval_Max,
Peripheral_Latency, and Timeout. The Central Host responds with code 0x13 (`_RSP`): result
0x0000 = accepted, 0x0001 = rejected.

If accepted, the Central Host calls `HCI_LE_Connection_Update` to apply the parameters.
If the Central supports the LL Connection Parameters Request procedure
(`HCI_LE_Remote_Connection_Parameter_Request_Reply` / `_Negative_Reply`), it can also be
initiated at LL level without going through L2CAP.

[Core 6.2, Vol 3, Part A, §4.20–4.21; Vol 3, Part C, §9.3.9]

**Common pitfalls:**
- A Central may legally reject the L2CAP request; the Peripheral must handle this gracefully.
- Do not initiate a connection parameter update while encryption setup (LTK exchange) is in progress.
- A Peripheral must wait at least `2 × (Peripheral_Latency + 1) × connInterval` before retrying
  a connection parameter update after a previous attempt. [Core 6.2, Vol 3, Part C, §9.3.9]

---

## Connection Subrating (5.3+)

Connection Subrating multiplies the effective connection interval by a `Subrate_Factor` without
changing the underlying (physical) connection interval. Only every N-th connection event
is a "subrated connection event" that devices must participate in.

**Key parameters:**

| Parameter | Range | Description |
|-----------|-------|-------------|
| Subrate_Factor | 1–500 (0x0001–0x01F4) | Virtual multiplier on the connection interval |
| Peripheral_Latency (subrated) | 0–499 (0x0000–0x01F3) | Skip additional subrated events (stacks on top of Subrate_Factor) |
| Continuation_Number | 0–15 (0x0000–0x000F) | Extra consecutive base events to stay active after a non-empty subrated exchange; independent of Subrate_Factor |
| connSubrateBaseEvent | 0–65535 | Anchor for which events are subrated events |

**Stacking clarification**: Subrate_Factor and Max_Latency (Peripheral_Latency in subrated units)
are independent multipliers that compound. If `connInterval = 7.5 ms`, `Subrate_Factor = 10`,
and `Max_Latency = 4`, the effective wakeup interval is `7.5 ms × 10 × (4 + 1) = 375 ms`.
Max_Latency is expressed in units of *subrated* connection events, not underlying events.

**Continuation_Number is distinct**: it controls how many additional consecutive base events
a device stays active after a non-empty PDU exchange at the subrated anchor point, enabling
a short burst window without renegotiating the subrate. It does **not** multiply the wakeup
interval. Range: 0–15 (raw 0x0000–0x000F); must be < Subrate_Factor.

**Formula summary**:
```
Effective_Wakeup_Interval = Connection_Interval × Subrate_Factor × (Max_Latency + 1)
```

**Supervision_Timeout with subrating** (mandatory check before applying):

```
Supervision_Timeout (ms) > (1 + Max_Latency) × Subrate_Factor × Connection_Interval_Max (ms) × 2
```

[Core 6.2, Vol 4, Part E, §7.8.123 (HCI_LE_Subrate_Request)]

**Two LL procedures:**

1. **Connection Subrate Update** (Central-initiated via `LL_SUBRATE_IND`):
   Central sends `HCI_LE_Subrate_Request` → Controller issues `LL_SUBRATE_IND` →
   `LE_Subrate_Change` event confirms completion.

2. **Connection Subrate Request** (Peripheral-initiated via `LL_SUBRATE_REQ`):
   Peripheral sends `HCI_LE_Subrate_Request` → Controller issues `LL_SUBRATE_REQ` →
   Central accepts (triggers Subrate Update procedure) or rejects with `LL_REJECT_EXT_IND`.

**HCI commands:**

| Command | Opcode | Role | Notes |
|---------|--------|------|-------|
| [`HCI_LE_Set_Default_Subrate`](../reference/hci-commands.md) | 0x207D | Central | Sets acceptable Subrate_Min/Max, Max_Latency, Continuation_Number for incoming Peripheral requests. Call before connections are established. |
| [`HCI_LE_Subrate_Request`](../reference/hci-commands.md) | 0x207E | Both | Triggers Subrate Update (Central) or Subrate Request (Peripheral) procedure. |

**Switching speed**: Transitioning from high subrate (e.g., 100) back to subrate=1 completes
in 1–2 connection events — far faster than a full Connection Parameter Update.

Requires LE Feature `Connection Subrating` on both devices. [Core 6.2, Vol 6, Part B, §4.6.35; Vol 3, Part C, §9.3.16]

---

## Short Connection Intervals (6.2+)

Core 6.2 reduces the minimum LE ACL connection interval from 7.5 ms to **375 µs** by
switching to a 125 µs tick unit. This reuses the Connection Subrating mechanism as a prerequisite.

**Key facts:**
- Interval range: N × 125 µs, N = 3–0x7D00 (375 µs–4 s)
- Both devices must have the `Connection Rate (Host Support)` feature bit set.
- The Controller advertises its hardware minimum via `HCI_LE_Read_Minimum_Supported_Connection_Interval`;
  actual capability varies per implementation.

**HCI commands:**

| Command | Opcode | Purpose |
|---------|--------|---------|
| [`HCI_LE_Connection_Rate_Request`](../reference/hci-commands.md) | 0x20A1 | Central or Peripheral requests new interval (125 µs ticks), subrate, latency, continuation number, timeout |
| [`HCI_LE_Set_Default_Rate_Parameters`](../reference/hci-commands.md) | 0x20A2 | Central sets acceptable defaults for incoming Peripheral requests |
| [`HCI_LE_Read_Minimum_Supported_Connection_Interval`](../reference/hci-commands.md) | 0x20A3 | Query controller hardware minimum |

**Completion event**: `LE_Connection_Rate_Change` (subevent 0x37) — carries confirmed
Connection_Interval (N × 125 µs), Subrate_Factor, Peripheral_Latency, Continuation_Number,
Supervision_Timeout.

**New LL PDUs**: `LL_CONNECTION_RATE_REQ` / `LL_CONNECTION_RATE_IND`. [Core 6.2, Vol 6, Part B, §5.1.32–5.1.33]

**Use cases**: gaming peripherals (sub-1 ms response), real-time haptic feedback,
industrial control over BLE, USB replacement scenarios.

[Core 6.2, Vol 4, Part E, §7.8.154–7.8.156; Vol 6, Part B, §4.6.50; §5.1.32–33]

---

## LE Power Control (5.2+)

LE Power Control enables path-loss-based adaptive TX power. The Controller monitors received
signal strength and compares it against configurable thresholds.

**Path loss zones:**

```
             Low_Threshold          High_Threshold
                   │                      │
    Low zone  ◄────┤    Mid zone          ├────►  High zone
         (reduce TX)│                    (increase TX)│
```

Each zone boundary has an associated hysteresis band to prevent rapid oscillation.
The `Min_Time_Spent` parameter (in connection events) prevents false threshold crossings.

**Per-PHY reporting**: TX power is tracked independently for each PHY (1M, 2M, Coded S=2, S=8).

**HCI commands:**

| Command | Opcode | Purpose |
|---------|--------|---------|
| [`HCI_LE_Set_Path_Loss_Reporting_Parameters`](../reference/hci-commands.md) | 0x2078 | Set High_Threshold, High_Hysteresis, Low_Threshold, Low_Hysteresis, Min_Time_Spent (events) |
| [`HCI_LE_Set_Path_Loss_Reporting_Enable`](../reference/hci-commands.md) | 0x2079 | Enable/disable path loss monitoring per connection |
| [`HCI_LE_Set_Transmit_Power_Reporting_Enable`](../reference/hci-commands.md) | 0x207A | Enable local and/or remote TX power change reporting |
| [`HCI_LE_Enhanced_Read_Transmit_Power_Level`](../reference/hci-commands.md) | 0x2076 | Read current and max TX power for a specific PHY |
| [`HCI_LE_Read_Remote_Transmit_Power_Level`](../reference/hci-commands.md) | 0x2077 | Initiate remote TX power read (async; returns LE_Transmit_Power_Reporting event) |

**HCI events:**
- `LE_Path_Loss_Threshold` — zone change detected; includes Current_Path_Loss (dB) and Zone_Entered (0=low, 1=mid, 2=high).
- `LE_Transmit_Power_Reporting` — local or remote TX power changed; includes TX_Power_Level (dBm), Delta.

Order of operations: call `HCI_LE_Set_Path_Loss_Reporting_Parameters` **before** enabling; calling
`HCI_LE_Set_Path_Loss_Reporting_Enable` before parameters are set returns error 0x0C (Command Disallowed).

Requires LE Feature `LE Path Loss Monitoring` (for path loss events) and `LE Power Control Request`
(for remote TX power). [Core 6.2, Vol 4, Part E, §7.8.119–7.8.121; Vol 6, Part B, §4.5.16]

---

## Supervision Timeout and Reconnection

### What happens when supervision timeout fires

- Both Central and Peripheral independently detect the timeout when no valid packet (including
  empty LL Data PDUs) is received within `connSupervisionTimeout` ms.
- Both sides independently enter Standby state and generate `HCI_Disconnection_Complete`
  with error code `Connection_Timeout (0x08)`.
- No synchronization between devices is required; each reacts to its own timer.

**Choosing a timeout value**: too short causes spurious disconnections during radio congestion;
too long delays link-loss detection. Recommended starting point:
`6 × connInterval × (Peripheral_Latency + 1)`, increased for high-interference environments.

### Reconnection flow

**Fast path — Directed advertising (high-duty-cycle):**

```
Peripheral                               Central (bonded)
    │                                         │
    │── ADV_DIRECT_IND (target = Central) ───►│
    │── ADV_DIRECT_IND ──────────────────────►│
    │   (up to 1.28 s, ~3.75 ms intervals)   │
    │                                         │─── CONNECT_IND ──────────────────►│
    │◄─────────────────────────────────────── LE_Connection_Complete event        │
```

Peripheral sends high-duty-cycle connectable directed advertising targeting the bonded
Central by identity address (or RPA if address resolution is active). Duration is limited
to approximately 1.28 s per the spec. If the Central does not respond within this window,
the Peripheral falls back to the slow path.

**Slow path — Undirected connectable advertising:**

```
Peripheral                                 Any Central
    │                                           │
    │── ADV_IND (interval ~1 s background) ────►│
    │── ADV_IND ─────────────────────────────── │
    │   ...                                     │
    │                                           │─── CONNECT_IND ─────────────────►│
```

The Peripheral switches to low-duty-cycle undirected advertising (typically 1–1.2 s interval
`TGAP(adv_slow_interval)`). Any Central can initiate. This is the fallback when the bonded
Central does not reconnect within the directed advertising window.

**RPA note**: Do not rotate the RPA while advertising to a bonded Central — this breaks directed
advertising. Core 6.1's randomized RPA rotation interval (`HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]`,
0x209E) hardens privacy without breaking reconnection. [Core 6.2, Vol 3, Part C, §9.3.11]

---

## Data Length Extension (4.2+)

Prior to 4.2, LE data PDUs carried at most 27 bytes of payload. Data Length Extension (DLE)
negotiates larger PDU sizes per connection:

| Parameter | Default | Maximum |
|-----------|---------|---------|
| TX_Octets (payload bytes) | 27 | 251 |
| TX_Time (µs) | 328 | 17040 |

Host calls `HCI_LE_Set_Data_Length` → Controller exchanges `LL_LENGTH_REQ` / `LL_LENGTH_RSP` with
the peer → both sides generate `LE_Data_Length_Change` events. The Controller may also initiate
the procedure autonomously if `connInitialMaxTxOctets` ≠ 27. Effective size =
`min(local_TX_Octets, remote_RX_Octets)`.

**HCI commands** (`../reference/hci-commands.md` → LE Data Length Extension section):
- [`HCI_LE_Set_Data_Length`](../reference/hci-commands.md) (0x2022) — per-connection override
- [`HCI_LE_Write_Suggested_Default_Data_Length`](../reference/hci-commands.md) (0x2024) — default for new connections
- [`HCI_LE_Read_Maximum_Data_Length`](../reference/hci-commands.md) (0x202F) — controller hardware max

**Practical impact**: upgrading from 27 to 251 bytes per PDU reduces per-byte overhead
(header + MIC) from ~30 % to ~3 %, roughly tripling ACL throughput at the same connection
interval. [Core 6.2, Vol 6, Part B, §4.5.10; §5.1.9]

---

## PHY Selection (5.0+)

LE 5.0 added two additional PHYs to the original 1M:

| PHY | Symbol Rate | Typical Range | Throughput |
|-----|-------------|---------------|------------|
| LE 1M | 1 Mb/s | Baseline | ~125 KB/s (DLE) |
| LE 2M | 2 Mb/s | Similar to 1M | ~250 KB/s (DLE) |
| LE Coded S=2 | 500 kb/s | ~2× range of 1M | ~55 KB/s |
| LE Coded S=8 | 125 kb/s | ~4× range of 1M | ~13 KB/s |

Either side initiates via [`HCI_LE_Set_PHY`](../reference/hci-commands.md) (0x2032) →
Controller exchanges `LL_PHY_REQ` / `LL_PHY_RSP` / `LL_PHY_UPDATE_IND` → both sides generate
`LE_PHY_Update_Complete`. Either side can be the initiator.
The `PHY_Options` field selects S=2 vs. S=8 for Coded PHY (bits 0–1: 0=no preference, 1=S2, 2=S8).
If no PHY change results, the `LE_PHY_Update_Complete` event is still generated (with status=success).

**Selection guidance**: Use **2M** for throughput at short range; **Coded S=8** for maximum
range (4× vs 1M, but 20× longer on-air time); **1M** as the interoperability baseline.
Both 2M and Coded require the respective LE feature bit on both devices.

[Core 6.2, Vol 4, Part E, §7.8.49; §7.7.65.12; Vol 6, Part B, §4.6.20–4.6.22]

---

## RSSI and Link Quality

**Basic RSSI**: `HCI_Read_RSSI` (0x1405) returns a signed dBm value for the connection handle.
RSSI is sampled by the Controller; its accuracy and averaging window are implementation-defined.

**Typical RSSI ranges (indicative, antenna-dependent):**
- Adjacent devices (< 1 m): −30 to −50 dBm
- Same room (3–5 m): −55 to −75 dBm
- Cross-room or obstructed (10+ m): −75 to −90 dBm
- Near link budget limit: < −90 dBm

For proximity use cases (e.g., PACS digital car keys, retail find-my), prefer LE Power Control
path loss monitoring over raw RSSI, as it accounts for both ends' TX power and compensates for
TX power changes. Path loss = Remote_TX_Power_Level − RSSI.

[Core 6.2, Vol 4, Part E, §7.5.4 (HCI_Read_RSSI); Vol 6, Part B, §4.5.16]

---

## Version History

| Feature | Introduced | Spec Reference |
|---------|-----------|----------------|
| LE ACL connections (base) | 4.0 | Vol 6, Part B, §4.5 |
| L2CAP Connection Parameter Update (Peripheral-initiated) | 4.0 | Vol 3, Part A, §4.20 |
| LE Connection Parameters Request (LL procedure) | 4.1 | Vol 6, Part B, §5.1.7 |
| Data Length Extension (27 → 251 bytes) | 4.2 | Vol 6, Part B, §4.5.10; §5.1.9 |
| LE 2M PHY / LE Coded PHY | 5.0 | Vol 6, Part B, §4.6.20–4.6.22 |
| LE Power Control (path loss monitoring) | 5.2 | Vol 6, Part B, §4.5.16 |
| Connection Subrating (Subrate_Factor 1–500) | 5.3 | Vol 6, Part B, §4.6.35; §5.1.19–5.1.20 |
| Short Connection Intervals (375 µs, 125 µs ticks) | 6.2 | Vol 6, Part B, §4.6.50; §5.1.32–5.1.33 |
| Randomized RPA rotation interval | 6.1 | Vol 4, Part E, §7.8.45 |

---

## See Also

- [BLE Architecture](ble-architecture.md) — Link Layer state machine, PDU types, channel map
- [HCI Command Reference](../reference/hci-commands.md) — full command tables for connection management, PHY, DLE, power control
- [Security](security.md) — encryption setup, pairing, LTK exchange over established connections
- [LE Audio](le-audio.md) — CIS/BIS isochronous connections layered on top of ACL

---

*Source: [Core 6.2, Vol 3, Part A + Vol 3, Part C + Vol 6, Part B + Vol 4, Part E](../../sources/specs/6.2/Core_v6.2.md)*
