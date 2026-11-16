# AC/DC as standalone FX processor (no computer connected)

Research date: 2026-10-23. Thread under study: https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244 (OP "m9dfukc" = Andreas). Source code checked: RebelTechnology/OpenWare `master`/`develop` = tag v22.5.0 (commit 62a0187, 2023-03-05), cloned from https://github.com/RebelTechnology/OpenWare . No newer OpenWare release tag exists (latest tags: v22.5.rc1..rc4, v22.5.0).

## 1. What exactly was asked and answered in thread #2244

### Takeaway
The OP asked how to get a firmware where AC/DC runs a patch like a Lich when no computer is attached and acts as an audio interface when attached. Stas Shtin (antisvin, forum admin) answered that the audio routing between patch and USB is a compile-time choice, that automatic switching is not implemented and not ideal, and pointed to FAUST via his own OwlProgram branch. The thread ended on 2024-12-09 with the OP switching to a borrowed Befaco Lich. Nothing was solved or posted after that.

### Cited Findings
All from https://community.rebeltech.org/t/2244.json (7 posts, read in full):
- **#1, Andreas (m9dfukc), 2024-11-14.** He has two AC/DCs that have sat unused for a long time. He gives two reasons: the noise floor is too high for interface use (linking https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072), and he mostly uses the module as a scope input for VCV Rack. He asks what firmware patching it would take for AC/DC to (A) act as a patchable FX/synth like the Lich when not connected to a computer and (B) act as an audio interface when connected. He asks @antisvin for the modified firmware mentioned before, and notes to @Befaco that the module seems to be discontinued.
- **#2, antisvin, 2024-11-14.**
  - He did not know it was discontinued. He suspects hardware problems needing a redesign: the noise, codec stability for some users, OS-specific USB issues and hard-to-understand firmware issues.
  - He expects no updates from Rebel Technology any time soon.
  - He points to https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110/5 .
  - **Key statement:** "Right now it's a compilation option, you have choose audio flow order between patch and USB when building firmware."
  - He sees quad audio as the ideal use (4-channel panner or reverb). Befaco never released the MIDI expander, so with only 4 knobs the module is limited as a standalone unit.
- **#3, Andreas, 2024-11-14.**
  - He found no official discontinuation notice. AC/DC is gone from Rebel's product overview, and Schneiders Laden lists it as no longer available.
  - He wants to start with a 4-channel mixer/attenuator and later build a Reaktor-style "write/read buffer" (sampler/looper) without a computer.
  - He asks to confirm that he must choose by firmware flag between patch mode and interface mode, with no automatic detection.
- **#4, antisvin, 2024-11-14.**
  - Sampling could work. It would be controlled by triggers sent into the audio inputs, which arrive at audio rate rather than block rate.
  - He confirms: "Yes, exactly." Normally OWL sends audio input to USB and USB input to the patch. For this use the order must flip: audio input to the patch, patch output to USB, and the same inversion on the output side.
  - Switching automatically is "not ideal" because the patch would stop working whenever USB is plugged in. A switch would be better, but AC/DC has very few controls, so custom-patch users would likely run one dedicated patch.
- **#5, Andreas, 2024-11-14.** He knows some Pd, a little FAUST and general C/C++, but has no OWL patch experience. He could live with the patch stopping when USB is plugged in. His first hurdle is compiling and flashing firmware: he previously almost bricked the module.
- **#6, antisvin, 2024-11-14.**
  - **Pd:** compiled with the Heavy compiler, which is not 100% compliant and may need workarounds.
  - **FAUST:** well supported. To run FAUST patches on AC/DC you need his branch, because it has fixes that upstream OwlProgram lacks and upstream only works with an older FAUST version. FAUST should probably be the first choice.
  - **C++:** steep learning curve.
- **#7, Andreas, 2024-12-09.** He borrowed a Befaco Lich and will try there first, then report back. No later posts as of 2026-10-23.

### Inferences
- The thread gives no ready-made firmware binary and no step-by-step recipe. The concrete recipe is in thread #2110 (see section 2).

### Gaps
- Nobody (Befaco or Rebel Technology) officially confirmed or denied the discontinuation in the thread.

## 2. Does AC/DC run patches standalone, and how does USB affect the audio path?

### Takeaway
AC/DC runs OpenWare and boots the patch stored in its program slot (default slot 1) whether or not USB is connected. The patch keeps running from Eurorack power alone; the stock 4-channel VCA/meter patch already does this. In stock firmware the DAC outputs carry the USB playback stream instead of the patch output, so patch output is not what you hear. My reading of the code is narrower than the forum's description: the override only happens while a USB host is actively streaming audio to the device. With no host at all, the stored patch's output should reach the outputs, but only if the patch reads the physical inputs as expected (see the next paragraph). This is not tested on hardware.

There is a catch on the input side: by default, before the patch runs, its input buffer holds the codec ADC inputs. The official fix is to rebuild the firmware with `USE_USBD_AUDIO_RX_PRE_FX` and `USE_USBD_AUDIO_TX_PRE_FX`.

### Cited Findings
- **AC/DC config.** `ACDC/Core/Inc/hardware.h` (https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Inc/hardware.h):
  - Defines `USE_USBD_AUDIO`, `USE_USBD_AUDIO_TX` and `USE_USBD_AUDIO_RX`, but neither `*_PRE_FX` flag, so the routing defaults to POST_FX.
  - 4 audio channels, 48 kHz, 16-bit USB audio, block size 16.
  - `USE_QSPI_FLASH`, `NO_INTERNAL_FLASH`, `USE_DFU_BOOTLOADER`.
  - `NOF_ADC_VALUES 4` (the 4 knobs).
  - No UART MIDI, no USB host.
- **Routing code.** `Source/ProgramManager.cpp` lines ~263-317 (https://github.com/RebelTechnology/OpenWare/blob/master/Source/ProgramManager.cpp):
  - If PRE_FX is not defined, POST_FX is used.
  - With TX POST_FX, the patch output is converted into the USB TX stream (to the computer).
  - With RX POST_FX, the USB RX stream is written into the patch output buffer "overwriting patch output" (code comment) after the patch runs.
  - With PRE_FX, USB TX takes the raw inputs and USB RX is written into the patch input before the patch runs.
- **The override is conditional on active streaming.** In the same file, `usbd_rx_convert()` only writes data `if(rx)`, where the global `usbd_rx` starts as `NULL`.
  - It is set by `usbd_audio_rx_start_callback()`, which is only called from `USBD_AUDIO_DataOut` in `Source/usbd_audio.cpp`, i.e. when the host actually sends isochronous audio packets.
  - It is reset to `NULL` when the host selects alt setting 0 (stops the stream) or on USB DeInit/disconnect.
  - Sources: https://github.com/RebelTechnology/OpenWare/blob/master/Source/ProgramManager.cpp and https://github.com/RebelTechnology/OpenWare/blob/master/Source/usbd_audio.cpp
- **Boot behaviour.** `bootstrap()` in `Source/ProgramManager.cpp` loads and starts `settings.program_index` if that slot holds a patch, and otherwise enters configure mode. Then it starts the codec. It has no dependency on USB enumeration. `DEFAULT_PROGRAM` is 1 (`Source/device.h`). `program_index` is reset to `DEFAULT_PROGRAM` unless settings are stored in flash (`Source/ApplicationSettings.cpp`).
- **Forum confirmation of standalone operation (stock firmware).** antisvin, 2023-04-03/04, at https://community.rebeltech.org/t/ac-dc-firmware-update/2083 :
  - With a broken-USB official build, "it's not bricked - the default patch is running".
  - The preinstalled default patch "is like a 4 channel VCA". Feed CV into a channel with gain at max to see it running via the LEDs.
- **Forum statement of the override.** antisvin, 2023-06-11, at https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110 :
  - "USB audio output overrides patch output. This is the default behavior", and changing it requires a custom firmware.
  - This was in reply to AuroraPolnareff, whose FAUST/Pd patches produced no sound or voltage at the outputs.
- **The recipe.** antisvin, 2023-11-04, at https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110/5 :
  - Running patches on AC/DC is "not really supported officially".
  - You need a custom firmware with `#define USE_USBD_AUDIO_RX_PRE_FX` and `#define USE_USBD_AUDIO_TX_PRE_FX` added to the ACDC config.
  - You need local builds from his OwlProgram branch for FAUST: FAUST label parsing for AA... parameters is broken upstream, and newer FAUST needs fixes.
  - A debugger (ST-Link v3 mini) is highly recommended.
  - As an untested workaround with stock firmware, he suggests looping USB input to USB output on the PC.
- **Reference config with PRE_FX.** The `XibecaDevKit` target in the same repo already defines both PRE_FX flags, plus UART MIDI and a USB host (https://github.com/RebelTechnology/OpenWare/blob/master/XibecaDevKit/Core/Inc/hardware.h). It is a working template for the needed change.
- **Forum users want auto-switching.** On #2110 JZerbian (2023-11-11) wants interface mode when connected and the patch when not. Andreas (m9dfukc, 2024-01-08) called the current process too complicated. Source: https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110
- **USB power and VBUS.** AC/DC enables USB VBUS sensing on PA9 (`ACDC/Core/Src/main.c`, `hpcd_USB_OTG_FS.Init.vbus_sensing_enable = ENABLE`). The `feature/acdc` branch's last commits (2022-05-22) are "set self-powered" and "allow USBD_SELF_POWERED override" (https://github.com/RebelTechnology/OpenWare/tree/feature/acdc). Power comes from the Eurorack bus (+12V 200 mA, -12V 30 mA) per https://www.befaco.org/ac-dc/ , so USB power is not needed.

### Inferences
- **No host connected.** With stock firmware and no host, the DAC should output the stored patch's own output, because `usbd_rx` stays NULL.
  - Stock POST_FX routing already feeds the codec inputs into the patch. That is how the default VCA/meter patch processes the inputs.
  - So a custom patch stored in slot 1 might work as standalone FX without a firmware rebuild, as long as USB is unplugged (or the host is not streaming to OWL-ACDC).
  - This reading comes from the code only. It is not tested on hardware or confirmed by any forum post.
- **Why the #2110 user heard silence.** The user was probably connected to a computer (patches are loaded from the browser) that streamed silence to OWL-ACDC, e.g. because macOS had it selected as an output device. That would match antisvin's "USB overrides patch output" explanation.
- **When PRE_FX is required.** PRE_FX is only needed for the "patch runs while connected and the computer records or feeds the patch" mode. With PRE_FX, USB RX replaces the patch input while the host streams. When nothing is connected, the patch reads the physical inputs.
  - So a PRE_FX build gives roughly the behaviour the OP asked for: standalone FX when disconnected, raw inputs to the computer, and computer playback into the patch when connected.
  - It is not a pure audio-interface mode: the DAC always outputs the patch. A "Nichts" pass-through patch (`process = _,_,_,_;`) would make it act like a normal interface while connected.
- **What auto-switching would take.** An auto-switch could gate on `usbd_rx != NULL` (an active host stream) rather than on cable presence. That would be a small firmware change, but nobody has published one.

### Gaps
- No hardware test or forum report confirms that a stored custom patch is audible on stock firmware with USB fully unplugged.
- The source of antisvin's modified ACDC firmware is not public as a named branch. His OpenWare fork (https://github.com/antisvin/OpenWare) has expander and MIDI branches but no obvious ACDC/PRE_FX branch.
- The OpenWare GitHub API could not be queried from this environment; the public git clone worked.

## 3. How patches are stored and selected on AC/DC, and how to set a startup patch

### Takeaway
Patches are uploaded and stored over USB MIDI SysEx from the browser-based Rebel patch library or OpenWareLab tools, into slots in QSPI flash. On boot the firmware runs the stored `program_index`, which defaults to slot 1. AC/DC has no buttons, so there is no on-device patch switching. To set a startup patch, store it in slot 1, or store it and persist settings.

### Cited Findings
- Storage uses SysEx commands handled in `Source/MidiHandler.cpp`:
  - `handleFirmwareStoreCommand` stores an uploaded patch into a numbered slot.
  - `handleSettingsStoreCommand` calls `settings.saveToFlash`.
  - After a store, `programFlashTask` writes the resource, resets the program index and loads the stored slot.
  - Source: https://github.com/RebelTechnology/OpenWare/blob/master/Source/MidiHandler.cpp , https://github.com/RebelTechnology/OpenWare/blob/master/Source/ProgramManager.cpp
- `MAX_NUMBER_OF_PATCHES` defaults to 40 slots, plus 12 resources (`Source/device.h`). `DEFAULT_PROGRAM 1`.
- `updateProgramIndex()` stores the selected index in `settings.program_index`. It is saved to flash only via the settings-store command. Source: `Source/ProgramManager.cpp`, `Source/ApplicationSettings.cpp`
- Martin Klang ("mars") told a user to revert to normal "by selecting patch 1 from the device page" after loading a test patch, and asked them not to store it. So the device page of the patch library selects slots, and slot 1 holds the default patch. Source: https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072 (post #4, 2023-04-04)
- Xibeca (the AC/DC board) has no OWL MIDI bootloader, only ST's system DFU bootloader. Ways in:
  - "Reset to bootloader" on https://www.openwarelab.org/Tools/firmware.html
  - Shorting the "boot" pads while powering up
  - ST-Link v3
  - Source: antisvin, 2026-04-23, https://community.rebeltech.org/t/bricked-xibeca-dev-kit/3725 ; https://community.rebeltech.org/t/ac-dc-firmware-update/2083
- The official v22.5.0 ACDC.bin release broke USB, and a self-built binary with the correct Libraries worked. Some Libraries submodule versions break USB. Sources: antisvin 2023-04-03, https://community.rebeltech.org/t/ac-dc-firmware-update/2083 ; 2026-06-04, https://community.rebeltech.org/t/bricked-xibeca-dev-kit/3725
- **OpenOCD recipe** for an ST-Link flash: `openocd -f xibeca.cfg -c "program ACDC.bin verify reset exit"`, with a stlink + stm32h7x config. Source: https://community.rebeltech.org/t/ac-dc-firmware-update/2083 (post #15)
- Some Xibeca boards have USB audio that fails after some time. Source: antisvin 2026-06-04, https://community.rebeltech.org/t/bricked-xibeca-dev-kit/3725
- "How many patches can AC/DC hold and how to recall them" (Pauper, 2023-10-30) has no replies. Source: https://community.rebeltech.org/t/ac-dc-diferent-patches/2177

### Inferences
- **Practical standalone workflow:**
  1. Build the patch.
  2. Store it to slot 1 via the patch library device page, with the computer connected.
  3. Unplug USB.
  4. Power-cycle: the patch boots from flash.
- **No on-device patch switching.** The firmware supports `program_change_button`, but AC/DC has no buttons, so changing patches without a computer would need MIDI program changes. USB MIDI needs a host, and serial MIDI is not enabled.

### Gaps
- Whether the patch-library web UI's "store" also persists `program_index` for slots other than 1 is not verified.

## 4. Controls and I/O for FX use, and control without a computer

### Takeaway
AC/DC gives a patch 4 DC-coupled ins and 4 DC-coupled outs (±10 V), 4 knobs (parameters A-D) and 8 LEDs (4 input, 4 output) that patches can drive. It has no buttons, no gate inputs, no dedicated CV inputs and no MIDI without a host. Any modulation has to go through the audio/CV inputs, which leaves fewer channels for audio.

### Cited Findings
- **Hardware specs:** 4 audio/CV inputs and 4 outputs at ±10 V, gain pots from -inf to +12 dB, level and clip LEDs, USB-B, 6 HP, STM32H7 with 32 MB RAM, 16-bit/48 kHz. The manual describes it only as a USB interface; standalone/patch use is not documented. Sources: https://www.befaco.org/ac-dc/ ; manual https://www.befaco.org/docs/AC_DC/AC_DC_User_Manual.pdf (manual quotes 20 ms latency at 256-sample buffer)
- **Patch mapping:** knobs are parameters A-D, AA-AD set green LED level, values ≥ ~4000/4095 light the red LED, and buttons 1-4 set red LED state. Source: antisvin, https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110 (posts #2, #5)
- **Firmware mapping:** `onLoop` maps AA-AD to the input LEDs with red at ≥4000, and BA-BD to the output LEDs. `updateParameters` smooths ADC A-D into parameters 0-3. Source: `ACDC/Core/Src/ACDC.cpp` https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/ACDC.cpp
- **Knob caveat:** the knobs are listed as the input gain pots in the manual, yet read by the ADC as parameters A-D.
  - Inference: in patch mode they likely act both as analog input gain and as patch parameters. That is how the default VCA patch uses them.
  - Not verified against the schematic: https://www.befaco.org/docs/AC_DC/ACDC_V1_THT_Schematic.pdf
- **MIDI expander:** AC/DC has only a USB device port, plus an expander header with UART RX/TX and ground but no power. Serial MIDI is not initialised in the AC/DC firmware.
  - Befaco planned a 2 HP MIDI expander (2023-04). A prototype existed (2023-10) and was confirmed working with Oneiroi (2024-07), but it was a "very low priority project".
  - Source: https://community.rebeltech.org/t/ac-dc-midi-input/2077
  - By 2024-11 antisvin said Befaco "never released" it: https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244
- **Trigger control:** controlling a sampler by triggers on the audio inputs works at audio rate. Source: antisvin, #2244 post 4.
- **Review:** MusicRadar (2022-10-03) lists limited patching I/O as the main con and does not cover standalone use: https://www.musicradar.com/reviews/befaco-acdc

### Inferences
- **Feasible standalone FX patches:**
  - Stereo FX with 2 audio ins and 2 CV/trigger ins.
  - Quad mixer, VCA or attenuator.
  - 4-channel panner or FDN reverb, which antisvin ran in FAUST.
  - A trigger-controlled stereo buffer/looper.

### Gaps
- No YouTube demo or ModWiggler thread showing AC/DC as a standalone FX unit was found.
- The OWL docs site has no AC/DC device page; the device list stops at the Lich: https://www.openwarelab.org/

## 5. Other OWL devices, and workarounds

### Takeaway
Other OWL modules (Lich, Witch, Magus, Wizard) are designed as standalone patch hosts, and USB is an extra for them. AC/DC is configured as an interface first. The practical paths are:
1. Try the stock firmware with USB fully unplugged and a patch stored in slot 1. This needs no rebuild, but is unverified.
2. Rebuild the ACDC firmware with the two PRE_FX defines, using XibecaDevKit's hardware.h as a reference, and flash it via DFU.
3. Use a Lich instead, which is what the OP did.

### Cited Findings
- On Lich, USB audio is "a feature of firmware, so it's always available" with no special patch. A user noted that USB audio "breaks" the direct input-output connection, and shared a pass-through patch, "_Lich_Nichts". Source: https://community.rebeltech.org/t/simple-patch-for-using-lich-as-an-audio-interface/1911 ; patch https://www.rebeltech.org/patch-library/patch/_Lich_Nichts
- Befaco sold a passive USB breakout only with MIDI Thing v2. Source: antisvin 2024-07-22, https://community.rebeltech.org/t/ac-dc-midi-input/2077
- Upstream OpenWare has had no release since v22.5.0 (2023-03-05). Source: `git ls-remote --tags` on https://github.com/RebelTechnology/OpenWare
- antisvin expects no AC/DC updates from Rebel Technology. Source: #2244 post 2.

### Inferences
- Several suggested workarounds do not help with the "no computer" use case:
  - A USB power-only adapter or dummy host adds nothing, because AC/DC is bus-powered and the override only applies to an active audio stream.
  - A USB-host MIDI box (sending program changes to the USB device port) could switch patches or send CC without a computer. This is untested for AC/DC.
- The cleanest auto-switching firmware patch would choose routing at run time based on whether a host stream is active (`usbd_rx`/`usbd_tx` non-NULL), instead of the compile-time PRE/POST flags. Nobody has published such a fork.

### Gaps
- No Lich, Witch, Magus or Wizard hardware.h was compared in detail. The Lich source sits in the `Lich3`/`Lich` folders; `Lich/Core/Inc/hardware.h` was not found at that path.
