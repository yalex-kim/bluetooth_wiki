# MCP.ICS.p4

> Source: PDF converted via PyMuPDF.

---

Media Control Profile (MCP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: MCP.ICS.p4 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Generic Audio Working Group ▪ Published during TCRL: TCRL.pkg102
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

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Media Control Server |  |  | [1] 3 |  |  | C.1 |  |  |
| 2 |  |  | Media Control Client |  |  | [1] 4 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.4 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.4 |  |  | C.2, C.3 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”. C.2: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core- Controller”. C.3: Mandatory to support at least one.

### 2.3 Media Control Server role


#### 2.3.1 Versions (Media Control Server)

Table 3: X.Y Versions (Media Control Server)
Prerequisite: MCP 1/1 “Media Control Server”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | MCP v1.0 |  |  | [1] |  |  | M |  |  |

Table 4: X.Y.Z Versions (Media Control Server)
Table number reserved but not yet in use

#### 2.3.2 Services (Media Control Server)

Table 5: Service Requirements
Prerequisite: MCP 1/1 “Media Control Server”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Media Control Service | [1] 3 | O | [5] MCS 0b/1 |  |  |
| 2 | Generic Media Control Service | [1] 3 | M | [5] MCS 0b/2 |  |  |
| 3 | Object Transfer Service | [1] 3 | O | [4] OTS |  |  |
| 4 | LE Extended Advertising | [1] 6.1.1.1 | M | [6] LL 9/41 |  |  |


#### 2.3.3 GAP requirements

Table 6: GAP Requirements (Media Control Server Role)
Prerequisite: MCP 1/1 “Media Control Server”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE security mode 1 | [1] 5.1 | C.1 | [2] GAP 25/1 OR GAP 35/1 |  |  |
| 2 | Bondable mode (LE) | [1] 5.1.1 | C.1 | [2] GAP 24/2 OR GAP 34/2 |  |  |
| 3 | Bonding procedure (LE) | [1] 5.1.1 | C.1 | [2] GAP 24/3 OR GAP 34/3 |  |  |
| 4 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 5 | C.6 | [2] GAP 25/11 OR GAP 35/11 |  |  |
| 5 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 5 | C.6 | [2] GAP 25/12 OR GAP 35/12 |  |  |
| 6 | LE security mode 1 level 4 | [1] 5 | C.6 | [2] GAP 25/9 OR GAP 35/9 |  |  |
| 7 | Minimum 128 Bit entropy key (LE) | [1] 5 | C.3 | [2] GAP 25/13 OR GAP 35/13 |  |  |
| 8 | Derivation of LE LTK from BR/EDR Link Key | [1] 5.1 | C.8 | [2] GAP 43/2b OR GAP 41/2b |  |  |
| 9 | Security mode 4, level 2 | [1] 5.2 | C.2 | [2] GAP 2/7c |  |  |
| 10 | 128-bit encryption key size capable (BR/EDR) | [1] 5.2 | C.2 | [2] GAP 2/13 |  |  |
| 11 | Derivation of BR/EDR Link Key from LE LTK | [1] 5.2 | C.7 | [2] GAP 43/2a OR GAP 41/2a |  |  |
| 12 | BR/EDR Secure Connections | [1] 5.2 | C.7 | N/A |  |  |
| 13 | LE Secure Connections | [1] 5.1 | C.8 | [2] GAP 27b/5 OR GAP 37b/5 |  |  |
| 14 | Out of Band (LE) | [1] 5.1 | C.8 | [2] GAP 27b/9 OR GAP 37b/9 |  |  |
| 15 | Out-of-Band (BR/EDR) | [1] 5.2 | C.7 | [2] GAP 2/14 |  |  |

C.1: Mandatory IF MCP 2/2 “Profile supported over LE”, otherwise not defined. C.2: Mandatory IF MCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.3: Mandatory IF MCP 6/4 “Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only” OR MCP 6/5 “Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only”, otherwise not defined. C.4–C.5: No longer used. C.6: Mandatory to support at least one IF MCP 2/2 “Profile supported over LE”, otherwise not defined. C.7: Mandatory to support at least one IF MCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.8: Mandatory to support at least one IF MCP 2/2 “Profile supported over LE”, otherwise not defined.

#### 2.3.4 OTP requirements

Table 8: OTP Requirements (Media Control Server)
Prerequisite: MCP 5/3 “Object Transfer Service”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Object Server | [1] 3 | M | [7] OTP 2/1 |  |  |

Table 9: OTS Characteristics Requirements (Media Control Server)
Prerequisite: MCP 5/3 “Object Transfer Service”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Object ID Characteristic | [3] 3.2.7 | M | [4] OTS 4/12 |  |  |
| 2 | Object List Control Point (OLCP) | [3] 3.4 | M | [4] OTS 4/16 |  |  |
| 3 | Object Changed Characteristic | [3] 3.6 | M | [4] OTS 4/20 |  |  |

Table 10: OTS Feature Requirements (Media Control Server)
Prerequisite: MCP 5/3 “Object Transfer Service”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | OACP Read Procedure | [3] 3.3.2.5 | M | [4] OTS 5/5 |  |  |
| 2 | OLCP Go To Procedure | [3] 3.4.2.5 | M | [4] OTS 6/5 |  |  |


### 2.4 Media Control Client role


#### 2.4.1 Versions (Media Control Client)

Table 11: X.Y Versions (Media Control Client)
Prerequisite: MCP 1/2 “Media Control Client”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | MCP v1.0 |  |  | [1] |  |  | M |  |  |

Table 12: X.Y.Z Versions (Media Control Client)
Table number reserved but not yet in use

#### 2.4.2 Services Support (Media Control Client)


##### 2.4.2.1 Media Control Service

Table 13: Media Control Service Support
Prerequisite: MCP 1/2 “Media Control Client”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Discover Media Control Service |  |  | [1] 4 |  |  | C.1 |  |  |
| 2 |  |  | Discover Generic Media Control Service |  |  | [1] 4 |  |  | C.1 |  |  |
| 3 |  |  | Discover Object Transfer Service |  |  | [1] 4 |  |  | C.2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF MCP 14/20 “Search Results Object ID Characteristic” OR MCP 16/20 “Search Results Object ID Characteristic” OR MCP 14/10 “Current Track Segments Object ID Characteristic” OR MCP 16/10 “Current Track Segments Object ID Characteristic” OR MCP 14/11 “Current Track Object ID Characteristic” OR MCP 16/11 “Current Track Object ID Characteristic”, otherwise Optional.
Table 14: Media Control Service Characteristic Support Requirements
Prerequisite: MCP 13/1 “Discover Media Control Service”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Media Player Name Characteristic |  |  | [1] 4.5.1 |  |  | M |  |  |
| 2 |  |  | Media Player Icon Object ID Characteristic |  |  | [1] 4.5.1 |  |  | O |  |  |
| 3 |  |  | Media Player Icon URL Characteristic |  |  | [1] 4.5.1 |  |  | O |  |  |
| 4 |  |  | Track Changed Characteristic |  |  | [1] 4.6.1 |  |  | O |  |  |
| 5 |  |  | Track Title Characteristic |  |  | [1] 4.5.3 |  |  | O |  |  |
| 6 |  |  | Track Duration Characteristic |  |  | [1] 4.5.4 |  |  | O |  |  |
| 7 |  |  | Track Position Characteristic |  |  | [1] 4.5.5 |  |  | O |  |  |
| 8 |  |  | Playback Speed Characteristic |  |  | [1] 4.5.8 |  |  | O |  |  |
| 9 |  |  | Seeking Speed Characteristic |  |  | [1] 4.5.10 |  |  | O |  |  |
| 10 |  |  | Current Track Segments Object ID Characteristic |  |  | [1] 4.5.11 |  |  | O |  |  |
| 11 |  |  | Current Track Object ID Characteristic |  |  | [1] 4.5.12 |  |  | O |  |  |
| 12 |  |  | Next Track Object ID Characteristic |  |  | [1] 4.5.14 |  |  | O |  |  |
| 13 |  |  | Parent Group Object ID Characteristic |  |  | [1] 4.5.18 |  |  | O |  |  |
| 14 |  |  | Current Group Object ID Characteristic |  |  | [1] 4.5.17 |  |  | O |  |  |
| 15 |  |  | Playing Order Characteristic |  |  | [1] 4.5.19 |  |  | O |  |  |
| 16 |  |  | Playing Order Supported Characteristic |  |  | [1] 4.5.21 |  |  | O |  |  |
| 17 |  |  | Media State Characteristic |  |  | [1] 4.5.22 |  |  | O |  |  |
| 18 |  |  | Media Control Point Characteristic |  |  | [1] 4.5 |  |  | O |  |  |
| 19 |  |  | Media Control Point Opcodes Supported Characteristic |  |  | [1] 4.5.42 |  |  | O |  |  |
| 20 |  |  | Search Results Object ID Characteristic |  |  | [1] 4.5.43 |  |  | O |  |  |
| 21 |  |  | Search Control Point Characteristic |  |  | [1] 4.5.43 |  |  | C.1 |  |  |
| 22 |  |  | Content Control ID Characteristic |  |  | [1] 4.5.44 |  |  | O |  |  |

Table 15: Media Control Point Procedure Requirements
Prerequisite: MCP 14/18 “Media Control Point Characteristic”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Play Current Track Procedure |  |  | [1] 4.5.22 |  |  | O |  |  |
| 2 |  |  | Pause Current Track Procedure |  |  | [1] 4.5.23 |  |  | O |  |  |
| 3 |  |  | Fast Forward Fast Rewind Procedure |  |  | [1] 4.5.24 |  |  | O |  |  |
| 4 |  |  | Stop Current Track Procedure |  |  | [1] 4.5.25 |  |  | O |  |  |
| 5 |  |  | Move Relative Procedure |  |  | [1] 4.5.7 |  |  | O |  |  |
| 6 |  |  | Move to Previous Segment Procedure |  |  | [1] 4.5.26 |  |  | O |  |  |
| 7 |  |  | Move to Next Segment Procedure |  |  | [1] 4.5.27 |  |  | O |  |  |
| 8 |  |  | Move to First Segment Procedure |  |  | [1] 4.5.28 |  |  | O |  |  |
| 9 |  |  | Move to Last Segment Procedure |  |  | [1] 4.5.29 |  |  | O |  |  |
| 10 |  |  | Move to Segment Number Procedure |  |  | [1] 4.5.30 |  |  | O |  |  |
| 11 |  |  | Move to Previous Track Procedure |  |  | [1] 4.5.31 |  |  | O |  |  |
| 12 |  |  | Move to Next Track Procedure |  |  | [1] 4.5.32 |  |  | O |  |  |
| 13 |  |  | Move to First Track Procedure |  |  | [1] 4.5.33 |  |  | O |  |  |
| 14 |  |  | Move to Last Track Procedure |  |  | [1] 4.5.34 |  |  | O |  |  |
| 15 |  |  | Move to Track Number Procedure |  |  | [1] 4.5.35 |  |  | O |  |  |
| 16 |  |  | Move to Previous Group Procedure |  |  | [1] 4.5.36 |  |  | O |  |  |
| 17 |  |  | Move to Next Group Procedure |  |  | [1] 4.5.37 |  |  | O |  |  |
| 18 |  |  | Move to First Group Procedure |  |  | [1] 4.5.38 |  |  | O |  |  |
| 19 |  |  | Move to Last Group Procedure |  |  | [1] 4.5.39 |  |  | O |  |  |
| 20 |  |  | Move to Group Number Procedure |  |  | [1] 4.5.40 |  |  | O |  |  |


##### 2.4.2.2 Generic Media Control Service

Table 16: Generic Media Control Service Characteristic Support Requirements
Prerequisite: MCP 13/2 “Discover Generic Media Control Service”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Media Player Name Characteristic |  |  | [1] 4.5.1 |  |  | M |  |  |
| 2 |  |  | Media Player Icon Object ID Characteristic |  |  | [1] 4.5.1 |  |  | O |  |  |
| 3 |  |  | Media Player Icon URL Characteristic |  |  | [1] 4.5.1 |  |  | O |  |  |
| 4 |  |  | Track Changed Characteristic |  |  | [1] 4.6.1 |  |  | O |  |  |
| 5 |  |  | Track Title Characteristic |  |  | [1] 4.5.3 |  |  | O |  |  |
| 6 |  |  | Track Duration Characteristic |  |  | [1] 4.5.4 |  |  | O |  |  |
| 7 |  |  | Track Position Characteristic |  |  | [1] 4.5.5 |  |  | O |  |  |
| 8 |  |  | Playback Speed Characteristic |  |  | [1] 4.5.8 |  |  | O |  |  |
| 9 |  |  | Seeking Speed Characteristic |  |  | [1] 4.5.10 |  |  | O |  |  |
| 10 |  |  | Current Track Segments Object ID Characteristic |  |  | [1] 4.5.11 |  |  | O |  |  |
| 11 |  |  | Current Track Object ID Characteristic |  |  | [1] 4.5.12 |  |  | O |  |  |


|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | Next Track Object ID Characteristic |  |  | [1] 4.5.14 |  |  | O |  |  |
| 13 |  |  | Parent Group Object ID Characteristic |  |  | [1] 4.5.18 |  |  | O |  |  |
| 14 |  |  | Current Group Object ID Characteristic |  |  | [1] 4.5.17 |  |  | O |  |  |
| 15 |  |  | Playing Order Characteristic |  |  | [1] 4.5.19 |  |  | O |  |  |
| 16 |  |  | Playing Order Supported Characteristic |  |  | [1] 4.5.21 |  |  | O |  |  |
| 17 |  |  | Media State Characteristic |  |  | [1] 4.5.22 |  |  | O |  |  |
| 18 |  |  | Media Control Point Characteristic |  |  | [1] 4.5 |  |  | O |  |  |
| 19 |  |  | Media Control Opcodes Supported Characteristic |  |  | [1] 4.5.42 |  |  | O |  |  |
| 20 |  |  | Search Results Object ID Characteristic |  |  | [1] 4.5.43 |  |  | O |  |  |
| 21 |  |  | Search Control Point Characteristic |  |  | [1] 4.5.43 |  |  | C.1 |  |  |
| 22 |  |  | Content Control ID Characteristic |  |  | [1] 4.5.44 |  |  | O |  |  |

C.1: Mandatory IF MCP 16/20 “Search Results Object ID Characteristic”, otherwise Excluded.
Table 17: Media Control Point Procedure Requirements
Prerequisite: MCP 16/18 “Media Control Point Characteristic”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Play Current Track Procedure |  |  | [1] 4.5.22 |  |  | O |  |  |
| 2 |  |  | Pause Current Track Procedure |  |  | [1] 4.5.23 |  |  | O |  |  |
| 3 |  |  | Fast Forward Fast Rewind Procedure |  |  | [1] 4.5.24 |  |  | O |  |  |
| 4 |  |  | Stop Current Track Procedure |  |  | [1] 4.5.25 |  |  | O |  |  |
| 5 |  |  | Move Relative Procedure |  |  | [1] 4.5.7 |  |  | O |  |  |
| 6 |  |  | Move to Previous Segment Procedure |  |  | [1] 4.5.26 |  |  | O |  |  |
| 7 |  |  | Move to Next Segment Procedure |  |  | [1] 4.5.27 |  |  | O |  |  |
| 8 |  |  | Move to First Segment Procedure |  |  | [1] 4.5.28 |  |  | O |  |  |
| 9 |  |  | Move to Last Segment Procedure |  |  | [1] 4.5.29 |  |  | O |  |  |
| 10 |  |  | Move to Segment Number Procedure |  |  | [1] 4.5.30 |  |  | O |  |  |
| 11 |  |  | Move to Previous Track Procedure |  |  | [1] 4.5.31 |  |  | O |  |  |
| 12 |  |  | Move to Next Track Procedure |  |  | [1] 4.5.32 |  |  | O |  |  |
| 13 |  |  | Move to First Track Procedure |  |  | [1] 4.5.33 |  |  | O |  |  |
| 14 |  |  | Move to Last Track Procedure |  |  | [1] 4.5.34 |  |  | O |  |  |
| 15 |  |  | Move to Track Number Procedure |  |  | [1] 4.5.35 |  |  | O |  |  |
| 16 |  |  | Move to Previous Group Procedure |  |  | [1] 4.5.36 |  |  | O |  |  |
| 17 |  |  | Move to Next Group Procedure |  |  | [1] 4.5.37 |  |  | O |  |  |
| 18 |  |  | Move to First Group Procedure |  |  | [1] 4.5.38 |  |  | O |  |  |
| 19 |  |  | Move to Last Group Procedure |  |  | [1] 4.5.39 |  |  | O |  |  |
| 20 |  |  | Move to Group Number Procedure |  |  | [1] 4.5.40 |  |  | O |  |  |


#### 2.4.3 GAP requirements

Table 18: GAP Requirements (Media Control Client)
Prerequisite: MCP 1/2 “Media Control Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | No longer used | N/A | N/A | N/A |  |  |
| 2 | LE security mode 1 | [1] 5.1 | C.1 | [2] GAP 25/1 OR GAP 35/1 |  |  |
| 3 | Bondable mode (LE) | [1] 6.2 | C.1 | [2] GAP 24/2 OR GAP 34/2 |  |  |
| 4 | Bonding procedure | [1] 6.2 | C.1 | [2] GAP 24/3 OR GAP 34/3 |  |  |
| 5 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 5.1 | O | [2] GAP 25/11 OR GAP 35/11 |  |  |
| 6 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 5.1 | O | [2] GAP 25/12 OR GAP 35/12 |  |  |
| 7 | LE security mode 1 level 4 | [1] 5.1 | O | [2] GAP 25/9 OR GAP 35/9 |  |  |
| 8 | Minimum 128 Bit entropy key (LE) | [1] 5.1 | C.5 | [2] GAP 25/13 OR GAP 35/13 |  |  |
| 9 | Derivation of LE LTK from BR/EDR Link Key | [1] 5.1 | C.6 | [2] GAP 43/2b OR GAP 41/2b |  |  |
| 10 | Security mode 4, level 2 | [1] 5.2 | C.2 | [2] GAP 2/7c |  |  |
| 11 | 128-bit encryption key size capable (BR/EDR) | [1] 5.2 | C.2 | [2] GAP 2/13 |  |  |
| 12 | Derivation of BR/EDR Link Key from LE LTK | [1] 5.2 | C.7 | [2] GAP 43/2a OR GAP 41/2a |  |  |
| 13 | BR/EDR Secure Connections | [1] 5.2 | C.7 | N/A |  |  |
| 14 | LE Secure Connections | [1] 5.1 | C.6 | [2] GAP 27b/5 OR GAP 37b/5 |  |  |
| 15 | Out of Band (LE) | [1] 5.1 | C.6 | [2] GAP 27b/9 OR GAP 37b/9 |  |  |
| 16 | Out-of-Band (BR/EDR) | [1] 5.2 | C.7 | [2] GAP 2/14 |  |  |

C.1: Mandatory IF MCP 2/2 “Profile supported over LE”, otherwise not defined. C.2: Mandatory IF MCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.3–C.4: No longer used. C.5: Mandatory IF MCP 18/5 “Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only” OR MCP 18/6 “Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only”, otherwise not defined. C.6: Mandatory to support at least one IF MCP 2/2 “Profile supported over LE”, otherwise not defined. C.7: Mandatory to support at least one IF MCP 2/1 “Profile supported over BR/EDR”, otherwise not defined.

#### 2.4.4 GATT requirements

Table 18a: GATT Requirements
Prerequisite: MCP 1/2 “Media Control Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Client over BR/EDR | [1] 1.4 | C.1 | [8] GATT 1a/2 |  |  |
| 2 | GATT Client over LE | [1] 1.4 | C.2 | [8] GATT 1a/1 |  |  |
| 3 | Discover All Primary Services | [1] 4.1 | C.3 | [8] GATT 3/2 |  |  |
| 4 | Discover Primary Service by Service UUID | [1] 4.1 | C.3 | [8] GATT 3/3 |  |  |
| 5 | Find Included Services | [1] 4.1 | O | [8] GATT 3/4 |  |  |
| 6 | Discover All Characteristics of a Service | [1] 4.1 | C.4 | [8] GATT 3/5 |  |  |
| 7 | Discover Characteristics by UUID | [1] 4.1 | C.4 | [8] GATT 3/6 |  |  |
| 8 | Discover All Characteristic Descriptors | [1] 4.1 | M | [8] GATT 3/7 |  |  |
| 9 | Single Notification | [1] 4.1 | M | [8] GATT 3/17 |  |  |
| 10 | Read Characteristic Value | [1] 4.1 | M | [8] GATT 3/8 |  |  |
| 11 | Write Characteristic Value | [1] 4.1 | C.5 | [8] GATT 3/14 |  |  |
| 12 | Write Without Response | [1] 4.1 | C.5 | [8] GATT 3/12 |  |  |
| 13 | Read Characteristic Descriptor | [1] 4.1 | M | [8] GATT 3/19 |  |  |
| 14 | Write Characteristic Descriptor | [1] 4.1 | M | [8] GATT 3/21 |  |  |

C.1: Mandatory IF MCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.2: Mandatory IF MCP 2/2 “Profile supported over LE”, otherwise not defined. C.3: Mandatory to support at least one. C.4: Mandatory to support at least one. C.5: Mandatory to support at least one.
Table 19: No longer used

#### 2.4.5 OTP requirements

Table 20: OTP Requirements (Media Control Client)
Prerequisite: MCP 13/3 “Discover Object Transfer Service”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Object Client | [1] 3 | M | [7] OTP 2/2 |  |  |

Prerequisite: MCP 13/3 “Discover Object Transfer Service”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Object Discovery – Discover All Objects | [1] 3 | M | [7] OTP 8/2 |  |  |
| 2 | Select Object – Select by Object ID | [1] 3 | M | [7] OTP 8/17 |  |  |
| 3 | Read Object – Read Object Contents | [1] 3 | M | [7] OTP 8/19 |  |  |


## 3 References

[1] Media Control Profile Specification, Version 1.0 or later
[2] ICS Proforma for Generic Access Profile (GAP)
[3] Object Transfer Service Specification, Version 1.0 or later
[4] ICS Proforma for Object Transfer Service (OTS)
[5] ICS Proforma for Media Control Service (MCS)
[6] ICS Proforma for Link Layer (LL)
[7] ICS Proforma for Object Transfer Profile (OTP)
[8] ICS Proforma for Generic Attribute Profile (GATT)

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2021-03-16 | Approved by BTI on 2021-02-25. MCP v1.0 adopted by the BoD on 2021-03-09. Prepared for publication. |
|  |  |  | p1r00–r02 |  |  | 2021-04-19 – 2021-05-30 | TSE 16754 (rating 1): Updated the inter-layer dependencies in GAP Tables 6 and 18. Removed item 18/1. Consistency checker fixes. |
| 1 |  |  | p1 |  |  | 2021-07-13 | Approved by BTI on 2021-06-01. Prepared for TCRL 2021-1 publication. |
|  |  |  | p1ed2r00 |  |  | 2022-01-25 | TSE 18188 (rating 1): Updated Link Layer inter-layer dependency item in Table 5 to align with updates made in the LL ICS. Made template-related fixes, including aligning the copyright page with v2 of the DNMD. |
|  |  |  | p1 edition 2 |  |  | 2022-01-27 | Approved by BTI on 2022-01-27. Prepared for edition 2 publication. |
|  |  |  | p1ed3r00 |  |  | 2023-02-15 | TSE 22635 (rating 1): Replaced ILD references to Security Manager 8/1 with SM 8a/1 (for Central role) or SM 8b/1 (for Peripheral role) in Tables 7 and 19. Updated references. Editorials to align the document with the latest ICS template. |
|  |  |  | p1 edition 3 |  |  | 2023-03-15 | Approved by BTI on 2023-03-13. Prepared for edition 3 publication. |
|  |  |  | p2r00–r03 |  |  | 2023-10-04 – 2024-01-08 | TSE 23341 (rating 2): To resolve GAP/SM ILDs: Removed the SM ICS item from the References section and updated cross-refs throughout the doc. Updated “or” to “OR” in ILDs throughout the doc. In Table 6, added items 6/12–6/15 and updated conditionals and statuses accordingly. Removed SM requirements heading and deleted Table 7. Updated service names of 13/1–13/3 and related prerequisites for Tables 14, 16, 20, and 21. In Table 18, added items 18/13–18/16 and updated conditionals and statuses accordingly. Removed SM requirements heading and deleted Table 19. TSE 24103 (rating 1): Removed GMCS ICS from the References section. Updated MCS and GMCS ILDs in Table 5. TSE 24772 (rating 2): Added OTP ILDs to 8/1, 20/1, and 21/1–21/3. Template-related editorials, including removing the draft entries from the rev history. |
| 2 |  |  | p2 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p3r00–r02 |  |  | 2025-02-19 – 2025-05-15 | TSE 26836 (rating 2): Added Table 18a. Updated the References section. Applied the current ICS template. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 27375 (rating 1): Updated the Status value for MCP 2/1 and MCP 2/2. Added conditionals C.1 and C.2 to Table 2 and renumbered C.1 as C.3. Modified the heading for the Roles section and added a section heading for Transports. Incorporated editorials to align the document with the latest ICS template, including updates to Section 1 and the addition of a section heading for the ICS declarations section. |
| 3 |  |  | p3 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p4r00–r01 |  |  | 2025-12-07 – 2026-01-14 | TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 4 |  |  | p4 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Jim Harper |  |  | Bluetooth SIG, Inc. |  |  |
| Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
