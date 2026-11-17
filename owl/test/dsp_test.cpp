#include "Tanh3Patch.hpp"
#include "AcdcOutput.h"
#include <cmath>
#include <cstdio>
static int fails;
static void check(const char* name, bool ok, double a, double b = 0){ printf("%-4s %-58s %10.5f %10.5f\n", ok ? "ok" : "FAIL", name, a, b); if(!ok) fails++; }
static const double PI = 3.14159265358979;
// Lässt den Patch über n Samples laufen (Blöcke zu 8), gibt die letzten 'keep' Samples je Kanal zurück
template<class F> static std::vector<std::vector<float>> run(Patch& p, size_t n, size_t keep, F in){
  std::vector<std::vector<float>> out(4);
  for(size_t t = 0; t < n; t += 8){
    AudioBuffer b; b.ch.assign(4, std::vector<float>(8));
    for(size_t i = 0; i < 8; ++i) for(int c = 0; c < 4; ++c) b.ch[c][i] = in(c, t + i);
    p.processAudio(b);
    if(t + 8 > n - keep) for(int c = 0; c < 4; ++c) out[c].insert(out[c].end(), b.ch[c].begin(), b.ch[c].end());
  }
  return out;
}
static double peak(const std::vector<float>& v){ double m = 0; for(float x : v) m = std::fmax(m, std::fabs(x)); return m; }
static double level_for(double k){ return 0.5 * std::exp(3.4657359 * k); }
int main(){
  const double fs = 48000;
  { // kleines Signal, Level 1 (Regler = ln(2)/ln(32) = 0.2): Verstärkung 1
    Tanh3Patch p; p.params[PARAMETER_A] = 0.2f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c == 0 ? 0.01 * std::sin(2*PI*100*t/fs) : 0.0; });
    check("small signal at level 1 passes at unity (peak 0.01)", std::fabs(peak(o[0]) - 0.01) < 2e-4, peak(o[0]), 0.01); }
  { // DC: 0.5 (5 V) bei Level 1 -> 0.5*tanh(1)
    Tanh3Patch p; p.params[PARAMETER_A] = 0.2f;
    auto o = run(p, 48000, 8, [&](int c, size_t){ return c == 0 ? 0.5 : 0.0; });
    check("DC 5 V at level 1 -> 5 V * tanh(1) = 0.3808", std::fabs(o[0].back() - 0.5*std::tanh(1.0)) < 1e-4, o[0].back(), 0.5*std::tanh(1.0)); }
  { // voll aufgedreht: Sättigung bei SAT, nie darüber
    Tanh3Patch p; p.params[PARAMETER_A] = 1.0f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c == 0 ? 0.9 * std::sin(2*PI*440*t/fs) : 0.0; });
    check("hot 440 Hz sine at full level saturates near 0.5 (band-limited overshoot < 10 %)", peak(o[0]) <= 0.55 && peak(o[0]) > 0.49, peak(o[0]), 0.5);
    check("  red LED on channel 1 (deep saturation)", p.params[PARAMETER_AA] == 1.0f, p.params[PARAMETER_AA]); }
  { // Linksanschlag: 0.5-fach, nicht stumm
    Tanh3Patch p; p.params[PARAMETER_A] = 0.0f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c == 0 ? 0.02 * std::sin(2*PI*100*t/fs) : 0.0; });
    check("knob fully left: half level, not muted", std::fabs(peak(o[0]) - 0.01) < 2e-4, peak(o[0]), 0.01); }
  { // statische Kennlinie: langsame Rampe, Referenz um die Filterlaufzeit (47/4 Samples) verschoben
    Tanh3Patch p; p.params[PARAMETER_B] = 0.6f; double g = level_for(0.6), err = 0; const double delay = 47.0 / 4.0;
    auto o = run(p, 96000, 48000, [&](int c, size_t t){ return c == 1 ? -0.9 + 1.8 * t / 96000.0 : 0.0; });
    for(size_t i = 1; i < o[1].size(); ++i){ double x = -0.9 + 1.8 * (48000 + i - delay) / 96000.0; err = std::fmax(err, std::fabs(o[1][i] - 0.5*std::tanh(g*x/0.5))); }
    check("slow ramp follows SAT*tanh(level*x/SAT), delay 11.75 samples (max error)", err < 1e-4, err); }
  { // Aliasing: 3001 Hz bei 6,7-fachem Level, Fremdlinien unter 15 kHz (Goertzel je Hz, kohärent über 1 s)
    Tanh3Patch p; p.params[PARAMETER_A] = 0.75f; const size_t N = 48000; const int f = 3001;
    auto o = run(p, 2*N, N, [&](int c, size_t t){ return c == 0 ? 0.5 * std::sin(2*PI*f*t/fs) : 0.0; });
    auto mag = [&](int bin){ double w = 2*PI*bin/N, c2 = 2*std::cos(w), s1 = 0, s2 = 0; for(size_t i = 0; i < N; ++i){ double s0 = o[0][i] + c2*s1 - s2; s2 = s1; s1 = s0; }
      return std::sqrt(std::fmax(0.0, s1*s1 + s2*s2 - c2*s1*s2)) / (N/2); };
    double fund = mag(f), alias = 0; for(int bin = 20; bin < 15000; ++bin) if(bin % f) { double m = mag(bin); alias += m*m; }
    double db = 20*std::log10(std::sqrt(alias)/fund);
    check("3 kHz at level 6.7: alias products below 15 kHz under -90 dB", db < -90, db, -90);
    check("  band-limited peak stays below 0.6", peak(o[0]) < 0.6, peak(o[0]), 0.6); }
  { // Mix: drei kleine Signale, Regler 4 voll, In 4 offen mit Offset -0.03
    Tanh3Patch p; for(int c = 0; c < 3; ++c) p.params[c] = 0.2f; p.params[PARAMETER_D] = 1.0f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c < 3 ? 0.01 * std::sin(2*PI*100*t/fs) : -0.03; });
    check("mix = sum of the three channels at full level (0.03)", std::fabs(peak(o[3]) - 0.03) < 5e-4, peak(o[3]), 0.03); }
  { // Regler 4 am Linksanschlag (liest 0.02): stumm
    Tanh3Patch p; for(int c = 0; c < 3; ++c) p.params[c] = 0.2f; p.params[PARAMETER_D] = 0.02f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c < 3 ? 0.2 * std::sin(2*PI*100*t/fs) : -0.03; });
    check("mix knob at the left stop (reads 0.02): silent", peak(o[3]) < 1e-6, peak(o[3])); }
  { // CV: Regler 0, +2.5 V + Totzone -> halber Pegel
    Tanh3Patch p; for(int c = 0; c < 3; ++c) p.params[c] = 0.2f; p.params[PARAMETER_D] = 0.0f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c == 0 ? 0.02 * std::sin(2*PI*100*t/fs) : (c == 3 ? 0.30 : 0.0); });
    check("CV 3 V with knob at 0: level (0.30-0.05)*2 = 0.5", std::fabs(peak(o[3]) - 0.01) < 3e-4, peak(o[3]), 0.01); }
  { // CV negativ nimmt Pegel weg
    Tanh3Patch p; for(int c = 0; c < 3; ++c) p.params[c] = 0.2f; p.params[PARAMETER_D] = 0.5f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c == 0 ? 0.02 * std::sin(2*PI*100*t/fs) : (c == 3 ? -0.5 : 0.0); });
    check("CV -5 V with knob at 12 o'clock: silent", peak(o[3]) < 1e-6, peak(o[3])); }
  { // Mix sättigt ebenfalls bei SAT
    Tanh3Patch p; for(int c = 0; c < 4; ++c) p.params[c] = 1.0f;
    auto o = run(p, 48000, 4800, [&](int c, size_t t){ return c < 3 ? 0.9 * std::sin(2*PI*(200+50*c)*t/fs) : 0.0; });
    check("mix of three saturated channels stays near 0.5 (overshoot < 10 %)", peak(o[3]) <= 0.55, peak(o[3]), 0.5); }
  // ---- Limiter
  { AcdcOutputLimiter lim; lim.setSampleRate(fs); std::vector<float> l(4800), r(4800), l0; double diff = 0;
    for(size_t i = 0; i < l.size(); ++i){ l[i] = 0.45 * std::sin(2*PI*220*i/fs); r[i] = 0.3 * std::sin(2*PI*331*i/fs); } l0 = l;
    lim.process({l.data(), l.size()}, {r.data(), r.size()}); for(size_t i = 0; i < l.size(); ++i) diff = std::fmax(diff, std::fabs(l[i]-l0[i]));
    check("limiter: signal below 5 V is bit-identical", diff == 0, diff); }
  { AcdcOutputLimiter lim; lim.setSampleRate(fs); std::vector<float> l(48000), r(48000); double all = 0;
    for(size_t i = 0; i < l.size(); ++i){ l[i] = 1.6 * std::sin(2*PI*220*i/fs); r[i] = 0.8 * std::sin(2*PI*220*i/fs); }
    lim.process({l.data(), l.size()}, {r.data(), r.size()}); for(float x : l) all = std::fmax(all, std::fabs(x));
    std::vector<float> lt(l.end()-4800, l.end()), rt(r.end()-4800, r.end());
    check("limiter: 16 V sine settles near 5 V (peak of the last 100 ms)", peak(lt) > 0.47 && peak(lt) < 0.56, peak(lt), 0.5);
    check("  stereo image kept: right stays at half of left", std::fabs(peak(rt)/peak(lt) - 0.5) < 0.03, peak(rt)/peak(lt), 0.5);
    check("  never above the ceiling 0.75, even during the attack", all <= 0.75, all, 0.75); }
  { AcdcOutputLimiter lim; lim.setSampleRate(fs); std::vector<float> l(4800, 0.f), r(4800, 0.f); l[100] = NAN; l[101] = 50.f; r[102] = -50.f;
    lim.process({l.data(), l.size()}, {r.data(), r.size()}); bool fin = true; for(float x : l) fin &= std::isfinite(x) && std::fabs(x) <= 0.75f;
    check("limiter: NaN and spikes from a patch stay finite and bounded", fin, peak(l)); }
  printf("%s\n", fails ? "FAILURES" : "all cases ok"); return fails;
}
