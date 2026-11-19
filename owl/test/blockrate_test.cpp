// Host-Test für owl/AcdcInput.h: Sperre für die Blockraten-Linien (Periode 8 Samples)
#include "AcdcInput.h"
#include <cmath>
#include <cstdio>
#include <functional>
#include <vector>
static int fails;
static void check(const char* name, bool ok, double a, double b = 0){ printf("%-4s %-66s %12.7f %12.7f\n", ok ? "ok" : "FAIL", name, a, b); if(!ok) fails++; }
static const double PI = 3.14159265358979, FS = 48000;
// Störung wie am Gerät: feste Wellenform über 8 Samples, mittelwertfrei, Spitze ≈ 1e-4 (−80 dBFS)
static const double W[8] = { 9e-5, -4e-5, 2e-5, -7e-5, 5e-5, -1e-5, -6e-5, 2e-5 };
static unsigned seed = 1;
static double noise(double amp){ seed = seed * 1664525u + 1013904223u; return amp * ((seed >> 8) / 8388608.0 - 1.0); }
static std::vector<double> run(AcdcBlockRateCanceller& c, size_t n, std::function<double(size_t)> in, size_t t0 = 0){
  std::vector<double> y(n); for(size_t t = 0; t < n; ++t) y[t] = c.process((float)in(t0 + t)); return y; }
// Anteil mit Periode 8: Mittel je Position minus Gesamtmittel, größter Betrag. from und to sind Vielfache von 8.
static double periodic(const std::vector<double>& y, size_t from, size_t to){
  double r[8] = {}, all = 0; for(size_t t = from; t < to; ++t) r[t % 8] += y[t];
  for(double& v : r){ v /= (to - from) / 8; all += v / 8; } double m = 0; for(double v : r) m = std::fmax(m, std::fabs(v - all)); return m; }
static double mean(const std::vector<double>& y, size_t from, size_t to){ double s = 0; for(size_t t = from; t < to; ++t) s += y[t]; return s / (to - from); }
int main(){
  const double DC = -0.03, N = 5e-5;
  auto idle = [&](size_t t){ return DC + W[t % 8] + noise(N); };
  { // Leerlauf: Offset, Störung, Rauschen
    AcdcBlockRateCanceller c; c.setSampleRate(FS); auto y = run(c, 6 * 48000, idle);
    std::vector<double> x(48000); for(size_t t = 0; t < x.size(); ++t) x[t] = W[t % 8];
    check("idle: period-8 part before (reference, 9e-5)", std::fabs(periodic(x, 0, 48000) - 9e-5) < 1e-6, periodic(x, 0, 48000), 9e-5);
    check("idle: period-8 part after 4 s below 3e-6 (-30 dB)", periodic(y, 4 * 48000, 6 * 48000) < 3e-6, periodic(y, 4 * 48000, 6 * 48000), 3e-6);
    check("  after 2 s already below 1e-5", periodic(y, 2 * 48000, 3 * 48000) < 1e-5, periodic(y, 2 * 48000, 3 * 48000), 1e-5);
    check("  DC offset passes unchanged", std::fabs(mean(y, 4 * 48000, 6 * 48000) - DC) < 2e-6, mean(y, 4 * 48000, 6 * 48000), DC); }
  { // langsames CV (1 Hz, 5 V): bleibt bis auf die Störung unverändert, keine neuen Anteile im Blocktakt
    AcdcBlockRateCanceller c; c.setSampleRate(FS); double err = 0;
    auto in = [&](size_t t){ return 0.5 * std::sin(2 * PI * 1.0 * t / FS) + W[t % 8]; };
    auto y = run(c, 8 * 48000, in);
    for(size_t t = 5 * 48000; t < 8 * 48000; ++t) err = std::fmax(err, std::fabs(y[t] - 0.5 * std::sin(2 * PI * 1.0 * t / FS)));
    check("1 Hz CV at 5 V: output equals the CV without the interference", err < 2e-4, err, 2e-4);
    check("  no period-8 part left or added", periodic(y, 5 * 48000, 8 * 48000) < 3e-6, periodic(y, 5 * 48000, 8 * 48000), 3e-6); }
  { // lautes Signal nach dem Lernen: Schätzung bleibt stehen, danach sofort wieder sauber, kein Nachklingen
    AcdcBlockRateCanceller c; c.setSampleRate(FS); run(c, 3 * 48000, idle);
    auto loud = run(c, 2 * 48000, [&](size_t t){ return DC + W[t % 8] + noise(0.3); });
    auto after = run(c, 12000, idle);
    check("after 2 s of loud noise (3 V): interference still cancelled at once", periodic(after, 480, 12000) < 6e-6, periodic(after, 480, 12000), 6e-6);
    double p = periodic(loud, 0, 2 * 48000);
    check("  loud noise itself passes (period-8 part only chance, < 3e-3)", p < 3e-3, p, 3e-3); }
  { // Ton genau auf fs/8: Die Korrektur ist auf 10 mV begrenzt, von der Grundwelle fehlen höchstens 13 mV
    AcdcBlockRateCanceller c; c.setSampleRate(FS);
    auto y = run(c, 4 * 48000, [&](size_t t){ return 0.25 * std::sin(2 * PI * 6000.0 * t / FS + 0.3); });
    double s = 0, q = 0; const size_t a = 3 * 48000, b = 4 * 48000;
    for(size_t t = a; t < b; ++t){ s += y[t] * std::sin(2 * PI * 6000.0 * t / FS + 0.3); q += y[t] * std::cos(2 * PI * 6000.0 * t / FS + 0.3); }
    double amp = 2 * std::sqrt(s * s + q * q) / (b - a);
    check("a 2.5 V tone exactly at fs/8 loses at most 13 mV (clipped correction, 4/pi * 10 mV)", amp > 0.25 - 0.0014 && amp <= 0.25, amp, 0.25); }
  { // Störung ändert sich in der Stille (andere Rechenlast): wird neu gelernt
    AcdcBlockRateCanceller c; c.setSampleRate(FS); run(c, 3 * 48000, idle);
    auto y = run(c, 4 * 48000, [&](size_t t){ return DC + 2.5 * W[(t + 3) % 8] + noise(N); });
    check("interference changes while quiet: relearned within 3 s", periodic(y, 3 * 48000, 4 * 48000) < 5e-6, periodic(y, 3 * 48000, 4 * 48000), 5e-6); }
  printf("%s\n", fails ? "FAILURES" : "all cases ok"); return fails;
}
