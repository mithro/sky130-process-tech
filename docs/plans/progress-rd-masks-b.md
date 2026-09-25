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

* **G1 (p1m).** R-PARAMS assumes a paragraph of parameter/value pairs. The p1m paragraph also qualifies
  its rows per table — "which the table does not explain" (Table 2's second "Poly 1" row), "neither row
  has a unit or says what the value applies to" (the two Table 7 rows), Table 7's own title — and a
  four-column table has no cell for those clauses without new wording. The paragraph became a
  three-item list by table (bold `Table N` labels, every word and marker kept) instead. If the owner
  wants the table, the clauses need a `Note` column, which breaks the §1 column budget.

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

### 6. p1m — done

* **Rules applied.** R-INTRO (153 → 57 words; the whole reading sentence, dash list included, stays in the
  intro at 40 words); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST (the three kinds of feature,
  the Table F2b `C` rows, "Two things the mask does not define", "Two rules show …", the
  *Criteria & Assumptions* rows by table); R-RELATED; R-H3 (Exposure class, Mask errors, Proximity and
  line ends, Resist and tone, Overlay and alignment, Pattern transfer).
* **R-PARAMS** applied as a list by table, not a table: see guide problem G1.
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged apart from its semicolon split,
  above "Pattern transfer".
* **Intro.** "Because the etched poly width is the transistor gate length, this is the mask …" moved
  unchanged to the top of the body.
* **"Two things the mask does not define".** The base's closing ", on the step pages' readings" covered
  both clauses of the sentence; as a two-item list, each item ends with it.
* **Declared additions** (`--allow-added markers,numbers`): marker `mask-renders` (render sentence split
  at its semicolon); numbers `1` ×2, `2`, `7`, `8` (x.1a, x.1b, x.2, poly.7 and poly.8 in the rule-table
  caption, copied from the lead-in).
* **Marker coverage.** Flags read: list items under lead-in markers; "So the PDK assumes tighter bias
  control …" (no marker in the base; its premise keeps `pdk-03`); "On the step pages' readings the tip
  and halo implants …" (the `pdk-periph` marker belonged to the rule values before the semicolon);
  Kuijten / Arthur split at ", and", each with its own marker.
* **Wording at splits.** "The rows it leaves unmarked" → "The rows the table leaves unmarked" (after a
  list); the *Criteria & Assumptions* list opens "The tables of *Criteria & Assumptions* give, table by
  table:" (the base's "Table 2 of *Criteria & Assumptions* gives" spread over three bold labels).
* **Over the caps after the pass:** the x.1a quotation sentence (49 by the script, one quotation) and
  the Wong sentence (50; its marker sits at the end of the following "They also found …" sentence, and
  a split at the semicolon would put the arithmetic between Wong's two findings and their shared
  marker); the quoted x.1a rule cell. Before → after: paragraphs 9 → 0, items 0 → 0, sentences 9 → 2,
  cells 1 → 1.
* **Content problems for the owner:** none found.

### 7. pdm — done (page with two in-force notes)

* **Rules applied.** R-INTRO (207 → 53 words); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST
  (the `gds_layers.csv` layers beside `pad`, the Error Messages pad checks, the e-test pad checks, the
  Table 9 "CD" criteria — markers on the lead-ins); R-RELATED; R-H3 (Exposure class, The plate and its
  tolerance, Resist and tone, Overlay and alignment, Pattern transfer). The bold run-ins under
  `## What the mask defines` (Test pads and the scribe, Polyimide …, Fuses, Variants) stay bold.
* **R-PARAMS not applied:** the design-rules paragraph gives values for three parameters (`PDMCD`,
  `PDMCDSP`, `PdmCD_tol`) and names two more without values; the Table 9 criteria sit in
  `## What the mask defines` and became a list there.
* **In-force notes.** Both byte-identical (diff against the base). The scribe paragraph was split so
  that its last paragraph ("Lee found … A TSMC patent that may still be in force is cited here too, in
  the collapsed note below this paragraph.") is still the one directly above the note.
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer".
* **Intro.** Kept the first sentence up to its colon and the whole reading (43 words). The `masks.csv`
  sentence (split at ", and the process-steps sheet") and "The features are large — … —" (its dash pair
  became a colon and a full stop) moved to the top of the body.
* **Error Messages list.** The base sentence ran "It requires …; it gives a bond pad chamfered corners
  — … — a "150.0um Max Width/Length …" …; and it words pad.3 as …". The items keep their own "it
  requires / it gives / it words"; the second "it gives" item repeats the verb for the size checks that
  followed the dash pair.
* **Declared additions** (`--allow-added markers,numbers,hedges`): markers `caravel-sealring` and hedge
  `our reading` (the sub-cell sentence's dash clause "— the opposite form from the cross it draws on
  `cnsm` … —" became "That is the opposite form …", the hedge and marker repeated), `mask-renders` ×3
  (render sentence; the per-die counts split at their semicolons), `pdk-03` ×2 (Table 9 "space" and Table
  7 sentences), `pdk-06` (the Table C3 / `gds_layers.csv` sentence split), `pdk-errors` ×2 (Error
  Messages "describes"; `PDMmk` / "It also checks" split); number `9` ("In its column headed "space"
  Table 9 gives", the pronoun after the list given its noun back).
* **LOST lines that are not losses:** `number_order` ('9', '0.5', '4.5', '7.5', '87', '0', '0.5',
  '19.16', '10', '7', '0') is the Table 9 list with the repeated "Table 9"; same values, same order.
* **Wording at splits.** "; scribe.21, which keeps …" → ". Rule scribe.21, which keeps …" (a rule id is
  not capitalised); "It also notes that this is the only mask printed after the passivation nitride" →
  "The page also notes …" (after the dark-field sentence split off).
* **Over the caps after the pass:** four sentences the script over-counts (the Table F4 and WLCSP
  sentences, mostly quotations; the sub-cell sentence at 49 with its numbers; the Exposure-class formula)
  and the second Open question (50, its three markers cover the renders note and the unpublished
  operation together, so it was not split); the quick-facts Polarity cell and the quoted x.9 cell.
  Before → after: paragraphs 12 → 0, items 1 → 0, sentences 24 → 5, cells 2 → 2.
* **Content problems for the owner:** none found.

### 8. psdm — done

The sibling of nsdm; the same treatment throughout.

* **Rules applied.** R-INTRO (211 → 40 words); R-PARAMS (three columns, eleven parameters: the
  `NPNWLU` description passes five lines at 400 px with four); R-CAPTION (rule table, parameter
  table); R-PARA, R-SENTENCE; R-LIST (device-page regions, the three Table C3 definitions, the Table F2b
  `C` rows, the core checks, the per-die counts); R-RELATED (RTAD, a second relationship in the base's
  mask bullet, under **Steps.**); R-H3 (Exposure class, Mask errors, Resist and tone, Resist edges,
  Overlay and alignment, Pattern transfer).
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer".
* **Intro.** As on nsdm: the regions dash list became "On the PSDM page's reading, the regions drawn in
  `psdm` are …", then "On the PSDM page's reading, the implants PSDI and 2PSDI pass …"; "It is the first
  of the two …" → "The mask is the first …".
* **R-PARAMS.** As on nsdm; "matching psd.10b and psd.11" in the two Table 7 Value cells; `JCTD` /
  `LD` from the page's Pattern transfer; "in its column headed "CD"" and "describe the junction the
  implant forms" in the sentence after the table.
* **Declared additions** (`--allow-added markers,numbers,refs,hedges`): markers `mask-renders` ×2
  (render sentence; the `PSDI` render sentence split at its semicolon), `pdk-03` (resist-thickness
  sentence split before "argues"), `pdk-errors` ×2 (Error Messages "describes"; the psd.9/licon.9
  sentence split from the x.9 list), `pdk-summary` (Table F3a split); numbers `2`, `3` ×5, `7` ×2
  (parameter-table table numbers and the sentence after it); refs `step-081` (hedge repeated; the
  second refs line is the backtick-pairing artefact); hedge `our reading` (Table F3a).
* **Marker moves by clause.** The device-pages sentence's `[^pdk-07][^pdk-08]` split as on nsdm; the first
  Open question's `[^pdk-06][^pdk-03][^mask-renders]` split at its semicolon: `pdk-06` (the `cpsdm`
  purposes) on the first half, `pdk-03` (Table 7) and `mask-renders` (the note) on the second.
* **LOST lines that are not losses:** the two `number_order` lines are the parameter table, values in
  the base order with the base's table numbers.
* **Marker coverage.** Flags read: all list items or clauses with no marker of their own in the base.
* **Other edits.** Resist edges: the dash pair "— Hook et al. measured …, Sheu et al. … and Drennan,
  Kniffin and Locascio …[^drennan-2006] —" became its own sentence in place, order kept; the gapped
  study list split in two with "treated" restored; Steps section: "The one point that needs stating is
  PSDI:" split at its colon, and the long sentence split before "the step pages read it as …", the two
  markers staying with the sheet and render facts they support.
* **Over the caps after the pass:** "The page lists "PSDMdrop …"" (47, quotations) and the
  Exposure-class formula sentence (49); the quick-facts Polarity cell. Before → after: paragraphs 12 →
  0, items 0 → 0, sentences 22 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 9. pwbm — done

* **Rules applied.** R-INTRO (190 → 54 words); R-PARAMS; R-CAPTION (rule table, parameter table);
  R-PARA, R-SENTENCE; R-LIST (the three signs of the thin record; the Table 3a/3b result); R-RELATED;
  R-H3 (Exposure class, Resist and tone, Resist edges, Overlay and alignment, Pattern transfer).
* **Template sentence with an extra clause.** This page's template sentence ends "— and reports the gaps
  without drawing conclusions from them". The listing part was deleted as on every page; the extra
  clause is kept, with its subject, as "This page reports the gaps without drawing conclusions from
  them." after the list it refers to (§7 step 4: "Any other clause in it is kept").
* **Intro.** Kept the first sentence up to its colon and "On the step pages' reading, the resist … remains
  over the N-wells and over the special 20 V regions drawn as `pwbm`." Moved with the hedge repeated:
  "On the step pages' reading, the boron well implants … go into all the silicon the resist leaves open
  …" ("it" → "the resist"); "It is the mask of this reference whose public record is thinnest …:" →
  "`PWBM` is the mask …:" followed by its three clauses as a list.
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer".
* **R-PARAMS.** Six parameters (Tables 2, 3d, 7) under "*Criteria & Assumptions* gives the
  following:[^pdk-03]"; the two Table 2 rows have no published description on the page, so the cell
  is `—`. The base's two `[^pdk-03]` became one on the lead-in (one source, as the fom ruling M4 did):
  `LOST markers: 'pdk-03'` ×1.
* **Error Messages sentence.** "The periphery rules give no values … ("N/A"),[^pdk-periph] but the PDK's
  Error Messages page, which describes "…", gives `pwbm.5` as … and `rpm.10` as …" → the relative
  clause became the next sentence ("The page describes "…".[^pdk-errors]") so that the "but" contrast
  stays in one sentence.
* **Declared additions** (`--allow-added markers,numbers,quotes,refs`): markers `pat-well-ibm` (the IBM
  sentence split before "uses a resist of the same thickness"), `mask-renders` ("No drawn shapes"
  split), `pdk-errors` (the "describes" sentence), `steps-sheet` ×2 ("Partial record" lead split off;
  "Plate number" split at its semicolon); numbers `2`, `3`, `7` (parameter-table column). The
  LOST/ADDED `quotes` and `refs` lines are the tool pairing quotation marks and backticks across the new
  table and across "{ref}`PWIS <step-029>`. `PWBM` is …"; read by hand, no quotation and no role changed.
* **LOST lines that are not losses:** `number_order` ('3', '0.05', '0.15', '7', '0.12', '1.2') is the
  parameter table (0.05 µm, 0.15 µm, 0.12, 1.2 in the base order, with the base's tables).
* **Marker coverage.** Flags read: each flagged sentence had no marker of its own in the base, or its
  marker sits on the list lead-in.
* **Other edits.** "Partial record" bullet: the lead sentence split at "and does not say why" ("The sheet
  does not say why …", marker repeated), and the continuation's colon → full stop ("… the other six
  runs. The gap may be in the record …", the parenthetical inference staying with that clause).
* **Over the caps after the pass:** the Table F2b sentence (46 by the script, "5/20" and the device
  list), "We read the match as consistent …" (46; its "though `PWDEM` …" clause qualifies the reading
  and cannot stand alone), the two-quotation "The site says …" sentence (52 by the script); three
  quick-facts cells. Before → after: paragraphs 9 → 0, items 1 → 0, sentences 15 → 3, cells 3 → 3.
* **Content problems for the owner:** none found.

### 10. pwdem — done

* **Rules applied.** R-INTRO (180 → 43 words); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST
  (the three signs of the sparse record; where the periphery rules put the layer); R-RELATED; R-H3
  (Exposure class, Resist and tone, Overlay and alignment, Pattern transfer).
* **R-PARAMS not applied:** two parameters (`PWDEMCD`, `PWDEMCDSP`).
* **Template sentence with an extra clause:** as on pwbm, "and reports the gaps without drawing
  conclusions from them" kept as "This page reports the gaps without drawing conclusions from them."
* **Intro.** Kept the first sentence up to its colon and "On the PWDEM page's reading, the resist …
  is opened over the `pwde` regions of the 20 V devices." Moved with the hedge repeated: "On the PWDEM
  page's reading, the two implants … put a lighter, purpose-built P-well into the `pwde` regions — …
  —" ("into them" → "into the `pwde` regions"); "Like `PWBM`, it is a mask …:" → "Like `PWBM`,
  `PWDEM` is a mask …:" with its three clauses as a list.
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer".
* **Declared additions** (`--allow-added markers,refs`): markers `mask-renders` ("No drawn shapes"
  split), `pdk-errors` (Error Messages "describes"), `steps-sheet` ("Partial record" lead split off);
  refs `step-030` (hedge repeated; the other refs lines are the backtick-pairing artefact around "Like
  `PWBM`, `PWDEM`").
* **Marker coverage.** Flags read: every flagged sentence had no marker of its own in the base (the
  marker belonged to the clause before its semicolon).
* **Other edits.** "has a long history:" → "has a long history." (the two studies that followed stay
  one sentence); "Partial record" and "No drawn shapes" split as on pwbm.
* **Over the caps after the pass:** the 20 V PMOS page sentence (47 by the script, a long quotation) and
  the two-quotation "The site says …" sentence (52); the quick-facts Polarity cell. Before → after:
  paragraphs 8 → 0, items 1 → 0, sentences 10 → 2, cells 1 → 1.
* **Content problems for the owner:** none found.

### 11. rpm — done

* **Rules applied.** R-INTRO (171 → 43 words); R-PARAMS (three columns: the `POLYRCD` description passes
  five lines at 400 px with four); R-CAPTION (rule table, parameter table, and the renders' per-run
  frame table); R-PARA, R-SENTENCE; R-LIST (the two precision-resistor devices, the step page's three
  inferences, the Table F2b marks); R-RELATED (the base's second bullet named steps and masks, so RRPM
  and URPM went under **Steps.** and their mask pages under **Masks.**); R-H3 (Exposure class, Resist
  and tone, Resist edges, Overlay and alignment, Pattern transfer).
* **Moved passage (canonical order), done the other way round.** The base order was Exposure, Resist,
  Pattern transfer, Resist edges, Overlay. Resist edges ends "(below)", which may point at the overlay
  passage that reads rpm.3 as the overlay budget; moving the overlay passage above it would falsify
  that. So the *pattern-transfer* passage moved, unchanged, to the end of the H2, below Resist edges and
  Overlay and alignment; it refers to no other passage by position.
* **Intro.** Kept the first sentence up to its colon and "On the RPM page's reading, the resist … stays as
  islands over the future precision-resistor bodies." Moved with the hedge repeated ("On the RPM page's
  reading, the heavy n-type gate implant P1I dopes …"); "It is the only one of the three resistor
  masks" → "The mask is …".
* **R-PARAMS.** Five parameters (Tables 2 and 4). "the values of poly.3 and poly.9" went into the two
  Value cells as "the value of poly.3" / "the value of poly.9", each with the `pdk-periph` marker the
  base put on the sentence; the shared description of `POLYRCD` and `POLYRSPC` is repeated on both rows
  (one ADDED quote). The base's two `[^pdk-03]` became one on the lead-in (`LOST markers: 'pdk-03'` ×1,
  one source, as on pwbm).
* **Declared additions** (`--allow-added markers,numbers,quotes,refs`): markers `mask-renders` (render
  sentence), `pdk-errors` ×3 (the "describes" sentence; the `urpm` sentence split twice at its
  semicolon and after "(our comparison)"), `pdk-periph` (the second Value cell), `steps-sheet` ("Plate
  number" split); numbers `2` ×2, `4` ×3 (table column), `3` and `15` (rpm.3 and x.15a in the rule-table
  caption), `39` (a tool artefact: the base line began "39.[^pdk-06]", which the tool's numbered-label
  masking skips; the list item now reads "in the other 39"); quote — the repeated description; refs
  `step-049` (hedge repeated).
* **LOST lines that are not losses:** the two `number_order` lines are the parameter table (1.27, 0.84,
  0.33, 0.48, 2.03 in the base order, with poly.3, poly.9 and "6 contacts" as in the base).
* **Marker coverage.** Flags read: every flagged sentence had no marker of its own in the base, or its
  marker sits on a list lead-in.
* **Other edits.** "It lists messages for rpm.3 …" → "The page lists …" (new paragraph); the
  `urpm.1a`… sentence split into three ("It has no message …", "Under the names … it lists …", "They sit
  …"); Overlay: "…infers alignment to the trench marks of FOM and reads the 0.200 µm enclosure …" →
  "… FOM. It reads the 0.200 µm enclosure …".
* **Over the caps after the pass:** "The page lists messages for rpm.3 …" (53 by the script, three
  quotations) and the resist sentence (49; its "with anti-reflective coating optional because …"
  clause is part of the step page's reading and has no subject of its own); three quick-facts cells.
  Before → after: paragraphs 11 → 0, items 0 → 0, sentences 15 → 2, cells 3 → 3.
* **Content problems for the owner:** none found.

### 12. rrpm — done

* **Rules applied.** R-INTRO (197 → 49 words); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST (the
  PDK tables that name no such mask; the three test-tile structures); R-RELATED; R-H3 (Exposure class,
  Resist and tone, Pattern transfer, Overlay with `RPM`).
* **No move needed.** The run-in "**Overlay with `RPM`.**" is not one of the checker's synonyms, so it
  keeps its own words (as cap2m's "Overlay and charging" did) and stays last; the canonical H3s present
  are already in order.
* **R-PARAMS not applied:** the design-rules paragraph gives the `RPM` pair only as the step page's
  borrowed geometry and three Table 4 values; the page names no parameter of this mask.
* **Template sentence with an extra clause:** as on pwbm, "and reports the gaps without drawing
  conclusions from them" kept as "This page reports the gaps without drawing conclusions from them."
* **Intro.** Kept the first sentence up to its colon and the reading up to "… that RPM protected."
  Moved with the hedge repeated ("On the RRPM page's reading, the p-type resistor implant PRI goes …");
  "The PDK's mask table does not list it and …; the process-steps sheet …; and the public mask-layer
  renders …" → two sentences, "it" → "`RRPM`" where the split separated it from its antecedent.
* **Test-tile list.** "it marks three — A, B, and C — "(will not work for any routes using RRPM mask)""
  → "it marks three "(will not work …)":" followed by the three structures as bullets; the quotation
  and the marker are unchanged, and the dash pair became the list.
* **Declared additions** (`--allow-added markers,numbers,refs`): markers `pdk-06` (the `gds_layers.csv`
  item of the "no such mask" list; the base's `pdk-06` after the Table F2b clause covered it, both being
  the *Layers Reference* source), `raw-data-passives` ("It notes that the files do not say which route
  …", split from the extraction sentence; `pdk-07` stays with the e-test table), `steps-sheet` (the
  "Run Mask IDs" sentence split at its semicolon; `pdk-05` stays with the `masks.csv` clause); number
  `3` (rpm.3 in the rule-table caption); refs `step-052` (hedge repeated).
* **Marker coverage.** Flags read: every flagged sentence had no marker of its own in the base (its
  marker belonged to the clause before the semicolon), or keeps the marker of its clause.
* **Kept whole.** "The RRPM page infers that `RPM` and `RRPM` both align … : a gap … and an overlap …"
  (54): the colon's clauses are the page's inference, and a split would need the inference repeated in
  new words.
* **Over the caps after the pass:** that sentence; "Both precision flavours are p-type films — … —"
  (47 by the script, mostly quotations); the Error Messages `urpm` sentence (54, three quotations);
  "On the step page's reading the `RRPM` data would come …" (46, eight counts); three quick-facts cells.
  Before → after: paragraphs 9 → 0, items 1 → 0, sentences 14 → 4, cells 3 → 3.
* **Content problems for the owner:** none found.

### 13. tunm — done (page with three in-force notes)

* **Rules applied.** R-INTRO (168 → 38 words); R-CAPTION (rule table); R-PARA, R-SENTENCE; R-LIST (the
  four more steps the openings serve; the placement rules, each item given "it" as subject; the Table
  F2b marks; what the mask does not define; the four uses of the pattern); R-RELATED (the ONO/ONOM step
  links under **Steps.**, the ONO mask page under **Masks.**, the base bullet naming both); R-H3
  (Exposure class, Mask errors, Resist and tone, Overlay and alignment, Pattern transfer, Resist edges).
* **In-force notes.** All three byte-identical (diff of the fenced blocks against the base). The
  exposure paragraph was split before "At the NA 0.48 low end …", so the pointer ("its sentence is in
  the collapsed note below this paragraph") is still in the paragraph directly above its note; the
  pattern-transfer pointer paragraph follows the new four-use list and still sits directly above its
  note.
* **Moved passage (canonical order):** "**Overlay.**" moved, unchanged, above "Pattern transfer" (not the
  other way round, so that no note moves); "Resist edges", a free extra, now follows the
  pattern-transfer note. No passage refers to another by position.
* **Intro.** Kept the first sentence up to its colon and the reading up to "… and nowhere else."
  Moved with the hedge repeated: "On the TUNM page's reading, the same openings serve four more
  steps:" and the dash list as bullets; "Its public record is lopsided" → "The mask's public record …"
  (after the list).
* **Declared additions** (`--allow-added markers,numbers,refs,hedges`): markers `mask-renders` (render
  sentence), `pdk-errors` (Error Messages "describes"), `steps-sheet` (Plate number: the dash pair became
  a colon and the sentence split before "The sheet does not say …"); numbers `3`, `15` (tunm.3, x.15a in
  the rule-table caption); refs `step-035` (hedge repeated); hedge `our reading` ("(our reading of the
  rows; the table does not explain its marks)" repeated when "which we take to be the cell's pass
  transistor …" became "We take those rows to be …"). `LOST markers: 'pdk-06'` ×1: the two `[^pdk-06]` of
  the Table F2b sentences became one on the list lead-in (one source). The placement-rules sentence's
  `[^pdk-periph][^pdk-06]` split by clause: `pdk-periph` on the lead-in, `pdk-06` on the `areaid.ce`
  item, whose description ("Memory (SRAM) core cell identifier") is the *Layers Reference*'s.
* **Marker coverage.** Flags read: each flagged sentence had no marker of its own in the base, or keeps
  its clause's marker on a lead-in.
* **Over the caps after the pass:** "The page names a mask-data layer `TUNMmk` in three generic checks —
  …" (54 by the script, three quotations); the "Plates on runs with no drawn `tunm`" bullet (73: its
  second sentence begins "Because", so it cannot open a continuation paragraph — R-PARA 2); the
  quick-facts Polarity cell. Inside the second in-force note (not editable, §2.5): one 126-word
  paragraph with sentences of 66 and 60 words. Before → after: paragraphs 14 → 1 (in the note), items 1
  → 1, sentences 15 → 3 (two in the note), cells 1 → 1.
* **Content problem for the owner (not changed):** as on onom, the open text paraphrases the notes:
  "takes the other view for tight layouts" and "describe the same sequence, the mask it uses and the
  undercut the isotropic etch leaves". `check_inforce.py` passes; §2.5 would forbid writing it now.
