# OwlProgram upstream after 2024 and a flag test for our patches (2026-11-27)

Question (user): https://github.com/RebelTechnology/OwlProgram – how does it overlap with the workbench, and what can we learn from it?

Method: `gh api` (commits, branches, PRs #125–#132, `compile.mk` and `HISTORY.md` on `develop`). Offline builds of the seven FX patches on acdc1 (slots 2–8) plus PlateauProfile with `tools/build_owl_patch.sh` (Arm GNU 12.2.Rel1), once with our SDK and once with a copy that uses the flags from `develop`. Disassembly with `arm-none-eabi-objdump`. No device access.

## Overlap

- OwlProgram is the patch SDK we already use: `tools/build_owl_patch.sh` builds every patch in `owl/` and `owl-patches/acdc-patches/` with it. Local copy `owl-patches/OwlProgram/` = `master` `60f44ab5` (2026-11-11, "ld: align _sidata and .data to 8 bytes") plus DaisySP `4263388`.
- `TestPatches/PatchRun.cpp` + `native.mk` run a patch on the host over a WAV file (macOS fixed in PR #130, whole WAV processed since `273b54dc`). Our `owl/test/run.sh` uses a minimal stand-in for `Patch.h` and targeted checks instead. PatchRun would be an addition for offline listening or for `analysis/`, not a replacement.
- Nothing in upstream is AC/DC-specific (only `04addfd`, 2021, AC/DC block size). Limiter wrapper, block-rate canceller and the LED findings stay ours.

## Upstream state [belegt: GitHub API]

- The repo was revived in October 2026 (maintainer pingdynasty). The earlier note in `openware_firmware_forks.md` ("last commit 3942f82, 2024-10-16") is outdated.
- `master`: Release **23.0** (2026-10-24, PR #125 "OwlLibrary API Updates": brings `master` up to the state of the online compiler since 2022, adds a `Dockerfile` that mimics the server: ARM GCC 9-2020-q2, FAUST 2.30.5), 23.1 fixes (PR #126), `60f44ab5`, `e7f70b50` (2026-11-18, CI only).
- `develop`: 45 commits ahead of `master`, 2 behind (2026-11-27). Merged into `develop`:
  - PR #129 (2026-11-17): LibSource unit tests for 17 classes, `SmoothValue::normalForSampleRate()`, fixes in TapTempo (per-sample clock) and WavetableOscillator (out-of-bounds read, negative-FM phase wrap).
  - PR #130 (2026-11-17): native, web and test builds on macOS.
  - PR #131 (2026-11-21, "Feature/bruckert"): Gen parameter/output maps; Faust `[scale:log]`, 48 widgets instead of 20, `faustmath.h` uses single FPU instructions for floorf/ceilf/sqrtf/rintf/roundf on Cortex-M7; PatchMetadata 40 parameters; web build pow/exp/log tables filled.
  - PR #132 (2026-11-26, "Perf/libsource locals"): **no `-fno-builtin` and no `-mtune=cortex-m4`** in `compile.mk`; block `generate()`/`process()` for AdsrEnvelope; state kept in registers in several LibSource filters and oscillators.
  - Also on `develop`: `-ffreestanding` dropped and `-D_GLIBCXX_USE_STD_SPEC_FUNCS=0` added (GCC 13+, same as OpenWare PR #89).
  - https://github.com/RebelTechnology/OwlProgram/pull/132 , https://github.com/RebelTechnology/OwlProgram/pull/131

## Flag test [gemessen am Rechner, 2026-11-27]

Our SDK compiles patches and libraries with `-nostdlib -nostartfiles -fno-builtin -ffreestanding -mtune=cortex-m4`, also for OWL3 (Cortex-M7). Both `-fno-builtin` and `-ffreestanding` (which implies `-fno-builtin`) stop GCC from expanding `fabsf`, `sqrtf`, `fminf`, `fmaxf`, `floorf` into FPU instructions; every use is a call into newlib.

Test: `owl-patches/OwlProgram-fpu/` = copy of our SDK, only the flag line replaced by the one from `develop` (`-nostdlib -nostartfiles`, no `-mtune`); libraries rebuilt with it. All eight builds made with both SDKs into separate folders (`WORK=owl-patches/_work-flagtest/<v>`, `OUT=owl-patches/builds-flagtest/<v>`, driver as in the table below; `WORK` is a new override in `build_owl_patch.sh`).

- **Baseline holds:** all eight `base` builds are byte-identical with the builds in `owl-patches/builds/` (the slot patches and PlateauProfile) (`owl-patches/builds/<name>/`).
- All `fpu` builds link without errors or new warnings.

| Patch (slot) | `patch.bin` base → fpu | calls to fabsf/sqrtf/fmaxf/floorf in `process*`, base → fpu | FPU min/max/abs/sqrt/rint instructions in `process*`, base → fpu |
|---|---|---|---|
| TapeDelay (2, LIMIT) | 30 036 → 29 404 B | 26 → 0 | 19 → 43 |
| Grainz (3, LIMIT) | 26 700 → 26 284 B | 17 → 0 | 11 → 26 |
| RingsReverb (4, LIMIT) | 21 556 → 21 156 B | 13 → 0 | 16 → 27 |
| Plateau (5, plusram) | 33 828 → 33 300 B | 11 → 0 | 68 → 79 |
| Tanh3 (6) | 18 580 → 18 452 B | 8 → 0 | 9 → 19 |
| SchliereS (7) | 18 156 → 18 068 B | 16 → 0 | 27 → 44 |
| SchliereL (8) | 22 948 → 22 908 B | 12 → 0 | 25 → 34 |
| PlateauProfile (test) | 29 644 → 28 900 B | – | – |

Whole binary: `sqrtf` calls go from 1–12 per patch to 0; `fabsf` calls from 11–31 to 0–4. The remaining 2–4 `fabsf` calls sit inside newlib itself (`tanhf`, `__kernel_tanf`, `__ieee754_rem_pio2f`), prebuilt, not affected by the flags. `memset` calls rise (GCC now turns zeroing loops into `memset`, mostly in init code). Tanh3 shows `expf` 2 → 12 call sites: the once-per-block level mapping (`(expf)(…)`, 4 channels) is unrolled, the number of calls at run time stays the same [Code].

## CPU load on the device [gemessen, D92, 2026-11-27]

acdc1, fx9a, no cables, no stream, knobs 63/64/71/50. Each patch run from RAM (`owl_write.py --run`) in the order base → fpu → base, three `owl_read.py` readouts each. Firmware CPU display (whole percent):

| Patch | base | fpu | Δ |
|---|---|---|---|
| Plateau | 29.3 % | 27.7 % | −6 % |
| Tanh3 | 50.3 % | 45.0 % | −11 % |
| SchliereS | 38.7 % | 35.0 % | −9 % |
| SchliereL | 70.7 % | 58.7 % | −17 % |
| TapeDelay | 31.5 % | 25.0 % | −21 % |
| Grainz | 13.0 % | 12.0 % | −8 % |
| RingsReverb | 15.3 % | 14.0 % | −9 % |

PlateauProfile: 2644–2668 → 2445–2483 cycles per sample (−7 %). Section o (14 taps) gets slower (236 → 279), all others faster; cause not examined. base was the same before and after fpu. Sound and output not compared yet.

## Adopted (2026-11-27, user)

Only the flag line, not the whole `develop` state: `owl-patches/OwlProgram/compile.mk` now equals the test copy (sha256 `7498a0c3…`), the original is kept as `compile.mk.orig-60f44ab`. `tools/build_owl_patch.sh` warns when `compile.mk` still sets `-fno-builtin`/`-ffreestanding`, rebuilds the libraries when `compile.mk` changes and writes `sdk_flags` to `BUILD_INFO.txt`. The eight builds in `owl-patches/builds/` were rebuilt and are byte-identical with the measured fpu builds. Slots 2–8 on acdc1 still hold the old builds.

Output check (D93, 2026-11-27): Out 1 → UMC, open inputs, old → new → old per patch, 30 s each. RMS of new within the two old runs (≤ 0.16 dB), third-octave bands inside the old spread ± 1 dB, no clicks, no new interference lines. No measurable difference at the output.

Stored (D94, 2026-11-27): slots 2–8 on acdc1 now hold the new builds, each read back byte-identical.

## What else to take from upstream

- `develop` as the SDK base instead of `master` `60f44ab`: flags (above) plus LibSource fixes. Our own patches in `owl/` use only `Patch.h` and `<math.h>`, the LibSource changes mainly matter for the `acdc-patches` (Grainz uses `SmoothValue.h`).
- FAUST: the TODO item says FAUST needs antisvin's OwlProgram branch. `develop` now contains Faust fixes, and the `Dockerfile` pins FAUST 2.30.5 as on the website. Possibly enough without antisvin's branch [Hypothese], not tried.
- `60f44ab5` (8-byte alignment of `_sidata`) is already in our copy.
