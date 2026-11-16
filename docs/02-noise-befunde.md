# 02 – Noise: Befunde, Hypothesen, Isolator-Frage

## Was im Forum bekannt ist [belegt]

**Thread #2072 „Clock noise in AC/DC“** ist die einzige Quelle mit Messungen.

- **atau** (2023-03 bis 06):
  - Setup: 2020er MacBook Pro, macOS 10.15, Logic, 48 kHz, FW v22.5.0, offene Eingänge.
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
| H3 | LED-PWM ≈ 2,32 kHz | Linien bei ≈2,32 kHz und Vielfachen, **pegelabhängig** | Patch, der alle LED-Parameter auf 0 setzt | [Hypothese]. Linie und Pegelabhängigkeit [gemessen] (M1–M3), der LED-aus-Test fehlt |
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

Die Schritte 4 (Akku) und 5 (Ground-Lift) aus dem Messplan sind entfallen, ein Kauf steht nicht an. Die Kaufoptionen bleiben zum Nachschlagen:

| Modell | Speed | Preis ca. | Eignung |
|---|---|---|---|
| Generisches ADuM3160-Board | LS/FS | 10–35 € | ✅ reicht für AC/DC (Full Speed). Jumper auf **FS** stellen, nicht LS |
| Hifime ISO2 | FS | 29 $ | ✅ |
| Olimex USB-ISO-HS (TI ISOUSB211) | LS/FS/HS auto | ca. 45 € | ✅ zukunftssicher, auch für HS-Geräte (ES-8/ES-9) |
| Topping HS01 | nur HS | ca. 70 $ | ❌ erkennt keine USB-1.x-/UAC1-Geräte |
| iFi iDefender+ | – | ca. 59 $ | nur Ground-Lift, keine Isolation der Datenleitungen |
| Manikin Modul 2 (Eurorack) | HS | 179 € | zu teuer für einen Test |

Die Stromgrenze der Isolator-Boards ist beim AC/DC kein Problem, weil er aus dem Eurorack-Bus gespeist wird.

Offen: Es gibt keinen Bericht, dass alle 4×4 Kanäle des AC/DC durch einen Isolator streamen. Auch die VBUS-Erkennung an PA9 hinter einem Isolator ist unbestätigt.

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
