# 🔌 IoT/Hardware Hacking Playbook

A practical guide to hardware hacking with Linux. Built from real-world embedded device testing experience and community contributions.

## Table of Contents

1. [Introduction](./01-introduction.md)  -  Why hardware hacking matters
2. [Tools and Equipment](./02-tools.md)  -  Building your hardware hacking toolkit
3. [Linux and Raspberry Pi Setup](./03-linux-setup.md)  -  Setting up your hacking platform
4. [The Hardware Hacking Process](./04-process.md)  -  Step-by-step methodology
5. [OSINT for Hardware](./05-osint.md)  -  Finding datasheets and documentation
6. [UART](./06-uart.md)  -  Serial boot consoles and debug output
7. [SPI Flash](./07-spi.md)  -  Dumping firmware from flash chips
8. [SWD and JTAG](./08-swd-jtag.md)  -  Debugging and control interfaces
9. [Firmware Analysis](./09-firmware-analysis.md)  -  From binary to code
10. [Lab Setup](./lab-setup.md)  -  Build your own test environment
11. [Tools](./tools.md)  -  Hardware and software toolkit
12. [Resources](./resources.md)  -  Links, references, further reading

## Who This Is For

- Security researchers and bug bounty hunters
- Embedded systems enthusiasts
- IoT device owners who want to understand their hardware
- Conference badge hackers
- Anyone curious about how devices really work

## Background

IoT devices run on embedded processors with debug interfaces left exposed, firmware stored in readable flash chips, and serial consoles waiting for a connection. If you can open the case, you can usually get root.

The same techniques that work on a $5 smart plug work on industrial controllers, medical devices, and automotive ECUs. UART, SPI, SWD, and JTAG are everywhere.

Every new connected device is another target. More devices = more attack surface.

## Important Disclaimer

This knowledge can be used for both good and bad purposes. Use it ethically:

- Only modify devices you own or have explicit permission to test
- Responsibly disclose vulnerabilities through proper channels
- Report bugs to vendors through HackerOne, vendor programs, or responsible disclosure platforms
- Build things, make them better, help make the world safer
- Do not use this to cause harm

## Contributing

See the [main contribution guide](../README.md#-how-to-contribute). For IoT/hardware-specific content, we especially welcome:

- Real-world device teardown writeups
- New tool discoveries or reviews
- Protocol analysis and chip documentation
- Lab setup guides and equipment reviews
- Firmware extraction walkthroughs

## Attribution

This playbook is based on "Hardware Hacking with Linux" by John "Panda" Aff, presented at JAXLUG 2025. The talk covered practical hardware hacking methodologies, tools, and real-world demonstrations using Raspberry Pi, PiFex, and common IoT devices.

## License

CC BY-SA 4.0 - You are free to share and adapt this content with attribution.
