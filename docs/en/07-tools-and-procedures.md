<!-- i18n source=docs/07-werkzeuge-und-ablaeufe.md sha256=d1d1d69379e01761157e061340bc6744bab696dc820ccc5157df1cdc21a79ee0 date=2026-11-27 -->
> English translation of [`docs/07-werkzeuge-und-ablaeufe.md`](../../docs/07-werkzeuge-und-ablaeufe.md), as of 2026-11-27. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 07 – Tools and procedures

What tools the workbench has and how the recurring procedures go: recording, reading out the module, uploading a patch, building and flashing firmware, checking USB stability. `--help` shows all arguments of a tool. The analysis package `analysis/` is described in `03-measurement-plan-python.md`, the plan and result of every firmware build in `05-firmware-plan.md`.

The device tools are tied to the author's test module (acdc1, through the MIDI device ID and the DFU serial number). Measuring and flashing was only done there.

## Environment

- Python runs through **uv** (`uv run`, `uv add`). Other requirements: macOS, `dfu-util`, Arm GNU Toolchain 12.2.Rel1 under `/Applications/ArmGNUToolchain/12.2.rel1/`.
- The **MIDI tools** (`owl_read.py`, `owl_write.py`, `dump_stress.py`, `knob_series.py`) need Python 3.12 and two packages that are not in `pyproject.toml`:

  ```sh
  uv run --no-project --python 3.12 --with mido --with python-rtmidi python tools/owl_read.py
  ```

- Close OWL web pages first, they poll the module.
- In the sandbox of Claude Code, recording (CoreAudio), MIDI (CoreMIDI) and DFU (USB) do not run, these calls need the exception. uv needs `UV_CACHE_DIR=.uv-cache` there.

## Tools in `tools/`

| Tool | Purpose |
|---|---|
| `acdc_rec.py` | Recordings and test signals, the standard since 2026-11-16. Also for other devices (`--device UMC202HD --input-only --channels 2`). `--prompt --progress 1` in the terminal starts on Enter and shows the time once per second |
| `owl_read.py` | Reads the module over MIDI/SysEx (read-only), restarts it into DFU mode |
| `owl_write.py` | Uploads a patch: `--run` (RAM only) or `--store N --yes` (slot in the patch flash). acdc1 only, backs up an occupied slot first, reads back afterwards. `--erase N --yes` erases a slot from 2 upwards, only with a matching local copy given as PATCH (tried on the module on 2026-11-27 with slot 9, the other slots unchanged). `--info` and `--syx-out` run offline |
| `build_owl_patch.sh` | Builds a C++ patch with OwlProgram, SysEx goes to `owl/vendor/builds/` |
| `sim_boot_menu.sh` | Host test of the boot menu logic (patch 15/15b, from Build 8 also knob 2 for the LED mode) with simulated knobs, plus from Build 8 the LED loop per mode (`firmware/sim/led_loop_sim.cpp`) |
| `test_owl_dsp.sh` | Host test of the own patch sources in `owl/` (Tanh3, limiter, Schliere, block-rate canceller, both LED measurement patches). Calls `owl/test/run.sh` in the submodule |
| `dfu_readback.sh`, `compare_firmware.py` | Read the internal flash and compare it with a reference |
| `dump_stress.py` | Download stress test for the MIDI send path: downloads all slots in rounds while a patch runs and counts corrupted downloads. acdc1 only, read-only except for one Program Change. Aborts when the module stops answering (D62) |
| `flash_acdc.py` | Flashes a build to acdc1: offline check, readout, DFU restart, write, readback comparison, flash log, start via `:leave` and A1. See "Flashing" |
| `build_acdc.sh` | Reproducible firmware build from a commit, the Libraries tarball and patches |
| `setup_repo.sh` | Sets up a fresh clone: submodules, `upstream` remote, Libraries tarball and the official `ACDC.bin` with SHA check |
| `check_itcm.py` | Checks an ITCM build on the ELF (`--groups` for variants, `--same-itcm` for padding variants) |
| `phase_slips.py`, `stale_samples.py` | Check loop recordings for sample slips and single stale samples |
| `family_table.py` | Family levels of several measurements, Δ against the control. `--dc-ref/--dc-correct` corrects recordings taken behind the VCA of the default patch through the DC offset (D26, D86) |
| `crosstalk_lines.py`, `click_sensitivity.py` | Crosstalk of the outputs, sensitivity of the click detector |
| `line_levels.py` | Levels of single lines per channel right at the line frequency, for several recordings, with the distance to the noise floor. Matches the hand values from D58 within 0.1 dB |
| `ledpath_phases.py` | Levels per phase of a recording with the measurement patch `SchliereLedPath` at an interface input (e.g. UMC), converted to the output of acdc1 through the calibration tone: RMS, 40 Hz (LED blinking), comb, 6 and 12 kHz (D74, D91) |
| `ab_bands.py` | A/B/A comparison of three recordings (e.g. old build → new → old): RMS, level per third-octave band against the spread of the A runs, new lines, clicks, table as Markdown (D93) |
| `knob_series.py` | Guided series of recordings with the knobs in given positions: reads CC 20–23, waits for the position, records with `acdc_rec.py`, and writes the table `reports/<series>-session-table.md` at the end. `--simulate` runs without a module |
| `i18n_check.py` | Lists outdated English versions in `docs/en/` (checksum of the German source in the header). `--stamp` writes the header after a new translation |
| `doc_check.py` | Checks the documentation before a push: length of `CLAUDE.md`, dead links, dead paths in the current documents, outdated translations, index of the lab notebook (`--messlog-index` rewrites it) |

## Recording

**Always record with `tools/acdc_rec.py`** (decision of 2026-11-16). The early measurements went through a host software with a multichannel recorder, the cross-check of both routes passed (D35). A host software is only needed when a patch has to run in the computer.

- The script opens the device duplex with zeros at the output, 48 kHz, block 256 (like the earlier host software). It writes a 4-channel WAV with 16 bit following the naming convention and creates the entry in `recordings/manifest.toml`.
- Naming convention: `YYYYMMDD_<device>_<test>_<gain>_<usb-state>.wav`, e.g. `20261113_acdc1_open-inputs_g12_usb-stream.wav`.
- Optional: `--reps` with reopening in between, `--owl-read` before closing, `--analyze --ref …`. Length, device, channels and format are arguments.
- Device list: `UV_CACHE_DIR=.uv-cache uv run python tools/acdc_rec.py --list`.

**Test signals:**

- `--sine F1 F2 F3 F4` sends a real sine to each output (0 = silent). Level with `--sine-level` in device dBFS (default −6 ≙ 5 V peak at the output), `--sine-fade` fades in.
- `--dc V1 … V4` outputs a DC component in full scale (−1…1, 1 ≈ 10 V at the output), `--dc-ramp SEC` ramps up slowly.
- `--simulate` with `--sine` is a loopback without a module.

**Rules for noise measurements:**

- Record open inputs twice (2 × 60 s). The comb scatters by ≈ 0.4 dB between runs (D35), and there have been single outliers (D22/D23).
- A/B between builds always against a control in the same session, preferably at the start and at the end. The levels drift by 0.4 to 2 dB within a session (D44, D77).
- All four knobs at 12 o'clock. Knobs set unequally raise lines of their own (D61).
- Note the installation (in the case or beside it) and whether the ground wire is on the module. Values before 2026-11-24 apply without the wire (D90).
- Every measurement gets an entry in `messlog.md`: setup, file, finding, conclusion.

**Level of the early recordings (D7/D8):** Recordings through the earlier host software carry a factor of 2 (+6 dB) between module and file. File dBFS − 6.02 dB = device dBFS. `acdc_rec.py` reproduces this with `scale = 2.0` in the manifest so that old and new files stay comparable.

## Reading out the module, choosing and uploading a patch

- **Reading out:** `owl_read.py` shows version, settings, slots and the last debug message. `--dump --out <folder>` backs up all slots. With a dump, look for `ok` in the report.
- **Reading the knobs:** The settings request returns CC 20–23 (knobs 1–4, 7 bit) in the report under `settings_cc`.
- **Changing the patch from the computer:** `owl_read.py --program N`. This is not remembered. **Only without an open stream**: a Program Change with an open stream breaks USB playback until the next stream start (D76).
- **Uploading a patch:** first `owl_write.py <file> --run` (RAM only), then `--store N --yes`.
  - If the slot is occupied, give the backup with `--backup-file <local copy>`. Size and CRC must match the slot.
  - Slot 1 additionally needs `--allow-slot1`.
  - After a store the stored slot runs, `--program-after 1` switches back.
- **Slot downloads while a patch runs** were unreliable up to fx4b (a race in the MIDI send path of the original firmware, D53, D54, D62). fx5a fixes this: 240 of 240 downloads fine (D63). Test: `dump_stress.py`.
- **Loader page in the browser** for other AC/DC owners: <https://m9dfukc.github.io/acdc-patches/> (source `owl/docs/`, Web MIDI with SysEx, Chromium). It runs, stores or erases a local `.bin` or `.syx` in slots 1–39 and downloads a slot. It refuses slot 40 and above because the firmware takes the slot as a `uint8_t`: on erase, 40 would hit resource 0 and 255 erases the whole storage [code].

**Boot menu on the module** (from fx4b, LED mode from fx6a):

- Powering on with knobs 1, 2, 3 at the left and knob 4 at the right opens the menu. Knob 1 chooses among the occupied slots (it only counts after being moved), knob 4 away from the stop confirms, knob 3 away from the stop or 30 s cancel.
- Knob 2 chooses the LED mode: normal (left third), clip only (middle), off (right).
- The input LEDs show the slot in binary (1–15, LED 1 = 1 … LED 4 = 8).
- Slot and LED mode are remembered as the resources `ACDC.slot` and `ACDC.led` in the patch flash, the settings stay untouched. Without the knob pattern the remembered slot starts, its number is shown on the LEDs for 1 s. If the remembered slot is empty, slot 1 starts [code].
- End values of the knobs: left 2, right 127 of 127 (D51).

## Building OWL patches

- `tools/build_owl_patch.sh` builds a C++ patch with OwlProgram and writes `patch.bin`, `<name>.syx` and `BUILD_INFO.txt` to `owl/vendor/builds/<name>/`. Defaults: sources `SRC` = `owl/patches-private/`, SDK = `owl/vendor/OwlProgram/`, work trees in `owl/vendor/_work/`.
- **SDK:** OwlProgram `60f44ab` with DaisySP `4263388`. `compile.mk` locally carries the flag line of OwlProgram `develop` (without `-fno-builtin`, `-ffreestanding`, `-mtune`), the original lies next to it as `compile.mk.orig-60f44ab`. The flags lower the CPU load of the patches by 5–21 % (D92), at the output no difference can be measured (D93). The script warns about `-fno-builtin` and writes `sdk_flags` to `BUILD_INFO.txt`.
- **Switches:** `LINK=plusram` puts the patch into the AXI SRAM instead of the DTCM (default `patchram`, this is how Plateau is built), `LIMIT=1` wraps an FX patch in the output limiter (`owl/include/AcdcOutput.h`).
- **Host tests:** `tools/test_owl_dsp.sh`. The comparison of Plateau with the original code only runs with `VALLEY_SRC=$PWD/owl/vendor/downloads/vrf245/ValleyRackFree-2.4.5/src owl/test/run.sh`.
- Third-party sources come as a tarball from `codeload.github.com` into `owl/vendor/downloads/`. The builds from before the flag change are in `owl/vendor/builds-archive/`.
- The API finds the sources of unpublished library patches: `https://www.rebeltech.org/api/patch/?seoName=<name>` (metadata with source URL), `/api/patches/` (list). They are kept in `owl/patches-private/library/`.

## Building firmware

- All own builds: base `db9d3dd` (v22.4.r, branch `hack/acdc-output-levels`), Libraries `9e8f64e` (old H7 HAL), built with `tools/build_acdc.sh` and Arm GNU 12.2.Rel1, deterministic. The call for the current firmware is in the English `README.md`, "Getting started".
- `build_acdc.sh` does not depend on the checked-out state of `firmware/OpenWare`, it fetches the commit with `git archive`.
- Patches, builds and their results: `firmware/README.md`.

**Rules for new firmware:**

- Code that runs periodically belongs in the ITCM (linker patch 11g). Every ITCM build goes through `tools/check_itcm.py` before the flash.
- Without the ITCM the old rule applies: put new code at the end (`.late_text`/`.late_bss`) or check the addresses with `nm` against the reference build. The position of the code in flash shifts the interference lines (D33).
- No polling loops at block rate (D42).
- The loop check always runs with `phase_slips.py` **and** `stale_samples.py` on the same WAV.
- A new daily build gets a release of its own at the fork, only after approval.

## Flashing

Without the pads, DFU through the front USB-B socket. Every flash only after approval, acdc1 only, never write settings. Before every intervention read out and back up settings and slots.

**By hand:**

1. `owl_read.py --out <flashlog>/owl_read_before`
2. `owl_read.py --reset-to-dfu --yes`
3. `dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000 -D <bin>`
4. Readback with `-s 0x08000000:131072 -U`, compare with the binary and check for 0xFF
5. Starting the firmware: a second, read-only readback with `-s 0x08000000:131072:leave -U` (the standard since 2026-11-19, D79). The ROM DFU then starts the firmware, `dfu-util` ends with "Error during download get_status", which is normal. No cold start, the codec stays powered
6. A1 with `owl_read.py`: version, `SR/BS/CH 48000 8 4`, slots unchanged

**Cold start** (case off, USB off, case on, USB on; case off alone is not enough, USB powers the board) only in these cases: `:leave` fails, a build changes something at power-on (clock, codec init), the test concerns power-on (boot menu, remembered slot or LED mode after off and on), or the way back after a problem.

Each flash gets a folder in `firmware/flashlog/`.

**As a script: `tools/flash_acdc.py`** (outside the sandbox). It runs steps 1–6, with `--cold` only 1–4 and step 6 after the restart by hand.

- `python3 tools/flash_acdc.py <build>`: only the offline check (size, vector table, version, SHA against `BUILD_INFO.txt`, `check_itcm.json`). `<build>` is a `.bin`, a build folder or a folder name in `firmware/builds/`.
- `… <build> --yes [--name <log>]`: flashes acdc1. The MIDI device ID and the DFU serial number are checked. The log folder is called `firmware/flashlog/<date>_<name>` (default: build folder without `acdc1-`), an existing one is never reused (then e.g. `--name …-zurueck`).
- After the readback: `:leave`, wait until the DFU device disappears (`--leave-wait`, 10 s), then A1 with up to three attempts. Exit 6: `:leave` did not work or acdc1 does not answer over MIDI, then restart by hand and `--a1`. Exit 7: A1 passed, but the second readback differs.
- `--cold`: no `:leave`, wait for the restart by hand after the readback.
- `… --a1 <log folder>`: after a restart by hand. Checks the device, version, 48000 Hz, block size 8 and the slots against the state before the flash. It does not check the channel count.
- `--from-dfu`: acdc1 is already in DFU mode, e.g. after a failed flash. Then do not restart, but flash the fallback with it.
- If it aborts before anything was written, it renames the log folder to `…-abgebrochen-<time>`.

**Tried:** three flashes with readback and `--a1` (D63/D64), `:leave` by hand (D79) and from the script (D84, D88). `--from-dfu`, the abort path and the error paths (stays in DFU, no MIDI, differing readback) only ran against dummies.

**Fallbacks for acdc1**, each with `flash_acdc.py <build>`: from fx9a to fx8a (`e1b1097b…`), then fx7a (`cac6fee0…`), fx6a (`6a3fc427…`), fx5a (`b69c25b3…`), fx4b (`a21f35c9…`), fx3l (`b55b94d8…`), 3d (`d212cf8d…`), Build 2, 1d. The last fallback is the readback of the factory firmware in `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (`433b3fd3…`). The official `ACDC.bin` v22.5.0 is **not** a fallback: according to the forum it breaks USB (thread 2083 #4).

Flashing via ST-Link and the boot pads: `05-firmware-plan.md`, "Flashing – general notes".

## Checking USB stability (loop test)

- Patch cables out n → in n, gain at 12 o'clock, `tools/acdc_rec.py --sine 440 530 670 790 --owl-read`, 60 s.
- Then `tools/phase_slips.py --freqs 440 530 670 790` and `tools/stale_samples.py` on the same WAV.
- **Before every cable from an output to an input, check which patch is running.** An FX patch that passes this input to this output (Schliere, measurement patches with gain) forms a feedback loop with it. First switch to slot 1 or open the stream, then plug in (D75).
- **Choose the patch before opening the stream**, never while it is open (D76).
- Read the module's message **before** the stream closes (`--owl-read` does that).
- Through the loop an input can only be overdriven with a negative voltage (`--dc … -1`), because of the negative input offset (D36, D75).

**Debug messages** (PROGRAM_MESSAGE, only the last one stays):

| Message | Meaning |
|---|---|
| `rx unf 0.9513 0.4722 4.0000` | underrun in the middle of a run |
| `rx unf 1.0000 … 32` | buffer empty, typical at the end of a stream |
| `tx ovf 1.0000 1.0000 32` | typical at the start of a stream |
| `fb <old> <new>` | feedback measurement discarded, e.g. ≈ 32 ms without SOF (D18) |
| `fb clamp` | controller at its limit, a sign of an error while a stream runs (D38). Occurs after a Program Change with an open stream (D76) |
| `midi tx ovf` (from fx5a) | MIDI send buffer full, one message was discarded |
| `Sending 100` | progress display after a slot download, not an error |

## Checking the documentation

- `python3 tools/doc_check.py` before every push: reports a `CLAUDE.md` over 200 lines, dead links, dead paths in the current documents, outdated English versions and an outdated index in the lab notebook.
- After a new entry in the lab notebook, `python3 tools/doc_check.py --messlog-index` rewrites the index at the top of `messlog.md`.
- `python3 tools/i18n_check.py` alone lists the outdated versions in `docs/en/`. After a new translation `--stamp <file>`.
