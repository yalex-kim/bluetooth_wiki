# RF.ICS.p22

> Source: PDF converted via PyMuPDF.

---

Radio Frequency (RF)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: RF.ICS.p22 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
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

### 1.2 Capability statement

Table 1: RF Capabilities

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Power Class 1 |  |  | [1] 3 |  |  | C.5 |  |  |
| 2 |  |  | Power Class 2 |  |  | [1] 3 |  |  | C.5 |  |  |
| 3 |  |  | Power Class 3 |  |  | [1] 3 |  |  | C.5 |  |  |
| 4 |  |  | Power Control |  |  | [1] 3 |  |  | C.1 |  |  |
| 5 |  |  | 1-slot packets supported |  |  | [2] 6.5 |  |  | M |  |  |
| 6 |  |  | 3-slot packets supported |  |  | [2] 6.5 |  |  | O |  |  |
| 7 |  |  | 5-slot packets supported |  |  | [2] 6.5 |  |  | O |  |  |
| 8 |  |  | 79 Channels |  |  | [1] 2 |  |  | M |  |  |
| 9 |  |  | Support for GFSK modulation |  |  | [1] 3.1 |  |  | M |  |  |
| 10 |  |  | Support for π/4-DQPSK modulation |  |  | [1] 3.2 |  |  | O |  |  |
| 11 |  |  | Support for 8DPSK modulation |  |  | [1] 3.2 |  |  | C.3 |  |  |
| 12 |  |  | Enhanced Power Control |  |  | [1] 3 |  |  | C.4 |  |  |

C.1: Mandatory IF RF 1/1 “Power Class 1”, otherwise Optional IF RF 1/2 “Power Class 2” OR RF 1/3
“Power Class 3”, otherwise Excluded. C.2: No longer used. C.3: Optional IF RF 1/10 “Support for π/4-DQPSK modulation”, otherwise Excluded. C.4: Optional IF RF 1/4 “Power Control”, otherwise Excluded. C.5: Mandatory to support at least one.

## 2 References

[1] Specification of the Bluetooth System, Radio (RF) Volume 2, Part A
[2] Specification of the Bluetooth System, Baseband (BB) Volume 2, Part B

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | D5r3 |  |  | 2003-11-05 | Original Release |
|  |  |  | D10R00 |  |  | 2004-03-10 | Re-partitioned to match Main Specification Volume/Part partitioning. |
|  |  |  | D10R01 |  |  | 2004-03-11 | Editorial changes |
|  |  |  | D12r02 |  |  | 2004-03-25 | Editorial changes. Changed reference and document numbering to D12 to reflect applicable Bluetooth version. |
|  |  |  | 1.2.1 |  |  | 2004-03-29 | Changed document number and revision number to conform with legacy system. Added Disclaimer and Copyright Notice. |
|  |  |  | 1.2.1r01 |  |  | 2004-10-06 | Added EDR material. |
|  |  |  | 2.0.E.0 Draft |  |  | 2004-10-22 | Updated to reflect latest Conformance Requirements. |
| 10 |  |  | 2.0.E.0 |  |  | 2004-11-04 | First version for 1.2/2.0/2.0 + EDR available for qualification |
|  |  |  | 2.1.E.0r0 |  |  | 2006-12-13 | Editorial updates; changes to Conditional Statements to accommodate the introduction of the 2.1 and 2.1+EDR Specification. |
|  |  |  | 2.1.E.0r1 |  |  | 2006-12-26 | Editorial changes. |
| 11 |  |  | 2.1.E.0 |  |  | 2006-12-29 | Prepare for publication. |
|  |  |  | 2.1.E.1r0 |  |  | 2009-02-12 | Add new item for enhanced power control feature |
|  |  |  | 2.1.E.1r1 |  |  | 2009-03-25 | Added EDR constraint to the C.2, C.3 conditionals, and fixed the ( on C.3 |
| 12 |  |  | 3.0.H.0 |  |  | 2009-04-21 | TSE 2744: add two more rows for each of the power classes in Table 1. Prepare for publication. |
| 13 |  |  | 3.0.H.1 |  |  | 2009-08-12 | TSE 2938. Change Table 1 footnote C.4 from 1/2 to 1/4 |
|  |  |  | 4.0.2r0 |  |  | 2010-12-12 | TSE 4064: Table 1, Footnote C.2 and C.3 |
| 14 |  |  | 4.0.2 |  |  | 2011-07-18 | Prepare for publication. |
|  |  |  | 4.1.0r01 |  |  | 2013-11-11 | Updated revision to 4.1.0 Updated top sheet to include version 4.1 |
| 15 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
|  |  |  | 4.2.0r01 |  |  | 2014-11-24 | Review by Alicia Minor editorial changes |
| 16 |  |  | 4.2.0 |  |  | 2014-12-04 | Corrected conditional in 1/4 to C.1. Prepared for TCRL 2014-2 publication |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 4.2.1r00 |  |  | 2015-10-14 | TSE 6650: Updated conditionals in Table 1 to reflect omitted changes from TSE 4597. Additional editorial changes made to bring document in line with current conventions. TSE 6506: Reworded C.5 of Table 1 to allow support for more than one power class. |
| 17 |  |  | 4.2.1 |  |  | 2015-12-22 | Prepared for TCRL 2015-2 publication |
|  |  |  | 5.0.0r00 |  |  | 2016-11-08 | Revision updated for Core Specification 5.0 release |
|  |  |  | 5.0.0r01 |  |  | 2016-11-08 | Updated Template. Removed unnecessary parentheses. |
| 18 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1 |
| 19 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | p20r00 |  |  | 2019-11-12 | Revised document numbering convention, setting last release publication of 5.1.0 as p19; added Publication Number column to Revision History. Moved Revision History and Contributors tables to end of doc. Updated Documentation Disclaimer and Confidentiality Markers to align with updated Documentation Marking Requirements. Made minor editorial changes. |
| 20 |  |  | p20 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p20ed2r00 |  |  | 2022-07-19 | TSE 19146 (rating 1): Updated to align with current ICS conventions/template. Removed Support and Values Allowed/Supported columns. Removed deprecated SUM ICS references in C.2–C.4. |
|  |  |  | p20 edition 2 |  |  | 2022-08-23 | Approved by BTI on 2022-08-22. Prepared for edition 2 publication. |
|  |  |  | p21r00–r01 |  |  | 2023-09-26 – 2023-10-23 | TSE 24077 (rating 2): Replaced SUM ICS references with CORE ICS references. In Table 1, deleted C.2 and updated C.3 (affecting 1/11) and updated the status of 1/10 to Optional. Updated the document to align with latest standards. |
| 21 |  |  | p21 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p22r00–r01 |  |  | 2024-07-16 – 2024-07-21 | TSE 25655 (rating 1): Corrected RF 1/10 to “Support for π/4-DQPSK modulation” to align with the Core spec. Incorporated integration review feedback. |
| 22 |  |  | p22 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Magnus Sommansson |  |  | Qualcomm Technologies International, Ltd. |  |  |
| Totti Huang |  |  | SGS |  |  |
