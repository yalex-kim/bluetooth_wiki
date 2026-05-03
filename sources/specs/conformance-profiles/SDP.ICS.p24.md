# SDP.ICS.p24

> Source: PDF converted via PyMuPDF.

---

Service Discovery Protocol (SDP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: SDP.ICS.p24 ▪ Revision Date: 2024-07-01 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-1
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2003–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Roles

Table 1b: Role Requirements

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Server |  |  | [1] 2.1 |  |  | C.1 |  |  |
| 2 |  |  | Client |  |  | [1] 2.1 |  |  | C.1 |  |  |

C.1: Mandatory to support at least one.

### 1.3 SDP Server role

Table 1: No longer used

#### 1.3.1 Service Search Response PDU

Table 2: Service Search Response
Prerequisite: SDP 1b/1 “Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service Search Response |  |  | [1] 4.5.2 |  |  | M |  |  |
| 2 |  |  | Generates continuation state in Service Search Response |  |  | [1] 4.3, 4.5.2 |  |  | O |  |  |
| 3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |

Table 3: No longer used

#### 1.3.2 Service Attribute Response PDU

Table 4: Service Attribute Response
Prerequisite: SDP 1b/1 “Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service Attribute Response |  |  | [1] 4.6.2 |  |  | M |  |  |
| 2 |  |  | Generates continuation state in Service Attribute Response |  |  | [1] 4.3, 4.6.2 |  |  | O |  |  |
| 3 |  |  | Service Attribute Response with AdditionalProtocolDescriptorList attribute |  |  | [1] 4.5.2, 5.1.6 |  |  | O |  |  |

Table 5: No longer used

#### 1.3.3 Service Search Attribute Response PDU

Table 6: Service Search Attribute Response
Prerequisite: SDP 1b/1 “Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service Search Attribute Response |  |  | [1] 4.7.2 |  |  | M |  |  |
| 2 |  |  | Generates continuation state in Service Search Attribute Response |  |  | [1] 4.3, 4.7.2 |  |  | O |  |  |
| 3 |  |  | Service Search Attribute Response with AdditionalProtocolDescriptorList attribute |  |  | [1] 4.7.2, 5.1.6 |  |  | O |  |  |

Table 7: Invalid Service Search Attribute Request
Prerequisite: SDP 1b/1 “Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Error response to Service Search Attribute Request |  |  | [1] 4.4 |  |  | M |  |  |


#### 1.3.4 Service Browsing

Table 8: Service Browsing
Prerequisite: SDP 1b/1 “Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Browsing, using SDP ServiceSearchRequest and _ SDP ServiceAttributeRequest _ |  |  | [1] 2.6, 4.5, 4.6 |  |  | O |  |  |
| 2 |  |  | Browsing, using SDP ServiceSearchAttributeRequest _ |  |  | [1] 2.6, 4.7 |  |  | O |  |  |


#### 1.3.5 Attributes

Table 9: Attributes Present in IUT
Prerequisite: SDP 1b/1 “Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | ServiceID |  |  | [1] 5.1.4 |  |  | O |  |  |
| 2 |  |  | ProtocolDescriptorList |  |  | [1] 5.1.5 |  |  | O |  |  |
| 3 |  |  | ServiceRecordState |  |  | [1] 5.1.3 |  |  | O |  |  |
| 4 |  |  | ServiceInfoTimeToLive |  |  | [1] 5.1.9 |  |  | O |  |  |
| 5 |  |  | BrowseGroupList |  |  | [1] 5.1.7 |  |  | O |  |  |
| 6 |  |  | LanguageBaseAttributeIdList |  |  | [1] 5.1.8 |  |  | O |  |  |
| 7 |  |  | ServiceAvailability |  |  | [1] 5.1.10 |  |  | O |  |  |
| 8 |  |  | IconURL |  |  | [1] 5.1.14 |  |  | O |  |  |
| 9 |  |  | ServiceName |  |  | [1] 5.1.15 |  |  | O |  |  |
| 10 |  |  | ServiceDescription |  |  | [1] 5.1.16 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 |  |  | ProviderName |  |  | [1] 5.1.17 |  |  | O |  |  |
| 12 |  |  | VersionNumberList |  |  | [1] 5.2.3 |  |  | O |  |  |
| 13 |  |  | ServiceDataBaseState |  |  | [1] 5.2.4 |  |  | O |  |  |
| 14 |  |  | BluetoothProfileDescriptorList |  |  | [1] 5.1.11 |  |  | O |  |  |
| 15 |  |  | DocumentationURL |  |  | [1] 5.1.12 |  |  | O |  |  |
| 16 |  |  | ClientExecutableURL |  |  | [1] 5.1.13 |  |  | O |  |  |
| 17 |  |  | AdditionalProtocolDescriptorList |  |  | [1] 5.1.6 |  |  | C.1 |  |  |
| 18 |  |  | ServiceRecordHandle |  |  | [1] 5.1.1 |  |  | M |  |  |
| 19 |  |  | ServiceClassIDList |  |  | [1] 5.1.2 |  |  | M |  |  |

C.1: Optional IF SDP 9/2 “ProtocolDescriptorList”, otherwise Excluded.

### 1.4 SDP Client role


#### 1.4.1 Service Attribute Request PDU

Table 10: Service Attribute Request
Prerequisite: SDP 1b/2 “Client”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service Attribute Request |  |  | [1] 4.6.1 |  |  | O |  |  |


#### 1.4.2 Service Search Attribute Request PDU

Table 11: Service Search Attribute Request
Prerequisite: SDP 1b/2 “Client”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Service Search Attribute Request |  |  | [1] 4.7.1 |  |  | O |  |  |


## 2 References

[1] Specification of the Bluetooth System, Service Discovery Protocol (SDP) Volume 3, Part B

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | D5r3 |  |  | 2003-11-05 | Original Release |
|  |  |  | D10R00 |  |  | 2004-03-10 | Re-partitioned to match Main Specification Volume/Part partitioning. TSE 555 incorporated. |
|  |  |  | D10R01 |  |  | 2004-03-11 | Editorial changes |
|  |  |  | D12r02 |  |  | 2004-03-23 | Editorial changes. Changed reference and document numbering to D12 to reflect applicable Bluetooth version. |
|  |  |  | D12r03 |  |  | 2004-03-25 | Editorial changes |
| 10 |  |  | 1.2.1 |  |  | 2004-03-29 | Changed document number and revision number to conform to legacy system. Added Disclaimer and Copyright Notice. |
| 11 |  |  | 1.2.2 |  |  | 2006-06-20 | Changed part number, prepare for publication. |
| 12 |  |  | 1.2.3r0 |  |  | 2006-12-05 | Editorial update |
| 13 |  |  | 2.1.E.0 |  |  | 2006-12-29 | Change doc identifier to apply to v1.2 and later specifications |
| 14 |  |  | 2.1.E.1 |  |  | 2007-08-14 | TSE 2000: Add rows to Tables 4 and 6 to SDP 2.0- TSE 2001: Add rows to Tables 4 and 6 to SDP 2.1 Add Status of O to Tables 4 and 6 |
| 15 |  |  | 2.1.E.2 |  |  | 2008-04-30 | TSE 2474: Table 2/1 Conditional |
|  |  |  | 2.1.E.3r0 |  |  | 2008-08-21 | TSE 2654: Added three attributes to Table 9 |
|  |  |  | 2.1.E.3r1 |  |  | 2008-11-19 | Added “O” as status to new items |
| 16 |  |  | 2.1.E.3 |  |  | 2008-12-11 | Prepare for publication. |
|  |  |  | 4.0.0r0 |  |  | 2011-12-14 | TSE 4472: Change 9/17 from O to C.1. Add conditional statement to Table 9 |
| 17 |  |  | 4.0.0 |  |  | 2012-03-30 | Updated text in Section 1.1.1. Prepare for publication. |
|  |  |  | 4.1.0r01 |  |  | 2013-11-11 | Updated revision to 4.1.0 Updated top sheet to include version 4.1 |
| 18 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.1.0r01 |  |  | 2014-01-22 | Updated Disclaimer and Copyright to 2014 |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
|  |  |  | 4.2.0r01 |  |  | 2014-11-20 | Updated title to include 4.2 |
| 19 |  |  | 4.2.0 |  |  | 2014-12-05 | Prepare for TCRL 2014-2 publication |
|  |  |  | 5.0.0r00 |  |  | 2016-11-08 | Revision updated for Core Specification 5.0 release |
|  |  |  | 5.0.0r01 |  |  | 2016-11-08 | Updated Template. Removed unnecessary parentheses. |
| 20 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 21 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | p22r00 |  |  | 2019-11-27 | Revised document numbering convention, setting last release publication of 5.1.0 as p21; added publication number column to Revision History. |
| 22 |  |  | p22 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p22ed2r00 |  |  | 2022-07-19 | TSE 19145 (rating 1): Updated to align with current ICS conventions/template. Removed Support columns. |
|  |  |  | p22 edition 2 |  |  | 2022-08-23 | Approved by BTI on 2022-08-22. Prepared for edition 2 publication. |
|  |  |  | p23r00–r01 |  |  | 2022-10-03 – 2022-10-28 | TSE 20423 (rating 2): Updated prerequisites and references throughout the ICS and aligned item descriptions with the latest ICS conventions. |
| 23 |  |  | p23 |  |  | 2023-02-07 | Approved by BTI on 2022-12-28. Prepared for TCRL 2022-2 publication. |
|  |  |  | p24r00–r01 |  |  | 2023-09-08 – 2023-10-10 | TSE 24193 (rating 4): Overhauled the SDP ICS to add command support for the Client role. Removed irrelevant ICS items: Tables 1, 3, and 5 (all mandatory if SDP 1b/1). |
| 24 |  |  | p24 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Alicia Courtney |  |  | Broadcom LTD |  |  |
