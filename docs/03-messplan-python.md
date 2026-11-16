# 03 – Messplan & Python-Analyse (uv)

Ziel: Herausfinden, **ob ich denselben 1-kHz-Kamm habe wie atau**, und welche Hypothese aus `02-noise-befunde.md` zutrifft. Jeder Schritt schneidet einen Hypothesenzweig ab.

## Setup

```sh
uv init --no-workspace   # falls noch nicht geschehen
uv add numpy scipy soundfile matplotlib
# optional: uv add rich typer   (CLI-Komfort)
```

Ordner: `recordings/`, `analysis/`, `out/`, `docs/messlog.md`.

## Aufnahmeregeln

- **Werkzeug ab 2026-11-16:** `tools/acdc_rec.py` (siehe `CLAUDE.md` „Konventionen“, `--help`). Es ersetzt für reine Aufnahmen die frühere Kette aus Host-Software und Mehrkanal-Recorder: duplex mit Nullen, 48 kHz, Block 256, 4-Kanal-WAV 16 Bit, Manifest-Eintrag mit `scale = 2.0` (Datei-dBFS wie die frühen Aufnahmen).
- **60 s** pro Messung, WAV, **nativ 48 kHz**. `acdc_rec.py` schreibt 16 Bit PCM, das ist das USB-Format des Geräts. Für Aufnahmen aus einer Host-Software gilt: 24 oder 32 Bit float. Die erste Serie (M1–M3) lag als 96 kHz / 16 Bit vor, also von der Aufnahme-Software hochgerechnet. Projekt-Samplerate in der Aufnahme-Software auf 48 kHz stellen, sonst verfälscht die Umrechnung Frequenzen und Rauschboden.
- Pro Messung notieren: Gerät (acdc1/acdc2), welcher Patch in Slot 1 läuft, Gain-Stellung, USB-Zustand.
- Referenz für die Frequenzachse: Die 6-kHz-Linie (= fs/8) ist sample-synchron. Liegt sie im File exakt auf 6000,00 Hz, ist das File im Sample-Takt des AC/DC und nicht umgetaktet (M1–M3: ja).
- Eingänge offen bzw. mit Dummy-Stecker (Kurzschluss-Klinke), sofern nicht anders angegeben.
- Gain-Knob-Positionen notieren (z. B. `g07` = 7 Uhr, `g12`, `g17` = Vollanschlag).
- Ab Schritt 6 brauche ich ein **zweites, sauberes Interface** als Referenz-Recorder (für die AC/DC-Ausgänge). Vorhanden: **Behringer UMC202HD**. Dabei beachten:
  - Richtung UMC → AC/DC (Line-Pegel in den AC/DC-Eingang) ist unkritisch, z. B. Testton für Schritt 2b.
  - Richtung AC/DC → UMC: Die AC/DC-Ausgänge können ±10 V liefern, das verträgt der UMC nicht. Nur mit Abschwächer (passiv oder Attenuator-Modul) oder sicher kleinem Pegel anschließen.
  - Das UMC hängt am selben Thunderbolt-Hub. Ist ein Audiokabel zwischen beiden gesteckt, entsteht ein zusätzlicher Massepfad. Für Schritt 6 notieren, ob der Rechner/Hub beim Aufnehmen mit dem AC/DC per USB verbunden ist.
  - Für Schritt 2b hat auch der UMC einen eigenen Taktfehler (unbekannt, typ. einige 10 ppm). Der Test ist deshalb relativ. Vor dem Messen das Vorgehen noch einmal durchdenken (`/grill-me`).
- Gleiche Aufnahme auch mit **beiden** AC/DCs machen, damit Unterschiede zwischen den Exemplaren sichtbar werden.

## Messschritte

| # | Test | Datei-Suffix | Schluss |
|---|---|---|---|
| 1 | AC/DC → Rechner per USB, Eingänge offen, Gain 12 Uhr, 60 s. Zusätzlich Gain-Serie 7/12/17 Uhr | `open-inputs_g12_usb-stream` | Liefert die Signatur: Linien bei k·1 kHz → H1. Bei 50 Hz·k → H2. Bei ≈2,32 kHz·k → H3. Klick-Bursts → H5. Breitband skaliert mit Gain → H6 |
| 2 | Aus Schritt 1 die Grundfrequenz f0 exakt bestimmen (Peak-Interpolation) | – | Bei SOF-Kopplung erwarte ich im File etwa **1000,0–1000,2 Hz**, nicht exakt 1000. f0 ist auch der Filter-Parameter. **M1: 1000,053 Hz** [gemessen] |
| 2b | **Echte Samplerate des AC/DC messen:** Testton aus einem Referenz-Interface (bekannte Frequenz, z. B. 1000,000 Hz) ins AC/DC, per USB aufnehmen. Abweichung im File = Taktfehler des AC/DC | `fs-check` | fs ≈ 47 997,5 Hz → Kamm ist SOF-gekoppelt (H1). fs ≈ 47 991 Hz → Kamm kommt nicht vom SOF |
| 3 | Pass-through- oder Bypass-Patch laden (umgeht die Gain-Regler), erneut aufnehmen | `bypass-patch` | Unverändert → Störung steckt in den ADC-Daten |
| 4 | Laptop im Akkubetrieb, nur das AC/DC am Rechner, direkter Port | `battery` | Weg → H2 (Host-Masseschleife), dann lohnt ein Isolator |
| 5 | Audioseite: AC/DC-Ausgänge gehen in ein geerdetes Pult? Schleife per DI mit Ground-Lift trennen | `groundlift` | Weg → Masseschleife über die Audioleitungen |
| 6 | **Standalone-Gegenprobe:** USB ab, Patch in Slot 1 läuft. AC/DC-Ausgänge mit dem Referenz-Interface aufnehmen, Eingänge offen, Gain hoch. Danach USB anstecken, Stream starten (AC/DC in der DAW als Gerät wählen) und erneut aufnehmen | `standalone_usb-off`, `standalone_usb-on` | Kamm nur mit aktivem Stream → **H1 bestätigt**. Diesen Test hat noch niemand gemacht |
| 7 | LED-Test: Patch, der LED-Parameter AA–AD und BA–BD konstant auf 0 setzt | `leds-off` | ≈2,32-kHz-Linien weg → H3 |
| 8 | Erst jetzt Isolator testen (falls 4 oder 5 positiv) | `isolator` | – |

Jeden Schritt in `docs/messlog.md` festhalten: Datum, Gerät, Datei, Pegel der Top-Linien, Fazit.

**Stand der Schritte (2026-11-16):**

| # | Stand | Beleg |
|---|---|---|
| 1 | erledigt | M1/M2, sauber wiederholt in Serie 2 |
| 2 | erledigt | f0 = 1000,0528 Hz (acdc2 am Hub). f0 hängt am USB-Anschluss (S2-6) |
| 2b | entfallen | H1 ist über S2-6 belegt. Taktverhältnis UMC/acdc1 = 1,000185 (D20) |
| 3 | entfallen | Gain 0 → USB-Strom digital stumm (Serie 2). Rohe Eingänge mit Build 2 (D25/D26) |
| 4 | entfallen | Mobiler Betrieb kommt nicht vor (Nutzer 2026-11-15). Masseschleife geklärt (D21) |
| 5 | entfallen | D21: Masseschleife nur mit AC/DC am Mac-Port und UMC am Hub. Im Alltag gibt es AC/DC-Out → UMC nicht |
| 6 | erledigt | S3 mit Build 1d (D20): Kamm am Ausgang ohne USB weg, schon ohne Stream da |
| 7 | **offen** | LED-aus-Patch für H3 |
| 8 | entfallen | Kein Isolator nötig (D21–D23) |

## Serie 2 (nächste Aufnahmen, Stand 2026-11-13)

Ziel: M1/M2 sauber wiederholen und die neuen Fragen klären (Musterperiode 3,16 s, Firmware-Einfluss, SOF ja/nein).

| # | Gerät | Eingänge | Gain | Dauer | Datei-Basis | Frage |
|---|---|---|---|---|---|---|
| S2-1 | acdc2 | offen (nichts gesteckt) | g12 | **120 s** | `<datum>_acdc2_open-inputs_g12_usb-stream` | Referenz: f0, Mischprodukte, 3,16-s-Periode, Klicks |
| S2-2 | acdc2 | offen | g17 | 60 s | `…_acdc2_open-inputs_g17_usb-stream` | Gain-Abhängigkeit, LED-Linie |
| S2-3 | acdc2 | offen | g07 | 60 s | `…_acdc2_open-inputs_g07_usb-stream` | Was bleibt bei minimalem digitalem Gain? |
| S2-4 | acdc1 | offen | g12 | 120 s | `…_acdc1_open-inputs_g12_usb-stream` | Anderes Exemplar, ggf. andere Firmware/Blockgröße → anderes Linienbild? Device-Status (Firmware, Patch) notieren |
| ~~S2-5~~ | – | – | – | – | – | Entfällt: kein zweiter Rechner vorhanden (2026-11-13). Ersatz: S2-6 und S3 unten |
| S2-6 | acdc1 (geplant war acdc2) | offen | g12 | 119 s | `20261114_acdc1_nohub_open-inputs_g12_usb-stream.4chan.000.4chan.000.wav` (geplant: `…_usb-direct`) | **AC/DC direkt an einem USB-Port des Macs statt am Thunderbolt-Hub.** Anderer USB-Controller → anderer SOF-Takt. Verschiebt sich f1k (1000,0528 Hz), ist der Kamm SOF-gekoppelt |

Stand 2026-11-13: S2-1 bis S2-4 und S2-6 aufgenommen und ausgewertet (siehe `messlog.md`). Device-Status beider Module notiert.

**S3 – USB-Zustände über den UMC202HD. Status 2026-11-15: gemessen mit Build 1d (messlog D20)**, einkanalig (Out 1), zusätzlich Zustand d (Duplex), Ergebnis: SOF-Kamm ohne USB weg, Masseschleife dominiert mit USB. Ursprünglicher Stand 2026-11-14: mit damaliger Firmware nicht messbar, weil die Ausgänge ohne Rechner-Playback stumm sind (siehe `messlog.md`, „Durchleitung“). Erst die Durchleitung klären, ggf. eigene Firmware (Phase 5). Geplanter Aufbau aus der `/grill-me`-Runde: acdc1 direkt am Mac, Eingänge offen, Gain 12; Out 1/2 → MTM Startup (L/R, Pegel auf Line) → Y-Kabel → UMC In 1/2 (LINE, Gain fest); Aufnahme in der Host-Software; Zustand (c) über ein Aufnahmeprogramm (nur Eingang), weil die Host-Software das AC/DC in beide Richtungen öffnet; Startup- und UMC-Pegel fest; Reihenfolge S3-0 (UMC allein), b, c, a, b2 à 120 s.

Ursprüngliche Idee: Die AC/DC-Ausgänge über einen Abschwächer mit dem UMC aufnehmen, in drei Zuständen:
- (a) USB-Kabel des AC/DC abgezogen,
- (b) USB gesteckt, aber kein Stream (keine Software nutzt das AC/DC),
- (c) AC/DC-Eingänge streamen per USB.

Erwartung bei SOF-Kopplung: 1-kHz-Kamm und Mischprodukte in (a) weg, die 6-kHz-Linie bleibt. Ist der Kamm in (b) schon da, reicht der SOF allein, sonst braucht es den Iso-Datenverkehr. Offen vor dem Messen: Abschwächer, DAW-Routing für (c) (in Stock-Firmware überschreibt aktives USB-Playback den DAC), Massepfad über das Audiokabel. Vorher mit `/grill-me` durchgehen.

Aufnahme-Einstellungen für Serie 2 und S3 (Host-Software, vor `acdc_rec.py`): Projekt **48 kHz**, Aufnahmeformat **32 Bit float** (oder 24 Bit), **eine 4-Kanal-WAV** pro Messung (oder 4 Mono-Dateien `_ch1…_ch4`), keine Plugins/Effekte auf den Eingangsspuren, kein Dither beim Export. Danach Eintrag in `recordings/manifest.toml` (ID S2-1 …) und `uv run python -m analysis S2-1`.

## Analyse-Tool (`analysis/`) – Umsetzung

Stand 2026-11-13: Punkte 1–9 der Spezifikation unten sind umgesetzt.

```sh
UV_CACHE_DIR=.uv-cache uv run python -m analysis M1            # Manifest-ID
UV_CACHE_DIR=.uv-cache uv run python -m analysis M2 --ref M1   # mit Referenz-Overlay + Δ-Tabelle
UV_CACHE_DIR=.uv-cache uv run python -m analysis aufnahme.wav  # direkt eine Datei
UV_CACHE_DIR=.uv-cache uv run python -m analysis.selftest      # Selbsttest mit synthetischem Signal
```

Ausgabe in `out/<name>/`: `_report.md`, `.json`, `_spectrogram.png`, `_psd.png`, `_combs.png`, `_timeline.png`.

| Modul | Inhalt |
|---|---|
| `audio_io.py` | WAV/Manifest laden, Kanäle zusammensetzen, DC abziehen. Manifest-Feld `channels = [1, …]` (1-basiert) wählt Kanäle aus, z. B. um leere Kanäle wegzulassen (seit 2026-11-15) |
| `spectra.py` | Hann-Voll-FFT, parabolische Peak-Interpolation, lokaler Rauschboden (Median), Welch, A-Bewertung |
| `lines.py` | Familien fs/8, 1 kHz, LED, Netz + stärkste übrige Linien, gewichteter f0-Fit, Mischprodukte n·f1 + m·f2, Leistungsanteile nach Parseval |
| `timing.py` | f0/Pegel in Fenstern (Standard 10 s), Hüllkurven-Modulation, Klick-Detektor |
| `plots.py`, `report.py` | Abbildungen, Markdown, JSON |
| `selftest.py` | synthetisches Signal mit bekannten Linien, Mischprodukten, Klicks. Prüft f0 < 5 mHz, Pegel ± 0,5 dB |

Weitere Auswerte- und Gerätewerkzeuge liegen in `tools/` (Aufnahme, Loop-Prüfung, Familientabellen über mehrere Messungen, Geräte-Report). Die Übersicht steht in `CLAUDE.md`, Abschnitt „Werkzeuge in `tools/`“.

Grenzen: Zwei Linien lassen sich erst ab ≈ 4 Bins Abstand trennen (Bin = 1 / Dauer). Bei 10 s sind das 0,4 Hz, die Mischprodukte im Abstand 0,316 Hz verschmelzen dann. Deshalb ≥ 60 s aufnehmen.

## Spezifikation für das Analyse-Tool (`analysis/`)

Ursprüngliche Vorgabe vom 2026-11-13, umgesetzt bis auf den Punkt „RMS nach Notch-Bank“ (kommt mit `analysis/notch.py`, siehe `04`). Aufruf und Dateinamen stehen im Abschnitt „Umsetzung“ oben.

Ein CLI-Skript, z. B. `uv run analysis/noise.py recordings/<file>.wav --channel all`. Es soll Folgendes liefern:

1. **Spektrogramm** (habe ich schon). Empfehlung: STFT mit Hann-Fenster, nperseg 8192–16384, log-Frequenzachse 20 Hz bis 24 kHz, dBFS-Skala. Damit werden zeitliche Muster sichtbar (Klicks, 0,8-s-Periode, Drift).
2. **Langzeit-PSD** (Welch, `nperseg=65536` oder größer, Hann) → `out/<name>_psd.png`, log-x, dBFS/√Hz bzw. dBFS pro Bin. Auf derselben Achse optional eine Referenzdatei (`--ref`) überlagern, für A/B-Vergleiche.
3. **Peak-Liste**: die Top-N-Linien über dem Median-Noise-Floor (z. B. +10 dB), mit **parabolischer oder quadratischer Interpolation** auf dem log-Magnitudenspektrum, damit die Frequenz auf <0,05 Hz genau ist. Ausgabe als JSON und Markdown-Tabelle: Frequenz, Pegel dBFS, Abstand zum Floor.
4. **Harmonik-Erkennung**: Testet die Kandidaten-Grundfrequenzen 50, 60, 1000 und 2320 Hz sowie die Grundfrequenz der stärksten Linie. Für jede wird das „Kammprofil“ ermittelt: Pegel bei k·f0 (k = 1…⌊24000/f0⌋) und der Anteil der Energie im Kamm am Gesamtrauschen. Ergebnis: Welche Familie dominiert?
5. **f0-Fit**: Least-Squares über alle gefundenen Harmonischen (f_k ≈ k·f0) → präzises f0 + Residuen. Wichtig für den Notch-Filter, weil die oberen Harmonischen sonst verfehlt werden.
6. **Stabilität über die Zeit**: f0 und Pegel in 5-s-Fenstern. Driftet f0? Schwankt der Pegel periodisch (LED, 0,8 s)?
7. **Klick-Detektion** (für H5): Hochpass bei ca. 5 kHz, Hüllkurve, Schwelle, Abstände zwischen Ereignissen. Regelmäßige Abstände von wenigen Sekunden (z. B. ≈3,9 s) deuten auf den USB-TX-Ratenfehler hin.
8. **Kennzahlen pro Kanal**: RMS gesamt (dBFS), RMS nach Notch-Bank (siehe `04`), A-gewichtet optional. Damit lässt sich sagen, wie viel des Rauschens der Kamm ausmacht.
9. **Report** `out/<name>_report.md` mit den Plots und Tabellen, zum Einfügen in den Messlog.

Hinweise:
- Die AC/DC-Aufnahme über USB ist 16 Bit, der Boden liegt bei ca. −96 dBFS. Linien bei −30 dB sind also weit darüber.
- Alle 4 Kanäle getrennt analysieren. Bei Kopplung auf der Platine sind die Pegel oft kanalabhängig.
- DC-Offset vor der FFT abziehen (das AC/DC ist DC-gekoppelt).

## Entscheidungsbaum nach den Messungen

```
Kamm k·1 kHz?
├─ nein → 50 Hz-Familie? → Masseschleife (H2) → Akku/Ground-Lift/Isolator (02)
│        └─ 2,32 kHz? → LED-PWM (H3) → LED-Patch / Firmware-PWM verschieben (05)
└─ ja → Schritt 6: nur mit USB-Stream?
         ├─ ja (H1) → Isolator sinnlos → Notch-Patch (04) + Standalone-Firmware (05)
         └─ nein → Kopplung geräteintern unabhängig von USB → Notch-Patch (04), Firmware-Experimente H3/H4
Klick-Bursts? → shmuga-Fixes backporten (05)
```

**Ergebnis (2026-11-15) [gemessen]:** Kamm ja → Schritt 6: Am Ausgang ist er ohne USB weg und schon ohne Stream da (D20). Das ist der Zweig H1: Ein Isolator ist sinnlos, weiter mit Firmware (`05`) und Filter (`04`). Klick-Bursts gab es keine (D6, D7, D27).
