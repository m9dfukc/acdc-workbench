<!-- i18n source=docs/99-quellen.md sha256=4b36b50118de75113bc8b1700c9f0a41dcd7d793631a01bed3e8b51953f12f1b date=2026-11-16 -->
> English translation of [`docs/99-quellen.md`](../../docs/99-quellen.md), as of 2026-11-16. The German original is authoritative. This file is generated from it, do not edit it by hand.

# 99 – Sources

## Rebel Technology Forum
- #2072 Clock noise in AC/DC (atau, mars, antisvin, Pauper): https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072
- #2244 AC/DC as FX when not connected to computer (my own thread): https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244
- #2110/5 FAUST/Pd patches on AC/DC (PRE_FX recipe, antisvin's OwlProgram branch): https://community.rebeltech.org/t/faust-pd-patches-on-ac-dc/2110/5
- #2083 AC/DC firmware update (broken release binary, OpenOCD, default patch without USB): https://community.rebeltech.org/t/ac-dc-firmware-update/2083
- #2077 AC/DC MIDI input (expander never appeared): https://community.rebeltech.org/t/ac-dc-midi-input/2077
- #2069 Sending CV via ACDC: https://community.rebeltech.org/t/sending-cv-via-acdc-patch-needed-or-something-else/2069
- #2042 44.1 kHz sample rate: https://community.rebeltech.org/t/44-1khz-sample-rate-possible/2042
- #2025 Befaco AC/DC not recognized: https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025
- #3725 Bricked Xibeca dev kit (DFU, USB audio dropouts 2026): https://community.rebeltech.org/t/bricked-xibeca-dev-kit/3725
- Sibling devices:
  - Wizard #1104: https://community.rebeltech.org/t/wizard-ground-loop-problem/1104
  - Magus #1511: https://community.rebeltech.org/t/usb-isolator-with-magus/1511
  - Magus #1703: https://community.rebeltech.org/t/output-noise-on-magus-please-help/1703
  - Lich #1863: https://community.rebeltech.org/t/digital-noise-from-lich-after-firmware-update/1863
  - OWL #185: https://community.rebeltech.org/t/high-pitched-noise-when-connected-via-usb/185
  - OWL #444: https://community.rebeltech.org/t/new-owl-user-having-noise-in-my-sig-chain-when-connected-to-a-compuer-via-usb/444

Tip: Discourse serves raw data at `https://community.rebeltech.org/t/<id>.json` or `/raw/<id>`.

## Firmware / Code
- OpenWare: https://github.com/RebelTechnology/OpenWare (v22.5.0 = `62a0187`)
  - `ACDC/Core/Inc/hardware.h`, `ACDC/Core/Src/main.c`, `Source/ProgramManager.cpp`, `Source/usbd_audio.cpp`, `Source/pcm3168a.c`, `Hardware/xibeca.mk`
  - Branch `hack/acdc-output-levels`: https://github.com/RebelTechnology/OpenWare/tree/hack/acdc-output-levels
- shmuga `lich3-usb-fixes`: https://github.com/shmuga/OpenWare/tree/lich3-usb-fixes
- burstMembrane ACDC commit: https://github.com/burstMembrane/OpenWare/commit/20d322dc09d983bfd04502053b420cc7bcf15e50
- OwlProgram: https://github.com/RebelTechnology/OwlProgram
- OpenWareLab (patch library, firmware tool): https://www.openwarelab.org/Tools/firmware.html
- Fork list (API): https://api.github.com/repos/RebelTechnology/OpenWare/forks?sort=newest&per_page=100

## Manufacturers / datasheets
- Befaco AC/DC: https://www.befaco.org/ac-dc/
- ADuM3160 (LS/FS): https://www.analog.com/ADuM3160
- FAUST filters.lib (`fi.notchw`): https://faustlibraries.grame.fr/libs/filters/

## Ground loop / isolators / filters
- Hifimediy, USB audio noise: https://hifimediy.com/usb-audio-noise/
- Hifimediy, isolator comparison: https://hifimediy.com/2020/06/choosing-the-right-usb-isolator/
- Archimago, 8 kHz USB PHY tone: https://archimago.blogspot.com/2015/05/measurements-usb-hubs-and-8khz-phy.html?m=0
- Archimago, Topping HS01: https://archimago.blogspot.com/2022/03/measurements-topping-hs01-usb-20.html?m=0
- Olimex USB-ISO-HS: https://core-electronics.com.au/usb-high-speed-isolator-galvanic-protection.html.md
- Manikin Modul 2: https://schneidersladen.de/en/manikin-electronic-modul-2-usb-high-speed-isolator
- iZotope RX De-hum: https://help.izotope.com/docs/rx-plug-in-pack/De-hum.html
- ReaFIR: https://www.cockos.com/wiki/index.php/ReaFIR
