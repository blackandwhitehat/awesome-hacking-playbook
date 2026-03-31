# Tools

## Hardware

| Tool | Type | Price | Notes |
|------|------|-------|-------|
| [M5Stack Atomic CAN](https://m5stack.com) | ESP32 CAN Interface | ~$15 | **Recommended.** WiFi, web UI, open-source firmware. |
| [Comma AI Panda](https://comma.ai) | Automotive CAN Interface | ~$100 | Good if you already have one. Needs OBD-II mod. |
| [CANable Pro](https://canable.io) | USB CAN Interface | ~$40 | Open-source, SocketCAN compatible. |
| [Peak PCAN-USB](https://www.peak-system.com) | USB CAN Interface | ~$250 | Industry standard, great driver support. |
| [Actisense NGT-1](https://actisense.com) | Commercial NMEA Gateway | ~$200-600 | Overkill for hacking, but rock solid. |
| NMEA 2000 Backbone Kit | Bus Hardware | ~$50-100 | T-connectors, terminators, drop cables. |
| Garmin Chart Plotter (used) | Feedback Device | ~$50-200 | Physical feedback for spoofed data. |

## Software

| Tool | Platform | License | Purpose |
|------|----------|---------|---------|
| [NMEA 2000 Simulator (kave.fi)](https://www.kave.fi/Apps) | Windows | Free (limited) | Simulate NMEA 0183/2000 traffic |
| [NMEASimulator](https://github.com/panaaj/nmeasimulator) | Cross-platform | Open source | NMEA 0183 / Signal K simulation |
| [OpenCPN](https://opencpn.org) | Cross-platform | GPLv2 | Open-source chart plotter (target) |
| [Coastal Explorer](https://www.rosepoint.com/coastal-explorer) | Windows | $399 | Commercial chart plotter |
| [com0com](https://sourceforge.net/projects/com0com/) | Windows | Open source | Virtual serial port pairs |
| [socat](http://www.dest-unreach.org/socat/) | Linux/macOS | GPLv2 | Virtual serial pairs and more |
| [canboat](https://github.com/canboat/canboat) | Cross-platform | Open source | NMEA 2000 PGN decoder/analyzer |
| [python-can](https://python-can.readthedocs.io) | Cross-platform | LGPL | Python CAN bus library |
| [ESP32 NMEA2000](https://github.com/AK-Homberger/NMEA2000-AIS-Gateway) | ESP32 | Open source | Open-source NMEA 2000 gateway firmware |

## Python Libraries

| Library | Purpose |
|---------|---------|
| `python-can` | CAN bus communication |
| `cantools` | DBC file parsing and encoding |
| `panda` (comma.ai) | Comma Panda interface |
| `pyserial` | Serial port communication (NMEA 0183) |

## Reference Resources

| Resource | URL | Description |
|----------|-----|-------------|
| Canboat PGN Database | [github.com/canboat/canboat](https://github.com/canboat/canboat) | Reverse-engineered NMEA 2000 PGN definitions |
| NMEA 2000 Wikipedia | [en.wikipedia.org/wiki/NMEA_2000](https://en.wikipedia.org/wiki/NMEA_2000) | Protocol overview |
| CAN Bus Wikipedia | [en.wikipedia.org/wiki/CAN_bus](https://en.wikipedia.org/wiki/CAN_bus) | Underlying protocol |
