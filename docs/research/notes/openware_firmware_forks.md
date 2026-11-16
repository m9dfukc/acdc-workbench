# OpenWare firmware and forks: Rebel Technology / Befaco AC/DC support (as of 2026-10-23)

Method: cloned https://github.com/RebelTechnology/OpenWare (blob:none) plus the `pingdynasty/OpenWare` and `antisvin/OpenWare` forks, the `pingdynasty/OpenWareLibraries` submodule (commit e102c6f, pinned by master), and `RebelTechnology/OwlProgram`. I read the code and did not build it. **Limitation:** the GitHub REST API (gh api, issues, PR metadata, fork list) and github.com HTML pages (robots) were blocked in this session. Fork discovery was therefore limited to `git ls-remote` probes of known or likely fork owners. PRs were inspected through `refs/pull/*/head` refs only, so their titles and open/closed state are unknown. File-path URLs below have the form `https://github.com/RebelTechnology/OpenWare/blob/master/<path>`, and commit URLs have the form `https://github.com/RebelTechnology/OpenWare/commit/<hash>`.

## 1. How AC/DC is supported in OpenWare (target, MCU, codec, USB, audio format)

### Takeaway
AC/DC is the `ACDC/` project, built on the Xibeca platform: an STM32H750 at 480 MHz running FreeRTOS, with a TI PCM3168A codec over SAI1 in TDM. The codec runs at 48 kHz and 24 bits internally. USB is a **Full-Speed** device using **USB Audio Class 1.0** with 4 in and 4 out at 16 bit/48 kHz, an asynchronous OUT endpoint with explicit feedback, and USB-MIDI. The default audio block size is 16 samples.

### Cited Findings
- Project directory `ACDC/` (ACDC.ioc, Makefile, Core/Inc, Core/Src). It was added 2021-11-04 in commit eb3371142b6cfde8087a2e9a63aa080b9984c02e ("adding ACDC project"). In commit 1e6f11bdb47b23d2e6271e715ec51f261d432ef9 (2022-03-17, "identify as AC/DC and reduce default blocksize") it was renamed to identify as AC/DC — [ACDC/](https://github.com/RebelTechnology/OpenWare/tree/master/ACDC)
- `ACDC/Makefile` includes `Hardware/xibeca.mk`, `Source/pcm3168a.c`, `sdram-as4cXm32.c` and `flash-qspi.c`, plus the SAI, SDRAM, DSP, OS, UART, I2C, QSPI, MDMA, USBD and USBD_AUDIO sources. The top-level `Makefile` target is `acdc`. — [ACDC/Makefile](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Makefile)
- `Hardware/xibeca.mk`: `-DSTM32H750xx`, `-mcpu=cortex-m7 -mfpu=fpv5-d16`, Release build `-O3` — [Hardware/xibeca.mk](https://github.com/RebelTechnology/OpenWare/blob/master/Hardware/xibeca.mk)
- Key defines in `ACDC/Core/Inc/hardware.h` (master): `HARDWARE_VERSION "AC/DC"`, `USBD_PRODUCT_STRING_FSHS "OWL-ACDC"`, `ARM_CYCLES_PER_SAMPLE (480000000/AUDIO_SAMPLINGRATE)`, `USE_QSPI_FLASH`, `NO_INTERNAL_FLASH`, `USE_DFU_BOOTLOADER`, `AUDIO_INPUT_GAIN 104`, `AUDIO_OUTPUT_GAIN 114`, `USE_PCM3168A`, `CODEC_ADC_INVERT`, `CODEC_DAC_INVERT`, `/* #define CODEC_HP_FILTER */` (commented out), `CODEC_SPI hspi2`, `CODEC_BLOCKSIZE 256`, `AUDIO_BLOCK_SIZE 16`, `AUDIO_BITS_PER_SAMPLE 16`, `AUDIO_CHANNELS 4`, `USE_USBD_AUDIO`, `USE_USBD_AUDIO_FEATURES`, `USE_USBD_AUDIO_TX`, `USE_USBD_AUDIO_RX`, `USE_USBD_RX_FB`, `USE_USBD_FS`, `USBD_AUDIO_BUFFER_PACKETS 3`, `AUDIO_SAMPLINGRATE 48000`, 4 ADC (CV) values, 40 parameters — [ACDC/Core/Inc/hardware.h](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Inc/hardware.h)
- USB peripheral: `USB_OTG_FS`, `PCD_SPEED_FULL`, embedded PHY, `Sof_enable = DISABLE`, `vbus_sensing_enable = ENABLE`, `battery_charging_enable = ENABLE` (`MX_USB_OTG_FS_PCD_Init`, around line 961). The USB clock is `RCC_USBCLKSOURCE_HSI48` (stm32h7xx_hal_msp.c line 820), and no CRS (clock recovery) configuration was found anywhere in ACDC/ or Source/. — [ACDC/Core/Src/main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c), [ACDC/Core/Src/stm32h7xx_hal_msp.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/stm32h7xx_hal_msp.c)
- `USE_USBD_FS` automatically enables `USE_USBD_MIDI` (Source/device.h lines 221-227). USB RX/TX channels default to `AUDIO_CHANNELS` (4), and the USB rates default to `AUDIO_SAMPLINGRATE`. — [Source/device.h](https://github.com/RebelTechnology/OpenWare/blob/master/Source/device.h)
- UAC version: the descriptor has `bcdADC` 0x0100, commented "compliant to the USB Audio specification version 1.00" (usbd_audio.cpp lines 291-292). The streaming OUT endpoint is `USBD_EP_ATTR_ISOC_ASYNC` with `bSynchAddress = AUDIO_FB_EP (0x81)`. The feedback endpoint uses a 3-byte 10.14 format, with `FB_REFRESH 5` (every 32 SOFs) — [Source/usbd_audio.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/usbd_audio.cpp)
- Feedback is computed in `USBD_AUDIO_SOF()` from `usbd_audio_get_rx_count()`, which measures the codec's DMA sample counter (`codec.getSampleCounter()`, from the SAI TX DMA NDTR). The value is only accepted within ±1 sample of 48.0 (`0x0c0000 ± 0x4000`). In other words, the **codec clock is the master** and the host is told to adapt. — [Source/usbd_audio.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/usbd_audio.cpp) lines 1363-1390; [Source/ProgramManager.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/ProgramManager.cpp) lines 38-45
- SAI1: Block A = `SAI_MODEMASTER_RX` (generates MCLK, SCK and FS, PG7 = SAI1_MCLK_A), Block B = `SAI_MODESLAVE_TX`, synchronous. Both use FREE protocol, 24-bit data, 8 slots × 32 bit, FrameLength 256, `SlotActive 0x0000FFFF` (all slots), `AudioFrequency SAI_AUDIO_FREQUENCY_48K`, `NoDivider = SAI_MASTERDIVIDER_ENABLE`, `OutputDrive ENABLE` — [ACDC/Core/Src/main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c) lines 465-525
- Clocks (master): HSE 8 MHz (`HSE_VALUE 8000000`). PLL1 M=1 N=120 P=2 gives SYSCLK 480 MHz, with `AHBCLKDivider = RCC_HCLK_DIV2`. SAI1 is clocked from PLL3 with M=7 N=172 P=2 FRACN=0, i.e. 98.2857 MHz (ACDC.ioc `RCC.SAI1Freq_Value=98285714.2857143`). — [ACDC/Core/Src/main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c) lines 246-317, [ACDC/ACDC.ioc](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/ACDC.ioc)
- HAL MCKDIV formula with NODIV=0 is `MCKDIV = SAI_CK / (FS*256)`, rounded only if the remainder is >0.8 — [OpenWareLibraries stm32h7xx_hal_sai.c @ e102c6f](https://github.com/pingdynasty/OpenWareLibraries/blob/e102c6f6c8525305fbf7de29f9b72a13088e34c2/Drivers/STM32H7xx_HAL_Driver/Src/stm32h7xx_hal_sai.c) lines 612-655
- PCM3168A init (`Source/pcm3168a.c`), register writes via SPI2:
  - reg 64 = 0b11000001: normal operation, single rate
  - reg 65 = 0b00000110: DAC "Power Save Enable", slave, 24-bit I2S TDM
  - reg 66 = 0b11000000: DAC channels 5-8 disabled for 4ch
  - reg 67 = 0xff: DAC phase invert
  - reg 70 = ATMDDA
  - reg 80 = single rate; reg 81 = ADC slave, 24-bit I2S TDM
  - reg 82: ADC 5/6 disabled, and **HPF disabled on all ADC channels** unless `CODEC_HP_FILTER` is defined
  - reg 83 = 0b00111111: single-ended inputs
  - reg 84 = ADC phase invert; reg 87 = ATMDAD
  - DAC soft mute (reg 68) is *not* set at init (that line is commented out)
  - The codec's own reset (`codec_reset`) is an empty stub
  
  Last changes: 7100726f42f99977558ed90cdb19f3bef42e5c7d (2022-06-11, "Added codec_highpass() function") and cefc8f9 (2022-06-12). — [Source/pcm3168a.c](https://github.com/RebelTechnology/OpenWare/blob/master/Source/pcm3168a.c)
- Input gain is written to reg 88 as `level+128` ("127 = +20dB … 0.5dB steps"). Output gain is written to reg 71 as `level+128` ("127 = 0dB"). The defaults come from `AUDIO_INPUT_GAIN` and `AUDIO_OUTPUT_GAIN` via `settings` — [Source/pcm3168a.c](https://github.com/RebelTechnology/OpenWare/blob/master/Source/pcm3168a.c), [Source/ApplicationSettings.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/ApplicationSettings.cpp) lines 23-24
- Audio interrupt: for the PCM3168A, `HAL_SAI_TxHalfCpltCallback` and `TxCpltCallback` call `audioCallback()` every `codec_blocksize` frames. Block size is `clamp(settings.audio_blocksize, 4, CODEC_BLOCKSIZE=256)` — [Source/Codec.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/Codec.cpp) lines 52-62, 228-245
- Product specs from retail: 4×4 DC-coupled at ±10 V, 48 kHz/16-bit, class compliant, USB-B, 200 mA +12 V / 30 mA -12 V, 6 HP — [Perfect Circuit](https://www.perfectcircuit.com/befaco-ac-dc.html). Synthtopia gives the same 48 kHz/16-bit, names Befaco with Rebel Technology on the "Xibeca" platform, and dates the announcement to Superbooth on 2022-05-12 — [Synthtopia](https://synthtopia.com/?p=129661)

### Inferences
- With `NoDivider` enabled, MCKDIV = 98.2857 MHz / (48000·256) ≈ 7.99, which rounds to 8. That gives MCLK ≈ 12.2857 MHz and **fs ≈ 47,991 Hz** (−186 ppm from 48 kHz), which matches the ioc value. My calculation, using the HAL formula cited above. The async feedback absorbs this for USB playback, but the device's "48 kHz" is actually slightly low. Upstream also produced the "acdc-lowspeed" retune for this reason (see §3).
- 16-bit USB samples are converted with `>>8` and `<<8` against 24-bit codec words (`AUDIO_INT32_TO_SAMPLE`). This means USB audio is truncated to 16 bits (no dither), which can add quantisation noise at low levels.

### Gaps
- The exact hardware revision (BOM, analog front-end, op-amps) is not in this repo.
- The Befaco or Rebel AC/DC manual was not retrieved.

## 2. Latest upstream activity, releases, and anything AC/DC-related

### Takeaway
Upstream `master` and `develop` have been frozen since **v22.5.0, 2023-03-05** (commit 62a0187797d81f01b5895e69814b7368f99cf69b). AC/DC firmware has not changed on master since mid-2022. The only later upstream activity is on non-AC/DC branches: `feature/witch3` (2023-10-10) and `feature/oneiroi` (2025-06-11).

### Cited Findings
- `master` = `develop` = 62a0187 "v22.5.0", 2023-03-05 22:48 +0100, by pingdynasty (Martin Klang). The last tags are v22.5.0, v22.5.rc4, v22.5.rc2 and v22.5.rc1 — [commit 62a0187](https://github.com/RebelTechnology/OpenWare/commit/62a0187797d81f01b5895e69814b7368f99cf69b)
- The v22.5.0 HISTORY includes "Improved USBD Audio host synchronisation", USBH fixes and a settings-save fix. Nothing in it is specific to AC/DC. 22.2.2 notes "Support for AC/DC and XibecaDevKit subprojects" and "Configurable audio block size". — [HISTORY.md](https://github.com/RebelTechnology/OpenWare/blob/master/HISTORY.md)
- An ACDC release build target was added in ed313997b63289dbb19237160635b9cbc6d18fcb (2023-01-04, Tools/makeprojects.py). The release v22.5.0 ships `ACDC.bin` (107 KB, asset dated 2023-03-05), and it is the only release with an ACDC asset. Release notes for v22.0.0 had the known issue "USB Audio might 'click' due to synchronisation with host". v22.1.rc1 notes "Fix USBD audio sync issues" and "descriptor issues (Windows)". — [pingdynasty/OpenWare releases](https://github.com/pingdynasty/OpenWare/releases)
- Since v22.4.0, the USB audio changes that reached master are: f842464 (2022-06-11, "Update RX feedback and use first DataIn/Out message to reset buffer positions"), 24af8cf (2022-06-12, "updated usbd logging"), and dd7f7fe32af409cc6f2cb9eeabe1081724de223a (2022-06-19, "Make USBD_AUDIO_BUFFER_PACKETS configurable on project level") — `git log v22.4.0..v22.5.0 -- Source/usbd_audio.cpp` in [OpenWare](https://github.com/RebelTechnology/OpenWare)
- The last commit touching `ACDC/` on master is dd7f7fe (2022-06-19). Earlier ones: 6aa9056 (2022-04-06, "updated ACDC config"), 1e6f11b (2022-03-17), and the series from 2021-11 to 2022-03 (LED PWM, 4-channel audio, inverted ADC/DAC, "10Vpp output gain" 05be43d 2021-12-17) — [ACDC history](https://github.com/RebelTechnology/OpenWare/commits/master/ACDC)
- Most recently pushed upstream branches: `feature/oneiroi` 2f51bf2768daf93ca310a4eeb7592c0f9a8d81d7 (2025-06-11, "Removed pots and faders calibration"; 104 commits ahead of master, v2.0.0 on 2025-03-29, for the Befaco Oneiroi). Then `mk/oneiroi` 8a6d691 (2025-02-21) and `feature/witch3` c5496ac40a409fefa457bc7bc6cd36133a0eec65 (2023-10-10). None of them touches `ACDC/` or `Source/pcm3168a.c`. Oneiroi changes `Source/usbd_audio.cpp` only for whitespace and logging, e.g. 4b0533c (2023-06-04) "Using double when logging USB error". — [OpenWare branches](https://github.com/RebelTechnology/OpenWare/branches)
- RebelTechnology/OwlProgram (patch SDK): last commit 3942f82 on 2024-10-16 (licence wording merge). The only AC/DC-ish match is 04addfd (2021-02-17), "added ac/dc blocking IIR filters", which refers to DC-blocking filters and not the module. — [OwlProgram](https://github.com/RebelTechnology/OwlProgram)
- RebelTechnology/OpenWareLab (docs site): last commit 5159b50 on 2022-03-31 ("Xibeca Dev Kit resources") — [OpenWareLab](https://github.com/RebelTechnology/OpenWareLab)

### Inferences
- No upstream AC/DC firmware work has landed since mid-2022. The released ACDC.bin (v22.5.0) is built from master's ACDC config. The noise, clock and output-level experiments on side branches (§3) were never merged.

### Gaps
- I could not list GitHub Releases on RebelTechnology/OpenWare directly (blocked), so I used the pingdynasty mirror page instead.
- Activity after 2025-06 could not be checked beyond the git refs. No newer refs exist as of 2026-10-23.

## 3. Forks and side branches with divergent work relevant to AC/DC

### Takeaway
The meaningful AC/DC-specific divergent work is in three **unmerged upstream branches by Martin Klang (2022)**, mirrored in pingdynasty's fork. `hack/acdc-output-levels` (v22.4.s) has exact-48 kHz clocking, a codec auto-rate mode, SAI output drive disabled, new gains, a mute when no USB stream is present, and output level LEDs. `feature/acdc-lowspeed` runs the CPU at 240 MHz and retunes the SAI clock. `feature/acdc` adds self-powered USB, gains and 4-slot SAI. antisvin's fork (OWLsy for Daisy) is active to 2023-04 but contains nothing for AC/DC.

### Cited Findings
- **`hack/acdc-output-levels`** — tip 7f3cc4113b33ea71e03d537f4ba2d09233e528ee (2022-07-15, "v22.4.s: MCLK=256fs no master div"), 59 ahead / 56 behind master, version string `FIRMWARE_VERSION "v22.4.s"`. Contents:
  - e219182 (2022-07-15) "Update SAI clocking to 256fs and no master divider": PLL3P/Q = 16, PLL3FRACN = 262, `NoDivider = SAI_MASTERDIVIDER_DISABLE`, `SlotActive = 0x0000000F`
  - bc7391c (2022-07-09) "changed SAI MCLK to 24.576Mhz (div by 4)"; db9d3dd (2022-07-13) "v22.4.r: MCLK=512fs"
  - f90e3f4a5cf3bdb271f2fb08a253352587a4592e (2022-07-15) "AUTO clock mode": pcm3168a reg 64 and reg 80 set to auto rate instead of single rate
  - 65fc0db3d543a858717b78726b89a734a74dbff9 and 7a082be (2022-06-26) "Disable SAI output drive and change nvic priorities in favour of SAI": DMA1 Stream2/3 priority 5 → 10
  - A USB rework: 2df3aef "Fix usb buffer initialisation and ensure always on frame boundary", ddba010 "Always calculate USBD feedback", e9c4e97 "Allow usbd_audio_sof_callback to be called from TIM handler", 5a5e1a1 "Zero fb handling", edc6c99 "Increase usbd audio buffer to 4 packets", a series of margin tunings (v22.4.n/p/q), USB `Sof_enable = ENABLE`, and a new `usbd_audio_sof_callback()` that also accepts half-rate readings
  - hardware.h: `AUDIO_INPUT_GAIN 88` (comment "84 too low, 92 too high"; "88 / 114 : 10Vpp in, 5.3/4.99Vpp out"), `AUDIO_BLOCK_SIZE 8`, `USBD_SELF_POWERED 1U`, a boot LED sweep, and clip level 4090
  - 4cafadbb93dbfb6749dcc1737aa36b588fe872ba (2022-05-21) "ACDC hack to set output LEDs" (RMS of output into LED PWM)
  - 237c63d3fddb037c70fe89a9a340e95e418e620a (2022-05-22) "hack to prevent ACDC audio thru": `memset` of the DAC output to 0 in `usbd_rx_convert()` when no USB RX stream exists
  
  — [branch hack/acdc-output-levels](https://github.com/RebelTechnology/OpenWare/tree/hack/acdc-output-levels), [commit 7f3cc41](https://github.com/RebelTechnology/OpenWare/commit/7f3cc4113b33ea71e03d537f4ba2d09233e528ee), [commit 237c63d](https://github.com/RebelTechnology/OpenWare/commit/237c63d3fddb037c70fe89a9a340e95e418e620a), [commit 65fc0db](https://github.com/RebelTechnology/OpenWare/commit/65fc0db3d543a858717b78726b89a734a74dbff9), [commit f90e3f4](https://github.com/RebelTechnology/OpenWare/commit/f90e3f4a5cf3bdb271f2fb08a253352587a4592e)
- **`feature/acdc-lowspeed`** — 237f74628beb2878815e55c9c31e547740bd02b6 (2022-10-19, "Set master clock to 240Mhz and tune SAI clock to 48.000kHz") plus bd05348 ("Cube update"). It is 2 ahead / 46 behind. PLL1N goes 120 → 60 (SYSCLK 240 MHz), AHB DIV2 → DIV1, and ACDC.ioc PLL3FRACN goes 0 → 280 (SAI1 98.305 MHz). The generated `main.c`, however, sets `PLL3FRACN = 6144`. — [commit 237f746](https://github.com/RebelTechnology/OpenWare/commit/237f74628beb2878815e55c9c31e547740bd02b6)
- **`feature/acdc`** — tip 56174b4700fb4618392c0d6d3873da27fcc76413 (2022-05-22, "allow USBD_SELF_POWERED override"), 8 ahead / 81 behind. Commits: a00820b ("set self-powered", `USBD_SELF_POWERED 1U`), 62eed18b32ff2c1cf8fd59f83aa71db778ea7160 (2022-05-06, "adjusted gain settings and clipping level", IG 104 → 88), cf8eaf9c8a62dc9a8538cb293781bea829d857f9 (2022-04-15, "enable 4 ch SAI", SlotActive slots 0-3 only), 24cc21b ("correct sample counter") and 03deb20 (EXP2 footswitch). The earlier part was merged as PR #69/#70 (dac65df, 2022-04-07), but cf8eaf9 and 62eed18 are **not** in master. — [commit 56174b4](https://github.com/RebelTechnology/OpenWare/commit/56174b4700fb4618392c0d6d3873da27fcc76413), [commit cf8eaf9](https://github.com/RebelTechnology/OpenWare/commit/cf8eaf9c8a62dc9a8538cb293781bea829d857f9)
- **pingdynasty/OpenWare** (Martin Klang's personal fork): its branch tips are identical to upstream (master 62a0187, feature/oneiroi 2f51bf2, the hack/acdc branches as above). It has no unique AC/DC work. — [pingdynasty/OpenWare](https://github.com/pingdynasty/OpenWare)
- **antisvin/OpenWare** (Stas Shtin, main external contributor; OWLsy port for Electro-Smith Daisy). Most recent branch is `feature/takeover` fba3a9d21a8ebea5713cc1799c971c434e42a045 (2023-04-11, tag `owlsy-v25.2-rc1`, 213 ahead / 905 behind master), with "Truncation and DC offset compensation" (a180745) and "Bipolar CV inputs" (9bc37e3) for Daisy targets. Other branches: `daisy`/`feature/daisy-pod` 019353d (2023-03-13), `feature/patch-init` (2023-01-18), `feature/spi-flash-fix` 934ff6a (2022-11-12, = upstream PR #81), `feature/patch-external-codec` (2022-08-03), `preenfm3` (2022-04-09). Its default branch is stale: master a2db5a6 (2020-04-15). Only `feature/expander-digitalbus` (efd4c8f) and `preenfm3` (ee13a0a) touch ACDC/pcm3168a files, and in both cases only through merge commits. Release tags run owlsy-v24.1.0 → owlsy-v25.2-rc1. — [antisvin/OpenWare](https://github.com/antisvin/OpenWare); OWLsy forum thread [Electro-Smith forum](https://forum.electro-smith.com/t/owlsy-announcements-releases/2277)
- I probed about 20 other likely fork owners with `git ls-remote https://github.com/<owner>/OpenWare` (hemmer, xconverge, olilarkin, electrosmith, mcclure and others). None exist under that name. — (shell probe; no URL)

### Inferences
- The `hack/acdc-output-levels` commits read like a 2022 investigation into AC/DC output level, clocking accuracy, USB glitches and possibly noise:
  - exact 48 kHz: 12.288 MHz MCLK with NODIV, which I calculate as fs ≈ 47,999.995 Hz
  - turning off SAI OutputDrive and raising the SAI DMA priority
  - switching the codec to auto rate
  - suppressing analog pass-through when USB is idle
  
  None of it is in the released v22.5.0 ACDC.bin. For anyone fixing AC/DC noise or clock issues, this branch is the most relevant starting point, but it is 56 commits behind master and would need merging.
- `feature/acdc-lowspeed` has an internal inconsistency: by my calculation the main.c FRACN 6144 gives about 48.2 kHz, while the ioc FRACN 280 gives about 48.0006 kHz. It should not be built without checking.
- The "4 ch SAI" change (enabling only TDM slots 0-3) is unmerged. Master transfers all 8 slots by DMA while only 4 are used.

### Gaps
- The full GitHub fork list (network graph) could not be retrieved because the API and HTML were blocked. Forks under other owner names may have divergent AC/DC work that I did not find.
- The gitlab.huma-num.fr `bbdmi/OpenWare` mirror (seen via search, [code.gouv.fr listing](https://data.code.gouv.fr/hosts/gitlab.huma-num.fr/repositories/bbdmi%2FOpenWare)) refused the connection, so its contents are unknown. It is probably for BioSignals rather than AC/DC (unverified).

## 4. Noise-relevant details in the AC/DC code, and standalone behaviour without a USB host

### Takeaway
AC/DC firmware runs the stored patch and processes audio **without a USB host**. Audio is clocked by the SAI/codec (from the HSE crystal via PLL3), not by USB SOF. Several code details are plausible noise contributors:
- PWM LEDs at about 2.3 kHz, in the audio band
- codec HPF intentionally off (DC coupling)
- 16-bit truncation for USB
- SAI clock about 186 ppm off 48 kHz
- non-functional mute and USB volume controls
- no muting of output when no patch is running (only a buffer clear)
- the unmerged "no audio thru" hack

### Cited Findings
- **Boot and standalone path:**
  - `Owl::setup()` → `codec.init()`, `codec.set(0)`, gain set, ADC DMA start, then `program.startManager()`. `bootstrap()` loads `settings.program_index` (default `DEFAULT_PROGRAM 1`) if `registry.hasPatch()`, and otherwise enters `CONFIGURE_MODE`. It then calls `codec.start()` unconditionally.
  - Nothing in this path checks for USB enumeration or VBUS.
  - The audio task wakes on each SAI DMA half/complete interrupt (`audioCallback` → `vTaskNotifyGiveFromISR`).
  
  — [Source/Owl.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/Owl.cpp) lines 72-117; [Source/ProgramManager.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/ProgramManager.cpp) lines 206-218, 576-601; [Source/device.h](https://github.com/RebelTechnology/OpenWare/blob/master/Source/device.h) line 145
- **USB/patch routing:**
  - With `USE_USBD_AUDIO_RX` and no `_PRE_FX` define, POST_FX is active. After each patch block, `usbd_tx_convert(pv->audio_output)` sends the patch output to the host. Then `usbd_rx_convert(pv->audio_output)` "convert[s] USBD audio rx to DAC (overwriting patch output)", but only when `usbd_rx != NULL`, i.e. while the host is streaming.
  - Without a stream, the patch output goes to the DAC. If the host underflows, the missing samples are zero-filled (`memset`).
  - The conversion is only called from `onProgramReady()`, the patch's per-block hook. So without a running patch, no USB audio is moved at all.
  
  — [Source/ProgramManager.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/ProgramManager.cpp) lines 83-158, 263-318
- MIDI handling: since PR #63 (076c033adf79350d1222fe0a2a3521ccc09497d7, 2021-11-02, "process USB messages each audio block, before patch runs (or in loop if no patch is loaded)") — [commit 076c033](https://github.com/RebelTechnology/OpenWare/commit/076c033adf79350d1222fe0a2a3521ccc09497d7)
- **Clock source:** the SAI1 kernel clock comes from PLL3 off the 8 MHz HSE, and SAI1 Block A is the master. The USB OUT endpoint is async with explicit feedback derived from the codec DMA counter. The USB kernel clock is HSI48, with no CRS trimming found. — [ACDC/Core/Src/main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c), [Source/usbd_audio.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/usbd_audio.cpp)
- **Runtime controls:** SysEx configuration codes exist for `"HP"` (codec high-pass, via `codec.setHighPass()` → `codec_highpass()`, PCM3168A reg 82), `"IG"`/`"OG"` (codec input and output attenuation) and bypass. The HP setting is *not* stored in `settings`, so it reverts on reboot. The gain settings are stored. — [Source/MidiHandler.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/MidiHandler.cpp) lines 209-226; [Source/OpenWareMidiControl.h](https://github.com/RebelTechnology/OpenWare/blob/master/Source/OpenWareMidiControl.h) lines 85-87
- **Mute and volume are not implemented:** `Codec::mute()` is `codec_set_gain_out(0); // todo: fixme!`. `usbd_audio_mute_callback` and `usbd_audio_gain_callback` are `// todo!` no-ops. `codec_bypass()` is `// todo`. — [Source/Codec.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/Source/Codec.cpp) lines 27-43, 106-112; [Source/pcm3168a.c](https://github.com/RebelTechnology/OpenWare/blob/master/Source/pcm3168a.c)
- **LED PWM:** TIM2, TIM3, TIM4 and TIM8 drive 8 LEDs with `Prescaler = 100` and `Period = 1023`. Timer clock is 240 MHz (ACDC.ioc `RCC.Tim2OutputFreq_Value=240000000`). Brightness tracks the CV/audio level each loop (`onLoop`: input LEDs follow `PARAMETER_AA..AD`, output LEDs `PARAMETER_BA..BD`). The clip LEDs are GPIOs on PA0, PC13, PI11 and PC9. — [ACDC/Core/Src/main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c) lines 646-809; [ACDC/Core/Src/ACDC.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/ACDC.cpp)
- **Codec analog-relevant settings:** HPF off on all ADCs (intentional, for DC coupling). ADC channels 5/6 and DAC 5-8 are disabled. DAC "Power Save Enable". Single-ended inputs. Phase inversion on both ADC and DAC. — [Source/pcm3168a.c](https://github.com/RebelTechnology/OpenWare/blob/master/Source/pcm3168a.c)
- **CV ADC:** STM32 ADC1, `ClockPrescaler ADC_CLOCK_SYNC_PCLK_DIV4`, software trigger, oversampling disabled, 64.5-cycle sampling. Parameters are smoothed with `(p*3 + adc)>>2` — [ACDC/Core/Src/main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c) lines 345-374; [ACDC/Core/Src/ACDC.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/ACDC.cpp)

### Inferences
- **Standalone:** yes. A powered AC/DC with no USB host runs the patch in slot `settings.program_index`. Audio in → patch → out, clocked by the codec. There is no firmware setting to make it wait for USB.
  - If a stream later starts, the USB RX audio *replaces* the patch's DAC output (POST_FX). USB TX carries the patch output.
  - If no patch is stored, the device sits in CONFIGURE_MODE: the DMA runs on a zeroed TX buffer, giving silence, and no USB audio flows.
  - Whether an input → output pass-through happens without USB depends on the stored patch. The upstream "hack to prevent ACDC audio thru" (237c63d, unmerged) suggests the stock patch passes input to output when the host is not streaming.
- **LED PWM as a noise suspect:** 240 MHz / 101 / 1024 ≈ **2.32 kHz** (my calculation from the cited prescaler, period and timer clock). Eight LEDs switching at an audio-band rate, with level-dependent duty, could couple a ~2.3 kHz whine and harmonics into the analog stages or the ground. Raising the PWM frequency (smaller prescaler, e.g. 0 → ~234 kHz) would be a cheap firmware experiment. This is a plausible hypothesis, not confirmed.
- **Digital edge noise:** SAI OutputDrive is enabled, and Klang's hack branch disabled it (65fc0db). DMA transfers all 8 TDM slots. Turning the SAI and codec clocks to exact rates (hack branch) could reduce digital edge noise or intermodulation. I found no measurements of either.
- **HPF off (correct for DC CV):** any DC offset or very-low-frequency drift passes straight through. Enabling the codec HPF via SysEx `HP=1` is an option for audio-only use, but it is not persistent.
- **Truncation:** 16-bit USB truncation (no dither) raises the noise floor of USB-recorded material to about −96 dBFS. The hardware.h approach permits `AUDIO_BITS_PER_SAMPLE 24/32` in principle, but that was not done for AC/DC.
- **USB host clicks:** the ±1-sample feedback clamp, combined with a sample rate 186 ppm off nominal, may contribute to occasional clicks or pops with some hosts. The v22.0 release notes list USB clicking as a known issue, and later fixes claim improvements.

### Gaps
- No public measurement or bug report about AC/DC noise was found. Searches on retail, review and forum sites gave nothing specific, and modwiggler/GitHub issue pages could not be fetched.
- I could not confirm which patch Befaco/Rebel preload in slot 1 on shipped AC/DC units, or whether it passes audio through.

## 5. Known issues and PRs about AC/DC, noise, USB audio and standalone mode

### Takeaway
I could not read issue and PR metadata (API and HTML blocked). The PR refs show 65 PRs, the latest being #81 (antisvin, 2022-11-12, unmerged SPI-flash ISR fix) and #76 (v22.5.0 release merge). AC/DC entered via PRs #69/#70 (2022-04). Release notes list USB-audio sync and clicking issues as fixed or improved. No AC/DC-specific issue could be verified.

### Cited Findings
- `git ls-remote origin 'refs/pull/*/head'` gives 65 PR refs. Most recent by commit date:
  - #76 (62a0187, v22.5.0, merged)
  - #81 (934ff6a7acc1dd2029d10774df7fed2488c42e64, 2022-11-12, antisvin, "This gets called from ISR currently", Source/Storage.cpp; 1 commit not in master)
  - #70 and #69 (feature/acdc merge dac65df, 2022-04-07)
  - #68 (pow/log tables)
  - #63 (USB message processing per block, 2021-11-02)
  - #62 (antisvin, memory barriers on H7, 2021-10-20; 4 commits not in master)
  
  — [OpenWare pulls](https://github.com/RebelTechnology/OpenWare/pulls)
- Release-note issues: v22.0.0 "USB Audio might 'click' due to synchronisation with host". v22.1.rc1 "Fix USBD audio sync issues / descriptor issues (Windows support)". v22.2.0 "Improved USB Audio FIFO allocation". v22.5.0 "Improved USBD Audio host synchronisation". — [pingdynasty/OpenWare releases](https://github.com/pingdynasty/OpenWare/releases), [HISTORY.md](https://github.com/RebelTechnology/OpenWare/blob/master/HISTORY.md)
- Review context: MusicRadar (2022-10-03) gives no noise remarks. It describes 4 × ±10 V DC-coupled channels and use with Ableton CV Tools — [MusicRadar](https://www.musicradar.com/reviews/befaco-acdc)

### Inferences
- Because master has not changed since 2023-03 and the AC/DC experiments sit unmerged on branches, any open AC/DC issue is probably unaddressed upstream.

### Gaps
- Titles and states of issues and PRs, and any AC/DC, noise or standalone issue threads, could not be retrieved. This needs authenticated GitHub API access (`gh issue list -R RebelTechnology/OpenWare --state all`) or a browser.
- The OWL patch library (https://www.rebeltech.org/patch-library/) was not inspected for AC/DC-specific patches.
