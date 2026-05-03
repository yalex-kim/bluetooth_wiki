# BB.ICS.p27

> Source: PDF converted via PyMuPDF.

---

Baseband (BB)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: BB.ICS.p27 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2004–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Capability Statement


#### 1.2.1 Physical Channel

Table 1: Physical Channel

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Frequency band and 79 RF channels |  |  | [1] 2.1 |  |  | M |  |  |
| 2 |  |  | Adaptive Frequency Hopping Kernel |  |  | [1] 2.6 |  |  | M |  |  |

Table 1a: Modulation

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Support for GFSK modulation | [2] 3.1 | M | [6] RF 1/9 |  |  |
| 2 | Support for π/4-DQPSK modulation | [2] 3.2 | O | [6] RF 1/10 |  |  |
| 3 | Support for 8DPSK modulation | [2] 3.2 | C.2 | [6] RF 1/11 |  |  |

C.1: No longer used.
C.2: Optional IF BB 1a/2 “Support for π/4-DQPSK modulation”, otherwise not defined.

#### 1.2.2 Physical Links

Table 2: Link Types

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | ACL link |  |  | [1] 5.2 |  |  | M |  |  |
| 2 |  |  | SCO link |  |  | [1] 5.4 |  |  | O |  |  |
| 3 |  |  | eSCO link |  |  | [1] 4.3 |  |  | O |  |  |
| 4 |  |  | Enhanced Data Rate ACL links |  |  | [1] 6.5.4 |  |  | C.1 |  |  |
| 5 |  |  | Enhanced Data Rate eSCO links |  |  | [1] 6.5.3 |  |  | C.2 |  |  |
| 6 |  |  | Profile Broadcast Data Link |  |  | [1] 5.7 |  |  | O |  |  |
| 7 |  |  | ACL with AES-CCM and MIC |  |  | [4] 8.3.2 |  |  | C.4 |  |  |
| 8 |  |  | eSCO with AES-CCM |  |  | [4] 8.3.1 |  |  | C.5 |  |  |

C.1: Mandatory IF LMP 2b/1 “EDR for asynchronous transports (single slot)” OR LMP 2b/2 “EDR for asynchronous transports (multi-slot)”, otherwise Excluded.
C.2: Mandatory IF LMP 2b/3 “EDR for synchronous transports (Core 3.0 or later)”, otherwise Excluded.
C.3: No longer used.
C.4: Mandatory IF LMP 2/26 “Secure Connections (Controller Support)”, otherwise Excluded.
C.5: Mandatory IF LMP 2/26 “Secure Connections (Controller Support)” AND BB 2/3 “eSCO link”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | SCO links to same Peripheral |  |  | [1] 4.3 |  |  | C.1 |  |  |
| 2 |  |  | SCO links to different Peripherals |  |  | [1] 4.3 |  |  | C.3 |  |  |
| 3 |  |  | SCO links from same Central |  |  | [1] 4.3 |  |  | C.1 |  |  |
| 4 |  |  | SCO links from different Centrals |  |  | [1] 4.3 |  |  | C.3 |  |  |
| 5 |  |  | eSCO links to same Peripheral |  |  | [1] 4.2 |  |  | C.2 |  |  |
| 6 |  |  | eSCO links to different Peripherals |  |  | [1] 4.2 |  |  | C.4 |  |  |
| 7 |  |  | eSCO links from same Central |  |  | [1] 4.2 |  |  | C.2 |  |  |
| 8 |  |  | eSCO links from different Centrals |  |  | [1] 4.2 |  |  | C.4 |  |  |

C.1: Mandatory to support at least one IF BB 2/2 “SCO link”, otherwise Excluded.
C.2: Mandatory to support at least one IF BB 2/3 “eSCO link”, otherwise Excluded.
C.3: Optional IF BB 2/2 “SCO link”, otherwise Excluded.
C.4: Optional IF BB 2/3 “eSCO link”, otherwise Excluded.
Table 3a: Profile Broadcast Data Link Support
Prerequisite: BB 2/6 “Profile Broadcast Data Link”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connectionless Peripheral Broadcast Transmitter |  |  | [1] 8.10.1, [2] 3.3, Table 3.4, Item 128 |  |  | C.1 |  |  |
| 2 |  |  | Connectionless Peripheral Broadcast Receiver |  |  | [1] 6.5.1, 6.5.1.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

#### 1.2.3 Packet Types

Table 4: Common Packet Types

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | ID packet type |  |  | [1] 6.5.1, 6.5.1.1 |  |  | M |  |  |
| 2 |  |  | NULL packet type |  |  | [1] 6.5.1, 6.5.1.2 |  |  | M |  |  |
| 3 |  |  | POLL packet type |  |  | [1] 6.5.1, 6.5.1.3 |  |  | M |  |  |
| 4 |  |  | FHS packet type |  |  | [1] 6.5.1, 6.5.1.4 |  |  | M |  |  |
| 5 |  |  | DM1 packet type |  |  | [1] 6.5.1, 6.5.1.5, 6.5.4, 6.5.4.1 |  |  | M |  |  |

Table 5: ACL Packet Types

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | DH1 packet type |  |  | [1] 6.5.4, 6.5.4.2 |  |  | M |  |  |
| 2 |  |  | DM3 packet type |  |  | [1] 6.5.4, 6.5.4.3 |  |  | C.1 |  |  |
| 3 |  |  | DH3 packet type |  |  | [1] 6.5.4, 6.5.4.4 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | DM5 packet type |  |  | [1] 6.5.4, 6.5.4.5 |  |  | O |  |  |
| 5 |  |  | DH5 packet type |  |  | [1] 6.5.4, 6.5.4.6 |  |  | O |  |  |
| 6 |  |  | AUX1 packet type |  |  | [1] 6.5.4, 6.5.4.7 |  |  | O |  |  |

C.1: Mandatory IF BB 9c/1 “Synchronization Train” OR BB 9c/2 “Synchronization Scan”, otherwise Optional.
Table 5a: Enhanced Data Rate ACL Packet Types
Prerequisite: BB 2/4 “Enhanced Data Rate ACL links”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 2-DH1 packet type |  |  | [1] 6.5.4.8 |  |  | C.1 |  |  |
| 2 |  |  | 2-DH3 packet type |  |  | [1] 6.5.4.9 |  |  | C.2 |  |  |
| 3 |  |  | 2-DH5 packet type |  |  | [1] 6.5.4.10 |  |  | C.2 |  |  |
| 4 |  |  | 3-DH1 packet type |  |  | [1] 6.5.4.11 |  |  | C.3 |  |  |
| 5 |  |  | 3-DH3 packet type |  |  | [1] 6.5.4.12 |  |  | C.4 |  |  |
| 6 |  |  | 3-DH5 packet type |  |  | [1] 6.5.4.13 |  |  | C.5 |  |  |

C.1: Mandatory IF (LMP 2b/1 “EDR for asynchronous transports (single slot)” OR LMP 2b/2 “EDR for asynchronous transports (multi-slot)”), otherwise Optional IF BB 1a/2 “Support for π/4-DQPSK modulation”, otherwise Excluded.
C.2: Mandatory IF LMP 2b/2 “EDR for asynchronous transports (multi-slot)”, otherwise Optional IF BB 1a/2 “Support for π/4-DQPSK modulation”, otherwise Excluded.
C.3: Mandatory IF LMP 2b/1 “EDR for asynchronous transports (single slot)” OR LMP 2b/2 “EDR for asynchronous transports (multi-slot)”, otherwise Optional IF BB 1a/3 “Support for 8DPSK modulation”, otherwise Excluded.
C.4: Mandatory IF LMP 2b/2 “EDR for asynchronous transports (multi-slot)”, otherwise Optional IF BB 5a/2 “2-DH3 packet type” AND BB 5a/4 “3-DH1 packet type”, otherwise Excluded.
C.5: Mandatory IF LMP 2b/2 “EDR for asynchronous transports (multi-slot)”, otherwise Optional IF BB 5a/3 “2-DH5 packet type” AND BB 5a/4 “3-DH1 packet type”, otherwise Excluded.
Table 6: SCO and eSCO Packet Types

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HV1 packet type |  |  | [1] 6.5.2, 6.5.2.1 |  |  | C.1 |  |  |
| 2 |  |  | HV2 packet type |  |  | [1] 6.5.2, 6.5.2.2 |  |  | C.2 |  |  |
| 3 |  |  | HV3 packet type |  |  | [1] 6.5.2, 6.5.2.3 |  |  | C.2 |  |  |
| 4 |  |  | DV packet type |  |  | [1] 6.5.2, 6.5.2.4 |  |  | C.1 |  |  |
| 5 |  |  | EV3 packet type |  |  | [1] 6.5.3, 6.5.3.1 |  |  | C.3 |  |  |
| 6 |  |  | EV4 packet type |  |  | [1] 6.5.3, 6.5.3.2 |  |  | C.4 |  |  |
| 7 |  |  | EV5 packet type |  |  | [1] 6.5.3, 6.5.3.3 |  |  | C.4 |  |  |

C.1: Mandatory IF BB 2/2 “SCO link”, otherwise Excluded.
C.2: Optional IF BB 2/2 “SCO link”, otherwise Excluded.
C.3: Mandatory IF BB 2/3 “eSCO link”, otherwise Excluded.
C.4: Optional IF BB 2/3 “eSCO link”, otherwise Excluded.
Prerequisite: BB 2/5 “Enhanced Data Rate eSCO links”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 2-EV3 packet type |  |  | [1] 6.5.3.4 |  |  | C.1 |  |  |
| 2 |  |  | 2-EV5 packet type |  |  | [1] 6.5.3.5 |  |  | C.2 |  |  |
| 3 |  |  | 3-EV3 packet type |  |  | [1] 6.5.3.6 |  |  | C.3 |  |  |
| 4 |  |  | 3-EV5 packet type |  |  | [1] 6.5.3.7 |  |  | C.4 |  |  |

C.1: Optional IF BB 1a/2 “Support for π/4-DQPSK modulation”, otherwise Excluded.
C.2: Optional IF BB 6a/1 “2-EV3 packet type”, otherwise Excluded.
C.3: Optional IF BB 1a/3 “Support for 8DPSK modulation” AND BB 6a/1 “2-EV3 packet type”, otherwise Excluded.
C.4: Optional IF BB 6a/3 “3-EV3 packet type”, otherwise Excluded.

#### 1.2.4 Access Procedures

Table 7: Page Procedures

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Paging |  |  | [1] 8.3.2 |  |  | M |  |  |
| 2 |  |  | Page Scan |  |  | [1] 8.3.1 |  |  | M |  |  |
| 3–4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 5 |  |  | Interlaced Scan during Page Scan |  |  | [1] 2.4 |  |  | O |  |  |
| 6 |  |  | Truncated Paging |  |  | [1] 8.3.3 |  |  | C.1 |  |  |
| 7 |  |  | Page Response Timeout Detection |  |  | [1] 8.3 |  |  | C.2 |  |  |
| 8 |  |  | Train Nudging During Page |  |  | [4] 8.3.2 |  |  | C.3 |  |  |
| 9 |  |  | Generalized Interlaced Page Scan |  |  | [4] 8.3.1 |  |  | C.4 |  |  |

C.1: Mandatory IF BB 3a/2 “Connectionless Peripheral Broadcast Receiver”, otherwise Optional.
C.2: Mandatory IF BB 3a/1 “Connectionless Peripheral Broadcast Transmitter”, otherwise Optional.
C.3: Mandatory IF BB 10/8 “Train Nudging During Inquiry”, otherwise Optional.
C.4: Mandatory IF BB 10/9 “Generalized Interlaced Inquiry Scan”, otherwise Optional.
Table 8: Paging Schemes

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Mandatory Scan Mode |  |  | [1] 8.3, Table 6.5 |  |  | M |  |  |

Table 9: Paging Modes

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | paging mode R0 |  |  | [1] 8.3.1, Table 8.1 |  |  | C.1 |  |  |
| 2 |  |  | paging mode R1 |  |  | [1] 8.3.1, Table 8.1 |  |  | C.1 |  |  |
| 3 |  |  | paging mode R2 |  |  | [1] 8.3.1, Table 8.1 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Npage >= 1 |  |  | [1] 8.3.2, Table 8.2 |  |  | O |  |  |
| 2 |  |  | Npage >= 128 |  |  | [1] 8.3.2, Table 8.2 |  |  | O |  |  |
| 3 |  |  | Npage >= 256 |  |  | [1] 8.3.2, Table 8.2 |  |  | M |  |  |

Table 9c: Synchronization Modes Support

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Synchronization Train |  |  | [1] 8.3.5, [2] 3.3, Table 3.4, Item 130 |  |  | C.1 |  |  |
| 2 |  |  | Synchronization Scan |  |  | [1] 8.3.4 [2] 3.3, Table 3.4, Item 131 |  |  | C.2 |  |  |

C.1: Mandatory IF BB 3a/1 “Connectionless Peripheral Broadcast Transmitter” OR BB 18/1 “Coarse Clock Adjustment”, otherwise Excluded.
C.2: Mandatory IF BB 3a/2 “Connectionless Peripheral Broadcast Receiver” OR BB 18/1 “Coarse Clock Adjustment”, otherwise Excluded.
Table 10: Inquiry Procedures

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Inquiry |  |  | [1] 8.4.2 |  |  | O |  |  |
| 2 |  |  | Inquiry Scan with first FHS |  |  | [1] 8.4.2 |  |  | O |  |  |
| 3–4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 5 |  |  | Dedicated Inquiry Access Code |  |  | [1] 6.3.1 |  |  | O |  |  |
| 6 |  |  | Interlaced Scan during Inquiry Scan |  |  | [1] 2.5 |  |  | O |  |  |
| 7 |  |  | Extended Inquiry Response |  |  | [1] 8.4.2, 8.4.3 |  |  | C.1 |  |  |
| 8 |  |  | Train Nudging During Inquiry |  |  | [4] 8.4.2 |  |  | C.2 |  |  |
| 9 |  |  | Generalized Interlaced Inquiry Scan |  |  | [4] 8.4.1 |  |  | C.3 |  |  |

C.1: Mandatory IF GAP 1/3 “General discoverable mode”, otherwise Optional.
C.2: Mandatory IF BB 7/8 “Train Nudging During Page” AND BB 10/1 “Inquiry”, otherwise Excluded.
C.3: Mandatory IF BB 7/9 “Generalized Interlaced Page Scan” AND BB 10/2 “Inquiry Scan with first FHS”, otherwise Excluded.

#### 1.2.5 Networking Capabilities

Table 11: Piconet Capabilities

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcast Messages |  |  | [1] 7.6.5 |  |  | M |  |  |
| 2 |  |  | Point-to-multipoint Connections |  |  | [1] 1 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Act as Central in one piconet and as Peripheral in another piconet |  |  | [1] 1 |  |  | O |  |  |
| 2 |  |  | Act as Peripheral in more than one piconet |  |  | [1] 1 |  |  | O |  |  |


#### 1.2.6 Synchronous Data Formats

Table 13: Synchronous Coding Schemes
Prerequisite: BB 2/2 “SCO link” OR BB 2/3 “eSCO link”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | A-law |  |  | [1] 9.1 |  |  | C.1 |  |  |
| 2 |  |  | -law |  |  | [1] 9.1 |  |  | C.1 |  |  |
| 3 |  |  | CVSD |  |  | [1] 9.2 |  |  | C.1 |  |  |
| 4 |  |  | Transparent Synchronous Data |  |  | [1] 5.4, 5.5 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

#### 1.2.7 Erroneous Data Reporting

Table 14: Erroneous Data Reporting

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Erroneous Data Reporting for SCO |  |  | [1] 7.7 |  |  | C.1 |  |  |
| 2 |  |  | Erroneous Data Reporting for eSCO |  |  | [1] 7.7 |  |  | C.2 |  |  |

C.1: Excluded IF NOT HCI 9/6 “SCO data via HCI” OR NOT BB 2/2 “SCO link”, otherwise Mandatory IF BB 14/2 “Erroneous Data Reporting for eSCO”, otherwise Optional.
C.2: Excluded IF NOT HCI 9/7 “eSCO data via HCI” OR NOT BB 2/3 “eSCO link”, otherwise Mandatory IF BB 14/1 “Erroneous Data Reporting for SCO”, otherwise Optional.

#### 1.2.8 Non-flushable Packet Boundary Flag

Table 16: Non-flushable Packet Boundary Flag

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-flushable Packet Boundary Flag |  |  | [1] 7.6.3 |  |  | C.1 |  |  |

C.1: Mandatory IF HCI 12/10 “Enhanced Flush command”, otherwise Optional.

#### 1.2.9 Connection States

Table 17: Connection States

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sniff Subrating mode |  |  | [3] 4.5.3.3 |  |  | C.1 |  |  |

C.1: Mandatory IF LMP 2/8 “Sniff mode”, otherwise Optional.

#### 1.2.10 Piconet Clock Adjust

Table 18: Coarse Clock Adjust

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Coarse Clock Adjustment |  |  | [4] 8.6.10.1 |  |  | O |  |  |


#### 1.2.11 Slot Availability Mask

Table 19: Slot Availability Mask

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Slot Availability Mask |  |  | [5] 8.6.11 |  |  | C.1 |  |  |

C.1: Optional IF CORE 1a/50 “Controller Core v5.0 or later”, otherwise Excluded.

## 2 References

[1] Specification of the Bluetooth System, Volume 2, Part B
[2] Specification of the Bluetooth System, Volume 2, Part A
[3] Specification of the Bluetooth System, Volume 2, Part C
[4] Bluetooth Core Specification, Version 4.1 or later
[5] Bluetooth Core Specification, Version 5.0 or later
[6] ICS Proforma for Radio Frequency (RF)

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.2.1 |  |  | 2004-03-29 | Changed document number and revision number to conform to legacy system. Added Disclaimer and Copyright Notice. |
|  |  |  | 2.0.E.0 Draft |  |  | 2004-10-22 | Incorporate Enhanced Data Rate Changes, affecting Tables 1a, 2, 5a, 6a, and latest Compliance requirements. |
| 10 |  |  | 2.0.E.0 |  |  | 2004-11-04 | First version for 1.2/2.0/2.0 + EDR available for qualification. |
|  |  |  | 2.0.E.8r0 |  |  | 2006-11 | Add Tables 14, 15, 16, 17 for 2.1 + EDR features Add line 7 to Table 10 for EIR Add new Erroneous Data table Add new Packet Boundary Flag table Add new Persistent Sniff table Add new Connection States table |
|  |  |  | 2.1.E.0r1 |  |  | 2006-12-14 | Change document number for new spec release v2.1 Incorporate reviewer’s comments for M/O 2.1 changes. |
|  |  |  | 2.1.E.0r2 |  |  | 2006-12-20 | Change Connection States Table number from Table 16 to Table 17 |
| 11 |  |  | 2.1.E.0 |  |  | 2006-12-27 | Prepare for publication. |
| 12 |  |  | 2.1.E.1 |  |  | 2007-09-04 | TSE 2082:Add Core 2.1 conditionals to Table 1A TSE 2083: Add Core 2.1 conditionals to Table 2 TSE 2084: Remove Table 15 |
|  |  |  | 2.1.E.2r0 |  |  | 2008-08-27 | TSE 2641; Table 15 renumbered Table16, Table 16 renumbered Table 17. TSE 2653: C.3 for Table 6a. |
| 13 |  |  | 2.1.E.2 |  |  | 2008-12-12 | Prepare for publication. |
|  |  |  | 2.1.E.2a |  |  | 2008-04-21 | Update conditionals to reflect the addition of Core Specification 3.0/3.0+HS |
|  |  |  | 4.0.0r0 |  |  | 2012-05-12 | TSE 4597: Table 1a Footnotes C.1 and C.2 |
| 14 |  |  | 4.0.0 |  |  | 2012-07-24 | Prepare for publication. |
|  |  |  | 4.0.1r1 |  |  | 2012-12-21 | Connectionless Broadcast Change Request |
|  |  |  | 4.0.1r2 |  |  | 2013-01-02 | Connectionless Broadcast Review: Changed Table 5 Item 2 from “O” to “C.1” |
|  |  |  | 4.0.1r3 |  |  | 2013-01-17 | Connectionless Broadcast Review (Magnus) Added C.1 and C.2 for item 6 and 7 in Table 7. |
|  |  |  | 4.0.1r4 |  |  | 2013-01-17 | Connectionless Broadcast Review (Farooq) Table 2 C.3 edited to read “Supported” |
|  |  |  | 4.0.1r5 |  |  | 2013-01-18 | Connectionless Broadcast Review (Magnus & Jason) Edited C.3 for Table 2, item 6. |
|  |  |  | 4.0.1r6 |  |  | 2013-01-22 | Connectionless Broadcast Review (Jason) Added “…or later” after CSA4 in conditionals. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 4.0.1r7 |  |  | 2013-01-24 | Connectionless Broadcast Review (Jason, Alicia, Meagan) Editorial Review Edited for consistent language and syntax for conditionals. Update Table 3a, C.1. |
|  |  |  | 4.0.1r8 |  |  | 2013-01-28 | Approved by BTI |
|  |  |  | 4.0.1r8 |  |  | 2013-02-12 | Approved by BQRB |
| 15 |  |  | 4.0.1 |  |  | 2013-02-19 | Prepare for Publication |
|  |  |  | 4.0.2rT |  |  | 2013-07-26 | Template Conversion Reworded Conditionals to match current conventions |
|  |  |  | 4.0.2rTr3 |  |  | 2013-09-06 | Resolution of Template Conversion Comments |
|  |  |  | 4.1.0r01 |  |  | 2013-09-25 | BR/EDR Secure Connections CR |
|  |  |  | 4.1.0r02 |  |  | 2013-09-25 | Train Nudging and Generalized Interlaced Scan CR |
|  |  |  | 4.1.0r03 |  |  | 2013-09-26 | TSE 5316: Updated C.1 in Table 7 to read “Mandatory if 3a/2 is supported, otherwise Optional." |
|  |  |  | 4.1.0r04 |  |  | 2013-10-09 | Piconet Clock Adjust CR |
|  |  |  | 4.1.0r07 |  |  | 2013-11-06 | Comment resolution |
| 16 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.2.0 |  |  | 2014-11-20 | Version for 4.2 impact |
| 17 |  |  | 4.2.0 |  |  | 2014-12-03 | Prepare for TCRL 2014-2 publication |
|  |  |  | 5.0.0r00 |  |  | 2016-08-16 | TSE 7082: Updated conditional C.2 for Table 2. |
|  |  |  | 5.0.0r01 |  |  | 2016-11-08 | Updated Template. Removed unnecessary parentheses. |
|  |  |  | 5.0.0r02 |  |  | 2016-11-11 | Issue 7884: Global edit. Added support in conditionals for Core Spec version 5.0. |
| 18 |  |  | 5.0.0 |  |  | 2015-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.0.1r00 |  |  | 2017-07-19 | TSE 7436: In C.1 for Table 1a: Modulation, changed “Excluded” to “Optional. In C.2 for Table 1a: Modulation, changed mapping from SUM ICS 22/4 to BB 1a/2. |
| 19 |  |  | 5.0.1 |  |  | 2017-12-07 | Approved by BTI. Prepared for TCRL 2017-2 publication. |
|  |  |  | 5.0.2r00-01 |  |  | 2018-02-15 – 2018-05-11 | TSE 10012 (rating 1): Deleted “Support(s)” from Section 1.2 (Capability Statement). TSE 10611 (rating 2): Some conditionals incorrectly included SUM ICS references for BT core v5.0. Revised Conditional C.2 in Table 2. Revised Conditional C.3 in Table 7. Revised Conditionals C.1 and C.2 in Table 10. Revised Conditionals C.1 and C.2 in Table 14. Revised Conditional C.1 in Table 16. Revised Conditional C.1 in Table 17. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 10612 (rating 2): Added conditional C.1 to Table 18 and changed status of item 18/1 from O to C.1. TSE 10617 (rating 2): Added new section “Slot Availability Mask” and added new reference [5]. |
| 20 |  |  | 5.0.2 |  |  | 2018-07-02 | Approved by BTI. Prepared for TCRL 2018-1 publication. |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1 |
| 21 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | p22r00–r02 |  |  | 2019-10-04 – 2019-12-03 | TSE 12608 (rating 1): Removed references to deprecated and/or withdrawn core specs by updating C.1 and C.2 for Table 1a, updating item 6 and C.1 – C.3 for Table 2, updating C.1 and C.3 for Table 6a, updating items 8 and 9 and C.3 for Table 7, updating items 8 and 9 and C.1 and C.2 for Table 10, removing Values column from Table 11, updating C.1 and C.2 for Table 14, updating C.1 for Table 16, updating C.1 for Table 17, updating item 1 and C.1 for Table 18, and updating C.1 for Table 19. Revised document numbering convention, setting last release publication of 5.1.0 as p21; added Publication Number column to Revision History. Added names to Contributors list. |
| 22 |  |  | p22 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p23r00–r03 |  |  | 2020-09-15 – 2021-06-11 | TSE 14933 (rating 2): Updated conditionals C.2–C.4 of Table 6a. TSE 14938 (rating 2): Updated conditionals C.1 and C.2 of Table 14. TSE 14941 (rating 2): Added conditionals C.3 and C.4 to Table 7 and updated Status column for items 8 and 9 accordingly; added conditionals C.2 and C.3 to Table 10 and updated Status column for items 8 and 9 accordingly. TSE 15446 (rating 1): Editorials to address Erratum 15352, globally change “Master” to “Central” and “Slave” to “Peripheral”. TSE 16044 (rating 2): Updated status of items in Table 11 to Mandatory and updated the reference for item 1. Template-based and consistency checker editorials. |
| 23 |  |  | p23 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |
|  |  |  | p24r00 |  |  | 2021-08-12 | TSE 16945 (rating 2): To address an issue with SCO/eSCO in Table 13, updated the prerequisite and the status column for all items and added conditional C.1. Performed template-related fixes. Updated the copyright page to align with v2 of the DNMD. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 24 |  |  | p24 |  |  | 2022-01-25 | Approved by BTI on 2021-12-27. Prepared for TCRL 2021-2 publication. |
|  |  |  | p24ed2 r00–r01 |  |  | 2022-02-18 – 2022-03-07 | TSE 18358 (rating 1): Updated “is/not supported” language in conditionals globally to align with new conventions. Consistency checker editorials. |
|  |  |  | p24, edition 2 |  |  | 2022-03-07 | Approved by BTI on 2022-03-07. Prepared for edition 2 publication. |
|  |  |  | p25r00 |  |  | 2022-03-30 | TSE 18511 (rating 2): Deleted the prerequisite and updated C1 and C2 for Table 9c. Deleted C1 from Table 18. |
| 25 |  |  | p25 |  |  | 2022-06-28 | Approved by BTI on 2022-05-31. Prepared for TCRL 2022-1 publication. |
|  |  |  | p26r00–r01 |  |  | 2023-09-12 – 2023-10-23 | TSE 24069 (rating 2): To replace SUM.ICS with Core.ICS references, revised descriptions and added ILDs for 1a/1, 1a/2, and 1a/3 and deleted C.1 and revised C.2, changing the status of 1a/2 accordingly. Revised Table 2 conditionals C.1 and C.2. Revised Table 5a conditionals C.1–C.5. Revised Table 19 conditional C.1. Updated the document to align with the latest standards. |
| 26 |  |  | p26 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p27r00–r02 |  |  | 2024-07-22 – 2024-07-24 | TSE 25849 (rating 1): Updated BB ICS item 1a/2 “Support for p/4-DQPSK modulation” to “π/4-DQPSK” and corrected in conditionals throughout. Performed consistency checker editorial updates. |
| 27 |  |  | p27 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| John Padgette |  |  | Accenture |  |  |
| Prasanna Desai |  |  | Broadcom |  |  |
| Shawn Ding |  |  | Broadcom |  |  |
| Steven Hall |  |  | Broadcom |  |  |
| Farooq Hameed |  |  | Broadcom |  |  |
| Robert Hulvey |  |  | Broadcom |  |  |
| Knut Odman |  |  | Broadcom |  |  |
| Erik Rivard |  |  | Broadcom |  |  |
| Mayank Batra |  |  | CSR |  |  |
| Joe Decuir |  |  | CSR |  |  |
| Ian Jones |  |  | CSR |  |  |
| Sean Mitchell |  |  | CSR |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Ross O'Connor |  |  | CSR |  |  |
| Steven Singer |  |  | CSR |  |  |
| Dishant Srivastava |  |  | CSR |  |  |
| Steven Wenham |  |  | CSR |  |  |
| Fabien Duvoux |  |  | Ellisys |  |  |
| Kyle Penri-Williams |  |  | Ellisys |  |  |
| Clement Vacheron |  |  | Ellisys |  |  |
| Leif Wilhelmsson |  |  | Ericsson |  |  |
| Oren Haggai |  |  | Intel |  |  |
| Marcel Holtmann |  |  | Intel |  |  |
| Sharon Yang |  |  | Intel |  |  |
| Josselin de la Broise |  |  | Marvell |  |  |
| L. C. Ko |  |  | MediaTek |  |  |
| Huanchun Ye |  |  | MediaTek |  |  |
| Lily Chen |  |  | NIST |  |  |
| Kaisa Nyberg |  |  | Nokia |  |  |
| Tsuyoshi Okada |  |  | Panasonic Corporation |  |  |
| Olaf Hirsch |  |  | Qualcomm Atheros |  |  |
| Joel Linsky |  |  | Qualcomm Atheros |  |  |
| Cameron McDonald |  |  | Qualcomm Atheros |  |  |
| Brian A. Redding |  |  | Qualcomm Atheros |  |  |
| Magnus Sommansson |  |  | Qualcomm Technologies International, Ltd. |  |  |
| Jean-Philippe Lambert |  |  | RivieraWaves |  |  |
| Clive D. W. Feather |  |  | Samsung Electronics |  |  |
| Kyong-Sok Seo |  |  | Samsung Electronics Co. Ltd |  |  |
| Andrew Estrada |  |  | Sony Corporation |  |  |
| Masahiko Seki |  |  | Sony Corporation |  |  |
| Jorgen van Parijs |  |  | ST Ericsson |  |  |
| Yves Wernaers |  |  | ST-Ericsson |  |  |
| Alon Cheifetz |  |  | Texas Instruments |  |  |
| Alon Paycher |  |  | Texas Instruments |  |  |
| Rod Kimmell |  |  | X6D, Inc |  |  |
