import re, statistics, collections
from pathlib import Path
D = Path("docs")
pages = [p for p in D.rglob("*.md") if "plans" not in p.parts]
DEF = re.compile(r"^\[\^([A-Za-z0-9_-]+)\]:(.*?)(?=^\[\^[A-Za-z0-9_-]+\]:|\Z)", re.M | re.S)
REF = re.compile(r"\[\^([A-Za-z0-9_-]+)\](?!:)")
INL = re.compile(r"\]\((https?://[^)\s]+)\)")
AUTO = re.compile(r"<(https?://[^>\s]+)>")
rows = []
host_count = collections.Counter()
wiki_defs = 0; wiki_pages = 0; total_defs = 0; total_refs = 0
inline_ext = 0; marker_only_bullets = 0; marker_end_bullets = 0
for p in pages:
    t = p.read_text()
    defs = DEF.findall(t)
    body = DEF.sub("", t)
    refs = REF.findall(body)
    total_defs += len(defs); total_refs += len(refs)
    w = 0
    for lab, d in defs:
        urls = AUTO.findall(d) + INL.findall(d)
        for u in urls[:1]:
            host_count[re.sub(r"^www\.", "", u.split("/")[2])] += 1
        if any("wikipedia.org" in u for u in urls): w += 1
    wiki_defs += w; wiki_pages += bool(w)
    inline_ext += len(INL.findall(body)) + len(AUTO.findall(body))
    rows.append((len(defs), len(refs), w, str(p)))
print("pages", len(pages), "defs", total_defs, "refs", total_refs, "wiki defs", wiki_defs, "pages w/ wiki", wiki_pages, "inline ext links in body", inline_ext)
for kind in ["steps", "machines", "materials", "masks", "categories", "overview"]:
    r = [x for x in rows if f"docs/{kind}/" in x[3] and x[0]]
    if r:
        ds = [x[0] for x in r]; rs = [x[1] for x in r]
        print(kind, len(r), "defs median", statistics.median(ds), "max", max(ds), "refs median", statistics.median(rs), "max", max(rs), "wiki total", sum(x[2] for x in r))
print(sorted(rows, reverse=True)[:8])
print(host_count.most_common(25))
