# PBP.ICS.p4-2

> Source: PDF converted via PyMuPDF.

---

Public Broadcast Profile (PBP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: PBP.ICS.p4 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Audio, Telephony, and Automotive Working Group ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2021–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 General principles


### 1.1 Implementation Under Test (IUT) identification

Using the Bluetooth SIG qualification tool, the implementer is expected to declare details about what will be implemented.

### 1.2 Enforcement of inter-layer dependencies

This ICS includes one or more tables with inter-layer dependencies (ILDs). ILDs are used for specification requirements that are dependent on other supporting specifications. ILDs can refer to an individual ICS item in a separate layer (individual ILD), or it can refer to the full layer (full-layer ILD).
ILDs residing in an X2Core layer will be enforced from the Bluetooth SIG qualification tool in the following conditions, depending on where the referred ILD is residing:

|  | Referred ILD resides in |  |  | Individual ILD |  |  | Full-layer ILD |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Controller layer | Controller layer |  | Core-Complete configuration, or Referred layer is supported |  |  | N/A |  |  |
|  | Lower HCI layer |  | HCI is supported |  |  | N/A |  |  |
| Upper HCI layer | Upper HCI layer |  | Core-Host configuration, or UHCI is supported |  |  | N/A |  |  |
| Host layer |  |  | Core-Host configuration, or Core-Complete configuration, or Referred layer is supported |  |  | N/A |  |  |
| X2Core layer |  |  | Core-Host configuration, or Core-Complete configuration, or Referred layer is supported |  |  | Core-Host configuration, or Core-Complete configuration |  |  |

Table 1.1: Enforcement of an ILD within the Bluetooth SIG qualification tool

## 2 ICS declarations


### 2.1 Roles

Table 1: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Public Broadcast Source |  |  | [1] 2.1 |  |  | C.1 |  |  |
| 2 |  |  | Public Broadcast Sink |  |  | [1] 2.1 |  |  | C.1 |  |  |
| 3 |  |  | Public Broadcast Assistant |  |  | [1] 2.1 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.3 [4] 2.4 |  |  | C.1 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.3 [4] 2.4 |  |  | C.2, C.3 |  |  |

C.1: Excluded for this Profile. C.2: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core- Controller”. C.3: Mandatory for this Profile.

### 2.3 Public Broadcast Source Role

Table 3: X.Y Versions
Prerequisite: PBP 1/1 “Public Broadcast Source”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBP v1.0 |  |  | [1] |  |  | M |  |  |

Table 4: X.Y.Z Versions
Prerequisite: PBP 1/1 “Public Broadcast Source”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBP v1.0.1 |  |  | [4] |  |  | C.1 |  |  |
| 2 |  |  | PBP v1.0.2 |  |  | [5] |  |  | C.1 |  |  |

C.1: Optional to support one and only one.

#### 2.3.1 Public Broadcast Source Role Features

Table 5: Public Broadcast Source Role – Support Requirements
Prerequisite: PBP 1/1 “Public Broadcast Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initiator | [1] 3.1.1 [4] 3.1 | M | [3] CAP 1/2 |  |  |
| 2 | BAP Broadcast Source | [1] 2.1 [4] 3.1 | M | [3] CAP 16/2 |  |  |

Table 6: Public Broadcast Source Role – Features
Prerequisite: PBP 1/1 “Public Broadcast Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Transmit Program Info Metadata _ | [1] 3.1.2 [4] 3.2.2 | O | N/A |  |  |
| 2 | BAP Broadcast Audio Stream Metadata Update | [1] 3.1.2 [4] 3.2.2 | C.1 | [2] BAP 51/1 |  |  |
| 3 | Public Broadcast Announcement | [1] 4 | M | N/A |  |  |
| 4 | Standard Quality Public Broadcast Audio | [1] 4.1 | M | N/A |  |  |
| 5 | High Quality Public Broadcast Audio | [1] 4.2 | O | N/A |  |  |
| 6 | Encrypted Broadcast Isochronous Stream | [1] 4 | C.2 | [2] BAP 61/6 |  |  |
| 7 | Unencrypted Broadcast Isochronous Stream | [1] 4 | C.2 | [2] BAP 61/5 |  |  |
| 8 | Broadcast Name AD Type | [1] 5 | M | N/A |  |  |
| 9 | Broadcast Name of length 4 to 32 octets | [5] 5.1.1 | C.3 | N/A |  |  |

C.1: Mandatory IF PBP 6/1 “Transmit Program_Info Metadata”, otherwise not defined. C.2: Mandatory to support at least one. C.3: Mandatory IF PBP 4/2 “PBP v1.0.2”, otherwise Optional.
Table 7: Standard Quality Public Broadcast Audio Configuration Support Requirements
Prerequisite: PBP 6/4 “Standard Quality Public Broadcast Audio”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency |  |  |  |  |  |  |
| 1 | 16 2 1 LC3: 10000 SDU Interval, unframed, _ _ 40 Max SDU Size, 2 RTN, 10 Max Transport Latency _ _ | [1] 4.2 | M | [2] BAP 55/4 |  |  |
| 2 | 24 2 1 LC3: 10000 SDU Interval, unframed, _ _ 60 Max SDU Size, 2 RTN, 10 Max Transport Latency _ _ | [1] 4.2 | O | [2] BAP 55/6 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| High Reliability |  |  |  |  |  |  |
| 3 | 16 2 2 LC3: 10000 SDU Interval, unframed, _ _ 40 Max SDU Size, 4 RTN, 60 Max Transport Latency _ _ | [1] 4.2 | M | [2] BAP 56/4 |  |  |
| 4 | 24 2 2 LC3: 10000 SDU Interval, unframed, _ _ 60 Max SDU Size, 4 RTN, 60 Max Transport Latency _ _ | [1] 4.2 | O | [2] BAP 56/6 |  |  |

Table 8: High Quality Public Broadcast Audio Configuration Support Requirements
Prerequisite: PBP 6/5 “High Quality Public Broadcast Audio”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency |  |  |  |  |  |  |
| 1 | 48 1 1 LC3: 7500 SDU Interval, _ _ unframed, 75 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 55/11 |  |  |
| 2 | 48 2 1 LC3: 10000 SDU Interval, _ _ unframed, 100 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 55/12 |  |  |
| 3 | 48 3 1 LC3: 7500 SDU Interval, _ _ unframed, 90 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 55/13 |  |  |
| 4 | 48 4 1 LC3: 10000 SDU Interval, _ _ unframed, 120 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 55/14 |  |  |
| 5 | 48 5 1 LC3: 7500 SDU Interval, _ _ unframed, 117 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 55/15 |  |  |
| 6 | 48 6 1 LC3: 10000 SDU Interval, _ _ unframed, 155 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 55/16 |  |  |
| High Reliability |  |  |  |  |  |  |
| 7 | 48 1 2 LC3: 7500 SDU Interval, _ _ unframed, 75 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 56/11 |  |  |
| 8 | 48 2 2 LC3: 10000 SDU Interval, _ _ unframed, 100 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 56/12 |  |  |
| 9 | 48 3 2 LC3: 7500 SDU Interval, _ _ unframed, 90 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 56/13 |  |  |
| 10 | 48 4 2 LC3: 10000 SDU Interval, _ _ unframed, 120 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 56/14 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 11 | 48 5 2 LC3: 7500 SDU Interval, _ _ unframed, 117 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 56/15 |  |  |
| 12 | 48 6 2 LC3: 10000 SDU Interval, _ _ unframed, 155 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 56/16 |  |  |

C.1: Mandatory to support at least one.

### 2.4 Public Broadcast Sink Role

Table 9: X.Y Versions
Prerequisite: PBP 1/2 “Public Broadcast Sink”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBP v1.0 |  |  | [1] |  |  | M |  |  |

Table 10: X.Y.Z Versions
Prerequisite: PBP 1/2 “Public Broadcast Sink”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBP v1.0.1 |  |  | [4] |  |  | C.1 |  |  |
| 2 |  |  | PBP v1.0.2 |  |  | [5] |  |  | C.1 |  |  |

C.1: Optional to support one and only one.

#### 2.4.1 Public Broadcast Sink Role Features

Table 11: Public Broadcast Sink Role – Support Requirements
Prerequisite: PBP 1/2 “Public Broadcast Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Acceptor | [1] 3.2.1 [4] 3.1 | M | [3] CAP 1/1 |  |  |
| 2 | BAP Broadcast Sink | [1] 3.2.1 [4] 3.1 | M | [3] CAP 6/3 |  |  |

Table 12: Public Broadcast Sink Role – Features
Prerequisite: PBP 1/2 “Public Broadcast Sink”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Standard Quality Public Broadcast Audio |  |  | [1] 4.1 |  |  | M |  |  |
| 2 |  |  | High Quality Public Broadcast Audio |  |  | [1] 4.2 |  |  | O |  |  |
| 3 |  |  | Broadcast Name of length 4 to 32 octets |  |  | [5] 5.1.1 |  |  | C.1 |  |  |

C.1: Mandatory IF PBP 10/2 “PBP v1.0.2”, otherwise Optional.
Prerequisite: PBP 12/1 “Standard Quality Public Broadcast Audio”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency |  |  |  |  |  |  |
| 1 | 16 2 1 LC3: 10000 SDU Interval, _ _ unframed, 40 Max SDU Size, 2 RTN, 10 Max Transport Latency _ _ | [1] 4.2 | M | [2] BAP 69/4 |  |  |
| 2 | 24 2 1 LC3: 10000 SDU Interval, _ _ unframed, 60 Max SDU Size, 2 RTN, 10 Max Transport Latency _ _ | [1] 4.2 | M | [2] BAP 69/6 |  |  |
| High Reliability |  |  |  |  |  |  |
| 3 | 16 2 2 LC3: 10000 SDU Interval, _ _ unframed, 40 Max SDU Size, 4 RTN, 60 Max Transport Latency _ _ | [1] 4.2 | M | [2] BAP 70/4 |  |  |
| 4 | 24 2 2 LC3: 10000 SDU Interval, _ _ unframed, 60 Max SDU Size, 4 RTN, 60 Max Transport Latency _ _ | [1] 4.2 | M | [2] BAP 70/6 |  |  |

Table 14: High Quality Public Broadcast Audio Configuration Support Requirements
Prerequisite: PBP 12/2 “High Quality Public Broadcast Audio”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency |  |  |  |  |  |  |
| 1 | 48 1 1 LC3: 7500 SDU Interval, _ _ unframed, 75 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 69/11 |  |  |
| 2 | 48 2 1 LC3: 10000 SDU Interval, _ _ unframed, 100 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 69/12 |  |  |
| 3 | 48 3 1 LC3: 7500 SDU Interval, _ _ unframed, 90 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 69/13 |  |  |
| 4 | 48 4 1 LC3: 10000 SDU Interval, _ _ unframed, 120 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 69/14 |  |  |
| 5 | 48 5 1 LC3: 7500 SDU Interval, _ _ unframed, 117 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 69/15 |  |  |
| 6 | 48 6 1 LC3: 10000 SDU Interval, _ _ unframed, 155 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 69/16 |  |  |
| High Reliability |  |  |  |  |  |  |
| 7 | 48 1 2 LC3: 7500 SDU Interval, _ _ unframed, 75 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 70/11 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 8 | 48 2 2 LC3: 10000 SDU Interval, _ _ unframed, 100 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 70/12 |  |  |
| 9 | 48 3 2 LC3: 7500 SDU Interval, _ _ unframed, 90 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 70/13 |  |  |
| 10 | 48 4 2 LC3: 10000 SDU Interval, _ _ unframed, 120 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 70/14 |  |  |
| 11 | 48 5 2 LC3: 7500 SDU Interval, _ _ unframed, 117 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 70/15 |  |  |
| 12 | 48 6 2 LC3: 10000 SDU Interval, _ _ unframed, 155 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [1] 4.3 | C.1 | [2] BAP 70/16 |  |  |

C.1: Mandatory to support at least one.

#### 2.4.2 Feature requirements in Core layers


##### 2.4.2.1 LL requirements

Table 14a: LL Requirements – PBK
Prerequisite: PBP 1/2 “Public Broadcast Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE 2M PHY | [5] 3.5 | C.1 | [6] LL 9/7 |  |  |

C.1: Mandatory IF PBP 10/2 “PBP v1.0.2”, otherwise Optional.

### 2.5 Public Broadcast Assistant Role

Table 15: X.Y Versions
Prerequisite: PBP 1/3 “Public Broadcast Assistant”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBP v1.0 |  |  | [1] |  |  | M |  |  |

Table 16: X.Y.Z Versions
Prerequisite: PBP 1/3 “Public Broadcast Assistant”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBP v1.0.1 |  |  | [4] |  |  | C.1 |  |  |
| 2 |  |  | PBP v1.0.2 |  |  | [5] |  |  | C.1 |  |  |

C.1: Optional to support one and only one.

#### 2.5.1 Public Broadcast Assistant Role Features

Table 17: Public Broadcast Assistant Role – Support Requirements
Prerequisite: PBP 1/3 “Public Broadcast Assistant”

| Item | Capability | Reference | Status | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Dependency |  |
| 1 | Commander | [1] 3.3.1 [4] 3.1 | M | [3] CAP 1/3 |  |
| 2 | BAP Broadcast Assistant | [1] 3.3.1 [4] 3.1 | M | [3] CAP 26/2 |  |

Table 17a: Public Broadcast Assistant Role – Features
Prerequisite: PBP 1/3 “Public Broadcast Assistant”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcast Name of length 4 to 32 octets |  |  | [5] 5.1.1 |  |  | C.1 |  |  |

C.1: Mandatory IF PBP 16/2 “PBP v1.0.2”, otherwise Optional.

#### 2.5.2 Feature requirements in Core layers


##### 2.5.2.1 LL requirements

Table 18: LL Requirements – PBA
Prerequisite: PBP 1/3 “Public Broadcast Assistant”

| Item | Capability | Reference | Status | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Dependency |  |
| 1 | LE 2M PHY | [5] 3.5 | C.1 |  | [6] LL 9/7 |  |  |

C.1: Mandatory IF PBP 16/2 “PBP v1.0.2”, otherwise Optional.

## 3 References

[1] Public Broadcast Profile Specification, Version 1.0 or later
[2] ICS Proforma for Basic Audio Profile (BAP)
[3] ICS Proforma for Common Audio Profile (CAP)
[4] Public Broadcast Profile Specification, Version 1.0.1 or later
[5] Public Broadcast Profile Specification, Version 1.0.2 or later
[6] ICS Proforma for Link Layer (LL)

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2022-07-12 | Approved by BTI on 2022-07-03. PBP v1.0 adopted by the BoD on 2022-07-05. Prepared for initial publication. |
|  |  |  | p1r00–r01 |  |  | 2024-08-13 – 2024-08-26 | TSE 25246 (rating 1): Per E24733, updated the references cited in Tables 2, 5, 6, 11, and 17. Updated the references list to add PBP v1.0.1. TSE 25564 (rating 1): Per E23389, E23860, and E24733, added Tables 4, 10, and 16 to account for PBP v1.0.1 as part of the .Z release. Updated the references list. Made editorial updates to align the document with the latest ICS template. Updated the copyright year. |
| 1 |  |  | p1 |  |  | 2024-10-08 | Approved by BTI on 2024-09-11. PBP v1.0.1 adopted by the BoD on 2024-10-01. Prepared for TCRL 2024- 2-addition publication. |
|  |  |  | p2r00 |  |  | 2025-04-21 | TSE 27358 (rating 1): Updated the Status value for PBP 2/2 and added conditions C.2 and C.3 to Table 2. Incorporated editorials to align the document with the latest ICS template, including updates to Section 1 and the addition of a section heading for the ICS declarations section. |
| 2 |  |  | p2 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p3r00–r03 |  |  | 2025-07-23 – 2025-08-18 | TSE 27403 (rating 4): Per E23131, updated entries and added conditional C.1 to Tables 4, 10, and 16. Added new sections for Feature requirements in Core layers and LL requirements. Added Tables 14a and 18. Updated References section. TSE 27940 (rating 4): Per E24424, added new row and conditional C.3 to Table 6. Added new row and conditional C.1 to Table 12. Added Table 17a. |
| 3 |  |  | p3 |  |  | 2025-11-04 | Approved by BTI on 2025-09-29. Prepared for TCRL pkg101 publication. |
|  |  |  | p4r00 |  |  | 2025-12-05 – 2026-01-06 | TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 4 |  |  | p4 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Siegfried Lehmann |  |  | Apple Inc. |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Dejan Berec |  |  | Bluetooth SIG, Inc. |  |  |
| Tharon Hall |  |  | Bluetooth SIG, Inc. |  |  |
| Rasmus Abildgren |  |  | Bose |  |  |
| Nick Hunn |  |  | GN Hearing A/S |  |  |
| HJ Lee |  |  | LG Electronics |  |  |
| Chris Church |  |  | Qualcomm |  |  |
| Georg Dickmann |  |  | Sonova AG |  |  |
| Andrew Estrada |  |  | Sony Corporation |  |  |
| Jeff Solum |  |  | Starkey Hearing Technologies |  |  |
