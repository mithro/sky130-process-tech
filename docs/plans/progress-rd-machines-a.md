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

(to be continued — pages 2–15)
