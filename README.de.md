# acdc-workbench

Eine Werkbank für das **Befaco / Rebel Technology AC/DC**, das Eurorack-USB-Audiointerface mit OpenWare-Firmware. Sie liest das Modul aus, nimmt automatisch auf, wertet das Rauschspektrum aus, baut die Firmware reproduzierbar und protokolliert jeden Flash.

Anlass war das Rauschen in meinen AC/DC-Aufnahmen. Die Werkzeuge, die dabei entstanden sind, sind inzwischen das wichtigste Ergebnis. Die Firmware selbst liegt in einem Fork: [m9dfukc/OpenWare](https://github.com/m9dfukc/OpenWare), Branch `acdc/fx1d`, hier als Submodul eingebunden.

> **Inoffiziell und eng gefasst.** Gemessen wurde an einem Modul, mit einem Rechner, unter macOS. Ein zweites Modul dient als unberührte Referenz. Flashen geschieht auf eigene Gefahr: vorher die Firmware des eigenen Moduls sichern.

English version: [README.md](README.md)

## Was die Werkbank kann

| Werkzeug | Zweck |
|---|---|
| `tools/acdc_rec.py` | Nimmt mit festem Aufbau auf (4 Kanäle, 48 kHz), gibt Testsignale aus (Sinus, Gleichanteil, Rampen), benennt die Datei und legt den Eintrag in `recordings/manifest.toml` an |
| `python -m analysis` | Rauschanalyse einer Aufnahme: Langzeit-Spektrum, gemessene Linienfrequenzen, Linienfamilien (USB-Frame-Kamm, fs/8, Mischprodukte, LED-PWM, Netz), Zeitverlauf, Report als Markdown, JSON und Plots |
| `tools/family_table.py` | Tabelle der Familienpegel über mehrere Messungen, mit Differenz zur Kontrolle |
| `tools/owl_read.py` | Liest das Modul per MIDI/SysEx aus, ohne zu schreiben: Firmware-Version, Settings, Patch-Slots, Statusmeldung. Kann es in den DFU-Bootloader neu starten |
| `tools/owl_write.py` | Lädt einen OWL-Patch per MIDI/SysEx hoch: nur im RAM starten oder in einen Slot speichern. Sichert einen belegten Slot vorher und liest den neuen danach zurück |
| `tools/build_owl_patch.sh` | Baut einen C++-Patch mit OwlProgram für das AC/DC und schreibt die SysEx-Datei für `owl_write.py` |
| `tools/sim_boot_menu.sh` | Testet die Logik des Boot-Menüs (Patch 15) am Rechner mit simulierten Reglern |
| `tools/dfu_readback.sh`, `tools/compare_firmware.py` | Internes Flash über DFU lesen und mit einer Referenz vergleichen |
| `tools/dump_stress.py` | Stresstest für den MIDI-Sendeweg: lädt bei laufendem Patch alle Slots immer wieder herunter und zählt beschädigte Downloads |
| `tools/flash_acdc.py` | Flasht einen Build über DFU und führt ein Flash-Log: prüft das Binary offline, liest das Modul aus, startet es in den DFU-Modus, schreibt, liest zurück und vergleicht, startet danach die Firmware mit einem nur lesenden `dfu-util … :leave` und prüft das Modul (A1). `--cold` wartet stattdessen auf einen Neustart von Hand, `--a1` prüft danach. Über die Geräte-ID an das Testmodul des Autors gebunden |
| `tools/build_acdc.sh` | Reproduzierbarer Firmware-Build aus Commit, festem Libraries-Tarball und Patch-Liste. Schreibt `BUILD_INFO.txt` mit allen Prüfsummen |
| `tools/check_itcm.py` | Prüft einen ITCM-Build am ELF vor dem Flash: was liegt wo, welche Aufrufe verlassen das ITCM, Vergleich mit einem Referenz-Build |
| `tools/phase_slips.py`, `tools/stale_samples.py` | Prüfen eine Loop-Aufnahme (Out → In) auf verlorene oder doppelte Samples und auf einzelne veraltete Samples |
| `tools/line_levels.py` | Pegel einzelner Linien je Kanal, direkt bei der Linienfrequenz gemessen, über mehrere Aufnahmen, mit Abstand zum Grundrauschen |
| `tools/knob_series.py` | Geführte Aufnahmeserie mit den Reglern in vorgegebenen Stellungen: liest die Regler per MIDI, wartet auf die Stellung, nimmt auf und schreibt am Ende eine Tabelle der Linienpegel |

## Befunde bisher

- **Vier Familien von Störlinien** stecken in den ADC-Daten, auf allen Kanälen stark korreliert:
  - ein Kamm bei k · ≈1 kHz
  - eine Linie bei fs/8 = 6000 Hz, der Audio-Blockrate bei Blockgröße 8
  - Mischprodukte der beiden
  - eine LED-PWM-Linie bei 2321 Hz
- **Der Kamm folgt dem USB-Start-of-Frame des Host-Controllers.** Seine Grundfrequenz hängt vom USB-Anschluss ab (999,87 bis 1000,00 Hz im Takt des Moduls). An den Ausgängen verschwindet er ohne USB.
- **Die Lage des Codes im Flash verschiebt die Linien.** Ein Build, der nur Füllbytes ergänzt und an der Funktion nichts ändert, hat die Familien um 1,5 bis 4,5 dB verschoben.
- **Periodisch laufender Code im ITCM hilft.** Mit dem heißen Pfad im ITCM sinkt die fs/8-Linie um rund 5 dB, die Mischprodukte verschwinden, und das Ergebnis hängt nicht mehr von der Flash-Lage ab.
- **Kleine Linien aus den Takten der MCU.** Der frei laufende Regler-ADC scannt mit 105,634 kHz und erscheint gefaltet bei 9633,8 Hz, etwa −118 dBFS. Eine weitere Gruppe von Linien (2200,95 Hz und Harmonische) steigt, wenn die vier Regler verschieden stehen: Ein Regler am Anschlag bringt sie auf etwa −100 dBFS, abwechselnde Anschläge auf −94 dBFS, immer noch 19 dB unter dem Kamm. Stehen alle vier Regler gleich, egal wo, bleibt sie bei etwa −116 dBFS. Woher ihre Frequenz kommt, ist offen.
- **Der LED-Strom verschiebt den Nullpunkt aller Eingänge.** Jede leuchtende Eingangs-LED verschiebt die rohen ADC-Daten aller Kanäle um etwa −2,9 mV (−71 dBFS). Eine dauerhaft leuchtende LED ist still, jeder Wechsel ist ein Knack, und eine gedimmte LED wiederholt den Sprung 2321-mal pro Sekunde: Das ist die LED-PWM-Linie. Ein Patch, der seinen Eingang durchreicht, bringt all das an die Ausgänge. Build 9 (`v22.4.r-fx7a`) lässt die LED-PWM mit 48 kHz im Takt der Abtastung laufen: Die Linie bei 2321 Hz ist an Ein- und Ausgängen weg, die langsame Verschiebung bleibt.
- **Drei Timing-Fehler im ursprünglichen USB-Audio-Code** wurden dabei gefunden und behoben: ein Feedback in offener Schleife, ein Wettlauf zwischen RX- und TX-DMA und ein Start-of-Frame-Handler, der zweimal je Frame lief.

Firmware `v22.4.r-fx3l` gegen den Vorgänger `v22.4.r-fx2d`, offene Eingänge, Gain auf 12 Uhr, je 2 × 60 s, Pegel in dBFS des USB-Stroms:

| Größe | `fx2d` | `fx3l` | Differenz |
|---|---|---|---|
| RMS ≥ 20 Hz | −77,6 | −78,7 | −1,1 dB |
| Breitbandrauschen ohne Linien | −83,2 | −84,5 | −1,3 dB |
| 1-kHz-Kamm (Summe) | −80,9 | −80,6 | +0,2 … +0,4 dB |
| fs/8-Linie bei 6000 Hz | −84,3 | −89,4 | −5,1 dB |
| Mischprodukte | −90,8 | ≈ −125 | ≈ −35 dB |

![Langzeit-Spektrum von fx3l (schwarz) gegen fx2d (grau), vier Kanäle](docs/img/psd_fx3l_vs_3d.png)

Der Kamm ist damit die stärkste verbleibende Familie. Die Alltags-Firmware auf dem Testmodul ist seit 2026-11-18 `v22.4.r-fx5a`: `fx3l` plus ein Boot-Menü, das den Patch-Slot mit den Reglern wählt (`fx4b`), plus ein Fix für den MIDI-Sendeweg. Mit `fx4b` kamen 19 von 79 Slot-Downloads neben einem laufenden Patch beschädigt an, danach hing MIDI bis zum Neustart. Mit `fx5a` waren 240 von 240 in Ordnung (D62, D63). Das Rauschen von `fx4b` ist innerhalb von ±0,4 dB gleich dem von `fx3l` (Kontrolle in derselben Sitzung), `fx5a` zeigt keine Änderung über die Streuung der Sitzung hinaus (D64). Einzelheiten und alle Zahlen: [docs/messlog.md](docs/messlog.md), Einträge D45 bis D49, D50 bis D59 und D62 bis D65.

## Firmware

Der Fork hat zwei Branches:

| Branch | Version | Inhalt |
|---|---|---|
| `acdc/thru-usb-feedback` | `v22.4.r-thru1d` | Der Patch-Ausgang erreicht die Buchsen ohne Rechner, dazu der Fix des USB-Feedbacks |
| `acdc/fx1d` | `v22.4.r-fx5a` | Wie oben. Der Rechner nimmt die rohen Eingänge auf, die Eingangs-LEDs zeigen beim Aufnehmen den rohen Pegel, der heiße Pfad läuft im ITCM, ein Boot-Menü wählt den Patch-Slot und merkt ihn sich, und der MIDI-Sendeweg ist repariert |

Beide beruhen auf dem Upstream-Commit `db9d3dd` (v22.4.r) mit den Libraries bei `9e8f64e`. Das README im Fork erklärt, warum, und was jede Änderung tut.

- `firmware/patches/` enthält dieselben Änderungen als nummerierte Patch-Dateien. `tools/build_acdc.sh` wendet sie auf einen sauberen Baum an.
- `firmware/builds/<name>/BUILD_INFO.txt` hält Commit, Toolchain, Patch-Liste und Prüfsummen jedes Builds fest. Die Binaries liegen nicht im Repo, jedes lässt sich bytegleich nachbauen. Fertige Binaries von `v22.4.r-fx2d`, `v22.4.r-fx3l`, `v22.4.r-fx4b` und `v22.4.r-fx5a` hängen an den [Releases des Forks](https://github.com/m9dfukc/OpenWare/releases).
- `firmware/flashlog/` hat je Flash einen Ordner: Geräte-Report davor und danach, DFU-Logs, Prüfsumme des Readbacks.

**Die offizielle `ACDC.bin` v22.5.0 von der Upstream-Release-Seite nicht auf ein AC/DC flashen.** Laut Forum macht sie USB kaputt ([Thread](https://community.rebeltech.org/t/ac-dc-firmware-update/2083)).

## Einstieg

Voraussetzungen: macOS, [uv](https://docs.astral.sh/uv/), `dfu-util` für Readback und Flashen, Arm GNU Toolchain 12.2.Rel1 für Firmware-Builds.

```sh
git clone https://github.com/m9dfukc/acdc-workbench.git
cd acdc-workbench
tools/setup_repo.sh    # Submodul, Upstream-Remote, feste Downloads mit Prüfsumme
uv sync
```

Die Aufrufe für Aufnahme, Loop-Prüfung, Auslesen und Nachbau stehen im englischen [README.md](README.md#getting-started). Der Flash-Ablauf steht in [CLAUDE.md](CLAUDE.md), Abschnitt „Flash-Ablauf“, als Skript in `tools/flash_acdc.py` (bisher nur ohne Modul geprüft).

## Aufbau des Repos

| Pfad | Inhalt |
|---|---|
| `tools/`, `analysis/` | Die Werkbank |
| `docs/` | Referenz-Docs `01` bis `05`, das Laborbuch `messlog.md`, Recherche-Notizen in `docs/research/` |
| `docs/en/` | Englische Fassungen der Referenz-Docs, siehe [docs/en/README.md](docs/en/README.md) |
| `firmware/OpenWare/` | Submodul, der Firmware-Fork |
| `firmware/patches/`, `firmware/builds/`, `firmware/flashlog/` | Patches, Build-Protokolle, Flash-Protokolle |
| `owl/` | Eigene OWL-Patches für das Modul: `Tanh3` (dreifacher tanh-Waveshaper mit Mix-Kanal), `Schliere` (Kette aus 61 Allpässen 2. Ordnung: Laufzeit je Frequenz, Phaser-Kerben, Resonator, mono hinein und stereo heraus) ein Ausgangs-Limiter für FX-Patches und eine Sperre für die Blockraten-Linien am Eingang, mit Tests am Rechner |
| `recordings/manifest.toml` | Metadaten jeder Aufnahme |
| `out/<ID>/` | Analyse-Report je Messung |
| `TODO.md`, `CLAUDE.md` | Offene Punkte und der Projektkontext für die Arbeit mit Claude Code |

Nicht im Repo: die Aufnahmen selbst (8 GB WAV), Plots und JSON-Ergebnisse in `out/`, Firmware-Binaries, die Geräte-Backups sowie fremde OWL-Patch-Quellen ohne Lizenz samt ihren Builds (`owl-patches/`). Plots und Ergebnisse erzeugt `python -m analysis` aus den Aufnahmen neu.

## Sprache

Die Arbeitsdokumente sind deutsch und bleiben es, Deutsch ist die Quelle.

- Englische Fassungen der Referenz-Docs `01` bis `05` und `99` liegen in [docs/en/](docs/en/README.md). Sie werden aus dem Deutschen erzeugt und zu Meilensteinen aufgefrischt. `python tools/i18n_check.py` listet veraltete Fassungen auf.
- Das Laborbuch `docs/messlog.md`, `TODO.md` und `CLAUDE.md` gibt es nur auf Deutsch.
- Die Werkzeuge geben Hilfe und Meldungen auf Englisch aus. Die Reports der Analyse sind deutsch.
- Die Recherche-Notizen in `docs/research/notes/` sind englisch.

## Lizenz

Werkzeuge MIT, Firmware-Patches GPL-2.0, Dokumente und Messdaten CC BY 4.0. Einzelheiten: [LICENSE.md](LICENSE.md).
