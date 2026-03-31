# Chapter 1: Introduction to Hardware Hacking

![Slide 4: Targets](./images/slide-04.png)

## Why Hardware Hack?

Hardware hacking starts with curiosity. Something is broken, or something is not working the way you want it to. You take it apart and figure out why.

The truth is simple: *It's okay to take things apart.*

As a child, you might have torn apart an old radio or broken toy. Maybe you learned something. Maybe you broke it permanently. Either way, you learned. Now we do the same thing, but with the knowledge that we need, using proper tools and techniques.

Hardware hacking has real, tangible benefits:

1. **Troubleshooting** - Your device isn't working right. Dig into the hardware to understand why
2. **Trust and Verify** - Don't trust what companies tell you. Verify what the device actually does by looking at the firmware
3. **Extending Features** - Your truck has a 10-minute remote start timer. You want it to work from a mile away. Hack it
4. **Building Your Own** - Learn from existing designs. Use open-source schematics. Build something better
5. **Security Research** - Find vulnerabilities. Report them responsibly. Get paid through bug bounty programs
6. **Learning** - Every device is a circuit with pieces that talk to each other. Understanding how teaches you about electronics and embedded systems

## What Can You Hack?

### Old, Broken Hardware

Your greatest resource is broken hardware. A device that no longer works is perfect for learning. You cannot break something that's already broken. Grab that old router, that ancient coffee maker, the wireless speaker that went silent. These are your training grounds.

### Conference Badges

If you attend conferences like Defcon, Black Hat, or smaller regional security events, you have access to hardware badges. Badge designers are creative. They build in challenges. They try new features. Studying how others have solved design problems teaches you tremendously. Plus, the badges are designed to be hacked. That's part of the fun.

### Training Boards

Organizations like Ptoria offer official training boards and challenges designed specifically to teach hardware hacking fundamentals. These are wonderful. They have labeled interfaces, intentional vulnerabilities, and a clear progression of difficulty. If you find a class at a conference, take it.

### Untrusted and Cheap Devices

Devices from unknown manufacturers, especially cheap ones from AliExpress or Amazon, are perfect targets. If the manufacturer won't put their name on it, they won't come after you if you open it. A 30-dollar IoT device is a fantastic learning tool. If you break it, you only lost 30 dollars and gained knowledge.

### Bug Bounty Targets

Companies like Logitech, Ring, and various vendors on HackerOne actively pay for hardware vulnerabilities. These are not theoretical exercises. You can find real bugs, write real reports, and get paid. Bug bounty is a legitimate path from hobby to career.

## Goals: Why You're Here

![Slide 5: Goals](./images/slide-05.png)

### Troubleshoot

Something is not working. You want to know why. Maybe the device intermittently connects to the network. Maybe the battery doesn't charge fully. Maybe it spontaneously reboots. By examining the boot console (UART), monitoring bus traffic (SPI/I2C), and dumping the firmware, you can figure out what's going wrong.

### Trust and Verify

Your wireless device says it's not transmitting. Your USB hub claims it's not recording anything. Companies make claims about security and privacy. The only way to truly know is to look at the hardware and firmware yourself.

### Expand Features

Your car's remote start times out after 10 minutes. You live in Florida and have a dog. That's a problem. The solution: find the wireless receiver module, dump its firmware, modify the timeout value, re-flash it, and now your truck starts remotely from a mile away. This is what extending features means.

### Build Your Own

You see how badges work. You understand how sensors connect via I2C. You know how to program an MCU. Now you build something. You design a PCB. You integrate a module. You learn that building something from scratch is harder than modifying something existing, but infinitely more rewarding.

### Exploit and Report

The S in IoT stands for security. Joke, but not a joke. Many devices have trivial vulnerabilities. Weak firmware verification. No encryption on debug interfaces. Hardcoded credentials. When you find these issues, you have two responsibilities: confirm they are real, and report them so they can be fixed.

## The Hacker Mindset

Hardware hacking requires a specific approach:

**Methodical** - You follow a process. Disassemble, identify, research, find interfaces, monitor, dump, analyze, modify. You do not guess. You verify.

**Patient** - Hardware doesn't care about your timeline. A chip might take 30 seconds to respond. A flash dump might take 10 minutes. You wait.

**Curious** - Why does the device boot before setting the watchdog? Why does that line toggle every 10 seconds? Why is that signal different when the device is idle versus active? Your curiosity drives investigation.

**Careful** - Electrostatic discharge can destroy a chip permanently. Jumper wires can slip. A solder bridge can kill a microcontroller. You use ESD protection. You check your connections twice. You test before you power on.

**Humble** - You will get stuck. You will make mistakes. You will break things. This is learning. You ask for help. You read the datasheet more carefully. You try a different approach.

## What You'll Discover

As you hack devices, you'll find:

- Debugging interfaces left enabled in production (UART, SWD, JTAG)
- Firmware loaded from unencrypted flash that anyone can read
- Credentials and keys baked into the firmware
- Capabilities disabled in software that the hardware supports
- Sensors accessible via standard protocols with no authentication
- Network services listening on unexpected ports

None of this is exotic or rare. It's standard practice. Resources are limited. Security costs time. Many teams just want to ship. Your job is to find these issues, report them, and teach people how to do better.

## What This Playbook Covers

This guide walks you through the complete process:

- Tools you need (and which ones to buy first)
- How to set up a Raspberry Pi and PiFex for hacking
- The standard process for any device
- How to find information about chips and devices
- How to connect to and read from UART
- How to dump SPI flash without desoldering
- How to use SWD or JTAG to read and modify firmware
- How to analyze firmware with Ghidra
- How to set up your own hardware hacking lab

Every chapter includes practical examples and real commands you can run.

## Your First Challenge

If you're starting now, here's what to do:

1. Get an old broken device
2. Safely open it
3. Take notes and photos
4. Try to identify the main microcontroller (look for printed text like "STM32", "ESP32", "NXP")
5. Search for that chip name plus "datasheet"
6. Look for test points or header pads (these are debugging interfaces)
7. Search "FCC ID" on the device label to find official documentation

You do not need expensive equipment yet. You need curiosity and patience.

The rest of this playbook teaches you the tools and techniques to go deeper.
