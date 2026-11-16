# Firmware update, DFU, SWD on AC/DC – forum re-read 2026-11-14

Sources (read via Discourse JSON): https://community.rebeltech.org/t/ac-dc-firmware-update/2083 (posts 1–39, post 29 missing from the API), https://community.rebeltech.org/t/bricked-xibeca-dev-kit/3725 (complete), https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244 (complete). Images were not viewed.

## Official v22.5.0 ACDC.bin vs. working USB

- 2083 #4, antisvin, 2023-04-03: he tested the official build and "noticed that it breaks USB". The default patch still runs.
- 2083 #5: he reported it to RebelTech/Befaco ("a correct update is expected soon") and attached his own build `ACDC.bin (101.9 KB)`, built "with correct libraries". The attachment is at community.rebeltech.org `/uploads/short-url/yFjVjZGdeNvnl5Mwja3zTovigzP.bin`. Not fetched.
- 2083 #30/#35, Bearwise: neither the official build nor antisvin's restored his module. #36 antisvin: he "can't doublecheck" that his build fixed USB, and suggests the older v22.5.rc4.
- 2083 #39, Bearwise, 2023-10-13: it worked only after he got a replacement board and "took the firmware from that". That firmware is not public.
- 3725 #4, antisvin, 2026-06-04: "some versions of Libraries submodule" broke USB. See also https://community.rebeltech.org/t/how-should-i-upgrade-genius-firmware-from-22-3-o-to-22-5-0/3473/7 (not fetched).
- No fixed RebelTech/Befaco build with a version label is mentioned anywhere.

**Implication for this project:** acdc1 reports "v22.5.0" **and** has working USB. So it is most likely *not* the GitHub `ACDC.bin`, which breaks USB according to antisvin. It is probably a factory or replacement-board build. That fits D2 (thru-mute, i.e. `237c63d` behaviour), blocksize 8 and the 186 ppm difference. Flashing the GitHub `ACDC.bin` is therefore **not** a safe reversible step: it may break USB, and the firmware currently on acdc1 is not available anywhere else.

## Standalone / thru

- No post says the outputs are silent without a computer. "audio thru" and "pass-through" do not appear.
- 2083 #4/#7/#23: the "default VCA patch" runs without a host. That means LEDs and processing work. Nobody confirms that audio reaches the output jacks.
- 2244 #2/#4, antisvin: the routing is a compile option. Normally the input goes to USB and USB goes to the patch, so for standalone you need the PRE_FX routing.

## DFU entry

- "Reset to bootloader" on https://www.openwarelab.org/Tools/firmware.html (3725 #2). This is SysEx `0x7E` → `device_dfu()` [Code].
- Boot pads on the Xibeca board: short them while the unit is unpowered, then power on (2083 #4/#7, 3725 #2).
- **Location (photo in https://community.rebeltech.org/t/ac-dc-firmware-update/2083/4):** a two-pad solder jumper labelled **BOOT** on the Xibeca Rev02 board, on the exposed side (the one with the big "REBEL TECHNOLOGY" print), left edge next to header pins 78/76. It sits directly **below a similar jumper labelled PDR** (do not short that one) and below the J1 SWD footprint. antisvin used a small screwdriver. 3725 #3 (kurt): it worked with the pads shorted at power-on. A permanent solder bridge (2083 #24/#26) would hold BOOT0 high, so the board would always start in DFU. This is unreliable for some people (2083 #22/#24/#25). Disconnect USB first, because the cable can keep the board powered (2083 #7).
- WebUSB DFU page: https://rebeltechnology.github.io/webdfu_owl/owl/ (3725 #3, "DFU in FS Mode").
- Which physical jack carries DFU (front USB-B or rear micro-USB) is **not stated**. The firmware uses only USB_OTG_FS PA11/PA12 (VBUS PA9) [Code, `ACDC/ACDC.ioc`].
- Micro-USB: 2083 #15, antisvin powered the Xibeca board "from its microUSB port" while flashing with the ST-Link.

## SWD / ST-Link

- Header "J1": 2×5 pads, 0.05" pitch, the SMT header must be soldered on (2083 #10/#12).
- The ST-Link cable has 14 pins and the board header 10. Plug it centered, leaving 2 pins free on each side. The red stripe goes on the side with the dot near the header (2083 #15). Upside down gives a target-voltage error, not damage (2083 #28).
- Disconnect the device USB while the programmer is attached, or there may be ground-loop problems (2083 #19).
- OpenOCD (2083 #15): `source [find interface/stlink.cfg]`, `transport select hla_swd`, `set WORKAREASIZE 0x1c000`, `source [find target/stm32h7x.cfg]`, `reset_config srst_only`. Flash: `openocd -f interface/stlink.cfg -f target/stm32h7x.cfg -c "program ACDC.bin 0x08000000 verify reset exit"` (#28).
- Backup: antisvin advises storing a firmware dump with OpenOCD first (2083 #38). No command given.

## burstMembrane

- `burstMembrane/OpenWare` and `burstMembrane/acdc-patches` have **no GitHub releases** and no prebuilt binary (API checked 2026-11-14). acdc-patches has no README. Files: `ACDC.h`, `BypassProcessor.hpp`, `DattorroReverb.hpp`, `DattorroStereoReverb.hpp`, `Delay.h`, `Dummypatch.hpp`, `FaustTapeDelay.dsp`, `Grain.hpp`, `GrainzPatch.hpp`, `Nonlinearity.hpp`, `RingsStereoReverbPatch.hpp`, `TapeDelay.dsp`, `TapeDelayPatch.hpp`. Using them means building firmware and patches ourselves.
