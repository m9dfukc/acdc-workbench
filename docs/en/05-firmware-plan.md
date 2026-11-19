<!-- i18n source=docs/05-firmware-plan.md sha256=7e9e1aaeb1ee239473ef98b21d2b2835f9ab84fa2a503cf191d912959a86e2c2 date=2026-11-19 -->
> English translation of [`docs/05-firmware-plan.md`](../../docs/05-firmware-plan.md), as of 2026-11-19. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 05 – Firmware: Status, Forks, Build Plan

> **Status 2026-11-19:** acdc1 runs **Build 9 `v22.4.r-fx7a`** (`cac6fee0…`, section "Build 9", lab notebook D78, D79) as its daily firmware (the user's decision). The fallback is Build 8 `v22.4.r-fx6a` (`6a3fc427…`), then Build 7 `v22.4.r-fx5a` (`b69c25b3…`), Build 6b `v22.4.r-fx4b` (`a21f35c9…`), Build 5c `v22.4.r-fx3l` (`b55b94d8…`), then Build 3d (`d212cf8d…`).
>
> This document grew chronologically. "Runs on acdc1", "not agreed" and "next steps" in the sections on Build 1 to 4z describe the status of the respective section. What is open today is in `TODO.md`.

## Upstream status [sourced]

- `RebelTechnology/OpenWare`: `develop` = `62a0187` "v22.5.0", **2023-03-05**, this is the last firmware revision. Last commit under `ACDC/`: `dd7f7fe` (2022-06-19).
- **Addendum 2026-11-16:** `master` has been at `36eaf1c4` since 2026-11-15 (PR #89, build flags for GCC 13+, CI on GCC 14.3). The 4 new commits change only the build chain, no firmware code. `d5b6409a` is taken over as patch 08. Details: `docs/research/notes/upstream_master_2026-11-16.md`.
- Later branches: `feature/oneiroi` (until 2025-06, Befaco Oneiroi), `feature/witch3` (2023-10). None of them concerns the AC/DC.
- Issue tracker: 88 entries, **no** AC/DC issue from users, 0 hits for "noise". Open PR #81 (antisvin): saving settings from the USB ISR can hang.
- According to antisvin, the official `ACDC.bin` v22.5.0 **broke USB**. A self-built version with the matching `Libraries` submodule worked (thread #2083).
- June 2026: on some Xibeca boards USB audio fails after a while (thread #3725).
- In effect the module is orphaned. Firmware updates for the AC/DC are not to be expected from Rebel.

## What is relevant in forks and branches

| Source | Content | Use |
|---|---|---|
| **shmuga/OpenWare `lich3-usb-fixes`** (2026-10-18) | `d8fdfa3`: On H7, an incomplete isochronous IN transfer shuts the TX endpoint down **permanently**, and the host then hears only silence (the H7 HAL behaves differently from the F4 HAL). `c5aff8c`: The TX rate control misestimates the fill level, which produces **click bursts every few seconds**. `d39aa53`: crash caused by `__builtin_clz(0)` with GCC 12. `9104f1a`: 3 → 5 buffer packets (Lich3) | Backport candidate for **Option A** (v22.5.0 line, E1). In v22.5.0 the AC/DC uses the same `Source/usbd_audio.cpp` with TX on H7 and also has 3 packets. The hack branch has its own USB path. Untested on the AC/DC |
| **burstMembrane/OpenWare `20d322d`** (2026-03-31) | The only fork with an ACDC change: both `*_PRE_FX` defines, product string "LIAM-ACDC", `Libraries` submodule at `5a3f964` ("fix usb device enumeration") | Precedent. `5a3f964` = old H7 HAL before the upgrade (see "Libraries revisions"), template for Option A |
| Upstream `hack/acdc-output-levels` (`7f3cc41`, 2022) | Martin Klang's unmerged experiments: exact 48 kHz (MCLK 12.288 MHz), codec auto rate, **SAI OutputDrive off** (`65fc0db`), **only 4 TDM slots** (`cf8eaf9`), input gain 88, block size 8, 4 buffer packets, level LEDs | **Base of all my own builds** (E1, since D10 the revision `db9d3dd` = v22.4.r instead of the tip), only without `237c63d`: that commit mutes the DAC without a USB stream, the opposite of standalone. A build from this branch ran on acdc1 from the factory (labelled "v22.5.0"), v22.4.q runs on acdc2 |
| Upstream `feature/acdc-lowspeed` (`237f746`) | CPU at 240 MHz, SAI retuned. FRACN values inconsistent (`.ioc` 280 vs. `main.c` 6144) | do not build unchecked |
| hirnlego, XponentOneAudio, antisvin/OpenWare_Owlsy | Oneiroi storage fixes, Lich patches, Daisy port | nothing for the AC/DC (checked as of 2026-11-14) |
| **burstMembrane/acdc-patches** (`78ffa22`, 2026-04-02) | Ready-made AC/DC FX patches (Dattorro reverb, tape delay, grain, Rings reverb) + helper `ACDC.h` (audio L/R = channel 1/2, CV = 3/4, LED metering), matching the PRE_FX firmware `20d322d` | Template for phase 4 (standalone FX) [sourced: repo] |
| **shmuga/lich-patcher** (2026-10-18, https://lich.markorel.ninja/) | Browser tool, general OWL SysEx: slot/resource **download from the module**, **reading out settings**, module info | Backup of acdc1/acdc2 before every intervention, check settings (read only, no erase/store) |

No source addresses the analog noise, the PCM3168A driver or the LED PWM.

## Finding 2026-11-14: pass-through without a computer is missing on both modules

- acdc2 (v22.4.q) contains `237c63d` (zeros to the DAC without USB playback) [code].
- acdc1 ("v22.5.0") does not pass audio through after a cold start either [measured]. Cause according to D3: acdc1 runs a build from `hack/acdc-output-levels` with the label "v22.5.0", not the release `ACDC.bin` [measured: readback + string fingerprint, `messlog.md` D1–D3]. The hack branch contains `237c63d`.
- Consequence: standalone FX is only possible with my own firmware.
- The source code is kept permanently under `firmware/OpenWare` (one clone with remotes `upstream` and `fork`, all branches as `upstream/*`). In the sandbox, Git write access is blocked there (`.git/config`); cloning and fetching need approval. The `Libraries` submodule is **not** checked out there.

## Facts for my own build (2026-11-14)

### `Libraries` revisions (pingdynasty/OpenWareLibraries) [sourced: repo + GitHub compare API]

| Revision | Date | Content | Who uses it |
|---|---|---|---|
| `5a3f964` | 2022-03-24 | OpenWare commit `ad6422f2` "revert libs to prevent USB issues" (before that already `2185efd2` "latest libs") | burstMembrane `20d322d` |
| `9e8f64e` | 2022-03-25 | = `5a3f964` + 1 commit "apply NAK fix to H7 drivers", only `stm32h7xx_hal_hcd.c` (+8). Affects only USB **host**, so practically the same for the AC/DC as a USB device [code] | OpenWare `05dc03e0` "patched library". From there on all v22.4.x, all v22.5.rc* and `hack/acdc-output-levels` |
| `8a07845` | 2023-01-29 | Upgrade to **STM32H7 HAL v1.11.0**, CMSIS 5.1.0, middlewares, USB host fixes (300 files) | OpenWare `8c569c0e` "Updated H7 libs", 2023-03-05, release tag |
| `e102c6f` | 2023-03-05 | = `8a07845` + CMSIS F4 headers | v22.5.0 `62a0187` |

- The USB breakage of the release `ACDC.bin` (antisvin, thread 2083 #4) coincides exactly in time with the HAL upgrade `8a07845`/`e102c6f` [hypothesis, strong]. Fitting this, `3237e7ca` (2023-01-29): build flags in `Hardware/owl3.mk` adapted to the new HAL. A v22.5.0 build with the old HAL may need this commit reverted [hypothesis]. **Addendum 2026-11-16:** Not needed for the AC/DC, it builds with `xibeca.mk` instead of `owl3.mk` [code]. `master` + old HAL `9e8f64e` builds and links without the revert (`cand-master-oldhal-fx`) [measured: build].
- So the firmware on acdc1 (hack branch) runs with the **old HAL** `9e8f64e`, and its USB works [measured: in operation for months, series 2].

### Hack branch vs. v22.5.0 [code]

- Base: `hack/acdc-output-levels` branches off at `dd7f7fe` and merged `develop` several times until 2022-06-19. Tip `7f3cc41` "v22.4.s: MCLK=256fs no master div" (2022-07-15). `Source/device.h`: `FIRMWARE_VERSION "v22.4.s"`.
- Only in the hack branch: reworked USB audio path (SOF sync, feedback calculation, `CircularBuffer`, buffer init on a frame boundary, unified `usbd_audio_error()`), block size 8, input gain 88, MCLK 256fs/exact 48 kHz (`bc7391cd`, `e219182a`, `7f3cc41`), SAI OutputDrive off (`65fc0db`), 4 TDM slots (`cf8eaf9`), level LEDs, `codec_highpass()`, **`237c63d`**.
- Only in v22.5.0 (56 commits): Lich3/Magus3/Witch3, USB host, watchdog, settings in unmapped flash, "Ensure valid DAC value range", HAL upgrade. Almost all of it is irrelevant for the AC/DC.
- `237c63d` is an `else` branch in `usbd_rx_convert()` with `memset(dst, 0, …)` under `#ifdef OWL_ACDC`: without an active RX stream, zeros go to the buffer. The revert is trivial.
- `USE_USBD_AUDIO_TX_PRE_FX` / `_RX_PRE_FX` are implemented the same way in both revisions (`Source/ProgramManager.cpp`): POST_FX converts `pv->audio_output`, PRE_FX `pv->audio_input`.
- Which revision runs on acdc1: **no published commit** (reproduction build, `messlog.md` D3a). `ProgramManager.cpp` with `237c63d` comes from the hack branch [measured: disassembly], `usbd_audio.cpp` matches no hack commit. Probably a self-assembled revision, built with GCC < 12 [hypothesis, strong]. Which MCLK configuration it uses remains open. That acdc1 has almost exactly 48 kHz points to ≥ v22.4.r [hypothesis].

### Settings [code]

- `ApplicationSettings` has the same structure in both revisions. The checksum is `sizeof(*this) ^ 0xf0f0f0f0`. An existing `__SETTINGS__` would therefore be **taken over** by every new build.
- There is probably no `__SETTINGS__` on acdc1 [hypothesis]: the reported usage of 31 232 B is exactly slot 1 (10 164 B) + slot 2 (20 724 B), each with a 32-B header and rounded up to 256 B. However, `getUsedSize()` only counts resources with `FLASH_DEFAULT_FLAGS`, so this is no proof. Block size 8 is the default in the hack branch anyway.

### Toolchain and size

- Upstream CI (`.github/workflows/c-cpp.yml`, v22.5.0): `carlosperate/arm-none-eabi-gcc-action`, Arm GNU **12.2.Rel1** [sourced: repo]. Installed since 2026-11-14 under `/Applications/ArmGNUToolchain/12.2.rel1/`.
- Sizes: acdc1 readback 106 608 B, release 109 080 B, limit 131 072 B (128 KB internal flash according to the build config).

## Agreed plan (review round 2026-11-14)

Decided with the user in two rounds of questions. **No build and no flash without explicit approval in the chat, each flash individually. acdc2 stays untouched.**

### E1 – Base: hack tip instead of v22.5.0

- **Build 1 = `7f3cc41` (v22.4.s, tip of `hack/acdc-output-levels`) + Libraries `9e8f64e`, only `237c63d` reverted.**
- Reason: this is closest to the revision that runs on acdc1 today with working USB (old HAL, hack USB path). This keeps the USB risk smallest, and the pass-through can be tested in isolation.
- Deliberately the **tip** and not the commit that comes closest to the readback (user decision). The reproduction build has shown anyway that no such commit exists (D3a). So Build 1 differs from acdc1 in more than the revert: USB error paths in `usbd_audio.cpp`, compiler, possibly MCLK. Deviations in A5/A6 are then to be attributed to these differences first.
- v22.5.0 with release Libraries `e102c6f` is ruled out (USB breakage).
- **Addendum (D10, 2026-11-14):** Build 1 on the tip `7f3cc41` gives no audio on acdc1 (clock and codec setting of v22.4.s). All later builds are therefore based on **`db9d3dd` (v22.4.r)**. This is also the clock setting of the factory firmware of acdc1 [measured: disassembly].
- **Option A (stays on the plan for later, user 2026-11-16: merge with v22.5.0 or with the current upstream `master` including fixes):** v22.5.0 + Libraries `9e8f64e`/`5a3f964` (like burstMembrane), **plus the shmuga USB fixes** (`d8fdfa3`, `c5aff8c`, `d39aa53`, 5 buffer packets from `9104f1a`), with `TX_PRE_FX`. The shmuga fixes belong to this line because they are written against the v22.5.0/Lich3 USB code. The hack branch has its own reworked USB path; there they would be a port, not a cherry-pick.
  - The revert of `3237e7ca` mentioned earlier is dropped: the commit changes `owl3.mk`, the AC/DC builds with `xibeca.mk` [code].
  - According to the upstream analysis (`docs/research/notes/upstream_master_2026-11-16.md`), the switch is a port: the clock of v22.4.r, patches 04/05/06/07d and the ITCM patches would have to be carried over to the USB path of v22.5.0 and acceptance-tested again. Groundwork: patches 09 and 10, candidates `cand-r-merge2250-fx2d` and `cand-master-oldhal-fx` (built, not flashed).

### E2 – Routing in two stages

| Build | Change relative to the hack tip | Without computer | With computer: recording | With computer: playback |
|---|---|---|---|---|
| **1** `v22.4.s-thru1` | only revert `237c63d` | patch → jacks | patch output (as before, digital gain included, comparable with M/S2) | overwrites the outputs as long as the RX stream runs |
| **2** `v22.4.s-fx1` | + `USE_USBD_AUDIO_TX_PRE_FX`, product string "OWL-ACDC-FX" | patch → jacks | **raw ADC data**, without patch and without digital gain | as Build 1 |

- Both PRE_FX (burstMembrane) discarded: with `RX_PRE_FX` the playback overwrites the patch **input**; the input jacks would be gone while playback runs [code].
- Open [hypothesis]: if macOS keeps the output stream open as long as the AC/DC is selected as the output device, the outputs are silent during that time (host silence overwrites the patch). According to the code, RX only stops on SetInterface Alt 0 or USB DeInit. This is observed in A4.
- Auto-switching at runtime (tying the routing to `usbd_rx != NULL` or to the level) only after Option A.

### E3 – What stays from the hack branch

In Build 1 and 2 everything stays as it runs on acdc1 today: block size 8, input gain 88, output gain 114, MCLK/exact 48 kHz, OutputDrive off, 4 TDM slots, 3 buffer packets, level LEDs, codec HPF off. This way every step remains a single variable.

Later noise experiments, each as a separate build with an A/B measurement against the Build 2 baseline:
1. Block size 16 → the 6 kHz line (fs/8) should move to 3 kHz (fs/16), and the mixing products should change.
2. LED PWM out of the audio band (prescaler 100 → 0, ≈ 234 kHz) → H3.
3. Codec HPF on (`CODEC_HP_FILTER`).

We set the order after Build 2.

### E4 – Settings

Never write, never reset (no SysEx `0x15`, no store). Read out with `tools/owl_read.py` before and after every flash: version, `SR/BS/CH`, slot names and CRCs, storage. In case of deviations, ask first.

### E5 – Toolchain and build tree

- Arm GNU Toolchain **12.2.Rel1**, like upstream CI. The user does the installation (Arm tarball or package manager). The version goes into every build log.
- No build in the clone `firmware/OpenWare`, because Git write access is blocked and the clone should stay clean. Instead:
  - `git archive <commit>` to `firmware/_work/<name>/`
  - Libraries as a GitHub tarball of the fixed commit (`codeload.github.com/pingdynasty/OpenWareLibraries/tar.gz/9e8f64e…`) to `firmware/_work/<name>/Libraries/`
  - my own changes only as `firmware/patches/NN-<name>.patch` (`01-gcc12-extern-uint8`, revert `237c63d`, later `TX_PRE_FX` + product string). The version string is set by `FW_VERSION=…` in the script.
  - `.git*` files are skipped when unpacking, because the sandbox blocks `.gitmodules` and the build does not need them.
- `tools/build_acdc.sh <commit> <libraries> <patch…>`: set up the tree, apply the patches, `make` for ACDC, check `arm-none-eabi-size` against 131 072 B. Then write `.bin`/`.elf` with SHA-256, toolchain version and patch list to `firmware/builds/<name>/`.
- **First the reproduction build:** hack tip unchanged, only the version string set to "v22.5.0", comparison with the readback. Done 2026-11-14, result see below. It is not flashed.
- The `__builtin_clz(0)` case (shmuga `d39aa53`) concerns code from v22.5.0/Lich3. For the hack base it is only pulled in if it occurs there.

#### Result of the reproduction build (2026-11-14)

- Toolchain and script work. For GCC 12 the hack sources need the patch `01-gcc12-extern-uint8.patch`: upstream `5108fc56` + `fe6eff4f`, changes only the types of linker symbols (`extern char` → `uint8_t`). Without it GCC 12 aborts with "conflicting declaration '_PATCHRAM'". `develop` from v22.5.rc2 on already contains the fix.
- **Builds are deterministic [measured]:** two runs for `7f3cc41` (once with a version patch, once with `FW_VERSION`) give the same SHA-256.
- Stored in `firmware/builds/archive/repro-*/` (`ACDC.bin`/`.elf`/`.map`, `BUILD_INFO.txt`, `build.log`), all with `FW_VERSION=v22.5.0`, **not for flashing**:

| Build | Commit | Size B | SHA-256 (start) |
|---|---|---|---|
| `repro-7f3cc41` | Hack v22.4.s | 105 664 | `910f71e3…` |
| `repro-db9d3dd` | Hack v22.4.r | 105 664 | `1fce4352…` |
| `repro-e81cfc3` | Hack v22.4.q (= acdc2 source) | 105 632 | `cb1c2d0e…` |
| `repro-961b49f` | Hack merge 2022-06-19 (v22.4.m) | 104 296 | `924bc72b…` |
| `repro-c79cf7a` | `develop` v22.5.rc5, without GCC patch | 104 288 | `f1d3026c…` |
| Readback acdc1 | ? | 106 608 | `433b3fd3…` (128 KB image) |

- No candidate matches the readback. The firmware on acdc1 is not a published commit; `237c63d` is proven in it by disassembly (`messlog.md` D3a). Plan E1 (hack tip + revert) stands.

#### Build 1 and Build 2 built (2026-11-14, not flashed)

Built with `tools/build_acdc.sh`, base `7f3cc41` + Libraries `9e8f64e`, Arm GNU 12.2.Rel1. Stored today in: `firmware/builds/archive/acdc1-build{1-thru1,2-fx1}/`. The source trees are deleted; a rebuild is reproducible bit for bit.

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` |
|---|---|---|---|---|
| `acdc1-build1-thru1` | `v22.4.s-thru1` | 01, 02 | 105 656 | `97a876b45512e23cbc019e721601bb70de38fb9e056b72b0928f1a0c12c4f332` |
| `acdc1-build2-fx1` | `v22.4.s-fx1` | 01, 02, 03 | 105 656 | `3a6e5df63751f32ee821b3cbda8705519f6e11667ffde708fb27b24ceda18289` |

Patches in `firmware/patches/`:
- `01-gcc12-extern-uint8.patch`: GCC 12 compatibility, types only
- `02-revert-237c63d-thru-mute.patch`: removes the `else` branch with `memset` in `usbd_rx_convert()`
- `03-tx-pre-fx-owl-acdc-fx.patch`: `USE_USBD_AUDIO_TX_PRE_FX`, product string "OWL-ACDC-FX"

Checked in the binary [code: disassembly of the ELFs]:
- **Build 1:** `usbd_rx_convert()` now contains only one `memset` (underrun fill), the tail call `memset(dst,0,…)` for `usbd_rx == NULL` is gone. In the repro tip there are 2. `onProgramReady` calls `tx_convert` and `rx_convert` at the start on `audio_output`, so POST_FX as before. Strings: "OWL-ACDC", "AC/DC v22.4.s-thru1".
- **Build 2:** like Build 1, but `tx_convert` is only called at the end of `onProgramReady` as a tail call, on `audio_input` before the next patch block (PRE_FX). `rx_convert` stays POST_FX. Strings: "OWL-ACDC-FX", "AC/DC v22.4.s-fx1".
- Vector table as in the readback (SP `0x00001000`), size well below 131 072 B.

Next steps before the first flash (E7): boot pad probe, 10 min reference recording, dry run. All only with approval. **Status 2026-11-14: all three done** (lab notebook D4, D5, D6/D7).

### E6 – Identification

- Version string: Build 1 `v22.4.s-thru1`, Build 2 `v22.4.s-fx1`. Never again "v22.5.0" on one of my own builds.
- USB product string: Build 1 stays "OWL-ACDC", so that `owl_read.py`, audio software and macOS keep running unchanged. Build 2 is called "OWL-ACDC-FX", the device name in the system then shows the routing.
- **Addendum 2026-11-15:**
  - Build 2 is now called `v22.4.r-fx1d` (base 1d, see "Build 2 new").
  - `owl_read.py` already finds "OWL-ACDC-FX" today, because `--port` searches by substring.
  - Audio software on the computer has to select the device again.

### E7 – Flash route, preconditions, fallback

- Route: ROM DFU via the **front USB-B jack**. Entry with `tools/owl_read.py --reset-to-dfu --yes`, then `dfu-util -a 0 -s 0x08000000:leave -D <bin>`. We check the exact command before the first write. **Addendum:** Since D5, flashing is done **without** `:leave`, with a readback and comparison afterwards (procedure in `CLAUDE.md`). Since 2026-11-19 (D79) a second, read-only readback with `:leave` starts the firmware, the default in `tools/flash_acdc.py`. A cold start by hand (case off **and** USB unplugged, then case on, then USB plugged in, D3) only with `--cold`.
- **Preconditions before the first write**, in this order:
  1. **Boot pad probe:** DFU entry via the boot pads on the Xibeca board, only `dfu-util -l`, write nothing. This is the emergency route in case USB is dead in a new build. **Without a successful probe there is no flashing.**
  2. **Reference recording:** 10 min with today's firmware, setup as in A6, as a comparison for clicks and dropouts. Recording in the host software, engine 48 kHz (no upsampling), lean patch, AC/DC input not patched to the output. The same patch later for A6. (Shortened from 30 to 10 min on 2026-11-14: gross USB errors such as a broken feedback endpoint show up within seconds at ≈ 190 ppm clock offset. With 0 clicks in 10 min, the rate is below ≈ 1 per 3 min with 95 %. If Build 1 is conspicuous, record longer in a targeted way.)
  3. **Dry run of the fallback:** flash the readback image `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (identical content), read it back, compare the SHA-256 (`433b3fd3…`), cold start, `owl_read.py`. This tests `-D`, address, length and restart without changing the state. An aborted write cannot damage the ROM DFU.
- **Programmer:** dropped (user 2026-11-16). DFU via SysEx and the boot pads are enough as routes (D4, D5). Flashing and debugging via SWD with an ST-Link remains possible, see "Flashing – general notes".
- **Fallback to the readback image** as soon as one of these cases occurs:
  - USB does not enumerate stably
  - audio dropouts, or more clicks than in the reference recording
  - noise more than 1 dB worse than S2 or the reference (exception according to E1: check the MCLK difference first)
  - settings or storage changed
- Between Build 1 and Build 2 there is no flashing back; Build 2 goes directly over Build 1.
- Every flashed build stays in `firmware/builds/` with its SHA-256.

### Acceptance tests

Every step gets its own section in `docs/messlog.md` (D4 ff.), recordings are entered in `recordings/manifest.toml`.

**Build 1 (`v22.4.s-thru1`)**, in this order:
- **A1:** `owl_read.py` reports `AC/DC v22.4.s-thru1`, `SR/BS/CH 48000 8 4`, slot 1 "ACDC" (CRC `0xbeb3bb2e`), slot 2 `[Lich]`, storage 31 232 B.
- **A2:** Cold start without USB, DPO → In 1…4 one after the other → Out 1…4 audible (default patch VCA, knob at 12 o'clock ≈ ×1).
- **A3:** USB plugged in, no audio app: still audible.
- **A4:** Host playback → outputs. Then stop the playback or deselect the device: the pass-through comes back. If macOS stays in the stream and the outputs are silent, note it as behavior, not as an error.
- **A5:** USB recording of open inputs as in S2 (acdc1, hub, gain at 12 o'clock, 120 s). Comb f0, 6 kHz line, LED line and noise ≥ 20 Hz within ±1 dB of S2.
- **A6:** Long-term test 10 min as in D7: cables Out n → In n, sine 440 / 530 / 670 / 790 Hz from the host software (saved patch, same levels), recording of all 4 inputs. `tools/phase_slips.py` and click detector: 0 phase jumps, 0 clicks, channel assignment as in D7 (reference `E7-ref-loop`). In addition, open inputs as in D6 (`E7-ref`) for the noise comparison.
- **A7:** Then measure **S3** (comb at the outputs with USB unplugged, plugged in and streaming, setup in `docs/03`).

**Build 2 (`v22.4.s-fx1`)**: A1–A6 analogously, plus:
- **B1:** macOS shows "OWL-ACDC-FX", `owl_read.py` finds the port.
- **B2:** The gain knob no longer changes the USB recording, only the output. Gain 0 → output silent, the USB recording still has signal (reversal of series 2).
- **B3:** Noise measurement at the raw inputs = new baseline for all noise experiments (E3).

### Build 1d – Feedback with buffer level control (draft 2026-11-14, not built)

**Reason:** Build 1b and 1c lose one block of 8 frames over USB every ≈ 2–3 min (lab notebook D12, D16). The cause is a net drift of 1.15–1.7 ppm, that is about 1 LSB of the feedback value. So far the feedback only measures the consumption and does not regulate according to the buffer level (open loop). The atomic counter (patch 05) does not help (D16).

**Base:** Build 1c = `db9d3dd` + 01, 02, 04, 05. New is `firmware/patches/06-fb-level-control.patch`, which changes only `Source/usbd_audio.cpp`. Patch 05 stays in, it is harmless and closes the race in any case. Patches 01–06 are tested on `db9d3dd` with `patch`, nothing has been compiled yet.

**Control [code, not tested on hardware]:**
- **Measured quantity:** RX fill level directly after every USB packet in `USBD_AUDIO_DataOut`, that is `getReadCapacity() − codec.getSampleCounter()` in samples over all channels. Both values are read with interrupts disabled. Subtracting the codec counter smooths the block steps of the DMA. The measurement is always taken at the same point of the packet curve (peak), independent of the phase between SOF and codec.
- **Setpoint:** `(buffer + packet)/2` = (576 + 192)/2 = **384 samples** (96 frames). Before the next packet there are then ≈ 192 samples available (reserve 40 frames until underrun), after the packet 192 are free (reserve ≈ 47 frames until overrun).
- **Start:** On the first packet the write head is set so that the fill level is on the setpoint right away (so far 288 after the packet, that is only ≈ 24 frames of reserve). This adds ≈ 0.5 ms of latency. The controller is reset at that point.
- **Controller:** Every 32 ms (`usbd_audio_sof_callback`) the mean of the ≈ 32 measurements is smoothed (EMA over ≈ 8 periods = 0.26 s). The correction is `−FB_GAIN × deviation in frames` in LSB (10.14), with `FB_GAIN = 2`, limited to ±32 LSB (≈ ±40 ppm). Too full means a smaller feedback, the computer then sends less.
- **Behavior:** First-order P controller, time constant ≈ 1/(2 × 0.061/s) ≈ 8 s. With 1.3 LSB of base drift a deviation of ≈ 0.65 frames remains, negligible compared with 40 frames of reserve.
- **Plausibility check:** The check "max. 1 sample difference" (or factor 2) still compares the *uncorrected* value.
- **Diagnostics:** If the correction reaches the limit, the PROGRAM_MESSAGE contains `fb clamp <deviation> <correction>`. In normal operation no new message appears.

**Risks [hypothesis]:**
- How macOS reacts to a fluctuating feedback is not known. But the correction stays in the range of a few ppm and changes slowly.
- If the host follows the feedback only with a delay (seconds), the controller with τ ≈ 8 s is still stable. If it oscillates after all, lower `FB_GAIN` to 1.
- On packet loss or when the host is idle nothing changes; without measurements the correction stays where it is.

**Acceptance test:** A1, briefly A2 (pass-through without USB), then A6 as a **long run of 30 min** in the loop-back as in D16. Criteria: 0 phase jumps, 0 clicks, no new `rx unf`/`fb clamp` message while the stream is running. Then A5 (open inputs) against A5-b1b, because the USB timing changes.

**Result (D17/D18):**
- Flashed and A1 passed.
- Long run without block slips [measured]. There was a single event (≈ 20 ms, no net offset, presumably on the USB bus).
- Accepted by the user as the status for acdc1.
- **A5 [measured, D19]:** passed. Open inputs on average 1.1 dB quieter than Build 1b, broadband noise the same, mixing products +4.7 dB. **D24:** reproducible (spread ≤ 0.1 dB), so firmware (05 and/or 06), not session.
- **A7 = S3 [measured, D20]:** SOF comb at the output gone without USB, standalone output clean. If an app records from the AC/DC, macOS also starts the playback, then the pass-through is off.
- Ground loop and daily-use setup: D21–D23 (not a firmware topic).

### Build 2 new – `v22.4.r-fx1d` (review round 2026-11-15, flashed and accepted 2026-11-15)

**Decisions (review round 2026-11-15):**
- **Purpose:** first the measurement baseline B3 (raw inputs without digital gain), then the daily-use test. Whether Build 2 becomes the daily-use firmware is decided by the user after a few days of operation.
- **Routing accepted [code]:** RX stays POST_FX. As soon as an app records from the AC/DC, macOS also starts the playback stream (D20). The host silence then overwrites the patch output. **Without a computer stream the FX is at the output, during a recording it is gone.** Switching at runtime comes as a separate build.
- **Base:** Build 1d + 03 on top: `db9d3dd` + Libraries `9e8f64e` + 01, 02, 04, 05, 06, **03** (in this order).
- **Identification:** `FW_VERSION=v22.4.r-fx1d`, product string "OWL-ACDC-FX", folder `firmware/builds/acdc1-build2-fx1d/`.
- **The mixing products question (D19) is clarified along the way:**
  - before the flash, still with 1d: A5 twice in one session
  - after the flash: the same with Build 2 (= B3)
  - setup as in D19 (daily-use chain, gain 12, open inputs, 120 s, host software with multichannel recorder), check every file for zeros beforehand
- **Fallback:** first Build 1d (`f522560e…`), then the readback (`433b3fd3…`). Fallback criteria as in E7.
- **Acceptance test:**
  - A1–A4
  - A5/B3 as above
  - A6 as a 10 min loop-back test (extend on a sample slip)
  - B1: port name in macOS and `owl_read.py`
  - B2: gain 0 → output silent, the USB recording still has signal
- **Host software:** Saved patches remember the device name "OWL-ACDC". After the flash a copy with "OWL-ACDC-FX" is created, the original stays.
- **`owl_read.py`** needs no change: `--port` searches by substring (default "OWL-ACDC") and so also finds "OWL-ACDC-FX".
- **Fork:** Only after the acceptance test is passed comes the local branch `acdc/fx1d` (= `acdc/thru-usb-feedback` + one commit with 03). Push only with approval.

**Dry run:** In a fresh tree (`git archive db9d3dd`) 01, 02, 04, 05 and 06 went through, then 03 went through cleanly with `patch --dry-run` (rc 0, without fuzz or offset).

**Build (2026-11-15T14:47:57Z):**

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` |
|---|---|---|---|---|
| `acdc1-build1d-thru1` (ran until this flash) | `v22.4.r-thru1d` | 01, 02, 04, 05, 06 | 105 972 | `f522560eb3d3c329c37753a1ebfdb326e45bae02192f81e866693b363f044c28` |
| `acdc1-build2-fx1d` | `v22.4.r-fx1d` | 01, 02, 04, 05, 06, 03 | 105 968 | `7f9f9a34b5b19a0245f0ab15426d891adc4f00505c86236cadec167e0402925b` |

**Checked:**
- **Source tree:** A diff against a freshly generated 1d tree shows only three lines of difference:
  - `hardware.h`: the product string and the new line `USE_USBD_AUDIO_TX_PRE_FX`
  - `device.h`: the version
- **Binary** [code: disassembly of the ELFs]:
  - In 1d `onProgramReady` calls `usbd_tx_convert` and `usbd_rx_convert` at the start, so POST_FX.
  - In Build 2 only `usbd_rx_convert` is left at the start. `usbd_tx_convert` comes as a tail call (`b.w`) at the end, after MIDI, parameters and buttons, on `audio_input` of the next block (PRE_FX).
  - All other functions have the same size as in 1d.
  - Strings "OWL-ACDC-FX" and "AC/DC v22.4.r-fx1d".
  - The vector table is the same as in 1d (SP `0x00001000`, reset `0x08018479`).
  - Size well below 131 072 B.

**Result (lab notebook D24–D27, 2026-11-15):**
- **D24:** before the flash 2 × A5 with 1d, the same to ≤ 0.1 dB. So the +4.7 dB of the mixing products (D19) come from the firmware.
- **D25:**
  - Flashed, readback = `ACDC.bin`.
  - A1 passed.
  - B1: USB/audio "OWL-ACDC-FX". The MIDI port stays "OWL-ACDC" in CoreMIDI (cosmetic).
  - A2–A4 passed.
  - B2 passed: the USB recording stays constant to 0.05 dB during the gain sweep.
- **D26:**
  - A5/B3: after subtracting the patch factor the same as 1d to ±0.2 dB, mixing products +0.2 dB.
  - B3 is the new noise baseline.
  - The DC offset serves as a gain probe.
- **D27:** A6 (10 min loop-back): 0 sample slips, 0 clicks.
- **Build 2 then ran on acdc1** (until Build 3d, D34).
- **Fork branch `acdc/fx1d`** (2026-11-15, pushed):
  - Base `acdc/thru-usb-feedback` (`06430d10`), on top of it:
    1. `f7a255cc` ACDC: TX pre-FX + product string "OWL-ACDC-FX"
    2. `11199347` version `v22.4.r-fx1d`
    3. `741bac39` README (English): goals, base and why not v22.5.0, every change with its reason, routing table incl. macOS behavior during pure recording, build, DFU backup/flash, measured values (B3 in module dBFS, SOF comb, USB stability, limits)
  - Created via a temporary `git worktree` in `$TMPDIR`. The clone stays on `acdc/thru-usb-feedback`.
  - Commit messages and code comment in English.
  - **Check:** `git archive acdc/fx1d` against the Build 2 source tree: only the comments in `hardware.h` and `usbd_audio.cpp` differ (as with 1d), the code without comments is identical.
  - **Pushed 2026-11-15** (approval in the chat): https://github.com/m9dfukc/OpenWare/tree/acdc/fx1d

### Build 3 – Input LEDs show the raw inputs while recording (review rounds 2026-11-15; 3/3b/3c discarded, **3d `v22.4.r-fx2d` accepted**, today the fallback)

**Starting point [code]:** With TX_PRE_FX and a running stream the knobs act neither on the recording nor on the output. The input LEDs nevertheless showed `PARAMETER_AA` of the patch, that is the level after the knob gain. That was misleading.

**Decisions (review round Q1–Q9):**
- **Q1 Condition:** TX stream active (`usbd_tx != NULL`). RX alone (pure playback) does not count.
- **Q2 Location:** in `usbd_tx_convert` (audio task, not ISR), over all 8 frames × 4 channels. It runs only with active TX; without a stream the computing load stays the same.
- **Q3 Scale:** mean square × 4096 like the patch and `tx_levels`, without the −60 dB threshold. With the knob at 12 o'clock (gain ×1) both modes look the same.
- **Q4 Smoothing:** exponential per block, τ = 4 ms (factor 0.9592 at 6 kHz block rate).
- **Q5 Clip:** Red as soon as a sample reaches |s| ≥ −0.1 dBFS (8 293 000 of 8 388 607), 300 ms hold time (`HAL_GetTick` in `onLoop`).
- **Q6 Transitions:** TX start and stop reset the levels and clip bits. Without a stream the old logic applies immediately. The output LEDs stay unchanged; the peculiarity of `tx_levels` (only the first 8 of 32 samples per block) is not touched.
- **Q7 Knobs as MIDI CC:** not in Build 3. The firmware sends them only on request (`sendPatchParameterValues` on the settings request) [code]. This is to come later if it brings neither load nor interference lines (`TODO.md`).
- **Q8 Names:** patch `07-input-leds-raw-when-recording.patch`, version `v22.4.r-fx2(b)`, product string stays "OWL-ACDC-FX".
- **Q9 Abort:** If a line family is more than 0.5 dB worse in the A/B against B3 and a repetition confirms this, we go back to Build 2.

**Implementation (patch 07):**
- `Source/ProgramManager.cpp`: `raw_in_levels[4]`, `raw_in_clip` (bit mask, `__atomic_fetch_or`), `usbd_audio_tx_active()`, `raw_in_levels_update()` at the start of `usbd_tx_convert`, only under `USE_USBD_AUDIO_TX_PRE_FX`.
- `ACDC/Core/Src/ACDC.cpp`, `onLoop`: With TX it reads `raw_in_clip` via `__atomic_exchange_n` and holds red for 300 ms, otherwise `raw_in_levels × 4096` (limited to 4095). Without TX the old code applies.
- Names deliberately `raw_in_*` instead of `rx_levels`, because "rx" means the playback in the USB part.
- **Pitfall (D28):** SAI1 delivers 24 bit right-aligned **unsigned** (`SAI_DATASIZE_24`). v1 overlooked this, hence permanent red. v2 sign-extends before the measurement.

**Builds:**

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` | Status |
|---|---|---|---|---|---|
| `acdc1-build3-fx2` | `v22.4.r-fx2` | 01, 02, 04, 05, 06, 03, 07 v1 | 106 316 | `f01c8e6bab917d9e6b8f9a38b8200a3ff00b8c2d8c13a8331f23ebcfb58d1bb9` | flashed, LED test failed (D28) |
| `acdc1-build3b-fx2` | `v22.4.r-fx2b` | 01, 02, 04, 05, 06, 03, 07 v2 | 106 332 | `cfa479f30c3bd71bd9ff5515f0208f59fcd0cf28dad0114d8dba2200a9f9cabb` | LEDs ok (D29), A/B failed (D30/D31), then Build 2 as a control |
| `acdc1-build3c-fx2` | `v22.4.r-fx2c` | 01, 02, 04, 05, 06, 03, 07c | 106 304 | `f354239dd305f2417b9ca3d5c9f403aff2890c0c66c8bf117c57643663df7364` | LEDs ok, A/B failed (D32) |
| `acdc1-build2p-layout` | `v22.4.r-fx1p` | 01, 02, 04, 05, 06, 03, 90 (padding bytes) | 106 304 | `cbf45166672a02337d45b9514096dd63ab28a7ba7b23baa1d287d91bb08521f9` | layout test, = 3c to ≤ 0.12 dB (D33) |
| `acdc1-build3d-fx2` | `v22.4.r-fx2d` | 01, 02, 04, 05, 06, 03, 07d | 106 788 | `d212cf8def6f239db997cd45a73304db9bcaf981375e55fdfc2ca2862718832a` | accepted (D34), ran until 2026-11-16, today the fallback |

**Acceptance test (D29–D31):**
- A1 and A2/A3 passed, LED test with stream passed
- Clip red not checked at the time (a signal above ≈ 9.5 V was missing). Done later and passed with 3d (D36)
- A6 dropped (user)
- **A/B against B3 failed (D30)** [measured]: fs/8 +1.4 dB, comb +1.5 dB, mixing products −4.0 dB, residual −0.4 dB, RMS +0.8 dB. r1/r2 the same to ≤ 0.04 dB.
- **Control (D31):** Build 2 flashed back, 2 × 60 s in the same session = B3 to ≤ 0.2 dB. So the shift comes from patch 07, not from the session.
- **Q9 → Build 2 stays on acdc1** (`7f9f9a34…`, since 2026-11-15 ≈ 17:47).
- **Lesson (H7):** Even 32 multiply-adds per block in the audio task shift the block-synchronous interferers measurably, and not monotonically: fs/8 and comb rise, the mixing products fall. This is a lever for E3.
- **Open:** `fb clamp -50.0000 32.0000` as the last message of 3b (D31), time unknown, no clicks.

**Build 3c (review round 3c, D32):**
- Q1 measurement in `onLoop` (every 2 ms) on `codec_rxbuf` (64 samples), nothing in the audio path
- Q2 incomplete coverage (≈ 1/6) accepted
- Q3 τ 40 ms against alias flicker
- Q4 scale, threshold and hold time as in 07
- Q5 patch `07c-input-leds-raw-onloop.patch` as an alternative to 07, version `v22.4.r-fx2c`
- Q6 acceptance test A1, LEDs, A/B against the control D31
- Q7 push later, together
- **Result:** LEDs ok, but fs/8 +2.0, comb +1.5, mixing products −4.4 dB. It changes only `ACDC.cpp`, but shifts all following functions by 0x150 B.

**Padding byte test `v22.4.r-fx1p` (D33):**
- Build 2 + a padding function that is never called (0x150 B, section `.text.onLoop`) and 0x28 B of RAM (section `.bss.fast_log_table_size`), patch `90-layout-pad-like-3c.patch`
- 955 of 957 addresses as in 3c
- **Reproduces 3c to ≤ 0.12 dB** → The placement of code and data in memory shifts the lines, not the function [measured].

**Build 3d `v22.4.r-fx2d` (D34), ran on acdc1 until 2026-11-16, today the fallback:**
- **Function:** as 3c.
- **Code:** located in `.late_text`, a new output section behind the `.data` load image at the end of the flash.
- **State:** located in `.late_bss` (NOLOAD) in the top 64 B of RAM_D2. `_HEAP_D2_END` moves down by 64 B, the heap start stays. Because the area is not zeroed at boot, a magic check resets it on the first call.
- **`onLoop`:** `b.w` + `naked` padding function in `.text.onLoop`, together exactly 0x1d0 B.
- **Patch:** `07d-input-leds-raw-late-section.patch`, affects `ACDC.cpp` and `Hardware/xibeca.ld`.
- **Binary:**
  - 106 788 B, SHA `d212cf8d…`
  - Byte identical with Build 2 in the first 105 968 B, except `onLoop`, the literal `_HEAP_D2_SIZE` and one character of the version.
- **A/B against the control:**
  - fs/8 +0.05, mixing products +0.03, residual −0.18, RMS +0.19 dB
  - comb +0.55 (against B3 +0.42, r2 − r1 +0.26)
- **User:** 3d stays, without a further control.

**Lesson for all further builds:**
- Every change that shifts code or data in front of the audio functions changes fs/8, comb and mixing products by up to ±2 or ±4.5 dB respectively.
- A/B between builds therefore measures code **and** placement.
- New functions therefore go to `.late_text`/`.late_bss`, or the placement is checked with `nm` against the reference build.
- The placement is at the same time a lever for E3: try out padding bytes.

**Fork:**
- `acdc/fx1d` + `f206fdd4` (code 07), `6eee596c` (version fx2b), `b3bd3752` (README), pushed 2026-11-15.
- In addition locally `8da4eb7b` (README A/B), `6d3b8bd5` (code 07d), `cc2e08f8` (version fx2d), `abc3a72a` (README fx2d + "Memory layout matters"). **Pushed 2026-11-15.**
- The branch name stays for historical reasons.

**Fallback (from 3d on):** Build 2 (`7f9f9a34…`), then 1d (`f522560e…`), then the readback (`433b3fd3…`).

### Build 4 – Hot path in the ITCM, `v22.4.r-fx3i` / `fx3ip` (review round 2026-11-16; built 2026-11-16; **fx3i measured: fs/8 −5 dB, but USB playback disturbed (D37/D38), then back to 3d**)

**Goal:** The placement of the remaining code in the flash should no longer shift the interference lines (D33). Basis: `docs/research/notes/layout_noise_2026-11-16.md` and `daisy_itcm_2026-11-16.md`. There is no evidence anywhere that ITCM lowers interference lines; this remains [hypothesis]. Teensy 4 puts all code into the ITCM, so the pattern is proven. Daisy does not use ITCM.

**Decisions (user 2026-11-16, Q1–Q15):**
- **Q1 Base:** `db9d3dd` + Libraries `9e8f64e` + 01 02 04 05 06 03 07d **+ 08** (upstream build flags `d5b6409a`, byte identical on 3d). No switch to master `36eaf1c4` (would be a port, see `docs/research/notes/upstream_master_2026-11-16.md`), no patch 09.
- **Q2 Success:** (a) and (b) are mandatory.
  - (a) `fx3i` is not worse than 3d at fs/8, comb and mixing products, threshold ≈ 0.5 dB. Quieter is a bonus.
  - (b) `fx3ip` (= `fx3i` + padding bytes like `fx1p`/patch 90) differs from `fx3i` by ≤ 0.5 dB, so the placement no longer matters.
- **Q3 Measurement:** one session, order 3d → fx3i → fx3ip → 3d. 2 × 60 s each, open inputs, gain at 12 o'clock, stream reopened between the runs. Each flash only after approval.
- **Q4:** Jitter (Daisy), WFI in idle and uniform load in idle (Electrosmith recommendation, Daisy docs "Avoiding Callback Noise") only afterwards, each as a separate build with A/B.
- **Q5:** Clip test of 3d at the start of the same session (signal above ≈ 9.5 V).
- **Q6:** no separate diagnostic build on the mechanism (e.g. I-cache off).
- **Q7 Scope:** everything that runs periodically, ≈ 10 KB:
  - SAI DMA ISR including `HAL_DMA_IRQHandler`
  - FreeRTOS scheduler with idle and PendSV
  - audio task with `onProgramReady`, `usbd_tx/rx_convert`, `updateParameters`, MIDI send/receive
  - USB OTG ISR including `HAL_PCD_IRQHandler`, USBD core and audio class, feedback
  - SysTick, ADC DMA
  - helpers `memset`/`memcpy`/`abs` and the list functions
  - the 07d functions from `.late_text`

  The function list with sizes was in the handoff of 2026-11-16 (not in the repository). Today `tools/check_itcm.py --ref <build>` provides it as a table in the report, e.g. in `firmware/builds/acdc1-build6-fx4a/check_itcm.md`.
- **Q8:** The vector table also goes into the ITCM, aligned to 1 KB. VTOR is switched after copying, the original stays in the flash for the boot.
- **Q9 Location:** CCMRAM from 0x3000, behind `PROGRAMSTACK`. In the linker script the code must come **before** `PROVIDE(_CCMRAM)`, otherwise the patch start zeroes it (`ProgramManager.cpp`, `USE_CCM_RAM`). Heap segment 0 shrinks from 52 to ≈ 41 KB.
- **Q10:** The remaining layout is not pinned down; (b) checks the layout dependence directly.
- **Q11 Check before the flash:** new `tools/check_itcm.py` checks on the ELF:
  - All hot path functions and the vector table are located in the ITCM block.
  - From the hot path, `bl`/`b.w` go into the flash only in the error path.
  - Veneers are listed.
  - The size is below 131072 B, LMA/VMA of the copy are correct.
  - In addition the `nm` table against 3d.

  After the flash first A1 (`owl_read.py`), pass-through, USB recording and LEDs, then the noise measurement. Fallback: 3d.
- **Q12–Q15 Recording:** with `tools/acdc_rec.py`, cross-check against the host software passed (D35).

**Technique (from the research, to be implemented this way without asking back):**
- **Linker script:** `.itcm_text` with `>CCMRAM AT>FLASH` before `.text` (the first matching output section wins). Patterns by file and section, e.g. `*stm32h7xx_hal_dma.o(.text.HAL_DMA_IRQHandler)`. This is possible because `-ffunction-sections` is set and no LTO runs. C++ names are mangled. Filter weak/strong duplicates (SAI callbacks, `updateParameters`) by object file. Check COMDAT copies.
- **ECC:** The ITCM has 64-bit ECC (AN5342/RM0433). Put the start, end and LMA of the section on `ALIGN(8)`, copy in 64-bit words, then DSB/ISB. RAMECC is off in OpenWare, so errors would be flagged silently.
- **Startup:** second copy loop in `startup_owl3.s` after the `.data` loop, before `__libc_init_array`/`main`. Nothing that runs before `main` (`SystemInit`, constructors) may go into the ITCM.
- **Veneers:** GNU ld creates them itself, `-mlong-calls` is not needed. But every call from the ITCM into the flash costs a veneer plus a flash fetch. Therefore list them all after the link and pull helpers in (`__aeabi_*`, `memcpy` etc.).
- **Optional, not in the first attempt:** hot `.rodata` into the DTCM, MPU write protection over `.itcm_text`.
- **Building:** new patch `11-itcm-hotpath.patch` (choose the number freely, do not change existing ones), `FW_VERSION=v22.4.r-fx3i tools/build_acdc.sh acdc1-build4-fx3i db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz 01 02 04 05 06 03 07d 08 11`. `fx3ip` = plus patch 90 or a padding patch that shifts the rest of the flash (goal: different addresses outside the ITCM, ITCM content the same).

**Implementation (2026-11-16) [code, checked on the ELF, not on hardware]:**
- **Patch `11-itcm-hotpath.patch`** (only `Hardware/xibeca.ld` and `Source/startup_owl3.s`, existing patches unchanged):
  - `.ccmdata` (NOLOAD, PROGRAMSTACK 0x1000–0x3000) moved before `.text` in the script, address unchanged.
  - `.itcm_vectors` (NOLOAD) at 0x3000, aligned to 1 KB, for the vector copy (664 B).
  - `.itcm_text >CCMRAM AT>FLASH` before `.text`, linker patterns by object file + section. VMA 0x32A0–0x62C8 (12 328 B incl. 27 veneers), LMA 0x08000298. Start, end and LMA 8-byte aligned (ECC).
  - `_CCMRAM = _eitcm_text`: patch heap in the CCM 40 248 B (39.3 KB) instead of 53 248 B.
  - `Reset_Handler`: after `.data`/`.bss` two `ldrd/strd` loops (vectors, code), DSB/ISB, VTOR = 0x3000, DSB/ISB, then `__libc_init_array` and `main`. `SystemInit` runs before that and calls nothing in the ITCM.
  - **Anchor** at the start of `.text` (0x080032C0, 2 395 B): all flash targets whose address is stored in the ITCM (vector handlers in the flash, 27 veneer targets, 6 debug texts). Only this way does the ITCM content stay byte identical in the padding variant.
- **Scope extended relative to the handoff list** (veneer check, Q7 "everything that runs periodically"):
  - Group H main loop every 2 ms: `StartDefaultTask`, `loop`, `onLoop` (with the 07d padding function, 0x1D0 B), `Owl::loop`, `ProgramManager::isProgramRunning`, `device_watchdog`, `vTaskDelayUntil`, `vTaskSuspendAll`, `xTaskResumeAll` (+ `.part.0`).
  - onLoop helpers: `setLed` (+ `.constprop.0`), `getParameterValue`, `setParameterValue`, `HAL_GetTick`.
  - USB: `usbd_midi_tx`, flush chain (`USBD_LL_FlushEP`, `HAL_PCD_EP_Flush`, `USB_FlushTx/RxFifo`), ISO OUT incomplete chain.
  - 104 functions in total, 11 606 B.
- **Veneers ITCM → flash (27), all cold:** errors (`usbd_audio_error`, `debugMessage` ×2, `vApplicationStackOverflowHook`, `HAL_ADC_ErrorCallback`, `USBD_LL_StallEP`) and rare events (enumeration/reset/suspend/resume/connect/LPM, EP0 control transfer, stream start `usbd_audio_rx_start_callback`, MIDI input `usbd_midi_rx`, `vPortFree` in idle after task deletion, `setup` once at start). Literals into the flash: only 6 debug texts. List with callers in `check_itcm.md`.
- **Patch `91-layout-pad-behind-itcm-anchor.patch`** (fx3ip): `. = . + 0x150` behind `_eitcm_anchor`. 479 flash functions +0x150, anchor (171 symbols incl. default handler aliases) fixed, ITCM code and vector table byte identical with fx3i, all RAM addresses the same. Unlike fx1p (D33) the RAM stays unshifted.
- **`tools/check_itcm.py`** checks Q11 on the ELF and binary (sections, alignment, LMA, binary = ELF, vectors, hot list, veneers against a list of cold targets with reason, literals, anchor, USBD_AUDIO pointers, nothing in the ITCM before the copy, nm against the reference, `--same-itcm`). Report `check_itcm.md`/`.json` in the build folder.
- **nm against 3d:** 728 common functions, 105 into the ITCM, none at the old address (everything shifted), only `Reset_Handler` larger (66 → 128 B). RAM: all 176 data objects at the same address as in 3d.
- [hypothesis] Patches put nothing at a fixed place in the CCM (the heap comes via `heapSegments`), otherwise they would overwrite the code. A function test after the flash clarifies this.

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` | Status |
|---|---|---|---|---|---|
| `acdc1-build4-fx3i` | `v22.4.r-fx3i` | 01 02 04 05 06 03 07d 08 11 | 107 304 | `8fedebf7e909457f69d8b2a06003cd550496c7f65b330d3f5d5206597037fdf2` | flashed 2026-11-16 (D37): fs/8 −5.1 dB, residual −0.9 dB, comb ±0; **playback disturbed** (28 sample slips/60 s, `fb clamp`, D38) → back to 3d |
| `acdc1-build4p-fx3ip` | `v22.4.r-fx3ip` | plus 91 | 107 640 | `d2b36d8453e856f63c5e2ebbae983b93eaebec41161987078379f4b0cf9b541d` | checked, ITCM byte identical with fx3i, **not flashed** (has the same fault) |

**Result of the session (D36–D38):**
- Clip red of 3d passed (D36).
- Q2 (a) fulfilled: fx3i relative to the mean of two 3d controls fs/8 −5.06 dB, RMS −0.98, residual −0.89, mixing products −0.54, comb +0.01 dB (D37).
- Q2 (b) open: fx3ip not measured.
- **Functional fault:** In the USB loop-back fx3i has 28 sample slips in 60 s and increased phase noise, 3d in the same setup 0 (D38). The RX buffer runs ≈ 1 packet too empty (`fb clamp −195…−208`). Cause open [hypothesis: lost ISO OUT packets or a race between ISR and audio task due to the changed timing].
- **Next step:** Bisect with fx3i variants (without group D or C in the ITCM), check each variant with the 60 s loop-back test (`acdc_rec.py --sine 440 530 670 790` + `phase_slips.py`), only then noise measurement and fx3ip again. Every new variant goes through `check_itcm.py` before the flash. **Done:** "Build 4x" below (D39/D40).

### Build 4x – Bisection of the fx3i fault (2026-11-16 evening, lab notebook D39/D40)

**Goal:** Find out which group in the ITCM triggers the playback fault of fx3i (D38). Agreed with the user: build all four variants, on the module noD → noC → onlyD, novt only if needed, diagnostic build with counters only after the variants.

**Implementation [code, checked on the ELF]:**
- For each variant a separate, **complete replacement for patch 11** (11 and all other patches unchanged). Generated from the state after patch 11: groups that are not selected are replaced by a comment in the `.itcm_text` block. Anchor, `.itcm_vectors` and startup stay as in 11.
  - `11a-itcm-variant-noD.patch`: groups A B C E F G H L
  - `11b-itcm-variant-noC.patch`: A B D E F G H L
  - `11c-itcm-variant-onlyD.patch`: D L
  - `11d-itcm-variant-novt.patch`: all groups, linker script as in 11 (space for the vectors stays reserved), but `Reset_Handler` without the vector copy and without the VTOR write
- Group **L** = libc helpers `memset`/`memcpy`/`abs` (already a separate block in the linker script). It stays in the ITCM in all variants.
- **`tools/check_itcm.py`** new with `--groups` (letters A–H, L) and `--no-vector-copy`:
  - Functions and vectors of groups that are not selected must be located in the flash.
  - Veneers to them are a separate, intended category.
  - For variants the anchor only produces a warning.
  - `USBD_AUDIO` callbacks are expected in the ITCM only with group D.
  - Group L is new: `memset` was previously under C, `memcpy`/`abs` under D.
  - With the new version fx3i gives the same report as before.
- Build: `FW_VERSION=v22.4.r-fx3i-<v> tools/build_acdc.sh acdc1-build4x-<v> db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz 01 02 04 05 06 03 07d 08 11x`. Under zsh pass the patch list as an array, otherwise it arrives as one argument.
- New **`tools/stale_samples.py`**: find single wrong samples in loop-back recordings (position in the block grid, best-matching distance of the wrong value), complements `phase_slips.py`.

| Build | `FW_VERSION` | ITCM code | Patch heap CCM | Size B | SHA-256 `ACDC.bin` | check_itcm | Loop-back test (D39) |
|---|---|---|---|---|---|---|---|
| `acdc1-build4x-noD` | `v22.4.r-fx3i-noD` | 7 232 B | 45 344 B | 107 116 | `2c140449cd44b4f93cc43405bca4553ac12d1c6e0ace30cfcb5c336772cfcd59` | passed, 1 WARN (anchor) | **USB clean**, channel 4 stale |
| `acdc1-build4x-noC` | `v22.4.r-fx3i-noC` | 11 432 B | 41 144 B | 107 300 | `8b7d2197bfe67bb9d31d2a9a9af241e3374f1b5ed59440c40ab44d610c338a26` | passed, 1 WARN (anchor) | 16 sample slips, `fb clamp`, channel 4 clean |
| `acdc1-build4x-onlyD` | `v22.4.r-fx3i-onlyD` | 5 152 B | 47 432 B | 107 136 | `f75efaeed79c74330819b1c36063d9c31a90e91b80a3d800a7d2b7d31400f107` | passed, 1 WARN (anchor) | 8 sample slips, channel 4 clean |
| `acdc1-build4x-novt` | `v22.4.r-fx3i-novt` | 12 328 B | 40 248 B | 107 260 | `da25fc5f374a17679408c72b33d08e2b720b0de076579f6cb31e6f673408aaab` | passed | not flashed (unnecessary) |

**Result [measured, D39/D40]:** fx3i has **two separate faults**.
1. **USB playback fault ↔ group D in the ITCM.** D alone triggers it (onlyD), without D it is gone (noD). Vector table/VTOR are ruled out (H-e). The mechanism within D is open, [hypothesis] H-a (ISO OUT parity on re-arming, empty `IsoOutIncomplete`).
2. **Stale last input sample (channel 4, 16 frames old) ↔ group C in the ITCM.** [code] `audioCallback` hangs on the TX DMA interrupt, but releases the RX half before the RX DMA has written the last word. The fast audio task reads too early. This is a latent bug in the original; it also affects the patch input (standalone).

**What is suitable next for the noise measurement (fx3i′ + fx3ip′)?** Proposal, not yet agreed:
- **Base noD** (USB code in the flash, everything else in the ITCM). It is clean in the USB loop-back.
- **Plus a fix for the RX race**, otherwise channel 4 is corrupted and standalone is affected. Two ways, both change code:
  - (a) In `audioCallback` wait until the RX DMA counter (NDTR of SAI1-A) has passed the half boundary. This takes at most one word, ≈ 1–5 µs, and hardly changes the timing.
  - (b) Hang the block on the RX interrupts as in the CS4271 branch. This shifts the position of the audio task relative to the codec and thus possibly the block-synchronous interference lines.
  - Recommendation (a), because it is minimal. Whether the fix also belongs in 3d is open: there the race was never measured (0 of 96 000).
- **Open:** How much of the fs/8 improvement (−5 dB, D37) remains when D is in the flash. And whether noD is layout independent, because the 1 kHz USB code is then in the flash again, and the anchor would need `USBD_LL_Transmit`. Both are only clarified by the measurement of fx3i′ against 3d and fx3ip′ respectively.
- **Alternative:** Understand and fix the USB fault with group D in the ITCM (diagnostic build with counters in `.late_bss`: `INCOMPISOOUT`, frame number gaps between `DataOut`, packet lengths, `rx unf/ovf`, message via `PROGRAM_MESSAGE`). Then split D (OUT path / SOF+feedback / IN path). This is more effort, but would be necessary if the fs/8 gain depends on D.

### Build 4y – fx3j = noD + RX fix (2026-11-16 late evening, lab notebook D41/D42)

**Decision (user):** fx3i′ = noD + fix of the RX race (D40). Built as fx3j, plus the padding variant fx3jp.

**Implementation [code]:**
- **Patch `11e-itcm-variant-noD-anchor.patch`** (replacement for 11/11a): like 11a, plus `USBD_LL_Transmit` in the anchor. This was the only flash target of the ITCM code behind the anchor (veneer from `usbd_midi_tx`). `check_itcm --groups ABCEFGHL`: 0 FAIL, 0 WARN.
- **Patch `12-rx-dma-wait.patch`** (`Source/Codec.cpp`, PCM3168A branch):
  - In `HAL_SAI_TxHalfCpltCallback`/`TxCpltCallback`, wait before `audioCallback` until NDTR of the RX DMA (`hdma_sai1_a`, DMA1_Stream0) has left the released half.
  - First half done: NDTR ≤ blocksize·channels. Second half done: NDTR > blocksize·channels.
  - At most 4096 read accesses. The callbacks are located in the ITCM (group A).
- fx3jp = fx3j + patch 91: ITCM byte identical with fx3j, 514 flash functions +0x150. Here the USB code shifts as well, because it is in the flash. RAM unchanged.

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` | Status |
|---|---|---|---|---|---|
| `acdc1-build4y-fx3j` | `v22.4.r-fx3j` | 01 02 04 05 06 03 07d 08 11e 12 | 107 176 | `707d9cd3324baa7ea20f3178df972e60c2822466e3a7c7bc826b7b456c5546ac` | flashed 2026-11-16: loop-back clean (D41), **noise worse than 3d** (D42) → back to 3d |
| `acdc1-build4yp-fx3jp` | `v22.4.r-fx3jp` | plus 91 | 107 512 | `6db0f56c06469f13e298cd6a4d6baf1f0ef0037508a98f38cc8ef7efadf55306` | checked (`--same-itcm` fx3j), not flashed |

**Result [measured, D42]** (Δ against 3d of the same session):
- **fx3j:** fs/8 +5.2, comb +3.1, RMS +2.8, mixing products −10.1 dB. Functionally flawless, but unusable for the noise measurement.
- **noD (without fix):** fs/8 −5.4, comb +2.5, RMS +0.7 dB.
- **From this:**
  1. The fs/8 gain of fx3i does **not** depend on the USB code in the ITCM.
  2. **The wait loop (patch 12) costs ≈ +10.6 dB fs/8.** A few µs of reading a D2 peripheral register per block are enough. [hypothesis] What the CPU does at the block rate appears directly at fs/8. For the search for the cause this is an important finding.
  3. **The comb** is lowered only by the USB code in the ITCM (fx3i ±0, noD +2.5 dB).

**Next steps (proposal, not agreed):**
1. **RX fix without a polling loop (patch 12b):** **Done, see "Build 4z" (D43/D44).** In the PCM3168A branch call `audioCallback` from `HAL_SAI_RxHalfCpltCallback`/`RxCpltCallback` instead of from the TX callbacks, as in the CS4271 branch.
   - The RX DMA interrupts already run today (DMA1_Stream0, the weak HAL callbacks are empty). So there is no additional interrupt and no bus traffic, the block only starts ≈ 1 word later.
   - Output side [code]: The task writes the TX half that has just been sent, the TX DMA is ahead by at most the FIFO depth. Almost a whole block of time remains.
   - Check: loop-back (0 sample slips, 0 stale samples), noise against 3d and noD.
2. **Comb:** USB code (all of it or only SOF/feedback) into the ITCM, without the playback fault. For this, split group D (D-SOF: SOF chain + feedback, D-OUT: `DataOut`/`PrepareReceive`/`EP_Receive`/`EPStartXfer`/`ReadPacket`, D-IN) or make a diagnostic build with counters (`INCOMPISOOUT`, frame gaps between `DataOut`, packet lengths).
3. Then a layout test (padding variant) for the chosen revision.
4. Open: whether patch 12b also belongs in 3d or in the standalone revision. In 3d the race never occurred (0 of 96 000 samples).

### Build 4z – fx3k = noD + RX callback (2026-11-16 late evening, lab notebook D43/D44)

**Implementation [code]:**
- **Patch `12b-rx-dma-callback.patch`** (replacement for 12, `Source/Codec.cpp`, PCM3168A branch):
  - `audioCallback` is called from `HAL_SAI_RxHalfCpltCallback`/`RxCpltCallback` (RX DMA, SAI1-A, DMA1_Stream0), with the same arguments as before from the TX callbacks. This is the pattern of the CS4271 branch.
  - The RX DMA interrupts already ran before, only with empty weak callbacks. So there is no additional interrupt and no polling.
  - The TX callbacks stay as strong, empty definitions in `Codec.o`. This way the ITCM rule still applies, and no veneer to the HAL version is created.
  - [code] `codec.getSampleCounter()` still reads the TX NDTR and jumps to 0 ≈ 1 word before the block start. The window in which patch 06 or `usbd_audio_get_rx_count` already count the block as consumed becomes ≈ 5 µs longer. This window already existed before (wake-up latency of the task), and it corrects itself. The loop-back test shows no effect (D43).
- **Patch `11f-itcm-variant-noD-anchor-rxcb.patch`** (replacement for 11/11a/11e): like 11e, plus `*Codec.o(.text.HAL_SAI_RxHalfCpltCallback .text.HAL_SAI_RxCpltCallback)` in group A. The rule for `stm32h7xx_hal_sai.o` no longer applies with 12b, because the weak versions are dropped by `--gc-sections`.
- Checked: `check_itcm.py --groups ABCEFGHL` with 0 FAIL and 0 WARN. The RX callbacks from `Codec.o` are located in the ITCM and jump into `audioCallback` via `b.w`, the TX callbacks are `bx lr`. fx3kp with `--same-itcm` fx3k: ITCM byte identical (7232 B), 514 flash functions +0x150.
- fx2e = 3d + 12b without ITCM. Code behind `Codec.o` moves there by −8/−16 B against 3d (301 and 163 functions respectively). Patch 08 alone does not change the binary (`cand-r-fx2d-gcc13flags` = `d212cf8d…`).

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` | Status |
|---|---|---|---|---|---|
| `acdc1-build4z-fx3k` | `v22.4.r-fx3k` | 01 02 04 05 06 03 07d 08 11f 12b | 107 112 | `06e868d16ea8c601ac1433bd2f67fc14a31edd7737885bcf4754d0c08de3dea8` | flashed 2026-11-16: loop-back clean (D43), fs/8 −5.8, comb +3.5 dB (D44) → back to 3d |
| `acdc1-build4zp-fx3kp` | `v22.4.r-fx3kp` | plus 91 | 107 448 | `c3835524f4d5281cb3469800a6cab436d317554c6cb60e49cb957a051c67a91a` | checked, not flashed (comb criterion missed) |
| `acdc1-build3e-fx2e` | `v22.4.r-fx2e` | 01 02 04 05 06 03 07d 08 12b | 106 780 | `4a1aa25f3cd96f62ef23d477526c86c0ecc0c19c32f20424eabc7af82edf7055` | built, not flashed |

**Result [measured, D43/D44]** (Δ against 3d of the same session):
- **Loop-back:** 0 sample slips, 0 stale samples (30 s), no `fb clamp`.
- **Noise:** fs/8 −5.8, comb +3.5, mixing products −19.4, RMS +1.0 dB.
- **12b costs nothing at fs/8** (noD −5.4, fx3i −5.1). The rise in fx3j came from the polling loop.
- fx3k misses Q2 (a) only on the comb (USB in the flash), therefore no fx3kp.

**Next steps (proposal, not agreed):**
1. **Comb:** **Done, see "Build 5" (D45–D48): fx3l.** On the fx3k base, USB code into the ITCM, without the playback fault from D39. Either split group D (D-SOF: SOF chain + feedback; D-OUT: `DataOut`/`PrepareReceive`/`EP_Receive`/`EPStartXfer`/`ReadPacket`; D-IN) or a diagnostic build with counters (`INCOMPISOOUT`, frame gaps, packet lengths). Goal: fx3i comb (±0) with fx3k fs/8 and fx3k mixing products.
2. Then a layout test (padding variant) for the chosen revision.
3. Open: whether 12b also belongs in 3d/standalone (fx2e is ready). In 3d the race never occurred. But the fix is correct, and 12b is cheap.

### Build 5 – USB in the ITCM: diagnosis, SOF fix, fx3l (2026-11-16 at night, lab notebook D45–D48)

**Approach (user decision):** First build a diagnostic build with counters, then fix in a targeted way. Do not split D.

**Diagnosis [measured]:**
- Patch `13-usb-diag-counters`: counters in the USB path, message every 500 ms from onLoop. With USB in the ITCM (dg5i) **no** ISO OUT packets are lost (H-a refuted), but the feedback controller clamps constantly. With USB in the flash (dg5f) everything runs cleanly (D45).
- Patch `13b-usb-diag-sof-fb`: With USB in the ITCM, `USBD_AUDIO_SOF` runs **twice** in ≈ 97 % of the frames (same frame number). The feedback period then covers ≈ 16 instead of 32 frames, the value sent is 47.5…48.5, the buffer runs to the limit (D46).
- [hypothesis] HAL clears `GINTSTS.SOF` only after the callback. The ITCM handler is entered again before the clearing takes effect in the USB clock domain.

**Fix:** Patch `14-usbd-sof-once-per-frame` (`Source/usbd_audio.cpp`): `USBD_AUDIO_SOF` remembers `DSTS.FNSOF` and returns immediately on a second call in the same frame. With USB in the flash the patch has no effect.
- Open and not necessary: move the clearing in HAL before the callback. This would also remove the surplus interrupt entries (≈ 1 kHz, only a few cycles). Their effect on the noise is unknown.

**Linker:** Patch `11g-itcm-hotpath-rxcb` = patch 11 (all groups A–H + L) + RX callbacks from `Codec.o` (for 12b).

| Build | `FW_VERSION` | Patches | Size B | SHA-256 `ACDC.bin` | Status |
|---|---|---|---|---|---|
| `acdc1-build5-diag-itcm` | `v22.4.r-dg5i` | Base + 11g 12b 13 | 108 904 | `27390dcadfd911e2697e0cf6caf1d83e4008c2b4918f5736f25796cb2d8faf48` | flashed, D45 |
| `acdc1-build5-diag-flash` | `v22.4.r-dg5f` | Base + 11f 12b 13 | 108 728 | `02052846c647e990abdfecaf55c138b067b4d6b6387f653f3b93a053eb808431` | flashed, D45 |
| `acdc1-build5b-diag-itcm` | `v22.4.r-dg5i2` | Base + 11g 12b 13 13b | 109 104 | `9611f646d7fa68a1149fcc063cc72f1cc37b16154a8610007367eaff89e9c2e5` | flashed, D46 |
| `acdc1-build5b-diag-flash` | `v22.4.r-dg5f2` | Base + 11f 12b 13 13b | 108 928 | `0a0851f43999391378d33eb5c32e2e24136a3577c9919471d5d4e6aca115838f` | built, not flashed |
| **`acdc1-build5c-fx3l`** | `v22.4.r-fx3l` | Base + **11g 12b 14** | 107 340 | `b55b94d8734baf1cf763dfefb380a561029bd00d4a645cdcef3b75d99e6f010e` | flashed: loop-back clean (D47), noise D48 |
| `acdc1-build5cp-fx3lp` | `v22.4.r-fx3lp` | plus 91 | 107 676 | `a4deba3e6263e1b96b7098a6f03b5117d18abb724cdefac987fb28eba556939f` | flashed: noise D48 (ITCM byte identical, 479 flash functions +0x150) |

(Base = 01 02 04 05 06 03 07d 08.) Check of fx3l/fx3lp: `check_itcm.py` 0 FAIL, 0 WARN, 104 hot functions in the ITCM (12 352 B code + 664 B vectors), 27 veneers going out, all cold, patch heap 39.3 KB.

**Result [measured, D47/D48]** (Δ against 3d):
- **fx3l:** loop-back clean (0 sample slips, 0 stale samples, no `fb clamp`). fs/8 −5.1, mixing products −34.8, residual −1.25, RMS −1.1 dB, comb +0.2…+0.4 dB.
- **fx3lp:** within ≤ 0.25 dB of fx3l → layout independent.
- **This fulfils Q2 (a) and (b).** fx3l is the first candidate that can replace 3d.

**Next steps (proposal, not agreed):**
1. Decide whether fx3l replaces 3d on acdc1. Before that a longer daily-use test would make sense (recording + playback on the computer, standalone pass-through, LEDs, patch change; patch heap in the CCM only 39.3 KB).
2. Second noise session with a 3d start control (3d → fx3l → 3d), because the comb (+0.2…+0.4) is close to the threshold.
3. Fork branch: **done 2026-11-16.** `acdc/fx1d` now has `151bd8bc` (upstream `d5b6409a`, = 08), `2ae8b836` (12b), `0b7122de` (11g), `fb2c6ed9` (14), `5cb2c17c` (version) and `b7062ef2` (README). Pushed, a build of the tip is byte identical with fx3l.
4. Optional: HAL clears `GINTSTS.SOF` before the callback, A/B against fx3l.

### Build 6 – Boot menu to choose the patch, `v22.4.r-fx4a` (agreed and built 2026-11-17, **acceptance passed with fx4a/fx4b**, lab notebook D50–D58)

**Reason:** Slot 1 always starts at power-on. Without a computer the patch could not be changed.

**Decisions (user, 2026-11-17):**
- Selection only at power-on, not during operation.
- Entry: knobs 1, 2, 3 at the left stop, knob 4 at the right stop.
- Knob 1 selects, knob 4 away from the right stop confirms, knob 3 away from the left stop cancels. After 60 s without confirming the menu cancels.
- Knob 1 only counts once it has been moved. Until then the remembered slot stays selected, so confirming by accident changes nothing.
- At most 15 slots (4 LEDs in binary). Storage does not limit this: 8 MB of patch flash, the firmware handles 40 slots.
- The chosen slot is remembered in flash and starts at the next power-on.
- At start the input LEDs show the slot number for 1 s.

**Implementation (patch `15-boot-menu-slot-select.patch`) [code]:**
- **Place:** `acdcBootSelect()` in `ACDC/Core/Src/ACDC.cpp`, called from `bootstrap()` (`Source/ProgramManager.cpp`, under `OWL_ACDC`). The menu runs in the manager task before the first patch starts. So the output is silent while the menu is open.
- **Scheduler:** `configUSE_PREEMPTION` is 0. `onSetup()` (LED chaser, ≈ 0.9 s) has finished before `bootstrap()` runs. The main loop (MIDI, watchdog) only runs while the menu sleeps in `vTaskDelay()`. So `owl_read.py` reaches the module in the menu too.
- **Knobs:** read directly from `adc_values` (12 bit), smoothed with 1/8 in the menu. "At the stop" means below 5 % or above 95 %, "away from the stop" another 5 %. Measured on acdc1: left stop ≈ 1.6 %, right stop 100 % (D51).
- **Selection:** Only occupied slots can be selected. They share the knob travel evenly, with hysteresis at the borders.
- **Display:** input LEDs = slot number in binary (LED 1 = 1, 2 = 2, 3 = 4, 4 = 8). The output LEDs are lit in the menu and blink while confirming would change the slot.
- **Storing:** 4 bytes as a system resource `ACDC.slot` in the patch flash (QSPI). The settings stay untouched (E4 still holds). From my reading of the code the normal settings store does not work on the AC/DC anyway, because it requires memory-mapped flash and the AC/DC has no internal storage [code, not checked].
  - Each change appends 256 B and marks the old record as erased.
  - Below 64 KB of free storage nothing is written, otherwise `writeResource()` would trigger a defrag, which erases the whole flash. The slot then starts without being remembered, and the input LEDs flash red for 1 s.
  - If the record is missing or points to an empty slot, slot 1 starts, or else the first occupied slot.
- **Host:** If a computer sends a Program Change or an upload while the menu is open, the menu ends and `bootstrap()` starts nothing itself.
- **Periodic path:** The only addition is the test of `acdc_boot.led_hold` at the start of `acdcOnLoopLate` (5 instructions). While it is set (menu or 1 s slot display), `onLoop()` leaves the LEDs alone. The state (2 bytes) lives in `.late_bss`.
- A Program Change from the computer during operation is not remembered.

**Build:** `firmware/builds/acdc1-build6-fx4a/`, `v22.4.r-fx4a`, 108 496 B, SHA-256 `e7ee9b90ccd2cb2763e695dbab0bb82e5fa63c94c6e823e2e48dc3177ff2f063`. Patches as for fx3l + 15.

**Check without the module [measured, D50]:**
- `tools/check_itcm.py`: PASSED, 0 FAIL, 0 WARN. ITCM code +40 B, all RAM objects at the same address as in fx3l.
- `tools/sim_boot_menu.sh`: the menu code runs unchanged on the host against simulated knobs. 18 cases: normal start, selection, cancel, timeout, host, full storage, jitter at zone borders, 15 slots, gaps in the slots.

**Acceptance after the flash:**
1. Done (D51): end values of the knobs measured, left 2 and right 127 of 127. The thresholds fit, no rebuild. Flash with a byte-identical readback.
2. Done (D52): A1 with `owl_read.py`, version fx4a, block size 8, slots 1–5 unchanged. The menu works (user), the choice of slot 3 was remembered once (+256 B).
3. Done (D53, D55): normal start from the remembered slot.
4. Done (user, D52/D53, fx4a): entry, display, selection, confirming, cancel with knob 3, cancel after 60 s. The 30 s timeout of fx4b has not been timed on the module.
5. Done (D52, D55, D58): after a power cycle the chosen slot starts (slot 3, later 4 and 5).
6. Done (D55): a start with the knobs in an everyday position (104 / 125 / 85 / 50) does not open the menu.
7. Done (D57, fx4b): loop test with `phase_slips.py` and `stale_samples.py`, 0 slips, 0 stale samples, also with Tanh3 at 53 % CPU.
8. Done (D58, fx4b): noise A/B against fx3l in the same session (fx4b → fx3l → fx4b, 2 × 60 s each). All families within ±0.4 dB, on average ±0.2 dB. The noise of fx4b equals that of fx3l.

**Build 6b `v22.4.r-fx4b` (2026-11-17, D53/D55):** After the acceptance of the menu the user asked for 30 s instead of 60 s until it cancels. Patch `15b-boot-menu-slot-select-30s.patch` replaces 15 completely, the only difference is `ACDC_MENU_TIMEOUT_MS`. `firmware/builds/acdc1-build6b-fx4b/`, 108 496 B, SHA-256 `a21f35c990cc33737620597d883c4bd205fc4495bf2291a1b6013af6f2b06307`. `check_itcm --same-itcm` against fx4a: ITCM code and vector table byte-identical. Flashed 2026-11-17 (D55). The open acceptance items 7 and 8 (loop test, noise A/B) apply to fx4b.

**Decision (user, 2026-11-17, D59): fx4b is the daily firmware of acdc1.**

**Fork branch `acdc/fx1d` (pushed 2026-11-17):**
1. `7ef6284a` boot menu (= patch 15b)
2. `2c963e3a` version `v22.4.r-fx4b`
3. `27d3630b` README: section "Boot menu", tables and test status

A build of `2c963e3a` without patches is byte-identical with fx4b (`firmware/builds/verify-fx1d-2c963e3a`, `a21f35c9…`). In addition the release `acdc-v22.4.r-fx4b` (tag on `27d3630b`) with `ACDC-v22.4.r-fx4b.bin` and `BUILD_INFO-v22.4.r-fx4b.txt`.

**Fallback:** fx4a (`e7ee9b90…`), then fx3l (`b55b94d8…`), after that 3d as before.

### Build 7 – MIDI send path atomic, `v22.4.r-fx5a` (grilling round, build and acceptance 2026-11-18, lab notebook D62–D64, **daily firmware on acdc1 since 2026-11-18**)

**Reason:** While a patch is running and the computer downloads a slot, data arrives damaged, and afterwards the module may send no MIDI until a restart (D53, D54). Reproduced on fx4b: 19 of 79 downloads damaged, then the hang (D62).

**Bugs in the original code [code]** (the same in `upstream/master`):
1. The audio task, the main loop and the USB interrupt write to the send buffer without protection. The replies to SysEx requests are generated in the interrupt.
2. `write()` calls `transmit()` at every wrap of the buffer, the audio task in every block. `usbd_midi_tx()` sends nothing while the lock is set, the read head advances all the same.
3. Two contexts can start a transfer on the same endpoint twice [hypothesis: the hang].
4. The read head advances when the transfer starts, USB copies from the ring buffer only afterwards.
5. `write()` never checks whether the buffer is full.
6. `SendResourceTask` writes 324 bytes every 2 ms without waiting for room.

**Decisions (user, grilling round 2026-11-18):**
- Check, start and bookkeeping of the transfer are atomic, by masking interrupts, usable from all three contexts. "Only one caller" is not enough, because the interrupt writes too.
- The read head only advances once the transfer has completed.
- A full buffer drops the new message instead of overwriting old data.
- Flow control only in `SendResourceTask`.
- No rescue of the lock by a timeout. If the hang occurs again, it gets a patch of its own.
- Nested messages (a reply from the interrupt in the middle of a SysEx from the main loop) stay out.
- `transmit()` stays in group C of the ITCM, the noise A/B decides. Fallback: new code at the end of the ITCM block, a filler at the old place.

**Implementation (patch `16-midi-tx-atomic.patch`) [code]:**
- `Source/MidiWriter.cpp`, `UsbdMidiTransmitter`: accesses to the buffer state run with interrupts masked (PRIMASK, as in patch 05). `inflight` holds the length of the running transfer, the read head advances at the next call after the lock has been released. The DataIn interrupt stays unchanged.
- `transmit()` leaves the idle case without masking: empty buffer, running transfer or no computer. The audio task only masks in the blocks in which it starts something.
- `write()` calls `transmit()` only when the buffer is full, otherwise it drops the message and reports `midi tx ovf` once (only with a computer on USB).
- `usbd_midi_tx()` returns whether it sent (`usbd_audio.cpp`, the same in `usbd_midi.c` for other devices, untested there).
- `Source/MidiController.cpp`, `SendResourceTask`: only writes when 324 bytes are free, otherwise in the next pass. After 5 s without room the task gives up.

**Build:** `firmware/builds/acdc1-build7-fx5a/`, `v22.4.r-fx5a`, 109 524 bytes, SHA-256 `b69c25b3f469fc6fb793b16569c53a63a7333c32d83c96de4d97b6fb71bdb8ef`. Patches as for fx4b + 16.

**Check without the module [measured, D62]:** `tools/check_itcm.py --ref fx4b` PASSED, 0 FAIL, 0 WARN. ITCM code +48 bytes (`transmit()` 76 → 124 bytes), everything behind it in the ITCM 48 bytes higher, patch heap 48 bytes smaller. 164 of 180 RAM objects at the same address. Flash +1028 bytes.

**Acceptance:**
1. Done (D63): flash with `tools/flash_acdc.py` (first use on the module), readback byte-identical, A1 passed.
2. Done (D63): download stress test with `tools/dump_stress.py`, 240 of 240 downloads intact (TapeDelay 32 %, Tanh3 51 %, Tanh3 with an audio stream), no hang. fx4b in the same session: 19 of 79 damaged, hang.
3. Done (D63): loop test with `phase_slips.py` and `stale_samples.py`, 0 slips, 0 stale samples, also with Tanh3 and during 40 downloads.
4. Done, with a limitation (D64): noise A/B fx4b → fx5a → fx4b → fx5a, 2 × 60 s each. RMS, residual, comb and fs/8 within ±0.5 dB in every block. Mixing products +0.70 dB on average with 2.3 dB of scatter between the two controls, so not decidable. No sign of an effect of the patch.

**Decision (user, 2026-11-18, D65): fx5a is the daily firmware of acdc1.**

**Fork branch `acdc/fx1d` (pushed 2026-11-18):**
1. `bd04588e` MIDI send path (= patch 16)
2. `c222fa49` version `v22.4.r-fx5a`
3. `b4b95e43` README: section "MIDI send path", tables and test status

A build of `c222fa49` without patches is byte-identical with fx5a (`firmware/builds/verify-fx1d-c222fa49`, `b69c25b3…`). In addition the release `acdc-v22.4.r-fx5a` (tag on `b4b95e43`, "Latest") with `ACDC-v22.4.r-fx5a.bin` and `BUILD_INFO-v22.4.r-fx5a.txt`.

**Open:** a small disturbance on channel 2 during downloads (D63).

**Fallback:** fx4b (`a21f35c9…`), then fx3l (`b55b94d8…`), after that as before.

### Build 8 – LED mode in the boot menu, `v22.4.r-fx6a` (agreed and built 2026-11-18, lab notebook D72–D77, **acceptance complete, fallback from fx7a**)

**Reason [measured, D73, D74]:** Every lit input LED shifts the zero point of all inputs by about −2.9e-4 full scale (≈ −2.9 mV, −71 dBFS). A steady light is only a fixed offset, every change is a step, and a dimmed LED repeats the step at the PWM rate (2320.54 Hz): that is the LED PWM line. In daily use the level LEDs follow the signal, so the disturbance is in every recording.

**Decisions (user, 2026-11-18):**
- One LED mode, selectable with knob 2 in the boot menu (the user's suggestion: knob 2 was still free there) and remembered.
- Three modes: normal (as before), clip only (everything dark, red only when an input clips while recording), off.
- The PWM frequency comes separately afterwards in a build of its own, so that its effect stays measurable on its own.
- Not in this build: cleaning up red (nothing of it was measurable in D73), a switch over MIDI during operation.

**Implementation (patch `17-led-mode-boot-menu.patch`, only `ACDC/Core/Src/ACDC.cpp`) [code]:**
- **Boot menu:** knob 2 selects the mode, left third normal, middle clip only, right off. Like knob 1 it only counts after it has been moved (250 of 4096), otherwise the remembered mode stays. The output LEDs show the mode (four, two, none lit) and blink when confirming would change the slot or the mode. In mode off there is nothing that could blink. Cancelling (knob 3, 30 s) and a computer that takes over leave the remembered mode as it is.
- **Storage:** a resource of its own, `ACDC.led`, in the patch flash (4 bytes: mode, ~mode, 'L', 'D'), separate from `ACDC.slot`. fx5a and fx4b still find their slot after a fallback. The same reserve as for the slot (64 KB free): otherwise the chosen mode only holds until the next power-up, and the input LEDs blink red for 1 s. The settings are not touched.
- **Main loop (every 2 ms):** in the dark modes `onLoop()` calls `acdcOnLoopDark()` instead of `acdcOnLoopLate()`. The function switches the eight LEDs off once and then writes no pin and no timer register as long as nothing changes. In mode clip only it keeps measuring the raw inputs while recording and switches an input LED red for 300 ms (only the static pin, green stays off). In mode off this measurement is dropped as well. `PARAMETER_BA…BD` (output levels) keep running in all modes.
- **Menu and slot display** at power-up use the LEDs in every mode.
- **Memory layout:** `acdcOnLoopLate()` is unchanged. `acdcOnLoopDark()` (292 B) and the larger `onLoop()` (24 B) sit in `.text.onLoop` (in ITCM) and take their room from the padding that has been there since 3d (`ACDC_ONLOOP_PAD` 0x1cc → 0x94). `AcdcBootState` grows from 2 to 4 bytes (`.late_bss`).
- The branch without `USE_USBD_AUDIO_TX_PRE_FX` does not know the mode. It is not built.

**Build:** `firmware/builds/acdc1-build8-fx6a/`, `v22.4.r-fx6a`, 110 088 B, SHA-256 `6a3fc427b30ae1043b239f01e5ecf9894db92d9a6ca3dc51b47cc9a6f80260eb`. Patches as fx5a + 17.

**Checks without the module [measured on the computer]:**
- `tools/sim_boot_menu.sh`: 48 cases passed. 18 old menu cases, 15 new ones for knob 2 (selection, hysteresis, cancel, timeout, computer takes over, full storage, two writes for slot and mode) and 15 for the LED loop (`firmware/sim/led_loop_sim.cpp`: what the main loop writes to the LEDs in each mode).
- `tools/check_itcm.py --ref fx5a`: PASSED, 0 FAIL, 0 WARN. ITCM end unchanged at 0x6338, patch heap unchanged at 40 136 B, all 180 RAM objects at the same address.
- ITCM content against fx5a: all functions outside `.text.onLoop` (0x5de8–0x5fb7) are at the same address. 398 of 12 440 bytes differ: 316 in the new code, the rest in the veneers and in branch targets to them, because code moved in flash. Flash +564 B.
- `tools/flash_acdc.py acdc1-build8-fx6a`: offline checks passed.

**Acceptance (status D75, every flash only after approval):**
1. Done (D75): flash with `tools/flash_acdc.py`, readback byte-identical, A1 passed.
2. Partly done (D75): the user selected off and clip only with knob 2, the resource `ACDC.led` was created (+256 B). After power off and on without the menu a dark mode is active (addendum 2026-11-19). Only clip is remembered (clip probe, second addendum). Open: display on the output LEDs according to the user, slot selection as before.
3. Partly done (D75): LED measurement with `owl/test/SchliereLedPathPatch.hpp`. Mode normal as in D74 (2–5 % more). Mode off: shift down to 1.3–1.7 % with the opposite sign, about −37 dB. Remembered dark mode without a stream (addendum 2026-11-19): blinking 0.3 % of normal, static 0.6–2.2 %, the static remainder scatters. Clip only fresh from the menu (third addendum): just as quiet, blinking 0.4–0.5 %.
4. Partly done (D75): mode clip only, negative DC ramp on In 1. When In 1 reaches the threshold, the open inputs jump by −0.08…−0.15 mV, as with a red LED without green. Repeated on 2026-11-19 in the remembered mode: a step of −0.2 mV, in both recordings within 2 ms of the firmware's clip threshold and 220 ms before the converter's limit. So the step is the red LED, and the counter-check in mode off is no longer required. In a repetition the user saw the red LED. Item done except for the size of the step (half as large the evening before).
5. Noise A/B against fx5a in the same session (mode normal), control at the beginning and end, 2 × 60 s each. Plus loop test (`phase_slips.py`, `stale_samples.py`) and `dump_stress.py`. Done on 2026-11-19: `dump_stress.py` without a stream, 240 of 240 downloads fine (D75, fourth addendum). Loop test passed, also with Tanh3 and during 48 downloads (D76). Noise A/B (D77): no sign of a difference, fx5a lies between the two fx6a controls, the session drifts by 2 dB. Found along the way: a program change while a stream is open breaks USB playback (D76), the same under fx5a (D77), so it is older than Build 8. **Acceptance complete.** As the daily firmware the user then chose fx7a (2026-11-19), fx6a is the fallback.

**Planned afterwards (a build of its own):** LED PWM at exactly 48 000 Hz (timer prescaler 4, 1000 steps instead of 2320.54 Hz with 1024 steps). [hypothesis] The switching frequency is then above the audible range and in step with the sampling, the line disappears. Risk: twenty times as many switching edges. The slow shift of the zero point with the brightness stays. → Build 9.

**Fallback:** fx5a (`b69c25b3…`), then fx4b (`a21f35c9…`), after that as before. The resource `ACDC.led` does not disturb older builds.

### Build 9 – LED PWM at 48 kHz, `v22.4.r-fx7a` (agreed and built 2026-11-19, lab notebook D78, D79, **daily firmware on acdc1 since 2026-11-19**)

**Reason [measured, D67, D73, D74]:** A dimmed LED switches the zero point shift at the PWM rate, which is the line at 2320.54 Hz with harmonics on inputs and outputs (up to −39.8 dBFS at the UMC with dimmed green, D73). Build 8 lets the LEDs go dark, Build 9 moves the PWM itself out of the audible range. Built separately so that the effect stays measurable on its own (user's decision, 2026-11-18).

**Clocks [code]:**
- Timers: HSE 8 MHz, PLL1 × 120 / 2 = 480 MHz system clock, AHB /2, APB1 and APB2 /2 = 120 MHz, timer clock ×2 = 240 MHz. Matches the measured 2320.54 Hz = 240 MHz / (101 × 1024) (D60).
- Audio: SAI1 from PLL3 (8 MHz / 7 × (172 + 262/8192) / 8 = 24.576 MHz), SAI1 block A is master (`SAI_MODEMASTER_RX`), the codec is slave, frame 256 bits. fs ≈ 47 999.995 Hz (measured "exactly 48 kHz", D10).
- Both come from the same crystal. With prescaler 4 and period 999 the PWM runs at 240 MHz / 5000 = 48 000.000 Hz, 0.1 ppm (0.0049 Hz) above fs. A drift of the crystal hits both alike. [hypothesis] Whatever folds from the PWM into the ADC data lands at ≈ 0 Hz (a beat every 204 s) instead of at 2321 Hz with harmonics. 48 kHz itself lies in the stop band of the codec's decimation filter.

**Who uses the timers [code]:** only `MX_TIM2/3/4/8_Init()` in `main.c`, `initLed()` (start of the eight channels) and `setLed()` (`CCR`). No code reads `ARR`, `CNT` or `PSC`. The `htim8` references in `Source/Codec.cpp` belong to other codecs (`USE_IIS3DWB`, `USE_ADS1294`) and are not built for the AC/DC. The simulators do not compute with PWM values.

**Decision (user, 2026-11-19): variant A, only the timer init.** `setLed()` lives in ITCM (0x5cd8, 204 B) before `.text.onLoop`, any change there would move the addresses behind it. Variant B (exact conversion to 1000 steps in `setLed()`) is therefore discarded.

**Implementation (patch `18-led-pwm-48k.patch`, only `ACDC/Core/Src/main.c`) [code]:**
- TIM2, TIM3, TIM4, TIM8: prescaler 100 → 4, period 1023 → 999.
- `setLed()` stays: `pwm = 1024 − v` with v = 0…1023, mode PWM1, the LED is lit at CNT ≥ CCR. CCR ≥ 1000 is above ARR, the LED stays off permanently: that is NO_COLOUR and all values v ≤ 24 (below 2.4 %). v = 1023 gives CCR = 1, so 999/1000 on. Above that the brightness is (v − 24)/1000 instead of v/1024, at most 2.4 % off. "Off" stays off, nothing overflows. Red (static pin) is untouched.
- Consequence: very faintly glowing level LEDs go dark. Patches that set LEDs below 2.4 % show nothing any more.

**Build:** `firmware/builds/acdc1-build9-fx7a/`, `v22.4.r-fx7a`, 110 088 B (as fx6a), SHA-256 `cac6fee0f86426aed3d9b5bfaa2ff758b69de59ed7e11971f2a2ba0d0233ff20`. Patches as fx6a + 18.

**Checks without the module [measured on the computer, 2026-11-19]:**
- `tools/check_itcm.py --ref fx6a --same-itcm fx6a`: PASSED, 0 FAIL, 0 WARN. ITCM boundaries 0x32a0–0x6338 the same, `.itcm_text` (12 440 B) and vector table byte-identical, all 656 flash functions and 180 RAM objects at the same address.
- Binary against fx6a: 113 bytes differ, all in `main()` (timer init, same length, `movs #4` / `movw #999` instead of `#100` / `#1023`) and one in the version string.
- `tools/sim_boot_menu.sh`: all cases passed (boot menu and LED loop, unchanged against fx6a).
- `tools/flash_acdc.py acdc1-build9-fx7a`: offline checks passed.

**Risks [hypothesis]:** twenty times as many switching edges (only a measurement shows whether more couples in at high frequencies). The shift of the zero point with the mean brightness stays (−2.9e-4 per LED, D74). 48 kHz directly at the output (≈ 0.15 mV per LED, D74) is inaudible; at the UMC a remainder would fall to a few Hz because of its own clock. The beat of 204 s can let the DC level wander very slowly.

**Acceptance (every flash only after approval, only acdc1):**
1. Done (D78): flash with `tools/flash_acdc.py acdc1-build9-fx7a --yes`, readback byte-identical, restart by the user, A1 passed. In D79 restarted twice via `:leave` (fx6a and back).
2. Done (D78): LED line at the output with `owl/test/SchliereLedTestPatch.hpp`, phase "green 60 %": **no line any more** at 2321 Hz and harmonics (−85.2 dBFS in the noise against −39.8 dBFS under fx5a, D73), no new line, also not below 20 Hz.
3. Done (D78): LED shift at the inputs with `owl/test/SchliereLedPathPatch.hpp`: the same as fx6a in D77 (±2 %), as expected.
4. Done (D79): noise against fx6a, control at the beginning and end: fx7a at the end within 0.15 dB of fx6a, the LED PWM line is also missing in the raw inputs (fx6a: −115 dB). The control at the beginning is 1.9 dB lower in the comb, a cold-start probe shows: session drift. Loop test passed (D79): 0 slips, 0 stale samples. **Acceptance complete. fx7a is the daily firmware (user's decision, 2026-11-19).**
5. Done (D78): brightness of the LEDs on the module fine according to the user.

**Fork branch `acdc/fx1d` (pushed 2026-11-19):**
1. `1cf56d3e` LED mode (= patch 17)
2. `34782dea` version `v22.4.r-fx6a`
3. `bd5ee463` LED PWM at 48 kHz (= patch 18)
4. `351b2071` version `v22.4.r-fx7a`
5. `13b58412` README: section "LEDs: mode and PWM rate", tables, test status, `:leave` in the flash procedure

Builds of `34782dea` and `351b2071` without patches are byte-identical with fx6a (`firmware/builds/verify-fx1d-34782dea`, `6a3fc427…`) and fx7a (`verify-fx1d-351b2071`, `cac6fee0…`). In addition the release `acdc-v22.4.r-fx7a` (tag on `13b58412`, "Latest", 2026-11-19) with `ACDC-v22.4.r-fx7a.bin` and `BUILD_INFO-v22.4.r-fx7a.txt`. fx6a has no release of its own.

**Fallback:** fx6a (`6a3fc427…`), then fx5a (`b69c25b3…`), after that as before.

### Fork `m9dfukc/OpenWare` (pushed 2026-11-14: https://github.com/m9dfukc/OpenWare/tree/acdc/thru-usb-feedback)

- **Local clone:** `firmware/OpenWare`. The branch was prepared in a separate clone `firmware/fork/OpenWare`. During the cleanup (2026-11-14) both were merged: `upstream` fetched, checked that all 55 refs, 27 branches, 27 tags and all commits of the old mirror are contained, then the mirror deleted and the fork clone moved to `firmware/OpenWare`. Remotes:
  - `fork` = `git@github.com:m9dfukc/OpenWare.git`
  - `upstream` = RebelTechnology (all branches as `upstream/*`)
- **Branch `acdc/thru-usb-feedback`** from `db9d3dd` (v22.4.r, hack branch `hack/acdc-output-levels`, submodule Libraries `9e8f64e`). Commits in this order:
  1. `85dd465c` GCC 12 (patch 01)
  2. `21837c5d` revert `237c63d` (02)
  3. `3cfa66dd` atomic RX counter (05)
  4. `174ef59a` output 125 (04)
  5. `6753794f` feedback control (06)
  6. `06430d10` version `v22.4.r-thru1d`
  7. `41fb9480` README (English, pushed 2026-11-15). Structure as for `acdc/fx1d`, but with standard routing (the computer records the patch output) and measured values of 1d (D24, module dBFS)

  Commit messages and code comments are in English. The author is the user's global git identity, plus a Co-Authored-By trailer.
- **Check:** The tree of the branch tip is equal to the source tree of Build 1d (at that time `firmware/build/acdc1-build1d-thru1`, deleted during the cleanup 2026-11-14, can be regenerated with `tools/build_acdc.sh`). It differs only in comments (`usbd_audio.cpp`, `hardware.h`), the code without comments is identical, the line counts are the same. `usbd_audio.cpp` has CRLF line endings, they are preserved. A build from the branch to confirm the SHA is still pending (approval).
- **Push (user or after approval):** `git -C firmware/OpenWare push -u fork acdc/thru-usb-feedback`. The push also uploads the hack branch commits up to `db9d3dd`, even if the fork contains only `master`.
- **For a PR against upstream** 01, 05 and 06 would have to be ported to `master` (v22.5.0, new HAL) and tested there (Option A). 02 and 04 are acdc-specific and belong only in the fork.

### Order

1. Install the toolchain (user), write `tools/build_acdc.sh`, reproduction build + comparison with the readback.
2. Build Build 1 and Build 2 (no flash yet).
3. Preconditions E7: boot pad probe, reference recording, dry run. Dry run only after approval.
4. Flash Build 1 (approval) → A1–A7.
5. Flash Build 2 (approval) → A1–A6, B1–B3. **Done 2026-11-15:** `v22.4.r-fx1d` (1d base), all acceptance tests passed (D25–D27).
6. Noise experiments (E3). **Status 2026-11-16:** Instead of E3 came the placement in memory (Build 3, D33) and the hot path in the ITCM (Build 4 and 5, fx3l). Block size 16, LED PWM and codec HPF are open.
7. Option A: v22.5.0 or upstream `master` + old HAL + shmuga fixes + `TX_PRE_FX`, acceptance test as for Build 2 and comparison with fx3l. Stays on the plan for later.
8. Auto-switching (open). Public fork: done, branches `acdc/thru-usb-feedback` and `acdc/fx1d`.

### Discarded or superseded

- The earlier build recipe (v22.5.0 + `5a3f964` + `TX_PRE_FX` as the first build) is replaced by E1/E2 and lives on as Option A.
- The "zero-effort pre-test" is done (negative, 2026-11-14), because the firmware on acdc1 contains `237c63d`.
- "Save the release `ACDC.bin` as a known good binary": it is not a safe fallback (USB breakage). The fallback is the DFU readback.

## Flashing – general notes

- Route 1: OpenOCD via ST-Link (`program ACDC.bin 0x08000000 verify reset exit`, configuration stlink + stm32h7x, thread #2083 #15/#28). Never used in the project. With an ST-Link the firmware can also be debugged via SWD (connector J1 on the Xibeca board, 2×5 pins on a 1.27 mm pitch, unplug the module's USB when flashing via SWD, thread 2083 #19). Programmer: [STLINK-V3MINIE](https://www.st.com/en/development-tools/stlink-v3minie.html), software: [OpenOCD](https://openocd.org/).
- Route 2: ST ROM DFU, either via SysEx `0x7E` (`owl_read.py --reset-to-dfu`, corresponds to "Reset to bootloader" on openwarelab.org/Tools/firmware.html) or via the boot pads at power-on. The AC/DC (Xibeca) has **no** OWL MIDI bootloader, only the ROM DFU.
- The ROM DFU cannot be overwritten, so real bricking is practically ruled out. A build with broken USB is risky: then only boot pad/DFU or SWD still works.
- Flash only acdc1 (test module). acdc2 (DIY, v22.4.q) stays the reference.

## Long term

A clean, public ACDC branch with TX_PRE_FX, USB fixes, a documented Libraries revision, LED PWM outside the audio band and measurement data would be what the forum is missing.

**Status 2026-11-16:** The branch `acdc/fx1d` in the fork has this except for the LED PWM (README with measured values, tip `b7062ef2`). The forum posts in thread #2072 and #2244 are dropped (user 2026-11-16). Possibly the results come as a GitHub issue instead (`TODO.md`).

## DFU readback acdc1 (prepared 2026-11-14)

Goal: Back up the firmware of acdc1 purely by reading. It is presumably a non-public build with working USB (see `messlog.md` D2, `docs/research/notes/firmware_update_threads_2026-11-14.md`). Then comparison with the release `ACDC.bin` (`firmware/releases/v22.5.0/ACDC.bin`, 109 080 B, SHA-256 `5f44a811…892c2b`).

Tools (all in the project, read-only except for the DFU restart):
- `tools/owl_read.py --reset-to-dfu --yes`: sends SysEx `0x7E` → `device_dfu()` (magic word + reset → ROM DFU) [code]. Aborts if the connected module is not acdc1.
- `tools/dfu_readback.sh`: only `dfu-util -l` and `dfu-util -U` (128 KB from `0x08000000`), overwrites nothing. Stored in: `backup/acdc1/<datum>/`.
- `tools/compare_firmware.py <readback> <release>`: SHA-256, byte diff, vector table, version strings.

Procedure:
1. User: install `dfu-util`.
2. OWL web pages closed, audio software closed. Only acdc1 connected to the computer via USB.
3. `owl_read.py --reset-to-dfu --yes` (outside the sandbox, because of CoreMIDI). The AC/DC disappears as an audio/MIDI device.
4. `dfu_readback.sh` (outside the sandbox, because of USB). If no `0483:df11` appears: unplug USB at the front, try Micro-USB at the back on the Xibeca board. **Never both at the same time.** If necessary, the boot pads.
5. Case off **and USB cable unplugged**, wait a few seconds, case on, then USB plugged in again → normal firmware. Case off/on alone is not enough, because the USB cable keeps powering the Xibeca board and it stays in DFU (measured 2026-11-14, cf. thread 2083 #7). Check with `owl_read.py` that acdc1 reports "v22.5.0" again and slot 1 runs.
6. Run `compare_firmware.py`, result into the lab notebook (D3).

Risks: If RDP level 1 is active, `-U` fails. Then do not attempt an RDP change, because it erases the flash. Continue only via SWD. No `-D`, no `:leave`, do not write option bytes. The ROM DFU does not reach the QSPI flash (patches, settings). The patches are backed up via SysEx (D1).
