// Host-Test der Boot-Menü-Logik aus Patch 15 und 17 (Code unverändert aus ACDC.cpp eingebunden).
// Mit -DACDC_SIM_LED_MODE zusätzlich die Fälle für den LED-Modus (Patch 17, Regler 2).
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <functional>
#include <map>
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
static TickType_t probe_tick; // zu diesem Tick die Zahl der leuchtenden Ausgangs-LEDs festhalten
static int probe_lit;
void setLed(uint8_t led, uint32_t v){ leds[led] = v; if(v == RED_COLOUR) red_seen++; }
void vTaskDelay(TickType_t n){ for(TickType_t i=0;i<n;++i){ ++tick; if(script) script(tick);
  if(tick == probe_tick){ probe_lit = 0; for(int l=5;l<=8;++l) probe_lit += leds[l] != 0; } } }
TickType_t xTaskGetTickCount(){ return tick; }
struct Resource { ResourceHeader h; uint8_t d[4]; bool valid = false;
  size_t getDataSize(){ return h.size; } ResourceHeader* getHeader(){ return &h; } };
struct Storage { std::map<std::string, Resource> recs; size_t freesize = 8u<<20; int writes = 0;
  Resource* getResourceByName(const char* n){ auto it = recs.find(n); return it != recs.end() && it->second.valid ? &it->second : nullptr; }
  size_t readResource(ResourceHeader* h, void* data, size_t, size_t len){ memcpy(data, recs[h->name].d, len); return len; }
  size_t getFreeSize(uint32_t){ return freesize; }
  size_t writeResource(const char* name, uint8_t* data, size_t size, uint32_t flags){
    Resource& rec = recs[name];
    writes++; memset(&rec.h, 0, sizeof rec.h); strcpy(rec.h.name, name); rec.h.size = size; rec.h.flags = flags;
    memcpy(rec.d, data + sizeof(ResourceHeader), size); rec.valid = true; return size; } } storage;
struct Registry { std::set<int> p; int inits = 0; bool hasPatch(uint8_t i){ return p.count(i); } void init(){ inits++; } } registry;
struct OwlStub { uint8_t mode = STARTUP_MODE; uint8_t getOperationMode(){ return mode; } } owl;
static constexpr uint16_t ACDC_LED_HOLD_BOOT = 0xffff;
static constexpr uint8_t ACDC_LEDS_NORMAL = 0, ACDC_LEDS_CLIP = 1, ACDC_LEDS_OFF = 2;
struct AcdcBootState { volatile uint16_t led_hold; volatile uint8_t led_mode; volatile uint8_t led_dark; } acdc_boot;
#include "menu.inc"

static int fails;
static void put(const char* name, int v, char c2, char c3){ Resource& r = storage.recs[name]; r.valid = true; strcpy(r.h.name, name); r.h.size = 4;
  r.d[0] = v; r.d[1] = ~v; r.d[2] = c2; r.d[3] = c3; }
static void record(int slot){ if(slot) put("ACDC.slot", slot, 'S', 'L'); else storage.recs.erase("ACDC.slot"); }
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
#ifdef ACDC_SIM_LED_MODE
// LED-Modus (Patch 17): rec_mode < 0 = keine Ressource. probe = Tick, zu dem die Ausgangs-LEDs gezählt werden (0 = nicht prüfen)
struct LedCase { const char* name; int rec_slot; int rec_mode; std::function<void(TickType_t)> scr; int expect_slot; int expect_mode; int expect_rec_mode;
  int expect_writes; TickType_t probe; int expect_lit; size_t free; };
static void runLed(LedCase c){
  tick = 0; storage = Storage(); registry = Registry(); owl = OwlStub(); memset(leds, 0, sizeof leds); red_seen = 0;
  registry.p = {1,2,3}; record(c.rec_slot); if(c.rec_mode >= 0) put("ACDC.led", c.rec_mode, 'L', 'D');
  storage.freesize = c.free; script = c.scr; script(0); probe_tick = c.probe; probe_lit = -1;
  acdc_boot.led_hold = 0x1234; acdc_boot.led_mode = 77; acdc_boot.led_dark = 9;
  int got = acdcBootSelect();
  int rec_mode = acdcReadLedMode(), rec_slot = acdcReadSlot();
  bool ok = got == c.expect_slot && acdc_boot.led_mode == c.expect_mode && rec_mode == c.expect_rec_mode && storage.writes == c.expect_writes
            && acdc_boot.led_dark == 0 && (c.probe == 0 || probe_lit == c.expect_lit) && (got == 0 || rec_slot == got || c.free < (8u<<20));
  printf("%-4s %-46s slot %2d (exp %2d) mode %d (exp %d) rec %d (exp %d) writes %d lit %2d red %d t=%6u ms\n", ok ? "ok" : "FAIL",
         c.name, got, c.expect_slot, (int)acdc_boot.led_mode, c.expect_mode, rec_mode, c.expect_rec_mode, storage.writes, probe_lit, red_seen, (unsigned)tick);
  if(!ok) fails++;
}
#endif
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
#ifdef ACDC_SIM_LED_MODE
  // Regler 2 von links auf v zwischen 1 und 2 s, Bestätigen mit Regler 4 ab 3 s
  auto k2 = [](int v){ return [v](TickType_t t){ knobs(10, ramp(t,1000,2000,20,v), 15, ramp(t,3000,3500,4080,2000)); }; };
  runLed({"led: normal boot, no record -> normal", 3, -1, [](TickType_t){ knobs(2000,2000,2000,2000); }, 3, 0, 0, 0, 0, 0, BIG});
  runLed({"led: normal boot, record off -> off", 3, 2, [](TickType_t){ knobs(2000,2000,2000,2000); }, 3, 2, 2, 0, 0, 0, BIG});
  runLed({"led: invalid record (mode 3) -> normal", 3, 3, [](TickType_t){ knobs(2000,2000,2000,2000); }, 3, 0, 0, 0, 0, 0, BIG});
  runLed({"led: menu, knob 2 untouched keeps clip, 2 lit", 3, 1, k2(20), 3, 1, 1, 0, 2500, 2, BIG});
  runLed({"led: menu, knob 2 untouched keeps off, 0 lit", 3, 2, k2(20), 3, 2, 2, 0, 2500, 0, BIG});
  runLed({"led: menu, knob 2 to 50 % -> clip, stored", 3, -1, k2(2048), 3, 1, 1, 1, 2700, 2, BIG});
  runLed({"led: menu, knob 2 fully right -> off, stored", 3, -1, k2(4095), 3, 2, 2, 1, 2700, 0, BIG});
  runLed({"led: menu, off stored, knob 2 to 20 % -> normal", 3, 2, k2(819), 3, 0, 0, 1, 2700, 4, BIG});
  runLed({"led: menu, knob 2 up and back left -> normal", 3, 2, [](TickType_t t){ knobs(10, t<2000?ramp(t,1000,2000,20,3000):ramp(t,2000,3000,3000,0), 15, ramp(t,4000,4500,4080,2000)); }, 3, 0, 0, 1, 0, 0, BIG});
  runLed({"led: menu, slot and mode change: two writes", 3, -1, [](TickType_t t){ knobs(ramp(t,1000,2000,10,2048), ramp(t,1000,2000,20,4095), 15, ramp(t,3000,3500,4080,2000)); }, 2, 2, 2, 2, 0, 0, BIG});
  runLed({"led: menu, knob 2 to off, cancel with knob 3", 3, 1, [](TickType_t t){ knobs(10, ramp(t,1000,2000,20,4095), ramp(t,3000,3500,15,1500), 4080); }, 3, 1, 1, 0, 0, 0, BIG});
  runLed({"led: menu, knob 2 to off, timeout", 3, -1, [](TickType_t t){ knobs(10, ramp(t,1000,2000,20,4095), 15, 4080); }, 3, 0, 0, 0, 0, 0, BIG});
  runLed({"led: menu, host takes over keeps stored mode", 3, 1, [](TickType_t t){ knobs(10, ramp(t,1000,2000,20,4095), 15, 4080); if(t>5000) owl.mode = LOAD_MODE; }, 0, 1, 1, 0, 0, 0, BIG});
  runLed({"led: menu, storage nearly full: applies, not stored", 3, -1, k2(4095), 3, 2, 0, 0, 0, 0, 30000});
  runLed({"led: menu, jitter at a zone border keeps the mode", 3, -1, [](TickType_t t){ int k = t<2000 ? ramp(t,1000,2000,20,1200) : 1365 + ((t/7)%2 ? 60 : -60); knobs(10, k, 15, ramp(t,6000,6500,4080,2000)); }, 3, 0, 0, 0, 0, 0, BIG});
#endif
  printf("%s\n", fails ? "FAILURES" : "all cases ok");
  return fails;
}
