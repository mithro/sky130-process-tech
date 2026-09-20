import re, collections
from pathlib import Path
D = Path("docs")
pages = [p for p in D.rglob("*.md") if "plans" not in p.parts and "references" not in p.parts]
DEFSTART = re.compile(r"^\[\^[A-Za-z0-9_-]+\]:", re.M)
REF = re.compile(r"\[\^([A-Za-z0-9_-]+)\]")
tier_bullets = 0; tier_single = 0; tier_with_inline = 0
wiki_refs_body = 0; wiki_refs_tier = 0; wiki_only_tier = 0; wiki_labels_total = 0
marker_only = 0; marker_heavy = []
quote_wiki = 0
bullets_nontier_end = 0
for p in pages:
    t = p.read_text()
    m = DEFSTART.search(t)
    body = t[:m.start()] if m else t
    # split refs section
    rm = re.search(r"^## References\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    tier = rm.group(1) if rm else ""
    prose = body.replace(tier, "")
    bl = re.split(r"\n(?=\* )", tier)
    for b in bl:
        if not b.startswith("* "): continue
        tier_bullets += 1
        r = REF.findall(b)
        if len(r) == 1: tier_single += 1
        if "](http" in b: tier_with_inline += 1
    labels = set(REF.findall(body))
    for l in labels:
        if l.startswith("wiki"):
            wiki_labels_total += 1
            inprose = len(re.findall(r"\[\^%s\]" % re.escape(l), prose))
            if inprose == 0: wiki_only_tier += 1
    # list items made only of markers / name + marker
    for b in re.findall(r"^[*-] +(.*(?:\n  .*)*)", prose, re.M):
        stripped = REF.sub("", b).strip(" .;,\n")
        if len(stripped.split()) <= 6 and REF.search(b):
            marker_only += 1; marker_heavy.append((str(p), b[:100].replace("\n"," ")))
print("tier bullets", tier_bullets, "single-marker", tier_single, "already inline link", tier_with_inline)
print("wiki labels (page,label) pairs", wiki_labels_total, "cited ONLY in the References tiers", wiki_only_tier)
print("short bullets (<=6 words + marker) outside References", marker_only)
for x in marker_heavy[:25]: print(x)
