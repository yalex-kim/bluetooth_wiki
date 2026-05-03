# HCI.ICS.p30

> Source: PDF converted via PyMuPDF.

---

Bluetooth® Implementation Conformance Statement (ICS) Proforma
▪ Revision: HCI.ICS.p30 ▪ Revision Date: 2024-09-04 ▪ Prepared By: BTI ▪ Published during TCRL: TCRL.2024-2
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.
THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.
This document is subject to change without notice.
Copyright © 2005–2024 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
Contents

## 1 Identification of the implementation


### 1.1 Implementation Under Test (IUT) identification

Identification of the Implementation Under Test (IUT) is to be filled in to provide as much detail as possible regarding version numbers and configuration options.
An ICS contact person to respond to queries regarding information supplied in this ICS proforma is named in the Declaration of Compliance: Summary of Selected Specifications in Implementation.

### 1.2 IUT configuration

Table 0: No longer used
Table 1a: IUT Configuration

|  | Item |  |  | Role |  |  | Reference |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | BR/EDR Controller |  |  | [1] 1 |  |  | C.0 |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  |
| 3 |  |  | AMP Controller |  |  | [1] 1 |  |  | C.0, C.901 |  |  |
| 4 |  |  | LE Controller |  |  | [1] 1 |  |  | C.0 |  |  |

C.0: Mandatory to support at least one.
C.901: Optional IF CORE 1b/52 “Controller Core v5.2 or earlier”, otherwise Excluded.

### 1.3 Capability statement

The “IUT Configuration” and “Core Version” columns used in the tables below specify prerequisites for each item. Thus, for example, table 3 item 6 (LE Request Peer SCA command) is excluded unless both HCI 1a/4 (LE Controller) and CORE 1a/52 (5.2 or later) are true. Furthermore, in those instances where either the “IUT Configuration” or “Core Version” columns do not have an entry then the item status apply to any of the IUT Controller configurations or to any of the active Core Versions.
Note that the split into tables 1 to 20 is historical and no longer is significant, therefore the tables do not have titles anymore.
Table 1

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Command Complete event |  |  | [1] 7.7.14 |  |  |  |  |  |  |  |  | M |  |  |
| 1a |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 1b |  |  | Support all BR/EDR Controller commands |  |  | [1] 3.3, 7.7 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 1c |  |  | Support all AMP Controller commands |  |  | [1] 3.3, 7.7 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | O |  |  |
| 1d |  |  | Support all LE Controller commands |  |  | [1] 3.3, 7.7 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | O |  |  |
| 2 |  |  | Command Status event |  |  | [1] 7.7.15 |  |  |  |  |  |  |  |  | M |  |  |
| 3 |  |  | Hardware Error event |  |  | [1] 7.7.16 |  |  |  |  |  |  |  |  | O |  |  |

Table 2

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Reset command |  |  | [1] 7.3.2 |  |  |  |  |  |  |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Buffer Size command |  |  | [1] 7.4.5 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 2 |  |  | Read Data Block Size command |  |  | [1] 7.4.7 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | C.124 |  |  |
| 3 |  |  | Read Flow Control Mode command |  |  | [1] 7.3.72 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | C.124 |  |  |
| 4 |  |  | Write Flow Control Mode command |  |  | [1] 7.3.73 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | C.124 |  |  |
| 5 |  |  | LE Read Buffer Size command [v1] |  |  | [1] 7.8.2 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 6 |  |  | LE Request Peer SCA command |  |  | [5] 7.8.108 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.44 |  |  |
| 7 |  |  | LE Request Peer SCA Complete event |  |  | [5] 7.7.65.31 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.95 |  |  |
| 8 |  |  | LE Read Buffer Size command [v2] |  |  | [5] 7.8.2 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.55 |  |  |
| 9 |  |  | LE Read ISO TX Sync command |  |  | [5] 7.8.96 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.45 |  |  |

C.3: Mandatory IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.5a: No longer used.
C.44: Mandatory IF LL 9/30 “Sleep Clock Accuracy Updates” AND (LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral”), otherwise Optional IF LL 9/30 “Sleep Clock Accuracy Updates”, otherwise Excluded.
C.45: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.55: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/33 “Isochronous Broadcaster”, otherwise Optional IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.95: Mandatory IF HCI 3/6 “LE Request Peer SCA command”, otherwise Excluded.
C.124: Mandatory IF HCI 14/21 “Data Block Based Flow Control”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Local Version Information command |  |  | [1] 7.4.1 |  |  |  |  |  |  |  |  | M |  |  |
| 2 |  |  | Read Local Supported Commands command |  |  | [1] 7.4.2 |  |  |  |  |  |  |  |  | M |  |  |
| 3 |  |  | Read Local Supported Features command |  |  | [1] 7.4.3 |  |  |  |  |  |  |  |  | M |  |  |
| 4 |  |  | Read Local Extended Features command |  |  | [1] 7.4.4 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.220 |  |  |
| 5 |  |  | Read BD ADDR _ command |  |  | [1] 7.4.6 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 6 |  |  | Read Local AMP Info command |  |  | [1] 7.5.8 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 7 |  |  | Read Local AMP ASSOC command |  |  | [1] 7.5.9 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 8 |  |  | LE Read Local Supported Features Page 0 command |  |  | [1] 7.8.3 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 9 |  |  | LE Read Supported States command |  |  | [1] 7.8.27 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 10 |  |  | Read Local Supported Codecs command [v1] |  |  | [1] 7.4.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.157 |  |  |
| 11 |  |  | LE Read Antenna Information command |  |  | [2] 7.8.87 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.31 |  |  |
| 12 |  |  | Read Local Simple Pairing Options command |  |  | [4] 7.4.9 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 13 |  |  | Read Local Supported Codecs command [v2] |  |  | [5] 7.4.8 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | O |  |  |
| 14 |  |  | Read Local Supported Codec Capabilities command |  |  | [5] 7.4.10 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.156 |  |  |
| 15 |  |  | Read Local Supported Controller Delay command |  |  | [1] 7.4.11 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.156 |  |  |
| 16 |  |  | AMP Status Change event |  |  | [1] 7.7.61 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 |  |  | Channel Selected event |  |  | [1] 7.7.52 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.150 |  |  |
| 18 |  |  | LE Read All Local Supported Features command |  |  | [8] 7.8.128 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.70 |  |  |

C.31: Mandatory IF LL 9/14 “Connection CTE Request” OR LL 9/15 “Connection CTE Response” OR LL 9/16 “Connectionless CTE Transmitter” OR LL 9/17 “Connectionless CTE Receiver”, otherwise Excluded.
C.70: Mandatory IF LL 9/55 “LL Extended Feature Set”, otherwise Optional.
C.150: Optional IF HCI 4/7 “Read Local AMP ASSOC command”, otherwise Excluded.
C.156: Mandatory IF HCI 4/13 “Read Local Supported Codecs command [v2]”, otherwise Excluded.
C.157: Mandatory IF HCI 4/13 “Read Local Supported Codecs command [v2]”, otherwise Optional.
C.220: Mandatory IF LMP 11/4 “Respond to extended features request”, otherwise Excluded.
Table 5

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Local Name command |  |  | [1] 7.3.12 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 2 |  |  | Write Local Name command |  |  | [1] 7.3.11 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 3 |  |  | Read Class of Device command |  |  | [1] 7.3.25 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 4 |  |  | Write Class of Device command |  |  | [1] 7.3.26 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 5 |  |  | Read Number of Supported IAC command |  |  | [1] 7.3.43 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 6 |  |  | Read Current IAC LAP command |  |  | [1] 7.3.44 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 7 |  |  | Write Current IAC LAP command |  |  | [1] 7.3.45 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 8 |  |  | Read Scan Enable command |  |  | [1] 7.3.17 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 9 |  |  | Write Scan Enable command |  |  | [1] 7.3.18 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 10 |  |  | Write Remote AMP ASSOC command |  |  | [1] 7.5.10 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 11 |  |  | Write Location Data command |  |  | [1] 7.3.71 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 12 |  |  | Read Location Data command |  |  | [1] 7.3.70 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 13 |  |  | LE Set Random Address command |  |  | [1] 7.8.4 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.1 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 |  |  | LE Read Filter Accept List Size command |  |  | [1] 7.8.14 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 15 |  |  | LE Add Device To Filter Accept List command |  |  | [1] 7.8.16 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 16 |  |  | LE Clear Filter Accept List command |  |  | [1] 7.8.15 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 17 |  |  | LE Remove Device From Filter Accept List command |  |  | [1] 7.8.17 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 18 |  |  | Set MWS Channel Parameters command |  |  | [1] 7.3.80 |  |  |  |  |  |  |  |  | O |  |  |
| 19 |  |  | Set External Frame Configuration command |  |  | [1] 7.3.81 |  |  |  |  |  |  |  |  | C.108 |  |  |
| 20 |  |  | Set MWS Signaling command |  |  | [1] 7.3.82 |  |  |  |  |  |  |  |  | O |  |  |
| 21 |  |  | Set MWS Transport Layer command |  |  | [1] 7.3.83 |  |  |  |  |  |  |  |  | C.109 |  |  |
| 22 |  |  | Set MWS Scan Frequency Table command |  |  | [1] 7.3.84 |  |  |  |  |  |  |  |  | O |  |  |
| 23 |  |  | Set MWS PATTERN _ Configuration command |  |  | [1] 7.3.85 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.136 |  |  |
| 24 |  |  | Get MWS Transport Layer Configuration command |  |  | [1] 7.5.11 |  |  |  |  |  |  |  |  | C.109 |  |  |
| 25 |  |  | Set Triggered Clock Capture command |  |  | [1] 7.5.12 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 26 |  |  | Triggered Clock Capture event |  |  | [1] 7.7.66 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.110 |  |  |
| 27 |  |  | LE Add Device To Resolving List command |  |  | [1] 7.8.38 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.9 |  |  |
| 28 |  |  | LE Remove Device From Resolving List command |  |  | [1] 7.8.39 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.9 |  |  |
| 29 |  |  | LE Clear Resolving List command |  |  | [1] 7.8.40 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.9 |  |  |
| 30 |  |  | LE Read Resolving List Size command |  |  | [1] 7.8.41 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.9 |  |  |
| 31 |  |  | LE Set Address Resolution Enable command |  |  | [1] 7.8.44 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.9 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32 |  |  | LE Set Resolvable Private Address Timeout command |  |  | [1] 7.8.45 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.9 |  |  |
| 33 |  |  | LE Set Advertising Set Random Address command |  |  | [2] 7.8.52 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 34 |  |  | LE Set Extended Advertising Parameters command [v1] |  |  | [2] 7.8.53 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.65 |  |  |
| 34a |  |  | LE Set Extended Advertising Parameters command [v2] |  |  | [2] 7.8.53 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.66 |  |  |
| 35 |  |  | LE Set Periodic Advertising Parameters command [v1] |  |  | [2] 7.8.61 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.18 |  |  |
| 35a |  |  | LE Set Periodic Advertising Parameters command [v2] |  |  | [2] 7.8.61 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.67 |  |  |
| 36 |  |  | LE Set Extended Advertising Data command |  |  | [2] 7.8.54 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 37 |  |  | LE Set Periodic Advertising Data command |  |  | [2] 7.8.62 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.18 |  |  |
| 38 |  |  | LE Set Extended Scan Response Data command |  |  | [2] 7.8.55 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 39 |  |  | LE Scan Request Received event |  |  | [2] 7.7.65.19 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 40 |  |  | LE Set Extended Advertising Enable command |  |  | [2] 7.8.56 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 41 |  |  | LE Set Periodic Advertising Enable command |  |  | [2] 7.8.63 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.18 |  |  |
| 42 |  |  | LE Read Maximum Advertising Data Length command |  |  | [2] 7.8.57 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 |  |  | LE Read Number of Supported Advertising Sets command |  |  | [2] 7.8.58 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 44 |  |  | LE Read Transmit Power command |  |  | [2] 7.8.74 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.64 |  |  |
| 45 |  |  | LE Write RF Path Compensation command |  |  | [2] 7.8.76 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.22 |  |  |
| 46 |  |  | LE Read RF Path Compensation command |  |  | [2] 7.8.75 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.22 |  |  |
| 47 |  |  | LE Remove Advertising Set command |  |  | [2] 7.8.59 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 48 |  |  | LE Clear Advertising Sets command |  |  | [2] 7.8.60 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 49 |  |  | LE Advertising Set Terminated event |  |  | [2] 7.7.65.18 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.17 |  |  |
| 50 |  |  | LE Set Connectionless CTE Transmit Parameters command |  |  | [2] 7.8.80 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.27 |  |  |
| 51 |  |  | LE Set Connectionless CTE Transmit Enable command |  |  | [2] 7.8.81 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.27 |  |  |
| 52 |  |  | LE Set Connectionless IQ Sampling Enable command |  |  | [2] 7.8.82 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.28 |  |  |
| 53 |  |  | SAM Status Change event |  |  | [2] 7.7.76 |  |  | HCI 1a/1 “BR/EDR” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.219 |  |  |
| 54 |  |  | LE Setup ISO Data Path command |  |  | [5] 7.8.109 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.47 |  |  |
| 55 |  |  | LE Remove ISO Data Path command |  |  | [2] 7.8.110 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.47 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56 |  |  | LE Set CIG Parameters command |  |  | [2] 7.8.97 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.39 |  |  |
| 57 |  |  | LE Remove CIG command |  |  | [2] 7.8.100 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.39 |  |  |
| 58 |  |  | LE Set CIG Parameters Test command |  |  | [2] 7.8.98 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.39 |  |  |
| 59 |  |  | LE Enhanced Read Transmit Power Level command |  |  | [2] 7.8.117 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.51 |  |  |
| 60 |  |  | LE Set Path Loss Reporting Parameters command |  |  | [2] 7.8.119 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.52 |  |  |
| 61 |  |  | LE Set Path Loss Reporting Enable command |  |  | [2] 7.8.120 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.52 |  |  |
| 62 |  |  | LE Transmit Power Reporting event |  |  | [2] 7.7.65.33 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.51 |  |  |
| 63 |  |  | LE Path Loss Threshold event |  |  | [2] 7.7.65.32 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.52 |  |  |
| 64 |  |  | LE Set Transmit Power Reporting Enable command |  |  | [2] 7.8.121 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.51 |  |  |
| 65 |  |  | Set Ecosystem Base Interval command |  |  | [2] 7.3.100 |  |  |  |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | O |  |  |
| 66 |  |  | Configure Data Path command |  |  | [5] 7.3.101 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.156 |  |  |
| 67 |  |  | LE Periodic Advertising Response Report event |  |  | [2] 7.7.65.37 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.67 |  |  |
| 68 |  |  | LE Periodic Advertising Subevent Data Request event |  |  | [2] 7.7.65.36 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.67 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 69 |  |  | LE Set Periodic Advertising Subevent Data command |  |  | [2] 7.8.125 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.67 |  |  |
| 70 |  |  | LE Set Decision Data command |  |  | [7] 7.8.144 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.73 |  |  |
| 71 |  |  | LE Set Decision Instructions command |  |  | [7] 7.8.145 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.74 |  |  |
| 72 |  |  | LE Add Device To Monitored Advertisers List command |  |  | [7] 7.8.146 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.78 |  |  |
| 73 |  |  | LE Remove Device From Monitored Advertisers List command |  |  | [7] 7.8.147 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.78 |  |  |
| 74 |  |  | LE Clear Monitored Advertisers List command |  |  | [7] 7.8.148 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.78 |  |  |
| 75 |  |  | LE Enable Monitoring Advertisers command |  |  | [7] 7.8.149 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.78 |  |  |
| 76 |  |  | LE Read Monitored Advertisers List Size command |  |  | [7] 7.8.150 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.78 |  |  |
| 77 |  |  | LE Monitored Advertisers Report Event |  |  | [7] 7.7.65.47 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.78 |  |  |

C.1: Mandatory IF RFPHY 1/1 “LE Transmitter” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.9: Mandatory IF LL 9/13 “LL Privacy”, otherwise Excluded.
C.17: Mandatory IF LL 3/9 “Extended Advertising”, otherwise Excluded.
C.18: Mandatory IF LL 3/10 “Periodic Advertising”, otherwise Excluded.
C.22: Mandatory IF LL 3/12 “Sending Tx Power in advertisements” OR LL 9/37 “LE Power Control Request”, otherwise Optional.
C.27: Mandatory IF LL 9/16 “Connectionless CTE Transmitter”, otherwise Excluded.
C.28: Mandatory IF LL 9/17 “Connectionless CTE Receiver”, otherwise Excluded.
C.39: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central”, otherwise Excluded.
C.47: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral”, OR LL 9/33 “Isochronous Broadcaster” OR LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.51: Mandatory IF LL 9/37 “LE Power Control Request”, otherwise Excluded.
C.52: Mandatory IF LL 9/39 “LE Path Loss Monitoring”, otherwise Excluded.
C.65: Mandatory IF HCI 5/34a “LE Set Extended Advertising Parameters command [v2]” OR LL 3/9 “Extended Advertising”, otherwise Excluded.
C.66: Mandatory IF LL 9/48 “Advertising Coding Selection“, otherwise Optional IF LL 3/9 “Extended Advertising”, otherwise Excluded.
C.67: Mandatory IF LL 3/10a “Periodic Advertising with responses”, otherwise Excluded.
C.73: Mandatory IF LL 1/1 “Advertising State” AND LL 9/51 “Decision-Based Advertising Filtering”, otherwise Excluded.
C.74: Mandatory IF LL 1/2 “Scanning State” AND LL 9/51 “Decision-Based Advertising Filtering”, otherwise Excluded.
C.78: Mandatory IF LL 9/52 “Monitoring Advertisers”, otherwise Excluded.
C.108: Mandatory IF HCI 5/23 “Set MWS_PATTERN Configuration command”, otherwise Optional.
C.109: Mandatory IF HCI 5/20 “Set MWS Signaling command”, otherwise Excluded.
C.110: Mandatory IF HCI 5/25 “Set Triggered Clock Capture command”, otherwise Excluded.
C.125: Mandatory IF BB 10/2 “Inquiry Scan with first FHS”, otherwise Excluded.
C.136: Optional IF BB 19/1 “Slot Availability Mask”, otherwise Excluded.
C.156: Mandatory IF HCI 4/13 “Read Local Supported Codecs command [v2]”, otherwise Excluded.
C.219: Mandatory IF LMP 2/29 “Slot Availability Mask”, otherwise Excluded.
Table 6

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Inquiry command |  |  | [1] 7.1.1 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.127 |  |  |
| 2 |  |  | Inquiry Cancel command |  |  | [1] 7.1.2 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.127 |  |  |
| 3 |  |  | Periodic Inquiry Mode command |  |  | [1] 7.1.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.128 |  |  |
| 4 |  |  | Exit Periodic Inquiry Mode command |  |  | [1] 7.1.4 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.103 |  |  |
| 5 |  |  | Read Inquiry Scan Activity command |  |  | [1] 7.3.21 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 6 |  |  | Write Inquiry Scan Activity command |  |  | [1] 7.3.22 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 7 |  |  | Read Inquiry Scan Type command |  |  | [1] 7.3.47 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 8 |  |  | Write Inquiry Scan Type command |  |  | [1] 7.3.48 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 9 |  |  | Read Inquiry Mode command |  |  | [1] 7.3.49 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.115 |  |  |
| 10 |  |  | Write Inquiry Mode command |  |  | [1] 7.3.50 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.146 |  |  |
| 11 |  |  | Read Inquiry Response Transmit Power Level command |  |  | [1] 7.3.61 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.125 |  |  |
| 12 |  |  | Write Inquiry Transmit Power Level command |  |  | [1] 7.3.62 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.127 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 |  |  | Read Extended Inquiry Response command |  |  | [1] 7.3.55 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.205 |  |  |
| 14 |  |  | Write Extended Inquiry Response command |  |  | [1] 7.3.56 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.205 |  |  |
| 15 |  |  | LE Set Advertising Enable command |  |  | [1] 7.8.9 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.97 |  |  |
| 16 |  |  | LE Set Advertising Parameters command |  |  | [1] 7.8.5 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.97 |  |  |
| 17 |  |  | LE Set Scan Response Data command |  |  | [1] 7.8.8 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.15 |  |  |
| 18 |  |  | LE Set Advertising Data command |  |  | [1] 7.8.7 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.97 |  |  |
| 19 |  |  | LE Advertising Report event |  |  | [1] 7.7.65.2 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.98 |  |  |
| 20 |  |  | LE Set Scan Enable command |  |  | [1] 7.8.11 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.98 |  |  |
| 21 |  |  | LE Set Scan Parameters command |  |  | [1] 7.8.10 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.98 |  |  |
| 22 |  |  | LE Read Advertising Physical Channel Tx Power command |  |  | [1] 7.8.6 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.97 |  |  |
| 23 |  |  | Inquiry Response Notification event |  |  | [1] 7.7.74 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.126 |  |  |
| 24 |  |  | Read Extended Inquiry Length command |  |  | [1] 7.3.98 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.113 |  |  |
| 25 |  |  | Write Extended Inquiry Length command |  |  | [1] 7.3.99 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.128 |  |  |
| 26 |  |  | LE Directed Advertising Report event |  |  | [1] 7.7.65.11 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.63 |  |  |
| 27 |  |  | LE Set Extended Scan Parameters command |  |  | [2] 7.8.64 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.19 |  |  |
| 28 |  |  | LE Set Extended Scan Enable command |  |  | [2] 7.8.65 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.19 |  |  |
| 29 |  |  | LE Extended Advertising Report event |  |  | [2] 7.7.65.13 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.19 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30 |  |  | LE Periodic Advertising Create Sync command |  |  | [2] 7.8.67 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.16 |  |  |
| 31 |  |  | LE Periodic Advertising Create Sync Cancel command |  |  | [2] 7.8.68 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.16 |  |  |
| 32 |  |  | LE Periodic Advertising Terminate Sync command |  |  | [2] 7.8.69 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |
| 33 |  |  | LE Periodic Advertising Report event [v1] |  |  | [2] 7.7.65.15 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |
| 33a |  |  | LE Periodic Advertising Report event [v2] |  |  | [2] 7.7.65.15 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.68 |  |  |
| 34 |  |  | LE Periodic Advertising Sync Lost event |  |  | [2] 7.7.65.16 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |
| 35 |  |  | LE Periodic Advertising Sync Established event [v1] |  |  | [2] 7.7.65.14 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.16 |  |  |
| 35a |  |  | LE Periodic Advertising Sync Established event [v2] |  |  | [2] 7.7.65.14 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.68 |  |  |
| 36 |  |  | LE Scan Timeout event |  |  | [2] 7.7.65.17 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.19 |  |  |
| 37 |  |  | LE Set Periodic Advertising Receive Enable command |  |  | [3] 7.8.88 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.32 |  |  |
| 38 |  |  | LE BIG Create Sync command |  |  | [5] 7.8.106 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.42 |  |  |
| 39 |  |  | LE BIG Sync Established event |  |  | [2] 7.7.65.29 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.42 |  |  |
| 40 |  |  | LE Terminate BIG command |  |  | [2] 7.8.105 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.41 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41 |  |  | LE BIG Sync Lost event |  |  | [2] 7.7.65.30 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.42 |  |  |
| 42 |  |  | LE BIG Terminate Sync command |  |  | [2] 7.8.107 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.42 |  |  |
| 43 |  |  | LE Terminate BIG Complete event |  |  | [2] 7.7.65.28 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.41 |  |  |
| 44 |  |  | LE BIGInfo Advertising Report event |  |  | [2] 7.7.65.34 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.54 |  |  |
| 45 |  |  | Inquiry Result event |  |  | [2] 7.7.2 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.127 |  |  |
| 46 |  |  | Extended Inquiry Result event |  |  | [2] 7.7.38 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.147 |  |  |
| 47 |  |  | Inquiry Result with RSSI event |  |  | [2] 7.7.33 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.128 |  |  |
| 48 |  |  | Inquiry Complete event |  |  | [2] 7.7.1 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.127 |  |  |
| 49 |  |  | Page Scan Repetition Mode Change event |  |  | [2] 7.7.31 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 50 |  |  | LE Set Periodic Sync Subevent command |  |  | [2] 7.8.127 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.68 |  |  |
| 51 |  |  | LE Set Periodic Advertising Response Data command |  |  | [2] 7.8.126 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.68 |  |  |

C.15: Mandatory IF LL 3/2 “Connectable and scannable undirected events” OR LL 3/5 “Scannable undirected events” OR LL 3/5a “Scannable directed events”, otherwise Excluded.
C.16: Mandatory IF LL 4/8 “Scanning for Periodic Advertising” AND LL 1/3a “Synchronized State”, otherwise Excluded.
C.19: Mandatory IF LL 4/7 “Extended Scanning”, otherwise Excluded.
C.21: Mandatory IF LL 11/1 “Synchronizing to Periodic Advertising”, otherwise Excluded.
C.32: Mandatory IF LL 9/27 “Periodic Advertising Sync Transfer - Recipient”, otherwise Optional IF LL 11/1 “Synchronizing to Periodic Advertising”, otherwise Excluded.
C.41: Mandatory IF LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.42: Mandatory IF LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.54: Mandatory IF LL 9/34 “Synchronized Receiver”, otherwise Optional.
C.63: Mandatory IF LL 1/2 “Scanning State” AND LL 9/13 “LL Privacy”, otherwise Excluded.
C.68: Mandatory IF LL 4/8a “Scanning for Periodic Advertising with Responses”, otherwise Excluded.
C.97: Mandatory IF LL 1/1 “Advertising State”, otherwise Excluded.
C.98: Mandatory IF LL 1/2 “Scanning State”, otherwise Excluded.
C.113: Mandatory IF HCI 6/25 “Write Extended Inquiry Length command”, otherwise Excluded.
C.115: Mandatory IF HCI 6/10 “Write Inquiry Mode command”, otherwise Excluded.
C.125: Mandatory IF BB 10/2 “Inquiry Scan with first FHS”, otherwise Excluded.
C.126: Optional IF BB 10/2 “Inquiry Scan with first FHS”, otherwise Excluded.
C.127: Mandatory IF BB 10/1 “Inquiry”, otherwise Excluded.
C.128: Optional IF BB 10/1 “Inquiry”, otherwise Excluded.
C.146: Mandatory IF HCI 6/46 “Extended Inquiry Result event” OR HCI 16/54 “IO Capability Request
event”, otherwise Optional IF BB 10/1 “Inquiry”, otherwise Excluded.
C.147: Optional IF HCI 6/47 “Inquiry Result with RSSI event”, otherwise Excluded.
C.205: Mandatory IF BB 10/7 “Extended Inquiry Response”, otherwise Excluded.
Table 7

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Create Connection command |  |  | [1] 7.1.5 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 2 |  |  | Accept Connection Request command |  |  | [1] 7.1.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 3 |  |  | Reject Connection Request command |  |  | [1] 7.1.9 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 4 |  |  | Create Connection Cancel command |  |  | [1] 7.1.7 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 5 |  |  | Disconnect command |  |  | [1] 7.1.6 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  |  |  |  | C.3b |  |  |
| 6 |  |  | Read Page Timeout command |  |  | [1] 7.3.15 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 7 |  |  | Write Page Timeout command |  |  | [1] 7.3.16 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 8 |  |  | Read Page Scan Activity command |  |  | [1] 7.3.19 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 9 |  |  | Write Page Scan Activity command |  |  | [1] 7.3.20 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 10 |  |  | Read Page Scan Type command |  |  | [1] 7.3.51 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.119 |  |  |
| 11 |  |  | Write Page Scan Type command |  |  | [1] 7.3.52 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.154 |  |  |
| 12 |  |  | Read Connection Accept Timeout command |  |  | [1] 7.3.13 |  |  |  |  |  |  |  |  | C.40a |  |  |
| 13 |  |  | Write Connection Accept Timeout command |  |  | [1] 7.3.14 |  |  |  |  |  |  |  |  | C.40a |  |  |
| 14 |  |  | Create Physical Link command |  |  | [1] 7.1.37 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 |  |  | Accept Physical Link command |  |  | [1] 7.1.38 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 16 |  |  | Disconnect Physical Link command |  |  | [1] 7.1.39 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 17 |  |  | Create Logical Link command |  |  | [1] 7.1.40 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 18 |  |  | Accept Logical Link command |  |  | [1] 7.1.41 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 19 |  |  | Disconnect Logical Link command |  |  | [1] 7.1.42 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 20 |  |  | Logical Link Cancel command |  |  | [1] 7.1.43 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 21 |  |  | Read Logical Link Accept Timeout command |  |  | [1] 7.3.67 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 22 |  |  | Write Logical Link Accept Timeout command |  |  | [1] 7.3.68 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 23 |  |  | LE Create Connection command |  |  | [1] 7.8.12 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.59 |  |  |
| 24 |  |  | LE Create Connection Cancel command |  |  | [1] 7.8.13 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.94 |  |  |
| 25 |  |  | LE Connection Complete event |  |  | [1] 7.7.65.1 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 26 |  |  | Disconnection Complete event |  |  | [1] 7.7.5 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/4 “LE” |  |  |  |  |  | C.3b |  |  |
| 27 |  |  | LE Connection Update command |  |  | [1] 7.8.18 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.62 |  |  |
| 28 |  |  | LE Connection Update Complete event |  |  | [1] 7.7.65.3 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 29 |  |  | Truncated Page command |  |  | [1] 7.1.47 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.129 |  |  |
| 30 |  |  | Truncated Page Cancel command |  |  | [1] 7.1.48 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.129 |  |  |
| 31 |  |  | Truncated Page Complete event |  |  | [1] 7.7.71 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.129 |  |  |
| 32 |  |  | Peripheral Page Response Timeout event |  |  | [1] 7.7.72 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 33 |  |  | Read Extended Page Timeout command |  |  | [1] 7.3.96 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.114 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 34 |  |  | Write Extended Page Timeout command |  |  | [1] 7.3.97 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 35 |  |  | LE Remote Connection Parameter Request Reply command |  |  | [1] 7.8.31 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.6 |  |  |
| 36 |  |  | LE Remote Connection Parameter Request Negative Reply command |  |  | [1] 7.8.32 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.6 |  |  |
| 37 |  |  | LE Remote Connection Parameter Request event |  |  | [1] 7.7.65.6 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.6 |  |  |
| 38 |  |  | LE Enhanced Connection Complete event [v1] |  |  | [1] 7.7.65.10 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.24 |  |  |
| 38a |  |  | LE Enhanced Connection Complete event [v2] |  |  | [2] 7.7.65.10 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.69 |  |  |
| 39 |  |  | LE Read Peer Resolvable Address command |  |  | [1] 7.8.42 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.10 |  |  |
| 40 |  |  | LE Read Local Resolvable Address command |  |  | [1] 7.8.43 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.10 |  |  |
| 41 |  |  | LE Extended Create Connection command [v1] |  |  | [2] 7.8.66 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.20 |  |  |
| 41a |  |  | LE Extended Create Connection command [v2] |  |  | [2] 7.8.66 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.67 |  |  |
| 42 |  |  | LE Channel Selection Algorithm event |  |  | [2] 7.7.65.20 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.23 |  |  |
| 43 |  |  | LE Set Privacy Mode command |  |  | [2] 7.8.77 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.9 |  |  |
| 44 |  |  | Connection Request event |  |  | [1] 7.7.4 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45 |  |  | Connection Complete event |  |  | [1] 7.7.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 46 |  |  | Physical Link Complete event |  |  | [1] 7.7.51 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 47 |  |  | Logical Link Complete event |  |  | [1] 7.7.56 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 48 |  |  | Disconnection Physical Link Complete event |  |  | [1] 7.7.53 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 49 |  |  | Disconnection Logical Link Complete event |  |  | [1] 7.7.57 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 50 |  |  | LE Default Subrate Request command |  |  | [6] 7.8.123 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | C.57 |  |  |
| 51 |  |  | LE Subrate Request command |  |  | [6] 7.8.124 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | C.57 |  |  |
| 52 |  |  | LE Subrate Change event |  |  | [6] 7.7.65.35 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | C.57 |  |  |

C.3: Mandatory IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.3b: Mandatory IF HCI 1a/1 “BR/EDR Controller” OR LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.6: Mandatory IF LL 9/3 “Connection Parameters Request procedure”, otherwise Excluded.
C.9: Mandatory IF LL 9/13 “LL Privacy”, otherwise Excluded.
C.10: Optional IF LL 9/13 “LL Privacy”, otherwise Excluded.
C.20: Mandatory IF LL 5/4 “Requesting connections using extended advertising”, otherwise Excluded.
C.23: Mandatory IF LL 9/10 “Channel Selection Algorithm #2”, otherwise Excluded.
C.24: Mandatory IF (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”) AND (LL 9/13 “LL Privacy” OR LL 5/4 “Requesting connections using extended advertising”), otherwise Optional IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.40a: Mandatory IF HCI 1a/1 “BR/EDR Controller” OR HCI 1a/3 “AMP Controller” OR LL 9/32
“Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.57: Mandatory IF LL 9/45 “Connection Subrating”, otherwise Excluded.
C.59: Mandatory IF LL 1/5 “Central Role”, otherwise Excluded.
C.62: Mandatory IF LL 1/5 “Central Role” OR (LL 1/4 “Peripheral Role” AND LL 9/3 “Connection Parameters Request procedure”), otherwise Excluded.
C.67: Mandatory IF LL 3/10a “Periodic Advertising with responses”, otherwise Excluded.
C.69: Mandatory IF LL 3/10a “Periodic Advertising with responses” OR LL 4/8a “Scanning for Periodic Advertising with Responses”, otherwise Excluded.
C.94: Mandatory IF HCI 7/23 “LE Create Connection command” OR HCI 7/41 “LE Extended Create Connection command [v1]”, otherwise Excluded.
C.119: Mandatory IF HCI 7/11 “Write Page Scan Type command”, otherwise Excluded.
C.129: Mandatory IF BB 7/6 “Truncated Paging”, otherwise Excluded.
C.154: Mandatory IF BB 7/5 “Interlaced Scan during Page Scan”, otherwise Optional.
Table 8

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Remote Name Request command |  |  | [1] 7.1.19 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 2 |  |  | Remote Name Request Cancel command |  |  | [1] 7.1.20 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.106 |  |  |
| 3 |  |  | Read Remote Supported Features command |  |  | [1] 7.1.21 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 4 |  |  | Read Remote Extended Features command |  |  | [1] 7.1.22 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.220 |  |  |
| 5 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 5a |  |  | Read Remote Version Information command on BR/EDR |  |  | [1] 7.1.23 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 5b |  |  | Read Remote Version Information command on LE |  |  | [1] 7.1.23 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 6 |  |  | LE Read Remote Features Page 0 command |  |  | [1] 7.8.21 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 7 |  |  | LE Read Remote Features Page 0 Complete event |  |  | [1] 7.7.65.4 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 8 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 8a |  |  | Read Remote Version Information Complete event on BR/EDR |  |  | [1] 7.7.12 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.105 |  |  |
| 8b |  |  | Read Remote Version Information Complete event on LE |  |  | [1] 7.7.12 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 9 |  |  | LE Connectionless IQ Report event |  |  | [2] 7.7.65.21 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.28 |  |  |
| 10 |  |  | LE Read Remote Transmit Power Level command |  |  | [2] 7.8.118 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.51 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 |  |  | Read Remote Extended Features Complete event |  |  | [1] 7.7.34 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.220 |  |  |
| 12 |  |  | Read Remote Supported Features Complete event |  |  | [1] 7.7.11 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 13 |  |  | Remote Host Supported Features Notification event |  |  | [1] 7.7.50 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.106 |  |  |
| 14 |  |  | Remote Name Request Complete event |  |  | [1] 7.7.7 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.106 |  |  |
| 15 |  |  | LE Read All Remote Features command |  |  | [8] 7.8.129 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.71 |  |  |
| 16 |  |  | LE Read All Remote Features Complete event |  |  | [8] 7.7.65.38 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.72 |  |  |

C.3: Mandatory IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.28: Mandatory IF LL 9/17 “Connectionless CTE Receiver”, otherwise Excluded.
C.51: Mandatory IF LL 9/37 “LE Power Control Request”, otherwise Excluded.
C.71: Mandatory IF (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”) AND LL 9/55 “LL Extended Feature Set”, otherwise Optional IF (LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”), otherwise Excluded.
C.72: Mandatory IF HCI 8/15 “LE Read All Remote Features command”, otherwise Excluded.
C.105: Mandatory IF HCI 8/5a “Read Remote Version Information command on BR/EDR”, otherwise
Excluded.
C.106: Mandatory IF HCI 8/1 “Remote Name Request command”, otherwise Excluded.
C.220: Mandatory IF LMP 11/4 “Respond to extended features request”, otherwise Excluded.
Table 9

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Setup Synchronous Connection command |  |  | [1] 7.1.26 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |
| 2 |  |  | Accept Synchronous Connection Request command |  |  | [1] 7.1.27 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |
| 3 |  |  | Reject Synchronous Connection Request command |  |  | [1] 7.1.28 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |
| 4 |  |  | Read Voice Setting command |  |  | [1] 7.3.27 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |
| 5 |  |  | Write Voice Setting command |  |  | [1] 7.3.28 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 |  |  | SCO data via HCI |  |  | [1] 5.4.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.902 |  |  |
| 7 |  |  | eSCO data via HCI |  |  | [1] 5.4.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.903 |  |  |
| 8 |  |  | Write Default Erroneous Data Reporting command |  |  | [1] 7.3.65 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.206 |  |  |
| 9 |  |  | Read Default Erroneous Data Reporting command |  |  | [1] 7.3.64 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.112 |  |  |
| 10 |  |  | Enhanced Setup Synchronous Connection command |  |  | [1] 7.1.45 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.135 |  |  |
| 11 |  |  | Enhanced Accept Synchronous Connection Request command |  |  | [1] 7.1.46 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.135 |  |  |
| 12 |  |  | Synchronous Connection Complete event |  |  | [1] 7.7.35 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |
| 13 |  |  | Synchronous Connection Changed event |  |  | [1] 7.7.36 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |

C.112: Mandatory IF HCI 9/8 “Write Default Erroneous Data Reporting command”, otherwise Excluded.
C.134: Mandatory IF BB 2/2 “SCO link” OR BB 2/3 “eSCO link”, otherwise Excluded.
C.135: Optional IF BB 2/2 “SCO link” OR BB 2/3 “eSCO link”, otherwise Excluded.
C.206: Mandatory IF BB 14/1 “Erroneous Data Reporting for SCO” OR BB 14/2 “Erroneous Data
Reporting for eSCO”, otherwise Excluded.
C.902: Optional IF BB 2/2 “SCO link”, otherwise Excluded.
C.903: Optional IF BB 2/3 “eSCO link”, otherwise Excluded.
Table 10

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Hold Mode command |  |  | [1] 7.2.1 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.213 |  |  |
| 2 |  |  | Sniff Mode command |  |  | [1] 7.2.2 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.214 |  |  |
| 3 |  |  | Exit Sniff Mode command |  |  | [1] 7.2.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.214 |  |  |
| 4–5 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 6 |  |  | Read Link Policy Settings command |  |  | [1] 7.2.9 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.141 |  |  |
| 7 |  |  | Write Link Policy Settings command |  |  | [1] 7.2.10 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.141 |  |  |
| 8 |  |  | Read Default Link Policy Settings command |  |  | [1] 7.2.11 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.141 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 |  |  | Write Default Link Policy Settings command |  |  | [1] 7.2.12 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.141 |  |  |
| 10 |  |  | Read Hold Mode Activity command |  |  | [1] 7.3.33 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.213 |  |  |
| 11 |  |  | Write Hold Mode Activity command |  |  | [1] 7.3.34 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.213 |  |  |
| 12 |  |  | LE Set Data Length command |  |  | [1] 7.8.33 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.8 |  |  |
| 13 |  |  | LE Data Length Change event |  |  | [1] 7.7.65.7 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.8 |  |  |
| 14 |  |  | LE Read Suggested Default Data Length command |  |  | [1] 7.8.34 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.8 |  |  |
| 15 |  |  | LE Write Suggested Default Data Length command |  |  | [1] 7.8.35 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.8 |  |  |
| 16 |  |  | LE Read Maximum Data Length command |  |  | [1] 7.8.46 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.8 |  |  |
| 17 |  |  | Short Range Mode command |  |  | [1] 7.3.77 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.131 |  |  |
| 18 |  |  | LE Set Connection CTE Receive Parameters command |  |  | [2] 7.8.83 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.25 |  |  |
| 19 |  |  | LE Set Connection CTE Transmit Parameters command |  |  | [2] 7.8.84 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.26 |  |  |
| 20 |  |  | LE Connection CTE Request Enable command |  |  | [2] 7.8.85 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.25 |  |  |
| 21 |  |  | LE Connection CTE Response Enable command |  |  | [2] 7.8.86 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.26 |  |  |
| 22 |  |  | LE Connection IQ Report event |  |  | [2] 7.7.65.22 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.25 |  |  |
| 23 |  |  | LE CTE Request Failed event |  |  | [2] 7.7.65.23 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.25 |  |  |
| 24 |  |  | LE Periodic Advertising Sync Transfer command |  |  | [3] 7.8.89 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.33 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25 |  |  | LE Periodic Advertising Set Info Transfer command |  |  | [3] 7.8.90 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.34 |  |  |
| 26 |  |  | LE Periodic Advertising Sync Transfer Received event [v1] |  |  | [3] 7.7.65.24 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.35 |  |  |
| 26a |  |  | LE Periodic Advertising Sync Transfer Received event [v2] |  |  | [3] 7.7.65.24 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/54 “Controller Core v5.4 or later” |  |  | C.68 |  |  |
| 27 |  |  | LE Set Periodic Advertising Sync Transfer Parameters command |  |  | [3] 7.8.91 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.35 |  |  |
| 28 |  |  | LE Set Default Periodic Advertising Sync Transfer Parameters command |  |  | [3] 7.8.92 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.35 |  |  |
| 29 |  |  | LE Modify Sleep Clock Accuracy command |  |  | [3] 7.8.94 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.37 |  |  |
| 30 |  |  | LE Create CIS command |  |  | [5] 7.8.99 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.39 |  |  |
| 31 |  |  | LE CIS Established event [v1] |  |  | [5] 7.7.65.25 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.38 |  |  |
| 31a |  |  | LE CIS Established event [v2] |  |  | [5] 7.7.65.25 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.159 |  |  |
| 32 |  |  | LE CIS Request event |  |  | [5] 7.7.65.26 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.40 |  |  |
| 33 |  |  | LE Accept CIS Request command |  |  | [5] 7.8.101 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.40 |  |  |
| 34 |  |  | LE Reject CIS Request command |  |  | [5] 7.8.102 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.40 |  |  |
| 35 |  |  | Max Slots Change event |  |  | [1] 7.7.27 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.132 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 |  |  | Mode Change event |  |  | [1] 7.7.20 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.144 |  |  |
| 37 |  |  | Role Change event |  |  | [1] 7.7.18 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.212 |  |  |
| 38 |  |  | Connection Packet Type Changed event |  |  | [1] 7.7.29 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.133 |  |  |
| 39 |  |  | Short Range Mode Change Complete event |  |  | [1] 7.7.60 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.131 |  |  |
| 40 |  |  | LE Set Data Related Address Changes command |  |  | [1] 7.8.122 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | C.10 |  |  |

C.8: Mandatory IF LL 9/6 “LE Data Packet Length Extension”, otherwise Optional.
C.10: Optional IF LL 9/13 “LL Privacy”, otherwise Excluded.
C.25: Mandatory IF LL 9/14 “Connection CTE Request”, otherwise Excluded.
C.26: Mandatory IF LL 9/15 “Connection CTE Response”, otherwise Excluded.
C.33: Mandatory IF LL 9/26 “Periodic Advertising Sync Transfer - Sender” AND LL 1/2 “Scanning State”, otherwise Excluded.
C.34: Mandatory IF LL 9/26 “Periodic Advertising Sync Transfer - Sender” AND LL 1/1 “Advertising State”, otherwise Excluded.
C.35: Mandatory IF LL 9/27 “Periodic Advertising Sync Transfer - Recipient”, otherwise Excluded.
C.37: Mandatory IF LL 9/40 “Can Change Sleep Clock Accuracy”, otherwise Excluded.
C.38: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.39: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central”, otherwise Excluded.
C.40: Mandatory IF LL 9/32 “Connected Isochronous Stream - Peripheral”, otherwise Excluded.
C.68: Mandatory IF LL 4/8a “Scanning for Periodic Advertising with Responses”, otherwise Excluded.
C.131: Mandatory IF 80211PAL 1/11 “Short Range Mode”, otherwise Excluded.
C.132: Mandatory IF BB 5/2 “DM3 packet type” OR BB 5/3 “DH3 packet type” OR BB 5/4 “DM5 packet
type” OR BB 5/5 “DH5 packet type” OR LMP 2b/2 “EDR for asynchronous transports (multi-slot)”, otherwise Excluded.
C.133: Mandatory IF BB 5/2 “DM3 packet type” OR BB 5/3 “DH3 packet type” OR BB 5/4 “DM5 packet
type” OR BB 5/5 “DH5 packet type” OR BB 6/2 “HV2 packet type” OR BB 6/3 “HV3 packet type” OR BB 2/4 “Enhanced Data Rate ACL links”, otherwise Excluded.
C.141: Mandatory IF LMP 2/6 “Role switch” OR LMP 2/7 “Hold mode” OR LMP 2/8 “Sniff mode”,
otherwise Excluded.
C.144: Mandatory IF LMP 2/7 “Hold mode” OR LMP 2/8 “Sniff mode”, otherwise Excluded.
C.159: Optional IF HCI 10/31 “LE CIS Established event [v1]”, otherwise Excluded.
C.212: Mandatory IF LMP 2/6 “Role switch”, otherwise Excluded.
C.213: Mandatory IF LMP 2/7 “Hold mode”, otherwise Excluded.
C.214: Mandatory IF LMP 2/8 “Sniff mode”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Role Discovery command |  |  | [1] 7.2.7 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 2 |  |  | Switch Role command |  |  | [1] 7.2.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.212 |  |  |

C.212: Mandatory IF LMP 2/6 “Role switch”, otherwise Excluded.
Table 12

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Flow Specification command |  |  | [1] 7.2.13 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 2 |  |  | QoS Setup command |  |  | [1] 7.2.6 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 3 |  |  | Flush command |  |  | [1] 7.3.4 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 4 |  |  | Read Automatic Flush Timeout command |  |  | [1] 7.3.29 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 5 |  |  | Write Automatic Flush Timeout command |  |  | [1] 7.3.30 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 6 |  |  | Read Failed Contact Counter command |  |  | [1] 7.5.1 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 7 |  |  | Reset Failed Contact Counter command |  |  | [1] 7.5.2 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 8 |  |  | Read Num Broadcast Retransmissions command |  |  | [1] 7.3.31 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.118 |  |  |
| 9 |  |  | Write Num Broadcast Retransmissions command |  |  | [1] 7.3.32 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 10 |  |  | Enhanced Flush command |  |  | [1] 7.3.66 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 11–16 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 17 |  |  | Sniff Subrating command |  |  | [1] 7.2.14 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.221 |  |  |
| 18 |  |  | Sniff Subrating event |  |  | [1] 7.7.37 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.221 |  |  |
| 19 |  |  | Flow Spec Modify command |  |  | [1] 7.1.44 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 20 |  |  | Read Best Effort Flush Timeout command |  |  | [1] 7.3.75 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 21 |  |  | Write Best Effort Flush Timeout command |  |  | [1] 7.3.76 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 22 |  |  | Flush Occurred event |  |  | [1] 7.7.17 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 23 |  |  | Enhanced Flush Complete event |  |  | [1] 7.7.47 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 24 |  |  | Flow Specification Complete event |  |  | [1] 7.7.32 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |


| Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25 |  | Flow Spec Modify Complete event |  |  | [1] 7.7.58 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 26 |  | QoS Setup Complete event |  |  | [1] 7.7.13 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 27 |  | QoS Violation event |  |  | [1] 7.7.30 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |

C.118: Mandatory IF HCI 12/9 “Write Num Broadcast Retransmissions command”, otherwise Excluded.
C.221: Mandatory IF LMP 16/7 “Sniff Subrating Mode”, otherwise Excluded.
Table 13

| Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 1a |  | Read Link Supervision Timeout command on BR/EDR |  |  | [1] 7.3.41 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.117 |  |  |
| 1b |  | Read Link Supervision Timeout command on AMP |  |  | [1] 7.3.41 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 2 |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 2a |  | Write Link Supervision Timeout command on BR/EDR |  |  | [1] 7.3.42 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 2b |  | Write Link Supervision Timeout command on AMP |  |  | [1] 7.3.42 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | M |  |  |
| 3 |  | Read AFH Channel Assessment Mode command |  |  | [1] 7.3.53 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.140 |  |  |
| 3a |  | Read AFH Channel Assessment Mode command |  |  | [6] 7.3.53 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | C.58 |  |  |
| 4 |  | Write AFH Channel Assessment Mode command |  |  | [1] 7.3.54 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.140 |  |  |
| 4a |  | Write AFH Channel Assessment Mode command |  |  | [6] 7.3.54 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | C.58 |  |  |
| 5 |  | Set AFH Host Channel Classification command |  |  | [1] 7.3.46 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.140 |  |  |
| 6 |  | Change Connection Packet Type command |  |  | [1] 7.1.14 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.133 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 |  |  | Link Supervision Timeout Changed event |  |  | [1] 7.7.46 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 8 |  |  | LE Set Host Channel Classification command |  |  | [1] 7.8.19 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.36 |  |  |
| 9 |  |  | LE Read PHY command |  |  | [2] 7.8.47 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.11 |  |  |
| 10 |  |  | LE Set Default PHY command |  |  | [2] 7.8.48 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.11 |  |  |
| 11 |  |  | LE Set PHY command |  |  | [2] 7.8.49 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.11 |  |  |
| 12 |  |  | LE PHY Update Complete event |  |  | [2] 7.7.65.12 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.11 |  |  |
| 13 |  |  | Physical Link Loss Early Warning event |  |  | [1] 7.7.54 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | O |  |  |
| 14 |  |  | Physical Link Recovery event |  |  | [1] 7.7.55 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.149 |  |  |
| 15 |  |  | LE Frame Space Update command |  |  | [8] 7.8.151 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.79 |  |  |
| 16 |  |  | LE Frame Space Update Complete event |  |  | [8] 7.7.65.48 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” |  |  | C.79 |  |  |

C.11: Mandatory IF LL 9/6a “Multiple PHYs”, otherwise Optional.
C.36: Mandatory IF LL 9/44 “Channel Classification” OR LL 1/5 “Central Role”, otherwise Optional IF (LL 9/41 “LE Extended Advertising” AND LL 1/1 “Advertising State”) OR LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.58: Mandatory IF LL 9/44 “Channel Classification”, otherwise Excluded.
C.79: Mandatory IF LL 9/54 “Frame Space Update”, otherwise Excluded.
C.117: Mandatory IF HCI 13/2a “Write Link Supervision Timeout command on BR/EDR”, otherwise
Excluded.
C.133: Mandatory IF BB 5/2 “DM3 packet type” OR BB 5/3 “DH3 packet type” OR BB 5/4 “DM5 packet
type” OR BB 5/5 “DH5 packet type” OR BB 6/2 “HV2 packet type” OR BB 6/3 “HV3 packet type” OR BB 2/4 “Enhanced Data Rate ACL links”, otherwise Excluded.
C.140: Mandatory IF LMP 26/1 “Support of AFH switch as Central” OR LMP 26/6 “Support of Channel
Classification”, otherwise Excluded.
C.149: Optional IF HCI 13/13 “Physical Link Loss Early Warning event”, otherwise Excluded.

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Host Buffer Size command |  |  | [1] 7.3.39 |  |  |  |  |  |  |  |  | C.107 |  |  |
| 2 |  |  | Set Event Mask command |  |  | [1] 7.3.1 |  |  |  |  |  |  |  |  | M |  |  |
| 3 |  |  | Set Event Filter command |  |  | [1] 7.3.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.148 |  |  |
| 4 |  |  | Set Controller to Host Flow Control command |  |  | [1] 7.3.38 |  |  |  |  |  |  |  |  | C.96a |  |  |
| 5 |  |  | Host Number of Completed Packets command |  |  | [1] 7.3.40 |  |  |  |  |  |  |  |  | C.107 |  |  |
| 6 |  |  | Read Synchronous Flow Control Enable command |  |  | [1] 7.3.36 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.122 |  |  |
| 7 |  |  | Write Synchronous Flow Control Enable command |  |  | [1] 7.3.37 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.135 |  |  |
| 8 |  |  | Set Event Mask Page 2 command |  |  | [1] 7.3.69 |  |  |  |  |  |  |  |  | O |  |  |
| 9–11 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 12 |  |  | Number of Completed Packets event |  |  | [1] 7.7.19 |  |  |  |  |  |  |  |  | C.3a |  |  |
| 13 |  |  | Data Buffer Overflow event |  |  | [1] 7.7.26 |  |  |  |  |  |  |  |  | O |  |  |
| 14 |  |  | LE Set Event Mask command |  |  | [1] 7.8.1 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 15 |  |  | Read LE Host Support command |  |  | [1] 7.3.78 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.116 |  |  |
| 16 |  |  | Write LE Host Support command |  |  | [1] 7.3.79 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.153 |  |  |
| 17 |  |  | LE Add Device To Periodic Advertiser List command |  |  | [2] 7.8.70 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |
| 18 |  |  | LE Remove Device From Periodic Advertiser List command |  |  | [2] 7.8.71 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |
| 19 |  |  | LE Clear Periodic Advertiser List command |  |  | [2] 7.8.72 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |
| 20 |  |  | LE Read Periodic Advertiser List Size command |  |  | [2] 7.8.73 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.21 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21 |  |  | Data Block Based Flow Control |  |  | [1] 4.1.2 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | O |  |  |
| 22 |  |  | Number of Completed Data Blocks event |  |  | [1] 7.7.59 |  |  | HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP” |  |  |  |  |  | C.124 |  |  |
| 23 |  |  | Separate BR/EDR and LE Data Buffers |  |  | [1] 1.1 |  |  | (HCI 1a/1 “BR/EDR” OR HCI 1a/3 “AMP”) AND HCI 1a/4 “LE” |  |  |  |  |  | O |  |  |

C.3a: Mandatory IF HCI 1a/1 “BR/EDR Controller” OR HCI 1a/3 “AMP Controller” OR LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.21: Mandatory IF LL 11/1 “Synchronizing to Periodic Advertising”, otherwise Excluded.
C.96a: Optional IF HCI 1a/1 “BR/EDR Controller” OR HCI 1a/3 “AMP Controller” OR LL 1/4 “Peripheral
Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.107: Mandatory IF HCI 14/4 “Set Controller to Host Flow Control command”, otherwise Excluded.
C.116: Mandatory IF HCI 14/16 “Write LE Host Support command”, otherwise Excluded.
C.122: Mandatory IF HCI 14/7 “Write Synchronous Flow Control Enable command”, otherwise Excluded.
C.124: Mandatory IF HCI 14/21 “Data Block Based Flow Control”, otherwise Excluded.
C.135: Optional IF BB 2/2 “SCO link” OR BB 2/3 “eSCO link”, otherwise Excluded.
C.148: Optional IF HCI 7/45 “Connection Complete event” OR HCI 7/44 “Connection Request event” OR
HCI 6/46 “Extended Inquiry Result event” OR HCI 6/47 “Inquiry Result with RSSI event” OR HCI 16/54 “IO Capability Request event” OR HCI 9/12 “Synchronous Connection Complete event”, otherwise Excluded.
C.153: Mandatory IF HCI 1a/4 “LE Controller”, otherwise Optional.
Table 15

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read LMP Handle command |  |  | [1] 7.1.25 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.134 |  |  |
| 2 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 2a |  |  | Read Enhanced Transmit Power Level command |  |  | [1] 7.3.74 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.217 |  |  |
| 2b |  |  | Read Transmit Power Level command on BR/EDR |  |  | [1] 7.3.35 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.152 |  |  |
| 2c |  |  | Read Transmit Power Level command on LE |  |  | [1] 7.3.35 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 3a |  |  | Read Link Quality command on BR/EDR |  |  | [1] 7.5.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 3b |  |  | Read Link Quality command on AMP |  |  | [1] 7.5.3 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | O |  |  |
| 4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 4a |  |  | Read RSSI command on BR/EDR |  |  | [1] 7.5.4 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4b |  |  | Read RSSI command on AMP |  |  | [1] 7.5.4 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | O |  |  |
| 4c |  |  | Read RSSI command on LE |  |  | [1] 7.5.4 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 5 |  |  | Read Clock Offset command |  |  | [1] 7.1.24 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 6 |  |  | Read Clock command |  |  | [1] 7.5.6 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 7 |  |  | Read AFH Channel Map command |  |  | [1] 7.5.5 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.139 |  |  |
| 8 |  |  | LE Read Channel Map command |  |  | [1] 7.8.20 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.3 |  |  |
| 9 |  |  | LE Read ISO Link Quality command |  |  | [5] 7.8.116 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.50 |  |  |
| 10 |  |  | Read Clock Offset Complete event |  |  | [1] 7.7.28 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.104 |  |  |

C.3: Mandatory IF LL 1/4 “Peripheral Role” OR LL 1/5 “Central Role”, otherwise Excluded.
C.50: Optional IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.104: Mandatory IF HCI 15/5 “Read Clock Offset command”, otherwise Excluded.
C.134: Mandatory IF BB 2/2 “SCO link” OR BB 2/3 “eSCO link”, otherwise Excluded.
C.139: Mandatory IF LMP 26/1 “Support of AFH switch as Central” OR LMP 26/2 “Support of AFH switch
as Peripheral”, otherwise Excluded.
C.152: Mandatory IF LMP 2/10 “Power Control”, otherwise Optional.
C.217: Mandatory IF LMP 2/20 “Enhanced Power Control”, otherwise Excluded.
Table 16

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Authentication Enable command |  |  | [1] 7.3.23 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.111 |  |  |
| 2 |  |  | Write Authentication Enable command |  |  | [1] 7.3.24 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 3–4 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 5 |  |  | Link Key Request Reply command |  |  | [1] 7.1.10 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 6 |  |  | Link Key Request Negative Reply command |  |  | [1] 7.1.11 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 7 |  |  | PIN Code Request Reply command |  |  | [1] 7.1.12 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 8 |  |  | PIN Code Request Negative Reply command |  |  | [1] 7.1.13 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 9 |  |  | Authentication Requested command |  |  | [1] 7.1.15 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 |  |  | Set Connection Encryption command |  |  | [1] 7.1.16 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 11 |  |  | Change Connection Link Key command |  |  | [1] 7.1.17 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 12 |  |  | Link Key Selection command |  |  | [1] 7.1.18 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.215 |  |  |
| 13 |  |  | Read PIN Type command |  |  | [1] 7.3.5 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.120 |  |  |
| 14 |  |  | Write PIN Type command |  |  | [1] 7.3.6 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 15 |  |  | Read Stored Link Key command |  |  | [1] 7.3.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.121 |  |  |
| 16 |  |  | Write Stored Link Key command |  |  | [1] 7.3.9 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | O |  |  |
| 17 |  |  | Delete Stored Link Key command |  |  | [1] 7.3.10 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.121 |  |  |
| 18 |  |  | Create New Unit Key command |  |  | [1] 7.3.7 |  |  | HCI 1a/1 “BR/EDR” |  |  | CORE 1b/50 “Controller Core v5.0 or earlier” |  |  | O |  |  |
| 19 |  |  | User Confirmation Request Reply command |  |  | [1] 7.1.30 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 20 |  |  | User Confirmation Request Negative Reply command |  |  | [1] 7.1.31 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 21 |  |  | User Passkey Request Reply command |  |  | [1] 7.1.32 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 22 |  |  | User Passkey Request Negative Reply command |  |  | [1] 7.1.33 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 23 |  |  | IO Capability Request Reply command |  |  | [1] 7.1.29 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 23a |  |  | IO Capability Request Negative Reply command |  |  | [1] 7.1.36 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 24 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 24a |  |  | Remote OOB Data Request Reply command |  |  | [1] 7.1.34 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 25 |  |  | Remote OOB Data Request Negative Reply command |  |  | [1] 7.1.35 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 26 |  |  | Read Local OOB Data command |  |  | [1] 7.3.60 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 27 |  |  | Write Simple Pairing Mode command |  |  | [1] 7.3.59 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28 |  |  | Read Simple Pairing Mode command |  |  | [1] 7.3.58 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 29 |  |  | Refresh Encryption Key command |  |  | [1] 7.3.57 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 30 |  |  | Read Encryption Key Size command |  |  | [1] 7.5.7 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 31 |  |  | Send Keypress Notification command |  |  | [1] 7.3.63 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 32 |  |  | LE Encrypt command |  |  | [1] 7.8.22 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.4 |  |  |
| 33 |  |  | LE Rand command |  |  | [1] 7.8.23 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.4 |  |  |
| 34 |  |  | LE Long Term Key Request Reply command |  |  | [1] 7.8.25 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.61 |  |  |
| 35 |  |  | LE Enable Encryption command |  |  | [1] 7.8.24 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.60 |  |  |
| 36 |  |  | LE Long Term Key Request event |  |  | [1] 7.7.65.5 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.61 |  |  |
| 37 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 37a |  |  | Encryption Change event [v1] on BR/EDR |  |  | [1] 7.7.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 37b |  |  | Encryption Change event [v1] on LE |  |  | [1] 7.7.8 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.4 |  |  |
| 37c |  |  | Encryption Change event [v2] on BR/EDR |  |  | [1] 7.7.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.158 |  |  |
| 37d |  |  | Encryption Change event [v2] on LE |  |  | [1] 7.7.8 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.56 |  |  |
| 38 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 38a |  |  | Encryption Key Refresh Complete event on BR/EDR |  |  | [1] 7.7.39 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 38b |  |  | Encryption Key Refresh Complete event on LE |  |  | [1] 7.7.39 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.4 |  |  |
| 39 |  |  | LE Long Term Key Request Negative Reply command |  |  | [1] 7.8.26 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.61 |  |  |
| 40 |  |  | Link Key Notification event |  |  | [1] 7.7.24 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 41 |  |  | Read Secure Connections Host Support command |  |  | [1] 7.3.91 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.218 |  |  |
| 42 |  |  | Write Secure Connections Host Support command |  |  | [1] 7.3.92 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.218 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 |  |  | Remote OOB Extended Data Request Reply command |  |  | [1] 7.1.53 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.142 |  |  |
| 44 |  |  | Read Local OOB Extended Data command |  |  | [1] 7.3.95 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.142 |  |  |
| 45 |  |  | Write Secure Connections Test Mode command |  |  | [1] 7.6.8 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.138 |  |  |
| 46 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 46a |  |  | Authenticated Payload Timeout Expired event on BR/EDR |  |  | [1] 7.7.75 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.155a |  |  |
| 46b |  |  | Authenticated Payload Timeout Expired event on LE |  |  | [1] 7.7.75 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.155b |  |  |
| 47 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 47a |  |  | Read Authenticated Payload Timeout command on BR/EDR |  |  | [1] 7.3.93 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.155a |  |  |
| 47b |  |  | Read Authenticated Payload Timeout command on LE |  |  | [1] 7.3.93 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.155b |  |  |
| 48 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 48a |  |  | Write Authenticated Payload Timeout command on BR/EDR |  |  | [1] 7.3.94 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.151 |  |  |
| 48b |  |  | Write Authenticated Payload Timeout command on LE |  |  | [1] 7.3.94 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.7 |  |  |
| 49 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 50 |  |  | LE Read Local P-256 Public Key command |  |  | [1] 7.8.36 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | O |  |  |
| 51 |  |  | LE Generate DHKey command [v1] |  |  | [1] 7.8.37 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.99 |  |  |
| 51a |  |  | LE Generate DHKey command [v2] |  |  | [3] 7.8.37 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | O |  |  |
| 52 |  |  | LE Read Local P-256 Public Key Complete event |  |  | [1] 7.7.65.8 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | O |  |  |
| 53 |  |  | LE Generate DHKey Complete event |  |  | [1] 7.7.65.9 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | O |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 54 |  |  | IO Capability Request event |  |  | [1] 7.7.40 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 55 |  |  | IO Capability Response event |  |  | [1] 7.7.41 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 56 |  |  | Link Key Request event |  |  | [1] 7.7.23 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 57 |  |  | Return Link Keys event |  |  | [1] 7.7.21 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.121 |  |  |
| 58 |  |  | Change Connection Link Key Complete event |  |  | [1] 7.7.9 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.102 |  |  |
| 59 |  |  | Link Key Type Changed event |  |  | [1] 7.7.10 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.215 |  |  |
| 60 |  |  | Keypress Notification event |  |  | [1] 7.7.49 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 61 |  |  | PIN Code Request event |  |  | [1] 7.7.22 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 62 |  |  | Remote OOB Data Request event |  |  | [1] 7.7.44 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 63 |  |  | User Passkey Request event |  |  | [1] 7.7.43 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 64 |  |  | User Passkey Notification event |  |  | [1] 7.7.48 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 65 |  |  | User Confirmation Request event |  |  | [1] 7.7.42 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 66 |  |  | Authentication Complete event |  |  | [1] 7.7.6 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.101 |  |  |
| 67 |  |  | Simple Pairing Complete event |  |  | [1] 7.7.45 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 68 |  |  | Set Min Encryption Key Size command |  |  | [6] 7.3.102 |  |  | HCI 1a/1 “BR/EDR” |  |  | CORE 1a/53 “Controller Core v5.3 or later” |  |  | O |  |  |

C.4: Mandatory IF LL 9/1 “LE Encryption”, otherwise Excluded.
C.7: Mandatory IF LL 9/1 “LE Encryption” AND LL 9/2 “LE Ping”, otherwise Excluded.
C.60: Mandatory IF LL 1/5 “Central Role” AND LL 9/1 “LE Encryption”, otherwise Excluded.
C.61: Mandatory IF LL 1/4 “Peripheral Role” AND LL 9/1 “LE Encryption”, otherwise Excluded.
C.99: Mandatory IF HCI 16/51a “LE Generate DHKey command [v2]”, otherwise Optional.
C.101: Mandatory IF HCI 16/9 “Authentication Requested command”, otherwise Excluded.
C.102: Mandatory IF HCI 16/11 “Change Connection Link Key command”, otherwise Excluded.
C.111: Mandatory IF HCI 16/2 “Write Authentication Enable command”, otherwise Excluded.
C.120: Mandatory IF HCI 16/14 “Write PIN Type command”, otherwise Excluded.
C.121: Mandatory IF HCI 16/16 “Write Stored Link Key command”, otherwise Excluded.
C.138: Mandatory IF LMP 2/26 “Secure Connections (Controller Support)”, otherwise Optional IF BB 2/3
“eSCO link”, otherwise Excluded.
C.142: Mandatory IF LMP 2/26 “Secure Connections (Controller Support)” OR LMP 2/19b “Secure
Simple Pairing (Controller Support)”, otherwise Excluded.
otherwise Excluded.
C.155a: Mandatory IF HCI 16/48a “Write Authenticated Payload Timeout command on BR/EDR”,
otherwise Optional.
C.155b: Mandatory IF HCI 16/48b “Write Authenticated Payload Timeout command on LE”, otherwise
Optional.
C.215: Mandatory IF LMP 2/14 “Broadcast encryption”, otherwise Excluded.
C.218: Mandatory IF LMP 2/26 “Secure Connections (Controller Support)”, otherwise Excluded.
C.158: Mandatory IF HCI 16/68 “Set Min Encryption Key Size command”, otherwise Optional.
C.56: Optional IF LL 9/1 “LE Encryption”, otherwise Excluded.
Table 17

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | Read Loopback Mode command |  |  | [1] 7.6.1 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.123 |  |  |
| 2 |  |  | Write Loopback Mode command |  |  | [1] 7.6.2 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.123 |  |  |
| 3 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |
| 3a |  |  | Enable Device Under Test Mode command on BR/EDR |  |  | [1] 7.6.3 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.123 |  |  |
| 3b |  |  | Enable Device Under Test Mode command on AMP |  |  | [1] 7.6.3 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 4 |  |  | Write Simple Pairing Debug Mode command |  |  | [1] 7.6.4 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | M |  |  |
| 5 |  |  | AMP Test command |  |  | [1] 7.6.7 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 5a |  |  | Enable AMP Receiver Reports command |  |  | [1] 7.6.5 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 6 |  |  | AMP Test End command |  |  | [1] 7.6.6 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 7 |  |  | LE Receiver Test command [v1] |  |  | [1] 7.8.28 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.2 |  |  |
| 8 |  |  | LE Transmitter Test command [v1] |  |  | [1] 7.8.29 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | C.1 |  |  |
| 9 |  |  | LE Test End command |  |  | [1] 7.8.30 |  |  | HCI 1a/4 “LE” |  |  |  |  |  | M |  |  |
| 10 |  |  | LE Receiver Test command [v2] |  |  | [2] 7.8.28 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.13 |  |  |
| 11 |  |  | LE Transmitter Test command [v2] |  |  | [2] 7.8.29 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/50 “Controller Core v5.0 or later” |  |  | C.12 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 |  |  | LE Receiver Test command [v3] |  |  | [3] 7.8.28 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.30 |  |  |
| 13 |  |  | LE Transmitter Test command [v3] |  |  | [3] 7.8.29 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/51 “Controller Core v5.1 or later” |  |  | C.29 |  |  |
| 14 |  |  | LE ISO Transmit Test command |  |  | [5] 7.8.111 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.45 |  |  |
| 15 |  |  | LE ISO Receive Test command |  |  | [5] 7.8.112 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.46 |  |  |
| 16 |  |  | LE ISO Read Test Counters command |  |  | [5] 7.8.113 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.46 |  |  |
| 17 |  |  | LE ISO Test End command |  |  | [5] 7.8.114 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.47 |  |  |
| 18 |  |  | LE Transmitter Test command [v4] |  |  | [5] 7.8.29 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.53 |  |  |
| 19 |  |  | AMP Start Test event |  |  | [1] 7.7.62 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 20 |  |  | AMP Receiver Report event |  |  | [1] 7.7.64 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 21 |  |  | AMP Test End event |  |  | [1] 7.7.63 |  |  | HCI 1a/3 “AMP” |  |  |  |  |  | C.130 |  |  |
| 22 |  |  | Loopback command event |  |  | [1] 7.7.25 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.123 |  |  |

C.1: Mandatory IF RFPHY 1/1 “LE Transmitter” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.2: Mandatory IF RFPHY 1/2 “LE Receiver” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.12: Mandatory IF LL 9/6a “Multiple PHYs” OR RFPHY 1/5 “Stable Modulation Index – Transmitter”, otherwise Optional IF RFPHY 1/1 “LE Transmitter” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.13: Mandatory IF LL 9/6a “Multiple PHYs” OR RFPHY 1/6 “Stable Modulation Index – Receiver”, otherwise Optional IF RFPHY 1/2 “LE Receiver” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.29: Mandatory IF LL 9/15 “Connection CTE Response” OR LL 9/16 “Connectionless CTE Transmitter”, otherwise Optional IF RFPHY 1/1 “LE Transmitter” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.30: Mandatory IF LL 9/14 “Connection CTE Request” OR LL 9/17 “Connectionless CTE Receiver”, otherwise Optional IF RFPHY 1/2 “LE Receiver” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.45: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.46: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.47: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/33 “Isochronous Broadcaster” OR LL 9/34 “Synchronized Receiver”, otherwise Excluded.
C.53: Mandatory IF LL 9/37 “LE Power Control Request”, otherwise Optional IF RFPHY 1/1 “LE Transmitter” OR RFPHY 1/3 “LE Transceiver”, otherwise Excluded.
C.123: Mandatory IF LMP 25/1 “Activate test mode”, otherwise Excluded.
C.130: Mandatory IF A2MP 1/2 “AMP Test Mode”, otherwise Excluded.
Table 18

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  |  | Set Connectionless |  | [1] 7.1.49 | [1] 7.1.49 |  | HCI 1a/1 “BR/EDR” | HCI 1a/1 “BR/EDR” |  |  |  |  | C.201 | C.201 |  |
|  |  |  |  | Peripheral Broadcast |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | command |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  | Set Connectionless Peripheral Broadcast Receive command |  |  | [1] 7.1.50 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.202 |  |  |
| 3 |  |  | Start Synchronization Train command |  |  | [1] 7.1.51 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 4 |  |  | Receive Synchronization Train command |  |  | [1] 7.1.52 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.202 |  |  |
| 5 |  |  | Set Reserved LT ADDR command _ |  |  | [1] 7.3.86 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 6 |  |  | Delete Reserved LT ADDR command _ |  |  | [1] 7.3.87 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 7 |  |  | Set Connectionless Peripheral Broadcast Data command |  |  | [1] 7.3.88 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 8 |  |  | Write Synchronization Train Parameters command |  |  | [1] 7.3.90 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 9 |  |  | Read Synchronization Train Parameters command |  |  | [1] 7.3.89 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 10 |  |  | Synchronization Train Complete event |  |  | [1] 7.7.67 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |
| 11 |  |  | Synchronization Train Received event |  |  | [1] 7.7.68 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.202 |  |  |
| 12 |  |  | Connectionless Peripheral Broadcast Receive event |  |  | [1] 7.7.69 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.202 |  |  |
| 13 |  |  | Connectionless Peripheral Broadcast Timeout event |  |  | [1] 7.7.70 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.202 |  |  |


|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14 |  |  | Connectionless Peripheral Broadcast Channel Map Change event |  |  | [1] 7.7.73 |  |  | HCI 1a/1 “BR/EDR” |  |  |  |  |  | C.201 |  |  |

C.201: Mandatory IF BB 3a/1 “Connectionless Peripheral Broadcast Transmitter”, otherwise Excluded.
C.202: Mandatory IF BB 3a/2 “Connectionless Peripheral Broadcast Receiver”, otherwise Excluded.
Table 19

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |

Table 20

|  | Item |  |  | Capability |  |  | Reference |  |  | IUT Configuration |  |  | Core Version |  |  | Status |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | LE Create BIG command |  |  | [5] 7.8.103 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.41 |  |  |
| 2 |  |  | LE Create BIG Test command |  |  | [5] 7.8.104 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.41 |  |  |
| 3 |  |  | LE Create BIG Complete event |  |  | [5] 7.7.65.27 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.41 |  |  |
| 4 |  |  | Isochronous data over HCI |  |  | [5] 5.4.5 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | O |  |  |
| 5 |  |  | LE Set Host Feature command |  |  | [5] 7.8.115 |  |  | HCI 1a/4 “LE” |  |  | CORE 1a/52 “Controller Core v5.2 or later” |  |  | C.49 |  |  |
| 6 |  |  | No longer used |  |  | N/A |  |  | N/A |  |  | N/A |  |  | N/A |  |  |

C.41: Mandatory IF LL 9/33 “Isochronous Broadcaster”, otherwise Excluded.
C.49: Mandatory IF LL 9/31 “Connected Isochronous Stream - Central” OR LL 9/32 “Connected Isochronous Stream - Peripheral” OR LL 9/45 “Connection Subrating” OR LL 9/48 “Advertising Coding Selection” OR LL 9/56 “Channel Sounding”, otherwise Optional.

| Item | Capability | Reference |  | IUT |  | Core Version | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Configuration |  |  |  |
| 1 | LE CS Read Local Supported Capabilities command | [8] 7.8.130 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 2 | LE CS Read Remote Supported Capabilities command | [8] 7.8.131 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 3 | LE CS Write Cached Remote Supported Capabilities command | [8] 7.8.132 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 4 | LE CS Security Enable command | [8] 7.8.133 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 5 | LE CS Set Default Settings command | [8] 7.8.134 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 6 | LE CS Read Remote FAE Table command | [8] 7.8.135 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 7 | LE CS Write Cached Remote FAE Table command | [8] 7.8.136 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.76 |
| 8 | LE CS Create Config command | [8] 7.8.137 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 9 | LE CS Remove Config command | [8] 7.8.138 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 10 | LE CS Set Channel Classification command | [8] 7.8.139 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 11 | LE CS Set Procedure Parameters command | [8] 7.8.140 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 12 | LE CS Set Procedure Enable command | [8] 7.8.141 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 13 | LE CS Test command | [8] 7.8.142 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 14 | LE CS Test End | [8] 7.8.143 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 15 | LE CS Read Remote Supported Capabilities Complete event | [8] 7.7.65.39 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 16 | LE CS Read Remote FAE Table Complete event | [8] 7.7.65.40 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |


| Item | Capability | Reference |  | IUT |  | Core Version | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Configuration |  |  |  |
| 17 | LE CS Security Enable Complete event | [8] 7.7.65.41 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 18 | LE CS Config Complete event | [8] 7.7.65.42 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 19 | LE CS Procedure Enable Complete event | [8] 7.7.65.43 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 20 | LE CS Subevent Result event | [8] 7.7.65.44 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 21 | LE CS Subevent Result Continue event | [8] 7.7.65.45 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |
| 22 | LE CS Test End Complete event | [8] 7.7.65.46 | HCI 1a/4 “LE” |  |  | CORE 1a/60 “Controller Core v6.0 or later” | C.75 |

C.75: Mandatory IF LL 9/56 “Channel Sounding”, otherwise Excluded
C.76: Mandatory IF LL 9/56 “Channel Sounding” AND LL 1/7 “CS Initiator”, otherwise Excluded.

## 2 References

[1] Bluetooth Core Specification Volume 41 Part E, Host Controller Interface (HCI), Version 4.2 or later
[2] Bluetooth Core Specification Volume 41 Part E, Host Controller Interface (HCI), Version 5.0 or later
[3] Bluetooth Core Specification Volume 41 Part E, Host Controller Interface (HCI), Version 5.1 or later
[4] Erratum 10734: Pairing Updates
[5] Bluetooth Core Specification Volume 4, Part E, Host Controller Interface (HCI), Version 5.2 or later
[6] Bluetooth Core Specification Volume 4, Part E, Host Controller Interface (HCI), Version 5.3 or later
[7] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification), Version

### 6.0 or later

[8] Specification of the Bluetooth System, Volume 4, Part E, Host Controller Interface (HCI), Version 6.0
or later

## 3 Revision history and acknowledgments

Revision History

|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
| 0 | 0 |  | 2.0.E.1 | 2.0.E.1 |  | 2005-11-22 |  |  |  | Reformatted and renamed document |  |
|  |  |  |  |  |  |  |  |  |  | TSE 864: Changed title page; |  |
|  |  |  |  |  |  |  |  |  |  | TSE 859 for Table 5 row 1 and Table 13 row 1 and |  |
|  |  |  |  |  |  |  |  |  |  | footnote C.2. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 871 for Table 10 Connection State |  |
| 1 |  |  | 2.0.E.2 |  |  | 2006-06-20 |  |  |  | TSE 895 for Table 7: remove read/write Page Scan |  |
|  |  |  |  |  |  |  |  |  |  | period mode |  |
|  |  |  | 2.1.E.0r0 to 2.1.E.0r3 |  |  | 2006-10-01 2006-12-27 |  |  |  | TSE 1885: Table 16: HCI write, read, store link keys |  |
|  |  |  |  |  |  |  |  |  |  | optional |  |
|  |  |  |  |  |  |  |  |  |  | Table 13: Added line 7 for LSTO event |  |
|  |  |  |  |  |  |  |  |  |  | Table 9: Erroneous Data Reporting Table Add lines |  |
|  |  |  |  |  |  |  |  |  |  | 6-9 |  |
|  |  |  |  |  |  |  |  |  |  | Table12: Add rows 10 through 16 for SSR and |  |
|  |  |  |  |  |  |  |  |  |  | Persistent Sniff; |  |
|  |  |  |  |  |  |  |  |  |  | TSE 1922 editorial correction made for PDF; reposted |  |
|  |  |  |  |  |  |  |  |  |  | Changed Vol 2, Part E, Section 7.x.x. to HCI:7.x.x |  |
|  |  |  |  |  |  |  |  |  |  | Renamed document from 2.0.E.3 to 2.1.E.1 |  |
|  |  |  |  |  |  |  |  |  |  | Revised previous column entry for clarity (added TSE |  |
|  |  |  |  |  |  |  |  |  |  | 1922) |  |
|  |  |  |  |  |  |  |  |  |  | Table 6: Add rows 11 and 12 for Simple Pairing |  |
|  |  |  |  |  |  |  |  |  |  | Table 16: Add rows 19 – 27 for Simple Pairing |  |
|  |  |  |  |  |  |  |  |  |  | Table 17 Add row 4 for Simple Pairing |  |
|  |  |  |  |  |  |  |  |  |  | Aligned specification references for new commands |  |
|  |  |  |  |  |  |  |  |  |  | with the 2.1 HCI spec |  |
|  |  |  |  |  |  |  |  |  |  | Added EIR commands; Items 13 and 14 in Table 6 |  |
|  |  |  |  |  |  |  |  |  |  | Added SP command; Item 25 in Table 16 |  |
|  |  |  |  |  |  |  |  |  |  | Added EPR command; Item 29 in Table 16 |  |
|  |  |  |  |  |  |  |  |  |  | Table 12: Removed Persistent Sniff related ICS line |  |
|  |  |  |  |  |  |  |  |  |  | items |  |
|  |  |  |  |  |  |  |  |  |  | Table 12, Item 19 pertaining to PBF added |  |
| 2 |  |  | 2.1.E.0 |  |  | 2006-12-28 |  |  |  | Add status to Table 6, lines 13 and 14; |  |
|  |  |  |  |  |  |  |  |  |  | Prepare for publication. |  |
| 3 |  |  | 2.1.E.1 |  |  | 2007-09-05 |  |  |  | TSE 2157: Add “Roles” table |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2116: Make C.1 M.1 in Table 8. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2108: Add row to Table 1. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2134: Table 16, items 15, 16, 17 M->O |  |
|  |  |  |  |  |  |  |  |  |  | Remove extra p in Table 1 and circular reference in |  |
|  |  |  |  |  |  |  |  |  |  | Table 3. Removed all “M1 footnotes.” Prerequisites |  |
|  |  |  |  |  |  |  |  |  |  | used instead |  |
|  | 4 |  |  | 2.1.E.2 |  |  | 2008-04-01 |  |  | TSE 2333: Table 9, C5 footnote |  |
| 5 | 5 |  | 2.1.E.3 | 2.1.E.3 |  | 2008-12-11 | 2008-12-11 |  |  | TSE 2642: Table 12, Footnote update to refer to |  |
|  |  |  |  |  |  |  |  |  |  | correct table |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2653: Table 12/8, 12/9 |  |
|  |  |  |  |  |  |  |  |  |  | Prepare for publication |  |
|  |  |  | 2.1.E.4r0-1 |  |  | 2009-02-17 |  |  |  | AMP updates |  |
|  |  |  |  |  |  |  |  |  |  | Removed SUMMARY 21/9 as it is removed from SUM |  |
|  |  |  |  |  |  |  |  |  |  | ICS. |  |
|  |  |  |  |  |  |  |  |  |  | Replaced SUM 2-1 with SUM 21. |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  | 6 |  |  | 3.0.H.0 |  |  | 2009-04-07 |  |  | Prepare for publication. |  |
|  |  |  | 3.0.H.0 | 3.0.H.0 |  | 2009-04-21 | 2009-04-21 |  |  | Correction to Table 5 rows 10-12, and additional rows |  |
|  |  |  |  |  |  |  |  |  |  | to Table 14. |  |
|  |  |  | 3.0.H.1 |  |  | 2009-08-11 |  |  |  | TSE 2717; Change footnotes for Tables 6, 9, 12, 13, |  |
|  |  |  |  |  |  |  |  |  |  | 16, 17 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2940: Change footnotes for Tables 6, 9, 12, 13, |  |
|  |  |  |  |  |  |  |  |  |  | 16, 17 |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2680: Remove pre-requisites for Controller role |  |
|  |  |  |  |  |  |  |  |  |  | from HCI features |  |
|  |  |  |  |  |  |  |  |  |  | TSE 2794: Table 12, Footnote C.2. |  |
|  |  |  |  | 3.0.H.2r0 |  |  | 2009-10-06 |  |  | New PICS due to LE LMP Enhancements |  |
|  |  |  | 3.0.H.2+LEr3 | 3.0.H.2+LEr3 |  | 2009-11-12 | 2009-11-12 |  |  | Document merged with LE HCI ICS 0.9d5 (dated _ _ |  |
|  |  |  |  |  |  |  |  |  |  | Nov 6) |  |
|  |  |  |  |  |  |  |  |  |  | LE references checked/updated to Tokyo Draft v03 |  |
|  |  |  | 3.0.H.2+LEr4 -4.0.0r5 |  |  | 2009-11-19 - 2009-12-15 |  |  |  | Removal of Flush for LE, consistent with errata 3316 |  |
|  |  |  |  |  |  |  |  |  |  | Review and corrections of conditionals by Steven |  |
|  |  |  |  |  |  |  |  |  |  | Wenham |  |
|  |  |  |  |  |  |  |  |  |  | Removal of 4/9 LE Set Local Used Features |  |
|  |  |  |  |  |  |  |  |  |  | Command due to E3127 Editorial review’ |  |
|  |  |  |  |  |  |  |  |  |  | Review input from Steven Wenham |  |
|  |  |  |  |  |  |  |  |  |  | Corrected conditions for 16/37 and 16/38 applicable to |  |
|  |  |  |  |  |  |  |  |  |  | 1a/1. |  |
|  |  |  |  |  |  |  |  |  |  | Editorial review’ |  |
|  |  |  |  |  |  |  |  |  |  | Document reference change from Tokyo to 4.0 |  |
|  | 7 |  |  | 4.0.0 |  |  | 2009-12-15 |  |  | Prepare for publication |  |
| 8 | 8 |  | 4.0.1 | 4.0.1 |  | 2010-06-24 | 2010-06-24 |  |  | TSE 3188: Tables 6, 8, 9,10, 11, 13, 16: Added |  |
|  |  |  |  |  |  |  |  |  |  | column for prerequisite |  |
|  |  |  |  |  |  |  |  |  |  | TSE 3386: Table 14: Change C.1 to 0 for buffer |  |
|  |  |  |  |  |  |  |  |  |  | overflow event |  |
|  |  |  |  | 4.0.2r0 |  |  | 2010-11-22 |  |  | TSE 3526: Add 1b-d for controller-type support |  |
|  | 9 |  |  | 4.0.2 |  |  | 2011-07-15 |  |  | Prepare for publication. |  |
|  |  |  | 4.0.3r0 | 4.0.3r0 |  | 2011-10-28 | 2011-10-28 |  |  | TSE 4482: Table 6, Table 9, Table 12, Table 13, |  |
|  |  |  |  |  |  |  |  |  |  | Table 16, Table 17: update Conditionals make |  |
|  |  |  |  |  |  |  |  |  |  | BR/EDR HCI features mandatory for 4.0 |  |
|  | 10 |  |  | 4.0.3 |  |  | 2012-03-30 |  |  | Prepare for publication. |  |
|  |  |  | 4.0.4r0 | 4.0.4r0 |  | 2012-05-01 | 2012-05-01 |  |  | TSE 4482 Table 6: C.2 and C.3, Table 9: C.5, Table |  |
|  |  |  |  |  |  |  |  |  |  | 12: C.3, Table 13: C.4, Table 16: C.6, C.7, C.8 and |  |
|  |  |  |  |  |  |  |  |  |  | C.9, Table 17: C.1 |  |
|  | 11 |  |  | 4.0.4 |  |  | 2012-07-24 |  |  | Adopted by the Bluetooth SIG Board of Directors |  |
|  |  |  |  | 4.0.5r1 |  |  | 2012-12-20 |  |  | Connectionless Broadcast Change Request |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 4.0.5r2 | 4.0.5r2 |  | 2013-01-02 |  |  |  | Connectionless Broadcast Review: |  |
|  |  |  |  |  |  |  |  |  |  | Table 5, added item 25 and 26 and added C.2 |  |
|  |  |  |  |  |  |  |  |  |  | Table 7. Moved items 1, 2, and 16 from table 18 to |  |
|  |  |  |  |  |  |  |  |  |  | table 7 and become the new 29, 30, and 31. (Table 18 |  |
|  |  |  |  |  |  |  |  |  |  | renumbered). |  |
|  |  |  |  |  |  |  |  |  |  | Table 7, added item 32. |  |
|  |  |  |  |  |  |  |  |  |  | Table7, added conditionals C.3 and C.4 |  |
|  |  |  |  |  |  |  |  |  |  | Table 18, changed item 10 from C.2 to C.1 (was |  |
|  |  |  |  |  |  |  |  |  |  | previously item 12 before the renumbering) |  |
|  |  |  | 4.0.5r3 |  |  | 2013-01-03 |  |  |  | Connectionless Broadcast Review: |  |
|  |  |  |  |  |  |  |  |  |  | Table 18 item 1 changed to C.1 |  |
|  |  |  |  |  |  |  |  |  |  | Updated References in Table 7 and Table 18. |  |
|  |  |  | 4.0.5r4 |  |  | 2013-01-22 |  |  |  | Connectionless Broadcast Review (Jason & Xuguang) |  |
|  |  |  |  |  |  |  |  |  |  | Added conditionals to 5/25 and 6/23 to require |  |
|  |  |  |  |  |  |  |  |  |  | support of CSA4 or later. |  |
|  |  |  |  |  |  |  |  |  |  | Added references section and normative cross- |  |
|  |  |  |  |  |  |  |  |  |  | references in the reference cells. |  |
|  |  |  | 4.0.5r5 |  |  | 2013-01-24 |  |  |  | Connectionless Broadcast Review (Jason, Alicia and |  |
|  |  |  |  |  |  |  |  |  |  | Meagan) |  |
|  |  |  |  |  |  |  |  |  |  | Fixed type-o in Table 6, C.8. |  |
|  |  |  |  |  |  |  |  |  |  | Edited for consistent language and syntax for |  |
|  |  |  |  |  |  |  |  |  |  | conditionals. |  |
|  |  |  | 4.0.5r6 |  |  | 2013-01-25 |  |  |  | Connectionless Broadcast Review (Xuguang) |  |
|  |  |  |  |  |  |  |  |  |  | Added “Part B Volume 2 Part E” to the CSA4 |  |
|  |  |  |  |  |  |  |  |  |  | reference |  |
|  |  |  |  | 4.0.5r7 |  |  | 2013-01-28 |  |  | Approved by BTI |  |
|  |  |  |  | 4.0.5r7 |  |  | 2013-02-13 |  |  | Approved by BQRB |  |
|  | 12 |  |  | 4.0.5 |  |  | 2013-02-19 |  |  | Prepare for Publication |  |
|  |  |  | 4.0.6r1 | 4.0.6r1 |  | 2013-05-31 | 2013-05-31 |  |  | TSE 5072: Updated Table 7, C.1 to “Mandatory if LL |  |
|  |  |  |  |  |  |  |  |  |  | 1/5 and LL 3/3 are supported, otherwise Excluded” |  |
|  |  |  |  | 4.0.6 |  |  | 2013-07-02 |  |  | Prepare for Publication |  |
|  |  |  |  | 4.0.5 |  |  | 2013-02-12 |  |  | Approved by BQRB |  |
|  |  |  | 4.0.6r1 | 4.0.6r1 |  | 2013-02-13 | 2013-02-13 |  |  | Editorial error in Table 17. C.1 Conditional corrected |  |
|  |  |  |  |  |  |  |  |  |  | to read 17/1 (Privacy Feature). C.1 and C.3 edited for |  |
|  |  |  |  |  |  |  |  |  |  | clarity. |  |
|  |  |  |  |  |  |  |  |  |  | Approved by BTI & BQRB |  |
|  | 13 |  |  | 4.0.6 |  |  | 2013-02-19 |  |  | Prepare for Publication |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  | 4.0.7r1 | 4.0.7r1 |  | 2013-05-30 |  |  |  | TSE 5063: |  |
|  |  |  |  |  |  |  |  |  |  | • Updated title of section 1.4 to “LE Only |  |
|  |  |  |  |  |  |  |  |  |  | Capability Statement” |  |
|  |  |  |  |  |  |  |  |  |  | • Removed conditionals from Table 19, already |  |
|  |  |  |  |  |  |  |  |  |  | covered in the prerequisite. All items changed to |  |
|  |  |  |  |  |  |  |  |  |  | Mandatory. |  |
|  |  |  |  |  |  |  |  |  |  | • Removed conditionals from Table 20, already |  |
|  |  |  |  |  |  |  |  |  |  | covered in the prerequisite. Item 1 and 4 changed to |  |
|  |  |  |  |  |  |  |  |  |  | Mandatory, Item 2 and 3 as optional. |  |
|  |  |  |  |  |  |  |  |  |  | • Updated conditionals for Table 22, removed |  |
|  |  |  |  |  |  |  |  |  |  | “AND (20/1 OR 20/3 OR 20/4) from C.1, and updated |  |
|  |  |  |  |  |  |  |  |  |  | parenthesis and language in C.2 and C.3. |  |
|  |  |  |  |  |  |  |  |  |  | • Removed C.1 and C.2 from Table 23, |  |
|  |  |  |  |  |  |  |  |  |  | updated C.3 to be C.1. Item 1 status changed to C.1, |  |
|  |  |  |  |  |  |  |  |  |  | items 2 and 4 changed to optional, and items 3 and 5 |  |
|  |  |  |  |  |  |  |  |  |  | updated to Mandatory. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5091: Updated Table 20A item 6 status to C.3, |  |
|  |  |  |  |  |  |  |  |  |  | added “C.2: Mandatory if 22/2 or 22/3 is supported, |  |
|  |  |  |  |  |  |  |  |  |  | otherwise Optional” C.2 had been included in an |  |
|  |  |  |  |  |  |  |  |  |  | earlier version and was still needed, former C.2 |  |
|  |  |  |  |  |  |  |  |  |  | became C.3. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5100: Updated C.4 in Table 2 to remove “SUM |  |
|  |  |  |  |  |  |  |  |  |  | ICS 31/5” because the item no longer exists. |  |
|  |  |  | 4.0.7r2 |  |  | 2013-06-04 |  |  |  | BTI Review, Alicia’s Comments: |  |
|  |  |  |  |  |  |  |  |  |  | Fixed the TSE reference number in the Change |  |
|  |  |  |  |  |  |  |  |  |  | History. |  |
|  |  |  |  |  |  |  |  |  |  | Table 0a – changed Device to Version Configuration |  |
|  |  |  |  |  |  |  |  |  |  | to match the Table title. |  |
|  |  |  |  |  |  |  |  |  |  | Added the ICS item description in parenthesis to |  |
|  |  |  |  |  |  |  |  |  |  | conditionals where it wasn’t yet indicated for |  |
|  |  |  |  |  |  |  |  |  |  | consistency and clarity: Tables 1-3, 20A, 22-25, 30, |  |
|  |  |  |  |  |  |  |  |  |  | 32-36. |  |
|  |  |  |  |  |  |  |  |  |  | Table 2: Further review of TSE 5100 showed there |  |
|  |  |  |  |  |  |  |  |  |  | was a missing ICS item that needed adding due to the |  |
|  |  |  |  |  |  |  |  |  |  | Sum ICS re-shuffle: SUM ICS 31/11 (Core |  |
|  |  |  |  |  |  |  |  |  |  | Specification 4.0 + HS). Updated C.4 with this item. |  |
|  |  |  |  |  |  |  |  |  |  | Table 3 conditional C.1 had 2 references to GAP 3/1 it |  |
|  |  |  |  |  |  |  |  |  |  | is an obvious mistake that one should say 3/2. |  |
|  |  |  |  |  |  |  |  |  |  | In Tables that had been updated for the pre-requisites |  |
|  |  |  |  |  |  |  |  |  |  | affected by previous TSE’s 4330 and 4305 consistent |  |
|  |  |  |  |  |  |  |  |  |  | with changes in TSE 5063 changed the pre-requisites |  |
|  |  |  |  |  |  |  |  |  |  | that stated either Optional or Mandatory to Support |  |
|  |  |  |  |  |  |  |  |  |  | based on the support of the Table’s pre-requisites to |  |
|  |  |  |  |  |  |  |  |  |  | simply “M” or “O”: Tables 18, 28, 29, 30, 31, 34, 36, |  |
|  |  |  |  |  |  |  |  |  |  | and 37. |  |
|  |  |  |  |  |  |  |  |  |  | Simplified conditionals by removing the pre-requisite |  |
|  |  |  |  |  |  |  |  |  |  | items from the conditionals leaving only the |  |
|  |  |  |  |  |  |  |  |  |  | dependencies in Table 30 item C.1 and Table 36 |  |
|  |  |  |  |  |  |  |  |  |  | items C.1 and C.2. |  |
|  |  |  |  |  |  |  |  |  |  | Misc. editorial changes. |  |
|  | 14 |  |  | 4.0.7 |  |  | 2013-07-02 |  |  | Prepare for Publication |  |
|  |  |  |  | 4.0.7rT |  |  | 2013-08-01 |  |  | Template Conversion |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  | 4.0.7rTr3 |  |  | 2013-09-09 |  |  | Resolution of Template Conversion Comments |  |
|  |  |  |  | 4.1.0r01 |  |  | 2013-09-24 |  |  | BR/EDR Secure Connections CR |  |
|  |  |  |  | 4.1.0r02 |  |  | 2013-09-25 |  |  | Train Nudging and Generalized Interlaced Scan CR |  |
|  |  |  | 4.1.0r03 | 4.1.0r03 |  | 2013-09-27 | 2013-09-27 |  |  | TSE 5325: Removed C.3, updated 18/13 to C.2 for |  |
|  |  |  |  |  |  |  |  |  |  | 1a/1. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5322: Updated references throughout |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5318: Updated item 5/25 and 5/26 to be |  |
|  |  |  |  |  |  |  |  |  |  | “Excluded” for 1a/3 and 1a/4. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5317: Updated C.1 for Table 5. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5193: Updated C.1 and C.2 conditionals for |  |
|  |  |  |  |  |  |  |  |  |  | Table 7. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5137: Addition of item 9 in Table 4, and |  |
|  |  |  |  |  |  |  |  |  |  | conditional C.2. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 5348: Updated item 1/1a to be no longer used, |  |
|  |  |  |  |  |  |  |  |  |  | and removed the C.1 conditional in Table 1. |  |
|  |  |  |  | 4.1.0r04 |  |  | 2013-10-09 |  |  | Piconet Clock Adjust CR |  |
|  |  |  |  | 4.1.0r05 |  |  | 2013-10-09 |  |  | LE Ping CR |  |
|  |  |  |  | 4.1.0r06 |  |  | 2013-10-14 |  |  | LE Link Layer Topology CR |  |
|  |  |  |  | 4.1.0r09 |  |  | 2013-10-31 |  |  | Table 14 Changes by Mayank |  |
|  |  |  |  | 4.1.0r10 |  |  | 2013-11-06 |  |  | Comment resolution |  |
|  |  |  | 4.1.0r12 | 4.1.0r12 |  | 2013-11-07 | 2013-11-07 |  |  | Review by Chris Church |  |
|  |  |  |  |  |  |  |  |  |  | Updates to conditionals to represent all specification |  |
|  |  |  |  |  |  |  |  |  |  | versions. |  |
|  | 15 |  |  | 4.1.0 |  |  | 2013-12-03 |  |  | Prepare for Publication |  |
|  |  |  | 4.2.0r00 | 4.2.0r00 |  | 2014-11-07 | 2014-11-07 |  |  | Integrated Section 3.1 of |  |
|  |  |  |  |  |  |  |  |  |  | Core LE Data Length Extensions TEST.CRr01 _ _ _ _ _ |  |
|  |  |  | 4.2.0r01 |  |  | 2014-11-20 |  |  |  | Review by Mayank, Jason, Rasmus. |  |
|  |  |  |  |  |  |  |  |  |  | Changes integrated |  |
|  |  |  | 4.2.0r02 |  |  | 2014-11-23 |  |  |  | Incorporated additions from Rasmus and Alicia. |  |
|  |  |  |  |  |  |  |  |  |  | Table 4, C.2 updated to remove CSA2 |  |
|  |  |  |  |  |  |  |  |  |  | Table 6, C.2 updated to be 2.1 or later |  |
|  |  |  |  |  |  |  |  |  |  | Table 6, C.3 updated to be GAP 1/3 AND 2.1 or later |  |
|  |  |  |  |  |  |  |  |  |  | Standardization of Core version parenthetical |  |
|  |  |  |  |  |  |  |  |  |  | references in conditionals. |  |
|  |  |  |  |  |  |  |  |  |  | Additional Items for Privacy 1.2 |  |
|  |  |  |  |  |  |  |  |  |  | Table 5, new items 27, 28, 29, 30, 31, 32 and C.4 and |  |
|  |  |  |  |  |  |  |  |  |  | C.5 |  |
|  |  |  |  |  |  |  |  |  |  | Table 6, new item 26 and C.11 |  |
|  |  |  |  |  |  |  |  |  |  | Table 7, new items 38. 39, 40 and C.9 |  |
|  |  |  | 4.2.0r03 |  |  | 2014-11-24 |  |  |  | Further review by Rasmus – updates to Table 7 / 39 & |  |
|  |  |  |  |  |  |  |  |  |  | 40; C.10 added. |  |
|  |  |  | 4.2.0r04 |  |  | 2014-11-25 |  |  |  | Review by Mayank, editorial correction to Table 4, C.2 |  |
|  |  |  |  |  |  |  |  |  |  | and added the missing LE Read Maximum Data |  |
|  |  |  |  |  |  |  |  |  |  | Length command that was recently added as part of |  |
|  |  |  |  |  |  |  |  |  |  | the LE Data Packet Length Extension Core feature, |  |
|  |  |  |  |  |  |  |  |  |  | as item 10/16. |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
|  |  |  |  | 4.2.0r05 |  |  | 2014-11-25 |  |  | Additional editorial review by Alicia integrated |  |
|  |  |  |  | 4.2.0r06 |  |  | 2014-11-25 |  |  | Review by Dave. Minor editorial changes. |  |
|  | 16 |  |  | 4.2.0 |  |  | 2014-12-04 |  |  | Prepare for TCRL 2014-2 publication |  |
|  |  |  |  | 4.2.1r00 |  |  | 2016-03-03 |  |  | TSE 6949: HCI 14/3, Core Version updated. |  |
|  |  |  | 4.2.1r01 | 4.2.1r01 |  | 2016-04-06 | 2016-04-06 |  |  | TSE 6370: Corrected Capability name for HCI 1/1, |  |
|  |  |  |  |  |  |  |  |  |  | 1/1b, 1/1c, and 1/1d. Prerequisite Status updated for |  |
|  |  |  |  |  |  |  |  |  |  | HCI 1/2, 1/3, 3/1, and 8/8. |  |
|  | 17 |  |  | 4.2.1 |  |  | 2016-07-07 |  |  | Prepared for TCRL 2016-1 publication |  |
|  |  |  |  | 5.0.0r00 |  |  | 2016-07-07 |  |  | Integrated changes for Core Specification 5.0 release |  |
|  |  |  | 5.0.0r01 | 5.0.0r01 |  | 2016-08-30 | 2016-08-30 |  |  | Issue 7534: Updated “TBD” references in Table 5, 6, |  |
|  |  |  |  |  |  |  |  |  |  | 7, 13, and 14. Changed “LE Used Channel Selection |  |
|  |  |  |  |  |  |  |  |  |  | Algorithm Event” to “LE Channel Selection Algorithm |  |
|  |  |  |  |  |  |  |  |  |  | Event” in Table 7. |  |
|  |  |  | 5.0.0r02 |  |  | 2016-09-13 |  |  |  | Issue 7633: Updated Conditional C.7 for Table 13: |  |
|  |  |  |  |  |  |  |  |  |  | Deleted references to item LL 9/11. Added references |  |
|  |  |  |  |  |  |  |  |  |  | to items LL 6/23 and LL 7/23. |  |
|  |  |  | 5.0.0r03 |  |  | 2016-09-20 |  |  |  | Issue 7682: Updated Conditional C.7 for Table 13: |  |
|  |  |  |  |  |  |  |  |  |  | Deleted references to items LL 6/23 and LL 7/23. |  |
|  |  |  |  |  |  |  |  |  |  | Added reference to SUM ICS 21/16. |  |
|  |  |  | 5.0.0r04 |  |  | 2016-09-30 |  |  |  | Issue 7728: Deleted item HCI 13/13 and conditional |  |
|  |  |  |  |  |  |  |  |  |  | C.7. |  |
|  |  |  | 5.0.0r05 |  |  | 2016-10-07 |  |  |  | TSE 7537 (erratum 6356): Added item 7/43 for LE Set |  |
|  |  |  |  |  |  |  |  |  |  | Privacy Mode. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 7581 (erratum 7021): Changed LE Set Advertise |  |
|  |  |  |  |  |  |  |  |  |  | Enable to LE Set Advertising Enable. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 6971: Added row 17 to Table 10, row 2a and |  |
|  |  |  |  |  |  |  |  |  |  | conditional C.5 to Table 15, row 23a to Table 16, and |  |
|  |  |  |  |  |  |  |  |  |  | row 5a to Table 17. Deleted redundant entries from |  |
|  |  |  |  |  |  |  |  |  |  | Table 14 (rows 9, 10, and 11) and Table 19 (row 1). |  |
|  |  |  | 5.0.0r06 |  |  | 2016-11-11 |  |  |  | Issue 7884: Global edit. Added support in conditionals |  |
|  |  |  |  |  |  |  |  |  |  | for Core Spec version 5.0. |  |
|  |  |  | 5.0.0r07 |  |  | 2016-11-16 |  |  |  | Updated to current template. Removed unnecessary |  |
|  |  |  |  |  |  |  |  |  |  | parentheses and replaced with quotation marks. |  |
|  |  |  |  |  |  |  |  |  |  | Editorial re-writes to Conditional logic to future proof |  |
|  |  |  |  |  |  |  |  |  |  | Core versioning increments. Conditionals affected: |  |
|  |  |  |  |  |  |  |  |  |  | Table 4: C.2; Table 6: C.2, C.3; Table 7: C.5; Table 9: |  |
|  |  |  |  |  |  |  |  |  |  | C.5; Table 12: C.3; Table 13: C.4, C.6; Table 16: C.6, |  |
|  |  |  |  |  |  |  |  |  |  | C.7, C.8, C.9, C.13; Table 17: C.1, C.4. |  |
|  |  |  | 5.0.0r08 |  |  | 2016-11-18 |  |  |  | Corrected “CSA4 or later” to correct references in |  |
|  |  |  |  |  |  |  |  |  |  | Table 5:C.2 and Table 6: C.8, C.9 |  |
| 18 |  |  | 5.0.0 |  |  | 2016-12-13 |  |  |  | Approved by BTI. Prepared for TCRL 2016-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication |  |
|  |  |  | 5.0.1r00 |  |  | 2017-03-28 |  |  |  | TSE 8535: Updated item 16/46 capability from |  |
|  |  |  |  |  |  |  |  |  |  | “Authentication” to “Authenticated” and Status from |  |
|  |  |  |  |  |  |  |  |  |  | “Excluded” to “C.12”. Removed 16/49 as a duplicate. |  |
|  |  |  | 5.0.1r01 |  |  | 2017-04-28 |  |  |  | TSE 8916: Updated Status from "C.10" to "C.13" for |  |
|  |  |  |  |  |  |  |  |  |  | item 43 in Table7: Connection Setup and added |  |
|  |  |  |  |  |  |  |  |  |  | Conditional C.13. |  |


|  | Publication |  |  | Revision |  | Date |  |  | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |  |  |
| 19 | 19 |  | 5.0.1 | 5.0.1 |  | 2017-07-05 |  |  |  | Approved by BTI. Prepared for TCRL 2017-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  |  | 5.0.2r00 |  |  | 2017-09-14 |  |  | TSE 9218: Modified Table 9, C.13 note. |  |
|  |  |  | 5.0.2r01 | 5.0.2r01 |  | 2017-09-19 | 2017-09-19 |  |  | AoA/AoD: Integrated the AoA/AoD CR into Tables 4, |  |
|  |  |  |  |  |  |  |  |  |  | 5, 8, 10, and 17. |  |
|  |  |  | 5.0.2r02 |  |  | 2017-09-29 |  |  |  | TSE 9829: Changed “LE Read Remote Used |  |
|  |  |  |  |  |  |  |  |  |  | Features Command” to “LE Read Remote Features |  |
|  |  |  |  |  |  |  |  |  |  | command” and “LE Read Remote Used Features |  |
|  |  |  |  |  |  |  |  |  |  | Complete Event” to “LE Read Remote Features |  |
|  |  |  |  |  |  |  |  |  |  | Complete Event” in Table 8. |  |
| 20 |  |  | 5.0.2 |  |  | 2017-12-07 |  |  |  | Approved by BTI. Prepared for TCRL 2017-2 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 5.0.3r00-02 |  |  | 2018-01-24 – 2018-06-14 |  |  |  | Issue 10276: |  |
|  |  |  |  |  |  |  |  |  |  | Added new reference in Section 2 References. |  |
|  |  |  |  |  |  |  |  |  |  | Updated Capability for 17/7, 17/8, 17/10, and 17/11. |  |
|  |  |  |  |  |  |  |  |  |  | Updated Capability and Reference for 17/12 and |  |
|  |  |  |  |  |  |  |  |  |  | 17/13. |  |
|  |  |  |  |  |  |  |  |  |  | Revised Table 17 C.5 and C.6. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 9903 (rating 2): Added 5/53 and C.11 to Table 5. |  |
|  |  |  |  |  |  |  |  |  |  | Editorial fix to C.6 in Table 13. Added HCI prefix to |  |
|  |  |  |  |  |  |  |  |  |  | C.2 in Table 14. Changed C.4 to make the command |  |
|  |  |  |  |  |  |  |  |  |  | mandatory if any of the above features are supported. |  |
|  |  |  |  |  |  |  |  |  |  | Incorporated Core E10734 Pairing Updates TS CR: |  |
|  |  |  |  |  |  |  |  |  |  | Added item 4/12 and C.4. |  |
| 21 |  |  | 5.0.3 |  |  | 2018-07-02 |  |  |  | Approved by BTI. Prepared for TCRL 2018-1 |  |
|  |  |  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 5.0.4r00-r06 |  |  | 2018-07-16 – 2018-11-13 |  |  |  | Incorporated Core PAST CLE TEST CR r05: |  |
|  |  |  |  |  |  |  |  |  |  | _ _ _ _ _ Table 6: Added row 37 and conditional note C.14; |  |
|  |  |  |  |  |  |  |  |  |  | modified conditional note C.13. |  |
|  |  |  |  |  |  |  |  |  |  | Table 10: Added rows 24–28 and conditional notes |  |
|  |  |  |  |  |  |  |  |  |  | C.8–C.10. |  |
|  |  |  |  |  |  |  |  |  |  | Table 14: Modified conditional note C.5. |  |
|  |  |  |  |  |  |  |  |  |  | Incorporated Core Minor Enhancements Batch 1 Test |  |
|  |  |  |  |  |  |  |  |  |  | CRr10-clean: For Table 16: Modified item 51; added |  |
|  |  |  |  |  |  |  |  |  |  | item 51a and conditional note C.16. |  |
|  |  |  |  |  |  |  |  |  |  | Issue 10707: Updated conditional note ref. for items |  |
|  |  |  |  |  |  |  |  |  |  | 51 and 51a. Modified conditional note C.16; added |  |
|  |  |  |  |  |  |  |  |  |  | C.17 for Table 16. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 10959 (rating 2): Revised conditionals C.3 and |  |
|  |  |  |  |  |  |  |  |  |  | C.4 in Table 14 so they point to Controller SUM ICS |  |
|  |  |  |  |  |  |  |  |  |  | Table 21 rather than Host Table 31. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 10731 (rating 2): Added conditional C.18 and |  |
|  |  |  |  |  |  |  |  |  |  | updated items 16/34, 16/35, 16/36, and 16/39 with |  |
|  |  |  |  |  |  |  |  |  |  | C.18. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 10943 (rating 3): Deprecated items 16/3 and |  |
|  |  |  |  |  |  |  |  |  |  | 16/4. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 11155 (rating 2): Updated conditional C.11 for |  |
|  |  |  |  |  |  |  |  |  |  | Table 7. |  |
|  |  |  |  |  |  |  |  |  |  | TSE 11156 (rating 2): Updated conditional C.9 for |  |
|  |  |  |  |  |  |  |  |  |  | Table 7. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Replaced [X] values with actual values. |  |
|  |  |  |  |  |  |  |  | Updated Madrid styles - changed light grey text to |  |
|  |  |  |  |  |  |  |  | black text. |  |
|  |  |  | 5.1.0r00-r01 |  |  | 2018-11-13 – 2018-11-19 |  | Updated revision number from 5.0.4 to 5.1.0 to align |  |
|  |  |  |  |  |  |  |  | with the adoption of Core Specification version 5.1. |  |
|  |  |  |  |  |  |  |  | Corrected implementation of conditionals |  |
|  |  |  |  |  |  |  |  | referencing 5.1. |  |
| 22 |  |  | 5.1.0 |  |  | 2018-12-07 |  | Approved by BTI. Prepared for TCRL 2018-2 |  |
|  |  |  |  |  |  |  |  | publication. |  |
|  |  |  | 5.1.1r00–r06 |  |  | 2019-04-01 – 2019-06-13 |  | TSE 11468 (rating 1): Updated Table 7 to C.2 for LE |  |
|  |  |  |  |  |  |  |  | transport in Item 27 and changed C.8 to “No Longer |  |
|  |  |  |  |  |  |  |  | Used.” |  |
|  |  |  |  |  |  |  |  | TSE 11530 (rating 2): Added entry for HCI LE Modify |  |
|  |  |  |  |  |  |  |  | Sleep Clock Accuracy command to Table 10; added |  |
|  |  |  |  |  |  |  |  | conditional C.11 under table. |  |
|  |  |  |  |  |  |  |  | TSE 11453 (rating 2): Updated item 26 of Table 7 and |  |
|  |  |  |  |  |  |  |  | conditional C.2 under table. |  |
|  |  |  |  |  |  |  |  | TSE 11924 (rating 2): Modified Table 4 and Table 14 |  |
|  |  |  |  |  |  |  |  | to address support of certain features under AMP. |  |
|  |  |  |  |  |  |  |  | TSE 11843 (rating 2): Updated Table 8, item 8 as |  |
|  |  |  |  |  |  |  |  | Excluded for AMP Transport and added a new |  |
|  |  |  |  |  |  |  |  | conditional for BR and LE transport support. |  |
|  |  |  |  |  |  |  |  | TSE 11845 (rating 2): Updated item 12 of Table 4: |  |
|  |  |  |  |  |  |  |  | Controller Information to reflect “Excluded” for Core |  |
|  |  |  |  |  |  |  |  | Version. |  |
|  |  |  |  |  |  |  |  | TSE 11178 (rating 2): Updated conditional statement |  |
|  |  |  |  |  |  |  |  | C.5 under Table 13, “Physical Links” to include |  |
|  |  |  |  |  |  |  |  | Extended Advertising. |  |
|  |  |  |  |  |  |  |  | Incorporated changes associated with Key |  |
|  |  |  |  |  |  |  |  | Negotiation Changes specification erratum 11838: |  |
|  |  |  |  |  |  |  |  | Changed status for item 16/30 (Read Encryption Key |  |
|  |  |  |  |  |  |  |  | Size command) from Optional to Mandatory for |  |
|  |  |  |  |  |  |  |  | devices operating over BR/EDR transport. |  |
| 23 |  |  | 5.1.1 |  |  | 2019-08-01 |  | Approved by BTI. Prepared for TCRL 2019-1 |  |
|  |  |  |  |  |  |  |  | publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p24r00–r07 | p24r00–r07 |  | 2019-08-06 – 2019-12-03 |  | Added test groups to accommodate adoption of Core |  |
|  |  |  |  |  |  |  |  | Specification v5.2 with regard to Isochronous |  |
|  |  |  |  |  |  |  |  | Channels CR r20 (includes Issues 11742, 11762, |  |
|  |  |  |  |  |  |  |  | 11777, 11778, 11779, 11783,11786, 11804, 11817, |  |
|  |  |  |  |  |  |  |  | 11819, 11820, 11852, 11917, 11919, 11928, 11929, |  |
|  |  |  |  |  |  |  |  | 11930, 11983, 11740, 11801, 11941, 12029, 12030, |  |
|  |  |  |  |  |  |  |  | 12043, 12052, 12053, 12054, 12055, 12059, 12061, |  |
|  |  |  |  |  |  |  |  | 12071, 12072, 12073, 12077, 12084, 12031, 12078, |  |
|  |  |  |  |  |  |  |  | 12094, 12095, 12106, 12107, 12130, 12132, 12133, |  |
|  |  |  |  |  |  |  |  | 12251, 12280, and 12321). Added items 6–9 and |  |
|  |  |  |  |  |  |  |  | notes C.1 and C.2 to Table 3; added items 54–58 and |  |
|  |  |  |  |  |  |  |  | notes C.12 and C.13 to Table 5; added items 38–43 |  |
|  |  |  |  |  |  |  |  | and notes C.15 and C.16 to Table 6; added items 30– |  |
|  |  |  |  |  |  |  |  | 34 and notes C.12–C.14 to Table 10; updated text in |  |
|  |  |  |  |  |  |  |  | note C.5 for Table 13; added item 9 and note C.6 to |  |
|  |  |  |  |  |  |  |  | Table 15; added items 14–17 and notes C.7–C.9 to |  |
|  |  |  |  |  |  |  |  | Table 17; added new Table 20; updated references |  |
|  |  |  |  |  |  |  |  | section with new Core Specification. |  |
|  |  |  |  |  |  |  |  | Added test groups to accommodate adoption of Core |  |
|  |  |  |  |  |  |  |  | Specification v5.2 with regard to LE Power Control CR |  |
|  |  |  |  |  |  |  |  | r07 (includes Issues 12116, 12112, 12115, 12117, |  |
|  |  |  |  |  |  |  |  | 12118, 12255). Added items 59–64 and notes C.14– |  |
|  |  |  |  |  |  |  |  | C.16 to Table 5; added item 10 and note C.7 to Table |  |
|  |  |  |  |  |  |  |  | 8; added item 18 and note 3.10 to Table 17. |  |
|  |  |  |  |  |  |  |  | TSE 11963 (rating 3): Updated ICS to match the Core |  |
|  |  |  |  |  |  |  |  | specification and to ensure that every command and |  |
|  |  |  |  |  |  |  |  | event is included. Added Table 0 Core Version table. |  |
|  |  |  |  |  |  |  |  | Removed table names. Aligned all conditional |  |
|  |  |  |  |  |  |  |  | numbering with Table 3.1: Alphabetical list of |  |
|  |  |  |  |  |  |  |  | commands and events found in the HCI Volume in the |  |
|  |  |  |  |  |  |  |  | Core specification. Added IUT Configuration column |  |
|  |  |  |  |  |  |  |  | to replace the column prerequisite structure and a |  |
|  |  |  |  |  |  |  |  | Core Version column to simplify conditionals. |  |
|  |  |  |  |  |  |  |  | Simplified the status into a single column. Added [v1] |  |
|  |  |  |  |  |  |  |  | to items 3/5 and 4/10. Added items 3/6–9, 4/13–17, |  |
|  |  |  |  |  |  |  |  | 6/45–49, 7/44–49, 8/5a, 8/5b, 8/8a, 8/8b, 8/11–14, |  |
|  |  |  |  |  |  |  |  | 9/12–13, 10/35–39, 12/22–27, 13/1a, 13/1b, 13/2a, |  |
|  |  |  |  |  |  |  |  | 13/2b, 13/13–14, 14/21–22, 15/2b, 15/2c, 15/3a, |  |
|  |  |  |  |  |  |  |  | 15/3b, 15/4a, 15/4b, 15/4c, 15/10, 16/37a, 16/37b, |  |
|  |  |  |  |  |  |  |  | 16/38a, 16/38b, 16/46a, 16/46b, 16/47a, 16/47b, |  |
|  |  |  |  |  |  |  |  | 16/48a, 16/48b, 16/54–67, 17/3a, 17/3b, and 17/19– |  |
|  |  |  |  |  |  |  |  | 22. Removed items 8/8, 15/2–4, 16/24, 16/37–38, |  |
|  |  |  |  |  |  |  |  | 16/46–48, and 17/3. Marked 12/11–16 as no longer |  |
|  |  |  |  |  |  |  |  | used. |  |
|  |  |  |  |  |  |  |  | TSE 12048 (rating 1): Added row to Table 12 to |  |
|  |  |  |  |  |  |  |  | account for items deleted for persistent sniff feature. |  |
|  |  |  |  |  |  |  |  | Fixed a numbering error in Table 17. |  |
|  |  |  |  |  |  |  |  | TSE 12110 (rating 1): Fixed references to align with |  |
|  |  |  |  |  |  |  |  | changes made in erratum 11876. |  |
|  |  |  |  |  |  |  |  | TSE 12779 (rating 2): Updated Table 4 status of item |  |
|  |  |  |  |  |  |  |  | 12 and deleted conditional C.4 to remove requirement |  |
|  |  |  |  |  |  |  |  | to support SUM ICS 21/17 (Erratum 10734); updated |  |
|  |  |  |  |  |  |  |  | Table 16 conditional C.15. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Issue 12714 (CR in comment 51978): Added a row to |  |
|  |  |  |  |  |  |  |  | Table 5. |  |
|  |  |  |  |  |  |  |  | Issue 12706 (CR in comment 52042): Updated Table |  |
|  |  |  |  |  |  |  |  | 5 item 10 Capability and Status and added three new |  |
|  |  |  |  |  |  |  |  | items (13–15) and two new conditionals (C.5 and |  |
|  |  |  |  |  |  |  |  | C.6); updated Table 5 with one new item (66) and one |  |
|  |  |  |  |  |  |  |  | new conditional (C.17). |  |
|  |  |  |  |  |  |  |  | Integration reviews in multiple rounds. Editorial |  |
|  |  |  |  |  |  |  |  | refinement in multiple steps, including corrected |  |
|  |  |  |  |  |  |  |  | references and smaller updates to changes that came |  |
|  |  |  |  |  |  |  |  | with TSE 11963. |  |
|  |  |  |  |  |  |  |  | Items 10/4 and 10/5 set to no longer used. |  |
|  |  |  |  |  |  |  |  | Revised document numbering convention, setting last |  |
|  |  |  |  |  |  |  |  | release publication of 5.1.1 as p23; added publication |  |
|  |  |  |  |  |  |  |  | number column to Revision History. Minor editorial |  |
|  |  |  |  |  |  |  |  | fixes. |  |
|  |  |  |  |  |  |  |  | Updated Contributors list. |  |
| 24 |  |  | p24 |  |  | 2020-01-07 |  | Approved by BTI on 2019-12-22. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2019-2 publication. |  |
|  |  |  | p25r00–r22 |  |  | 2020-02-25 – 2021-06-09 |  | TSE 13121 (rating 4): Added item 23 to Table 14 to |  |
|  |  |  |  |  |  |  |  | address issue with test written only for BR/EDR but |  |
|  |  |  |  |  |  |  |  | mapped to all transports. |  |
|  |  |  |  |  |  |  |  | TSE 13583 (rating 2): Updated “Read Buffer Size |  |
|  |  |  |  |  |  |  |  | command” item in Table 3 to accommodate spec |  |
|  |  |  |  |  |  |  |  | changes. |  |
|  |  |  |  |  |  |  |  | TSE 13587 (rating 2): Updated conditionals for Table |  |
|  |  |  |  |  |  |  |  | 3 to align with Erratum 13143 changes to the LE Read |  |
|  |  |  |  |  |  |  |  | Buffer Size conditional. |  |
|  |  |  |  |  |  |  |  | TSE 14635 (rating 2): Corrected errors in conditionals |  |
|  |  |  |  |  |  |  |  | in Tables 3, 5, 6, 7, 10, and 16. |  |
|  |  |  |  |  |  |  |  | TSE 14695 (rating 4): Added item 40 and note C.10 to |  |
|  |  |  |  |  |  |  |  | Table 10 to address Erratum 12379, adding an |  |
|  |  |  |  |  |  |  |  | HCI LE Set Data Related Address Changes |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ _ command. |  |
|  |  |  |  |  |  |  |  | TSE 14954 (rating 2): Updated the status for item 7 of |  |
|  |  |  |  |  |  |  |  | Table 3, updated C.44, and added new C.95 (number |  |
|  |  |  |  |  |  |  |  | assigned using final editor’s proof in spec Erratum |  |
|  |  |  |  |  |  |  |  | 14980). |  |
|  |  |  |  |  |  |  |  | TSE 14963 (rating 2): Updated the status for items 6 |  |
|  |  |  |  |  |  |  |  | and 7 of Table 9 and added new conditionals C.135a |  |
|  |  |  |  |  |  |  |  | and C.135b. |  |
|  |  |  |  |  |  |  |  | TSE 15025 (rating 2): Changed C.36 to delete “LL 1/4 |  |
|  |  |  |  |  |  |  |  | “Slave Role” OR case to address Erratum 14998. |  |
|  |  |  |  |  |  |  |  | TSE 15045 (rating 2): Updated note C.22 of Table 5 |  |
|  |  |  |  |  |  |  |  | per Erratum 15010, which updates the LE Path |  |
|  |  |  |  |  |  |  |  | Compensation conditionals. |  |
|  |  |  |  |  |  |  |  | TSE 15239 (rating 4): To address an issue with |  |
|  |  |  |  |  |  |  |  | adding Time Stamp as an optional feature to |  |
|  |  |  |  |  |  |  |  | _ “Isochronous data over HCI”, added new Item 6 and |  |
|  |  |  |  |  |  |  |  | conditional C.900 to Table 20. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | TSE 15270 (rating 4): To address Erratum 14893, |  |
|  |  |  |  |  |  |  |  | which addresses changes to the Read/Write |  |
|  |  |  |  |  |  |  |  | Connection Accept Timeout command for LE and |  |
|  |  |  |  |  |  |  |  | changes to the CIS request command, updated items |  |
|  |  |  |  |  |  |  |  | 12 and 13 of Table 7 and added C.40a conditional. |  |
|  |  |  |  |  |  |  |  | TSE 15290 (rating 2): To address Erratum 15233, |  |
|  |  |  |  |  |  |  |  | which updates conditionals for two HCI commands, |  |
|  |  |  |  |  |  |  |  | updated C.108 and items 18 and 19 of Table 5. |  |
|  |  |  |  |  |  |  |  | TSE 15433 (rating 1): Editorials to address Erratum |  |
|  |  |  |  |  |  |  |  | 15348, globally change “White List” to “Filter Accept |  |
|  |  |  |  |  |  |  |  | List”. |  |
|  |  |  |  |  |  |  |  | TSE 15448 (rating 1): Editorials to address Erratum |  |
|  |  |  |  |  |  |  |  | 15334, globally change “Master” to “Central” and |  |
|  |  |  |  |  |  |  |  | “Slave” to “Peripheral”. |  |
|  |  |  |  |  |  |  |  | TSE 15491 (rating 1): Editorials to address Erratum |  |
|  |  |  |  |  |  |  |  | 15328, in Table 16, change the command name from |  |
|  |  |  |  |  |  |  |  | “Master Link Key” to “Link Key Selection” and the |  |
|  |  |  |  |  |  |  |  | event name from “Master Link Key Complete” to “Link |  |
|  |  |  |  |  |  |  |  | Key Type Changed”. |  |
|  |  |  |  |  |  |  |  | TSE 15610 (rating 3): To address E15570 regarding |  |
|  |  |  |  |  |  |  |  | changes to conditionals in the ICS for some HCI |  |
|  |  |  |  |  |  |  |  | commands and events: updated status of Item 26 in |  |
|  |  |  |  |  |  |  |  | Table 6 and added C.63; updated status of Items 23, |  |
|  |  |  |  |  |  |  |  | 24, and 27 in Table 7 and added conditionals C.59, |  |
|  |  |  |  |  |  |  |  | C.62, and C.94; and updated status of Items 34–36 |  |
|  |  |  |  |  |  |  |  | and 39 in Table 16 and added conditionals C.60 and |  |
|  |  |  |  |  |  |  |  | C.61. |  |
|  |  |  |  |  |  |  |  | TSE 15914 (rating 1): To address E15233, updated |  |
|  |  |  |  |  |  |  |  | conditional C.108 and status for item 18 in Table 5. |  |
|  |  |  |  |  |  |  |  | TSE 16137 (rating 2): To address an issue raised in |  |
|  |  |  |  |  |  |  |  | E16142, changed item 44 in Table 5 from C.1 to C.64 |  |
|  |  |  |  |  |  |  |  | and added C.64 to the notes for that table. |  |
|  |  |  |  |  |  |  |  | TSE 16175 (rating 2): Changes made to conditionals |  |
|  |  |  |  |  |  |  |  | C.12, C.13, and C.29 as part of TSE 16235, above |  |
|  |  |  |  |  |  |  |  | (keeping TSE active to accommodate associated |  |
|  |  |  |  |  |  |  |  | TCW). |  |
|  |  |  |  |  |  |  |  | TSE 16235 (rating 2): Updated C.12, C.13, and C.29 |  |
|  |  |  |  |  |  |  |  | for Table 17 to address E16167. |  |
|  |  |  |  |  |  |  |  | Incorporated |  |
|  |  |  |  |  |  |  |  | Enhanced Connection Update TEST CR r17: |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ Added three new items and a new conditional to |  |
|  |  |  |  |  |  |  |  | Table 7, updated C.49 of Table 20; the reference to |  |
|  |  |  |  |  |  |  |  | the Core v5.3 release was already added under |  |
|  |  |  |  |  |  |  |  | Host To Controller Encryption Key Control |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ _ Enhancements TEST CR r06. _ _ _ |  |
|  |  |  |  |  |  |  |  | Incorporated |  |
|  |  |  |  |  |  |  |  | Host To Controller Encryption Key Control |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ _ Enhancements TEST CR r06: Added to the |  |
|  |  |  |  |  |  |  |  | _ _ _ References list a reference to v5.3 of the HCI |  |
|  |  |  |  |  |  |  |  | volume/part of the Core spec; updated Table 16 by |  |
|  |  |  |  |  |  |  |  | modifying items 37a and 37b, adding items 37c, 37d, |  |
|  |  |  |  |  |  |  |  | and 68, and adding related conditionals to be |  |
|  |  |  |  |  |  |  |  | numbered later. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Incorporated |  |
|  |  |  |  |  |  |  |  | LE Channel Classification TEST CR r07: Added |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ item to Table 0 for Core v5.3; added items 3a and 4a |  |
|  |  |  |  |  |  |  |  | to Table 13, as well as associated conditional; |  |
|  |  |  |  |  |  |  |  | modified conditional C.36 for Table 13. |  |
|  |  |  |  |  |  |  |  | Incorporated Removing AMP TEST CRr03a: Added |  |
|  |  |  |  |  |  |  |  | _ _ _ Removing AMP section to the Conditional Text |  |
|  |  |  |  |  |  |  |  | section; added C.901 and updated Status of item 3 in |  |
|  |  |  |  |  |  |  |  | Table 1a. |  |
|  |  |  |  |  |  |  |  | Template-related editorials. |  |
| 25 |  |  | p25 |  |  | 2021-07-13 |  | Approved by BTI on 2021-06-27. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2021-1 publication. |  |
|  |  |  | p25ed2r00 |  |  | 2021-07-26 |  | TSE 17283 (rating 1): Deleted a conditional no longer |  |
|  |  |  |  |  |  |  |  | relevant to Table 6. |  |
|  |  |  | p25 edition 2 |  |  | 2021-08-20 |  | Approved by BTI on 2021-08-19. Prepared for |  |
|  |  |  |  |  |  |  |  | edition 2 publication. |  |
|  |  |  | p26r00–r04 |  |  | 2021-08-31 – 2022-01-04 |  | TSE 16890 (rating 2): Updated C.15 of Table 6. |  |
|  |  |  |  |  |  |  |  | TSE 17150 (rating 2): To address E17069 “HCI |  |
|  |  |  |  |  |  |  |  | Remote OOB Extended Data Request Reply |  |
|  |  |  |  |  |  |  |  | command ICS conditional changed”, deleted C.143 |  |
|  |  |  |  |  |  |  |  | from Table 16 and changed status of item 43 to |  |
|  |  |  |  |  |  |  |  | C.142. |  |
|  |  |  |  |  |  |  |  | TSE 16960 (rating 2): To accommodate E16908, |  |
|  |  |  |  |  |  |  |  | Changes to HCI commands related Sync Train / Sync |  |
|  |  |  |  |  |  |  |  | Scan ICS conditionals, updated Table 18 to remove |  |
|  |  |  |  |  |  |  |  | C.203 and C.204 and changed Status for items 3, 4, |  |
|  |  |  |  |  |  |  |  | 8, 9, 10, and 11. |  |
|  |  |  |  |  |  |  |  | TSE 17515 (rating 2): To address E17510, updated |  |
|  |  |  |  |  |  |  |  | Table 14: IUT Config of items 15 and 16 and text of |  |
|  |  |  |  |  |  |  |  | C.153a. |  |
|  |  |  |  |  |  |  |  | TSE 17654 (rating 2): Added prerequisites to all |  |
|  |  |  |  |  |  |  |  | tables to address an issue with limiting IUT |  |
|  |  |  |  |  |  |  |  | configurations to Control configurations. |  |
|  |  |  |  |  |  |  |  | Consistency checker editorials. Updated copyright |  |
|  |  |  |  |  |  |  |  | page to align with v2 of the DNMD. |  |
| 26 |  |  | p26 |  |  | 2022-01-25 |  | Approved by BTI on 2021-12-27. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2021-2 publication. |  |
|  |  |  | p27r00–r04 |  |  | 2022-04-06 – 2022-05-03 |  | TSE 18513 (rating 2): Added a Core Version to 6/29. |  |
|  |  |  |  |  |  |  |  | TSE 18514 (rating 2): Updated 20/6 to “HCI 0/3 “5.2 |  |
|  |  |  |  |  |  |  |  | or later””. |  |
|  |  |  |  |  |  |  |  | TSE 18894 (rating 2): De-integrated TSE 16960 |  |
|  |  |  |  |  |  |  |  | changes, as they were prematurely integrated with |  |
|  |  |  |  |  |  |  |  | respect to the related Erratum 16908, which is not yet |  |
|  |  |  |  |  |  |  |  | released. Added C.203 and C.204 back to Table 18 |  |
|  |  |  |  |  |  |  |  | and updated statuses for 18/3, 18/4, and 18/8–18/11 |  |
|  |  |  |  |  |  |  |  | accordingly. |  |
|  |  |  |  |  |  |  |  | Editorials (template, consistency checker). |  |
| 27 |  |  | p27 |  |  | 2022-06-28 |  | Approved by BTI on 2022-05-31. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2022-1 publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p28r00–r06 | p28r00–r06 |  | 2022-09-27 – 2022-12-21 |  | TSE 20619 (rating 2): Set 1a/2, the host configuration, |  |
|  |  |  |  |  |  |  |  | to "No longer used” and updated C.1. Removed |  |
|  |  |  |  |  |  |  |  | prerequisites from Tables 1–20. |  |
|  |  |  |  |  |  |  |  | Core v5.4 CRs: |  |
|  |  |  |  |  |  |  |  | CSSA (from CR Coding Scheme Selection on |  |
|  |  |  |  |  |  |  |  | _ _ _ _ Advertising Test CR r08): Added new item 0/5. |  |
|  |  |  |  |  |  |  |  | _ _ _ Updated item 5/34, added 5/34a, and added related |  |
|  |  |  |  |  |  |  |  | conditionals C.65 ad C.66. |  |
|  |  |  |  |  |  |  |  | PAwR (from CR |  |
|  |  |  |  |  |  |  |  | Periodic Advertising with Responses TEST |  |
|  |  |  |  |  |  |  |  | _ _ _ _ _ CR r22): Added item 0/5; modified item 5/35 and |  |
|  |  |  |  |  |  |  |  | _ added items 5/35a, 5/67, 5/68, and 5/69 and related |  |
|  |  |  |  |  |  |  |  | C.67; modified items 6/33 and 6/35 and added items |  |
|  |  |  |  |  |  |  |  | 6/33a, 6/35a, 6/50, and 6/51 and related C.68; |  |
|  |  |  |  |  |  |  |  | updated 7/38 and 7/41 and added 7/38a and 7/41a |  |
|  |  |  |  |  |  |  |  | and related C.67 and C.69; modified 10/26 and added |  |
|  |  |  |  |  |  |  |  | 10/26a and related C.68. |  |
| 28 |  |  | p28 |  |  | 2023-02-07 |  | Approved by BTI on 2022-12-28. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2022-2 publication. |  |
|  |  |  | p29r00–r10 |  |  | 2023-08-08 – 2024-01-04 |  | TSE 23188 (rating 2): Added conditional C.206 to |  |
|  |  |  |  |  |  |  |  | Table 9 and updated the Status column for 9/8. |  |
|  |  |  |  |  |  |  |  | TSE 23209 (rating 3): To accommodate changes |  |
|  |  |  |  |  |  |  |  | needed to support E18552, added item 10/31a and |  |
|  |  |  |  |  |  |  |  | conditional C.159. |  |
|  |  |  |  |  |  |  |  | TSE 23253 (rating 2): Removed C.203 and C.204 |  |
|  |  |  |  |  |  |  |  | from Table 18. Updated the conditionals for 18/3, |  |
|  |  |  |  |  |  |  |  | 18/4, 18/8, 18/9, 18/10, and 18/11. |  |
|  |  |  |  |  |  |  |  | TSE 23581 (rating 1): In the References section, |  |
|  |  |  |  |  |  |  |  | removed the references for Core v1.2, CSA4, and |  |
|  |  |  |  |  |  |  |  | CSA3 and removed the footnote from Core v5.2. |  |
|  |  |  |  |  |  |  |  | Added a reference for Core v5.4. Updated cross-refs |  |
|  |  |  |  |  |  |  |  | throughout the ICS accordingly. Corrected the Core |  |
|  |  |  |  |  |  |  |  | Version for 16/51a and added a Core Version for |  |
|  |  |  |  |  |  |  |  | 16/68. |  |
|  |  |  |  |  |  |  |  | TSE 24072 (rating 2): Removed Table 0. Updated |  |
|  |  |  |  |  |  |  |  | references to the previous Table 0 and to SUM.ICS to |  |
|  |  |  |  |  |  |  |  | Core.ICS references in C.901, the “Capability |  |
|  |  |  |  |  |  |  |  | statement” section intro, and items 3/6–3/9, 4/11, |  |
|  |  |  |  |  |  |  |  | 4/13–4/15, 5/33–5/69, 6/27–6/44, 6/50, 6/51, 7/38a, |  |
|  |  |  |  |  |  |  |  | 7/41–7/43, 7/50–7/52, 8/9, 8/10, 10/18–10/34, 10/40, |  |
|  |  |  |  |  |  |  |  | 13/3a, 13/4a, 13/9–13/12, 14/17–4/20, 15/9, 16/18, |  |
|  |  |  |  |  |  |  |  | 16/51a, 16/68, 17/10–17/18, and 20/1–20/6. |  |
|  |  |  |  |  |  |  |  | TSE 24547 (rating 1): Set 20/6 to “no longer used” |  |
|  |  |  |  |  |  |  |  | and deleted associated C.900 from the conditionals |  |
|  |  |  |  |  |  |  |  | list. |  |
|  |  |  |  |  |  |  |  | TSE 24764 (rating 1): Updated C.135a to C.902 and |  |
|  |  |  |  |  |  |  |  | C.135b to C.903 per current document conventions. |  |
|  |  |  |  |  |  |  |  | Updated items 9/6 and 9/7 accordingly. |  |
|  |  |  |  |  |  |  |  | TSE 24767 (rating 1): Set the configuration for |  |
|  |  |  |  |  |  |  |  | HCI 16/18 to “HCI 1a/1 “BR/EDR””. |  |
| 29 |  |  | p29 |  |  | 2024-07-01 |  | Approved by BTI on 2024-05-22. Prepared for |  |
|  |  |  |  |  |  |  |  | TCRL 2024-1 publication. |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  | p30r00–r15 | p30r00–r15 |  | 2024-05-20 – 2024-08-01 |  | Incorporated changes from Decision Based |  |
|  |  |  |  |  |  |  |  | _ _ Advertising Filtering TEST CR r17: Added Items 70 |  |
|  |  |  |  |  |  |  |  | _ _ _ _ and 71 and notes C.73 and C.74. to Table 5. |  |
|  |  |  |  |  |  |  |  | Integrated the following test issues for Core v6.0: |  |
|  |  |  |  |  |  |  |  | 20399 (TI 18581, 18583, 18584, 18928, 19316, |  |
|  |  |  |  |  |  |  |  | 19330, 19331), 20408, 20411 – 20415, 20418, 20462, |  |
|  |  |  |  |  |  |  |  | 20468, 20517, 20523, 20555, 20563, 20565, 22454, |  |
|  |  |  |  |  |  |  |  | 22455, 22472, 22497, 22907, 22915, 23436, 24156, |  |
|  |  |  |  |  |  |  |  | and 24788. |  |
|  |  |  |  |  |  |  |  | Incorporated changes from Monitoring |  |
|  |  |  |  |  |  |  |  | Advertising Test CR r02: Added Items 72–77 and |  |
|  |  |  |  |  |  |  |  | _ _ _ note C. 78 to Table 5. |  |
|  |  |  |  |  |  |  |  | Updated references from SUM ICS to CORE ICS per |  |
|  |  |  |  |  |  |  |  | Jörg’s updated CR: Decision Based Advertising |  |
|  |  |  |  |  |  |  |  | _ _ _ Filtering TEST CR r17-Jorg. _ _ _ |  |
|  |  |  |  |  |  |  |  | Incorporated CR Frame Space Update Test CR r08 |  |
|  |  |  |  |  |  |  |  | _ _ _ (which includes Test Issues 25371, 25444, 25452, |  |
|  |  |  |  |  |  |  |  | 25453, 25470, 25471, 25475). To account for the |  |
|  |  |  |  |  |  |  |  | Frame Space Update feature in Core Specification |  |
|  |  |  |  |  |  |  |  | v6.0, performed the following updates: Added Items |  |
|  |  |  |  |  |  |  |  | 13/15 and 13/16 and conditional C.79 to Table 13. |  |
|  |  |  |  |  |  |  |  | Updated the references list. |  |
|  |  |  |  |  |  |  |  | Incorporated CR Core LLExtendedFeatureSet |  |
|  |  |  |  |  |  |  |  | _ _ Test CRr11-Jorg (which includes Test issues 24450, |  |
|  |  |  |  |  |  |  |  | _ 24696, 24807, 24896, 24905). To account for the Low |  |
|  |  |  |  |  |  |  |  | Energy Extended Feature Set feature in Core |  |
|  |  |  |  |  |  |  |  | Specification v6.0, updated Item 4/8, added Item 4/18 |  |
|  |  |  |  |  |  |  |  | and C.70 in Table 4. Updated Items 8/6 and 8/7 and |  |
|  |  |  |  |  |  |  |  | added Items 8/15 and 8/16 and conditionals C.71 and |  |
|  |  |  |  |  |  |  |  | C.72 in Table 8. Updated the references list. |  |
|  |  |  |  |  |  |  |  | Incorporated the changed parts of the Monitoring |  |
|  |  |  |  |  |  |  |  | Advertising Test |  |
|  |  |  |  |  |  |  |  | _ _ CR r03 (changes only for Test Issue 25248). _ |  |
|  |  |  |  |  |  |  |  | Incorporated CR CS Test CR r16-jorg (which |  |
|  |  |  |  |  |  |  |  | _ _ _ includes Test issues 23205, 23293, 23331, 23332, |  |
|  |  |  |  |  |  |  |  | 23361, 23362, 23363, 23364, 23365, 23378, 23379, |  |
|  |  |  |  |  |  |  |  | 23381, 23382, 23384, 23404, 23419, 23422, 23424, |  |
|  |  |  |  |  |  |  |  | 23425, 23500, 23501, 23502, 23503, 23504, 23506, |  |
|  |  |  |  |  |  |  |  | 23594, 23693, 23694, 23696, 23701, 23706, 23711, |  |
|  |  |  |  |  |  |  |  | 23732, 23736, 23737, 23738, 23776, 23842, 23923, |  |
|  |  |  |  |  |  |  |  | 23993, 24023, 24033, 24043, 24049, 24133, 24135, |  |
|  |  |  |  |  |  |  |  | 24137, 24138, 24139, 24141, 24142, 24143, 24146, |  |
|  |  |  |  |  |  |  |  | 24147, 24149, 24150, 24151, 24153, 24177, 24181, |  |
|  |  |  |  |  |  |  |  | 24231, 24232, 24330, 24331, 24332, 24410, 24411, |  |
|  |  |  |  |  |  |  |  | 24418, 24419, 24478, 24483, 24515, 24531, 24599, |  |
|  |  |  |  |  |  |  |  | 24601, 24602, 24614, 24618, 24619, 24621, 24623, |  |
|  |  |  |  |  |  |  |  | 24624, 24625, 24627, 24630, 24639, 24645, 24646, |  |
|  |  |  |  |  |  |  |  | 24655, 24656, 24657, 24659, 24660, 24669, 24681, |  |
|  |  |  |  |  |  |  |  | 24717, 24769, 24776, 24789, 24808, 24809, 24838, |  |
|  |  |  |  |  |  |  |  | 24844, 24850, 24867, 24868, 24893, 24894, 24895, |  |
|  |  |  |  |  |  |  |  | 25028, 25029, 25040, 25042, 25053, 25055, 25111, |  |
|  |  |  |  |  |  |  |  | 25112, 25120, 25139, 25140, 25141, 25142, 25143, |  |
|  |  |  |  |  |  |  |  | 25148, 25149, 25150, 25157, 25166, 25209, 25240, |  |
|  |  |  |  |  |  |  |  | 25278, 25282, 25299, 25428, 25443, 25479, 25498, |  |


|  | Publication |  |  | Revision |  | Date | Comments |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Number |  |  | Number |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 25511, 25512, 25525, 25585, 25617, 25632). To |  |
|  |  |  |  |  |  |  |  | account for the Channel Sounding feature in Core |  |
|  |  |  |  |  |  |  |  | Specification v6.0, updated C.49 for Table 20 and |  |
|  |  |  |  |  |  |  |  | added Table 21. |  |
|  |  |  |  |  |  |  |  | TSE 25664 (rating 2): Per E25658, updated |  |
|  |  |  |  |  |  |  |  | conditional C.142 for Table 16. |  |
|  |  |  |  |  |  |  |  | Incorporated integration review feedback and made |  |
|  |  |  |  |  |  |  |  | template-related and consistency checker editorial |  |
|  |  |  |  |  |  |  |  | updates. |  |
| 30 |  |  | p30 |  |  | 2024-09-04 |  | Approved by BTI on 2024-08-14. Prepared for TCRL |  |
|  |  |  |  |  |  |  |  | 2024-2 publication. |  |

Acknowledgments

|  | Name |  |  | Company |  |
| --- | --- | --- | --- | --- | --- |
|  | Juan Manuel Hidalgo |  |  | AT4wireless |  |
|  | Fransisco Narvaez |  |  | AT4wireless |  |
|  | Elisa Rincón |  |  | AT4wireless |  |
|  | Nathan Burns |  |  | Bluetooth SIG, Inc. |  |
|  | Gene Chang |  |  | Bluetooth SIG, Inc. |  |
|  | Virgil Dragomir |  |  | Bluetooth SIG, Inc. |  |
|  | Jeff Drake |  |  | Bluetooth SIG, Inc. |  |
|  | Tharon Hall |  |  | Bluetooth SIG, Inc. |  |
|  | Mayank Batra |  |  | Cambridge Silicon Radio |  |
|  | Peter Flittner |  |  | Cambridge Silicon Radio |  |
|  | Robin Heydon |  |  | Cambridge Silicon Radio |  |
|  | Steven Wenham |  |  | Cambridge Silicon Radio |  |
|  | Fabien Duvoux |  |  | Ellisys |  |
|  | Kyle Penri-Williams |  |  | Ellisys |  |
|  | Clement Vacheron |  |  | Ellisys |  |
|  | Jimmy Karlsson |  |  | Intel |  |
|  | Chris Church |  |  | Qualcomm |  |
|  | Magnus Sommansson |  |  | Qualcomm |  |
|  | Clive D.W. Feather |  |  | Samsung Electronics Co., Ltd. |  |
|  | Ben Brown |  |  | Teledyne LeCroy |  |
|  | Martti Söderlund |  |  | TietoEnator |  |
