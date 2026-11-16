# acdc-workbench

A workbench for the **Befaco / Rebel Technology AC/DC**, the Eurorack USB audio interface that runs the OpenWare firmware. It reads out the module, records from it automatically, analyses the noise spectrum, builds the firmware reproducibly and documents every flash.

It started as a hunt for the noise in my AC/DC recordings. The tooling that grew around that hunt is now the main result. The firmware itself lives in a fork: [m9dfukc/OpenWare](https://github.com/m9dfukc/OpenWare), branch `acdc/fx1d`, included here as a submodule.

> **Unofficial, and narrow in scope.** Everything was measured on one module, with one computer, on macOS. A second module serves as an untouched reference. Flashing is at your own risk: back up the firmware of your module first.

Deutsche Fassung: [README.de.md](README.de.md)

## What the workbench does

| Tool | Purpose |
|---|---|
| `tools/acdc_rec.py` | Records from the module with a fixed setup (4 channels, 48 kHz), plays test signals (sine, DC, ramps) on the outputs, names the file and writes the entry in `recordings/manifest.toml` |
| `python -m analysis` | Noise analysis of a recording: long-term spectrum, measured line frequencies, line families (USB frame comb, fs/8, mixing products, LED PWM, mains), level over time, report as Markdown, JSON and plots |
| `tools/family_table.py` | Table of family levels across several measurements, with the difference to a control |
| `tools/owl_read.py` | Reads the module over MIDI/SysEx without writing: firmware version, settings, patch slots, status message. Can restart it into the DFU bootloader |
| `tools/dfu_readback.sh`, `tools/compare_firmware.py` | Read the internal flash over DFU and compare it with a reference binary |
| `tools/build_acdc.sh` | Reproducible firmware build from a commit, a pinned library tarball and a list of patches. Writes `BUILD_INFO.txt` with all checksums |
| `tools/check_itcm.py` | Checks an ITCM build on the ELF before it is flashed: what sits where, which calls leave ITCM, comparison with a reference build |
| `tools/phase_slips.py`, `tools/stale_samples.py` | Check a loop-back recording (out → in) for lost or repeated samples and for single stale samples |

## Findings so far

- **Four families of interference lines** sit in the ADC data, strongly correlated across all channels:
  - a comb at k · ≈1 kHz
  - a line at fs/8 = 6000 Hz, the audio block rate at block size 8
  - mixing products of the two
  - an LED PWM line at 2321 Hz
- **The comb follows the USB start-of-frame of the host controller.** Its fundamental changes with the USB port (999.87 to 1000.00 Hz in the module's clock). On the outputs it disappears without USB.
- **Where code sits in flash shifts the lines.** A build that only adds padding, with no change in function, moved the families by 1.5 to 4.5 dB.
- **Running the periodic code from ITCM helps.** With the hot path in ITCM, the fs/8 line drops by about 5 dB, the mixing products disappear, and the result no longer depends on the flash layout.
- **Three timing bugs in the original USB audio code** were found and fixed on the way: a feedback loop that ran open, a race between the RX and TX DMA, and a start-of-frame handler that ran twice per frame.

Firmware `v22.4.r-fx3l` against the previous build `v22.4.r-fx2d`, open inputs, gain at 12 o'clock, 2 × 60 s each, levels in dBFS of the USB stream:

| Measure | `fx2d` | `fx3l` | Difference |
|---|---|---|---|
| RMS ≥ 20 Hz | −77.6 | −78.7 | −1.1 dB |
| Broadband floor without lines | −83.2 | −84.5 | −1.3 dB |
| 1 kHz comb (sum) | −80.9 | −80.6 | +0.2 … +0.4 dB |
| fs/8 line at 6000 Hz | −84.3 | −89.4 | −5.1 dB |
| Mixing products | −90.8 | ≈ −125 | ≈ −35 dB |

![Long-term spectrum of fx3l (black) against fx2d (grey), four channels](docs/img/psd_fx3l_vs_3d.png)

The comb is now the strongest remaining family. `fx3l` has been in daily use on the test module since 2026-11-16; a second noise session is still open. Details and all numbers: [docs/messlog.md](docs/messlog.md) (German), entries D45 to D49.

## Firmware

The fork has two branches:

| Branch | Version | Content |
|---|---|---|
| `acdc/thru-usb-feedback` | `v22.4.r-thru1d` | The patch output reaches the jacks without a computer, plus the USB feedback fix |
| `acdc/fx1d` | `v22.4.r-fx3l` | As above. The computer records the raw inputs, the input LEDs show the raw level while recording, the hot path runs from ITCM |

Both are based on upstream commit `db9d3dd` (v22.4.r) with the libraries at `9e8f64e`. The fork README explains why, and what each change does.

- `firmware/patches/` holds the same changes as numbered patch files. `tools/build_acdc.sh` applies them to a clean tree.
- `firmware/builds/<name>/BUILD_INFO.txt` records commit, toolchain, patch list and checksums of every build. The binaries are not in this repository, each one can be rebuilt byte for byte. Ready-made binaries of `v22.4.r-fx2d` and `v22.4.r-fx3l` are attached to the [releases of the fork](https://github.com/m9dfukc/OpenWare/releases).
- `firmware/flashlog/` has one folder per flash: device report before and after, DFU logs, checksum of the readback.

**Do not flash the official `ACDC.bin` v22.5.0 from the upstream release page onto an AC/DC.** It is reported to break USB ([forum thread](https://community.rebeltech.org/t/ac-dc-firmware-update/2083)).

## Getting started

Requirements: macOS, [uv](https://docs.astral.sh/uv/), `dfu-util` for readback and flashing, Arm GNU Toolchain 12.2.Rel1 for firmware builds.

```sh
git clone https://github.com/m9dfukc/acdc-workbench.git
cd acdc-workbench
tools/setup_repo.sh    # submodule, upstream remote, pinned downloads with checksum
uv sync
```

Record open inputs twice for 60 s and analyse both takes:

```sh
uv run python tools/acdc_rec.py --list
uv run python tools/acdc_rec.py --id T1 --test open-inputs --duration 60 --reps 2 --analyze
```

Check USB stability with patch cables from each output to its input:

```sh
uv run python tools/acdc_rec.py --id L1 --test loop-sine --sine 440 530 670 790 --owl-read
uv run python tools/phase_slips.py recordings/<file>.wav --freqs 440 530 670 790
uv run python tools/stale_samples.py recordings/<file>.wav --freqs 440 530 670 790
```

Read out a module, including all patch slots. This tool needs Python 3.12 and two MIDI packages that are not in `pyproject.toml`:

```sh
uv run --no-project --python 3.12 --with mido --with python-rtmidi \
  python tools/owl_read.py --dump --out backup
```

Rebuild `v22.4.r-fx3l`. The result must have the SHA-256 `b55b94d8734baf1cf763dfefb380a561029bd00d4a645cdcef3b75d99e6f010e`:

```sh
P=firmware/patches
FW_VERSION=v22.4.r-fx3l tools/build_acdc.sh my-fx3l db9d3dd \
  firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz \
  $P/01-gcc12-extern-uint8.patch $P/02-revert-237c63d-thru-mute.patch \
  $P/04-output-gain-125.patch $P/05-atomic-usbd-rx-count.patch \
  $P/06-fb-level-control.patch $P/03-tx-pre-fx-owl-acdc-fx.patch \
  $P/07d-input-leds-raw-late-section.patch $P/08-upstream-gcc13-build-flags.patch \
  $P/11g-itcm-hotpath-rxcb.patch $P/12b-rx-dma-callback.patch \
  $P/14-usbd-sof-once-per-frame.patch
```

The flash procedure (read out, restart into DFU, write, read back, compare, restart) is described in [CLAUDE.md](CLAUDE.md), section "Flash-Ablauf". There is no finished flash script yet.

## Repository layout

| Path | Content |
|---|---|
| `tools/`, `analysis/` | The workbench |
| `docs/` | Reference documents `01` to `05` (German), the lab notebook `messlog.md`, research notes in `docs/research/` |
| `docs/en/` | English versions of the reference documents, see [docs/en/README.md](docs/en/README.md) |
| `firmware/OpenWare/` | Submodule, the firmware fork |
| `firmware/patches/`, `firmware/builds/`, `firmware/flashlog/` | Patches, build records, flash records |
| `recordings/manifest.toml` | Metadata of every recording |
| `out/<ID>/` | Analysis report of each measurement |
| `TODO.md`, `CLAUDE.md` | Open points and the project context used when working with Claude Code |

Not in the repository: the recordings themselves (8 GB of WAV files), plots and JSON results in `out/`, firmware binaries, and the device backups. Plots and results can be regenerated from recordings with `python -m analysis`.

## Language

The working documents are written in German and stay that way, German is the source.

- English versions of the reference documents `01` to `05` and `99` are in [docs/en/](docs/en/README.md). They are generated from the German originals and refreshed at milestones. `python tools/i18n_check.py` lists the ones that are out of date.
- The lab notebook `docs/messlog.md`, the handoff notes, `TODO.md` and `CLAUDE.md` are German only.
- The tools print English help and messages. Reports generated by the analysis are German.
- The research notes in `docs/research/notes/` are English.

## License

Tools MIT, firmware patches GPL-2.0, documents and measurement data CC BY 4.0. Details: [LICENSE.md](LICENSE.md).
