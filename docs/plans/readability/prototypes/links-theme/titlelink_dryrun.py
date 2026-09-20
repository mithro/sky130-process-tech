"""Dry run of rule C1 (title links in the three reading lists). Prints, never writes.
usage: python3 tmp/readability/c-work/titlelink_dryrun.py [docs/steps/006-stie.md ...]  (no args = whole site, counts only)"""
import re, sys
from pathlib import Path
DEF = re.compile(r"^\[\^([A-Za-z0-9_-]+)\]:(.*?)(?=^\[\^[A-Za-z0-9_-]+\]:|\Z)", re.M | re.S)
MARK = re.compile(r"\[\^([A-Za-z0-9_-]+)\]")
URL = re.compile(r"<(https?://[^<>\s]+)>")
def convert(bullet, urls):
    labs = MARK.findall(bullet)
    if len(labs) != 1 or labs[0] not in urls: return None, "multi-marker" if len(labs) != 1 else "no-url"
    m = re.match(r"\* (.*?)(\s+—\s)", bullet, re.S)
    if not m: return None, "no-dash"
    head = m.group(1)
    if "{" in head or "[" in head or "`" in head:
        it = re.findall(r"\*[^*]+\*", head)
        if len(it) != 1 or "{" in it[0]: return None, "role-in-head"
        new = head.replace(it[0], f"[{it[0]}](<{urls[labs[0]]}>)", 1)
    else:
        new = f"[{head}](<{urls[labs[0]]}>)"
    return "* " + new + bullet[m.end(1):], "ok"
files = [Path(a) for a in sys.argv[1:]] or [p for p in Path("docs").rglob("*.md") if "plans" not in p.parts and "references" not in p.parts]
stats = {}
for p in files:
    t = p.read_text()
    urls = {}
    for lab, d in DEF.findall(t):
        u = URL.findall(d)
        if u: urls[lab] = u[0]
    rm = re.search(r"^## References\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    if not rm: continue
    for b in re.split(r"\n(?=\* )", rm.group(1)):
        if not b.startswith("* "): continue
        b = b.split("\n\n")[0]
        new, why = convert(b, urls)
        stats[why] = stats.get(why, 0) + 1
        if sys.argv[1:] and new: print(new, "\n")
print(stats)
