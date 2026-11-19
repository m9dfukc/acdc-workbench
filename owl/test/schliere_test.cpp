// Host-Test für owl/SchlierePatch.hpp: Übertragungsfunktion aus der Impulsantwort,
// geprüft gegen die Zahlen aus dem Handbuch des Vorbilds und gegen die Rechnung.
#include "SchlierePatch.hpp"
#include <cmath>
#include <complex>
#include <cstdio>
#include <functional>
static int fails;
static void check(const char* name, bool ok, double a, double b = 0){ printf("%-4s %-66s %10.5f %10.5f\n", ok ? "ok" : "FAIL", name, a, b); if(!ok) fails++; }
static const double PI = 3.14159265358979, FS = 48000;
typedef std::complex<double> cplx;
typedef std::vector<std::vector<float>> Out;

// Lässt den Patch über n Samples laufen (Blöcke zu 8) und gibt alle vier Ausgänge zurück
static Out run(Patch& p, size_t n, std::function<double(int, size_t)> in){
  Out out(4);
  for(size_t t = 0; t < n; t += 8){
    AudioBuffer b; b.ch.assign(4, std::vector<float>(8));
    for(size_t i = 0; i < 8; ++i) for(int c = 0; c < 4; ++c) b.ch[c][i] = (float)in(c, t + i);
    p.processAudio(b);
    for(int c = 0; c < 4; ++c) out[c].insert(out[c].end(), b.ch[c].begin(), b.ch[c].end());
  }
  return out;
}
// Regler: Stellung 0…1 nach Abzug der Totzone am Anschlag
static float raw(double x){ return (float)(0.03 + 0.94 * x); }
static double freqKnob(double hz){ return 0.5 + std::log(hz / 632.4555) / std::log(2000.0); }
static double tapKnob(double point){ return (point - 1.0) / 6.0; } // Rastpunkt 1…7, 4.5 = zwischen 4 und 5
static void set(Patch& p, double hz, double q, double point, double fb){
  p.params[PARAMETER_A] = raw(freqKnob(hz)); p.params[PARAMETER_B] = raw(q);
  p.params[PARAMETER_C] = raw(tapKnob(point)); p.params[PARAMETER_D] = raw(fb / 0.97); }
static const size_t T0 = 64; // Zeitpunkt des Impulses
// Impulsantwort der Länge n auf In 1, cv = feste Werte an In 2…4
static Out impulse(Patch& p, size_t n, double amp, double cv2 = 0, double cv3 = 0, double cv4 = 0){
  return run(p, T0 + n, [&](int c, size_t t){ return c == 0 ? (t == T0 ? amp : 0.0) : (c == 1 ? cv2 : (c == 2 ? cv3 : cv4)); });
}
static cplx response(const std::vector<float>& y, double f, double amp){
  cplx acc = 0; const cplx step = std::polar(1.0, -2 * PI * f / FS); cplx w = 1;
  for(size_t i = T0; i < y.size(); ++i){ acc += (double)y[i] * w; w *= step; }
  return acc / amp;
}
static double db(double x){ return 20 * std::log10(x + 1e-30); }
static double groupDelay(const std::vector<float>& y, double f, double amp){
  const double df = 0.1; double d = std::arg(response(y, f + df, amp) / response(y, f - df, amp));
  return -d / (2 * PI * 2 * df);
}
// Allpass 2. Ordnung nach der Lehrbuchformel (bilineare Transformation mit Vorverzerrung)
static cplx reference(double f, double f0, double q, int stages){
  const double w0 = 2 * PI * f0 / FS, al = std::sin(w0) / (2 * q); const cplx z = std::polar(1.0, -2 * PI * f / FS);
  const cplx h = ((1 - al) - 2 * std::cos(w0) * z + (1 + al) * z * z) / ((1 + al) - 2 * std::cos(w0) * z + (1 - al) * z * z);
  return std::pow(h, stages);
}
static double peak(const std::vector<float>& v, size_t from = 0){ double m = 0; for(size_t i = from; i < v.size(); ++i) m = std::fmax(m, std::fabs(v[i])); return m; }
static bool finite(const Out& o){ for(auto& c : o) for(float x : c) if(!std::isfinite(x)) return false; return true; }
static int notches(const std::vector<float>& y, double amp, double limitDb){
  int count = 0; const int points = 6000; std::vector<double> m(points);
  for(int i = 0; i < points; ++i) m[i] = db(std::abs(response(y, 20 * std::pow(1000.0, (double)i / (points - 1)), amp)));
  for(int i = 1; i + 1 < points; ++i) if(m[i] < m[i-1] && m[i] <= m[i+1] && m[i] < limitDb) count++;
  return count;
}

int main(){
  const double A = 0.25;
  { // eine Stufe: Betrag und Phase wie die Lehrbuchformel, für alle Stützpunkte des Resonance-Reglers
    const double knobs[5] = { 0, 0.25, 0.5, 0.75, 1 }, qs[5] = { 0.01, 0.026, 0.51, 3.81, 16 }; double err = 0;
    for(int i = 0; i < 5; ++i){ SchlierePatch p; set(p, 1000, knobs[i], 1, 0); auto o = impulse(p, 96000, A);
      for(double f : { 300.0, 900.0, 1000.0, 1150.0, 4000.0 }) err = std::fmax(err, std::abs(response(o[0], f, A) - reference(f, 1000, qs[i], 1))); }
    check("one stage matches the textbook allpass for Q 0.01 … 16 (max error)", err < 2e-3, err); }
  { // Rastpunkt 7, kein Feedback: alle Frequenzen gleich laut, an L, R und Tail
    SchlierePatch p; set(p, 1000, 0.5, 7, 0); auto o = impulse(p, 16384, A); double dev = 0;
    for(int c : { 0, 1, 3 }) for(double f : { 30.0, 200.0, 1000.0, 3000.0, 15000.0 }) dev = std::fmax(dev, std::fabs(db(std::abs(response(o[c], f, A)))));
    check("top tap, no feedback: level flat at L, R and tail (max deviation, dB)", dev < 0.01, dev);
    double err = std::abs(response(o[0], 700, A) - reference(700, 1000, 0.51, 49)) + std::abs(response(o[1], 700, A) - reference(700, 1000, 0.51, 61));
    check("  L = 49 stages (98 poles), R = 61 stages (122 poles)", err < 5e-3, err); }
  { // Handbuch: 98 Pole bei 1 kHz, Q 16 -> Gruppenlaufzeit 0,50 s
    SchlierePatch p; set(p, 1000, 1, 7, 0); auto o = impulse(p, 4 * 48000, A); double gd = groupDelay(o[0], 1000, A), tail = groupDelay(o[3], 1000, A);
    check("98 poles at 1 kHz, Q 16: group delay 0.50 s (manual)", std::fabs(gd - 0.501) < 0.005, gd, 0.501);
    check("  tail, 122 poles: 0.50 s * 61 / 49", std::fabs(tail - 0.501 * 61 / 49) < 0.007, tail, 0.501 * 61 / 49); }
  { // Handbuch: 98 Pole bei 400 Hz, Q 16 -> 1,25 s
    SchlierePatch p; set(p, 400, 1, 7, 0); auto o = impulse(p, 10 * 48000, A); double gd = groupDelay(o[0], 400, A);
    check("98 poles at 400 Hz, Q 16: group delay 1.25 s (manual)", std::fabs(gd - 1.249) < 0.012, gd, 1.249); }
  { // Handbuch: zwischen 50 und 66 Polen 8 Kerben. R überblendet dort 62 -> 82 Pole: 10 Kerben
    SchlierePatch p; set(p, 1000, 0.5, 4.5, 0); auto o = impulse(p, 8192, A); int l = notches(o[0], A, -25), r = notches(o[1], A, -25);
    check("halfway between taps 4 and 5: 8 notches at L (manual)", l == 8, l, 8);
    check("  10 notches at R (taps 20 poles apart)", r == 10, r, 10);
    check("  LEDs 1-3 off between two taps", p.params[PARAMETER_AA] == 0 && p.params[PARAMETER_AB] == 0 && p.params[PARAMETER_AC] == 0, p.params[PARAMETER_AA]); }
  { // unterster Rastpunkt: L und R identisch, Diff still
    SchlierePatch p; set(p, 1000, 0.5, 1, 0); unsigned s = 1;
    auto o = run(p, 48000, [&](int c, size_t){ s = s * 1664525u + 1013904223u; return c == 0 ? 0.4 * ((s >> 8) / 8388608.0 - 1.0) : 0.0; });
    double diff = 0; for(size_t i = 0; i < o[0].size(); ++i) diff = std::fmax(diff, std::fabs(o[0][i] - o[1][i]));
    check("bottom tap: L and R identical, diff output silent", diff == 0 && peak(o[2]) == 0, diff, peak(o[2])); }
  { // Regler am Anschlag: 20 Hz und 20 kHz (eine Stufe dreht bei der Mittenfrequenz um 180 Grad)
    SchlierePatch lo; set(lo, 1000, 0.5, 1, 0); lo.params[PARAMETER_A] = 0.02f; auto a = impulse(lo, 96000, A);
    SchlierePatch hi; set(hi, 1000, 0.5, 1, 0); hi.params[PARAMETER_A] = 1.0f; auto b = impulse(hi, 4096, A);
    double e1 = std::abs(response(a[0], 20, A) + 1.0), e2 = std::abs(response(b[0], 20000, A) + 1.0);
    check("frequency knob at the stops: 20 Hz and 20 kHz", e1 < 0.01 && e2 < 0.01, e1, e2); }
  { // In 2: +1 V = eine Oktave
    SchlierePatch p; set(p, 1000, 0.5, 1, 0); auto o = impulse(p, 4096, A, 0.1); double e = std::abs(response(o[0], 2000, A) + 1.0);
    check("frequency CV: +1 V moves 1 kHz to 2 kHz", e < 0.01, e); }
  { // In 3: Tap-CV. Regler 0, CV so, dass Rastpunkt 5 getroffen wird (2 * (cv - 0.05) = 4/6)
    SchlierePatch p; set(p, 1000, 0.5, 1, 0); auto o = impulse(p, 8192, A, 0, 0.05 + 4.0 / 12.0);
    double err = std::abs(response(o[0], 700, A) - reference(700, 1000, 0.51, 33));
    check("tap CV reaches tap 5 (66 poles) with the knob at 0", err < 5e-3, err);
    check("  LEDs show 5 = red, off, red", p.params[PARAMETER_AA] == 1 && p.params[PARAMETER_AB] == 0 && p.params[PARAMETER_AC] == 1, p.params[PARAMETER_AA], p.params[PARAMETER_AC]); }
  { // offene CV-Eingänge mit Offset -0,3 V: Tap und Feedback bleiben unberührt
    SchlierePatch p; set(p, 1000, 0.5, 1, 0); auto o = impulse(p, 8192, A, 0, -0.03, -0.03);
    double err = std::abs(response(o[0], 700, A) - reference(700, 1000, 0.51, 1));
    check("open tap and feedback inputs (-0.3 V offset) change nothing", err < 2e-3 && p.params[PARAMETER_AD] == 0, err); }
  { // Gleichspannung: Vorwärtsweg DC-gekoppelt
    SchlierePatch p; set(p, 1000, 0.5, 7, 0); auto o = run(p, 48000, [](int c, size_t){ return c == 0 ? 0.2 : 0.0; });
    double e = std::fmax(std::fabs(o[0].back() - 0.2), std::fmax(std::fabs(o[1].back() - 0.2), std::fabs(o[3].back() - 0.2)));
    check("DC passes at unity (forward path is DC coupled)", e < 1e-4, e); }
  { // Feedback 90 %: Gleichspannung wird nicht verstärkt (Hochpass in der Schleife)
    SchlierePatch p; set(p, 1000, 0.5, 7, 0.9); auto o = run(p, 4 * 48000, [](int c, size_t){ return c == 0 ? 0.2 : 0.0; });
    const double want = 0.2 * std::sqrt(1 - 0.81);
    check("feedback 90 %: DC is not amplified (0.2 * sqrt(1 - fb^2))", std::fabs(o[0].back() - want) < 1e-3, o[0].back(), want); }
  { // Feedback 90 %, kleines Signal: Spitzen und Täler bei +-12,8 dB, mit negativem Feedback vertauscht
    const double a = 0.001, want = db(std::sqrt(1.9 / 0.1));
    SchlierePatch p; set(p, 1000, 0.5, 7, 0.9); auto o = impulse(p, 4 * 48000, a);
    double hi = -1e9, lo = 1e9, fHi = 0; for(double f = 900; f < 1100; f += 0.25){ double m = db(std::abs(response(o[0], f, a))); if(m > hi){ hi = m; fHi = f; } lo = std::fmin(lo, m); }
    check("feedback 90 %: peaks at +12.8 dB", std::fabs(hi - want) < 0.3, hi, want);
    check("  troughs at -12.8 dB", std::fabs(lo + want) < 0.3, lo, -want);
    SchlierePatch n; set(n, 1000, 0.5, 7, 0); auto on = impulse(n, 4 * 48000, a, 0, 0, -(0.05 + 0.9 / 0.97 / 2));
    double swapped = db(std::abs(response(on[0], fHi, a)));
    check("  negative feedback by CV: the peak becomes a trough", std::fabs(swapped + want) < 0.5, swapped, -want); }
  { // alles am Anschlag, heißes Signal: beschränkt, endlich, Begrenzung in der Schleife zeigt Rot
    SchlierePatch p; set(p, 200, 1, 7, 0.97); unsigned s = 7;
    auto o = run(p, 10 * 48000, [&](int c, size_t t){ s = s * 1664525u + 1013904223u; return c == 0 ? 0.6 * ((t / 218) % 2 ? 1.0 : -1.0) + 0.3 * ((s >> 8) / 8388608.0 - 1.0) : 0.0; });
    double m = std::fmax(std::fmax(peak(o[0]), peak(o[1])), std::fmax(peak(o[2]), peak(o[3])));
    check("9 V square plus noise, feedback and Q at maximum: outputs stay below 9.8 V", finite(o) && m <= 0.98, m, 0.98);
    check("  LED 4 red: the loop limiter works", p.params[PARAMETER_AD] == 1.0f, p.params[PARAMETER_AD]); }
  { // keine Selbstschwingung: nach dem Signal klingt die Schleife aus
    SchlierePatch p; set(p, 1000, 0.5, 7, 0.97);
    auto o = run(p, 14 * 48000, [&](int c, size_t t){ return c == 0 && t < 48000 ? 0.5 * std::sin(2 * PI * 997 * t / FS) : 0.0; });
    double early = peak(std::vector<float>(o[0].begin() + 48000, o[0].begin() + 2 * 48000)), late = peak(o[0], 13 * 48000);
    check("feedback at maximum: the loop rings out, no self-oscillation (dB after 12 s)", db(late / early) < -60, db(late / early), -60); }
  { // Modulation aller CV-Eingänge mit Audio-Rate
    SchlierePatch p; set(p, 800, 0.8, 4, 0.5); unsigned s = 3;
    auto o = run(p, 5 * 48000, [&](int c, size_t t){ s = s * 1664525u + 1013904223u; const double x = 2 * PI * t / FS;
      return c == 0 ? 0.5 * ((s >> 8) / 8388608.0 - 1.0) : (c == 1 ? 0.3 * std::sin(1300 * x) : (c == 2 ? 0.5 * std::sin(900 * x) : 0.5 * std::sin(2100 * x))); });
    double m = std::fmax(std::fmax(peak(o[0]), peak(o[1])), std::fmax(peak(o[2]), peak(o[3])));
    check("audio-rate modulation of frequency, tap and feedback: finite and bounded", finite(o) && m <= 0.98, m, 0.98); }
  { // schneller Sprung der Frequenz bei hohem Q und klingendem Filter: keine Pegelspitze
    SchlierePatch p; set(p, 500, 1, 7, 0);
    auto o = run(p, 3 * 48000, [&](int c, size_t t){ return c == 0 ? 0.25 * std::sin(2 * PI * 500 * t / FS) : (c == 1 ? ((t / 4800) % 2 ? 0.2 : -0.2) : 0.0); });
    check("frequency jumping by 4 octaves at Q 16 while ringing: no level burst", finite(o) && peak(o[0]) < 0.75, peak(o[0]), 0.75); }
  { // Störung im Blocktakt am Eingang (Periode 8 Samples, wie am Gerät): kommt nicht an die Ausgänge
    const double w[8] = { 9e-5, -4e-5, 2e-5, -7e-5, 5e-5, -1e-5, -6e-5, 2e-5 }; unsigned s = 9;
    SchlierePatch p; set(p, 1000, 0.5, 7, 0);
    auto o = run(p, 6 * 48000, [&](int c, size_t t){ s = s * 1664525u + 1013904223u; return c == 0 ? -0.03 + w[t % 8] + 5e-5 * ((s >> 8) / 8388608.0 - 1.0) : 0.0; });
    double worst = 0;
    for(int c : { 0, 1, 3 }){ double r[8] = {}, all = 0; for(size_t t = 4 * 48000; t < 6 * 48000; ++t) r[t % 8] += o[c][t];
      for(double& v : r){ v /= 12000; all += v / 8; } for(double v : r) worst = std::fmax(worst, std::fabs(v - all)); }
    check("block-rate interference at the input (9e-5) is cancelled at L, R and tail", worst < 3e-6, worst, 3e-6);
    check("  the input offset still passes at unity", std::fabs(o[0].back() + 0.03) < 2e-4, o[0].back(), -0.03); }
  { // LEDs nur aus oder rot, nie gedimmt: Gedimmtes Grün läuft über die LED-PWM (2320 Hz) und fiepst
    SchlierePatch p; set(p, 800, 0.8, 1, 0.5); bool dimmed = false; unsigned s = 5; float tap = 0;
    for(size_t t = 0; t < 4 * 48000; t += 8){ AudioBuffer b; b.ch.assign(4, std::vector<float>(8));
      tap = (float)t / (4 * 48000); p.params[PARAMETER_C] = tap; p.params[PARAMETER_D] = 1.0f - tap;
      for(size_t i = 0; i < 8; ++i){ s = s * 1664525u + 1013904223u; b.ch[0][i] = (float)(0.8 * ((s >> 8) / 8388608.0 - 1.0)); }
      p.processAudio(b);
      for(int l = 0; l < 4; ++l){ float v = p.params[PARAMETER_AA + l]; dimmed |= v != 0.0f && v != 1.0f; } }
    check("LED values are only 0 or 1 (never dimmed) over a sweep of tap and feedback", !dimmed, dimmed); }
  printf("%s\n", fails ? "FAILURES" : "all cases ok"); return fails;
}
