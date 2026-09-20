#!/usr/bin/env python3
import re
from pathlib import Path
from collections import Counter, defaultdict
ROOT = Path(__file__).resolve().parents[3]
pages = sorted((ROOT/"docs/steps").glob("[0-9][0-9][0-9]-*.md"))
def clean(t):
    t = re.sub(r"\[\^[^\]]+\]", "", t)
    t = re.sub(r"\{(ref|term|doc|math)\}`([^`<]*?)(?: <[^>]*>)?`", r"\2", t)
    return t
def sections(t):
    t = t.split("<!-- footnotes -->")[0]
    t = re.sub(r"<!-- index-links:begin.*?index-links:end -->", "", t, flags=re.S)
    out = defaultdict(str); cur = "TOP"
    for l in t.split("\n"):
        if l.startswith("## "): cur = l[3:].strip(); continue
        out[cur] += l + "\n"
    return out
# 1. within-page repetition: 10-word shingles shared between two different H2 sections (excluding References)
K = 10
pages_rep = 0; tot = 0; ex = []
for p in pages:
    s = sections(p.read_text()); seen = {}
    shared = set()
    for k, v in s.items():
        if k in ("References", "TOP"): continue
        w = re.findall(r"[\w.%°µ]+", clean(v).lower())
        for i in range(len(w)-K+1):
            sh = " ".join(w[i:i+K])
            if sh in seen and seen[sh] != k: shared.add((sh, seen[sh], k))
            seen.setdefault(sh, k)
    # collapse overlapping shingles: count distinct (secA,secB) runs roughly by /K
    if shared:
        pages_rep += 1; tot += len(shared); ex.append((len(shared), p.name, sorted(shared)[0]))
print(f"pages with a 10-word run repeated in two different sections: {pages_rep}/171; shared shingles total {tot}")
for e in sorted(ex, reverse=True)[:8]: print("  ", e[0], e[1], e[2][1], "<->", e[2][2], "|", e[2][0])
pairs = Counter()
for p in pages:
    s = sections(p.read_text()); seen = {}
    for k, v in s.items():
        if k in ("References", "TOP"): continue
        w = re.findall(r"[\w.%°µ]+", clean(v).lower())
        prs = set()
        for i in range(len(w)-K+1):
            sh = " ".join(w[i:i+K])
            if sh in seen and seen[sh] != k: prs.add((seen[sh], k))
            seen.setdefault(sh, k)
        for pr in prs: pairs[pr] += 1
print("section pairs sharing text (pages):"); [print("  ", n, a, "<->", b) for (a, b), n in pairs.most_common(8)]
# 2. cross-page boilerplate sentences
sent = Counter()
for p in pages:
    s = sections(p.read_text())
    txt = clean(" ".join(" ".join(v for k, v in s.items() if k not in ("References", "TOP")).split()))
    for x in set(re.split(r"(?<=[.!?])\s+(?=[A-Z`*])", txt)):
        if len(x.split()) >= 8: sent[x] += 1
print("sentences repeated verbatim on >=10 pages:", sum(1 for v in sent.values() if v >= 10))
for x, n in sent.most_common(12): print("  ", n, x[:150])
# 3. table candidates
cand = Counter(); exs = []
for p in pages:
    s = sections(p.read_text())
    for k, v in s.items():
        if k in ("References", "TOP"): continue
        for it in re.split(r"\n\s*\n|\n(?=\s*(?:[*+-]|\d+\.) )", v):
            c = clean(" ".join(it.split()))
            nums = len(re.findall(r"\d[\d.,]*\s?(?:keV|MeV|nm|µm|Å|°C|cm⁻²|cm⁻³|mTorr|Torr|sccm|W\b|Ω|fF|V\b|min\b|s\b|%)", c))
            if nums >= 5 and c.count(";") >= 2:
                cand[p.name] += 1; exs.append((nums, p.name, k, c[:80]))
print(f"paragraphs/items with >=5 unit-bearing numbers and >=2 semicolons (table candidates): {sum(cand.values())} on {len(cand)} pages")
for e in sorted(exs, reverse=True)[:6]: print("  ", e)
# 4. Strength variants and SkyWater machines items
st = Counter()
for p in pages:
    for m in re.findall(r"Strength:\s*\**([A-Za-z]+)", p.read_text()): st[m.lower()] += 1
print("Strength values:", st.most_common())
# 5. How section form
form = Counter()
for p in pages:
    h = sections(p.read_text())["How it is typically performed"]
    n_num = len(re.findall(r"^\d+\. ", h, flags=re.M)); n_bul = len(re.findall(r"^\* ", h, flags=re.M))
    form["numbered" if n_num >= 3 else "bulleted" if n_bul >= 3 else "prose"] += 1
print("How-section form:", dict(form))
# 6. hand-written bold pseudo-headings at paragraph start
ps = Counter()
for p in pages:
    s = sections(p.read_text())
    for k, v in s.items():
        if k == "References": continue
        ps[p.name] += len(re.findall(r"(?:^|\n\n)\*\*[^*\n]{3,80}[.?:]\*\*", v))
print("hand-written bold pseudo-headings:", sum(ps.values()), "on", sum(1 for v in ps.values() if v), "pages")
# 7. intro sentences ending in colon before list ("Three reasons:")
# 8. Open questions item counts
oq = [len(re.findall(r"^\* ", sections(p.read_text())["Open questions"], flags=re.M)) for p in pages]
print("open-question bullets per page: median", sorted(oq)[85], "max", max(oq))
# 9. quoted material density
qd = [len(re.findall(r"“|\"[^\"]{10,}\"", sections(p.read_text())["What this step is"])) for p in pages]
print("quotes in 'What this step is': median", sorted(qd)[85], "max", max(qd))
