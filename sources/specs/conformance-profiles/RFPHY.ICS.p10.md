# RFPHY.ICS.p10

> Source: PDF converted via PyMuPDF.

---

Radio Frequency Physical Layer (RFPHY)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: RFPHY.ICS.p10 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: 2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2007–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 Capability Statement

Table 1: Bluetooth LE RF Capabilities

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE Transmitter |  |  | [1] 3 |  |  | C.1 |  |  |
| 2 |  |  | LE Receiver |  |  | [1] 4 |  |  | C.1 |  |  |
| 3 |  |  | LE Transceiver |  |  | [1] 3, 4 |  |  | C.1 |  |  |
| 4 |  |  | LE 2M PHY |  |  | [2] 3, 4 |  |  | C.2 |  |  |
| 5 |  |  | Stable Modulation Index - Transmitter |  |  | [2] 3.1.1 |  |  | C.3 |  |  |
| 6 |  |  | Stable Modulation Index - Receiver |  |  | [2] 3.1.1 |  |  | C.4 |  |  |
| 7 |  |  | LE Coded PHY |  |  | [2] 3, 4 |  |  | C.2 |  |  |
| 8 |  |  | Transmitting Constant Tone Extensions |  |  | [3] 5 |  |  | C.10 |  |  |
| 9 |  |  | 2 µs Antenna Switching During Constant Tone Extension Transmission (AoD) |  |  | [3] 5 |  |  | C.5 |  |  |
| 10 |  |  | 1 μs Antenna Switching During Constant Tone Extension Transmission (AoD) |  |  | [3] 5 |  |  | C.6 |  |  |
| 11 |  |  | 2 μs Antenna Sampling During Constant Tone Extension Reception (AoD) |  |  | [3] 5 |  |  | C.11 |  |  |
| 12 |  |  | 2 μs Antenna Switching and Sampling During Constant Tone Extension Reception (AoA) |  |  | [3] 5 |  |  | C.7 |  |  |
| 13 |  |  | 1 μs Antenna Sampling During Constant Tone Extension Reception (AoD) |  |  | [3] 5 |  |  | C.7 |  |  |
| 14 |  |  | 1 µs Antenna Switching and Sampling During Constant Tone Extension Reception (AoA) |  |  | [3] 5 |  |  | C.8 |  |  |
| 15 |  |  | Power Class 1 |  |  | [4] 4.6 |  |  | C.9 |  |  |
| 16 |  |  | Channel Sounding |  |  | [5] 1 |  |  | C.12 |  |  |

C.1: Mandatory to support at least one. Note: Selecting both RFPHY 1/1 “LE Transmitter” and RFPHY
1/2 “LE Receiver” is equivalent to selecting RFPHY 1/3 “LE Transceiver” and vice versa. C.2: Optional IF CORE 1a/50 “Controller Core v5.0 or later”, otherwise Excluded. C.3: Optional IF CORE 1a/50 “Controller Core v5.0 or later” AND (RFPHY 1/1 “LE Transmitter” OR
RFPHY 1/3 “LE Transceiver”), otherwise Excluded. C.4: Optional IF CORE 1a/50 “Controller Core v5.0 or later” AND (RFPHY 1/2 “LE Receiver” OR
RFPHY 1/3 “LE Transceiver”), otherwise Excluded. C.5: Optional IF RFPHY 1/8 “Transmitting Constant Tone Extensions”, otherwise Excluded. C.6: Optional IF RFPHY 1/9 “2 μs Antenna Switching During Constant Tone Extension Transmission
(AoD)”, otherwise Excluded. C.7: Optional IF RFPHY 1/11 “2 μs Antenna Sampling During Constant Tone Extension Reception
(AoD)”, otherwise Excluded. C.8: Mandatory IF RFPHY 1/12 “2 μs Antenna Switching and Sampling During Constant Tone Extension
Reception (AoA)” AND RFPHY 1/13 “1 μs Antenna Sampling During Constant Tone Extension Reception (AoD)”, otherwise Excluded. C.9: Optional IF (CORE 1a/50 “Controller Core v5.0 or later” OR CORE 1c/1 “Core Specification
Addendum 5”) AND (RFPHY 1/1 “LE Transmitter” OR RFPHY 1/3 “LE Transceiver”), otherwise Excluded. C.10: Optional IF CORE 1a/51 “Controller Core v5.1 or later” AND (RFPHY 1/1 “LE Transmitter” OR
RFPHY 1/3 “LE Transceiver”), otherwise Excluded.
RFPHY 1/3 “LE Transceiver”), otherwise Excluded. C.12: Optional IF CORE 1a/60 “Controller Core v6.0 or later”, otherwise Excluded.
Table 2: No longer used

### 1.3 Channel sounding capabilities

Table 3: Channel Sounding Capabilities
Prerequisite: ((RFPHY 1/1 “LE Transmitter” AND RFPHY 1/2 “LE Receiver”) OR RFPHY 1/3 “LE Transceiver”) AND RFPHY 1/16 “Channel Sounding”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | CS Initiator |  |  | [6] 4.6.41 [7] 4.3 |  |  | O |  |  |
| 2 |  |  | CS Reflector |  |  | [6] 4.6.41 [7] 4.3 |  |  | O |  |  |
| 3 |  |  | CS Antenna Array |  |  | [5] 5.3 |  |  | O |  |  |
| 4 |  |  | CS Phase-Based Measurements |  |  | [5] 6 |  |  | M |  |  |
| 5 |  |  | CS Mode-1 |  |  | [5] 3.4 |  |  | M |  |  |
| 6 |  |  | CS Mode-2 |  |  | [5] 3.4 |  |  | M |  |  |
| 7 |  |  | CS Mode-3 |  |  | [5] 3.4 |  |  | O |  |  |
| 8 |  |  | TX/SNR |  |  | [5] 3.1.3 |  |  | O |  |  |
| 9 |  |  | LE 2M 2BT |  |  | [5] 3, 4 |  |  | C.1 |  |  |

C.1: Optional IF RFPHY 1/4 “LE 2M PHY”, otherwise Excluded.

## 2 References

[1] Specification of the Bluetooth System, Physical Layer Specification (PHY) Volume 6, Part A,
Version 4.0 or later
[2] Specification of the Bluetooth System, Physical Layer Specification (PHY) Volume 6, Part A,
Version 5.0 or later
[3] Specification of the Bluetooth System, Physical Layer Specification (PHY) Volume 6, Part A,
Version 5.1 or later
[4] Specification of the Bluetooth System, Link Layer Specification (PHY) Volume 6, Part B,
Version 4.2 or later
[5] Specification of the Bluetooth System, Physical Layer Specification (PHY) Volume 6, Part A,
Version 6.0 or later
[6] Specification of the Bluetooth System, Link Layer Specification (LL) Volume 6, Part B, Version 6.0
or later
[7] Specification of the Bluetooth System, Channel Sounding Specification (CS) Volume 6, Part H,
Version 6.0 or later

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 0.5d1 |  |  | 2007-06-12 | Initial ULP RF-PHY ICS Draft |
|  |  |  | 0.5d2 |  |  | 2007-10-22 | First revision including device category mapping |
|  |  |  | 0.5d3 |  |  | 2007-10-30 | Second revision for BTI review, minor editorial changes |
|  |  |  | 0.7d1 |  |  | 2008-09-23 | Updated to be in synch with the RF PHY TS version 0.7d2. Name update from ULP to LE |
|  |  |  | 0.7d2 |  |  | 2008-09-29 | Minor editorial adjustments related to name transition |
|  |  |  | 0.9d1 |  |  | 2009-01-13 | Reference to test interface used for IUT RF PHY test added |
|  |  |  | 0.9d2 |  |  | 2009-01-14 | Edit by Magnus Sommansson: Inclusion of Table 2; Test interface capabilities. Editorial adjustment of references. |
|  |  |  | 0.9d3 |  |  | 2009-04-02 | Updated references, version submitted to BTI |
|  |  |  | 1.0d1 |  |  | 2009-10-30 | Updated references |
|  |  |  | 1.0d2 |  |  | 2009-11-12 | Editorial review |
|  |  |  | 1.0d3 |  |  | 2009-11-20 | Capability statement made independent of profile roles (Controller spec scheduled for December 2009 adoption does not contain profile role definitions) Updated references |
|  |  |  | 10d4 |  |  | 2009-12-08 | Updated references in table 2 |
| 0 |  |  | 4.0.0 |  |  | 2009-12-15 | Prepare for publication |
|  |  |  | 4.1.0r01 |  |  | 2013-11-11 | Updated revision to 4.1.0 Updated top sheet to include version 4.1 |
| 1 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
| 2 |  |  | 4.2.0 |  |  | 2014-12-04 | Prepare for TCRL 2014-2 publication |
|  |  |  | 5.0.0r00 |  |  | 2016-06-01 | Integrated changes for Core Specification 5.0 release |
|  |  |  | 5.0.0r01 |  |  | 2016-09-01 | Issue 7534: Updated “TBD” reference in Table 1. Issue 7550: Added new reference and conditionals C.3 and C.4 to Table 1. Added new reference for Bluetooth Core Specification 5.0. |
|  |  |  | 5.0.0r01 |  |  | 2016-11-14 | Updated to current template. Removed unnecessary parentheses and replaced with quotation marks. |
| 3 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.1.0r00-r01 |  |  | 2018-11-13 – 2018-11-27 | Updated revision number to 5.1.0 to align with the adoption of Core Specification version 5.1. Updated conditionals in Table 1 for Core 5.1. |
| 4 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.1.1r00–r02 |  |  | 2019-04-24– 2019-06-12 | TSE 11791 (rating 2): Updated Capability Statement table and notes and References section to address issues with the number and gain of the antennas and the length of the CTE. TSE 11957 (rating 1): Updated references section to more accurately reflect the correct Part of the spec and updated field codes to reflect resulting new numbering. |
| 5 |  |  | 5.1.1 |  |  | 2019-08-01 | Approved by BTI. Prepared for TCRL 2019-1 publication. |
|  |  |  | p6r00–r02 |  |  | 2019-09-16 – 2019-11-12 | TSE 12127 (rating 2): Updated Table 1 (items 1–3) and C.1–C.4 and C.6 conditionals to clarify roles after TCMT updates to take into account the PHYs for the IQ sample tests. Removed deprecated specs from 1:C.2–C.4 per integration review feedback. Revised document numbering convention, setting last release publication of 5.1.1 as p5; added publication number column to Revision History. |
| 6 |  |  | p6 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p7r00–r01 |  |  | 2021-03-29 – 2021-06-11 | TSE 16485 (rating 4): To address E16372 regarding Transmit Power Level for Power Class, added a reference to LL v4.2; updated table 1 with new item 15 and new conditional C.9. TSE 16697 (rating 1): Changed title of document and updated all instances of “RF PHY” and “RF-PHY” to “RFPHY” to align with new TCID structure. Minor editorials to item 14 and conditional C.8. Template-related and consistency checker editorials. |
| 7 |  |  | p7 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |
|  |  |  | p7ed2r00 |  |  | 2022-02-18 | TSE 18365 (rating 1): Updated “is/not supported” language in conditionals globally to align with new conventions. Made template-related editorials, including aligning the copyright page with v2 of the DNMD. |
|  |  |  | p7, edition 2 |  |  | 2022-03-07 | Approved by BTI on 2022-03-07. Prepared for edition 2 publication. |
|  |  |  | p8r00–r03 |  |  | 2022-03-14 – 2022-04-18 | TSE 18260 (rating 2): Updated row 8 and C.4 and added C.10 in Table 1. TSE 18347 (rating 2): Updated C.9 of Table 1. Performed template-related formatting fixes. Made consistency checker editorials. |
| 8 |  |  | p8 |  |  | 2022-06-28 | Approved by BTI on 2022-05-31. Prepared for TCRL 2022-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p9r00–r02 |  |  | 2023-08-28 – 2023-11-03 | TSE 23057 (rating 1): Removed Table 2, and related section header of the now-empty section. TSE 24078 (rating 2): Replaced SUM ICS references with CORE ICS references. Updated Table 1 conditionals C.2, C.3, C.4, C.9, C.10, and C.11, affecting items 1/4 – 1/8, 1/11, and 1/15. Updated the document to align with latest standards. |
| 9 |  |  | p9 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |
|  |  |  | p10r00–r05 |  |  | 2024-07-03 – 2024-08-20 | Incorporated CR CS Test CR r16-jorg (which _ _ _ includes Test Issues 23205, 23293, 23331, 23332, 23361, 23362, 23363, 23364, 23365, 23378, 23379, 23381, 23382, 23384, 23404, 23419, 23422, 23424, 23425, 23500, 23501, 23502, 23503, 23504, 23506, 23594, 23693, 23694, 23696, 23701, 23706, 23711, 23732, 23736, 23737, 23738, 23776, 23842, 23923, 23993, 24023, 24033, 24043, 24049, 24133, 24135, 24137, 24138, 24139, 24141, 24142, 24143, 24146, 24147, 24149, 24150, 24151, 24153, 24177, 24181, 24231, 24232, 24330, 24331, 24332, 24410, 24411, 24418, 24419, 24478, 24483, 24515, 24531, 24599, 24601, 24602, 24614, 24618, 24619, 24621, 24623, 24624, 24625, 24627, 24630, 24639, 24645, 24646, 24655, 24656, 24657, 24659, 24660, 24669, 24681, 24717, 24769, 24776, 24789, 24808, 24809, 24838, 24844, 24850, 24867, 24868, 24893, 24894, 24895, 25028, 25029, 25040, 25042, 25053, 25055, 25111, 25112, 25120, 25139, 25140, 25141, 25142, 25143, 25148, 25149, 25150, 25157, 25166, 25209, 25240, 25278, 25282, 25299, 25428, 25443, 25479, 25498, 25511, 25512, 25525, 25585, 25617, 25632). To account for the Channel Sounding feature of Core v6.0, added references to Core Vol. 6 Part B and Vol. 4 Part E, added new items 1/16–1/27 and related conditionals C.12–C.15. Incorporated Test Issue 25785. TSE 26029 (rating 2): Updated the prerequisite for Table 3 to improve test coverage. |
| 10 |  |  | p10 |  |  | 2024-09-04 | Approved by BTI on 2024-08-14. Prepared for TCRL 2024-2 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Alexandru Andreescu |  |  | Bluetooth SIG, Inc. |  |  |
| Magnus Sommansson |  |  | Qualcomm |  |  |
