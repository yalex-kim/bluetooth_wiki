# MAP.TS .p15

> Source: PDF converted via PyMuPDF.

---

Message Access Profile (MAP)
Bluetooth® Test Suite
▪ Revision: MAP.TS.p15 ▪ Revision Date: 2024-07-01 ▪ Prepared By: Audio, Telephony, and Automotive Working Group ▪ Published during TCRL: TCRL.2024-1
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2008–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Message Access Profile (MAP) Specification, with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers’ Bluetooth devices.

## 2 References, definitions, and abbreviations


### 2.1 References

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1], [2], and [3].
[1] Bluetooth Core Specification, Version 2.1+EDR or later
[2] Test Strategy and Terminology Overview
[3] Message Access Profile Specification
[4] ICS Proforma for Message Access Profile (MAP)
[5] Generic Object Exchange Profile Test Suite, GOEP.TS
[6] Infrared Data Association, IrDA Object Exchange Protocol (IrOBEX), Version 1.5 or later
[7] SDP Test Suite, SDP.TS
[8] IXIT Proforma for Message Access Profile (MAP)

### 2.2 Definitions

In this Bluetooth document, the definitions from [1], [2], and [3] apply.

### 2.3 Acronyms and abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1], [2], and [3] apply.

|  | Acronyms or abbreviations |  |  | Definition |  |
| --- | --- | --- | --- | --- | --- |
| IM |  |  | Instant Messaging |  |  |
| MAS |  |  | Message Access Service |  |  |
| MMS |  |  | Multimedia Message Service |  |  |
| MNS |  |  | Message Notification Service |  |  |
| SMS |  |  | Short Message Service |  |  |

Table 2.1: Acronyms and abbreviations

## 3 Test Suite Structure (TSS)


### 3.1 Test strategy

This document describes the test procedures for testing of MAP. MAP is dependent upon the Generic Object Exchange Profile (GOEP) and tests from the GOEP Test Suite are required to test parts of the MAP functionality. The GOEP tests are referred to in test case mapping table within this document.
Whenever a test case defined by this document requires functionality from external networks, such as receiving or sending messages, this can be performed by a real network or a suitable network simulator.

### 3.2 Test groups

The following test groups have been defined:
• Generic SDP Integrated Tests
• Session Management
• Notification Registration
• Browsing
• Delete
• Uploading
• Notification
• Instance Information
• MapSupportedFeatures Bits
• Message Forwarding Message Handling

## 4 Test cases


### 4.1 Introduction


#### 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [2]. The convention used here is: <spec abbreviation>/<IUT role>/<class>/<feat>/<func>/<subfunc>/<cap>/<xx>-<nn>-<y>.
Testing of this specification includes a set of tests from the GOEP Test Suite [5]; when used, the GOEP tests are referred to in the TCMT per the following convention: <spec abbreviation>/<IUT role>/GOEP/<GOEP TC Identifier>.
Additionally, testing of this specification includes tests from the SDP Test Suite [7] referred to as Generic SDP Integrated Tests (GSIT); when used, the GSIT tests are referred to through a TCID string using the following convention: <spec abbreviation>/<IUT role>/<GSIT test group>/<GSIT class>/<xx>-<nn>-<y>.

|  | Identifier Abbreviation |  |  | Spec Identifier <spec abbreviation> |  |
| --- | --- | --- | --- | --- | --- |
| MAP |  |  | Message Access Profile |  |  |
|  | Identifier Abbreviation |  |  | Role Identifier <IUT role> |  |
| MCE |  |  | Message Client Equipment |  |  |
| MSE |  |  | Message Server Equipment |  |  |
|  | Identifier Abbreviation |  |  | Reference Identifier <GSIT test group> |  |
| CGSIT |  |  | Client Generic SDP Integrated Tests |  |  |
| SGSIT |  |  | Server Generic SDP Integrated Tests |  |  |
|  | Identifier Abbreviation |  |  | Reference Identifier <GSIT class> |  |
| ATTR |  |  | Attribute |  |  |
| OFFS |  |  | Attribute ID Offset String |  |  |
| SERR |  |  | Service Record |  |  |
| SFC |  |  | SDP Future Compatibility |  |  |
|  | Identifier Abbreviation |  |  | Feature Identifier <feat> |  |
| GOEP |  |  | Generic Object Exchange Profile |  |  |
| MSM |  |  | MAP Session Management functions |  |  |
| MNR |  |  | MAP Notification Registration functions |  |  |
| MMN |  |  | MAP Notification Feature functions |  |  |
| MMB |  |  | MAP Browsing Feature functions |  |  |
| MMD |  |  | MAP Delete Feature functions |  |  |
| MMU |  |  | MAP Upload Feature functions |  |  |
| MMI |  |  | MAP Instance Information Feature functions |  |  |
| MFB |  |  | MAP Features Bits Feature functions |  |  |
| MFMH |  |  | Message Forwarding Message Handling |  |  |

Table 4.1: MAP TC feature naming conventions

#### 4.1.2 Conformance

When conformance is claimed for a particular specification, all capabilities are to be supported in the specified manner. The mandated tests from this Test Suite depend on the capabilities to which conformance is claimed.
The Bluetooth Qualification Program may employ tests to verify implementation robustness. The level of implementation robustness that is verified varies from one specification to another and may be revised for cause based on interoperability issues found in the market.
Such tests may verify:
• That claimed capabilities may be used in any order and any number of repetitions not excluded by the specification
• That capabilities enabled by the implementations are sustained over durations expected by the use case
• That the implementation gracefully handles any quantity of data expected by the use case
• That in cases where more than one valid interpretation of the specification exists, the implementation complies with at least one interpretation and gracefully handles other interpretations
• That the implementation is immune to attempted security exploits
A single execution of each of the required tests is required to constitute a Pass verdict. However, it is noted that to provide a foundation for interoperability, it is necessary that a qualified implementation consistently and repeatedly pass any of the applicable tests.
In any case, where a member finds an issue with the test plan generated by the Bluetooth SIG qualification tool, with the test case as described in the Test Suite, or with the test system utilized, the member is required to notify the responsible party via an erratum request such that the issue may be addressed.

#### 4.1.3 Pass/Fail verdict conventions

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.
The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.

### 4.2 Generic SDP Integrated Tests


#### 4.2.1 Server Generic SDP Integrated Tests


##### 4.2.1.1 Message Access Service on the MSE device

Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [7] using Table 4.2 below as input:

| TCID |  |  | Reference | Attribute ID name | Attribute ID definition source (Universal, Profile) | Value/secondary value |  |  |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  |  |  |  |  | defined) |  |
|  | MAP/MSE/SGSIT/SERR/BV-01-C |  | [3] 7.1.1 | ServiceClassIDList | Universal | “Message Access Server” (UUID) |  |  | Present for MSE | Present for MSE |  |
|  | [Service record GSIT – MAP MSE |  |  |  |  |  |  |  |  |  |  |
|  | Message Access Service] |  |  |  |  |  |  |  |  |  |  |
| MAP/MSE/SGSIT/ATTR/BV-01-C [Attribute GSIT – Protocol Descriptor List] | MAP/MSE/SGSIT/ATTR/BV-01-C |  | [3] 7.1.1 | ProtocolDescriptorList | Universal |  | “L2CAP” (UUID), |  | Present for MSE |  |  |
|  | [Attribute GSIT – Protocol Descriptor |  |  |  |  |  | “RFCOMM” (UUID): |  |  |  |  |
|  | List] |  |  |  |  |  | Channel number – skip |  |  |  |  |
|  |  |  |  |  |  |  | (Uint8), |  |  |  |  |
|  |  |  |  |  |  |  | “OBEX” (UUID) |  |  |  |  |
|  | MAP/MSE/SGSIT/ATTR/BV-02-C |  | [3] 7.1.1 | BluetoothProfileDescriptorList | Universal |  | “Message Access Profile” |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  | (UUID): Version – “0x0103” |  |  |  |  |
|  | Descriptor List, MAP 1.3] |  |  |  |  |  | (Uint16) |  |  |  |  |
|  | MAP/MSE/SGSIT/ATTR/BV-03-C |  | [3] 7.1.1 | BluetoothProfileDescriptorList | Universal |  | “Message Access Profile” |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  | (UUID): Version – “0x0104” |  |  |  |  |
|  | Descriptor List, MAP 1.4] |  |  |  |  |  | (Uint16) |  |  |  |  |
|  | MAP/MSE/SGSIT/ATTR/BV-04-C |  | [3] 7.1.1 | GoepL2CapPsm | Profile | skip (Uint16) | skip (Uint16) |  | Present for MSE |  |  |
|  | [Attribute GSIT – GoepL2CapPsm] |  |  |  |  |  |  |  |  |  |  |
|  | MAP/MSE/SGSIT/ATTR/BV-05-C |  | [3] 7.1.1 | MASInstanceID | Profile | skip (Uint8) |  |  | Present for MSE |  |  |
|  | [Attribute GSIT – MAS Instance ID] |  |  |  |  |  |  |  |  |  |  |
|  | MAP/MSE/SGSIT/ATTR/BV-06-C |  | [3] 7.1.1 | SupportedMessageTypes | Profile | skip (Uint8) |  |  | Present for MSE |  |  |
|  | [Attribute GSIT – Supported |  |  |  |  |  |  |  |  |  |  |
|  | Message Types] |  |  |  |  |  |  |  |  |  |  |
|  | MAP/MSE/SGSIT/ATTR/BV-07-C |  | [3] 7.1.1 | MapSupportedFeatures | Profile | skip (Uint32) |  |  | Present for MSE |  |  |
|  | [Attribute GSIT – MAP Supported |  |  |  |  |  |  |  |  |  |  |
|  | Features] |  |  |  |  |  |  |  |  |  |  |

Table 4.2: Input for the Message Access Profile MSE SGSIT SDP test procedure

##### 4.2.1.2 Message Notification Service on the MCE device

Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [7] using Table 4.3 below as input:

| TCID |  |  | Reference | Attribute ID name | Attribute ID definition source (Universal, Profile) | Value/secondary value |  |  |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  |  |  |  |  | defined) |  |
|  | MAP/MCE/SGSIT/SERR/BV-02-C |  | [3] 7.1.2 | ServiceClassIDList | Universal | “Message Notification Server” (UUID) |  |  | Present for MCE | Present for MCE |  |
|  | [Service record GSIT – MAP MCE |  |  |  |  |  |  |  |  |  |  |
|  | Notification Service] |  |  |  |  |  |  |  |  |  |  |
| MAP/MCE/SGSIT/ATTR/BV-08-C [Attribute GSIT – Protocol Descriptor List] | MAP/MCE/SGSIT/ATTR/BV-08-C |  | [3] 7.1.2 | ProtocolDescriptorList | Universal |  | “L2CAP” (UUID), |  | Present for MCE |  |  |
|  | [Attribute GSIT – Protocol Descriptor |  |  |  |  |  | “RFCOMM” (UUID): |  |  |  |  |
|  | List] |  |  |  |  |  | Channel number – skip |  |  |  |  |
|  |  |  |  |  |  |  | (Uint8), |  |  |  |  |
|  |  |  |  |  |  |  | “OBEX” (UUID) |  |  |  |  |
|  | MAP/MCE/SGSIT/ATTR/BV-09-C |  | [3] 7.1.2 | BluetoothProfileDescriptorList | Universal |  | “Message Access Profile” |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  | (UUID): Version – “0x0103” |  |  |  |  |
|  | Descriptor List, MAP 1.3] |  |  |  |  |  | (Uint16) |  |  |  |  |
|  | MAP/MCE/SGSIT/ATTR/BV-10-C |  | [3] 7.1.2 | BluetoothProfileDescriptorList | Universal |  | “Message Access Profile” |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  | (UUID): Version – “0x0104” |  |  |  |  |
|  | Descriptor List, MAP 1.4] |  |  |  |  |  | (Uint16) |  |  |  |  |
|  | MAP/MCE/SGSIT/ATTR/BV-11-C |  | [3] 7.1.2 | GoepL2CapPsm | Profile | skip (Uint16) | skip (Uint16) |  | Present for MCE |  |  |
|  | [Attribute GSIT – GoepL2CapPsm] |  |  |  |  |  |  |  |  |  |  |
|  | MAP/MCE/SGSIT/ATTR/BV-12-C |  | [3] 7.1.2 | MapSupportedFeatures | Profile | skip (Uint32) |  |  | Present for MCE |  |  |
|  | [Attribute GSIT – MAP Supported |  |  |  |  |  |  |  |  |  |  |
|  | Features] |  |  |  |  |  |  |  |  |  |  |

Table 4.3: Input for the Message Access Profile MCE SGSIT SDP test procedure

##### 4.2.1.3 Message Access Profile – Attribute ID Offset String tests

Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [7] using Table 4.4 below as input:

| TCID |  |  | Reference | ServiceSearchPattern | Attribute ID name | Attribute ID Offset |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  |  |  | defined) |  |
|  | MAP/MSE/SGSIT/OFFS/BV-01-C |  | [3] 7.1.1 | Message Access Server | ServiceName | 0x0000 | Present for MSE | Present for MSE |  |
|  | [Attribute ID Offset String GSIT – |  |  |  |  |  |  |  |  |
|  | Service Name] |  |  |  |  |  |  |  |  |
|  | MAP/MCE/SGSIT/OFFS/BV-02-C |  | [3] 7.1.2 | Message Notification Server | ServiceName | 0x0000 | Present for MCE |  |  |
|  | [Attribute ID Offset String GSIT – |  |  |  |  |  |  |  |  |
|  | Service Name] |  |  |  |  |  |  |  |  |

Table 4.4: Input for the Message Access Profile SGSIT Attribute ID Offset String tests

#### 4.2.2 Client Generic SDP Integrated Tests

Execute the Generic SDP Future Compatibility Tests defined in Section 6.4, Client test procedures (CGSIT), in [7] using Table 4.5 below as input:

| TCID | Reference |  | Service Record Service Class |  | Lower Tester SDP record initial conditions |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | UUID description |  |  |  |  |
| MAP/MCE/CGSIT/SFC/BV-01-C [SDP Future Compatibility – IUT is MAP MCE] | [3] 7.1, 7.1.1 | Message Access Server | Message Access Server |  |  | The Lower Tester exposes a MAP MSE SDP record. |  |
|  |  |  |  |  |  | The version in the Bluetooth Profile Descriptor List is greater than the most |  |
|  |  |  |  |  |  | recently adopted version. |  |
|  |  |  |  |  |  | All bits are set in the SupportedMessageTypes attribute, including |  |
|  |  |  |  |  |  | Reserved bits. |  |
|  |  |  |  |  |  | All bits are set in the MAPSupportedFeatures attribute, including Reserved |  |
|  |  |  |  |  |  | bits. |  |
|  |  |  |  |  |  | The HFP SDP record is exposed if specified by IXIT [8]. |  |

Table 4.5: Input for the Client CGSIT SDP future compatibility tests

### 4.3 Session Management

Verify that the MAP sessions can be established and terminated properly.

#### 4.3.1 IUT – Message Client Equipment (MCE)

Verify that the Message Client Equipment can properly establish and terminate MAP sessions.
MAP/MCE/MSM/BV-01-C [MCE opens a MAP session with Message Access Service only]
• Test Purpose
Verify that the MCE can start a MAP session that involves only the Message Access Service.
• Reference
[3] 6.4.1
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
The IUT establishes a MAP session with the Lower Tester by sending an OBEX CONNECT to the Lower Tester according to the connection parameters defined by the Lower Tester's MAS SDP record.
• Expected Outcome
Pass verdict
The OBEX CONNECT response messages related to the MAS have been exchanged properly so the MAS service is established.
MAP/MCE/MSM/BV-02-C [MCE opens a MAP session with Message Access Service and Message Notification Service]
• Test Purpose
Verify that the MCE can start a MAP session that involves both the Message Access Service and Message Notification.
• Reference
[3] 6.4.2
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The MCE supports the Notification feature.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
1. The IUT establishes a MAP session with the Lower Tester by connecting to the OBEX Message
Access Service of the Lower Tester.
‘SetNotificationRegistration’. 3. The Lower Tester connects to the OBEX Message Notification Service of the IUT.
• Expected Outcome
Pass verdict
The OBEX CONNECT response messages of both the MAS and MNS have been exchanged properly.
Both the Message Access Service and the Message Notification Service are established.
MAP/MCE/MSM/BV-03-C [MCE closes a MAP session when both the Message Access Service and the Message Notification Service are active]
• Test Purpose
Verify that the MCE can terminate a MAP session.
• Reference
[3] 6.4.4
• Initial Condition
- The IUT is engaged in a MAP session with the Lower Tester.
- Both the Message Access Service and Message Notification Service are in use.
• Test Procedure
1. The IUT finishes the MNS session by switching the Notification ‘off’ (function
SetNotificationRegistration). 2. The Lower Tester disconnects the MNS session by sending an OBEX DISCONNECT. 3. The IUT disconnects the MAS session by sending an OBEX DISCONNECT.
• Expected Outcome
Pass verdict
Both the Message Access Service session and the Message Notification Service sessions are closed.
The OBEX DISCONNECT response messages for MAS have been exchanged properly.
The OBEX DISCONNECT response messages for MNS have been exchanged properly or MNS transport channel is disconnected by the IUT.
MAP/MCE/MSM/BV-04-C [MCE closes a MAP session when only the Message Access Service is active]
• Test Purpose
Verify that the MCE can terminate a MAP session.
• Reference
[3] 6.4.4
• Initial Condition
- The IUT is engaged in a MAP session with the Lower Tester.
• Test Procedure
The IUT disconnects the MAS session by sending an OBEX DISCONNECT.
• Expected Outcome
Pass verdict
The OBEX session for Message Access Service is closed.
The OBEX DISCONNECT response messages of the MAS have been exchanged properly.
MAP/MCE/MSM/BV-13-C [MCE opens multiple MAS and one MNS with Notification turned on]
• Test Purpose
Verify that the MCE can open a MAP session with at least two MAS and one MNS active.
• Reference
[3] 6.4.4
• Initial Condition
- Both the Lower Tester and the IUT support multiple MAS instances simultaneously (i.e., SMS, MMS, multiple email accounts). The MCE supports Notification feature.
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
1. The IUT sends the Lower Tester a SDP Search request for Message Access Server. The Lower
Tester replies with at least two Service Record Handles. 2. The IUT connects to the Lower Tester’s two instances and sends the notification status to ‘on’ for
each use. This may be done in any order. 3. As soon as the first notification registration is set to ‘on’ the Lower Tester connects to the
notification channel.
• Expected Outcome
Pass verdict
Both the Message Access Service sessions and the Message Notification Service session are open.
The OBEX CONNECT response messages of both the MAS and MNS have been exchanged properly.
MAP/MCE/MSM/BV-14-C [MCE closes multiple active MAS and active MNS sessions with Notification turned off first]
• Test Purpose
Verify that the MCE can close a MAP session with at least two MAS and one MNS active.
• Reference
[3] 6.4.4
• Initial Condition
- Both the Lower Tester and the IUT support multiple MAS instances simultaneously (i.e., SMS, MMS, multiple email accounts).
- The MCE supports the Notification feature.
- A MAP session with at least two active MAS and one MNS is ongoing between the IUT and the Lower Tester.
- The IUT sets the Notifications mode on the Lower Tester to “on” for at least two MAS instances.
• Test Procedure
1. The IUT, for both instances, sets the notification status to ‘off’ and disconnects the MAS
connections. This may be done in any order. 2. As soon as both instances have unregistered notifications, the Lower Tester disconnects the
notification channel.
• Expected Outcome
Pass verdict
Both the Message Access Service sessions and the Message Notification Service session are closed.
The OBEX DISCONNECT response messages for MAS have been exchanged properly.
The OBEX DISCONNECT response messages for MNS have been exchanged properly or MNS transport channel is disconnected by the IUT.

#### 4.3.2 IUT – Message Server Equipment (MSE)

Verify that the Message Server Equipment device can properly respond to MAP session establishment and Notification requests by the Message Client Equipment (MCE) device.
MAP/MSE/MSM/BV-05-C [MSE responds to an open MAP session request for the Message Access Service]
• Test Purpose
Verify that the MSE can properly respond to a MAP session establishment request.
• Reference
[3] 6.4.1
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable mode.
• Test Procedure
The Lower Tester connects to the IUT by sending an OBEX CONNECT request to the Message Access Service of the IUT.
• Expected Outcome
Pass verdict
The IUT responds with an OBEX CONNECT response.
MAP/MSE/MSM/BV-06-C [MSE responds to an open MAP session request with Message Access Service and Message Notification Service]
• Test Purpose
Verify that the MSE can properly respond to a MAP session establishment request.
• Reference
[3] 6.4.2
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The MCE supports the Notification feature.
- The IUT is in discoverable and connectable mode.
• Test Procedure
1. The Lower Tester connects to the IUT by sending an OBEX CONNECT request to the Message
Access Service of the IUT. 2. The Lower Tester sends the notification status ‘on’ to the IUT using the function
‘SetNotificationRegistration’. 3. The IUT connects to the Lower Tester by sending an OBEX CONNECT request to the Message
Notification Service of the Lower Tester.
• Expected Outcome
Pass verdict
The IUT responds with an OBEX CONNECT response and subsequently connects to the Message Notification Service of the Lower Tester.
MAP/MSE/MSM/BV-07-C [MSE closes a MAP session when both MAS and MNS are active]
• Test Purpose
Verify that the MSE can close a MAP session.
• Reference
[3] 6.4.4
• Initial Condition
- A MAP session with active MAS and MAS is ongoing between the IUT and the Lower Tester.
• Test Procedure
1. The Lower Tester sends the notification status ‘off’ to the IUT using the function
‘SetNotificationRegistration’. 2. The IUT disconnects the MAP MNS session by sending an OBEX DISCONNECT. 3. The Lower Tester disconnects the MAP MAS session by sending an OBEX DISCONNECT.
• Expected Outcome
Pass verdict
Both the Message Access Service session and the Message Notification Service sessions are closed.
The OBEX DISCONNECT response messages of both the MAS and MNS have been exchanged properly.
MAP/MSE/MSM/BV-08-C [MSE closes a MAP session when only the Message Access Service is active]
• Test Purpose
Verify that the MSE can close a MAP session.
• Reference
[3] 6.4.4
• Initial Condition
- A MAP session with active MAS is ongoing between the IUT and the Lower Tester.
• Test Procedure
1. The Lower Tester disconnects the MAP MAS session by sending an OBEX DISCONNECT. 2. The IUT receives an OBEX DISCONNECT and finishes the MAP session.
• Expected Outcome
Pass verdict
The Message Access Service session is closed.
The OBEX DISCONNECT response messages of the MAS have been exchanged properly.
MAP/MSE/MSM/BV-09-C [MSE responds to multiple open MAS instances requests for the Message Access Service]
• Test Purpose
Verify that the MSE can properly respond to multiple MAS instance establishment requests.
• Reference
[3] 3.1.8, 6.4.2, 7.1.1
• Initial Condition
- Both the Lower Tester and the IUT support multiple MAS instances simultaneously (i.e., SMS, MMS, multiple email accounts).
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable mode.
• Test Procedure
1. The Lower Tester sends the IUT SDP Search Request for Message Access Server. The IUT
replies with multiple Service Record Handles. 2. The Lower Tester connects to the IUT by sending an OBEX CONNECT request sequentially to
each Message Access Service instance of the IUT.
• Expected Outcome
Pass verdict
The IUT responds with an OBEX CONNECT response for each Message Access Service (response code ‘SUCCESS’).
MAP/MSE/MSM/BV-10-C [MSE responds to multiple open MAS instances requests with Message Access Service and Message Notification Service]
• Test Purpose
Verify that the MSE can properly respond to multiple MAS instance establishment requests.
• Reference
[3] 3.1.8, 6.4.3, 7.1.1, 7.1.2
• Initial Condition
- Both the Lower Tester and the IUT support multiple MAS instances simultaneously (i.e., SMS, MMS, multiple email accounts).
- The IUT and the Lower Tester have been paired. The MCE supports the Notification feature.
- The IUT is in discoverable and connectable mode.
• Test Procedure
1. The Lower Tester sends the IUT SDP Search Request for Message Access Server. The IUT
replies with multiple Service Record Handles. 2. The Lower Tester connects to the IUT by sending an OBEX CONNECT request sequentially to
each Message Access Service instance of the IUT. 3. The Lower Tester sends the notification status ‘on’ to each Message Access Service instance of
the IUT by using the function ‘SetNotificationRegistration’. 4. The IUT connects to the Lower Tester by sending an OBEX CONNECT request to the Message
Notification Service of the Lower Tester.
• Expected Outcome
Pass verdict
The IUT responds with each OBEX CONNECT response (response code ‘SUCCESS’) and subsequently connects to the Message Notification Service of the Lower Tester.
MAP/MSE/MSM/BV-11-C [MSE closes multiple active MAS and active MNS sessions with Notification turned off first]
• Test Purpose
Verify that the MSE can close a MAP session with multiple active MAS.
• Reference
[3] 6.4.4
• Initial Condition
- Both the Lower Tester and the IUT support multiple MAS instances simultaneously (i.e., SMS, MMS, multiple email accounts).
- A MAP session with at least two active MAS and one MNS is ongoing between the IUT and the Lower Tester.
- The Lower Tester sets the Notification mode on the IUT to “on” for at least two MAS instances.
• Test Procedure
1. The Lower Tester sends the notification status ‘off’ to the IUT using the function
‘SetNotificationRegistration’ for each registered MAS. 2. The IUT disconnects the MAP MNS session by sending an OBEX DISCONNECT. 3. The Lower Tester disconnects each MAP MAS session by sending an OBEX DISCONNECT.
• Expected Outcome
Pass verdict
Both the Message Access Service sessions and the Message Notification Service session are closed.
The OBEX DISCONNECT response messages of both the MAS and MNS have been exchanged properly.
MAP/MSE/MSM/BV-12-C [MSE closes multiple active MAS and active MNS sessions without Notifications being turned off first]
• Test Purpose
Verify that the MSE can close a MAP session with at least two active MAS and one MNS without having the client send Notification Registration off for the different instances.
• Reference
[3] 6.4.4
• Initial Condition
- Both the Lower Tester and the IUT support multiple MAS instances simultaneously (i.e., SMS, MMS, multiple email accounts).
- A MAP session with at least two active MAS and one MNS is ongoing between the IUT and the Lower Tester.
- The Lower Tester sets the Notification mode on the IUT to “on” for at least two MAS instances.
• Test Procedure
1. The Lower Tester disconnects the all the MAP MAS sessions by sending an OBEX
DISCONNECT for each instance. 2. The IUT disconnects the MAP MNS session by sending an OBEX DISCONNECT.
• Expected Outcome
Pass verdict
Both the Message Access Service sessions and the Message Notification Service session are closed.
The OBEX DISCONNECT response messages of both the MAS and MNS have been exchanged properly.

### 4.4 Notification Registration Feature

Verify the normal behavior of the components necessary to realize the Notification Registration feature.

#### 4.4.1 IUT – Message Client Equipment (MCE)

Verify that the Message Client Equipment device can properly take advantage of the Notification Registration feature.
MAP/MCE/MNR/BV-01-C [MCE switches Notification to ‘off’ status]
• Test Purpose
Verify that the MCE can switch off the Notification of the MSE.
• Reference
[3] 5.2
• Initial Condition
- The IUT and the Lower Tester have established a MAP session and both the Message Access Service and the Message Notification Service are active (Notification status ‘on’).
• Test Procedure
The IUT sends the notification status ‘off’ to the Lower Tester using the function ‘SetNotificationRegistration’.
• Expected Outcome
Pass verdict
The request of the ‘SetNotificationRegistration’ function is well formatted according to [3].
Message Notification Service is terminated either by the Lower Tester sending an OBEX DISCONNECT to the IUT or the IUT disconnecting the MNS transport channel.
MAP/MCE/MNR/BV-02-C [MCE switches Notification to ‘on’ status]
• Test Purpose
Verify that the MCE can switch on the Notification of the MSE.
• Reference
[3] 5.2
• Initial Condition
- The IUT and the Lower Tester have established a MAP session and the Message Notification Service is not connected (Notification status ‘off’).
• Test Procedure
1. The IUT sends the notification status ‘on’ to the Lower Tester using the function
‘SetNotificationRegistration’. 2. The Lower Tester connects to the OBEX Message Notification Service of the IUT.
• Expected Outcome
Pass verdict
The request of the ‘SetNotificationRegistration’ function is well formatted according to [3].
The Lower Tester connects to the IUT’s MNS by sending an OBEX CONNECT to the IUT.

#### 4.4.2 IUT – Message Server Equipment (MSE)

Verify that the Message Server Equipment device can properly implement the Notification Registration feature.
MAP/MSE/MNR/BV-03-C [MSE terminates Message Notification]
• Test Purpose
Verify that the MSE can terminate the Message Notification.
• Reference
[3] 5.2
• Initial Condition
- The IUT and the Lower Tester have established a MAP session and both the Message Access Service and the Message Notification Service are active (Notification status ‘on’).
• Test Procedure
The Lower Tester sends the notification status ‘off’ to the IUT using the function ‘SetNotificationRegistration’.
• Expected Outcome
Pass verdict
The response of the ‘SetNotificationRegistration’ function is well formatted according to [3].
The IUT terminates the MNS session by sending an OBEX DISCONNECT to the Lower Tester.
MAP/MSE/MNR/BV-04-C [MSE starts Message Notification]
• Test Purpose
Verify that the MSE can establish a Message Notification.
• Reference
[3] 5.2
• Initial Condition
- The IUT and the Lower Tester have established a MAP session and the Message Notification Service is not connected (Notification status ‘off’).
• Test Procedure
The Lower Tester sends the notification status ‘on’ to the IUT using the function ‘SetNotificationRegistration’.
• Expected Outcome
Pass verdict
The response of the ‘SetNotificationRegistration’ function is well formatted according to [3].
The IUT connects to the Lower Tester’s MNS by sending an OBEX CONNECT to the Lower Tester.

### 4.5 Browsing Feature

Verify that the components that are specific to the Browsing feature are properly implemented.

#### 4.5.1 IUT – Message Client Equipment (MCE)

Verify that the components that are specific to the Browsing feature are properly implemented by the MCE.
MAP/MCE/MMB/BV-01-C [MCE reads the folder structure of the MSE]
• Test Purpose
Verify that the MCE can retrieve a Folders Listing on the MSE.
• Reference
[3] 5.2
• Initial Condition
- The IUT and the Lower Tester have established a MAP session.
- The Lower Tester contains at least one non-null folder object.
• Test Procedure
1. The IUT sends a ‘GetFoldersListing’ request to at least one of the MAP virtual folders supported
by the Lower Tester. 2. The Lower Tester delivers the requested folder-listing object.
• Expected Outcome
Pass verdict
The request of the ‘GetFoldersListing’ function is well formatted according to [3].
The folder can be displayed properly on the IUT.
MAP/MCE/MMB/BV-02-C [MCE selects the current folder on MSE]
• Test Purpose
Verify that the MCE can set the current folder on the MSE.
• Reference
[3] 5.3
• Initial Condition
- The IUT and the Lower Tester have established a MAP session.
- The Lower Tester contains at least one non-null folder object.
• Test Procedure
The IUT sends a ‘SetFolder’ command to the Lower Tester, targeting one of the MAP virtual folders supported by the Lower Tester.
• Expected Outcome
Pass verdict
The request of the ‘SetFolder’ function is well formatted according to [3].
The current folder on the MSE is set to the requested folder.
MAP/MCE/MMB/BV-03-C [MCE retrieves a list of messages]
• Test Purpose
Verify that the MCE can retrieve a Messages-Listing from the MSE.
• Reference
[3] 3.1.6, 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester contains at least one folder that is non-empty.
• Test Procedure
1. The IUT requests the Messages-Listing object of the current folder. 2. The Lower Tester delivers the requested Messages-Listing object.
• Expected Outcome
Pass verdict
The request of the ‘GetMessagesListing’ function is well formatted according to [3].
The IUT is able to receive the Messages-Listing object and correctly display it.
MAP/MCE/MMB/BV-19-C [MCE retrieves a filtered list of messages]
• Test Purpose
Verify that the MCE can retrieve a filtered Messages-Listing from the MSE using all supported filtering parameters.
• Reference
[3] 5.5, 5.5.4
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to a folder with a large number of messages with different values for the message attributes type, delivery date, read status, recipient, originator and priority.
- The Lower Tester contains at least one folder with a large number of messages with different values for the message attributes type, delivery date, read status, recipient, originator and priority.
• Test Procedure
1. The IUT iteratively requests a Messages-Listing object of the current folder by using each of the
supported filtering parameters, if the respective filtering type is supported by the MCE:
▪ FilterMessageType: to filter out the messages which are not of the delivered type; to be done for all types supported by both the MSE and MCE
▪ FilterPeriodBegin only: to filter out the messages older than the delivered value of FilterPeriodBegin
▪ FilterPeriodEnd only: to filter out the messages more recent than the delivered value of FilterPeriodEnd
▪ FilterPeriodBegin and FilterPeriodEnd: to filter out the messages outside the period defined by these values
▪ FilterReadStatus: to filter out the messages which are not of the delivered read status; to be done both for status values ‘read’ and ‘unread’
▪ FilterRecipient: to filter out the messages where not at least a substring is matching the delivered value
▪ FilterOriginator: to filter out the messages where not at least a substring is matching the delivered value
▪ FilterPriority: to filter out the messages which are not of the delivered priority; to be done both for priority values ‘high’ and ‘non-high’
2. The Lower Tester delivers the requested Messages-Listing object.
• Expected Outcome
Pass verdict
The request of the ‘GetMessagesListing’ function is well formatted according to [3].
The request includes filtering application parameters as supported by the MCE.
The IUT is able to receive the Messages-Listing object.
The Messages-Listing object is correctly filtered.
• Notes
The IUT demonstrates the support of all filtering parameters as declared in Table 20 of the MAP.ICS [4].
MAP/MCE/MMB/BV-04-C [MCE retrieves an email message]
• Test Purpose
Verify that the MCE can retrieve an email message from the MSE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one email with only textual content. The IUT has retrieved the Messages-Listing of this folder.
- The Lower Tester contains at least one folder that includes at least one email with only textual content.
• Test Procedure
1. The IUT requests one of the email message objects contained in the Messages-Listing object. 2. The Lower Tester delivers the requested message object.
• Expected Outcome
Pass verdict
The request of the ‘GetMessage’ function is well formatted according to [3].
The IUT is able to receive the message object and correctly display it.
MAP/MCE/MMB/BV-17-C [MCE retrieves an MMS message]
• Test Purpose
Verify that the MCE can retrieve an MMS message from the MSE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one MMS with only textual content. The IUT has retrieved the Messages-Listing of this folder.
- The Lower Tester contains at least one folder that includes at least one MMS with only textual content.
• Test Procedure
1. The IUT requests one of the MMS message objects contained in the Messages-Listing object. 2. The Lower Tester delivers the requested message object.
• Expected Outcome
Pass verdict
The request of the ‘GetMessage’ function is well formatted according to [3].
The IUT is able to receive the message object and correctly display it.
• Test Purpose
Verify that the MCE can retrieve an SMS message either in native format or with text trans-coded to UTF-8 from the MSE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one GSM- SMS or CDMA-SMS, as supported by the declared message types of the IUT, with textual content. The IUT has retrieved the Messages-Listing of this folder.
- The Lower Tester contains at least one folder that includes at least one GSM-SMS or CDMA- SMS, as supported by the declared message types of the IUT, with textual content.
• Test Procedure
1. The IUT requests one of the SMS message objects contained in the Messages-Listing object in
native format (function ‘GetMessage’ attribute ‘Charset’=<native> or with text trans-coded to UTF-8 (function ‘GetMessage’ attribute ‘Charset’=<UTF-8>). 2. The Lower Tester delivers the requested message object.
• Expected Outcome
Pass verdict
The request of the ‘GetMessage’ function is well formatted according to [3].
The IUT is able to receive the message object and correctly display it.
MAP/MCE/MMB/BV-07-C [MCE modifies the 'read' status of a message]
• Test Purpose
Verify that the MCE can set the status of a message on the MSE.
• Reference
[3] 5.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to one non-empty folder. The IUT has retrieved the Messages-Listing of this folder.
- The Lower Tester contains at least one folder that is non-empty. All the messages on the Lower Tester have the status “Unread”.
• Test Procedure
1. The IUT requests the Lower Tester to change the status of one message that was contained in
the Messages-Listing object from “Unread” to “Read”. 2. The Lower Tester repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict
The request of the ‘SetMessageStatus’ function is well formatted according to [3].
The status of the messages has been set to 'read' as requested.
MAP/MCE/MMB/BV-08-C [MCE initiates an update of the MSE’s inbox]
• Test Purpose
Verify that the MCE can initiate the MSE to update its inbox with new messages loaded from its corresponding remote mailbox.
• Reference
[3] 5.9
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
1. The IUT requests the update of the Messages-Listing of the Lower Tester’s ‘Inbox’ folder. 2. The Lower Tester simulates a mailbox connection to a remote mailbox and adds a new message
to the message listing in its ‘Inbox’. 3. The IUT requests the Messages-Listing of the ‘Inbox’.
• Expected Outcome
Pass verdict
- The request of the ‘UpdateInbox’ function is well formatted according to [3].
- The IUT is able to request receive the Messages-Listing of the Lower Tester’s ‘Inbox’ folder updated by the new message.
MAP/MCE/MMB/BV-21-C [MCE retrieves an bMessage with type ‘IM’]
• Test Purpose
Verify that the MCE sends a correctly formatted GetMessage request for type ‘IM’.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one IM message with only textual content. The IUT has retrieved the Messages-Listing of this folder.
- The Lower Tester contains at least one folder that includes at least one IM message with only textual content.
• Test Procedure
1. The IUT requests one of the IM message objects contained in the Messages-Listing object. 2. The Lower Tester delivers the requested message object.
• Expected Outcome
Pass verdict
The request of the ‘GetMessage’ function is well formatted according to [3].
The IUT is able to request receive the message object and correctly display it.
MAP/MCE/MMB/BV-26-C [MCE retrieves a list of conversations]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Conversation-Listing.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester is configured to contain a Conversation-Listing object.
• Test Procedure
The IUT is triggered to request a Conversation-Listing from the Lower Tester.
• Expected Outcome
Pass verdict
The request for the Conversation-Listing is correctly formatted according to [3].
The IUT is able to receive the Conversation-Listing object and correctly display it.
MAP/MCE/MMB/BV-27-C [MCE retrieves a filtered list of conversations]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Messages-Listing of all messages of a specific conversation.
• Reference
[3] 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Messages-Listing of all messages of a specific conversation.
• Expected Outcome
Pass verdict
The request for the Messages-Listing is correctly formatted according to [3].
The request for the Messages-Listing contains the application parameter ConversationID with a valid conversation ID.
MAP/MCE/MMB/BV-28-C [MCE retrieves DatabaseIdentifier and FolderVersionCounter]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Messages-Listing with MaxListCount=0 to receive DatabaseIdentifier and FolderVersionCounter.
• Reference
[3] 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Messages-Listing to receive DatabaseIdentifier and FolderVersionCounter.
• Expected Outcome
Pass verdict
The request for the Messages-Listing is correctly formatted according to [3] and has MaxListCount set to zero.
MAP/MCE/MMB/BV-29-C [MCE retrieves Conversation-Listing, Counter, Size and DatabaseIdentifier]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Conversation-Listing with MaxListCount=0 to receive the ConversationListingVersionCounter, ConversationListingSize and DatabaseIdentifier.
• Reference
[3] 5.13, 3.1.14, 3.1.15
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Conversation-Listing to receive ConversationListingVersionCounter, ConversationListingSize and DatabaseIdentifier.
• Expected Outcome
Pass verdict
The request for the Conversation-Listing is correctly formatted according to [3] and has MaxListCount set to zero.
MAP/MCE/MMB/BV-30-C [MCE retrieves list of conversations filtered by LastActivity]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Conversation-Listing with Filtering for LastActivity.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Conversation-Listing with Filtering by LastActivity.
• Expected Outcome
Pass verdict
The request for the Conversation-Listing is correctly formatted according to [3] and contains valid values for FilterLastActivityBegin and FilterLastActivityEnd.
MAP/MCE/MMB/BV-31-C [MCE retrieves list of conversations filtered by read status]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Conversation-Listing with Filtering by read status.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Conversation-Listing with Filtering by read status.
• Expected Outcome
Pass verdict
The request for the Conversation-Listing is correctly formatted according to [3] and contains a valid value for read status.
MAP/MCE/MMB/BV-32-C [MCE retrieves list of conversations filtered by recipient]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Conversation-Listing with Filtering by recipient.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Conversation-Listing with Filtering by recipient.
• Expected Outcome
Pass verdict
The request for the Conversation-Listing is correctly formatted according to [3] and contains a valid value for FilterRecipient.
MAP/MCE/MMB/BV-33-C [MCE retrieves list of conversations filtered by message handle]
• Test Purpose
Verify that the MCE sends a correctly formatted request for a Messages-Listing with Filtering by message handle.
• Reference
[3] 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT is triggered to request a Messages-Listing with Filtering by message handle.
• Expected Outcome
Pass verdict
The request for the Messages-Listing is correctly formatted according to [3] and contains the application parameter FilterMessageHandle with a valid message handle.
• Test Purpose
Verify that the MCE sends a correctly formatted request to change the extended data of a message.
• Reference
[3] 3.1.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT sends a ‘SetMessageStatus’ request to the Lower Tester with new values for the extended data.
• Expected Outcome
Pass verdict
The request of the ‘SetMessageStatus’ function is well formatted according to [3].

#### 4.5.2 IUT – Message Server Equipment (MSE)

Verify that the components that are specific to the Browsing feature are properly implemented by the MSE.
MAP/MSE/MMB/BV-09-C [MSE returns folder structure information to the MCE]
• Test Purpose
Verify that the MSE can return a Folders Listing to the MCE.
• Reference
[3] 5.4
• Initial Condition
- The IUT and the Lower Tester have established a MAP session.
- The IUT contains at least one non-null folder object.
• Test Procedure
The Lower Tester sends a ‘GetFoldersListing’ request to at least one of the MAP virtual folders supported by the IUT.
• Expected Outcome
Pass verdict
The response of the ‘GetFoldersListing’ function is well formatted according to [3].
The requested folder can be displayed properly on the Lower Tester.
MAP/MSE/MMB/BV-10-C [MSE sets its current folder]
• Test Purpose
• Reference
[3] 5.3
• Initial Condition
- The IUT and the Lower Tester have established a MAP session.
- The IUT contains at least one non-null folder object.
• Test Procedure
The Lower Tester sends a ‘SetFolder’ request targeting one of the MAP virtual folders supported by the IUT.
• Expected Outcome
Pass verdict
The response of the ‘SetFolder’ function is well formatted according to [3].
The current folder on the MSE is set to the requested folder.
MAP/MSE/MMB/BV-11-C [MSE returns a list of messages]
• Test Purpose
Verify that the MSE can return a Messages-Listing object to the MCE.
• Reference
[3] 3.1.6, 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder to one non-empty folder.
- The IUT contains at least one non-null folder object.
• Test Procedure
The Lower Tester requests the Messages-Listing object of the current folder.
• Expected Outcome
Pass verdict
The response of the ‘GetMessagesListing’ function is well formatted according to [3].
The Lower Tester is able to receive the Messages-Listing object and correctly display it.
MAP/MSE/MMB/BV-20-C [MSE returns a filtered list of messages]
• Test Purpose
Verify that the MSE can return a filtered Messages-Listing to the MCE.
• Reference
[3] 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder of the IUT with a large number of messages with different values for the message attributes type, delivery date, read status, recipient, originator and priority.
- The IUT contains at least one folder with a large number of messages with different values for the message attributes type, delivery date, read status, recipient, originator and priority.
• Test Procedure
1. The Lower Tester iteratively requests Messages-Listing objects of the current folder by using
filtering parameters:
▪ FilterMessageType: to filter out the messages which are not of the delivered type; to be done for all types supported by both the MSE
▪ FilterPeriodBegin only: to filter out the messages older than the delivered value of FilterPeriodBegin
▪ FilterPeriodEnd only: to filter out the messages more recent than the delivered value of FilterPeriodEnd
▪ FilterPeriodBegin and FilterPeriodEnd: to filter out the messages outside the period defined by these values
▪ FilterReadStatus: to filter out the messages which are not of the delivered read status; to be done both for status values ‘Read’ and ‘Unread’
▪ FilterRecipient: to filter out the messages where not at least a substring is matching the delivered value
▪ FilterOriginator: to filter out the messages where not at least a substring is matching the delivered value
▪ FilterPriority: to filter out the messages which are not of the delivered priority; to be done both for priority values ‘high’ and ‘non-high’
2. The IUT delivers the requested Messages-Listing objects.
• Expected Outcome
Pass verdict
The response of the ‘GetMessagesListing’ function is well formatted according to [3].
The Lower Tester is able to receive the Messages-Listing object.
The Messages-Listing object is correctly filtered.
MAP/MSE/MMB/BV-12-C [MSE returns an email message]
• Test Purpose
Verify that the MSE can return an email message to the MCE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder to a folder that includes at least one email with only textual content. The Lower Tester has retrieved the Messages-Listing of this folder.
- The IUT contains at least one folder that includes at least one email with only textual content.
• Test Procedure
1. The Lower Tester requests one of the email message objects contained in the Messages-Listing. 2. The IUT delivers the requested message object.
• Expected Outcome
Pass verdict
The response of the ‘GetMessage’ function is well formatted according to [3].
The Lower Tester is able to receive the message object and correctly display it.
MAP/MSE/MMB/BV-18-C [MSE returns an MMS message]
• Test Purpose
Verify that the MSE can return an MMS message to the MCE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder to a folder that includes at least one MMS with only textual content. The Lower Tester has retrieved the Messages-Listing of this folder.
- The IUT contains at least one folder that includes at least one MMS with only textual content.
• Test Procedure
1. The Lower Tester requests one of the MMS message objects contained in the Messages-Listing. 2. The IUT delivers the requested message object.
• Expected Outcome
Pass verdict
The response of the ‘GetMessage’ function is well formatted according to [3].
The Lower Tester is able to receive the message object and correctly display it.
MAP/MSE/MMB/BV-13-C [MSE returns an SMS message in native format]
• Test Purpose
Verify that the MSE can return an SMS message in native format to the MCE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder to a folder that includes at least one GSM-SMS and/or one CDMA-SMS with textual content. The Lower Tester has retrieved the Messages- Listing of this folder.
- The IUT contains at least one folder that includes at least one GSM-SMS and/or one CDMA-SMS with textual content.
• Test Procedure
If the IUT supports message type GSM-SMS:
1. The Lower Tester requests one of the GSM-SMS message objects contained in the Messages-
Listing in native format (function ‘GetMessage’ attribute ‘Charset’=<native>). 2. The IUT delivers the requested message object.
If the IUT supports message type CDMA-SMS:
1. The Lower Tester requests one of the CDMA-SMS message objects contained in the Messages-
Listing in native format (function ‘GetMessage’ attribute ‘Charset’=<native>). 2. The IUT delivers the requested message object.
• Expected Outcome
Pass verdict
The response of the ‘GetMessage’ function is well formatted according to [3].
For each of the supported message types GSM-SMS and/or CDMA-SMS the Lower Tester is able to receive the message object and correctly display it.
MAP/MSE/MMB/BV-14-C [MSE returns an SMS message trans-coded to UTF-8]
• Test Purpose
Verify that the MSE can return an SMS message with text trans-coded to UTF-8 to the MCE.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder to a folder that includes at least one GSM-SMS and/or one CDMA-SMS with textual content. The Lower Tester has retrieved the Messages- Listing of this folder.
- The IUT contains at least one folder that includes at least one GSM-SMS or CDMA-SMS with textual content.
• Test Procedure
1. The Lower Tester requests one of the SMS message objects contained in the Messages-Listing
with text trans-coded to UTF-8 (function ‘GetMessage’ attribute ‘Charset’=<UTF-8>). 2. The IUT delivers the requested message object as text trans-coded to UTF-8.
• Expected Outcome
Pass verdict
The response of the ‘GetMessage’ function is well formatted according to [3].
The Lower Tester is able to receive the message object and correctly display it.
MAP/MSE/MMB/BV-22-C [MSE returns an IM message]
• Test Purpose
Verify that the MSE correctly responds to a request for a bMessage in format 1.1 with message type “IM”.
• Reference
[3] 5.6, 3.1.3, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has set the current folder to a folder that includes at least one IM message with only textual content.
• Test Procedure
1. The Lower Tester requests one of the IM message objects contained in the Messages-Listing
object. 2. The IUT delivers the requested message object.
• Expected Outcome
Pass verdict
The response to the ‘GetMessage’ function is well formatted with a valid bMessage of type ‘IM’ according to [3].
The Lower Tester is able to receive the message object and correctly display it.
MAP/MSE/MMB/BV-15-C [MSE updates the ‘read’ status of a message]
• Test Purpose
Verify that the MSE can set the status of a message as requested by the MCE.
• Reference
[3] 5.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT contains at least one folder that is non-empty. All the messages on the IUT have the status “Unread”.
- The Lower Tester has set the current folder to one non-empty folder. The Lower Tester has retrieved the Messages-Listing of this folder.
• Test Procedure
1. The Lower Tester requests the IUT to change the status of one message that was contained in
the Messages-Listing object from “Unread” to “Read”. 2. The Lower Tester repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The response of the ‘SetMessageStatus’ function is well formatted according to [3].
The status of the messages has been set to ‘read’ as requested AND if the Lower Tester has received a 'SUCCESS' response from the IUT.
MAP/MSE/MMB/BV-16-C [MSE updates its inbox folder]
• Test Purpose
Verify that, on demand of the MCE, the MSE is able to update its inbox with new messages loaded from its corresponding remote mailbox.
• Reference
[3] 5.9
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
1. A new message not currently included in the IUT’s ‘Inbox’ message listing has been sent to the
remote mailbox of the IUT. 2. On request of the Lower Tester the IUT contacts the remote mailbox, loads the new message and
updates its ‘Inbox’ folder. 3. The Lower Tester requests the Messages-Listing of the ‘Inbox’.
• Test Condition
The IUT supports a message type and a related service which is not pushed or forwarded instantly from the remote mailbox to the MSE device but has to be retrieved actively from a remote mailbox.
• Expected Outcome
Pass verdict
The response of the ‘UpdateInbox’ function is well formatted according to [3].
AND
The Lower Tester is able to receive the Messages-Listing of the IUT’s ‘Inbox’ folder and correctly display it with the new message.
OR
If the IUT does not allow the polling of its mailbox, it answers with a “Not implemented” error response.
MAP/MSE/MMB/BV-23-C [MSE updates Folder version counter]
• Test Purpose
Verify that the MSE correctly updates the Folder version counter when adding a message to a folder.
• Reference
[3] 3.1.15, 5.5, 3.1.9
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has retrieved the current value of FolderVersionCounter by having executed GetMessagesListing.
• Test Procedure
1. On the IUT, a message is added to a folder. 2. The Lower Tester retrieves the value for FolderVersionCounter by executing a
GetMessagesListing requests.
• Expected Outcome
Pass verdict
The value for FolderVersionCounter is updated according to [3] after the message has been added on the IUT.
MAP/MSE/MMB/BV-24-C [MSE updates Conversation version counter]
• Test Purpose
Verify that the MSE correctly updates the Conversation version counter when adding a participant to a conversation.
• Reference
[3] 3.1.15, 5.13, 3.1.9
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has retrieved the current value of the Conversation Version Counter, e.g., by having executed GetConversationListing commands.
• Test Procedure
1. On the IUT, a participant is added to a conversation. 2. The Lower Tester retrieves the value for Conversation version counter by executing
GetConversationListing requests.
• Expected Outcome
Pass verdict
The values of the Conversation Version Counter are updated according to [3] after the participant has been added on the IUT.
MAP/MSE/MMB/BV-25-C [MSE updates Conversation-Listing version counter]
• Test Purpose
Verify that the MSE correctly updates the Conversation-Listing version counter when creating a conversation.
• Reference
[3] 3.1.15, 5.13, 3.1.9
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester has retrieved the current value of the Conversation-Listing Version Counter by having executed a GetConversationListing request.
• Test Procedure
1. On the IUT, create a new conversation. 2. The Lower Tester retrieves the values of the Conversation-Listing version counter by executing
GetConversationListing requests.
• Expected Outcome
Pass verdict
The value of the Conversation-Listing Version Counter is updated according to [3] after the conversation has been created on the IUT.
MAP/MSE/MMB/BV-34-C [MSE returns a list of conversations]
• Test Purpose
Verify that the MSE correctly responds to a request for a Conversation-Listing.
• Reference
[3] 5.13, 3.1.9
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT is configured to contain a Conversation-Listing object.
• Test Procedure
The Lower Tester requests a Conversation-Listing from the IUT.
• Expected Outcome
Pass verdict
The response to the Conversation-Listing request is correctly formatted according to [3].
MAP/MSE/MMB/BV-35-C [MSE returns a list of conversations filtered by a specific conversation]
• Test Purpose
Verify that the MSE correctly responds to a request for a Messages-Listing of all messages of a specific conversation.
• Reference
[3] 5.5, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT is configured to contain a Messages-Listing object for a specific conversation.
• Test Procedure
The Lower Tester requests a Messages-Listing of a specific conversation from the IUT.
• Expected Outcome
Pass verdict
The response to the Messages-Listing request is correctly formatted according to [3].
The response contains the specific messages of the requested conversation.
MAP/MSE/MMB/BV-36-C [MSE returns a list of messages in format v1.1]
• Test Purpose
Verify that the MSE correctly responds to a request for a Messages-Listing in format 1.1.
• Reference
[3] 5.5, 3.1.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT is configured to contain a Messages-Listing object.
- The Lower Tester has set its MapSupportedFeatures Bit 9 for Messages-Listing Format Version v1.1.
• Test Procedure
The Lower Tester requests a Messages-Listing from the IUT.
• Expected Outcome
Pass verdict
The response to the Messages-Listing request is correctly formatted according to [3] using Messages-Listing Format Version 1.1.
MAP/MSE/MMB/BV-37-C [MSE returns DatabaseIdentifier and FolderVersionCounter]
• Test Purpose
Verify that the MSE correctly responds to a request for a Messages-Listing with MaxListCount=0 including DatabaseIdentifier and FolderVersionCounter.
• Reference
[3] 5.5, 3.1.14, 3.1.15
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The Lower Tester sends a GetMessageListing request with MaxListCount set to zero.
• Expected Outcome
Pass verdict
The MSE returns DatabaseIdentifier and FolderVersionCounter in the GetMessageListing response according to [3].
MAP/MSE/MMB/BV-38-C [MSE returns ConversationListingVersionCounter, ConversationListingSize and DatabaseIdentifier]
• Test Purpose
Verify that the MSE correctly responds to a request for a Conversation-Listing with MaxListCount=0 including Conversation-ListingVersionCounter, ConversationListingSize and DatabaseIdentifier.
• Reference
[3] 5.13, 3.1.14, 3.1.15
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The Lower Tester sends a GetConversationListing request with MaxListCount set to zero.
• Expected Outcome
Pass verdict
The MSE returns the ConversationListingVersionCounter, ConversationListingSize and DatabaseIdentifier in the GetConversationListing response according to [3].
• Test Purpose
Verify that the MSE correctly responds to a request for a Conversation-Listing with Filtering for LastActivity.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has a conversation with more than one message from within a known activity period.
• Test Procedure
The Lower Tester sends a GetConversationListing request with FilterLastActivityBegin and FilterLastActivityEnd set to be within the known activity period of the messages in the requested conversation.
• Expected Outcome
Pass verdict
The MSE returns all messages from the requested conversation that fall into the requested activity period in the GetConversationListing response according to [3].
The GetConversationListing response is correctly formatted according to [3].
MAP/MSE/MMB/BV-40-C [MSE returns a list of conversations filtered by read status]
• Test Purpose
Verify that the MSE correctly responds to a request for a Conversation-Listing with Filtering by read status.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has a conversation with more than one message with a known read status.
• Test Procedure
The Lower Tester sends a GetConversationListing request with FilterReadStatus set to the known status of the messages in the requested conversation.
• Expected Outcome
Pass verdict
The MSE returns all messages of the request read status from the requested conversation in the GetConversationListing response according to [3].
The GetConversationListing response is correctly formatted according to [3].
• Test Purpose
Verify that the MSE correctly responds to a request for a Conversation-Listing with Filtering by recipient.
• Reference
[3] 5.13
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has a conversation with more than one message with a known recipient.
• Test Procedure
The Lower Tester sends a GetConversationListing request with FilterRecipient set to the known recipient of the messages in the requested conversation.
• Expected Outcome
Pass verdict
The MSE returns all messages of the request recipient from the requested conversation in the GetConversationListing response according to [3].
The GetConversationListing response is correctly formatted according to [3].
MAP/MSE/MMB/BV-42-C [MSE returns a list of conversations filtered by message handle]
• Test Purpose
Verify that the MSE correctly responds to a request for a Messages-Listing with Filtering by message handle.
• Reference
[3] 5.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has a conversation with more than one message with a known message handle.
• Test Procedure
The Lower Tester sends a GetMessagesListing request with FilterMessageHandle set to a valid message handle value.
• Expected Outcome
Pass verdict
The MSE returns the Messages-Listing object of the requested message in the GetMessagesListing response according to [3].
The GetMessagesListing response is correctly formatted according to [3].
• Test Purpose
Verify that the MSE updates the Conversation-Listing version counter when a new conversation is being created.
• Reference
[3] 3.1.15, 4.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Message Notification Service is active between IUT and the Lower Tester.
- The Lower Tester has set the current folder of the IUT to one non-empty folder which is not the ‘Delete’ folder. The Lower Tester has retrieved the Conversation-Listing of this folder.
- The IUT contains at least one folder which is not the 'Delete' folder and contains a message of type IM.
• Test Procedure
On the IUT, create a new conversation.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request with EventType ConversationChanged.
The IUT updates the value of the Conversation-ListingVersionCounter.
MAP/MSE/MMB/BV-44-C [MSE participant status change counter behavior]
• Test Purpose
Verify that the MSE does not change the conversation counter and Conversation-Listing counters when the presence, chat-state and LastActivity of a participant are changed.
• Reference
[3] 5.13, 3.1.15
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Message Notification Service is active between IUT and the Lower Tester.
- The Lower Tester has set the current folder of the IUT to one non-empty folder which is not the ‘Delete’ folder. The Lower Tester has retrieved the Conversation-Listing of this folder.
- The IUT contains at least one folder which is not the ‘Delete’ folder and contains a message of type IM.
• Test Procedure
1. On the IUT, change the presence, chat-state and LastActivity of a participant. 2. The Lower Tester sends a ‘GetConversationListing’ request to the IUT.
• Expected Outcome
Pass verdict
The IUT returns a ConversationListing with unchanged conversation and Conversation_ListingVersionCounter.
MAP/MSE/MMB/BV-45-C [MSE responds to owner status change request]
• Test Purpose
Verify that the MSE correctly responds to a request to change the presence, chat state and last activity datetime of the owner.
• Reference
[3] 5.11
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The Lower Tester sends a ‘SetOwnerStatus’ request to the IUT with new values for presence, chat state and last activity.
• Expected Outcome
Pass verdict
The ‘SetOwnerStatus’ response is well formatted according to [3].
MAP/MSE/MMB/BV-46-C [MSE returns owner status]
• Test Purpose
Verify that the MSE correctly responds to a request to get the presence, chat state and last activity datetime of the owner.
• Reference
[3] 5.12
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The Lower Tester sends a ‘GetOwnerStatus’ request to the IUT with a valid value for the ConversationID.
• Expected Outcome
Pass verdict
The ‘GetOwnerStatus’ response is well formatted according to [3].
• Test Purpose
Verify that the MSE correctly responds to a request to change the extended data of a message.
• Reference
[3] 3.1.13, 5.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The Lower Tester sends a ‘SetMessageStatus’ request to the IUT with new values for the extended data.
• Expected Outcome
Pass verdict
The ‘SetMessageStatus’ response is well formatted according to [3].

### 4.6 Delete Feature

Verify that the components that are specific to the Delete feature are properly implemented.

#### 4.6.1 IUT – Message Client Equipment (MCE)

Verify that the components that are specific to the Delete feature are properly implemented by the MCE.
MAP/MCE/MMD/BV-01-C [MCE deletes a message on the MSE]
• Test Purpose
Verify that the MCE can delete a message on the MSE.
• Reference
[3] 5.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to one non-empty folder which is not the ‘Delete’ folder. The IUT has retrieved the Messages-Listing of this folder.
- The Lower Tester contains at least one folder that is non-empty and which is not the ‘Delete’ folder.
• Test Procedure
1. The IUT requests the Lower Tester to change the status of one message that was contained in
the Messages-Listing object to “Delete”. 2. The IUT repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The request of the ‘SetMessageStatus’ function is well formatted according to [3].
The status of the messages has been set to ‘Delete’ and has been shifted to the ‘Delete’ folder.
MAP/MCE/MMD/BV-03-C [MCE requests removal of a message]
• Test Purpose
Verify that the MCE sends a correctly formatted request to permanently remove a message on the MSE.
• Reference
[3] 4.4
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to one non-empty folder which is not the ‘Delete’ folder. The IUT has retrieved the Conversation-Listing of this folder.
- The Lower Tester contains at least one folder that is non-empty and which is not the ‘Delete’ folder and contains a message of type IM.
• Test Procedure
The IUT requests the Lower Tester to change the status of one message of type IM that was contained in the Conversation-Listing object to ‘Delete’.
• Expected Outcome
Pass verdict
The request of the ‘SetMessageStatus’ function is well formatted according to [3].
The status of the message has been set to ‘Delete’ and has been shifted to the ‘Delete’ folder.

#### 4.6.2 IUT – Message Server Equipment (MSE)

Verify that the components that are specific to the Delete feature are properly implemented by the MSE.
MAP/MSE/MMD/BV-02-C [MSE deletes a message]
• Test Purpose
Verify that the MSE can delete a message on request of the MCE.
• Reference
[3] 5.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The current folder of the IUT has been set to one non-empty folder which is not the 'Delete' folder. The Lower Tester has retrieved the Messages-Listing of this folder.
- The Lower Tester has received a folders listing that is non-empty and which is not of the ‘Delete’ folder.
• Test Procedure
The Lower Tester requests the IUT to change the status of one message that was contained in the Messages-Listing object to “Delete”. The Lower Tester repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The response of the ‘SetMessageStatus’ function is well formatted according to [3].
The status of the messages has been set to ‘Delete’ and has been shifted to the ‘Delete’ folder.
MAP/MSE/MMD/BV-05-C [MSE removes a message]
• Test Purpose
Verify that the MSE correctly responds to a request to permanently remove a message.
• Reference
[3] 4.4
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
- The Lower Tester has set the current folder of the IUT to one non-empty folder which is not the ‘Delete’ folder. The Lower Tester has retrieved the Conversation-Listing of this folder.
- The IUT contains at least one folder that is non-empty and which is not the 'Delete' folder and contains a message of type IM.
• Test Procedure
The Lower Tester requests the IUT to change the status of one message of type IM that was contained in the Conversation-Listing object to “deleted”.
• Expected Outcome
Pass verdict
The IUT sends a ‘SetMessageStatus’ response that is well formatted according to [3].
The IUT sends a ‘SendEvent’ request with EventType ‘MessageRemoved’ or ‘MessageDeleted’ depending on the implementation of the IUT.

### 4.7 Uploading Feature

Verify that the components that are specific to the Uploading feature are properly implemented.

#### 4.7.1 IUT – Message Client Equipment (MCE)

Verify that the components that are specific to the Uploading feature are properly implemented by the MCE.
MAP/MCE/MMU/BV-01-C [MCE uploads a message to the MSE]
• Test Purpose
Verify that the MCE can upload a message to the MSE.
• Reference
[3] 5.8
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT contains at least one message.
• Test Procedure
The IUT sends a ‘PushMessage’ request to one of the MAP virtual folders supported by the Lower Tester. The IUT repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The request of the ‘PushMessage’ function is well formatted according to [3].
The message is received by the Lower Tester and stored correctly in the addressed folder.
MAP/MCE/MMU/BV-04-C [MCE uploads a conversation message to the MSE]
• Test Purpose
Verify that the MCE sends a correctly formatted request to add a message to a conversation.
• Reference
[3] 5.8
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT contains at least one message of type IM.
• Test Procedure
The IUT sends a ‘PushMessage’ request with a valid ConversationID Application Parameter.
• Expected Outcome
Pass verdict
The request of the ‘PushMessage’ function is well formatted according to [3].
The message is received by the Lower Tester and stored correctly in the addressed conversation.
MAP/MCE/MMU/BV-05-C [MCE requests to change the owner status]
• Test Purpose
Verify that the MCE sends a correctly formatted request to change the presence, chat state, and last activity datetime of the owner.
• Reference
[3] 5.11
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT sends a ‘SetOwnerStatus’ request to the Lower Tester with new values for presence, chat state, and last activity.
• Expected Outcome
Pass verdict
The request of the ‘SetOwnerStatus’ function is well formatted according to [3].
MAP/MCE/MMU/BV-06-C [MCE requests the owner status]
• Test Purpose
Verify that the MCE sends a correctly formatted request to get the presence, chat state, and last activity datetime of the owner.
• Reference
[3] 5.12
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
• Test Procedure
The IUT sends a ‘GetOwnerStatus’ request to the Lower Tester with a valid value for the ConversationID.
• Expected Outcome
Pass verdict
The request of the ‘GetOwnerStatus’ function is well formatted according to [3].

#### 4.7.2 IUT – Message Server Equipment (MSE)

Verify that the components that are specific to the Uploading feature are properly implemented by the MSE.
MAP/MSE/MMU/BV-02-C [MSE receives a message from the MCE for storage]
• Test Purpose
Verify that the MSE can receive a message uploaded by the MCE.
• Reference
[3] 5.8
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has at least one folder different from the outbox folder.
- The Lower Tester contains at least one message. At least one of the messages on the Lower Tester contains a valid ConversationID parameter.
• Test Procedure
The Lower Tester sends a ‘PushMessage’ request to the IUT. The Lower Tester repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The response of the ‘PushMessage’ function is well formatted according to [3].
The message is received by the IUT and stored correctly in the addressed folder.
MAP/MSE/MMU/BV-03-C [MSE receives a message from the MCE and sends it to the network]
• Test Purpose
Verify that the MSE can send a message as requested by the MCE.
• Reference
[3] 5.8
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester contains at least one message.
• Test Procedure
The Lower Tester sends a ‘PushMessage’ request to the IUT. The Lower Tester repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The response of the ‘PushMessage’ function is well formatted according to [3].
The message is received by the IUT.
The message has been sent by the IUT to the network.
The message has been shifted from the ‘Outbox’ folder to the ‘Sent’ folder.

### 4.8 Notification Feature

Verify the normal behavior of the components necessary to realize the Notification feature.

#### 4.8.1 IUT – Message Client Equipment (MCE)

Verify that the Message Client Equipment device can properly take advantage of the Notification feature and the Extended MAP-Event-Report feature.
MAP/MCE/MMN/BV-01-C [MCE receives a message notification (MAP-Event-Report Version 1.0)]
• Test Purpose
Verify that the MCE is properly notified of a new message.
• Reference
[3] 5.1
• Initial Condition
- The Lower Tester’s SDP Record does not contain the MapSupportedFeatures SDP attribute.
- The IUT and the Lower Tester have established a MAP session, and the Message Notification Service is active.
• Test Procedure
1. The Lower Tester sends a message notification to the IUT, in order to advertise the arrival of a
new message. 2. The Lower Tester repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The IUT can receive and decode the event-report object.
The response of the ‘SendEvent’ function is well formatted according to [3].
The message arrival event is signaled to the user.
• Notes
This test checks for legacy compatibility.
• Test Purpose
Verify that the MCE can correctly receive and parse a version 1.1 MAP-Event-Report.
• Reference
[3] 3.1.7.2
• Initial Condition
- The Lower Tester’s SDP Record does contain the MapSupportedFeatures SDP attribute and the MAP-Event-Report 1.1 bit is set.
- The IUT and the Lower Tester have established a MAP session and the Message Notification Service is active.
• Test Procedure
The Lower Tester sends MAP-Event-Reports to the IUT, one per event type.
• Expected Outcome
Pass verdict (to be verified for each event type)
The IUT can receive and decode the version 1.1 event-report objects.
The response of the ‘SendEvent’ function is well formatted according to [3].
MAP/MCE/MMN/BV-05-C [MCE requests to filter notifications]
• Test Purpose
Verify that the MCE sends a correctly formatted request to filter notifications.
• Reference
[3] 5.14
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT sends a ‘SetNotificationFilter’ request to the Lower Tester.
• Expected Outcome
Pass verdict
The 'SetNotificationFilter' request is well formatted according to [3].

#### 4.8.2 IUT – Message Server Equipment (MSE)

Verify that the Message Server Equipment device can properly implement the Notification feature and the Extended MAP-Event-Report feature.
MAP/MSE/MMN/BV-02-C [MSE sends a message notification (MAP-Event-Report Version 1.0)]
• Test Purpose
Verify that the MSE can send a message notification.
• Reference
[3] 5.1
• Initial Condition
- The Lower Tester’s SDP Record does not contain the MapSupportedFeatures SDP attribute.
- The IUT and the Lower Tester have established a MAP session and the Message Notification Service is active.
- The attribute ‘MASInstanceID’ of the related SDP record has the value i.
• Test Procedure
1. The IUT receives a new message. 2. The IUT repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The IUT sends an event-report object to the Lower Tester.
The request of the ‘SendEvent’ function is well formatted according to [3] and its application parameter MASInstanceID has the value i.
The message arrival event is signaled to the user.
MAP/MSE/MMN/BV-04-C [MSE sends a MAP-Event-Report Version 1.1]
• Test Purpose
Verify that the MSE can correctly generate and send version 1.1 MAP-Event-Reports. In this case a new Message event.
• Reference
[3] 5.1
• Initial Condition
- The Lower Tester’s SDP Record does contain the MapSupportedFeatures SDP attribute and the MAP-Event-Report 1.1 bit is set.
- The IUT and the Lower Tester have established a MAP session and the Message Notification Service is active.
- The attribute ‘MASInstanceID’ of the related SDP record has the value i.
• Test Procedure
1. The IUT receives a new message. 2. The IUT repeats the test for each message type supported by the IUT.
• Expected Outcome
Pass verdict (to be verified for each supported message type)
The IUT sends a version 1.1 event-report object to the Lower Tester.
The request of the ‘SendEvent’ function is well formatted according to [3] and its application parameter MASInstanceID has the value i.
The message arrival event is signaled to the user.
MAP/MSE/MMN/BV-06-C [MSE responds to notification filter]
• Test Purpose
Verify that the MSE correctly responds to a request to filter notifications.
• Reference
[3] 5.14
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and the Message Notification Service are active.
• Test Procedure
The Lower Tester sends a ‘SetNotificationFilter’ request to the IUT.
• Expected Outcome
Pass verdict
The IUT sends a ‘SetNotificationFilter’ response.
The ‘SetNotificationFilter' response is well formatted according to [3].
MAP/MSE/MMN/BV-07-C [MSE sends event-report in format v1.2]
• Test Purpose
Verify that the MSE sends an event-report in format 1.2.
• Reference
[3] 3.1.7.3
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT sends a ‘SendEvent’ request to the Lower Tester.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and is well formatted according to [3].
The MAP-event-report is in format v1.2.
MAP/MSE/MMN/BV-08-C [MSE sends event-report MessageExtendedDataChanged]
• Test Purpose
Verify that the MSE sends a “MessageExtendedDataChanged” event-report when the extended data of a message is changed.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to send a ‘MessageExtendedDataChanged’ event-report to the Lower Tester.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘MessageExtendedDataChanged’ event-report.
MAP/MSE/MMN/BV-09-C [MSE considers notification filtering]
• Test Purpose
Verify that the read status of a message is changed on the MSE, after the read status notification has been disabled via notification filtering, and ensure that there is no event-report for the read status.
• Reference
[3] 3.1.7, 5.14
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
- The Lower Tester has successfully disabled the read status notification on the IUT.
• Test Procedure
The read status of a message on the IUT is changed.
• Expected Outcome
Pass verdict
The IUT does not send an event-report for the read status.
• Test Purpose
Verify that the MSE sends a ‘ParticipantPresenceChanged’ event-report when the presence of a participant is changed.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to change the presence of a participant.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘ParticipantPresenceChanged’ event-report.
MAP/MSE/MMN/BV-11-C [MSE sends event-report on chat-state change]
• Test Purpose
Verify that the MSE sends a ‘ParticipantChatStateChanged’ event-report when the chat-state of a participant is changed.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to change the chat-state of a participant.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘ParticipantChatStateChanged’ event-report.
• Test Purpose
Verify that the MSE sends a ‘ConversationChanged’ event-report when a participant is added to a conversation.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to add a participant to a conversation.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘ConversationChanged’ event-report.
MAP/MSE/MMN/BV-13-C [MSE sends event-report on participant removal]
• Test Purpose
Verify that the MSE sends a ‘ConversationChanged’ event-report when a participant is removed from a conversation.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to remove a participant from a conversation.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘ConversationChanged’ event-report.
• Test Purpose
Verify that the MSE sends a ‘MessageRemoved’ event-report when a message is removed from a conversation.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to remove (not delete) a message.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘MessageRemoved’ event-report.
MAP/MSE/MMN/BV-15-C [MSE sends event-report on presence change of the owner]
• Test Purpose
Verify that the MSE sends a ‘ParticipantPresenceChanged’ event-report when the presence of the owner is changed on the IUT.
• Reference
[3] 3.1.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to change the presence of the owner.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘ParticipantPresenceChanged’ event-report.
• Test Purpose
Verify that the MSE sends a ‘ParticipantChatStateChanged’ event-report when the chat state of the owner is changed on the IUT.
• Reference
[3] 3.1.7, 5.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service and Message Notification Service are active.
• Test Procedure
The IUT is triggered to change the chat state of the owner.
• Expected Outcome
Pass verdict
The IUT sends a ‘SendEvent’ request and it is well formatted according to [3].
The ‘SendEvent’ request contains the ‘ParticipantChatStateChanged’ event-report.

### 4.9 Instance Information Feature

Verify the normal behavior of the components necessary to realize the MAS Instance Information Feature.

#### 4.9.1 IUT – Message Client Equipment (MCE)

Verify that the Message Client Equipment device can properly take advantage of the Instance Information Feature.
MAP/MCE/MMI/BV-01-C [MCE reads the MAS-instance information from the MSE]
• Test Purpose
Verify that the MCE can retrieve user-readable information about the MAS-instance from the MSE.
• Reference
[3] 5.10
• Initial Condition
- The IUT and the Lower Tester have established a MAP MAS connection.
• Test Procedure
1. The IUT sends a ‘GetMASInstanceInformation’ request to the Lower Tester. 2. The Lower Tester delivers the requested MAS-instance information in the Body/End of Body
header of its response.
• Expected Outcome
Pass verdict
The request of the ‘GetMASInstanceInformation’ function is well formatted according to [3].
The MAS-instance information string can be properly retrieved by the IUT.
• Notes
The information in the Body/End of Body header is a UTF8 string.

#### 4.9.2 IUT – Message Server Equipment (MSE)

Verify that the Message Server Equipment device can properly implement the Instance Information feature.
MAP/MSE/MMI/BV-02-C [MSE returns the MAS-instance information to the MCE]
• Test Purpose
Verify that the MSE can return user-readable information about the MAS-instance to the MCE.
• Reference
[3] 5.10
• Initial Condition
- The IUT and the Lower Tester have established a MAP MAS connection.
• Test Procedure
1. The IUT receives a ‘GetMASInstanceInformation’ request from the Lower Tester. 2. The IUT delivers the requested MAS-instance information in the Body/End of Body header of its
response.
• Expected Outcome
Pass verdict
The response of the ‘GetMASInstanceInformation’ function is well formatted according to [3].
The MAS-instance information string retrieved by the Lower Tester corresponds to the IUT’s instance.
• Notes
The information in the Body/End of Body header is a UTF8 string.

### 4.10 SDP MapSupportedFeatures Bits

Verify that the MapSupportedFeatures advertised in the SDP record match the supported features listed in the Implementation Conformance Statement [4].

#### 4.10.1 IUT – Message Client Equipment (MCE)

Verify that the Message Client Equipment device can properly take advantage of the SDP MapSupportedFeatures Bits.
• Test Purpose
Verify that the MCE correctly advertises the correct feature bits in the MNS SDP record.
• Reference
[3] 7.1
• Initial Condition
- The IUT is in discoverable and connectable mode.
• Test Procedure
The Lower Tester retrieves the MapSupportedFeatures attribute from the MNS SDP record.
• Expected Outcome
Pass verdict
The feature bits correspond to the Implementation Conformance Statement (ICS) [4].
MAP/MCE/MFB/BV-03-C [MCE MNS MapSupportedFeatures bits after MAS connection establishment]
• Test Purpose
Verify that the MCE correctly advertises the correct feature bits in the MNS SDP record during MAS connection.
• Reference
[3] 7.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP MAS connection.
- There is no MAP MNS connection that exists between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester retrieves the MapSupportedFeatures attribute from the MNS SDP record.
• Expected Outcome
Pass verdict
The feature bits correspond to the Implementation Conformance Statement (ICS) [4].
MAP/MCE/MFB/BV-04-C [MCE MNS MapSupportedFeatures bits after MNS connection establishment]
• Test Purpose
Verify that the MCE correctly advertises the correct feature bits in the MNS SDP record during MNS connection.
• Reference
[3] 7.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP MNS connection.
• Test Procedure
The Lower Tester retrieves the MapSupportedFeatures attribute from the MNS SDP record.
• Expected Outcome
Pass verdict
The feature bits correspond to the Implementation Conformance Statement (ICS) [4].
MAP/MCE/MFB/BV-06-C [MCE sends an OBEX connect request with its MAPSupportedFeatures bitmask]
• Test Purpose
Verify that the MCE sends its MapSupportedFeatures in the OBEX Connect request if the MSE declares support for the feature “MapSupportedFeatures in Connect Request” in its SDP record.
• Reference
[3] 6.4.1
• Initial Condition
- The Lower Tester declares support for the feature “MapSupportedFeatures in Connect Request” in its SDP record.
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
The IUT establishes a MAP session with the Lower Tester by sending an OBEX Connect request to the Lower Tester according to the connection parameter defined by the Lower Tester’s MAS SDP record.
• Expected Outcome
Pass verdict
The OBEX Connect request from the IUT contains the MapSupportedFeatures Application Parameter according to its supported features.
The OBEX Connect response messages related to the MAS have been exchanged properly so the MAS service is established.

#### 4.10.2 IUT – Message Server Equipment (MSE)

Verify that the Message Server Equipment device can properly implement the SDP MapSupportedFeatures Bits.
MAP/MSE/MFB/BV-02-C [MSE MAS MapSupportedFeatures bits]
• Test Purpose
Verify that the MSE correctly advertises the correct MapSupportedFeatures bits in the MAS SDP record.
• Reference
[3] 7.1
• Initial Condition
- The IUT is in discoverable and connectable mode.
• Test Procedure
The Lower Tester retrieves the MapSupportedFeatures attribute from the MAS SDP record.
• Expected Outcome
Pass verdict
The feature bits correspond to the Implementation Conformance Statement (ICS) [4].
MAP/MSE/MFB/BV-05-C [MSE MAS Support Feature bits during MAS connection]
• Test Purpose
Verify that the MSE correctly advertises the correct MapSupportedFeatures bits in the MAS SDP record during MAS connection.
• Reference
[3] 7.1
• Initial Condition
- The IUT and the Lower Tester have established a MAP MAS connection.
• Test Procedure
The Lower Tester retrieves the MapSupportedFeatures attribute from the MAS SDP record.
• Expected Outcome
Pass verdict
The feature bits correspond to the Implementation Conformance Statement (ICS) [4].
MAP/MSE/MFB/BV-07-C [MSE responds to an OBEX connect request with its MapSupportedFeatures bitmask]
• Test Purpose
Verify that the MSE responds to an OBEX connect request if the MSE declares support for the feature “MapSupportedFeatures in Connect Request” in its SDP record.
• Reference
[3] 6.4.1
• Initial Condition
- The IUT declares support for the feature “MapSupportedFeatures in Connect Request” in its SDP record.
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable mode.
• Test Procedure
The Lower Tester establishes a MAP session with the IUT by sending an OBEX Connect request to the IUT according to the connection parameters defined by the IUT’s MAS SDP record.
• Expected Outcome
Pass verdict
The OBEX Connect response messages related to the MAS have been exchanged properly so the MAS service is established.

### 4.11 Message Forwarding Message Handling

Verify that the components that are specific to the Message Forwarding feature are properly implemented by the MCE and the MSE.

#### 4.11.1 IUT – Message Client Equipment (MCE)

MAP/MCE/MFMH/BV-01-C [PushMessage request including ‘MessageHandle’]
• Test Purpose
Verify that the MCE sends a correctly formatted PushMessage request including MessageHandle Application Parameter.
• Reference
[3] 4.7, 5.8.4.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Upper Tester invokes the IUT to send PushMessage request with the Application Parameter MessageHandle set to a valid message handle.
• Expected Outcome
Pass verdict
The request of the ‘PushMessage’ function is correctly formatted according to [3].
MAP/MCE/MFMH/BV-02-C [PushMessage request ‘Attachment’ ‘ON’]
• Test Purpose
Verify that the MCE sends a correctly formatted PushMessage request including Application Parameter ‘Attachment’=ON.
• Reference
[3] 5.8.4.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Upper Tester invokes the IUT to send a PushMessage request with Application Parameter ‘Attachment’=ON.
• Expected Outcome
Pass verdict
The request of the ‘PushMessage’ function is well formatted according to [3].
MAP/MCE/MFMH/BV-03-C [PushMessage request ‘Attachment’ ‘OFF’]
• Test Purpose
Verify that the MCE sends a correctly formatted PushMessage request including Application Parameter ‘Attachment’=OFF.
• Reference
[3] 5.8.4.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Upper Tester invokes the IUT to send a PushMessage request with Application Parameter ‘Attachment’=OFF.
• Expected Outcome
Pass verdict
The request of the 'PushMessage' function is well formatted according to [3].
MAP/MCE/MFMH/BV-04-C [PushMessage request ModifyText ‘REPLACE’]
• Test Purpose
Verify that the MCE sends a correctly formatted PushMessage request including Application Parameter ModifyText=REPLACE.
• Reference
[3] 5.8.4.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Upper Tester invokes the IUT to send a PushMessage request with Application Parameter ModifyText=REPLACE.
• Expected Outcome
Pass verdict
The request of the ‘PushMessage’ function is well formatted according [3].
MAP/MCE/MFMH/BV-05-C [PushMessage request ModifyText ‘PREPEND’]
• Test Purpose
Verify that the MCE sends a correctly formatted PushMessage request including Application Parameter ModifyText=PREPEND.
• Reference
[3] 5.8.4.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The Lower Tester contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The IUT has set the current folder of the Lower Tester to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Upper Tester invokes the IUT to send a PushMessage request with Application Parameter ModifyText=PREPEND.
• Expected Outcome
Pass verdict
The request of the ‘PushMessage’ function is well formatted according to [3].

#### 4.11.2 IUT – Message Server Equipment (MSE)

MAP/MSE/MFMH/BV-01-C [PushMessage response for ‘MessageHandle’]
• Test Purpose
Verify that the MSE sends a correctly formatted response to a PushMessage request including MessageHandle application parameter.
• Reference
[3] 4.7, 5.8.4.5
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT The Lower Tester contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The Lower Tester has set the current folder of the IUT to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Lower Tester sends a PushMessage request with the Application Parameter MessageHandle set to a valid message handle.
• Expected Outcome
Pass verdict
The IUT response to the ‘PushMessage’ request is well formatted according to [3].
MAP/MSE/MFMH/BV-02-C [PushMessage response ‘Attachment’ ‘ON’]
• Test Purpose
Verify that the MSE sends a correctly formatted response to a PushMessage request including application parameter ‘Attachment’=ON.
• Reference
[3] 5.8.4.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The Lower Tester has set the current folder of the IUT to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Lower Tester sends a PushMessage request with Application Parameter ‘Attachment’=ON.
• Expected Outcome
Pass verdict
The response of the ‘PushMessage’ function is well formatted according to [3].
The message is forwarded including the attachments of the original message.
• Test Purpose
Verify that the MSE sends a correctly formatted response to a PushMessage request including application parameter ‘Attachment’=OFF.
• Reference
[3] 5.8.4.6
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The Lower Tester has set the current folder of the IUT to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Lower Tester sends a PushMessage request with Application Parameter ‘Attachment’=OFF.
• Expected Outcome
Pass verdict
The request of the ‘PushMessage’ function is well formatted according to [3].
The message is forwarded without attachments.
MAP/MSE/MFMH/BV-04-C [PushMessage response ModifyText ‘REPLACE’]
• Test Purpose
Verify that the MSE sends a correctly formatted response to a PushMessage request including application parameter ModifyText=REPLACE.
• Reference
[3] 5.8.4.7
• Initial Condition
- The IUT contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The Lower Tester has set the current folder of the Lower IUT to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Lower Tester sends a PushMessage request with Application Parameter ModifyText=REPLACE.
• Expected Outcome
Pass verdict
The response of the ‘PushMessage’ function is well formatted according to [3]. The message is forwarded with the textual content of the replaced text.
• Test Purpose
Verify that the MSE sends a correctly formatted response to a PushMessage request including application parameter ModifyText=PREPEND.
• Reference
[3] 5.8.4.7
• Initial Condition
- The IUT and the Lower Tester have established a MAP session. In that MAP session, the Message Access Service is active.
- The IUT contains at least one folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
- The Lower Tester has set the current folder of the IUT to a folder that includes at least one bmessage (type=EMAIL) with textual content and attachment.
• Test Procedure
The Lower Tester sends a PushMessage request with Application Parameter ModifyText=PREPEND.
• Expected Outcome
Pass verdict
The response of the ‘PushMessage’ function is well formatted according to [3].
The message is forwarded with the new textual content containing the prepended text and the original message.

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.
The columns for the TCMT are defined as follows:
Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for the Message Access Profile (MAP) [4].
Feature: A brief, informal description of the feature being tested.
Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [2].
For the purpose and structure of the ICS/IXIT, refer to [2].

|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 2/2 OR MAP 2/3 OR MAP 2/4 OR MAP 2/5 |  |  | Session Management MAS (MCE) |  |  | MAP/MCE/MSM/BV-01-C MAP/MCE/MSM/BV-04-C |  |  |
| MAP 2/1 OR MAP 2/5 |  |  | Session Management MAS and MNS (MCE) |  |  | MAP/MCE/MSM/BV-02-C MAP/MCE/MSM/BV-03-C |  |  |
| MAP 3/2 OR MAP 3/3 OR MAP 3/4 OR MAP 3/5 |  |  | Session Management MAS (MSE) |  |  | MAP/MSE/MSM/BV-05-C MAP/MSE/MSM/BV-08-C |  |  |
| MAP 3/1 OR MAP 3/5 |  |  | Session Management MAS and MNS (MSE) |  |  | MAP/MSE/MSM/BV-06-C MAP/MSE/MSM/BV-07-C |  |  |
| (MAP 3/2 OR MAP 3/3 OR MAP 3/4 OR MAP 3/5) AND MAP 3/2g |  |  | Session Management Multiple MAS (MSE) |  |  | MAP/MSE/MSM/BV-09-C |  |  |
| (MAP 3/1 OR MAP 3/5) AND MAP 3/2g |  |  | Session Management Multiple MAS and MNS (MSE) |  |  | MAP/MSE/MSM/BV-10-C MAP/MSE/MSM/BV-11-C MAP/MSE/MSM/BV-12-C |  |  |
| (MAP 2/1 OR MAP 2/5) AND MAP 2/2h |  |  | Session Management Multiple MAS and MNS (MCE) |  |  | MAP/MCE/MSM/BV-13-C MAP/MCE/MSM/BV-14-C |  |  |
| MAP 2/5a |  |  | Message Notification Registration (MCE) |  |  | MAP/MCE/MNR/BV-01-C MAP/MCE/MNR/BV-02-C |  |  |
| MAP 3/5a |  |  | Message Notification Registration (MSE) |  |  | MAP/MSE/MNR/BV-03-C MAP/MSE/MNR/BV-04-C |  |  |
| MAP 2/2 OR MAP 2/3 |  |  | Message Browsing/ Message Uploading: Folder Navigation (MCE) |  |  | MAP/MCE/MMB/BV-01-C MAP/MCE/MMB/BV-02-C |  |  |
| MAP 2/2 |  |  | Message Browsing: Messages Listing (MCE) |  |  | MAP/MCE/MMB/BV-03-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 2/2d AND MAP 2/6a |  |  | Message Browsing: Get EMAIL Message (MCE) |  |  | MAP/MCE/MMB/BV-04-C |  |  |
| MAP 2/2d AND MAP 2/6d |  |  | Message Browsing: Get MMS Message (MCE) |  |  | MAP/MCE/MMB/BV-17-C |  |  |
| MAP 2/2d AND (MAP 2/6b OR MAP 2/6c) |  |  | Message Browsing: Get SMS Message (MCE) |  |  | MAP/MCE/MMB/BV-06-C |  |  |
| MAP 2/2e |  |  | Message Browsing: Set Message Status (MCE) |  |  | MAP/MCE/MMB/BV-07-C |  |  |
| MAP 2/2f |  |  | Message Browsing: Update Inbox (MCE) |  |  | MAP/MCE/MMB/BV-08-C |  |  |
| MAP 20/1 OR MAP 20/2 OR MAP 20/3 OR MAP 20/4 OR MAP 20/5 OR MAP 20/6 OR MAP 20/7 |  |  | Message Browsing: Messages Listing using filters (MCE) |  |  | MAP/MCE/MMB/BV-19-C |  |  |
| MAP 3/2 OR MAP 3/3 |  |  | Message Browsing/ Message Uploading: Folder Navigation (MSE) |  |  | MAP/MSE/MMB/BV-09-C MAP/MSE/MMB/BV-10-C |  |  |
| MAP 3/2 |  |  | Message Browsing: Messages Listing (MSE) |  |  | MAP/MSE/MMB/BV-11-C MAP/MSE/MMB/BV-20-C |  |  |
| MAP 3/2d AND MAP 3/6a |  |  | Message Browsing: Get EMAIL Message (MSE) |  |  | MAP/MSE/MMB/BV-12-C |  |  |
| MAP 3/2d AND MAP 3/6d |  |  | Message Browsing: Get MMS Message (MSE) |  |  | MAP/MSE/MMB/BV-18-C |  |  |
| MAP 3/2d AND (MAP 3/6b OR MAP 3/6c) |  |  | Message Browsing: Get SMS Message (MSE) |  |  | MAP/MSE/MMB/BV-13-C MAP/MSE/MMB/BV-14-C |  |  |
| MAP 3/2e |  |  | Message Browsing: Set Message Status (MSE) |  |  | MAP/MSE/MMB/BV-15-C |  |  |
| MAP 3/2f |  |  | Message Browsing: Update Inbox (MSE) |  |  | MAP/MSE/MMB/BV-16-C |  |  |
| MAP 2/4a |  |  | Message Delete (MCE) |  |  | MAP/MCE/MMD/BV-01-C |  |  |
| MAP 3/4a |  |  | Message Delete (MSE) |  |  | MAP/MSE/MMD/BV-02-C |  |  |
| MAP 2/3 |  |  | Message Uploading (MCE) |  |  | MAP/MCE/MMU/BV-01-C |  |  |
| MAP 3/3 |  |  | Message Uploading (MSE) |  |  | MAP/MSE/MMU/BV-02-C MAP/MSE/MMU/BV-03-C |  |  |
| MAP 2/1a |  |  | Message Notification (MCE) |  |  | MAP/MCE/MMN/BV-01-C |  |  |
| MAP 3/1a |  |  | Message Notification (MSE) |  |  | MAP/MSE/MMN/BV-02-C |  |  |
| MAP 2/1a AND MAP 2/8a |  |  | Message Notification (MCE) |  |  | MAP/MCE/MMN/BV-03-C |  |  |
| MAP 3/1a AND MAP 3/8a |  |  | Message Notification (MSE) |  |  | MAP/MSE/MMN/BV-04-C |  |  |
| MAP 2/7a |  |  | Instance Information (MCE) |  |  | MAP/MCE/MMI/BV-01-C |  |  |
| MAP 3/7a |  |  | Instance Information (MCE) |  |  | MAP/MSE/MMI/BV-02-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 2/1 |  |  | Supported Feature Bits (MCE) |  |  | MAP/MCE/MFB/BV-01-C MAP/MCE/MFB/BV-03-C MAP/MCE/MFB/BV-04-C |  |  |
| MAP 1/1 |  |  | Supported Feature Bits (MSE) |  |  | MAP/MSE/MFB/BV-02-C MAP/MSE/MFB/BV-05-C |  |  |
| MAP 2/6e AND MAP 2/2d |  |  | Request bMessage with type ‘IM’ |  |  | MAP/MCE/MMB/BV-21-C |  |  |
| MAP 3/6e AND MAP 3/2d |  |  | Response to bMessage request with type ‘IM’ |  |  | MAP/MSE/MMB/BV-22-C |  |  |
| MAP 3/13a |  |  | Update Folder Version Counter |  |  | MAP/MSE/MMB/BV-23-C |  |  |
| MAP 3/13b AND MAP 3/19 |  |  | Update Conversation Version Counter |  |  | MAP/MSE/MMB/BV-24-C |  |  |
| MAP 3/13b AND MAP 3/13c AND MAP 3/19 |  |  | Update Conversation-Listing Version Counter |  |  | MAP/MSE/MMB/BV-25-C |  |  |
| MAP 2/2i AND MAP 2/19 |  |  | Request Conversation-Listing Filtering LastActivity Filtering read status Filtering recipient |  |  | MAP/MCE/MMB/BV-26-C MAP/MCE/MMB/BV-30-C MAP/MCE/MMB/BV-31-C MAP/MCE/MMB/BV-32-C |  |  |
| MAP 2/2c AND MAP 20/8 |  |  | Request Messages-Listing by conversation |  |  | MAP/MCE/MMB/BV-27-C |  |  |
| MAP 2/2c AND MAP 2/12 AND MAP 2/13a |  |  | Request Messages-Listing DatabaseIdentifer and FolderVersionCounter |  |  | MAP/MCE/MMB/BV-28-C |  |  |
| MAP 2/2i AND MAP 2/13c AND MAP 2/12 AND MAP 2/19 |  |  | Request Conversation-Listing Version Counter, Size and Identifier |  |  | MAP/MCE/MMB/BV-29-C |  |  |
| MAP 3/2h AND MAP 3/19 |  |  | Respond to request for Conversation-Listing Respond to request with Filter Last Acitvity Respond to request with Filter read status Respond to request with Filter recipient |  |  | MAP/MSE/MMB/BV-34-C MAP/MSE/MMB/BV-39-C MAP/MSE/MMB/BV-40-C MAP/MSE/MMB/BV-41-C |  |  |
| MAP 3/2c AND MAP 3/6e |  |  | Respond to request for Messages-Listing for a specific conversation |  |  | MAP/MSE/MMB/BV-35-C |  |  |
| MAP 3/2c AND MAP 3/10b |  |  | Respond to request for Messages-Listing v1.1 |  |  | MAP/MSE/MMB/BV-36-C |  |  |
| MAP 3/2c AND MAP 3/12 AND MAP 3/13a AND MAP 3/6e |  |  | Respond to request for DatabaseIdentifier and FolderVersionCounter |  |  | MAP/MSE/MMB/BV-37-C |  |  |
| MAP 3/2h AND MAP 3/13c AND MAP 3/19 |  |  | Respond to request for Conversation-Listing Respond to request with Version Counter, Size and Identifier |  |  | MAP/MSE/MMB/BV-38-C |  |  |
| MAP 2/2c AND MAP 2/6e |  |  | Filtering Messages-Listing for message |  |  | MAP/MCE/MMB/BV-33-C |  |  |
| MAP 3/2c AND MAP 3/6e |  |  | Respond to Messages-Listing request with message handle |  |  | MAP/MSE/MMB/BV-42-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 2/4a AND MAP 2/6e |  |  | Request message removal |  |  | MAP/MCE/MMD/BV-03-C |  |  |
| MAP 2/4a AND MAP 2/6e |  |  | Request to change message extended data |  |  | MAP/MCE/MMB/BV-48-C |  |  |
| MAP 2/3c AND MAP 2/6e |  |  | Request adding a message |  |  | MAP/MCE/MMU/BV-04-C |  |  |
| MAP 2/3d AND MAP 2/6e |  |  | Request to change owner values |  |  | MAP/MCE/MMU/BV-05-C |  |  |
| MAP 3/2e AND MAP 3/6e |  |  | Respond to removal request |  |  | MAP/MSE/MMD/BV-05-C |  |  |
| MAP 3/2e AND MAP 3/6e |  |  | Respond to message extended data change request |  |  | MAP/MSE/MMB/BV-47-C |  |  |
| MAP 3/3c AND MAP 3/13c AND MAP 3/6e |  |  | New conversation creation |  |  | MAP/MSE/MMB/BV-43-C |  |  |
| MAP 3/2h AND MAP 3/6e |  |  | Participant and owner presence change behavior |  |  | MAP/MSE/MMB/BV-44-C MAP/MSE/MMB/BV-46-C |  |  |
| MAP 3/3d AND MAP 3/6e AND MAP 3/20 |  |  | Response to owner status change request |  |  | MAP/MSE/MMB/BV-45-C |  |  |
| MAP 2/17 |  |  | Request to filter notifications |  |  | MAP/MCE/MMN/BV-05-C |  |  |
| MAP 3/17 |  |  | Response to filter notification request |  |  | MAP/MSE/MMN/BV-06-C |  |  |
| MAP 3/8b AND MAP 3/1a |  |  | Event-report format 1.2 Notification behavior remove message |  |  | MAP/MSE/MMN/BV-07-C MAP/MSE/MMN/BV-14-C |  |  |
| MAP 3/1a AND MAP 3/6e |  |  | MessageExtendedDataChanged Notification |  |  | MAP/MSE/MMN/BV-08-C |  |  |
| MAP 3/17 AND MAP 3/6e |  |  | Behavior read status notification disabled |  |  | MAP/MSE/MMN/BV-09-C |  |  |
| MAP 3/1a AND MAP 3/14 |  |  | Notification behavior change presence or add or remove participant |  |  | MAP/MSE/MMN/BV-10-C MAP/MSE/MMN/BV-12-C MAP/MSE/MMN/BV-13-C |  |  |
| MAP 3/1a AND MAP 3/15 |  |  | Participant and owner chat-state change behavior |  |  | MAP/MSE/MMN/BV-11-C MAP/MSE/MMN/BV-16-C |  |  |
| MAP 2/3e AND MAP 2/20 |  |  | Request to get the owner status |  |  | MAP/MCE/MMU/BV-06-C |  |  |
| MAP 3/2e AND MAP 3/20 |  |  | Response to get the owner status |  |  | MAP/MSE/MMN/BV-15-C |  |  |
| MAP 2/1 |  |  | MapSupportedFeatures bitmask (MCE) |  |  | MAP/MCE/MFB/BV-06-C |  |  |
| MAP 1/1 |  |  | MapSupportedFeatures bitmask (MSE) |  |  | MAP/MSE/MFB/BV-07-C |  |  |
| MAP 2/21 AND MAP 2/3c AND MAP 2/6a |  |  | PushMessage request including ‘MessageHandle’ |  |  | MAP/MCE/MFMH/BV-01-C |  |  |
| MAP 3/21 AND MAP 3/3c AND MAP 3/6a |  |  | PushMessage response for ‘MessageHandle’ |  |  | MAP/MSE/MFMH/BV-01-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 2/21 AND MAP 2/3c AND MAP 2/6a |  |  | PushMessage request ‘Attachment’ |  |  | MAP/MCE/MFMH/BV-02-C MAP/MCE/MFMH/BV-03-C |  |  |
| MAP 3/21 AND MAP 3/3c AND MAP 3/6a |  |  | PushMessage response ‘Attachment’ |  |  | MAP/MSE/MFMH/BV-02-C MAP/MSE/MFMH/BV-03-C |  |  |
| MAP 2/21 AND MAP 2/3c AND MAP 2/6a |  |  | PushMessage request ModifyText |  |  | MAP/MCE/MFMH/BV-04-C MAP/MCE/MFMH/BV-05-C |  |  |
| MAP 3/21 AND MAP 3/3c AND MAP 3/6a |  |  | PushMessage response ModifyText |  |  | MAP/MSE/MFMH/BV-04-C MAP/MSE/MFMH/BV-05-C |  |  |
| MAP 7b/2 AND MAP 3/3c |  |  | Process an incoming PUT request from a legacy device (OBEX over RFCOMM is used) |  |  | MAP/MSE/GOEP/BC/BV-01-C |  |  |
| MAP 7b/2 AND MAP 2/3c |  |  | Initiate a PUT request to a legacy device (OBEX over RFCOMM is used) |  |  | MAP/MCE/GOEP/BC/BV-02-C |  |  |
| MAP 7b/2 AND (MAP 3/2b OR MAP 3/2c OR MAP 3/2d OR MAP 3/3b) |  |  | Process an incoming GET request from a legacy device (OBEX over RFCOMM is used) |  |  | MAP/MSE/GOEP/BC/BV-03-C |  |  |
| MAP 7b/2 AND (MAP 2/2b OR MAP 2/2c OR MAP 2/2d OR MAP 2/3b) |  |  | Initiate a GET request to a legacy device (OBEX over RFCOMM is used) |  |  | MAP/MCE/GOEP/BC/BV-04-C |  |  |
| MAP 7b/1 AND MAP 1/2 |  |  | IUT issues an OBEX CONNECT request |  |  | MAP/MCE/GOEP/CON/BV-01-C |  |  |
| MAP 7b/1 AND MAP 3/1 |  |  | IUT issues an OBEX CONNECT request |  |  | MAP/MSE/GOEP/CON/BV-01-C |  |  |
| MAP 1/1 AND MAP 7b/1 |  |  | MAP MSE SDP attribute: GoepL2CapPsm |  |  | MAP/MSE/SGSIT/ATTR/BV-04-C |  |  |
| MAP 2/1 AND MAP 7b/1 |  |  | MAP MCE SDP attribute: GoepL2CapPsm |  |  | MAP/MCE/SGSIT/ATTR/BV-11-C |  |  |
| MAP 7b/1 AND MAP 2/3c |  |  | IUT issues a PUT request with SRM enabled – Initiate PUT |  |  | MAP/MCE/GOEP/SRM/BV-03-C |  |  |
| MAP 7b/1 AND MAP 3/3c |  |  | IUT issues a PUT response with SRM enabled – Receive PUT |  |  | MAP/MSE/GOEP/SRM/BV-04-C |  |  |
| MAP 7b/1 AND (MAP 2/2b OR MAP 2/2c OR MAP 2/2d OR MAP 2/3b) |  |  | IUT issues a GET request with SRM enabled – Initiate GET |  |  | MAP/MCE/GOEP/SRM/BV-07-C |  |  |
| MAP 7b/1 AND (MAP 3/2b OR MAP 3/2c OR MAP 3/2d OR MAP 3/3b) |  |  | IUT issues a GET response w/ SRM enabled – Receive GET |  |  | MAP/MSE/GOEP/SRM/BV-08-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 7b/1 AND MAP 3/3c |  |  | Process a PUT request with an invalid SRM header |  |  | MAP/MSE/GOEP/SRM/BI-02-C |  |  |
| MAP 7b/1 AND MAP 1/1 |  |  | Process an OBEX CONNECT request (incorrectly) containing a SRM header |  |  | MAP/MSE/GOEP/SRM/BI-03-C |  |  |
| MAP 7b/1 AND (MAP 3/2b OR MAP 3/2c OR MAP 3/2d OR MAP 3/3b) |  |  | Process a GET request with an invalid SRM header |  |  | MAP/MSE/GOEP/SRM/BI-05-C |  |  |
| MAP 7b/1 AND MAP 2/3c |  |  | IUT receives a PUT response with SRM enabled and a SRMP wait header |  |  | MAP/MCE/GOEP/SRMP/BV-01-C |  |  |
| MAP 7b/1 AND (MAP 3/2b OR MAP 3/2c OR MAP 3/2d OR MAP 3/3b) |  |  | IUT receives a GET request with SRM enabled and a SRMP wait header |  |  | MAP/MSE/GOEP/SRMP/BV-02-C |  |  |
| MAP 7b/1 AND MAP 3/3c AND MAP 15/11 |  |  | IUT does not include an invalid SRMP header in the PUT response |  |  | MAP/MSE/GOEP/SRMP/BV-03-C |  |  |
| MAP 7b/1 AND MAP 10/11 AND (MAP 2/2b OR MAP 2/2c OR MAP 2/2d OR MAP 2/3b) |  |  | IUT does not include an invalid SRMP header in the GET request |  |  | MAP/MCE/GOEP/SRMP/BV-04-C |  |  |
| MAP 7b/1 AND (MAP 2/2b OR MAP 2/2c OR MAP 2/2d OR MAP 2/3b) AND MAP 10/11 |  |  | IUT and Lower Tester include a SRMP header during the GET operation |  |  | MAP/MCE/GOEP/SRMP/BV-05-C |  |  |
| MAP 7b/1 AND (MAP 2/2b OR MAP 2/2c OR MAP 2/2d OR MAP 2/3b) |  |  | IUT receives a GET response with SRM enabled and a SRMP wait header |  |  | MAP/MCE/GOEP/SRMP/BV-06-C |  |  |
| MAP 7b/1 AND (MAP 2/2b OR MAP 2/2c OR MAP 2/2d OR MAP 2/3b) |  |  | IUT ignores an invalid SRMP header from Server during a GET operation (SRM enabled) |  |  | MAP/MCE/GOEP/SRMP/BI-01-C |  |  |
| MAP 7b/1 AND (MAP 3/2b OR MAP 3/2c OR MAP 3/2d OR MAP 3/3b) |  |  | IUT ignores an invalid SRMP header from the Client during a GET operation (SRM enabled) |  |  | MAP/MSE/GOEP/SRMP/BI-02-C |  |  |
| MAP 7b/1 AND MAP 1/1 |  |  | IUT (Action commands not supported) is able to reject an incoming ACTION command |  |  | MAP/MSE/GOEP/ROB/BV-01-C |  |  |
| MAP 7b/1 AND MAP 2/1 |  |  | IUT (Action commands not supported) is able to reject an incoming ACTION command |  |  | MAP/MCE/GOEP/ROB/BV-01-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAP 7b/1 AND MAP 1/1 |  |  | IUT (Reliable Sessions not supported) is able to reject the request to create a Reliable Session |  |  | MAP/MSE/GOEP/ROB/BV-02-C |  |  |
| MAP 7b/1 AND MAP 2/1 |  |  | IUT (Reliable Sessions not supported) is able to reject the request to create a Reliable Session |  |  | MAP/MCE/GOEP/ROB/BV-02-C |  |  |
| MAP 2/1 |  |  | MAP MCE Notification Service Discovery |  |  | MAP/MCE/SGSIT/SERR/BV-02-C MAP/MCE/SGSIT/ATTR/BV-08-C MAP/MCE/SGSIT/ATTR/BV-12-C MAP/MCE/SGSIT/OFFS/BV-02-C |  |  |
| MAP 0/5 AND MAP 1/2 |  |  | MCE SDP attribute: BluetoothProfileDescriptorList – MAP v1.3 |  |  | MAP/MCE/SGSIT/ATTR/BV-09-C |  |  |
| MAP 0/6 AND MAP 1/2 |  |  | MCE SDP attribute: BluetoothProfileDescriptorList – MAP v1.4 |  |  | MAP/MCE/SGSIT/ATTR/BV-10-C |  |  |
| MAP 1/2 |  |  | MAP MCE SDP Future Compatibility |  |  | MAP/MCE/CGSIT/SFC/BV-01-C |  |  |
| MAP 1/1 |  |  | MAP MSE Access Service Discovery |  |  | MAP/MSE/SGSIT/SERR/BV-01-C MAP/MSE/SGSIT/ATTR/BV-01-C MAP/MSE/SGSIT/ATTR/BV-05-C MAP/MSE/SGSIT/ATTR/BV-06-C MAP/MSE/SGSIT/ATTR/BV-07-C MAP/MSE/SGSIT/OFFS/BV-01-C |  |  |
| MAP 0/5 AND MAP 1/1 |  |  | MSE SDP attribute: BluetoothProfileDescriptorList – MAP v1.3 |  |  | MAP/MSE/SGSIT/ATTR/BV-02-C |  |  |
| MAP 0/6 AND MAP 1/1 |  |  | MSE SDP attribute: BluetoothProfileDescriptorList – MAP v1.4 |  |  | MAP/MSE/SGSIT/ATTR/BV-03-C |  |  |

Table 5.1: Test case mapping

## 6 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  | 0 |  |  | 1.0.0 |  |  | 2009-12-05- |  |  | Prepare for publication. |  |
|  |  |  | 1.0.1r0 1.0.1r1 | 1.0.1r0 |  | 2010-11-11- 2010-12-02 | 2010-11-11- |  |  | TSE 3390: MAP/MSE/MMB/BV-16-I (legacy test case |  |
|  |  |  |  | 1.0.1r1 |  |  | 2010-12-02 |  |  | ID TP/MMB/BV-16-I): Expected Outcome |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3384: New test cases MAP/MSE/MSM/BV-09-I |  |
|  |  |  |  |  |  |  |  |  |  | and 10-1 (legacy test case IDs TP/MSM/BV-09, 10-1) |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3480: MAP/MSE/MMU/BV-02-I, |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMU/BV-03-I (legacy test case IDs |  |
|  |  |  |  |  |  |  |  |  |  | TP/MMU/BV-02-I, TP/MMU/BV-03-I); Test procedure |  |
|  |  |  |  |  |  |  |  |  |  | and pass verdict |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3595: MAP/MSE/MMB/BV-15-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMB/BV-15-I); Revise Pass and Fail verdicts |  |
|  | 1 |  |  | 1.0.1 |  |  | 2011-07-21 |  |  | Prepare for publication. |  |
|  |  |  | 1.0.2r0 | 1.0.2r0 |  | 2011-11-08 | 2011-11-08 |  |  | TSE 4201: TP/MMB/BV-05-I: Change GSM to CDMA |  |
|  |  |  |  |  |  |  |  |  |  | in Test procedure |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4317: MAP/MCE/MMD/BV-01-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMD/BV-01-I): Clarify test procedure, Pass |  |
|  |  |  |  |  |  |  |  |  |  | verdict |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4318: MAP/MSE/MMD/BV-02-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMD/BV-02-I): Clarify test procedure, Pass |  |
|  |  |  |  |  |  |  |  |  |  | verdict |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4319: MAP/MCE/MMU/BV-01-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMU/BV-01-I): Enhance test procedure; some |  |
|  |  |  |  |  |  |  |  |  |  | overlap with TSE 4317 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4320: MAP/MCE/MMN/BV-01-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMN/BV-01-I): Clarify test procedure and Pass |  |
|  |  |  |  |  |  |  |  |  |  | verdict |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4321: MAP/MSE/MMN/BV-02-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMN/BV-02-I): Clarify test procedure and Pass |  |
|  |  |  |  |  |  |  |  |  |  | verdict |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4322: MAP/MCE/MMB/BV-07-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMB/BV-07-I): Clarify test procedure and Pass |  |
|  |  |  |  |  |  |  |  |  |  | verdict |  |
|  |  |  |  |  |  |  |  |  |  | TSE 4323: MAP/MSE/MMB/BV-15-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMB/BV-15-I): Clarify test procedure and Pass |  |
|  |  |  |  |  |  |  |  |  |  | verdict |  |
|  |  |  |  | 1.0.2-ac |  |  | 2012-01-20 |  |  | Reviewer corrections. |  |
|  | 2 |  |  | 1.0.2 |  |  | 2012-03-30 |  |  | Prepare for publication. |  |
|  |  |  | 1.0.3r0 | 1.0.3r0 |  | 2012-05-18 | 2012-05-18 |  |  | TSE 4102: MAP/MCE/MMB/BV-19-I (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/MMB/BV-19-I): TCMT, Test Procedure |  |
|  | 3 |  |  | 1.0.3 |  |  | 2012-07-24 |  |  | Prepare for publication. |  |
|  |  |  | 1.1.0 | 1.1.0 |  | 2013-01-02 | 2013-01-02 |  |  | Update document version to 1.1.0 to reflect |  |
|  |  |  |  |  |  |  |  |  |  | specification version change. |  |
|  |  |  | 1.1.0r1 |  |  | 2013-03-28 |  |  |  | TSE 4416: Removed TP/MMB/BV-05-I and TCMT |  |
|  |  |  |  |  |  |  |  |  |  | entry, MAP/MCE/MMB/BV-06-I (legacy test case ID |  |
|  |  |  |  |  |  |  |  |  |  | TP/MMB/BV-06-I) changed to include both UTF-8 and |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | native formats in one test case. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5066: Added two test cases to Section 4.2.1 IUT |  |
|  |  |  |  |  |  |  |  |  |  | – Message Client Equipment (MCE), |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/MSM/BV-13-I and MAP/MCE/MSM/BV-14- |  |
|  |  |  |  |  |  |  |  |  |  | I (legacy test case IDs TP/MSM/BV-13-I and |  |
|  |  |  |  |  |  |  |  |  |  | TP/MSM/BV-14-I) and TCMT. Added two test cases |  |
|  |  |  |  |  |  |  |  |  |  | to Section 4.2.2 IUT – Message Server Equipment |  |
|  |  |  |  |  |  |  |  |  |  | (MSE), MAP/MSE/MSM/BV-11-I and |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MSM/BV-12-I (legacy test case IDs |  |
|  |  |  |  |  |  |  |  |  |  | TP/MSM/BV-11-I and TP/MSM/BV-12-I) and TCMT. |  |
|  |  |  |  |  |  |  |  |  |  | Also added MAP/MSE/MSM/BV-09-I and |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MSM/BV-10-I (legacy test case IDs |  |
|  |  |  |  |  |  |  |  |  |  | TP/MSM/BV-09-I and TP/MSM/BV-10-I) to the TCMT. |  |
|  |  |  |  |  |  |  |  |  |  | BTI Review Comments |  |
|  |  |  |  | 1.1.0r2 |  |  | 2013-04-03 |  |  | Editorial fixes |  |
|  |  |  | 1.1.0r3 | 1.1.0r3 |  | 2013-05-16 | 2013-05-16 |  |  | Fixed Figure 1.1 to reflect changes to the MCE SMS |  |
|  |  |  |  |  |  |  |  |  |  | tests. |  |
|  |  |  | 1.2.0r0 |  |  | 2013-05-16 |  |  |  | Incorporated MAPII TS CR 09r06 changes and Fort |  |
|  |  |  |  |  |  |  |  |  |  | Worth F2F Comment resolutions |  |
|  |  |  |  | 1.2.0r1 |  |  | 2013-05-29 |  |  | BTI Review, Alicia’s Comments. |  |
|  |  |  |  | 1.2.0r1 |  |  | 2013-06-10 |  |  | Approved by BTI. |  |
|  | 4 |  |  | 1.2.0 |  |  | 2013-07-16 |  |  | Prepare for Publication |  |
|  |  |  | 1.2.1r00 | 1.2.1r00 |  | 2014-05-01 | 2014-05-01 |  |  | TSE 5437: Updated mapping for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/GOEP/SRMP/BV-04-C (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/SRMP/BV-04-C). |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5439: Updated Test Procedure for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/MSM/BV-13-I and MAP/MCE/MSM/BV-14- |  |
|  |  |  |  |  |  |  |  |  |  | I (legacy test case IDs TP/MSM/BV-13-I and |  |
|  |  |  |  |  |  |  |  |  |  | TP/MSM/BV-14-I). |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5492: Removed IUT requirements in Initial |  |
|  |  |  |  |  |  |  |  |  |  | Condition for MAP/MCE/MMB/BV-03-I (legacy test |  |
|  |  |  |  |  |  |  |  |  |  | case ID TP/MMB/BV-03-I). |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5588: Updated TCMT mapping for TP/MFB/BV- |  |
|  |  |  |  |  |  |  |  |  |  | 02-C and TP/MFB/BV-05-C to add “AND 1/1” |  |
|  |  |  | 1.2.1r01 |  |  | 2014-06-16 |  |  |  | BTI Review – Stephen Raxter. Corrected Revision |  |
|  |  |  |  |  |  |  |  |  |  | history for TSE 5439. |  |
|  | 5 |  |  | 1.2.1 |  |  | 2014-07-07 |  |  | TCRL 2014-1 Publication |  |
|  |  |  | 1.2.1.0r00 | 1.2.1.0r00 |  | 2015-05-20 | 2015-05-20 |  |  | TSE 6031: Corrected TCMT mapping for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/GOEP/SRMP/BV-06-C (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/SRMP/BV-06-C). |  |
|  |  |  |  |  |  |  |  |  |  | ESR08 Update: Added MAP 1.2.1 support to TCMT |  |
|  |  |  |  |  |  |  |  |  |  | by adding item 0/4 to the mapping for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/MFB/BV-01-I, MAP/MCE/MFB/BV-03-I, |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/MFB/BV-04-I, MAP/MSE/MFB/BV-02-I, |  |
|  |  |  |  |  |  |  |  |  |  | and MAP/MSE/MFB/BV-05-I |  |
|  |  |  |  |  |  |  |  |  |  | (legacy test case IDs TP/MFB/BV-01-I, TP/MFB/BV- |  |
|  |  |  |  |  |  |  |  |  |  | 03-I, TP/MFB/BV-04-I, TP/MFB/BV-02-I, and |  |
|  |  |  |  |  |  |  |  |  |  | TP/MFB/BV-05-I). |  |
|  | 6 |  |  | 1.2.1.0 |  |  | 2015-07-14 |  |  | Prepared for TCRL 2015-1 publication |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 1.2.1.1r00 | 1.2.1.1r00 |  | 2015-10-06 |  |  |  | TSE 6406 and TSE 6701: corrected mapping for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/GOEP/SRMP/BV-03-C (legacy test case |  |
|  |  |  |  |  |  |  |  |  |  | ID TP/SRMP/BV-03-C) by adding mapping to 15/11. |  |
|  |  |  | 1.2.2.0r00 |  |  | 2015-10-28 |  |  |  | Updated version numbering to align with Specification |  |
|  |  |  |  |  |  |  |  |  |  | version change to 1.2.2 for ESR09. |  |
|  | 7 |  |  | 1.2.2.0 |  |  | 2015-12-22 |  |  | Prepared for TCRL 2015-2 publication |  |
|  |  |  | 1.3.0.r00 | 1.3.0.r00 |  | 2015-12-08 | 2015-12-08 |  |  | Incorporated the Instant Messaging part of Instant |  |
|  |  |  |  |  |  |  |  |  |  | Messaging and Message Forwarding TS CR r09 |  |
|  |  |  |  | 1.3.0.r01 |  |  | 2016-02-01 |  |  | Addressing BTI comments |  |
|  |  |  | 1.3.0.r02 | 1.3.0.r02 |  | 2016-04-04 | 2016-04-04 |  |  | Accepted amendments from BTI |  |
|  |  |  |  |  |  |  |  |  |  | Updated tables in section 3.1 |  |
|  |  |  |  | 1.3.0 |  |  | 2016-05-02 |  |  | Approved by BTI |  |
|  |  |  |  | 1.3.0 |  |  | 2016-05-17 |  |  | Specification v1.3 adopted by the Bluetooth SIG BoD |  |
|  | 8 |  |  | 1.3.0 |  |  | 2016-05-24 |  |  | Prepared for publication |  |
|  |  |  | 1.3.1r01 | 1.3.1r01 |  | 2016-10-13 | 2016-10-13 |  |  | Converted to new Test Case ID conventions as |  |
|  |  |  |  |  |  |  |  |  |  | defined in TSTO v4.1.0. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 7562: Corrected mapping for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMN/BV-15-I. |  |
|  |  |  | 1.3.1r02 |  |  | 2016-11-14 |  |  |  | Added clarification to section 3.1 about the test |  |
|  |  |  |  |  |  |  |  |  |  | strategy to use a subset of the tests in GOEP to test |  |
|  |  |  |  |  |  |  |  |  |  | MAP functionality. Consequential clarifications made |  |
|  |  |  |  |  |  |  |  |  |  | in section 4.1 about the naming conventions used to |  |
|  |  |  |  |  |  |  |  |  |  | refer to GOEP tests. |  |
|  |  |  | 1.3.1r03 |  |  | 2016-11-21 |  |  |  | Corrected suggested mistakes in TCMT for GOEP |  |
|  |  |  |  |  |  |  |  |  |  | tests that map to multiple roles. |  |
| 9 |  |  | 1.3.1 |  |  | 2016-12-13 |  |  |  | Approved by BTI. Prepared for TCRL 2016-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.4.0r00 |  |  | 2017-02-08 |  |  |  | Incorporated Message Forwarding TS CR r07 |  |
|  |  |  |  |  |  |  |  |  |  | Added test cases for Message Forwarding and their |  |
|  |  |  |  |  |  |  |  |  |  | TCMT: |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/MFMH/BV-01-I, MAP/MCE/MFMH/BV-02- |  |
|  |  |  |  |  |  |  |  |  |  | I, MAP/MCE/MFMH/BV-03-I, MAP/MCE/MFMH/BV- |  |
|  |  |  |  |  |  |  |  |  |  | 04-I, MAP/MCE/MFMH/BV-05-I, |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MFMH/BV-01-I, MAP/MSE/MFMH/BV-02-I |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MFMH/BV-03-I, MAP/MSE/MFMH/BV-04-I |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MFMH/BV-05-I |  |
|  |  |  | 1.4.0r01 |  |  | 2017-03-27 |  |  |  | Updated template. Fixed misc. editorials. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 7972: Update TCMT for MAP/MCE/MMU/BV-06- |  |
|  |  |  |  |  |  |  |  |  |  | I. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 8006: Modify Pass verdict for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MCE/MSM/BV-03-I, MAP/MCE/MSM/BV-14-I, |  |
|  |  |  |  |  |  |  |  |  |  | and MAP/MCE/MNR/BV-01-I to separate out MAS |  |
|  |  |  |  |  |  |  |  |  |  | and MNS requirements to specify disconnect may be |  |
|  |  |  |  |  |  |  |  |  |  | done by the IUT for MNS. |  |
|  |  |  |  | 1.4.0r02 |  |  | 2017-04-13 |  |  | Addressed remaining BTI comments |  |
|  |  |  | 1.4.0r03 | 1.4.0r03 |  | 2017-04-26 | 2017-04-26 |  |  | TSE 8862: Update Description in TCMT for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMB/BV-25-I. Update TCMT and |  |
|  |  |  |  |  |  |  |  |  |  | description for MAP/MCE/MMB/BV-29-I and |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMB/BV-38-I. Update TCMT for |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMB/BV-43-I. |  |
|  | 10 |  |  | 1.4.0 |  |  | 2017-05-21 |  |  | Approved by BTI. Prepared for publication. |  |
|  |  |  | 1.4.1r00 | 1.4.1r00 |  | 2018-04-27 | 2018-04-27 |  |  | TSE 9910 (rating 3): Revised Initial Condition of the |  |
|  |  |  |  |  |  |  |  |  |  | Lower Tester of test case MAP/MSE/MMU/BV-02-I. |  |
| 11 |  |  | 1.4.1 |  |  | 2018-07-01 |  |  |  | Approved by BTI. Prepared for TCRL 2018-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.4.1.0r00 |  |  | 2018-11-09 |  |  |  | Updated version number to 1.4.1.0 to align with |  |
|  |  |  |  |  |  |  |  |  |  | adoption of the specification 1.4.1 |  |
| 12 |  |  | 1.4.1.0 |  |  | 2018-11-21 |  |  |  | Approved by BTI. Prepared for TCRL 2018-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 1.4.1.1 r00–r01 1.4.2.0r00 |  |  | 2019-04-15– 2019-07-12 |  |  |  | TSE 11800 (rating 2): Updated TCMT for test case |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMB/BV-36-I. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 11638 (rating 3): Updated Initial Condition text |  |
|  |  |  |  |  |  |  |  |  |  | for test cases MAP/MCE/MMU/BV-01-I and -04-I and |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MMU/BV-02-I and -03-I. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 11918: Updated version number to align with |  |
|  |  |  |  |  |  |  |  |  |  | new spec version 1.4.2. |  |
| 13 |  |  | 1.4.2.0 |  |  | 2019-07-28 |  |  |  | Approved by BTI. Prepared for TCRL 2019-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | p14r00–r01 |  |  | 2021-04-05 – 2021-06-16 |  |  |  | TSE 15685 (rating 1): To address an issue with |  |
|  |  |  |  |  |  |  |  |  |  | incorrect wording re: MAP Session and MAS |  |
|  |  |  |  |  |  |  |  |  |  | Instances, updated initial condition and pass verdict |  |
|  |  |  |  |  |  |  |  |  |  | for TCs MAP/MCE/MSM/BV-13-I and -14-I and |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MSM/BV-12-I; revised title (also in TCRL), |  |
|  |  |  |  |  |  |  |  |  |  | test purpose, initial condition, and references for TCs |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MSM/BV-09-I and -10-I; and revised test |  |
|  |  |  |  |  |  |  |  |  |  | purpose, initial condition, and pass verdict for TC |  |
|  |  |  |  |  |  |  |  |  |  | MAP/MSE/MSM/BV-11-I. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 15984 (rating 2): Made changes to the TCMT to |  |
|  |  |  |  |  |  |  |  |  |  | align with items deprecated/withdrawn in the ICS. |  |
|  |  |  |  |  |  |  |  |  |  | Template-related and consistency checker editorials, |  |
|  |  |  |  |  |  |  |  |  |  | including assigning the previous v1.4.2.0 as p13. |  |
| 14 |  |  | p14 |  |  | 2021-07-13 |  |  |  | Approved by BTI on 2021-06-03. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  |  |  | 2021-1 publication. |  |
|  |  |  | p15r00–r06 |  |  | 2023-10-25 – 2024-04-02 |  |  |  | TSE 23957 (rating 1): Converted -I tests to -C tests as |  |
|  |  |  |  |  |  |  |  |  |  | appropriate; updated the TCMT and TCRL |  |
|  |  |  |  |  |  |  |  |  |  | accordingly. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | TSE 24531 (rating 4): Added new GSIT section with |  |
|  |  |  |  |  |  |  |  | new TCs MAP/MCE/CGSIT/SFC/BV-01-C, |  |
|  |  |  |  |  |  |  |  | MAP/MCE/SGSIT/ATTR/BV-08-C – -12-C, |  |
|  |  |  |  |  |  |  |  | MAP/MCE/SGSIT/OFFS/BV-02-C, |  |
|  |  |  |  |  |  |  |  | MAP/MCE/SGSIT/SERR/BV-02-C, |  |
|  |  |  |  |  |  |  |  | MAP/MSE/SGSIT/ATTR/BV-01-C – -07-C, |  |
|  |  |  |  |  |  |  |  | MAP/MSE/SGSIT/OFFS/BV-01-C, and |  |
|  |  |  |  |  |  |  |  | MAP/MSE/SGSIT/SERR/BV-01-C. Updated the |  |
|  |  |  |  |  |  |  |  | TCMT accordingly. Removed |  |
|  |  |  |  |  |  |  |  | MAP/MCE/GOEP/CON/BV-02-C and |  |
|  |  |  |  |  |  |  |  | MAP/MSE/GOEP/CON/BV-02-C from the TCRL. |  |
|  |  |  |  |  |  |  |  | Added references to the SDP TS and the MAP IXIT. |  |
|  |  |  |  |  |  |  |  | Updated the Test Groups and TC Conventions |  |
|  |  |  |  |  |  |  |  | sections. |  |
|  |  |  |  |  |  |  |  | TSE 24603 (rating 2): Updated the TCMT entries for |  |
|  |  |  |  |  |  |  |  | MAP/MCE/MFB/BV-01-C, -03-C, -04-C, and -06-C |  |
|  |  |  |  |  |  |  |  | and for MAP/MSE/MFB/BV-02-C, -05-C, and -07-C to |  |
|  |  |  |  |  |  |  |  | address deprecated versions. |  |
|  |  |  |  |  |  |  |  | Updated the document to align with the most recent |  |
|  |  |  |  |  |  |  |  | standards. |  |
| 15 |  |  | p15 |  |  | 2024-07-01 |  | Approved by BTI on 2024-05-22. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2024-1 publication. |  |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Johannes Albrecht |  |  | Berner & Mattner Systemtechnik GmbH |  |
|  | Olivia Bellamou-Huet |  |  | Berner & Mattner Systemtechnik GmbH |  |
|  | Norman Geilhardt |  |  | Berner & Mattner Systemtechnik GmbH |  |
|  | Joachim Mertz |  |  | Berner&Mattner |  |
|  | Rüdiger Mosig |  |  | Berner&Mattner |  |
|  | Dominik Sollfrank |  |  | Berner & Mattner Systemtechnik GmbH |  |
|  | Alicia Courtney |  |  | Broadcom |  |
|  | Burch Seymour |  |  | Continental Automotive Systems |  |
|  | Meshach Rajsingh |  |  | CSR |  |
|  | Kyle Penri-Williams |  |  | Parrot |  |
