# PBAP.TS.p22

> Source: PDF converted via PyMuPDF.

---

Phone Book Access Profile (PBAP)
Bluetooth® Test Suite
▪ Revision: PBAP.TS.p22 ▪ Revision Date: 2025-11-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.pkg101
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2004–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Phone Book Access Profile (PBAP) Specification with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers’ Bluetooth devices.

## 2 References, definitions, and abbreviations


### 2.1 References

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [2] and [3].
[1] Bluetooth Phone Book Access Profile Specification, Version 1.0 or later
[2] Bluetooth Core Specification, Version 2.1 or later
[3] Test Strategy and Terminology Overview
[4] ICS for Phone Book Access Profile, PBAP.ICS
[5] SDP Test Suite, SDP.TS
[6] GOEP Test Suite, GOEP.TS
[7] IXIT Proforma for Phone Book Access Profile

### 2.2 Definitions

In this Bluetooth document, the definitions from [2] and [3] apply.

### 2.3 Abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [2] and [3] apply.

## 3 Test Suite Structure (TSS)


### 3.1 Overview

This section defines the tree structure of the conformance and interoperability tests to be passed to qualify as PBAP device. The TSS is composed of nested test groups organized in a top-down approach.

### 3.2 Test Strategy

The test objectives are to verify the functionality of the Phone Books Access Profile within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true.
The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT’s peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT.
This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes.

### 3.3 Test groups

The following test groups have been defined:
• Generic SDP Integrated Tests
• Session management functions
• Phone book downloading functions and features
• Phone book browsing functions and features

## 4 Test cases (TC)


### 4.1 Introduction


#### 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [3]. The convention used here is: <spec abbreviation>/<IUT role>/<class>/<feat>/<func>/<subfunc>/<cap>/<xx>-<nn>-<y>.
Testing of this specification includes tests from the GOEP Test Suite [6]; when used, the test cases in GOEP are referred to in the TCMT using the following convention: <spec abbreviation>/<IUT role>/GOEP/<GOEP TC Identifier>.
Additionally, testing of this specification includes tests from the SDP Test Suite [5] referred to as Generic SDP Integrated Tests (GSIT); when used, the test cases in GSIT are referred to through a TCID string using the following convention: <spec abbreviation>/<IUT role>/<GSIT test group>/<GSIT class>/<xx>-<nn>-<y>.

|  | Identifier Abbreviation |  |  | Spec Identifier <spec abbreviation> |  |
| --- | --- | --- | --- | --- | --- |
| PBAP |  |  | Phone Book Access Profile |  |  |
|  | Identifier Abbreviation |  |  | Role Identifier <IUT role> |  |
| PCE |  |  | Phone Book Client Equipment |  |  |
| PSE |  |  | Phone Book Server Equipment |  |  |
|  | Identifier Abbreviation |  |  | Reference Identifier <GSIT test group> |  |
| CGSIT |  |  | Client Generic SDP Integrated Tests |  |  |
| SGSIT |  |  | Server Generic SDP Integrated Tests |  |  |
|  | Identifier Abbreviation |  |  | Reference Identifier <GSIT class> |  |
| ATTR |  |  | Attribute |  |  |
| OFFS |  |  | Attribute ID Offset String |  |  |
| SERR |  |  | Service Record |  |  |
| SFC |  |  | SDP Future Compatibility |  |  |
|  | Identifier Abbreviation |  |  | Feature Identifier <feat> |  |
| PBB |  |  | Phone Book Browsing functions |  |  |
| PBD |  |  | Phone Book Downloading functions |  |  |
| PBF |  |  | Phone Book Browsing Feature |  |  |
| PDF |  |  | Phone Book Download Feature |  |  |
| SSM |  |  | Session Management functions |  |  |

Table 4.1: PBAP TC class naming conventions

#### 4.1.2 Conformance

When conformance is claimed for a particular specification, all capabilities are to be supported in the specified manner. The mandated tests from this Test Suite depend on the capabilities to which conformance is claimed.
The Bluetooth Qualification Program may employ tests to verify implementation robustness. The level of implementation robustness that is verified varies from one specification to another and may be revised for cause based on interoperability issues found in the market.
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

#### 4.1.4 vCard Test Requirements


##### 4.1.4.1 vCard Formats

The following table describes the vCard format and headings to be used in the test cases that verify transfer of vCard data from PSE to PCE.

|  | Property |  |  | Status |  |  | Value (Example text only) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name |  |  | M |  |  | Mr. John M. Smith Esq. |  |  |
| Telephone-Work |  |  | C.1 |  |  | +1(919)555-1234 |  |  |
| Telephone-Cell |  |  | C.1 |  |  | +1(919)555-6758 |  |  |
| Telephone-FAX |  |  | C.1 |  |  | +1(919)555-9876 |  |  |
| X-BT-UCI |  |  | C.1 |  |  | test1:kyle123 |  |  |
| X-BT-UCI |  |  | C.1 |  |  | test2:scott123 |  |  |
| X-BT-UCI |  |  | C.1 |  |  | test3:dominik123 |  |  |
| Organization |  |  | O |  |  | ABC, Inc. North American Division Marketing |  |  |
| Address-Work |  |  | O |  |  | Suite 101 1 Central St; Any Town NC 27654 |  |  |
| E-mail-Internet |  |  | O |  |  | john.public@abc.com |  |  |
| X-BT-UID |  |  | C.2 |  |  | {Varies} |  |  |


|  | Property |  |  | Status |  |  | Value (Example text only) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PHOTO |  |  | C.3 |  |  | {Valid Image} |  |  |
| X-BT-SPEEDDIALKEY |  |  | C.4 |  |  | 5 |  |  |

Table 4.2: vCard Data
M: Mandatory to support this property.
C.1: Mandatory to support at least one telephone number or X-BT-UCI. At least one entry of each phonebook has an X-BT-UCI Property if the X-BT-UCI Feature is supported by the PSE. If the PSE is the Lower Tester, at least ten (10) entries of each phonebook contain this property, five (5) of which have multiple entries of this property.
C.2: If the X-BT-UID Feature is supported by the PSE, then all the supported ‘pb’ objects/folders contain this property. If the ‘Contact Referencing’ Feature is supported by the PSE, then all the supported ‘fav’,’spd’,’mch’,’ich’,’och’, and ‘cch’ have at least one contact with this property.
C.3: If the ‘Default Contact Image Format’ Feature is supported by the PSE, then at least one of the Phone Book objects supported contains at least one entry with this property.
C.4: If the ‘spd’ repository is supported by the PSE, then all the entries of that object contain this property.
O: Optional to support this property.

##### 4.1.4.2 vCard Count

If the IUT is PSE:
Each Phone Book object that supports more than one hundred entries contains at least 100 entries.
Each Phone Book object that supports less than one hundred entries contains its maximum number of entries.

### 4.2 Generic SDP Integrated Tests


#### 4.2.1 Server Generic SDP Integrated Tests


##### 4.2.1.1 Phone Book Access Profile – PCE

Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [5] using Table 4.3 below as input:

| TCID |  |  | Reference | Attribute ID Name |  | Attribute ID |  | Value/ Secondary Value |  |  |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | definition |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  | source |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  | (Universal, |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  | Profile) |  |  |  |  |  | defined) |  |
|  | PBAP/PCE/SGSIT/SERR/BV-01-C |  | [1] 7.1.1 | ServiceClassIDList | Universal | Universal |  |  | “Phonebook Access |  | Present for PCE | Present for PCE |  |
|  | [Service record GSIT – PBAP PCE] |  |  |  |  |  |  |  | Client” (UUID) |  |  |  |  |
|  | PBAP/PCE/SGSIT/ATTR/BV-01-C |  | [1] 7.1.1 | BluetoothProfileDescriptor List | Universal |  |  |  | “Phonebook Access |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  |  |  | Profile” (UUID): Version |  |  |  |  |
|  | Descriptor List, PBAP 1.1] |  |  |  |  |  |  |  | – “0x0101” (Uint16) |  |  |  |  |
|  | PBAP/PCE/SGSIT/ATTR/BV-02-C |  | [1] 7.1.1 | BluetoothProfileDescriptor List | Universal |  |  |  | “Phonebook Access |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  |  |  | Profile” (UUID): Version |  |  |  |  |
|  | Descriptor List, PBAP 1.2] |  |  |  |  |  |  |  | – “0x0102” (Uint16) |  |  |  |  |

Table 4.3: Input for the Phone Book Access Profile PCE SGSIT SDP test procedure

##### 4.2.1.2 Phone Book Access Profile – PSE

Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [5] using Table 4.4 below as input:

| TCID |  |  | Reference | Attribute ID Name |  | Attribute ID |  | Value/ Secondary Value |  |  |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | definition |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  | source |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  | (Universal, |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  | Profile) |  |  |  |  |  | defined) |  |
|  | PBAP/PSE/SGSIT/SERR/BV-01-C |  | [1] 7.1.2 | ServiceClassIDList | Universal | Universal |  |  | “Phonebook Access |  | Present for PSE | Present for PSE |  |
|  | [Service record GSIT – PBAP PSE] |  |  |  |  |  |  |  | Server” (UUID) |  |  |  |  |
| PBAP/PSE/SGSIT/ATTR/BV-01-C [Attribute GSIT – Protocol Descriptor List] | PBAP/PSE/SGSIT/ATTR/BV-01-C |  | [1] 7.1.2 | ProtocolDescriptorList | Universal |  |  |  | “L2CAP” (UUID), |  | Present for PSE |  |  |
|  | [Attribute GSIT – Protocol Descriptor |  |  |  |  |  |  |  | “RFCOMM” (UUID): |  |  |  |  |
|  | List] |  |  |  |  |  |  |  | Channel number: skip |  |  |  |  |
|  |  |  |  |  |  |  |  |  | (Uint8), |  |  |  |  |
|  |  |  |  |  |  |  |  |  | “OBEX” (UUID) |  |  |  |  |


| TCID |  |  | Reference | Attribute ID Name |  | Attribute ID |  | Value/ Secondary Value |  |  |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | definition |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  | source |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  | (Universal, |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  | Profile) |  |  |  |  |  | defined) |  |
|  | PBAP/PSE/SGSIT/ATTR/BV-02-C |  | [1] 7.1.2 | BluetoothProfileDescriptor List | Universal | Universal |  |  | “Phonebook Access |  | TCMT defined | TCMT defined |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  |  |  | Profile” (UUID): Version |  |  |  |  |
|  | Descriptor List, PBAP 1.1] |  |  |  |  |  |  |  | – “0x0101” (Uint16) |  |  |  |  |
|  | PBAP/PSE/SGSIT/ATTR/BV-03-C |  | [1] 7.1.2 | BluetoothProfileDescriptor List | Universal |  |  |  | “Phonebook Access |  | TCMT defined |  |  |
|  | [Attribute GSIT – Bluetooth Profile |  |  |  |  |  |  |  | Profile” (UUID): Version |  |  |  |  |
|  | Descriptor List, PBAP 1.2] |  |  |  |  |  |  |  | – “0x0102” (Uint16) |  |  |  |  |
|  | PBAP/PSE/SGSIT/ATTR/BV-04-C |  | [1] 7.1.2 | Supported Repositories | Profile |  |  | skip (Uint8) | skip (Uint8) |  | Present for PSE |  |  |
|  | [Attribute GSIT – Supported |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Repositories] |  |  |  |  |  |  |  |  |  |  |  |  |
|  | PBAP/PSE/SGSIT/ATTR/BV-05-C |  | [1] 7.1.2 | GoepL2CapPsm | Profile |  |  | skip (Uint16) |  |  | TCMT defined |  |  |
|  | [Attribute GSIT – GoepL2CapPsm] |  |  |  |  |  |  |  |  |  |  |  |  |
|  | PBAP/PSE/SGSIT/ATTR/BV-06-C |  | [1] 7.1.2 | PbapSupportedFeatures | Profile |  |  | skip (Uint32) |  |  | TCMT defined |  |  |
|  | [Attribute GSIT – |  |  |  |  |  |  |  |  |  |  |  |  |
|  | PBAPSupportedFeatures] |  |  |  |  |  |  |  |  |  |  |  |  |

Table 4.4: Input for the Phone Book Access Profile PSE SGSIT SDP test procedure

##### 4.2.1.3 Phone Book Access Profile – Attribute ID Offset String tests

Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [5] using Table 4.5 below as input:

| TCID |  |  | Reference | ServiceSearchPattern | Attribute ID Name | Attribute ID Offset |  | Attribute presence |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | (Present/Present for |  |
|  |  |  |  |  |  |  |  | [role], Optionally |  |
|  |  |  |  |  |  |  |  | present, TCMT |  |
|  |  |  |  |  |  |  |  | defined) |  |
|  | PBAP/PCE/SGSIT/OFFS/BV-01-C |  | [1] 7.1.1 | Phonebook Access Client | ServiceName | 0x0000 | Present for PCE | Present for PCE |  |
|  | [Attribute ID Offset String GSIT – |  |  |  |  |  |  |  |  |
|  | Service Name] |  |  |  |  |  |  |  |  |
|  | PBAP/PSE/SGSIT/OFFS/BV-01-C |  | [1] 7.1.2 | Phonebook Access Server | ServiceName | 0x0000 | Present for PSE |  |  |
|  | [Attribute ID Offset String GSIT – |  |  |  |  |  |  |  |  |
|  | Service Name] |  |  |  |  |  |  |  |  |

Table 4.5: Input for the Phone Book Access Profile SGSIT Attribute ID Offset String tests

#### 4.2.2 Client Generic SDP Integrated Tests

Execute the Generic SDP Future Compatibility Tests defined in Section 6.4, Client test procedures (CGSIT), in [5] using Table 4.6 below as input:

| TCID | Reference |  | Service Record Service |  | Lower Tester SDP record initial conditions |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Class UUID description |  |  |  |  |
| PBAP/PCE/CGSIT/SFC/BV-01-C [SDP Future Compatibility – IUT is PBAP PCE] | [2] 6.1, 7 | Phonebook Access Server | Phonebook Access Server |  |  | The Lower Tester exposes a PBAP PCE SDP record. |  |
|  |  |  |  |  |  | The version in the Bluetooth Profile Descriptor List is greater than the |  |
|  |  |  |  |  |  | most recently adopted version. |  |
|  |  |  |  |  |  | All bits are set in the Supported Repositories attribute including |  |
|  |  |  |  |  |  | Reserved bits. |  |
|  |  |  |  |  |  | All bits are set in the PBAPSupportedFeatures attribute including |  |
|  |  |  |  |  |  | Reserved bits. |  |
|  |  |  |  |  |  | HFP SDP record is exposed if specified by IXIT [7]. |  |

Table 4.6: Input for the Client CGSIT SDP future compatibility tests

### 4.3 Session Management Functional Components

Verify that a PBAP session can be properly opened and terminated.

#### 4.3.1 IUT – PCE

Verify that a PCE implementation can properly open and terminate a PBAP session.
PBAP/PCE/SSM/BV-01-C [PCE Opens a PBAP Session]
• Test Purpose
Verify that the PCE can start a PBAP session.
• Reference
[1] 2.4
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
The IUT attempts to establish a PBAP session with the Lower Tester.
• Expected Outcome
Pass verdict
The IUT issues an OBEX CONNECT request.
PBAP/PCE/SSM/BV-02-C [PCE Closes a PBAP Session]
• Test Purpose
Verify that the PCE can terminate a PBAP session.
• Reference
[1] 2.4
• Initial Condition
- The IUT is engaged in a PBAP session with the Lower Tester.
• Test Procedure
The IUT attempts to disconnect the PBAP session.
• Expected Outcome
Pass verdict
The IUT issues an OBEX DISCONNECT to the Lower Tester.
PBAP/PCE/SSM/BV-06-C [PCE Responds to Authentication Requests from PSE]
• Test Purpose
Verify that the PCE responds properly to an authentication request from the PSE at the time of PBAP session initiation.
• Reference
[1] 2.4
• Initial Condition
- The IUT is in the PCE role.
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
1. The IUT sends an OBEX CONNECT request to the Lower Tester
2. The Lower Tester refuses the connect request with the “Unauthorized” error response code and
includes an authentication challenge (challenge1).
3. The IUT re-sends a connect request to the Lower Tester with an authentication response
(response1). The IUT may also include an authentication challenge (challenge2).
4. The Lower Tester verifies the authentication response (response1) of the IUT and responds with
success. If applicable, the response includes an authentication response (response2) for the second challenge (challenge2).
• Expected Outcome
Pass verdict
The client correctly sent a response (response1) in a second connect request to the first authentication challenge (challenge1).
PBAP/PCE/SSM/BV-08-C [PCE Opens a PBAP Session and initiates OBEX Authentication]
• Test Purpose
Verify that the PCE can start a PBAP session.
• Reference
[1] 2.4
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode. The OBEX server on the Lower Tester enforces OBEX authentication for its Phone Book Access Service.
• Test Procedure
The IUT attempts to establish a PBAP session with the Lower Tester.
• Expected Outcome
Pass verdict
The IUT issues an OBEX CONNECT request containing an appropriate authenticate-challenge.
• Test Purpose
Verify that the PCE can start a PBAP session.
• Reference
[1] 2.4
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
The IUT attempts to establish a PBAP session with the Lower Tester, with OBEX authentication (either one-way with the IUT issuing the Authentication Challenge; or mutual with the Lower Tester issuing the first Authentication Challenge). In that process, the Lower Tester issues a wrong Authentication Response.
• Expected Outcome
Pass verdict
The IUT issues an OBEX DISCONNECT or closes the RFCOMM channel.
PBAP/PCE/SSM/BV-09-C [PCE Shares PbapSupportedFeature bits]
• Test Purpose
Verify that the PCE can share its PbapSupportedFeatures bits with a server and that they correspond to the ICS.
• Reference
[1] 6.3
[4] Table 2
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode. The Lower Tester has a PbapSupportedFeatures attribute in its SDP record (Any value).
• Test Procedure
The IUT attempts to establish a PBAP session with the Lower Tester.
• Expected Outcome
Pass verdict
The IUT issues an OBEX CONNECT request containing a PbapSupportedFeatures header.
The IUT’s PbapSupportedFeatures match those declared in Table 2: Supported features of the ICS [4].
• Test Purpose
Verify that the PCE does not share its PbapSupportedFeatures bits with a legacy server.
• Reference
[1] 6.3
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode. The Lower Tester does not have a PbapSupportedFeatures attribute in its SDP record.
• Test Procedure
The IUT attempts to establish a PBAP session with the Lower Tester.
• Expected Outcome
Pass verdict
The IUT issues an OBEX CONNECT request that does not contain a PbapSupportedFeatures header.

#### 4.3.2 IUT – PSE

Verify that a PSE implementation can properly respond to opening and terminating a PBAP session.
PBAP/PSE/SSM/BV-03-C [PSE Responds to a Session Opening Request]
• Test Purpose
Verify that the PSE can properly respond to a PBAP session establishment request.
• Reference
[1] 2.4
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The Lower Tester is in discoverable and connectable mode.
• Test Procedure
The Lower Tester connects to the IUT and issues an OBEX CONNECT request to the IUT.
• Expected Outcome
Pass verdict
The IUT responds with an OBEX CONNECT response.
PBAP/PSE/SSM/BV-05-C [PSE Responds to a Disconnect Request]
• Test Purpose
Verify that the PSE can properly process a PBAP session disconnect request.
• Reference
[1] 2.4
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester sends an OBEX Disconnect request to the IUT.
• Expected Outcome
Pass verdict
The IUT sends an OBEX DISCONNECT response to the Lower Tester.
PBAP/PSE/SSM/BV-07-C [PSE Responds to Authentication Requests from PCE]
• Test Purpose
Verify that the PSE responds properly to an authentication request from the PCE at the time of PBAP session initiation.
• Reference
[1] 2.4
• Initial Condition
- The IUT is in the PSE role.
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable mode.
• Test Procedure
1. The Lower Tester attempts to establish a PBAP session with the IUT using OBEX authentication. 2. The IUT issues a response with a correct authentication challenge response.
• Expected Outcome
Pass verdict
The IUT issues an OBEX CONNECT response.
PBAP/PSE/SSM/BI-02-C [PSE Reject a PUT command]
• Test Purpose
Verify that the PSE systematically rejects any PUT request.
• Reference
[1] 2.4
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester sends an OBEX PUT command to the IUT. This PUT command contains a non- NULL object.
• Expected Outcome
Pass verdict
The IUT sends a PUT response with error code ‘Bad Request’.
PBAP/PSE/SSM/BI-03-C [PSE Reject an Unidentified PCE]
• Test Purpose
Verify that the PSE can authenticate the PCE properly at the time of PBAP session initiation.
• Reference
[1] 2.4
• Initial Condition
- The IUT is in the PSE role.
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable modes.
• Test Procedure
1. The Lower Tester attempts to establish a PBAP session with the IUT. The IUT uses OBEX
authentication. 2. The Lower Tester issues a response with an incorrect authentication challenge response.
• Expected Outcome
Pass verdict
The server responds with a response code of 0x41/0xc1 (unauthorized).
PBAP/PSE/SSM/BV-08-C [PSE Asks for Authorization for a Session Opening Request]
• Test Purpose
Verify that the PSE asks the user for authorization for the first PBAP session connection.
• Reference
[1] 2.5
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable mode.
• Test Procedure
The Lower Tester connects to the IUT and issues an OBEX CONNECT request to the IUT.
• Test Condition
This must be the first PBAP connection between the IUT and the Lower Tester after pairing.
• Expected Outcome
Pass verdict
The IUT displays a message to the user to authorize the service-level PBAP connection, or alternatively, the user was previously required to authorize the device pairing.
PBAP/PSE/SSM/BV-11-C [PSE Shares PbapSupportedFeatures bits]
• Test Purpose
Verify that the PSE can share its PbapSupportedFeatures bits with a client and that they correspond to the ICS.
• Reference
[1] 7.1.2
[4] Table 9
• Initial Condition
- The IUT and the Lower Tester have been paired.
- The IUT is in discoverable and connectable mode.
• Test Procedure
The Lower Tester requests the PBAP PSE SDP record of the IUT.
• Test Condition
This must be the first PBAP connection between the IUT and the Lower Tester after pairing.
• Expected Outcome
Pass verdict
The IUT correctly advertises a PbapSupportedFeatures attribute.
The IUT’s PbapSupportedFeatures and SupportedRepositories match Table 9 of the ICS [4].

### 4.4 Phone Book Downloading Functional Components

Verify that the functions needed for Phone Book Download are correctly implemented.

#### 4.4.1 IUT – PCE

Verify that a PCE implementation can properly download the Phone Book.
PBAP/PCE/PBD/BV-01-C [PCE Download a Phone Book]
• Test Purpose
Verify that the PCE can download a Phone Book object from the PSE.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester have established a PBAP session.
- The IUT and the Lower Tester have established a PBAP session. The Lower Tester contains at least 1 non-NULL Phone Book object.
• Test Procedure
The IUT sends a PullPhoneBook request to at least one of the PBAP virtual folders supported by the Lower Tester.
• Expected Outcome
Pass verdict
The PullPhoneBook request is well formed.
PBAP/PCE/PBD/BV-04-C [PCE Get the size of a Phone Book via PullPhoneBook]
• Test Purpose
Verify that the PCE can obtain at any time Phone Book size information from the PSE.
• Reference
[1] 5.1
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
- At least one Phone Book on the Lower Tester is non-NULL.
• Test Procedure
The IUT attempts to download a Phone Book object (pb, och, ich, cch, mch) but requests the size information for the Phone Book by issuing a Max List Count of 0.
• Expected Outcome
Pass verdict
The IUT issues a PullPhoneBook command with the MaxListCount header set to 0 and retrieves the Phonebook Size.

##### 4.4.1.1 PCE Test PullPhoneBook related features

• Test Purpose
This test group contains test cases to verify the features that affect the operation of the PCE’s PullPhoneBook function. Each row represents a specific test case and requires separate PullPhoneBook requests to verify the specific Pass verdicts, as enumerated in the test cases in Table 4.7.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
1. The IUT sends a PullPhoneBook request to the Lower Tester with the given parameters of the
table below.
2. The Lower Tester sends a PullPhoneBook response with the given parameters of the table
below.
• Expected Outcome
Pass verdict
All successful requests must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
See the Additional Pass Verdicts column in Table 4.7 for additional pass criteria.

| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | PCE correctly received the response. |  |
| X-BT-UCI Feature | Common to all tests in this group: Phonebooks to test: All objects supported by the PCE. |  |  |  |
| PBAP/PCE/PBD/BV-38-C [PCE Download X-BT- UCI property when supported] | The Lower Tester’s “X-BT- UCI vCard Property” PbapSupportedFeatures bit is set The response contains multiple vCards with one or more X-BT-UCI properties | PCE correctly set the “X-BT-UCI vCard Property” bit in its PbapSupportedFeatures. PCE correctly set the X-BT-UCI property bit in the PropertySelector (if present). |  |  |
| PBAP/PCE/PBD/BV-39-C [PCE Do not download X- BT-UCI property when not supported] | The Lower Tester’s “X-BT- UCI vCard Property” PbapSupportedFeatures bit is not set | PCE correctly set the “X-BT-UCI vCard Property” bit in its PbapSupportedFeatures. PCE did not set the X-BT-UCI property bit in the PropertySelector (if present). |  |  |
| X-BT-UID Feature | Common to all tests in this group: Phonebooks to test: All objects supported by the PCE. |  |  |  |
| PBAP/PCE/PBD/BV-40-C [PCE Download X-BT- UID property when supported] | The Lower Tester’s “X-BT- UID vCard Property” PbapSupportedFeatures bit is set Multiple vCards are returned with each one having a correctly formatted X-BT- UID’s property. | PCE correctly set the “X-BT-UID vCard Property” bit in its PbapSupportedFeatures. PCE correctly set the X-BT-UID property bit in the PropertySelector (if present). |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | PCE correctly received the response. |  |
| PBAP/PCE/PBD/BV-41-C [PCE Do not download X- BT-UID property when not supported] | The Lower Tester’s “X-BT- UID vCard Property” PbapSupportedFeatures bit is not set | PCE correctly set the “X-BT-UID vCard Property” bit in its PbapSupportedFeatures. PCE did not set the X-BT-UID property bit in the PropertySelector (if present). |  |  |
| Enhanced Missed Calls Feature | Common to all tests in this group: Phonebooks to test: Any supported cch.vcf and mch.vcf objects |  |  |  |
| PBAP/PCE/PBD/BV-42-C [PCE Reset the missed calls when supported] | The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set Response contains a NewMissedCalls header. | The request contains a valid ResetNewMissedCalls header with a value of 1. |  |  |
| PBAP/PCE/PBD/BV-43-C [PCE Do not reset the missed calls when not supported] | The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is not set Response contains a NewMissedCalls header only for mch. | The request does not contain a ResetNewMissedCalls header. |  |  |
| vCard Selecting | Common to all tests in this group: Phonebooks to test: All objects supported by the PCE |  |  |  |
| PBAP/PCE/PBD/BV-44-C [PCE Download using vCardSelector when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set | The request contains a valid vCardSelector header. |  |  |
| PBAP/PCE/PBD/BV-45-C [PCE Download using vCardSelector and vCardSelectorOperator when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set | The request contains valid vCardSelector and vCardSelectorOperator headers. |  |  |
| PBAP/PCE/PBD/BV-46-C [PCE Download without vCardSelector and vCardSelectorOperator when not supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is not set | The request does not contain a vCardSelector header. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | PCE correctly received the response. |  |
| Default Contact Image Format | Common to all tests in this group: Phonebooks to test: All supported objects |  |  |  |
| PBAP/PCE/PBD/BV-47-C [PCE Download images with “Default Contact Image Format” supported] | The Lower Tester’s “Default Contact Image Format” PbapSupportedFeatures bit is set Response contains multiple vCards with images respecting the feature’s constraints. | PCE set the PHOTO property bit in the PropertySelector (if present) |  |  |
| PBAP/PCE/PBD/BV-48-C [PCE Download images with “Default Contact Image Format” not supported] | The Lower Tester’s “Default Contact Image Format” PbapSupportedFeatures bit is not set | PCE set the PHOTO property bit in the PropertySelector (if present) |  |  |

Table 4.7: Test PullPhoneBook test cases

#### 4.4.2 IUT – PSE

Verify that a PSE implementation can properly respond to requests to download the Phone Book.
PBAP/PSE/PBD/BV-02-C [PSE Return the size of a Phone Book]
• Test Purpose
Verify that the PSE can properly return the size information of a Phone Book.
• Reference
[1] 5.1
• Initial Condition
- The IUT has at least one non-NULL Phone Book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Phone Book object (pb, och, ich, cch, mch).
• Expected Outcome
Pass verdict
The Lower Tester successfully retrieved the entire Phone Book object. The Phone Book object selected is identical on the Lower Tester and on the IUT.
PBAP/PSE/PBD/BV-03-C [PSE Return a Phone Book]
• Test Purpose
Verify that the PSE can properly deliver a Phone Book.
• Reference
[1] 5.1
• Initial Condition
- The IUT has at least one non-NULL Phone Book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Phone Book object (i.e., pb, och, ich, cch, mch).
• Expected Outcome
Pass verdict
The Lower Tester successfully downloads the specified Phone Book object. The Phone Book selected is identical on the Lower Tester and on the IUT.
PBAP/PSE/PBD/BV-05-C [PSE Return NewMissedCalls Value]
• Test Purpose
Verify that the PSE can properly return the Phonebook object corresponding to the /telecom/mch folder with the correct value of the NewMissedCalls application parameter.
• Reference
[1] 5.1.4.6
• Initial Condition
- The IUT indicates that new missed calls are available. The IUT and the Lower Tester have established a PBAP connection.
• Test Procedure
The Lower Tester requests PullPhoneBook from /telecom/mch.vcf of the IUT.
• Expected Outcome
Pass verdict
The Lower Tester successfully receives the /telecom/mch.vcf Phonebook object, which is well formed, and the NewMissedCalls application parameter is included in the response with the number of new missed calls that matches the number of new missed indicated by the PSE.
PBAP/PSE/PBD/BI-01-C [PSE Reject an invalid Phone Book request]
• Test Purpose
Verify that the PSE does not abide by illegal Phone Book requests.
• Reference
[1] 5.1
• Initial Condition
- The IUT must have at least one non-NULL Phone Book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to retrieve an object that is out of scope of the PBAP Phone Book Downloading feature (the Lower Tester will at random choose to request either a Phone Book entry corresponding to the non-NULL Phone Book object of the IUT, or another object that is known to be stored on the IUT if any, or arbitrary object).
• Expected Outcome
Pass verdict
The IUT rejects all the attempts by the Lower Tester to retrieve an object.
PBAP/PSE/PBD/BV-06-C [PSE Return a persistent Database Identifier via PullPhoneBook]
• Test Purpose
Verify that the PSE can share a persistent Database Identifier.
• Reference
[1] 5.1.4.9
• Initial Condition
- The IUT and the Lower Tester have been paired and have established a PBAP session.
- The Lower Tester has the ‘Database Identifier’ PbapSupportedFeatures bit set.
• Test Procedure
Execute for all the phonebook objects supported by the IUT
1. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
2. The IUT sends a response with a Database Identifier value (A).
3. The Lower Tester closes and re-establishes a PBAP session with the IUT.
4. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
5. The IUT sends a response with a Database Identifier value (B).
• Expected Outcome
Pass verdict
The Database Identifiers returned (A & B) have equal values and are non-NULL.
PBAP/PSE/PBD/BV-07-C [PSE Return a regenerated Database Identifier via PullPhoneBook]
• Test Purpose
Verify that the PSE can regenerate a persistent Database Identifier.
• Reference
[1] 5.1.4.9
• Initial Condition
- The IUT and the Lower Tester have been paired and have established a PBAP session.
- The Lower Tester has the ‘Database Identifier’ PbapSupportedFeatures bit set.
• Test Procedure
Execute for all the phonebook objects supported by the IUT.
1. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
2. The IUT sends a response with a Database Identifier value (A).
3. The Lower Tester closes the PBAP session.
4. The user is requested to trigger a regeneration of a new Database Identifier value (e.g., due to a
factory reset, change counter rollover, contact X-BT-UID rollover or any other event).
5. The Lower Tester re-establishes the PBAP session.
6. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
7. The IUT sends a response with a Database Identifier value (B).
• Expected Outcome
Pass verdict
The Database Identifiers (A & B) have unequal values and are non-NULL.
PBAP/PSE/PBD/BV-08-C [PSE Return updated Folder Version via PullPhoneBook due to property change 1]
• Test Purpose
Verify that the PSE correctly handles the Folder Version Counters when its contents are updated.
• Reference
[1] 5.1.4.8, 5.1.4.9
• Initial Condition
- The IUT and the Lower Tester have been paired and have established a PBAP session.
- The Lower Tester has the ‘Database Identifier’ and the ‘Folder Version Counters’ PbapSupportedFeatures bits set.
• Test Procedure
Execute for all pb, fav, and spd objects supported by the IUT.
1. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
2. The IUT sends a response with a PrimaryFolderVersion of value (A1) and a
SecondaryFolderVersion of value (A2) and a Database Identifier of value (A3).
3. The Lower Tester closes and re-establishes a PBAP session with the IUT.
4. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
5. The IUT sends a response with a PrimaryFolderVersion of value (B1) and a
SecondaryFolderVersion of value (B2) and a Database Identifier of value (B3).
6. The user is requested to modify the N, TEL, EMAIL, MAILER, ADR or X-BT-UCI property of an
existing contact.
8. The IUT sends a response with a PrimaryFolderVersion of value (C1) and a
SecondaryFolderVersion of value (C2) and a Database Identifier of value (C3).
• Expected Outcome
Pass verdict
The Database Identifiers returned (A3, B3, and C3) are all equal and non-NULL.
The PrimaryFolderVersions (A1) and (B1) are equal.
The PrimaryFolderVersions (B1) and (C1) are not equal.
The SecondaryFolderVersions (A2) and (B2) are equal.
The SecondaryFolderVersions (B2) and (C2) are not equal.
PBAP/PSE/PBD/BV-09-C [PSE Return updated Folder Version via PullPhoneBook due to property change 2]
• Test Purpose
Verify that the PSE correctly handles the Folder Level Version Identifiers when its contents are updated.
• Reference
[1] 5.1.4.8, 5.1.4.9
• Initial Condition
- The IUT and the Lower Tester have been paired and have established a PBAP session.
- The Lower Tester has the ‘Database Identifier’ and the ‘Folder Version Counters’ PbapSupportedFeatures bits set.
• Test Procedure
Execute for all pb, fav, and spd objects supported by the IUT.
1. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
2. The IUT sends a response with a PrimaryFolderVersion of value (A1) and a
SecondaryFolderVersion of value (A2) and a Database Identifier of value (A3).
3. The Lower Tester closes and re-establishes a PBAP session with the IUT.
4. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
5. The IUT sends a response with a PrimaryFolderVersion of value (B1) and a
SecondaryFolderVersion of value (B2) and a Database Identifier of value (B3).
6. The user is requested to modify a property other than N, FN, TEL, EMAIL, MAILER, ADR or X-
BT-UCI of an existing contact.
7. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
8. The IUT sends a response with a PrimaryFolderVersion of value (C1) and a
SecondaryFolderVersion of value (C2) and a Database Identifier of value (C3).
• Expected Outcome
Pass verdict
The Database Identifiers returned (A3, B3, and C3) are all equal and non-NULL.
The PrimaryFolderVersions (A1) and (B1) are equal.
The PrimaryFolderVersions (B1) and (C1) are not equal.
The SecondaryFolderVersions (A2, B2, and C2) are equal.
PBAP/PSE/PBD/BV-10-C [PSE Return updated Folder Version via PullPhoneBook due to entry deletion/insertion]
• Test Purpose
Verify that the PSE correctly handles the Folder Level Version Identifiers when its contents are updated.
• Reference
[1] 5.1.4.8, 5.1.4.9
• Initial Condition
- The IUT and the Lower Tester have been paired and have established a PBAP session.
- The Lower Tester has the ‘Database Identifier’ and the ‘Folder Version Counters’ PbapSupportedFeatures bits set.
• Test Procedure
Execute for all phonebook objects supported by the IUT.
1. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
2. The IUT sends a response with a PrimaryFolderVersion of value (A1) and a
SecondaryFolderVersion of value (A2) and a Database Identifier of value (A3).
3. The Lower Tester closes and re-establishes a PBAP session with the IUT.
4. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
5. The IUT sends a response with a PrimaryFolderVersion of value (B1) and a
SecondaryFolderVersion of value (B2) and a Database Identifier of value (B3).
6. The user is requested to add or remove a Contact on the IUT.
7. The Lower Tester sends a PullPhoneBook with MaxListSize = 0 request to the IUT.
8. The IUT sends a response with a PrimaryFolderVersion of value (C1) and a
SecondaryFolderVersion of value (C2) and a Database Identifier of value (C3).
• Expected Outcome
Pass verdict
The Database Identifiers returned (A3, B3, and C3) are all equal and non-NULL.
The PrimaryFolderVersions (A1) and (B1) are equal.
The PrimaryFolderVersions (B1) and (C1) are not equal.
The SecondaryFolderVersions (B2) and (C2) are not equal.

##### 4.4.2.1 PSE Test PullPhoneBook size and selecting related features

• Test Purpose
This test group test group contains test cases to verify the features that affect the operation of the PSE’s PullPhoneBook function, particularly regarding the size of the objects and the selecting of items. Each row represents a specific test case and requires separate PullPhoneBook requests to verify the specific Pass verdicts, as enumerated in the test cases in Table 4.8.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
1. The Lower Tester sends a PullPhoneBook request to the IUT with the given parameters of the
table below.
2. The IUT sends a response.
3. The Lower Tester sends a PullPhoneBook request to the IUT for the complete phone book of the
same phonebook object.
4. The IUT sends the complete phonebook to the Lower Tester.
5. The Lower Tester verifies the result of Step 2 using information from the phonebook received in
Step 4.
• Expected Outcome
Pass verdict
All successful responses (response code 0x90 or 0xA0) must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
- A PrimaryFolderVersion header if the “Folder Version Counters” bit of the IUT’s PbapSupportedFeatures is set.
- A SecondaryFolderVersion header if the “Folder Version Counters” bit of the IUT’s PbapSupportedFeatures is set.
- A DatabaseIdentifier header if the “Database Identifier” bit of the IUT’s PbapSupportedFeatures is set.
See the Additional Pass Verdicts column in Table 4.8 for additional pass criteria.

| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | The response(s) is/are successful |  |
|  |  |  | (response code is 0x90 or 0xA0). |  |
| Phone Book Object Size |  |  |  |  |
| PBAP/PSE/PBD/BV-17-C [PSE Return phonebook size] | Phonebooks to test: All supported phonebook objects MaxListCount=0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements. The response of Step 4 can be used to determine this. The mch object response has valid NewMissedCalls header. |  |  |
| Enhanced Missed Calls Feature |  |  |  |  |
| PBAP/PSE/PBD/BV-18-C [PSE Return newMissedCalls for cch when supported] | Phonebooks to test: All supported cch.vcf objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set | The response contains a Body with vCards. The response contains a NewMissedCalls header. |  |  |
| PBAP/PSE/PBD/BV-19-C [PSE Do not return newMissedCalls for cch when not supported] | Phonebooks to test: All supported cch.vcf objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is not set | The response contains a Body with vCards. The response does not contain a NewMissedCalls header. |  |  |
| PBAP/PSE/PBD/BV-20-C [PSE Reset and return newMissedCalls when supported] | Phonebooks to test: All supported cch.vcf and mch.vcf objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set ResetNewMissedCalls =1 | The response contains a Body with vCards. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |
| PBAP/PSE/PBD/BV-21-C [PSE Reset and return newMissedCalls and phone book size when supported] | Phonebooks to test: All supported cch.vcf and mch.vcf objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set ResetNewMissedCalls = 1 MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements. The response of Step 4 can be used to determine this. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | The response(s) is/are successful |  |
|  |  |  | (response code is 0x90 or 0xA0). |  |
| PBAP/PSE/PBD/BV-22-C [PSE Reset and return newMissedCalls and phone book size with vCardSelector when supported] | Phonebooks to test: All supported cch.vcf and mch.vcf objects The Lower Tester’s “Enhanced Missed Calls” and “vCard Selecting” PbapSupportedFeatures bits are set ResetNewMissedCalls = 1 MaxListCount = 0 vCardSelector=[See IXIT] | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (OR-logic). The response of Step 4 can be used to determine this. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |
| PBAP/PSE/PBD/BV-23-C [PSE Reset and return newMissedCalls and phone book size with vCardSelector and vCardSelectorOperator when supported] | Phonebooks to test: All supported cch.vcf and mch.vcf objects The Lower Tester’s “Enhanced Missed Calls” and “vCard Selecting” PbapSupportedFeatures bits are set ResetNewMissedCalls = 1 MaxListCount = 0 vCardSelector=[See IXIT] vCardSelectorOperator = 1 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (AND-logic). The response of Step 4 can be used to determine this. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |
| vCard Selecting | Common to all tests in this group: Phonebooks to test: All objects supported by the PSE |  |  |  |
| PBAP/PSE/PBD/BV-24-C [PSE Return phone book using vCardSelector when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] | The response contains a Body with vCards. The response body contains valid elements respecting the vCardSelector criteria (OR-logic). The response of Step 4 can be used to determine this. |  |  |
| PBAP/PSE/PBD/BV-25-C [PSE Return phone book using vCardSelector and vCardSelectorOperator ‘OR’ when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] vCardSelectorOperator = 0 | The response contains a Body with vCards. The response body contains valid elements respecting the vCardSelector criteria (OR-logic). The response of Step 4 can be used to determine this. |  |  |
| PBAP/PSE/PBD/BV-26-C [PSE Return phone book using vCardSelector and vCardSelectorOperator ‘AND’ when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] vCardSelectorOperator = 1 | The response contains a Body with vCards. The response body contains valid elements respecting the vCardSelector criteria (AND-logic). The response of Step 4 can be used to determine this. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | The response(s) is/are successful |  |
|  |  |  | (response code is 0x90 or 0xA0). |  |
| PBAP/PSE/PBD/BV-27-C [PSE Return phone book size using vCardSelector when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (OR-logic). The response of Step 4 can be used to determine this. |  |  |
| PBAP/PSE/PBD/BV-28-C [PSE Return phone book size using vCardSelector and vCardSelectorOperator ‘AND’ when supported] | The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] vCardSelectorOperator = 1 MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (AND-logic). The response of Step 4 can be used to determine this. |  |  |

Table 4.8: Test PullPhoneBook Size and Selecting test cases

##### 4.4.2.2 PSE Test PullPhoneBook vCard Contents related features

• Test Purpose
This test group contains test cases to verify the features that affect the operation of the PSE’s PullPhoneBook function, particularly regarding the contents of the vCards exchanged. The verification is done for each PullPhoneBook procedure performed, as enumerated in the test cases in Table 4.9.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
Send a PullPhoneBook request to the IUT with the given parameters of the table below.
• Expected Outcome
Pass verdict
All successful responses (response code 0x90 or 0xA0) must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
- A PrimaryFolderVersion header if the “Folder Version Counters” bit of the IUT’s PbapSupportedFeatures is set.
- A SecondaryFolderVersion header if the “Folder Version Counters” bit of the IUT’s PbapSupportedFeatures is set.
- A DatabaseIdentifier header if the “Database Identifier” bit of the IUT’s PbapSupportedFeatures is set.

| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | The response(s) is/are successful |  |
|  |  |  | (response code is 0x90 or 0xA0). |  |
| X-BT-UCI Feature | Common to all tests in this group: Phonebooks to test: All objects supported by the PSE |  |  |  |
| PBAP/PSE/PBD/BV-29-C [PSE Return X-BT-UCI properties when supported] | The Lower Tester’s “X-BT- UCI vCard Property” PbapSupportedFeatures bit is set | Multiple vCards are returned some of which have one or more correctly formatted X-BT-UCI properties. |  |  |
| PBAP/PSE/PBD/BV-30-C [PSE Do not return X-BT-UCI properties when not supported] | The Lower Tester’s “X-BT- UCI vCard Property” PbapSupportedFeatures bit is not set | No X-BT-UCI properties are present in the vCards of the response. |  |  |
| X-BT-UID Feature | Common to all tests in this group: Phonebooks to test: All supported pb.vcf objects |  |  |  |
| PBAP/PSE/PBD/BV-31-C [PSE Return X-BT-UID properties when supported] | The Lower Tester’s “X-BT- UID vCard Property” PbapSupportedFeatures bit is set | Multiple vCards are returned with each one having a correctly formatted X-BT-UID property |  |  |
| PBAP/PSE/PBD/BV-32-C [PSE Do not return X-BT-UID properties when not supported] | The Lower Tester’s “X-BT- UID vCard Property” PbapSupportedFeatures bit is not set | No X-BT-UID properties are present in the vCards of the response. |  |  |
| Referencing Contacts |  |  |  |  |
| PBAP/PSE/PBD/BV-33-C [PSE Reference X-BT-UID properties when supported] | Phonebooks to test: All supported cch.vcf, mch.vcf, ich.vcf, och.vcf, fav.vcf, spd.vcf objects The Lower Tester’s “Referencing Contacts” PbapSupportedFeatures bit is set | Multiple vCards are returned some of which have a correctly formatted X- BT-UID property. |  |  |
| PBAP/PSE/PBD/BV-34-C [PSE Do not reference X-BT- UID properties when not supported] | Phonebooks to test: All supported cch.vcf, mch.vcf, ich.vcf, och.vcf, fav.vcf, spd.vcf objects The Lower Tester’s “Referencing Contacts” PbapSupportedFeatures bit is not set | No X-BT-UID properties are present in the vCards of the response. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this column: |  |
|  |  |  | The response(s) is/are successful |  |
|  |  |  | (response code is 0x90 or 0xA0). |  |
| Default Contact Image Format | Common to all tests in this group: Phonebooks to test: All objects supported by the PSE |  |  |  |
| PBAP/PSE/PBD/BV-35-C [PSE Return images when requested] | PropertySelector = 0x18F (VERSION FN N PHOTO TEL EMAIL) The Lower Tester has the ability to display or evaluate images | At least one vCard in at least one of the Phone Book objects that is returned has a correctly formatted contact image. It should be displayed on the Lower Tester and confirmed by the test operator. |  |  |
| PBAP/PSE/PBD/BV-36-C [PSE Do not return images when not requested] | PropertySelector = 0x187 (VERSION FN N TEL EMAIL) | vCards do not contain any images |  |  |
| Speed Dial folder |  |  |  |  |
| PBAP/PSE/PBD/BV-37-C [PSE Return Speed Dial entries] | Phonebooks to test: All supported spd.vcf | Multiple vCards are returned each having a correctly formatted X-BT- SPEEDDIALKEY property in the response. |  |  |

Table 4.9: Test PullPhoneBook Contact test cases

### 4.5 Phone Book Browsing Functional Components

Verify that the functions that are necessary for the Phone Book Browsing feature are correctly implemented.

#### 4.5.1 IUT – PCE

Verify that a PCE implementation can properly browse the Phone Book.
PBAP/PCE/PBB/BV-01-C [PCE Select a Phone Book]
• Test Purpose
Verify that the PCE can select a Phone Book.
• Reference
[1] 5.1
• Initial Condition
- A PBAP session is ongoing between the IUT and the Lower Tester.
- A PBAP session is ongoing between the IUT and the Lower Tester. At least one non-NULL Phone Book is available on the Lower Tester.
• Test Procedure
The IUT sends as many SetPhoneBook requests as necessary to set the current folder to a folder corresponding to a non-NULL Phone Book object on the Lower Tester.
• Expected Outcome
Pass verdict
All the SetPhoneBook requests are valid and accepted by the Lower Tester.
PBAP/PCE/PBB/BV-02-C [PCE Get a list of Phone Book entries]
• Test Purpose
Verify that the PCE can retrieve a list of Phone Book entries from the PSE.
• Reference
[1] 5.3
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
- At least one non-NULL Phone Book is available on the Lower Tester.
- ALT 1: The IUT has successfully set the current folder to /telecom/.
or
- ALT 2: The IUT has successfully set the current folder to a non-NULL phone book directory on the Lower Tester.
• Test Procedure
ALT 1: The IUT requests the Phone Book-listing object with the NAME header set to a non-NULL Phone Book that is available on the Lower Tester.
ALT2: The IUT requests the Phone Book-listing object with an empty NAME header.
• Expected Outcome
Pass verdict
The IUT issues a well-formed PullvCardListing command as described in section 5.3 of the PBAP specification [1].
PBAP/PCE/PBB/BV-03-C [PCE Get the size of a Phone Book]
• Test Purpose
Verify that the PCE can obtain at any time Phone Book size information from the PSE.
• Reference
[1] 5.3
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
- At least one Phone Book on the Lower Tester is non-NULL.
• Test Procedure
The IUT requests the size information for the current folder.
• Expected Outcome
Pass verdict
The IUT issues a PullvCardListing command with the MaxListCount header set to 0.
PBAP/PCE/PBB/BV-05-C [PCE Retrieve a Phone Book entry]
• Test Purpose
Verify that the PCE can retrieve a Phone Book entry from a PSE using the PullvCardEntry function with a simple filter.
• Reference
[1] 5.4
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
- The IUT has successfully set the current folder to a folder corresponding to a non-NULLNULL Phone Book on the Lower Tester.
- At least one Phone Book on the Lower Tester is non-NULL and contains non-mandatory properties in the vCards.
• Test Procedure
The IUT requests a Phone Book entry from the Lower Tester. The IUT must use the filter application parameter to request name (N) and telephone number (TEL) only.
• Expected Outcome
Pass verdict
The IUT receives the requested Phone Book entry. The received entry contains only the VERSION, N, TEL, and for vCard, 3.0 FN. Additionally, if the requested vCard contains multiple TEL properties, then multiple TEL properties are received.

##### 4.5.1.1 PCE Test PullvCardListing related features

• Test Purpose
This test group contains test cases to verify the features that affect the operation of the PCE’s PullvCardListing function. Each row represents a specific test case and requires separate PullvCardListing requests to verify the specific Pass verdicts, as enumerated in the test cases in Table 4.10.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
1. IUT sends a PullvCardListing request to the Lower Tester with the given parameters of the table
below.
2. The Lower Tester sends a PullvCardListing response with the given parameters of the table
below.
• Expected Outcome
Pass verdict
All successful requests must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
See the Additional Pass Verdicts column in Table 4.10 for additional pass criteria.

| Test Case Name | Additional Lower Tester Settings |  | Additional Pass |  |
| --- | --- | --- | --- | --- |
|  |  |  | Verdicts |  |
|  |  |  | Common to all tests in |  |
|  |  |  | this column: |  |
|  |  |  | PCE correctly received |  |
|  |  |  | the response |  |
| Enhanced Missed Calls Feature |  |  |  |  |
| PBAP/PCE/PBB/BV-39-C [PCE Reset the missed calls when supported] | Phonebooks to test: Any supported cch.vcf and mch.vcf objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set Response contains a NewMissedCalls header. | The request contains a valid ResetNewMissedCalls header with a value of 1. |  |  |
| PBAP/PCE/PBB/BV-40-C [PCE Do not reset the missed calls when not supported] | Phonebooks to test: Any supported cch.vcf and mch.vcf objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is not set Response contains a NewMissedCalls header only for mch. | The request does not contain a ResetNewMissedCalls header. |  |  |
| vCard Selecting |  |  |  |  |
| PBAP/PCE/PBB/BV-41-C [PCE Send a PullvCardListing with a vCardSelector when supported] | Phonebooks to test: All objects supported by the PCE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set | The request contains a valid vCardSelector header. |  |  |
| PBAP/PCE/PBB/BV-42-C [PCE Send a PullvCardListing without a vCardSelector when not supported] | Phonebooks to test: All objects supported by the PCE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is not set | The request does not contain a vCardSelector header. |  |  |

Table 4.10: Test PullvCardListing test cases
• Test Purpose
This test group contains test cases to verify the features that affect the operation of the PCE’s PullvCardEntry function. Each row represents a specific test case and requires separate PullvCardEntry requests to verify the specific Pass verdicts, as enumerated in the test cases in Table 4.11.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
1. IUT sends a PullvCardListing request to the Lower Tester with the given parameters of IUT sends
a PullvCardEntry request to the Lower Tester with the given parameters of the table below.
2. The Lower Tester sends a PullvCardEntry response with the given parameters of the table below.
• Expected Outcome
Pass verdict
All successful requests must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
See the Additional Pass Verdicts column in Table 4.11 for additional pass criteria.

| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this |  |
|  |  |  | column: |  |
|  |  |  | PCE correctly received the |  |
|  |  |  | response. |  |
| X-BT-UCI Feature | Common to all tests in this group: Phonebooks to test: All objects supported by the PCE. The Lower Tester’s “X-BT-UCI vCard Property”. |  |  |  |
| PBAP/PCE/PBB/BV-33-C [PCE Send a PullvCardEntry with X- BT-UCI when supported] | PbapSupportedFeatures bit is set The response contains a vCard with one or more X-BT-UCI properties. | PCE correctly set the “X-BT-UCI vCard Property” bit in its PbapSupportedFeatures. PCE correctly set the X-BT-UCI property bit in the PropertySelector (if present). |  |  |
| PBAP/PCE/PBB/BV-34-C [PCE Send a PullvCardEntry without X- BT-UCI when not supported] | PbapSupportedFeatures bit is not set. | PCE did not set the X-BT-UCI property bit in the PropertySelector (if present). |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this |  |
|  |  |  | column: |  |
|  |  |  | PCE correctly received the |  |
|  |  |  | response. |  |
| X-BT-UID Feature | Common to all tests in this group: Phonebooks to test: All objects supported by the PCE. The Lower Tester’s “X-BT-UID vCard Property”. |  |  |  |
| PBAP/PCE/PBB/BV-35-C [PCE Send a PullvCardEntry with X- BT-UID when supported] | PbapSupportedFeatures bit is set. A vCard is returned having a correctly formatted X-BT-UID property. | PCE correctly set the “X-BT-UID vCard Property” bit in its PbapSupportedFeatures. PCE correctly set the X-BT-UID property bit in the PropertySelector (if present). |  |  |
| PBAP/PCE/PBB/BV-36-C [PCE Send a PullvCardEntry without X- BT-UID when not supported] | PbapSupportedFeatures bit is not set. | PCE did not set the X-BT-UID property bit in the PropertySelector (if present). |  |  |
| PBAP/PCE/PBB/BV-43-C [PCE Send a PullvCardEntry with header ‘Name’ set to a valid UID] | PbapSupportedFeatures bit is set. The vCard returned has the X-BT- UID property set to the UID of the request. | PCE correctly set the “X-BT-UID vCard Property” bit in its PbapSupportedFeatures. PCE correctly set the X-BT-UID property bit in the PropertySelector (if present). PCE correctly set a valid UID in the Name header. |  |  |
| Default Contact Image Format | Common to all tests in this group: Phonebooks to test: Any supported objects The Lower Tester’s “Default Contact Image Format” |  |  |  |
| PBAP/PCE/PBB/BV-37-C [PCE Send a PullvCardEntry with image when supported] | PbapSupportedFeatures bit is set. Response contains a vCard with an image respecting the feature’s constraints. | PCE set the PHOTO property bit in the PropertySelector (if present). |  |  |
| PBAP/PCE/PBB/BV-38-C [PCE Send a PullvCardEntry without image when not supported] | PbapSupportedFeatures bit is not set. |  |  |  |

Table 4.11: Test PullvCardEntry test cases

#### 4.5.2 IUT – PSE

Verify that a PSE implementation can respond to the PCE’s requests to browse the Phone Book.
PBAP/PSE/PBB/BV-06-C [PSE Set the current Phone Book]
• Test Purpose
Verify that the PSE can properly process requests to change the current folder.
• Reference
[1] 5.2
• Initial Condition
- The IUT contains at least one non-NULL Phone Book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester sends a SetPhoneBook request to the IUT.
• Expected Outcome
Pass verdict
The IUT sets the current folder to the one that was requested by the Lower Tester.
PBAP/PSE/PBB/BV-07-C [PSE Return a list of Phone Book entries]
• Test Purpose
Verify that the PSE can properly generate and return a vCard-listing object.
• Reference
[1] 5.3
• Initial Condition
- There must be at least one non-NULL Phone Book available on the IUT.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester requests the vCard-listing object corresponding to the current Phone Book.
• Expected Outcome
Pass verdict
The Lower Tester can successfully retrieve the vCard-listing object from the IUT. The content of this object is accurate.
• Test Purpose
Verify that the PSE can properly return the size information of a Phone Book.
• Reference
[1] 5.3
• Initial Condition
- The IUT has at least one non-NULL Phone Book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester successively retrieves Phone Book size information corresponding to the requested Phone Book object.
• Expected Outcome
Pass verdict
The Lower Tester successfully retrieves the size for the specified Phone Book object. The Phone Book sizes are identical on the Lower Tester and on the IUT.
PBAP/PSE/PBB/BV-09-C [PSE Return the vCard Listing Object]
• Test Purpose
Verify that the PSE can properly return the vCard-listing object corresponding to the current folder.
• Reference
[1] 5.3
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to retrieve from the PSE the vCard-listing object corresponding to the current folder by use of PullvCardListing with an empty name header.
• Expected Outcome
Pass verdict
The Lower Tester successfully retrieved the vCard-listing object.
PBAP/PSE/PBB/BV-10-C [PSE Return a Phone Book entry]
• Test Purpose
Verify that the PSE can return Phone Book entry.
• Reference
[1] 5.4
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
- The IUT has a vCard-listing object containing at least one non-NULL card handle.
• Test Procedure
The Lower Tester requests one of the vCard entries present in the vCard-listing object sent from the IUT.
• Expected Outcome
Pass verdict
The Lower Tester can successfully retrieve the vCard object from the IUT. The content of this object is accurate.
PBAP/PSE/PBB/BV-11-C [PSE Return the Number of NewMissedCalls]
• Test Purpose
Verify that the PSE can properly return the vCard-listing object corresponding to the /telecom/mch folder with the correct value of the NewMissedCalls application parameter.
• Reference
[1] 5.3.4.7
• Initial Condition
- The IUT indicates that new missed calls are available. The IUT and the Lower Tester have established a PBAP connection.
• Test Procedure
The Lower Tester requests PullvCardListing with an empty name header from /telecom/mch to the IUT.
• Expected Outcome
Pass verdict
The Lower Tester successfully retrieved the vCard-listing object containing the NewMissedCalls application parameter that matches the number of new missed calls indicated to the user by the PSE.
PBAP/PSE/PBB/BI-01-C [PSE Reject an invalid Phone Book selection]
• Test Purpose
Verify that the PSE does not accept SetPhoneBook requests to non-existing Phone Books or any object that is out of scope of the PBAP.
• Reference
[1] 5.2
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester issues an invalid SetPhoneBook request by using either a non-existing Phone Book (if any are not supported on the IUT) or an arbitrary folder name.
• Expected Outcome
Pass verdict
The IUT rejects the request.
PBAP/PSE/PBB/BI-07-C [PSE Prevent use of NULL characters in objects]
• Test Purpose
Verify that NULL characters are not used by the PSE when returning a vCard object.
• Reference
[1] 5.2
• Initial Condition
- The IUT has at least one non-NULL Phone Book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Condition
The test should be performed under normal conditions. Both devices have to be in communication range.
• Test Procedure
The Lower Tester attempts to retrieve from the PSE the vCard-listing object.
• Expected Outcome
Pass verdict
The retrieved vCard-listing object is encoded in Base 64 (default) or Quoted-Printable encoding (alphanumeric) and does not contain any NULL characters.

##### 4.5.2.1 PSE Test PullvCardListing size and selecting related features

• Test Purpose
This test group test group contains test cases to verify the features that affect the operation of the PSE’s PullvCardListing function, particularly regarding the size of the objects and selection of items. Each row represents a specific test case and requires separate PullvCardListing requests to verify the specific Pass verdicts, as enumerated in the test cases in Table 4.12.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
1. The Lower Tester sends a PullvCardListing request to the IUT with the given parameters of the
table below.
2. The IUT sends a response.
3. The Lower Tester sends a PullPhoneBook request to the IUT for the entire phonebook object
corresponding to the virtual folder.
4. The IUT sends the requested phonebook to the Lower Tester.
5. The Lower Tester verifies the result of Step 2 using information from the phonebook received in
Step 4.
• Expected Outcome
Pass verdict
All successful responses (response code 0x90 or 0xA0) must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
- A PrimaryFolderVersion header if the “Folder Version Counters” bit of the IUT’s PbapSupportedFeatures is set.
- A SecondaryFolderVersion header if the “Folder Version Counters” bit of the IUT’s PbapSupportedFeatures is set.
- A DatabaseIdentifier header if the “Database Identifier” bit of the IUT’s PbapSupportedFeatures is set.
See the Additional Pass Verdicts column in Table 4.12 for additional pass criteria.

| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this |  |
|  |  |  | column: |  |
|  |  |  | The response(s) is/are |  |
|  |  |  | successful (response code is |  |
|  |  |  | 0x90 or 0xA0). |  |
| Phone Book Object Size |  |  |  |  |
| PBAP/PSE/PBB/BV-12-C [PSE Return PullvCardListing with size] | Phonebooks to test: All supported phonebook virtual folder objects MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements. The response of Step 4 can be used to determine this. The mch object response has valid NewMissedCalls header. |  |  |
| Enhanced Missed Calls Feature |  |  |  |  |
| PBAP/PSE/PBB/BV-13-C [PSE Return PullvCardListing with newMissedCalls when supported] | Phonebooks to test: All supported cch virtual folder objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set | The response contains a Body with XML entries. The response contains a NewMissedCalls header. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this |  |
|  |  |  | column: |  |
|  |  |  | The response(s) is/are |  |
|  |  |  | successful (response code is |  |
|  |  |  | 0x90 or 0xA0). |  |
| PBAP/PSE/PBB/BV-14-C [PSE Return PullvCardListing without newMissedCalls when not supported] | Phonebooks to test: All supported cch virtual folder objects The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is not set | The response contains a Body with XML entries. The response does not contain a NewMissedCalls header. |  |  |
| PBAP/PSE/PBB/BV-15-C [PSE Return PullvCardListing and reset NewMissedCalls] | Phonebooks to test: All supported cch and mch virtual folder objects: The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set ResetNewMissedCalls = 1 | The response contains a Body with XML entries. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |
| PBAP/PSE/PBB/BV-16-C [PSE Return PullvCardListing size and reset NewMissedCalls] | Phonebooks to test: All supported cch and mch virtual folder objects: The Lower Tester’s “Enhanced Missed Calls” PbapSupportedFeatures bit is set ResetNewMissedCalls = 1 MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements. The response of Step 4 can be used to determine this. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |
| PBAP/PSE/PBB/BV-17-C [PSE Return PullvCardListing size with vCardSelector and reset NewMissedCalls] | Phonebooks to test: All supported cch and mch virtual folder objects The Lower Tester’s “Enhanced Missed Calls” and “vCard Selecting” PbapSupportedFeatures bits are set ResetNewMissedCalls = 1 MaxListCount = 0 vCardSelector=[See IXIT] | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (OR- logic). The response of Step 4 can be used to determine this. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this |  |
|  |  |  | column: |  |
|  |  |  | The response(s) is/are |  |
|  |  |  | successful (response code is |  |
|  |  |  | 0x90 or 0xA0). |  |
| PBAP/PSE/PBB/BV-18-C [PSE Return PullvCardListing size with vCardSelector and vCardSelectorOperator and reset NewMissedCalls] | Phonebooks to test: All supported cch and mch virtual folder objects The Lower Tester’s “Enhanced Missed Calls” and “vCard Selecting” PbapSupportedFeatures bits are set ResetNewMissedCalls = 1 MaxListCount = 0 vCardSelector=[See IXIT] vCardSelectorOperator = 1 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (AND- logic). The response of Step 4 can be used to determine this. The response contains a valid NewMissedCalls header. The response of Step 4 has its NewMissedCalls counter reset to 0. |  |  |
| vCard Selecting |  |  |  |  |
| PBAP/PSE/PBB/BV-19-C [PSE Return PullvCardListing with vCardSelector] | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] | The response contains a Body with XML entries. The response body contains valid elements respecting the vCardSelector criteria (OR- logic). The response of Step 4 can be used to determine this. |  |  |
| PBAP/PSE/PBB/BV-20-C [PSE Return PullvCardListing with vCardSelector and vCardSelectorOperator ‘OR’] | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] vCardSelectorOperator = 0 | The response contains a Body with XML entries. The response body contains valid elements respecting the vCardSelector criteria (OR- logic). The response of Step 4 can be used to determine this. |  |  |
| PBAP/PSE/PBB/BV-21-C [PSE Return PullvCardListing with vCardSelector and vCardSelectorOperator ‘AND’] | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] vCardSelectorOperator = 1 | The response contains a Body with XML entries. The response body contains valid elements respecting the vCardSelector criteria (AND- logic). The response of Step 4 can be used to determine this. |  |  |


| Test Case Name | Additional Lower Tester Settings |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- |
|  |  |  | Common to all tests in this |  |
|  |  |  | column: |  |
|  |  |  | The response(s) is/are |  |
|  |  |  | successful (response code is |  |
|  |  |  | 0x90 or 0xA0). |  |
| PBAP/PSE/PBB/BV-22-C [PSE Return PullvCardListing size with vCardSelector] | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (OR- logic). The response of Step 4 can be used to determine this. |  |  |
| PBAP/PSE/PBB/BV-23-C [PSE Return PullvCardListing size with vCardSelector and vCardSelectorOperator ‘AND’] | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “vCard Selecting” PbapSupportedFeatures bit is set vCardSelector=[See IXIT] vCardSelectorOperator = 1 MaxListCount = 0 | The response does not contain a Body. The PhonebookSize header contains the correct number of elements respecting the vCardSelector criteria (AND- logic). The response of Step 4 can be used to determine this. |  |  |

Table 4.12: Test PullvCardListing Content test cases

##### 4.5.2.2 PSE Test PullvCardEntry vCard Contents related features

• Test Purpose
This test group test group contains test cases to verify the features that affect the operation of the PSE’s PullvCardEntry function, particularly regarding the content of the vCards. Each row represents a specific test case and requires separate PullvCardEntry requests to verify the specific Pass verdicts, as enumerated in the test cases in Table 4.13.
• Reference
[1] 5.1
• Initial Condition
- The IUT and the Lower Tester are paired.
- The IUT and the Lower Tester are connected and a PBAP session is ongoing.
• Test Procedure
1. The Lower Tester sends a PullvCardListing optionally with vCardSelector set to the vCard
property according to the table below.
2. The IUT sends a response.
3. The Lower Tester sends a PullvCardEntry request to the IUT for one of the vCards in the
response of Step 2 with the given parameters of the table below.
• Expected Outcome
Pass verdict
All successful responses (response code 0x90 or 0xA0) must contain:
- A SRM enabled header if GOEP 2.0 or later is used.
- A DatabaseIdentifier header if the “Database Identifier” bit of the IUT’s PbapSupportedFeatures is set.
See the Additional Pass Verdicts column in Table 4.13 for additional pass criteria.

|  | Test Case Name |  |  | Additional Lower Tester Settings |  |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-BT-UCI Feature |  |  |  |  |  |  |  |  |
| PBAP/PSE/PBB/BV-24-C [PSE Return PullvCardEntry with X- BT-UCI properties when supported] |  |  | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UCI vCard Property” PbapSupportedFeatures bit is set The Lower Tester sent a vCardSelector with the X-BT-UCI bit set in the PullvCardListing request. |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has one or more correctly formatted X- BT-UCI properties. |  |  |
| PBAP/PSE/PBB/BV-25-C [PSE Return PullvCardEntry without X- BT-UCI properties when not supported] |  |  | Phonebooks to test: All virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UCI vCard Property” PbapSupportedFeatures bit is not set The Lower Tester sent a vCardSelector with the X-BT-UCI bit set in the PullvCardListing request. |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The X-BT-UCI property is NOT present in the returned vCard. |  |  |
| X-BT-UID Feature |  |  |  |  |  |  |  |  |
| PBAP/PSE/PBB/BV-26-C [PSE Return PullvCardEntry with X- BT-UID properties when supported] |  |  | Phonebooks to test: All pb virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UID vCard Property” PbapSupportedFeatures bit is set The Lower Tester sent a vCardSelector with the X-BT-UID bit set in the PullvCardListing request. |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has a correctly formatted X-BT-UID property. |  |  |
| PBAP/PSE/PBB/BV-27-C [PSE Return PullvCardEntry without X- BT-UID properties when not supported] |  |  | Phonebooks to test: All pb virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UID vCard Property” PbapSupportedFeatures bit is not set The Lower Tester did not sent a vCardSelector in the PullvCardListing request |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The X-BT-UID property is NOT present in the returned vCards. |  |  |


|  | Test Case Name |  |  | Additional Lower Tester Settings |  |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PBAP/PSE/PBB/BV-44-C [PSE Respond to a PullvCardEntry with a valid X-BT-UID] |  |  | Phonebooks to test: All pb virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UID vCard Property” PbapSupportedFeatures bit is set The Lower Tester sends a vCardSelector with the X-BT-UID bit set in the PullvCardListing request. The Lower Tester sends a PullvCardEntry to obtain any vCard object listed on the previous PullvCardListing response. The Lower Tester sends another PullvCardEntry with the header ‘Name’ set to the X-BT-UID obtained from the previous PullvCardEntry request. |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has a correctly formatted X-BT-UID property. The value of the X-BT-UID property is equal to the X-BT- UID of the PullvCardEntry’s Name header. |  |  |
| PBAP/PSE/PBB/BV-45-C [PSE Respond to a PullvCardEntry with an invalid UID] |  |  | Phonebooks to test: All pb virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UID vCard Property” PbapSupportedFeatures bit is set. The Lower Tester sends a PullvCardEntry with the header ‘Name’ set to an inexistent X-BT-UID [See TSPX PullVCardEntry invalid value] _ _ _ |  |  | The response code of the response is returned as error code ‘NOT FOUND’. |  |  |
| PBAP/PSE/PBB/BV-46-C [PSE Respond to a PullvCardEntry with a valid UID from a different folder] |  |  | Phonebooks to test: All pb virtual folder objects supported by the PSE The Lower Tester’s “X-BT-UID vCard Property” PbapSupportedFeatures bit is set. The Lower Tester sends a vCardSelector with the X-BT-UID bit set in the PullvCardListing request. The Lower Tester sends a PullvCardEntry to obtain any vCard object listed on the previous PullvCardListing response. The Lower Tester sends another PullvCardEntry with the header ‘Name’ set to the X-BT UID obtained from the previous PullvCardEntry request, while the virtual folder of the vCard of the requested X-BT UID is different than the current virtual folder. |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has a correctly formatted X-BT-UID property. The value of the X-BT-UID property is equal to the X-BT- UID of the PullvCardEntry. |  |  |


|  | Test Case Name |  |  | Additional Lower Tester Settings |  |  | Additional Pass Verdicts |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Referencing Contacts |  |  |  |  |  |  |  |  |
| PBAP/PSE/PBB/BV-28-C [PSE Return PullvCardEntry with referencing X-BT-UID properties when supported] |  |  | Phonebooks to test: All cch, mch, ich, och, fav, spd virtual folder objects supported by the PSE The Lower Tester’s “Referencing Contacts” PbapSupportedFeatures bit is set The Lower Tester sent a vCardSelector with the X-BT-UID bit set in the PullvCardListing request |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has a correctly formatted X-BT-UID property. |  |  |
| PBAP/PSE/PBB/BV-29-C [PSE Return PullvCardEntry without referencing X-BT-UID properties when not supported] |  |  | Phonebooks to test: All cch, mch, ich, och, fav, spd virtual folder objects supported by the PSE The Lower Tester’s “Referencing Contacts” PbapSupportedFeatures bit is not set The Lower Tester did not sent a vCardSelector in the PullvCardListing request |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The X-BT-UID property is NOT present in the returned vCard. |  |  |
| Default Contact Image Format |  |  |  |  |  |  |  |  |
| PBAP/PSE/PBB/BV-30-C [PSE Return PullvCardEntry with an image when requested] |  |  | Phonebooks to test: All virtual folder objects supported by the PSE PropertySelector = 0x18F (VERSION FN N PHOTO TEL EMAIL) The Lower Tester has the ability to display or evaluate images The Lower Tester sent a vCardSelector with the PHOTO bit set in the PullvCardListing request |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has a correctly formatted contact image. It should be displayed on the Lower Tester and confirmed by the test operator. |  |  |
| PBAP/PSE/PBB/BV-31-C [PSE Return PullvCardEntry without an image when not requested] |  |  | Phonebooks to test: All virtual folder objects supported by the PSE PropertySelector = 0x187 (VERSION FN N TEL EMAIL) The Lower Tester did not sent a vCardSelector in the PullvCardListing request |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). vCards do not contain any images |  |  |
| Speed Dial Folder |  |  |  |  |  |  |  |  |
| PBAP/PSE/PBB/BV-32-C [PSE Return PullvCardEntry with a X-BT-SPEEDDIALKEY property from the spd folder] |  |  | Phonebooks to test: All supported spd virtual folders |  |  | The response(s) is/are successful (response code is 0x90 or 0xA0). The returned vCard has a correctly formatted X-BT- SPEEDDIALKEY property in the response. |  |  |

Table 4.13: Test PullvCardEntry Content test cases

### 4.6 Phone Book Downloading Feature

Verify that the Phone Book Downloading feature can be used successfully.

#### 4.6.1 PCE and PSE Retrieve a Phone Book • Test Purpose

Verify that the PCE can retrieve Phone Books from the PSE. This test may be executed with the IUT being either PCE or PSE.
• Test Case Configuration

|  | Test Case |  |
| --- | --- | --- |
| PBAP/PCE/PDF/BV-01-C [PCE and PSE Retrieve a Phone Book (PCE IUT)] |  |  |
| PBAP/PSE/PDF/BV-01-C [PCE and PSE Retrieve a Phone Book (PSE IUT)] |  |  |

Table 4.14: PCE and PSE Retrieve a Phone Book test cases
• Reference
[1] 5.1
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains at least one non-NULL Phone Book. This non-NULL Phone Book must be of interest for the PCE.
• Test Procedure
The PCE establishes a PBAP session with the PSE and in this session retrieves the Phone Book objects of interest.
• Expected Outcome
Pass verdict
The PCE retrieves all the Phone Book objects of interest from the PSE. The information thus downloaded is accurate. Both the PCE and the PSE are in normal operation mode after the completion of the downloading operation.

#### 4.6.2 PCE and PSE Retrieve a Phone Book • Test Purpose

Verify that the PCE can abort a Phone Book object download from the PSE. This test may be executed with the IUT being either PCE or PSE.
• Test Case Configuration

|  | Test Case |  |
| --- | --- | --- |
| PBAP/PCE/PDF/BV-06-C [PCE and PSE Abort a Phone Book Download (PCE IUT)] |  |  |
| PBAP/PSE/PDF/BV-06-C [PCE and PSE Abort a Phone Book Download (PSE IUT)] |  |  |

Table 4.15: PCE and PSE Retrieve a Phone Book test cases
• Reference
[1] 5.1, 6.1
• Initial Condition
- The PCE and the PSE have been paired and have established a PBAP session.
- The PCE and the PSE have established a PBAP session. The PSE contains at least one non- NULL Phone Book. This non-NULL Phone Book must be large enough to allow the PCE to successfully abort the transfer before completion.
• Test Procedure
1. The PCE sends a Pull Phonebook request to the PSE to retrieve the Phone Book objects of
interest. 2. The PCE initiates the user action to ABORT the Phone Book download before the transfer has
completed.
• Expected Outcome
Pass verdict
The PCE successfully sends the ABORT request to the PSE prior to completion of the Phone Book download.
The PSE processes the ABORT operation correctly and the Phone Book object is not downloaded. Both the PCE and the PSE are in normal operation mode after the downloading operation is aborted.

### 4.7 Phone Book Browsing Feature

Verify that the PCE can efficiently browse Phone Book information in the PSE.

#### 4.7.1 PCE and PSE Search Phone Book entries • Test Purpose

Verify that the PCE can perform a search on the list of Phone Book entries available on the PSE. This test may be executed with the IUT being either PCE or PSE.
• Test Case Configuration

|  | Test Case |  |
| --- | --- | --- |
| PBAP/PCE/PBF/BV-01-C [PCE and PSE Search Phone Book Entries (PCE IUT)] |  |  |
| PBAP/PSE/PBF/BV-01-C [PCE and PSE Search Phone Book Entries (PSE IUT)] |  |  |

Table 4.16: PCE and PSE Search Phone Book entries test cases
• Reference
[1] 5.4
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains at least one non-NULL Phone Book. This non-NULL Phone Book must be of interest for the PCE.
• Test Procedure
The PCE establishes a PBAP session with the PSE and in this session requests a list of vCard entries that satisfy the search criteria of its choice.
• Expected Outcome
Pass verdict
The PCE retrieves the list of entries and all the information delivered corresponds to the search criteria, based on the implementation-specific searching mechanism used on the PSE.

#### 4.7.2 PCE and PSE Retrieve Phone Book entries • Test Purpose

Verify that the PCE can read Phone Book entries on the PSE. This test may be executed with the IUT being either PCE or PSE.
• Test Case Configuration

|  | Test Case |  |
| --- | --- | --- |
| PBAP/PCE/PBF/BV-02-C [PCE and PSE Retrieve Phone Book Entries (PCE IUT)] |  |  |
| PBAP/PSE/PBF/BV-02-C [PCE and PSE Retrieve Phone Book Entries (PSE IUT)] |  |  |

Table 4.17: PCE and PSE Retrieve Phone Book entries test cases
• Reference
[1] 5.3
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains at least one non-NULL Phone Book. This non-NULL Phone Book must be of interest for the PCE.
• Test Procedure
The PCE establishes a PBAP session with the PSE and in this session attempts to browse the content of the PSE.
• Expected Outcome
Pass verdict
The PCE can browse the Phone Book information that is available on the PSE. The information acquired by the PCE is accurate.

#### 4.7.3 PCE and PSE Retrieve Phone Book entries • Test Purpose

Verify that the PCE can abort a vCard-listing object download from the PSE. This test may be executed with the IUT being either PCE or PSE.
• Test Case Configuration

|  | Test Case |  |
| --- | --- | --- |
| PBAP/PCE/PBF/BV-03-C [PCE and PSE Abort a Phone Book Listing Request (PCE IUT)] |  |  |
| PBAP/PSE/PBF/BV-03-C [PCE and PSE Abort a Phone Book Listing Request (PSE IUT)] |  |  |

Table 4.18: PCE and PSE Retrieve Phone Book entries test cases
• Reference
[1] 5.1, 6.1
• Initial Condition
- The PCE and the PSE have been paired and have established a PBAP session.
- The PCE and the PSE have established a PBAP session. The PSE contains at least one non- NULL Phone Book. This non-NULL Phone Book must be large enough to allow the PCE to successfully abort the transfer before completion.
• Test Procedure
1. The PCE sends a Pull vCardListing request to the PSE to retrieve the Phone Book listing objects
of interest. 2. The PCE initiates the user action to ABORT the Phone Book download before the transfer has
completed.
• Expected Outcome
Pass verdict
The PCE successfully sends the ABORT request to the PSE prior to completion of the Phone Book vCard-listing object download.
The PSE processes the ABORT operation correctly and the vCard-listing object is not downloaded. Both the PCE and the PSE are in normal operation mode after the downloading operation is aborted and the PBAP session is sustained.

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.
The columns for the TCMT are defined as follows:
Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for the Phone Book Access Profile (PBAP) [4].
If a test case is mandatory within the respective layer, then the y/x reference is omitted.
Feature: A brief, informal description of the feature being tested.
Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [3].
For the purpose and structure of the ICS/IXIT, refer to [3].

|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PBAP 1/1 |  |  | Authentication request and SDP Record |  |  | PBAP/PCE/SSM/BV-06-C PBAP/PCE/SGSIT/SERR/BV-01-C PBAP/PCE/SGSIT/OFFS/BV-01-C PBAP/PCE/CGSIT/SFC/BV-01-C |  |  |
| PBAP 1/1 AND PBAP 2a/2 |  |  | PBAP PCE SDP Service, PBAP 1.1 |  |  | PBAP/PCE/SGSIT/ATTR/BV-01-C |  |  |
| PBAP 1/1 AND PBAP 2a/3 |  |  | PBAP PCE SDP Service, PBAP 1.2 |  |  | PBAP/PCE/SGSIT/ATTR/BV-02-C |  |  |
| PBAP 1/2 |  |  | Authentication request and SDP Record |  |  | PBAP/PSE/SSM/BV-07-C PBAP/PSE/SGSIT/SERR/BV-01-C PBAP/PSE/SGSIT/ATTR/BV-01-C PBAP/PSE/SGSIT/ATTR/BV-04-C PBAP/PSE/SGSIT/OFFS/BV-01-C |  |  |
| PBAP 1/2 AND PBAP 9a/2 |  |  | PBAP PSE SDP Service, PBAP 1.1 |  |  | PBAP/PSE/SGSIT/ATTR/BV-02-C |  |  |
| PBAP 1/2 AND PBAP 9a/3 |  |  | PBAP PSE SDP Service, PBAP 1.2 |  |  | PBAP/PSE/SGSIT/ATTR/BV-03-C |  |  |
| PBAP 1/2 AND NOT PBAP 9a/2 |  |  | PBAP PSE SDP attribute – PBAPSupportedFeatures |  |  | PBAP/PSE/SGSIT/ATTR/BV-06-C |  |  |
| PBAP 26/1 |  |  | PBAP PSE SDP attribute – GoepL2CapPsm |  |  | PBAP/PSE/SGSIT/ATTR/BV-05-C |  |  |
| PBAP 2/1 |  |  | Phone Book Download |  |  | PBAP/PCE/PBD/BV-01-C |  |  |
| PBAP 2/1 AND PBAP 2/9 |  |  | Phone Book Download : X-BT-UCI vCard Property |  |  | PBAP/PCE/PBD/BV-38-C PBAP/PCE/PBD/BV-39-C |  |  |
| PBAP 2/1 AND PBAP 2/10 |  |  | Phone Book Download : X-BT-UID vCard Property |  |  | PBAP/PCE/PBD/BV-40-C PBAP/PCE/PBD/BV-41-C |  |  |
| PBAP 2/1 AND PBAP 2/8a |  |  | Phone Book Download : Enhanced Missed Calls |  |  | PBAP/PCE/PBD/BV-42-C PBAP/PCE/PBD/BV-43-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PBAP 2/1 AND PBAP 2/7a |  |  | Phone Book Download : vCard Selecting |  |  | PBAP/PCE/PBD/BV-44-C PBAP/PCE/PBD/BV-46-C |  |  |
| PBAP 2/1 AND PBAP 2/7b |  |  | Phone Book Download : vCard Selecting |  |  | PBAP/PCE/PBD/BV-45-C |  |  |
| PBAP 2/1 AND PBAP 2/12a |  |  | Phone Book Download : Default Contact Image Format |  |  | PBAP/PCE/PBD/BV-47-C PBAP/PCE/PBD/BV-48-C |  |  |
| PBAP 2/1 |  |  | Phone Book Download |  |  | PBAP/PCE/PDF/BV-01-C |  |  |
| PBAP 9/1 |  |  | Phone Book Download |  |  | PBAP/PSE/PDF/BV-01-C |  |  |
| PBAP 2/1 AND PBAP 6/4 |  |  | Abort Phone Book Download |  |  | PBAP/PCE/PDF/BV-06-C |  |  |
| PBAP 9/1 |  |  | Abort Phone Book Download |  |  | PBAP/PSE/PDF/BV-06-C |  |  |
| PBAP 2/2 AND PBAP 2/4 |  |  | Phone Book Browsing |  |  | PBAP/PCE/PBB/BV-01-C PBAP/PCE/PBB/BV-02-C PBAP/PCE/PBB/BV-03-C PBAP/PCE/PBB/BV-05-C |  |  |
| PBAP 2/2 AND PBAP 2/8a |  |  | Phone Book Browsing: Enhanced Missed Calls |  |  | PBAP/PCE/PBB/BV-39-C PBAP/PCE/PBB/BV-40-C |  |  |
| PBAP 2/2 AND PBAP 2/7a |  |  | Phone Book Browsing: vCard Selecting |  |  | PBAP/PCE/PBB/BV-41-C PBAP/PCE/PBB/BV-42-C |  |  |
| PBAP 2/2 AND PBAP 2/9 |  |  | Phone Book Browsing: X-BT-UCI vCard Property |  |  | PBAP/PCE/PBB/BV-33-C PBAP/PCE/PBB/BV-34-C |  |  |
| PBAP 2/2 AND PBAP 2/10 |  |  | Phone Book Browsing: X-BT-UID vCard Property |  |  | PBAP/PCE/PBB/BV-35-C PBAP/PCE/PBB/BV-36-C PBAP/PCE/PBB/BV-43-C |  |  |
| PBAP 9/2 AND PBAP 9/10 |  |  | Phone Book Browsing: X-BT-UID vCard Property |  |  | PBAP/PSE/PBB/BV-44-C PBAP/PSE/PBB/BV-45-C PBAP/PSE/PBB/BV-46-C |  |  |
| PBAP 2/2 AND PBAP 2/12a |  |  | Phone Book Browsing: Default Contact Image Format |  |  | PBAP/PCE/PBB/BV-37-C PBAP/PCE/PBB/BV-38-C |  |  |
| PBAP 2/2 AND PBAP 2/14 AND PBAP 2/14a |  |  | Phone Book Browsing: Searching |  |  | PBAP/PCE/PBF/BV-01-C |  |  |
| PBAP 9/2 |  |  | Phone Book Browsing: Searching |  |  | PBAP/PSE/PBF/BV-01-C |  |  |
| PBAP 2/2 |  |  | Phone Book Browsing |  |  | PBAP/PCE/PBF/BV-02-C |  |  |
| PBAP 9/2 |  |  | Phone Book Browsing |  |  | PBAP/PSE/PBF/BV-02-C |  |  |
| PBAP 4/2 AND PBAP 6/4 |  |  | Abort Phone Book Listing Request |  |  | PBAP/PCE/PBF/BV-03-C |  |  |
| PBAP 9/2 |  |  | Abort Phone Book Listing Request |  |  | PBAP/PSE/PBF/BV-03-C |  |  |
| PBAP 2/4 |  |  | Phone Book Download |  |  | PBAP/PCE/PBD/BV-04-C |  |  |
| PBAP 2/3 |  |  | Session Management |  |  | PBAP/PCE/SSM/BV-01-C PBAP/PCE/SSM/BV-02-C |  |  |
| PBAP 2a/3 AND PBAP 1/1 |  |  | PbapSupportedFeatures bits |  |  | PBAP/PCE/SSM/BV-09-C PBAP/PCE/SSM/BV-10-C |  |  |
| PBAP 6/6 |  |  | OBEX authentication initiation |  |  | PBAP/PCE/SSM/BI-01-C PBAP/PCE/SSM/BV-08-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PBAP 13/6 |  |  | OBEX authentication initiation |  |  | PBAP/PSE/SSM/BI-03-C |  |  |
| PBAP 1/2 |  |  | Authentication Request |  |  | PBAP/PSE/SSM/BV-08-C |  |  |
| PBAP 9/1 |  |  | Phone Book Download |  |  | PBAP/PSE/PBD/BV-02-C PBAP/PSE/PBD/BV-03-C PBAP/PSE/PBD/BI-01-C |  |  |
| PBAP 9/1 AND PBAP 10/2 |  |  | Phone Book Download – NewMissedCalls |  |  | PBAP/PSE/PBD/BV-05-C |  |  |
| PBAP 9/5a |  |  | Phone Book Download : Persistent Database Identifier |  |  | PBAP/PSE/PBD/BV-06-C |  |  |
| PBAP 9/5b |  |  | Phone Book Download : Regenerated Database Identifier |  |  | PBAP/PSE/PBD/BV-07-C |  |  |
| PBAP 9/6b |  |  | Phone Book Download : Folder Version – Property Change 1 |  |  | PBAP/PSE/PBD/BV-08-C |  |  |
| PBAP 9/6c |  |  | Phone Book Download : Folder Version – Property Change 2 |  |  | PBAP/PSE/PBD/BV-09-C |  |  |
| PBAP 9/6a |  |  | Phone Book Download : Folder Version – Delete/Insert |  |  | PBAP/PSE/PBD/BV-10-C |  |  |
| PBAP 9/1 |  |  | Phone Book Download: Object Size |  |  | PBAP/PSE/PBD/BV-17-C |  |  |
| PBAP 9/1 AND PBAP 9/8 |  |  | Phone Book Download: Enhanced Missed Calls |  |  | PBAP/PSE/PBD/BV-18-C PBAP/PSE/PBD/BV-19-C PBAP/PSE/PBD/BV-20-C PBAP/PSE/PBD/BV-21-C |  |  |
| PBAP 9/1 AND PBAP 9/8 AND PBAP 9/7 |  |  | Phone Book Download: Enhanced Missed Calls + vCardSelector |  |  | PBAP/PSE/PBD/BV-22-C PBAP/PSE/PBD/BV-23-C |  |  |
| PBAP 9/1 AND PBAP 9/7 |  |  | Phone Book Download: vCardSelector |  |  | PBAP/PSE/PBD/BV-24-C PBAP/PSE/PBD/BV-25-C PBAP/PSE/PBD/BV-26-C PBAP/PSE/PBD/BV-27-C PBAP/PSE/PBD/BV-28-C |  |  |
| PBAP 9/1 AND PBAP 9/9 |  |  | Phone Book Download: X-BT-UCI vCard Property |  |  | PBAP/PSE/PBD/BV-29-C PBAP/PSE/PBD/BV-30-C |  |  |
| PBAP 9/1 AND PBAP 9/10 |  |  | Phone Book Download: X-BT-UID vCard Property |  |  | PBAP/PSE/PBD/BV-31-C PBAP/PSE/PBD/BV-32-C |  |  |
| PBAP 9/1 AND PBAP 9/10a |  |  | Phone Book Download: Referencing Contacts |  |  | PBAP/PSE/PBD/BV-33-C PBAP/PSE/PBD/BV-34-C |  |  |
| PBAP 9/1 AND PBAP 9/12a |  |  | Phone Book Download: Default Contact Image Format |  |  | PBAP/PSE/PBD/BV-35-C |  |  |
| PBAP 9/1 |  |  | Phone Book Download: Default Contact Image Format |  |  | PBAP/PSE/PBD/BV-36-C |  |  |
| PBAP 9/1 AND PBAP 9/13f |  |  | Phone Book Download: Speed Dial Folder |  |  | PBAP/PSE/PBD/BV-37-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PBAP 9/2 |  |  | Phone Book Browsing |  |  | PBAP/PSE/PBB/BI-01-C PBAP/PSE/PBB/BI-07-C PBAP/PSE/PBB/BV-06-C PBAP/PSE/PBB/BV-07-C PBAP/PSE/PBB/BV-08-C PBAP/PSE/PBB/BV-09-C PBAP/PSE/PBB/BV-10-C |  |  |
| PBAP 9/2 |  |  | Phone Book Browsing – NewMissedCalls |  |  | PBAP/PSE/PBB/BV-11-C |  |  |
| PBAP 9/2 |  |  | Phone Book Browsing: vCard-listing Size |  |  | PBAP/PSE/PBB/BV-12-C |  |  |
| PBAP 9/2 AND PBAP 9/8 |  |  | Phone Book Browsing: Enhanced Missed Calls |  |  | PBAP/PSE/PBB/BV-13-C PBAP/PSE/PBB/BV-14-C PBAP/PSE/PBB/BV-15-C PBAP/PSE/PBB/BV-16-C |  |  |
| PBAP 9/2 AND PBAP 9/8 AND PBAP 9/7 |  |  | Phone Book Browsing: Enhanced Missed Calls + vCardSelector |  |  | PBAP/PSE/PBB/BV-17-C PBAP/PSE/PBB/BV-18-C |  |  |
| PBAP 9/2 AND PBAP 9/7 |  |  | Phone Book Browsing: vCardSelector |  |  | PBAP/PSE/PBB/BV-19-C PBAP/PSE/PBB/BV-20-C PBAP/PSE/PBB/BV-21-C PBAP/PSE/PBB/BV-22-C PBAP/PSE/PBB/BV-23-C |  |  |
| PBAP 9/2 AND PBAP 9/9 |  |  | Phone Book Browsing: X-BT-UCI vCard Property |  |  | PBAP/PSE/PBB/BV-24-C PBAP/PSE/PBB/BV-25-C |  |  |
| PBAP 9/2 AND PBAP 9/10 |  |  | Phone Book Browsing: X-BT-UID vCard Property |  |  | PBAP/PSE/PBB/BV-26-C PBAP/PSE/PBB/BV-27-C |  |  |
| PBAP 9/2 AND PBAP 9/10a |  |  | Phone Book Browsing: Referencing Contacts |  |  | PBAP/PSE/PBB/BV-28-C PBAP/PSE/PBB/BV-29-C |  |  |
| PBAP 9/2 AND PBAP 9/12a |  |  | Phone Book Browsing: Default Contact Image Format |  |  | PBAP/PSE/PBB/BV-30-C |  |  |
| PBAP 9/2 |  |  | Phone Book Browsing: Default Contact Image Format |  |  | PBAP/PSE/PBB/BV-31-C |  |  |
| PBAP 9/2 AND PBAP 9/13f |  |  | Phone Book Browsing: Speed Dial Folder |  |  | PBAP/PSE/PBB/BV-32-C |  |  |
| PBAP 9/3 |  |  | Session Management |  |  | PBAP/PSE/SSM/BV-03-C PBAP/PSE/SSM/BV-05-C PBAP/PSE/SSM/BI-02-C |  |  |
| PBAP 9a/3 AND PBAP 1/2 |  |  | PbapSupportedFeatures bits |  |  | PBAP/PSE/SSM/BV-11-C |  |  |
| PBAP 24/1 |  |  | Retrieve large phone book - PCE |  |  | PBAP/PCE/PDF/BV-02-C |  |  |
| PBAP 24/2 |  |  | Transfer Large Phone Book - PSE |  |  | PBAP/PSE/PDF/BV-03-C |  |  |
| PBAP 24/3 |  |  | Retrieve empty phone book - PCE |  |  | PBAP/PCE/PDF/BV-04-C |  |  |
| PBAP 24/4 |  |  | Transfer empty Phone Book - PSE |  |  | PBAP/PSE/PDF/BV-05-C |  |  |
| PBAP 24/5 |  |  | Return Phonebook – Limit number of entries |  |  | PBAP/PSE/PBD/BV-11-C |  |  |


|  | Item |  |  | Feature |  |  | Test Case(s) |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PBAP 24/6 |  |  | Return vCard listing – Limit number of entries |  |  | PBAP/PSE/PBD/BV-12-C |  |  |
| PBAP 24/7 AND PBAP 10/2 |  |  | Phone Book Order |  |  | PBAP/PSE/PBD/BV-13-C |  |  |
| PBAP 24/8 |  |  | Call stack timestamps – PSE |  |  | PBAP/PSE/PBD/BV-14-C |  |  |
| PBAP 24/9 |  |  | No User Interaction – PSE |  |  | PBAP/PSE/PBD/BV-15-C |  |  |
| PBAP 24/10 |  |  | Special Character Handling – PSE |  |  | PBAP/PSE/PBD/BV-16-C |  |  |
| PBAP 26/2 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Legacy Get |  |  | PBAP/PSE/GOEP/BC/BV-03-C |  |  |
| PBAP 25/2 AND PBAP 1/1 |  |  | GOEP 2.0 or later: Legacy Get |  |  | PBAP/PCE/GOEP/BC/BV-04-C |  |  |
| PBAP 25/1 AND PBAP 1/1 |  |  | GOEP 2.0 or later: Issue Connect |  |  | PBAP/PCE/GOEP/CON/BV-01-C |  |  |
| PBAP 25/4 AND PBAP 1/1 |  |  | GOEP 2.0 or later: GET server no SRM |  |  | PBAP/PCE/GOEP/SRM/BV-05-C |  |  |
| PBAP 25/4 AND PBAP 1/1 |  |  | GOEP 2.0 or later: Send GET with SRM |  |  | PBAP/PCE/GOEP/SRM/BV-07-C |  |  |
| PBAP 26/4 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Receive GET with SRM |  |  | PBAP/PSE/GOEP/SRM/BV-08-C |  |  |
| PBAP 26/4 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Receive invalid connect with SRM |  |  | PBAP/PSE/GOEP/SRM/BI-03-C |  |  |
| PBAP 26/4 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Receive GET with invalid SRM |  |  | PBAP/PSE/GOEP/SRM/BI-05-C |  |  |
| PBAP 26/6 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Receive GET with SRMP |  |  | PBAP/PSE/GOEP/SRMP/BV-02-C |  |  |
| PBAP 25/5 AND PBAP 1/1 |  |  | GOEP 2.0 or later: Send GET with SRMP |  |  | PBAP/PCE/GOEP/SRMP/BV-04-C |  |  |
| PBAP 25/5 AND PBAP 1/1 |  |  | GOEP 2.0 or later: Send GET with SRMP |  |  | PBAP/PCE/GOEP/SRMP/BV-05-C |  |  |
| PBAP 25/6 AND PBAP 1/1 |  |  | GOEP 2.0 or later: Receive GET response with SRMP |  |  | PBAP/PCE/GOEP/SRMP/BV-06-C |  |  |
| PBAP 25/6 AND PBAP 1/1 |  |  | GOEP 2.0 or later: GET response with invalid SRMP |  |  | PBAP/PCE/GOEP/SRMP/BI-01-C |  |  |
| PBAP 26/6 AND PBAP 1/2 |  |  | GOEP 2.0 or later: GET request with invalid SRMP |  |  | PBAP/PSE/GOEP/SRMP/BI-02-C |  |  |
| PBAP 26/1 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Reject Action |  |  | PBAP/PSE/GOEP/ROB/BV-01-C |  |  |
| PBAP 26/1 AND PBAP 1/2 |  |  | GOEP 2.0 or later: Reject Reliable Sessions |  |  | PBAP/PSE/GOEP/ROB/BV-02-C |  |  |

Table 5.1: Test case mapping

## 6 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | 1.0.0 |  |  | 2006-03-15 | Publication date |
|  |  |  | 1.0.1r0 |  |  | 2006-11-13 | Add “Conformance” section. TSE1818: PBAP/PCE/SSM/BI-01-C (legacy test case ID TP/SSM/BI-1-C): Change Pass verdict TSE 1926: PBAP/PSE/PBB/BV-09-C (legacy test case ID TP/PBB/BV-9-C): New test case TSE 1828: PBAP/PCE/PBB/BV-05-C (legacy test case ID TP/PBB/BV-5-C) move to different row in TCMT TSE 1839: TP/PBB/BV-4-C: Change pass verdict TSE 1945: New test cases PBAP/PSE/SSM/BI-03-C, PBAP/PCE/SSM/BV-06-C, PBAP/PSE/SSM/BV-07-C (legacy test case IDs TP/SSM/BI-3-C, TP/SSM/ BV-6-C, TP/SSM/BV-7-C). Added rows to TCMT for these. TSE 1963: Corrections to TP/PBB/BV-4-C: change Phonebook to vCard TSE 1964: Move PBAP/PCE/PBB/BV-05-C (legacy test case ID TP/PBB/BV-5-C) to 3-1/2 row in TCMT. TSE 1965: Add “not” to Fail Verdict for TP/PBB/BV-4- C |
|  |  |  | 1.0.1r1, r2 |  |  | 2006-12-04 | TSE 1829: PBAP/PCE/SSM/BI-01-C (legacy test case ID TP/SSM/BI-1-C): Change test procedure TSE 1945: Change wording to PBAP/PSE/SSM/BI-03- C and PBAP/PCE/SSM/BV-06-C (legacy test case IDs TP/SSM/BI-3-C and TP/SSM/BV-06-C) according to TSE comment of 2006-11-16 TSE 1979: Change TCMT table numbers to match the new ICS table numbers |
| 1 |  |  | 1.0.1 |  |  | 2007-01-10 | Prepare for publication. |
| 2 |  |  | 1.0.2 |  |  | 2007-07-31 | TSE 2117: PBAP/PSE/PBD/BV-02-C , PBAP/PSE/PBD/BV-03-C , PBAP/PSE/PBB/BV-08-C (legacy test case IDs TP/PBD/BV-02-C, TP/PBD/BV- 03-C, TP/PBB/BV-8-C) TSE 2125: PBAP/PCE/PBB/BV-05-C (legacy test case ID TP/PBB/BV-5-C) TSE 2059: fixed by TSE 1963 TSE 2240 Remove TP/SSM/BV-4-C TSE 2241: PBAP/PSE/PBB/BV-10-C (legacy test case ID TP/PBB/BV-10-C): fix init. Condition, procedure TSE 2258: TSE PBAP/PSE/SSM/BI-03-C (legacy test case ID TP/SSM-BI-3): Fix pass verdict TSE 2029: PBAP/PCE/SSM/BV-01-C (legacy test case ID TP/SSM/BV-1-C), changes. New test case PBAP/PCE/SSM/BV-08-C (legacy test case ID TP/SSM/BV-8-C), TCMT |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TSE 1981: PBAP/PSE/PBB/BV-08-C (legacy test case ID TP/PBB/BV-8-C); Fix Reference # TSE 2266: PBAP/PSE/SSM/BV-07-C (legacy test case ID TP/SSM/BV-7-C): update pass/fail verdicts TSE 2257/2258: PBAP/PSE/SSM/BI-03-C (legacy test case ID TP/SSM/BI-3-C): fix Pass Verdict |
|  |  |  | 1.0.3r0 |  |  | 2008 02 | TSE 2371: PBAP/PSE/SSM/BI-03-C (legacy test case ID TP/SSM/BI-3-C): Change Pass verdict TSE 2408: PBAP/PCE/SSM/BV-06-C, PBAP/PCE/SSM/BV-08-C (legacy test case IDs TP/SSM/BV-6-C, TP/SSM/BV-8-C): relocate to PCE section. |
|  |  |  | 1.0.3r1 |  |  | 2008-03 | Input reviewer’s comments |
| 3 |  |  | 1.0.3 |  |  | 2008-04 | Prepare for publication. |
|  |  |  | 1.0.4r0 |  |  | 2008-09 | TSE 2521: New test case PBAP/PSE/SSM/BV-08-I (legacy test case ID TP/SSM/BV-8-1) TSE 2694: PBAP/PCE/PBB/BV-03-C (legacy test case ID TP/PBB/BV-3-C): Move to PCE Download section, change command name in Pass and Fail verdicts TSE 2695: PBAP/PCE/PBB/BV-02-C (legacy test case ID TP/PBB/BV-2-C) updates, Remove TP/PBB/BV-4-C |
| 4 |  |  | 1.0.4 |  |  | 2008-12-04 | Prepare for publication. |
|  |  |  | 1.0.5r0 |  |  | 2009-04-29 | TSE 2699 : New test case: PBAP/PCE/PBD/BV-04-C (legacy test case ID TP/PBD/BV-4-C) TSE 2892: New test case PBAP/PSE/PBB/BI-07-C (legacy test case ID TP/PBB/BI-7-C) |
| 5 |  |  | 1.0.5 |  |  | 2009-08-10 | Prepare for publication. |
|  |  |  | 1.0.6r0 |  |  | 2010-08-09 | Update Conformance section |
|  |  |  | 1.0.7r0 |  |  | 2010-11-12 | TSE 3647: PBAP/PSE/SSM/BV-08-I (legacy test case ID TP/SSM/BV-8-I): Change Pass verdict TSE 3936: PBAP/PCE/PBD/BV-04-C (legacy test case ID TP/PBD/BV-4-C): TCMT |
|  |  |  | 1.0.7r1 |  |  | 2011-01-04 | TSE 3936: Moved from PSE to PCE per reviewer’s comments. |
| 6 |  |  | 1.0.7 |  |  | 2011-07-21 | Prepare for publication. |
|  |  |  | 1.0.8r0 |  |  | 2011-11-11 | TSE 4470: Two new test cases PBAP/PSE/PBF/BV- 03-I, PBAP/PCE/PBF/BV-03-I, PBAP/PSE/PDF/BV- 06-I, PBAP/PCE/PDF/BV-06-I (legacy test case ID TP/PBF/BV-3-I, TP/PDF/BV-6-I); update TCMT TSE 4507: PBAP/PCE/PBB/BV-01-C, PBAP/PCE/PBB/BV-02-C, PBAP/PCE/PBB/BV-03-C, PBAP/PCE/PBB/BV-05-C (legacy test case IDs TP/PBB/BV-1-C, TP/PBB/BV-2-C, TP/PBB/BV-3-C, TP/PBB/BV-5-C): update TCMT |
|  |  |  | 1.1.8r1 |  |  | 2012-02-01 | Change document name. Updated title page for publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.1.8r2 |  |  | 2012-02-20 | TSE 4685: PBAP Addendum 1.8.0 merged and TCMT updated |
| 7 |  |  | 1.1.8 |  |  | 2012-03-30 | Prepare for publication. |
|  |  |  | 1.1.9r0 |  |  | 2012-05-20 | TSE 4589: PBAP/PCE/PBD/BV-04-C (legacy test case ID TP/PBD/BV-4-C): change Reference number |
| 8 |  |  | 1.1.9 |  |  | 2012-07-24 | Prepare for publication. |
|  |  |  | 1.1.10r1 |  |  | 2012-09-05 | TSE 4871: Changes to Fail Verdict description in PBAP/PSE/PDF/BV-06-I, PBAP/PCE/PDF/BV-06-I (legacy test case IDTP/PDF/BV-6-I) |
| 9 |  |  | 1.1.10 |  |  | 2012-11-2 | Prepare for Publication |
|  |  |  | 1.1.11r1 |  |  | 2013-05-24 | TSE 4702: Added two new test cases, PBAP/PSE/PBD/BV-05-C and PBAP/PSE/PBB/BV- 11-C (legacy test case IDs TP/PBD/BV-5-C and TP/PBB/BV-11-C), added to TCMT. |
|  |  |  | 1.1.11r2 |  |  | 2013-05-28 | Removed PBAP/PSE/PBB/BV-14-C (legacy test case ID TP/PBB/BV-14-C) from Figure 3.1 TSS. Added new tests to the TSS, PBAP/PSE/PBD/BV-05- C and PBAP/PSE/PBB/BV-11-C (legacy test case IDs TP/PBD/BV-5-C and TP/PPB/BV-11-C). Revised redundant initial conditions. Consistency on terms “PullPhoneBook”, “Lower Tester”, “MaxListCount” etc. Removed all N/A sections for Notes and Test Conditions. |
| 10 |  |  | 1.1.11 |  |  | 2013-07-02 | Prepare for Publication |
|  |  |  | 1.2.0r0 |  |  | 2013-04-26 | Initial updates for PBAPII features |
|  |  |  | 1.2.0r1 |  |  | 2013-04-30 | Added PSE PullPhoneBook Tests |
|  |  |  | 1.2.0r2 |  |  | 2013-05-01 | Added PCE PullPhoneBook Tests |
|  |  |  | 1.2.0r3 |  |  | 2013-05-02 | Updated test requirements (Section 3.3.4) |
|  |  |  | 1.2.0r4 |  |  | 2013-05-03 | Added PullvCardEntry and PullvCardListing |
|  |  |  | 1.2.0r5 |  |  | 2013-05-05 | Mapped TCMT, included GOEP2.0 or later TPs. |
|  |  |  | 1.2.0r8 |  |  | 2013-05-24 | Renumbering test cases, TCMT fixes, and hundreds of minor editorial fixes |
|  |  |  | 1.2.0r9 |  |  | 2013-06-26 | Addressed comments from UPF45 F2F Added missing test cases for PullvCardEntry Replaces all occurences of the terms field and attribute in regards to vCards by property |
|  |  |  | 1.20r10 |  |  | 2013-08-09 | Updated versions. PBAPII is now targeted as v1.2. |
|  |  |  | 1.20r12 |  |  | 2013-10-03 | Fixed Minor Typos and text inconsistencies. |
| 11 |  |  | 1.2.0 |  |  | 2013-11-05 | Adopted by BoD |
|  |  |  | 1.2.1r01 |  |  | 2013-12-03 | TSE 5385: Update to Test Procedure and Pass Verdict for PBAP/PCE/SSM/BV-06-C (legacy test case ID TP/SSM/BV-6-C) |
| 12 |  |  | 1.2.1 |  |  | 2013-11-05 | Prepare for Publication |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.2.2r00 |  |  | 2014-06-16 | TSE 5404: Updated test objectives and descriptions for PBAP/PSE/PDF/BV-01-I, PBAP/PCE/PDF/BV-01-I, PBAP/PSE/PDF/BV-06-I, PBAP/PCE/PDF/BV-06-I, PBAP/PSE/PBF/BV-01-I, PBAP/PCE/PBF/BV-01-I, PBAP/PSE/PBF/BV-02-I, PBAP/PCE/PBF/BV-02-I, PBAP/PSE/PBF/BV-03-I, PBAP/PCE/PBF/BV-03-I (legacy test case IDs TP/PDF/BV-01-I, TP/PDF-BV- 06-I, TP/PBF/BV-01-I, TP/PBF/BV-02-I, and TP/PBF/BV-03-I). Added "OR 9/1" to TCMT mappings for PBAP/PSE/PDF/BV-06-I, PBAP/PCE/PDF/BV-06-I, PBAP/PSE/PBF/BV-03-I, PBAP/PCE/PBF/BV-03-I (legacy test case IDs TP/PDF-BV-06-I and TP/PBF/BV-03-I). TSE 5493: Updated the TCMT entries for PBAP/PCE/PDF/BV-02-I, PBAP/PSE/PDF/BV-03-I, PBAP/PCE/PDF/BV-04-I, PBAP/PSE/PDF/BV-05-I, PBAP/PSE/PBD/BV-11-C, PBAP/PSE/PBD/BV-12-C, PBAP/PSE/PBD/BV-13-C, PBAP/PSE/PBD/BV-14-C, PBAP/PSE/PBD/BV-15-C, PBAP/PSE/PBD/BV-16-C (legacy test case IDs TP/PDF/BV-02-I, TP/PDF/BV- 03-I, TP/PDF/BV-04-I, TP/PDF/BV-05-I, TP/PBD/BV- 11-C, TP/PBF/BV-12-C, TP/PBF/BV-13-C, TP/PBF/BV-14-C, TP/PBF/BV-15-C, and TP/PBF/BV- 16-C) from table 25 to table 24. TSE 5496: Updated TCMT mapping for PBAP/PSE/SSM/BV-11-C (legacy test case ID TP/SSM/BV-11-C) from "AND 1/1" to "AND 1/2". TSE 5504: Added leading zeroes to TC IDs containing numbers under 10, PBAP/PCE/SSM/BV-01-C , PBAP/PCE/SSM/BV-02-C, PBAP/PCE/SSM/BI-01-C, PBAP/PSE/SSM/BV-03-C, PBAP/PSE/SSM/BV-05-C, PBAP/PCE/SSM/BV-06-C, PBAP/PSE/SSM/BV-07-C, PBAP/PCE/SSM/BV-08-C, PBAP/PSE/SSM/BI-02-C, PBAP/PSE/SSM/BI-03-C, PBAP/PCE/PBD/BV-01-C, PBAP/PSE/PBD/BV-02-C, PBAP/PSE/PBD/BV-03-C, PBAP/PCE/PBD/BV-04-C, PBAP/PSE/PBD/BV-05-C, PBAP/PSE/PBD/BI-01-C, PBAP/PCE/PBB/BV-01-C, PBAP/PCE/PBB/BV-02-C, PBAP/PCE/PBB/BV-03-C, PBAP/PCE/PBB/BV-05-C, PBAP/PSE/PBB/BV-06-C, PBAP/PSE/PBB/BV-07-C, PBAP/PSE/PBB/BV-08-C, PBAP/PSE/PBB/BV-09-C, PBAP/PSE/PBB/BI-01-C, PBAP/PSE/PBB/BI-07-C, PBAP/PSE/PDF/BV-01-I, PBAP/PCE/PDF/BV-01-I, PBAP/PSE/PBF/BV-01-I, PBAP/PCE/PBF/BV-01-I, PBAP/PSE/SSM/BV-08-I, PBAP/PSE/PBF/BV-02-I, PBAP/PCE/PBF/BV-02-I, PBAP/PSE/PBF/BV-03-I, PBAP/PCE/PBF/BV-03-I, PBAP/PSE/PDF/BV-06-I, PBAP/PCE/PDF/BV-06-I, PBAP/PCE/SSM/BV-09-C, PBAP/PSE/PBD/BV-06-C, PBAP/PSE/PBD/BV-07-C, PBAP/PSE/PBD/BV-08-C, PBAP/PSE/PBD/BV-09-C (legacy test case IDs TP/SSM/BV-1-C, TP/SSM/BV-2-C, TP/SSM/BI-1-C, TP/SSM/BV-3-C, TP/SSM/BV-5-C, TP/SSM/BV-6-C, TP/SSM/BV-7-C, TP/SSM/BV-8-C, TP/SSM/BI-2-C, TP/SSM/BI-3-C, TP/PBD/BV-1-C, TP/PBD/BV-2-C, TP/PBD/BV-3-C, TP/PBD/BV-4-C, TP/PBD/BV-5-C, |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  |  |  |  |  | TP/PBD/BI-1-C, TP/PBB/BV-1-C, TP/PBB/BV-2-C, TP/PBB/BV-3-C, TP/PBB/BV-5-C, TP/PBB/BV-6-C, TP/PBB/BV-7-C, TP/PBB/BV-8-C, TP/PBB/BV-9-C, TP/PBB/BI-1-C, TP/PBB/BI-7-C, TP/PDF/BV-1-I, TP/PBF/BV-1-I, TP/SSM/BV-8-I, TP/PBF/BV-2-I, TP/PBF/BV-3-I, TP/PDF/BV-6-I, TP/SSM/BV-9-C, TP/PBD/BV-6-C, TP/PBD/BV-7-C, TP/PBD/BV-8-C, TP/PBD/BV-9-C). |
|  |  |  | 1.2.2r01 |  |  | 2014-06-18 | BTI Review, Nerissa: Added clarifications to test cases changes in TSE 5404 to make procedures role- neutral. |
|  |  |  | 1.2.2r02 |  |  | 2014-06-24 | BQRB Review, Alicia: rejected Nerissa’s comments and filed TSE 5768 to address the issues instead. TE Review: Legal Review preparations |
| 13 |  |  | 1.2.2 |  |  | 2014-07-07 | Publication |
|  |  |  | 1.2.3r00 |  |  | 2014-10-25 | TSE 5655: Updated TCMT mapping for PBAP/PCE/SSM/BV-09-C , PBAP/PCE/SSM/BV-10- C, PBAP/PSE/SSM/BV-11-C (legacy test case IDs TP/SSM/BV-09-C, TP/SSM/BV-10-C, and TP/SSM/BV-11-C). |
|  |  |  | 1.2.3r02 |  |  | 2014-11-25 | Corrected Stephen’s company name. |
| 14 |  |  | 1.2.3 |  |  | 2014-12-08 | Prepared for TCRL 2014-2 publication |
|  |  |  | 1.2.4r00 |  |  | 2015-04-29 | TSE 5864: Revised pass verdict and TCMT for PBAP/PSE/PBF/BV-01-I, PBAP/PCE/PBF/BV-01-I (legacy test case ID TP/PBF/BV-01-I) |
| 15 |  |  | 1.2.4 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 1.2.1.0r00 |  |  | 2015-11-23 | Updated version numbering to align with Specification version change from 1.2 to 1.2.1 for ESR09. With the specification taking a third identifying number, the TS version identifier moves to the fourth number and starts again at 0. |
| 16 |  |  | 1.2.1.0 |  |  | 2015-12-22 | Prepared for TCRL 2015-2 publication |
|  |  |  | 1.2.1.1r00 |  |  | 2016-08-31 | Converted to new Test Case ID conventions as defined in TSTO v4.1 |
|  |  |  | 1.2.1.1r01 |  |  | 2016-10-13 | TSE 7559: Change "PrimaryVersionCounter" and "SecondaryVersionCounter" in sections 3.4.2.10, 3.4.2.11, & 3.5.2.9 to use "PrimaryFolderVersion" and "SecondaryFolderVersion". |
|  |  |  | 1.2.1.1r02 |  |  | 2016/10/27 | Updated template |
| 17 |  |  | 1.2.1.1 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 1.2.1.2r00– r01 |  |  | 2018-10-03 – 2018-10-04 | TSE 10857 (rating 3): Updated Additional Lower Tester settings for test cases PBAP/PSE/PBB/BV-44- C to 46-C. Also updated Additional Pass verdicts for 46-C. Updated template. |
|  |  |  | 1.2.3.0 |  |  | 2018-11-09 | Updated version number from 1.2.1.2 to 1.2.3.0 to align with adoption of the specification 1.2.3 |
| 18 |  |  | 1.2.3.0 |  |  | 2018-11-21 | Approved by BTI. Prepared for TCRL 2018-2 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 1.2.3.0ed2 r00–r03 |  |  | 2023-03-11 – 2023-04-13 | TSE 22801 (rating 1): Corrected the test condition in PBAP/PCE/PBB/BV-40-C. Editorial edits to align the document with the latest TS template, including removal of section numbering from sections containing a single TC and conversion to double-numbering to the table numbers for Tables 4.3 – 4.9. |
|  |  |  | 1.2.3.0 edition 2 |  |  | 2023-04-14 | Approved by BTI on 2023-04-13. Prepared for edition 2 publication. |
|  |  |  | p19r00–r02 |  |  | 2023-04-18 – 2023-05-02 | TSE 22654 (rating 2): Updated initial condition, test procedure, and expected outcome for PBAP/PSE/PBD/BV-13-C. Updated the TCMT for PBAP/PSE/PBD/BV-13-C. TSE 22800 (rating 2): Deleted the test condition and updated the test procedure in PBAP/PCE/PBB/BV-01- C. TSE 22832 (rating 1): Updated the additional Lower Tester settings for PBAP/PCE/PBD/BV-48-C and PBAP/PCE/PBB/BV-38-C. Updated the additional Pass verdicts for PBAP/PCE/PBB/BV-34-C, -36-C, and -38-C. Revised the document numbering convention, setting the last release publication of 1.2.3.0 as p18. |
| 19 |  |  | p19 |  |  | 2023-06-29 | Approved by BTI on 2023-05-28. Prepared for TCRL 2023-1 publication. |
|  |  |  | p19ed2 r00–r02 |  |  | 2023-08-07 – 2023-08-28 | TSE 23063 (rating 1): Replaced “PSE” with “PBAP” in three items of the TCMT to eliminate references to a non-existent layer abbreviation. Added Test Strategy section. Reformatted the Test groups section to align with the current TS template. |
|  |  |  | p19 edition 2 |  |  | 2023-08-28 | Approved by BTI on 2023-08-24. Prepared for edition 2 publication. |
|  |  |  | p20r00–r08 |  |  | 2023-12-18 – 2024-04-26 | TSE 24002 (rating 1): Updated the document to align with current standards. Corrected two TCIDs in the TCMT. TSE 24534 (rating 4): Added new GSIT section with new TCs PBAP/PCE/CGSIT/SFC/BV-01-C, PBAP/PCE/SGSIT/SERR/BV-01-C, PBAP/PCE/SGSIT/ATTR/BV-01-C and -02-C, PBAP/PSE/SGSIT/SERR/BV-01-C, PBAP/PSE/SGSIT/ATTR/BV-01-C – -06-C, PBAP/PCE/SGSIT/OFFS/BV-01-C, and PBAP/PSE/SGSIT/OFFS/BV-01-C. Removed PBAP/PSE/GOEP/CON/BV-02-C from the TCRL. Updated the TCMT accordingly. Updated the references list, the test groups list, the TC class naming conventions table, and Appendix A. Updated the GSIT statements in the TCID conventions section. |
| 20 |  |  | p20 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p21r00 |  |  | 2024-10-15 | TSE 22816 (rating 1): Updated the Pass verdict for PBAP/PSE/SSM/BI-03-C. |
| 21 |  |  | p21 |  |  | 2025-02-18 | Approved by BTI on 2024-12-25. Prepared for TCRL 2025-1 publication. |
|  |  |  | p22r00 |  |  | 2025-09-12 | TSE 28175 (rating 2): Converted the following non- IOPT -I test cases to -C: PBAP/PCE/PBF/BV-01-I – -03-I; PBAP/PCE/PDF/BV-01-I, -02-I, -04-I, and -06-I; PBAP/PSE/PBF/BV-01-I – -03-I; PBAP/PSE/PDF/BV- 01-I, -03-I, -05-I, and -06-I; and PBAP/PSE/SSM/BV- 08-I. Updated the TCMT accordingly. |
| 22 |  |  | p22 |  |  | 2025-11-04 | Approved by BTI on 2025-09-24. Prepared for TCRL pkg101 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Dominik Sollfrank |  |  | Berner & Mattner |  |
|  | Alicia Courtney |  |  | Broadcom, Inc. |  |
|  | Magnus Sommansson |  |  | Cambridge Sillicon Radio |  |
|  | Burch Seymour |  |  | Continental Automotive Systems |  |
|  | Robert Hrabak |  |  | General Motors |  |
|  | Stephen Raxter |  |  | Johnson Controls, Inc. |  |
|  | Stephen Raxter |  |  | National Analysis Center |  |
|  | Stephane Bouet |  |  | Nissan |  |
|  | Patrick Clauberg |  |  | Nokia |  |
|  | Nerissa Green |  |  | Nokia |  |
|  | Kyle Penri-Williams |  |  | Parrot |  |
|  | Scott Walsh |  |  | Plantronics, Inc. |  |
|  | Saravanun Sankaralingam |  |  | UL |  |


## 7 Appendix A - Supplementary Interoperability Tests

This section provides a supplementary set of interoperability tests. These tests are aimed at scenarios that do not have a direct specification reference. The tests are recommended by the Bluetooth SIG to be run for improved interoperability but they are not required to be executed as part of the Bluetooth Qualification program.

### 7.1 Phone Book Downloading Feature

Verify that the Phone Book Downloading feature can be used successfully.
PBAP/PCE/PDF/BV-02-C [PCE Retrieve Large Phone Book]
• Test Purpose
Verify that the PCE can retrieve large Phone Books from the PSE.
• Reference and Motivation
[1] 5.1
When downloading a large phone book, some PCE have been reported to become unresponsive. This test case is to verify this common scenario.
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains at least one non-NULL Phone Book. The phone book contains at least five hundred entries. This non-NULL Phone Book must be of interest for the PCE.
• Test Procedure
The PCE establishes a PBAP session with the PSE and in this session retrieves the Phone Book objects of interest.
• Expected Outcome
Pass verdict
The PCE is capable of retrieving all the Phone Book objects of interest from the PSE.
The information thus downloaded is accurate. Both the PCE and the PSE are in normal operation mode after the completion of the downloading operation.
PBAP/PSE/PDF/BV-03-C [PSE Transfer Large Phone Book]
• Test Purpose
Verify that the PSE can transfer large Phone Books to PCE.
• Reference and Motivation
[1] 5.1
Most PSEs have the capability of holding large phone books. When transferring this phone book to the client, some PSE have become unresponsive. This case is to verify that phone book transfer is not affected by the size of the phone book.
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains at least one non-NULL Phone Book. The phone book contains at least one hundred entries. This non-NULL Phone Book must be of interest for the PCE.
• Test Procedure
1. The PCE establishes a PBAP session with the PSE. 2. The PSE transfers this large phone book to the PCE.
• Expected Outcome
Pass verdict
The PSE transfers all the Phone Book objects of interest to the PCE.
The information thus downloaded is accurate. Both the PCE and the PSE are in normal operation mode after the completion of the downloading operation.
PBAP/PCE/PDF/BV-04-C [PCE Retrieve Empty Phone Book]
• Test Purpose
Verify that the PCE can retrieve an empty Phone Book from the PSE.
• Reference and Motivation
[1] 5.1
This is a scenario where PCEs have been reported to hang or become unresponsive.
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains one NULL Phone Book. This Phone Book must be of interest for the PCE.
• Test Procedure
The PCE establishes a PBAP session with the PSE and in this session retrieves the Phone Book objects of interest.
• Expected Outcome
Pass verdict
The PCE retrieves the Phone Book of interests from the PSE.
Both the PCE and the PSE are in normal operation mode after the completion of the downloading operation.
PBAP/PSE/PDF/BV-05-C [PSE Transfer Empty Phone Book]
• Test Purpose
Verify that the PSE can transfer empty phone book to PCE.
• Reference and Motivation
[1] 5.1
This test case is to ensure that phone book transfer is not affected by the size of the phone book.
• Initial Condition
- The PCE and the PSE have been paired.
- The PSE is discoverable and connectable. The PSE contains at least one NULL Phone Book. This Phone Book must be of interest for the PCE.
• Test Procedure
1. The PCE establishes a PBAP session with the PSE. 2. The PSE transfers the phone book to the PCE.
• Expected Outcome
Pass verdict
The PSE transfers the phone book of interest to the PCE.
Both the PCE and the PSE are in normal operation mode after the completion of the downloading operation.

### 7.2 Phone Book Downloading Functional Components

Verify Phone Book Download scenarios.
PBAP/PSE/PBD/BV-11-C [PSE Return Phonebook – Limit number of entries]
• Test Purpose
Verify that the PSE can properly deliver a phone book with the maximum number of phone book entries returned specified by the PCE.
This test only applies to devices that allow for the MaxListCount value to be set.
• Reference and Motivation
[1] 5.1.4
The PBAP specification states the following about the header MaxListCount - “This header is used to indicate the maximum number of entries of the <xbt/phonebook> object that the PCE can handle. This header always contains a value between 0 and 65535”.
This test is based on issues reported that some PSEs do not correctly handle a case where this header value is set to any value other than the default value.
• Initial Condition
- The IUT has at least one non-NULL Phone Book with a minimum of 5 phone book entries.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Phone Book with the header MaxListCount set to 3.
• Expected Outcome
Pass verdict
The Lower Tester successfully downloads the specified Phone Book object. The Phone Book selected is identical on the Lower Tester and on the IUT. The number of phone book entries downloaded is three (3).
The IUT and Lower Tester are in normal operation mode after the completion of the downloading operation.
PBAP/PSE/PBD/BV-12-C [PSE Return vCard listing – Limit number of entries]
• Test Purpose
Verify that the PSE can properly deliver a vCard listing with the maximum number of entries specified by the PCE.
This test only applies to devices that allow for the MaxListCount value to be set.
• Reference and Motivation
[1] 5.3, 5.1.4
This test is based on issues reported that some PSEs do not correctly handle a case where this header value is set to any value other than the default value.
• Initial Condition
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
1. The Lower Tester attempts to retrieve from the PSE the vCard-listing object corresponding to the
current folder by use of PullvCardListing with an empty name header. The header MaxListCount is set to 3.
• Expected Outcome
Pass verdict
The Lower Tester successfully retrieved the vCard-listing object.
PBAP/PSE/PBD/BV-13-C [PSE Phone Book Order]
• Test Purpose
Verify that the PSE can properly deliver a phone book with call events arranged chronologically.
• Reference and Motivation
[1] 3.1.5
This test case is created for checking some implementations that do not conform to the specification, thereby causing some interoperability issues and poor user experience.
Section 3.1.5.3 states “The handles should be attributed in the PSE in such a way that once sorted by increasing handles; the most recent call event in the listed folder has the handle 1.vcf. The order is therefore chronological.”
Numerous implementations violating this rule have been reported.
• Initial Condition
- The IUT has at least one non-NULL Phone Book with more than one entry in any call history phone book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Call History Phone Book (e.g., ich, och etc.) vCard listing object and vCard entries.
• Expected Outcome
Pass verdict
The Lower Tester successfully downloads the specified Phone Book listing and entries. The Phone Book selected is identical on the Lower Tester and on the IUT.
When the call events handles are arranged by increasing handle value, then the most recent call event has handle 1.vcf and the timestamps are in chronological order.
The IUT and Lower Tester are in normal operation mode after the completion of the downloading operation.
PBAP/PSE/PBD/BV-14-C [PSE Call stack timestamps]
• Test Purpose
Verify that the PSE provides timestamps for the MCH, ICH, OCH, CCH phonebooks and that these timestamps are correct [i.e., they contain the actual local time on the phone when the call was made].
• Reference and Motivation
[1] 3.1.5, 3.1.4.1
The Phone Book Profile Access Specification [1] states the following – “The time of each call found in och, ich, mch and cch folder, can be shown using the IrMC defined X-IRMC-CALL-DATETIME property that extends the vCard specification.” It is strongly recommended to use this property parameter whenever possible. This test is to verify if each Phone Book object has a timestamp and if this timestamp is correct.
• Initial Condition
- The IUT has at least one non-NULL Phone Book with more one entry in any call history phone book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Phone Book (e.g., ich, och etc.).
• Expected Outcome
Pass verdict
The Lower Tester successfully downloads the specified Phone Book object. The Phone Book selected is identical on the Lower Tester and on the IUT.
Each phone book entry in the call history phone book has a timestamp associated to it and this time stamp is correct.
The IUT and Lower Tester are in normal operation mode after the completion of the downloading operation.
PBAP/PSE/PBD/BV-15-C [PSE No User Interaction]
• Test Purpose
Verify that no user interaction on the PSE is required for phonebook download.
• Reference and Motivation
[1] 3.1.5
Any PSE requirement to use PSE during a phonebook download could be frustrating for a user.
• Initial Condition
- The IUT has at least one non-NULL Phone Book with more one entry in any call history phone book.
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Phone Book (e.g., ich, och etc.).
• Expected Outcome
Pass verdict
The Lower Tester successfully downloads the specified Phone Book object. The Phone Book selected is identical on the Lower Tester and on the IUT.
The IUT and Lower Tester are in normal operation mode after the completion of the downloading operation.
PBAP/PSE/PBD/BV-16-C [PSE Special Character Handling]
• Test Purpose
Verify that the PSE correctly handles control characters (for example semicolons “;”, CR, LF, …) in the name property correctly by using the appropriate escape characters ‘\’ as defined in the vCard standard, and that formatting characters like white spaces, brackets, dashes, slashes are transferred correctly.
• Reference and Motivation
[1] 3.1.5
In most common scenarios, the name property of phone book entries may contain special characters. It has been reported that many PSEs do not handle these characters during phone book download operation causing interoperability issues. This test is to verify if these characters can be handled by the PSE.
• Initial Condition
- The IUT has at least one non-NULL Phone Book.
- At least one phone book entry has a special character in the name property (“;”, “?”, “,”, “%”, etc.).
- A PBAP session must be ongoing between the IUT and the Lower Tester.
• Test Procedure
The Lower Tester attempts to download a Phone Book (e.g., ich, och, etc.).
• Expected Outcome
Pass verdict
The Lower Tester successfully downloads the specified Phone Book object. The Phone Book selected is identical on the Lower Tester and on the IUT.
The IUT and Lower Tester are in normal operation mode after the completion of the downloading operation.