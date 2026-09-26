# Progress — readability batch 11, steps 141–149 (`topic/rd-steps-141-149`)

Writer: Opus. Started 2026-09-27 from `main` at `e9bbf1a6`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–10 (plain bullets over invented labels; no
H3 where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing; no hand-inserted non-breaking
spaces; "What is specific … is (that) X, and (that) Y" over the cap → "… is (that):" and one bullet per
clause; one bullet per topic where a pronoun needs its antecedent; a hyphen or slash at a source line
break joined; a blank line after the glance box's closing `:::`; hedge scope at a semicolon split per
R-SENTENCE step 5 and D1). Medium classes avoided (batch 4–10 reviews): a pronoun whose referent
changes after a split; a marker lost when dash material moves; a sentence moved below the grade that
refers to it; glance wording that strengthens a grade; a whole-sentence trailing hedge not repeated on
every half of a split. Model pages: 126, 129 (batch 9), 139 (batch 10). One commit per page.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base HEAD --allow-regrouped <page>` against
  the commit before the page, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line is named in the page entry; every REGROUPED line read; `--strict-words` as the final
  run, every LOST word named.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every sentence
  not verbatim in the base — split at full stops **and semicolons** — with its closest base sentence
  and flags any marker or hedge word the base sentence had and the new one lacks. Every flag read.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts rows, H2 list and Deep-dive
  count identical; one admonition (the glance box) followed by a blank line; no duplicate H3; every
  glance marker recurs below; the scope sentence is the italic lead-in; no consecutive duplicate line,
  no prose line ending in a hyphen or slash, no bare `>`, no NBSP.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in or italic R-TOOLS label is not counted into its
  sentence; a quotation and a code span count as one word; an em dash is not a word.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 141 NILD5 — done

Base `e9bbf1a6`. Caps before: 3 paragraphs, 7 items, 13 sentences over; after 0/0/0. Lead 164 words
(base 159, one paragraph) in two paragraphs (89, 75); first sentence 11 words.

* Lead: the dash material "0.845 µm tall … (m3.2)" moved after the sentence as "The lines are 0.845 µm
  tall …" with both markers (126 form); the sentence split before CMPM3 ("which" → "CMPM3 then polishes
  that layer flat and NCAPOX5 caps it"); the "_C" sentence split at ", and the diagram's levels". The
  trailing "(our arithmetic from the diagram)" stays on the levels sentence: its other half ("drawn with
  no separate "_C" film") is cited to `pdk-04`, which states it (D1).
* R-LIST: "Two things make this gap fill different …:" two bullets, each bolding its own opening words
  in place ("The gap is deeper:", "The surface is not only metal:"; "And" dropped); the CAPM sentence
  split at ", and the PDK's cross-section" (the "on our reading" hedge is inside the dash pair of the
  first half and stays there); "The oxide deposited here is therefore …" an indented continuation.
* R-CATEGORY: classification sentence to "(after NILD4)." (21 words); "which sets out" → "NILD3 sets
  out" (restored noun; the page's own Related bullet and 126 say NILD3 sets out the routes) with the two
  routes as bullets; the SkyWater sentence a paragraph; "What is specific to this instance is:" three
  bullets (only "and" dropped).
* R-PARA/R-SENTENCE (Why): insulation item split at the semicolon, the studies a continuation; the
  capacitor item's colon lead with the two studies as sub-bullets ("and" dropped) and "Here the top
  plate floats …" as a continuation, its trailing "(inference that …)" unchanged; capacitance item split
  at the semicolon ("they" → "The tables", restored noun); polishable-overburden item split at the
  semicolon, "on our reading" stays with the Oxide-Bias clause it was in.
* How: scope sentence as the italic lead-in; step 1 split at the semicolon (two separately cited facts);
  step 2 split at the semicolon, "Backside helium …" a continuation (126 form); step 4 split at the
  semicolon, "as-\ndeposited" joined; its "(industry practice; … not public)" stays on the second half,
  the first being covered by the italic scope sentence (as 140 step 2 in batch 10).
* R-TOOLS: HDP-CVD three-line item, model sentence as a continuation; PECVD TEOS two grades; C1 bullet
  unchanged (no "Strength:").
* R-RELATED: Previous · Next · Same module (the capacitor steps; every step 135–163 has the Phase cell
  "MiM capacitors, metal 3–5, via 3–4") · Depends on (NILD3, NILD4) · Same category (NILD6) · Category
  page.
* R-OPENQ: five labels from the bullets' own words.
* R-GLANCE: Does/Why from the lead and the "Without `NILD5` …" paragraph; numbers from the lead
  (`pdk-04`, `pdk-periph`); tool line = the R-TOOLS grades; Not public = Open question 1.
* `check_preserved --allow-regrouped`: ADDED only the glance box (markers `pdk-04`, `pdk-periph`,
  `skw-01`; numbers 0.300, 0.845, 4.1, 3, 4; quote "NILD5"; hedges inference, likely, not public;
  identifiers NILD5, metal-3) and the restored noun `NILD3` and the label "Metal-3 thickness";
  REGROUPED lines are the three splits above and the glance (same digits, same order).
  WORDS LOST: `and`, `strength`×2, `they`, `which`×2 (all named above). No DUPLICATED line.
* `cov`: 4 flags, all read — the "our arithmetic" and "on our reading" hedges stay on the clauses they
  qualify (see Lead and R-LIST above); two pairing noise.
* R-REPEAT: none (only the glance repeats body text).

### 142 CMPM3 — done

Base `ed78ad03`. Caps before: 3 paragraphs, 4 items, 6 sentences over; after 0/0/0. Lead 142 words
(base 142, one paragraph) in two paragraphs (90, 52) split at "As at CMPM …" (127 form).

* R-LIST: "The PDK's metal-3 rules are written around it:" kept in its paragraph (so "it" still follows
  the same sentences as in the base), the `pdk-periph` rules and the `pdk-03` assumptions as two
  bullets, each with its own marker (127 form). "Two things are specific to this instance:" (full
  stop → colon) and two plain bullets; "And" dropped.
* The second category bullet (50 words) split at its colon; "(inference from the construction)"
  repeated on the first half ("closer to a *device* than any earlier oxide polish"), which is neither
  cited nor otherwise hedged (D1; declared ADDED hedge `inference`).
* R-PARA/R-SENTENCE (Why): planarity item split at the semicolon, studies a continuation (127 form);
  capacitor item split at the semicolon — the first half keeps its "On our reading", the second its
  "(our arithmetic from estimated thicknesses)"; pattern-density item split at the semicolon, "Stine
  et al. showed …" a continuation.
* How: italic scope sentence; step 3 split at the first semicolon (two cited facts) and at "the
  PDK;[^pdk-04] down-force" (two cited facts), the platen sentences a continuation; step 6 (53-word
  sentence) as four sub-bullets at its semicolons (127 form), words unchanged. Step 2's semicolon kept
  (127 form, 40 words).
* R-TOOLS: Mirra three-line item; KLA "Strength: medium." → "*Tool exists:* medium." (127 form); the
  SEZ bullet has no grade and is unchanged.
* R-RELATED: Previous · Next · Depends on (MM3E, CAPME; MM3) · Feeds (VIM3E; MM4) · Same category
  (CMPM, CMPM2, CMPM4) · Category page. R-OPENQ: five labels from the bullets' words.
* R-GLANCE: numbers from the lead (`pdk-04`), the rules bullets (`pdk-periph`, `pdk-03`); tool line =
  R-TOOLS grades; Not public = Open questions 1 and 3 (no number: the 0.2–0.3 µm estimate has no
  marker).
* `check_preserved --allow-regrouped`: ADDED = glance (markers `pdk-03`, `pdk-04`, `pdk-periph`,
  `skw-01`; numbers; quote "Oxide Bias for MM3"; ref `step-141`; hedges inference, likely, not public)
  + the repeated "inference" above + identifiers from the glance and the "Split of the via-3 height"
  label. REGROUPED: the rules sentence into two bullets, the capacitor item split (same digits, same
  order). WORDS LOST: `strength`×2. No DUPLICATED line.
* `cov`: 3 flags, pairing noise (the "assumptions"/"typical"/"our reading" words are in the
  neighbouring bullet or sentence, unchanged).

### 143 NCAPOX5 — done

Base `7663248c`. Caps before: 3 paragraphs, 2 items, 5 sentences over; after 0/0/0. Lead 139 words
(base 139, one paragraph) in two paragraphs (85, 54) split at "The finished number is public" (128
form).

* Post-figure paragraph (140 words) split before "What the cap prepares for"; the 23-word
  parenthetical on the `cap_mim` cross-section became the following sentence, its parentheses removed,
  words and `pdk-07` unchanged (R-SENTENCE, parenthetical ≥ 12 words; one dash pair left inside it, as
  in the base).
* R-CATEGORY: classification to the closing dash ("… PECVD section."); "and, like its predecessors, …"
  → "It is, like its predecessors, …" (subject and verb added, "and" dropped; 128 form); "What is
  specific to this instance is that:" two bullets (only "and" dropped; 128 form).
* R-PARA/R-SENTENCE (Why): thickness item split before "Polishing slightly …" (continuation); sealing
  item split at the semicolon ("them" = the scratches, particles and layer of the sentence before).
* How: italic scope sentence; step 1 split at the semicolon (two cited facts); step 2's Cypress
  sentences a continuation, split at the semicolon ("That it is a plasma …", hedges "our inference" and
  "a further inference" unchanged on their clauses); step 5's 13-word trailing hedge "(Inference that
  it matters here; Wang, Ackaert et al. document the MiM case.[^wang-2004-mim])" now its own
  parenthetical sentence directly after the sentence it qualifies (R-SENTENCE step 7), so it still
  covers the whole of it.
* R-TOOLS: TEOS item two grades, the "readings of the names, not stated" sentence a continuation (128
  form); C1 bullet unchanged.
* R-RELATED: Previous · Next · Depends on (NILD5; MM3E, CAPME) · Same category (the cap oxides) ·
  Category page. R-OPENQ: four labels from the bullets' words.
* R-GLANCE: Why keeps "we infer"; the only number is the lead's 0.39 µm (`pdk-04`); the tool line
  keeps both grades.
* `check_preserved --allow-regrouped`: ADDED = glance only (markers `pdk-04`, `skw-01`; 0.39, 3;
  quote "C2 and Producer"; hedges inference, likely, not public, we infer; identifiers) and the
  labels. REGROUPED: the cross-section parenthetical (same digits). WORDS LOST: `strength`.
* `cov`: 6 flags, all read — glance/label pairing noise; the step 5 hedge is the next sentence.

### 144 VIM3 — done

Base `4008a297`. Caps before: 5 paragraphs, 6 items, 10 sentences over; after 0/0/0. Lead 114 words
(within the cap in the base too) in two paragraphs (83, 31); first sentence 5 words (base 29: "…
lithography: the mask step …" → "… lithography. It is the mask step …", subject and verb added).

* Lead: split at "Unlike `VIM2`" and at the semicolon before "The minimum-CD table" (two cited facts;
  "it" is still the via-3 mask of the sentence before).
* R-H3 + R-TABLE: `### What the public record shows` after the caption (129 form); the via-3 rule
  sentence as a `Rule | Constrains | Value` table, lead-in "The periphery rules give:[^pdk-periph]"
  (the sentence-end marker on the lead-in); via3.3 has no value in the base → `—`; the dash aside
  "the layer that marks e-test modules[^pdk-06]" the first sentence after the table ("`areaid.mt` is
  …", subject and verb added). `number_order` LOST on the rule sentence, hand re-paired: via3.1 0.200;
  via3.1a 0.200 and 0.800 inside `areaid.mt`; via3.2 0.200; via3.3 the quoted rule, no value; via3.4
  0.060; via3.5 0.090 on one of two adjacent sides; m4.3 0.065 — base order, same digits. WORDS LOST
  `enclose`, `must`, `with` from the cells ("metal 4 must enclose the via by" → "enclosure of the via
  by metal 4", as 129's m3.4 row). The hole-depth sentence a paragraph of its own.
* "What makes this via mask different …" (106 words) split before "Since the plate stands …"
  ("Since X, Y" is a complete subordinate opener, not a connective); its 46-word sentence split at the
  dash: "…than a via over bare metal 3, by the plate and dielectric thicknesses (inference). These are
  of the order of 0.1–0.2 µm on our reading of CAPILD and CAPTIW1 (inference)." — the trailing
  "(inference)" repeated on the first half, which is uncited (D1; declared ADDED hedge).
* Step category (three paragraphs in the base, so R-CATEGORY does not apply): first paragraph split
  after the classification sentence; the 50-word k₁ sentence split at its colon ("Its geometry is via
  2's. At 0.20 µm …"), so "while" and "(our arithmetic)" stay where they were; the Sheet4 paragraph
  split at the colon after "248 nm exposure" and before "We also read", and at the semicolon after
  `itrs-03` (the "less certainly" reading stays on its clause; "The tab does not define …" is a
  statement about the tab).
* Why: hole-size item split after the lead sentence; metal-3 placement item split at the semicolon,
  "A via that slips …" a continuation; capacitor-plate item: lead sentence, then the `capm`-rules
  sentence, then the two-dash-pair sentence split — "On our reading, in the flow described here those
  rules apply to via 3 (inference; see CAPILD). This reading is consistent with the cross-section, …
  "Via3",[^pdk-07] the layer table[^pdk-06] and CAPM." (subject and verb added; the inner dash pair
  "— the only via it labels —" kept); uniformity item: the dash aside on capacitor via arrays moved
  after the sentence with its "(inference from the 5.8 Ω/sq `RSCAPM`[^pdk-07])" (REGROUPED, same
  digits).
* How: italic scope sentence; step 2 split at the semicolon (two cited facts); step 3's sheet sentence
  a continuation ("the latter" still follows the sentence naming the two reticle types).
* R-TOOLS: ASML three-line item; tracks and CD/overlay items with their grades (129 form).
* R-RELATED: Previous · Next · Depends on · Feeds · Same category (the hole masks) · Mask (with
  previous/next mask, from the "Previous mask" bullet) · Category page. WORDS LOST `page` ("Mask
  page:" → "Mask:").
* R-OPENQ: five labels; the mask-type bullet split at its semicolon (129 form); the `capm` bullet split
  at its semicolon with "we read it so" → "We read that wording so" (restored noun, the head being two
  lines above); the PLM bullet split after its first clause.
* R-GLANCE: numbers from the table (`pdk-periph`) and the hole depth (`pdk-04`); tool line = the
  R-TOOLS grades; Not public = Open questions 1 and 2.
* `check_preserved --allow-regrouped`: ADDED = glance, the H3, the repeated "inference", identifiers
  from the glance and labels; LOST only the rule-table `number_order` above. WORDS LOST: `enclose`,
  `must`, `with`, `page`, `strength`×3. No DUPLICATED line.
* `cov`: 8 flags, all read: pairing noise, or the hedge now in the neighbouring sentence as described.
* R-REPEAT: the cross-section sentence ("labels the via that lands on "CAPM" — the only via it labels
  — "Via3"") occurs under Why and Open questions, as in the base; each copy carries its own argument,
  so none deleted.

### 145 VIM3E — done

Base `f333b98f`. Caps before: 3 paragraphs, 3 items, 9 sentences over; after 0/0/0. Lead 142 words
(base 141, one paragraph) as an opening paragraph, a two-item list and a closing paragraph (32, 70,
40); first sentence 5 words.

* Lead, R-LIST: "… down to two kinds of floor at once:" announces a count; one bullet per floor, every word kept
  ("and" dropped, comma → semicolon), each with its own markers (`cyp-qtp-*` and `pdk-04` on the
  metal-3 cap, `pdk-07` on the plates). The floor wording ("the refractory cap of the metal-3 lines")
  is unchanged — see Content problems.
* Post-figure paragraph (135 words) split before "The plate floor is higher …"; that 50-word sentence
  split at ", so" ("So a via …", allowed where the split requires it), the dash aside a comma
  apposition in place, so "on our reading" stays on the 0.1–0.2 µm and "(inference from the
  construction)" on the So-sentence (D1: the other half carries its own hedge).
* Step category (190 words, one paragraph): classification sentence alone (130 form); the VIME
  sentence split into "VIME sets out … within the flow." + the stop-layer sentence + "So the etch must
  …" + "CTME sets out the underlying surface chemistry." (the elided verb restored, 130 form); the
  17-word parenthetical "(which is why the Ti-bearing part … ; not separately sourced here)" stays in
  parentheses as its own sentence directly after the clause it explains, "which" → "That" (it follows
  "…volatile only at elevated temperature." at once); the dual-depth sentence's dash aside (the ARDE
  review, `gottscho-1992`) moved after the sentence it interrupted, so "here that shallow floor" still
  follows "the shallow floor" (REGROUPED); "What is specific to this instance is the dual-depth
  landing." left as its own label (R-CATEGORY step 3).
* Why: plate item — the Schaepkens dash aside (with `schaepkens-1999` and its "by inference") became
  "That protection is a steady-state fluorocarbon film …" after the sentence it interrupted (subject
  and verb added; "them" still Schaepkens et al.); metal-3-cap item split at the semicolon with
  `pat-etchstop-ti` repeated on the quotation sentence (130 form; declared ADDED marker); charging item
  split at the semicolon.
* How: italic scope sentence; step 3 split after the cited chemistry ("It has high selectivity …",
  subject and verb added; WORDS LOST `with`), its "(industry practice; … Freescale patent)" stays on
  the selectivity sentence, the other half being cited; step 4 dash aside → "Wodecki describes …" and
  "The etch is run by time …" a continuation (130 form); step 5 the ash-class dash aside with
  `skw-01` a continuation "The ash is GaSonics, Iridia or Mattson class in SkyWater's list." (130
  form); step 7 the test-tile sentence a continuation.
* R-TOOLS: "No dielectric etcher" bullet — grade as `*Runs this step:* **weak** …` after the "All three
  carry …" continuation (130 form); Exelan bullet unchanged; strip/clean `*Tool exists:*`.
* R-RELATED: Previous · Next · Depends on · Same category · Category page. R-OPENQ: five labels.
* R-GLANCE: "none assignable", with the page's **weak**; numbers `pdk-periph`, `pdk-04`, `pdk-08`.
* `check_preserved --allow-regrouped`: ADDED = glance + the repeated `pat-etchstop-ti`; REGROUPED:
  the lead list, the plate-floor split. WORDS LOST: `strength`×2, `with`. No DUPLICATED line.
* `cov`: 7 flags, all read (pairing noise; hedges on the neighbouring sentence as above).

### 146 TIN5 — done

Base `d04fe7bd`. Caps before: 3 paragraphs, 3 items, 5 sentences over; after 0/0/0. Lead 237 words
(base 233, one paragraph) in three paragraphs (91, 62, 84), split at "The liner is described here" and
"The film is" (131 form); first sentence 8 words (base 85).

* Lead: "…plug: a thin titanium nitride film …" → "…plug. It is a thin titanium nitride film …" (131
  form); "the floors, which are of two kinds:" → "the floors. The floors are of two kinds:" (restored
  noun; WORDS LOST `which`); the 21-word parenthetical's second half became the sentence "The PDK's
  `cap_mim` cross-section draws vias from metal 4 landing on both.[^pdk-07]" ("both" = the two kinds of
  floor of the sentence before), "(TiW, as assumed at CAPTIW1)" kept in place; the 18-word IMP
  parenthetical → "This is ionised-metal-plasma …" (131 form); "…for the plug; it is removed …" split
  at the semicolon.
* Post-figure paragraph (110 words) split at the semicolon before "A via over a capacitor …"; its
  "(on our reading 0.1–0.2 µm, …)" stays in that sentence.
* Step category: classification sentence alone; "TIN2 sets out …" kept whole; "It is the last of the
  five liner depositions" → "`TIN5` is the last …" (restored noun, since "It" would now follow the
  TIN2/TIN3 sentence), split at the semicolon before "Via 4 above it"; "What is specific …" with the
  plate sentence as its own paragraph (R-CATEGORY step 3).
* Why: coverage item and via-resistance item split before their study sentences (continuations).
* How: italic scope sentence; step 3 split at the semicolon, the Boumerzoug sentence a continuation
  (62-word item otherwise).
* R-TOOLS: AMAT PVD three-line item (131 form); INOVA bullet unchanged.
* R-RELATED: Previous · Next · Depends on · Feeds · Same category · Category page. R-OPENQ: four
  labels.
* R-GLANCE: Why condenses the lead's three roles; numbers `pdk-periph`, `pdk-04`, and "no liner
  thickness is published for SKY130" (lead: "Its thickness is not public").
* `check_preserved --allow-regrouped`: ADDED = glance only; REGROUPED: the floor sentence split.
  WORDS LOST: `strength`, `which`. No DUPLICATED line. `cov`: 4 flags, pairing noise.

## Content problems for the owner (not fixed; text kept verbatim)

* From the S9b figure notes: on the stop-on-dielectric reading of CAPME, the MiM dielectric stays on
  every metal-3 shape under the MM3 resist; 141's caption says so ("left on the metal-3 shapes on this
  drawing, as at MM3E"), the page text does not. The 145 page gives the via floor as the metal cap
  without saying so (see 145 below).
