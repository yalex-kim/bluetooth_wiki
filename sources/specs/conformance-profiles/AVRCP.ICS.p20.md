# AVRCP.ICS.p20

> Source: PDF converted via PyMuPDF.

---

Audio/Video Remote Control Profile (AVRCP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: AVRCP.ICS.p20 ▪ Revision Date: 2026-02-17 ▪ Prepared By: Audio, Telephony, & Automotive Working Group ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2003–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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
Table 2b: Controller – X.Y Versions
Prerequisite: AVRCP 1/1 “Controller”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AVRCP v1.0** |  |  | AVRCP v1.0 |  |  | Deprecated 2022-02-01. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | AVRCP v1.3** |  |  | AVRCP v1.3 |  |  | Deprecated 2023-02-01. Withdrawn 2027-02-01. |  |  |
| 3 |  |  | AVRCP v1.4** |  |  | AVRCP v1.4 |  |  | Deprecated 2013-08-01. Withdrawn 2023-02-01. |  |  |
| 4 |  |  | AVRCP v1.5 |  |  | [1] |  |  | C.1 |  |  |
| 5 |  |  | AVRCP v1.6 |  |  | [3] |  |  | C.1, C.2 |  |  |

C.1: Mandatory to support one and only one.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 2c: Controller – X.Y.Z Versions
Prerequisite: AVRCP 1/1 “Controller”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AVRCP v1.6.1** |  |  | AVRCP v1.6.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 2 |  |  | AVRCP v1.6.2 |  |  | [6] |  |  | C.1 |  |  |
| 3 |  |  | AVRCP v1.5.1 |  |  | [5] |  |  | C.2 |  |  |
| 4 |  |  | AVRCP v1.6.3 |  |  | [7] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one IF AVRCP 2b/5 “AVRCP v1.6”, otherwise Excluded.
C.2: Optional IF AVRCP 2b/4 “AVRCP v1.5”, otherwise Excluded.
Table 0b: No longer used
** Deprecated versions may not appear in the Bluetooth SIG qualification tool after the deprecation date. TCRLs published after this date will not allow the use of deprecated versions.
Prerequisite: AVRCP 1/2 “Target”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AVRCP v1.0** |  |  | AVRCP v1.0 |  |  | Deprecated 2022-02-01. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | AVRCP v1.3** |  |  | AVRCP v1.3 |  |  | Deprecated 2023-02-01. Withdrawn 2027-02-01. |  |  |
| 3 |  |  | AVRCP v1.4** |  |  | AVRCP v1.4 |  |  | Deprecated 2013-08-01. Withdrawn 2023-02-01. |  |  |
| 4 |  |  | AVRCP v1.5 |  |  | [1] |  |  | C.1 |  |  |
| 5 |  |  | AVRCP v1.6 |  |  | [3] |  |  | C.1, C.2 |  |  |

C.1: Mandatory to support one and only one.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 7c: Target – X.Y.Z Versions
Prerequisite: AVRCP 1/2 “Target”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 |  |  | AVRCP v1.6.1** |  |  | AVRCP v1.6.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 7 |  |  | AVRCP v1.6.2 |  |  | [6] |  |  | C.1 |  |  |
| 8 |  |  | AVRCP v1.5.1 |  |  | [5] |  |  | C.2 |  |  |
| 9 |  |  | AVRCP v1.6.3 |  |  | [7] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one IF AVRCP 7b/5 “AVRCP v1.6”, otherwise Excluded.
C.2: Optional IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Excluded.

### 2.2 Core Configuration

Table 0c: Core Configuration Requirements

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
| 1 |  |  | Controller |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 2 |  |  | Target |  |  | [1] 2.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.4 Controller features

Table 2: Controller Features
Prerequisite: AVRCP 1/1 “Controller”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiating connection establishment for control |  |  | [1] 4.1.1 |  |  | M |  |  |
| 2 |  |  | Accepting connection establishment for control initiated by TG |  |  | [1] 4.1.1 |  |  | M |  |  |
| 3 |  |  | Initiating connection release for control |  |  | [1] 4.1.2 |  |  | M |  |  |
| 4 |  |  | Accepting connection release for control initiated by TG |  |  | [1] 4.1.2 |  |  | M |  |  |
| 5 |  |  | Sending UNIT INFO command |  |  | [1] 4.1.3 |  |  | O |  |  |
| 6 |  |  | Sending SUBUNIT INFO command |  |  | [1] 4.1.3 |  |  | O |  |  |
| 7 |  |  | Sending PASS THROUGH command in category 1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 8 |  |  | Sending PASS THROUGH command in category 2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 9 |  |  | Sending PASS THROUGH command in category 3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 10 |  |  | Sending PASS THROUGH command in category 4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 11 |  |  | Get Capabilities |  |  | [1] 6.4.1 |  |  | O |  |  |
| 12 |  |  | List Player Application Setting Attributes |  |  | [1] 6.5.1 |  |  | C.9 |  |  |
| 13 |  |  | List Player Application Setting Values |  |  | [1] 6.5.2 |  |  | O |  |  |
| 14 |  |  | Get Current Player Application Setting Value |  |  | [1] 6.5.3 |  |  | C.10 |  |  |
| 15 |  |  | Set Player Application Setting Value |  |  | [1] 6.5.4 |  |  | C.10 |  |  |
| 16 |  |  | Get Player Application Setting Attribute Text |  |  | [1] 6.5.5 |  |  | O |  |  |
| 17 |  |  | Get Player Application Setting Value Text |  |  | [1] 6.5.6 |  |  | O |  |  |
| 18 |  |  | Inform Displayable Character Set |  |  | [1] 6.5.7 |  |  | O |  |  |
| 19 |  |  | Inform Battery Status of CT |  |  | [1] 6.5.8 |  |  | O |  |  |
| 20 |  |  | Get Element Attributes |  |  | [1] 6.6.1 |  |  | O |  |  |
| 21 |  |  | Get Play Status |  |  | [1] 6.7.1 |  |  | O |  |  |
| 22 |  |  | Register Notification |  |  | [1] 6.7.2 |  |  | C.11 |  |  |
| 23 |  |  | Request Continuing Response |  |  | [1] 6.8.1 |  |  | C.2 |  |  |
| 24 |  |  | Abort Continuing Response |  |  | [1] 6.8.2 |  |  | C.2 |  |  |
| 25 |  |  | Next Group |  |  | [1] 6.14.1 |  |  | C.12 |  |  |
| 26 |  |  | Previous Group |  |  | [1] 6.14.2 |  |  | C.12 |  |  |
| 27 |  |  | Media Player Selection |  |  | [1] 6.9 |  |  | O |  |  |
| 28 |  |  | SetAddressedPlayer |  |  | [1] 6.9.1 |  |  | O |  |  |
| 29 |  |  | GetFolderItems(MediaPlayerList) |  |  | [1] 6.10.4.2 |  |  | C.5 |  |  |
| 29b |  |  | GetTotalNumberOfItems(MediaPlayerList) |  |  | [3] 6.10.4.4 |  |  | C.15 |  |  |
| 30 |  |  | EVENT AVAILABLE PLAYERS CHANGED _ _ _ |  |  | [1] 6.9.4 |  |  | O |  |  |
| 31 |  |  | EVENT ADDRESSED PLAYER CHANGED _ _ _ |  |  | [1] 6.9.2 |  |  | O |  |  |
| 32 |  |  | Browsing |  |  | [1] 6.10 |  |  | O |  |  |
| 33 |  |  | SetBrowsedPlayer |  |  | [1] 6.9.3 |  |  | C.4 |  |  |
| 34 |  |  | ChangePath |  |  | [1] 6.10.4.1 |  |  | C.4 |  |  |
| 35 |  |  | GetFolderItems(Filesystem) |  |  | [1] 6.10.4.2 |  |  | C.4 |  |  |
| 35b |  |  | GetTotalNumberOfItems(Filesystem) |  |  | [3] 6.10.4.4 |  |  | C.15 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 |  |  | GetItemAttributes |  |  | [1] 6.10.4.3 |  |  | O |  |  |
| 37 |  |  | PlayItem(Filesystem) |  |  | [1] 6.12.1 |  |  | C.4 |  |  |
| 38 |  |  | EVENT UIDS CHANGED _ _ |  |  | [1] 6.10.3.3 |  |  | O |  |  |
| 39 |  |  | Searching |  |  | [1] 6.11 |  |  | O |  |  |
| 40 |  |  | Search |  |  | [1] 6.11 |  |  | C.7 |  |  |
| 41 |  |  | GetFolderItems(Search Results) |  |  | [1] 6.10.4.2 |  |  | C.7 |  |  |
| 41b |  |  | GetTotalNumberOfItems(Search Results) |  |  | [3] 6.10.4.4 |  |  | C.15 |  |  |
| 42 |  |  | PlayItem(SearchResultList) |  |  | [1] 6.12.1 |  |  | C.7 |  |  |
| 43 |  |  | NowPlaying |  |  | [1] 6.10.1 |  |  | C.8 |  |  |
| 44 |  |  | GetFolderItems(NowPlayingList) |  |  | [1] 6.10.4.2 |  |  | C.8 |  |  |
| 44b |  |  | GetTotalNumberOfItems(NowPlayingList) |  |  | [3] 6.10.4.4 |  |  | C.15 |  |  |
| 45 |  |  | PlayItem(NowPlayingList) |  |  | [1] 6.12.1 |  |  | C.8 |  |  |
| 46 |  |  | AddToNowPlaying |  |  | [1] 6.12.2 |  |  | O |  |  |
| 47 |  |  | EVENT NOW PLAYING CONTENT CHANGED _ _ _ _ |  |  | [1] 6.9.5 |  |  | O |  |  |
| 48 |  |  | Playable Folders |  |  | [1] 6.10.2.2 |  |  | O |  |  |
| 49 |  |  | Absolute Volume |  |  | [1] 6.13 |  |  | C.3 |  |  |
| 50 |  |  | SetAbsoluteVolume |  |  | [1] 6.13.2 |  |  | C.3 |  |  |
| 51 |  |  | NotifyVolumeChange |  |  | [1] 6.13.3 |  |  | C.3 |  |  |
| 52 |  |  | Discoverable Mode |  |  | [1] 12.1 |  |  | M |  |  |
| 53 |  |  | PASSTHROUGH operation supporting Press and Hold |  |  | [1] 4.1.3 |  |  | O |  |  |
| 54 |  |  | Cover Art |  |  | [3] 5.14 |  |  | C.15 |  |  |
| 55 |  |  | GetImageProperties |  |  | [3] 5.14 |  |  | C.14 |  |  |
| 56 |  |  | GetImage |  |  | [3] 5.14 |  |  | C.13 |  |  |
| 57 |  |  | GetLinkedThumbnail |  |  | [3] 5.14 |  |  | C.13 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory to support at least one IF AVRCP 2/20 “Get Element Attributes”, otherwise Optional.
C.3: Mandatory IF AVRCP 2/8 “Sending PASS THROUGH command in category 2”, otherwise Excluded.
C.4: Mandatory IF AVRCP 2/32 “Browsing”, otherwise Excluded.
C.5: Mandatory IF AVRCP 2/27 “Media Player Selection”, otherwise Excluded.
C.6: No longer used.
C.7: Mandatory IF AVRCP 2/39 “Searching”, otherwise Excluded.
C.8: Mandatory IF AVRCP 2/32 “Browsing”, otherwise Optional.
C.9: Mandatory IF AVRCP 2/13 “List Player Application Setting Values” OR AVRCP 2/14 “Get Current Player Application Setting Value” OR AVRCP 2/15 “Set Player Application Setting Value”, otherwise Optional.
C.10: Mandatory to support at least one IF AVRCP 2/12 “List Player Application Setting Attributes”, otherwise Excluded.
C.11: Mandatory IF AVRCP 2/20 “Get Element Attributes” OR AVRCP 2/49 “Absolute Volume”, otherwise Optional.
C.12: Mandatory to support none or all.
C.13: Excluded IF AVRCP 2b/4 “AVRCP v1.5”, otherwise Mandatory to support at least one IF AVRCP 2/54 “Cover Art”, otherwise Excluded.
C.14: Excluded IF AVRCP 2b/4 “AVRCP v1.5”, otherwise Optional IF AVRCP 2/54 “Cover Art”, otherwise Excluded.
C.15: Excluded IF AVRCP 2b/4 “AVRCP v1.5”, otherwise Optional.
Table 3: operation_id of category 1 for CT
Prerequisite: AVRCP 2/7 “Sending PASS THROUGH command in category 1”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 0 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 2 |  |  | 1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 3 |  |  | 2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 4 |  |  | 3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 5 |  |  | 4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 6 |  |  | 5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 7 |  |  | 6 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 8 |  |  | 7 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 9 |  |  | 8 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 10 |  |  | 9 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 11 |  |  | dot |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 12 |  |  | enter |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 13 |  |  | clear |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 14 |  |  | sound select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 15 |  |  | input select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 16 |  |  | display information |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 17 |  |  | help |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 18 |  |  | power |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 19 |  |  | play |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 20 |  |  | stop |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 21 |  |  | pause |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 22 |  |  | record |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 23 |  |  | rewind |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 24 |  |  | fast forward |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 25 |  |  | eject |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 26 |  |  | forward |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 27 |  |  | backward |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 28 |  |  | angle |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 29 |  |  | subpicture |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 30 |  |  | F1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 31 |  |  | F2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 32 |  |  | F3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 33 |  |  | F4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 34 |  |  | F5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |


|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 35 |  |  | vendor unique |  |  | [1] 4.1.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one item.
Table 4: operation_id of category 2 for CT
Prerequisite: AVRCP 2/8 “Sending PASS THROUGH command in category 2”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 0 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 2 |  |  | 1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 3 |  |  | 2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 4 |  |  | 3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 5 |  |  | 4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 6 |  |  | 5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 7 |  |  | 6 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 8 |  |  | 7 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 9 |  |  | 8 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 10 |  |  | 9 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 11 |  |  | dot |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 12 |  |  | enter |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 13 |  |  | clear |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 14 |  |  | sound select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 15 |  |  | input select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 16 |  |  | display information |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 17 |  |  | help |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 18 |  |  | power |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 19 |  |  | volume up |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 20 |  |  | volume down |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 21 |  |  | mute |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 22 |  |  | F1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 23 |  |  | F2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 24 |  |  | F3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 25 |  |  | F4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 26 |  |  | F5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 27 |  |  | vendor unique |  |  | [1] 4.1.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one item.
Prerequisite: AVRCP 2/9 “Sending PASS THROUGH command in category 3”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 0 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 2 |  |  | 1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 3 |  |  | 2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 4 |  |  | 3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 5 |  |  | 4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 6 |  |  | 5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 7 |  |  | 6 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 8 |  |  | 7 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 9 |  |  | 8 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 10 |  |  | 9 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 11 |  |  | dot |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 12 |  |  | enter |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 13 |  |  | clear |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 14 |  |  | channel up |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 15 |  |  | channel down |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 16 |  |  | previous channel |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 17 |  |  | sound select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 18 |  |  | input select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 19 |  |  | display information |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 20 |  |  | help |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 21 |  |  | power |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 22 |  |  | angle |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 23 |  |  | subpicture |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 24 |  |  | F1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 25 |  |  | F2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 26 |  |  | F3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 27 |  |  | F4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 28 |  |  | F5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 29 |  |  | vendor unique |  |  | [1] 4.1.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one item.
Table 6: operation_id of category 4 for CT
Prerequisite: AVRCP 2/10 “Sending PASS THROUGH command in category 4”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | select |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 2 |  |  | up |  |  | [1] 4.1.3 |  |  | C.1 |  |  |


|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | down |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 4 |  |  | left |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 5 |  |  | right |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 6 |  |  | right-up |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 7 |  |  | right-down |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 8 |  |  | left-up |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 9 |  |  | left-down |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 10 |  |  | root menu |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 11 |  |  | setup menu |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 12 |  |  | contents menu |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 13 |  |  | favorite menu |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 14 |  |  | exit |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 15 |  |  | 0 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 16 |  |  | 1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 17 |  |  | 2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 18 |  |  | 3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 19 |  |  | 4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 20 |  |  | 5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 21 |  |  | 6 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 22 |  |  | 7 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 23 |  |  | 8 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 24 |  |  | 9 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 25 |  |  | dot |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 26 |  |  | enter |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 27 |  |  | clear |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 28 |  |  | display information |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 29 |  |  | help |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 30 |  |  | page up |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 31 |  |  | page down |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 32 |  |  | power |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 33 |  |  | F1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 34 |  |  | F2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 35 |  |  | F3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 36 |  |  | F4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 37 |  |  | F5 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 38 |  |  | vendor unique |  |  | [1] 4.1.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one item.

### 2.5 Target features

Table 7: Target Features
Prerequisite: AVRCP 1/2 “Target”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Initiating connection establishment for control |  |  | [1] 4.1.1 |  |  | O |  |  |
| 2 |  |  | Accepting connection establishment for control initiated by CT |  |  | [1] 4.1.1 |  |  | M |  |  |
| 3 |  |  | Initiating connection release for control |  |  | [1] 4.1.2 |  |  | M |  |  |
| 4 |  |  | Accepting connection release for control initiated by CT |  |  | [1] 4.1.2 |  |  | M |  |  |
| 5 |  |  | Receiving UNIT INFO command |  |  | [1] 4.1.3 |  |  | M |  |  |
| 6 |  |  | Receiving SUBUNIT INFO command |  |  | [1] 4.1.3 |  |  | M |  |  |
| 7 |  |  | Receiving PASS THROUGH command in category 1 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 8 |  |  | Receiving PASS THROUGH command in category 2 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 9 |  |  | Receiving PASS THROUGH command in category 3 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 10 |  |  | Receiving PASS THROUGH command in category 4 |  |  | [1] 4.1.3 |  |  | C.1 |  |  |
| 11 |  |  | Get Capabilities Response |  |  | [1] 6.4.1 |  |  | C.3 |  |  |
| 12 |  |  | List Player Application Settings Attributes Response |  |  | [1] 6.5.1 |  |  | C.14 |  |  |
| 13 |  |  | List Player Application Setting Values Response |  |  | [1] 6.5.2 |  |  | C.14 |  |  |
| 14 |  |  | Get Current Player Application Settings Value Response |  |  | [1] 6.5.3 |  |  | C.14 |  |  |
| 15 |  |  | Set Player Application Setting Value Response |  |  | [1] 6.5.4 |  |  | C.14 |  |  |
| 16 |  |  | Get Player Application Setting Attribute Text Response |  |  | [1] 6.5.5 |  |  | O |  |  |
| 17 |  |  | Get Player Application Setting Value Text Response |  |  | [1] 6.5.6 |  |  | O |  |  |
| 18 |  |  | Inform Displayable Character Set Response |  |  | [1] 6.5.7 |  |  | O |  |  |
| 19 |  |  | Inform Battery Status of CT Response |  |  | [1] 6.5.8 |  |  | O |  |  |
| 20 |  |  | Get Element Attributes Response |  |  | [1] 6.6.1 |  |  | C.3 |  |  |
| 21 |  |  | Get Play Status Response |  |  | [1] 6.7.1 |  |  | C.2 |  |  |
| 22 |  |  | Register Notification Response |  |  | [1] 6.7.2 |  |  | C.12 |  |  |
| 23 |  |  | Notify Event Response: PLAYBACK STATUS CHANGED _ _ |  |  | [1] 6.7.2 |  |  | C.4 |  |  |
| 24 |  |  | Notify Event Response: TRACK CHANGED _ |  |  | [1] 6.7.2 |  |  | C.4 |  |  |
| 25 |  |  | Notify Event Response: TRACK REACHED END _ _ |  |  | [1] 6.7.2 |  |  | O |  |  |
| 26 |  |  | Notify Event Response: TRACK REACHED START _ _ |  |  | [1] 6.7.2 |  |  | O |  |  |
| 27 |  |  | Notify Event Response: PLAYBACK POS CHANGED _ _ |  |  | [1] 6.7.2 |  |  | O |  |  |
| 28 |  |  | Notify Event Response: BATT STATUS CHANGED _ _ |  |  | [1] 6.7.2 |  |  | O |  |  |
| 29 |  |  | Notify Event Response: SYSTEM STATUS CHANGED _ _ |  |  | [1] 6.7.2 |  |  | O |  |  |
| 30 |  |  | Notify Event Response: PLAYER APPLICATION SETTING CHANGED _ _ _ |  |  | [1] 6.7.2 |  |  | O |  |  |
| 31 |  |  | Request Continuing Response |  |  | [1] 6.8.1 |  |  | C.2 |  |  |
| 32 |  |  | Abort Continuing Response |  |  | [1] 6.8.2 |  |  | C.2 |  |  |
| 33 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 34 |  |  | Next Group |  |  | [1] 6.14.1 |  |  | C.15 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 35 |  |  | Previous Group |  |  | [1] 6.14.2 |  |  | C.15 |  |  |
| 36 |  |  | Media Player Selection |  |  | [1] 6.9 |  |  | C.8 |  |  |
| 37 |  |  | SetAddressedPlayer |  |  | [1] 6.9.1 |  |  | C.8 |  |  |
| 38 |  |  | GetFolderItems(MediaPlayerList) |  |  | [1] 6.10.4.2 |  |  | C.8 |  |  |
| 38b |  |  | GetTotalNumberOfItems(MediaPlayerList) |  |  | [3] 6.10.4.4 |  |  | C.20 |  |  |
| 39 |  |  | EVENT AVAILABLE PLAYERS CHANGED _ _ _ |  |  | [1] 6.9.4 |  |  | C.8 |  |  |
| 40 |  |  | EVENT ADDRESSED PLAYER CHANGED _ _ _ |  |  | [1] 6.9.2 |  |  | C.8 |  |  |
| 41 |  |  | Supports Multiple Players |  |  | [1] 6.9 |  |  | O |  |  |
| 42 |  |  | Browsing |  |  | [1] 6.10 |  |  | O |  |  |
| 42a |  |  | Initiating connection establishment for browsing channel |  |  | [1] 4.1.1 |  |  | O |  |  |
| 43 |  |  | SetBrowsedPlayer |  |  | [1] 6.9.3 |  |  | C.6 |  |  |
| 43a |  |  | Non-addressed Player Browsing |  |  | [1] 6.9.3 |  |  | C.17 |  |  |
| 44 |  |  | ChangePath |  |  | [1] 6.10.4.1 |  |  | C.6 |  |  |
| 45 |  |  | GetFolderItems(Filesystem) |  |  | [1] 6.10.4.2 |  |  | C.6 |  |  |
| 45b |  |  | GetTotalNumberOfItems(Filesystem) |  |  | [3] 6.10.4.4 |  |  | C.19 |  |  |
| 46 |  |  | GetItemAttributes |  |  | [1] 6.10.4.3 |  |  | C.6 |  |  |
| 47 |  |  | PlayItem(Filesystem) |  |  | [1] 6.12.1 |  |  | C.6 |  |  |
| 48 |  |  | EVENT UIDS CHANGED _ _ |  |  | [1] 6.10.3.3 |  |  | C.9 |  |  |
| 49 |  |  | Database Aware Players |  |  | [1] 6.10.3.2 |  |  | O |  |  |
| 50 |  |  | Searching |  |  | [1] 6.11 |  |  | O |  |  |
| 51 |  |  | Search |  |  | [1] 6.11 |  |  | C.10 |  |  |
| 52 |  |  | GetFolderItems(Search Results) |  |  | [1] 6.10.4.2 |  |  | C.10 |  |  |
| 52b |  |  | GetTotalNumberOfItems(SearchResults) |  |  | [3] 6.10.4.4 |  |  | C.21 |  |  |
| 53 |  |  | PlayItem(SearchResultList) |  |  | [1] 6.12.1 |  |  | C.10 |  |  |
| 54 |  |  | NowPlaying |  |  | [1] 6.10.1 |  |  | C.11 |  |  |
| 55 |  |  | GetFolderItems(NowPlayingList) |  |  | [1] 6.10.4.2 |  |  | C.11 |  |  |
| 55b |  |  | GetTotalNumberOfItems(NowPlayingList) |  |  | [3] 6.10.4.4 |  |  | C.22 |  |  |
| 56 |  |  | PlayItem(NowPlayingList) |  |  | [1] 6.12.1 |  |  | C.11 |  |  |
| 57 |  |  | AddToNowPlaying |  |  | [1] 6.12.2 |  |  | O |  |  |
| 58 |  |  | EVENT NOW PLAYING CONTENT CHANGED _ _ _ _ |  |  | [1] 6.9.5 |  |  | C.11 |  |  |
| 59 |  |  | Playable Folders |  |  | [1] 6.10.2.2 |  |  | O |  |  |
| 60 |  |  | Absolute Volume |  |  | [1] 6.13 |  |  | C.5 |  |  |
| 61 |  |  | SetAbsoluteVolume |  |  | [1] 6.13.2 |  |  | C.5 |  |  |
| 62 |  |  | NotifyVolumeChange |  |  | [1] 6.13.3 |  |  | C.5 |  |  |
| 63 |  |  | Error Response |  |  | [1] 6.15 |  |  | O |  |  |
| 64 |  |  | General Reject |  |  | [1] 6.15.2.1 |  |  | C.13 |  |  |
| 65 |  |  | Discoverable Mode |  |  | [1] 12.1 |  |  | M |  |  |
| 66 |  |  | PASSTHROUGH operation supporting Press and Hold |  |  | [1] 4.1.3 |  |  | O |  |  |
| 67 |  |  | Cover Art |  |  | [3] 5.14 |  |  | C.18 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 68 |  |  | GetImageProperties |  |  | [3] 5.14 |  |  | C.16 |  |  |
| 69 |  |  | GetImage |  |  | [3] 5.14 |  |  | C.16 |  |  |
| 70 |  |  | GetLinkedThumbnail |  |  | [3] 5.14 |  |  | C.16 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF AVRCP 7/20 “Get Element Attributes Response”, otherwise Optional.
C.3: Mandatory IF AVRCP 7/7 “Receiving PASS THROUGH command in category 1”, otherwise Optional.
C.4: Mandatory IF AVRCP 7/22 “Register Notification Response” AND AVRCP 7/20 “Get Element Attributes Response”, otherwise Optional.
C.5: Mandatory IF AVRCP 7/8 “Receiving PASS THROUGH command in category 2”, otherwise Excluded.
C.6: Mandatory IF AVRCP 7/42 “Browsing”, otherwise Excluded.
C.7: No longer used.
C.8: Mandatory IF AVRCP 7/7 “Receiving PASS THROUGH command in category 1” OR AVRCP 7/9 “Receiving PASS THROUGH command in category 3”, otherwise Excluded.
C.9: Mandatory IF AVRCP 7/49 “Database Aware Players”, otherwise Optional.
C.10: Mandatory IF AVRCP 7/50 “Searching”, otherwise Excluded.
C.11: Mandatory IF AVRCP 7/42 “Browsing”, otherwise Optional.
C.12: Mandatory IF AVRCP 7/7 “Receiving PASS THROUGH command in category 1” OR (AVRCP 7/8 “Receiving PASS THROUGH command in category 2” AND AVRCP 7/60 “Absolute Volume”) OR AVRCP 7/9 “Receiving PASS THROUGH command in category 3”, otherwise Optional.
C.13: Mandatory IF AVRCP 7/7 “Receiving PASS THROUGH command in category 1” OR AVRCP 7/9 “Receiving PASS THROUGH command in category 3” OR AVRCP 7/42 “Browsing”, otherwise Optional.
C.14: Mandatory to support none or all.
C.15: Mandatory to support none or all.
C.16: Excluded IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Mandatory IF AVRCP 7/67 “Cover Art”, otherwise Excluded.
C.17: Optional IF AVRCP 7/42 “Browsing”, otherwise Excluded.
C.18: Excluded IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Optional.
C.19: Excluded IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Mandatory IF AVRCP 7/42 “Browsing”, otherwise Excluded.
C.20: Excluded IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Mandatory IF AVRCP 7/7 “Receiving PASS THROUGH command in category 1” OR AVRCP 7/9 “Receiving PASS THROUGH command in category 3”, otherwise Excluded.
C.21: Excluded IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Mandatory IF AVRCP 7/50 “Searching”, otherwise Excluded.
C.22: Excluded IF AVRCP 7b/4 “AVRCP v1.5”, otherwise Mandatory IF AVRCP 7/42 “Browsing”, otherwise Optional.
Prerequisite: AVRCP 7/7 “Receiving PASS THROUGH command in category 1”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 0 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 2 |  |  | 1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 3 |  |  | 2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 4 |  |  | 3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 5 |  |  | 4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 6 |  |  | 5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 7 |  |  | 6 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 8 |  |  | 7 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 9 |  |  | 8 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 10 |  |  | 9 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 11 |  |  | Dot |  |  | [1] 4.1.3 |  |  | O |  |  |
| 12 |  |  | Enter |  |  | [1] 4.1.3 |  |  | O |  |  |
| 13 |  |  | Clear |  |  | [1] 4.1.3 |  |  | O |  |  |
| 14 |  |  | Sound select |  |  | [1] 4.1.3 |  |  | O |  |  |
| 15 |  |  | Input select |  |  | [1] 4.1.3 |  |  | O |  |  |
| 16 |  |  | Display information |  |  | [1] 4.1.3 |  |  | O |  |  |
| 17 |  |  | Help |  |  | [1] 4.1.3 |  |  | O |  |  |
| 18 |  |  | Power |  |  | [1] 4.1.3 |  |  | O |  |  |
| 19 |  |  | Play |  |  | [1] 4.1.3 |  |  | M |  |  |
| 20 |  |  | Stop |  |  | [1] 4.1.3 |  |  | M |  |  |
| 21 |  |  | Pause |  |  | [1] 4.1.3 |  |  | O |  |  |
| 22 |  |  | Record |  |  | [1] 4.1.3 |  |  | O |  |  |
| 23 |  |  | Rewind |  |  | [1] 4.1.3 |  |  | O |  |  |
| 24 |  |  | Fast forward |  |  | [1] 4.1.3 |  |  | O |  |  |
| 25 |  |  | Eject |  |  | [1] 4.1.3 |  |  | O |  |  |
| 26 |  |  | Forward |  |  | [1] 4.1.3 |  |  | O |  |  |
| 27 |  |  | Backward |  |  | [1] 4.1.3 |  |  | O |  |  |
| 28 |  |  | Angle |  |  | [1] 4.1.3 |  |  | O |  |  |
| 29 |  |  | Subpicture |  |  | [1] 4.1.3 |  |  | O |  |  |
| 30 |  |  | F1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 31 |  |  | F2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 32 |  |  | F3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 33 |  |  | F4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 33a |  |  | F5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 34 |  |  | Vendor unique |  |  | [1] 4.1.3 |  |  | O |  |  |

Prerequisite: AVRCP 7/8 “Receiving PASS THROUGH command in category 2”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 0 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 2 |  |  | 1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 3 |  |  | 2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 4 |  |  | 3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 5 |  |  | 4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 6 |  |  | 5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 7 |  |  | 6 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 8 |  |  | 7 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 9 |  |  | 8 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 10 |  |  | 9 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 11 |  |  | Dot |  |  | [1] 4.1.3 |  |  | O |  |  |
| 12 |  |  | Enter |  |  | [1] 4.1.3 |  |  | O |  |  |
| 13 |  |  | Clear |  |  | [1] 4.1.3 |  |  | O |  |  |
| 14 |  |  | Sound select |  |  | [1] 4.1.3 |  |  | O |  |  |
| 15 |  |  | Input select |  |  | [1] 4.1.3 |  |  | O |  |  |
| 16 |  |  | Display information |  |  | [1] 4.1.3 |  |  | O |  |  |
| 17 |  |  | Help |  |  | [1] 4.1.3 |  |  | O |  |  |
| 18 |  |  | Power |  |  | [1] 4.1.3 |  |  | O |  |  |
| 19 |  |  | Volume up |  |  | [1] 4.1.3 |  |  | M |  |  |
| 20 |  |  | Volume down |  |  | [1] 4.1.3 |  |  | M |  |  |
| 21 |  |  | Mute |  |  | [1] 4.1.3 |  |  | O |  |  |
| 22 |  |  | F1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 23 |  |  | F2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 24 |  |  | F3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 25 |  |  | F4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 26 |  |  | F5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 27 |  |  | Vendor unique |  |  | [1] 4.1.3 |  |  | O |  |  |

Prerequisite: AVRCP 7/9 “Receiving PASS THROUGH command in category 3”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 0 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 2 |  |  | 1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 3 |  |  | 2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 4 |  |  | 3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 5 |  |  | 4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 6 |  |  | 5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 7 |  |  | 6 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 8 |  |  | 7 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 9 |  |  | 8 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 10 |  |  | 9 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 11 |  |  | Dot |  |  | [1] 4.1.3 |  |  | O |  |  |
| 12 |  |  | Enter |  |  | [1] 4.1.3 |  |  | O |  |  |
| 13 |  |  | Clear |  |  | [1] 4.1.3 |  |  | O |  |  |
| 14 |  |  | Channel up |  |  | [1] 4.1.3 |  |  | M |  |  |
| 15 |  |  | Channel down |  |  | [1] 4.1.3 |  |  | M |  |  |
| 16 |  |  | Previous channel |  |  | [1] 4.1.3 |  |  | O |  |  |
| 17 |  |  | Sound select |  |  | [1] 4.1.3 |  |  | O |  |  |
| 18 |  |  | Input select |  |  | [1] 4.1.3 |  |  | O |  |  |
| 19 |  |  | Display information |  |  | [1] 4.1.3 |  |  | O |  |  |
| 20 |  |  | Help |  |  | [1] 4.1.3 |  |  | O |  |  |
| 21 |  |  | Power |  |  | [1] 4.1.3 |  |  | O |  |  |
| 21a |  |  | Angle |  |  | [1] 4.1.3 |  |  | O |  |  |
| 21b |  |  | Subpicture |  |  | [1] 4.1.3 |  |  | O |  |  |
| 22 |  |  | F1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 23 |  |  | F2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 24 |  |  | F3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 25 |  |  | F4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 25a |  |  | F5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 26 |  |  | Vendor unique |  |  | [1] 4.1.3 |  |  | O |  |  |

Prerequisite: AVRCP 7/10 “Receiving PASS THROUGH command in category 4”

|  | Item |  |  | Operation id _ |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Select |  |  | [1] 4.1.3 |  |  | M |  |  |
| 2 |  |  | Up |  |  | [1] 4.1.3 |  |  | M |  |  |
| 3 |  |  | Down |  |  | [1] 4.1.3 |  |  | M |  |  |
| 4 |  |  | Left |  |  | [1] 4.1.3 |  |  | M |  |  |
| 5 |  |  | Right |  |  | [1] 4.1.3 |  |  | M |  |  |
| 6 |  |  | Right-up |  |  | [1] 4.1.3 |  |  | O |  |  |
| 7 |  |  | Right-down |  |  | [1] 4.1.3 |  |  | O |  |  |
| 8 |  |  | Left-up |  |  | [1] 4.1.3 |  |  | O |  |  |
| 9 |  |  | Left-down |  |  | [1] 4.1.3 |  |  | O |  |  |
| 10 |  |  | Root menu |  |  | [1] 4.1.3 |  |  | M |  |  |
| 11 |  |  | Setup menu |  |  | [1] 4.1.3 |  |  | O |  |  |
| 12 |  |  | Contents menu |  |  | [1] 4.1.3 |  |  | O |  |  |
| 13 |  |  | Favorite menu |  |  | [1] 4.1.3 |  |  | O |  |  |
| 14 |  |  | Exit |  |  | [1] 4.1.3 |  |  | O |  |  |
| 15 |  |  | 0 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 16 |  |  | 1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 17 |  |  | 2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 18 |  |  | 3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 19 |  |  | 4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 20 |  |  | 5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 21 |  |  | 6 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 22 |  |  | 7 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 23 |  |  | 8 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 24 |  |  | 9 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 25 |  |  | Dot |  |  | [1] 4.1.3 |  |  | O |  |  |
| 26 |  |  | Enter |  |  | [1] 4.1.3 |  |  | O |  |  |
| 27 |  |  | Clear |  |  | [1] 4.1.3 |  |  | O |  |  |
| 28 |  |  | Display information |  |  | [1] 4.1.3 |  |  | O |  |  |
| 29 |  |  | Help |  |  | [1] 4.1.3 |  |  | O |  |  |
| 30 |  |  | Page up |  |  | [1] 4.1.3 |  |  | O |  |  |
| 31 |  |  | Page down |  |  | [1] 4.1.3 |  |  | O |  |  |
| 32 |  |  | Power |  |  | [1] 4.1.3 |  |  | O |  |  |
| 33 |  |  | F1 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 34 |  |  | F2 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 35 |  |  | F3 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 36 |  |  | F4 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 36a |  |  | F5 |  |  | [1] 4.1.3 |  |  | O |  |  |
| 37 |  |  | Vendor unique |  |  | [1] 4.1.3 |  |  | O |  |  |


### 2.6 Requirements towards other profiles


#### 2.6.1 Requirements towards GAP

Table 12: Requirements towards the Generic Access Profile (CT)
Prerequisite: AVRCP 1/1 “Controller”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [1] 12.1 | M | [2] GAP 1/3 |  |  |

Table 13: Requirements towards the Generic Access Profile (TG)
Prerequisite: AVRCP 1/2 “Target”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [1] 12.1 | M | [2] GAP 1/3 |  |  |


#### 2.6.2 Requirements towards GOEP

Table 14: OBEX Operations (AVRCP CT, OBEX Client)
Prerequisite: AVRCP 1/1 “Controller”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | OBEX Connect operation |  |  | [4] 5.1 |  |  | C.1 |  |  |
| 2 |  |  | OBEX Get operation |  |  | [4] 5.1 |  |  | C.1 |  |  |
| 3 |  |  | OBEX Disconnect operation |  |  | [4] 5.1 |  |  | C.1 |  |  |

C.1: Mandatory IF AVRCP 2/54 “Cover Art”, otherwise Excluded.
Table 15: OBEX Operations (AVRCP TG, OBEX Server)
Prerequisite: AVRCP 1/2 “Target”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | OBEX Connect operation |  |  | [4] 5.1 |  |  | C.1 |  |  |
| 2 |  |  | OBEX Get operation |  |  | [4] 5.1 |  |  | C.1 |  |  |
| 3 |  |  | OBEX Disconnect operation |  |  | [4] 5.1 |  |  | C.1 |  |  |

C.1: Mandatory IF AVRCP 7/67 “Cover Art”, otherwise Excluded.

## 3 References

[1] Audio/Video Remote Control Profile (AVRCP) Specification, Version 1.5 or later
[2] ICS Proforma for Generic Access Profile (GAP)
[3] Audio/Video Remote Control Profile (AVRCP) Specification, Version 1.6 or later
[4] Generic Object Exchange Profile (GOEP) Specification, Version 2.0 or later
[5] Audio/Video Remote Control Profile (AVRCP) Specification, Version 1.5.1
[6] Audio/Video Remote Control Profile (AVRCP) Specification, Version 1.6.2
[7] Audio/Video Remote Control Profile (AVRCP) Specification, Version 1.6.3

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | Version 1.0 |  |  | 2003-05 | Update title and header |
| 1 |  |  | 1.2.0 |  |  | 2006-02-02 | Editorial updates for conformance to template and 1.2 spec |
| 2 |  |  | 1.2.1 |  |  | 2007-03-22 | Add Metadata Transfer Change version number to match spec version number |
| 3 |  |  | 1.2.2 |  |  | 2007-08-24 | TSE 2103: Exchange tables 9 and 10 row data, add 5F to CT and TG tables |
|  |  |  | 1.3.3r0 |  |  | 2008-02 | Renamed document to match updated TCRL. Correct version number is 1.3. TSE 2375: Table 2 and Table 7 changes TSE 2376: Addition to Table 7 TSE 2383: Table 7, add C.4 Added prerequisites to match TPG |
| 4 |  |  | 1.3.3 |  |  | 2008-04 | Prepare for publication. |
|  |  |  | 1.4.0r1 |  |  | 2008-06-30 | Removed C6 from Table 2 and C7 from Table 7 |
| 5 |  |  | 1.4.0 |  |  | 2008-06 | Advanced Control update: Add line item to Table 0 |
|  |  |  | 1.4.0a |  |  | 2009-01 | Editorial: Add pre-reqs to Table 2, Table 7 for v1.4 and later. |
|  |  |  | 1.4.0b |  |  | 2009-05-12 | TSE 2950: Fix radio buttons in Table 2 and Table 3 |
|  |  |  | 1.4.1r0 |  |  | 2011-01 | TSE 3861: Update Table 7, footnote C.3 TSE 3366: Add Tables 12 and 13 |
| 6 |  |  | 1.4.1 |  |  | 2011-07-21 | Prepare for publication. |
|  |  |  | 1.4.2r0 |  |  | 2011-09-22 | TSE 4408: Delete Table 0. Add Table 2b and Table 7b. TSE 4499: Update Table 2 and Table 7 per TSE 2706 |
|  |  |  | 1.4.2r1 |  |  | 2011-10-25 | Revisions by AC per MS comments of 25 Oct 2011. |
|  |  |  | 1.6.0r1 |  |  | 2012-02-28 | Added NumberOfItems and Cover Art to 1.4.2 baseline |
| 7 |  |  | 1.4.2 |  |  | 2012-03-30 | Prepare for publication. |
|  |  |  | 1.6.0r2 |  |  | 2012-04-23 | Updated 1.6.0r1. Added list of AVRCP 1.6 items to Table 2 and 7 Prerequisite. Corrected AVRCP 1.6 Status in Table 2b and 7b. |
|  |  |  | 1.6.0r3 |  |  | 2012-05-08 | Updated 1.6.0r2. Contributors reordered alphabetically by company Adjusted NumberOfItems and Cover Art Item numbers in Table 2 and 7 Added scopes to NumberOfItems feature descriptions in Table 2 and 7 |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.5.0r0 |  |  | 2012-06-21 | Updated 1.4.2. Updated references for AVRCP 1.5. Added appropriate ICS items to Tables 2b and 7b. Changed O.1 status in Table 1 to C.1 since it is mandatory to support at least one item. Updated references in Tables 2 and 7 to correctly reference sections in different AVRCP versions. Added section header and reformatted tables for GAP requirements. |
| 8 |  |  | 1.5.0 |  |  | 2012-07-24 | Prepare for publication. |
|  |  |  | 1.5.1r0 |  |  | 2012-08-30 | TSE 4531: Added a new ICS item to Table 7 (7/42a) for initiation of browsing channel establishment. TSE 4962: Changes to match the intent of the ESR06 specification. Added conditionals to 1.4 and 1.5. |
|  |  |  | 1.5.1r1 |  |  | 2012-10-23 | Editorial changes. Incorporated latest additional changes suggested to TSE 4531. |
| 9 |  |  | 1.5.1 |  |  | 2012-11-01 | Prepare for Publication |
|  |  |  | 1.6.0r4 |  |  | 2013-06-17 | Updates for Cover Art and Number of Items added to version 1.5.1 baseline. |
|  |  |  | 1.6.0r5 |  |  | 2013-09-18 | Moved to new document template and associated formats and default language. Implemented TSE 5148. Clarified section references for Number of Items feature in Tables 2 and 7. Corrected section references for Absolute Volume messages in Tables 2 and 7. Added missing AVRCP 1.6 reference hyperlinks in Tables 2 and 7. |
|  |  |  | 1.6.0r6 |  |  | 2014-09-02 | TSE 5377 – Update to Table 2 Conditional C.2 to align with Specification Erratum 5376 |
| 10 |  |  | 1.6.0 |  |  | 2014-09-18 | Adopted by the BoD |
|  |  |  | 1.6.1r00 |  |  | 2015-04-28 | TSE 6300: Fixed broken reference in Section 1.2. Updated copyright/disclaimer and header/sidebar to current standards. |
|  |  |  | 1.6.1r02 |  |  | 2015-06-05 | Deleted Section 1.2 (Global Statement of Conformance) per current ICS template standards. |
| 11 |  |  | 1.6.1 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 1.6.1.0r00 |  |  | 2015-10-28 | Updated version numbering to align with Specification version change from 1.6 to 1.6.1 for ESR09. With the specification taking a third identifying number, the ICS version identifier moves to the fourth number and starts again at 0. |
|  |  |  | 1.6.1.0r01 |  |  | 2015-11-03 | Added items 2b/6 and 7b/6 for support of AVRCP 1.6.1 (ESR09). |
|  |  |  | 1.6.1.0r03 |  |  | 2015-11-24 | Added Tables 2c and 7c for minor version support. |
| 12 |  |  | 1.6.1.0 |  |  | 2015-12-22 | Prepared for TCRL 2015-2 publication |
|  |  |  | 1.6.1.1r00 |  |  | 2016-02-29 | TSE 6425: Added Item 43a, Non-addressed Player Browsing, to Table 7. Added conditional status C.17 to Table 7 legend. |
| 13 |  |  | 1.6.1.1 |  |  | 2016-07-13 | Prepared for TCRL 2016-1 publication. |
|  |  |  | 1.6.1.2r00 |  |  | 2018-04-06 | TSE 10586 (rating 1): Template Conversion. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 14 |  |  | 1.6.1.2 |  |  | 2018-07-01 | Approved by BTI. Prepared for TCRL 2018-1 publication. |
|  |  |  | 1.6.1.3r00 |  |  | 2018-09-24 | Drafted Deprecation/Withdrawal changes |
|  |  |  | 1.6.2.0r00 |  |  | 2018-11-09 | Updated version number to 1.6.2.0 to align with adoption of the specification 1.6.2. Added items 2c/2 and 7c/7 for the new spec version. |
| 15 |  |  | 1.6.2.0 |  |  | 2018-11-21 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | 1.6.2.0 ed2r00 |  |  | 2020-03-25 – 2020-03-26 | TSE 14644 (rating 1): Revised to fix issue with Consistency Check fail. Also updated template-related items (DMR, etc.) and made other minor editorials. |
|  |  |  | 1.6.2.0 edition 2 |  |  | 2020-06-01 | Performed minor formatting and template updates (including adding Inter-Layer Dependency column to Tables 12 and 13), rolled back document numbering to reflect an edition release, and accepted all tracked changes. Approved by BTI on 2020-06-01. Prepared for edition 2 publication. |
|  |  |  | 1.6.2.0 ed3r00 |  |  | 2021-01-12 | TSE 15976 (rating 1): Changes for deprecation. |
|  |  |  | 1.6.2.0 edition 3 |  |  | 2021-02-01 | Approved by BTI on 2021-01-15. Prepared for edition 3 publication. |
|  |  |  | 1.6.2.0ed4 r00–r02 |  |  | 2021-03-15 – 2021-04-26 | TSE 16680 (rating 2): Split Table 0 into Table 0a and Table 0b. Minor editorials from consistency checker findings. |
|  |  |  | 1.6.2.0 edition 4 |  |  | 2021-05-24 | Approved by BTI on 2021-05-06. Prepared for edition 4 publication. |
|  |  |  | 1.6.2.0ed5 r00–r01 |  |  | 2021-07-15 – 2021-08-12 | TSE 16975 (rating 1): Editorial updates to Table 2 and Table 7 conditionals. Minor template-related editorials. |
|  |  |  | 1.6.2.0 edition 5 |  |  | 2021-08-19 | Approved by BTI on 2021-08-19. Prepared for edition 5 publication. |
|  |  |  | 1.6.2.0ed6 r00–r01 |  |  | 2021-08-26 – 2021-09-24 | TSE 17324 (rating 1): Minor editorials to item numbering and/or descriptions in Tables 8, 9, 10, and 11 to align with Launch Studio. Consistency checker editorials to align with the wording in the latest ICS template. |
|  |  |  | 1.6.2.0 edition 6 |  |  | 2021-09-28 | Approved by BTI on 2021-09-27. Prepared for edition 6 publication. |
|  |  |  | 1.6.2.0ed7r00 |  |  | 2021-10-14 | TSE 17681 (rating 1): Updated deprecation and withdrawal information. |
|  |  |  | 1.6.2.0 edition 7 |  |  | 2021-11-22 | Approved by BTI on 2021-11-08. Prepared for edition 7 publication. |
|  |  |  | 1.6.2.0ed8 r00–r01 |  |  | 2022-02-16 – 2022-03-07 | TSE 18287 (rating 1): Updated C.1 – C.3 for Tables 0a and 0b. Editorials, including template-related formatting fixes, aligning the copyright page with v2 of the DNMD, and consistency checker fixes. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.6.2.0, edition 8 |  |  | 2022-03-07 | Approved by BTI on 2022-03-07. Prepared for edition 8 publication. |
|  |  |  | 1.6.2.0ed9r00 –r01 |  |  | 2022-04-04 – 2022-04-21 | TSE 18546 (rating 1): Updated the versions tables (Tables 0a, 2b, 0b, and 7b) to account for deprecation and withdrawal, renaming the section to “Versions” and moving the Major and Minor Versions tables for the Controller and Target there from later in the document (Tables 2b, 2c, 7b, and 7c); added D&W dates for AVRCP v1.0 in Tables 2b and 7b and updated conditionals accordingly; added a “Roles” heading before Table 1; modified the intro paragraph for the “Controller features” and “Target features” sections; adjusted the content of the Major Version Prerequisite column in Tables 2 and 7 and added a References column to Tables 3–6 and 8–11. |
|  |  |  | 1.6.2.0 edition 9 |  |  | 2022-04-25 | Approved by BTI on 2022-04-25. Prepared for edition 2 publication. |
|  |  |  | 1.6.2.0ed10 r00–r05 |  |  | 2023-02-07 – 2023-02-23 | TSE 22623 (rating 1): Replaced Major/Minor with X.Y(.Z) in the titles of Tables 0a, 0b, 2b, 7b, and 7c. Adjusted the Withdrawal date from February 2023 to February 2024 for AVRCP v1.6 and 1.6.1. In Tables 0a and 0b, removed items as no longer needed after evaluating the remaining active specification versions. Updated references. Editorials to align the document with the latest ICS template. |
|  |  |  | 1.6.2.0 edition 10 |  |  | 2023-02-27 | Approved by BTI on 2023-02-23. Prepared for edition 10 publication. |
|  |  |  | p16r00–r02 |  |  | 2023-03-20 – 2023-05-25 | TSE 22865 (rating 2): Removed Tables 0a and 0b because they are no longer used. Deleted the introductory text in Sections 1.4 and 1.5. In Table 2, removed the “Major Version Prerequisite” column; updated statuses in Items 29b, 35b, 41b, 44b, and 54; updated C.13 and C.14; and added C.15. In Table 7, removed the “Major Version Prerequisite” column; updated statuses in Items 38b, 45b, 52b, 55b, and 67; updated C.16; and added C.18–C.22. |
| 16 |  |  | p16 |  |  | 2023-06-29 | Approved by BTI on 2023-05-28. Prepared for TCRL 2023-1 publication. |
|  |  |  | p17r00 |  |  | 2024-04-24 | TSE 25114 (rating 1): Updated the withdrawal date for AVRCP v1.3 in Tables 2b and 7b. |
| 17 |  |  | p17 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p18r00–r01 |  |  | 2024-08-14 – 2024-08-26 | TSE 25563 (rating 1): Per E10214, E15773, E15828, E18309, E18310, E18396, E18543, E18790, E23562, E23746, and E23747, accounted for AVRCP v1.5.1 and AVRCP v1.6.3. In Table 2c, added Items 2c/3 and 2c/4 and conditional C.2. In Table 7c, added Items 7c/8 and 7c/9 and conditional C.2. Updated conditional C.1 for Tables 2c and 7c. Updated the references list. Made editorial updates to align the document with the latest ICS template. |
| 18 |  |  | p18 |  |  | 2024-10-08 | Approved by BTI on 2024-09-11. Audio/Video Remote Control Profile (AVRCP) Specification Versions 1.5.1 and 1.6.3 adopted by the BoD on 2024-10-01. Prepared for TCRL 2024-2-addition publication. |
|  |  |  | p19r00 |  |  | 2025-02-24 | TSE 26844 (rating 2): Updated conditional C.2 for Tables 2b and 7b. Added “Core Configuration” section and Table 0c. Applied the current ICS template. |
| 19 |  |  | p19 |  |  | 2025-07-08 | Approved by BTI on 2025-05-30. Prepared for TCRL pkg100 publication. |
|  |  |  | p20r00 |  |  | 2025-12-05 – 2026-01-06 | TSE 28346 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |
| 20 |  |  | p20 |  |  | 2026-02-17 | Approved by BTI on 2026-01-22. Prepared for TCRL pkg102 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Mat Davidson |  |  | Apple |  |  |
| Rüdiger Mosig |  |  | Berner & Mattner |  |  |
| Dominik Sollfrank |  |  | Berner & Mattner |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
| Ash Kapur |  |  | Broadcom |  |  |
| Jiny Bradshaw |  |  | CSR |  |  |
| Gordon Downie |  |  | CSR |  |  |
| David Trainor |  |  | CSR |  |  |
| Miyajima Akira |  |  | Denso |  |  |
| Morgan Lindqvist |  |  | Ericsson |  |  |
| Masahiko Nakashima |  |  | Fujitsu |  |  |
| Ilya Goldberg |  |  | Matsushita |  |  |
| Tsuyoshi Okada |  |  | Matsushita |  |  |
| Thomas Karlsson |  |  | Mecel |  |  |
| Ross Bundy |  |  | Motorola |  |  |
| Thomas Block |  |  | Nokia |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Brian Gix |  |  | Open Interface |  |  |
| François Ferrand |  |  | Parrot |  |  |
| Sébastien Henrio |  |  | Parrot |  |  |
| Christian Bouffioux |  |  | Philips |  |  |
| Laurent Meunier |  |  | Philips |  |  |
| Scott Walsh |  |  | Plantronics |  |  |
| Dimitri Toropov |  |  | Siemens |  |  |
| Wilhelm Hagg |  |  | Sony |  |  |
| Masakazu Hattori |  |  | Sony |  |  |
| Atsushi Ichise |  |  | Sony |  |  |
| Harumi Kawamura |  |  | Sony |  |  |
| Yoshiyuki Nezu |  |  | Sony |  |  |
| Hiroyasu Noguchi |  |  | Sony |  |  |
| Masahiko Seki |  |  | Sony |  |  |
| Dick deJong |  |  | Sony Ericsson |  |  |
| Patric Lind |  |  | Sony Ericsson |  |  |
| Siân James |  |  | Symbian |  |  |
| Makoto Kobayashi |  |  | Toshiba |  |  |
| Yoshinari Kumaki |  |  | Toshiba |  |  |
| Shuichi Sakurai |  |  | Toshiba |  |  |
| Ichiro Tomoda |  |  | Toshiba |  |  |
| Makoto Yamashita |  |  | Toshiba |  |  |
