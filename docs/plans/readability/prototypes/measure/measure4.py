import re
from pathlib import Path
from collections import Counter
ROOT = next(d for d in Path(__file__).resolve().parents if (d / "docs/steps").is_dir())  # repo root, wherever the script sits
pages = sorted((ROOT/"docs/steps").glob("[0-9][0-9][0-9]-*.md"))
VERB = r"(?:showed|studied|described|describe|reviewed|review|found|traced|explained|introduced|established|treated|related|simulated|characterised|measured|reported|report|quantified|observed|modelled|compared|demonstrated|analysed|evaluated|examined|improved|give|gave|proposed|developed|identified|derived|investigated|discuss|discussed|applied|set out|surveyed)"
NAME = r"[A-Z][\w’'\-]+(?:, [A-Z][\w’'\-]+)*(?: and [A-Z][\w’'\-]+(?: [A-Z][\w’'\-]+)?| et al\.?| and co-workers)?(?:'s?)?"
rc = Counter(); para3 = Counter(); rules = Counter(); ex=[]
for p in pages:
    t = p.read_text().split("<!-- footnotes -->")[0].split("\n## References")[0]
    for u in re.split(r"\n\s*\n|\n(?=\s*(?:[*+-]|\d+\.) )", t):
        c = " ".join(u.split())
        n = len(re.findall(NAME + r"[^.;]{0,25}?\b" + VERB + r"\b", c))
        rc[p.name] += n
        if n >= 3: para3[p.name] += 1; ex.append((n, p.name, c[:70]))
        r = len(re.findall(r"\((?:[a-z0-9]+\.[0-9]+[a-z]?(?:, )?)+[^)]{0,25}\)|\b[a-z]{2,8}[0-9]?\.[0-9]{1,2}[a-z]?\b", c))
        if r >= 3: rules[p.name] += 1
print("author-verb roll-call clauses:", sum(rc.values()), "pages", sum(1 for v in rc.values() if v))
print("paragraphs/items with >=3 roll-call clauses:", sum(para3.values()), "on", len(para3), "pages")
print(sorted(ex, reverse=True)[:5])
print("paragraphs/items citing >=3 design-rule ids:", sum(rules.values()), "on", len(rules), "pages")
# lead-in sentence ending with colon then a bullet list (good) vs inline enumerations
inl = Counter(); exi = []
for p in pages:
    t = p.read_text().split("<!-- footnotes -->")[0].split("\n## References")[0]
    for u in re.split(r"\n\s*\n|\n(?=\s*(?:[*+-]|\d+\.) )", t):
        c = " ".join(u.split())
        for s in re.split(r"(?<=[.!?])(?<![Pp]p\.)(?<![Vv]ol\.)(?<!Proc\.)(?<!ch\.)(?<![Nn]o\.)(?<!Fig\.)\s+(?=[A-Z0-9`*])", c):
            # a colon or dash followed by >=3 semicolon/comma separated clauses, or ordinal markers
            if re.search(r"\b(first|one)\b.*\b(second|another)\b.*\b(third|finally|last)\b", s, flags=re.I) or re.search(r"\((a|i|1)\).*\((b|ii|2)\).*\((c|iii|3)\)", s) or (s.count(";") >= 2 and len(s.split()) >= 45) or re.search(r"[:—] [^.;]+,[^.;]+,[^.;]+,[^.;]+,[^.;]+(,| and | or )", s):
                inl[p.name] += 1; exi.append((p.name, s[:100]))
print("inline-enumeration candidate sentences:", sum(inl.values()), "on", len(inl), "pages")
for e in exi[:6]: print("  ", e)
