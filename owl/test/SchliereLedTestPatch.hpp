#ifndef __SCHLIERE_LED_TEST_PATCH_HPP__
#define __SCHLIERE_LED_TEST_PATCH_HPP__

/* Mess-Patch, kein Musik-Patch: Schliere mit unverändertem Klang, aber die Eingangs-LEDs
 * laufen nach der Uhr durch feste Zustände. Damit lässt sich am Ausgang messen, was die
 * LEDs selbst beitragen, ohne dass sich ein Regler oder der Abgriff bewegt (messlog D72:
 * In Schliere hängen LEDs und Abgriff beide an Regler 3).
 *
 * Ablauf, je PHASE_S Sekunden, beginnt beim Laden des Patches und wiederholt sich:
 *   0  alle aus                       Bezug
 *   1  LED 1 rot
 *   2  LED 1–3 rot
 *   3  LED 1–4 rot
 *   4  alle aus                       Bezug
 *   5  LED 1–3 blinken rot mit 40 Hz  wie ein Flackern an der Grenze einer Haltezone
 *   6  alle aus                       Bezug
 *   7  LED 1–3 grün mit 60 %          Gegenprobe: gedimmtes Grün fiepst nachweislich (D67)
 *
 * „Rot“ heißt in der Firmware Rot plus Grün mit Tastgrad 1023/1024 (messlog D72).
 * Die Anzeige von Schliere selbst wird überschrieben. Bauen:
 *   SRC=owl tools/build_owl_patch.sh SchliereLedTest SchliereLedTestPatch test/SchliereLedTestPatch.hpp
 */

#include "SchlierePatch.hpp"

class SchliereLedTestPatch : public SchlierePatch {
public:
  static constexpr float PHASE_S = 5.0f;
  static constexpr size_t PHASES = 8;
  static constexpr size_t FLICKER_BLOCKS = 75; // Blöcke je Halbperiode: 12,5 ms an, 12,5 ms aus
  static constexpr float RED = 1.0f;
  static constexpr float GREEN = 0.6f;

  void processAudio(AudioBuffer& buffer){
    SchlierePatch::processAudio(buffer);
    const size_t perPhase = (size_t)(PHASE_S * getSampleRate() / buffer.getSize());
    const size_t phase = block / perPhase;
    float led[4] = { 0.0f, 0.0f, 0.0f, 0.0f };
    switch(phase){
    case 1: led[0] = RED; break;
    case 2: led[0] = led[1] = led[2] = RED; break;
    case 3: led[0] = led[1] = led[2] = led[3] = RED; break;
    case 5: if(((block % perPhase) / FLICKER_BLOCKS) & 1) led[0] = led[1] = led[2] = RED; break;
    case 7: led[0] = led[1] = led[2] = GREEN; break;
    default: break;
    }
    for(int i = 0; i < 4; ++i)
      setParameterValue(PatchParameterId(PARAMETER_AA + i), led[i]);
    if(++block >= PHASES * perPhase)
      block = 0;
  }

private:
  size_t block = 0;
};

#endif // __SCHLIERE_LED_TEST_PATCH_HPP__
