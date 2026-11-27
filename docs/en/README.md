# English versions of the reference documents

The working language of this project is German, and the German files are the source. This folder holds English translations of the reference documents. They are generated from the German originals and refreshed at milestones, so a translation can be older than its source. Each file states its source and date at the top.

| English | German source | Content |
|---|---|---|
| [01-hardware-and-firmware.md](01-hardware-and-firmware.md) | `docs/01-hardware-und-firmware.md` | Facts about the module: MCU, codec, USB, audio routing in the code, the MIDI header on the back |
| [02-noise-findings.md](02-noise-findings.md) | `docs/02-noise-befunde.md` | Noise findings: status today, what the forum knows, hypotheses on the cause with their measurement status |
| [03-measurement-plan-python.md](03-measurement-plan-python.md) | `docs/03-messplan-python.md` | Measurement plan (finished) and description of the Python analysis |
| [04-software-filter.md](04-software-filter.md) | `docs/04-software-filter.md` | Notch bank in the computer: filter shape, Python prototype, plugin, FAUST patch. Not built, dropped |
| [05-firmware-plan.md](05-firmware-plan.md) | `docs/05-firmware-plan.md` | Chronicle of the firmware: state of OpenWare, forks, plan and result of every build |
| [06-hardware-mod-ground.md](06-hardware-mod-ground.md) | `docs/06-hardware-mod-masse.md` | Hardware mod: ground wire pin 15 ↔ pin 33 on the processor module, effect, background, step-by-step guide |
| [07-tools-and-procedures.md](07-tools-and-procedures.md) | `docs/07-werkzeuge-und-ablaeufe.md` | Tools and procedures: recording, reading out, uploading a patch, building, flashing, loop test, debug messages |
| [99-sources.md](99-sources.md) | `docs/99-quellen.md` | All links |

Check which translations are out of date:

```sh
python tools/i18n_check.py
```

## Not translated

- `docs/messlog.md`, the lab notebook with every measurement (entries M1 to D94, with an index at the top). The translated documents refer to its entries by ID.
- `docs/chronik.md`, the chronicle: what is done, dropped or answered.
- `docs/00-ausgangsfragen-und-verlauf.md`, the original questions and the course of the research.
- `TODO.md` and `CLAUDE.md` in the project root.

The research notes in `docs/research/notes/` were written in English from the start.

## Evidence markers

Statements in the documents carry a marker that says how well they are supported:

| Marker | German | Meaning |
|---|---|---|
| **[sourced]** | [belegt] | A source exists: forum, repository or manufacturer |
| **[code]** | [Code] | Derived from the OpenWare source, not checked on hardware |
| **[hypothesis]** | [Hypothese] | A conclusion, untested |
| **[measured]** | [gemessen] | Confirmed or refuted by an own measurement, with a reference to the lab notebook |

## Terms

| English | German | Meaning here |
|---|---|---|
| comb | Kamm | Lines at multiples of ≈1 kHz that follow the USB start-of-frame |
| mixing products | Mischprodukte | Lines at n · f_comb + m · 6000 Hz |
| residual | Rest | Noise that remains when all line families are removed |
| hot path | heißer Pfad | Code that runs periodically: audio interrupts, audio task, USB, main loop |
| padding build | Füll-Build | A build that only adds unused bytes to shift code in flash |
| pass-through | Durchleitung | The patch output reaches the jacks without a computer |
| fallback | Rückweg | The firmware to flash back if a build fails |
