# TMAP.ICS.p4

> Source: PDF converted via PyMuPDF.

---

Telephony and Media Audio Profile (TMAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: TMAP.ICS.p4 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Audio, Telephony, and Automotive Working Group ▪ Published during TCRL: TCRL.pkg102
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

|  | Item |  |  | Profile Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Call Gateway (CG) |  |  | [2] 3.1 |  |  | C.1 |  |  |
| 2 |  |  | Call Terminal (CT) |  |  | [2] 3.1 |  |  | C.1 |  |  |
| 3 |  |  | Unicast Media Sender (UMS) |  |  | [2] 3.1 |  |  | C.1 |  |  |
| 4 |  |  | Unicast Media Receiver (UMR) |  |  | [2] 3.1 |  |  | C.1 |  |  |
| 5 |  |  | Broadcast Media Sender (BMS) |  |  | [2] 3.1 |  |  | C.1 |  |  |
| 6 |  |  | Broadcast Media Receiver (BMR) |  |  | [2] 3.1 |  |  | C.1, C.2 |  |  |
| 7 |  |  | TMA Client |  |  | [2] 3.8 |  |  | O |  |  |
| 8 |  |  | TMA Server |  |  | [2] 3.8 |  |  | C.3, C.4 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF TMAP 1/4 “Unicast Media Receiver (UMR)”, otherwise Optional. C.3:  Mandatory IF TMAP 1/1 “Call Gateway (CG)” OR TMAP 1/2 “Call Terminal (CT)” OR TMAP 1/3
“Unicast Media Sender (UMS)” OR TMAP 1/4 “Unicast Media Receiver (UMR)” OR TMAP 1/6 “Broadcast Media Receiver (BMR)”, otherwise Optional. C.4:  (Reverse ILD) Mandatory IF TMAP 1/5 “Broadcast Media Sender (BMS)” AND GATT 1/2 “Generic
Attribute Profile (GATT) Server”, otherwise Optional.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [2] 2.3 |  |  | C.1 |  |  |
| 1a |  |  | Service TMAS supported over BR/EDR |  |  | [2] 4.3 |  |  | C.2 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [2] 2.3 |  |  | C.3, C.4 |  |  |
| 2a |  |  | Service TMAS supported over LE |  |  | [2] 4.3 |  |  | C.3, C.5 |  |  |

C.1: Excluded for this Profile. C.2: Optional IF (TMAP 1/7 “TMA Client” OR TMAP 1/8 “TMA Server”) AND NOT CORE 41/2 “LE Core
Configuration” AND NOT CORE 40/1 “Core-Controller”, otherwise Excluded. C.3: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core-
Controller”. C.4: Mandatory for this Profile. C.5: Mandatory IF TMAP 1/7 “TMA Client” OR TMAP 1/8 “TMA Server”, otherwise Excluded.

### 2.3 Host configurations

Table 3: GAP Host Configuration Requirements

| Item | Device Configuration | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GAP LE Host | [2] 4.3 | M | [1] GAP 0b/2 |  |  |


| Item | Device Configuration | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 2 | GAP BR/EDR Host | [2] 4.9 | O | [1] GAP 0b/1 |  |  |


## 3 Profile support requirements


### 3.1 CAP Initiator/Commander roles


#### 3.1.1 Call Gateway (CG)


##### 3.1.1.1 CG versions

Table 10: X.Y Versions
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0 |  |  | [2] |  |  | M |  |  |

Table 11: X.Y.Z Versions
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0.1 |  |  | [2][10] |  |  | C.1 |  |  |

C.1: Optional IF TMAP 10/1 “TMAP v1.0”, otherwise Excluded.

##### 3.1.1.2 CG profile and service dependencies

Table 12: Call Gateway Profile and Service Dependencies
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Common Audio Profile | [2] 3.1 | M | [3] CAP |  |  |
| 2 | Basic Audio Profile | [2] 3.1 | M | [4] BAP |  |  |
| 3 | Call Control Profile | [2] 3.1 | M | [7] CCP |  |  |


##### 3.1.1.3 Role discovery requirements

Table 13: Role Discovery Requirements
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Advertise Call Gateway Support |  |  | [2] 3.4 |  |  | O |  |  |

Table 14: CG Inter-Layer Dependency Role Requirements
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| CAP Roles |  |  |  |  |  |  |
| 1 | CAP Initiator | [2] 3.1 | M | [3] CAP 1/2 |  |  |
| 2 | CAP Commander | [2] 3.1 | M | [3] CAP 1/3 |  |  |
| Content Control |  |  |  |  |  |  |
| 3 | CCP Call Control Server | [2] 3.1 | M | [3] CAP 16/5 |  |  |
| Capture and Rendering Control |  |  |  |  |  |  |
| 4 | VCP Volume Controller | [2] 3.1 | M | [3] CAP 26/4 |  |  |
| CAP Initiator Unicast Client Role Requirements |  |  |  |  |  |  |
| 5 | Audio Source | [2] 3.1 | M | [3] CAP 18/1 |  |  |
| 6 | Audio Sink | [2] 3.1 | M | [3] CAP 18/2 |  |  |
| 7 | BAP Unicast Client | [2] 3.1 | M | [3] CAP 16/3 |  |  |
| Context Type Support Requirements |  |  |  |  |  |  |
| 8 | Conversational (CAP Initiator) | [10] 3.5.1.1 | C.1 | [3] CAP 22/2 |  |  |

C.1: Mandatory IF TMAP 11/1 “TMAP v1.0.1”, otherwise Optional.
Table 15: Call Gateway Config Codec Operation Parameters
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 30 Octets (Audio Source) | [2] 3.5.1.4.2 | O | [4] BAP 37/3 |  |  |
| 2 | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 60 Octets (Audio Source) | [2] 3.5.1.4.2 | O | [4] BAP 37/7 |  |  |
| 3 | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms _ Frame Duration, 80 Octets (Audio Source) | [2] 3.5.1.4.1 | M | [4] BAP 37/8 |  |  |
| 4 | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 30 Octets (Audio Sink) | [2] 3.5.1.4.2 | O | [4] BAP 36/3 |  |  |
| 5 | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 60 Octets (Audio Sink) | [2] 3.5.1.4.2 | O | [4] BAP 36/7 |  |  |
| 6 | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms _ Frame Duration, 80 Octets (Audio Sink) | [2] 3.5.1.4.1 | M | [4] BAP 36/8 |  |  |

Prerequisite: TMAP 1/1 “Call Gateway (CG)”

| Item | Audio Location Values | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Source) _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 39/3 |  |  |
| 2 | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Source) _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 39/7 |  |  |
| 3 | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 _ _ Max SDU Size, 2 RTN, 10 Max Transport Latency (Audio Source) _ _ | [2] 3.5.1.4.2 | M | [4] BAP 39/8 |  |  |
| 4 | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Sink) _ _ | [2] 3.5.1.4.2 | C.3 | [4] BAP 38/3 |  |  |
| 5 | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Sink) _ _ | [2] 3.5.1.4.2 | C.4 | [4] BAP 38/7 |  |  |
| 6 | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 _ _ Max SDU Size, 2 RTN, 10 Max Transport Latency (Audio Sink) _ _ | [2] 3.5.1.4.2 | M | [4] BAP 38/8 |  |  |

C.1: Mandatory IF TMAP 15/1 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30
Octets (Audio Source)”, otherwise not defined. C.2: Mandatory IF TMAP 15/2 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60
Octets (Audio Source)”, otherwise not defined. C.3: Mandatory IF TMAP 15/4 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30
Octets (Audio Sink)”, otherwise not defined. C.4: Mandatory IF TMAP 15/5 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60
Octets (Audio Sink)”, otherwise not defined.
Table 17: Number of Concurrent Unicast Audio Streams, Channels, and Devices
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

|  | Item |  |  | Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Configuration A: 1 bidirectional stream between CG and CT |  |  | [2] 3.5.1.5 |  |  | M |  |  |
| 2 |  |  | Configuration B: 1 stream with 1 channel from CG to CT, 1 stream with 1 channel from 2nd CT to CG. |  |  | [2] 3.5.1.5 |  |  | M |  |  |
| 3 |  |  | Configuration C: 1 stream with 1 channel from CG to CT, 1 bidirectional stream between CG and a 2nd CT |  |  | [2] 3.5.1.5 |  |  | M |  |  |
| 4 |  |  | Configuration D: 1 stream with 1 channel from CG to CT, 1 bidirectional stream between CG and same CT |  |  | [2] 3.5.1.5 |  |  | M |  |  |
| 5 |  |  | Configuration E: 1 bidirectional stream with 2 channels from CG to CT |  |  | [2] 3.5.1.5 |  |  | O |  |  |
| 6 |  |  | Configuration F: 2 bidirectional streams between CG and CT |  |  | [2] 3.5.1.5 |  |  | O |  |  |
| 7 |  |  | Configuration G: 1 bidirectional stream from CG to CT, 1 bidirectional stream between CG and a 2nd CT |  |  | [2] 3.5.1.5 |  |  | O |  |  |

Prerequisite: TMAP 1/1 “Call Gateway (CG)”

| Item | Characteristics | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Sink Audio Locations characteristic | [2] 3.5.1.2 | M | [4] BAP 32/2 |  |  |
| 2 | Source Audio Locations characteristic | [2] 3.5.1.2 | M | [4] BAP 32/4 |  |  |

Table 19: Call Gateway Audio Channel Allocation Audio Location Values
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

|  | Item |  |  | Audio Location Values |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Front Left Audio Location |  |  | [2] 3.5.1.4.1 |  |  | O |  |  |
| 2 |  |  | Front Right Audio Location |  |  | [2] 3.5.1.4.1 |  |  | O |  |  |
| 3 |  |  | Front Right and Front Left Audio Locations |  |  | [2] 3.5.1.4.1 |  |  | C.1 |  |  |

C.1: Mandatory IF TMAP 17/5 “Configuration E: 1 bidirectional stream with 2 channels from CG to CT”,
otherwise Excluded.
Table 20: Call Gateway Audio Input Features
Prerequisite: TMAP 1/1 “Call Gateway (CG)”

|  | Item |  |  | Features |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CG Audio Source accepts external mono input |  |  | [2] 3.5.1.5 |  |  | O |  |  |


#### 3.1.2 Unicast Media Sender (UMS)


##### 3.1.2.1 UMS versions

Table 30: X.Y Versions
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0 |  |  | [2] |  |  | M |  |  |

Table 31: X.Y.Z Versions
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0.1 |  |  | [2][10] |  |  | C.1 |  |  |

C.1: Optional IF TMAP 30/1 “TMAP v1.0”, otherwise Excluded.
Table 32: UMS Profile and Service Dependencies
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Common Audio Profile | [2] 3.1 | M | [3] CAP |  |  |
| 2 | Basic Audio Profile | [2] 3.1 | M | [4] BAP |  |  |
| 3 | Media Control Profile | [2] 3.1 | M | [6] MCP |  |  |


##### 3.1.2.3 Role discovery requirements

Table 33: Role Discovery Requirements
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Advertise Unicast Media Sender Support |  |  | [2] 3.4 |  |  | O |  |  |


##### 3.1.2.4 UMS requirements

Table 34: UMS Inter-Layer Dependency Role Requirements
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| CAP Roles |  |  |  |  |  |  |
| 1 | CAP Initiator | [2] 3.1 | M | [3] CAP 1/2 |  |  |
| 2 | CAP Commander | [2] 3.1 | M | [3] CAP 1/3 |  |  |
| Content Control |  |  |  |  |  |  |
| 3 | MCP Media Control Server | [2] 3.1 | M | [3] CAP 16/6 |  |  |
| Capture and Rendering Control |  |  |  |  |  |  |
| 4 | VCP Volume Controller | [2] 3.1 | M | [3] CAP 26/4 |  |  |
| CAP Initiator Unicast Client Role Requirements |  |  |  |  |  |  |
| 5 | Audio Source | [2] 3.1 | M | [3] CAP 18/1 |  |  |
| 6 | BAP Unicast Client | [2] 3.1 | M | [3] CAP 16/3 |  |  |
| Context Type Support Requirements |  |  |  |  |  |  |
| 7 | Media (CAP Initiator) | [10] 3.5.1.1 | C.1 | [3] CAP 22/3 |  |  |

C.1: Mandatory IF TMAP 31/1 “TMAP v1.0.1”, otherwise Optional.
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 _ ms Frame Duration, 75 Octets | [2] 3.5.1.4.2 | O | [4] BAP 37/11 |  |  |
| 2 | 48 2 LC3: 48 kHz Sampling Frequency, 10 _ ms Frame Duration, 100 Octets | [2] 3.5.1.4.1 | M | [4] BAP 37/12 |  |  |
| 3 | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 _ ms Frame Duration, 90 Octets | [2] 3.5.1.4.2 | O | [4] BAP 37/13 |  |  |
| 4 | 48 4 LC3: 48 kHz Sampling Frequency, 10 _ ms Frame Duration, 120 Octets | [2] 3.5.1.4.1 | C.1 | [4] BAP 37/14 |  |  |
| 5 | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 _ ms Frame Duration, 117 Octets | [2] 3.5.1.4.2 | O | [4] BAP 37/15 |  |  |
| 6 | 48 6 LC3: 48 kHz Sampling Frequency, 10 _ ms Frame Duration, 155 Octets | [2] 3.5.1.4.1 | C.1 | [4] BAP 37/16 |  |  |
| 7 | 441 1 LC3: 44.1 kHz Sampling Frequency, _ 8.163 ms Frame Duration, 97 Octets | [2] 3.5.1.4.2 | O | [4] BAP 37/9 |  |  |
| 8 | 441 2 LC3: 44.1 kHz Sampling Frequency, _ 10.884 ms Frame Duration, 130 Octets | [2] 3.5.1.4.2 | O | [4] BAP 37/10 |  |  |

C.1: Mandatory to support at least one.
Table 36: Unicast Media Sender QoS Settings Requirements
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency Media |  |  |  |  |  |  |
| 1 | 48 1 1 LC3: 7500 SDU Interval, unframed, _ _ 75 Max SDU Size, 5 RTN, 15 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 39/11 |  |  |
| 2 | 48 2 1 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 5 RTN, 20 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 39/12 |  |  |
| 3 | 48 3 1 LC3: 7500 SDU Interval, unframed, _ _ 90 Max SDU Size, 5 RTN, 15 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 39/13 |  |  |
| 4 | 48 4 1 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 5 RTN, 20 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.3 | [4] BAP 39/14 |  |  |
| 5 | 48 5 1 LC3: 7500 SDU Interval, unframed, _ _ 117 Max SDU Size, 5 RTN, 15 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.4 | [4] BAP 39/15 |  |  |
| 6 | 48 6 1 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 5 RTN, 20 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.5 | [4] BAP 39/16 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 7 | 441 1 1 LC3: 8163 SDU Interval, framed, 97 _ _ Max SDU Size, 5 RTN, 24 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.6 | [4] BAP 39/9 |  |  |
| 8 | 441 2 1 LC3: 10884 SDU Interval, framed, _ _ 130 Max SDU Size, 5 RTN, 31 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.7 | [4] BAP 39/10 |  |  |
| High Reliability Media |  |  |  |  |  |  |
| 9 | 48 1 2 LC3: 7500 SDU Interval, unframed, _ _ 75 Max SDU Size, 13 RTN, 75 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 41/11 |  |  |
| 10 | 48 2 2 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 13 RTN, 95 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 41/12 |  |  |
| 11 | 48 3 2 LC3: 7500 SDU Interval, unframed, _ _ 90 Max SDU Size, 13 RTN, 75 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 41/13 |  |  |
| 12 | 48 4 2 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 13 RTN, 100 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.3 | [4] BAP 41/14 |  |  |
| 13 | 48 5 2 LC3: 7500 SDU Interval, unframed, _ _ 117 Max SDU Size, 13 RTN, 75 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.4 | [4] BAP 41/15 |  |  |
| 14 | 48 6 2 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 13 RTN, 100 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.5 | [4] BAP 41/16 |  |  |
| 15 | 441 1 2 LC3: 8163 SDU Interval, framed, 97 _ _ Max SDU Size, 13 RTN, 80 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.6 | [4] BAP 41/9 |  |  |
| 16 | 441 2 2 LC3: 10884 SDU Interval, framed, _ _ 130 Max SDU Size, 13 RTN, 85 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.7 | [4] BAP 41/10 |  |  |

C.1: Mandatory IF TMAP 35/1 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75
Octets”, otherwise not defined. C.2: Mandatory IF TMAP 35/3 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90
Octets”, otherwise not defined. C.3: Mandatory IF TMAP 35/4 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120
Octets”, otherwise not defined. C.4: Mandatory IF TMAP 35/5 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117
Octets”, otherwise not defined. C.5: Mandatory IF TMAP 35/6 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155
Octets”, otherwise not defined. C.6:  Mandatory IF TMAP 35/7 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration,

## 97 Octets”, otherwise not defined. C.7: Mandatory IF TMAP 35/8 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration,


## 130 Octets”, otherwise not defined.

Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Characteristics | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Sink Audio Locations characteristic | [2] 3.5.1.2 | M | [4] BAP 32/2 |  |  |

Table 38: Unicast Media Sender Audio Channel Allocation Audio Location Values
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

|  | Item |  |  | Audio Location Values |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Front Left Audio Location |  |  | [2] 3.5.1.4.1 |  |  | M |  |  |
| 2 |  |  | Front Right Audio Location |  |  | [2] 3.5.1.4.1 |  |  | M |  |  |
| 3 |  |  | Front Right and Front Left Audio Locations |  |  | [2] 3.5.1.4.1 |  |  | C.1 |  |  |

C.1: Mandatory IF TMAP 39/2 “AC 4: 1 Server, 1 Sink ASE, 2 Channels/Sink, 1 CIS, 1 Audio Stream”,
otherwise Excluded.
Table 39: Unicast Media Sender BAP Audio Configuration
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Two Audio Channels | [2] 3.5.1.4.1 | O | [4] BAP 30/3 |  |  |
| 2 | AC 4: 1 Server, 1 Sink ASE, 2 Channels/Sink, 1 CIS, 1 Audio Stream | [2] 3.5.1.4.1 | C.1 | [4] BAP 44/4 |  |  |

C.1: Optional IF TMAP 39/1 “Two Audio Channels”, otherwise not defined.
Table 40: GMCS Generic Media Control Point Opcodes
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Sub-procedure | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Play | [2] 3.6.1 | M | [9] MCS 23/1 |  |  |
| 2 | Pause | [2] 3.6.1 | M | [9] MCS 23/2 |  |  |

Table 41: Call Gateway Audio Input Features
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)”

| Item | Features | Reference | Status |
| --- | --- | --- | --- |
| 1 | UMS Audio Source accepts external mono input | [2] 3.5.1.5 | O |


#### 3.1.3 Broadcast Media Sender (BMS)


##### 3.1.3.1 BMS versions

Table 50: X.Y Versions
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0 |  |  | [2] |  |  | M |  |  |

Table 51: X.Y.Z Versions
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0.1 |  |  | [2][10] |  |  | C.1 |  |  |

C.1: Optional IF TMAP 50/1 “TMAP v1.0”, otherwise Excluded.

##### 3.1.3.2 BMS Profile and Service Dependencies

Table 52: BMS Profile and Service Dependencies
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Common Audio Profile | [2] 3.1 | M | [3] CAP |  |  |
| 2 | Basic Audio Profile | [2] 3.1 | M | [4] BAP |  |  |


##### 3.1.3.3 Role discovery requirements

Table 53: Role Discovery Requirements
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)” AND TMAP 1/8 “TMA Server”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Advertise Broadcast Media Sender Support |  |  | [2] 3.4 |  |  | O |  |  |


##### 3.1.3.4 BMS requirements

Table 54: BMS Inter-Layer Dependency Role Requirements
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| CAP Roles |  |  |  |  |  |  |
| 1 | CAP Initiator | [2] 3.1 | M | [3] CAP 1/2 |  |  |
| 2 | CAP Commander | [2] 3.1 | C.1 | [3] CAP 1/3 |  |  |
| CAP Audio Stream Transition |  |  |  |  |  |  |
| 3 | BAP Broadcast Source | [2] 3.1 | M | [3] CAP 16/2 |  |  |


| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 4 | BAP Broadcast Assistant | [2] 3.5.2.5 | C.2 | [3] CAP 26/2 |  |  |
| Context Type Support Requirements |  |  |  |  |  |  |
| 5 | Media (BAP Broadcast Source) | [10] 3.5.2.1 | C.3 | [4] BAP 59/3 |  |  |

C.1: Mandatory IF TMAP 1/3 “Unicast Media Sender (UMS)”, otherwise Optional. C.2: Mandatory IF TMAP 1/3 “Unicast Media Sender (UMS)”, otherwise not defined. C.3: Mandatory IF TMAP 51/1 “TMAP v1.0.1”, otherwise Optional.
Table 55: Broadcast Media Sender Codec Settings Requirements
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 _ ms Frame Duration, 75 Octets | [2] 3.5.2.1 | M | [4] BAP 54/11 |  |  |
| 2 | 48 2 LC3: 48 kHz Sampling Frequency, 10 _ ms Frame Duration, 100 Octets | [2] 3.5.2.1 | M | [4] BAP 54/12 |  |  |
| 3 | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 _ ms Frame Duration, 90 Octets | [2] 3.5.2.1 | C.1 | [4] BAP 54/13 |  |  |
| 4 | 48 4 LC3: 48 kHz Sampling Frequency, 10 _ ms Frame Duration, 120 Octets | [2] 3.5.2.1 | C.2 | [4] BAP 54/14 |  |  |
| 5 | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 _ ms Frame Duration, 117 Octets | [2] 3.5.2.1 | C.1 | [4] BAP 54/15 |  |  |
| 6 | 48 6 LC3: 48 kHz Sampling Frequency, 10 _ ms Frame Duration, 155 Octets | [2] 3.5.2.1 | C.2 | [4] BAP 54/16 |  |  |
| 7 | 441 1 LC3: 44.1 kHz Sampling Frequency, _ 8.163 ms Frame Duration, 97 Octets | [2] 3.5.2.3 | O | [4] BAP 54/9 |  |  |
| 8 | 441 2 LC3: 44.1 kHz Sampling Frequency, _ 10.884 ms Frame Duration, 130 Octets | [2] 3.5.2.3 | O | [4] BAP 54/10 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one.
Table 56: Broadcast Media Sender QoS Settings Requirements
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency Media |  |  |  |  |  |  |
| 1 | 48 1 1 LC3: 7500 SDU Interval, unframed, _ _ 75 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 55/11 |  |  |
| 2 | 48 2 1 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 55/12 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 3 | 48 3 1 LC3: 7500 SDU Interval, unframed, _ _ 90 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [2] 3.5.2.3 | C.1 | [4] BAP 55/13 |  |  |
| 4 | 48 4 1 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [2] 3.5.2.3 | C.2 | [4] BAP 55/14 |  |  |
| 5 | 48 5 1 LC3: 7500 SDU Interval, unframed, _ _ 117 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [2] 3.5.2.3 | C.3 | [4] BAP 55/15 |  |  |
| 6 | 48 6 1 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [2] 3.5.2.3 | C.4 | [4] BAP 55/16 |  |  |
| 7 | 441 1 1 LC3: 8163 SDU Interval, framed, _ _ 97 Max SDU Size, 4 RTN, 24 Max Transport Latency _ _ | [2] 3.5.2.3 | C.5 | [4] BAP 55/9 |  |  |
| 8 | 441 2 1 LC3: 10884 SDU Interval, framed, _ _ 130 Max SDU Size, 4 RTN, 31 Max Transport Latency _ _ | [2] 3.5.2.3 | C.6 | [4] BAP 55/10 |  |  |
| High Reliability Media |  |  |  |  |  |  |
| 9 | 48 1 2 LC3: 7500 SDU Interval, unframed, _ _ 75 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 56/11 |  |  |
| 10 | 48 2 2 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 56/12 |  |  |
| 11 | 48 3 2 LC3: 7500 SDU Interval, unframed, _ _ 90 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [2] 3.5.2.3 | C.1 | [4] BAP 56/13 |  |  |
| 12 | 48 4 2 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [2] 3.5.2.3 | C.2 | [4] BAP 56/14 |  |  |
| 13 | 48 5 2 LC3: 7500 SDU Interval, unframed, _ _ 117 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [2] 3.5.2.3 | C.3 | [4] BAP 56/15 |  |  |
| 14 | 48 6 2 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [2] 3.5.2.3 | C.4 | [4] BAP 56/16 |  |  |
| 15 | 441 1 2 LC3: 8163 SDU Interval, framed, _ _ 97 Max SDU Size, 4 RTN, 54 Max Transport Latency _ _ | [2] 3.5.2.3 | C.5 | [4] BAP 56/9 |  |  |
| 16 | 441 2 2 LC3: 10884 SDU Interval, framed, _ _ 130 Max SDU Size, 4 RTN, 60 Max Transport Latency _ _ | [2] 3.5.2.3 | C.6 | [4] BAP 56/10 |  |  |

C.1: Mandatory IF TMAP 55/3 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90
Octets”, otherwise not defined. C.2: Mandatory IF TMAP 55/4 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120
Octets”, otherwise not defined. C.3: Mandatory IF TMAP 55/5 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117
Octets”, otherwise not defined.
Octets”, otherwise not defined. C.5: Mandatory IF TMAP 55/7 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration,

## 97 Octets”, otherwise not defined. C.6: Mandatory IF TMAP 55/8 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration,


## 130 Octets”, otherwise not defined.

Table 57: Broadcast Media Sender Audio Channel Allocation Audio Location Values
Prerequisite: TMAP 1/5 “Broadcast Media Sender (BMS)”

|  | Item |  |  | Audio Location Values |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Front Left Audio Location |  |  | [2] 3.5.2.2 |  |  | M |  |  |
| 2 |  |  | Front Right Audio Location |  |  | [2] 3.5.2.2 |  |  | M |  |  |
| 3 |  |  | Front Right and Front Left Audio Locations |  |  | [2] 3.5.2.2 |  |  | O |  |  |


### 3.2 CAP Acceptor/Commander roles


#### 3.2.1 Call Terminal (CT)


##### 3.2.1.1 CT versions

Table 70: X.Y Versions
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0 |  |  | [2] |  |  | M |  |  |

Table 71: X.Y.Z Versions
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0.1 |  |  | [2][10] |  |  | C.1 |  |  |

C.1: Optional IF TMAP 70/1 “TMAP v1.0”, otherwise Excluded.

##### 3.2.1.2 CT profile and service dependencies

Table 72: CT Profile and Service Dependencies
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Common Audio Profile | [2] 3.1 | M | [3] CAP |  |  |
| 2 | Basic Audio Profile | [2] 3.1 | M | [4] BAP |  |  |

Table 73: Role Discovery Requirements
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Advertise Call Terminal Support |  |  | [2] 3.4 |  |  | O |  |  |


##### 3.2.1.4 CT requirements

Table 74: CT Inter-Layer Dependency Role Requirements
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| CAP Roles |  |  |  |  |  |  |
| 1 | CAP Acceptor | [2] 3.1 | M | [3] CAP 1/1 |  |  |
| 2 | CAP Commander | [2] 3.1 | O | [3] CAP 1/3 |  |  |
| Capture and Rendering Control |  |  |  |  |  |  |
| 3 | VCP Volume Renderer | [2] 3.1 | C.1 | [3] CAP 6/5 |  |  |
| BAP Unicast Server Role Requirements |  |  |  |  |  |  |
| 4 | BAP Audio Sink | [2] 3.1 | C.2 | [4] BAP 8/1 |  |  |
| 5 | BAP Audio Source | [2] 3.1 | C.2 | [4] BAP 8/2 |  |  |
| 6 | BAP Unicast Server | [2] 3.1 | M | [3] CAP 6/4 |  |  |
| Context Type Support Requirements |  |  |  |  |  |  |
| 7 | Conversational (BAP Audio Sink) | [10] 3.5.1.1 | C.3 | [4] BAP 21/2 |  |  |
| 8 | Conversational (BAP Audio Source) | [10] 3.5.1.1 | C.4 | [4] BAP 22/2 |  |  |

C.1: Mandatory IF TMAP 74/4 “BAP Audio Sink”, otherwise not defined. C.2: Mandatory to support at least one. C.3: Mandatory IF TMAP 71/1 “TMAP v1.0.1” AND TMAP 74/4 “BAP Audio Sink”, otherwise Optional. C.4: Mandatory IF TMAP 71/1 “TMAP v1.0.1” AND TMAP 74/5 “BAP Audio Source”, otherwise Optional.
Table 75: Call Terminal PAC Records
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

| Item | Record | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 30 Octets (Audio Sink) | [2] 3.5.1.1 | C.1 | [4] BAP 12/3 |  |  |
| 2 | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 60 Octets (Audio Sink) | [2] 3.5.1.1 | C.1 | [4] BAP 12/7 |  |  |
| 3 | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms _ Frame Duration, 80 Octets (Audio Sink) | [2] 3.5.1.1 | C.1 | [4] BAP 12/8 |  |  |
| 4 | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 30 Octets (Audio Source) | [2] 3.5.1.1 | C.2 | [4] BAP 13/3 |  |  |


| Item | Record | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 5 | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 60 Octets (Audio Source) | [2] 3.5.1.1 | C.2 | [4] BAP 13/7 |  |  |
| 6 | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms _ Frame Duration, 80 Octets (Audio Source) | [2] 3.5.1.1 | C.2 | [4] BAP 13/8 |  |  |

C.1: Mandatory IF TMAP 74/4 “BAP Audio Sink”, otherwise not defined. C.2: Mandatory IF TMAP 74/5 “BAP Audio Source”, otherwise not defined.
Table 76: Call Terminal QoS Settings Requirements
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Sink) _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 14/3 |  |  |
| 2 | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Sink) _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 14/7 |  |  |
| 3 | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 _ _ Max SDU Size, 2 RTN, 10 Max Transport Latency (Audio Sink) _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 14/8 |  |  |
| 4 | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Source) _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 15/3 |  |  |
| 5 | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 _ _ Max SDU Size, 2 RTN, 8 Max Transport Latency (Audio Source) _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 15/7 |  |  |
| 6 | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 _ _ Max SDU Size, 2 RTN, 10 Max Transport Latency (Audio Source) _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 15/8 |  |  |

C.1: Mandatory IF TMAP 74/4 “BAP Audio Sink”, otherwise not defined. C.2: Mandatory IF TMAP 74/5 “BAP Audio Source”, otherwise not defined.
Table 77: Number of Audio Outputs
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

|  | Item |  |  | Number |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 audio output |  |  | [2] 3.5.1.5 |  |  | M |  |  |
| 2 |  |  | 2 or more audio outputs |  |  | [2] 3.5.1.5 |  |  | O |  |  |

Prerequisite: TMAP 1/2 “Call Terminal (CT)”

|  | Item |  |  | Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Configuration D: 1 stream with 1 channel from CG to CT, 1 bidirectional stream between CG and CT |  |  | [2] 3.5.1.5 |  |  | C.1 |  |  |
| 2 |  |  | Configuration E: 1 bidirectional stream with 2 channels from CG to CT |  |  | [2] 3.5.1.5 |  |  | C.2 |  |  |
| 3 |  |  | Configuration F: 2 bidirectional streams between CG and CT |  |  | [2] 3.5.1.5 |  |  | C.2 |  |  |

C.1: Mandatory IF TMAP 74/4 “BAP Audio Sink” AND TMAP 74/5 “BAP Audio Source” AND TMAP 77/2
“2 or more audio outputs”, otherwise Excluded. C.2: Optional IF TMAP 74/4 “BAP Audio Sink” AND TMAP 74/5 “BAP Audio Source” AND TMAP 77/2 “2
or more audio outputs”, otherwise Excluded.
Table 79: Call Terminal Multi-Stream Configurations
Prerequisite: TMAP 1/2 “Call Terminal (CT)”

|  | Item |  |  | Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Case 1: Multiple CT audio sink devices each with a single ASE |  |  | [2] 3.7 |  |  | C.1 |  |  |
| 2 |  |  | Case 2: A single CT audio sink device with multiple ASEs |  |  | [2] 3.7 |  |  | C.1, C.2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF TMAP 77/2 “2 or more audio outputs”, otherwise Excluded.

#### 3.2.2 Unicast Media Receiver (UMR)


##### 3.2.2.1 UMR versions

Table 90: X.Y Versions
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0 |  |  | [2] |  |  | M |  |  |

Table 91: X.Y.Z Versions
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0.1 |  |  | [2][10] |  |  | C.1 |  |  |

C.1: Optional IF TMAP 90/1 “TMAP v1.0”, otherwise Excluded.
Table 92: UMR Profile and Service Dependencies
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Common Audio Profile | [2] 3.1 | M | [3] CAP |  |  |
| 2 | Basic Audio Profile | [2] 3.1 | M | [4] BAP |  |  |


##### 3.2.2.3 Role discovery requirements

Table 93: Role Discovery Requirements
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Advertise Unicast Media Receiver Support |  |  | [2] 3.4 |  |  | O |  |  |


##### 3.2.2.4 UMR requirements

Table 94: UMR Inter-Layer Dependency Role Requirements
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| CAP Roles |  |  |  |  |  |  |
| 1 | CAP Acceptor | [2] 3.1 | M | [3] CAP 1/1 |  |  |
| 2 | CAP Commander | [2] 3.1 | O | [3] CAP 1/3 |  |  |
| Capture and Rendering Control |  |  |  |  |  |  |
| 3 | VCP Volume Renderer | [2] 3.1 | M | [3] CAP 6/5 |  |  |
| BAP Unicast Server Role Requirements |  |  |  |  |  |  |
| 4 | BAP Audio Sink | [2] 3.1 | M | [4] BAP 8/1 |  |  |
| 5 | BAP Unicast Server | [2] 3.1 | M | [3] CAP 6/4 |  |  |
| Context Type Support Requirements |  |  |  |  |  |  |
| 6 | Media (BAP Audio Sink) | [10] 3.5.1.1 | C.1 | [4] BAP 21/3 |  |  |

C.1: Mandatory IF TMAP 91/1 “TMAP v1.0.1”, otherwise Optional.
Table 95: Unicast Media Receiver PAC Records
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

| Item | Record | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 75 Octets | [2] 3.5.1.1 | M | [4] BAP 12/11 |  |  |
| 2 | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms _ Frame Duration, 100 Octets | [2] 3.5.1.1 | M | [4] BAP 12/12 |  |  |


| Item | Record | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 3 | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 90 Octets | [2] 3.5.1.1 | M | [4] BAP 12/13 |  |  |
| 4 | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms _ Frame Duration, 120 Octets | [2] 3.5.1.1 | M | [4] BAP 12/14 |  |  |
| 5 | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 117 Octets | [2] 3.5.1.1 | M | [4] BAP 12/15 |  |  |
| 6 | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms _ Frame Duration, 155 Octets | [2] 3.5.1.1 | M | [4] BAP 12/16 |  |  |
| 7 | 441 1 LC3: 44.1 kHz Sampling Frequency, _ 8.163 ms Frame Duration, 97 Octets | [2] 3.5.1.4.2 | O | [4] BAP 12/9 |  |  |
| 8 | 441 2 LC3: 44.1 kHz Sampling Frequency, _ 10.884 ms Frame Duration, 130 Octets | [2] 3.5.1.4.2 | O | [4] BAP 12/10 |  |  |

Table 96: Unicast Media Receiver QoS Settings Requirements
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency Media |  |  |  |  |  |  |
| 1 | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 _ _ Max SDU Size, 5 RTN, 15 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 14/11 |  |  |
| 2 | 48 2 1 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 5 RTN, 20 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 14/12 |  |  |
| 3 | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 _ _ Max SDU Size, 5 RTN, 15 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 14/13 |  |  |
| 4 | 48 4 1 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 5 RTN, 20 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 14/14 |  |  |
| 5 | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 _ _ Max SDU Size, 5 RTN, 15 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 14/15 |  |  |
| 6 | 48 6 1 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 5 RTN, 20 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 14/16 |  |  |
| 7 | 441 1 1 LC3: 8163 SDU Interval, framed, 97 _ _ Max SDU Size, 5 RTN, 24 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 14/9 |  |  |
| 8 | 441 2 1 LC3: 10884 SDU Interval, framed, 130 _ _ Max SDU Size, 5 RTN, 31 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 14/10 |  |  |
| High Reliability Media |  |  |  |  |  |  |
| 9 | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 _ _ Max SDU Size, 13 RTN, 75 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 16/11 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 10 | 48 2 2 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 13 RTN, 95 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 16/12 |  |  |
| 11 | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 _ _ Max SDU Size, 13 RTN, 75 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 16/13 |  |  |
| 12 | 48 4 2 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 13 RTN, 100 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 16/14 |  |  |
| 13 | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 _ _ Max SDU Size, 13 RTN, 75 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 16/15 |  |  |
| 14 | 48 6 2 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 13 RTN, 100 Max Transport Latency _ _ | [2] 3.5.1.4.2 | M | [4] BAP 16/16 |  |  |
| 15 | 441 1 2 LC3: 8163 SDU Interval, framed, 97 _ _ Max SDU Size, 13 RTN, 80 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.1 | [4] BAP 16/9 |  |  |
| 16 | 441 2 2 LC3: 10884 SDU Interval, framed, 130 _ _ Max SDU Size, 13 RTN, 85 Max Transport Latency _ _ | [2] 3.5.1.4.2 | C.2 | [4] BAP 16/10 |  |  |

C.1: Mandatory IF TMAP 95/7 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration,

## 97 Octets”, otherwise not defined. C.2: Mandatory IF TMAP 95/8 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration,


## 130 Octets”, otherwise not defined.

Table 97: Unicast Media Receiver PACS Characteristic Support Requirements
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

| Item | Characteristics | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Sink Audio Locations characteristic | [2] | M | [4] BAP 9/2 |  |  |
| 2 | Multiple Sink Audio Locations | [2] 3.5.1.5 | O | [4] BAP 9/7 |  |  |

Table 98: Unicast Media Receiver Sink Audio Locations Values
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

|  | Item |  |  | Sink Audio Location Bit Values |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Front Left Sink Audio Location |  |  | [2] 3.5.1.2.1 |  |  | C.1 |  |  |
| 2 |  |  | Front Right Sink Audio Location |  |  | [2] 3.5.1.2.1 |  |  | C.1 |  |  |
| 3 |  |  | Front Right and Front Left Sink Audio Locations |  |  | [2] 3.5.1.2.1 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

|  | Item |  |  | Number |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 audio output |  |  | [2] 3.7 |  |  | M |  |  |
| 2 |  |  | 2 or more audio outputs |  |  | [2] 3.7 |  |  | O |  |  |

Table 100: Unicast Media Receiver Multi-Stream Configurations
Prerequisite: TMAP 1/4 “Unicast Media Receiver (UMR)”

|  | Item |  |  | Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Case 1: Multiple UMR audio sink devices each with a single ASE |  |  | [2] 3.7 |  |  | C.1 |  |  |
| 2 |  |  | Case 2: A single UMR audio sink device with multiple ASEs |  |  | [2] 3.7 |  |  | C.1, C.2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF TMAP 99/2 “2 or more audio outputs”, otherwise Excluded.

#### 3.2.3 Broadcast Media Receiver (BMR)


##### 3.2.3.1 BMR versions

Table 110: X.Y Versions
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0 |  |  | [2] |  |  | M |  |  |

Table 111: X.Y.Z Versions
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP v1.0.1 |  |  | [2][10] |  |  | C.1 |  |  |

C.1: Optional IF TMAP 110/1 “TMAP v1.0”, otherwise Excluded.

##### 3.2.3.2 BMR profile and service dependencies

Table 112: BMR Profile and Service Dependencies
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Common Audio Profile | [2] 3.1 | M | [3] CAP |  |  |
| 2 | Basic Audio Profile | [2] 3.1 | M | [4] BAP |  |  |

Table 113: Role Discovery Requirements
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Advertise Broadcast Media Receiver Support |  |  | [2] 3.4 |  |  | O |  |  |


##### 3.2.3.4 BMR requirements

Table 114: BMR Inter-Layer Dependency Role Requirements
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | External Roles | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| CAP Roles |  |  |  |  |  |  |
| 1 | CAP Acceptor | [2] 3.1 | M | [3] CAP 1/1 |  |  |
| 2 | CAP Commander | [2] 3.1 | O | [3] CAP 1/3 |  |  |
| Capture and Rendering Control |  |  |  |  |  |  |
| 3 | VCP Volume Renderer | [2] 3.1 | M | [3] CAP 6/5 |  |  |
| CAP Audio Stream Transition |  |  |  |  |  |  |
| 4 | BAP Broadcast Sink | [2] 3.1 | M | [4] BAP 1/4 |  |  |
| Context Type Support Requirements |  |  |  |  |  |  |
| 5 | Media (BAP Broadcast Sink) | [10] 3.5.2.1 | C.1 | [4] BAP 73/3 |  |  |

C.1: Mandatory IF TMAP 111/1 “TMAP v1.0.1”, otherwise Optional.
Table 115: Broadcast Media Receiver Codec Settings Requirements
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 75 Octets | [2] 3.5.2.1 | M | [4] BAP 68/11 |  |  |
| 2 | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms _ Frame Duration, 100 Octets | [2] 3.5.2.1 | M | [4] BAP 68/12 |  |  |
| 3 | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 90 Octets | [2] 3.5.2.1 | M | [4] BAP 68/13 |  |  |
| 4 | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms _ Frame Duration, 120 Octets | [2] 3.5.2.1 | M | [4] BAP 68/14 |  |  |
| 5 | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms _ Frame Duration, 117 Octets | [2] 3.5.2.1 | M | [4] BAP 68/15 |  |  |
| 6 | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms _ Frame Duration, 155 Octets | [2] 3.5.2.1 | M | [4] BAP 68/16 |  |  |
| 7 | 441 1 LC3: 44.1 kHz Sampling Frequency, _ 8.163 ms Frame Duration, 97 Octets | [2] 3.5.2.3 | O | [4] BAP 68/9 |  |  |
| 8 | 441 2 LC3: 44.1 kHz Sampling Frequency, _ 10.884 ms Frame Duration, 130 Octets | [2] 3.5.2.3 | O | [4] BAP 68/10 |  |  |

Table 116: Broadcast Media Receiver QoS Settings Requirements
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| Low Latency Media |  |  |  |  |  |  |
| 1 | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 _ _ Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 69/11 |  |  |
| 2 | 48 2 1 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 69/12 |  |  |
| 3 | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 _ _ Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 69/13 |  |  |
| 4 | 48 4 1 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 69/14 |  |  |
| 5 | 48 5 1 LC3: 7500 SDU Interval, unframed, _ _ 117 Max SDU Size, 4 RTN, 15 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 69/15 |  |  |
| 6 | 48 6 1 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 4 RTN, 20 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 69/16 |  |  |
| 7 | 441 1 1 LC3: 8163 SDU Interval, framed, 97 _ _ Max SDU Size, 4 RTN, 24 Max Transport Latency _ _ | [2] 3.5.2.3 | C.1 | [4] BAP 69/9 |  |  |
| 8 | 441 2 1 LC3: 10884 SDU Interval, framed, _ _ 130 Max SDU Size, 4 RTN, 31 Max Transport Latency _ _ | [2] 3.5.2.3 | C.2 | [4] BAP 69/10 |  |  |
| High Reliability Media |  |  |  |  |  |  |
| 9 | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 _ _ Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 70/11 |  |  |
| 10 | 48 2 2 LC3: 10000 SDU Interval, unframed, _ _ 100 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 70/12 |  |  |
| 11 | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 _ _ Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 70/13 |  |  |
| 12 | 48 4 2 LC3: 10000 SDU Interval, unframed, _ _ 120 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 70/14 |  |  |
| 13 | 48 5 2 LC3: 7500 SDU Interval, unframed, _ _ 117 Max SDU Size, 4 RTN, 50 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 70/15 |  |  |
| 14 | 48 6 2 LC3: 10000 SDU Interval, unframed, _ _ 155 Max SDU Size, 4 RTN, 65 Max Transport Latency _ _ | [2] 3.5.2.3 | M | [4] BAP 70/16 |  |  |


| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 15 | 441 1 2 LC3: 8163 SDU Interval, framed, 97 _ _ Max SDU Size, 4 RTN, 54 Max Transport Latency _ _ | [2] 3.5.2.3 | C.1 | [4] BAP 70/9 |  |  |
| 16 | 441 2 2 LC3: 10884 SDU Interval, framed, _ _ 130 Max SDU Size, 4 RTN, 60 Max Transport Latency _ _ | [2] 3.5.2.3 | C.2 | [4] BAP 70/10 |  |  |

C.1: Mandatory IF TMAP 115/7 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration,

## 97 Octets”, otherwise not defined. C.2: Mandatory IF TMAP 115/8 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration,


## 130 Octets”, otherwise not defined.

Table 117: BMR Codec Specific Audio Capability Support
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Settings | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Multiple Audio Locations | [2] 3.5.2. | O | [4] BAP 66/1 |  |  |
| 2 | Two Audio Channels | [2] 3.5.2 | O | [4] BAP 66/2 |  |  |

Table 118: BMR Audio Location Values
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Audio Location Values | Reference | Status |
| --- | --- | --- | --- |
| 1 | Front Left Audio Location | [2] 3.5.2.2 | C.1 |
| 2 | Front Right Audio Location | [2] 3.5.2.2 | C.1 |
| 3 | Front Right and Front Left Audio Locations | [2] 3.5.2.2 | C.1 |

C.1: Mandatory to support at least one.
Table 119: Number of Audio Outputs
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

|  | Item |  |  | Number |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 audio output |  |  | [2] 3.7 |  |  | M |  |  |
| 2 |  |  | 2 or more audio outputs |  |  | [2] 3.7 |  |  | O |  |  |

Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Characteristics | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | AC14: 1 BIS, Multiple Audio Channels/BIS, 1 Audio Stream | [2] | C.1 | [4] BAP 72/3 |  |  |

C.1: Mandatory IF TMAP 117/1 “Multiple Audio Locations” AND TMAP 117/2 “Two Audio Channels”,
otherwise not defined.
Table 121: Multi-Stream Configurations
Prerequisite: TMAP 1/6 “Broadcast Media Receiver (BMR)”

|  | Item |  |  | Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Case 5: Multiple BMR devices, each synchronized to a single BIS |  |  | [2] 3.7 |  |  | C.1 |  |  |
| 2 |  |  | Case 6: A single BMR device synchronized to multiple BISes |  |  | [2] 3.7 |  |  | C.1, C.2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF TMAP 119/2 “2 or more audio outputs”, otherwise Excluded.

## 4 Audio, Link Layer and HCI features


### 4.1 Audio, Link Layer and HCI features

Table 130: CAP Procedure Requirements
Prerequisite: TMAP 1/3 “Unicast Media Sender (UMS)” AND TMAP 1/5 “Broadcast Media Sender (BMS)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Unicast to Broadcast Handover Support (Initiator) | [2] 3.5.2.5 | M | [3] CAP 17/3 |  |  |
| 2 | Broadcast to Unicast Handover Support (Initiator) | [2] 3.5.2.5 | M | [3] CAP 17/4 |  |  |
| 3 | Unicast to Broadcast Handover Support (Commander) | [2] 3.5.2.5 | M | [3] CAP 27/2 |  |  |
| 4 | Broadcast to Unicast Handover Support (Commander) | [2] 3.5.2.5 | M | [3] CAP 27/3 |  |  |

Table 131: Link Layer and HCI Features
Prerequisite: TMAP 1/1 “Call Gateway (CG)” OR TMAP 1/2 “Call Terminal (CT)” OR TMAP 1/3 “Unicast Media Sender (UMS)” OR TMAP 1/4 “Unicast Media Receiver (UMR)” OR TMAP 1/5 “Broadcast Media Sender (BMS)” OR TMAP 1/6 “Broadcast Media Receiver (BMR)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE 2M PHY | [2] 3.2 | M | [8] LL 9/7 |  |  |
| 2 | No longer used. | N/A | N/A | N/A |  |  |


## 5 Content control


### 5.1 MCP Server function

Table 140: MCS Media Control Point Opcodes
Prerequisite: TMAP 1/1 “Call Gateway (CG)” OR TMAP 1/3 “Unicast Media Sender (UMS)” OR TMAP 1/5 “Broadcast Media Sender (BMS)”

| Item | Sub-procedure | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Play | [2] 3.6.1 | C.1 | [9] MCS 3/1 |  |  |
| 2 | Pause | [2] 3.6.1 | C.1 | [9] MCS 3/2 |  |  |
| 3 | Media Control Service | [2] 3.6.1 | O | [9] MCS 0b/1 |  |  |

C.1: Mandatory IF TMAP 140/3 “Media Control Service”, otherwise not defined.

## 6 Telephony and Media Audio Client and Server


### 6.1 Telephony and Media Audio Client requirements


#### 6.1.1 Client service requirements

Table 150: TMA Service Characteristic Support Requirements
Prerequisite: TMAP 1/7 “TMA Client”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP Role Characteristic |  |  | [2] 4.7.1 |  |  | M |  |  |


#### 6.1.2 Client GATT requirements

Table 151: GATT Requirements
Prerequisite: TMAP 1/7 “TMA Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Client over LE | [2] 3.8 | M | [5] GATT 1a/1 |  |  |
| 1a | GATT Client over BR/EDR | [2] 3.8 | C.3 | [5] GATT 1a/2 |  |  |
| 2 | Discover All Primary Services | [2] 3.8.1.3 | C.1 | [5] GATT 3/2 |  |  |
| 3 | Discover Primary Service by Service UUID | [2] 3.8.1.3 | C.1 | [5] GATT 3/3 |  |  |
| 4 | Discover All Characteristics of a Service | [2] 3.8.1.3 | C.2 | [5] GATT 3/5 |  |  |
| 5 | Discover Characteristics by UUID | [2] 3.8.1.3 | C.2 | [5] GATT 3/6 |  |  |
| 6 | Read Characteristic Value | [2] 3.8.1.3 | M | [5] GATT 3/8 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one. C.3: Mandatory IF TMAP 2/1a “Service TMAS supported over BR/EDR“, otherwise not defined.

### 6.2 Telephony and Media Audio Server requirements


#### 6.2.1 Service requirements

Table 152: Service Characteristic
Prerequisite: TMAP 1/8 “TMA Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | TMAP Role Characteristic |  |  | [2] 4.7.1 |  |  | M |  |  |

Prerequisite: TMAP 152/1 “TMAP Role Characteristic”

|  | Item |  |  | Profile Role Support |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Call Gateway Support |  |  | [2] 4.7.1.2 |  |  | C.1 |  |  |
| 2 |  |  | Call Terminal Support |  |  | [2] 4.7.1.2 |  |  | C.2 |  |  |
| 3 |  |  | Unicast Media Sender Support |  |  | [2] 4.7.1.2 |  |  | C.3 |  |  |
| 4 |  |  | Unicast Media Receiver Support |  |  | [2] 4.7.1.2 |  |  | C.4 |  |  |
| 5 |  |  | Broadcast Media Sender Support |  |  | [2] 4.7.1.2 |  |  | C.5 |  |  |
| 6 |  |  | Broadcast Media Receiver Support |  |  | [2] 4.7.1.2 |  |  | C.6 |  |  |

C.1: Mandatory IF TMAP 1/1 “Call Gateway (CG)”, otherwise Excluded. C.2: Mandatory IF TMAP 1/2 “Call Terminal (CT)”, otherwise Excluded. C.3: Mandatory IF TMAP 1/3 “Unicast Media Sender (UMS)”, otherwise Excluded. C.4: Mandatory IF TMAP 1/4 “Unicast Media Receiver (UMR)”, otherwise Excluded. C.5: Mandatory IF TMAP 1/5 “Broadcast Media Sender (BMS)”, otherwise Excluded. C.6: Mandatory IF TMAP 1/6 “Broadcast Media Receiver (BMR)”, otherwise Excluded.

#### 6.2.2 Server GATT requirements

Table 154: GATT Requirements
Prerequisite: TMAP 1/8 “TMA Server”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | GATT Server over LE | [2] 4.8 | M | [5] GATT 1a/3 |  |  |
| 2 | GATT Server over BR/EDR | [2] 4.8 | C.1 | [5] GATT 1a/4 |  |  |

C.1: Mandatory IF TMAP 2/1a “Service TMAS supported over BR/EDR”, otherwise not defined.

#### 6.2.3 SDP requirements

Table 155: SDP Requirements
Prerequisite: TMAP 1/8 “TMA Server” AND TMAP 2/1a “Service TMAS supported over BR/EDR”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | SDP record present for TMAP |  |  | [2] 4.9 |  |  | M |  |  |
| 2–4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |


### 6.3 GAP requirements

Table 156: GAP Requirements
Prerequisite: TMAP 1/7 “TMA Client” OR TMAP 1/8 “TMA Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |  | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE security mode 1 |  |  | [2] 4.8 |  |  | M |  |  | [1] GAP 25/1 OR GAP 35/1 |  |  |


## 7 References

[1] ICS Proforma for Generic Access Profile (GAP)
[2] Telephony and Media Audio Profile (TMAP) Specification, Version 1.0 or later
[3] ICS Proforma for Common Audio Profile (CAP)
[4] ICS Proforma for Basic Audio Profile (BAP)
[5] ICS Proforma for Generic Attribute Profile (GATT)
[6] ICS Proforma for Media Control Profile (MCP)
[7] ICS Proforma for Call Control Profile (CCP)
[8] ICS Proforma for Link Layer (LL)
[9] ICS Proforma for Media Control Service (MCS)
[10] Telephony and Media Audio Profile (TMAP) Specification, Version 1.0.1

## 8 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2022-06-14 | Adopted by the BoD on 2022-06-11. Prepared for initial publication. |
|  |  |  | p1r00–r07 |  |  | 2023-08-09 – 2024-04-08 | TSE 23095 (rating 2): Added BAP Unicast Client/Server role dependencies, items 14/7, 34/6, 74/6, and 94/5. TSE 23681 (rating 1): To support resolving SDP ILDs, removed references to LL and HCI parts of Core v5.2 or later from the References section, updated Table 155 by removing the ILD column, revising the Feature description for 155/1, and deleting 155/2, 155/3, and 155/4. Editorials throughout to align the document with the latest ICS conventions. TSE 24101 (rating 1): Removed the GMCS ICS from the References section. Updated 40/1 and 40/2 ILDs from GMCS to MCS. TSE 24549 (rating 1): Updated 131/2 to “No longer used” and removed associated conditional C.1. TSE 24613 (rating 2): Updated settings in Table 36. TSE 25098 (rating 2): Added 140/3 and updated the prerequisite for Table 140 and the C.1 conditional to clarify the MCS ILDs. |
| 1 |  |  | p1 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p2r00–r05 |  |  | 2024-11-11 – 2024-12-16 | TSE 26433 (rating 1): In Table 2, added Items 2/1a and 2/2a, updated the reference and status values for Items 2/1 and 2/2, deleted the existing conditional C.1, and added conditionals C.1–C.5. In Table 151, added Item 1a and conditional C.3. Updated conditional C.1 in Table 154. Updated the prerequisite for Table 155. TSE 26508 (rating 4): Per E25928, to support the “Conversational” and “Media” context types and TMAP v1.0.1, added Tables 11, 31, 51, 71, 91, and 111; added a “Context Type Support Requirement”" section to Tables 14, 34, 54, 74, 94, and 114; and added Telephony and Media Audio Profile (TMAP) Specification, Version 1.0.1, to the References section. |
| 2 |  |  | p2 |  |  | 2025-02-18 | Approved by BTI on 2025-02-09. TMAP v1.0.1 adopted by the BoD on 2024-02-11. Prepared for TCRL 2025-1 publication. |
|  |  |  | p2ed2 r00–r01 |  |  | 2025-02-12 – 2025-02-24 | TSE 26971 (rating 1): Updated “External Roles” value for 14/8, 34/7, 54/5, 74/7, 74/8, 94/6, and 114/5. Updated “Inter-layer Dependency” value for 94/6. |
|  |  |  | p2 edition 2 |  |  | 2025-03-14 | Approved by BTI on 2025-03-11. Prepared for edition 2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p3r00 |  |  | 2025-07-24 | TSE 27526 (rating 1): Updated entries for TMAP 3/1 and TMAP 3/2. Removed conditional C.1 for Table 3 and added note. |
| 3 |  |  | p3 |  |  | 2025-11-04 | Approved by BTI on 2025-09-29. Prepared for TCRL pkg101 publication. |
|  |  |  | p4r00–r02 |  |  | 2025-12-05 – 2025-12-26 | TSE 28120 (rating 1): Updated condition C.3 and added C.4 to Table 1 to replace GATT reference with a reverse ILD. TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 4 |  |  | p4 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Dejan Berec |  |  | Bluetooth SIG, Inc. |  |  |
| Tharon Hall |  |  | Bluetooth SIG, Inc. |  |  |
| Rasmus Abildgren |  |  | Bose Corporation |  |  |
| Łukasz Rymanowski |  |  | Codecoup |  |  |
| Andrew Estrada |  |  | Sony Group Corporation |  |  |
| Masahiko Seki |  |  | Sony Group Corporation |  |  |
| Akio Tanaka |  |  | Sony Group Corporation |  |  |
