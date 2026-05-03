# GAP.ICS.p42

> Source: PDF converted via PyMuPDF.

---

Generic Access Profile (GAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: GAP.ICS.p42 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
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

### 1.2 Auto-fill tables

This ICS includes one or more tables that are defined as auto-fill tables. Auto-fill tables are defined to allow for less-complex conditions within other tables. Auto-fill tables are distinguished from regular ICS tables by the addition of “(auto-fill)” after the table number, prior to the colon “:”.
An auto-fill table is automatically populated based on selected capabilities elsewhere in the ICS. The populated settings in the auto-fill table are not user editable.

### 1.3 Device and version configuration

Table 0: Device Configuration

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR |  |  | [1] 1.1 |  |  | C.1, C.4 |  |  |
| 2 |  |  | LE |  |  | [2] 1.1 |  |  | C.2, C.4 |  |  |
| 3 |  |  | BR/EDR/LE |  |  | [2] 1.1 |  |  | C.3, C.4 |  |  |

C.1: Mandatory IF CORE 41/1 “BR/EDR Core Configuration”, otherwise Optional.
C.2: Mandatory IF CORE 41/2 “LE Core Configuration”, otherwise Optional.
C.3: Mandatory IF CORE 41/3 “BR/EDR/LE Core Configuration”, otherwise Optional.
C.4: Mandatory to support one and only one.
Table 0a: No longer used

### 1.4 BR/EDR Capability Statement


#### 1.4.1 Modes

Table 1: Modes
Prerequisite: GAP 0/1 “BR/EDR” OR GAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-discoverable mode |  |  | [1] 4.1.1 |  |  | C.1 |  |  |
| 2 |  |  | Limited discoverable mode |  |  | [1] 4.1.2 |  |  | O |  |  |
| 3 |  |  | General discoverable mode |  |  | [1] 4.1.3 |  |  | O |  |  |
| 4 |  |  | Non-connectable mode |  |  | [1] 4.2.1 |  |  | O |  |  |
| 5 |  |  | Connectable mode |  |  | [1] 4.2.2 |  |  | M |  |  |
| 6 |  |  | Non-bondable mode |  |  | [1] 4.3.1 |  |  | O |  |  |
| 7 |  |  | Bondable mode |  |  | [1] 4.3.2 |  |  | C.2 |  |  |
| 8 |  |  | Non-synchronizable mode |  |  | [4] 4.4.1 |  |  | C.3 |  |  |
| 9 |  |  | Synchronizable mode |  |  | [4] 4.4.2 |  |  | C.3 |  |  |

C.1: Mandatory IF GAP 1/2 “Limited discoverable mode” OR NOT GAP 1/3 “General discoverable mode”, otherwise Optional.
C.2: Mandatory IF GAP 3/5 “Initiation of general bonding”, otherwise Optional.
C.3: Optional IF BB 3a/1 “Connectionless Peripheral Broadcast Transmitter”, otherwise Excluded.

#### 1.4.2 Security Aspects

Table 2: Security Aspects
Prerequisite: GAP 0/1 “BR/EDR” OR GAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Authentication procedure |  |  | [1] 5.1 |  |  | C.1 |  |  |
| 2 |  |  | Support of LMP-Authentication |  |  | [1] 5.1 |  |  | M |  |  |
| 3 |  |  | Initiate LMP-Authentication |  |  | [1] 5.1 |  |  | C.5 |  |  |
| 4 |  |  | Security Mode-1 |  |  | [1] 5.2.1.1 |  |  | C.7 |  |  |
| 5 |  |  | Security Mode-2 |  |  | [1] 5.2.1.2 |  |  | O |  |  |
| 6 |  |  | Security Mode-3 |  |  | [1] 5.2.1.3 |  |  | C.7 |  |  |
| 7 |  |  | Security Mode-4 |  |  | [1] 5.2.2 |  |  | M |  |  |
| 7a |  |  | Security Mode-4, level 4 |  |  | [4] 5.2.2.8 |  |  | C.9 |  |  |
| 7b |  |  | Security Mode-4, level 3 |  |  | [4] 5.2.2.8 |  |  | C.9 |  |  |
| 7c |  |  | Security Mode-4, level 2 |  |  | [4] 5.2.2.8 |  |  | C.9 |  |  |
| 7d |  |  | Security Mode-4, level 1 |  |  | [4] 5.2.2.8 |  |  | C.9 |  |  |
| 8 |  |  | Authenticated link key |  |  | [1] 5.2.2 |  |  | C.6 |  |  |
| 9 |  |  | Unauthenticated link key |  |  | [1] 5.2.2 |  |  | C.6 |  |  |
| 10 |  |  | Security Optional |  |  | [1] 5.2.2 |  |  | C.6 |  |  |
| 11 |  |  | Secure Connections Only Mode |  |  | [12] 5.2.2, 14.3 |  |  | C.8 |  |  |
| 12 |  |  | 56-bit minimum encryption key size |  |  | [9] 5.2.2.8 |  |  | C.10 |  |  |
| 13 |  |  | 128-bit encryption key size capable |  |  | [4] 5.2.2.8 |  |  | C.11 |  |  |
| 13a |  |  | 128-bit encryption key size capable, Security Mode-4, level 4 |  |  | [4] 5.2.2.8 |  |  | C.12 |  |  |
| 13b |  |  | 128-bit encryption key size capable, Security Mode-4, level 3 |  |  | [4] 5.2.2.8 |  |  | C.13 |  |  |
| 13c |  |  | 128-bit encryption key size capable, Security Mode-4, level 2 |  |  | [4] 5.2.2.8 |  |  | C.14 |  |  |
| 13d |  |  | 128-bit encryption key size capable, Security Mode-4, level 1 |  |  | [4] 5.2.2.8 |  |  | C.15 |  |  |
| 14 |  |  | Out-of-Band |  |  | [4] 5.2.2.7 |  |  | O |  |  |

C.1: Mandatory IF GAP 2/5 “Security Mode-2” OR GAP 2/6 “Security Mode-3”, otherwise Optional.
C.2–C.4: No longer used.
C.5: Mandatory IF GAP 2/5 “Security Mode-2” OR GAP 2/6 “Security Mode-3” OR GAP 2/7 “Security Mode-4”, otherwise Optional.
C.6: Mandatory to support at least one IF GAP 2/7 “Security Mode-4”, otherwise Excluded.
C.7: Excluded. See Note 2.
C.8: Mandatory IF GAP 25/10 “Secure Connections Only mode” OR GAP 35/10 “Secure Connections Only mode”, otherwise Optional IF LMP 2/26 “Secure Connections (Controller Support)” AND GAP 2/7a “Security Mode-4, level 4”, otherwise Excluded.
C.9: Optional IF GAP 2/7 “Security Mode-4”, otherwise Excluded.
C.10: Optional IF GAP 2/7d “Security Mode-4, level 1” OR GAP 2/7c “Security Mode-4, level 2” OR GAP 2/7b “Security Mode-4, level 3”, otherwise Excluded.
C.11: Mandatory IF GAP 2/13a “128-bit encryption key size capable, Security Mode-4, level 4” OR GAP 2/13b “128-bit encryption key size capable, Security Mode-4, level 3” OR GAP 2/13c “128-bit
encryption key size capable, Security Mode-4, level 2” OR GAP 2/13d “128-bit encryption key size capable, Security Mode-4, level 1”, otherwise Excluded.
C.12: Mandatory IF GAP 2/7a “Security Mode-4, level 4”, otherwise Excluded.
C.13: Optional IF GAP 2/7b “Security Mode-4, level 3”, otherwise Excluded.
C.14: Optional IF GAP 2/7c “Security Mode-4, level 2”, otherwise Excluded.
C.15: Optional IF GAP 2/7d “Security Mode-4, level 1”, otherwise Excluded.
Note 1: The “Authentication Procedure” in item 1TGAP 2/1 is the one described in 1TFig. 5.1 in the GAP
Specification and not the LMP-Authentication.
Note 2: A Core 2.1 or later device is required to support security Mode-4. Security Mode-2 is used only
for backward compatibility purposes with Core 2.0 and earlier devices. Security Mode-1 and security Mode-3 are excluded for Core 2.1 or later devices.

#### 1.4.3 Idle Mode Procedures

Table 3: Idle Mode Procedures
Prerequisite: GAP 0/1 “BR/EDR” OR GAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiation of general inquiry |  |  | [1] 6.1 |  |  | C.1 |  |  |
| 2 |  |  | Initiation of limited inquiry |  |  | [1] 6.2 |  |  | C.1 |  |  |
| 3 |  |  | Initiation of name discovery |  |  | [1] 6.3 |  |  | O |  |  |
| 4 |  |  | Initiation of device discovery |  |  | [1] 6.4 |  |  | O |  |  |
| 5 |  |  | Initiation of general bonding |  |  | [1] 6.5 |  |  | O |  |  |
| 6 |  |  | Initiation of dedicated bonding |  |  | [1] 6.5 |  |  | O |  |  |

C.1: Mandatory to support at least one IF GAP 3/5 “Initiation of general bonding”, otherwise Optional.

#### 1.4.4 Establishment Procedures

Table 4: Establishment Procedures
Prerequisite: GAP 0/1 “BR/EDR” OR GAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Link Establishment as initiator |  |  | [1] 7.1 |  |  | M |  |  |
| 2 |  |  | Link Establishment as acceptor |  |  | [1] 7.1 |  |  | M |  |  |
| 3 |  |  | Channel Establishment as initiator |  |  | [1] 7.2 |  |  | O |  |  |
| 4 |  |  | Channel Establishment as acceptor |  |  | [1] 7.2 |  |  | M |  |  |
| 5 |  |  | Connection Establishment as initiator |  |  | [1] 7.3 |  |  | O |  |  |
| 6 |  |  | Connection Establishment as acceptor |  |  | [1] 7.3 |  |  | O |  |  |
| 7 |  |  | Synchronization Establishment as receiver |  |  | [4] 7.5 |  |  | C.1 |  |  |

C.1: Optional IF BB 3a/2 “Connectionless Peripheral Broadcast Receiver”, otherwise Excluded.

#### 1.4.5 L2CAP requirements

Table 4a (auto-fill): L2CAP Requirements
Prerequisite: GAP 0/1 “BR/EDR” OR GAP 0/3 “BR/EDR/LE”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Detect insufficient authentication | [1] 5.1 | C.1 | [14] L2CAP 5/1 |  |  |

C.1: Mandatory IF GAP 2/1 “Authentication procedure", otherwise not defined.

#### 1.4.6 Generic Access Profile Characteristics

Table 4b: GAP Characteristics
Prerequisite: GATT 1a/4 “GATT Server over BR/EDR”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Device Name |  |  | [2] 12.1 |  |  | M |  |  |
| 2 |  |  | Appearance |  |  | [2] 12.2 |  |  | M |  |  |
| 3 |  |  | Peripheral Preferred Connection Parameters |  |  | [2] 12.5 |  |  | O |  |  |
| 4 |  |  | Central Address Resolution |  |  | [5] 12 |  |  | O |  |  |
| 5 |  |  | Resolvable Private Address Only |  |  | [2] 12.5 |  |  | O |  |  |
| 6 |  |  | Encrypted Data Key Material |  |  | [12] 12.6 |  |  | O |  |  |
| 7 |  |  | Encrypted Data Key Material Indications |  |  | [12] 12.6 |  |  | C.1 |  |  |
| 8 |  |  | Writable Device Name |  |  | [2] 12.1 |  |  | O |  |  |
| 9 |  |  | Writable Appearance |  |  | [2] 12.2 |  |  | O |  |  |

C.1: Optional IF GAP 4b/6 “Encrypted Data Key Material”, otherwise Excluded.

### 1.5 LE Capability Statement

Table 5: LE Roles
Prerequisite: GAP 0/2 “LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcaster |  |  | [2] 2.2.2 |  |  | C.1 |  |  |
| 2 |  |  | Observer |  |  | [2] 2.2.2 |  |  | C.1 |  |  |
| 3 |  |  | Peripheral |  |  | [2] 2.2.2 |  |  | C.1 |  |  |
| 4 |  |  | Central |  |  | [2] 2.2.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.
Note: Table 5 is applicable for LE configurations. For BR/EDR/LE configurations, see Table 38 for role declarations.

#### 1.5.1 Broadcaster


##### 1.5.1.1 Physical Layer

Table 6: Broadcaster Physical Layer
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Transmitter |  |  | [2] 2.2.2 |  |  | M |  |  |
| 2 |  |  | Receiver |  |  | [2] 2.2.2 |  |  | O |  |  |


##### 1.5.1.2 Link Layer Features


###### 1.5.1.2.1 Link Layer States

Table 7: Broadcaster Link Layer States
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Standby State | [2] 2.2.2, 2.2.2.1 | M | N/A |  |  |
| 2 | Advertising State | [2] 2.2.2, 2.2.2.1 | M | [15] LL 1/1 |  |  |
| 3 | Isochronous Broadcasting State | [10] 2.2.2, 2.2.2.1 | C.1 | [15] LL 1/6 |  |  |

C.1: Optional IF CORE 2a/52 “Host Core v5.2 or later”, otherwise not defined.

###### 1.5.1.2.2 Advertising Event Types

Table 8: Broadcaster Link Layer Advertising Event Types
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Non-connectable and non-scannable undirected events | [2] 2.2.2 | M | [15] LL 3/1 |  |  |
| 2 | Scannable undirected events | [2] 2.2.2 | O | [15] LL 3/5 |  |  |
| 3 | Non-connectable and non-scannable directed events | [7] 2.2.2 | C.1 | [15] LL 3/1a |  |  |
| 4 | Scannable directed events | [7] 2.2.2 | C.1 | [15] LL 3/5a |  |  |
| 5 | LE Extended Advertising | [7] 2.2.2 | O | [15] LL 9/41 |  |  |

C.1: Optional IF GAP 8/5 “LE Extended Advertising”, otherwise not defined.
Table 8a: Broadcaster Link Layer Advertising Data Types
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service UUID |  |  | [3] 1.1 |  |  | O |  |  |
| 2 |  |  | Local Name |  |  | [3] 1.2 |  |  | O |  |  |
| 3 |  |  | Flags |  |  | [3] 1.3 |  |  | O |  |  |
| 4 |  |  | Manufacturer Specific Data |  |  | [3] 1.4 |  |  | O |  |  |
| 5 |  |  | TX Power Level |  |  | [3] 1.5 |  |  | O |  |  |
| 6 |  |  | Security Manager OOB |  |  | [3] 1.7 |  |  | O |  |  |
| 7 |  |  | Security Manager TK Value |  |  | [3] 1.8 |  |  | O |  |  |
| 8 |  |  | Peripheral Connection Interval Range |  |  | [3] 1.9 |  |  | O |  |  |
| 9 |  |  | Service Solicitation |  |  | [3] 1.10 |  |  | O |  |  |
| 10 |  |  | Service Data |  |  | [3] 1.11 |  |  | O |  |  |
| 11 |  |  | Appearance |  |  | [3] 1.12 |  |  | O |  |  |
| 12 |  |  | Public Target Address |  |  | [3] 1.13 |  |  | O |  |  |
| 13 |  |  | Random Target Address |  |  | [3] 1.14 |  |  | O |  |  |
| 14 |  |  | Advertising Interval |  |  | [3] 1.15 |  |  | O |  |  |
| 14a |  |  | Advertising Interval – Long |  |  | [3] 1.15 |  |  | O |  |  |
| 15 |  |  | LE Bluetooth Device Address |  |  | [3] 1.16 |  |  | O |  |  |
| 16 |  |  | LE Role |  |  | [3] 1.17 |  |  | O |  |  |
| 17 |  |  | Uniform Resource Identifier |  |  | [3] 1.18 |  |  | O |  |  |
| 18 |  |  | LE Supported features |  |  | [3] 1.19 |  |  | O |  |  |
| 19 |  |  | Encrypted Data |  |  | [3] 1.23 |  |  | O |  |  |
| 20 |  |  | Periodic Advertising Response Timing |  |  | [3] 1.24 |  |  | O |  |  |

Table 9: Broadcaster Connection Modes and Procedures
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-connectable mode |  |  | [2] 9.3.2 |  |  | M |  |  |


##### 1.5.1.4 Broadcasting and Observing

Table 10: Broadcaster Broadcasting and Observing Features
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcast mode |  |  | [2] 9.1.1 |  |  | M |  |  |
| 2 |  |  | Broadcast Isochronous Synchronizability mode |  |  | [10] 9.6.1 |  |  | C.1 |  |  |
| 3 |  |  | Broadcast Isochronous Broadcasting mode |  |  | [10] 9.6.2 |  |  | C.2 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | Broadcast Isochronous Terminate procedure |  |  | [10] 9.6.5 |  |  | C.1 |  |  |
| 5 |  |  | Broadcast Isochronous Channel Map Update procedure |  |  | [10] 9.6.4 |  |  | C.1 |  |  |

C.1: Mandatory IF GAP 10/3 “Broadcast Isochronous Broadcasting mode”, otherwise Excluded.
C.2: Optional IF CORE 2a/52 “Host Core v5.2 or later”, otherwise Excluded.

##### 1.5.1.5 Privacy Feature

Table 11: Broadcaster Privacy Feature
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Privacy feature |  |  | [5] 10.7 |  |  | O |  |  |
| 2 |  |  | Resolvable private address generation procedure |  |  | [5] 10.8.2.2 [6] 1.3.2.2 |  |  | C.1 |  |  |
| 3 |  |  | Non-resolvable private address generation procedure |  |  | [5] 10.8.2.1 [6] 1.3.2.2 |  |  | C.2 |  |  |
| 4 |  |  | Resolvable private address resolution procedure |  |  | [5] 10.8.2.3 [6] 1.3.2.2 |  |  | O |  |  |
| 5 |  |  | Controller-based privacy |  |  | [5] 10.7 |  |  | O |  |  |

C.1: Mandatory IF GAP 11/1 “Privacy feature” AND NOT GAP 11/3 “Non-resolvable private address
generation procedure”, otherwise Optional.
C.2: Mandatory IF GAP 11/1 “Privacy feature” AND NOT GAP 11/2 “Resolvable private address
generation procedure”, otherwise Optional.

##### 1.5.1.6 Periodic Advertising Modes and Procedures

Table 11a: Periodic Advertising Modes and Procedures
Prerequisite: (GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”) AND CORE 2a/50 “Host Core v5.0 or later”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Periodic Advertising Synchronizability mode | [7] 9.5.1 | C.1 | N/A |  |  |
| 2 | Periodic Advertising | [7] 9.5.2 | O | [15] LL 3/10 |  |  |
| 3 | Periodic Advertising with responses | [7] 9.5.2.1 | O | [15] LL 3/10a |  |  |
| 4 | No longer used | N/A | N/A | N/A |  |  |

C.1: Optional IF GAP 11a/2 “Periodic Advertising”, otherwise Excluded.
C.2–C.4: No longer used.
Table 11b: Broadcaster Security Aspects Features
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

|  | Item |  |  | Capability | Reference | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE security Mode-3 |  | [10] 10.2.5 | C.1 |  |
| 2 |  |  | LE security Mode-3 level 1 |  | [10] 10.2.5 | C.2 |  |
| 3 |  |  | LE security Mode-3 level 2 |  | [10] 10.2.5 | C.2 |  |
| 4 |  |  | LE security Mode-3 level 3 |  | [10] 10.2.5 | C.2 |  |

C.1: Mandatory IF GAP 10/2 “Broadcast Isochronous Synchronizability mode”, otherwise Excluded.
C.2: Mandatory to support at least one IF GAP 11b/1 “LE security Mode-3”, otherwise Excluded.
Table 11c: SM Requirements
Prerequisite: GAP 5/1 “Broadcaster (LE)” OR GAP 38/1 “Broadcaster (BR/EDR/LE)”

| Item | Capability | Reference | Status | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- |
| 1 | Out of Band | N/A | C.1 | [13] SM 4/3 |  |

C.1: Mandatory IF GAP 8a/6 “Security Manager OOB”, otherwise not defined.

#### 1.5.2 Observer


##### 1.5.2.1 Physical Layer

Table 12: Observer Physical Layer
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

|  | Item |  |  | Capability | Reference | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Receiver |  | [2] 2.2.2 | M |  |
| 2 |  |  | Transmitter |  | [2] 2.2.2 | O |  |


##### 1.5.2.2 Link Layer Features


###### 1.5.2.2.1 Link Layer States

Table 13: Observer Link Layer States
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

| Item | Capability | Reference | Status | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- |
| 1 | Standby State | [2] 2.2.2 | M | N/A |  |
| 2 | Scanning State | [2] 2.2.2 | M | [15] LL 1/2 |  |

Table 14: Observer Link Layer Scanning Types
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Passive Scanning | [2] 2.2.2 | M | [15] LL 4/1 |  |  |
| 2 | Active Scanning | [2] 2.2.2 | O | [15] LL 4/3 |  |  |

Table 14a: Observer Link Layer Scanning Data Types
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service UUID |  |  | [3] 1.1 |  |  | O |  |  |
| 2 |  |  | Local Name |  |  | [3] 1.2 |  |  | O |  |  |
| 3 |  |  | Flags |  |  | [3] 1.3 |  |  | O |  |  |
| 4 |  |  | Manufacturer Specific Data |  |  | [3] 1.4 |  |  | O |  |  |
| 5 |  |  | TX Power Level |  |  | [3] 1.5 |  |  | O |  |  |
| 6 |  |  | Security Manager OOB |  |  | [3] 1.7 |  |  | O |  |  |
| 7 |  |  | Security Manager TK Value |  |  | [3] 1.8 |  |  | O |  |  |
| 8 |  |  | Peripheral Connection Interval Range |  |  | [3] 1.9 |  |  | O |  |  |
| 9 |  |  | Service Solicitation |  |  | [3] 1.10 |  |  | O |  |  |
| 10 |  |  | Service Data |  |  | [3] 1.11 |  |  | O |  |  |
| 11 |  |  | Appearance |  |  | [3] 1.12 |  |  | O |  |  |
| 12 |  |  | Public Target Address |  |  | [3] 1.13 |  |  | O |  |  |
| 13 |  |  | Random Target Address |  |  | [3] 1.14 |  |  | O |  |  |
| 14 |  |  | Advertising Interval |  |  | [3] 1.15 |  |  | O |  |  |
| 14a |  |  | Advertising Interval – Long |  |  | [3] 1.15 |  |  | O |  |  |
| 15 |  |  | LE Bluetooth Device Address |  |  | [3] 1.16 |  |  | O |  |  |
| 16 |  |  | LE Role |  |  | [3] 1.17 |  |  | O |  |  |
| 17 |  |  | Uniform Resource Identifier |  |  | [3] 1.18 |  |  | O |  |  |
| 18 |  |  | LE Supported features |  |  | [3] 1.19 |  |  | O |  |  |
| 19 |  |  | Encrypted Data |  |  | [3] 1.23 |  |  | O |  |  |
| 20 |  |  | Periodic Advertising Response Timing |  |  | [3] 1.24 |  |  | O |  |  |


##### 1.5.2.3 Connection Modes and Procedures

Table 15: Observer Connection Modes and Procedures
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-connectable mode |  |  | [2] 9.3.2 |  |  | M |  |  |


##### 1.5.2.4 Broadcasting and Observing

Table 16: Observer Broadcasting and Observing Features
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Observation procedure |  |  | [2] 9.1.2 |  |  | M |  |  |
| 2 |  |  | Broadcast Isochronous Synchronization Establishment procedure |  |  | [10] 9.6.3 |  |  | C.1 |  |  |
| 3 |  |  | Broadcast Isochronous Termination procedure |  |  | [10] 9.6.5 |  |  | C.2 |  |  |
| 4 |  |  | Broadcast Isochronous Channel Map Update procedure |  |  | [10] 9.6.4 |  |  | C.2 |  |  |

C.1: Optional IF CORE 2a/52 “Host Core v5.2 or later”, otherwise Excluded.
C.2: Mandatory IF GAP 16/2 “Broadcast Isochronous Synchronization Establishment procedure”, otherwise Excluded.

##### 1.5.2.5 Privacy Feature

Table 17: Observer Privacy Feature
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Privacy feature |  |  | [5] 10.7 |  |  | O |  |  |
| 2 |  |  | Non-resolvable private address generation procedure |  |  | [5] 10.8.2.1 [6] 1.3.2.2 |  |  | C.1 |  |  |
| 3 |  |  | Resolvable private address resolution procedure |  |  | [5] 10.8.2.3 [6] 1.3.2.2 |  |  | O |  |  |
| 4 |  |  | Resolvable private address generation procedure |  |  | [5] 10.8.2.2 [6] 1.3.2.3 |  |  | C.2 |  |  |
| 5 |  |  | Controller-based privacy |  |  | [5] 10.7 |  |  | O |  |  |

C.1: Mandatory IF GAP 17/1 “Privacy feature” AND GAP 14/2 “Active Scanning” AND NOT GAP 17/4 “Resolvable private address generation procedure”, otherwise Optional.
C.2: Mandatory IF GAP 17/1 “Privacy feature” AND GAP 14/2 “Active Scanning” AND NOT GAP 17/2 “Non-resolvable private address generation procedure”, otherwise Optional.
Table 17a: Periodic Advertising Modes and Procedures
Prerequisite: (GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”) AND CORE 2a/50 “Host Core v5.0 or later”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising | [7] 9.5.3 | O | N/A |  |  |
| 2 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising | [7] 9.5.3 | O | N/A |  |  |
| 3 | No longer used | N/A | N/A | N/A |  |  |
| 4 | Scanning for Periodic Advertising | [7] 9.5.3 | C.1 | [15] LL 4/8 |  |  |
| 5 | Synchronizing to Periodic Advertising | [7] 9.5.3 | C.2 | [15] LL 11/1 |  |  |
| 6 | Scanning for Periodic Advertising with Responses | [12] 9.3.17 | C.3 | [15] LL 4/8a |  |  |

C.1: Mandatory IF GAP 17a/1 “Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising”, otherwise not defined.
C.2: Mandatory IF GAP 17a/2 “Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising”, otherwise not defined.
C.3: Mandatory IF GAP 33/10 “Periodic Advertising Connection procedure”, otherwise not defined.

##### 1.5.2.7 Security Aspects

Table 17b: Observer Security Aspects Features
Prerequisite: GAP 5/2 “Observer (LE)” OR GAP 38/2 “Observer (BR/EDR/LE)”

|  | Item |  |  | Capability | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE security Mode-3 |  | [10] 10.2.5 |  | C.1 |  |  |
| 2 |  |  | LE security Mode-3 level 1 |  | [10] 10.2.5 |  | C.2 |  |  |
| 3 |  |  | LE security Mode-3 level 2 |  | [10] 10.2.5 |  | C.2 |  |  |
| 4 |  |  | LE security Mode-3 level 3 |  | [10] 10.2.5 |  | C.2 |  |  |

C.1: Mandatory IF GAP 16/2 “Broadcast Isochronous Synchronization Establishment procedure”, otherwise Excluded.
C.2: Mandatory to support at least one IF GAP 17b/1 “LE security Mode-3”, otherwise Excluded.

#### 1.5.3 Peripheral


##### 1.5.3.1 Physical Layer

Table 18: Peripheral Physical Layer
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Transmitter |  |  | [2] 2.2.2 |  |  | M |  |  |
| 2 |  |  | Receiver |  |  | [2] 2.2.2 |  |  | M |  |  |


##### 1.5.3.2 Link Layer Features


###### 1.5.3.2.1 Link Layer States

Table 19: Peripheral Link Layer States
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Standby State | [2] 2.2.2 | M | N/A |  |  |
| 2 | Advertising State | [2] 2.2.2 | M | [15] LL 1/1 |  |  |
| 3 | Connection State (Peripheral Role) | [4] 2.2.2 | M | [15] LL 1/4 |  |  |


###### 1.5.3.2.2 Advertising Event Types

Table 20: Peripheral Link Layer Advertising Event Types
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Connectable and scannable undirected events | [4] 2.2.2 | M | [15] LL 3/2 |  |  |
| 2 | Connectable directed events | [4] 2.2.2 | O | [15] LL 3/4 |  |  |
| 2a | No longer used | N/A | N/A | N/A |  |  |
| 3 | Non-connectable and non-scannable undirected events | [4] 2.2.2, 9.3.2.2, 9.3.11.2 | O | [15] LL 3/1 |  |  |
| 4 | Scannable undirected events | [4] 2.2.2, 9.3.4.2 | O | [15] LL 3/5 |  |  |
| 5 | Connectable undirected events | [7] 2.2.2 | C.1 | [15] LL 3/4b |  |  |
| 6 | Non-connectable and non-scannable directed events | [7] 2.2.2 | C.1 | [15] LL 3/1a |  |  |
| 7 | Scannable directed events | [7] 2.2.2 | C.1 | [15] LL 3/5a |  |  |
| 8 | LE Extended Advertising | [7] 2.2.2 | O | [15] LL 9/41 |  |  |

C.1: Mandatory to support at least one.
Table 20a: Peripheral Link Layer Advertising Data Types
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Service UUID | [3] 1.1 | C.1 | N/A |  |  |
| 2 | Local Name | [3] 1.2 | C.1 | N/A |  |  |
| 3 | Flags | [3] 1.3 | C.2 | N/A |  |  |
| 4 | Manufacturer Specific Data | [3] 1.4 | C.1 | N/A |  |  |
| 5 | TX Power Level | [3] 1.5 | C.1 | N/A |  |  |
| 6 | Security Manager OOB | [3] 1.7 | C.3 | N/A |  |  |
| 7 | Security Manager TK Value | [3] 1.8 | C.1 | N/A |  |  |
| 8 | Peripheral Connection Interval Range | [3] 1.9 | C.1 | N/A |  |  |
| 9 | Service Solicitation | [3] 1.10 | C.1 | N/A |  |  |
| 10 | Service Data | [3] 1.11 | C.1 | N/A |  |  |
| 11 | Appearance | [3] 1.12 | C.1 | N/A |  |  |
| 12 | Public Target Address | [3] 1.13 | C.1 | N/A |  |  |
| 13 | Random Target Address | [3] 1.14 | C.1 | N/A |  |  |
| 14 | Advertising Interval | [3] 1.15 | C.1 | N/A |  |  |
| 14a | Advertising Interval – Long | [3] 1.15 | C.1 | N/A |  |  |
| 15 | LE Bluetooth Device Address | [3] 1.16 | C.1 | N/A |  |  |
| 16 | LE Role | [3] 1.17 | C.1 | N/A |  |  |
| 17 | Uniform Resource Identifier | [3] 1.18 | O | N/A |  |  |
| 18 | LE Supported features | [3] 1.19 | O | N/A |  |  |
| 19 | Encrypted Data | [3] 1.23 | O | N/A |  |  |
| 20 | Periodic Advertising Response Timing | [3] 1.24 | O | N/A |  |  |
| 21 | Periodic Advertising with responses | [3] 1.24 | C.4 | [15] LL 3/10a |  |  |

C.1: Optional IF GAP 20/1 “Connectable and scannable undirected events” OR GAP 20/3 “Non- connectable and non-scannable undirected events” OR GAP 20/4 “Scannable undirected events”, otherwise Excluded.
C.2: Mandatory IF GAP 22/2 “Limited discoverable mode” OR GAP 22/3 “General discoverable mode”, otherwise Optional.
C.3: Optional IF (GAP 20/1 “Connectable and scannable undirected events” OR GAP 20/3 “Non- connectable and non-scannable undirected events” OR GAP 20/4 “Scannable undirected events”) AND GAP 27b/9 “Out of Band”, otherwise Excluded.
C.4: Mandatory IF GAP 20a/20 “Periodic Advertising Response Timing”, otherwise not defined.
Table 21: Peripheral Link Layer Control Procedures
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connection Update procedure |  |  | [4] 2.2.2 |  |  | M |  |  |
| 2 |  |  | Channel Map Update procedure |  |  | [4] 2.2.2 |  |  | M |  |  |
| 3 |  |  | Encryption procedure |  |  | [4] 2.2.2 |  |  | C.3 |  |  |
| 4 |  |  | Central-initiated Feature Exchange procedure |  |  | [4] 2.2.2 |  |  | M |  |  |
| 5 |  |  | Version Exchange procedure |  |  | [4] 2.2.2 |  |  | M |  |  |
| 6 |  |  | Termination procedure |  |  | [4] 2.2.2 |  |  | M |  |  |
| 7 |  |  | LE Ping procedure |  |  | [4] 2.2.2 |  |  | O |  |  |
| 8 |  |  | Peripheral-initiated Feature Exchange procedure |  |  | [4] 2.2.2 |  |  | C.1 |  |  |
| 9 |  |  | Connection Parameter Request procedure |  |  | [4] 2.2.2 |  |  | O |  |  |
| 10 |  |  | Data Length Update procedure |  |  | [8] 2.2.2 |  |  | O |  |  |
| 11 |  |  | PHY Update procedure |  |  | [8] 2.2.2 |  |  | C.2 |  |  |
| 12 |  |  | Minimum Number Of Used Channels procedure |  |  | [8] 2.2.2 |  |  | C.2 |  |  |

C.1: Mandatory IF GAP 21/9 “Connection Parameter Request procedure”, otherwise Optional.
C.2: Optional IF CORE 2a/50 “Host Core v5.0 or later”, otherwise Excluded.
C.3: Mandatory IF GAP 25/6 “Authenticate signed data procedure” OR GAP 25/7 “Authenticated Pairing (LE security Mode-1 level 3)” OR GAP 25/9 “LE security Mode-1 level 4”, otherwise Optional.

##### 1.5.3.3 Discovery Modes and Procedures

Table 22: Peripheral Discovery Modes and Procedures
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-discoverable mode |  |  | [4] 9.2.2, 13.1 |  |  | M |  |  |
| 2 |  |  | Limited discoverable mode |  |  | [4] 9.2.3, 13.1 |  |  | O |  |  |
| 3 |  |  | General discoverable mode |  |  | [4] 9.2.4, 13.1 |  |  | C.1 |  |  |
| 4 |  |  | Name discovery procedure |  |  | [2] 9.2.7 |  |  | O |  |  |

C.1: Mandatory IF NOT GAP 22/2 “Limited discoverable mode”, otherwise Optional.
Table 23: Peripheral Connection Modes and Procedures
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- |
| 1 | Non-connectable mode | [4] 9.3.2 | M | N/A |  |
| 2 | Directed connectable mode | [4] 9.3.3 | O | N/A |  |
| 3 | Undirected connectable mode | [4] 9.3.4 | M | N/A |  |
| 4 | Connection parameter update procedure | [4] 9.3.9 | O | N/A |  |
| 5 | Terminate connection procedure | [4] 9.3.10 | M | N/A |  |
| 6 | Connected Isochronous Stream Peripheral Establishment procedure | [10] 9.3.14 | C.1 | N/A |  |
| 7 | Connected Isochronous Stream Terminate procedure | [10] 9.3.15 | C.1 | N/A |  |
| 7a | Connected Isochronous Stream - Peripheral | [10] 9.3.14, 9.3.15 | O | [15] LL 9/32 |  |
| 8 | Connection Subrate procedure | [11] 9.3.16 | C.2 | N/A |  |
| 9 | Periodic Advertising Connection | [11] 9.5.5.1 | C.3 | N/A |  |

C.1: Mandatory IF GAP 23/7a “Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.2: Optional IF CORE 2a/53 “Host Core v5.3 or later”, otherwise Excluded.
C.3: Optional IF GAP 11a/3 “Periodic Advertising with Responses”, otherwise Excluded.
Table 23a: Peripheral Connection Modes and Procedures
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CS Initiator Role | [16] 9.7.1 | C.1 | [16] LL 1/7 |  |  |
| 2 | CS Reflector Role | [16] 9.7.2 | C.2 | [16] LL 1/8 |  |  |

C.1: Mandatory IF NOT GAP 33a/1 “CS Initiator Role”, otherwise Optional.
C.2: Mandatory IF NOT GAP 33a/2 “CS Reflector Role”, otherwise Optional.

##### 1.5.3.5 Bonding Modes and Procedures

Table 24: Peripheral Bonding Modes and Procedures
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-bondable mode |  |  | [2] 9.4.2 |  | M |  |  |
| 2 |  |  | Bondable mode |  |  | [4] 9.4.3, 13.2 |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Bonding procedure |  |  | [4] 9.4.4, 13.2 |  |  | C.2 |  |  |
| 4 |  |  | Multiple Bonds |  |  | [4] 9.4 |  |  | C.1 |  |  |

C.1: Optional IF GAP 24/2 “Bondable mode”, otherwise Excluded.
C.2: Mandatory IF GAP 24/2 “Bondable mode”, otherwise Excluded.

##### 1.5.3.6 Security Aspects

Table 25: Peripheral Security Aspects Features
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE security Mode-1 |  |  | [4] 10.2.1 |  |  | O |  |  |
| 2 |  |  | LE security Mode-2 |  |  | [4] 10.2.2 |  |  | O |  |  |
| 3 |  |  | Authentication procedure |  |  | [4] 10.3 |  |  | O |  |  |
| 4 |  |  | Authorization procedure |  |  | [4] 10.5 |  |  | O |  |  |
| 5 |  |  | Connection data signing procedure |  |  | [4] 10.4.1 |  |  | C.6 |  |  |
| 6 |  |  | Authenticate signed data procedure |  |  | [4] 10.4.2 |  |  | C.6 |  |  |
| 7 |  |  | Authenticated Pairing (LE security Mode-1 level 3) |  |  | [4] 10.3 |  |  | C.1 |  |  |
| 8 |  |  | Unauthenticated Pairing (LE security Mode-1 level 2) |  |  | [4] 10.3 |  |  | C.1 |  |  |
| 9 |  |  | LE security Mode-1 level 4 |  |  | [5] 10.3 |  |  | C.1 |  |  |
| 10 |  |  | Secure Connections Only mode |  |  | [12] 10.2.4, 14.3 |  |  | C.4 |  |  |
| 11 |  |  | Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only |  |  | [5] 10.3 |  |  | C.1 |  |  |
| 12 |  |  | Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only |  |  | [5] 10.3 |  |  | C.1 |  |  |
| 13 |  |  | Minimum 128 Bit entropy key |  |  | [5] 10.3 |  |  | C.5 |  |  |
| 13a |  |  | Minimum 128 Bit entropy key, LE security Mode-1 level 4 |  |  | [5] 10.3 |  |  | C.7 |  |  |
| 13b |  |  | Minimum 128 Bit entropy key, LE security Mode-1 level 3 |  |  | [5] 10.3 |  |  | C.8 |  |  |
| 13c |  |  | Minimum 128 Bit entropy key, LE security Mode-1 level 2 |  |  | [5] 10.3 |  |  | C.9 |  |  |
| 14 |  |  | Client security checks for GATT indications and notifications |  |  | [11] 10.3.2.2 |  |  | O |  |  |
| 15 |  |  | Channel Sounding Security Level 1 |  |  | [16] 10.11.1 |  |  | C.10 |  |  |
| 16 |  |  | Channel Sounding Security Level 2 |  |  | [16] 10.11.1 |  |  | C.11 |  |  |
| 17 |  |  | Channel Sounding Security Level 3 |  |  | [16] 10.11.1 |  |  | C.12 |  |  |
| 18 |  |  | Channel Sounding Security Level 4 |  |  | [16] 10.11.1 |  |  | C.13 |  |  |

C.1: Optional IF GAP 25/1 “LE security Mode-1”, otherwise Excluded.
C.2–C.3: No longer used.
C.4: Mandatory IF GAP 2/11 “Secure Connections Only Mode” OR GAP 35/10 “Secure Connections Only mode”, otherwise Optional IF GAP 25/9 “LE security Mode-1 level 4”, otherwise Excluded.
C.5: Mandatory IF GAP 25/13a “Minimum 128 Bit entropy key, LE security Mode-1 level 4” OR GAP 25/13b “Minimum 128 Bit entropy key, LE security Mode-1 level 3” OR GAP 25/13c “Minimum 128 Bit entropy key, LE security Mode-1 level 2”, otherwise Excluded.
C.6: Mandatory to support at least one IF GAP 25/2 “LE security Mode-2”, otherwise Optional.
C.7: Mandatory IF GAP 25/9 “LE security Mode-1 level 4”, otherwise Excluded.
C.8: Optional IF GAP 25/12 “Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only”, otherwise Excluded.
C.9: Optional IF GAP 25/11 “Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only”, otherwise Excluded.
C.10: Mandatory IF GAP 25a/1 “CS Mode-2” OR GAP 25a/2 “CS Mode-3” OR GAP 25a/3 “CS RTT Access Address, 10 ns” OR GAP 25a/4 “CS RTT Access Address, 150 ns”, otherwise Excluded.
C.11: Mandatory IF GAP 25a/4 “CS RTT Access Address, 150 ns”, otherwise Excluded.
C.12: Mandatory IF GAP 25a/3 “CS RTT Access Address, 10 ns”, otherwise Excluded.
C.13: Mandatory IF GAP 25a/2 “CS Mode-3” AND (GAP 25a/5 “CS RTT Sounding Sequence, 10 ns” OR GAP 25a/6 “CS RTT Sounding Sequence, 150 ns” OR GAP 25a/7 “CS RTT Random Payload, 10 ns” OR GAP 25a/8 “CS RTT Random Payload, 150 ns”), otherwise Excluded.
Table 25a: Peripheral Security Aspects Features
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CS Mode-2 | [16] 10.11 | M | [16] LL 13/2 |  |  |
| 2 | CS Mode-3 | [16] 10.11 | O | [16] LL 13/3 |  |  |
| 3 | CS RTT Access Address, 10 ns | [16] 10.11.1 | C.1 | [16] LL 13/4 |  |  |
| 4 | CS RTT Access Address, 150 ns | [16] 10.11.1 | C.1 | [16] LL 13/5 |  |  |
| 5 | CS RTT Sounding Sequence, 10 ns | [16] 10.11.1 | C.2 | [16] LL 13/6 |  |  |
| 6 | CS RTT Sounding Sequence, 150 ns | [16] 10.11.1 | C.2 | [16] LL 13/7 |  |  |
| 7 | CS RTT Random Payload, 10 ns | [16] 10.11.1 | C.3 | [16] LL 13/8 |  |  |
| 8 | CS RTT Random Payload, 150 ns | [16] 10.11.1 | C.3 | [16] LL 13/9 |  |  |

C.1: Mandatory to support one and only one.
C.2: Mandatory to support one and only one.
C.3: Mandatory to support one and only one.

##### 1.5.3.7 Privacy Feature

Table 26: Peripheral Privacy Feature
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Privacy feature | [5] 10.7 | O | N/A |  |  |
| 2 | Non-resolvable private address generation procedure | [5] 10.7, 10.8.2.1 [6] 1.3.2.2 | O | N/A |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 3 | Resolvable private address generation procedure | [5] 10.7, 10.8.2.2 [6] 1.3.2.2 | C.1 | N/A |  |  |
| 4 | Resolvable private address resolution procedure | [5] 10.7, 10.8.2.3 [6] 1.3.2.2 | C.1 | N/A |  |  |
| 5 | Controller-based privacy | [5] 10.7 | O | N/A |  |  |
| 6 | LL Privacy | [5] 10.7 [6] 6 | O | [15] LL 9/13 |  |  |

C.1: Mandatory IF GAP 26/1 “Privacy feature”, otherwise Optional.

##### 1.5.3.8 Generic Access Profile Characteristics

Table 27: Peripheral GAP Characteristics
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Device Name | [2] 12.1 | M | N/A |  |  |
| 2 | Appearance | [2] 12.2 | M | N/A |  |  |
| 3–4 | No longer used | N/A | N/A | N/A |  |  |
| 5 | Peripheral Preferred Connection Parameters | [2] 12.5 | O | N/A |  |  |
| 6 | Writable Device Name | [2] 12.1 | O | N/A |  |  |
| 7 | Writable Appearance | [2] 12.2 | O | N/A |  |  |
| 8 | No longer used | N/A | N/A | N/A |  |  |
| 9 | Central Address Resolution | [5] 12 | O | N/A |  |  |
| 9a | Resolution of private addresses | [5] 12 | C.1 | [15] LL 2/5 |  |  |
| 10 | Encrypted Data Key Material | [12] 12.6 | O | N/A |  |  |
| 10a | Encrypted Data Key Material Indications | [12] 12.6 | C.2 | N/A |  |  |
| 11 | LE GATT Security Levels | [12] 12.7 | O | N/A |  |  |
| 12 | Resolvable Private Address Only | [2] 12.5 | C.3 | N/A |  |  |

C.1: Mandatory IF GAP 27/9 “Central Address Resolution”, otherwise not defined.
C.2: Optional IF GAP 27/10 “Encrypted Data Key Material”, otherwise Excluded.
C.3: Optional IF GAP 26/6 “LL Privacy”, otherwise Excluded.
Table 27a: Periodic Advertising Modes and Procedures
Prerequisite: (GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”) AND CORE 2a/51 “Host Core v5.1 or later”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Periodic Advertising Synchronization Transfer procedure | [8] 9.5.4 | O | N/A |  |  |
| 2 | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising | [8] 9.5.3 | O | N/A |  |  |
| 3 | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising | [8] 9.5.3 | O | N/A |  |  |
| 4 | Periodic Advertising Sync Transfer - Sender | [8] 9.5.4 | C.1 | [15] LL 9/26 |  |  |
| 5 | Periodic Advertising Sync Transfer - Recipient | [8] 9.5.3 | C.2 | [15] LL 9/27 |  |  |
| 6 | Synchronizing to Periodic Advertising | [8] 9.5.3 | C.3 | [15] LL 11/1 |  |  |

C.1: Mandatory IF GAP 27a/1 “Periodic Advertising Synchronization Transfer procedure”, otherwise not defined.
C.2: Mandatory IF GAP 27a/2 “Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising” OR GAP 27a/3 “Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising”, otherwise not defined.
C.3: Mandatory IF GAP 27a/3 “Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising”, otherwise not defined.

##### 1.5.3.10 SM requirements

Table 27b: SM Requirements
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Peripheral Role (Responder) | N/A | M | [13] SM 1/2 |  |  |
| 2 | Authenticated MITM protection | [4] 10.3 | C.1 | [13] SM 2/1 |  |  |
| 3 | Unauthenticated no MITM protection | [4] 10.3 | C.2 | [13] SM 2/2 |  |  |
| 4 | No security requirements | [4] 10.3 | C.3 | [13] SM 2/3 |  |  |
| 5 | LE Secure Connections | [4] 10.3 | C.4 | [13] SM 2/5 |  |  |
| 6 | Encryption Key | [4] 9.4.3 | C.5 | [13] SM 7b/1 |  |  |
| 7 | Identity Key | [4] 10.7 | C.6 | [13] SM 7b/2 |  |  |
| 8 | Signing Key | [4] 10.4 | C.7 | [13] SM 7b/3 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 9 | Out of Band | [4] 10.4 | O | [13] SM 4/3 |  |  |
| 10 | Peripheral Initiated Security | [4] 10.3 | O | [13] SM 5/3 |  |  |

C.1: Mandatory IF GAP 25/7 “Authenticated Pairing (LE security Mode-1 level 3)” OR GAP 25/12 “Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only” OR (GAP 25/2 “LE security Mode-2” AND GAP 25/3 “Authentication procedure”), otherwise not defined.
C.2: Mandatory IF GAP 25/8 “Unauthenticated Pairing (LE security Mode-1 level 2)” OR GAP 25/11 “Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only” OR (GAP 25/2 “LE security Mode-2” AND NOT GAP 25/3 “Authentication procedure”), otherwise not defined.
C.3: Mandatory IF GAP 25/1 “LE security Mode-1” AND NOT GAP 25/8 “Unauthenticated Pairing (LE security Mode-1 level 2)” AND NOT GAP 25/7 “Authenticated Pairing (LE security Mode-1 level 3)”, otherwise not defined.
C.4: Mandatory IF GAP 25/9 “LE security Mode-1 level 4” OR GAP 25/11 “Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only” OR GAP 25/12 “Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only”, otherwise not defined.
C.5: Mandatory IF GAP 24/2 “Bondable mode”, otherwise not defined.
C.6: Mandatory IF GAP 26/3 “Resolvable private address generation procedure”, otherwise not defined.
C.7: Mandatory IF GAP 25/6 “Authenticate signed data procedure”, otherwise not defined.

##### 1.5.3.11 L2CAP requirements

Table 27c (auto-fill): L2CAP Requirements
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Detect insufficient authentication | [4] 10.3 | C.1 | [14] L2CAP 4/1 |  |  |
| 2 | Detect insufficient authorization | [4] 10.5 | C.2 | [14] L2CAP 4/2 |  |  |
| 3 | Detect insufficient encryption | [4] 2.2.2 | C.3 | [14] L2CAP 4/3 |  |  |

C.1: Mandatory IF GAP 25/3 “Authentication procedure", otherwise not defined.
C.2: Mandatory IF GAP 25/4 “Authorization procedure", otherwise not defined.
C.3: Mandatory IF GAP 21/3 “Encryption procedure”, otherwise not defined.

#### 1.5.4 Central


##### 1.5.4.1 Physical Layer

Table 28: Central Physical Layer
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Transmitter |  | [2] 2.2.2 |  | M |  |  |
| 2 |  |  | Receiver |  | [2] 2.2.2 |  | M |  |  |


##### 1.5.4.2 Link Layer Features


###### 1.5.4.2.1 Link Layer States

Table 29: Central Link Layer States
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Standby State | [2] 2.2.2 | M | N/A |  |  |
| 2 | Scanning State | [2] 2.2.2 | M | [15] LL 1/2 |  |  |
| 3 | Initiating State | [2] 2.2.2 | M | [15] LL 1/3 |  |  |
| 4 | Connection State (Central Role) | [2] 2.2.2 | M | [15] LL 1/5 |  |  |


###### 1.5.4.2.2 Scanning Types

Table 30: Central Link Layer Scanning Types
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Passive Scanning | [2] 2.2.2 | C.1 | [15] LL 4/1 |  |  |
| 2 | Active Scanning | [2] 2.2.2 | C.1 | [15] LL 4/3 |  |  |

C.1: Mandatory to support at least one.
Table 30a: Central Link Layer Scanning Data Types
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service UUID |  | [3] 1.1 |  | O |  |  |
| 2 |  |  | Local Name |  | [3] 1.2 |  | O |  |  |
| 3 |  |  | Flags |  | [3] 1.3 |  | O |  |  |
| 4 |  |  | Manufacturer Specific Data |  | [3] 1.4 |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 |  |  | TX Power Level |  |  | [3] 1.5 |  |  | O |  |  |
| 6 |  |  | Security Manager OOB |  |  | [3] 1.7 |  |  | O |  |  |
| 7 |  |  | Security Manager TK Value |  |  | [3] 1.8 |  |  | O |  |  |
| 8 |  |  | Peripheral Connection Interval Range |  |  | [3] 1.9 |  |  | O |  |  |
| 9 |  |  | Service Solicitation |  |  | [3] 1.10 |  |  | O |  |  |
| 10 |  |  | Service Data |  |  | [3] 1.11 |  |  | O |  |  |
| 11 |  |  | Appearance |  |  | [3] 1.12 |  |  | O |  |  |
| 12 |  |  | Public Target Address |  |  | [3] 1.13 |  |  | O |  |  |
| 13 |  |  | Random Target Address |  |  | [3] 1.14 |  |  | O |  |  |
| 14 |  |  | Advertising Interval |  |  | [3] 1.15 |  |  | O |  |  |
| 14a |  |  | Advertising Interval – Long |  |  | [3] 1.15 |  |  | O |  |  |
| 15 |  |  | LE Bluetooth Device Address |  |  | [3] 1.16 |  |  | O |  |  |
| 16 |  |  | LE Role |  |  | [3] 1.17 |  |  | O |  |  |
| 17 |  |  | Uniform Resource Identifier |  |  | [3] 1.18 |  |  | O |  |  |
| 18 |  |  | LE Supported features |  |  | [3] 1.19 |  |  | O |  |  |
| 19 |  |  | Encrypted Data |  |  | [3] 1.23 |  |  | O |  |  |
| 20 |  |  | Periodic Advertising Response Timing |  |  | [3] 1.24 |  |  | O |  |  |


##### 1.5.4.3 Control Procedures

Table 31: Central Link Layer Control Procedures
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connection Update procedure |  |  | [2] 2.2.2 |  |  | M |  |  |
| 2 |  |  | Channel Map Update procedure |  |  | [2] 2.2.2 |  |  | M |  |  |
| 3 |  |  | Encryption procedure |  |  | [2] 2.2.2 |  |  | C.3 |  |  |
| 4 |  |  | Central-initiated Feature Exchange procedure |  |  | [2] 2.2.2 |  |  | M |  |  |
| 5 |  |  | Version Exchange procedure |  |  | [2] 2.2.2 |  |  | M |  |  |
| 6 |  |  | Termination procedure |  |  | [2] 2.2.2 |  |  | M |  |  |
| 7 |  |  | LE Ping procedure |  |  | [4] 2.2.2 |  |  | O |  |  |
| 8 |  |  | Peripheral-initiated Feature Exchange procedure |  |  | [4] 2.2.2 |  |  | C.1 |  |  |
| 9 |  |  | Connection Parameter Request procedure |  |  | [4] 2.2.2 |  |  | O |  |  |
| 10 |  |  | Data Length Update procedure |  |  | [8] 2.2.2 |  |  | O |  |  |
| 11 |  |  | PHY Update procedure |  |  | [8] 2.2.2 |  |  | C.2 |  |  |
| 12 |  |  | Minimum Number Of Used Channels procedure |  |  | [8] 2.2.2 |  |  | C.2 |  |  |

C.1: Mandatory IF GAP 31/9 “Connection Parameter Request procedure”, otherwise Optional.
C.2: Optional IF CORE 2a/50 “Host Core v5.0 or later”, otherwise Excluded.
C.3: Mandatory IF GAP 35/6 “Authenticate signed data procedure” OR GAP 35/7 “Authenticated Pairing (LE security Mode-1 level 3)” OR GAP 35/9 “LE security Mode-1 level 4”, otherwise Optional.
Table 32: Central Discovery Modes and Procedures
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Limited Discovery procedure |  |  | [4] 9.2.5 |  |  | O |  |  |
| 2 |  |  | General Discovery procedure |  |  | [4] 9.2.6 |  |  | M |  |  |
| 3 |  |  | Name Discovery procedure |  |  | [4] 9.2.7 |  |  | O |  |  |


##### 1.5.4.5 Connection Modes and Procedures

Table 33: Central Connection Modes and Procedures
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Auto connection establishment procedure | [2] 9.3.5 | O | N/A |  |  |
| 2 | General connection establishment procedure | [4] 9.3.6 | O | N/A |  |  |
| 3 | Selective connection establishment procedure | [2] 9.3.7 | O | N/A |  |  |
| 4 | Direct connection establishment procedure | [2] 9.3.8 | M | N/A |  |  |
| 5 | Connection parameter update procedure | [2] 9.3.9 | M | N/A |  |  |
| 6 | Terminate connection procedure | [2] 9.3.10 | M | N/A |  |  |
| 7 | Connected Isochronous Stream Central Establishment procedure | [10] 9.3.13 | C.1 | N/A |  |  |
| 8 | Connected Isochronous Stream Terminate procedure | [10] 9.3.15 | C.1 | N/A |  |  |
| 8a | Connected Isochronous Stream - Central | [10] 9.3.13, 9.3.15 | O | [15] LL 9/31 |  |  |
| 9 | Connection Subrate procedure | [11] 9.3.16 | C.2 | N/A |  |  |
| 10 | Periodic Advertising Connection procedure | [12] 9.3.17 | O | N/A |  |  |
| 11 | Scanning for Periodic Advertising with Responses | [12] 9.3.17 | C.3 | [15] LL 4/8a |  |  |

C.1: Mandatory IF GAP 33/8a “Connected Isochronous Stream - Central”, otherwise Excluded.
C.2: Optional IF CORE 2a/53 “Host Core v5.3 or later”, otherwise Excluded.
C.3: Mandatory IF GAP 33/10 “Periodic Advertising Connection procedure”, otherwise not defined.
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CS Initiator Role | [16] 9.7.1 | C.1 | [16] LL 1/7 |  |  |
| 2 | CS Reflector Role | [16] 9.7.1 | C.2 | [16] LL 1/8 |  |  |

C.1: Mandatory IF NOT GAP 23a/1 “CS Initiator Role”, otherwise Optional.
C.2: Mandatory IF NOT GAP 23a/2 “CS Reflector Role”, otherwise Optional.

##### 1.5.4.6 Bonding Modes and Procedures

Table 34: Central Bonding Modes and Procedures
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Non-bondable mode |  |  | [4] 9.4.2, 13.2 |  |  | M |  |  |
| 2 |  |  | Bondable mode |  |  | [4] 9.4.3, 13.2 |  |  | O |  |  |
| 3 |  |  | Bonding procedure |  |  | [4] 9.4.4, 13.2 |  |  | C.1 |  |  |

C.1: Mandatory IF GAP 34/2 “Bondable mode”, otherwise Excluded.

##### 1.5.4.7 Security Aspects

Table 35: Central Security Features
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE security Mode-1 |  |  | [2] 10.2.1 |  |  | O |  |  |
| 2 |  |  | LE security Mode-2 |  |  | [2] 10.2.2 |  |  | O |  |  |
| 3 |  |  | Authentication procedure |  |  | [2] 10.3 |  |  | O |  |  |
| 4 |  |  | Authorization procedure |  |  | [2] 10.5 |  |  | O |  |  |
| 5 |  |  | Connection data signing procedure |  |  | [2] 10.4.1 |  |  | O |  |  |
| 6 |  |  | Authenticate signed data procedure |  |  | [2] 10.4.3 |  |  | O |  |  |
| 7 |  |  | Authenticated Pairing (LE security Mode-1 level 3) |  |  | [2] 10.3 |  |  | C.1 |  |  |
| 8 |  |  | Unauthenticated Pairing (LE security Mode-1 level 2) |  |  | [2] 10.3 |  |  | C.1 |  |  |
| 9 |  |  | LE security Mode-1 level 4 |  |  | [5] 10.3 |  |  | C.1 |  |  |
| 10 |  |  | Secure Connections Only mode |  |  | [12] 10.2.4, 14.3 |  |  | C.3 |  |  |
| 11 |  |  | Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only |  |  | [5] 10.3 |  |  | C.1 |  |  |
| 12 |  |  | Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only |  |  | [5] 10.3 |  |  | C.1 |  |  |
| 13 |  |  | Minimum 128 Bit entropy key |  |  | [5] 10.3 |  |  | C.4 |  |  |
| 13a |  |  | Minimum 128 Bit entropy key, LE security Mode-1 level 4 |  |  | [5] 10.3 |  |  | C.5 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13b |  |  | Minimum 128 Bit entropy key, LE security Mode-1 level 3 |  |  | [5] 10.3 |  |  | C.6 |  |  |
| 13c |  |  | Minimum 128 Bit entropy key, LE security Mode-1 level 2 |  |  | [5] 10.3 |  |  | C.7 |  |  |
| 14 |  |  | Encrypted Advertising Data Procedure |  |  | [12] 10.10 |  |  | O |  |  |
| 15 |  |  | Client security checks for GATT indications and notifications |  |  | [11] 10.3.2.2 |  |  | O |  |  |
| 16 |  |  | Channel Sounding Security Level 1 |  |  | [16] 10.11.1 |  |  | C.8 |  |  |
| 17 |  |  | Channel Sounding Security Level 2 |  |  | [16] 10.11.1 |  |  | C.9 |  |  |
| 18 |  |  | Channel Sounding Security Level 3 |  |  | [16] 10.11.1 |  |  | C.10 |  |  |
| 19 |  |  | Channel Sounding Security Level 4 |  |  | [16] 10.11.1 |  |  | C.11 |  |  |

C.1: Optional IF GAP 35/1 “LE security Mode-1”, otherwise Excluded.
C.2: No longer used.
C.3: Mandatory IF GAP 2/11 “Secure Connections Only Mode” OR GAP 25/10 “Secure Connections Only mode”, otherwise Optional IF GAP 35/9 “LE security Mode-1 level 4”, otherwise Excluded.
C.4: Mandatory IF GAP 35/13a “Minimum 128 Bit entropy key, LE security Mode-1 level 4” OR GAP 35/13b “Minimum 128 Bit entropy key, LE security Mode-1 level 3” OR GAP 35/13c “Minimum 128 Bit entropy key, LE security Mode-1 level 2”, otherwise Excluded.
C.5: Mandatory IF GAP 35/9 “LE security Mode-1 level 4”, otherwise Excluded.
C.6: Optional IF GAP 35/12 “Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only”, otherwise Excluded.
C.7: Optional IF GAP 35/11 “Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only”, otherwise Excluded.
C.8: Mandatory IF GAP 35a/1 “CS Mode-2” OR GAP 35a/2 “CS Mode-3” OR GAP 25a/3 “CS RTT Access Address, 10 ns” OR GAP 35a/4 “CS RTT Access Address, 150 ns”, otherwise Excluded.
C.9: Mandatory IF GAP 35a/4 “CS RTT Access Address, 150 ns”, otherwise Excluded.
C.10: Mandatory IF GAP 35a/3 “CS RTT Access Address, 10 ns”, otherwise Excluded.
C.11: Mandatory IF GAP 35a/2 “CS Mode-3” AND (GAP 35a/5 “CS RTT Sounding Sequence, 10 ns” OR GAP 35a/6 “CS RTT Sounding Sequence, 150 ns” OR GAP 35a/7 “CS RTT Random Payload, 10 ns” OR GAP 35a/8 “CS RTT Random Payload, 150 ns”), otherwise Excluded.
Table 35a: Central Security Features
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CS Mode-2 | [16] 10.11 | M | [16] LL 13/2 |  |  |
| 2 | CS Mode-3 | [16] 10.11 | O | [16] LL 13/3 |  |  |
| 3 | CS RTT Access Address, 10 ns | [16] 10.11.1 | C.1 | [16] LL 13/4 |  |  |
| 4 | CS RTT Access Address, 150 ns | [16] 10.11.1 | C.1 | [16] LL 13/5 |  |  |
| 5 | CS RTT Sounding Sequence, 10 ns | [16] 10.11.1 | C.2 | [16] LL 13/6 |  |  |
| 6 | CS RTT Sounding Sequence, 150 ns | [16] 10.11.1 | C.2 | [16] LL 13/7 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 7 | CS RTT Random Payload, 10 ns | [16] 10.11.1 | C.3 | [16] LL 13/8 |  |  |
| 8 | CS RTT Random Payload, 150 ns | [16] 10.11.1 | C.3 | [16] LL 13/9 |  |  |

C.1: Mandatory to support one and only one.
C.2: Mandatory to support one and only one.
C.3: Mandatory to support one and only one.

##### 1.5.4.8 Privacy Feature

Table 36: Central Privacy Feature
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Privacy feature |  |  | [5] 10.7 |  |  | O |  |  |  |  |  |
| 2 |  |  | Non-resolvable private address generation procedure |  |  | [5] 10.7, 10.8.2.1 [6] 1.3.2.2 |  |  | O |  |  |  |  |  |
| 3 |  |  | Resolvable private address resolution procedure |  |  | [5] 10.7, 10.8.2.3 [6] 1.3.2.2 |  |  | C.1 |  |  |  |  |  |
| 4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |  |  |  |
| 5 |  |  | Resolvable private address generation procedure |  |  | [5] 10.7, 10.8.2.2 [6] 1.3.2.3 |  |  | C.1 |  |  |  |  |  |
| 6 |  |  | Controller-based privacy |  |  | [5] 10.7 |  |  | O |  |  |  |  |  |

C.1: Mandatory IF GAP 36/1 “Privacy feature”, otherwise Optional.

##### 1.5.4.9 Generic Access Profile Characteristics

Table 37: Central GAP Characteristics
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Device Name | [2] 12.1 | M | N/A |  |  |
| 2 | Appearance | [2] 12.2 | M | N/A |  |  |
| 3 | Central Address Resolution | [5] 12.4 | O | N/A |  |  |
| 3a | Resolution of private addresses | [5] 12.4 | C.1 | [15] LL 2/5 |  |  |
| 4 | LE GATT Security Levels | [12] 12.7 | O | N/A |  |  |
| 5 | Resolvable Private Address Only | [2] 12.5 | C.2 | N/A |  |  |
| 6 | Writable Device Name | [2] 12.1 | O | N/A |  |  |
| 7 | Writable Appearance | [2] 12.2 | O | N/A |  |  |

C.1: Mandatory IF GAP 37/3 “Central Address Resolution”, otherwise not defined.
C.2: Optional IF GAP 37/3a “Resolution of private addresses”, otherwise Excluded.
Table 37a: Periodic Advertising Modes and Procedures
Prerequisite: (GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”) AND CORE 2a/51 “Host Core v5.1 or later”

| Item | Capability | Reference | Status | Inter-Layer Dependency |
| --- | --- | --- | --- | --- |
| 1 | Periodic Advertising Synchronization Transfer procedure | [8] 9.5.4 | O | N/A |
| 2 | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising | [8] 9.5.3 | O | N/A |
| 3 | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising | [8] 9.5.3 | O | N/A |
| 4 | Periodic Advertising Sync Transfer - Sender | [8] 9.5.4 | C.1 | [15] LL 9/26 |
| 5 | Periodic Advertising Sync Transfer - Recipient | [8] 9.5.3 | C.2 | [15] LL 9/27 |
| 6 | Synchronizing to Periodic Advertising | [8] 9.5.3 | C.3 | [15] LL 11/1 |

C.1: Mandatory IF GAP 37a/1 “Periodic Advertising Synchronization Transfer procedure”, otherwise not defined.
C.2: Mandatory IF GAP 37a/2 “Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising” OR GAP 37a/3 “Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising”, otherwise not defined.
C.3: Mandatory IF GAP 37a/3 “Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising”, otherwise not defined.

##### 1.5.4.11 SM requirements

Table 37b: SM Requirements
Prerequisite: GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Central Role (Initiator) | N/A | M | [13] SM 1/1 |  |  |
| 2 | Authenticated MITM protection | [4] 10.3 | C.1 | [13] SM 2/1 |  |  |
| 3 | Unauthenticated no MITM protection | [4] 10.3 | C.2 | [13] SM 2/2 |  |  |
| 4 | No security requirements | [4] 10.3 | C.3 | [13] SM 2/3 |  |  |
| 5 | LE Secure Connections | [4] 10.3 | C.4 | [13] SM 2/5 |  |  |
| 6 | Encryption Key | [4] 9.4.3 | C.5 | [13] SM 7a/1 |  |  |
| 7 | Identity Key | [4] 10.7 | C.6 | [13] SM 7a/2 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 8 | Signing Key | [4] 10.4 | C.7 | [13] SM 7a/3 |  |  |
| 9 | Out of Band | [4] 10.4 | O | [13] SM 4/3 |  |  |

C.1: Mandatory IF GAP 35/7 “Authenticated Pairing (LE security Mode-1 level 3)” OR GAP 35/12 “Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only” OR (GAP 35/2 “LE security Mode-2” AND GAP 35/3 “Authentication procedure”), otherwise not defined.
C.2: Mandatory IF GAP 35/8 “Unauthenticated Pairing (LE security Mode-1 level 2)” OR GAP 35/11 “Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only” OR (GAP 35/2 “LE security Mode-2” AND NOT GAP 35/3 “Authentication procedure”), otherwise not defined.
C.3: Mandatory IF GAP 35/1 “LE security Mode-1” AND NOT GAP 35/8 “Unauthenticated Pairing (LE security Mode-1 level 2)” AND NOT GAP 35/7 “Authenticated Pairing (LE security Mode-1 level 3)”, otherwise not defined.
C.4: Mandatory IF GAP 35/9 “LE security Mode-1 level 4” OR GAP 35/11 “Unauthenticated Pairing (LE security Mode-1 level 2) with LE Secure Connections Pairing only” OR GAP 35/12 “Authenticated Pairing (LE security Mode-1 level 3) with LE Secure Connections Pairing only”, otherwise not defined.
C.5: Mandatory IF GAP 34/2 “Bondable mode”, otherwise not defined.
C.6: Mandatory IF GAP 36/5 “Resolvable private address generation procedure”, otherwise not defined.
C.7: Mandatory IF GAP 35/6 “Authenticate signed data procedure”, otherwise not defined.

##### 1.5.4.12 L2CAP requirements

Table 37c (auto-fill): L2CAP Requirements
Prerequisite: GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Detect insufficient authentication | [2] 10.3 | C.1 | [14] L2CAP 4/1 |  |  |
| 2 | Detect insufficient authorization | [2] 10.5 | C.2 | [14] L2CAP 4/2 |  |  |
| 3 | Detect insufficient encryption | [2] 2.2.2 | C.3 | [14] L2CAP 4/3 |  |  |

C.1: Mandatory IF GAP 35/3 “Authentication procedure", otherwise not defined.
C.2: Mandatory IF GAP 35/4 “Authorization procedure", otherwise not defined.
C.3: Mandatory IF GAP 31/3 “Encryption procedure”, otherwise not defined.

### 1.6 BR/EDR/LE Capability Statement

Table 38: BR/EDR/LE Roles
Prerequisite: GAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcaster |  |  | [2] 13 |  |  | C.1 |  |  |
| 2 |  |  | Observer |  |  | [2] 13 |  |  | C.1 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Peripheral |  |  | [2] 13 |  |  | C.1 |  |  |
| 4 |  |  | Central |  |  | [2] 13 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.
Note: Table 38 is applicable for BR/EDR/LE configurations. For LE configurations, see Table 5 for role declarations.

#### 1.6.1 Central


##### 1.6.1.1 Modes

Table 39: No longer used

##### 1.6.1.2 Idle Mode Procedures

Table 40: No longer used

##### 1.6.1.3 Security Aspects

Table 41: Central BR/EDR/LE Security Aspects
Prerequisite: GAP 38/4 “Central (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Security aspects | [2] 14 | M | N/A |  |  |
| 2 | Cross Transport Key Derivation Supported | [4] 14.1 | C.1 | [13] SM 8a/1 |  |  |
| 2a | Derivation of BR/EDR Link Key from LE LTK | [4] 14.1 | C.2 | [13] SM 8a/3 |  |  |
| 2b | Derivation of LE LTK from BR/EDR Link Key | [4] 14.1 | C.3 | [13] SM 8a/2 |  |  |

C.1: Mandatory IF GAP 41/2a “Derivation of BR/EDR Link Key from LE LTK” AND GAP 41/2b “Derivation of LE LTK from BR/EDR Link Key”, otherwise not defined.
C.2: Optional IF GAP 35/9 “LE security Mode-1 level 4”, otherwise not defined.
C.3: Optional IF GAP 2/7a “Security Mode-4, level 4”, otherwise not defined.

##### 1.6.1.4 Simultaneous Transports

Table 44: Central Simultaneous BR/EDR and LE Transports
Prerequisite: GAP 38/4 “Central (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Simultaneous BR/EDR and LE Transports – BR/EDR Peripheral to the same device |  |  | [4] 13.1.1 |  |  | O |  |  |
| 2 |  |  | Simultaneous BR/EDR and LE Transports – BR/EDR Central to the same device |  |  | [4] 13.1.1 |  |  | O |  |  |


#### 1.6.2 Peripheral


##### 1.6.2.1 Modes

Table 42: No longer used

##### 1.6.2.2 Security Aspects

Table 43: Peripheral BR/EDR/LE Security Aspects
Prerequisite: GAP 38/3 “Peripheral (BR/EDR/LE)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Security aspects | [2] 14 | M | N/A |  |  |
| 2 | Cross Transport Key Derivation Supported | [4] 14.1 | C.1 | [13] SM 8b/1 |  |  |
| 2a | Derivation of BR/EDR Link Key from LE LTK | [4] 14.1 | C.2 | [13] SM 8b/3 |  |  |
| 2b | Derivation of LE LTK from BR/EDR Link Key | [4] 14.1 | C.3 | [13] SM 8b/2 |  |  |

C.1: Mandatory IF GAP 43/2a “Derivation of BR/EDR Link Key from LE LTK” AND GAP 43/2b “Derivation of LE LTK from BR/EDR Link Key”, otherwise not defined.
C.2: Optional IF GAP 25/9 “LE security Mode-1 level 4”, otherwise not defined.
C.3: Optional IF GAP 2/7a “Security Mode-4, level 4”, otherwise not defined.

##### 1.6.2.3 Simultaneous Transports

Table 45: Peripheral Simultaneous BR/EDR and LE Transports
Prerequisite: GAP 38/3 “Peripheral (BR/EDR/LE)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Simultaneous BR/EDR and LE Transports – BR/EDR Peripheral to the same device |  |  | [4] 13.1.1 |  |  | O |  |  |
| 2 |  |  | Simultaneous BR/EDR and LE Transports – BR/EDR Central to the same device |  |  | [4] 13.1.1 |  |  | O |  |  |


## 2 References

[1] Specification of the Bluetooth System, Volume 3, Part C (Generic Access Profile), Version 2.1 or later
[2] Specification of the Bluetooth System, Volume 3, Part C, Version 4.0 or later
[3] Core Specification Supplement (CSS), Part A, Current Version
[4] Specification of the Bluetooth System, Volume 3, Part C, Version 4.1 or later
[5] Specification of the Bluetooth System, Volume 3, Part C, Version 4.2 or later
[6] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Specification)
[7] Specification of the Bluetooth System, Volume 3, Part C, Version 5.0 or later
[8] Specification of the Bluetooth System, Volume 3, Part C, Version 5.1 or later
[9] Core Erratum 11838 Key Size Updates
[10] Specification of the Bluetooth System, Volume 3, Part C, Version 5.2
[11] Specification of the Bluetooth System, Volume 3, Part C, Version 5.3 or later
[12] Specification of the Bluetooth System, Volume 3, Part C, Version 5.4 or later
[13] ICS Proforma for Security Manager (SM)
[14] ICS Proforma for Logical Link Control and Adaptation Protocol (L2CAP)
[15] ICS Proforma for Link Layer (LL)
[16] Specification of the Bluetooth System, Volume 3, Part C, Version 6.0 or later

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | D10R00 | D10R00 |  | 2004-03-10 |  |  |  | Re-partitioned to match Main Specification |  |
|  |  |  |  |  |  |  |  |  |  | Volume/Part partitioning. |  |
|  |  |  |  | D10r01 |  |  | 2004-03-11 |  |  | Editorial changes. |  |
|  |  |  | D12r02 | D12r02 |  | 2004-03-23 | 2004-03-23 |  |  | Editorial changes. Changed reference and document |  |
|  |  |  |  |  |  |  |  |  |  | numbering to D12 to reflect applicable Bluetooth |  |
|  |  |  |  |  |  |  |  |  |  | version. |  |
|  |  |  |  | D12r03 |  |  | 2004-03-25 |  |  | Editorial changes. |  |
| 10 | 10 |  | 1.2.2 | 1.2.2 |  | 2004-03-29 | 2004-03-29 |  |  | Changed document number and revision number to |  |
|  |  |  |  |  |  |  |  |  |  | conform to legacy system. Added Disclaimer and |  |
|  |  |  |  |  |  |  |  |  |  | Copyright Notice. |  |
|  | 11 |  |  | 1.2.3 |  |  | 2005-01-13 |  |  | Release after review. |  |
|  |  |  |  | 1.2.4r0 |  |  | 2005-09-20 |  |  | Changed cover page to refer 1.2/2.0/2.0+EDR |  |
|  | 12 |  |  | 1.2.4 |  |  | 2005-11-09 |  |  | Prepare for publication. |  |
|  |  |  |  | 2.1.E.0r0 |  |  | 2006-11-29 |  |  | Updates to Table 2 and Table 3 for Simple Pairing |  |
|  |  |  | 2.1.E.0r1 | 2.1.E.0r1 |  | 2006-12-14 | 2006-12-14 |  |  | Changed document number, updates to Table 2 |  |
|  |  |  |  |  |  |  |  |  |  | status and footnotes |  |
|  | 13 |  |  | 2.1.E.0 |  |  | 2006-12-28 |  |  | Prepare for publication. |  |
|  |  |  | 2.1.E.1r0 | 2.1.E.1r0 |  | 2008-02 | 2008-02 |  |  | TSE 2279: Table 2 C1 and C2 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2283: Table 2, Note 3. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2289: Table 3: C1 change |  |
|  | 14 |  |  | 2.1.E.1 |  |  | 2008-04-29 |  |  | Publication version. |  |
|  |  |  | 2.1.E.2r0-1 | 2.1.E.2r0-1 |  |  | 2008-10- |  |  | TSE 2638, TSE 2631, TSE 2494; Add rows to Table |  |
|  |  |  |  |  |  |  | 08/29 |  |  | 2. |  |
|  | 15 |  |  | 2.1.E.2 |  |  | 2008-12-12 |  |  | Prepare for publication. |  |
|  |  |  | 2.1.E.2a | 2.1.E.2a |  | 2009-04-21 | 2009-04-21 |  |  | Update conditionals to reflect the addition of Core |  |
|  |  |  |  |  |  |  |  |  |  | Specification 3.0/3.0+HS |  |
| 16 |  |  | 2.1.E.3 |  |  | 2009-08-12 |  |  |  | TSE 2649: Change Table 2 Footnote C.7 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2979: Table 2 Footnote C.4 updated. |  |
| 17 |  |  | 4.0.0d4 d12 |  |  | 2010-06-09 – 2010-07-01 |  |  |  | Document merge between GAP ICS 2.1.E.3 and LE |  |
|  |  |  |  |  |  |  |  |  |  | specific GAP ICS called 0.9d3 dated 2010-06-09 56T |  |
|  |  |  |  |  |  |  |  |  |  | References to Volume 3 Part C versions 2.0 or later |  |
|  |  |  |  |  |  |  |  |  |  | [1] separated from references to Volume 3 Part C |  |
|  |  |  |  |  |  |  |  |  |  | versions 4.0 or later [2]. |  |
|  |  |  |  |  |  |  |  |  |  | TSE3788 “Pairable” changed to “Bondable” in table 1 |  |
|  |  |  |  |  |  |  |  |  |  | Updated BR/EDR/LE ICS to align with the latest |  |
|  |  |  |  |  |  |  |  |  |  | errata in Tokyo v13 |  |
|  |  |  |  |  |  |  |  |  |  | Updated BR/EDR/LE ICS with review comment |  |
|  |  |  |  |  |  |  |  |  |  | resolution |  |
|  |  |  |  |  |  |  |  |  |  | Updated BR/EDR/LE ICS with review comment |  |
|  |  |  |  |  |  |  |  |  |  | resolution |  |
|  |  |  |  |  |  |  |  |  |  | SUM ICS references added to 0/x- conditions |  |
|  |  |  |  |  |  |  |  |  |  | Change in C.1, table 22 |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | Table 38, informative note removed – created more |  |
|  |  |  |  |  |  |  |  |  |  | problems than it solved |  |
|  |  |  |  |  |  |  |  |  |  | 0/3 added as a prerequisite in section 1.4 |  |
|  |  |  |  |  |  |  |  |  |  | BR/EDR/LE Central and Peripheral prerequisite |  |
|  |  |  |  |  |  |  |  |  |  | added to relevant ICS sub-sections of section 1.4 LE |  |
|  |  |  |  |  |  |  |  |  |  | Capability Statement. 0/3 is no longer a prerequisite in |  |
|  |  |  |  |  |  |  |  |  |  | section 1.4. |  |
|  |  |  |  |  |  |  |  |  |  | Comment resolutions to the addition of the |  |
|  |  |  |  |  |  |  |  |  |  | BR/EDR/LE Central and Peripheral prerequisites. |  |
|  |  |  |  |  |  |  |  |  |  | Corrections, where prerequisites were transferred to |  |
|  |  |  |  |  |  |  |  |  |  | conditions in tables 18-24, 28-37 |  |
|  |  |  |  |  |  |  |  |  |  | Corrected confusion around multiple C.1 in table 34 |  |
|  |  |  |  |  |  |  |  |  |  | Update contributors list |  |
|  |  |  | 4.0.1r0-r3 |  |  | 2010-10-09 – 2011-03-09 |  |  |  | TSE 3289: Changed IF 2/6…to IF 2/7… |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3849:Table 22: Footnote C1: |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3848: Table 20/C.3: Change M to O |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3788: Table 1/6 and 1/7: rename |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3862: Add Tables 8A and 20A |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4090: Table 20, footnote C.3 (same change as |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3848) |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4116: Table 25,Add item 7 |  |
|  |  |  |  |  |  |  |  |  |  | Input MS review comments: |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4116 (was made only to test spec) |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4244: Delete Annex A |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4245: Add pre-requisite “Prerequisite: GAP 5/3” |  |
|  |  |  |  |  |  |  |  |  |  | to the following tables 18, 19, 20, 20A, 22, 23 ,24 |  |
|  |  |  |  |  |  |  |  |  |  | Add prerequisite 5/4 from tables 27 to 38 |  |
|  |  |  |  |  |  |  |  |  |  | Input SL’s comments: TSE 3849: fix footnote, fix Rev. |  |
|  |  |  |  |  |  |  |  |  |  | His. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4305: Add prerequisite: “GAP 5/3 or GAP 38/3” |  |
|  |  |  |  |  |  |  |  |  |  | to Tables: 18, 19, 20, 20A, 21, 22, 23, 24, 25, 26 & |  |
|  |  |  |  |  |  |  |  |  |  | 27 ; Add prerequisite: “GAP 5/4 or GAP 38/4” to |  |
|  |  |  |  |  |  |  |  |  |  | Tables: 28, 29, 30, 31, 32, 33, 34, 35, 36 & 37 |  |
| 18 |  |  | 4.0.1 |  |  | 2011-07-20 |  |  |  | Prepare for publication. Add Reference section in |  |
|  |  |  |  |  |  |  |  |  |  | place of Section 1 text. |  |
|  |  |  | 4.0.2r0 |  |  | 2011-11-21 |  |  |  | TSE 4560 Table 27: Two new rows |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3865: Same as 3955—TPG only? |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4330: Change prerequisites for 1.4, Tables 6 – |  |
|  |  |  |  |  |  |  |  |  |  | 11, and Tables 12-17 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4451: Change Table 27 C.2 to refer to correct |  |
|  |  |  |  |  |  |  |  |  |  | table |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4561: Table 2 References and Note 3. |  |
|  |  |  |  | 4.0.2r1 |  |  | 2012-01-31 |  |  | TSE 4330: Update Prerequisite for Table 8 |  |
|  | 19 |  |  | 4.0.2 |  |  | 2012-03-30 |  |  | Changed wording in §1.1.1. Prepare for publication |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 4.0.3r0 | 4.0.3r0 |  | 2012-05-16 |  |  |  | TSE 4568 Table 24: add row 4 and footnote C.3 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4573 Table 25, add row 8 and footnote C.1; |  |
|  |  |  |  |  |  |  |  |  |  | Table 35, change status from C.1 to O, add rows 7 |  |
|  |  |  |  |  |  |  |  |  |  | and 8; modify footnote C.1 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4740: Change Table 2/3 and Table 2/10 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4741: Add 27/8 and 36/4 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4751: Table 5, Table 38: Change titles, add |  |
|  |  |  |  |  |  |  |  |  |  | notes. Table 38: Change O to C.1 and add conditional |  |
|  |  |  |  |  |  |  |  |  |  | footnote. |  |
|  |  |  | 4.0.3r1 |  |  | 2012-06-11 |  |  |  | Editorial updates for TSE 4741 |  |
|  |  |  |  |  |  |  |  |  |  | Table 0a introduced for CSA3 declaration and |  |
|  |  |  |  |  |  |  |  |  |  | requirements. C.2 updated in Table 27 to address |  |
|  |  |  |  |  |  |  |  |  |  | errata 4202 requirements. |  |
|  | 20 |  |  | 4.0.3 |  |  | 2012-07-24 |  |  | Prepare for publication. |  |
|  |  |  | 4.0.4r0 | 4.0.4r0 |  | 2012-10-10 | 2012-10-10 |  |  | TSE 4966: Update to conditionals in Table 17 and |  |
|  |  |  |  |  |  |  |  |  |  | addition of Item 4. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4873: Added conditional to Table 8 A and Table |  |
|  |  |  |  |  |  |  |  |  |  | 20A. |  |
|  |  |  | 4.0.4r1 |  |  | 2012-11-29 |  |  |  | Per BQRB review: |  |
|  |  |  |  |  |  |  |  |  |  | Added [3] Core Specification Supplement (CSS) v2, |  |
|  |  |  |  |  |  |  |  |  |  | Part A |  |
|  |  |  |  |  |  |  |  |  |  | Add section reference to [3] in table 8A and table 20A |  |
|  |  |  | 4.0.4r2 |  |  | 2012-12-05 |  |  |  | TSE 5033: Correction to Table 20A conditionals to |  |
|  |  |  |  |  |  |  |  |  |  | remove Connected Directed Event and Add |  |
|  |  |  |  |  |  |  |  |  |  | Scannable Undirected Event. |  |
|  | 21 |  |  | 4.0.4 |  |  | 2012-11-29 |  |  | Prepare for Publication |  |
|  |  |  |  | 4.0.5r1 |  |  | 2012-12-21 |  |  | Connectionless Broadcast Change Request |  |
|  |  |  | 4.0.5r2 | 4.0.5r2 |  | 2013-01-02 | 2013-01-02 |  |  | Connectionless Broadcast Review: |  |
|  |  |  |  |  |  |  |  |  |  | Table 1 revised C.4 conditional |  |
|  |  |  |  |  |  |  |  |  |  | Table 4, revised C.1 conditional |  |
|  |  |  | 4.0.5r3 |  |  | 2013-01-03 |  |  |  | Connectionless Broadcast Review: |  |
|  |  |  |  |  |  |  |  |  |  | Table 1/9 synchronizable mode edit to conditional |  |
|  |  |  |  |  |  |  |  |  |  | C.4. |  |
|  |  |  | 4.0.5r4 |  |  | 2013-01-22 |  |  |  | Connectionless Broadcast Review (Jason & Magnus) |  |
|  |  |  |  |  |  |  |  |  |  | Added “…or later” after CSA4 conditionals |  |
|  |  |  |  |  |  |  |  |  |  | Update to References Section, added CSA3 and |  |
|  |  |  |  |  |  |  |  |  |  | CSA4 cross-references |  |
|  |  |  | 4.0.5r5 |  |  | 2013-01-24 |  |  |  | Connectionless Broadcast Review (Jason, Alicia, |  |
|  |  |  |  |  |  |  |  |  |  | Meagan) |  |
|  |  |  |  |  |  |  |  |  |  | Edited for consistent language and syntax for |  |
|  |  |  |  |  |  |  |  |  |  | conditionals. |  |
|  | 22 |  |  | 4.0.5 |  |  | 2013-02-12 |  |  | Prepare for Publication |  |
|  |  |  | 4.0.6r1 | 4.0.6r1 |  | 2013-02-13 | 2013-02-13 |  |  | Editorial error in Table 17. C.1 Conditional corrected |  |
|  |  |  |  |  |  |  |  |  |  | to read 17/1 (Privacy Feature). C.1 and C.3 edited for |  |
|  |  |  |  |  |  |  |  |  |  | clarity. |  |
|  |  |  |  |  |  |  |  |  |  | Approved by BTI & BQRB |  |
|  | 23 |  |  | 4.0.6 |  |  | 2013-02-19 |  |  | Prepare for Publication |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 4.0.7r1 | 4.0.7r1 |  | 2013-05-30 |  |  |  | TSE 5063: |  |
|  |  |  |  |  |  |  |  |  |  | •Updated title of section 1.4 to “LE Only Capability |  |
|  |  |  |  |  |  |  |  |  |  | Statement” |  |
|  |  |  |  |  |  |  |  |  |  | •Removed conditionals from Table 19, already |  |
|  |  |  |  |  |  |  |  |  |  | covered in the prerequisite. All items changed to |  |
|  |  |  |  |  |  |  |  |  |  | Mandatory. |  |
|  |  |  |  |  |  |  |  |  |  | •Removed conditionals from Table 20, already |  |
|  |  |  |  |  |  |  |  |  |  | covered in the prerequisite. Item 1 and 4 changed to |  |
|  |  |  |  |  |  |  |  |  |  | Mandatory, Item 2 and 3 as optional. |  |
|  |  |  |  |  |  |  |  |  |  | •Updated conditionals for Table 22, removed “AND |  |
|  |  |  |  |  |  |  |  |  |  | (20/1 OR 20/3 OR 20/4) from C.1, and updated |  |
|  |  |  |  |  |  |  |  |  |  | parenthesis and language in C.2 and C.3. |  |
|  |  |  |  |  |  |  |  |  |  | •Removed C.1 and C.2 from Table 23, updated C.3 to |  |
|  |  |  |  |  |  |  |  |  |  | be C.1. Item 1 status changed to C.1, items 2 and 4 |  |
|  |  |  |  |  |  |  |  |  |  | changed to optional, and items 3 and 5 updated to |  |
|  |  |  |  |  |  |  |  |  |  | Mandatory. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5091: Updated Table 20A item 6 status to C.3, |  |
|  |  |  |  |  |  |  |  |  |  | added “C.2: Mandatory if 22/2 or 22/3 is supported, |  |
|  |  |  |  |  |  |  |  |  |  | otherwise Optional” C.2 had been included in an |  |
|  |  |  |  |  |  |  |  |  |  | earlier version and was still needed, former C.2 |  |
|  |  |  |  |  |  |  |  |  |  | became C.3. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5100: Updated C.4 in Table 2 to remove “SUM |  |
|  |  |  |  |  |  |  |  |  |  | ICS 31/5” because the item no longer exists. |  |
|  |  |  | 4.0.7r2 |  |  | 2013-06-04 |  |  |  | Fixed the TSE reference number in the Change |  |
|  |  |  |  |  |  |  |  |  |  | History. |  |
|  |  |  |  |  |  |  |  |  |  | Table 0a – changed Device to Version Configuration |  |
|  |  |  |  |  |  |  |  |  |  | to match the Table title. |  |
|  |  |  |  |  |  |  |  |  |  | Added the ICS item description in parenthesis to |  |
|  |  |  |  |  |  |  |  |  |  | conditionals where it wasn’t yet indicated for |  |
|  |  |  |  |  |  |  |  |  |  | consistency and clarity: Tables 1-3, 20A, 22-25, 30, |  |
|  |  |  |  |  |  |  |  |  |  | 32-36. |  |
|  |  |  |  |  |  |  |  |  |  | Table 2: Further review of TSE 5100 showed there |  |
|  |  |  |  |  |  |  |  |  |  | was a missing ICS item that needed adding due to the |  |
|  |  |  |  |  |  |  |  |  |  | Sum ICS re-shuffle: SUM ICS 31/11 (Core |  |
|  |  |  |  |  |  |  |  |  |  | Specification 4.0 + HS). Updated C.4 with this item. |  |
|  |  |  |  |  |  |  |  |  |  | Table 3 conditional C.1 had 2 references to GAP 3/1 it |  |
|  |  |  |  |  |  |  |  |  |  | is an obvious mistake that one should say 3/2. |  |
|  |  |  |  |  |  |  |  |  |  | In Tables that had been updated for the pre-requisites |  |
|  |  |  |  |  |  |  |  |  |  | affected by previous TSE’s 4330 and 4305 consistent |  |
|  |  |  |  |  |  |  |  |  |  | with changes in TSE 5063 changed the pre-requisites |  |
|  |  |  |  |  |  |  |  |  |  | that stated either Optional or Mandatory to Support |  |
|  |  |  |  |  |  |  |  |  |  | based on the support of the Table’s pre-requisites to |  |
|  |  |  |  |  |  |  |  |  |  | simply “M” or “O”: Tables 18, 28, 29, 30, 31, 34, 36, |  |
|  |  |  |  |  |  |  |  |  |  | and 37. |  |
|  |  |  |  |  |  |  |  |  |  | Simplified conditionals by removing the pre-requisite |  |
|  |  |  |  |  |  |  |  |  |  | items from the conditionals leaving only the |  |
|  |  |  |  |  |  |  |  |  |  | dependencies in Table 30 item C.1 and Table 36 |  |
|  |  |  |  |  |  |  |  |  |  | items C.1 and C.2. |  |
|  |  |  |  |  |  |  |  |  |  | Misc. editorial changes. |  |
|  | 24 |  |  | 4.0.7 |  |  | 2013-07-02 |  |  | Prepare for Publication |  |
|  |  |  |  | 4.0.8rT |  |  | 2013-08-01 |  |  | Template Conversion |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  | 4.0.8rTr4 |  |  | 2013-09-24 |  |  | Template Conversion Comment Resolution |  |
|  |  |  |  | 4.1.0r01 |  |  | 2013-09-24 |  |  | BR/EDR Secure Connections CR |  |
|  |  |  |  | 4.1.0r02 |  |  | 2013-09-25 |  |  | Low Duty Cycle Directed Advertising CR |  |
|  |  |  |  | 4.1.0r03 |  |  | 2013-09-25 |  |  | LE Privacy 1.1 CR |  |
|  |  |  | 4.1.0r04 | 4.1.0r04 |  | 2013-09-26 | 2013-09-26 |  |  | TSE 5288: Revised conditional statement C.3 in |  |
|  |  |  |  |  |  |  |  |  |  | Table 1. |  |
|  |  |  |  | 4.1.0r05 |  |  | 2013-10-04 |  |  | LE Dual Mode Topology CR |  |
|  |  |  |  | 4.1.0r06 |  |  | 2013-10-09 |  |  | LE Ping CR |  |
|  |  |  |  | 4.1.0r07 |  |  | 2013-10-14 |  |  | LE Link Layer Topology CR |  |
|  |  |  |  | 4.1.0r13 |  |  | 2013-10-31 |  |  | Fixed C.1 in Table 11 |  |
|  |  |  | 4.1.0.r14 | 4.1.0.r14 |  | 2013-11-10 | 2013-11-10 |  |  | Added new item 3 in Table 0a to allow mandate |  |
|  |  |  |  |  |  |  |  |  |  | CSA.3 centric changes for GAP Authentication and |  |
|  |  |  |  |  |  |  |  |  |  | Lot Bond, Private Address Changes, Connection |  |
|  |  |  |  |  |  |  |  |  |  | Parameters Changes and Dual Mode Addressing |  |
|  |  |  |  |  |  |  |  |  |  | Changes absorbed in Core v4.1. Introduced to allow |  |
|  |  |  |  |  |  |  |  |  |  | GAP.TS TCMT to remove SUM ICS references. |  |
|  | 25 |  |  | 4.1.0 |  |  | 2013-12-03 |  |  | Prepare for Publication |  |
|  |  |  | 4.1.1r00 | 4.1.1r00 |  | 2014-01-23 | 2014-01-23 |  |  | TSE 5477: Corrected Reference for 44/1, 44/2, and |  |
|  |  |  |  |  |  |  |  |  |  | 45/1. Corrected Prerequisite for Table 45, from GAP |  |
|  |  |  |  |  |  |  |  |  |  | 38/4 to GAP 38/3. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5463: Updated Table 36, C.1. |  |
|  |  |  | 4.1.1r01 |  |  | 2014-04-04 |  |  |  | TSE 5579: Added 4.1 and 4.1 + HS references to |  |
|  |  |  |  |  |  |  |  |  |  | conditionals and updated from otherwise Optional to |  |
|  |  |  |  |  |  |  |  |  |  | otherwise Excluded for all conditionals in Table 39, |  |
|  |  |  |  |  |  |  |  |  |  | Table 40, and Table 42. |  |
|  |  |  |  | 4.1.1r02 |  |  | 2014-04-04 |  |  | TSE 5561: Updated Table 0a C.3. |  |
|  | 26 |  |  | 4.1.1 |  |  | 2014-07-07 |  |  | TCRL 2014-1 Publication |  |
|  |  |  | 4.1.2r00 | 4.1.2r00 |  | 2014-10-17 | 2014-10-17 |  |  | TSE 5652: Added C.2 to Table 8A. Updated 8A/3 |  |
|  |  |  |  |  |  |  |  |  |  | from M to C.2. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5765: Table 26, C.2, Corrected item reference |  |
|  |  |  |  |  |  |  |  |  |  | for Privacy Feature v1.1 to be 26/1a instead of 26/2. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5781: Updated Table 25 C.2 to include 31/10 |  |
|  |  |  |  |  |  |  |  |  |  | and 31/10a. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5944: Removed 20/2a, updated to Item no longer |  |
|  |  |  |  |  |  |  |  |  |  | used, Removed C.3. |  |
|  |  |  |  | 4.1.2r01 |  |  | 2014-10-30 |  |  | TSE 5633: Updated status of 23/4 from C.2 to C.1. |  |
|  |  |  | 4.2.0r00 | 4.2.0r00 |  | 2014-11-14 | 2014-11-14 |  |  | Integrated Section 1.3 of |  |
|  |  |  |  |  |  |  |  |  |  | Core Enhanced Privacy 1 2.TS.CR.R05 & Section |  |
|  |  |  |  |  |  |  |  |  |  | _ _ _ _ 5 of Core LE Secure Connections.TS.CR.R16 _ _ _ |  |
|  |  |  | 4.2.0r01 |  |  | 2014-11-21 |  |  |  | Integrated comments from Rasmus, Jason, and |  |
|  |  |  |  |  |  |  |  |  |  | Mayank, and added Privacy CR changes. |  |
|  |  |  |  | 4.2.0r02 |  |  | 2014-11-24 |  |  | Updated Table 11 after further review from Jason. |  |
|  |  |  | 4.2.0r04 | 4.2.0r04 |  | 2014-11-25 | 2014-11-25 |  |  | BTI Rejected TSE 5781. Changes from that TSE |  |
|  |  |  |  |  |  |  |  |  |  | undone and conditionals updated. |  |
|  |  |  |  |  |  |  |  |  |  | Updated 0a Conditionals |  |
|  | 27 |  |  | 4.2.0 |  |  | 2014-12-03 |  |  | Prepare for TCRL 2014-2 publication |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 4.2.1r00 | 4.2.1r00 |  | 2015-05-08 |  |  |  | TSE 6259: Corrected typos in C.4 of Table 21 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 6130: Deleted tables 39, 40, and 42. |  |
|  |  |  | 4.2.1r01 |  |  | 2015-05-18 |  |  |  | Reinstated tables 39, 40, and 42. Implemented |  |
|  |  |  |  |  |  |  |  |  |  | changes from TSE 6130 by removing SUM ICS |  |
|  |  |  |  |  |  |  |  |  |  | references to 4.1 or later in those tables and |  |
|  |  |  |  |  |  |  |  |  |  | extending prerequisite statements. |  |
|  |  |  | 4.2.1r02 |  |  | 2015-06-05 |  |  |  | Deleted Section 1.2 (Global Statement of |  |
|  |  |  |  |  |  |  |  |  |  | Conformance) per current ICS template standards. |  |
|  |  |  | 4.2.1r03 |  |  | 2015-06-08 |  |  |  | Adjusted section numbering following deletion of |  |
|  |  |  |  |  |  |  |  |  |  | Section 1.2 at 4.2.1r02. |  |
|  |  |  | 4.2.1r04 |  |  | 2015-06-22 |  |  |  | Integrated changes from Core Specification |  |
|  |  |  |  |  |  |  |  |  |  | Supplement v6. |  |
|  |  |  |  |  |  |  |  |  |  | Advertising URI: Added items to tables 8A and 20A. |  |
|  |  |  |  |  |  |  |  |  |  | Efficient Non-Connectable Advertising: Revised C.2 in |  |
|  |  |  |  |  |  |  |  |  |  | Table 8A. |  |
|  |  |  | 4.2.1r05 |  |  | 2015-06-23 |  |  |  | Revised CSSv6 changes to account for corresponding |  |
|  |  |  |  |  |  |  |  |  |  | updates to SUM ICS. |  |
|  | 28 |  |  | 4.2.1 |  |  | 2015-07-14 |  |  | Prepared for TCRL 2015-1 publication |  |
|  |  |  | 4.2.2r00 | 4.2.2r00 |  | 2015-10-09 | 2015-10-09 |  |  | TSE 6485: Split item 41/2 into two items and 43/2 into |  |
|  |  |  |  |  |  |  |  |  |  | two items. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 6169 & 6323: Rewrote Tables 11, 17, 26, 27, 36, |  |
|  |  |  |  |  |  |  |  |  |  | 37 and corresponding conditionals to resolve issues |  |
|  |  |  |  |  |  |  |  |  |  | with Privacy feature. |  |
|  | 29 |  |  | 4.2.2 |  |  | 2015-12-22 |  |  | Prepared for TCRL 2015-2 publication. |  |
|  |  |  | 5.0.0r00 | 5.0.0r00 |  | 2016-10-03 | 2016-10-03 |  |  | Issue 7732: Added new item support for Bluetooth |  |
|  |  |  |  |  |  |  |  |  |  | Core Specification v5.0 and new conditional C.5 to |  |
|  |  |  |  |  |  |  |  |  |  | Table 0a. Added two new tables 11a and 17a for |  |
|  |  |  |  |  |  |  |  |  |  | Periodic Advertising Modes and Procedures. Added |  |
|  |  |  |  |  |  |  |  |  |  | new reference for Bluetooth Core Specification v.5.0 |  |
|  |  |  |  |  |  |  |  |  |  | to References section. |  |
|  |  |  | 5.0.0r01 |  |  | 2016-10-13 |  |  |  | TSE 7297: Updated conditional C.3 for Table 27. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 7058: Updated conditionals in Tables 24 (C.1), |  |
|  |  |  |  |  |  |  |  |  |  | 33 (C.1), and 34 (C.2). |  |
|  |  |  | 5.0.0r02 |  |  | 2016-11-08 |  |  |  | Issue 7872: Corrected reference in 0a/5 from [1] to |  |
|  |  |  |  |  |  |  |  |  |  | [11]. |  |
|  |  |  | 5.0.0r03 |  |  | 2016-11-10 |  |  |  | Issue 7803: Added two new items 8/3 and 8/4 and |  |
|  |  |  |  |  |  |  |  |  |  | conditional C.1 to Table 8. Added three items 20/5, |  |
|  |  |  |  |  |  |  |  |  |  | 20/6, and 20/7 and conditional C.3 to Table 20. |  |
|  |  |  |  |  |  |  |  |  |  | Modified items 20/1 and 20/3. Updated conditionals |  |
|  |  |  |  |  |  |  |  |  |  | for Table 20A. |  |
|  |  |  |  |  |  |  |  |  |  | Issue 7884: Global edit. Added support in conditionals |  |
|  |  |  |  |  |  |  |  |  |  | and prerequisites for Core Spec version 5.0. |  |
|  |  |  | 5.0.0r04 |  |  | 2016-11-16 |  |  |  | Updated to current template. Removed unnecessary |  |
|  |  |  |  |  |  |  |  |  |  | parentheses and replaced with quotation marks. |  |
|  |  |  |  |  |  |  |  |  |  | Simplified the “or later” issue in Tables 39, 40, and 42 |  |
|  |  |  |  |  |  |  |  |  |  | by revising the Conditionals to exclude anything other |  |
|  |  |  |  |  |  |  |  |  |  | than Core Spec v4.0 or 4.0+HS and added the |  |
|  |  |  |  |  |  |  |  |  |  | informative note. |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 5.0.0r05 | 5.0.0r05 |  | 2016-11-16 |  |  |  | Updated references and conditionals for Core |  |
|  |  |  |  |  |  |  |  |  |  | Specification Supplement (CSS) v7. |  |
|  |  |  | 5.0.0r06 |  |  | 2016-11-17 |  |  |  | Simplified conditionals in Tables 39, 40 and 42 by |  |
|  |  |  |  |  |  |  |  |  |  | adding a prerequisite requirement for 4.0 support. |  |
|  | 30 |  |  | 5.0.0 |  |  | 2016-12-13 |  |  | Prepared for TCRL 2016-2 publication |  |
|  |  |  | 5.0.1r00 | 5.0.1r00 |  | 2017-02-16 | 2017-02-16 |  |  | TSE 7816: Added new item GAP 2/7a. Added new |  |
|  |  |  |  |  |  |  |  |  |  | conditional statement, C.9. Updated conditional |  |
|  |  |  |  |  |  |  |  |  |  | statement C.8. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 8704: Revised Table 42 prerequisite by adding |  |
|  |  |  |  |  |  |  |  |  |  | “GAP 38/3 “Peripheral BR/EDR/LE” AND”. |  |
|  |  |  | 5.0.1r01 |  |  | 2017-05-04 |  |  |  | TSE 7816: Fixed cross references to 5.0 and odd |  |
|  |  |  |  |  |  |  |  |  |  | hidden formatting. Made font size uniform within the |  |
|  |  |  |  |  |  |  |  |  |  | tables and Change History. Removed extra row in the |  |
|  |  |  |  |  |  |  |  |  |  | Change History that didn’t add any material |  |
|  |  |  |  |  |  |  |  |  |  | information. Enhanced the change History where it |  |
|  |  |  |  |  |  |  |  |  |  | was stated that “rows were added” which might |  |
|  |  |  |  |  |  |  |  |  |  | explain what a tech editor did but what someone |  |
|  |  |  |  |  |  |  |  |  |  | looking at the Change History would rather know is |  |
|  |  |  |  |  |  |  |  |  |  | that items 20/3, 20/4, and 20/5 were added. |  |
|  |  |  |  |  |  |  |  |  |  | Updated copyright/disclaimer. |  |
| 31 |  |  | 5.0.1 |  |  | 2017-07-05 |  |  |  | Approved by BTI. Prepared for TCRL 2017-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  |  | 5.0.2r00 |  |  | 2017-08-22 |  |  | TSE 9678: Revised Security Aspects table note C.9. |  |
|  |  |  | 5.0.2r01 | 5.0.2r01 |  | 2017-10-13 | 2017-10-13 |  |  | TSE 9937: Added LL control procedures to Tables 21 |  |
|  |  |  |  |  |  |  |  |  |  | and 31. |  |
| 32 |  |  | 5.0.2 |  |  | 2017-12-07 |  |  |  | Approved by BTI. Prepared for TCRL 2017-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 5.0.3r00 |  |  | 2018-07-17 |  |  |  | Incorporated Core PAST CLE TEST CR r05: _ _ _ _ _ |  |
|  |  |  |  |  |  |  |  |  |  | Modified conditional note C.1 for Table 17a. Added 2 |  |
|  |  |  |  |  |  |  |  |  |  | new sections, both titled “Periodic Advertising Modes |  |
|  |  |  |  |  |  |  |  |  |  | and Procedures,” as well as Tables 27a and 37a, to |  |
|  |  |  |  |  |  |  |  |  |  | sections “Peripheral” and “Central,” respectively. |  |
|  |  |  | 5.0.3r01 |  |  | 2018-10-04 |  |  |  | Drafted changed for deprecation and withdrawal. |  |
|  |  |  |  |  |  |  |  |  |  | Affects 27/3-4 and 27/8 as well as 0a/1 and 0a/2. |  |
|  |  |  | 5.0.3r02 |  |  | 2018-11-12 |  |  |  | Replaced TBD and [X] values with actual values. |  |
|  |  |  |  |  |  |  |  |  |  | Added new reference for Bluetooth Core Specification |  |
|  |  |  |  |  |  |  |  |  |  | version 5.1. |  |
|  |  |  | 5.0.3r03 |  |  | 2018-11-13 |  |  |  | Updated Madrid styles – changed light grey text to |  |
|  |  |  |  |  |  |  |  |  |  | black text. |  |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 |  |  |  | Updated revision number to 5.1.0 to align with the |  |
|  |  |  |  |  |  |  |  |  |  | adoption of Core Specification version 5.1. |  |
|  |  |  | 5.1.0r01 |  |  | 2018-11-16 |  |  |  | Added entry 0a/6 for Core Specification version 5.1 |  |
|  |  |  |  |  |  |  |  |  |  | and updated conditionals to include the new version. |  |
|  |  |  | 5.1.0r02 |  |  | 2018-11-19 |  |  |  | Corrected implementation of conditionals referencing |  |
|  |  |  |  |  |  |  |  |  |  | 5.1. |  |
|  |  |  | 5.1.0r03 |  |  | 2018-11-20 |  |  |  | Added item 0a/0a for Core 4.0 and updated Table |  |
|  |  |  |  |  |  |  |  |  |  | 17a/C.1 as well as the prerequisites for 27a and 37a |  |
|  |  |  |  |  |  |  |  |  |  | with the new item. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | 5.1.0r04 | 5.1.0r04 |  | 2018-11-21 |  | Marked C.5 of Table 21 and C.3 of Table 31 as no |  |
|  |  |  |  |  |  |  |  | longer used (as they duplicated C.3 and C.1 |  |
|  |  |  |  |  |  |  |  | respectively. Updated the status for the two items |  |
|  |  |  |  |  |  |  |  | referencing those conditionals. |  |
| 33 |  |  | 5.1.0 |  |  | 2018-12-07 |  | Approved by BTI. Prepared for TCRL 2018-2 |  |
|  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 5.1.1r00–r01 |  |  | 2019-04-09 – 2019-07-18 |  | TSE 11552 (rating 2): Removed ICS items that are no |  |
|  |  |  |  |  |  |  |  | longer applicable to Specifications 4.2 or later. |  |
|  |  |  |  |  |  |  |  | Simplified conditionals. Updated, simplified, or |  |
|  |  |  |  |  |  |  |  | removed tables throughout. Moved Revision History |  |
|  |  |  |  |  |  |  |  | and Contributors tables to the end of the document. |  |
|  |  |  |  |  |  |  |  | Incorporated changes associated with Key |  |
|  |  |  |  |  |  |  |  | Negotiation Changes specification erratum 11838: |  |
|  |  |  |  |  |  |  |  | Added new ICS entry to Table 2 (item 12) to indicate if |  |
|  |  |  |  |  |  |  |  | the IUT enforces a minimum encryption key size of 56 |  |
|  |  |  |  |  |  |  |  | bits. |  |
| 34 |  |  | 5.1.1 |  |  | 2019-08-01 |  | Approved by BTI. Prepared for TCRL 2019-1 |  |
|  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | p35r00–r03 |  |  | 2019-08-06 – 2019-11-22 |  | Added test groups to accommodate adoption of Core |  |
|  |  |  |  |  |  |  |  | Specification v5.2 with regard to Isochronous |  |
|  |  |  |  |  |  |  |  | Channels CR r20 (includes Issues 11742, 11762, |  |
|  |  |  |  |  |  |  |  | 11777, 11778, 11779, 11783,11786, 11804, 11817, |  |
|  |  |  |  |  |  |  |  | 11819, 11820, 11852, 11917, 11919, 11928, 11929, |  |
|  |  |  |  |  |  |  |  | 11930, 11983, 11740, 11801, 11941, 12029, 12030, |  |
|  |  |  |  |  |  |  |  | 12043, 12052, 12053, 12054, 12055, 12059, 12061, |  |
|  |  |  |  |  |  |  |  | 12071, 12072, 12073, 12077, 12084, 12031, 12078, |  |
|  |  |  |  |  |  |  |  | 12094, 12095, 12106, 12107, 12130, 12132, 12133, |  |
|  |  |  |  |  |  |  |  | 12251, 12280, and 12321). Added item 3 and note |  |
|  |  |  |  |  |  |  |  | C.1 to Table 7; added items 2–5 and notes C.1 and |  |
|  |  |  |  |  |  |  |  | C.2 to Table 10; added Section “Security Aspects” |  |
|  |  |  |  |  |  |  |  | (1.4.1.7) and Table 11b; added items 2–4 and notes |  |
|  |  |  |  |  |  |  |  | C.1 and C.2 to Table 16; added Section “Security |  |
|  |  |  |  |  |  |  |  | Aspects” (1.4.2.7) and Table 17b; added items 6 and |  |
|  |  |  |  |  |  |  |  | 7 and note C.1 to Table 23; added items 7 and 8 and |  |
|  |  |  |  |  |  |  |  | note C.1 to Table 33; updated references section with |  |
|  |  |  |  |  |  |  |  | new Core Specification. |  |
|  |  |  |  |  |  |  |  | TSE 12751 (rating 1): Updated to SUM ICS 31 per |  |
|  |  |  |  |  |  |  |  | TSE 12647 and made minor editorial updates, which |  |
|  |  |  |  |  |  |  |  | included deleting Tables 0a, 39, 40, and 42; updating |  |
|  |  |  |  |  |  |  |  | C.1 and C.2 for Table 1; updating item 12 and C.3 for |  |
|  |  |  |  |  |  |  |  | Table 2; updating C.1 for Tables 7, 8, 11a, 11b, 16, |  |
|  |  |  |  |  |  |  |  | 17a, 17b, and 20; updating C.2 for Tables 10, 21, and |  |
|  |  |  |  |  |  |  |  | 31; and updating prerequisites for Tables 27a and |  |
|  |  |  |  |  |  |  |  | 37a. |  |
|  |  |  |  |  |  |  |  | Updated .X and Milan references to real numbers. |  |
|  |  |  |  |  |  |  |  | Revised document numbering convention, setting last |  |
|  |  |  |  |  |  |  |  | release publication of 5.1.1 as p34; added publication |  |
|  |  |  |  |  |  |  |  | number column to Revision History. |  |
| 35 |  |  | p35 |  |  | 2020-01-07 |  | Approved by BTI on 2019-12-22. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2019-2 publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p36r00–r11 | p36r00–r11 |  | 2020-01-23 – 2020-11-18 |  | TSE 13341 (rating 4): Added items and conditionals to |  |
|  |  |  |  |  |  |  |  | Tables 25 and 35 to accommodate allowing SM1L2 |  |
|  |  |  |  |  |  |  |  | and SM1L3 to use LE Secure Connections pairing |  |
|  |  |  |  |  |  |  |  | only. |  |
|  |  |  |  |  |  |  |  | TSE 14862 (rating 1): Fixed references in Tables 7, |  |
|  |  |  |  |  |  |  |  | 10, 11b, 16, 17b, 23, and 33 to align with GAP v5.2 |  |
|  |  |  |  |  |  |  |  | spec. |  |
|  |  |  |  |  |  |  |  | TSE 14950 (rating 2): Updated C.3 for Table 25 and |  |
|  |  |  |  |  |  |  |  | C.2 for Table 35 to address issue with LE Security |  |
|  |  |  |  |  |  |  |  | Mode 1 Level 4 being mandatory when LE Secure |  |
|  |  |  |  |  |  |  |  | Connections is supported. |  |
|  |  |  |  |  |  |  |  | TSE 14863 (rating 2): Updated C.1 in Tables 11b and |  |
|  |  |  |  |  |  |  |  | 17b to address security mode issues. |  |
|  |  |  |  |  |  |  |  | TSE 15150 (rating 4): To support new LE Audio |  |
|  |  |  |  |  |  |  |  | Security Consideration requirements, updated Table |  |
|  |  |  |  |  |  |  |  | 2, adding items 7b, 7c, 7d, and 13, and conditionals |  |
|  |  |  |  |  |  |  |  | C.10 and C.11, and updating Status of item 12; |  |
|  |  |  |  |  |  |  |  | updated Table 11b, adding items 2, 3, and 4, and |  |
|  |  |  |  |  |  |  |  | conditional C.2; updated Table 17b, adding items 2, 3, |  |
|  |  |  |  |  |  |  |  | and 4, and conditional C.2; updated Table 35, |  |
|  |  |  |  |  |  |  |  | Capability text of items 11 and 12 to add "LE" and |  |
|  |  |  |  |  |  |  |  | "Pairing"; updated Table 41 by adding conditionals |  |
|  |  |  |  |  |  |  |  | C.1 and C.2 and updating status of items 2a and 2b, |  |
|  |  |  |  |  |  |  |  | respectively; updated Table 43 by adding conditionals |  |
|  |  |  |  |  |  |  |  | C.1 and C.2 and updating status of items 2a and 2b, |  |
|  |  |  |  |  |  |  |  | respectively. |  |
|  |  |  |  |  |  |  |  | TSE 15762 (rating 4): To address adding Minimum |  |
|  |  |  |  |  |  |  |  | 128 Bit Key Size for the LE ICS entry, updated Table |  |
|  |  |  |  |  |  |  |  | 25, modifying items 11 and 12 and adding item 13 |  |
|  |  |  |  |  |  |  |  | and conditional C.5, and updated Table 35, adding |  |
|  |  |  |  |  |  |  |  | item 13 and conditional C.4. |  |
|  |  |  |  |  |  |  |  | TSE 15447 (rating 1): Editorials to address Erratum |  |
|  |  |  |  |  |  |  |  | 15353 (Vol 3), globally change “Master” to “Central” |  |
|  |  |  |  |  |  |  |  | and “Slave” to “Peripheral”. |  |
|  |  |  |  |  |  |  |  | Consistency Checker fixes and template-related |  |
|  |  |  |  |  |  |  |  | editorials. |  |
| 36 |  |  | p36 |  |  | 2020-12-22 |  | Approved by BTI on 2020-12-03. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2020-1 publication. |  |
|  |  |  | p37r00–r07 |  |  | 2020-12-28 – 2021-06-10 |  | TSE 12794 (rating 2): In Table 2, revised security |  |
|  |  |  |  |  |  |  |  | mode 1 and security mode 3 item conditionals to |  |
|  |  |  |  |  |  |  |  | match with Table 5.1 in the GAP section of Core Spec |  |
|  |  |  |  |  |  |  |  | 4.2 and later, which shows as simply Excluded. |  |
|  |  |  |  |  |  |  |  | TSE 14687 (rating 2): Updated Prerequisite and note |  |
|  |  |  |  |  |  |  |  | C.1 for Table 11a and updated Prerequisite and note |  |
|  |  |  |  |  |  |  |  | C.1 and added note C.2 for item 1 for Table 17a. |  |
|  |  |  |  |  |  |  |  | TSE 14889 (rating 1): Updated all references to |  |
|  |  |  |  |  |  |  |  | remove CSAs and clean up the existing references. |  |
|  |  |  |  |  |  |  |  | References were not forward compatible in previous |  |
|  |  |  |  |  |  |  |  | revision. |  |
|  |  |  |  |  |  |  |  | TSE 15689 (rating 4): To address E15498, added |  |
|  |  |  |  |  |  |  |  | item 14a to Tables 8A and 20A. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | TSE 16115 (rating 1): Corrected capitalization and |  |
|  |  |  |  |  |  |  |  | references of ICS items, aligning them with Core Spec |  |
|  |  |  |  |  |  |  |  | and other referenced layers. |  |
|  |  |  |  |  |  |  |  | TSE 16608 (rating 1): Fixed wording in item 17 of |  |
|  |  |  |  |  |  |  |  | Tables 8A and 20A. |  |
|  |  |  |  |  |  |  |  | Incorporated |  |
|  |  |  |  |  |  |  |  | Enhanced Connection Update TEST CR r17: |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ Added a reference to the v5.3 Core release; added |  |
|  |  |  |  |  |  |  |  | item 8 and note C.2 to Table 23; added item 9 and |  |
|  |  |  |  |  |  |  |  | note C.2 to Table 33. Subsequently updated “Sydney” |  |
|  |  |  |  |  |  |  |  | and “.x” references to real numbers. |  |
|  |  |  |  |  |  |  |  | Minor template-related and consistency checker |  |
|  |  |  |  |  |  |  |  | editorials. |  |
| 37 |  |  | p37 |  |  | 2021-07-13 |  | Approved by BTI on 2021-06-27. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2021-1 publication. |  |
|  |  |  | p37ed2r00 |  |  | 2021-07-26 |  | TSE 17284 (rating 1): Added “IF” to C.6 of Table 16 |  |
|  |  |  |  |  |  |  |  | and performed other minor consistency checker |  |
|  |  |  |  |  |  |  |  | editorials. |  |
|  |  |  | p37 edition 2 |  |  | 2021-08-19 |  | Approved by BTI on 2021-08-19. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  | p38r00–r02 |  |  | 2021-08-27 – 2021-12-28 |  | TSE 16688 (rating 2): Changed all BB dependencies |  |
|  |  |  |  |  |  |  |  | to Optional by updating C.3 and Status of item 9 and |  |
|  |  |  |  |  |  |  |  | deleting C.4 in Table 1 and updating C.1 in Table 4. |  |
|  |  |  |  |  |  |  |  | TSE 17496 (rating 1): Capitalization change to table |  |
|  |  |  |  |  |  |  |  | numbers (8a and 20a) to make consistent and align |  |
|  |  |  |  |  |  |  |  | with Launch Studio. |  |
|  |  |  |  |  |  |  |  | Performed template-related fixes and consistency |  |
|  |  |  |  |  |  |  |  | checker editorials. Updated the copyright page to |  |
|  |  |  |  |  |  |  |  | align with v2 of the DNMD. |  |
| 38 |  |  | p38 |  |  | 2022-01-25 |  | Approved by BTI on 2021-12-27. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2021-2 publication. |  |
|  |  |  | p38ed2 r00–r02 |  |  | 2022-02-01 – 2022-03-07 |  | TSE 18025 (rating 1): Corrected references in |  |
|  |  |  |  |  |  |  |  | items 11–17 of Tables 8a and 20a. |  |
|  |  |  |  |  |  |  |  | TSE 18359 (rating 1): Updated “is/not supported” |  |
|  |  |  |  |  |  |  |  | language in conditionals globally to align with new |  |
|  |  |  |  |  |  |  |  | conventions. Simplified C.1 in Table 22. |  |
|  |  |  |  |  |  |  |  | Template-related editorials. |  |
|  |  |  | p38, edition 2 |  |  | 2022-03-07 |  | Approved by BTI on 2022-03-07. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  | p39r00–r12 |  |  | 2022-09-30 – 2022-12-15 |  | TSE 17191 (rating 2): Updated the conditionals for the |  |
|  |  |  |  |  |  |  |  | Secure Connections Only Mode items (GAP 2/11, |  |
|  |  |  |  |  |  |  |  | GAP 25/10, and GAP 35/10) to align with E17214 |  |
|  |  |  |  |  |  |  |  | requirements to support over all supported transports. |  |
|  |  |  |  |  |  |  |  | TSE 18444 (rating 4): Per E17946, added items 8a/18 |  |
|  |  |  |  |  |  |  |  | and 20a/19. |  |
|  |  |  |  |  |  |  |  | TSE 18547 (rating 1): Cleaned up conditionals to align |  |
|  |  |  |  |  |  |  |  | with the latest ICS conventions and removed |  |
|  |  |  |  |  |  |  |  | unnecessary intro text from Section 1.5.1. |  |
|  |  |  |  |  |  |  |  | TSE 18669 (rating 2): Per E18668, added conditionals |  |
|  |  |  |  |  |  |  |  | to 24/3 and 34/3 for Bondable mode. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | TSE 20648 (rating 3): Updated 25/5 and 25/6 with |  |
|  |  |  |  |  |  |  |  | conditional C.6. Updated conditional for 25/9, 25/11, |  |
|  |  |  |  |  |  |  |  | and 25/12 and set C.3 to no longer used. Updated |  |
|  |  |  |  |  |  |  |  | conditional for 35/9, 35/11, and 35/12 and set C.2 to |  |
|  |  |  |  |  |  |  |  | no longer used. Added new Table 27b for SM |  |
|  |  |  |  |  |  |  |  | Peripheral ILD requirements and new Table 37b for |  |
|  |  |  |  |  |  |  |  | SM Central ILD requirements. Converted Table 41 |  |
|  |  |  |  |  |  |  |  | and Table 43 to contain an ILD column, and removed |  |
|  |  |  |  |  |  |  |  | conditionals. |  |
|  |  |  |  |  |  |  |  | TSE 22131 (rating 1): Corrected reference for CSS. |  |
|  |  |  |  |  |  |  |  | TSE 22228 (rating 4): Per E22185, added new items |  |
|  |  |  |  |  |  |  |  | 11a/4 and 17a/3 and associated conditionals. |  |
|  |  |  |  |  |  |  |  | Core v5.4 CRs: |  |
|  |  |  |  |  |  |  |  | EAD (from CR Encrypted Advertising Data.Test |  |
|  |  |  |  |  |  |  |  | _ _ .CR.13): Added a new reference for Core v5.4. Added |  |
|  |  |  |  |  |  |  |  | 20a/18, 25/14, 27/10, 30/3 with conditional C.2, and |  |
|  |  |  |  |  |  |  |  | 35/14. |  |
|  |  |  |  |  |  |  |  | EAD (from CR Encrypted Advertising Data.Test |  |
|  |  |  |  |  |  |  |  | _ _ .CR.14): Added 8a/19 to address E22205. |  |
|  |  |  |  |  |  |  |  | Incorporated Test Issue 22239 for EAD, with r02 CR |  |
|  |  |  |  |  |  |  |  | from comment 963971. Added items 8a/20, 14a/20, |  |
|  |  |  |  |  |  |  |  | and 30a/20. Resolved TBD references per Clive’s |  |
|  |  |  |  |  |  |  |  | email conversion list. |  |
|  |  |  |  |  |  |  |  | SLC (from CR Security Level Characteristics. |  |
|  |  |  |  |  |  |  |  | _ _ Test.CR r07): Added 27/11 and 37/4 to cover LE |  |
|  |  |  |  |  |  |  |  | _ GATT Security Levels related to Core v5.4 release. |  |
|  |  |  |  |  |  |  |  | PAwR (Periodic Advertising with Responses |  |
|  |  |  |  |  |  |  |  | _ _ _ _ TEST CR r22): Added item 11a/3 and associated |  |
|  |  |  |  |  |  |  |  | _ _ C.3 and 20a/20 and associated C.4. |  |
| 39 |  |  | p39 |  |  | 2023-02-07 |  | Approved by BTI on 2022-12-28. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2022-2 publication. |  |
|  |  |  | p40r00 |  |  | 2023-04-16 |  | TSE 22294 (rating 2): Added new 25/14 and related |  |
|  |  |  |  |  |  |  |  | conditional C.7 and new 35/15 and related conditional |  |
|  |  |  |  |  |  |  |  | C.5. |  |
|  |  |  |  |  |  |  |  | TSE 22563 (rating 3): Added new 11/4. |  |
| 40 |  |  | p40 |  |  | 2023-06-29 |  | Approved by BTI on 2023-06-05. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2023-1 publication. |  |
|  |  |  | p41r00–r07 |  |  | 2023-08-07 – 2023-11-14 |  | TSE 18350 (rating 2): Added Link Layer ILDs to |  |
|  |  |  |  |  |  |  |  | Tables 8 and 20. |  |
|  |  |  |  |  |  |  |  | TSE 23143 (rating 4): Per E20385, added new 27/10a |  |
|  |  |  |  |  |  |  |  | and related conditional C.2. |  |
|  |  |  |  |  |  |  |  | TSE 23338 (rating 2): Added new items 2/14, 27b/9, |  |
|  |  |  |  |  |  |  |  | 37b/9, 41/2 (with updated status for 41/2a and 41/2b |  |
|  |  |  |  |  |  |  |  | and new conditionals C.1–C.3), and 43/2 (with |  |
|  |  |  |  |  |  |  |  | updated status for 43/2a and 43/2b and new |  |
|  |  |  |  |  |  |  |  | conditionals C.1–C.3). |  |
|  |  |  |  |  |  |  |  | TSE 23525 (rating 2): Removed C.7 and updated the |  |
|  |  |  |  |  |  |  |  | status of 25/14 to Optional. Removed C.5 and |  |
|  |  |  |  |  |  |  |  | updated the status of 35/15 to Optional. Added the |  |
|  |  |  |  |  |  |  |  | GATT ICS to the References section. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | TSE 24070 (rating 1): Replaced SUM ICS references |  |
|  |  |  |  |  |  |  |  | with CORE ICS references. Updated Table 0 |  |
|  |  |  |  |  |  |  |  | conditionals C.1–C.3 and added C.4, affecting 0/1, |  |
|  |  |  |  |  |  |  |  | 0/2, and 0/3; updated Table 7 conditional C.1, |  |
|  |  |  |  |  |  |  |  | affecting 7/3; updated Table 8 conditional C.1, |  |
|  |  |  |  |  |  |  |  | affecting 8/3 and 8/4; updated Table 10 conditional |  |
|  |  |  |  |  |  |  |  | C.2, affecting 10/3; updated Table 11a prerequisite; |  |
|  |  |  |  |  |  |  |  | updated Table 16 conditional C.1, affecting 16/2; |  |
|  |  |  |  |  |  |  |  | updated Table 17a prerequisite; updated Table 20 |  |
|  |  |  |  |  |  |  |  | conditional C.1, affecting 20/5, 20/6, and 20/7; |  |
|  |  |  |  |  |  |  |  | updated Table 21 conditional C.1, affecting 21/8; |  |
|  |  |  |  |  |  |  |  | updated Table 23 conditional C.2, affecting 23/8; |  |
|  |  |  |  |  |  |  |  | updated Table 27a prerequisite; updated Table 31 |  |
|  |  |  |  |  |  |  |  | conditional C.2, affecting 31/11 and 31/12; updated |  |
|  |  |  |  |  |  |  |  | Table 33 conditional C.2, affecting 33/9; and updated |  |
|  |  |  |  |  |  |  |  | Table 37a prerequisite. |  |
|  |  |  |  |  |  |  |  | TSE 24220 (rating 2): Updated to align ILDs toward |  |
|  |  |  |  |  |  |  |  | L2CAP. Added an “Auto-fill tables” informational |  |
|  |  |  |  |  |  |  |  | section. Added Table 4a to cover L2CAP ILDs. |  |
|  |  |  |  |  |  |  |  | Updated 21/3 status to a conditional from L2CAP. |  |
|  |  |  |  |  |  |  |  | Added Table 27c to cover L2CAP ILDs. Updated 31/3 |  |
|  |  |  |  |  |  |  |  | status to a conditional from L2CAP. Added Table 37c |  |
|  |  |  |  |  |  |  |  | to cover L2CAP ILDs. Added a reference to the |  |
|  |  |  |  |  |  |  |  | L2CAP ICS to the References section. |  |
| 41 |  |  | p41 |  |  | 2024-07-01 |  | Approved by BTI on 2024-05-22. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2024-1 publication. |  |
|  |  |  | p42r00–r14 |  |  | 2024-06-24 – 2024-07-31 |  | TSE 22966 (rating 2): Per E18082, updated Table 1 |  |
|  |  |  |  |  |  |  |  | conditional C.1. |  |
|  |  |  |  |  |  |  |  | TSE 23081 (rating 2): Added items 13a–13d for |  |
|  |  |  |  |  |  |  |  | Table 2, updated Table 2 conditional C.11, and added |  |
|  |  |  |  |  |  |  |  | Table 2 conditionals C.12–C.15. Added items |  |
|  |  |  |  |  |  |  |  | 13a–13c for Table 25, updated Table 25 conditional |  |
|  |  |  |  |  |  |  |  | C.5, and added Table 25 conditionals C.7–C.9. Added |  |
|  |  |  |  |  |  |  |  | items 13a–13c for Table 35, updated Table 35 |  |
|  |  |  |  |  |  |  |  | conditional C.4, and added Table 35 conditionals |  |
|  |  |  |  |  |  |  |  | C.5–C.7. |  |
|  |  |  |  |  |  |  |  | TSE 24466 (rating 2): Added Items 11/5, 17/5, 26/5, |  |
|  |  |  |  |  |  |  |  | and 36/6. |  |
|  |  |  |  |  |  |  |  | TSE 24837 (rating 2): Added Item 27b/10. |  |
|  |  |  |  |  |  |  |  | TSE 24878 (rating 2): Per E17874, added item 5 for |  |
|  |  |  |  |  |  |  |  | Table 8 and item 8 for Table 20 and updated |  |
|  |  |  |  |  |  |  |  | conditional C.1 for Tables 8 and 20. |  |
|  |  |  |  |  |  |  |  | TSE 25249 (rating 4): Per E24891, added Section |  |
|  |  |  |  |  |  |  |  | 1.4.6 and Table 4b. In Table 26, added an ILD |  |
|  |  |  |  |  |  |  |  | column, Item 26/6, and conditional C.1. In Table 27, |  |
|  |  |  |  |  |  |  |  | added Item 27/12 and conditional C.3. n Table 37, |  |
|  |  |  |  |  |  |  |  | added Items 37/5 – 37/7 and conditional C.2. |  |
|  |  |  |  |  |  |  |  | TSE 25552 (rating 2): Added Inter-Layer Dependency |  |
|  |  |  |  |  |  |  |  | column to Tables 7, 11a, 13, 14, 17a, 19, 20a, 23, 27, |  |
|  |  |  |  |  |  |  |  | 27a, 29, 30, 33, 37, and 37a. Updated the Capability |  |
|  |  |  |  |  |  |  |  | column for Tables 7, 13, 14, 19, 29, and 30. Updated |  |
|  |  |  |  |  |  |  |  | the Status column for Tables 8a, 11a, 17a, 27a, 37, |  |
|  |  |  |  |  |  |  |  | and 37a. Added conditional C.1 to Table 7. Deleted |  |
|  |  |  |  |  |  |  |  | conditional C.1 from Table 8a. Updated conditionals |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | C.2–C.4 for Table 11a. Added Table 11c. Updated |  |
|  |  |  |  |  |  |  |  | item 3, added items 4–6, and updated conditionals |  |
|  |  |  |  |  |  |  |  | C.1–C.3 for Table 17a. Added item 21 and updated |  |
|  |  |  |  |  |  |  |  | conditionals C.3 and C.4 for Table 20a. Added items |  |
|  |  |  |  |  |  |  |  | 7a and 9 and conditional C.3 for Table 23. Added item |  |
|  |  |  |  |  |  |  |  | 9a and updated conditional C.1 for Table 27. Added |  |
|  |  |  |  |  |  |  |  | items 4–6 and updated conditionals C.1–C.3 for Table |  |
|  |  |  |  |  |  |  |  | 27a. Added items 8a, 10, and 11 and conditional C.3 |  |
|  |  |  |  |  |  |  |  | and updated conditionals C.1 and C.2 for Table 33. |  |
|  |  |  |  |  |  |  |  | Added item 3a and updated conditional C.1 for Table |  |
|  |  |  |  |  |  |  |  | 37. Added items 4–6 and updated conditionals C.1– |  |
|  |  |  |  |  |  |  |  | C.3 for Table 37a. |  |
|  |  |  |  |  |  |  |  | Incorporated CR CS Test CR r16-jorg (which |  |
|  |  |  |  |  |  |  |  | _ _ _ includes Test Issues 23205, 23293, 23331, 23332, |  |
|  |  |  |  |  |  |  |  | 23361, 23362, 23363, 23364, 23365, 23378, 23379, |  |
|  |  |  |  |  |  |  |  | 23381, 23382, 23384, 23404, 23419, 23422, 23424, |  |
|  |  |  |  |  |  |  |  | 23425, 23500, 23501, 23502, 23503, 23504, 23506, |  |
|  |  |  |  |  |  |  |  | 23594, 23693, 23694, 23696, 23701, 23706, 23711, |  |
|  |  |  |  |  |  |  |  | 23732, 23736, 23737, 23738, 23776, 23842, 23923, |  |
|  |  |  |  |  |  |  |  | 23993, 24023, 24033, 24043, 24049, 24133, 24135, |  |
|  |  |  |  |  |  |  |  | 24137, 24138, 24139, 24141, 24142, 24143, 24146, |  |
|  |  |  |  |  |  |  |  | 24147, 24149, 24150, 24151, 24153, 24177, 24181, |  |
|  |  |  |  |  |  |  |  | 24231, 24232, 24330, 24331, 24332, 24410, 24411, |  |
|  |  |  |  |  |  |  |  | 24418, 24419, 24478, 24483, 24515, 24531, 24599, |  |
|  |  |  |  |  |  |  |  | 24601, 24602, 24614, 24618, 24619, 24621, 24623, |  |
|  |  |  |  |  |  |  |  | 24624, 24625, 24627, 24630, 24639, 24645, 24646, |  |
|  |  |  |  |  |  |  |  | 24655, 24656, 24657, 24659, 24660, 24669, 24681, |  |
|  |  |  |  |  |  |  |  | 24717, 24769, 24776, 24789, 24808, 24809, 24838, |  |
|  |  |  |  |  |  |  |  | 24844, 24850, 24867, 24868, 24893, 24894, 24895, |  |
|  |  |  |  |  |  |  |  | 25028, 25029, 25040, 25042, 25053, 25055, 25111, |  |
|  |  |  |  |  |  |  |  | 25112, 25120, 25139, 25140, 25141, 25142, 25143, |  |
|  |  |  |  |  |  |  |  | 25148, 25149, 25150, 25157, 25166, 25209, 25240, |  |
|  |  |  |  |  |  |  |  | 25278, 25282, 25299, 25428, 25443, 25479, 25498, |  |
|  |  |  |  |  |  |  |  | 25511, 25512, 25525, 25585, 25617, 25632). To |  |
|  |  |  |  |  |  |  |  | account for the Channel Sounding feature in Core |  |
|  |  |  |  |  |  |  |  | Specification v6.0, added Tables 23a, 25a, 33a, and |  |
|  |  |  |  |  |  |  |  | 35a. In Table 25, added Items 25/15 – 25/18 and C.10 |  |
|  |  |  |  |  |  |  |  | – C.13. In Table 35, added Items 35/16 – 35/19 and |  |
|  |  |  |  |  |  |  |  | C.8 – C.11. Updated the references list. |  |
|  |  |  |  |  |  |  |  | Incorporated approved Test Issues 25302 and 25788. |  |
| 42 |  |  | p42 |  |  | 2024-09-04 |  | Approved by BTI on 2024-08-14. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2024-2 publication. |  |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Elisabeth Domínguez Cañizares |  |  | AT4 wireless |  |  |
| Noemí Pérez Dans |  |  | AT4 wireless |  |  |
| Elisa Rincón |  |  | AT4 wireless |  |  |
| Nathan Burns |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Jeff Drake |  |  | Bluetooth SIG, Inc. |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Alicia Courtney |  |  | Broadcom |  |  |
| Norbert Grunert |  |  | Broadcom |  |  |
| Chaojing Sun |  |  | Broadcom |  |  |
| Mayank Batra |  |  | CSR |  |  |
| Chris Church |  |  | CSR |  |  |
| Magnus Sommansson |  |  | CSR |  |  |
| James Dent |  |  | Nokia |  |  |
| Jonathan Tanner |  |  | Nokia |  |  |
| Brian A. Redding |  |  | Qualcomm |  |  |
