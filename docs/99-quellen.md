# 99 – Quellen

## Rebel Technology Forum
- #2072 Clock noise in AC/DC (atau, mars, antisvin, Pauper): https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072
- #2244 AC/DC as FX when not connected to computer (eigener Thread): https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244
- #2110/5 FAUST/Pd patches on AC/DC (PRE_FX-Rezept, antisvins OwlProgram-Branch): https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110/5
- #2083 AC/DC firmware update (kaputtes Release-Binary, OpenOCD, Default-Patch ohne USB): https://community.rebeltech.org/t/ac-dc-firmware-update/2083
- #2077 AC/DC MIDI input (Expander nie erschienen): https://community.rebeltech.org/t/ac-dc-midi-input/2077
- #2069 Sending CV via ACDC: https://community.rebeltech.org/t/sending-cv-via-acdc-patch-needed-or-something-else/2069
- #2042 44.1 kHz sample rate: https://community.rebeltech.org/t/44-1khz-sample-rate-possible/2042
- #2025 Befaco AC/DC not recognized: https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025
- #3725 Bricked Xibeca dev kit (DFU, USB-Audio-Ausfälle 2026): https://community.rebeltech.org/t/bricked-xibeca-dev-kit/3725
- Geschwistergeräte:
  - Wizard #1104: https://community.rebeltech.org/t/wizard-ground-loop-problem/1104
  - Magus #1511: https://community.rebeltech.org/t/usb-isolator-with-magus/1511
  - Magus #1703: https://community.rebeltech.org/t/output-noise-on-magus-please-help/1703
  - Lich #1863: https://community.rebeltech.org/t/digital-noise-from-lich-after-firmware-update/1863
  - OWL #185: https://community.rebeltech.org/t/high-pitched-noise-when-connected-via-usb/185
  - OWL #444: https://community.rebeltech.org/t/new-owl-user-having-noise-in-my-sig-chain-when-connected-to-a-compuer-via-usb/444

Tipp: Discourse liefert Rohdaten unter `https://community.rebeltech.org/t/<id>.json` bzw. `/raw/<id>`.

## Firmware / Code
- OpenWare: https://github.com/RebelTechnology/OpenWare (v22.5.0 = `62a0187`)
  - `ACDC/Core/Inc/hardware.h`, `ACDC/Core/Src/main.c`, `Source/ProgramManager.cpp`, `Source/usbd_audio.cpp`, `Source/pcm3168a.c`, `Hardware/xibeca.mk`
  - Branch `hack/acdc-output-levels`: https://github.com/RebelTechnology/OpenWare/tree/hack/acdc-output-levels
- shmuga `lich3-usb-fixes`: https://github.com/shmuga/OpenWare/tree/lich3-usb-fixes
- burstMembrane ACDC-Commit: https://github.com/burstMembrane/OpenWare/commit/20d322dc09d983bfd04502053b420cc7bcf15e50
- OwlProgram: https://github.com/RebelTechnology/OwlProgram
- OpenWareLab (Patch Library, Firmware-Tool): https://www.openwarelab.org/Tools/firmware.html
- Fork-Liste (API): https://api.github.com/repos/RebelTechnology/OpenWare/forks?sort=newest&per_page=100

## Hersteller / Datenblätter
- Befaco AC/DC: https://www.befaco.org/ac-dc/
- ADuM3160 (LS/FS): https://www.analog.com/ADuM3160
- FAUST filters.lib (`fi.notchw`): https://faustlibraries.grame.fr/libs/filters/

## Ground Loop / Isolatoren / Filter
- Hifimediy, USB-Audio-Noise: https://hifimediy.com/usb-audio-noise/
- Hifimediy, Isolator-Vergleich: https://hifimediy.com/2020/06/choosing-the-right-usb-isolator/
- Archimago, 8-kHz-USB-PHY-Ton: https://archimago.blogspot.com/2015/05/measurements-usb-hubs-and-8khz-phy.html?m=0
- Archimago, Topping HS01: https://archimago.blogspot.com/2022/03/measurements-topping-hs01-usb-20.html?m=0
- Olimex USB-ISO-HS: https://core-electronics.com.au/usb-high-speed-isolator-galvanic-protection.html.md
- Manikin Modul 2: https://schneidersladen.de/en/manikin-electronic-modul-2-usb-high-speed-isolator
- iZotope RX De-hum: https://help.izotope.com/docs/rx-plug-in-pack/De-hum.html
- ReaFIR: https://www.cockos.com/wiki/index.php/ReaFIR
