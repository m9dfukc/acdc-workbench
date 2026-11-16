<!-- i18n source=docs/04-software-filter.md sha256=aecf5d6ab4962525fe40adc677b32c682ec33d8720f19ab6c2fa395e5b789712 date=2026-11-16 -->
> English translation of [`docs/04-software-filter.md`](../../docs/04-software-filter.md), as of 2026-11-16. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 04 – Software filter (notch bank)

Prerequisite: measurement plan steps 1–2 show a **stable, narrowband** comb, and f0 is measured.

**Status 2026-11-16:** None of this is built yet. The plan has shifted:
- With my own firmware (`TX_PRE_FX`, from Build 2 on) acdc1 records the **raw inputs**. A filter patch in the module (section 2) no longer reaches the recording [measured, lab notebook D25, B2]. It is only useful for modules with stock routing (acdc2, Build 1d).
- Filtering would therefore be done in the computer. **Optional** (user 2026-11-16), depending on how much interference noise is left in the end and whether it is worth it: a small **plugin that can be loaded with the "fingerprint" of the current module**, that is, with the exact frequency bands in which the interference lines lie. The analysis tool delivers the fingerprint per module and USB port. The design is open (`TODO.md`, "interference lines").
- With fx3l the SOF comb is the strongest remaining family. An ideal notch bank would give ≈ 5.8 dB (RMS −72.7 against residual −78.5 dBFS, D48).

## Which filter form?

| Variant | Problem | Verdict |
|---|---|---|
| FIR comb `y = x − x[n−48]` | Notches all k·1 kHz **and DC**, strong colouration. Destroys CV | for diagnosis only |
| IIR notch comb `(1+g)/2·(1−z^−N)/(1−g·z^−N)` | Narrow, but also a DC notch. N must be an integer, and in reality f0 is not | unsuitable |
| **Notch bank** (one biquad per harmonic) | No DC notch, f0 freely selectable, width adjustable per k | ✅ **choice** |
| Adaptive (LMS/PLL notch) | Follows a drifting f0. More effort | only if f0 drifts |
| Spectral subtraction (learning denoising plugins) | For broadband, can produce artefacts | offline/DAW |

At 48 kHz there are **23 harmonics** below Nyquist. The notch width should grow slightly with k, because small f0 errors multiply at high k. This applies all the more because the AC/DC really runs at ≈47 991 Hz and f0 in the file is not exactly 1000 Hz.

### Filter targets from my own measurements (M1–M3, see `messlog.md`)

| Family | f0 in the file | Harmonics | Note |
|---|---|---|---|
| 1 kHz comb | **1000.053 Hz** [measured] | k = 1…23 | At k = 23 the line is already 1.2 Hz away from 23 000 Hz. With a fixed 1000 Hz the bank would miss the lines at the top |
| fs/8 line | **6000.00 Hz** exact | 6, 12, 18 kHz | Separate family, lies 0.32 Hz next to 6 × 1000.053. Use separate notches or notch wide enough |
| LED PWM | **2320.98 Hz** [measured] | k = 1…9 | Only relevant with signal or high gain. Better solved at the source (LED off / shift the PWM frequency) |

Improvement according to M1/M2: ≈ 4–5 dB noise power at gain 12, ≈ 10 dB at full gain. Series 2 (open inputs): 4–10 dB.

**Important (S2-6):** f0 depends on the USB SOF of the host controller. Measured: acdc2 on the hub 1000.0528 Hz, acdc1 on the hub 999.8663 Hz, acdc1 directly on the Mac 999.9908 Hz. At k = 23 the variants are up to 4 Hz apart. It follows:
- A notch filter with a fixed f0 must be calibrated per module **and** USB port. The analysis tool delivers f0 to < 1 mHz.
- A filter that tracks f0 itself (adaptive/PLL) would be more robust. In the OWL patch the SOF clock is not known directly, but it could be estimated from the signal.
- Besides the comb there are mixing products n·f1k + m·6 kHz (≈ 3–5 % of the power) spaced a few tenths of a Hz apart. Slightly wider notches (≈ 1–2 Hz) cover them as well.

## 1. Python prototype (offline, for tuning)

In the analysis project under `analysis/notch.py`. Goal: tune the parameters (f0, width, count) on real recordings before the FAUST patch is written.

Specification:
- One `scipy.signal.iirnotch(w0=k*f0, Q=k*f0/bw_k, fs=fs)` per harmonic, with `bw_k = bw * (1 + 0.1*k)`. Cascade as SOS (`sosfilt`, numerically stable). In addition `sosfiltfilt` for the zero-phase offline variant.
- CLI: `uv run analysis/notch.py in.wav --f0 1000.13 --bw 3 --harmonics 23 -o out/in_notched.wav`
- Plot the before/after PSD overlaid. Output the RMS reduction and the remaining lines.
- Test signal: recording of a real audio signal (sine sweep, music) **with** noise. Do a listening test for colouration and plot the phase response of the bank.
- Carry the parameters that work well over into `docs/messlog.md`. They go into the FAUST patch.

## 2. FAUST patch for the AC/DC (slot 1)

**Only for stock routing (acdc2, Build 1d). On acdc1 from Build 2 on it has no effect on the recording, see "Status" above.**

With stock firmware the **patch output goes into the USB recording** (TX POST_FX). A filter patch therefore cleans the recording without a firmware change. Live monitoring via the DAC outputs stays unfiltered in interface operation, because the DAW playback overwrites the DAC.

```faust
import("stdfaust.lib");
// Notch bank against the USB frame comb, 4 channels, DC is preserved
f0   = hslider("f0 [OWL:A]", 1000.0, 995.0, 1005.0, 0.01) : si.smoo;
bw   = hslider("width [OWL:B]", 3.0, 0.5, 20.0, 0.1);           // Hz at k=1
gain = hslider("gain [OWL:C]", 1.0, 0.0, 4.0, 0.01) : si.smoo;  // replaces the gain of the default patch
NH   = 23;
bank = seq(k, NH, fi.notchw(bw * (1 + 0.1*k), f0 * (k+1)));
process = par(i, 4, *(gain) : bank);
```

Notes:
- The computing load is about 92 biquads × 48 kHz. That is uncritical on a Cortex-M7 at 480 MHz [hypothesis]. Check with `DEBUG_DWT` or the patch CPU figures.
- The knobs A–D act on the **input gain hardware and** on the patch parameters. The default VCA patch provides gain, a custom patch replaces it. That is why there is `gain` above.
- Better to enter **f0 fixed from the measurement** and use knob A only for fine tuning. A knob with 995–1005 Hz over a 12 bit ADC resolves about 0.0025 Hz, that is enough.
- FAUST toolchain: according to antisvin, the upstream OwlProgram is broken with newer FAUST versions. You need **antisvin's OwlProgram branch** (thread #2110/5). Whether the label syntax for parameters from `AA` on works upstream is unclear. A–D should work.
- Build and upload via OwlProgram: `make FAUST=NotchBank load` (RAM only, for testing) and then `store` with slot 1. Alternatively the web interface of the patch library (openwarelab.org).
- Test with `load` first, do not `store` right away.

## 3. DAW variant and plugin

This is the route for acdc1 if filtering is wanted. A custom plugin that loads the fingerprint of the module is optional (see "Status" above). Without a custom plugin:

- The same FAUST code as a plugin: `faust2vst`/`faust2au` or export via the Faust IDE. Put it on the input tracks.
- Ready-made plugins as an interim solution, three types:
  - Hum removers with freely selectable fundamental and harmonics. Open whether 1 kHz works as the fundamental and whether the number of harmonics is enough.
  - Spectral subtraction with a profile from a recording of silence.
  - Broadband denoisers.
  - Specific products: `research/notes/general_ground_loop_filtering.md`.

## Limits

- A patch cannot remove what is added at the DAC output or on the cables. It only sees the ADC data.
- Every notch also removes wanted signal at k·f0. For slow CV that does not matter, with audio and narrow notches it is hardly audible.
- If f0 drifts with load (measurement plan item 6), fixed notches fail. Then an adaptive approach is needed.
