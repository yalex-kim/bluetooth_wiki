# CORE.ICS.p1

> Source: PDF converted via PyMuPDF.

---

Core Configurations (CORE)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: CORE.ICS.p1 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third- party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Auto-fill tables

This ICS includes one or more tables that are defined as auto-fill tables. Auto-fill tables are defined to allow for less-complex conditions within other tables. Auto-fill tables are distinguished from regular ICS tables by the addition of “(auto-fill)” after the table number, prior to the colon “:”.
An auto-fill table is automatically populated based on selected capabilities elsewhere in the ICS. The populated settings in the auto-fill table are not user editable.

### 1.3 Versions

Table 1: Controller Core Specification X.Y Versions
Prerequisite: CORE 10/1 “BR/EDR Security (SEC)” OR CORE 10/2 “Link Manager Protocol (LMP)” OR CORE 10/3 “Baseband (BB)” OR CORE 10/4 “Radio Frequency (RF)” OR CORE 10/10 “Isochronous Adaptation Layer (IAL)” OR CORE 10/11 “LE Security (LESEC)” OR CORE 10/12 “Link Layer (LL)” OR CORE 10/13 “Radio Frequency Physical Layer (RFPHY)” OR CORE 10/14 “Channel Sounding (CS)” OR CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” OR CORE 12/2 “Lower HCI role”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Controller Core any version |  |  | N/A |  |  | M |  |  |
| 42 |  |  | Controller Core v4.2 |  |  | [1] |  |  | C.1, C.2 |  |  |
| 50 |  |  | Controller Core v5.0 |  |  | [2] |  |  | C.1 |  |  |
| 51 |  |  | Controller Core v5.1 |  |  | [3] |  |  | C.1 |  |  |
| 52 |  |  | Controller Core v5.2 |  |  | [4] |  |  | C.1 |  |  |
| 53 |  |  | Controller Core v5.3 |  |  | [5] |  |  | C.1 |  |  |
| 54 |  |  | Controller Core v5.4 |  |  | [6] |  |  | C.1 |  |  |
| 60 |  |  | Controller Core v6.0 |  |  | [28] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one. C.2: Excluded after Deprecation. Deprecated 2026-02-01. Withdrawn 2031-02-01.
Table 1a (auto-fill): Controller Core Specification X.Y Versions or Later
Prerequisite: CORE 1/1 “Controller Core any version”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 |  |  | Controller Core v5.0 or later |  |  | N/A |  |  | C.1 |  |  |
| 51 |  |  | Controller Core v5.1 or later |  |  | N/A |  |  | C.2 |  |  |
| 52 |  |  | Controller Core v5.2 or later |  |  | N/A |  |  | C.3 |  |  |
| 53 |  |  | Controller Core v5.3 or later |  |  | N/A |  |  | C.4 |  |  |
| 54 |  |  | Controller Core v5.4 or later |  |  | N/A |  |  | C.5 |  |  |
| 60 |  |  | Controller Core v6.0 or later |  |  | N/A |  |  | C.6 |  |  |

C.1: Excluded IF CORE 1/42 “Controller Core v4.2”, otherwise Mandatory. C.2: Excluded IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0”, otherwise Mandatory. C.3: Excluded IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1”, otherwise Mandatory. C.4: Excluded IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2”, otherwise Mandatory. C.5: Excluded IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2” OR CORE 1/53 “Controller Core v5.3”, otherwise Mandatory. C.6: Excluded IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2” OR CORE 1/53 “Controller Core v5.3” OR CORE 1/54 “Controller Core v5.4”, otherwise Mandatory.
Prerequisite: CORE 1/1 “Controller Core any version”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 |  |  | Controller Core v5.0 or earlier |  |  | N/A |  |  | C.1 |  |  |
| 51 |  |  | Controller Core v5.1 or earlier |  |  | N/A |  |  | C.2 |  |  |
| 52 |  |  | Controller Core v5.2 or earlier |  |  | N/A |  |  | C.3 |  |  |
| 53 |  |  | Controller Core v5.3 or earlier |  |  | N/A |  |  | C.4 |  |  |
| 54 |  |  | Controller Core v5.4 or earlier |  |  | N/A |  |  | C.5 |  |  |
| 60 |  |  | Controller Core v6.0 or earlier |  |  | N/A |  |  | C.6 |  |  |

C.1: Mandatory IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0”, otherwise Excluded. C.2: Mandatory IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1”, otherwise Excluded. C.3: Mandatory IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2”, otherwise Excluded. C.4: Mandatory IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2” OR CORE 1/53 “Controller Core v5.3”, otherwise Excluded. C.5: Mandatory IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2” OR CORE 1/53 “Controller Core v5.3” OR CORE 1/54 “Controller Core v5.4”, otherwise Excluded. C.6: Mandatory IF CORE 1/42 “Controller Core v4.2” OR CORE 1/50 “Controller Core v5.0” OR CORE 1/51 “Controller Core v5.1” OR CORE 1/52 “Controller Core v5.2” OR CORE 1/53 “Controller Core v5.3” OR CORE 1/54 “Controller Core v5.4” OR CORE 1/60 “Controller Core v6.0”, otherwise Excluded.
Table 1c: Controller Core Addenda and Errata

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Core Specification Addendum 5 |  |  | [7] |  |  | C.1, C.2 |  |  |

C.1: Optional IF CORE 1/42 “Controller Core v4.2”, otherwise Excluded. C.2: Excluded after Deprecation. Deprecated 2026-02-01. Withdrawn 2031-02-01.
Table 2: Host Core Specification X.Y Versions
Prerequisite: CORE 11/1 “Generic Attribute Profile (GATT)” OR CORE 11/2 “Attribute Protocol (ATT)” OR CORE 11/3 “Generic Access Profile (GAP)” OR CORE 11/4 “Service Discovery Protocol (SDP)” OR CORE 11/5 “Logical Link Control and Adaptation Protocol (L2CAP)” OR CORE 11/6 “Security Manager (SM)” OR CORE 11/20 “AMP Manager Protocol (A2MP)” OR CORE 12/3 “Upper HCI role”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Host Core any version |  |  | N/A |  |  | M |  |  |
| 42 |  |  | Host Core v4.2 |  |  | [1] |  |  | C.1, C.2 |  |  |
| 50 |  |  | Host Core v5.0 |  |  | [2] |  |  | C.1 |  |  |
| 51 |  |  | Host Core v5.1 |  |  | [3] |  |  | C.1 |  |  |
| 52 |  |  | Host Core v5.2 |  |  | [4] |  |  | C.1 |  |  |


|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 53 |  |  | Host Core v5.3 |  |  | [5] |  |  | C.1 |  |  |
| 54 |  |  | Host Core v5.4 |  |  | [6] |  |  | C.1 |  |  |
| 60 |  |  | Host Core v6.0 |  |  | [28] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one. C.2: Excluded after Deprecation. Deprecated 2026-02-01. Withdrawn 2031-02-01.
Table 2a (auto-fill): Host Core Specification X.Y Versions or Later
Prerequisite: CORE 2/1 “Host Core any version”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 |  |  | Host Core v5.0 or later |  |  | N/A |  |  | C.1 |  |  |
| 51 |  |  | Host Core v5.1 or later |  |  | N/A |  |  | C.2 |  |  |
| 52 |  |  | Host Core v5.2 or later |  |  | N/A |  |  | C.3 |  |  |
| 53 |  |  | Host Core v5.3 or later |  |  | N/A |  |  | C.4 |  |  |
| 54 |  |  | Host Core v5.4 or later |  |  | N/A |  |  | C.5 |  |  |
| 60 |  |  | Host Core v6.0 or later |  |  | N/A |  |  | C.6 |  |  |

C.1: Excluded IF CORE 2/42 “Host Core v4.2”, otherwise Mandatory. C.2: Excluded IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0”, otherwise Mandatory. C.3: Excluded IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1”, otherwise Mandatory. C.4: Excluded IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2”, otherwise Mandatory. C.5: Excluded IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2” OR CORE 2/53 “Host Core v5.3”, otherwise Mandatory. C.6: Excluded IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2” OR CORE 2/53 “Host Core v5.3” OR CORE 2/54 “Host Core v5.4”, otherwise Mandatory.
Table 2b (auto-fill): Host Core Specification X.Y Versions or Earlier
Prerequisite: CORE 2/1 “Host Core any version”

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 |  |  | Host Core v5.0 or earlier |  |  | N/A |  |  | C.1 |  |  |
| 51 |  |  | Host Core v5.1 or earlier |  |  | N/A |  |  | C.2 |  |  |
| 52 |  |  | Host Core v5.2 or earlier |  |  | N/A |  |  | C.3 |  |  |
| 53 |  |  | Host Core v5.3 or earlier |  |  | N/A |  |  | C.4 |  |  |
| 54 |  |  | Host Core v5.4 or earlier |  |  | N/A |  |  | C.5 |  |  |
| 60 |  |  | Host Core v6.0 or earlier |  |  | N/A |  |  | C.6 |  |  |

C.1: Mandatory IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0”, otherwise Excluded. C.2: Mandatory IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1”, otherwise Excluded.
C.3: Mandatory IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2”, otherwise Excluded. C.4: Mandatory IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2” OR CORE 2/53 “Host Core v5.3”, otherwise Excluded. C.5: Mandatory IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2” OR CORE 2/53 “Host Core v5.3” OR CORE 2/54 “Host Core v5.4”, otherwise Excluded. C.6: Mandatory IF CORE 2/42 “Host Core v4.2” OR CORE 2/50 “Host Core v5.0” OR CORE 2/51 “Host Core v5.1” OR CORE 2/52 “Host Core v5.2” OR CORE 2/53 “Host Core v5.3” OR CORE 2/54 “Host Core v5.4” OR CORE 2/60 “Host Core v6.0”, otherwise Excluded.

### 1.4 Core layer

Table 10: Controller Layer Requirements

| Item | Feature | Reference | Status |  | Inter-Layer |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |  |
| 1 | BR/EDR Security (SEC) | [1] [2] [3] [4] [5] [6] [28] Volume 2, Part H | O | [12] SEC |  |  |  |
| 2 | Link Manager Protocol (LMP) | [1] [2] [3] [4] [5] [6] [28] Volume 2, Part C | O | [11] LMP |  |  |  |
| 3 | Baseband (BB) | [1] [2] [3] [4] [5] [6] [28] Volume 2, Part B | O | [10] BB |  |  |  |
| 4 | Radio Frequency (RF) | [1] [2] [3] [4] [5] [6] [28] Volume 2, Part A | O | [9] RF |  |  |  |
| 10 | Isochronous Adaptation Layer (IAL) | [4] [5] [6] [28] Volume 6, Part G | C.2 | [16] IAL |  |  |  |
| 11 | LE Security (LESEC) | [1] [2] [3] [4] [5] [6] [28] Volume 6, Part E | C.1 | [15] LESEC |  |  |  |
| 12 | Link Layer (LL) | [1] [2] [3] [4] [5] [6] [28] Volume 6, Part B | O | [14] LL |  |  |  |
| 13 | Radio Frequency Physical Layer (RFPHY) | [1] [2] [3] [4] [5] [6] [28] Volume 6, Part A | O | [13] RFPHY |  |  |  |
| 14 | Channel Sounding (CS) | [28] Volume 6, Part H | C.4 | [29] CS |  |  |  |
| 20 | PAL for 802.11 MAC/PHY (802.11 PAL) | [1] [2] [3] [4] Volume 5, Part A | C.3 | [17] [18] |  | 80211PAL AND |  |
|  |  |  |  |  |  | 80211MP |  |

C.1: Mandatory IF CORE 20a/2 “LE encryption”, otherwise Excluded. C.2: Optional IF CORE 1a/52 “Controller Core v5.2 or later”, otherwise Excluded. C.3: Optional IF CORE 1b/52 “Controller Core v5.2 or earlier”, otherwise Excluded. C.4: Optional IF CORE 1a/60 “Controller Core v6.0 or later”, otherwise Excluded.
Table 11: Host Layer Requirements

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Generic Attribute Profile (GATT) | [1] [2] [3] [4] [5] [6] [28] Volume 3, Part G | O | [23] GATT |  |  |
| 2 | Attribute Protocol (ATT) | [1] [2] [3] [4] [5] [6] [28] Volume 3, Part F | O | [22] ATT |  |  |


| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 3 | Generic Access Profile (GAP) | [1] [2] [3] [4] [5] [6] [28] Volume 3, Part C | O | [21] GAP |  |  |
| 4 | Service Discovery Protocol (SDP) | [1] [2] [3] [4] [5] [6] [28] Volume 3, Part B | O | [20] SDP |  |  |
| 5 | Logical Link Control and Adaptation Protocol (L2CAP) | [1] [2] [3] [4] [5] [6] [28] Volume 3, Part A | O | [19] L2CAP |  |  |
| 6 | Security Manager (SM) | [1] [2] [3] [4] [5] [6] [28] Volume 3, Part H | O | [24] SM |  |  |
| 20 | AMP Manager Protocol (A2MP) | [1] [2] [3] [4] Volume 3, Part E | C.1 | [25] A2MP |  |  |

C.1: Optional IF CORE 2b/52 “Host Core v5.2 or earlier”, otherwise Excluded.
Table 12: HCI Layer Requirements

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Host Controller Interface (HCI) | [1] [2] [3] Volume 2, Part E [4] [5] [6] [28]Volume 4, Part E | O | N/A |  |  |
| 2 | Lower HCI role | [1] [2] [3] Volume 2, Part E [4] [5] [6] [28]Volume 4, Part E | C.1, C.2 | [26] HCI |  |  |
| 3 | Upper HCI role | [1] [2] [3] Volume 2, Part E [4] [5] [6] [28]Volume 4, Part E | C.1, C.2 | [27] UHCI |  |  |

C.1: Mandatory to support at least one IF CORE 12/1 “Host Controller Interface (HCI)”, otherwise Excluded. C.2: Mandatory to support none or all IF CORE 40/3 “Core-Complete”, otherwise Optional.
Table 13: Other Core Layer Requirements

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HCI-UART |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 4, Part A |  |  | O |  |  |
| 2 |  |  | HCI-USB |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 4, Part B |  |  | O |  |  |
| 3 |  |  | HCI-SD |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 4, Part C |  |  | O |  |  |
| 4 |  |  | HCI-3W |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 4, Part D |  |  | O |  |  |
| 5 |  |  | DTM |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 6, Part F |  |  | O |  |  |
| 6 |  |  | MWS |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 7, Part A |  |  | O |  |  |
| 7 |  |  | WCI-1 |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 7, Part B |  |  | O |  |  |
| 8 |  |  | WCI-2 |  |  | [1] [2] [3] [4] [5] [6] [28] Volume 7, Part C |  |  | O |  |  |


### 1.5 Layer groupings

Table 20 (auto-fill): Core Layer Groupings (Excluding HCI)

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR Controller Layers |  |  | [8] 2.1.1 |  |  | C.1 |  |  |
| 2 |  |  | BR/EDR Host Layers |  |  | [8] 2.2.1 |  |  | C.2 |  |  |
| 3 |  |  | LE Controller Layers |  |  | [8] 2.1.2 |  |  | C.3 |  |  |
| 4 |  |  | LE Host Layers |  |  | [8] 2.2.2 |  |  | C.4 |  |  |

C.1: Mandatory IF CORE 10/1 “BR/EDR Security (SEC)” AND CORE 10/2 “Link Manager Protocol (LMP)” AND CORE 10/3 “Baseband (BB)” AND CORE 10/4 “Radio Frequency (RF)”, otherwise Excluded. C.2: Mandatory IF CORE 11/3 “Generic Access Profile (GAP)” AND CORE 11/4 “Service Discovery Protocol (SDP)” AND CORE 11/5 “Logical Link Control and Adaptation Protocol (L2CAP)” AND ((CORE 11/1 “Generic Attribute Profile (GATT)” AND CORE 11/2 “Attribute Protocol (ATT)”) OR (NOT CORE 11/1 “Generic Attribute Profile (GATT)” AND NOT CORE 11/2 “Attribute Protocol (ATT)”)), otherwise Excluded. C.3: Mandatory IF CORE 10/12 “Link Layer (LL)” AND CORE 10/13 “Radio Frequency Physical Layer (RFPHY)” AND ((CORE 10/11 “LE Security (LESEC)” AND CORE 20a/2 “LE encryption”) OR (NOT CORE 10/11 “LE Security (LESEC)” AND NOT CORE 20a/2 “LE encryption”)) AND ((CORE 10/10 “Isochronous Adaptation Layer (IAL)” AND CORE 20a/3 “Isochronous channels”) OR (NOT CORE 10/10 “Isochronous Adaptation Layer (IAL)” AND NOT CORE 20a/3 “Isochronous channels”)) AND ((CORE 10/14 “Channel Sounding (CS)” AND CORE 20a/4 “Channel Sounding”) OR (NOT CORE 10/14 “Channel Sounding (CS)” AND NOT CORE 20a/4 “Channel Sounding”)), otherwise Excluded. C.4: Mandatory IF CORE 11/3 “Generic Access Profile (GAP)” AND ((CORE 11/1 “Generic Attribute Profile (GATT)” AND CORE 11/2 “Attribute Protocol (ATT)” AND CORE 11/5 “Logical Link Control and Adaptation Protocol (L2CAP)” AND CORE 11/6 “Security Manager (SM)” AND CORE 20a/1 “LE connections”) OR (NOT CORE 11/1 “Generic Attribute Profile (GATT)” AND NOT CORE 11/2 “Attribute Protocol (ATT)” AND NOT CORE 11/5 “Logical Link Control and Adaptation Protocol (L2CAP)” AND NOT CORE 11/6 “Security Manager (SM)” AND NOT CORE 20a/1 “LE connections”)), otherwise Excluded.
Table 20a (auto-fill): Core Layer References

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE connections |  |  | [8] 2.2.2 |  |  | C.1 |  |  |
| 2 |  |  | LE encryption |  |  | [8] 2.1.2 |  |  | C.2 |  |  |
| 3 |  |  | Isochronous channels |  |  | [8] 2.1.2 |  |  | C.3 |  |  |
| 4 |  |  | Channel Sounding |  |  | [8] 2.1.2 |  |  | C.4 |  |  |

C.1: Mandatory IF GAP 5/4 “Central (LE)” OR GAP 38/4 “Central (BR/EDR/LE)” OR GAP 5/3 “Peripheral (LE)” OR GAP 38/3 “Peripheral (BR/EDR/LE)”, otherwise Excluded. C.2: Mandatory IF LL 9/1 “LE Encryption”, otherwise Excluded. C.3: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/33 “Isochronous Broadcaster” OR LL 9/34 “Synchronized Receiver”, otherwise Excluded. C.4: Mandatory IF LL 9/56 “Channel Sounding”, otherwise Excluded.

### 1.6 Core configurations

Table 30 (auto-fill): Core-Controller Configurations
Prerequisite: CORE 12/2 “Lower HCI role” AND NOT (CORE 11/1 “Generic Attribute Profile (GATT)” OR CORE 11/2 “Attribute Protocol (ATT)” OR CORE 11/3 “Generic Access Profile (GAP)” OR CORE 11/4 “Service Discovery Protocol (SDP)” OR CORE 11/5 “Logical Link Control and Adaptation Protocol (L2CAP)” OR CORE 11/6 “Security Manager (SM)” OR CORE 11/20 “AMP Manager Protocol (A2MP)” OR CORE 12/3 “Upper HCI role”)

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR Core-Controller Configuration |  |  | [8] 2.1.1 |  |  | C.1 |  |  |
| 2 |  |  | LE Core-Controller Configuration |  |  | [8] 2.1.2 |  |  | C.2 |  |  |
| 3 |  |  | BR/EDR/LE Core-Controller Configuration |  |  | [8] 2.1.3 |  |  | C.3 |  |  |
| 4 |  |  | HS Core-Controller Configuration |  |  | [8] 2.1.4 |  |  | C.4 |  |  |
| 5 |  |  | HS/LE Core-Controller Configuration |  |  | [8] 2.1.5 |  |  | C.5 |  |  |

C.1: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND NOT CORE 20/3 “LE Controller Layers” AND NOT CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)”, otherwise Excluded. C.2: Mandatory IF CORE 20/3 “LE Controller Layers” AND NOT CORE 20/1 “BR/EDR Controller Layers”, otherwise Excluded. C.3: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/3 “LE Controller Layers” AND NOT CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)”, otherwise Excluded. C.4: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” AND NOT CORE 20/3 “LE Controller Layers”, otherwise Excluded. C.5: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/3 “LE Controller Layers” AND CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)”, otherwise Excluded.
Table 31 (auto-fill): Core-Host Configurations
Prerequisite: CORE 12/3 “Upper HCI role” AND NOT (CORE 10/1 “BR/EDR Security (SEC)” OR CORE 10/2 “Link Manager Protocol (LMP)” OR CORE 10/3 “Baseband (BB)” OR CORE 10/4 “Radio Frequency (RF)” OR CORE 10/10 “Isochronous Adaptation Layer (IAL)” OR CORE 10/11 “LE Security (LESEC)” OR CORE 10/12 “Link Layer (LL)” OR CORE 10/13 “Radio Frequency Physical Layer (RFPHY)” OR CORE 10/14 “Channel Sounding (CS)” OR CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” OR CORE 12/2 “Lower HCI role”)

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR Core-Host Configuration |  |  | [8] 2.2.1 |  |  | C.1 |  |  |
| 2 |  |  | LE Core-Host Configuration |  |  | [8] 2.2.2 |  |  | C.2 |  |  |
| 3 |  |  | BR/EDR/LE Core-Host Configuration |  |  | [8] 2.2.3 |  |  | C.3 |  |  |
| 4 |  |  | HS Core-Host Configuration |  |  | [8] 2.2.4 |  |  | C.4 |  |  |
| 5 |  |  | HS/LE Core-Host Configuration |  |  | [8] 2.2.5 |  |  | C.5 |  |  |

C.1: Mandatory IF CORE 20/2 “BR/EDR Host Layers” AND NOT CORE 20/4 “LE Host Layers” AND NOT CORE 11/20 “AMP Manager Protocol (A2MP)”, otherwise Excluded. C.2: Mandatory IF CORE 20/4 “LE Host Layers” AND NOT CORE 20/2 “BR/EDR Host Layers”, otherwise Excluded. C.3: Mandatory IF CORE 20/2 “BR/EDR Host Layers” AND CORE 20/4 “LE Host Layers” AND NOT CORE 11/20 “AMP Manager Protocol (A2MP)”, otherwise Excluded.
C.4: Mandatory IF CORE 20/2 “BR/EDR Host Layers” AND CORE 11/20 “AMP Manager Protocol (A2MP)” AND NOT CORE 20/4 “LE Host Layers”, otherwise Excluded. C.5: Mandatory IF CORE 20/2 “BR/EDR Host Layers” AND CORE 20/4 “LE Host Layers” AND CORE 11/20 “AMP Manager Protocol (A2MP)”, otherwise Excluded.
Table 32 (auto-fill): Core-Complete Configurations

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR Core-Complete Configuration |  |  | [8] 2.3.1 |  |  | C.1 |  |  |
| 2 |  |  | LE Core-Complete Configuration |  |  | [8] 2.3.2 |  |  | C.2 |  |  |
| 3 |  |  | BR/EDR/LE Core-Complete Configuration |  |  | [8] 2.3.3 |  |  | C.3 |  |  |
| 4 |  |  | HS Core-Complete Configuration |  |  | [8] 2.3.4 |  |  | C.4 |  |  |
| 5 |  |  | HS/LE Core-Complete Configuration |  |  | [8] 2.3.5 |  |  | C.5 |  |  |

C.1: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/2 “BR/EDR Host Layers” AND NOT (CORE 20/3 “LE Controller Layers” AND CORE 20/4 “LE Host Layers”) AND NOT (CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” AND CORE 11/20 “AMP Manager Protocol (A2MP)”), otherwise Excluded. C.2: Mandatory IF CORE 20/3 “LE Controller Layers” AND CORE 20/4 “LE Host Layers” AND NOT (CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/2 “BR/EDR Host Layers”), otherwise Excluded. C.3: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/2 “BR/EDR Host Layers” AND CORE 20/3 “LE Controller Layers” AND CORE 20/4 “LE Host Layers” AND NOT (CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” AND CORE 11/20 “AMP Manager Protocol (A2MP)”), otherwise Excluded. C.4: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/2 “BR/EDR Host Layers” AND CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” AND CORE 11/20 “AMP Manager Protocol (A2MP)” AND NOT (CORE 20/3 “LE Controller Layers” AND CORE 20/4 “LE Host Layers”), otherwise Excluded. C.5: Mandatory IF CORE 20/1 “BR/EDR Controller Layers” AND CORE 20/2 “BR/EDR Host Layers” AND CORE 20/3 “LE Controller Layers” AND CORE 20/4 “LE Host Layers” AND CORE 10/20 “PAL for 802.11 MAC/PHY (802.11 PAL)” AND CORE 11/20 “AMP Manager Protocol (A2MP)”, otherwise Excluded.

### 1.7 Configurations

Table 40 (auto-fill): Configurations

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Core-Controller |  |  | [8] 2.1 |  |  | C.1 |  |  |
| 2 |  |  | Core-Host |  |  | [8] 2.2 |  |  | C.2 |  |  |
| 3 |  |  | Core-Complete |  |  | [8] 2.3 |  |  | C.3 |  |  |

C.1: Mandatory IF CORE 30/1 “BR/EDR Core-Controller Configuration” OR CORE 30/2 “LE Core- Controller Configuration” OR CORE 30/3 “BR/EDR/LE Core-Controller Configuration” OR CORE 30/4 “HS Core-Controller Configuration” OR CORE 30/5 “HS/LE Core-Controller Configuration”, otherwise Excluded. C.2: Mandatory IF CORE 31/1 “BR/EDR Core-Host Configuration” OR CORE 31/2 “LE Core-Host Configuration” OR CORE 31/3 “BR/EDR/LE Core-Host Configuration” OR CORE 31/4 “HS Core- Host Configuration” OR CORE 31/5 “HS/LE Core-Host Configuration”, otherwise Excluded. C.3: Mandatory IF CORE 32/1 “BR/EDR Core-Complete Configuration” OR CORE 32/2 “LE Core- Complete Configuration” OR CORE 32/3 “BR/EDR/LE Core-Complete Configuration” OR
CORE 32/4 “HS Core-Complete Configuration” OR CORE 32/5 “HS/LE Core-Complete Configuration”, otherwise Excluded.
Table 41 (auto-fill): Transport Configurations

|  | Item |  |  | Feature |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR Core Configuration |  |  | [8] 2 |  |  | C.1 |  |  |
| 2 |  |  | LE Core Configuration |  |  | [8] 2 |  |  | C.2 |  |  |
| 3 |  |  | BR/EDR/LE Core Configuration |  |  | [8] 2 |  |  | C.3 |  |  |

C.1: Mandatory IF CORE 30/1 “BR/EDR Core-Controller Configuration” OR CORE 30/4 “HS Core- Controller Configuration” OR CORE 31/1 “BR/EDR Core-Host Configuration” OR CORE 31/4 “HS Core-Host Configuration” OR CORE 32/1 “BR/EDR Core-Complete Configuration” OR CORE 32/4 “HS Core-Complete Configuration”, otherwise Excluded. C.2: Mandatory IF CORE 30/2 “LE Core-Controller Configuration” OR CORE 31/2 “LE Core-Host Configuration” OR CORE 32/2 “LE Core-Complete Configuration”, otherwise Excluded. C.3: Mandatory IF CORE 30/3 “BR/EDR/LE Core-Controller Configuration” OR CORE 30/5 “HS/LE Core-Controller Configuration” OR CORE 31/3 “BR/EDR/LE Core-Host Configuration” OR CORE 31/5 “HS/LE Core-Host Configuration” OR CORE 32/3 “BR/EDR/LE Core-Complete Configuration” OR CORE 32/5 “HS/LE Core-Complete Configuration”, otherwise Excluded.

## 2 References

[1] Core Specification Version 4.2. Adopted 02 December 2014.
[2] Core Specification Version 5.0. Adopted 06 December 2016.
[3] Core Specification Version 5.1. Adopted 15 January 2019.
[4] Core Specification Version 5.2. Adopted 31 December 2019.
[5] Core Specification Version 5.3. Adopted 06 July 2021.
[6] Core Specification Version 5.4. Adopted 31 January 2023.
[7] Core Specification Addendum 5. Adopted 01 December 2015.
[8] Core Specification Version 4.2 or later, Volume 0, Part D, Core Configurations
[9] ICS Proforma for Radio (RF)
[10] ICS Proforma for Baseband (BB)
[11] ICS Proforma for Link Manager Protocol (LMP)
[12] ICS Proforma for Security (SEC)
[13] ICS Proforma for Physical Layer (RFPHY)
[14] ICS Proforma for Link Layer (LL)
[15] ICS Proforma for Low Energy Link Layer Security (LESEC)
[16] ICS Proforma for Isochronous Adaptation Layer (IAL)
[17] ICS Proforma for 802.11 Protocol Adaptation Layer (802.11 PAL)
[18] ICS Proforma for 802.11 MAC/PHY (802.11 MP)
[19] ICS Proforma for Logical Link Control and Adaptation Protocol (L2CAP)
[20] ICS Proforma for Service Discovery Protocol (SDP)
[21] ICS Proforma for Generic Access Profile (GAP)
[22] ICS Proforma for Attribute Protocol (ATT)
[23] ICS Proforma for Generic Attribute Profile (GATT)
[24] ICS Proforma for Security Manager (SM)
[25] ICS Proforma for AMP Manager Protocol (A2MP)
[26] ICS Proforma for Host Controller Interface, Lower HCI Role (HCI)
[27] ICS Proforma for Host Controller Interface, Upper HCI Role (UHCI)
[28] Core Specification Version 6.0. Adopted 27 August 2024.
[29] ICS Proforma for Channel Sounding (CS)

## 3 Configuration summary (informational)

The configuration summary table below is provided for informational purposes. In the event of any contradiction with the ICS tables in Section 1 or with the Core Specifications, the table below should be assumed to be wrong.

| Summary of Core Configuration options and their included Bluetooth Layers |  |  |  |  | Core version dependency | Core-Controller Configuration See Table 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Core-Host Configuration See Table 31 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Core-Complete Configuration See Table 32 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  | BR/EDR Controller |  |  | LE Controller |  |  | BR/EDR/LE Controller |  |  | HS Controller |  |  | HS/LE Controller |  |  | BR/EDR Host |  |  | LE Host |  |  | BR/EDR/LE Host |  |  | HS Host |  |  | HS/LE Host |  |  | BR/EDR Complete |  |  | LE Complete |  |  | BR/EDR/LE Complete |  |  | HS Complete |  |  | HS/LE Complete |  |
| Core version dependency |  |  |  |  |  | C.6 C.6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C.7 C.7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C.8 C.8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Core Layers |  | Controller Layers See Table 10 | SEC |  | M |  |  | C.12 |  |  | M |  |  | M |  |  | M |  |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | M |  |  | C.12 |  |  | M |  |  | M |  |  | M |  |  |
|  |  |  |  | LMP |  | M C.12 M M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | M C.12 M M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | BB |  | M |  |  | C.12 |  |  | M |  |  | M |  |  | M |  |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | M |  |  | C.12 |  |  | M |  |  | M |  |  | M |  |  |
|  |  |  |  | RF |  | M C.12 M M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | M C.12 M M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | IAL | C.5 | C.12 |  |  | C.3 |  |  | C.3 |  |  | C.12 |  |  | C.3 |  |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | C.12 |  |  | C.3 |  |  | C.3 |  |  | C.12 |  |  | C.3 |  |  |
|  |  |  |  | CS | C.13 | C.12 C.14 C.14 C.12 C.14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C.12 C.14 C.14 C.12 C.14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | LESEC |  | C.12 |  |  | C.11 |  |  | C.11 |  |  | C.12 |  |  | C.11 |  |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | C.12 |  |  | C.11 |  |  | C.11 |  |  | C.12 |  |  | C.11 |  |  |
|  |  |  |  | LL |  | C.12 M M C.12 M |  |  |  |  |  |  |  |  |  |  |  |  |  |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C.12 M M C.12 M |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | RFPHY |  | C.12 |  |  | M |  |  | M |  |  | C.12 |  |  | M |  |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | C.12 |  |  | M |  |  | M |  |  | C.12 |  |  | M |  |  |
|  |  |  |  | PAL for 802.11 MP | C.6 | E C.12 E M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | E C.12 E M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | HCI | Lower HCI role |  | M |  |  | M |  |  | M |  |  | M |  |  | M |  |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | C.10 |  |  | C.10 |  |  | C.10 |  |  | C.10 |  |  | C.10 |  |  |
|  |  |  | See Table 12 | Upper HCI role |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | M M M M M |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C.10 C.10 C.10 C.10 C.10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | Host Layers | GATT |  | E |  |  | E |  |  | E |  |  | E |  |  | E |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  | C.1 |  |  |
|  |  |  | See Table 11 | ATT |  | E E E E E |  |  |  |  |  |  |  |  |  |  |  |  |  |  | O C.2 C.4 O C.4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | O C.2 C.4 O C.4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


|  |  | GAP |  | E | E | E | E | E | M | M | M | M | M | M | M | M | M | M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | SDP |  | E E E E E |  |  |  |  | M C.12 M M M |  |  |  |  | M C.12 M M M |  |  |  |  |
|  |  | L2CAP |  | E | E | E | E | E | M | C.2 | M | M | M | M | C.2 | M | M | M |
|  |  | SM |  | E E E E E |  |  |  |  | C.12 C.2 C.2 C.12 C.2 |  |  |  |  | C.12 C.2 C.2 C.12 C.2 |  |  |  |  |
|  |  | A2MP | C.7 | E | E | E | E | E | E | C.12 | E | M | M | E | C.12 | E | M | M |
| X2Core Layers |  |  |  | C.9 C.9 C.9 C.9 C.9 |  |  |  |  | O O O O O |  |  |  |  | O O O O O |  |  |  |  |

C.1: Mandatory if ATT is included, otherwise Excluded. C.2: Mandatory if either the GAP Central role or the GAP Peripheral role is supported, otherwise Excluded. C.3: Mandatory if Link Layer (LL) supports any of the following features: 1: Connected Isochronous Stream (Central), 2: Connected Isochronous Stream (Peripheral), 3: Isochronous Broadcaster, 4: Synchronized Receiver, otherwise Excluded. C.4: Mandatory if either the GAP Central role or the GAP Peripheral role is supported, otherwise Optional. C.5: Excluded if one of Controller Core v4.2, Controller Core v5.0, Controller Core v5.1 is supported. C.6: Excluded if none of Controller Core v4.2, Controller Core v5.0, Controller Core v5.1, Controller Core v5.2 are supported. C.7: Excluded if none of Host Core v4.2, Host Core v5.0, Host Core v5.1, Host Core v5.2 are supported. C.8: Excluded if none of Controller Core v4.2, Controller Core v5.0, Controller Core v5.1, Controller Core v5.2 and none of Host Core v4.2, Host Core v5.0, Host Core v5.1, Host Core v5.2 are supported. C.9: Optional for Codec-in-the-Controller layers, otherwise Excluded. C.10: Mandatory to support none or both of Upper HCI role and Lower HCI role. C.11: Mandatory if the LE Encryption feature is supported, otherwise Excluded. C.12: Excluded if including the layer would make the IUT also be compliant to another Core Configuration, otherwise Optional. C.13: Excluded if Controller Core v6.0 is not supported C.14: Mandatory if Link Layer (LL) supports the Channel Sounding (CS) feature, otherwise Excluded.

## 4 Bridge mapping between CORE ICS and prior

SUM ICS (informational)
Erratum 23556 removed Vol 0, Part B “Compliance” and Vol 1, Part D “Mixing Of Specification Versions” from the Core specification and replaced them with a new Vol 0, Part D “Core Configurations”.
Prior to Erratum 23556, the concepts of product types, as well as some conditions tied to specific core capabilities, were described in Vol 0, Part B “Compliance” and indicated by entries in SUM.ICS. For legacy reasons, the Bluetooth SIG qualification tool implementation of SUM.ICS was separated into two parts 1) PROD.ICS (Table 11 of SUM ICS) and 2) the Core-specific tables of SUM.ICS under the label “SUM.ICS”.
Table 4.1 provides the mapping between the new CORE ICS and the prior PROD ICS and SUM ICS items. If an implementation previously supported one of the prior capabilities, then it now supports the corresponding CORE ICS capability. The mapping entry “auto-fill” indicates that the CORE ICS item can be automatically derived from other CORE ICS items. The mapping entry “Not supported” indicates that the CORE ICS item is automatically set to not supported.
Core v5.4 was the last version in SUM ICS. Therefore, any CORE ICS items added with Core v6.0 or later are not explicitly mapped and missing from Table 4.1. These CORE ICS items should be considered “Not supported” unless otherwise stated.

|  | CORE ICS |  |  | Description |  |  | Mapping |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CORE 1/1 |  |  | Controller Core any version |  |  | layer selection (LMP) OR layer selection (BB) OR layer selection (RF) OR layer selection (IAL) OR layer selection (LL) OR layer selection (RFPHY) OR layer selection (80211PAL) |  |  |
| CORE 1/42 |  |  | Controller Core v4.2 |  |  | SUM ICS 21/14 “Controller v4.2” |  |  |
| CORE 1/50 |  |  | Controller Core v5.0 |  |  | SUM ICS 21/16 “Controller v5.0” |  |  |
| CORE 1/51 |  |  | Controller Core v5.1 |  |  | SUM ICS 21/18 “Controller v5.1” |  |  |
| CORE 1/52 |  |  | Controller Core v5.2 |  |  | SUM ICS 21/20 “Controller v5.2” |  |  |
| CORE 1/53 |  |  | Controller Core v5.3 |  |  | SUM ICS 21/21 “Controller v5.3” |  |  |
| CORE 1/54 |  |  | Controller Core v5.4 |  |  | SUM ICS 21/22 “Controller v5.4” |  |  |
| CORE 1a/50 |  |  | Controller Core v5.0 or later |  |  | auto-fill |  |  |
| CORE 1a/51 |  |  | Controller Core v5.1 or later |  |  | auto-fill |  |  |
| CORE 1a/52 |  |  | Controller Core v5.2 or later |  |  | auto-fill |  |  |
| CORE 1a/53 |  |  | Controller Core v5.3 or later |  |  | auto-fill |  |  |
| CORE 1a/54 |  |  | Controller Core v5.4 or later |  |  | auto-fill |  |  |
| CORE 1b/50 |  |  | Controller Core v5.0 or earlier |  |  | auto-fill |  |  |
| CORE 1b/51 |  |  | Controller Core v5.1 or earlier |  |  | auto-fill |  |  |
| CORE 1b/52 |  |  | Controller Core v5.2 or earlier |  |  | auto-fill |  |  |
| CORE 1b/53 |  |  | Controller Core v5.3 or earlier |  |  | auto-fill |  |  |
| CORE 1b/54 |  |  | Controller Core v5.4 or earlier |  |  | auto-fill |  |  |
| CORE 1c/1 |  |  | Core Specification Addendum 5 |  |  | SUM ICS 21/15 “CSA5” |  |  |


|  | CORE ICS |  |  | Description |  |  | Mapping |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CORE 2/1 |  |  | Host Core any version |  |  | layer selection (GATT) OR layer selection (ATT) OR layer selection (GAP) OR layer selection (SDP) OR layer selection (L2CAP) OR layer selection (SM) OR layer selection (A2MP) |  |  |
| CORE 2/42 |  |  | Host Core v4.2 |  |  | SUM ICS 31/17“Host v4.2” OR SUM ICS 31/18 “Host v4.2+HS” |  |  |
| CORE 2/50 |  |  | Host Core v5.0 |  |  | SUM ICS 31/19 “Host v5.0” |  |  |
| CORE 2/51 |  |  | Host Core v5.1 |  |  | SUM ICS 31/20 “Host v5.1” |  |  |
| CORE 2/52 |  |  | Host Core v5.2 |  |  | SUM ICS 31/21 “Host v5.2” |  |  |
| CORE 2/53 |  |  | Host Core v5.3 |  |  | SUM ICS 31/22 “Host v5.3” |  |  |
| CORE 2/54 |  |  | Host Core v5.4 |  |  | SUM ICS 31/23 “Host v5.4” |  |  |
| CORE 2a/50 |  |  | Host Core v5.0 or later |  |  | auto-fill |  |  |
| CORE 2a/51 |  |  | Host Core v5.1 or later |  |  | auto-fill |  |  |
| CORE 2a/52 |  |  | Host Core v5.2 or later |  |  | auto-fill |  |  |
| CORE 2a/53 |  |  | Host Core v5.3 or later |  |  | auto-fill |  |  |
| CORE 2a/54 |  |  | Host Core v5.4 or later |  |  | auto-fill |  |  |
| CORE 2b/50 |  |  | Host Core v5.0 or earlier |  |  | auto-fil |  |  |
| CORE 2b/51 |  |  | Host Core v5.1 or earlier |  |  | auto-fill |  |  |
| CORE 2b/52 |  |  | Host Core v5.2 or earlier |  |  | auto-fill |  |  |
| CORE 2b/53 |  |  | Host Core v5.3 or earlier |  |  | auto-fill |  |  |
| CORE 2b/54 |  |  | Host Core v5.4 or earlier |  |  | auto-fill |  |  |
| CORE 10/1 |  |  | BR/EDR Security (SEC) |  |  | layer selection (LMP) |  |  |
| CORE 10/2 |  |  | Link Manager Protocol (LMP) |  |  | layer selection (LMP) |  |  |
| CORE 10/3 |  |  | Baseband (BB) |  |  | layer selection (BB) |  |  |
| CORE 10/4 |  |  | Radio Frequency (RF) |  |  | layer selection (RF) |  |  |
| CORE 10/10 |  |  | Isochronous Adaptation Layer (IAL) |  |  | layer selection (IAL) |  |  |
| CORE 10/11 |  |  | LE Security (LESEC) |  |  | LL 9/1 “LE Encryption” |  |  |
| CORE 10/12 |  |  | Link Layer (LL) |  |  | layer selection (LL) |  |  |
| CORE 10/13 |  |  | Radio Frequency Physical Layer (RFPHY) |  |  | layer selection (RFPHY) |  |  |
| CORE 10/20 |  |  | PAL for 802.11 MAC/PHY (802.11 PAL) |  |  | layer selection (80211PAL) |  |  |
| CORE 11/1 |  |  | Generic Attribute Profile (GATT) |  |  | layer selection (GATT) |  |  |
| CORE 11/2 |  |  | Attribute Protocol (ATT) |  |  | layer selection (ATT) |  |  |
| CORE 11/3 |  |  | Generic Access Profile (GAP) |  |  | layer selection (GAP) |  |  |
| CORE 11/4 |  |  | Service Discovery Protocol (SDP) |  |  | layer selection (SDP) |  |  |
| CORE 11/5 |  |  | Logical Link Control and Adaptation Protocol (L2CAP) |  |  | layer selection (L2CAP) |  |  |
| CORE 11/6 |  |  | Security Manager (SM) |  |  | layer selection (SM) |  |  |
| CORE 11/20 |  |  | AMP Manager Protocol (A2MP) |  |  | layer selection (A2MP) |  |  |


|  | CORE ICS |  |  | Description |  |  | Mapping |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CORE 12/1 |  |  | Host Controller Interface (HCI) |  |  | layer selection (HCI) OR PROD 1/4 “Host Subsystem” |  |  |
| CORE 12/2 |  |  | Lower HCI role |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” OR HCI 1a/4 “LE” |  |  |
| CORE 12/3 |  |  | Upper HCI role |  |  | HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI)) |  |  |
| CORE 13/1 |  |  | HCI-UART |  |  | Not supported |  |  |
| CORE 13/2 |  |  | HCI-USB |  |  | Not supported |  |  |
| CORE 13/3 |  |  | HCI-SD |  |  | Not supported |  |  |
| CORE 13/4 |  |  | HCI-3W |  |  | Not supported |  |  |
| CORE 13/5 |  |  | DTM |  |  | Not supported |  |  |
| CORE 13/6 |  |  | MWS |  |  | Not supported |  |  |
| CORE 13/7 |  |  | WCI-1 |  |  | Not supported |  |  |
| CORE 13/8 |  |  | WCI-2 |  |  | Not supported |  |  |
| CORE 20/1 |  |  | BR/EDR Controller Layers |  |  | auto-fill |  |  |
| CORE 20/2 |  |  | BR/EDR Host Layers |  |  | auto-fill |  |  |
| CORE 20/3 |  |  | LE Controller Layers |  |  | auto-fill |  |  |
| CORE 20/4 |  |  | LE Host Layers |  |  | auto-fill |  |  |
| CORE 20a/1 |  |  | LE connections |  |  | auto-fill |  |  |
| CORE 20a/2 |  |  | LE encryption |  |  | auto-fill |  |  |
| CORE 20a/3 |  |  | Isochronous channels |  |  | auto-fill |  |  |
| CORE 30/1 |  |  | BR/EDR Core-Controller Configuration |  |  | auto-fill |  |  |
| CORE 30/2 |  |  | LE Core-Controller Configuration |  |  | auto-fill |  |  |
| CORE 30/3 |  |  | BR/EDR/LE Core-Controller Configuration |  |  | auto-fill |  |  |
| CORE 30/4 |  |  | HS Core-Controller Configuration |  |  | auto-fill |  |  |
| CORE 30/5 |  |  | HS/LE Core-Controller Configuration |  |  | auto-fill |  |  |
| CORE 31/1 |  |  | BR/EDR Core-Host Configuration |  |  | auto-fill |  |  |
| CORE 31/2 |  |  | LE Core-Host Configuration |  |  | auto-fill |  |  |
| CORE 31/3 |  |  | BR/EDR/LE Core-Host Configuration |  |  | auto-fill |  |  |
| CORE 31/4 |  |  | HS Core-Host Configuration |  |  | auto-fill |  |  |
| CORE 31/5 |  |  | HS/LE Core-Host Configuration |  |  | auto-fill |  |  |
| CORE 32/1 |  |  | BR/EDR Core-Complete Configuration |  |  | auto-fill |  |  |
| CORE 32/2 |  |  | LE Core-Complete Configuration |  |  | auto-fill |  |  |
| CORE 32/3 |  |  | BR/EDR/LE Core-Complete Configuration |  |  | auto-fill |  |  |


|  | CORE ICS |  |  | Description |  |  | Mapping |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CORE 32/4 |  |  | HS Core-Complete Configuration |  |  | auto-fill |  |  |
| CORE 32/5 |  |  | HS/LE Core-Complete Configuration |  |  | auto-fill |  |  |
| CORE 40/1 |  |  | Core-Controller |  |  | auto-fill |  |  |
| CORE 40/2 |  |  | Core-Host |  |  | auto-fill |  |  |
| CORE 40/3 |  |  | Core-Complete |  |  | auto-fill |  |  |
| CORE 41/1 |  |  | BR/EDR Core Configuration |  |  | auto-fill |  |  |
| CORE 41/1 |  |  | LE Core Configuration |  |  | auto-fill |  |  |
| CORE 41/1 |  |  | BR/EDR/LE Core Configuration |  |  | auto-fill |  |  |

Table 4.1: Bridge mapping between SUM ICS and PROD ICS and supported CORE capabilities for QDIDs

## 5 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p0r00–r10 |  |  | 2023-09-27 – 2024-04-23 | TSE 24091 (rating 2): New CORE ICS to replace the now obsolete SUM ICS. TSE 24191 (rating 1): Added an informational section “Bridge mapping between CORE.ICS and prior SUM.ICS”. |
| 0 |  |  | p0 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p1r00–r07 |  |  | 2024-06-10 – 2024-08-07 | To support the Low Energy Extended Feature Set feature in Core Specification v6.0, incorporated CR Core LLExtendedFeatureSet Test CRr11-Jorg _ _ _ (which includes Test Issues 24450, 24696, 24807, 24896, and 24905) and added a reference to Core v6.0 and added 1/60. To support the Channel Sounding feature in Core Specification v6.0, incorporated CR CS Test CR r16-jorg (which includes Test Issues _ _ _ 23205, 23293, 23331, 23332, 23361, 23362, 23363, 23364, 23365, 23378, 23379, 23381, 23382, 23384, 23404, 23419, 23422, 23424, 23425, 23500, 23501, 23502, 23503, 23504, 23506, 23594, 23693, 23694, 23696, 23701, 23706, 23711, 23732, 23736, 23737, 23738, 23776, 23842, 23923, 23993, 24023, 24033, 24043, 24049, 24133, 24135, 24137, 24138, 24139, 24141, 24142, 24143, 24146, 24147, 24149, 24150, 24151, 24153, 24177, 24181, 24231, 24232, 24330, 24331, 24332, 24410, 24411, 24418, 24419, 24478, 24483, 24515, 24531, 24599, 24601, 24602, 24614, 24618, 24619, 24621, 24623, 24624, 24625, 24627, 24630, 24639, 24645, 24646, 24655, 24656, 24657, 24659, 24660, 24669, 24681, 24717, 24769, 24776, 24789, 24808, 24809, 24838, 24844, 24850, 24867, 24868, 24893, 24894, 24895, 25028, 25029, 25040, 25042, 25053, 25055, 25111, 25112, 25120, 25139, 25140, 25141, 25142, 25143, 25148, 25149, 25150, 25157, 25166, 25209, 25240, 25278, 25282, 25299, 25428, 25443, 25479, 25498, 25511, 25512, 25525, 25585, 25617, 25632) and added a reference to Core v6.0, 1/60, 1a/60 and associated C.6, 1b/60 and associated C.6, 2/60, 2a/60 and associated C.6, and 2b/60 and associated C.6. |
| 1 |  |  | p1 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Jörg Brakensiek |  |  | Bluetooth SIG, Inc. |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Shirin Ebrahimi-Taghizadeh |  |  | Microsoft |  |  |
| Miles Smith |  |  | Nordic Semiconductor A/S |  |  |
| Magnus Sommansson |  |  | Qualcomm Technologies International, Ltd. |  |  |
| Clive Feather |  |  | Samsung Cambridge Solution Centre |  |  |
