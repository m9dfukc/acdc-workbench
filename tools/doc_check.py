"""Check the documentation before a push.

Checks, each reported as ok or with the offending places:
  1. CLAUDE.md is at most 200 lines long (it is loaded into every Claude Code session).
  2. Relative Markdown links point to existing files.
  3. Paths in backticks in the current documents exist. Chronicles (docs/05, docs/chronik.md,
     docs/messlog.md, docs/00, research notes) are skipped, they name paths as of their date.
  4. The English versions in docs/en/ are up to date (tools/i18n_check.py).
  5. The index at the top of docs/messlog.md matches the entries.

Usage:
  python3 tools/doc_check.py                  run all checks, exit 1 if one fails
  python3 tools/doc_check.py --messlog-index  rewrite the index in docs/messlog.md, then check
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_CLAUDE_LINES = 200

# Ordner, die bei der Suche nach Markdown-Dateien übersprungen werden (fremd, lokal oder erzeugt)
SKIP_DIRS = (".git", ".uv-cache", ".venv", "owl/vendor", "owl/patches-private", "firmware/_work",
             "firmware/downloads", "firmware/OpenWare", "docs/uebergaben", "backup", "reports")

# Dokumente, deren Pfadangaben heute stimmen müssen
CURRENT_DOCS = [
    "CLAUDE.md", "README.md", "README.de.md", "TODO.md", "firmware/README.md",
    "owl/README.md", "owl/README.de.md",
    "docs/01-hardware-und-firmware.md", "docs/02-noise-befunde.md", "docs/03-messplan-python.md",
    "docs/04-software-filter.md", "docs/06-hardware-mod-masse.md", "docs/07-werkzeuge-und-ablaeufe.md",
    "docs/99-quellen.md", "docs/en/README.md",
]
# Erste Pfadteile, die als Projektpfad gelten
TOP = ("docs", "tools", "analysis", "firmware", "owl", "recordings", "reports", "backup", ".claude", "LICENSES")
# Nur lokal vorhanden: auf einem frischen Klon fehlen sie, deshalb nicht prüfen
LOCAL_ONLY = ("backup/", "docs/uebergaben/", "firmware/_work/", "firmware/downloads/", "firmware/releases/",
              "owl/vendor/", "owl/patches-private/")

LINK_RE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
TICK_RE = re.compile(r"`([A-Za-z0-9_.][A-Za-z0-9_./-]*/[A-Za-z0-9_./-]*)`")
ENTRY_RE = re.compile(r"^### (.+)$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
ID_RE = re.compile(r"^((?:D\d+[a-z]?|S\d-\d))\b\s*[–:-]\s*(.*)$")
TAIL_DATE_RE = re.compile(r"\s*\(\d{4}-\d{2}-\d{2}[^()]*\)\s*$")
IDX_START, IDX_END = "<!-- messlog-index:start -->", "<!-- messlog-index:end -->"


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel == s or rel.startswith(s + "/") for s in SKIP_DIRS):
            continue
        yield rel, p


def check_claude_md():
    n = len((ROOT / "CLAUDE.md").read_text(encoding="utf-8").splitlines())
    if n > MAX_CLAUDE_LINES:
        return [f"CLAUDE.md has {n} lines, the limit is {MAX_CLAUDE_LINES}. Move history and procedures into docs/."]
    return []


def check_links():
    bad = []
    for rel, p in md_files():
        for m in LINK_RE.finditer(p.read_text(encoding="utf-8", errors="replace")):
            target = m.group(1)
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#")[0]
            if path and not (p.parent / path).exists():
                bad.append(f"{rel}: link to missing file {target}")
    return bad


def path_exists(doc: Path, token: str) -> bool:
    """Pfad vom Projekt-Root oder vom Ordner des Dokuments aus. `docs/05` gilt als Kurzform für `docs/05-…`."""
    for base in (ROOT, doc.parent):
        cand = base / token
        if cand.exists():
            return True
        if list(cand.parent.glob(cand.name + "*")) if cand.parent.exists() else False:
            return True
    return False


def check_paths():
    bad = []
    for rel in CURRENT_DOCS:
        doc = ROOT / rel
        if not doc.exists():
            continue  # z. B. Submodul owl nicht ausgecheckt
        seen = set()
        for m in TICK_RE.finditer(doc.read_text(encoding="utf-8", errors="replace")):
            token = m.group(1)
            if token in seen or token.split("/")[0] not in TOP:
                continue
            seen.add(token)
            if token.startswith(LOCAL_ONLY) or token.startswith("recordings/") and token != "recordings/manifest.toml":
                continue
            if not path_exists(doc, token):
                bad.append(f"{rel}: path `{token}` does not exist")
    return bad


def check_i18n():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "i18n_check.py")], capture_output=True, text=True)
    if r.returncode == 0:
        return []
    return [line for line in r.stdout.splitlines() if line.strip() and "  ok  " not in line]


def messlog_index(text: str) -> str:
    """Index aus den Einträgen (Überschriften der Ebene 3): ID, Datum, Titel."""
    rows = ["| ID | Datum | Eintrag |", "|---|---|---|"]
    for line in text.split("\n"):
        m = ENTRY_RE.match(line)
        if not m:
            continue
        head = m.group(1).strip()
        d = DATE_RE.search(head)
        idm = ID_RE.match(head)
        ident, title = (idm.group(1), idm.group(2)) if idm else ("–", head)
        title = TAIL_DATE_RE.sub("", title).replace("|", "\\|")
        rows.append(f"| {ident} | {d.group(0) if d else '–'} | {title} |")
    return "\n".join(rows)


def check_messlog(fix: bool):
    p = ROOT / "docs" / "messlog.md"
    text = p.read_text(encoding="utf-8")
    if IDX_START not in text or IDX_END not in text:
        return ["docs/messlog.md: index markers are missing"]
    head, rest = text.split(IDX_START, 1)
    old, tail = rest.split(IDX_END, 1)
    new = "\n" + messlog_index(tail) + "\n"
    if old == new:
        return []
    if fix:
        p.write_text(head + IDX_START + new + IDX_END + tail, encoding="utf-8")
        print("docs/messlog.md: index rewritten")
        return []
    return ["docs/messlog.md: the index is out of date, run tools/doc_check.py --messlog-index"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--messlog-index", action="store_true", help="rewrite the index in docs/messlog.md first")
    a = ap.parse_args()
    checks = [
        ("CLAUDE.md length", check_claude_md),
        ("Markdown links", check_links),
        ("Paths in current documents", check_paths),
        ("English versions", check_i18n),
        ("Lab notebook index", lambda: check_messlog(a.messlog_index)),
    ]
    failed = 0
    for name, fn in checks:
        problems = fn()
        print(f"{'ok  ' if not problems else 'FAIL'}  {name}")
        for line in problems:
            print(f"      {line}")
        failed += bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
