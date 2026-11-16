# Fork update 2026-11-14 (XponentOneAudio, shmuga, hirnlego, burstMembrane, SonBonAudio, antisvin)

Method: GitHub REST API (`/users/<u>/repos`, `/repos/.../branches`, `/compare`), shallow clones of new repos into `$TMPDIR/forks`, and string checks against the full OpenWare clone in `firmware/OpenWare`. Baseline: `openware_forks_complete.md` (2026-10-23). Questions: (1) anything that explains or fixes the missing input → output pass-through on the AC/DC without host playback, (2) anything else useful (noise, USB, backups, standalone FX).

## Summary

- No fork contains a firmware change that explains acdc1's missing pass-through. No fork touches `usbd_rx_convert()`. The thru-mute hack `237c63d` exists only on upstream `hack/acdc-output-levels`, which hirnlego mirrors unchanged.
- **New and useful: shmuga/lich-patcher** (2026-10-18). A browser tool (Web MIDI + SysEx) that speaks the generic OWL protocol. It can **download stored patches and resources from the device** and **read firmware settings**. These are read-only operations, so we can back up acdc1 (slot-1 patch, settings resource) before any change, and check the stored `audio_blocksize`, `program_index` etc.
- **New and useful: burstMembrane/acdc-patches** (2026-04-02). Standalone-FX patches written for the AC/DC on burstMembrane's PRE_FX firmware (`burstMembrane/OpenWare 20d322d`, already known). This is a precedent for the "AC/DC as FX" goal, including a channel/LED helper.
- XponentOneAudio: 49 new commits since 2026-10-19 on `ccr-caea708d-dnrfe4`, all under `Patches/` (Lich "Pearls"). Not relevant.
- shmuga/OpenWare `lich3-usb-fixes`: unchanged since 2026-10-18 (fixes already in the backport list, `docs/05`).
- hirnlego/OpenWare-fork: last push 2026-07-30, unchanged. OwlProgram-fork 2025-09. Not relevant.
- SonBonAudio: only Daisy repos (libDaisy, DaisySP, DaisySeedMidiBoot). Not relevant.
- antisvin: no pushes since 2023. `PyOwlControl` (2020) is an old Python/Qt OWL MIDI control tool. `OpenWareLab` fork is from 2021 and predates the AC/DC.
- The openwarelab.org firmware page links to `github.com/pingdynasty/OpenWare/releases`. That repo is a redirect to `RebelTechnology/OpenWare` (same repo id 94117107), so the update page serves the same v22.5.0 `ACDC.bin` (109080 B) that we string-checked. The page itself accepts only `.syx`, and AC/DC firmware is `.bin` (DFU).

## shmuga/lich-patcher

- Repo: https://github.com/shmuga/lich-patcher (HEAD 9e44802, 2026-10-18). Hosted at https://lich.markorel.ninja/ (Netlify). Static frontend; an optional closed-source compile server is used only for building Pd patches.
- `src/js/protocol.js` follows `Source/OpenWareMidiControl.h`, `FirmwareLoader.hpp`, `MidiController.cpp`. SysEx header `F0 7D 52 <cmd> … F7`.
- `docs/details.md` protocol notes:
  - Download: `0x18 <slot>` makes the device stream the stored slot back in the `0x10` upload format, with CRC32. **Resources are slots `40 + n`**, so the stored settings resource can be fetched too.
  - Requests via CC67: `127` info, `1` patch names, `3` settings (plus program and A–E), `4` resource names, `0x24` stats. The firmware runs these on one background task, and a new request cancels the pending one.
  - Erase: `0x14 <slot>`. **An empty payload erases all storage.** The tool always sends a slot.
  - CC26 (remote A–D) can hang the H7 over USB-ISR ADC restart. The tool never sends it.
- UI: "Patches" (list, load, **download a slot as .syx**, erase, **back up every slot**), "Device" (firmware/bootloader version, device id, stats, **firmware settings**, restart). It looks for an `OWL-LICH` port by default and lets you pick another port manually. Not tested with `OWL-ACDC` yet.
- Use for this project: back up acdc1 (and acdc2, read-only) and read settings. Avoid Erase, Store and Restart.

## burstMembrane/acdc-patches

- Repo: https://github.com/burstMembrane/acdc-patches (1 commit 78ffa22, 2026-04-02, "Initial commit: ACDC patches for OwlProgram").
- Files: `ACDC.h` (helper: audio L/R = channels 0/1, CV in/out = channels 2/3, input LEDs AA–AD, output LEDs BA–BD, RMS metering), `BypassProcessor.hpp`, `DattorroReverb.hpp`, `DattorroStereoReverb.hpp`, `RingsStereoReverbPatch.hpp`, `GrainzPatch.hpp`/`Grain.hpp`, `TapeDelayPatch.hpp`, `TapeDelay.dsp`/`FaustTapeDelay.dsp`, `Nonlinearity.hpp`, `Delay.h`, `Dummypatch.hpp` (empty `processAudio` = pass-through).
- Paired firmware: `burstMembrane/OpenWare 20d322d` = v22.5.0 + `USE_USBD_AUDIO_TX_PRE_FX` + `USE_USBD_AUDIO_RX_PRE_FX` ("ALLOW Audio passthrough"), Libraries `5a3f964`. With both PRE_FX defines the DAC always carries the patch output, and host playback is written into the patch input. The source has no thru-mute.
- Implication: a source-built v22.5.0 (without `237c63d`) plus PRE_FX is a known AC/DC setup for standalone FX [belegt: repo, not a measured report]. It does not tell us why acdc1's installed v22.5.0 is silent.

## Consequences for the pass-through question (acdc1)

- Hypothesis "different firmware build on acdc1" gets weaker. The official update path serves the checked release binary, and the user had flashed one module before ("fast gebrickt", thread #2244).
- Hypotheses "stale stored settings" (e.g. `program_index` → empty slot / configure mode, `audio_codec_bypass`, blocksize 8 from an older build) and "slot-1 patch differs from the library ACDC patch" (acdc1: 9.93 KB, acdc2: 9.32 KB) get stronger. **Both can be checked read-only with lich-patcher.**
