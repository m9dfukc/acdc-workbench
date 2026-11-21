#ifndef __SCHLIERE_L_PATCH_HPP__
#define __SCHLIERE_L_PATCH_HPP__

/* Schliere L (lang): SchliereS mit einer Kette aus 160 statt 61 Stufen (320 statt 122 Pole).
 * Wunsch des Nutzers (2026-11-21): mindestens so viele Stufen wie das Vorbild. Laut dessen
 * Handbuch (v1.2.1) hat eine Sektion 2 bis 98 Pole, mit der Config-Datei bis 160 Pole, und im
 * Normalbetrieb laufen beide Sektionen in Reihe. Das Maximum sind damit 320 Pole je Kanal,
 * hier am Ende der Kette (R und Tail) erreicht.
 *
 *   Out 1 (L)  Abgriffe 2, 44, 86, 128, 170, 212, 254 Pole (Stufen 1, 22 … 127, je 21)
 *   Out 2 (R)  Abgriffe 2, 56, 108, 162, 214, 268, 320 Pole (Stufen 1, 28, 54, 81, 107, 134, 160,
 *              abwechselnd 27 und 26 Stufen Abstand)
 *   Out 4      Tail = Ende der Kette, 320 Pole
 *
 * L und R stehen wie bei den anderen Varianten etwa im Verhältnis 4 : 5. Die Abstände der
 * Abgriffe sind 2,6-mal so groß: Zwischen zwei Rastpunkten entstehen an L 21 Kerben statt 8,
 * an R 26 oder 27 statt 10 (je 2 Pole Abstand eine Kerbe). Laufzeit an jedem Abgriff
 * proportional zur Zahl der Pole: bei 1 kHz und Q 16 rund 10,2 ms je Stufe, also 1,3 s an L
 * und 1,6 s an R (SchliereS: 0,5 und 0,6 s).
 *
 * Sonst wie SchliereS: Feedback-CV an In 4 leicht geglättet (zwei Tiefpässe mit je 12 kHz),
 * Eingang der Kette mit 96 kHz (Halbband aus SchliereOPatch.hpp), Tap-Glättung, Ausgänge
 * und LEDs aus SchliereBase. Die Klasse ist eigenständig, damit SchliereO und SchliereS
 * bytegleich mit ihren Slots bleiben (schon ein Template ändert deren Binary). Die Länge
 * steht hier fest, nicht über SCHLIERE_STAGES, so können alle Varianten in einem Host-Test
 * nebeneinander laufen.
 *
 * Rechenlast am Gerät 70 % (SchliereS: 39 %, messlog D81). Geschätzt waren aus D80 etwa
 * 0,43 % je Stufe, also rund 82 %.
 */

#include "SchliereOPatch.hpp"

#ifndef SCHLIERE_S_HZ
#define SCHLIERE_S_HZ 12000.0f // Grenzfrequenz je Pol, wie SchliereSPatch
#endif

class SchliereLPatch : public SchliereBase {
public:
  static constexpr size_t LONG = 160; // Länge der Kette in Stufen
private:
  float state[2 * LONG] = {};
  float node[LONG + 1] = {};
  float w1[TAPS] = {}, w2[TAPS] = {};
  SchliereUp2x upIn, upCv, upLoop;
  SchliereDown2x down;
  float s1 = 0.0f, s2 = 0.0f; // Zustand der beiden Tiefpässe für In 4 (wie SchliereS)
  float cvG;
  bool cvStarted = false;

  /* Eingang der Kette mit 96 kHz (wie SchliereO) */
  float chainInput2x(float in1, float cv4){
    fbKnob += (targetFb - fbKnob) * slewSample;
    float in[2], cv[2], lp[2], x[2];
    upIn.process(inputClean.process(in1), in[0], in[1]);
    upCv.process(cv4, cv[0], cv[1]);
    upLoop.process(loopState, lp[0], lp[1]);
    float fb = 0.0f;
    for(int h = 0; h < 2; ++h){
      fb = FB_MAX * soft(fbKnob + CV_SCALE * deadzone(cv[h]), FB_KNEE, 1.0f);
      x[h] = (sqrtf)(1.0f - fb * fb) * in[h] + fb * lp[h];
    }
    fbNow = fb;
    return down.process(x[0], x[1]);
  }

public:
  SchliereLPatch(){
    const float gs = (tanf)(3.14159265f * SCHLIERE_S_HZ / getSampleRate());
    cvG = gs / (1.0f + gs);
  }

  void processAudio(AudioBuffer& buffer){
    if(channels < 4)
      return; // nur für das AC/DC gedacht
    static const uint8_t tapsL[TAPS] = { 1, 22, 43, 64, 85, 106, 127 };
    static const uint8_t tapsR[TAPS] = { 1, 28, 54, 81, 107, 134, 160 };
    static_assert(LONG >= 160 && LONG < 256, "Abgriffe passen nicht zur Länge der Kette");
    const size_t size = buffer.getSize();
    FloatArray io[4] = { buffer.getSamples(0), buffer.getSamples(1),
                         buffer.getSamples(2), buffer.getSamples(3) };

    // Feedback-CV leicht glätten (wie SchliereS), bevor beginBlock die Eingänge liest
    if(!cvStarted && size > 0){
      s1 = s2 = io[3][0];
      cvStarted = true;
    }
    for(size_t i = 0; i < size; ++i)
      io[3][i] = lowpass(lowpass(io[3][i], s1, cvG), s2, cvG);

    bool first = beginBlock(io, size);

    for(size_t i = 0; i < size; ++i){
      stepCoefficients();
      float x = chainInput2x(io[0][i], io[3][i]);

      node[0] = x;
      float* s = state;
      for(size_t n = 1; n <= LONG; ++n, s += 2){
        x = stage(x, s, a1, a2, g, c);
        node[n] = x;
      }

      // Abgriffe: Haltezone, S-Kurve, Gewichte über zwei Tiefpässe (wie SchliereO)
      const float u = tapPosition(io[2][i]);
      const int index = u >= (float)(TAPS - 1) ? (int)TAPS - 2 : (int)u;
      float t = clamp((u - index - HOLD) / (1.0f - 2.0f * HOLD), 0.0f, 1.0f);
      t = t * t * (3.0f - 2.0f * t);
      float left = 0.0f, right = 0.0f;
      for(int j = 0; j < (int)TAPS; ++j){
        const float target = j == index ? 1.0f - t : (j == index + 1 ? t : 0.0f);
        if(first)
          w1[j] = w2[j] = target;
        const float w = lowpass(lowpass(target, w1[j], modG), w2[j], modG);
        left += w * node[tapsL[j]];
        right += w * node[tapsR[j]];
      }
      first = false;

      outputs(io, i, left, right, 0.5f * (left - right), node[LONG]);
    }

    if(resetIfBroken(io, size, node[LONG])){
      for(size_t n = 0; n < 2 * LONG; ++n) state[n] = 0.0f;
      for(size_t n = 0; n <= LONG; ++n) node[n] = 0.0f;
      upIn = SchliereUp2x(); upCv = SchliereUp2x(); upLoop = SchliereUp2x(); down = SchliereDown2x();
    }
    leds(size);
  }
};

#endif // __SCHLIERE_L_PATCH_HPP__
