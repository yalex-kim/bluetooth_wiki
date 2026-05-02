# Diff: Bluetooth Core Spec 5.4 → 6.0

**From**: [Core Spec 5.4](../versions/core-spec-5.4.md) (2023-02-02)
**To**: [Core Spec 6.0](../versions/core-spec-6.0.md) (2024-08-27)

---

## At a Glance

6.0 is dominated by **Channel Sounding (CS)** — a precise distance measurement capability
that positions Bluetooth as a competitor to UWB (Ultra-Wideband) for ranging applications.
CS uses phase-based ranging and round-trip time to achieve centimeter accuracy, enabling
secure digital car keys, access control, and fine-grained asset location.
**DBAF** and **Monitoring Advertisers** are smaller but high-value additions for scanner power optimization.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **LE Channel Sounding (CS)** | Centimeter-accuracy distance measurement via PBR and RTT | Vol 6, Part B, §4.5.22 |
| **CS Initiator / Reflector roles** | Symmetric ranging procedure with defined roles | Vol 6, Part B |
| **CS Steps (tone, RTT, both)** | Individual measurement events within a CS procedure | Vol 6, Part B |
| **CS Security** | Built-in anti-relay, anti-spoofing protections for PACS use cases | Vol 6, Part H |
| **CS Subfeature negotiation** | Capabilities exchange before CS configuration | Vol 6, Part B |
| **Decision-Based Advertising Filtering (DBAF)** | Programmable controller-side advertising filter rules | Vol 6, Part B, §4.4.3 |
| **Monitoring Advertisers** | Controller tracks appearance/disappearance of specific advertisers | Vol 6, Part B, §4.4.3 |
| **Frame Space Updates** | New interframe spacing rules for improved scheduling | Vol 6, Part B, §4.2.3 |
| **ISO Adaptation Layer updates** | Segmentation improvements for LE Audio streams | Vol 6, Part G |
| **LE L2CAP enhancements** | Credit-Based Connection procedure improvements | Vol 3, Part A |

---

## Modified

| What | Change |
|------|--------|
| **LE Features** | New bits: CS Initiator, CS Reflector, CS (with no preference), DBAF, Monitoring Advertisers |
| **HCI** | ~25 new HCI commands/events for CS (LE_CS_Read_Remote_Supported_Capabilities, LE_CS_Create_Config, LE_CS_Procedure_Enable, etc.) |
| **LE Meta events** | New subevents for CS results (LE_CS_Read_Remote_Supported_Capabilities_Complete, LE_CS_Subevent_Result, etc.) |
| **Scanner HCI** | New commands for DBAF rule configuration, Monitoring Advertisers |
| **Periodic Advertising** | Minor timing adjustments for frame space compatibility |

---

## Deprecated / Removed

- Nothing removed. Full backward compatibility.

---

## Migration Guide

### Channel Sounding for car key / access control

CS is the most complex feature to implement in the Bluetooth spec.
Required steps:

1. **Check hardware support**: `LE Features` CS bits on both controller and peer
2. **Read capabilities**: `HCI_LE_CS_Read_Remote_Supported_Capabilities` — learn supported step types, antenna config, etc.
3. **Create CS Configuration**: `HCI_LE_CS_Create_Config` — define channel map, tone durations, RTT type, number of steps
4. **Enable CS Security** (for access control): exchange CS random values to prevent relay attacks
5. **Start procedure**: `HCI_LE_CS_Procedure_Enable`
6. **Process results**: `LE_CS_Subevent_Result` events contain raw phase/timing data
7. **Compute distance**: Host-side algorithm converts IQ/timing samples to distance estimate

**CS measurement accuracy** depends on:
- Number of channels (more = better accuracy; up to 72 channels usable)
- Step repetitions (averaging reduces noise)
- Antenna configuration (multiple antennas improve spatial diversity)
- Environment (multipath in indoors can affect accuracy)

**Anti-relay for PACS**:
- Digital car keys require proving that the key is physically close (anti-relay)
- CS is designed so relay attacks add measurable latency / phase distortion
- CS security procedures verify both sides have direct RF path

### DBAF and Monitoring Advertisers for power-efficient scanning

**Before 6.0** (continuous scan in a retail environment with hundreds of BLE devices):
- Every advertising PDU wakes the host
- Host discards 99% of reports (wrong device, wrong RSSI, etc.)
- High CPU and radio duty cycle

**With DBAF**:
```
// Pseudo-code: program controller with rules
LE_Set_Decision_Data([
  rule: RSSI > -70 dBm AND contains AD_TYPE_NAME,
  rule: address == "AA:BB:CC:DD:EE:FF"
])
// Controller now only wakes host for matching reports
```

**With Monitoring Advertisers** (simpler use case: "is my device nearby?"):
```
LE_Set_Monitored_Advertisers(["AA:BB:CC:DD:EE:FF"])
// Host wakes only when device appears or disappears
// Zero CPU usage while device is consistently present/absent
```
