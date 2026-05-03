# Erratum 18552 Access to Additional CIS Parameters

> Source: PDF converted via PyMuPDF.

---

Errata Correction 18552: Access to Additional CIS Parameters
Bluetooth® Errata Correction
▪ Version: v1.0
▪ Version Date: 2024-06-11
▪ Prepared By: Core Specification Working Group
This Errata Correction applies to the following specifications (collectively, the “Source Specifications”):
• Core Specification v5.4 [1]
• Core Specification v5.3 [2]
• Core Specification v5.2 [3]
Abstract:
This document specifies the changes to be applied to the Core Specifications required to provide access to CIS parameters that are not available to the Peripheral using existing mechanisms.
Version History

| Version Number |  | Date |  | Comments |
| --- | --- | --- | --- | --- |
|  |  | (yyyy-mm-dd) |  |  |
| v1.0 | 2024-06-11 |  |  | Adopted by the Bluetooth SIG Board of Directors. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Clive Feather |  |  | Samsung Electronics Co. Ltd |  |  |
| Emil Gydesen |  |  | Nordic Semiconductor ASA |  |  |
| Sam Geeraerts |  |  | NXP Semiconductors |  |  |

Use of this specification is your acknowledgement that you agree to and will comply with the following notices and disclaimers. You are advised to seek appropriate legal, engineering, and other professional advice regarding the use, interpretation, and effect of this specification.
Use of Bluetooth specifications by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG and its members, including those agreements posted on Bluetooth SIG’s website located at www.bluetooth.com. Any use of this specification by a member that is not in compliance with the applicable membership and other related agreements is prohibited and, among other things, may result in (i) termination of the applicable agreements and (ii) liability for infringement of the intellectual property rights of Bluetooth SIG and its members. This specification may provide options, because, for example, some products do not implement every portion of the specification. All content within the specification, including notes, appendices, figures, tables, message sequence charts, examples, sample data, and each option identified is intended to be within the bounds of the Scope as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”). Also, the identification of options for implementing a portion of the specification is intended to provide design flexibility without establishing, for purposes of the PCLA, that any of these options is a “technically reasonable non-infringing alternative.”
Use of this specification by anyone who is not a member of Bluetooth SIG is prohibited and is an infringement of the intellectual property rights of Bluetooth SIG and its members. The furnishing of this specification does not grant any license to any intellectual property of Bluetooth SIG or its members. THIS SPECIFICATION IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, TITLE, NON- INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, OR THAT THE CONTENT OF THIS SPECIFICATION IS FREE OF ERRORS. For the avoidance of doubt, Bluetooth SIG has not made any search or investigation as to third parties that may claim rights in or to any specifications or any intellectual property that may be required to implement any specifications and it disclaims any obligation or duty to do so.
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS SPECIFICATION AND ANY INFORMATION CONTAINED IN THIS SPECIFICATION, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF THE DAMAGES.
Products equipped with Bluetooth wireless technology ("Bluetooth Products") and their combination, operation, use, implementation, and distribution may be subject to regulatory controls under the laws and regulations of numerous countries that regulate products that use wireless non-licensed spectrum. Examples include airline regulations, telecommunications regulations, technology transfer controls, and health and safety regulations. You are solely responsible for complying with all applicable laws and regulations and for obtaining any and all required authorizations, permits, or licenses in connection with your use of this specification and development, manufacture, and distribution of Bluetooth Products. Nothing in this specification provides any information or assistance in connection with complying with applicable laws or regulations or obtaining required authorizations, permits, or licenses.
Bluetooth SIG is not required to adopt any specification or portion thereof. If this specification is not the final version adopted by Bluetooth SIG’s Board of Directors, it may not be adopted. Any specification adopted by Bluetooth SIG’s Board of Directors may be withdrawn, replaced, or modified at any time. Bluetooth SIG reserves the right to change or alter final specifications in accordance with its membership and operating agreements.
Copyright © 2023. All copyrights in the Bluetooth Specifications themselves are owned by Apple Inc., Ericsson AB, Intel Corporation, Lenovo (Singapore) Pte. Ltd., Microsoft Corporation, Nokia Corporation, and Toshiba Corporation. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Drafting conventions


### 1.1 Language

Refer to and follow any terminology, language conventions, and interpretation sections of the Source Specification(s).

### 1.2 Formatting and color

The formatting and color conventions described in Table 1.1 below are used in this Errata Correction to describe the specific changes and additions to the Source Specification(s) identified on the cover page.

| Text Color | Description |
| --- | --- |
| black | Text that is unmodified from the Source Specification. |
| red | Text that is added to the Source Specification. |
| red strikethrough | Text that is deleted from the Source Specification. |
| [green bracketed text] | Comments that are intended to aid the reader. |
| blue | Default color used for section numbers and headings of this document. |

Table 1.1: Color key for headings, captions, and body text

## 2 Changes to Core Specification v5.4

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.4.

### 2.1 Changes to Core Specification v5.4, Volume 4, Part E: HCI


#### 2.1.1 [Modified Section] Section 3 Overview of commands and events

[Update the “LE CIS Established event” row in Table 3.1.]

| Name | Vers. | Summary description | BR/EDR | LE |
| --- | --- | --- | --- | --- |
| LE CIS Established event | 5.2 Erratum 18552 | The HCI LE CIS Established event indicates _ _ _ that the Controller established a CIS. | E | [v1] C.38 [v2] C.159 |

[Add the following conditional to the list at the end of Table 3.1 in numerical order of assigned number.]
C.158: Mandatory if the Set Min Encryption Key Size command is supported, otherwise optional.
C.159: Optional if the LE CIS Established event [v1] is supported, otherwise excluded.

#### 2.1.2 [Modified Section] Section 7.7.65.25 LE CIS Established event

[Amend the table at the beginning of the section as shown and add a new table row.]

| Event | Event Code | Event Parameters |
| --- | --- | --- |
| HCI LE CIS Established _ _ _ [v2] | 0x3E | Subevent Code, _ Status, Connection Handle, _ CIG Sync Delay, _ _ CIS Sync Delay, _ _ Transport Latency C To P, _ _ _ _ Transport Latency P To C, _ _ _ _ PHY C To P, _ _ _ PHY P To C, _ _ _ NSE, BN C To P, _ _ _ BN P To C, _ _ _ FT C To P, _ _ _ FT P To C, _ _ _ Max PDU C To P, _ _ _ _ |


|  |  | Max PDU P To C, _ _ _ _ ISO Interval, _ Sub Interval, _ Max SDU C To P, _ _ _ _ Max SDU P To C, _ _ _ _ SDU Interval C To P, _ _ _ _ SDU Interval P To C, _ _ _ _ Framing |
| --- | --- | --- |
| HCI LE CIS Established _ _ _ [v1] | 0x3E | Subevent Code, _ Status, Connection Handle, _ CIG Sync Delay, _ _ CIS Sync Delay, _ _ Transport Latency C To P, _ _ _ _ Transport Latency P To C, _ _ _ _ PHY C To P, _ _ _ PHY P To C, _ _ _ NSE, BN C To P, _ _ _ BN P To C, _ _ _ FT C To P, _ _ _ FT P To C, _ _ _ Max PDU C To P, _ _ _ _ Max PDU P To C, _ _ _ _ ISO Interval _ |

Description:
[Change the penultimate paragraph as shown.]
The NSE, BN_C_To_P, BN_P_To_C, FT_C_To_P, FT_P_To_C, Max_PDU_C_To_P, Max_PDU_P_To_C, and ISO_Interval remaining parameters are the corresponding parameters of the CIS (see [Vol 6] Part B, Section 4.5.13.1).
[Modify the Subevent_Code parameter block as shown.]
Subevent_Code: Size: 1 octet

| Value | Parameter Description |
| --- | --- |
| 0x2A | Subevent Code for HCI LE CIS Established [v2] event _ _ _ |
| 0x19 | Subevent Code for HCI LE CIS Established [v1] event _ _ _ |

[Add the following parameter blocks at the end of the section, after the ISO_Interval parameter block, as shown.]
ISO_Interval: Size: 2 octets

| Value | Parameter Description |
| --- | --- |
| N = 0xXXXX | The time between two consecutive CIS anchor points. Range: 0x0004 to 0x0C80 Time = N × 1.25 ms Time Range: 5 ms to 4 s. |

Sub_Interval: Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0x000000 | NSE = 1 (meaning there is no Sub Interval) _ |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive subevents in a CIS event Range: 0x000190 to ISO Interval×1250 – 1 _ |

Max_SDU_C_To_P: Size: 2 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXX | Maximum size, in octets, of the payload from the Central’s Host Range: 0 to 0x0FFF |


| Value | Parameter Description |
| --- | --- |
| 0xXXXX | Maximum size, in octets, of the payload from the Peripheral’s Host Range: 0 to 0x0FFF |

SDU_Interval_C_To_P Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive SDUs sent by the Central Range: 0x0000FF to 0x0FFFFF |

SDU_Interval_P_To_C Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive SDUs sent by the Peripheral Range: 0x0000FF to 0x0FFFFF |

Framing Size: 1 octet

| Value | Parameter Description |
| --- | --- |
| 0x00 | Unframed PDUs |
| 0x01 | Framed PDUs |
| All other values | Reserved for future use |

[Amend the following row of the LE_Event_Mask table as shown. Do not include “[v1]” in the cross- reference link.]
Command parameters:
LE_Event_Mask: Size: 8 octets

| Bit | LE Subevent Types |
| --- | --- |
| 23 | LE Periodic Advertising Sync Transfer Received event [v1] |
| 24 | LE CIS Established event [v1] |
| 25 | LE CIS Request event |

[Add the following row to the LE_Event_Mask table in the assigned position in numerical order by bit and make the second column a cross-reference link. Do not include “[v2]” in the cross-reference link.]

| Bit | LE Subevent Types |
| --- | --- |
| 40 | LE Enhanced Connection Complete event [v2] |
| 41 | LE CIS Established event [v2] |
| 60 to 63 | Reserved for future use (used for specification development purposes) |


## 3 Changes to Core Specification v5.3

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.3.

### 3.1 Changes to Core Specification v5.3, Volume 4, Part E: HCI


#### 3.1.1 [Modified Section] Section 3 Overview of commands and events

[Update the “LE CIS Established event” row in Table 3.1.]

| Name | Vers. | Summary description | BR/EDR | LE |
| --- | --- | --- | --- | --- |
| LE CIS Established event | 5.2 Erratum 18552 | The HCI LE CIS Established event indicates _ _ _ that the Controller established a CIS. | E | [v1] C38 [v2] C159 |

[Add the following conditional to the list at the end of Table 3.1 in numerical order of assigned number.]
C158: Mandatory if the Set Min Encryption Key Size command is supported, otherwise optional.
C159: Optional if the LE CIS Established event [v1] is supported, otherwise excluded.

#### 3.1.2 [Modified Section] Section 7.7.65.25 LE CIS Established event

[Amend the table at the beginning of the section as shown and add a new table row.]

| Event | Event Code | Event Parameters |
| --- | --- | --- |
| HCI LE CIS Established _ _ _ [v2] | 0x3E | Subevent Code, _ Status, Connection Handle, _ CIG Sync Delay, _ _ CIS Sync Delay, _ _ Transport Latency C To P, _ _ _ _ Transport Latency P To C, _ _ _ _ PHY C To P, _ _ _ PHY P To C, _ _ _ NSE, BN C To P, _ _ _ BN P To C, _ _ _ FT C To P, _ _ _ FT P To C, _ _ _ Max PDU C To P, _ _ _ _ |


|  |  | Max PDU P To C, _ _ _ _ ISO Interval, _ Sub Interval, _ Max SDU C To P, _ _ _ _ Max SDU P To C, _ _ _ _ SDU Interval C To P, _ _ _ _ SDU Interval P To C, _ _ _ _ Framing |
| --- | --- | --- |
| HCI LE CIS Established _ _ _ [v1] | 0x3E | Subevent Code, _ Status, Connection Handle, _ CIG Sync Delay, _ _ CIS Sync Delay, _ _ Transport Latency C To P, _ _ _ _ Transport Latency P To C, _ _ _ _ PHY C To P, _ _ _ PHY P To C, _ _ _ NSE, BN C To P, _ _ _ BN P To C, _ _ _ FT C To P, _ _ _ FT P To C, _ _ _ Max PDU C To P, _ _ _ _ Max PDU P To C, _ _ _ _ ISO Interval _ |

Description:
[Change the penultimate paragraph as shown.]
The NSE, BN_C_To_P, BN_P_To_C, FT_C_To_P, FT_P_To_C, Max_PDU_C_To_P, Max_PDU_P_To_C, and ISO_Interval remaining parameters are the corresponding parameters of the CIS (see [Vol 6] Part B, Section 4.5.13.1).
[Modify the Subevent_Code parameter block as shown.]
Subevent_Code: Size: 1 octet

| Value | Parameter Description |
| --- | --- |
| 0x2A | Subevent Code for HCI LE CIS Established [v2] event _ _ _ |
| 0x19 | Subevent Code for HCI LE CIS Established [v1] event _ _ _ |

[Add the following parameter blocks at the end of the section, after the ISO_Interval parameter block, as shown.]
ISO_Interval: Size: 2 octets

| Value | Parameter Description |
| --- | --- |
| N = 0xXXXX | The time between two consecutive CIS anchor points. Range: 0x0004 to 0x0C80 Time = N × 1.25 ms Time Range: 5 ms to 4 s. |

Sub_Interval: Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0x000000 | NSE = 1 (meaning there is no Sub Interval) _ |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive subevents in a CIS event Range: 0x000190 to ISO Interval×1250 – 1 _ |

Max_SDU_C_To_P: Size: 2 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXX | Maximum size, in octets, of the payload from the Central’s Host Range: 0 to 0x0FFF |


| Value | Parameter Description |
| --- | --- |
| 0xXXXX | Maximum size, in octets, of the payload from the Peripheral’s Host Range: 0 to 0x0FFF |

SDU_Interval_C_To_P Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive SDUs sent by the Central Range: 0x0000FF to 0x0FFFFF |

SDU_Interval_P_To_C Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive SDUs sent by the Peripheral Range: 0x0000FF to 0x0FFFFF |

Framing Size: 1 octet

| Value | Parameter Description |
| --- | --- |
| 0x00 | Unframed PDUs |
| 0x01 | Framed PDUs |
| All other values | Reserved for future use |

[Amend the following row of the LE_Event_Mask table as shown. Do not include “[v1]” in the cross- reference link.]
Command parameters:
LE_Event_Mask: Size: 8 octets

| Bit | LE Subevent Types |
| --- | --- |
| 23 | LE Periodic Advertising Sync Transfer Received event |
| 24 | LE CIS Established event [v1] |
| 25 | LE CIS Request event |

[Add the following row to the LE_Event_Mask table in the assigned position in numerical order by bit and make the second column a cross-reference link. Do not include “[v2]” in the cross-reference link.]

| Bit | LE Subevent Types |
| --- | --- |
| 34 | LE Subrate Change event |
| 41 | LE CIS Established event [v2] |
| 60 to 63 | Reserved for future use (used for specification development purposes) |


## 4 Changes to Core Specification v5.2

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.2.

### 4.1 Changes to Core Specification v5.2, Volume 4, Part E: HCI


#### 4.1.1 [Modified Section] Section 3 Overview of commands and events

[Update the “LE CIS Established event” row in Table 3.1.]

| Name | Vers. | Summary description | BR/EDR | AMP | LE |
| --- | --- | --- | --- | --- | --- |
| LE CIS Established event | 5.2 Erratum 18552 | The HCI LE CIS Established event _ _ _ indicates that the Controller established a CIS. | E | E | [v1] C38 [v2] C159 |

[Add the following conditional to the list at the end of Table 3.1 in numerical order of assigned number.]
C157: Mandatory if the Read Local Supported Codecs command [v2] is supported, otherwise optional.
C159: Optional if the LE CIS Established event [v1] is supported, otherwise excluded.

#### 4.1.2 [Modified Section] Section 7.7.65.25 LE CIS Established event

[Amend the table at the beginning of the section as shown and add a new table row.]

| Event | Event Code | Event Parameters |
| --- | --- | --- |
| HCI LE CIS Established _ _ _ [v2] | 0x3E | Subevent Code, _ Status, Connection Handle, _ CIG Sync Delay, _ _ CIS Sync Delay, _ _ Transport Latency M To S, _ _ _ _ Transport Latency S To M, _ _ _ _ PHY M To S, _ _ _ PHY S To M, _ _ _ NSE, BN M To S, _ _ _ BN S To M, _ _ _ FT M To S, _ _ _ FT S To M, _ _ _ Max PDU M To S, _ _ _ _ |


|  |  | Max PDU S To M, _ _ _ _ ISO Interval, _ Sub Interval, _ Max SDU M To S, _ _ _ _ Max SDU S To M, _ _ _ _ SDU Interval M To S, _ _ _ _ SDU Interval S To M, _ _ _ _ Framing |
| --- | --- | --- |
| HCI LE CIS Established _ _ _ [v1] | 0x3E | Subevent Code, _ Status, Connection Handle, _ CIG Sync Delay, _ _ CIS Sync Delay, _ _ Transport Latency M To S, _ _ _ _ Transport Latency S To M, _ _ _ _ PHY M To S, _ _ _ PHY S To M, _ _ _ NSE, BN M To S, _ _ _ BN S To M, _ _ _ FT M To S, _ _ _ FT S To M, _ _ _ Max PDU M To S, _ _ _ _ Max PDU S To M, _ _ _ _ ISO Interval _ |

Description:
[Change the second paragraph as shown.]
The CIG_Sync_Delay parameter is the maximum time, in microseconds, for transmission of PDUs of all CISes in a CIG in a CIG event (see [Vol 6] Part B, Section 4.5.14.1).
[Change the last paragraph as shown.]
The NSE, BN_M_To_S, BN_S_To_M, FT_M_To_S, FT_S_To_M, Max_PDU_M_To_S, Max_PDU_S_To_M, and ISO_Interval remaining parameters are the corresponding parameters of the CIS (see [Vol 6] Part B, Section 4.5.13.1).
[Modify the Subevent_Code parameter block as shown.]
Subevent_Code: Size: 1 octet

| Value | Parameter Description |
| --- | --- |
| 0x2A | Subevent Code for HCI LE CIS Established [v2] event _ _ _ |
| 0x19 | Subevent Code for HCI LE CIS Established [v1] event _ _ _ |

[Add the following parameter blocks at the end of the section, after the ISO_Interval parameter block, as shown.]
ISO_Interval: Size: 2 octets

| Value | Parameter Description |
| --- | --- |
| N = 0xXXXX | The time between two consecutive CIS anchor points. Range: 0x0004 to 0x0C80 Time = N × 1.25 ms Time Range: 5 ms to 4 s. |

Sub_Interval: Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0x000000 | NSE = 1 (meaning there is no Sub Interval) _ |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive subevents in a CIS event Range: 0x000190 to ISO Interval×1250 – 1 _ |

Max_SDU_M_To_S: Size: 2 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXX | Maximum size, in octets, of the payload from the Central’s1 Host Range: 0 to 0x0FFF |

[1 This is a replacement term for what is used in the referenced specification due to the original term now being deemed inappropriate [4].]

| Value | Parameter Description |
| --- | --- |
| 0xXXXX | Maximum size, in octets, of the payload from the Peripheral’s1 Host Range: 0 to 0x0FFF |

SDU_Interval_M_To_S Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive SDUs sent by the Central1 Range: 0x0000FF to 0x0FFFFF |

SDU_Interval_S_To_M Size: 3 octets

| Value | Parameter Description |
| --- | --- |
| 0xXXXXXX | Time, in microseconds, between the start of consecutive SDUs sent by the Peripheral1 Range: 0x0000FF to 0x0FFFFF |

Framing Size: 1 octet

| Value | Parameter Description |
| --- | --- |
| 0x00 | Unframed PDUs |
| 0x01 | Framed PDUs |
| All other values | Reserved for future use |

[1 This is a replacement term for what is used in the referenced specification due to the original term now being deemed inappropriate [4].]
[Amend the following row of the LE_Event_Mask table as shown. Do not include “[v1]” in the cross- reference link.]
Command parameters:
LE_Event_Mask: Size: 8 octets

| Bit | LE Subevent Types |
| --- | --- |
| 23 | LE Periodic Advertising Sync Transfer Received event |
| 24 | LE CIS Established event [v1] |
| 25 | LE CIS Request event |

[Add the following row to the LE_Event_Mask table in the assigned position in numerical order by bit and make the second column a cross-reference link. Do not include “[v2]” in the cross-reference link.]

| Bit | LE Subevent Types |
| --- | --- |
| 33 | LE BIGInfo Advertising Report event |
| 41 | LE CIS Established event [v2] |


## 5 References

[1] Bluetooth Core Specification, Version 5.4
[2] Bluetooth Core Specification, Version 5.3
[3] Bluetooth Core Specification, Version 5.2
[4] Appropriate Language Mapping Tables, https://www.bluetooth.com/language-mapping/Appropriate- Language-Mapping-Table