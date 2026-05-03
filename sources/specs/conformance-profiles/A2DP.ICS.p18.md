# A2DP.ICS.p18

> Source: PDF converted via PyMuPDF.

---

Advanced Audio Distribution Profile (A2DP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: A2DP.ICS.p18 ▪ Revision Date: 2026-02-17 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2001–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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


### 2.1 Versions

Table 0: No longer used
Table 0a: No longer used
Table 2a: X.Y Versions (Source)
Prerequisite: A2DP 1/1 “Source”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | A2DP v1.0** |  |  | A2DP v1.0 |  |  | Deprecated 2022-02-01. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | A2DP v1.2 |  |  | [1] |  |  | C.1 |  |  |
| 3 |  |  | A2DP v1.3 |  |  | [8] |  |  | C.1, C.2 |  |  |
| 4 |  |  | A2DP v1.4 |  |  | [6] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 2b: X.Y.Z Versions (Source)

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | A2DP v1.3.1** |  |  | A2DP v1.3.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 2 |  |  | A2DP v1.3.2 |  |  | [9] |  |  | C.1 |  |  |
| 3 |  |  | A2DP v1.4.1 |  |  | [10] |  |  | C.2 |  |  |

C.1: Mandatory IF A2DP 2a/3 “A2DP v1.3”, otherwise Excluded.
C.2: Optional IF A2DP 2a/4 “A2DP v1.4”, otherwise Excluded.
Table 7a: X.Y Versions (Sink)
Prerequisite: A2DP 1/2 “Sink”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | A2DP v1.0** |  |  | A2DP v1.0 |  |  | Deprecated 2022-02-01. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | A2DP v1.2 |  |  | [1] |  |  | C.1 |  |  |
| 3 |  |  | A2DP v1.3 |  |  | [8] |  |  | C.1, C.2 |  |  |
| 4 |  |  | A2DP v1.4 |  |  | [6] |  |  | C.1 |  |  |

** Deprecated items will not appear in the Bluetooth SIG qualification tool after the next TCRL following the deprecation date.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 7b: X.Y.Z Versions (Sink)

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | A2DP v1.3.1** |  |  | A2DP v1.3.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 2 |  |  | A2DP v1.3.2 |  |  | [9] |  |  | C.1 |  |  |
| 3 |  |  | A2DP v1.4.1 |  |  | [10] |  |  | C.2 |  |  |

C.1: Mandatory IF A2DP 7a/3 “A2DP v1.3”, otherwise Excluded.
C.2: Optional IF A2DP 7a/4 “A2DP v1.4”, otherwise Excluded.

### 2.2 Core Configuration

Table 1d: Core Configuration Requirements

|  | Item |  |  | Core Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.1 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.1 |  |  | C.2 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”.
C.2: Excluded for this Profile.
C.3: Mandatory for this Profile.

### 2.3 Roles

Table 1: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Source |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 2 |  |  | Sink |  |  | [1] 2.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.4 Source Features

Table 2: A2DP SRC Features
Prerequisite: A2DP 1/1 “Source”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate Connection Establishment |  |  | [2] 3.1.1 |  |  | M |  |  |
| 2 |  |  | Accept Connection Establishment |  |  | [2] 3.1.1 |  |  | M |  |  |
| 3 |  |  | Initiate Start Streaming |  |  | [2] 3.1.2 |  |  | M |  |  |
| 4 |  |  | Accept Start Streaming |  |  | [2] 3.1.2 |  |  | M |  |  |
| 5 |  |  | Send Audio Stream |  |  | [1] 3.2.1 |  |  | M |  |  |
| 6 |  |  | Initiate Connection Release |  |  | [2] 3.1.3 |  |  | M |  |  |
| 7 |  |  | Accept Connection Release |  |  | [2] 3.1.3 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 |  |  | Initiate Suspend |  |  | [2] 3.1.4 |  |  | O |  |  |
| 9 |  |  | Accept Suspend |  |  | [2] 3.1.4 |  |  | O |  |  |
| 10 |  |  | SBC Encoder |  |  | [1] 4.3 |  |  | M |  |  |
| 10a |  |  | Encode and Forward Audio Stream |  |  | [1] 3.2.1 |  |  | O |  |  |
| 11 |  |  | SBC Configurations in 16 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | O |  |  |
| 12 |  |  | SBC Configurations in 32 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | O |  |  |
| 13 |  |  | SBC Configurations in 44.1 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | C.1 |  |  |
| 14 |  |  | SBC Configurations in 48 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | C.1 |  |  |
| 15 |  |  | Delay Reporting |  |  | [1] 5.1.1.2 [2] 3.1.8 |  |  | C.2 |  |  |
| 16 |  |  | SRC video playback via Bluetooth VDP |  |  | [2] 3.1.8 |  |  | C.3 |  |  |
| 17 |  |  | SRC video playback on a local video display |  |  | [2] 3.1.8 |  |  | C.3 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF A2DP 2/16 “SRC video playback via Bluetooth VDP” OR A2DP 2/17 “SRC video playback on a local video display”, otherwise Excluded.
C.3: Excluded IF A2DP 2a/2 “A2DP v1.2”, otherwise Optional.

### 2.5 SRC Implementation

Table 3: Supported Codec Interoperability Requirements in SRC
Prerequisite: A2DP 1/1 “Source”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | SBC encoder |  |  | [1] 4.3 & Appendix B [3] 3.2.3 |  |  | M |  |  |
| 1a |  |  | Encode and Forward SBC Audio Stream |  |  | [1] 4.3 & Appendix B [3] 3.2.3 |  |  | O |  |  |
| 2–3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 4 |  |  | Encode and forward MPEG-1,2 Audio Stream |  |  | [1] 4.4 |  |  | O |  |  |
| 5 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 6 |  |  | Encode and forward MPEG-2,4 AAC Audio Stream |  |  | [1] 4.5 |  |  | O |  |  |
| 7 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 8 |  |  | Encode and forward ATRAC family Audio Stream |  |  | [1] 4.6 |  |  | O |  |  |
| 9 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 10 |  |  | Encode and forward MPEG-D USAC Audio Stream |  |  | [6] 4.8 |  |  | C.6 |  |  |

C.1–C.5: No longer used.
C.6: Excluded IF A2DP 2a/2 “A2DP v1.2” OR A2DP 2a/3 “A2DP v1.3”, otherwise Optional.
Table 3a: Supported Codec Feature Interoperability Requirements in SRC
Prerequisite: A2DP 3/1 “SBC encoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Channel Mode - Mono |  |  | [1] 4.3.2.2 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 |  |  | Channel Mode – Dual Channel |  |  | [1] 4.3.2.2 |  |  | C.1 |  |  |
| 3 |  |  | Channel Mode – Stereo |  |  | [1] 4.3.2.2 |  |  | C.1 |  |  |
| 4 |  |  | Channel Mode – Joint Stereo |  |  | [1] 4.3.2.2 |  |  | C.1 |  |  |
| 5 |  |  | Block Length 4 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 6 |  |  | Block Length 8 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 7 |  |  | Block Length 12 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 8 |  |  | Block Length 16 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 9 |  |  | Subbands - 4 |  |  | [1] 4.3.2.4 |  |  | O |  |  |
| 10 |  |  | Subbands - 8 |  |  | [1] 4.3.2.4 |  |  | M |  |  |
| 11 |  |  | Allocation - SNR |  |  | [1] 4.3.2.5 |  |  | O |  |  |
| 12 |  |  | Allocation - Loudness |  |  | [1] 4.3.2.5 |  |  | M |  |  |

C.1: Mandatory to support at least one.

#### 2.5.1 MPEG-2,4 AAC Supported Codec Feature Interoperability Requirements

in SRC
Table 3g: Supported MPEG-2,4 AAC Object Type Interoperability Requirements in SRC
Prerequisite: A2DP 3/6 “Encode and forward MPEG-2,4 AAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | MPEG-2 AAC LC |  |  | [1] 4.5.2.1 |  |  | M |  |  |
| 2 |  |  | MPEG-4 AAC LC |  |  | [1] 4.5.2.1 |  |  | O |  |  |
| 3 |  |  | MPEG-4 AAC LTP |  |  | [1] 4.5.2.1 |  |  | O |  |  |
| 4 |  |  | MPEG-4 AAC scalable |  |  | [1] 4.5.2.1 |  |  | O |  |  |
| 5 |  |  | MPEG-4 HE-AAC |  |  | [6] 4.5.2.1 |  |  | C.1 |  |  |
| 6 |  |  | MPEG-4 HE-AACv2 |  |  | [6] 4.5.2.1 |  |  | C.1 |  |  |
| 7 |  |  | MPEG-4 AAC-ELDv2 |  |  | [6] 4.5.2.1 |  |  | C.1 |  |  |

C.1: Excluded IF A2DP 2a/2 “A2DP v1.2” OR A2DP 2a/3 “A2DP v1.3”, otherwise Optional.
Table 3h: Supported MPEG-2,4 AAC Channel Interoperability Requirements in SRC
Prerequisite: A2DP 3/6 “Encode and forward MPEG-2,4 AAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 Channel |  |  | [1] 4.5.2.4 |  |  | C.1 |  |  |
| 2 |  |  | 2 Channels |  |  | [1] 4.5.2.4 |  |  | C.1 |  |  |
| 3 |  |  | 6 (5.1) Channels |  |  | [6] 4.5.2.4 |  |  | C.2 |  |  |
| 4 |  |  | 8 (7.1) Channels |  |  | [6] 4.5.2.4 |  |  | C.2 |  |  |

C.1: Mandatory to support at least one.
C.2: Excluded IF A2DP 2a/2 “A2DP v1.2” OR A2DP 2a/3 “A2DP v1.3”, otherwise Optional.
Prerequisite: A2DP 3/6 “Encode and forward MPEG-2,4 AAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 2 |  |  | 11025 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 3 |  |  | 12000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 4 |  |  | 16000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 5 |  |  | 22050 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 6 |  |  | 24000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 7 |  |  | 32000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 8 |  |  | 44100 Hz |  |  | [1] 4.5.2.3 |  |  | C.1 |  |  |
| 9 |  |  | 48000 Hz |  |  | [1] 4.5.2.3 |  |  | C.1 |  |  |
| 10 |  |  | 64000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 11 |  |  | 88200 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 12 |  |  | 96000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |

C.1: Mandatory to support at least one.
Table 3j: Supported MPEG-2,4 AAC Feature Interoperability Requirements in SRC
Prerequisite: A2DP 3/6 “Encode and forward MPEG-2,4 AAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Variable Bit Rate |  |  | [1] 4.5.2.5 [6] 4.5.2.6 |  |  | O |  |  |
| 2 |  |  | MPEG-D DRC |  |  | [6] 4.5.2.2 |  |  | C.1 |  |  |

C.1: Excluded IF A2DP 2a/2 “A2DP v1.2” OR A2DP 2a/3 “A2DP v1.3”, otherwise Optional IF A2DP 3g/2 “MPEG-4 AAC LC” OR A2DP 3g/3 “MPEG-4 AAC LTP” OR A2DP 3g/4 “MPEG-4 AAC scalable” OR A2DP 3g/5 “MPEG-4 HE-AAC” OR A2DP 3g/6 “MPEG-4 HE-AACv2” OR A2DP 3g/7 “MPEG-4 AAC-ELDv2”, otherwise Excluded.

#### 2.5.2 MPEG-D USAC Supported Codec Feature Interoperability Requirements

in SRC
Table 3k: Supported MPEG-D USAC Channel Interoperability Requirements in SRC
Prerequisite: A2DP 3/10 “Encode and forward MPEG-D USAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 Channel |  |  | [1] 4.8.2.3 |  |  | C.1 |  |  |
| 2 |  |  | 2 Channels |  |  | [1] 4.8.2.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.
Prerequisite: A2DP 3/10 “Encode and forward MPEG-D USAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 7350 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 2 |  |  | 8000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 3 |  |  | 8820 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 4 |  |  | 9600 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 5 |  |  | 11025 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 6 |  |  | 11760 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 7 |  |  | 12000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 8 |  |  | 12800 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 9 |  |  | 14700 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 10 |  |  | 16000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 11 |  |  | 17640 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 12 |  |  | 19200 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 13 |  |  | 22050 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 14 |  |  | 24000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 15 |  |  | 29400 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 16 |  |  | 32000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 17 |  |  | 35280 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 18 |  |  | 38400 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 19 |  |  | 44100 Hz |  |  | [1] 4.8.2.2 |  |  | C.1 |  |  |
| 20 |  |  | 48000 Hz |  |  | [1] 4.8.2.2 |  |  | C.1 |  |  |
| 21 |  |  | 58800 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 22 |  |  | 64000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 23 |  |  | 70560 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 24 |  |  | 76800 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 25 |  |  | 88200 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 26 |  |  | 96000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |

C.1: Mandatory to support at least one.
Table 3m: Supported MPEG-D USAC Feature Interoperability Requirements in SRC
Prerequisite: A2DP 3/10 “Encode and forward MPEG-D USAC Audio Stream”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Variable Bit Rate |  |  | [6] 4.8.2.4 |  |  | O |  |  |
| 2 |  |  | MPEG-D DRC |  |  | [6] 4.8.2.1 |  |  | M |  |  |


#### 2.5.3 Requirements toward Other Profiles


##### 2.5.3.1 Requirements toward SDP

Table 8: SDP Attributes (Source)
Prerequisite: A2DP 1/1 “Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | No longer used | N/A | N/A | N/A |  |  |
| 2 | ProtocolDescriptorList | [1] 5.3 | M | [5] SDP 9/2 |  |  |
| 3 | BluetoothProfileDescriptorList | [1] 5.3 | M | [5] SDP 9/14 |  |  |
| 4 | Supported Features | [1] 5.3 | O | N/A |  |  |


##### 2.5.3.2 Requirements toward GAVDP

Table 9: GAVDP Roles (Source)
Prerequisite: A2DP 1/1 “Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initiator | [1] 5.1.1.1 | M | [4] GAVDP 1/1 |  |  |
| 2 | Acceptor | [1] 5.1.1.1 | M | [4] GAVDP 1/2 |  |  |
| 3 | Delay Reporting Initiator | [1] 5.1.1.2 | C.2 | [4] GAVDP 1/3 |  |  |
| 4 | Delay Reporting Acceptor | [1] 5.1.1.2 | C.1 | [4] GAVDP 1/4 |  |  |

C.1: Excluded IF A2DP 2a/2 “A2DP v1.2”, otherwise Optional.
C.2: Excluded for this Role. Note: It is not permitted to be a delay reporting initiator for A2DP Source role.
Table 10: No longer used
Table 11: No longer used

##### 2.5.3.3 Requirements toward AVDTP Capabilities

Table 11a: AVDTP Capabilities (Initiator, Source)
Prerequisite: A2DP 1/1 “Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set configuration command | [1] 5.1.3 | M | [7] AVDTP 4/3 |  |  |
| 2 | Reconfigure command | [1] 5.1.3 | O | [7] AVDTP 4/5 |  |  |

Prerequisite: A2DP 1/1 “Source”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set configuration response | [1] 5.1.3 | M | [7] AVDTP 10/3 |  |  |
| 2 | Reconfigure response | [1] 5.1.3 | O | [7] AVDTP 10/5 |  |  |


### 2.6 Sink Features

Table 4: A2DP SNK Features
Prerequisite: A2DP 1/2 “Sink”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiate Connection Establishment |  |  | [2] 3.1.1 |  |  | O |  |  |
| 2 |  |  | Accept Connection Establishment |  |  | [2] 3.1.1 |  |  | M |  |  |
| 3 |  |  | Initiate Start Streaming |  |  | [2] 3.1.2 |  |  | O |  |  |
| 4 |  |  | Accept Start Streaming |  |  | [2] 3.1.2 |  |  | M |  |  |
| 5 |  |  | Receive Audio Stream |  |  | [1] 3.2.1 |  |  | M |  |  |
| 6 |  |  | Initiate Connection Release |  |  | [2] 3.1.3 |  |  | O |  |  |
| 7 |  |  | Accept Connection Release |  |  | [2] 3.1.3 |  |  | M |  |  |
| 8 |  |  | Initiate Suspend |  |  | [2] 3.1.4 |  |  | O |  |  |
| 9 |  |  | Accept Suspend |  |  | [2] 3.1.4 |  |  | O |  |  |
| 10 |  |  | SBC Decoder |  |  | [1] 4.3 |  |  | M |  |  |
| 10a |  |  | Receive and Decode Audio Stream |  |  | [1] 3.2.2 |  |  | O |  |  |
| 11 |  |  | SBC Configurations in 16 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | O |  |  |
| 12 |  |  | SBC Configurations in 32 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | O |  |  |
| 13 |  |  | SBC Configurations in 44.1 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | M |  |  |
| 14 |  |  | SBC Configurations in 48 kHz sampling frequency |  |  | [1] 4.3.2.1 |  |  | M |  |  |
| 15 |  |  | Delay Reporting |  |  | [1] 5.1.1.2 [2] 3.1.8 |  |  | C.1 |  |  |

C.1: Excluded IF A2DP 7a/2 “A2DP v1.2”, otherwise Mandatory.

### 2.7 SNK Implementation

Table 5: Supported Codec Interoperability Requirements in SNK
Prerequisite: A2DP 1/2 “Sink”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | SBC Decoder |  |  | [1] 4.3 & Appendix B [3] 3.2.4 |  |  | M |  |  |
| 1a |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3 |  |  | MPEG-1,2 Audio decoder |  |  | [1] 4.4 |  |  | O |  |  |
| 4 |  |  | MPEG-2,4 AAC decoder |  |  | [1] 4.5 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 |  |  | ATRAC family decoder |  |  | [1] 4.6 |  |  | O |  |  |
| 6 |  |  | MPEG-D USAC decoder |  |  | [6] 4.8 |  |  | C.2 |  |  |

C.1: No longer used.
C.2: Excluded IF A2DP 7a/2 “A2DP v1.2” OR A2DP 7a/3 “A2DP v1.3”, otherwise Optional.
Table 5a: Supported Codec Feature Interoperability Requirements in SNK
Prerequisite: A2DP 5/1 “SBC Decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Channel Mode – Mono |  |  | [1] 4.3.2.2 |  |  | M |  |  |
| 2 |  |  | Channel Mode – Dual Channel |  |  | [1] 4.3.2.2 |  |  | M |  |  |
| 3 |  |  | Channel Mode – Stereo |  |  | [1] 4.3.2.2 |  |  | M |  |  |
| 4 |  |  | Channel Mode – Joint Stereo |  |  | [1] 4.3.2.2 |  |  | M |  |  |
| 5 |  |  | Block Length 4 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 6 |  |  | Block Length 8 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 7 |  |  | Block Length 12 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 8 |  |  | Block Length 16 |  |  | [1] 4.3.2.3 |  |  | M |  |  |
| 9 |  |  | Subbands – 4 |  |  | [1] 4.3.2.4 |  |  | M |  |  |
| 10 |  |  | Subbands – 8 |  |  | [1] 4.3.2.4 |  |  | M |  |  |
| 11 |  |  | Allocation – SNR |  |  | [1] 4.3.2.5 |  |  | M |  |  |
| 12 |  |  | Allocation – Loudness |  |  | [1] 4.3.2.5 |  |  | M |  |  |


#### 2.7.1 MPEG-2,4 AAC Supported Codec Feature Interoperability Requirements

in SNK
Table 5g: Supported MPEG-2,4 AAC Object Type Interoperability Requirements in SNK
Prerequisite: A2DP 5/4 “MPEG-2,4 AAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | MPEG-2 AAC LC |  |  | [1] 4.5.2.1 |  |  | M |  |  |
| 2 |  |  | MPEG-4 AAC LC |  |  | [1] 4.5.2.1 |  |  | O |  |  |
| 3 |  |  | MPEG-4 AAC LTP |  |  | [1] 4.5.2.1 |  |  | O |  |  |
| 4 |  |  | MPEG-4 AAC scalable |  |  | [1] 4.5.2.1 |  |  | O |  |  |
| 5 |  |  | MPEG-4 HE-AAC |  |  | [6] 4.5.2.1 |  |  | O |  |  |
| 6 |  |  | MPEG-4 HE-AACv2 |  |  | [6] 4.5.2.1 |  |  | C.1 |  |  |
| 7 |  |  | MPEG-4 AAC-ELDv2 |  |  | [6] 4.5.2.1 |  |  | C.1 |  |  |

C.1: Excluded IF A2DP 7a/2 “A2DP v1.2” OR A2DP 7a/3 “A2DP v1.3”, otherwise Optional.
Prerequisite: A2DP 5/4 “MPEG-2,4 AAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 Channel |  |  | [1] 4.5.2.4 |  |  | M |  |  |
| 2 |  |  | 2 Channels |  |  | [1] 4.5.2.4 |  |  | M |  |  |
| 3 |  |  | 6 (5.1) Channels |  |  | [6] 4.5.2.4 |  |  | C.1 |  |  |
| 4 |  |  | 8 (7.1) Channels |  |  | [6] 4.5.2.4 |  |  | C.1 |  |  |

C.1: Excluded IF A2DP 7a/2 “A2DP v1.2” OR A2DP 7a/3 “A2DP v1.3”, otherwise Optional.
Table 5i: Supported MPEG-2,4 AAC Sampling Frequency Interoperability Requirements in SNK
Prerequisite: A2DP 5/4 “MPEG-2,4 AAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 8000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 2 |  |  | 11025 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 3 |  |  | 12000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 4 |  |  | 16000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 5 |  |  | 22050 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 6 |  |  | 24000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 7 |  |  | 32000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 8 |  |  | 44100 Hz |  |  | [1] 4.5.2.3 |  |  | M |  |  |
| 9 |  |  | 48000 Hz |  |  | [1] 4.5.2.3 |  |  | M |  |  |
| 10 |  |  | 64000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 11 |  |  | 88200 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |
| 12 |  |  | 96000 Hz |  |  | [1] 4.5.2.3 |  |  | O |  |  |

Table 5j: Supported MPEG-2,4 AAC Feature Interoperability Requirements in SNK
Prerequisite: A2DP 5/4 “MPEG-2,4 AAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Variable Bit Rate |  |  | [1] 4.5.2.5 [6] 4.5.2.6 |  |  | M |  |  |
| 2 |  |  | MPEG-D DRC |  |  | [6] 4.5.2.2 |  |  | C.1 |  |  |

C.1: Excluded IF A2DP 7a/2 “A2DP v1.2” OR A2DP 7a/3 “A2DP v1.3”, otherwise Optional IF A2DP 5g/2 “MPEG-4 AAC LC” OR A2DP 5g/3 “MPEG-4 AAC LTP” OR A2DP 5g/4 “MPEG-4 AAC scalable” OR A2DP 5g/5 “MPEG-4 HE-AAC” OR A2DP 5g/6 “MPEG-4 HE-AACv2” OR A2DP 5g/7 “MPEG-4 AAC-ELDv2”, otherwise Excluded.

#### 2.7.2 MPEG-D USAC Supported Codec Feature Interoperability Requirements

in SNK
Table 5k: Supported MPEG-D USAC Channel Interoperability Requirements in SNK
Prerequisite: A2DP 5/6 “MPEG-D USAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 1 Channel |  |  | [1] 4.8.2.3 |  |  | M |  |  |
| 2 |  |  | 2 Channels |  |  | [1] 4.8.2.3 |  |  | M |  |  |

Table 5l: Supported MPEG-D USAC Sampling Frequency Interoperability Requirements in SNK
Prerequisite: A2DP 5/6 “MPEG-D USAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 7350 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 2 |  |  | 8000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 3 |  |  | 8820 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 4 |  |  | 9600 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 5 |  |  | 11025 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 6 |  |  | 11760 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 7 |  |  | 12000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 8 |  |  | 12800 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 9 |  |  | 14700 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 10 |  |  | 16000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 11 |  |  | 17640 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 12 |  |  | 19200 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 13 |  |  | 22050 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 14 |  |  | 24000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 15 |  |  | 29400 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 16 |  |  | 32000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 17 |  |  | 35280 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 18 |  |  | 38400 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 19 |  |  | 44100 Hz |  |  | [1] 4.8.2.2 |  |  | M |  |  |
| 20 |  |  | 48000 Hz |  |  | [1] 4.8.2.2 |  |  | M |  |  |
| 21 |  |  | 58800 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 22 |  |  | 64000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 23 |  |  | 70560 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 24 |  |  | 76800 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 25 |  |  | 88200 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |
| 26 |  |  | 96000 Hz |  |  | [1] 4.8.2.2 |  |  | O |  |  |

Prerequisite: A2DP 5/6 “MPEG-D USAC decoder”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Variable Bit Rate |  |  | [6] 4.8.2.4 |  |  | M |  |  |
| 2 |  |  | MPEG-D DRC |  |  | [6] 4.8.2.1 |  |  | M |  |  |


#### 2.7.3 Requirements toward Other Profiles


##### 2.7.3.1 Requirements toward SDP

Table 12: SDP Attributes (Sink)
Prerequisite: A2DP 1/2 “Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | No longer used | N/A | N/A | N/A |  |  |
| 2 | ProtocolDescriptorList | [1] 5.3 | M | [5] SDP 9/2 |  |  |
| 3 | BluetoothProfileDescriptorList | [1] 5.3 | M | [5] SDP 9/14 |  |  |
| 4 | Supported Features | [1] 5.3 | O | N/A |  |  |


##### 2.7.3.2 Requirements toward GAVDP

Table 13: GAVDP Roles (Sink)
Prerequisite: A2DP 1/2 “Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initiator | [1] 5.1.1.1 | O | [4] GAVDP 1/1 |  |  |
| 2 | Acceptor | [1] 5.1.1.1 | M | [4] GAVDP 1/2 |  |  |
| 3 | Delay Reporting Initiator | [1] 5.1.1.2 | C.1 | [4] GAVDP 1/3 |  |  |
| 4 | Delay Reporting Acceptor | [1] 5.1.1.2 | C.2 | [4] GAVDP 1/4 |  |  |

C.1: Excluded IF A2DP 7a/2 “A2DP v1.2”, otherwise Mandatory.
C.2: Excluded for this Role. Note: It is not permitted to be a delay reporting acceptor for A2DP Sink role.
Table 14: No longer used
Table 15: No longer used
Table 15a: AVDTP Capabilities (Initiator, Sink)
Prerequisite: A2DP 1/2 “Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set configuration command | [1] 5.1.3 | C.1 | [7] AVDTP 4b/3 |  |  |
| 2 | Reconfigure command | [1] 5.1.3 | O | [7] AVDTP 4b/5 |  |  |

C.1: Mandatory IF A2DP 13/1 “Initiator”, otherwise not defined.
Table 15b: AVDTP Capabilities (Acceptor, Sink)
Prerequisite: A2DP 1/2 “Sink”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Set configuration response | [1] 5.1.3 | M | [7] AVDTP 10b/3 |  |  |
| 2 | Reconfigure response | [1] 5.1.3 | O | [7] AVDTP 10b/5 |  |  |


## 3 References

[1] Advanced Audio Distribution Profile (A2DP) Specification, Version 1.2 or later
[2] Generic Audio/Video Distribution Profile (GAVDP) Specification
[3] Advanced Audio Distribution Profile (A2DP) Test Suite
[4] ICS Proforma for Generic Audio/Video Distribution Profile (GAVDP)
[5] ICS Proforma for Service Discovery Protocol (SDP)
[6] Advanced Audio Distribution Profile (A2DP) Specification, Version 1.4 or later
[7] ICS Proforma for Audio/Video Distribution Transport Protocol (AVDTP)
[8] Advanced Audio Distribution Profile (A2DP) Specification, Version 1.3
[9] Advanced Audio Distribution Profile (A2DP) Specification, Version 1.3.2
[10] Advanced Audio Distribution Profile (A2DP) Specification, Version 1.4.1

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  | 0 |  |  | 1.00 |  |  | 2003-02-01 |  |  | Release for Voting Draft |  |
|  |  |  |  | Version 1.0 |  |  | 2003-05-01 |  |  | Updated title and header |  |
|  | 1 |  |  | 1.1.1r1 |  |  | 2004-12-16 |  |  | Editorial and format changes. |  |
|  |  |  | 1.1.2r0 | 1.1.2r0 |  | 2006-02-03 | 2006-02-03 |  |  | Editorial updates; remove spec version from title |  |
|  |  |  |  |  |  |  |  |  |  | TSE 910: Corrections to Tables 9-1 and 9-2 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 911:Remove “None” items in Tables 9-1 and 9-2 |  |
|  | 2 |  |  | 1.1.2 |  |  | 2006-06-12 |  |  | Prepare for publication. |  |
|  |  |  | 1.1.3r0 | 1.1.3r0 |  | 2006-10-01 | 2006-10-01 |  |  | TSE 1806: Corrections to Sec. 5 & 6 due to TSE 879 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 1886 Items 5.2.1, 6.2.1 change feature name |  |
|  |  |  |  |  |  |  |  |  |  | Inserted preliminary new table numbers in parens (x) |  |
|  |  |  |  |  |  |  |  |  |  | to comply with TSE 1979. |  |
|  |  |  | 1.1.3r1 |  |  | 2006-11-15 |  |  |  | Changed all references to be of type [x] |  |
|  |  |  |  |  |  |  |  |  |  | Removed implementation of 1762. |  |
|  |  |  | 1.1.3r2 |  |  | 2006-12-10 |  |  |  | Input reviewer’s comments |  |
|  |  |  |  |  |  |  |  |  |  | Added Table of Contents for clarity |  |
|  |  |  |  | 1.1.3r3 |  |  | 2006-12-14 |  |  | TSE 1886: ServiceClassIDList from Tables 3 and 8. |  |
|  | 3 |  |  | 1.1.3 |  |  | 2007-01-05 |  |  | Prepare for publication |  |
|  |  |  | 1.1.4r0-1 | 1.1.4r0-1 |  | 2008-02-08 | 2008-02-08 |  |  | TSE 1962: Add items ¾ and 8/4 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2267: Table 2, Table 7: add rows |  |
|  | 4 |  |  | 1.1.4 |  |  | 2008-04-15 |  |  | Prepare for publication |  |
|  |  |  |  | 1.0.5r0, |  | 2008-10-05 | 2008-10-05 |  | TSE 2659: C1 for Table 2/13 and 2/14 | TSE 2659: C1 for Table 2/13 and 2/14 |  |
|  |  |  |  | 1.2.5r0 |  |  |  |  |  |  |  |
|  | 5 |  |  | 1.0.5, 1.2.5 |  |  | 2008-11-25 |  |  | Prepare for publication. |  |
|  |  |  |  | 1.2.5a |  |  | 2010-01-25 |  |  | TSE 3272: Fix radio button functionality for Table 5/5 |  |
|  |  |  | 1.2.6r0 | 1.2.6r0 |  | 2011-02-25 | 2011-02-25 |  |  | TSE 4271: Table 2 and Table 7: Change spec ref. |  |
|  |  |  |  |  |  |  |  |  |  | sections |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4272: Add Table 0 to match TPG |  |
|  | 6 |  |  | 1.2.6 |  |  | 2011-07-21 |  |  | Prepare for publication. |  |
|  |  |  |  | 1.1.5 |  |  | 2009-12-19 |  |  | Release for Synchronization Voting Draft |  |
|  |  |  |  | 1.3.0r0 |  |  | 2011-02-15 |  |  | Prepare for publication |  |
|  |  |  |  | 1.3.0r1 |  |  | 2011-03-31 |  |  | Update after AV F2F |  |
|  |  |  | 1.3.0r2 | 1.3.0r2 |  | 2011-12-10 | 2011-12-10 |  |  | Merged for Core Spec 2.1 +EDR updates |  |
|  |  |  |  |  |  |  |  |  |  | ESR04 errata 938: Move test requirements from ICS |  |
|  |  |  |  |  |  |  |  |  |  | to Appendix in A2DP |  |
|  |  |  |  |  |  |  |  |  |  | ESR04 errata 879: Only the devices supporting SRC |  |
|  |  |  |  |  |  |  |  |  |  | role should be required to support inquiry, extension |  |
|  |  |  |  |  |  |  |  |  |  | of errata 872 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4602: Add else excluded to C1 of codec support |  |
|  |  |  |  |  |  |  |  |  |  | Tables 7 and 13 |  |
|  |  |  |  | 1.3.0r3 |  |  | 2012-02-20 |  |  | Updated to latest PICS template |  |
|  |  |  |  | 1.3.0r4 |  |  | 2012-04-02 |  |  | Updates to resolve BTI comments |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  | 1.3.0r4 |  |  | 2012-04-02 |  |  | Updates to resolve BTI comments |  |
|  |  |  | 1.3.0r5 | 1.3.0r5 |  | 2012-05-01 | 2012-05-01 |  |  | TSE 4274: Comment ID 12943. Add Tables 12a and |  |
|  |  |  |  |  |  |  |  |  |  | 13a for SBC feature declaration |  |
|  |  |  |  |  |  |  |  |  |  | Revert the table numbers that were changed in an |  |
|  |  |  |  |  |  |  |  |  |  | intermediate revision according to BTI feedback. |  |
|  |  |  |  |  |  |  |  |  |  | Sections renumbered. |  |
|  |  |  |  |  |  |  |  |  |  | Rename Non A2DP Codecs to Vendor Specific |  |
|  |  |  |  |  |  |  |  |  |  | Codecs |  |
|  |  |  | 1.3.0r6 |  |  | 2012-05-10 |  |  |  | TSE 4675: Comment ID 12979. Add ICS in Tables 2 |  |
|  |  |  |  |  |  |  |  |  |  | and 7 for rendering devices. Also separate |  |
|  |  |  |  |  |  |  |  |  |  | requirements in Table 12 and 13 based on this new |  |
|  |  |  |  |  |  |  |  |  |  | ICS distinction. |  |
|  |  |  | 1.3.0r7 |  |  | 2012-05-21 |  |  |  | Renumbered the remaining ICS Tables that needed to |  |
|  |  |  |  |  |  |  |  |  |  | be consistent with previous published numbering. |  |
|  |  |  |  |  |  |  |  |  |  | Changed X to N/A as appropriate. |  |
|  |  |  |  | 1.3.0r8 |  |  | 2012-06-07 |  |  | Changed the remaining “X” to Conditionals. |  |
|  |  |  | 1.3.0r9 | 1.3.0r9 |  | 2012-07-01 | 2012-07-01 |  |  | Editorial updates to align section numbering with |  |
|  |  |  |  |  |  |  |  |  |  | published ICS template. |  |
|  | 7 |  |  | 1.3.0 |  |  | 2012-07-24 |  |  | Prepare for publication. |  |
|  |  |  | 1.3.1.0r00 | 1.3.1.0r00 |  | 2015-05-20 | 2015-05-20 |  |  | ESR08: Added item 4 to Table 0 for A2DP 1.3.1 and |  |
|  |  |  |  |  |  |  |  |  |  | updated conditionals |  |
|  |  |  | 1.3.1.0r01 |  |  | 2015-05-27 |  |  |  | Reviewed by Alicia Courtney. Updated to current |  |
|  |  |  |  |  |  |  |  |  |  | document template. |  |
|  | 8 |  |  | 1.3.1.0 |  |  | 2015-07-14 |  |  | Prepared for TCRL 2015-1 publication |  |
|  |  |  | 1.3.1.1r00 | 1.3.1.1r00 |  | 2016-02-26 | 2016-02-26 |  |  | TSE 6895: Table 12 modified conditionals for items |  |
|  |  |  |  |  |  |  |  |  |  | 2a, 2c, and 2e and added references. |  |
|  |  |  |  |  |  |  |  |  |  | Added Table 0a for the X.Y.Z version items and |  |
|  |  |  |  |  |  |  |  |  |  | removed version 1.3.1 from Table 0 per the current |  |
|  |  |  |  |  |  |  |  |  |  | conventions. |  |
|  | 9 |  |  | 1.3.1.1 |  |  | 2016-07-13 |  |  | Prepared for TCRL 2016-1 publication. |  |
|  |  |  | 1.3.1.2r00 | 1.3.1.2r00 |  | 2017-03-29 | 2017-03-29 |  |  | TSE 7514: Updated capabilities for items 2a-2f to |  |
|  |  |  |  |  |  |  |  |  |  | Table 12. Updated status for items 2a, 2c, and 2e to |  |
|  |  |  |  |  |  |  |  |  |  | Table 12. |  |
|  |  |  |  |  |  |  |  |  |  | Modified conditionals (C.2-C.4) to Table 12 from |  |
|  |  |  |  |  |  |  |  |  |  | “otherwise Excluded” to “otherwise Optional”. |  |
|  |  |  | 1.3.1.2r01 |  |  | 2017-04-25 |  |  |  | Updated template. Replaced parentheses with |  |
|  |  |  |  |  |  |  |  |  |  | quotation marks to align with current ICS conventions. |  |
| 10 |  |  | 1.3.1.2 |  |  | 2017-07-03 |  |  |  | Approved by BTI. Prepared for TCRL 2017-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.3.1.3r00 |  |  | 2018-10-04 |  |  |  | TSE 10820 (rating 2): Added new ICS tables to |  |
|  |  |  |  |  |  |  |  |  |  | separate ICS versions by role. |  |
| 11 |  |  | 1.3.2.0r00 |  |  | 2018-11-09 |  |  |  | Updated version number to 1.3.2.0 to align with |  |
|  |  |  |  |  |  |  |  |  |  | adoption of specification version1.3.2. Added items |  |
|  |  |  |  |  |  |  |  |  |  | 2b/2 and 7b/2 for the new spec version. |  |
|  |  |  | 1.3.2.1 r00–r02 |  |  | 2019-04-09– 2019-06-21 |  |  |  | TSE 11675 (rating 2): Updated GAVDP Table 0 |  |
|  |  |  |  |  |  |  |  |  |  | references after TSE 11210. Aligned table numbering |  |
|  |  |  |  |  |  |  |  |  |  | to match historical TPG data. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
| 12 | 12 |  | 1.3.2.1 | 1.3.2.1 |  | 2019-07-28 |  | Approved by BTI. Prepared for TCRL 2019-1 |  |
|  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.3.2.2 r00–r01 |  |  | 2019-10-04 – 2019-10-29 |  | TSE 12659 (rating 2): Deleted Tables 10, 11, 14, and |  |
|  |  |  |  |  |  |  |  | 15 (and their related section headings) to remove |  |
|  |  |  |  |  |  |  |  | incorrect A2DP role dependencies. |  |
|  |  |  |  |  |  |  |  | TSE 12530 (rating 2): Deleted Tables 0 and 0a and |  |
|  |  |  |  |  |  |  |  | changed C.2 of 9/3 and 13/4 Delay Reporting |  |
|  |  |  |  |  |  |  |  | Initiator/Acceptor so that an invalid is not generated |  |
|  |  |  |  |  |  |  |  | when both roles are supported. |  |
| 13 |  |  | 1.3.2.2 |  |  | 2020-01-07 |  | Approved by BTI on 2019-11-17. Prepared for 2019-2 |  |
|  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.3.2.2ed2 r00–r01 |  |  | 2020-01-16 – 2020-03-27 |  | TSE 12974 (rating 1): Renumbered items in Table 3 |  |
|  |  |  |  |  |  |  |  | and Table 5 and updated conditionals in Table 3 that |  |
|  |  |  |  |  |  |  |  | needed to reflect those changes. |  |
|  |  |  |  |  |  |  |  | Updated document number, setting previous 1.3.2.2 |  |
|  |  |  |  |  |  |  |  | release as p13. Made minor editorials and formatting |  |
|  |  |  |  |  |  |  |  | changes. |  |
|  |  |  | 1.3.2.2 edition 2 |  |  | 2020-08-13 |  | Rolled back document numbering to reflect an edition |  |
|  |  |  |  |  |  |  |  | release, made minor formatting and template |  |
|  |  |  |  |  |  |  |  | editorials, and accepted all tracked changes. |  |
|  |  |  |  |  |  |  |  | Approved by BTI on 2020-08-13. Prepared for edition |  |
|  |  |  |  |  |  |  |  | 2 publication. |  |
|  |  |  |  | 1.3.2.2ed3 |  | 2021-01-13 |  | TSE 15954 (rating 1): Updated conditionals in version |  |
|  |  |  |  | r00 |  |  |  | tables for deprecation. |  |
|  |  |  |  | 1.3.2.2 |  | 2021-02-01 |  | Approved by BTI on 2021-01-13. Prepared for |  |
|  |  |  |  | edition 3 |  |  |  | edition 3 publication. |  |
|  |  |  | p14r00–r04 | p14r00–r04 |  | 2021-03-15 – 2021-06-11 |  | TSE 15972 (rating 1): Fixed typo in numbering in |  |
|  |  |  |  |  |  |  |  | Table 7b. |  |
|  |  |  |  |  |  |  |  | TSE 16974 (rating 1): Updated C.1 of Table 2, C.1 |  |
|  |  |  |  |  |  |  |  | and C.2 of Table 9, C.1 and C.2 of Table 13, C.2–C.4 |  |
|  |  |  |  |  |  |  |  | of Table 3, and C.1 of Table 3a to align with the latest |  |
|  |  |  |  |  |  |  |  | ICS template grammar. Also made other minor |  |
|  |  |  |  |  |  |  |  | consistency checker editorials. |  |
|  |  |  |  |  |  |  |  | Editorials to align with the latest D&W conventions. |  |
|  |  |  |  |  |  |  |  | Consistency checker and other template-related |  |
|  |  |  |  |  |  |  |  | editorials. |  |
| 14 |  |  | p14 |  |  | 2021-07-13 |  | Approved by BTI on 2021-06-03. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2021-1 publication. |  |
|  |  |  | p14ed2r00 |  |  | 2021-07-15 |  | TSE 17081 (rating 1): Changed section heading for |  |
|  |  |  |  |  |  |  |  | 3.1.3 from “Non-A2DP Codecs” to “Vendor Specific |  |
|  |  |  |  |  |  |  |  | Codecs”. |  |
|  |  |  | p14 edition 2 |  |  | 2021-08-19 |  | Approved by BTI on 2021-08-19. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  | p14ed3r00 |  |  | 2021-10-13 |  | TSE 17522 (rating 1): Changed KHz to kHz. Changed |  |
|  |  |  |  |  |  |  |  | sampling frequency rate to sampling frequency. |  |
|  |  |  |  |  |  |  |  | Inverted the Excluded logic for conditionals that apply |  |
|  |  |  |  |  |  |  |  | to A2DP v1.3 or later for forward compatibility. |  |
|  |  |  |  |  |  |  |  | Removed unused reference. |  |
|  |  |  | p14ed3r01 |  |  | 2021-10-18 |  | TSE 17724 (rating 1): Consistency checker updates |  |
|  |  |  |  |  |  |  |  | throughout the document. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p14 edition 3 | p14 edition 3 |  | 2021-11-09 |  | Approved by BTI on 2021-11-08. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 3 publication. |  |
|  |  |  | p15r00–r07 |  |  | 2021-12-10 – 2022-05-23 |  | Incorporated CR |  |
|  |  |  |  |  |  |  |  | A2DP NewAACObjTypes.ICS.CRr13, the CR for |  |
|  |  |  |  |  |  |  |  | _ A2DP v1.4, approved by BTI on 2021-11-01, which |  |
|  |  |  |  |  |  |  |  | includes the following TSEs: |  |
|  |  |  |  |  |  |  |  | TSE 17015 (rating 4): Added coverage for mandated |  |
|  |  |  |  |  |  |  |  | codec related to error codes in AVDTP. Added new |  |
|  |  |  |  |  |  |  |  | item 2a/4 and revised C.1. Added new section under |  |
|  |  |  |  |  |  |  |  | Source Features “Requirements toward AVDTP |  |
|  |  |  |  |  |  |  |  | Capabilities”, including new Tables 11a and 11b. |  |
|  |  |  |  |  |  |  |  | Added new item 7a/4 and revised C.1. Added new |  |
|  |  |  |  |  |  |  |  | section under Sink Features “Requirements toward |  |
|  |  |  |  |  |  |  |  | AVDTP Capabilities”, including new Tables 15a and |  |
|  |  |  |  |  |  |  |  | 15b. Added new references to A2DP v1.4 and the |  |
|  |  |  |  |  |  |  |  | AVDTP ICS. |  |
|  |  |  |  |  |  |  |  | TSE 17519 (rating 1): Renamed “Optional Codecs” to |  |
|  |  |  |  |  |  |  |  | “Externally Referenced Codecs” per Legal. |  |
|  |  |  |  |  |  |  |  | TSE 17521 (rating 3): Cleaned up optional codec |  |
|  |  |  |  |  |  |  |  | items. Updated description of 4/10a. Removed item |  |
|  |  |  |  |  |  |  |  | 3/2, updated status column for 3/3–3/8, and added 3/9 |  |
|  |  |  |  |  |  |  |  | and 3/10; set C.1 to “No longer used” and added C.5. |  |
|  |  |  |  |  |  |  |  | Removed 5/1a and 5/2, updated status column for |  |
|  |  |  |  |  |  |  |  | 5/3–5/5, and added 5/6; set C.1 to “No longer used”. |  |
|  |  |  |  |  |  |  |  | TSE 17523 (rating 3): Added MPEG-2,4 and MPEG-D |  |
|  |  |  |  |  |  |  |  | features. Added two new subsections to the “SRC |  |
|  |  |  |  |  |  |  |  | Implementation” section, including new Tables 3g, 3h, |  |
|  |  |  |  |  |  |  |  | 3i, 3j, 3k, 3l, and 3m. Added two new subsections to |  |
|  |  |  |  |  |  |  |  | the “SNK Implementation” section, including new |  |
|  |  |  |  |  |  |  |  | Tables 5g, 5h, 5i, 5j, 5k, 5l, and 5m. |  |
|  |  |  |  |  |  |  |  | Incorporated Test Issue 18118, removing sections |  |
|  |  |  |  |  |  |  |  | containing Tables 3b, 3c, 3d, 3e, and the placeholder |  |
|  |  |  |  |  |  |  |  | for 3f, and Tables 5b, 5c, 5d, 5e, and the placeholder |  |
|  |  |  |  |  |  |  |  | for 5f. Updated rev history comment for TSE 17523 |  |
|  |  |  |  |  |  |  |  | accordingly. |  |
|  |  |  |  |  |  |  |  | TSE 18374 (rating 1): Removed “is supported” |  |
|  |  |  |  |  |  |  |  | language globally to align with the latest ICS |  |
|  |  |  |  |  |  |  |  | conventions. (Note: applied to AAC Object Types– |  |
|  |  |  |  |  |  |  |  | related material, too.) |  |
|  |  |  |  |  |  |  |  | TSE 18610 (rating 1): Per Erratum 18398, removed |  |
|  |  |  |  |  |  |  |  | Appendix A to consolidate all tables into the main part |  |
|  |  |  |  |  |  |  |  | of the document. Removed Appendix D–related |  |
|  |  |  |  |  |  |  |  | Requirements column from Tables 3 and 5. Deleted |  |
|  |  |  |  |  |  |  |  | Manufacturer Declaration of Codecs material that |  |
|  |  |  |  |  |  |  |  | remained from the AAC Object Types CR. |  |
|  |  |  |  |  |  |  |  | TSE 18683 (rating 1): Per Erratum 18481, updated |  |
|  |  |  |  |  |  |  |  | terminology for codecs to finalized language. |  |
|  |  |  |  |  |  |  |  | Incorporated Test Issue 18118, removing sections |  |
|  |  |  |  |  |  |  |  | containing Tables 3b, 3c, 3d, 3e, and the placeholder |  |
|  |  |  |  |  |  |  |  | for 3f, and Tables 5b, 5c, 5d, 5e, and the placeholder |  |
|  |  |  |  |  |  |  |  | for 5f. Updated rev history comment for TSE 17523 |  |
|  |  |  |  |  |  |  |  | accordingly. |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | Editorials, including aligning the copyright page to the |  |
|  |  |  |  |  |  |  |  |  |  | latest DNMD and revising the Acknowledgments list. |  |
| 15 |  |  | p15 |  |  | 2022-06-28 |  |  |  | A2DP v1.4 adopted by the BoD on 2022-06-21. |  |
|  |  |  |  |  |  |  |  |  |  | Prepared for TCRL 2022-1 publication. |  |
|  |  |  | p16r00–r02 |  |  | 2022-07-21 – 2022-11-28 |  |  |  | TSE 19010 (rating 2): Per E18994 “Removal of |  |
|  |  |  |  |  |  |  |  |  |  | transcoding requirements”, removed items 3, 5, 7, and |  |
|  |  |  |  |  |  |  |  |  |  | 9, and associated C.2–C.5, from Table 3. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 20368 (rating 2): Updated status of 3/10 and |  |
|  |  |  |  |  |  |  |  |  |  | added C.6. Updated status of 3g/5, 3g/6, and 3g/7 |  |
|  |  |  |  |  |  |  |  |  |  | and added C.1. Updated status of 3h/3 and 3h/4 and |  |
|  |  |  |  |  |  |  |  |  |  | added C.2. Updated C.1 for Table 3j. Updated status |  |
|  |  |  |  |  |  |  |  |  |  | of 5/6 and added C.2. Updated status of 5g/6 and |  |
|  |  |  |  |  |  |  |  |  |  | 5g/7 and added C.1. Updated status of 5h/3 and 5h/4 |  |
|  |  |  |  |  |  |  |  |  |  | and added C.1. Updated C.1 for Table 5j. |  |
| 16 |  |  | p16 |  |  | 2023-02-07 |  |  |  | Approved by BTI on 2022-12-19. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  |  |  | 2022-2 publication. |  |
|  |  |  | p16ed2r00– r03 |  |  | 2023-02-07 – 2023-02-23 |  |  |  | TSE 22628 (rating 1): Updated to align with current |  |
|  |  |  |  |  |  |  |  |  |  | ICS conventions, moved version tables to the |  |
|  |  |  |  |  |  |  |  |  |  | beginning of the document, and updated the |  |
|  |  |  |  |  |  |  |  |  |  | Withdrawal date for A2DP 1.3 and A2DP 1.3.1 from |  |
|  |  |  |  |  |  |  |  |  |  | 2023-02-01 to 2024-02-01. |  |
|  |  |  | p16 edition 2 |  |  | 2023-02-27 |  |  |  | Approved by BTI on 2023-02-23. Prepared for |  |
|  |  |  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  |  | p16ed3r00– |  |  | 2023-03-09 – |  |  | TSE 22863 (rating 1): Corrected the deprecation date |  |
|  |  |  |  | r01 |  |  | 2023-04-13 |  |  | for A2DP v1.3. Affected tables are Tables 2a and 7a. |  |
|  |  |  | p16 edition 3 | p16 edition 3 |  | 2023-04-14 | 2023-04-14 |  |  | Approved by BTI on 2023-04-13. Prepared for |  |
|  |  |  |  |  |  |  |  |  |  | edition 3 publication. |  |
|  |  |  | p17r00–r08 |  |  | 2024-10-08 – 2025-04-23 |  |  |  | TSE 25979 (rating 2): Added Section 1.3 and |  |
|  |  |  |  |  |  |  |  |  |  | Table 1d listing core configuration requirements, and |  |
|  |  |  |  |  |  |  |  |  |  | made minor updates for formatting and style. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 27269 (rating 2): Updated the table title, added |  |
|  |  |  |  |  |  |  |  |  |  | the missing "v" in the Version value, and updated the |  |
|  |  |  |  |  |  |  |  |  |  | Reference value for Tables 2a, 2b, 7a, and 7b. |  |
|  |  |  |  |  |  |  |  |  |  | Deleted the prerequisite for Tables 2b and 7b. Added |  |
|  |  |  |  |  |  |  |  |  |  | Item A2DP 2b/3 and condition C.2 to Table 2b and |  |
|  |  |  |  |  |  |  |  |  |  | added Item A2DP 7b/3 and condition C.2 to Table 7b |  |
|  |  |  |  |  |  |  |  |  |  | to cover A2DP v1.4.1. Updated the references list. |  |
|  |  |  |  |  |  |  |  |  |  | Incorporated editorials to align the document with the |  |
|  |  |  |  |  |  |  |  |  |  | latest ICS template: Updated Section 1 and added a |  |
|  |  |  |  |  |  |  |  |  |  | section heading for the ICS declarations section. |  |
| 17 |  |  | p17 |  |  | 2025-07-08 |  |  |  | Approved by BTI on 2025-05-30. A2DP v1.4.1 |  |
|  |  |  |  |  |  |  |  |  |  | adopted by the BoD on 2025-06-30. Prepared for |  |
|  |  |  |  |  |  |  |  |  |  | TCRL pkg100 publication. |  |
|  |  |  | p18r00–r01 |  |  | 2025-12-04 – 2025-12-31 |  |  | TSE 28346 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |  |  |
| 18 |  |  | p18 |  |  | 2026-02-17 |  |  | Approved by BTI on 2026-01-22. Prepared for TCRL pkg102 publication. |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Rüdiger Mosig |  |  | Berner and Mattner |  |
|  | Tharon Hall |  |  | Bluetooth SIG, Inc. |  |
|  | Alicia Courtney |  |  | Broadcom |  |
|  | Ash Kapur |  |  | Broadcom |  |
|  | Jiny Bradshaw |  |  | CSR |  |
|  | Allan Madsen |  |  | CSR |  |
|  | David Trainor |  |  | CSR |  |
|  | Akira Miyajima |  |  | Denso |  |
|  | Christof Fersch |  |  | Dolby Laboratories |  |
|  | Morgan Lindqvist |  |  | Ericsson |  |
|  | Fisseha Mekuria |  |  | Ericsson |  |
|  | Yuan Quinton |  |  | Marvell |  |
|  | Tsuyoshi Okada |  |  | Matsushita Electric Industrial |  |
|  | Thomas Karlsson |  |  | Mecel |  |
|  | Stephen Raxter |  |  | National Analysis Center |  |
|  | Janne Hamalainen |  |  | Nokia |  |
|  | Kalervo Kontola |  |  | Nokia |  |
|  | Jurgen Schnitzler |  |  | Nokia |  |
|  | Thierry Wœlfflé |  |  | Parrot |  |
|  | Frans de Bont |  |  | Philips |  |
|  | Christian Bouffioux |  |  | Philips |  |
|  | Emmanuel Mellery |  |  | Philips |  |
|  | Scott Walsh |  |  | Plantronics |  |
|  | Brian Gix |  |  | Qualcomm |  |
|  | John Larkin |  |  | Qualcomm |  |
|  | Wilhelm Hagg |  |  | Sony |  |
|  | Masakazu Hattori |  |  | Sony |  |
|  | Atsushi Ichise |  |  | Sony |  |
|  | Harumi Kawamura |  |  | Sony |  |
|  | Yoshiyuki Nezu |  |  | Sony |  |
|  | Hiroyasu Noguchi |  |  | Sony |  |
|  | Masahiko Seki |  |  | Sony |  |
|  | Siân James |  |  | Symbian |  |
|  | Yoshinari Kumaki |  |  | Toshiba |  |
|  | Yoshiaki Takabatake |  |  | Toshiba |  |
|  | Ichiro Tomoda |  |  | Toshiba |  |
