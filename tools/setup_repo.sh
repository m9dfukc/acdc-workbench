#!/usr/bin/env bash
# Richtet einen frischen Klon ein. Wiederholbar, überschreibt nichts.
#
#   1. Submodul firmware/OpenWare holen (ohne dessen eigenes Submodul Libraries)
#   2. Remote `upstream` (RebelTechnology) im Submodul anlegen und holen.
#      Die Docs nennen Upstream-Commits, die an keinem Fork-Branch hängen (z. B. 7f3cc41, 62a0187).
#   3. Libraries-Tarball mit festem Commit nach firmware/downloads/ laden (für tools/build_acdc.sh)
#   4. Offizielle ACDC.bin v22.5.0 nach firmware/releases/ laden (nur zum Vergleich, nicht zum Flashen)
#
# Aufruf:
#   tools/setup_repo.sh [--no-upstream] [--no-downloads]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SUB="$ROOT/firmware/OpenWare"
UPSTREAM_URL="https://github.com/RebelTechnology/OpenWare.git"

LIB_COMMIT="9e8f64e07b7a64b76de32f67c164ecf9068b728c"
LIB_URL="https://codeload.github.com/pingdynasty/OpenWareLibraries/tar.gz/$LIB_COMMIT"
LIB_FILE="$ROOT/firmware/downloads/OpenWareLibraries-9e8f64e.tar.gz"
LIB_SHA="c56a465cf59086b2a1f742b7cb9848e17af4b3957108cc1289540b180ad69d88"

REL_URL="https://github.com/RebelTechnology/OpenWare/releases/download/v22.5.0/ACDC.bin"
REL_FILE="$ROOT/firmware/releases/v22.5.0/ACDC.bin"
REL_SHA="5f44a8116b9d0bd17e41ada3d8daa881e155e42e9c7717cd49c98422ff892c2b"

DO_UPSTREAM=1; DO_DOWNLOADS=1
for a in "$@"; do
  case "$a" in
    --no-upstream) DO_UPSTREAM=0;;
    --no-downloads) DO_DOWNLOADS=0;;
    -h|--help) sed -n '2,12p' "$0"; exit 0;;
    *) echo "Unknown argument: $a" >&2; exit 2;;
  esac
done

# Lädt eine Datei, falls sie fehlt, und prüft in jedem Fall die SHA-256.
fetch() {
  local url="$1" file="$2" sha="$3" got
  if [ ! -f "$file" ]; then
    echo "== download $(basename "$file")"
    mkdir -p "$(dirname "$file")"
    curl -fL --retry 2 -o "$file.part" "$url"
    mv "$file.part" "$file"
  fi
  got="$(shasum -a 256 "$file" | cut -d' ' -f1)"
  if [ "$got" != "$sha" ]; then
    echo "SHA-256 mismatch for $file" >&2
    echo "  expected $sha" >&2
    echo "  got      $got" >&2
    return 1
  fi
  echo "ok  $(basename "$file")  sha256 ${sha:0:12}…"
}

echo "== submodule firmware/OpenWare"
git -C "$ROOT" submodule update --init firmware/OpenWare

if [ "$DO_UPSTREAM" = 1 ]; then
  if ! git -C "$SUB" remote get-url upstream >/dev/null 2>&1; then
    git -C "$SUB" remote add upstream "$UPSTREAM_URL"
  fi
  echo "== fetch upstream (branches and tags)"
  git -C "$SUB" fetch --tags upstream
fi

if [ "$DO_DOWNLOADS" = 1 ]; then
  fetch "$LIB_URL" "$LIB_FILE" "$LIB_SHA"
  fetch "$REL_URL" "$REL_FILE" "$REL_SHA"
  echo "Note: the official ACDC.bin is for comparison only. Do not flash it, see docs/05-firmware-plan.md."
fi

echo "Done. Python environment: uv sync"
