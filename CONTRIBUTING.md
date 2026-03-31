# Contributing to Awesome Hacking Playbook

Thanks for wanting to contribute. This project thrives on community knowledge.

## Quick Start

1. **Fork** this repo
2. **Create a branch** for your changes
3. **Write or edit** content in the relevant playbook directory
4. **Submit a PR** with a clear description of what you added or changed
5. We review, discuss, and merge

## What We're Looking For

- **New chapters or sections** within existing playbooks
- **New playbooks** on security topics (propose via issue first)
- **Tool recommendations** with real-world context
- **Lab setup guides** that others can follow
- **Corrections** to existing content (technical accuracy matters)
- **Better explanations** of existing concepts

## Content Guidelines

### Tone and Style

- Write for practitioners, not academics
- Be direct and practical. "Here's how to do X" beats "One might consider..."
- Include actual commands, tool names, and configuration examples
- Use code blocks for commands and file contents
- No emdashes or endashes. Use commas, periods, or semicolons instead

### Structure

Each playbook follows a consistent layout:

```
playbook-name/
├── README.md          # Overview and table of contents
├── 01-introduction.md # Background and motivation
├── 02-topic.md        # Core content chapters (numbered)
├── images/            # Slide images and diagrams
├── tools.md           # Relevant tools and hardware
├── lab-setup.md       # How to build a practice environment
├── resources.md       # Links, references, further reading
└── MANIFEST.json      # Chapter listing for the web reader
```

When adding a chapter, also update `MANIFEST.json` so it appears on the website.

### Images

- Place images in the playbook's `images/` directory
- Reference them with relative paths: `./images/my-diagram.png`
- Keep file sizes reasonable (compress PNGs, use JPEG for photos)
- Diagrams and screenshots are great. Stock photos are not.

### What NOT to Submit

- Classified, restricted, or export-controlled content
- Active 0day exploits (responsible disclosure applies)
- Content copied from copyrighted sources without permission
- Marketing or promotional material
- AI-generated content that hasn't been verified by a human practitioner

## Proposing a New Playbook

Want to start a whole new playbook? Open an issue first with:

- **Topic**: What area of security does it cover?
- **Scope**: What chapters would it include?
- **Source**: What's your background or source material?
- **Commitment**: Can you write the initial content, or are you proposing for someone else?

We'll discuss it in the issue before you start writing.

## Code of Conduct

- Be respectful. Disagree on technical merit, not personality.
- No gatekeeping. Everyone started somewhere.
- Share knowledge freely. That's the whole point.

## License

By contributing, you agree that your contributions are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). You retain authorship credit, but the content stays open.

## Questions?

Open an issue. We'll figure it out together.
