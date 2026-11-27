# AC/DC Noise & Firmware – Projektkontext

Werkbank für mein **Befaco / Rebel Technology AC/DC** (Eurorack-USB-Audiointerface, OpenWare-Firmware). Anlass war das Rauschen des Moduls. Ziele, in dieser Reihenfolge:

1. **Werkbank:** Gerät auslesen, automatisch aufnehmen, Spektren auswerten, Firmware reproduzierbar bauen, sicher flashen. Hier liegt der größte Nutzen (Nutzer, 2026-11-16).
2. **Störlinien verstehen und senken:** Rauschen und digitale Störlinien in den Aufnahmen. Hörbar war es immer, vor allem mit Kompressor auf der Spur.
3. **Standalone-FX und Interface:** Ohne Rechner läuft das AC/DC als FX, mit Rechner weiter als normales Audiointerface.

## Geräte

Zwei AC/DC-Module. **acdc1 = Testgerät**, **acdc2 = Referenz** (nicht flashen, nichts speichern, nichts löschen).

| Modul | Device-UUID (als Seriennummer) | Firmware | Hardware |
|---|---|---|---|
| acdc1 | `0039001c:31315101:39333437` | `v22.4.r-fx9a` (Build 11, `fd77ec3a…`), Alltags-Firmware seit 2026-11-23 | Masse-Draht Pin 15 ↔ Pin 33 seit 2026-11-24 (D90), seit 2026-11-18 im Case |
| acdc2 (DIY) | `00250049:31315102:39333437` | v22.4.q (`e81cfc3`, Hack-Branch, nie veröffentlicht), Slot 1 ACDC | unverändert, bisher kein Abbild |

- **Slots auf acdc1** (D94): 1 ACDC, 2 TapeDelay, 3 Grainz, 4 RingsReverb, 5 Plateau, 6 Tanh3, 7 SchliereS, 8 SchliereL, 9–12 leer. Gemerkt ist Slot 12, der leer ist, beim Einschalten startet deshalb Slot 1.
- **Rückwege für acdc1:** fx8a, dann fx7a, fx6a, fx5a, fx4b, fx3l, 3d, zuletzt das Readback der Werks-Firmware (`backup/acdc1/20261114/flash/acdc1_internal_flash.bin`, `433b3fd3…`). Prüfsummen in `docs/07`, „Flashen“. Die offizielle `ACDC.bin` v22.5.0 ist **kein** Rückweg, sie macht USB kaputt.
- acdc1 trug ab Werk einen Hack-Branch-Build mit dem Etikett „v22.5.0“ (D3/D3a). „Gerät 1“ in älteren Docs = acdc1, „Gerät 2“ = acdc2. M1–M3 wurden mit acdc2 aufgenommen.

## Harte Regeln

- **Jeder Flash nur nach Freigabe und nur acdc1.** Settings nie schreiben (E4). Vor jedem Eingriff in ein Gerät Settings und Slots auslesen und sichern.
- **acdc2 nicht anfassen**, bis der Nutzer es freigibt (`TODO.md`, Punkt 3).
- **Commit und Push nur mit Freigabe.** Push immer einzeln nachfragen, auch in den Submodulen. Releases nur nach Freigabe.
- **Patch nie bei offenem Stream wechseln** (D76). **Vor jedem Kabel von einem Ausgang auf einen Eingang prüfen, welcher Patch läuft** (Rückkopplung, D75).
- Firmware-Code aus fremden Repos und Forks erst lesen und diffen, nicht blind bauen oder flashen.
- Geflashte Builds, Flash-Logs und Backups nie überschreiben. `docs/uebergaben/` nie löschen und nie committen.

## Stand (2026-11-27)

Dieser Abschnitt beschreibt nur den heutigen Stand, in höchstens zehn Punkten. Ein neuer Build oder Befund **ersetzt** den alten Satz. Verlauf gehört nach `docs/chronik.md`, `docs/05` und in den Messlog, nie hierher.

- **Firmware:** fx9a = Werks-Stand v22.4.r mit Durchleitung ohne Rechner, rohen Eingängen zum Rechner (`TX_PRE_FX`), heißem Pfad im ITCM, Boot-Menü für Slot und LED-Modus, repariertem MIDI-Sendeweg, LED-PWM mit 48 kHz, I- und D-Cache. Abnahme vollständig (D88, D89). Was jeder Teil tut: `docs/01`, „Eigene Firmware auf acdc1“.
- **Masse-Draht** (D90, D91, `docs/06`): offene Eingänge RMS −5,7 dB, Kamm −7,2 dB, fs/8 −18,3 dB, am Ausgang Kamm −11 dB. **Rauschwerte vor dem 2026-11-24 gelten ohne Draht und sind mit neuen nicht direkt vergleichbar.**
- **Patches:** Slots 2–8 sind seit 2026-11-27 mit den Flags aus OwlProgram-`develop` gebaut und gespeichert (D92–D94). Die Ladeseite <https://m9dfukc.github.io/acdc-patches/> ist live.
- **Bekannter Fehler:** Ein Program Change bei offenem Stream bricht die USB-Wiedergabe bis zum nächsten Stream-Start (D76).
- **Nächster Firmware-Build:** mit Arm GNU 14.3.Rel1 (Probebuild bestanden, `docs/05`).
- **Offen:** Hörprobe mit Kompressor, Slots anhören, acdc2 sichern und umrüsten. Alles in `TODO.md`.

## Aufbau im Alltag

- Zweites Interface: **Behringer UMC202HD**, am selben Thunderbolt-Hub wie das AC/DC. Es verträgt **keine Eurorack-Pegel** an den Eingängen.
- **Signalfluss:** AC/DC-Eingänge = Aufnahmen aus dem Eurorack. AC/DC-Ausgänge = CV oder Audio zurück ins Rack. Der UMC ist nur Ausgabe an Boxen und Kopfhörer. AC/DC-Out → UMC-In gibt es nur im Messaufbau.
- **USB-Kette:** AC/DC → kleiner passiver USB-Hub → USB-Hub im Monitor → Thunderbolt-Hub. Der Mac wird über den TB-Hub versorgt.
- **Nur ein Rechner.** Tests mit Host-Wechsel fallen weg.
- Forum-Handle: `m9dfukc` (community.rebeltech.org), eigener Thread: #2244.

## Wo steht was

| Pfad | Inhalt |
|---|---|
| `TODO.md` | Was offen ist, nach Dringlichkeit. **Hier anfangen** |
| `docs/chronik.md` | Erledigtes nach Phasen, Entfallenes mit Grund, beantwortete Fragen |
| `docs/messlog.md` | **Alle eigenen Messungen** (M1 … D94) mit Index am Anfang. Jede Messung bekommt hier einen Eintrag (Setup, Datei, Befund, Fazit), danach `python3 tools/doc_check.py --messlog-index` |
| `docs/01-hardware-und-firmware.md` | Fakten zum Gerät: MCU, Codec, USB, Routing, MIDI-Header, eigene Firmware auf acdc1 |
| `docs/02-noise-befunde.md` | Rausch-Befunde: Stand heute, Hypothesen mit Messstand, Verlauf |
| `docs/03-messplan-python.md` | Messplan (abgeschlossen) und Beschreibung des Analyse-Pakets `analysis/` |
| `docs/04-software-filter.md` | Notch-Bank im Rechner. Nicht gebaut, gestrichen (2026-11-27) |
| `docs/05-firmware-plan.md` | Chronik der Firmware: Upstream, Forks, Plan und Ergebnis jedes Builds |
| `docs/06-hardware-mod-masse.md` | Masse-Draht: Wirkung, Hintergrund, Anleitung |
| `docs/07-werkzeuge-und-ablaeufe.md` | **Werkzeuge und Abläufe:** aufnehmen, auslesen, Patch aufspielen, bauen, flashen, Loop-Test, Debug-Meldungen |
| `docs/99-quellen.md`, `docs/research/` | Links, Recherchebericht, Rohnotizen (englisch). **Bei Detailfragen zuerst `docs/research/notes/` durchsuchen** |
| `docs/00-…`, `docs/uebergaben/` | Ausgangsfragen (eingefroren). Übergaben zwischen Sitzungen, nur lokal, die jüngste ist die aktuelle |
| `docs/en/` | Englische Fassungen von `01`–`07` und `99`, aus dem Deutschen erzeugt |
| `README.md`, `README.de.md` | Einstieg für Außenstehende. Bei neuen Befunden oder Werkzeugen beide nachziehen |
| `analysis/`, `tools/` | Analyse-Paket (`uv run python -m analysis <ID\|wav…>`) und Werkzeuge, beschrieben in `docs/03` und `docs/07` |
| `recordings/` | Aufnahmen (nur lokal) und `manifest.toml` mit den Metadaten jeder Messung |
| `reports/` | Je Messung Report, JSON und Plots, dazu Sitzungstabellen und Geräte-Reports |
| `firmware/` | Submodul `OpenWare`, Patches, Builds, Flash-Logs. Register in `firmware/README.md` |
| `owl/` | Submodul `m9dfukc/acdc-patches`: eigene OWL-Patches in `patches/`, gemeinsame Header in `include/`, Host-Tests in `test/`, Ladeseite in `docs/`. Nur lokal: `patches-private/` (fremde Quellen ohne Lizenz) und `vendor/` (SDK, Builds, Downloads) |
| `backup/<gerät>/<datum>/` | Geräte-Backups, nur lokal |

## Konventionen

- **Aufnahmen immer mit `tools/acdc_rec.py`**, benannt `YYYYMMDD_<geraet>_<test>_<gain>_<usb-zustand>.wav`. Das Skript legt den Manifest-Eintrag an. Einzelheiten und Testsignale: `docs/07`, „Aufnehmen“.
- **Offene Eingänge doppelt aufnehmen** (2 × 60 s), alle Regler auf 12 Uhr, Einbau notieren.
- **A/B zwischen Builds immer gegen eine Kontrolle in derselben Sitzung**, am besten am Anfang und am Ende.
- **Frequenzen immer messen** (Peak-Interpolation) statt 1000 Hz anzunehmen.
- Analyse-Skripte sind reproduzierbar: CLI mit Argumenten, keine festen Pfade, Ergebnisse als PNG und JSON oder Markdown nach `reports/`.
- Aussagen in den Docs tragen einen Marker. Beibehalten und nur mit Verweis auf den Messlog hochstufen:
  - **[belegt]**: Quelle wie Forum, Repo oder Hersteller vorhanden.
  - **[Code]**: aus dem OpenWare-Quelltext abgeleitet, nicht auf Hardware geprüft.
  - **[Hypothese]**: Schlussfolgerung, ungetestet.
  - **[gemessen]**: durch eine eigene Messung bestätigt oder widerlegt.
- **Keine fremde Software beim Namen nennen:** „Host-Software“, „Mehrkanal-Recorder“, „Aufnahmeprogramm“. Ausnahme ist, was das Projekt selbst braucht (uv, dfu-util, Arm-Toolchain, OpenOCD, FAUST, OwlProgram).
- **Sprache:** Deutsch ist die Quelle (Docs, Messlog, `TODO.md`, `CLAUDE.md`, Kommentare im Code, Reports der Analyse). Englisch sind `README.md`, `LICENSE.md`, Hilfe- und Konsolentexte der Werkzeuge und alle Kommentare in `owl/`. Im Deutschen heißt es „Oversampling“, nie „Überabtastung“.
- **Englische Fassungen (`docs/en/`):** Claude erzeugt sie aus der deutschen Quelle und stempelt sie mit `tools/i18n_check.py --stamp <datei>`. Aufgefrischt wird zu Meilensteinen und vor einem Push, wenn der Nutzer zustimmt. Marker und Glossar in `docs/en/README.md`, neue Paare in `PAIRS` im Skript.

## Kernfakten

- MCU **STM32H750IB** (128 KB internes Flash, Patches im QSPI), Codec **TI PCM3168A** an SAI1, DC-gekoppelt. SAI1 liefert die ADC-Wörter 24 Bit rechtsbündig **ohne Vorzeichen** [Code, D28].
- **USB Full Speed**, UAC 1.0, 4 in / 4 out, 16 Bit, 48 kHz, async mit Feedback-Endpoint. acdc1 läuft mit exakt 48 kHz, acdc2 mit ≈ 47 991 Hz (D10).
- **Routing auf acdc1:** Der Rechner nimmt die **rohen Eingänge** auf, der Gain-Knob wirkt darauf nicht. Ausgang ohne Stream = Patch, mit Stream = USB-Playback. Nimmt eine App vom AC/DC auf, startet macOS auch den Playback-Stream, dann ist die Durchleitung aus (D20). Audiogerät „OWL-ACDC-FX“, MIDI-Port „OWL-ACDC“.
- Eingangsbereich ≈ ±9,5 V Vollausschlag, Eingangsoffset ≈ −0,2…−0,4 V je Kanal (D29, D36).
- **Pegel:** Dateien tragen einen Faktor 2 gegen das Gerät (`scale = 2.0`, Datei-dBFS − 6,02 dB = Geräte-dBFS, D7/D8).
- **Störfamilien** in den ADC-Daten: SOF-Kamm bei k·≈1 kHz, fs/8 = 6000 Hz (Blockrate), Mischprodukte, Regler-Linien. Der Kamm hängt am USB-SOF des Host-Controllers, f0 je Anschluss messen (S2-6). Stand und Zahlen: `docs/02`, „Stand heute“.
- **Was die CPU im Blocktakt tut, erscheint bei fs/8** (D42), auch die Rechenlast eines Patches (D69).
- **Jeder Wechsel einer LED verschiebt den Nullpunkt der Eingänge** (D73, D74). Patches schalten LEDs deshalb selten, nie flackernd und nie gedimmt.

## Firmware-Arbeit

- Alle eigenen Builds: Basis `db9d3dd` (v22.4.r) + Libraries `9e8f64e`, gebaut mit `tools/build_acdc.sh` und Arm GNU 12.2.Rel1, deterministisch. Register der Patches und Builds: `firmware/README.md`. Plan und Ergebnis je Build: `docs/05`.
- **Vor jedem Flash `docs/07`, „Flashen“ lesen.** Standard ist `tools/flash_acdc.py <build> --yes` mit Start per `:leave`.
- Periodisch laufender Code gehört ins ITCM, jeder ITCM-Build vor dem Flash durch `tools/check_itcm.py`. Keine Abfrage-Schleifen im Blocktakt (D42).
- Abnahme eines Builds: Loop-Test mit `phase_slips.py` **und** `stale_samples.py`, Downloads mit `dump_stress.py`, Rauschen gegen den Vorgänger mit Kontrolle. Abläufe in `docs/07`.
- **Fork:** https://github.com/m9dfukc/OpenWare. `acdc/fx1d` (Spitze `54228769`, bytegleich mit fx9a) und `acdc/thru-usb-feedback` (Spitze `edb32852`, Build 1d). Releases heißen `acdc-<version>`, „Latest“ ist `acdc-v22.4.r-fx9a`. `gh` immer mit `--repo m9dfukc/OpenWare` aufrufen, sonst zielt es auf das Upstream-Repo.

## Git und Submodule

- Öffentliches Repo https://github.com/m9dfukc/acdc-workbench (Remote `origin`, Branch `main`).
- **Nur lokal (`.gitignore`):** WAVs, Plots und JSON in `reports/`, Binaries und Readbacks, `backup/`, `docs/uebergaben/`, `firmware/_work/`, `firmware/downloads/`, `firmware/releases/`, im Submodul `owl/patches-private/` und `owl/vendor/`. Aus `reports/` sind nur `*_report.md` und `*-session-table.md` im Repo.
- **Vor jedem Commit:** `git status --short` darf keine Binaries, WAVs oder Dateien aus `backup/` zeigen. Nichts Privates über Geräte-UUIDs, Heimpfad und Vorname hinaus. **Vor jedem Push:** `python3 tools/doc_check.py`.
- Plots für Docs und README liegen als Kopie in `docs/img/`. Nie auf Plots in `reports/` verlinken, sie fehlen im Repo.
- **`firmware/OpenWare`** (Submodul, Branch `acdc/fx1d`): Die Remotes heißen `fork` und `upstream`, ein `origin` gibt es nicht. Wer dort umschaltet oder committet, muss danach im Hauptrepo `firmware/OpenWare` neu committen. Andere Stände per `git show <commit>:<pfad>` lesen.
- **`owl`** (Submodul `m9dfukc/acdc-patches`, Branch `main`, Push per SSH): Änderungen dort committen und pushen, danach im Hauptrepo `owl` neu committen.

## Umgebung

- In der Sandbox ist `~/.cache/uv` nicht schreibbar: `UV_CACHE_DIR=.uv-cache uv run …`.
- Aufnahme (CoreAudio), MIDI (CoreMIDI), DFU (USB) und `gh` laufen nur außerhalb der Sandbox. Die MIDI-Werkzeuge brauchen Python 3.12 mit `mido` und `python-rtmidi`, Aufruf in `docs/07`, „Umgebung“.
- `git clone` scheitert in der Sandbox. Fremde Quellen als Tarball von `codeload.github.com` holen.

## Skills (projektlokal, `.claude/skills/`)

Aus `mattpocock/skills` @ `5863806`: `/grill-me` (Plan oder Entscheidung in Fragerunden prüfen, z. B. vor Firmware-Schritten oder Messreihen), `/handoff` (Übergabe nach `docs/uebergaben/`), `research` (Recherche gegen Primärquellen, Ablage in `docs/research/notes/`).
