#!/usr/bin/env bash
# Host test of the boot menu logic (patch 15): compiles the menu code of a build tree
# unchanged together with stubs for knobs, LEDs, storage and scheduler, and runs it
# against scripted knob movements (firmware/sim/boot_menu_sim.cpp).
#
# Usage:
#   tools/sim_boot_menu.sh [source tree]
# Default tree: firmware/_work/acdc1-build6b-fx4b (left behind by tools/build_acdc.sh).
# Exit code 0 = all cases ok.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TREE="${1:-$ROOT/firmware/_work/acdc1-build6b-fx4b}"
SRC="$TREE/ACDC/Core/Src/ACDC.cpp"
[ -f "$SRC" ] || { echo "Not found: $SRC" >&2; exit 2; }
WORK="$(mktemp -d "${TMPDIR:-/tmp}/bootmenu.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT
# Menü-Block: vom Kommentarkopf bis vor den nächsten Abschnitt
awk '/^\/\* --- Boot menu: choose the patch slot at power-on/{p=1} /^#ifdef USE_FAST_POW_RESOURCES/{p=0} p' "$SRC" > "$WORK/menu.inc"
[ -s "$WORK/menu.inc" ] || { echo "No boot menu block in $SRC" >&2; exit 2; }
cp "$ROOT/firmware/sim/boot_menu_sim.cpp" "$WORK/sim.cpp"
c++ -std=c++17 -O1 -Wall -Wno-unused-function -o "$WORK/sim" "$WORK/sim.cpp" 2> "$WORK/cc.log" \
  || { grep -v xcrun_db "$WORK/cc.log" >&2; echo "Compile failed" >&2; exit 1; }
"$WORK/sim"
