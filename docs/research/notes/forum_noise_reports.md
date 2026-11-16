# Noise/hum/whine reports for the Rebel Technology / Befaco AC/DC and OWL siblings (forum inventory, as of 2026-10-23)

Method note: I read the Rebel Tech Discourse forum through its JSON endpoints (`/t/<id>.json?print=true`, `/search.json?q=...`, `/raw/<id>`) with curl. Those endpoints worked, but after about 30 requests the forum rate-limited curl ("You've performed this action too many times"). I fetched the remaining threads with WebFetch (HTML). I ran 19 forum searches: ac/dc noise, acdc noise, hum, whine, ground loop, isolator, usb noise, buzz, hiss, interference, noise floor, 1khz, led noise, and noise plus witch/lich/magus/genius/wizard. On GitHub, I did a shallow clone of RebelTechnology/OpenWare at master (HEAD commit "v22.5.0", 2023-03-05) to check the AC/DC hardware config. The `gh` API (issues) was not available for that repo in this session, so **I could not search GitHub issues**. Web searches for ModWiggler, Reddit and YouTube found no AC/DC noise threads; only shop pages and reviews came up (see Gaps).

## 1. Who reports noise with the AC/DC, and with what symptoms?

### Takeaway
I found four separate AC/DC noise reports on the forum (2022-2024). The only detailed one is atau's (Mar–Jun 2023). It describes a narrowband tone at **1 kHz plus its harmonics** on the USB-recorded inputs, with nothing plugged in. Its level rises with the input trim knobs (about -30 dB at unity, up to -18 dB at max). Changing PSU or skiff, running the laptop on battery, or adding a USB opto-isolator did not change it. An ES-8 tested under the same conditions was clean. A forum developer (antisvin) reproduced the 1 kHz-harmonic signal on his own unit at a lower level. In 2024 he described "that noise issue" as a hardware problem that would need a redesign to fix.

### Cited Findings
**Thread "Clock noise in AC/DC" (topic 2072), 7 posts, read in full** — https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072
- **#1 atau, 2023-03-11:** AC/DC on firmware v22.5.0, used as an ES-8 alternative. Output from Max to the modular works. Recording into Logic 10.6.1 on a 13" 2020 MacBook Pro (4× TB3, macOS 10.15.7) at 48 kHz with nothing in the inputs gives a "harmonic clock noise" that grows as the input trim pots are turned up. In the spectrogram (Adobe Audition), the noise follows the knob sweeps on Ch1 and Ch2 exactly. A different skiff with a different PSU gave the same result. Nothing else in the system is noisy, and the ES-8 recorded clean in the same test. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **#2 maceq687, 2023-03-23:** Does not own an AC/DC. Suspects the USB ground connection. Asks whether the ES-8 was on USB or ADAT, and suggests unplugging the MacBook from the wall. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **#3 atau, 2023-04-01:** The ES-8 was also on USB, in parallel conditions. He then tried everything he could think of:
  - an **opto-isolator inline on the USB**
  - different skiffs and PSUs
  - insulating the module from contact with other modules
  - **running the host on battery**

  The artifact remained in every case. He reproduced it on **two AC/DC units (serials 191 and 250)**. Measured character: **harmonic at multiples of 1 kHz**, dependent on the front-panel input gain. About **-30 dB at unity (12 o'clock), up to -18 dB at max gain**. Recordings and screenshots are in a Google Drive folder (https://drive.google.com/drive/u/1/folders/1f9noaaT1r5M0GiCiWgSXza5I7TscWwVr). — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **#4 mars (Martin Klang, Rebel Technology), 2023-04-04:** Said the reported levels are "definitely not normal". Promised noise-floor and SNR graphs once back "in the lab (i.e my garage)", about a week later. **No follow-up with measurements appears in the thread.** As a diagnostic, he asked atau to load a pass-through patch from the OWL Patch Library, without storing it. That patch disables the gain controls and leaves probably two channels working. If the noise went away, the gain controls would be the culprit. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **#5 antisvin, 2023-04-04:** Gets "this 1KHz + harmonics signal too", at a lower level. His unit also picks up something else from his computer, possibly **related to LED blinking**. That noise recurs about every 0.8 s and is louder than atau's. He planned a test with a USB splitter that separates power/ground from the data lines. **No result was posted.** He expected the bypass patch to make no difference: the ADC (pot) values are smoothed, and pot or block-related noise would have a **3 kHz root** (48 kHz SR / 16-sample block), not 1 kHz. He also noted that the official v22.5.0 release file broke USB for him and only his own build worked. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **#6 atau, 2023-06-28:** The gain-bypass patch **changes nothing**. With the AC/DC plugged into the laptop via USB and Logic running, he sees **-30 dB indicated on inputs 1–4** with nothing connected. The harmonic signal still shows in the spectrogram. He posted two screenshots. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **#7 Pauper, 2023-11-01 (last post):** In full: "With a cheap ground isolator the noise desapears." **That is all he wrote.** He gives no isolator model, no USB speed, and does not say whether it was a USB isolator or an analog audio-line isolator. He also does not say whether audio streaming still worked through it. There is no further reply. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)

**Other AC/DC reports**
- **selex (sebastian), 2022-11-27:** New Befaco AC/DC on a MacBook in Ableton. It worked, but "the noise floor was very high". The unit later stopped enumerating as an audio interface, a separate issue. — [topic 2025](https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025)
- **antisvin's reply to selex, 2022-11-28,** lists three possible noise sources: (1) the case PSU, fixed by replacing the PSU or using another case; (2) the USB connection, which "you might be able fix … with a USB isolator"; (3) using the AC/DC to amplify line-level signals considerably, which amplifies the **codec input noise**. For (3) he recommends an analog gain stage to bring the signal up to Eurorack level. — [topic 2025](https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025)
- **TigerMM, 2023-03-01:** Running SuperCollider and VCV into the AC/DC. Sending CV gave random-looking results with "a lot of noise", and the LFO arrived as trigger-like fragments (video https://www.youtube.com/shorts/umeY5GzunLQ and https://youtu.be/8RKdizZQNVw). antisvin attributed it to USB audio output or sync problems, or possibly a faulty unit or host clock. He suggested a larger buffer and the pre-release firmware, which "does have some improvements related to USB audio synchronization". He noted a new stable release came out around 2023-03-05. This is a USB-stream/sync artifact, not hum. — [topic 2069](https://community.rebeltech.org/t/sending-cv-via-acdc-patch-needed-or-something-else/2069)
- **m9dfukc, 2024-11-14:** Owns two AC/DCs that sit unused because "the noise floor is just to high if used as an audio interface which I could never resolve". — [topic 2244](https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244)
- **antisvin's reply, 2024-11-14:** He suspects the AC/DC was discontinued "because there are some problems with hardware that would require redesign to fix (**that noise issue**, but there have been other problems with codec's stability for some users, various OS-specific USB issues and more)". He adds that "it doesn't look like there's going to be any updates from RebelTechnology any time soon". m9dfukc notes the AC/DC is gone from Befaco's product overview, and Schneiders Laden lists it as no longer available. Neither had seen an official discontinuation statement. — [topic 2244](https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244)

### Inferences
- There are only about 4 AC/DC noise reporters on the forum (atau, selex, m9dfukc, Pauper), plus developer antisvin reproducing it. Only atau's report is quantitative.
- atau's measured profile: 1 kHz fundamental plus harmonics, present with inputs open, scaling with input gain, not removed by PSU or skiff changes, a battery-powered host, or a USB opto-isolator, and present on two serials. That fits **a deterministic 1 ms-periodic disturbance on the board itself** better than a classic mains ground loop, which would sit at 50/60 Hz harmonics. USB Full-Speed frames (SOF) and USB audio packets repeat every 1 ms, so a 1 kHz comb is a typical signature of USB-packet-rate current or ground bounce coupling into the codec input stage. This is my inference; no developer stated it.
- The gain-dependence does not prove the noise enters before the trim stage. The default patch applies the knob as digital gain, so any noise in the ADC data scales with the knob. The bypass-patch result (no change, -30 dB at fixed unity gain) is consistent with noise already present in the codec ADC data.

### Gaps
- mars's promised noise-floor and SNR measurements never appeared in the thread.
- antisvin's USB power/data splitter test result was never posted.
- I could not see atau's Google Drive files or the screenshots (images only).
- Whether noise appears with no USB host connected (standalone patch mode) was never tested on the AC/DC.

## 2. What is the noise tied to: USB ground loop, clock, codec, power rails, LEDs?

### Takeaway
No root cause was ever officially confirmed for the AC/DC. Developers offered PSU, USB ground, codec input noise and LED PWM as possibilities. Atau's tests rule out PSU and host mains/ground for his case. antisvin's 2024 remark ("problems with hardware that would require redesign") is the closest thing to a verdict. On sibling OWL devices, the recurring, developer-acknowledged sources are USB bus power/ground loops and LED/OLED PWM.

### Cited Findings
- **Hardware facts from OpenWare source (master, tag commit v22.5.0, 2023-03-05), `ACDC/Core/Inc/hardware.h`:**
  - codec `USE_PCM3168A` (TI PCM3168A)
  - `CODEC_HP_FILTER` **commented out**, so the codec's DC-blocking HPF is off and the unit stays DC-coupled
  - `AUDIO_CHANNELS 4`, `AUDIO_BITS_PER_SAMPLE 16`, `AUDIO_SAMPLINGRATE 48000`
  - `USE_USBD_AUDIO_TX`/`RX` (both directions)
  - `USE_USBD_FS`, `USBD_AUDIO_BUFFER_PACKETS 3`
  - MCU STM32H743 at 480 MHz

  `ACDC.ioc` maps `USB_OTG_FS` to PA11/PA12 with no ULPI PHY. — [OpenWare ACDC hardware.h](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Inc/hardware.h), [ACDC.ioc](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/ACDC.ioc)
- **LED drive:** The `ACDC.cpp` input and clip LEDs are PWM-dimmed via TIM2/TIM3 with prescaler 100 and period 1023 on a 240 MHz timer clock (per `main.c`/`.ioc`). The default patch sets LED intensity from signal level. — [ACDC.cpp](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/ACDC.cpp), [main.c](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Src/main.c), [topic 2069 (antisvin on default patch)](https://community.rebeltech.org/t/sending-cv-via-acdc-patch-needed-or-something-else/2069)
- **Befaco's own spec page:** "class compliant audio interface", 48 kHz, **16-bit**, DC-coupled ±10 V, +12 V 200 mA / -12 V 30 mA, 6 HP. It gives no SNR figure and does not state the USB speed. — [befaco.org/ac-dc](https://www.befaco.org/ac-dc/)
- **antisvin (2023-04-04):** a pot-related artifact would have a 3 kHz root, not 1 kHz. He suspects a separate ~0.8 s periodic noise is tied to LED blinking. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **antisvin (2022-11-28):** three candidate sources: PSU, USB connection, and codec input noise under high digital gain. — [topic 2025](https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025)
- **antisvin (2023-05-20), AC/DC firmware-flashing thread:** two simultaneous USB connections (programmer plus device port) caused "weird problems… probably some kind of ground loop". He advises unplugging the device USB while using the ST-Link. — [topic 2083](https://community.rebeltech.org/t/ac-dc-firmware-update/2083)

**Sibling devices (OWL Pedal/Modular, Wizard, Magus, Lich)**
- **OWL Pedal 2014, johannes-g:** high-pitched noise when USB-powered from a Linux PC. A 2008 MacBook was clean. Developer giom said some USB ports are noisy and suggested a phone charger or a powered hub. mars said laptop power adapters are a source and that an external 9 V supply beats USB power. He advised avoiding PSUs with a switching frequency below 30 kHz. — [topic 185](https://community.rebeltech.org/t/high-pitched-noise-when-connected-via-usb/185)
- **OWL Pedal 2017, evan:** high-pitched, variable noise or hiss when connected to the computer. Ableton Push LEDs change the interference. An external Voodoo Pedal Power 2 reduced but did not eliminate it. mars described a **hidden jumper under the digital board that disconnects USB VBUS**, so the pedal runs on external power with USB data still working. He named ground loops via a USB-powered interface as the likely cause. — [topic 444](https://community.rebeltech.org/t/new-owl-user-having-noise-in-my-sig-chain-when-connected-to-a-compuer-via-usb/444)
- **OWL Pedal 2017, dotnet555:** constant background noise. mars measured an OWL at about 97 dB SNR on a Rohde & Schwarz analyzer, so the noise floor should be very low. He listed levels, noisy PSU and ground loops as typical causes. He called the recorded noise "the high pitch buzz of a switching power supply", suspected a faulty unit and offered a return. — [topic 825](https://community.rebeltech.org/t/background-noise-problem/825)
- **Wizard 2018, maric:** high-pitched whine only when the Wizard is USB-powered and connected to an interface's inputs (two laptops, three interfaces). mars said he has seen hum like a ground loop **"modulated by the LED"** and would experiment with LED PWM. No result was posted. maric confirms timbre changes with LED colour. User Myql explains it as a resistive voltage drop across the USB cable ground, not a classic loop. — [topic 1104](https://community.rebeltech.org/t/wizard-ground-loop-problem/1104)
- **Magus 2019, mcc:** a "quite prominent buzzy hum", about 60 Hz-like, on the output when USB-powered from a MacBook. It was absent on the 9 V adapter. antisvin called this common with USB-powered audio devices, usually a ground loop. — [topic 1321](https://community.rebeltech.org/t/magus-patch-projects-log/1321)
- **Magus 2020, mcc:** USB-only power gives a very pronounced 60-cycle hum. DC only, or DC plus USB, is near-silent. A separate input hum remained even on DC. antisvin's unit also has noisy inputs on PSU, and he suggested a DC blocker since the Magus inputs are not AC-coupled. — [topic 1511](https://community.rebeltech.org/t/usb-isolator-with-magus/1511)
- **Magus 2021, charlesgershom:** unusable output noise floor regardless of power source. He tried a filtered laptop USB, 3 wall adapters, 3 battery banks, 2 DC PSUs and a boost converter. antisvin named USB power, the **OLED and PWM-controlled LEDs** as sources. He said mars had tried PWM changes that "caused other issues", and that the Kickstarter units have since had internal changes for power and noise. **Turning the LEDs off fixed it**, and the noise was acceptable even on USB power. — [topic 1703](https://community.rebeltech.org/t/output-noise-on-magus-please-help/1703)
- **Lich 2022:** high-pitched noise only when a desktop soundcard is connected. A passive audio isolator reduced it but muffled the sound. Unresolved. — [topic 1927](https://community.rebeltech.org/t/is-it-time-for-a-power-conditioner/1927)
- **Lich 2022, rabalan:** white or digital noise after a firmware update. It turned out to be mechanical or intermittent: pressing the OWL board stops it. mars suggested re-soldering the board-to-board joints and mentioned PSU noise. Unresolved. This one is not a ground issue. — [topic 1863](https://community.rebeltech.org/t/digital-noise-from-lich-after-firmware-update/1863)

### Inferences
- **Across the OWL family, the developer-acknowledged noise mechanisms are:**
  - USB VBUS/ground coupling with the host or interface, giving 50/60 Hz hum or switching whine
  - PWM LED and OLED current modulation
- The AC/DC 1 kHz comb fits neither cleanly. It is not 50/60 Hz. By my calculation from the timer settings, LED PWM is about 2.3 kHz (240 MHz / 101 / 1024), which also is not 1 kHz, though this is unverified on hardware. The best match is the USB Full-Speed 1 ms frame or packet cadence, which runs on the same board as the codec. That would also explain why it is present only while streaming over USB, and why host-side measures (battery, opto-isolator) don't remove it. This is unconfirmed.
- The AC/DC has no local power path that bypasses USB ground. It draws from the Eurorack rails, but its USB ground still ties to the host. The PCM3168A is a 24-bit codec run at 16-bit over USB, so 16-bit quantization alone would put the floor around -96 dBFS. The reported -30 dB is far above that and points to coupled interference, not codec resolution.

### Gaps
- The forum has no schematic-level discussion of AC/DC grounding, rail filtering or layout.
- I found no confirmed test of the AC/DC with LEDs dimmed or off. AC/DC firmware has no LED-brightness setting like the Magus has.
- Whether the comb tracks USB SOF (1 kHz) was never measured, for example by checking whether it disappears when the USB audio stream stops.

## 3. Did a USB ground isolator really help, and for whom? Does USB Full Speed matter?

### Takeaway
The evidence conflicts. On the AC/DC, atau (2023-04-01) said a USB opto-isolator did **not** help. Pauper (2023-11-01) said a "cheap ground isolator" made the noise disappear, but gave no model and didn't say whether it was a USB or an audio-line isolator. On siblings, USB isolators (Olimex USB-ISO, a generic isolator) fixed Wizard USB noise. On Magus, an Adafruit ADuM-based isolator either failed to power the unit or blocked USB data. The AC/DC is a **USB Full-Speed** device (STM32H7 OTG_FS, 4 in / 4 out, 16-bit, 48 kHz). ADuM3160/4160 Full-Speed isolators should therefore be bandwidth-compatible in principle, unlike with High-Speed interfaces such as the ES-8. Their current limit is less of an issue because the AC/DC takes its power from Eurorack. No AC/DC-specific report confirms audio streaming through a Full-Speed isolator.

### Cited Findings
- **atau, AC/DC:** "putting an opto-isolator inline with the USB" did not remove the artifact. Model and speed setting are not given, and he does not say audio failed, so presumably it streamed. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **Pauper, AC/DC, 2023-11-01:** "With a cheap ground isolator the noise desapears." He gives no model, type, USB speed or audio-function details. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **antisvin, 2022-11-28:** USB-sourced noise on the AC/DC "might be" fixable with a USB isolator. — [topic 2025](https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025)
- **Wizard, 2018:**
  - Myql: the **Olimex USB-ISO (~€30) removed the noise** and supplied enough power.
  - maric: a generic "3000 kV" USB-to-USB audio/power isolator **worked**.

  — [topic 1104](https://community.rebeltech.org/t/wizard-ground-loop-problem/1104)
- **Magus, 2020:**
  - The **Adafruit #2107 USB isolator** with USB power only: Magus didn't boot properly (insufficient power).
  - antisvin asked whether the **full-speed switch** was set. He said Magus draws about 200 mA (later measured about 450 mA), and that most cheap isolators use the same ADuM3160/4160 chips with limited current.
  - mars, with an Olimex isolator and no external power: the patch ran but the OLED stayed off.
  - mcc, with DC power plus USB through the Adafruit isolator: hum gone but the **Mac could not communicate** (no USB data).
  - The working fix was **DC adapter plus direct USB**, which developers confirmed is safe.

  — [topic 1511](https://community.rebeltech.org/t/usb-isolator-with-magus/1511)
- **antisvin, Magus 2019:** recommends an adaptor that takes power from one source and data from another, which he says fixes it "every time". He said a USB hub won't help. He also mentioned commercial ground loop isolators. — [topic 1321](https://community.rebeltech.org/t/magus-patch-projects-log/1321)
- **antisvin, Magus 2021:** warns that with a USB isolator, USB might not work or might not supply enough power. A powered splitter would be no quieter than the PSU. — [topic 1703](https://community.rebeltech.org/t/output-noise-on-magus-please-help/1703)
- **AC/DC USB mode:** `USE_USBD_FS`, `USB_OTG_FS` on PA11/PA12, 4 channels, 16-bit, 48 kHz. — [hardware.h](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Inc/hardware.h), [ACDC.ioc](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/ACDC.ioc)
- **Sample rate is fixed at 48 kHz.** On 2022-12-31 antisvin relayed mars's view that 44.1 kHz "might be possible, but would require a custom firmware build", with no progress since. — [topic 2042](https://community.rebeltech.org/t/44-1khz-sample-rate-possible/2042)

### Inferences
- **Bandwidth check (my calculation):** 4 ch × 48 kHz × 2 bytes = 384 kB/s, or 384 bytes per 1 ms frame per direction. That fits within one Full-Speed isochronous endpoint (max 1023 B/frame). So the AC/DC does not need High Speed, and an ADuM3160 isolator set to Full Speed should carry its audio. The ADuM3160's own speed limit (Low/Full only) is therefore not a blocker for the AC/DC. Users must set the isolator to FS, not LS. It is a blocker for the ES-8, which is High-Speed USB, but that is outside this forum and not sourced here.
- **Power is less of a concern for the AC/DC than for the Magus:** the module runs from Eurorack ±12 V (per Befaco specs), so a low-current isolated VBUS should not starve it. This is unverified; whether AC/DC firmware or hardware needs VBUS sensing (PA9 is configured as `USB_OTG_FS_VBUS`) and works with the isolator's VBUS was not reported.
- **Pauper vs atau conflict:** Pauper's success may reflect a classic host ground loop, which an isolator fixes, rather than atau's 1 kHz on-board comb, which survived an isolator and a battery-powered host. The two may be different noise problems. Pauper's "ground isolator" could also be an analog audio-line isolator on the outputs, though that is impossible to tell from the post.

### Gaps
- I found no AC/DC report naming an isolator model, its speed setting, or confirming that all 4×4 channels stream through it.
- I found no reports of isolators breaking AC/DC audio, and none confirming that they don't.

## 4. Official statements, hardware revisions or firmware fixes regarding noise

### Takeaway
I found no official Rebel Technology or Befaco statement, hardware revision or firmware change addressing AC/DC noise. mars acknowledged atau's levels as abnormal (2023-04) and promised measurements that never appeared. antisvin said in 2024 the noise is a hardware issue needing a redesign, and that the module appears discontinued with no RebelTech updates expected. Firmware activity on the AC/DC concerned USB functionality and sync (v22.5.0 in Mar 2023), not noise.

### Cited Findings
- **mars, 2023-04-04:** "definitely not normal". He promised noise-floor and SNR graphs, but none were posted. — [thread 2072](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **antisvin, 2024-11-14:** hardware problems including "that noise issue" "would require redesign to fix", and no RebelTech updates are expected soon. The AC/DC is absent from Befaco's product overview, but neither poster had seen an official announcement. — [topic 2244](https://community.rebeltech.org/t/ac-dc-as-fx-when-not-connected-to-computer/2244)
- **Firmware v22.5.0:** In early Mar 2023 the pre-release firmware had "improvements related to USB audio synchronization", and a stable release followed around 2023-03-05. — [topic 2069](https://community.rebeltech.org/t/sending-cv-via-acdc-patch-needed-or-something-else/2069)
  - The official v22.5.0 `ACDC.bin` "breaks USB". antisvin reported this to RebelTech/Befaco on 2023-04-03 ("a correct update is expected soon") and shared his own working build. — [topic 2083](https://community.rebeltech.org/t/ac-dc-firmware-update/2083), [thread 2072 #5](https://community.rebeltech.org/t/clock-noise-in-ac-dc/2072)
- **OpenWare master** is still at the "v22.5.0" commit dated 2023-03-05. I found no later AC/DC firmware commits on master. — [OpenWare repo](https://github.com/RebelTechnology/OpenWare)
- **Codec HPF:** A DC-blocking codec HPF exists but is disabled in the AC/DC build (DC-coupled design). Enabling it requires a custom firmware build. — [topic 2069](https://community.rebeltech.org/t/sending-cv-via-acdc-patch-needed-or-something-else/2069), [hardware.h](https://github.com/RebelTechnology/OpenWare/blob/master/ACDC/Core/Inc/hardware.h)
- **Sibling precedent:** on the Magus, antisvin says Kickstarter-era units later got internal changes for power and noise. He also says mars's LED-PWM experiments to reduce noise caused other issues. — [topic 1703](https://community.rebeltech.org/t/output-noise-on-magus-please-help/1703)
- **Sibling precedent:** the OWL Pedal has a hidden jumper that cuts USB VBUS. — [topic 444](https://community.rebeltech.org/t/new-owl-user-having-noise-in-my-sig-chain-when-connected-to-a-compuer-via-usb/444)

### Inferences
- Firmware alone is unlikely to fix the AC/DC comb if it is board-level coupling. A possible mitigation is changing LED PWM frequency or disabling LEDs in a custom build. It is plausible but untested for the AC/DC; the Magus precedent showed LEDs-off helped there.
- Firmware changes cannot fix a 1 kHz component from USB packet-cadence current draw. Only hardware filtering or grounding changes can.

### Gaps
- **GitHub issues** in the RebelTechnology repos could not be searched: GitHub API access for the repo was not enabled in this session, and the issue pages were not fetched.
- **ModWiggler, Reddit r/modular, Muffwiggler archive, YouTube:** web searches found no AC/DC noise discussions. Results were only shop listings, the [MusicRadar review (Rob Redman, 2022-10-03)](https://musicradar.com/reviews/befaco-acdc) (which does not mention noise; its con is "Limited patching IO"), and [Synthtopia](https://www.synthtopia.com/?p=129661) / [Synthanatomy](https://synthanatomy.com/2022/05/superbooth-22-befaco-ac-dc-an-open-source-4x4-audio-interface-for-eurorack.html) launch news. That is weak evidence of absence; these sites are poorly indexed by the search tool.
- Befaco support threads and email are not public. Befaco staff (Matt/Mattin) appear on the forum only regarding support contacts. — [topic 2025](https://community.rebeltech.org/t/befaco-ac-dc-not-recognized-anymore/2025)
