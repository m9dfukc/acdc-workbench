# 02 – Noise: Befunde, Hypothesen, Isolator-Frage

## Stand heute (2026-11-27)

Kurzfassung aller Befunde. Zahlen und Aufbau stehen im Messlog (`messlog.md`) unter der genannten ID. Die datierten Abschnitte weiter unten zeigen den Verlauf, je mit dem Stand ihres Datums. **Rauschwerte vor dem 2026-11-24 gelten ohne Masse-Draht und sind mit neuen nicht direkt vergleichbar.**

**Störfamilien** in den ADC-Daten, auf allen Kanälen stark korreliert:

- **SOF-Kamm** bei k·≈1 kHz
- **fs/8** = 6000,00 Hz (Audio-Blockrate bei Blockgröße 8, sample-synchron)
- **Mischprodukte** n·f1k + m·6000 Hz
- **LED-PWM** 2320,98 Hz auf acdc2, 2320,54 Hz auf acdc1 mit der Werks-Firmware. Seit fx7a läuft die PWM mit 48 kHz, die Linie ist an Ein- und Ausgängen weg [gemessen, D78]
- **Regler-Linien** und **Linien aus Takten der MCU**, beide schwach (siehe unten)

**Was die Familien senkt:**

- **Masse zwischen Modul und Träger ist ein Hauptweg der Störungen [gemessen, D90].** Auf dem Xibeca-Modul verbindet nur die Ferritperle L1 AGND (Codec) und GND, der Träger legt alle AGND-Pins direkt auf seine Masse [Code: Schaltplan]. Der Draht Pin 15 ↔ Pin 33 senkt fs/8 um 18 dB, den Kamm um 7 dB, den Rest um 3 dB und die LED-Verschiebung auf ein Viertel. Am Ausgang sinken der Kamm um 11 dB und fs/8 um 12 dB [gemessen, D91]. Nicht bewegt: 7384,62 / 1215,19 / 4401,90 Hz. Die Scan-Linie 9633,80 Hz steigt um 3,7 dB (−120 Datei-dBFS). Der Kamm trägt danach 30–50 % der Rauschleistung, eine ideale Notch-Bank brächte nur noch 1,6–3 dB. Anleitung: `06-hardware-mod-masse.md`.
- **Heißer Pfad im ITCM [gemessen, D48, gilt auch für fx4b, D58]:** gegen 3d fs/8 −5,1 dB, Mischprodukte −35 dB, Rest −1,25 dB, RMS −1,1 dB, Kamm +0,2…+0,4 dB. Liegt der heiße Pfad im ITCM, zählt die Flash-Lage des übrigen Codes nicht mehr (fx3lp ≤ 0,25 dB bei fx3l).
- **Den Kamm senkt in der Firmware nur USB-Code im ITCM [gemessen, D42/D44]:** USB im Flash +2,5…+3,5 dB gegen 3d, im ITCM ±0.
- **fx8a gegen die Original-Firmware in einer Sitzung [gemessen, D86]:** RMS −1,8 dB, Rest −3,2 dB, fs/8 −5,2 dB, Mischprodukte −22,6 dB, Kamm gleich. LED-PWM-Linie und eine Familie bei 75,72 Hz zeigt nur das Original. Das Original nimmt nach dem VCA des Default-Patches auf, korrigiert über den DC-Offset der offenen Eingänge (`tools/family_table.py --dc-ref/--dc-correct`, Verfahren aus D26). fx9a liegt gegen fx8a bei fs/8 −0,7 dB und zeigt keine neue Linie (D89).

**Woher die Familien kommen:**

- **Der Kamm hängt am USB-SOF des Host-Controllers [gemessen, S2-6].** f0 hängt vom Anschluss ab: Mac-Port 999,99 Hz, TB-Hub 999,868 oder 999,997 Hz je Port (im acdc1-Takt). Ein Notch-Filter müsste f0 je Modul und Anschluss messen.
- **Am Ausgang ist der Kamm ohne USB weg und schon ohne Stream da [gemessen, D20].** Standalone ist der Ausgang sauber.
- **Die Lage des Codes im Speicher verschiebt die Störlinien [gemessen, D33].** Ein reiner Füll-Build ohne Funktionsänderung ändert fs/8, Kamm und Mischprodukte um 1,5–4,5 dB.
- **Was die CPU im Blocktakt tut, erscheint bei fs/8 [gemessen, D42]:** Ein paar µs Abfrage eines DMA-Registers pro Block heben fs/8 um ≈ 10,6 dB. Mechanismus [Hypothese]: Busverkehr bzw. Strompuls.
- **Auch die Rechenlast eines Patches hebt fs/8 [gemessen, D69]:** Schliere (29 % CPU) gegen den Default-Patch (6 %) in derselben Sitzung: fs/8 +3,8 dB, Mischprodukte +13,4 dB, Rest und Kamm ±0,25 dB. Ein FX-Patch reicht diese Linien samt Kamm an die Ausgänge durch, ohne Eingangssignal sind sie das, was man hört (D68). Die Sperre `owl/include/AcdcInput.h` zieht die Blockraten-Linien am Eingang ab: am Ausgang −22…−25 dB (D70, D71).
- **Masseschleife [gemessen, D21]:** nur mit AC/DC am Mac-Port und UMC am Hub (+20 dB). Beide am Hub → weg. Kein Isolator nötig. Die Alltags-Kette ist für Aufnahmen in Ordnung (D22/D23).
- **Einbau ins Case [gemessen, D69]:** in den ADC-Daten keine Verschlechterung gegen „neben dem Case“ (Rest −0,1 dB, fs/8 −0,2 dB, Kamm +0,65 dB bei zwei Stunden Abstand). Die Ausgänge sind dazu nicht gemessen.

**LEDs:**

- **Am Ausgang bewiesen [gemessen, D67]:** Ein Patch, der LEDs gedimmt leuchten lässt, bringt 2321 Hz mit Vielfachen auf den Ausgang, der Pegel folgt dem LED-Muster um bis zu 27 dB. Bei „Rot“ lässt die Firmware Grün mit Tastgrad 1023/1024 weiterlaufen und setzt den roten Pin alle 2 ms neu [Code], am Ausgang ist davon nichts messbar [gemessen, D72].
- **Jeder Wechsel einer LED verschiebt den Ausgang [gemessen, D73]:** Dauerhaft rote LEDs stören nicht, aber jedes Ein- oder Ausschalten gibt einen Knack (je LED etwa das 6-Fache des Rauschens im Bass, additiv), Blinken mit 40 Hz hebt den Gesamtpegel um 17,6 dB. Patches sollten LEDs deshalb selten und nie flackernd schalten und nie dauerhaft dimmen. Mess-Patch: `owl/test/SchliereLedTestPatch.hpp`.
- **Der LED-Strom verschiebt den Nullpunkt aller Eingänge [gemessen, D74]:** je leuchtender Eingangs-LED −2,9e-4 Vollausschlag (≈ −2,9 mV, −71 dBFS), an In 1–3 gleich, vom Patch selbst an den rohen Eingängen gemessen (`owl/test/SchliereLedPathPatch.hpp`). Direkt am Ausgang kommen bei digital stummem Ausgang etwa 0,15 mV je LED dazu. Die PWM-Linie ist derselbe Effekt, 2321-mal pro Sekunde geschaltet. Folge [Hypothese]: Die Pegel-LEDs der Firmware bewegen den Nullpunkt der Aufnahme im Takt der Hüllkurve. Der LED-Modus aus (ab fx6a) senkt die Verschiebung auf 1,7 % (D75), der Masse-Draht auf ein Viertel (D90).

**Regler und MCU-Takte:**

- **Ungleich gestellte Regler heben eigene Linien an [gemessen, D58, D60, D61]:** 2200,95 / 4401,90 / 6602,85 Hz und 8549,33 Hz, an den Gerätetakt gekoppelt, unabhängig von der Firmware (fx3l = fx4b).
  - **Es zählt der Unterschied zwischen den Reglern, nicht der Anschlag [gemessen, D61].** Alle vier am selben Anschlag liegen wie 12 Uhr (−114…−119 dB). Ein Regler allein am Anschlag bringt ≈ −100 dB, abwechselnd links und rechts (LRLR) −94 dB. Der Pegel wächst stetig mit dem Abstand.
  - Das Muster bestimmt die Linie: LLRR hebt 2200,95 und 6602,85 Hz, LRLR hebt 4401,90 Hz. Auf 12 Uhr bleiben sie 6…16 dB über dem Grundrauschen, weg sind sie nie.
  - [Hypothese] Der Abtastkondensator des Regler-ADC wird von Kanal zu Kanal umgeladen. Die Quelle der Frequenz 2200,95 Hz ist offen: Die ADC-Scanrate faltet auf 9633,80 Hz, die LED-PWM lag bei 2320,54 Hz.
  - Ein FX-Patch reicht sie an den Ausgang durch [gemessen, D72]: Schliere mit Regler 3 am Linksanschlag −66…−73 dBFS am UMC, so stark wie die stärksten Kamm-Linien, in der Mitte des Regelwegs im Rauschen.
  - Rauschmessungen deshalb immer mit allen Reglern auf 12 Uhr.
- **Linien aus Takten der MCU [Code, gemessen, D60]:** Die Scanrate des Regler-ADC von 105 633,8 Hz faltet auf 9633,80 und 19 267,6 Hz (acdc2: 9653,46 Hz), −116…−129 dB, fast unabhängig von den Reglern. [Hypothese] 2000,0002 und 3000,0003 Hz sind Vielfache des 1-kHz-Systemtakts.

**Sonst:**

- Der Gain-Knob ist im Default-Patch ein **digitaler** Gain [belegt]. Mit `TX_PRE_FX` (acdc1) wirkt er nicht mehr auf die Aufnahme.
- Das Rauschen driftet innerhalb einer Sitzung um 0,4 bis 2 dB (D44, D77). Vergleiche zwischen Builds brauchen deshalb eine Kontrolle am Anfang und am Ende.
- Gewinn einer idealen Notch-Bank: 4–10 dB mit dem Default-Patch (M1/M2, Serie 2, beide Module), bei fx3l ≈ 5,8 dB (D48), mit Masse-Draht 1,6–3 dB (D90). Der Filter im Rechner ist deshalb gestrichen (`04-software-filter.md`).
- **Offen:** Hörprobe mit Kompressor am heutigen Stand, Quelle der Regler-Linien, weitere Massepins. Alles in `TODO.md`.

## Was im Forum bekannt ist [belegt]

**Thread #2072 „Clock noise in AC/DC“** ist die einzige Quelle mit Messungen.

- **atau** (2023-03 bis 06):
  - Setup: 2020er MacBook Pro, macOS 10.15, eine DAW, 48 kHz, FW v22.5.0, offene Eingänge.
  - Rauschbild: **Kamm bei k·1 kHz**, ca. **−30 dB bei Gain 12 Uhr**, bis −18 dB bei vollem Gain.
  - Tritt auf **zwei Geräten** auf (SN 191 und 250).
  - **Kein Effekt** hatten: USB-Optoisolator, andere Skiffs und Netzteile, mechanische Isolation, Laptop im Akkubetrieb.
  - Ein ES-8 ist im selben Setup sauber.
  - Der Bypass-Patch (umgeht die Gain-Regler) ändert nichts. Die Störung steckt also schon in den ADC-Daten.
- **mars (Martin Klang):** Die Pegel seien „definitely not normal“. Er kündigte Messgraphen an, die nie kamen.
- **antisvin:**
  - Er kann den 1-kHz-Kamm reproduzieren, bei ihm leiser.
  - Zusätzlich hört er ein Geräusch mit ca. 0,8 s Periode, evtl. von den LEDs.
  - Ein Block- oder Pot-Artefakt läge bei **3 kHz** (48 kHz / 16 Samples), nicht bei 1 kHz.
- **Pauper** (2023-11-01, letzter Post): „With a cheap ground isolator the noise desapears.“ Mehr steht dort nicht. Kein Modell, kein Hinweis, ob USB- oder Audio-Isolator, und keine Angabe, ob das Streaming danach noch lief.

**Weitere AC/DC-Meldungen:**
- selex (2022-11): sehr hoher Noise-Floor.
- ich (2024-11, Thread #2244): zwei Geräte ungenutzt wegen Noise-Floor.
- antisvin dazu (2024-11): ein Hardwareproblem, das „would require redesign to fix“. Updates von Rebel erwartet er keine mehr.

**Geschwistergeräte** (dieselbe Firma, andere Ursachen):
- Wizard: Masseschleife, ein Olimex USB-ISO hat geholfen (#1104).
- Magus: 60-Hz-Brumm bei USB-Speisung (#1511). Die LEDs abzuschalten hat Rauschen beseitigt (#1703).
- OWL-Pedal: USB-Speisung rauscht, ein externes Netzteil ist besser.

## Hypothesen zur Ursache

| # | Hypothese | Erwartete Signatur | Test | Status |
|---|---|---|---|---|
| H1 | **USB-Full-Speed-Frame-Takt (1 ms)** koppelt auf der Platine in die Codec-Eingänge (Paket-Stromspitzen, Ground Bounce) | Linien bei k·1 kHz, nur bei **aktivem USB-Stream** | Messplan Schritt 6 (Standalone-Gegenprobe) | **[gemessen]** S2-6 (f0 folgt dem Host-Controller) und S3/D20: am Ausgang ohne USB weg, **schon ohne Stream da** (SOF allein reicht) |
| H2 | Klassische Masseschleife zum Host oder über Audiokabel | 50/100/150 Hz + Obertöne, evtl. Schaltnetzteil-Pfeifen. Ändert sich mit Akku/Isolator/Ground-Lift | Schritte 4 und 5 | **[gemessen] D20/D21:** Masseschleife nur, wenn AC/DC am Mac-Port und Ausgang → zweites Interface (UMC) am Hub. +20 dB, 59,98-Hz-Impulse (Monitor am Hub), Fremdkamm 1000,03 Hz. Beide Geräte am selben Hub → weg. Im Alltag (kein AC/DC-Out → UMC) nicht relevant |
| H3 | LED-PWM ≈ 2,32 kHz | Linien bei ≈2,32 kHz und Vielfachen, **pegelabhängig** | Patch, der alle LED-Parameter auf 0 setzt | **[gemessen]** Linie und Pegelabhängigkeit (M1–M3). Am Ausgang bewiesen mit einem Patch, der LEDs dimmt (D67). Der LED-Strom verschiebt den Nullpunkt der Eingänge (D74), die PWM-Linie ist derselbe Effekt. Im LED-Modus aus sinkt die Verschiebung auf 1,7 % (D75), mit der PWM bei 48 kHz ist die Linie weg (fx7a, D78) |
| H4 | Clock/SAI-Flanken (OutputDrive an, 8 TDM-Slots) | Breitbandiger Anstieg oder Linien bei Taktteilern | nur per Firmware-Experiment | [Hypothese], ungetestet. Beide Geräte laufen mit OutputDrive aus und 4 Slots (Hack-Branch) [Code]. Die sample-synchrone fs/8-Linie gehört zu H7 |
| H5 | USB-TX-Ratenregelung (shmuga-Bug, siehe 05) | **Klick-Bursts** alle paar Sekunden in der Aufnahme, kein stationärer Ton | Klick-Detektion im Messplan | **[gemessen] für den Hack-Branch: nicht vorhanden.** 0 Klicks in 360 s (Serie 2), in 10 min mit der Werks-Firmware (D6, D7) und mit Build 2 (D27). Der shmuga-Fehler betrifft den USB-Pfad von v22.5.0, dort ungeprüft. Gefunden wurde stattdessen ein Fehler im Playback: Block-Slips durch Feedback-Drift (D12–D18, behoben mit Patch 06) |
| H6 | Analoge Gain-Struktur, hoher Gain auf Line-Signal | Breitbandiges Rauschen, skaliert mit dem Knob | Gain-Serie | [Hypothese]. Der Knob ist im Default-Patch ein digitaler Gain [belegt], die Gain-Serie sagt deshalb nichts über eine analoge Stufe |
| H7 | Zwei periodische Digitalaktivitäten koppeln in die ADC-Daten und wirken zusammen: Audio-Blockverarbeitung (fs/8) und SOF-Takt | Linie bei fs/Blockgröße, Mischprodukte n·f1k + m·fs/8, Musterperiode 1/(6·f1k − 6000) | Musterperiode vorhersagen, Code-Lage und Blocktakt-Aktivität ändern | **[gemessen]** Serie 2 (Periode getroffen), D33 (Lage im Speicher verschiebt alle drei Familien), D42 (Aktivität im Blocktakt hebt fs/8 um ≈ 10,6 dB), D48 (heißer Pfad im ITCM: fs/8 −5,1 dB, Mischprodukte −35 dB). Der physikalische Weg (Strom, Masse, Bus) bleibt [Hypothese] |

Ausgeschlossen: Die 16-Bit-Trunkierung allein, denn sie liegt bei ca. −96 dBFS, weit unter −30 dB.

## Eigene Messungen M1–M3 (2026-11-13) → Stand der Hypothesen

Dieser Abschnitt zeigt den Stand nach den ersten Messungen. Der aktuelle Status jeder Hypothese steht in der Tabelle oben.

Details, Tabellen und Einschränkungen: `messlog.md`. Kurz: Ich habe den 1-kHz-Kamm, aber **viel leiser als atau** (−80…−96 dBFS bei Gain 12 statt −30 dB).

| # | Was die Messung sagt | Status |
|---|---|---|
| H1 | 1-kHz-Kamm vorhanden, f0 = **1000,053 Hz**, also **nicht** sample-synchron. Passt zu einem Takt außerhalb des Codecs (USB-SOF oder geräteinterner Timer). Ob nur bei aktivem Stream: noch nicht getestet | Kamm [gemessen], Ursache weiter [Hypothese] |
| H2 | 50 Hz nur schwach (−95 dBFS bei g12). Keine ausgeprägte 50-Hz-Familie | eher nicht dominant [gemessen, vorläufig] |
| H3 | Linie bei **2320,98 Hz** + 4641,95 Hz. Ohne Signal bei g12 weg (−110 dB), mit Signal oder hohem DC-Offset −75…−80 dBFS. Frequenz und Pegelabhängigkeit passen zur LED-PWM | **gestützt** [gemessen], Beweis per LED-aus-Patch fehlt |
| H4 | **Linie bei exakt 6000,00 Hz = fs/8** (+12/18 kHz), auf allen Kanälen gleich stark, sample-synchron. acdc2 läuft mit v22.4.q, dort ist `AUDIO_BLOCK_SIZE 8` → Audio-Callback mit 6 kHz [Code]. Dazu **Mischprodukte n·f1k + m·6 kHz** → 1-kHz- und 6-kHz-Störer wirken nichtlinear zusammen, Musterperiode ≈ 3,16 s | Linien [gemessen], Blockrate als Ursache sehr plausibel |
| H5 | In 7–10 s keine Klicks sichtbar. Für eine Aussage zu kurz | offen |
| H6 | Breitbandiger Rest (ohne Kamm/LED) −84 dBFS bei g12. Steigt mit dem digitalen Gain | [gemessen], erwartbar |

**Korrektur zur Deutung von M2:** Der Gain-Knob ist im Default-Patch ein **digitaler** Gain [belegt, siehe `research/notes/forum_noise_reports.md`]. Dass die Störlinien stärker steigen als der Rauschboden, beweist daher **nicht**, dass sie vor einer analogen Gain-Stufe einkoppeln. Es zeigt nur, dass sie in den ADC-Daten stecken. Der 16-Bit-Boden nach dem Patch steigt nicht mit. Dass Kamm (+14…26 dB) und LED-Linie (+30 dB) **stärker** steigen als DC und 50 Hz (≈ +9 dB), deutet auf eine pegelabhängige Kopplung hin [Hypothese].

**Serie 2 (S2-1…S2-4), Kurzfassung, Details in `messlog.md`:**
- H7 (Mischprodukte) **[gemessen]**: Die Musterperiode wurde vorhergesagt und getroffen, acdc2 3,16 → 3,13 s, acdc1 1,247 → 1,24 s.
- **H1 [gemessen, S2-6]:** Der Kamm hängt am **USB-SOF des Host-Controllers**. Beim Wechsel Thunderbolt-Hub → Mac-Port wanderte er um +124,5 ppm (999,8663 → 999,9908 Hz), der Gerätetakt blieb gleich. Ohne USB-Verbindung verschwindet er am Ausgang ganz (S3, D20).
- Direkt am Mac kommt eine neue Brummfamilie bei 119,944 Hz hinzu. Der Hub ist insgesamt etwas ruhiger.
- Bei Gain 0 ist der USB-Strom digital stumm → Nach dem Patch kommt keine Störung hinzu, alles steckt in den ADC-Daten.
- acdc1 hat dasselbe Linienbild (6 kHz → Blockgröße 8), aber exakt 48 kHz statt 47 991 Hz. Grund: Die Werks-Firmware von acdc1 hatte den Takt von v22.4.r [gemessen: Disassembly, D10].
- H5 (Klicks): in 360 s Aufnahme kein Klick.

**Neuer Mechanismus (H7) [gemessen über die Musterperiode]:** Zwei periodische Digitalaktivitäten koppeln in die ADC-Daten: die Audio-Blockverarbeitung (fs/Blockgröße) und ein ≈1-kHz-Takt aus einer anderen Taktdomäne (vermutlich USB-SOF). Wo beide zusammenfallen, entsteht zusätzliche Störung. Folgen:
- Die Blockgröße bestimmt die sample-synchronen Linien. Ein Wechsel auf Blockgröße 16 (v22.5.0) würde das Linienbild ändern. Beide Geräte laufen mit Blockgröße 8, der Test steht aus (E3 in `05`).
- Die Musterperiode hängt vom Taktversatz Host ↔ Gerät ab. antisvins „0,8 s“ passt rechnerisch dazu.
- Bei reinem Standalone-Betrieb (kein USB) müsste der 1-kHz-Anteil samt Mischprodukten verschwinden, die 6-kHz-Linie aber bleiben. **Bestätigt [gemessen, D20]:** Am Ausgang bleiben ohne USB nur fs/8 und ein schwacher fs/48-Kamm.

**Folge für die Lösung:** Eine Notch-Bank auf k·1000,05 Hz + k·2321 Hz entfernt bei Gain 12 ≈ 4–5 dB, bei vollem Gain ≈ 10 dB Rauschleistung [gemessen, Rechnung auf M1/M2]. Der Rest ist breitbandig.

## USB-Isolator: bringt das was?

**Stand 2026-11-15 [gemessen, messlog D21–D23]:** Für den eigenen Aufbau ist kein Isolator nötig. Die einzige gemessene Masseschleife (AC/DC am Mac-Port, Ausgang in den UMC am Hub) verschwindet, wenn beide Geräte am selben Hub hängen. Die Alltags-Kette (passiver Hub → Monitor-Hub → TB-Hub) ist an Ausgang und Eingängen so sauber wie der TB-Hub direkt. Den SOF-Kamm an den Eingängen beseitigt ein Isolator ohnehin nicht (atau).

**Kurz:** Ein billiger Test, aber wahrscheinlich nicht die Lösung, wenn ich denselben 1-kHz-Kamm habe wie atau. Bei ihm hat der Isolator nichts geändert. Er hilft nur bei H2.

Die Schritte 4 (Akku) und 5 (Ground-Lift) aus dem Messplan sind entfallen, ein Kauf steht nicht an. Modelle und ihre Eignung für Full Speed stehen in `research/notes/general_ground_loop_filtering.md`.

## Weitere Hardware-Maßnahmen (falls H2)

- Laptop im Akkubetrieb, keine weiteren Kabel am Rechner (HDMI, Hubs).
- Case und Rechner an derselben Steckdosenleiste.
- Audioseite: DI-Box mit Ground-Lift oder Übertrager (ART DTI, Happy Nerding Isolator, Joranalogue Transmit 2).
- Ferrite, anderes USB-Kabel, direkter Port statt USB-C-Hub.
- **Nie** den Schutzleiter abklemmen.

## Stand 2026-11-15: Ausgänge, USB-Zustände, Masse (messlog D19–D23)

- **SOF-Kamm am Ausgang [gemessen, D20]:** Er ist ohne USB weg und schon bei gestecktem USB ohne Stream da. Im Standalone-Betrieb bleiben am Ausgang nur die fs/8-Linie (über die Durchleitung vom Eingang), ein schwacher Kamm **genau bei fs/48 = 1000,000 Hz im Gerätetakt** (−105…−111 dB, **[Hypothese]** firmware-interne 1-ms-Aktivität) und Netz 50 Hz.
- **Masse [gemessen, D21]:** siehe H2. Der TB-Hub versorgt den Mac. Mac-Port und Hub-Ports liegen deshalb auf verschiedenem Massepotential **[Hypothese]**.
- **SOF-Frequenz je Anschluss [gemessen]:** Mac-Port 999,99 Hz, TB-Hub 999,868 Hz (A5, Monitor-Hub-Kette) **oder** 999,997 Hz (anderer Port, G5), jeweils im acdc1-Takt. Ein Notch-Filter muss f0 je Anschluss messen.
- **Offene Eingänge streuen [gemessen, D22/D23]:** Ein einzelner Ausreißer brachte +10 dB breitbandig und tieffrequent, 10 min später war er weg. Messungen mit offenen Eingängen deshalb doppelt aufnehmen.
- **Mischprodukte in A5-b1d +4,7 dB gegen A5-b1b [gemessen, D19]:** Es ist die Firmware, nicht die Sitzung (D24: 2 × A5 mit 1d auf ≤ 0,1 dB gleich). Ob Patch 05/06 selbst oder nur die verschobene Code-Lage (D33), ist nicht getrennt. Mit fx3l spielt es keine Rolle mehr.

## Stand 2026-11-16: Lage im Speicher, ITCM, fx3l (messlog D24–D49)

Alle Werte an acdc1, rohe Eingänge (`TX_PRE_FX`), offen, Alltags-Kette, Datei-dBFS, Mittel über 4 Kanäle.

- **Die Lage von Code und Daten im Speicher verschiebt die Störlinien [gemessen, D33].** Ein Füll-Build ohne Funktionsänderung (+0x150 B) hebt fs/8 um 1,8 dB und den Kamm um 1,5 dB und senkt die Mischprodukte um 4,5 dB. A/B zwischen zwei Builds misst deshalb Code **und** Lage.
- **Heißer Pfad im ITCM [gemessen, D37, D48]:** fs/8 sinkt um ≈ 5 dB, die CPU-Last mit Stream halbiert sich (15 % → 6–8 %). Die Flash-Lage des übrigen Codes zählt dann nicht mehr (Füllvariante fx3lp ≤ 0,25 dB bei fx3l).
- **Was die CPU im Blocktakt tut, erscheint bei fs/8 [gemessen, D42].** Eine Abfrage-Schleife von ein paar µs auf ein DMA-Register pro Block hebt fs/8 um ≈ 10,6 dB. Der Blockstart aus dem RX- statt aus dem TX-Interrupt kostet dagegen nichts (D44). **[Hypothese]** Busverkehr bzw. Strompuls im Blocktakt koppelt in die ADC-Daten.
- **Der Kamm hängt an der Lage des USB-Codes [gemessen, D42, D44, D48].** USB-Code im Flash bei sonst gleichem ITCM-Stand: +2,5…+3,5 dB gegen 3d. USB-Code im ITCM: ±0…+0,4 dB. Unter den Stand von 3d ist der Kamm mit keinem Build gefallen.
- **Die Mischprodukte folgen nicht einfach den Pegeln von fs/8 und Kamm [gemessen, D42, D44].** In fx3j sind beide lauter und die Mischprodukte 10 dB leiser. **[Hypothese]** Die Phasenlage zwischen Blocktakt und SOF entscheidet.
- **fx3l gegen 3d [gemessen, D48]:**

  | Größe | fx3l | Δ gegen 3d |
  |---|---|---|
  | RMS ≥ 20 Hz | −72,7 | −1,1 dB |
  | Rest ohne Störlinien | −78,5 | −1,25 dB |
  | Kamm (SOF) | −74,6 | +0,2…+0,4 dB |
  | fs/8 | −83,4 | −5,1 dB |
  | Mischprodukte | −119…−120 | −34,8 dB |

- **Folge:** Der SOF-Kamm ist jetzt mit Abstand die stärkste Störfamilie und liegt ≈ 4 dB über dem breitbandigen Rest. Die Firmware hat ihn nicht gesenkt. Eine ideale Notch-Bank brächte bei fx3l ≈ 5,8 dB (RMS −72,7 gegen Rest −78,5 dBFS). Weil der Rechner die rohen Eingänge aufnimmt, müsste sie im Rechner laufen. Ob sich das lohnt, ist offen (optional, siehe `04-software-filter.md`).
- **Offen:** Hörprobe mit Kompressor, zweite Rauschsitzung mit 3d-Startkontrolle (D48 hatte keine), Linien bei k·fs/48 (2000/3000 Hz), die fx3j, noD und fx3k zeigten (D42, D44) und für fx3l nicht ausgewertet sind. Alles in `TODO.md`.

## Stand 2026-11-24: Masse-Brücke auf dem Modul (messlog D90)

- **Draht Pin 15 (GND) ↔ Pin 33 (AGND) auf der Rückseite des Xibeca-Moduls [gemessen, D90]:** acdc1, fx9a, offene Eingänge, je 2 × 60 s am selben Tag. RMS −5,7 dB, Rest −2,9 dB, Kamm −7,2 dB, fs/8 −18,3 dB, Mischprodukte unter der Erkennung, LED-Verschiebung der Eingänge auf 20–25 %. Verstärkung unverändert (Loop-Test +0,02 dB). Anleitung und Hintergrund: `06-hardware-mod-masse.md`.
- **Mechanismus [Hypothese]:** Rückstrom des Moduls floss über L1 und die AGND-Fläche zum Träger. Die Spannung darüber lag zwischen dem Bezug des Codecs (AGND) und dem der Eingangsstufe (Träger-GND). Alle Familien, die aus Strompulsen des Moduls stammen, sinken gemeinsam. Das stützt die Hypothesen aus D42 (Strompuls im Blocktakt) und D74 (LED-Strom verschiebt den Nullpunkt): Der Kopplungsweg ist zum großen Teil die Masse zwischen Modul und Träger.
- **Nicht bewegt:** 7384,62 und 1215,19 Hz, die Regler-Linie 4401,90 Hz. Die Scan-Linie des Regler-ADC (9633,80 Hz) steigt um 3,7 dB, bleibt aber bei −120 Datei-dBFS.
- **Folge:** Der Kamm trägt jetzt 30–50 % der Rauschleistung, fs/8 unter 1,5 %. Eine ideale Notch-Bank brächte nur noch 1,6–3,0 dB. Die Sperre `owl/include/AcdcInput.h` bleibt ohne Änderung brauchbar, ihr Nutzen ist kleiner.
- **Ausgang [gemessen, D91]:** über den UMC gegen D74 ohne Draht Kamm −11 dB, fs/8 −12 dB, LED-Blinken −12,6 dB.
- **Offen:** Hörprobe, ob weitere Massepins (16 ↔ 47/48) oder ein direkter Kurzschluss von L1 noch mehr bringen. Das A-B-A an acdc1 entfällt (Ablöten zu aufwendig), stattdessen später acdc2 mit Messung vorher und nachher.
