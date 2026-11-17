#!/usr/bin/env bash
# Host test of the project's own OWL patch code (owl/Tanh3Patch.hpp, owl/AcdcOutput.h):
# compiles it unchanged against a minimal stand-in for the OwlProgram API
# (owl/test/Patch.h) and checks levels, saturation, antialiasing, mix, CV and limiter.
#
# Usage: tools/test_owl_dsp.sh        Exit code 0 = all cases ok.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/owldsp.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT
c++ -std=c++17 -O1 -Wall -I"$ROOT/owl/test" -I"$ROOT/owl" -o "$WORK/test" "$ROOT/owl/test/dsp_test.cpp" 2> "$WORK/cc.log" \
  || { grep -v xcrun_db "$WORK/cc.log" >&2; echo "Compile failed" >&2; exit 1; }
"$WORK/test"
