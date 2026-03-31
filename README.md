# 🔓 Awesome Hacking Playbook

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

**Community-curated, open-source hacking playbooks for security researchers, penetration testers, and curious minds.**

> *"Why build out notes for myself and hoard that? Let's create something that's a really good resource for the community."*

## 📖 Playbooks

| Playbook | Status | Description |
|----------|--------|-------------|
| [Vessel Hacking](./vessel-hacking/) | 🚧 Active | Maritime cybersecurity: NMEA 0183/2000, CAN bus attacks, GPS spoofing, shipboard networks |
| [IoT Hacking](./iot-hacking/) | 🚧 Active | Hardware hacking with Linux: UART, SPI, SWD/JTAG, firmware extraction, Ghidra analysis |
| Phone Hacking (Phreaking) | 📋 Planned | SS7, VoIP/SIP, cellular baseband, SIM cloning, modern phreaking |
| Satellite Hacking | 📋 Planned | SatCom, VSAT, ground station security |

## 🤝 How to Contribute

1. **Fork** this repo
2. **Add or edit** content in the relevant playbook directory
3. **Submit a PR**  -  we review and merge community contributions
4. That's it. No gatekeeping.

### Content Guidelines

- Write for practitioners, not academics
- Include tools, techniques, and real-world context
- Link to original sources when possible
- No classified or restricted content
- Responsible disclosure applies  -  don't publish active 0days

## 🏗️ Structure

Each playbook follows the same structure:

```
playbook-name/
├── README.md          # Overview and table of contents
├── 01-introduction.md # Background and motivation
├── 02-topic.md        # Core content chapters
├── tools.md           # Relevant tools and hardware
├── lab-setup.md       # How to build a practice environment
└── resources.md       # Links, references, further reading
```

## 🌐 Website

These playbooks are rendered at [hackingplaybook.com](https://hackingplaybook.com) with a fancy interface, search, and premium quiz features.

The content here is the source of truth. The website reads from this repo.

## 📜 License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Share it, remix it, just give credit and keep it open.

## ⚠️ Disclaimer

This content is for **educational and authorized security testing purposes only**. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal. The authors are not responsible for misuse of this information.

---

*Maintained by the community. Built on the hacker ethos of sharing knowledge.*
