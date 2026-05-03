# CCP.ICS.p4

> Source: PDF converted via PyMuPDF.

---

Call Control Profile (CCP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: CCP.ICS.p4 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Generic Audio Working Group ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2019–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Call Control Server |  |  | [1] 3 |  |  | C.1 |  |  |
| 2 |  |  | Call Control Client |  |  | [1] 4 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2 |  |  | C.2, C.3 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”. C.2: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core- Controller”. C.3: Mandatory to support at least one.

### 2.3 Call Control Server role

Table 3: Call Control Server, X.Y Versions
Prerequisite: CCP 1/1 “Call Control Server”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CCP v1.0 |  |  | [1] |  |  | M |  |  |

Table 4: Call Control Server, X.Y.Z Versions
Table number reserved but not yet in use

#### 2.3.1 Server profile feature

Table 5: Server Features
Prerequisite: CCP 1/1 “Call Control Server”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Telephone Bearer Service | [1] 3 | O | [3] TBS 0b/1 |  |  |
| 2 | Generic Telephone Bearer Service | [1] 3 | M | [3] TBS 0b/2 |  |  |
| 3 | LE Extended Advertising | [1] 6.1.1.1 | M | [4] LL 9/41 |  |  |


#### 2.3.2 GAP requirements

Table 6: GAP Requirements – Call Control Server Role
Prerequisite: CCP 1/1 “Call Control Server”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE security mode 1 | [1] 5.1 | C.1 | [2] GAP 25/1 OR GAP 35/1 |  |  |
| 2 | Bondable mode (LE) | [1] 5.1.2 | C.1 | [2] GAP 24/2 OR GAP 34/2 |  |  |
| 3 | Bondable mode (BR/EDR) | [1] 5.1.2 | C.2 | [2] GAP 1/7 |  |  |
| 4 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 5.1.2 | C.7 | [2] GAP 25/11 OR GAP 35/11 |  |  |
| 5 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 5.1.2 | C.7 | [2] GAP 25/12 OR GAP 35/12 |  |  |
| 6 | LE security mode 1 level 4 | [1] 5.1.2 | C.7 | [2] GAP 25/9 OR GAP 35/9 |  |  |
| 7 | Minimum 128 Bit entropy key (LE) | [1] 5.1 | C.3 | [2] GAP 25/13 OR GAP 35/13 |  |  |
| 8 | Derivation of LE LTK from BR/EDR Link Key | [1] 5.1 | C.9 | [2] GAP 41/2b OR GAP 43/2b |  |  |
| 9 | Security mode 4, level 2 | [1] 5.2 | C.5 | [2] GAP 2/7c |  |  |
| 10 | 128-bit encryption key size capable (BR/EDR) | [1] 5.2 | C.5 | [2] GAP 2/13 |  |  |
| 11 | Derivation of BR/EDR Link Key from LE LTK | [1] 5.2 | C.8 | [2] GAP 41/2a OR GAP 43/2a |  |  |
| 12 | BR/EDR Secure Connections | [1] 5.2 | C.8 | N/A |  |  |
| 13 | LE Secure Connections | [1] 5.1 | C.9 | [2] GAP 27b/5 OR GAP 37b/5 |  |  |
| 14 | Out of Band (LE) | [1] 5.1 | C.9 | [2] GAP 27b/9 OR GAP 37b/9 |  |  |
| 15 | Out-of-Band (BR/EDR) | [1] 5.2 | C.8 | [2] GAP 2/14 |  |  |

C.1: Mandatory IF CCP 2/2 “Profile supported over LE”, otherwise not defined. C.2: Optional IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.3: Mandatory IF CCP 6/4 “Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only” OR CCP 6/5 “Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only”, otherwise not defined. C.4: No longer used. C.5: Mandatory IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.6: No longer used. C.7: Mandatory to support at least one IF CCP 2/2 “Profile supported over LE”, otherwise not defined. C.8: Mandatory to support at least one IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.9: Mandatory to support at least one IF CCP 2/2 “Profile supported over LE”, otherwise not defined.

### 2.4 Call Control Client role

Table 8: Call Control Client, X.Y Versions
Prerequisite: CCP 1/2 “Call Control Client”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CCP v1.0 |  |  | [1] |  |  | M |  |  |

Table 9: Call Control Client, X.Y.Z Versions
Table number reserved but not yet in use

#### 2.4.1 Services Support - Call Control Client role

Table 10: Call Control Server Support
Prerequisite: CCP 1/2 “Call Control Client”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Discover Telephone Bearer Service |  |  | [1] 4 |  |  | C.1 |  |  |
| 2 |  |  | Discover Generic Telephone Bearer Service |  |  | [1] 4 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

##### 2.4.1.1 Telephone Bearer Service Support

Table 11: Telephone Bearer Service Characteristic Support by Client
Prerequisite: CCP 10/1 “Discover Telephone Bearer Service”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bearer Provider Name Characteristic |  |  | [1] 4.4.1 |  |  | O |  |  |
| 2 |  |  | Bearer UCI Characteristic |  |  | [1] 4.4.2 |  |  | O |  |  |
| 3 |  |  | Bearer Technology Characteristic |  |  | [1] 4.4.3 |  |  | O |  |  |
| 4 |  |  | Bearer URI Schemes Supported List Characteristic |  |  | [1] 4.4.4 |  |  | O |  |  |
| 5 |  |  | Bearer Signal Strength Characteristic |  |  | [1] 4.4.5 |  |  | O |  |  |
| 6 |  |  | Bearer Signal Strength Reporting Interval Characteristic |  |  | [1] 4.4.6 |  |  | C.1 |  |  |
| 7 |  |  | Bearer List Current Calls Characteristic |  |  | [1] 4.4.8 |  |  | O |  |  |
| 8 |  |  | Content Control ID Characteristic |  |  | [1] 4.4.9 |  |  | O |  |  |
| 9 |  |  | Status Flags Characteristic |  |  | [1] 4.4.11 |  |  | O |  |  |
| 10 |  |  | Incoming Call Target Bearer URI Characteristic |  |  | [1] 4.4.10 |  |  | O |  |  |
| 11 |  |  | Call State Characteristic |  |  | [1] 4.4.12 |  |  | M |  |  |
| 12 |  |  | Call Control Point Characteristic |  |  | [1] 4.4.13 |  |  | O |  |  |
| 13 |  |  | Call Control Point Optional Opcodes Characteristic |  |  | [1] 4.4.14 |  |  | O |  |  |
| 14 |  |  | Termination Reason Characteristic |  |  | [1] 4.5.1 |  |  | O |  |  |
| 15 |  |  | Incoming Call Characteristic |  |  | [1] 4.4.15 |  |  | O |  |  |


|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 |  |  | Call Friendly Name Characteristic |  |  | [1] 4.4.16 |  |  | O |  |  |

C.1: Mandatory IF CCP 11/5 “Bearer Signal Strength Characteristic”, otherwise Excluded.
Table 12: Telephone Bearer Service Procedure Requirements
Prerequisite: CCP 10/1 “Discover Telephone Bearer Service”

|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Bearer Provider Name |  |  | [1] 4.4.1 |  |  | O |  |  |
| 2 |  |  | Read Bearer UCI |  |  | [1] 4.4.2 |  |  | O |  |  |
| 3 |  |  | Read Bearer Technology |  |  | [1] 4.4.3 |  |  | O |  |  |
| 4 |  |  | Read Bearer URI Schemes Supported List |  |  | [1] 4.4.4 |  |  | O |  |  |
| 5 |  |  | Read Bearer Signal Strength |  |  | [1] 4.4.5 |  |  | O |  |  |
| 6 |  |  | Read Bearer Signal Strength Reporting Interval |  |  | [1] 4.4.6 |  |  | O |  |  |
| 7 |  |  | Set Bearer Signal Strength Reporting Interval |  |  | [1] 4.4.7 |  |  | O |  |  |
| 8 |  |  | Read Bearer List Current Calls |  |  | [1] 4.4.8 |  |  | O |  |  |
| 9 |  |  | Read Content Control ID |  |  | [1] 4.4.9 |  |  | O |  |  |
| 10 |  |  | Read Status Flags |  |  | [1] 4.4.11 |  |  | O |  |  |
| 11 |  |  | Read Incoming Call Target Bearer URI |  |  | [1] 4.4.10 |  |  | O |  |  |
| 12 |  |  | Read Call State |  |  | [1] 4.4.12 |  |  | M |  |  |
| 13 |  |  | Answer Incoming Call |  |  | [1] 4.4.13.1 |  |  | O |  |  |
| 14 |  |  | Terminate Call |  |  | [1] 4.4.13.2 |  |  | O |  |  |
| 15 |  |  | Move Call To Local Hold |  |  | [1] 4.4.13.3 |  |  | O |  |  |
| 16 |  |  | Move Locally Held Call To Active Call |  |  | [1] 4.4.13.4 |  |  | O |  |  |
| 17 |  |  | Move Locally Held Call To Remotely Held |  |  | [1] 4.4.13.5 |  |  | O |  |  |
| 18 |  |  | Originate Call |  |  | [1] 4.4.13.6 |  |  | O |  |  |
| 19 |  |  | Join Calls |  |  | [1] 4.4.13.7 |  |  | O |  |  |
| 20 |  |  | Read Call Control Point Optional Opcodes |  |  | [1] 4.4.14 |  |  | O |  |  |
| 21 |  |  | Read Incoming Call |  |  | [1] 4.4.15 |  |  | O |  |  |
| 22 |  |  | Read Call Friendly Name |  |  | [1] 4.4.16 |  |  | O |  |  |


##### 2.4.1.2 Generic Telephone Bearer Server

Table 13: Generic Telephone Bearer Service Characteristic Support by Client
Prerequisite: CCP 10/2 “Discover Generic Telephone Bearer Service”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bearer Provider Name Characteristic |  |  | [1] 4.4.1 |  |  | O |  |  |
| 2 |  |  | Bearer UCI Characteristic |  |  | [1] 4.4.2 |  |  | O |  |  |
| 3 |  |  | Bearer Technology Characteristic |  |  | [1] 4.4.3 |  |  | O |  |  |
| 4 |  |  | Bearer URI Schemes Supported List Characteristic |  |  | [1] 4.4.4 |  |  | O |  |  |
| 5 |  |  | Bearer Signal Strength Characteristic |  |  | [1] 4.4.5 |  |  | O |  |  |


|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 |  |  | Bearer Signal Strength Reporting Interval Characteristic |  |  | [1] 4.4.6 |  |  | C.1 |  |  |
| 7 |  |  | Bearer List Current Calls Characteristic |  |  | [1] 4.4.8 |  |  | O |  |  |
| 8 |  |  | Content Control ID Characteristic |  |  | [1] 4.4.9 |  |  | O |  |  |
| 9 |  |  | Status Flags Characteristic |  |  | [1] 4.4.11 |  |  | O |  |  |
| 10 |  |  | Incoming Call Target Bearer URI Characteristic |  |  | [1] 4.4.10 |  |  | O |  |  |
| 11 |  |  | Call State Characteristic |  |  | [1] 4.4.12 |  |  | M |  |  |
| 12 |  |  | Call Control Point Characteristic |  |  | [1] 4.4.13 |  |  | O |  |  |
| 13 |  |  | Call Control Point Optional Opcodes Characteristic |  |  | [1] 4.4.14 |  |  | O |  |  |
| 14 |  |  | Termination Reason Characteristic |  |  | [1] 4.5.1 |  |  | O |  |  |
| 15 |  |  | Incoming Call Characteristic |  |  | [1] 4.4.15 |  |  | O |  |  |
| 16 |  |  | Call Friendly Name Characteristic |  |  | [1] 4.4.16 |  |  | O |  |  |

C.1: Mandatory IF CCP 13/5 “Bearer Signal Strength Characteristic”, otherwise Excluded.
Table 14: Generic Telephone Bearer Service Procedure Requirements
Prerequisite: CCP 10/2 “Discover Generic Telephone Bearer Service”

|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Bearer Provider Name |  |  | [1] 4.4.1 |  |  | O |  |  |
| 2 |  |  | Read Bearer UCI |  |  | [1] 4.4.2 |  |  | O |  |  |
| 3 |  |  | Read Bearer Technology |  |  | [1] 4.4.3 |  |  | O |  |  |
| 4 |  |  | Read Bearer URI Schemes Supported List |  |  | [1] 4.4.4 |  |  | O |  |  |
| 5 |  |  | Read Bearer Signal Strength |  |  | [1] 4.4.5 |  |  | O |  |  |
| 6 |  |  | Read Bearer Signal Strength Reporting Interval |  |  | [1] 4.4.6 |  |  | O |  |  |
| 7 |  |  | Set Bearer Signal Strength Reporting Interval |  |  | [1] 4.4.7 |  |  | O |  |  |
| 8 |  |  | Read Bearer List Current Calls |  |  | [1] 4.4.8 |  |  | O |  |  |
| 9 |  |  | Read Content Control ID |  |  | [1] 4.4.9 |  |  | O |  |  |
| 10 |  |  | Read Status Flags |  |  | [1] 4.4.11 |  |  | O |  |  |
| 11 |  |  | Read Incoming Call Target Bearer URI |  |  | [1] 4.4.10 |  |  | O |  |  |
| 12 |  |  | Read Call State |  |  | [1] 4.4.12 |  |  | M |  |  |
| 13 |  |  | Answer Incoming Call |  |  | [1] 4.4.13.1 |  |  | O |  |  |
| 14 |  |  | Terminate Call |  |  | [1] 4.4.13.2 |  |  | O |  |  |
| 15 |  |  | Move Call To Local Hold |  |  | [1] 4.4.13.3 |  |  | O |  |  |
| 16 |  |  | Move Locally Held Call To Active Call |  |  | [1] 4.4.13.4 |  |  | O |  |  |
| 17 |  |  | Move Locally Held Call To Remotely Held |  |  | [1] 4.4.13.5 |  |  | O |  |  |
| 18 |  |  | Originate Call |  |  | [1] 4.4.13.6 |  |  | O |  |  |
| 19 |  |  | Join Calls |  |  | [1] 4.4.13.7 |  |  | O |  |  |
| 20 |  |  | Read Call Control Point Optional Opcodes |  |  | [1] 4.4.14 |  |  | O |  |  |
| 21 |  |  | Read Incoming Call |  |  | [1] 4.4.15 |  |  | O |  |  |
| 22 |  |  | Read Call Friendly Name |  |  | [1] 4.4.16 |  |  | O |  |  |


#### 2.4.2 GAP requirements

Table 15: GAP Requirements – Call Control Client Role
Prerequisite: CCP 1/2 “Call Control Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Bondable mode (BR/EDR) | [1] 5.2 | C.1 | [2] GAP 1/7 |  |  |
| 2 | LE security mode 1 | [1] 5.2 | C.2 | [2] GAP 25/1 OR GAP 35/1 |  |  |
| 3 | Bondable mode (LE) | [1] 5.2 | C.2 | [2] GAP 24/2 OR GAP 34/2 |  |  |
| 4 | Bonding procedure | [1] 5.2 | C.2 | [2] GAP 24/3 OR GAP 34/3 |  |  |
| 5 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 5.1.1 | O | [2] GAP 25/11 OR GAP 35/11 |  |  |
| 6 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 5.1.1 | O | [2] GAP 25/12 OR GAP 35/12 |  |  |
| 7 | LE security mode 1 level 4 | [1] 5.1.1 | O | [2] GAP 25/9 OR GAP 35/9 |  |  |
| 8 | Minimum 128 Bit entropy key (LE) | [1] 5.1 | C.4 | [2] GAP 25/13 OR GAP 35/13 |  |  |
| 9 | Derivation of LE LTK from BR/EDR Link Key | [1] 5.1 | C.8 | [2] GAP 41/2b OR GAP 43/2b |  |  |
| 10 | Security mode 4, level 2 | [1] 5.2 | C.3 | [2] GAP 2/7c |  |  |
| 11 | 128-bit encryption key size capable (BR/EDR) | [1] 5.2 | C.3 | [2] GAP 2/13 |  |  |
| 12 | Derivation of BR/EDR Link Key from LE LTK | [1] 5.2 | C.7 | [2] GAP 41/2a OR GAP 43/2a |  |  |
| 13 | BR/EDR Secure Connections | [1] 5.2 | C.7 | N/A |  |  |
| 14 | LE Secure Connections | [1] 5.1 | C.8 | [2] GAP 27b/5 OR GAP 37b/5 |  |  |
| 15 | Out of Band (LE) | [1] 5.1 | C.8 | [2] GAP 27b/9 OR GAP 37b/9 |  |  |
| 16 | Out-of-Band (BR/EDR) | [1] 5.2 | C.7 | [2] GAP 2/14 |  |  |

C.1: Optional IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.2: Mandatory IF CCP 2/2 “Profile supported over LE”, otherwise not defined. C.3: Mandatory IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.4: Mandatory IF CCP 15/5 “Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only” OR CCP 15/6 “Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only”, otherwise not defined. C.5–C.6: No longer used. C.7: Mandatory to support at least one IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.8: Mandatory to support at least one IF CCP 2/2 “Profile supported over LE”, otherwise not defined.

#### 2.4.3 GATT requirements

Table 17: GATT Requirements
Prerequisite: CCP 1/2 “Call Control Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Client over BR/EDR | [1] 4.1 | C.1 | [5] GATT 1a/2 |  |  |
| 2 | GATT Client over LE | [1] 4.1 | C.2 | [5] GATT 1a/1 |  |  |
| 3 | Discover All Primary Services | [1] 4.1 | C.3 | [5] GATT 3/2 |  |  |
| 4 | Discover Primary Service by Service UUID | [1] 4.1 | C.3 | [5] GATT 3/3 |  |  |
| 5 | Find Included Services | [1] 4.1 | O | [5] GATT 3/4 |  |  |
| 6 | Discover All Characteristics of a Service | [1] 4.1 | C.4 | [5] GATT 3/5 |  |  |
| 7 | Discover Characteristics by UUID | [1] 4.1 | C.4 | [5] GATT 3/6 |  |  |
| 8 | Discover All Characteristic Descriptors | [1] 4.1 | M | [5] GATT 3/7 |  |  |
| 9 | Single Notification | [1] 4.1 | M | [5] GATT 3/17 |  |  |
| 10 | Read Characteristic Value | [1] 4.1 | M | [5] GATT 3/8 |  |  |
| 11 | Read Long Characteristic Value | [1] 4.1 | M | [5] GATT 3/10 |  |  |
| 12 | Write Characteristic Value | [1] 4.1 | C.5 | [5] GATT 3/14 |  |  |
| 13 | Write Without Response | [1] 4.1 | C.5 | [5] GATT 3/12 |  |  |
| 14 | Read Characteristic Descriptor | [1] 4.1 | M | [5] GATT 3/19 |  |  |
| 15 | Write Characteristic Descriptor | [1] 4.1 | M | [5] GATT 3/21 |  |  |

C.1: Mandatory IF CCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.2: Mandatory IF CCP 2/2 “Profile supported over LE”, otherwise not defined. C.3: Mandatory to support at least one. C.4: Mandatory to support at least one. C.5: Mandatory to support at least one.

## 3 References

[1] Call Control Profile Specification, Version 1.0
[2] ICS Proforma for Generic Access Profile (GAP)
[3] ICS Proforma for Telephone Bearer Service (TBS)
[4] ICS Proforma for Link Layer (LL)
[5] ICS Proforma for Generic Attribute Profile (GATT)

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2021-03-16 | Approved by BTI on 2021-02-15. CCP v1.0 adopted by the BoD on 2021-03-09. Prepared for publication. |
|  |  |  | p1r00–r02 |  |  | 2021-04-16 – 2021-05-30 | TSE 16755 (rating 1): Updated the inter-layer dependencies in GAP Tables 6 and 15. Consistency checker fixes. |
| 1 |  |  | p1 |  |  | 2021-07-13 | Approved by BTI on 2021-06-01. Prepared for TCRL 2021-1 publication. |
|  |  |  | p1ed2r00 |  |  | 2022-01-25 | TSE 18187 (rating 1): Updated Link Layer inter-layer dependency item in Table 5 to align with updates made in the LL ICS. Made template-related fixes, including aligning the copyright page with v2 of the DNMD. |
|  |  |  | p1 edition 2 |  |  | 2022-01-27 | Approved by BTI on 2022-01-27. Prepared for edition 2 publication. |
|  |  |  | p1ed3r00 |  |  | 2023-02-14 | TSE 22634 (rating 1): Updated ILD references to Security Manager 8/1 to SM 8a/1 (for Central role) or SM 8b/1 (for Peripheral role) in Tables 7 and 16. Updated references. Editorials to align the document with the latest ICS template. |
|  |  |  | p1 edition 3 |  |  | 2023-03-15 | Approved by BTI on 2023-03-13. Prepared for edition 3 publication. |
|  |  |  | p2r00–r04 |  |  | 2023-10-04 – 2023-11-28 | TSE 23344 (rating 2): To resolve GAP/SM ILDs: Removed the item for SM ICS from the References section and updated cross-refs throughout the doc. Updated “or” to “OR” in ILDs throughout the doc. In Table 6, added items 6/12–6/15 and updated conditionals and statuses accordingly. Removed SM requirements heading and deleted Table 7. Updated service names of 10/1 and 10/2 and related prerequisites for Tables 11–14. In Table 15, added items 15/13–15/16 and updated conditionals and statuses accordingly. Removed SM requirements heading and deleted Table 16. TSE 24107 (rating 1): Replaced GTBS reference in 5/2 and updated TBS reference in 5/1. |
| 2 |  |  | p2 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p3r00–r02 |  |  | 2025-02-19 – 2025-05-15 | TSE 26835 (rating 2): Added Table 17. Updated the References section. Applied the current ICS template. TSE 27365 (rating 1): Updated the Status value for CCP 2/1 and CCP 2/2. In Table 2, added conditions C.1 and C.2 and renumbered C.1 as C.3. |
| 3 |  |  | p3 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p4r00–r01 |  |  | 2025-12-05 – 2026-01-14 | TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 4 |  |  | p4 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
