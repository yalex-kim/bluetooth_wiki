# Bluetooth Core Specification 5.3

**Release Date**: 2021-07-13
**Status**: Superseded by 5.4 (withdrawn by Bluetooth SIG, use 5.4)
**Spec Volume**: ~3698 pages
**Source PDF**: [bluetooth.com](https://www.bluetooth.com/specifications/specs/core-specification-5-3/) | [Local PDF](../../sources/specs/core-spec-5.3.pdf) | [Local Markdown](../../sources/specs/core-spec-5.3.md)

> **Note**: The Bluetooth SIG withdrew Core Specification 5.3. It is superseded by 5.4.
> The features introduced in 5.3 are retained in 5.4.

---

## Executive Summary

Bluetooth 5.3 was an incremental but important release focused on **connection efficiency**
and **coexistence**. The headline feature, **Connection Subrating**, allows connected devices
to dramatically reduce the frequency of connection events without disconnecting — critical for
battery-powered devices that need to maintain a "ready" connection while spending most time asleep.

**LE Enhanced Connection Update** replaced the classic Connection Parameter Update procedure
with a more symmetric, lower-latency approach. **Advertising Coding Selection** gave advertisers
explicit control over which LE Coded PHY coding scheme (S=2 or S=8) to use, enabling better
range/power tradeoffs.

Several periodic advertising improvements laid groundwork for the PAwR feature in 5.4.

---

## New Features

| Feature | Brief Description | Spec Reference |
|---------|------------------|----------------|
| Connection Subrating | Reduce connection event frequency without reconnecting | Vol 6, Part B, §4.5.20 |
| LE Enhanced Connection Update | Symmetric connection parameter update procedure | Vol 6, Part B, §4.5.19 |
| Advertising Coding Selection | Advertiser specifies S=2 or S=8 for LE Coded PHY | Vol 6, Part B, §2.3 |
| Periodic Advertising ADI | ADI field added to periodic advertising PDUs | Vol 6, Part B, §2.3.4 |
| Periodic Advertising with Responses prep | Spec changes anticipating PAwR in 5.4 | Vol 6, Part B |
| LE Ping improvements | Optimized authenticated payload timeout procedure | Vol 6, Part B, §4.5.6 |

---

## Key Changes to Existing Mechanisms

### Connection Subrating

Before 5.3, a device that wanted to "slow down" a connection had to use Connection Parameter
Update to increase the connection interval (e.g., from 7.5 ms to 1000 ms). This required
host-level negotiation and applied to all traffic.

Connection Subrating adds a **subrate factor** that multiplies the connection interval
without changing the underlying interval. For example:
- Base interval: 7.5 ms
- Subrate factor: 100
- Effective interval: 750 ms

The advantage: **fast switching**. Devices can switch from slow (power saving) to fast (responsive)
mode much quicker than a full parameter update. This is ideal for:
- Mouse/keyboard peripherals (slow when idle, fast when active)
- Industrial sensors (wake on event, then return to slow mode)

The LL procedure uses `LL_SUBRATE_REQ / LL_SUBRATE_IND`.

### LE Enhanced Connection Update

The legacy Connection Parameter Update (pre-5.3) had asymmetric roles: only the peripheral could
request updates. The central could accept or reject but not propose alternatives.

Enhanced Connection Update (`LL_CONNECTION_PARAM_REQ`) is bidirectional: either side can
propose new parameters, and both sides can counter-propose. Reduces negotiation latency.

### Advertising Coding Selection

5.0 introduced LE Coded PHY (S=2 and S=8) but the advertiser could not specify which coding
to use — the scanner chose. 5.3 allows advertisers to explicitly indicate their preferred coding,
enabling range-optimized deployment (choose S=8 for maximum range, S=2 for moderate range + power).

---

## Deprecated / Removed

- Core Spec 5.3 itself was later **withdrawn** by Bluetooth SIG (superseded by 5.4)
- Connection Parameter Update (legacy) is still supported for backward compatibility

---

## Developer Impact

**High impact areas:**
- **Battery-powered peripherals**: Connection Subrating enables aggressive duty cycling without
  sacrificing reconnection speed. Implement this in mice, keyboards, wearables.
- **LE Coded PHY deployments**: Now can explicitly select S=2 vs S=8 per use case.
- **Connection management**: Enhanced Connection Update simplifies parameter negotiation.

---

## Cross-References

- Diff from 5.2: [diff-5.2-to-5.3](../version-diff/diff-5.2-to-5.3.md)
- Diff to 5.4: [diff-5.3-to-5.4](../version-diff/diff-5.3-to-5.4.md)
- Related concepts: [BLE Architecture](../concepts/ble-architecture.md)
