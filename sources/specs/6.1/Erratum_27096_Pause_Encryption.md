# Erratum 27096 Pause Encryption

> Source: PDF converted via PyMuPDF.

---

Errata Correction 27096: Pause Encryption should be mandatory to support with encryption
Bluetooth® Errata Correction
▪ Version: v1.0
▪ Version Date: 2025-04-08
▪ Prepared By: Core Specification Working Group
This Errata Correction applies to the following specifications (collectively, the “Source Specifications”):
• Core Specification v6.1 [8]
• Core Specification v6.0 [1]
• Core Specification (amended) v5.4 [2]
• Core Specification (amended) v5.3 [3]
• Core Specification (amended) v5.2 [4]
• Core Specification (amended) v5.1 [5]
• Core Specification (amended) v5.0 [6]
• Core Specification (amended) v4.2 [7]
Abstract:
Make the Pause Encryption LMP feature mandatory on all devices that support the Encryption LMP feature in the Core Specifications from v4.2 to v6.1.
Version History

| Version Number |  | Date |  | Comments |
| --- | --- | --- | --- | --- |
|  |  | (yyyy-mm-dd) |  |  |
| v1.0 | 2025-04-08 |  |  | Adopted by the Bluetooth SIG Board of Directors. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Clive D.W. Feather |  |  | Samsung Cambridge Solution Centre |  |  |

Use of this specification is your acknowledgement that you agree to and will comply with the following notices and disclaimers. You are advised to seek appropriate legal, engineering, and other professional advice regarding the use, interpretation, and effect of this specification.
Use of Bluetooth specifications by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG and its members, including those agreements posted on Bluetooth SIG’s website located at www.bluetooth.com. Any use of this specification by a member that is not in compliance with the applicable membership and other related agreements is prohibited and, among other things, may result in (i) termination of the applicable agreements and (ii) liability for infringement of the intellectual property rights of Bluetooth SIG and its members. This specification may provide options, because, for example, some products do not implement every portion of the specification. All content within the specification, including notes, appendices, figures, tables, message sequence charts, examples, sample data, and each option identified is intended to be within the bounds of the Scope as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”). Also, the identification of options for implementing a portion of the specification is intended to provide design flexibility without establishing, for purposes of the PCLA, that any of these options is a “technically reasonable non-infringing alternative.”
Use of this specification by anyone who is not a member of Bluetooth SIG is prohibited and is an infringement of the intellectual property rights of Bluetooth SIG and its members. The furnishing of this specification does not grant any license to any intellectual property of Bluetooth SIG or its members. THIS SPECIFICATION IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, TITLE, NON- INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, OR THAT THE CONTENT OF THIS SPECIFICATION IS FREE OF ERRORS. For the avoidance of doubt, Bluetooth SIG has not made any search or investigation as to third parties that may claim rights in or to any specifications or any intellectual property that may be required to implement any specifications and it disclaims any obligation or duty to do so.
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS SPECIFICATION AND ANY INFORMATION CONTAINED IN THIS SPECIFICATION, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF THE DAMAGES.
Products equipped with Bluetooth wireless technology ("Bluetooth Products") and their combination, operation, use, implementation, and distribution may be subject to regulatory controls under the laws and regulations of numerous countries that regulate products that use wireless non-licensed spectrum. Examples include airline regulations, telecommunications regulations, technology transfer controls, and health and safety regulations. You are solely responsible for complying with all applicable laws and regulations and for obtaining any and all required authorizations, permits, or licenses in connection with your use of this specification and development, manufacture, and distribution of Bluetooth Products. Nothing in this specification provides any information or assistance in connection with complying with applicable laws or regulations or obtaining required authorizations, permits, or licenses.
Bluetooth SIG is not required to adopt any specification or portion thereof. If this specification is not the final version adopted by Bluetooth SIG’s Board of Directors, it may not be adopted. Any specification adopted by Bluetooth SIG’s Board of Directors may be withdrawn, replaced, or modified at any time. Bluetooth SIG reserves the right to change or alter final specifications in accordance with its membership and operating agreements.
Copyright © 2025. All copyrights in the Bluetooth Specifications themselves are owned by Apple Inc., Ericsson AB, Intel Corporation, Google LLC, Lenovo (Singapore) Pte. Ltd., Microsoft Corporation, Nokia Corporation, and Toshiba Corporation. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

### 6.1 Changes to Core Specification v5.2, Volume 2, Part C: Link Manager Protocol Specification .. 10


### 7.1 Changes to Core Specification v5.1, Volume 2, Part C: Link Manager Protocol Specification .. 11


### 8.1 Changes to Core Specification v5.0, Volume 2, Part C: Link Manager Protocol Specification .. 12


### 9.1 Changes to Core Specification v4.2, Volume 2, Part C: Link Manager Protocol Specification .. 13


## 1 Drafting conventions


### 1.1 Language

Refer to and follow any terminology, language conventions, and interpretation sections of the Source Specification(s).

### 1.2 Formatting and color

The formatting and color conventions described in Table 1.1 below are used in this Errata Correction to describe the specific changes and additions to the Source Specification(s) identified on the cover page.

| Text Color | Description |
| --- | --- |
| black | Text that is unmodified from the Source Specification. |
| red | Text that is added to the Source Specification. |
| red strikethrough | Text that is deleted from the Source Specification. |
| [green bracketed text] | Comments that explain the changes to be made to the Source Specification. |
| […] | Indicates the section of the Source Specification that includes additional text that is not included in black text. |
| blue | Default color used for section numbers and headings of this document. |

Table 1.1: Color key for headings, captions, and body text

## 2 Changes to Core Specification v6.1

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v6.1.

### 2.1 Changes to Core Specification v6.1, Volume 2, Part C: Link Manager Protocol Specification


#### 2.1.1 [Modified Section] 3.5 Feature requirements

[Modify Table 3.5 as shown.]
Feature
(2) Encryption
(42) Pause Encryption
(51) Secure Simple Pairing (Controller Support)
(52) Encapsulated PDU
Table 3.5: Mandatory features

## 3 Changes to Core Specification v6.0

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v6.0.

### 3.1 Changes to Core Specification v6.0, Volume 2, Part C: Link Manager Protocol Specification


#### 3.1.1 [Modified Section] 3.5 Feature requirements

[Modify Table 3.5 as shown.]
[Note to reviewers: this change is identical to the one in v6.1.]
Feature
(2) Encryption
(42) Pause Encryption
(51) Secure Simple Pairing (Controller Support)
(52) Encapsulated PDU
Table 3.5: Mandatory features

## 4 Changes to Core Specification (amended) v5.4

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.4.

### 4.1 Changes to Core Specification v5.4, Volume 2, Part C: Link Manager Protocol Specification


#### 4.1.1 [Modified Section] 3.5.1 Devices supporting BR/EDR

[Modify Table 3.5 as shown.]
[Note to reviewers: though the section number has changed, this change is identical to the one in v6.0.]
Feature
(2) Encryption
(42) Pause Encryption
(51) Secure Simple Pairing (Controller Support)
(52) Encapsulated PDU
Table 3.5: Mandatory features

## 5 Changes to Core Specification (amended) v5.3

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.3.

### 5.1 Changes to Core Specification v5.3, Volume 2, Part C: Link Manager Protocol Specification


#### 5.1.1 [Modified Section] 3.5.1 Devices supporting BR/EDR

[Modify Table 3.5 as shown.]
[Note to reviewers: this change is identical to the one in v5.4.]
Feature
(2) Encryption
(42) Pause Encryption
(51) Secure Simple Pairing (Controller Support)
(52) Encapsulated PDU
Table 3.5: Mandatory features

## 6 Changes to Core Specification (amended) v5.2

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.2.

### 6.1 Changes to Core Specification v5.2, Volume 2, Part C: Link Manager Protocol Specification


#### 6.1.1 [Modified Section] 3.5.1 Devices supporting BR/EDR

[Modify Table 3.5 as shown.]
[Note to reviewers: this change is identical to the one in v5.4 and v5.3.]
Feature
(2) Encryption
(42) Pause Encryption
(51) Secure Simple Pairing (Controller Support)
(52) Encapsulated PDU
Table 3.5: Mandatory features

## 7 Changes to Core Specification (amended) v5.1

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.1.

### 7.1 Changes to Core Specification v5.1, Volume 2, Part C: Link Manager Protocol Specification


#### 7.1.1 [Modified Section] 3.5.1 Devices supporting BR/EDR

[Modify Table 3.5 as shown.]
Feature
(2) Encryption
(42) Pause Encryption
(51) Secure Simple Pairing (Controller Support)
(52) Encapsulated PDU
Table 3.5: Mandatory features

## 8 Changes to Core Specification (amended) v5.0

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v5.0.

### 8.1 Changes to Core Specification v5.0, Volume 2, Part C: Link Manager Protocol Specification


#### 8.1.1 [Modified Section] 3.2 Feature Definitions

[Modify the rows of Table 3.1 shown (all other rows are omitted).]

| Feature | Definition |
| --- | --- |
| Pause Encryption [Sheet 3, row 2] | When this feature bit is enabled on both sides, then the encryption pause/resume sequences shall be used. If either side does not support the Pause Encryption feature bit, then the encryption pause/resume sequences shall not be used. This feature bit shall be supported set if the “Secure Connections (Controller Support)” feature bit is set. |
| Secure Simple Pairing (Controller Support) [Sheet 5, row 5] | This feature indicates whether the Link Manager is capable of supporting the Secure Simple Pairing, Section 4.2.7. This feature shall be supported. |
| Encapsulated PDU [Sheet 5, row 7] | This feature indicates whether the device is capable of supporting the Encapsulated PDU mechanism as defined in Section 4.1.12.1. This feature shall be supported set if Secure Simple Pairing is supported. |

Table 3.1: Feature Definitions

## 9 Changes to Core Specification (amended) v4.2

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to the Core Specification v4.2.

### 9.1 Changes to Core Specification v4.2, Volume 2, Part C: Link Manager Protocol Specification


#### 9.1.1 [Modified Section] 3.2 Feature Definitions

[Modify the rows of Table 3.1 shown (all other rows are omitted).]
[Note to reviewers: though the positions of the rows in the table have changed and there is additional text in some definitions, this change is identical to the one in v5.0.]

| Feature | Definition |
| --- | --- |
| Pause Encryption [Sheet 3, row 6] | When this feature bit is enabled on both sides, then the encryption pause/resume sequences shall be used. If either side does not support the Pause Encryption feature bit, then the encryption pause/resume sequences shall not be used. This feature bit shall be supported set if the “Secure Connections (Controller Support)” feature bit is set. |
| Secure Simple Pairing (Controller Support) [Sheet 6, row 1] | This feature indicates whether the Link Manager is capable of supporting the Secure Simple Pairing, Section 4.2.7, “Secure Simple Pairing,” on page 294. This feature shall be supported. |
| Encapsulated PDU [Sheet 6, row 3] | This feature indicates whether the device is capable of supporting the Encapsulated PDU mechanism as defined in Section 4.1.12.1, “Sending an Encapsulated PDU,” on page 267. This feature shall be supported set if Secure Simple Pairing is supported. |

Table 3.1: Feature Definitions

## 10 References

[1] Bluetooth Core Specification, Version 6.0
[2] Bluetooth Core Specification (amended), Version 5.4
[3] Bluetooth Core Specification (amended), Version 5.3
[4] Bluetooth Core Specification (amended), Version 5.2
[5] Bluetooth Core Specification (amended), Version 5.1
[6] Bluetooth Core Specification (amended), Version 5.0
[7] Bluetooth Core Specification (amended), Version 4.2
[8] Bluetooth Core Specification, Version 6.1