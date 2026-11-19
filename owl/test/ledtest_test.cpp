// Host-Test für owl/test/SchliereLedTestPatch.hpp: Zeitplan der LED-Zustände
#include "SchliereLedTestPatch.hpp"
#include <cstdio>
static int fails;
static void check(const char* name, bool ok, double a, double b = 0){ printf("%-4s %-66s %10.5f %10.5f\n", ok ? "ok" : "FAIL", name, a, b); if(!ok) fails++; }
int main(){
  SchliereLedTestPatch p;
  for(int i = 0; i < 4; ++i) p.params[i] = 0.5f;
  // 50 s in Blöcken zu 8, LED-Werte jeweils nach dem Block. code = LED 1…4 als Ziffern (0 aus, 1 rot, 6 grün 60 %)
  auto code = [&](){ int c = 0; for(int i = 0; i < 4; ++i){ float v = p.params[PARAMETER_AA + i]; c = c * 10 + (v == 1.0f ? 1 : (v == 0.6f ? 6 : (v == 0.0f ? 0 : 9))); } return c; };
  int at[10] = {}; int toggles = 0, last = 0; bool otherInFlicker = false;
  for(size_t blk = 0; blk < 50 * 6000; ++blk){
    AudioBuffer b; b.ch.assign(4, std::vector<float>(8, 0.0f));
    p.processAudio(b);
    const int c = code(); const double t = (blk + 1) / 6000.0;
    for(int k = 0; k < 10; ++k) if(blk == (size_t)(k * 30000 + 15000)) at[k] = c;
    if(t > 25.0 && t <= 30.0){ if(c != last) toggles++; otherInFlicker |= c != 0 && c != 1110; }
    last = c;
  }
  const int want[10] = { 0, 1000, 1110, 1111, 0, -1, 0, 6660, 0, 1000 };
  const char* name[10] = { "2.5 s: all off", "7.5 s: LED 1 red", "12.5 s: LEDs 1-3 red", "17.5 s: LEDs 1-4 red", "22.5 s: all off", "",
                           "32.5 s: all off", "37.5 s: LEDs 1-3 green at 60 %", "42.5 s: sequence repeats, all off", "47.5 s: LED 1 red" };
  for(int k = 0; k < 10; ++k) if(want[k] >= 0) check(name[k], at[k] == want[k], at[k], want[k]);
  // 400 Halbperioden, beginnt und endet aus: 399 Wechsel im Fenster, der letzte fällt auf den Phasenwechsel
  check("25-30 s: LEDs 1-3 blink at 40 Hz (399 changes), LED 4 off", toggles == 399 && !otherInFlicker, toggles, 399);
  printf("%s\n", fails ? "FAILURES" : "all cases ok"); return fails;
}
