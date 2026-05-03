# ATT and GATT — Protocol Deep Dive

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> ATT (Attribute Protocol) is the wire protocol. GATT (Generic Attribute Profile) is the application layer built on top of it.
> For a list of standard GATT services and profiles, see [profiles-and-services.md](profiles-and-services.md).

---

## Overview

```
Application
    └── GATT (Vol 3, Part G)   — service/characteristic model, caching, operations
         └── ATT  (Vol 3, Part F)   — PDU framing, permissions, MTU
              └── L2CAP CID 0x0004 (classic ATT bearer)
              └── L2CAP EATT  PSM 0x0027 (enhanced bearer, 5.2+)
```

- **ATT bearer (classic)**: fixed L2CAP CID 0x0004, one channel per connection, sequential request/response
- **EATT bearer (5.2+)**: CoC (Credit Based) channels over PSM 0x0027, multiple simultaneous bearers, parallel request/response

---

## ATT Default MTU

| Scenario | Default ATT_MTU |
|----------|----------------|
| LE (pre-negotiation) | 23 bytes |
| LE (post-negotiation) | Up to 517 bytes (5.0+ with DLE 251-byte payload) |
| BR/EDR | 48 bytes |
| EATT channel minimum | **64 bytes** |

After `ATT_EXCHANGE_MTU_REQ/RSP`, both sides use `min(Client_Rx_MTU, Server_Rx_MTU)` as the effective MTU.

---

## MTU Negotiation Flow

```
Client                                    Server
  |-- ATT_EXCHANGE_MTU_REQ (0x02) -------->|
  |   Client_Rx_MTU = 512                  |
  |<------- ATT_EXCHANGE_MTU_RSP (0x03) ---|
  |         Server_Rx_MTU = 247            |
  |                                        |
  Effective MTU = min(512, 247) = 247 bytes
```

Rules:
- Client initiates; shall be sent **at most once** per connection on the classic ATT bearer
- Client_Rx_MTU must be ≥ 23 (default ATT_MTU)
- New MTU takes effect before the next PDU is sent
- A device acting as both client and server must use the same MTU in both roles

**Practical tip**: Request MTU immediately after connection establishment. Most stacks accept up to 517 bytes on LE (limited by DLE payload 251 + overhead).

---

## ATT PDU Opcode Table

[Core 6.2, Vol 3, Part F, §3.4.8 Table 3.43]

| Opcode | PDU Name | Direction | Parameters |
|--------|----------|-----------|------------|
| 0x01 | ATT_ERROR_RSP | S→C | Req Opcode, Handle, Error Code |
| 0x02 | ATT_EXCHANGE_MTU_REQ | C→S | Client Rx MTU |
| 0x03 | ATT_EXCHANGE_MTU_RSP | S→C | Server Rx MTU |
| 0x04 | ATT_FIND_INFORMATION_REQ | C→S | Start Handle, End Handle |
| 0x05 | ATT_FIND_INFORMATION_RSP | S→C | Format, Information Data |
| 0x06 | ATT_FIND_BY_TYPE_VALUE_REQ | C→S | Start, End, Type UUID, Value |
| 0x07 | ATT_FIND_BY_TYPE_VALUE_RSP | S→C | Handles Info List |
| 0x08 | ATT_READ_BY_TYPE_REQ | C→S | Start Handle, End Handle, UUID |
| 0x09 | ATT_READ_BY_TYPE_RSP | S→C | Length, Attribute Data List |
| 0x0A | ATT_READ_REQ | C→S | Attribute Handle |
| 0x0B | ATT_READ_RSP | S→C | Attribute Value |
| 0x0C | ATT_READ_BLOB_REQ | C→S | Handle, Value Offset |
| 0x0D | ATT_READ_BLOB_RSP | S→C | Part Attribute Value |
| 0x0E | ATT_READ_MULTIPLE_REQ | C→S | Handle Set |
| 0x0F | ATT_READ_MULTIPLE_RSP | S→C | Value Set |
| 0x10 | ATT_READ_BY_GROUP_TYPE_REQ | C→S | Start, End, UUID |
| 0x11 | ATT_READ_BY_GROUP_TYPE_RSP | S→C | Length, Attribute Data List |
| 0x12 | ATT_WRITE_REQ | C→S | Handle, Value |
| 0x13 | ATT_WRITE_RSP | S→C | (none) |
| 0x16 | ATT_PREPARE_WRITE_REQ | C→S | Handle, Offset, Part Value |
| 0x17 | ATT_PREPARE_WRITE_RSP | S→C | Handle, Offset, Part Value (echo) |
| 0x18 | ATT_EXECUTE_WRITE_REQ | C→S | Flags (0x00=cancel, 0x01=execute) |
| 0x19 | ATT_EXECUTE_WRITE_RSP | S→C | (none) |
| 0x1B | ATT_HANDLE_VALUE_NTF | S→C | Handle, Value |
| 0x1D | ATT_HANDLE_VALUE_IND | S→C | Handle, Value |
| 0x1E | ATT_HANDLE_VALUE_CFM | C→S | (none) |
| 0x20 | ATT_READ_MULTIPLE_VARIABLE_REQ | C→S | Set Of Handles |
| 0x21 | ATT_READ_MULTIPLE_VARIABLE_RSP | S→C | Length-Value Tuples |
| 0x23 | ATT_MULTIPLE_HANDLE_VALUE_NTF | S→C | Handle-Length-Value Tuples |
| 0x52 | ATT_WRITE_CMD | C→S | Handle, Value (no response) |
| 0xD2 | ATT_SIGNED_WRITE_CMD | C→S | Handle, Value, Auth Signature |

> **Note**: `ATT_SIGNED_WRITE_CMD` (0xD2) must **not** be used on an EATT bearer.

---

## ATT Permission Model

Each attribute has four orthogonal permission axes [Core 6.2, Vol 3, Part F, §3.2.5]:

| Axis | Options |
|------|---------|
| Access | Readable, Writable, or both |
| Encryption | Encryption required / not required |
| Authentication | Authentication required / not required |
| Authorization | Authorization required / not required |

**Security error codes returned in ATT_ERROR_RSP**:

| Error Code | Meaning | Trigger |
|-----------|---------|---------|
| 0x05 | Insufficient Authentication | Link not authenticated; need pairing |
| 0x08 | Insufficient Authorization | Application-level authorization missing |
| 0x0C | Encryption Key Size Too Short | Paired but key too short |
| 0x0F | Insufficient Encryption | Link not encrypted; need encryption |

**Typical permission combinations**:

| Use Case | Permissions |
|----------|-------------|
| Public readable (e.g., Device Name) | Read only, no security |
| Config writable by bonded peer | Write, encryption required |
| Sensitive health data | Read+Write, authentication required |
| OTA control point | Write, authentication + encryption |

---

## Long Read (> MTU–1 bytes)

When an attribute value exceeds `ATT_MTU – 1` bytes, use `ATT_READ_BLOB_REQ` with increasing offsets:

```
Client                                 Server
  |-- ATT_READ_REQ (0x0A) ----------->|  read first (MTU-1) bytes
  |<------- ATT_READ_RSP (0x0B) ------|
  |-- ATT_READ_BLOB_REQ (offset=N) -->|  read next chunk
  |<------- ATT_READ_BLOB_RSP --------|
  |   (repeat until RSP < MTU-1)      |
```

- Stop when the response is shorter than `ATT_MTU – 1` bytes (last chunk).
- Server returns `ATT_ERROR_RSP 0x07 (Invalid Offset)` if offset ≥ attribute length.

---

## Long Write — Prepare/Execute

For attribute values that exceed `ATT_MTU – 5` bytes per PDU, use the Prepare Queue:

```
Client                                        Server
  |-- ATT_PREPARE_WRITE_REQ (offset=0) ------>|
  |<--- ATT_PREPARE_WRITE_RSP (echo) ----------|  client verifies echo
  |-- ATT_PREPARE_WRITE_REQ (offset=N) ------>|
  |<--- ATT_PREPARE_WRITE_RSP (echo) ----------|
  |-- ATT_EXECUTE_WRITE_REQ (Flags=0x01) ---->|  atomic commit
  |<--- ATT_EXECUTE_WRITE_RSP (0x19) ----------|
```

- Each PREPARE carries up to `ATT_MTU – 5` bytes of payload.
- The server echoes handle + offset + value back; client must verify for transmission integrity.
- `Flags = 0x00` in EXECUTE cancels all queued writes without applying them.
- Server returns `0x09 (Prepare Queue Full)` when the queue is exhausted.

---

## Reliable Write

Reliable Write is a GATT-level procedure [Core 6.2, Vol 3, Part G, §4.9.5] that adds an integrity guarantee:

1. Client sends `ATT_PREPARE_WRITE_REQ` with the intended value.
2. Server echoes the value back in `ATT_PREPARE_WRITE_RSP`.
3. Client **verifies the echo** matches the sent value — if not, it cancels with `EXECUTE Flags=0x00`.
4. Only after successful verification does the client send `EXECUTE Flags=0x01`.

This guarantees that the value actually committed to the server is exactly what the client intended, even across unreliable transports.

---

## GATT Service / Characteristic Model

```
GATT Server Attribute Table
  ├── Primary Service Declaration  (UUID 0x2800)
  │   ├── Include Declaration      (UUID 0x2802) [optional]
  │   ├── Characteristic Declaration (UUID 0x2803)
  │   │   ├── Characteristic Value  (client-defined UUID)
  │   │   ├── Client Characteristic Configuration Descriptor (CCCD) 0x2902
  │   │   ├── Server Characteristic Configuration Descriptor (SCCD) 0x2903
  │   │   └── Characteristic User Description 0x2901
  │   └── (more characteristics...)
  └── Secondary Service Declaration (UUID 0x2801)
```

**CCCD values**:

| Bits | Meaning |
|------|---------|
| 0x0000 | Notifications and indications disabled |
| 0x0001 | Notifications enabled |
| 0x0002 | Indications enabled |

CCCD state is **bonded-device-specific** — the server stores a separate CCCD value per bonded client.

---

## Notification vs. Indication

| Property | Notification (0x1B) | Indication (0x1D) |
|----------|--------------------|--------------------|
| Client ack required | No | Yes (ATT_HANDLE_VALUE_CFM) |
| Delivery guarantee | Best effort | Confirmed |
| Can queue multiple | Yes | No (must wait for CFM) |
| Use case | High-frequency sensor data | Critical events (e.g., Service Changed) |

---

## GATT Caching (5.1+)

Clients may cache GATT service structure (handles, UUIDs) across connections to avoid rediscovery [Core 6.2, Vol 3, Part G, §2.5.2].

### Service Changed Characteristic (UUID 0x2A05)

- Properties: **Indicate only** (0x20)
- Value: Start Handle + End Handle of changed range (4 bytes total)
- Sent by the server when services are added, removed, or modified
- Client must re-discover the affected handle range after receiving an indication

### Database Hash Characteristic (UUID 0x2B2A) [5.1+]

- Properties: **Read only** (0x02)
- Value: 128-bit AES-CMAC hash over all GATT service definition attributes
- Recalculated whenever the service database changes
- Client reads this hash to determine if re-discovery is needed without going through full discovery

### Robust Caching Flow

```
Reconnect
  ├── Client reads Database Hash (0x2B2A)
  │     ├── Hash unchanged → cache still valid, skip discovery
  │     └── Hash changed   → re-discover affected services
  └── If Robust Caching enabled on server:
        Server returns 0x12 (Database Out Of Sync) on first access
        → Client must read Database Hash to become "change-aware"
```

**Change-aware** vs **change-unaware**:
- A client becomes change-aware by: (a) reading the Database Hash, (b) receiving and confirming a Service Changed indication, or (c) receiving the 0x12 error.
- A change-unaware client receives `ATT_ERROR_RSP 0x12` on its first request after reconnection.

---

## EATT — Enhanced ATT Bearer (5.2+)

EATT replaces the single classic ATT bearer (CID 0x0004) with one or more L2CAP CoC channels, enabling **parallel request/response** [Core 6.2, Vol 3, Part F, §5.3].

| Property | Classic ATT bearer | EATT bearer |
|----------|--------------------|-------------|
| L2CAP channel | Fixed CID 0x0004 | Dynamic CoC, PSM 0x0027 |
| Channels per connection | 1 | Multiple (negotiated) |
| Parallelism | Sequential (one outstanding request) | Parallel requests on separate bearers |
| Minimum MTU | 23 bytes | **64 bytes** |
| Signed writes | Allowed | **Not allowed** (0xD2) |
| Transport | LE | LE + BR/EDR |

### Establishing EATT

```
Client                                         Server
  |-- L2CAP LE_CREDIT_BASED_CONNECTION_REQ  -->|  PSM=0x0027
  |<-- L2CAP LE_CREDIT_BASED_CONNECTION_RSP ---|
  |   (repeat for additional bearers)           |
  |-- ATT_EXCHANGE_MTU_REQ (per bearer) ------->|
```

- Server must support EATT if the **Enhanced ATT Bearer** bit is set in Server Supported Features (0x2B3A) characteristic.
- Client advertises EATT support via **Client Supported Features** (0x2B29) characteristic bit 1.
- A client can open multiple EATT bearers and distribute requests across them for higher throughput.

---

## Version History

| Version | Change |
|---------|--------|
| 4.0 | ATT and GATT introduced; basic read/write/notify/indicate |
| 4.2 | Long-term Key and IRK distribution; no ATT/GATT protocol changes |
| 5.1 | **GATT Caching**: Database Hash (0x2B2A) + Service Changed indication for efficient cache invalidation |
| 5.2 | **EATT**: Enhanced ATT bearer via L2CAP CoC PSM 0x0027; parallel requests; 64-byte min MTU |
| 5.2 | `ATT_READ_MULTIPLE_VARIABLE_REQ/RSP` (0x20/0x21) for variable-length handle reads |
| 5.2 | `ATT_MULTIPLE_HANDLE_VALUE_NTF` (0x23) for batched notifications |
| 5.3 | No ATT/GATT protocol changes |
| 5.4 | No ATT/GATT protocol changes |
| 6.0 | No ATT/GATT protocol changes |
| 6.1 | No ATT/GATT protocol changes |
| 6.2 | No ATT/GATT protocol changes |

---

## See Also

- [profiles-and-services.md](profiles-and-services.md) — GATT services and profiles list (A2DP, HFP, LE Audio, etc.)
- [hci-sequences.md](../reference/hci-sequences.md) — GATT discovery, read/write, subscribe HCI flows
- [error-codes.md](../reference/error-codes.md) — ATT error codes (0x01–0xFF)
- [ble-architecture.md](ble-architecture.md) — where ATT/GATT fits in the BLE stack

---

*Source: [Core 6.2, Vol 3, Part F §3 (ATT)](../../sources/specs/6.2/Core_v6.2.md) and [Core 6.2, Vol 3, Part G §4 (GATT)](../../sources/specs/6.2/Core_v6.2.md)*
