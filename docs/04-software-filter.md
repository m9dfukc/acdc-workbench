# 04 – Software-Filter (Notch-Bank)

Voraussetzung: Messplan Schritt 1–2 zeigt einen **stabilen, schmalbandigen** Kamm, und f0 ist gemessen.

**Stand 2026-11-16:** Noch nichts davon ist gebaut. Der Plan hat sich verschoben:
- acdc1 nimmt mit der eigenen Firmware (`TX_PRE_FX`, ab Build 2) die **rohen Eingänge** auf. Ein Filter-Patch im Gerät (Abschnitt 2) erreicht die Aufnahme nicht mehr [gemessen, messlog D25, B2]. Er taugt nur noch für Geräte mit Stock-Routing (acdc2, Build 1d).
- Gefiltert würde deshalb im Rechner. **Optional** (Nutzer 2026-11-16), je nachdem, wie viel Störgeräusch am Ende bleibt und ob es sich lohnt: ein kleines **Plugin, das sich mit dem „Fingerabdruck“ des aktuellen Moduls bestücken lässt**, also mit den genauen Frequenzbändern, in denen die Störlinien liegen. Den Fingerabdruck liefert das Analyse-Tool je Modul und USB-Anschluss. Der Entwurf ist offen (`TODO.md`, „Störlinien“).
- Mit fx3l ist der SOF-Kamm die stärkste verbleibende Familie. Eine ideale Notch-Bank brächte ≈ 5,8 dB (RMS −72,7 gegen Rest −78,5 dBFS, D48).

## Welche Filterform?

| Variante | Problem | Urteil |
|---|---|---|
| FIR-Kamm `y = x − x[n−48]` | Kerbt alle k·1 kHz **und DC** aus, starke Färbung. Zerstört CV | nur zur Diagnose |
| IIR-Notch-Comb `(1+g)/2·(1−z^−N)/(1−g·z^−N)` | Schmal, aber ebenfalls DC-Kerbe. N muss ganzzahlig sein, f0 ist es real nicht | ungeeignet |
| **Notch-Bank** (ein Biquad pro Harmonischer) | Keine DC-Kerbe, f0 frei wählbar, Breite pro k einstellbar | ✅ **Wahl** |
| Adaptiv (LMS/PLL-Notch) | Folgt einer drift. f0. Mehr Aufwand | nur wenn f0 driftet |
| Spektrale Subtraktion (lernende Entstör-Plugins) | Für Breitband, kann Artefakte erzeugen | Offline/DAW |

Bei 48 kHz liegen **23 Harmonische** unter Nyquist. Die Kerbbreite sollte mit k leicht wachsen, weil kleine f0-Fehler sich bei hohen k vervielfachen. Das gilt umso mehr, als das AC/DC real mit ≈47 991 Hz läuft und f0 im File nicht exakt 1000 Hz ist.

### Filterziele aus den eigenen Messungen (M1–M3, siehe `messlog.md`)

| Familie | f0 im File | Harmonische | Hinweis |
|---|---|---|---|
| 1-kHz-Kamm | **1000,053 Hz** [gemessen] | k = 1…23 | Bei k = 23 liegt die Linie schon 1,2 Hz neben 23 000 Hz. Mit festem 1000 Hz würde die Bank oben vorbeikerben |
| fs/8-Linie | **6000,00 Hz** exakt | 6, 12, 18 kHz | Eigene Familie, liegt 0,32 Hz neben 6 × 1000,053. Eigene Notches oder breiter genug kerben |
| LED-PWM | **2320,98 Hz** [gemessen] | k = 1…9 | Nur relevant bei Signal oder hohem Gain. Besser an der Quelle lösen (LED aus / PWM-Frequenz verschieben) |

Gewinn laut M1/M2: ≈ 4–5 dB Rauschleistung bei Gain 12, ≈ 10 dB bei vollem Gain. Serie 2 (offene Eingänge): 4–10 dB.

**Wichtig (S2-6):** f0 hängt am USB-SOF des Host-Controllers. Gemessen: acdc2 am Hub 1000,0528 Hz, acdc1 am Hub 999,8663 Hz, acdc1 direkt am Mac 999,9908 Hz. Bei k = 23 liegen die Varianten bis zu 4 Hz auseinander. Daraus folgt:
- Ein Notch-Filter mit festem f0 muss pro Modul **und** USB-Anschluss eingemessen werden. Das Analyse-Tool liefert f0 auf < 1 mHz.
- Robuster wäre ein Filter, das f0 selbst nachführt (adaptiv/PLL). Im OWL-Patch kennt man den SOF-Takt nicht direkt, könnte ihn aber aus dem Signal schätzen.
- Neben dem Kamm gibt es Mischprodukte n·f1k + m·6 kHz (≈ 3–5 % der Leistung) im Abstand weniger Zehntel Hz. Etwas breitere Kerben (≈ 1–2 Hz) erfassen sie mit.

## 1. Python-Prototyp (offline, zum Abstimmen)

Im Analyse-Projekt unter `analysis/notch.py`. Ziel: Parameter (f0, Breite, Anzahl) an echten Aufnahmen tunen, bevor der FAUST-Patch geschrieben wird.

Spezifikation:
- Ein `scipy.signal.iirnotch(w0=k*f0, Q=k*f0/bw_k, fs=fs)` pro Harmonischer, mit `bw_k = bw * (1 + 0.1*k)`. Als SOS kaskadieren (`sosfilt`, numerisch stabil). Zusätzlich `sosfiltfilt` für die nullphasige Offline-Variante.
- CLI: `uv run analysis/notch.py in.wav --f0 1000.13 --bw 3 --harmonics 23 -o out/in_notched.wav`
- Vorher/Nachher-PSD überlagert plotten. RMS-Reduktion und Restlinien ausgeben.
- Testsignal: Aufnahme eines echten Audiosignals (Sinus-Sweep, Musik) **mit** Rauschen. Hörtest auf Färbung machen und die Phasenantwort der Bank plotten.
- Die Parameter, die gut funktionieren, in `docs/messlog.md` übernehmen. Sie fließen in den FAUST-Patch.

## 2. FAUST-Patch für das AC/DC (Slot 1)

**Nur für Stock-Routing (acdc2, Build 1d). Auf acdc1 ab Build 2 wirkungslos für die Aufnahme, siehe „Stand“ oben.**

Mit Stock-Firmware geht der **Patch-Ausgang in die USB-Aufnahme** (TX POST_FX). Ein Filter-Patch säubert also die Aufnahme ohne Firmware-Änderung. Live-Monitoring über die DAC-Ausgänge bleibt im Interface-Betrieb ungefiltert, weil das DAW-Playback den DAC überschreibt.

```faust
import("stdfaust.lib");
// Notch-Bank gegen USB-Frame-Kamm, 4 Kanäle, DC bleibt erhalten
f0   = hslider("f0 [OWL:A]", 1000.0, 995.0, 1005.0, 0.01) : si.smoo;
bw   = hslider("width [OWL:B]", 3.0, 0.5, 20.0, 0.1);           // Hz bei k=1
gain = hslider("gain [OWL:C]", 1.0, 0.0, 4.0, 0.01) : si.smoo;  // ersetzt Gain des Default-Patches
NH   = 23;
bank = seq(k, NH, fi.notchw(bw * (1 + 0.1*k), f0 * (k+1)));
process = par(i, 4, *(gain) : bank);
```

Hinweise:
- Die Rechenlast liegt bei ca. 92 Biquads × 48 kHz. Das ist auf einem Cortex-M7 mit 480 MHz unkritisch [Hypothese]. Mit `DEBUG_DWT` bzw. den Patch-CPU-Angaben prüfen.
- Die Knobs A–D wirken auf die **Eingangs-Gain-Hardware und** auf die Patch-Parameter. Der Default-VCA-Patch stellt Gain bereit, ein eigener Patch ersetzt ihn. Deshalb gibt es oben `gain`.
- Besser **f0 fest aus der Messung** eintragen und den Knob A nur zum Feintuning nutzen. Ein Knob mit 995–1005 Hz über 12 Bit ADC löst ca. 0,0025 Hz auf, das reicht.
- FAUST-Toolchain: Laut antisvin ist der Upstream-OwlProgram mit neueren FAUST-Versionen kaputt. Man braucht **antisvins OwlProgram-Branch** (Thread #2110/5). Ob die Label-Syntax für Parameter ab `AA` upstream funktioniert, ist unklar. A–D sollten gehen.
- Build und Upload über OwlProgram: `make FAUST=NotchBank load` (nur RAM, zum Testen) und danach `store` mit Slot 1. Alternativ die Web-Oberfläche der Patch Library (openwarelab.org).
- Erst mit `load` testen, nicht sofort `store`.

## 3. DAW-Variante und Plugin

Das ist der Weg für acdc1, falls gefiltert werden soll. Optional ist ein eigenes Plugin, das den Fingerabdruck des Moduls lädt (siehe „Stand“ oben). Ohne eigenes Plugin:

- Derselbe FAUST-Code als Plugin: `faust2vst`/`faust2au` oder über die Faust-IDE exportieren. Auf die Eingangsspuren legen.
- Fertige Plugins als Zwischenlösung, drei Bauarten:
  - Brumm-Entferner mit frei wählbarer Grundfrequenz und Harmonischen. Offen, ob 1 kHz als Grundfrequenz geht und ob die Zahl der Harmonischen reicht.
  - Spektrale Subtraktion mit einem Profil aus einer Stille-Aufnahme.
  - Breitbandige Entrauscher.
  - Konkrete Produkte: `research/notes/general_ground_loop_filtering.md`.

## Grenzen

- Was am DAC-Ausgang oder auf den Kabeln dazukommt, kann ein Patch nicht entfernen. Er sieht nur die ADC-Daten.
- Jede Kerbe entfernt auch Nutzsignal bei k·f0. Für langsame CV ist das egal, bei Audio und schmalen Kerben kaum hörbar.
- Wenn f0 lastabhängig driftet (Messplan Punkt 6), versagen feste Notches. Dann braucht es einen adaptiven Ansatz.
