# IAL.ICS.p3

> Source: PDF converted via PyMuPDF.

---

Isochronous Adaptation Layer (IAL)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: IAL.ICS.p3 ▪ Revision Date: 2025-05-06 ▪ Prepared By: Core Specification Working Group ▪ Published during TCRL: TCRL.2025-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2019–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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

### 1.3 Supported features

Table 1: Supported Features

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Segmentable Framed Data Traffic |  |  | [1] 2.2 |  |  | M |  |  |
| 2 |  |  | Unframed Data Traffic |  |  | [1] 2.1 |  |  | M |  |  |
| 3 |  |  | Connected Isochronous Stream Adaptation |  |  | [1] 2 |  |  | O |  |  |
| 4 |  |  | Broadcast Isochronous Stream Adaptation |  |  | [1] 2 |  |  | O |  |  |
| 5 |  |  | Synchronized Receiver Adaptation |  |  | [1] 2 |  |  | O |  |  |
| 6 |  |  | Unsegmented Framed Data Traffic |  |  | [2] 2.2 |  |  | O |  |  |


### 1.4 LL requirements

Table 2: LL Requirements

| Item | Capability | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Connected Isochronous Stream - Central | [1] 2 | C.1 | [3] LL 9/31 |  |  |
| 2 | Connected Isochronous Stream - Peripheral | [1] 2 | C.1 | [3] LL 9/32 |  |  |
| 3 | Isochronous Broadcaster | [1] 2 | C.2 | [3] LL 9/33 |  |  |
| 4 | Synchronized Receiver | [1] 2 | C.3 | [3] LL 9/34 |  |  |
| 5 | Unsegmented Framed Mode | [1] 2.2 | C.4 | [3] LL 9/53 |  |  |

C.1: Mandatory to support at least one IF IAL 1/3 “Connected Isochronous Stream Adaptation”, otherwise not defined. C.2: Mandatory IF IAL 1/4 “Broadcast Isochronous Stream Adaptation”, otherwise not defined. C.3: Mandatory IF IAL 1/5 “Synchronized Receiver Adaptation”, otherwise not defined. C.4: Mandatory IF IAL 1/6 “Unsegmented Framed Data Traffic”, otherwise not defined.

## 2 References

[1] Specification of the Bluetooth System, Volume 6, Part G (Isochronous Adaptation Layer), Version 5.2
or later
[2] Specification for the Bluetooth System, Volume 6, Part G (Isochronous Adaptation Later), Version 6.0
or later
[3] ICS Proforma for Link Layer (LL)

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p1r00–r04 |  |  | 2020-02-21 – 2021-06-11 | TSE 13553 (rating 1): Updated Table 1 C.1 conditional to properly reference LL feature Connected Isochronous Stream Slave as LL 9/32. TSE 15449 (rating 1): Updated instances of “Master” to “Central” and “Slave” to “Peripheral”. Template-related and consistency checker editorials. |
| 1 |  |  | p1 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |
|  |  |  | p2r00–r04 |  |  | 2024-05-20 – 2024-07-31 | Incorporated changes from Enhancements for ISOAL TEST CR r12: In _ _ _ _ _ Table 1, updated the Capability for Item 1 and added Item 6 and C.4. Updated the list of references. Incorporated integration review feedback and made template-related and consistency checker editorial updates. |
| 2 |  |  | p2 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |
|  |  |  | p3r00 |  |  | 2025-01-30 | TSE 26827 (rating 2): Updated 1/3–1/6 to Optional and removed all conditionals. Added new Table 2 to cover LL ICS items through ILDs. Added a reference to the LL ICS to the references list. |
| 3 |  |  | p3 |  |  | 2025-05-06 | Approved by BTI on 2025-04-16. Prepared for TCRL 2025-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
| Tharon Hall |  |  | Bluetooth SIG, Inc. |  |  |
| Fabien Duvoux |  |  | Ellisys |  |  |
| Kyle Penri-Williams |  |  | Ellisys |  |  |
| Clement Vacheron |  |  | Ellisys |  |  |
| Magnus Sommansson |  |  | Qualcomm Technologies International, Ltd. |  |  |
