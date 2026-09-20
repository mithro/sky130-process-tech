# Report C — site-level reading experience, links and references

Reviewer C, 2026-09-20. Source and rendered pages were both read (desktop; phone width for the landing page,
the overview and step 006). Prototypes and measurement scripts: `tmp/readability/c-work/`; screenshots:
`tmp/readability/shots/c-*.png`.

## Measurements (all of `docs/` except `plans/`)

| Measure | Value |
|---|---|
| Pages / footnote definitions / markers in running text | 291 / 8,412 / 22,742 |
| Footnotes per page, median (max) | step 30 (58) · machine 31 (46) · material 42 (60) · mask 29 (39) · category 43.5 (57) · overview 62.5 (79) |
| Markers per page, median (max) | step 69 (142) · machine 110 (149) · material 135 (236) · overview 250 (342) |
| **External links inline in the body of any hand-written page** | **0** — all are behind footnotes |
| Definitions pointing at Wikipedia | 804, on 263 pages (third host after doi.org 3,461 and PDK docs 805) |
| (page, `wiki-*`) pairs cited only in the reading lists | 298 of 796 |
| Reading-list bullets | 7,074; 6,398 end in exactly one marker; 0 contain a link |
| … convertible by script (dry run) | 6,200 (676 multi-marker, 176 without " — ", 16 role in head, 6 no URL) |
| Short "name + marker" bullets outside reading lists | 22 |
| Pages where one footnote is cited ≥ 17 times (C2) | 15 (worst: 81 on `machines/index.md`) |
| Glossary terms / `{term}` uses / never-linked terms | 219 / 2,550 / 15 |
| Inventory | 15,501 lines, 1,826 entries, 1.2 MB HTML, no entry anchors |
| URLs `check_links.py` never checks (generated pages) | 4,247 (3,569 Espacenet/Google Patents, ≈ 680 others) |
| Figures or images on the site | 0 |

## 1. Findings catalogue

### C1 — Reading lists are lists of footnote markers, not lists of links (P1, scripted)

**Problem.** The three reading lists exist so that a reader can open a source, yet each of 7,074 bullets ends
in a marker: click, land at the page foot, find the URL, click again, place lost. Nearly all the Wikipedia
"further reading" sits here. `docs/plans/citation-style.md` rule 5 currently forbids the fix ("Do not repeat
URLs in the bullets").

**Before** (`docs/steps/006-stie.md:215`):
```markdown
* Wikipedia, *Shallow trench isolation* — the three STI operations and
  the LOCOS cross-over node.[^wiki-sti]
```
**After:**
```markdown
* [Wikipedia, *Shallow trench isolation*](<https://en.wikipedia.org/wiki/Shallow_trench_isolation>) — the
  three STI operations and the LOCOS cross-over node.[^wiki-sti]
```

**Rule.** Inside `## References` only, per bullet:
1. One marker `[^k]`, and the text before the first ` — ` (the *head*) has no `{role}`, `[` or backtick: wrap
   the whole head as `[head](<URL>)`, URL = **first `<URL>` in the page's own `[^k]:` definition**. Angle
   brackets keep URLs with parentheses (`Etching_(microfabrication)`) valid.
2. Head has a role or backtick but exactly one `*italic title*`: link only that span.
3. N markers and exactly N italic titles in the same order (`docs/machines/pecvd.md:468`: "*Silane*,
   *Tetraethyl orthosilicate* and *Nitrogen trifluoride* …`[^wiki-silane][^wiki-teos][^wiki-nf3]`"): link
   title *i* to marker *i*'s URL. Anything else: leave alone.
4. **The marker always stays** — it carries the inventory key, keeps "every definition is referenced" true,
   and keeps the full citation one hover away (C3).

**Do not touch.** Definitions; the annotation after the dash; the number of bullets (`check_refs.py` counts
`^\* ` under `### Deep dive`); bullets inside a `{dropdown}` stay inside it (`check_inforce.py`); the
generated `index-links` block.

**Scripting.** `python3 tmp/readability/c-work/titlelink_dryrun.py [page]` prints converted bullets without
writing (no argument: site totals, `ok: 6200`). Promote it to `tools/fix_reading_list_links.py`; the ≈ 870
leftovers are hand work under rules 2–3. No current checker fails on the converted form. Plan change:
reword rule 5 ("the head of each bullet links to the footnote's first URL; the footnote keeps the full
citation") and add C4's invariant.

### C2 — Footnote back-reference lists break the phone layout (P1, one CSS line)

Before each footnote cited more than once, docutils prints "(1,2,3,…,77)" without spaces. It cannot wrap, so
on a phone the page becomes wider than the screen and **every paragraph is cut off at the right**
(`shots/c-overview-phone-01.png`; the `pdk-04` list on the overview measures 1,437 px in a 400 px viewport).
15 pages: both overview pages, the machines, materials and masks indexes, `machines/rapid-thermal-processor`
and nine more. Fix: `.footnote .backrefs { overflow-wrap: anywhere; }` in a new `docs/_static/custom.css`
(prototype `c-work/custom.css`; verified, `shots/c-proto-phone-01.png`). Wide tables are already safe (furo scrolls them).

### C3 — A marker costs two clicks and the reader's place (P1, theme-level, no content edits)

22,742 markers, each a tiny superscript (`[18][19]` is a 12 px target). Clicking jumps to the page foot; the
way back is a "(1,2,3,4)" list. **Fix:** `docs/_static/footnote-popover.js` (≈ 45 lines, no dependency;
prototype in `c-work/`, verified in `shots/c-proto-popover.png`): hover, keyboard focus or first tap shows
the footnote's text with its live links in a card beside the marker; `Esc` or click-away closes; a second tap
follows the anchor as today. It reads the existing `<aside class="footnote" id="label">`, so no page changes.
`conf.py`: `html_js_files = ["footnote-popover.js"]`, `html_css_files += ["custom.css"]`. Every evidence
footnote becomes "hover, one click", which is why C1 and C4 can keep all markers. `check_inforce.py` is
unaffected: the card shows only footnote *definitions*, which it already allows in the open.

### C4 — The policy: what becomes a direct link, what stays a footnote (P1)

| Kind of reference | Treatment |
|---|---|
| Evidence for a claim, number or quotation | **Footnote only**, as now. |
| A source *named* in prose by its italic title, with that source's marker in the same sentence ("the PDK's *Periphery rules* page …`[^pdk-periph]`") | Link the italic title to the definition's first URL, first occurrence per H2 only; marker stays. Exact title match finds 172 cases on 92 pages — scriptable. |
| Reading-list bullets (Wikipedia, textbooks, vendor pages, papers) | C1. |
| Short "name + marker" bullets elsewhere (22; `docs/steps/171-hpetest.md`: "**Probe cards** and probe-tip cleaning media.`[^wiki-probecard]`") | Leave: they are claims with evidence. |
| Vendor models in "Representative 200 mm-era models", "Machines typically used" | Footnote only: the footnote is the evidence, often a Wayback copy. |
| Generated index pages | Already inline; keep. |

**Invariant that keeps every key (new `check_refs.py` rule, ≈ 15 lines + a self-test).** *Every external URL
written inline in the body of a checked page must equal a URL inside one of that page's own footnote
definitions.* An inline link is then only a convenience copy of a keyed footnote: no key is lost, and
`check_links.py` still covers every URL. Split the page at the first `^\[\^`; collect
`<(https?://[^<>\s]+)>` from the definitions and `\]\(<(https?://[^<>\s]+)>\)` from the body; report
`body − defs`, and report any `](http` not in angle-bracket form.

Marker-free Wikipedia links are **not** recommended: they need a second key mechanism, leave 298 definitions
unreferenced (a `-W` error) unless deleted, and silently stale the inventory's "used on" lines.

### C5 — Dead links: rule and procedure (P1 for the rule; few links today)

**State.** `link-check-2026-09.md`: 6 dead of 1,791 tokens, 2 truly gone. But its table says "no snapshot"
for THUNG-2016 while the availability API returns one (re-queried 2026-09-20) — the API answers `{}`
intermittently and the tool caches that; 4,247 URLs on generated pages are never checked; and the 261
existing Wayback citations use several wordings.

**Rule.** *Dead* = two checks ≥ 24 h apart both fail (404/410/DNS/5xx/timeout) and the host is not in
`BLOCKED_HOSTS`. Never touch blocked-to-scripts. Then:

1. **Find.** `GET https://archive.org/wayback/available?url=<percent-encoded URL>&timestamp=<YYYYMMDD>`,
   `User-Agent: sky130-process-tech docs checker`; the timestamp is the citation's accessed/retrieved date,
   else 20260830 (the inventory's check date). Accept `archived_snapshots.closest` only with
   `available: true`, `status: "200"`. On `{}`: retry once after 10 s, then the other scheme, then
   with/without `www.`, then CDX
   (`https://web.archive.org/cdx/search/cdx?url=<url>&output=json&filter=statuscode:200&limit=-3&fl=timestamp,original`).
   One request per 3 s; never loop on an error.
2. **Verify.** Fetch `https://web.archive.org/web/<timestamp>id_/<original>` once; the title, or a string the
   pages quote from it, must be present. A captured soft-404 or redirect counts as no snapshot.
3. **Cite both URLs**, in every page footnote that repeats it and in the inventory entry:
   ```markdown
   [^key]: Author, *Title*, publisher, date.
       <https://web.archive.org/web/20260411150120/https://example.com/page>
       (Wayback Machine capture of 2026-04-11; original, dead since 2026-09-19:
       `https://example.com/page`).
   ```
   Archive URL **first** (C1 and the hover card use the first URL), always `https://`; the original in
   backticks — visible and searchable but not a link, so the checker stops re-reporting it. Use exactly the
   house wording "Wayback Machine capture of YYYY-MM-DD" (already in 100+ definitions).
4. **No snapshot** (also try `https://archive.ph/newest/<url>` by hand): rule 11 of `agent-briefs.md`,
   unchanged. A DOI whose landing page is broken (MERCKEL-1977, ROSENFIELD-1986) keeps the DOI plus a dated
   note; never replace a DOI by an archive URL.

**Automate in `check_links.py`?** Half. Yes: fix the lookup as in step 1 and never cache a negative answer
for more than a day; add `--suggest-archive`, printing for each dead token the ready-to-paste lines of step 3
and the files to change; add `--include-generated` to scan `docs/references/{patents,papers,filings}/`, with
Espacenet/Google Patents sampled (1 in 50), not crawled. No: it must not rewrite files — step 2 is a
judgement, and for generated pages the fix belongs in `data/*.yaml` (an `archive_url` field the generators
prefer).

### C6 — Landing page is a bare table of contents (P1, one page, hand edit)

**Problem.** `docs/index.md` is three paragraphs and a bulleted toctree that repeats the sidebar
(`shots/c-index-01.png`): nothing on who it is for, how big it is, how to read it, or that much is inference.

**Skeleton.** Keep the three paragraphs and footnotes verbatim. Then: (1) a `sphinx_design` card grid
(`::::{grid} 1 2 3 3`; `grid-item-card` with `:link:` + `:link-type: ref`), one sentence and a count per
card: Overview ("start here"), Process steps (171), Categories (10), Machines (30), Materials (12), Masks
(36), Glossary (219), References (1,826 sources + three indexes); (2) "The flow in 13 modules" — the first
four columns of the overview's module table, so a step is two clicks away; (3) four lines on how to read a
page (fact / typical / inference; footnotes), linking to the overview; (4) `:hidden:` on the three toctrees.
`docs/index.md` is not a `check_refs.py` target. The same defect opens `docs/machines/index.md:17-57` (30 bare
links): make it a table (class → one clause → number of steps); leave the checked table lower down untouched.

### C7 — The overview is an essay, not a guided tour (P2, hand edit, no fact changes)

**Problem.** 1,544 lines, 342 markers, 13 paragraphs over 120 words (longest 517). "How to read this
reference" starts at line 219, after the corporate history; a 250-line metal-cap argument interrupts the
tour; "A simplified cross-section" (line 798) describes a drawing that does not exist.

**Rules.** (1) Reorder H2s only (labels keep every link working): *How to read* → *The flow by module* →
*cross-section* → *Front end, middle of line and back end* → *What SKY130 is* → *metal cap* → *Key open
questions* → References. (2) Add a five-bullet "On this page" of `{ref}` links after the opening paragraph
(furo hides the contents list below ≈ 1,300 px). (3) Turn each run-in bold module paragraph ("**Wells and
threshold implants.** …") into an H3, so modules appear in the contents list and are linkable from C6/C8;
each collapsed in-force note stays directly after its paragraph. (4) The cross-section needs a figure.
(5) Owner: move the metal-cap section to its own page? 57 pages use its label (which would survive), but a new
page in `docs/overview/` must pass `check_refs.py` (≥ 12 Deep dive entries).

### C8 — The step list cannot be scanned (P2, generator change)

`docs/steps/index.md` is one ungrouped 171-row table, and the open sidebar is 171 two-line entries ("Step 095
— SACETCH: Sacrificial etch"). In `tools/gen_steps.py` (which already holds the phase boundaries): emit the
table as 13 H3 module groups, same rows and columns, so the contents list becomes a module jump list; give
toctree entries short titles (`006 STIE — Shallow trench etch <006-stie>`) so they fit one sidebar line (page
titles, URLs and previous/next labels are unaffected). Owner option: 13 module landing pages with nested
toctrees, giving 13 collapsible sidebar groups. Previous/next already follow process order; keep.

### C9 — Glossary: links are inconsistent and the page is hard to scan (P2, mostly scripted)

**Problem.** `{term}` is used 2,550 times, yet ≈ 2,100 (page, term) pairs have the term but no link on that
page, although the overview promises "linked from the pages on first use". The **Phase** row of every
quick-facts table (`| **Phase** | FEOL — isolation |`, 171 pages) is plain text. On the glossary page 219
terms render in normal weight with no A–Z navigation (`shots/c-glossary-01.png`); 15 terms are never linked.

**Rules.** (1) Script: make the leading `FEOL`/`MOL`/`BEOL` of the Phase cell a `{term}` (no checker reads
the row; update the stub template in `gen_steps.py`). (2) Per page, link the *first* prose occurrence of each
term (whole word; case-sensitive for acronyms) — never in headings, code spans, link text, table header rows,
footnote definitions, `## References`, or **inside quotation marks**. Plurals: ``{term}`vias <via>` ``. Skip
`via`, `liner`, `TED` (preposition; *IEEE TED*). (3) One `{glossary}` block per initial under `## A`…`## W`
plus an A–Z link line (Sphinx merges the blocks; every `{term}` still resolves); bold `dt` by CSS.

### C10 — The inventory is unusable as a page (P2/P3)

**Problem.** 1.2 MB of run-in paragraphs (`shots/c-pubsrc-02.png`); 1,711 of 1,826 entries under "## 8"; no
entry anchors, so nothing can link to "its" entry although label = key; 2,369 hand-written "Also used on …"
sentences that are exactly derivable from the pages' labels.

**Rules, cheapest first.** (1) Script an anchor line `(src-pdk-04)=` above every `**PDK-04** —`; the popover
can then add an "inventory entry" link (`…/public-sources.html#src-<footnote id>`) with no page edits.
(2) Script: move each entry's `Tier:` sentence and "used on" sentences to the end, each on its own line
(whole-sentence reordering only). (3) Owner: generate the "used on" lines as `{ref}` links, and/or split
section 8 into sub-pages. Nine tools in `tools/` read this one file, so a split means teaching them a glob.

### C11 — Generated indexes open with methodology and print 533 unclickable URLs (P2, generator change)

`references/patents/index.md` opens with a 797-word retrieval-accounting paragraph (`shots/c-patents-01.png`)
and puts its views last. `gen_patents.py` emits `**Verified:** … record page https://patents.google.com/…`
as bare text 532 times (MyST does not auto-link), plus the Cornell URL at `gen_patents.py:297`. In the
generators: order each index as purpose (one paragraph) → browse the views, with counts → how to read an
entry → legal caveat → a `{dropdown}` "Scope, method and counts" holding the present text verbatim (the papers
index already puts "Other views" second); wrap every emitted URL in `<…>`. Do not enable MyST `linkify`
(new dependency, touches every page).

### C12 — Theme polish (P3, `custom.css` + `conf.py` only)

In `c-work/custom.css`, furo variables only, so dark mode follows (dark mode not screenshotted — check by
hand): top-aligned cells and zebra rows (the overview's fact cells run to 9 lines against centred one-line
cells); sticky table header; 44 em measure for `p`/`li`/`dd` (lines are ≈ 100 characters today) while tables,
code and figures keep the full column; a "Sources cited on this page" label over the unlabelled footnote
block; small left-aligned figure captions; bold glossary terms. `conf.py`: `"navigation_with_keys": True`.
Not fixable in CSS: a marker wrapping to the next line ("fab. ⏎ [1][2]", `shots/c-index-phone-01.png`).

## 2. Page-type guidance (pages in this lens)

| Page type | Skeleton and limits |
|---|---|
| Landing | ≤ 120 words of prose → cards → 13-module table → how to read. No reading lists. Any section in one click, a module's first step in two. |
| Section indexes | Purpose (≤ 80 words) + a navigational **table** (name → one clause → count) on the first screen; methodology below it. Checked tables (`check_machines`, `check_masks`, `check_materials`) keep headings, column order and cell syntax exactly. |
| Overview | Order as C7. Paragraphs ≤ 90 words (cap 130); more than four markers in a paragraph → consider a list or table. One H3 per module. In-force dropdowns stay beside their paragraph. |
| Glossary | One block per letter; bold term; ≤ 80 words; first sentence expands the acronym; `{term}`/`{ref}` only. |
| References index | Add after paragraph 1 a four-row table (Inventory · Papers · Patents · Filings: count + one clause). Update "How citations work" for C1 and C3. |
| Inventory | Entry = anchor, bold key, bibliographic sentence, URL(s), what it gives, then `Tier:` and "used on" last. Keep all headings. |
| Generated indexes | Purpose → browse → how to read → caveat → collapsed methodology. Every URL clickable. |
| Citations on content pages | Prose: marker after the claim; at most one named-title link per source per H2. Reading lists: head is a link, marker last. Definitions: format unchanged; archive URL first when the original is dead. |

## 3. Risks and open questions for the coordinator

1. **Amend `citation-style.md` rule 5 and add the C4 invariant to `check_refs.py` in one change**, before C1
   runs; otherwise inline links drift from the footnotes.
2. **Order.** C2 + C3 are theme-only and relieve the "two clicks" complaint on all 291 pages at once: do them
   first. Run C1's script *after* other reviewers' rules that reorder or re-wrap reading-list bullets, then
   `check_refs`, `check_inforce`, `gen_index_links --check` and a `-W` build.
3. **In-force patents.** C1 edits bullets in place (a bullet in a `{dropdown}` stays there); the hover card
   shows only footnote definitions, which already sit in the open with the flag sentence. Owner to confirm
   the card is acceptable for those.
4. **Long source lines.** `[head](<URL>)` cannot break between `]` and `(`; accept lines over 100 columns.
5. **New pages.** Anything new under `overview/`, `machines/`, `materials/`, `masks/`, `categories/` must
   carry footnotes and a 12-entry Deep dive; put navigation/how-to pages at top level or add an exemption list.
6. **Owner decisions:** module pages in the sidebar (C8); moving the metal-cap section (C7); splitting the
   inventory / generating "used on" (C10); the 44 em measure (C12); whether `--include-generated` may sample
   patent-office hosts (C5); "Read more" Wikipedia links in glossary entries (would need footnotes there).
7. **The link-check report is wrong on one point:** it lists THUNG-2016 as "no snapshot"; the API returns
   one. Fix the lookup before "no snapshot" is used to apply rule 11, which deletes quotations.
8. **Not verified:** dark mode; site search; the popover on a real touch device.
