"""Check whether the English translations in docs/en/ are up to date.

German is the source. Each translation starts with a header that names its source file and the
SHA-256 of that file at translation time. This tool compares the recorded hash with the current
source and lists every translation as ok, stale, missing or unstamped.

Usage:
  python tools/i18n_check.py                 check all pairs, exit 1 if any is not ok
  python tools/i18n_check.py --stamp         write the header of every existing translation
  python tools/i18n_check.py --stamp FILE …  only for these translations (right after regenerating them)

Stamping records the current source hash and today's date. Only stamp a translation that was
regenerated from the current German source.
"""
import argparse
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Quelle (deutsch) -> Übersetzung (englisch). Neue Paare hier eintragen.
PAIRS = {
    "docs/01-hardware-und-firmware.md": "docs/en/01-hardware-and-firmware.md",
    "docs/02-noise-befunde.md": "docs/en/02-noise-findings.md",
    "docs/03-messplan-python.md": "docs/en/03-measurement-plan-python.md",
    "docs/04-software-filter.md": "docs/en/04-software-filter.md",
    "docs/05-firmware-plan.md": "docs/en/05-firmware-plan.md",
    "docs/06-hardware-mod-masse.md": "docs/en/06-hardware-mod-ground.md",
    "docs/99-quellen.md": "docs/en/99-sources.md",
}

HEADER_RE = re.compile(r"^<!-- i18n source=(\S+) sha256=([0-9a-f]{64}) date=(\d{4}-\d{2}-\d{2}) -->$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def split_header(text: str):
    """Trennt den Kopf (Kommentarzeile + Hinweis-Zitat + Leerzeile) vom Rest. Ohne Kopf: (None, text)."""
    lines = text.split("\n")
    if not lines or not HEADER_RE.match(lines[0]):
        return None, text
    i = 1
    while i < len(lines) and lines[i].startswith(">"):
        i += 1
    while i < len(lines) and lines[i] == "":
        i += 1
    return HEADER_RE.match(lines[0]), "\n".join(lines[i:])


def make_header(src: str, digest: str, date: str, dst: str) -> str:
    # Relativer Link von der Übersetzung zur Quelle
    rel = Path(*[".."] * (len(Path(dst).parts) - 1)) / src
    return (
        f"<!-- i18n source={src} sha256={digest} date={date} -->\n"
        f"> English translation of [`{src}`]({rel.as_posix()}), as of {date}. "
        "The German original is authoritative. This file is generated from it, do not edit it by hand.\n\n"
    )


def check() -> int:
    bad = 0
    rows = []
    for src, dst in PAIRS.items():
        s, d = ROOT / src, ROOT / dst
        if not s.exists():
            rows.append((dst, "source missing", src)); bad += 1; continue
        if not d.exists():
            rows.append((dst, "missing", "no translation yet")); bad += 1; continue
        m, _ = split_header(d.read_text(encoding="utf-8"))
        if m is None:
            rows.append((dst, "unstamped", "no i18n header")); bad += 1; continue
        if m.group(1) != src:
            rows.append((dst, "wrong source", f"header names {m.group(1)}")); bad += 1; continue
        if m.group(2) != sha256(s):
            rows.append((dst, "stale", f"source changed since {m.group(3)}")); bad += 1; continue
        rows.append((dst, "ok", f"as of {m.group(3)}"))
    w = max(len(r[0]) for r in rows)
    for dst, state, note in rows:
        print(f"{dst:<{w}}  {state:<14} {note}")
    if bad:
        print(f"\n{bad} of {len(rows)} translations need attention.")
    return 1 if bad else 0


def stamp(only) -> int:
    by_dst = {dst: src for src, dst in PAIRS.items()}
    targets = list(by_dst) if not only else []
    for f in only or []:
        rel = Path(f).resolve().relative_to(ROOT).as_posix()
        if rel not in by_dst:
            print(f"Not a known translation: {f}", file=sys.stderr)
            return 2
        targets.append(rel)
    today = dt.date.today().isoformat()
    for dst in targets:
        d, src = ROOT / dst, by_dst[dst]
        if not d.exists():
            print(f"skip   {dst} (missing)")
            continue
        _, body = split_header(d.read_text(encoding="utf-8"))
        d.write_text(make_header(src, sha256(ROOT / src), today, dst) + body.lstrip("\n"), encoding="utf-8")
        print(f"stamp  {dst}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stamp", nargs="*", metavar="FILE",
                    help="write the i18n header (all translations, or only the given files)")
    args = ap.parse_args()
    if args.stamp is not None:
        return stamp(args.stamp)
    return check()


if __name__ == "__main__":
    sys.exit(main())
