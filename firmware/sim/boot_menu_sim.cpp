// Host-Test der Boot-Menü-Logik aus Patch 15 (Code unverändert aus ACDC.cpp eingebunden)
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <functional>
#include <set>
#include <string>
typedef uint32_t TickType_t;
#define pdMS_TO_TICKS(x) ((TickType_t)(x))
#define MAIN_LOOP_SLEEP_MS 2
#define NOF_ADC_VALUES 4
#define DEFAULT_PROGRAM 1
#define RED_COLOUR 0x3ff00000
#define NO_COLOUR 0
#define RESOURCE_SYSTEM_RESOURCE 0x0100
#define RESOURCE_PORT_MAPPED 0x0800
enum { STARTUP_MODE, LOAD_MODE, RUN_MODE, CONFIGURE_MODE };
struct ResourceHeader { uint32_t magic, size; char name[16]; uint32_t checksum, flags; };
uint16_t adc_values[NOF_ADC_VALUES];
static TickType_t tick;
static std::function<void(TickType_t)> script;   // setzt adc_values und den Modus je Tick
static uint32_t leds[9];
static int red_seen;
void setLed(uint8_t led, uint32_t v){ leds[led] = v; if(v == RED_COLOUR) red_seen++; }
void vTaskDelay(TickType_t n){ for(TickType_t i=0;i<n;++i){ ++tick; if(script) script(tick); } }
TickType_t xTaskGetTickCount(){ return tick; }
struct Resource { ResourceHeader h; uint8_t d[4]; bool valid = false;
  size_t getDataSize(){ return h.size; } ResourceHeader* getHeader(){ return &h; } };
struct Storage { Resource rec; size_t freesize = 8u<<20; int writes = 0;
  Resource* getResourceByName(const char* n){ return rec.valid && !strcmp(n, rec.h.name) ? &rec : nullptr; }
  size_t readResource(ResourceHeader*, void* data, size_t, size_t len){ memcpy(data, rec.d, len); return len; }
  size_t getFreeSize(uint32_t){ return freesize; }
  size_t writeResource(const char* name, uint8_t* data, size_t size, uint32_t flags){
    writes++; memset(&rec.h, 0, sizeof rec.h); strcpy(rec.h.name, name); rec.h.size = size; rec.h.flags = flags;
    memcpy(rec.d, data + sizeof(ResourceHeader), size); rec.valid = true; return size; } } storage;
struct Registry { std::set<int> p; int inits = 0; bool hasPatch(uint8_t i){ return p.count(i); } void init(){ inits++; } } registry;
struct OwlStub { uint8_t mode = STARTUP_MODE; uint8_t getOperationMode(){ return mode; } } owl;
static constexpr uint16_t ACDC_LED_HOLD_BOOT = 0xffff;
struct AcdcBootState { volatile uint16_t led_hold; } acdc_boot;
#include "menu.inc"

static int fails;
static void record(int slot){ if(slot){ storage.rec.valid = true; strcpy(storage.rec.h.name, "ACDC.slot"); storage.rec.h.size = 4;
  storage.rec.d[0] = slot; storage.rec.d[1] = ~slot; storage.rec.d[2] = 'S'; storage.rec.d[3] = 'L'; } else storage.rec.valid = false; }
static int shown(){ int s = 0; for(int i=0;i<4;++i) if(leds[i+1] && leds[i+1] != RED_COLOUR) s |= 1<<i; return s; }
struct Case { const char* name; std::set<int> slots; int rec; std::function<void(TickType_t)> scr; int expect; int expect_rec; int expect_writes; int hold; size_t free; };
static void run(Case c){
  tick = 0; storage = Storage(); registry = Registry(); owl = OwlStub(); memset(leds, 0, sizeof leds); red_seen = 0;
  registry.p = c.slots; record(c.rec); storage.freesize = c.free; script = c.scr; script(0);
  acdc_boot.led_hold = 0x1234;
  int got = acdcBootSelect();
  int rec = acdcReadSlot();
  bool ok = got == c.expect && rec == c.expect_rec && storage.writes == c.expect_writes && acdc_boot.led_hold == c.hold
            && (got == 0 || shown() == (c.slots.empty() ? 0 : got));
  printf("%-4s %-46s slot %2d (exp %2d) rec %2d (exp %2d) writes %d hold %5u leds %2d red %d t=%6u ms\n", ok ? "ok" : "FAIL",
         c.name, got, c.expect, rec, c.expect_rec, storage.writes, (unsigned)acdc_boot.led_hold, shown(), red_seen, (unsigned)tick);
  if(!ok) fails++;
}
static void knobs(int a, int b, int c, int d){ adc_values[0]=a; adc_values[1]=b; adc_values[2]=c; adc_values[3]=d; }
// Rampe von v0 nach v1 zwischen t0 und t1
static int ramp(TickType_t t, TickType_t t0, TickType_t t1, int v0, int v1){ if(t<=t0) return v0; if(t>=t1) return v1; return v0 + (int)((int64_t)(v1-v0)*(t-t0)/(t1-t0)); }
int main(){
  const size_t BIG = 8u<<20;
  auto pattern = [](TickType_t){ knobs(10, 20, 15, 4080); };
  run({"normal boot, no record", {1,2,3}, 0, [](TickType_t){ knobs(2000,2000,2000,2000); }, 1, 0, 0, 500, BIG});
  run({"normal boot, record 3", {1,2,3}, 3, [](TickType_t){ knobs(2000,2000,2000,2000); }, 3, 3, 0, 500, BIG});
  run({"record 5 but slot 5 empty", {1,2,3}, 5, [](TickType_t){ knobs(0,0,0,0); }, 1, 5, 0, 500, BIG});
  run({"slot 1 empty, no record -> first occupied", {2,4}, 0, [](TickType_t){ knobs(2000,0,0,4095); }, 2, 0, 0, 500, BIG});
  run({"no patches at all", {}, 0, pattern, 1, 0, 0, 500, BIG});
  run({"three knobs left but knob 4 at 90 %", {1,2,3}, 3, [](TickType_t){ knobs(0,0,0,3686); }, 3, 3, 0, 500, BIG});
  run({"menu, knob 1 untouched, confirm", {1,2,3}, 3, [](TickType_t t){ knobs(10,20,15, ramp(t,3000,3500,4080,2000)); }, 3, 3, 0, 500, BIG});
  run({"menu, knob 1 to middle, confirm", {1,2,3}, 3, [](TickType_t t){ knobs(ramp(t,1000,2000,10,2048),20,15, ramp(t,3000,3500,4080,2000)); }, 2, 2, 1, 500, BIG});
  run({"menu, knob 1 up and back left, confirm", {1,2,3}, 3, [](TickType_t t){ knobs(t<2000?ramp(t,1000,2000,10,3000):ramp(t,2000,3000,3000,0),20,15, ramp(t,4000,4500,4080,2000)); }, 1, 1, 1, 500, BIG});
  run({"menu, knob 1 to slot 2, cancel with knob 3", {1,2,3}, 3, [](TickType_t t){ knobs(ramp(t,1000,2000,10,2048),20,ramp(t,3000,3500,15,1500),4080); }, 3, 3, 0, 500, BIG});
  run({"menu, timeout", {1,2,3}, 3, [](TickType_t t){ knobs(ramp(t,1000,2000,10,2048),20,15,4080); }, 3, 3, 0, 500, BIG});
  run({"menu, host takes over (LOAD_MODE)", {1,2,3}, 3, [](TickType_t t){ knobs(10,20,15,4080); if(t>5000) owl.mode = LOAD_MODE; }, 0, 3, 0, 0, BIG});
  run({"menu, storage nearly full: not remembered", {1,2,3}, 3, [](TickType_t t){ knobs(ramp(t,1000,2000,10,2048),20,15, ramp(t,3000,3500,4080,2000)); }, 2, 3, 0, 500, 30000});
  run({"menu, 15 slots, knob 1 fully right", {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}, 1, [](TickType_t t){ knobs(ramp(t,1000,3000,10,4095),20,15, ramp(t,4000,4500,4080,2000)); }, 15, 15, 1, 500, BIG});
  run({"menu, 15 slots, knob 1 at 50 %", {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}, 1, [](TickType_t t){ knobs(ramp(t,1000,3000,10,2048),20,15, ramp(t,4000,4500,4080,2000)); }, 8, 8, 1, 500, BIG});
  run({"menu, sparse slots 1,4,9, knob 1 at 90 %", {1,4,9}, 1, [](TickType_t t){ knobs(ramp(t,1000,3000,10,3686),20,15, ramp(t,4000,4500,4080,2000)); }, 9, 9, 1, 500, BIG});
  run({"menu, jitter at a zone border keeps the slot", {1,2}, 1, [](TickType_t t){ int k = t<2000 ? ramp(t,1000,2000,10,1900) : 2048 + ((t/7)%2 ? 60 : -60); knobs(k,20,15, ramp(t,6000,6500,4080,2000)); }, 1, 1, 0, 500, BIG});
  run({"menu, noisy knob 4 at the stop does not confirm", {1,2,3}, 3, [](TickType_t t){ knobs(10,20,15, t>61000 ? 4000 : 3990 + (int)(t*37%100)); }, 3, 3, 0, 500, BIG});
  printf("%s\n", fails ? "FAILURES" : "all cases ok");
  return fails;
}
