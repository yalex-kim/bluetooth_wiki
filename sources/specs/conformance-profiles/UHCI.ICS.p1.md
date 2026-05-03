# UHCI.ICS.p1

> Source: PDF converted via PyMuPDF.

---

Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: UHCI.ICS.p1 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
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

### 1.2 Versions

Table 0: X.Y Versions

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42 |  |  | Upper HCI v4.2 |  |  | [1] |  |  | C.1, C.2 |  |  |
| 50 |  |  | Upper HCI v5.0 |  |  | [2] |  |  | C.1, C.3 |  |  |
| 51 |  |  | Upper HCI v5.1 |  |  | [3] |  |  | C.1, C.4 |  |  |
| 52 |  |  | Upper HCI v5.2 |  |  | [4] |  |  | C.1, C.5 |  |  |
| 53 |  |  | Upper HCI v5.3 |  |  | [5] |  |  | C.1, C.6 |  |  |
| 54 |  |  | Upper HCI v5.4 |  |  | [6] |  |  | C.1, C.7 |  |  |
| 60 |  |  | Upper HCI v6.0 |  |  | [8] |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one. C.2: Excluded IF CORE 2a/50 “Host Core v5.0 or later”, otherwise Optional. C.3: Excluded IF CORE 2a/51 “Host Core v5.1 or later”, otherwise Optional. C.4: Excluded IF CORE 2a/52 “Host Core v5.2 or later”, otherwise Optional. C.5: Excluded IF CORE 2a/53 “Host Core v5.3 or later”, otherwise Optional. C.6: Excluded IF CORE 2a/54 “Host Core v5.4 or later”, otherwise Optional. C.7: Excluded IF CORE 2a/60 “Host Core v6.0 or later”, otherwise Optional.

## 2 References

[1] Bluetooth Core Specification Volume 2, Part E, Version 4.2
[2] Bluetooth Core Specification Volume 2, Part E, Version 5.0
[3] Bluetooth Core Specification Volume 2, Part E, Version 5.1
[4] Bluetooth Core Specification Volume 4, Part E, Version 5.2
[5] Bluetooth Core Specification Volume 4, Part E, Version 5.3
[6] Bluetooth Core Specification Volume 4, Part E, Version 5.4
[7] ICS Proforma for Summary of Selected Specifications in Implementation (SUM ICS)
[8] Bluetooth Core Specification Volume 4, Part E, Version 6.0

## 3 UHCI tests

The capabilities in this ICS are not tested.

## 4 Bridge mapping between UHCI and SUM ICS

Erratum 23556 removed Vol 0, Part B “Compliance” and Vol 1, Part D “Mixing Of Specification Versions” from the Core specification and replaced them with a new Vol 0, Part D “Core Configurations”.
Erratum 23556 introduces two HCI roles, the Lower HCI and the Upper HCI role.
Table 4.1 provides a mapping from SUM ICS capabilities to UHCI capabilities. If an implementation that pre-dates the introduction of the UHCI.ICS supports HCI host capability, then it also supports the associated UHCI capability, and vice versa.

|  | UHCI ICS |  |  | Description |  |  | Corresponding SUM ICS [7] selections |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UHCI 0/42 |  |  | Upper HCI v4.2 |  |  | (SUM ICS 31/17 “Host Core v4.2” OR SUM ICS 31/18 “Host Core v4.2+HS”) AND (HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI))) |  |  |
| UHCI 0/50 |  |  | Upper HCI v5.0 |  |  | SUM ICS 31/19 “Host Core v5.0” AND (HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI))) |  |  |
| UHCI 0/51 |  |  | Upper HCI v5.1 |  |  | SUM ICS 31/20 “Host Core v5.1” AND (HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI))) |  |  |
| UHCI 0/52 |  |  | Upper HCI v5.2 |  |  | SUM ICS 31/21 “Host Core v5.2” AND (HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI))) |  |  |
| UHCI 0/53 |  |  | Upper HCI v5.3 |  |  | SUM ICS 31/22 “Host Core v5.3” AND (HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI))) |  |  |
| UHCI 0/54 |  |  | Upper HCI v5.4 |  |  | SUM ICS 31/23 “Host Core v5.4” AND (HCI 1a/2 OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND NOT PROD 2/1-6 “Controller Core Configuration”) OR ((PROD 3/1 “BR Host” OR PROD 3/2 “BR/HS Host” OR PROD 3/3 “LE Host” OR PROD 3/4 “BR/LE Host” OR PROD 3/5 “BR/HS/LE Host”) AND layer selection (HCI))) |  |  |


## 5 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p0r00–r01 |  |  | 2023-08-15 – 2024-01-29 | TSE 23691 (rating 2): In accordance with E23556, added an Upper HCI ICS to the HCI layer. |
| 0 |  |  | p0 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p1r00 |  |  | 2024-08-07 | Incorporated Test Issue 25968. Updated Table 0 to account for Core v6.0; updated the bridge mapping table. |
| 1 |  |  | p1 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Jörg Brakensiek |  |  | Bluetooth SIG, Inc. |  |  |
| Matt Canavan |  |  | Bluetooth SIG, Inc. |  |  |
