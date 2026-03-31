# IoT/Hardware Hacking Playbook

Welcome to the Hardware Hacking with Linux field manual. This playbook is your guide to extracting, analyzing, and modifying firmware on embedded devices using Linux, Raspberry Pi, and specialized tools.

## What You'll Learn

This playbook covers the complete hardware hacking workflow:

- **Physical teardown** of devices and board identification
- **OSINT techniques** for chip identification and datasheet hunting
- **Serial interfaces** (UART) for boot console access
- **SPI flash** dumping and firmware extraction
- **Debug interfaces** (SWD/JTAG) for firmware access and modification
- **Firmware analysis** with Ghidra and IDA Pro
- **Lab setup** and tool recommendations

## Who This Is For

This playbook is for:

- Security researchers and bug bounty hunters
- Embedded systems enthusiasts
- IoT device owners who want to understand their hardware
- Conference badge hackers
- Anyone curious about how devices really work

## Important Disclaimer

This knowledge can be used for both good and bad purposes. Use it ethically:

- Only modify devices you own or have explicit permission to test
- Responsibly disclose vulnerabilities through proper channels
- Report bugs to vendors through HackerOne, vendor programs, or responsible disclosure platforms
- Build things, make them better, help make the world safer
- Do not use this to cause harm

## How To Use This Playbook

Start with the introduction to understand your targets and goals, then work through the tools section to build your kit. Follow the process guide step-by-step for your first hardware hack. Jump to specific chapters (UART, SPI, SWD) as needed for your target device.

Chapters include command syntax and examples where available. This playbook is a living document and some sections are still being expanded.

## Quick Links

- **First Time?** Read [01-introduction.md](01-introduction.md)
- **Building Your Lab?** See [lab-setup.md](lab-setup.md)
- **Need Tools?** Check [tools.md](tools.md)
- **Finding Datasheets?** Look at [05-osint.md](05-osint.md)

## Attribution

This playbook is based on "Hardware Hacking with Linux" by John "Panda" Aff, presented at JAXLUG 2025. The talk covered practical hardware hacking methodologies, tools, and real-world demonstrations using Raspberry Pi, PiFex, and common IoT devices.

## License

CC BY-SA 4.0 - You are free to share and adapt this content with attribution.

---

*"It's okay to take things apart."* - Hardware hackers everywhere
