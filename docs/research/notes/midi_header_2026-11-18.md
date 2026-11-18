# Rear "MIDI" header: serial MIDI, I2C and USB host on the AC/DC (2026-11-18)

Question (user): can MIDI controllers (pad and knob controllers with USB and partly with MIDI jacks) control patch parameters in standalone/FX mode? First idea: plug them into the front USB-B port. Second idea: use the 3-pin header labelled "MIDI" on the back, together with a passive 2 HP MIDI jack breakout that the user already owns (Expert Sleepers "Tiny MIDI breakout", made for the ES-9 and its siblings).

Method: Befaco schematic (PDF, rendered at 600 dpi and read), forum thread #2077, manual and product pages of the breakout's manufacturer, OpenWare source at the fork tip `27d3630b` (`acdc/fx1d`). No device access, no build, nothing measured.

## Summary

- **USB host on the front port: not with the current firmware, and not worth it.** The port is `Device_Only` [Code], the socket supplies no 5 V, there is only one USB peripheral wired, and the host stack would eat most of the remaining flash.
- **The rear header is a raw 3.3 V UART without supply [belegt: schematic].** Pin 1 = `SDA_RX`, pin 2 = GND, pin 3 = `SCL_TX`, wired straight to the Xibeca module.
- **The firmware does not run serial MIDI on the AC/DC [Code, belegt: #2077].** A UART is initialised at 115200 baud but not connected to the MIDI code. A firmware patch is needed.
- **A small adapter board (optocoupler stage, 3.3 V regulator) between header and passive breakout is enough on the hardware side.** All parts are through-hole. Circuit below.
- **The same header is electrically suited for I2C** (section 6): the nets are named for both uses. A follower on the monome "ii" bus is possible with a firmware patch, but pin order and bus voltage do not match the ii bus as is. Audio I/O cannot be added this way.
- **Open:** which MCU pin is behind header pin 1 (PB5 or PB7), see "Open points".

## 1. USB host on the front USB-B port

- `ACDC/ACDC.ioc`: `USB_OTG_FS.VirtualMode=Device_Only`, PA11/PA12 = DM/DP, PA9 = `USB_OTG_FS_VBUS` (sense input) [Code].
- `ACDC/Makefile` pulls `C_SRC_USBD` and `C_SRC_USBD_AUDIO` only. No `C_SRC_USBH`, no `USE_USB_HOST` in `ACDC/Core/Inc/hardware.h` [Code].
- OpenWare has USB host MIDI (`USE_USB_HOST`, `USE_USBH_MIDI`), but only on boards with a separate host port: Witch, Magus, Wizard, Noctua, Mussol, PlayerF7 (`hardware.h` of each). XibecaDevKit defines `USE_USBH_HS` and builds `C_SRC_USBH`, `C_SRC_USBH_MIDI` [Code].
- The Xibeca module has a second USB port: the schematic symbol lists `USBH_VBUS`, `USBH_DM`, `USBH_DP`, `USBH_ID` on pins 94/92/90/88. **On the AC/DC these pins are not connected** [belegt: schematic].
- A USB-B socket has no ID pin and the AC/DC does not drive VBUS. Bus-powered controllers would need 5 V from outside (adapter B → A socket plus a powered hub).
- One port only: host mode would exclude the audio interface, `owl_read.py` and `owl_write.py`. The choice would have to be made at power-on.
- Flash: fx4b is 108 496 B of 131 072 B, so ≈ 22.5 KB free. Size of the host stack: not built, estimate 15–25 KB [Hypothese].
- A host sends a start-of-frame every millisecond. The comb at the output would probably return, as with any USB connection (D20) [Hypothese].

What works today: the firmware maps MIDI CC from the USB host to patch parameters (`Source/MidiHandler.cpp`, `handleControlChange`) [Code].
- CC 20–23 = A–D, CC 24 = E, CC 1 = F, CC 12 = G, CC 13 = H, CC 75–106 = AA–DH (`Source/OpenWareMidiControl.h`).
- A–D are overwritten every block by the knobs (`ACDC/Core/Src/ACDC.cpp`, `updateParameters`). AA–AD drive the input LEDs, BA–BD are written by the firmware with the output levels (`onLoop`). So MIDI can usefully control E–H and the extended parameters from AE on.

Ways without host mode and without firmware change:
- CV: controller with MIDI jacks → MIDI-to-CV module → AC/DC input (DC-coupled), the patch reads the channel as a parameter. Costs one input per parameter.
- A small USB MIDI host box between controller and AC/DC. Pass-through stays on while nobody opens the audio stream, but the comb at the output is back (D20).

## 2. The rear header

Source: https://www.befaco.org/docs/AC_DC/ACDC_V1_THT_Schematic.pdf (EAGLE 9.6.2, created 2022-09-16, one page). The PDF text is not extractable with a plain fetch, it has to be rendered.

- 3-pin header, labelled "MIDI": **pin 1 = `SDA_RX`, pin 2 = GND, pin 3 = `SCL_TX`** [belegt].
- `SCL_TX` goes to Xibeca module pin 73 (symbol name `I2C_SCL`), `SDA_RX` to module pin 74 (`I2C_SDA`). No series resistor, no pull-up, no protection, no level shifter in between [belegt].
- No supply on the header. The module has `+3.3V` (module pin 1) and `+5V` (module pin 95) on other board connectors (`3.3v` on JP6 pin 1, `+5V` on JP3). Tapping them is possible but they feed the pots and the analog side, so not recommended.
- The module's `USART2_TX/RX` (pins 83/81) and `USART3_TX/RX` (pins 84/82) are not connected on the AC/DC [belegt].

Forum thread #2077, https://community.rebeltech.org/t/ac-dc-midi-input/2077 (16 posts, 2023-03-30 to 2024-07-22):
- #2 antisvin 2023-03-31: the AC/DC "only has an USB device port", there is "an extra header on it that might be used for serial MIDI IO if there would be some sort of expander made".
- #6 antisvin 2023-04-11: "the expander header on OWL board is providing ground and UART RX/TX connections, but no power". "serial MIDI is not enabled in firmware for devices don't have it, so we'll have to wait for a new release that adds code to initialize UART. But it's not hard to hack a custom firmware version that adds it."
- #10 antisvin 2023-09-02: "ACDC only exposes its UART port". "Serial MIDI is not initialized in current ACDC firmware, but likely would be in the next firmware release along with official MIDI expander."
- #5/#7 Befaco 2023-04: will draw "a simple solution", 2 HP possible in SMD. #8: TRS jacks with jumpers for type A/B. #12 antisvin 2023-10-28: prototype exists, "fairly simple, but SMD soldering is necessary (0603 size)". #14 2023-12-07: also meant for Lich, works after "a few minor mistakes on PCB". #16 2024-07-22: confirmed with Oneiroi, "a very low priority project for them".
- The thread names no UART number, no MCU pin, no voltage. No released firmware enables serial MIDI on the AC/DC.

## 3. Firmware state (fork tip `27d3630b`)

- `ACDC/ACDC.ioc`: `PB5 = UART5_RX`, `PB6 = UART5_TX`, `PB7 = I2C1_SDA`, `PA8 = UART7_RX`, `PF7 = UART7_TX`. IPs: UART5, UART7, no I2C1 [Code].
- `ACDC/Core/Src/main.c`: `MX_UART5_Init()` and `MX_UART7_Init()` are called, both 115200 8N1. PB7 is set to `GPIO_MODE_AF_OD`, `GPIO_AF4_I2C1`, no pull [Code]. So with fx4b the TX line (PB6) should idle at 3.3 V.
- `ACDC/Core/Inc/hardware.h`: no `USE_UART_MIDI_RX`, no `USE_UART_MIDI_TX`, no `UART_MIDI_HANDLE`. `C_SRC_UART` is already in the Makefile [Code].
- Template: `XibecaDevKit/Core/Inc/hardware.h` defines `USE_UART_MIDI_RX`, `USE_UART_MIDI_TX`, `UART_MIDI_HANDLE huart7`, `UART_MIDI_RX_BUFFER_SIZE 256`. Its `.ioc` sets UART7 to 31250 baud with DMA for RX and TX [Code].
- `Source/uart.cpp`: RX runs over DMA (`__HAL_DMA_GET_COUNTER(huart->hdmarx)`), bytes go to `uart_rx_callback` in `Source/MidiReceiver.cpp`. The AC/DC build has no DMA stream for UART5 or UART7 [Code].

A firmware patch therefore needs: 31250 baud, the three defines with the right UART handle, a DMA stream plus interrupt handlers for RX (and TX if wanted), and the usual acceptance (check_itcm, loop test, noise A/B against fx4b).

## 4. The passive breakout and its host

ES-9 manual (section "5-pin DIN MIDI I/O"), https://analoguehaven.com/expert-sleepers/es-9/manual.pdf :
- "The MIDI ports are exposed on a 4-pin expansion header (labelled GT2) on the rear of the module. All of the necessary electronics are on the PCB; all that needs to be added is the actual sockets."
- Header: pin 1 = OUT pin 4, pin 2 = OUT pin 5, pin 3 = IN pin 5, pin 4 = IN pin 4. "Pin numbers refer to the 5-pin DIN socket as in the MIDI standard."
- It uses the 3.3 V "Low-Voltage Signaling" variant of the MIDI electrical specification.

2 HP TRS breakout, https://expert-sleepers.co.uk/tinymidibreakout.html :
- "The module is entirely passive." Current draw: none. 2 HP, 30 mm deep.
- Upper socket = MIDI input, the one below = MIDI output (with a type A cable).
- Each jack has a 3-way header: "the jack socket tip is the right pin on the 3-way header, the ring is the centre pin, and the shield is the left pin."
- "For type A output, connect pins 1 & 2 from the attached module to the ring and tip pins respectively. For type A input, connect pins 3 & 4 from the attached module to the tip and ring pins respectively. For type B, swap ring and tip."

So for type A: tip = DIN pin 5 (data), ring = DIN pin 4 (source). The older DIN breakout (https://expert-sleepers.co.uk/dm4midibreakout.html) connects to the same hosts. Its page does not say whether it is passive, the host manual implies it.

MIDI electrical specification: https://www.midi.org/specifications/item/midi-din-electrical-specification

## 5. Adapter board (sketch, not built)

It rebuilds what the ES-9 has on its PCB. All parts through-hole, fits on stripboard. Draws less than 15 mA from +12 V.

MIDI in, galvanically isolated:

```
IN jack                             H11L1 (DIP-6)
ring (DIN 4) ──[R1 220Ω]──┬──────── 1 anode     6 Vcc ───┬── +3V3
                          │                              │
                     D1 1N4148                        [R2 1k]
                  (cathode at pin 1)                     │
                          │                     4 out ───┴──[R3 100Ω]── AC/DC pin 1 (RX)
tip  (DIN 5) ─────────────┴──────── 2 cathode   5 GND ───── GND
shield: leave open                  3 n.c.
                                    C1 100 nF directly between pin 6 and pin 5
```

Supply from the Eurorack bus (own power header on the board):

```
+12V ──[D2 1N4148]──[R4 47Ω]──┬── IN  78L33  OUT ──┬──────┬── +3V3
                          C2 10µF      GND     C3 100nF  C4 10µF
GND ──────────────────────────┴─────────┴──────────┴──────┴── GND ── AC/DC pin 2
```

MIDI out, optional, 3.3 V variant of the specification:

```
+3V3 ──[R5 33Ω]───────────────────────────── ring   (DIN 4)  OUT jack
AC/DC pin 3 (TX) ──[inv]──[inv]──[R6 10Ω]─── tip    (DIN 5)
GND ──────────────────────────────────────── shield
```

- Two inverters of a 74HC14 (pin 14 to +3V3, pin 7 to GND, 1→2, 3→4, unused inputs 5, 9, 11, 13 to GND, 100 nF at the supply). The buffer protects the MCU pin: a TRS plug shorts tip and ring for a moment when it is inserted.
- H11L1: Schmitt-trigger optocoupler, specified from 3 V supply, open-collector output. Current through the LED = output low = UART start bit, so no inversion is needed. Alternative 6N138 (other pinout, extra resistor).
- 78L33 in TO-92. Alternative LP2950-3.3 (other pinout, check capacitors in the datasheet).
- Parts: H11L1, 78L33, 2 × 1N4148, 220 Ω, 1 kΩ, 100 Ω, 47 Ω, 2 × 100 nF, 2 × 10 µF, 2×5 Eurorack power header, pin headers 1×3 (to the AC/DC) and 2 × 1×3 (to the breakout). For the output: 74HC14, 33 Ω, 10 Ω, 100 nF.

## 6. I2C on the same header (follow-up question, same day)

Question (user): is the header suitable for I2C, e.g. to control the AC/DC from a monome crow, or to add inputs and outputs?

AC/DC side:
- The header nets are `SDA_RX` and `SCL_TX`, on module pins named `I2C_SDA` and `I2C_SCL` [belegt: schematic]. The lines are meant for either use.
- `ACDC/Core/Src/main.c` already sets PB7 to `GPIO_AF4_I2C1`, open drain. PB6 is `UART5_TX` today and would be `I2C1_SCL` (AF4). `ACDC/Makefile` builds `C_SRC_I2C` (`stm32h7xx_hal_i2c.c`, `_ex.c`). No `hi2c` handle, no `MX_I2C1_Init` in the AC/DC build [Code].
- OpenWare has no code for an I2C bus between modules. I2C appears only as a codec control port (`Source/wm8731.c`, master) and in a sensor driver [Code].
- No pull-ups and no protection on the header [belegt: schematic].
- PB6 is shared: serial MIDI and I2C exclude each other. The choice is made at build time or at power-on.

monome ii bus (https://monome.org/docs/modular/ii, https://monome.org/docs/modular/iiheader):
- Three lines. "On all monome and Whimsical Raps modules, and the TELEX expanders... the pins are in this order: gnd, scl, sda." Other makers may differ, "modules might crash" if wired wrong. **The AC/DC header is SDA, GND, SCL**, so a straight 3-pin cable is wrong.
- Pull-ups: "pulled high' via pull-up resistors to 5V". Leaders usually have them, followers not. Resistor values and bus speed in kHz are not stated.
- Whether PB6/PB7 tolerate 5 V has to be checked in the STM32H750 datasheet (FT pins). If not, a level shifter is needed (per line one 2N7000 and two pull-ups, through-hole).

crow (https://monome.org/docs/crow/reference/):
- Leader for most ii devices: `ii.<device>.<command>(…)`. Pull-ups: "These are on by default and should probably stay on", switchable with `ii.pullup( state )`. `ii.fastmode( state )` for "about 4x" speed, default off.
- Arbitrary bytes: `ii.raw(addr, bytes [, rx_len])`, answers arrive in `ii.event_raw`. So the AC/DC only has to be a follower.
- A grid does not appear on the ii pages. It is a USB device and needs a host.

Protocol (https://github.com/scanner-darkly/teletype/wiki/II-protocol):
- "`[address byte] [command byte] [data bytes (optional)]`", 7-bit address, commands 0xC0–0xFF reserved. Voltages: −16384…16384 = −10…10 V.
- TELEXo: address 0x60–0x67, set CV = `0x11 I H L` (I = output 0–3, signed 16 bit). ER-301: address 0x31–0x33, same layout. A follower that takes this format also works with the Teletype ops.

What a firmware patch would need: I2C1 as follower (HAL listen mode, interrupt driven), an address, a mapping of commands to patch parameters (E–H and the extended ones) and maybe buttons. Event driven, so no polling in the block clock (D42). Still: check_itcm, loop test and noise A/B against fx4b.

Expanding I/O:
- Control rate: possible if the AC/DC leads the bus and queries e.g. a TELEXi (4 knobs, 4 CV inputs) or drives an I2C DAC. Regular queries are periodic work in the module, the kind that has produced lines before (D42). Needs a noise A/B.
- Audio: no. I2C is far too slow. The codec has 6 inputs and 8 outputs and the module symbol carries `AIN5/6` and `AOUT5–8`, but on the AC/DC board these nets apparently go nowhere [Hypothese: each name appears only twice in the PDF text, the used channels three to four times].

## Open points

- **Which MCU pin is behind header pin 1?** [Hypothese] The firmware sets up UART5 with RX on PB5 and TX on PB6. The module pin is named `I2C_SDA`, which matches PB7 (I2C1_SDA), not PB5. PB6/PB7 would also be USART1 TX/RX (AF7). Either the module ties PB5 and PB7 together, or RX needs USART1 instead of UART5. No Xibeca pinout was found. Test: a firmware build with UART MIDI and a wire from header pin 3 to pin 1 (loopback). For I2C the pin has to be PB7, and the I2C setting of PB7 in the code speaks for that.
- Check with a multimeter (no risk, fx4b): header pin 3 against pin 2 should read ≈ 3.3 V (TX idle) [Code]. That confirms TX and the orientation of the header.
- Type A or B on the controller's MIDI jacks: check its manual. Controllers with USB only cannot be used this way.
- Noise: UART and DMA activity is new periodic work for the MCU. A/B against fx4b is mandatory (D33, D42).
