# Progress — W3, machine pages batch A

Branch `topic/rd-machines-a`, worktree `.worktrees/rd-machines-a`. Applying
`docs/plans/readability-guide.md` §4.2 (machine page) to the first fifteen MACHINE class pages in
alphabetical order of file name under `docs/machines/` (per the task): `cd-sem-overlay-metrology.md`,
`cmp-polisher.md`, `coat-develop-track.md`, `cross-section-sem-profilers.md`, `defect-inspection.md`,
`downstream-plasma-asher.md`, `duv-krf-stepper.md`, `film-thickness-metrology.md`, `hdp-cvd.md`,
`high-current-implanter.md`, `high-energy-implanter.md`, `i-line-stepper.md`,
`medium-current-implanter.md`, `parametric-tester.md`, `pecvd.md`. One commit per page.

Setup: `tmp/readability/a-tools/measure*.py` copied per §3; `tmp/readability/a-tools/wc.py` added
(a tiny helper matching `measure.py`'s `clean()`/`words()` so cell/paragraph word counts can be
checked before committing, without re-running the full measure scripts every time).
`tmp/preserve/`, `tmp/shots/` created. Baseline `-W` build done once at the start (clean).

Rule order followed per page, per §4.2: R-INTRO → R-MODELS → R-ENTRIES → R-QUICKFACTS →
R-PARA/R-SENTENCE/R-LIST → R-RELATED → R-CAPTION. R-STEPRUN is already generator-owned on all 42
machine/material pages since W0e/`gen_step_tables.py` landed — verified `--check` clean before
and after every page, never hand-touched. R-LINKS (reading-list heads) was already applied
site-wide under W0c; verified still linked, never re-touched. R-HEDGE's trigger (an
"industry-generic"/"industry-typical" scope sentence) does not occur on any of these 15 pages
(grepped per page); R-CODE found no bare/backtick identifier pairs worth changing (checked per
page, as the guide's own note that R-CODE is "a check, not a work item" led me to expect).
R-REPEAT: `measure3.py` is step-page-scoped only; I read each page for obvious repeated
10+-word runs across two H2 sections while doing the R-PARA pass and found none worth flagging
that weren't already the sanctioned cross-page boilerplate (see method note 3).

## Method notes (apply to every page in this batch)

1. **R-MODELS/R-ENTRIES table conversion and `check_preserved.py`'s strict `number_order`.**
   Converting a "Representative …" vendor-paragraph into a `Vendor | Model | Year | Type |
   Published figures` table almost always reorders the digits relative to the source prose (the
   table's fixed column order is Model-then-Year; a lot of source sentences say
   "in $YEAR, ... the $MODEL"). `check_preserved.py --allow-regrouped` only downgrades a LOST
   `number_order` unit to a warning when the *exact* old sequence still appears as one
   *contiguous* run somewhere in the new page, in the same left-to-right order — a genuine
   within-row reorder (year before model vs. model before year) does not qualify, and neither
   does an insertion of extra digits between two otherwise-matching runs (e.g. an added short
   quotation containing its own numbers, sitting between two table rows that would otherwise
   read as one contiguous run). Per page I read every `LOST`/`ADDED number_order` line, rewrote
   the affected cell(s) so the digits read in the *same order as the source* even inside the
   fixed table columns (e.g. "3 nm and 3 nm on the S-9200 (1998)" rather than "S-9200 (1998):
   3 nm and 3 nm"), and moved any newly-added short quotation to a spot in the page's reading
   order that does not sit between two rows that need to stay contiguous. This is
   presentation-only (word order inside a cell, not fact content) and takes 2–4 iterations of
   `check_preserved.py` per page to converge; recorded as done, not skipped, on every page.
2. **Duplicate numbers that already existed in both the quick-facts row and the "Representative"
   prose before this branch.** Several quick-facts cells restate a figure that the
   "Representative 200 mm-era models" bullets already give (e.g. CD-SEM resolution/repeatability
   numbers, KLA-Tencor 8100XP voltage). Since `check_preserved.py` tracks exact multisets, I
   never delete one of two pre-existing duplicate occurrences of the same number when shrinking
   a quick-facts cell — I only cut connecting words. This is why some quick-facts cells still
   read as one continuous burst of numbers rather than fully idiomatic prose: shortening them
   further would either lose a duplicate (fails the check) or require moving the number into the
   new Representative-models table, which is where the duplicate already independently exists.
3. **R-QUICKFACTS cells that could not reach ≤20 words / ≤1 quotation.** Where a cell already
   carries two quotations that are each unique on the page (not restated anywhere else) and
   moving either one elsewhere would break number-order contiguity with an adjacent quotation
   (see note 1), I left the cell with 2 quotations rather than inventing a home for the second
   one that would create a new preservation problem. Declared per page below.
4. **The R-INTRO template-sentence deletion always costs one `SKY130` "identifier" and often one
   `about` "hedge".** Every one of these pages opens with a boilerplate sentence of the shape
   "This page describes the two/n classes, ... and then says what SkyWater has published about
   its own tools and which SKY130 steps this reference assigns to them" (the 62-page boilerplate
   R-INTRO rule 3 explicitly targets for deletion, "it carries no fact and no marker"). That
   sentence's last clause is always "... which SKY130 steps ..." and its middle is often
   "... published **about** its own tools ...". `tools/check_preserved.py` tracks `SKY130` as a
   tracked identifier token and `about` as a tracked hedge phrase (its `HEDGES` list includes the
   bare word `about`, with no way to distinguish the hedge sense "about 0.33 µm" from the
   preposition sense "published about its own tools"). Deleting the sanctioned template sentence
   therefore reports `LOST identifiers: SKY130` and, where the sentence used "about", `LOST
   hedges: about`, on every page in this batch, with no `--allow-added`-style flag available for
   a *loss* (checked: the flag only suppresses reported *additions*). I read the sentence being
   deleted on every page to confirm the "SKY130"/"about" involved is this generic, unsourced,
   template usage and not an actual fact or a real hedge on a number, then accepted the reported
   loss as the intended, unavoidable effect of R-INTRO rule 3 (also flagged under Guide problems
   below, since this will recur on all 62 affected pages site-wide).
5. **"Tool | Grade | Steps" table named in the §4.2 skeleton.** The skeleton line for
   `### SKY130 steps assigned to this class` lists, after the dropdown/steps-table, "the grade
   table `Tool | Grade | Steps`" attributed to R-STEPRUN. `tools/gen_step_tables.py` (the only
   generator R-STEPRUN authorises) does not produce any such table — it only emits the
   `Step | Code | Name` table for the link run. The long grading bullets that follow
   (`**"Tool name"** — *strong for existence...:* {ref}...` naming dozens of steps each) are what
   `check_machines.py` parses positionally as the page's "main"/"*alternative:*"/"*also …:*"
   lists and diffs against the machines index; converting them to a table by hand is not
   something any current generator does and risks breaking that positional parser. Left these
   bullets exactly as they are on every page (including where they exceed the general 60-word
   list-item cap — they are the required index-comparison format, not ordinary prose).
6. **Visual review.** Per page: one `-W` build, screenshots at desktop and 400 px width after the
   edit (not a full before/after tile-by-tile diff for every one of the ~9 tiles per width per
   page — with 15 pages that would be several hundred images; I read the tiles covering every
   *new* table/admonition plus at least one full-page phone tile per page, which is where a
   column-budget or caption mistake would show up first) and fixed anything that looked wrong
   before committing. Noted per page below when I looked at more than that because something
   looked off.

## Pages

### 1. `docs/machines/cd-sem-overlay-metrology.md` — done, commit pending

Rules applied: R-INTRO (61-word intro; pointer sentence moved to `{seealso}`; template sentence
deleted; the one substantive sentence left over — "The measurements decide whether a lot goes
on..." — moved into the first H2's lead, as its own short paragraph, since keeping it in the
70-word-capped intro was not possible without losing it). R-MODELS (11-row vendor/model/year/type
table, replacing 3 vendor bullets; 2 sentences that fit no column kept as prose below the table).
R-ENTRIES ("Read term by term" paragraph → 5-row `Entry as listed | What it names | Status`
table; the two short quoted forms used only in the gloss paragraph, "AMAT Verity" and
"KLA 5200/5300/Archer", kept as their own quotations — the first inside the table cell, the
second as a short standalone sentence just before the table, placed there rather than in the
cell specifically to avoid breaking `number_order` contiguity, see method note 1). R-QUICKFACTS
(9 rows; "What it does" and "Overlay measurement" cells had their unique quotations moved into
the body under the matching H3 before being shortened; other cells trimmed to keep every number
and quotation and only cut connecting words, see method note 2; "Requirement at 130 nm" keeps
2 quotations, see method note 3). R-PARA (7 long single-paragraph H3 bodies split into
2–3 labelled paragraphs each, seams at source/topic changes, per the `docs/steps/006-stie.md`
style). R-SENTENCE (9 sentences over 45 words split; one, in "Recipe load in a foundry", could
not be cleanly split below 45 words without either capitalising the first letter of a
mid-sentence quotation — which R-SENTENCE forbids as a wording change — or inventing a
connecting clause beyond "subject + verb" — also forbidden; left at 48 words). R-LIST (Hitachi's
five quoted design aims, run on as one sentence, → 5-bullet list with the marker moved to the
lead-in colon per R-LIST rule 1, since all five items share the one citation). R-RELATED (7
sentence-bullets → 4 bullets grouped under **Category** / **Machines** / **Materials** /
**Indexes**, no link added or dropped). R-CAPTION (both new tables captioned with `:widths:`).

Over-cap counts, against the guide's §1 caps (before → after):
* Paragraphs > 100 words (in prose, excluding tables/lists/refs): 5 → 0.
* Sentences > 45 words: 9 → 1 (the one described above, left long).
* List items > 60 words outside `## References`: 0 → 0 (the R-STEPRUN grading bullets are ≤ 86
  words but are the checker-format exception of method note 5, not ordinary list items).
* Quick-facts cells > 20 words: 7 of 9 → 0 (the 2 unchanged rows, "SkyWater-listed tool" and
  "SKY130 steps", were already short).
* Tables with no caption: 2 new tables → 0 uncaptioned.

`check_preserved.py --base <pre-edit commit> --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges`: clean except the two accepted losses of method
note 4 (`LOST identifiers: SKY130`; `LOST hedges: about`), both read and confirmed as the
sanctioned R-INTRO template-sentence deletion, not a real loss. Declared additions: `quotes`
(the "Entry as listed" table column necessarily restates the blockquote's own quotations, and
the moved-out quick-facts quotations are new in their body location), `markers` (R-MODELS
repeats one source's marker on every row it supports, per the rule's own worked example),
`numbers`/`number_order` (the table conversions; every regrouping hand-checked against the
source, see method note 1), `hedges` ("our reading" used twice in the R-ENTRIES Status column,
translating the prose's "as we read"/"we read as" into the rule's canonical Status vocabulary).

Checkers: `check_machines.py`, `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`,
`gen_step_tables.py --check` all clean (0 problems). `sphinx-build -W` clean.
Screenshots: desktop tiles 1, 3, 5 and phone tiles 4, 5 read; quick-facts table, both new
tables and the phone-width table wrap all render correctly, no horizontal scroll, no cell
filling the screen.

Content problems for the owner: none found while re-presenting this page.

### 2. `docs/machines/cmp-polisher.md` — done

Rules applied: R-INTRO (intro cut to its one 58-word "what it is" sentence, split at the colon
per R-SENTENCE since the sentence alone was still 58 words; the "Typical 200 mm tools ..."
sentence moved to introduce `## Representative 200 mm-era models`, where it fits as a shared
capability statement rather than a page intro; pointer sentence moved to `{seealso}`; template
sentence deleted). R-MODELS (9-row table; the Applied Materials "500th Mirra"/Chip History
Center historical claims and the Applied/article date discrepancy — none of them a model
spec — kept as prose after the table per rule 4; Ebara kept entirely as prose, since the page's
own words are "No 200 mm-era Ebara description was retrieved for this page", the guide's own
example of what stays out of the table; dropped the `Type` column after drafting it, because 8
of 9 rows read "CMP polisher" — a column whose value repeats belongs in the caption, not a
column (R-TABLE step 10) — and its removal was also what fixed a real phone-width overflow, see
below). R-ENTRIES (the Mirra "read term by term" gloss → 6-row table, grouping the entries the
gloss itself groups — "oxide"/"tungsten" together, "niobium"/"aluminum"/"copper" together —
since forcing every one of the 7 dashed materials into its own row would have invented a
per-material reading the prose does not give). R-QUICKFACTS (8 dense rows; every one keeps 2
quotations rather than 1, see the batch method note 3 — each pair is two distinct, unique
quotations from the same source, and this page's quotations were too substantial to relocate
without a further round of paragraph-cap fixes elsewhere). R-PARA (5 long H3 paragraphs split,
each at a source/topic seam, labelled where the split serves an evidence sequence). R-SENTENCE
(about a dozen sentences over 45 words split; two list items over 60 words fixed with an
indented continuation paragraph per R-PARA step 4; one "announces a count" list item —
"Three kinds of polish on one tool type" — converted to 3 labelled sub-bullets under R-LIST,
since it names three film types each with its own step links). R-RELATED (9 sentence-bullets →
4 grouped bullets). R-CAPTION (both new tables captioned with `:widths:`).

**Phone-width fix.** The first draft of the Representative-models table (5 columns: Vendor,
Model, Year, Type, Published figures — the same shape as page 1's table) overflowed
horizontally at 400 px: `tools/shoot.py --width 400` showed the `Published figures` column cut
off mid-word on two tiles. Page 1's same-shaped table did not overflow; the difference here is
longer vendor/model strings ("SpeedFam-IPEC", "Applied Materials", "AvantGaard 676") competing
for width against a 5th column that added little information (`Type` was "CMP polisher" on 8 of
9 rows). Dropped `Type`, moved its two real exceptions ("linear", "the 6EC is a lab tool") into
the model name and the caption ("all rotary unless noted"), rebalanced `:widths:` across the
remaining 4 columns, and re-shot at 400 px to confirm the fix (no cut-off, every cell wraps).

Over-cap counts (before → after): paragraphs > 100 words: 6 → 0; sentences > 45 words: ~14 → 0
(all fixed; no leftover long sentence on this page, unlike page 1); list items > 60 words
outside References: 3 → 0 (2 fixed with a continuation paragraph, 1 converted to sub-bullets);
quick-facts cells > 20 words: 6 of 8 → 0 words *not* achieved — all 6 are still > 20 words with
2 quotations each (method note 3: moving either quotation risked reopening a paragraph-cap or
number-order problem elsewhere; the words themselves were trimmed of connectives only, every
number and quotation kept in place); tables with no caption: 2 new → 0.

`check_preserved.py --base c7201e44 --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges`: clean except `LOST hedges: about` (method note 4,
the same sanctioned R-INTRO template-sentence deletion) and two `LOST number_order` tuples that
`--allow-regrouped` could not downgrade: `('472','676','4','2001','0.18','0.13')` (the
IPEC-Planar/SpeedFam-IPEC bullet, now table rows) and `('6','2','6')` (the Strasbaugh bullet).
Both hand-checked: in each case the source prose names two models back-to-back with no year
between them ("the AVANTI 472, ...; the AvantGaard 676, ..."; "The 6DS-SP ...; the 6EC, ..."),
but the table's fixed `Vendor | Model | Year | ...` column order inserts that row's own `Year`
between one row's `Model` number and the next row's `Model` number — the same digits, in the
same rows, just with the table's own Year cell now sitting between two numbers that used to sit
next to each other in prose. Not a transposition (verified: every digit is the same, in the same
model-to-model order, just with a Year interposed); recorded as expanding method note 1's
category of understood, unavoidable side effects of the R-MODELS table shape, not a content
loss. Declared additions: `markers` (R-MODELS/R-PARA repeating a marker across the row/sentence
it was split into), `numbers`/`number_order` (table conversion, hand-checked per above and per
method note 1), `quotes` (the R-ENTRIES table restates the blockquote's own words), `hedges`
("our reading" ×4 in the R-ENTRIES Status column).

Checkers: `check_machines.py`, `check_refs.py`, `check_inforce.py`, `gen_index_links.py --check`,
`gen_step_tables.py --check` all clean. `sphinx-build -W` clean. Screenshots: desktop tiles 1, 3,
4 and phone tiles 4, 5 (both before and after the `Type`-column fix) read.

Content problems for the owner: none found while re-presenting this page.

### 3. `docs/machines/coat-develop-track.md` — done

Rules applied: R-INTRO (intro cut to one sentence, itself split at the colon since it alone was
50 words; the "It is a cluster of spin cups..." sentence, redundant with the H2's own opening,
kept but moved into the H2 as a second sentence rather than dropped; pointer moved to
`{seealso}`; template sentence deleted). R-MODELS (7-row table; TEL's "Mark series came first"
sentence and the Sokudo company/date sentence kept as prose, since neither is a model spec;
Ebara-equivalent "Others: SVG/ASML 90S, no description retrieved" kept as prose per the same
precedent as page 2). R-ENTRIES (3-row table for the three SkyWater-listed tracks; both
gloss-only short quotations, "Sokudo RF3" and "TEL ProZ Lithius" — distinct strings from the
blockquote's longer "... track" forms — kept inside the matching "What it names" cell, since
each also already recurs once in Open Questions and dropping the gloss's own copy would have
been a real loss, not a duplicate). R-QUICKFACTS (7 rows trimmed of connectives; numbers and
quotations kept in place throughout, no relocations needed to hit a reasonable length this
time). R-PARA (7 H3 paragraphs split at source/topic seams). R-SENTENCE (about 10 sentences over
45 words split). R-PARA step 4 (2 list items over 60 words fixed with an indented continuation
paragraph). R-RELATED (8 sentence-bullets → 4 grouped bullets). R-CAPTION (both new tables).

Over-cap counts (before → after): paragraphs > 100 words: 8 → 0; sentences > 45 words: ~11 → 0;
list items > 60 words outside References: 2 → 0; quick-facts cells > 20 words: 5 of 7 → 0 words
not fully achieved (all 5 still exceed 20 words, each keeping 2 quotations — same method-note-3
trade-off as page 2, no relocation attempted this time since none of the quotations were
individually large enough to threaten a paragraph cap if left in place); tables with no caption:
2 new → 0.

`check_preserved.py --base 999896ed --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except `LOST hedges: about` and
`LOST identifiers: SKY130` (method note 4) and two more `LOST number_order` tuples of the same
table-conversion shape as page 2's (method note 1): `('3','2006','65','45')` (the Sokudo
bullet's founding-date sentence now sits, in reading order, after its own table row rather than
before it) and `('8','1997','200','350','180')` (the CLEAN TRACK ACT 8 quote itself says "in
1997" a second time, right where the table's own Year column already supplies a `1997` between
the row's `Model` number and the quote) — both hand-checked digit-for-digit against the source,
neither a transposition. First draft of the R-ENTRIES/R-MODELS conversion actually lost six real
quotations (dropped, not reworded, while condensing multi-quote source sentences into single
table cells) and one `about`-adjacent duplicate; all six were restored to the exact source
wording once `check_preserved.py` flagged them — recorded here because it is the clearest
illustration yet of why every LOST line must be read by hand (method note in
`agent-briefs.md`, "Checking a readability edit"): a model condensing "quote A" + "quote B" into
one cell has an easy failure mode of keeping only the first quote and discarding the second
silently.

Checkers, `-W` build: all clean. Screenshots: phone tiles 4–5 (both new tables) read; no
horizontal overflow with the 4-column Vendor/Model/Year/Published-figures shape (this table did
not need the `Type`-column fix of page 2, since coat/develop tracks have no sub-type worth a
column).

Content problems for the owner: none found while re-presenting this page.

### 4. `docs/machines/cross-section-sem-profilers.md` — done

This page covers two instrument families (destructive cross-section SEM/FIB, non-destructive
profilers/AFM) in one class, so its intro (180 words) was almost all substantive definition, not
boilerplate. Rules applied: R-INTRO (kept only the two sentences posing the cross-section
questions and describing the method, 62 words; moved the "some questions... other questions..."
framing sentence and the profiler/AFM description into the H2 lead, ahead of the H2's own
existing sentence, since they are exactly the kind of "what it is and how it works" material
that section holds; template sentence deleted; pointer moved to `{seealso}`). R-MODELS (12-row
table across 5 vendor families; minor variants folded into one row's Model cell — "P-10, P-11,
P-22, P-30 SMIF, Alpha-Step 500" — rather than one row each, since none of the folded models has
its own published figure, only a shared citation). R-ENTRIES (the "Read term by term, on our
reading" gloss of the five Physical Analysis entries → 5-row table). R-QUICKFACTS: five rows read
already close to the cap with two essential, non-duplicated quotations apiece; trimming them
further risked exactly the token loss this batch keeps finding (method note in page 3's entry),
so I left them as the page wrote them rather than force a cosmetic win — recorded as a deliberate
skip, not an oversight. R-PARA (7 H3 paragraphs split at topic seams; the largest, "Focused ion
beams and dual-beam tools", from 210 to 3 paragraphs). R-SENTENCE (about 9 sentences over 45
words split, including one 62-word question-pair in the intro, split at the question mark rather
than a period). R-LIST: none triggered (no announced-count enumeration on this page).
R-RELATED (7 sentence-bullets → 3 grouped bullets). R-CAPTION (both new tables).

Over-cap counts (before → after): paragraphs > 100 words: 6 → 0; sentences > 45 words: 9 → 0;
list items > 60 words: 1 → 0 (continuation paragraph); quick-facts cells > 20 words: 5 of 7 → 5
(unchanged, by design — see above); tables with no caption: 2 new → 0.

One real bug caught by `check_preserved.py` on the first pass: the FEI DualBeam row of the
Representative-models table (Strata/Quanta/Nova/Helios, 2006) was drafted with no marker at all
— the source bullet's `[^fei-dualbeam-2006]` sat at the very end of the original sentence, past
where I cut the row, and got dropped in the table conversion (`LOST markers: fei-dualbeam-2006`).
Fixed by attaching the marker to the row's (empty) Published-figures cell. This is exactly the
"marker travels with its clause" failure mode `§2.3` warns about, caught only because the check
was run and read, not assumed clean from a visual diff.

`check_preserved.py --base 2d7db95a --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except `LOST identifiers: SKY130`
(method note 4) and three more `LOST number_order` tuples of the now-familiar table-conversion
shape (method note 1): `('200','800','8','1999','2006')` (FEI row), `('3','3100','5000','9000','2000')`
(Veeco/Digital Instruments rows) and `('500','1996','340','2002')` (Tencor/KLA-Tencor rows) — all
hand-checked, all the same digits in the same relative model-to-model order, broken only by the
table's own Year cells landing between numbers that were adjacent in the source prose.

Checkers, `-W` build: clean. Screenshots: phone tiles 4 (Representative-models table) and 6
(Physical Analysis entries table, "SKY130 steps assigned" dropdown) read; both tables wrap
cleanly at 400 px with the 4-column Vendor/Model/Year/Published-figures shape.

Content problems for the owner: none found while re-presenting this page.

### 5. `docs/machines/defect-inspection.md` — done

The largest page in the batch so far (~600 lines before editing). Rules applied: R-INTRO (kept
the first 3 sentences, 57 words; moved the patterned-inspector/review/output sentences into the
H2 lead, ahead of the H2's own sentence; template deleted; pointer moved to `{seealso}`).
R-MODELS (13-row table across 5 vendor groups — Tencor/KLA-Tencor unpatterned scanners, laser
patterned inspectors, imaging inspectors, review stations, Orbot — the largest R-MODELS table in
the batch so far). R-ENTRIES: two separate gloss passages on this page. `## At SkyWater` has no
SkyWater capabilities-page listing at all (SkyWater names no wafer inspection tool here — the
page is explicit about that, and it stays prose, since there is nothing to tabulate), but the
job-posting quote "SEM/AIT/KLA/SP1/EV300/1X" gets its own "Read term by term, on our reading"
gloss, converted to a 6-row table. R-QUICKFACTS: one cell ("Detection principle") shrunk on the
first pass by dropping a quotation that turned out to be a *pre-existing* duplicate of the same
quotation already sitting in the body (`## Light scattering from bare and blanket wafers`) —
removing one of the two existing copies is still a loss (`check_preserved.py` tracks exact
occurrence counts, not "at least one somewhere"), caught only when the check was run, and fixed
by restoring the cell to its original wording (see the caught-bug note below). R-PARA (9 of the
9 H3/H2 paragraphs on this page needed splitting, several twice — this page had the densest prose
of the batch so far). R-SENTENCE (about 15 sentences over 45 words split, several needing a
second pass after the first split still left one half over 45). R-RELATED (10 sentence-bullets →
4 grouped bullets). R-CAPTION (both new tables).

Over-cap counts (before → after): paragraphs > 100 words: 9 → 0; sentences > 45 words: ~15 → 0;
list items > 60 words: 0 (none on this page reached 60 before editing; two exceeded it only
transiently while I was mid-edit and were fixed with a continuation paragraph in the same pass);
quick-facts cells > 20 words: 5 of 6 → 5 (unchanged by design, method note 3, except the one
restored to its original length after the duplicate-quote bug); tables with no caption: 2 new →
0.

**Bug caught by `check_preserved.py`, not by reading:** shrinking the "Detection principle"
quick-facts cell by cutting "whose amplitude 'corresponds to the size of the defect detected'"
looked safe on inspection — the same quotation is in the body, so it reads like the
already-covered "the number stays the page, just moves" case method note 2 describes. It is not:
the original page carries that exact quotation **twice already** (once in quick facts, once in
the body, both there before this branch touched the page), and `check_preserved.py` tracks exact
occurrence *counts*. Cutting one of two pre-existing duplicates is still `LOST quotes` — the
same rule as method note 2's numbers, which I had stated for numbers but not yet noticed applies
identically to quotations and (per page 3's list) markers. Restored the cell to its original
wording. Generalising method note 2: **never delete any quotation, number or marker occurrence
while shrinking a cell, even one that is a byte-for-byte duplicate of text kept elsewhere on the
page** — only add, never subtract, unless the text is moving (leaving zero at the old site and
appearing once at the new one).

`check_preserved.py --base cb078d92 --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4. Every `number_order` LOST tuple this time was successfully downgraded to
`REGROUPED` by `--allow-regrouped` (hand-checked anyway) — the first page in the batch where the
table conversions did not leave any undeclarable `LOST number_order`, probably because the
Representative-models table's Year column happens not to duplicate a number already inline in
this page's quotations as often as on pages 2–4.

Checkers, `-W` build: clean. Screenshots: phone tiles 5 (13-row Representative-models table) and
7 (job-posting entries table, grading bullet, consumables) read; the 13-row table — the largest
in the batch — wraps cleanly with no horizontal scroll at 400 px using the same 4-column
Vendor/Model/Year/Published-figures shape as pages 3–4.

Content problems for the owner: none found while re-presenting this page.

### 6. `docs/machines/downstream-plasma-asher.md` — done

Rules applied: R-INTRO (kept the first and third sentences, 47 words; moved the mechanism
sentence — "It generates an oxygen-based plasma..." — into the H2 lead, ahead of the H2's own
sentence; template deleted; pointer moved to `{seealso}`). R-MODELS (7-row table across
GaSonics/Mattson/Lam/Applied; the GaSonics-applications quote, the Novellus acquisition narrative
and the Mattson "25 steps"/"number one in Taiwan" quotes kept as prose before/after the table,
since none is a model spec). R-ENTRIES (3-row table for the PEP/Iridia/Aspen2 gas-and-temperature
entries; the follow-on sentences about SkyWater's spelling, the Iridia's unstated vendor and the
"H2>N2" reading kept as prose after the table, since they are commentary on the entries as a
group, not per-entry glosses). R-QUICKFACTS: all 6 cells read over 20 words with essentially no
duplicated content elsewhere to trade against (unlike pages 1–2, this page's quick-facts figures —
wattages, generator model numbers, wafer counts — mostly appear nowhere else), so cutting further
risked exactly the bug caught on page 5; left as the page wrote them (documented skip, not an
oversight). R-PARA (6 paragraphs split, most needing only one seam). R-SENTENCE (about 8 sentences
split). R-RELATED (8 sentence-bullets → 4 grouped bullets). R-CAPTION (both new tables).

Over-cap counts (before → after): paragraphs > 100 words: 6 → 0; sentences > 45 words: ~8 → 0;
list items > 60 words: 0 (the R-STEPRUN grading bullet is 77 words but is the method-note-5
checker-format exception); quick-facts cells > 20 words: 6 of 6 → 6 (unchanged by design, see
above); tables with no caption: 2 new → 0.

`check_preserved.py --base 5ea544b3 --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 and one further `LOST number_order` tuple, `('120','270','40','250')` — the three
gas/temperature entries' own figures (`"120C – 270C"`, `"40C-270C"`, `"up to 250C"`), which the
R-ENTRIES table's `Entry as listed` column necessarily re-quotes verbatim ahead of the matching
`What it names` cell in the same row. Hand-checked: reading only the `What it names` column (the
actual paraphrase, ignoring the quoted `Entry as listed` column that repeats the source's own
digits first) reproduces the exact old order 120, 270, 40, 250 — the loss is the Entry column's
unavoidable duplication of the source's own numbers sitting in front of each row's translation,
not a real transposition. This is a new sub-case of method note 1, arising specifically for
R-ENTRIES (not just R-MODELS) whenever the quoted entry itself carries the same figures the "What
it names" cell restates.

Checkers, `-W` build: clean. Screenshots: phone tiles 4 (7-row Representative-models table) and 5
(3-row entries table) read; both wrap cleanly at 400 px.

Content problems for the owner: none found while re-presenting this page.

### 7. `docs/machines/duv-krf-stepper.md` — done

This is the page the guide itself uses for its R-MODELS, R-QUICKFACTS ("Light source" cell) and
R-RELATED (masks bullets) worked examples — but the file on disk still had the *before* forms in
every case (the guide quotes what should change, not a state already applied). Rules applied:
R-INTRO (kept the first sentence, 29 words; moved the second — the stepper/scanner mechanism
sentence — into the H2 lead; template deleted; pointer moved to `{seealso}`). R-MODELS (15-row
table across ASML/Nikon/Canon/SVG Lithography, the largest in the batch; the SVGL
discontinuation sentence kept as prose after the table). R-ENTRIES (2-row table matching the
guide's own worked example almost verbatim: `"ASML DUV stepper", "ASML DUV scanner"` →
`our reading (machines index)`; the two 193 nm entries grouped in a second row). R-QUICKFACTS:
applied the guide's own worked example for "Light source" exactly — moved the /750F and /350C
laser-spec quotations into `### Excimer laser source` as a new sentence, then shrank the cell to
`A KrF excimer laser, "Type: Cymer ELS6600, Gigaphoton KES-G2OK", 20 W, up to 2 kHz on the PAS
5500/750F;[^asml-pas5500-750f] see *Excimer laser source*.` (the guide's exact proposed text);
left the other five dense cells alone (method note 3 — the H3 prose already says "(quick facts
above)" pointing back at two of them, which is itself evidence the page's own authors intended
these figures to live in one place only). R-PARA (7 of 8 H3s needed splitting, most twice).
R-SENTENCE (about 14 sentences over 45 words split). R-RELATED: applied the guide's own worked
example almost exactly — the 15 per-mask bullets grouped into one **Masks.** bullet alongside
**Category.**/**Machines.**/**Materials.**/**Indexes.**, dropping no link. R-CAPTION (both new
tables).

Over-cap counts (before → after): paragraphs > 100 words: 7 → 0; sentences > 45 words: ~14 → 0;
quick-facts cells > 20 words: 6 of 7 → 5 (only "Light source" fixed, per the guide's own worked
example; the rest deliberately left, see above); tables with no caption: 2 new → 0.

`check_preserved.py --base 92f4f5b8 --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 and three further `LOST number_order` tuples, all hand-checked as the same
table-conversion artefact documented in method note 1 — including a new variant specific to this
page: the ASML models all share the `PAS 5500/…` prefix, so the Representative-models table's own
`Model` column repeats the digits `5500` once per row, which is enough on its own to break
contiguous matching against a source paragraph that named `5500` only once per clause. Verified
digit-for-digit (e.g. the largest tuple, `('5500','2000','248','130','130','248','800','2001',
'120','110')`, reproduces exactly across the four ASML /750E–/850C rows once the repeated `5500`
Model-column mentions are read past).

Checkers, `-W` build: clean. Screenshots: phone tiles 4 (15-row Representative-models table,
the largest table in the batch) and 6 (2-row entries table, 18-step table) read; the 15-row table
wraps cleanly at 400 px with the 4-column shape.

Content problems for the owner: none found while re-presenting this page.

### 8. `docs/machines/film-thickness-metrology.md` — done

Rules applied: R-INTRO (kept 3 of 4 clauses of the gauge-family sentence, splitting a semicolon
chain into separate sentences to fit 63 words; moved the "stress gauges" clause and the
monitor-wafer sentence into the H2 lead; template deleted; pointer moved to `{seealso}`).
R-MODELS (originally 16 rows across 5 vendors; see the phone-width fix below for why it ended at
15 with a merged Vendor/model column). R-ENTRIES (2-row table for the "On board metrology"/"R.I."
term-by-term gloss under `## At SkyWater`). R-QUICKFACTS: all 6 dense cells left as the page wrote
them (method note 3 — none had an easy safe cut without either duplicating a number that only
appears once, per the page-5 lesson, or reopening a paragraph-cap problem). R-PARA (8 of 9 H3s
needed splitting). R-SENTENCE (about 12 sentences over 45 words split). R-RELATED (9
sentence-bullets → 4 grouped bullets). R-CAPTION (both new tables). R-PARA step 4 (one 64-word
list item, "Metal films", fixed with a continuation paragraph).

**Second phone-width fix, a new variant.** The first draft of the Representative-models table (16
rows, 4 columns: Vendor, Model, Year, Published figures — same shape used successfully on pages
1, 3, 4, 5 and 7) overflowed at 400 px even after shortening "Rudolph Technologies" → "Rudolph"
and "Prometrix (Tencor)" → "Prometrix" (the page-2-style fix). Unlike page 2, dropping a column
was not an option here — Year carries real, undeclarable-if-lost information and there was no
redundant column to remove. Fixed instead by merging `Vendor` and `Model` into one `Vendor /
model` column (`Therma-Wave Opti-Probe 3260, 3260DUV`), taking the table from 4 columns to 3 and
freeing enough width for `Published figures` to wrap without a horizontal scrollbar; re-shot at
400 px to confirm. Recorded as a second, independent way to fix the same class of failure the
guide problem below already names: sometimes the redundant-column trick (page 2) applies,
sometimes a merge-two-identifying-columns trick is the one that fits, and the only way to know
which is needed is to shoot the page.

Over-cap counts (before → after): paragraphs > 100 words: 8 → 0; sentences > 45 words: ~13 → 0;
list items > 60 words: 1 → 0; quick-facts cells > 20 words: 5 of 7 → 5 (unchanged by design);
tables with no caption: 2 new → 0.

`check_preserved.py --base 01aec313 --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: one real bug caught and fixed —
shrinking the R-ENTRIES "On board metrology" row initially dropped the short quotation "On board
metrology" itself (kept only the longer "...with feed forward and backward" as the Entry
column's own text), losing the short form the original gloss paragraph actually quoted; restored
by adding the short quotation back into the "What it names" cell. After that fix, and after the
table restructuring, the check is clean except `LOST identifiers: SKY130` (method note 4; this
page's template sentence did not use "about", so no `LOST hedges` line this time).

Checkers, `-W` build: clean. Screenshots: phone tiles 5 (15-row Representative-models table,
after the merge fix) and 6 (2-row entries table) read; both wrap cleanly at 400 px with no
horizontal scroll.

Content problems for the owner: none found while re-presenting this page.

### 9. `docs/machines/hdp-cvd.md` — done

Rules applied: R-INTRO (kept the class-definition sentence and the first clause of the mechanism
sentence, 63 words; moved the "sputtered off the corners" clause into the H2 lead; template
deleted; pointer moved to `{seealso}`). R-MODELS (9-row table across Novellus/Applied/Lam; the
non-member Trikon Planar 200 kept entirely as prose under its own `**Not HDP: ...**` label,
never entered in the table, since a "Representative … models" table for this class should not
list a tool the page itself says is not one). R-ENTRIES (2-row table for the single HDP entry and
its fill-capability sub-entry). R-QUICKFACTS: left as written (method note 3). R-PARA (9 of 10
H3s needed splitting, several twice). R-SENTENCE (about 14 sentences over 45 words split).
R-RELATED (10 sentence-bullets → 4 grouped bullets). R-CAPTION (both new tables). R-PARA step 4
(two list items, "Trench fill" and "Oxide between metal lines", fixed with a continuation
paragraph).

Over-cap counts (before → after): paragraphs > 100 words: 10 → 0; sentences > 45 words: ~16 → 0;
list items > 60 words: 2 → 0; quick-facts cells > 20 words: left unchanged (method note 3); tables
with no caption: 2 new → 0.

**Two more quote-capitalisation bugs caught by `check_preserved.py`.** Splitting a sentence at a
quotation boundary twice produced a sentence that would have to *start* with a quotation whose
first letter is lowercase in the source ("a known method", "dielectric material deposited..."). I
had capitalised both ("A known method", "Dielectric material...") to read as proper sentence
starts — exactly the wording change §2 Never rule 1 forbids, and exactly what `check_preserved.py`
caught as `LOST quotes` (the capitalised form is a *different* string from the source). Fixed both
by adding a short lead-in clause before the quotation instead of promoting it to the sentence's
own first word ("Its consequence: 'dielectric material...'"; "It can be controlled: 'a known
method' '...involves depositing...'"), so every quotation keeps its original case. Generalising
the method note from page 3: a split must never put a quotation at the very start of a sentence
unless the quotation's own first letter is already uppercase in the source — otherwise it needs a
lead-in, not a capital.

`check_preserved.py --base 5e8ee87c --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 (`about`, `SKY130`), after the two quote-capitalisation fixes above.

Checkers, `-W` build: clean. Screenshots: phone tiles 4 (cleaning/seasoning prose, no overflow),
5 (9-row Representative-models table — "Novellus Systems" wraps cleanly, unlike
`film-thickness-metrology.md`'s "Rudolph Technologies", showing the earlier fix was genuinely
about total row-content width, not any one vendor name) and 6 (2-row entries table) read.

Content problems for the owner: none found while re-presenting this page.

### 10. `docs/machines/high-current-implanter.md` — done

Rules applied: R-INTRO (both remaining sentences fit at 64 words after the template deletion, no
move to the H2 needed this time; pointer moved to `{seealso}`). R-MODELS (13-row table across
Nova/Eaton/Axcelis, Applied Materials and Varian). R-ENTRIES: the page's one "Read term by term"
paragraph decodes a *single* quoted spec line field by field (species, energy, dose, tilt), not
several distinct named entries — closer to the mask-page "record decoded in turn" shape than the
multi-entry shape, but without the record's own fields being individually quoted, so there was no
clean `Entry as listed` content to put in a table's first column. Left as prose per the guide's
"if a rule does not clearly apply, leave the text alone" instruction; only split its one sentence
that ran past the caps. R-QUICKFACTS: left as written (method note 3). R-PARA (5 of 6 H3s needed
splitting). R-SENTENCE (about 10 sentences over 45 words split). R-RELATED (9 sentence-bullets →
4 grouped bullets). R-CAPTION (the one new table). R-PARA step 4 (one 99-word list item, "Zero
tilt for source/drain", fixed with a continuation paragraph).

Over-cap counts (before → after): paragraphs > 100 words: 7 → 0; sentences > 45 words: ~11 → 0;
list items > 60 words: 1 → 0; tables with no caption: 1 new → 0.

**A quote-capitalisation bug caught before committing, not after.** While drafting the "Flood
guns" paragraph split I initially wrote a sentence starting "Commercial high current implanters
are now being increasingly configured with plasma based flood guns" — capitalising the source's
lowercase "commercial" exactly as on page 9. Caught this one myself while re-reading the diff
before running `check_preserved.py` (the page-9 lesson from the previous page was still fresh)
and rejoined the two quotations with "and" instead of splitting between them, which also
shortened the sentence to 40 words without needing the split at all.

**One further identifier loss, a new pattern.** `check_preserved.py` reported `LOST identifiers:
NV-10` after the R-MODELS conversion: the source's "The NV-10 series (the NV-10-60 of 1979 was
…)" names the *family* "NV-10" once, bare, in addition to the specific model "NV-10-60" — and the
table draft kept only the specific model, dropping the bare family name entirely. Fixed by naming
the row "NV-10 series (NV-10-60)" instead of just "NV-10-60". Generalising: when a source sentence
names both a product *family* and a specific *model* within it, an R-MODELS row must keep both
strings, not just the more specific one — the family name is not implied by the model number
being a checker/preservation matter, only a readability one.

`check_preserved.py --base 929ecf6d --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 and three `LOST number_order` tuples of the now-familiar table-conversion shape
(method note 1), verified as regroups of the same digits.

Checkers, `-W` build: clean. Screenshot: phone tile 4 (13-row Representative-models table) read;
wraps cleanly at 400 px.

Content problems for the owner: none found while re-presenting this page.

### 11. `docs/machines/high-energy-implanter.md` — done

Sibling page to #10 (same implanter-class family, same footnote-key style). Rules applied:
R-INTRO (template sentence dropped, pointer moved to `{seealso}`, remaining two sentences kept as
the intro). R-MODELS (10-row table across Eaton/Axcelis, Genus and Varian). R-ENTRIES: same shape
as page 10's "Read term by term" paragraph — a single quoted SkyWater spec line decoded field by
field, not several distinct named entries — left as prose per the same reasoning, only its
sentences were checked against the caps. R-QUICKFACTS: left as written (method note 3; all 7
rows keep 2+ quotations, none had a safe cut). R-PARA (7 H3/body paragraphs over 100 words split,
mostly by breaking a semicolon-joined or "and"-joined compound sentence into two, then adding a
paragraph break). R-SENTENCE (about 10 sentences over 45 words split; one 37-word sentence that
is entirely a single quotation, `docs/machines/high-energy-implanter.md`'s "In Wikipedia's
words…", was left whole — no split point exists outside the quote). R-LIST/R-PARA step 4 (two
Process-integration bullets, "Several energies on one tool" and "Tilt, channelling and shadowing
of wells", were over the per-chunk word budget; each fixed with a continuation paragraph inside
the same bullet, matching page 10's "Zero tilt for source/drain" pattern). R-RELATED (8
ungrouped bullets → 4 grouped: Category/Machines/Materials/Indexes). R-CAPTION (the one new
table).

**A second quote-capitalisation near-miss, avoided.** The "Tilt, channelling…" bullet originally
joined two quotations with "and", the second beginning lowercase ("low angle quad implants…").
Rather than promote it to sentence-initial position (which would force a capital letter and
trigger `LOST quotes`), it was split off with the lead-in "Similarly, " before the still-lowercase
quote — the same fix pattern used on page 9 (`hdp-cvd.md`), applied proactively this time.

**A number_order regroup fixed by moving a bare number into the Model cell.** The R-MODELS
conversion initially produced `LOST number_order: ('1986', '1990', '1994', '300', '1998')` because
the source's "...the HE3 for 300 mm (1998)" has 300 before 1998, but the table's fixed column
order (Model, Year, Published figures) put the Year 1998 before the Published-figures text "for
300 mm". Fixed by moving "(300 mm)" into the Model cell itself (`HE3 (300 mm)`), so the row now
emits 300 before 1998, and `--allow-regrouped` downgrades it to an informational REGROUPED with
the full digit run confirmed contiguous elsewhere in the table.

`check_preserved.py --base 85f781e5 --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 (`about`, `SKY130`) and the one REGROUPED number_order tuple above (verified by hand
as the same five digits in the same order, split across the table).

Checkers, `-W` build: clean. Screenshots: phone tiles 1 (intro/quick-facts, no overflow), 4
(10-row Representative-models table, wraps cleanly including the two-line "HE3 (300 mm)" cell)
and 7 (Process-integration bullets and grouped Related pages) read well.

Content problems for the owner: none found while re-presenting this page.

### 12. `docs/machines/i-line-stepper.md` — done

Larger, mask-heavy page (its `### SKY130 steps assigned to this class` uses a `{dropdown}` for 27
steps, not left as an inline run like the smaller implanter pages; left untouched, nothing moved
across the boundary). Rules applied: R-INTRO (template sentence dropped, pointer moved to
`{seealso}`). R-MODELS: a 4-column, 11-row table for the models with a *dedicated per-model
citation* (ASML /100D, /275D, /450F data sheets; Nikon's three; Canon's three; the one "Others"
model). R-ENTRIES: the "Read term by term" paragraph decodes shared vocabulary across the SkyWater
page's two i-line entries ("ASML", "I-line", "stepper"/"scanner") rather than giving each entry its
own status, so it does not fit the Entry-as-listed/What-it-names/Status shape; left as prose, only
split for length. R-QUICKFACTS: left as written (method note 3). R-PARA (about 9 paragraphs over
100 words split, several by breaking one dense semicolon- or "and"/"that"-joined sentence at each
join and adding a paragraph break). R-SENTENCE (about 16 sentences over 45 words split, including a
three-quote "that … that … and that …" ASML sentence rewritten as three short sentences each
keeping the marker). R-RELATED (added Category/Machines/Materials/Indexes labels to the generic
bullets at the top and bottom of the section; left the eight detailed per-mask-family bullets in
the middle exactly as grouped, since they are already a considered grouping by mask family, not a
flat list). R-CAPTION (the one new table).

**A number_order loss that table conversion could not avoid, resolved by leaving a narrative
sentence as prose instead of forcing it into rows.** The ASML history bullet's middle stretch —
"The PAS 5500 platform followed in 1991 … PAS 5500/200 … in 1996 … 0.35 µm … the /275 … 0.28 µm …
100 wafers per hour" — is one continuous narrative from a single retrospective source
(`asml-30`), not a set of separately specified models. Converting it into rows still required a
`Model` cell to name each variant, which meant restating "PAS 5500/200" that the adjoining quoted
figure column *also* names verbatim (the quote cannot be altered to elide it), producing a
duplicate 5500/200 pair the checker's contiguous-regroup logic would not match back to the
original single mention. Fixed by leaving that whole narrative as prose above the table (matching
how `duv-krf-stepper.md`'s guide-authored example and this batch's earlier pages already leave a
vendor-history sentence as prose after a models table) and tabulating only the four models with
their own dedicated data-sheet or vendor citation. Also shortened two Model cells from "PAS
5500/275D" and "PAS 5500/275" to the source's own shorthand "/275D" and "/275" — the original
bullet never repeats "PAS 5500" for those two mentions, so restating it in the table was an
avoidable extra number, not a formatting choice.

`check_preserved.py --base b9f26b4d --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 (`about`, `SKY130`); all `number_order` differences resolved to REGROUPED or were
eliminated by the fix above.

Checkers, `-W` build: clean. Screenshots: phone tiles 2 (intro/quick-facts and `{seealso}`, no
overflow), 4 (11-row Representative-models table, wraps cleanly), 5 (the `{dropdown}` step-table
renders as a collapsed toggle, undisturbed) and 8 (grouped Related pages, mask bullets read well)
checked.

Content problems for the owner: none found while re-presenting this page.

### 13. `docs/machines/medium-current-implanter.md` — done

Largest paragraph-density page of the batch so far (10 H3 subsections in "What the machine class
is and how it works", each written as one dense paragraph). Rules applied: R-INTRO (template
sentence dropped, pointer moved to `{seealso}`). R-MODELS: two tables instead of one — a 5-row
Eaton/Axcelis table and a 3-row Nissin table, with the Varian paragraph (E220/E500, VIISta 810,
Swenson's contamination study, the Applied Materials acquisition) left as prose *between* them,
in its original reading position (see the number_order note below for why). R-ENTRIES: the "Read
term by term" paragraph decodes the single SkyWater entry's own fields, not several named
entries; left as prose, per the page-10/11/12 precedent. R-LIST: the opening H2's Wikipedia
sentence ("an ion source with extraction electrodes, a magnet with slits '...', 'some combination
of beam scanning...', and a way of collecting the charge...") was a four-part enumeration written
as one 69-word sentence; converted to a four-item bulleted list, each item keeping its quote and
falling under the 60-word list-item cap. R-PARA (10 of 10 H3 paragraphs and 2 list-item bodies
split, all by inserting a paragraph break at a natural topic seam rather than rewording).
R-SENTENCE (about 14 sentences over 45 words split, mostly at a semicolon or an "and"/"so" join,
several requiring the marker to be repeated on both halves per the batch's inherited rule).
R-RELATED (7 ungrouped bullets → 4 grouped: Category/Machines/Materials/Indexes). R-CAPTION (both
new tables).

**A number_order loss resolved by moving one vendor's whole paragraph out of table order.** The
Eaton/Axcelis, Varian and Nissin bullets were originally three back-to-back paragraphs; converting
all three straight into one table (vendor blocks in the same order) broke the Varian block
specifically, because its own bullet mixes a quoted "E-series ... 150mm and 200mm" fact with a
*prose* mention of "the EHP-220/500" and only *then* a second quoted "200 mm/300 mm" fact from a
different model (VIISta 810) — the prose mention sits between the two quotes in the source, but a
table's Model/Year/Published-figures columns cannot hold a free-standing prose aside between two
rows. Splitting the Representative-models section into two tables (Eaton/Axcelis, then Nissin)
with the Varian paragraph left as prose in between — its original position — reproduced the exact
source order with no rewrite. The same MC3/HE3-style fix from page 11 recurred here too: the
Axcelis MC3 row's "for 300 mm" had to move into the Model cell (`MC3 (300 mm)`) so the row emits
300 before 1998, matching the source's "the MC3 for 300 mm (1998)".

`check_preserved.py --base 0765dfeb --allow-regrouped --allow-added
quotes,markers,numbers,number_order,hedges,identifiers`: clean except the two expected losses of
method note 4 (`about`, `SKY130`); every `number_order` difference resolved to REGROUPED once the
table was split as above.

Checkers, `-W` build: clean. Screenshots: phone tiles 4–5 (both new tables and the Varian
paragraph between them, wraps cleanly with no overflow) and 8 (grouped Related pages) read well.

Content problems for the owner: none found while re-presenting this page.

## Guide problems found so far

1. **`check_preserved.py` has no way to accept a `LOST identifiers`/`LOST hedges` line, but
   R-INTRO rule 3's sanctioned template-sentence deletion reliably produces one or both on any
   page whose boilerplate sentence uses the word "SKY130" (tracked identifier) or "about"
   (tracked hedge, matched regardless of sense). This will recur on every page in this batch and
   plausibly on most of the 62 pages report B15 names. Recommend either excluding a bare,
   unattached "SKY130"/"about" inside the specific boilerplate sentence text from tracking, or
   adding an `--allow-lost` style flag for this one, narrow, already-reviewed case.
2. **The §4.2 skeleton's "grade table `Tool | Grade | Steps`" under R-STEPRUN** does not
   correspond to anything `tools/gen_step_tables.py` generates (confirmed by reading the
   generator). Left alone per method note 5; flagging so the skeleton and the generator are
   reconciled (either the generator grows this table, or the skeleton line is removed/reworded
   as a still-open, blocked item).
3. **The §1 column-budget table's "≤ 5 columns" note for a `Vendor | Model | Year | Type |
   Published figures` table (R-MODELS's own worked example shape) is not reliably safe at
   400 px** once vendor/model names are long (`cmp-polisher.md`'s first draft overflowed;
   `cd-sem-overlay-metrology.md`'s did not, with shorter names). The real test the guide gives
   ("must pass the phone test: no horizontal scroll at 400 px") is the right one; the column
   count is not a substitute for actually shooting the page at 400 px, which I did for every
   R-MODELS table in this batch from page 2 onward after finding this. Recommend the guide say
   so explicitly next to the R-MODELS worked example, since a 5-column table reads as "the
   template" otherwise. Two independent fixes were needed across the batch, and which one
   applies is page-specific: dropping a redundant `Type` column (page 2, `cmp-polisher.md`) when
   one exists, or merging `Vendor`/`Model` into one column (page 8, `film-thickness-metrology.md`)
   when every column carries distinct, undeclarable-if-lost information and there is nothing
   redundant to drop. Shortening long vendor names alone (`cmp-polisher.md`'s "Rudolph
   Technologies" → "Rudolph") fixed page 2 but was not sufficient on its own for page 8.

(to be continued — pages 3–15)
