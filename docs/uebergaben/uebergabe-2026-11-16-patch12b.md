# Übergabe – Patch 12b: RX-Fix ohne Abfrage-Schleife (Stand 2026-11-16 spätabends)

Für eine neue Session. Ersetzt `uebergabe-2026-11-16-fx3i-fehlersuche.md` als aktuelle Übergabe. Die gilt weiter für Prüfablauf und Werkzeuge. Antworte auf Deutsch.

**Auftrag:** Patch **12b** schreiben, damit einen neuen ITCM-Build bauen und prüfen, dann mit dem Nutzer am Gerät Loop-Test und Rauschmessung machen. 12b soll den veralteten Eingangs-Sample (D40) beheben, **ohne** die Abfrage-Schleife aus Patch 12. Die kostet ≈ 10,6 dB bei fs/8 (D42). **Nicht flashen ohne Freigabe**, jeder Flash einzeln. acdc2 nie anfassen.

## Zuerst lesen

1. `CLAUDE.md`: die Abschnitte „Build 4“, „Build 4x“, „Build 4y“ und „Konventionen“.
2. `docs/messlog.md`, **D39–D42**.
3. `docs/05-firmware-plan.md`, „Build 4x“ und „Build 4y“ (dort „Nächste Schritte“).
4. `firmware/patches/11e-itcm-variant-noD-anchor.patch` und `12-rx-dma-wait.patch`.

## Stand

- **acdc1 läuft mit 3d** `v22.4.r-fx2d` (`d212cf8d…`): Readback bytegleich, A1 bestanden, 3d-Endkontrolle in `B4y-3d-end`.
- **Zwei Fehler in fx3i (D39/D40):**
  1. USB-Slips/`fb clamp` ↔ Gruppe D (USB) im ITCM. Ungelöst. Deshalb bleibt D vorerst im Flash (noD-Basis).
  2. Veralteter letzter Eingangs-Sample (Kanal 4, 16 Frames alt) ↔ Gruppe C (Audio-Task) im ITCM. [Code] `audioCallback` hängt im PCM3168A-Zweig von `Source/Codec.cpp` an den **TX**-DMA-Callbacks (`HAL_SAI_TxHalfCpltCallback`/`TxCpltCallback`, SAI1-B, DMA1_Stream1). Freigegeben wird aber auch die **RX**-Hälfte (SAI1-A, DMA1_Stream0), und deren letztes Wort ist zu dem Zeitpunkt noch nicht geschrieben.
- **Messung D42** (Δ gegen 3d derselben Sitzung, Datei-dBFS):

  | Build | ITCM | RX-Fix | RMS | Kamm | fs/8 | Mischprod. | Loop |
  |---|---|---|---|---|---|---|---|
  | noD | ohne D | – | +0,7 | +2,5 | **−5,4** | +0,3 | 0 Slips, Kanal 4 veraltet |
  | fx3j (11e + 12) | ohne D | Abfrage-Schleife | +2,8 | +3,1 | **+5,2** | −10,1 | sauber |
  | fx3i (D37) | alles | – | −1,0 | ±0 | −5,1 | −0,5 | 28 Slips, Kanal 4 veraltet |

  - [Hypothese] CPU- bzw. Busaktivität im Blocktakt prägt fs/8. Schon wenige µs Lesen eines DMA-Registers pro Block heben fs/8 um ≈ 10 dB.
  - Den Kamm senkt nur der USB-Code im ITCM. Das ist der nächste Schritt danach, nicht Teil dieses Auftrags.

## Entwurf Patch 12b [Code, noch nicht gebaut]

- **Änderung in `Source/Codec.cpp`**, PCM3168A-Zweig (`#else // PCM3168A: TX is slave`): `audioCallback(...)` aus `HAL_SAI_RxHalfCpltCallback` bzw. `HAL_SAI_RxCpltCallback` aufrufen, mit denselben Argumenten wie heute in den TX-Callbacks. Das ist das Muster des CS4271-Zweigs direkt darüber.
  - Die RX-DMA-Interrupts laufen heute schon: `HAL_SAI_Receive_DMA` setzt `SAI_DMARxHalfCplt`/`SAI_DMARxCplt`, DMA1_Stream0_IRQHandler ist aktiv, nur die schwachen HAL-Callbacks sind leer. Es entsteht also kein zusätzlicher Interrupt und keine Abfrage. Der Block startet nur ≈ 1 Wort später.
  - Wenn der RX-Interrupt kommt, ist die RX-Hälfte vollständig. Die TX-DMA ist höchstens FIFO-Tiefe in die andere Hälfte voraus, der Task hat also fast einen ganzen Block Zeit, um die eben gesendete TX-Hälfte zu schreiben.
- **TX-Callbacks in `Codec.o` leer stehen lassen** (starke, leere Definitionen). Grund: Die ITCM-Regel `*Codec.o(.text.HAL_SAI_TxHalfCpltCallback .text.HAL_SAI_TxCpltCallback)` greift dann weiter, und der TX-DMA-Interrupt springt nicht über einen Veneer in die schwache HAL-Fassung im Flash.
- **Linkerskript:** Die neuen starken RX-Callbacks liegen in `Codec.o`. Die bisherige Regel `*stm32h7xx_hal_sai.o(.text.HAL_SAI_RxHalfCpltCallback .text.HAL_SAI_RxCpltCallback)` greift deshalb nicht mehr, sie landen sonst im Flash.
  - Neuer Ersatz-Patch **11f** = 11e plus `*Codec.o(.text.HAL_SAI_RxHalfCpltCallback .text.HAL_SAI_RxCpltCallback)` in Gruppe A.
  - Bestehende Patches nie ändern. 11f vollständig als Alternative zu 11/11a/11e schreiben, wie 11e entstanden ist: `orig` (3d-Baum) + 11e anwenden, Zeile ergänzen, `diff -u` mit Labels `a/`/`b/`. `startup_owl3.s` hat CRLF.
  - Danach `check_itcm.py --groups ABCEFGHL`. Die HOT-Liste kennt die RX-Callbacks schon. Prüfen, dass sie aus `Codec.o` kommen und im ITCM liegen und dass keine Veneers zu `HAL_SAI_*Callback` hinausgehen.
- **Zähler [Code]:** `codec.getSampleCounter()` liest den TX-NDTR (`codec_ndtr`, `hdma_sai1_b`). Patch 06 (Füllstand) und `usbd_audio_get_rx_count` bleiben dadurch gültig. Zum Callback-Zeitpunkt steht der Zähler nur um ≈ 1 Wort anders. Kurz gegenlesen.
- **Header von 12b** wie in 12: Befund, Ursache, Änderung, auf welche Patches. FW_VERSION nur `[A-Za-z0-9._-]`.

## Builds (Vorschlag)

| Name | FW_VERSION | Patches | Zweck |
|---|---|---|---|
| `acdc1-build4z-fx3k` | `v22.4.r-fx3k` | 01 02 04 05 06 03 07d 08 **11f 12b** | Kandidat fx3i′ |
| `acdc1-build4zp-fx3kp` | `v22.4.r-fx3kp` | dazu 91 | Lagen-Test, nur wenn fx3k ≤ 3d |
| optional `acdc1-build3e-fx2e` | `v22.4.r-fx2e` | 01 02 04 05 06 03 07d 08 **12b** | Gehört 12b auch in 3d bzw. Standalone? Ändert das Rauschen ohne ITCM? |

Aufruf unter **zsh mit Array**, sonst kommt die Patchliste als ein einziges Argument an:

```
P=firmware/patches; base=($P/01-gcc12-extern-uint8.patch $P/02-revert-237c63d-thru-mute.patch $P/04-output-gain-125.patch $P/05-atomic-usbd-rx-count.patch $P/06-fb-level-control.patch $P/03-tx-pre-fx-owl-acdc-fx.patch $P/07d-input-leds-raw-late-section.patch $P/08-upstream-gcc13-build-flags.patch)
FW_VERSION=v22.4.r-fx3k tools/build_acdc.sh acdc1-build4z-fx3k db9d3dd firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz $base $P/11f-….patch $P/12b-….patch
UV_CACHE_DIR=.uv-cache uv run python tools/check_itcm.py firmware/builds/acdc1-build4z-fx3k --groups ABCEFGHL --ref firmware/builds/acdc1-build3d-fx2
```

Für fx3kp zusätzlich `--same-itcm firmware/builds/acdc1-build4z-fx3k`. Disassembly der RX-Callbacks ansehen (`arm-none-eabi-objdump -d … | awk '/<HAL_SAI_RxHalfCpltCallback>:/,/^$/'`): Sie sollen direkt `audioCallback` aufrufen, ohne Schleife.

## Prüfablauf am Gerät (mit dem Nutzer, je Flash Freigabe)

Flash nach `CLAUDE.md` (owl_read vorher, `--reset-to-dfu --yes`, `dfu-util -D`, Readback-Vergleich + Rest 0xFF, Neustart durch den Nutzer, A1). Flashlog nach `firmware/flashlog/YYYYMMDD_<build>/`. Geräte-Werkzeuge laufen außerhalb der Sandbox. Die Kurzfassung als Skript steht unten.

Reihenfolge wie D42, jede Rauschmessung mit 2 × 60 s und `--owl-read --analyze`, Host-Last gleich halten:

1. Kabel ab: **3d-Startkontrolle**: `acdc_rec.py --id B4z-3d --test 3d-open-inputs-4z --reps 2 --duration 60 … --owl-read --analyze --ref B4y-3d-r1`
2. Kabel Out n → In n: Flash fx3k, **Loop** 60 s mit `--sine 440 530 670 790 --sine-fade 1 --owl-read`, danach
   - `tools/phase_slips.py <wav> --freqs 440 530 670 790` → 0 Slips, MAD ≈ 0,01 mrad
   - `tools/stale_samples.py <wav> --freqs 440 530 670 790 [--dur 30]` → 0 veraltete Samples, Kanal 4 ≈ −6,06 dBFS
   - Gerätemeldung ohne `fb clamp`
3. Kabel ab: **Rauschen fx3k** 2 × 60 s
4. Nur wenn fx3k bei fs/8, Kamm und Mischprodukten ≤ 3d + 0,5 dB liegt: Flash fx3kp, Rauschen (Q2 b, lagenunabhängig ≤ 0,5 dB)
5. 3d zurück (Freigabe), **3d-Endkontrolle** 2 × 60 s
6. `tools/family_table.py <IDs…> --ref B4z-3d-r1 B4z-3d-r2 B4z-3d-end-r1 B4z-3d-end-r2 --out out/B4z-session-table.md`
7. Doku: messlog D43ff., docs/05 „Build 4z“, CLAUDE.md, TODO.

**Erwartung [Hypothese]:** fx3k ≈ noD bei fs/8 (≈ −5 dB), Kamm ≈ +2,5 dB (USB im Flash), Kanal 4 sauber. Hebt fx3k fs/8 trotzdem an, ist schon die Verschiebung des Blockstarts um ≈ 1 Wort relevant. Dann zum Vergleich die optionale 3d+12b-Variante messen.

## Flash-Helfer (bewährt, Ablauf aus CLAUDE.md)

```zsh
#!/bin/zsh
# flash.sh <build-dir-name> <flashlog-name>   (außerhalb der Sandbox ausführen)
set -e
cd /Users/m9dfukc/Desktop/acdc
B=firmware/builds/$1/ACDC.bin; FL=firmware/flashlog/$2
[ -f $B ] || { echo "kein $B"; exit 1; }
[ -e $FL ] && { echo "$FL existiert"; exit 1; }
mkdir -p $FL
OWL=(env UV_CACHE_DIR=.uv-cache uv run --no-project --python 3.12 --with mido --with python-rtmidi python tools/owl_read.py)
$OWL --out $FL/owl_read_before 2>&1 | tail -2
grep -q '0039001c:31315101:39333437' $FL/owl_read_before/acdc1/*/device_report.json || { echo "nicht acdc1"; exit 1; }
$OWL --reset-to-dfu --yes 2>&1 | tail -1
for i in {1..15}; do dfu-util -l 2>/dev/null | grep -q "0483:df11.*serial=\"200364500000\"" && break; sleep 1; done
dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000 -D $B > $FL/dfu-util_download.txt 2>&1
tail -1 $FL/dfu-util_download.txt
dfu-util -d 0483:df11 -S 200364500000 -a 0 -s 0x08000000:131072 -U $FL/readback_after.bin > $FL/dfu-util_upload.txt 2>&1
N=$(stat -f %z $B)
{ shasum -a 256 $B $FL/readback_after.bin; echo "$(head -c $N $FL/readback_after.bin | shasum -a 256 | cut -d' ' -f1)  readback_after.bin[0:$N]"; } | tee $FL/sha256.txt
python3 -c "
b=open('$B','rb').read();d=open('$FL/readback_after.bin','rb').read()
print('Readback bytegleich:', d[:len(b)]==b, '| Rest 0xFF:', all(x==0xff for x in d[len(b):]))"
```

Nach dem Neustart A1: `owl_read.py --out $FL/owl_read_after`, dann im `device_report.json` unter `info` Version, `SR/BS/CH 48000 8 4` und die Slots (ACDC, ACDC, [Lich]) prüfen.

## Fallstricke

- **zsh:** Eine Patchliste als String wird nicht aufgeteilt, Arrays nehmen. Die Shell gibt bei `cd` ein `ls` aus. Absolute Pfade nehmen.
- **Sandbox:** `$TMPDIR` ist in der Sandbox `/tmp/claude-501`, außerhalb ein anderes Verzeichnis. Skripte, die beide Seiten brauchen, ins Scratchpad legen.
- `acdc_rec.py` ohne `--analyze` erzeugt keine `out/<ID>/<ID>.json`. `family_table.py` bricht dann ab. Nachholen mit `uv run python -m analysis <ID> --manifest recordings/manifest.toml --ref … --no-spectrogram`.
- Gerätemeldung: Nur die letzte bleibt. `fb clamp` (alle 32 ms) überdeckt alles andere.
- Eine Input-Section landet in der **ersten** passenden Linker-Regel. Weak/Strong-Paare nach Objektdatei filtern, darum 11f.
- Neuer Code verschiebt die Flash-Lage (der ITCM-Block wächst, alles dahinter rückt). Immer gegen 3d derselben Sitzung messen.
- Git-Schreibzugriffe und Push nur mit Freigabe.
