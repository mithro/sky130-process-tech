#!/usr/bin/env python3
import re, sys, json
from pathlib import Path
from collections import Counter, defaultdict
ROOT = next(d for d in Path(__file__).resolve().parents if (d / "docs/steps").is_dir())  # repo root, wherever the script sits
pages = sorted((ROOT/"docs/steps").glob("[0-9][0-9][0-9]-*.md"))
N = len(pages)
def clean(t):
    t = re.sub(r"\[\^[^\]]+\]", "", t)
    t = re.sub(r"\{(ref|term|doc|math)\}`([^`<]*?)(?: <[^>]*>)?`", r"\2", t)
    return t
def q(v, f): v = sorted(v); return v[min(len(v)-1, int(f*len(v)))]
def rep(name, per_page_counts):
    v = [c for c in per_page_counts.values()]
    nz = [c for c in v if c]
    print(f"{name}: total={sum(v)} pages={len(nz)}/{N} median/page={q(v,.5)} p90={q(v,.9)} max={max(v)}")

def body_of(t): return t.split("<!-- footnotes -->")[0]
def sections(t):
    out = defaultdict(str); cur = "TOP"
    for l in body_of(t).split("\n"):
        if l.startswith("## "): cur = l[3:].strip(); continue
        out[cur] += l + "\n"
    return out
def prose_nonref(t):
    s = sections(t)
    return "\n".join(v for k, v in s.items() if k != "References")

# sentence stats
sent_len = []; long60 = Counter(); long40 = Counter(); dash2 = Counter(); semi3 = Counter(); paren3 = Counter(); longparen = Counter()
arith = Counter(); arith_ex = []
ex_long = []
for p in pages:
    t = p.read_text(); txt = prose_nonref(t)
    txt = re.sub(r"<!-- index-links:begin.*?index-links:end -->", "", txt, flags=re.S)
    txt = re.sub(r"^\|.*$", "", txt, flags=re.M)
    # paragraphs / list items as units
    units = re.split(r"\n\s*\n|\n(?=\s*(?:[*+-]|\d+\.) )", txt)
    for u in units:
        c = clean(" ".join(u.split()))
        if not c or c.startswith(":::") or c.startswith("#"): continue
        for s in re.split(r"(?:(?<=[.!?])|(?<=[.!?][\"”)]))(?<![Pp]p\.)(?<![Vv]ol\.)(?<!Proc\.)(?<!ch\.)(?<![Nn]o\.)(?<!Fig\.)\s+(?=[A-Z0-9`*\[“\"(])", c):
            w = len(s.split())
            if w < 3: continue
            sent_len.append(w)
            if w >= 40: long40[p.name] += 1
            if w >= 60: long60[p.name] += 1; ex_long.append((w, p.name, s[:90]))
            if s.count(" — ") + s.count("— ") >= 2 and s.count("—") >= 2: dash2[p.name] += 1
            if s.count(";") >= 3: semi3[p.name] += 1
            if s.count("(") >= 3: paren3[p.name] += 1
            for m in re.findall(r"\(([^()]*)\)", s):
                if len(m.split()) >= 15: longparen[p.name] += 1
        if re.search(r"\d[^.;]{0,40}[−×÷+/][^.;]{0,40}\s(=|≈)\s*[\d~]", c):
            arith[p.name] += 1; arith_ex.append((p.name, re.search(r".{0,60}\s(=|≈)\s.{0,30}", c).group(0)))
print(f"sentences: n={len(sent_len)} mean={sum(sent_len)/len(sent_len):.1f} median={q(sent_len,.5)} p75={q(sent_len,.75)} p90={q(sent_len,.9)} p95={q(sent_len,.95)} max={max(sent_len)}")
for nm, c in [("sentences>=40w", long40), ("sentences>=60w", long60), ("sentences with >=2 em-dashes", dash2), ("sentences with >=3 semicolons", semi3), ("sentences with >=3 parentheses", paren3), ("parentheticals >=15 words", longparen), ("units with inline arithmetic (= / ≈)", arith)]:
    rep(nm, {p.name: c[p.name] for p in pages})
print("longest:", sorted(ex_long, reverse=True)[:5])
print("arith examples:", arith_ex[:8])

# phrase counts
PH = {
 "Strength:": r"Strength:",
 "(category page)": r"\(category page[^)]*\)",
 "we infer / (inference)": r"\bwe infer\b|\(inference[^)]*\)|\binference\b",
 "our reading / our arithmetic / our extraction": r"\bour (reading|arithmetic|extraction|estimate|inference)\b",
 "this reference (self-ref)": r"\b[Tt]his reference\b",
 "is/are not public": r"\b(is|are) not public\b|not stated publicly|no public source",
 "industry-typical / industry-generic": r"industry-(typical|generic)",
 "collapsed note (pointer prose)": r"collapsed note",
 "may still be in force": r"may still be in force",
 "200 mm, 130 nm-era fab opener": r"An industry-generic [^\n]*(\n[^\n]*)?130 nm-era",
 "Without `X` ... closer": r"^Without `",
 "does not interpret the": r"does not interpret the",
 "see below / above": r"\b(see|noted|described|cited) (below|above)\b|\(below\)|\(above\)",
}
for nm, rx in PH.items():
    c = {p.name: len(re.findall(rx, prose_nonref(p.read_text()), flags=re.M)) for p in pages}
    rep(nm, c)

# code spans
c = {p.name: len(re.findall(r"(?<![`{}])`[^`\n]+`", re.sub(r"\{[a-z]+\}`[^`]*`", "", prose_nonref(p.read_text())))) for p in pages}
rep("code spans (non-role) outside refs", c)
selfcode = {}
for p in pages:
    t = p.read_text(); m = re.search(r"\*\*Step code\*\* \| `([^`]+)`", t)
    selfcode[p.name] = prose_nonref(t).count(f"`{m.group(1)}`") - 1 if m else 0
rep("own step code repeated in backticks", selfcode)

# footnotes
defs = {p.name: len(re.findall(r"^\[\^[^\]]+\]:", p.read_text(), flags=re.M)) for p in pages}
rep("footnote definitions", defs)
refs = {p.name: len(re.findall(r"\[\^[^\]]+\](?!:)", prose_nonref(p.read_text()))) for p in pages}
rep("footnote refs in body (excl. References)", refs)
mx = {}
for p in pages:
    units = re.split(r"\n\s*\n|\n(?=\s*(?:[*+-]|\d+\.) )", prose_nonref(p.read_text()))
    mx[p.name] = max(len(re.findall(r"\[\^", u)) for u in units)
rep("max footnote refs in a single paragraph/item", mx)
# share of page that is references+footnotes
shares = []
for p in pages:
    t = p.read_text(); tot = len(t.split())
    s = sections(t); r = len(s.get("References", "").split()) + len(t.split("<!-- footnotes -->")[1].split()) if "<!-- footnotes -->" in t else 0
    shares.append(r/tot)
print(f"References+footnote-defs share of page words: median={q(shares,.5):.2f} p90={q(shares,.9):.2f}")
# reference bullets & wikipedia
refb = Counter(); wikib = Counter(); linked = Counter()
for p in pages:
    r = sections(p.read_text()).get("References", "")
    items = re.split(r"\n(?=\* )", r)
    for it in items:
        if not it.startswith("* "): continue
        refb[p.name] += 1
        if it.startswith("* Wikipedia"): wikib[p.name] += 1
        if re.search(r"\]\(http|<http", it): linked[p.name] += 1
rep("reference-tier bullets", {p.name: refb[p.name] for p in pages})
rep("  of which 'Wikipedia, *Title*' bullets (footnote-only link)", {p.name: wikib[p.name] for p in pages})
rep("  reference bullets with a direct link", {p.name: linked[p.name] for p in pages})
# wikipedia footnotes cited in body prose
wb = {p.name: len(re.findall(r"\[\^wiki-[^\]]+\](?!:)", prose_nonref(p.read_text()))) for p in pages}
rep("wiki footnote refs in body prose", wb)

# dropdowns
dd = Counter(); dup = Counter(); tl = []; gen_dd = Counter()
for p in pages:
    t = body_of(p.read_text())
    hand = re.sub(r"<!-- index-links:begin.*?index-links:end -->", "", t, flags=re.S)
    titles = re.findall(r"^:::+\{dropdown\} (.*)$", hand, flags=re.M)
    dd[p.name] = len(titles); dup[p.name] = len(titles) - len(set(titles))
    tl += [len(x.split()) for x in titles]
    gen_dd[p.name] = len(re.findall(r"\{dropdown\}", t)) - len(titles)
rep("hand-written patent dropdowns", {p.name: dd[p.name] for p in pages})
rep("  repeated identical dropdown titles on a page", {p.name: dup[p.name] for p in pages})
print("  dropdown title words: median", q(tl,.5), "max", max(tl))
# index-links block kinds
kinds = Counter(); blk_lines = []
for p in pages:
    m = re.search(r"<!-- index-links:begin.*?-->\n(.*?)<!-- index-links:end -->", p.read_text(), flags=re.S)
    if not m: kinds["none"] += 1; continue
    b = m.group(1)
    blk_lines.append(len([l for l in b.split("\n") if l.startswith("* ")]))
    for k in ("Related patents", "Related papers", "Related filings"):
        if f"**{k}.**" in b: kinds[k] += 1
    if "see {ref}`patents-by-module`" in b or re.search(r"\d+ families concern", b): kinds["count-only variant"] += 1
    if "{dropdown}" in b: kinds["has generated dropdown"] += 1
print("index-links kinds:", dict(kinds), "bullets in block median", q(blk_lines,.5), "p90", q(blk_lines,.9), "max", max(blk_lines))

# tables, figures, extra headings, run-in heads
tb = {}; fig = {}; h3 = {}; runin = {}; pseudo = {}
for p in pages:
    t = body_of(p.read_text())
    tb[p.name] = len(re.findall(r"^\|[ -]*-[-| :]*\|\s*$", t, flags=re.M)) - 1
    fig[p.name] = len(re.findall(r"!\[|\{figure\}|\{image\}|\{mermaid\}|```\{", t))
    h3[p.name] = len([h for h in re.findall(r"^###+ (.*)$", t, flags=re.M) if h not in ("Cross-check", "High-level understanding", "Deep dive")])
    pseudo[p.name] = len(re.findall(r"^\*\*[^*\n]{3,80}[.?:]\*\*", t, flags=re.M))
    runin[p.name] = len(re.findall(r"^(?:[*+-]|\d+\.) \*\*[^*\n]+\*\*", t, flags=re.M))
rep("tables besides quick-facts", tb); rep("figures/diagrams/directive code blocks", fig)
rep("extra ### headings outside References", h3); rep("paragraph-start bold pseudo-headings", pseudo); rep("list items with bold run-in head", runin)

# opening paragraph
fp = []; fs = []
for p in pages:
    w = sections(p.read_text())["What this step is"].strip().split("\n\n")
    fp.append(len(clean(w[0]).split()))
    s1 = re.split(r"(?<=[.!?])\s+(?=[A-Z`])", clean(" ".join(w[0].split())))[0]; fs.append(len(s1.split()))
secw = defaultdict(list)
for p in pages:
    for k, v in sections(p.read_text()).items(): secw[k].append(len(clean(v).split()))
print(f"opening paragraph words: median={q(fp,.5)} p90={q(fp,.9)} max={max(fp)}; first sentence: median={q(fs,.5)} p90={q(fs,.9)} max={max(fs)}")
print("section word totals (median / p90 / max):")
for k, v in secw.items():
    if len(v) > 100: print(f"   {k:40} {q(v,.5):5} {q(v,.9):5} {max(v):5}")
# prev/next duplicated in Related
pn = sum(1 for p in pages if re.search(r"^\* (Previous|Next):", sections(p.read_text()).get("Related steps and cross-references", ""), flags=re.M))
cp = sum(1 for p in pages if re.search(r"^\* Category page:", sections(p.read_text()).get("Related steps and cross-references", ""), flags=re.M))
print("Related section repeats Previous/Next from quick facts:", pn, "pages; repeats 'Category page:'", cp)
