// Host-Test für owl/test/SchliereLedPathPatch.hpp: Zeitplan, Ausgänge je Phase und die Messung am Eingang
#include "SchliereLedPathPatch.hpp"
#include <cmath>
#include <cstdio>
#include <cstring>
static int fails;
static void check(const char* name, bool ok, double a, double b = 0){ printf("%-4s %-66s %10.5f %10.5f\n", ok ? "ok" : "FAIL", name, a, b); if(!ok) fails++; }
static int blinkMsg[3], statMsg[3], blinkN, statN;
void debugMessage(const char* msg, int a, int b, int c){
  if(!strcmp(msg, "LEDblink In1-3")){ blinkMsg[0] = a; blinkMsg[1] = b; blinkMsg[2] = c; blinkN++; }
  if(!strcmp(msg, "LEDstat In1-3")){ statMsg[0] = a; statMsg[1] = b; statMsg[2] = c; statN++; }
}
int main(){
  SchliereLedPathPatch p;
  for(int i = 0; i < 4; ++i) p.params[i] = 0.5f;
  // Modell: Jede leuchtende LED verschiebt In 1 um 2e-4 und In 3 um −5e-5, In 2 bleibt. Die LED folgt dem
  // Parameter einen Block später. Dazu Offset, Rauschen und 50 Hz Brumm auf allen Eingängen.
  unsigned s = 7; int lit = 0; double maxMute = 0, calPeak = 0, gainErr = 0; bool ledsOk = true;
  for(size_t blk = 0; blk < 100 * 6000; ++blk){
    AudioBuffer b; b.ch.assign(4, std::vector<float>(8));
    float in1[8];
    for(size_t i = 0; i < 8; ++i){
      const double hum = 3e-4 * std::sin(2 * 3.14159265358979 * 50.0 * (blk * 8 + i) / 48000.0);
      for(int c = 0; c < 4; ++c){ s = s * 1664525u + 1013904223u; b.ch[c][i] = (float)(-0.03 + hum + 1e-4 * ((s >> 8) / 8388608.0 - 1.0)); }
      b.ch[0][i] += 2e-4f * lit; b.ch[2][i] -= 5e-5f * lit; in1[i] = b.ch[0][i];
    }
    p.processAudio(b);
    lit = 0; for(int l = 0; l < 4; ++l) lit += p.params[PARAMETER_AA + l] == 1.0f;
    const size_t phase = (blk / 30000) % 10, inPhase = blk % 30000;
    const int want = (phase == 5) ? 4 : (((phase == 1 || phase == 3 || phase == 9) && ((inPhase / 75) & 1)) ? 3 : 0);
    ledsOk &= lit == want;
    for(size_t i = 0; i < 8; ++i){
      if(phase >= 2 && phase <= 6) for(int c = 0; c < 4; ++c) maxMute = std::fmax(maxMute, std::fabs(b.ch[c][i]));
      if(phase == 7){ calPeak = std::fmax(calPeak, std::fabs(b.ch[0][i])); maxMute = std::fmax(maxMute, std::fabs(b.ch[1][i])); }
      if(phase >= 8) for(int c = 0; c < 4; ++c) gainErr = std::fmax(gainErr, std::fabs(b.ch[c][i] - 4.0f * in1[i]));
    }
  }
  check("LED schedule: off, 3 blink, off, 3 blink, off, 4 red, off, off, off, 3 blink", ledsOk, ledsOk);
  check("phases 2-6: all outputs are exactly zero (phase 7: Out 2 too)", maxMute == 0, maxMute);
  check("phase 7: calibration tone at Out 1 peaks at 0.001", std::fabs(calPeak - 0.001) < 2e-6, calPeak, 0.001);
  check("phases 8-9: all outputs = 4 x In 1", gainErr < 1e-6, gainErr);
  check("two cycles: one message per cycle and kind", blinkN == 2 && statN == 2, blinkN, statN);
  check("blink at In 1: 3 LEDs x 2e-4 = 6000 (1e-7 full scale)", std::abs(blinkMsg[0] - 6000) < 60, blinkMsg[0], 6000);
  check("blink at In 2: nothing", std::abs(blinkMsg[1]) < 60, blinkMsg[1], 0);
  check("blink at In 3: 3 x -5e-5 = -1500", std::abs(blinkMsg[2] + 1500) < 60, blinkMsg[2], -1500);
  check("static at In 1: 4 LEDs x 2e-4 = 8000", std::abs(statMsg[0] - 8000) < 60, statMsg[0], 8000);
  check("static at In 2: nothing", std::abs(statMsg[1]) < 60, statMsg[1], 0);
  check("static at In 3: 4 x -5e-5 = -2000", std::abs(statMsg[2] + 2000) < 60, statMsg[2], -2000);
  printf("%s\n", fails ? "FAILURES" : "all cases ok"); return fails;
}
