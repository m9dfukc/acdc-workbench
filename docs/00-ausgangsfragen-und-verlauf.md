# 00 – Ausgangsfragen & bisheriger Verlauf

Diese Datei hält fest, wie das Projekt entstanden ist: meine Fragen, wie recherchiert wurde, was dabei herauskam und welche Anmerkungen und Vorschläge Claude gemacht hat. Stand: 2026-11-14.

**Diese Datei wird nicht fortgeschrieben.** Sie zeigt den Wissensstand zu Beginn. Einiges ist überholt: acdc1 trug nie das offizielle v22.5.0 (messlog D3), ein Filter-Patch im Gerät erreicht mit der eigenen Firmware die Aufnahme nicht mehr, und Upstream hat seit 2026-11-15 neue Commits an der Build-Kette. Aktueller Stand: `CLAUDE.md` und `TODO.md`.

## 1. Meine ursprüngliche Anfrage (2026-10-23, wörtlich)

> ich habe ein AC/DC Eurorack Audiointerface. Leider produziert dieses viel Noise, ähnlich wie von der Person hier bereichtet: https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072 ... ein Kommentator schreibt, dass ein USB Ground Isolator geholfen hat. Recherchiere (weiter in diesem Forum aber auch generell), ob das wirklich etwas bringt und ob andere ebenfalls Noise Issues mit dem AC/DC Interface haben / hatten und welche Lösungsmöglichkeiten es gibt (potentiell auch per software filtering, falls das Band sehr schmal ist?!). Ausserdem checke die FW des Devices (https://github.com/RebelTechnology/OpenWare) und ob es hier neuere Entwicklungen (insbesondere in den Forks) gibt und ob mir diese irgend etwas für mein AC/DC bringen. mache einen deep-research, nutze parallele subagenten um die diversen Foren und Platformen zu durchsuchen. Ausserdem würde mich eine Lösung zu diesem Thema https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244 interessieren (der Poster bin ich). Falls Du Probleme hast das Forum zu scrapen / auszulesen ... finde einen Weg drum herum, zur not auch mit einem Webview.

Daraus ergeben sich diese Teilfragen:

| # | Frage | Antwort in |
|---|---|---|
| F1 | Bringt ein USB-Ground-Isolator wirklich etwas? | `02-noise-befunde.md` |
| F2 | Haben bzw. hatten andere auch Rauschprobleme mit dem AC/DC? | `02-noise-befunde.md` |
| F3 | Welche Lösungen gibt es, auch Software-Filter bei schmalem Band? | `02`, `03`, `04` |
| F4 | Wie ist der Stand der OpenWare-Firmware? Gibt es neue Entwicklungen, vor allem in Forks, die mir etwas bringen? | `05-firmware-plan.md` |
| F5 | Lösung für meinen Forum-Thread #2244: AC/DC als FX ohne Rechner, als Interface mit Rechner | `01`, `05` |

## 2. Mein Forum-Thread #2244 (Kontext, 2024-11 bis 2024-12)

- **Ich (2024-11-14):**
  - Zwei AC/DCs liegen ungenutzt, weil der Noise-Floor zu hoch ist (Verweis auf #2072).
  - Ich frage, welche Firmware-Änderung nötig wäre, damit das Modul (A) ohne Rechner als patchbarer FX/Synth läuft, wie beim Lich, und (B) mit Rechner als Audiointerface.
  - Ich frage nach antisvins modifizierter Firmware.
- **antisvin:**
  - Er vermutet, das Modul wurde wegen Hardwareproblemen eingestellt: Rauschen, Codec-Stabilität, OS-spezifische USB-Probleme. Updates von Rebel erwartet er keine.
  - Die Routing-Reihenfolge Patch/USB sei eine **Compile-Option** (Verweis auf #2110/5).
  - Mit nur 4 Knobs und ohne MIDI-Expander sei der Standalone-Betrieb begrenzt.
- **Ich:**
  - Zuerst wäre ein Mixer/Attenuator interessant, später ein Reaktor-artiger Write/Read-Buffer.
  - Frage: Muss es wirklich ein Firmware-Flag sein, gibt es keine Auto-Erkennung?
- **antisvin:**
  - Ja. Normal gehen die Eingänge an USB und USB in den Patch, hier bräuchte man das Umgekehrte.
  - Auto-Switching sei „not ideal“, weil der Patch beim Anstecken stoppt.
  - Einen Sampler kann man per Audio-Rate über die Eingänge triggern.
- **Ich:**
  - Ich kann etwas Pd, FAUST und C/C++.
  - Damit, dass der Patch bei USB stoppt, könnte ich leben.
  - Beim letzten Flashen habe ich das Modul fast gebrickt.
- **antisvin:**
  - Pd über Heavy ist nicht 100 % kompatibel.
  - FAUST empfiehlt er zuerst, aber nur mit **seinem OwlProgram-Branch**, weil Upstream mit neuem FAUST kaputt ist.
  - C++ hat eine steile Lernkurve.
- **Ich (2024-12-09):** Ich habe mir einen Lich geliehen und probiere das zuerst. Seitdem keine weiteren Posts.

## 3. Wie recherchiert wurde

- Deep-Research mit **vier parallelen Recherche-Strängen**:
  1. Forum-Rauschberichte AC/DC und Geschwistergeräte
  2. Allgemeine Ground-Loop-, Isolator- und Filterlösungen (ModWiggler, Gearspace, Reddit, Archimago, Hersteller)
  3. OpenWare-Code und Forks
  4. Standalone-FX (Thread #2244 + Code)
- Danach gab es eine **Nachrecherche** zur vollständigen Fork-Liste (die GitHub-API war anfangs blockiert und wurde über WebFetch umgangen).
- Forum gelesen über Discourse-JSON (`/t/<id>.json`, `/raw/<id>`). Nach ca. 30 Requests griff ein Rate-Limit, der Rest lief über WebFetch.
- OpenWare und Forks wurden geklont und nur gelesen (nichts gebaut). Auf `api.github.com` wurde die Fork-Liste ausgewertet: 21 Forks, 20 identifiziert, davon 5 mit eigenen Commits.
- Lücken:
  - ModWiggler- und Gearspace-Threads speziell zu Eurorack-Interfaces ließen sich nicht laden.
  - Es gibt keine YouTube- oder ModWiggler-Inhalte zu AC/DC-Rauschen.
  - atau's Google-Drive-Messdateien waren nicht einsehbar.
  - Kein Isolatormodell ist für das AC/DC bestätigt.
- Vollständiger Bericht: `research/report-2026-10-23.md`. Rohnotizen mit allen URLs: `research/notes/`.

## 4. Antworten in Kurzform (Stand der Recherche)

**F1 – Isolator:**
- Ein billiger Test, wahrscheinlich aber **nicht** die Lösung.
- Beim einzigen gemessenen Fall (atau) blieb der 1-kHz-Kamm mit USB-Optoisolator und im Akkubetrieb bestehen.
- Paupers „cheap ground isolator“ ist ein einzelner Satz ohne Details, vermutlich ein anderes Problem (klassische Masseschleife).
- Falls doch testen: Das AC/DC ist **USB Full Speed**, ein ADuM3160-Board reicht. **Kein Topping HS01.**

**F2 – Andere Betroffene:**
- Ja: atau (gemessen, 2 Geräte), selex, Pauper, ich.
- antisvin spricht von einem Hardwareproblem, das ein Redesign bräuchte. Ein offizielles Statement oder eine Hardware-Revision gibt es nicht.

**F3 – Lösungen:**
- Zuerst messen (Messplan in `03`). Der wichtigste neue Test ist die **Standalone-Gegenprobe**: Kamm nur bei aktivem USB-Stream? Den hat noch niemand gemacht.
- Bei stabilem Kamm eine **Notch-Bank** (23 Biquads, keine DC-Kerbe), entweder im DAW oder als FAUST-Patch in Slot 1.
- Mit Stock-Firmware geht der Patch-Ausgang direkt in die USB-Aufnahme, man muss also **nichts flashen**.
- Einen Kammfilter nicht verwenden, weil er DC auslöscht und damit CV zerstört.

**F4 – Firmware:**
- Upstream ist seit **v22.5.0 (2023-03-05)** eingefroren.
- Kein Fork adressiert das Rauschen.
- Relevant sind:
  - **shmuga `lich3-usb-fixes`** (Okt. 2026): H7-USB-TX-Bugs, nämlich dauerhafte Stille nach einem unvollständigen ISO-Transfer und Klick-Bursts durch die Ratenregelung. Backport-Kandidat.
  - **burstMembrane** (März 2026): PRE_FX-Routing für das ACDC als Präzedenzfall.
  - Klangs ungemergter Branch **`hack/acdc-output-levels`** (2022) für Rausch-Experimente. Commit `237c63d` nicht übernehmen.

**F5 – Standalone:**
- Laut Code läuft der Patch aus Slot 1 schon mit Stock-Firmware ohne Rechner.
- Für genau mein Wunschverhalten reicht **nur `USE_USBD_AUDIO_TX_PRE_FX`**. antisvin hatte beide Defines vorgeschlagen, mit RX_PRE_FX würde das DAW-Playback durch den Patch laufen.
- Die Unabhängigkeit der TX/RX-`#ifdef`s in `ProgramManager.cpp` wurde am 2026-11-13 im Quelltext geprüft.
- Auf Hardware ist das ungetestet.

## 5. Claudes Anmerkungen & Vorschläge (nicht vergessen)

- **Rauschen und Standalone hängen zusammen:** Wenn der Kamm im USB-Frame-Takt (1 ms) koppelt, ist der Standalone-Betrieb nicht nur ein Feature, sondern auch der saubere Betriebsmodus. Die Gegenprobe entscheidet, ob Geld in einen Isolator fließen sollte oder gleich Notch-Patch und Firmware dran sind.
- **f0 messen statt annehmen:** Das AC/DC sampelt real mit ≈47 991 Hz (−186 ppm). Bei SOF-Kopplung erwarte ich die Linien im File bei etwa 1000,2 Hz. Ein fester 1000-Hz-Kamm verfehlt die oberen Harmonischen.
- **Billigster LED-Test:** Ein Patch, der alle LED-Parameter auf 0 setzt, testet die LED-PWM-Hypothese (≈2,32 kHz) ohne Firmware-Build.
- **Null-Aufwand-Standalone-Test:** Eigenen Patch in Slot 1 speichern, USB ziehen, neu starten.
- **Flash-Sicherheit:**
  - Ein ST-Link V3 mini (STLINKV3MINIE) vorab.
  - Ein bekannt gutes Binary sichern.
  - Nur acdc1 (Testgerät) flashen, acdc2 (DIY, v22.4.q) bleibt Referenz.
  - Beim ST-Link-Flashen das Geräte-USB abziehen.
  - Das Release-`ACDC.bin` v22.5.0 hat laut antisvin USB kaputtgemacht. Der `Libraries`-Stand ist kritisch.
- **Flash-Budget:** nur ca. 20 KB frei (STM32H750, 128 KB).
- **Monitoring:** Ein Notch-Patch filtert die USB-Aufnahme, aber nicht die DAC-Ausgänge im Interface-Betrieb.
- **Strategisch:** Das AC/DC ist eine verwaiste Plattform. Ein sauberer öffentlicher `acdc-fx`-Branch mit Messdaten wäre de facto Maintainer-Arbeit und genau das, was dem Forum seit 2023 fehlt.
- **Angebotene nächste Schritte:** den Notch-Patch als fertiges OWL-Projekt vorbereiten bzw. den Firmware-Build mit `TX_PRE_FX` und den shmuga-Fixes.

## 6. Aktueller Stand (2026-11-13)

- Ich ziehe in ein Claude-Code-Projekt um und setze dort alles um.
- Ich wandle gerade meine Aufnahmen mit uv/Python in Spektrogramme um, das ist Phase 1 in `TODO.md`.

## 7. Erste eigene Messungen (2026-11-13)

- Drei Messungen (M1: kein Signal, Gain 12 Uhr; M2: kein Signal, Gain voll; M3: Sinus 838 Hz) mit je 4 Kanälen. Die Spektrogramme liegen heute in `out/v0/`, das erste Skript `spectrograms.py` ist entfernt (ersetzt durch `analysis/`). Details in `messlog.md`.
- **Ergebnis:** Ich habe den 1-kHz-Kamm, aber bei Gain 12 nur mit −80…−96 dBFS, also ≈ 50 dB leiser als atau. Er liegt bei 1000,053 Hz und ist nicht sample-synchron.
- Dazu: eine sample-synchrone Linie bei 6000,00 Hz (fs/8) und die LED-PWM bei 2320,98 Hz, die nur bei Signal oder hohem Gain auftaucht.
- Eine Notch-Bank brächte ≈ 4–5 dB (Gain 12) bzw. ≈ 10 dB (voller Gain).
- Korrektur einer eigenen Deutung: Der Gain-Knob ist im Default-Patch digital. Dass Linien stärker steigen als der Boden, beweist keine Einkopplung vor einer analogen Gain-Stufe.
- Die Aufnahmen lagen als 96 kHz / 16 Bit vor (hochgerechnet), ohne Geräte-Notiz und nur 7–10 s lang. Die nächste Serie wird sauber nach Messplan gemacht.
- Installierte Skills (aus `mattpocock/skills`): `grill-me`/`grilling`, `handoff`, `research`.
- Meine Antworten auf Claudes Rückfragen:
  - M1–M3 stammen von der **DIY-Variante**, ab jetzt **acdc2** genannt.
  - Fokus bleibt vorerst beim Rauschen und den digitalen Störlinien. In Aufnahmen über das AC/DC war immer etwas zu hören, vor allem mit Kompressor (der hebt leise Anteile an und macht den Kamm hörbar).
  - Zweites Interface: Behringer UMC202HD am selben Thunderbolt-Hub, verträgt keine Eurorack-Pegel.
  - Nächster Schritt: Analyse-Tool neu schreiben.

## 8. Serie 2, SOF-Nachweis und Durchleitung (2026-11-13/14)

- Serie 2 (S2-1…S2-4, S2-6): Mischprodukt-Periode bestätigt, acdc1 = v22.5.0, Kamm hängt am USB-SOF des Host-Controllers (Hub → Mac-Port verschiebt ihn um +124,5 ppm). acdc1 = Testgerät, acdc2 = Referenz.
- S3-Planung per `/grill-me`: Ausgänge über MTM Startup → UMC aufnehmen. Dabei kam heraus: **Die Ausgänge sind ohne Rechner-Playback stumm**, auf acdc1 auch im Kaltstart. Für acdc2 erklärt das der Hack `237c63d` in v22.4.q, für acdc1 (v22.5.0) ist es offen.
- Default-Patch „ACDC“ in der Library gefunden (unveröffentlicht, Martin Klang), Quelle gesichert in `owl-patches/library/`. Er ist ein Durchleit-VCA.
- OpenWare dauerhaft geklont nach `firmware/OpenWare`.
- Entscheidung: Vor dem Notch-Prototyp erst klären, ob eine Durchleitung auf acdc1 hinzubekommen ist. Neue Session per Handoff.
