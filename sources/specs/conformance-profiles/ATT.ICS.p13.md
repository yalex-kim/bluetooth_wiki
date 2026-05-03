# ATT.ICS.p13

> Source: PDF converted via PyMuPDF.

---

Attribute Protocol (ATT)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: ATT.ICS.p13 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
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

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Attribute Protocol Client |  |  | [1] 2 |  |  | O |  |  |
| 2 |  |  | Attribute Protocol Server |  |  | [1] 2 |  |  | M |  |  |


### 1.3 Transports

Table 2: Transport Requirements

|  | Item |  |  | Transport |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Unenhanced ATT bearer over BR/EDR |  |  | [1] 2 |  |  | C.1, C.4 |  |  |
| 2 |  |  | Unenhanced ATT bearer over LE |  |  | [1] 2 |  |  | C.2, C.4 |  |  |
| 3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3a |  |  | Enhanced ATT bearer over LE |  |  | [2] 2, 3.2.11 |  |  | C.5 |  |  |
| 3b |  |  | Enhanced ATT bearer over BR/EDR |  |  | [2] 2, 3.2.11 |  |  | C.3, C.4 |  |  |

C.1: Optional IF CORE 20/2 “BR/EDR Host Layers”, otherwise Excluded. C.2: Mandatory IF CORE 20/4 “LE Host Layers” AND ATT 7/1 “LE Connections”, otherwise Excluded. C.3: Optional IF CORE 2a/52 “Host Core v5.2 or later” AND CORE 20/2 “BR/EDR Host Layers”,
otherwise Excluded. C.4: Mandatory to support at least one. C.5: Optional IF CORE 2a/52 “Host Core v5.2 or later” AND ATT 2/2 “Unenhanced ATT bearer over LE”,
otherwise Excluded. Note: In Core versions prior to v5.2, there was only one type of ATT bearer, which is now called the
“Unenhanced ATT bearer”.

### 1.4 Attribute Protocol Messages


#### 1.4.1 Attribute Client

Table 3: Attribute Protocol Client Messages Prerequisite: ATT 1/1 “Attribute Protocol Client”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Attribute Error Response |  |  | [1] 3.4.1.1 |  |  | M |  |  |
| 2 |  |  | Exchange MTU Request |  |  | [1] 3.4.2.1 |  |  | O |  |  |
| 3 |  |  | Exchange MTU Response |  |  | [1] 3.4.2.2 |  |  | C.1 |  |  |
| 4 |  |  | Find Information Request |  |  | [1] 3.4.3.1 |  |  | O |  |  |
| 5 |  |  | Find Information Response |  |  | [1] 3.4.3.2 |  |  | C.9 |  |  |
| 6 |  |  | Find by Type Value Request |  |  | [1] 3.4.3.3 |  |  | O |  |  |
| 7 |  |  | Find by Type Value Response |  |  | [1] 3.4.3.4 |  |  | C.2 |  |  |
| 8 |  |  | Read by Type Request |  |  | [1] 3.4.4.1 |  |  | O |  |  |
| 9 |  |  | Read by Type Response |  |  | [1] 3.4.4.2 |  |  | C.3 |  |  |
| 10 |  |  | Read Request |  |  | [1] 3.4.4.3 |  |  | O |  |  |
| 11 |  |  | Read Response |  |  | [1] 3.4.4.4 |  |  | C.10 |  |  |
| 12 |  |  | Read Blob Request |  |  | [1] 3.4.4.5 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 |  |  | Read Blob Response |  |  | [1] 3.4.4.6 |  |  | C.4 |  |  |
| 14 |  |  | Read Multiple Request |  |  | [1] 3.4.4.7 |  |  | O |  |  |
| 15 |  |  | Read Multiple Response |  |  | [1] 3.4.4.8 |  |  | C.5 |  |  |
| 16 |  |  | Read by Group Type Request |  |  | [1] 3.4.4.9 |  |  | O |  |  |
| 17 |  |  | Read by Group Type Response |  |  | [1] 3.4.4.10 |  |  | C.6 |  |  |
| 18 |  |  | Write Request |  |  | [1] 3.4.5.1 |  |  | O |  |  |
| 19 |  |  | Write Response |  |  | [1] 3.4.5.2 |  |  | C.7 |  |  |
| 20 |  |  | Write Command |  |  | [1] 3.4.5.3 |  |  | O |  |  |
| 21 |  |  | Signed Write Command |  |  | [1] 3.4.5.4 |  |  | O |  |  |
| 22 |  |  | Prepare Write Request |  |  | [1] 3.4.6.1 |  |  | O |  |  |
| 23 |  |  | Prepare Write Response |  |  | [1] 3.4.6.2 |  |  | C.8 |  |  |
| 24 |  |  | Execute Write Request |  |  | [1] 3.4.6.3 |  |  | C.8 |  |  |
| 25 |  |  | Execute Write Response |  |  | [1] 3.4.6.4 |  |  | C.8 |  |  |
| 26 |  |  | Handle Value Notification |  |  | [1] 3.4.7.1 |  |  | C.22 |  |  |
| 27 |  |  | Handle Value Indication |  |  | [1] 3.4.7.2 |  |  | O |  |  |
| 28 |  |  | Handle Value Confirmation |  |  | [1] 3.4.7.3 |  |  | C.24 |  |  |
| 29 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 30 |  |  | Read Multiple Variable Length Request |  |  | [2] 3.4.4.11 |  |  | C.22 |  |  |
| 31 |  |  | Read Multiple Variable Length Response |  |  | [2] 3.4.4.12 |  |  | C.26 |  |  |
| 32 |  |  | Handle Value Multiple Notification |  |  | [2] 3.4.7.4 |  |  | C.22 |  |  |

BR/EDR”, otherwise Optional. C.23: No longer used. C.24: Mandatory IF ATT 3/27 “Handle Value Indication”, otherwise Excluded. C.25: No longer used. C.26: Mandatory IF ATT 3/30 “Read Multiple Variable Length Request” OR ATT 2/3a “Enhanced ATT
bearer over LE” OR ATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Optional.

#### 1.4.2 Attribute Server

Table 4: Attribute Protocol Server Messages Prerequisite: ATT 1/2 “Attribute Protocol Server”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Attribute Error Response |  |  | [1] 3.4.1.1 |  |  | M |  |  |
| 2 |  |  | Exchange MTU Request |  |  | [1] 3.4.2.1 |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 |  |  | Exchange MTU Response |  |  | [1] 3.4.2.2 |  |  | C.19 |  |  |
| 4 |  |  | Find Information Request |  |  | [1] 3.4.3.1 |  |  | M |  |  |
| 5 |  |  | Find Information Response |  |  | [1] 3.4.3.2 |  |  | M |  |  |
| 6 |  |  | Find by Type Value Request |  |  | [1] 3.4.3.3 |  |  | M |  |  |
| 7 |  |  | Find by Type Value Response |  |  | [1] 3.4.3.4 |  |  | M |  |  |
| 8 |  |  | Read by Type Request |  |  | [1] 3.4.4.1 |  |  | M |  |  |
| 9 |  |  | Read by Type Response |  |  | [1] 3.4.4.2 |  |  | M |  |  |
| 10 |  |  | Read Request |  |  | [1] 3.4.4.3 |  |  | M |  |  |
| 11 |  |  | Read Response |  |  | [1] 3.4.4.4 |  |  | M |  |  |
| 12 |  |  | Read Blob Request |  |  | [1] 3.4.4.5 |  |  | C.6 |  |  |
| 13 |  |  | Read Blob Response |  |  | [1] 3.4.4.6 |  |  | C.1 |  |  |
| 14 |  |  | Read Multiple Request |  |  | [1] 3.4.4.7 |  |  | O |  |  |
| 15 |  |  | Read Multiple Response |  |  | [1] 3.4.4.8 |  |  | C.2 |  |  |
| 16 |  |  | Read by Group Type Request |  |  | [1] 3.4.4.9 |  |  | M |  |  |
| 17 |  |  | Read by Group Type Response |  |  | [1] 3.4.4.10 |  |  | M |  |  |
| 18 |  |  | Write Request |  |  | [1] 3.4.5.1 |  |  | C.6 |  |  |
| 19 |  |  | Write Response |  |  | [1] 3.4.5.2 |  |  | C.3 |  |  |
| 20 |  |  | Write Command |  |  | [1] 3.4.5.3 |  |  | C.6 |  |  |
| 21 |  |  | Signed Write Command |  |  | [1] 3.4.5.3 |  |  | O |  |  |
| 22 |  |  | Prepare Write Request |  |  | [1] 3.4.6.1 |  |  | C.6 |  |  |
| 23 |  |  | Prepare Write Response |  |  | [1] 3.4.6.2 |  |  | C.4 |  |  |
| 24 |  |  | Execute Write Request |  |  | [1] 3.4.6.3 |  |  | C.4 |  |  |
| 25 |  |  | Execute Write Response |  |  | [1] 3.4.6.4 |  |  | C.4 |  |  |
| 26 |  |  | Handle Value Notification |  |  | [1] 3.4.7.1 |  |  | C.6 |  |  |
| 27 |  |  | Handle Value Indication |  |  | [1] 3.4.7.2 |  |  | O |  |  |
| 28 |  |  | Handle Value Confirmation |  |  | [1] 3.4.7.3 |  |  | C.5 |  |  |
| 29– 30 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 31 |  |  | Read Multiple Variable Length Request |  |  | [2] 3.4.4.11 |  |  | C.6 |  |  |
| 32 |  |  | Read Multiple Variable Length Response |  |  | [2] 3.4.4.12 |  |  | C.16 |  |  |
| 33 |  |  | Handle Value Multiple Notification |  |  | [2] 3.4.7.4 |  |  | C.6 |  |  |

BR/EDR”, otherwise Optional. C.7–C.15: No longer used. C.16: Mandatory IF ATT 4/31 “Read Multiple Variable Length Request” OR ATT 2/3a “Enhanced ATT
bearer over LE” OR ATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise Optional. C.17–C.18: No longer used. C.19: Mandatory IF ATT 4/2 “Exchange MTU Request”, otherwise Excluded.
Table 5: No longer used

### 1.5 L2CAP requirements

Table 6: L2CAP Requirements

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Enhanced Credit Based Flow Control Mode – LE | [2] 2, 3.2.11 | C.1 | [3] L2CAP 2/48b |  |  |
| 2 | Enhanced Credit Based Flow Control Mode – BR/EDR | [2] 2, 3.2.11 | C.2 | [3] L2CAP 2/48a |  |  |

C.1: Mandatory IF ATT 2/3a “Enhanced ATT bearer over LE”, otherwise not defined. C.2: Mandatory IF ATT 2/3b “Enhanced ATT bearer over BR/EDR”, otherwise not defined.

### 1.6 GAP requirements

Table 7: GAP Requirements

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | LE Connections | [5] 4.4 | C.1 | N/A |  |  |
| 2 | Peripheral | [5] 4.4 | O | [4] GAP 5/3 OR GAP 38/3 |  |  |
| 3 | Central | [5] 4.4 | O | [4] GAP 5/4 OR GAP 38/4 |  |  |


## 2 References

[1] Specification of the Bluetooth System, Volume 3, Part F (Attribute Protocol), Version 4.0 or later
[2] Specification of the Bluetooth System, Volume 3, Part F (Attribute Protocol), Version 5.2 or later
[3] ICS Proforma for Logical Link Control and Adaptation Protocol (L2CAP)
[4] ICS Proforma for Generic Access Profile (GAP)
[5] Specification of the Bluetooth System, Volume 0, Part B (Core Configurations), Version 4.2 or later

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 4.0 R09 |  |  | 2010-06-02 | Posted for BTI |
|  |  |  | 4.0.0 R10 |  |  | 2010-06-09 | Response to BTI comments – clean version |
|  |  |  | 4.0.0 R11 |  |  | 2010-06-24 | Add Table 5 for Attribute Protocol Transport Security features |
| 0 |  |  | 4.0.0 |  |  | 2010-06-30 | Publication. |
|  |  |  | 4.0.1r0 |  |  | 2011-04-14 | TSE 4331: Add row 29 to Table 3 for Client Timeout and Table 4 for Server Timeout |
| 1 |  |  | 4.0.1 |  |  | 2011-07-15 | Prepare for publication. |
|  |  |  | 4.0.2r0 |  |  | 2011-09-12 | TSE 4263: Table 2: Clarify descriptions and add C.1 and C.2 |
|  |  |  | 4.0.2r1 |  |  | 2011-10-21 | TSE 4559 Table 1. Client is optional; server is mandatory |
|  |  |  | 4.0.2r2 |  |  | 2012-02-08 | TSE 4502: Update Table 3 |
| 2 |  |  | 4.0.2 |  |  | 2012-03-30 | Prepare for publication. |
|  |  |  | 4.1.0r01 |  |  | 2013-11-11 | Updated revision to 4.1.0 Updated top sheet to include version 4.1 |
| 3 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
|  |  |  | 4.2.0r01 |  |  | 2014-11-20 | Updated title to say “4.2” |
|  |  |  | 4.2.0r02 |  |  | 2014-11-23 | Alicia’s review, updated status to align with 4.2. |
| 4 |  |  | 4.2.0 |  |  | 2014-12-03 | Prepare for TCRL 2014-2 publication |
|  |  |  | 4.2.1r00 |  |  | 2016-03-04 | TSE 6651: Section 1.2 deleted. For Tables 3 & 4, statuses updated. For Tables 3 & 4, conditional statements added. |
| 5 |  |  | 4.2.1 |  |  | 2016-07-13 | Prepared for TCRL 2016-1 publication. |
|  |  |  | 5.0.0r00 |  |  | 2016-10-17 | TSE 7573 (erratum 5610): Added item 4/30 – Execute Write Request with no pending prepared write values |
|  |  |  | 5.0.0r01 |  |  | 2016-11-08 | Updated to current template. Removed unnecessary parentheses and replaced with quotation marks. |
| 6 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1 |
| 7 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | 5.1.1r00–r01 |  |  | 2019-04-15– 2019-05-27 | TSE 11795 (rating 1): Updated item 1 in Table 2 to reflect that there is no fixed channel on BR-EDR. |
| 8 |  |  | 5.1.1 |  |  | 2019-08-01 | Approved by BTI. Prepared for TCRL 2019-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p9r00–r04 |  |  | 2019-08-19 – 2019-11-12 | Added test groups to accommodate adoption of Core Specification V5.2 with regard to EATT CR r07. Added item 3 and note C.3 to Table 2; added items 31–33 and notes C.25–C.27 to Table 3 and updated notes C.1, C.11, C.19, and C.22; added items 31–33 and notes C.15–C.18 to Table 4 and updated notes C.6, C.8–C.12 and status of items 2 and 3; updated references section with new Core Specification. TSE 12421 (rating 1): Updated conditionals in Tables 3 and 4 to make wording more consistent with conventions. TSE 12753 (rating 1): Updated conditionals C.3 in Table 2 and C.14 in Table 4 to fix SUM.ICS references per TSE 12647. TSE 12739 (rating 2): Changed conditional C.1 for Table 2 from Mandatory to Optional. Updated .X and “Milan” references to valid numbers. Revised document numbering convention, setting last release publication of 5.1.1 as p8; added publication number column to Revision History. |
| 9 |  |  | p9 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p10r00–r02 |  |  | 2020-02-25 – 2020-11-12 | TSE 13343 (rating 2): Updated conditionals in Table 3 and updated item 3 and conditionals in Table 4 to address issue with exchange MTU features being excluded if legacy ATT protocol based on L2CAP channel with a fixed CID is supported. TSE 14883 (rating 2): Corrected C.3 in Table 2 after the additions from TSE 13111. Added items 2/3a and 2/3b to align with GATT ICS changes from TSE 13111. Added a reference to the GATT Specification. Consistency Checker fixes and minor editorials. |
| 10 |  |  | p10 |  |  | 2020-12-22 | Approved by BTI on 2020-12-03. Prepared for TCRL 2020-1 publication. |
|  |  |  | p11r00 |  |  | 2022-09-29 – 2022-09-30 | TSE 20593 (rating 3): Resolved GATT inter-layer dependencies by simplifying the EATT conditions in Table 2, removing references to GATT, and removing Table 5. TSE 20622 (rating 3): Added Table 6 for L2CAP Requirements and a reference item for the L2CAP ICS. Editorials to align with the latest ICS template. |
|  |  |  | p11r01–r03 |  |  | 2022-11-21 – 2022-12-06 | TSE 22224 (rating 3): Updated naming of 2/1, 2/2, 2/3a, and 2/3b; set 2/3 to “No longer used”; and updated Table 2’s C.2, C.3, C.4, C.5, deleted C.6, and added a note about Core versioning. Updated Table 3’s C.22, C.25, and C.26. Updated Table 4’s C.6 and C.16. Added a new GAP Requirements table as Table 7. Added references for the GAP ICS and Core v4.2. Editorials to align with the latest ICS template. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 11 |  |  | p11 |  |  | 2023-02-07 | Approved by BTI on 2022-12-28. Prepared for TCRL 2022-2 publication. |
|  |  |  | p12r00–r01 |  |  | 2023-09-25 – 2023-10-30 | TSE 24068 (rating 1): Replaced SUM ICS references with CORE ICS references. Updated Table 2 conditionals C.1–C.3 and C.5 (affecting 2/1, 2/2, 2/3a, and 2/3b) and Table 4 conditional C.14 (affecting 4/30). Updated document to align with latest standards. |
| 12 |  |  | p12 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p13r00–r01 |  |  | 2024-07-16 – 2024-07-19 | TSE 25734 (rating 1): Removed ATT 4/30 and associated C.14. Removed unused reference per consistency check. |
| 13 |  |  | p13 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Elisabeth Domiguez |  |  | AT4 wireless |  |  |
| Juan Manuel Hidalgo |  |  | AT4 wireless |  |  |
| Elisa Rincón |  |  | AT4 Wireless |  |  |
| Virgil Dragomir |  |  | Bluetooth SIG, Inc. |  |  |
| Manivannan Elangovan |  |  | Bluetooth SIG, Inc. |  |  |
| Aravind Narasimhan |  |  | Bluetooth SIG, Inc. |  |  |
| Brandon Nott |  |  | Bluetooth SIG, Inc. |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
| Norbert Grunert |  |  | Broadcom |  |  |
| Joe Decuir |  |  | CSR |  |  |
| Magnus Sommansson |  |  | CSR |  |  |
| Sebastian Mackaie-Blanchi |  |  | Nordic Semiconductor |  |  |
