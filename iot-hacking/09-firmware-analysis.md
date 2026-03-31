# Firmware Analysis - From Binary to Code

![Slide 13: What's Next](./images/slide-13.png)

Once you have the firmware binary (from SPI, SWD, UART, or bootloader), the next step is to understand it. This is reverse engineering: taking compiled, optimized code and turning it back into something readable.

Modern tools like Ghidra make this dramatically easier.

## Ghidra Basics

Ghidra is the NSA's free reverse engineering tool. It disassembles binaries, identifies functions, generates pseudo-code, and even has plugins for specialized formats.

### Install Ghidra

1. Download from https://ghidra-sre.org/
2. Extract to a directory (e.g., ~/tools/ghidra)
3. Run: `./ghidraRun`

### Open a Binary

1. File > Open As Binary (or drag the file)
2. Select the file
3. When prompted, choose:
   - Language: ARM (Cortex-M4, Cortex-M3, etc) or x86 or MIPS, depending on the CPU
   - Compiler: Usually "default" works
   - Click OK
4. Let Ghidra auto-analyze (this takes minutes for large binaries)

### The Ghidra Interface

- **Listing pane** (left): Shows assembly code with addresses
- **Decompiler pane** (right): Shows pseudo-code (looks like C)
- **Symbol tree** (bottom left): Lists functions and data structures
- **Address bar** (top): Jump to specific memory addresses

## Reading Disassembly

ARM assembly is relatively readable. Key instructions:

```asm
PUSH {r0-r3, lr}    # Push registers and return address onto stack
MOV r0, #0x100      # Move immediate value to register
LDR r0, [r1]        # Load from memory address in r1
STR r0, [r1]        # Store to memory address in r1
CMP r0, r1          # Compare (sets flags)
BEQ label           # Branch if Equal
BNE label           # Branch if Not Equal
CALL function       # Call a function
RET                 # Return from function
```

The pseudo-code (right pane) is more readable and shows the logic in C-like syntax.

## Finding Interesting Functions

When Ghidra loads a binary, it identifies some functions automatically. But many are missed.

### Search for Strings

Firmware often contains human-readable strings. Find them, and you find important functions.

```
Listing > String Search (or Ctrl-F)
```

Search for:
- "password"
- "error"
- "debug"
- "config"
- "version"
- Function names you recognize
- WiFi SSID
- API endpoints

When you find a string, right-click it and select "References" to see where it's used in code. This leads you to important functions.

### Look at the Entry Point

The entry point is where execution starts. In ARM:
1. Vector table at address 0x00000000
2. First entry is the initial stack pointer
3. Second entry is the reset handler (first code to run)

Jump to the reset handler and look at what it does:
- Initialize hardware
- Call main() or app_main()
- Enter a loop

From there, you trace forward to understand the program flow.

### Analyze Known Imports

If the firmware uses a well-known library (like OpenSSL, mbedTLS, lwIP for networking), Ghidra sometimes recognizes it and imports symbol information.

In the Symbol Tree, expand "External Libraries" to see what's available.

## Identifying Security Checks

Security vulnerabilities are often simple:

**Check for**:
- Password/PIN validation (strcmp, strncmp with a hardcoded string)
- Access level checks (if user_level >= 3, allow)
- Timeout values (if counter > 600, reboot)
- Crypto key usage (where keys are loaded and used)
- Authentication (where device checks credentials)

Example: You find a function that checks a PIN:

```c
if (strcmp(user_input, "1234") == 0) {
    grant_access();
} else {
    deny_access();
}
```

You can:
- Change the PIN to something you know
- Patch the comparison to always be true
- Call grant_access() directly without checking

## Using the SVD Loader Plugin

ARM provides SVD (System View Description) files that map memory to registers. Ghidra can load these.

### Install SVD Loader

1. Download from: https://github.com/leveldown-security/ghidra-svd
2. Extract to Ghidra's extension directory: `~/.config/Ghidra/extensions/` (or similar)
3. Restart Ghidra

### Load SVD File

1. Open your firmware in Ghidra
2. File > Load SVD File
3. Select the SVD file for your chip (e.g., STM32F1.svd)
4. Ghidra now maps memory addresses to register names

### Example

Without SVD:
```
0x40013800: mov r0, 0x0001
0x40013804: mov r1, 0x0000
```

With SVD (STM32F1):
```
0x40013800 (TIM1_CR1): mov r0, 0x0001  # Enable Timer 1
0x40013804 (TIM1_CR2): mov r1, 0x0000
```

Suddenly you understand what the code is doing: configuring timers, setting up GPIO, managing peripherals.

## Making Changes

Once you understand a function and want to modify it:

### Option 1: Hex Editor

Edit the binary directly at the byte level:
1. Tools > Hex Editor (or Alt-H)
2. Navigate to the address
3. Modify bytes
4. Save

For simple changes (like a timeout value), this works:

Find the instruction:
```
0x08001234: cmp r0, 0x258  # Compare to 600 (0x258 in hex)
```

Want to change the timeout to 3600? Change 0x258 to 0xe10.

### Option 2: Reassemble with Build Tools

If you have the source code (or can reverse-engineer it) and the original toolchain:

1. Modify the source or assembly
2. Recompile with the original compiler
3. Link with the original libraries
4. Compare with the original to ensure compatibility

This is complex but produces reliable results.

### Option 3: Patching Tools

Some projects have automated patching tools:

```bash
# Hexdump to find the target
xxd firmware.bin | grep "pattern you want to change"

# Use sed or Python to replace bytes
python3 -c "
with open('firmware.bin', 'rb') as f:
    data = f.read()
data = data.replace(b'\\x00\\x01', b'\\x00\\x02')  # Example patch
with open('firmware_patched.bin', 'wb') as f:
    f.write(data)
"
```

## Verifying Your Changes

After modifying:

1. Re-flash to the device
2. Test that your changes work as expected
3. Watch for side effects
4. Document what you changed and why

Keep the original and modified binaries. Later, you might want to understand what broke.

## Advanced Techniques

### Cross-References

Ghidra shows where functions are called:
1. Right-click a function name
2. Select "Show References"
3. Jump to each call site

This traces the program's logic flow.

### Data Types and Structures

Many binaries use structured data (arrays, custom types). Ghidra tries to infer these:

```c
// Ghidra deduced this structure:
typedef struct {
    char ssid[32];
    char password[64];
    uint8_t security_type;
    uint32_t flags;
} wifi_config_t;
```

You can manually define structures to make analysis clearer:
1. Data > Define Structure
2. Add fields with names and types
3. Apply to memory locations

### GDB Integration

For debugging, connect a running device via SWD and step through code in Ghidra in real-time.

This is advanced and requires both Ghidra and GDB, but it's powerful: you see the code, set breakpoints, step through, and watch registers change.

## IDA Pro Alternative

IDA Pro is the commercial alternative to Ghidra. It's very powerful but expensive ($$ - $$$).

IDA includes:
- Better auto-analysis (recognizes more patterns)
- Debugger integration
- Many plugins
- Community scripts

For professional work, some prefer IDA. For learning and personal projects, Ghidra is excellent and free.

## Real-World Example: Modifying a Timeout

Scenario: Your truck's remote start times out after 10 minutes. You want 30 minutes.

### Step 1: Extract and Analyze Firmware

Dump the firmware from the truck's receiver module (assuming you can access it via SPI or SWD).

### Step 2: Search for the Timeout Value

In Ghidra, search for "600" (10 minutes in seconds) or "0x258" (600 in hex).

Find it in a function:
```c
void check_remote_timeout() {
    if (remote_timer > 600) {  // 10 minutes
        disable_remote_start();
    }
}
```

### Step 3: Identify the Instruction

Ghidra shows the exact instruction and address:
```
0x08003400: cmp r0, 0x258
```

This compares register r0 to 0x258 (600). If r0 is greater, the timeout triggers.

### Step 4: Calculate the New Value

30 minutes = 1800 seconds = 0x708 in hex

### Step 5: Patch the Binary

Use a hex editor to change 0x258 to 0x708:
```
Original: ... 0x258 ...
Modified: ... 0x708 ...
```

Or use Python:
```python
with open('firmware.bin', 'rb') as f:
    data = bytearray(f.read())

# Find and replace (be specific to avoid false matches)
# Assuming little-endian ARM: 0x258 is stored as 58 02 00 00
import struct
offset = 0x08003400 - 0x08000000  # Adjust for your base address
struct.pack_into('<I', data, offset, 0x708)

with open('firmware_patched.bin', 'wb') as f:
    f.write(data)
```

### Step 6: Flash and Test

Flash the modified firmware back to the truck's receiver using SPI or SWD.

Test: Turn on the remote start. Count to verify it runs for 30 minutes now.

### Step 7: Document

Write down:
- What firmware version you modified
- What change you made (address, original value, new value)
- Why you made it
- Whether it worked
- Any side effects

## Limitations

Firmware analysis is powerful but has limits:

- Encrypted firmware cannot be analyzed (decrypt it first, if possible)
- Optimized code is harder to understand than source
- You're reading someone else's code without documentation
- One mistake in patching can break everything
- Some changes might trigger watchdog timers or security checks

Start simple: read strings, understand the structure, find obvious functions. Graduate to modifications only after you're confident.

## Next Steps

With firmware analysis skills:
1. Find security vulnerabilities
2. Understand device behavior
3. Make targeted modifications
4. Contribute security research
5. Build on existing firmware (unofficial custom firmwares)

Many popular IoT devices have active reverse engineering communities. Search GitHub for "[device name] firmware reverse engineering" to see what others have discovered.

Hardware hacking combines hardware skills (finding interfaces, connecting hardware) with reverse engineering (understanding binary firmware). Master both, and you can modify nearly any device.
