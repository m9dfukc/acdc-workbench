<!-- i18n source=docs/03-messplan-python.md sha256=6451967c6b475d9233c0e2bac769a21363cf7f9eb334c0c86d1b1494b0a8759f date=2026-11-16 -->
> English translation of [`docs/03-messplan-python.md`](../../docs/03-messplan-python.md), as of 2026-11-16. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 03 – Measurement plan & Python analysis (uv)

Goal: find out **whether I have the same 1 kHz comb as atau**, and which hypothesis from `02-noise-befunde.md` applies. Each step cuts off one branch of the hypotheses.

## Setup

```sh
uv init --no-workspace   # if not done yet
uv add numpy scipy soundfile matplotlib
# optional: uv add rich typer   (CLI convenience)
```

Folders: `recordings/`, `analysis/`, `out/`, `docs/messlog.md`.

## Recording rules

- **Tool from 2026-11-16 on:** `tools/acdc_rec.py` (see `CLAUDE.md` "Conventions", `--help`). For plain recordings it replaces the earlier chain of host software and multichannel recorder: duplex with zeros, 48 kHz, block 256, 4-channel WAV 16 bit, manifest entry with `scale = 2.0` (file dBFS as in the early recordings).
- **60 s** per measurement, WAV, **native 48 kHz**. `acdc_rec.py` writes 16 bit PCM, which is the USB format of the module. For recordings from a host software: 24 or 32 bit float. The first series (M1–M3) came as 96 kHz / 16 bit, so the recording software had upsampled it. Set the project sample rate in the recording software to 48 kHz, otherwise the conversion distorts frequencies and noise floor.
- Note for each measurement: module (acdc1/acdc2), which patch runs in slot 1, gain setting, USB state.
- Reference for the frequency axis: the 6 kHz line (= fs/8) is sample-synchronous. If it sits at exactly 6000.00 Hz in the file, the file is in the sample clock of the AC/DC and not resampled (M1–M3: yes).
- Inputs open or with a dummy plug (shorting jack), unless stated otherwise.
- Note the gain knob positions (e.g. `g07` = 7 o'clock, `g12`, `g17` = end stop).
- From step 6 on I need a **second, clean interface** as reference recorder (for the AC/DC outputs). Available: **Behringer UMC202HD**. Points to note:
  - Direction UMC → AC/DC (line level into the AC/DC input) is uncritical, e.g. a test tone for step 2b.
  - Direction AC/DC → UMC: the AC/DC outputs can deliver ±10 V, the UMC cannot take that. Connect only through an attenuator (passive or attenuator module) or at a level that is safely low.
  - The UMC is on the same Thunderbolt hub. If an audio cable is plugged between the two, an additional ground path is created. For step 6, note whether the computer/hub is connected to the AC/DC via USB while recording.
  - For step 2b the UMC also has its own clock error (unknown, typically a few 10 ppm). The test is therefore relative. Think the procedure through once more before measuring (`/grill-me`).
- Make the same recording with **both** AC/DCs too, so that differences between the units become visible.

## Measurement steps

| # | Test | File suffix | Conclusion |
|---|---|---|---|
| 1 | AC/DC → computer via USB, inputs open, gain at 12 o'clock, 60 s. In addition a gain series at 7/12/17 o'clock | `open-inputs_g12_usb-stream` | Gives the signature: lines at k·1 kHz → H1. At 50 Hz·k → H2. At ≈2.32 kHz·k → H3. Click bursts → H5. Broadband scales with gain → H6 |
| 2 | From step 1, determine the fundamental f0 exactly (peak interpolation) | – | With SOF coupling I expect about **1000.0–1000.2 Hz** in the file, not exactly 1000. f0 is also the filter parameter. **M1: 1000.053 Hz** [measured] |
| 2b | **Measure the real sample rate of the AC/DC:** feed a test tone from a reference interface (known frequency, e.g. 1000.000 Hz) into the AC/DC, record via USB. Deviation in the file = clock error of the AC/DC | `fs-check` | fs ≈ 47 997.5 Hz → comb is SOF-coupled (H1). fs ≈ 47 991 Hz → comb does not come from the SOF |
| 3 | Load a pass-through or bypass patch (bypasses the gain controls), record again | `bypass-patch` | Unchanged → the interference is in the ADC data |
| 4 | Laptop on battery, only the AC/DC on the computer, direct port | `battery` | Gone → H2 (host ground loop), then an isolator is worth it |
| 5 | Audio side: do the AC/DC outputs go into a grounded mixer? Break the loop with a DI with ground lift | `groundlift` | Gone → ground loop via the audio lines |
| 6 | **Standalone cross-check:** USB unplugged, patch in slot 1 runs. Record the AC/DC outputs with the reference interface, inputs open, gain high. Then plug in USB, start the stream (select the AC/DC as device in the DAW) and record again | `standalone_usb-off`, `standalone_usb-on` | Comb only with active stream → **H1 confirmed**. Nobody has done this test yet |
| 7 | LED test: patch that sets the LED parameters AA–AD and BA–BD constantly to 0 | `leds-off` | ≈2.32 kHz lines gone → H3 |
| 8 | Only now test the isolator (if 4 or 5 is positive) | `isolator` | – |

Record each step in `docs/messlog.md`: date, module, file, level of the top lines, conclusion.

**Status of the steps (2026-11-16):**

| # | Status | Evidence |
|---|---|---|
| 1 | done | M1/M2, repeated cleanly in series 2 |
| 2 | done | f0 = 1000.0528 Hz (acdc2 on the hub). f0 depends on the USB port (S2-6) |
| 2b | dropped | H1 is shown by S2-6. Clock ratio UMC/acdc1 = 1.000185 (D20) |
| 3 | dropped | Gain 0 → USB stream digitally silent (series 2). Raw inputs with Build 2 (D25/D26) |
| 4 | dropped | Mobile use does not occur (user 2026-11-15). Ground loop resolved (D21) |
| 5 | dropped | D21: ground loop only with the AC/DC on the Mac port and the UMC on the hub. In daily use there is no AC/DC out → UMC |
| 6 | done | S3 with Build 1d (D20): comb at the output gone without USB, already there without a stream |
| 7 | **open** | LED-off patch for H3 |
| 8 | dropped | No isolator needed (D21–D23) |

## Series 2 (next recordings, as of 2026-11-13)

Goal: repeat M1/M2 cleanly and answer the new questions (pattern period 3.16 s, firmware influence, SOF yes/no).

| # | Module | Inputs | Gain | Duration | File base | Question |
|---|---|---|---|---|---|---|
| S2-1 | acdc2 | open (nothing plugged in) | g12 | **120 s** | `<datum>_acdc2_open-inputs_g12_usb-stream` | Reference: f0, mixing products, 3.16 s period, clicks |
| S2-2 | acdc2 | open | g17 | 60 s | `…_acdc2_open-inputs_g17_usb-stream` | Gain dependence, LED line |
| S2-3 | acdc2 | open | g07 | 60 s | `…_acdc2_open-inputs_g07_usb-stream` | What remains at minimum digital gain? |
| S2-4 | acdc1 | open | g12 | 120 s | `…_acdc1_open-inputs_g12_usb-stream` | Different unit, possibly different firmware/block size → different line pattern? Note the device status (firmware, patch) |
| ~~S2-5~~ | – | – | – | – | – | Dropped: no second computer available (2026-11-13). Replacement: S2-6 and S3 below |
| S2-6 | acdc1 (acdc2 was planned) | open | g12 | 119 s | `20261114_acdc1_nohub_open-inputs_g12_usb-stream.4chan.000.4chan.000.wav` (planned: `…_usb-direct`) | **AC/DC directly on a USB port of the Mac instead of on the Thunderbolt hub.** Different USB controller → different SOF clock. If f1k (1000.0528 Hz) shifts, the comb is SOF-coupled |

As of 2026-11-13: S2-1 to S2-4 and S2-6 recorded and analysed (see `messlog.md`). Device status of both modules noted.

**S3 – USB states via the UMC202HD. Status 2026-11-15: measured with Build 1d (lab notebook D20)**, single channel (Out 1), plus state d (duplex), result: SOF comb gone without USB, ground loop dominates with USB. Original status 2026-11-14: not measurable with the firmware of that time, because the outputs are silent without computer playback (see `messlog.md`, "pass-through"). Clarify the pass-through first, if necessary with my own firmware (phase 5). Planned setup from the `/grill-me` round: acdc1 directly on the Mac, inputs open, gain 12; Out 1/2 → MTM Startup (L/R, level set to line) → Y cable → UMC In 1/2 (LINE, gain fixed); recording in the host software; state (c) via a recording app (input only), because the host software opens the AC/DC in both directions; Startup and UMC levels fixed; order S3-0 (UMC alone), b, c, a, b2 at 120 s each.

Original idea: record the AC/DC outputs with the UMC through an attenuator, in three states:
- (a) USB cable of the AC/DC unplugged,
- (b) USB plugged in, but no stream (no software uses the AC/DC),
- (c) AC/DC inputs stream via USB.

Expectation with SOF coupling: 1 kHz comb and mixing products gone in (a), the 6 kHz line stays. If the comb is already there in (b), the SOF alone is enough, otherwise it takes the iso data traffic. Open before measuring: attenuator, DAW routing for (c) (in stock firmware active USB playback overwrites the DAC), ground path via the audio cable. Go through it with `/grill-me` first.

Recording settings for series 2 and S3 (host software, before `acdc_rec.py`): project **48 kHz**, recording format **32 bit float** (or 24 bit), **one 4-channel WAV** per measurement (or 4 mono files `_ch1…_ch4`), no plugins/effects on the input tracks, no dither on export. Then an entry in `recordings/manifest.toml` (ID S2-1 …) and `uv run python -m analysis S2-1`.

## Analysis tool (`analysis/`) – implementation

As of 2026-11-13: items 1–9 of the specification below are implemented.

```sh
UV_CACHE_DIR=.uv-cache uv run python -m analysis M1            # manifest ID
UV_CACHE_DIR=.uv-cache uv run python -m analysis M2 --ref M1   # with reference overlay + Δ table
UV_CACHE_DIR=.uv-cache uv run python -m analysis aufnahme.wav  # a file directly
UV_CACHE_DIR=.uv-cache uv run python -m analysis.selftest      # self-test with a synthetic signal
```

Output in `out/<name>/`: `_report.md`, `.json`, `_spectrogram.png`, `_psd.png`, `_combs.png`, `_timeline.png`.

| Module | Contents |
|---|---|
| `audio_io.py` | Load WAV/manifest, assemble channels, remove DC. The manifest field `channels = [1, …]` (1-based) selects channels, e.g. to leave out empty channels (since 2026-11-15) |
| `spectra.py` | Full-length Hann FFT, parabolic peak interpolation, local noise floor (median), Welch, A-weighting |
| `lines.py` | Families fs/8, 1 kHz, LED, mains + strongest remaining lines, weighted f0 fit, mixing products n·f1 + m·f2, power shares by Parseval |
| `timing.py` | f0/level in windows (default 10 s), envelope modulation, click detector |
| `plots.py`, `report.py` | Figures, Markdown, JSON |
| `selftest.py` | Synthetic signal with known lines, mixing products, clicks. Checks f0 < 5 mHz, level ± 0.5 dB |

More analysis and module tools are in `tools/` (recording, loop check, family tables across several measurements, module report). The overview is in `CLAUDE.md`, section "Tools in `tools/`".

Limits: two lines can only be separated from a spacing of ≈ 4 bins (bin = 1 / duration). At 10 s that is 0.4 Hz, and the mixing products spaced 0.316 Hz apart then merge. Therefore record ≥ 60 s.

## Specification for the analysis tool (`analysis/`)

Original specification of 2026-11-13, implemented except for the item "RMS after notch bank" (comes with `analysis/notch.py`, see `04`). Invocation and file names are in the section "Implementation" above.

A CLI script, e.g. `uv run analysis/noise.py recordings/<file>.wav --channel all`. It should deliver the following:

1. **Spectrogram** (I already have that). Recommendation: STFT with Hann window, nperseg 8192–16384, log frequency axis 20 Hz to 24 kHz, dBFS scale. This makes patterns in time visible (clicks, 0.8 s period, drift).
2. **Long-term PSD** (Welch, `nperseg=65536` or larger, Hann) → `out/<name>_psd.png`, log x, dBFS/√Hz or dBFS per bin. Optionally overlay a reference file (`--ref`) on the same axis, for A/B comparisons.
3. **Peak list**: the top N lines above the median noise floor (e.g. +10 dB), with **parabolic or quadratic interpolation** on the log magnitude spectrum, so that the frequency is accurate to <0.05 Hz. Output as JSON and Markdown table: frequency, level in dBFS, distance to the floor.
4. **Harmonic detection**: tests the candidate fundamentals 50, 60, 1000 and 2320 Hz and the fundamental of the strongest line. For each one the "comb profile" is determined: level at k·f0 (k = 1…⌊24000/f0⌋) and the share of the energy in the comb in the total noise. Result: which family dominates?
5. **f0 fit**: least squares over all harmonics found (f_k ≈ k·f0) → precise f0 + residuals. Important for the notch filter, because otherwise the upper harmonics are missed.
6. **Stability over time**: f0 and level in 5 s windows. Does f0 drift? Does the level fluctuate periodically (LED, 0.8 s)?
7. **Click detection** (for H5): high-pass at about 5 kHz, envelope, threshold, intervals between events. Regular intervals of a few seconds (e.g. ≈3.9 s) point to the USB TX rate error.
8. **Key figures per channel**: total RMS (dBFS), RMS after notch bank (see `04`), A-weighted optional. This tells how much of the noise the comb accounts for.
9. **Report** `out/<name>_report.md` with the plots and tables, for pasting into the lab notebook.

Notes:
- The AC/DC recording via USB is 16 bit, the floor is at about −96 dBFS. Lines at −30 dB are therefore far above it.
- Analyse all 4 channels separately. With coupling on the board the levels often depend on the channel.
- Remove the DC offset before the FFT (the AC/DC is DC-coupled).

## Decision tree after the measurements

```
Comb k·1 kHz?
├─ no → 50 Hz family? → ground loop (H2) → battery/ground lift/isolator (02)
│        └─ 2.32 kHz? → LED PWM (H3) → LED patch / move firmware PWM (05)
└─ yes → step 6: only with USB stream?
         ├─ yes (H1) → isolator pointless → notch patch (04) + standalone firmware (05)
         └─ no → coupling inside the module, independent of USB → notch patch (04), firmware experiments H3/H4
Click bursts? → backport shmuga fixes (05)
```

**Result (2026-11-15) [measured]:** comb yes → step 6: at the output it is gone without USB and already there without a stream (D20). That is branch H1: an isolator is pointless, continue with firmware (`05`) and filter (`04`). There were no click bursts (D6, D7, D27).
