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
- (remaining seven to do: deposition, etch, implant, lithography, oxidation, strip, test)

## Pages

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

