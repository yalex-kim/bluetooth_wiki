# MAP.ICS.p14

> Source: PDF converted via PyMuPDF.

---

Message Access Profile (MAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: MAP.ICS.p14 ▪ Revision Date: 2026-02-17 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.pkg102
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2008–2026 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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

Table 0: X.Y Versions

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | MAP v1.0** |  |  | [1] v1.0 |  |  | Deprecated 2015-07-16. Withdrawn 2023-02-01. |  |  |
| 2 |  |  | MAP v1.1** |  |  | [2] v1.1 |  |  | Deprecated 2023-02-01. Withdrawn 2024-02-01. |  |  |
| 3 |  |  | MAP v1.2** |  |  | [7] v1.2 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 5 |  |  | MAP v1.3 |  |  | [8] v1.3 |  |  | C.1, C.2 |  |  |
| 6 |  |  | MAP v1.4 |  |  | [9] v1.4 |  |  | C.1, C.2 |  |  |

C.1: Mandatory to support one and only one. C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 0a: X.Y.Z Versions

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | MAP v1.2.1** |  |  | [7] v1.2.1 |  |  | Deprecated 2021-02-01. Withdrawn 2024-02-01. |  |  |
| 2 |  |  | MAP v1.2.2** |  |  | [7] v1.2.2 |  |  | Deprecated 2023-02-01. Withdrawn 2024-02-01. |  |  |
| 3 |  |  | MAP v1.3.1 |  |  | [8] v1.3.1 |  |  | C.2 |  |  |
| 3a |  |  | MAP v1.3.2 |  |  | [8] v1.3.2 |  |  | C.2 |  |  |
| 4 |  |  | MAP v1.4.1** |  |  | [9] v1.4.1 |  |  | Deprecated 2019-11-20. Withdrawn 2024-02-01. |  |  |
| 5 |  |  | MAP v1.4.2 |  |  | [9] v1.4.2 |  |  | C.3 |  |  |
| 6 |  |  | MAP v1.4.3 |  |  | [9] v1.4.3 |  |  | C.3 |  |  |

C.1: No longer used. C.2: Mandatory to support one and only one IF MAP 0/5 “MAP v1.3”, otherwise Excluded. C.3: Mandatory to support one and only one IF MAP 0/6 “MAP v1.4”, otherwise Excluded.

### 2.2 Core Configuration

Table 0b: Core Configuration Requirements

|  | Item |  |  | Core Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 1.4 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 1.4 |  |  | C.2 |  |  |

** Deprecated versions may not appear in the Bluetooth SIG qualification tool after the deprecation date. TCRLs published after this date will not allow the use of deprecated versions.
C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”. C.2: Excluded for this Profile. C.3: Mandatory for this Profile.

### 2.3 Roles

Table 1: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Messaging Server Equipment |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 2 |  |  | Messaging Client Equipment |  |  | [1] 2.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 2.4 Message Client Equipment (MCE)


#### 2.4.1 Features

Table 2: Supported features MCE
Prerequisite: MAP 1/2 “Messaging Client Equipment”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Notification |  |  | [1] 4.1 |  |  | C.1 |  |  |
| 1a |  |  | SendEvent |  |  | [1] 4.1 |  |  | C.4 |  |  |
| 1b |  |  | SetNotificationFilter |  |  | [8] 4.1 |  |  | C.11 |  |  |
| 2 |  |  | Browsing |  |  | [1] 4.2 |  |  | C.1 |  |  |
| 2a |  |  | SetFolder |  |  | [1] 4.2 |  |  | C.5 |  |  |
| 2b |  |  | GetFolderListing |  |  | [1] 4.2 |  |  | C.5 |  |  |
| 2c |  |  | GetMessagesListing |  |  | [1] 4.2 |  |  | C.5 |  |  |
| 2d |  |  | GetMessage |  |  | [1] 4.2 |  |  | O |  |  |
| 2e |  |  | SetMessageStatus |  |  | [1] 4.2 |  |  | O |  |  |
| 2f |  |  | UpdateInbox |  |  | [1] 4.2 |  |  | O |  |  |
| 2g |  |  | Filtering |  |  | [1] 5.5 |  |  | O |  |  |
| 2h |  |  | Multiple Simultaneous MAS Instances |  |  | [1] 3.1.8 |  |  | O |  |  |
| 2i |  |  | GetConversationListing |  |  | [8] 4.2 |  |  | C.18 |  |  |
| 3 |  |  | Uploading |  |  | [1] 4.3 |  |  | O |  |  |
| 3a |  |  | SetFolder |  |  | [1] 4.3 |  |  | C.6 |  |  |
| 3b |  |  | GetFoldersListing |  |  | [1] 4.3 |  |  | C.6 |  |  |
| 3c |  |  | PushMessage |  |  | [1] 4.3, [9] 4.3, 4.7 |  |  | C.20 |  |  |
| 3d |  |  | SetOwnerStatus |  |  | [8] 4.3 |  |  | C.15 |  |  |
| 3e |  |  | GetOwnerStatus |  |  | [8] 4.3 |  |  | C.15 |  |  |
| 4 |  |  | Delete |  |  | [1] 4.4 |  |  | O |  |  |
| 4a |  |  | SetMessageStatus |  |  | [1] 4.4 |  |  | C.7 |  |  |
| 5 |  |  | Notification Registration |  |  | [1] 4.5 |  |  | C.2 |  |  |
| 5a |  |  | SetNotificationRegistration off |  |  | [1] 4.5 |  |  | O |  |  |
| 5b |  |  | SetNotificationRegistration on |  |  | [1] 4.5 |  |  | C.8 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Supported Message Types |  |  |  |  |  |  |  |  |
| 6 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 6a |  |  | EMAIL |  |  | [1] 2.4 |  |  | C.3 |  |  |
| 6b |  |  | SMS GSM _ |  |  | [1] 2.4 |  |  | C.3 |  |  |
| 6c |  |  | SMS CDMA _ |  |  | [1] 2.4 |  |  | C.3 |  |  |
| 6d |  |  | MMS |  |  | [1] 2.4 |  |  | C.3 |  |  |
| 6e |  |  | IM |  |  | [8] 2.3 |  |  | C.12 |  |  |
| 7 |  |  | Instance Information |  |  | [7] 4.6 |  |  | O |  |  |
| 7a |  |  | GetMASInstanceInformation |  |  | [7] 4.6 |  |  | O |  |  |
| 8 |  |  | Extended MAP-Event-Report |  |  | [7] 3.1.7.2 |  |  | C.4 |  |  |
| 8a |  |  | MAP-Event-Report: Version 1.1 |  |  | [7] 3.1.7.2 |  |  | C.4 |  |  |
| 8b |  |  | MAP-Event-Report: Version 1.2 |  |  | [8] 3.1.7.3 |  |  | C.21 |  |  |
|  |  |  | Message format Version |  |  |  |  |  |  |  |  |
| 9 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 9a |  |  | Message format Version 1.0 |  |  | [1] 3.1.3 |  |  | M |  |  |
| 9b |  |  | Message format Version 1.1 |  |  | [8] 3.1.3.1 |  |  | O |  |  |
|  |  |  | Messages-Listing Object Version |  |  |  |  |  |  |  |  |
| 10 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 10a |  |  | Messages-Listing Object Version 1.0 |  |  | [1] 3.1.6 |  |  | M |  |  |
| 10b |  |  | Messages-Listing Format Version 1.1 |  |  | [8] 3.1.6.1 |  |  | M |  |  |
| 11 |  |  | Persistent Message Handles |  |  | [8] 4 |  |  | O |  |  |
| 12 |  |  | Database Identifier |  |  | [8] 3.1.14 |  |  | C.17 |  |  |
|  |  |  | Version Counters |  |  |  |  |  |  |  |  |
| 13 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 13a |  |  | Folder Version Counter |  |  | [8] 3.1.15 |  |  | O |  |  |
| 13b |  |  | Conversation Version Counters |  |  | [8] 3.1.15 |  |  | C.14 |  |  |
| 13c |  |  | Conversation-Listing Version Counter |  |  | [8] 3.1.15 |  |  | C.14 |  |  |
| 14 |  |  | Participant Presence Change Notification |  |  | [8] 4 |  |  | O |  |  |
| 15 |  |  | Participant Chat State Change Notification |  |  | [8] 4 |  |  | O |  |  |
| 16 |  |  | PBAP Contact Cross Reference |  |  | [8] 3.1.9 |  |  | O |  |  |
| 17 |  |  | Notification Filtering |  |  | [8] 4 |  |  | O |  |  |
| 18 |  |  | UTC Offset Timestamp Format |  |  | [8] 3.1.10 |  |  | O |  |  |
| 19 |  |  | Conversation listing |  |  | [8] 4 |  |  | O |  |  |
| 20 |  |  | Owner status |  |  | [8] 4 |  |  | O |  |  |
| 21 |  |  | Message Forwarding |  |  | [9] 4.7 |  |  | C.19 |  |  |

C.1: Mandatory to support at least one. C.2: Mandatory IF MAP 2/1 “Notification”, otherwise Optional. C.3: Mandatory to support at least one IF MAP 2/2 “Browsing” OR MAP 2/3 “Uploading”, otherwise Optional. C.4: Mandatory IF MAP 2/1 “Notification”, otherwise Excluded. C.5: Mandatory IF MAP 2/2 “Browsing”, otherwise Excluded.
C.6: Mandatory IF MAP 2/3 “Uploading”, otherwise Excluded. C.7: Mandatory IF MAP 2/4 “Delete”, otherwise Excluded. C.8: Mandatory IF MAP 2/5 “Notification Registration”, otherwise Excluded. C.9–C.10: No longer used. C.11: Mandatory IF MAP 2/17 “Notification Filtering”, otherwise Excluded. C.12: Optional IF MAP 2/9b “Message format Version 1.1”, otherwise Excluded. C.13: No longer used. C.14: Optional IF MAP 2/19 “Conversation listing”, otherwise Excluded. C.15: Mandatory IF MAP 2/20 “Owner status”, otherwise Excluded. C.16: No longer used. C.17: Mandatory IF MAP 2/11 “Persistent Message Handles” OR MAP 2/13a “Folder Version Counter”, otherwise Optional. C.18: Mandatory IF MAP 2/19 “Conversation listing”, otherwise Excluded. C.19: Excluded IF MAP 0/5 “MAP v1.3”, otherwise Optional. C.20: Mandatory IF MAP 2/3 “Uploading” OR MAP 2/21 “Message Forwarding”, otherwise Excluded. C.21: Mandatory IF MAP 2/14 “Participant Presence Change Notification” OR MAP 2/15 “Participant Chat State Change Notification”, otherwise Optional.

### 2.5 Message Server Equipment (MSE)


#### 2.5.1 Features

Table 3: Supported features MSE
Prerequisite: MAP 1/1 “Messaging Server Equipment”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Notification |  |  | [1] 4.1 |  |  | M |  |  |
| 1a |  |  | SendEvent |  |  | [1] 4.1 |  |  | M |  |  |
| 1b |  |  | SetNotificationFilter |  |  | [8] 4.1 |  |  | M |  |  |
| 2 |  |  | Browsing |  |  | [1] 4.2 |  |  | M |  |  |
| 2a |  |  | SetFolder |  |  | [1] 4.2 |  |  | M |  |  |
| 2b |  |  | GetFoldersListing |  |  | [1] 4.2 |  |  | M |  |  |
| 2c |  |  | GetMessagesListing |  |  | [1] 4.2 |  |  | M |  |  |
| 2d |  |  | GetMessage |  |  | [1] 4.2 |  |  | M |  |  |
| 2e |  |  | SetMessageStatus |  |  | [1] 4.2 |  |  | M |  |  |
| 2f |  |  | UpdateInbox |  |  | [1] 4.2 |  |  | M |  |  |
| 2g |  |  | Multiple Simultaneous MAS Instances |  |  | [1] 3.1.8 |  |  | O |  |  |
| 2h |  |  | GetConversationListing |  |  | [8] 4.2 |  |  | C.9 |  |  |
| 3 |  |  | Uploading |  |  | [1] 4.3 |  |  | M |  |  |
| 3a |  |  | SetFolder |  |  | [1] 4.3 |  |  | M |  |  |
| 3b |  |  | GetFoldersListing |  |  | [1] 4.3 |  |  | M |  |  |
| 3c |  |  | PushMessage |  |  | [1] 4.3 |  |  | M |  |  |
| 3d |  |  | SetOwnerStatus |  |  | [8] 4.3 |  |  | C.7 |  |  |
| 3e |  |  | GetOwnerStatus |  |  | [8] 4.3 |  |  | C.7 |  |  |
| 4 |  |  | Delete |  |  | [1] 4.4 |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4a |  |  | SetMessageStatus |  |  | [1] 4.4 |  |  | M |  |  |
| 5 |  |  | Notification Registration |  |  | [1] 4.5 |  |  | M |  |  |
| 5a |  |  | SetNotificationRegistration |  |  | [1] 4.5 |  |  | M |  |  |
|  |  |  | Supported Message Types |  |  |  |  |  |  |  |  |
| 6 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 6a |  |  | EMAIL |  |  | [1] 2.4 |  |  | C.1 |  |  |
| 6b |  |  | SMS GSM _ |  |  | [1] 2.4 |  |  | C.1 |  |  |
| 6c |  |  | SMS CDMA _ |  |  | [1] 2.4 |  |  | C.1 |  |  |
| 6d |  |  | MMS |  |  | [1] 2.4 |  |  | C.1 |  |  |
| 6e |  |  | IM |  |  | [8] 2.4 |  |  | O |  |  |
| 7 |  |  | Instance Information |  |  | [7] 4.6 |  |  | M |  |  |
| 7a |  |  | GetMASInstanceInformation |  |  | [7] 4.6 |  |  | M |  |  |
| 8 |  |  | Extended MAP-Event-Report |  |  | [7] 3.1.7.2 |  |  | M |  |  |
| 8a |  |  | MAP-Event-Report: Version 1.1 |  |  | [7] 3.1.7.2 |  |  | M |  |  |
| 8b |  |  | MAP-Event-Report: Version 1.2 |  |  | [8] 3.1.7.3 |  |  | C.12 |  |  |
|  |  |  | Message format Version |  |  |  |  |  |  |  |  |
| 9 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 9a |  |  | Message format Version 1.0 |  |  | [1] 3.1.3 |  |  | M |  |  |
| 9b |  |  | Message format Version 1.1 |  |  | [8] 3.1.3.1 |  |  | M |  |  |
|  |  |  | Messages-Listing Object Version |  |  |  |  |  |  |  |  |
| 10 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 10a |  |  | Messages-Listing Object Version 1.0 |  |  | [1] 3.1.6 |  |  | M |  |  |
| 10b |  |  | Messages-Listing Format Version 1.1 |  |  | [8] 3.1.6.1 |  |  | M |  |  |
| 11 |  |  | Persistent Message Handles |  |  | [8] 4 |  |  | O |  |  |
| 12 |  |  | Database Identifier |  |  | [8] 3.1.14 |  |  | C.8 |  |  |
|  |  |  | Version Counters |  |  |  |  |  |  |  |  |
| 13 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 13a |  |  | Folder Version Counter |  |  | [8] 3.1.15 |  |  | O |  |  |
| 13b |  |  | Conversation Version Counters |  |  | [8] 3.1.15 |  |  | C.10 |  |  |
| 13c |  |  | Conversation-Listing Version Counter |  |  | [8] 3.1.15 |  |  | C.10 |  |  |
| 14 |  |  | Participant Presence Change Notification |  |  | [8] 4 |  |  | O |  |  |
| 15 |  |  | Participant Chat State Change Notification |  |  | [8] 4 |  |  | O |  |  |
| 16 |  |  | PBAP Contact Cross Reference |  |  | [8] 3.1.9 |  |  | O |  |  |
| 17 |  |  | Notification Filtering |  |  | [8] 4 |  |  | M |  |  |
| 18 |  |  | UTC Offset Timestamp Format |  |  | [8] 3.1.10 |  |  | M |  |  |
| 19 |  |  | Conversation listing |  |  | [8] 4 |  |  | O |  |  |
| 20 |  |  | Owner status |  |  | [8] 4 |  |  | O |  |  |
| 21 |  |  | Message Forwarding |  |  | [9] 4.7 |  |  | C.11 |  |  |

C.1: Mandatory to support at least one. C.2–C.6: No longer used. C.7: Mandatory IF MAP 3/20 “Owner status”, otherwise Excluded.
C.8: Mandatory IF MAP 3/11 “Persistent Message Handles” OR MAP 3/13a “Folder Version Counter”, otherwise Excluded. C.9: Mandatory IF MAP 3/19 “Conversation listing”, otherwise Excluded. C.10: Optional IF MAP 3/19 “Conversation listing”, otherwise Excluded. C.11: Excluded IF MAP 0/5 “MAP v1.3”, otherwise Optional. C.12: Mandatory IF MAP 3/14 “Participant Presence Change Notification” OR MAP 3/15 “Participant Chat State Change Notification”, otherwise Optional.

### 2.6 Requirements toward other Bluetooth profiles


#### 2.6.1 GAP requirements

Table 4: GAP Modes requirements for the MCE
Prerequisite: MAP 1/2 “Messaging Client Equipment”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [9] 8.1 | M | [6] GAP 1/3 |  |  |
| 2 | Bondable mode | [9] 8.1 | M | [6] GAP 1/7 |  |  |

Table 5: GAP Idle Mode requirements for the MCE
Prerequisite: MAP 1/2 “Messaging Client Equipment”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initiation of general inquiry | [9] 8.3 | O | [6] GAP 3/1 |  |  |
| 2 | Initiation of limited inquiry | [9] 8.3 | O | [6] GAP 3/2 |  |  |

Table 6: GAP Modes requirements for the MSE
Prerequisite: MAP 1/1 “Messaging Server Equipment”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | General discoverable mode | [9] 8.1 | M | [6] GAP 1/3 |  |  |
| 2 | Bondable mode | [9] 8.1 | M | [6] GAP 1/7 |  |  |

Table 7: GAP Idle Mode requirements for the MSE
Prerequisite: MAP 2/2 “Browsing”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Initiation of general inquiry | [9] 8.3 | M | [6] GAP 3/1 |  |  |
| 2 | Initiation of limited inquiry | [9] 8.3 | O | [6] GAP 3/2 |  |  |
| 3 | Initiation of general bonding | [9] 2.4 | M | [6] GAP 3/5 |  |  |


#### 2.6.2 GOEP requirements

Table 7b: GOEP v2.0 or later Features

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | GOEP v2.0 or later |  |  | [4] |  |  | M |  |  |
| 2 |  |  | GOEP v2.0 or later Backwards Compatibility |  |  | [4] 6.2 |  |  | M |  |  |
| 3 |  |  | OBEX over L2CAP |  |  | IrDA Interoperability |  |  | M |  |  |


#### 2.6.3 OBEX – Message Client Equipment (MCE)

Table 8: MCE OBEX Functions support for MAS
Prerequisite: MAP 1/2 “Messaging Client Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connect (Client) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 2 |  |  | Disconnect (Client) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 3 |  |  | Put (Client) |  |  | [1] 6.2, [5] |  |  | C.1 |  |  |
| 4 |  |  | Get (Client) |  |  | [1] 6.2, [5] |  |  | C.2 |  |  |
| 5 |  |  | Abort (Client) |  |  | [1] 6.2, [5] |  |  | C.3 |  |  |
| 6 |  |  | SetPath (Client) |  |  | [1] 6.2, [5] |  |  | C.4 |  |  |

C.1: Mandatory IF MAP 2/2e “SetMessageStatus” OR MAP 2/2f “UpdateInbox” OR MAP 2/3c “PushMessage” OR MAP 2/4a “SetMessageStatus” OR MAP 2/5a “SetNotificationRegistration off”, otherwise Optional. C.2: Mandatory IF MAP 2/2b “GetFolderListing” OR MAP 2/2c “GetMessagesListing” OR MAP 2/2d “GetMessage” OR MAP 2/3b “GetFoldersListing” OR MAP 2/7a “GetMASInstanceInformation”, otherwise Optional. C.3: Mandatory IF MAP 8/3 “Put (Client)” OR MAP 8/4 “Get (Client)”, otherwise Optional. C.4: Mandatory IF MAP 2/2a “SetFolder” OR MAP 2/3a “SetFolder”, otherwise Optional.
Table 9: MCE OBEX Functions support for MNS
Prerequisite: MAP 1/2 “Messaging Client Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connect (Server) |  |  | [1] 6.2, [5] |  |  | C.1 |  |  |
| 2 |  |  | Disconnect (Server) |  |  | [1] 6.2, [5] |  |  | C.1 |  |  |
| 3 |  |  | Put (Server) |  |  | [1] 6.2, [5] |  |  | C.1 |  |  |
| 4 |  |  | Abort (Server) |  |  | [1] 6.2, [5] |  |  | C.1 |  |  |

C.1: Mandatory IF MAP 2/1 “Notification”, otherwise Optional.
Table 10: MCE OBEX Header support
Prerequisite: MAP 1/2 “Messaging Client Equipment”

|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Name |  |  | [1] 6.3, [5] |  |  | M |  |  |


|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 |  |  | Type |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 3 |  |  | Body |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 4 |  |  | End of Body |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 5 |  |  | Target |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 6 |  |  | Who |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 7 |  |  | Connection ID |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 8 |  |  | Application Parameters |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 9 |  |  | SRM |  |  | [7] 6.3, [4] 5.2 |  |  | M |  |  |
| 10 |  |  | Receive SRMP |  |  | [7] 6.3, [4] 5.2 |  |  | M |  |  |
| 11 |  |  | Send SRMP |  |  | [7] 6.3, [4] 5.2 |  |  | O |  |  |

Table 11: MCE OBEX Client Error Codes Recognition
Prerequisite: MAP 1/2 “Messaging Client Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bad Request |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 2 |  |  | Not Implemented |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 3 |  |  | Unauthorized |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 4 |  |  | Precondition Failed |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 5 |  |  | Not Found |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 6 |  |  | Not Acceptable |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 7 |  |  | Service Unavailable |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 8 |  |  | Forbidden |  |  | [1] 6.3, [5] |  |  | M |  |  |

Table 12: MCE OBEX Server Error Codes Recognition
Prerequisite: MAP 1/2 “Messaging Client Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bad Request |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 2 |  |  | Not Implemented |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 3 |  |  | Unauthorized |  |  | [1] 6.3, [5] |  |  | O |  |  |
| 4 |  |  | Precondition Failed |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 5 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 6 |  |  | Not Acceptable |  |  | [1] 6.3, [5] |  |  | O |  |  |
| 7 |  |  | Service Unavailable |  |  | [1] 6.3, [5] |  |  | O |  |  |
| 8 |  |  | Forbidden |  |  | [1] 6.3, [5] |  |  | O |  |  |


#### 2.6.4 OBEX – Message Server Equipment (MSE)

Table 13: MSE OBEX Functions support for MAS
Prerequisite: MAP 1/1 “Messaging Server Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connect (Server) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 2 |  |  | Disconnect (Server) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 3 |  |  | Put (Server) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 4 |  |  | Get (Server) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 5 |  |  | Abort (Server) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 6 |  |  | SetPath (Server) |  |  | [1] 6.2, [5] |  |  | M |  |  |

Table 14: MSE OBEX Functions support for MNS
Prerequisite: MAP 1/1 “Messaging Server Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Connect (Client) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 2 |  |  | Disconnect (Client) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 3 |  |  | Put (Client) |  |  | [1] 6.2, [5] |  |  | M |  |  |
| 4 |  |  | Abort (Client) |  |  | [1] 6.2, [5] |  |  | M |  |  |

Table 15: MSE OBEX Header support
Prerequisite: MAP 1/1 “Messaging Server Equipment”

|  | Item |  |  | OBEX Header |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Name |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 2 |  |  | Type |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 3 |  |  | Body |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 4 |  |  | End of Body |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 5 |  |  | Target |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 6 |  |  | Who |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 7 |  |  | Connection ID |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 8 |  |  | Application Parameters |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 9 |  |  | SRM |  |  | [7] 6.3, [4] 5.2 |  |  | M |  |  |
| 10 |  |  | Receive SRMP |  |  | [7] 6.3, [4] 5.2 |  |  | M |  |  |
| 11 |  |  | Send SRMP |  |  | [7] 6.3, [4] 5.2 |  |  | O |  |  |

Table 16: MSE OBEX Client Error Codes Recognition
Prerequisite: MAP 1/1 “Messaging Server Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bad Request |  |  | [1] 6.3, [5] |  |  | M |  |  |


|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 |  |  | Not Implemented |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 3 |  |  | Unauthorized |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 4 |  |  | Precondition Failed |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 5 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 6 |  |  | Not Acceptable |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 7 |  |  | Service Unavailable |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 8 |  |  | Forbidden |  |  | [1] 6.3, [5] |  |  | M |  |  |

Table 17: MSE OBEX Server Error Codes Reporting
Prerequisite: MAP 1/1 “Messaging Server Equipment”

|  | Item |  |  | OBEX Operation |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Bad Request |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 2 |  |  | Not Implemented |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 3 |  |  | Unauthorized |  |  | [1] 6.3, [5] |  |  | O |  |  |
| 4 |  |  | Precondition Failed |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 5 |  |  | Not Found |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 6 |  |  | Not Acceptable |  |  | [1] 6.3, [5] |  |  | O |  |  |
| 7 |  |  | Service Unavailable |  |  | [1] 6.3, [5] |  |  | M |  |  |
| 8 |  |  | Forbidden |  |  | [1] 6.3, [5] |  |  | O |  |  |


#### 2.6.5 SDP requirements

Table 18: SDP Attributes MCE
Prerequisite: MAP 1/2 “Messaging Client Equipment”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | ProtocolDescriptorList | [9] 7.1.2 | M | [3] SDP 9/2 |  |  |
| 2 | BluetoothProfileDescriptorList | [9] 7.1.2 | M | [3] SDP 9/14 |  |  |
| 3 | ServiceName | [9] 7.1.2 | M | [3] SDP 9/9 |  |  |

Table 19: SDP Attributes MSE
Prerequisite: MAP 1/1 “Messaging Server Equipment”

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | ProtocolDescriptorList | [9] 7.1.1 | M | [3] SDP 9/2 |  |  |
| 2 | BluetoothProfileDescriptorList | [9] 7.1.1 | M | [3] SDP 9/14 |  |  |
| 3 | ServiceName | [9] 7.1.1 | M | [3] SDP 9/9 |  |  |


### 2.7 MCE Filtering Parameter Support

Table 20: GetMessagesListing Filtering Parameter Support
Prerequisite: MAP 2/2c "GetMessagesListing" AND MAP 2/2g "Filtering"

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | FilterMessageType |  |  | [1] 5.5 |  |  | O |  |  |
| 2 |  |  | FilterPeriodBegin |  |  | [1] 5.5 |  |  | O |  |  |
| 3 |  |  | FilterPeriodEnd |  |  | [1] 5.5 |  |  | O |  |  |
| 4 |  |  | FilterReadStatus |  |  | [1] 5.5 |  |  | O |  |  |
| 5 |  |  | FilterRecipient |  |  | [1] 5.5 |  |  | O |  |  |
| 6 |  |  | FilterOriginator |  |  | [1] 5.5 |  |  | O |  |  |
| 7 |  |  | FilterPriority |  |  | [1] 5.5 |  |  | O |  |  |
| 8 |  |  | ConversationID |  |  | [8] 5.5 |  |  | C.1 |  |  |
| 9 |  |  | FilterMessageHandle |  |  | [1] 5.5 |  |  | O |  |  |

C.1: Optional IF MAP 2/6e “IM”, otherwise Excluded.

## 3 References

[1] Message Access Profile, Version 1.0 or later
[2] Message Access Profile, Version 1.1 or later
[3] ICS Proforma for Service Discovery Protocol (SDP)
[4] Generic Object Exchange Profile, Version 2.0 or later
[5] IrOBEX Specification, Version 1.5
[6] ICS Proforma for Generic Access Profile (GAP)
[7] Message Access Profile, Version 1.2 or later
[8] Message Access Profile, Version 1.3 or later
[9] Message Access Profile, Version 1.4 or later

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  | 0 |  |  | 1.0.0 |  |  | 2009-05-12 |  |  | Prepare for publication. |  |
|  |  |  | 1.0.1r0 | 1.0.1r0 |  | 2010-09-03 | 2010-09-03 |  |  | TSE 3331: Add Table 20 for parameter support |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3389: Table 16; change title from Server to Client |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3954: Add 5.1.1 and 5.1.2 for TP/MNR/BV-01,02- |  |
|  |  |  |  |  |  |  |  |  |  | I |  |
|  | 1 |  |  | 1.0.1 |  |  | 2011-07-21 |  |  | Prepare for publication. |  |
|  |  |  | 1.0.2r0 | 1.0.2r0 |  | 2012-05-18 | 2012-05-18 |  |  | TSE 4102: Added Table 2/2g and updated Table 20 |  |
|  |  |  |  |  |  |  |  |  |  | prerequisite |  |
|  | 2 |  |  | 1.0.2 |  |  | 2012-07-24 |  |  | Prepare for Publication |  |
|  |  |  |  | 1.1.0r0 |  |  | 2013-01-02 |  |  | Added Version Table 0. |  |
|  |  |  | 1.1.0r1 | 1.1.0r1 |  | 2013-01-09 | 2013-01-09 |  |  | Reformatted dates in Change History. |  |
|  |  |  |  |  |  |  |  |  |  | Fixed conditional in Table 2 item 5b from TSE 3954 |  |
|  |  |  |  |  |  |  |  |  |  | Fixed numbering in tables 4-7 and 18-19 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5055: Removed item 5 “Not Found” from Tables |  |
|  |  |  |  |  |  |  |  |  |  | 12 and 16. Changed Conditional for Table 12 item 7 |  |
|  |  |  |  |  |  |  |  |  |  | “Service Unavailable” |  |
|  |  |  | 1.1.0r2 |  |  | 2013-03-28 |  |  |  | TSE 5066: Removed tables 20 and 21, added to |  |
|  |  |  |  |  |  |  |  |  |  | existing MAP Tables 2 and 3. Item 2h to Table 2 and |  |
|  |  |  |  |  |  |  |  |  |  | Item 2g to Table 3. |  |
|  |  |  | 1.2.0r0 |  |  | 2013-05-16 |  |  |  | Incorporated MAPII ICS CR 09r08 changes and Fort |  |
|  |  |  |  |  |  |  |  |  |  | Worth F2F Comment resolutions |  |
|  |  |  |  | 1.2.0r1 |  |  | 2013-06-10 |  |  | Approved in BTI. |  |
|  | 3 |  |  | 1.2.0 |  |  | 2013-07-16 |  |  | Prepare for Publication |  |
|  |  |  |  | 1.2.1.0r00 |  |  | 2015-05-20 |  |  | ESR08: Added item 4 to Table 0 for MAP 1.2.1 |  |
|  |  |  | 1.2.1.0r01 | 1.2.1.0r01 |  | 2015-06-05 | 2015-06-05 |  |  | Deleted Section 1.2 (Global Statement of |  |
|  |  |  |  |  |  |  |  |  |  | Conformance) per current ICS template standards. |  |
|  |  |  |  | 1.2.1.0r02 |  |  | 2015-06-10 |  |  | Converted to current document template. |  |
|  | 4 |  |  | 1.2.1.0 |  |  | 2015-07-14 |  |  | Prepared for TCRL 2015-1 publication |  |
|  |  |  | 1.2.2.0r00 | 1.2.2.0r00 |  | 2015-10-28 | 2015-10-28 |  |  | Updated version numbering to align with Specification |  |
|  |  |  |  |  |  |  |  |  |  | version change from to 1.2.2 for ESR09. |  |
|  |  |  | 1.2.2.0r01 |  |  | 2015-11-02 |  |  |  | Added item 0/5 for new Specification version 1.2.2 |  |
|  |  |  |  |  |  |  |  |  |  | (ESR09). |  |
|  |  |  | 1.2.2.0r02 |  |  | 2015-11-24 |  |  |  | Added Table 0a for minor profile versions and |  |
|  |  |  |  |  |  |  |  |  |  | updated conditionals accordingly throughout. |  |
|  | 5 |  |  | 1.2.2.0 |  |  | 2015-12-22 |  |  | Prepared for TCRL 2015-2 publication |  |
|  |  |  | 1.3.0r01 | 1.3.0r01 |  | 2015-12-08 | 2015-12-08 |  |  | Incorporated MAP 1.3 ICS for Instant Messaging |  |
|  |  |  |  |  |  |  |  |  |  | Feature Support. |  |
|  |  |  |  | 1.3.0r02 |  |  | 2016-02-01 |  |  | Addressing BTI comments |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 1.3.0r03 | 1.3.0r03 |  | 2016-03-18 |  |  |  | Addressing comments from Chris Church |  |
|  |  |  |  |  |  |  |  |  |  | Editorial update to Items 2/1, 2/2, 2/3, 2/4 |  |
|  |  |  |  |  |  |  |  |  |  | 2/1 was “Message Notification”, is now “Notification”, |  |
|  |  |  |  |  |  |  |  |  |  | 2/2 was “Message Browsing”, is now “Browsing”, 2/3 |  |
|  |  |  |  |  |  |  |  |  |  | was “Message Uploading”, is now “Uploading”, 2/4 |  |
|  |  |  |  |  |  |  |  |  |  | was “Message Delete”, is now “Delete”. |  |
|  |  |  |  |  |  |  |  |  |  | Editorial update to Items 3/1, 3/2, 3/3, 3/4 |  |
|  |  |  |  |  |  |  |  |  |  | 3/1 was “Message Notification”, is now “Notification”, |  |
|  |  |  |  |  |  |  |  |  |  | 3/2 was “Message Browsing”, is now “Browsing”, 3/3 |  |
|  |  |  |  |  |  |  |  |  |  | was “Message Uploading”, is now “Uploading”, 3/4 |  |
|  |  |  |  |  |  |  |  |  |  | was “Message Delete”, is now “Delete”. |  |
|  |  |  |  | 1.3.0r04 |  |  | 2016-04-04 |  |  | Accepted amendments from BTI |  |
|  |  |  |  | 1.3.0r05 |  |  | 2016-04-18 |  |  | Further BTI comment resolution |  |
|  |  |  |  | 1.3.0 |  |  | 2016-05-02 |  |  | Approved by BTI |  |
|  |  |  |  | 1.3.0 |  |  | 2016-05-17 |  |  | Specification v1.3 adopted by the Bluetooth SIG BoD |  |
|  | 6 |  |  | 1.3.0 |  |  | 2016-05-24 |  |  | Prepared for publication |  |
|  |  |  | 1.4.0r00 | 1.4.0r00 |  | 2016-05-11 | 2016-05-11 |  |  | Incorporate changes for Message Forwarding |  |
|  |  |  |  |  |  |  |  |  |  | enhancement |  |
|  |  |  |  |  |  |  |  |  |  | Added new version to Table 0. |  |
|  |  |  |  |  |  |  |  |  |  | Added new reference to MAP v1.4. |  |
|  |  |  |  |  |  |  |  |  |  | Added new ICS items 2/21 and 3/21. |  |
|  |  |  |  | 1.4.0r01 |  |  | 2016-05-23 |  |  | Addressed ATA WG internal comments |  |
|  |  |  |  | 1.4.0r02 |  |  | 2016-06-22 |  |  | Addressed BTI comments |  |
|  |  |  | 1.4.0r03 | 1.4.0r03 |  | 2017-03-27 | 2017-03-27 |  |  | Updated template. |  |
|  |  |  |  |  |  |  |  |  |  | Fixed the pre-requisite for Table 7. |  |
|  | 7 |  |  | 1.4.0 |  |  | 2017-05-21 |  |  | Approved by BTI. Prepared for publication. |  |
|  |  |  | 1.4.1r00-r01 | 1.4.1r00-r01 |  | 2018-10-04 | 2018-10-04 |  |  | TSE 10782 (rating 2): Updated conditionals for Table |  |
|  |  |  |  |  |  |  |  |  |  | 10 and 15. |  |
|  |  |  |  |  |  |  |  |  |  | Drafted deprecation/withdrawal changes: Updated |  |
|  |  |  |  |  |  |  |  |  |  | status for item 0/1 (MAP 1.0). |  |
|  |  |  | 1.4.1.0 |  |  | 2018-11-09 |  |  |  | Updated version number from 1.4.1 to 1.4.1.0 to align |  |
|  |  |  |  |  |  |  |  |  |  | with adoption of the specification version 1.4.1. Added |  |
|  |  |  |  |  |  |  |  |  |  | items 0a/3 and 0a/4 for new versions 1.3.1 and 1.4.1. |  |
| 8 |  |  | 1.4.1.0 |  |  | 2018-11-21 |  |  |  | Approved by BTI. Prepared for TCRL 2018-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.4.1.1 r00–r01 1.4.2.0 r00–r01 |  |  | 2019-04-02 – 2019-07-17 |  |  |  | TSE 11607 (rating 1): Revised conditionals C.1 and |  |
|  |  |  |  |  |  |  |  |  |  | C.2 of Table 15 that were incorrectly integrated from |  |
|  |  |  |  |  |  |  |  |  |  | TSE 10782. |  |
|  |  |  |  |  |  |  |  |  |  | Removed numbers from rows in Table 2 and Table 3 |  |
|  |  |  |  |  |  |  |  |  |  | that were intended to be descriptions of the items to |  |
|  |  |  |  |  |  |  |  |  |  | follow rather than ICS items for selection and |  |
|  |  |  |  |  |  |  |  |  |  | indicated that those items are no longer used. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 11918: Updated version number to 1.4.2.0 to |  |
|  |  |  |  |  |  |  |  |  |  | align with adoption of spec version 1.4.2. Added item |  |
|  |  |  |  |  |  |  |  |  |  | 0a/6 for the new spec version along with planned |  |
|  |  |  |  |  |  |  |  |  |  | deprecation and withdrawal dates for 1.4.1. |  |
| 9 |  |  | 1.4.2.0 |  |  | 2019-07-28 |  |  |  | Approved by BTI. Prepared for TCRL 2019-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  | 1.4.2.0 |  | 2021-01-05 |  | TSE 15983 (rating 1): Updated conditionals for |  |
|  |  |  |  | ed2r00 |  |  |  | deprecation. |  |
|  |  |  |  | 1.4.2.0 |  | 2021-02-01 |  | Approved by BTI on 2021-01-15. Prepared for edition |  |
|  |  |  |  | edition 2 |  |  |  | 2 publication. |  |
|  |  |  | p10r00–r02 | p10r00–r02 |  | 2021-04-05 – 2021-06-11 |  | TSE 15504 (rating 2): Updated Table 2 item 2/3c by |  |
|  |  |  |  |  |  |  |  | changing conditional and adding a reference, and by |  |
|  |  |  |  |  |  |  |  | adding new conditional C.20. |  |
|  |  |  |  |  |  |  |  | Template-related and consistency checker editorials, |  |
|  |  |  |  |  |  |  |  | including assigning p9 to previous v1.4.2.0. |  |
| 10 |  |  | p10 |  |  | 2021-07-13 |  | Approved by BTI on 2021-06-03. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2021-1 publication. |  |
|  |  |  | p10ed2 r00–r02 |  |  | 2021-07-23 – 2021-09-24 |  | TSE 17168 (rating 1): Corrected deprecation date for |  |
|  |  |  |  |  |  |  |  | MAP v1.0 in Table 0. |  |
|  |  |  |  |  |  |  |  | TSE 17286 (rating 1): Globally removed references to |  |
|  |  |  |  |  |  |  |  | deprecated MAP v1.0 (MAP 0/1) from conditionals. |  |
|  |  |  |  |  |  |  |  | Consistency checker editorials to align wording with |  |
|  |  |  |  |  |  |  |  | the latest ICS template. |  |
|  |  |  | p10 edition 2 |  |  | 2021-09-28 |  | Approved by BTI on 2021-09-27. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  | p10ed3r00 |  |  | 2021-10-18 |  | TSE 17685 (rating 1): Adjusted deprecation and |  |
|  |  |  |  |  |  |  |  | withdrawal dates and made other consistency checker |  |
|  |  |  |  |  |  |  |  | fixes. |  |
|  |  |  | p10 edition 3 |  |  | 2021-11-24 |  | Approved by BTI on 2021-11-08. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 3 publication. |  |
|  |  |  | p10ed4r00– r04 |  |  | 2023-02-07 – 2023-02-23 |  | TSE 22629 (rating 1): Updated to align with current |  |
|  |  |  |  |  |  |  |  | ICS conventions. Updated the Withdrawal date for |  |
|  |  |  |  |  |  |  |  | MAP 1.2, 1.2.1, 1.3, 1.4, 1.4.1 from 2023-02-01 to |  |
|  |  |  |  |  |  |  |  | 2024-02-01. Removed C.1 and C.2 from MAP 1.1 and |  |
|  |  |  |  |  |  |  |  | MAP 1.2 in Table 0 as they are both deprecated |  |
|  |  |  |  |  |  |  |  | without any associated active X.Y.Z versions. |  |
|  |  |  |  |  |  |  |  | Removed C.1 from MAP 1.2.2 and Table 0a since it is |  |
|  |  |  |  |  |  |  |  | past the deprecation date and no longer used. |  |
|  |  |  |  |  |  |  |  | Updates to conditionals to remove deprecated version |  |
|  |  |  |  |  |  |  |  | ICS references. |  |
|  |  |  |  |  |  |  |  | Deleted draft revision history comments prior to p0. |  |
|  |  |  | p10 edition 4 |  |  | 2023-02-27 |  | Approved by BTI on 2023-02-23. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 4 publication. |  |
|  |  |  | p11r00 |  |  | 2023-10-18 – 2023-10-23 |  | TSE 23941 (rating 1): Updated to align the document |  |
|  |  |  |  |  |  |  |  | with the latest ICS template, including updates to |  |
|  |  |  |  |  |  |  |  | section and table titles. Updated the references. In |  |
|  |  |  |  |  |  |  |  | Table 3, updated C.1. In Tables 4 and 6, deleted |  |
|  |  |  |  |  |  |  |  | heading rows. In Tables 10 and 15, updated the |  |
|  |  |  |  |  |  |  |  | Status value for Items 9–11 and deleted C.1 and C.2. |  |
| 11 |  |  | p11 |  |  | 2024-07-01 |  | Approved by BTI on 2024-05-22. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2024-1 publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p12r00–r02 | p12r00–r02 |  | 2024-10-14 – 2024-12-19 |  | TSE 22279 (rating 2): Per E22359, added C.21 to |  |
|  |  |  |  |  |  |  |  | Table 2 and C.12 to Table 3, and updated table |  |
|  |  |  |  |  |  |  |  | spacing to current guidelines. |  |
|  |  |  |  |  |  |  |  | TSE 26911 (rating 1): Per E11797, E23840, and |  |
|  |  |  |  |  |  |  |  | E23841, updated Table 0a to account for MAP v1.3.2 |  |
|  |  |  |  |  |  |  |  | and MAP v1.4.3 as part of the .Z release. Updated |  |
|  |  |  |  |  |  |  |  | C.2 of Table 0. |  |
| 12 |  |  | p12 |  |  | 2025-02-18 |  | Approved by BTI on 2024-12-25. MAP v1.4.3 and |  |
|  |  |  |  |  |  |  |  | v1.3.2 adopted by the BoD on 2024-02-11. Prepared |  |
|  |  |  |  |  |  |  |  | for TCRL 2025-1 publication. |  |
|  |  |  | p13r00 |  |  | 2025-02-27 |  | TSE 27009 (rating 2): Added “Core Configuration” |  |
|  |  |  |  |  |  |  |  | section and Table 0b. |  |
| 13 |  |  | p13 |  |  | 2025-07-08 |  | Approved by BTI on 2025-05-30. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | pkg100 publication. |  |
|  |  |  | p14r00 |  |  | 2025-12-05 – 2026-01-07 | TSE 28346 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |  |  |
| 14 |  |  | p14 |  |  | 2026-02-17 | Approved by BTI on 2026-01-22. Prepared for TCRL pkg102 publication. |  |  |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Joachim Mertz |  |  | Berner&Mattner |  |
|  | Rüdiger Mosig |  |  | Berner&Mattner |  |
|  | Olivia Bellamou-Huet |  |  | Berner & Mattner Systemtechnik GmbH |  |
|  | Dominik Sollfrank |  |  | Berner & Mattner Systemtechnik GmbH |  |
|  | Alicia Courtney |  |  | Broadcom |  |
|  | Burch Seymour |  |  | Continental Automotive Systems |  |
|  | Meshach Rajsingh |  |  | CSR |  |
|  | Kyle Penri-Williams |  |  | Parrot |  |
