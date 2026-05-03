# L2CAP.ICS.p26

> Source: PDF converted via PyMuPDF.

---

Logical Link Control and Adaptation Protocol (L2CAP)
Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: L2CAP.ICS.p26 ▪ Revision Date: 2024-07-01 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-1
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

### 1.2 L2CAP Transport Configuration

Table 0: L2CAP Transport Configuration

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR |  |  | [1] 1.1 [6] 1.1 |  |  | C.1, C.4 |  |  |
| 2 |  |  | LE |  |  | [6] 1.1 |  |  | C.2, C.4 |  |  |
| 3 |  |  | BR/EDR/LE |  |  | [6] 1.1 |  |  | C.3, C.4 |  |  |


### 1.3 Capability Statement


#### 1.3.1 Roles

Table 1: Role Requirements

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Data Channel Initiator |  |  | [1] 2 |  |  | C.3 |  |  |
| 2 |  |  | Data Channel Acceptor |  |  | [1] 2 |  |  | C.1 |  |  |
| 3 |  |  | LE Central |  |  | [4] 2 |  |  | C.2 |  |  |
| 4 |  |  | LE Peripheral |  |  | [4] 2 |  |  | C.2 |  |  |
| 5 |  |  | LE Data Channel Initiator |  |  | [5] 3.4 |  |  | C.4 |  |  |
| 6 |  |  | LE Data Channel Acceptor |  |  | [5] 3.4 |  |  | C.5 |  |  |


#### 1.3.2 General Operation

Table 2: General Operation

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | L2CAP Signaling channel over BR/EDR |  |  | [1] 2.2 |  |  | C.16 |  |  |
| 2 |  |  | Configuration process |  |  | [1] 7.1 |  |  | C.16 |  |  |
| 3 |  |  | Connection-oriented data channel over BR/EDR |  |  | [1] 2.2 |  |  | C.16 |  |  |
| 4 |  |  | Send echo request |  |  | [1] 4.8 |  |  | C.17 |  |  |
| 5 |  |  | Send echo response |  |  | [1] 4.9 |  |  | C.16 |  |  |
| 6 |  |  | Send information request |  |  | [1] 4.10 |  |  | C.11 |  |  |
| 7 |  |  | Send information response |  |  | [1] 4.11 |  |  | C.16 |  |  |
| 8 |  |  | Item no longer used |  |  | N/A |  |  | N/A |  |  |
| 9 |  |  | Connectionless channel packet |  |  | [1] 3.2 |  |  | C.17 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 |  |  | Retransmission mode |  |  | [1] 8.4 |  |  | C.17 |  |  |
| 11 |  |  | Flow Control mode |  |  | [1] 8.5 |  |  | C.11 |  |  |
| 12 |  |  | Enhanced Retransmission Mode |  |  | [2] 8.6 |  |  | C.11 |  |  |
| 13 |  |  | Streaming Mode |  |  | [2] 8.7 |  |  | O |  |  |
| 14 |  |  | FCS Option |  |  | [2] 5.5 |  |  | C.1 |  |  |
| 15 |  |  | Generate Local Busy Condition |  |  | [2] 8.6.4.3 |  |  | C.2 |  |  |
| 16 |  |  | Send Reject |  |  | [2] 8.6.1.2 |  |  | C.2 |  |  |
| 17 |  |  | Send Selective Reject |  |  | [2] 8.6.1.3 |  |  | C.2 |  |  |
| 18 |  |  | Mandatory use of ERTM |  |  | [2] 8.6 |  |  | C.3 |  |  |
| 19 |  |  | Mandatory use of Streaming Mode |  |  | [2] 8.7 |  |  | C.4 |  |  |
| 20 |  |  | Optional use of ERTM |  |  | [2] 8.6 |  |  | C.3 |  |  |
| 21 |  |  | Optional use of Streaming Mode |  |  | [2] 8.7 |  |  | C.4 |  |  |
| 22 |  |  | Send data using SAR in ERTM |  |  | [2] 3.3.2 |  |  | C.5 |  |  |
| 23 |  |  | Send data using SAR in Streaming Mode |  |  | [2] 3.3.2 |  |  | C.6 |  |  |
| 24 |  |  | Actively request Basic Mode for a PSM that supports the use of ERTM or Streaming Mode |  |  | [2] 5.4 |  |  | C.1 |  |  |
| 25 |  |  | Performing L2CAP channel mode configuration fallback from Streaming Mode to ERTM |  |  | [2] 5.4 |  |  | C.8 |  |  |
| 26 |  |  | Sending more than one unacknowledged I-Frame when operating in ERTM |  |  | [2] 8.6.5 |  |  | C.5 |  |  |
| 27 |  |  | Sending more than three unacknowledged I-Frame when operating in ERTM |  |  | [2] 8.6.5 |  |  | C.5 |  |  |
| 28 |  |  | Peer TxWindow configuration greater than 1 |  |  | [2] 5.4 |  |  | C.5 |  |  |
| 29 |  |  | AMP |  |  | [3] 9 |  |  | C.24 |  |  |
| 30 |  |  | Information request for fixed channels |  |  | [3] 4.10, 4.13 |  |  | C.9 |  |  |
| 31 |  |  | AMP Manager |  |  | [3] 2.1 |  |  | C.18 |  |  |
| 32 |  |  | ERTM over AMP |  |  | [3] 9 |  |  | C.25 |  |  |
| 33 |  |  | Streaming Mode Source over AMP |  |  | [3] 3.3, 8.7 |  |  | C.12 |  |  |
| 34 |  |  | Streaming Mode Sink over AMP |  |  | [3] 3.3, 8.7 |  |  | C.12 |  |  |
| 35 |  |  | Unicast Connectionless Data, Reception |  |  | [3] 3.3, 7.6 |  |  | O |  |  |
| 36 |  |  | Ability to transmit an unencrypted packet over a Unicast connectionless L2CAP channel |  |  | [3] 7.6 |  |  | O |  |  |
| 37 |  |  | Ability to transmit an encrypted packet over a Unicast connectionless L2CAP channel |  |  | [3] 7.6 [6] GAP, 5.2.2 |  |  | O |  |  |
| 38 |  |  | Extended Flow Specification for BR/EDR |  |  | [3] 7.10 |  |  | C.1 |  |  |
| 39 |  |  | Extended Window Size |  |  | [1] 5.7 |  |  | C.1 |  |  |
| 40 |  |  | L2CAP LE Signaling channel |  |  | [4] 2.1, 2.2 |  |  | C.13 |  |  |
| 41 |  |  | Command reject |  |  | [4] 4.10 |  |  | C.29 |  |  |
| 42 |  |  | Send Connection Parameter Update Request |  |  | [4] 4.20 |  |  | C.14 |  |  |
| 43 |  |  | Send Connection Parameter Update Response |  |  | [4] 4.21 |  |  | C.15 |  |  |
| 44 |  |  | Extended Flow Specification for AMP |  |  | [3] 5.6 |  |  | C.18 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45 |  |  | Send Disconnect Request Command |  |  | [1] 4.6 |  |  | C.21 |  |  |
| 45a |  |  | Send Disconnect Request Command – LE |  |  | [5] 4.6 |  |  | C.22 |  |  |
| 46 |  |  | LE Credit Based Flow Control Mode |  |  | [5] 3.4 |  |  | C.19 |  |  |
| 47 |  |  | LE Data Channel |  |  | [1] 3.4 |  |  | C.20 |  |  |
| 48 |  |  | Enhanced Credit Based Flow Control Mode |  |  | [7] 3.4 |  |  | C.23 |  |  |
| 48a |  |  | Enhanced Credit Based Flow Control Mode – BR/EDR |  |  | [7] 3.4 |  |  | C.26 |  |  |
| 48b |  |  | Enhanced Credit Based Flow Control Mode – LE |  |  | [7] 3.4 |  |  | C.27 |  |  |
| 49 |  |  | Support pending result in L2CAP CREDIT BASED CONNECTION RSP _ _ _ _ |  |  | [1] 4.26 |  |  | C.28 |  |  |

C.1: Optional IF L2CAP 2/12 “Enhanced Retransmission Mode” OR L2CAP 2/13 “Streaming Mode”, otherwise Excluded. C.2: Optional IF L2CAP 2/12 “Enhanced Retransmission Mode” AND L2CAP 2/28 “Peer TxWindow configuration greater than 1”, otherwise Excluded. C.3: Mandatory to support at least one IF L2CAP 2/12 “Enhanced Retransmission Mode”, otherwise Excluded. C.4: Mandatory to support at least one IF L2CAP 2/13 “Streaming Mode”, otherwise Excluded. C.5: Optional IF L2CAP 2/12 “Enhanced Retransmission Mode”, otherwise Excluded. C.6: Optional IF L2CAP 2/13 “Streaming Mode”, otherwise Excluded. C.7: No longer used. C.8: Mandatory IF L2CAP 2/12 “Enhanced Retransmission Mode” AND L2CAP 2/13 “Streaming Mode” AND L2CAP 2/21 “Optional use of Streaming Mode”, otherwise Excluded. C.9: Mandatory IF L2CAP 2/29 “AMP”, otherwise Optional IF L2CAP 2/6 “Send information request”, otherwise Excluded. C.10: No longer used. C.11: Mandatory IF L2CAP 2/29 “AMP”, otherwise Optional IF L2CAP 0/1 “BR/EDR” OR L2CAP 0/3 “BR/EDR/LE”, otherwise Excluded. C.12: Optional IF L2CAP 2/29 “AMP”, otherwise Excluded. C.13: Mandatory IF L2CAP 0/2 “LE” OR L2CAP 0/3 “BR/EDR/LE”, otherwise Excluded. C.14: Optional IF L2CAP 1/4 “LE Peripheral”, otherwise Excluded. C.15: Mandatory IF L2CAP 1/3 “LE Central”, otherwise Excluded. C.16: Mandatory IF L2CAP 0/1 “BR/EDR” OR L2CAP 0/3 “BR/EDR/LE”, otherwise Excluded. C.17: Optional IF L2CAP 0/1 “BR/EDR” OR L2CAP 0/3 “BR/EDR/LE”, otherwise Excluded. C.18: Mandatory IF L2CAP 2/29 “AMP”, otherwise Excluded. C.19: Optional IF L2CAP 0/2 “LE” OR L2CAP 0/3 “BR/EDR/LE”, otherwise Excluded. C.20: Mandatory IF L2CAP 2/46 “LE Credit Based Flow Control Mode”, otherwise Excluded. C.21: Optional IF L2CAP 2/1 “L2CAP Signaling channel over BR/EDR”, otherwise Excluded. C.22: Optional IF L2CAP 2/40 “L2CAP LE Signaling channel” AND L2CAP 2/46 “LE Credit Based Flow Control Mode”, otherwise Excluded. C.23: Optional IF CORE 2a/52 “Host Core v5.2 or later”, otherwise Excluded. C.24: Mandatory IF CORE 11/20 “AMP Manager Protocol (A2MP)”, otherwise Excluded. C.25: Optional IF L2CAP 2/12 “Enhanced Retransmission Mode” AND L2CAP 2/29 “AMP”, otherwise Excluded. C.26: Optional IF L2CAP 2/48 “Enhanced Credit Based Flow Control Mode” AND (L2CAP 0/1 “BR/EDR” OR L2CAP 0/3 “BR/EDR/LE”), otherwise Excluded. C.27: Optional IF L2CAP 2/48 “Enhanced Credit Based Flow Control Mode” AND (L2CAP 0/2 “LE” OR L2CAP 0/3 “BR/EDR/LE”), otherwise Excluded. C.28: Mandatory IF CORE 2a/53 “Host Core v5.3 or later” AND L2CAP 2/48 “Enhanced Credit Based Flow Control Mode”, otherwise Optional IF L2CAP 2/48 “Enhanced Credit Based Flow Control Mode”, otherwise Excluded. C.29: Mandatory IF L2CAP 2/1 “L2CAP Signaling channel over BR/EDR” OR L2CAP 2/40 “L2CAP LE Signaling channel”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | RTX timer |  |  | [1] 6.2.1 |  |  | M |  |  |
| 2 |  |  | ERTX timer |  |  | [1] 6.2.2 |  |  | C.4 |  |  |
| 3 |  |  | Minimum MTU size of 48 octets |  |  | [1] 5.1 |  |  | C.4 |  |  |
| 4 |  |  | MTU size larger than 48 octets |  |  | [1] 5.1 |  |  | C.5 |  |  |
| 5 |  |  | Flush timeout value for reliable channel |  |  | [1] 5.2 |  |  | C.4 |  |  |
| 6 |  |  | Flush timeout value for unreliable channel |  |  | [1] 5.2 |  |  | C.5 |  |  |
| 7 |  |  | Bi-directional quality of service (QoS) option field |  |  | [1] 5.3 |  |  | C.1 |  |  |
| 8 |  |  | Negotiate QoS service type |  |  | [1] 5.3 |  |  | C.5 |  |  |
| 9 |  |  | Negotiate and support service type ‘No traffic’ |  |  | [1] 5.3 |  |  | C.2 |  |  |
| 10 |  |  | Negotiate and support service type ‘Best effort’ |  |  | [1] 5.3 |  |  | C.3 |  |  |
| 11 |  |  | Negotiate and support service type ‘Guaranteed’ |  |  | [1] 5.3 |  |  | C.2 |  |  |
| 12 |  |  | Minimum MTU size of 23 octets |  |  | [4] 5.1 |  |  | C.6 |  |  |
| 13 |  |  | Negotiate and support service type ‘No traffic’ for Extended Flow Specification |  |  | [3] 5.6 |  |  | C.7 |  |  |
| 14 |  |  | Negotiate and support service type ‘Best Effort’ for Extended Flow Specification |  |  | [3] 5.6 |  |  | C.8 |  |  |
| 15 |  |  | Negotiate and support service type ‘Guaranteed’ for Extended Flow Specification. |  |  | [3] 5.6 |  |  | C.7 |  |  |
| 16 |  |  | Support Multiple Simultaneous LE Data Channels |  |  | [5] 3.4 |  |  | C.10 |  |  |

Table 4: Security Aspects (LE)
Prerequisite: L2CAP 0/2 “LE” OR L2CAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Detect insufficient authentication |  |  | [1] 10.1, 10.2 |  |  | O |  |  |
| 2 |  |  | Detect insufficient authorization |  |  | [1] 10.1, 10.2 |  |  | O |  |  |
| 3 |  |  | Detect insufficient encryption |  |  | [1] 10.1, 10.2 |  |  | O |  |  |

Prerequisite: L2CAP 0/1 “BR/EDR” OR L2CAP 0/3 “BR/EDR/LE”

|  | Item |  |  | Capability |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Detect insufficient authentication |  |  | [1] 10.1, 10.2 |  |  | O |  |  |
| 2 |  |  | Detect insufficient authorization |  |  | [1] 10.1, 10.2 |  |  | O |  |  |


## 2 References

[1] Specification of the Bluetooth System, Volume 3, Part A, L2CAP, Version 2.0 or later
[2] Specification of the Bluetooth System, Volume 3, Part A, L2CAP, Version 2.1 plus CSA1 or later
[3] Specification of the Bluetooth System, Volume 3, Part A, L2CAP, Version 3.0 or later
[4] Specification of the Bluetooth System, Volume 3, Part A, L2CAP, Version 4.0 or later
[5] Specification of the Bluetooth System, Volume 3, Part A, L2CAP, Version 4.1 or later
[6] Specification of the Bluetooth System, Volume 3, Part C, GAP, Version 3.0 or later
[7] Specification of the Bluetooth System, Volume 3, Part A (Logical Link Control and Adaptation Protocol Specification), Version 5.2 or later

## 3 Mapping of L2CAP feature bits to ICS items

This section is informative.
Not all L2CAP features have corresponding ICS entries.

|  | Feature Bit |  |  | Feature |  |  | ICS |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |  |  | Flow control mode |  |  | 2/11 |  |  |
| 1 |  |  | Retransmission mode |  |  | 2/10 |  |  |
| 2 |  |  | Bi-directional QOS |  |  |  |  |  |
| 3 |  |  | Enhanced Retransmission Mode |  |  | 2/12 |  |  |
| 4 |  |  | Streaming Mode |  |  | 2/13 |  |  |
| 5 |  |  | FCS Option |  |  | 2/14 |  |  |
| 6 |  |  | Extended Flow Specification for BR/EDR |  |  | 2/38 |  |  |
| 7 |  |  | Information request for fixed channels |  |  | 2/30 |  |  |
| 8 |  |  | Extended Window Size |  |  | 2/39 |  |  |
| 9 |  |  | Unicast Connectionless Data reception |  |  | 2/35 |  |  |
| 10 |  |  | Enhanced Credit Based Flow Control Mode over BR/EDR |  |  | 2/48a |  |  |
| 31 |  |  | Reserved for feature mask extension |  |  |  |  |  |

Table 3.1: Mapping of L2CAP feature bits to ICS items

## 4 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 0 |  |  | 1.2.1 |  |  | 2004-03-29 | Changed document number and revision number to conform with legacy system. Added Disclaimer and Copyright Notice. |
| 1 |  |  | 1.2.2 |  |  | 2004-08-24 | Incorporated TSE 554 affecting Tables 1 and 2. |
|  |  |  | 1.2.3r1 |  |  | 2005-03-23 | Incorporated TSE 595 to create new Table 1 and renumber tables. |
| 2 |  |  | 1.2.3 |  |  | 2005-03-23 | Prepare for publication. |
|  |  |  | 2.1.E.0r0 |  |  | 2006-12-20 | Change doc identifier to apply to v1.2 and later specifications |
| 3 |  |  | 2.1.E.0 |  |  | 2006-12-21 | Prepare for publication. |
|  |  |  | 2.1.E.1r0 |  |  | 2008-04-19 | Added Table 2/12-28 for CSA1 |
|  |  |  | 2.1.E.1r1 |  |  | 2008-04-22 | Input editorial review comments from SIG staff |
| 4 |  |  | 2.1.E.1 |  |  | 2008-06-23 | Prepare for publication. |
|  |  |  | 2.1.E.2r0-1 |  |  | 2009-02-05 | Table 2: add rows for A2MP, AMP L2CAP, and UCD Technical review |
| 5 |  |  | 3.0.H.0/ 2.1.E.2 |  |  | 2009-03-25 | Prepare for publication. |
| 6 |  |  | 3.0.H.1r0 |  |  | 2009-08-12 | TSE 2934: Change Table 2, footnote C.14 TSE 2933: Change Table 2 footnote C.1 |
| 7 |  |  | 3.0.H.1a |  |  | 2010-01-11 | Fixed Table 2 radio buttons 30/31. |
|  |  |  | 4.0.0r1-r4 |  |  | 2010-05-18– 2010-06-16 | Document merged (2.1.E.2r0 LE7 L2CAP ICS) _ including LE Added table 0 All M’s and O’s for BR/EDR turned into condtionals Global update on references to “2.0 and later..” AND “4.0 and later references..” Minor clarification to table 0 conditions tied to SUM ICS _ TSE 3420, added item 2/44 Extended Flow Specification for AMP TSE 3421, added items 3/13, 3/14 and 3/15 |
| 8 |  |  | 4.0.0 |  |  | 2010-06-30 | Prepare for publication. |
|  |  |  | 4.0.1r0-r2 |  |  | 2010-11-19– 2011-04-28 | TSE 3838: Table 2, footnote C.14 TSE 3839: Table 2, footnote C.16 TSE 3863: Table 2, footnote C.22 added TSE 3873: Duplicate of TSE 3839 TSE 4352: Table 3, Footnote C.7, C.8, C.9 TSE4269 Added item 1/3 and 1/4. Table 2 C18 and C.19 |
| 9 |  |  | 4.0.1 |  |  | 2011-07-15 | Prepare for publication. |
|  |  |  | 4.0.2r0 |  |  | 2011-11-07 | TSE 4431: Table 2/42 and 2/43: Table 2, C.18 |
| 10 |  |  | 4.0.2 |  |  | 2012-03-30 | Prepare for publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
| 11 |  |  | 4.0.3r0 |  |  | 2012-05-18 | TSE 4752: Correct numbering, modify Table 0 Prerequisite, and Table 1 C.2 and Table 2/35 and Table 2 C.1 TSE 4737: Table 2/4 |
| 12 |  |  | 4.0.4 |  |  | 2012-07-24 | Adopted by the Bluetooth SIG Board of Directors |
|  |  |  | 4.0.5r0 |  |  | 2012-09-05 | TSE 4828: Made Support of RTX timer mandatory in Table 3: Configurable Parameters |
| 13 |  |  | 4.0.5 |  |  | 2012-11-12 | Prepare for Publication |
|  |  |  | 4.0.6r1 |  |  | 2013-05-31 | TSE 4839: Added C.3 to Table 1. |
| 14 |  |  | 4.0.6 |  |  | 2013-07-02 | Prepare for Publication |
|  |  |  | 4.0.7rT |  |  | 2013-08-07 | Template Conversion - Updated conditional wording to match current language. |
|  |  |  | 4.0.7rTr3 |  |  | 2013-10-07 | Template Review Comment Resolution |
|  |  |  | 4.1.0r01 |  |  | 2013-10-07 | TSE 4840: Added item 2/45 “Send Disconnect Request Command” |
|  |  |  | 4.1.0r02 |  |  | 2013-10-11 | LE L2CAP Connection Oriented Channels CR |
|  |  |  | 4.1.0r03 |  |  | 2013-11-06 | Updated references to SUM ICS for 4.1 |
| 15 |  |  | 4.1.0 |  |  | 2013-12-03 | Prepare for Publication |
|  |  |  | 4.1.1r00 |  |  | 2014-01-23 | TSE 5430: Updated SUM ICS references for Table 0 C.3, Table 1 C.4 and C.5, Table 2 C.1 and C.23, Table 3 C.10. |
|  |  |  | 4.1.1r01 |  |  | 2014-04-04 | TSE 5564: Corrected Table 1 C.4, C.5; Table 2 C.1, C.12, C.14, C.16, C.18, C.19, and C.23; Table 3 C.10. TSE 5578: Table 2 C.1, C.12, C.14, C.16, C.18, C.19. TSE 5543: Table 2 C.5, C.16 |
| 16 |  |  | 4.1.1 |  |  | 2014-07-07 | TCRL 2014-1 Publication |
|  |  |  | 4.2.0r00 |  |  | 2014-11-17 | Revved version to align with Core Specification Version 4.2 Release. |
| 17 |  |  | 4.2.0 |  |  | 2014-12-04 | Prepare for TCRL2014-2 publication |
|  |  |  | 4.2.1r00 |  |  | 2015-05-05 | TSE 6093: Added new conditional C.25 to Table 2 and updated item 2/45 to point to it. |
|  |  |  | 4.2.1r01 |  |  | 2015-06-05 | Deleted Section 1.2 (Global Statement of Conformance) per current ICS template standards. |
|  |  |  | 4.2.1r02 |  |  | 2015-06-08 | Adjusted section numbering following deletion of Section 1.2 at 4.2.1r01 above. |
| 18 |  |  | 4.2.1 |  |  | 2015-07-14 | Prepared for TCRL 2015-1 publication |
|  |  |  | 4.2.2r00 |  |  | 2016-03-10 | TSE 6543: Section 1.2/Table 0, changed “Device Configuration” to “L2CAP Transport Configuration.” Item 1 Capability updated. |
| 19 |  |  | 4.2.2 |  |  | 2016-07-13 | Prepared for TCRL 2016-1 publication. |
|  |  |  | 5.0.0r00 |  |  | 2016-11-01 | Updated for Core Specification v5.0 release. Added support for Bluetooth Core Specification v5.0 to Table 2, C.1. Modified conditional statements in Table 1 and 2. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | 5.0.0r01 |  |  | 2016-11-08 | Updated to current template. Removed unnecessary parentheses and replaced with quotation marks. |
|  |  |  | 5.0.0r02 |  |  | 2016-11-21 | TSE 7808: Updated Table 2 Conditional C.1 to remove the “Implement at least one new feature” rule logic to Core versions 4.1 or later. |
| 20 |  |  | 5.0.0 |  |  | 2016-12-13 | Approved by BTI. Prepared for TCRL 2016-2 publication. |
|  |  |  | 5.0.1r00 |  |  | 2017-03-27 | TSE 8527: Updated reference in Table 0/1.Updated references for items 1-6 in Table 1. Updated references for items 1-20, 21-35, and 36-47 for Table 2. Added row 45a “Send Disconnect Request Command – LE” to Table 2. Updated conditional (C.25) to remove LE related dependencies and added conditional (C.26) to Table 2. Updated references for items 1-8 to Table 3. Updated references for items 9- 16 to Table 3. Updated existing references (1 and 4) and added 4 additional references for Core Spec 4.1 or later. |
| 21 |  |  | 5.0.1 |  |  | 2017-07-05 | Approved by BTI. Prepared for TCRL 2017-1 publication. |
|  |  |  | 5.0.2r00 |  |  | 2018-08-20 | Drafted 2019 Deprecation & Withdrawal changes |
|  |  |  | 5.1.0r00 |  |  | 2018-11-13 | Updated revision number from 5.0.2 to 5.1.0 to align with the adoption of Core Specification version 5.1 |
| 22 |  |  | 5.1.0 |  |  | 2018-12-07 | Approved by BTI. Prepared for TCRL 2018-2 publication. |
|  |  |  | p23r00–r02 |  |  | 2019-08-19 – 2019-11-22 | Added test groups to accommodate adoption of Core Specification v5.2 with regard to EATT CR r07. Added item 48 and note C.23 to Table 2; updated references section with new Core Specification. TSE 12752 (rating 1): Updated C.11 and C.23 for Table 2 to update numbering for SUM ICS Table 31 per TSE 12647. Revised document numbering convention, setting last release publication of 5.1.0 as p22; added publication number column to Revision History. |
| 23 |  |  | p23 |  |  | 2020-01-07 | Approved by BTI on 2019-12-22. Prepared for TCRL 2019-2 publication. |
|  |  |  | p24r00–r07 |  |  | 2020-04-15 – 2021-06-09 | TSE 12929 (rating 2): Added new Table 4 for Security Aspects in General Operation section. TSE 15450 (rating 1): Editorials to address Erratum 15353, globally change “Master” to “Central” and “Slave” to “Peripheral.” Incorporated Removing AMP TEST CRr03a: Added _ _ _ Removing AMP section to the References section to explain conditional text; added conditionals C.24 and C.25 and updated Status of items 29, 31, and 32 in Table 2. Template-related and consistency checker editorials. |
| 24 |  |  | p24 |  |  | 2021-07-13 | Approved by BTI on 2021-06-27. Prepared for TCRL 2021-1 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p25r00–r02 |  |  | 2021-08-17 – 2021-12-29 | TSE 15271 (rating 4): To address E14605, modified Table 4 (title, item 1 description, conditionals, added inter-layer dependency column) and added new Table 5. TSE 17463 (rating 4): Added ICS items in Table 2 for Enhanced Credit Based Flow Control Mode for BR/EDR and LE support with corresponding conditionals. Editorial cleanup of items with the word “support” in the name. Alignment of item 2/40 with the language used in the specification. Performed template-related formatting fixes and consistency checker editorials, including updates to the copyright page to align with v2 of the DNMD. |
| 25 |  |  | p25 |  |  | 2022-01-25 | Approved by BTI on 2021-12-27. Prepared for TCRL 2021-2 publication. |
|  |  |  | p25ed2 r00–r01 |  |  | 2022-02-02 – 2022-03-07 | TSE 17870 (rating 1): Revised the descriptions of items 1 and 3 in Table 2 to show that they are for BR/EDR transport. Updated ICS descriptions (and associated conditionals) in Tables 2 and 3 to remove the redundant word “support” in alignment with current ICS conventions. TSE 17871 (rating 1): Removed item 8 from Table 2 because it is no longer used. Editorials, including template-related items and consistency checker fixes. |
|  |  |  | p25, edition 2 |  |  | 2022-03-07 | Approved by BTI on 2022-03-07. Prepared for edition 2 publication. |
|  |  |  | p25ed3r00– r01 |  |  | 2023-03-10 – 2023-03-20 | TSE 22227 (rating 1): Deleted the reference to SUM ICS 32/5 in the prerequisite for Table 0. Deleted the introductory text for the Capability Statement section. Editorial edits to align the document with the latest ICS template. |
|  |  |  | p25 edition 3 |  |  | 2023-04-14 | Approved by BTI on 2023-04-13. Prepared for edition 3 publication. |


|  | Publication |  |  | Revision |  | Date | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |
|  |  |  | p26r00–r06 |  |  | 2023-09-25 – 2024-04-24 | TSE 18351 (rating 3): Added new item 2/49 and associated C.28. TSE 22166 (rating 4): Added an informational section to map L2CAP feature bits to ICS items. TSE 23557 (rating 2): Renamed Tables 4 and 5, removed the ILDs to GAP, in addition to related conditionals, added prerequisites, and updated the Capability names, references, and statuses to be clearer. TSE 23558 (rating 2): Updated the status of 2/6, 2/11, and 2/30, also updating 2/30’s Capability name and references. Added C.9 and expanded C.11. TSE 24074 (rating 1): Replaced SUM ICS references with CORE ICS references. Updated Table 0 conditionals C.1–C.3 and added C.4, affecting 0/1, 0/2, and 0/3; updated Table 1 conditionals C.1 and C.3, affecting 1/1 and 1/2; updated Table 2 conditionals C.11, C.16, C.17, C.23, C.24, and C.26, affecting 2/1–2/7, 2/9–2/12, 2/29, 2/30, 2/48, and 2/48a; updated Table 3 conditionals C.4 and C.5, affecting 3/2–3/6 and 3/8. TSE 24849 (rating 2): Updated 2/41 with a more appropriate conditional. Updated the document to align with latest standards. |
| 26 |  |  | p26 |  |  | 2024-07-01 | Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication. |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Virgil Dragomir |  |  | Bluetooth SIG, Inc. |  |  |
| Alicia Courtney |  |  | Broadcom |  |  |
| Leonid Eidelman |  |  | Broadcom |  |  |
| Ash Kapur |  |  | Broadcom |  |  |
| Angel Polo |  |  | Broadcom |  |  |
| Mayank Batra |  |  | CSR |  |  |
| Chris Church |  |  | CSR |  |  |
| Giriraj Goyal |  |  | CSR |  |  |
| Robin Heydon |  |  | CSR |  |  |
| Tim Howes |  |  | CSR |  |  |
| Neil Stewart |  |  | CSR |  |  |
| Harish Balasubramaniam |  |  | Intel |  |  |
| Magnus Eriksson |  |  | Intel |  |  |
| Oren Haggai |  |  | Intel |  |  |
| Marcel Holtmann |  |  | Intel |  |  |
| Robert Hughes |  |  | Intel |  |  |
| Yao Wang |  |  | IVT |  |  |


|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
| Josselin De La Broise |  |  | Marvell |  |  |
| Anindya Bakshi |  |  | Mindtree |  |  |
| Shwetha Madadik |  |  | Mindtree |  |  |
| Krishna Singala |  |  | Mindtree |  |  |
| Niclas Granqvist |  |  | Polar |  |  |
| Joel Linsky |  |  | Qualcomm Atheros |  |  |
| Brian A. Redding |  |  | Qualcomm Atheros |  |  |
| Magnus Sommansson |  |  | Qualcomm Technologies International, Ltd. |  |  |
| Jean-Philippe Lambert |  |  | RivieraWaves |  |  |
| Rasmus Abildgren |  |  | Samsung Electronics |  |  |
| Clive Feather |  |  | Samsung Electronics |  |  |
| Jason Hillyard |  |  | Wicentric |  |  |
