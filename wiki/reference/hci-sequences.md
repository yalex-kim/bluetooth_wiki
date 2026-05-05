# HCI Command Sequences

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> Step-by-step HCI command flows for common BLE implementation tasks.
> Each sequence shows commands in order, with key parameters and expected events.
> Central = the device that initiates connection. Peripheral = the device that advertises.

---

## 1. Controller Initialization

Every host must run this sequence after power-on or HCI reset before using the controller.

1. `HCI_Reset` (0x0C03) — Reset controller state; all parameters revert to defaults.
   → `HCI_Command_Complete`: Status=0x00
   > Do not send any other commands until this Command_Complete arrives. [Core 6.2, Vol 4, Part E, §7.3.2]

2. `HCI_Read_Local_Version_Information` (0x1001) — Check HCI and LMP/LL versions to determine feature availability.
   → `HCI_Command_Complete`: HCI_Version, HCI_Subversion, LMP_Version, Manufacturer_Name, LMP_Subversion

3. `HCI_Read_Local_Supported_Commands` (0x1002) — Read the 64-byte bitmask of supported commands before calling any optional command.
   → `HCI_Command_Complete`: Supported_Commands[64]

4. `HCI_LE_Read_Local_Supported_Features_Page_0` (0x2003) — Read LE feature bits (DLE, 2M PHY, LE Secure Connections, etc.).
   → `HCI_Command_Complete`: LE_Features (8 bytes)
   > On 6.0+ controllers, prefer `HCI_LE_Read_All_Local_Supported_Features` (0x2087) to get features across all pages.

5. `HCI_LE_Read_Buffer_Size` [v1 or v2] — Determine LE TX buffer count and packet length.
   - v1 (0x2002, since 4.0): returns LE_ACL_Data_Packet_Length, Total_Num_LE_ACL_Data_Packets
   - v2 (0x2060, since 5.2): additionally returns ISO_Data_Packet_Length, Total_Num_ISO_Data_Packets (required if ISO is supported)
   → `HCI_Command_Complete`: buffer sizes and counts
   > If Total_Num_LE_ACL_Data_Packets = 0, the controller shares a BR/EDR buffer — use `HCI_Read_Buffer_Size` (0x1005) instead. [Core 6.2, Vol 4, Part E, §7.8.2]

6. `HCI_Set_Event_Mask` (0x0C01) — Enable the BR/EDR and general events the host wants to receive.
   → `HCI_Command_Complete`: Status=0x00
   > Typical mask enables: Disconnection_Complete (bit 4), Encryption_Change (bit 7), Read_Remote_Version_Information_Complete (bit 11).

7. `HCI_LE_Set_Event_Mask` (0x2001) — Enable the LE events the host wants to receive.
   → `HCI_Command_Complete`: Status=0x00
   > Key bits: bit 0=LE_Connection_Complete, bit 1=LE_Advertising_Report, bit 4=LE_Long_Term_Key_Request, bit 9=LE_Enhanced_Connection_Complete. Enable all bits for maximum coverage.

8. `HCI_Read_BD_ADDR` (0x1009) — Read the controller's public IEEE address.
   → `HCI_Command_Complete`: BD_ADDR (6 bytes)

9. *(Optional)* `HCI_LE_Set_Random_Address` (0x2005) — Set a static random address (MSBs 0b11xxxxxx).
   → `HCI_Command_Complete`: Status=0x00

10. *(Optional)* `HCI_LE_Set_Resolvable_Private_Address_Timeout` [v1] (0x202E) or [v2] (0x209E, 6.1+) — Configure RPA rotation interval.
    - v1: RPA_Timeout=900 (s) — fixed 15-minute rotation
    - v2: RPA_Timeout_Min=480, RPA_Timeout_Max=900 — randomized rotation window (6.1 privacy hardening)
    → `HCI_Command_Complete`: Status=0x00

---

## 2. BLE Connection Establishment

### 2a. Peripheral Side (Advertising and Accepting a Connection)

1. `HCI_LE_Set_Advertising_Parameters` (0x2006)
   — Advertising_Type=0x00 (ADV_IND, connectable undirected), Advertising_Interval_Min=0x0800 (1280 ms), Advertising_Interval_Max=0x0800, Own_Address_Type=0x00 (public), Advertising_Channel_Map=0x07 (all three channels)
   → `HCI_Command_Complete`: Status=0x00

2. `HCI_LE_Set_Advertising_Data` (0x2008)
   — Advertising_Data_Length=N, Advertising_Data=\[AD structures: Flags, Local Name, UUIDs, etc.\]
   → `HCI_Command_Complete`: Status=0x00

3. *(Optional)* `HCI_LE_Set_Scan_Response_Data` (0x2009) — Provide data for scan responses.
   → `HCI_Command_Complete`: Status=0x00

4. `HCI_LE_Set_Advertising_Enable` (0x200A) — Advertising_Enable=0x01
   → `HCI_Command_Complete`: Status=0x00
   > Controller begins advertising. When the Central sends a CONNECT_IND, advertising stops automatically and the controller generates a connection event.

5. ← `LE_Connection_Complete` (Event 0xFF, Subevent 0x01) *or* `LE_Enhanced_Connection_Complete` (Subevent 0x0A)
   — Status=0x00, Connection_Handle, Role=0x01 (Peripheral), Peer_Address_Type, Peer_Address, Conn_Interval, Peripheral_Latency, Supervision_Timeout
   > The connection is now established. Advertising is automatically disabled.

> **5.0+ extended advertising**: Replace steps 1–4 with `HCI_LE_Set_Extended_Advertising_Parameters` (0x2036), `HCI_LE_Set_Extended_Advertising_Data` (0x2037), and `HCI_LE_Set_Extended_Advertising_Enable` (0x2039). Extended advertising supports multiple simultaneous advertising sets and >31 bytes of data.

### 2b. Central Side (Scanning and Initiating a Connection)

1. `HCI_LE_Set_Scan_Parameters` (0x200B)
   — LE_Scan_Type=0x01 (active), LE_Scan_Interval=0x0060 (60 ms), LE_Scan_Window=0x0030 (30 ms), Own_Address_Type=0x00, Scanning_Filter_Policy=0x00
   → `HCI_Command_Complete`: Status=0x00

2. `HCI_LE_Set_Scan_Enable` (0x200C) — LE_Scan_Enable=0x01, Filter_Duplicates=0x01
   → `HCI_Command_Complete`: Status=0x00

3. ← `LE_Advertising_Report` (Event 0xFF, Subevent 0x02) — Controller reports an advertising PDU from the target peripheral.
   — Event_Type, Address_Type, Address, Data_Length, Data, RSSI

4. `HCI_LE_Set_Scan_Enable` (0x200C) — LE_Scan_Enable=0x00 (stop scanning before initiating)
   → `HCI_Command_Complete`: Status=0x00

5. `HCI_LE_Create_Connection` (0x200D)
   — LE_Scan_Interval=0x0060, LE_Scan_Window=0x0030, Initiator_Filter_Policy=0x00 (use Peer_Address), Peer_Address_Type, Peer_Address, Own_Address_Type=0x00, Conn_Interval_Min=0x0018 (30 ms), Conn_Interval_Max=0x0028 (50 ms), Max_Latency=0x0000, Supervision_Timeout=0x00C8 (2 s), Min_CE_Length=0x0000, Max_CE_Length=0x0000
   → `HCI_Command_Status`: Status=0x00 (command acknowledged, connection pending)

6. ← `LE_Connection_Complete` (Event 0xFF, Subevent 0x01) *or* `LE_Enhanced_Connection_Complete` (Subevent 0x0A)
   — Status=0x00, Connection_Handle, Role=0x00 (Central), Peer_Address_Type, Peer_Address, Conn_Interval, Peripheral_Latency, Supervision_Timeout
   > The connection is established. Both sides now share the same Connection_Handle reference.

> **5.0+ extended initiating**: Use `HCI_LE_Set_Extended_Scan_Parameters` (0x2041) + `HCI_LE_Set_Extended_Scan_Enable` (0x2042) for scanning, and `HCI_LE_Extended_Create_Connection` (0x2043) for initiating — supports multi-PHY and receives `LE_Enhanced_Connection_Complete`.

---

## 3. LE Secure Connections Pairing (LESC)

SMP messages (Pairing Request, Pairing Response, DHKey Check, etc.) are L2CAP PDUs on CID 0x0006, handled entirely by the host stack. Only the P-256 key generation and DHKey computation go through HCI. The sequence below shows the crypto-primitive HCI calls within the broader SMP flow.

> Note: A controller can only execute one `HCI_LE_Read_Local_P-256_Public_Key` or `HCI_LE_Generate_DHKey` at a time — only one LESC pairing can proceed concurrently per controller. [Core 6.2, Vol 3, Part H, §2.3.5.6]

1. *SMP: Pairing Request / Pairing Response* — Exchanged as L2CAP PDUs. Hosts negotiate IO Capabilities, OOB flag, Authentication Requirements (MITM, SC bits), and key distribution fields. Not HCI commands.

2. `HCI_LE_Read_Local_P-256_Public_Key` (0x2025) — Request the controller to generate (or return a cached) P-256 key pair.
   → `HCI_Command_Status`: Status=0x00
   → *(async)* `LE_Read_Local_P256_Public_Key_Complete` (Subevent 0x08): Status=0x00, Local_P256_Public_Key (64 bytes)

3. *SMP: Public Key exchange* — Both devices exchange their 64-byte P-256 public keys as SMP PDUs over L2CAP.

4. `HCI_LE_Generate_DHKey [v2]` (0x205E) — Remote_P256_Public_Key (64 bytes from peer), Key_Type=0x01 (use generated private key, not debug key).
   → `HCI_Command_Status`: Status=0x00
   → *(async)* `LE_Generate_DHKey_Complete` (Subevent 0x09): Status=0x00, DH_Key (32 bytes)
   > If the remote public key is invalid, DH_Key will be all 0xFF. Abort pairing in that case. [Core 6.2, Vol 4, Part E, §7.7.65.9]

5. *SMP: Confirm / Random / DHKey Check exchange* — Host computes f4/g2/f5/f6 using the DHKey and nonces. Passkey entry or numeric comparison prompts are shown to the user at this stage. Not HCI commands.

6. *Key distribution* — LTK, IRK, and CSRK are exchanged as SMP PDUs over L2CAP after authentication.

7. **Central**: `HCI_LE_Enable_Encryption` (0x2019)
   — Connection_Handle, Random_Number=0x0000000000000000 (all zeros for LESC), Encrypted_Diversifier=0x0000 (all zeros for LESC), Long_Term_Key (16 bytes, from f5 key generation)
   → `HCI_Command_Status`: Status=0x00

8. **Peripheral**: ← `LE_Long_Term_Key_Request` (Event 0xFF, Subevent 0x05)
   — Connection_Handle, Random_Number=0x0000000000000000, Encrypted_Diversifier=0x0000
   > For LESC, the peripheral identifies this as a Secure Connections request by the all-zero Rand and EDIV.

9. **Peripheral**: `HCI_LE_Long_Term_Key_Request_Reply` (0x201A)
   — Connection_Handle, Long_Term_Key (16 bytes, same LTK derived from f5)
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

10. ← `HCI_Encryption_Change` (Event 0x08) on **both sides**
    — Status=0x00, Connection_Handle, Encryption_Enabled=0x01
    > Encryption is now active. The connection is bonded. Store the LTK and peer's identity address + IRK for future reconnections.

> **LL layer** (steps 7–10): These HCI calls drive the `LL_ENC_REQ` / `LL_ENC_RSP` / `LL_START_ENC_REQ` / `LL_START_ENC_RSP` PDU exchange at the Link Layer. [Core 6.2, Vol 6, Part B, §5.1.3]

---

## 4. Re-encryption on Reconnection (Bonded Devices)

After reconnecting to a previously bonded peer, the Central restores encryption using the stored LTK. No new SMP exchange is needed.

1. ← `LE_Connection_Complete` / `LE_Enhanced_Connection_Complete` — Connection established (see Section 2).

2. **Central**: `HCI_LE_Enable_Encryption` (0x2019)
   — Connection_Handle, Random_Number (8 bytes, stored from original pairing), Encrypted_Diversifier (2 bytes, stored), Long_Term_Key (16 bytes, stored LTK)
   → `HCI_Command_Status`: Status=0x00

3. **Peripheral**: ← `LE_Long_Term_Key_Request` (Event 0xFF, Subevent 0x05)
   — Connection_Handle, Random_Number, Encrypted_Diversifier (matches what Central sent)
   > Peripheral looks up the matching LTK using (Random_Number, Encrypted_Diversifier) as the key.

4. **Peripheral**: `HCI_LE_Long_Term_Key_Request_Reply` (0x201A)
   — Connection_Handle, Long_Term_Key (16 bytes, stored LTK)
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle
   > If no matching LTK exists: send `HCI_LE_Long_Term_Key_Request_Negative_Reply` (0x201B) — the Central will disconnect.

5. ← `HCI_Encryption_Change` (Event 0x08) on **both sides**
   — Status=0x00, Connection_Handle, Encryption_Enabled=0x01

---

## 5. GATT Service Discovery and Operations

GATT operations are ATT PDUs carried as LE ACL data — they are not individual HCI commands.
The host sends them using `HCI_ACL_Data` packets, which are framed as:

```
HCI_ACL_Data header (4 bytes: Handle[12] | PB_Flag[2] | BC_Flag[2] | DataLen[16])
  └── L2CAP header (4 bytes: Length[16] | CID[16], CID=0x0004 for ATT)
        └── ATT PDU (OpCode + parameters)
```

All ATT operations require an active, complete connection (Status=0x00 in `LE_Connection_Complete`).

### 5a. MTU Negotiation

1. **Client** → ATT_Exchange_MTU_Request (OpCode 0x02): Client_Rx_MTU (e.g., 512)
2. **Server** → ATT_Exchange_MTU_Response (OpCode 0x03): Server_Rx_MTU (e.g., 247)
   > Negotiated MTU = min(Client_Rx_MTU, Server_Rx_MTU). Default ATT_MTU = 23 bytes (20 bytes payload).

### 5b. Discover All Primary Services

1. **Client** → ATT_Read_By_Group_Type_Request (OpCode 0x10): Starting_Handle=0x0001, Ending_Handle=0xFFFF, Attribute_Type=0x2800 (Primary Service UUID)
2. **Server** → ATT_Read_By_Group_Type_Response (OpCode 0x11): list of {Attribute_Handle, End_Group_Handle, UUID}
3. Repeat from the last End_Group_Handle + 1 until **Server** returns ATT_Error_Response (OpCode 0x01) with Error_Code=0x0A (Attribute Not Found).

> To find a specific service by UUID, use ATT_Find_By_Type_Value_Request (OpCode 0x06): Starting_Handle=0x0001, Ending_Handle=0xFFFF, Attribute_Type=0x2800, Attribute_Value=\[target 16- or 128-bit UUID\].

### 5c. Discover Characteristics Within a Service

1. **Client** → ATT_Read_By_Type_Request (OpCode 0x08): Starting_Handle=\[service start\], Ending_Handle=\[service end\], Attribute_Type=0x2803 (Characteristic declaration UUID)
2. **Server** → ATT_Read_By_Type_Response (OpCode 0x09): list of {Handle, Value={Properties, Value_Handle, UUID}}
3. Repeat until ATT_Error_Response 0x0A.

### 5d. Enable Notifications or Indications

Requires writing to the Client Characteristic Configuration Descriptor (CCCD) at the handle associated with the characteristic.

1. **Client** → ATT_Write_Request (OpCode 0x12): Handle=\[CCCD handle, UUID 0x2902\], Value=0x0001 (Notifications) *or* 0x0002 (Indications)
2. **Server** → ATT_Write_Response (OpCode 0x13)
   > Once enabled, the server can send ATT_Handle_Value_Notification (OpCode 0x1B) at any time. Indications use OpCode 0x1D and require ATT_Handle_Value_Confirmation (OpCode 0x1E) from the client.

### 5e. Read a Characteristic Value

1. **Client** → ATT_Read_Request (OpCode 0x0A): Attribute_Handle
2. **Server** → ATT_Read_Response (OpCode 0x0B): Attribute_Value (up to MTU-1 bytes)
   > For values larger than MTU-1 bytes, use ATT_Read_Blob_Request (OpCode 0x0C) with incrementing Value_Offset.

### 5f. Write a Characteristic Value

**With response** (confirmed write):
1. **Client** → ATT_Write_Request (OpCode 0x12): Attribute_Handle, Attribute_Value
2. **Server** → ATT_Write_Response (OpCode 0x13)

**Without response** (Write Without Response property required):
1. **Client** → ATT_Write_Command (OpCode 0x52): Attribute_Handle, Attribute_Value
   > No response is sent. The write is silently dropped if the server's buffer is full.

> **GATT caching (5.1+)**: After first discovery, store all handles and check the Database Hash (UUID 0x2B2A) on reconnection. If the hash matches, skip rediscovery. If the server sends a Service Changed indication (UUID 0x2A05), clear cached handles and rediscover. [Core 6.2, Vol 3, Part G, §2.5.2]

---

## 6. CIS Setup (LE Audio Unicast)

Requires a prior ACL connection. The Central configures the CIG, then creates CIS streams to one or more peripherals.

> For detailed timing and codec configuration, see [LE Audio — CIS Setup HCI Sequence](../concepts/le-audio.md#cis-setup).

**Central side:**

1. `HCI_LE_Set_CIG_Parameters` (0x2062)
   — CIG_ID=0x00, SDU_Interval_C→P=10000 µs (10 ms), SDU_Interval_P→C=10000 µs, Worst_Case_SCA=0x00, Packing=0x00 (sequential), Framing=0x00 (unframed), Max_Transport_Latency_C→P=40 ms, Max_Transport_Latency_P→C=40 ms, CIS_Count=1, CIS_ID=0x00, Max_SDU_C→P=100, Max_SDU_P→C=100, PHY_C→P=0x02 (2M), PHY_P→C=0x02, RTN_C→P=2, RTN_P→C=2
   → `HCI_Command_Complete`: Status=0x00, CIG_ID, CIS_Count, Connection_Handle\[0\] (pre-allocated CIS handle)

2. `HCI_LE_Create_CIS` (0x2064)
   — CIS_Count=1, CIS_Connection_Handle\[0\]=\[from step 1\], ACL_Connection_Handle\[0\]=\[existing ACL handle\]
   → `HCI_Command_Status`: Status=0x00

**Peripheral side (simultaneously):**

3. ← `LE_CIS_Request` (Event 0xFF, Subevent 0x1A)
   — ACL_Connection_Handle, CIS_Connection_Handle, CIG_ID, CIS_ID

4. `HCI_LE_Accept_CIS_Request` (0x2066) — Connection_Handle=\[CIS handle from event\]
   → `HCI_Command_Status`: Status=0x00

**Both sides:**

5. ← `LE_CIS_Established` (Event 0xFF, Subevent 0x19) on **both sides**
   — Status=0x00, Connection_Handle (CIS), CIG_Sync_Delay, CIS_Sync_Delay, Transport_Latency_C→P/P→C, PHY_C→P/P→C, NSE, ISO_Interval

6. `HCI_LE_Setup_ISO_Data_Path` (0x206E) on **both sides** (TX and RX directions separately)
   — Connection_Handle (CIS), Data_Path_Direction=0x00 (input/TX) *then* 0x01 (output/RX), Data_Path_ID=0x00 (HCI), Coding_Format=0x06 (LC3), Controller_Delay (µs)
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

---

## 7. BIS Setup (LE Audio Broadcast)

### 7a. Broadcaster (Transmitter)

[Core 5.2, Vol 6, Part B, §4.4.6]

Requires an extended advertising set configured as non-connectable non-scannable.

1. `HCI_LE_Set_Extended_Advertising_Parameters` (0x2036)
   — Advertising_Handle=0x00, Advertising_Event_Properties=0x0000 (non-connectable, non-scannable, non-legacy), Primary_Advertising_PHY=0x01 (1M), Secondary_Advertising_PHY=0x01 (1M)
   → `HCI_Command_Complete`: Status=0x00, Selected_TX_Power

2. `HCI_LE_Set_Extended_Advertising_Data` (0x2037)
   — Advertising_Handle=0x00, Operation=0x03 (complete data), Fragment_Preference=0x01, Advertising_Data_Length=N, Advertising_Data=\[AD structures: Service UUIDs, Broadcast_Name, etc.\]
   → `HCI_Command_Complete`: Status=0x00
   > Set the extended advertising payload. The BASE structure is carried in periodic advertising data (step 4), not here.

3. `HCI_LE_Set_Periodic_Advertising_Parameters` (0x203E)
   — Advertising_Handle=0x00, Periodic_Advertising_Interval_Min=0x0050 (100 ms), Periodic_Advertising_Interval_Max=0x0050
   → `HCI_Command_Complete`: Status=0x00

4. `HCI_LE_Set_Periodic_Advertising_Data` (0x203F)
   — Advertising_Handle=0x00, Operation=0x03 (complete data), Advertising_Data_Length=N, Advertising_Data=\[BASE LTV structure: BIG_Info, BIS codec configs, sampling rate, frame duration, etc.\]
   → `HCI_Command_Complete`: Status=0x00
   > The BASE (Basic Audio Announcement) LTV structure here tells receivers how to join and decode the BIG. Required before enabling periodic advertising.

5. `HCI_LE_Set_Extended_Advertising_Enable` (0x2039) — Enable=0x01, Num_Sets=1, Advertising_Handle=0x00
   → `HCI_Command_Complete`: Status=0x00
   > **Must precede Periodic Advertising Enable.** The periodic train rides on the extended advertising set; enabling periodic advertising before the extended set is active returns `Command Disallowed`. [Core 5.2, Vol 6, Part B, §4.4.6]

6. `HCI_LE_Set_Periodic_Advertising_Enable` (0x2040) — Enable=0x01, Advertising_Handle=0x00
   → `HCI_Command_Complete`: Status=0x00

7. `HCI_LE_Create_BIG` (0x2068)
   — BIG_Handle=0x00, Advertising_Handle=0x00, Num_BIS=1, SDU_Interval=10000 µs, Max_SDU=100, Max_Transport_Latency=40 ms, RTN=2, PHY=0x02 (2M), Packing=0x00, Framing=0x00, Encryption=0x00, Broadcast_Code (16 bytes, zeros for unencrypted)
   → `HCI_Command_Status`: Status=0x00

8. ← `LE_Create_BIG_Complete` (Event 0xFF, Subevent 0x1B)
   — Status=0x00, BIG_Handle, BIG_Sync_Delay, Transport_Latency_BIG, PHY, NSE, BN, ISO_Interval, Num_BIS, Connection_Handle\[\]

9. `HCI_LE_Setup_ISO_Data_Path` (0x206E)
   — Connection_Handle (BIS), Data_Path_Direction=0x00 (input/TX), Data_Path_ID=0x00, Coding_Format=0x06 (LC3)
   → `HCI_Command_Complete`: Status=0x00
   > The broadcaster can now send ISO SDUs. Use `HCI_Number_Of_Completed_Packets` events to track TX slot availability.

### 7b. Receiver (Broadcast Sink)

1. Set up extended scanning (see Section 2b, steps 1–2 using `HCI_LE_Set_Extended_Scan_Parameters` + `HCI_LE_Set_Extended_Scan_Enable`).

2. ← `LE_Extended_Advertising_Report` — Locate the broadcaster's advertising address and Advertising_SID.

3. `HCI_LE_Periodic_Advertising_Create_Sync` (0x2044)
   — Options=0x00, Advertising_SID=\[from report\], Advertiser_Address_Type, Advertiser_Address, Skip=0x0000, Sync_Timeout=0x0028 (4 s), Sync_CTE_Type=0x00
   → `HCI_Command_Status`: Status=0x00

4. ← `LE_Periodic_Advertising_Sync_Established` (Event 0xFF, Subevent 0x0E)
   — Status=0x00, Sync_Handle, Advertising_SID, Advertiser_Address, Periodic_Advertising_Interval

5. ← `LE_Periodic_Advertising_Report` (Subevent 0x0F) — Receive BASE structure (BIG/BIS topology and codec configuration) from the broadcaster's periodic advertising data.

6. `HCI_LE_BIG_Create_Sync` (0x206B)
   — BIG_Handle=0x00, Sync_Handle=\[from step 4\], Encryption=0x00, Broadcast_Code (zeros), MSE=0x00, BIG_Sync_Timeout=0x0028, Num_BIS=1, BIS\[0\]=0x01
   → `HCI_Command_Status`: Status=0x00

7. ← `LE_BIG_Sync_Established` (Event 0xFF, Subevent 0x1D)
   — Status=0x00, BIG_Handle, Transport_Latency_BIG, NSE, ISO_Interval, Num_BIS, Connection_Handle\[\]

8. `HCI_LE_Setup_ISO_Data_Path` (0x206E)
   — Connection_Handle (BIS), Data_Path_Direction=0x01 (output/RX), Data_Path_ID=0x00, Coding_Format=0x06 (LC3)
   → `HCI_Command_Complete`: Status=0x00

---

## 8. Connection Parameter Update

### 8a. Central-Initiated (Direct LL Update)

The Central directly instructs the controller to negotiate new parameters with the peer.

1. `HCI_LE_Connection_Update` (0x2013)
   — Connection_Handle, Conn_Interval_Min=0x0018 (30 ms), Conn_Interval_Max=0x0028 (50 ms), Max_Latency=0x0000, Supervision_Timeout=0x00C8 (2 s), Min_CE_Length=0x0000, Max_CE_Length=0x0000
   → `HCI_Command_Status`: Status=0x00

2. ← `LE_Connection_Update_Complete` (Event 0xFF, Subevent 0x03) on **both sides**
   — Status=0x00, Connection_Handle, Conn_Interval, Peripheral_Latency, Supervision_Timeout
   > The controller may apply different values than requested (within the requested range).

> **6.2 shorter intervals**: To request sub-7.5 ms intervals (down to 375 µs), use `HCI_LE_Connection_Rate_Request` (0x20A1) instead, which uses 125 µs ticks. The Central must support the LE Connection Rate feature (Feature bit 0x38). See [Core 6.2, Vol 4, Part E, §7.8.154].

### 8b. Peripheral-Initiated (L2CAP Signaling)

The peripheral cannot directly call `HCI_LE_Connection_Update`. It requests the change via L2CAP:

1. **Peripheral host** sends L2CAP LE Connection Parameter Update Request (signal code 0x12, CID 0x0005)
   — Interval_Min, Interval_Max, Peripheral_Latency, Timeout

2. **Central host** receives the L2CAP request. If accepted:
   - Sends L2CAP LE Connection Parameter Update Response (signal code 0x13): Result=0x0000 (accepted)
   - Issues `HCI_LE_Connection_Update` (0x2013) to its own controller with the requested parameters

3. ← `LE_Connection_Update_Complete` (Event 0xFF, Subevent 0x03) on **both sides**

> If the Central's controller supports the `LE_Remote_Connection_Parameter_Request` feature, the LL can also initiate the update at the link layer level. In that case the Central's host receives `LE_Remote_Connection_Parameter_Request` (Subevent 0x06) and replies with `HCI_LE_Remote_Connection_Parameter_Request_Reply` (0x2020) or `..._Negative_Reply` (0x2021). [Core 6.2, Vol 3, Part A, §4.20; Vol 4, Part E, §7.8.31]

---

## 9. Direction Finding — CTE / AoA / AoD (5.1+)

Direction Finding uses a **Constant Tone Extension (CTE)** appended to advertising or connection PDUs. The receiving device samples the CTE across its antenna array (IQ samples) to compute angle of arrival (AoA) or angle of departure (AoD).

[Core 6.2, Vol 4, Part E, §7.8.79–7.8.84; Vol 6, Part B, §4.4.5]

### 9a. Connectionless CTE (Periodic Advertising, Transmitter Side)

Requires a running extended + periodic advertising set (see Section 7 setup, steps 1–5).

1. `HCI_LE_Set_Connectionless_CTE_Transmit_Parameters` (0x2051)
   — Advertising_Handle, CTE_Length (2–20, units of 8 µs), CTE_Type (0x00=AoA, 0x01=AoD 1µs, 0x02=AoD 2µs), CTE_Count (CTEs per periodic advertising interval), Switching_Pattern_Length, Antenna_IDs[]
   → `HCI_Command_Complete`: Status=0x00

2. `HCI_LE_Set_Connectionless_CTE_Transmit_Enable` (0x2052)
   — Advertising_Handle, CTE_Enable=0x01
   → `HCI_Command_Complete`: Status=0x00
   > Controller appends a CTE to `Num_CTE_Per_Interval` PDUs per periodic advertising event.

### 9b. Connectionless CTE (Periodic Advertising, Receiver Side)

Scanner must first synchronize to the periodic advertising train (see Section 7b, steps 1–4).

1. `HCI_LE_Set_Connectionless_IQ_Sampling_Enable` (0x2053)
   — Sync_Handle, Sampling_Enable=0x01, Slot_Durations (0x01=1µs, 0x02=2µs), Max_Sampled_CTEs, Switching_Pattern_Length, Antenna_IDs[]
   → `HCI_Command_Complete`: Status=0x00, Sync_Handle

2. ← `LE_Connectionless_IQ_Report` (Event 0xFF, Subevent 0x15) — arrives for each received CTE
   — Sync_Handle, Channel_Index, RSSI, RSSI_Antenna_ID, CTE_Type, Slot_Durations, Packet_Status, Periodic_Event_Counter, Sample_Count, I_Sample[], Q_Sample[]
   > Feed the IQ samples into an AoA/AoD algorithm (e.g., MUSIC, ESPRIT, or a vendor library). The Host is responsible for angle computation — the Controller only provides raw IQ samples.

3. *(Cleanup)* `HCI_LE_Set_Connectionless_IQ_Sampling_Enable` (0x2053) — Sampling_Enable=0x00 to stop.

### 9c. Connection-based CTE (Both Sides)

Requires an established LE ACL connection. Either the Initiator or the Reflector can be the CTE transmitter.

**Reflector (CTE Transmitter) side:**

1. `HCI_LE_Set_Connection_CTE_Transmit_Parameters` (0x2055)
   — Connection_Handle, CTE_Types bitmask (0x01=AoA, 0x02=AoD 1µs, 0x04=AoD 2µs), Switching_Pattern_Length, Antenna_IDs[]
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

2. `HCI_LE_Connection_CTE_Response_Enable` (0x2057)
   — Connection_Handle, Enable=0x01
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

**Initiator (IQ Sampler) side:**

3. `HCI_LE_Set_Connection_CTE_Receive_Parameters` (0x2054)
   — Connection_Handle, Sampling_Enable=0x01, Slot_Durations, Switching_Pattern_Length, Antenna_IDs[]
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

4. `HCI_LE_Connection_CTE_Request_Enable` (0x2056)
   — Connection_Handle, Enable=0x01, CTE_Request_Interval (connection events between CTE requests), Requested_CTE_Length, Requested_CTE_Type
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle
   > Controller automatically sends `LL_CTE_REQ` PDUs at the specified interval and collects IQ samples.

5. ← `LE_Connection_IQ_Report` (Event 0xFF, Subevent 0x16) — one event per received CTE
   — Connection_Handle, RX_PHY, Data_Channel_Index, RSSI, RSSI_Antenna_ID, CTE_Type, Slot_Durations, Packet_Status, Connection_Event_Counter, Sample_Count, I_Sample[], Q_Sample[]

6. *(Cleanup)* `HCI_LE_Connection_CTE_Request_Enable` (0x2056) — Enable=0x00

> **Antenna switching note**: The Antenna_IDs array programs the GPIO switching pattern used during the CTE. Both transmitter and receiver must use the same slot duration. For AoA, only the receiver switches antennas; for AoD, only the transmitter switches.

---

## 10. Channel Sounding (CS, 6.0+)

Channel Sounding enables centimeter-level ranging. A CS procedure involves two devices — **Initiator** and **Reflector** — exchanging CS steps over an encrypted LE connection.

[Core 6.2, Vol 4, Part E, §7.8.116–7.8.130; Vol 6, Part H]

> **Prerequisite**: The connection must be encrypted before CS can be enabled. [Core 6.2, Vol 6, Part H, §4.2]

### 10a. Capability and Security Setup (One-time per connection)

1. `HCI_LE_CS_Read_Remote_Supported_Capabilities` (0x208A) — Initiator queries peer CS capabilities.
   → `HCI_Command_Status`: Status=0x00
   ← `LE_CS_Read_Remote_Supported_Capabilities_Complete` — Num_Config_Supported, Max_Consecutive_Procedures_Supported, Num_Antennas_Supported, Max_Antenna_Paths_Supported, Roles_Supported, Optional_Modes_Supported, RTT_Capability, RTT_AA_Only_N, RTT_Sounding_N, RTT_Random_Payload_N, NADM_Sounding_Capability, NADM_Random_Capability, CS_SYNC_PHY_Supported, Subfeatures_Supported, T_IP1/IP2/FCS/PM_Times_Supported

2. `HCI_LE_CS_Security_Enable` (0x2089) — triggers the CS Security Start procedure (LL_CS_SEC_REQ / LL_CS_SEC_RSP).
   → `HCI_Command_Status`: Status=0x00
   ← `LE_CS_Security_Enable_Complete` on **both sides** — Status=0x00
   > This must complete before any CS config or procedure can be run. The spec requires this cryptographic handshake to prevent relay attacks.

### 10b. Configuration (Per ranging session type)

3. `HCI_LE_CS_Set_Default_Settings` (0x208C) — Set role (0x01=Initiator, 0x02=Reflector, 0x03=Both), CS_SYNC_Antenna_Selection, Max_TX_Power
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

4. `HCI_LE_CS_Create_Config` (0x208F)
   — Connection_Handle, Config_ID (0x00–0x03), Create_Context (0x00=local only, 0x01=both peers), Main_Mode (1=RTT, 2=PBR, 3=PBR+RTT), Sub_Mode, Min_Main_Mode_Steps, Max_Main_Mode_Steps, Main_Mode_Repetition, Mode_0_Steps, Role (0x01=Initiator/0x02=Reflector), RTT_Type, CS_SYNC_PHY, Channel_Map (10 bytes, 72-channel bitmask), Channel_Map_Repetition, Channel_Selection_Type, Ch3c_Shape, Ch3c_Jump, Companion_Signal_Enable
   → `HCI_Command_Status`: Status=0x00
   ← `LE_CS_Config_Complete` on **both sides** — Config_ID, Action=0x01 (config created), Main_Mode, Sub_Mode, T_IP1/IP2/FCS/PM, Max_Procedure_Len, Min/Max_Subevent_Len

### 10c. Procedure Execution

5. `HCI_LE_CS_Set_Procedure_Parameters` (0x2092)
   — Connection_Handle, Config_ID, Max_Procedure_Len, Min_Procedure_Interval, Max_Procedure_Interval, Max_Procedure_Count (0=indefinite), Min/Max_Subevent_Len, Tone_Antenna_Config_Selection, PHY, TX_Power_Delta, Preferred_Peer_Antenna, SNR_Control_Initiator/Reflector
   → `HCI_Command_Complete`: Status=0x00, Connection_Handle

6. `HCI_LE_CS_Procedure_Enable` (0x2093) — Enable=0x01, Config_ID, Connection_Handle
   → `HCI_Command_Status`: Status=0x00
   ← `LE_CS_Procedure_Enable_Complete` on **both sides** — Status=0x00, Config_ID, State=0x01 (enabled), Tone_Antenna_Config_Selection, Selected_TX_Power, Subevent_Len, Subevents_Per_Event, Subevent_Interval, Event_Interval, Procedure_Interval, Procedure_Count, Max_Procedure_Len

7. ← `LE_CS_Subevent_Result` (repeating) — one event per CS subevent
   — Connection_Handle, Config_ID, Start_ACL_Conn_Event, Procedure_Counter, Frequency_Compensation, Reference_Power_Level, Procedure_Done_Status, Subevent_Done_Status, Abort_Reason, Num_Antenna_Paths, Num_Steps_Reported, Step_Mode[], Step_Channel[], Step_Data_Length[], Step_Data[][]
   > Step_Data contains raw RTT timestamps (Mode 1) or phase/amplitude IQ samples (Mode 2/3). The Host is responsible for converting these into distance estimates.

8. ← `LE_CS_Subevent_Result_Continue` — if result data exceeds event payload; carries continuation fragments.

9. *(Stop)* `HCI_LE_CS_Procedure_Enable` (0x2093) — Enable=0x00 to stop ongoing procedures.

> **Distance calculation**: RTT (Mode 1) gives time-of-flight → distance. PBR (Mode 2) gives phase differences across frequencies → distance via IFFT. Mode 3 combines both. Vendor SDKs or host-side algorithms process `Step_Data`. See [Channel Sounding](../concepts/channel-sounding.md) for method details.

---

## Tips and Common Pitfalls

- **Read Supported_Commands first**: Always check `HCI_Read_Local_Supported_Commands` (0x1002) before calling any command introduced after 4.0. Calling an unsupported command returns `Unknown HCI Command (0x01)`.

- **Wait for Command_Complete / Command_Status before proceeding**: Commands that return `HCI_Command_Status` (async) — such as `HCI_LE_Create_Connection`, `HCI_LE_Enable_Encryption`, `HCI_LE_Create_CIS` — continue pending until a completion event arrives. Do not issue the next command that depends on the result until the event is received.

- **No ATT before LE_Connection_Complete**: Do not send any ATT/GATT PDUs until `LE_Connection_Complete` (or `LE_Enhanced_Connection_Complete`) with Status=0x00 has been received.

- **No encryption before LE_Connection_Complete**: `HCI_LE_Enable_Encryption` must be issued only after the connection is fully established. Sending it during the connection setup phase returns `Command Disallowed (0x0C)`.

- **GATT handle caching**: After the first service discovery, store all attribute handles. On reconnection, compare the GATT Database Hash (characteristic 0x2B2A under the Generic Attribute service) against the stored hash. If unchanged, reuse cached handles. If a Service Changed indication (characteristic 0x2A05) is received, clear all cached handles and rediscover.

- **Extended vs. legacy advertising**: Legacy advertising commands (`HCI_LE_Set_Advertising_Parameters`, `HCI_LE_Set_Advertising_Enable`) and extended advertising commands (`HCI_LE_Set_Extended_Advertising_*`) cannot be mixed on the same controller. On 5.0+ stacks, prefer extended advertising for all new implementations.

- **PAwR / ESL advertising setup**: `HCI_LE_Set_Extended_Advertising_Parameters` must set `Advertising_Event_Properties=0x0000` (non-connectable, non-scannable, non-legacy) before calling `HCI_LE_Set_Periodic_Advertising_Parameters` for PAwR. Attempting periodic advertising on a connectable or legacy extended advertising set returns an error.

- **ISO flow control**: After `HCI_LE_Setup_ISO_Data_Path`, use `HCI_Number_Of_Completed_Packets` events to track available TX slots. Each ISO SDU sent consumes a slot; the controller reports completions asynchronously. Never exceed `Total_Num_ISO_Data_Packets` from `HCI_LE_Read_Buffer_Size [v2]`.

- **LESC DHKey timing**: `HCI_LE_Generate_DHKey` can take tens to hundreds of milliseconds on constrained hardware. The SMP timer (30 s) provides ample margin, but avoid calling it multiple times concurrently — it is serialized per controller.

---

## See Also

- [HCI Command Reference](hci-commands.md) — Full command list with opcodes and all parameters
- [BLE Architecture](../concepts/ble-architecture.md) — Protocol stack layers (PHY, LL, HCI, L2CAP, ATT, GATT, SM, GAP)
- [Security](../concepts/security.md) — Pairing modes, key hierarchy, bonding, Filter Accept List, Resolving List
- [LE Audio](../concepts/le-audio.md) — CIS and BIS ISO setup sequences with codec configuration
- [Direction Finding](../concepts/direction-finding.md) — AoA/AoD algorithm background, antenna array design
- [Channel Sounding](../concepts/channel-sounding.md) — PBR/RTT ranging methods, Step_Data interpretation, relay attack resilience
- [L2CAP](../concepts/l2cap.md) — CoC channel setup flows underlying EATT and application protocols

---

*Source: [Core 6.2, Vol 4, Part E, §7](../../sources/specs/6.2/Core_v6.2.md) — HCI command and event specifications; [Core 6.2, Vol 3, Part F (ATT) and Part G (GATT)](../../sources/specs/6.2/Core_v6.2.md) — attribute protocol PDU sequences; [Core 6.2, Vol 3, Part H (SMP)](../../sources/specs/6.2/Core_v6.2.md) — LE Secure Connections pairing flow; [Core 6.2, Vol 3, Part A (L2CAP)](../../sources/specs/6.2/Core_v6.2.md) — L2CAP signaling; [Core 6.2, Vol 6, Part B, §4.4.5 (Direction Finding)](../../sources/specs/6.2/Core_v6.2.md); [Core 6.2, Vol 6, Part H (Channel Sounding)](../../sources/specs/6.2/Core_v6.2.md)*
