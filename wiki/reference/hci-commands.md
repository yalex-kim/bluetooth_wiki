# HCI Command Reference

**Last updated**: 2026-05-04
**Covers**: Core Spec 5.0 – 6.2 (LE focus; BR/EDR included where relevant)

> Quick lookup for HCI commands. Commands are organized by functional area.
> Opcode format: OGF (bits 15:10) | OCF (bits 9:0). OGF values: Link Control=0x01, Link Policy=0x02, Controller & Baseband=0x03, Informational=0x04, Status=0x05, Testing=0x06, LE=0x08.
> Combined 16-bit opcode = (OGF << 10) | OCF.
> All commands return a Command_Complete or Command_Status event unless noted.

---

## Controller Initialization

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_Reset | 0x0C03 | — | Status | 1.0 |
| HCI_Read_Local_Version_Information | 0x1001 | — | HCI_Version, HCI_Subversion, LMP_Version, Manufacturer_Name, LMP_Subversion | 1.0 |
| HCI_Read_Local_Supported_Commands | 0x1002 | — | Supported_Commands (64-byte bitmask) | 1.2 |
| HCI_Read_Local_Supported_Features | 0x1003 | — | LMP_Features (8 bytes) | 1.0 |
| HCI_Read_BD_ADDR | 0x1009 | — | BD_ADDR | 1.0 |
| HCI_Read_Buffer_Size | 0x1005 | — | ACL_Data_Packet_Length, Synchronous_Data_Packet_Length, Total_Num_ACL_Data_Packets, Total_Num_Synchronous_Data_Packets | 1.0 |
| HCI_Set_Event_Mask | 0x0C01 | Event_Mask (8 bytes bitmask) | Status | 1.0 |
| HCI_Set_Event_Mask_Page_2 | 0x0C63 | Event_Mask_Page_2 (8 bytes bitmask) | Status | 3.0+HS |
| HCI_LE_Set_Event_Mask | 0x2001 | LE_Event_Mask (8 bytes bitmask); bit 0=LE Connection Complete, bit 1=LE Advertising Report, etc. | Status | 4.0 |
| HCI_LE_Read_Buffer_Size [v1] | 0x2002 | — | LE_ACL_Data_Packet_Length, Total_Num_LE_ACL_Data_Packets | 4.0 |
| HCI_LE_Read_Buffer_Size [v2] | 0x2060 | — | Adds ISO_Data_Packet_Length, Total_Num_ISO_Data_Packets | 5.2 |
| HCI_LE_Read_Local_Supported_Features_Page_0 | 0x2003 | — | LE_Features (8 bytes) | 4.0 |
| HCI_LE_Read_All_Local_Supported_Features | 0x2087 | — | Max_Page, LE_Features (248 bytes) | **6.0+** |
| HCI_LE_Read_Supported_States | 0x201C | — | LE_States (8-byte bitmask of state/role combos) | 4.0 |

> Note: `HCI_LE_Read_Buffer_Size [v2]` is mandatory on 5.2+ controllers that support ISO. If LE buffer size returns 0, fall back to `HCI_Read_Buffer_Size` (shared BR/EDR buffer). [Core 6.2, Vol 4, Part E, §7.8.2]

---

## LE Advertising (Legacy)

Legacy advertising uses PDU types ADV_IND, ADV_DIRECT_IND, ADV_SCAN_IND, ADV_NONCONN_IND. Max 31 bytes of data. OGF=0x08.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Advertising_Parameters | 0x2006 | Advertising_Interval_Min/Max (0x0020–0x4000, ×0.625 ms), Advertising_Type (0x00–0x04), Own_Address_Type, Peer_Address_Type, Peer_Address, Advertising_Channel_Map (bits 0–2 = ch37/38/39), Advertising_Filter_Policy | Status | 4.0 |
| HCI_LE_Read_Advertising_Physical_Channel_Tx_Power | 0x2007 | — | TX_Power_Level (dBm, –127 to +20) | 4.0 |
| HCI_LE_Set_Advertising_Data | 0x2008 | Advertising_Data_Length (0–31), Advertising_Data (31 bytes) | Status | 4.0 |
| HCI_LE_Set_Scan_Response_Data | 0x2009 | Scan_Response_Data_Length (0–31), Scan_Response_Data (31 bytes) | Status | 4.0 |
| HCI_LE_Set_Advertising_Enable | 0x200A | Advertising_Enable (0x00/0x01) | Status; may also generate LE_Connection_Complete on connection | 4.0 |

> Deprecated in favour of extended advertising commands on 5.0+ stacks. These commands do not work when extended advertising is in use.

---

## LE Extended Advertising (5.0+)

Extended advertising supports multiple advertising sets, >31 bytes of data, secondary channels, coded PHY, and anonymous/non-connectable non-scannable extended PDUs. OGF=0x08.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Advertising_Set_Random_Address | 0x2035 | Advertising_Handle (0x00–0xEF), Random_Address | Status | 5.0 |
| HCI_LE_Set_Extended_Advertising_Parameters [v1] | 0x2036 | Advertising_Handle, Advertising_Event_Properties (2-byte bitmask), Primary_Advertising_Interval_Min/Max (3 bytes, ×0.625 ms), Primary_Advertising_Channel_Map, Own/Peer Address Type, Advertising_Filter_Policy, Advertising_TX_Power, Primary/Secondary_Advertising_PHY, Secondary_Advertising_Max_Skip, Advertising_SID, Scan_Request_Notification_Enable | Status, Selected_TX_Power | 5.0 |
| HCI_LE_Set_Extended_Advertising_Parameters [v2] | 0x207F | Adds Primary_Advertising_PHY_Options, Secondary_Advertising_PHY_Options | Status, Selected_TX_Power | 5.4 |
| HCI_LE_Set_Extended_Advertising_Data | 0x2037 | Advertising_Handle, Operation (0x00–0x04), Fragment_Preference, Advertising_Data_Length, Advertising_Data | Status | 5.0 |
| HCI_LE_Set_Extended_Scan_Response_Data | 0x2038 | Advertising_Handle, Operation, Fragment_Preference, Scan_Response_Data_Length, Scan_Response_Data | Status | 5.0 |
| HCI_LE_Set_Extended_Advertising_Enable | 0x2039 | Enable, Num_Sets, Advertising_Handle[i], Duration[i], Max_Extended_Advertising_Events[i] | Status; LE_Advertising_Set_Terminated event on timeout/connection | 5.0 |
| HCI_LE_Read_Maximum_Advertising_Data_Length | 0x203A | — | Max_Advertising_Data_Length | 5.0 |
| HCI_LE_Read_Number_of_Supported_Advertising_Sets | 0x203B | — | Num_Supported_Advertising_Sets | 5.0 |
| HCI_LE_Remove_Advertising_Set | 0x203C | Advertising_Handle | Status | 5.0 |
| HCI_LE_Clear_Advertising_Sets | 0x203D | — | Status | 5.0 |

> `Advertising_Event_Properties` bits: 0=connectable, 1=scannable, 2=directed, 3=high-duty-cycle, 4=legacy PDU, 5=anonymous, 6=include TxPower. Extended non-connectable non-scannable (0x0000) is the most common for beacons.

---

## LE Periodic Advertising (5.0+)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Periodic_Advertising_Parameters [v1] | 0x203E | Advertising_Handle, Periodic_Advertising_Interval_Min/Max (0x0006–0xFFFF, ×1.25 ms), Periodic_Advertising_Properties | Status | 5.0 |
| HCI_LE_Set_Periodic_Advertising_Parameters [v2] | 0x2086 | Adds Num_Subevents, Subevent_Interval, Response_Slot_Delay, Response_Slot_Spacing, Num_Response_Slots (PAwR) | Status | 5.4 |
| HCI_LE_Set_Periodic_Advertising_Data | 0x203F | Advertising_Handle, Operation, Advertising_Data_Length, Advertising_Data | Status | 5.0 |
| HCI_LE_Set_Periodic_Advertising_Enable | 0x2040 | Enable (bits: 0=enable, 1=include ADI), Advertising_Handle | Status | 5.0 |
| HCI_LE_Periodic_Advertising_Create_Sync | 0x2044 | Options, Advertising_SID, Advertiser_Address_Type, Advertiser_Address, Skip, Sync_Timeout, Sync_CTE_Type | none; LE_Periodic_Advertising_Sync_Established event | 5.0 |
| HCI_LE_Periodic_Advertising_Create_Sync_Cancel | 0x2045 | — | Status | 5.0 |
| HCI_LE_Periodic_Advertising_Terminate_Sync | 0x2046 | Sync_Handle | Status | 5.0 |
| HCI_LE_Add_Device_To_Periodic_Advertiser_List | 0x2047 | Advertiser_Address_Type, Advertiser_Address, Advertising_SID | Status | 5.0 |
| HCI_LE_Remove_Device_From_Periodic_Advertiser_List | 0x2048 | Advertiser_Address_Type, Advertiser_Address, Advertising_SID | Status | 5.0 |
| HCI_LE_Clear_Periodic_Advertiser_List | 0x2049 | — | Status | 5.0 |
| HCI_LE_Read_Periodic_Advertiser_List_Size | 0x204A | — | Periodic_Advertiser_List_Size | 5.0 |
| HCI_LE_Set_Periodic_Advertising_Receive_Enable | 0x2059 | Sync_Handle, Enable | Status | 5.1 |
| HCI_LE_Periodic_Advertising_Sync_Transfer | 0x205A | Connection_Handle, Service_Data, Sync_Handle | Status, Connection_Handle | 5.1 |
| HCI_LE_Periodic_Advertising_Set_Info_Transfer | 0x205B | Connection_Handle, Service_Data, Advertising_Handle | Status, Connection_Handle | 5.1 |
| HCI_LE_Set_Periodic_Advertising_Sync_Transfer_Parameters | 0x205C | Connection_Handle, Mode, Skip, Sync_Timeout, CTE_Type | Status, Connection_Handle | 5.1 |
| HCI_LE_Set_Default_Periodic_Advertising_Sync_Transfer_Parameters | 0x205D | Mode, Skip, Sync_Timeout, CTE_Type | Status | 5.1 |
| HCI_LE_Set_Periodic_Advertising_Subevent_Data | 0x2082 | Advertising_Handle, Num_Subevents, Subevent[i], Response_Slot_Start[i], Response_Slot_Count[i], Subevent_Data_Length[i], Subevent_Data[i] | Status | 5.4 |
| HCI_LE_Set_Periodic_Advertising_Response_Data | 0x2083 | Sync_Handle, Request_Event, Request_Subevent, Response_Subevent, Response_Slot, Response_Data_Length, Response_Data | Status | 5.4 |
| HCI_LE_Set_Periodic_Sync_Subevent | 0x2084 | Sync_Handle, Periodic_Advertising_Properties, Num_Subevents, Subevent[i] | Status, Sync_Handle | 5.4 |

---

## LE Scanning

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Scan_Parameters | 0x200B | LE_Scan_Type (0=passive, 1=active), LE_Scan_Interval (0x0004–0x4000, ×0.625 ms), LE_Scan_Window (≤ Interval), Own_Address_Type, Scanning_Filter_Policy | Status | 4.0 |
| HCI_LE_Set_Scan_Enable | 0x200C | LE_Scan_Enable (0/1), Filter_Duplicates | Status; LE_Advertising_Report event | 4.0 |
| HCI_LE_Set_Extended_Scan_Parameters | 0x2041 | Own_Address_Type, Scanning_Filter_Policy, Scanning_PHYs (bitmask), Scan_Type[i], Scan_Interval[i], Scan_Window[i] | Status | 5.0 |
| HCI_LE_Set_Extended_Scan_Enable | 0x2042 | Enable, Filter_Duplicates, Duration (×10 ms), Period (×1.28 s) | Status; LE_Extended_Advertising_Report and LE_Scan_Timeout events | 5.0 |

> Legacy scan (`HCI_LE_Set_Scan_Enable`) does not report extended advertising PDUs. Use extended scan on 5.0+ stacks. [Core 6.2, Vol 4, Part E, §7.8.11]

---

## LE Connection Management

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Create_Connection | 0x200D | LE_Scan_Interval/Window, Initiator_Filter_Policy, Peer_Address_Type, Peer_Address, Own_Address_Type, Conn_Interval_Min/Max (0x0006–0x0C80, ×1.25 ms), Max_Latency (0–0x01F3), Supervision_Timeout (0x000A–0x0C80, ×10 ms), Min/Max_CE_Length | Command_Status; LE_Connection_Complete or LE_Enhanced_Connection_Complete | 4.0 |
| HCI_LE_Create_Connection_Cancel | 0x200E | — | Status; LE_Connection_Complete with error 0x02 | 4.0 |
| HCI_LE_Extended_Create_Connection [v1] | 0x2043 | Initiator_Filter_Policy, Own_Address_Type, Peer_Address_Type, Peer_Address, Initiating_PHYs (bitmask), per-PHY: Scan_Interval/Window, Conn_Interval_Min/Max, Max_Latency, Supervision_Timeout, Min/Max_CE_Length | Command_Status; LE_Enhanced_Connection_Complete v2 event | 5.0 |
| HCI_LE_Extended_Create_Connection [v2] | 0x2085 | Adds Connection_Rate_Min/Max params | Command_Status; LE_Enhanced_Connection_Complete | 6.2 |
| HCI_Disconnect | 0x0406 | Connection_Handle, Reason (0x05/0x13–0x15/0x1A/0x29/0x3B) | Command_Status; HCI_Disconnection_Complete | 1.0 |
| HCI_LE_Connection_Update | 0x2013 | Connection_Handle, Conn_Interval_Min/Max, Max_Latency, Supervision_Timeout, Min/Max_CE_Length | Command_Status; LE_Connection_Update_Complete | 4.0 |
| HCI_LE_Remote_Connection_Parameter_Request_Reply | 0x2020 | Connection_Handle, Interval_Min/Max, Latency, Timeout, Min/Max_CE_Length | Status, Connection_Handle | 4.1 |
| HCI_LE_Remote_Connection_Parameter_Request_Negative_Reply | 0x2021 | Connection_Handle, Reason | Status, Connection_Handle | 4.1 |
| HCI_LE_Read_Remote_Features_Page_0 | 0x2016 | Connection_Handle | Command_Status; LE_Read_Remote_Features_Complete | 4.0 |
| HCI_LE_Read_All_Remote_Features | 0x2088 | Connection_Handle, Pages_Requested | Command_Status; LE_Read_All_Remote_Features_Complete | **6.0+** |
| HCI_LE_Set_Default_Subrate | 0x207D | Subrate_Min/Max (1–500), Max_Latency, Continuation_Number, Supervision_Timeout | Status | 5.3 |
| HCI_LE_Subrate_Request | 0x207E | Connection_Handle, Subrate_Min/Max, Max_Latency, Continuation_Number, Supervision_Timeout | Command_Status; LE_Subrate_Change event | 5.3 |
| HCI_LE_Connection_Rate_Request | 0x20A1 | Connection_Handle, Conn_Interval_Min/Max (×125 µs, range 0x0003–0x7D00), Subrate_Min/Max, Max_Latency, Continuation_Number, Supervision_Timeout, Min/Max_CE_Length | Command_Status; LE_Connection_Rate_Change event | 6.2 |
| HCI_LE_Set_Default_Rate_Parameters | 0x20A2 | Conn_Interval_Min/Max, Subrate_Min/Max, Max_Latency, Continuation_Number, Supervision_Timeout, Min/Max_CE_Length | Status | 6.2 |
| HCI_LE_Read_Minimum_Supported_Connection_Interval | 0x20A3 | — | Minimum_Supported_Connection_Interval (×125 µs), Num_Groups, Group_Min/Max/Stride[i] | 6.2 |
| HCI_LE_Frame_Space_Update | 0x209D | Connection_Handle, Frame_Space_Min/Max (µs), PHYS (bitmask), Spacing_Types (bitmask) | Command_Status; LE_Frame_Space_Update_Complete | 6.2 |

> `HCI_LE_Connection_Rate_Request` uses 125 µs ticks (vs 1.25 ms for classic LE connection update), enabling the shorter 375 µs intervals introduced in Core 6.2. [Core 6.2, Vol 4, Part E, §7.8.154]

---

## LE Filter Accept List (Whitelist)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Read_Filter_Accept_List_Size | 0x200F | — | Filter_Accept_List_Size | 4.0 |
| HCI_LE_Clear_Filter_Accept_List | 0x2010 | — | Status | 4.0 |
| HCI_LE_Add_Device_To_Filter_Accept_List | 0x2011 | Address_Type, Address | Status | 4.0 |
| HCI_LE_Remove_Device_From_Filter_Accept_List | 0x2012 | Address_Type, Address | Status | 4.0 |

---

## LE PHY Management (5.0+)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Read_PHY | 0x2030 | Connection_Handle | TX_PHY (1=1M, 2=2M, 3=Coded), RX_PHY | 5.0 |
| HCI_LE_Set_Default_PHY | 0x2031 | All_PHYs (bit 0=no TX pref, bit 1=no RX pref), TX_PHYs (bitmask), RX_PHYs (bitmask) | Status | 5.0 |
| HCI_LE_Set_PHY | 0x2032 | Connection_Handle, All_PHYs, TX_PHYs, RX_PHYs, PHY_Options (bits 0–1: 0=no pref, 1=S2, 2=S8 for Coded) | Command_Status; LE_PHY_Update_Complete | 5.0 |

> PHY bitmask: bit 0=LE 1M, bit 1=LE 2M, bit 2=LE Coded (S=2 or S=8). Coded PHY requires `LE_Coded_PHY` feature bit.

---

## LE Data Length Extension (4.2+)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Data_Length | 0x2022 | Connection_Handle, TX_Octets (27–251), TX_Time (328–17040 µs) | Status, Connection_Handle; LE_Data_Length_Change event | 4.2 |
| HCI_LE_Read_Suggested_Default_Data_Length | 0x2023 | — | Suggested_Max_TX_Octets, Suggested_Max_TX_Time | 4.2 |
| HCI_LE_Write_Suggested_Default_Data_Length | 0x2024 | Suggested_Max_TX_Octets, Suggested_Max_TX_Time | Status | 4.2 |
| HCI_LE_Read_Maximum_Data_Length | 0x202F | — | Supported_Max_TX/RX_Octets, Supported_Max_TX/RX_Time | 4.2 |

---

## LE Security & Privacy

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Encrypt | 0x2017 | Key (16 bytes), Plaintext_Data (16 bytes) | Encrypted_Data (16 bytes) — synchronous AES-128 | 4.0 |
| HCI_LE_Rand | 0x2018 | — | Random_Number (8 bytes) | 4.0 |
| HCI_LE_Enable_Encryption | 0x2019 | Connection_Handle, Random_Number (8 bytes), Encrypted_Diversifier (2 bytes), Long_Term_Key (16 bytes) | Command_Status; HCI_Encryption_Change; Central role only | 4.0 |
| HCI_LE_Long_Term_Key_Request_Reply | 0x201A | Connection_Handle, Long_Term_Key (16 bytes) | Status, Connection_Handle; Peripheral role only | 4.0 |
| HCI_LE_Long_Term_Key_Request_Negative_Reply | 0x201B | Connection_Handle | Status, Connection_Handle; Peripheral role only | 4.0 |
| HCI_LE_Read_Local_P-256_Public_Key | 0x2025 | — | Command_Status; LE_Read_Local_P256_Public_Key_Complete | 4.2 |
| HCI_LE_Generate_DHKey [v1] | 0x2026 | Remote_P256_Public_Key (64 bytes) | Command_Status; LE_Generate_DHKey_Complete | 4.2 |
| HCI_LE_Generate_DHKey [v2] | 0x205E | Remote_P256_Public_Key, Key_Type | Command_Status; LE_Generate_DHKey_Complete | 5.1 |
| HCI_LE_Add_Device_To_Resolving_List | 0x2027 | Peer_Identity_Address_Type, Peer_Identity_Address, Peer_IRK (16 bytes), Local_IRK (16 bytes) | Status | 4.2 |
| HCI_LE_Remove_Device_From_Resolving_List | 0x2028 | Peer_Identity_Address_Type, Peer_Identity_Address | Status | 4.2 |
| HCI_LE_Clear_Resolving_List | 0x2029 | — | Status | 4.2 |
| HCI_LE_Read_Resolving_List_Size | 0x202A | — | Resolving_List_Size | 4.2 |
| HCI_LE_Read_Peer_Resolvable_Address | 0x202B | Peer_Identity_Address_Type, Peer_Identity_Address | Peer_Resolvable_Address | 4.2 |
| HCI_LE_Read_Local_Resolvable_Address | 0x202C | Peer_Identity_Address_Type, Peer_Identity_Address | Local_Resolvable_Address | 4.2 |
| HCI_LE_Set_Address_Resolution_Enable | 0x202D | Address_Resolution_Enable (0/1) | Status | 4.2 |
| HCI_LE_Set_Resolvable_Private_Address_Timeout [v1] | 0x202E | RPA_Timeout (1–3600 s, default 900 s) | Status | 4.2 |
| HCI_LE_Set_Resolvable_Private_Address_Timeout [v2] | 0x209E | RPA_Timeout_Min (1–3600 s), RPA_Timeout_Max (1–3600 s); Controller picks random interval in range | Status | 6.1 |
| HCI_LE_Set_Privacy_Mode | 0x204E | Peer_Identity_Address_Type, Peer_Identity_Address, Privacy_Mode (0=Network, 1=Device) | Status | 4.2 |
| HCI_LE_Set_Host_Feature | 0x2074 | Bit_Number, Bit_Value (0/1); controls host-supported LE features | Status | 5.2 |
| HCI_LE_Set_Data_Related_Address_Changes | 0x207C | Advertising_Handle, Change_Reasons (bitmask) | Status | 5.2 |

> `HCI_LE_Set_Resolvable_Private_Address_Timeout [v2]` is the 6.1 privacy enhancement: uses a randomized RPA rotation interval rather than a fixed timeout, hardening against timing-based tracking. [Core 6.2, Vol 4, Part E, §7.8.45]

---

## LE Channel Classification

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Host_Channel_Classification | 0x2014 | Channel_Map (5 bytes, 37 bits; 0=bad, 1=unknown) | Status | 4.0 |
| HCI_LE_Read_Channel_Map | 0x2015 | Connection_Handle | Channel_Map (5 bytes) | 4.0 |

---

## LE Audio / Isochronous Channels (5.2+)

### CIS (Connected Isochronous Stream)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_CIG_Parameters | 0x2062 | CIG_ID, SDU_Interval_C→P/P→C (µs), Worst_Case_SCA, Packing, Framing, Max_Transport_Latency_C→P/P→C (ms), CIS_Count, per-CIS: CIS_ID, Max_SDU_C→P/P→C, PHY_C→P/P→C, RTN_C→P/P→C | Status, CIG_ID, CIS_Count, Connection_Handle[i] | 5.2 |
| HCI_LE_Set_CIG_Parameters_Test | 0x2063 | Low-level CIG params for test purposes (NSE, BN, FT, ISO_Interval, etc.) | Status, CIG_ID, handles | 5.2 |
| HCI_LE_Create_CIS | 0x2064 | CIS_Count, CIS_Connection_Handle[i], ACL_Connection_Handle[i] | Command_Status; LE_CIS_Established event per CIS | 5.2 |
| HCI_LE_Remove_CIG | 0x2065 | CIG_ID | Status, CIG_ID | 5.2 |
| HCI_LE_Accept_CIS_Request | 0x2066 | Connection_Handle (CIS) | Command_Status; LE_CIS_Established; Peripheral only | 5.2 |
| HCI_LE_Reject_CIS_Request | 0x2067 | Connection_Handle, Reason | Status, Connection_Handle; Peripheral only | 5.2 |

### BIS (Broadcast Isochronous Stream)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Create_BIG | 0x2068 | BIG_Handle, Advertising_Handle, Num_BIS, SDU_Interval (µs), Max_SDU, Max_Transport_Latency (ms), RTN, PHY, Packing, Framing, Encryption, Broadcast_Code (16 bytes) | Command_Status; LE_Create_BIG_Complete | 5.2 |
| HCI_LE_Create_BIG_Test | 0x2069 | Low-level BIG test params (ISO_Interval, NSE, Max_PDU, BN, NTO, IRC, PTO, etc.) | Command_Status; LE_Create_BIG_Complete | 5.2 |
| HCI_LE_Terminate_BIG | 0x206A | BIG_Handle, Reason | Command_Status; LE_Terminate_BIG_Complete | 5.2 |
| HCI_LE_BIG_Create_Sync | 0x206B | BIG_Handle, Sync_Handle, Encryption, Broadcast_Code, MSE, BIG_Sync_Timeout, Num_BIS, BIS[i] | Command_Status; LE_BIG_Sync_Established | 5.2 |
| HCI_LE_BIG_Terminate_Sync | 0x206C | BIG_Handle | Status, BIG_Handle; LE_BIG_Sync_Lost | 5.2 |

### ISO Data Path

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Setup_ISO_Data_Path | 0x206E | Connection_Handle, Data_Path_Direction (0=input/TX, 1=output/RX), Data_Path_ID, Coding_Format, Company_ID, Vendor_Specific_Codec_ID, Controller_Delay (µs), Codec_Configuration_Length, Codec_Configuration | Status, Connection_Handle | 5.2 |
| HCI_LE_Remove_ISO_Data_Path | 0x206F | Connection_Handle, Data_Path_Direction_Flags (bit 0=input, bit 1=output) | Status, Connection_Handle | 5.2 |
| HCI_LE_Read_ISO_TX_Sync | 0x2061 | Connection_Handle (CIS/BIS) | Packet_Sequence_Number, TX_Time_Stamp, Time_Offset | 5.2 |
| HCI_LE_Read_ISO_Link_Quality | 0x2075 | Connection_Handle (CIS/BIS) | TX/RX_UnACKed_Packets, TX/RX_Flushed_Packets, TX/RX_Last_Subevent_Packets, Retransmitted_Packets, CRC_Error_Packets, RX_Unreceived_Packets, Duplicate_Packets | 5.2 |
| HCI_LE_Request_Peer_SCA | 0x206D | Connection_Handle | Command_Status; LE_Request_Peer_SCA_Complete | 5.2 |

### ISO Test Commands

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_ISO_Transmit_Test | 0x2070 | Connection_Handle, Payload_Type | Status, Connection_Handle | 5.2 |
| HCI_LE_ISO_Receive_Test | 0x2071 | Connection_Handle, Payload_Type | Status, Connection_Handle | 5.2 |
| HCI_LE_ISO_Read_Test_Counters | 0x2072 | Connection_Handle | Received_SDU_Count, Missed_SDU_Count, Failed_SDU_Count | 5.2 |
| HCI_LE_ISO_Test_End | 0x2073 | Connection_Handle | Status, Received_SDU_Count, Missed_SDU_Count, Failed_SDU_Count | 5.2 |

---

## LE Power Control (5.2+)

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Enhanced_Read_Transmit_Power_Level | 0x2076 | Connection_Handle, PHY (1=1M, 2=2M, 3=Coded S8, 4=Coded S2) | Current_TX_Power_Level, Max_TX_Power_Level | 5.2 |
| HCI_LE_Read_Remote_Transmit_Power_Level | 0x2077 | Connection_Handle, PHY | Command_Status; LE_Transmit_Power_Reporting event | 5.2 |
| HCI_LE_Set_Path_Loss_Reporting_Parameters | 0x2078 | Connection_Handle, High_Threshold (dB), High_Hysteresis (dB), Low_Threshold (dB), Low_Hysteresis (dB), Min_Time_Spent (connection events) | Status, Connection_Handle | 5.2 |
| HCI_LE_Set_Path_Loss_Reporting_Enable | 0x2079 | Connection_Handle, Enable (0/1) | Status, Connection_Handle; LE_Path_Loss_Threshold event | 5.2 |
| HCI_LE_Set_Transmit_Power_Reporting_Enable | 0x207A | Connection_Handle, Local_Enable, Remote_Enable | Status, Connection_Handle; LE_Transmit_Power_Reporting event | 5.2 |
| HCI_LE_Read_Transmit_Power | 0x204B | — | Min_TX_Power, Max_TX_Power (dBm) | 5.0 |
| HCI_LE_Read_RF_Path_Compensation | 0x204C | — | RF_TX_Path_Compensation_Value (dB×10), RF_RX_Path_Compensation_Value | 5.0 |
| HCI_LE_Write_RF_Path_Compensation | 0x204D | RF_TX_Path_Compensation_Value, RF_RX_Path_Compensation_Value | Status | 5.0 |

---

## Direction Finding / CTE (5.1+)

CTE = Constant Tone Extension; AoA = Angle of Arrival; AoD = Angle of Departure.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Set_Connectionless_CTE_Transmit_Parameters | 0x2051 | Advertising_Handle, CTE_Length (2–20, ×8 µs), CTE_Type (0=AoA, 1=AoD-1µs, 2=AoD-2µs), CTE_Count (1–16), Switching_Pattern_Length, Antenna_IDs[] | Status | 5.1 |
| HCI_LE_Set_Connectionless_CTE_Transmit_Enable | 0x2052 | Advertising_Handle, CTE_Enable | Status | 5.1 |
| HCI_LE_Set_Connectionless_IQ_Sampling_Enable | 0x2053 | Sync_Handle, Sampling_Enable, Slot_Durations (1=1µs, 2=2µs), Max_Sampled_CTEs, Switching_Pattern_Length, Antenna_IDs[] | Status, Sync_Handle; LE_Connectionless_IQ_Report events | 5.1 |
| HCI_LE_Set_Connection_CTE_Receive_Parameters | 0x2054 | Connection_Handle, Sampling_Enable, Slot_Durations, Switching_Pattern_Length, Antenna_IDs[] | Status, Connection_Handle | 5.1 |
| HCI_LE_Set_Connection_CTE_Transmit_Parameters | 0x2055 | Connection_Handle, CTE_Types (bitmask: bit 0=AoA, 1=AoD-1µs, 2=AoD-2µs), Switching_Pattern_Length, Antenna_IDs[] | Status, Connection_Handle | 5.1 |
| HCI_LE_Connection_CTE_Request_Enable | 0x2056 | Connection_Handle, Enable, CTE_Request_Interval, Requested_CTE_Length, Requested_CTE_Type | Status, Connection_Handle | 5.1 |
| HCI_LE_Connection_CTE_Response_Enable | 0x2057 | Connection_Handle, Enable | Status, Connection_Handle | 5.1 |
| HCI_LE_Read_Antenna_Information | 0x2058 | — | Supported_Switching_Sampling_Rates, Num_Antennae, Max_Switching_Pattern_Length, Max_CTE_Length | 5.1 |

---

## Channel Sounding (6.0+)

Channel Sounding (CS) provides sub-meter ranging using HADM (High Accuracy Distance Measurement). Uses RTT and/or PCT (Phase-based Carrier Tone) measurements.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_CS_Read_Local_Supported_Capabilities | 0x2089 | — | Num_Config_Supported, Max_Consecutive_Procedures, Num_Antennae, Max_Antenna_Paths, Roles_Supported, Modes_Supported, RTT_Capability, NADM capability fields, CS_SYNC_PHYs_Supported, T_IP1/IP2/FCS/PM/SW timing, TX_SNR_Capability | **6.0+** |
| HCI_LE_CS_Read_Remote_Supported_Capabilities | 0x208A | Connection_Handle | Command_Status; LE_CS_Read_Remote_Supported_Capabilities_Complete | **6.0+** |
| HCI_LE_CS_Write_Cached_Remote_Supported_Capabilities | 0x208B | Connection_Handle + capability fields (same as Read_Local) | Status, Connection_Handle | **6.0+** |
| HCI_LE_CS_Security_Enable | 0x208C | Connection_Handle | Command_Status; LE_CS_Security_Enable_Complete | **6.0+** |
| HCI_LE_CS_Set_Default_Settings | 0x208D | Connection_Handle, Role_Enable (bitmask: bit 0=Initiator, bit 1=Reflector), CS_SYNC_Antenna_Selection, Max_TX_Power | Status, Connection_Handle | **6.0+** |
| HCI_LE_CS_Read_Remote_FAE_Table | 0x208E | Connection_Handle | Command_Status; LE_CS_Read_Remote_FAE_Table_Complete | **6.0+** |
| HCI_LE_CS_Write_Cached_Remote_FAE_Table | 0x208F | Connection_Handle, Remote_FAE_Table (72 bytes) | Status, Connection_Handle | **6.0+** |
| HCI_LE_CS_Create_Config | 0x2090 | Connection_Handle, Config_ID (0–3), Create_Context (0x00=local only, 0x01=local+remote), Main_Mode_Type (1=RTT, 2=PBR, 3=RTT+PBR), Sub_Mode_Type, Min/Max_Main_Mode_Steps, Main_Mode_Repetition, Mode_0_Steps, Role (0=Initiator, 1=Reflector), RTT_Type, CS_SYNC_PHY, Channel_Map (10 bytes), Channel_Map_Repetition, Channel_Selection_Type, Ch3c_Shape, Ch3c_Jump, T_IP1/IP2/FCS/PM Times, T_SW Time | Command_Status; LE_CS_Config_Complete | **6.0+** |
| HCI_LE_CS_Remove_Config | 0x2091 | Connection_Handle, Config_ID | Command_Status; LE_CS_Config_Complete | **6.0+** |
| HCI_LE_CS_Set_Channel_Classification | 0x2092 | Channel_Classification (10 bytes) | Status | **6.0+** |
| HCI_LE_CS_Set_Procedure_Parameters | 0x2093 | Connection_Handle, Config_ID, Max_Procedure_Len, Min_Procedure_Interval, Max_Procedure_Interval, Max_Procedure_Count, Min/Max_Subevent_Len (µs), Tone_Antenna_Config_Selection, PHY, TX_Power_Delta, Preferred_Peer_Antenna, SNR_Control_Initiator/Reflector | Status, Connection_Handle | **6.0+** |
| HCI_LE_CS_Procedure_Enable | 0x2094 | Connection_Handle, Config_ID, Enable | Command_Status; LE_CS_Procedure_Enable_Complete | **6.0+** |
| HCI_LE_CS_Test | 0x2095 | Extensive test params (Main_Mode, Sub_Mode, PHY, channel, timing, antenna, power, access address, tone extensions) | Command_Status; LE_CS_Subevent_Result events | **6.0+** |
| HCI_LE_CS_Test_End | 0x2096 | — | Command_Status; LE_CS_Test_End_Complete | **6.0+** |

> CS security hardened in 6.2: `HCI_LE_CS_Security_Enable` now exchanges cryptographic credentials to prevent spoofing. [Core 6.2, Vol 4, Part E, §7.8.133]

---

## LE Monitored Advertisers (6.0+)

Monitors specific advertisers by address for RSSI threshold crossing and timeouts.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Add_Device_To_Monitored_Advertisers_List | 0x2098 | Address_Type, Address, RSSI_Low_Threshold (dBm), RSSI_High_Threshold (dBm), Timeout (s) | Status | **6.0+** |
| HCI_LE_Remove_Device_From_Monitored_Advertisers_List | 0x2099 | Address_Type, Address | Status | **6.0+** |
| HCI_LE_Clear_Monitored_Advertisers_List | 0x209A | — | Status | **6.0+** |
| HCI_LE_Read_Monitored_Advertisers_List_Size | 0x209B | — | Number | **6.0+** |
| HCI_LE_Enable_Monitoring_Advertisers | 0x209C | Enable | Status; LE_Monitored_Advertisers_Report events | **6.0+** |
| HCI_LE_Set_Decision_Data | 0x2080 | Advertising_Handle, Decision_Type_Flags, Decision_Data_Length, Decision_Data | Status | **6.0+** |
| HCI_LE_Set_Decision_Instructions | 0x2081 | Num_Tests, Test_Flags[i], Test_Field[i], Test_Parameters[i] | Status | **6.0+** |

---

## LE UTP (Unreliable Transport Protocol) (6.2+)

UTP provides a low-overhead OTA transport for Upper Tester access.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Enable_UTP_OTA_Mode | 0x209F | Enable (0/1) | Status | 6.2 |
| HCI_LE_UTP_Send | 0x20A0 | UTP_Data_Length, UTP_Data | Status | 6.2 |

---

## LE Test Commands

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_LE_Receiver_Test [v1] | 0x201D | RX_Channel (0–39) | Status | 4.0 |
| HCI_LE_Receiver_Test [v2] | 0x2033 | RX_Channel, PHY (1=1M, 2=2M, 3=Coded), Modulation_Index | Status | 5.0 |
| HCI_LE_Receiver_Test [v3] | 0x204F | Adds CTE_Length, CTE_Type, Slot_Durations, Switching_Pattern_Length, Antenna_IDs | Status | 5.1 |
| HCI_LE_Transmitter_Test [v1] | 0x201E | TX_Channel, Test_Data_Length, Packet_Payload (0–7) | Status | 4.0 |
| HCI_LE_Transmitter_Test [v2] | 0x2034 | TX_Channel, Test_Data_Length, Packet_Payload, PHY | Status | 5.0 |
| HCI_LE_Transmitter_Test [v3] | 0x2050 | Adds CTE_Length, CTE_Type, Switching_Pattern_Length, Antenna_IDs | Status | 5.1 |
| HCI_LE_Transmitter_Test [v4] | 0x207B | Adds TX_Power_Level, TX_Power_Level_Flag | Status | 5.2 |
| HCI_LE_Test_End | 0x201F | — | Status, Num_Packets | 4.0 |
| HCI_LE_Modify_Sleep_Clock_Accuracy | 0x205F | Action (0=decrease accuracy, 1=increase accuracy) | Status | 5.1 |

---

## BR/EDR Connection Management

OGF=0x01 for Link Control; OGF=0x02 for Link Policy; OGF=0x03 for Controller & Baseband.

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_Inquiry | 0x0401 | LAP (0x9E8B00–0x9E8B3F), Inquiry_Length (×1.28 s), Num_Responses | Command_Status; HCI_Inquiry_Result, HCI_Inquiry_Complete | 1.0 |
| HCI_Inquiry_Cancel | 0x0402 | — | Status | 1.0 |
| HCI_Create_Connection | 0x0405 | BD_ADDR, Packet_Type, Page_Scan_Repetition_Mode, Clock_Offset, Allow_Role_Switch | Command_Status; HCI_Connection_Complete | 1.0 |
| HCI_Disconnect | 0x0406 | Connection_Handle, Reason | Command_Status; HCI_Disconnection_Complete | 1.0 |
| HCI_Accept_Connection_Request | 0x0409 | BD_ADDR, Role (0=Central, 1=Peripheral) | Command_Status; HCI_Connection_Complete | 1.0 |
| HCI_Reject_Connection_Request | 0x040A | BD_ADDR, Reason | Command_Status; HCI_Connection_Complete (remote, status=Reason) | 1.0 |
| HCI_Remote_Name_Request | 0x0419 | BD_ADDR, Page_Scan_Repetition_Mode, Clock_Offset | Command_Status; HCI_Remote_Name_Request_Complete | 1.0 |
| HCI_Read_Remote_Version_Information | 0x041D | Connection_Handle | Command_Status; HCI_Read_Remote_Version_Information_Complete | 1.0 |
| HCI_Setup_Synchronous_Connection | 0x0428 | Connection_Handle, Tx/Rx_Bandwidth, Max_Latency, Voice_Setting, Retransmission_Effort, Packet_Type | Command_Status; HCI_Synchronous_Connection_Complete | 1.1 |
| HCI_IO_Capability_Request_Reply | 0x042B | BD_ADDR, IO_Capability, OOB_Data_Present, Authentication_Requirements | Status, BD_ADDR | 2.1+EDR |
| HCI_User_Confirmation_Request_Reply | 0x042C | BD_ADDR | Status, BD_ADDR | 2.1+EDR |
| HCI_User_Passkey_Request_Reply | 0x042E | BD_ADDR, Numeric_Value | Status, BD_ADDR | 2.1+EDR |
| HCI_Switch_Role | 0x080B | BD_ADDR, Role (0=Central, 1=Peripheral) | Command_Status; HCI_Role_Change | 1.0 |
| HCI_Sniff_Mode | 0x0803 | Connection_Handle, Sniff_Max/Min_Interval, Sniff_Attempt, Sniff_Timeout | Command_Status; HCI_Mode_Change | 1.0 |
| HCI_Exit_Sniff_Mode | 0x0804 | Connection_Handle | Command_Status; HCI_Mode_Change | 1.0 |
| HCI_Write_Authenticated_Payload_Timeout | 0x0C5C | Connection_Handle, Authenticated_Payload_Timeout (×10 ms) | Status, Connection_Handle | 4.1 |

---

## Controller & Host Flow Control

| Command | Opcode | Key Parameters | Return / Event | Since |
|---------|--------|----------------|----------------|-------|
| HCI_Host_Number_Of_Completed_Packets | 0x0C35 | Num_Handles, Connection_Handle[i], Host_Num_Completed_Packets[i] | none; no event | 1.0 |
| HCI_Host_Buffer_Size | 0x0C33 | Host_ACL_Data_Packet_Length, Host_Synchronous_Data_Packet_Length, Host_Total_Num_ACL_Data_Packets, Host_Total_Num_Synchronous_Data_Packets | Status | 1.0 |
| HCI_Set_Controller_To_Host_Flow_Control | 0x0C31 | Flow_Control_Enable (0=off, 1=ACL only, 2=SCO only, 3=both) | Status | 1.0 |

---

## Key HCI Events

Events generated asynchronously by the Controller; Host must process them on the HCI interrupt/callback.

| Event | Code | Subevent | Key Fields | Trigger |
|-------|------|----------|------------|---------|
| HCI_Command_Complete | 0x0E | — | Num_HCI_Command_Packets, Command_Opcode, Return_Parameters | All synchronous commands |
| HCI_Command_Status | 0x0F | — | Status, Num_HCI_Command_Packets, Command_Opcode | All async commands (Disconnect, Create_Connection, LE_Create_Connection, etc.) |
| HCI_Hardware_Error | 0x10 | — | Hardware_Code | Hardware failure |
| HCI_Number_Of_Completed_Packets | 0x13 | — | Num_Handles, Connection_Handle[i], Num_Completed_Packets[i] | After TX packets consumed by Controller |
| HCI_Disconnection_Complete | 0x05 | — | Status, Connection_Handle, Reason | Link teardown |
| HCI_Encryption_Change | 0x08 | — | Status, Connection_Handle, Encryption_Enabled (0/1/2) | After LE_Enable_Encryption |
| HCI_Encryption_Key_Refresh_Complete | 0x30 | — | Status, Connection_Handle | Key refresh |
| **LE Meta Event** | **0xFF** | | Subevent code in byte 1 | All LE async events |
| LE_Connection_Complete | 0xFF | 0x01 | Status, Connection_Handle, Role, Peer_Address_Type, Peer_Address, Conn_Interval, Peripheral_Latency, Supervision_Timeout | New LE connection |
| LE_Enhanced_Connection_Complete [v1] | 0xFF | 0x0A | Adds Local_Resolvable_Private_Address, Peer_Resolvable_Private_Address | New LE connection (privacy-aware) |
| LE_Enhanced_Connection_Complete [v2] | 0xFF | 0x29 | Adds Advertising_Handle, Subevent for PAwR connections | 5.4 |
| LE_Advertising_Report | 0xFF | 0x02 | Num_Reports, Event_Type, Address_Type, Address, Data_Length, Data, RSSI | Legacy scan result |
| LE_Extended_Advertising_Report | 0xFF | 0x0D | Event_Type (2 bytes), Address_Type, Address, Primary_PHY, Secondary_PHY, Advertising_SID, TX_Power, RSSI, Periodic_Advertising_Interval, Direct_Address, Data | Extended scan result (5.0+) |
| LE_Connection_Update_Complete | 0xFF | 0x03 | Status, Connection_Handle, Conn_Interval, Peripheral_Latency, Supervision_Timeout | Connection params changed |
| LE_PHY_Update_Complete | 0xFF | 0x0C | Status, Connection_Handle, TX_PHY, RX_PHY | PHY negotiation done (5.0+) |
| LE_Data_Length_Change | 0xFF | 0x07 | Connection_Handle, Max_TX_Octets, Max_TX_Time, Max_RX_Octets, Max_RX_Time | DLE negotiation (4.2+) |
| LE_Long_Term_Key_Request | 0xFF | 0x05 | Connection_Handle, Random_Number, Encrypted_Diversifier | Peripheral must reply with LTK |
| LE_Periodic_Advertising_Sync_Established [v1] | 0xFF | 0x0E | Status, Sync_Handle, Advertising_SID, Advertiser_Address_Type, Advertiser_Address, Advertiser_PHY, Periodic_Advertising_Interval, Advertiser_Clock_Accuracy | 5.0+ |
| LE_Periodic_Advertising_Report [v1] | 0xFF | 0x0F | Sync_Handle, TX_Power, RSSI, CTE_Type, Data_Status, Data_Length, Data | Periodic adv data (5.0+) |
| LE_CIS_Established [v1] | 0xFF | 0x19 | Status, Connection_Handle (CIS), CIG_Sync_Delay (µs), CIS_Sync_Delay, Transport_Latency_C→P/P→C, PHY_C→P/P→C, NSE, BN_C→P/P→C, FT_C→P/P→C, Max_PDU_C→P/P→C, ISO_Interval | 5.2+ |
| LE_CIS_Request | 0xFF | 0x1A | ACL_Connection_Handle, CIS_Connection_Handle, CIG_ID, CIS_ID | Peripheral receives CIS setup |
| LE_Create_BIG_Complete | 0xFF | 0x1B | Status, BIG_Handle, BIG_Sync_Delay, Transport_Latency_BIG, PHY, NSE, BN, PTO, IRC, Max_PDU, ISO_Interval, Num_BIS, Connection_Handle[i] | 5.2+ |
| LE_Terminate_BIG_Complete | 0xFF | 0x1C | BIG_Handle, Reason | 5.2+ |
| LE_BIG_Sync_Established | 0xFF | 0x1D | Status, BIG_Handle, Transport_Latency_BIG, NSE, BN, PTO, IRC, Max_PDU, ISO_Interval, Num_BIS, Connection_Handle[i] | 5.2+ |
| LE_Transmit_Power_Reporting | 0xFF | 0x21 | Status, Connection_Handle, Reason, PHY, TX_Power_Level, TX_Power_Level_Flag, Delta | 5.2+ |
| LE_Path_Loss_Threshold | 0xFF | 0x20 | Connection_Handle, Current_Path_Loss, Zone_Entered (0=low, 1=mid, 2=high) | 5.2+ |
| LE_Subrate_Change | 0xFF | 0x23 | Status, Connection_Handle, Subrate_Factor, Peripheral_Latency, Continuation_Number, Supervision_Timeout | 5.3+ |
| LE_CS_Read_Remote_Supported_Capabilities_Complete | 0xFF | 0x2C | Status + full capability set | 6.0+ |
| LE_CS_Config_Complete | 0xFF | 0x2F | Status, Connection_Handle, Config_ID, Action (0=removed, 1=created/modified), Config fields | 6.0+ |
| LE_CS_Procedure_Enable_Complete | 0xFF | 0x30 | Status, Connection_Handle, Config_ID, State (0=disabled, 1=enabled), tone_antenna_config, selected_TX_power, subevent_len, subevents_per_interval, subevent_interval, event_interval, procedure_interval, procedure_count, max_procedure_len | 6.0+ |
| LE_CS_Subevent_Result | 0xFF | 0x31 | Connection_Handle, Config_ID, Start_ACL_Conn_Event, Procedure_Counter, Freq_Compensation, Reference_Power_Level, Procedure_Done_Status, Subevent_Done_Status, Abort_Reason, Num_Antenna_Paths, Num_Steps, per-step: Step_Mode, Step_Channel, Step_Data_Length, Step_Data | 6.0+ |
| LE_Frame_Space_Update_Complete | 0xFF | 0x35 | Status, Connection_Handle | 6.2+ |
| LE_UTP_Receive | 0xFF | 0x36 | UTP_Data_Length, UTP_Data | 6.2+ |
| LE_Connection_Rate_Change | 0xFF | 0x37 | Status, Connection_Handle, Conn_Interval (×125 µs), Subrate_Factor, Peripheral_Latency, Continuation_Number, Supervision_Timeout | 6.2+ |

---

## Common Parameter Reference

| Parameter | Min | Max | Unit | Typical Range | Notes |
|-----------|-----|-----|------|---------------|-------|
| Advertising_Interval | 0x0020 | 0x4000 | 0.625 ms | 20 ms – 10.24 s | Default: 0x0800 (1.28 s). Min of 100 ms recommended for connectable |
| Scan_Interval | 0x0004 | 0x4000 | 0.625 ms | 2.5 ms – 10.24 s | Scan_Window ≤ Scan_Interval |
| Scan_Window | 0x0004 | 0x4000 | 0.625 ms | 2.5 ms – 10.24 s | Continuous scan when Window = Interval |
| Connection_Interval (classic LE) | 0x0006 | 0x0C80 | 1.25 ms | 7.5 ms – 4 s | Used by `HCI_LE_Create_Connection` and `HCI_LE_Connection_Update` |
| Connection_Interval (6.2 short) | 0x0003 | 0x7D00 | 125 µs | 375 µs – 4 s | Used by `HCI_LE_Connection_Rate_Request`; requires Connection Rate feature |
| Peripheral_Latency (subevents) | 0x0000 | 0x01F3 | events | 0 – 499 | Must satisfy: (Latency+1) × Interval < Supervision_Timeout/2 |
| Supervision_Timeout | 0x000A | 0x0C80 | 10 ms | 100 ms – 32 s | Must be > 2 × Conn_Interval × (Peripheral_Latency + 1) |
| Subrate_Factor | 0x0001 | 0x01F4 | — | 1 – 500 | 5.3+ only. Subrate_Max × (Max_Latency + 1) ≤ 500 |
| RPA_Timeout [v1] | 0x0001 | 0x0E10 | 1 s | 1 s – 1 hour | Default 900 s (15 min) |
| RPA_Timeout [v2] | 0x0001 | 0x0E10 | 1 s | 480 s – 900 s | 6.1+: randomized between Min and Max; default Min=480 s, Max=900 s |
| TX_Octets (DLE) | 0x001B | 0x00FB | bytes | 27 – 251 bytes | Per LL Data PDU payload |
| TX_Time (DLE) | 0x0148 | 0x4290 | 1 µs | 328 – 17040 µs | |
| CIG_SDU_Interval | 0x0000FF | 0x0FFFFF | 1 µs | 1.25 ms – 8 ms | Per-SDU interval for CIS |
| BIG_SDU_Interval | 0x0000FF | 0x0FFFFF | 1 µs | 1.25 ms – 8 ms | Per-SDU interval for BIS |
| Max_SDU | 0x0001 | 0x0FFF | bytes | 40 – 240 bytes | Max SDU size per CIS/BIS direction |
| CS_CTE_Length | 0x02 | 0x14 | 8 µs | 16 – 160 µs | Constant Tone Extension duration |
| CS_T_IP1 / T_IP2 | varies | varies | µs | 10–145 µs | CS tone measurement intervals; capability-dependent |
| ISO_Interval | 0x0004 | 0x0C80 | 1.25 ms | 5 ms – 4 s | CIS/BIS isochronous event interval |

---

## OGF Summary

| OGF | Value | Command Group |
|-----|-------|---------------|
| Link Control | 0x01 | Inquiry, connection setup, SCO |
| Link Policy | 0x02 | Sniff, role switch, QoS |
| Controller & Baseband | 0x03 | Reset, event mask, host config |
| Informational | 0x04 | Version, features, BD_ADDR, buffer sizes |
| Status | 0x05 | RSSI, link quality, clock |
| Testing | 0x06 | Loopback, test modes |
| **LE Controller** | **0x08** | All HCI_LE_* commands |
| Vendor Specific | 0x3F | Manufacturer-defined |

> Full opcode = `(OGF << 10) | OCF`. Example: `HCI_LE_Create_Connection` = `(0x08 << 10) | 0x000D` = `0x200D`.

---

*Source: [Core 6.2, Vol 4, Part E, §7] and [HCI.ICS.p30]*
