# Progress — W3 category pages (topic/rd-categories)

Scope: docs/categories/{anneal,cmp,deposition,etch,implant,lithography,oxidation,strip,substrate,test}.md
(index.md excluded). Rules: R-INTRO (skeleton), quick-facts table (new), R-COMPARE, R-CAPTION, R-PARA,
R-SENTENCE, R-LIST, R-H3, R-HEDGE, R-REPEAT, R-CODE.

## Method notes (apply to every page)

* **Intro** (≤ 60 words, above the quick-facts table): the first one or two sentences of
  "## What this class of step does", copied verbatim (with their markers, if any) — not moved, so the
  same text also stays in its original place. This is a duplication, declared as an ADDED "identifiers"
  and, where the copied sentence carries a marker, an ADDED marker occurrence.
* **Quick-facts table** columns and how each cell is derived (all NEW, declared each time):
  * *What it does* — a short verbatim fragment of the page's own opening sentence(s), no new wording.
  * *Steps in SKY130 (N)* — a computed count of the data rows in this page's own "Steps in this
    category" table. Declared as an ADDED number, "computed from the Steps table row count".
  * *Tool classes (links)* — the `{ref}` targets already used for the page's "Typical equipment"
    classes, duplicated (not new links, same targets as already on the page after R-COMPARE work).
  * *Consumable classes (links)* — the `{ref}` targets added to "Typical consumables" lead-ins under
    R-COMPARE step 2 (see below), duplicated the same way.
  * *Governing relation* — the name of a named law/model/equation already given on the page's own
    "Physics and engineering background" section (its own words, e.g. "Preston's equation",
    "Deal–Grove model"), or `—` when the page names none.
* **R-COMPARE step 2 (consumables links).** Each "Typical consumables" lead-in is linked to the one
  class page from `docs/materials/index.md`'s class-page table that plainly owns that lead-in's
  materials, judged from the class's "Rows owned" column and its class-page role. Left unlinked when
  the mapping is not clear-cut.
* **R-COMPARE step 3 (Machine class column).** Built with `tmp/scripts/build_lookup.py`, which parses
  the "Machine classes and the steps that use them" table of `docs/machines/index.md` into a
  step-number → (class, qualifier) map (qualifier `primary` = listed outside any `*label:*` clause).
  For the category's own "Steps in this category" table, the Machine class cell lists every `primary`
  class from that map that is **also** a class already named in this page's own "Typical equipment"
  section (so no new fact — the class was already on the page). Where two apply, both are given.

## Pages (index) — ALL TEN DONE

- cmp.md — done
- substrate.md — done
- anneal.md — done
- oxidation.md — done
- test.md — done
- strip.md — done
- implant.md — done
- etch.md — done
- deposition.md — done
- lithography.md — done

## Pages

### lithography.md — done

The last page (556 lines, 36 mask steps). Rules applied: intro + quick-facts table (Governing relation
"Rayleigh resolution equation (k1)", the page's own {math} formula and named criterion); a new table for
the ITRS-2001 number-dense sentence (8 rows: DRAM half-pitch, MPU/ASIC gate in-resist/after-etch pairs,
contact, overlay, two CD-control figures, mask magnification) — not a material/chemistry comparison, the
same "numeric list announced by a colon" pattern already used on deposition.md's film-thickness table;
R-SENTENCE splits (the k1 physical-limit sentence, the KrF-scanner worked example, the mixed-line
sentence, the mask-type-inference sentence, the stepper/scanner sentence, one Phase-shift-masks bullet);
R-PARA on the Deep-UV-resists bullet and two Typical-equipment bullets (KrF systems, Metrology), each
split into a lead plus an indented continuation; R-COMPARE step 2 (seven consumables lead-ins linked to
`lithography-materials`); R-COMPARE step 3 (Machine class column on the 36-row steps table, generated
with a script — `overview-metal-cap`-style ambiguity does not arise here since the step pages' own KrF/
i-line readings are what the machines index already encodes); R-CAPTION on the two new tables. The
"Masks, phase shift and OPC" 2-item list and the 3-item "Photoresist chemistry" list were **not** put
through R-COMPARE: the phase-shift/OPC list is below the rule's 3-bullet threshold, and the photoresist
list's items are differently shaped (technique description, not material/steps/chemistry) — both handled
with R-PARA/R-SENTENCE instead, consistent with the judgement calls made throughout this batch.

**A genuine numeric-ordering bug found and fixed by the checker, worth flagging:** the ITRS table's two
"CD control" rows originally put the sigma value ("3σ") in the *parameter* cell and the plain number in
the *value* cell ("CD control (3σ) on the half-pitch | 15.9 nm"), which reversed the source order
(original text gives the plain figure **before** its "(3σ)" qualifier: "CD control of 15.9 nm (3σ) on the
half-pitch and 5.3 nm (3σ) on the MPU gate"). `check_preserved.py` flagged this exactly as designed — one
row's tuple came back as a plain `ADDED number_order` with no matching contiguous run in the old page,
because the digits were in the wrong relative order, not just regrouped. This is a real ordering fault a
casual read of the rendered table would not have caught (both readings look equally plausible printed as
"CD control (3σ) on the half-pitch: 15.9 nm"). Fixed by moving "(3σ)" into the value cell after its
number: "15.9 nm (3σ)" / "5.3 nm (3σ)", restoring the source order. Also caught before running the
checker: the ITRS table's own caption first read "ITRS 2001 targets for the 130 nm node, as given for the
year 2001" — reusing the digits `2001`/`130`/`2001` as new numbers sitting *between* the lead-in
sentence's own `2001` and the table's first row, which broke contiguity for the whole 15-number original
run even though every individual row was internally correct. Fixed by writing a caption with no digits at
all ("ITRS targets for this node's introduction year, as listed in the paragraph above"). General lesson
for any future page: a new caption or header sitting between an already-cited number and the table that
continues it must not introduce its own numbers, even ones that "just repeat" facts already on the page,
or it silently breaks the contiguous-run check for everything that spans the caption.

`check_preserved.py --base f09d8c11 --allow-regrouped --allow-added markers,numbers,refs,identifiers` →
exit 0. Many `--allow-regrouped` groups (the Resolution/k1 sentences, the ITRS 8-row table, the
phase-shift-mask bullet, the two split equipment bullets), all confirmed by hand — same digits, same
order, split cleanly at sentence/row boundaries.

* **ADDED markers:** `itrs-03`, `lin-2002`, `mack-2007`, `wiki-psm` (one extra occurrence each) —
  R-SENTENCE rule 5 repeats.
* **ADDED numbers:** `36` — Steps-in-SKY130 count (matches the page's own "36 of them" sentence).
* **ADDED refs:** `machine-duv-krf-stepper` ×15, `machine-i-line-stepper` ×25, `machine-coat-develop-track`
  ×1 (quick facts + the 36-row Machine class column), `material-lithography-materials` ×8 (quick facts +
  the seven consumables lead-ins).
* **ADDED identifiers:** `SKY130` ×1, `k1` ×1 (the quick-facts row label "Rayleigh resolution equation
  (k1)" repeats the page's own `{term}`k1`` word).

Quick-facts derivation: What it does = verbatim fragment of the opening sentence. Steps in SKY130 = 36
(steps table; matches the page's own count). Tool classes = the three `{ref}` targets in Typical
equipment. Consumable classes = `lithography-materials` (owns every row this page's consumables bullets
name). Governing relation = "Rayleigh resolution equation (k1)", named directly in "Resolution, k1 and
depth of focus".

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: both new tables and the 36-row,
4-column steps table wrap cleanly at 400 px, no horizontal scroll.

## Batch summary (all ten category pages)

**Pages done:** cmp, substrate, anneal, oxidation, test, strip, implant, etch, deposition, lithography —
all ten, each committed separately, each passing the full checker suite and a clean `-W` build.

**Numbers.** Every page gained: a ≤60-word intro, a 5-row quick-facts table (What it does / Steps in
SKY130 / Tool classes / Consumable classes / Governing relation), a `Machine class` column on its "Steps
in this category" table (all steps-table row counts cross-check against the page's own prose count where
one was given: cmp 12, substrate 1, anneal 7, oxidation 6, test 1, strip 15, implant 25, etch 27,
deposition 41, lithography 36 — 171 rows total, one per step in the flow, no double-counting).
Six category pages gained at least one R-COMPARE or number-list table beyond the
quick-facts table (cmp's existing table gained a caption only; implant, etch, deposition ×3, lithography
×2 gained genuinely new comparison/data tables); every new table has an R-CAPTION caption. Roughly 40
consumables lead-ins were linked to their material-class page across the ten pages; roughly 35
R-SENTENCE/R-PARA/R-LIST edits were made in total.

**Guide problems found (for the coordinator, not fixed here):**
* R-CAPTION's crib doesn't say what to do when a table's own caption would sit between an
  already-cited number and a table that continues counting it — see the lithography.md write-up above.
  This is a `check_preserved.py`-driven finding specific to the new-table-per-page pattern this batch
  used a lot; worth a line in the guide for the next batch that builds new tables (masks doesn't have W3
  category-style new content, but overview or future batches might).
* R-COMPARE's rule text is written around a single shape ("thing (steps): values; explanation") but in
  practice about half the qualifying triples/quadruples on these ten pages lacked per-item step refs
  (implant's Threshold-adjust row, etch's Tungsten row, several LPCVD/PECVD rows). The rule already
  tolerates this via `—`, which worked cleanly every time, but the guide's own single worked example
  doesn't show the no-ref case — worth adding a one-line note for the next executor.
* The R-COMPARE column header "Typical chemistry" (the rule's own prescribed name) collides with the
  `check_preserved.py` hedge word list (`typical`); see the etch.md write-up. Not a guide bug exactly —
  more a note that this specific, unavoidable collision should be pre-declared in the guide rather than
  rediscovered per page.

**Content problems found (not fixed, flagged for the owner):** none. No arithmetic slips, unit errors or
factual contradictions were noticed while re-presenting any of the ten pages.

### deposition.md — done

The biggest page in the batch (532 lines, 41 steps, four separate technique sections each with its own
film list). Rules applied: intro + quick-facts table (Governing relation "Arrhenius growth-rate law",
from the page's own {math} formula in "Growth regimes and conformality"); three R-COMPARE-style tables
(LPCVD films: 3 rows + a 4th for HTO split out of a combined bullet; PECVD films: 4 rows, all short
enough to keep their explanation in the table itself — none over 40 words — so no separate prose was
needed; a film-thickness table built from the "Film thicknesses in SKY130" number-dense sentence, not a
material/chemistry comparison but the same "numeric list announced by a colon" shape, converted the same
way); R-PARA on two PVD/metallisation bullets (Titanium/TiN, Titanium–tungsten) — kept as labelled
paragraphs rather than a fourth table, since this list is about layer history/function (Blech length,
the metal-cap open question) rather than a clean chemistry comparison, matching the same judgement as
anneal.md's silicide bullets and etch.md's aluminium-cap paragraph; R-SENTENCE splits (the "choice
between them" sentence, the conformality-regime sentence); R-COMPARE step 2 (seven consumables lead-ins
linked across `precursors`/`process-gases`/`dopant-sources`/`etch-gases`/`sputter-targets`/
`hardware-consumables`); R-COMPARE step 3 (Machine class column on the 41-row steps table, generated with
a script from the machines-index lookup rather than typed by hand, given the size — several rows carry
two co-primary classes, e.g. PECVD+HDP-CVD for the ILD oxide steps); R-CAPTION on all four new tables.

Applied the etch.md lesson throughout: every row's own numbers were kept inside that row's own cells
(e.g. the silicon-nitride row's "tensile stress of order 1 GPa" stayed in the composition cell rather
than moving to prose after the table), so no number ever had to cross other rows to reach a same-bullet
number placed in prose. This produced **zero LOST or bare-unregrouped number_order entries** on the first
checker run — the only page in this batch where that was true without a second pass.

`check_preserved.py --base 0e980ba7 --allow-regrouped --allow-added markers,numbers,refs,hedges,
identifiers` → exit 0. Three `--allow-regrouped` groups, all confirmed by hand: the silicon-nitride
bullet's digits reappearing (with the added "1" GPa figure) in the same row; the TEOS/HTO bullet's two
temperature pairs, now in two separate rows but each internally intact; the 14-number film-thickness run,
now one table with one row per figure, same digits, same order read top to bottom.

* **ADDED markers:** `txt-01`, `ohring-2002` (one extra occurrence each) — R-SENTENCE rule 5 repeats.
* **ADDED numbers:** `41` — Steps-in-SKY130 count.
* **ADDED refs:** the five machine-class targets across quick facts and the 41-row Machine class column
  (`machine-pecvd` ×20, `machine-pvd-cluster-tool` ×14, `machine-hdp-cvd` ×8, `machine-tungsten-cvd` ×6,
  `machine-vertical-furnace-lpcvd` ×6); the six material-class targets from the consumables links and
  quick facts; `step-003`/`step-048`/`step-058`/`step-076` ×1 each (kept in both the LPCVD table's Steps
  cells and the "used for..." prose that names the same steps by their bold labels).
* **ADDED hedges:** `typical` ×1 — the LPCVD table's caption echoes the page's own "typical industry
  conditions" phrase from the sentence directly above it (unchanged, still on the page).
* **ADDED identifiers:** `SKY130` ×4.

Quick-facts derivation: What it does = verbatim fragment of the opening sentence. Steps in SKY130 = 41
(steps table, generated and cross-checked against the source table's own row count). Tool classes = the
five `{ref}` targets in Typical equipment. Consumable classes = `precursors` and `sputter-targets`, the
two classes that between them own most of this page's named consumables (gases and dopant sources were
left out of the summary cell for brevity, as elsewhere in this batch). Governing relation = the Arrhenius
growth-rate law named in "Growth regimes and conformality".

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: all four new tables and the 41-row
steps table wrap cleanly at 400 px, no horizontal scroll.

### etch.md — done

This is report-B7's own named example: "Chemistries by material" (7 bullets) is the exact passage the
rule was written from (`etch.md:91` in the report text), so it became the literal
`Material | SKY130 steps | Typical chemistry` table (dropped the fourth "Why" column — every explanation
here is over 40 words, so per R-COMPARE step 1 it all stays as prose below the table, under the same
material names as bold run-in labels, and a fourth column would have held nothing). Rules applied: intro
+ quick-facts table (Governing relation "ion-enhanced etch-yield law (Steinbrüchel)", from the page's own
{math} formula and citation); R-COMPARE table (7 rows; the Tungsten row has no step ref in the source, so
`—`); R-LIST (the "four numbers" rate/selectivity/anisotropy/uniformity sentence, zero markers, pure
reformat); R-SENTENCE splits (the RF-plasma quote sentence, the Coburn-and-Winters sentence, the ICP
sentence, the BOE/HF sentence, the endpoint/interferometry sentence); R-COMPARE step 2 (five consumables
lead-ins linked to `etch-gases`/`wet-chemicals`/`hardware-consumables`); R-COMPARE step 3 (Machine class
column on the 27-row steps table, three rows carrying two classes where the machines index lists both as
primary); R-CAPTION on the new tables.

**Two mistakes caught and fixed before the checker run, both worth flagging for whoever reviews this
batch:**
1. My first cut at the table left the original "Ti:W and TiN", "Anti-reflective coatings" and "Tungsten"
   bullets in place below it (my `old_string` for the Edit call stopped short of the full original bullet
   list), so those three materials were briefly duplicated — once in the new table, once in the leftover
   bullets. Caught by reading the file back, not by the checker (which would have reported it as `ADDED`
   refs/text, not a hard failure, so it is worth an explicit re-read of the diff after every multi-bullet
   replacement, not just a green checker run).
2. Converting "metal 1–5, {ref}`MM1E` to {ref}`MM5E`; the 2013 Cypress report..." lost the `1–5` number
   when the table's Steps cell kept only the `{ref}` range and the "2013/2014/130" numbers moved to a
   separate prose paragraph several table rows later — breaking `check_preserved.py`'s contiguous-run
   check (nothing between the original `1–5` and `2013` in the source, but four other rows' numbers now
   sat between them). Fixed by moving `1–5` into the same prose paragraph ("For metal 1–5, a 2013 Cypress
   report…"), immediately ahead of `2013`, restoring contiguity. General lesson for the remaining page
   (deposition) and any reviewer: when a bullet's lead clause and its explanation both carry numbers and
   the explanation is being pushed to prose after the table, keep every number that was in the lead
   *with* the explanation's numbers (same paragraph, correct order) rather than splitting them into the
   table row and the prose separately.

`check_preserved.py --base 2b1188ec --allow-regrouped --allow-added markers,numbers,refs,hedges,
identifiers` → exit 0. One `--allow-regrouped` group confirmed by hand (the BOE/HF sentence's
`6,1,40,49,2,25` run, now on its own sentence, unchanged order; the `HF₂⁻` superscript-minus token that
was part of the same original unit is now alone in the preceding sentence, below the tracking threshold,
consistent with a clean split).

* **ADDED markers:** `wiki-rie`, `wiki-boe`, `wiki-hf` (one extra occurrence each) — R-SENTENCE rule 5
  repeats.
* **ADDED numbers:** `27` — Steps-in-SKY130 count (matches the page's own "27 etch steps" sentence).
* **ADDED refs:** `hard mask` ×1 (new intro repeats the opening sentence's own `{term}` use);
  `machine-plasma-etcher-dielectric` ×13, `machine-plasma-etcher-metal` ×9,
  `machine-plasma-etcher-silicon` ×5, `machine-single-wafer-spin-processor` ×4, `machine-wet-bench` ×3
  (quick facts + Machine class column, three rows with two classes); `material-etch-gases` ×4,
  `material-hardware-consumables` ×1, `material-wet-chemicals` ×1; `step-166` ×1 (kept in both the table's
  Steps cell and the "mainly oxide on the reading of that page" aside moved to prose).
* **ADDED hedges:** `typical` ×1 — unavoidable: the R-COMPARE rule's own prescribed column header is
  "Typical chemistry", literally named in the guide. Declared, not reworded, because renaming the rule's
  own column header would be a bigger deviation than a harmless hedge-word match on UI chrome.
* **ADDED identifiers:** `SKY130` ×2.

Quick-facts derivation: What it does = verbatim fragment of the opening sentence. Steps in SKY130 = 27
(steps table; matches the page's own count). Tool classes = the three plasma-etcher `{ref}` targets in
Typical equipment (wet-process classes left out of the summary cell). Consumable classes = `etch-gases`
(owns the fluorine/chlorine/additive rows this page names). Governing relation = the Steinbrüchel
ion-enhanced etch-yield law, the page's own cited formula.

Checkers, `check_inforce.py` in particular (the metal-cap paragraph touches the same topic as prior
in-force findings on other pages; verified clean — no patent number or restricted phrase appears outside
a dropdown here), and `-W` build all pass. Screenshots (desktop, 400 px) reviewed: the R-COMPARE table
and the 4-column, 27-row steps table both fit at 400 px, no horizontal scroll.

### implant.md — done

The first page in this batch with a genuine, literal R-COMPARE match: "Implant classes in a 130 nm CMOS
flow" is 5 bullets of exactly the shape *class (steps): values; explanation*, so it became the named
`Material | SKY130 steps | Typical chemistry | Why` shape (columns renamed `Implant class | SKY130 steps
| Species, energy and dose | Note`, per R-COMPARE step 1). Rules applied: intro + quick-facts table
(Governing relation "LSS theory", the page's own H3 name); R-COMPARE table (5 rows; one row,
Threshold-adjust, has no step refs in the source, so its steps cell is `—`, not invented); R-LIST four
times (the "25 implants, in order" sentence; the "two mechanisms" nuclear/electronic stopping sentence;
the "classified by current and energy" implanter-class sentence — all zero-marker or single-trailing-
marker passages, safe reformats); R-SENTENCE (the Gaussian peak-concentration sentence); R-COMPARE step 2
(four consumables lead-ins linked to `dopant-sources`/`hardware-consumables`); R-COMPARE step 3 (Machine
class column on the 25-row steps table, from the machines index, several rows carrying two classes where
the index lists both as `primary`); R-CAPTION on the new tables.

**Numeric-preservation design for the R-COMPARE table** (worth recording as a pattern for any later
review): the guide's four-column shape puts short parallel facts in "Species, energy and dose" and any
longer explanation in "Note" — and two of the five source bullets carry a quoted or nearly-as-long ITRS
sentence with its own numbers (`2001`, `0.5`; `2001`, `130`, `51`). Putting a row's dose numbers and its
own explanation numbers in the **same row** (dose cell, then note cell, left to right) keeps them exactly
as `check_preserved.py`'s contiguous-run check expects — the tool treats a whole table row as one
left-to-right sequence. Splitting a bullet's numbers across a table (for the dose) and separate prose
placed *elsewhere* on the page (for the explanation) — my first attempt — breaks contiguity as soon as
another row's numbers fall in between; fixed by keeping each row's own explanation with its own row
(quoted in full in the Note cell) and moving only the number-free connective sentences ("we infer...",
"the extension and halo implants form...") to a shared paragraph after the table.

Also caught before running any checker: the new table's own header row read "Typical species, energy and
dose", which would have been a real, undeclarable ADDED hedge (`typical`, matching `HEDGES` in
`check_preserved.py`) purely from a header label, not a hedge on any fact. Renamed to "Species, energy
and dose" to avoid manufacturing a hedge out of new UI chrome. Reviewers of the remaining pages: check
new column headers for this word before running the checker.

`check_preserved.py --base 77f42034 --allow-regrouped --allow-added markers,numbers,refs,identifiers` →
exit 0. Six `--allow-regrouped` groups confirmed by hand, including the two multi-number table rows
above; all read back correctly as the same digits, same order.

* **ADDED markers:** `wiki-implant`, `current-2017` (one extra occurrence each) — R-LIST rule 1 repeats
  (lead-in colon plus the original trailing position).
* **ADDED numbers:** `25` — Steps-in-SKY130 count (cross-checks the page's own "the SKY130 flow has 25
  implants" sentence).
* **ADDED refs:** `machine-high-current-implanter` ×7, `machine-high-energy-implanter` ×8,
  `machine-medium-current-implanter` ×21 (quick facts + the Machine class column, several rows carrying
  two classes), `material-dopant-sources` ×4, `material-hardware-consumables` ×1.
* **ADDED identifiers:** `SKY130` ×2.

Quick-facts derivation: What it does = verbatim fragment of the opening sentence. Steps in SKY130 = 25
(steps table; matches the page's own count). Tool classes = the three `{ref}` targets in Typical
equipment. Consumable classes = `dopant-sources` (owns every row this page's "Source gases"/"Solid
sources"/"Ion-source parts" bullets name). Governing relation = "LSS theory" (the page's own H3 title and
`{term}`).

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: the 4-column R-COMPARE table and
the 4-column steps table both wrap cleanly at 400 px with no horizontal scroll (cells stack tall but stay
within the column width).

### strip.md — done

Rules applied: intro + quick-facts table (Governing relation "—", no named law on this page); R-PARA on
the SPM/SC-1/SC-2 and Ashers list items (each already had 2-3 sentences; split into a lead sentence plus
an indented continuation, wording unchanged) — the "Wet strip and clean chemistry" 5-bullet list was
**not** put through R-COMPARE: it has no `(steps)` per item (these are general chemistries, not tied to
numbered steps), so the rule's own trigger shape does not match, matching the same judgement made for
anneal.md's Titanium/Cobalt bullets; R-SENTENCE splits (the nitride-strip hot-phosphoric sentence, the
surface-state sentence), each a semicolon/colon joining two claims; R-COMPARE step 2 (five consumables
lead-ins linked: Gases → `process-gases`, Acids and bases/Solvents → `wet-chemicals`); R-COMPARE step 3
(Machine class column on the 15-row steps table — 14 rows get `Downstream plasma asher`, the primary
class for every implant-mask strip; `NS19` (the wet nitride strip) gets `Wet bench`, its own primary
class per the machines index); R-CAPTION on the new steps table.

`check_preserved.py --base bd8ab46d --allow-regrouped --allow-added markers,numbers,refs,identifiers` →
exit 0, no LOST or REGROUPED entries at all (every split landed on a sentence boundary with no digit
runs to preserve).

* **ADDED markers:** `txt-02`, `wiki-h3po4` (one extra occurrence each) — R-SENTENCE rule 5 repeats.
* **ADDED numbers:** `15` — Steps-in-SKY130 count.
* **ADDED refs:** `machine-downstream-plasma-asher` ×15, `machine-wet-bench` ×2 (quick facts + Machine
  class column), `material-process-gases` ×1, `material-wet-chemicals` ×3 (quick facts + the three
  linked consumables lead-ins).
* **ADDED identifiers:** `SKY130` ×1.

Quick-facts derivation: What it does = trimmed from the page's own opening sentence. Steps in SKY130 =
15 (steps table). Tool classes = the two dominant `{ref}` targets in Typical equipment (Ashers, Wet
benches — Spray processors and single-wafer spin processors share the `machine-wet-bench`/
`machine-single-wafer-spin-processor` targets already and were left out of the summary cell). Consumable
classes = `wet-chemicals`, the class page owning every acid/base/solvent row this page names. Governing
relation = `—` (no named law on this page — plasma ashing and RCA-clean chemistry are described only
qualitatively).

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: no horizontal scroll; the 15-row,
4-column steps table wraps cleanly on the phone tile.

### test.md — done

Rules applied: intro + quick-facts table (Governing relation "Van der Pauw's theorem", named on the page
in "Sheet resistance and van der Pauw"); R-LIST three times (the "wafer testing comes in two kinds"
sentence → two bullets; the "by our count they include" module-count sentence, a dense 12-number run →
six bullets, kept as a plain list since it is a tally, not a chemistry/material comparison; the PCM list
was already bulleted, untouched); R-PARA with bold run-in labels on the test-tile evidence block (The
public test tile / Module counts / Measurement files / Passive-device files — an evidence sequence, so
labelled per R-PARA step 3) — this also fixes what had been one ~230-word paragraph; R-SENTENCE splits
(the four-terminal-measurement sentence, the transistor-sweep sentence), each a semicolon joining two
claims; R-COMPARE step 2 (two consumables lead-ins linked: Probe cards → `hardware-consumables`
(its `probe-cards` row), Test wafers → `substrates`); R-COMPARE step 3 (Machine class column, one row:
Parametric tester); R-CAPTION on the new steps table.

**Tool-limitation finding, worth flagging to the coordinator:** converting "wafer functional testing
(also called die sort or `{term}`wafer\nsort``)" into a list item at first produced a false LOST/ADDED
ref pair in `check_preserved.py` — not a real change. The original source happens to hard-wrap the bare
`{term}` role across a line break with no indentation (`{term}`wafer` / `sort``), and `role_target()`
only strips leading/trailing whitespace from a bare (no explicit `<target>`) role's content, so the
literal embedded newline is part of the extracted "ref" string. My first two reformattings (indented
list continuation, then an explicit `<wafer sort>` target) both legitimately changed that raw string and
were flagged, even though the rendered link is identical either way. Fixed by keeping the same bare role
with the same mid-word line break, using CommonMark's lazy-continuation rule (an unindented follow-on
line still belongs to the list item's paragraph) so the source bytes inside the backticks are now
byte-for-byte what they were before. No content changed at any point; this is a documented tool
quirk (whitespace inside a bare, target-less role is not normalised) for whoever reviews the other
category pages, in case the same pattern recurs.

`check_preserved.py --base 26714efa --allow-regrouped --allow-added markers,numbers,refs,identifiers` →
exit 0. One `--allow-regrouped` group confirmed by hand: the original 12-digit module-count run
(36,28,24,300,2,7,9,6,6,1,4,2) reappears as three contiguous sub-runs across the new bullets
((28,24,300,2), (9,6,6), (1,4)) with the other four digits (36, 7, 2) now alone in their own bullets,
below the tool's two-number tracking threshold — same digits, same order throughout.

* **ADDED markers:** `raw-data-testtile-pads` (one extra occurrence, R-LIST rule 1: repeated on the
  list's lead-in colon as well as its original position on the trailing clause), `wiki-rs`, `wiki-4t`
  (one extra occurrence each, R-SENTENCE rule 5).
* **ADDED numbers:** `1` — Steps-in-SKY130 count.
* **ADDED refs:** `WAT`, `e-test` (the new intro repeats the page's own naming sentence),
  `machine-parametric-tester` ×2, `material-hardware-consumables` ×2, `material-substrates` ×1.
* **ADDED identifiers:** `SKY130` ×1.

Quick-facts derivation: What it does = verbatim fragment "the finished wafer is measured rather than
changed". Steps in SKY130 = 1. Tool classes = the one `{ref}` target in Typical equipment. Consumable
classes = `hardware-consumables` (its `probe-cards` row is this page's main consumable). Governing
relation = "Van der Pauw's theorem" (page's own H3 and named theorem).

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: the reformatted evidence block and
new lists read cleanly; no horizontal scroll.

### oxidation.md — done

Rules applied: intro + quick-facts table (Governing relation "Deal–Grove model", the page's own named
model); R-LIST (the "oxidation steps are" sentence, 5 items → bullets, zero markers/numbers so a pure
reformat; the "grows its gate oxides in two passes" description → a numbered list, a genuine sequence
per R-LIST rule 6); R-SENTENCE splits (the "Because the oxide is grown..." sentence, the "Precisely: the
wafer is heated..." sentence — split with an added subject "It is exposed to...", the ISSG sentence);
R-CAPTION on the Deal–Grove parameters table (previously only a colon lead-in, which is not a caption on
a class page — see the rule's step-page-only exception) and the new steps table; R-PARA on three
list items over the cap (Gate oxides, Field oxides in "Thin gate oxide versus thick field oxide";
Vertical batch furnaces in Typical equipment) — each split into a lead sentence plus an indented
continuation, wording unchanged; R-COMPARE step 2 (five consumables lead-ins linked to
`process-gases`/`hardware-consumables`/`substrates`); R-COMPARE step 3 (Machine class column on the
6-row steps table — two rows get both Vertical furnace and Rapid thermal processor, matching the
machines index where both are listed as `primary` for those two steps, not one primary/one alternative).

Caught and reverted during drafting: the first pass of the "Because the oxide is grown..." split
mistakenly attached `[^wiki-thox]` to the first half — that sentence has **no** citation in the
original at all. Fixed before running any checker (would have been a fabricated citation, forbidden by
§2 rule 1/4). Recorded here as a caution for reviewers of the remaining pages in this batch, not as a
live defect.

`check_preserved.py --base b71c67d9 --allow-regrouped --allow-added markers,numbers,refs,identifiers` →
exit 0. Two `--allow-regrouped` groups confirmed by hand (the 800/1200/2/2 tuple from the wafer-heating
sentence split into two sentences' worth of digits in the same order; the 900–1000/250 tuple from the
Field-oxides bullet split the same way).

* **ADDED markers:** `txt-09` (one extra occurrence) — R-SENTENCE rule 5 repeat.
* **ADDED numbers:** `6` — Steps-in-SKY130 count.
* **ADDED refs:** `machine-vertical-furnace-oxidation` ×7, `machine-rapid-thermal-processor` ×3 (quick
  facts + Machine class column), `material-process-gases` ×4, `material-hardware-consumables` ×1,
  `material-substrates` ×1 (quick facts + the five consumables lead-ins).
* **ADDED identifiers:** `SKY130` ×1.

Quick-facts derivation: What it does = a verbatim fragment of the page's opening sentence. Steps in
SKY130 = 6 (steps table). Tool classes = the two `{ref}` targets in Typical equipment. Consumable
classes = `process-gases` (the class page owning every "Typical consumables" row on this page — O2, H2,
N2, HCl/DCE, N2O/NO are all `process-gases` rows per the materials index; quartz hardware and dummy
wafers were linked separately in the body to their own classes but left out of this summary cell to keep
it to the one dominant class). Governing relation = "Deal–Grove model" (the page's own `{term}` and H3).

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: numbered list renders correctly,
Deal–Grove table and the new equipment/steps tables fit at 400 px with no horizontal scroll.

### anneal.md — done

Rules applied: intro + quick-facts table (Governing relation "Fick's laws of diffusion", the page's own
named law); R-LIST twice (the opening "make something happen that only heat can do:" four-item sentence
→ Repair/Diffuse/React/Sinter bullets; the "Two effects make the choice of anneal a compromise:" sentence
→ Deactivation/TED bullets — both zero-marker, zero-number passages, so purely a reformat); R-SENTENCE
splits (activation-energy sentence, RTP intro sentence, RTA-chamber sentence, Titanium and Cobalt
silicide bullets, the alloy-anneal passivation sentence — each a semicolon joining two claims, trailing
whole-sentence marker repeated where the original had only one); R-PARA (the "Rapid thermal processors"
equipment bullet, >60 words, split into a lead sentence plus an indented continuation, wording
unchanged); R-COMPARE step 2 (three consumables lead-ins — Gases, RTP hardware, Furnace hardware — linked
to `anneal-ambients`/`hardware-consumables` per the materials index class table); R-COMPARE step 3
(Machine class column on the 7-row steps table, from the machines index: `Rapid thermal processor` for
five rows, `Vertical furnace` for the two alloy steps, which the machines index lists as the *primary*
class for 96/170 with RTP only as the *alternative*); R-CAPTION on the new steps table. The "Silicidation"
Titanium/Cobalt bullets were **not** put in an R-COMPARE table (only two items — the rule's own trigger
is "three or more bullets"), so R-PARA was used instead.

`check_preserved.py --base 7b117719 --allow-regrouped --allow-added markers,numbers,refs,identifiers` →
exit 0. All four `--allow-regrouped` groups (the diffusion sentence, the Titanium bullet, the alloy
sentence, the "Rapid thermal processors" equipment bullet) were confirmed by hand: each LOST tuple's
digits reappear, same order, in the REGROUPED "now" lines the tool prints alongside it.

* **ADDED markers:** `deal-1980`, `wiki-rtp` (one extra occurrence each), `txt-01` (two extra
  occurrences, from two different R-SENTENCE splits) — rule 5 repeats.
* **ADDED numbers:** `7` — the Steps-in-SKY130 count (matches the page's own "seven thermal steps"
  wording, so also a cross-check).
* **ADDED refs:** `category-oxidation` ×1 (new intro repeats the page's own "Unlike oxidation (...)"
  sentence), `machine-rapid-thermal-processor` ×6, `machine-vertical-furnace-anneal` ×3 (quick facts,
  steps-table Machine class column), `material-anneal-ambients` ×2, `material-hardware-consumables` ×3
  (quick facts + the three consumables lead-ins).
* **ADDED identifiers:** `SKY130` ×1 — the quick-facts row label.

Quick-facts derivation: What it does = built from the labels the R-LIST conversion itself created
(Repair/Diffuse/React/Sinter), each label taken from that item's own words, so still page-derived.
Steps in SKY130 = 7 (steps table). Tool classes = the two `{ref}` targets in Typical equipment.
Consumable classes = the two class pages the consumables bullets were linked to. Governing relation =
"Fick's laws of diffusion" (H3 "Diffusion", `{math}` block).

Checkers and `-W` build pass. Screenshots (desktop, 400 px) reviewed: no horizontal scroll, four-column
steps table wraps cleanly on the phone tile.

### substrate.md — done

Rules applied: intro + quick-facts table (Governing relation `—`, none named on this page); R-SENTENCE
(five semicolon-joined sentences split: SKY130-layer-set/infer sentence, the Czochralski sentence, the
boule-slicing quote sentence, the (100)-surface/notch sentence, the Boron/resistivity sentence — each
trailing whole-sentence marker repeated on both halves per rule 5); R-PARA (three >60-word list items in
"What this class of step does" — Diameter/thickness, Crystal orientation, Doping type — each already
had two sentences; turned the second sentence of each into an indented continuation paragraph, no
wording changed at all); R-COMPARE step 2 (two "Typical consumables" bullets' lead-ins linked to
`material-substrates`, the one class-page row-owner for `si-wafers`/`test-wafers`; "Wafer carriers" left
unlinked, no owning row); R-COMPARE step 3 (Machine class column, one row: `Incoming inspection`);
R-CAPTION on the new steps table. "Typical equipment" bullets were **not** restructured into a table:
none of them are flagged over the length caps and the section's own framing sentence ("no process tool
in the fab itself... at the wafer vendor") would be awkward to preserve in a strict three-column table
without inventing connective text, so the rule does not clearly apply here (§0's "leave the text alone"
default) — left as the existing bulleted list. R-H3, R-LIST, R-REPEAT, R-CODE, R-HEDGE: none found
needed.

`check_preserved.py --base bdfd706c --allow-regrouped --allow-added markers,numbers,quotes,refs,
identifiers` → exit 0.

* **ADDED markers:** `pdk-01`, `txt-01`, `wiki-cz` (one extra occurrence each) — R-SENTENCE rule 5 repeats.
* **ADDED numbers:** `1` — Steps-in-SKY130 count (one row in the Steps table).
* **ADDED quotes:** `starting material` ×1 — the new intro repeats the page's own quoted phrase
  (unchanged elsewhere on the page).
* **ADDED refs:** `machine-starting-material` ×2 (quick facts + Machine class column),
  `material-substrates` ×3 (quick facts + two consumables lead-ins).
* **REGROUPED number_order** (confirmed by hand): three original multi-number units, each split by an
  R-SENTENCE edit, reappear as the same digits in the same order, split across the resulting sentences
  (Miller-index tuple `100,111` + a lone, untracked `100`; the `200 mm wafers` pair, one per new
  sentence; the `100,111,200,110` run, split into `100,111` and `200,110`). No digit altered or swapped.
* **ADDED identifiers:** `SKY130` ×1 — the quick-facts row label "Steps in SKY130".

Quick-facts derivation: What it does = a verbatim (trimmed) fragment of the page's own "it fixes the
diameter..." clause. Steps in SKY130 = 1 (the Steps table). Tool classes = the one `{ref}` target
already used for "Incoming inspection" in Typical equipment. Consumable classes = `material-substrates`,
the class-page owner of every row this page's consumables bullets name. Governing relation = `—` (no
named law or equation on this page).

Checkers (`check_refs`, `check_inforce`, `gen_index_links --check`, plus the full suite) and `-W` build
all pass. Screenshots reviewed at desktop and 400 px: no horizontal scroll, four-column steps table
wraps cleanly on the phone tile.

### cmp.md — done

Rules applied: intro + quick-facts table (new), R-COMPARE (consumables links, Machine class column;
no comparison-bullet table needed — `cmp.md`'s comparison table was already in table form, the model
the guide names to copy), R-CAPTION (comparison table, new equipment table, new steps table), R-PARA
(Chemistry-and-mechanics paragraph split into Oxide/Tungsten/pad sub-paragraphs), R-SENTENCE (Preston
deviations sentence, Kaufman tungsten sentence, Chip-History/Mesa sentence — all semicolon splits),
R-LIST (the "two classic defects" sentence → dishing/erosion bullets, matching the guide's own worked
example). R-H3, R-HEDGE (n/a — no "How it is typically performed" section on category pages), R-REPEAT,
R-CODE: none found needed on this page.

`check_preserved.py --base 7e1cbff3 --allow-regrouped --allow-added
markers,numbers,refs,hedges,identifiers` → exit 0, declarations below (no LOST anything, no undeclared
ADDED):

* **ADDED markers:** `kaufman-1991` ×1 — R-SENTENCE rule 5 (repeat a trailing whole-sentence marker on
  both halves of a split).
* **ADDED numbers:** `12` — the Steps-in-SKY130 count, computed from the "Steps in this category" table's
  row count (12 rows). (The "Typical equipment" bullets were turned into labelled paragraphs, byte-for-
  byte the same wording as the original bullets apart from the label, so the Mirra/F-REX/IPEC/Strasbaugh
  numbers keep their original contiguous order; the new scanning table's own cells were written to name
  vendors and models **without** repeating any of those digits, precisely to avoid a second, conflicting
  copy of the same numbers elsewhere on the page.)
* **ADDED refs:** `CMP` ×1 (the new intro paragraph repeats the page's own opening two sentences,
  including its `{term}`CMP`` use). `machine-cmp-polisher` ×13, `machine-post-cmp-cleaner` ×1,
  `machine-film-thickness-metrology` ×1, `machine-cross-section-sem-profilers` ×1,
  `machine-defect-inspection` ×1, `material-cmp-consumables` ×4 — the quick-facts table (Tool classes,
  Consumable classes cells), the new scanning table's class links, the Machine class column added to
  all 12 rows of the steps table (R-COMPARE step 3), and the three "Typical consumables" lead-ins linked
  under R-COMPARE step 2 (Slurries, Pads, Chemicals — all three are rows of the `cmp-consumables` class
  page per `docs/materials/index.md`'s class table; "Conditioners" left unlinked, not a listed row-owner
  there).
* **ADDED hedges:** `typical` ×1 — the new caption on the polishes-compared table echoes the existing
  lead-in sentence's own words ("typical of the node"); the original sentence is untouched and still on
  the page.
* **ADDED identifiers:** `SKY130` ×2 — one in the quick-facts row label "Steps in SKY130", one in the
  new table caption echoing the existing "SKY130's own films are this reference's readings" sentence
  (untouched, still on the page).

Quick-facts cell derivation (for the record):
* What it does — verbatim fragment of the page's own first two clauses.
* Steps in SKY130 — counted from the Steps table (12 rows).
* Tool classes — the two `{ref}` targets already used in "Typical equipment" (Polishers, Post-CMP
  cleaners); the three metrology classes were left out of this cell to keep it short (all facts stay
  on the page in the equipment table itself).
* Consumable classes — the one class page (`cmp-consumables`) that owns every row named in "Typical
  consumables" per `docs/materials/index.md`.
* Governing relation — "Preston's equation", the page's own H3 title and `{term}` name.

Checkers: `check_steps.py`, `check_refs.py`, `check_machines.py`, `check_materials.py`,
`check_masks.py`, `check_inforce.py`, `gen_index_links.py --check` all pass. `-W` build clean.
Screenshots before/after at desktop and 400 px reviewed; no horizontal scroll, no oversized cells.

Design note for "Typical equipment" (applies to every page in this batch): the guide's skeleton names a
`Tool class (link) | Representative models | Note` table for this section, with model history "staying
on the machine page". The category pages' existing "Typical equipment" bullets carry quotations and
model-history facts (dates, quoted specs) that are not, in fact, only on the machine page — they are
also written out here, and `check_preserved.py`/rd-common.txt rule 3 forbid deleting them from this page
to avoid a duplicate. The pattern used on every page: the original bullet becomes a bold-labelled
paragraph (one per equipment class), keeping every word, quote, number and marker exactly as before
(often this alone brings a >60-word list item under the 100-word paragraph cap, since R-PARA's list-item
cap is stricter than its paragraph cap); a short scanning table is added after the paragraphs, naming
each tool class (linked) and its vendors/models **without repeating any digit already given in the
paragraph above**, so the new table adds zero numbers and cannot create a second, differently-ordered
copy of a number sequence for `check_preserved.py`'s contiguous-run check to trip over. This is
documented once here rather than repeated on every page's entry below.


## Fix round (review): tmp/reviews/rd-categories.md, 2026-09-26

Reviewer verdict was "approve with fixes": nine lost citations, two dropped hedges ("of order" x2) and
one added hedge ("roughly"), one widened hedge (etch's NSME), one re-worded-into-false claim (implant's
extension/halo sentence), Machine-class columns stated as flat fact where the body says "not public",
plus a set of Medium items (dropped role labels/member lists, a duplicate equipment table on cmp, the
intro sentence appearing on-page three times, implant's table failing the phone test, hand-picked
consumable/tool-class subsets in the quick-facts rows, two caption/connective wording slips) and several
Low items. All High and Medium items are fixed, each in its own commit, verified with
`tools/check_preserved.py --base c79af95b --allow-regrouped` plus a precise `--allow-added` list (no
LOST anything on any of the ten pages after the fixes) and the full checker suite. Most Low items were
also fixed opportunistically (substrate/cmp's dropped ", so"; ONO's missing LPCVD furnace class; strip's
unlinked Water/Hardware and verbless paragraph; anneal's repeated R-LIST labels) where the fix was a
one-line change; link-text consistency across pages (A6) was left alone as a follow-on since it changes
no fact and the review marked it Low.

**Rulings accepted and applied:**
* D1 (caption digits/claims): every table caption added or touched in this round carries no digit and
  states no fact the page does not already give — confirmed by rereading each one after the fix
  (deposition's thickness caption now uses the PDK's own "uses for antenna-ratio calculations" wording;
  lithography's ITRS caption now reads "The ITRS figures listed in the sentence above, one per row").
* D2 ("Typical chemistry" as an ADDED hedge): kept the R-COMPARE column name as prescribed; the
  declaration in etch's write-up already matched the ruling (declare, don't rename) before this round.
* Every steps table now carries a caption clause: `Machine class is the class each step page's "Machines
  typically used" section names (see the machines index), not a published SkyWater assignment`;
  lithography's also adds "which mask runs on which tool is not public", and oxidation's explains "A, B".

**For the tool branch** (not actioned here — `check_preserved.py` is a checker, and rule 15/rd-common
forbid touching it from a content worktree): the reviewer recommends adding `roughly`, `of order`, `of
the order of`, `typically`, `usually` and `likely` to `check_preserved.py`'s `HEDGES` list. With `of
order` listed, the tool would have caught implant's two silent losses in the original pass by itself.

**Correction:** the earlier "191 rows total... expected double-counting" line above is wrong; the
per-page row counts sum to 171, one row per step in the flow, with no double-counting. Fixed in place.

## Fix round (verify): tmp/reviews/rd-categories-verify.md, 2026-09-26

Verifier's "needs another round, short": all High items from the first fix round confirmed. Three
Medium items still failed (M5 test intro triplication, M7 implant 400 px wrap, M9 consumable-classes
against the materials-index set) plus one new undeclared `ADDED numbers: '1–5'` on etch, introduced by
the first fix round's own restoring of the "metal 1–5" table label. Each fixed in its own commit:

1. **test.md** — the body sentence at :24 still carried the intro's second sentence in expanded form
   ("This is the e-test or wafer acceptance test (WAT); it is the single HPETEST step…"). Trimmed to
   keep only the HPETEST clause, so `e-test`/`WAT` appear once, on the first screen.
2. **implant.md** — the Wells and Threshold-adjust rows' "10¹²–10¹³" ranges wrapped mid-number at
   400 px. Fixed with a word joiner (U+2060) after the en dash in both cells; `check_preserved.py`
   is unaffected (the dash carries no token of its own) and the digit sequence still regroups
   identically. Re-shot at `--width 400`: confirmed one line.
3. **implant.md** — added `Hardware consumables` to the quick-facts Consumable classes row (the page
   already links `material-hardware-consumables` under "Typical consumables"). The guide's §4.5 now
   states the rule explicitly: Tool/Consumable classes are the classes the page itself already links,
   page-derived, no new facts — not a set derived from the machines/materials index.
4. **etch.md:137** — restoring "metal 1–5" into the R-COMPARE table's Steps cell (first fix round)
   duplicated the "For metal 1–5, a 2013 Cypress report…" prose lead-in added earlier in the same
   round to keep the base's contiguous digit run (`1–5, 2013, 1–3, 2014, 130`) together. Tried the
   verifier's suggested fix (drop "For metal 1–5, " from the prose) first: this reintroduces a hard
   `LOST number_order` for that run, because the table's "1–5" is now many rows away from "2013" with
   other rows' numbers in between — worse than the undeclared ADDED it was meant to fix. Reverted that
   and instead declared the repeated range: `--allow-added numbers` on etch.md, with the reason "1–5
   is a second, page-adjacent copy of a range already in the base, needed opposite ends of the same
   table/prose split to satisfy the contiguous-run check at each end; not a new fact." Confirmed
   `check_preserved.py --base c79af95b --allow-regrouped --allow-added markers,numbers,quotes,refs,
   hedges,identifiers` → 0 undeclared differences, same declared-addition set as before plus `1–5`.

**Note for the owner (not actioned as edits) — consumable-classes, materials-index cross-check.** The
verifier also built, for etch/deposition/oxidation/strip/test, the union of consumable classes the
*materials index* assigns to each category's steps, and compared it against each page's quick-facts
cell (which lists only the classes the page's own body already links, per the rule above). Under the
"page links" rule all five pages are consistent by construction; under an "every class the materials
index assigns" rule they would gain rows. For the owner to decide, not applied here:

| Page | Quick facts (page-derived) | Classes the materials index adds for this category's steps |
|---|---|---|
| etch | etch-gases, wet-chemicals, hardware | process-gases (N₂ 27/27, O₂, Ar, He, H₂O); ultrapure-water (20/27); anneal-ambients (forming gas 16/27); substrates (test wafers 22/27); lithography-materials (ARC, step 36) |
| deposition | 6 classes | substrates (test wafers 40/41); wet-chemicals (HF, step 3) |
| oxidation | process-gases, hardware, substrates | precursors (NH₃ on 10/40/47; DCS on 40); wet-chemicals (HF, BOE, SC-1/SC-2 pre-cleans on 2/10/43) |
| strip | process-gases, wet-chemicals, UPW, hardware | etch-gases (CF₄, 14/15); anneal-ambients (forming gas, 14/15); precursors (NH₃, 3/15) |
| test | hardware, substrates | none: exact match |

Strip's own "Gases" bullet already names CF₄ and forming gas on the page, so strip is the case where the
two candidate rules give different answers even on the page's own evidence — worth the owner's attention
first if the rule is revisited.
