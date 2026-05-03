# Core Specification Addendum (CSA) 6

> Source: PDF converted via PyMuPDF.

---

Addendum 6
Disclaimer and Copyright Notice
Use of this specification is your acknowledgement that you agree to and will comply with the following notices and disclaimers. You are advised to seek appropriate legal, engineering, and other professional advice regarding the use, interpretation, and effect of this specification.
Use of Bluetooth specifications by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG and its members, including those agreements posted on Bluetooth SIG's website located at www.bluetooth.com. Any use of this specification by a member that is not in compliance with the applicable membership and other related agreements is prohibited and, among other things, may result in (i) termination of the applicable agreements and (ii) liability for infringement of the intellectual property rights of Bluetooth SIG and its members.
Use of this specification by anyone who is not a member of Bluetooth SIG is prohibited and is an infringement of the intellectual property rights of Bluetooth SIG and its members. The furnishing of this specification does not grant any license to any intellectual property of Bluetooth SIG or its members. THIS SPECIFICATION IS PROVIDED "AS IS" AND BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTIES OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, OR THAT THE CONTENT OF THIS SPECIFICATION IS FREE OF ERRORS. For the avoidance of doubt, Bluetooth SIG has not made any search or investigation as to third parties that may claim rights in or to any specifications or any intellectual property that may be required to implement any specifications and it disclaims any obligation or duty to do so.
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, BLUETOOTH SIG, ITS MEMBERS AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS SPECIFICATION AND ANY INFORMATION CONTAINED IN THIS SPECIFICATION, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF THE DAMAGES.
If this specification is a prototyping specification, it is solely for the purpose of developing and using prototypes to verify the prototyping specifications at Bluetooth SIG sponsored IOP events. Prototyping Specifications cannot be used to develop products for sale or distribution and prototypes cannot be qualified for distribution.
Products equipped with Bluetooth wireless technology ("Bluetooth Products") and their combination, operation, use, implementation, and distribution may be subject to regulatory controls under the laws and regulations of numerous countries that regulate products that use wireless non-licensed spectrum. Examples include airline regulations, telecommunications regulations, technology transfer controls and health and safety regulations. You are solely responsible for complying with all applicable laws and regulations and for obtaining any and all required authorizations, permits, or licenses in connection with your use of this specification and development, manufacture, and distribution of Bluetooth Products. Nothing in this specification provides any information or assistance in connection with complying with applicable laws or regulations or obtaining required authorizations, permits, or licenses.
Bluetooth SIG is not required to adopt any specification or portion thereof. If this specification is not the final version adopted by Bluetooth SIG's Board of Directors, it may not be adopted. Any specification adopted by Bluetooth SIG's Board of Directors may be withdrawn, replaced, or modified at any time. Bluetooth SIG reserves the right to change or alter final specifications in accordance with its membership and operating agreements.
Copyright © 1999–2017. All copyrights in the Bluetooth Specifications themselves are owned by Apple Inc., Ericsson AB, Intel Corporation, Lenovo (Singapore) Pte. Ltd., Microsoft Corporation, Nokia Corporation, and Toshiba Corporation. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.
ABOUT ADDENDUM 6
This addendum provides an optional update to the Bluetooth® Core Specification. When the addendum is applied to an allowed Core Specification (see Volume 1, Part D, Section 1.2, Table 1.3), the following parts of the specification shall be replaced, added, or appended with the revised versions:
Volume 0 Part B Bluetooth Compliance Requirements
Volume 1 Part A Architecture
Part D Mixing of Specification Versions
Master Table of Contents &  Compliance Requirements
Part B
PART B: BLUETOOTH COMPLIANCE REQUIREMENTS
This document specifies the requirements for Bluetooth compliance.
CONTENTS

## 1  INTRODUCTION

The Bluetooth Qualification Program Reference Document (PRD) is the primary reference document for the Bluetooth Qualification Program and defines its requirements, functions, and policies. The PRD is available on the Bluetooth Web site.
Passing the Bluetooth Qualification Process demonstrates a certain measure of compliance and interoperability, but because products are not tested for every aspect of this Bluetooth Specification, qualification does not guarantee compliance. Passing the Bluetooth Qualification Process only satisfies one condition of the license grant. The Member has the ultimate responsibility to ensure that the qualified product complies with this Bluetooth Specification and interoperates with other products.

## 2  SCOPE

This part of the specification defines some fundamental concepts used in the Bluetooth Qualification Program.

## 3  DEFINITIONS

Bluetooth Qualification Process – The process defined in the Bluetooth Qualification Program Reference Document (PRD) to qualify a design used in implementations of Bluetooth wireless technology.
Bluetooth Qualification Program – The Bluetooth Qualification Process together with other related requirements and processes.

### 3.1   TYPES OF BLUETOOTH PRODUCTS

Bluetooth Product — Any product containing an implementation of Bluetooth wireless technology. Bluetooth Products as defined herein may require enabling technology external to Bluetooth Scope, as defined by the Patent and Copyright License Agreement, to become functional (e.g. power supply, technology capable of running executable code, etc.). Enabling technology is not part of any of the Bluetooth Product type definitions and is not included in the Bluetooth License grant.
All Bluetooth Products shall be one of the following:
• Bluetooth End Product
• Bluetooth Host Subsystem Product
• Bluetooth Controller Subsystem Product
• Bluetooth Profile Subsystem Product
• Bluetooth Component Product
• Bluetooth Development Tool
• Bluetooth Test Equipment.
Table 3.1 defines abbreviations for the different Core Configurations defined in Section 4.

| Abbreviation | Explanation | Section Reference |
| --- | --- | --- |
| BR CC | Bluetooth Basic Rate Core Configuration | Section 4.1 |
| EDR CC | Bluetooth Enhanced Data Rate Core Configuration | Section 4.2 |
| HS CC | High Speed Bluetooth Core Configuration | Section 4.3 |
| LE CC | Bluetooth Low Energy Core Configuration | Section 4.4 |
| BR and LE Combined CC | Bluetooth Basic Rate and Low Energy Combined Core Configuration | Section 4.5 |
| HCI CC | Host Controller Interface Core Configuration | Section 4.6 |

Table 3.1:  Core Configuration abbreviations
Using the abbreviations in Table 3.1 the following tables define Bluetooth product types in terms of Core Configurations. For the respective Core Configuration, the letter “M” indicates that it is mandatory to claim support, “O” indicates that it is optional to claim support, “P” indicates that it is optionally permitted to claim only partial support of the Core Configuration, “I” indicates that the Core Configuration is inherently included in the combined Core Configuration, “E” indicates that support for the Core Configuration shall not be claimed.

#### 3.1.1  Bluetooth End Product

A Bluetooth End Product is a Bluetooth product that claims to implement one or more Core Configurations, in compliance with the required parts of the Specification, and in accordance with the mandatory requirements as defined herein. Complementary products for Bluetooth End Products are limited to only Bluetooth Profile Subsystem Products. The Bluetooth End Product types are defined in Table 3.2.

|  | BR CC | EDR CC | HS CC | BR and LE Combined CC | LE CC | HCI CC |
| --- | --- | --- | --- | --- | --- | --- |
| BR End Product | M | P | P | E | E | O |
| EDR End Product | M | M | P | E | E | O |
| HS End Product | M | M | M | E | E | O |
| LE End Product | E | E | E | E | M | O |
| BR and LE End Product | I | P | P | M | I | O |
| EDR and LE End Product | I | M | P | M | I | O |
| HS and LE End Product | I | M | M | M | I | O |

Table 3.2:  Required configuration per Bluetooth End Product type

#### 3.1.2  Bluetooth Subsystem Product

A Bluetooth Subsystem Product is a Bluetooth product that claims to implement only a portion of the Specification, in compliance with such portion of the Specification, and in accordance with the mandatory requirements as defined herein. Bluetooth Subsystem Products can be qualified solely for distribution; the use of Bluetooth wireless technology in Bluetooth Subsystem Products requires such Bluetooth Subsystem Products to be combined with one or more complementary products such that the resulting combination satisfies the requirements of a Bluetooth End Product. Complementary
products used in combinations are limited to those complementary products specified in each of the product definitions.
There are three types of Bluetooth Subsystem Products defined:
1. Bluetooth Host Subsystem Product
2. Bluetooth Controller Subsystem Product
3. Bluetooth Profile Subsystem Product.
A Bluetooth Subsystem Product shall be one of these types.

##### 3.1.2.1  Bluetooth Host Subsystem Product

The required configuration for each Bluetooth Host Subsystem Product type is listed in Table 3.3.

|  | BR CC Host Parts | HS CC Host Parts | BR and LE Combined CC Host Parts | LE CC Host Parts | HCI C |
| --- | --- | --- | --- | --- | --- |
| BR/EDR Host Subsystem Product | M | P | E | E | M |
| HS Host Subsystem Product | M | M | E | E | M |
| LE Host Subsystem Product | E | E | E | M | M |
| BR/EDR and LE Host Subsystem Product | I | P | M | I | M |
| HS and LE Host Subsystem Product | I | M | M | I | M |

Table 3.3:  Required configuration per Bluetooth Host Subsystem Product type
A Bluetooth Host Subsystem Product may contain, in addition to the required Core Configuration Host parts (as defined in Table 3.3), all the mandatory requirements defined in one or more of the protocols and profiles above HCI. Protocols below HCI required by the Core Configuration Controller parts (as defined in Table 3.4) shall be excluded from the Host Subsystem Product. Complementary products for Bluetooth Host Subsystem Products are limited to:
a) Bluetooth Controller Subsystem Products that implement and use the HCI ([Vol 2] Part E) for communication between the subsystems; and
b) Bluetooth Profile Subsystem Products when the Bluetooth Host Subsystem is combined with a Bluetooth Controller Subsystem Product.

##### 3.1.2.2  Bluetooth Controller Subsystem Product

The required configuration for each Bluetooth Controller Subsystem Product type is listed in Table 3.4.

|  | BR CC Controller Parts | EDR CC Controller Parts | HS CC Controller Parts | BR and LE Combined CC Controller Parts | LE CC Controller H Parts |
| --- | --- | --- | --- | --- | --- |
| BR Controller Subsystem Product | M | P | P | E | E |
| EDR Control- ler Subsys- tem Product | M | M | P | E | E |
| HS Controller Subsystem Product | M | M | M | E | E |
| HS only Con- troller Subsys- tem Product | E | E | M | E | E |
| LE Controller Subsystem Product | E | E | E | E | M |
| BR and LE Controller Subsystem Product | I | P | P | M | I |
| EDR and LE Controller Subsystem Product | I | M | P | M | I |
| HS and LE Controller Subsystem Product | I | M | M | M | I |

Table 3.4:  Required configuration per Bluetooth Controller Subsystem Product type
A Bluetooth Controller Subsystem Product shall be limited to the Controller parts of the Core Configurations. Protocols and Profiles above HCI required by the Core Configuration Host parts (as defined in Table 3.3) shall be excluded from the Controller Subsystem Product. Complementary products for Bluetooth Controller Subsystem Products are limited to Bluetooth Host Subsystem Products that implement and use the HCI ([Vol 2] Part E) for communication between the subsystems.

##### 3.1.2.3  Bluetooth Profile Subsystem Product

A Bluetooth Profile Subsystem Product is a Bluetooth product that claims to implement, at a minimum, all the mandatory requirements defined in one or more of the profile or service profile, service, or model specifications. Complementary products for Bluetooth Profile Subsystem Products are limited to:
a) Bluetooth Host Subsystem Products when combined with a Bluetooth Controller Subsystem Product; and
b) Bluetooth End Products.

#### 3.1.3  Bluetooth Component Product

A Bluetooth Component Product is a Bluetooth product that claims to implement, at a minimum, all the mandatory requirements, if any, of either one or more of any of the protocol and profile or service protocol, profile, service, or model parts of the Specification in compliance with such portion of the Specification. Bluetooth Component Products can be qualified solely for distribution and the use of the Bluetooth wireless technology in Bluetooth Component Products require such Bluetooth Component Products to be incorporated in Bluetooth End Products or Bluetooth Subsystem Products. A product that meets the requirements of a Bluetooth End Product or Bluetooth Subsystem product may be qualified as a Bluetooth Component Product if a manufacturer determines that further integration is necessary prior to qualifying the product as a Bluetooth End Product or Bluetooth Subsystem Product.

#### 3.1.4  Bluetooth Development Tool

A Bluetooth Development Tool is a Bluetooth product intended to facilitate the development of new Bluetooth designs. Bluetooth Development Tools can be qualified solely for distribution and the use of the Bluetooth wireless technology in development of new Bluetooth Products.

#### 3.1.5  Bluetooth Test Equipment

A Bluetooth Test Equipment is a Bluetooth product intended to facilitate the testing of new Bluetooth Products. Bluetooth Test Equipment can be qualified solely for distribution and the use of the Bluetooth wireless technology in testing of new Bluetooth Products. Where necessary, Bluetooth Test Equipment may deviate from the Specification in order to fulfill the test purposes in the Bluetooth Test Specifications.

## 4  CORE CONFIGURATIONS

This section defines the set of features that are required for a product to be qualified to a specification name. The Core Specification version number is simply the version number of the specification itself.
Specification names differ from Core Specification version numbers in that products are marked based on meeting requirements for a Core Configuration together with the mixing requirements (see [Vol 1] Part D, Section 1).
Each Core Configuration is defined by a set of parts and individual features of the Core Specification that shall be supported to allow the configuration name to be used. The configuration requirements imposed on a device may depend on the profiles that it supports.

### 4.1   BASIC RATE CORE CONFIGURATION

This section specifies compliance requirements for the “Basic Rate” Core Configuration.
To claim support to the “Basic Rate” Core Configuration, an implementation must support a set of Required Features, according to the details in Table 4.1 and Table 4.2.
Host Part:

| Layer | Required Features |
| --- | --- |
| L2CAP ([Vol 3] Part A) | L2CAP Signaling Channel (CID 0x0001) and all mandatory features associated with it |
| SDP ([Vol 3] Part B) | All mandatory features |
| ATT ([Vol 3] Part F) | If ATT is supported, all mandatory features |
| GATT ([Vol 3] Part G) | GATT is mandatory when ATT is supported. When supported all mandatory features |
| GAP ([Vol 3] Part C) | All mandatory features in sections 2 through 8 and section 15 |

Table 4.1:  BR Core Configuration Host requirements
Controller Part:

| Layer | Required Features |
| --- | --- |
| RF ([Vol 2] Part A) | All mandatory features |
| BB ([Vol 2] Part B) | All mandatory features |
| LMP ([Vol 2] Part C) | All mandatory features |

Table 4.2:  BR Core Configuration Controller requirements

### 4.2   ENHANCED DATA RATE CORE CONFIGURATIONS

This section specifies compliance requirements for the “Enhanced Data Rate” Core Configuration.
Table 4.3 defines three categories of Transport Requirements that shall be satisfied subject to the following rules:
• A Bluetooth product shall support category 1 whenever it supports asynchronous transports for the profiles it incorporates.
• A Bluetooth product shall support category 2 whenever it supports asynchronous transports with multislot ACL packets for the profiles it incorporates.
• A Bluetooth product shall support category 3 whenever it supports eSCO synchronous transports for the profiles it incorporates.
A multi-profile product shall support all applicable categories in order to claim support for the Enhanced Data Rate Core Configuration.

| Category No. | Transport Requirements | Controller Part | Host Part |
| --- | --- | --- | --- |
|  |  | LMP Features Supported | L2CAP Featur Bits Required |
| 1 | EDR for asynchronous transports (single slot) | Enhanced Data Rate ACL 2 Mb/s mode (25) AND Enhanced Data Rate ACL 3 Mb/s mode (26) | None |
| 2 | EDR for asynchronous transports (multi-slot) | 3-slot Enhanced Data Rate ACL packets (39) AND 5-slot Enhanced Data Rate ACL packets (40) | None |
| 3 | EDR for synchronous trans- ports | Enhanced Data Rate eSCO 2 Mb/s mode (45) | None |

Table 4.3:  EDR Core Configuration requirements
Note: No additional requirements are stated on the support of 3-EV3, 2-EV5 and 3-EV5 packets.

### 4.3   HIGH SPEED CORE CONFIGURATION

This section specifies compliance requirements for the “High Speed” Core Configuration.
To claim support to the “High Speed” Core Configuration, an implementation must support a set of Required Features, according to the details in Table 4.4 and Table 4.5.
Host Part:

| Layer | Required Features |
| --- | --- |
| L2CAP ([Vol 3] Part A) | Enhanced Retransmission Mode (L2CAP extended features mask number 3) Fixed Channels (L2CAP extended features mask number 7) AMP Manager Fixed Channel (CID 0x0003) AMP Channel Creation and Handling ([Vol 3] Part A, Section 9 |
| A2MP ([Vol 3] Part E) | All mandatory features |

Table 4.4:  HS Core Configuration Host requirements
Controller Part:

| Layer | Required Features |
| --- | --- |
| 802.11 PAL ([Vol 5] Part A) | All mandatory features |

Table 4.5:  HS Core Configuration Controller requirements

### 4.4   LOW ENERGY CORE CONFIGURATION

This section specifies compliance requirements for the “Low Energy” Core Configuration.
To claim support to the “Low Energy” Core Configuration, an implementation must support a set of Required Features, according to the details in Table 4.6 and Table 4.7.
Host Part:

| Layer | Required Features |
| --- | --- |
| L2CAP ([Vol 3] Part A) | If the GAP Peripheral or Central role is supported, L2CAP LE Signaling Channel (CID 0x0005) and all mandatory features associated with it |
| GAP ([Vol 3] Part C) | All mandatory features for at least one of the LE GAP roles (Broadcaster, Observer, Peripheral or Central) in sections 9-1 and section 15 |

Table 4.6:  LE Core Configuration Host requirements

| Layer | Required Features |
| --- | --- |
| ATT ([Vol 3] Part F) | If the GAP Peripheral or Central role is supported, all manda- tory features |
| GATT ([Vol 3] Part G) | GATT is mandatory when ATT is supported. When supported, all mandatory features |
| SM ([Vol 3] Part H) | If the GAP Peripheral or Central role is supported, all manda- tory features |

Table 4.6:  LE Core Configuration Host requirements
Controller Part:

| Layer | Required Features |
| --- | --- |
| PHY ([Vol 6] Part A) | All mandatory features |
| LL ([Vol 6] Part B) | All mandatory features |

Table 4.7:  LE Core Configuration Controller requirements

### 4.5   BASIC RATE AND LOW ENERGY COMBINED CORE CONFIGURATION

This section specifies compliance requirements for the “Basic Rate and Low Energy Combined” Core Configuration.
To claim support for the “Basic Rate and Low Energy” Core Configuration, an implementation must support a set of Required Features, according to the details inTable 4.8 and Table 4.9.
Host Part:

| Layer | Required Features |
| --- | --- |
| L2CAP ([Vol 3] Part A) | All L2CAP requirements in the BR CC and LE CC |
| SDP ([Vol 3] Part B) | All mandatory features |
| GAP ([Vol 3] Part C) | All GAP requirements in the BR CC and LE CC AND All requirements in sections 13, 14 and 15 |
| ATT ([Vol 3] Part F) | All ATT requirements in the LE CC. If ATT is supported on BR, all ATT requirements in the BR CC. |
| GATT ([Vol 3] Part G) | All GATT requirements in the LE CC. If GATT is supported on BR, all GATT requirements in the BR CC. |
| SM ([Vol 3] Part H) | All SM requirements in the LE CC |

Table 4.8:  BR and LE Combined Core Configuration Host requirements
Controller Part:

| Layer | Required Features |
| --- | --- |
| RF ([Vol 2] Part A) | All RF requirements in the BR CC |
| BB ([Vol 2] Part B) | All BB requirements in the BR CC |
| LMP ([Vol 2] Part C) | All LMP requirements in the BR CC AND LMP feature bits 38 and 65 shall be set |
| PHY ([Vol 6] Part A) | All mandatory features in the LE CC |
| LL ([Vol 6] Part B) | All mandatory features in the LE CC |

Table 4.9:  BR and LE Combined Core Configuration Controller requirements

### 4.6   HOST CONTROLLER INTERFACE CORE CONFIGURATION

This section specifies compliance requirements for the “Host Controller Interface” Core Configuration.
To claim support for the “Host Controller Interface” Core Configuration, an implementation must support a set of Required Features, according to the details in Table 4.10.

| Layer | Required Features |
| --- | --- |
| HCI ([Vol 2] Part E) | All the supported features in the implementation shall be compliant to the Host Controller Interface. |

Table 4.10:  HCI Core Configuration requirements
Architecture & Terminology Overview Part A
PART C: ARCHITECTURE
CONTENTS

## 6  BLUETOOTH APPLICATION ARCHITECTURE [Updated]


### 6.6   MESH-BASED MODEL HIERARCHY [New Section]

The Mesh Profile1 specifies the structure within which data is exchanged by devices in a mesh network. This structure defines basic building blocks such as models and properties.
The top level of the hierarchy is a model, which is either a client model or a server model. A client model can send messages to a server model and the server model can use other messages to respond to the client model. Models enable devices to send standardized messages, using standardized data formats, to other devices that they have had no previous relationship with.

#### 6.6.1  Model

A model is a collection of properties, states, messages, and associated behaviors that accomplishes a particular device function. A model defines and exposes states along with any associated behavior. It also defines the messages that are used to communicate between models within devices in a mesh network. Messages are defined globally and are not model-specific. Models are immutable meaning that features cannot be added to or removed from a model definition. Therefore, the only way to add features to a model is by defining a new model that extends an existing model by defining new states, messages, and behaviors. These new states and behaviors are linked to the existing model using state binding. This ensures backwards and forwards compatibility by allowing newer devices to access the newer features of the extended model, and older devices to access the base features of an existing model.

#### 6.6.2  Properties

A property adds context to a defined characteristic. When sending data into a mesh network, it is very useful to label data with the meaning, or context, of that data. This allows a device that receives a property to interpret that data without having to negotiate the context beforehand. For example, a temperature characteristic can be given a context about how or when that temperature was measured such as “outside temperature”, “indoor temperature”, or “oil temperature”.
Properties are defined globally and are not model-specific.
1. The Mesh Profile specification is available at https://www.bluetooth.com/specifications/
adopted-specifications.
Architecture & Terminology Overview Part D
PART C: MIXING OF SPECIFICATION VERSIONS
CONTENTS

## 1  MIXING OF SPECIFICATION VERSIONS

This part describes how volumes, and parts within volumes, of different versions and Specification Addenda of the Core Specification may be mixed in Bluetooth implementations. The Core System consists of a BR/EDR Controller Package (see Volume 2), a Low Energy Controller Package (see Volume 6), a Host Package (see Volume 3) and AMP Protocol Adaptation Layers (see Volume 5).
• All parts within a Primary Controller implementation shall comply with the same version of Volume 2 and Volume 6.
• All parts within a Host implementation of Volume 3 shall comply with the same version.
• An AMP Controller implementation shall contain parts of Volume 2 and Volume 5 from the same version.
• The Primary Controller, AMP Controller, and Host may comply with different versions within a single implementation.
In order to describe how these volumes and parts within volumes can be mixed, one needs to distinguish between four categories of features specified in the different specification versions. The four categories are:

| Category | Description |
| --- | --- |
| Type 1 | Feature that exists below HCI and cannot be configured/enabled via HCI |
| Type 2 | Feature that exists below HCI and can be configured/enabled via HC |
| Type 3 | Feature that exists below and above HCI and requires HCI command events to function |
| Type 4 | Feature that exists only above HCI |

Table 1.1:  Feature type definitions
The outcome of mixing different Core System Packages are derived from the feature definitions in the table above:
• If an implementation contains features of type 1 or type 4, these features can function with any combination of Host Package and Controller Package or AMP Protocol Adaptation Layer (PAL) versions with applicable addenda.
• If an implementation contains features of type 2, these features can only be used under a default condition if a Host Package of an older version with applicable addenda is mixed with a Controller Package or AMP PAL of this version with applicable Core Specification Addenda (CSAs).
• In order to fully use the feature under all conditions, the Host Package, Controller Package, and AMP PAL must comply with the same or later version with applicable CSAs.
• If an implementation contains features of type 3, these features can only function if the Host Package supports this version or a later version with applicable CSAs and if the Controller Package complies with this version or a later version with applicable CSAs.
See the Bluetooth Brand Usage Guide for specification naming requirements.

### 1.1   FEATURES AND THEIR TYPES

The following table lists the features, their types, and the version or addendum where the feature was first introduced.

| Feature | Version | Type |
| --- | --- | --- |
| Basic AFH operation | 1.2 | 1 |
| Enhanced inquiry | 1.2 | 1 |
| Configuration of AFH (setting channels and enabling/dis- abling channel assessment) | 1.2 | 2 |
| Enhanced synchronization capability | 1.2 | 2 |
| Interlaced inquiry scan | 1.2 | 2 |
| Interlaced page scan | 1.2 | 2 |
| Broadcast encryption | 1.2 | 2 |
| Enhanced flow specification and flush time-out | 1.2 | 3 |
| Extended SCO links | 1.2 | 3 |
| Inquiry Result with RSSI | 1.2 | 3 |
| L2CAP flow and error control | 1.2 | 4 |
| 2 Mb/s EDR | 2.0 + EDR | 2 |
| 3 Mb/s EDR | 2.0 + EDR | 2 |
| 3 slot packets in EDR | 2.0 + EDR | 2 |
| 5 slot packets in EDR | 2.0 + EDR | 2 |
| 2 Mb/s eSCO | 2.0 + EDR | 2 |
| 3 Mb/s eSCO | 2.0 + EDR | 2 |
| 3 slot packets for EDR eSCO | 2.0 + EDR | 2 |
| Erroneous Data Reporting | 2.1 + EDR | 3 |
| Extended Inquiry Response | 2.1 + EDR | 3 |
| Encryption Pause and Resume | 2.1 + EDR | 1 |
| Link Supervision Timeout Changed Event | 2.1 + EDR | 3 |
| Non-Flushable Packet Boundary Flag | 2.1 + EDR | 3 |
| Sniff subrating | 2.1+ EDR | 3 |
| Secure Simple Pairing | 2.1.+ EDR | 3 |
| L2CAP Enhanced Retransmission Mode | Addendum 1/ 3.0 + HS | 4 |
| L2CAP Streaming Mode | Addendum 1/ 3.0 + HS | 4 |
| Enhanced Power Control | 3.0 + HS | 1 |

Table 1.2:  Features and their types

| Feature | Version | Type |
| --- | --- | --- |
| AMP Manager Protocol (A2MP) | 3.0 + HS | 4 |
| L2CAP Enhancements for AMP | 3.0 + HS | 4 |
| 802.11 PAL | 3.0 + HS | 3 |
| Generic Test Methodology | 3.0 + HS | 3 |
| Unicast Connectionless Data | 3.0 + HS | 4 |
| Low Energy Controller (PHY and LL) | 4.0 | 3 |
| Low Energy Host (L2CAP and Security Manager) | 4.0 | 4 |
| Attribute Protocol and Generic Attribute Profile | 4.0 | 4 |
| Appearance Data Type | Addendum 2 | 4 |
| 802.11n Enhancements to the 802.11 PAL | Addendum 2 | 3 |
| MWS Coexistence Signaling | Addendum 3 | 2 |
| Connectionless Slave Broadcast | Addendum 4 | 3 |
| Unencrypted UCD | Addendum 4 | 4 |
| BR/EDR Secure Connections | 4.1 | 3 |
| Train Nudging | 4.1 | 2 |
| Generalized Interlaced Scan | 4.1 | 2 |
| Piconet Clock Adjustment | 4.1 | 3 |
| Low Duty Cycle Directed Advertising | 4.1 | 2 |
| 32-bit UUID Support in LE | 4.1 | 4 |
| LE Dual Mode Topology | 4.1 | 4 |
| LE L2CAP Connection Oriented Channel Support | 4.1 | 4 |
| LE Privacy v1.1 | 4.1 | 4 |
| LE Link Layer Topology | 4.1 | 3 |
| LE Ping | 4.1 | 2 |
| LE Data Packet Length Extension | 4.2 | 2 |
| LE Secure Connections | 4.2 | 4 |
| Link Layer Privacy | 4.2 | 3 |
| Link Layer Extended Filter Policies | 4.2 | 3 |
| Slot Availability Mask | 5.0 | 2 |
| LE 2M PHY | 5.0 | 2 |
| LE Coded PHY | 5.0 | 3 |
| High Duty Cycle Non-Connectable Advertising | 5.0 | 2 |
| LE Advertising Extensions | 5.0 | 3 |

Table 1.2:  Features and their types

| Feature | Version | Type |
| --- | --- | --- |
| LE Channel Selection Algorithm #2 | 5.0 | 2 |
| LE Higher Output Power | Addendum 5 | 1 |

Table 1.2:  Features and their types

### 1.2   CORE SPECIFICATION ADDENDA

A Core Specification Addendum (CSA) contains one or more parts of a single volume, one or more parts in multiple volumes, changes on one or more parts, or a combination of parts and changes. Addenda are used to supersede a part in a volume or may be used to add a part to a volume according to the rules in Table 1.3.
Note: Each Change may contain changes and/or additions to one or more parts of the Core Specification.

| Addendum | Volume and Part or Change Name | Addition/ Changes/ Replacement | Allowed Versions & Addendum | Mandatory / Optional / Conditional | Type |
| --- | --- | --- | --- | --- | --- |
| 1 | Volume 3, Part A | Replacement | 2.0 + EDR, 2.1 + EDR | O | 4 |
| 2 | Audio Architec- ture HCI Changes | Change | 2.1 + EDR, 3.0 + HS, 4.0 | O | 2 |
|  | Audio Architec- ture USB Changes | Change | 2.1 + EDR, 3.0 + HS, 4.0 | O | 2 |
|  | LE Limited Discov- ery Time Changes | Change | 4.0 | C.1 | 4 |
|  | EIR and AD Data Types in GAP Changes | Change | 4.0 | C.1 | 4 |
|  | EIR and AD Data Types Specification | Addition | 4.0 | C.1 | 4 |
|  | Volume 5, Part A | Replacement | 3.0 + HS, 4.0 | O | 3 |

Table 1.3:  Adopted core specification versions to use with addenda.

| Addendum | Volume and Part or Change Name | Addition/ Changes/ Replacement | Allowed Versions & Addendum | Mandatory / Optional / Conditional | Type |
| --- | --- | --- | --- | --- | --- |
| 3 | LE Errata | Change | 4.0 with CSA2 | C.2 | Multip |
|  | GAP Connection Parameters Changes | Change | 4.0 with CSA2 | C.1 | 4 |
|  | GAP Authentica- tion and Lost Bond Changes | Change | 4.0 with CSA2 | C.1 | 4 |
|  | Common Profile and Services Error Code Range Changes | Change | 4.0 with CSA2 | C.1 | 4 |
|  | Private Addressing Changes | Change | 4.0 with CSA2 | C.1 | 4 |
|  | Dual Mode Addressing Changes | Change | 4.0 with CSA2 | C.3 | 4 |
|  | MWS Coexistence Logical Signaling Specification | Addition | 2.1 + EDR, 3.0 + HS, 4.0 with CSA2 | O | 2 |
|  | MWS Coexistence HCI | Addition | 2.1 + EDR, 3.0 + HS, 4.0 with CSA2 | C.4 | 2 |
|  | Wireless Coexis- tence Interface 1 (WCI-1) Transport Layer Specifica- tion | Addition | 2.1 + EDR, 3.0 + HS, 4.0 with CSA2 | C.4 | 2 |
|  | Wireless Coexis- tence Interface 2 (WCI-2) Transport Layer Specifica- tion | Addition | 2.1 + EDR, 3.0 + HS, 4.0 with CSA2 | C.4 | 2 |

Table 1.3:  Adopted core specification versions to use with addenda.

| Addendum | Volume and Part or Change Name | Addition/ Changes/ Replacement | Allowed Versions & Addendum | Mandatory / Optional / Conditional | Type |
| --- | --- | --- | --- | --- | --- |
| 4 | Connectionless Slave Broadcast | Change | 3.0 + HS, 4.0 with CSA3 | O | 3 |
|  | Unencrypted UCD | Change | 3.0 + HS, 4.0 with CSA3 | O | 4 |
|  | Fast Advertising Interval | Change | 4.0 with CSA3 | C.1 | 4 |
|  | eSCO Reserved Slot Clarification | Change | 2.1 + EDR, 3.0 + HS, 4.0 with CSA3 | O | 1 |
| 5 | Higher Output Power | Change | 4.0 with CSA3, 4.0 with CSA4, 4.1, 4.2 | O | 1 |
| 6 | Volume 0, Part B | Replacement | 4.0 with CSA3, 4.0 with CSA4, 4.0 with CSA5, 4.1, 4.1 with CSA5, 4.2, 4.2 with CSA5, 5.0 | M | N/A |
|  | Volume 1, Part A | Change | 4.0 with CSA3, 4.0 with CSA4, 4.0 with CSA5, 4.1, 4.1 with CSA5, 4.2, 4.2 with CSA5, 5.0 | M | N/A |

Table 1.3:  Adopted core specification versions to use with addenda.
C.1: Mandatory if either the Host Part of the Low Energy Core Configuration or the Host Part of the Basic Rate and Low Energy Combined Core Configuration is supported, otherwise Excluded.
C.2: Mandatory if either the Host Part of the Low Energy Core Configuration, Controller Part of the Low Energy Core Configuration, Host Part of the Basic Rate and Low Energy Combined Core Configuration, or Controller Part of the Basic Rate and Low Energy Combined Core Configuration is supported, otherwise Excluded.
C.3: Mandatory if the Host Part of the Basic Rate and Low Energy Combined Core Con- figuration is supported, otherwise Excluded.
C.4: Optional if MWS Coexistence Logical Signaling is supported, otherwise Excluded.
2872
unthinkably connected