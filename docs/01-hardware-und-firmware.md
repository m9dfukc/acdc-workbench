# 01 – Hardware & Firmware des AC/DC

Basis: OpenWare-Quelltext `RebelTechnology/OpenWare` @ `62a0187` (v22.5.0, 2023-03-05), Build-Target `ACDC/` (Plattform „Xibeca“), plus Forum-Aussagen.

**[Code]-Angaben gelten für v22.5.0, wenn nichts anderes dabeisteht.** Die eigenen Builds auf acdc1 stehen auf `db9d3dd` (v22.4.r, Branch `hack/acdc-output-levels`) und weichen in Takt, Blockgröße, Gains und USB-Pfad ab. Was dort gilt, steht im Abschnitt „Eigene Firmware auf acdc1“ am Ende und in `05-firmware-plan.md`.

## Hardware

| Aspekt | Wert | Status |
|---|---|---|
| MCU | STM32H750IB, 480 MHz, FreeRTOS. Build über `Hardware/xibeca.mk` mit `-DSTM32H750xx`, Linker-Skript für 128 KB Flash („Xibeca red“). `ACDC.ioc` nennt STM32H743IIKx (Prototyp) | [Code] |
| Flash-Budget | Release-Binary ≈ 107 KB von 128 KB, also nur ca. **20 KB Luft** für Backports | [Code] |
| Patch-Speicher | QSPI-Flash, bis zu 40 Slots. Boot-Patch = `settings.program_index`, Default Slot 1 | [Code] |
| Codec | TI PCM3168A, SAI1 Block A als Master (erzeugt MCLK), TDM 8 Slots, 24 Bit. Davon werden 4 genutzt, per DMA laufen aber alle 8 | [Code] |
| Codec-HPF | aus (`/* #define CODEC_HP_FILTER */`), absichtlich für DC-Kopplung. Zur Laufzeit per SysEx `HP` aktivierbar, wird aber **nicht gespeichert** | [Code] |
| Samplerate | nominal 48 kHz. PLL3 98,2857 MHz, MCKDIV gerundet auf 8 → **≈ 47 991 Hz (−186 ppm)**. Das gilt für v22.5.0 und v22.4.q (acdc2). Ab v22.4.r im Hack-Branch (PLL3 P/Q 8, FRACN 262) sind es exakt 48 kHz, so läuft acdc1 | [Code], [gemessen] messlog D10 |
| I/O | 4 Eingänge, 4 Ausgänge, ±10 V, DC-gekoppelt | [belegt] |
| Bedienung | 4 Knobs (Input-Gain **und** Patch-Parameter A–D), 8 LEDs (Parameter AA–AD, BA–BD). Keine Taster, kein Gate/CV-Eingang, kein serielles MIDI in der Firmware. Auf der Rückseite sitzt ein 3-poliger Header „MIDI“ (roher UART), der dazu geplante MIDI-Expander erschien nie (Thread #2077). Siehe „MIDI-Header auf der Rückseite“ | [belegt] |
| LEDs | PWM über TIM2/3/4/8, Prescaler 100, Periode 1023 → **≈ 2,32 kHz** (im Audioband). Das Tastverhältnis folgt dem Pegel | [Code] |
| Versorgung | Eurorack-Bus (+12 V, ca. 200 mA). Nicht über USB versorgt | [belegt] |
| Default-Gains | Input 104, Output 114 (v22.5.0). Im Hack-Branch (v22.4.q, v22.4.r): Input 88. Eigene Builds ab 1c: Output 125 (Patch 04). Alles Defaults: Gespeicherte Settings im Flash haben Vorrang | [Code] |
| Firmware acdc1 | Heute **`v22.4.r-fx4b`** (eigener Build, seit 2026-11-17, davor `v22.4.r-fx3l` seit 2026-11-16). Ab Werk meldete das Gerät „v22.5.0“, es war aber ein Build aus `hack/acdc-output-levels` mit diesem Etikett, kein veröffentlichter Commit. Daher Blockgröße 8, die 6-kHz-Linie und der Takt von v22.4.r | [gemessen] messlog D3, D3a, D10, D49, D59 |
| Firmware acdc2 | **v22.4.q** = Commit `e81cfc3` (2022-06-27) aus `hack/acdc-output-levels`, nie gemergt. `AUDIO_BLOCK_SIZE 8` (v22.5.0: 16), `AUDIO_INPUT_GAIN 88`, HPF aus, PLL/LED-Timer wie v22.5.0. Unsere Code-Analyse bezieht sich sonst auf v22.5.0 | [Code], Device-Status 2026-11-13 |

## USB

| Aspekt | Wert | Status |
|---|---|---|
| Speed | **Full Speed** (`USE_USBD_FS`, OTG_FS mit internem PHY, USB-Takt aus HSI48, kein CRS-Trimming konfiguriert) | [Code] |
| Klasse | USB Audio Class **1.0** (`bcdADC 0x0100`) + USB-MIDI | [Code] |
| Format | 4×4 Kanäle, **16 Bit** (24 Bit vom Codec werden ohne Dither abgeschnitten), 48 kHz | [Code] |
| Bandbreite | 4 × 48 000 × 2 B = 384 B pro 1-ms-Frame und Richtung. Passt in Full Speed, ein **ADuM3160-Isolator reicht** | [Code] |
| Sync | Playback async mit explizitem Feedback (EP 0x81), Format 10.14, alle 32 ms (`FB_REFRESH 5`). Upstream bis v22.4.r: **offene Schleife**, gemeldet wird nur der Verbrauch des Codecs, nicht der Pufferstand | [Code] |
| Puffer | `USBD_AUDIO_BUFFER_PACKETS 3` = 576 Samples = 144 Frames = 3 ms (RX). Start in v22.4.r: Füllstand nach dem ersten Paket = halber Puffer, also nur ≈ 24 Frames Reserve bis zum Unterlauf | [Code] |
| Feedback-Drift macOS | Mit offener Schleife liefert macOS im Mittel ≈ 1 LSB zu wenig (1,15–1,7 ppm). Der RX-Puffer läuft alle ≈ 2–3 min um einen Block (8 Frames) leer, hörbar als Klick, und die Loop-Latenz wächst um 8 Samples. Behoben durch Pufferstand-Regelung (eigener Patch 06, Build 1d) | [gemessen] messlog D12, D16, D18 |
| Debug-Meldungen | `usbd_audio_error()` → PROGRAM_MESSAGE `<msg> <rx frei> <tx belegt> <diff>`: `rx unf` (Unterlauf), `rx ovf`, `tx unf`, `tx ovf`; Feedback: `fb <alt> <neu>` (verworfene Messung). Nur die letzte Meldung bleibt, lesbar per `tools/owl_read.py` | [Code] |
| Interrupt-Prioritäten | SAI-DMA (Codec) 5, OTG_FS 6: Der Audio-Interrupt kann USB unterbrechen. Daraus entsteht eine Race in `usbd_audio_get_rx_count()` (Patch 05), die aber nicht die Ursache der Drift war | [Code] |
| Mute/Volume | `Codec::mute()` und die USB-Mute/Volume-Callbacks sind TODO-Stubs ohne Funktion | [Code] |

## Audio-Routing (wichtig für Standalone und Filter)

Relevante Datei: `Source/ProgramManager.cpp`, Funktion `onProgramReady()` (ca. Z. 263–318).

```c
// pre / post fx routing
#if defined USE_USBD_AUDIO_RX and !defined USE_USBD_AUDIO_RX_PRE_FX
#define USE_USBD_AUDIO_RX_POST_FX
#endif
#if defined USE_USBD_AUDIO_TX and !defined USE_USBD_AUDIO_TX_PRE_FX
#define USE_USBD_AUDIO_TX_POST_FX
#endif
```

TX- und RX-Routing sind **unabhängig** voneinander schaltbar (im Quelltext geprüft) [Code].

- **Stock (beides POST_FX):**
  - Nach dem Patch wird der **Patch-Ausgang** an USB TX geschickt, also an den Rechner zur Aufnahme.
  - Danach überschreibt USB RX (DAW-Playback) den DAC.
  - `usbd_rx_convert()` tut nur etwas, solange `usbd_rx != NULL` ist. Das gilt erst ab dem ersten `DataOut`-Paket vom Host. Bei Alt-Setting 0 oder Disconnect wird es wieder `NULL`.
  - **macOS schickt auch dann Playback-Pakete, wenn eine App nur vom AC/DC aufnimmt** (Aufnahmeprogramm, Wiedergabe auf anderem Gerät) [gemessen, messlog D20, S3-c]. Mit Build 1d ist dann die Durchleitung aus, und an den Ausgängen liegt der Host-Playback (meist Stille). „Nur Eingang streamt, Ausgang leitet durch“ gibt es auf dem Mac also nicht.
- **Ohne Host:** `bootstrap()` startet den Patch aus Slot `program_index` und danach den Codec. Es gibt keine USB- oder VBUS-Abhängigkeit, der Takt kommt vom Codec (8-MHz-Quarz) [Code]. antisvin bestätigt, dass der Default-Patch ohne USB läuft (Thread #2083) [belegt].
- **Mit eigener Firmware Build 1d (acdc1) geht die Durchleitung ohne Rechner [gemessen, messlog D11/D17].** Der folgende Punkt beschreibt die alten Firmwares.
- **Alte Firmware: An den Buchsen kommt ohne Rechner-Playback nichts an [gemessen, acdc1 Kaltstart, siehe `messlog.md`].** Der Patch läuft also, ist aber nicht hörbar. Bei acdc2 (v22.4.q) erklärt das der Hack `237c63d`, der ohne USB-Playback Nullen an den DAC schreibt [Code]. Bei acdc1 war es derselbe Hack: Die Werks-Firmware war ein Hack-Branch-Build mit dem Etikett „v22.5.0“, `237c63d` ist darin per Disassembly belegt [gemessen, messlog D3/D3a].
- **Default-Patch „ACDC“** (Martin Klang, Quelle in `owl-patches/library/`): 4-Kanal-VCA, Ausgang = Eingang × (Knob·2)², LEDs = Pegel/Clip. Er leitet also durch [Code].
- **Ohne gespeicherten Patch** bleibt das Gerät im Configure-Modus: Ausgang still, kein USB-Audio. Der USB-Transfer läuft im Per-Block-Hook des Patches [Code].

| Build | Ohne Host | Host streamt |
|---|---|---|
| Stock (Quelltext v22.5.0) | Eingänge → Patch → DAC [Code]. Auf Hardware nie geprüft: Beide Geräte trugen Hack-Branch-Builds mit `237c63d`, dort ist der DAC stumm [gemessen] | DAC = DAW-Playback, Rechner bekommt den **Patch-Ausgang** |
| `TX_PRE_FX` + `RX_PRE_FX` (antisvin, burstMembrane-Fork) | Eingänge → Patch → DAC | Rechner bekommt rohe Eingänge, DAW-Playback geht **in den Patch** |
| **nur `TX_PRE_FX`** | Eingänge → Patch → DAC | Rechner bekommt rohe Eingänge, DAC = DAW-Playback ✅ **Zielverhalten** |

- **Einschränkung bei „nur `TX_PRE_FX`“ (Build 2 `v22.4.r-fx1d`, ebenso 3d und fx3l):** Nimmt eine App vom AC/DC auf, startet macOS auch den Playback-Stream [gemessen, D20]. Dann gilt die rechte Spalte, und die Host-Stille überschreibt den Patch-Ausgang. Der FX ist also nur ohne Rechner-Stream an den Buchsen [Code]. Für Build 2 so hingenommen (`docs/05`, „Build 2 neu“).

Konsequenz für das Rauschen: Mit Stock-Routing (acdc2, Build 1d) landet ein **Filter-Patch in Slot 1 direkt in der USB-Aufnahme**. Mit `TX_PRE_FX` (acdc1 ab Build 2) nimmt der Rechner die rohen Eingänge auf, ein Patch im Gerät erreicht die Aufnahme nicht mehr [gemessen, messlog D25, B2]. Gefiltert wird dann im Rechner. Siehe `04-software-filter.md`.

## MIDI-Header auf der Rückseite

Stand 2026-11-18: nur recherchiert, nichts gebaut und nichts gemessen. Anlass war die Frage, ob ein MIDI-Controller im Standalone-Betrieb Patch-Parameter steuern kann. Quellen, Zitate und Einzelheiten: `research/notes/midi_header_2026-11-18.md`.

| Aspekt | Wert | Status |
|---|---|---|
| Header | 3-polig, beschriftet „MIDI“. **Pin 1 = RX** (Netz `SDA_RX`), **Pin 2 = GND**, **Pin 3 = TX** (Netz `SCL_TX`). Pegel 3,3 V | [belegt] Befaco-Schaltplan |
| Beschaltung | Beide Leitungen gehen direkt auf das Xibeca-Modul (Pin 74 `I2C_SDA`, Pin 73 `I2C_SCL`). Kein Serienwiderstand, kein Schutz, kein Optokoppler, **keine Versorgung** am Header | [belegt] Befaco-Schaltplan |
| MCU-Pins | TX = PB6 (`UART5_TX`). RX laut Code PB5 (`UART5_RX`), der Modul-Pin heißt aber `I2C_SDA`, das passt zu PB7. Welcher Pin wirklich am Header liegt, ist offen | [Code], [Hypothese] |
| Firmware | UART5 ist mit 115200 Baud eingerichtet, aber nicht mit dem MIDI-Code verbunden (`USE_UART_MIDI_RX` fehlt, kein DMA-Kanal). Serielles MIDI braucht einen eigenen Build. Vorlage: `XibecaDevKit` (UART7, 31250 Baud) | [Code], [belegt] Thread #2077 |
| I2C | Der Header taugt elektrisch auch für I2C: Die Netze heißen `SDA_RX`/`SCL_TX`, PB7 ist im Code schon `I2C1_SDA` (Open Drain), der HAL-Treiber wird mitgebaut. Benutzt wird I2C nicht, einen Bus zwischen Modulen kennt OpenWare nicht. MIDI und I2C teilen sich die Pins. Am ii-Bus von monome passen Pinfolge (dort GND, SCL, SDA) und Busspannung (Pull-ups nach 5 V) nicht ohne Weiteres. Audio-Kanäle lassen sich so nicht ergänzen | [belegt] Befaco-Schaltplan, monome-Doku, [Code] |
| MIDI-CC | CC vom USB-Host setzt Patch-Parameter: CC 20–23 = A–D, 24 = E, 1 = F, 12 = G, 13 = H, 75–106 = AA–DH. A–D überschreiben die Regler in jedem Block, AA–AD steuern die Eingangs-LEDs, BA–BD schreibt die Firmware. Per MIDI nutzbar sind also E–H und die erweiterten Parameter ab AE | [Code] |
| USB-Host vorn | Geht nicht: Der Port ist `Device_Only`, die Buchse liefert keine 5 V, der zweite USB-Anschluss des Xibeca-Moduls ist auf der Platine nicht verdrahtet. Ein Host-Stack bräuchte geschätzt 15–25 KB von 22,5 KB freiem Flash | [Code], [belegt] Befaco-Schaltplan, Größe [Hypothese] |

### Zwischenplatine für ein passives MIDI-Breakout (Skizze)

Ein passives Buchsen-Breakout (hier: Expert Sleepers „Tiny MIDI breakout“, 2 HP, 3,5-mm-TRS) erwartet fertige MIDI-Leitungen. Beim ES-9 sitzt die Elektronik dafür auf dem Interface, beim AC/DC fehlt sie. Die Platine dazwischen ist in Lochraster baubar, alle Teile sind bedrahtet, Stromaufnahme unter 15 mA aus +12 V [Hypothese, nicht gebaut].

MIDI In, galvanisch getrennt (Typ A: Spitze = DIN-Pin 5, Ring = DIN-Pin 4):

```
IN-Buchse                           H11L1 (DIP-6)
Ring  (DIN 4) ──[R1 220Ω]──┬─────── 1 Anode     6 Vcc ───┬── +3V3
                           │                             │
                      D1 1N4148                       [R2 1k]
                   (Kathode an Pin 1)                    │
                           │                    4 Out ───┴──[R3 100Ω]── AC/DC Pin 1 (RX)
Spitze (DIN 5) ────────────┴─────── 2 Kathode   5 GND ───── GND
Schirm: offen lassen                3 frei
                                    C1 100 nF direkt zwischen Pin 6 und Pin 5
```

Versorgung aus dem Eurorack-Bus (eigener Stromanschluss auf der Platine):

```
+12V ──[D2 1N4148]──[R4 47Ω]──┬── IN  78L33  OUT ──┬──────┬── +3V3
                          C2 10µF      GND     C3 100nF  C4 10µF
GND ──────────────────────────┴─────────┴──────────┴──────┴── GND ── AC/DC Pin 2
```

MIDI Out, optional (3,3-V-Variante der MIDI-Spezifikation):

```
+3V3 ──[R5 33Ω]───────────────────────────── Ring   (DIN 4)  OUT-Buchse
AC/DC Pin 3 (TX) ──[Inv]──[Inv]──[R6 10Ω]─── Spitze (DIN 5)
GND ──────────────────────────────────────── Schirm
```

- Die zwei Inverter sind ein 74HC14: Pin 14 an +3V3, Pin 7 an GND, 1→2, 3→4, unbenutzte Eingänge 5, 9, 11, 13 an GND, 100 nF an der Versorgung. Der Puffer schützt den MCU-Pin, weil ein TRS-Stecker beim Einstecken kurz Spitze und Ring verbindet.
- H11L1: Optokoppler mit Schmitt-Trigger, läuft ab 3 V, Ausgang mit offenem Kollektor. Strom durch die LED = Ausgang low = Startbit, es braucht also keinen Inverter. Ersatz: 6N138 (andere Pinbelegung, ein Widerstand mehr).
- 78L33 im TO-92. Ersatz: LP2950-3.3 (andere Pinbelegung, Kondensatoren nach Datenblatt).
- Am Breakout hat jede Buchse einen 3-poligen Header: Spitze rechts, Ring Mitte, Schirm links. Obere Buchse = In, darunter = Out. Für Typ B Spitze und Ring tauschen.

Vor dem Bauen zu klären:

- Welcher MCU-Pin an Header-Pin 1 liegt (PB5 oder PB7). Test: Firmware-Build mit UART-MIDI und eine Drahtbrücke von Pin 3 nach Pin 1.
- Ohne Risiko messbar, mit fx4b: Zwischen Pin 3 und Pin 2 sollten ≈ 3,3 V liegen (TX in Ruhe) [Code]. Das bestätigt TX und die Orientierung des Headers.
- UART und DMA sind neue Arbeit für die MCU. Ein Build mit seriellem MIDI braucht den Rausch-Vergleich gegen fx4b (D33, D42).

## Eigene Firmware auf acdc1 (Stand `v22.4.r-fx4b`, 2026-11-17)

Kurzfassung, Begründungen und Messungen in `05-firmware-plan.md` und `messlog.md`.

| Aspekt | Wert | Status |
|---|---|---|
| Basis | `db9d3dd` (v22.4.r) + Libraries `9e8f64e` (altes H7-HAL). Exakt 48 kHz, Blockgröße 8, Input-Gain 88, 4 TDM-Slots, SAI-OutputDrive aus | [Code], Takt [gemessen] D10 |
| Durchleitung | Ohne Rechner-Stream liegt der Patch an den Ausgängen (Revert `237c63d`, Patch 02) | [gemessen] D11, D17 |
| Routing | `TX_PRE_FX`: Rechner bekommt die rohen Eingänge. Produktstring „OWL-ACDC-FX“ (Patch 03) | [gemessen] D25 |
| USB-Feedback | Regelung nach dem Füllstand des RX-Puffers (Patch 06): Ziel 384 Samples, P-Regler, ±32 LSB | [gemessen] D18: 30 min ohne Block-Slips |
| SOF-Auswertung | `USBD_AUDIO_SOF` wertet jede Frame-Nummer nur einmal aus (Patch 14). Mit USB-Code im ITCM lief die SOF-Kette sonst in ≈ 97 % der Frames doppelt | [gemessen] D46, D47 |
| Blockstart | `audioCallback` hängt an den RX-DMA-Callbacks statt am TX-DMA-Interrupt (Patch 12b). Vorher konnte der letzte Eingangs-Sample eines Blocks 16 Frames alt sein | [gemessen] D40, D43 |
| Eingangs-LEDs | Mit TX-Stream roher Pegel (Quadratmittel × 4096, τ 40 ms), Rot 300 ms ab −0,1 dBFS. Gemessen alle 2 ms in `onLoop` auf dem Codec-DMA-Puffer (Patch 07d) | [gemessen] D34, D36 |
| Speicher | Heißer Pfad (104 Funktionen, 12 392 B) und Vektortabelle im ITCM ab 0x3000 (Patch 11g). Patch-Heap im CCM 39,2 KB statt 52 KB | [Code: `check_itcm.py`], [gemessen] D47–D49, D50 |
| Patch-Wahl | Boot-Menü (Patch 15b): Einschalten mit Regler 1, 2, 3 links und Regler 4 rechts. Regler 1 wählt unter den belegten Slots 1–15, Regler 4 bestätigt, Regler 3 oder 30 s brechen ab. Die Eingangs-LEDs zeigen den Slot binär. Der Slot wird als Ressource `ACDC.slot` im Patch-Flash gemerkt und startet beim nächsten Einschalten. Die Settings bleiben unberührt | [gemessen] D52, D53, D55, D57, D58 |
| ADC-Format | SAI1 liefert 24 Bit rechtsbündig **ohne Vorzeichen** (`SAI_DATASIZE_24`). Vor jeder Pegelrechnung das Vorzeichen erweitern | [Code], aufgefallen in D28 |
| Eingangsbereich | Vollausschlag ≈ ±9,5 V, Offset ≈ −0,2…−0,4 V je Kanal | [gemessen] D29 (indirekt), D36 |
