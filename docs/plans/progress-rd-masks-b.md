# Progress — `topic/rd-masks-b` (W3 masks, pages 19–36)

Readability pass over the remaining eighteen mask pages in file-name order
(`ls docs/masks/*.md | grep -v index | tail -18`): nsdm, nsm, ntm, nwm, onom, p1m, pdm, psdm, pwbm,
pwdem, rpm, rrpm, tunm, urpm, vim, vim2, vim3, vim4. Rules per `docs/plans/readability-guide.md` §4.4,
in its order: R-INTRO → R-PARAMS → R-CAPTION → prose rules (R-PARA, R-SENTENCE, R-LIST, R-REPEAT,
R-CODE) → R-RELATED → R-H3, with the rulings of the first mask batch (canonical H3 order, `**Steps.**`
label, three-column R-PARAMS where a cell runs past five lines at 400 px, "Resist and tone"). Model pages:
`fom.md`, `lvtnm.md`, `lvom.md`. Base for every page: `f629785e` (main when the branch was cut).

## Method, the same on every page

* **Baseline.** Desktop and 400 px tiles of every page from a build of the base, before any edit.
* **Preservation.** `uv run python tools/check_preserved.py --base f629785e --allow-regrouped <page>`;
  every ADDED item is read and listed per page below with the rule that adds it. Never
  `--allow-dropdown-edits`.
* **Marker coverage.** `tmp/readability/markcov.py f629785e <page>` (git-ignored scratch script, the
  same one the step batches use): pairs every changed sentence with its base sentence and flags a lost
  marker or hedge phrase. Every flag is read; the per-page entry says which were real.
* **Checkers.** check_masks, check_refs, check_inforce, gen_index_links --check, gen_figures --check,
  `-W` build; tiles at desktop and 400 px after the edit.
* **Measurement.** `measure5.py` (copied to `tmp/readability/a-tools/`) at the §1 caps: paragraph > 100
  words, list item > 60, sentence > 45, cell > 25.

## Decisions (same on every page, as on the first batch)

* **Intro (R-INTRO).** The intro keeps the first sentences that say what the mask is and what it does,
  ≤ 70 words, split at the first sentence's colon. The pointer sentence ("How the step is performed is
  on the step page; every mask is indexed on the masks index.") moves word for word into a `{seealso}`
  under the quick facts. The template sentence ("This page gathers what public sources say about the
  mask itself — its PDK entry and layers, the plates the process-steps sheet records for the MPW runs,
  what the public renders of those runs show, the lithography it needs and the rules that constrain
  it.") is deleted; it carries no fact, hedge or marker, and it is the cause of `LOST hedges: 'about'`
  (its preposition) on every page. Everything else moves, unchanged apart from "it" → "the mask", to
  the top of `## What the mask defines`, with the step page's reading hedge repeated where the moved
  part was under it.
* **H3s.** Every bold run-in under `## Lithography and pattern transfer` becomes an H3 with its own
  words, except the synonyms the checker names (`Resist` → `Resist and tone`, `Overlay`/`Alignment` →
  `Overlay and alignment`). Canonical H3s stand in canonical order; a passage that has to move to meet
  it moves whole, unchanged, inside the H2 (recorded per page). Run-ins under other H2s stay bold.
* **Lists (R-LIST).** A marker at the end of an enumerating sentence goes on the lead-in. Items that are
  fragments take no invented label; a trailing "and" before the last item and a trailing semicolon are
  dropped.
* **Split sentences.** A marker or a hedge that covered the whole sentence is repeated on each piece
  that carries its claim; a marker that belonged to one clause stays with that clause.
* **After a list,** a sentence that began "It" (meaning the source) begins "The page" / "The table".
* **Related pages.** `**Steps.**` · `**Category.**` · `**Machines.**` · `**Materials.**` · `**Masks.**` ·
  `**Indexes.**`; links, link text and glosses unchanged.
* **Captions.** Every table except the quick facts and the checker-read plate table gets a one-line
  `:::{table}` caption, no `:widths:`.
* **R-PARAMS.** `Parameter | PDK table | Published description | Value`; where a description cell runs
  past five lines at 400 px, `Parameter (table) | Published description | Value`. Value left-aligned
  when a cell holds prose. The page's interpretation stays as prose after the table.

## Guide problems

(none yet)

## Pages

### 1. nsdm — done

* **Rules applied.** R-INTRO (intro 208 → 40 words); R-PARAMS; R-CAPTION (rule table, parameter
  table); R-PARA, R-SENTENCE; R-LIST (the device-page regions, the Table F2b `C` rows, the core checks
  of the Error Messages page, the per-die counts — markers on the lead-ins); R-RELATED; R-H3 (Exposure
  class, Mask errors, Resist and tone, Resist edges, Overlay and alignment, Pattern transfer).
* **Moved passage (canonical order):** "**Overlay.** The NSDM page reads the mask as aligned …" followed
  "**Pattern transfer.**"; it now sits, unchanged, under `### Overlay and alignment` before
  `### Pattern transfer`. Neither passage refers to the other by position.
* **Intro.** Kept: the first sentence up to its colon, and "On the NSDM page's reading, the resist
  printed through it at step 85 is opened over every region drawn in `nsdm`." The dash list of regions
  became its own sentence at the top of `## What the mask defines` ("On the NSDM page's reading, the
  regions drawn in `nsdm` are …"), followed by "On the NSDM page's reading, the implant NSDI passes …",
  the hedge repeated because the base sentence carried it over both. "It is the second of the two …" →
  "The mask is the second …".
* **R-PARAMS.** Ten parameters from Tables 2, 7, 3b, 3d and 3e. Three columns, because the `NPNWLU`
  description ran to seven lines at 400 px with four. "matching nsd.10a and nsd.11" went into the two
  Table 7 Value cells ("0.265, matching nsd.10a", "0.265, matching nsd.11"); `JCTD` / `LD` for the
  "N+ or P+ S/D (XJ)" row are the page's own names for that row (Pattern transfer). The base's "in its
  column headed "CD"" and "describe the junction the implant forms" stay as prose after the table
  ("Table 7 gives its two areas in its column headed "CD", and the Table 3b rows describe the junction
  the implant forms.[^pdk-03]").
* **Declared additions** (`--allow-added markers,numbers,refs,hedges`):
  * markers — `mask-renders` (render sentence split at its semicolon), `pdk-03` (the resist-thickness
    sentence split before "argues"; the base marker ended the whole sentence, so both pieces keep it),
    `pdk-errors` ×2 (Error Messages sentence as on fom; the nsd.9/rpm.6 sentence split from the x.9 list),
    `pdk-periph` (the nsd.8 / rpm.6 sentence split at its semicolon), `pdk-summary` (Table F3a sentence
    split at "and, in its diff and tap columns"), `steps-sheet` (Plate number, split before "So");
  * numbers — `2`, `3` ×4, `7` ×2 (the parameter table's table numbers and the sentence after it),
    `250` ("It is lower" → "`250` is lower", the continuation paragraph's pronoun given its noun back);
  * refs — `step-085` (the NSDM page's reading hedge repeated at the top of the body; the second
    "refs" line is the tool pairing backticks across the role and the next code span);
  * hedge — `our reading` ("(our reading of the columns)" repeated on the first half of the Table F3a
    sentence).
* **LOST lines that are not losses (read by hand):** `number_order` ('2', '0.38', '0.38', '7', '0.265',
  … '0.05') and ('3', '0.23', '0.15', '3', '0.23') are the R-PARAMS table: values in row order 0.38,
  0.38, 0.265, 0.265, 0.1 / 0.06, 0.007, 0.05, 0.23, 0.15, 0.23 — the base order — each with the base's
  table number. Every other number_order line is REGROUPED (list items and split sentences).
* **Marker coverage.** 20 flags read: the list items and lead-ins (R-LIST 1), clauses that had no marker
  of their own in the base, and splitter artefacts ("Rubin et al." ends a "sentence" for the script).
  The pdk-07 / pdk-08 pair at the end of the device-pages sentence was split by clause: `pdk-07`
  (*Device Details*) on the list of regions, `pdk-08` (*Parasitic Layout Extraction*) on the sheet
  resistance.
* **Other edits.** "rpm.6 as …, and lists" → "rpm.6 as … . The page lists" and "and Lukaszek … . Lee
  et al. and Horsky treated resist outgassing" (the gapped study list split in two, the verb restored);
  "the PDK does not state their purpose" → "the values' purpose" (the pronoun's noun back after the
  semicolon split).
* **Over the caps after the pass:** "It lists "NSDMdrop …" / "The page lists …" (46 by the script,
  which counts the four quotations word by word); the Exposure-class sentence (46, the formula counted
  as several words); the quick-facts Polarity cell (41; mask quick facts are left alone, R-QUICKFACTS 4). Before →
  after: paragraphs 10 → 0, items 1 → 0, sentences 21 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.
