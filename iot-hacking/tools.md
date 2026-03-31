# Quick Reference: Hardware Hacking Tools

## Physical Tools

| Tool | Purpose | Cost | Priority |
|------|---------|------|----------|
| Soldering iron (Pinecil) | Solder/desolder connections | $30-50 | High |
| USB microscope | Read chip labels and trace routes | $30-100 | High |
| Multimeter (true RMS) | Test voltage, continuity, resistance | $20-50 | High |
| Logic analyzer | Capture and decode UART, SPI, I2C | $10-30 | Medium |
| Jumper wires | Connect components | $5-15 | High |
| USB-to-serial adapter | UART communication | $5-15 | High |
| ESD mat + wrist strap | Electrostatic discharge protection | $15-30 | Medium |
| PiFex HAT | SWD/JTAG on Raspberry Pi | $75 | High (if serious) |
| PCBite probes | Clip onto tiny pins without soldering | $50-100 | Low (optional) |
| Chip clip (SOIC) | Clip onto flash chips | $20-50 | Low (nice to have) |
| Bus Pirate 6 | Multi-protocol interface | $50-100 | Low (alternative to PiFex) |
| Oscilloscope | View analog signals | $300+ | Low (professional only) |

## Software Tools (All Linux)

### UART Communication
```bash
screen /dev/ttyUSB0 115200
minicom -D /dev/ttyUSB0 -b 115200
```

### SPI Flash Dumping
```bash
sudo flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=8000 -r firmware.bin
```

### JTAG/SWD Debugging
```bash
openocd -f config.cfg
telnet localhost 4444
```

### Binary Analysis
```bash
file firmware.bin
strings firmware.bin
xxd firmware.bin | head
```

### Firmware Disassembly
```bash
# Ghidra: https://ghidra-sre.org/
ghidraRun
```

### Hex Editing
```bash
# Built-in hex editor in many editors
vim -b firmware.bin  # Binary mode
# Or use a dedicated tool: bless, hexedit, wxhexeditor
```

### Logic Analyzer Software
```bash
sudo apt install pulseview sigrok
pulseview
```

## Raspberry Pi Specific

### Installation (Standard Pi OS)
```bash
sudo apt update
sudo apt install -y flashrom openocd screen minicom
sudo apt install -y pulseview sigrok git python3-pip
```

### Enable Interfaces
```bash
sudo raspi-config
# Enable SSH, Serial, SPI, I2C under Interfacing Options

# Or edit /boot/config.txt:
dtparam=spi=on
dtparam=i2c_arm=on
enable_uart=1
```

### Remote Access
```bash
# SSH from main computer
ssh pi@192.168.1.100

# SCP files
scp firmware.bin pi@192.168.1.100:/home/pi/

# SSH mount (SSHFS)
sshfs pi@192.168.1.100:/home/pi /mnt/pi
```

## Command Reference

### UART
```bash
# Monitor serial at 115200 baud
screen /dev/ttyUSB0 115200

# Exit screen: Ctrl-A K
# Detach screen: Ctrl-A D
# Reattach: screen -r
```

### SPI Flash
```bash
# Detect and list flash chip
sudo flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=8000 -L | grep "Found"

# Read entire flash
sudo flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=8000 -r firmware.bin

# Write modified firmware
sudo flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=8000 -w firmware_new.bin

# Verify read is correct
diff firmware.bin firmware_verify.bin
```

### Binary Analysis
```bash
# Show file type
file firmware.bin

# Extract strings
strings firmware.bin | grep "password"

# Hex dump first 100 lines
xxd firmware.bin | head -100

# Search for a specific pattern
xxd firmware.bin | grep "deadbeef"

# Extract all ASCII strings
strings firmware.bin > strings.txt
grep -i "config\|password\|api\|version" strings.txt
```

### GPIO Access (Python)
```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Pin 4 as input
GPIO.setup(4, GPIO.IN)
print(GPIO.input(4))  # Read pin

# Pin 17 as output
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
GPIO.output(17, GPIO.LOW)

GPIO.cleanup()
```

### OpenOCD Commands
```bash
# Start OpenOCD with your config
openocd -f config.cfg

# In telnet (telnet localhost 4444):
halt                          # Halt CPU
resume                        # Resume execution
dump_image firmware.bin 0x08000000 0x40000  # Dump memory
mww 0x20000000 0x12345678    # Write to memory
reg                           # Show all registers
reset                         # Reset the device
```

## Common Baud Rates

- 9600
- 19200
- 38400
- 57600
- 115200

Start with 115200, try others if garbage.

## SPI Flash Chip Identification

```bash
# Common manufacturers and part numbers:
W25Q32          # Winbond, 4MB
W25Q64          # Winbond, 8MB
MX25L6433F      # Macronix, 8MB
GD25Q32         # GigaDevice, 4MB
```

## ARM Cortex-M Variants

```
Cortex-M0       # Very basic, low power
Cortex-M3       # Common in STM32F1, NXP
Cortex-M4       # With FPU, STM32F4
Cortex-M7       # Fast, high-end
```

Set Ghidra language to match your target.

## Useful GitHub Repositories

```bash
# Ghidra reverse engineering framework
https://github.com/NationalSecurityAgency/ghidra

# SVD loader for Ghidra
https://github.com/leveldown-security/ghidra-svd

# ARM SVD files
https://github.com/ARM-Software/CMSIS-SVD

# Flashrom
https://github.com/flashrom/flashrom

# OpenOCD
https://github.com/openocd-org/openocd
```

## Websites

- [fccid.io](https://fccid.io/) - FCC filings and documentation
- [datasheetspdf.com](https://datasheetspdf.com/) - Chip datasheets
- [pinout.xyz](https://pinout.xyz/) - Raspberry Pi and other pinouts
- [iFixit](https://www.ifixit.com/) - Device teardowns
- [GitHub](https://github.com/) - Code and research

## Typical Lab Setup

```
Workbench:
- Soldering iron and stand
- USB microscope on arm
- ESD mat
- Storage for components and tools
- Device under test

Desk:
- Main computer with Ghidra, text editor
- Monitor for serial output or disassembly
- SSH connection to Raspberry Pi

Network:
- Raspberry Pi (wired or WiFi)
- Main computer
- Device under test (if wireless)
```

## Starting Budget (Minimal)

- Raspberry Pi 4: $50-100
- Jumper wires: $5
- USB-to-serial: $5
- Multimeter: $20
- Logic analyzer: $10
- USB microscope: $30

**Total: ~$120-170** for a functional hardware hacking kit

Add as needed:
- Soldering iron ($30) when you need to solder
- PiFex ($75) when you're serious about SWD/JTAG
- Better multimeter ($40) when you need precision

## Pro Tips

1. **Document everything** - Take photos, write notes, keep the original firmware
2. **Start simple** - UART > SPI > SWD. Each builds on the last
3. **Buy what you need** - Don't overinvest in tools you won't use
4. **Join communities** - Reddit r/hardwarehacking, Matt Brown's Discord, GitHub issues
5. **Read datasheets** - They answer most questions you'll have
6. **Be patient** - Hardware hacking takes time. Rushing causes mistakes
7. **Keep backups** - Always save the original firmware before modifying

## Resources

- [JAXLUG 2025 Talk - Hardware Hacking with Linux](https://www.youtube.com/watch?v=7pVtVpKTGqs)
- [Ghidra Official Documentation](https://ghidra-sre.org/)
- [ARM CMSIS Documentation](https://arm-software.github.io/CMSIS_5/)
- [Flashrom Manual](https://www.flashrom.org/Documentation)
- [OpenOCD User Guide](http://openocd.org/doc/html/index.html)
