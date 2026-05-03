# Bluetooth Assigned Numbers

**Last updated**: 2026-05-04
**Covers**: Core Spec 4.0 – 6.2

> Quick-reference for the most commonly used 16-bit UUIDs and Company Identifiers.
> Complete list: [bluetooth.com/specifications/assigned-numbers](https://www.bluetooth.com/specifications/assigned-numbers)

---

## 16-bit GATT Service UUIDs

Used in Primary/Secondary Service declarations and AD type `0x02`/`0x03` (Incomplete/Complete List of 16-bit Service UUIDs).

### Core Services

| UUID | Service Name | Key Characteristics |
|------|-------------|-------------------|
| 0x1800 | Generic Access Profile (GAP) | Device Name, Appearance, PPCP |
| 0x1801 | Generic Attribute Profile (GATT) | Service Changed, CSF, SSF, Database Hash |

### Standard Services

| UUID | Service Name | Common Profile |
|------|-------------|---------------|
| 0x1802 | Immediate Alert | Proximity Profile |
| 0x1803 | Link Loss | Proximity Profile |
| 0x1804 | Tx Power | Proximity Profile |
| 0x1805 | Current Time Service | — |
| 0x1808 | Glucose | Glucose Profile |
| 0x1809 | Health Thermometer | Health Thermometer Profile |
| 0x180A | Device Information Service (DIS) | All profiles (firmware/hardware revision) |
| 0x180D | Heart Rate | Heart Rate Profile |
| 0x180E | Phone Alert Status Service | — |
| 0x180F | Battery Service | Most battery-powered devices |
| 0x1810 | Blood Pressure | Blood Pressure Profile |
| 0x1811 | Alert Notification Service | — |
| 0x1812 | Human Interface Device (HID) | HID over GATT (HOG) |
| 0x1813 | Scan Parameters | — |
| 0x1814 | Running Speed and Cadence | — |
| 0x1815 | Automation IO | — |
| 0x1816 | Cycling Speed and Cadence | — |
| 0x1818 | Cycling Power | — |
| 0x1819 | Location and Navigation | — |
| 0x181A | Environmental Sensing | Temperature/Humidity sensors |
| 0x181B | Body Composition | — |
| 0x181C | User Data | — |
| 0x181D | Weight Scale | — |
| 0x181F | Continuous Glucose Monitoring | — |
| 0x1820 | Internet Protocol Support Service | — |
| 0x1821 | Indoor Positioning | — |
| 0x1826 | Fitness Machine Service | — |
| 0x1829 | Reconnection Configuration | — |

### LE Audio Services (5.2+)

| UUID | Service Name | Profile |
|------|-------------|---------|
| 0x1843 | Audio Stream Control Service (ASCS) | BAP |
| 0x184E | Broadcast Audio Scan Service (BASS) | BAP |
| 0x184F | Published Audio Capabilities Service (PACS) | BAP |
| 0x1850 | Basic Audio Announcement Service | BAP |
| 0x1851 | Broadcast Audio Announcement Service | BAP |
| 0x1843 | Audio Input Control Service (AICS) | VCP |
| 0x1844 | Volume Control Service (VCS) | VCP |
| 0x1853 | Common Audio Service (CAS) | CAP |
| 0x1854 | Hearing Access Service (HAS) | HAP |
| 0x1855 | Telephony and Media Audio Service (TMAS) | TMAP |
| 0x1856 | Public Broadcast Announcement Service | PBP |
| 0x1848 | Media Control Service (MCS) | MCP |
| 0x184B | Generic Media Control Service (GMCS) | MCP |
| 0x184C | Telephone Bearer Service (TBS) | CCP |
| 0x184D | Generic Telephone Bearer Service (GTBS) | CCP |

---

## 16-bit GATT Characteristic UUIDs

### GAP Characteristics (Service 0x1800)

| UUID | Characteristic | Size | Notes |
|------|---------------|------|-------|
| 0x2A00 | Device Name | Variable (≤248 B) | UTF-8 string |
| 0x2A01 | Appearance | 2 bytes | Category + subcategory |
| 0x2A02 | Peripheral Privacy Flag | 1 byte | 0=public, 1=private |
| 0x2A04 | Peripheral Preferred Connection Parameters | 8 bytes | Interval, latency, timeout |
| 0x2AA6 | Central Address Resolution | 1 byte | 0=not supported, 1=supported |
| 0x2AC9 | Resolvable Private Address Only | 1 byte | 5.0+ |
| 0x2B88 | Encrypted Data Key Material | 17 bytes | 5.4+ (EAD) |
| 0x2BF5 | LE GATT Security Levels | 4 bytes | GSLS (6.0+) |

### GATT Characteristics (Service 0x1801)

| UUID | Characteristic | Notes |
|------|---------------|-------|
| 0x2A05 | Service Changed | Indicate-only; notifies clients of GATT db change |
| 0x2B29 | Client Supported Features (CSF) | EATT support, robust caching, etc. (5.1+) |
| 0x2B2A | Database Hash | 128-bit AES-CMAC hash of GATT db (5.1+) |
| 0x2B3A | Server Supported Features (SSF) | EATT support flag (5.2+) |

### Device Information Service (DIS, 0x180A)

| UUID | Characteristic | Notes |
|------|---------------|-------|
| 0x2A29 | Manufacturer Name String | e.g., "Apple Inc." |
| 0x2A24 | Model Number String | e.g., "iPhone15,2" |
| 0x2A25 | Serial Number String | — |
| 0x2A27 | Hardware Revision String | PCB revision |
| 0x2A26 | Firmware Revision String | Firmware version |
| 0x2A28 | Software Revision String | Software version |
| 0x2A50 | PnP ID | Vendor ID Source + Vendor ID + Product ID + Version |

### Battery Service (0x180F)

| UUID | Characteristic | Notes |
|------|---------------|-------|
| 0x2A19 | Battery Level | 0–100% |

### Heart Rate Service (0x180D)

| UUID | Characteristic | Notes |
|------|---------------|-------|
| 0x2A37 | Heart Rate Measurement | Flags + value (1 or 2 bytes) |
| 0x2A38 | Body Sensor Location | Chest/Wrist/Finger/Hand/Ear/Foot |
| 0x2A39 | Heart Rate Control Point | Write 0x01 to reset energy expended |

### Human Interface Device (HID, 0x1812)

| UUID | Characteristic | Notes |
|------|---------------|-------|
| 0x2A4A | HID Information | bcdHID, bCountryCode, flags |
| 0x2A4B | Report Map | HID descriptor blob |
| 0x2A4C | HID Control Point | Write 0x00=suspend, 0x01=exit suspend |
| 0x2A4D | Report | Input/Output/Feature reports; handle in CCCD |
| 0x2A4E | Protocol Mode | 0x00=Boot, 0x01=Report |

### Environmental Sensing (0x181A)

| UUID | Characteristic | Notes |
|------|---------------|-------|
| 0x2A6D | Pressure | Pascal × 10 |
| 0x2A6E | Temperature | Celsius × 100 (sint16) |
| 0x2A6F | Humidity | Percent × 100 (uint16) |

### LE Audio Characteristics (5.2+)

| UUID | Characteristic | Service |
|------|---------------|---------|
| 0x2B77 | Sink ASE | ASCS |
| 0x2B78 | Source ASE | ASCS |
| 0x2B84 | ASE Control Point | ASCS |
| 0x2B79 | Sink PAC | PACS |
| 0x2B7A | Source PAC | PACS |
| 0x2B7B | Available Audio Contexts | PACS |
| 0x2B7C | Supported Audio Contexts | PACS |
| 0x2B7D | Audio Location | PACS |
| 0x2B7E | Volume Setting | VCS |
| 0x2B7F | Volume Control Point | VCS |
| 0x2B80 | Volume Flags | VCS |
| 0x2B81 | Volume Offset Control Point | VOCS |
| 0x2B82 | Audio Output Description | VOCS |
| 0x2BC0 | Audio Input State | AICS |
| 0x2BC4 | Audio Input Control Point | AICS |
| 0x2BB9 | Broadcast Audio Scan Control Point | BASS |
| 0x2BBA | Broadcast Receive State | BASS |
| 0x2B93 | Hearing Aid Features | HAS |
| 0x2B95 | Active Preset Index | HAS |

---

## 16-bit GATT Descriptor UUIDs

[Core 6.2, Vol 3, Part G, §3.3.3]

| UUID | Descriptor Name | Notes |
|------|----------------|-------|
| 0x2900 | Characteristic Extended Properties | Reliable Write / Writable Auxiliaries bits |
| 0x2901 | Characteristic User Description | Human-readable UTF-8 label |
| 0x2902 | Client Characteristic Configuration (CCCD) | Bit 0=Notify, Bit 1=Indicate; per-bond storage |
| 0x2903 | Server Characteristic Configuration (SCCD) | Bit 0=Broadcast; global (not per-bond) |
| 0x2904 | Characteristic Presentation Format | Format, exponent, unit, namespace, description |
| 0x2905 | Characteristic Aggregate Format | List of handles for multi-value aggregation |

**CCCD bit values**:

| Value | Meaning |
|-------|---------|
| 0x0000 | Notifications and indications disabled |
| 0x0001 | Notifications enabled |
| 0x0002 | Indications enabled |

---

## Appearance Values (UUID 0x2A01)

High byte = category, low byte = subcategory. Commonly used values:

| Value | Category / Subcategory |
|-------|----------------------|
| 0x0000 | Unknown |
| 0x0040 | Phone (generic) |
| 0x0041 | Phone (smartphone) |
| 0x0080 | Computer (generic) |
| 0x00C0 | Watch (generic) |
| 0x00C1 | Watch (sports) |
| 0x0180 | HID (generic) |
| 0x0181 | Keyboard |
| 0x0182 | Mouse |
| 0x0183 | Joystick |
| 0x0184 | Gamepad |
| 0x0185 | Digitizer tablet |
| 0x0186 | Card reader |
| 0x0187 | Digital pen |
| 0x0188 | Barcode scanner |
| 0x0240 | Glucose meter |
| 0x0340 | Cycling (generic) |
| 0x0341 | Cycling computer |
| 0x0342 | Speed sensor |
| 0x0343 | Cadence sensor |
| 0x0344 | Power sensor |
| 0x0345 | Speed and cadence sensor |
| 0x0540 | Pulse oximeter (generic) |
| 0x07C0 | Hearing aid (generic) |
| 0x0880 | Audio source (generic) |
| 0x0881 | Headset |
| 0x0882 | Hands-free unit |
| 0x0940 | Audio sink (generic) |
| 0x0941 | Headphones |
| 0x0942 | Speaker |

---

## Company Identifiers

Used in **AD type 0xFF (Manufacturer Specific Data)**: first 2 bytes are the Company ID (little-endian), followed by proprietary payload.

### Well-Known Companies

| ID | Company | Common Use in BLE |
|----|---------|------------------|
| 0x0002 | Intel Corporation | — |
| 0x0006 | Microsoft | Swift Pair (Windows 10+ pairing) |
| 0x000D | Texas Instruments Inc. | SimpleLink devices |
| 0x001D | Qualcomm Technologies International (QTIL) | — |
| 0x0046 | Tenovis | — |
| 0x004C | Apple, Inc. | iBeacon, AirDrop, AirPods, FindMy, Nearby |
| 0x0059 | Nordic Semiconductor ASA | Dev/test devices |
| 0x0075 | Samsung Electronics Co. Ltd. | Galaxy devices |
| 0x00D0 | Panasonic | — |
| 0x00E0 | Google | Nearby Share, Fast Pair (0x2CFE service UUID) |
| 0x0157 | Fitbit, Inc. | Fitbit wearables |
| 0x0171 | Amazon Fulfillment Service | Echo devices, Ring |
| 0x01D7 | Bose Corporation | Bose headphones |
| 0x038F | Meta Platforms, Inc. | Quest, Ray-Ban |

> Full list (3,000+ companies): [bluetooth.com/specifications/assigned-numbers](https://www.bluetooth.com/specifications/assigned-numbers) → Company Identifiers section.

### Apple Manufacturer Specific Data Types

Apple's 0x004C payload uses a sub-type byte:

| Sub-type | Name | Notes |
|----------|------|-------|
| 0x02 | iBeacon | UUID (16B) + Major (2B) + Minor (2B) + TX Power (1B) |
| 0x05 | AirDrop | — |
| 0x07 | AirPods | — |
| 0x10 | Nearby Action | Handoff, Universal Clipboard |
| 0x0F | Nearby Info | — |
| 0x12 | FindMy | — |

### Google Fast Pair

Google Fast Pair uses **Service UUID 0x2CFE** (16-bit) with a 3-byte model ID in the service data. Provider advertises:

```
AD type 0x16 (Service Data):
  UUID  0x2CFE       (2 bytes, little-endian)
  Model 0xXXXXXX     (3 bytes, big-endian)
```

---

## AD Type Quick Reference

Common values for the Length-Type-Value fields in advertising PDU payloads:

| AD Type | Name | Notes |
|---------|------|-------|
| 0x01 | Flags | Bit 0=LE Limited Discoverable, Bit 1=LE General Discoverable, Bit 2=BR/EDR Not Supported |
| 0x02 | Incomplete 16-bit Service UUIDs | — |
| 0x03 | Complete 16-bit Service UUIDs | — |
| 0x04 | Incomplete 32-bit Service UUIDs | — |
| 0x05 | Complete 32-bit Service UUIDs | — |
| 0x06 | Incomplete 128-bit Service UUIDs | — |
| 0x07 | Complete 128-bit Service UUIDs | — |
| 0x08 | Shortened Local Name | — |
| 0x09 | Complete Local Name | — |
| 0x0A | Tx Power Level | dBm (signed) |
| 0x0D | Class of Device | BR/EDR only |
| 0x0F | Simple Pairing Hash C-192 | BR/EDR OOB |
| 0x16 | Service Data — 16-bit UUID | 2-byte UUID + payload |
| 0x17 | Service Data — 32-bit UUID | 4-byte UUID + payload |
| 0x18 | Service Data — 128-bit UUID | 16-byte UUID + payload |
| 0x19 | Appearance | Same values as GATT 0x2A01 |
| 0x1A | Advertising Interval | — |
| 0x1F | List of 32-bit Service Solicitation UUIDs | — |
| 0x20 | Service Data — 32-bit UUID | — |
| 0x24 | URI | — |
| 0x25 | Indoor Positioning | — |
| 0x26 | Transport Discovery Data | — |
| 0x27 | LE Supported Features | — |
| 0x29 | Channel Map Update Indication | — |
| 0x2C | LE Supported Features | — |
| 0x2D | Channel Sounding (CS) Capabilities | 6.0+ |
| 0x31 | Encrypted Advertising Data (EAD) | 5.4+ |
| 0xFF | Manufacturer Specific Data | Company ID (2B LE) + payload |

---

## See Also

- [advertising.md](../concepts/advertising.md) — AD type framing, legacy vs. extended PDUs, PAwR
- [att-gatt.md](../concepts/att-gatt.md) — ATT/GATT protocol internals, MTU, CCCD, caching
- [profiles-and-services.md](../concepts/profiles-and-services.md) — profile-level usage of these UUIDs
- [ble-architecture.md](../concepts/ble-architecture.md) — where GATT fits in the BLE stack

---

*Source: [Core 6.2, Vol 3, Part G §3 (GATT Attributes)](../../sources/specs/6.2/Core_v6.2.md) · [BAP v1.0.2](../../sources/specs/profiles/BAP_v1.0.2.md) · [bluetooth.com/specifications/assigned-numbers](https://www.bluetooth.com/specifications/assigned-numbers)*
