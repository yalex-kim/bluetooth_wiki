# CS.ICS.p3

> Source: PDF converted via PyMuPDF.

---

Channel Sounding (CS)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: CS.ICS.p3 ▪ Revision Date: 2025-11-04 ▪ Prepared By: Core Specification Working Group ▪ Published during TCRL: TCRL.pkg101
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2024–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
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


### 2.1 Roles

Table 1: Role Requirements

| Item | Version | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | CS Initiator | [1] 4.3 | C.1 | [2] LL 1/7 |  |  |
| 2 | CS Reflector | [1] 4.3 | C.1 | [2] LL 1/8 |  |  |

C.1: Mandatory to support at least one.

### 2.2 Supported features

Table 2: Supported Features

| Item | Feature | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | Channel Sounding | [1] | M | [2] LL 9/56 |  |  |
| 2 | CS LE 2M PHY | [1] 2 | O | [2] LL 13/10 |  |  |
| 3 | CS Mode-0 | [1] 4.3.1 | M | N/A |  |  |
| 4 | CS Mode-1 | [1] 4.3.2 | M | [2] LL 13/1 |  |  |
| 5 | CS Mode-2 | [1] 4.3.3 | M | [2] LL 13/2 |  |  |
| 6 | CS Mode-3 | [1] 4.3.4 | O | [2] LL 13/3 |  |  |
| 7 | Round Trip Time | [1] 3.2 | M | N/A |  |  |
| 8 | More than one antenna element | [1] 4.7 | O | N/A |  |  |
| 9 | Multiple CS Configurations | [1] 4.2 | O | N/A |  |  |
| 10 | Procedure Repeat | [1] 2.4 | O | [2] LL 13/12 |  |  |
| 11 | Channel Selection #3c | [1] 4.1.4 | O | [2] LL 13/13 |  |  |
| 12 | Phase-based Distance Estimate with Sounding Sequence | [1] 3.3.1.1 | O | N/A |  |  |
| 13 | CS LE 2M 2BT PHY | [1] 2 | O | [3] RFPHY 3/9 |  |  |
| 14 | No longer used | N/A | N/A | N/A |  |  |
| 14a | Phase-based Normalized Attack Detector Metric – Sounding Sequence | [1] 3.5.1 | C.1 | N/A |  |  |
| 14b | Phase-based Normalized Attack Detector Metric – Random Bit Sequence | [1] 3.5.1 | C.2 | N/A |  |  |
| 15 | CS Tone Quality Indication | [1] 4.6 | O | [2] LL 9/57 |  |  |
| 16 | Amplitude-based Normalized Attack Detector Metric | [4] 3.5.4 | C.3 | N/A |  |  |

C.1: Optional IF CS 3/2 “RTT w/ Sounding Sequence, 32-bit” OR CS 3/3 “RTT w/ Sounding Sequence, 96-bit”, otherwise Excluded. C.2: Optional IF CS 3/4 “RTT w/ Random Bit Sequence, 32-bit” OR CS 3/5 “RTT w/ Random Bit Sequence, 64-bit” OR CS 3/6 “RTT w/ Random Bit Sequence, 96-bit” OR CS 3/7 “RTT w/ Random Bit Sequence, 128-bit”, otherwise Excluded. C.3: Optional IF CS 3/2 “RTT w/ Sounding Sequence, 32-bit” OR CS 3/3 “RTT w/ Sounding Sequence, 96-bit” OR CS 3/4 “RTT w/ Random Bit Sequence, 32-bit” OR CS 3/5 “RTT w/
Random Bit Sequence, 64-bit” OR CS 3/6 “RTT w/ Random Bit Sequence, 96-bit” OR CS 3/7 “RTT w/ Random Bit Sequence, 128-bit”, otherwise Excluded.
Table 3: Round Trip Time Feature
Prerequisite: CS 2/7 “Round Trip Time”

| Item | Version | Reference | Status |  | Inter-Layer |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | Dependency |  |
| 1 | RTT AA Only | [1] 3.2 | M | N/A |  |  |
| 2 | RTT w/ Sounding Sequence, 32-bit | [1] 3.3 | C.3 | N/A |  |  |
| 3 | RTT w/ Sounding Sequence, 96-bit | [1] 3.3 | O | N/A |  |  |
| 4 | RTT w/ Random Bit Sequence, 32-bit | [1] 3.4 | O | N/A |  |  |
| 5 | RTT w/ Random Bit Sequence, 64-bit | [1] 3.4 | O | N/A |  |  |
| 6 | RTT w/ Random Bit Sequence, 96-bit | [1] 3.4 | O | N/A |  |  |
| 7 | RTT w/ Random Bit Sequence, 128-bit | [1] 3.4 | O | N/A |  |  |
| 8 | CS RTT Access Address, 10 ns | [1] 3.2 | O | [2] LL 13/4 |  |  |
| 9 | CS RTT Sounding Sequence, 10 ns | [1] 3.3 | C.1 | [2] LL 13/6 |  |  |
| 10 | CS RTT Random Payload, 10 ns | [1] 3.4 | C.2 | [2] LL 13/8 |  |  |

C.1: Optional IF CS 3/2 “RTT w/ Sounding Sequence, 32-bit” OR CS 3/3 “RTT w/ Sounding Sequence, 96-bit”, otherwise not defined. C.2: Optional IF CS 3/4 “RTT w/ Random Bit Sequence, 32-bit” OR CS 3/5 “RTT w/ Random Bit Sequence, 64-bit” OR CS 3/6 “RTT w/ Random Bit Sequence, 96-bit” OR CS 3/7 “RTT w/ Random Bit Sequence, 128-bit”, otherwise not defined. C.3: Mandatory IF CS 2/12 “Phase-based Distance Estimate with Sounding Sequence”, otherwise Optional.
Table 4: Antenna Configuration
Prerequisite: CS 2/8 “More than one antenna element”

|  | Item |  |  | Version |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 2 antennae |  |  | [1] 4.7 |  |  | C.1 |  |  |
| 2 |  |  | 3 antennae |  |  | [1] 4.7 |  |  | C.1 |  |  |
| 3 |  |  | 4 antennae |  |  | [1] 4.7 |  |  | C.1 |  |  |

C.1: Mandatory to support one and only one.

## 3 References

[1] Specification of the Bluetooth System, Volume 6, Part H (Channel Sounding), Version 6.0 or later
[2] ICS Proforma for Link Layer (LL)
[3] ICS Proforma for Radio Frequency Physical Layer (RFPHY)
[4] Specification of the Bluetooth System, Volume 6, Part H (Channel Sounding), Version 6.2 or later

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | p0 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |
|  |  |  | p1r00–r03 |  |  | 2024-10-30 – 2024-12-13 | TSE 26157 (rating 1): Corrected an ICS item number in the prerequisite and in C.3 for Table 3 and corrected an ICS item number in the prerequisite and fixed the table title for Table 4. TSE 26238 (rating 2): Split 2/14 into 2/14a and 2/14b to distinguish Sounding Sequence and Random Bit Sequence. TSE 26691: Per E26162, updated “antennas” to “antennae” in 4/1, 4/2, and 4/3. |
| 1 |  |  | p1 |  |  | 2025-02-18 | Approved by BTI on 2024-12-26. Prepared for TCRL 2025-1 publication. |
|  |  |  | p2r00–r01 |  |  | 2025-02-10 – 2025-03-24 | TSE 26663 (rating 1): Added LL ILDs for 3/8, 3/9, and 3/10. |
| 2 |  |  | p2 |  |  | 2025-05-06 | Approved by BTI on 2025-04-16. Prepared for TCRL 2025-2 publication. |
|  |  |  | p3r00–p01 |  |  | 2025-07-08 – 2025-08-04 | TSE 27907 (rating 4): To support the CSAA feature added for Core v6.2, added 2/16 and associated conditional C.3. |
| 3 |  |  | p3 |  |  | 2025-11-04 | Approved by BTI on 2025-10-05. Prepared for TCRL pkg101 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Matt Canavan |  |  | Bluetooth SIG, Inc. |  |  |
| Gene Chang |  |  | Bluetooth SIG, Inc. |  |  |
