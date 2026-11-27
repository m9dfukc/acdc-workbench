# 07 – Werkzeuge und Abläufe

Was die Werkbank an Werkzeugen hat und wie die wiederkehrenden Abläufe gehen: aufnehmen, Gerät auslesen, Patch aufspielen, Firmware bauen und flashen, USB-Stabilität prüfen. Alle Argumente eines Werkzeugs zeigt `--help`. Das Analyse-Paket `analysis/` ist in `03-messplan-python.md` beschrieben, Plan und Ergebnis jedes Firmware-Builds in `05-firmware-plan.md`.

Die Geräte-Werkzeuge sind an das Testmodul des Autors gebunden (acdc1, über MIDI-Geräte-ID und DFU-Seriennummer). Gemessen und geflasht wurde nur dort.

## Umgebung

- Python läuft über **uv** (`uv run`, `uv add`). Voraussetzungen sonst: macOS, `dfu-util`, Arm GNU Toolchain 12.2.Rel1 unter `/Applications/ArmGNUToolchain/12.2.rel1/`.
- **MIDI-Werkzeuge** (`owl_read.py`, `owl_write.py`, `dump_stress.py`, `knob_series.py`) brauchen Python 3.12 und zwei Pakete, die nicht in `pyproject.toml` stehen:

  ```sh
  uv run --no-project --python 3.12 --with mido --with python-rtmidi python tools/owl_read.py
  ```

- OWL-Webseiten vorher schließen, sie pollen das Gerät.
- In der Sandbox von Claude Code laufen Aufnahme (CoreAudio), MIDI (CoreMIDI) und DFU (USB) nicht, diese Aufrufe brauchen die Ausnahme. uv braucht dort `UV_CACHE_DIR=.uv-cache`.

## Werkzeuge in `tools/`

| Werkzeug | Zweck |
|---|---|
| `acdc_rec.py` | Aufnahmen und Testsignale, Standard seit 2026-11-16. Auch für andere Geräte (`--device UMC202HD --input-only --channels 2`). `--prompt --progress 1` im Terminal gibt Start per Enter und eine Zeitanzeige im Sekundentakt |
| `owl_read.py` | Gerät per MIDI/SysEx auslesen (nur lesend), Neustart in den DFU-Modus |
| `owl_write.py` | Patch hochladen: `--run` (nur RAM) oder `--store N --yes` (Slot im Patch-Flash). Nur acdc1, sichert einen belegten Slot vorher, liest danach zurück. `--erase N --yes` löscht einen Slot ab 2, nur mit passender lokaler Kopie als PATCH (am Gerät erprobt 2026-11-27 mit Slot 9, übrige Slots unverändert). `--info` und `--syx-out` laufen offline |
| `build_owl_patch.sh` | C++-Patch mit OwlProgram bauen, SysEx nach `owl/vendor/builds/` |
| `sim_boot_menu.sh` | Host-Test der Boot-Menü-Logik (Patch 15/15b, ab Build 8 auch Regler 2 für den LED-Modus) mit simulierten Reglern, dazu ab Build 8 die LED-Schleife je Modus (`firmware/sim/led_loop_sim.cpp`) |
| `test_owl_dsp.sh` | Host-Test der eigenen Patch-Quellen in `owl/` (Tanh3, Limiter, Schliere, Blockraten-Sperre, beide LED-Mess-Patches). Ruft `owl/test/run.sh` im Submodul auf |
| `dfu_readback.sh`, `compare_firmware.py` | Internes Flash lesen und mit einer Referenz vergleichen |
| `dump_stress.py` | Download-Stresstest für den MIDI-Sendeweg: lädt bei laufendem Patch alle Slots in Runden herunter und zählt beschädigte Downloads. Nur acdc1, nur lesend bis auf einen Program Change. Bricht ab, wenn das Gerät nicht mehr antwortet (D62) |
| `flash_acdc.py` | Build auf acdc1 flashen: Offline-Prüfung, Auslesen, DFU-Neustart, Schreiben, Readback-Vergleich, Flash-Log, Start per `:leave` und A1. Siehe „Flashen“ |
| `build_acdc.sh` | Reproduzierbarer Firmware-Build aus Commit, Libraries-Tarball und Patches |
| `setup_repo.sh` | Frischen Klon einrichten: Submodule, `upstream`-Remote, Libraries-Tarball und offizielle `ACDC.bin` mit SHA-Prüfung |
| `check_itcm.py` | ITCM-Build am ELF prüfen (`--groups` für Varianten, `--same-itcm` für Füllvarianten) |
| `phase_slips.py`, `stale_samples.py` | Loop-Aufnahmen auf Sample-Slips und einzelne veraltete Samples prüfen |
| `family_table.py` | Familienpegel mehrerer Messungen, Δ gegen die Kontrolle. `--dc-ref/--dc-correct` korrigiert Aufnahmen hinter dem VCA des Default-Patches über den DC-Offset (D26, D86) |
| `crosstalk_lines.py`, `click_sensitivity.py` | Übersprechen der Ausgänge, Empfindlichkeit des Klick-Detektors |
| `line_levels.py` | Pegel einzelner Linien je Kanal direkt bei der Linienfrequenz, für mehrere Aufnahmen, mit Abstand zum Grundrauschen. Trifft die Handwerte aus D58 auf 0,1 dB |
| `ledpath_phases.py` | Pegel je Phase einer Aufnahme mit dem Mess-Patch `SchliereLedPath` an einem Interface-Eingang (z. B. UMC), über den Eichton auf den Ausgang von acdc1 umgerechnet: RMS, 40 Hz (LED-Blinken), Kamm, 6 und 12 kHz (D74, D91) |
| `ab_bands.py` | A/B/A-Vergleich dreier Aufnahmen (z. B. alter Build → neuer → alter): RMS, Pegel je Terzband gegen die Streuung der A-Läufe, neue Linien, Knackser, Tabelle als Markdown (D93) |
| `knob_series.py` | Geführte Aufnahmeserie mit Reglern in vorgegebenen Stellungen: liest CC 20–23, wartet auf die Stellung, nimmt mit `acdc_rec.py` auf, am Ende Tabelle `reports/<serie>-session-table.md`. `--simulate` läuft ohne Gerät |
| `i18n_check.py` | Listet veraltete englische Fassungen in `docs/en/` auf (Prüfsumme der deutschen Quelle im Kopf). `--stamp` schreibt den Kopf nach einer neuen Übersetzung |
| `doc_check.py` | Prüft die Doku vor einem Push: Länge von `CLAUDE.md`, tote Links, tote Pfade in den aktuellen Docs, veraltete Übersetzungen, Index des Messlogs (`--messlog-index` schreibt ihn neu) |

## Aufnehmen

**Aufnahmen immer mit `tools/acdc_rec.py`** (Entscheidung vom 2026-11-16). Die frühen Messungen liefen über eine Host-Software mit Mehrkanal-Recorder, die Gegenprobe beider Wege ist bestanden (D35). Eine Host-Software braucht es nur noch, wenn ein Patch im Rechner nötig ist.

- Das Skript öffnet das Gerät duplex mit Nullen am Ausgang, 48 kHz, Block 256 (wie die frühere Host-Software). Es schreibt eine 4-Kanal-WAV mit 16 Bit nach Namenskonvention und legt den Eintrag in `recordings/manifest.toml` an.
- Namenskonvention: `YYYYMMDD_<geraet>_<test>_<gain>_<usb-zustand>.wav`, z. B. `20261113_acdc1_open-inputs_g12_usb-stream.wav`.
- Optional: `--reps` mit Neuöffnen dazwischen, `--owl-read` vor dem Schließen, `--analyze --ref …`. Länge, Gerät, Kanäle und Format sind Argumente.
- Geräteliste: `UV_CACHE_DIR=.uv-cache uv run python tools/acdc_rec.py --list`.

**Testsignale:**

- `--sine F1 F2 F3 F4` schickt je Ausgang einen echten Sinus (0 = still). Pegel mit `--sine-level` in Geräte-dBFS (Standard −6 ≙ 5 V Spitze am Ausgang), `--sine-fade` blendet ein.
- `--dc V1 … V4` gibt einen Gleichanteil in Vollausschlag aus (−1…1, 1 ≈ 10 V am Ausgang), `--dc-ramp SEK` fährt langsam hoch.
- `--simulate` mit `--sine` ist ein Loopback ohne Gerät.

**Regeln für Rauschmessungen:**

- Offene Eingänge doppelt aufnehmen (2 × 60 s). Der Kamm streut zwischen Läufen um ≈ 0,4 dB (D35), einzelne Ausreißer gab es auch (D22/D23).
- A/B zwischen Builds immer gegen eine Kontrolle in derselben Sitzung, am besten am Anfang und am Ende. Die Pegel driften in einer Sitzung um 0,4 bis 2 dB (D44, D77).
- Alle vier Regler auf 12 Uhr. Ungleich gestellte Regler heben eigene Linien (D61).
- Den Einbau notieren (im Case oder daneben) und ob der Masse-Draht auf dem Modul sitzt. Werte vor dem 2026-11-24 gelten ohne Draht (D90).
- Jede Messung bekommt einen Eintrag in `messlog.md`: Setup, Datei, Befund, Fazit.

**Pegel der frühen Aufnahmen (D7/D8):** Aufnahmen über die frühere Host-Software tragen einen Faktor 2 (+6 dB) zwischen Gerät und Datei. Datei-dBFS − 6,02 dB = Geräte-dBFS. `acdc_rec.py` bildet das mit `scale = 2.0` im Manifest nach, damit alte und neue Dateien vergleichbar bleiben.

## Gerät auslesen, Patch wählen und aufspielen

- **Auslesen:** `owl_read.py` zeigt Version, Settings, Slots und die letzte Debug-Meldung. `--dump --out <ordner>` sichert alle Slots. Bei einem Dump auf `ok` im Report achten.
- **Regler lesen:** Der Settings-Request liefert CC 20–23 (Regler 1–4, 7 Bit) im Report unter `settings_cc`.
- **Patch wechseln vom Rechner:** `owl_read.py --program N`. Das wird nicht gemerkt. **Nur ohne offenen Stream**: Ein Program Change bei offenem Stream bricht die USB-Wiedergabe bis zum nächsten Stream-Start (D76).
- **Patch aufspielen:** erst `owl_write.py <datei> --run` (nur RAM), dann `--store N --yes`.
  - Ist der Slot belegt, die Sicherung mit `--backup-file <lokale Kopie>` angeben. Größe und CRC müssen zum Slot passen.
  - Slot 1 braucht zusätzlich `--allow-slot1`.
  - Nach einem Store läuft der gespeicherte Slot, `--program-after 1` schaltet zurück.
- **Slot-Downloads bei laufendem Patch** waren bis fx4b unzuverlässig (Wettlauf im MIDI-Sendeweg der Original-Firmware, D53, D54, D62). fx5a behebt das: 240 von 240 Downloads in Ordnung (D63). Test: `dump_stress.py`.
- **Ladeseite im Browser** für andere AC/DC-Besitzer: <https://m9dfukc.github.io/acdc-patches/> (Quelle `owl/docs/`, Web MIDI mit SysEx, Chromium). Sie startet, speichert oder löscht eine lokale `.bin` oder `.syx` in den Slots 1–39 und lädt einen Slot herunter. Slot 40 und höher lehnt sie ab, weil die Firmware den Slot als `uint8_t` nimmt: 40 träfe beim Löschen Ressource 0, 255 löscht den ganzen Speicher [Code].

**Boot-Menü am Gerät** (ab fx4b, LED-Modus ab fx6a):

- Einschalten mit Regler 1, 2, 3 links und Regler 4 rechts öffnet das Menü. Regler 1 wählt unter den belegten Slots (zählt erst nach Bewegung), Regler 4 weg vom Anschlag bestätigt, Regler 3 weg vom Anschlag oder 30 s brechen ab.
- Regler 2 wählt den LED-Modus: normal (linkes Drittel), nur Clip (Mitte), aus (rechts).
- Die Eingangs-LEDs zeigen den Slot binär (1–15, LED 1 = 1 … LED 4 = 8).
- Slot und LED-Modus werden als Ressourcen `ACDC.slot` und `ACDC.led` im Patch-Flash gemerkt, die Settings bleiben unberührt. Ohne das Regler-Muster startet der gemerkte Slot, seine Nummer steht 1 s auf den LEDs. Ist der gemerkte Slot leer, startet Slot 1 [Code].
- Regler-Endwerte: links 2, rechts 127 von 127 (D51).

## OWL-Patches bauen

- `tools/build_owl_patch.sh` baut einen C++-Patch mit OwlProgram und schreibt `patch.bin`, `<name>.syx` und `BUILD_INFO.txt` nach `owl/vendor/builds/<name>/`. Standardwerte: Quellen `SRC` = `owl/patches-private/`, SDK = `owl/vendor/OwlProgram/`, Arbeitsbäume in `owl/vendor/_work/`.
- **SDK:** OwlProgram `60f44ab` mit DaisySP `4263388`. In `compile.mk` steht lokal die Flag-Zeile aus OwlProgram-`develop` (ohne `-fno-builtin`, `-ffreestanding`, `-mtune`), das Original liegt daneben als `compile.mk.orig-60f44ab`. Die Flags senken die Rechenlast der Patches um 5–21 % (D92), am Ausgang ist kein Unterschied messbar (D93). Das Skript warnt bei `-fno-builtin` und schreibt `sdk_flags` in `BUILD_INFO.txt`.
- **Schalter:** `LINK=plusram` legt den Patch ins AXI-SRAM statt ins DTCM (Standard `patchram`, so ist Plateau gebaut), `LIMIT=1` hüllt einen FX-Patch in den Ausgangs-Limiter (`owl/include/AcdcOutput.h`).
- **Host-Tests:** `tools/test_owl_dsp.sh`. Der Vergleich von Plateau mit dem Original-Code läuft nur mit `VALLEY_SRC=$PWD/owl/vendor/downloads/vrf245/ValleyRackFree-2.4.5/src owl/test/run.sh`.
- Fremde Quellen kommen als Tarball von `codeload.github.com` nach `owl/vendor/downloads/`. Die Builds vor dem Flag-Wechsel liegen in `owl/vendor/builds-archive/`.
- Quellen unveröffentlichter Library-Patches findet die API: `https://www.rebeltech.org/api/patch/?seoName=<name>` (Metadaten mit Quell-URL), `/api/patches/` (Liste). Ablage in `owl/patches-private/library/`.

## Firmware bauen

- Alle eigenen Builds: Basis `db9d3dd` (v22.4.r, Branch `hack/acdc-output-levels`), Libraries `9e8f64e` (altes H7-HAL), gebaut mit `tools/build_acdc.sh` und Arm GNU 12.2.Rel1, deterministisch. Der Aufruf für die aktuelle Firmware steht im englischen `README.md`, „Getting started“.
- `build_acdc.sh` hängt nicht am ausgecheckten Stand von `firmware/OpenWare`, es holt den Commit per `git archive`.
- Patches, Builds und ihre Ergebnisse: `firmware/README.md`.

**Regeln für neue Firmware:**

- Periodisch laufender Code gehört ins ITCM (Linker-Patch 11g). Jeder ITCM-Build geht vor dem Flash durch `tools/check_itcm.py`.
- Ohne ITCM gilt die alte Regel: neuen Code ans Ende legen (`.late_text`/`.late_bss`) oder die Adressen per `nm` gegen den Referenz-Build prüfen. Die Lage des Codes im Flash verschiebt die Störlinien (D33).
- Keine Abfrage-Schleifen im Blocktakt (D42).
- Die Loop-Prüfung läuft immer mit `phase_slips.py` **und** `stale_samples.py` auf derselben WAV.
- Ein neuer Alltags-Build bekommt ein eigenes Release am Fork, nur nach Freigabe.

## Flashen

Ohne Pads, DFU über die vordere USB-B-Buchse. Jeder Flash nur nach Freigabe, nur acdc1, Settings nie schreiben. Vor jedem Eingriff Settings und Slots auslesen und sichern.

**Von Hand:**

1. `owl_read.py --out <flashlog>/owl_read_before`
2. `owl_read.py --reset-to-dfu --yes`
3. `dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000 -D <bin>`
4. Readback mit `-s 0x08000000:131072 -U`, mit dem Binary vergleichen und auf 0xFF prüfen
5. Start der Firmware: ein zweites, nur lesendes Readback mit `-s 0x08000000:131072:leave -U` (Standard seit 2026-11-19, D79). Der ROM-DFU startet danach die Firmware, `dfu-util` endet dabei mit „Error during download get_status“, das ist normal. Kein Kaltstart, der Codec bleibt unter Strom
6. A1 per `owl_read.py`: Version, `SR/BS/CH 48000 8 4`, Slots unverändert

**Kaltstart** (Case aus, USB ab, Case an, USB an; nur Case aus reicht nicht, USB versorgt das Board) nur in diesen Fällen: `:leave` scheitert, ein Build ändert etwas am Einschalten (Takt, Codec-Init), der Test betrifft das Einschalten (Boot-Menü, gemerkter Slot oder LED-Modus nach Aus und Ein) oder es geht nach einem Problem auf den Rückweg.

Je Flash entsteht ein Ordner in `firmware/flashlog/`.

**Als Skript: `tools/flash_acdc.py`** (außerhalb der Sandbox). Es führt die Schritte 1–6 aus, mit `--cold` nur 1–4 und Schritt 6 nach dem Neustart von Hand.

- `python3 tools/flash_acdc.py <build>`: nur die Offline-Prüfung (Größe, Vektortabelle, Version, SHA gegen `BUILD_INFO.txt`, `check_itcm.json`). `<build>` ist eine `.bin`, ein Build-Ordner oder ein Ordnername in `firmware/builds/`.
- `… <build> --yes [--name <log>]`: flasht acdc1. Geprüft werden die MIDI-Geräte-ID und die DFU-Seriennummer. Der Log-Ordner heißt `firmware/flashlog/<datum>_<name>` (Standard: Build-Ordner ohne `acdc1-`), ein vorhandener wird nie benutzt (dann z. B. `--name …-zurueck`).
- Nach dem Readback: `:leave`, warten, bis das DFU-Gerät verschwindet (`--leave-wait`, 10 s), dann A1 mit bis zu drei Versuchen. Exit 6: `:leave` hat nicht gewirkt oder acdc1 meldet sich nicht über MIDI, dann Neustart von Hand und `--a1`. Exit 7: A1 bestanden, aber das zweite Readback weicht ab.
- `--cold`: kein `:leave`, nach dem Readback auf den Neustart von Hand warten.
- `… --a1 <log-ordner>`: nach einem Neustart von Hand. Prüft Gerät, Version, 48000 Hz, Blockgröße 8 und die Slots gegen den Stand vor dem Flash. Die Kanalzahl prüft es nicht.
- `--from-dfu`: acdc1 steht schon im DFU-Modus, z. B. nach einem fehlgeschlagenen Flash. Dann nicht neu starten, sondern damit den Rückweg flashen.
- Bricht es ab, bevor etwas geschrieben wurde, benennt es den Log-Ordner in `…-abgebrochen-<zeit>` um.

**Erprobt:** drei Flashes mit Readback und `--a1` (D63/D64), `:leave` von Hand (D79) und aus dem Skript (D84, D88). `--from-dfu`, der Abbruchweg und die Fehlerwege (bleibt im DFU, kein MIDI, abweichendes Readback) liefen nur gegen Attrappen.

**Rückwege für acdc1**, je mit `flash_acdc.py <build>`: von fx9a aus fx8a (`e1b1097b…`), dann fx7a (`cac6fee0…`), fx6a (`6a3fc427…`), fx5a (`b69c25b3…`), fx4b (`a21f35c9…`), fx3l (`b55b94d8…`), 3d (`d212cf8d…`), Build 2, 1d. Der letzte Rückweg ist das Readback der Werks-Firmware in `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (`433b3fd3…`). Die offizielle `ACDC.bin` v22.5.0 ist **kein** Rückweg: Laut Forum macht sie USB kaputt (Thread 2083 #4).

Flashen über ST-Link und die Boot-Pads: `05-firmware-plan.md`, „Flashen – allgemeine Hinweise“.

## USB-Stabilität prüfen (Loop-Test)

- Patchkabel Out n → In n, Gain 12 Uhr, `tools/acdc_rec.py --sine 440 530 670 790 --owl-read`, 60 s.
- Danach `tools/phase_slips.py --freqs 440 530 670 790` und `tools/stale_samples.py` auf derselben WAV.
- **Vor jedem Kabel von einem Ausgang auf einen Eingang prüfen, welcher Patch läuft.** Ein FX-Patch, der diesen Eingang auf diesen Ausgang gibt (Schliere, Mess-Patches mit Verstärkung), bildet damit eine Rückkopplungsschleife. Erst auf Slot 1 schalten oder den Stream öffnen, dann stecken (D75).
- **Den Patch vor dem Öffnen des Streams wählen**, nie währenddessen (D76).
- Die Geräte-Meldung lesen, **bevor** der Stream schließt (`--owl-read` tut das).
- Über den Loop lässt sich ein Eingang nur mit negativer Spannung übersteuern (`--dc … -1`), wegen des negativen Eingangsoffsets (D36, D75).

**Debug-Meldungen** (PROGRAM_MESSAGE, nur die letzte bleibt):

| Meldung | Bedeutung |
|---|---|
| `rx unf 0.9513 0.4722 4.0000` | Unterlauf mitten im Lauf |
| `rx unf 1.0000 … 32` | Puffer leer, typisch am Stream-Ende |
| `tx ovf 1.0000 1.0000 32` | typisch am Stream-Start |
| `fb <alt> <neu>` | Feedback-Messung verworfen, z. B. ≈ 32 ms ohne SOF (D18) |
| `fb clamp` | Regler an der Grenze, bei laufendem Stream ein Fehlerzeichen (D38). Tritt nach einem Program Change bei offenem Stream auf (D76) |
| `midi tx ovf` (ab fx5a) | MIDI-Sendepuffer voll, eine Nachricht wurde verworfen |
| `Sending 100` | Fortschrittsanzeige nach einem Slot-Download, kein Fehler |

## Doku prüfen

- `python3 tools/doc_check.py` vor jedem Push: meldet eine `CLAUDE.md` über 200 Zeilen, tote Links, tote Pfade in den aktuellen Docs, veraltete englische Fassungen und einen veralteten Index im Messlog.
- Nach einem neuen Eintrag im Messlog schreibt `python3 tools/doc_check.py --messlog-index` den Index am Anfang von `messlog.md` neu.
- `python3 tools/i18n_check.py` allein listet die veralteten Fassungen in `docs/en/`. Nach einer neuen Übersetzung `--stamp <datei>`.
