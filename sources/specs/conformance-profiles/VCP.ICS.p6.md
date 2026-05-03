# VCP.ICS.p6

> Source: PDF converted via PyMuPDF.

---

Volume Control Profile (VCP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: VCP.ICS.p6 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Generic Audio Working Group ▪ Published during TCRL: TCRL.pkg102
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
| 1 |  |  | Volume Renderer |  |  | [1] 3.0 |  |  | C.1 |  |  |
| 2 |  |  | Volume Controller |  |  | [1] 4.0 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.4 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.4 |  |  | C.2, C.3 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”. C.2: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core- Controller”. C.3: Mandatory to support at least one.

### 2.3 Volume Renderer role

Table 3: X.Y Versions (Volume Renderer)
Prerequisite: VCP 1/1 “Volume Renderer”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | VCP v1.0 |  |  | [1] |  |  | M |  |  |

Table 4: X.Y.Z Versions (Volume Renderer)
Table number reserved but not yet in use

#### 2.3.1 Services (Volume Renderer)

Table 5: Service Requirements
Prerequisite: VCP 1/1 “Volume Renderer”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Volume Control Service | [1] 3.0 | M | [6] VCS |  |  |
| 2 | Volume Offset Control Service | [1] 3.0 | O | [4] VOCS |  |  |
| 3 | Audio Input Control Service | [1] 3.0 | O | [5] AICS |  |  |
| 4 | LE Extended Advertising | [1] 6.1.1.1 | M | [7] LL 9/41 |  |  |


#### 2.3.2 GAP requirements

Table 6: GAP Requirements (Volume Renderer)
Prerequisite: VCP 1/1 “Volume Renderer”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE security mode 1 | [1] 5.1 | C.1 | [3] GAP 25/1 |  |  |
| 2 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 5.1 | C.1 | [3] GAP 25/11 |  |  |
| 3 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 5.1 | C.3 | [3] GAP 25/12 |  |  |
| 4 | Derivation of LE LTK from BR/EDR Link Key | [1] 5.1 | C.6 | [3] GAP 43/2b |  |  |
| 5 | Security mode 4, level 2 | [1] 5.2 | C.2 | [3] GAP 2/7c |  |  |
| 6 | 128-bit encryption key size capable (BR/EDR) | [1] 5.2 | C.2 | [3] GAP 2/13 |  |  |
| 7 | Derivation of BR/EDR Link Key from LE LTK | [1] 5.2 | C.7 | [3] GAP 43/2a |  |  |
| 8 | Minimum 128 Bit entropy key (LE) | [1] 5.1 | C.1 | [3] GAP 25/13 |  |  |
| 9 | BR/EDR Secure Connections | [1] 5.2 | C.7 | N/A |  |  |
| 10 | LE Secure Connections (Peripheral) | [1] 5.1 | C.6 | [3] GAP 27b/5 |  |  |
| 11 | Out of Band (Peripheral) | [1] 5.1 | C.6 | [3] GAP 27b/9 |  |  |
| 12 | Out-of-Band (BR/EDR) | [1] 5.2 | C.7 | [3] GAP 2/14 |  |  |
| 13 | Peripheral | [1] 4.1 | C.1 | [3] GAP 5/3 |  |  |

C.1: Mandatory IF VCP 2/2 “Profile supported over LE”, otherwise not defined. C.2: Mandatory IF VCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.3: Optional IF VCP 2/2 “Profile supported over LE”, otherwise not defined. C.4–C.5: No longer used. C.6: Mandatory to support at least one IF VCP 2/2 “Profile supported over LE”, otherwise not defined. C.7: Mandatory to support at least one IF VCP 2/1 “Profile supported over BR/EDR”, otherwise not defined.

### 2.4 Volume Controller role

Table 8: X.Y Versions (Volume Controller)
Prerequisite: VCP 1/2 “Volume Controller”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | VCP v1.0 |  |  | [1] |  |  | M |  |  |

Table 9: X.Y.Z Versions (Volume Controller)
Table number reserved but not yet in use

#### 2.4.1 Services Support (Volume Controller)

Table 10: Volume Control Service Support
Prerequisite: VCP 1/2 “Volume Controller”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Discover Volume Control Service |  |  | [1] 4.0 |  |  | M |  |  |
| 2 |  |  | Discover Volume Offset Control Service |  |  | [1] 4.0 |  |  | O |  |  |
| 3 |  |  | Discover Audio Input Control Service |  |  | [1] 4.0 |  |  | O |  |  |

Table 11: Volume Control Service Characteristic Support Requirements
Prerequisite: VCP 10/1 “Discover Volume Control Service”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Volume State |  |  | [1] 4.3.1 |  |  | M |  |  |
| 2 |  |  | Volume Control Point |  |  | [1] 4.3.1 |  |  | M |  |  |
| 3 |  |  | Volume Flags |  |  | [1] 4.3.1 |  |  | O |  |  |

Table 12: Volume Control Service Procedure Support Requirements
Prerequisite: VCP 10/1 “Discover Volume Control Service”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Configure Volume State Notifications |  |  | [1] 4.4.1, 4.4.1.1 |  |  | M |  |  |
| 2 |  |  | Read Volume State |  |  | [1] 4.4.1, 4.4.1.2 |  |  | M |  |  |
| 3 |  |  | Configure Volume Flags Notifications |  |  | [1] 4.4.1, 4.4.1.3 |  |  | O |  |  |
| 4 |  |  | Read Volume Flags |  |  | [1] 4.4.1, 4.4.1.4 |  |  | O |  |  |
| 5 |  |  | Set Initial Volume |  |  | [1] 4.4.1, 4.4.1.5 |  |  | C.1 |  |  |
| 6 |  |  | Set Absolute Volume |  |  | [1] 4.4.1, 4.4.1.6.5 |  |  | C.2 |  |  |
| 7 |  |  | Relative Volume Down |  |  | [1] 4.4.1, 4.4.1.6.1 |  |  | C.3 |  |  |
| 8 |  |  | Relative Volume Up |  |  | [1] 4.4.1, 4.4.1.6.2 |  |  | C.3 |  |  |
| 9 |  |  | Unmute/ Relative Volume Down |  |  | [1] 4.4.1, 4.4.1.6.3 |  |  | C.4 |  |  |
| 10 |  |  | Unmute/ Relative Volume Up |  |  | [1] 4.4.1, 4.4.1.6.4 |  |  | C.4 |  |  |
| 11 |  |  | Mute |  |  | [1] 4.4.1, 4.4.1.6.6 |  |  | O |  |  |
| 12 |  |  | Unmute |  |  | [1] 4.4.1, 4.4.1.6.7 |  |  | O |  |  |

C.1: Optional IF VCP 12/4 “Read Volume Flags” OR VCP 12/6 “Set Absolute Volume”, otherwise Excluded. C.2: Mandatory IF NOT VCP 12/7 “Relative Volume Down” AND NOT VCP 12/8 “Relative Volume Up” AND NOT VCP 12/9 “Unmute/ Relative Volume Down” AND NOT VCP 12/10 “Unmute/ Relative Volume Up”, otherwise Optional. C.3: Mandatory to support none or all. C.4: Mandatory to support none or all.
Prerequisite: VCP 10/2 “Discover Volume Offset Control Service”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Volume Offset State |  |  | [1] 4.3.2 |  |  | C.1 |  |  |
| 2 |  |  | Audio Location |  |  | [1] 4.3.2 |  |  | O |  |  |
| 3 |  |  | Volume Offset Control Point |  |  | [1] 4.3.2 |  |  | O |  |  |
| 4 |  |  | Audio Output Description |  |  | [1] 4.3.2 |  |  | O |  |  |

C.1: Mandatory IF VCP 14/1 “Configure Offset State Notifications” OR VCP 14/2 “Read Volume Offset State” OR VCP 14/3 “Configure Audio Location Notifications” OR VCP 14/4 “Read Audio Location” OR VCP 14/5 “Set Audio Location” OR VCP 14/6 “Set Volume Offset” OR VCP 14/7 “Configure Audio Output Description Notifications” OR VCP 14/8 “Read Audio Output Description” OR VCP 14/9 “Set Audio Output Description”, otherwise Optional.
Table 14: Volume Offset Control Service Procedure Support Requirements
Prerequisite: VCP 10/2 “Discover Volume Offset Control Service”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Configure Offset State Notifications |  |  | [1] 4.4.2.1 |  |  | C.1, C.2 |  |  |
| 2 |  |  | Read Volume Offset State |  |  | [1] 4.4.2.2 |  |  | C.1, C.2 |  |  |
| 3 |  |  | Configure Audio Location Notifications |  |  | [1] 4.4.2.3 |  |  | O |  |  |
| 4 |  |  | Read Audio Location |  |  | [1] 4.4.2.4 |  |  | O |  |  |
| 5 |  |  | Set Audio Location |  |  | [1] 4.4.2.5 |  |  | O |  |  |
| 6 |  |  | Set Volume Offset |  |  | [1] 4.4.2.6.1 |  |  | O |  |  |
| 7 |  |  | Configure Audio Output Description Notifications |  |  | [1] 4.4.2.7 |  |  | O |  |  |
| 8 |  |  | Read Audio Output Description |  |  | [1] 4.4.2.8 |  |  | O |  |  |
| 9 |  |  | Set Audio Output Description |  |  | [1] 4.4.2.9 |  |  | O |  |  |

C.1: Mandatory IF VCP 14/3 “Configure Audio Location Notifications” OR VCP 14/4 “Read Audio Location” OR VCP 14/5 “Set Audio Location” OR VCP 14/6 “Set Volume Offset” OR VCP 14/7 “Configure Audio Output Description Notifications” OR VCP 14/8 “Read Audio Output Description” OR VCP 14/9 “Set Audio Output Description”, otherwise Optional. C.2: Mandatory to support none or all.
Table 15: Audio Input Control Service Characteristic Support Requirements
Prerequisite: VCP 10/3 “Discover Audio Input Control Service”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Audio Input State |  |  | [1] 4.3.3 |  |  | C.1 |  |  |
| 2 |  |  | Gain Setting Properties |  |  | [1] 4.3.3 |  |  | C.1 |  |  |
| 3 |  |  | Audio Input Type |  |  | [1] 4.3.3 |  |  | O |  |  |
| 4 |  |  | Audio Input Status |  |  | [1] 4.3.3 |  |  | O |  |  |
| 5 |  |  | Audio Input Control Point |  |  | [1] 4.3.3 |  |  | O |  |  |
| 6 |  |  | Audio Input Description |  |  | [1] 4.3.3 |  |  | O |  |  |

C.1: Mandatory IF VCP 16/1 “Configure Audio Input State Notifications” OR VCP 16/2 “Read Audio Input State” OR VCP 16/3 “Read Gain Setting Properties” OR VCP 16/4 “Read Audio Input Type”
OR VCP 16/5 “Configure Audio Input Status Notifications” OR VCP 16/6 “Read Audio Input Status” OR VCP 16/7 “Set Gain Setting” OR VCP 16/8 “Mute” OR VCP 16/9 “Unmute” OR VCP 16/10 “Set Manual Gain Mode” OR VCP 16/11 “Set Automatic Gain Mode” OR VCP 16/12 “Configure Audio Input Description Notifications” OR VCP 16/13 “Read Audio Input Description” OR VCP 16/14 “Set Audio Input Description”, otherwise Optional.
Table 16: Audio Input Control Service Procedure Support Requirements
Prerequisite: VCP 10/3 “Discover Audio Input Control Service”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Configure Audio Input State Notifications |  |  | [1] 4.4.3.1 |  |  | C.1, C.2 |  |  |
| 2 |  |  | Read Audio Input State |  |  | [1] 4.4.3.2 |  |  | C.1, C.2 |  |  |
| 3 |  |  | Read Gain Setting Properties |  |  | [1] 4.4.3.3 |  |  | O |  |  |
| 4 |  |  | Read Audio Input Type |  |  | [1] 4.4.3.4 |  |  | O |  |  |
| 5 |  |  | Configure Audio Input Status Notifications |  |  | [1] 4.4.3.5 |  |  | O |  |  |
| 6 |  |  | Read Audio Input Status |  |  | [1] 4.4.3.6 |  |  | O |  |  |
| 7 |  |  | Set Gain Setting |  |  | [1] 4.4.3.7.1 |  |  | O |  |  |
| 8 |  |  | Mute |  |  | [1] 4.4.3.7.3 |  |  | O |  |  |
| 9 |  |  | Unmute |  |  | [1] 4.4.3.7.2 |  |  | O |  |  |
| 10 |  |  | Set Manual Gain Mode |  |  | [1] 4.4.3.7.4 |  |  | O |  |  |
| 11 |  |  | Set Automatic Gain Mode |  |  | [1] 4.4.3.7.5 |  |  | O |  |  |
| 12 |  |  | Configure Audio Input Description Notifications |  |  | [1] 4.4.3.8 |  |  | O |  |  |
| 13 |  |  | Read Audio Input Description |  |  | [1] 4.4.3.9 |  |  | O |  |  |
| 14 |  |  | Set Audio Input Description |  |  | [1] 4.4.3.10 |  |  | O |  |  |

C.1: Mandatory IF VCP 16/3 “Read Gain Setting Properties” OR VCP 16/4 “Read Audio Input Type” OR VCP 16/5 “Configure Audio Input Status Notifications” OR VCP 16/6 “Read Audio Input Status” OR VCP 16/7 “Set Gain Setting” OR VCP 16/8 “Mute” OR VCP 16/9 “Unmute” OR VCP 16/10 “Set Manual Gain Mode” OR VCP 16/11 “Set Automatic Gain Mode” OR VCP 16/12 “Configure Audio Input Description Notifications” OR VCP 16/13 “Read Audio Input Description” OR VCP 16/14 “Set Audio Input Description”, otherwise Optional. C.2: Mandatory to support none or all.

#### 2.4.2 GATT requirements

Table 17: Volume Controller GATT Requirements
Prerequisite: VCP 1/2 “Volume Controller”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Discover All Primary Services | [1] 4.1 | C.1 | [2] GATT 3/2 |  |  |
| 2 | Discover Primary Service by Service UUID | [1] 4.1 | C.1 | [2] GATT 3/3 |  |  |
| 3 | Find Included Services | [1] 4.1 | C.3 | [2] GATT 3/4 |  |  |
| 4 | Discover All Characteristics of a Service | [1] 4.1 | C.2 | [2] GATT 3/5 |  |  |
| 5 | Discover Characteristics by UUID | [1] 4.1 | C.2 | [2] GATT 3/6 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 6 | Discover All Characteristic Descriptors | [1] 4.1 | M | [2] GATT 3/7 |  |  |
| 7 | Read Characteristic Value | [1] 4.1 | M | [2] GATT 3/8 |  |  |
| 8 | Write Characteristic Value | [1] 4.1 | M | [2] GATT 3/14 |  |  |
| 9 | Single Notification | [1] 4.1 | M | [2] GATT 3/17 |  |  |
| 10 | Read Characteristic Descriptor | [1] 4.1 | M | [2] GATT 3/19 |  |  |
| 11 | Write Characteristic Descriptor | [1] 4.1 | M | [2] GATT 3/21 |  |  |
| 12 | GATT Client over BR/EDR | [1] 4.1 | C.4 | [2] GATT 1a/2 |  |  |
| 13 | GATT Client over LE | [1] 4.1 | C.5 | [2] GATT 1a/1 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one. C.3: Mandatory IF VCP 16/1 “Configure Audio Input State Notifications” OR VCP 14/1 “Configure Offset State Notifications” otherwise Optional. C.4: Mandatory IF VCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.5: Mandatory IF VCP 2/2 “Profile supported over LE”, otherwise not defined.

#### 2.4.3 GAP requirements

Table 18: GAP Requirements (Volume Controller)
Prerequisite: VCP 1/2 “Volume Controller”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Central | [1] 4.1 | C.2 | [3] GAP 5/4 |  |  |
| 2 | LE security mode 1 | [1] 5.1 | C.2 | [3] GAP 35/1 |  |  |
| 3 | Bondable mode (LE) | [1] 6.2 | C.2 | [3] GAP 34/2 |  |  |
| 4 | Bonding procedure | [1] 6.2 | C.3 | [3] GAP 34/3 |  |  |
| 5 | Initiation of dedicated bonding | [1] 6.3 | C.1 | [3] GAP 3/6 |  |  |
| 6 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 5.1 | C.2 | [3] GAP 35/11 |  |  |
| 7 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 5.1 | C.3 | [3] GAP 35/12 |  |  |
| 8 | Derivation of LE LTK from BR/EDR Link Key | [1] 5.1 | C.7 | [3] GAP 41/2b |  |  |
| 9 | Security mode 4, level 2 | [1] 5.2 | C.4 | [3] GAP 2/7c |  |  |
| 10 | 128-bit encryption key size capable (BR/EDR) | [1] 5.2 | C.4 | [3] GAP 2/13 |  |  |
| 11 | Derivation of BR/EDR Link Key from LE LTK | [1] 5.2 | C.8 | [3] GAP 41/2a |  |  |
| 12 | Minimum 128 Bit entropy key (LE) | [1] 5.1 | C.2 | [3] GAP 35/13 |  |  |
| 13 | BR/EDR Secure Connections | [1] 5.2 | C.8 | N/A |  |  |
| 14 | LE Secure Connections (Central) | [1] 5.1 | C.7 | [3] GAP 37b/5 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 15 | Out of Band (Central) | [1] 5.1 | C.7 | [3] GAP 37b/9 |  |  |
| 16 | Out-of-Band (BR/EDR) | [1] 5.2 | C.8 | [3] GAP 2/14 |  |  |

C.1: Optional IF VCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.2: Mandatory IF VCP 2/2 “Profile supported over LE”, otherwise not defined. C.3: Optional IF VCP 2/2 “Profile supported over LE”, otherwise not defined. C.4: Mandatory IF VCP 2/1 “Profile supported over BR/EDR”, otherwise not defined. C.5–C.6: No longer used. C.7: Mandatory to support at least one IF VCP 2/2 “Profile supported over LE”, otherwise not defined. C.8: Mandatory to support at least one IF VCP 2/1 “Profile supported over BR/EDR”, otherwise not defined.

## 3 References

[1] Volume Control Profile Specification, Version 1.0
[2] ICS Proforma for Generic Attribute Profile (GATT)
[3] ICS Proforma for Generic Access Profile (GAP)
[4] ICS Proforma for Volume Offset Control Service (VOCS)
[5] ICS Proforma for Audio Input Control Service (AICS)
[6] ICS Proforma for Volume Control Service (VCS)
[7] ICS Proforma for Link Layer (LL)

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2020-12-22 | Approved by BTI on 2020-11-29. VCP v1.0 adopted by the BoD on 2020-12-15. Prepared for publication. |
|  |  |  | p0ed2 r00–r02 |  |  | 2021-03-23 – 2021-05-23 | TSE 15974 (rating 1): Fixed typos in Table 12. Editorials for consistency checker findings. |
|  |  |  | p0 edition 2 |  |  | 2021-05-25 | Approved by BTI on 2021-05-06. Prepared for edition 2 publication. |
|  |  |  | p0ed3 r00–r01 |  |  | 2021-07-26 – 2021-09-24 | TSE 16976 (rating 1): Corrected conditional wording for C.1 of Table 12. (NOTE: Other changes tracked in this CR were made in the edition 2 publication.) Consistency checker editorials to align with wording in the latest ICS template. |
|  |  |  | p0 edition 3 |  |  | 2021-09-28 | Approved by BTI on 2021-09-27. Prepared for edition 3 publication. |
|  |  |  | p0ed4r00 |  |  | 2022-01-25 | TSE 18189 (rating 1): Updated Link Layer inter-layer dependency item in Table 5 to align with updates made in the LL ICS. Made template-related fixes, including aligning the copyright page with v2 of the DNMD. |
|  |  |  | p0 edition 4 |  |  | 2022-01-27 | Approved by BTI on 2022-01-27. Prepared for edition 4 publication. |
|  |  |  | p1r00 |  |  | 2022-02-24 | TSE 18371 (rating 2): Removed “is/not supported” language in the conditionals globally, and updated references for Table 12. Performed template-related formatting fixes. Fixed cross-reference formatting where possible. |
| 1 |  |  | p1 |  |  | 2022-06-28 | Approved by BTI on 2022-06-20. Prepared for TCRL 2022-1 publication. |
|  |  |  | p1ed2r00 |  |  | 2023-02-15 | TSE 22637 (rating 1): Replaced ILD references to Security Manager 8/1 with SM 8a/1 (for Central role) or SM 8b/1 (for Peripheral role) in Tables 7 and 19. Updated references. Editorials to align the document with the latest ICS template. Deleted draft revision history comments prior to p0. |
|  |  |  | p1 edition 2 |  |  | 2023-03-15 | Approved by BTI on 2023-03-13. Prepared for edition 2 publication. |
|  |  |  | p2r00–r03 |  |  | 2023-08-09 – 2023-11-28 | TSE 23339 (rating 2): Removed the reference to the SM ICS and updated cross-refs accordingly. Added 6/3a, 6/5a, 6/5b, 6/9, 6/10, 6/11, 6/12, 6/13, and 6/14 and C.6 – C.12, and updated C.4 and C.5 and the status for 6/4 and 6/7. Deleted Table 7 (the SM Requirements section). Revised the capability descriptions for 10/1, 10/2, and 10/3. Added 18/7a, 18/9a, 18/9b, 18/13, 18/14, 18/15, 18/16, 18/17, and 18/18 and C.7 – C.12, and updated C.5 and C.6 and the status for 18/8 and 18/11. Deleted Table 7 (the SM Requirements section). |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 2 |  |  | p2 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p3r00–r02 |  |  | 2024-11-08 – 2024-12-06 | TSE 24997 (rating 2): Per E24427, added conditional C.3 to Table 17 and updated the Status value for Item 3 to reference C.3. |
| 3 |  |  | p3 |  |  | 2025-02-18 | Approved by BTI on 2025-02-09. Prepared for TCRL 2025-1 publication. |
|  |  |  | p4r00–r01 |  |  | 2025-02-20 – 2025-04-10 | TSE 26842 (rating 2): For Table 17, added 17/12 and 17/13 and conditionals C.4 and C.5. TSE 27380 (rating 1): Updated the Status value for VCP 2/1 and VCP 2/2. Added conditionals C.1 and C.2 to Table 2 and renumbered C.1 as C.3. |
| 4 |  |  | p4 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p5r00 |  |  | 2025-07-23 | TSE 27574 (rating 1): Updated ILD in VCP 6/13 and VCP 18/1. |
| 5 |  |  | p5 |  |  | 2025-11-04 | Approved by BTI on 2025-09-29. Prepared for TCRL pkg101 publication. |
|  |  |  | p6r00–r01 |  |  | 2025-12-05 – 2026-01-14 | TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 6 |  |  | p6 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |  |
| Jawid Mirani |  |  | Bluetooth SIG, Inc. |  |  |
