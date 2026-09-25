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

### 2. nsm — done (page with two in-force notes)

* **Rules applied.** R-INTRO (194 → 56 words); R-PARAMS (three columns); R-CAPTION (rule table,
  parameter table); R-PARA, R-SENTENCE; R-LIST (the `nsm` rules under "The rules place the layer:", the
  general seal-ring rules — markers on the lead-ins); R-RELATED; R-H3 (Exposure class, The plate,
  Resist and tone, Overlay and alignment, Pattern transfer).
* **In-force notes.** Both `{dropdown}` blocks byte-identical (checked with a diff of the fenced blocks
  against the base). The paragraph carrying the pointer ("… in the collapsed note below this paragraph")
  still sits directly above its note: the 230-word paragraph was split *before* the pointer sentence,
  and the pointer sentence ("The step pages compare the construction with a Siemens and IBM patent …,
  and with a GlobalFoundries patent that may still be in force, …") was split at its comma, the second
  half given its subject back ("The step pages compare the construction with a GlobalFoundries patent
  …") and opening the last paragraph before the note. Nothing crossed a fence.
* **Moved passage (canonical order):** "**Overlay.** The 1.000 µm keep-out of nsm.3 is …" moved, unchanged,
  above "Pattern transfer" as `### Overlay and alignment`. Neither refers to the other by position.
* **Intro.** Kept the first sentence up to its colon and "On the NSM page's reading, the resist … along
  the edge of every die." The rest moved to the top of the body with the hedge repeated ("On the NSM
  page's reading, the NSME etch cuts the dielectric in the ring, and …"): "there" → "in the ring", the
  pro-adverb given its noun back, because its antecedent is now above the quick facts.
* **R-PARAMS.** Six parameters (Tables 2, 7, 4). Descriptions of `NSMKeepout` and `NSMKeepout_3um` are
  the page's own quotations of them in `## What the mask defines` (two ADDED quotes, shown by the tool
  as `ADDED identifiers: 'TCS-2253'×2`); "in its column headed "space"/"CD"" and "in its "Minimum Space
  and Overlap" block, headed "Value (um)"" stay with their rows. Three columns from the start: the
  `TBOWINGSEAL` description would pass five lines at 400 px with four.
* **Declared additions** (`--allow-added markers,numbers,refs,hedges,quotes,identifiers`):
  * markers — `caravel-sealring` (the GDS-reading sentence split at ", and the square"; "(our reading of
    the GDS file)" repeated with it), `mask-renders` (render sentence), `pdk-errors` ×2 (the Error
    Messages "describes" sentence; the `NSMmk` sentence split from the x.12a/x.28 one — `pdk-periph`
    stays with "which the periphery rules give as "N/A"");
  * numbers — `2` ×2, `3`, `4`, `7` ×3: table numbers in the parameter table and its lead-in;
  * refs — `step-165` (hedge repeated at the top of the body);
  * hedge — `our reading` ("(our reading of the GDS file)" repeated);
  * "(inferences on those pages)" repeated twice more (not a tracked hedge): the base sentence ran from
    the NSM page's reading of the ring to the NSME page's two depth readings under one closing hedge;
    it is now three sentences, each ending with it;
  * quotes — the LOST/ADDED quote pairs `'(x.23e); the'` → `'(x.23e) * the'`, `'(x.26); and'` → `'(x.26) *'`
    and the table rows are the tool re-pairing quotation marks around the nested `""advSeal_6um"`
    quotation and the table cells; read by hand, no quotation changed.
* **LOST lines that are not losses:** `number_order` ('2', '3', '4', '7', '1', '3', '50', '4', '0.015') is
  the parameter table: values 3, 4, 1, 3, 50, 0.015 in the base order with the base's table numbers.
* **Marker coverage.** Flags read: list items under lead-in markers, clauses with no marker of their own
  in the base (the "So `cnsm` shapes …" reading, "It names a mask-data layer …" without `pdk-periph`,
  the ALTA sentence, "At 365 nm …" after the Wong split).
* **Other edits.** "It also checks" → "The page also checks" (paragraph after a split); "From the rules
  and that layout it reads" → "… the page reads" (new paragraph); "and the purpose of the opening as"
  → ". It reads the purpose of the opening as" (subject and verb added at the split).
* **Over the caps after the pass:** three sentences the script over-counts (the Table 7 keep-out
  sentence and "It repeats nsm.1 and nsm.2 …", mostly quotations; the Exposure-class formula); five
  quoted rule-table cells and the quick-facts Polarity cell. Before → after: paragraphs 10 → 0, items
  1 → 0, sentences 16 → 3, cells 6 → 6.
* **Content problems for the owner:** none found.

### 3. ntm — done

* **Rules applied.** R-INTRO (201 → 38 words); R-PARAMS; R-CAPTION (rule table, parameter table);
  R-PARA, R-SENTENCE; R-LIST (the Table 3b/3f criteria, the Table F2b `C` rows — markers on the
  lead-ins); R-RELATED (TIPRTAD, which the base's mask bullet named as a second relationship, now
  under **Steps.**); R-H3 (Exposure class, Mask errors, Resist and tone, Resist edges and shadowing,
  Overlay and alignment, Pattern transfer).
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer". The
  overlay passage names "the shadowing allowances" but not by position.
* **Intro.** Kept the first sentence up to its colon and "On the NTM page's reading, the resist … is
  opened over the 1.8 V NMOS transistors." Moved with the hedge repeated: "On the NTM page's reading,
  the arsenic tip ASTI and the boron halo BHI pass through the same openings, …"; "It is the first of
  three tip masks" → "The mask is …"; "What sets it apart is that no designer draws it:" split at its
  colon (the "on our reading" hedge stays in the second half, which it qualifies).
* **R-PARAMS.** The paragraph's "other criteria that name the mask or its implant" became a five-row
  table under the lead-in "The other criteria that name the mask or its implant are these:[^pdk-03]"
  (caption "Other parameters of *Criteria & Assumptions* that name the mask or its implant"). `TipAng`,
  `ntmShadowing`, `minTip_impW` and `pseudoShadowing` are the page's own names for those rows (What the
  mask defines, Resist edges and shadowing); the paragraph gave only the descriptions. The Table 2 pair
  stays in prose (it carries the comparison with nwell.1 and hvi.2a/hvi.5), and so does "Table 4 also
  lists …" (three entries the page does not class as naming the mask, with the `masks.csv` remark and
  its `pdk-05` marker).
* **Declared additions** (`--allow-added markers,numbers,refs`):
  * markers — `mask-renders` ×3 (the README sentence split at its colon; the per-die counts split at
    their semicolons), `pdk-03` ×2 (the resist-thickness sentence split at its semicolon, both halves
    quoting the PDK; the parameter-table lead-in), `pdk-06` ×2 (the `masks.csv`/`gds_layers.csv`
    sentence split at its semicolon — the second half quotes `gds_layers.csv`; the second Open question
    split at its semicolon, its first half being the reading of Table F2b), `pdk-errors` (Error Messages
    "describes" sentence);
  * numbers — `4` ×2 (the parameter table's table column);
  * refs — `step-064` (hedge repeated at the top of the body).
* **LOST lines that are not losses:** `number_order` ('3', '0.01', '3', '7', '4', '0.16', '0.1', '0.045',
  '4', '0.3', '0.232', '0.089') is the parameter table plus the "Table 4 also lists" sentence: 0.01,
  7°, 0.16, 0.1, 0.045 in the base order with their tables, then 0.3, 0.232, 0.089 unchanged.
* **Marker coverage.** Flags read: list items under lead-in markers; clauses that had no marker of
  their own (the step page's `TipAng` reading, "The table does not say …", "At the NA 0.48 low end …"
  which keeps its own `asml-pas5500-275d`).
* **Other edits.** "It also has two `cntm.nikon` checks" → "The page also has …" (new paragraph); the
  dash pair "— on the step pages' readings the PMOS, the 5 V devices and the memory cells, none of which
  takes the standard tip —" became its own sentence after "… consistent with the Table F2b rows above"
  ("On the step pages' readings these are …", R-SENTENCE 1 and 7); ", puts them at" → "and puts them
  at" and ", quotes ASML's statement" → ". It quotes …" (Exposure class); "Codella and Ogura added the
  halo," → "and Codella and Ogura added the halo." and "Horsky resist outgassing …, and Ross et al." →
  "and Horsky … . Ross et al. …" (study lists split in two).
* **Over the caps after the pass:** two sentences the script over-counts (the `cntm.1`/`cntm.2` list and
  the `cntm.nikon` sentence, both mostly quotations); the quick-facts Polarity cell. Before → after:
  paragraphs 11 → 0, items 1 → 0, sentences 21 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 4. nwm — done

* **Rules applied.** R-INTRO (167 → 31 words); R-PARAMS (three columns); R-CAPTION (rule table,
  parameter table); R-PARA, R-SENTENCE; R-LIST (what the regions are for, the Table F2b `C` rows, the
  Table 7 serif/extension rows, the per-die counts, the two resist-thickness patents — markers on the
  lead-ins, the two patents as plain bullets with their own markers); R-RELATED; R-H3 (Exposure class,
  Mask errors, Resist and tone, Resist edges, Overlay and alignment, Pattern transfer).
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged apart from the split below, above
  "Pattern transfer". Neither refers to the other by position.
* **Intro.** Kept the first sentence up to its colon and "On the NWM page's reading, the thick resist
  … is opened over every future N-well." The dash list became "On the NWM page's reading, the future
  N-wells are the body of every PMOS, the ring … and the drift regions …" at the top of the body,
  followed by "On the NWM page's reading, three implants pass through the same openings, …" (the hedge
  covered the whole base sentence); "It is an implant block mask" → "The mask is …".
* **R-PARAMS.** Eight parameters (Tables 2, 3d, 3e, 4, 7, 8). The base's comparisons stay in their Value
  cells with the `pdk-periph` marker they rest on ("0.835 µm, below the 1.270 µm of nwell.2a",
  "2, the value of hvnwell.8"), as on lvtnm; "for photo diodes" is repeated on both Table 4 rows it
  covered. The lead-in keeps `pdk-03`.
* **Declared additions** (`--allow-added markers,numbers,refs`):
  * markers — `mask-renders` (render sentence split at its semicolon), `pdk-errors` (Error Messages
    "describes" sentence), `pdk-periph` (the base's one `pdk-periph` at the end of the Criteria
    sentence now sits on the two Value cells that compare with periphery rules), `steps-sheet` (Plate
    number split at its semicolon);
  * numbers — `2`, `4`: the table column ("Table 2" twice, "Table 4" twice where the base named each
    table once);
  * refs — `step-017` ×2 (the NWM page's reading hedge, twice at the top of the body).
* **LOST lines that are not losses:** `number_order` ('2', '0.84', '1.27', '3', '0.835', …, '8', '2', '8')
  is the parameter table: values 0.84, 1.27, 0.835, 0.04, 0.84, 1.08, 0.22, 2 in the base order, each
  with its base table number and comparison.
* **Marker coverage.** Flags read: list items under lead-in markers; the three-way "So the PDK names a
  rule `cnwm.3f` …, but …; the Error Messages page …,[^pdk-errors] and the serif and extension rows …"
  split into three sentences, each keeping its own marker (the serif sentence had none in the base);
  "On no run do more than nine dies …" (no marker in the base); "ASML specifies …" (see below).
* **Other edits.** Overlay: "…(difftap.9),[^pdk-periph] against the "≤ 40 nm" single-machine overlay
  ASML specifies for the /275D stepper[^asml-pas5500-275d] (our comparison; …)" → "…(difftap.9).[^pdk-periph]
  ASML specifies the "≤ 40 nm" single-machine overlay for the /275D stepper[^asml-pas5500-275d] (our
  comparison; …)" — the word "against" goes; "(our comparison)" still marks the two as compared, as the
  sibling pages (nsdm, ntm) write the same comparison. Renders: "Counts rarely repeat — on no run … —
  so we read …" → "Counts rarely repeat. On no run … . So we read …". Steps section: "The one point
  that needs stating is LVTPI:" split at its colon only; the rest of the sentence (51 by the script)
  keeps its dash pair, because moving the IBM-patent clause out would detach it from "the step pages
  read it as using the `NWM` resist" or attach it to "no public document says so".
* **Over the caps after the pass:** five sentences the script over-counts because of quotations (the
  two Table C3 sentences, the Hook quotation, the Table 3b/3e overlay sentence, the Table 3a/3b
  "result" sentence) and the Steps-section sentence above; the quick-facts Polarity cell. Before →
  after: paragraphs 10 → 0, items 0 → 0, sentences 22 → 6, cells 1 → 1.
* **Content problems for the owner:** none found.

### 5. onom — done (page with four in-force notes)

* **Rules applied.** R-INTRO (171 → 50 words); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST (the
  Cypress stack figures, the Table F2b marks, the generic Error Messages checks — markers on the
  lead-ins); R-RELATED; R-H3 (Exposure class, Resist and tone, Overlay and alignment, Pattern
  transfer).
* **R-PARAMS not applied:** the design-rules paragraph names two parameters (`ONOMCD`, `ONOMCDSP`).
* **In-force notes.** All four `{dropdown}` blocks byte-identical (diff of the fenced blocks against the
  base). Each of the three in the body still follows the paragraph whose pointer sentence ("… in the
  collapsed note below this paragraph") names it: the island paragraph was split before "Cypress's
  integration patent …", the pattern-transfer paragraph before "The Cypress integration patent …", so
  the pointer and the sentence after it stay in the last paragraph above each note; the resist pointer
  was split from the sentence before it at its semicolon only. No heading, table or figure sits between
  a pointer paragraph and its note.
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer": it now
  follows the resist note and precedes the pattern-transfer paragraphs and their note. The
  pattern-transfer passage's "(above)" points at the first note, in `## What the mask defines`, which is
  still above it.
* **Intro.** Kept the first sentence up to its colon and the whole reading ("On the ONOM page's
  reading, the resist … before the logic gate oxides are grown.", 38 words). "The PDK lists the mask
  …" and "Like the tunnel mask, it has a plate recorded …" moved unchanged to the top of the body.
* **Declared additions** (`--allow-added markers,numbers`): markers `mask-renders` (render sentence),
  `pdk-errors` (Error Messages "describes"), `pdk-06` (first Open question split at its semicolon; its
  first half names the `conom` drawing purpose 87:44 of `gds_layers.csv`); numbers `15`, `3` (x.15a and
  tunm.3 in the rule-table caption, copied from the lead-in).
* **Marker coverage.** Flags read: list items under lead-in markers, "The site gives no source for
  either statement." and "So a design inside the die …" (no marker of their own in the base), the
  second "On the step pages' readings …" sentence (the hedge repeated; "(inference on the step page)"
  stays with the island clause it closed).
* **Over the caps after the pass:** "We read the identical columns as consistent …" (47; its closing
  12-word parenthetical is the hedge, and a split would separate "since the table gives …" from what it
  supports); the first sentence of the "Plates on runs with no drawn `tunm`" bullet (46, six run names
  counted as words); two quick-facts cells. Before → after: paragraphs 10 → 0, items 1 → 0, sentences
  14 → 2, cells 2 → 2.
* **Content problem for the owner (not changed):** outside the collapsed notes, the base already
  paraphrases their content — "says the same of its own flow", "describes the same combination and
  notes what the wet step does to the masked region", "The undercut it describes shrinks the island's
  overlap of the window, which is why the patent calls the dimensions and alignment of the two
  important (above)". `check_inforce.py` passes (no number, title or listed phrase), but §2.5 forbids
  paraphrasing a collapsed note outside it. Left word for word; the owner may want those sentences
  looked at.
