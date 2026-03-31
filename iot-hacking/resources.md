# Resources and Further Learning

This chapter is a curated list of resources to deepen your hardware hacking knowledge. It includes tools, communities, tutorials, documentation, and events.

## Official Documentation

### ARM and Processor Resources

- [ARM Cortex-M Documentation](https://developer.arm.com/) - Processor docs, memory maps, instruction encodings
- [CMSIS SVD Repository](https://github.com/ARM-Software/CMSIS-SVD) - Register definitions for ARM chips
- [ARM Instruction Set Reference](https://developer.arm.com/documentation/) - Architecture reference manuals

Read the ARM documentation when you need to understand processor behavior, memory maps, or instruction encodings.

### Ghidra

- [Ghidra Home](https://ghidra-sre.org/) - NSA's free reverse engineering suite
- [Ghidra GitHub](https://github.com/NationalSecurityAgency/ghidra) - Source, issues, and community
- [Ghidra Release Notes](https://ghidra-sre.org/releaseNotes.html) - Version history and new features

Ghidra has extensive docs and a helpful community on the GitHub repository.

### Tools Documentation

- [Flashrom Manual](https://www.flashrom.org/Documentation) - SPI flash reading/writing
- [OpenOCD Documentation](http://openocd.org/doc/) - On-chip debugger for SWD/JTAG
- Linux man pages: `man flashrom`, `man screen`, `man openocd`

These are your quick reference for command-line tools.

## Tutorials and Guides

### Video Tutorials

- [JAXLUG 2025: Hardware Hacking with Linux](https://www.youtube.com/watch?v=7pVtVpKTGqs) - The source talk for this playbook
- [Matt Brown's Hardware Hacking Channel](https://www.youtube.com/c/mattbrowneng) - Excellent real-world hacking demonstrations
- [LiveOverflow](https://www.youtube.com/c/LiveOverflow) - Security research and CTF walkthroughs
- [stacksmashing](https://www.youtube.com/c/stacksmashing) - Hardware security and reverse engineering

### Written Guides

- [Adafruit Learning System](https://learn.adafruit.com/) - Includes reverse engineering and GPIO tutorials
- [CTF Writeups on GitHub](https://github.com/topics/ctf-writeups) - Real examples of reverse engineering
- [Azeria Labs ARM Assembly](https://azeria-labs.com/writing-arm-assembly-part-1/) - ARM exploitation tutorials

## Communities and Collaboration

### Online Communities

- [r/hardwarehacking](https://www.reddit.com/r/hardwarehacking/) - Reddit community dedicated to hardware hacking
- [r/reverseengineering](https://www.reddit.com/r/reverseengineering/) - Broader reverse engineering community
- [r/netsec](https://www.reddit.com/r/netsec/) - Network security news and discussion
- [DEF CON Groups](https://defcongroups.org/) - Local DEF CON communities in most cities
- [2600 The Hacker Quarterly](https://www.2600.com/) - Magazine and [meetup groups](https://www.2600.com/meetings/)

### Discord Servers and Chat

- [Matt Brown's Hardware Hacking Discord](https://discord.gg/mattbrown) - Active collaboration on real devices
- [Chaos Communication Club](https://www.ccc.de/) - European hacker community
- [Hack Spaces](https://hackerspaces.org/) - Find local Hack Spaces, Makerspaces, or Fab Labs

### Conferences and Events

- [DEF CON](https://defcon.org/) - Las Vegas, August. Premier hacker conference with hardware villages and badge hacking
- [Black Hat](https://www.blackhat.com/) - Multiple locations. Security-focused, includes hardware tracks
- [Chaos Communication Congress](https://events.ccc.de/) - Annual European conference
- [Maker Faire](https://makerfaire.com/) - Local events showcasing makers and tinkerers
- [BSides](http://www.securitybsides.com/) - Community-driven security conferences worldwide
- [OWASP Events](https://owasp.org/events/) - Local security meetups and chapter meetings

Conferences are invaluable for learning, networking, and getting inspired. Many share presentation materials and videos online later.

## Bug Bounty and Responsible Disclosure

### Bug Bounty Platforms

- [HackerOne](https://www.hackerone.com/) - Largest platform, many hardware programs
- [Bugcrowd](https://www.bugcrowd.com/) - Bug bounty and vulnerability disclosure
- [Synack](https://www.synack.com/) - Invite-only security testing

These platforms connect researchers with companies that want security testing. Many have hardware programs (Ring, Logitech, etc).

### Responsible Disclosure

If you find a vulnerability and the manufacturer isn't on a bug bounty platform:

1. Find contact info: look for a `security.txt` file (`/.well-known/security.txt`) or a security page
2. Draft a report: clearly describe the vulnerability, impact, and proof-of-concept
3. Send it: use PGP encryption if they provide a key
4. Wait: give them reasonable time (typically 30-90 days) to fix it
5. Disclose responsibly: if they don't respond, you can disclose publicly after a reasonable period

**Never:**
- Test on devices you don't own without permission
- Break laws (unauthorized access is illegal)
- Demand payment (this is extortion)
- Disclose the vulnerability publicly before giving the vendor time to fix

## Hardware Hacking Specific Guides

### Chip Identification and Datasheets

- [FCC ID Lookup](https://fccid.io/) - FCC filing database with internal photos
- [Datasheets PDF](https://datasheetspdf.com/) - Mirror of many datasheets
- [All Datasheet](https://www.alldatasheet.com/) - Another datasheet mirror
- [Octopart](https://octopart.com/) - Component search with datasheets

### Reverse Engineering Resources

- [Ghidra](https://ghidra-sre.org/) - Free, open-source reverse engineering suite
- [IDA Pro](https://www.hex-rays.com/ida-pro/) - Commercial disassembler
- [Binary Ninja](https://binary.ninja/) - Modern disassembler, alternative to Ghidra
- [Radare2](https://rada.re/) - Open-source, command-line focused
- [Capstone Engine](https://www.capstone-engine.org/) - Disassembly library

## Books

- [The Hardware Hacking Handbook](https://nostarch.com/hardwarehacking) - Colin O'Flynn, Jasper van Woudenberg
- [Practical IoT Hacking](https://nostarch.com/practical-iot-hacking) - Fotios Chantzis et al
- [The Hacker Playbook 3](https://www.thehackerplaybook.com/) - Peter Kim (Practical security testing)
- [ARM System Developer's Guide](https://www.elsevier.com/books/arm-system-developers-guide/sloss/978-1-55860-874-0) - Andrew Sloss, Dominic Symes, John Upton

## Tools and Projects to Study

### Open Source Hardware Projects

- [Arduino](https://www.arduino.cc/) - Beginner-friendly microcontroller
- [Raspberry Pi](https://www.raspberrypi.com/) - What we're using for hacking
- [ESP32 (Espressif)](https://www.espressif.com/) - WiFi/Bluetooth SoC, very popular in IoT
- [STM32 (ST Micro)](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html) - ARM Cortex-M family, common in products

### Firmware Project Examples

- [OpenWrt](https://openwrt.org/) - Custom router firmware
- [LibreMesh](https://libremesh.org/) - Community mesh networks
- [ESPHome](https://esphome.io/) - Home automation with ESP devices
- [RIOT OS](https://www.riot-os.org/) - Operating system for IoT

## Staying Current

### Blogs and News

- [Hacker News](https://news.ycombinator.com/) - Tech news, often includes security
- [OWASP Blog](https://owasp.org/blog/) - Application and system security
- [Exploit Database](https://www.exploit-db.com/) - Published exploits and advisories

### Podcasts

- [Hackers IRL](https://hackersirl.com) - Raw tales from infosec conferences
- [Security Now!](https://www.grc.com/SecurityNow.htm) - Weekly security news and deep dives
- [Darknet Diaries](https://darknetdiaries.com/) - True stories from the hacking world

## Practice Projects

After reading this playbook, try these in order:

1. Find UART on a device: easiest first step, just read console output
2. Dump firmware via SPI: learn flashrom, practice soldering
3. Analyze in Ghidra: identify functions, find strings
4. Patch a value: change a timeout or constant, verify it works
5. Find a vulnerability: document your findings responsibly
6. Report the bug: follow responsible disclosure, help the vendor fix it

Each project teaches multiple skills and builds confidence.

## Contributing Back

Once you've learned:

1. Write tutorials: share what you learned on your blog or GitHub
2. Create tools: build scripts that solve problems you encountered
3. Participate in communities: answer others' questions, collaborate
4. Present at conferences: share your findings and techniques
5. Contribute to open source: help projects like [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [Flashrom](https://www.flashrom.org/), [OpenOCD](http://openocd.org/)
6. Help vendors: report vulnerabilities professionally, help them improve

The security community grows through knowledge sharing.
