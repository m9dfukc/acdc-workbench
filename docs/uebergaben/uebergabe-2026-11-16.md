# Übergabe – Stand 2026-11-16

Für eine neue Session. Ersetzt `uebergabe-2026-11-15-abend.md`. Deren Fallstricke gelten weiter, die wichtigsten stehen unten.

**Zuerst lesen:**
1. `CLAUDE.md`, vor allem „Build 3d“.
2. `TODO.md` Phase 5.
3. `docs/messlog.md` **D28–D34**.
4. `docs/05-firmware-plan.md` Abschnitt „Build 3“.

## Wo wir stehen

- **acdc1 läuft mit Build 3d `v22.4.r-fx2d`:**
  - Datei `firmware/builds/acdc1-build3d-fx2/`, SHA `d212cf8d…`
  - geflasht 2026-11-15 ≈ 18:40, Log `firmware/flashlog/20261115_build3d-fx2/`
  - besteht aus Build 2 und Patch `firmware/patches/07d-input-leds-raw-late-section.patch`
- **Verhalten:**
  - Ohne TX-Stream zeigen die Eingangs-LEDs den Patch-Wert (`PARAMETER_AA`, Pegel nach dem Regler).
  - Mit TX-Stream zeigen sie den rohen Pegel: Quadratmittel × 4096, τ 40 ms, gemessen in `onLoop` auf `codec_rxbuf`. Rot leuchtet 300 ms ab −0,1 dBFS.
  - **Clip-Rot ist noch ungeprüft.**
- **Rauschen gegen Build 2, in derselben Sitzung:**
  - fs/8 und Mischprodukte liegen ≤ 0,05 dB auseinander.
  - Der Kamm liegt +0,4…0,55 dB höher. Das ist an der Schwelle, Drift ist möglich.
  - Der Nutzer behält 3d.
- **acdc2:** unberührt, nie flashen.
- **Rückweg:**
  1. Build 2 `firmware/builds/acdc1-build2-fx1d/` (`7f9f9a34…`)
  2. Build 1d (`f522560e…`)
  3. Readback `backup/acdc1/20261114/flash/acdc1_internal_flash.bin` (`433b3fd3…`)

  Flash-Ablauf steht in `CLAUDE.md`.
- **Fork:** `acdc/fx1d` steht bei `abc3a72a`, gepusht 2026-11-15 (https://github.com/m9dfukc/OpenWare/tree/acdc/fx1d). Das README enthält den Abschnitt „Memory layout matters“. Der Klon `firmware/OpenWare` steht weiter auf `acdc/thru-usb-feedback`.

## Kernbefund D33: Die Speicherlage verschiebt die Störlinien [gemessen]

- **Testaufbau:** Der Füll-Build `fx1p` ist funktional gleich Build 2. Er hat nur 0x150 B ungenutzten Code in `.text.onLoop` und 0x28 B in `.bss.fast_log_table_size`.
- **Ergebnis:**
  - fs/8 +1,8 dB
  - Kamm +1,5 dB
  - Mischprodukte −4,5 dB
- **Folgen:**
  - Damit sind 3b und 3c erklärt, die mit Mehrlast im Audio-Pfad nichts zu tun hatten.
  - Vielleicht kommen auch die +4,8 dB Mischprodukte von 1b → 1d daher.
- **Lösung 3d:**
  - Neuer Code liegt in `.late_text` (Ende des Flash), der Zustand in `.late_bss` (oberste 64 B von RAM_D2, `Hardware/xibeca.ld`).
  - `onLoop` ist ein Stub, der mit Füllbytes auf die alte Größe 0x1d0 gebracht ist.
- **Regel für jeden neuen Build:**
  - Neuen Code ans Ende legen oder die Adressen per `nm` gegen die Referenz prüfen.
  - A/B immer gegen eine Kontrolle in derselben Sitzung messen: 2 × 60 s, Neustart der Host-Software dazwischen, Schwelle ≈ 0,5 dB.
- **Recherche dazu (2026-11-16):** `docs/research/notes/layout_noise_2026-11-16.md` (englisch, mit URLs)
  - **Kein Bericht zu Lage → Rauschen** fand sich, weder in OpenWare (alle Branches, Commit-Messages) noch in Forks, GitHub-Issues/PRs oder im Rebel-Tech-Forum. D33 ist offenbar der erste dokumentierte Fall.
  - **Verwandt, aber mit funktionaler Ursache [belegt]:**
    - Magus: Eine geänderte LED-PWM-Zeitbasis erzeugte einen ≈ 2,9-kHz-Ton und CV-Rauschen. Rückbau in `3c7e2301` (im Klon geprüft), Forum t/1365, t/1628.
    - Witch: LED-PWM koppelt in den Regler ein (t/1831).
    - Lich: Rauschen bei aktivem USB-Host (t/1610).
  - **Nächster Verwandter: Daisy Seed (ebenfalls STM32H750 + externer Codec) [belegt]:**
    - Electrosmith erklärt den Ton bei der Callback-Rate mit dem Stromstoß je Callback, der GND anhebt. Gemessen 10–15 dB über dem Grundrauschen.
    - Abhilfen dort: zufälliger Jitter von 0–2 µs in der Verarbeitung, Callback-Rate über dem Hörbereich, Notch.
    - Quelle: forum.electro-smith.com t/432 #10, t/6028 #7.
  - **ST-Datenblatt DS12556 §6.3.6 [belegt]:** Der Strom hängt von der „program location in memory“ ab. Bei 400 MHz: 71 mA aus ITCM, 105 mA aus Flash mit Cache, 73 mA ohne Cache. Der Schritt „Lage → ADC-Störlinien“ steht aber nirgends, das bleibt unsere **[Hypothese]**, gestützt durch D33.
  - **Mytkowicz et al. 2009 [belegt]:** Allein Link-Reihenfolge und Ausrichtung ändern die Laufzeit messbar. Das ist das fehlende Glied „Adressen → anderer Stromverlauf pro Block“.
  - **Unser Code [Code, im Klon geprüft]:**
    - I-Cache und D-Cache sind an, Flash läuft mit `FLASH_LATENCY_4`.
    - ITCM ist nur 4 KB (Stack), `CCMRAM` 60 KB ab 0x1000 ist ebenfalls ITCM.
    - Kein Firmware-Code liegt in ITCM.
    - Es gibt kein WFI.
  - **Ideen [Hypothese]:**
    - Den heißen Pfad ins ITCM/CCMRAM legen (Codec-DMA-ISR, `audioCallback`, Umwandlung, USB-Audio-ISR). Dann gibt es keine Wartezyklen und keinen Cache-Einfluss mehr, und die Laufzeit wird unabhängig vom übrigen Image.
    - Den Strom zwischen den Blöcken glätten, oder testweise WFI im Idle einbauen. Wächst die Linie dann, zählt die Strom-Differenz zwischen Blockarbeit und Leerlauf.
    - Jitter wie beim Daisy.
    - Den Füllbyte-Scan als Messwerkzeug benutzen.
    - Jede dieser Änderungen verschiebt die Lage einmal, darum gilt die A/B-Regel.

## Nächste Schritte (Vorschlag, alles in `TODO.md` Phase 5)

1. **Clip-Test mit 3d:** Signal über ≈ 9,5 V, z. B. VCO ±5 V + Offset +6 V über einen Mixer.
2. **E3-Hebel Lage:**
   - Füllbytes vor den Audio-Funktionen durchprobieren, z. B. in 0x20-Schritten über 0x200, je 2 × 60 s.
   - Frage: Gibt es eine Lage mit weniger Störlinien als Build 2?
   - Den Mechanismus eingrenzen: Flash-Wartezyklen, ART/I-Cache, Ausrichtung von `audioCallback`/`onProgramReady`, Ausführung aus ITCM.
   - **Kandidat mit Aussicht auf Dauerlösung:** den heißen Pfad ins ITCM/CCMRAM legen (siehe Recherche oben). Danach wäre die Lage des übrigen Codes egal.
   - Weitere Kandidaten: Jitter (wie beim Daisy) und der WFI-Test.
   - Vor dem Start mit `/grill-me` planen.
3. **1b → 1d neu bewerten:** Lage statt Patch 05/06?
4. **Optional:** Kontrolle Build 2 gegen 3d, falls der Kamm stört.
5. **Ideen des Nutzers:**
   - Regler als MIDI-CC beim Streamen senden, nur ohne Last und ohne Störlinien.
   - CV-taugliche LED-Anzeige.
6. **Offen:** `fb clamp -50.0000 32.0000` (3b, D31). Kommt das auch mit Build 2 und 3d vor?
7. **Forum #2244:** nur nach Freigabe posten.

## Fallstricke

- **SAI1 liefert die ADC-Wörter 24 Bit rechtsbündig ohne Vorzeichen** (`SAI_DATASIZE_24`). Deshalb erweitern: `(int32_t)((uint32_t)x << 8) >> 8`.
- **`--gc-sections` entfernt ungenutzte Füllfunktionen.**
  - Füllbytes in bestehende Input-Sections legen (`.text.onLoop`, `.bss.<symbol>`).
  - Oder `KEEP` im Linkerskript.
- **`.late_bss` wird beim Boot nicht genullt.** Deshalb Magic-Wert prüfen und selbst initialisieren (siehe 07d).
- **Patch-Dateien:** brauchen `+++ b/`-Pfade und werden mit `patch -p1` eingespielt. `usbd_audio.cpp` hat CRLF.
- **Build:**
  - Befehl: `FW_VERSION=… tools/build_acdc.sh <name> db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz 01 02 04 05 06 03 <07x>`
  - Das Ergebnis ist deterministisch, die SHA also vergleichbar.
- **Commits auf `acdc/fx1d`:** nur über einen temporären `git worktree`, den Klon nicht umschalten. Git-Schreibzugriffe, `owl_read.py` und `dfu-util` laufen nur außerhalb der Sandbox und jeweils mit Freigabe. Push nur nach Nachfrage.
- **`owl_read.py`:**
  - Aufruf: `uv run --no-project --python 3.12 --with mido --with python-rtmidi tools/owl_read.py`
  - Nach einer Messung lesen, aber bevor Host-Software gestoppt wird.
  - Nur die letzte Meldung bleibt erhalten.
- **Host-Software:**
  - Das Gerät heißt „OWL-ACDC-FX“, der MIDI-Port weiter „OWL-ACDC“.
  - Patch: `vcv-patches/acdc-fx-umc-in-out.vcv`
  - Pegel: Datei-dBFS = Gerät + 6,02 dB.
  - Host-Software öffnet ein Gerät immer in beide Richtungen.
- **Aufnahmen:**
  - Dateinamen nach Konvention, Mehrkanal-Recorder hängt `.4chan.000` an.
  - Jede Aufnahme kommt in `recordings/manifest.toml`.
  - Offene Eingänge doppelt aufnehmen und dabei nichts am Rack anfassen.
- **Analyse:** `UV_CACHE_DIR=.uv-cache uv run python -m analysis <ID> --ref <ID> --no-spectrogram`
- **Sitzungsdrift:** Absolute Werte zwischen Sitzungen schwanken bis ≈ 0,5 dB. Deshalb immer eine Kontrolle in derselben Sitzung.
