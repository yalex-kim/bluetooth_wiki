# GATT.ICS.p19

> Source: PDF converted via PyMuPDF.

---

Generic Attribute Profile (GATT)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: GATT.ICS.p19 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2009–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Roles

Table 1: Role Requirements

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Generic Attribute Profile (GATT) Client |  |  | [1] 2.2 |  |  | O |  |  |
| 2 |  |  | Generic Attribute Profile (GATT) Server |  |  | [1] 2.2 |  |  | M |  |  |


### 1.3 Transports

Table 1a: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | GATT Client over LE |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 2 |  |  | GATT Client over BR/EDR |  |  | [1] 2.2 |  |  | C.1 |  |  |
| 3 |  |  | GATT Server over LE |  |  | [1] 2.2 |  |  | C.2 |  |  |
| 4 |  |  | GATT Server over BR/EDR |  |  | [1] 2.2 |  |  | C.2 |  |  |

Table 2: Attribute Protocol Transport Requirements

| Item | Transport | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Unenhanced ATT bearer over BR/EDR | [1] 2 | C.1 | [5] ATT 2/1 |  |  |
| 2 | Unenhanced ATT bearer over LE | [1] 2 | C.2 | [5] ATT 2/2 |  |  |
| 3 | No longer used | N/A | N/A | N/A |  |  |
| 3a | Enhanced ATT bearer over LE | [1] 5.5 [3] 3.2.11 | C.4, C.3 | [5] ATT 2/3a |  |  |
| 3b | Enhanced ATT bearer over BR/EDR | [1] 5.5 [3] 3.2.11 | C.1, C.3 | [5] ATT 2/3b |  |  |
| 4 | Attribute Protocol Client | [1] 2 | C.6 | [5] ATT 1/1 |  |  |
| 5 | Attribute Protocol Server | [1] 2 | C.7 | [5] ATT 1/2 |  |  |


### 1.4 GATT Features

Table 3: Generic Attribute Profile Feature Support, by Client
Prerequisite: GATT 1/1 “Generic Attribute Profile (GATT) Client”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Exchange MTU |  |  | [1] 4.3.1 |  |  | C.11 |  |  |
| 2 |  |  | Discover All Primary Services |  |  | [1] 4.4.1 |  |  | O |  |  |
| 3 |  |  | Discover Primary Services by Service UUID |  |  | [1] 4.4.2 |  |  | O |  |  |
| 4 |  |  | Find Included Services |  |  | [1] 4.5.1 |  |  | O |  |  |
| 5 |  |  | Discover All Characteristics of a Service |  |  | [1] 4.6.1 |  |  | O |  |  |
| 6 |  |  | Discover Characteristics by UUID |  |  | [1] 4.6.2 |  |  | O |  |  |
| 7 |  |  | Discover All Characteristic Descriptors |  |  | [1] 4.7.1 |  |  | O |  |  |
| 8 |  |  | Read Characteristic Value |  |  | [1] 4.8.1 |  |  | O |  |  |
| 9 |  |  | Read Using Characteristic UUID |  |  | [1] 4.8.2 |  |  | O |  |  |
| 10 |  |  | Read Long Characteristic Values |  |  | [1] 4.8.3 |  |  | O |  |  |
| 11 |  |  | Read Multiple Characteristic Values |  |  | [1] 4.8.4 |  |  | O |  |  |
| 12 |  |  | Write without Response |  |  | [1] 4.9.1 |  |  | O |  |  |
| 13 |  |  | Signed Write Without Response |  |  | [1] 4.9.2 |  |  | C.11 |  |  |
| 14 |  |  | Write Characteristic Value |  |  | [1] 4.9.3 |  |  | O |  |  |
| 15 |  |  | Write Long Characteristic Values |  |  | [1] 4.9.4 |  |  | O |  |  |
| 16 |  |  | Characteristic Value Reliable Writes |  |  | [1] 4.9.5 |  |  | O |  |  |
| 17 |  |  | Notifications |  |  | [1] 4.10.1 |  |  | C.7 |  |  |
| 18 |  |  | Indications |  |  | [1] 4.11.1 |  |  | M |  |  |
| 19 |  |  | Read Characteristic Descriptors |  |  | [1] 4.12.1 |  |  | O |  |  |
| 20 |  |  | Read Long Characteristic Descriptors |  |  | [1] 4.12.2 |  |  | O |  |  |
| 21 |  |  | Write Characteristic Descriptors |  |  | [1] 4.12.3 |  |  | O |  |  |
| 22 |  |  | Write Long Characteristic Descriptors |  |  | [1] 4.12.4 |  |  | O |  |  |
| 23 |  |  | Service Changed Characteristic |  |  | [1] 7.1 |  |  | M |  |  |
| 24 |  |  | Configured Broadcast |  |  | [1] 2.7 |  |  | C.2 |  |  |
| 25 |  |  | Client Supported Features Characteristic |  |  | [1] 7.2 |  |  | C.4 |  |  |
| 25a |  |  | Enabling Robust Caching |  |  | [1] 7.2 |  |  | C.12 |  |  |
| 26 |  |  | Database Hash Characteristic |  |  | [1] 7.3 |  |  | C.4 |  |  |
| 27 |  |  | Read and Interpret Characteristic Presentation Format |  |  | [1] 3.3.3.5 |  |  | O |  |  |
| 28 |  |  | Read and Interpret Characteristic Aggregate Format |  |  | [1] 3.3.3.6 |  |  | C.6 |  |  |
| 29 |  |  | Read Multiple Variable Length Characteristic Values |  |  | [4] 4.8.5 |  |  | C.9 |  |  |
| 30 |  |  | Multiple Variable Length Notifications |  |  | [4] 4.10.2 |  |  | C.10 |  |  |

C.7: Mandatory IF GATT 2/3a “Enhanced ATT bearer over LE” OR GATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Optional. C.8: No longer used. C.9: Optional IF CORE 2a/52 “Host Core v5.2 or later”, otherwise Excluded. C.10: Mandatory IF CORE 2a/52 “Host Core v5.2 or later” AND (GATT 2/3a “Enhanced ATT bearer over LE” OR GATT 2/3b “Enhanced ATT bearer over BR/EDR”), otherwise Optional IF CORE 2a/52 “Host Core v5.2 or later”, otherwise Excluded. C.11: Optional IF GATT 1a/1 “GATT Client over LE”, otherwise Excluded. C.12: Optional IF GATT 3/25 “Client Supported Features Characteristic”, otherwise Excluded.
Table 3a: GAP Role Requirements for GATT Client
Prerequisite: GATT 1a/1 “GATT Client over LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |  | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Peripheral |  |  | [2] 15.2 |  |  | O |  |  | [7] GAP 5/3 OR GAP 38/3 |  |  |
| 2 |  |  | Central |  |  | [2] 15.2 |  |  | O |  |  | [7] GAP 5/4 OR GAP 38/4 |  |  |

Table 3B: No longer used
Table 4: Generic Attribute Profile Feature Support, by Server
Prerequisite: GATT 1/2 “Generic Attribute Profile (GATT) Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Exchange MTU |  |  | [1] 4.3.1 |  |  | C.6 |  |  |
| 2 |  |  | Discover All Primary Services |  |  | [1] 4.4.1 |  |  | M |  |  |
| 3 |  |  | Discover Primary Services by Service UUID |  |  | [1] 4.4.2 |  |  | M |  |  |
| 4 |  |  | Find Included Services |  |  | [1] 4.5.1 |  |  | M |  |  |
| 5 |  |  | Discover All Characteristics of a Service |  |  | [1] 4.6.1 |  |  | M |  |  |
| 6 |  |  | Discover Characteristics by UUID |  |  | [1] 4.6.2 |  |  | M |  |  |
| 7 |  |  | Discover All Characteristic Descriptors |  |  | [1] 4.7.1 |  |  | M |  |  |
| 8 |  |  | Read Characteristic Value |  |  | [1] 4.8.1 |  |  | M |  |  |
| 9 |  |  | Read Using Characteristic UUID |  |  | [1] 4.8.2 |  |  | M |  |  |
| 10 |  |  | Read Long Characteristic Values |  |  | [1] 4.8.3 |  |  | C.12 |  |  |
| 11 |  |  | Read Multiple Characteristic Values |  |  | [1] 4.8.4 |  |  | O |  |  |
| 12 |  |  | Write without Response |  |  | [1] 4.9.1 |  |  | C.2 |  |  |
| 13 |  |  | Signed Write Without Response |  |  | [1] 4.9.2 |  |  | C.6 |  |  |
| 14 |  |  | Write Characteristic Value |  |  | [1] 4.9.3 |  |  | C.3 |  |  |
| 15 |  |  | Write Long Characteristic Values |  |  | [1] 4.9.4 |  |  | C.12 |  |  |
| 16 |  |  | Characteristic Value Reliable Writes |  |  | [1] 4.9.5 |  |  | O |  |  |
| 17 |  |  | Notifications |  |  | [1] 4.10.1 |  |  | O |  |  |
| 18 |  |  | Indications |  |  | [1] 4.11.1 |  |  | C.1 |  |  |
| 19 |  |  | Read Characteristic Descriptors |  |  | [1] 4.12.1 |  |  | C.12 |  |  |
| 20 |  |  | Read Long Characteristic Descriptors |  |  | [1] 4.12.2 |  |  | C.12 |  |  |
| 21 |  |  | Write Characteristic Descriptors |  |  | [1] 4.12.3 |  |  | C.12 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 |  |  | Write Long Characteristic Descriptors |  |  | [1] 4.12.4 |  |  | O |  |  |
| 23 |  |  | Service Changed Characteristic |  |  | [1] 7.1 |  |  | C.14 |  |  |
| 24 |  |  | Configured Broadcast |  |  | [1] 2.7 |  |  | C.5 |  |  |
| 25 |  |  | Execute Write Request with empty queue |  |  | [1] 4.9.4, 4.9.5, 4.12.4 |  |  | C.7 |  |  |
| 26 |  |  | Client Supported Features Characteristic |  |  | [1] 7.2 |  |  | C.9 |  |  |
| 27 |  |  | Database Hash Characteristic |  |  | [1] 7.3 |  |  | C.8 |  |  |
| 28 |  |  | Report Characteristic Value: Characteristic Presentation Format |  |  | [1] 3.3.3.5 |  |  | O |  |  |
| 29 |  |  | Report aggregate Characteristic Value: Characteristic Aggregate Format |  |  | [1] 3.3.3.6 |  |  | C.10 |  |  |
| 30 |  |  | Read Multiple Variable Length Characteristic Values |  |  | [4] 4.8.5 |  |  | C.13 |  |  |
| 31 |  |  | Multiple Variable Length Notifications |  |  | [4] 4.10.2 |  |  | C.13 |  |  |

Table 4a: GAP Role Requirements for GATT Server
Prerequisite: GATT 1a/3 “GATT Server over LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |  | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Peripheral |  |  | [2] 15.2 |  |  | O |  |  | [7] GAP 5/3 OR GAP 38/3 |  |  |
| 2 |  |  | Central |  |  | [2] 15.2 |  |  | O |  |  | [7] GAP 5/4 OR GAP 38/4 |  |  |


### 1.5 SDP requirements

Table 6: SDP Interoperability
Prerequisite: GATT 2/1 “Unenhanced ATT bearer over BR/EDR” OR GATT 2/3b “Enhanced ATT bearer over BR/EDR”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | No longer used | N/A | N/A | N/A |  |  |
| 2 | Client | [1] 5.1.2 [4] 5.1.2, 5.3.2 | C.1 | [6] SDP 1b/2 |  |  |
| 3 | Server | [1] 9 | C.2 | [6] SDP 1b/1 |  |  |
| 4 | ProtocolDescriptorList | [1] 9, [2] 15.4 | C.2 | [6] SDP 9/2 |  |  |
| 5 | BrowseGroupList | [1] 9, [2] 15.4 | C.2 | [6] SDP 9/5 |  |  |
| 6 | AdditionalProtocolDescriptorList | [1] 9, [2] 15.4 | C.3 | [6] SDP 9/17 |  |  |


### 1.6 GAP requirements

Table 7: GAP Requirements

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |  | Inter-Layer Dependency |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 2 |  |  | LE security mode 1 |  |  | [2] 10.2.1 |  |  | C.2 |  |  | [7] GAP 25/1 OR GAP 35/1 |  |  |
| 3 |  |  | LE security mode 2 |  |  | [2] 10.2.2 |  |  | C.2 |  |  | [7] GAP 25/2 OR GAP 35/2 |  |  |
| 4 |  |  | Authentication procedure |  |  | [2] 10.3 |  |  | C.2 |  |  | [7] GAP 25/3 OR GAP 35/3 |  |  |
| 5 |  |  | Connection data signing procedure |  |  | [2] 10.4.1 |  |  | C.2 |  |  | [7] GAP 25/5 OR GAP 35/5 |  |  |
| 6 |  |  | Authenticate signed data procedure |  |  | [2] 10.4.2 |  |  | C.2 |  |  | [7] GAP 25/6 OR GAP 35/6 |  |  |
| 7 |  |  | Authorization procedure |  |  | [2] 10.5 |  |  | C.2 |  |  | [7] GAP 25/4 OR GAP 35/4 |  |  |
| 8 |  |  | Client security checks for GATT indications and notifications |  |  | [2] 10.3.2.2 |  |  | C.3 |  |  | [7] GAP 25/14 OR GAP 35/15 |  |  |

C.1: No longer used. C.2: Optional IF GATT 2/2 “Unenhanced ATT bearer over LE”, otherwise not defined. C.3: Mandatory IF CORE 2a/53 “Host Core v5.3 or later” AND GATT 1a/1 “GATT Client over LE”, otherwise Optional IF GATT 1a/1 “GATT Client over LE”, otherwise not defined.

### 1.7 Multiple Bearer Support

Table 8: Multiple Simultaneous ATT Bearers

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Support for multiple simultaneous active ATT bearers from same device – ATT over LE and ATT over BR/EDR |  |  | [3] 3.3.3 |  |  | C.1 |  |  |
| 2 |  |  | Support for multiple simultaneous active ATT bearers from same device – ATT over LE and EATT over LE |  |  | [4] 5.5 |  |  | C.2 |  |  |
| 3 |  |  | Support for multiple simultaneous active ATT bearers from same device – ATT over BR/EDR and EATT over BR/EDR |  |  | [4] 5.5 |  |  | C.3 |  |  |
| 4 |  |  | Support for multiple simultaneous active ATT bearers from same device – ATT over LE and EATT over BR/EDR |  |  | [4] 5.5 |  |  | C.4 |  |  |
| 5 |  |  | Support for multiple simultaneous active ATT bearers from same device – ATT over BR/EDR and EATT over LE |  |  | [4] 5.5 |  |  | C.5 |  |  |
| 6 |  |  | Support for multiple simultaneous active EATT bearers from same device – EATT over BR/EDR and EATT over LE |  |  | [4] 5.5 |  |  | C.6 |  |  |
| 7 |  |  | Support for multiple simultaneous active EATT bearers from same device – EATT over BR/EDR |  |  | [4] 5.5 |  |  | C.7 |  |  |
| 8 |  |  | Support for multiple simultaneous active EATT bearers from same device – EATT over LE |  |  | [4] 5.5 |  |  | C.7 |  |  |

C.1: Optional IF GATT 2/1 “Unenhanced ATT bearer over BR/EDR” AND GATT 2/2 “Unenhanced ATT bearer over LE”, otherwise Excluded. C.2: Optional IF GATT 2/2 “Unenhanced ATT bearer over LE” AND GATT 2/3a “Enhanced ATT bearer over LE”, otherwise Excluded. C.3: Optional IF GATT 2/1 “Unenhanced ATT bearer over BR/EDR” AND GATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Excluded. C.4: Optional IF GATT 2/2 “Unenhanced ATT bearer over LE” AND GATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Excluded. C.5: Optional IF GATT 2/1 “Unenhanced ATT bearer over BR/EDR” AND GATT 2/3a “Enhanced ATT bearer over LE”, otherwise Excluded. C.6: Optional IF GATT 2/3a “Enhanced ATT bearer over LE” AND GATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Excluded. C.7: Optional IF GATT 2/3a “Enhanced ATT bearer over LE” OR GATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Excluded.

### 1.8 ATT requirements

Table 9: Attribute Protocol Client Requirements
Prerequisite: GATT 1/1 “Generic Attribute Profile (GATT) Client”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Exchange MTU Request | [1] 4.3.1 | C.1 | [5] ATT 3/2 |  |  |
| 2 | Find Information Request | [1] 4.7.1 | C.2 | [5] ATT 3/4 |  |  |
| 3 | Find by Type Value Request | [1] 4.4.2 | C.3 | [5] ATT 3/6 |  |  |
| 4 | Read by Type Request | [1] 4.8.1 | C.4 | [5] ATT 3/8 |  |  |
| 5 | Read Request | [1] 4.8.1, 4.12.1 | C.5 | [5] ATT 3/10 |  |  |
| 6 | Read Blob Request | [1] 4.8.2, 4.12.2 | C.6 | [5] ATT 3/12 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 7 | Read Multiple Request | [1] 4.8.3 | C.7 | [5] ATT 3/14 |  |  |
| 8 | Write Request | [1] 4.9.3, 4.12.3 | C.8 | [5] ATT 3/18 |  |  |
| 9 | Write Command | [1] 4.9.1 | C.9 | [5] ATT 3/20 |  |  |
| 10 | Signed Write Command | [1] 4.9.2 | C.10 | [5] ATT 3/21 |  |  |
| 11 | Prepare Write Request | [1] 4.9.4, 4.9.5, 4.9.12.4 | C.11 | [5] ATT 3/22 |  |  |
| 12 | Handle Value Notification | [1] 4.10.1 | C.12 | [5] ATT 3/26 |  |  |
| 13 | Handle Value Indication | [1] 4.11.1 | C.13 | [5] ATT 3/27 |  |  |
| 14 | Read Multiple Variable Length Request | [4] 4.8.5 | C.14 | [5] ATT 3/30 |  |  |
| 15 | Handle Value Multiple Notification | [4] 4.10.2 | C.15 | [5] ATT 3/32 |  |  |

C.1: Mandatory IF GATT 3/1 “Exchange MTU”, otherwise not defined. C.2: Mandatory IF GATT 3/7 “Discover All Characteristic Descriptors”, otherwise not defined. C.3: Mandatory IF GATT 3/3 “Discover Primary Services by Service UUID”, otherwise not defined. C.4: Mandatory IF GATT 3/9 “Read Using Characteristic UUID”, otherwise not defined. C.5: Mandatory IF GATT 3/8 “Read Characteristic Value” OR GATT 3/19 “Read Characteristic Descriptors”, otherwise not defined. C.6: Mandatory IF GATT 3/10 “Read Long Characteristic Values” OR GATT 3/20 “Read Long Characteristic Descriptors”, otherwise not defined. C.7: Mandatory IF GATT 3/11 “Read Multiple Characteristic Values”, otherwise not defined. C.8: Mandatory IF GATT 3/14 “Write Characteristic Value” OR GATT 3/21 “Write Characteristic Descriptors”, otherwise not defined. C.9: Mandatory IF GATT 3/12 “Write without Response”, otherwise not defined. C.10: Mandatory IF GATT 3/13 “Signed Write Without Response”, otherwise not defined. C.11: Mandatory IF GATT 3/15 “Write Long Characteristic Values” OR GATT 3/16 “Characteristic Value Reliable Writes” OR GATT 3/22 “Write Long Characteristic Descriptors”, otherwise not defined. C.12: Mandatory IF GATT 3/17 “Notifications”, otherwise Optional. C.13: Mandatory IF GATT 3/18 “Indications”, otherwise not defined. C.14: Mandatory IF GATT 3/29 “Read Multiple Variable Length Characteristic Values”, otherwise not defined. C.15: Mandatory IF GATT 3/30 “Multiple Variable Length Notifications”, otherwise not defined.
Table 10: Attribute Protocol Server Requirements
Prerequisite: GATT 1/2 “Generic Attribute Profile (GATT) Server”

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Exchange MTU Request | [1] 4.3.1 | C.1 | [5] ATT 4/2 |  |  |
| 2 | Read Blob Request | [1] 4.8.2, 4.12.2 | C.2 | [5] ATT 4/12 |  |  |
| 3 | Read Multiple Request | [1] 4.8.3 | C.3 | [5] ATT 4/14 |  |  |
| 4 | Write Request | [1] 4.9.3, 4.12.3 | C.4 | [5] ATT 4/18 |  |  |
| 5 | Write Command | [1] 4.9.1 | C.5 | [5] ATT 4/20 |  |  |
| 6 | Signed Write Command | [1] 4.9.2 | C.6 | [5] ATT 4/21 |  |  |
| 7 | Prepare Write Request | [1] 4.9.4, 4.9.5, 4.9.12.4 | C.7 | [5] ATT 4/22 |  |  |
| 8 | Handle Value Notification | [1] 4.10.1 | C.8 | [5] ATT 4/26 |  |  |
| 9 | Handle Value Indication | [1] 4.11.1 | C.9 | [5] ATT 4/27 |  |  |


| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 10 | No longer used | N/A | N/A | N/A |  |  |
| 11 | Read Multiple Variable Length Request | [4] 4.8.5 | C.11 | [5] ATT 4/31 |  |  |
| 12 | Handle Value Multiple Notification | [4] 4.10.2 | C.12 | [5] ATT 4/33 |  |  |

C.1: Mandatory IF GATT 4/1 “Exchange MTU”, otherwise not defined. C.2: Mandatory IF GATT 4/10 “Read Long Characteristic Values”, otherwise not defined. C.3: Mandatory IF GATT 4/11 “Read Multiple Characteristic Values”, otherwise Optional. C.4: Mandatory IF GATT 4/14 “Write Characteristic Value” OR GATT 4/21 “Write Characteristic Descriptors”, otherwise Optional. C.5: Mandatory IF GATT 4/12 “Write without Response”, otherwise Optional. C.6: Mandatory IF GATT 4/13 “Signed Write Without Response”, otherwise Optional. C.7: Mandatory IF GATT 4/15 “Write Long Characteristic Values” OR GATT 4/16 “Characteristic Value Reliable Writes” OR GATT 4/22 “Write Long Characteristic Descriptors” OR GATT 2/3a “Enhanced ATT bearer over LE” OR GATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Optional. C.8: Mandatory IF GATT 4/17 “Notifications”, otherwise Optional. C.9: Mandatory IF GATT 4/18 “Indications”, otherwise Optional. C.10: No longer used. C.11: Mandatory IF GATT 4/30 “Read Multiple Variable Length Characteristic Values”, otherwise Optional. C.12: Mandatory IF GATT 4/31 “Multiple Variable Length Notifications”, otherwise Optional.

## 2 References

[1] Specification of the Bluetooth System, Volume 3, Part G (GATT)
[2] Specification of the Bluetooth System, Volume 3, Part C (GAP)
[3] Specification of the Bluetooth System, Volume 3, Part F (ATT)
[4] Specification of the Bluetooth System, Volume 3, Part G, (GATT), Version 5.2 or later
[5] ICS Proforma for Attribute Protocol (ATT)
[6] ICS Proforma for Service Discovery Protocol (SDP)
[7] ICS Proforma for Generic Access Profile (GAP)

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | 4.0.0 |  |  | 2010-06-30 | Publication. |
|  |  |  | 4.0.1r0 |  |  | 2011-02-02 | TSE 4236: Remove 5/1, add 3/23 and 4/23, 4. C1 TSE 4252: Table 2 C.1, C.2 additions |
|  |  |  | 4.0.1r1 |  |  | 2011-03-09 | TSE 4225: Removal of Table 6 (never tested) |
|  |  |  | 4.0.1r1 (cont.) |  |  | 2011-03-10 | TSE 3862: Add tables 8A and 20A |
|  |  |  | 4.0.1r2 |  |  | 2011-03-16 | Per review comments, reinstate Table 6 except for Row 1 TSE 4286: Edit Table 3 and Table 4 titles |
| 1 |  |  | 4.0.1 |  |  | 2011-07-15 | Prepare for publication. |
|  |  |  | 4.0.2r0 |  |  | 2011-11-21 – 12-16 | TSE 4559: Update Table 1 to make server mandatory, client optional. TSE 4661 Additions from GATT-3 Test CR D09r08 |
| 2 |  |  | 4.0.2 |  |  | 2012-03-30 | Prepare for publication. |
|  |  |  | 4.0.3r0 |  |  | 2012-09-07 | TSE 4915: Note added after Table 1, Changes to Prerequisites and Conditionals in Table 3b and 4b. |
| 3 |  |  | 4.0.3 |  |  | 2012-11-12 | Prepare for Publication |
|  |  |  | 4.0.4rT |  |  | 2013-08-12 | Template Conversion |
|  |  |  | 4.0.4rTr3 |  |  | 2013-09-27 | Template Review Comment Resolution |
|  |  |  | 4.0.4rTr4 |  |  | 2013-09-27 | TSE 5303: Updated references in Table 2 from 2.2 to 2.4. TSE 5344: Updated C.1 and C.2 for Table 1. |
|  |  |  | 4.1.0r01 |  |  | 2013-10-04 | LE Dual Mode Topology CR |
|  |  |  | 4.1.0r02 |  |  | 2013-11-06 | Comment resolution |
| 4 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
| 5 |  |  | 4.1.1r00 |  |  | 2014-10-20 | TSE 5873: Added C.2 to Table 3 and updated the status of 3/1. |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
| 6 |  |  | 4.2.0 |  |  | 2014-12-04 | Prepare for TCRL 2014-2 publication |
|  |  |  | 4.2.1r00 |  |  | 2015-05-05 | TSE 6320: Revised Table 3 conditionals TSE 6274: Added ATT reference to References section and corrected reference in Table 8. |
|  |  |  | 4.2.1r01 |  |  | 2015-06-05 | Deleted Section 1.2 (Global Statement of Conformance) per current ICS template standards. |
| 7 |  |  | 4.2.1 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 4.2.2r00 |  |  | 2016-01-15 | TSE 6876: Added Item 24, Configured Broadcast, to Tables 3 and 4. Added new conditional statements, C.3 and C.5. (TSE 5448: Change addressed, but not integrated.) |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 4.2.2r01 |  |  | 2016-03-04 | TSE 6651: For Table 3, Item 3, Status changed from C.1 to C.4. Expanded conditional statement C.2 for Table 3. Added new conditional statement C.4 for Table 3. For Table 4, Item 1, Status changed from C.4 to C.6. Added new conditional statement C.6 for Table 4. For Table 7, Items 3, 4, and 7, Status updated. Added three new conditional statements for Table 7. |
|  |  |  | 4.2.2r02 |  |  | 2016-04-27 | Editorial changes. |
| 8 |  |  | 4.2.2 |  |  | 2016-07-13 | Prepared for TCRL 2016-1 publication. |
|  |  |  | 5.0.0r00 |  |  | 2016-08-16 | TSE 7430: Updated Status column of and added one conditional to Table 7. |
|  |  |  | 5.0.0r01 |  |  | 2016-10-17 | TSE 7573 (erratum 5610): Added item 4/25 – Execute Write Request with empty queue. |
|  |  |  | 5.0.0r02 |  |  | 2016-11-08 | Updated Template. Removed unnecessary parentheses. |
| 9 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.0.1r00-r03 |  |  | 2018-03-01 - 2018-11-13 | TSE 8319 (rating 3): Table 1: For items 1 and 2, added (GATT) to the Capability column. Deleted items 3 and 4. Revised C.2 (changed "or" to "OR"). Deleted C.3, C.4, and Note. Table 1a: Added new table and conditionals. Table 2: For C.1, changed "Mandatory" to "Optional". Table 3: Replaced with new table. Deleted old C.1, renumbered and revised subsequent conditionals. Table 3B: Revised Prerequisite. Changed "Status" column heading to "Prerequisite 1a/5 Status". Added new column "Prerequisite 1a/6 Status". Table 4: Replaced with new table. Revised C.6. Table 4B: Revised Prerequisite. Changed "Status" column heading to "Prerequisite 1a/7 Status". Added new column "Prerequisite 1a/8 Status". Table 6: Revised C.1 and C.2. Table 8: For item 1, changed Status from "O" to "C.1". Added new C.1. Incorporated GATT Caching TEST CR r09. Added items 3/25, 3/26, and new conditionals C.4 and C.5 to Table 3. Added items 4/26, 4/27, and new conditional C.8 to Table 4. Issue 11143: Changes to Table 4 to make the GATT Caching feature optional. Production edits. |
|  |  |  | 5.1.0r00-r01 |  |  | 2018-11-13 - 2018-12-09 | Updated revision number from 5.0.1 to 5.1.0 to align with the adoption of Core Specification version 5.1. Corrected Table 4 C.4 to refer to new items 1a/7 and 1a/8 instead of deleted item 1/4. |
| 10 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.1.1r00 |  |  | 2019-04-10 | TSE 11538 (rating 4): Removed Complete GATT ICS items and Tables 3B and 4B. Added new ICS for Server and Client for Characteristic Presentation Format and Characteristic Aggregate Format. TSE 11781 (rating 2): Updated C.4 note in Table 3 to reference appropriate Host Configuration Spec Version. |
|  |  |  | 5.1.1r01–r03 |  |  | 2019-05-30– 2019-06-18 | Updated to accommodate additional changes made by Alicia to incorporate TSE 11781 fully (Table 4 required changes similar to those made in Table 3 earlier). |
| 11 |  |  | 5.1.1 |  |  | 2019-08-01 | Approved by BTI. Prepared for TCRL 2019-1 publication. |
|  |  |  | p12r00–r06 |  |  | 2019-08-20 – 2019-11-21 | Added test groups to accommodate adoption of Core Specification Milan with regard to EATT CR r07. Added items 29 and 30 and notes C.7–C.11 to Table 3 and updated status of items 1, 13, 17, 18; added items 30 and 31 and notes C.11–C.14 to Table 4 and updated table title and status of items 10, 13, 15, 17, and 19–21; updated references section with new Core Specification. TSE 12444 (rating 2): Updated conditional statements C.1 and C.2 after Table 1. Updated conditional statements C.1–C.4 after Table 1a. TSE 12440 (rating 3): For Table 3, updated prerequisite statement and edited two prerequisite columns into a single Status column, removed conditional 3 (changed to No Longer Used) and added conditional C.12 (renumbered to C.11 after removal of Milan’s C.7 during BTI F2F), and updated status for items 1, 3, and 13; for Table 4, updated prerequisite statement and edited two prerequisite columns into a single Status column, updated conditional statement C.6 (revised further at BTI F2F from Milan, thereby deleting Milan’s C.13), and updated status for item 13. TSE 12780 (rating 2): Updated the conditionals for Table 2 to align with ATT changes (after incorporation of TSE 12739). Issue 12503 (CR from comment 51825): For Table 3, deleted conditional C.8 and changed item 18’s status to M accordingly; for Table 4, modified C.6 and C.13 and deleted C.11. Issue 12740 (CR from comment 51451): For Table 2, added item 3 and note C.3. Updated .X references and Milan references to real numbers. Revised document numbering convention, setting last release publication of 5.1.1 as p11; added publication number column to Revision History. |
| 12 |  |  | p12 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p13r00–r03 |  |  | 2020-03-26 – 2020-11-16 | TSE 13111 (rating 3): To align ICS with revised TS addressing issue with “ATT 2/3 does not mean multiple ATT bearer support”: updated items and added conditionals to Tables 2 and 8, renamed Table 7. TSE 14883 (rating 2): Corrected C.3 in Table 2 after the additions from TSE 13111. Consistency Checker fixes and template-related editorials. |
| 13 |  |  | p13 |  |  | 2020-12-22 | Approved by BTI on 2020-12-03. Prepared for TCRL 2020-1 publication. |
|  |  |  | p14r00–r02 |  |  | 2021-02-23 – 2021-06-11 | TSE 16382 (rating 1): To address an “or-later” issue from TSE 16342, revised C.7 for Table 4 so that it reflects the correct Core versions in the Mandatory and Optional logical clauses. Template-related and consistency checker editorials. |
| 14 |  |  | p14 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |
|  |  |  | p15r00–r03 |  |  | 2022-02-02 – 2022-04-06 | TSE 17969 (rating 2): Updated references for item 2 in Table 6 and changed C.1 from “Mandatory” to “Optional”. TSE 18361 (rating 1): Removed “is/not supported” language globally. Updated C.4 of Table 2 to correct an “otherwise” clause. Updated C.7 of Table 4 to remove SUM.ICS reference. TSE 18641 (rating 2): To address an issue with a condition not related to an ICS item, updated C.3 in Table 2; modified the prerequisite of Tables 3 and 4; and updated the status of item 23 in Table 4, modifying C.1 and adding C.14.Performed template- related editorials, including updating the copyright page to align with v2 of the DNMD. |
| 15 |  |  | p15 |  |  | 2022-06-28 | Approved by BTI on 2022-05-31. Prepared for TCRL 2022-1 publication. |
|  |  |  | p16r00–r05 |  |  | 2022-09-30 – 2022-12-08 | TSE 20594 (rating 3): Resolved inter-layer dependencies with ATT by updating the conditionals in the Role and Transport Requirements tables, introducing ILD tables toward ATT, replacing ATT references with GATT references in conditionals, and introducing GAP and SDP ILD tables. TSE 22134 (rating 3): Added missing ILD from GATT to GAP, specified in Vol 3, Part C, Section 15.2, by adding Tables 3a and 4a. Minor editorials to 3/5 and 4/5. Made editorial fixes related to the consistency checker. Removed revision history entries related to pre-initial-publication activities per the latest BTI conventions. |
| 16 |  |  | p16 |  |  | 2023-02-07 | Approved by BTI on 2022-12-28. Prepared for TCRL 2022-2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p17r00–r02 |  |  | 2023-04-16 – 2023-05-26 | TSE 22911 (rating 2): Added GATT 3/25a to the TCMT for GATT/CL/GPM/BV-07-C – -12-C and GATT/CL/GAS/BV-03-C. |
| 17 |  |  | p17 |  |  | 2023-06-29 | Approved by BTI on 2023-05-28. Prepared for TCRL 2023-1 publication. |
|  |  |  | p18r00–r05 |  |  | 2023-08-07 – 2023-10-30 | TSE 23651 (rating 2): Updated C.14 in Table 4 from Optional to Excluded. TSE 23968 (rating 2): Added 6/6 and related C.3 and updated the references for 6/4 and 6/5. TSE 23974 (rating 2): Added 7/8 and related C.3. TSE 24071 (rating 1): Replaced SUM ICS references with CORE ICS references. Updated Table 2 conditional C.2, affecting 2/3a and 2/3b; updated Table 3 conditionals C.4, C.9, and C.10, affecting 3/25, 3/26, 3/29, and 3/30; updated Table 4 conditionals C.7–C.9 and C.13, affecting 4/25, 4/26, 4/27, 4/30, and 4/31; updated Table 7 conditional C.3, affecting 7/8; and updated Table 10 conditional C.10, affecting 10/10. Updated the document to align with the latest standards. |
| 18 |  |  | p18 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p19r00 |  |  | 2024-07-16 | TSE 25250 (rating 2): Per E24891, removed the conditional from Table 1 and reset 1/1 to Optional and 1/2 to Mandatory. TSE 25735 (rating 1): Removed GATT 10/10, related C.10, and the associated ILD to ATT 4/30, which was removed by TSE 25734. |
| 19 |  |  | p19 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Elisabeth Dominguez |  |  | AT4 wireless |  |  |
| Juan Manuel Hidalgo |  |  | AT4 wireless |  |  |
| Elisa Rincón |  |  | AT4 Wireless |  |  |
| Bogdan Alexandru |  |  | Bluetooth SIG, Inc. |  |  |
| Alexandru Andreescu |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Virgil Dragomir |  |  | Bluetooth SIG, Inc. |  |  |
| Charlie Lenahan |  |  | Bluetooth SIG, Inc. |  |  |
| Jawid Mirani |  |  | Bluetooth SIG, Inc. |  |  |
| Aravind Narasimhan |  |  | Bluetooth SIG, Inc. |  |  |
| Florin Toma |  |  | Bluetooth SIG, Inc. |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Norbert Grunert |  |  | Broadcom |  |  |
| Joe Decuir |  |  | CSR |  |  |
| Magnus Sommansson |  |  | CSR |  |  |
| Sebastian Mackaie-Blanchi |  |  | Nordic Semiconductor |  |  |
