# Übergabe – Stand 2026-11-15, abends

Für eine neue Session. Zuerst `CLAUDE.md` lesen (vor allem „Build 2 auf acdc1“), dann `TODO.md` Phase 5. Die Messungen von heute Nachmittag stehen in `docs/messlog.md` **D24–D27**. Diese Übergabe ersetzt `uebergabe-2026-11-15.md`. Deren Fallstricke gelten weiter und sind unten übernommen.

## Wo wir stehen

- **acdc1 läuft mit Build 2 `v22.4.r-fx1d`** (`firmware/builds/acdc1-build2-fx1d/`, SHA `7f9f9a34…`):
  - = Build 1d + Patch 03 (`USE_USBD_AUDIO_TX_PRE_FX`, Produktstring „OWL-ACDC-FX“)
  - Geflasht 2026-11-15, Log `firmware/flashlog/20261115_build2-fx1d/`
  - Abnahme A1–A6 und B1–B3 bestanden (D25–D27)
- **Routing [gemessen/Code]:**
  - Der Rechner nimmt die rohen Eingänge auf, der Gain-Knob wirkt nicht darauf (B2).
  - Ohne USB-Stream liegt der Patch an den Ausgängen.
  - Mit Stream liegt das USB-Playback an den Ausgängen, auch bei reiner Aufnahme, weil macOS den Playback mitstartet (D20).
- **Mischprodukte-Frage geklärt (D24):**
  - 2 × A5 mit 1d (Neustart der Host-Software dazwischen) sind auf ≤ 0,1 dB gleich.
  - Die +4,8 dB gegenüber 1b kommen also von der Firmware (Patch 05 und/oder 06), nicht von der Sitzung.
  - Build 2 liegt gegenüber 1d nur +0,2 dB höher.
- **B3 = neue Rausch-Basislinie (D26),** Datei-dBFS (Gerät = −6,02 dB), unabhängig vom Knob:
  - RMS ≥ 20 Hz −72,6, A-bewertet −73,8, Rest −78,1
  - Kamm −76,4, fs/8 −79,0, Mischprodukte −85,5 dB
  - Störanteil 71 %, ideale Notch-Bank 5,5 dB
- **Rückfall:** Build 1d (`firmware/builds/acdc1-build1d-thru1/ACDC.bin`, `f522560e…`), dann das Readback (`433b3fd3…`). Ablauf wie in `CLAUDE.md`.
- acdc2 unberührt.

## Nächste Schritte (Vorschlag)

1. **Alltag mit Build 2** (Entscheidung des Nutzers, Grill-Runde Q1): ein paar Tage benutzen, dann festlegen, ob Build 2 bleibt oder wieder 1d drauf kommt.
2. **Fork-Branch `acdc/fx1d`** ist lokal angelegt (`f7a255cc` TX pre-FX + Produktstring, `11199347` Version, `741bac39` README englisch), Code gleich Build 2:
   - **Gepusht 2026-11-15:** https://github.com/m9dfukc/OpenWare/tree/acdc/fx1d. Offen: Hinweis im Forum-Thread #2244 (Posten nur nach Freigabe).
   - README auch auf `acdc/thru-usb-feedback` (`41fb9480`, gepusht 2026-11-15).
3. **Rausch-Experimente (E3)**, jeweils als eigener Build auf Build-2-Basis, A/B gegen B3 (2 × 60 s, Neustart der Host-Software dazwischen, Schwelle ≈ 0,5 dB):
   - Blockgröße 16
   - LED-PWM aus dem Audioband
   - Codec-HPF an
   - optional: Build 1c (nur 05) bzw. 2 ohne 06, um herauszufinden, welcher Patch die Mischprodukte hebt
4. **Kleinkram (TODO):**
   - Clipping-Fehlalarm bei Float-Dateien (`analysis/__main__.py:72`)
   - Paar-IMD-Test (D6)
   - MIDI-Name „OWL-ACDC“ in CoreMIDI (kosmetisch, MIDI-Studio)
5. **Offene Fragen:**
   - `fb 48.0004 96.2500` nach A6 (ein SOF ≈ 2 ms verspätet, folgenlos)
   - Einzelereignis D18
   - Fremdkamm 1000,0346 Hz und 29,2-Hz-Familie
   - fs/48-Kamm ohne USB
   - 186 ppm acdc1/acdc2
   - TB-Hub-Ports mit verschiedenem SOF

## Fallstricke

**Neu (2026-11-15 nachmittags):**
- **Host-Gerät heißt jetzt „OWL-ACDC-FX“.** Neuer Patch `vcv-patches/acdc-fx-umc-in-out.vcv`, das Original (`OWL-ACDC`) bleibt für 1d.
- **MIDI-Port heißt weiter „OWL-ACDC“** (CoreMIDI merkt sich den alten Namen). `owl_read.py` findet ihn per Teilstring, `--port` nicht nötig.
- **Vergleich mit 1d-Aufnahmen:** Bei 1d ging die USB-Aufnahme durch den VCA des Patches ((2·Knob)², bei 12 Uhr nicht exakt ×1). Den Faktor je Kanal über das **DC-Verhältnis** der offenen Eingänge bestimmen und abziehen (D26: +0,37/+0,46/+0,48/+1,62 dB).
- **Übersprechen:** Gain auf Vollanschlag übersteuert den Ausgang. Dessen Harmonische sprechen um 9–17 dB in offene Eingänge über (D25). Rauschmessungen deshalb ohne Signal am Ausgang.
- **Gleich lange Stücke vergleichen:** Die 60-s-Kürzung ändert nichts (D26), trotzdem 1d-Aufnahmen bei Bedarf kürzen (`out/A5-b1d-r{1,2}-60s/`).
- MIDI-Abfragen (`owl_read.py`) nicht während einer laufenden Messung, erst danach, aber bevor Host-Software gestoppt wird.

**Weiter gültig:**
- Host-Software öffnet ein Gerät immer in beide Richtungen. Auch eine reine Aufnahme in einem Aufnahmeprogramm startet den Playback-Stream (D20).
- Leere Dateien: vor der Auswertung `np.count_nonzero` prüfen.
- Zwei Zeitbasen: UMC/acdc1 = 1,000185.
- Offene Eingänge: doppelt aufnehmen, nichts am Rack anfassen.
- Dateinamen: Datum = Aufnahmedatum. Mehrkanal-Recorder hängt `.4chan.000` an.
- Leerer Kanal 2 in den UMC-Dateien → `channels = [1]`.
- Host-Pegel: Datei-dBFS = Gerät + 6,02 dB.
- `owl_read.py`, `dfu-util` und git-Schreibzugriffe gehen nur außerhalb der Sandbox.
- `usbd_audio.cpp` hat CRLF. Patches mit `patch -p1` einspielen.
- zsh: Arrays benutzen, `<(…)` ist gesperrt.
- `firmware/_work/` enthält nur den letzten Baum. Für Diffs andere Stände per `git archive` + Patches in `$TMPDIR` neu erzeugen.

## Nachtrag: Plan „Build 3 – LEDs zeigen beim Aufnehmen die rohen Eingänge“ (2026-11-15 abends)

**Befund [Code, Basis `acdc/fx1d`]:**
- **Ausgangs-LEDs 5–8:** Die Firmware misst sie selbst, `tx_levels` in `audioCallback` (`Source/ProgramManager.cpp:214`, geglättetes Quadratmittel des DAC-Puffers). Sie zeigen also immer den echten Ausgangspegel.
- **Eingangs-LEDs 1–4** samt Rot: `onLoop` in `ACDC/Core/Src/ACDC.cpp` zeigt `PARAMETER_AA` des Patches an, Rot ab `ACDC_CLIPPING_LEVEL` 4090. Der Default-Patch „ACDC“ (`owl-patches/library/ACDC_ACDCPatch.hpp`, Library-Quelle; der Slot-1-Build auf acdc1 ist älter, D1/D2) setzt AA = RMS **nach** dem Regler-Gain (2·Knob)². Rot heißt dort: über −1 dB nach dem Gain.
- **Mit laufendem Rechner-Stream** sind die Regler in `fx1d` praktisch wirkungslos: RX POST_FX überschreibt den Ausgang, TX kommt PRE_FX. Nur die Eingangs-LEDs reagieren noch auf sie, und das führt in die Irre.

**Wunsch des Nutzers:**
- **Ohne Rechner-Stream** bleibt alles wie heute: Regler = Gain, Eingangs-LEDs = Pegel nach dem Regler (Wert des Patches).
- **Wenn der Rechner aufnimmt** (TX-Stream aktiv, `usbd_tx != NULL`), zeigen die Eingangs-LEDs den **rohen Eingangspegel**. Den misst die Firmware selbst (`rx_levels` analog `tx_levels`, auf dem ADC-Puffer `rx` in `audioCallback`). **Rot = echtes ADC-Clipping:** Spitze ≥ ≈ −0,1 dBFS mit kurzer Haltezeit.

Das ist Option B mit Umschaltung. Option A (nur den Patch ändern) geht nicht, weil der Patch den USB-Zustand nicht kennt.

**Offen für die Grill-Runde:**
- Bedingung TX oder RX-Stream
- Clip-Schwelle und Haltezeit
- Skalierung wie `tx_levels` (Quadratmittel × 4096) oder wie der Patch
- Glättung
- Versionsname (z. B. `v22.4.r-fx2`)
- optional: Regler bei aktivem Stream als MIDI-CC an den Host senden [Hypothese; prüfen, ob die Firmware das schon tut]

**Ablauf:** wie Build 2 (`docs/05` „Build 2 neu“):
1. Patch `07-…` in `firmware/patches/`
2. Build mit `tools/build_acdc.sh`
3. Flash nur mit Freigabe
4. Abnahme: A1, A2/A3 (LEDs zeigen den Gain), LED-Test mit Stream (Regler ändern nichts, Clip bei ADC-Vollaussteuerung), A6 kurz, **A/B gegen B3** (2 × 60 s, Neustart der Host-Software dazwischen, Schwelle 0,5 dB). Mehrarbeit im Audio-ISR kann die Mischprodukte verschieben (D24).
5. Danach Commit auf `acdc/fx1d` (README-Abschnitt Routing/LEDs anpassen). Push nur mit Freigabe.

**Nebenbei (Antwort an den Nutzer):** Kalibrierte CV vom Rechner berührt das nicht, der USB-Playback geht am Patch und an den Reglern vorbei. Seit Patch 04 ist der Ausgangspegel aber 125 statt 114. CV-Kalibrierungen von vor Build 1c müssen neu gemacht werden.

## Nachtrag 2: Ergebnis Build 3 (2026-11-15, ≈ 18 Uhr)

- **acdc1 läuft wieder mit Build 2 `v22.4.r-fx1d`** (`7f9f9a34…`, zurückgeflasht ≈ 17:47, A1 bestanden, Log `firmware/flashlog/20261115_build2-fx1d-kontrolle/`).
- Build 3 ist umgesetzt, aber verworfen (messlog D28–D31, `docs/05` „Build 3“):
  - Build 3 `v22.4.r-fx2`: Dauer-Rot, weil die SAI-24-Bit-Wörter kein Vorzeichen tragen.
  - Build 3b `v22.4.r-fx2b`: LEDs funktionieren, aber fs/8 +1,4 dB, Kamm +1,5 dB, Mischprodukte −4,0 dB gegen die Kontrolle mit Build 2 in derselben Sitzung. Kriterium Q9 → Build 2 bleibt.
- Fork `acdc/fx1d` steht bei `b3bd3752` (fx2b-Code + README, gepusht). Das README nennt das A/B-Ergebnis noch nicht (TODO).
- Neue Kontroll-Basislinie: `B3-fx1d-k-r1/-r2` (D31) = B3 auf ≤ 0,2 dB.
- Nächste Möglichkeiten: Build 3c mit weniger Last pro Block, Clip-Test, MIDI-CC der Regler, CV-Anzeige, Lastverteilung als E3-Hebel (alles in `TODO.md` Phase 5).

## Nachtrag 3: Build 3d läuft (2026-11-15, ≈ 18:40)

- **acdc1 läuft mit Build 3d `v22.4.r-fx2d`** (`d212cf8d…`, Log `firmware/flashlog/20261115_build3d-fx2/`). Die LEDs zeigen beim Aufnehmen den rohen Pegel. Nachtrag 2 („Build 2 läuft wieder“) ist damit überholt.
- **Befund des Abends (D32–D34):** Die Lage von Code und Daten im Speicher verschiebt fs/8 (±2 dB), Kamm (±1,5 dB) und Mischprodukte (±4,5 dB), ganz ohne Funktionsänderung (Füll-Build `fx1p`). Darum liegt der neue Code von 3d am Ende von Flash und RAM, alle anderen Adressen sind wie in Build 2.
- **Regel:** Jeder neue Build bekommt eine `nm`-Prüfung der Adressen gegen die Referenz und ein A/B gegen eine Kontrolle in derselben Sitzung.
- **Kamm bei 3d +0,4…0,55 dB** gegen Build 2. Der Nutzer behält 3d trotzdem.
- **Fork:** `acdc/fx1d` steht bei `abc3a72a`, gepusht 2026-11-15. Der temporäre Worktree ist entfernt.
- **Nächste Ideen** (`TODO.md` Phase 5): Lage als Rausch-Hebel durchprobieren, 1b → 1d neu bewerten, Clip-Test, MIDI-CC der Regler, CV-Anzeige.
