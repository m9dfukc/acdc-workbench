<!-- i18n source=docs/01-hardware-und-firmware.md sha256=09f71c55f21cbc9fd6a1d74bfaa310044a32f012051e370924116729452be630 date=2026-11-17 -->
> English translation of [`docs/01-hardware-und-firmware.md`](../../docs/01-hardware-und-firmware.md), as of 2026-11-17. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 01 – Hardware & firmware of the AC/DC

Basis: OpenWare source `RebelTechnology/OpenWare` @ `62a0187` (v22.5.0, 2023-03-05), build target `ACDC/` (platform "Xibeca"), plus forum statements.

**[code] statements apply to v22.5.0 unless stated otherwise.** My own builds on acdc1 are based on `db9d3dd` (v22.4.r, branch `hack/acdc-output-levels`) and differ in clocking, block size, gains and USB path. What applies there is in the section "My own firmware on acdc1" at the end and in `05-firmware-plan.md`.

## Hardware

| Aspect | Value | Status |
|---|---|---|
| MCU | STM32H750IB, 480 MHz, FreeRTOS. Build via `Hardware/xibeca.mk` with `-DSTM32H750xx`, linker script for 128 KB flash ("Xibeca red"). `ACDC.ioc` names STM32H743IIKx (prototype) | [code] |
| Flash budget | Release binary ≈ 107 KB of 128 KB, so only approx. **20 KB of headroom** for backports | [code] |
| Patch storage | QSPI flash, up to 40 slots. Boot patch = `settings.program_index`, default slot 1 | [code] |
| Codec | TI PCM3168A, SAI1 block A as master (generates MCLK), TDM 8 slots, 24 bit. 4 of them are used, but all 8 run via DMA | [code] |
| Codec HPF | off (`/* #define CODEC_HP_FILTER */`), deliberately for DC coupling. Can be enabled at runtime via SysEx `HP`, but is **not saved** | [code] |
| Sample rate | nominally 48 kHz. PLL3 98.2857 MHz, MCKDIV rounded to 8 → **≈ 47 991 Hz (−186 ppm)**. This applies to v22.5.0 and v22.4.q (acdc2). From v22.4.r in the hack branch (PLL3 P/Q 8, FRACN 262) it is exactly 48 kHz, this is how acdc1 runs | [code], [measured] lab notebook D10 |
| I/O | 4 inputs, 4 outputs, ±10 V, DC-coupled | [sourced] |
| Controls | 4 knobs (input gain **and** patch parameters A–D), 8 LEDs (parameters AA–AD, BA–BD). No buttons, no gate/CV input, no serial MIDI. The MIDI expander never appeared (thread #2077) | [sourced] |
| LEDs | PWM via TIM2/3/4/8, prescaler 100, period 1023 → **≈ 2.32 kHz** (in the audio band). The duty cycle follows the level | [code] |
| Power | Eurorack bus (+12 V, approx. 200 mA). Not powered via USB | [sourced] |
| Default gains | Input 104, output 114 (v22.5.0). In the hack branch (v22.4.q, v22.4.r): input 88. My own builds from 1c on: output 125 (patch 04). These are all defaults: settings stored in flash take precedence | [code] |
| Firmware acdc1 | Today **`v22.4.r-fx4b`** (my own build, since 2026-11-17, before that `v22.4.r-fx3l` since 2026-11-16). From the factory the module reported "v22.5.0", but it was a build from `hack/acdc-output-levels` with this label, not a published commit. Hence block size 8, the 6 kHz line and the clocking of v22.4.r | [measured] lab notebook D3, D3a, D10, D49, D59 |
| Firmware acdc2 | **v22.4.q** = commit `e81cfc3` (2022-06-27) from `hack/acdc-output-levels`, never merged. `AUDIO_BLOCK_SIZE 8` (v22.5.0: 16), `AUDIO_INPUT_GAIN 88`, HPF off, PLL/LED timers as in v22.5.0. Our code analysis otherwise refers to v22.5.0 | [code], device status 2026-11-13 |

## USB

| Aspect | Value | Status |
|---|---|---|
| Speed | **Full Speed** (`USE_USBD_FS`, OTG_FS with internal PHY, USB clock from HSI48, no CRS trimming configured) | [code] |
| Class | USB Audio Class **1.0** (`bcdADC 0x0100`) + USB MIDI | [code] |
| Format | 4×4 channels, **16 bit** (24 bits from the codec are truncated without dither), 48 kHz | [code] |
| Bandwidth | 4 × 48 000 × 2 B = 384 B per 1 ms frame and direction. Fits in Full Speed, an **ADuM3160 isolator is sufficient** | [code] |
| Sync | Playback async with explicit feedback (EP 0x81), format 10.14, every 32 ms (`FB_REFRESH 5`). Upstream up to v22.4.r: **open loop**, only the consumption of the codec is reported, not the buffer level | [code] |
| Buffer | `USBD_AUDIO_BUFFER_PACKETS 3` = 576 samples = 144 frames = 3 ms (RX). Start in v22.4.r: fill level after the first packet = half the buffer, so only ≈ 24 frames of margin until underflow | [code] |
| Feedback drift macOS | With an open loop macOS delivers on average ≈ 1 LSB too little (1.15–1.7 ppm). Every ≈ 2–3 min the RX buffer runs empty by one block (8 frames), audible as a click, and the loop latency grows by 8 samples. Fixed by buffer-level control (my own patch 06, build 1d) | [measured] lab notebook D12, D16, D18 |
| Debug messages | `usbd_audio_error()` → PROGRAM_MESSAGE `<msg> <rx free> <tx used> <diff>`: `rx unf` (underflow), `rx ovf`, `tx unf`, `tx ovf`; feedback: `fb <old> <new>` (discarded measurement). Only the last message is kept, readable via `tools/owl_read.py` | [code] |
| Interrupt priorities | SAI DMA (codec) 5, OTG_FS 6: the audio interrupt can preempt USB. This creates a race in `usbd_audio_get_rx_count()` (patch 05), which however was not the cause of the drift | [code] |
| Mute/volume | `Codec::mute()` and the USB mute/volume callbacks are TODO stubs with no function | [code] |

## Audio routing (important for standalone and filter)

Relevant file: `Source/ProgramManager.cpp`, function `onProgramReady()` (approx. lines 263–318).

```c
// pre / post fx routing
#if defined USE_USBD_AUDIO_RX and !defined USE_USBD_AUDIO_RX_PRE_FX
#define USE_USBD_AUDIO_RX_POST_FX
#endif
#if defined USE_USBD_AUDIO_TX and !defined USE_USBD_AUDIO_TX_PRE_FX
#define USE_USBD_AUDIO_TX_POST_FX
#endif
```

TX and RX routing can be switched **independently** of each other (checked in the source) [code].

- **Stock (both POST_FX):**
  - After the patch, the **patch output** is sent to USB TX, i.e. to the computer for recording.
  - Then USB RX (DAW playback) overwrites the DAC.
  - `usbd_rx_convert()` only does something while `usbd_rx != NULL`. That holds only from the first `DataOut` packet from the host. On alt setting 0 or disconnect it becomes `NULL` again.
  - **macOS sends playback packets even when an app only records from the AC/DC** (recording app, playback on another device) [measured, lab notebook D20, S3-c]. With build 1d the pass-through is then off, and the outputs carry the host playback (usually silence). So "only the input streams, the output passes through" does not exist on the Mac.
- **Without a host:** `bootstrap()` starts the patch from slot `program_index` and then the codec. There is no USB or VBUS dependency, the clock comes from the codec (8 MHz crystal) [code]. antisvin confirms that the default patch runs without USB (thread #2083) [sourced].
- **With my own firmware build 1d (acdc1), pass-through works without a computer [measured, lab notebook D11/D17].** The following item describes the old firmwares.
- **Old firmware: without computer playback nothing arrives at the jacks [measured, acdc1 cold start, see `messlog.md`].** So the patch runs but is not audible. On acdc2 (v22.4.q) this is explained by the hack `237c63d`, which writes zeros to the DAC without USB playback [code]. On acdc1 it was the same hack: the factory firmware was a hack-branch build with the label "v22.5.0", `237c63d` is proven in it by disassembly [measured, lab notebook D3/D3a].
- **Default patch "ACDC"** (Martin Klang, source in `owl-patches/library/`): 4-channel VCA, output = input × (knob·2)², LEDs = level/clip. So it passes the signal through [code].
- **Without a stored patch** the module stays in configure mode: output silent, no USB audio. The USB transfer runs in the per-block hook of the patch [code].

| Build | Without host | Host streaming |
|---|---|---|
| Stock (source v22.5.0) | Inputs → patch → DAC [code]. Never checked on hardware: both modules carried hack-branch builds with `237c63d`, where the DAC is mute [measured] | DAC = DAW playback, the computer gets the **patch output** |
| `TX_PRE_FX` + `RX_PRE_FX` (antisvin, burstMembrane fork) | Inputs → patch → DAC | The computer gets the raw inputs, DAW playback goes **into the patch** |
| **only `TX_PRE_FX`** | Inputs → patch → DAC | The computer gets the raw inputs, DAC = DAW playback ✅ **target behavior** |

- **Limitation of "only `TX_PRE_FX`" (build 2 `v22.4.r-fx1d`, likewise 3d and fx3l):** When an app records from the AC/DC, macOS also starts the playback stream [measured, D20]. Then the right column applies, and the host silence overwrites the patch output. So the FX is at the jacks only without a computer stream [code]. Accepted as is for build 2 (`docs/05`, "Build 2 neu").

Consequence for the noise: with stock routing (acdc2, build 1d) a **filter patch in slot 1 ends up directly in the USB recording**. With `TX_PRE_FX` (acdc1 from build 2 on) the computer records the raw inputs, a patch in the module no longer reaches the recording [measured, lab notebook D25, B2]. Filtering then happens in the computer. See `04-software-filter.md`.

## My own firmware on acdc1 (as of `v22.4.r-fx4b`, 2026-11-17)

Short version. Reasons and measurements are in `05-firmware-plan.md` and `messlog.md`.

| Aspect | Value | Status |
|---|---|---|
| Base | `db9d3dd` (v22.4.r) + libraries `9e8f64e` (old H7 HAL). Exactly 48 kHz, block size 8, input gain 88, 4 TDM slots, SAI OutputDrive off | [code], clock [measured] D10 |
| Pass-through | Without a computer stream the patch is at the outputs (revert of `237c63d`, patch 02) | [measured] D11, D17 |
| Routing | `TX_PRE_FX`: the computer gets the raw inputs. Product string "OWL-ACDC-FX" (patch 03) | [measured] D25 |
| USB feedback | Control based on the fill level of the RX buffer (patch 06): target 384 samples, P controller, ±32 LSB | [measured] D18: 30 min without block slips |
| SOF evaluation | `USBD_AUDIO_SOF` evaluates each frame number only once (patch 14). With USB code in ITCM the SOF chain otherwise ran twice in ≈ 97 % of the frames | [measured] D46, D47 |
| Block start | `audioCallback` is attached to the RX DMA callbacks instead of the TX DMA interrupt (patch 12b). Before, the last input sample of a block could be 16 frames old | [measured] D40, D43 |
| Input LEDs | With a TX stream raw level (mean square × 4096, τ 40 ms), red for 300 ms from −0.1 dBFS. Measured every 2 ms in `onLoop` on the codec DMA buffer (patch 07d) | [measured] D34, D36 |
| Memory | Hot path (104 functions, 12 392 B) and vector table in ITCM from 0x3000 (patch 11g). Patch heap in CCM 39.2 KB instead of 52 KB | [code: `check_itcm.py`], [measured] D47–D49, D50 |
| Patch selection | Boot menu (patch 15b): power on with knobs 1, 2, 3 at the left stop and knob 4 at the right stop. Knob 1 selects among the occupied slots 1–15, knob 4 confirms, knob 3 or 30 s cancel. The input LEDs show the slot in binary. The slot is remembered as the resource `ACDC.slot` in the patch flash and starts at the next power-on. The settings stay untouched | [measured] D52, D53, D55, D57, D58 |
| ADC format | SAI1 delivers 24 bits right-aligned **without sign extension** (`SAI_DATASIZE_24`). Sign-extend before any level calculation | [code], noticed in D28 |
| Input range | Full scale ≈ ±9.5 V, offset ≈ −0.2…−0.4 V per channel | [measured] D29 (indirect), D36 |
