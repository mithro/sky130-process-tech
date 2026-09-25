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

## Pages

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

