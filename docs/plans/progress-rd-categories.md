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

## Pages (index)

- cmp.md — done
- substrate.md — done
- anneal.md — done
- oxidation.md — done
- test.md — done
- strip.md — done
- implant.md — done
- (remaining three to do: deposition, etch, lithography)

## Pages

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

