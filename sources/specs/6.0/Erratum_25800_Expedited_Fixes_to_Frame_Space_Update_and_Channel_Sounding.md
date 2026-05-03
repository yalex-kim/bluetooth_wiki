# Erratum 25800 Expedited Fixes to Frame Space Update and Channel Sounding

> Source: PDF converted via PyMuPDF.

---

Errata Correction 25800: Expedited Fixes to Frame Space Update and Channel Sounding
Bluetooth® Errata Correction
▪ Version: v1.0
▪ Version Date: 2024-08-27
▪ Prepared By: Core Specification Working Group
This Errata Correction applies to the following specification:
• Bluetooth Core Specification v6.0 (“Source Specification”) [1]
Abstract:
This Errata Correction makes some corrections to the Frame Space Update and Channel Sounding features of the Source Specification.
Version History

| Version Number |  | Date |  | Comments |
| --- | --- | --- | --- | --- |
|  |  | (yyyy-mm-dd) |  |  |
| v1.0 | 2024-08-27 |  |  | Adopted by the Bluetooth SIG Board of Directors. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Clive D.W. Feather |  |  | Samsung Cambridge Solution Centre |  |  |
| Angel Polo |  |  | Broadcom Corporation |  |  |
| Pål Håland |  |  | Nordic Semiconductor ASA |  |  |
| Harish Balasubramaniam |  |  | Intel Corporation |  |  |
| Pouria Zand |  |  | Google Inc. |  |  |

Use of this specification is your acknowledgement that you agree to and will comply with the following notices and disclaimers. You are advised to seek appropriate legal, engineering, and other professional advice regarding the use, interpretation, and effect of this specification.
Use of Bluetooth specifications by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG and its members, including those agreements posted on Bluetooth SIG’s website located at www.bluetooth.com. Any use of this specification by a member that is not in compliance with the applicable membership and other related agreements is prohibited and, among other things, may result in (i) termination of the applicable agreements and (ii) liability for infringement of the intellectual property rights of Bluetooth SIG and its members. This specification may provide options, because, for example, some products do not implement every portion of the specification. All content within the specification, including notes, appendices, figures, tables, message sequence charts, examples, sample data, and each option identified is intended to be within the bounds of the Scope as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”). Also, the identification of options for implementing a portion of the specification is intended to provide design flexibility without establishing, for purposes of the PCLA, that any of these options is a “technically reasonable non-infringing alternative.”
Use of this specification by anyone who is not a member of Bluetooth SIG is prohibited and is an infringement of the intellectual property rights of Bluetooth SIG and its members. The furnishing of this specification does not grant any license to any intellectual property of Bluetooth SIG or its members. THIS SPECIFICATION IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, TITLE, NON- INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, OR THAT THE CONTENT OF THIS SPECIFICATION IS FREE OF ERRORS. For the avoidance of doubt, Bluetooth SIG has not made any search or investigation as to third parties that may claim rights in or to any specifications or any intellectual property that may be required to implement any specifications and it disclaims any obligation or duty to do so.
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS SPECIFICATION AND ANY INFORMATION CONTAINED IN THIS SPECIFICATION, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF THE DAMAGES.
Products equipped with Bluetooth wireless technology ("Bluetooth Products") and their combination, operation, use, implementation, and distribution may be subject to regulatory controls under the laws and regulations of numerous countries that regulate products that use wireless non-licensed spectrum. Examples include airline regulations, telecommunications regulations, technology transfer controls, and health and safety regulations. You are solely responsible for complying with all applicable laws and regulations and for obtaining any and all required authorizations, permits, or licenses in connection with your use of this specification and development, manufacture, and distribution of Bluetooth Products. Nothing in this specification provides any information or assistance in connection with complying with applicable laws or regulations or obtaining required authorizations, permits, or licenses.
Bluetooth SIG is not required to adopt any specification or portion thereof. If this specification is not the final version adopted by Bluetooth SIG’s Board of Directors, it may not be adopted. Any specification adopted by Bluetooth SIG’s Board of Directors may be withdrawn, replaced, or modified at any time. Bluetooth SIG reserves the right to change or alter final specifications in accordance with its membership and operating agreements.
Copyright © 2024. All copyrights in the Bluetooth Specifications themselves are owned by Apple Inc., Ericsson AB, Intel Corporation, Lenovo (Singapore) Pte. Ltd., Microsoft Corporation, Nokia Corporation, and Toshiba Corporation. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

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

## 2 Changes to Bluetooth Core Specification v6.0

This Section sets forth the specific changes and additions, using the formatting and color conventions described in Section 1.2, to Bluetooth Core Specification v6.0.

### 2.1 Changes to Bluetooth Core Specification, v6.0, Volume 4, Part E: Host Controller Interface Functional Specification


#### 2.1.1 [Modified Section] Section 7.8.151 LE Frame Space Update command

[The modified text with changes is shown below.]
[…]
If the Host issues this command with no bits set in the PHYS or the Spacing_Types parameter, then the Controller shall reject the command and return the error code Invalid HCI Command Parameters (0x12).
If the Host issues this command with a bit set in the PHYS or the Spacing_Types parameter that the Controller does not support, then the Controller shall reject the command and return the error code Unsupported Feature or Parameter Value (0x11)Invalid HCI Command Parameters (0x12).
If the Host issues this command with a bit set in the PHYS or the Spacing_Types parameter that the remote device does not support, then the Controller shall reject the command and return the error code Unsupported Remote Feature (0x1A). The Controller can determine this either because it receives a corresponding error response from the remote device or because it has checked the features supported by the remote device.
Command parameters:
[…]

### 2.2 Changes to Bluetooth Core Specification, v6.0, Volume 6, Part B: Link Layer Specification


#### 2.2.1 [Modified Section] Section 2.4.2.44 LL_CS_CAPABILITIES_REQ and LL_CS_CAPABILITIES_RSP

[The modified text with changes is shown below.]
[…]
A device that supports the RTT_Capability shall support the following section of this document:
• [Vol 6] Part H, Section 3.1
The RTT_AA_Only_N, RTT_Sounding_N, and RTT_Random_Sequence_N fields shall hold the values specified by the product manufacturer to satisfy the accuracy requirements described in [Vol 6] Part H, Section 3.1.2. If an implementation supports optional transmit and receive PHYs as indicated by the CS_SYNC_PHY_Capability field, then the correspondingrespective field shall be set to the highest “N” value derived when tested across all mandatory and optional PHYs. The value of RTT_AA_Only_N shall be non-zero. If an implementation does not support anotheran RTT type, then the correspondingrespective field shall be set to 0.
• [Vol 6] Part H, Section 2
• [Vol 6] Part H, Section 3.1
[…]

#### 2.2.2 [Modified Section] Section 4.5.10 Data PDU length management

[The modified text with changes is shown below.]
[…]
• connIntervalRequired - the value T_IFS_ACL_CP + T_MCES + min (connEffectiveMaxRxTime, ((connEffectiveMaxRxOctets × 64) + 976)).
• connIntervalUncodedMin - the value connIntervalRequired + 328.
• connIntervalCodedMin - the value connIntervalRequired + 2704.
[…]

#### 2.2.3 [Modified Section] Section 5.1.1 Connection Update procedure

[The modified text with changes is shown below.]
[…]
A Central shall not issue the LL_CONNECTION_UPDATE_IND PDU when a CS procedure or CS procedure instance repeats, as described in Section 4.5.18.1, are in progress.
The Link Layer of the Central shall determine the connInterval from the interval range given by the Host (connIntervalmin and connIntervalmax); the value chosenand shall be at least connIntervalUncodedMinRequired μs. However, if the current PHY is the LE Coded PHY and the Controller supports the LE Data Packet Length Extension feature, then the new connection interval shall be at least connIntervalCodedMin μs.
The Link Layer shall indicate to the Host the selected interval value.
[…]

#### 2.2.4 [Modified Section] Section 5.1.7.2 Responding to LL_CONNECTION_PARAM_REQ and LL_CONNECTION_PARAM_RSP PDUs

[The modified text with changes is shown below.]
[…]
• The Peripheral shall respond to an LL_CONNECTION_PARAM_REQ PDU with an LL_CONNECTION_PARAM_RSP PDU. The rules for filling in various fields of the LL_CONNECTION_PARAM_RSP PDU are the same as those for filling in various fields of the LL_CONNECTION_PARAM_REQ PDU, as described in Section 5.1.7.1. The rules for handling a received LL_CONNECTION_PARAM_RSP PDU on the Link Layer of the Central are identical to the
rules for handling a received LL_CONNECTION_PARAM_REQ PDU that are described earlier in this section.
• The Central shall respond to an LL_CONNECTION_PARAM_REQ PDU or an LL_CONNECTION_PARAM_RSP PDU with an LL_CONNECTION_UPDATE_IND PDU. The Central should try to choose a value of Interval that is a multiple of PreferredPeriodicity if the Peripheral has set the PreferredPeriodicity field of the LL_CONNECTION_PARAM_REQ or LL_CONNECTION_PARAM_RSP PDU. andThe chosen value shall be at least connIntervalUncodedMinRequired μs. However, if the current PHY is the LE Coded PHY and the Controller supports the LE Data Packet Length Extension feature, then the new connection interval shall be at least connIntervalCodedMin μs.The Central should try to pick the values of WinOffset and WinSize such that the timing of the new connection events matches one of the Offset0 to Offset5 fields of the LL_CONNECTION_PARAM_REQ PDU or the LL_CONNECTION_PARAM_RSP PDU sent by the Peripheral. The Instant field of the LL_CONNECTION_UPDATE_IND PDU is set as described in Section 5.1.1.
Once the Central issues the LL_CONNECTION_UPDATE_IND PDU, the connection parameters get updated as described in Section 5.1.1.
[…]

#### 2.2.5 [Modified Section] Section 5.1.30 Frame Space Update procedure

[The modified text with changes is shown below.]
[…]
FS_Max shall be greater than or equal to the frame space value in use. If FS_Min and FS_Max in the LL_FRAME_SPACE_REQ PDU are both less than the frame space value in use for any of the selected frame space types and PHYs, then the responding device may reject the request by sending an LL_REJECT_EXT_IND PDU with the error code set to Unsupported Feature or Parameter Value (0x11).
If the resulting frame space value causes connIntervalRequiredUncodedMin (if the current PHY is an LE Uncoded PHY) or connIntervalCodedMin (if the current PHY is the LE Coded PHY) to exceed the connection interval and the change is being done on the existing ACL connection on the PHY in use, then the responding device shall reject the request by sending an LL_REJECT_EXT_IND PDU with the error code set to Unsupported Feature or Parameter Value (0x11).
The responding device shall set the FS field of the LL_FRAME_SPACE_RSP PDU to a value between the FS_Min and FS_Max of the LL_FRAME_SPACE_REQ PDU, and should set it to the lowest value the responding device supports within that range.
[…]

## 3 References

[1] Bluetooth Core Specification, Version 6.0