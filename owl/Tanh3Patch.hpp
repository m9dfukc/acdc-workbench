#ifndef __TANH3_PATCH_HPP__
#define __TANH3_PATCH_HPP__

/* Tanh3: dreifacher tanh-Waveshaper für das AC/DC, nach dem Vorbild eines analogen
 * Eurorack-Moduls mit drei tanh-Kanälen (Waveshaper, Limiter, Overdrive,
 * Feedback-Zähmer), dazu ein Mix-Kanal (Nutzer-Wunsch 2026-11-17).
 *
 *   Kanal 1–3   Out n = SAT · tanh(Level n · In n / SAT)
 *               Regler n = Level (Eingangspegel vor dem tanh), 0,5-fach am Linksanschlag
 *               bis 16-fach am Rechtsanschlag, ≈ 2,8-fach bei 12 Uhr. Wie beim Vorbild
 *               wird der Kanal nie stumm.
 *   Kanal 4     Out 4 = SAT · tanh(Pegel · (Out 1 + Out 2 + Out 3) / SAT)
 *               Regler 4 = Pegel des Mix (0…1, linear)
 *               In 4 = CV auf den Pegel, addiert zum Regler: +5 V ≙ voller Regelweg,
 *               negative Spannung nimmt Pegel weg. Wirkt pro Sample (VCA bis Audio-Rate).
 *               Unter ±0,5 V ist die CV tot, damit der offene Eingang (Offset
 *               −0,2…−0,4 V, D36) den Pegel nicht verschiebt.
 *
 * Pegel: 1.0 = Vollausschlag ≈ 10 V. SAT = 0.5: Die Ausgänge sättigen bei ±5 V (10 Vpp).
 * Kleine Signale laufen bei Level 1 unverändert durch. Alles ist DC-gekoppelt, taugt
 * also auch für CV.
 *
 * Nicht nachgebildet: die Normalisierung der Eingänge (oben → Mitte → unten). Das AC/DC
 * erkennt nicht, ob ein Kabel steckt.
 *
 * Aliasing: tanh erzeugt bei hohem Level Obertöne über fs/2, die als unharmonische
 * Linien in den Hörbereich zurückfallen. Die erste Fassung rechnete mit Antiderivative
 * Antialiasing erster Ordnung (wie Nonlinearity.hpp von burstMembrane/acdc-patches).
 * Das reichte nicht: 3 kHz bei 6,7-fachem Level ergab −37 dB Fremdlinien unter 15 kHz,
 * hörbar als „digitale“ Störgeräusche (Nutzer, messlog D56). Jetzt läuft jeder Kanal
 * mit vierfachem Oversampling: FIR hoch auf 192 kHz (Polyphase), tanh, FIR herunter.
 * Derselbe Fall liegt damit bei −98 dB. Preis: ≈ 0,25 ms Laufzeit (11,75 Samples, für
 * alle Kanäle gleich) und mehr Rechenlast. Bei hart angefahrenen, hellen Signalen schwingt der
 * bandbegrenzte Ausgang bis ≈ 10 % über SAT hinaus.
 *
 * LEDs (ohne USB-Aufnahme): Eingangs-LED n = Ausgangspegel des Kanals relativ zu SAT,
 * Rot = tief in der Sättigung (tanh-Argument über 2,5).
 *
 * basicmaths.h ersetzt expf() durch Tabellen-Näherungen. (expf)(x) in Klammern ruft
 * die genaue libm-Funktion.
 */

#include "Patch.h"
#include <math.h>

#ifndef TANH3_TAPS
#define TANH3_TAPS 48 // Länge des FIR bei 192 kHz, Vielfaches von 4 (64 bringt kaum mehr, D56)
#endif

class Tanh3Patch : public Patch {
  static constexpr float SAT = 0.5f;            // Sättigungspegel, 5 V
  static constexpr float LEVEL_MIN = 0.5f;      // Level am Linksanschlag
  static constexpr float LEVEL_LN_RANGE = 3.4657359f; // ln(32): 0,5 … 16
  static constexpr float SLEW = 0.002f;         // Regler-Glättung pro Sample, τ ≈ 10 ms
  static constexpr float KNOB_DEAD = 0.03f;     // der Linksanschlag liest ≈ 0,016–0,023 (D51)
  static constexpr float CV_DEAD = 0.05f;       // 0,5 V
  static constexpr float CV_SCALE = 2.0f;       // 5 V ≙ 1,0
  static constexpr size_t OS = 4;               // Oversampling
  static constexpr size_t TAPS = TANH3_TAPS;
  static constexpr size_t UP_TAPS = TAPS / OS;  // Abgriffe je Polyphase
  static constexpr float CUTOFF = 22000.0f / 192000.0f; // Grenzfrequenz relativ zur hohen Rate
  static constexpr float KAISER_BETA = 9.0f;
  static constexpr float RED_DRIVE = 2.5f;
  static constexpr float LED_DECAY = 0.995f;    // pro Block

  /* tanh als Kettenbruch (Lambert, 7. Ordnung). Bei |x| = 4,97 erreicht die Näherung genau 1,
   * darüber gilt ±1: stetig, monoton, Fehler unter 1e-4 (unter 1e-6 bis |x| = 3).
   * Läuft viermal pro Sample und Kanal, deshalb nicht tanhf(). */
  static float fastTanh(float x){
    if(x > 4.97f) return 1.0f;
    if(x < -4.97f) return -1.0f;
    const float x2 = x * x;
    const float num = x * (135135.0f + x2 * (17325.0f + x2 * (378.0f + x2)));
    const float den = 135135.0f + x2 * (62370.0f + x2 * (3150.0f + x2 * 28.0f));
    return num / den;
  }

  /* Filterkoeffizienten, einmal im Konstruktor berechnet: Kaiser-gefensterter Tiefpass.
   * up[p][k]: Polyphase p, je auf Summe 1 normiert (Gleichspannung bleibt exakt gleich).
   * down[j]: derselbe Tiefpass, Summe 1. */
  float up[OS][UP_TAPS];
  float down[TAPS];

  static float besselI0(float x){
    float sum = 1.0f, term = 1.0f;
    for(int k = 1; k < 25; ++k){
      term *= (x / (2.0f * k)) * (x / (2.0f * k));
      sum += term;
    }
    return sum;
  }
  void designFilters(){
    float h[TAPS];
    const float mid = 0.5f * (TAPS - 1);
    for(size_t n = 0; n < TAPS; ++n){
      const float t = n - mid;
      const float arg = 2.0f * 3.14159265f * CUTOFF * t;
      const float sinc = fabsf(t) < 1e-6f ? 1.0f : (sinf)(arg) / arg;
      const float r = t / mid;
      h[n] = sinc * besselI0(KAISER_BETA * (sqrtf)(1.0f - r * r)) / besselI0(KAISER_BETA);
    }
    float total = 0.0f;
    for(size_t n = 0; n < TAPS; ++n) total += h[n];
    for(size_t n = 0; n < TAPS; ++n) down[n] = h[n] / total;
    for(size_t p = 0; p < OS; ++p){
      float sum = 0.0f;
      for(size_t k = 0; k < UP_TAPS; ++k) sum += h[p + OS * k];
      for(size_t k = 0; k < UP_TAPS; ++k) up[p][k] = h[p + OS * k] / sum;
    }
  }

  /* Ein Kanal: Eingangs- und Ausgangsgedächtnis als doppelt beschriebene Ringe, damit die
   * Skalarprodukte über einen zusammenhängenden Bereich laufen. x in Einheiten von SAT. */
  struct Shaper {
    float in[2 * UP_TAPS] = {};
    float hi[2 * TAPS] = {};
    size_t inPos = 0;
    size_t hiPos = 0;
    float process(float x, const float (*up)[UP_TAPS], const float* down){
      inPos = inPos == 0 ? UP_TAPS - 1 : inPos - 1;
      in[inPos] = in[inPos + UP_TAPS] = x; // in[inPos + k] = x vor k Samples
      const float* xi = in + inPos;
      for(size_t p = 0; p < OS; ++p){
        float acc = 0.0f;
        for(size_t k = 0; k < UP_TAPS; ++k)
          acc += up[p][k] * xi[k];
        hiPos = hiPos == 0 ? TAPS - 1 : hiPos - 1;
        hi[hiPos] = hi[hiPos + TAPS] = fastTanh(acc);
      }
      const float* z = hi + hiPos;
      float out = 0.0f;
      for(size_t j = 0; j < TAPS; ++j)
        out += down[j] * z[j];
      return out;
    }
  };

  Shaper shaper[4];
  float level[3] = { 1.0f, 1.0f, 1.0f };
  float mixLevel = 0.0f;
  float led[4] = {};
  size_t channels;

public:
  Tanh3Patch(){
    channels = getNumberOfChannels();
    registerParameter(PARAMETER_A, "Level 1");
    registerParameter(PARAMETER_B, "Level 2");
    registerParameter(PARAMETER_C, "Level 3");
    registerParameter(PARAMETER_D, "Mix");
    designFilters();
  }

  void processAudio(AudioBuffer& buffer){
    if(channels < 4)
      return; // nur für das AC/DC gedacht
    const size_t size = buffer.getSize();
    FloatArray io[4] = { buffer.getSamples(0), buffer.getSamples(1),
                         buffer.getSamples(2), buffer.getSamples(3) };
    float target[3];
    for(size_t ch = 0; ch < 3; ++ch)
      target[ch] = LEVEL_MIN * (expf)(LEVEL_LN_RANGE * getParameterValue(PatchParameterId(PARAMETER_A + ch)));
    float mixTarget = (getParameterValue(PARAMETER_D) - KNOB_DEAD) / (1.0f - 2.0f * KNOB_DEAD);
    mixTarget = mixTarget < 0.0f ? 0.0f : (mixTarget > 1.0f ? 1.0f : mixTarget);

    float peak[4] = {};
    float drive[4] = {};
    for(size_t i = 0; i < size; ++i){
      float sum = 0.0f;
      for(size_t ch = 0; ch < 3; ++ch){
        level[ch] += (target[ch] - level[ch]) * SLEW;
        const float x = io[ch][i] * level[ch] * (1.0f / SAT);
        const float y = SAT * shaper[ch].process(x, up, down);
        io[ch][i] = y;
        sum += y;
        if(fabsf(x) > drive[ch]) drive[ch] = fabsf(x);
        if(fabsf(y) > peak[ch]) peak[ch] = fabsf(y);
      }
      mixLevel += (mixTarget - mixLevel) * SLEW;
      float cv = io[3][i];
      cv = cv > CV_DEAD ? cv - CV_DEAD : (cv < -CV_DEAD ? cv + CV_DEAD : 0.0f);
      float gain = mixLevel + CV_SCALE * cv;
      gain = gain < 0.0f ? 0.0f : (gain > 1.0f ? 1.0f : gain);
      const float x = sum * gain * (1.0f / SAT);
      const float y = SAT * shaper[3].process(x, up, down);
      io[3][i] = y;
      if(fabsf(x) > drive[3]) drive[3] = fabsf(x);
      if(fabsf(y) > peak[3]) peak[3] = fabsf(y);
    }

    for(size_t ch = 0; ch < 4; ++ch){
      float value = peak[ch] * (0.97f / SAT);
      if(value > 0.97f) value = 0.97f;
      led[ch] = value > led[ch] * LED_DECAY ? value : led[ch] * LED_DECAY;
      setParameterValue(PatchParameterId(PARAMETER_AA + ch), drive[ch] > RED_DRIVE ? 1.0f : led[ch]);
    }
  }
};

#endif // __TANH3_PATCH_HPP__
