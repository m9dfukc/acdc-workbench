# TODO – AC/DC: Werkbank, Störlinien, Standalone-FX

Hier steht nur, was offen ist. Erledigtes, Entfallenes und beantwortete Fragen stehen in `docs/chronik.md`, Belege im Messlog (`docs/messlog.md`, IDs wie D49).

Stand: 2026-11-27, neu geordnet nach der Inventur. Ein erledigter Punkt wandert mit Datum und Beleg in die Chronik und bleibt hier nicht abgehakt stehen.

Jeder Flash nur nach ausdrücklicher Freigabe. acdc2 bleibt unberührt, bis Punkt 3 freigegeben ist. Settings nur lesen (E4).

## Als Nächstes

1. [ ] **Hörprobe mit Kompressor am heutigen Stand** (fx9a mit Masse-Draht): Aufnahme mit Kompressor auf der Spur. Das war der Anlass des Projekts und ist seit fx3l nicht geprüft
2. [ ] **Slots 2–8 anhören und beurteilen** (Stand der Slots: D94)
   - TapeDelay, Grainz, RingsReverb mit Limiter (D54, D56). Grainz bei Density am Linksanschlag auf Aussetzer prüfen (vor den Caches 78 % CPU, D52)
   - Plateau: RT60 und Freeze, Schwellen der Normalisierung von In 2, Gate-Erkennung an In 4. Kostet das SDRAM messbar, Pre-Delay kürzen oder `PLATEAU_MAX_SIZE` 3,0
   - Tanh3 Fassung 2 (4× Oversampling gegen Aliasing, D56)
   - SchliereS und SchliereL: Breite der Haltezonen am Tap-Regler (geschätzt 15 %), Regelweg des Feedbacks, Pegel der Ausgänge 3/4 (D66). Mit Signal und bewegten Reglern prüfen, die Blockraten-Sperre lernt nur in der Stille
   - Dazu die Linien am Ausgang bei hoher Last nachmessen (SchliereL 59 %): fs/8 und Mischprodukte steigen mit der Last (D69)
3. [ ] **acdc2** (Nutzer 2026-11-24, ersetzt das A-B-A an acdc1). Bis dahin bleibt acdc2 Referenz und unverändert
   - [ ] Nur lesend sichern, mit eigener Freigabe: `tools/owl_read.py` (Slots, Settings, Report) und DFU-Readback des internen Flash. Der Readback schreibt nichts, braucht aber einen Neustart von acdc2 in den DFU-Modus. Von v22.4.q gibt es bisher kein Abbild
   - [ ] Danach neue Firmware und Masse-Draht, dabei alle Messungen vorher und nachher wiederholen (Eingänge, LEDstat, Loop, UMC)
   - Dabei möglich: Regler in Stellung LRLR aufnehmen. Die Verschiebung der Regler-Linie gegen acdc1 ergibt ihre Quellfrequenz (Punkt 5)
4. [ ] **Fehler: Program Change bei offenem Stream bricht die USB-Wiedergabe** (D76, unter fx5a genauso: D77). Danach rund 10 % Stille an allen Ausgängen bis zum nächsten Stream-Start, `fb clamp`. Unabhängig von Patch und Last. Ursache im Code suchen (Audio-Task steht beim Laden, Empfangspuffer und Zähler), eigener Patch, danach die Läufe `B8-fx6a-pc*-stream` wiederholen. Bis dahin: Patch nur ohne offenen Stream wechseln
5. [ ] **Regler-Linien: Quelle und Abhilfe** (D60, D61, D72)
   - Quelle der Frequenzen 2200,95 und 8549,33 Hz finden. 2200,95 Hz steht für einen Durchlauf durch die vier Regler (D61), der ADC-Scan läuft aber mit 105 633,8 Hz und faltet auf 9633,80 Hz (D60). Dazwischen liegen 103 432,86 bzw. 107 834,76 Hz, ein passender Takt ist nicht gefunden. Wege:
     - an acdc2 nur aufnehmen, Regler in Stellung LRLR (siehe Punkt 3, eigene Freigabe, geschrieben wird dabei nichts)
     - Test-Build mit anderer ADC-Abtastzeit: Wandert die Linie mit der Scanrate?
     - Schaltplan: Zuordnung der ADC-Kanäle 10, 11, 14, 3 zu den Reglern, Beschaltung der Schleifer (Kondensator?), Referenz
   - Abhilfe prüfen, wenn die Quelle klar ist (ein ADC-Scan je Audioblock statt freiem Lauf, längere Abtastzeit), je mit A/B. Schlimmster Fall: −94 dB bei LRLR (ohne Draht gemessen, D61)
   - Scan-Linie bei 9633,80 und 19 267,6 Hz (−116…−129 dB, D60, mit Draht +3,7 dB, D90): Abhilfe wäre ein ADC-Start im Blocktakt oder eine Scanrate, die auf ein Vielfaches von 48 kHz fällt. Nur mit A/B, die Linie ist schwach
   - Am Ausgang eines FX-Patches so stark wie die stärksten Kamm-Linien (Schliere mit Regler 3 am Linksanschlag, D72): prüfen, ob die Firmware sie senken kann
6. [ ] **Eigene Patches mit Link plusram neu bauen und speichern**, damit sie von I- und D-Cache profitieren (Tanh3, SchliereS, SchliereL; Library-Patches nur, wenn die Quellen da sind). Slots mit Link patchram (DTCM) sind mit den Caches nicht schneller geworden (D84). Vorher messen, ob der Speicher im AXI reicht, danach die Rechenlast je Patch vergleichen
7. [ ] **Compiler auf Arm GNU 14.3.Rel1 umstellen, zusammen mit dem nächsten Build, der ohnehin eine volle Abnahme braucht** (Probebuild 2026-11-27, `docs/05`, „Probebuild GCC 14.3 und 15.2“). `cand-fx9a-gcc14` baut ohne neue Warnung, `check_itcm` bestanden, Audio-Pfad fast unverändert, `HAL_DMA_IRQHandler` −644 B, Patch-Heap +552 B. Ein Flash nur für den Compiler lohnt den Aufwand der Abnahme nicht. 15.2.Rel1 nicht weiter verfolgen (mehr Code, `codec_ndtr` 20 → 200 B)
   - [ ] Toolchains nach `/Applications/ArmGNUToolchain/` verschieben (Nutzer, braucht sudo). Sie liegen entpackt in `firmware/downloads/toolchains/<version>/arm-none-eabi/`
   - [ ] Beim Umstieg den Standard-`TOOLROOT` in `tools/build_acdc.sh` und `tools/check_itcm.py` ändern, die Toolchain-Zeile in `CLAUDE.md` und `docs/07` nachziehen
8. [ ] **Masse-Draht, weitere Schritte** (D90, `docs/06`)
   - [ ] Weitere Massepins (16 ↔ 47/48) oder L1 direkt überbrücken, je mit A/B
   - [ ] DC-Verschiebung 65–90 mV erklären (zu groß für L1 und Steckerleiste allein)

## Klein

- [ ] Abhängigkeiten von `tools/owl_read.py` festhalten: Python 3.12, `mido`, `python-rtmidi`. `pyproject.toml` verlangt Python ≥ 3.14 und nennt beide Pakete nicht
- [ ] Analyse-Tool: Clipping-Hinweis bei Float-Dateien nur bei flachen Kuppen melden (Fehlalarm in D15)
- [ ] Hörbares Fiepen des Moduls (D79, auch im DFU-Modus, ≈ 800–1000 Hz, leise): Quelle eingrenzen (Modul oder Netzteil, Ohr oder Mikrofon), hören, ob es mit Last, Slot oder Reglern wandert. USB abziehen macht es leiser und höher (Nutzer). [Hypothese] Schaltregler im Pulsbetrieb
- [ ] Kleine Störung auf Kanal 2 während Slot-Downloads (±0,002 Samples Phase, nur im Loop-Lauf mit Downloads gesehen, D63). Eingrenzen: Kanal, Slot, mit und ohne laufenden Patch
- [ ] LED-Strom in den Aufnahmen (D74, mit Draht ein Viertel: D90): Wie stark wandert der Nullpunkt mit den Pegel-LEDs bei Musik? Aufnahme der rohen Eingänge mit einem Burst auf einem Kanal, die anderen offen
- [ ] Antwort im Forum zum Masse-Draht (Hinweisgeber und eigener Thread #2244), falls sie noch aussteht. Nur nach Freigabe

## Bekannte Grenzen

Kein Auftrag, aber gut zu wissen:

- MIDI: Antworten aus dem USB-Interrupt können mitten in ein SysEx der Hauptschleife fallen (verschachtelte Nachrichten, bewusst nicht in Patch 16). Tritt nur auf, wenn der Rechner während eines Downloads anfragt
- MIDI: Patch 16 ändert `usbd_midi.c` (andere Geräte, Bootloader) gleichlautend mit, gebaut und geprüft ist nur das AC/DC
- Ein Program Change bei offenem Stream bricht die Wiedergabe (Punkt 4)

## Offene Fragen

- Linien bei 2000,0002 und 3000,0003 Hz (k·fs/48), die fx3j, noD, fx3k und fx4b zeigen (D42, D44, D60: −104…−108 dB). [Hypothese] Vielfache des 1-kHz-Systemtakts, der in Codec-Zeit bei 1000,0001 Hz liegt. Welcher Takt es ist, im Code nachsehen
- D86: Woher kommt der um 3,2 dB höhere Rest der Original-Firmware (mehr, als die Kette der Einzelvergleiche erwarten lässt), und woher ihre 75,72-Hz-Familie?
- Wandernde Linien am Ausgang: 684,8 Hz mit Oktaven, 942,5 Hz, 281,6 Hz (D72) und 840–930 Hz mit Drift über die Sitzung (D93). Reglerstellung, andere Module im Case oder Messkette?
- Wie entsteht die fs/8-Linie? Was die CPU im Blocktakt tut, erscheint bei fs/8 (D42) [Hypothese: Busverkehr bzw. Strompuls]. Der Masse-Draht senkt sie um 18 dB (D90), der Kopplungsweg ist also zum großen Teil die Masse zwischen Modul und Träger
- Warum hängt der Kamm an der Lage des USB-Codes (ITCM ±0, Flash +2,5…+3,5 dB, D42/D44)?
- Warum läuft die SOF-Kette mit USB im ITCM doppelt (D46)? [Hypothese: Der Handler springt ein, bevor das gelöschte `GINTSTS.SOF` wirkt]

## Ideen, ohne Termin

Je eine Zeile. Einzelheiten stehen im genannten Doc oder in der Notiz.

**Firmware**
- Merge mit v22.5.0 bzw. dem Upstream-`master` (`36eaf1c4`) samt Fixes: eine Portierung, kein Merge. Umfang, Abnahme und Kandidaten-Builds in `docs/05`, „Option A“, und `docs/research/notes/upstream_master_2026-11-16.md`. Heute kämen die Patches 15b bis 21 dazu
- Serielles MIDI oder I2C über den Header hinten (Nutzer 2026-11-18: keine Eile). Stand, Schaltung und Schritte in `docs/01`, „MIDI-Header auf der Rückseite“, und `docs/research/notes/midi_header_2026-11-18.md`
- Rausch-Experimente je Build mit A/B (E3): Blockgröße 16 oder 32 (zur Laufzeit per SysEx `BS` setzbar, nie getestet, verschiebt die Blockraten-Linie, wäre auch ein Ausweg für die Last von Tanh3), Codec-HPF
- ITCM-Folgeideen (Q4 der Grill-Runde 2026-11-16): Jitter 0–2 µs (Daisy), WFI im Idle, gleichmäßige Last im Idle. Je eigener Build mit A/B
- HAL löscht `GINTSTS.SOF` vor dem Callback (überzählige Interrupt-Einsprünge weg), mit A/B
- Auto-Switching des Routings zur Laufzeit statt per Compile-Flag
- Regler bei aktivem Stream als MIDI-CC an den Host senden (Nutzer, Q7), nur wenn es weder Last noch Störlinien bringt. Die Firmware sendet sie heute nur auf Anfrage [Code]
- CV-taugliche Eingangsanzeige (Nutzer), z. B. Grün linear zum Betrag des Gleichanteils. Rot ist reines GPIO ohne PWM, taugt also nicht als Polaritätsanzeige mit Stärke
- Alte Firmware (Readback) disassemblieren: Hat ihr Feedback eine Pufferstand-Korrektur (D16)?
- Prüf-Build aus dem Fork-Branch `acdc/thru-usb-feedback`, SHA mit Build 1d vergleichen (Freigabe)

**Patches**
- Blockraten-Sperre als Hülle für die anderen FX-Patches (`owl/include/AcdcInput.h`, Schalter in `build_owl_patch.sh` wie `LIMIT=1`), danach je Patch gegenmessen. Woher kommt der Rest von −97 dBFS am Ausgang (D71)? Seit dem Masse-Draht ist der Nutzen kleiner (D90)
- Sperre für den USB-Kamm am Ausgang: Er ist nicht sample-synchron, sie müsste f0 nachführen (D71)
- Ein offener Eingang als Bezug, den ein Patch abzieht (D74): Die LED-Verschiebung ist auf allen Eingängen gleich. Kostet Rauschen, träfe aber auch Kamm und Blockrate, soweit sie auf allen Kanälen gleich sind
- Weitere FX-Patches: Mixer/Attenuator, danach Write/Read-Buffer. Steuerung über 4 Knobs und Audio-Rate-Trigger an den Eingängen. Vorlage `burstMembrane/acdc-patches` (`docs/research/notes/forks_update_2026-11-14.md`)
- Plateau: Varianten als Slots (Layout B der Recherche: Tone-Regler, Tuned, Gated mit stummem Eingang im Freeze)
- Tanh3: Rechenlast senken (45 % CPU, D94), z. B. Oversampling nur bei Signal oder ein kürzerer Abwärtsfilter
- Schliere am Gerät nachmessen (D66): Gruppenlaufzeit und Kerben per Loop Out n → In 1, CV-Skalierung an In 2–4, LEDs. Ideen: Abgriffe als Ressource einstellbar, Regler für die Streuung der Koeffizienten (Richtung Diffusion), Hüllkurven-CV statt Tail an Out 4
- FAUST-Patches bauen (`TapeDelay.dsp`, `FaustTapeDelay.dsp`): braucht den FAUST-Compiler und laut antisvin seinen OwlProgram-Branch. OwlProgram-`develop` hat seit 2026-11 eigene Faust-Fixes, vielleicht reicht das [Hypothese] (`docs/research/notes/owlprogram_develop_2026-11-27.md`)
- SDK ganz auf OwlProgram-`develop` umstellen (LibSource-Fixes und schnellere Blockverarbeitung, betrifft vor allem Grainz und TapeDelay)

**Messen und Werkzeuge**
- Ausgänge im Case gegen daneben messen (zweites Interface, gleiche Kette, gleicher Pegel): Streut das Case direkt auf die Ausgänge ein? D69 hat nur die Eingänge
- Nebenbefund D6: Mischprodukte f1±f2 nur innerhalb der Ausgangspaare 1/2 und 3/4 (lauter als die Grundtöne). Test: Sinus nur auf Out 1, nur auf Out 2, dann beide, Pegel notieren (`tools/crosstalk_lines.py`)
- Sprachschalter `--lang en|de` für die Reports der Analyse, Standard deutsch
- Ergebnisse als GitHub-Issue anlegen. Wo (Upstream `RebelTechnology/OpenWare` oder eigenes Repo), ist offen
