# Building Your Hardware Hacking Lab

A good lab is organized, safe, and equipped for the work you do. It doesn't need to be fancy or expensive. It needs to support focused, methodical hardware hacking.

## Space and Layout

### Workbench Area

Dedicate a physical workspace. This is where you:
- Disassemble devices
- Solder and desolder
- Use microscopes and magnification
- Connect logic analyzers and USB adapters

**What you need:**
- A sturdy table (desk is fine)
- Good lighting (overhead light + adjustable desk lamp)
- ESD mat (1-2 feet square minimum)
- Comfortable chair
- Storage for small parts (drawers, bins)

**Optional but nice:**
- Adjustable workbench light with magnifier attached
- Flexible arm for holding the microscope or camera
- Anti-fatigue mat (if standing)

### Computing Area

Separate from your workbench (physically or just conceptually):
- Main computer (Linux is recommended, but Windows or Mac work)
- Monitor (or monitor + laptop screen)
- Keyboard, mouse, headphones

From here, you:
- SSH into your Raspberry Pi
- Run Ghidra for firmware analysis
- Edit config files
- Write scripts

**Recommendation:** If possible, put the computing area away from your workbench. This separates "thinking" space from "doing" space.

### Raspberry Pi Setup

The Raspberry Pi can be:
- At your workbench (to control devices directly)
- At your desk (to analyze data from devices remotely)
- Somewhere else entirely (connected over SSH or USB)

I recommend a separate location from the workbench. It's quiet, connected to the network, and you can access it from your main computer via SSH.

**Setup:**
- Plug Pi into power
- Plug into Ethernet (or WiFi, if needed)
- SSH in: `ssh pi@<IP_ADDRESS>`
- All interactions are remote

This way, you can hack at your workbench while controlling everything from your desk. The Pi sits in the corner, unattended.

## Equipment Organization

### Tool Storage

Keep your hardware hacking tools where you can find them:

**Essential tools (always on the workbench or desk):**
- Multimeter
- Tweezers
- Small screwdriver set
- Jumper wire assortment
- Soldering iron + solder (when in use)
- USB-to-serial adapters

**Consumables (in drawers):**
- Solder (multiple types)
- Thermal paste
- Flux
- Desoldering braid
- Isopropyl alcohol (for cleaning)
- Small storage containers for screws and parts

**Specialty tools (stored, pulled out as needed):**
- Logic analyzer
- USB microscope
- PiFex (if you have one)
- ST-Link or other adapters
- Oscilloscope (if you own one)

### Cable Management

Organize your cables:
- Label them (or use color-coded labels)
- Use cable organizers or clips to keep them tidy
- Keep cables coiled to avoid kinks
- Know what each cable is (USB-A to Micro, USB-C, serial, etc)

At the end of a session, coil cables and store them. This saves time next session and prevents damage.

### Firmware and Data Storage

Create a directory structure on your main computer and Pi:

```
~/hacking/
├── devices/
│   ├── device-1/
│   │   ├── firmware_original.bin
│   │   ├── firmware_modified.bin
│   │   ├── notes.md
│   │   ├── uart_output.txt
│   │   ├── ghidra_project/
│   │   └── photos/
│   └── device-2/
│       └── ...
├── tools/
│   ├── ghidra/
│   ├── openocd_configs/
│   └── scripts/
└── reference/
    ├── datasheets/
    ├── schematics/
    └── teardowns/
```

**Why organize:**
- You'll revisit old projects
- You need to find configurations for your tools
- You want to learn from past mistakes
- Others might want to learn from your work

## Computer Setup

### Linux Recommendations

Ubuntu or Debian is standard. Install required packages:

```bash
sudo apt update
sudo apt install -y \
  flashrom openocd screen minicom \
  pulseview sigrok \
  git vim python3 python3-pip \
  binutils-arm-none-eabi \
  gcc-arm-none-eabi

# Optional tools
sudo apt install -y gdb-multiarch hexdump
```

### Python Tools

Create a Python environment for hardware hacking scripts:

```bash
mkdir ~/hacking/scripts
cd ~/hacking/scripts
python3 -m venv venv
source venv/bin/activate

# Install useful packages
pip install pwntools  # For binary manipulation
pip install pycryptodome  # For crypto analysis
pip install requests  # For API interactions
pip install scapy  # For network analysis
```

### Ghidra Installation

Download from https://ghidra-sre.org/

```bash
mkdir ~/tools
unzip ghidra_*.zip -d ~/tools/
cd ~/tools/ghidra_*/
./ghidraRun
```

Create a desktop shortcut or alias:
```bash
alias ghidra='~/tools/ghidra_*/ghidraRun'
```

### Text Editor or IDE

Use whatever you're comfortable with:
- Vim / Neovim (terminal-based, powerful)
- VS Code (GUI, lots of extensions)
- Emacs (advanced, steep learning curve)
- Sublime Text (lightweight, paid)

For firmware analysis, VS Code with a hex editor extension is nice.

## Raspberry Pi Setup

### Initial Configuration

```bash
# Download Pi OS from raspberrypi.com
# Flash with Balena Etcher or dd

# Boot the Pi, connect via SSH
ssh pi@192.168.1.xxx

# Expand filesystem
sudo raspi-config  # Advanced > Expand Filesystem

# Update packages
sudo apt update
sudo apt upgrade -y

# Install tools
sudo apt install -y flashrom openocd screen minicom
sudo apt install -y python3-pip git

# Enable interfaces
sudo raspi-config
# Interfacing > SSH: Enable
# Interfacing > Serial: Enable
# Interfacing > SPI: Enable
# Interfacing > I2C: Enable

# Reboot
sudo reboot
```

### SSH Key Authentication

On your main computer:
```bash
ssh-keygen -t ed25519 -f ~/.ssh/pi_rsa
ssh-copy-id -i ~/.ssh/pi_rsa.pub pi@192.168.1.xxx
```

Now you can SSH without a password:
```bash
ssh -i ~/.ssh/pi_rsa pi@192.168.1.xxx
```

### Network Discovery

If you don't know the Pi's IP:

```bash
# Scan the network
nmap -sn 192.168.1.0/24 | grep -i raspberry

# Or check your router's DHCP client list
```

### Static IP (Optional)

Edit `/etc/dhcpcd.conf` on the Pi:

```
interface eth0
static ip_address=192.168.1.50/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8
```

Reboot to apply.

## Safety and Protection

### ESD Protection

Electrostatic discharge kills chips:
- Wear a wrist strap connected to the ESD mat
- The ESD mat connects to ground
- Work on the mat when handling bare PCBs
- Some people prefer ESD shoes or clothing

In high-humidity areas (like Florida), ESD is less critical. In dry areas (winter, high altitude), it's essential.

### Soldering Safety

- Soldering irons get extremely hot (350+ Celsius)
- Keep water nearby in case of burns
- Use a soldering stand; never put the iron down on the desk
- Ventilate the area (solder fumes contain lead, flux contains rosin)
- Wash hands after soldering

### Component Protection

- Don't leave devices powered on unattended (fire hazard)
- Check polarity before powering (reversed polarity destroys chips)
- Use current-limiting power supplies when testing unknown devices
- Keep flammable materials away from your workbench

## Project Workflow

Every project follows a similar workflow:

### Phase 1: Preparation (30 min - 2 hours)

1. Gather information about the device
2. Search FCC database, datasheets, GitHub
3. Plan your approach (which interfaces to try, what you're looking for)
4. Set up your tools and workspace

### Phase 2: Physical Access (30 min - 2 hours)

1. Safely disassemble the device
2. Take photos and notes
3. Identify chips and connectors
4. Document the PCB layout

### Phase 3: Interface Discovery (1-2 hours)

1. Search for UART, SPI, JTAG, SWD
2. Probe test points with multimeter or logic analyzer
3. Try to connect and verify communication

### Phase 4: Data Extraction (1-4 hours)

1. Dump firmware via SPI, SWD, or bootloader
2. Verify dumps are consistent (compare two reads)
3. Analyze strings, structure, and content
4. Archive the firmware

### Phase 5: Analysis (2-8 hours)

1. Load firmware in Ghidra
2. Identify important functions
3. Look for security checks, credentials, or vulnerabilities
4. Document findings

### Phase 6: Modification (2-6 hours, optional)

1. Plan your modification
2. Edit the binary or reassemble code
3. Re-flash to device
4. Test on real hardware
5. Document results

### Phase 7: Documentation and Cleanup (1-2 hours)

1. Write a detailed report
2. Save all files (firmware, analysis, photos)
3. Clean up your workspace
4. Archive the project

**Total time per device: 1-3 days**, depending on complexity.

## Keeping a Lab Notebook

Document everything:

```
Device: Acme WiFi Switch (Model XYZ-123)
Date: 2025-03-31
Goal: Dump firmware and look for hardcoded credentials

## Disassembly
- 4 screws under stickers
- Main PCB with ESP32-S3
- Secondary module for relay control
- See photos/

## Interfaces Found
- UART: Header pads TP1-TP4 (VCC, GND, TX, RX)
- SPI: W25Q32 flash chip, pins not directly accessible
- SWD: Not found

## UART Connection
- Adapter: FTDI FT232RL
- Baud rate: 115200
- Boot output: Shows loading from 0x1000 in flash
- Debug messages mention /etc/config.json

## Firmware Dump
- Method: SPI via flashrom with chip clip
- Size: 4MB (W25Q32)
- Dump time: 3 minutes
- Verified: 2 reads match exactly

## Key Findings
- Hardcoded WiFi SSID: "setup_AP"
- Credentials in /etc/config.json (found via strings)
- No encryption on SPI bus
- Debug shell accessible via UART (no password)

## Modifications
- Changed timeout value from 600 to 3600 seconds
- Re-flashed successfully
- Tested: Feature works as intended

## Files Saved
- firmware_original.bin
- firmware_modified.bin
- uart_boot_output.txt
- ghidra_analysis/
- photos/

## Time Invested
- Prep: 45 min
- Disassembly + photos: 30 min
- Interface discovery: 45 min
- Firmware dump: 15 min
- Analysis: 2 hours
- Modification: 1 hour
- Total: ~5 hours
```

This notebook helps you remember what you did, why you did it, and what you learned.

## Scaling Up

As you do more projects:

1. **Build your tool collection** - Each project teaches you what's missing
2. **Create config templates** - Save OpenOCD configs, flashrom recipes
3. **Develop scripts** - Automate common tasks (parsing dumps, finding patterns)
4. **Share and learn** - Post findings on GitHub, help others, learn from community

## Recommended Reading

- **Hands-On Reverse Engineering Workbook** - Jon Erickson
- **The Hardware Hacking Handbook** - Colin O'Flynn
- **Firmware Security Assessment** - Glenn S. Wilkinson
- Papers and talks at DefCon, Black Hat, Chaos Computer Club

## Community Resources

- **r/hardwarehacking** - Reddit community
- **Matt Brown's Discord** - Active hardware hacking community
- **GitHub Topics** - Search "#hardware-hacking" or "[device] reverse engineering"
- **IDA Pro forums** - Useful for advanced reverse engineering

## Conclusion

A good lab is:
- **Organized** - You know where everything is
- **Safe** - Proper ESD, soldering safety, component protection
- **Documented** - You remember what you did and why
- **Flexible** - You can adapt to different device types
- **Scalable** - It grows with your skills

Start simple. Add tools as you need them. Over time, you'll have a professional-grade hardware hacking capability.

The best investment is patience and curiosity. Tools are secondary.
