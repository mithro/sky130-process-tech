# Report B — machine, material, mask and category pages, and their indexes

Scope: `docs/machines/` (30 + index), `docs/materials/` (12 + index), `docs/masks/` (36 + index),
`docs/categories/` (10 + index): 92 pages, ~409,000 words. Read in source and rendered at desktop width:
machines/index, duv-krf-stepper, pvd-cluster-tool, wet-bench; materials/index, process-gases; masks/index, fom,
vim2; categories/etch. Source only: starting-material, sputter-targets, wet-chemicals, nsdm, rrpm, implant, cmp,
substrate. Phone width (400 px): machines/wet-bench, machines/index, masks/index. Shots: `tmp/readability/shots/b-*`.
Counts come from `tmp/readability/tools-B/measure.py` (`--list` prints hits) and the greps quoted. Proposed syntax
was built with `sphinx-build -W` in a scratch project (myst, sphinx_design, furo): `{table}` wrapper with
caption/`:widths:`/`:class:`, `{dropdown}`, `{grid}` cards, `{tab-set}`, definition lists pass; `{numref}` fails
(numfig is off) — never use it.

Headline numbers for the 92 pages: 185 tables, 0 captions; 0 figures; 0 admonitions; 351 paragraphs > 150 words
(88 pages); 253 bullets > 60 words; 124 step-link runs of 6–160 links (37 paragraphs, 41 bullets, 46 index
cells); 296 "Wikipedia, *Title*.[^n]" reference bullets (90 pages); 1,975 step links whose text is a bare number.

## 1. Findings catalogue

### B1. "Which steps use this" is a comma-separated blob — P1, scriptable
**Wrong.** Every machine and material page answers its most-asked question with one paragraph of up to 160
links: no step numbers, names or grouping, and on machine pages the role markers (`*alternative:*`, `*also for a
clean or strip:*`) sit mid-run.
**Before.** `docs/materials/process-gases.md:307` — `Steps:` then 142 links (`{ref}`SMAT <step-001>`, {ref}`BOX
<step-002>`, …`); `docs/machines/wet-bench.md:213` — 4 main + 36 "also" links.
**After.**
```
:::{table} SKY130 steps assigned to the KrF exposure class
:widths: 8 14 40 38
| Step | Code | Name | Role on this page |
|---:|---|---|---|
| 4 | {ref}`FOM <step-004>` | Field oxide mask | main; i-line is the fallback |
| 7 | {ref}`DNM <step-007>` | Deep N-well mask | alternative |
:::

:::{dropdown} The same 18 steps as one line of links (checked against the machines index)
{ref}`FOM <step-004>`, … ; *alternative:* {ref}`DNM <step-007>`, …

:::
```
**Rule.** (1) Run of ≤ 25 links: add a table `Step | Code | Name | Role`; Name from the step-page title; Role
only from the page's markers and existing grouped bullets ("main", "alternative", the `*also …:*` wording).
(2) Run of > 25 links: no table; keep the page's grouped bullets ("Nitrogen almost everywhere …") first and put
the run in a `{dropdown}` titled "All N steps (links)". (3) The run stays byte-identical. On machine pages it
must remain the *first* non-bullet block containing step links under its H3 — so the dropdown goes before the
new table there; on material and mask pages it must directly follow the `Steps:` line (both may sit inside the
dropdown). Blank line before the closing `:::`. Verified: `check_materials.py` passes with this wrapping.
**Detect.** `measure.py`: `steplink-run-paragraph`, `bullet>=8steplinks`, `tablecell>=8steplinks`.
**Do not touch.** Link order, markers, the `N steps; see …` quick-facts row. Mask pages (≤ 6 steps, one bullet
per step already) need nothing.
**Scriptable.** Yes; best as a generator (`gen_step_tables.py`, marker-delimited like `index-links`) fed by
`tools/steps.csv` and the index rows, so the table cannot drift from the checked run.

### B2. Index lookup tables: prose cells and link blobs in narrow columns — P1
**Wrong.** furo's text column is ~740 px. `machines/index.md:231` has 4 columns, three of prose: "What it does"
renders ~160 px wide and one row (RTP) is 370 px tall (`b-machines-index-04.png`). `materials/index.md:236` has
6 columns × 66 rows; the last cell holds up to 142 numeric links two abreast — the argon row is 850 px tall and
the table overflows (`b-mat-index-06.png`). `masks/index.md:178` has 6 columns; at 400 px 2½ are visible and the
key column scrolls away. Finding "the machine for step 89" means Ctrl-F.
**After.**
* *Machines index.* Replace the 30-link toctree echo at the top (duplicates the sidebar; make the toctree
  `:hidden:`) with a `{grid} 1 2 2 2` of cards under the eight unit-process groups the page already names: card
  title = class link, body = today's "What it does" cell, footer = today's "Tools SkyWater lists" cell with its
  footnotes. The lookup table becomes `Machine class | Steps`. **Checker change:**
  `check_machines.index_rows()` demands `len(cells) == 4` and reads `cells[3]` → "first cell links a machine
  label; Steps = last cell".
* *SkyWater-tools table* (`machines/index.md:344`; no checker reads it): one row per (tool, grade) instead of
  run-in italics inside one cell: `Tool as listed | Grade in the step pages' words | Steps`. Split each third
  cell at `; *grade:*`; nothing else changes.
* *Materials index.* Two tables keyed by material: (a) `Material | Class page | Role | SkyWater evidence`;
  (b) `Material | Steps`, "all except …" kept, cells over 25 links shown as a count plus a link to the class
  page's steps section. **Checker change:** `check_materials.Index` needs 6 cells, key first, Steps sixth →
  read Steps from table (b) by key. Without it only the cosmetic fix is possible (`{table}` with `:widths: 8 16
  12 22 22 20` plus CSS, section 3).
* *Masks index.* Keep the six checked columns; wrap in `{table}` with caption; add above it an unchecked
  navigation table `Step no. | Mask page | Exposure class (machine-page link) | Min. CD | Steps patterned`. The
  masks index has 0 links to machine pages today.
* *Reverse lookup.* Nothing answers "step N → machine class, mask". Add `Machine class` and `Mask` columns to
  the generated `docs/steps/index.md` (`gen_steps.py`) by inverting the machines-index Steps cells (main list)
  and the masks-index Patterns column. No new facts.
**Do not touch.** Cell wording, quotations, footnotes, row order of checked tables.

### B3. Lookup content buried under methodology — P1, move-only hand edit
Main tables start at line 231/640 (machines), 236/640 (materials), 178/870 (masks), after 1,500–2,500 words of
evidence policy. **Rule.** Index order: (1) purpose, ≤ 80 words; (2) navigation (cards, lookup table);
(3) detail tables; (4) "How to read this index" — the evidence and grading text, unchanged; (5) open questions;
(6) references. Move whole H2 sections with their `(label)=` lines; rewrite nothing. The three index checkers
find sections by H2 title, not position — confirm by running them.

### B4. "Representative models / materials and grades": tabular data as vendor paragraphs — P1
**Wrong.** Model, year, type and headline figure are what readers compare; they sit in 40–110-word bullets.
42/42 class pages have no table in this section (3–6 bullets, 113–283 words).
**Before.** `docs/machines/duv-krf-stepper.md:144` — `* **ASML.** Its first KrF stepper, the PAS 5000/70 of
1991, had NA 0.42;[^kato-2007] its first step-and-scan tool, the PAS 5500/500 of 1997, had "a resolution of
0.22µm, with 96wph throughput (200mm)".[^kato-2007] The PAS 5500/350C is …`
**After.**
```
:::{table} Representative KrF exposure tools of the 200 mm era (figures as each source gives them)
:widths: 12 20 8 12 48
| Vendor | Model | Year | Type | Published figures |
|---|---|---:|---|---|
| ASML | PAS 5000/70 | 1991 | stepper | NA 0.42[^kato-2007] |
| ASML | PAS 5500/500 | 1997 | scanner | "a resolution of 0.22µm, with 96wph throughput (200mm)"[^kato-2007] |
:::
```
then the non-tabular sentences (litigation, "still used in 2014", "no vendor description was retrieved")
unchanged as a short paragraph.
**Rule.** One row per model (material pages: `Material | As supplied | Specification | Note`, e.g.
`wet-chemicals.md` "49% (48–52%)" / SEMI C28). A value the page does not give is "—"; never fill from memory.
Quotation marks and footnotes travel with the value. What fits no column stays as prose below.
**Detect.** No `^|` line between `## Representative` and `## At SkyWater`. **Scriptable.** No.

### B5. "Quick facts" are not quick — P2
Machine quick-facts cells: median 30 words, 162 of 248 over 25, 46 over 40 — stitched quotations
(`duv-krf-stepper.md:22` "Light source": 38 words, 6 quotes); at 400 px one cell fills the screen
(`b-wet-400-01.png`). Mask quick facts (median 9 words) are the model. **Rule.** Cell ≤ 20 words: value first,
at most one quotation, footnotes, pointer to the section. Text taken out must already be in the body or be moved
there with its citations — check before deleting. Keep all row labels; on mask pages do not edit the cells the
checker compares with the index (PDK mask, layers, CD, mask type, plates, dies). **Detect.** `tablecell>40w`
(97 cells, 42 pages). Not scriptable.

### B6. "Read term by term" paragraphs — P2
34 pages follow the SkyWater blockquote with a 120–200-word paragraph glossing each quoted entry in turn,
semicolon-separated (`duv-krf-stepper.md:191`); mask pages do the same with the mask-type code (`vim2.md`, "The
mask-type record"). **After.** Table (or definition list when there are two columns): `Entry as listed | What
it names | Status`, Status being the page's own hedge ("SkyWater statement", "our reading", "our inference",
"not stated"). One row per quoted entry; hedges copied, never upgraded; sentences about the list as a whole stay
as prose. **Detect.** `grep -rl "term by term"`; `para>=3semicolons` (129 paragraphs, 65 pages).

### B7. Category pages: comparisons in bullets; consumables link nowhere — P2
`categories/etch.md:86` "Chemistries by material": seven bullets shaped `material (steps): gases; mechanism` —
a table in disguise (`cmp.md:134` already does it right). "Typical consumables" (`etch.md:217`) names ~25
materials, yet the ten category pages contain 0 links to material pages. The steps table (`Step | Code | Name`)
omits the machine class. **Rule.** (1) ≥ 3 bullets of the shape *thing (steps): values; explanation* → table
`Material | SKY130 steps | Typical chemistry | Why`; explanations over 40 words stay as prose below under the
same names. (2) Each consumables lead-in becomes a link to its material page, mapped through the class-page
table of `materials/index.md`. (3) Add `Machine class` to the steps table from the machines index. (2) and (3)
are scriptable.

### B8. Bold run-in pseudo-headings on mask pages — P2, needs checker change
"Lithography and pattern transfer" runs 600–900 words structured only by `**Exposure class.**`, `**Mask
errors.**`, `**Overlay.**`, `**Pattern transfer.**` … (208 lead-ins, 36/36 pages) — absent from the contents
sidebar, not linkable. `check_masks.py` forbids H3s under this H2. **Change.** Add to `OPTIONAL_H3` for it:
`Exposure class`, `Mask errors`, `Resist and tone`, `Overlay and alignment`, `Pattern transfer`, then free
extras; convert by script (`^\*\*(.+?)\.\*\* ` at paragraph start → `### \1`). Merge only true synonyms
(`Resist`/`Resist and tone`; `Overlay`/`Alignment`). Without the checker change, leave alone.

### B9. Step links that show only a number — P2, scriptable
1,975 links in 11 files render as "089" where the rest of the site shows "PSG". **Rule.** Link text = step code
everywhere; tables with a Step-number column show both. Index cells need only *start* with a link, so checkers
pass. **Detect.** `grep -rE '\{ref\}`[0-9]{3} <step-'`; map from step titles.

### B10. Reference bullets hide the link behind a footnote — P1, scriptable (shared finding)
`categories/etch.md:295`: `* Wikipedia, *Plasma etching*.[^wiki-plasma-etch]` — two clicks to Wikipedia. 2,779
tier bullets on my pages share the shape, 296 of them Wikipedia. **Rule.** Title becomes the link, footnote
stays: `* Wikipedia, [*Plasma etching*](https://en.wikipedia.org/wiki/Plasma_etching).[^wiki-plasma-etch]`;
URL copied from that page's footnote definition (the archive URL where the definition marks the live one dead).
`check_refs.py` still passes; confirm `check_links.py` tolerates the duplicates.

### B11. Generated index-links block floats without a heading — P2, generator change
Spliced before `## References`, it renders as the tail of whatever comes first: under the steps table on all 10
category pages (`b-etch-04.png`), under "Safety and abatement" (materials index), under the renders section
(masks index); 47 of 60 land in "Related pages". **Change `gen_index_links.py`** to emit either its own H2
`Related patents, papers and filings` (add it to the three checker templates) or, with no checker change, one
`:::{dropdown} Related index entries: 9 patents, 4 filings`. In-force families stay in their inner dropdown.

### B12. "Related pages" as 8–16 sentence-bullets — P3
`duv-krf-stepper.md:333-352`: seven bullets beginning "per-mask pages for …". **Rule.** Group under bold labels
(Category · Machines · Materials · Masks · Indexes); ≤ 12 words of gloss per link; ≥ 6 masks with one gloss →
one line. Drop no link. Only 2 of 30 machine pages link mask pages; add the reverse of each mask page's
"Exposure class" row (scriptable).

### B13. No captions; unit caveats arrive after the table — P2
185 tables, 0 captions. Design-rule tables mix "0.150 µm" and bare "0.290" (faithful to the PDK) and explain it
two paragraphs later (`fom.md:328`). **Rule.** Wrap every non-quick-facts table in `:::{table} Caption`:
what the rows are, source, unit note ("values in µm where the PDK gives a unit; blank units are blank in the
PDK"). Checkers match lines starting `| ` and are unaffected (verified for materials; run the rest).

### B14. Number-dense paragraphs after tables — P2
Mask "Design rules" sections add 120–370 words of "Table 2 gives … `FOMCD` 0.14 …; Table 7 gives … 0.135
(`FOMSE`) …" (`fom.md:331`; 36/36 pages). **Rule.** ≥ 4 named parameters with values in a paragraph → second
table `Parameter | PDK table | Published description | Value`; interpretation ("the PDK does not reconcile …",
"our reading") stays as prose.

### B15. Oversized paragraphs, bullets, intros — P1 (prose rules: see other reports)
Intros: median 145 (machines), 162 (materials), 184 (masks) words, including the boilerplate "This page
describes the class in general, lists …" (62 pages); category pages have no intro at all. **Rule.** Intro ≤ 70
words: what it is, what it does in SKY130. Pointer sentences ("… is on the category page") move to one
`{seealso}` under the quick-facts table; delete only the sentence listing the page's own sections.

### B16. Three orderings of the 30 machine classes — P3
Toctree/sidebar (implanters first), main table (starting material first) and the eight-group list differ.
**Rule.** One order: the eight groups, flow order within each; eight captioned toctrees group the sidebar too.

### B17. No figure on any of the 92 pages — P1 (detail: diagrams reviewer)
Minimum: machine page — block schematic; category page — before/after cross-section; mask page — link or
thumbnail of the already-cited public render (`[^mask-renders]`); masks index — masks against the flow. No
mermaid/graphviz extension is enabled: static SVG in `{figure}`.

## 2. Page-type guidance

### Table design rules
1. **Column budget.** ~740 px desktop, ~370 px phone. Any prose column: ≤ 4 columns, ≤ 2 of prose. All cells
   codes/numbers/≤ 3 words: ≤ 6. Wider → split by key, transpose, or move a column to cards/definition list.
2. **Order.** Reader's key first; identifiers; numbers; prose; steps/link-out last. Tooling slugs
   (`` `forming-gas` ``) are not reader keys (today `check_materials` wants them first).
3. **Cells.** ≤ 25 words, ≤ 8 links; more → "N steps — see §…". Run-in italic sub-labels inside a cell mean a
   missing row or column.
4. **Units in headers** ("Value (µm)"); per-cell units only where the source is inconsistent, said in the caption.
5. **Alignment.** Numbers, step numbers, years right (`---:`); all else left; never centred.
6. **Caption + `:widths:`** on every table with a prose column. No `{numref}`.
7. **> 40 rows:** split by group under H3s.
8. **Container.** One thing, attribute–value → 2-column quick facts. Term → cited explanation → definition
   list. Same attributes for ≥ 3 things → table. Navigation to ≤ 12 targets with a blurb → `{grid}` cards.
   Two views of one dataset (by class / by SkyWater tool) → `{tab-set}`. Checked raw link runs and generated
   blocks → `{dropdown}`. A caveat governing the whole page ("SKY130 recipes are not public") → one `{note}`.
9. **Checked tables stay pipe tables**, rows starting `| `, cells split by ` | `: machines main table;
   materials main, class-page and summary tables; every masks-index table named in `check_masks.py`; mask
   quick facts and plate tables. No `list-table` there.

### Machine page (H2s fixed by `check_machines.py`)
Intro ≤ 70 words → quick facts → `{seealso}` → **How it works**: H3 per subsystem, opening paragraph ≤ 60
words, one schematic → **Models**: table + ≤ 3 remarks (B4) → **At SkyWater**: blockquote, entry table (B6);
*Strength*: grade in bold in the first sentence, ≤ 80 words; *Steps*: dropdown run, steps table or grouped
bullets, grade table `Tool | Grade | Steps` (B1) → **Consumables**: bullets whose lead-ins link material pages
→ **Integration notes**: bullets ≤ 60 words, lead-in names the steps → grouped Related pages → generated block
→ References → Open questions, one question per bullet (split the three-in-one bullets).

### Material page (`check_materials.py`)
As machine. Grades table (B4); the supplier table at `sputter-targets.md:195` is the model for "What SkyWater's
filings list"; keep the checked `* `key` — name` bullets and add after the steps paragraph a table `Material |
Steps (count) | Used for` built from the grouped bullets.

### Mask page (strictest checker; already the most consistent)
Leave quick facts, plates table, step bullets, design-rule table. Add H3s (B8), parameter table (B14),
captions, shorter intro, render link/figure. The identical reticle-set column on all 36 pages is
checker-enforced; leave.

### Category page (no heading checker)
Add a ≤ 60-word intro and a quick-facts table (`What it does | Steps in SKY130 (N) | Tool classes (links) |
Consumable classes (links) | Governing relation`). Comparisons as tables (B7). "Typical equipment" → `Tool
class (link) | Representative models | Note`, deferring model history to the machine page.

### Lengths
Paragraph ≤ 120 words (flag 150); sentence ≤ 35 (flag 45; one quotation per sentence); bullet ≤ 60; intro ≤ 70;
cell ≤ 25.

## 3. Risks and open questions

1. **Checker/generator changes requested:** `check_machines.index_rows` (2-column main table);
   `check_materials.Index` (Steps from a second table; key not first); `check_masks.OPTIONAL_H3`;
   `gen_index_links.py` heading or dropdown (+ H2 in three templates); `gen_steps.py` columns; new
   `gen_step_tables.py`. Without them B2 (machines, materials) and B8 are cosmetic only.
2. **Site CSS** (new file in `html_css_files`): smaller font and sticky first column inside `.table-wrapper`,
   min-width on steps columns, no-wrap quick-facts labels. Fixes phone scrolling for all 185 tables; needs the
   owner's approval since it is not a content edit.
3. **Checkers are positional text parsers.** On a machine page any block with step links placed before the
   checked run is mistaken for it. After each page: the four page checkers, `check_refs`, `check_inforce`,
   `gen_index_links.py --check`; then a `-W` build.
4. **Fact safety when tabulating.** The main risk in B4–B6 is a weaker model "completing" a table. Require:
   blanks are "—"; the 408 hedges ("(inference)", "our reading", "not stated") are copied verbatim; every moved
   value keeps its footnote; per page, the multisets of quoted strings, `[^labels]` and numbers must be
   unchanged apart from added step numbers/names (scriptable diff). Sentences that mention a patent "that may
   still be in force" (e.g. `starting-material.md:25`) and existing in-force dropdowns must be moved whole, never
   expanded — `check_inforce.py`.
5. **Owner decisions.** (a) May quick-facts cells shrink when the text survives in the body (B5)? (b) Render
   thumbnail from data.wafer.space, or link only? (c) Is the materials `Key` column reader-facing? (d) "Starting
   material" sits under "What the machine class is and how it works" — accept, or allow a heading variant?
