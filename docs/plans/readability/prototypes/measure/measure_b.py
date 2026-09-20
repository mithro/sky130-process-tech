"""Reviewer B detection heuristics. Run: python3 tmp/readability/tools-B/measure.py [--list]"""
import re, glob, sys, collections
LIST = '--list' in sys.argv
DIRS = ['machines', 'materials', 'masks', 'categories']
FN = re.compile(r'\[\^[^\]]+\]')
STEP = re.compile(r'\{ref\}`[^`]*step-\d{3}>?`')
def words(s): return len(FN.sub('', s).split())
def blocks(text):
    text = text.split('<!-- footnotes -->')[0]
    text = re.sub(r'<!-- index-links:begin.*?index-links:end -->', '', text, flags=re.S)
    return [b for b in re.split(r'\n\s*\n', text) if b.strip()]
tot = collections.Counter(); pages = collections.defaultdict(set); ex = collections.defaultdict(list)
def hit(k, f, b, n=1):
    tot[k] += n; pages[k].add(f)
    if LIST: ex[k].append(f'{f}: {b.strip()[:90]!r}')
for d in DIRS:
    for f in sorted(glob.glob(f'docs/{d}/*.md')):
        t = open(f).read()
        for b in blocks(t):
            s = b.lstrip()
            if s.startswith('|'):
                rows = [r for r in s.splitlines() if r.startswith('|')]
                ncol = rows[0].count('|') - 1
                if ncol >= 5: hit(f'table>=5cols', f, rows[0])
                for r in rows[2:]:
                    for c in r.strip('|').split(' | '):
                        if words(c) > 40: hit('tablecell>40w', f, c)
                        if len(STEP.findall(c)) >= 8: hit('tablecell>=8steplinks', f, c)
                continue
            if s.startswith('#') or s.startswith('(') and s.endswith(')=') or s.startswith('```') or s.startswith(':::'): continue
            if re.match(r'[*-] ', s):
                items = re.split(r'\n(?=[*-] )', s)
                for it in items:
                    if words(it) > 60: hit('bullet>60w', f, it)
                    if words(it) > 100: hit('bullet>100w', f, it)
                    if len(STEP.findall(it)) >= 8: hit('bullet>=8steplinks', f, it)
                continue
            w = words(s)
            if len(STEP.findall(s)) >= 6 and w < 6 * len(STEP.findall(s)): hit('steplink-run-paragraph', f, s); continue
            if w > 100: hit('para>100w', f, s)
            if w > 150: hit('para>150w', f, s)
            if s.count(';') >= 3 and not s.startswith('>'): hit('para>=3semicolons', f, s)
            for sent in re.split(r'(?<=[.?!])["”]?(?:\[\^[^\]]+\])*\s+(?=[A-Z])', FN.sub('', s)):
                if len(sent.split()) > 45: hit('sentence>45w', f, sent)
for k in sorted(tot): 
    print(f'{k:28s} {tot[k]:5d} in {len(pages[k]):3d} pages')
    if LIST:
        for e in ex[k][:8]: print('    ', e)
