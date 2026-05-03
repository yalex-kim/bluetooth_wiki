# PBAP.ICS.p13

> Source: PDF converted via PyMuPDF.

---

Phone Book Access Profile (PBAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: PBAP.ICS.p13 ▪ Revision Date: 2026-02-17 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2004–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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
Table 2a: X.Y Versions (PCE)
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBAP 1.0** |  |  | PBAP 1.0 |  |  | Deprecated 2015-11-19. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | PBAP 1.1 |  |  | PBAP 1.1 |  |  | C.1, C.2 |  |  |
| 3 |  |  | PBAP 1.2 |  |  | PBAP 1.2 |  |  | C.1, C.3 |  |  |

C.1: Mandatory to support one and only one. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2015-11-19. Withdrawn 2023-02-01. C.3: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 2b: X.Y.Z Versions (PCE)
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBAP 1.1.1 |  |  | PBAP 1.1.1 |  |  | C.1 |  |  |
| 2 |  |  | PBAP 1.2.1** |  |  | PBAP 1.2.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 3 |  |  | PBAP 1.2.3 |  |  | PBAP 1.2.3 |  |  | C.2 |  |  |

C.1: Mandatory IF PBAP 2a/2 “PBAP 1.1”, otherwise Excluded. C.2: Mandatory IF PBAP 2a/3 “PBAP 1.2”, otherwise Excluded.
Table 9a: X.Y Versions (PSE)
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBAP 1.0** |  |  | PBAP 1.0 |  |  | Deprecated 2015-11-19. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | PBAP 1.1 |  |  | PBAP 1.1 |  |  | C.1, C.2 |  |  |
| 3 |  |  | PBAP 1.2 |  |  | PBAP 1.2 |  |  | C.1, C.3 |  |  |

** Deprecated versions may not appear in the Bluetooth SIG qualification tool after the deprecation date. TCRLs published after this date will not allow the use of deprecated versions.
C.1: Mandatory to support one and only one. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2015-11-19. Withdrawn 2023-02-01. C.3: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 9b: X.Y.Z Versions (PSE)
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PBAP 1.1.1 |  |  | PBAP 1.1.1 |  |  | C.1 |  |  |
| 2 |  |  | PBAP 1.2.1** |  |  | PBAP 1.2.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 3 |  |  | PBAP 1.2.3 |  |  | PBAP 1.2.3 |  |  | C.2 |  |  |

C.1: Mandatory IF PBAP 9a/2 “PBAP 1.1”, otherwise Excluded. C.2: Mandatory IF PBAP 9a/3 “PBAP 1.2”, otherwise Excluded.

### 2.2 Core Configuration

Table 0b: Core Configuration Requirements

|  | Item |  |  | Core Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 2.1 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 2.1 |  |  | C.2 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”. C.2: Excluded for this Profile. C.3: Mandatory for this Profile.

### 2.3 Roles

Table 1: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PCE |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 2 |  |  | PSE |  |  | [1] 2.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.4 PCE Features

Table 2: Supported Features (PCE)
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Phone Book Download |  |  | [1] 4.1 |  |  | C.1 |  |  |
| 2 |  |  | Phone Book Browsing |  |  | [1] 4.1 |  |  | C.1 |  |  |
| 3 |  |  | Session Management |  |  | [1] 2.4 |  |  | M |  |  |
| 4 |  |  | Able to Request Size of the Phonebook |  |  | [1] 5.1.4.3, 5.3.4.4 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 |  |  | Database Identifier |  |  | [5] 5.1.4.9 |  |  | C.2 |  |  |
| 6 |  |  | Folder Version Counters |  |  | [5] 5.1.4.8 |  |  | C.2 |  |  |
| 7 |  |  | vCard Selecting |  |  | [5] 5.1.4.7 |  |  | C.2 |  |  |
| 7a |  |  | Able to send vCardSelector |  |  | [5] 5.1.4.7 |  |  | C.2 |  |  |
| 7b |  |  | Able to send vCardSelectorOperator |  |  | [5] 5.1.4.7 |  |  | C.2 |  |  |
| 8 |  |  | Enhanced Missed Calls |  |  | [5] 5.1.4.6, 5.1.4.10 |  |  | C.4 |  |  |
| 8a |  |  | Able to reset the missed Calls |  |  | [5] 5.1.4.6, 5.1.4.10 |  |  | C.2 |  |  |
| 9 |  |  | X-BT-UCI vCard Property |  |  | [5] 3.1.4.5 |  |  | C.2 |  |  |
| 9a |  |  | Able to request X-BT-UCI Property |  |  | [5] 3.1.4.5 |  |  | C.2 |  |  |
| 10 |  |  | X-BT-UID vCard Property |  |  | [5] 3.1.4.4 |  |  | C.2 |  |  |
| 10a |  |  | Referencing Contacts |  |  | [5] 3.1.4.4 |  |  | C.2 |  |  |
| 12 |  |  | Contact Image Default Format |  |  | [5] 3.1.6.2 |  |  | C.2 |  |  |
| 12a |  |  | Able to request Contact Images |  |  | [5] 3.1.6.2 |  |  | C.2 |  |  |
|  |  |  | Supported Phonebook Objects |  |  |  |  |  |  |  |  |
| 13a |  |  | Telecom/pb |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13b |  |  | Telecom/ich |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13c |  |  | Telecom/och |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13d |  |  | Telecom/mch |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13e |  |  | Telecom/cch |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13f |  |  | Telecom/spd |  |  | [5] 3.1.5 |  |  | C.2 |  |  |
| 13g |  |  | Telecom/fav |  |  | [5] 3.1.5 |  |  | C.2 |  |  |
| 13h |  |  | SIM1/Telecom/pb |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13i |  |  | SIM1/Telecom/ich |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13j |  |  | SIM1/Telecom/och |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13k |  |  | SIM1/Telecom/mch |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
| 13l |  |  | SIM1/Telecom/cch |  |  | [1] 3.1.5 |  |  | C.3 |  |  |
|  |  |  | Search Behavior |  |  |  |  |  |  |  |  |
| 14 |  |  | Able to send SearchProperty |  |  | [5] 5.3.4.2 |  |  | O |  |  |
| 14a |  |  | Able to send SearchValue |  |  | [5] 5.3.4.3 |  |  | O |  |  |

C.1: Mandatory to support at least one. C.2: Optional IF PBAP 2a/3 “PBAP 1.2”, otherwise Excluded. C.3: Mandatory to support at least one. C.4: Optional IF PBAP 2a/3 “PBAP 1.2” AND (PBAP 2/13d “Telecom/mch” OR PBAP 2/13e “Telecom/cch” OR PBAP 2/13k “SIM1/Telecom/mch” OR PBAP 2/13l “SIM1/Telecom/cch”), otherwise Excluded.
Table 3: Supported Phone Book Download Functions (PCE)
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PullPhonebook |  |  | [1] 4.2 |  |  | C.1 |  |  |

C.1: Mandatory IF PBAP 2/1 “Phone Book Download”, otherwise Excluded.
Table 4: Supported Phone Book Browsing Functions (PCE)
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | SetPhonebook |  |  | [1] 4.3 |  |  | C.1 |  |  |
| 2 |  |  | PullvCardListing |  |  | [1] 4.3 |  |  | C.1 |  |  |
| 3 |  |  | PullvCardEntry |  |  | [1] 4.3 |  |  | C.1 |  |  |

C.1: Mandatory IF PBAP 2/2 “Phone Book Browsing”, otherwise Excluded.
Table 5: Used vCard Formats (PCE)
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | VCard 2.1 |  |  | [1] 3.1.4 |  |  | C.1 |  |  |
| 2 |  |  | VCard 3.0 |  |  | [1] 3.1.4 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

#### 2.4.1 PCE Features – OBEX

Table 6: OBEX Functions for PCE
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connect |  |  | [1] 6.1 |  |  | M |  |  |
| 2 |  |  | Disconnect |  |  | [1] 6.1 |  |  | M |  |  |
| 3 |  |  | Get |  |  | [1] 6.1 |  |  | M |  |  |
| 4 |  |  | Abort |  |  | [1] 6.1 |  |  | O |  |  |
| 5 |  |  | SetPath |  |  | [1] 6.1 |  |  | C.1 |  |  |
| 6 |  |  | Initiating OBEX Authentication |  |  | [1] 6.3 |  |  | C.2 |  |  |
| 7 |  |  | Responding to OBEX Authentication |  |  | [1] 6.3 |  |  | M |  |  |

C.1: Mandatory IF PBAP 2/2 “Phone Book Browsing”, otherwise Excluded. C.2: Optional IF PBAP 2a/2 “PBAP 1.1”, otherwise Excluded.
Table 7: PCE OBEX Header Support
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Name |  |  | [1] 6.2 |  |  | M |  |  |
| 2 |  |  | Type |  |  | [1] 6.2 |  |  | M |  |  |
| 3 |  |  | Body |  |  | [1] 6.2 |  |  | M |  |  |
| 4 |  |  | End of Body |  |  | [1] 6.2 |  |  | M |  |  |


|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 |  |  | Target |  |  | [1] 6.2 |  |  | M |  |  |
| 6 |  |  | Who (ability to parse) |  |  | [1] 6.2 |  |  | M |  |  |
| 7 |  |  | Connection ID |  |  | [1] 6.2 |  |  | M |  |  |
| 8 |  |  | Authentication Challenge |  |  | [1] 6.2 |  |  | M |  |  |
| 9 |  |  | Authentication Response |  |  | [1] 6.2 |  |  | M |  |  |
| 10 |  |  | Application Parameters |  |  | [1] 6.2 |  |  | M |  |  |
| 11 |  |  | Single Response Mode |  |  | [5] 5.1.5 |  |  | C.1 |  |  |
| 12 |  |  | Single Response Mode Parameter (ability to parse) |  |  | [5] 5.1.5 |  |  | C.1 |  |  |
| 13 |  |  | Single Response Mode Parameter (ability to send) |  |  | [5] 5.1.5 |  |  | C.2 |  |  |

C.1: Mandatory IF PBAP 2a/3 “PBAP 1.2”, otherwise Excluded. C.2: Optional IF PBAP 2a/3 “PBAP 1.2”, otherwise Excluded.
Table 8: OBEX Error Codes for PCE
Prerequisite: PBAP 1/1 “PCE”

|  | Item |  |  | OBEX Error Code |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bad Request |  |  | [1] 6.2.3 |  |  | M |  |  |
| 2 |  |  | Not Implemented |  |  | [1] 6.2.3 |  |  | M |  |  |
| 3 |  |  | Unauthorized |  |  | [1] 6.2.3 |  |  | M |  |  |
| 4 |  |  | Precondition Failed |  |  | [1] 6.2.3 |  |  | M |  |  |
| 5 |  |  | Not Found |  |  | [1] 6.2.3 |  |  | M |  |  |
| 6 |  |  | Not Acceptable |  |  | [1] 6.2.3 |  |  | M |  |  |
| 7 |  |  | Service Unavailable |  |  | [1] 6.2.3 |  |  | M |  |  |
| 8 |  |  | Forbidden |  |  | [1] 6.2.3 |  |  | M |  |  |


### 2.5 PSE Features

Table 9: Supported Features (PSE)
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Phone Book Download |  |  | [1] 4.1 |  |  | M |  |  |
| 2 |  |  | Phone Book Browsing |  |  | [1] 4.1 |  |  | M |  |  |
| 3 |  |  | Session Management |  |  | [1] 2.4 |  |  | M |  |  |
| 4 |  |  | Able to Return the size of the Phonebook |  |  | [1] 5.1.4.3, 5.3.4.4 |  |  | M |  |  |
| 5 |  |  | Database Identifier |  |  | [5] 5.1.4.9 |  |  | C.1 |  |  |
| 5a |  |  | Able to keep a persistent Database Identifier |  |  | [5] 5.1.4.9 |  |  | C.2 |  |  |
| 5b |  |  | Able to regenerate a Database Identifier |  |  | [5] 5.1.4.9 |  |  | C.2 |  |  |
| 6 |  |  | Folder Version Counters |  |  | [5] 5.1.4.8 |  |  | C.1 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6a |  |  | Able to Insert or Remove Entries |  |  | [5] 5.1.4.8 |  |  | C.2 |  |  |
| 6b |  |  | Able to Modify contact primary Properties* |  |  | [5] 5.1.4.8 |  |  | C.2 |  |  |
| 6c |  |  | Able to Modify contact secondary Properties |  |  | [5] 5.1.4.8 |  |  | C.2 |  |  |
| 7 |  |  | vCard Selecting |  |  | [5] 5.1.4.7 |  |  | C.1 |  |  |
| 8 |  |  | Enhanced Missed Calls |  |  | [5] 5.1.4.6, 5.1.4.10 |  |  | C.4 |  |  |
| 9 |  |  | X-BT-UCI vCard Property |  |  | [5] 3.1.4.5 |  |  | C.2 |  |  |
| 10 |  |  | X-BT-UID vCard Property |  |  | [5] 3.1.4.4 |  |  | C.2 |  |  |
| 10a |  |  | Referencing Contacts |  |  | [5] 3.1.4.4 |  |  | C.3 |  |  |
| 12 |  |  | Contact Image Default Format |  |  | [5] 3.1.6.2 |  |  | C.1 |  |  |
| 12a |  |  | Able to return Contact Images |  |  | [5] 3.1.6.2 |  |  | C.2 |  |  |
|  |  |  | Supported Repositories |  |  |  |  |  |  |  |  |
| 13a |  |  | Telecom/pb |  |  | [1] 3.1.5 |  |  | M |  |  |
| 13b |  |  | Telecom/ich |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13c |  |  | Telecom/och |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13d |  |  | Telecom/mch |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13e |  |  | Telecom/cch |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13f |  |  | Telecom/spd |  |  | [5] 3.1.5 |  |  | C.2 |  |  |
| 13g |  |  | Telecom/fav |  |  | [5] 3.1.5 |  |  | C.2 |  |  |
| 13h |  |  | SIM1/Telecom/pb |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13i |  |  | SIM1/Telecom/ich |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13j |  |  | SIM1/Telecom/och |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13k |  |  | SIM1/Telecom/mch |  |  | [1] 3.1.5 |  |  | O |  |  |
| 13l |  |  | SIM1/Telecom/cch |  |  | [1] 3.1.5 |  |  | O |  |  |
|  |  |  | Deleted Handles Behavior |  |  |  |  |  |  |  |  |
| 14a |  |  | Error reporting |  |  | [1] 3.1.5.1 |  |  | C.5 |  |  |
| 14b |  |  | Change tracking |  |  | [1] 3.1.5.1 |  |  | C.5 |  |  |

C.1: Mandatory IF PBAP 9a/3 “PBAP 1.2”, otherwise Excluded. C.2: Optional IF PBAP 9a/3 “PBAP 1.2”, otherwise Excluded. C.3: Optional IF PBAP 9/10 “X-BT-UID vCard Property”, otherwise Excluded. C.4: Optional IF PBAP 9a/3 “PBAP 1.2” AND (PBAP 9/13d “Telecom/mch” OR PBAP 9/13e “Telecom/cch” OR PBAP 9/13k “SIM1/Telecom/mch” OR PBAP 9/13l “SIM1/Telecom/cch”), otherwise Excluded. C.5: Mandatory to support at least one.
Table 10: Supported Phone Book Download Functions (PSE)
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PullPhonebook |  |  | [1] 4.2 |  |  | M |  |  |
| 2 |  |  | Call History Function |  |  | [1] 3.1.4.1 |  |  | O |  |  |

Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | SetPhonebook |  |  | [1] 4.3 |  |  | M |  |  |
| 2 |  |  | PullvCardListing |  |  | [1] 4.3 |  |  | M |  |  |
| 3 |  |  | PullvCardEntry |  |  | [1] 4.3 |  |  | M |  |  |

Table 12: Used vCard Formats (PSE)
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | VCard 2.1 |  |  | [1] 3.1.4 |  |  | M |  |  |
| 2 |  |  | VCard 3.0 |  |  | [1] 3.1.4 |  |  | M |  |  |


#### 2.5.1 PSE Features – OBEX

Table 13: OBEX Functions for PSE
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connect |  |  | [1] 6.1 |  |  | M |  |  |
| 2 |  |  | Disconnect |  |  | [1] 6.1 |  |  | M |  |  |
| 3 |  |  | Get |  |  | [1] 6.1 |  |  | M |  |  |
| 4 |  |  | Abort |  |  | [1] 6.1 |  |  | M |  |  |
| 5 |  |  | SetPath |  |  | [1] 6.1 |  |  | M |  |  |
| 6 |  |  | Initiating OBEX Authentication |  |  | [1] 6.3 |  |  | C.1 |  |  |
| 7 |  |  | Responding to OBEX Authentication |  |  | [1] 6.3 |  |  | M |  |  |

C.1: Optional IF PBAP 9a/2 “PBAP 1.1”, otherwise Excluded.
Table 14: PSE OBEX Header Support
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Name |  |  | [1] 6.2 |  |  | M |  |  |
| 2 |  |  | Type |  |  | [1] 6.2 |  |  | M |  |  |
| 3 |  |  | Body |  |  | [1] 6.2 |  |  | M |  |  |
| 4 |  |  | End of Body |  |  | [1] 6.2 |  |  | M |  |  |
| 5 |  |  | Target (ability to parse) |  |  | [1] 6.2 |  |  | M |  |  |
| 6 |  |  | Who |  |  | [1] 6.2 |  |  | M |  |  |
| 7 |  |  | Connection ID |  |  | [1] 6.2 |  |  | M |  |  |
| 8 |  |  | Authentication Challenge |  |  | [1] 6.2 |  |  | M |  |  |


|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 |  |  | Authentication Response |  |  | [1] 6.2 |  |  | M |  |  |
| 10 |  |  | Application Parameters |  |  | [1] 6.2 |  |  | M |  |  |
| 11 |  |  | Single Response Mode |  |  | [5] 5.1.5 |  |  | C.1 |  |  |
| 12 |  |  | Single Response Mode Parameter (ability to parse) |  |  | [5] 5.1.5 |  |  | C.1 |  |  |
| 13 |  |  | Single Response Mode Parameter (ability to send) |  |  | [5] 5.1.5 |  |  | C.2 |  |  |

C.1: Mandatory IF PBAP 9a/3 “PBAP 1.2”, otherwise Excluded. C.2: Optional IF PBAP 9a/3 “PBAP 1.2”, otherwise Excluded.
Table 15: OBEX Error Codes for PSE
Prerequisite: PBAP 1/2 “PSE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bad Request |  |  | [1] 6.2.3 |  |  | M |  |  |
| 2 |  |  | Not Implemented |  |  | [1] 6.2.3 |  |  | M |  |  |
| 3 |  |  | Unauthorized |  |  | [1] 6.2.3 |  |  | O |  |  |
| 4 |  |  | Precondition Failed |  |  | [1] 6.2.3 |  |  | C.1 |  |  |
| 5 |  |  | Not Found |  |  | [1] 6.2.3 |  |  | M |  |  |
| 6 |  |  | Not Acceptable |  |  | [1] 6.2.3 |  |  | O |  |  |
| 7 |  |  | Service Unavailable |  |  | [1] 6.2.3 |  |  | M |  |  |
| 8 |  |  | Forbidden |  |  | [1] 6.2.3 |  |  | O |  |  |

C.1: Mandatory IF PBAP 9/14b “Change tracking”, otherwise Optional.

## 3 Requirements towards other Bluetooth profiles


### 3.1 GAP requirements

Table 16: GAP Modes for PCE
Prerequisite: PBAP 1/1 “PCE”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [1] 8.1 | M | [3] GAP 1/3 |  |  |
| 2 | Bondable mode | [1] 8.1 | M | [3] GAP 1/7 |  |  |

Table 17: GAP Modes for PSE
Prerequisite: PBAP 1/2 “PSE”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [1] 8.1 | M | [3] GAP 1/3 |  |  |
| 2 | Bondable mode | [1] 8.1 | M | [3] GAP 1/7 |  |  |

Table 18: No longer used
Table 19: No longer used
Table 20: No longer used
Table 21: GAP Idle Modes for PSE
Prerequisite: PBAP 1/2 “PSE”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initiation of general inquiry | [1] 8.2.1 | M | [3] GAP 3/1 |  |  |
| 2 | Initiation of limited inquiry | [1] 8.2.1 | O | [3] GAP 3/2 |  |  |
| 3 | Initiation of general bonding | [1] 8.2.2 | M | [3] GAP 3/5 |  |  |


### 3.2 SDP requirements

Table 22: SDP Requirements (PCE)
Prerequisite: PBAP 1/1 “PCE”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | BluetoothProfileDescriptorList | [1] 7.1.1 | M | [2] SDP 9/14 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 2 | ServiceName | [1] 7.1.1 | M | [2] SDP 9/9 |  |  |

Table 23: SDP Requirements (PSE)
Prerequisite: PBAP 1/2 “PSE”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | ProtocolDescriptorList | [1] 7.1.2 | M | [2] SDP 9/2 |  |  |
| 2 | BluetoothProfileDescriptorList | [1] 7.1.2 | M | [2] SDP 9/14 |  |  |
| 3 | ServiceName | [1] 7.1.1 | M | [2] SDP 9/9 |  |  |


### 3.3 GOEP requirements


#### 3.3.1 GOEP 2.0 or Later Features

Table 25: GOEP 2.0 or Later Features (PCE)
Prerequisite: PBAP 2a/3 “PBAP 1.2” AND PBAP 1/1 “PCE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | GOEP v2.0 or later |  |  | [4] |  |  | M |  |  |
| 2 |  |  | GOEP v2.0 or later Backwards Compatibility |  |  | [4] 5.2 |  |  | M |  |  |
| 3 |  |  | OBEX over L2CAP |  |  | [4] 3 |  |  | M |  |  |
| 4 |  |  | OBEX SRM |  |  | [4] 4.6 |  |  | M |  |  |
| 5 |  |  | Send OBEX SRMP header |  |  | [4] 4.6 |  |  | C.1 |  |  |
| 6 |  |  | Receive OBEX SRMP header |  |  | [4] 4.6 |  |  | M |  |  |

C.1: Optional IF PBAP 25/4 “OBEX SRM”, otherwise Excluded.
Table 26: GOEP 2.0 or Later Features (PSE)
Prerequisite: PBAP 9a/3 “PBAP 1.2” AND PBAP 1/2 “PSE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | GOEP v2.0 or later |  |  | [4] |  |  | M |  |  |
| 2 |  |  | GOEP v2.0 or later Backwards Compatibility |  |  | [4] 5.2 |  |  | M |  |  |
| 3 |  |  | OBEX over L2CAP |  |  | [4] 3 |  |  | M |  |  |
| 4 |  |  | OBEX SRM |  |  | [4] 4.6 |  |  | M |  |  |
| 5 |  |  | Send OBEX SRMP header |  |  | [4] 4.6 |  |  | C.1 |  |  |
| 6 |  |  | Receive OBEX SRMP header |  |  | [4] 4.6 |  |  | M |  |  |

C.1: Optional IF PBAP 26/4 “OBEX SRM”, otherwise Excluded.

## 4 Supplementary interoperability verification

It is recommended but not required to support any of the capabilities defined below. The Bluetooth license grant obtained through Qualification is not predicated on passing any test that is linked to support of these capabilities.
Table 24: Additional Phone Book Access Capabilities

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Retrieve Large Phone Book – PCE |  |  | N/A |  |  | C.1 |  |  |
| 2 |  |  | Transfer Large Phone Book – PSE |  |  | N/A |  |  | C.2 |  |  |
| 3 |  |  | Retrieve Empty Phone Book – PCE |  |  | N/A |  |  | C.1 |  |  |
| 4 |  |  | Transfer Empty Phone Book – PSE |  |  | N/A |  |  | C.2 |  |  |
| 5 |  |  | Return Phonebook – Limit number of entries |  |  | N/A |  |  | C.2 |  |  |
| 6 |  |  | Return vCard listing – Limit number of entries |  |  | N/A |  |  | C.2 |  |  |
| 7 |  |  | Phone Book Order |  |  | N/A |  |  | C.2 |  |  |
| 8 |  |  | Call stack timestamps – PSE |  |  | N/A |  |  | C.3 |  |  |
| 9 |  |  | No User Interaction – PSE |  |  | N/A |  |  | C.2 |  |  |
| 10 |  |  | Special Character Handling – PSE |  |  | N/A |  |  | C.2 |  |  |

C.1: Optional IF PBAP 2/1 “Phone Book Download”, otherwise Excluded. C.2: Optional IF PBAP 1/2 “PSE”, otherwise Excluded. C.3: Optional IF PBAP 10/2 “Call History Function”, otherwise Excluded.

## 5 References

[1] Bluetooth Phone Book Access Profile, Version 1.0 or later
[2] ICS Proforma for Service Discovery Protocol (SDP)
[3] ICS Proforma for Generic Access Profile (GAP)
[4] Bluetooth Generic Object Exchange Profile, Version 2.0 or later
[5] Bluetooth Phone Book Access Profile, Version 1.2 or later

## 6 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | 1.0.0 |  |  | 2006-03-02 | Publication date |
|  |  |  | 1.0.1r0 |  |  | 2006-11-10 | TSE 1804: Fix GAP-related inherited requirement issues TSE 1945: Add Items 6/6 and 13/6 for OBEX authentication initiation TSE 1979: Fix table numbers |
|  |  |  | 1.0.1r1 |  |  | 2006-12-08 | Input reviewer’s TSE 1804 comments of 11-30 and 12-08 |
| 1 |  |  | 1.0.1 |  |  | 2007-01-10 | Prepare for publication |
|  |  |  | 1.0.2r0 |  |  | 2009-04-29 | TSE 2699: New row in Table 2 and Table 9 |
| 2 |  |  | 1.0.2 |  |  | 2009-08-10 | Prepare for publication |
|  |  |  | 1.0.2a |  |  | 2009-10-28 | Fix radio button for 5/1 and 5/2 |
|  |  |  | 1.1.3r0 |  |  | 2011-11-11 | TSE 4113: Table 10; add row 2 TSE 4338: Table 6, Table 7, add row for Security mode 4 |
|  |  |  | 1.1.3r1 |  |  | 2012-02-20 | TSE 4685: New ICS table for Supplementary Interoperability Verification/Category-X test case mapping. |
| 3 |  |  | 1.1.3 |  |  | 2012-03-30 | Prepare for publication. |
|  |  |  | 1.3r00 |  |  | 2013-04-26 | Initial updates for PBAPII features |
|  |  |  | 1.3r01 |  |  | 2013-04-30 | Minor Editorial Updates |
|  |  |  | 1.3r02 |  |  | 2013-05-03 | Updated features following an update to the TCMT in the TS |
|  |  |  | 1.3r03 |  |  | 2013-05-05 | Addressed editorial issues |
|  |  |  | 1.2r07 |  |  | 2013-08-09 | Changed the version number since PBAPII is now targeted as PBAP 1.2. |
|  |  |  | 1.2r08 |  |  | 2013-09-26 | TSE 5311: Table 6. Change row 4 to O Addressed comments by BTI |
|  |  |  | 1.2r09 |  |  | 2013-10-03 | Fixed Minor Typos and text inconsistencies and incorrect table references |
| 4 |  |  | 1.2.0 |  |  | 2013-11-05 | Adopted by the BoD |
|  |  |  | 1.2.1r00 |  |  | 2014-10-25 | TSE 5665: Updated Table 0 and Table 0a to “No Longer Used”. Added Table 2a, 2b, 9a, 9b. Updated conditional references to reflect removal of 0 and 0a and addition of the new tables, Table 2, C.2 and C.4; Table 6, C.2; Table 7, C.2 and C.2; Table 9, C.1, C.2 and C.4; Table 13, C.1; Table 14 C.1 and C.2; Table 25, prerequisite; Table 26, prerequisite. |
|  |  |  | 1.2.1r01 |  |  | 2014-11-10 | BTI Review |
|  |  |  | 1.2.1r02 |  |  | 2014-11-25 | Corrected Stephen’s company name. |
| 5 |  |  | 1.2.1 |  |  | 2014-12-08 | Prepared for TCRL 2014-2 publication |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.2.2r00 |  |  | 2015-04-29 | TSE 5864: Added items 14 and 14a to Table 2 for Search Behavior |
|  |  |  | 1.2.2r01 |  |  | 2015-06-05 | Deleted Section 1.2 (Global Statement of Conformance) per current template standards. |
| 6 |  |  | 1.2.2 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 1.2.1.0r00 |  |  | 2015-11-23 | Updated version numbering to align with Specification version change from 1.2 to 1.2.1 for ESR09. With the specification taking a third identifying number, the ICS version identifier moves to the fourth number and starts again at 0. Added items 2b/2 and 9b/2 for minor version support. |
| 7 |  |  | 1.2.1.0 |  |  | 2015-12-22 | Prepared for TCRL 2015-2 publication. |
|  |  |  | 1.2.1.1r00 |  |  | 2018-05-09 | TSE 10587 (rating 2): Template Conversion. Removed IXIT items to separate IXIT spreadsheet format. |
| 8 |  |  | 1.2.1.1 |  |  | 2018-07-01 | Approved by BTI. Prepared for TCRL 2018-1 publication. |
|  |  |  | 1.2.1.2r00– r01 |  |  | 2018-08-20 – 2018-09-24 | Drafted 2019 Deprecation & Withdrawal changes. Deprecation & Withdrawal changes following BTI review: Updated tables 2a, 2b, 9a, 9b with deprecation dates for PBAP 1.0 and 1.1. Updated conditionals accordingly to enforce selection of a single version. |
| 9 |  |  | 1.2.3.0 |  |  | 2018-11-09 | Updated version number from 1.2.1.2 to 1.2.3.0 to align with adoption of the specification 1.2.3. Added items 2b/3 and 9b/3 for the new version. |
|  |  |  | 1.2.3.1r00 |  |  | 2019-04-29 | TSE 11972 (rating 2): Aligned PBAP ICS with the conventions discussed at the BTI Face to Face for deprecation and withdrawal impact. GAP Tables 18– 19 are no longer needed. Version Tables reference SDP versions. PBAP 1.1 (which was removed in Launch Studio) comes back but has a clear dependency on PBAP 1.1.1. |
| 10 |  |  | 1.2.3.1 |  |  | 2020-01-07 | Approved by BTI on 2019-11-17. Prepared for TCRL 2019-2 publication. |
|  |  |  | 1.2.3.1ed2 r00 |  |  | 2021-01-16 | TSE 15986 (rating 1): Updates for Deprecation. |
|  |  |  | 1.2.3.1 edition 2 |  |  | 2021-02-01 | Approved by BTI on 2021-01-18. Prepared for edition 2 publication. |
|  |  |  | 1.2.3.1ed3 r00–r01 |  |  | 2021-04-05 | TSE 16037 (rating 1): Updated incorrect item numbers in Table 9. Made template-related editorials, including assigning publication number 10 to previous v1.2.3.1. Added consistency checker fixes. TSE 16792 (rating 1): Updated the References section and refreshed cross-references within the tables to keep everything aligned, and updated several items, conditionals, and ILD entries per consistency checker findings. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.2.3.1 edition 3 |  |  | 2021-05-21 | Approved by BTI on 2021-05-06. Prepared for edition 3 publication. |
|  |  |  | 1.2.3.1ed4 r00–r01 |  |  | 2021-08-30 – 2021-09-24 | TSE 17431 (rating 1): Editorial corrections to table titles for Tables 2a, 2b, 9a, and 9b. Consistency checker editorials to align with the wording in the latest ICS template. |
|  |  |  | 1.2.3.1 edition 4 |  |  | 2021-09-28 | Approved by BTI on 2021-09-27. Prepared for edition 4 publication. |
|  |  |  | 1.2.3.1ed5 r00–r03 |  |  | 2023-02-08 – 2023-02-20 | TSE 22627 (rating 1): Adjusted the current Withdrawal date from February 2023 to February 2024 for PBAP 1.2 and 1.2.1. Moved Versions tables to the beginning of the document. Editorials to align the document with the latest ICS template. |
|  |  |  | 1.2.3.1 edition 5 |  |  | 2023-02-27 | Approved by BTI on 2023-02-23. Prepared for edition 5 publication. |
|  |  |  | p11r00 |  |  | 2023-10-18 | TSE 23945 (rating 2): Added missing GAP inter-layer dependencies in Tables 21–23. Updated the Reference value for Item 2 in Table 21. Deleted unnecessary introductory text in the OBEX sections and Section 2. Updated to align with the latest ICS template, including updates to the section and table titles. |
| 11 |  |  | p11 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p12r00 |  |  | 2025-02-27 | TSE 27013 (rating 2): Added “Core Configuration” section and Table 0b. Updated Tables 2a and 9a conditionals C.2 and C.3. Editorial updates to titles for Tables 0, 0a, 18, 19, and 20 and “GOEP requirements” heading. Applied the current ICS template. |
| 12 |  |  | p12 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p13r00 |  |  | 2025-12-05 – 2026-01-08 | TSE 28346 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 13 |  |  | p13 |  |  | 2026-02-17 | Approved by BTI on 2026-01-22. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Dominik Sollfrank |  |  | Berner & Mattner |  |  |
| Alicia Courtney |  |  | Broadcom, Inc. |  |  |
| Magnus Sommansson |  |  | Cambridge Sillicon Radio |  |  |
| Burch Seymour |  |  | Continental Automotive Systems |  |  |
| Stephen Raxter |  |  | Johnson Controls, Inc. |  |  |
| Stephen Raxter |  |  | National Analysis Center |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Stephane Bouet |  |  | Nissan |  |  |
| Nerissa Green |  |  | Nokia |  |  |
| Kyle Penri-Williams |  |  | Parrot |  |  |
| Scott Walsh |  |  | Plantronics, Inc. |  |  |
| Saravanun Sankaralingam |  |  | UL |  |  |
