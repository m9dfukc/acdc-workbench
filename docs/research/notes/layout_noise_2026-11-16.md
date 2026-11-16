# Code/data layout and audio noise: OpenWare, forum, forks, MCU literature (2026-11-16)

Research note for messlog D33 (2026-11-15). In that test, only the addresses of code and data moved: 0x150 B of dead code in `.text`, 0x28 B in `.bss`, no functional change. This moved the deterministic lines in the AC/DC ADC data: fs/8 +1.8 dB, 1 kHz SOF comb +1.5 dB, intermodulation products −4.5 dB. With `.late_text`/`.late_bss` the effect went away (D34).

## Question

1. Do OpenWare, its forks, issues/PRs, commit messages or the Rebel Technology forum report any of the following on OWL/Lich/Witch/Magus/Genius/AC/DC/Xibeca hardware?
   - Noise, spurs or "digital noise" that change with code/data placement, linker layout, section placement, alignment, cache/ITCM/DTCM use, compiler version/optimisation, or build differences.
   - Noise that changes between firmware versions without obvious cause.
   - Noise that depends on CPU load or on the patch.
2. Secondary: is it documented (ST/ARM/TI/ADI or well-documented engineering sources) that any of these change the supply-current pattern and therefore the noise/spurs in an adjacent ADC/codec, on STM32H7/Cortex-M7 or MCUs in general: code layout, flash wait states, cache behaviour, execution pattern? Which mitigations exist?

## Short answer

- **No source explicitly reports that code/data layout (linker placement, alignment, padding, section order, ITCM vs flash) changes audio noise on OWL/Rebel Tech hardware.** This covers the OpenWare repo (all upstream branches + our fork), RebelTechnology GitHub issues/PRs, and the forum. Our D33 result appears to be the first documented case for this platform.
- **Related firmware→noise reports exist on Rebel Tech hardware, but each has a functional cause:**
  - LED PWM timer settings on Magus: an audible ~2.9 kHz tone, and CV-output noise. These were changed and reverted, commit `3c7e2301`.
  - A sample-conversion bug in OwlWare v13/v14.
  - USB-host activity on Lich.
  - Patch/buffer-size-dependent tones on the OWL Pedal (reported, not diagnosed).
- **The closest match is on the Electrosmith Daisy Seed, which uses the same MCU family (STM32H750) with an external audio codec.** Electrosmith's founder (shensley) explains the callback-frequency tone: the STM32's current draw is a transient with each periodic audio callback, it lifts GND, and it appears at the callback frequency. Users measured that tone at 10–15 dB above the floor and suppressed it by randomly jittering processing time ("dither"), by raising the callback rate above the audio band, or with notch filters. None of these posts mentions layout, but the mechanism is the one we assume.
- **ST documents that MCU supply current depends on "program location in memory and executed binary code"** (STM32H750 datasheet DS12556 §6.3.6). The run-mode tables give, at 400 MHz VOS1, all peripherals off (CoreMark): 71 mA from ITCM, 105 mA from flash with cache ON, 73 mA from flash with cache OFF. ST AN2834 explains how CPU activity couples into an ADC ("capacitive coupling", aim for "digital silence"). Neither document makes the specific claim "layout → ADC spurs". That step is our own [Hypothese], supported by D33.
- General computer-architecture literature (Mytkowicz et al., ASPLOS 2009) shows that link order and stack alignment alone change execution timing measurably. This is the missing link between "addresses moved" and "different current waveform per audio block".

---

## 1. Findings in OpenWare / forks / forum

### 1a. Explicitly reports layout → noise

**None found.** Searches are listed in section 3.

### 1b. Related, but not the same (firmware change → noise with a functional cause)

| # | Source | What | Why it is not "layout" |
|---|---|---|---|
| R1 | Forum t/1365 "V/Oct calibration on Magus", #12 (antisvin, 2020-02-13), #14 (mars, 2020-02-17), #15 (antisvin): https://community.rebeltech.org/t/v-oct-calibration-on-magus/1365 | After a firmware update: "constant tone high-pitch ringing in output". mars attributes it to a changed **LED PWM rate** and reverts it. antisvin then confirms a tone at ~2.9 kHz + harmonics is gone. A pulse every 10 ms in the codec input remains and is also present in v20.5 (#16). | A changed timer configuration, a functional change. It does show that a pure firmware change of periodic digital activity creates or removes audible tones on OWL hardware. |
| R2 | OpenWare commit `3c7e2301f06dd0ce` "reverted to previous LED PWM timings" (Martin, 2020-02-17), local clone `firmware/OpenWare`, files `Magus/Src/main.c`, `Magus.ioc`. TIM2: prescaler 6/period 4100 → 4095/200; TIM3: period 6 → 100 | The firmware side of R1. | as R1 |
| R3 | Forum t/1628 "Noisy parameter patch points" (Magus), #4/#8/#9/#13/#20: https://community.rebeltech.org/t/noisy-parameter-patch-points/1628 | mars (#4): "most of the noise is coming from the LED drivers"; a higher PWM frequency worked on one device, not on all, and was rolled back. antisvin (#8): reverting `3c7e2301` (= the faster PWM) "eliminates noise pretty much completely" on his unit. Side effects: double LED brightness, whining noise on USB power (#9). #13: after a brightness-control fix, the old patch no longer helps much and adds coil whine. #20 (mars, v22.4): CV noise 150–180 mVpp, possibly a regression, LED level has little effect. #21: spikes about every 200 µs. | Noise depends on firmware version and on periodic peripheral activity (LED PWM, MAX11300 update). No one checked layout. The effect also varies from device to device (#4). |
| R4 | Forum t/1831 "Periodic Noise in Distortion FX?" (Witch), #4/#5/#10 (mars, 2022): https://community.rebeltech.org/t/periodic-noise-in-distortion-fx/1831 | Patch-dependent noise: about −80 dB, visible in USB recordings, follows the LED phase of LFO1. Cause (#10): "a bit of LED PWM noise on the E control", amplified by the overdrive. | Coupling of LED PWM into a pot/CV input, then amplified by the patch. |
| R5 | Forum t/1610 "Adjustable USB host problem" (Lich), #1–#5: https://community.rebeltech.org/t/adjustable-usb-host-problem/1610 | High-pitched noise ("probably a clock") while the USB host is active with a Keystep. After a replug the host stops working (known bug) and the noise is gone. | The noise depends on the activity state of a peripheral (USB host), not on layout. |
| R6 | Forum t/1555 "New firmware: OpenWare v21.0", #7–#12: https://community.rebeltech.org/t/new-firmware-openware-v21-0/1555 | Cyclic "bit crusher" noise when streaming USB audio from Lich. mars (#10): synchronous USB, no clock synchronisation. He suggests a minimal-CPU patch to rule out CPU load. | A USB synchronisation/data error, not analog coupling. |
| R7 | Forum t/868 #7 (mars, 2017-10-25): https://community.rebeltech.org/t/owl-firmware-release-v13/868 ; t/888 #7: https://community.rebeltech.org/t/noise-problem-on-extra-assignable-slot-patches/888 ; t/1002 #3: https://community.rebeltech.org/t/user-patch-noise-update/1002 | OwlWare v13/v14 "terrible noise superimposed on the signal": "a little bug … mess[ed] with the sample conversion code". Also incompatibilities between patches and firmware. | A software bug, not coupling. |
| R8 | Forum t/1032 "Any news on v15?" #7 (B1gBulg3, 2019-08-07): https://community.rebeltech.org/t/any-news-on-v15/1032 | OWL Pedal: a constant background tone ("almost like a harsh saw wave at certain buffer settings"). Its loudness and frequency change with buffer size and patch. No reply. | Fits a **block-rate tone** (like our fs/8). No diagnosis, no layout aspect. Compare t/825 #12 (https://community.rebeltech.org/t/background-noise-problem/825): "changing the buffer size helps the noise". |
| R9 | Forum t/1002 #8 (markdibarry, 2018-05-03): https://community.rebeltech.org/t/user-patch-noise-update/1002 | Counter-example on the OWL Pedal: block size has no effect on the noise floor, patch change ±1 dB. Noise is dominated by the supply (USB +26 dB vs. isolated PSU +18 dB). | Broadband/supply-dominated, no line analysis. |
| R10 | Forum t/2172 #2 (antisvin, 2023-10-23): https://community.rebeltech.org/t/bad-noise-with-some-patches/2172 | "the new OWL3 is using a more performant MCU that happens to have significantly cleaner ADC inputs". | Concerns pot/CV ADC, not codec. Patch-dependent noise there = delay-line zipper. |
| R11 | Forum t/2174 #2 (antisvin, 2023-10-30): https://community.rebeltech.org/t/owl3-witch-magus/2174 | Magus hardware was updated "to reduce amount of noise which can be a problem there due to having LEDs and display". | Hardware fix, no firmware layout. |
| R12 | pingdynasty/OwlNest issue #13 (2014): https://github.com/pingdynasty/OwlNest/issues/13 | "Digital artefacts" depending on the Remote-Control mode. Fix: hysteresis on pot ADC values (OwlWare commit `a6056648`). | Pot ADC noise → parameter jitter. |

### 1c. Code facts (OpenWare, our fork `fork/acdc/fx1d`) relevant to the mechanism [Code]

- `ACDC/Core/Inc/hardware.h`: `USE_ICACHE`, `USE_DCACHE` are defined. `ACDC/Core/Src/main.c` enables both caches (`SCB_EnableICache/DCache`), runs at `PWR_REGULATOR_VOLTAGE_SCALE0` with `FLASH_LATENCY_4`. Code therefore runs from internal flash through the 16 KB L1 I-cache, and timing depends on hits and misses.
- `Hardware/xibeca.ld`: `ITCMRAM` only 4 KB (stack, `_estack`), `CCMRAM` 60 KB at 0x1000, `DTCMRAM` 48 KB + `PATCHRAM` 80 KB, `DMA_D2` 64 KB at 0x30000000, `RAM_D2` 224 KB. **No firmware code is placed in ITCM** (no `.itcm`/RAMFUNC section in `Source/`, `ACDC/`).
- FreeRTOS `configUSE_IDLE_HOOK 0` (`ACDC/Core/Inc/FreeRTOSConfig.h`). Apart from vendor drivers, `Source/` and `ACDC/` contain no `__WFI`/`__WFE`. The CPU never sleeps. Current changes come from the instruction/memory mix (cache misses → AXI flash accesses, DMA), not from sleep/wake transitions.
- `AUDIO_BLOCK_SIZE 8`, `CODEC_BLOCKSIZE 256` → audio callback at 6 kHz = the fs/8 line.
- Upstream ITCM/cache commits (`d848233d` "use ITCM for CCM, fw and program stack", `94b09e52`, `7938b6ee` "enabled cache", PR #37 "H7 cache" https://github.com/RebelTechnology/OpenWare/pull/37) are motivated by performance only. None of their messages mentions noise.

---

## 2. General literature (STM32/MCU, comparable platforms)

### 2a. Primary sources (vendor/academic)

- **STM32H750 datasheet DS12556 Rev 7 (March 2023), §6.3.6 "Supply current characteristics"**, Tables 28–30. Copy used: https://cdn.sparkfun.com/assets/b/6/0/6/b/stm32h750ib.pdf (official: https://www.st.com/en/microcontrollers-microprocessors/stm32h750ib.html).
  - Text: "The current consumption is a function of … I/O pin switching rate, program location in memory and executed binary code."
  - Values (Typ, CoreMark, all peripherals disabled, 400 MHz VOS1):

    | Code running from | Typ |
    |---|---|
    | ITCM | 71 mA |
    | flash, cache ON | 105 mA |
    | flash, cache OFF | 73 mA |

    With all peripherals enabled: 165 / 160 / 135 mA.
  - Footnote to the ITCM table: "Data are in DTCM … cache has no influence on consumption in this case."
  - → Where code is fetched from, and whether the cache is active, changes core current by tens of mA. These are averages. The time profile within an audio block is not specified. Its modulation is our [Hypothese].
- **ST AN2834 "How to get the best ADC accuracy in STM32 microcontrollers"** (Rev 3, §3.3.5 "Minimizing internal CPU noise"; §4.3.5 in Rev 10, 2024). https://www.st.com/resource/en/application_note/cd00211314-how-to-optimize-the-adc-accuracy-in-the-stm32-mcus-stmicroelectronics.pdf (ST blocks automated downloads, text read from the Rev 3 copy at https://www.manualslib.com/manual/1573810/St-Stm32.html?page=38).
  - The CPU "generates a lot of internal and external signal changes", which reach the ADC "through capacitive coupling".
  - Goal: "digital silence" during sampling/conversion.
  - Measures: minimise I/O changes, minimise CPU activity (stop/wait mode), stop clocks of unused peripherals.
  - Covers the **on-chip** ADC. For an external codec that converts continuously (PCM3168A), "silence during conversion" is impossible. The transferable idea is to **keep the digital activity spectrum constant/flat**.
- **ST AN4891 "STM32H72x/73x and single-core STM32H74x/75x system architecture and performance"**: https://www.st.com/resource/en/application_note/dm00306681-stm32h72x-stm32h73x-and-singlecore-stm32h74x75x-system-architecture-and-performance-stmicroelectronics.pdf. Benchmarks with different code/data placement (ITCM, AXI-SRAM, flash with/without cache, flash wait states). It documents **performance/timing**, not noise. Not re-read in full here, summarised from the search snippet.
- **Mytkowicz, Diwan, Hauswirth, Sweeney: "Producing Wrong Data Without Doing Anything Obviously Wrong!", ASPLOS 2009**, DOI 10.1145/1508244.1508275, PDF: https://huang.isis.vanderbilt.edu/cs8395/readings/producing-wrong-data.pdf.
  - Link order (= code/data layout) and environment size (= stack alignment) alone change measured performance by several percent: −O3 vs −O2 between +8 % and −7 % depending on link order.
  - Desktop CPUs, but the same mechanism (alignment → fetch/cache/branch behaviour → timing) applies in principle to the Cortex-M7 with I-cache, 64-bit instruction fetch and branch prediction [Hypothese].
- **Camurati, Poeplau, Muench, Hayes, Francillon: "Screaming Channels: When Electromagnetic Side Channels Meet Radio Transceivers", ACM CCS 2018**, DOI 10.1145/3243734.3243802, https://www.eurecom.fr/en/node/4902417. On mixed-signal chips, the noise of digital processing (code-dependent, e.g. AES) leaks into the analog RF path of the same chip and is transmitted. Shows in principle that what code does is visible in an adjacent analog path. Different chip and frequency range.

### 2b. Comparable audio platforms (engineering forums, not peer-reviewed)

- **Electrosmith Daisy (STM32H750 + codec), community.daisy.audio (formerly forum.electro-smith.com):**
  - t/432 "Questions about digital noise and grounding": https://forum.electro-smith.com/t/questions-about-digital-noise-and-grounding/432
    - **#10 shensley (Electrosmith, 2020-08-24):** "The STM32 chip is actually a little too good at regulating its own power consumption." The current transient at each periodic callback lifts GND, and the tone is "most audible at the callback frequency". Mitigations: callback rate outside the audible range, isolated DC-DC for the audio section (Petal/Field/Patch designs).
    - #8 (jerry20091103): noise during LCD frame drawing, louder when Reverbsc runs at the same time ("processor itself emits noise when it's busy running particular tasks").
    - #11/#27 (MikeDB): compute at 96 kHz with a fixed slot schedule, and random delay at the start of the non-real-time work "spreads the noise out rather than being a repetitive 12kHz tone".
    - #51: block size 3 → callback at 16 kHz, practically inaudible.
    - #96 (Firesledge, 2025-10-24): 2nd-order notches (Q 100, −40 dB) at the callback frequency and its harmonics on the inputs, plus a multi-band noise gate.
  - t/6028 "Daisy Seed DMA tx/rx timing and issues with small block sizes": https://forum.electro-smith.com/t/daisy-seed-dma-tx-rx-timing-and-issues-with-small-block-sizes/6028
    - #1/#3 (jeffffff): ADC noise at sample_rate/block_size, 10–15 dB above the floor. A ripple that depends on CPU usage (gone at < 50 % CPU) was traced to DMA rx/tx timing.
    - **#7 (passtheducky):** "the processor's power draw fluctuates perfectly periodically with the audio callback and this modulates ground potentials". Fix: small callback, processing in the main loop through ring buffers with **random delays of 0–2 µs** between frames. The callback line drops into the noise floor (−3 dB(A) overall).
    - #4/#5: ITCM discussed for the callbacks. jeffffff thinks it would not help much because the I-cache is large enough. Not measured.
    - #9/#10: extra spikes at 8/16 kHz with the ST-LINK attached.
- **PJRC Teensy Audio**, thread "Audio High pitch buzzing", #45 (Paul Stoffregen, 2016-02-08): https://forum.pjrc.com/threads/27443-Audio-High-pitch-buzzing?p=64647. With the audio library the CPU "draws more current" 344 times per second (= 44.1 kHz/128 audio block), and the tone is "almost certainly a 'ground loop' problem". Fixed by ground routing and supply choice (#43, #48, #49).
- **ST Community, "STM32L031 noisy even in reset"** (LCE, 2025-03-18): https://community.st.com/t5/stm32-mcus-products/stm32l031-noisy-even-in-reset/m-p/784467. A 10 kHz timer-interrupt frequency is visible in an analog spectrum, attributed to sleep/wake ("powering the CPU up and down"). In the end, the 4 kHz line there came from another sleep-cycling IC.

**Note:** None of these sources reports that pure **address shifts** (padding, link order) change the tone level. They all document the block-periodic current → ground → ADC mechanism, and they show that the time profile of execution within the block sets the line spectrum. That layout changes this time profile is plausible (2a), but not documented as an audio effect.

---

## 3. Searched without hits (do not repeat)

- **Local OpenWare clone** (`git log --all --grep`, all `upstream/*` + `fork/*`): `noise`, `noisy`, `noise floor`, `hum`, `interference`, `spur`, `whine`, `glitch` (only `ad1d60d0` "reduce sync-related glitches when streaming audio to DAC", USB sync), `decoupl`, `WFI`, `sleep`, `ICache`, `DCache`, `prefetch`, `FLASH_LATENCY`, `wait state`, `dmadata`, `-O2`.
  - Hits on `ITCM`, `cache`, `align`, `section`, `linker`, `D2`, `optimi` are all performance/build related. No noise reference.
  - `git grep` "noise|interfer|spur|hum" in `upstream/master` (without drivers): only BioSignals GPIO comment, UART noise error, PCM3168A pop noise.
- **GitHub API (unauthenticated; the `gh` token is invalid)**, issues/PRs `repo:RebelTechnology/OpenWare`: `noise`, `hum`, `interference`, `whine`, `glitch` → 0. `cache` → PR #37/#64/#66/#67/#14 (performance). `linker` → #10/#29/#41.
  - `org:RebelTechnology noise` → only OwlProgram DSP topics.
  - Commit search `repo:RebelTechnology/OpenWare noise` → 0. `shmuga/OpenWare`, `hirnlego/OpenWare-fork`: `noise`/`ITCM`/`cache` → 0.
  - `antisvin/OpenWare`, `pingdynasty/OpenWare`: the GitHub commit search does not index forks ("Validation Failed"). Not searchable without a clone. The fork overview of 2026-11-14 (`openware_forks_complete.md`, `forks_update_2026-11-14.md`) found nothing on noise.
  - GitHub code search needs auth → not done.
- **Forum community.rebeltech.org** (`search.json`), no relevant hits: `ITCM`, `DTCM` (only memory/porting topics), `icache`, `dcache`, `cache noise`, `linker script`, `ld file`, `memory layout` (performance only), `SDRAM noise`, `oled noise`, `current consumption`, `noise cpu load`, `noise depends patch`, `ringing`, `whistle`, `wait states` (t/301 = performance), `clock speed noise`, `compiler version`/`gcc version` (build problems only), `6kHz`, `fs/8`, `blocksize noise`, `callback noise`, `ground bounce`, `interference`.
  - Hits evaluated and classified as unrelated or as in table 1b: `noise firmware`, `digital noise`, `noise cpu`, `noise patch`, `whine`, `noise version`, `noise update`, `noise load`, `noise leds`, `noise usb`, `hiss`, `noise floor`, `buzz`, `noise compiler`, `LED PWM`, `pwm noise`, `display noise`, `screen noise`, `power consumption`, `noise changes`, `noise different firmware`, `noise new firmware`, `block size noise`, `buffer size noise`.
  - Threads read in full: 1628, 1365, 2172, 1610, 1002, 888, 868, 1831, 1555, 1948, 2174, 1480, 1927, 1863, 825, 301, 1202, 237, 1032.
  - Already in older notes (not re-evaluated): 2072, 2083, 2244, 2025, 1703, 1511, 1104, 444, 1321, 185.
- Not reachable: ST PDFs directly (Akamai blocks curl/WebFetch). ADI MT-031 (AGND/DGND, digital transient currents) timed out and was **not verified** as a source.

---

## 4. Implications for our firmware [Hypothese throughout]

1. **The mechanism is plausible and fits the literature.** Each 6 kHz block causes a current transient (ISR + DMA + patch + USB). Its exact time course depends on I-cache hits/misses, 4 flash wait states, AXI/D2 bus arbitration and branch alignment. Shifting addresses changes this course, and with it the harmonic content at fs/8 and the phase relation to SOF activity (→ intermodulation products H7). D33 is consistent with that: fs/8 and comb up, intermodulation products down. Two more sources fit: DS12556 (location → current) and Mytkowicz 2009 (layout → timing).
2. **Make the layout sensitivity smaller instead of searching for a lucky layout:**
   - **Hot path into ITCM** (codec DMA ISR, `audioCallback`, sample conversion, USB-audio ISR). ITCM has zero wait states and no cache dependence, so timing becomes deterministic and independent of the rest of the image. ITCM is currently only 4 KB (stack). `CCMRAM` (0x1000, 60 KB) is also ITCM and could take a `.itcm_text` section. Note: per DS12556 the average current from ITCM is *lower* than flash+cache (71 vs 105 mA). That shrinks the swing between block work and idle. The move itself changes the layout once, so A/B against a control in the same session is mandatory (rule from D33/D34).
   - **Flatten the current between blocks:** the idle task spins (no WFI) but executes different code than the block processing. Tests: (a) an idle loop with a similar current profile (e.g. dummy MAC loads from DTCM), (b) the reverse, WFI in idle, to see whether the line *grows* (that would show that the block-to-idle current difference matters).
   - **Dither:** a random start delay of the patch/LED/`onLoop` work within the block (Daisy #7/#27) spreads fs/8 into broadband noise. Watch out: block size 8 leaves little slack (CPU 8 % → slack is there), and the USB/codec timing must not shift.
   - **Callback rate above the audio band:** block size 2 → 24 kHz. Costs CPU/IRQ overhead and changes USB buffer logic (Patch 06). Only an experiment.
3. **Use layout as an experimental lever (E3 in `docs/05`):** a pad sweep (e.g. 0…0x1C0 in 0x20 steps, before the audio functions) with a fixed measurement protocol. It shows how large the spread is and whether there is a "best" layout. Risk: the result may only hold for this one device, and the comb depends on the host port (D21). An ITCM build would be more robust.
4. **Analysis/notch:** Daisy #96 confirms the notch approach (`docs/04`) for callback lines. Our fs/8 line is sample-synchronous, so it can be notched exactly.
5. **For the forum (thread #2244):** D33 would be a new data point for the community. Daisy and Teensy describe the block-rate tone, but no one has yet shown its dependence on pure address shifts.
