# HAP.ICS.p6

> Source: PDF converted via PyMuPDF.

---

Hearing Access Profile (HAP) (HAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: HAP.ICS.p6 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Hearing Aid Working Group ▪ Published during TCRL: TCRL.pkg102
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
| 1 |  |  | Hearing Aid (HA) |  |  | [1] 3 |  |  | C.1 |  |  |
| 2 |  |  | Hearing Aid Unicast Client (HAUC) |  |  | [1] 4 |  |  | C.1 |  |  |
| 3 |  |  | Hearing Aid Remote Controller (HARC) |  |  | [1] 5 |  |  | C.1 |  |  |
| 4 |  |  | Immediate Alert Client (IAC) |  |  | [1] 6 |  |  | C.2 |  |  |

C.1: Mandatory to support at least one. C.2: Optional IF HAP 1/2 “Hearing Aid Unicast Client (HAUC)” OR HAP 1/3 “Hearing Aid Remote Controller (HARC)”, otherwise Excluded.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.5 |  |  | C.1 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.5 |  |  | C.2, C.3 |  |  |

C.1: Excluded for this Profile. C.2: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core- Controller”. C.3: Mandatory for this Profile.

### 2.3 Hearing Aid role


#### 2.3.1 Versions

Table 10: Hearing Aid, X.Y Versions
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0 |  |  | [1] |  |  | M |  |  |

Table 11: Hearing Aid, X.Y.Z Versions
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0.1 |  |  | [14] |  |  | O |  |  |


#### 2.3.2 Features

Table 12: Hearing Aid, Features
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Volume Balance |  |  | [1] 3.1 |  |  | O |  |  |
| 2 |  |  | Binaural Hearing Aid Set |  |  | [1] 3.1 |  |  | C.1 |  |  |
| 3 |  |  | Banded Hearing Aid |  |  | [1] 3.5 |  |  | C.1 |  |  |
| 4 |  |  | Monaural Hearing Aid |  |  | [1] 3.5 |  |  | C.1 |  |  |
| 5 |  |  | Connected Isochronous Stream |  |  | [1] 3.2 |  |  | M |  |  |
| 6 |  |  | Broadcast Isochronous Stream |  |  | [1] 3.2 |  |  | M |  |  |
| 7 |  |  | 7.5 ms Transport Interval |  |  | [1] 3.2 |  |  | O |  |  |

C.1: Mandatory to support at least one.

#### 2.3.3 Profile and service dependencies

Table 13: Hearing Aid, Profile Dependencies
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Call Control Client (CCP) | [1] 2.2 | O | [9] CCP 1/2 |  |  |
| 2 | Volume Renderer (VCP) | [1] 2.2 | M | [5] VCP 1/1 |  |  |
| 3 | Microphone Device (MICP) | [1] 2.2 | C.1 | [6] MICP 1/1 |  |  |
| 4 | Set Member (CSIP) | [1] 2.2 | C.2 | [7] CSIP 1/1 |  |  |
| 5 | Unicast Server (BAP) | [1] 2.2 | M | [10] BAP 1/1 |  |  |
| 6 | Acceptor (CAP) | [1] 2.2 | M | [11] CAP 1/1 |  |  |
| 7 | Broadcast Sink (BAP) | [1] 2.2 | M | [10] BAP 1/4 |  |  |

C.1: Mandatory IF HAP 19/2 “Audio Source”, otherwise not defined. C.2: Mandatory IF HAP 12/2 “Binaural Hearing Aid Set”, otherwise not defined.
Table 14: Hearing Aid, Service Dependencies
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Hearing Access Service (HAS) | [1] 3.5.1 | M | [12] HAS |  |  |
| 2 | Immediate Alert Service (IAS) | [1] 3.5.3 | O | [13] IAS |  |  |
| 3 | Coordinated Set Identification Service (CSIS) | [1] 3.6 | C.1 | [8] CSIS |  |  |

C.1: Mandatory IF HAP 12/2 “Binaural Hearing Aid Set”, otherwise not defined.

#### 2.3.4 Feature requirements in dependent services


##### 2.3.4.1 CCP Client requirements

Table 15: Hearing Aid, CCP Client Requirements
Table number reserved but not yet in use

##### 2.3.4.2 VCP Volume Renderer requirements

Table 16: Hearing Aid, VCP Volume Renderer Requirements
Prerequisite: HAP 13/2 “Volume Renderer (VCP)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Volume Offset Control Service | [1] 3.8 | C.1 | [5] VCP 5/2 |  |  |
| 2 | Audio Input Control Service | [1] 3.8 | O | [5] VCP 5/3 |  |  |

C.1: Mandatory IF HAP 12/1 “Volume Balance”, otherwise not defined.

##### 2.3.4.3 MICP Microphone Device requirements

Table 17: Hearing Access, MICP Microphone Device Requirements
Prerequisite: HAP 13/3 “Microphone Device (MICP)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Microphone Control Service | [1] 3.9 | M | [5] MICP 5/1 |  |  |


##### 2.3.4.4 CSIP Set Member requirements

Table 18: Hearing Aid, CSIP Set Member Requirements
Prerequisite: HAP 13/4 “Set Member (CSIP)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Coordinated Set Size Characteristic | [1] 3.6 | M | [8] CSIS 2/2 |  |  |


##### 2.3.4.5 BAP Unicast Server requirements

Table 19: Hearing Aid, BAP Unicast Server Requirements
Prerequisite: HAP 13/5 “Unicast Server (BAP)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Audio Sink | [1] 3.7 | M | [10] BAP 8/1 |  |  |
| 2 | Audio Source | [1] 3.7 | O | [10] BAP 8/2 |  |  |

Table 20: Hearing Aid, CAP Acceptor Requirements
Table number reserved but not yet in use

##### 2.3.4.7 Hearing Access Service requirements

Table 21: Hearing Aid, Hearing Access Service Requirements
Table number reserved but not yet in use

##### 2.3.4.8 Immediate Alert Service requirements

Table 22: Hearing Access, Immediate Alert Service Requirements
Table number reserved but not yet in use

##### 2.3.4.9 Coordinated Set Identification Service requirements

Table 23: Hearing Access, Coordinated Set Identification Service Requirements
Table number reserved but not yet in use

#### 2.3.5 Feature requirements in Core layers


##### 2.3.5.1 GAP requirements

Table 24: Hearing Aid, GAP Requirements
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 9.1 | M | [4] GAP 25/11 |  |  |
| 2 | Minimum 128-bit entropy key | [1] 9.1 | M | [4] GAP 25/13 |  |  |
| 3 | Service UUID | [1] 3.3 | O | [4] GAP 20a/1 |  |  |
| 4 | Appearance | [1] 3.4 | O | [4] GAP 20a/11 |  |  |
| 5 | Resolvable private address generation procedure | [1] 3.4 | O | [4] GAP 26/3 |  |  |
| 6 | LE Secure Connections | [1] 9.1 | M | [4] GAP 27b/5 |  |  |

Table 25: No longer used
Table 26: Hearing Aid, LL Requirements
Prerequisite: HAP 1/1 “Hearing Aid (HA)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE 2M PHY | [1] 3.2 | M | [3] LL 9/7 |  |  |


### 2.4 Hearing Aid Unicast Client role


#### 2.4.1 Versions

Table 40: Hearing Aid Unicast Client, X.Y Versions
Prerequisite: HAP 1/2 “Hearing Aid Unicast Client (HAUC)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0 |  |  | [1] |  |  | M |  |  |

Table 41: Hearing Aid Unicast Client, X.Y.Z Versions
Prerequisite: HAP 1/2 “Hearing Aid Unicast Client (HAUC)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0.1 |  |  | [14] |  |  | O |  |  |


#### 2.4.2 Features

Table 42: Hearing Aid Unicast Client, Features
Table number reserved but not yet in use

#### 2.4.3 Profile and service dependencies

Table 43: Hearing Aid Unicast Client, Profile Dependencies
Prerequisite: HAP 1/2 “Hearing Aid Unicast Client (HAUC)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Call Control Server (CCP) | [1] 2.2 | O | [9] CCP 1/1 |  |  |
| 2 | Set Coordinator (CSIP) | [1] 2.2 | M | [7] CSIP 1/2 |  |  |
| 3 | Unicast Client (BAP) | [1] 2.2 | M | [10] BAP 1/2 |  |  |
| 4 | Initiator (CAP) | [1] 2.2 | M | [11] CAP 1/2 |  |  |


#### 2.4.4 Feature requirements in dependent profiles and services


##### 2.4.4.1 CCP Server requirements

Table 44: Hearing Aid Unicast Client, CCP Server Requirements
Table number reserved but not yet in use

##### 2.4.4.2 CSIP Set Coordinator requirements

Table 45: Hearing Aid Unicast Client, CCP Server Requirements
Table number reserved but not yet in use

##### 2.4.4.3 BAP Unicast Client requirements

Table 46: Hearing Aid Unicast Client, BAP Unicast Client Requirements
Prerequisite: HAP 43/3 “Unicast Client (BAP)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Audio Source | [1] 5.3 | M | [10] BAP 29/2 |  |  |
| 2 | Audio Sink | [1] 5.3 | C.1 | [10] BAP 29/1 |  |  |

C.1: Mandatory IF HAP 43/1 “Call Control Server (CCP)”, otherwise not defined.
Tables 47 – 48: No longer used

##### 2.4.4.4 CAP Initiator

Table 49: Hearing Aid Unicast Client, CCP Server Requirements
Table number reserved but not yet in use

#### 2.4.5 Feature requirements in Core layers


##### 2.4.5.1 GATT requirements

Table 50: GATT Requirements – Hearing Aid Unicast Client Role
Prerequisite: HAP 1/2 “Hearing Aid Unicast Client (HAUC)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Discover All Primary Services | [1] 4.2 | C.1 | [2] GATT 3/2 |  |  |
| 2 | Discover Primary Service by Service UUID | [1] 4.2 | C.1 | [2] GATT 3/3 |  |  |
| 3 | GATT Client over LE | [1] 4.2 | M | [10] GATT 1a/1 |  |  |

C.1: Mandatory to support at least one.
Table 51: Hearing Aid Unicast Client, LL Requirements
Prerequisite: HAP 1/2 “Hearing Aid Unicast Client (HAUC)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE 2M PHY | [1] 5.1 | M | [3] LL 9/7 |  |  |


### 2.5 Hearing Aid Remote Controller role


#### 2.5.1 Versions

Table 70: Hearing Aid Remote Controller, X.Y Versions
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0 |  |  | [1] |  |  | M |  |  |

Table 71: Hearing Aid Remote Controller, X.Y.Z Versions
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0.1 |  |  | [14] |  |  | O |  |  |


#### 2.5.2 Features


##### 2.5.2.1 Characteristic Discovery requirements

Table 72: Hearing Aid Remote Controller, Characteristic Discovery Requirements
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Active Preset Index Characteristic |  |  | [1] 5.6 |  |  | O |  |  |
| 2 |  |  | Hearing Aid Preset Control Point Characteristic |  |  | [1] 5.5 |  |  | C.1 |  |  |
| 3 |  |  | Hearing Aid Features Characteristic |  |  | [1] 5.4 |  |  | C.2 |  |  |
| 4 |  |  | Hearing Aid Features Characteristic, Notifications |  |  | [1] 5.4 |  |  | C.3 |  |  |

C.1: Mandatory IF HAP 72/1 “Active Preset Index Characteristic”, otherwise Optional. C.2: Mandatory IF HAP 72/2 “Hearing Aid Preset Control Point Characteristic”, otherwise Excluded. C.3: Optional IF HAP 72/3 “Hearing Aid Features Characteristic”, otherwise Excluded.
Table 73: Hearing Aid Remote Controller, Preset Control Point Requirements
Prerequisite: HAP 72/2 “Hearing Aid Preset Control Point Characteristic”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Write Preset Name Procedure |  |  | [1] 5.5.4 |  |  | O |  |  |
| 2 |  |  | Set Active Preset Procedure |  |  | [1] 5.5.5 |  |  | C.3 |  |  |
| 3 |  |  | Set Next Preset Procedure |  |  | [1] 5.5.6 |  |  | C.3 |  |  |
| 4 |  |  | Set Previous Preset Procedure |  |  | [1] 5.5.7 |  |  | C.3 |  |  |
| 5 |  |  | Set Active Preset – Synchronized Locally Procedure |  |  | [1] 5.5.8 |  |  | C.4 |  |  |
| 6 |  |  | Set Next Preset – Synchronized Locally Procedure |  |  | [1] 5.5.9 |  |  | C.5 |  |  |
| 7 |  |  | Set Previous Preset – Synchronized Locally Procedure |  |  | [1] 5.5.10 |  |  | C.6 |  |  |
| 8 |  |  | Read Preset by Index Procedure |  |  | [1] 5.5.2 |  |  | C.2 |  |  |
| 9 |  |  | Preset Changed Procedure |  |  | [1] 5.5.3 |  |  | C.1 |  |  |

C.1: Mandatory IF HAP 73/1 “Write Preset Name Procedure” OR HAP 73/2 “Set Active Preset Procedure”, otherwise Optional. C.2: Mandatory IF HAP 72/1 “Active Preset Index Characteristic”, otherwise Optional. C.3: Mandatory to support at least one. C.4: Mandatory IF HAP 73/2 “Set Active Preset Procedure”, otherwise Excluded. C.5: Mandatory IF HAP 73/3 “Set Next Preset Procedure”, otherwise Excluded. C.6: Mandatory IF HAP 73/4 “Set Previous Preset Procedure”, otherwise Excluded.

#### 2.5.3 Profile and service dependencies

Table 74: Hearing Aid Remote Controller, Profile Dependencies
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Volume Controller (VCP) | [1] 2.2 | M | [5] VCP 1/2 |  |  |
| 2 | Microphone Controller (MICP) | [1] 2.2 | O | [6] MICP 1/2 |  |  |
| 3 | Set Coordinator (CSIP) | [1] 2.2 | M | [7] CSIP 1/2 |  |  |
| 4 | Commander (CAP) | [1] 2.2 | M | [11] CAP 1/3 |  |  |

Table 75: Hearing Aid Remote Controller, Service Dependencies
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Hearing Access Service Client (HAS) | [1] 2.2 | M | N/A |  |  |


#### 2.5.4 Feature requirements in dependent profiles and services


##### 2.5.4.1 VCP Volume Controller requirements

Table 76: Hearing Aid Remote Controller, VCP Volume Controller Requirements
Prerequisite: HAP 74/1 “Volume Controller (VCP)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set Absolute Volume | [1] 6.5 | M | [5] VCP 12/6 |  |  |


##### 2.5.4.2 MICP Microphone Controller requirements

Table 77: Hearing Aid Remote Controller, MICP Microphone Controller Requirements
Table number reserved but not yet in use

##### 2.5.4.3 CSIP Set Coordinator requirements

Table 78: Hearing Aid Remote Controller, CSIP Set Coordinator Requirements
Table number reserved but not yet in use

##### 2.5.4.4 CAP Commander requirements

Table 79: Hearing Aid Remote Controller, CAP Commander Requirements
Table number reserved but not yet in use

##### 2.5.4.5 HAS Hearing Access Service Client requirements

Table 80: Hearing Aid Remote Controller, HAS Hearing Access Service Client Requirements
Table number reserved but not yet in use

#### 2.5.5 Feature requirements in Core layers


##### 2.5.5.1 Link Layer requirements

Table 81: Hearing Aid Remote Controller, LL Requirements
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE 2M PHY | [1] 3.2 | M | [3] LL 9/7 |  |  |

Table 82: GAP Requirements – Immediate Alert Client Role
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Bondable mode (LE) | [1] 9.4 | M | [4] GAP 34/2 |  |  |


##### 2.5.5.3 GATT requirements

Table 83: GATT Requirements – Immediate Alert Client Role
Prerequisite: HAP 1/3 “Hearing Aid Remote Controller (HARC)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Enhanced ATT bearer over LE | [1] 5.5 | O | [2] GATT 2/3a |  |  |
| 2 | GATT Client over LE | [1] 5.2 | M | [2] GATT 1a/1 |  |  |


### 2.6 Immediate Alert Client role


#### 2.6.1 Versions

Table 90: Immediate Alert Client, X.Y Versions
Prerequisite: HAP 1/4 “Immediate Alert Client (IAC)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0 |  |  | [1] |  |  | M |  |  |

Table 91: Immediate Alert Client, X.Y.Z Versions
Prerequisite: HAP 1/4 “Immediate Alert Client (IAC)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HAP v1.0.1 |  |  | [14] |  |  | O |  |  |


#### 2.6.2 Service dependencies

Table 92: Immediate Alert Client, Service Dependencies
Prerequisite: HAP 1/4 “Immediate Alert Client (IAC)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Immediate Alert Service (IAS) | [1] 6.1 | M | [13] IAS |  |  |


#### 2.6.3 Feature requirements in Core layers


##### 2.6.3.1 GATT requirements

Table 93: GATT Requirements – Immediate Alert Client Role
Prerequisite: HAP 1/4 “Immediate Alert Client (IAC)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Client over LE | [1] 6.1 | M | [2] GATT 1a/1 |  |  |
| 2 | Discover All Primary Services | [1] 6.1 | C.1 | [2] GATT 3/2 |  |  |
| 3 | Discover Primary Service by Service UUID | [1] 6.1 | C.1 | [2] GATT 3/3 |  |  |
| 4 | Discover All Characteristics of a Service | [1] 6.2 | C.2 | [2] GATT 3/5 |  |  |
| 5 | Discover Characteristics by UUID | [1] 6.2 | C.2 | [2] GATT 3/6 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one.

## 3 References

[1] Hearing Access Profile, Version 1.0 or later
[2] ICS Proforma for Generic Attribute Profile (GATT)
[3] ICS Proforma for Bluetooth Low Energy Link Layer Protocol Specification
[4] ICS Proforma for Generic Access Profile (GAP)
[5] ICS Proforma for Volume Control Profile (VCP)
[6] ICS Proforma for Microphone Control Profile (MICP)
[7] ICS Proforma for Coordinated Set Identification Profile (CSIP)
[8] ICS Proforma for Coordinated Set Identification Service (CSIS)
[9] ICS Proforma for Call Control Profile (CCP)
[10] ICS Proforma for Basic Audio Profile (BAP)
[11] ICS Proforma for Common Audio Profile (CAP)
[12] ICS Proforma for Hearing Access Service (HAS)
[13] ICS Proforma for Immediate Alert Service (IAS)
[14] Hearing Access Profile, Version 1.0.1

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2022-06-14 | HAP v1.0 adopted by the BoD on 2022-06-07. Prepared for initial publication. |
|  |  |  | p1r00–r01 |  |  | 2022-07-28 – 2022-11-21 | TSE 19154 (rating 2): Updated Status for 1/1 and updated C.1 and C.2 for Table 1. Consistency checker editorials. |
| 1 |  |  | p1 |  |  | 2023-02-07 | Approved by BTI on 2022-12-19. Prepared for TCRL 2022-2 publication. |
|  |  |  | p2r00–r03 |  |  | 2023-08-25 – 2024-04-11 | TSE 23342 (rating 2): To resolve GAP/SM ILDs, removed the SM ICS from the References section and deleted the SM Requirements table (Table 25). Added 24/6. Other changes throughout to align with the latest ICS template conventions. TSE 25097 (rating 2): Added new Table 83 “GATT Requirements – Immediate Alert Client Role” to account for GATT ILDs. Removed extra “Feature requirements in Core layers” subheading. |
| 2 |  |  | p2 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p3r00–r01 |  |  | 2024-08-09 – 2024-08-12 | TSE 25408 (rating 2): Per E19220, added item 7, Broadcast Sink (BAP) service, for Table 13. TSE 25567 (rating 1): Per E19220, E23132, and E23815, added new X.Y.Z version as part of the .Z release. Added Tables 11, 41, 71, and 91. Added a reference to Hearing Access Profile, Version 1.0.1. |
| 3 |  |  | p3 |  |  | 2024-10-08 | Approved by BTI on 2024-09-11. HAP v1.0.1 adopted by the BoD on 2024-10-01. Prepared for TCRL 2024- 2-addition publication. |
|  |  |  | p4r00–r01 |  |  | 2025-02-03 – 2025-02-18 | TSE 27125 (rating 2): For Table 2, added conditionals C.2 and C.3 and updated 2/2 Status value. Made an editorial update to 24/2 Capability value. Updated Reference values for 50/1 and 50/2 and added 50/3. Added 83/2. Added “Feature requirements in Core layers” section, “GATT requirements” subsection, and Table 93. |
| 4 |  |  | p4 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p5r00 |  |  | 2025-07-23 | TSE 27782 (rating 1): Removed Tables 47–48. |
| 5 |  |  | p5 |  |  | 2025-11-04 | Approved by BTI on 2025-09-29. Prepared for TCRL pkg101 publication. |
|  |  |  | p6r00–r01 |  |  | 2025-12-05 – 2026-01-14 | TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 6 |  |  | p6 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Dejan Berec |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
