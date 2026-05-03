# HFP.ICS.p26

> Source: PDF converted via PyMuPDF.

---

Hands-Free Profile (HFP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: HFP.ICS.p26 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Audio, Telephony, and Automotive Working Group ▪ Published during TCRL: TCRL.102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2005–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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
Table 0a: AG X.Y Versions
Prerequisite: HFP 1/1 “Audio Gateway (AG)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Hands-Free Profile 1.5 |  |  | [1] |  |  | Deprecated 2021-02-01. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | Hands-Free Profile 1.6 |  |  | [1] |  |  | Deprecated 2021-02-01. Withdrawn 2023-02-01. |  |  |
| 3 |  |  | Hands-Free Profile 1.7 |  |  | [2] |  |  | C.1, C.2 |  |  |
| 4 |  |  | Hands-Free Profile 1.8 |  |  | [4] |  |  | C.1 |  |  |
| 5 |  |  | Hands-Free Profile 1.9 |  |  | [5] |  |  | C.1 |  |  |
| 6 |  |  | Hands-Free Profile 1.10 |  |  | [10] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated
2021-02-01. Withdrawn 2024-02-01.
Table 0b: HF X.Y Versions
Prerequisite: HFP 1/2 “Hands-Free (HF)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Hands-Free Profile 1.5 |  |  | [1] |  |  | Deprecated 2021-02-01. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | Hands-Free Profile 1.6 |  |  | [1] |  |  | Deprecated 2021-02-01. Withdrawn 2023-02-01. |  |  |
| 3 |  |  | Hands-Free Profile 1.7 |  |  | [2] |  |  | C.1, C.2 |  |  |
| 4 |  |  | Hands-Free Profile 1.8 |  |  | [4] |  |  | C.1 |  |  |
| 5 |  |  | Hands-Free Profile 1.9 |  |  | [5] |  |  | C.1 |  |  |
| 6 |  |  | Hands-Free Profile 1.10 |  |  | [10] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated
2021-02-01. Withdrawn 2024-02-01.
Prerequisite: HFP 1/1 “Audio Gateway (AG)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Hands-Free Profile 1.7.1** |  |  | [2] |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 2 |  |  | Hands-Free Profile 1.5.1** |  |  | [2] |  |  | Deprecated 2022-02-01. Withdrawn 2023-02-01. |  |  |
| 3 |  |  | Hands-Free Profile 1.6.1** |  |  | [2] |  |  | Deprecated 2022-02-01. Withdrawn 2024-02-01. |  |  |
| 4 |  |  | Hands-Free Profile 1.7.2 |  |  | [2] |  |  | C.1, C.2 |  |  |

C.1: Mandatory IF HFP 0a/3 “Hands-Free Profile 1.7”, otherwise Excluded.
C.2: Excluded after Deprecation or Withdrawal. Deprecated 2029-02-01. Withdrawn 2031-02-01.
Table 0d: HF X.Y.Z Versions
Prerequisite: HFP 1/2 “Hands-Free (HF)”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Hands-Free Profile 1.7.1** |  |  | [2] |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 2 |  |  | Hands-Free Profile 1.5.1** |  |  | [2] |  |  | Deprecated 2022-02-01. Withdrawn 2023-02-01. |  |  |
| 3 |  |  | Hands-Free Profile 1.6.1** |  |  | [2] |  |  | Deprecated 2022-02-01. Withdrawn 2024-02-01. |  |  |
| 4 |  |  | Hands-Free Profile 1.7.2 |  |  | [2] |  |  | C.1, C.2 |  |  |

C.1: Mandatory IF HFP 0b/3 “Hands-Free Profile 1.7”, otherwise Excluded.
C.2: Excluded after Deprecation or Withdrawal. Deprecated 2029-02-01. Withdrawn 2031-02-01.

### 2.2 Core Configuration

Table 0e: Core Configuration Requirements

|  | Item |  |  | Core Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.1 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.1 |  |  | C.2 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”.
C.2: Excluded for this Profile.
C.3: Mandatory for this Profile.
** Deprecated items will not appear in the Bluetooth SIG qualification tool after the next TCRL following the deprecation date.

### 2.3 Roles

Table 1: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Audio Gateway (AG) |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 2 |  |  | Hands-Free (HF) |  |  | [1] 2.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.4 Audio Gateway role

Table 2: Capabilities of the AG
Prerequisite: HFP 1/1 “Audio Gateway (AG)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connection management |  |  | [1] 4.2, 4.3 |  |  | M |  |  |
| 1a |  |  | SLC initiation during active ongoing call |  |  | [1] 4.2 |  |  | O |  |  |
| 2 |  |  | Phone status information |  |  | [1] 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10 |  |  | M |  |  |
| 3 |  |  | Audio Connection handling |  |  | [1] 4.11, 4.12 |  |  | M |  |  |
| 3a |  |  | Audio Connection establishment independent of call processing |  |  | [1] 4.11, 4.12 |  |  | O |  |  |
| 3b |  |  | eSCO support in Audio Connection |  |  | [1] 5.7.1 [5] 6.7.1 |  |  | M |  |  |
| 3c |  |  | Codec Negotiation |  |  | [1] 4.11 |  |  | C.7 |  |  |
| 4a |  |  | Accept an incoming voice call (in-band ring) |  |  | [1] 4.13 |  |  | C.1 |  |  |
| 4b |  |  | Accept an incoming voice call (no in-band ring) |  |  | [1] 4.13 |  |  | C.1 |  |  |
| 4c |  |  | Capability to change the “in-band ring” settings |  |  | [1] 4.13 |  |  | O |  |  |
| 5 |  |  | Reject an incoming voice call |  |  | [1] 4.14 |  |  | O |  |  |
| 6 |  |  | Terminate a call |  |  | [1] 4.15 |  |  | M |  |  |
| 7 |  |  | Audio Connection transfer during an ongoing call |  |  | [1] 4.16, 4.17 |  |  | M |  |  |
| 7a |  |  | HF-initiated Audio transfer to AG during ongoing call |  |  | [1] 4.17 |  |  | O |  |  |
| 7b |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 8 |  |  | Place a call with the phone number supplied by the HF |  |  | [1] 4.18 |  |  | M |  |  |
| 9 |  |  | Place a call using memory dialing |  |  | [1] 4.19 |  |  | M |  |  |
| 10 |  |  | Place a call to the last number dialed |  |  | [1] 4.20 |  |  | M |  |  |
| 11 |  |  | Call Waiting notification |  |  | [1] 4.21 |  |  | M |  |  |
| 12 |  |  | Three Way Calling |  |  | [1] 4.22 |  |  | O |  |  |
| 12a |  |  | User Busy (AT+CHLD value 0) |  |  | [1] 4.22 |  |  | C.3 |  |  |
| 12b |  |  | Call Hold Handling (AT+CHLD value 1,2) |  |  | [1] 4.22 |  |  | C.2 |  |  |
| 12c |  |  | Three Way Call (AT+CHLD value 3) |  |  | [1] 4.22 |  |  | C.3 |  |  |
| 12d |  |  | Explicit Call Transfer (AT+CHLD value 4) |  |  | [1] 4.22 |  |  | C.3 |  |  |
| 13 |  |  | Calling Line Identification (CLI) |  |  | [1] 4.23 |  |  | M |  |  |
| 14 |  |  | Echo Canceling (EC) and Noise Reduction (NR) |  |  | [1] 4.24 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 |  |  | Voice recognition activation |  |  | [1] 4.25 |  |  | O |  |  |
| 15a |  |  | Initiate voice recognition from AG |  |  | [1] 4.25 |  |  | C.6 |  |  |
| 15b |  |  | Autonomous voice deactivation |  |  | [1] 4.25 |  |  | C.6 |  |  |
| 15c |  |  | Enhanced Voice Recognition Status |  |  | [4] 4.25 [5] 4.26 |  |  | C.14 |  |  |
| 15d |  |  | Voice Recognition Text |  |  | [4] 4.25 |  |  | C.13 |  |  |
| 16 |  |  | Attach a phone number for a voice tag |  |  | [1] 4.26 [5] 4.27 |  |  | O |  |  |
| 17 |  |  | Ability to transmit DTMF codes |  |  | [1] 4.27 [5] 4.28 |  |  | M |  |  |
| 18a |  |  | Remote audio volume control – speaker |  |  | [1] 4.28.1 [5] 4.29.1 |  |  | O |  |  |
| 18b |  |  | Remote audio volume control – microphone |  |  | [1] 4.28.1 [5] 4.29.1 |  |  | O |  |  |
| 18c |  |  | Volume level synchronization – speaker and microphone |  |  | [1] 4.28.2 [5] 4.29.2 |  |  | C.5 |  |  |
| 19 |  |  | Response and Hold |  |  | [1] 4.29 [5] 4.30 |  |  | O |  |  |
| 20 |  |  | Subscriber Number Information |  |  | [1] 4.30 [5] 4.31 |  |  | M |  |  |
| 21a |  |  | Enhanced Call Status |  |  | [1] 4.31 [5] 4.32 |  |  | C.4 |  |  |
| 21b |  |  | Enhanced Call Control |  |  | [1] 4.32 [5] 4.33 |  |  | C.3 |  |  |
| 21c |  |  | Enhanced Call Status with limited network notification |  |  | [1] 4.31 [5] 4.32 |  |  | C.4 |  |  |
| 22 |  |  | Support for automatic link loss recovery |  |  | [1] 4.2 |  |  | O |  |  |
| 23 |  |  | Individual Indicator Activation |  |  | [1] 4.34 [4] 4.35 [5] 4.34 |  |  | M |  |  |
| 24 |  |  | Wide Band Speech service |  |  | [1] 5.7 [5] 6.7 |  |  | O |  |  |
| 25 |  |  | Support roaming function |  |  | [1] 4.6 |  |  | O |  |  |
| 26 |  |  | HF Indicators |  |  | [2] 4.35 [4] 4.36 [5] 4.35 |  |  | O |  |  |
| 27 |  |  | Support CVSD eSCO S4 setting |  |  | [2] 5.7.3 [5] 6.7.3 |  |  | M |  |  |
| 28 |  |  | Reserved Fields and RFU Bits |  |  | [5] 1.4.2 |  |  | C.15 |  |  |
| 29 |  |  | Super Wide Band Speech |  |  | [5] 6.7 |  |  | C.16 |  |  |
| 30 |  |  | Call Forwarding |  |  | [10] 4.36 |  |  | C.17 |  |  |
| 31 |  |  | Call Duration Information |  |  | [10] 4.37 |  |  | C.17 |  |  |
| 32 |  |  | Multiparty Call Duration |  |  | [10] 4.37 |  |  | C.18 |  |  |

C.2: Mandatory IF HFP 2/12 “Three Way Calling”, otherwise Excluded.
C.3: Optional IF HFP 2/12 “Three Way Calling”, otherwise Excluded.
C.4: Mandatory to support one and only one.
C.5: Mandatory IF HFP 2/18a “Remote audio volume control – speaker” OR HFP 2/18b “Remote audio
volume control – microphone”, otherwise Optional.
C.6: Optional IF HFP 2/15 “Voice recognition activation”, otherwise Excluded.
C.7: Mandatory IF HFP 2/24 “Wide Band Speech service” OR HFP 2/29 “Super Wide Band Speech”,
otherwise Optional.
C.8–C.12: No longer used.
C.13: Optional IF HFP 2/15c “Enhanced Voice Recognition Status”, otherwise Excluded.
C.14: Excluded IF HFP 0a/3 “Hands-Free Profile 1.7”, otherwise Optional IF HFP 2/15 “Voice recognition
activation”, otherwise Excluded.
C.15: Excluded IF HFP 0a/3 “Hands-Free Profile 1.7” OR HFP 0a/4 “Hands-Free Profile 1.8”, otherwise
Mandatory.
C.16: Excluded IF HFP 0a/3 “Hands-Free Profile 1.7” OR HFP 0a/4 “Hands-Free Profile 1.8”, otherwise
Optional.
C.17: Excluded IF HFP 0a/3 “Hands-Free Profile 1.7” OR HFP 0a/4 “Hands-Free Profile 1.8” OR HFP
0a/5 “Hands-Free Profile 1.9”, otherwise Optional.
C.18: Optional IF HFP 2/31 “Call Duration Information” AND HFP 2/12c “Three Way Call (AT+CHLD
value 3)”, otherwise Excluded.

### 2.5 Hands-Free role

Table 3: Capabilities of the HF
Prerequisite: HFP 1/2 “Hands-Free (HF)”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connection management |  |  | [1] 4.2, 4.3 |  |  | M |  |  |
| 2a |  |  | Phone status information (“service” and “call” indicators) |  |  | [1] 4.4, 4.10 |  |  | M |  |  |
| 2b |  |  | Phone status information (“callsetup” indicator) |  |  | [1] 4.10 |  |  | O |  |  |
| 2c |  |  | Accept indicator of signal strength |  |  | [1] 4.5 |  |  | O |  |  |
| 2d |  |  | Accept indicator of roaming state (“roam:”) |  |  | [1] 4.6 |  |  | O |  |  |
| 2e |  |  | Accept indicator of battery level (“battchg”) |  |  | [1] 4.7 |  |  | O |  |  |
| 2f |  |  | Accept indicator of operator selection |  |  | [1] 4.8 |  |  | O |  |  |
| 3 |  |  | Audio Connection handling |  |  | [1] 4.11, 4.12 |  |  | M |  |  |
| 3a |  |  | Audio Connection establishment independent of call processing |  |  | [1] 4.11, 4.12 |  |  | O |  |  |
| 3b |  |  | eSCO support in Audio Connection |  |  | [1] 5.7.1 [5] 6.7.1 |  |  | M |  |  |
| 3c |  |  | Codec Negotiation |  |  | [1] 4.11 |  |  | C.5 |  |  |
| 4a |  |  | Accept an incoming voice call (in-band ring) |  |  | [1] 4.13 |  |  | M |  |  |
| 4b |  |  | Accept an incoming voice call (no in-band ring) |  |  | [1] 4.13 |  |  | M |  |  |
| 4c |  |  | Accept an incoming voice call (in-band ring muting) |  |  | [1] 4.13 |  |  | O |  |  |
| 5 |  |  | Reject an incoming voice call |  |  | [1] 4.14 |  |  | M |  |  |
| 6 |  |  | Terminate a call |  |  | [1] 4.15 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 |  |  | Audio Connection transfer during an ongoing call |  |  | [1] 4.16, 4.17 |  |  | M |  |  |
| 7a |  |  | HF-initiated Audio transfer to AG during ongoing call |  |  | [1] 4.17 |  |  | O |  |  |
| 8 |  |  | Place a call with the phone number supplied by the HF |  |  | [1] 4.18 |  |  | O |  |  |
| 9 |  |  | Place a call using memory dialing |  |  | [1] 4.19 |  |  | O |  |  |
| 10 |  |  | Place a call to the last number dialed |  |  | [1] 4.20 |  |  | O |  |  |
| 11 |  |  | Call Waiting notification |  |  | [1] 4.21 |  |  | O |  |  |
| 12 |  |  | Three Way Calling |  |  | [1] 4.22 |  |  | O |  |  |
| 12a |  |  | Three way calling (AT+CHLD values 0) |  |  | [1] 4.22 |  |  | C.2 |  |  |
| 12b |  |  | Three way calling (AT+CHLD values 1 and 2) |  |  | [1] 4.22 |  |  | C.1 |  |  |
| 12c |  |  | Three way calling (AT+CHLD value 3) |  |  | [1] 4.22 |  |  | C.2 |  |  |
| 12d |  |  | Three way calling (AT+CHLD value 4) |  |  | [1] 4.22 |  |  | C.2 |  |  |
| 12e |  |  | Originate new call with established call in progress |  |  | [1] 4.22 |  |  | C.2 |  |  |
| 13 |  |  | Calling Line Identification (CLI) |  |  | [1] 4.23 |  |  | O |  |  |
| 14 |  |  | Echo Canceling (EC) and Noise Reduction (NR) |  |  | [1] 4.24 |  |  | O |  |  |
| 15 |  |  | Voice recognition activation/deactivation |  |  | [1] 4.25 |  |  | O |  |  |
| 15a |  |  | Enhanced Voice Recognition Status |  |  | [4] 4.25 [5] 4.26 |  |  | C.10 |  |  |
| 15b |  |  | Voice Recognition Text |  |  | [4] 4.25 |  |  | C.11 |  |  |
| 16 |  |  | Attach a phone number for a voice tag |  |  | [1] 4.26 [5] 4.27 |  |  | O |  |  |
| 17 |  |  | Ability to transmit DTMF codes |  |  | [1] 4.27 [5] 4.28 |  |  | O |  |  |
| 18a |  |  | Remote audio volume control – speaker |  |  | [1] 4.28.1 [5] 4.29.1 |  |  | O |  |  |
| 18b |  |  | Remote audio volume control – microphone |  |  | [1] 4.28.1 [5] 4.29.1 |  |  | O |  |  |
| 18c |  |  | Volume level synchronization – speaker |  |  | [1] 4.28.2 [5] 4.29.2 |  |  | C.3 |  |  |
| 18d |  |  | Volume level synchronization – microphone |  |  | [1] 4.28.2 [5] 4.29.2 |  |  | C.4 |  |  |
| 18e |  |  | HF informs AG about local changes of audio volume |  |  | [1] 4.28.2 [5] 4.29.2 |  |  | O |  |  |
| 18f |  |  | HF informs AG about local changes of microphone gain |  |  | [1] 4.28.2 [5] 4.29.2 |  |  | O |  |  |
| 19 |  |  | Response and Hold |  |  | [1] 4.29 [5] 4.30 |  |  | O |  |  |
| 20 |  |  | Subscriber Number Information |  |  | [1] 4.30 [5] 4.31 |  |  | O |  |  |
| 21a |  |  | Enhanced Call Status |  |  | [1] 4.31 [5] 4.32 |  |  | O |  |  |
| 21b |  |  | Enhanced Call Control |  |  | [1] 4.32 [5] 4.33 |  |  | C.2 |  |  |
| 22 |  |  | Support for automatic link loss recovery |  |  | [1] 4.3 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23 |  |  | Individual Indicator Activation |  |  | [1] 4.34 [4] 4.35 [5] 4.34 |  |  | O |  |  |
| 24 |  |  | Wide Band Speech service |  |  | [1] 5.7 [5] 6.7 |  |  | O |  |  |
| 25 |  |  | HF Indicators |  |  | [2] 4.35 [4] 4.36 [5] 4.35 |  |  | O |  |  |
| 26 |  |  | Support CVSD eSCO S4 setting |  |  | [2] 5.7.3 [5] 6.7.3 |  |  | M |  |  |
| 27 |  |  | Reserved Fields and RFU Bits |  |  | [5] 1.4.2 |  |  | C.12 |  |  |
| 28 |  |  | Super Wide Band Speech |  |  | [5] 6.7 |  |  | C.13 |  |  |
| 29 |  |  | Call Forwarding |  |  | [10] 4.36 |  |  | C.14 |  |  |
| 30 |  |  | Call Duration Information |  |  | [10] 4.37 |  |  | C.14 |  |  |
| 31 |  |  | Multiparty Call Duration |  |  | [10] 4.37 |  |  | C.15 |  |  |

C.1: Mandatory IF HFP 3/12 “Three Way Calling”, otherwise Excluded.
C.2: Optional IF HFP 3/12 “Three Way Calling”, otherwise Excluded.
C.3: Mandatory IF HFP 3/18a “Remote audio volume control – speaker” OR HFP 3/18b “Remote audio
volume control – microphone”, otherwise Optional.
C.4: Mandatory IF HFP 3/18b “Remote audio volume control – microphone”, otherwise Optional.
C.5: Mandatory IF HFP 3/24 “Wide Band Speech service” OR HFP 3/28 “Super Wide Band Speech”,
otherwise Optional.
C.6–C.9: No longer used.
C.10: Excluded IF HFP 0b/3 “Hands-Free Profile 1.7”, otherwise Optional IF HFP 3/15 “Voice recognition
activation/deactivation”, otherwise Excluded.
C.11: Optional IF HFP 3/15a “Enhanced Voice Recognition Status”, otherwise Excluded.
C.12: Excluded IF HFP 0b/3 “Hands-Free Profile 1.7” OR HFP 0b/4 “Hands-Free Profile 1.8”, otherwise
Mandatory.
C.13: Excluded IF HFP 0b/3 “Hands-Free Profile 1.7” OR HFP 0b/4 “Hands-Free Profile 1.8”, otherwise
Optional.
C.14: Excluded IF HFP 0b/3 “Hands-Free Profile 1.7” OR HFP 0b/4 “Hands-Free Profile 1.8” OR HFP
0b/5 “Hands-Free Profile 1.9”, otherwise Optional.
C.15: Mandatory IF HFP 3/30 “Call Duration Information” AND HFP 3/12c “Three way calling (AT+CHLD
value 3)”, otherwise Excluded.

### 2.6 Audio coding requirements

Table 4: Requirements towards the Link Control Procedures of the Serial Port Profile (AG and HF)

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CVSD audio coding over SCO |  |  | [1] 2.3 |  |  | M |  |  |
| 2 |  |  | mSBC audio coding over eSCO |  |  | [1] 5.7.4 [5] 6.7.4 |  |  | C.1 |  |  |
| 3 |  |  | CVSD audio coding over eSCO (Initiating) |  |  | [1] 5.7.3 [5] 6.7.3 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | CVSD audio coding over eSCO (Accepting) |  |  | [1] 5.7.3 [5] 6.7.3 |  |  | M |  |  |
| 5 |  |  | LC3-SWB audio coding over eSCO |  |  | [5] 6.7.6 |  |  | C.2 |  |  |

C.1: Mandatory IF HFP 2/24 “Wide Band Speech service” OR HFP 3/24 “Wide Band Speech service”,
otherwise Excluded.
C.2: Mandatory IF HFP 2/29 “Super Wide Band Speech” OR HFP 3/28 “Super Wide Band Speech”,
otherwise Excluded.

### 2.7 Requirements towards other layers


#### 2.7.1 RFCOMM requirements

Table 5: No longer used
Table 5a: RFCOMM Requirements (AG and HF)

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initialize RFCOMM Session | [2] 5 [5] 6.1 | M | [8] RFCOMM 1/1 |  |  |
| 2 | Respond to Initialization of an RFCOMM Session | [2] 5 [5] 6.1 | M | [8] RFCOMM 1/2 |  |  |


#### 2.7.2 GAP requirements

Table 6: GAP Requirements (AG)
Prerequisite: HFP 1/1 “Audio Gateway (AG)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Bondable mode | [1] 6.1 [5] 7.1 | M | [3] GAP 1/7 |  |  |
| 2 | Initiation of general inquiry | [1] 6.3 [5] 7.3 | M | [3] GAP 3/1 |  |  |
| 3 | Initiation of general bonding | [1] 6.3 [5] 7.3 | O | [3] GAP 3/5 |  |  |
| 4 | Security mode 4, level 4 | [1] 6.2 [5] 7.2 | O | [3] GAP 2/7a |  |  |

Prerequisite: HFP 1/2 “Hands-Free (HF)”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [1] 6.1 [5] 7.1 | M | [3] GAP 1/3 |  |  |
| 2 | Security mode 4, level 4 | [1] 6.2 [5] 7.2 | O | [3] GAP 2/7a |  |  |


#### 2.7.3 BB and L2CAP requirements

Table 7b: BB and L2CAP Requirements

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | 2-EV3 packet type | [1] 3 | M | [7] BB 6a/1 |  |  |
| 2 | No longer used | N/A | N/A | N/A |  |  |
| 3 | Data Channel Initiator | [2] 5.2 [5] 6.2 | M | [9] L2CAP 1/1 |  |  |
| 4 | Data Channel Acceptor | [2] 5.2 [5] 6.2 | M | [9] L2CAP 1/2 |  |  |


#### 2.7.4 LC3 requirements

Table 7c: LC3 Requirements
Prerequisite: HFP 2/29 “Super Wide Band Speech” OR HFP 3/28 “Super Wide Band Speech”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | No longer used | N/A | N/A | N/A |  |  |
| 2 | Superwideband (32 kHz) (Encoder) | [5] 6.7.6 | M | [6] LC3 3/4 |  |  |
| 3 | 7.5 ms (Encoder) | [5] 6.7.6 | M | [6] LC3 4/1 |  |  |
| 4 | Superwideband (32 kHz) (Decoder) | [5] 6.7.6 | M | [6] LC3 5/4 |  |  |
| 5 | 7.5 ms (Decoder) | [5] 6.7.6 | M | [6] LC3 6/1 |  |  |


### 2.8 Supplementary Interoperability Verification

It is recommended but not required to support any of the capabilities defined below. The Bluetooth license grant obtained through Qualification is not predicated on passing any test that is linked to support of these capabilities.
Table 8: Additional Hands-Free Capabilities

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Multiple audio transfers during call – AG and HF initiated |  |  | [1] |  |  | C.1 |  |  |
| 2 |  |  | Audio transfer by SLC release during an active call |  |  | [1] |  |  | C.1 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Audio transfer by powering ON HF |  |  | [1] |  |  | O |  |  |
| 4 |  |  | SLC during SDP response |  |  | [1] |  |  | O |  |  |
| 5 |  |  | Handle dynamic server channel number for HFP service |  |  | [1] |  |  | O |  |  |
| 6 |  |  | HF disallows connections in non-discoverable mode |  |  | [1] |  |  | C.2 |  |  |
| 7 |  |  | HF connects to AG during incoming call |  |  | [1] |  |  | O |  |  |
| 8 |  |  | Link loss during incoming call |  |  | [1] |  |  | C.3 |  |  |
| 9 |  |  | SLC release during incoming call |  |  | [1] |  |  | C.3 |  |  |
| 10 |  |  | Voice recognition activation |  |  | [1] |  |  | C.4 |  |  |
| 11 |  |  | Place outgoing call by dialing number on the AG |  |  | [1] |  |  | O |  |  |
| 12 |  |  | Active call termination – NO CARRIER signal |  |  | [1] |  |  | C.5 |  |  |

C.1: Optional IF HFP 2/7a “HF-initiated Audio transfer to AG during ongoing call” OR HFP 3/7a “HF-
initiated Audio transfer to AG during ongoing call”, otherwise Excluded.
C.2: Optional IF HFP 1/2 “Hands-Free (HF)”, otherwise Excluded.
C.3: Optional IF HFP 1/1 “Audio Gateway (AG)”, otherwise Excluded.
C.4: Optional IF HFP 2/15 “Voice recognition activation” OR HFP 3/15 “Voice recognition
activation/deactivation”, otherwise Excluded.
C.5: Optional IF HFP 2/6 “Terminate a call”, otherwise Excluded.

## 3 References

[1] Hands-Free Profile, Version 1.5 or later
[2] Hands-Free Profile, Version 1.7 or later
[3] ICS Proforma for Generic Access Profile (GAP)
[4] Hands-Free Profile, Version 1.8 or later
[5] Hands-Free Profile, Version 1.9 or later
[6] ICS Proforma for Low Complexity Communication Code (LC3)
[7] ICS Proforma for Baseband (BB)
[8] ICS Proforma for RFCOMM
[9] ICS Proforma for Logical Link Control and Adaptation Protocol (L2CAP)
[10] Hands-Free Profile, Version 1.10

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | 1.5.1 |  |  | 2005-10-31 | Change name from HFP1.5.ICS.1.0.x to HFP.ICS.1.5.x. Prepare for publication. |
|  |  |  | 1.5.2r0 |  |  | 2006-04-04 | TSE 853: Added new entry to Table 2 for Enhanced call status with Limited Network Notification. Technical correction to Table 2 |
| 1 |  |  | 1.5.2 |  |  | 2006-06-19 | Prepare for publication. |
|  |  |  | 1.5.3r0 |  |  | 2006-10-01 | Fix numbering in Table to accommodate TPG TSE 1813: Refine 2/18 and 3/18 |
|  |  |  | 1.5.3r1 |  |  | 2006-11-06 | Fix Table 2 footnote O4 to match 21a, 21b, 21c numbering change TSE 1982: Add line !5a in Table HFP 2, Change line 15b, add C.1 footnote |
|  |  |  | 1.5.3r2 |  |  | 2006-12-08 | Change O.x conditional statements to C.x. Fix for TSE 1813 |
| 2 |  |  | 1.5.3 |  |  | 2007-01-10 | Prepare for publication. |
| 3 |  |  | 1.5.4 |  |  | 2007-08-31 | TSE 2055 Table 3/15: change activation to activation/deactivation TSE 2100: Add rows to Tables 2 and 3 TSE 2112: Change 2/21B to C.3 TSE 2219: Table 7: Fix GAP reference TSE 2221: Add eSCO entries to Tables 2 and 3 TSE 2238; Add two rows to Table 3 TSE 1998: Change to Table 2: Add 1a TSE 2027: Changes to Table 2 |
|  |  |  | 1.5.5r0-1 |  |  | 2008-04 | Change to Tables 2 and 3 /7a to reflect TSE 2100 text TSE 2449: Item 12/e TSE 2434: Add 2/22 and 3/22 as O Correction for item 3/12e: Change O.x to C.x |
| 4 |  |  | 1.5.5 |  |  | 2008-04-15 | Prepare for publication |
|  |  |  | 1.5.6r0 |  |  | 2008-09 | TSE: 2487: Add row Table 2/7b TSE 2605: Add Prereq. to Table 2 and Table 3 |
| 5 |  |  | 1.5.6 |  |  | 2008-11-20 | Prepare for publication. |
| 6 |  |  | 1.5.7 |  |  | 2009-08-05 | TSE 2882: Table item 2/7: Change Reference |
| 7 |  |  | 1.5.8r0 |  |  | 2010-08-17 | TSE 2884: Remove 2/7b |
|  |  |  | 1.6.0r0 |  |  | 2011-04-01 | Merge HFP 1.5 and HFP 1.6 ICS |
| 8 |  |  | 1.6.0r1-5 |  |  | 2011-05-04 | Edits and reviews by technical reviewers and spec director. Added Prerequisites to Tables 6 and 7. Accept changes. |
|  |  |  | 1.6.1r0 |  |  | 2013-02-20 | TSE 4684: New ICS table for Supplementary Interoperability Verification/Category-X test case mapping. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 9 |  |  | 1.6.1 |  |  | 2012-04-30 | Prepare for publication. |
|  |  |  | 1.6.2r0 |  |  | 2012-09-06 | TSE 4617: Correct references in Table 2 and Table 3 for eSCO support in Audio Connection to be 5.7.1, not 5.17. TSE 4905: Added 8/12, Active call termination – NO CARRIER signal |
|  |  |  | 1.6.2r1 |  |  | 2012-10-22 | TSE 4743: Added 2/25 “Support Roaming function” |
| 10 |  |  | 1.6.2 |  |  | 2012-11-02 | Prepare for Publication |
|  |  |  | 1.6.3r1 |  |  | 2013-10-03 | TCRL 2013-2 TSE 5166: Updated Table 3, Item 21a to "O". |
| 11 |  |  | 1.6.3 |  |  | 2013-12-03 | Adopted by BoD |
|  |  |  | DDR CR r00 |  |  | 2013-12-18 | Added HFP 1.7 and HF Indicators feature |
|  |  |  | DDR CR r01 |  |  | 2013-12-18 | Minor versioning and conditional updates |
|  |  |  | DDR CR r02 |  |  | 201-01-09 | Added IXIT Appendix for HF Indicators |
|  |  |  | DDR CR r03 |  |  | 2014-03-04 | Merged comments from Meagan |
|  |  |  | 1.7.0r01 |  |  | 2014-03-24 | Template Conversion (Template ICS 2014r01) _ _ Editorial review by Meagan |
|  |  |  | 1.7.0r02 |  |  | 2014-04-09 | Updated contributors list |
|  |  |  | 1.7.0r03 |  |  | 2014-07-16 | Incorporated “HFP – 4.1 Updates ICS CR r03” |
|  |  |  | 1.7.0r04 |  |  | 2014-08-04 | Addressed comments by Alicia and Jason |
|  |  |  | 1.7.0r05 |  |  | 2014-08-14 | TSE 5629: Added tracking for removed item 2/7b that was removed by TSE 2884 and noted as “Item no longer used” according to current convention. TSE 5572: Added a note to Table 2 Conditional item C.4 clarifying what network support was intended to indicate. This was lost in the integration of TSE 1723. |
|  |  |  | 1.7.0r06 |  |  | 2014-08-11 | Legal review edits and addressed Meagan’s comments |
|  |  |  | 1.7.0r07 |  |  | 2014-08-18 | Removed occurrences of “UUID” for HF Indicators |
|  |  |  | 1.7.0r08 |  |  | 2014-09-08 | Fixed Table 7b and changed incorrect eSCO conditional |
| 12 |  |  | 1.7.0 |  |  | 2014-09-18 | Adopted by SIG BoD |
|  |  |  | 1.7.1r00 |  |  | 2015-04-28 | TSE 6172: Removed items in Table 0 and added new tables 0a and 0b for AG and HF. TSE 6312: Added items 3 and 4 to IXIT to support updates to TP/HFI/BI-03-I in HFP.TS |
|  |  |  | 1.7.1r01 |  |  | 2015-06-05 | Deleted Section 1.2 (Global Statement of Conformance) per current ICS template standards. Fixed broken references in Table 4. |
| 13 |  |  | 1.7.1 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 1.7.1.0r00 |  |  | 2015-10-28 | Updated version numbering to align with Specification version change from 1.7 to 1.7.1 for ESR09. With the specification taking a third identifying number, the ICS version identifier moves to the fourth number and starts again at 0. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.7.1.0r01 |  |  | 2015-11-02 | Added items 0a/4 and 0b/4 for new Specification version 1.7.1 (ESR09). |
|  |  |  | 1.7.1.0r03 |  |  | 2015-11-24 | Added Tables 0c and 0d for minor profile versions. |
| 14 |  |  | 1.7.1.0 |  |  | 2015-12-22 | Prepared for TCRL 2015-2 publication |
|  |  |  | 1.7.1.1r00 |  |  | 2016-03-01 | TSE 6678: Updated conditional statements C.7 in Table 2 & C.5 in Table 3. |
| 15 |  |  | 1.7.1.1 |  |  | 2016-07-13 | Prepared for TCRL 2016-1 publication. |
|  |  |  | 1.7.1.2r00 |  |  | 2017-03-15 | TSE 7814: Updated Table 6/4 and 7/2 to include new GAP item (2/7a). |
|  |  |  | 1.7.1.2r01 |  |  | 2017-04-25 | Updated to the ICS description for items 6/4 and 7/2. Update ICS template. Replace parentheses with quotation marks per the current ICS conventions. Separate the IXIT information to a separate document. |
| 16 |  |  | 1.7.1.2 |  |  | 2017-07-03 | Approved by BTI. Prepared for TCRL 2017-1 publication. |
|  |  |  | 1.7.2.0r00 |  |  | 2018-11-09 | Updated version number to 1.7.2.0 to align with adoption of the specification 1.7.2. Added items 0c/2- 4 and 0d/2-4 for new versions 1.5.1, 1.6.1, and 1.7.2. |
| 17 |  |  | 1.7.2.0 |  |  | 2018-11-21 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | 1.8.0r00–r03 |  |  | 2019-06-05 – 2019-08-28 | Incorporated changes to accommodate integration of Enhanced Voice Recognition Activation change request for HFP 1.8. Items added: 2/15c Enhanced Voice Recognition Status 2/15d Voice Recognition Text 3/15a Enhanced Voice Recognition Status 3/15b Voice Recognition Text Updated template and made minor editorial fixes. Accepted Changes, added Contributor. Expanded revision history in response to BTI feedback. TSE 12506 (rating 1): Clarify the ICS conditionals of Table 2 to indicate at least one or one and only one (C.1, C.4). Revise Table 2 conditionals C.8, C.9, and C.11 to remove the “NOT” by starting the statement with “Excluded IF x supported”. TSE 12515 (rating 1): Correct the SPP ICS references in Table 5 and correct the layer name typo. |
| 18 |  |  | p18 |  |  | 2020-04-21 | Set publication number for previous v1.8.0 as p18. Removed “Support” column from tables per new document guidelines. Approved by BTI on 2019-10- 08. Adopted by the BoD on 2020-04-14. Prepared for publication. |
|  |  |  | p18ed2r00 |  |  | 2021-01-14 | TSE 15982 (rating 1): Changes for deprecation. |
|  |  |  | p18 edition 2 |  |  | 2021-02-01 | Approved by BTI on 2021-01-15. Prepared for edition 2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p18ed3 r00–r01 |  |  | 2021-08-02 – 2021-09-24 | TSE 17318 (rating 1): Consistency checker findings. Template-related editorials. Consistency checker editorials to align wording with the latest ICS template. |
|  |  |  | p18 edition 3 |  |  | 2021-09-28 | Approved by BTI on 2021-09-27. Prepared for edition 3 publication. |
|  |  |  | p18ed4 r00–r04 |  |  | 2022-02-17 – 2022-04-29 | TSE 18104 (rating 1): Updated deprecation and withdrawal dates for HFP 1.5, 1.5.1, 1.6, and 1.6.1 in Tables 0a – 0d and updated item statuses and conditionals to account for those deprecations as follows: updated 2/3b, 2/23, and 2/27 to M, updated 2/24 and 2/26 to O, deleted C.8–C.12, and removed v1.5 and v1.6 from C.14; updated 3/3b and 3/26 to M and 3/23, 3/24, and 3/25 to O, deleted C.6–C.9, and removed v1.5 and v1.6 from C.10; updated 4/3 and 4/4 to M and deleted C.2; and updated 7b/1 to M and deleted C.1. TSE 18373 (rating 1): Corrected “is/are/not supported” language in conditionals globally to align with the latest ICS conventions. Editorials, including template-related formatting fixes and alignment of copyright page with v2 of the DNMD. |
| 19 |  |  | p19 |  |  | 2022-06-28 | Approved by BTI on 2022-05-31. Prepared for TCRL 2022-1 publication. |
|  |  |  | p19ed2r00– r03 |  |  | 2023-02-07 – 2023-02-23 | TSE 22626 (rating 1): Updated to align with current ICS conventions, and updated the Withdrawal date for HFP 1.7 and HFP 1.7.1 from 2023-02-01 to 2024-02-01. Deleted all draft revision history comments prior to p0. |
|  |  |  | p19 edition 2 |  |  | 2023-02-27 | Approved by BTI on 2023-02-23. Prepared for edition 2 publication. |
|  |  |  | p20r00–r03 |  |  | 2023-07-25 – 2023-08-21 | TSE 18207 (rating 4): To align with E18424 and E20445, added new “Reserved Fields and RFU Bits” items 2/28 and 3/27 and related conditionals C.15 and C.12, respectively. Added new reference to HFP v1.9 and added “or later” to the v1.8 reference text. TSE 19028 (rating 1): To align with E18696, added references to HFP v1.9 to 2/3b, 2/24, 2/27, 3/3b, 3/24, 3/26, 4/2, 4/3, 4/4, 5/1, 5/2, 6/1, 6/2, 6/3, 6/4, 7/1, and 7/2 and added references to HFP v1.8 to 2/23, 2/26, 3/23, and 3/25. TSE 19177 (rating 1): Per E18697, globally updated terminology capitalization and grammar per new conventions approved by the working group (made consistent with the latest spec draft where conflicting). TSE 19239 (rating 1): Per E17611, which calls for the removal of references to SPP, set Table 5 to “No longer used” and added new Table 5a, renaming auto-numbered Section 1.6.1 from SPP to RFCOMM. Added 7b/3 and 7b/4. Updated references to include HFP v1.9 and the ICSs for RFCOMM and L2CAP. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | Incorporated changes to accommodate integration of Super Wide Band Speech change request for HFP v1.9 (HFP.ICS TS.p24r00 TSE18207 _ _ _ CRr05 th.docx). Items added: HFP 0a/5, HFP 0b5, _ HFP 2/29 and C.16, HFP 3/28 and C.13, HFP 4/5 and C.2, and HFP 7b2 and C.1. Added entire new Table 7c. |
| 20 |  |  | p20 |  |  | 2023-09-19 | Approved by BTI on 2023-08-30. HFP v1.9 adopted by the BoD on 2023-09-12. Prepared for publication. |
|  |  |  | p21r00–r01 |  |  | 2023-10-04 – 2024-04-23 | TSE 24073 (rating 2): Removed SUM ICS from the References section. Updated 7b/1 to BB ILDs. TSE 24998 (rating 1): Marked Item 1 of Table 7c as “No longer used.” |
| 21 |  |  | p21 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p22r00–r02 |  |  | 2024-10-10 – 2024-11-19 | TSE 25895 (rating 2): Per E25913, updated Table 7b to cut conditional C.1. Updated table spacing to guidelines throughout. TSE 26428 (rating 2): Updated items 2/15c, 2/16, 2/17, 2/18a, 2/18b, 2/18c, 2/19, 2/20, 2/21a, 2/21b, 2/21c, 2/23, 2/26, 3/15a, 3/16, 3/17, 3/18a, 3/18b, 3/18c, 3/18d, 3/18e, 3/18f, 3/19, 3/20, 3/21a, 3/21b, 3/23, and 3/25. |
| 22 |  |  | p22 |  |  | 2025-02-18 | Approved by BTI on 2024-12-25. Prepared for TCRL 2025-1 publication. |
|  |  |  | p23r00 |  |  | 2025-02-26 | TSE 27004 (rating 2): Updated conditional C.2 for Tables 0a and 0b. Added “Core Configuration” section and Table 0e. |
| 23 |  |  | p23 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p24r00 |  |  | 2025-07-23 | TSE 27855 (rating 2): Per E25913, removed item 7b/2. |
| 24 |  |  | p24 |  |  | 2025-11-04 | Approved by BTI on 2025-09-24. Prepared for TCRL pkg101 publication. |
|  |  |  | p25r00–r03 |  |  | 2025-09-04 – 2025-10-22 | Work for p25 began after p24 content was finalized; publication of p24 occurred later due to internal processes. Incorporated HFP CF.ICS.CRr08. To account for the _ Call Forwarding feature enhancement in Hands-Free Profile v1.10, incorporated approved Test Issues 25373 and 25704. Added HFP 0a/6, HFP 0b/6, HFP 2/30, HFP 3/29, and conditions 2/C.17 and 3/C.14. Incorporated HFP CDI.ICS.CRr04. To account for the _ Call Duration Information feature enhancement in Hands-Free Profile v1.10, incorporated approved Test Issues 20438, 25379, and 27508. Per E20436, added HFP 2/32. Also added HFP 2/31, HFP 3/30, HFP 3/31, and conditions 2/C.18 and 3/C.15. Updated the references list and the acknowledgments. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 25 |  |  | p25 |  |  | 2025-12-16 | Approved by BTI on 2025-11-20. HFP v1.10 adopted by the BoD on 2025-12-15. Prepared for TCRL pkg101-addition publication. |
|  |  |  | p26r00 |  |  | 2026-01-08 | TSE 28611 (rating 1): Updated the status and conditions for Tables 0c and 0d to include D&W dates for HFP v1.7.2. |
| 26 |  |  | p26 |  |  | 2026-02-17 | Approved by BTI on 2026-01-22. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Nick Jahn |  |  | Audi AG |  |
|  | Rüdiger Mosig |  |  | Berner&Mattner |  |
|  | Dejan Berec |  |  | Bluetooth SIG, Inc. |  |
|  | Tharon Hall |  |  | Bluetooth SIG, Inc. |  |
|  | Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |
|  | Jason Nydegger |  |  | Bluetooth SIG, Inc. |  |
|  | Meagan Schuver |  |  | Bluetooth SIG, Inc. |  |
|  | Michael Buntscheck |  |  | BMS |  |
|  | Alicia Courtney |  |  | Broadcom Ltd. |  |
|  | Jaebeom Kim |  |  | CETECOM MOVON Ltd. |  |
|  | Burch Seymour |  |  | Continental Automotive Systems |  |
|  | Jiny Bradshaw |  |  | CSR |  |
|  | Thomas Carmody |  |  | CSR |  |
|  | Neil Macmullen |  |  | CSR |  |
|  | Magnus Sommansson |  |  | CSR |  |
|  | Jeremy Stark |  |  | CSR |  |
|  | Basam Masri |  |  | Denso |  |
|  | Aaron Weinfield |  |  | Denso |  |
|  | Norman Geilhardt |  |  | Expleo |  |
|  | Sophia Feil |  |  | Expleo Germany GmbH |  |
|  | Atef Kort |  |  | Expleo Germany GmbH |  |
|  | Maximilian Krammer |  |  | Expleo Germany GmbH |  |
|  | Don Liechty |  |  | Extended Systems |  |
|  | Doron M. Elliot |  |  | Ford Motor Company |  |
|  | Denis Kenzior |  |  | Intel |  |
|  | Stephen Raxter |  |  | Johnson Controls / National Analysis Center |  |
|  | Vartika Agarwal |  |  | Motorola |  |
|  | Leonard Hinds |  |  | Motorola |  |
|  | Tony Mansour |  |  | Motorola |  |
|  | Stephane Bouet |  |  | Nissan |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Patrick Clauberg |  |  | Nokia |  |
|  | Jamie Mchardy |  |  | Nokia |  |
|  | Jurgen Schnitzler |  |  | Nokia |  |
|  | Josselin de la Broise |  |  | Parrot |  |
|  | Kyle Penri-Williams |  |  | Parrot |  |
|  | Guillaume Poujade |  |  | Parrot |  |
|  | Scott Walsh |  |  | Plantronics |  |
|  | Chris Church |  |  | Qualcomm Technologies International, Ltd. |  |
|  | Laurence Richardson |  |  | Qualcomm Technologies International, Ltd. |  |
|  | Dmitri Toropov |  |  | Siemens |  |
|  | Erwin Weinans |  |  | Sony Ericsson |  |
|  | Tim Reilly |  |  | Stonestreet One |  |
|  | Akira Miyajima |  |  | Toyota |  |
|  | Bill Bernard |  |  | Visteon |  |
|  | Ryan Bruner |  |  | Visteon |  |
|  | Florencio Ceballos |  |  | Visteon |  |
