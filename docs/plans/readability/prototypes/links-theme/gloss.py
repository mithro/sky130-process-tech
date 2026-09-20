import re, collections
from pathlib import Path
g = Path("docs/glossary.md").read_text()
terms = re.findall(r"^([^\s`:#(].*)$\n    \S", g, re.M)
print("terms", len(terms))
pages = [p for p in Path("docs").rglob("*.md") if "plans" not in p.parts and p.name != "glossary.md" and "references" not in p.parts]
use = collections.Counter(); miss = collections.Counter()
for p in pages:
    t = p.read_text()
    body = re.split(r"^<!-- footnotes", t, flags=re.M)[0]
    linked = set()
    for m in re.finditer(r"\{term\}`([^`]*)`", body):
        x = m.group(1); mm = re.search(r"<(.*)>", x)
        linked.add((mm.group(1) if mm else x).lower())
    for l in linked: use[l] += 1
    plain = re.sub(r"\{term\}`[^`]*`", "", body); plain = re.sub(r"`[^`]*`", "", plain)
    for t_ in terms:
        if len(t_) < 3: continue
        if t_.lower() not in linked and re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(t_), plain):
            miss[t_] += 1
print("terms never linked from any page:", [t for t in terms if use[t.lower()] == 0][:40], sum(1 for t in terms if use[t.lower()] == 0))
print("top term used on page without any {term} link on that page:", miss.most_common(25))
print("total (page,term) pairs unlinked", sum(miss.values()), "linked", sum(use.values()))
