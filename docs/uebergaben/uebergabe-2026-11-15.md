# Übergabe – Stand 2026-11-15, nachmittags

Für eine neue Session. Zuerst lesen: `CLAUDE.md` (vor allem „Eigene Firmware auf acdc1“ und „Signalfluss im Alltag“), dann `TODO.md` Phase 5. Die Messungen von heute stehen in `docs/messlog.md` **D19–D23**. Hier steht nur, was für den Einstieg wichtig ist. Die vorige Übergabe `docs/uebergaben/uebergabe-2026-11-14-abend.md` ist damit überholt, ihre Fallstricke gelten aber weiter (unten übernommen).

## Wo wir stehen

- **acdc1 läuft mit Build 1d `v22.4.r-thru1d`** (unverändert seit 2026-11-14, Fork-Branch `acdc/thru-usb-feedback` gepusht). Abnahme komplett:
  - A1–A4 und A6 (Langlauf) waren schon durch (D11–D18).
  - **A5 bestanden (D19):** Offene Eingänge im Mittel 1,1 dB leiser als Build 1b. Die Mischprodukte sind dabei +4,7 dB lauter, Ursache offen.
  - **A7 = S3 gemessen (D20):** Der SOF-Kamm ist am Ausgang **ohne USB weg** und **schon ohne Stream da**. Der Standalone-Ausgang ist sauber: nur fs/8, ein schwacher fs/48-Kamm (Firmware-intern?) und 50 Hz.
- **acdc2 unberührt** (v22.4.q). Nie flashen, nie Settings schreiben.
- **Masse geklärt (D21–D23):**
  - Eine Masseschleife (+20 dB) gab es nur im Messaufbau mit AC/DC am Mac-Port und Out 1 → Startup → UMC am Hub. Mit beiden Geräten am Hub ist sie weg.
  - Die 59,98-Hz-Impulse kommen vom Monitor am Hub.
  - **Alltags-Aufbau** (AC/DC → passiver USB-Hub → Monitor-Hub → TB-Hub, UMC nur als Ausgabe): Ausgang sauber, Eingänge wie TB-Hub direkt und wie A5 (A/B G5/G6 auf 0,1–0,4 dB gleich). Kein Isolator nötig. G3 (ohne Hub) entfällt.
- **Analyse-Tool:** neues Manifest-Feld `channels = [1]` (Kanalauswahl, `analysis/audio_io.py`), Selbsttest läuft.

## Nächste Schritte (Vorschlag, Reihenfolge)

1. **Build 2 neu auf 1d-Basis:** `db9d3dd` + 01, 02, 04, 05, 06 + `03-tx-pre-fx-owl-acdc-fx.patch`.
   - Zuerst prüfen, ob 03 auf dieser Basis sauber geht (`patch --dry-run` in einem `mktemp`-Baum).
   - `owl_read.py` um `--port` für den Portnamen „OWL-ACDC-FX“ erweitern.
   - Vorher `/grill-me`. Bauen und Flashen nur mit ausdrücklicher Freigabe.
   - Abnahme A1–A6 + B1–B3 (`docs/05`).
   - Neu zu bedenken: Die Durchleitung ist aus, sobald macOS Playback schickt, und das passiert schon bei reiner Aufnahme (D20). Bei `TX_PRE_FX` bekommt der Rechner die rohen Eingänge. Was dann an den Ausgängen liegt, hängt von `RX_PRE/POST_FX` ab (`docs/01`, Routing-Tabelle).
2. **README im Fork-Branch** (was, warum, bauen/flashen, Messergebnisse inkl. D19–D23), danach ein Hinweis im Forum-Thread #2244. Pushen und Posten nur nach Freigabe.
3. **Mischprodukte +4,7 dB (D19):** Firmware oder Sitzung? A5 zweimal in einer Sitzung aufnehmen (Streuung), oder A/B bei Build 2.
4. **Kleinkram (TODO):**
   - Clipping-Fehlalarm bei Float-Dateien (`analysis/__main__.py:72`)
   - Paar-IMD-Test (D6)
   - optional: alte Firmware (Readback) auf Feedback-Regelung disassemblieren
   - optional: Build aus dem Fork-Branch, SHA gegen 1d vergleichen
5. **Offene Fragen** (kein Muss):
   - Herkunft Fremdkamm 1000,0346 Hz und 29,2-Hz-Familie (nur in der Mac-Port-Schleife)
   - fs/48-Kamm ohne USB (SysTick?)
   - Einzelereignis D18
   - 186 ppm acdc1/acdc2
   - TB-Hub-Ports mit verschiedenem SOF (999,868 / 999,997 Hz)

## Fallstricke

**Neu (2026-11-15):**
- **Host-Software öffnet ein Gerät immer in beide Richtungen.** Ist das AC/DC in einem Audio-Modul gewählt, ersetzt der USB-Playback (Stille) die Durchleitung. Für Ausgangsmessungen in der Host-Software nur den UMC auswählen.
- **Auch eine reine Aufnahme in einem Aufnahmeprogramm** schaltet die Durchleitung ab, weil macOS den Playback-Stream mitstartet (D20, S3-c).
- **Leere Dateien:** Zweimal kam aus der Host-Software eine Datei, in der jedes Sample 0 ist (G4-in). Vor der Auswertung prüfen (`np.count_nonzero`), den Nutzer vor der Aufnahme auf Pegelanzeige/Scope achten lassen.
- **Zwei Zeitbasen:** UMC-Dateien laufen im UMC-Takt, AC/DC-Dateien im acdc1-Takt. Verhältnis UMC/acdc1 = 1,000185. Linien vor dem Vergleich umrechnen. Das Analyse-Tool sucht fs/8 nur bei exakt 6000 Hz, in UMC-Dateien liegt sie bei 6001,11 Hz und wird als „other“ gemeldet.
- **Offene Eingänge streuen:** Einzelne Ausreißer bis +10 dB breitbandig (D22/D23). Doppelt aufnehmen (b/b2-Prinzip), währenddessen nichts am Rack anfassen.
- **Dateinamen:** Datum = Aufnahmedatum (eine A5-Datei wurde von 20261114 auf 20261115 umbenannt). Mehrkanal-Recorder hängt `.2chan.000` bzw. `.4chan.000` an. Versehentliche Aufnahmen nicht überschreiben, sondern umbenennen und als eigenen Messpunkt behalten (G2a).
- **Leerer Kanal 2** in den UMC-Dateien (in der Host-Software nicht verbunden) → `channels = [1]` im Manifest, sonst stört er die Auswertung.
- Hilfsskripte von heute lagen nur in `$TMPDIR` (Linien-Suche um 1/2/6 kHz, Kanalmittel-Vergleich). Bei Bedarf neu schreiben oder als `tools/`-Skript anlegen.

**Weiter gültig (aus der Übergabe vom 14.11.):**
- Host-Pegel: Datei-dBFS aus Mehrkanal-Recorder = Gerät + 6,02 dB. Aufnahmeprogramm-Dateien haben diesen Faktor nicht.
- `owl_read.py`, `dfu-util` und git-Schreibzugriffe in `firmware/OpenWare/.git` gehen nur außerhalb der Sandbox.
- Geräte-Meldung zuerst lesen, dann Host-Software stoppen, denn es bleibt nur die letzte Meldung.
- `usbd_audio.cpp` hat CRLF-Zeilenenden: beim Editieren per Skript binär lesen und schreiben.
- Patches mit `patch -p1` einspielen, nicht mit `git apply` (scheitert an `ACDC/Core/Inc/hardware.h`).
- zsh: Variablen werden nicht in Wörter zerlegt, Arrays benutzen. Prozess-Substitution `<(…)` ist in der Sandbox gesperrt.
- Flash-Ablauf ohne Boot-Pads steht in `CLAUDE.md`. Danach startet der Nutzer neu: Case aus, USB ab, Case an, USB an.

## Empfohlene Skills

- `grilling` (`/grill-me`): vor Build 2.
- `research`: bei Fragen zu macOS-UAC1 (Playback-Start bei reiner Aufnahme?) oder zu Forum-Themen. Ablage in `docs/research/notes/`.
