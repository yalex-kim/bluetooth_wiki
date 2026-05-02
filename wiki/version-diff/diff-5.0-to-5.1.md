# Diff: Bluetooth Core Spec 5.0 → 5.1

**From**: [Core Spec 5.0](../versions/core-spec-5.0.md) (2016-12-06)
**To**: [Core Spec 5.1](../versions/core-spec-5.1.md) (2019-01-21)

---

## At a Glance

5.1's defining addition is **Direction Finding** — a hardware-level capability to measure the
angle of a Bluetooth signal using antenna arrays. Beyond positioning, 5.1 improved GATT
reconnection efficiency via database caching and cleaned up several advertising mechanisms.

---

## Added

| What | Description | Reference |
|------|-------------|-----------|
| **Direction Finding (AoA)** | Angle of Arrival: receiver with antenna array measures incoming signal angle | Vol 6, Part B, §2.5.4 |
| **Direction Finding (AoD)** | Angle of Departure: transmitter switches antennas; single-antenna receiver measures angle | Vol 6, Part B, §2.5.4 |
| **Constant Tone Extension (CTE)** | Fixed-frequency tone appended after CRC for angle measurement | Vol 6, Part B, §2.5.4 |
| **Connectionless CTE Tx/Rx** | CTE in periodic advertising PDUs for infrastructure positioning | Vol 6, Part B, §4.4.2 |
| **Connection CTE Request/Response** | CTE exchange over an established connection | Vol 6, Part B, §4.5.13 |
| **IQ Sampling** | Controller reports raw I/Q samples from antenna array to host | Vol 4, Part E |
| **GATT Database Hash** | Server exposes hash of GATT database; bonded clients validate cache | Vol 3, Part G, §7.8.1 |
| **GATT Caching** | Bonded GATT clients cache service discovery; re-validation on reconnect | Vol 3, Part G, §2.5.2 |
| **Advertising Channel Index in ADI** | ADI field carries channel index to deduplicate scan results | Vol 6, Part B, §2.3.4 |
| **Sleep Clock Accuracy (SCA) Update** | LL procedure to update SCA during connection lifetime | Vol 6, Part B, §4.5.16 |
| **HCI DF Commands/Events** | ~20 new HCI commands for CTE configuration and IQ reporting | Vol 4, Part E |

---

## Modified

| What | Change |
|------|--------|
| **Periodic Advertising** | ADI field added to periodic advertising PDUs (enables channel index tracking) |
| **LE Features bitmask** | New bits: Connectionless CTE Tx, Connectionless CTE Rx, Connection CTE Tx, Connection CTE Rx, Antenna Switching, IQ Samples from CTE |
| **HCI LE Meta events** | New subevent codes for IQ reports (connectionless and connection-based) |
| **Advertising PDU formats** | AUX_SYNC_IND and AUX_CHAIN_IND gain CTE info fields |

---

## Deprecated / Removed

- Nothing removed. Full backward compatibility with 5.0.

---

## Migration Guide

### Adding Direction Finding to a new product

1. **Choose AoA or AoD** based on your hardware constraints:
   - **AoA**: Put the antenna array on the infrastructure side (reader/anchor), simple tags
   - **AoD**: Put the antenna array on the tag, simple reader hardware

2. **Verify hardware support**: Check controller's `LE Features` for DF bits.
   Software-only stacks cannot implement DF — it requires hardware IQ sampling.

3. **For infrastructure AoA** (most common for indoor positioning):
   - Anchor = scanner with antenna array
   - Tag = 5.x advertiser with Connectionless CTE in periodic advertising
   - Scanner reads IQ samples and computes angle via host-side algorithm

4. **For existing 5.0 products**: No changes needed. CTE is ignored by 5.0 receivers.
   GATT caching is transparent to 5.0 GATT clients (they simply don't use the hash).

### Improving GATT reconnection performance

If your application bonds with GATT-heavy peripherals (many services/characteristics):
- Implement **GATT Database Hash** characteristic in server
- Cache hash + service discovery results in bonded client
- On reconnect: read hash, compare, skip discovery if match
- Can reduce reconnection time from hundreds of ms to <10 ms
