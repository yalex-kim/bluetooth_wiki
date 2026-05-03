# BLE Parameter Quick Reference

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> One-stop reference for BLE tunable parameters. All values are controller-level unless noted.
> Unit column shows the raw tick unit; the Value column shows the usable range in human-readable form.

---

## Advertising Parameters

| Parameter | Raw Range | Unit | Usable Range | Typical | Notes |
|-----------|-----------|------|-------------|---------|-------|
| Advertising_Interval_Min/Max | 0x0020 – 0x4000 | 0.625 ms | 20 ms – 10.24 s | 100 ms – 1 s | Min 100 ms recommended for connectable. Default 1.28 s (0x0800) |
| Advertising_Channel_Map | bits 0–2 | — | ch37, ch38, ch39 | 0x07 (all) | Omitting channels reduces collision risk in congested 2.4 GHz environments |
| Extended Advertising Interval | 0x000020 – 0xFFFFFF | 0.625 ms | 20 ms – 10.486 s | 100 ms – 2 s | 3-byte field in `HCI_LE_Set_Extended_Advertising_Parameters` |
| Advertising_TX_Power | –127 – +20 | dBm | –127 – +20 dBm | 0 dBm | Set per advertising set in extended advertising |
| Max_Extended_Advertising_Events | 0x00 – 0xFF | events | 0 (no limit) – 255 | 0 | Per-set event limit in `HCI_LE_Set_Extended_Advertising_Enable` |
| Periodic_Advertising_Interval | 0x0006 – 0xFFFF | 1.25 ms | 7.5 ms – 81.92 s | 200 ms – 1 s | Used by `HCI_LE_Set_Periodic_Advertising_Parameters` |
| PAwR Num_Subevents | 0x01 – 0x80 | — | 1 – 128 | 4 – 16 | PAwR only (5.4+) |
| PAwR Subevent_Interval | 0x06 – 0xFF | 1.25 ms | 7.5 ms – 318.75 ms | 20 – 50 ms | Must fit within periodic interval |
| PAwR Response_Slot_Spacing | 0x02 – 0xFF | 0.125 ms | 0.25 ms – 31.875 ms | 1 – 5 ms | Time between response slots |
| PAwR Num_Response_Slots | 0x01 – 0xFF | — | 1 – 255 | 8 – 32 | Per subevent |

---

## Scanning Parameters

| Parameter | Raw Range | Unit | Usable Range | Typical | Notes |
|-----------|-----------|------|-------------|---------|-------|
| Scan_Interval | 0x0004 – 0x4000 | 0.625 ms | 2.5 ms – 10.24 s | 100 ms | Scan_Window ≤ Scan_Interval |
| Scan_Window | 0x0004 – 0x4000 | 0.625 ms | 2.5 ms – 10.24 s | 30 – 100 ms | Window = Interval → continuous scan (100% duty cycle) |
| Scan duty cycle | — | — | 0 – 100% | 10 – 50% | Window / Interval. Higher = faster discovery, more power |
| Extended Scan Duration | 0x0000 – 0xFFFF | 10 ms | 0 (no limit) – 655.35 s | 0 | Per scan period |
| Extended Scan Period | 0x0000 – 0xFFFF | 1.28 s | 0 (continuous) – 83886 s | 0 | Repeat interval for Duration-limited scans |

**Typical discovery times** (advertising at 100 ms, 3 channels):

| Scan duty cycle | Median discovery time |
|-----------------|----------------------|
| 100% (continuous) | ~110 ms |
| 50% (50 ms / 100 ms) | ~220 ms |
| 10% (10 ms / 100 ms) | ~1.1 s |

---

## Connection Parameters

| Parameter | Raw Range | Unit | Usable Range | Typical | Notes |
|-----------|-----------|------|-------------|---------|-------|
| Connection_Interval | 0x0006 – 0x0C80 | 1.25 ms | **7.5 ms – 4 s** | 15 – 100 ms | Used by `HCI_LE_Create_Connection`, `HCI_LE_Connection_Update` |
| Connection_Interval (6.2 short) | 0x0003 – 0x7D00 | **125 µs** | **375 µs – 4 s** | 375 µs – 5 ms | `HCI_LE_Connection_Rate_Request` only; requires "Connection Rate" LE feature |
| Peripheral_Latency | 0x0000 – 0x01F3 | events | 0 – 499 | 0 – 10 | Subrated events in 5.3+. Must satisfy constraint below |
| Supervision_Timeout | 0x000A – 0x0C80 | 10 ms | **100 ms – 32 s** | 3 – 10 s | Must be > 2 × Interval × (Latency + 1) |
| Min_CE_Length / Max_CE_Length | 0x0000 – 0xFFFF | 0.625 ms | 0 – 40.96 s | 0x0000 / 0xFFFF | Hint to Controller; not a hard guarantee |

**Supervision_Timeout constraint** (must hold, else connection will drop):
```
Supervision_Timeout > 2 × Connection_Interval × (Peripheral_Latency + 1)
```
Example: Interval=50 ms, Latency=4 → Timeout must be > 500 ms.

---

## Connection Subrating (5.3+)

| Parameter | Raw Range | Unit | Usable Range | Notes |
|-----------|-----------|------|-------------|-------|
| Subrate_Factor | 0x0001 – 0x01F4 | — | 1 – 500 | Multiplier on Connection_Interval for the effective event rate |
| Max_Latency (subrated) | 0x0000 – 0x01F3 | subrated events | 0 – 499 | Like Peripheral_Latency but in subrated event units |
| Continuation_Number | 0x0000 – 0x01F3 | events | 0 – 499 | Consecutive base events before returning to subrated schedule |

**Effective Supervision_Timeout constraint with subrating**:
```
Supervision_Timeout > 2 × Connection_Interval × Subrate_Factor × (Max_Latency + 1)
```

---

## Data Length Extension (4.2+)

| Parameter | Raw Range | Unit | Usable Range | Default | Notes |
|-----------|-----------|------|-------------|---------|-------|
| TX_Octets | 0x001B – 0x00FB | bytes | 27 – 251 bytes | 27 | LL Data PDU payload |
| TX_Time | 0x0148 – 0x4290 | 1 µs | 328 – 17040 µs | 328 µs | Must be consistent with TX_Octets × PHY bitrate |

**Throughput impact** (approximate, 1M PHY, no retransmission):

| TX_Octets | Effective data rate |
|-----------|-------------------|
| 27 bytes (default) | ~130 kbps |
| 251 bytes (max) | ~800 kbps |

---

## PHY Parameters (5.0+)

| PHY | Symbol Rate | Max Range | Use Case |
|-----|------------|-----------|---------|
| LE 1M | 1 Msym/s | ~100 m | Default; balanced |
| LE 2M | 2 Msym/s | ~80 m | High throughput (DLE + 2M ≈ 1.4 Mbps) |
| LE Coded S=2 | 500 ksym/s | ~200 m | Long range, medium power |
| LE Coded S=8 | 125 ksym/s | ~400 m | Max range, highest robustness |

---

## Privacy / RPA Parameters (4.2+)

| Parameter | Raw Range | Unit | Usable Range | Default | Notes |
|-----------|-----------|------|-------------|---------|-------|
| RPA_Timeout [v1] | 0x0001 – 0x0E10 | 1 s | 1 s – 1 hour | 900 s | Fixed rotation interval |
| RPA_Timeout_Min [v2] | 0x0001 – 0x0E10 | 1 s | 1 s – 1 hour | 480 s | 6.1+: Controller picks random value in [Min, Max] |
| RPA_Timeout_Max [v2] | 0x0001 – 0x0E10 | 1 s | 1 s – 1 hour | 900 s | Randomized RPA rotation (6.1+) |

---

## LE Audio / ISO Parameters (5.2+)

| Parameter | Raw Range | Unit | Usable Range | Typical | Notes |
|-----------|-----------|------|-------------|---------|-------|
| SDU_Interval | 0x0000FF – 0x0FFFFF | 1 µs | 255 µs – ~1.05 s | 7.5 ms / 10 ms | LC3 frame duration |
| Max_SDU | 0x0001 – 0x0FFF | bytes | 1 – 4095 bytes | 40 – 240 bytes | Per SDU per direction |
| ISO_Interval | 0x0004 – 0x0C80 | 1.25 ms | 5 ms – 4 s | 7.5 ms / 10 ms | CIS/BIS isochronous event interval |
| Max_Transport_Latency | 0x0005 – 0x0FA0 | 1 ms | 5 ms – 4 s | 10 – 40 ms | End-to-end transport latency budget |
| RTN (Retransmission Number) | 0x00 – 0x0F | — | 0 – 15 | 2 – 5 | Reliability vs. latency trade-off |
| BN (Burst Number) | 0x00 – 0x0F | — | 0 – 15 | 1 – 4 | PDUs per ISO interval |
| Broadcast_Code | — | 16 bytes | — | — | Encryption key for BIS; all-zero = no encryption |

**LC3 common configurations** (from BAP v1.0.2):

| Config | Sampling Rate | Frame Duration | Bitrate | SDU size | Latency |
|--------|--------------|----------------|---------|----------|---------|
| 8_1 | 8 kHz | 7.5 ms | 26 kbps | 26 bytes | — |
| 8_2 | 8 kHz | 10 ms | 24 kbps | 30 bytes | — |
| 16_1 | 16 kHz | 7.5 ms | 32 kbps | 30 bytes | — |
| 16_2 | 16 kHz | 10 ms | 32 kbps | 40 bytes | Default telephony |
| 24_2 | 24 kHz | 10 ms | 48 kbps | 60 bytes | — |
| 32_2 | 32 kHz | 10 ms | 64 kbps | 80 bytes | — |
| 48_1 | 48 kHz | 7.5 ms | 80 kbps | 75 bytes | — |
| 48_4 | 48 kHz | 10 ms | 96 kbps | 120 bytes | High quality |
| 48_6 | 48 kHz | 10 ms | 124 kbps | 155 bytes | Max quality |

---

## Channel Sounding Parameters (6.0+)

| Parameter | Range | Notes |
|-----------|-------|-------|
| T_IP1 (inter-procedure interval 1) | 10 – 145 µs | Capability-dependent; negotiated |
| T_IP2 (inter-procedure interval 2) | 10 – 145 µs | Capability-dependent |
| T_FCS (frequency change spacing) | 15 – 150 µs | Capability-dependent |
| T_PM (phase measurement period) | 10 – 40 µs | 10 / 20 / 40 µs options |
| CS procedure interval | 0x0001 – 0xFFFF | ×0.625 ms = 0.625 ms – 40.96 s |
| Max_Procedure_Len | 0x0001 – 0xFFFF | ×0.625 ms; max length of one procedure |
| Num_Config | 0 – 3 | Up to 4 simultaneous CS configs per connection |
| Num_Antenna_Paths | 1 – 4 | Capability-dependent |

---

## Key Formulas

```
# Supervision timeout minimum
Supervision_Timeout_min (ms) = 2 × Interval (ms) × (Peripheral_Latency + 1) + 10

# Subrated supervision timeout minimum
Supervision_Timeout_min (ms) = 2 × Interval (ms) × Subrate_Factor × (Max_Latency + 1) + 10

# Maximum BLE throughput (approximate)
Throughput (bps) ≈ (TX_Octets × 8) / Connection_Interval
  e.g. 251 bytes / 7.5 ms ≈ 268 kbps (1M PHY, no retransmission overhead)

# DLE TX_Time from TX_Octets (1M PHY)
TX_Time (µs) = (TX_Octets + 14) × 8      # +14 = LL header (4) + MIC (4) + preamble+AA (6)

# Advertising discovery time (approximate)
Discovery_time ≈ Adv_Interval × (1 / Scan_Duty_Cycle) × 1.1   # ×1.1 for channel diversity
```

---

## Parameter Selection Guide

| Use Case | Interval | Latency | Timeout | Notes |
|----------|----------|---------|---------|-------|
| Gaming peripheral | 7.5 – 15 ms | 0 | 500 ms | Lowest latency; high power |
| Audio (LE Audio) | 7.5 – 10 ms | 0 | 500 ms | Use CIS instead of ACL for audio data |
| HID (keyboard/mouse) | 7.5 – 20 ms | 0 – 2 | 1 s | Latency for keypress feel |
| Wearable (heart rate) | 200 – 500 ms | 4 – 10 | 5 s | Low power, tolerates latency |
| IoT sensor (periodic) | 1 – 4 s | 0 | 10 s | Minimum power; use Subrating on 5.3+ |
| Proximity / RSSI | 100 – 200 ms | 0 | 2 s | Frequent RSSI samples needed |
| OTA firmware update | 7.5 – 30 ms | 0 | 5 s | Maximize throughput with DLE |

---

## See Also

- [HCI Command Reference](hci-commands.md) — full command list with opcodes
- [HCI Sequences](hci-sequences.md) — step-by-step command flows
- [Connection Management](../concepts/connection-management.md) — parameter update procedures
- [LE Audio](../concepts/le-audio.md) — ISO/LC3 configuration details
- [Advertising](../concepts/advertising.md) — advertising-specific parameters

---

*Source: [Core 6.2, Vol 4, Part E, §7](../../sources/specs/6.2/Core_v6.2.md) and [BAP v1.0.2](../../sources/specs/profiles/BAP_v1.0.2.md)*
