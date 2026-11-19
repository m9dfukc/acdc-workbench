// Host-Test der LED-Schleife aus Patch 07d und 17 (onLoop mit acdcOnLoopLate und acdcOnLoopDark, Code unverändert
// aus ACDC.cpp eingebunden):
// Was schreibt die Hauptschleife in den drei LED-Modi an die LEDs?
#include <cstdint>
#include <cstdio>
#include <cstring>
#define RED_COLOUR 0x3ff00000
#define NO_COLOUR 0
enum { PARAMETER_AA = 8, PARAMETER_BA = 16 };
template<class T> struct CircularBuffer {};
typedef int32_t audio_t;
extern "C" { int32_t codec_rxbuf[2 * 8 * 4]; uint16_t codec_blocksize = 8; }
CircularBuffer<audio_t>* volatile usbd_tx;
float tx_levels[4];
static int16_t params[32];
static uint32_t leds[9], now_ms;
static int writes, levels; // Schreibzugriffe auf LEDs, davon mit einem Pegelwert (weder rot noch aus)
void setLed(uint8_t led, uint32_t v){ leds[led] = v; writes++; if(v != RED_COLOUR && v != NO_COLOUR) levels++; }
int16_t getParameterValue(int p){ return params[p]; }
void setParameterValue(int p, int16_t v){ params[p] = v; }
uint32_t HAL_GetTick(){ return now_ms; }
static constexpr uint16_t ACDC_CLIPPING_LEVEL = 4090;
static constexpr uint16_t ACDC_LED_HOLD_BOOT = 0xffff;
static constexpr uint8_t ACDC_LEDS_NORMAL = 0, ACDC_LEDS_CLIP = 1, ACDC_LEDS_OFF = 2;
struct AcdcBootState { volatile uint16_t led_hold; volatile uint8_t led_mode; volatile uint8_t led_dark; } acdc_boot;
#define __attribute__(x) // Sections und naked gibt es auf dem Host nicht
#include "loop.inc"
#undef __attribute__

static int fails;
static void check(const char* name, bool ok, long a, long b = 0){ printf("%-4s %-70s %8ld %8ld\n", ok ? "ok" : "FAIL", name, a, b); if(!ok) fails++; }
static CircularBuffer<audio_t> stream;
static void input(int ch, int32_t v){ for(int i = 0; i < 16; ++i) codec_rxbuf[i * 4 + ch] = v & 0x00ffffff; } // 24 Bit ohne Vorzeichen
static void loops(int n){ for(int i = 0; i < n; ++i){ now_ms += 2; onLoop(); } }
static void start(uint8_t mode){
  memset(codec_rxbuf, 0, sizeof codec_rxbuf); memset(params, 0, sizeof params); memset(leds, 0xff, sizeof leds); memset(&acdc_raw, 0xa5, sizeof acdc_raw);
  usbd_tx = nullptr; writes = levels = 0; acdc_boot.led_hold = 0; acdc_boot.led_mode = mode; acdc_boot.led_dark = 0;
  for(int i = 0; i < 4; ++i) tx_levels[i] = 0.25f;
}
static bool dark(){ for(int i = 1; i <= 8; ++i) if(leds[i] != NO_COLOUR) return false; return true; }
int main(){
  { start(ACDC_LEDS_NORMAL); params[PARAMETER_AA] = 2000; params[PARAMETER_AA + 1] = 4095; loops(10);
    check("normal: LED 1 shows the patch value, LED 2 red, output LEDs the level", leds[1] == 2000 && leds[2] == RED_COLOUR && leds[5] == 1024, leds[1], leds[5]);
    check("normal: the loop writes the LEDs every time", writes > 80, writes); }
  { start(ACDC_LEDS_NORMAL); usbd_tx = &stream; input(2, 8300000); loops(10);
    check("normal, recording: clipping input 3 turns LED 3 red", leds[3] == RED_COLOUR, leds[3]); }
  { start(ACDC_LEDS_NORMAL); acdc_boot.led_hold = 5; loops(5);
    check("boot display holds the LEDs for led_hold loops", writes == 0 && acdc_boot.led_hold == 0, writes); }
  { start(ACDC_LEDS_OFF); params[PARAMETER_AA] = 2000; params[PARAMETER_AA + 1] = 4095; loops(1);
    check("off: first loop switches all eight LEDs off", writes == 8 && dark() && acdc_boot.led_dark == 1, writes, 8);
    usbd_tx = &stream; input(0, 8388607); input(1, 4000000); loops(1000);
    check("off: no LED write afterwards, with patch values, stream and clipping input", writes == 8 && dark(), writes, 8);
    check("off: the output level parameters still follow", params[PARAMETER_BA] == 1024 && params[PARAMETER_BA + 3] == 1024, params[PARAMETER_BA]); }
  { start(ACDC_LEDS_OFF); acdc_boot.led_hold = 3; loops(3); const int before = writes; loops(2);
    check("off: stays out of the way during the boot display, then switches off", before == 0 && writes == 8 && dark(), before, writes); }
  { start(ACDC_LEDS_CLIP); params[PARAMETER_AA] = 4095; input(0, 8388607); loops(500);
    check("clip, no stream: dark, patch values and input level are ignored", writes == 8 && dark(), writes, 8); }
  { start(ACDC_LEDS_CLIP); usbd_tx = &stream; input(0, 4000000); input(1, -4000000); loops(500);
    check("clip, recording at -6 dBFS: dark, no level display", dark() && levels == 0, writes, levels);
    const int base = writes; input(1, -8300000); loops(50);
    check("clip, recording: clipping input 2 turns LED 2 red with one write", leds[2] == RED_COLOUR && leds[1] == NO_COLOUR && writes == base + 1, writes - base, 1);
    input(1, 0); loops(140);
    check("clip: red holds 280 ms after the last clipped sample", leds[2] == RED_COLOUR && writes == base + 1, writes - base, 1);
    loops(20);
    check("clip: off again after 300 ms, one more write", dark() && writes == base + 2, writes - base, 2);
    input(3, 8388607); loops(5); usbd_tx = nullptr; loops(1);
    check("clip: the stream ends while LED 4 is red: off at once", dark(), leds[4]);
    check("clip: never a level value on an LED", levels == 0, levels); }
  printf("%s\n", fails ? "FAILURES" : "all cases ok");
  return fails;
}
