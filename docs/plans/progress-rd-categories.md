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

(one row added as each page is committed)
