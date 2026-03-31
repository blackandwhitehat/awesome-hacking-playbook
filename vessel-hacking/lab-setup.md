# Lab Setup

## Overview

You don't need a boat to learn vessel hacking. A complete lab can be built with zero hardware (software-only) or with a minimal hardware investment (~$30-50).

## Option 1: Software-Only Lab (Free)

Everything runs on your computer. No hardware required.

### What You Need
- Windows, Mac, or Linux machine
- [OpenCPN](https://opencpn.org) (chart plotter)
- [NMEA Simulator](https://www.kave.fi/Apps) or [NMEASimulator](https://github.com/panaaj/nmeasimulator)
- [com0com](https://sourceforge.net/projects/com0com/) (Windows) or [socat](http://www.dest-unreach.org/socat/) (Linux/macOS)

### Setup Steps

1. **Install virtual serial ports**
   ```bash
   # Linux/macOS
   socat PTY,link=/dev/ttyS98 PTY,link=/dev/ttyS99
   
   # Windows: install com0com, create COM5 <-> COM6 pair
   ```

2. **Configure simulator** to output on one end of the virtual pair (e.g., COM5 / /dev/ttyS98)

3. **Configure OpenCPN** to read from the other end (e.g., COM6 / /dev/ttyS99)

4. **Start simulating**  -  you should see vessel position, heading, speed in OpenCPN

5. **Start hacking**  -  write Python scripts to inject modified data into the virtual serial pair

### MITM Setup

```
Simulator → COM5 ←→ COM6 → Python MITM → COM7 ←→ COM8 → OpenCPN
```

Your Python script reads from COM6, modifies the data, and writes to COM7. OpenCPN reads from COM8 and displays the modified data.

## Option 2: Hardware Lab (~$30-50)

Adds a real CAN bus to the mix.

### What You Need
- [M5Stack Atomic CAN](https://m5stack.com) (~$15)
- NMEA 2000 backbone kit or jumper wires ($10-20)
- A chart plotter (OpenCPN on a second machine, or a used Garmin ~$50+)

### Setup Steps

1. **Flash the M5Stack** with open-source NMEA 2000 firmware
2. **Connect to the backbone** (CAN High + CAN Low)
3. **Connect your laptop** to the M5Stack's WiFi hotspot
4. **Open the web UI**  -  you can now see and inject CAN messages
5. **Connect a chart plotter** to the other end of the backbone

### Wiring

For a minimal setup with jumper wires:
```
M5Stack CAN H ──── CAN H ──── Chart Plotter CAN H
M5Stack CAN L ──── CAN L ──── Chart Plotter CAN L
M5Stack GND   ──── GND   ──── Chart Plotter GND
```

Add 120Ω termination resistors at each end of the bus if using long cable runs.

## Option 3: Full Lab (~$200+)

For serious research.

### Additional Hardware
- Multiple CAN interfaces (attack from multiple nodes)
- Physical chart plotter (Garmin, Raymarine)
- NMEA 2000 backbone with proper connectors
- Inline CAN tap for passive monitoring
- Logic analyzer or oscilloscope for physical layer analysis

## First Exercises

Once your lab is running:

1. **Observe normal traffic**  -  what PGNs do you see? At what rate?
2. **Decode PGNs**  -  use canboat to parse raw CAN frames into readable data
3. **Inject a single PGN**  -  send a fake GPS position, see it on the chart plotter
4. **DoS test**  -  flood the bus, observe what happens to the display
5. **Address claim**  -  send an ISO Address Claim with a low NAME value, watch the real device get bumped
6. **GPS spoof**  -  gradually drift the displayed position
7. **MITM**  -  intercept and modify a specific PGN while passing others through

## Safety Notes

- Never test on a vessel that's underway
- Never transmit GPS spoofing signals over RF (illegal)
- On-bus attacks in a lab are fine
- If testing on a real vessel, do it at dock with explicit authorization
- Keep your lab isolated from any real navigation systems
