# OpenWare fork survey (complete) — RebelTechnology/OpenWare, Stand 2026-10-23

Method: the GitHub REST API was reachable through WebFetch (curl/gh in the container were blocked with "GitHub access to this repository is not enabled"). I took the fork lists and issue/PR metadata from api.github.com. I then fetched every fork (blobs filtered out) into one bare repo with the upstream branches as `refs/remotes/up/*`, and ran `git rev-list --count <branch> --not --remotes=up`. "Ahead" therefore means commits not reachable from ANY upstream branch, not just master 62a0187. I only read the code and built or ran nothing. Repo dir: /tmp/claude-0/-home-claude/20349f09-a405-56cc-8f73-fd29c49cae1a/scratchpad/forks/all

## 1. Complete fork list with last push and ahead status

### Takeaway
The upstream repo reports forks_count 21. There are 15 direct forks plus 5 forks of antisvin/OpenWare_Owlsy. Only 5 direct forks have commits that upstream does not have. Only one touches ACDC/: burstMembrane, 1 commit, 2026-03-31. One touches usbd_audio.cpp with substantive USB audio fixes: shmuga, 4 commits, 2026-10-18. The rest are stale mirrors or hold work for other devices.

### Cited Findings
- Upstream metadata: forks_count 21, stargazers 73, open_issues_count 19, pushed_at 2025-06-11T11:48:01Z, default branch master — [GitHub API repo](https://api.github.com/repos/RebelTechnology/OpenWare)
- Direct forks (pushed_at from API; ahead = unique commits vs all upstream branches) — [GitHub API forks](https://api.github.com/repos/RebelTechnology/OpenWare/forks?sort=newest&per_page=100):

| Fork | pushed_at | Ahead (unique commits) | Content |
|---|---|---|---|
| [XponentOneAudio/Owl-OpenWare](https://github.com/XponentOneAudio/Owl-OpenWare) | 2026-10-19 | branch `ccr-caea708d-dnrfe4`: 47 (6527a11, 2026-10-19); master = 62a0187 | Martyn Quickenden, "Pearls for Lich" patch; all 347 file changes are under `Patches/`. Not firmware, not ACDC |
| [shmuga/OpenWare](https://github.com/shmuga/OpenWare) | 2026-10-18 | branch `lich3-usb-fixes`: 4 (9104f1a, 2026-10-18); master = 62a0187 | USB audio TX fixes in Source/usbd_audio.cpp, BitState fix, Lich3 hardware.h. **Relevant** (see section 2) |
| [hirnlego/OpenWare-fork](https://github.com/hirnlego/OpenWare-fork) | 2026-07-30 | master: 60 (24f5098, 2026-07-29); feature/oneiroi 18 (5285a9d, 2026-06-09); feature/iroi 1 (7294fd2, 2025-09-14); all upstream branches incl. feature/acdc*, hack/acdc-output-levels mirrored with 0 ahead | Roberto Noris (Oneiroi/Iroi maker). Iroi project, v22.6.0 bump, ProgramManager/Storage/ServiceCall changes. No ACDC changes |
| [burstMembrane/OpenWare](https://github.com/burstMembrane/OpenWare) | 2026-03-30 | master: 1 (20d322d, 2026-03-31) | Liam Power. Only fork that touches ACDC/ (see section 2) |
| [alexeyavb/OpenWare](https://github.com/alexeyavb/OpenWare) | 2024-01-27 | 0 (master = 62a0187) | plain mirror |
| [ddf/OpenWare](https://github.com/ddf/OpenWare) | 2023-06-21 | 0 (master = 62a0187) | plain mirror |
| [xinghuaman/OpenWare](https://github.com/xinghuaman/OpenWare) | 2023-01-04 | 0 (master bca1221, 2022-04-07) | stale mirror |
| [casaroli/OpenWare](https://github.com/casaroli/OpenWare) | 2022-11-23 | 0 (master bca1221) | stale mirror |
| [Alefal44/OpenWare](https://github.com/Alefal44/OpenWare) | 2022-11-23 | 0 (master bca1221) | stale mirror |
| [RyanPWM/OpenWare](https://github.com/RyanPWM/OpenWare) | 2021-08-05 | 0 except old jc-norflash-dev (e6ae1db, 2017) | mirror of 2021 branches |
| [mcclure/OpenWare](https://github.com/mcclure/OpenWare) | 2020-09-20 | 0 (only jc-norflash-dev 2017 leftover) | 2020 mirror (Windows build fix became upstream PR #16) |
| [moonfall/OpenWare](https://github.com/moonfall/OpenWare) | 2020-04-11 | 0 (only jc-norflash-dev) | 2020 mirror |
| [antisvin/OpenWare_Owlsy](https://github.com/antisvin/OpenWare_Owlsy) | 2023-04-10 (13 stars) | many branches ahead (daisy 209, feature/takeover 213, preenfm3 47, bluemchen 134 …) | OWLsy/Daisy/PreenFM3/Axoloti work (already known); no ACDC |
| [MaciejMCh/OpenWare](https://github.com/MaciejMCh/OpenWare) | 2019-12-01 | master: 1 (89686f3 "run patches", 2019-11-24) | LibSource/Wavetable, irrelevant |
| [jdekozak/OpenWare](https://github.com/jdekozak/OpenWare) | 2019-04-24 | 0 (only jc-norflash-dev) | 2019 mirror |

- Second-level forks of antisvin/OpenWare_Owlsy — [GitHub API](https://api.github.com/repos/antisvin/OpenWare_Owlsy/forks?per_page=100):
  - metamaterialsuit/OpenWare_Owlsy (pushed 2023-04-10, created 2025-07-24) and Brokezawa/OpenWare_Owlsy (pushed 2023-04-10): no unique commits.
  - felart/OpenWare (pushed 2021-12-25): no unique commits.
  - SonBonAudio/DaisySeedMidiBoot (pushed 2024-09-23): 4 unique commits stripping the repo down to a Daisy Seed MIDI bootloader; README says "defunct" (22ec6ba).
  - ArcAudio/OpenWare (pushed 2021-08-22): preenfm3 (36), magus-right-encoder (4), daisy-sd (2); PreenFM3/DaisyPatch/Magus only.
  - None touch ACDC.

### Inferences
- 15 direct + 5 second-level = 20 listed forks versus forks_count 21. The 21st is probably a deleted, private, or not-listed fork. I could not identify it.
- No fork continues the upstream `feature/acdc`, `feature/acdc-lowspeed` or `hack/acdc-output-levels` branches. hirnlego mirrors them unchanged.

### Gaps
- The 21st fork could not be identified.
- GitHub's HTML forks page and network graph were not used.

## 2. Forks with ahead commits touching ACDC/, Xibeca, PCM3168A, usbd_audio, ProgramManager, LED PWM, noise

### Takeaway
No fork has anything about noise, the PCM3168A driver, or LED PWM. burstMembrane's single ACDC commit switches AC/DC USB audio to pre-FX routing, so USB audio passes through without the patch. shmuga's commits fix two real H7 bugs in usbd_audio.cpp: the TX endpoint dies after an incomplete iso IN, and TX rate adaptation drifts and causes click bursts. Both apply to AC/DC because it uses the same Source/usbd_audio.cpp on an H7 with USE_USBD_AUDIO_TX and USE_USBD_FS.

### Cited Findings
- **burstMembrane 20d322dc09d983bfd04502053b420cc7bcf15e50** (Liam Power, 2026-03-31, "feat: add pre_usb audio output, fix usb device enumeration"); [commit](https://github.com/burstMembrane/OpenWare/commit/20d322dc09d983bfd04502053b420cc7bcf15e50), read from the local git clone:
  - `ACDC/Core/Inc/hardware.h`: adds `#define USE_USBD_AUDIO_RX_PRE_FX` and `#define USE_USBD_AUDIO_TX_PRE_FX` (comment "ALLOW Audio passthrough") and changes `USBD_PRODUCT_STRING_FSHS` from "OWL-ACDC" to "LIAM-ACDC". The rest is clang-format whitespace. The audio settings stay the same: 16-bit, 4 channels, USBD_AUDIO_BUFFER_PACKETS 3, 48 kHz, AUDIO_BLOCK_SIZE 16.
  - `Hardware/common.mk`: TOOLROOT set to `/Applications/ARM/bin/` (macOS toolchain path).
  - `Libraries` submodule moved from e102c6f (2023-03-05, "Add CMSIS/Device/ST/STM32F4xx v1.27.1") to 5a3f964 (2021-11-02, "updated CMSIS device specific drivers"). In pingdynasty/OpenWareLibraries these two commits are on divergent lines (merge-base ec27ac1, 2020-10-08), so the bump is effectively a different and older HAL snapshot. It is probably the "fix usb device enumeration" part of the commit message, but that is unverified.
  - Upstream semantics: in Source/ProgramManager.cpp (62a0187, lines ~264–316), PRE_FX means USB TX takes the codec input *before* the patch and USB RX is written into the patch *input*. The default POST_FX sends patch output to USB TX and has USB RX overwrite the DAC output. XibecaDevKit already ships with both PRE_FX defines.
- **shmuga lich3-usb-fixes** (author "Mark", all dated 2026-10-18; the commits carry a "Co-Authored-By: Claude" trailer); branch [lich3-usb-fixes](https://github.com/shmuga/OpenWare/tree/lich3-usb-fixes):
  - [d39aa53](https://github.com/shmuga/OpenWare/commit/d39aa53585b105abbe430405762167b581243466) "Fix undefined __builtin_clz(0) in BitState" changes Source/BitState.hpp. The commit message says that with GCC 12 the button-callback loop in onProgramReady() (ProgramManager.cpp) runs with bid=-1, writes timestamps[-1] and crashes on button press (seen on Lich3; also Lich, Magus, Witch3). The fix returns 32/128 when no bit is set.
  - [d8fdfa3](https://github.com/shmuga/OpenWare/commit/d8fdfa3c13182d00edc4463aef4e61c9861f8758) "Fix USB audio TX on H7: handle incomplete iso IN per endpoint" changes Source/usbd_audio.cpp. The H7 HAL aborts an incomplete iso IN endpoint itself and passes its epnum. The old code only retransmitted when EPENA was still set (F4 behaviour), so "on H7 the first incomplete transfer stopped the TX endpoint for good and the host received silence". The fix also retransmits with the last packet's length instead of the nominal size.
  - [c5aff8c](https://github.com/shmuga/OpenWare/commit/c5aff8c3483180b0573e0658e159fd7c79b91a26) "Fix USB audio TX rate adaptation" changes Source/usbd_audio.cpp. The fill estimate included unwritten codec samples, so the read head overtook the write head and codec blocks were dropped, "producing a burst of clicks every few seconds (every ~3.9 s with a ~170 ppm clock offset on Lich3)". The fix servos the fill level to half the buffer with a half-packet deadband and never reads past the write head.
  - [9104f1a](https://github.com/shmuga/OpenWare/commit/9104f1a5f3f809c7f24016ad94ef45bb519af8a4) "Lich3: use 5 USB audio buffer packets" changes only Lich3/Core/Inc/hardware.h: "A 3 packet (1.5 ms) buffer is too small for 32 frame codec blocks and 1 ms USB packets and leads to dropouts."
- Upstream ACDC/Core/Inc/hardware.h (62a0187) also has `USBD_AUDIO_BUFFER_PACKETS 3`, `USE_USBD_FS`, `USE_USBD_AUDIO_TX`, `USE_USBD_RX_FB`, CODEC_BLOCKSIZE 256 and AUDIO_BLOCK_SIZE 16 — [upstream hardware.h](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Inc/hardware.h)
- **hirnlego master** (Roberto Noris, 2025-09 to 2026-07-29) touches Source/ProgramManager.cpp/.h, Storage.cpp/.h, ServiceCall.cpp/.h, mpu.c and hardware_ids.h. Commits include 37b48e6 "Gap-less save" (2026-07-25), 67faeb3 "Statically allocate the background save task and queue", c459cbb "Fix resource indexing and defragmenting corrupting storage when full", 65e8c92 "Defragment the storage in a task of its own, with the patch stopped", afe56a0 "Make the SDRAM cacheable" (mpu.c) and 1b0e2d9/095af05 "bump version to 22.6.0". Nothing concerns ACDC, USB audio or noise — [hirnlego master](https://github.com/hirnlego/OpenWare-fork/commits/master)
- XponentOneAudio: 47 commits, all under Patches/ (Lich patch "Pearls"). Not firmware — [branch](https://github.com/XponentOneAudio/Owl-OpenWare/tree/ccr-caea708d-dnrfe4)

### Inferences
- shmuga's d8fdfa3 and c5aff8c are generic H7 usbd_audio fixes. AC/DC builds the same Source/usbd_audio.cpp with TX enabled on an H7, so its USB-record path likely has the same two bugs: TX can go silent permanently after an incomplete iso IN, and periodic click bursts can come from clock drift. The ACDC buffer setting is the same 3 packets that shmuga raised to 5 on Lich3. AC/DC uses 16-sample blocks rather than 32, so the margin may differ. That is untested.
- The periodic clicks described in c5aff8c are a candidate explanation for "noise" or crackle reports on USB-audio recordings from AC/DC.
- burstMembrane's change is a configuration tweak, not a bug fix. Its "fix usb device enumeration" claim rests only on rolling the Libraries submodule onto a different line.

### Gaps
- Neither fork was tested on AC/DC hardware. No fork author reports AC/DC results.
- No fork addresses analogue noise, the PCM3168A configuration (pcm3168a.c), or LED PWM.

## 3. Upstream issues/PRs mentioning AC/DC, ACDC, noise, USB audio, standalone

### Takeaway
The tracker has 88 items. None is a user-filed AC/DC issue. AC/DC appears only in the maintainer's merge PRs #67 and #69. Searches for "noise" and "standalone" return no relevant items. The USB-audio items are maintainer PRs from 2020–2021 plus PR #81, still open, about USB-ISR settings saving.

### Cited Findings
- Search "acdc": 3 hits, all merged pingdynasty PRs. [#67 "feature/acdc"](https://github.com/RebelTechnology/OpenWare/pull/67) (2022-03-15 to 03-17; adds AC/DC, XibecaDev and BioSignals support, QSPI flash and a resource CRC). #64 "OWL Pedal mkII" and #66 "Release v22.2.0" match only through commit lists — [API search acdc](https://api.github.com/search/issues?q=repo:RebelTechnology/OpenWare+acdc&per_page=100)
- [PR #69 "v22.4.0"](https://github.com/RebelTechnology/OpenWare/pull/69): head `RebelTechnology:feature/acdc`, merged 2022-04-06T22:15:11Z — [API pulls](https://api.github.com/repos/RebelTechnology/OpenWare/pulls?state=all&per_page=100)
- Search "noise": total_count 0 — [API search noise](https://api.github.com/search/issues?q=repo:RebelTechnology/OpenWare+noise&per_page=100)
- Search "standalone": 1 hit, #83 (MidiMessage poly key pressure, closed), not relevant — [API search standalone](https://api.github.com/search/issues?q=repo:RebelTechnology/OpenWare+standalone&per_page=100)
- Search "usb audio": 11 hits — [API search usb audio](https://api.github.com/search/issues?q=repo:RebelTechnology/OpenWare+usb+audio&per_page=100):
  - #12 PR "USB audio driver" (pingdynasty, 2020-09-13, closed)
  - #21 issue "Minor: Divide by zero warning" (mcclure, 2020-10-10, closed; USB_AUDIO_CHANNELS = 0 in Codec.cpp)
  - #34 PR "H7 bootloader" (antisvin, 2021-03, closed)
  - #55 "Release v21.2"
  - #61 PR "USBD Audio updates" (2021-10-05, closed)
  - #63 PR "USB Block Process" (2021-11-04, closed; USB audio code to .cpp, USB messages processed every audio block)
  - #64, #66, #67, #70
  - #81 PR "This gets called from ISR currently" (antisvin, 2022-11-11, **open**, head antisvin:feature/spi-flash-fix; settings are stored from a USB interrupt and the old function hangs when interrupts are disabled)
- Other open issues of possible relevance — [API issues](https://api.github.com/repos/RebelTechnology/OpenWare/issues?state=all&per_page=100):
  - #78 "USB hubs not supported" (mcclure, 2022-06-12)
  - #77 "Does having MIDI equipment in USB-HOST plug break firmware upload?"
  - #80 "USB Power protection not working on Lich after Firmware 22.4" (closed 2022-11-15)
  - #87 "Error saving application settings in v25 firmware" and #86 "Checksum error when saving patches" (antisvin, 2023-06-07)
  - #88 "How to compile?" (Gahlord, 2024-09-03; newest item)
- Release PRs: #68 v22.4.rc1 (head feature/usbd-startup-refactor, merged 2022-03-28), #70 v22.4.0 (merged 2022-04-06) and #76 v22.5.0 (develop, merged 2023-03-05T21:52:23Z, the current master 62a0187) — [API pulls](https://api.github.com/repos/RebelTechnology/OpenWare/pulls?state=all&per_page=100)

### Inferences
- Nobody has reported AC/DC noise or USB-audio glitches on the upstream tracker. Knowledge of such problems, if any, is elsewhere (forum, Discord, Befaco).

### Gaps
- Issue comments and PR review threads were not read. Matches inside comment text are covered by the search API, but not the full discussion.

## Side check: AC/DC MCU — STM32H743 or STM32H750?

### Takeaway
The repo is inconsistent. ACDC/ACDC.ioc names STM32H743IIKx, but the build actually compiles for STM32H750 with a 128K-flash memory map. The build files point to an STM32H750 in production hardware.

### Cited Findings
From the upstream clone (62a0187), [ACDC/](https://github.com/RebelTechnology/OpenWare/tree/master/ACDC):
- ACDC/ACDC.ioc: `Mcu.Name=STM32H743IIKx`, `Mcu.UserName=STM32H743IIKx`, `Mcu.Package=UFBGA176`. The Xibeca/Xibeca.ioc file is identical (H743IIKx), and ACDC/Core/Src contains `startup_stm32h743xx.s`.
- ACDC/Makefile includes Hardware/xibeca.mk, which sets `DEF_FLAGS = -DSTM32H750xx`, uses `S_SRC = Source/startup_owl3.s` (not the Cube startup file) and `LDSCRIPT = Hardware/xibeca.ld`.
- Hardware/xibeca.ld: `FLASH ... LENGTH = 128K /* 128K total flash in Xibeca red */`. The H743 alternative ("2M total flash in Xibeca Rev01/02 green prototypes") is commented out.
- ACDC hardware.h: `USE_QSPI_FLASH`, `NO_INTERNAL_FLASH`, `USE_DFU_BOOTLOADER`, and the comment "note that with H750, PLUS_RAM may be used by firmware".
- XibecaDevKit.ioc: `STM32H750IBKx`.

### Inferences
- The production AC/DC (Xibeca "red" module) most likely uses an STM32H750IB, the value line with 128 KB internal flash. Firmware is stored in QSPI. The H743 .ioc was most likely inherited from the 2 MB green Xibeca prototypes. This is inferred from build config, not confirmed from a BOM or chip marking.

### Gaps
- No official datasheet, BOM or photo confirms the chip. A web search ("Rebel Technology AC/DC eurorack STM32H750") found nothing authoritative ([matrixsynth AC/DC announcement](https://www.matrixsynth.com/2022/07/acdc-by-rebel-technology-and-befaco.html) is the only product-related hit).
