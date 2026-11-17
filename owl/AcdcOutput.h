#ifndef __ACDC_OUTPUT_H__
#define __ACDC_OUTPUT_H__

/* Ausgangsstufe für FX-Patches auf dem AC/DC: Limiter auf den Audio-Ausgängen 1/2.
 *
 * Anlass (Nutzer, 2026-11-17): Manche Patches übersteuern am Ausgang, z. B. Grainz
 * (überlappende Grains, Feedback). Der DAC kappt bei Vollausschlag hart.
 *
 * Aufbau:
 *   1. Spitzenwert-Limiter, beide Kanäle gekoppelt (das Stereobild bleibt stehen):
 *      Hüllkurve über max(|L|, |R|), Anstieg 1 ms, Abfall 150 ms. Liegt sie über
 *      THRESHOLD, wird auf THRESHOLD heruntergeregelt. Darunter bleibt das Signal
 *      unverändert.
 *   2. Weiche Kennlinie für das, was in der Anstiegszeit durchrutscht: ab THRESHOLD
 *      biegt ein tanh-Knie ab, über CEILING kommt nichts hinaus.
 *
 * Pegel: 1.0 = Vollausschlag ≈ 10 V Spitze am Ausgang (AUDIO_OUTPUT_GAIN 125).
 * THRESHOLD 0.5 = 5 V Spitze = 10 Vpp, der übliche Eurorack-Audiopegel.
 *
 * Die Kanäle 3/4 bleiben unberührt, die FX-Patches geben dort CV aus.
 *
 * Einbinden ohne Eingriff in fremde Quellen: AcdcLimited<XyzPatch> erbt vom Patch und
 * hängt den Limiter hinter processAudio(). tools/build_owl_patch.sh erzeugt die Hülle
 * mit LIMIT=1.
 *
 * basicmaths.h ersetzt expf() durch eine Tabellen-Näherung. (expf)(x) in Klammern ruft
 * die genaue libm-Funktion.
 */

#include "Patch.h"
#include <math.h>

class AcdcOutputLimiter {
public:
  static constexpr float THRESHOLD = 0.5f;
  static constexpr float CEILING = 0.75f;
  static constexpr float ATTACK_S = 0.001f;
  static constexpr float RELEASE_S = 0.150f;

  void setSampleRate(float sr){
    attack = 1.0f - (expf)(-1.0f / (ATTACK_S * sr));
    release = 1.0f - (expf)(-1.0f / (RELEASE_S * sr));
  }

  void process(FloatArray left, FloatArray right){
    const size_t size = left.getSize();
    for(size_t i = 0; i < size; ++i){
      float l = left[i];
      float r = right[i];
      // NaN oder Unsinn aus dem Patch: stumm statt hängender Hüllkurve (je Kanal prüfen,
      // ein Vergleich mit NaN ist immer falsch)
      if(!(fabsf(l) < 100.0f))
        l = 0.0f;
      if(!(fabsf(r) < 100.0f))
        r = 0.0f;
      const float peak = fabsf(l) > fabsf(r) ? fabsf(l) : fabsf(r);
      envelope += (peak - envelope) * (peak > envelope ? attack : release);
      if(envelope > THRESHOLD){
        const float gain = THRESHOLD / envelope;
        l *= gain;
        r *= gain;
      }
      left[i] = knee(l);
      right[i] = knee(r);
    }
  }

  /* linear bis THRESHOLD, darüber tanh-Knie mit Asymptote CEILING */
  static float knee(float x){
    const float a = fabsf(x);
    if(a <= THRESHOLD)
      return x;
    const float range = CEILING - THRESHOLD;
    const float y = THRESHOLD + range * (tanhf)((a - THRESHOLD) / range);
    return x < 0.0f ? -y : y;
  }

private:
  float envelope = 0.0f;
  float attack = 0.0206f;   // 1 ms bei 48 kHz
  float release = 0.000139f; // 150 ms bei 48 kHz
};

template<class BasePatch>
class AcdcLimited : public BasePatch {
public:
  AcdcLimited(){
    limiter.setSampleRate(this->getSampleRate());
  }
  void processAudio(AudioBuffer& buffer) override {
    BasePatch::processAudio(buffer);
    if(buffer.getChannels() >= 2)
      limiter.process(buffer.getSamples(0), buffer.getSamples(1));
  }
private:
  AcdcOutputLimiter limiter;
};

#endif // __ACDC_OUTPUT_H__
