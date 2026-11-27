<!-- i18n source=docs/02-noise-befunde.md sha256=5c7f8d840adb2439b43271a6891b73e12372a8cbc4f33f59962c460bb4cc85f2 date=2026-11-27 -->
> English translation of [`docs/02-noise-befunde.md`](../../docs/02-noise-befunde.md), as of 2026-11-27. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 02 – Noise: findings, hypotheses, the isolator question

## Status today (2026-11-27)

A summary of all findings. Numbers and setup are in the lab notebook (`messlog.md`) under the ID given. The dated sections further down show the course of events, each as of its date. **Noise values from before 2026-11-24 apply without the ground wire and cannot be compared directly with new ones.**

**Interference families** in the ADC data, strongly correlated on all channels:

- **SOF comb** at k·≈1 kHz
- **fs/8** = 6000.00 Hz (audio block rate at block size 8, sample-synchronous)
- **Mixing products** n·f1k + m·6000 Hz
- **LED PWM** 2320.98 Hz on acdc2, 2320.54 Hz on acdc1 with the factory firmware. Since fx7a the PWM runs at 48 kHz, the line is gone at inputs and outputs [measured, D78]
- **Knob lines** and **lines from clocks of the MCU**, both weak (see below)

**What lowers the families:**

- **The ground between module and carrier is a main path of the interference [measured, D90].** On the Xibeca module only the ferrite bead L1 connects AGND (codec) and GND, the carrier puts all AGND pins directly on its ground [code: schematic]. The wire pin 15 ↔ pin 33 lowers fs/8 by 18 dB, the comb by 7 dB, the residual by 3 dB and the LED shift to a quarter. At the output the comb drops by 11 dB and fs/8 by 12 dB [measured, D91]. Not moved: 7384.62 / 1215.19 / 4401.90 Hz. The scan line 9633.80 Hz rises by 3.7 dB (−120 file dBFS). After that the comb carries 30–50 % of the noise power, an ideal notch bank would only bring 1.6–3 dB. Guide: `06-hardware-mod-ground.md`.
- **Hot path in the ITCM [measured, D48, also holds for fx4b, D58]:** against 3d fs/8 −5.1 dB, mixing products −35 dB, residual −1.25 dB, RMS −1.1 dB, comb +0.2…+0.4 dB. With the hot path in the ITCM the flash position of the remaining code no longer matters (fx3lp within ≤ 0.25 dB of fx3l).
- **In the firmware only USB code in the ITCM lowers the comb [measured, D42/D44]:** USB in flash +2.5…+3.5 dB against 3d, in the ITCM ±0.
- **fx8a against the original firmware in one session [measured, D86]:** RMS −1.8 dB, residual −3.2 dB, fs/8 −5.2 dB, mixing products −22.6 dB, comb the same. Only the original shows the LED PWM line and a family at 75.72 Hz. The original records after the VCA of the default patch, corrected through the DC offset of the open inputs (`tools/family_table.py --dc-ref/--dc-correct`, method from D26). fx9a is at fs/8 −0.7 dB against fx8a and shows no new line (D89).

**Where the families come from:**

- **The comb hangs on the USB SOF of the host controller [measured, S2-6].** f0 depends on the port: Mac port 999.99 Hz, TB hub 999.868 or 999.997 Hz depending on the port (in the acdc1 clock). A notch filter would have to measure f0 per module and port.
- **At the output the comb is gone without USB and already there without a stream [measured, D20].** Standalone, the output is clean.
- **The position of the code in memory shifts the interference lines [measured, D33].** A pure padding build without a functional change changes fs/8, comb and mixing products by 1.5–4.5 dB.
- **What the CPU does at block rate appears at fs/8 [measured, D42]:** a few µs of polling a DMA register per block raise fs/8 by ≈ 10.6 dB. Mechanism [hypothesis]: bus traffic or a current pulse.
- **The CPU load of a patch raises fs/8 as well [measured, D69]:** Schliere (29 % CPU) against the default patch (6 %) in the same session: fs/8 +3.8 dB, mixing products +13.4 dB, residual and comb ±0.25 dB. An FX patch passes these lines and the comb on to the outputs, without an input signal they are what one hears (D68). The canceller `owl/include/AcdcInput.h` subtracts the block-rate lines at the input: −22…−25 dB at the output (D70, D71).
- **Ground loop [measured, D21]:** only with the AC/DC at the Mac port and the UMC at the hub (+20 dB). Both at the hub → gone. No isolator needed. The daily chain is fine for recordings (D22/D23).
- **Installation in the case [measured, D69]:** no deterioration in the ADC data against "beside the case" (residual −0.1 dB, fs/8 −0.2 dB, comb +0.65 dB two hours apart). The outputs have not been measured for this.

**LEDs:**

- **Proven at the output [measured, D67]:** a patch that lets LEDs glow dimmed puts 2321 Hz with multiples on the output, the level follows the LED pattern by up to 27 dB. For "red" the firmware lets green keep running at a duty cycle of 1023/1024 and sets the red pin anew every 2 ms [code], none of this can be measured at the output [measured, D72].
- **Every change of an LED shifts the output [measured, D73]:** permanently red LEDs do not disturb, but every switching on or off gives a click (per LED about 6 times the noise in the bass, additive), blinking at 40 Hz raises the overall level by 17.6 dB. Patches should therefore switch LEDs rarely, never flickering, and never dim them permanently. Measurement patch: `owl/test/SchliereLedTestPatch.hpp`.
- **The LED current shifts the zero point of all inputs [measured, D74]:** per lit input LED −2.9e-4 of full scale (≈ −2.9 mV, −71 dBFS), the same at in 1–3, measured by the patch itself at the raw inputs (`owl/test/SchliereLedPathPatch.hpp`). Directly at the output about 0.15 mV per LED comes on top with a digitally silent output. The PWM line is the same effect, switched 2321 times per second. Consequence [hypothesis]: the level LEDs of the firmware move the zero point of the recording in time with the envelope. The LED mode off (from fx6a) lowers the shift to 1.7 % (D75), the ground wire to a quarter (D90).

**Knobs and MCU clocks:**

- **Knobs set unequally raise lines of their own [measured, D58, D60, D61]:** 2200.95 / 4401.90 / 6602.85 Hz and 8549.33 Hz, coupled to the device clock, independent of the firmware (fx3l = fx4b).
  - **What counts is the difference between the knobs, not the end stop [measured, D61].** All four at the same stop are like 12 o'clock (−114…−119 dB). One knob alone at the stop gives ≈ −100 dB, alternating left and right (LRLR) −94 dB. The level grows steadily with the distance.
  - The pattern determines the line: LLRR raises 2200.95 and 6602.85 Hz, LRLR raises 4401.90 Hz. At 12 o'clock they stay 6…16 dB above the noise floor, they are never gone.
  - [hypothesis] The sampling capacitor of the knob ADC is recharged from channel to channel. The source of the frequency 2200.95 Hz is open: the ADC scan rate folds to 9633.80 Hz, the LED PWM was at 2320.54 Hz.
  - An FX patch passes them on to the output [measured, D72]: Schliere with knob 3 at the left stop −66…−73 dBFS at the UMC, as strong as the strongest comb lines, in the noise in the middle of the knob travel.
  - Noise measurements therefore always with all knobs at 12 o'clock.
- **Lines from clocks of the MCU [code, measured, D60]:** the scan rate of the knob ADC of 105 633.8 Hz folds to 9633.80 and 19 267.6 Hz (acdc2: 9653.46 Hz), −116…−129 dB, almost independent of the knobs. [hypothesis] 2000.0002 and 3000.0003 Hz are multiples of the 1 kHz system tick.

**Otherwise:**

- The gain knob is a **digital** gain in the default patch [sourced]. With `TX_PRE_FX` (acdc1) it no longer acts on the recording.
- The noise drifts by 0.4 to 2 dB within a session (D44, D77). Comparisons between builds therefore need a control at the start and at the end.
- Gain of an ideal notch bank: 4–10 dB with the default patch (M1/M2, series 2, both modules), ≈ 5.8 dB with fx3l (D48), 1.6–3 dB with the ground wire (D90). The filter in the computer has therefore been dropped (`04-software-filter.md`).
- **Open:** listening test with a compressor at today's state, source of the knob lines, further ground pins. Everything in `TODO.md`.

## What is known in the forum [sourced]

**Thread #2072 "Clock noise in AC/DC"** is the only source with measurements.

- **atau** (2023-03 to 06):
  - Setup: 2020 MacBook Pro, macOS 10.15, a DAW, 48 kHz, FW v22.5.0, open inputs.
  - Noise pattern: **comb at k·1 kHz**, approx. **−30 dB at gain at 12 o'clock**, up to −18 dB at full gain.
  - Occurs on **two modules** (SN 191 and 250).
  - These had **no effect**: USB opto-isolator, other skiffs and power supplies, mechanical isolation, laptop on battery.
  - An ES-8 is clean in the same setup.
  - The bypass patch (bypasses the gain controls) changes nothing. So the interference is already in the ADC data.
- **mars (Martin Klang):** He said the levels are "definitely not normal". He announced measurement graphs, which never came.
- **antisvin:**
  - He can reproduce the 1 kHz comb, quieter in his case.
  - In addition he hears a noise with a period of approx. 0.8 s, possibly from the LEDs.
  - A block or pot artifact would be at **3 kHz** (48 kHz / 16 samples), not at 1 kHz.
- **Pauper** (2023-11-01, last post): "With a cheap ground isolator the noise desapears." Nothing more is said there. No model, no indication whether USB or audio isolator, and no statement whether streaming still worked afterwards.

**Further AC/DC reports:**
- selex (2022-11): very high noise floor.
- me (2024-11, thread #2244): two modules unused because of the noise floor.
- antisvin on this (2024-11): a hardware problem that "would require redesign to fix". He no longer expects any updates from Rebel.

**Sibling devices** (same company, different causes):
- Wizard: ground loop, an Olimex USB-ISO helped (#1104).
- Magus: 60 Hz hum with USB power (#1511). Switching off the LEDs removed noise (#1703).
- OWL pedal: USB power is noisy, an external power supply is better.

## Hypotheses on the cause

| # | Hypothesis | Expected signature | Test | Status |
|---|---|---|---|---|
| H1 | **USB Full Speed frame clock (1 ms)** couples into the codec inputs on the PCB (packet current spikes, ground bounce) | Lines at k·1 kHz, only with an **active USB stream** | Measurement plan step 6 (standalone cross-check) | **[measured]** S2-6 (f0 follows the host controller) and S3/D20: gone at the output without USB, **already present without a stream** (SOF alone is enough) |
| H2 | Classic ground loop to the host or via audio cables | 50/100/150 Hz + harmonics, possibly switching power supply whine. Changes with battery/isolator/ground lift | Steps 4 and 5 | **[measured] D20/D21:** ground loop only when the AC/DC is on the Mac port and output → second interface (UMC) on the hub. +20 dB, 59.98 Hz pulses (monitor on the hub), foreign comb 1000.03 Hz. Both devices on the same hub → gone. Not relevant in daily use (no AC/DC out → UMC) |
| H3 | LED PWM ≈ 2.32 kHz | Lines at ≈2.32 kHz and multiples, **level-dependent** | A patch that sets all LED parameters to 0 | **[measured]** Line and level dependence (M1–M3). Proven at the output with a patch that dims LEDs (D67). The LED current shifts the zero point of the inputs (D74), the PWM line is the same effect. In the LED mode off the shift drops to 1.7 % (D75), with the PWM at 48 kHz the line is gone (fx7a, D78) |
| H4 | Clock/SAI edges (OutputDrive on, 8 TDM slots) | Broadband rise or lines at clock dividers | only by firmware experiment | [hypothesis], untested. Both modules run with OutputDrive off and 4 slots (hack branch) [code]. The sample-synchronous fs/8 line belongs to H7 |
| H5 | USB TX rate control (shmuga bug, see 05) | **Click bursts** every few seconds in the recording, no stationary tone | Click detection in the measurement plan | **[measured] for the hack branch: not present.** 0 clicks in 360 s (series 2), in 10 min with the factory firmware (D6, D7) and with build 2 (D27). The shmuga bug concerns the USB path of v22.5.0, unchecked there. What was found instead is a bug in playback: block slips caused by feedback drift (D12–D18, fixed with patch 06) |
| H6 | Analog gain structure, high gain on a line signal | Broadband noise, scales with the knob | Gain series | [hypothesis]. The knob is a digital gain in the default patch [sourced], so the gain series says nothing about an analog stage |
| H7 | Two periodic digital activities couple into the ADC data and interact: audio block processing (fs/8) and the SOF clock | Line at fs/block size, mixing products n·f1k + m·fs/8, pattern period 1/(6·f1k − 6000) | Predict the pattern period, change code placement and block-rate activity | **[measured]** series 2 (period matched), D33 (placement in memory shifts all three families), D42 (activity at the block rate raises fs/8 by ≈ 10.6 dB), D48 (hot path in ITCM: fs/8 −5.1 dB, mixing products −35 dB). The physical path (current, ground, bus) remains [hypothesis] |

Ruled out: the 16-bit truncation alone, because it lies at approx. −96 dBFS, far below −30 dB.

## My own measurements M1–M3 (2026-11-13) → status of the hypotheses

This section shows the status after the first measurements. The current status of each hypothesis is in the table above.

Details, tables and limitations: `messlog.md`. In short: I have the 1 kHz comb, but **much quieter than atau** (−80…−96 dBFS at gain 12 instead of −30 dB).

| # | What the measurement says | Status |
|---|---|---|
| H1 | 1 kHz comb present, f0 = **1000.053 Hz**, so **not** sample-synchronous. Fits a clock outside the codec (USB SOF or a timer inside the module). Whether only with an active stream: not yet tested | Comb [measured], cause still [hypothesis] |
| H2 | 50 Hz only weak (−95 dBFS at g12). No pronounced 50 Hz family | probably not dominant [measured, preliminary] |
| H3 | Line at **2320.98 Hz** + 4641.95 Hz. Without signal at g12 gone (−110 dB), with signal or high DC offset −75…−80 dBFS. Frequency and level dependence fit the LED PWM | **supported** [measured], proof by an LED-off patch is missing |
| H4 | **Line at exactly 6000.00 Hz = fs/8** (+12/18 kHz), equally strong on all channels, sample-synchronous. acdc2 runs v22.4.q, where `AUDIO_BLOCK_SIZE 8` → audio callback at 6 kHz [code]. In addition **mixing products n·f1k + m·6 kHz** → the 1 kHz and 6 kHz interferers interact nonlinearly, pattern period ≈ 3.16 s | Lines [measured], block rate as the cause very plausible |
| H5 | No clicks visible in 7–10 s. Too short for a statement | open |
| H6 | Broadband residual (without comb/LED) −84 dBFS at g12. Rises with the digital gain | [measured], as expected |

**Correction to the interpretation of M2:** The gain knob is a **digital** gain in the default patch [sourced, see `research/notes/forum_noise_reports.md`]. That the interference lines rise more than the noise floor therefore does **not** prove that they couple in before an analog gain stage. It only shows that they are in the ADC data. The 16-bit floor after the patch does not rise with them. That the comb (+14…26 dB) and the LED line (+30 dB) rise **more** than DC and 50 Hz (≈ +9 dB) points to a level-dependent coupling [hypothesis].

**Series 2 (S2-1…S2-4), short version, details in `messlog.md`:**
- H7 (mixing products) **[measured]**: The pattern period was predicted and matched, acdc2 3.16 → 3.13 s, acdc1 1.247 → 1.24 s.
- **H1 [measured, S2-6]:** The comb depends on the **USB SOF of the host controller**. On the change Thunderbolt hub → Mac port it moved by +124.5 ppm (999.8663 → 999.9908 Hz), the module clock stayed the same. Without a USB connection it disappears completely at the output (S3, D20).
- Directly on the Mac a new hum family at 119.944 Hz is added. The hub is slightly quieter overall.
- At gain 0 the USB stream is digitally silent → no interference is added after the patch, everything is in the ADC data.
- acdc1 has the same line pattern (6 kHz → block size 8), but exactly 48 kHz instead of 47 991 Hz. Reason: the factory firmware of acdc1 had the clocking of v22.4.r [measured: disassembly, D10].
- H5 (clicks): no click in 360 s of recording.

**New mechanism (H7) [measured via the pattern period]:** Two periodic digital activities couple into the ADC data: the audio block processing (fs/block size) and a ≈1 kHz clock from another clock domain (presumably USB SOF). Where the two coincide, additional interference arises. Consequences:
- The block size determines the sample-synchronous lines. A change to block size 16 (v22.5.0) would change the line pattern. Both modules run with block size 8, the test is pending (E3 in `05`).
- The pattern period depends on the clock offset host ↔ module. antisvin's "0.8 s" fits this arithmetically.
- In pure standalone operation (no USB) the 1 kHz component together with the mixing products should disappear, but the 6 kHz line should remain. **Confirmed [measured, D20]:** Without USB only fs/8 and a weak fs/48 comb remain at the output.

**Consequence for the solution:** A notch bank at k·1000.05 Hz + k·2321 Hz removes ≈ 4–5 dB of noise power at gain 12, ≈ 10 dB at full gain [measured, calculation on M1/M2]. The residual is broadband.

## USB isolator: does it help?

**Status 2026-11-15 [measured, lab notebook D21–D23]:** No isolator is needed for my own setup. The only measured ground loop (AC/DC on the Mac port, output into the UMC on the hub) disappears when both devices are on the same hub. The daily-use chain (passive hub → monitor hub → TB hub) is as clean at output and inputs as the TB hub directly. An isolator does not remove the SOF comb at the inputs anyway (atau).

**In short:** A cheap test, but probably not the solution if I have the same 1 kHz comb as atau. For him the isolator changed nothing. It only helps with H2.

Steps 4 (battery) and 5 (ground lift) of the measurement plan have been dropped, no purchase is planned. Models and their suitability for Full Speed are in `research/notes/general_ground_loop_filtering.md`.

## Further hardware measures (if H2)

- Laptop on battery, no other cables on the computer (HDMI, hubs).
- Case and computer on the same power strip.
- Audio side: DI box with ground lift or transformer (ART DTI, Happy Nerding Isolator, Joranalogue Transmit 2).
- Ferrites, a different USB cable, a direct port instead of a USB-C hub.
- **Never** disconnect the protective earth.

## Status 2026-11-15: outputs, USB states, ground (lab notebook D19–D23)

- **SOF comb at the output [measured, D20]:** It is gone without USB and already present with USB plugged in without a stream. In standalone operation only these remain at the output: the fs/8 line (via the pass-through from the input), a weak comb **exactly at fs/48 = 1000.000 Hz in the module clock** (−105…−111 dB, **[hypothesis]** firmware-internal 1 ms activity) and 50 Hz mains.
- **Ground [measured, D21]:** see H2. The TB hub powers the Mac. Mac port and hub ports are therefore at different ground potentials **[hypothesis]**.
- **SOF frequency per port [measured]:** Mac port 999.99 Hz, TB hub 999.868 Hz (A5, monitor-hub chain) **or** 999.997 Hz (other port, G5), each in the acdc1 clock. A notch filter must measure f0 for each port.
- **Open inputs vary [measured, D22/D23]:** A single outlier brought +10 dB, broadband and low-frequency, 10 min later it was gone. Therefore record measurements with open inputs twice.
- **Mixing products in A5-b1d +4.7 dB against A5-b1b [measured, D19]:** It is the firmware, not the session (D24: 2 × A5 with 1d equal within ≤ 0.1 dB). Whether it is patch 05/06 itself or only the shifted code placement (D33) has not been separated. With fx3l it no longer matters.

## Status 2026-11-16: memory layout, ITCM, fx3l (lab notebook D24–D49)

All values on acdc1, raw inputs (`TX_PRE_FX`), open, daily-use chain, file dBFS, mean over 4 channels.

- **The placement of code and data in memory shifts the interference lines [measured, D33].** A padding build without functional change (+0x150 B) raises fs/8 by 1.8 dB and the comb by 1.5 dB and lowers the mixing products by 4.5 dB. An A/B between two builds therefore measures code **and** placement.
- **Hot path in ITCM [measured, D37, D48]:** fs/8 drops by ≈ 5 dB, the CPU load with a stream is halved (15 % → 6–8 %). The flash placement of the remaining code then no longer counts (padding variant fx3lp ≤ 0.25 dB for fx3l).
- **What the CPU does at the block rate appears at fs/8 [measured, D42].** A polling loop of a few µs on a DMA register per block raises fs/8 by ≈ 10.6 dB. Starting the block from the RX interrupt instead of the TX interrupt, in contrast, costs nothing (D44). **[hypothesis]** Bus traffic or a current pulse at the block rate couples into the ADC data.
- **The comb depends on the placement of the USB code [measured, D42, D44, D48].** USB code in flash with otherwise the same ITCM state: +2.5…+3.5 dB against 3d. USB code in ITCM: ±0…+0.4 dB. With no build has the comb fallen below the level of 3d.
- **The mixing products do not simply follow the levels of fs/8 and comb [measured, D42, D44].** In fx3j both are louder and the mixing products 10 dB quieter. **[hypothesis]** The phase relationship between block clock and SOF decides.
- **fx3l against 3d [measured, D48]:**

  | Quantity | fx3l | Δ against 3d |
  |---|---|---|
  | RMS ≥ 20 Hz | −72.7 | −1.1 dB |
  | Residual without interference lines | −78.5 | −1.25 dB |
  | Comb (SOF) | −74.6 | +0.2…+0.4 dB |
  | fs/8 | −83.4 | −5.1 dB |
  | Mixing products | −119…−120 | −34.8 dB |

- **Consequence:** The SOF comb is now by far the strongest line family and lies ≈ 4 dB above the broadband residual. The firmware has not lowered it. An ideal notch bank would gain ≈ 5.8 dB with fx3l (RMS −72.7 against residual −78.5 dBFS). Because the computer records the raw inputs, it would have to run in the computer. Whether that is worth it is open (optional, see `04-software-filter.md`).
- **Open:** Listening test with a compressor, second noise session with a 3d control at the start (D48 had none), lines at k·fs/48 (2000/3000 Hz), which fx3j, noD and fx3k showed (D42, D44) and which have not been evaluated for fx3l. Everything is in `TODO.md`.

## Status 2026-11-24: ground wire on the module (messlog D90)

- **Wire pin 15 (GND) ↔ pin 33 (AGND) on the back of the Xibeca module [measured, D90]:** acdc1, fx9a, open inputs, 2 × 60 s each on the same day. RMS −5.7 dB, residual −2.9 dB, comb −7.2 dB, fs/8 −18.3 dB, mixing products below detection, LED shift of the inputs down to 20–25 %. Gain unchanged (loop test +0.02 dB). Guide and background: `06-hardware-mod-ground.md`.
- **Mechanism [hypothesis]:** Return current of the module flowed through L1 and the AGND area to the carrier. The voltage across that path sat between the reference of the codec (AGND) and that of the input stage (carrier GND). All families that come from current pulses of the module drop together. This supports the hypotheses from D42 (current pulse at the block rate) and D74 (LED current shifts the zero point): the coupling path is largely the ground between module and carrier.
- **Did not move:** 7384.62 and 1215.19 Hz, the knob line at 4401.90 Hz. The scan line of the knob ADC (9633.80 Hz) rises by 3.7 dB but stays at −120 file dBFS.
- **Consequence:** The comb now carries 30–50 % of the noise power, fs/8 less than 1.5 %. An ideal notch bank would bring only 1.6–3.0 dB. The canceller `owl/include/AcdcInput.h` stays usable without changes, its benefit is smaller.
- **Output [measured, D91]:** through the UMC against D74 without the wire, comb −11 dB, fs/8 −12 dB, LED blinking −12.6 dB.
- **Open:** listening test, whether further ground pins (16 ↔ 47/48) or shorting L1 directly bring more. The A-B-A on acdc1 is dropped (desoldering too laborious), instead acdc2 later with a measurement before and after.
