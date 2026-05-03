# A2MP.ICS.p8

> Source: PDF converted via PyMuPDF.

---

AMP Manager Protocol (A2MP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: A2MP.ICS.p8 ▪ Revision Date: 2024-07-01 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-1
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

### 1.2 Capability statement

Table 1: General Operation

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | AMP Manager Protocol |  |  | [1] 1 |  |  | M |  |  |
| 2 |  |  | AMP Test Mode |  |  | [2] 1.2.3 |  |  | M |  |  |


## 2 References

[1] Specification of the Bluetooth System, Volume 3, Part E, Versions 3.0 or later (A2MP)
[2] Specification of the Bluetooth System, Volume 3, Part D (Test Support), Version 3.0 or later

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.0.0r0 |  |  | 2009-03-25 | First draft for review. |
| 0 |  |  | 3.0.H.0 |  |  | 2009-04-09 | Prepare for publication. |
|  |  |  | 3.0.H.0a |  |  | 2010-01-12 | Added radio buttons to PDF version. |
|  |  |  | 4.0.1r0 |  |  | 2010-12-12 | TSE 3840: Correct C.1 |
| 1 |  |  | 4.0.1 |  |  | 2011-07-15 | Prepare for publication. |
|  |  |  | 4.1.0r01 |  |  | 2013-10-08 | Template Conversion TSE 5354: Updated Table 1, C.1. |
| 2 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
|  |  |  | 4.2.0r01 |  |  | 2014-11-23 | Alicia’s review, updated status to reflect 4.2. |
| 3 |  |  | 4.2.0 |  |  | 2014-12-03 | Prepare for TCRL 2014-2 publication |
|  |  |  | 5.0.0r00 |  |  | 2016-11-08 | Revision updated for Core Specification 5.0 release |
|  |  |  | 5.0.0r01 |  |  | 2016-11-08 | Updated Template. Removed unnecessary parentheses. |
| 4 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1. |
| 5 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | p6r00 |  |  | 2019-11-14 | TSE 13024 (rating 3): Added new item 2 and conditional note C.2 to Table 1. Added “Specification of the Bluetooth System, Vol 3 Part D (Test Support), Version 3.0 or later” to references list. Updated template, moving Revision History and Contributors tables to the bottom of the document, updating Disclaimer text and Confidentiality markings to align with latest Documentation Marking Requirements, and making minor editorial fixes. |
| 6 |  |  | p6 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p7r00 |  |  | 2022-11-08 | TSE 20659 (rating 1): Updated document to the latest ICS conventions. Aligned the disclaimer with v2 of the DNMD and updated the logo in the footer (no tracked changes). |
| 7 |  |  | p7 |  |  | 2023-02-07 | Approved by BTI on 2022-12-28. Prepared for TCRL 2022-2 publication. |
|  |  |  | p8r00 |  |  | 2023-09-12 | TSE 24067 (rating 2): Removed SUM.ICS references affecting items 1/1 and 1/2. |
| 8 |  |  | p8 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Ayse Findikli |  |  | Bluetooth SIG, Inc. |  |  |
| Dave Suvak |  |  | iAnywhere |  |  |
| Joel Linsky |  |  | Qualcomm |  |  |
| Richard Lane |  |  | Stonestreet One |  |  |
| Doug Clark |  |  | Symbian |  |  |
| James Steele |  |  | Symbian |  |  |
