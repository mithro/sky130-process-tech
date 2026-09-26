# Progress — readability batch 9, steps 118–134 (`topic/rd-steps-118-134`)

Writer: Opus. Started 2026-09-26 from `main` at `b74bba1a`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–8 (plain bullets over invented labels; no H3
where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing, declared with the deleted text and
the survivor's location; no hand-inserted non-breaking spaces; "What is specific … is that X, and that
Y" over the cap → "… is that:" and one bullet per clause; one bullet per topic where a pronoun needs its
antecedent; a hyphen or slash at a source line break is joined). Medium classes avoided (batch 4–8
reviews): a pronoun whose referent changes after a split; a marker lost when dash material moves; a
sentence moved below the grade that refers to it; glance wording that strengthens a grade; a
whole-sentence trailing hedge not repeated on every half of a split. Model pages: 113, 110. One commit
per page.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base HEAD --allow-regrouped <page>` against
  the commit before the page, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line is named in the page entry; every REGROUPED and number_order line read;
  `--strict-words` as the final run, every LOST word named.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every sentence
  not verbatim in the base — split at full stops **and semicolons** — with its closest base sentence and
  flags any marker or hedge word the base sentence had and the new one lacks. Every flag read.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts rows, H2 list and Deep-dive
  count identical; one admonition (the glance box, `:class: at-a-glance`); no duplicate H3; every glance
  marker recurs below; the scope sentence is the italic lead-in.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in label is not counted into its sentence; a quotation
  counts as one word.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Content problems for the owner (not fixed; text kept verbatim)

(filled in per page below and collected here at the end)

## Pages

### 118 VIM — done

* **Lead:** 112 words → two paragraphs at "The holes are etched at".
* **R-H3 + R-TABLE:** `### What the public record shows` over the post-figure passage (rules, CD
  table, extraction values, then the two differences from the contact level). The via.1a–via.5a,
  m2.4/m2.5 enumeration → `Rule | Constrains | Value`, unit in each cell (via.3 is `0.2\*L`;
  m2.4/m2.5 one row, "the same 0.055 µm and 0.085 µm" as in the base); `[^pdk-periph]` on the lead-in
  "The periphery rules give:". number_order LOST
  `('0.150','1','0.150','0.230','0.280','1','0.170','2','3','0.2','1','0.055','4','0.085','5','2','0.055','0.085','4','5')`
  hand-checked against the rows: via.1a 0.150 µm; via.1b 0.150, 0.230 and 0.280 µm; via.2 0.170 µm;
  via.3 0.2\*L; via.4a 0.055 µm; via.5a 0.085 µm; m2.4, m2.5 0.055 and 0.085 µm — same digits, same
  pairing. "enclosures by metal 1" → "enclosure by metal 1" in two cells (word "enclosures" lost).
* **R-LIST:** "in two ways …: First, … Second, …" → plain bullets. First: split at its colon ("… though
  it is narrower. The stack diagram gives …"). Second: the dash material (the two Cypress stacks)
  becomes its own continuation sentence "The stack is a 300 Å …[^cyp-qtp-113005][^cyp-qtp-123907]
  ({ref}`overview-metal-cap`)." ("The stack is" added by the split); the which-clause (etch stop and
  mirror) stays with "the top of the metal-1 stack" it describes. Wording of both stacks verbatim.
* **R-CATEGORY:** classification sentence kept whole (33 words); **Specific to this step:** with three
  bullets: the k₁ passage (split at its semicolon; the k₁ formula stays inline, single operation), the
  ITRS quotation, "We infer …" (split from the ITRS sentence at its semicolon) with "Nothing public
  states …" in the same bullet (ruling D2). "What distinguishes it from `CTM1` …" is its own label and
  stays a paragraph; its 50-word sentence split at the semicolon ("… reflective metal. Light that …").
* **R-PARA/R-SENTENCE (Why):** Hole size: lead ends at "top opening;" (the "on our reading" of the
  second clause stays with the slope and capability readings in the continuation). Placement: split at
  ", but a via" — "but" dropped (a continuation paragraph may not open on a connective). Uniformity:
  split at the semicolon. Resistance: the 13-word "(inference: …)" parenthetical closed as its own
  parenthetical sentence directly after the clause it qualifies ("(Inference: … from.)"); the Le et al.
  clause is the continuation.
* **How:** italic scope lead-in (the whole sentence, with its CTM1 pointer). Resist coat: lead ends at
  "if one is used". Exposure: "the era's toolkit was:" + three plain sub-bullets (PSM with OPC, FLEX,
  chemical shrink), each with its markers; the Chen/Wang/Chu dash material becomes its own sentence
  after the list, "its" → "the attenuated PSM's" (R-PARA step 5).
* **R-TOOLS:** three items; *SkyWater says:* only on the ASML item (a quotation of `[^skw-01]`); "The
  model is not public." stays after the grades. Grades unchanged.
* **R-OPENQ:** four labels from each bullet's own words. **R-RELATED:** Previous / Next split; Depends
  on (metal it lands on, oxide it opens), Feeds (the metal that covers it), Same category (the
  analogous hole masks), Mask (mask page, previous and next mask), Category page.
* **R-REPEAT:** `rdtools.py rep` finds no 10-word run in two H2 sections.
* **R-GLANCE:** Does/Why from the lead and Why; numbers via.1a, via.2 (`[^pdk-periph]`) and the
  via-1 height 0.27 µm (`[^pdk-04]`); tool line mirrors the grades; Not public from Open questions.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `pdk-04`, `pdk-periph`,
  `skw-01`, numbers 0.150, 0.170, 0.27, `2`, ref `step-119`, hedges "inference", "likely", "not
  public", identifiers `NILD3`, `via-1` — all the glance box; ADDED numbers `1`×3 ("metal 1" in two
  table cells, "via 1" in the glance). LOST words "but" (above), "enclosures" (table cells), "its"
  (→ "the attenuated PSM's"), "page" ("Mask page:" → "Mask:"), "strength"×3 (R-TOOLS labels).
* **Coverage flags read:** table rows (marker on the lead-in); glance lines; the stack sentence took
  its Cypress markers; the Placement continuation (its enclosure marker stays with the enclosure
  clause); the Resistance and Resist-coat splits (each half keeps its own markers and hedges); the
  toolkit sub-bullets (own markers). None lost a marker or hedge.
* **Left over the caps:** none. Item lead over 30 words: Placement (37; one sentence).

### 119 VIME — done

* **R-H3:** none. As on 108, the post-figure passage mixes the public stack and dimensions with this
  reference's readings (the unlanded-floor "(inference)"), so none of the four titles is true of it;
  it is split into two paragraphs at "The public dimensions are the mask's" instead.
* **Lead:** one paragraph (87 words); the 60-word second sentence split at ", producing" → ". It
  produces" ("It" = the plasma); the dash pair (0.27 µm, `[^pdk-04]`) stays in the first half.
* **Post-figure:** the floor sentence's dash material (the two Cypress stacks, each with its own
  marker) becomes its own sentence, "On the 2013 Cypress description …, it is 300 Å …"
  ("it is" added); "— so the selectivity" → ". So the selectivity" (the ", so" form, same paragraph).
  The dimensions sentence split at its semicolon.
* **R-CATEGORY:** classification ends at the closing em dash (25 words); "and the first of the four
  via etches" → "It is the first …" (subject and verb added). The surface-chemistry sentences
  describe the class, not this step, so they stay a plain paragraph (split at the semicolon). "What
  is specific to this class …" is its own label (step 3), a paragraph; split at ", so the etch" →
  ". So the etch …"; "(industry practice;[^nojiri-2015] see below)" stays with the practice clause it
  qualifies.
* **R-PARA/R-SENTENCE (Why):** Landing: lead ends at the `[^pdk-08]` clause; "and on our reading that
  gap" → "On our reading that gap" (continuation; the hedge and `[^pdk-04]` stay with it). Not
  punching through: the cap dash material becomes the lead "The cap is 300 Å …" (subject and verb
  added, both Cypress markers); the Hess dash material becomes its own sentence after the AlF₃
  sentence; the patent sentence split after the quotation, **`[^pat-etchstop-ti]` repeated** on
  "Nothing public gives the corresponding figure for TiW." (the patent is what shows no TiW figure;
  declared). Poisoned via: "— the "poisoned via" that …" → "This is the "poisoned via" that …";
  "and that a UMC patent addresses" → a continuation "A UMC patent addresses it, …" ("it" for the
  relative "that"; the only way to keep the lead block under 60 words, since a continuation may not
  open on "This").
* **How:** italic scope lead-in. Main oxide etch: lead + continuation, split at the semicolon.
  Endpoint: split at the Wodecki dash pair (its marker stays with it), "and the etch" → "The etch"
  (continuation), ", and it fails" → ". It fails" ("It" = the protecting mechanism, as before). Strip
  and clean (a 48-word sentence with two dash pairs): the ash-class gloss becomes "The ash is
  GaSonics, Iridia or Mattson class in SkyWater's list.[^skw-01]" (subject and verb added) directly
  after the sentence; the SkyWater-lists dash material (a full sentence already) starts the
  continuation with its parenthetical. Metrology: lead + continuation at the semicolon.
* **R-TOOLS:** as 108: statement head with the quotation, gloss paragraph, *Runs this step:*
  **weak**; strip/clean *Tool exists:* strong. Lam Exelan has no grade; unchanged.
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** five labels; Previous / Next split, Depends on (films cut,
  cap it stops on), Same category (analogous hole etches); glance tool line in the 108 form.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED marker `pat-etchstop-ti` (the
  repeat above); every other ADDED line is the glance box (markers `pdk-04`, `pdk-08`,
  `pdk-periph`, `skw-01`; numbers 0.055, 0.150, 0.27, 4.5, `1`×3, `2`, `4`; ref `step-115`; hedges
  "likely", "not public"; identifiers `metal-1`, `via-1`×2). LOST words "producing" (→ "produces"),
  "strength"×2 (R-TOOLS). No number regrouped outside the glance.
* **Coverage flags read:** the halves of the lead, floor, landing, cap and endpoint splits (each keeps
  its own markers and hedges; "usually" and "on our reading" stay with their clauses); semicolon
  artefacts in parentheticals; glance lines. None lost a marker or hedge.
* **Left over the caps:** none. Item leads over 30 words: Strip and clean (40), poisoned via (47,
  two sentences; the second cannot open a continuation).

### 120 TIN3 — done

* **Kept verbatim** (the S9a figure agent's note): the lead's "coating the oxide sidewalls and the
  titanium–tungsten floor" (unhedged, while the post-figure bullets give the floor as TiW or TiN) —
  see Content problems. Both stack descriptions keep their wording.
* **Lead:** base 196 words → three paragraphs (§4.1 note ¹), split at "The liner is described" and
  "The film is"; first sentence cut at its colon to 9 words ("… of the via-1 plug. It is a thin
  titanium nitride film …"). The 22-word IMP parenthetical became its own sentence, "This is
  ionised-metal-plasma physical vapour deposition, … bias.[^rossnagel-1998]" (the 109 form). The
  film-roles sentence split at its semicolon ("It is removed from the field …").
* **R-H3:** none (as 109: the passage mixes the public geometry with this reference's readings).
* **R-LIST:** "differs … in the floor and the geometry" → two plain bullets. Floor: the dash material
  (the two stacks) becomes the continuation "On the 2013 Cypress description …, the floor is 300 Å …"
  ("the floor is" added); "and on the second reading the liner meets a film of its own material" →
  its own sentence, **`[^cyp-qtp-123907]` repeated** on it (the claim rests on the 2014 report;
  declared). Hole: split at the dash, "It is shallower …" (subject and verb added). The
  "min. etch and fill capability" sentence stays as prose after the list.
* **R-CATEGORY:** classification cut at its semicolon (12 words), the category-page sentence after it;
  the liner-family sentence (lists other steps) as a paragraph, "it" → "`TIN3`" (the paragraph now
  follows a sentence whose last subject is TIN2); "What is specific …" (its own label) split at ",
  which makes" → ". This makes …" in the same paragraph.
* **R-PARA (Why):** Nucleation: continuation at "Srinivas et al.". Barrier: lead ends at the first
  semicolon ("them" in the continuation keeps its antecedent directly above). Coverage: lead ends at
  the markers of "directional". Resistance: split at the colon before "Kwok et al.".
* **How:** italic scope lead-in. Sputter pre-clean (46 words, dash pair plus two parentheticals): the
  dash material becomes "These are the titanium- and tungsten-fluoride and oxide residue on the cap
  floor (industry practice[^txt-05])." — the trailing "(industry practice[^txt-05])" scoped the whole
  sentence, so it is **repeated** on the new sentence (R-SENTENCE step 5; declared ADDED marker
  `txt-05`); Boumerzoug is the continuation. IMP TiN: split at the semicolon; continuation from "A
  wafer bias".
* **R-TOOLS:** AMAT item in the 109 form; the platform-model and chamber-use sentence stays whole
  under *Runs this step:* (one sentence grading two things at one strength). Novellus bullet has no
  grade; unchanged.
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** four labels; Previous / Next split, Depends on, Feeds
  (TIAL12), Same category (the other liners); glance in the 109 form, "the floor" left unnamed.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `txt-05` and
  `cyp-qtp-123907` (the two repeats above); every other ADDED line is the glance box (markers
  `pdk-04`, `pdk-periph`, `skw-01`; numbers 0.15, 0.27; quotes "Imp TiN"×2; hedges "likely", "not
  public"; identifiers `metal-1`, `via-1`) or `TIN3` (noun restored). REGROUPED: the floor/hole
  sentence's numbers, same order. LOST word "strength" (R-TOOLS).
* **Coverage flags read:** the floor lead ("rather than … a TiN-on-refractory-cap interface"; its
  support is the stack sentence directly after it, as in the base's dash order), the hole split, the
  "This makes" sentence (the Cypress markers support the thickness clause they follow), the residue
  sentence (the cap markers belong to "thin the cap"). None lost a marker or hedge.
* **Left over the caps:** lead 200 words in three paragraphs (base 196; "It is", "This is" added).
  Item leads over 30 words: Resistance (33), IMP TiN (35, an attribution dash pair).
