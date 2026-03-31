# Introduction

## Why Vessel Hacking?

The utilization of Unmanned Aerial Systems (UAS) gets all the headlines, but maritime vessels present an equally fascinating and arguably more critical attack surface. Ships carry global commerce, transport passengers, and increasingly rely on autonomous systems.

The technology on many vessels is 30+ years old. As boats get more complex, the ability to hack them becomes easier: more systems, more attack surface. It's a blessing on the red team side, a curse on the blue team side.

## The Rabbit Hole

It often starts with a specific need. In one case, a penetration tester needed to test an autonomous vessel's GPS resilience. GPS spoofing over RF was off the table: you can't ensure RF isolation on open water, and GPS spoofing carries serious legal consequences.

The insight: instead of spoofing GPS signals to the receiver, why not just *be* the GPS receiver on the NMEA bus? If you can emulate the GPS device on the instrument network, you can feed whatever position data you want to the autopilot, chart plotter, and every other system that consumes GPS.

And that's when things got interesting: NMEA 2000 is just CAN bus. The same CAN bus that runs in every modern car. If you've done any automotive security research, you already have most of the skills you need.

## What You'll Learn

This playbook covers:

- **Vessel network architecture** from wireless down to instrument buses
- **NMEA 0183 and NMEA 2000** protocols in detail
- **Hardware interfaces** from $15 DIY to $600 commercial
- **Software tools** for simulation, targeting, and exploitation
- **CAN bus vulnerabilities** applied to maritime systems
- **Practical attack techniques** including spoofing, DoS, sniffing, and MITM
- **Lab setup** so you can practice at home without prison time

## Key Insight

CAN bus, whether it's in a car, a boat, an airplane, or a train, was designed without security. There's no authentication, no encryption, and any node on the bus is trusted. If you have physical access to the bus, you own it.

The maritime industry knows this is a problem, but the fix (migrating to Ethernet everywhere) means running new cable through cramped spaces on vessels that have been in service for decades. Realistic timeline for industry-wide change: 20+ years.

This stuff is vulnerable now, and it's going to stay vulnerable for the foreseeable future.
