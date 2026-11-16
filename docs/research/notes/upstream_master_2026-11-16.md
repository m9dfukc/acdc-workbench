# Upstream `master` after 2023 – merge check and candidate builds (2026-11-16)

Question (user): merge what upstream `master` has changed since our base, especially the build chain, and maybe switch to current `master`?

Method: `gh api` (commits, branches, PR #89, Actions runs), one `git fetch upstream` in `firmware/OpenWare` (no checkout, no commit), `git log/diff/show`, patch dry-runs in throwaway trees under `firmware/_work/`, three builds with `tools/build_acdc.sh` (Arm GNU 12.2.Rel1, Libraries `9e8f64e`), symbol comparison with `arm-none-eabi-nm -S`. No device access.

## Summary

- **`master` is no longer at v22.5.0.** On 2026-11-15 Martin Klang (pingdynasty) merged PR #89 "Update compiler flags for GCC13+" → `master` = `36eaf1c4` [belegt: GitHub API, fetch]. `develop` stays at `62a01877` (v22.5.0). Only new branch: `feature/gcc15-update` (= the PR). Upstream CI is green on both [belegt: Actions API].
  - https://github.com/RebelTechnology/OpenWare/pull/89
  - https://github.com/RebelTechnology/OpenWare/commits/master/
- The 4 new commits are **build chain only** — no firmware code, no `ACDC/`, no `Libraries` change (submodule still `e102c6f`) [Code]:
  - `632df73a` Add `AGENTS.md` (repo layout/build notes for coding agents).
  - `d5b6409a` Build with GCC 13+: drop `-ffreestanding`, add `-D_GLIBCXX_USE_STD_SPEC_FUNCS=0` in all `Hardware/*.mk` (incl. `xibeca.mk`), `Expander/`, `MidiBLE/`. Commit text: GCC 12.3 output byte-identical before/after; all targets build with 15.3.rel2. PR text: tested with GCC 12, 14, 15; newer GCC gives 1–3 % larger binaries [belegt].
  - `d3df5264` CI: Arm GNU 12.2.Rel1 → **14.3.Rel1**, `actions/checkout@v4`.
  - `36eaf1c4` merge.
- **Patch 08 (cherry-pick of `d5b6409a`) is byte-identical with GCC 12.2** on top of Build 3d [gemessen: build, `cmp`]. It is free to take: zero layout risk, and it opens the door to GCC 13+ later.
- Recommendation: **keep the base `db9d3dd` (v22.4.r) + take 08.** Do not switch the base to `master` now [Hypothese, reasons below].
- Patch 01 (GCC 12 `extern uint8_t`) stays necessary on the hack base: it is upstream `5108fc56` + `fe6eff4f`, which are in v22.5.0 but not in `db9d3dd`. On a `master` base it is redundant.

## Commits `db9d3dd..upstream/master` (60, merge-base `dd7f7fe3`)

The master side does **not touch `ACDC/`, `Source/usbd_audio.cpp`, `Source/pcm3168a.c`, `Source/CircularBuffer.h` or any SAI/clock code** since the merge-base [Code: `git diff --stat dd7f7fe3 upstream/master -- ACDC Source …`]. Every ACDC-specific difference between our base and `master` comes from the hack side (56 commits `upstream/master..db9d3dd`).

### (A) Build chain

| Commit | What | For us |
|---|---|---|
| `d5b6409a` (2026-11-15) | GCC 13+ flags in `Hardware/xibeca.mk` etc. | **useful**, neutral today (byte-identical with 12.2). Taken as patch 08 |
| `d3df5264` (2026-11-15) | CI → GCC 14.3.Rel1 | info only (we build locally). GCC 14 not installed here |
| `632df73a` (2026-11-15) | `AGENTS.md` | neutral |
| `5108fc56`, `fe6eff4f` (2022) | `extern char` → `uint8_t` linker symbols (GCC 12) | = our patch 01 |
| `0fbb77ae` + revert `ec8c7bc2` | RWX LOAD-segment warning flags (owl1/2/3 only) | net zero |
| `3237e7ca` (2023-01-29) | `owl3.mk` flags for new H7 HAL | **not used by ACDC** (ACDC uses `xibeca.mk`). The "Rückbau 3237e7ca" in Option A is therefore unnecessary [Code] |
| `528a0c7c` | `owl3.ld` ITCM 4K → 8K | OWL3 only, not `xibeca.ld` |
| `b806d556`, `ed313997`, `8687d1ee`, `f736430f`, `d2707a7b` | CI 12.2, `Tools/makeprojects.py` ACDC/Lich3/Magus3 targets, MidiBLE dump | neutral |
| `8c569c0e`, `62a01877` | `Libraries` → `8a07845`/`e102c6f` (**STM32H7 HAL v1.11.0**) | **risky**: coincides with the USB break of the release `ACDC.bin` (Thread 2083 #4). Keep `9e8f64e` |

Build files (`Hardware/xibeca.mk`, `xibeca.ld`, `h7.mk`, `common.mk`, `sources.mk`, `ACDC/Makefile`, top `Makefile`) at `db9d3dd` equal `master` except `d5b6409a` [Code]. The hack branch never touched `Hardware/`.

### (B) Shared code relevant to ACDC/H7 (all in v22.5.0, none ACDC-specific)

| Commit | What | For us |
|---|---|---|
| `44ea65c3` | Critical section moved out of `Storage::writeResource()` into callers (`programFlashTask`, settings) | useful in principle (patch/settings store). We never store on acdc1 (E4) |
| `6acdb532` | Settings may live in non-memory-mapped flash; `saveToFlash(bool isr)` with ISR-safe critical section; settings stored with `FLASH_DEFAULT_FLAGS` instead of `SYSTEM|MEMORY_MAPPED`. Struct layout unchanged, so checksum unchanged | neutral (we do not store settings); PR #81 (settings save from USB ISR) is still open upstream |
| `579faefa` | `device_watchdog()` → `device_watchdog_setup()/_tickle()` | neutral (ACDC has no `USE_IWDG`) |
| `c0e05a5d` | `MidiStatus.h`/`MidiMessage.h` from OwlProgram (CC names, RPN enum) | neutral; no SysEx code changed, `owl_read.py` unaffected [Code] |
| MidiHandler/FirmwareLoader (with `5108fc56`) | `saveToFlash(..., getDataSize())`, `allocateBuffer(size + header)`, firmware store slot `0xfe` | bug-fix for SysEx store; unused by us |
| `7d093a98`, `0aae1ba8`, `756b48e1`, `42f68113` | USB host power/logging/NULL check | irrelevant (ACDC has no USB host) |
| `11b45327` | `Pin::getPort()/getPin()` | neutral |

### (C) Other devices

Lich3/Magus3/Witch3/Genius/Lich/MidiBoot3/Wizard commits (`7669abb9` … `5474e2de`, `a433efd5`, `bcf9534a`, `f59446c0`, `fe6a267c`, `ce3a73ac`, `c1c35c6b`, `dcb36bc6`, version bumps, HISTORY). Irrelevant.

## Switching the base to `master` (= Option A)

Dry-run of our patches on a `git archive upstream/master` tree [gemessen: `patch --dry-run`]:

| Patch | On `master` |
|---|---|
| 01 GCC 12 | already applied (redundant) |
| 02 revert `237c63d` | not needed (`237c63d` exists only on the hack branch) |
| 03 TX_PRE_FX + product string | 1 of 2 hunks fails (master `hardware.h` lacks `USBD_SELF_POWERED`, `USBD_AUDIO_*_CHANNELS`) → new patch 10 |
| 04 output gain 125 | fails (master: input gain 104, no comments) |
| 05 atomic RX count | fails (different `ProgramManager.cpp`/USB path) |
| 06 feedback level control | 2 of 4 hunks fail (written for the hack `usbd_audio.cpp`) |
| 07d late-section LEDs | applies textually, but master `ACDC.cpp` has no hack level-LED code → semantics unchecked |

What a `master` base loses compared to Build 3d [Code: hack-side diff]: v22.4.r clock (master: PLL3 P=Q=2, FRACN 0, ≈ 47 991 Hz; hack r: P=Q=8, FRACN 262, codec single rate 0xC1), block size 8 (master 16, `CODEC_BLOCKSIZE 256`), input gain 88 (master 104), 4 TDM slots, SAI OutputDrive off, hack USB path (SOF sync, `CircularBuffer`, feedback) and with it our patches 05/06, the level LEDs. The `master` clock is the original release clock; whether it gives audio on acdc1 is untested (v22.4.s's clock did not, D10) [Hypothese].

So "switching to master" is not a merge but a port: 04/05/06/07d and the clock would have to be re-done on a different USB code base, plus the shmuga H7 USB fixes (`d8fdfa3`, `c5aff8c`, `d39aa53`, `9104f1a`) that are written for exactly that code. Every one of those needs the full A1–A7/B1–B3 acceptance again.

## Candidate builds (not flashed)

All: Arm GNU 12.2.Rel1, Libraries `9e8f64e`, `CONFIG=Release`. Limit 131072 B.

| Build (`firmware/builds/…`) | Base + patches | Size B | SHA-256 |
|---|---|---|---|
| `acdc1-build3d-fx2` (reference, running on acdc1) | `db9d3dd` + 01 02 04 05 06 03 07d | 106788 | `d212cf8d…` |
| `cand-r-fx2d-gcc13flags` | Build 3d + **08** | 106788 | `d212cf8d…` — **byte-identical** |
| `cand-r-merge2250-fx2d` (`v22.4.r-fx2d-m`) | `db9d3dd` + **09** + 02 04 05 06 03 07d 08 (01 is inside 09) | 106816 | `68f51d33…` |
| `cand-master-oldhal-fx` (`v22.5.0-oldhal-fx`) | `upstream/master` `36eaf1c4` + **10** | 104332 | `1b5dd2eb…` |

New patches (existing ones untouched):
- `firmware/patches/08-upstream-gcc13-build-flags.patch` — exact `d5b6409a`.
- `firmware/patches/09-upstream-v22.5.0-shared-source.patch` — `git diff dd7f7fe3 upstream/master -- Source/ ':!Source/device.h'` (the v22.5.0 shared code; `Source/` is unchanged between `62a01877` and `36eaf1c4`). Applies cleanly to `db9d3dd`, our patches 02–07d apply on top without fuzz.
- `firmware/patches/10-master-tx-pre-fx-owl-acdc-fx.patch` — patch 03 adapted to the `master` `hardware.h`.

`cand-master-oldhal-fx` only proves that `master` compiles and links with the old HAL `9e8f64e` [gemessen: build]. It is **not** a usable Option A: release clock, block size 16, no thru fix needed but no feedback fix, no level LEDs, original v22.5.0 USB path without shmuga fixes.

### Symbol addresses vs Build 3d (`arm-none-eabi-nm -S`, address (size), Δ to 3d)

| Symbol | 3d | +08 | merge (09) | master+oldHAL |
|---|---|---|---|---|
| `SAI1_IRQHandler` | `080019ac` | = | = | −0x8 |
| `DMA1_Stream0/1_IRQHandler` | `08001964`/`70` | = | = | −0x8 |
| `OTG_FS_IRQHandler` | `080019d4` | = | = | −0x8 |
| `HAL_SAI_IRQHandler`, `SAI_DMATxCplt`, `SAI_DMATxHalfCplt` | `08003478`, `…334`, `…390` | = | +0x30 | +0x28 |
| `HAL_DMA_IRQHandler` | `0800c258` | = | +0x30 | −0x348 |
| `HAL_SAI_TxHalfCplt/TxCpltCallback` | `08013fa8`/`fc0` | = | +0x64 | −0x484 |
| `audioCallback` | `08014d94` (148) | = | +0x68 | −0x510 (64) |
| `onProgramReady` | `08014c90` (248) | = | +0x68 | −0x560 (328) |
| `usbd_rx_convert` / `usbd_tx_convert` | `08014b54` / `08014c10` | = | +0x68 | −0x4a4 / – |
| `USBD_AUDIO_DataIn` / `DataOut` | `08009630` / `080093f4` | = | +0x30 | −0x4d4 / −0x538 (other code) |
| `usbd_audio_sof_callback` | `0800988c` | = | +0x30 | – |
| `runAudioTask` | `08015054` | = | +0x68 | −0x564 |
| `onLoop` | `08012e3c` (4, jump to `.late_text`) | = | +0x30 | −0x464 (340, master LED code) |
| `programVector`, `hUsbDeviceFS`, `codec_txbuf`/`rxbuf` (`30000000`/`30002000`) | | = | = | = |
| `codec`, `usbd_audio_handle`, `usbd_rx/tx` | `20005fb4`, `20005240`, `20006270/6c` | = | = | −0x20, −0x10, −0x30 |
| `acdc_raw` (`.late_bss`) | `30047fc0` | = | = | – |
| text symbols at the same address as 3d | 554 | 554/554 | 76/552 | 10/544 |

`arm-none-eabi-size` text/data/bss: 3d 106200/580/127992, merge 106228/580/127992, master+oldHAL 103744/580/127900.

Reading: 08 keeps the image identical. 09 shifts the hot audio/USB code by +0x30…+0x68 B (RAM unchanged); D33 showed that a +0x150 B shift moves lines by 1.5–4.5 dB, so 09 needs an A/B against 3d in the same session before it can replace 3d [Hypothese, based on D33]. A `master` base shifts everything [Code].

## Recommendation

1. Take **08** into the standard patch list (or as commit on `acdc/fx1d`): no binary change today, future-proof for GCC 13–15 [gemessen with 12.2].
2. Leave **09** optional. It brings no ACDC function we use (store/settings fixes, watchdog rename, MIDI header refresh). Only worth it if we want to be "v22.5.0 + hack ACDC" for a public branch; then A/B noise against 3d (D33 rule).
3. Do not switch to `master` as base now. Option A stays a separate project (port of clock, 04/05/06/07d, shmuga fixes, full acceptance).
4. GCC 14.3/15: not tested here (only 12.2 installed). Upstream says 1–3 % larger binaries; Build 3d at 106788 B would stay below 131072 B, but every compiler change moves the layout → treat like 09 (A/B) [Hypothese]. Whether the old HAL `9e8f64e` compiles warning-free with GCC 14+ is unchecked.

## Not checked

- Any of the candidates on hardware (no flash).
- GCC 13+ builds (toolchain not installed).
- 07d semantics on a `master` base; `master` clock on acdc1.
