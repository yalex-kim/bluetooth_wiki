# HID11.ICS.p16

> Source: PDF converted via PyMuPDF.

---

Human Interface Device Profile 1.1 or later (HID11)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: HID11.ICS.p16 ▪ Revision Date: 2026-02-17 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.pkg102
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

Table 0: X.Y Versions

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HID v1.1 |  |  | [1] |  |  | C.1, C.2 |  |  |

C.1: Mandatory.
C.2: Can only be supported with an active X.Y.Z version after Deprecation or Withdrawal. Deprecated 2021-02-01. Withdrawn 2024-02-01.
Table 0a: X.Y.Z Versions

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | HID v1.1.1 |  |  | [3] |  |  | C.1 |  |  |
| 2 |  |  | HID v1.1.2 |  |  | [4] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one.

### 2.2 Core Configuration

Table 0b: Core Configuration Requirements

|  | Item |  |  | Core Configuration |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Profile supported over BR/EDR |  |  | [1] 1.3 |  |  | C.1, C.3 |  |  |
| 2 |  |  | Profile supported over LE |  |  | [1] 1.3 |  |  | C.2 |  |  |

C.1: Excluded for this Profile IF CORE 41/2 “LE Core Configuration” OR CORE 40/1 “Core-Controller”.
C.2: Excluded for this Profile.
C.3: Mandatory for this Profile.

### 2.3 Roles

Table 1: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | General HID Host, Report protocol |  |  | [1] 2.1.2 |  |  | C.1, C.2 |  |  |
| 2 |  |  | Limited HID Host, Report protocol |  |  | [1] 2.1.2 |  |  | C.3, C.2 |  |  |
| 3 |  |  | Limited HID Host, Boot protocol |  |  | [1] 2.1.2 |  |  | C.2 |  |  |
| 4 |  |  | HID Device Role |  |  | [1] 2.1.2 |  |  | C.2 |  |  |

C.1: Excluded IF HID11 1/2 “Limited HID Host, Report protocol”, otherwise Optional.
C.2: Mandatory to support at least one.
C.3: Excluded IF HID11 1/1 “General HID Host, Report protocol”, otherwise Optional.

### 2.4 HID Host Role


#### 2.4.1 Application Procedures

Table 2: Application Procedures
Prerequisite: HID11 1/1 “General HID Host, Report protocol” OR HID11 1/2 “Limited HID Host, Report protocol” OR HID11 1/3 “Limited HID Host, Boot protocol”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Host initiated HID connection establishment |  |  | [1] 5.2.2 |  |  | C.1 |  |  |
| 2 |  |  | Device initiated HID connection establishment |  |  | [1] 5.2.2 |  |  | O |  |  |
| 3 |  |  | Terminate HID connection |  |  | [1] 5.2.2 |  |  | C.2 |  |  |
| 4 |  |  | Accept Termination of HID connection |  |  | [1] 5.2.2 |  |  | M |  |  |
| 5 |  |  | Support for virtual cables |  |  | [1] 4.5 |  |  | C.3 |  |  |
| 6 |  |  | Device initiated reconnection |  |  | [1] 5.4.2 |  |  | C.2 |  |  |
| 7 |  |  | Host initiated reconnection |  |  | [1] 5.4.2 |  |  | C.2 |  |  |
| 8 |  |  | Support for entering Suspend mode |  |  | [1] 3.1.2.2 |  |  | O |  |  |
| 9 |  |  | Support for exiting Suspend mode |  |  | [1] 3.1.2.2 |  |  | C.4 |  |  |
| 10 |  |  | Disconnect HID Devices when entering Suspend mode |  |  | [1] 3.1.2.2 |  |  | O |  |  |
| 11 |  |  | Host provides a user interface to support device discovery, pairing and display of a PIN |  |  | [1] 5.4.3.4.3 |  |  | O |  |  |

C.1: Mandatory IF HID11 1/1 “General HID Host, Report protocol” OR HID11 1/3 “Limited HID Host, Boot protocol”, otherwise Optional.
C.2: Mandatory IF HID11 1/1 “General HID Host, Report protocol”, otherwise Optional.
C.3: Mandatory IF HID11 1/1 “General HID Host, Report protocol” OR HID11 2/6 “Device initiated reconnection” OR HID11 2/7 “Host initiated reconnection”, otherwise Optional.
C.4: Mandatory IF HID11 2/8 “Support for entering Suspend mode”, otherwise Excluded.

#### 2.4.2 HID Protocol Procedures


##### 2.4.2.1 Report Protocol Transfers for General Hosts

Table 3: Report Protocol Transfers for General Hosts
Prerequisite: HID11 1/1 “General HID Host, Report protocol”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Report Protocol Device to Host reports on Control channel (Get Report) _ |  |  | [1] 3.2 |  |  | M |  |  |
| 2 |  |  | Report Protocol Device to Host reports on Interrupt channel |  |  | [1] 3.2 |  |  | M |  |  |
| 3 |  |  | Report Protocol Host to Device reports on Control channel (Set Report) for Output _ reports |  |  | [1] 3.2 |  |  | O |  |  |
| 4 |  |  | Report Protocol Host to Device reports on Interrupt channel |  |  | [1] 3.2 |  |  | M |  |  |
| 5 |  |  | Report Protocol Host to Device reports on Control channel (Set Report) for feature _ reports |  |  | [1] 3.2 |  |  | M |  |  |


##### 2.4.2.2 Report Protocol Transfers for Limited Hosts

Table 4: Report Protocol Transfers for Limited Hosts
Prerequisite: HID11 1/2 “Limited HID Host, Report protocol”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Report Protocol Device to Host reports on Control channel (Get Report) _ |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 2 |  |  | Report Protocol Device to Host reports on Interrupt channel |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 3 |  |  | Report Protocol Host to Device reports on Control channel (Set Report) for Output _ reports |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 4 |  |  | Report Protocol Host to Device reports on Interrupt channel |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 5 |  |  | Report Protocol Host to Device reports on Control channel (Set Report) for feature _ reports |  |  | [1] 3.2 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

##### 2.4.2.3 Boot Protocol Transfers

Table 5: Boot Protocol Transfers
Prerequisite: HID11 1/3 “Limited HID Host, Boot protocol”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Boot Protocol Device to Host reports on Control channel |  |  | [1] 3.3 |  |  | O |  |  |
| 2 |  |  | Boot Protocol Device to Host reports on Interrupt channel |  |  | [1] 3.3 |  |  | M |  |  |
| 3 |  |  | Boot Protocol Host to Device reports on Control channel (Set Report) _ |  |  | [1] 3.3 |  |  | O |  |  |
| 4 |  |  | Boot Protocol Host to Device reports on Interrupt channel |  |  | [1] 3.3 |  |  | O |  |  |


##### 2.4.2.4 HID Control Commands

Table 6: HID Control Commands
Prerequisite: HID11 1/1 “General HID Host, Report protocol” OR HID11 1/2 “Limited HID Host, Report protocol” OR HID11 1/3 “Limited HID Host, Boot protocol”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Set Protocol command _ |  |  | [1] 3.1.2.6 |  |  | C.1 |  |  |
| 2 |  |  | Get Protocol command _ |  |  | [1] 3.1.2.5 |  |  | O |  |  |
| 3 |  |  | Set Report command _ |  |  | [1] 3.1.2.4 |  |  | C.2 |  |  |
| 4 |  |  | Get Report command _ |  |  | [1] 3.1.2.3 |  |  | C.3 |  |  |
| 5 |  |  | HID CONTROL SUSPEND _ |  |  | [1] 3.1.2.2 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 |  |  | HID CONTROL EXIT SUSPEND _ _ |  |  | [1] 3.1.2.2 |  |  | C.4 |  |  |
| 7 |  |  | Receiving HID CONTROL VC UNPLUG _ _ |  |  | [1] 3.1.2.2 |  |  | C.5 |  |  |
| 8 |  |  | Sending HID CONTROL VC UNPLUG _ _ |  |  | [1] 3.1.2.2 |  |  | O |  |  |

C.1: Mandatory IF HID11 1/3 “Limited HID Host, Boot protocol”, otherwise Optional.
C.2: Mandatory IF HID11 3/3 “Report Protocol Host to Device reports on Control channel (Set_Report) for Output reports” OR HID11 3/5 “Report Protocol Host to Device reports on Control channel (Set_Report) for feature reports” OR HID11 4/3 “Report Protocol Host to Device reports on Control channel (Set_Report) for Output reports” OR HID11 4/5 “Report Protocol Host to Device reports on Control channel (Set_Report) for feature reports” OR HID11 5/3 “Boot Protocol Host to Device reports on Control channel (Set_Report)”, otherwise Optional.
C.3: Mandatory IF HID11 3/1 “Report Protocol Device to Host reports on Control channel (Get_Report)” OR HID11 4/1 “Report Protocol Device to Host reports on Control channel (Get_Report)” OR HID11 5/1 “Boot Protocol Device to Host reports on Control channel”, otherwise Optional.
C.4: Mandatory IF HID11 6/5 “HID_CONTROL SUSPEND”, otherwise Optional.
C.5: Mandatory IF HID11 2/5 “Support for virtual cables”, otherwise Optional.

#### 2.4.3 Link Manager Procedures

Table 7: Link Manager Procedures
Prerequisite: HID11 1/1 “General HID Host, Report protocol” OR HID11 1/2 “Limited HID Host, Report protocol” OR HID11 1/3 “Limited HID Host, Boot protocol”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Require MITM protection during pairing |  |  | [1] 5.4.3 |  |  | O |  |  |
| 2 |  |  | Security Mode 4 with Just Works |  |  | [1] 5.4.3 |  |  | C.1, C.4 |  |  |
| 3 |  |  | Security Mode 4 with Numeric Comparison |  |  | [1] 5.4.3 |  |  | C.1 |  |  |
| 4 |  |  | Security Mode 4 with Passkey Entry |  |  | [1] 5.4.3 |  |  | C.1 |  |  |
| 5 |  |  | Security Mode 4 with Out of Band |  |  | [1] 5.4.3 |  |  | C.1 |  |  |
| 6 |  |  | Security Mode 3 with pre-v2.1 HID Device |  |  | [1] 5.4.3.4.3 |  |  | C.2 |  |  |
| 7 |  |  | Security Mode 2 with pre-v2.1 HID Device, pairing before L2CAP channels established |  |  | [1] 5.4.3.4.3 |  |  | C.2 |  |  |
| 8 |  |  | Security Mode 2 with pre-v2.1 HID Device, pairing after L2CAP channels established |  |  | [1] 5.4.3.4.3 |  |  | C.2 |  |  |
| 9 |  |  | Security Mode 1 with pre-v2.1 HID Device |  |  | [1] 5.4.3.4.3 |  |  | O |  |  |
| 10 |  |  | Sniff mode |  |  | [1] 5.1.8.1, 5.1.12 |  |  | C.3 |  |  |
| 11 |  |  | Sniff Subrating |  |  | [1] 5.1.8.5, 5.1.12 |  |  | O |  |  |
| 12 |  |  | Role switch |  |  | [1] 5.1.12, 5.4.2 |  |  | O |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory to support at least one IF HID11 2/11 “Host provides a user interface to support device discovery, pairing and display of a PIN”, otherwise Optional.
C.3: Mandatory IF HID11 1/1 “General HID Host, Report protocol” OR HID11 1/3 “Limited HID Host, Boot protocol”, otherwise Optional.
C.4: Excluded IF HID11 7/1 “Require MITM protection during pairing”, otherwise Optional.

### 2.5 HID Device Role

Table 8: HID Device Roles
Prerequisite: HID11 1/4 “HID Device Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Pointing HID |  |  | [1] 5.3.4.3 |  |  | C.1 |  |  |
| 2 |  |  | Keyboard HID |  |  | [1] 5.3.4.3 |  |  | C.1 |  |  |
| 3 |  |  | Other HID (not pointing device nor keyboard device) |  |  | [1] 5.3.4.3 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

#### 2.5.1 Application Procedures

Table 9: Application Procedures
Prerequisite: HID11 1/4 “HID Device Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Accept HID connection |  |  | [1] 5.2.2 |  |  | M |  |  |
| 2 |  |  | Terminate HID connection |  |  | [1] 5.2.2 |  |  | O |  |  |
| 3 |  |  | Accept Termination of HID connection |  |  | [1] 5.2.2 |  |  | M |  |  |
| 4 |  |  | Support for virtual cables |  |  | [1] 4.5 |  |  | O |  |  |
| 5 |  |  | Device initiated reconnection |  |  | [1] 5.4.2 |  |  | C.1 |  |  |
| 6 |  |  | Host initiated reconnection |  |  | [1] 5.4.2 |  |  | C.1 |  |  |
| 7 |  |  | One or more output reports declared in report descriptor |  |  | [1] 2.1.1 |  |  | C.2, C.3 |  |  |
| 8 |  |  | One or more input reports declared in report descriptor |  |  | [1] 2.1.1 |  |  | C.2, C.4 |  |  |
| 9 |  |  | One or more feature reports declared in report descriptor |  |  | [1] 2.1.1 |  |  | C.2 |  |  |
| 10 |  |  | Support for multiple virtual cables |  |  | [1] 4.5.3 |  |  | O |  |  |
| 11 |  |  | Support for Suspend mode |  |  | [1] 3.1.2.2 |  |  | O |  |  |
| 12 |  |  | Disconnect from HID Host when entering Suspend mode |  |  | [1] 3.1.2.2 |  |  | O |  |  |

C.1: Mandatory to support at least one IF HID11 9/4 “Support for virtual cables”, otherwise Optional.
C.2: Mandatory to support at least one.
C.3: Mandatory IF HID11 8/2 “Keyboard HID”, otherwise Optional.
C.4: Mandatory IF HID11 8/1 “Pointing HID” OR HID11 8/2 “Keyboard HID”, otherwise Optional.

#### 2.5.2 HID Protocol Procedures


##### 2.5.2.1 Report Protocol Transfers

Table 10: Report Protocol Transfers
Prerequisite: HID11 1/4 “HID Device Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Report Protocol Device to Host reports on Control channel |  |  | [1] 3.2 |  |  | M |  |  |
| 2 |  |  | Report Protocol Device to Host reports on Interrupt channel |  |  | [1] 3.2 |  |  | C.1 |  |  |
| 3 |  |  | Report Protocol Host to Device reports on Control channel |  |  | [1] 3.2 |  |  | C.2 |  |  |
| 4 |  |  | Report Protocol Host to Device reports on Interrupt channel |  |  | [1] 3.2 |  |  | C.3 |  |  |

C.1: Optional IF HID11 9/8 “One or more input reports declared in report descriptor”, otherwise Excluded.
C.2: Mandatory IF HID11 9/7 “One or more output reports declared in report descriptor” OR HID11 9/9 “One or more feature reports declared in report descriptor”, otherwise Optional IF HID11 9/8 “One or more input reports declared in report descriptor”, otherwise Excluded.
C.3: Mandatory IF HID11 9/7 “One or more output reports declared in report descriptor”, otherwise Excluded.

##### 2.5.2.2 Boot Protocol Transfers

Table 11: Boot Protocol Transfers
Prerequisite: HID11 1/4 “HID Device Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Boot Protocol Device to Host reports on Control channel |  |  | [1] 3.3 |  |  | O |  |  |
| 2 |  |  | Boot Protocol Device to Host reports on Interrupt channel |  |  | [1] 3.3 |  |  | C.1 |  |  |
| 3 |  |  | Boot Protocol Host to Device reports on Control channel |  |  | [1] 3.3 |  |  | O |  |  |
| 4 |  |  | Boot Protocol Host to Device reports on Interrupt channel |  |  | [1] 3.3 |  |  | C.2 |  |  |

C.1: Mandatory IF HID11 8/1 “Pointing HID” OR HID11 8/2 “Keyboard HID”, otherwise Optional.
C.2: Mandatory IF HID11 8/2 “Keyboard HID”, otherwise Optional.

##### 2.5.2.3 HID Control Commands

Table 12: HID Control Commands
Prerequisite: HID11 1/4 “HID Device Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Set Protocol command _ |  |  | [1] 3.1.2.6 |  |  | C.1, C.5 |  |  |
| 2 |  |  | Get Protocol command _ |  |  | [1] 3.1.2.5 |  |  | C.1, C.5 |  |  |
| 3 |  |  | Set Report command _ |  |  | [1] 3.1.2.4 |  |  | C.2 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 |  |  | Get Report command _ |  |  | [1] 3.1.2.3 |  |  | M |  |  |
| 5 |  |  | HID CONTROL SUSPEND _ |  |  | [1] 3.1.2.2 |  |  | C.3 |  |  |
| 6 |  |  | HID CONTROL EXIT SUSPEND _ _ |  |  | [1] 3.1.2.2 |  |  | C.3 |  |  |
| 7 |  |  | Receiving HID CONTROL VC UNPLUG _ _ |  |  | [1] 3.1.2.2 |  |  | C.4 |  |  |
| 8 |  |  | Sending HID CONTROL VC UNPLUG _ _ |  |  | [1] 3.1.2.2 |  |  | O |  |  |

C.1: Mandatory IF HID11 8/1 “Pointing HID” OR HID11 8/2 “Keyboard HID”, otherwise Optional.
C.2: Mandatory IF HID11 9/7 “One or more output reports declared in report descriptor” OR HID11 9/9 “One or more feature reports declared in report descriptor”, otherwise Optional.
C.3: Mandatory IF HID11 9/11 “Support for Suspend mode”, otherwise Optional.
C.4: Mandatory IF HID11 9/4 “Support for virtual cables”, otherwise Optional.
C.5: Mandatory to support none or all.

#### 2.5.3 Link Manager Procedures

Table 13: Link Manager Procedures
Prerequisite: HID11 1/4 “HID Device Role”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Require MITM protection during pairing |  |  | [1] 5.4.3 |  |  | O |  |  |
| 2 |  |  | Security Mode 4 with Just Works |  |  | [1] 5.4.3 |  |  | C.1, C.6 |  |  |
| 3 |  |  | Security Mode 4 with Numeric Comparison |  |  | [1] 5.4.3 |  |  | C.1 |  |  |
| 4 |  |  | Security Mode 4 with Passkey Entry |  |  | [1] 5.4.3 |  |  | C.1 |  |  |
| 5 |  |  | Security Mode 4 with Out of Band |  |  | [1] 5.4.3 |  |  | C.1 |  |  |
| 6 |  |  | Security Mode 3 with pre-v2.1 HID Device |  |  | [1] 5.4.3.3.3 |  |  | C.5 |  |  |
| 7 |  |  | Security Mode 2 with pre-v2.1 HID Device, pairing before L2CAP channels established |  |  | [1] 5.4.3.3.3 |  |  | C.5 |  |  |
| 8 |  |  | Security Mode 2 with pre-v2.1 HID Device, pairing after L2CAP channels established |  |  | [1] 5.4.3.3.3 |  |  | C.5 |  |  |
| 9 |  |  | Security Mode 1 with pre-v2.1 HID Device |  |  | [1] 5.4.3.3.3 |  |  | O |  |  |
| 10 |  |  | Sniff mode |  |  | [1] 5.1.8.1 |  |  | C.2 |  |  |
| 11 |  |  | Request Sniff intervals or Sniff Subrating Maximum Latencies greater than 1 second |  |  | [1] 5.3.4.13 |  |  | O |  |  |
| 12 |  |  | Sniff Subrating |  |  | [1] 5.1.8.5, 5.1.12 |  |  | O |  |  |
| 13 |  |  | Role switch |  |  | [1] 5.1.12, 5.4.2 |  |  | C.3 |  |  |
| 14 |  |  | HIDReconnectInitiate in SDP has value of TRUE |  |  | [1] 5.3.4.6 |  |  | C.4 |  |  |

C.1: Mandatory to support at least one.
C.2: Mandatory IF HID Device remains connected for more than 30 s.
C.3: Mandatory IF HID11 13/4 “Security Mode 4 with Passkey Entry”, otherwise Optional.
C.4: Mandatory IF HID11 8/1 “Pointing HID” OR HID11 8/2 “Keyboard HID”, otherwise Optional.
C.5: Mandatory to support at least one IF HID11 8/2 “Keyboard HID”, otherwise Optional.
C.6: Excluded IF HID11 13/1 “Require MITM protection during pairing”, otherwise Optional.

#### 2.5.4 Profile Dependencies

Table 14: Profile Dependencies
Prerequisite: HID11 1/4 “HID Device Role”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1–2 | No longer used | N/A | N/A | N/A |  |  |
| 3 | Device Identification Profile v1.3 or later | [1] 1.3 | M | [2] DID 0/2 |  |  |

Table 15: GAP Requirements
Prerequisite: HID11 1/4 “HID Device Role”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Limited discoverable mode | [1] 5.4.1 | O | [5] GAP 1/2 |  |  |


## 3 References

[1] Human Interface Device Specification, Version 1.1 or later
[2] ICS Proforma for Device Identification Profile (DID)
[3] Human Interface Device Specification, Version 1.1.1
[4] Human Interface Device Specification, Version 1.1.2
[5] ICS Proforma for Generic Access Profile (GAP)

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
| 0 | 0 |  | 1.0 | 1.0 |  | 2003-04-06 |  |  |  | Removed mandatory HOLD mode for devices in |  |
|  |  |  |  |  |  |  |  |  |  | accordance with HID Profile Specification 1.0 |  |
|  |  |  |  |  |  |  |  |  |  | Final release for use with 1.0 Profile Specification |  |
|  | 1 |  |  | 1.0.1 |  |  | 2005-01-19 |  |  | Incorporate review comments for release. |  |
|  |  |  | 1.0.2r1 | 1.0.2r1 |  | 2005-06-20 | 2005-06-20 |  |  | Incorporate TSE 799 to accommodate boot mode |  |
|  |  |  |  |  |  |  |  |  |  | hosts |  |
|  | 2 |  |  | 1.0.2 |  |  | 2005-09-27 |  |  | Accept changes. Prepare for publication. |  |
|  |  |  | 1.0.3r0 | 1.0.3r0 |  | 2006-12-01 | 2006-12-01 |  |  | TSE 1797: Change Table 3.3.2.3 (Table 5 after TSE |  |
|  |  |  |  |  |  |  |  |  |  | 1979 is implemented) |  |
|  |  |  |  |  |  |  |  |  |  | TSE 1856: Update C.1. for Table 3.3.2.3 (5) and |  |
|  |  |  |  |  |  |  |  |  |  | 3.4.2.3 (13) |  |
|  |  |  |  |  |  |  |  |  |  | TSE 1979: Number tables consecutively |  |
|  | 3 |  |  | 1.0.3 |  |  | 2007-01-10 |  |  | Prepare for publication. |  |
|  |  |  | 1.0.4r0 | 1.0.4r0 |  | 2008-02 | 2008-02 |  |  | TSE 2308: Change Table 1 description and footnote |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2468: Add prerequisites to Tables 2,4, 6, and 7 |  |
|  | 4 |  |  | 1.0.4 |  |  | 2008-04 |  |  | Prepare for publication. |  |
|  |  |  | 1.0.5r0 | 1.0.5r0 |  | 2008-07-29 | 2008-07-29 |  |  | TSE: 2648: Aligned table numbers with TPG; Aligned |  |
|  |  |  |  |  |  |  |  |  |  | Table 1 items with TPG Table 1. Removed duplicate |  |
|  |  |  |  |  |  |  |  |  |  | table 17, moved Tables 8 and 9 to end. |  |
|  |  |  | 1.0.5r1-4 |  |  | 2008-08-09 – 11-20 |  |  |  | Further edits based on feedback in TSE 2648 |  |
|  |  |  |  |  |  |  |  |  |  | comments. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2582: Additions to Tables 2, 5, 9, and 12 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2562: TP/HCE/BV-02-I optional |  |
|  |  |  |  |  |  |  |  |  |  | Removed 15 and 16. |  |
|  | 5 |  |  | 1.0.5 |  |  | 2008-12-04 |  |  | Prepare for publication. |  |
|  |  |  | 1.1.0 r0-r15 | 1.1.0 r0-r15 |  | 2010-07-20 – 2011-02-01 | 2010-07-20 – |  |  | Major update to support the HID Profile Specification |  |
|  |  |  |  |  |  |  | 2011-02-01 |  |  | rev 1.1 (Alma) and the HID Profile Test Specification |  |
|  |  |  |  |  |  |  |  |  |  | rev 1.1 |  |
|  |  |  |  |  |  |  |  |  |  | Re-organized sections 3.4.2.1 & 3.4.2.2. Renumbered |  |
|  |  |  |  |  |  |  |  |  |  | table items. |  |
|  |  |  |  |  |  |  |  |  |  | Accepted all previous changes. Re-organized table 6 |  |
|  |  |  |  |  |  |  |  |  |  | and table 12. |  |
|  |  |  |  |  |  |  |  |  |  | Removed unreferenced items from table 2, 3 and 8. |  |
|  |  |  |  |  |  |  |  |  |  | Removed Identification HID device type since all |  |
|  |  |  |  |  |  |  |  |  |  | devices will have security support anyway. |  |
|  |  |  |  |  |  |  |  |  |  | Removed unreferenced PICS questions. |  |
|  |  |  |  |  |  |  |  |  |  | Separated PICS items for sending vs. receiving of |  |
|  |  |  |  |  |  |  |  |  |  | HID CONTROL VC UNPLUG _ _ |  |
|  |  |  |  |  |  |  |  |  |  | Minor changes to reflect that either Set Report or |  |
|  |  |  |  |  |  |  |  |  |  | _ asynchronous reports are required for General Hosts, |  |
|  |  |  |  |  |  |  |  |  |  | but not both. |  |
|  |  |  |  |  |  |  |  |  |  | Fixes to reflect Set Report required now only for |  |
|  |  |  |  |  |  |  |  |  |  | _ General Hosts when sending feature reports, and that |  |
|  |  |  |  |  |  |  |  |  |  | only async reports are required for input and output |  |
|  |  |  |  |  |  |  |  |  |  | reports. |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | Additional edits to clarify General Host requirements |  |
|  |  |  |  |  |  |  |  |  |  | related to Set Report. _ |  |
|  |  |  |  |  |  |  |  |  |  | Addressed further BTI comments. Added PICS entries |  |
|  |  |  |  |  |  |  |  |  |  | for external dependencies. |  |
|  | 6 |  |  | 1.1.0 |  |  | 2012-02-21 |  |  | Adopted by the Bluetooth SIG Board of Directors |  |
|  |  |  |  | 1.1.1r1 |  |  | 2013-05-01 |  |  | TSE 5048: Added Table 0 for versioning. |  |
|  | 7 |  |  | 1.1.1 |  |  | 2013-07-02 |  |  | Prepare for Publication |  |
|  |  |  | 1.1.2r00 | 1.1.2r00 |  | 2014-05-01 | 2014-05-01 |  |  | TSE 5501: Added C.5 to Table 13. Updated 13/6, |  |
|  |  |  |  |  |  |  |  |  |  | 13/7, and 13/8 Status from Mandatory to C.5. |  |
|  | 8 |  |  | 1.1.2 |  |  | 2014-07-07 |  |  | TCRL 2014-1 Publication |  |
|  |  |  | 1.1.3r00 | 1.1.3r00 |  | 2015-04-29 | 2015-04-29 |  |  | TSE 5932: Revised conditionals in Table 10 to reflect |  |
|  |  |  |  |  |  |  |  |  |  | Spec accurately. |  |
|  |  |  | 1.1.3r01 |  |  | 2015-06-01 |  |  |  | Review by Alicia Courtney. Converted to current |  |
|  |  |  |  |  |  |  |  |  |  | document template. |  |
|  | 9 |  |  | 1.1.3 |  |  | 2015-07-14 |  |  | Prepared for TCRL 2015-1 publication |  |
|  |  |  | 1.1.1.0r00 | 1.1.1.0r00 |  | 2015-10-28 | 2015-10-28 |  |  | Updated version numbering to align with Specification |  |
|  |  |  |  |  |  |  |  |  |  | version change from 1.1 to 1.1.1 for ESR09. With the |  |
|  |  |  |  |  |  |  |  |  |  | specification taking a third identifying number, the ICS |  |
|  |  |  |  |  |  |  |  |  |  | version identifier moves to the fourth number and |  |
|  |  |  |  |  |  |  |  |  |  | starts again at 0. |  |
|  |  |  | 1.1.1.0r01 |  |  | 2015-11-02 |  |  |  | Added item 1/4 for new Specification version 1.1.1 |  |
|  |  |  |  |  |  |  |  |  |  | (ESR09). |  |
|  |  |  |  | 1.1.1.0r02 |  |  | 2015-11-24 |  |  | Added Table 0a for minor versions. |  |
|  | 10 |  |  | 1.1.1.0 |  |  | 2015-12-22 |  |  | Prepared for TCRL 2015-2 publication |  |
|  |  |  | 1.1.1.1r00 | 1.1.1.1r00 |  | 2017-07-25 | 2017-07-25 |  |  | TSE 9114: Added “otherwise Optional” to C.1 of Table |  |
|  |  |  |  |  |  |  |  |  |  | 9. |  |
|  |  |  |  | 1.1.1.1r01 |  |  | 2017-09-21 |  |  | Template Update. |  |
| 11 | 11 |  | 1.1.1.1 | 1.1.1.1 |  | 2017-11-28 | 2017-11-28 |  |  | Approved by BTI. Prepared for TCRL 2017-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.1.1.1ed2 r00 |  |  | 2021-01-15 |  |  |  | TSE 15981 (rating 1): Updates for deprecations. Items |  |
|  |  |  |  |  |  |  |  |  |  | 14/1 and 14/2 are removed as they are no longer |  |
|  |  |  |  |  |  |  |  |  |  | needed after the 2.1 Core deprecations. |  |
|  |  |  |  | 1.1.1.1 |  | 2021-02-01 |  |  |  | Approved by BTI on 2021-01-15. Prepared for edition |  |
|  |  |  |  | edition 2 |  |  |  |  |  | 2 publication. |  |
|  |  |  | p12r00–r04 | p12r00–r04 |  | 2021-09-20 – 2021-12-08 |  |  |  | TSE 17437 (rating 1): Updated Table 0 to align with |  |
|  |  |  |  |  |  |  |  |  |  | the current ICS template. Changed the document |  |
|  |  |  |  |  |  |  |  |  |  | name and cover page. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 17684 (rating 1): Updated deprecation and |  |
|  |  |  |  |  |  |  |  |  |  | withdrawal information and made template-related |  |
|  |  |  |  |  |  |  |  |  |  | and consistency checker editorials. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 17715 (rating 1): Updated conditionals for |  |
|  |  |  |  |  |  |  |  |  |  | Table 1 to clarify roles; updated status of item 2 |  |
|  |  |  |  |  |  |  |  |  |  | accordingly. |  |
|  |  |  |  |  |  |  |  |  |  | Performed template-related fixes. Updated copyright |  |
|  |  |  |  |  |  |  |  |  |  | page to align with v2 of the DNMD. |  |
| 12 |  |  | p12 |  |  | 2022-01-25 |  |  |  | Approved by BTI on 2021-12-19. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  |  |  | 2021-2 publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p12ed2r00– r03 | p12ed2r00– |  | 2023-02-07 – 2023-02-23 |  | TSE 22360 (rating 1): Updated to the latest ICS |  |
|  |  |  |  | r03 |  |  |  | conventions, and updated the Withdrawal date for |  |
|  |  |  |  |  |  |  |  | HID 1.1 from 2023-02-01 to 2024-02-01 |  |
|  |  |  |  |  |  |  |  | Deleted draft revision history comment prior to p0. |  |
|  |  |  | p12 edition 2 |  |  | 2023-02-27 |  | Approved by BTI on 2023-02-23. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  | p13r00 |  |  | 2024-10-11 |  | TSE 25424 (rating 2): Per E23181, added prerequisite |  |
|  |  |  |  |  |  |  |  | HID11 1/4 “HID Device Role” to Table 14. |  |
| 13 |  |  | p13 |  |  | 2025-02-18 |  | Approved by BTI on 2024-12-25. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2025-1 publication. |  |
|  |  |  | p14r00 |  |  | 2025-02-27 |  | TSE 27006 (rating 2): For Table 0, updated 0/1 Status |  |
|  |  |  |  |  |  |  |  | value and conditional C.1 and added C.2. Added |  |
|  |  |  |  |  |  |  |  | “Core Configuration” section and Table 0b. |  |
| 14 |  |  | p14 |  |  | 2025-07-08 |  | Approved by BTI on 2025-05-30. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | pkg100 publication. |  |
|  |  |  | p15r00 |  |  | 2025-08-11 |  | TSE 27990 (rating 2): Updated the versions tables to |  |
|  |  |  |  |  |  |  |  | add HID v1.1.2. Updated the references list. |  |
| 15 |  |  | p15 |  |  | 2025-11-04 |  | Approved by BTI on 2025-09-24. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | pkg101 publication. |  |
|  |  |  | p16r00–r02 |  |  | 2025-12-05 – 2025-12-31 | TSE 28129 (rating 2): Updated the capability of Item HID11 14/3. Added Table 15, GAP Requirements. Updated the references list. TSE 28346 (rating 1): Updated the conditions in the transport table to make sure the layer is excluded when the design is an implementation of the Core- Controller Configuration by adding "OR CORE 40/1 “Core-Controller”" to an already excluded transport based on Core Configuration support. |  |  |
| 16 |  |  | p16 |  |  | 2026-02-17 | Approved by BTI on 2026-01-22. Prepared for TCRL pkg102 publication. |  |  |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Alicia Courtney |  |  | Broadcom |  |
|  | Robert Hulvey |  |  | Broadcom |  |
|  | Peter Flittner |  |  | Cambridge Silicon Radio |  |
|  | Fred Jaccard |  |  | Cypress Semiconductor |  |
|  | Steve McGowan |  |  | Intel |  |
|  | Venkat Yellapeddy |  |  | Intel |  |
|  | Jacques Chassot |  |  | Logitech |  |
|  | Roland Meyer |  |  | Logitech |  |
|  | Rene Sommer |  |  | Logitech |  |
|  | Randy Aull |  |  | Microsoft |  |
|  | Fred Bhesania |  |  | Microsoft |  |
|  | Chris Dreher |  |  | Microsoft |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Doron Holan |  |  | Microsoft |  |
|  | Craig Ranta |  |  | Microsoft |  |
|  | Jay Senior |  |  | Microsoft |  |
|  | Raymond Chiu |  |  | Motorola |  |
|  | Curtis Stevens |  |  | Phoenix Technologies |  |
|  | John Milios |  |  | Semtech |  |
