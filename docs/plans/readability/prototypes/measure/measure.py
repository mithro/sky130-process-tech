#!/usr/bin/env python3
"""Measure paragraph/list-item/sentence statistics on step pages."""
import re, sys, json, statistics as st
from pathlib import Path
from collections import Counter, defaultdict
ROOT = Path(__file__).resolve().parents[3]
pages = sorted(p for p in (ROOT/"docs/steps").glob("[0-9][0-9][0-9]-*.md"))

def clean(t):
    t = re.sub(r"\[\^[^\]]+\]", "", t)
    t = re.sub(r"\{(ref|term|doc)\}`([^`<]*?)(?: <[^>]*>)?`", r"\2", t)
    return t
def words(t): return len(clean(t).split())

def blocks(text):
    """yield (section, kind, text, lineno) ; kind in para, item, table, other"""
    body = text.split("<!-- footnotes -->")[0]
    lines = body.split("\n")
    sec = "TOP"; sub = None
    i = 0; buf = []; kind = None; start = 0
    out = []
    def flush():
        nonlocal buf, kind
        if buf: out.append((sec, kind, "\n".join(buf), start))
        buf = []; kind = None
    infence = False
    for n, l in enumerate(lines, 1):
        if re.match(r"^\s*(:::+|```+)", l):
            flush(); infence = not infence if re.match(r"^\s*(:::+|```+)\s*$", l) or not infence else infence
            continue
        if l.startswith("#"):
            flush()
            if l.startswith("## "): sec = l[3:].strip()
            elif l.startswith("### "): sec = sec.split(" / ")[0] + " / " + l[4:].strip()
            continue
        if l.startswith("<!--") or re.match(r"^\(.*\)=$", l): flush(); continue
        if not l.strip(): flush(); continue
        if l.startswith("|"):
            if kind != "table": flush(); kind = "table"; start = n
            buf.append(l); continue
        if re.match(r"^\s*([*+-]|\d+\.) ", l):
            flush(); kind = "item"; start = n; buf.append(l); continue
        if kind is None: kind = "para"; start = n
        buf.append(l)
    flush()
    return out

allp = []; alli = []
persec = defaultdict(list)
for p in pages:
    for sec, kind, t, n in blocks(p.read_text()):
        w = words(t)
        if kind == "para":
            allp.append((w, p.name, n, sec)); persec[sec.split(" / ")[0]].append(w)
        elif kind == "item":
            alli.append((w, p.name, n, sec))
def dist(v, name):
    v = sorted(v); N = len(v)
    q = lambda f: v[min(N-1, int(f*N))]
    print(f"{name}: n={N} mean={sum(v)/N:.0f} median={q(.5)} p75={q(.75)} p90={q(.9)} p95={q(.95)} max={v[-1]}")
    for lo, hi in [(0,40),(40,80),(80,120),(120,160),(160,200),(200,300),(300,10000)]:
        c = sum(1 for x in v if lo <= x < hi); print(f"   {lo:>4}-{hi:<5} {c:>5} {100*c/N:5.1f}%")
dist([w for w, *_ in allp], "prose paragraphs")
print("pages with a paragraph >=120 words:", len({f for w, f, *_ in allp if w >= 120}))
print("pages with a paragraph >=200 words:", len({f for w, f, *_ in allp if w >= 200}))
dist([w for w, *_ in alli], "list items")
ref = [w for w, f, n, s in alli if s.startswith("References")]
non = [(w, f, n, s) for w, f, n, s in alli if not s.startswith("References")]
dist([w for w, *_ in non], "list items outside References")
print("list items >=80 words outside References:", sum(1 for w, *_ in non if w >= 80), "on", len({f for w, f, *_ in non if w >= 80}), "pages")
print("\nper section paragraph stats")
for s, v in sorted(persec.items(), key=lambda kv: -len(kv[1])):
    if len(v) > 20:
        v = sorted(v); print(f"  {s[:45]:45} n={len(v):4} median={v[len(v)//2]:4} p90={v[int(.9*len(v))]:4} max={v[-1]}")
print("\ntop 15 paragraphs")
for w, f, n, s in sorted(allp, reverse=True)[:15]: print(f"  {w} {f}:{n} [{s}]")
print("\ntop 10 list items outside refs")
for w, f, n, s in sorted(non, reverse=True)[:10]: print(f"  {w} {f}:{n} [{s}]")
json.dump({"paras": allp, "items": alli}, open(ROOT/"tmp/readability/a-tools/measure.json", "w"))
