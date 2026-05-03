# LMP.ICS.p38

> Source: PDF converted via PyMuPDF.

---

Link Manager Protocol (LMP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: LMP.ICS.p38 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2003–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Capability Statement


#### 1.2.1 General Response Messages

Table 1: Response Messages

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Accept message |  |  | [1] 2.7 |  |  | M |  |  |
| 2 |  |  | Reject message |  |  | [1] 2.7 |  |  | M |  |  |


#### 1.2.2 Supported Features (General Statement)

Table 2: Supported Features

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 3-slot packets |  |  | [1] 3.3, 4.1.10 |  |  | O |  |  |
| 2 |  |  | 5-slot packets |  |  | [1] 3.3, 4.1.10 |  |  | O |  |  |
| 3 |  |  | Encryption |  |  | [1] 3.3, 4.2.5 |  |  | M |  |  |
| 4 |  |  | Slot offset |  |  | [1] 3.3, 4.4.1 |  |  | O |  |  |
| 5 |  |  | Timing accuracy |  |  | [1] 3.3, 4.3.1 |  |  | O |  |  |
| 6 |  |  | Role switch |  |  | [1] 3.3, 4.4.2 [3] 8.6.5 |  |  | C.5 |  |  |
| 7 |  |  | Hold mode |  |  | [1] 3.3, 4.5.1 |  |  | O |  |  |
| 8 |  |  | Sniff mode |  |  | [1] 3.3, 4.5.3 |  |  | O |  |  |
| 9 |  |  | Park mode |  |  | [1] 3.3, 4.5.3 |  |  | C.21 |  |  |
| 10 |  |  | Power Control |  |  | [1] 3.3, 4.1.3 [2] 3 |  |  | C.1 |  |  |
| 11 |  |  | Channel quality driven data rate |  |  | [1] 3.3, 4.1.7 |  |  | O |  |  |
| 12 |  |  | SCO link |  |  | [1] 3.3, 4.6.1 [3] 4.3, 6.5.2.1, 6.5.2.4 |  |  | O |  |  |
| 13 |  |  | RSSI with inquiry results |  |  | [1] 3.3 [3] 8.4.2 |  |  | O |  |  |
| 13a |  |  | Power Control Requests |  |  | [1] 3.3, 4.1.3 |  |  | O |  |  |
| 14 |  |  | Broadcast encryption |  |  | [1] 3.3, 4.2.4, 4.2.6 |  |  | C.18 |  |  |
| 15 |  |  | eSCO link |  |  | [1] 3.3, 4.6.2 [3] 5.5, 6.5.3.1 |  |  | O |  |  |
| 16 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 17 |  |  | Enhanced Data Rate ACL (2 Mb/s mode) |  |  | [1] 3.3 [3] 6.5.4 |  |  | O |  |  |
| 17a |  |  | Enhanced Data Rate ACL (3 Mb/s mode) |  |  | [1] 3.3 [3] 6.5.4 |  |  | C.19 |  |  |
| 18 |  |  | Enhanced Data Rate eSCO (2 Mb/s mode) |  |  | [1] 3.3 [3] 6.5.3 |  |  | O |  |  |
| 18a |  |  | Enhanced Data Rate eSCO (3 Mb/s mode) |  |  | [1] 3.3 [3] 6.5.3 |  |  | C.20 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 19a |  |  | Simple Pairing Updates |  |  | [4] [5] 3.3, 4.2.7.4 |  |  | M |  |  |
| 19b |  |  | Secure Simple Pairing (Controller Support) |  |  | [1] 3.3, 4.2.7 |  |  | M |  |  |
| 20 |  |  | Enhanced Power Control |  |  | [1] 3.3, 4.1.3.1 |  |  | C.6 |  |  |
| 21 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 22 |  |  | LE Supported (Controller) |  |  | [1] 3.3 |  |  | C.4 |  |  |
| 23 |  |  | LE and BR/EDR to same device capable (Controller) |  |  | [1] 3.3 |  |  | C.12 |  |  |
| 24– 25 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 26 |  |  | Secure Connections (Controller Support) |  |  | [1] 3.3, 4.2.7 |  |  | C.9 |  |  |
| 26a |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 27 |  |  | Ping |  |  | [1] 3.3, 4.1.13 |  |  | O |  |  |
| 28 |  |  | Coarse Clock Adjustment |  |  | [1] 3.3, 4.1.14 |  |  | C.15 |  |  |
| 29 |  |  | Slot Availability Mask |  |  | [1] 3.3, 4.1.15 |  |  | O |  |  |
| 30 |  |  | Paging Parameter Negotiation |  |  | [1] 3.3, 4.1.9 |  |  | O |  |  |

C.1: Mandatory IF RF 1/1 “Power Class 1”, otherwise Optional.
C.2–C.3: No longer used.
C.4: Mandatory IF CORE 10/12 “Link Layer (LL)”, otherwise Excluded.
C.5: Optional IF LMP 2/4 “Slot offset”, otherwise Excluded.
C.6: Optional IF LMP 2/10 “Power Control” AND LMP 2/13a “Power Control Requests”, otherwise Excluded.
C.7–C.8: No longer used.
C.9: Optional IF LMP 2/3 “Encryption” AND LMP 2/27 “Ping” AND LMP 6/10 “Encryption Pause/Resume”, otherwise Excluded.
C.10–C.11: No longer used.
C.12: Optional IF LMP 2/22 “LE Supported (Controller)”, otherwise Excluded.
C.13–C.14: No longer used.
C.15: Optional IF LMP 26/1 “Support of AFH switch as Central” AND LMP 26/2 “Support of AFH switch as Peripheral” AND LMP 2a/130 “Synchronization Train” AND LMP 2a/131 “Synchronization Scan” AND NOT LMP 2/14 “Broadcast encryption”, otherwise Excluded.
C.16–C.17: No longer used.
C.18: Excluded IF LMP 2/28 “Coarse Clock Adjustment”, otherwise Optional IF LMP 2/3 “Encryption”, otherwise Excluded.
C.19: Optional IF LMP 2/17 “Enhanced Data Rate ACL (2 Mb/s mode)”, otherwise Excluded.
C.20: Optional IF LMP 2/18 “Enhanced Data Rate eSCO (2 Mb/s mode)”, otherwise Excluded.
C.21: Optional IF CORE 1/42 “Controller Core v4.2”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | HV2 packets |  |  | [1] 3.3 [3] 6.5.2.2 |  |  | C.12 |  |  |
| 13 |  |  | HV3 packets |  |  | [1] 3.3 [3] 6.5.2.3 |  |  | C.12 |  |  |
| 14 |  |  | µ-law log synchronous data |  |  | [1] 3.3 [3] 9.1 |  |  | C.14 |  |  |
| 15 |  |  | A-law log synchronous data |  |  | [1] 3.3 [3] 9.1 |  |  | C.14 |  |  |
| 16 |  |  | CVSD synchronous data |  |  | [1] 3.3 [3] 9.2 |  |  | C.14 |  |  |
| 19 |  |  | Transparent synchronous data |  |  | [1] 3.3 [3] 6.4.3 |  |  | C.14 |  |  |
| 28 |  |  | Interlaced inquiry scan |  |  | [1] 3.3 [3] 8.4.1 |  |  | O |  |  |
| 29 |  |  | Interlaced page scan |  |  | [1] 3.3 [3] 8.3.1 |  |  | O |  |  |
| 32 |  |  | EV4 packets |  |  | [1] 3.3 [3] 6.5.3.2 |  |  | C.32 |  |  |
| 33 |  |  | EV5 packets |  |  | [1] 3.3 [3] 6.5.3.3 |  |  | C.32 |  |  |
| 39 |  |  | 3-slot Enhanced Data Rate ACL packets |  |  | [1] 3.3 [3] 4.1.10 |  |  | C.39 |  |  |
| 40 |  |  | 5-slot Enhanced Data Rate ACL packets |  |  | [1] 3.3 [3] 4.1.10 |  |  | C.39 |  |  |
| 47 |  |  | 3-slot Enhanced Data Rate eSCO packets |  |  | [1] 3.3 [3] 4.1.10 |  |  | C.47 |  |  |
| 48 |  |  | Extended Inquiry Response |  |  | [1] 3.3 |  |  | C.48 |  |  |
| 52 |  |  | Encapsulated PDU |  |  | [1] 3.3, 4.1.12.1 |  |  | M |  |  |
| 53 |  |  | Erroneous Data Reporting |  |  | [1] 3.3 |  |  | C.53 |  |  |
| 54 |  |  | Non-flushable Packet Boundary Flag |  |  | [1] 3.3 |  |  | O |  |  |
| 56 |  |  | Link Supervision Timeout Changed event |  |  | [1] 3.3 [7] 7.7.46 |  |  | C.56 |  |  |
| 57 |  |  | Variable Inquiry TX Power Level |  |  | [1] 3.3 |  |  | O |  |  |
| 128 |  |  | Connectionless Peripheral Broadcast - Central Operation |  |  | [1] 3.3 |  |  | C.128 |  |  |
| 129 |  |  | Connectionless Peripheral Broadcast - Peripheral Operation |  |  | [1] 3.3 |  |  | C.129 |  |  |
| 130 |  |  | Synchronization Train |  |  | [1] 3.3 |  |  | O |  |  |
| 131 |  |  | Synchronization Scan |  |  | [1] 3.3 |  |  | O |  |  |
| 132 |  |  | Inquiry Response Notification event |  |  | [1] 3.3 [7] 7.7.74 |  |  | C.132 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 133 |  |  | Generalized interlaced scan |  |  | [1] 3.3 [3] 8.3.1, 8.4.1 |  |  | C.133 |  |  |
| 139 |  |  | Train nudging |  |  | [1] 3.3 [3] 8.3.2, 8.4.1 |  |  | O |  |  |

C.12: Optional IF LMP 2/12 “SCO link”, otherwise Excluded.
C.14: Optional IF LMP 2/12 “SCO link” OR LMP 2/15 “eSCO link”, otherwise Excluded.
C.32: Optional IF LMP 2/15 “eSCO link”, otherwise Excluded.
C.39: Optional IF LMP 2/17 “Enhanced Data Rate ACL (2 Mb/s mode)”, otherwise Excluded.
C.47: Optional IF LMP 2/18 “Enhanced Data Rate eSCO (2 Mb/s mode)”, otherwise Excluded.
C.48: Optional IF LMP 2/13 “RSSI with inquiry results”, otherwise Excluded.
C.53: Mandatory IF (LMP 2/12 “SCO link” OR LMP 2/15 “eSCO link”) AND HCI 9/8 “Write Default Erroneous Data Reporting command”, otherwise Excluded.
C.56: Mandatory IF HCI 13/7 “Link Supervision Timeout Changed event”, otherwise Excluded.
C.128: Optional IF LMP 2a/130 “Synchronization Train”, otherwise Excluded.
C.129: Optional IF LMP 2a/131 “Synchronization Scan”, otherwise Excluded.
C.132: Mandatory IF HCI 6/23 “Inquiry Response Notification event”, otherwise Excluded.
C.133: Optional IF (LMP 2a/28 “Interlaced inquiry scan” OR LMP 2a/29 “Interlaced page scan”),
otherwise Excluded.
Table 2b: EDR Features

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | EDR for asynchronous transports (single slot) |  |  | [2] 3.2 |  |  | C.1, C.4 |  |  |
| 2 |  |  | EDR for asynchronous transports (multi-slot) |  |  | [2] 3.2 |  |  | C.2, C.4 |  |  |
| 3 |  |  | EDR for synchronous transports (Core 3.0 or later) |  |  | [2] 3.2 |  |  | C.3, C.4 |  |  |

C.1: Mandatory IF LMP 2/17 “Enhanced Data Rate ACL (2 Mb/s mode)”, otherwise Excluded.
C.2: Mandatory IF LMP 2a/39 “3-slot Enhanced Data Rate ACL packets”, otherwise Excluded.
C.3: Mandatory IF LMP 2/18 “Enhanced Data Rate eSCO (2 Mb/s mode)”, otherwise Excluded.
C.4: Mandatory to support at least one IF CORE 30/4 “HS Core-Controller Configuration” OR CORE 30/5 “HS/LE Core-Controller Configuration”, otherwise Optional.

#### 1.2.3 Authentication

Table 3: Authentication

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate authentication before connection completed |  |  | [1] 4.2.1 |  |  | O |  |  |
| 2 |  |  | Initiate authentication after connection completed |  |  | [1] 4.2.1 |  |  | O |  |  |
| 3 |  |  | Respond to authentication request |  |  | [1] 4.2.1 |  |  | M |  |  |


#### 1.2.4 Pairing

Table 4: Pairing

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate pairing before connection completed |  |  | [1] 4.4.2 |  |  | O |  |  |
| 2 |  |  | Initiate pairing after connection completed |  |  | [1] 4.4.2 |  |  | O |  |  |
| 3 |  |  | Respond to pairing request |  |  | [1] 4.2.2.1, 4.2.2.3 |  |  | M |  |  |
| 4 |  |  | Use fixed PIN and request responder to initiator switch |  |  | [1] 4.2.2.2 |  |  | C.1 |  |  |
| 5 |  |  | Use variable PIN |  |  | [1] 4.2.2.2 |  |  | C.1 |  |  |
| 6 |  |  | Accept initiator to responder switch |  |  | [1] 4.2.2.2 |  |  | C.2 |  |  |
| 7 |  |  | TSPC Change of IO Capabilities _ _ _ _ |  |  | [1] 4.2.7.3.4 |  |  | M |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF LMP 4/5 “Use variable PIN” AND (LMP 4/1 “Initiate pairing before connection completed” OR LMP 4/2 “Initiate pairing after connection completed”), otherwise Optional.
C.3: No longer used.

#### 1.2.5 Link Keys

Table 5: Link Keys

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 2 |  |  | Creation of link key - Combination Key |  |  | [1] 4.2.2.4 |  |  | M |  |  |
| 3 |  |  | Initiate change of link key |  |  | [1] 4.2.3 |  |  | O |  |  |
| 4 |  |  | Accept change of link key |  |  | [1] 4.2.3 |  |  | M |  |  |
| 5–7 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 8 |  |  | Support for 7 bytes or longer encryption key size |  |  | [1] 4.2.5.2 |  |  | M |  |  |


#### 1.2.6 Encryption

Table 6: Encryption
Prerequisite: LMP 2/3 “Encryption”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate encryption |  |  | [1] 4.2.5.1 |  |  | M |  |  |
| 2 |  |  | Accept encryption requests |  |  | [1] 4.2.5.1 |  |  | M |  |  |
| 3–4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 5 |  |  | Key size negotiation |  |  | [1] 4.2.5.2 |  |  | M |  |  |
| 6 |  |  | Start encryption, as Central |  |  | [1] 4.2.5.3 |  |  | M |  |  |
| 7 |  |  | Accept start of encryption |  |  | [1] 4.2.5.3 |  |  | M |  |  |
| 8 |  |  | Stop encryption, as Central |  |  | [1] 4.2.5.4 |  |  | M |  |  |
| 9 |  |  | Accept stop of encryption |  |  | [1] 4.2.5.4 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 |  |  | Encryption Pause/Resume |  |  | [1] 4.2.5.3 |  |  | M |  |  |
| 11 |  |  | AES CCM Encryption |  |  | [1] 4.2.5 |  |  | C.3 |  |  |

C.1–C.2: No longer used.
C.3: Mandatory IF LMP 2/26 “Secure Connections (Controller Support)”, otherwise Excluded.

#### 1.2.7 Information Requests

Table 7: Clock Offset Information

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request clock offset information |  |  | [1] 4.3.2 |  |  | M |  |  |
| 2 |  |  | Respond to clock offset requests |  |  | [1] 4.3.2 |  |  | M |  |  |

Table 8: Slot Offset Information
Prerequisite: LMP 2/4 “Slot offset”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Send slot offset information |  |  | [1] 4.4.1 |  |  | C.1 |  |  |

C.1: Mandatory IF LMP 13/1 “Request role switch”, otherwise Optional.
Table 9: Timing Accuracy Information
Prerequisite: LMP 2/5 “Timing accuracy”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request timing accuracy information |  |  | [1] 4.3.1 |  |  | O |  |  |
| 2 |  |  | Respond to timing accuracy information requests |  |  | [1] 4.3.1 |  |  | M |  |  |

Table 10: LM Version Information

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request LM version information |  |  | [1] 4.3.3 |  |  | O |  |  |
| 2 |  |  | Respond to LM version information requests |  |  | [1] 4.3.3 |  |  | M |  |  |

Table 11: Feature Support

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request supported features |  |  | [1] 4.3.4 |  |  | M |  |  |
| 2 |  |  | Respond to supported features requests |  |  | [1] 4.3.4 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Request extended features mask |  |  | [1] 4.3.4 |  |  | C.2 |  |  |
| 4 |  |  | Respond to extended features request |  |  | [1] 4.3.4 |  |  | C.2 |  |  |

C.1: No longer used.
C.2: Mandatory IF LMP 2a/128 “Connectionless Peripheral Broadcast - Central Operation” OR LMP 2a/129 “Connectionless Peripheral Broadcast - Peripheral Operation” OR LMP 2a/130 “Synchronization Train” OR LMP 2a/131 “Synchronization Scan” OR LMP 2a/132 “Inquiry Response Notification event” OR LMP 2a/133 “Generalized interlaced scan” OR LMP 2/28 “Coarse Clock Adjustment” OR LMP 2/26 “Secure Connections (Controller Support)” OR LMP 2/27 “Ping” OR LMP 2/29 “Slot Availability Mask” OR LMP 2a/139 “Train nudging”, otherwise Optional. Note: Mandatory IF a feature requiring another features page (a feature with an LMP feature number greater than 63 in Table 3.1: Mapping of LMP Feature Bits to ICS Items), other than Host features, is supported, otherwise Optional.
Table 12: Name Information

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request name information |  |  | [1] 4.3.5 |  |  | M |  |  |
| 2 |  |  | Respond to name requests |  |  | [1] 4.3.5 |  |  | M |  |  |


#### 1.2.8 Link Handling

Table 13: Role Switch
Prerequisite: LMP 2/6 “Role switch”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request role switch |  |  | [1] 4.4.2 |  |  | O |  |  |
| 2 |  |  | Accept role switch requests |  |  | [1] 4.4.2 |  |  | M |  |  |

Table 14: Detach

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Detach connection |  |  | [1] 4.1.2 |  |  | M |  |  |

Table 14a: Setting up and Removing Enhanced Date Rate ACL Connection

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Enter Enhanced Data Rate |  |  | [1] 4.1.11 |  |  | C.1 |  |  |
| 2 |  |  | Exit Enhanced Data Rate |  |  | [1] 4.1.11 |  |  | C.1 |  |  |

C.1: Mandatory IF LMP 2/17 “Enhanced Data Rate ACL (2 Mb/s mode)”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Enter and exit eSCO using Enhanced Data Rate Packets |  |  | [1] 4.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF LMP 2/18 “Enhanced Data Rate eSCO (2 Mb/s mode)”, otherwise Excluded.
Table 15: Hold Mode
Prerequisite: LMP 2/7 “Hold mode”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Force hold mode |  |  | [1] 4.5.1, 4.5.1.2 |  |  | O |  |  |
| 2 |  |  | Request hold mode |  |  | [1] 4.5.1, 4.5.1.3 |  |  | C.1 |  |  |
| 3 |  |  | Respond to hold mode requests |  |  | [1] 4.5.1, 4.5.1.3 |  |  | M |  |  |
| 4 |  |  | Accept forced hold mode |  |  | [1] 4.5.1, 4.5.1.2 |  |  | M |  |  |

C.1: Mandatory IF LMP 15/1 “Force hold mode”, otherwise Optional.
Table 16: Sniff Mode
Prerequisite: LMP 2/8 “Sniff mode”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 2 |  |  | Request sniff mode |  |  | [1] 4.5.3, 4.5.3.2 |  |  | O |  |  |
| 3 |  |  | Respond to sniff mode requests (renegotiate or reject) |  |  | [1] 4.5.3.2 |  |  | M |  |  |
| 4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 5 |  |  | Request un-sniff |  |  | [1] 4.5.3.2 |  |  | C.1 |  |  |
| 6 |  |  | Accept un-sniff requests |  |  | [1] 4.5.3.2 |  |  | M |  |  |
| 7 |  |  | Sniff Subrating Mode |  |  | [1] 4.5.3.2 |  |  | M |  |  |

C.1: Mandatory IF LMP 16/2 “Request sniff mode”, otherwise Optional.
Table 17: No longer used
Table 18: Power Control

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request to Increase Power |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 2 |  |  | Request to Decrease Power |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 3 |  |  | Respond when max power reached |  |  | [1] 4.1.3 |  |  | C.2 |  |  |
| 4 |  |  | Respond when min power reached |  |  | [1] 4.1.3 |  |  | C.2 |  |  |
| 5 |  |  | Request to increment power a single step |  |  | [1] 4.1.3.1.1 |  |  | C.3 |  |  |
| 6 |  |  | Request to decrease power a single step |  |  | [1] 4.1.3.1.1 |  |  | C.3 |  |  |
| 7 |  |  | Request to go to max power |  |  | [1] 4.1.3.1.1 |  |  | C.3 |  |  |
| 8 |  |  | Respond to increment power a single step |  |  | [1] 4.1.3.1.2 |  |  | C.3 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 |  |  | Respond to decrease power a single step |  |  | [1] 4.1.3.1.2 |  |  | C.3 |  |  |
| 10 |  |  | Respond to go to max power |  |  | [1] 4.1.3.1.2 |  |  | C.3 |  |  |

C.1: Mandatory IF LMP 2/13a “Power Control Requests”, otherwise Excluded.
C.2: Mandatory IF LMP 2/10 “Power Control”, otherwise Excluded.
C.3: Mandatory IF LMP 2/20 “Enhanced Power Control”, otherwise Excluded.
Table 19: Link Supervision Timeout

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Set link supervision timeout value |  |  | [1] 4.1.6 |  |  | O |  |  |
| 2 |  |  | Accept link supervision timeout setting |  |  | [1] 4.1.6 |  |  | M |  |  |


#### 1.2.9 Quality of Service

Table 20: Quality of Service

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Channel quality driven change between DM and DH packet types |  |  | [1] 4.1.7 |  |  | C.1 |  |  |
| 2 |  |  | Force/Request change of Quality of Service |  |  | [1] 4.1.8, 4.1.8.1 |  |  | M |  |  |
| 3 |  |  | Request change of Quality of Service |  |  | [1] 4.1.8, 4.1.8.2 |  |  | M |  |  |

C.1: Mandatory IF LMP 2/11 “Channel quality driven data rate”, otherwise Optional.
Table 21: No longer used

#### 1.2.10 Multi-Slot Packets

Table 22: Multi-Slot Packets

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Accept maximum allowed number of slots to be used |  |  | [1] 4.1.10 |  |  | C.1 |  |  |
| 2 |  |  | Request maximum number of slots to be used |  |  | [1] 4.1.10 |  |  | C.1 |  |  |
| 3 |  |  | Accept request of maximum number of slots to be used |  |  | [1] 4.1.10 |  |  | C.1 |  |  |

C.1: Mandatory IF LMP 2/1 “3-slot packets” OR LMP 2/2 “5-slot packets”, otherwise Optional.

#### 1.2.11 Paging Scheme

Table 23: Paging Scheme
Prerequisite: LMP 2/30 “Paging Parameter Negotiation”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Request page mode to use |  |  | [1] 4.1.9, 4.1.9.1 |  |  | M |  |  |
| 2 |  |  | Accept suggested page mode |  |  | [1] 4.1.9, 4.1.9.1 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Request page scan mode to use |  |  | [1] 4.1.9, 4.1.9.2 |  |  | M |  |  |
| 4 |  |  | Accept suggested page scan mode |  |  | [1] 4.1.9, 4.1.9.2 |  |  | M |  |  |


#### 1.2.12 Connection Establishment

Table 24: Connection Establishment

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Create connection for higher layers |  |  | [1] 4.1.1 |  |  | M |  |  |
| 2 |  |  | Respond to requests to establish connections for higher layers |  |  | [1] 4.1.1 |  |  | M |  |  |
| 3 |  |  | Indicate that link set-up is completed |  |  | [1] 4.1.1 |  |  | M |  |  |


#### 1.2.13 Test Mode

Table 25: Test Mode

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Activate test mode |  |  | [1] 4.7.1 |  |  | O |  |  |
| 2 |  |  | Ability to reject activation of test mode if test mode is disabled |  |  | [1] 4.7.1 |  |  | M |  |  |
| 3 |  |  | Control test mode |  |  | [1] 4.7.2 |  |  | O |  |  |
| 4 |  |  | Ability to reject test mode control commands if test mode is disabled |  |  | [1] 4.7.2 |  |  | M |  |  |

Table 26: Adaptive Frequency Hopping

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Support of AFH switch as Central |  |  | [1] 4.1.4 |  |  | O |  |  |
| 2 |  |  | Support of AFH switch as Peripheral |  |  | [1] 4.1.4 |  |  | O |  |  |
| 3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 4 |  |  | Support of Channel Classification reporting as Peripheral |  |  | [1] 4.1.5 |  |  | C.2 |  |  |
| 4a |  |  | Support of Channel Classification reporting as Central |  |  | [1] 4.1.5 |  |  | C.4 |  |  |
| 5 |  |  | Support channel classification from host |  |  | [1] 4.1.5 |  |  | C.3 |  |  |
| 6 |  |  | Support of Channel Classification |  |  | [1] 4.1.5 |  |  | O |  |  |

C.1: No longer used.
C.2: Optional IF LMP 26/2 “Support of AFH switch as Peripheral”, otherwise Excluded.
C.3: Mandatory IF LMP 26/1 “Support of AFH switch as Central” OR LMP 26/4 “Support of Channel Classification reporting as Peripheral”, otherwise Optional.
C.4: Optional IF LMP 26/1 “Support of AFH switch as Central”, otherwise Excluded.

#### 1.2.14 Ping

Table 27: Ping
Prerequisite: LMP 2/27 “Ping”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate LMP Ping |  |  | [1] 4.1.13 |  |  | O |  |  |
| 2 |  |  | Respond to LMP Ping |  |  | [1] 4.1.13 |  |  | M |  |  |


#### 1.2.15 Piconet Clock Adjust

Table 28: Coarse Clock Adjustment
Prerequisite: LMP 2/28 “Coarse Clock Adjustment”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Receive Request for Coarse Clock Adjustment |  |  | [1] 4.1.14.1 |  |  | O |  |  |
| 2 |  |  | Send Request for Coarse Clock Adjustment |  |  | [1] 4.1.14.1 |  |  | O |  |  |


#### 1.2.16 Slot Availability Mask

Table 29: Slot Availability Mask
Prerequisite: LMP 2/29 “Slot Availability Mask”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate SAM negotiations |  |  | [1] 4.1.15 |  |  | O |  |  |
| 2 |  |  | Respond to SAM negotiations |  |  | [1] 4.1.15 |  |  | M |  |  |


#### 1.2.17 Inter-layer Requirements

Table 30: BB Requirements

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 0a | DM3 packet type | [3] 6.5.4.3 | C.0 | [6] BB 5/2 |  |  |
| 0b | DH3 packet type | [3] 6.5.4.4 | C.0 | [6] BB 5/3 |  |  |
| 1a | DM5 packet type | [3] 6.5.4.5 | C.1 | [6] BB 5/4 |  |  |
| 1b | DH5 packet type | [3] 6.5.4.6 | C.1 | [6] BB 5/5 |  |  |
| 11 | SCO link | [3] 4.5.1.2, 8.6.2 | C.11 | [6] BB 2/2 |  |  |
| 12 | HV2 packet type | [3] 6.5.2.2 | C.12 | [6] BB 6/2 |  |  |
| 13 | HV3 packet type | [3] 6.5.2.3 | C.13 | [6] BB 6/3 |  |  |
| 14 | µ-law | [3] 9.1 | C.14 | [6] BB 13/2 |  |  |
| 15 | A-law | [3] 9.1 | C.15 | [6] BB 13/1 |  |  |
| 16 | CVSD | [3] 9.2 | C.16 | [6] BB 13/3 |  |  |
| 19 | Transparent Synchronous Data | [3] 6.4.3 | C.19 | [6] BB 13/4 |  |  |
| 25 | 2-DH1 packet type | [3] 6.5.4.8 | C.25 | [6] BB 5a/1 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 26 | 3-DH1 packet type | [3] 6.5.4.11 | C.26 | [6] BB 5a/4 |  |  |
| 28 | Interlaced Scan during Inquiry Scan | [3] 8.4.1 | C.28 | [6] BB 10/6 |  |  |
| 29 | Interlaced Scan during Page Scan | [3] 8.3.1 | C.29 | [6] BB 7/5 |  |  |
| 31 | eSCO link | [3] 4.5.1.4, 8.6.3 | C.31 | [6] BB 2/3 |  |  |
| 32 | EV4 packet type | [3] 6.5.3.2 | C.32 | [6] BB 6/6 |  |  |
| 33 | EV5 packet type | [3] 6.5.3.3 | C.33 | [6] BB 6/7 |  |  |
| 39 | 2-DH3 packet type | [3] 6.5.4.9 | C.39 | [6] BB 5a/2 |  |  |
| 40 | 2-DH5 packet type | [3] 6.5.4.13 | C.40 | [6] BB 5a/3 |  |  |
| 45 | 2-EV3 packet type | [3] 6.5.3.4 | C.45 | [6] BB 6a/1 |  |  |
| 46 | 3-EV3 packet type | [3] 6.5.3.6 | C.46 | [6] BB 6a/3 |  |  |
| 47a | 2-EV5 packet type | [3] 6.5.3.5 | C.47 | [6] BB 6a/2 |  |  |
| 47b | 3-EV5 packet type | [3] 6.5.3.7 | C.47 | [6] BB 6a/4 |  |  |
| 48 | Extended Inquiry Response | [3] 8.4.3 | C.48 | [6] BB 10/7 |  |  |
| 54 | Non-flushable Packet Boundary Flag | [3] 7.6.3 | C.54 | [6] BB 16/1 |  |  |
| 128 | Connectionless Peripheral Broadcast Transmitter | [3] 8.10.1 | C.128 | [6] BB 3a/1 |  |  |
| 129 | Connectionless Peripheral Broadcast Receiver | [3] 8.10.2 | C.129 | [6] BB 3a/2 |  |  |
| 130 | Synchronization Train | [3] 8.3.5 | C.130 | [6] BB 9c/1 |  |  |
| 131 | Synchronization Scan | [3] 8.3.4 | C.131 | [6] BB 9c/2 |  |  |
| 133a | Generalized Interlaced Page Scan | [3] 8.3.1 | C.133 | [6] BB 7/9 |  |  |
| 133b | Generalized Interlaced Inquiry Scan | [3] 8.4.1 | C.133 | [6] BB 10/9 |  |  |
| 134 | Coarse Clock Adjustment | [3] 8.6.10.1 | C.134 | [6] BB 18/1 |  |  |
| 138 | Slot Availability Mask | [3] 8.6.11 | C.138 | [6] BB 19/1 |  |  |
| 139a | Train Nudging During Page | [3] 8.3.2 | C.139 | [6] BB 7/8 |  |  |
| 139b | Train Nudging During Inquiry | [3] 8.4.2 | C.139 | [6] BB 10/8 |  |  |

C.0: Mandatory IF LMP 2/1 “3-slot packets”, otherwise not defined.
C.1: Mandatory IF LMP 2/2 “5-slot packets”, otherwise not defined.
C.11: Mandatory IF LMP 2/12 “SCO link”, otherwise not defined.
C.12: Mandatory IF LMP 2a/12 “HV2 packets”, otherwise not defined.
C.13: Mandatory IF LMP 2a/13 “HV3 packets”, otherwise not defined.
C.14: Mandatory IF LMP 2a/14 “µ-law log synchronous data”, otherwise not defined.
C.15: Mandatory IF LMP 2a/15 “A-law log synchronous data”, otherwise not defined.
C.16: Mandatory IF LMP 2a/16 “CVSD synchronous data”, otherwise not defined.
C.19: Mandatory IF LMP 2a/19 “Transparent synchronous data”, otherwise not defined.
C.25: Mandatory IF LMP 2/17 “Enhanced Data Rate ACL (2 Mb/s mode)”, otherwise not defined.
C.26: Mandatory IF LMP 2/17a “Enhanced Data Rate ACL (3 Mb/s mode)”, otherwise not defined.
C.28: Mandatory IF LMP 2a/28 “Interlaced inquiry scan”, otherwise not defined.
C.29: Mandatory IF LMP 2a/29 “Interlaced page scan”, otherwise not defined.
C.31: Mandatory IF LMP 2/15 “eSCO link”, otherwise not defined.
C.32: Mandatory IF LMP 2a/32 “EV4 packets”, otherwise not defined.
C.40: Mandatory IF LMP 2a/40 “5-slot Enhanced Data Rate ACL packets”, otherwise not defined.
C.45: Mandatory IF LMP 2/18 “Enhanced Data Rate eSCO (2 Mb/s mode)”, otherwise not defined.
C.46: Mandatory IF LMP 2/18a “Enhanced Data Rate eSCO (3 Mb/s mode)”, otherwise not defined.
C.47: Mandatory to support at least one IF LMP 2a/47 “3-slot Enhanced Data Rate eSCO packets”, otherwise not defined.
C.48: Mandatory IF LMP 2a/48 “Extended Inquiry Response”, otherwise not defined.
C.54: Mandatory IF LMP 2a/54 “Non-flushable Packet Boundary Flag”, otherwise not defined.
C.128: Mandatory IF LMP 2a/128 “Connectionless Peripheral Broadcast - Central Operation”, otherwise
not defined.
C.129: Mandatory IF LMP 2a/129 “Connectionless Peripheral Broadcast - Peripheral Operation”,
otherwise not defined.
C.130: Mandatory IF LMP 2a/130 “Synchronization Train”, otherwise not defined.
C.131: Mandatory IF LMP 2a/131 “Synchronization Scan”, otherwise not defined.
C.133: Mandatory to support at least one IF LMP 2a/133 “Generalized interlaced scan”, otherwise not
defined.
C.134: Mandatory IF LMP 2/28 “Coarse Clock Adjustment”, otherwise not defined.
C.138: Mandatory IF LMP 2/29 “Slot Availability Mask”, otherwise not defined.
C.139: Mandatory to support at least one IF LMP 2a/139 “Train nudging”, otherwise not defined.

## 2 References

[1] Specification of the Bluetooth System, Volume 2, Part C (LMP)
[2] Specification of the Bluetooth System, Volume 2, Part A (RF)
[3] Specification of the Bluetooth System, Volume 2, Part B (BB)
[4] Erratum 10734
[5] Specification of the Bluetooth System, Volume 2, Part C (LMP), Version 5.1 or later
[6] ICS Proforma for Base Band (BB)
[7] Specification of the Bluetooth System, Volume 4, Part E (HCI)

## 3 Mapping of LMP feature bits to ICS items

This section is informative.
Not all LMP features have corresponding ICS items.

|  | Feature |  |  | LMP Bit |  |  | ICS Item |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 slot packets |  |  | 0 |  |  | LMP 2/1 |  |  |
| 5 slot packets |  |  | 1 |  |  | LMP 2/2 |  |  |
| Encryption |  |  | 2 |  |  | LMP 2/3 |  |  |
| Slot offset |  |  | 3 |  |  | LMP 2/4 |  |  |
| Timing accuracy |  |  | 4 |  |  | LMP 2/5 |  |  |
| Role switch |  |  | 5 |  |  | LMP 2/6 |  |  |
| Hold mode |  |  | 6 |  |  | LMP 2/7 |  |  |
| Sniff mode |  |  | 7 |  |  | LMP 2/8 |  |  |
| Park |  |  | 8 |  |  | LMP 2/9 |  |  |
| Power control requests |  |  | 9 |  |  | LMP 2/13a |  |  |
| Channel quality driven data rate (CQDDR) |  |  | 10 |  |  | LMP 2/11 |  |  |
| SCO link |  |  | 11 |  |  | LMP 2/12 |  |  |
| HV2 packets |  |  | 12 |  |  | LMP 2a/12 |  |  |
| HV3 packets |  |  | 13 |  |  | LMP 2a/13 |  |  |
| µ-law log synchronous data |  |  | 14 |  |  | LMP 2a/14 |  |  |
| A-law log synchronous data |  |  | 15 |  |  | LMP 2a/15 |  |  |
| CVSD synchronous data |  |  | 16 |  |  | LMP 2a/16 |  |  |
| Paging parameter negotiation |  |  | 17 |  |  | LMP 2/30 |  |  |
| Power control |  |  | 18 |  |  | LMP 2/10 |  |  |
| Transparent synchronous data |  |  | 19 |  |  | LMP 2a/19 |  |  |
| Flow control lag (least significant bit) |  |  | 20 |  |  | See below |  |  |
| Flow control lag (middle bit) |  |  | 21 |  |  | See below |  |  |
| Flow control lag (most significant bit) |  |  | 22 |  |  | See below |  |  |
| Broadcast Encryption |  |  | 23 |  |  | LMP 2/14 |  |  |
| Enhanced Data Rate ACL 2 Mb/s mode |  |  | 25 |  |  | LMP 2/17 |  |  |
| Enhanced Data Rate ACL 3 Mb/s mode |  |  | 26 |  |  | LMP 2/17a |  |  |
| Enhanced inquiry scan |  |  | 27 |  |  | See below |  |  |
| Interlaced inquiry scan |  |  | 28 |  |  | LMP 2a/28 |  |  |
| Interlaced page scan |  |  | 29 |  |  | LMP 2a/29 |  |  |
| RSSI with inquiry results |  |  | 30 |  |  | LMP 2/13 |  |  |
| Extended SCO link (EV3 packets) |  |  | 31 |  |  | LMP 2/15 |  |  |
| EV4 packets |  |  | 32 |  |  | LMP 2a/32 |  |  |
| EV5 packets |  |  | 33 |  |  | LMP 2a/33 |  |  |
| AFH capable Peripheral |  |  | 35 |  |  | LMP 26/2 |  |  |
| AFH classification Peripheral |  |  | 36 |  |  | LMP 26/4 |  |  |
| No longer used |  |  | 37 |  |  | N/A |  |  |


|  | Feature |  |  | LMP Bit |  |  | ICS Item |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LE Supported (Controller) |  |  | 38 |  |  | LMP 2/22 |  |  |
| 3-slot Enhanced Data Rate ACL packets |  |  | 39 |  |  | LMP 2a/39 |  |  |
| 5-slot Enhanced Data Rate ACL packets |  |  | 40 |  |  | LMP 2a/40 |  |  |
| Sniff subrating |  |  | 41 |  |  | LMP 16/7 |  |  |
| Pause encryption |  |  | 42 |  |  | LMP 6/10 |  |  |
| AFH capable Central |  |  | 43 |  |  | LMP 26/1 |  |  |
| AFH classification Central |  |  | 44 |  |  | LMP 26/4a |  |  |
| Enhanced Data Rate eSCO 2 Mb/s mode |  |  | 45 |  |  | LMP 2/18 |  |  |
| Enhanced Data Rate eSCO 3 Mb/s mode |  |  | 46 |  |  | LMP 2/18a |  |  |
| 3-slot Enhanced Data Rate eSCO packets |  |  | 47 |  |  | LMP 2a/47 |  |  |
| Extended Inquiry Response |  |  | 48 |  |  | LMP 2a/48 |  |  |
| Simultaneous LE and BR/EDR to Same Device Capable (Controller) |  |  | 49 |  |  | LMP 2/23 |  |  |
| Secure Simple Pairing (Controller Support) |  |  | 51 |  |  | LMP 2/19b |  |  |
| Encapsulated PDU |  |  | 52 |  |  | LMP 2a/52 |  |  |
| Erroneous Data Reporting |  |  | 53 |  |  | LMP 2a/53 |  |  |
| Non-flushable Packet Boundary Flag |  |  | 54 |  |  | LMP 2a/54 |  |  |
| Link Supervision Timeout Changed event |  |  | 56 |  |  | LMP 2a/56 |  |  |
| Variable Inquiry TX Power Level |  |  | 57 |  |  | LMP 2a/57 |  |  |
| Enhanced Power Control |  |  | 58 |  |  | LMP 2/20 |  |  |
| Extended features |  |  | 63 |  |  | LMP 11/4 |  |  |
| Secure Simple Pairing (Host Support) |  |  | 64 |  |  | See below |  |  |
| LE Supported (Host) |  |  | 65 |  |  | See below |  |  |
| Simultaneous LE and BR/EDR to Same Device Capable (Host) |  |  | 66 |  |  | See below |  |  |
| Secure Connections (Host Support) |  |  | 67 |  |  | See below |  |  |
| Connectionless Peripheral Broadcast - Central Operation |  |  | 128 |  |  | LMP 2a/128 |  |  |
| Connectionless Peripheral Broadcast - Peripheral Operation |  |  | 129 |  |  | LMP 2a/129 |  |  |
| Synchronization Train |  |  | 130 |  |  | LMP 2a/130 |  |  |
| Synchronization Scan |  |  | 131 |  |  | LMP 2a/131 |  |  |
| Inquiry Response Notification event |  |  | 132 |  |  | LMP 2a/132 |  |  |
| Generalized interlaced scan |  |  | 133 |  |  | LMP 2a/133 |  |  |
| Coarse Clock Adjustment |  |  | 134 |  |  | LMP 2/28 |  |  |
| Secure Connections (Controller Support) |  |  | 136 |  |  | LMP 2/26 |  |  |
| Ping |  |  | 137 |  |  | LMP 2/27 |  |  |
| Slot Availability Mask |  |  | 138 |  |  | LMP 2/29 |  |  |
| Train nudging |  |  | 139 |  |  | LMP 2a/139 |  |  |

Table 3.1: Mapping of LMP feature bits to ICS items
Feature bits 64, 65, 66, and 67 are set at run-time by the Host; therefore, they do not have a corresponding ICS entry. Tests that check that feature masks match the ICS should ignore these bits.
Feature bits 20, 21, and 22 are the three bits corresponding to the Flow Control Lag. These bits should be ignored when testing the mask.
The value for Feature bit 27 is ignored when testing the mask.
The missing bit numbers are RFU and are 0 when testing the mask.

## 4 Bridge mapping between the SUM ICS and the

LMP ICS
Erratum 23556 removed Vol 0 Part B “Compliance” and Vol 1 Part D “Mixing Of Specification Versions” from the Core specification and replaced them with a new Vol 0 Part D “Core Configurations”.
The concepts of product types, as well as some conditions tied to specific core capabilities, were described in Vol 0 Part B “Compliance” and indicated by entries in the SUM ICS.
The withdrawal of the SUM ICS means that three ICS items for EDR capabilities (SUM ICS 22/1, SUM ICS 22/2, and SUM ICS 22/4) have been relocated to the LMP ICS. This means that implementations that previously selected these items in the SUM ICS will now need to select the corresponding items in the LMP ICS.
Table 4.1 provides the mapping between the LMP ICS and SUM ICS items. If an implementation previously supported one of the SUM ICS capabilities, then it now supports the corresponding LMP ICS capability.

| LMP ICS | Description |  | Past SUM ICS |  |
| --- | --- | --- | --- | --- |
|  |  |  | representation |  |
| LMP 2b/1 EDR for asynchronous transports (single slot) SUM ICS 22/1 LMP 2b/2 EDR for asynchronous transports (multi-slot) SUM ICS 22/2 LMP 2b/3 EDR for synchronous transports (Core 3.0 or later) SUM ICS 22/4 |  |  |  |  |

Table 4.1: Mapping between the LMP ICS and SUM ICS items

## 5 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | D5r3 |  |  | 2003-11-05 | Original Release |
|  |  |  | D10R00 |  |  | 2004-03-10 | Re-partitioned to match Main Specification Volume/Part partitioning. TSE 523, 524, 525, 545, and 547 incorporated. |
|  |  |  | D10r01 |  |  | 2004-03-11 | Editorial changes |
|  |  |  | D12r02 |  |  | 2004-03-23 | Editorial changes. Changed reference and document numbering to D12 to reflect applicable Bluetooth version. |
|  |  |  | D12r03 |  |  | 2004-03-25 | Editorial Changes |
| 10 |  |  | 1.2.2 |  |  | 2004-03-29 | Changed document number and revision number to conform to legacy system. Added Disclaimer and Copyright Notice. |
| 11 |  |  | 1.2.3 |  |  | 2004-06-21 | TSE 578 incorporated. |
|  |  |  | 2.0.E.0 Draft |  |  | 2004-10-22 | Incorporate Enhanced Data Rate Changes, affecting Tables 2, 14a, and 14b. |
| 12 |  |  | 2.0.E.0 |  |  | 2004-11-04 | First version for 1.2/2.0/2.0 + EDR available for qualification. |
|  |  |  | 2.0.E.1r1 |  |  | 2005-03-24 | Editorial and format changes. TSE 820: Added Table 8 heading |
| 13 |  |  | 2.0.E.1 |  |  | 2005-10-26 | Prepare for publication. |
| 14 |  |  | 2.1.E.0 |  |  | 2006-12-28 | Add line 7 to Table 16 for Sniff Subrating (but maybe not needed) Add line 10 to Table 6 for Encryption Pause Resume Update Table 2 and Table 6 for Simple Pairing feature Adjustment to previous Revision History document number. Adjustments to accommodate the introduction of mandatory/ optional settings for 2.1 features |
| 15 |  |  | 2.1.E.1 |  |  | 2007-07-31 | TSE 2113: Table 2: Change C.2 and C.3 TSE 2115: Table 26: Fix Prerequisite |
| 16 |  |  | 2.1.E.2 |  |  | 2008-04-29 | TSE 2438: Table 26/3: Update description Remove “Prepare for Publication” rows from table |
|  |  |  | 2.1.E.3r0 |  |  | 2009-02-12 | Add rows to Table 2.0 and add new table for EPC |
|  |  |  | 2.1.E.3r1 |  |  | 2009-03-25 | Removed SUM 21/9 as it does not exist Added SUM 21/8 to conditions where SUM 21/5 and SUM 21/6 were used Editorial – replaced 2-1 with 21 and 2-2 with 22. |
| 17 |  |  | 3.0.H.0/2.1.E. 3 |  |  | 2009-07-04 | Prepare for publication. |
| 18 |  |  | 3.0.H.1 |  |  | 2009-08-12 | TSE 2795: New condition for Item LMP:6/10 |
|  |  |  | 3.0.H.2r0 |  |  | 2009-10-6 | New PICS due to LMP Enhancements |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 3.0.H.2r1 |  |  | 2009-12-01 | Editorial review. Formatted table row height. Fixed Table 4 footnotes. Removed earlier Doc IDs from cover page. Updated title to include Tokyo. |
| 19 |  |  | 4.0.0r2-4.0.0 |  |  | 2009-12-15 | Updated document number. Prepare for publication. |
|  |  |  | 4.0.1r0 |  |  | 2011-01-27 | TSE 4220: Address legacy issues by adding “OR SUMMARY 21/9” to: Table 2: C2, C3, C4; Table 6: C1, C2;Table 16: C2 (TSE 3827) |
| 20 |  |  | 4.0.1 |  |  | 2011-07-18 | Prepare for publication. |
|  |  |  | 4.0.2r0 |  |  | 2011-11-07 | TSE 4228 Update Table 4 for ESR05 Erratum 2421. TSE 3857: Table 16, C.2—Check for sniff— Implemented in previous release; see TSE 4220. |
| 21 |  |  | 4.0.2 |  |  | 2012-30-12 | Prepare for publication. |
|  |  |  | 4.0.3r0 |  |  | 2012-05-16 | TSE 4765: Change 2/16 and 26/2 to O per core spec TSE 4597: Table 2, Footnotes C.2 and C.3 |
| 22 |  |  | 4.0.3 |  |  | 2012-07-24 | Prepare for publication. |
|  |  |  | 4.0.4rT |  |  | 2013-08-09 | Template Conversion |
|  |  |  | 4.0.4rTr3 |  |  | 2013-09-16 | Template Review Comment Resolution & Changes Accepted |
|  |  |  | 4.1.0r01 |  |  | 2013-09-16 | BR/EDR Secure Connections CR |
|  |  |  | 4.1.0r02 |  |  | 2013-10-09 | Piconet Clock Adjust CR |
| 23 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.1.1r00 |  |  | 2014-04-07 | TSE 5446: Removed prerequisite for Table 14, and updated items 18/1 and 18/2. |
| 24 |  |  | 4.1.1 |  |  | 2014-07-07 | TCRL 2014-1 Publication |
|  |  |  | 4.1.2r00 |  |  | 2014-11-06 | TSE 6081: Updated Table 2, C.4 to include “OR SUM ICS 21/13 (Core Specification 4.1)”. |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
| 25 |  |  | 4.2.0 |  |  | 2014-12-04 | Prepare for TCRL 2014-2 publication |
|  |  |  | 4.2.1r00 |  |  | 2016-03-02 | TSE 6593: Updated Table 2 Status column and conditional statements. Deleted Item 25. Added two new conditional statements. |
| 26 |  |  | 4.2.1 |  |  | 2016-07-07 | Prepared for TCRL 2016-1 Publication |
|  |  |  | 5.0.0r00 |  |  | 2016-07-08 | Integrated Core Slot Availability Masks CRr06 for Core Specification v5.0 release |
|  |  |  | 5.0.0r01 |  |  | 2016-08-30 | Issue 7534: Updated “TBD” references in Table 2 and 29. |
|  |  |  | 5.0.0r02 |  |  | 2016-10-05 | TSE 7448: In Table 2, C.8 and C.11 were duplicates. 2/28 remapped to C.11. C.8 repurposed for new conditional statement. 2/22 remapped to C.8. Updated blank items in Table 16 and 17. |
|  |  |  | 5.0.0r03 |  |  | 2016-10-13 | TSE 7215: “Packages” changed to “Packets” in the section heading and table title for Table 22. |
|  |  |  | 5.0.0r03 |  |  | 2016-11-11 | Issue 7884: Global edit. Added support in conditionals for Core Spec version 5.0. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.0.0r04 |  |  | 2016-11-14 | Update Template. Remove unnecessary paretheses. Replaced with quotation marks. TSE 8069: Revises C.6 in Table 2. Reversed the logic in Conditionals to address the issue of having to add in the next Core Version where it is to indicate “or later” (Table 2, C.4 and C.9; Table 6, C.1 and C.2; Table 16, C.2). |
| 27 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.0.1r00 |  |  | 2017-03-27 | TSE 8219: Added new conditional to Table 2 to exclude Park mode feature (LMP 2/9) for Bluetooth Core Specification v5.0 or later. |
|  |  |  | 5.0.1r01 |  |  | 2017-05-18 | Removal of Note preceding table 2. This note was found to be inconsistent with how items in table 2 are used (decision in BTI call 18th of May) |
| 28 |  |  | 5.0.1 |  |  | 2017-07-05 | Approved by BTI. Prepared for TCRL 2017-1 publication. |
|  |  |  | 5.0.2r00 |  |  | 2017-07-19 | TSE 7437: In C.2 and C.3 of Table 2: Supported Features, add LMP conditions for feature selection to reflect opportunity to optionally claim partial support of Core Configuration EDR, and change “Excluded” to “Optional”. |
| 29 |  |  | 5.0.2 |  |  | 2017-12-07 | Approved by BTI. Prepared for TCRL 2017-2 publication. |
|  |  |  | 5.0.3r00-01 |  |  | 2018-04-27 – 2018-05-10 | TSE 10614 (rating 2): Added new C.14 to Table 2 and changed status of 2/29 from O to C.14. TSE 10613 (rating 2): Added C.15 to Table 2 and changed status of item 2/28 from C.11 to C.15. Editorial fix to C.10 and added LMP prefix. |
| 30 |  |  | 5.0.3 |  |  | 2018-07-02 | Approved by BTI. Prepared for TCRL 2018-1 publication. |
|  |  |  | 5.0.4r00 |  |  | 2018-10-16 | TSE 10930 (rating 2): Removed items 5/1 and 5/7. Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1 Corrected conditional for Item 5/2 to M after removal of 5/1. |
|  |  |  | 5.1.0r00-r01 |  |  | 2018-11-13 – 2018-12-07 | Updated revision number from 5.0.4 to 5.1.0 to align with the adoption of Core Specification version 5.1. Corrected conditional for Item 5/2 to M after removal of 5/1. |
| 31 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | 5.1.1r00–r02 |  |  | 2019-04-02– 2019-08-14 | TSE 11296 (rating 3): Removed item 2/9 and all of Table 17 due to deprecation of the Park Mode feature. |
| 32 |  |  | 5.1.1 |  |  | 2019-08-01 | Approved by BTI. Prepared for TCRL 2019-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p33r00–r03 |  |  | 2019-10-03 – 2019-12-03 | TSE 12761 (rating 2): Added LMP item 2/19a for Erratum 10734 pairing updates and added that erratum and “Specification of the Bluetooth System, Volume 2, Part C, Version 5.1 or later” to the References section. TSE 12606 (rating 2): Removed references to deprecated and/or withdrawn core specs in conditionals by updating C.3 - C.6 and C.9 for Table 2, updating the status of items 1 and 10 and deleting C.1 and C.2 for Table 6, and updating the status of item 7 and deleting C.2 for Table 16; removed multiple table prerequisites, created conditionals C.1-C.4 to replace the removed prerequisites, and updated the status of items 1 - 10 for Table 18 (concatenated all rows into a cohesive table); removed reference to ESR05 by deleting C.3 and updating status of item 7 for Table 4. TSE 13025 (rating 3): Added item 26b and conditional note C.17 to Table 2; also added “(Controller Support)” to item 26 and “(Host Support)” to item 19. Revised document numbering convention, setting last release publication of 5.1.1 as p32; added publication number column to Revision History. Updated Contributors list. |
| 33 |  |  | p33 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p34r00–r11 |  |  | 2020-03-04 – 2021-06-10 | TSE 12735 (rating 2): Removed item 2/16 “Adaptive frequency hopping” as a single selectable item and instead use Table 26 items for better clarity. Cleaned up conditionals and prerequisites that referenced 2/16. Added item LMP 2/13a “Power Control Requests”. Revised conditionals for LMP 2/21 “BR/EDR Not Supported” and LMP 2/27 “Ping”. Fixed Table 2 conditionals. Revised conditional for LMP 11/1 “Request supported features”. Revised conditional C1 of Table 18. Revised conditional applied to LMP 18/7 “Request to go to max power”. Added item LMP 26/4a “Support of Channel Classification reporting as Central”. Removed item LMP 26/3 “Support of Channel Classification reporting — post Role Switch (as Slave)”. Corrections to Table 26 conditionals. Added informative Section 3 “Mapping of LMP feature bits to ICS items”. Revised Table 11 conditional C.2 to refer to the new LMP Feature Bits table. TSE 13061 (rating 3): In Table 2, added items 17a and 18a, modified items 17 and 18, updated conditionals C.2 and C.3, and added conditionals C.19 and C.20. TSE 13586 (rating 2): Revised conditionals for items LMP 2/14 “Broadcast Encryption” and LMP 2/28 “Coarse Clock Adjustment” to show that they are mutually exclusive features. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 14935 (rating 3): Added item LMP 2/30 “Paging Parameter Negotiation”. Made LMP 2/30 a prerequisite for Table 23. Updated all conditionals of Table 23 to M. TSE 14942 (rating 3): Added ICS item LMP 2/19b “Secure Simple Pairing (Controller Support)” and updated all relevant conditionals that should reference Secure Simple Pairing (Controller Support) to LMP 2/19b. TSE 15092 (rating 2): Changed items LMP 2/19 and LMP 2/24 to “No Longer Used”; updated Status for LMP 2/19a; deleted conditionals C.7, C.16, and C.21 (added temporarily for TSE 14942); updated conditional C.17. TSE 15175 (rating 2): Updated status of 12/1 to Mandatory. TSE 15488 (rating 1): To address Erratum 15334, globally changed “Master/Slave” language as it relates to role switches. TSE 15452 (rating 1): To address Erratum 15352, globally changed “Master” to “Central” and “Slave” to “Peripheral”. Incorporated Host To Controller Encryption Key Control _ _ _ _ _ _ Enhancements TEST CR r06: Added Table 5 item 8 _ _ _ and related conditional for “Support for 7 bytes or longer encryption key size”. Template-related and consistency checker editorials. |
| 34 |  |  | p34 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |
|  |  |  | p35r00 |  |  | 2022-04-04 – 2022-04-05 | TSE 18364 (rating 1): Updated C.1 – C.6, C.8, C.9, C.11 – C.15, and C.17 – C.20 for Table 2; C.2 for Table 4; C.1 for Table 5; C.3 for Table 6; C.1 for Table 8; C.1 for Table 14a; C.1 for Table 14b; C.1 for Table 15; C.1 for Table 16; C.1 – C.3 for Table 18; C.1 for Table 20; C.1 – C.4 for Table 21; C.1 for Table 22; and C.2 – C.4 for Table 26. TSE 18406 (rating 2): Updated the status for Table 5 item 8, deleted C.1 for Table 5, and added detail to the revision history for p34r00–r11 (per BTI). Performed template-related formatting fixes. Updated copyright page to align with v2 of the DNMD. |
| 35 |  |  | p35 |  |  | 2022-06-28 | Approved by BTI on 2022-05-31. Prepared for TCRL 2022-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p36r00–r02 |  |  | 2023-04-05 – 2023-05-26 | TSE 22388 (rating 3): Per E22262, removed the 2/21 entry for BR/EDR Not Supported, adjusted all conditionals that referenced it (modified C.1, C.2, C.3, C.5, C.6, C.9, C.12, C.14, C.15, C.18, C.19, and C.20 and deleted C.4, C.8, C.11, and C.13), and revised statuses accordingly for 2/1, 2/2, 2/3, 2/4, 2/5, 2/7, 2/8, 2/11, 2/12, 2/13, 2/13a, 2/15, 2/19a, 2/19b, 2/22, and 2/27. Editorial cleanup of “No longer used” throughout document to align with the latest ICS conventions. Removed Appropriate Language doc reference per the latest ICS conventions. |
| 36 |  |  | p36 |  |  | 2023-06-29 | Approved by BTI on 2023-06-05. Prepared for TCRL 2023-1 publication. |
|  |  |  | p37r00–r06 |  |  | 2023-09-26 – 2023-11-20 | TSE 22165 (rating 2): Added new reference items to cover the BB ICS, HCI ICS, and Core spec Vol 4 Part E. Added 2/9 back in with associated update to reference and status (new conditional C.21) and added new items 2/31 and 2/32. Added new Tables 30 and 31. Updated BB and HCI ICS Items in the “Mapping LMP feature bits to ICS items” table, and added new LMP items as necessary. TSE 24076 (rating 2): Replaced SUM ICS references. Updated Table 2 conditionals C.2 and C.3 (affecting 2/17 and 2/18) and added new Table 2b for EDR Features. TSE 24180 (rating 2): Added a new section to indicate bridge mapping between the old SUM ICS and new LMP ICS items. Replaced the LMP ICS reference with the BB ICS in the references column per query responses 998513 and 998549. Updated the document to align with the latest standards. |
| 37 |  |  | p37 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p38r00–r01 |  |  | 2024-07-11 – 2024-07-17 | TSE 25027 (rating 1): Set 2/26a and related conditional C.17 to “No longer used”. TSE 25355 (rating 2): Updated the status of 7/1 from Optional to Mandatory. TSE 25389 (rating 2): Set Table 21 to “No longer used” and removed section heading for SCO Links. |
| 38 |  |  | p38 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Joakim Linde |  |  | Apple |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
| Prasanna Desai |  |  | Broadcom |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Shawn Ding |  |  | Broadcom |  |  |
| Steven Hall |  |  | Broadcom |  |  |
| Farooq Hameed |  |  | Broadcom |  |  |
| Robert Hulvey |  |  | Broadcom |  |  |
| Knut Odman |  |  | Broadcom |  |  |
| Angel Polo |  |  | Broadcom |  |  |
| Erik Rivard |  |  | Broadcom |  |  |
| Mayank Batra |  |  | CSR |  |  |
| Joe Decuir |  |  | CSR |  |  |
| Tim Howes |  |  | CSR |  |  |
| Ian Jones |  |  | CSR |  |  |
| Sean Mitchell |  |  | CSR |  |  |
| Ross O'Connor |  |  | CSR |  |  |
| Steven Singer |  |  | CSR |  |  |
| Dishant Srivastava |  |  | CSR |  |  |
| Jonathan Tanner |  |  | CSR |  |  |
| Steven Wenham |  |  | CSR |  |  |
| Fabien Duvoux |  |  | Ellisys |  |  |
| Kyle Penri-Williams |  |  | Ellisys |  |  |
| Clement Vacheron |  |  | Ellisys |  |  |
| Leif Wilhelmsson |  |  | Ericsson |  |  |
| Magnus Eriksson |  |  | Intel |  |  |
| Marcel Holtmann |  |  | Intel |  |  |
| Sharon Yang |  |  | Intel |  |  |
| Josselin de la Broise |  |  | Marvell |  |  |
| L. C. Ko |  |  | MediaTek |  |  |
| Huanchun Ye |  |  | MediaTek |  |  |
| Krishna Singala |  |  | Mindtree |  |  |
| Lily Chen |  |  | NIST |  |  |
| Kaisa Nyberg |  |  | Nokia |  |  |
| Tsuyoshi Okada |  |  | Panasonic Corporation |  |  |
| Niclas Granqvist |  |  | Polar |  |  |
| Olaf Hirsch |  |  | Qualcomm Atheros |  |  |
| Joel Linsky |  |  | Qualcomm Atheros |  |  |
| Cameron McDonald |  |  | Qualcomm Atheros |  |  |
| Brian A. Redding |  |  | Qualcomm Atheros |  |  |
| Magnus Sommansson |  |  | Qualcomm Technologies International, Ltd. |  |  |
| Jean-Philippe Lambert |  |  | RivieraWaves |  |  |
| Rasmus Abildgren |  |  | Samsung Electronics |  |  |
| Clive D. W. Feather |  |  | Samsung Electronics |  |  |
| Kyong-Sok Seo |  |  | Samsung Electronics Co. Ltd |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Andrew Estrada |  |  | Sony Corporation |  |  |
| Masahiko Seki |  |  | Sony Corporation |  |  |
| Jorgen van Parijs |  |  | ST Ericsson |  |  |
| Yves Wernaers |  |  | ST-Ericsson |  |  |
| Alon Cheifetz |  |  | Texas Instruments |  |  |
| Alon Paycher |  |  | Texas Instruments |  |  |
| Rod Kimmell |  |  | X6D, Inc. |  |  |
