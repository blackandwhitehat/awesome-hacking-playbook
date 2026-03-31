# 🚢 Vessel Hacking Playbook

A practical guide to maritime cybersecurity testing. Built from real-world vessel penetration testing experience and community contributions.

## Contributing

See the [main contribution guide](../README.md#-how-to-contribute). For vessel-specific content, we especially welcome:

- Real-world engagement writeups (anonymized)
- New tool discoveries or reviews
- Protocol analysis and PGN documentation
- Lab setup guides for different hardware
- Defensive recommendations and blue team perspectives


## Table of Contents

1. [Introduction](./01-introduction.md)  -  Why vessel hacking matters
2. [Vessel Network Overview](./02-vessel-networks.md)  -  Attack surface mapping
3. [NMEA 0183](./03-nmea-0183.md)  -  Legacy serial protocol
4. [NMEA 2000](./04-nmea-2000.md)  -  CAN bus-based instrument network
5. [NMEA 2000 vs Automotive CAN](./05-nmea-vs-automotive.md)  -  What car hackers already know
6. [Hardware Interfaces](./06-hardware.md)  -  Commercial, custom, and DIY approaches
7. [Software & Simulators](./07-software.md)  -  Simulators, targets, and virtual serial
8. [CAN Bus Vulnerabilities](./08-vulnerabilities.md)  -  DoS, spoofing, sniffing, MITM
9. [PGNs Deep Dive](./09-pgns.md)  -  Parameter Group Numbers reference
10. [Bus Priority & Address Claiming](./10-bus-priority.md)  -  How spoofing actually works
11. [Lab Setup](./lab-setup.md)  -  Build your own test environment
12. [Tools](./tools.md)  -  Hardware and software toolkit
13. [Resources](./resources.md)  -  Links, references, further reading

## Who This Is For

- Security researchers exploring maritime attack surfaces
- Penetration testers with vessel/maritime engagements
- Boat owners curious about their own systems
- Students learning CAN bus security concepts
- Anyone who thinks boats are cool and hackable

## Background

Maritime vessels run on decades-old protocols with zero authentication, no encryption, and full bus trust. If you can get on the NMEA 2000 bus, you can talk to anything connected to it: GPS, autopilot, rudder, engine, radar, sonar, AIS.

The same CAN bus vulnerabilities that car hackers have been exploiting for years apply directly to boats, just at 250 kbps instead of 500 kbps.

Autonomy is creeping into every hull, one system at a time. More systems = more attack surface.
