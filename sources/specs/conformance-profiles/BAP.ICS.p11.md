# BAP.ICS.p11

> Source: PDF converted via PyMuPDF.

---

Basic Audio Profile (BAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: BAP.ICS.p11 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Generic Audio Working Group ▪ Published during TCRL: TCRL.pkg102
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
| 1 |  |  | Unicast Server |  |  | [1] 3.1 |  |  | C.1 |  |  |
| 2 |  |  | Unicast Client |  |  | [1] 3.1 |  |  | C.1 |  |  |
| 3 |  |  | Broadcast Source |  |  | [1] 3.1 |  |  | C.1 |  |  |
| 4 |  |  | Broadcast Sink |  |  | [1] 3.1 |  |  | C.1 |  |  |
| 5 |  |  | Scan Delegator |  |  | [1] 3.1 |  |  | C.1, C.2 |  |  |
| 6 |  |  | Broadcast Assistant |  |  | [1] 3.1 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF BAP 1/4 “Broadcast Sink”, otherwise Excluded.

### 2.2 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over LE |  |  | [1] 2.6 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over BR/EDR |  |  | [1] 2.6 |  |  | C.2, C.4 |  |  |

C.1: Excluded for this Profile IF CORE 41/1 “BR/EDR Core Configuration” OR CORE 40/1 “Core- Controller”. C.2: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”. C.3: Mandatory for this Profile. C.4: Optional for this Profile IF BAP 3/2 “GAP BR/EDR Host”, otherwise Excluded.

### 2.3 Host Configurations

Table 3: GAP Host Configuration

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |  | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | GAP LE Host |  |  | [1] 2.6 |  |  | M |  |  | [3] GAP 0b/2 |  |  |
| 2 |  |  | GAP BR/EDR Host |  |  | [1] 2.6 |  |  | O |  |  | [3] GAP 0b/1 |  |  |

Note: A GAP BR/EDR/LE Host will need to select BAP 3/1 and BAP 3/2.

### 2.4 LC3 Configurations

Table 93: LC3 Decoder Features

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Narrow Band (8 kHz) | [1] 3.5.2, 3.6.7, 3.8.2 | O | [11] LC3 5/1 |  |  |
| 2 | Wideband (16 kHz) | [1] 3.5.2, 3.6.7, 3.8.2 | C.1 | [11] LC3 5/2 |  |  |
| 3 | Semi-Superwideband (24 kHz) | [1] 3.5.2, 3.6.7, 3.8.2 | C.1 | [11] LC3 5/3 |  |  |
| 4 | Superwideband (32 kHz) | [1] 3.5.2, 3.6.7, 3.8.2 | O | [11] LC3 5/4 |  |  |


| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 5 | Full Band (44.1 kHz) | [1] 3.5.2, 3.6.7, 3.8.2 | O | [11] LC3 5/5 |  |  |
| 6 | Full Band (48 kHz) | [1] 3.5.2, 3.6.7, 3.8.2 | O | [11] LC3 5/6 |  |  |

C.1: Mandatory IF (BAP 1/1 “Unicast Server” AND BAP 8/1 “Audio Sink”) OR (BAP 1/2 “Unicast Client” AND BAP 29/1 “Audio Sink”) OR BAP 1/4 “Broadcast Sink”, otherwise Optional.
Table 94: LC3 Decoder Frame Interval

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 7.5 ms | [1] 3.5.2, 3.6.7, 3.8.2 | O | [11] LC3 6/1 |  |  |
| 2 | 10 ms | [1] 3.5.2, 3.6.7, 3.8.2 | C.1 | [11] LC3 6/2 |  |  |

C.1: Mandatory IF (BAP 1/1 “Unicast Server” AND BAP 8/1 “Audio Sink”) OR (BAP 1/2 “Unicast Client” AND BAP 29/1 “Audio Sink”) OR BAP 1/4 “Broadcast Sink”, otherwise Optional.
Table 95: LC3 Encoder Features

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Narrow Band (8 kHz) | [1] 3.5.2, 3.6.7, 3.7.1 | O | [11] LC3 3/1 |  |  |
| 2 | Wideband (16 kHz) | [1] 3.5.2, 3.6.7, 3.7.1 | C.1 | [11] LC3 3/2 |  |  |
| 3 | Semi-Superwideband (24 kHz) | [1] 3.5.2, 3.6.7, 3.7.1 | O | [11] LC3 3/3 |  |  |
| 4 | Superwideband (32 kHz) | [1] 3.5.2, 3.6.7, 3.7.1 | O | [11] LC3 3/4 |  |  |
| 5 | Full Band (44.1 kHz) | [1] 3.5.2, 3.6.7, 3.7.1 | O | [11] LC3 3/5 |  |  |
| 6 | Full Band (48 kHz) | [1] 3.5.2, 3.6.7, 3.7.1 | O | [11] LC3 3/6 |  |  |

C.1: Mandatory IF (BAP 1/1 “Unicast Server” AND BAP 8/2 “Audio Source”) OR (BAP 1/2 “Unicast Client” AND BAP 29/2 “Audio Source”) OR BAP 1/3 “Broadcast Source” , otherwise Optional.
Table 96: LC3 Encoder Frame Interval

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 7.5 ms | [1] 3.5.2, 3.6.7, 3.7.1 | O | [11] LC3 4/1 |  |  |
| 2 | 10 ms | [1] 3.5.2, 3.6.7, 3.7.1 | C.1 | [11] LC3 4/2 |  |  |

C.1: Mandatory IF (BAP 1/1 “Unicast Server” AND BAP 8/2 “Audio Source”) OR (BAP 1/2 “Unicast Client” AND BAP 29/2 “Audio Source”) OR BAP 1/3 “Broadcast Source” , otherwise Optional.

### 2.5 Unicast Server requirements

Table 4: Unicast Server, X.Y Versions
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2025-02-01. Withdrawn 2027-02-01.
Table 5: Unicast Server, X.Y.Z Versions
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0.1 |  |  | [9] |  |  | C.4 |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3 |  |  | Erratum 19096 |  |  | [8] |  |  | C.3 |  |  |
| 4 |  |  | BAP v1.0.2 |  |  | [10] |  |  | C.4 |  |  |

C.1–C.2: No longer used. C.3: Mandatory IF BAP 5/1 “BAP v1.0.1”, otherwise Excluded. C.4: Mandatory to support one and only one.
Table 6: Unicast Server: Services Included
Prerequisite: BAP 1/1 “Unicast Server”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | ASCS supported over BR/EDR | [1] 3.2 | C.1, C.3 | [4] ASCS 2/1 |  |  |
| 2 | ASCS supported over LE | [1] 3.2 | C.1 | [4] ASCS 2/2 |  |  |
| 3 | PACS supported over BR/EDR | [1] 3.2 | C.2, C.3 | [5] PACS 2/1 |  |  |
| 4 | PACS supported over LE | [1] 3.2 | C.2 | [5] PACS 2/2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one. C.3: Optional IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.
Table 7: Unicast Server: Feature Support
Prerequisite: BAP 1/1 “Unicast Server”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | ASCS UUID in AD | [1] 3.5.3 | M | N/A |  |  |
| 2 | Two Sink Audio Channels | [1] 4 | O | N/A |  |  |
| 3 | Two Source Audio Channels | [1] 4 | O | N/A |  |  |
| 4 | Autonomous Config Codec | [1] 5.6 | O | [4] ASCS 7/1 |  |  |
| 5 | Autonomous Receiver Start Ready | [1] 5.6 | C.1 | [4] ASCS 7/2 |  |  |
| 6 | Autonomous Disable | [1] 5.6 | O | [4] ASCS 7/3 |  |  |
| 7 | Autonomous Update Metadata | [1] 5.6 | O | [4] ASCS 7/4 |  |  |
| 8 | Autonomous Release | [1] 5.6 | O | [4] ASCS 7/5 |  |  |
| 9 | General Announcement | [1] 3.5.3 | C.2 | N/A |  |  |


## 10 Targeted Announcement [1] 3.5.3 C.2 N/A

C.1: Optional IF BAP 8/1 “Audio Sink”, otherwise not defined. C.2: Mandatory to support at least one.
Table 8: Audio Role Requirements: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Audio Sink |  |  | [1] 3.3 |  |  | C.1 |  |  |
| 2 |  |  | Audio Source |  |  | [1] 3.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.
Table 9: Published Audio Capabilities Service Characteristic Support Requirements
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sink PAC characteristic |  |  | [1] 3.5.2 |  |  | C.1 |  |  |
| 2 |  |  | Sink Audio Locations characteristic |  |  | [1] 3.5.3 |  |  | C.3 |  |  |
| 3 |  |  | Source PAC characteristic |  |  | [1] 3.5.2 |  |  | C.2 |  |  |
| 4 |  |  | Source Audio Locations characteristic |  |  | [1] 3.5.3 |  |  | C.4 |  |  |
| 5 |  |  | Available Audio Contexts characteristic |  |  | [1] 5.4 |  |  | M |  |  |
| 6 |  |  | Supported Audio Contexts characteristic |  |  | [1] 5.4 |  |  | M |  |  |
| 7 |  |  | Multiple Sink Audio Locations |  |  | [1] 4 |  |  | C.3 |  |  |
| 8 |  |  | Multiple Source Audio Locations |  |  | [1] 4 |  |  | C.4 |  |  |

C.1: Mandatory IF BAP 8/1 “Audio Sink”, otherwise Excluded. C.2: Mandatory IF BAP 8/2 “Audio Source”, otherwise Excluded. C.3: Optional IF BAP 8/1 “Audio Sink”, otherwise Excluded. C.4: Optional IF BAP 8/2 “Audio Source”, otherwise Excluded.
Table 9a: CIS Establishment Requirements: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sink ASE – Enabling, Source ASE – Enabling |  |  | [8] 5.6.9.1 |  |  | C.1 |  |  |
| 2 |  |  | Sink ASE – Enabling, Source ASE – QoS Configured |  |  | [8] 5.6.9.1 |  |  | C.1 |  |  |
| 3 |  |  | Sink ASE – Enabling, Source ASE – Not Bound |  |  | [8] 5.6.9.1 |  |  | C.2 |  |  |
| 4 |  |  | Sink ASE – QoS Configured, Source ASE – Enabling |  |  | [8] 5.6.9.1 |  |  | C.1 |  |  |
| 5 |  |  | Sink ASE – QoS Configured, Source ASE – QoS Configured |  |  | [8] 5.6.9.1 |  |  | C.3 |  |  |
| 6 |  |  | Sink ASE – QoS Configured, Source ASE – Not Bound |  |  | [8] 5.6.9.1 |  |  | C.4 |  |  |
| 7 |  |  | Sink ASE – Not bound, Source ASE – Enabling |  |  | [8] 5.6.9.1 |  |  | C.5 |  |  |
| 8 |  |  | Sink ASE – Not bound, Source ASE – QoS Configured |  |  | [8] 5.6.9.1 |  |  | C.6 |  |  |

C.1: Mandatory IF BAP 8/1 “Audio Sink” AND BAP 8/2 “Audio Source”, otherwise Excluded.
C.2: Mandatory IF BAP 8/1 “Audio Sink”, otherwise Excluded. C.3: Optional IF BAP 8/1 “Audio Sink” AND BAP 8/2 “Audio Source”, otherwise Excluded. C.4: Optional IF BAP 8/1 “Audio Sink”, otherwise Excluded. C.5: Mandatory IF BAP 8/2 “Audio Source”, otherwise Excluded. C.6: Optional IF BAP 8/2 “Audio Source”, otherwise Excluded.

#### 2.5.1 Audio Capability Support requirements

Table 10: Codec Specific Capabilities LTV Structures: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Supported Sampling Frequencies |  |  | [1] 4.3.1 |  |  | M |  |  |
| 2 |  |  | Supported Frame Durations |  |  | [1] 4.3.1 |  |  | M |  |  |
| 3 |  |  | Supported Octets per Codec Frame |  |  | [1] 4.3.1 |  |  | M |  |  |
| 4 |  |  | Supported Audio Channel Counts |  |  | [1] 4.3.1 |  |  | O |  |  |
| 5 |  |  | Supported Max Codec Frames Per SDU |  |  | [1] 4.3.1 |  |  | O |  |  |

Table 11: Metadata LTV Structures: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Preferred Audio Contexts _ _ |  |  | [1] 4.3.3 |  |  | O |  |  |
| 2 |  |  | Streaming Audio Contexts _ _ |  |  | [1] 4.3.3 |  |  | M |  |  |
| 3 |  |  | Vendor-specific Metadata |  |  | [1] 4.3.3 |  |  | O |  |  |

Table 12: Audio Capability Support Settings: Unicast Server is Audio Sink
Prerequisite: BAP 8/1 “Audio Sink”

|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, _ 26 Octets |  |  | [1] 3.5.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, _ 30 Octets |  |  | [1] 3.5.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 30 Octets |  |  | [1] 3.5.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 LC3: 16 kHz Sampling Frequency, 10 ms Frame _ Duration, 40 Octets |  |  | [1] 3.5.2 |  |  | M |  |  |
| 5 |  |  | 24 1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 45 Octets |  |  | [1] 3.5.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 LC3: 24 kHz Sampling Frequency, 10 ms Frame _ Duration, 60 Octets |  |  | [1] 3.5.2 |  |  | M |  |  |
| 7 |  |  | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 60 Octets |  |  | [1] 3.5.2 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms Frame _ Duration, 80 Octets |  |  | [1] 3.5.2 |  |  | C.6 |  |  |


|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 |  |  | 441 1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame _ Duration, 97 Octets |  |  | [1] 3.5.2 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame _ Duration, 130 Octets |  |  | [1] 3.5.2 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 75 Octets |  |  | [1] 3.5.2 |  |  | C.9 |  |  |
| 12 |  |  | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 100 Octets |  |  | [1] 3.5.2 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 90 Octets |  |  | [1] 3.5.2 |  |  | C.9 |  |  |
| 14 |  |  | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 120 Octets |  |  | [1] 3.5.2 |  |  | C.10 |  |  |
| 15 |  |  | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 117 Octets |  |  | [1] 3.5.2 |  |  | C.9 |  |  |
| 16 |  |  | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 155 Octets |  |  | [1] 3.5.2 |  |  | C.10 |  |  |
| 17 |  |  | Vendor-specific Codec Capability Setting |  |  | [1] 3.5.2 |  |  | O |  |  |

C.1: Optional IF BAP 93/1 “Narrow Band (8 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.2: Optional IF BAP 93/1 “Narrow Band (8 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.3: Optional IF BAP 93/2 “Wideband (16 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.4: Optional IF BAP 93/3 “Semi-Superwideband (24 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.5: Optional IF BAP 93/4 “Superwideband (32 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.6: Optional IF BAP 93/4 “Superwideband (32 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.7: Optional IF BAP 93/5 “Full Band (44.1 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.8: Optional IF BAP 93/5 “Full Band (44.1 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.9: Optional IF BAP 93/6 “Full Band (48 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.10: Optional IF BAP 93/6 “Full Band (48 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded.
Table 13: Audio Capability Support Settings: Unicast Server is Audio Source
Prerequisite: BAP 8/2 “Audio Source”

|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, _ 26 Octets |  |  | [1] 3.5.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, _ 30 Octets |  |  | [1] 3.5.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 30 Octets |  |  | [1] 3.5.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 LC3: 16 kHz Sampling Frequency, 10 ms Frame _ Duration, 40 Octets |  |  | [1] 3.5.2 |  |  | M |  |  |
| 5 |  |  | 24 1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 45 Octets |  |  | [1] 3.5.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 LC3: 24 kHz Sampling Frequency, 10 ms Frame _ Duration, 60 Octets |  |  | [1] 3.5.2 |  |  | C.5 |  |  |


|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 |  |  | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 60 Octets |  |  | [1] 3.5.2 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms Frame _ Duration, 80 Octets |  |  | [1] 3.5.2 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame _ Duration, 97 Octets |  |  | [1] 3.5.2 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame _ Duration, 130 Octets |  |  | [1] 3.5.2 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 75 Octets |  |  | [1] 3.5.2 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 100 Octets |  |  | [1] 3.5.2 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 90 Octets |  |  | [1] 3.5.2 |  |  | C.10 |  |  |
| 14 |  |  | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 120 Octets |  |  | [1] 3.5.2 |  |  | C.11 |  |  |
| 15 |  |  | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 117 Octets |  |  | [1] 3.5.2 |  |  | C.10 |  |  |
| 16 |  |  | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 155 Octets |  |  | [1] 3.5.2 |  |  | C.11 |  |  |
| 17 |  |  | Vendor-specific Codec Capability Setting |  |  | [1] 3.5.2 |  |  | O |  |  |

C.1: Optional IF BAP 95/1 “Narrow Band (8 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.2: Optional IF BAP 95/1 “Narrow Band (8 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.3: Optional IF BAP 95/2 “Wideband (16 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.4: Optional IF BAP 95/3 “Semi-Superwideband (24 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.5: Optional IF BAP 95/3 “Semi-Superwideband (24 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.6: Optional IF BAP 95/4 “Superwideband (32 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.7: Optional IF BAP 95/4 “Superwideband (32 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.8: Optional IF BAP 95/5 “Full Band (44.1 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.9: Optional IF BAP 95/5 “Full Band (44.1 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.10: Optional IF BAP 95/6 “Full Band (48 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.11: Optional IF BAP 95/6 “Full Band (48 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded.

#### 2.5.2 QoS Configuration requirements

Table 14: QoS Configuration: LC3 Low Latency: Unicast Server is Audio Sink
Prerequisite: BAP 8/1 “Audio Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 1 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 1 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | 16 2 1 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 5 |  |  | 24 1 1 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 1 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 1 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 5 RTN, 24 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 1 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 5 RTN, 31 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 1 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 14 |  |  | 48 4 1 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 15 |  |  | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |
| 16 |  |  | 48 6 1 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |

C.1: Optional IF BAP 12/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 12/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 12/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Mandatory IF BAP 12/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 12/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 12/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.7: Optional IF BAP 12/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.8: Optional IF BAP 12/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.9: Optional IF BAP 12/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.10: Optional IF BAP 12/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.11: Optional IF BAP 12/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded.
C.12: Optional IF BAP 12/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.13: Optional IF BAP 12/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.14: Optional IF BAP 12/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.15: Optional IF BAP 12/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Table 15: QoS Configuration: LC3 Low Latency: Unicast Server is Audio Source
Prerequisite: BAP 8/2 “Audio Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 1 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 1 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 1 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 5 |  |  | 24 1 1 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 1 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 1 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 5 RTN, 24 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 1 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 5 RTN, 31 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 1 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 14 |  |  | 48 4 1 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 15 |  |  | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |
| 16 |  |  | 48 6 1 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |

C.1: Optional IF BAP 13/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded.
C.2: Optional IF BAP 13/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 13/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Mandatory IF BAP 13/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 13/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 13/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.7: Optional IF BAP 13/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.8: Optional IF BAP 13/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.9: Optional IF BAP 13/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.10: Optional IF BAP 13/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.11: Optional IF BAP 13/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.12: Optional IF BAP 13/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.13: Optional IF BAP 13/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.14: Optional IF BAP 13/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.15: Optional IF BAP 13/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Table 16: QoS Configuration: LC3 High Reliability: Unicast Server is Audio Sink
Prerequisite: BAP 8/1 “Audio Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 2 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 2 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 2 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 2 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 5 |  |  | 24 1 2 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 2 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 7 |  |  | 32 1 2 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 2 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 |  |  | 441 1 2 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 13 RTN, 80 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 2 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 13 RTN, 85 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 12 |  |  | 48 2 2 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 14 |  |  | 48 4 2 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 15 |  |  | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 16 |  |  | 48 6 2 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |

C.1: Optional IF BAP 12/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 12/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 12/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 12/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 12/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 12/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.7: Optional IF BAP 12/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.8: Optional IF BAP 12/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.9: Optional IF BAP 12/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.10: Optional IF BAP 12/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.11: Optional IF BAP 12/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.12: Optional IF BAP 12/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.13: Optional IF BAP 12/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.14: Optional IF BAP 12/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Prerequisite: BAP 8/2 “Audio Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 2 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 2 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 2 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 2 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 5 |  |  | 24 1 2 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 6 |  |  | 24 2 2 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 7 |  |  | 32 1 2 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 8 |  |  | 32 2 2 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 9 |  |  | 441 1 2 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 13 RTN, 80 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 10 |  |  | 441 2 2 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 13 RTN, 85 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 11 |  |  | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 12 |  |  | 48 2 2 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 13 |  |  | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 14 |  |  | 48 4 2 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |
| 15 |  |  | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |
| 16 |  |  | 48 6 2 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.16 |  |  |

C.1: Optional IF BAP 13/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 13/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 13/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 13/4 “16_2 LC3: 16 kHz Sampling Frequency, 10 ms Frame Duration, 40 Octets”, otherwise Excluded. C.5: Optional IF BAP 13/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.6: Optional IF BAP 13/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded.
C.7: Optional IF BAP 13/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.8: Optional IF BAP 13/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.9: Optional IF BAP 13/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.10: Optional IF BAP 13/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.11: Optional IF BAP 13/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.12: Optional IF BAP 13/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.13: Optional IF BAP 13/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.14: Optional IF BAP 13/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.15: Optional IF BAP 13/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.16: Optional IF BAP 13/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Table 18: QoS Configuration: Vendor-Specific Codec: Unicast Server is Audio Sink
Prerequisite: BAP 8/1 “Audio Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Vendor-specific QoS Config Setting: Unicast Server is Audio Sink |  |  | [1] 5.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 12/17 “Vendor-specific Codec Capability Setting”, otherwise Excluded.
Table 19: QoS Configuration: Vendor-Specific Codec: Unicast Server is Audio Source
Prerequisite: BAP 8/2 “Audio Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Vendor-specific QoS Config Setting: Unicast Server is Audio Source |  |  | [1] 5.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 13/17 “Vendor-specific Codec Capability Setting”, otherwise Excluded.
Table 20: LC3 Audio Configuration: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

|  | Item |  |  | Audio Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AC 1: 1 Server, 1 Sink ASE, 1 Channel/Sink, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.1 |  |  | C.1 |  |  |
| 2 |  |  | AC 2: 1 Server, 1 Source ASE, 1 Channel/Source, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.2 |  |  | C.2 |  |  |
| 3 |  |  | AC 3: 1 Server, 1 Sink ASE, 1 Channel/Sink, 1 CIS, 2 Audio Streams |  |  | [1] 4.4.3 |  |  | C.3 |  |  |


|  | Item |  |  | Audio Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | AC 4: 1 Server, 1 Sink ASE, 2 Channels/Sink, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.4 |  |  | C.4 |  |  |
| 5 |  |  | AC 5: 1 Server, 1 Sink ASE, 1 Source ASE, 2 Channels/Sink, 1 Channel/Source, 1, CIS, 2 Audio Streams |  |  | [1] 4.4.5 |  |  | C.8 |  |  |
| 6 |  |  | AC 6i: 1 Server, 2 Sink ASEs, 1 Channel/Sink, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.6 |  |  | C.6 |  |  |
| 7 |  |  | AC 7i: 1 Server, 1 Sink ASE, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.8 |  |  | C.3 |  |  |
| 8 |  |  | AC 8i: 1 Server, 2 Sink ASEs, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 3 Audio Streams |  |  | [1] 4.4.10 |  |  | C.5 |  |  |
| 9 |  |  | AC 9i: 1 Server, 2 Source ASEs, 1 Channel/Source, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.12 |  |  | C.7 |  |  |
| 10 |  |  | AC 10: 1 Server, 1 Source ASE, 2 Channels/Source, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.14 |  |  | C.9 |  |  |
| 11 |  |  | AC 11i: 1 Server, 2 Sink ASEs, 2 Source ASEs, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 4 Audio Streams |  |  | [1] 4.4.15 |  |  | C.5 |  |  |

C.1: Mandatory IF BAP 8/1 “Audio Sink”, otherwise Excluded. C.2: Mandatory IF BAP 8/2 “Audio Source”, otherwise Excluded. C.3: Mandatory IF BAP 8/1 “Audio Sink” AND BAP 8/2 “Audio Source”, otherwise Excluded. C.4: Mandatory IF BAP 8/1 “Audio Sink” AND BAP 9/7 “Multiple Sink Audio Locations” AND BAP 7/2 “Two Sink Audio Channels”, otherwise Excluded. C.5: Optional IF BAP 8/1 “Audio Sink” AND BAP 8/2 “Audio Source”, otherwise Excluded. C.6: Mandatory IF BAP 8/1 “Audio Sink” AND BAP 9/7 “Multiple Sink Audio Locations”, otherwise Excluded. C.7: Mandatory IF BAP 8/2 “Audio Source” AND BAP 9/8 “Multiple Source Audio Locations”, otherwise Excluded. C.8: Optional IF BAP 8/1 “Audio Sink” AND BAP 8/2 “Audio Source” AND BAP 7/2 “Two Sink Audio Channels”, otherwise Excluded. C.9: Mandatory IF BAP 9/2 “Sink Audio Locations characteristic” AND BAP 7/3 “Two Source Audio Channels”, otherwise Excluded.

#### 2.5.3 Context Type requirements

Table 21: Supported Sink Context Requirements: Unicast Server
Prerequisite: BAP 8/1 “Audio Sink”

|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unspecified |  |  | [1] 3.5.2.1 |  |  | M |  |  |
| 2 |  |  | Conversational |  |  | [1] 5.5 |  |  | O |  |  |
| 3 |  |  | Media |  |  | [1] 5.5 |  |  | O |  |  |
| 4 |  |  | Game |  |  | [1] 5.5 |  |  | O |  |  |
| 5 |  |  | Instructional |  |  | [1] 5.5 |  |  | O |  |  |
| 6 |  |  | Voice assistants |  |  | [1] 5.5 |  |  | O |  |  |
| 7 |  |  | Live |  |  | [1] 5.5 |  |  | O |  |  |
| 8 |  |  | Sound effects |  |  | [1] 5.5 |  |  | O |  |  |
| 9 |  |  | Notifications |  |  | [1] 5.5 |  |  | O |  |  |


|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 |  |  | Ringtone |  |  | [1] 5.5 |  |  | O |  |  |
| 11 |  |  | Alerts |  |  | [1] 5.5 |  |  | O |  |  |
| 12 |  |  | Emergency Alarm |  |  | [1] 5.5 |  |  | O |  |  |

Table 22: Supported Source Context Requirements: Unicast Server
Prerequisite: BAP 8/2 “Audio Source”

|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unspecified |  |  | [1] 3.5.2.1 |  |  | M |  |  |
| 2 |  |  | Conversational |  |  | [1] 5.5 |  |  | O |  |  |
| 3 |  |  | Media |  |  | [1] 5.5 |  |  | O |  |  |
| 4 |  |  | Game |  |  | [1] 5.5 |  |  | O |  |  |
| 5 |  |  | Instructional |  |  | [1] 5.5 |  |  | O |  |  |
| 6 |  |  | Voice assistants |  |  | [1] 5.5 |  |  | O |  |  |
| 7 |  |  | Live |  |  | [1] 5.5 |  |  | O |  |  |
| 8 |  |  | Sound effects |  |  | [1] 5.5 |  |  | O |  |  |
| 9 |  |  | Notifications |  |  | [1] 5.5 |  |  | O |  |  |
| 10 |  |  | Ringtone |  |  | [1] 5.5 |  |  | O |  |  |
| 11 |  |  | Alerts |  |  | [1] 5.5 |  |  | O |  |  |
| 12 |  |  | Emergency Alarm |  |  | [1] 5.5 |  |  | O |  |  |


#### 2.5.4 GAP requirements

Table 23: GAP Requirements: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Peripheral | [1] 2.5 | M | [3] GAP 5/3 |  |  |
| 2 | Bondable mode (LE) | [1] 9.1.1 | M | [3] GAP 24/2 |  |  |
| 3 | Bondable mode (BR/EDR) | [1] 8.2.1 | C.2 | [3] GAP 1/7 |  |  |
| 4 | Bonding procedure | [1] 9.1.1 | M | [3] GAP 24/3 |  |  |
| 5 | LE security mode 1 | [1] 9.1.1 | M | [3] GAP 25/1 |  |  |
| 6 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 9.1.1 | M | [3] GAP 25/11 |  |  |
| 7 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 9.1.1 | O | [3] GAP 25/12 |  |  |
| 8 | Security mode 4, level 2 | [1] 9.2 | C.2 | [3] GAP 2/7c |  |  |
| 9 | 128-bit encryption key size capable (BR/EDR) | [1] 9.2 | C.2 | [3] GAP 2/13 |  |  |
| 10 | Minimum 128 Bit entropy key (LE) | [1] 9.1 | M | [3] GAP 25/13 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 11 | Derivation of BR/EDR Link Key from LE LTK | [1] 9.1.1, 9.2 | C.8 | [3] GAP 43/2a |  |  |
| 12 | Derivation of LE LTK from BR/EDR Link Key | [1] 9.2 | C.7 | [3] GAP 43/2b |  |  |
| 13 | CoD Major Service Class bit 14 | [1] 8.2.3 | C.2 | N/A |  |  |
| 14 | Limited discoverable mode | [1] 8.2.1 | C.6 | [3] GAP 1/2 |  |  |
| 15 | General discoverable mode (BR/EDR) | [1] 8.2.1 | C.6 | [3] GAP 1/3 |  |  |
| 16 | Initiation of general bonding | [1] 8.2.2 | C.2 | [3] GAP 3/5 |  |  |
| 17 | BR/EDR Secure Connections | [1] 9.2 | C.8 | N/A |  |  |
| 18 | LE Secure Connections | [1] 9.1 | C.7 | [3] GAP 27b/5 |  |  |
| 19 | Out of Band (Peripheral) | [1] 9.1 | C.7 | [3] GAP 27b/9 |  |  |
| 20 | Out-of-Band (BR/EDR) | [1] 9.2 | C.8 | [3] GAP 2/14 |  |  |
| 21 | LE security mode 1 level 4 | [1] 9.1.1 | O | [3] GAP 25/9 |  |  |

C.1: No longer used. C.2: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.3–C.5: No longer used. C.6: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.7: Mandatory to support at least one. C.8: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.
Table 24: No longer used

#### 2.5.5 LL requirements

Table 25: LL Requirements: Unicast Server
Prerequisite: BAP 1/1 “Unicast Server”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 3.4 | M | [7] LL 9/1 |  |  |
| 2 | LE Extended Advertising | [1] 3.4 | M | [7] LL 9/41 |  |  |
| 3 | Connected Isochronous Stream - Peripheral | [1] 3.4 | M | [7] LL 9/32 |  |  |


### 2.6 Unicast Client requirements

Table 26: Unicast Client, X.Y Versions
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2025-02-01. Withdrawn 2027-02-01.
Table 27: Unicast Client, X.Y.Z Versions
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 2 |  |  | BAP v1.0.1 |  |  | [9] |  |  | C.3 |  |  |
| 3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 4 |  |  | Erratum 19096 |  |  | [8][8] |  |  | C.2 |  |  |
| 5 |  |  | BAP v1.0.2 |  |  | [10] |  |  | C.3 |  |  |

C.1: No longer used. C.2: Mandatory IF BAP 27/2 “BAP v1.0.1”, otherwise Excluded. C.3: Mandatory to support one and only one.
Table 28: Unicast Client: Client Services Support
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Discover ASCS over BR/EDR |  |  | [1] 3.2 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Discover ASCS over LE |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 3 |  |  | Discover PACS over BR/EDR |  |  | [1] 3.2 |  |  | C.2, C.3 |  |  |
| 4 |  |  | Discover PACS over LE |  |  | [1] 3.2 |  |  | C.2 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one. C.3: Optional IF BAP 3/2 “GAP BR/EDR Host”, otherwise Excluded.
Table 29: Audio Role Requirements: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Audio Sink |  |  | [1] 3.3 |  |  | C.1 |  |  |
| 2 |  |  | Audio Source |  |  | [1] 3.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.
Table 30: Feature Support: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Multiple Server Support |  |  | [1] 4.4 |  |  | O |  |  |
| 2 |  |  | Multiple Audio Locations |  |  | [1] 4 |  |  | O |  |  |
| 3 |  |  | Two Audio Channels |  |  | [1] 4 |  |  | O |  |  |

Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sink ASE Characteristic discovery |  |  | [1] 3.6.4 |  |  | C.2 |  |  |
| 2 |  |  | Source ASE Characteristic discovery |  |  | [1] 3.6.4 |  |  | C.1 |  |  |
| 3 |  |  | ASE Control Point Characteristic discovery |  |  | [1] 3.6.4 |  |  | M |  |  |
| 4 |  |  | Audio Stream Control Service Discovery |  |  | [1] 3.6.3 |  |  | M |  |  |
| 5 |  |  | Audio Stream Control Service Characteristic Discovery |  |  | [1] 3.6.3 |  |  | M |  |  |
| 6 |  |  | Sink ASE ID Discovery _ |  |  | [1] 5.3 |  |  | C.2 |  |  |
| 7 |  |  | Source ASE ID Discovery _ |  |  | [1] 5.3 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 29/1 “Audio Sink”, otherwise Excluded. C.2: Mandatory IF BAP 29/2 “Audio Source”, otherwise Excluded.
Table 32: Published Audio Capabilities Service Characteristic Support Requirements
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sink PAC characteristic |  |  | [1] 3.6.4 |  |  | C.1 |  |  |
| 2 |  |  | Sink Audio Locations characteristic |  |  | [1] 3.6.4 |  |  | C.1 |  |  |
| 3 |  |  | Source PAC characteristic |  |  | [1] 3.6.4 |  |  | C.2 |  |  |
| 4 |  |  | Source Audio Locations characteristic |  |  | [1] 3.6.4 |  |  | C.2 |  |  |
| 5 |  |  | Available Audio Contexts characteristic |  |  | [1] 3.6.4 |  |  | M |  |  |
| 6 |  |  | Supported Audio Contexts characteristic |  |  | [1] 3.6.4 |  |  | M |  |  |
| 7 |  |  | Published Audio Capabilities Service Discovery |  |  | [1] 3.6.3 |  |  | M |  |  |
| 8 |  |  | Published Audio Capabilities Service Characteristic Discovery |  |  | [1] 3.6.3 |  |  | M |  |  |
| 9 |  |  | Supported Audio Contexts discovery |  |  | [1] 5.4 |  |  | O |  |  |
| 10 |  |  | Available Audio Contexts discovery |  |  | [1] 5.5 |  |  | M |  |  |

C.1: Mandatory IF BAP 29/2 “Audio Source”, otherwise Excluded. C.2: Mandatory IF BAP 29/1 “Audio Sink”, otherwise Excluded.
Table 33: ASE Control Operations Requirements: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Codec configuration |  |  | [1] 5.6.1 |  |  | M |  |  |
| 2 |  |  | QoS configuration |  |  | [1] 5.6.2 |  |  | M |  |  |
| 3 |  |  | Enabling an ASE |  |  | [1] 5.6.3 |  |  | M |  |  |
| 4 |  |  | Receiver Start Ready |  |  | [1] 5.6.3.2 |  |  | C.1 |  |  |
| 5 |  |  | Update Metadata |  |  | [1] 5.6.4 |  |  | O |  |  |
| 6 |  |  | Disabling an ASE |  |  | [1] 5.6.5 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 |  |  | Receiver Stop Ready |  |  | [1] 5.6.5.1 |  |  | C.1 |  |  |
| 8 |  |  | Releasing an ASE |  |  | [1] 5.6.6 |  |  | M |  |  |

C.1: Mandatory IF BAP 29/1 “Audio Sink”, otherwise Excluded.
Table 33a: CIS Establishment Requirements: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sink ASE – Enabling, Source ASE – Enabling |  |  | [8] 5.6.9.2 |  |  | C.1 |  |  |
| 2 |  |  | Sink ASE – Enabling, Source ASE – QoS Configured |  |  | [8] 5.6.9.2 |  |  | C.1 |  |  |
| 3 |  |  | Sink ASE – Enabling, Source ASE – Not Bound |  |  | [8] 5.6.9.2 |  |  | C.5 |  |  |
| 4 |  |  | Sink ASE – QoS Configured, Source ASE – Enabling |  |  | [8] 5.6.9.2 |  |  | C.1 |  |  |
| 5 |  |  | Sink ASE – QoS Configured, Source ASE – QoS Configured |  |  | [8] 5.6.9.2 |  |  | C.3 |  |  |
| 6 |  |  | Sink ASE – QoS Configured, Source ASE – Not Bound |  |  | [8] 5.6.9.2 |  |  | C.6 |  |  |
| 7 |  |  | Sink ASE – Not bound, Source ASE – Enabling |  |  | [8] 5.6.9.2 |  |  | C.2 |  |  |
| 8 |  |  | Sink ASE –Not bound, Source ASE – QoS Configured |  |  | [8] 5.6.9.2 |  |  | C.4 |  |  |

C.1: Mandatory to support at least one IF BAP 29/1 “Audio Sink” AND BAP 29/2 “Audio Source”, otherwise Excluded. C.2: Mandatory IF BAP 29/1 “Audio Sink”, otherwise Excluded. C.3: Optional IF BAP 29/1 “Audio Sink” AND BAP 29/2 “Audio Source”, otherwise Excluded. C.4: Optional IF BAP 29/1 “Audio Sink”, otherwise Excluded. C.5: Mandatory IF BAP 29/2 “Audio Source”, otherwise Excluded. C.6: Optional IF BAP 29/2 “Audio Source”, otherwise Excluded.

#### 2.6.1 Audio Capability Support requirements

Table 34: Codec Specific Configuration LTV Structures: Unicast Client
Prerequisite: BAP 29/1 “Audio Sink”

|  | Item |  |  | LTV Structure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sampling Frequency _ |  |  | [1] 4.3.2 |  |  | M |  |  |
| 2 |  |  | Frame Duration _ |  |  | [1] 4.3.2 |  |  | M |  |  |
| 3 |  |  | Audio Channel Allocation _ _ |  |  | [1] 4.3.2 |  |  | O |  |  |
| 4 |  |  | Octets Per Codec Frame _ _ _ |  |  | [1] 4.3.2 |  |  | M |  |  |
| 5 |  |  | Codec Frame Blocks Per SDU _ _ _ _ |  |  | [1] 4.3.2 |  |  | O |  |  |

Table 35: Metadata LTV Structures: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Streaming Audio Contexts _ _ |  |  | [1] 4.3.3 |  |  | M |  |  |
| 2 |  |  | Vendor-specific Metadata |  |  | [1] 4 |  |  | O |  |  |

Prerequisite: BAP 29/1 “Audio Sink”

|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, _ 26 Octets |  |  | [1] 3.6.7 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, _ 30 Octets |  |  | [1] 3.6.7 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 30 Octets |  |  | [1] 3.6.7 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 LC3: 16 kHz Sampling Frequency, 10 ms Frame _ Duration, 40 Octets |  |  | [1] 3.6.7 |  |  | M |  |  |
| 5 |  |  | 24 1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 45 Octets |  |  | [1] 3.6.7 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 LC3: 24 kHz Sampling Frequency, 10 ms Frame _ Duration, 60 Octets |  |  | [1] 3.6.7 |  |  | C.11 |  |  |
| 7 |  |  | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 60 Octets |  |  | [1] 3.6.7 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms Frame _ Duration, 80 Octets |  |  | [1] 3.6.7 |  |  | C.6 |  |  |
| 9 |  |  | 441 1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame _ Duration, 97 Octets |  |  | [1] 3.6.7 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame _ Duration, 130 Octets |  |  | [1] 3.6.7 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 75 Octets |  |  | [1] 3.6.7 |  |  | C.9 |  |  |
| 12 |  |  | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 100 Octets |  |  | [1] 3.6.7 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 90 Octets |  |  | [1] 3.6.7 |  |  | C.9 |  |  |
| 14 |  |  | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 120 Octets |  |  | [1] 3.6.7 |  |  | C.10 |  |  |
| 15 |  |  | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 117 Octets |  |  | [1] 3.6.7 |  |  | C.9 |  |  |
| 16 |  |  | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 155 Octets |  |  | [1] 3.6.7 |  |  | C.10 |  |  |
| 17 |  |  | Vendor-specific Codec Config Setting |  |  | [1] 3.6.7 |  |  | O |  |  |

C.1: Optional IF BAP 93/1 “Narrow Band (8 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.2: Optional IF BAP 93/1 “Narrow Band (8 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.3: Optional IF BAP 93/2 “Wideband (16 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.4: Optional IF BAP 93/3 “Semi-Superwideband (24 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.5: Optional IF BAP 93/4 “Superwideband (32 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.6: Optional IF BAP 93/4 “Superwideband (32 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.7: Optional IF BAP 93/5 “Full Band (44.1 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.8: Optional IF BAP 93/5 “Full Band (44.1 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.9: Optional IF BAP 93/6 “Full Band (48 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.10: Optional IF BAP 93/6 “Full Band (48 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded.
C.11: Optional IF BAP 93/3 “Semi-Superwideband (24 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded.
Table 37: Audio Capability Configuration Support Settings: Unicast Client is Audio Source
Prerequisite: BAP 29/2 “Audio Source”

|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, _ 26 Octets |  |  | [1] 3.6.7 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, _ 30 Octets |  |  | [1] 3.6.7 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 30 Octets |  |  | [1] 3.6.7 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 LC3: 16 kHz Sampling Frequency, 10 ms Frame _ Duration, 40 Octets |  |  | [1] 3.6.7 |  |  | M |  |  |
| 5 |  |  | 24 1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 45 Octets |  |  | [1] 3.6.7 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 LC3: 24 kHz Sampling Frequency, 10 ms Frame _ Duration, 60 Octets |  |  | [1] 3.6.7 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 60 Octets |  |  | [1] 3.6.7 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms Frame _ Duration, 80 Octets |  |  | [1] 3.6.7 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame _ Duration, 97 Octets |  |  | [1] 3.6.7 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame _ Duration, 130 Octets |  |  | [1] 3.6.7 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 75 Octets |  |  | [1] 3.6.7 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 100 Octets |  |  | [1] 3.6.7 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 90 Octets |  |  | [1] 3.6.7 |  |  | C.10 |  |  |
| 14 |  |  | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 120 Octets |  |  | [1] 3.6.7 |  |  | C.11 |  |  |
| 15 |  |  | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 117 Octets |  |  | [1] 3.6.7 |  |  | C.10 |  |  |
| 16 |  |  | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 155 Octets |  |  | [1] 3.6.7 |  |  | C.11 |  |  |
| 17 |  |  | Vendor-specific Codec Config Setting: Unicast Client is Audio Source |  |  | [1] 3.6.7 |  |  | O |  |  |

C.1: Optional IF BAP 95/1 “Narrow Band (8 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.2: Optional IF BAP 95/1 “Narrow Band (8 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.3: Optional IF BAP 95/2 “Wideband (16 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.4: Optional IF BAP 95/3 “Semi-Superwideband (24 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.5: Optional IF BAP 95/3 “Semi-Superwideband (24 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded.
C.6: Optional IF BAP 95/4 “Superwideband (32 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.7: Optional IF BAP 95/4 “Superwideband (32 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.8: Optional IF BAP 95/5 “Full Band (44.1 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.9: Optional IF BAP 95/5 “Full Band (44.1 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.10: Optional IF BAP 95/6 “Full Band (48 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.11: Optional IF BAP 95/6 “Full Band (48 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded.
Table 38: QoS Configuration: LC3 Low Latency: Unicast Client is Audio Sink
Prerequisite: BAP 29/1 “Audio Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 1 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 1 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 1 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 5 |  |  | 24 1 1 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 1 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 1 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 5 RTN, 24 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 1 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 5 RTN, 31 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 1 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 14 |  |  | 48 4 1 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 15 |  |  | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |
| 16 |  |  | 48 6 1 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |

C.1: Optional IF BAP 36/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 36/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded.
C.3: Optional IF BAP 36/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Mandatory IF BAP 36/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 36/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 36/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.7: Optional IF BAP 36/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.8: Optional IF BAP 36/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.9: Optional IF BAP 36/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.10: Optional IF BAP 36/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.11: Optional IF BAP 36/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.12: Optional IF BAP 36/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.13: Optional IF BAP 36/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.14: Optional IF BAP 36/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.15: Optional IF BAP 36/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Table 39: QoS Configuration: LC3 Low Latency: Unicast Client is Audio Source
Prerequisite: BAP 29/2 “Audio Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 1 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 1 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 1 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 5 |  |  | 24 1 1 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 1 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 1 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 5 RTN, 24 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 |  |  | 441 2 1 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 5 RTN, 31 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 1 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 14 |  |  | 48 4 1 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 15 |  |  | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 5 RTN, 15 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |
| 16 |  |  | 48 6 1 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 5 RTN, 20 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |

C.1: Optional IF BAP 37/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 37/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 37/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Mandatory IF BAP 37/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 37/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 37/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.7: Optional IF BAP 37/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.8: Optional IF BAP 37/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.9: Optional IF BAP 37/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.10: Optional IF BAP 37/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.11: Optional IF BAP 37/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.12: Optional IF BAP 37/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.13: Optional IF BAP 37/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.14: Optional IF BAP 37/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.15: Optional IF BAP 37/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Prerequisite: BAP 29/1 “Audio Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 2 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 2 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 2 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 2 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.16 |  |  |
| 5 |  |  | 24 1 2 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 2 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 2 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 2 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 2 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 13 RTN, 80 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 2 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 13 RTN, 85 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 2 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 14 |  |  | 48 4 2 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 15 |  |  | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |
| 16 |  |  | 48 6 2 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |

C.1: Optional IF BAP 36/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 36/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 36/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 36/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 36/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 36/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded.
C.7: Optional IF BAP 36/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.8: Mandatory IF BAP 36/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.9: Mandatory IF BAP 36/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.10: Mandatory IF BAP 36/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.11: Mandatory IF BAP 36/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.12: Mandatory IF BAP 36/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.13: Mandatory IF BAP 36/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.14: Mandatory IF BAP 36/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.15: Mandatory IF BAP 36/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded. C.16: Optional IF BAP 36/4 “16_2 LC3: 16 kHz Sampling Frequency, 10 ms Frame Duration, 40 Octets”, otherwise Excluded.
Table 41: QoS Configuration: LC3 High Reliability: Unicast Client is Audio Source
Prerequisite: BAP 29/2 “Audio Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 2 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 2 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 2 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 2 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.15 |  |  |
| 5 |  |  | 24 1 2 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 2 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.16 |  |  |
| 7 |  |  | 32 1 2 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 2 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 9 |  |  | 441 1 2 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 13 RTN, 80 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 2 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 13 RTN, 85 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | 48 2 2 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 13 RTN, 95 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 14 |  |  | 48 4 2 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 15 |  |  | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 13 RTN, 75 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 16 |  |  | 48 6 2 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 13 RTN, 100 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |

C.1: Optional IF BAP 37/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 37/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 37/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 37/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 37/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 37/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.7: Mandatory IF BAP 37/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.8: Mandatory IF BAP 37/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.9: Mandatory IF BAP 37/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.10: Mandatory IF BAP 37/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.11: Mandatory IF BAP 37/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.12: Mandatory IF BAP 37/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.13: Mandatory IF BAP 37/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.14: Mandatory IF BAP 37/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded. C.15: Optional IF BAP 37/4 “16_2 LC3: 16 kHz Sampling Frequency, 10 ms Frame Duration, 40 Octets”, otherwise Excluded. C.16: Optional IF BAP 37/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded.
Prerequisite: BAP 29/1 “Audio Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Vendor-specific QoS Config Setting: Unicast Client is Audio Sink |  |  | [1] 5.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 36/17 “Vendor-specific Codec Config Setting”, otherwise Excluded.
Table 43: QoS Configuration: Vendor-Specific Codec: Unicast Client is Audio Source
Prerequisite: BAP 29/2 “Audio Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Vendor-specific QoS Config Setting: Unicast Client is Audio Source |  |  | [1] 5.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 37/17 “Vendor-specific Codec Config Setting: Unicast Client is Audio Source”, otherwise Excluded.
Table 44: LC3 Audio Configuration: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

|  | Item |  |  | Audio Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AC 1: 1 Server, 1 Sink ASE, 1 Channel/Sink, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.1 |  |  | C.1 |  |  |
| 2 |  |  | AC 2: 1 Server, 1 Source ASE, 1 Channel/Source, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.2 |  |  | C.2 |  |  |
| 3 |  |  | AC 3: 1 Server, 1 Sink ASE, 1 Channel/Sink, 1 CIS, 2 Audio Streams |  |  | [1] 4.4.3 |  |  | C.3 |  |  |
| 4 |  |  | AC 4: 1 Server, 1 Sink ASE, 2 Channels/Sink, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.4 |  |  | C.4 |  |  |
| 5 |  |  | AC 5: 1 Server, 1 Sink ASE, 1 Source ASE, 2 Channels/Sink, 1 Channel/Source, 1, CIS, 2 Audio Streams |  |  | [1] 4.4.5 |  |  | C.7 |  |  |
| 6 |  |  | AC 6i: 1 Server, 2 Sink ASEs, 1 Channel/Sink, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.6 |  |  | C.1 |  |  |
| 7 |  |  | AC 6ii: 2 Servers, 2 Sink ASEs, 1 Channel/Sink, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.7 |  |  | C.1 |  |  |
| 8 |  |  | AC 7i: 1 Server, 1 Sink ASE, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.8 |  |  | C.5 |  |  |
| 9 |  |  | AC 7ii: 2 Servers, 1 Sink ASE, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.9 |  |  | C.3 |  |  |
| 10 |  |  | AC 8i: 1 Server, 2 Sink ASEs, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 3 Audio Streams |  |  | [1] 4.4.10 |  |  | C.5, C.8 |  |  |
| 11 |  |  | AC 8ii: 2 Servers, 2 Sink ASEs, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 3 Audio Streams |  |  | [1] 4.4.11 |  |  | C.5, C.9 |  |  |
| 12 |  |  | AC 9i: 1 Server, 2 Source ASEs, 1 Channel/Source, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.12 |  |  | C.2 |  |  |
| 13 |  |  | AC 9ii: 2 Servers, 2 Source ASEs, 1 Channel/Source, 2 CISes, 2 Audio Streams |  |  | [1] 4.4.13 |  |  | C.2 |  |  |


|  | Item |  |  | Audio Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 |  |  | AC 10: 1 Server, 1 Source ASE, 2 Channels/Source, 1 CIS, 1 Audio Stream |  |  | [1] 4.4.14 |  |  | C.6 |  |  |
| 15 |  |  | AC 11i: 1 Server, 2 Sink ASEs, 2 Source ASEs, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 4 Audio Streams |  |  | [1] 4.4.15 |  |  | C.5, C.10 |  |  |
| 16 |  |  | AC 11ii: 2 Servers, 2 Sink ASEs, 2 Source ASEs, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 4 Audio Streams |  |  | [1] 4.4.16 |  |  | C.5, C.11 |  |  |

C.1: Mandatory IF BAP 29/2 “Audio Source”, otherwise Excluded. C.2: Mandatory IF BAP 29/1 “Audio Sink”, otherwise Excluded. C.3: Mandatory IF BAP 29/1 “Audio Sink” AND BAP 29/2 “Audio Source”, otherwise Excluded. C.4: Optional IF BAP 29/2 “Audio Source” AND BAP 30/3 “Two Audio Channels”, otherwise Excluded. C.5: Optional IF BAP 29/1 “Audio Sink” AND BAP 29/2 “Audio Source”, otherwise Excluded. C.6: Optional IF BAP 29/1 “Audio Sink” AND BAP 30/3 “Two Audio Channels”, otherwise Excluded. C.7: Optional IF BAP 29/1 “Audio Sink” AND BAP 29/2 “Audio Source” AND BAP 30/3 “Two Audio Channels”, otherwise Excluded. C.8: Mandatory IF BAP 44/11 “AC 8ii: 2 Servers, 2 Sink ASEs, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 3 Audio Streams”, otherwise Excluded. C.9: Mandatory IF BAP 44/10 “AC 8i: 1 Server, 2 Sink ASEs, 1 Source ASE, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 3 Audio Streams”, otherwise Excluded. C.10: Mandatory IF BAP 44/16 “AC 11ii: 2 Servers, 2 Sink ASEs, 2 Source ASEs, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 4 Audio Streams”, otherwise Excluded. C.11: Mandatory IF BAP 44/15 “AC 11i: 1 Server, 2 Sink ASEs, 2 Source ASEs, 1 Channel/Sink, 1 Channel/Source, 2 CISes, 4 Audio Streams”, otherwise Excluded.

#### 2.6.2 GATT requirements

Table 45: GATT Requirements: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Discover All Primary Services | [1] 3.6.2 | C.1 | [2] GATT 3/2 |  |  |
| 2 | Discover Primary Service by Service UUID | [1] 3.6.2 | C.1 | [2] GATT 3/3 |  |  |
| 3 | Find Included Services | [1] 3.6.2 | O | [2] GATT 3/4 |  |  |
| 4 | Discover All Characteristics of a Service | [1] 3.6.2 | C.2 | [2] GATT 3/5 |  |  |
| 5 | Discover Characteristics by UUID | [1] 3.6.2 | C.2 | [2] GATT 3/6 |  |  |
| 6 | Discover All Characteristic Descriptors | [1] 3.6.2 | M | [2] GATT 3/7 |  |  |
| 7 | Read Characteristic Value | [1] 3.5.2 | M | [2] GATT 3/8 |  |  |
| 8 | Write Without Response | [1] 3.6.2 | M | [2] GATT 3/12 |  |  |
| 9 | Write Characteristic Value | [1] 3.6.2 | M | [2] GATT 3/14 |  |  |
| 10 | Write Long Characteristic Value | [1] 3.6.2 | M | [2] GATT 3/15 |  |  |
| 11 | Single Notification | [1] 3.6.2 | M | [2] GATT 3/17 |  |  |
| 12 | Read Characteristic Descriptor | [1] 3.6.2 | M | [2] GATT 3/19 |  |  |
| 13 | Write Characteristic Descriptor | [1] 3.6.2 | M | [2] GATT 3/21 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 14 | Exchange MTU | [1] 3.6.2 | M | [2] GATT 3/1 |  |  |
| 15 | GATT Client over BR/EDR | [1] 2.3 | C.3 | [2] GATT 1a/2 |  |  |
| 16 | GATT Client over LE | [1] 2.3 | M | [2] GATT 1a/1 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one. C.3: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.

#### 2.6.3 GAP requirements

Table 46: GAP Requirements: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Central | [1] 2.5 | M | [3] GAP 5/4 |  |  |
| 2 | Bondable mode (LE) | [1] 9.1.2 | M | [3] GAP 34/2 |  |  |
| 3 | Bonding procedure | [1] 9.1.2 | M | [3] GAP 34/3 |  |  |
| 4 | LE security mode 1 | [1] 9.1.2 | M | [3] GAP 35/1 |  |  |
| 5 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 9.1.2 | M | [3] GAP 35/11 |  |  |
| 6 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 9.1.2 | O | [3] GAP 35/12 |  |  |
| 7 | Security mode 4, level 2 | [1] 9.2 | C.3 | [3] GAP 2/7c |  |  |
| 8 | 128-bit encryption key size capable (BR/EDR) | [1] 9.2 | C.3 | [3] GAP 2/13 |  |  |
| 9 | Minimum 128 Bit entropy key (LE) | [1] 9.1 | M | [3] GAP 35/13 |  |  |
| 10 | Derivation of BR/EDR Link Key from LE LTK | [1] 9.1.2, 9.2 | C.7 | [3] GAP 41/2a |  |  |
| 11 | Derivation of LE LTK from BR/EDR Link Key | [1] 9.2 | C.6 | [3] GAP 41/2b |  |  |
| 12 | CoD Major Service Class bit 14 | [1] 8.2.3 | C.3 | N/A |  |  |
| 13 | BR/EDR Secure Connections | [1] 9.2 | C.7 | N/A |  |  |
| 14 | LE Secure Connections | [1] 9.1 | C.6 | [3] GAP 37b/5 |  |  |
| 15 | Out of Band (Central) | [1] 9.1 | C.6 | [3] GAP 37b/9 |  |  |
| 16 | Out-of-Band (BR/EDR) | [1] 9.2 | C.7 | [3] GAP 2/14 |  |  |
| 17 | LE security mode 1 level 4 | [1] 9.1.2 | O | [3] GAP 35/9 |  |  |

C.1–C.2: No longer used. C.3: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.4–C.5: No longer used. C.6: Mandatory to support at least one. C.7: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.

#### 2.6.4 LL requirements

Table 48: LL Requirements: Unicast Client
Prerequisite: BAP 1/2 “Unicast Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 3.4 | M | [7] LL 9/1 |  |  |
| 2 | LE Extended Advertising | [1] 3.4 | M | [7] LL 9/41 |  |  |
| 3 | Connected Isochronous Stream - Central | [1] 3.4 | M | [7] LL 9/31 |  |  |


### 2.7 Broadcast Source requirements

Table 49: Broadcast Source, X.Y Versions
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2025-02-01. Withdrawn 2027-02-01.
Table 50: Broadcast Source, X.Y.Z Versions
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0.1 |  |  | [9][9] |  |  | C.1 |  |  |
| 2 |  |  | BAP v1.0.2 |  |  | [10] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one.
Table 51: Broadcast Source: Service Support Requirements
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcast Audio Stream Metadata Update |  |  | [1] 6.3.3 |  |  | O |  |  |
| 2 |  |  | Broadcast Audio Stream Reconfiguration |  |  | [1] 6.3.1 |  |  | O |  |  |
| 3 |  |  | Broadcast Audio Stream Establishment |  |  | [1] 6.3.2 |  |  | M |  |  |
| 4 |  |  | Broadcast Audio Stream Disable |  |  | [1] 6.3.4 |  |  | M |  |  |
| 5 |  |  | Broadcast Audio Stream Release |  |  | [1] 6.3.5 |  |  | M |  |  |
| 6 |  |  | Broadcast Audio Announcement Service UUID |  |  | [1] 3.7.2.1 |  |  | M |  |  |
| 7 |  |  | Multiple BIG Support |  |  | [1] 3.7.2.1 |  |  | O |  |  |


#### 2.7.1 Audio Capability Support requirements

Table 52: Codec Specific Configuration LTV Structures: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | LTV Structure |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sampling Frequency _ |  |  | [1] 4.3.2 |  |  | M |  |  |
| 2 |  |  | Frame Duration _ |  |  | [1] 4.3.2 |  |  | M |  |  |
| 3 |  |  | Audio Channel Allocation _ _ |  |  | [1] 4.3.2 |  |  | O |  |  |
| 4 |  |  | Octets Per Codec Frame _ _ _ |  |  | [1] 4.3.2 |  |  | M |  |  |
| 5 |  |  | Codec Frame Blocks Per SDU _ _ _ _ |  |  | [1] 4.3.2 |  |  | O |  |  |

Table 53: Metadata LTV Structures: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Streaming Audio Contexts _ _ |  |  | [1] 6.3.3 |  |  | M |  |  |
| 2 |  |  | Vendor-specific Metadata |  |  | [1] 6.3.3 |  |  | O |  |  |

Table 54: Audio Capability Configuration Support Settings: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, _ 26 Octets |  |  | [1] 3.7.1 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, _ 30 Octets |  |  | [1] 3.7.1 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 30 Octets |  |  | [1] 3.7.1 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 LC3: 16 kHz Sampling Frequency, 10 ms Frame _ Duration, 40 Octets |  |  | [1] 3.7.1 |  |  | M |  |  |
| 5 |  |  | 24 1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 45 Octets |  |  | [1] 3.7.1 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 LC3: 24 kHz Sampling Frequency, 10 ms Frame _ Duration, 60 Octets |  |  | [1] 3.7.1 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 60 Octets |  |  | [1] 3.7.1 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms Frame _ Duration, 80 Octets |  |  | [1] 3.7.1 |  |  | C.7 |  |  |
| 9 |  |  | 441 1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame _ Duration, 97 Octets |  |  | [1] 3.7.1 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame _ Duration, 130 Octets |  |  | [1] 3.7.1 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 75 Octets |  |  | [1] 3.7.1 |  |  | C.10 |  |  |


|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 100 Octets |  |  | [1] 3.7.1 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 90 Octets |  |  | [1] 3.7.1 |  |  | C.10 |  |  |
| 14 |  |  | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 120 Octets |  |  | [1] 3.7.1 |  |  | C.11 |  |  |
| 15 |  |  | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 117 Octets |  |  | [1] 3.7.1 |  |  | C.10 |  |  |
| 16 |  |  | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 155 Octets |  |  | [1] 3.7.1 |  |  | C.11 |  |  |
| 17 |  |  | Vendor-specific Codec Configuration Setting |  |  | [1] 3.7.1 |  |  | O |  |  |

C.1: Optional IF BAP 95/1 “Narrow Band (8 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.2: Optional IF BAP 95/1 “Narrow Band (8 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.3: Optional IF BAP 95/2 “Wideband (16 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.4: Optional IF BAP 95/3 “Semi-Superwideband (24 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.5: Optional IF BAP 95/3 “Semi-Superwideband (24 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.6: Optional IF BAP 95/4 “Superwideband (32 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.7: Optional IF BAP 95/4 “Superwideband (32 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.8: Optional IF BAP 95/5 “Full Band (44.1 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.9: Optional IF BAP 95/5 “Full Band (44.1 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded. C.10: Optional IF BAP 95/6 “Full Band (48 kHz)” AND BAP 96/1 “7.5 ms”, otherwise Excluded. C.11: Optional IF BAP 95/6 “Full Band (48 kHz)” AND BAP 96/2 “10 ms”, otherwise Excluded.
Table 55: QoS Requirements: LC3 Low Latency: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 1 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 1 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 1 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | M |  |  |
| 5 |  |  | 24 1 1 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 1 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.5 |  |  |
| 7 |  |  | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.6 |  |  |
| 8 |  |  | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.7 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 |  |  | 441 1 1 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 4 RTN, 24 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.8 |  |  |
| 10 |  |  | 441 2 1 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 4 RTN, 31 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.9 |  |  |
| 11 |  |  | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 4 RTN, 15 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.10 |  |  |
| 12 |  |  | 48 2 1 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 4 RTN, 20 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.11 |  |  |
| 13 |  |  | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 4 RTN, 15 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.12 |  |  |
| 14 |  |  | 48 4 1 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 4 RTN, 20 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.13 |  |  |
| 15 |  |  | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 4 RTN, 15 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.14 |  |  |
| 16 |  |  | 48 6 1 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 4 RTN, 20 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.15 |  |  |

C.1: Optional IF BAP 54/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 54/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 54/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 54/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Mandatory IF BAP 54/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 54/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.7: Optional IF BAP 54/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.8: Optional IF BAP 54/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.9: Optional IF BAP 54/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.10: Optional IF BAP 54/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.11: Optional IF BAP 54/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.12: Optional IF BAP 54/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.13: Optional IF BAP 54/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.14: Optional IF BAP 54/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.15: Optional IF BAP 54/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 2 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 2 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 2 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 2 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | M |  |  |
| 5 |  |  | 24 1 2 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 2 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.15 |  |  |
| 7 |  |  | 32 1 2 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 2 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.6 |  |  |
| 9 |  |  | 441 1 2 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 4 RTN, 54 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 2 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 4 RTN, 50 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.9 |  |  |
| 12 |  |  | 48 2 2 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 4 RTN, 65 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 4 RTN, 50 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.11 |  |  |
| 14 |  |  | 48 4 2 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 4 RTN, 65 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.12 |  |  |
| 15 |  |  | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 4 RTN, 50 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.13 |  |  |
| 16 |  |  | 48 6 2 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 4 RTN, 65 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.14 |  |  |

C.1: Optional IF BAP 54/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 54/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 54/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 54/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 54/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 54/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded.
C.7: Optional IF BAP 54/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.8: Optional IF BAP 54/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.9: Optional IF BAP 54/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.10: Optional IF BAP 54/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.11: Optional IF BAP 54/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.12: Optional IF BAP 54/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.13: Optional IF BAP 54/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.14: Optional IF BAP 54/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded. C.15: Mandatory IF BAP 54/6 “24_2 LC3: 24 kHz Sampling Frequency, 10 ms Frame Duration, 60 Octets”, otherwise Excluded.
Table 57: QoS Configuration: Vendor-Specific Codec: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Vendor-specific QoS Config Setting: Broadcast Source |  |  | [1] 5.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 54/17 “Vendor-specific Codec Configuration Setting”, otherwise Excluded.
Table 58: LC3 Audio Configuration: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Audio Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AC12: 1 BIS, Single Audio Channel/BIS, 1 Audio Stream |  |  | [1] 4.5.1 |  |  | M |  |  |
| 2 |  |  | AC13: 2 BISes, Single Audio Channel/BIS, 2 Audio Streams |  |  | [1] 4.5.2 |  |  | M |  |  |
| 3 |  |  | AC14: 1 BIS, Multiple Audio Channels/BIS, 1 Audio Stream |  |  | [1] 4.5.3 |  |  | O |  |  |


#### 2.7.2 Context Type requirements

Table 59: Supported Sink Context Requirements: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unspecified |  |  | [1] 3.7.2.2 |  |  | M |  |  |
| 2 |  |  | Conversational |  |  | [1] 5.5 |  |  | O |  |  |
| 3 |  |  | Media |  |  | [1] 5.5 |  |  | O |  |  |
| 4 |  |  | Game |  |  | [1] 5.5 |  |  | O |  |  |
| 5 |  |  | Instructional |  |  | [1] 5.5 |  |  | O |  |  |


|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 |  |  | Voice assistants |  |  | [1] 5.5 |  |  | O |  |  |
| 7 |  |  | Live |  |  | [1] 5.5 |  |  | O |  |  |
| 8 |  |  | Sound effects |  |  | [1] 5.5 |  |  | O |  |  |
| 9 |  |  | Notifications |  |  | [1] 5.5 |  |  | O |  |  |
| 10 |  |  | Ringtone |  |  | [1] 5.5 |  |  | O |  |  |
| 11 |  |  | Alerts |  |  | [1] 5.5 |  |  | O |  |  |
| 12 |  |  | Emergency Alarm |  |  | [1] 5.5 |  |  | O |  |  |


#### 2.7.3 GAP requirements

Table 60: GAP Requirements: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Broadcaster | [1] 2.5 | M | [3] GAP 5/1 |  |  |
| 2 | LE security mode 3 level 1 | [1] 9.1.3 | M | [3] GAP 11b/2 |  |  |
| 3 | LE security mode 3 level 2 | [1] 9.1.3 | C.1 | [3] GAP 11b/3 |  |  |
| 4 | LE security mode 3 level 3 | [1] 9.1.3 | C.2 | [3] GAP 11b/4 |  |  |
| 5 | CoD Major Service Class bit 14 | [1] 8.2.3 | C.3 | N/A |  |  |

C.1: Mandatory IF BAP 61/6 “Encrypted Broadcast Isochronous Stream”, otherwise not defined. C.2: Optional IF BAP 61/6 “Encrypted Broadcast Isochronous Stream”, otherwise not defined. C.3: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise Excluded.
Table 61: Link Layer Requirements: Broadcast Source
Prerequisite: BAP 1/3 “Broadcast Source”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 3.4 | C.1 | [7] LL 9/1 |  |  |
| 2 | LE Extended Advertising | [1] 3.4 | M | [7] LL 9/41 |  |  |
| 3 | LE Periodic Advertising | [1] 3.4 | M | [7] LL 9/42 |  |  |
| 4 | Isochronous Broadcaster | [1] 3.4 | M | [7] LL 9/33 |  |  |
| 5 | Unencrypted Broadcast Isochronous Stream | [1] 3.4 | C.2 | [7] LL 12/2 |  |  |
| 6 | Encrypted Broadcast Isochronous Stream | [1] 3.4 | C.2 | [7] LL 12/1 |  |  |

C.1: Mandatory IF BAP 61/6 “Encrypted Broadcast Isochronous Stream”, otherwise not defined. C.2: Mandatory to support at least one.

### 2.8 Broadcast Sink requirements

Table 62: Broadcast Sink, X.Y Versions
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2025-02-01. Withdrawn 2027-02-01.
Table 63: Broadcast Sink, X.Y.Z Versions
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0.1 |  |  | [9] |  |  | C.3 |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3 |  |  | BAP v1.0.2 |  |  | [10] |  |  | C.3 |  |  |

C.1–C.2: No longer used. C.3: Mandatory to support one and only one.
Table 64: Broadcast Sink: Support Requirements
Prerequisite: BAP 1/4 “Broadcast Sink”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | PACS supported over BR/EDR | [1] 3.2 | C.1, C.2 | [5] PACS 2/1 |  |  |
| 2 | PACS supported over LE | [1] 3.2 | C.1 | [5] PACS 2/2 |  |  |

C.1: Mandatory to support at least one. C.2: Optional IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.

#### 2.8.1 Audio Capability Support requirements

Table 65: Codec Specific Capabilities LTV Structures: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Supported Sampling Frequencies |  |  | [1] 4.3.1 |  |  | M |  |  |
| 2 |  |  | Supported Frame Durations |  |  | [1] 4.3.1 |  |  | M |  |  |
| 3 |  |  | Supported Octets per Codec Frame |  |  | [1] 4.3.1 |  |  | M |  |  |
| 4 |  |  | Supported Audio Channel Counts |  |  | [1] 4.3.1 |  |  | M |  |  |
| 5 |  |  | Supported Max Codec Frames Per SDU |  |  | [1] 4.3.1 |  |  | M |  |  |

Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Multiple Audio Locations |  |  | [1] 4.5 |  |  | O |  |  |
| 2 |  |  | Two Audio Channels |  |  | [1] 4.5 |  |  | O |  |  |

Table 67: Metadata LTV Structures: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Codec Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Preferred Audio Contexts _ _ |  |  | [1] 4.3.3 |  |  | O |  |  |
| 2 |  |  | Streaming Audio Contexts _ _ |  |  | [1] 4.3.3 |  |  | M |  |  |
| 3 |  |  | Vendor-specific Metadata |  |  | [1] 4 |  |  | O |  |  |

Table 68: Audio Capability Support Settings: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, _ 26 Octets |  |  | [1] 3.8.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, _ 30 Octets |  |  | [1] 3.8.2 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 30 Octets |  |  | [1] 3.8.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 LC3: 16 kHz Sampling Frequency, 10 ms Frame _ Duration, 40 Octets |  |  | [1] 3.8.2 |  |  | M |  |  |
| 5 |  |  | 24 1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 45 Octets |  |  | [1] 3.8.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 LC3: 24 kHz Sampling Frequency, 10 ms Frame _ Duration, 60 Octets |  |  | [1] 3.8.2 |  |  | M |  |  |
| 7 |  |  | 32 1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 60 Octets |  |  | [1] 3.8.2 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 LC3: 32 kHz Sampling Frequency, 10 ms Frame _ Duration, 80 Octets |  |  | [1] 3.8.2 |  |  | C.6 |  |  |
| 9 |  |  | 441 1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame _ Duration, 97 Octets |  |  | [1] 3.8.2 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame _ Duration, 130 Octets |  |  | [1] 3.8.2 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 75 Octets |  |  | [1] 3.8.2 |  |  | C.9 |  |  |
| 12 |  |  | 48 2 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 100 Octets |  |  | [1] 3.8.2 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 90 Octets |  |  | [1] 3.8.2 |  |  | C.9 |  |  |


|  | Item |  |  | Codec Requirements |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 |  |  | 48 4 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 120 Octets |  |  | [1] 3.8.2 |  |  | C.10 |  |  |
| 15 |  |  | 48 5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame _ Duration, 117 Octets |  |  | [1] 3.8.2 |  |  | C.9 |  |  |
| 16 |  |  | 48 6 LC3: 48 kHz Sampling Frequency, 10 ms Frame _ Duration, 155 Octets |  |  | [1] 3.8.2 |  |  | C.10 |  |  |
| 17 |  |  | Vendor-specific Codec Capability Setting: Broadcast Sink |  |  | [1] 3.8.2 |  |  | O |  |  |

C.1: Optional IF BAP 93/1 “Narrow Band (8 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.2: Optional IF BAP 93/1 “Narrow Band (8 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.3: Optional IF BAP 93/2 “Wideband (16 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.4: Optional IF BAP 93/3 “Semi-Superwideband (24 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.5: Optional IF BAP 93/4 “Superwideband (32 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.6: Optional IF BAP 93/4 “Superwideband (32 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.7: Optional IF BAP 93/5 “Full Band (44.1 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.8: Optional IF BAP 93/5 “Full Band (44.1 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded. C.9: Optional IF BAP 93/6 “Full Band (48 kHz)” AND BAP 94/1 “7.5 ms”, otherwise Excluded. C.10: Optional IF BAP 93/6 “Full Band (48 kHz)” AND BAP 94/2 “10 ms”, otherwise Excluded.
Table 69: QoS Requirements: LC3 Low Latency: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 1 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 1 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.2 |  |  |
| 3 |  |  | 16 1 1 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 1 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | M |  |  |
| 5 |  |  | 24 1 1 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 1 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | M |  |  |
| 7 |  |  | 32 1 1 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 2 RTN, 8 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 1 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 2 RTN, 10 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.6 |  |  |
| 9 |  |  | 441 1 1 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 4 RTN, 24 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 1 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 4 RTN, 31 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 1 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 4 RTN, 15 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.9 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | 48 2 1 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 4 RTN, 20 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 1 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 4 RTN, 15 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.11 |  |  |
| 14 |  |  | 48 4 1 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 4 RTN, 20 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.12 |  |  |
| 15 |  |  | 48 5 1 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 4 RTN, 15 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.13 |  |  |
| 16 |  |  | 48 6 1 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 4 RTN, 20 Max Transport Latency _ _ |  |  | [1] 6.3 |  |  | C.14 |  |  |

C.1: Optional IF BAP 68/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 68/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 68/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Mandatory IF BAP 68/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 68/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 68/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.7: Optional IF BAP 68/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.8: Optional IF BAP 68/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.9: Optional IF BAP 68/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.10: Optional IF BAP 68/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded. C.11: Optional IF BAP 68/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.12: Optional IF BAP 68/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.13: Optional IF BAP 68/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.14: Optional IF BAP 68/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Table 70: QoS Configuration: LC3 High Reliability: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8 1 2 LC3: 7500 SDU Interval, unframed, 26 Max SDU Size, _ _ 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.1 |  |  |
| 2 |  |  | 8 2 2 LC3: 10000 SDU Interval, unframed, 30 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.2 |  |  |


|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | 16 1 2 LC3: 7500 SDU Interval, unframed, 30 Max SDU _ _ Size, 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.3 |  |  |
| 4 |  |  | 16 2 2 LC3: 10000 SDU Interval, unframed, 40 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 5 |  |  | 24 1 2 LC3: 7500 SDU Interval, unframed, 45 Max SDU _ _ Size, 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.4 |  |  |
| 6 |  |  | 24 2 2 LC3: 10000 SDU Interval, unframed, 60 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | M |  |  |
| 7 |  |  | 32 1 2 LC3: 7500 SDU Interval, unframed, 60 Max SDU _ _ Size, 4 RTN, 45 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.5 |  |  |
| 8 |  |  | 32 2 2 LC3: 10000 SDU Interval, unframed, 80 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.6 |  |  |
| 9 |  |  | 441 1 2 LC3: 8163 SDU Interval, framed, 97 Max SDU Size, _ _ 4 RTN, 54 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.7 |  |  |
| 10 |  |  | 441 2 2 LC3: 10884 SDU Interval, framed, 130 Max SDU _ _ Size, 4 RTN, 60 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.8 |  |  |
| 11 |  |  | 48 1 2 LC3: 7500 SDU Interval, unframed, 75 Max SDU _ _ Size, 4 RTN, 50 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.9 |  |  |
| 12 |  |  | 48 2 2 LC3: 10000 SDU Interval, unframed, 100 Max SDU _ _ Size, 4 RTN, 65 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.10 |  |  |
| 13 |  |  | 48 3 2 LC3: 7500 SDU Interval, unframed, 90 Max SDU _ _ Size, 4 RTN, 50 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.11 |  |  |
| 14 |  |  | 48 4 2 LC3: 10000 SDU Interval, unframed, 120 Max SDU _ _ Size, 4 RTN, 65 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.12 |  |  |
| 15 |  |  | 48 5 2 LC3: 7500 SDU Interval, unframed, 117 Max SDU _ _ Size, 4 RTN, 50 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.13 |  |  |
| 16 |  |  | 48 6 2 LC3: 10000 SDU Interval, unframed, 155 Max SDU _ _ Size, 4 RTN, 65 Max Transport Latency _ _ |  |  | [1] 5.6.2 |  |  | C.14 |  |  |

C.1: Optional IF BAP 68/1 “8_1 LC3: 8 kHz Sampling Frequency, 7.5 ms Frame Duration, 26 Octets”, otherwise Excluded. C.2: Optional IF BAP 68/2 “8_2 LC3: 8 kHz Sampling Frequency, 10 ms Frame Duration, 30 Octets”, otherwise Excluded. C.3: Optional IF BAP 68/3 “16_1 LC3: 16 kHz Sampling Frequency, 7.5 ms Frame Duration, 30 Octets”, otherwise Excluded. C.4: Optional IF BAP 68/5 “24_1 LC3: 24 kHz Sampling Frequency, 7.5 ms Frame Duration, 45 Octets”, otherwise Excluded. C.5: Optional IF BAP 68/7 “32_1 LC3: 32 kHz Sampling Frequency, 7.5 ms Frame Duration, 60 Octets”, otherwise Excluded. C.6: Optional IF BAP 68/8 “32_2 LC3: 32 kHz Sampling Frequency, 10 ms Frame Duration, 80 Octets”, otherwise Excluded. C.7: Optional IF BAP 68/9 “441_1 LC3: 44.1 kHz Sampling Frequency, 8.163 ms Frame Duration, 97 Octets”, otherwise Excluded. C.8: Optional IF BAP 68/10 “441_2 LC3: 44.1 kHz Sampling Frequency, 10.884 ms Frame Duration, 130 Octets”, otherwise Excluded. C.9: Optional IF BAP 68/11 “48_1 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 75 Octets”, otherwise Excluded. C.10: Optional IF BAP 68/12 “48_2 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 100 Octets”, otherwise Excluded.
C.11: Optional IF BAP 68/13 “48_3 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 90 Octets”, otherwise Excluded. C.12: Optional IF BAP 68/14 “48_4 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 120 Octets”, otherwise Excluded. C.13: Optional IF BAP 68/15 “48_5 LC3: 48 kHz Sampling Frequency, 7.5 ms Frame Duration, 117 Octets”, otherwise Excluded. C.14: Optional IF BAP 68/16 “48_6 LC3: 48 kHz Sampling Frequency, 10 ms Frame Duration, 155 Octets”, otherwise Excluded.
Table 71: QoS Configuration: Vendor-Specific Codec: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | QoS Configuration Settings |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Vendor-specific QoS Config Setting: Broadcast Sink |  |  | [1] 5.6.2 |  |  | C.1 |  |  |

C.1: Mandatory IF BAP 68/17 “Vendor-specific Codec Capability Setting: Broadcast Sink”, otherwise Excluded.
Table 72: LC3 Audio Configuration: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Audio Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AC12: 1 BIS, Single Audio Channel/BIS, 1 Audio Stream |  |  | [1] 4.5.1 |  |  | M |  |  |
| 2 |  |  | AC13: 2 BISes, Single Audio Channel/BIS, 2 Audio Streams |  |  | [1] 4.5.2 |  |  | C.1 |  |  |
| 3 |  |  | AC14: 1 BIS, Multiple Audio Channels/BIS, 1 Audio Stream |  |  | [1] 4.5.3 |  |  | C.2 |  |  |

C.1: Mandatory IF BAP 66/1 “Multiple Audio Locations”, otherwise Excluded. C.2: Mandatory IF BAP 66/1 “Multiple Audio Locations” AND BAP 66/2 “Two Audio Channels”, otherwise Excluded.

#### 2.8.2 Context Type requirements

Table 73: Supported Sink Context Requirements: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unspecified |  |  | [1] 4 |  |  | M |  |  |
| 2 |  |  | Conversational |  |  | [1] 4 |  |  | O |  |  |
| 3 |  |  | Media |  |  | [1] 4 |  |  | O |  |  |
| 4 |  |  | Game |  |  | [1] 4 |  |  | O |  |  |
| 5 |  |  | Instructional |  |  | [1] 4 |  |  | O |  |  |
| 6 |  |  | Voice assistants |  |  | [1] 4 |  |  | O |  |  |
| 7 |  |  | Live |  |  | [1] 4 |  |  | O |  |  |
| 8 |  |  | Sound effects |  |  | [1] 4 |  |  | O |  |  |
| 9 |  |  | Notifications |  |  | [1] 4 |  |  | O |  |  |
| 10 |  |  | Ringtone |  |  | [1] 4 |  |  | O |  |  |
| 11 |  |  | Alerts |  |  | [1] 4 |  |  | O |  |  |


|  | Item |  |  | Context Type |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | Emergency Alarm |  |  | [1] 4 |  |  | O |  |  |


#### 2.8.3 GAP requirements

Table 74: GAP Requirements: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Observer | [1] 2.5 | M | [3] GAP 5/2 |  |  |
| 2 | Central | [1] 2.5 | O | [3] GAP 5/4 |  |  |
| 3 | Peripheral | [1] 2.5 | M | [3] GAP 5/3 |  |  |
| 4 | Bondable mode (LE) | [1] 9.1.1, 9.1.2 | M | [3] GAP 24/2 OR GAP 34/2 |  |  |
| 5 | Bondable mode (BR/EDR) | [1] 8.2.1 | C.6 | [3] GAP 1/7 |  |  |
| 6 | Bonding procedure | [1] 9.1.1, 9.1.2 | M | [3] GAP 24/3 OR GAP 34/3 |  |  |
| 7 | LE security mode 1 | [1] 9.1.1, 9.1.2 | M | [3] GAP 25/1 |  |  |
| 8 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 9.1.1, 9.1.2 | M | [3] GAP 25/11 OR GAP 35/11 |  |  |
| 9 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 9.1.1, 9.1.2 | O | [3] GAP 25/12 OR GAP 35/12 |  |  |
| 10 | LE security mode 3 level 1 | [1] 9.1.4 | C.4 | [3] GAP 17b/2 |  |  |
| 11 | LE security mode 3 level 2 | [1] 9.1.4 | C.4 | [3] GAP 17b/3 |  |  |
| 12 | LE security mode 3 level 3 | [1] 9.1.4 | C.5 | [3] GAP 17b/4 |  |  |
| 13 | Security mode 4, level 2 | [1] 9.2 | C.6 | [3] GAP 2/7c |  |  |
| 14 | 128-bit encryption key size capable (BR/EDR) | [1] 9.2 | C.6 | [3] GAP 2/13 |  |  |
| 15 | Minimum 128 Bit entropy key (LE) | [1] 9.1 | M | [3] GAP 25/13 OR GAP 35/13 |  |  |
| 16 | Derivation of BR/EDR Link Key from LE LTK | [1] 9.1.1, 9.2 | C.11 | [3] GAP 41/2a OR GAP 43/2a |  |  |
| 17 | Derivation of LE LTK from BR/EDR Link Key | [1] 9.2 | C.10 | [3] GAP 41/2b OR GAP 43/2b |  |  |
| 18 | CoD Major Service Class bit 14 | [1] 8.2.3 | C.6 | N/A |  |  |
| 19 | Limited discoverable mode | [1] 8.2.1 | C.9 | [3] GAP 1/2 |  |  |
| 20 | General discoverable mode (BR/EDR) | [1] 8.2.1 | C.9 | [3] GAP 1/3 |  |  |
| 21 | BR/EDR Secure Connections | [1] 9.2 | C.11 | N/A |  |  |
| 22 | LE Secure Connections | [1] 9.1 | C.10 | [3] GAP 27b/5 OR GAP 37b/5 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 23 | Out of Band (LE) | [1] 9.1 | C.10 | [3] GAP 27b/9 OR GAP 37b/9 |  |  |
| 24 | Out-of-Band (BR/EDR) | [1] 9.2 | C.11 | [3] GAP 2/14 |  |  |
| 25 | LE security mode 1 level 4 | [1] 9.1.1, 9.1.2 | O | [3] GAP 25/9 OR GAP 35/9 |  |  |

C.1–C.3: No longer used. C.4: Mandatory IF BAP 74/1 “Observer”, otherwise not defined. C.5: Optional IF BAP 74/1 “Observer”, otherwise not defined. C.6: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.7–C.8: No longer used. C.9: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.10: Mandatory to support at least one. C.11: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.
Table 75: No longer used

#### 2.8.4 LL requirements

Table 76: LL Requirements: Broadcast Sink
Prerequisite: BAP 1/4 “Broadcast Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 3.4 | M | [7] LL 9/1 |  |  |
| 2 | LE Extended Advertising | [1] 3.4 | M | [7] LL 9/41 |  |  |
| 3 | LE Periodic Advertising | [1] 3.4 | M | [7] LL 9/42 |  |  |
| 4 | Synchronized Receiver | [1] 3.4 | M | [7] LL 9/34 |  |  |


### 2.9 Scan Delegator requirements

Table 77: Scan Delegator, X.Y Versions
Prerequisite: BAP 1/5 “Scan Delegator”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2025-02-01. Withdrawn 2027-02-01.
Prerequisite: BAP 1/5 “Scan Delegator”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0.1 |  |  | [9] |  |  | C.3 |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3 |  |  | BAP v1.0.2 |  |  | [10] |  |  | C.3 |  |  |

C.1–C.2: No longer used. C.3: Mandatory to support one and only one.
Table 79: Scan Delegator: Support Requirements
Prerequisite: BAP 1/5 “Scan Delegator”

| Item | Service | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | BASS supported over BR/EDR | [1] 3.2 | C.1, C.2 | [6] BASS 2/1 |  |  |
| 2 | BASS supported over LE | [1] 3.2 | C.1 | [6] BASS 2/2 |  |  |

C.1: Mandatory to support at least one. C.2: Optional IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.

#### 2.9.1 GAP requirements

Table 80: GAP Requirements: Scan Delegator
Prerequisite: BAP 1/5 “Scan Delegator”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Peripheral | [1] 2.5 | M | [3] GAP 5/3 |  |  |
| 2 | Central | [1] 2.5 | O | [3] GAP 5/4 |  |  |
| 3 | Bondable mode (LE) | [1] 9.1.1, 9.1.2 | M | [3] GAP 24/2 OR GAP 34/2 |  |  |
| 4 | Bondable mode (BR/EDR) | [1] 8.2.1 | C.2 | [3] GAP 1/7 |  |  |
| 5 | LE security mode 1 | [1] 9.1.1, 9.1.2 | M | [3] GAP 25/1 OR GAP 35/1 |  |  |
| 6 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 9.1.1, 9.1.2 | M | [3] GAP 25/11 OR GAP 35/11 |  |  |
| 7 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 9.1.1, 9.1.2 | O | [3] GAP 25/12 OR GAP 35/12 |  |  |
| 8 | Security mode 4, level 2 | [1] 9.2 | C.2 | [3] GAP 2/7c |  |  |
| 9 | 128-bit encryption key size capable (BR/EDR) | [1] 9.2 | C.2 | [3] GAP 2/13 |  |  |
| 10 | Minimum 128 Bit entropy key (LE) | [1] 9.1 | M | [3] GAP 25/13 OR GAP 35/13 |  |  |
| 11 | Derivation of BR/EDR Link Key from LE LTK | [1] 9.1.1, 9.1.2, 9.2 | C.11 | [3] GAP 41/2a OR GAP 43/2a |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 12 | Derivation of LE LTK from BR/EDR Link Key | [1] 9.2 | C.10 | [3] GAP 41/2b OR GAP 43/2b |  |  |
| 13 | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising (Peripheral) | [1] 3.9.2 | C.6 | [3] GAP 27a/2 |  |  |
| 14 | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising (Peripheral) | [1] 3.9.2 | C.6 | [3] GAP 27a/3 |  |  |
| 15 | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising (Central) | [1] 3.9.2 | C.7 | [3] GAP 37a/2 |  |  |
| 16 | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising (Central) | [1] 3.9.2 | C.7 | [3] GAP 37a/3 |  |  |
| 17 | Periodic Advertising Synchronization Transfer procedure (Peripheral) | [1] 5.5.8 | C.8 | [3] GAP 27a/1 |  |  |
| 18 | Periodic Advertising Synchronization Transfer procedure (Central) | [1] 5.5.8 | C.9 | [3] GAP 37a/1 |  |  |
| 19 | CoD Major Service Class bit 14 | [1] 8.2.3 | C.2 | N/A |  |  |
| 20 | BR/EDR Secure Connections | [1] 9.2 | C.11 | N/A |  |  |
| 21 | LE Secure Connections | [1] 9.1 | C.10 | [3] GAP 27b/5 OR GAP 37b/5 |  |  |
| 22 | Out of Band (LE) | [1] 9.1 | C.10 | [3] GAP 27b/9 OR GAP 37b/9 |  |  |
| 23 | Out-of-Band (BR/EDR) | [1] 9.2 | C.11 | [3] GAP 2/14 |  |  |
| 24 | LE security mode 1 level 4 | [1] 9.1.1, 9.1.2 | O | [3] GAP 25/9 OR GAP 35/9 |  |  |

C.1: No longer used. C.2: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.3–C.5: No longer used. C.6: Mandatory IF BAP 82/4 “Periodic Advertising Sync Transfer - Recipient” AND BAP 80/1 “Peripheral”, otherwise not defined. C.7: Mandatory IF BAP 82/4 “Periodic Advertising Sync Transfer - Recipient” AND BAP 80/2 “Central”, otherwise not defined. C.8: Mandatory IF BAP 82/4 “Periodic Advertising Sync Transfer - Recipient” AND BAP 80/1 “Peripheral” AND NOT BAP 80/2 “Central”, otherwise Optional IF BAP 82/4 “Periodic Advertising Sync Transfer - Recipient” AND BAP 80/1 “Peripheral”, otherwise not defined. C.9: Mandatory IF BAP 82/4 “Periodic Advertising Sync Transfer - Recipient” AND BAP 80/2 “Central” AND NOT BAP 80/1 “Peripheral”, otherwise Optional IF BAP 82/4 “Periodic Advertising Sync Transfer - Recipient” AND BAP 80/2 “Central”, otherwise not defined. C.10: Mandatory to support at least one. C.11: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.
Table 82: LL Requirements: Scan Delegator Role
Prerequisite: BAP 1/5 “Scan Delegator”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 3.4 | M | [7] LL 9/1 |  |  |
| 2 | LE Extended Advertising | [1] 3.4 | M | [7] LL 9/41 |  |  |
| 3 | LE Periodic Advertising | [1] 3.4 | M | [7] LL 9/42 |  |  |
| 4 | Periodic Advertising Sync Transfer - Recipient | [1] 3.4 | O | [7] LL 9/27 |  |  |


### 2.10 Broadcast Assistant requirements

Table 83: Broadcast Assistant, X.Y Versions
Prerequisite: BAP 1/6 “Broadcast Assistant”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2025-02-01. Withdrawn 2027-02-01.
Table 84: Broadcast Assistant, X.Y.Z Versions
Prerequisite: BAP 1/6 “Broadcast Assistant”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BAP v1.0.1 |  |  | [9] |  |  | C.3 |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3 |  |  | BAP v1.0.2 |  |  | [10] |  |  | C.3 |  |  |

C.1–C.2: No longer used. C.3: Mandatory to support one and only one.
Table 85: Broadcast Assistant: Client Services Support Requirements
Prerequisite: BAP 1/6 “Broadcast Assistant”

|  | Item |  |  | Service |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Discover BASS over BR/EDR |  |  | [1] 3.2 |  |  | C.1, C.2 |  |  |
| 2 |  |  | Discover BASS over LE |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 3 |  |  | Discover PACS over BR/EDR |  |  | [1] 3.2 |  |  | C.2 |  |  |
| 4 |  |  | Discover PACS over LE |  |  | [1] 3.2 |  |  | O |  |  |

C.1: Mandatory to support at least one.
Table 86: Broadcast Audio Scan Service Characteristic Support Requirements
Prerequisite: BAP 1/6 “Broadcast Assistant”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Broadcast Audio Scan Control Point characteristic |  |  | [1] 3.10.4 |  |  | M |  |  |
| 2 |  |  | Broadcast Receive State characteristic |  |  | [1] 3.10.4 |  |  | M |  |  |
| 3 |  |  | Broadcast Audio Scan Service discovery |  |  | [1] 3.10.3 |  |  | M |  |  |
| 4 |  |  | Broadcast Audio Scan Service characteristic discovery |  |  | [1] 3.10.3 |  |  | M |  |  |

Table 87: Published Audio Capabilities Service Characteristic Support Requirements
Prerequisite: BAP 85/3 “Discover PACS over BR/EDR” OR BAP 85/4 “Discover PACS over LE”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Sink PAC characteristic |  |  | [1] 3.10.4 |  |  | O |  |  |
| 2 |  |  | Sink Audio Locations characteristic |  |  | [1] 3.10.4 |  |  | O |  |  |
| 3 |  |  | Published Audio Capabilities Service discovery |  |  | [1] 3.10.3 |  |  | O |  |  |
| 4 |  |  | Published Audio Capabilities Service characteristic discovery |  |  | [1] 3.10.3 |  |  | O |  |  |

Table 88: Broadcast Audio Scan Service Operation Support Requirements
Prerequisite: BAP 1/6 “Broadcast Assistant”

|  | Item |  |  | Characteristic |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Remote Scan Start operation |  |  | [1] 6.5.3 |  |  | O |  |  |
| 2 |  |  | Remote Scan Stop operation |  |  | [1] 6.5.3 |  |  | O |  |  |
| 3 |  |  | Add Source operation |  |  | [1] 6.5.4 |  |  | O |  |  |
| 4 |  |  | Modify Source operation |  |  | [1] 6.5.5 |  |  | O |  |  |
| 5 |  |  | SyncInfo Transfer |  |  | [1] 6.5.6 |  |  | O |  |  |
| 6 |  |  | Set Broadcast Code operation |  |  | [1] 6.5.7 |  |  | M |  |  |
| 7 |  |  | Remove Source operation |  |  | [1] 6.5.8 |  |  | O |  |  |


#### 2.10.1 GATT requirements

Table 89: GATT Requirements: Broadcast Assistant
Prerequisite: BAP 1/6 “Broadcast Assistant”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Discover All Primary Services | [1] 3.10.2 | C.1 | [2] GATT 3/2 |  |  |
| 2 | Discover Primary Service by Service UUID | [1] 3.10.2 | C.1 | [2] GATT 3/3 |  |  |
| 3 | Find Included Services | [1] 3.10.2 | O | [2] GATT 3/4 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 4 | Discover All Characteristics of a Service | [1] 3.10.2 | C.2 | [2] GATT 3/5 |  |  |
| 5 | Discover Characteristics by UUID | [1] 3.10.2 | C.2 | [2] GATT 3/6 |  |  |
| 6 | Discover All Characteristic Descriptors | [1] 3.10.2 | M | [2] GATT 3/7 |  |  |
| 7 | Read Characteristic Value | [1] 3.10.2 | M | [2] GATT 3/8 |  |  |
| 8 | Write Characteristic Value | [1] 3.10.2 | M | [2] GATT 3/14 |  |  |
| 9 | Write Without Response | [1] 3.10.2 | M | [2] GATT 3/12 |  |  |
| 10 | Single Notification | [1] 3.10.2 | M | [2] GATT 3/17 |  |  |
| 11 | Read Characteristic Descriptor | [1] 3.10.2 | M | [2] GATT 3/19 |  |  |
| 12 | Write Characteristic Descriptor | [1] 3.10.2 | M | [2] GATT 3/21 |  |  |
| 13 | Exchange MTU | [1] 3.10.2 | M | [2] GATT 3/1 |  |  |
| 14 | GATT Client over BR/EDR | [1] 2.3 | C.3 | [2] GATT 1a/2 |  |  |
| 15 | GATT Client over LE | [1] 2.3 | M | [2] GATT 1a/1 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory to support at least one. C.3: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.

#### 2.10.2 GAP requirements

Table 90: GAP Requirements: Broadcast Assistant
Prerequisite: BAP 1/6 “Broadcast Assistant”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Observer | [1] 2.5 | O | [3] GAP 5/2 |  |  |
| 2 | Peripheral | [1] 2.5 | O | [3] GAP 5/3 |  |  |
| 3 | Central | [1] 2.5 | M | [3] GAP 5/4 |  |  |
| 4 | Bondable mode (LE) | [1] 9.1.1, 9.1.2 | M | [3] GAP 24/2 OR GAP 34/2 |  |  |
| 5 | Bonding procedure | [1] 9.1.1, 9.1.2 | M | [3] GAP 24/3 OR GAP 34/3 |  |  |
| 6 | LE security mode 1 | [1] 9.1.1, 9.1.2 | M | [3] GAP 25/1 OR GAP 35/1 |  |  |
| 7 | Unauthenticated Pairing (LE security mode 1 level 2) with LE Secure Connections Pairing only | [1] 9.1.1, 9.1.2 | M | [3] GAP 25/11 OR GAP 35/11 |  |  |
| 8 | Authenticated Pairing (LE security mode 1 level 3) with LE Secure Connections Pairing only | [1] 9.1.1, 9.1.2 | O | [3] GAP 25/12 OR GAP 35/12 |  |  |
| 9 | Security mode 4, level 2 | [1] 9.2 | C.3 | [3] GAP 2/7c |  |  |
| 10 | 128-bit encryption key size capable (BR/EDR) | [1] 9.2 | C.3 | [3] GAP 2/13 |  |  |
| 11 | Minimum 128 Bit entropy key (LE) | [1] 9.1 | M | [3] GAP 25/13 OR GAP 35/13 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 12 | Derivation of BR/EDR Link Key from LE LTK | [1] 9.1.1, 9.1.2, 9.2 | C.10 | [3] GAP 41/2a OR GAP 43/2a |  |  |
| 13 | Derivation of LE LTK from BR/EDR Link Key | [1] 9.2 | C.9 | [3] GAP 41/2b OR GAP 43/2b |  |  |
| 14 | Periodic Advertising Synchronization Transfer procedure (Peripheral) | [1] 6.5.6 | C.6 | [3] GAP 27a/1 |  |  |
| 15 | Periodic Advertising Synchronization Transfer procedure (Central) | [1] 6.5.6 | C.7 | [3] GAP 37a/1 |  |  |
| 16 | Periodic Advertising Synchronization Establishment procedure over an LE connection without listening for periodic advertising | [1] 6.4 | C.8 | [3] GAP 27a/2 |  |  |
| 17 | Periodic Advertising Synchronization Establishment procedure over an LE connection with listening for periodic advertising | [1] 6.4 | C.8 | [3] GAP 27a/3 |  |  |
| 18 | CoD Major Service Class bit 14 | [1] 8.2.3 | C.3 | N/A |  |  |
| 19 | BR/EDR Secure Connections | [1] 9.2 | C.10 | N/A |  |  |
| 20 | LE Secure Connections | [1] 9.1 | C.9 | [3] GAP 27b/5 OR GAP 37b/5 |  |  |
| 21 | Out of Band (LE) | [1] 9.1 | C.9 | [3] GAP 27b/9 OR GAP 37b/9 |  |  |
| 22 | Out-of-Band (BR/EDR) | [1] 9.2 | C.10 | [3] GAP 2/14 |  |  |
| 23 | LE security mode 1 level 4 | [1] 9.1.1, 9.1.2 | O | [3] GAP 25/9 OR GAP 35/9 |  |  |

C.1–C.2: No longer used. C.3: Mandatory IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined. C.4–C.5: No longer used. C.6: Mandatory IF BAP 92/4 “Periodic Advertising Sync Transfer - Sender” AND BAP 90/2 “Peripheral” AND NOT BAP 90/3 “Central”, otherwise Optional IF BAP 92/4 “Periodic Advertising Sync Transfer - Sender”, otherwise not defined. C.7: Mandatory IF BAP 92/4 “Periodic Advertising Sync Transfer - Sender” AND BAP 90/3 “Central” AND NOT BAP 90/2 “Peripheral”, otherwise Optional IF BAP 92/4 “Periodic Advertising Sync Transfer - Sender”, otherwise not defined. C.8: Mandatory to support at least one IF BAP 92/6 “Initiating Periodic Advertising Sync Transfer for Remote Periodic Advertising”, otherwise not defined. C.9: Mandatory to support at least one. C.10: Mandatory to support at least one IF BAP 3/2 “GAP BR/EDR Host”, otherwise not defined.
Table 91: No longer used

#### 2.10.3 LL requirements

Table 92: LL Requirements: Broadcast Assistant
Prerequisite: BAP 1/6 “Broadcast Assistant”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Encryption | [1] 3.4 | M | [7] LL 9/1 |  |  |
| 2 | LE Extended Advertising | [1] 3.4 | M | [7] LL 9/41 |  |  |
| 3 | LE Periodic Advertising | [1] 3.4 | M | [7] LL 9/42 |  |  |
| 4 | Periodic Advertising Sync Transfer - Sender | [1] 3.4 | O | [7] LL 9/26 |  |  |
| 5 | Initiating Periodic Advertising Sync Transfer for Local Periodic Advertising | [1] 3.4 | C.1 | [7] LL 9/28 |  |  |
| 6 | Initiating Periodic Advertising Sync Transfer for Remote Periodic Advertising | [1] 3.4 | C.1 | [7] LL 9/29 |  |  |
| 7 | Synchronized Receiver | [1] 3.4 | O | [7] LL 9/34 |  |  |

C.1: Mandatory to support at least one IF BAP 92/4 “Periodic Advertising Sync Transfer - Sender”, otherwise not defined.

## 3 References

[1] Basic Audio Profile Specification, Version 1.0 or later
[2] ICS Proforma for Generic Attribute Profile (GATT)
[3] ICS Proforma for Generic Access Profile (GAP)
[4] ICS Proforma for Audio Stream Control Service (ASCS)
[5] ICS Proforma for Published Audio Capabilities Service (PACS)
[6] ICS Proforma for Broadcast Audio Scan Service (BASS)
[7] ICS Proforma for Low Energy Link Layer (LL)
[8] BAP Erratum 19096: Ambiguous requirements for data path configuration and ASE states for bidirectional CISs
[9] Basic Audio Profile Specification, Version 1.0.1 or later
[10] Basic Audio Profile Specification, Version 1.0.2
[11] ICS Proforma for Low Complexity Communication Codec (LC3)

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2021-09-21 | Approved by BTI on 2021-09-10. Basic Audio Profile (BAP) v1.0 adopted by the BoD on 2021-09-14. Prepared for initial publication. |
|  |  |  | p0ed2r00 |  |  | 2021-10-13 | TSE 17550 (rating 1): Added missing BAP 1/2 “Unicast Client” prerequisite to Table 47. TSE 17551 (rating 1): Corrected the prerequisite for Table 72. |
|  |  |  | p0 edition 2 |  |  | 2021-11-10 | Approved by BTI on 2021-11-08. Prepared for edition 2 publication. (Includes additional Consistency Checker updates requested as integration review feedback during BTI review.) |
|  |  |  | p0ed3r00 |  |  | 2022-01-25 | TSE 18186 (rating 1): Updated Link Layer inter-layer dependency items in Tables 25, 48, 61, 76, 82, and 92 to align with updates made in the LL ICS. Made template-related fixes, including aligning the copyright page with v2 of the DNMD. |
|  |  |  | p0 edition 3 |  |  | 2022-01-27 | Approved by BTI on 2022-01-27. Prepared for edition 3 publication. |
|  |  |  | p1r00–r01 |  |  | 2022-02-24 – 2022-03-28 | TSE 18377 (rating 1): Removed “is/are supported” language from conditionals globally. TSE 18561 (rating 2): Added ICS item 27/1 for Expedited Erratum 18524, “Harmonize 1 and 2 server audio configuration support from client side”. A new reference is added for E18524. Added conditionals C.8, C.9, C.10, and C.11 to Table 44 and updated the conditional status of items BAP 44/10, BAP 44/11, BAP 44/15, and BAP 44/16. |
| 1 |  |  | p1 |  |  | 2022-04-12 | Approved by BTI on 2022-04-07. EE 18524 adopted by the BoD on 2022-04-12. Prepared for publication. |
|  |  |  | p2r00–r06 |  |  | 2022-04-12 – 2022-06-10 | TSE 17927 (rating 2): Updated the status of 46/8. TSE 18459 (rating 2): Added conditionals and updated 24/2, 47/2, 75/2, and 91/2. TSE 18938 (rating 4): Updated to accommodate Expedited Erratum 18556, including changes to references in line items and updates to conditionals: Table 23 (23/11, 23/12, C.4, C.5), Table 46 (46/10, 46/11, C.4, C.5), Table 74 (74/16, 74/17, C.7, C.8), Table 80 (80/11, 80/12, C.4, C.5), and Table 90 (90/12, 90/13, C.4, C.5). Added new ICS items to minor versions tables to cover EE 18556: 5/2, 27/3, 63/2, 78/2, and 84/2. TSE 18995 (rating 1): Modified Versions tables globally to account for v1.0.1 and associated deprecation and withdrawal. Affected tables are: Tables 4, 5, 26, 27, 49, 50, 62, 63, 77, 78, 83, and 84. Updated BAP reference with “or later”. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 2 |  |  | p2 |  |  | 2022-06-28 | Approved by BTI on 2022-06-20. BAP v1.0.1 and EE 18556 adopted by the BoD on 2022-06-21. Prepared for TCRL 2022-1 publication. |
|  |  |  | p2ed2 r00–r03 |  |  | 2022-07-18 – 2022-08-22 | TSE 19002 (rating 1): Updated “ – “ to “: ” and consistently added a space between kHz/ms and the accompanying number. TSE 19153 (rating 1): Updated the feature name of item 6 in Table 61. TSE 19320 (rating 1): Removed D&W information that was prematurely added during the .Z release until the dates are formally approved by the BoD. Editorials, including removing the draft entries from the Revision History table to align with current practices. |
|  |  |  | p2 edition 2 |  |  | 2022-08-22 | Approved by BTI on 2022-08-22. Prepared for edition 2 publication. |
|  |  |  | p3r00–r01 |  |  | 2022-09-29 – 2022-11-21 | TSE 20642 (rating 2): Updated C.2 in Tables 24, 47, 75, and 91 to include BAP 3/2. |
| 3 |  |  | p3 |  |  | 2023-02-07 | Approved by BTI on 2022-12-19. Prepared for TCRL 2022-2 publication. |
|  |  |  | p3ed2r00– r01 |  |  | 2023-02-14 | TSE 22435 (rating 1): Replaced “AC13: 2 BISes, Multiple Audio Channels/BIS, 2 Audio Stream” with “AC13: 2 BISes, Single Audio Channel/BIS, 2 Audio Streams” in Table 58, Item 2, and Table 72, Item 2. TSE 22638 (rating 1): Updated ILD references to Security Manager 8/1 to SM 8a/1 (for Central role) or SM 8b/1 (for Peripheral role) in Tables 24, 47, 75, 81, and 91. Editorials to align the document with the latest ICS template. TSE 22690 (rating 1): Updated Table 5, C.2; Table 63, C.2; Table 78, C.2; and Table 84, C.2. In Table 27, deleted C.2 and C.3 because they are no longer used. Editorials to align the document with the latest ICS template. |
|  |  |  | p3 edition 2 |  |  | 2023-03-14 | Approved by BTI on 2023-03-13. Prepared for edition 3 publication. |
|  |  |  | p4r00–r02 |  |  | 2023-04-06 – 2023-05-25 | TSE 22387 (rating 4): Added 7/9 and 7/10 and associated C.2 to cover general and targeted announcements. TSE 22614 (rating 2): Added C.16 to Table 40 and updated 40/4 from M to C.16; added C.15 and C.16 to Table 41 and updated 41/4 from M to C.15 and 41/6 from M to C.16. TSE 22831 (rating 4): To support Expedited Erratum 19096 (approved by the BoD on 2023-05-23), added item 5/3 and associated C.3, new Table 9a, item 27/4 and associated C.4, new Table 33a, and new reference to EE19096. Consistency checker editorials (including removing duplicated conditionals in 23/11, 46/10, 74/16, 80/11, and 90/12). |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 4 |  |  | p4 |  |  | 2023-06-29 | Approved by BTI on 2023-06-05. Prepared for TCRL 2023-1 publication. |
|  |  |  | p5r00 |  |  | 2023-07-24 | TSE 23538 (rating 2): Per EE 19096, modified the prerequisite and added conditionals C.1 through C.6 to Tables 9a and 33a and updated the statuses of all table items. |
| 5 |  |  | p5 |  |  | 2023-09-05 | Approved by BTI on 2023-08-14. EE 19096 adopted by the BoD on 2023-08-29. Prepared for TCRL 2023-1-addition publication. |
|  |  |  | p6r00–r03 |  |  | 2023-10-03 – 2023-12-14 | TSE 23128 (rating 1): Renamed the Feature and removed the ILD for 28/1, 28/2, 28/3, 28/4. TSE 23251 (rating 2): Corrected RTN and Max Transport Latency values in Tables 40 and 41. _ _ TSE 23345 (rating 2): To resolve GAP/SM ILDs: Removed the item for the SM ICS from the References list and updated cross-refs throughout the doc. Updated instances of “or” to “OR” in ILDs globally. Updated Table 23 with new statuses and the addition of 23/17–23/20; updated conditionals accordingly. Removed SM requirements section heading and deleted Table 24. Updated Table 46 with new statuses and the addition of 46/13–46/16; updated conditionals accordingly. Removed SM requirements section heading and deleted Table 47. Updated Table 71 with new statuses and the addition of 71/21–71/24; updated conditionals accordingly. Removed SM requirements section heading and deleted Table 72. Updated Table 80 with new statuses and the addition of 80/20–80/23; updated conditionals accordingly. Removed deleted SM requirements Table 81. Updated Table 90 with new statuses and the addition of 90/19–90/22; updated conditionals accordingly. Removed SM requirements section heading and deleted Table 91. |
| 6 |  |  | p6 |  |  | 2024-07-01 | Approved by BTI on 2024-04-21. Prepared for TCRL 2024-1 publication. |
|  |  |  | p7r00–06 |  |  | 2024-08-13 – 2024-08-26 | TSE 22920 (rating 2): Per E19111, updated status values for Tables 23, 46, 74, 80, 90 and added items 23/21, 46/17, 74/25, 80/24, 90/23. TSE 22921 (rating 2): Per E20442, updated the status for Item 36/6. TSE 24995 (rating 4): Updated Table 51 to add 51/7. TSE 25566 (rating 1): Per E18619, E18849, E18876, E18877, E19050, E19105, E19111, E19289, E19296, E20442, E20483, E20597, E22215, E22230, E22266, E22754, E22890, E23025, E23760, E24038, E24182, E24567, and E24730, updated to account for BAS v1.0.2 as part of the .Z release. In Table 5, updated the reference and status value for Item 5/1, added Item 5/4, updated conditionals C.2 and C.3, and added C.4. In Table 27, updated the reference and status value for Item 27/2, added Item 27/5, updated |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | conditionals C.1 and C.2, and added C.3. In Table 50, updated the reference and status value for Item 50/1, and added Item 50/2 and conditional C.1. In Table 63, updated the reference and status value for Item 63/1, added Item 63/3, updated conditional C.2, and added C.3. In Table 78, updated the reference and status value for Item 78/1, added Item 78/3, updated conditional C.2, and added C.3. In Table 84, updated the reference and status value for Item 84/1, added Item 84/3, updated conditional C.2, and added C.3. Updated the references. Made editorial updates to align the document with the latest ICS template. TSE 26002 (rating 2): Updated the Status value and added conditionals for items in Tables 12, 13, 36, 37, 54, and 68. Added new LC3 Configurations section including new Tables 93–96. Updated the references list. Incorporated consistency checker updates. |
| 7 |  |  | p7 |  |  | 2024-10-08 | Approved by BTI on 2024-09-11. BAP v1.0.2 adopted by the BoD on 2024-10-01. Prepared for TCRL 2024- 2-addition publication. |
|  |  |  | p8r00–r03 |  |  | 2024-10-22 | TSE 24448 (rating 2): Updated conditionals C.4 and C.5 for Table 55. Added conditional C.15 for Table 56. Updated table formatting to current guidelines. TSE 25554 (rating 2): Updated inter-layer dependencies for Items 80/21 and 80/22 and capabilities for 80/22. TSE 25796 (rating 1): Updated the title and service information for all items and deleted the Inter-Layer Dependency column for Table 85. TSE 26378 (rating 1): Updated to provide Deprecation and Withdrawal information. Updated the Status column and added conditionals C.1 and C.2 for Tables 4, 26, 49, 62, 77, and 83. Added a prerequisite, updated the Reference and Status columns, and updated conditionals C.2–C.4 for Table 5. Updated Items 1 and 3, the Reference column, and conditionals C.1–3 for Table 27. Added a prerequisite and updated the Reference column and conditional C.1 for Table 50. Added a prerequisite and updated Item 2, the References column, and conditionals C.1– 3 for Tables 63, 78, and 84. Updated the References section. |
| 8 |  |  | p8 |  |  | 2025-02-18 | Approved by BTI on 2025-02-09. Prepared for TCRL 2025-1 publication. |
|  |  |  | p9r00–r04 |  |  | 2025-02-17 – 2025-05-23 | TSE 26914 (rating 1): Updated Status values for 33a/3 and 33a/6 – 33a/8, and added a name to the Acknowledgements section. Fixed broken cross-references. |
| 9 |  |  | p9 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p10r00–r03 |  |  | 2025-08-07 – 2025-08-13 | TSE 27124 (rating 2): Added Table 2 with conditionals C.1–C.4. Updated Table 3 and replaced conditional C.1 with a Note. Added conditional C.3 to Table 6. Changed “BR/EDR/LE Host” to “GAP BR/EDR Host” throughout. Updated Status in BAP 28/1 and 28/3, and added conditional C.3. Added two new rows to Table 45 and 89, and added conditional C.3. Added conditional C.2 to Tables 64 and 79. Updated Status in BAP 85/1 and 85/3, and added conditional C.2. TSE 27571 (rating 1): Removed GAP 38/1–38/4 from Tables 23, 46, 60, 74, 80, and 90. TSE 27792 (rating 1): Updated conditional C.8 for Table 90. TSE 27952 (rating 1): Changed “Version” column to “Capability” in Table 51. |
| 10 |  |  | p10 |  |  | 2025-11-04 | Approved by BTI on 2025-09-29. Prepared for TCRL pkg101 publication. |
|  |  |  | p11r00–r01 |  |  | 2025-12-05 – 2026-01-14 | TSE 28372 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 11 |  |  | p11 |  |  | 2026-02-17 | Approved by BTI on 2026-01-26. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Dejan Berec |  |  | Bluetooth SIG, Inc. |  |  |
| Jörg Brakensiek |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Jim Harper |  |  | Bluetooth SIG, Inc. |  |  |
| Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |  |
| Jawid Mirani |  |  | Bluetooth SIG, Inc. |  |  |
| Rasmus Abildgren |  |  | Bose Corporation |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
| Chris Church |  |  | Qualcomm |  |  |
| Magnus Sommansson |  |  | Qualcomm |  |  |
| Masaya Masuda |  |  | Toshiba Corporation |  |  |
