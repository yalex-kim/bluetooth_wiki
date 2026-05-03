# LL.ICS.p22

> Source: PDF converted via PyMuPDF.

---

Link Layer (LL)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: LL.ICS.p22 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2009–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Controller States/Roles

Table 1: Controller States/Roles

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Advertising State | [1] 4.4.2 | C.1 | N/A |  |  |
| 2 | Scanning State | [1] 4.4.3 | C.1 | N/A |  |  |
| 3 | Initiating State | [1] 4.4.4 | C.1 | N/A |  |  |
| 3a | Synchronized State | [6] 4.4.5 | C.4 | N/A |  |  |
| Connection State |  |  |  |  |  |  |
| 4 | Peripheral Role | [1] 4.5.5 | C.3 | N/A |  |  |
| 5 | Central Role | [1] 4.5.4 | C.2 | N/A |  |  |
| 6 | Isochronous Broadcasting State | [7] 4.4.6 | C.5 | N/A |  |  |
| 7 | CS Initiator | [12] 2.4.2.44 | C.6 | [13] RFPHY 3/1 |  |  |
| 8 | CS Reflector | [12] 2.4.2.44 | C.6 | [13] RFPHY 3/2 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF LL 1/3 “Initiating State”, otherwise Excluded.
C.3: Optional IF LL 1/1 “Advertising State”, otherwise Excluded.
C.4: Mandatory IF CORE 1a/51 “Controller Core v5.1 or later” AND (LL 9/27 “Periodic Advertising Sync Transfer - Recipient” OR LL 4/8 “Scanning for Periodic Advertising” OR LL 9/34 “Synchronized Receiver”), otherwise Excluded.
C.5: Mandatory IF LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.6: Optional IF LL 9/56 “Channel Sounding”, otherwise not defined.

### 1.3 Device Addresses


#### 1.3.1 Address Types

Table 2: Device Address Types

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Public Address |  |  | [1] 1.3 |  |  | C.1 |  |  |
| 2 |  |  | Random Address |  |  | [1] 1.3 |  |  | C.1 |  |  |
| 3 |  |  | Static Address |  |  | [3] 1.3.2.1 |  |  | C.3 |  |  |
| 4 |  |  | Generation of private addresses |  |  | [3] 1.3.2.2 |  |  | C.3 |  |  |
| 5 |  |  | Resolution of private addresses |  |  | [3] 1.3.2.3 |  |  | C.2 |  |  |
| 6 |  |  | Network Privacy Mode: Ignore Identity Address when IRK is present in resolving list |  |  | [3] 4.7 |  |  | C.4 |  |  |
| 7 |  |  | Device Privacy Mode |  |  | [3] 4.7 |  |  | C.5 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF LL 2/4 “Generation of private addresses”, otherwise Excluded.
C.3: Mandatory to support at least one IF LL 2/2 “Random Address”, otherwise Excluded.
C.4: Mandatory IF LL 9/13 “LL Privacy”, otherwise Excluded.
C.5: Mandatory IF CORE 1a/50 “Controller Core v5.0 or later” AND LL 9/13 “LL Privacy”, otherwise Optional IF LL 9/13 “LL Privacy”, otherwise Excluded.

### 1.4 Advertising Features


#### 1.4.1 Advertising State

Table 3: Protocol Advertising Features
Prerequisite: LL 1/1 “Advertising State”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sending Events |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Non-connectable and non-scannable undirected events |  |  | [1] 4.4.2.6 [12] 4.4.2.13 |  |  | C.1 |  |  |
| 1a |  |  | Non-connectable and non-scannable directed events |  |  | [6] 4.4.2.9 [12] 4.4.2.13 |  |  | C.16 |  |  |
| 2 |  |  | Connectable and scannable undirected events |  |  | [1] 4.4.2.3 [12] 4.4.2.13 |  |  | C.3 |  |  |
| 3 |  |  | Advertising data |  |  | [1] 4.4.2.3, 4.4.2.5, 4.4.2.6 |  |  | M |  |  |
| 3a |  |  | Address change on advertising data change |  |  | [1] 6.1 |  |  | C.13 |  |  |
| 4 |  |  | Connectable directed events |  |  | [1] 4.4.2.4 [12] 4.4.2.13 |  |  | C.3 |  |  |
| 4a |  |  | Low Duty Cycle Direct Advertising |  |  | [1] 4.4.2.4 |  |  | O |  |  |
| 4b |  |  | Connectable undirected events |  |  | [6] 4.4.2.7 [12] 4.4.2.13 |  |  | C.17 |  |  |
| 5 |  |  | Scannable undirected events |  |  | [1] 4.4.2.5 [12] 4.4.2.13 |  |  | O |  |  |
| 5a |  |  | Scannable directed events |  |  | [6] 4.4.2.8 [12] 4.4.2.13 |  |  | C.18 |  |  |
| Responding in Events |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  | Sending scan responses |  |  | [1] 4.4.2.3, 4.4.2.5 |  |  | C.2 |  |  |
| 7 |  |  | Accepting connection requests |  |  | [1] 4.4.2.3, 4.4.2.4 |  |  | C.3 |  |  |
| Device Filtering |  |  |  |  |  |  |  |  |  |  |  |
| 8 |  |  | Filtering policies |  |  | [1] 4.3.2 |  |  | O |  |  |
| Sending Events |  |  |  |  |  |  |  |  |  |  |  |
| 9 |  |  | Extended Advertising |  |  | [4] 4.6.12 |  |  | C.6 |  |  |
| 10 |  |  | Periodic Advertising |  |  | [4] 4.4.2.12 |  |  | C.12 |  |  |
| 10a |  |  | Periodic Advertising with responses |  |  | [11] 4.4.2.12.2 |  |  | C.14 |  |  |
| 11 |  |  | Multiple Advertising Sets |  |  | [4] 4.4.2.10 |  |  | C.7 |  |  |
| 12 |  |  | Sending Tx Power in advertisements |  |  | [4] 2.3.4.7 |  |  | C.7 |  |  |
| 12a |  |  | Sending Channel Map Update Indication in ACAD |  |  | [9] 1.20 |  |  | C.11 |  |  |
| Additional Advertising Features |  |  |  |  |  |  |  |  |  |  |  |
| 13 |  |  | Connectionless CTE Transmitter |  |  | [6] 4.6.18 |  |  | C.8 |  |  |
| 14 |  |  | Decision-Based Advertising Filtering |  |  | [12] 4.4.2 |  |  | C.15 |  |  |

C.1: Mandatory IF LL 3/10 “Periodic Advertising” OR NOT LL 1/4 “Peripheral Role”, otherwise Optional.
C.2: Mandatory IF LL 1/4 “Peripheral Role”, otherwise Optional.
C.4–C.5: No longer used.
C.6: Mandatory IF LL 9/41 “LE Extended Advertising”, otherwise Excluded.
C.7: Optional IF LL 3/9 “Extended Advertising”, otherwise Excluded.
C.8: Mandatory IF LL 9/16 “Connectionless CTE Transmitter”, otherwise Excluded.
C.9–C.10: No longer used.
C.11: Optional IF LL 3/10 “Periodic Advertising”, otherwise Excluded.
C.12: Mandatory IF LL 9/42 “LE Periodic Advertising”, otherwise Excluded.
C.13: Optional IF LL 2/4 “Generation of private addresses” AND LL 3/3 “Advertising data” AND LL 9/13 “LL Privacy”, otherwise Excluded.
C.14: Mandatory IF LL 9/49 “Periodic Advertising with Responses – Advertiser”, otherwise Excluded.
C.15: Optional IF LL 9/51 “Decision-Based Advertising Filtering”, otherwise Excluded.
C.16: Mandatory IF LL 3/1 “Non-connectable and non-scannable undirected events” AND LL 3/9 “Extended Advertising”, otherwise Excluded.
C.17: Mandatory IF LL 3/4 “Connectable directed events” AND LL 3/9 “Extended Advertising”, otherwise Excluded.
C.18: Mandatory IF LL 3/5 “Scannable undirected events” AND LL 3/9 “Extended Advertising”, otherwise Excluded.

### 1.5 Scanning Features


#### 1.5.1 Scanning State

Table 4: Protocol Scanning Features
Prerequisite: LL 1/2 “Scanning State”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receiving Events |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Passive Scanning |  |  | [1] 4.4.3.1 |  |  | C.1 |  |  |
| 2 |  |  | Receiving Advertising Data |  |  | [1] 4.4.3.1, 4.4.3.2 |  |  | M |  |  |
| Requesting in Events |  |  |  |  |  |  |  |  |  |  |  |
| 3 |  |  | Active Scanning |  |  | [1] 4.4.3.2 |  |  | C.1 |  |  |
| 4 |  |  | Backoff Procedure |  |  | [1] 4.4.3.2 |  |  | C.2 |  |  |
| Device Filtering |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  | Filtering Policies |  |  | [1] 4.3.3 |  |  | M |  |  |
| 6 |  |  | Extended Scanner filter policies |  |  | [3] 4.4.3 |  |  | O |  |  |
| 6a |  |  | Periodic Sync Establishment Filtering Policies |  |  | [4] 4.6.13 |  |  | C.6 |  |  |
| Receiving Events |  |  |  |  |  |  |  |  |  |  |  |
| 7 |  |  | Extended Scanning |  |  | [4] 4.6.12 |  |  | C.4 |  |  |
| 8 |  |  | Scanning for Periodic Advertising |  |  | [4] 4.4.3.4 |  |  | C.5 |  |  |
| 8a |  |  | Scanning for Periodic Advertising with Responses |  |  | [11] 4.4.2.12.2 |  |  | C.7 |  |  |
| 9 |  |  | Decision-Based Advertising Filtering |  |  | [12] 4.4.3.6 |  |  | C.8 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF LL 4/3 “Active Scanning”, otherwise Excluded.
C.3: No longer used.
C.5: Mandatory IF LL 9/42 “LE Periodic Advertising”, otherwise Excluded.
C.6: Mandatory IF LL 4/8 “Scanning for Periodic Advertising”, otherwise Excluded.
C.7: Mandatory IF LL 9/50 “Periodic Advertising with Responses – Scanner”, otherwise Excluded.
C.8: Optional IF LL 9/51 “Decision-Based Advertising Filtering”, otherwise Excluded.
Table 4a: Protocol Scanning Events
Prerequisite: LL 1/2 “Scanning State”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receiving Events |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Non-connectable and non-scannable undirected events |  |  | [1] 4.4.2.6 [12] 4.4.3.7 |  |  | C.1 |  |  |
| 2 |  |  | Non-connectable and non-scannable directed events |  |  | [6] 4.4.2.9 [12] 4.4.3.7 |  |  | C.2 |  |  |
| 3 |  |  | Scannable undirected events |  |  | [1] 4.4.2.5 [12] 4.4.3.7 |  |  | C.3 |  |  |
| 4 |  |  | Scannable directed events |  |  | [6] 4.4.2.8 [12] 4.4.3.7 |  |  | C.4 |  |  |
| 5 |  |  | Connectable directed events |  |  | [1] 4.4.2.4 [12] 4.4.3.7 |  |  | C.5 |  |  |
| 6 |  |  | Connectable undirected events |  |  | [6] 4.4.2.7 [12] 4.4.3.7 |  |  | C.6 |  |  |
| 7 |  |  | Connectable and scannable undirected events |  |  | [1] 4.4.2.3 [12] 4.4.3.7 |  |  | C.7 |  |  |

C.1: Mandatory IF LL 4/8 “Scanning for Periodic Advertising” OR NOT (LL 1/5 “Central Role” OR LL 4/3 “Active Scanning”), otherwise Optional.
C.2: Mandatory IF LL 4/7 “Extended Scanning” AND LL 4a/1 “Non-connectable and non-scannable undirected events”, otherwise Excluded.
C.3: Mandatory IF LL 4/3 “Active Scanning”, otherwise Optional.
C.4: Mandatory IF LL 4/7 “Extended Scanning” AND LL 4a/3 “Scannable undirected events”, otherwise Excluded.
C.5: Mandatory IF LL 1/5 “Central Role”, otherwise Optional.
C.6: Mandatory IF LL 4/7 “Extended Scanning” AND LL 4a/5 “Connectable directed events”, otherwise Excluded.
C.7: Mandatory IF LL 1/5 “Central Role” OR LL 4/3 “Active Scanning”, otherwise Optional.

### 1.6 Initiator Features


#### 1.6.1 Initiating State

Table 5: Protocol Initiating Features
Prerequisite: LL 1/3 “Initiating State”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Requesting in Events |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Requesting Connections |  |  | [1] 4.4.4 |  |  | M |  |  |
| 2 |  |  | Requesting to Directed Advertising |  |  | [1] 4.4.4 |  |  | M |  |  |
| Device Filtering |  |  |  |  |  |  |  |  |  |  |  |
| 3 |  |  | Initiator Filtering |  |  | [1] 4.3.4 |  |  | M |  |  |
| 4 |  |  | Requesting connections using extended advertising |  |  | [4] 4.6.12 |  |  | C.1 |  |  |

C.1: Mandatory IF LL 9/41 “LE Extended Advertising”, otherwise Excluded.

### 1.7 Peripheral Features


#### 1.7.1 Peripheral Role

Table 6: Protocol Peripheral Role Features
Prerequisite: LL 1/4 “Peripheral Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connection Events |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Peripheral Transmissions |  |  | [1] 4.5.1, 4.5.5, 4.5.6 |  |  | M |  |  |
| 2 |  |  | Acknowledgement Scheme |  |  | [1] 4.5.9 |  |  | M |  |  |
| 3 |  |  | Unknown Response |  |  | [1] 5.1.4, 2.4.2 |  |  | M |  |  |
| Feature Setup |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  | Responding in Feature Setup |  |  | [1] 5.1.4.1 |  |  | M |  |  |
| 4a |  |  | Requesting Feature Setup |  |  | [1] 5.1.4.2 |  |  | C.18 |  |  |
| Data Transmissions |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  | Sending Data (Device supports data output from a Host) |  |  | [1] 4.5.1, 4.5.6 |  |  | M |  |  |
| 6 |  |  | Receiving Data (Device supports data input to a Host) |  |  | [1] 4.5.1, 4.5.6 |  |  | M |  |  |
| 7 |  |  | More Data |  |  | [1] 4.5.6 |  |  | O |  |  |
| 8–9 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| Connection Control |  |  |  |  |  |  |  |  |  |  |  |
| 10 |  |  | Accepting Parameter Update |  |  | [1] 5.1.1 |  |  | M |  |  |
| 10a |  |  | Initiating Connection Parameter Request |  |  | [1] 5.1 |  |  | C.2 |  |  |
| 10b |  |  | Accepting Connection Parameter Request |  |  | [1] 5.1 |  |  | C.2 |  |  |
| 11 |  |  | Accepting Channel Map Update |  |  | [1] 5.1.2 |  |  | M |  |  |
| 12 |  |  | Encryption Start |  |  | [1] 5.1.3 |  |  | C.17 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 |  |  | Connection Control Timer |  |  | [1] 5.2 |  |  | M |  |  |
| Connection Termination |  |  |  |  |  |  |  |  |  |  |  |
| 14 |  |  | Sending Termination |  |  | [1] 5.1.6 |  |  | M |  |  |
| 15 |  |  | Accepting Termination |  |  | [1] 5.1.6 |  |  | M |  |  |
| 16 |  |  | Connection Supervision Timer |  |  | [1] 4.5.2 |  |  | M |  |  |
| 17 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| Pause Encryption |  |  |  |  |  |  |  |  |  |  |  |
| 18 |  |  | Peripheral Pause Encryption |  |  | [1] 5.1.3 |  |  | C.17 |  |  |
| Version Exchange |  |  |  |  |  |  |  |  |  |  |  |
| 19 |  |  | Peripheral Version Exchange |  |  | [1] 5.1.5 |  |  | M |  |  |
| 20 |  |  | Peripheral listens to multiple packets per connection event |  |  | [1] 4.5.7 |  |  | O |  |  |
| 21 |  |  | LE Authenticated Payload Timeout |  |  | [2] 5.4 |  |  | C.5 |  |  |
| 22 |  |  | Data Length Update Procedure |  |  | [3] 5.1.9 |  |  | C.4 |  |  |
| 23 |  |  | Minimum Number Of Used Channels Procedure |  |  | [4] 4.6.15 |  |  | C.6 |  |  |
| 23a |  |  | PHY Update procedure |  |  | [4] 5.1.10 |  |  | C.9 |  |  |
| 24 |  |  | Constant Tone Extension Request Procedure as Initiator |  |  | [6] 5.1.12 |  |  | C.7 |  |  |
| 25 |  |  | Constant Tone Extension Request Procedure as Responder |  |  | [6] 5.1.12 |  |  | C.8 |  |  |
| 26 |  |  | Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising |  |  | [6] 5.1.13 |  |  | C.10 |  |  |
| 26a |  |  | Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising, Subevents |  |  | [11] 5.1.13 |  |  | C.22 |  |  |
| 27 |  |  | Initiating Periodic Advertising Sync Transfer Procedure for Remote Periodic Advertising |  |  | [6] 5.1.13 |  |  | C.11 |  |  |
| 28 |  |  | Accepting Periodic Advertising Sync Transfer Procedure |  |  | [6] 5.1.13 |  |  | C.12 |  |  |
| 28a |  |  | Accepting Periodic Advertising Sync Transfer Procedure, Subevents |  |  | [11] 5.1.13 |  |  | C.21 |  |  |
| 29 |  |  | Sending Long Control PDUs |  |  | [6] 4.5.11 |  |  | C.13 |  |  |
| 30 |  |  | Receiving Long Control PDUs |  |  | [6] 4.5.11 |  |  | C.14 |  |  |
| 31 |  |  | Can Change Sleep Clock Accuracy |  |  | [6] 4.6.25 |  |  | C.15 |  |  |
| Isochronous Channels |  |  |  |  |  |  |  |  |  |  |  |
| 32 |  |  | Bi-Directional Data in Single Connected Isochronous Stream |  |  | [7] 4.5.14 |  |  | C.16 |  |  |
| 33 |  |  | Bi-Directional Data in Multiple Connected Isochronous Streams |  |  | [7] 4.5.14 |  |  | C.20 |  |  |
| Channel Classification |  |  |  |  |  |  |  |  |  |  |  |
| 34 |  |  | Channel Classification Reporting |  |  | [1] 4.5.8.1 |  |  | C.19 |  |  |

C.1: No longer used.
C.2: Mandatory IF LL 9/3 “Connection Parameters Request procedure”, otherwise Excluded.
C.3: No longer used.
C.4: Mandatory IF LL 9/6 “LE Data Packet Length Extension”, otherwise Excluded.
C.6: Mandatory IF LL 9/12 “Minimum Number of Used Channels procedure”, otherwise Excluded.
C.7: Mandatory IF LL 9/14 “Connection CTE Request”, otherwise Excluded.
C.8: Mandatory IF LL 9/15 “Connection CTE Response”, otherwise Excluded.
C.9: Mandatory IF CORE 1a/50 “Controller Core v5.0 or later” AND LL 9/6a “Multiple PHYs”, otherwise Optional IF CORE 1a/50 “Controller Core v5.0 or later”, otherwise Excluded.
C.10: Mandatory IF LL 9/28 “Initiating Periodic Advertising Sync Transfer for Local Periodic Advertising”, otherwise Excluded.
C.11: Mandatory IF LL 9/29 “Initiating Periodic Advertising Sync Transfer for Remote Periodic Advertising”, otherwise Excluded.
C.12: Mandatory IF LL 9/27 “Periodic Advertising Sync Transfer - Recipient”, otherwise Excluded.
C.13: Mandatory IF LL 6/26 “Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising” OR LL 6/27 “Initiating Periodic Advertising Sync Transfer Procedure for Remote Periodic Advertising”, otherwise Excluded.
C.14: Mandatory IF LL 6/28 “Accepting Periodic Advertising Sync Transfer Procedure” OR LL 9/32 “Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.15: Mandatory IF LL 9/40 “Can Change Sleep Clock Accuracy”, otherwise Excluded.
C.16: Mandatory IF LL 9/32 “Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.17: Mandatory IF LL 9/1 “LE Encryption”, otherwise Excluded.
C.18: Mandatory IF LL 9/5 “Peripheral-initiated Features Exchange” OR LL 9/55 “LL Extended Feature Set”, otherwise Excluded.
C.19: Mandatory IF LL 9/44 “Channel Classification”, otherwise Excluded.
C.20: Optional IF LL 9/32 “Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.21: Mandatory IF LL 6/28 “Accepting Periodic Advertising Sync Transfer Procedure” AND LL 9/50 “Periodic Advertising with Responses – Scanner”, otherwise Excluded.
C.22: Mandatory IF LL 6/26 “Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising” AND LL 9/49 “Periodic Advertising with Responses – Advertiser”, otherwise Excluded.

### 1.8 Central Features


#### 1.8.1 Central Role

Table 7: Protocol Central Role Features
Prerequisite: LL 1/5 “Central Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connection Events |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Central Transmissions |  |  | [1] 4.5.1, 4.5.4, 4.5.6 |  |  | M |  |  |
| 2 |  |  | Acknowledgement Scheme |  |  | [1] 4.5.9 |  |  | M |  |  |
| 3 |  |  | Unknown Responses |  |  | [1] 5.1.4, 2.4.2 |  |  | M |  |  |
| Feature Setup |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  |  | Requesting Feature Setup |  |  | [1] 5.1.4.1 |  |  | M |  |  |
| 4a |  |  | Responding in Feature Setup |  |  | [1] 5.1.4.2 |  |  | C.18 |  |  |
| Data Transmissions |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  |  | Sending Data (Device supports data output from a Host) |  |  | [1] 4.5.1, 4.5.6 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 |  |  | Receiving Data (Device supports data input to a Host) |  |  | [1] 4.5.1, 4.5.6 |  |  | M |  |  |
| 7 |  |  | More Data |  |  | [1] 4.5.6 |  |  | O |  |  |
| 8–9 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| Connection Control |  |  |  |  |  |  |  |  |  |  |  |
| 10 |  |  | Requesting Parameter Update |  |  | [1] 5.1.1 |  |  | M |  |  |
| 10a |  |  | Initiating Connection Parameter Request |  |  | [1] 5.1 |  |  | C.2 |  |  |
| 10b |  |  | Accepting Connection Parameter Request |  |  | [1] 5.1 |  |  | C.2 |  |  |
| 11 |  |  | Requesting Channel Map Update |  |  | [1] 5.1.2 |  |  | M |  |  |
| 12 |  |  | Encryption Start |  |  | [1] 5.1.3 |  |  | C.17 |  |  |
| 13 |  |  | Connection Control Timer |  |  | [1] 5.2 |  |  | M |  |  |
| Connection Termination |  |  |  |  |  |  |  |  |  |  |  |
| 14 |  |  | Sending Termination |  |  | [1] 5.1.6 |  |  | M |  |  |
| 15 |  |  | Accepting Termination |  |  | [1] 5.1.6 |  |  | M |  |  |
| 16 |  |  | Connection Supervision Timer |  |  | [1] 4.5.2 |  |  | M |  |  |
| 17–18 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| Pause Encryption |  |  |  |  |  |  |  |  |  |  |  |
| 19 |  |  | Central Pause Encryption |  |  | [1] 5.1.3 |  |  | C.17 |  |  |
| Version Exchange |  |  |  |  |  |  |  |  |  |  |  |
| 20 |  |  | Central Version Exchange |  |  | [1] 5.1.5 |  |  | M |  |  |
| Connection Control |  |  |  |  |  |  |  |  |  |  |  |
| 21 |  |  | LE Authenticated Payload Timeout |  |  | [2] 5.4 |  |  | C.5 |  |  |
| 22 |  |  | Data Length Update Procedure |  |  | [3] 5.1.9 |  |  | C.4 |  |  |
| 23 |  |  | Minimum Number Of Used Channels Procedure |  |  | [4] 4.6.15 |  |  | C.6 |  |  |
| 23a |  |  | PHY Update procedure |  |  | [4] 5.1.10 |  |  | C.9 |  |  |
| 24 |  |  | Constant Tone Extension Request Procedure as Initiator |  |  | [6] 5.1.12 |  |  | C.7 |  |  |
| 25 |  |  | Constant Tone Extension Request Procedure as Responder |  |  | [6] 5.1.12 |  |  | C.8 |  |  |
| 26 |  |  | Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising |  |  | [6] 5.1.13 |  |  | C.10 |  |  |
| 26a |  |  | Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising, Subevents |  |  | [11] 5.1.13 |  |  | C.22 |  |  |
| 27 |  |  | Initiating Periodic Advertising Sync Transfer Procedure for Remote Periodic Advertising |  |  | [6] 5.1.13 |  |  | C.11 |  |  |
| 28 |  |  | Accepting Periodic Advertising Sync Transfer Procedure |  |  | [6] 5.1.13 |  |  | C.12 |  |  |
| 28a |  |  | Accepting Periodic Advertising Sync Transfer Procedure, Subevents |  |  | [11] 5.1.13 |  |  | C.21 |  |  |
| 29 |  |  | Sending Long Control PDUs |  |  | [6] 4.5.11 |  |  | C.13 |  |  |
| 30 |  |  | Receiving Long Control PDUs |  |  | [6] 4.5.11 |  |  | C.14 |  |  |
| 31 |  |  | Can Change Sleep Clock Accuracy |  |  | [6] 4.6.25 |  |  | C.15 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Isochronous Channels |  |  |  |  |  |  |  |  |  |  |  |
| 32a |  |  | More than one CIS in a CIG |  |  | [7] 4.5.14 |  |  | C.20 |  |  |
| 32 |  |  | CIG with multiple CISes: Sequential |  |  | [7] 4.5.14 |  |  | C.16 |  |  |
| 33 |  |  | CIG with multiple CISes: Interleaved |  |  | [7] 4.5.14 |  |  | C.16 |  |  |
| Channel Classification |  |  |  |  |  |  |  |  |  |  |  |
| 34 |  |  | Channel Classification Enable |  |  | [1] 4.5.8.1 |  |  | C.19 |  |  |

C.1: No longer used.
C.2: Mandatory IF LL 9/3 “Connection Parameters Request procedure”, otherwise Excluded.
C.3: No longer used.
C.4: Mandatory IF LL 9/6 “LE Data Packet Length Extension”, otherwise Excluded.
C.5: Mandatory IF LL 9/2 “LE Ping”, otherwise Excluded.
C.6: Mandatory IF LL 9/12 “Minimum Number of Used Channels procedure”, otherwise Excluded.
C.7: Mandatory IF LL 9/14 “Connection CTE Request”, otherwise Excluded.
C.8: Mandatory IF LL 9/15 “Connection CTE Response”, otherwise Excluded.
C.9: Mandatory IF CORE 1a/50 “Controller Core v5.0 or later” AND LL 9/6a “Multiple PHYs”, otherwise Optional IF CORE 1a/50 “Controller Core v5.0 or later”, otherwise Excluded.
C.10: Mandatory IF LL 9/28 “Initiating Periodic Advertising Sync Transfer for Local Periodic Advertising”, otherwise Excluded.
C.11: Mandatory IF LL 9/29 “Initiating Periodic Advertising Sync Transfer for Remote Periodic Advertising”, otherwise Excluded.
C.12: Mandatory IF LL 9/27 “Periodic Advertising Sync Transfer - Recipient”, otherwise Excluded.
C.13: Mandatory IF (LL 7/26 “Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising” OR LL 7/27 “Initiating Periodic Advertising Sync Transfer Procedure for Remote Periodic Advertising” OR LL 9/31 “Connected Isochronous Stream - Central”), otherwise Excluded.
C.14: Mandatory IF LL 7/28 “Accepting Periodic Advertising Sync Transfer Procedure”, otherwise Excluded.
C.15: Mandatory IF LL 9/40 “Can Change Sleep Clock Accuracy”, otherwise Excluded.
C.16: Mandatory IF LL 7/32a “More than one CIS in a CIG”, otherwise Excluded.
C.17: Mandatory IF LL 9/1 “LE Encryption”, otherwise Excluded.
C.18: Mandatory IF LL 9/5 “Peripheral-initiated Features Exchange” OR LL 9/55 “LL Extended Feature Set”, otherwise Excluded.
C.19: Mandatory IF LL 9/44 “Channel Classification”, otherwise Excluded.
C.20: Optional IF LL 9/31 “Connected Isochronous Stream - Central”, otherwise Excluded.
C.21: Mandatory IF LL 7/28 “Accepting Periodic Advertising Sync Transfer Procedure” AND LL 9/50 “Periodic Advertising with Responses – Scanner”, otherwise Excluded.
C.22: Mandatory IF LL 7/26 “Initiating Periodic Advertising Sync Transfer Procedure for Local Periodic Advertising” AND LL 9/49 “Periodic Advertising with Responses – Advertiser”, otherwise Excluded.

### 1.9 Physical Channels

Table 8: Physical Channels

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | General-purpose channels |  |  | [1] 1.4.1 |  |  | C.1 |  |  |
| 2 |  |  | Primary Advertising channels |  |  | [1] 1.4.1 |  |  | M |  |  |
| 3 |  |  | Support Data channel selection algorithm |  |  | [1] 4.5.8 |  |  | C.2 |  |  |

C.1: Mandatory IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role” OR LL 1/6 “Isochronous Broadcasting State” OR LL 3/9 “Extended Advertising”, otherwise Excluded.
C.2: Mandatory IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role” OR LL 9/10 “Channel Selection Algorithm #2”, otherwise Excluded.

### 1.10 Supported Features

Table 9: Supported Features

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 4.6.1 | O | N/A |  |  |
| 2 | LE Ping | [2] 4.6.5 | O | N/A |  |  |
| 3 | Connection Parameters Request procedure | [1] 4.6.2 | C.2 | N/A |  |  |
| 4 | Extended Reject Indication | [1] 4.6.3 | O | N/A |  |  |
| 5 | Peripheral-initiated Features Exchange | [1] 4.6.4 | O | N/A |  |  |
| 6 | LE Data Packet Length Extension | [3] 4.6.6 | O | N/A |  |  |
| 6a | Multiple PHYs | [4] 4.6.9 | C.6 | N/A |  |  |
| 7 | LE 2M PHY | [3] 2.1 | C.5 | N/A |  |  |
| 8 | Asymmetric connections | [4] 4.6.9.1 | C.7 | N/A |  |  |
| 9 | LE Coded PHY | [4] 2.2 | C.5 | N/A |  |  |
| 10 | Channel Selection Algorithm #2 | [4] 4.6.14 | C.10 | N/A |  |  |
| 11 | LE Power Class 1 | [4] 4.6 | C.9 | N/A |  |  |
| 12 | Minimum Number of Used Channels procedure | [4] 4.6.15 | C.10 | N/A |  |  |
| 13 | LL Privacy | [4] 4.6.7 | C.54 | N/A |  |  |
| 14 | Connection CTE Request | [6] 4.6.16 | C.11 | N/A |  |  |
| 15 | Connection CTE Response | [6] 4.6.17 | C.4 | N/A |  |  |
| 16 | Connectionless CTE Transmitter | [6] 4.6.18 | C.12 | N/A |  |  |
| 17 | Connectionless CTE Receiver | [6] 4.6.19 | C.13 | N/A |  |  |
| 18 | 2 µs Antenna Switching During Constant Tone Extension Transmission (AoD) | [6] 4.6.20 | C.14 | N/A |  |  |
| 19 | No Antenna Switching During Constant Tone Extension Transmission (AoA) | [6] 4.6.20 | C.15 | N/A |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 20 | 2 µs Antenna Sampling During Constant Tone Extension Reception (AoD) | [6] 4.6.21 | C.16 | N/A |  |  |
| 21 | 2 µs Antenna Switching And Sampling During Constant Tone Extension Reception (AoA) | [6] 4.6.21 | C.27 | N/A |  |  |
| 22 | 1 µs Antenna Switching During Constant Tone Extension Transmission (AoD) | [6] 4.6.20 | C.17 | N/A |  |  |
| 23 | 1 µs Antenna Sampling During Constant Tone Extension Reception (AoD) | [6] 4.6.21 | C.18 | N/A |  |  |
| 24 | 1 µs Antenna Switching and Sampling During Constant Tone Extension Reception (AoA) | [6] 4.6.21 | C.19 | N/A |  |  |
| 25 | Remote Public Key Validation | [5] 4.6.23 [6] 4.6.26 | O | N/A |  |  |
| 26 | Periodic Advertising Sync Transfer - Sender | [6] 4.6.23 | C.23 | N/A |  |  |
| 27 | Periodic Advertising Sync Transfer - Recipient | [6] 4.6.24 | C.22 | N/A |  |  |
| 28 | Initiating Periodic Advertising Sync Transfer for Local Periodic Advertising | [6] 5.1.13 | C.21 | N/A |  |  |
| 29 | Initiating Periodic Advertising Sync Transfer for Remote Periodic Advertising | [6] 5.1.13 | C.21 | N/A |  |  |
| 30 | Sleep Clock Accuracy Updates | [6] 4.6.25 | C.37 | N/A |  |  |
| 31 | Connected Isochronous Stream - Central | [7] 4.6.27 | C.28 | N/A |  |  |
| 32 | Connected Isochronous Stream - Peripheral | [7] 4.6.27 | C.29 | N/A |  |  |
| 33 | Isochronous Broadcaster | [7] 4.6.28 | C.30 | N/A |  |  |
| 34 | Synchronized Receiver | [7] 4.6.29 | C.30 | N/A |  |  |
| 35 | ISO Receive Test | [8] 7.8.112, 7.8.113, 7.8.114 | C.32 | N/A |  |  |
| 36 | ISO Transmit Test | [8] 7.8.111, 7.8.114 | C.33 | N/A |  |  |
| 37 | LE Power Control Request | [7] 4.6.31 | C.34 | N/A |  |  |
| 38 | No longer used | N/A | N/A | N/A |  |  |
| 39 | LE Path Loss Monitoring | [7] 4.6.32 | C.34 | N/A |  |  |
| 39a | LE Path Loss Monitoring when the path loss becomes unavailable | [7] 4.6.32 | C.43 | N/A |  |  |
| 40 | Can Change Sleep Clock Accuracy | [6] 4.6.25 | C.37 | N/A |  |  |
| 41 | LE Extended Advertising | [6] 4.6.12 | C.38 | N/A |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 42 | LE Periodic Advertising | [6] 4.6.13 | C.39 | N/A |  |  |
| 43 | Periodic Advertising ADI support | [10] 4.6.34 | C.40 | N/A |  |  |
| 44 | Channel Classification | [10] 4.6.36 | C.41 | N/A |  |  |
| 45 | Connection Subrating | [10] 4.6.35 | C.41 | N/A |  |  |
| 46 | BN values greater than 1 in CIS | [7] 4.5.13.1 | C.42 | N/A |  |  |
| 47 | FT values greater than 1 in CIS | [7] 4.5.13.1 | C.42 | N/A |  |  |
| 48 | Advertising Coding Selection | [11] 4.6.37 | C.44 | N/A |  |  |
| 49 | Periodic Advertising with Responses – Advertiser | [11] 4.6.38 | C.45 | N/A |  |  |
| 50 | Periodic Advertising with Responses – Scanner | [11] 4.6.39 | C.46 | N/A |  |  |
| 51 | Decision-Based Advertising Filtering | [12] 4.6.43 | C.47 | N/A |  |  |
| 52 | Monitoring Advertisers | [12] 4.6.45 | C.48 | N/A |  |  |
| 53 | Unsegmented Framed Mode | [12] 4.6.44 | C.49 | N/A |  |  |
| 54 | Frame Space Update | [12] 4.6.46 | C.50 | N/A |  |  |
| 55 | LL Extended Feature Set | [12] 4.6.40 | C.51 | N/A |  |  |
| 56 | Channel Sounding | [12] 4.6.41 | C.52 | [13] RFPHY 1/16 |  |  |
| 57 | CS Tone Quality Indication | [12] 4.6.42 | C.53 | N/A |  |  |
| 58 | Stable Modulation Index – Transmitter | [1] 4.6.10 | C.10 | [13] RFPHY 1/5 |  |  |
| 59 | Stable Modulation Index – Receiver | [1] 4.6.11 | C.10 | [13] RFPHY 1/6 |  |  |
| 60 | Features with Host Controlled feature bits | [7] 4.6, 4.6.33 | C.55 | N/A |  |  |
| 61 | Features with bits > 63 | [12] 4.6 | C.56 | N/A |  |  |

C.1: No longer used.
C.2: Optional IF LL 9/4 “Extended Reject Indication”, otherwise Excluded.
C.3: No longer used.
C.4: Optional IF CORE 1a/51 “Controller Core v5.1 or later” AND LL 9/4 “Extended Reject Indication” AND (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”) AND RFPHY 1/8 “Transmitting Constant Tone Extensions”, otherwise Excluded.
C.5: Optional IF CORE 1a/50 “Controller Core v5.0 or later” AND LL 9/4 “Extended Reject Indication”, otherwise Excluded.
C.6: Mandatory IF LL 9/7 “LE 2M PHY” OR LL 9/9 “LE Coded PHY”, otherwise Excluded.
C.7: Optional IF LL 9/6a “Multiple PHYs”, otherwise Excluded.
C.8: No longer used.
C.9: Mandatory IF RFPHY 1/15 “Power Class 1”, otherwise Excluded.
C.10: Optional IF CORE 1a/50 “Controller Core v5.0 or later”, otherwise not defined.
C.11: Optional IF CORE 1a/51 “Controller Core v5.1 or later” AND LL 9/4 “Extended Reject Indication” AND (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”) AND LL 9/20 “2 µs Antenna Sampling During Constant Tone Extension Reception (AoD)”, otherwise Excluded.
C.12: Optional IF CORE 1a/51 “Controller Core v5.1 or later” AND LL 3/10 “Periodic Advertising” AND RFPHY 1/8 “Transmitting Constant Tone Extensions”, otherwise Excluded.
C.13: Optional IF LL 11/1 “Synchronizing to Periodic Advertising” AND RFPHY 1/11 “2 µs Antenna Sampling During Constant Tone Extension Reception (AoD)”, otherwise Excluded.
C.14: Optional IF LL 9/19 “No Antenna Switching During Constant Tone Extension Transmission (AoA)” AND RFPHY 1/9 “2 µs Antenna Switching During Constant Tone Extension Transmission (AoD)”, otherwise Excluded.
C.15: Optional IF RFPHY 1/8 “Transmitting Constant Tone Extensions”, otherwise Excluded.
C.16: Optional IF RFPHY 1/11 “2 µs Antenna Sampling During Constant Tone Extension Reception (AoD)”, otherwise Excluded.
C.17: Optional IF LL 9/18 “2 µs Antenna Switching During Constant Tone Extension Transmission (AoD)” AND RFPHY 1/10 “1 µs Antenna Switching During Constant Tone Extension Transmission (AoD)”, otherwise Excluded.
C.18: Optional IF LL 9/20 “2 µs Antenna Sampling During Constant Tone Extension Reception (AoD)” AND RFPHY 1/13 “1 µs Antenna Sampling During Constant Tone Extension Reception (AoD)”, otherwise Excluded.
C.19: Mandatory IF LL 9/21 “2 µs Antenna Switching And Sampling During Constant Tone Extension Reception (AoA)” AND LL 9/23 “1 µs Antenna Sampling During Constant Tone Extension Reception (AoD)” AND RFPHY 1/14 “1 µs Antenna Switching and Sampling During Constant Tone Extension Reception (AoA)”, otherwise Excluded.
C.20: No longer used.
C.21: Mandatory IF LL 9/26 “Periodic Advertising Sync Transfer - Sender”, otherwise Excluded.
C.22: Optional IF CORE 1a/51 “Controller Core v5.1 or later” AND LL 11/1 “Synchronizing to Periodic Advertising” AND (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”), otherwise Excluded.
C.23: Optional IF CORE 1a/51 “Controller Core v5.1 or later” AND LL 3/10 “Periodic Advertising” AND (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”), otherwise Excluded.
C.24–C.26: No longer used.
C.27: Optional IF LL 9/20 “2 µs Antenna Sampling During Constant Tone Extension Reception (AoD)” AND RFPHY 1/12 “2 µs Antenna Switching and Sampling During Constant Tone Extension Reception (AoA)”, otherwise Excluded.
C.28: Optional IF CORE 1a/52 “Controller Core v5.2 or later” AND LL 1/5 “Central Role” AND LL 9/4 “Extended Reject Indication” AND LL 9/10 “Channel Selection Algorithm #2” AND LL 9/30 “Sleep Clock Accuracy Updates”, otherwise Excluded.
C.29: Optional IF CORE 1a/52 “Controller Core v5.2 or later” AND LL 1/4 “Peripheral Role” AND LL 9/4 “Extended Reject Indication” AND LL 9/10 “Channel Selection Algorithm #2” AND LL 9/30 “Sleep Clock Accuracy Updates”, otherwise Excluded.
C.30: Optional IF CORE 1a/52 “Controller Core v5.2 or later” AND LL 9/42 “LE Periodic Advertising”, otherwise Excluded.
C.31: No longer used.
C.32: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.33: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.34: Optional IF CORE 1a/52 “Controller Core v5.2 or later” AND LL 9/4 “Extended Reject Indication”, otherwise Excluded.
C.35–C.36: No longer used.
C.37: Optional IF CORE 1a/51 “Controller Core v5.1 or later”, otherwise Excluded.
C.38: Optional IF CORE 1a/50 “Controller Core v5.0 or later” AND (LL 9/10 “Channel Selection Algorithm #2” OR NOT (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”)), otherwise Excluded.
C.39: Optional IF LL 9/41 “LE Extended Advertising” AND LL 9/10 “Channel Selection Algorithm #2”, otherwise Excluded.
C.40: Optional IF CORE 1a/53 “Controller Core v5.3 or later” AND LL 9/42 “LE Periodic Advertising”, otherwise Excluded.
C.41: Optional IF CORE 1a/53 “Controller Core v5.3 or later”, otherwise Excluded.
C.42: Optional IF (LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral”), otherwise Excluded.
C.43: Optional IF LL 9/39 “LE Path Loss Monitoring”, otherwise Excluded.
C.44: Optional IF CORE 1a/54 “Controller Core v5.4 or later” AND LL 9/9 “LE Coded PHY” AND LL 3/9 “Extended Advertising”, otherwise Excluded.
C.45: Optional IF CORE 1a/54 “Controller Core v5.4 or later” AND LL 9/26 “Periodic Advertising Sync Transfer - Sender”, otherwise Excluded.
C.46: Optional IF CORE 1a/54 “Controller Core v5.4 or later” AND LL 9/27 “Periodic Advertising Sync Transfer - Recipient”, otherwise Excluded.
C.47: Optional IF CORE 1a/60 “Controller Core v6.0 or later” AND LL 9/41 “LE Extended Advertising”, otherwise Excluded.
C.48: Optional IF CORE 1a/60 “Controller Core v6.0 or later” AND LL 1/2 “Scanning State” AND LL 9/55 “LL Extended Feature Set”, otherwise Excluded.
C.49: Optional IF CORE 1a/60 “Controller Core v6.0 or later” AND CORE 20a/3 “Isochronous channels”, otherwise Excluded.
C.50: Optional IF CORE 1a/60 “Controller Core v6.0 or later”, otherwise Excluded.
C.51: Excluded IF CORE 1b/54 “Controller Core v5.4 or earlier”, otherwise Mandatory IF LL 9/61 “Features with bits > 63”, otherwise Optional.
C.52: Optional IF CORE 1a/60 “Controller Core v6.0 or later” AND LL 9/4 “Extended Reject Indication”, otherwise not defined.
C.53: Optional IF LL 9/56 “Channel Sounding”, otherwise Excluded.
C.54: Optional IF LL 2/4 “Generation of private addresses” AND LL 2/5 “Resolution of private addresses”, otherwise Excluded.
C.55: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/45 “Connection Subrating” OR LL 9/48 “Advertising Coding Selection” OR LL 9/56 “Channel Sounding”, otherwise Excluded.
C.56: Mandatory IF LL 9/52 “Monitoring Advertisers” OR LL 9/54 “Frame Space Update”, otherwise Excluded.

### 1.11 Scatternet Capabilities

Table 10: Scatternet Capabilities

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Act as LE Central and LE Peripheral at the same time |  |  | [2] 1.1.1 |  |  | C.1 |  |  |
| 2 |  |  | Act as LE Peripheral to more than one LE Central at the same time. |  |  | [2] 1.1.1 |  |  | C.2 |  |  |
| 3 |  |  | Simultaneous Connection and Advertising States |  |  | [2] 1.1.1 |  |  | O |  |  |

C.1: Optional IF LL 1/4 “Peripheral Role” AND LL 1/5 “Central Role”, otherwise Excluded.
C.2: Optional IF LL 1/4 “Peripheral Role”, otherwise Excluded.

### 1.12 Synchronized Features

Table 11 structures the mandatory and optional requirements as features of a device supporting synchronizing. This section is completed by suppliers with implementations supporting this state.

#### 1.12.1 Synchronized State

Table 11: Protocol Synchronizing Features
Prerequisite: LL 1/3a “Synchronized State”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Synchronizing to Periodic Advertising |  |  | [6] 4.4.3.4 |  |  | C.3 |  |  |
| 2 |  |  | Connectionless CTE Receiver |  |  | [6] 4.6.19 |  |  | C.1 |  |  |
| 3 |  |  | Receiving Data on Single Broadcast Isochronous Stream |  |  | [7] 4.4.5.2 |  |  | C.2 |  |  |
| 4 |  |  | Receiving Data on Multiple Broadcast Isochronous Streams |  |  | [7] 4.4.5.2 |  |  | C.4 |  |  |

C.1: Mandatory IF LL 9/17 “Connectionless CTE Receiver”, otherwise Excluded.
C.2: Mandatory IF LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.3: Mandatory IF LL 4/8 “Scanning for Periodic Advertising”, otherwise Excluded.
C.4: Optional IF LL 9/34 “Synchronized Receiver”, otherwise Excluded.
Table 11a: Synchronized Receiver Features
Prerequisite: LL 9/34 “Synchronized Receiver”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BN values greater than 1 |  |  | [7] 4.4.6.3 |  |  | O |  |  |
| 2 |  |  | Pre-transmission |  |  | [7] 4.4.6.3 |  |  | O |  |  |


### 1.13 Isochronous Broadcasting Features

Table 12 structures the mandatory and optional requirements as features of a device supporting streaming. This section is completed by suppliers with implementations supporting this state.

#### 1.13.1 Isochronous Broadcasting State

Table 12: Protocol Isochronous Broadcasting Features
Prerequisite: LL 1/6 “Isochronous Broadcasting State”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Encrypted Broadcast Isochronous Stream |  |  | [7] 4.4.6.1, 4.4.6.10 |  |  | C.1 |  |  |
| 2 |  |  | Unencrypted Broadcast Isochronous Stream |  |  | [7] 4.4.6.1 |  |  | M |  |  |
| 3 |  |  | Transmitting Data on Multiple Broadcast Isochronous Streams |  |  | [7] 4.4.6.3 |  |  | O |  |  |
| 4 |  |  | BN values greater than 1 |  |  | [7] 4.4.6.3 |  |  | O |  |  |
| 5 |  |  | Pre-transmission |  |  | [7] 4.4.6.6 |  |  | O |  |  |
| 6 |  |  | Create BIG from PAwR |  |  | [7] 4.4.6.2 |  |  | C.2 |  |  |

C.1: Mandatory IF LL 9/1 “LE Encryption”, otherwise Excluded.
C.2: Optional IF LL 9/49 “Periodic Advertising with Responses – Advertiser”, otherwise Excluded.

### 1.14 Channel Sounding Capabilities

Table 13: Supported Capabilities
Prerequisite: LL 9/56 “Channel Sounding”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CS Mode-1 | [12] 4.3.2 | M | [13] RFPHY 3/5 |  |  |
| 2 | CS Mode-2 | [12] 4.3.3 | M | [13] RFPHY 3/6 |  |  |
| 3 | CS Mode-3 | [12] 4.3.4 | O | [13] RFPHY 3/7 |  |  |
| 4 | CS RTT Access Address, 10 ns | [12] 3.2 | C.1 | N/A |  |  |
| 5 | CS RTT Access Address, 150 ns | [12] 3.2 | C.1 | N/A |  |  |
| 6 | CS RTT Sounding Sequence, 10 ns | [12] 3.3 | O | N/A |  |  |
| 7 | CS RTT Sounding Sequence, 150 ns | [12] 3.3 | O | N/A |  |  |
| 8 | CS RTT Random Payload, 10 ns | [12] 3.4 | O | N/A |  |  |
| 9 | CS RTT Random Payload, 150 ns | [12] 3.4 | O | N/A |  |  |
| 10 | CS SYNC LE 2M PHY _ | [12] 2 | O | [13] RFPHY 1/4 |  |  |
| 11 | No FAE | [12] 2.4.2.44 | O | N/A |  |  |
| 12 | Procedure Repeat | [12] 5.1.27 | O | N/A |  |  |
| 13 | Channel Selection #3c | [12] 4.1.4.2 | O | N/A |  |  |
| 14 | Sounding Sequence, PCT Estimate | [12] 3.3.1 | O | N/A |  |  |

C.1: Mandatory to support at least one.

### 1.15 Channel Sounding Mode Capabilities

Table 14: Channel Sounding Mode Capabilities
Prerequisite: LL 9/56 “Channel Sounding”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | T IP1, 145 µs _ |  |  | [12] 4.3.1 |  |  | M |  |  |
| 2 |  |  | T IP1, 80 µs _ |  |  | [12] 4.3.1 |  |  | C.1 |  |  |
| 3 |  |  | T IP1, 60 µs _ |  |  | [12] 4.3.1 |  |  | O |  |  |
| 4 |  |  | T IP1, 50 µs _ |  |  | [12] 4.3.1 |  |  | O |  |  |
| 5 |  |  | T IP1, 40 µs _ |  |  | [12] 4.3.1 |  |  | C.2 |  |  |
| 6 |  |  | T IP1, 30 µs _ |  |  | [12] 4.3.1 |  |  | O |  |  |
| 7 |  |  | T IP1, 20 µs _ |  |  | [12] 4.3.1 |  |  | O |  |  |
| 8 |  |  | T IP1, 10 µs _ |  |  | [12] 4.3.1 |  |  | O |  |  |
| 9 |  |  | T IP2, 145 µs _ |  |  | [12] 4.3.3 |  |  | M |  |  |
| 10 |  |  | T IP2, 80 µs _ |  |  | [12] 4.3.3 |  |  | C.3 |  |  |
| 11 |  |  | T IP2, 60 µs _ |  |  | [12] 4.3.3 |  |  | O |  |  |
| 12 |  |  | T IP2, 50 µs _ |  |  | [12] 4.3.3 |  |  | O |  |  |
| 13 |  |  | T IP2, 40 µs _ |  |  | [12] 4.3.3 |  |  | C.4 |  |  |
| 14 |  |  | T IP2, 30 µs _ |  |  | [12] 4.3.3 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 |  |  | T IP2, 20 µs _ |  |  | [12] 4.3.3 |  |  | O |  |  |
| 16 |  |  | T IP2, 10 µs _ |  |  | [12] 4.3.3 |  |  | O |  |  |
| 17 |  |  | T PM, 40 µs _ |  |  | [12] 4.3.3 |  |  | M |  |  |
| 18 |  |  | T PM, 20 µs _ |  |  | [12] 4.3.3 |  |  | C.5 |  |  |
| 19 |  |  | T PM, 10 µs _ |  |  | [12] 4.3.3 |  |  | O |  |  |

C.1: Mandatory IF LL 14/3 “T_IP1, 60 µs“ OR LL 14/4 “T_IP1, 50 µs“ OR LL 14/5 “T_IP1, 40 µs“ OR LL 14/6 “T_IP1, 30 µs“ OR LL 14/7 “T_IP1, 20 µs“ OR LL 14/8 “T_IP1, 10 µs“, otherwise Optional.
C.2: Mandatory IF LL 14/6 “T_IP1, 30 µs“ OR LL 14/7 “T_IP1, 20 µs“ OR LL 14/8 “T_IP1, 10 µs“, otherwise Optional.
C.3: Mandatory IF LL 14/11 “T_IP2, 60 µs“ OR LL 14/12 “T_IP2, 50 µs“ OR LL 14/13 “T_IP2, 40 µs“ OR LL 14/14 “T_IP2, 30 µs“ OR LL 14/15 “T_IP2, 20 µs“ OR LL 14/16 “T_IP2, 10 µs“, otherwise Optional.
C.4: Mandatory IF LL 14/14 “T_IP2, 30 µs“ OR LL 14/15 “T_IP2, 20 µs“ OR LL 14/16 “T_IP2, 10 µs“, otherwise Optional.
C.5: Mandatory IF LL 14/19 “T_PM, 10 µs”, otherwise Optional.

## 2 Mapping of LL feature bits to ICS items

This section is informative.
Not all LL features have corresponding ICS items.

|  | Feature |  |  | LL Feature Bit |  |  | ICS Item |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LE Encryption |  |  | 0 |  |  | LL 9/1 |  |  |
| Connection Parameters Request procedure |  |  | 1 |  |  | LL 9/3 |  |  |
| Extended Reject Indication |  |  | 2 |  |  | LL 9/4 |  |  |
| Peripheral-initiated Features Exchange |  |  | 3 |  |  | LL 9/5 |  |  |
| LE Ping |  |  | 4 |  |  | LL 9/2 |  |  |
| LE Data Packet Length Extension |  |  | 5 |  |  | LL 9/6 |  |  |
| LL Privacy |  |  | 6 |  |  | LL 9/13 |  |  |
| Extended Scanning Filter Policies |  |  | 7 |  |  | LL 4/6 |  |  |
| LE 2M PHY |  |  | 8 |  |  | LL 9/7 |  |  |
| Stable Modulation Index – Transmitter |  |  | 9 |  |  | LL 9/58 |  |  |
| Stable Modulation Index – Receiver |  |  | 10 |  |  | LL 9/59 |  |  |
| LE Coded PHY |  |  | 11 |  |  | LL 9/9 |  |  |
| LE Extended Advertising |  |  | 12 |  |  | LL 9/41 |  |  |
| LE Periodic Advertising |  |  | 13 |  |  | LL 9/42 |  |  |
| Channel Selection Algorithm #2 |  |  | 14 |  |  | LL 9/10 |  |  |
| LE Power Class 1 |  |  | 15 |  |  | LL 9/11 |  |  |
| Minimum Number of Used Channels procedure |  |  | 16 |  |  | LL 9/12 |  |  |
| Connection CTE Request |  |  | 17 |  |  | LL 9/14 |  |  |
| Connection CTE Response |  |  | 18 |  |  | LL 9/15 |  |  |
| Connectionless CTE Transmitter |  |  | 19 |  |  | LL 9/16 |  |  |
| Connectionless CTE Receiver |  |  | 20 |  |  | LL 9/17 |  |  |
| Antenna Switching During CTE Transmission (AoD) |  |  | 21 |  |  | LL 9/18 |  |  |
| Antenna Switching During CTE Reception (AoA) |  |  | 22 |  |  | LL 9/21 |  |  |
| Receiving Constant Tone Extensions |  |  | 23 |  |  | LL 9/20 |  |  |
| Periodic Advertising Sync Transfer – Sender |  |  | 24 |  |  | LL 9/26 |  |  |
| Periodic Advertising Sync Transfer – Recipient |  |  | 25 |  |  | LL 9/27 |  |  |
| Sleep Clock Accuracy Updates |  |  | 26 |  |  | LL 9/30 |  |  |
| Remote Public Key Validation |  |  | 27 |  |  | LL 9/25 |  |  |
| Connected Isochronous Stream – Central |  |  | 28 |  |  | LL 9/31 |  |  |
| Connected Isochronous Stream – Peripheral |  |  | 29 |  |  | LL 9/32 |  |  |
| Isochronous Broadcaster |  |  | 30 |  |  | LL 9/33 |  |  |
| Synchronized Receiver |  |  | 31 |  |  | LL 9/34 |  |  |
| Connected Isochronous Stream (Host Support) |  |  | 32 |  |  | See below |  |  |
| LE Power Control Request |  |  | 33 |  |  | LL 9/37 |  |  |
| LE Power Control Request (duplicate) |  |  | 34 |  |  | LL 9/37 |  |  |
| LE Path Loss Monitoring |  |  | 35 |  |  | LL 9/39 |  |  |


|  | Feature |  |  | LL Feature Bit |  |  | ICS Item |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Periodic Advertising ADI support |  |  | 36 |  |  | LL 9/43 |  |  |
| Connection Subrating |  |  | 37 |  |  | LL 9/45 |  |  |
| Connection Subrating (Host Support) |  |  | 38 |  |  | See below |  |  |
| Channel Classification |  |  | 39 |  |  | LL 9/44 |  |  |
| Advertising Coding Selection |  |  | 40 |  |  | LL 9/48 |  |  |
| Advertising Coding Selection (Host Support) |  |  | 41 |  |  | See below |  |  |
| Decision-Based Advertising Filtering |  |  | 42 |  |  | LL 9/51 |  |  |
| Periodic Advertising with Responses – Advertiser |  |  | 43 |  |  | LL 9/49 |  |  |
| Periodic Advertising with Responses – Scanner |  |  | 44 |  |  | LL 9/50 |  |  |
| Unsegmented Framed Mode |  |  | 45 |  |  | LL 9/53 |  |  |
| Channel Sounding |  |  | 46 |  |  | LL 9/56 |  |  |
| Channel Sounding (Host Support) |  |  | 47 |  |  | See below |  |  |
| Channel Sounding Tone Quality Indication |  |  | 48 |  |  | LL 9/57 |  |  |
| LL Extended Feature Set |  |  | 63 |  |  | LL 9/55 |  |  |
| Monitoring Advertisers |  |  | 64 |  |  | LL 9/52 |  |  |
| Frame Space Update |  |  | 65 |  |  | LL 9/54 |  |  |

Table 2.1: Mapping of LL feature bits to ICS items
Feature bits with “(Host Support)” in the name are set at run-time by the Host; therefore, they do not have a corresponding ICS entry. Tests that check that feature masks match the ICS should ignore these bits.

## 3 PDU Support table


| PDU | Supported if |  | Permitted to send in role |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Central |  |  | Peripheral |  |
| LL CONNECTION UPDATE IND _ _ _ | Mandatory | Yes |  |  | No |  |  |
| LL CHANNEL MAP IND _ _ _ | Mandatory | Yes |  |  | No |  |  |
| LL TERMINATE IND _ _ | Mandatory | Yes |  |  | Yes |  |  |
| LL ENC REQ _ _ | LL 9/1 | Yes |  |  | No |  |  |
| LL ENC RSP _ _ | LL 9/1 | No |  |  | Yes |  |  |
| LL START ENC REQ _ _ _ | LL 9/1 | No |  |  | Yes |  |  |
| LL START ENC RSP _ _ _ | LL 9/1 | Yes |  |  | Yes |  |  |
| LL UNKNOWN RSP _ _ | Mandatory | Yes |  |  | Yes |  |  |
| LL FEATURE REQ _ _ | Mandatory | Yes |  |  | No |  |  |
| LL FEATURE RSP _ _ | Mandatory | Yes |  |  | Yes |  |  |
| LL PAUSE ENC REQ _ _ _ | LL 9/1 | Yes |  |  | No |  |  |
| LL PAUSE ENC RSP _ _ _ | LL 9/1 | Yes |  |  | Yes |  |  |
| LL VERSION IND _ _ | Mandatory | Yes |  |  | Yes |  |  |
| LL REJECT IND _ _ | Mandatory | Yes |  |  | Yes |  |  |
| LL PERIPHERAL FEATURE REQ _ _ _ | LL 9/5 | No |  |  | Yes |  |  |
| LL CONNECTION PARAM REQ _ _ _ | LL 9/3 | Yes |  |  | Yes |  |  |
| LL CONNECTION PARAM RSP _ _ _ | LL 9/3 | Yes |  |  | Yes |  |  |
| LL REJECT EXT IND _ _ _ | LL 9/4 | Yes |  |  | Yes |  |  |
| LL PING REQ _ _ | LL 9/2 | Yes |  |  | Yes |  |  |
| LL PING RSP _ _ | LL 9/2 | Yes |  |  | Yes |  |  |
| LL LENGTH REQ _ _ | LL 9/6 | Yes |  |  | Yes |  |  |
| LL LENGTH RSP _ _ | LL 9/6 | Yes |  |  | Yes |  |  |
| LL PHY REQ _ _ | LL 9/6a | Yes |  |  | Yes |  |  |
| LL PHY RSP _ _ | LL 9/6a | No |  |  | Yes |  |  |
| LL PHY UPDATE IND _ _ _ | LL 9/6a | Yes |  |  | No |  |  |
| LL MIN USED CHANNELS IND _ _ _ _ | LL 9/12 | No |  |  | Yes |  |  |
| LL CTE REQ _ _ | LL 9/14 | Yes |  |  | Yes |  |  |
| LL CTE RSP _ _ | LL 9/15 | Yes |  |  | Yes |  |  |
| LL PERIODIC SYNC IND _ _ _ | LL 9/26 OR LL 9/27 | LL 9/26 |  |  | LL 9/27 |  |  |
| LL CLOCK ACCURACY REQ _ _ _ | LL 9/30 | Yes |  |  | Yes |  |  |
| LL CLOCK ACCURACY RSP _ _ _ | LL 9/30 | Yes |  |  | Yes |  |  |
| LL CIS REQ _ _ | LL 9/31 OR LL 9/32 | Yes |  |  | No |  |  |
| LL CIS RSP _ _ | LL 9/31 OR LL 9/32 | No |  |  | Yes |  |  |
| LL CIS IND _ _ | LL 9/31 OR LL 9/32 | Yes |  |  | No |  |  |
| LL CIS TERMINATE IND _ _ _ | LL 9/31 OR LL 9/32 | Yes |  |  | Yes |  |  |
| LL POWER CONTROL REQ _ _ _ | LL 9/37 | Yes |  |  | Yes |  |  |
| LL POWER CONTROL RSP _ _ _ | LL 9/37 | Yes |  |  | Yes |  |  |
| LL POWER CHANGE IND _ _ _ | LL 9/37 | Yes |  |  | Yes |  |  |


| PDU | Supported if |  | Permitted to send in role |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Central |  |  | Peripheral |  |
| LL SUBRATE REQ _ _ | LL 9/45 | No |  |  | Yes |  |  |
| LL SUBRATE IND _ _ | LL 9/45 | Yes |  |  | No |  |  |
| LL CHANNEL REPORTING IND _ _ _ | LL 9/44 | Yes |  |  | No |  |  |
| LL CHANNEL STATUS IND _ _ _ | LL 9/44 | No |  |  | Yes |  |  |
| LL PERIODIC SYNC WR IND _ _ _ _ | LL 9/49 OR LL 9/50 | LL 9/49 |  |  | LL 9/50 |  |  |

Table 3.1: PDU Support table

## 4 References

[1] Specification of the Bluetooth System, Volume 6, Part B, Version 4.0 or later
[2] Specification of the Bluetooth System, Volume 6, Part B, Version 4.1 or later
[3] Specification of the Bluetooth System, Volume 6, Part B, Version 4.2 or later
[4] Specification of the Bluetooth System, Volume 6, Part B, Version 5.0 or later
[5] Erratum 10734: Pairing Updates
[6] Specification of the Bluetooth System, Volume 6, Part B, Version 5.1 or later
[7] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification), Version 5.2 or later
[8] Specification of the Bluetooth System, Volume 4, Part E (Host Controller Functional Specification), Version 5.2 or later
[9] Core Specification Supplement (CSS), Part A, Current Version
[10] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification),
Version 5.3 or later
[11] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification),
Version 5.4 or later
[12] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification),
Version 6.0 or later
[13] ICS Proforma for Radio Frequency Physical Layer (RFPHY)

## 5 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | 4.0.0r9 |  |  | 2009-12-15 | Change of name and reference to Spec version 4.0 |
|  |  |  | 4.0.1r0 |  |  | 2010-11-24 | TSE 3634: add 6/20 TSE 3927: rename LL 3/6 (discoverable scan) |
|  |  |  | 4.0.1r1 |  |  | 2011-04-11 | Edits by Miles Smith |
| 1 |  |  | 4.0.1 |  |  | 2011-07-1 | Prepare for publication. |
|  |  |  | 4.0.2r0 |  |  | 2011-11-08 | TSE 4518: Table 3, Table 4. Remove Conditional footnotes. Change statuses to M |
| 2 |  |  | 4.0.2 |  |  | 2012-03-30 | Prepare for publication. |
|  |  |  | 4.0.3r1 |  |  | 2013-05-30 | TSE 5169: Table 3 Updates Changed item 1 to “C.1” Changed item 2 to “C.2” Changed item 4 to “C.3” Changed item 5 to “C.4” Added note to the table, and defined the conditionals added. Table 4 Updates Changed item 1 to “C.1” Changed item 3 to “C.2” Added note to the table and defined the conditionals added. |
| 3 |  |  | 4.0.3 |  |  | 2013-07-02 | Prepare for Publication |
|  |  |  | 4.0.4rT |  |  | 2013-08-07 | Template Conversion Updated conditional wording to match current language. |
|  |  |  | 4.0.4rTr3 |  |  | 2013-09-25 | Template Conversion Comment Resolution |
|  |  |  | 4.1.0r01 |  |  | 2013-09-25 | Low Duty Cycle Directed Advertising CR |
|  |  |  | 4.1.0r02 |  |  | 2013-10-01 | TSE 5343: Removed statements following Table 6 and Table 7. Updated items 6/5, 6/6, 6/8, 6/9, 7/5 and 7/6. TSE 5201: Updated Table 8, Item 1 capability to "Data channels (channel index 0 to 36)", reference to 1.4.1 and status from "M" to "C.1" |
|  |  |  | 4.1.0r03 |  |  | 2013-10-10 | LE Ping CR |
|  |  |  | 4.1.0r04 |  |  | 2013-10-14 | TSE 5342: Updated item 4/5 to M, updated text for C.2 and added a comment for GAP role support and removed comment about active scanning for table 4. |
|  |  |  | 4.1.0r05 |  |  | 2013-10-14 | LE Link Layer Topology CR |
|  |  |  | 4.1.0r08 |  |  | 2013-11-06 | Comment Resolution |
| 4 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.1.1r00 |  |  | 2014-04-10 | TSE 5602: Added Table 9 C.5, and updated Status for 9/5 to C.5. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 4.1.1r01 |  |  | 2014-06-22 | Editorial correction to Table 3, C.4 added extra space. |
| 5 |  |  | 4.1.1 |  |  | 2014-07-07 | TCRL 2014-1 Publication |
|  |  |  | 4.2.0r00 |  |  | 2014-11-14 | Integrated changes from Section 2 and Section 5 of Core LE Data Length Extensions TEST.CRr01 and _ _ _ _ _ section 1.8 of Core Enhanced Privacy 1 2.TS.CR.R05. _ _ _ _ |
|  |  |  | 4.2.0r01 |  |  | 2014-11-20 | Integrated reviews by Mayank, Jason, Rasmus. |
| 6 |  |  | 4.2.0 |  |  | 2014-12-04 | Prepare for TCRL 2014-2 publication |
|  |  |  | 4.2.1r00 |  |  | 2015-05-06 | TSE 6159: Corrected status of 3/6 and 3/7 to C.2 TSE 6280: Updated C.2 in Table 1 by completing the conditional expression |
|  |  |  | 4.2.1r01 |  |  | 2015-06-05 | Deleted Section 1.2 (Global Statement of Conformance) per current ICS template standards. |
| 7 |  |  | 4.2.1 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 4.2.2r00 |  |  | 2015-10-13 | TSE 6608: Corrected wording for LL 8/2 capability. TSE 6472: Removed item LL 7/18 (Master Non- Connectable Events) |
| 8 |  |  | 4.2.2 |  |  | 2015-12-22 | Prepared for TCRL 2015-2 publication. |
|  |  |  | 5.0.0r00 |  |  | 2016-06-01 | Integrated changes for Core Specification 5.0 release |
|  |  |  | 5.0.0r00 |  |  | 2016-07-07 | Integrated changes for Core Specification 5.0 release |
|  |  |  | 5.0.0r01 |  |  | 2016-08-30 | Issue 7532: Updated Table 3: Deleted row 12. Renumbered row 13 and 14 to 12 and 13, respectively. Deleted conditional C.8. Conditional C.9 renumbered to C.8. Issue 7533: Updated Table 5: Deleted Item 12, “Requesting in Events” subheading, and conditional C.1. Issue 7534: Updated “TBD” references in Table 3, 4, 6, 7, and 9. Table 5 "TBD" reference deleted (Issue 7533). Reference for “High Duty Cycle Non Connectable Advertising (Item 3/13) intentionally not updated. This reference will be addressed in a separate Issue. |
|  |  |  | 5.0.0r02 |  |  | 2016-09-20 | Issue 7633: Updated conditional C.5 for both Tables 6 and 7. Issue 7572: Deleted item LL 3/13 (High Duty Cycle Non-Connectable Advertising) and conditional C.8. Issue 7682: Deleted reference to item LL 9/11 from conditional C.5 for Table 6 and Table 7. |
|  |  |  | 5.0.0r03 |  |  | 2016-10-06 | TSE 7057: Updated status of LL.ICS 6/21 and conditionals C.2 and C.5. Updated capability and status of LL.ICS 7/21 and conditional C.5. Deleted conditional C.2 for Table 9. All conditionals and statuses above C.1 for Table 9 remapped accordingly (3 → 2; 4 → 3; 5 → 4…), except Item 2, which was remapped to conditional C.4. TSE 6899: Deleted items 6/8, 6/9, 7/8, and 7/9. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.0.0r04 |  |  | 2016-11-09 | TSE 7833: Added two new items and conditional statement C.4 to Table 2. |
|  |  |  | 5.0.0r05 |  |  | 2016-11-11 | Issue 7884: Global edit. Added support in conditionals for Core Spec version 5.0. Minor editorial changes. |
|  |  |  | 5.0.0r06 |  |  | 2016-11-14 | Updated to current template. Removed unnecessary parentheses and replaced with quotation marks. Editorial re-writes to Conditional logic to future proof Core versioning increments. Conditionals affected: Table 2: C.1, C.2; Table 3: C.5, C.6; Table 4: C.3, C.4; Table 6: C.1, C.2, C.3; Table 7: C.1, C.2, C.3; Table 9: C.2, C.3, C.4, C.5, C.6, C.8. Added the note appearing after Table 4 to Table 3. Revised the affected Conditionals to state “otherwise Optional” rather than “otherwise Excluded” to agree with the note. |
| 9 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.0.1r00 |  |  | 2017-03-23 | TSE 7385: Updated conditional statements C.1 to include “at least” for Table 1 and 2. TSE 8259: Changed 6/23 reference from 4.6.16 to 4.6.15. Not part of TSE 8259 but same problem applies as 4.6.16 is not in spec. Changed 7/23 reference from 4.6.16 to 4.6.15. TSE 8260: Updated 6/23 and 7/23 status from C.5 to C.6 and added conditional C.6 to Table 6 and 7. TSE 8261: Changed from PHY to Connections for Table 9/8. TSE 8274: Changed from LL to LE for Table 9/1. Changed the Reference from [5] 4.6.15 to [5] 4.6 and the Status from C.7 to C.9 for Table 9/11. Added additional Item 12 to Table 9. Replaced “are supported” with “otherwise Excluded” to C.1 for Table 9. Replaced last part of C.8 for Table 9 from “OR LL 9/11 “LE Power Class 1” is supported, otherwise Optional.” to “AND (LL 1/4 “Slave Role” OR LL 1/5 “Master Role” OR LL 3/10 “Periodic Advertising” OR LL 4/8 “Periodic Scanning”), otherwise Optional.” Added Conditionals (C.9 and C.10) to Table 9. |
|  |  |  | 5.0.1r01 |  |  | 2017-04-19 | Integrated review comments on TSE 8260: Updated C.6 in Tables 6 and 7. TSE 9304: Introductory statements deleted from all tables. (Note, 17 Aug 2017: Incorporated as editorial update for TCRL 2017-1 release.) |
|  |  |  | 5.0.1r02 |  |  | 2017-06-11 | Reverted C.6 for Minimum Number of Used Channels Procedure in Tables 6 and 7. Conditional statement changed back to: Excluded IF SUM ICS 21/9 “Core v4.0” OR SUM ICS 21/13 “Core v4.1” OR SUM ICS 21/14 “Core v4.2” is supported, otherwise Optional. |
| 10 |  |  | 5.0.1 |  |  | 2017-07-05 | Approved by BTI. Prepared for TCRL 2017-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.0.2.r00 |  |  | 2017-08-22 | TSE 9699: Deleted text from Table 2: Device Address Types note C.1. |
|  |  |  | 5.0.2.r01 |  |  | 2017-09-15 | TSE 9217: Revised privacy requirements in Tables 2 and 9. For Table 2, changed status of LL 2/7, modified conditional C.4, and added conditional C.5. For Table 9, added row 13 ("LL Privacy"). TSE 9776: Removed redundancy from conditional statements in Tables 3 and 4. |
|  |  |  | 5.0.2.r02 |  |  | 2017-09-22 | AoA/AoD: Added items and conditionals to Tables 3, 6, 7, and 9. Added Table 11: Synchronized State. |
|  |  |  | 5.0.2r03 |  |  | 2017-10-19 | TSE 9899: Updated the “Protocol Scanning Features” table. |
| 11 |  |  | 5.0.2 |  |  | 2017-12-07 | Approved by BTI. Prepared for TCRL 2017-2 publication. |
|  |  |  | 5.0.3r00-03 |  |  | 2018-03-12 – 2018-06-14 | TSE 9991 (rating 2): Added item 23a and table note C.9 in Tables 6 and 7. Added item 6a and table note 6a and revised table note 7 in Table 9. TSE 10357 (rating 1): Globally replaced “Periodic Scanning” with “Scanning for Periodic Advertising”. TSE 10080 (rating 2): Revised Conditional C.6 in Table 3 and C.4 in Table 4 to remove LE Coded PHY. Editorial revisions of references in Table 9 items 9/7 and 9/9. Incorporated Core E10734 Pairing Updates TS CR: Added item 9/25 and C.20. |
| 12 |  |  | 5.0.3 |  |  | 2018-07-02 | Approved by BTI. Prepared for TCRL 2018-1 publication. |
|  |  |  | 5.0.4r00-r04 |  |  | 2018-07-16 - 2018-11-12 | Incorporated Core PAST CLE TEST CR r05: _ _ _ _ _ Table 1: Added row 3a and conditional note C.4. LL 4/8, C.5: Added support for SUM ICS 21/16 "Core v5.0". Table 6: Added rows 26–30 and conditional notes C.10–C.14. Table 7: Added rows 26–30 and conditional notes C.10–C.14. Table 9: Added rows 26–29 and conditional notes C.21–C.23. Section 1.12: Added section introductory text. Table 11: Added row 1. Incorporated Core Minor Enhancements Batch 1 Test CRr10-clean: Added item 31 and conditional note C.15 to both Tables 6 and 7. Added item 30 and conditional note C.24 to Table 9. Issue 10710: Added cross-reference section "4.6.X" to LL 6/31, LL 7/31, and LL 9/30. Added reference [7] for Bluetooth 5.1 and updated TBD and [x] values. Production edits: Deleted “Core Madrid Feature Notation (Gray Text)” section. For all new Madrid (5.1) text, changed style from gray to black. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number from 5.0.4 to 5.1.0 to align with the adoption of Core Specification version 5.1. |
| 13 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | 5.1.1r00–r03 |  |  | 2019-04-01– 2019-05-23 | TSE 11546 (rating 1): Changed C.1 in Table 6 to “No longer used.” TSE 11165 (rating 2): For Table 3, updated status for item 10 and text in note C.6 and added note C.9. For Table 4, updated notes C.4 and C.5. For Table 5, added a new item and a new note. For Table 9, added items 9a and 9b, modified note C.8, and added notes C.25 and C.26. TSE 11791 (rating 2): Updated Table 9 items 15 and 21 “Status” column, and modified and added conditionals to accommodate changes made to RFPHY layer for this TSE. TSE 12099 (rating 2): Removed references to deprecated Core Specification versions in tables affected by TSE 11165 and 11791 updates (Tables 3, 4, 6, 9). |
| 14 |  |  | 5.1.1 |  |  | 2019-08-01 | Approved by BTI. Prepared for TCRL 2019-1 publication. |
|  |  |  | p15r00–r10 |  |  | 2019-08-05 – 2019-12-05 | Added test groups to accommodate adoption of Core Specification v5.2 with regard to Isochronous Channels CR r20 (includes Issues 11742, 11762, 11777, 11778, 11779, 11783,11786, 11804, 11817, 11819, 11820, 11852, 11917, 11919, 11928, 11929, 11930, 11983, 11740, 11801, 11941, 12029, 12030, 12043, 12052, 12053, 12054, 12055, 12059, 12061, 12071, 12072, 12073, 12077, 12084, 12031, 12078, 12094, 12095, 12106, 12107, 12130, 12132, 12133, 12251, 12280, and 12321). Added item 6 and note C.6 to Table 1; Added items 32 and 33 and note C.16 to Table 6; added items 32 and 33 and note C.16 to Table 7; added items 31–36 and notes C.28–C.33 to Table 9; added items 3 and 4 and note C.2 to Table 11; added section “Isochronous Broadcasting Features”; updated references section with new Core Specification. Added test groups to accommodate adoption of Core Specification v5.2 with regard to LE Power Control CR r07 (includes Issues 12116, 12112, 12115, 12117, 12118, 12255). Added items 37–39 and notes C.34– C.36 to Table 9. TSE 12501 (rating 1): Changed item 2 in Table 9 to optional. TSE 12607 (rating 2): Updated conditionals in Tables 1, 2, and 7 to remove references to deprecated and/or withdrawn core specs and to fix an editorial issue with conditionals no longer used. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 12065 (rating 3): Updated rows and conditionals in Table 3, updated conditionals only in Tables 6 and 7, and added a new row and conditional to Table 9 to account for missing features in Link Layer. TSE 12034 (rating 2): Updated Table 9 conditionals. TSE 12605 (rating 2): Updated rows 12 and 18 and added a conditional in Table 6; updated rows 12 and 19 and added a conditional in Table 7; updated row 1 and changed C.1 to “No longer used” in Table 9. TSE 12778 (rating 2): Updated Conditional and reference for item 9/25 to align with the current SUM ICS. Removed C.20, which required support for Erratum 10734 that was not future-proof. Conditional is now just Optional. IAL restructure: Removed “Isochronous Adaptation Layer” item and associated conditional C.2 from Table 12. TSE 12428 (rating 4): Added item 12a and conditional C.11 to Table 3. Added reference for “Supplement to Bluetooth Core Specification, Part A, Version 7 or later” to References section. TSE 11709 (rating 2): Updated C.4 for Table 1; updated item 10 and note C.6 and added note C.12 to Table 3; updated notes C.4 and C.5 for Table 4; added items 41 and 42 and notes C.38 and C.39 for Table 9; updated item 1 and added note C.3 for Table 11. Removed deprecated specs from 1:C.5, 9:C.28, 9:C.29, 9:C.31, 9:C.34–C.36, and 9:C.38 (“SUM ICS 21/9 “Core v4.0” OR SUM ICS 21/13 “Core v4.1” OR “) per integration review feedback when prepping 2019-2 for Launch Studio. Resolved .X and Milan references with real numbers. Backed out errant addition of item C.16a for 12034, which was added as C.27 in TCRL 2019-1. Revised document numbering convention, setting last release publication of 5.1.1 as p14; added publication number column to Revision History. Updated Contributors list. |
| 15 |  |  | p15 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p16r00–r24 |  |  | 2020-01-29 – 2021-06-21 | TSE 13062 (rating 2): Updated C.6 in Tables 6 and 7; updated Capability name of Item 3 and revised C.10 of Table 9. TSE 13333 (rating 2): Updated C.32 conditional note for Table 9 to fix dependencies. TSE 13361 (rating 2): Updated C.13 and C.14 conditionals in Tables 6 and 7 to align with updated spec. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 14629 (rating 2): Updated conditionals for Tables 6 and 7 and updated for appropriate items’ Status column to address requirements for Peripheral- initiated features exchange. TSE 14664 (rating 3): Added C.20 to Table 6 and updated item 33’s status with new conditional; updated text of C.16 for Tables 6 and 7; added item 46 and C.42 to Table 9; updated text of C.2, added C.4, and updated status of item 4 in Table 11; added new Table 11a; and added items 3, 4, and 5 to Table 12. TSE 14679 (rating 4): Added item 47 and C.43 to Table 9. TSE 14853 (rating 2): Updated conditionals for Table 12 items 1 and 2 to include LE Encryption dependencies. TSE 14907 (rating 2): Updated C.4 for Table 1 and C.3 for Table 11. TSE 15046 (rating 2): Updated Table 9 by modifying items 37–39 and notes C.34–C.36 to address Erratum 15010, regarding updates to the LL feature bits for LE Power Control. TSE 15451 (rating 1): Editorials to address Erratum 15334, globally change “Master” to “Central” and “Slave” to “Peripheral”. TSE 16758 (rating 2): To address E16372 regarding Transmit Power Level for Power Class, updated C.9 for Table 9. TSE 17009 (rating 3): Added item 9/39a for LE Path Loss Monitoring when the path loss becomes unavailable. TSE 17082 (rating 1): Added item 2/2 to C.1 in Table 2. TSE 17096 (rating 1): Added LL 3/3a and corresponding C.13 (Gene’s CR in 73492). Incorporated ADI In Periodic Advertising Test CR r06: Added _ _ _ _ _ _ “Periodic Advertising ADI support” item to Table 9 as well as associated conditional, and added a new reference to the v5.3 Core spec. Incorporated Enhanced Connection Update TEST CR r17: _ _ _ _ _ Added LL 9/45, referencing conditional and reference from other previously incorporated v5.3 CRs. Incorporated LE Channel Classification TEST CR r07: added _ _ _ _ _ new items and associated conditionals to Tables 6, 7, and 9. Template-related and consistency checker editorials. |
| 16 |  |  | p16 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p17r00–r02 |  |  | 2021-09-14 – 2022-01-03 | TSE 17274 (rating 2): Updated C.13 of Table 3. TSE 17285 (rating 2): Updated C.1 and C.9 of Table 3; updated C.1 and C.2 of Table 4 and status of items 3 and 4. TSE 17415 (rating 2): Updated C.13 of Table 6 and C.14 of Table 7. TSE 17488 (rating 2): Fixed capability name of item 37 and updated C.3 for Table 9. TSE 17491 (rating 2): To address an issue with the presentation of periodic and extended advertising: Table 5: updated C.1; Table 9, deleted items 9a and 9b and related C.25 and C.26, and updated C.8 and C.40. Consistency checker editorials. Updated copyright page to align with v2 of the DNMD. Updated table spacing to align with latest ICS template. |
| 17 |  |  | p17 |  |  | 2022-01-25 | Approved by BTI on 2021-12-27. Prepared for TCRL 2021-2 publication. |
|  |  |  | p17ed2 r00–r02 |  |  | 2022-01-28 – 2022-03-07 | TSE 17948 (rating 1): Removed redundant “LL 1/3a” from C.3 of Table 11. Consistency checker editorials. |
|  |  |  | p17 edition 2 |  |  | 2022-03-07 | Approved by BTI on 2022-03-07. Prepared for edition 2 publication. |
|  |  |  | p18r00–r01 |  |  | 2022-03-29 – 2022-04-05 | TSE 18323 (rating 2): Updated C.19 for Table 9 to correct conditions for AoD receive. TSE 18642 (rating 1): Updated items 1, 2, and 3 and C.1 for Table 8 and added C.2. Updated C.8 for Table 9. |
| 18 |  |  | p18 |  |  | 2022-06-28 | Approved by BTI on 2022-05-31. Prepared for TCRL 2022-1 publication. |
|  |  |  | p18ed2 r00–r02 |  |  | 2022-07-19 – 2022-08-22 | TSE 19152 (rating 1): Updated description of item 1 in Table 12 to align with grammar used in the subsequent item. Editorials, including punctuation changes, making “no longer used” language consistent, and removing unused references, including the reference to the Appropriate Language Mapping Tables document (if needed, it can be found at the link in this revision history comment). |
|  |  |  | p18 edition 2 |  |  | 2022-08-23 | Approved by BTI on 2022-08-22. Prepared for edition 2 publication. |
|  |  |  | p19r00–r08 |  |  | 2022-08-24 – 2022-12-19 | TSE 19123 (rating 2): Updated references for 9/19, 9/20, and 9/23. TSE 19329 (rating 3): Added new item 10/3. TSE 19332 (rating 2): Updated items 10/1 and 10/2 with new conditionals C.1 and C.2. TSE 20527 (rating 3): Added a new item 7/32a and conditional C.20 to Table 7 and updated 7/32, 7/33, and C.16. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 20646 (rating 3): Per E18415/18311, updated C.4 and C.5 in Table 1; added 3/10a and related C.14; added 4/8a and related C.7; updated 6/10a status and related C.2 and added 6/28a and related C.21; updated 7/10b and related C.2 and added 7/28a and related C.21; updated 9/4, 9/10, 9/26, 9/28, 9/29, 9/30 statuses and C.2, C.4, C.5, C.11, C.21, C.22, C.28, C.29, C.30, C.31, C.33, C.34, C.38, C.39, C.40, and deleted C.3, C.8, C.24, and added 9/49 and 9/50 and related C.45 and C.46. TSE 22132 (rating 1): Corrected the CSS citation in the references. Core v5.4 CR: CSSA (from CR Coding Scheme Selection on _ _ _ _ Advertising Test CR r08, including E18415 and _ _ _ E19196): Added item 9/48 and related C.44. Added v5.4 reference to Core in References. |
| 19 |  |  | p19 |  |  | 2023-02-07 | Approved by BTI on 2022-12-28. Prepared for TCRL 2022-2 publication. |
|  |  |  | p20r00–r02 |  |  | 2023-04-10 – 2023-05-26 | TSE 22259 (rating 2): Updated the status of 3/7 and added conditional C.3. TSE 22719 (rating 2): Added items 6/26a and associated conditional C.22 and 7/26a and associated conditional C.22. TSE 22916 (rating 1): Corrected the reference for LE Channel Classification in 9/44. |
| 20 |  |  | p20 |  |  | 2023-06-29 | Approved by BTI on 2023-06-05. Prepared for TCRL 2023-1 publication. |
|  |  |  | p21r00–r05 |  |  | 2023-09-28 – 2023-11-13 | TSE 18402 (rating 2): Updated Table 3 conditionals C.1 and C.2 and Table 4 C.1 and removed old “Comments” after the conditionals list in both tables. TSE 24075 (rating 2): Replaced SUM ICS references with CORE ICS references. In Table 1, removed the prerequisite and updated C.4 (affecting 1/3a). In Table 2, updated C.5 (affecting 2/7). In Table 6, updated C.9 (affecting 6/23a). In Table 7, updated C.9 (affecting 7/23a). In Table 9, updated C.4, C.5, C.10– C.12, C.22, C.23, C.28–C.30, C.34, C.37, C.38, C.40, C.41, and C.44–C.46 (affecting 9/7, 9/9, 9/10, 9/12, 9/14–9/16, 9/21, 9/26, 9/27, 9/30–9/34, 9/37, 9/39– 9/41, 9/43–9/45, and 9/48–9/50). Removed draft (pre-p0) revision history entries per current BTI conventions. |
| 21 |  |  | p21 |  |  | 2024-07-01 | Approved by BTI on 2024-XX-XX. Prepared for TCRL 2024-1 publication. |

p22r00–r22 2024-05-20 – 2024-07-31
Incorporated changes from Decision_Based_ Advertising_Filtering_TEST_CR_r17: In Table 3, added Item 3/14 and note C.15. In Table 5, added Item 4/9 and note C.8. In Table 9, added Item 9/51 and note C.47. Integrated the following test issues for Core v6.0: 20399 (TI 18581, 18583, 18584, 18928, 19316, 19330, 19331), 20408, 20411 – 20415, 20418, 20462, 20468, 20517, 20523, 20555, 20563, 20565, 22454, 22455, 22472, 22497, 22907, 22915, 23436, 24156, and 24788. Incorporated changes from Monitoring Advertising_Test_CR_r02: In Table 9, added Item 9/51 and note C.48. Updated the references list. Updated reference in Table 9, C.47, from SUM ICS to CORE ICS per updated CR. Incorporated CR Enhancements_for_ISOAL_TEST_CR_r12-jorg (which includes Test Issues 22481, 22725, 23116, 23360, 23385, 23913, 23920, 24024, 24096, 24828, 24829, 24830, 24937). To account for the Enhancements for ISOAL feature in Core Specification v6.0, updated References to include Core v6.0 LL layer, added 9/53 with new associated conditional C.49. Incorporated CR Frame Space Update_Test_CR_r08 (which includes Test Issues 25371, 25444, 25452, 25453, 25470, 25471, 25475). To account for the Frame Space Update feature in Core Specification v6.0, updated References to include Core v6.0 LL layer, added 9/54 with new associated conditional C.50. Incorporated CR Core_LLExtendedFeatureSet_Test_CRr11-Jorg (which includes Test Issues 24450, 24696, 24807, 24896, 24905). To account for the Low Energy Extended Feature Set feature in Core Specification v6.0, added a reference to Core v6.0 and added 9/55 with accompanying conditional C.51. Updated C.18 in Tables 6 and 7 to add the new 9/55. Incorporated the changed parts of the Monitoring Advertising_Test_CR_r03 (changes only for Test Issue 25248). Incorporated CR CS_Test_CR_r16-jorg (which includes Test Issues 23205, 23293, 23331, 23332, 23361, 23362, 23363, 23364, 23365, 23378, 23379, 23381, 23382, 23384, 23404, 23419, 23422, 23424, 23425, 23500, 23501, 23502, 23503, 23504, 23506, 23594, 23693, 23694, 23696, 23701, 23706, 23711, 23732, 23736, 23737, 23738, 23776, 23842, 23923, 23993, 24023, 24033, 24043, 24049, 24133, 24135, 24137, 24138, 24139, 24141, 24142, 24143, 24146, 24147, 24149, 24150, 24151, 24153, 24177, 24181, 24231, 24232, 24330, 24331, 24332, 24410, 24411, 24418, 24419, 24478, 24483, 24515, 24531, 24599, 24601, 24602, 24614, 24618, 24619, 24621, 24623, 24624, 24625, 24627, 24630, 24639, 24645, 24646, 24655, 24656, 24657, 24659, 24660, 24669, 24681,

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | 24717, 24769, 24776, 24789, 24808, 24809, 24838, 24844, 24850, 24867, 24868, 24893, 24894, 24895, 25028, 25029, 25040, 25042, 25053, 25055, 25111, 25112, 25120, 25139, 25140, 25141, 25142, 25143, 25148, 25149, 25150, 25157, 25166, 25209, 25240, 25278, 25282, 25299, 25428, 25443, 25479, 25498, 25511, 25512, 25525, 25585, 25617, 25632). To account for the Channel Sounding feature of Core v6.0, added references to Core Vol. 6 Part B and Vol. 4 Part E, added 1/7 and 1/8 and related C.6, added 9/56 and 9/57 with related C.52 and C.53, and added new Tables 13 and 14. TSE 22164 (rating 3): Per E25486, added items 9/58 and 9/59 and related conditionals C.54 and C.55. Also added a new section/table for mapping of LL feature bits to ICS items. TSE 22898 (rating 4): Added a “PDU Support” table. Updated .X references. TSE 23586 (rating 4): Per E23069, added 12/6 and related conditional C.2. TSE 24877 (rating 2): Per E17874, added Core v6.0 references to 3/1, 3/1a, 3/2, 3/4, 3/4b, 3/5, and 3/5a; updated the conditionals for 3/1a, 3/2, 3/4, 3/4b, 3/5a; updated the wording of Table 3 C.1; added new Table 4a with items 4a/1 – 4a/7 and conditionals C.1–C.7. TSE 25572 (rating 2): Removed the prerequisite from Table 2 and assigned text to C.3, setting it as the Status for 2/3 and 2/4. TSE 25573 (rating 2): Updated conditional for LL 9/13 “LL Privacy” from O to C.56. TSE 25793 (rating 2): Added new items 9/60, 9/61, and 9/62 and related conditionals C.57, C.58, and C.59. Incorporated TIs 25248, 25302, 25538, 25746, 25785. Captured BTI comments from 2024-07-31 ad hoc and cleaned up title page. Incorporated integration review feedback and made template-related editorial updates. |
| 22 |  |  | p22 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Antonio Narváez |  |  | AT4 wireless |  |  |
| Elisa Rincón |  |  | AT4 wireless |  |  |
| Bogdan Alexandru |  |  | Bluetooth SIG, Inc. |  |  |
| Alexandru Andreescu |  |  | Bluetooth SIG, Inc. |  |  |
| Nathan Burns |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Jeff Drake |  |  | Bluetooth SIG, Inc. |  |  |
| Tharon Hall |  |  | Bluetooth SIG, Inc. |  |  |
| Norbert Grunert |  |  | Broadcom |  |  |
| Mayank Batra |  |  | Cambridge Silicon Radio |  |  |
| Magnus Sommansson |  |  | Cambridge Silicon Radio |  |  |
| Fabien Duvoux |  |  | Ellisys |  |  |
| Kyle Penri-Williams |  |  | Ellisys |  |  |
| Clement Vacheron |  |  | Ellisys |  |  |
| Mika Kasslin |  |  | Nokia |  |  |
| Martti Söderlund |  |  | Nokia (TietoEnator) |  |  |
| Miles Smith |  |  | Nordic Semiconductor A/S |  |  |
| Clive Feather |  |  | Samsung |  |  |
| Paul Vanoostende |  |  | ST-NXP Wireless |  |  |
| Ben Brown |  |  | Teledyne LeCroy |  |  |
