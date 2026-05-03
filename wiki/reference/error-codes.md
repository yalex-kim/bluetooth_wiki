# Bluetooth Error Code Reference

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> Quick lookup for HCI Status Codes and ATT Error Codes.
> These appear in HCI events (Status field) and ATT_ERROR_RSP PDUs respectively.

---

## HCI Error / Status Codes

Returned in the `Status` field of:
- `HCI_Command_Complete` event
- `HCI_Command_Status` event
- `HCI_Disconnection_Complete` event (Reason field)
- Most other HCI events

| Code | Name | Common Cause |
|------|------|-------------|
| 0x00 | Success | — |
| 0x01 | Unknown HCI Command | Command not supported by this controller |
| 0x02 | Unknown Connection Identifier | Invalid connection handle |
| 0x03 | Hardware Failure | Controller hardware error |
| 0x04 | Page Timeout | BR/EDR paging timed out |
| 0x05 | Authentication Failure | PIN or link key incorrect |
| 0x06 | PIN or Key Missing | Bonding key not available |
| 0x07 | Memory Capacity Exceeded | Controller out of memory (e.g. filter accept list full) |
| 0x08 | Connection Timeout | Supervision timeout fired |
| 0x09 | Connection Limit Exceeded | Max connections reached |
| 0x0A | Synchronous Connection Limit To A Device Exceeded | Max SCO/eSCO connections to peer |
| 0x0B | Connection Already Exists | Already connected to this peer |
| 0x0C | Command Disallowed | Command not permitted in current state |
| 0x0D | Rejected due to Limited Resources | No buffer space |
| 0x0E | Rejected Due To Security Reasons | Security mode mismatch |
| 0x0F | Rejected due to Unacceptable BD ADDR | Address not acceptable |
| 0x10 | Connection Accept Timeout Exceeded | Connection accept timeout expired |
| 0x11 | Unsupported Feature or Parameter Value | Feature/parameter not supported |
| 0x12 | Invalid HCI Command Parameters | Parameter out of range or invalid combination |
| 0x13 | Remote User Terminated Connection | Peer closed connection normally |
| 0x14 | Remote Device Terminated Connection due to Low Resources | Peer closed: out of resources |
| 0x15 | Remote Device Terminated Connection due to Power Off | Peer closed: powering off |
| 0x16 | Connection Terminated By Local Host | Local host closed connection |
| 0x17 | Repeated Attempts | Too many pairing attempts |
| 0x18 | Pairing Not Allowed | Pairing rejected |
| 0x19 | Unknown LMP PDU | Unrecognized LMP PDU |
| 0x1A | Unsupported Remote Feature | Peer doesn't support requested feature |
| 0x1B | SCO Offset Rejected | SCO offset not acceptable |
| 0x1C | SCO Interval Rejected | SCO interval not acceptable |
| 0x1D | SCO Air Mode Rejected | SCO air mode not acceptable |
| 0x1E | Invalid LMP Parameters / Invalid LL Parameters | Invalid parameters in LMP/LL PDU |
| 0x1F | Unspecified Error | Generic error |
| 0x20 | Unsupported LMP Parameter Value / Unsupported LL Parameter Value | Parameter value not supported |
| 0x21 | Role Change Not Allowed | Role switch rejected |
| 0x22 | LMP Response Timeout / LL Response Timeout | Response not received in time |
| 0x23 | LMP Error Transaction Collision / LL Procedure Collision | Simultaneous PDU conflict |
| 0x24 | LMP PDU Not Allowed | PDU not allowed in current state |
| 0x25 | Encryption Mode Not Acceptable | Encryption mode mismatch |
| 0x26 | Link Key cannot be Changed | Key change not permitted |
| 0x27 | Requested QoS Not Supported | QoS parameters not supported |
| 0x28 | Instant Passed | LL Instant has already passed |
| 0x29 | Pairing With Unit Key Not Supported | Unit key pairing not supported |
| 0x2A | Different Transaction Collision | Collision of different transactions |
| 0x2B | Reserved for future use | — |
| 0x2C | QoS Unacceptable Parameter | QoS parameter not acceptable |
| 0x2D | QoS Rejected | QoS rejected by remote |
| 0x2E | Channel Classification Not Supported | Channel map classification not supported |
| 0x2F | Insufficient Security | Security level insufficient |
| 0x30 | Parameter Out Of Mandatory Range | Parameter outside mandatory range |
| 0x31 | Reserved for future use | — |
| 0x32 | Role Switch Pending | Role switch in progress |
| 0x33 | Reserved for future use | — |
| 0x34 | Reserved Slot Violation | Slot timing violation |
| 0x35 | Role Switch Failed | Role switch attempt failed |
| 0x36 | Extended Inquiry Response Too Large | EIR data exceeds limit |
| 0x37 | Secure Simple Pairing Not Supported By Host | SSP not supported by host |
| 0x38 | Host Busy - Pairing | Host is busy with another pairing |
| 0x39 | Rejected due to No Suitable Channel Found | No suitable channel available |
| 0x3A | Controller Busy | Controller is busy, retry later |
| 0x3B | Unacceptable Connection Parameters | Connection parameters rejected |
| 0x3C | Advertising Timeout | Extended advertising timeout |
| 0x3D | Connection Terminated due to MIC Failure | MIC verification failed (encryption error) |
| 0x3E | Connection Failed to be Established / Synchronization Timeout | Connection setup failed |
| 0x3F | Previously used | — |
| 0x40 | Coarse Clock Adjustment Rejected but Will Try to Adjust Using Clock Dragging | Clock adjustment fallback |
| 0x41 | Type0 Submap Not Defined | CSB type 0 submap missing |
| 0x42 | Unknown Advertising Identifier | Advertising_Handle not found |
| 0x43 | Limit Reached | Resource limit hit (e.g. max advertising sets) |
| 0x44 | Operation Cancelled by Host | Host cancelled pending operation |
| 0x45 | Packet Too Long | LL PDU exceeds max length |
| 0x46 | Too Late | Operation requested too late (CS-related) |
| 0x47 | Too Early | Operation requested too early (CS-related) |
| 0x48 | Insufficient Channels | Not enough suitable channels for the operation |

> Codes 0x49–0xFF are reserved. `[Core 6.2, Vol 1, Part F]`

---

## Frequently Seen HCI Codes (Developer Notes)

- **0x02 Unknown Connection Identifier** — typically means you're using a stale connection handle after a disconnect event; always discard handles on `HCI_Disconnection_Complete`.
- **0x0C Command Disallowed** — command not permitted in current state; e.g. calling `HCI_LE_Set_Advertising_Enable` while already advertising, or `HCI_LE_Enable_Encryption` on a Peripheral (only the Central initiates encryption).
- **0x12 Invalid HCI Command Parameters** — one of your parameter values is out of range or an invalid combination; check the command's parameter constraints carefully.
- **0x13 Remote User Terminated Connection** — normal disconnect initiated by the peer; not an error condition.
- **0x16 Connection Terminated By Local Host** — local host closed the connection; not an error condition.
- **0x22 LMP Response Timeout / LL Response Timeout** — peer did not respond to an LL procedure (encryption start, feature exchange, connection update) in time; usually means the peer is out of range or unresponsive.
- **0x28 Instant Passed** — LL channel map update or connection parameter update instant was already in the past when processed; schedule with more lead time and retry.
- **0x3B Unacceptable Connection Parameters** — Central rejected the Peripheral's L2CAP Connection Parameter Update Request; negotiate parameters within the Central's acceptable range.
- **0x3D Connection Terminated due to MIC Failure** — decryption of a received packet failed; most commonly caused by a key mismatch after re-bonding without clearing the old keys on both sides.
- **0x3E Connection Failed to be Established / Synchronization Timeout** — common during `HCI_LE_Create_Connection` when the peer is not advertising or is out of range; also returned for periodic advertising sync timeout.

---

## ATT Error Codes

Returned in `ATT_ERROR_RSP` PDU. Format: `[Opcode_In_Error (1B)] [Attribute_Handle (2B)] [Error_Code (1B)]`.

| Code | Name | Description | Common Cause |
|------|------|-------------|-------------|
| 0x01 | Invalid Handle | The attribute handle given was not valid on this server. | Handle 0x0000 passed, or beyond server's max handle |
| 0x02 | Read Not Permitted | The attribute cannot be read. | Characteristic has Write-only property |
| 0x03 | Write Not Permitted | The attribute cannot be written. | Characteristic is Read-only (e.g. measurement value) |
| 0x04 | Invalid PDU | The attribute PDU was invalid. | Incorrect PDU length or structure |
| 0x05 | Insufficient Authentication | The attribute requires authentication before it can be read or written. | Need to pair/bond before accessing; trigger pairing |
| 0x06 | Request Not Supported | ATT Server does not support the request received from the client. | Server doesn't implement this ATT request type |
| 0x07 | Invalid Offset | Offset specified was past the end of the attribute. | `ATT_READ_BLOB_REQ` offset too large |
| 0x08 | Insufficient Authorization | The attribute requires authorization before it can be read or written. | Authorization beyond pairing/encryption required |
| 0x09 | Prepare Queue Full | Too many prepare writes have been queued. | Flush or execute pending prepared writes first |
| 0x0A | Attribute Not Found | No attribute found within the given attribute handle range. | Wrong handle range in Read_By_Type or Find_By_Type |
| 0x0B | Attribute Not Long | The attribute cannot be read using the `ATT_READ_BLOB_REQ` PDU. | `ATT_READ_BLOB_REQ` on a short (≤ ATT_MTU−1 byte) attribute |
| 0x0C | Encryption Key Size Too Short | The Encryption Key Size used for encrypting this link is too short. | Increase minimum key size; enforce 128-bit keys |
| 0x0D | Invalid Attribute Value Length | The attribute value length is invalid for the operation. | Write value length doesn't match characteristic format |
| 0x0E | Unlikely Error | The attribute request encountered an error that was unlikely and could not be completed. | Internal server error; report as bug |
| 0x0F | Insufficient Encryption | The attribute requires encryption before it can be read or written. | Encrypt the link before accessing |
| 0x10 | Unsupported Group Type | The attribute type is not a supported grouping attribute as defined by a higher layer specification. | `ATT_READ_BY_GROUP_TYPE` with unsupported UUID |
| 0x11 | Insufficient Resources | Insufficient Resources to complete the request. | Server cannot complete the request |
| 0x12 | Database Out Of Sync | The server requests the client to rediscover the database. | Server changed its attribute database (GATT caching, 5.1+) |
| 0x13 | Value Not Allowed | The attribute parameter value was not allowed. | Written value violates server's value constraints |
| 0x80–0x9F | Application Error | Application error code defined by a higher layer specification. | Server-specific; check the relevant profile spec |
| 0xE0–0xFF | Common Profile and Service Error Codes | Common profile and service error codes. | Profile-defined; see profile spec for meaning |

> ATT Error Codes 0x14–0x7F are reserved. `[Core 6.2, Vol 3, Part F, §3.4.1.1]`

---

## GATT-Level Errors (Common Patterns)

Errors that arise from GATT procedures rather than raw ATT operations:

- **0x0A (Attribute Not Found)** during service discovery — normal termination signal, not a fatal error. `ATT_READ_BY_GROUP_TYPE` and `ATT_READ_BY_TYPE` return this to indicate the end of the handle range; iterate until received.
- **0x05 (Insufficient Authentication)** on CCCD write — server requires pairing; initiate SMP pairing and retry the write after the security level is established.
- **0x0F (Insufficient Encryption)** after pairing — pairing completed but the link is not yet encrypted; call `HCI_LE_Enable_Encryption` and retry.
- **0x12 (Database Out Of Sync)** — GATT caching (introduced in Core 5.1): the client's cached handles are stale because the server's attribute database changed. Re-run full service discovery, then update the Client Supported Features characteristic to re-enable caching.
- **0x80–0x9F (Application Error)** — defined per profile; for example `0x80` in HRS means "procedure already in progress". Consult the relevant profile specification for the specific code meaning.

---

## See Also

- [HCI Command Reference](hci-commands.md) — command opcodes and parameters
- [HCI Sequences](hci-sequences.md) — where these error codes appear in flows
- [Security](../concepts/security.md) — pairing/encryption (resolves 0x05, 0x0F)
- [BLE Architecture](../concepts/ble-architecture.md) — ATT/GATT layer description

---

*Source: [Core 6.2, Vol 1, Part F (HCI Error Codes)](../../sources/specs/6.2/Core_v6.2.md) and [Core 6.2, Vol 3, Part F §3.4.1 (ATT Error Codes)](../../sources/specs/6.2/Core_v6.2.md)*
