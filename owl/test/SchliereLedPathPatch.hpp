#ifndef __SCHLIERE_LED_PATH_PATCH_HPP__
#define __SCHLIERE_LED_PATH_PATCH_HPP__

/* Mess-Patch, kein Musik-Patch: Wo entsteht die Verschiebung, die der LED-Strom am
 * Ausgang hinterlässt (messlog D73)? Am Eingang (ADC), von wo ein Patch sie durchreicht,
 * oder erst am Ausgang (DAC, Ausgangsstufe)?
 *
 * Ablauf, je PHASE_S Sekunden, beginnt beim Laden des Patches und wiederholt sich:
 *   0  Schliere wie auf Slot 6, LEDs aus      Bezug
 *   1  Schliere, LED 1–3 blinken mit 40 Hz    wie D73
 *   2  Ausgänge digital null, LEDs aus        Bezug
 *   3  Ausgänge null, LED 1–3 blinken         bleibt das Blinken, entsteht es am Ausgang
 *   4  Ausgänge null, LEDs aus
 *   5  Ausgänge null, LED 1–4 rot             Sprung beim Ein- und Ausschalten
 *   6  Ausgänge null, LEDs aus
 *   7  Ausgänge null, an Out 1 ein Eichton    CAL_HZ mit Amplitude CAL_LEVEL, LEDs aus
 *   8  alle Ausgänge = GAIN × In 1, LEDs aus  Bezug
 *   9  GAIN × In 1, LED 1–3 blinken           wächst das Blinken mit GAIN, entsteht es am Eingang
 *
 * Dazu misst der Patch selbst am Eingang, in Einheiten von 1e-7 Vollausschlag (1 ≙ 1 µV
 * bei ±10 V), und meldet es als Debug-Meldung (tools/owl_read.py zeigt die letzte):
 *   „LEDblink In1-3“  nach Phase 3: Mittel der rohen Eingänge 1–3 bei LED an minus LED aus,
 *                     ohne die ersten 4 ms nach jedem Wechsel, über alle Durchläufe
 *   „LEDstat In1-3“   nach Phase 6: Mittel in Phase 5 minus Mittel der Phasen 4 und 6,
 *                     je ohne die erste Sekunde, letzter Durchlauf
 * In den Phasen 2–7 liegt am Ausgang kein Signal, das auf die Eingänge übersprechen könnte.
 *
 * „Rot“ heißt in der Firmware Rot plus Grün mit Tastgrad 1023/1024 (messlog D72). Bauen:
 *   SRC=owl tools/build_owl_patch.sh SchliereLedPath SchliereLedPathPatch test/SchliereLedPathPatch.hpp
 */

#include "../schliere/SchlierePatch.hpp"

void debugMessage(const char* msg, int, int, int); // message.h des SDK, im Host-Test ein Ersatz

class SchliereLedPathPatch : public SchlierePatch {
public:
  static constexpr float PHASE_S = 5.0f;
  static constexpr size_t PHASES = 10;
  static constexpr size_t FLICKER_BLOCKS = 75; // Blöcke je Halbperiode: 12,5 ms an, 12,5 ms aus
  static constexpr size_t SKIP_BLOCKS = 24;    // 4 ms nach jedem Wechsel nicht messen
  static constexpr float SETTLE_S = 1.0f;      // statische Messung: erste Sekunde jeder Phase auslassen
  static constexpr float GAIN = 4.0f;
  static constexpr float CAL_HZ = 300.0f;
  static constexpr float CAL_LEVEL = 0.001f;   // −60 dBFS ≙ 10 mV Spitze an Out 1
  static constexpr float RED = 1.0f;
  static constexpr size_t MAX_BLOCK = 64;

  void processAudio(AudioBuffer& buffer){
    const size_t size = buffer.getSize();
    const float sr = getSampleRate();
    const size_t perPhase = (size_t)(PHASE_S * sr / size);
    const size_t phase = block / perPhase, inPhase = block % perPhase;
    const bool blink = phase == 1 || phase == 3 || phase == 9;
    const bool on = blink && ((inPhase / FLICKER_BLOCKS) & 1);
    FloatArray io[4] = { buffer.getSamples(0), buffer.getSamples(1),
                         buffer.getSamples(2), buffer.getSamples(3) };

    // Messung am Eingang, vor allem anderen: Die Ausgänge überschreiben die Puffer
    float sum[3] = { 0.0f, 0.0f, 0.0f };
    for(size_t ch = 0; ch < 3; ++ch)
      for(size_t i = 0; i < size; ++i)
        sum[ch] += io[ch][i];
    if(phase == 3 && inPhase % FLICKER_BLOCKS >= SKIP_BLOCKS){
      for(size_t ch = 0; ch < 3; ++ch) blinkSum[on][ch] += sum[ch];
      blinkCount[on] += size;
    }
    if(phase >= 4 && phase <= 6 && inPhase >= (size_t)(SETTLE_S * sr / size)){
      if(phase == 4 && inPhase == (size_t)(SETTLE_S * sr / size))
        for(size_t n = 0; n < 2; ++n){ statCount[n] = 0; for(size_t ch = 0; ch < 3; ++ch) statSum[n][ch] = 0.0; }
      const size_t lit = phase == 5;
      for(size_t ch = 0; ch < 3; ++ch) statSum[lit][ch] += sum[ch];
      statCount[lit] += size;
    }
    float dry[MAX_BLOCK];
    const size_t n = size < MAX_BLOCK ? size : MAX_BLOCK;
    for(size_t i = 0; i < n; ++i) dry[i] = io[0][i];

    SchlierePatch::processAudio(buffer);

    if(phase >= 2 && phase <= 7){
      for(size_t ch = 0; ch < 4; ++ch)
        for(size_t i = 0; i < size; ++i) io[ch][i] = 0.0f;
      if(phase == 7){
        for(size_t i = 0; i < size; ++i){
          io[0][i] = CAL_LEVEL * (sinf)(calPhase);
          calPhase += 2.0f * 3.14159265f * CAL_HZ / sr;
          if(calPhase > 2.0f * 3.14159265f) calPhase -= 2.0f * 3.14159265f;
        }
      }
    }else if(phase >= 8){
      for(size_t ch = 0; ch < 4; ++ch)
        for(size_t i = 0; i < n; ++i) io[ch][i] = GAIN * dry[i];
    }

    float led[4] = { 0.0f, 0.0f, 0.0f, 0.0f };
    if(on) led[0] = led[1] = led[2] = RED;
    if(phase == 5) led[0] = led[1] = led[2] = led[3] = RED;
    for(int i = 0; i < 4; ++i)
      setParameterValue(PatchParameterId(PARAMETER_AA + i), led[i]);

    if(inPhase == perPhase - 1){
      if(phase == 3 && blinkCount[0] && blinkCount[1])
        debugMessage("LEDblink In1-3", unit(blinkSum[1][0] / blinkCount[1] - blinkSum[0][0] / blinkCount[0]),
                     unit(blinkSum[1][1] / blinkCount[1] - blinkSum[0][1] / blinkCount[0]),
                     unit(blinkSum[1][2] / blinkCount[1] - blinkSum[0][2] / blinkCount[0]));
      if(phase == 6 && statCount[0] && statCount[1])
        debugMessage("LEDstat In1-3", unit(statSum[1][0] / statCount[1] - statSum[0][0] / statCount[0]),
                     unit(statSum[1][1] / statCount[1] - statSum[0][1] / statCount[0]),
                     unit(statSum[1][2] / statCount[1] - statSum[0][2] / statCount[0]));
    }
    if(++block >= PHASES * perPhase)
      block = 0;
  }

private:
  static int unit(double x){ // in 1e-7 Vollausschlag, gerundet
    const double v = x * 1e7;
    return (int)(v < 0.0 ? v - 0.5 : v + 0.5);
  }
  double blinkSum[2][3] = {}, statSum[2][3] = {};
  size_t blinkCount[2] = {}, statCount[2] = {};
  float calPhase = 0.0f;
  size_t block = 0;
};

#endif // __SCHLIERE_LED_PATH_PATCH_HPP__
