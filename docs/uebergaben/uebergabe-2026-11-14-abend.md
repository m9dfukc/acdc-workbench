# Übergabe – Stand 2026-11-14, abends

Für eine neue Session. Zuerst lesen: `CLAUDE.md` (Abschnitt „Eigene Firmware auf acdc1“), dann `TODO.md` Phase 5. Details stehen in `docs/messlog.md` D9–D18 und `docs/05-firmware-plan.md` (Build 1d, Fork). Hier steht nur, was dort fehlt oder für den Einstieg wichtig ist.

## Wo wir stehen

- **acdc1 läuft mit Build 1d `v22.4.r-thru1d`** (`firmware/builds/acdc1-build1d-thru1/`).
  - Geht: Durchleitung ohne Rechner, Interface mit Rechner, Pegel wie die alte Firmware.
  - Im 30-min-Loop gibt es keine USB-Block-Slips mehr.
  - Vom Nutzer als Stand angenommen.
- **acdc2 ist unberührt** (v22.4.q). Nie flashen, nie Settings schreiben.
- **Fork:** Branch `acdc/thru-usb-feedback` auf `github.com/m9dfukc/OpenWare` ist gepusht und gleich Build 1d.
  - Lokal ist das der einzige Klon `firmware/OpenWare` mit den Remotes `upstream` und `fork`. Er ist auf diesen Branch ausgecheckt.
- **Aufgeräumt** (2026-11-14):
  - Ordnerübersicht in `firmware/README.md`.
  - Backups liegen in `backup/acdc1/20261114/{flash,owl}/`, die OWL-Library-Patches in `owl-patches/library/`.
  - `owl_read.py` schreibt standardmäßig nach `out/owl_read/` und überschreibt nie.

## Nächste Schritte (Vorschlag, Reihenfolge)

1. **A5 mit Build 1d:** offene Eingänge 120 s, Gain 12 Uhr, Hub. Mit `uv run python -m analysis <ID> --ref A5-b1b` gegen `A5-b1b` vergleichen. Zweck: Rauschvergleich nach der USB-Änderung.
2. **A7 = S3:** Kamm an den Ausgängen bei USB ab, gesteckt und streamend. Aufbau steht in `docs/03`. Seit Build 1d möglich. Beantwortet die offene Frage, ob der 1-kHz-Kamm ohne USB verschwindet.
3. **Build 2 neu:** `db9d3dd` + 01, 02, 04, 05, 06 + `03-tx-pre-fx-owl-acdc-fx.patch`.
   - Zuerst prüfen, ob 03 auf dieser Basis sauber geht (`patch --dry-run` in einem `mktemp`-Baum).
   - Der alte Build 2 in `builds/archive/` hat den v22.4.s-Takt, gibt also kein Audio.
   - `owl_read.py` für den Portnamen „OWL-ACDC-FX“ erweitern (`--port`).
   - Bauen und Flashen nur nach ausdrücklicher Freigabe.
4. **README im Fork-Branch** (was, warum, wie bauen/flashen, Messergebnis), dann ein Hinweis im Forum-Thread #2244. Pushen nur nach Freigabe.
5. **Kleinkram aus TODO:**
   - Clipping-Fehlalarm bei Float-Dateien in `analysis/__main__.py:72`.
   - Paar-IMD-Test (D6).
   - Optional: die alte Firmware (Readback) auf Feedback-Regelung disassemblieren.
   - Optional: Build aus dem Fork-Branch, SHA gegen 1d vergleichen.

## Fallstricke, die Zeit gekostet haben

- **Host-Pegel:** Dateiwerte aus Host-Software (Mehrkanal-Recorder) liegen +6,02 dB über dem Gerät. Kein Clipping, auch wenn die Float-Datei über ±1,0 geht.
- **Werkzeuge außerhalb der Sandbox:** `owl_read.py` und `dfu-util` laufen nur so (CoreMIDI/USB). Ebenso git-Schreibzugriffe in `firmware/OpenWare/.git` (commit, fetch, push).
- **Geräte-Meldung:** Erst lesen, dann Host-Software stoppen. Es bleibt nur die letzte Meldung. Bedeutung der Meldungen: `CLAUDE.md` bzw. `docs/01` (USB-Tabelle).
- **`usbd_audio.cpp`** hat CRLF-Zeilenenden. Beim Editieren per Skript binär lesen und schreiben, sonst wird der Diff riesig.
- **`patch` statt `git apply`:** `git apply` scheitert an `ACDC/Core/Inc/hardware.h` (Patch 04), `patch -p1` geht.
- **zsh:** Variablen werden nicht in Wörter zerlegt (`F="a b"; grep … $F` geht nicht), Arrays benutzen.
- **Prozess-Substitution `<(…)`** ist in der Sandbox gesperrt. Mit Temp-Dateien in `$TMPDIR` arbeiten.
- **Flash-Ablauf** steht in `CLAUDE.md` und kommt ohne Boot-Pads aus (SysEx 0x7E). Der Nutzer startet danach neu: Case aus, USB ab, Case an, USB an.

## Offene Fragen

- Einzelereignis D18: ≈ 20 ms gestört, ≈ 32 ms ohne SOF, kein Netto-Versatz. Liegt die Ursache am Hub/Bus oder am Host? Wenn es im Alltag hörbar wird: Langlauf direkt am Mac-Port.
- Liegt der Unterschied von 186 ppm zwischen Sample- und CPU-Takt zwischen acdc1 und acdc2 an der Hardware oder an HAL/Firmware?
- Herkunft der 119,944-Hz-Familie direkt am Mac.

## Empfohlene Skills

- `grilling` (bzw. `/grill-me`): vor Build 2 und vor Option A (v22.5.0 + altes HAL), um den Plan abzuklopfen.
- `research`: falls zu macOS-UAC1-Feedback oder Forum-Themen recherchiert werden muss. Ablage in `docs/research/notes/`.
