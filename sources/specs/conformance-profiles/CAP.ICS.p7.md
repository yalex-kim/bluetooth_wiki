# CAP.ICS.p7

> Source: PDF converted via PyMuPDF.

---

Common Audio Profile (CAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: CAP.ICS.p7 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Generic Audio Working Group ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2020–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other
third-party brands and names are the property of their respective owners.
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
| 1 |  |  | Acceptor |  |  | [1] 3 |  |  | C.1 |  |  |
| 2 |  |  | Initiator |  |  | [1] 3 |  |  | C.1 |  |  |
| 3 |  |  | Commander |  |  | [1] 3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.5 |  |  | C.1 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.5 |  |  | C.2, C.3 |  |  |

C.1: Excluded for this Profile. C.2: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core-
Controller”. C.3: Mandatory for this Profile.

### 2.3 Host Configurations

Table 3: GAP Host Configuration

| Item | Device Configuration | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GAP LE Host | [1] 2.5 | M | [2] GAP 0b/2 |  |  |
| 2 | GAP BR/EDR Host | [1] 2.5 | O | [2] GAP 0b/1 |  |  |

Note: A GAP BR/EDR/LE Host will need to select CAP 3/1 and CAP 3/2.

### 2.4 Acceptor role

Table 4: X.Y Versions
Prerequisite: CAP 1/1 “Acceptor”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP v1.0 |  |  | [1] |  |  | M |  |  |

Table 5: X.Y.Z Versions
Prerequisite: CAP 1/1 “Acceptor”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP v1.0.1 |  |  | [18] |  |  | O |  |  |

Prerequisite: CAP 1/1 “Acceptor”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CSIP Set Member | [1] 3 | O | [4] CSIP 1/1 |  |  |
| 2 | BAP Scan Delegator | [1] 3 | C.2 | [3] BAP 1/5 |  |  |
| 3 | BAP Broadcast Sink | [1] 3 | C.1 | [3] BAP 1/4 |  |  |
| 4 | BAP Unicast Server | [1] 3 | C.1 | [3] BAP 1/1 |  |  |
| 5 | VCP Volume Renderer | [1] 3 | O | [8] VCP 1/1 |  |  |
| 6 | MICP Microphone Device | [1] 3 | O | [7] MICP 1/1 |  |  |
| 7 | CCP Call Control Client | [1] 3 | O | [6] CCP 1/2 |  |  |
| 8 | MCP Media Control Client | [1] 3 | O | [5] MCP 1/2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF CAP 6/3 “BAP Broadcast Sink”, otherwise not defined.
Table 6a: Feature Support – Acceptor
Prerequisite: CAP 1/1 “Acceptor”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP Targeted Announcement Support |  |  | [1] 8.1.1, 8.1.2, 8.1.3 |  |  | C.1 |  |  |
| 2 |  |  | CAP General Announcement Support |  |  | [1] 8.1.1, 8.1.2, 8.1.3 |  |  | C.1 |  |  |
| 3 |  |  | Unicast to Broadcast Handover Support |  |  | [1] 4 |  |  | C.2 |  |  |
| 4 |  |  | Broadcast to Unicast Handover Support |  |  | [1] 4 |  |  | C.2 |  |  |

C.1: Mandatory to support at least one IF CAP 6/2 “BAP Scan Delegator” OR CAP 6/5 “VCP Volume
Renderer” OR CAP 6/6 “MICP Microphone Device” OR CAP 6/7 “CCP Call Control Client” OR CAP 6/8 “MCP Media Control Client”, otherwise Excluded. C.2: Optional IF CAP 6/2 “BAP Scan Delegator” AND CAP 6/3 “BAP Broadcast Sink” AND CAP 6/4
“BAP Unicast Server”, otherwise Excluded.
Table 6b: Unicast Server BAP Audio Role – Acceptor
Prerequisite: CAP 6/4 “BAP Unicast Server”

| Item | Role | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Audio Source | [1] 3 | C.1 | [3] BAP 8/2 |  |  |
| 2 | Audio Sink | [1] 3 | C.1 | [3] BAP 8/1 |  |  |

C.1: Mandatory to support at least one.
Prerequisite: CAP 1/1 “Acceptor”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Service supported over LE (CAS) | [1] 3, 7.3 | M | [16] CAS 2/2 |  |  |
| 2 | Service supported over LE (VCS) | [1] 4, 7.3 | C.1 | [11] VCS 1/2 |  |  |
| 3 | Service supported over LE (VOCS) | [1] 4.1.3, 7.3 | C.2 | [17] VOCS 1/2 |  |  |
| 4 | Service supported over LE (MICS) | [1] 4, 7.3 | C.3 | [12] MICS 1/2 |  |  |
| 5 | Service supported over LE (AICS) | [1] 4, 7.3 | C.4 | [15] AICS 1/2 |  |  |
| 6 | Service supported over LE (CSIS) | [1] 4.1.1, 7.3 | C.5 | [10] CSIS 1/2 |  |  |
| 7 | Service supported over LE (ASCS) | [1] 4, 7.3 | C.6 | [14] ASCS 2/2 |  |  |
| 8 | Service supported over LE (BASS) | [1] 4, 7.3 | C.7 | [9] BASS 2/2 |  |  |
| 9 | Service supported over LE (PACS) | [1] 4, 7.3 | C.8 | [13] PACS 2/2 |  |  |

C.1: Mandatory IF CAP 6/5 “VCP Volume Renderer”, otherwise not defined. C.2: Optional IF CAP 6/5 “VCP Volume Renderer”, otherwise not defined. C.3: Mandatory IF CAP 6/6 “MICP Microphone Device”, otherwise not defined. C.4: Optional IF CAP 6/6 “MICP Microphone Device” OR CAP 6/5 “VCP Volume Renderer”, otherwise
not defined. C.5: Mandatory IF CAP 6/1 “CSIP Set Member”, otherwise not defined. C.6: Mandatory IF CAP 6/4 “BAP Unicast Server”, otherwise not defined. C.7: Mandatory IF CAP 6/2 “BAP Scan Delegator”, otherwise not defined. C.8: Mandatory IF CAP 6/4 “BAP Unicast Server” OR CAP 6/3 “BAP Broadcast Sink”, otherwise not
defined.
Table 8: Audio Stream Transition Procedure Support – Acceptor
Prerequisite: CAP 1/1 “Acceptor”

|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unicast Audio Start procedure |  |  | [1] 7.3.1.2 |  |  | C.1 |  |  |
| 2 |  |  | Unicast Audio Update procedure |  |  | [1] 7.3.1.3 |  |  | C.1 |  |  |
| 3 |  |  | Unicast Audio Stop procedure |  |  | [1] 7.3.1.4 |  |  | C.1 |  |  |
| 4 |  |  | Find Content Control Service procedure |  |  | [1] 7.3.3.2 |  |  | O |  |  |
| 5 |  |  | Unicast to Broadcast Handover procedure |  |  | [1] 7.3.1.10 |  |  | C.2 |  |  |
| 6 |  |  | Broadcast to Unicast Handover procedure |  |  | [1] 7.3.1.11 |  |  | C.3 |  |  |

C.1: Mandatory IF CAP 6/4 “BAP Unicast Server”, otherwise Excluded. C.2: Mandatory IF CAP 6a/3 “Unicast to Broadcast Handover Support”, otherwise Excluded. C.3: Mandatory IF CAP 6a/4 “Broadcast to Unicast Handover Support”, otherwise Excluded.

#### 2.4.1 CSIS requirements

Table 9: Coordinated Set Features – Acceptor
Prerequisite: CAP 6/1 “CSIP Set Member”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Included CSIS Instance | [1] 4.4.1 | M | [16] CAS 3/1 |  |  |

Table 10: CSIS Requirements – Acceptor
Prerequisite: CAP 6/1 “CSIP Set Member”

| Item | Characteristic | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set Member Rank Characteristic | [1] 4.4.1 | M | [10] CSIS 2/4 |  |  |
| 2 | Coordinated Set Size Characteristic | [1] 4.4.1 | M | [10] CSIS 2/2 |  |  |


#### 2.4.2 Context Type requirements

Table 11: Supported Context Types – Acceptor
Prerequisite: CAP 1/1 “Acceptor”

|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unspecified |  |  | [1] 7.1 |  |  | M |  |  |
| 2 |  |  | Conversational |  |  | [1] 7.1 |  |  | O |  |  |
| 3 |  |  | Media |  |  | [1] 7.1 |  |  | O |  |  |
| 4 |  |  | Game |  |  | [1] 7.1 |  |  | O |  |  |
| 5 |  |  | Instructional |  |  | [1] 7.1 |  |  | O |  |  |
| 6 |  |  | Voice assistants |  |  | [1] 7.1 |  |  | O |  |  |
| 7 |  |  | Live |  |  | [1] 7.1 |  |  | O |  |  |
| 8 |  |  | Sound effects |  |  | [1] 7.1 |  |  | O |  |  |
| 9 |  |  | Notifications |  |  | [1] 7.1 |  |  | O |  |  |
| 10 |  |  | Ringtone |  |  | [1] 7.1 |  |  | O |  |  |
| 11 |  |  | Alerts |  |  | [1] 7.1 |  |  | O |  |  |
| 12 |  |  | Emergency Alarm |  |  | [1] 7.1 |  |  | O |  |  |


#### 2.4.3 CCP requirements

Table 12: CCP Requirements – Acceptor
Prerequisite: CAP 6/7 “CCP Call Control Client”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Status Flags procedure |  |  | [1] 4.4.3 |  |  | M |  |  |


#### 2.4.4 GAP requirements

Table 13: GAP Requirements – Acceptor
Prerequisite: CAP 1/1 “Acceptor”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Observer | [1] 2.4 | C.1 | [2] GAP 5/2 |  |  |
| 2 | Peripheral | [1] 2.4 | C.2 | [2] GAP 5/3 |  |  |

C.1: Mandatory IF CAP 6/3 “BAP Broadcast Sink”, otherwise not defined. C.2: Mandatory IF CAP 6/4 “BAP Unicast Server” OR CAP 6/3 “BAP Broadcast Sink” OR CAP 6/2 “BAP Scan Delegator” OR CAP 6/5 “VCP Volume Renderer” OR CAP 6/6 “MICP Microphone Device” OR CAP 6/7 “CCP Call Control Client” OR CAP 6/8 “MCP Media Control Client”, otherwise not defined.

### 2.5 Initiator role

Table 14: X.Y Versions
Prerequisite: CAP 1/2 “Initiator”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP v1.0 |  |  | [1] |  |  | M |  |  |

Table 15: X.Y.Z Versions
Prerequisite: CAP 1/2 “Initiator”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP v1.0.1 |  |  | [18] |  |  | O |  |  |

Table 16: CAP Role Dependency Support – Initiator
Prerequisite: CAP 1/2 “Initiator”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CSIP Set Coordinator | [1] 3 | C.1 | [4] CSIP 1/2 |  |  |
| 2 | BAP Broadcast Source | [1] 3 | C.2 | [3] BAP 1/3 |  |  |
| 3 | BAP Unicast Client | [1] 3 | C.2 | [3] BAP 1/2 |  |  |
| 4 | BAP Broadcast Assistant | [1] 3 | O | [3] BAP 1/6 |  |  |
| 5 | CCP Call Control Server | [1] 3 | O | [6] CCP 1/1 |  |  |
| 6 | MCP Media Control Server | [1] 3 | O | [5] MCP 1/1 |  |  |

C.1: Mandatory IF CAP 16/3 “BAP Unicast Client” OR CAP 16/4 “BAP Broadcast Assistant”, otherwise not defined. C.2: Mandatory to support at least one.
Prerequisite: CAP 1/2 “Initiator”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Multiple ASCS Server Support |  |  | [1] 7 |  |  | M |  |  |
| 2 |  |  | Multiple Broadcast Source Stream Support |  |  | [1] 7 |  |  | C.1 |  |  |
| 3 |  |  | Unicast to Broadcast Handover Support |  |  | [1] 5 |  |  | C.2 |  |  |
| 4 |  |  | Broadcast to Unicast Handover Support |  |  | [1] 5 |  |  | C.3 |  |  |
| 5 |  |  | Encrypted Broadcast Source |  |  | [1] 3 |  |  | C.1 |  |  |

C.1: Optional IF CAP 16/2 “BAP Broadcast Source”, otherwise Excluded. C.2: Optional IF CAP 1/3 “Commander” AND CAP 16/3 “BAP Unicast Client” AND CAP 16/2 “BAP Broadcast Source” AND CAP 16/4 “BAP Broadcast Assistant”, otherwise Excluded. C.3: Optional IF CAP 1/3 “Commander” AND CAP 16/3 “BAP Unicast Client” AND CAP 16/2 “BAP Broadcast Source”, otherwise Excluded.
Table 18: Unicast Client BAP Audio Role – Initiator
Prerequisite: CAP 16/3 “BAP Unicast Client”

| Item | Role | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Audio Source | [1] 3 | C.1 | [3] BAP 29/2 |  |  |
| 2 | Audio Sink | [1] 3 | C.1 | [3] BAP 29/1 |  |  |

C.1: Mandatory to support at least one.
Table 19: Service Requirements – Initiator
Prerequisite: CAP 1/2 “Initiator”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Telephone Bearer Service | [1] 3, 7.3 | C.1 | [6] CCP 5/1 |  |  |
| 2 | Generic Telephone Bearer Service | [1] 3, 7.3 | C.3 | [6] CCP 5/2 |  |  |
| 3 | Media Control Service | [1] 3, 7.3 | C.2 | [5] MCP 5/1 |  |  |
| 4 | Generic Media Control Service | [1] 3, 7.3 | C.4 | [5] MCP 5/2 |  |  |

C.1: Optional IF CAP 16/5 “CCP Call Control Server”, otherwise not defined. C.2: Optional IF CAP 16/6 “MCP Media Control Server”, otherwise not defined. C.3: Mandatory IF CAP 16/5 “CCP Call Control Server”, otherwise not defined. C.4: Mandatory IF CAP 16/6 “MCP Media Control Server”, otherwise not defined.
Table 20: Audio Stream Transition Procedure Support – Initiator
Prerequisite: CAP 1/2 “Initiator”

|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unicast Audio Start procedure |  |  | [1] 5 |  |  | C.1 |  |  |
| 2 |  |  | Unicast Audio Update procedure |  |  | [1] 5 |  |  | C.2 |  |  |


|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Unicast Audio Stop procedure |  |  | [1] 5 |  |  | C.1 |  |  |
| 4 |  |  | Broadcast Audio Start procedure |  |  | [1] 5 |  |  | C.3 |  |  |
| 5 |  |  | Broadcast Audio Update procedure |  |  | [1] 5 |  |  | C.4 |  |  |
| 6 |  |  | Broadcast Audio Stop procedure |  |  | [1] 5 |  |  | C.3 |  |  |
| 7 |  |  | Unicast to Broadcast Handover procedure |  |  | [1] 5 |  |  | C.5 |  |  |
| 8 |  |  | Broadcast to Unicast Handover procedure |  |  | [1] 5 |  |  | C.6 |  |  |
| 9 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |

C.1: Mandatory IF CAP 16/3 “BAP Unicast Client”, otherwise Excluded. C.2: Optional IF CAP 16/3 “BAP Unicast Client”, otherwise Excluded. C.3: Mandatory IF CAP 16/2 “BAP Broadcast Source”, otherwise Excluded. C.4: Optional IF CAP 16/2 “BAP Broadcast Source”, otherwise Excluded. C.5: Mandatory IF CAP 1/3 “Commander” AND CAP 17/3 “Unicast to Broadcast Handover Support”,
otherwise Excluded. C.6: Mandatory IF CAP 1/3 “Commander” AND CAP 17/4 “Broadcast to Unicast Handover Support”,
otherwise Excluded.

#### 2.5.1 BAP requirements

Table 21: BAP Procedures Requirements – Initiator
Prerequisite: CAP 1/2 “Initiator”

| Item | Procedure | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | BAP Available Audio Contexts discovery procedure | [1] 5.4 | C.1 | N/A |  |  |
| 2 | BAP Broadcast Audio Stream Metadata Update | [1] 5.4 | C.2 | [3] BAP 51/1 |  |  |
| 3 | No longer used | N/A | N/A | N/A |  |  |
| 4 | BAP Broadcast Audio Stream Reconfiguration | [1] 7.3.1.5 | C.2 | [3] BAP 51/2 |  |  |

C.1: Mandatory IF CAP 16/3 “BAP Unicast Client”, otherwise Excluded. C.2: Optional IF CAP 16/2 “BAP Broadcast Source”, otherwise not defined.

#### 2.5.2 Context Type requirements

Table 22: Supported Context Types – Initiator
Prerequisite: CAP 1/2 “Initiator”

|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unspecified |  |  | [1] 7.1 |  |  | M |  |  |
| 2 |  |  | Conversational |  |  | [1] 7.1 |  |  | O |  |  |
| 3 |  |  | Media |  |  | [1] 7.1 |  |  | O |  |  |
| 4 |  |  | Game |  |  | [1] 7.1 |  |  | O |  |  |
| 5 |  |  | Instructional |  |  | [1] 7.1 |  |  | O |  |  |
| 6 |  |  | Voice assistants |  |  | [1] 7.1 |  |  | O |  |  |
| 7 |  |  | Live |  |  | [1] 7.1 |  |  | O |  |  |


|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 |  |  | Sound effects |  |  | [1] 7.1 |  |  | O |  |  |
| 9 |  |  | Notifications |  |  | [1] 7.1 |  |  | O |  |  |
| 10 |  |  | Ringtone |  |  | [1] 7.1 |  |  | O |  |  |
| 11 |  |  | Alerts |  |  | [1] 7.1 |  |  | O |  |  |
| 12 |  |  | Emergency Alarm |  |  | [1] 7.1 |  |  | O |  |  |


#### 2.5.3 GAP requirements

Table 23: GAP Requirements – Initiator
Prerequisite: CAP 1/2 “Initiator”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Broadcaster | [1] 2.4 | C.1 | [2] GAP 5/1 |  |  |
| 2 | Central | [1] 2.4 | C.2 | [2] GAP 5/4 |  |  |

C.1: Mandatory IF CAP 16/2 “BAP Broadcast Source”, otherwise not defined. C.2: Mandatory IF CAP 16/3 “BAP Unicast Client” OR CAP 16/4 “BAP Broadcast Assistant” OR
CAP 16/5 “CCP Call Control Server” OR CAP 16/6 “MCP Media Control Server” OR CAP 16/1 “CSIP Set Coordinator”, otherwise not defined.

#### 2.5.4 GATT requirements

Table 23a: GATT Requirements
Prerequisite: CAP 16/3 “BAP Unicast Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Client over LE | [1] 5.2 | M | [5] GATT 1a/1 |  |  |
| 2 | Discover All Primary Services | [1] 5.2 | C.1 | [5] GATT 3/2 |  |  |
| 3 | Discover Primary Service by Service UUID | [1] 5.2 | C.1 | [5] GATT 3/3 |  |  |
| 4 | Find Included Services | [1] 5.2 | M | [5] GATT 3/4 |  |  |

C.1: Mandatory to support at least one.

### 2.6 Commander role

Table 24: X.Y Versions
Prerequisite: CAP 1/3 “Commander”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP v1.0 |  |  | [1] |  |  | M |  |  |

Prerequisite: CAP 1/3 “Commander”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CAP v1.0.1 |  |  | [18] |  |  | O |  |  |

Table 26: CAP Role Dependency Support – Commander
Prerequisite: CAP 1/3 “Commander”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CSIP Set Coordinator | [1] 3 | M | [4] CSIP 1/2 |  |  |
| 2 | BAP Broadcast Assistant | [1] 3 | C.1, C.2 | [3] BAP 1/6 |  |  |
| 3 | BAP Scan Delegator | [1] 3 | C.1 | [3] BAP 1/5 |  |  |
| 4 | VCP Volume Controller | [1] 3 | C.1 | [8] VCP 1/2 |  |  |
| 5 | MICP Microphone Controller | [1] 3 | C.1 | [7] MICP 1/2 |  |  |
| 6 | CCP Call Control Client | [1] 3 | O | [6] CCP 1/2 |  |  |
| 7 | MCP Media Control Client | [1] 3 | O | [5] MCP 1/2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF CAP 26/3 “BAP Scan Delegator”, otherwise Optional.
Table 27: Feature Support – Commander
Prerequisite: CAP 1/3 “Commander”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Multiple Broadcast Stream Support |  |  | [1] 7 |  |  | O |  |  |
| 2 |  |  | Unicast to Broadcast Handover Support |  |  | [1] 6 |  |  | C.1 |  |  |
| 3 |  |  | Broadcast to Unicast Handover Support |  |  | [1] 6 |  |  | C.2 |  |  |
| 4 |  |  | CAP Targeted Announcement Support |  |  | [1] 8.1.1, 8.1.2, 8.1.3 |  |  | C.3 |  |  |
| 5 |  |  | CAP General Announcement Support |  |  | [1] 8.1.1, 8.1.2, 8.1.3 |  |  | C.3 |  |  |

C.1: Optional IF CAP 1/2 “Initiator” AND CAP 26/2 “BAP Broadcast Assistant”, otherwise Excluded. C.2: Optional IF CAP 1/2 “Initiator”, otherwise Excluded. C.3: Mandatory to support at least one IF CAP 26/3 “BAP Scan Delegator” OR CAP 26/6 “CCP Call
Control Client” OR CAP 26/7 “MCP Media Control Client”, otherwise Excluded.
Table 28: Procedures – Commander
Prerequisite: CAP 1/3 “Commander”

|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Audio Stream Transition |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  |  | Broadcast Audio Reception Start procedure |  |  | [1] 7.3.1.8 |  |  | C.1 |  |  |
| 2 |  |  | Broadcast Audio Reception Stop procedure |  |  | [1] 7.3.1.9 |  |  | C.1 |  |  |
| 3 |  |  | Unicast to Broadcast Handover procedure |  |  | [1] 7.3.1.10 |  |  | C.2 |  |  |


|  | Item |  |  | Procedure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | Broadcast to Unicast Handover procedure |  |  | [1] 7.3.1.11 |  |  | C.3 |  |  |
| 5 |  |  | Distribute Broadcast Code procedure |  |  | [1] 7.3.1.12 |  |  | C.4 |  |  |
| Capture and Rendering Control |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  | Change Volume procedure |  |  | [1] 7.3.2.2 |  |  | C.5 |  |  |
| 7 |  |  | Change Volume Offset procedure |  |  | [1] 7.3.2.3 |  |  | C.6 |  |  |
| 8 |  |  | Change Volume Mute State procedure |  |  | [1] 7.3.2.4 |  |  | C.5 |  |  |
| 9 |  |  | Microphone Mute State procedure |  |  | [1] 7.3.2.5 |  |  | C.7 |  |  |
| 10 |  |  | Change Microphone Gain Setting procedure |  |  | [1] 7.3.2.6 |  |  | C.8 |  |  |
| Content Control |  |  |  |  |  |  |  |  |  |  |  |
| 11 |  |  | Find Content Control Service procedure |  |  | [1] 7.3.3.2 |  |  | O |  |  |

C.1: Mandatory IF CAP 26/2 “BAP Broadcast Assistant”, otherwise Excluded. C.2: Mandatory IF CAP 27/2 “Unicast to Broadcast Handover Support”, otherwise Excluded. C.3: Mandatory IF CAP 27/3 “Broadcast to Unicast Handover Support”, otherwise Excluded. C.4: Optional IF CAP 26/2 “BAP Broadcast Assistant”, otherwise Excluded. C.5: Mandatory IF CAP 26/4 “VCP Volume Controller”, otherwise Excluded. C.6: Optional IF CAP 26/4 “VCP Volume Controller”, otherwise Excluded. C.7: Mandatory IF CAP 26/5 “MICP Microphone Controller”, otherwise Excluded. C.8: Optional IF CAP 28/9 “Microphone Mute State procedure”, otherwise Excluded.
Table 29: Service Requirements – Commander
Prerequisite: CAP 1/3 “Commander”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Service supported over LE (CAS) | [1] 6 | C.1 | [16] CAS 2/2 |  |  |

C.1: Mandatory IF CAP 27/5 “CAP General Announcement Support” OR CAP 27/4 “CAP Targeted
Announcement Support”, otherwise not defined.

#### 2.6.1 BAP procedures

Table 30: BAP Procedures Requirements – Commander
Prerequisite: CAP 26/2 “BAP Broadcast Assistant”

| Item | Procedure | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Broadcast Audio capability discovery procedure | [1] 6.4 | M | N/A |  |  |
| 2 | Add Source operation | [1] 6.4 | M | [3] BAP 88/3 |  |  |
| 3 | Modify Source operation | [1] 6.4 | O | [3] BAP 88/4 |  |  |
| 4 | Remove Source operation | [1] 6.4 | M | [3] BAP 88/7 |  |  |


#### 2.6.2 VCP procedures

Table 31: VCP Volume Controller Procedures Requirements – Commander
Prerequisite: CAP 26/4 “VCP Volume Controller”

| Item | Procedure | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set Absolute Volume | [1] 6.4 | M | [8] VCP 12/6 |  |  |
| 2 | Set Volume Offset | [1] 6.4 | O | [8] VCP 14/6 |  |  |
| 3 | Mute | [1] 6.4 | M | [8] VCP 12/11 |  |  |
| 4 | Unmute | [1] 6.4 | M | [8] VCP 12/12 |  |  |


#### 2.6.3 MICP procedures

Table 32: MICP Procedures Requirements – Commander
Prerequisite: CAP 26/5 “MICP Microphone Controller”

| Item | Procedure | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set Mute | [1] 6.4 | M | [7] MICP 12/3 |  |  |
| 2 | Set Gain Setting | [1] 6.4 | C.1 | [7] MICP 14/7 |  |  |

C.1: Mandatory IF CAP 28/10 “Change Microphone Gain Setting procedure”, otherwise not defined.

#### 2.6.4 GAP requirements

Table 33: GAP Requirements – Commander
Prerequisite: CAP 1/3 “Commander”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Central | [1] 2.4 | C.1 | [2] GAP 5/4 |  |  |
| 2 | Peripheral | [1] 2.4 | C.2 | [2] GAP 5/3 |  |  |

C.1: Mandatory IF CAP 26/2 “BAP Broadcast Assistant” OR CAP 26/4 “VCP Volume Controller” OR
CAP 26/5 “MICP Microphone Controller” OR CAP 26/1 “CSIP Set Coordinator”, otherwise not defined. C.2: Mandatory IF CAP 26/3 “BAP Scan Delegator” OR CAP 26/6 “CCP Call Control Client” OR
CAP 26/7 “MCP Media Control Client”, otherwise not defined.

#### 2.6.5 GATT requirements

Table 33a: GATT Requirements
Prerequisite: CAP 1/3 “Commander”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Client over LE | [1] 6.2 | M | [5] GATT 1a/1 |  |  |
| 2 | Discover All Primary Services | [1] 6.2 | C.1 | [5] GATT 3/2 |  |  |
| 3 | Discover Primary Service by Service UUID | [1] 6.2 | C.1 | [5] GATT 3/3 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 4 | Find Included Services | [1] 6.2 | M | [5] GATT 3/4 |  |  |

C.1: Mandatory to support at least one.

## 3 References

[1] Common Audio Profile Specification, Version 1.0 or later
[2] ICS Proforma for Generic Access Profile (GAP)
[3] ICS Proforma for Basic Audio Profile (BAP)
[4] ICS Proforma for Coordinated Set Identification Profile (CSIP)
[5] ICS Proforma for Media Control Profile (MCP)
[6] ICS Proforma for Call Control Profile (CCP)
[7] ICS Proforma for Microphone Control Profile (MICP)
[8] ICS Proforma for Volume Control Profile (VCP)
[9] ICS Proforma for Broadcast Audio Scan Service (BASS)
[10] ICS Proforma for Coordinated Set Identification Service (CSIS)
[11] ICS Proforma for Volume Control Service (VCS)
[12] ICS Proforma for Microphone Control Service (MICS)
[13] ICS Proforma for Published Audio Capabilities Service (PACS)
[14] ICS Proforma for Audio Stream Control Service (ASCS)
[15] ICS Proforma for Audio Input Control Service (AICS)
[16] ICS Proforma for Common Audio Service (CAS)
[17] ICS Proforma for Volume Offset Control Service (VOCS)
[18] Common Audio Profile Specification, Version 1.0.1

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2022-03-29 | Approved by BTI on 2022-03-09. CAP v1.0 adopted by the BoD on 2022-03-22. Prepared for publication. |
|  |  |  | p1r00 |  |  | 2022-04-05 | TSE 18639 (rating 2): Updated C.2 for Table 26 to address a consistency check failure on selecting only BAP Broadcast Assistant role in CAP Commander. |
| 1 |  |  | p1 |  |  | 2022-06-28 | Approved by BTI on 2022-06-20. EE 18898 adopted by the BoD on 2022-06-21. Prepared for TCRL 2022-1 publication. |
|  |  |  | p2r00–r01 |  |  | 2022-08-25 – 2022-11-23 | TSE 18838 (rating 3): Added new table for “Feature Support – Acceptor” (Table 6a). Updated 27/4 and 27/5 and modified 27/C.3. Consistency checker editorials. |
| 2 |  |  | p2 |  |  | 2023-02-07 | Approved by BTI on 2022-12-19. Prepared for TCRL 2022-2 publication. |
|  |  |  | p3r00–r02 |  |  | 2023-10-04 – 2023-11-28 | TSE 24104 (rating 1): Removed the Reference items for the GTBS and GMCS ICSs. Replaced GTBS reference with TBS reference and GMCS reference with MCS reference in Table 19, updating the ILDs for 19/2 and 19/4 as well as C.1 and C.2. |
| 3 |  |  | p3 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p4r00–r05 |  |  | 2024-10-24 – 2024-12-18 | TSE 18802 (rating 2): For Table 19, updated Reference, Status, and Inter-Layer Dependency values and conditionals C.1 and C.2, and added conditionals C.3 and C.4. TSE 24857 (rating 1): Per E18922, deleted Item 9 from Table 20. Deleted conditional C.7 from Table 20. TSE 26908 (rating 1): Per E18922, E19214, E23221, E23780, E24511, E24713, E25020, E25591, E26552, and E26553, added Tables 5, 15, and 25 to account for CAP v1.0.1 as part of the .Z release. Updated the references list. Abbreviated the specification name in Tables 14 and 24 to align with the current ICS template. |
| 4 |  |  | p4 |  |  | 2025-02-18 | Approved by BTI on 2025-02-09. CAP v1.0.1 adopted by the BoD on 2024-02-11. Prepared for TCRL 2025-1 publication. |
|  |  |  | p4ed2r00 |  |  | 2025-02-12 | TSE 27090 (rating 1): Added back 20/9 marked as no longer used. |
|  |  |  | p4 edition 2 |  |  | 2025-03-14 | Approved by BTI on 2025-03-11. Prepared for edition 2 publication. |
|  |  |  | p5r00–r03 |  |  | 2025-04-08 – 2025-05-18 | TSE 26834 (rating 2): Added GATT requirements sections including new Tables 23a and 33a. TSE 26982 (rating 2): Added Table 6b, Unicast Server BAP Audio Role – Acceptor. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 27349 (rating 1): Updated the Status value for CAP 2/2. Added conditionals C.2 and C.3 to Table 2. |
| 5 |  |  | p5 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p6r00–r04 |  |  | 2025-07-22 – 2025-08-19 | TSE 27524 (rating 1): Updated title to Section 2.3 and Table 3. Updated Device Configuration, Status, and ILD in CAP 3/1 and CAP 3/2. Removed conditional C.1 in Table 3 and added note. TSE 27570 (rating 2): Added two new rows to Tables 6a and 8. Added conditional C.2 to Table 6a and conditionals C.2 and C.3 to Table 8. TSE 27572 (rating 1): Updated the ILD value for CAP 13/1, CAP 13/2, CAP 23/1, CAP 23/2, CAP 33/1, and CAP 33/2. TSE 27607 (rating 2): Added new row and ILD column to Table 21. Deleted draft revision history comments prior to p0. |
| 6 |  |  | p6 |  |  | 2025-11-04 | Approved by BTI on 2025-09-29. Prepared for TCRL pkg101 publication. |
|  |  |  | p7r00–r02 |  |  | 2025-12-05 – 2025-12-31 | TSE 28231 (rating 1): Updated Table 7, condition C.4, to modify the status value for CAP 7/5. TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 7 |  |  | p7 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Dejan Berec |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Jim Harper |  |  | Bluetooth SIG, Inc. |  |  |
| Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |  |
