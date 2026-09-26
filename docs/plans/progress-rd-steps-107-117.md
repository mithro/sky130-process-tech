# Progress — readability batch 8, steps 107–117 (`topic/rd-steps-107-117`)

Writer: Opus. Started 2026-09-26 from `main` at `fb02bd1f`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–7 (plain bullets over invented labels; no H3
where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing, declared with the deleted text and
the survivor's location; no hand-inserted non-breaking spaces). Medium classes avoided (batch 4–7b
reviews): a pronoun whose referent changes after a split; a marker lost when dash material moves; a
sentence moved below the grade that refers to it; glance wording that strengthens a grade; a
whole-sentence trailing hedge not repeated on every half of a split. Model pages: 101, 097. One commit
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
  flags any marker or hedge word the base sentence had and the new one lacks. Every flag read; the page
  entry says what each class is.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts table, H2 list and Deep-dive
  count identical; one admonition (the glance box, `:class: at-a-glance`); no duplicate H3; every glance
  marker recurs below; the scope sentence is the italic lead-in.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block and `## References`
  **excluded**; a leading bold run-in label is not counted into its sentence.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 107 CTM1 — done

* **R-H3:** `### What the public record shows` over the post-figure passage (rules, CD tables,
  extraction, stack diagram), which is public record ending in the hedged 0.34 µm depth.
* **R-TABLE:** the ct.1–ct.4, m1.4, m1.5 enumeration → `Rule | Constrains | Value`, unit in each cell
  (ct.3's value is `0.170\*L`); `[^pdk-periph]` on the lead-in. number_order LOST
  `('0.170','1','0.190','2','3','0.170','4','0.000','1','0.030','4','0.060','5')` hand-checked
  against the rows: ct.1 0.170 µm, ct.2 0.190 µm, ct.3 0.170\*L, ct.4 0.000 µm, m1.4 0.030 µm,
  m1.5 0.060 µm — same digits, same pairing.
* **R-LIST:** the four physical-criteria entries as bullets, `[^pdk-03]` on the lead-in "The
  physical-criteria table adds:"; the era's four exposure answers as sub-bullets under **Exposure**,
  each with its own markers.
* **R-CATEGORY:** classification split at the colon ("… for a projection printer.[^mack-2007] An
  isolated small square …[^mack-2007]"; marker repeated, declared); the remaining five sentences as
  plain bullets under **Specific to this step:**; "it" → `CTM1` in the first (R-PARA step 5).
* **R-PARA/R-SENTENCE:** lead in two paragraphs (split at the full stop before "The holes are
  etched"; the 59-word sentence split at its semicolon). The extraction sentence: the mid-sentence
  parenthetical hedge "(the PDK heads the column … we read the contact rows as per-contact resistance)"
  moved, unchanged, to directly after its sentence as "(The PDK heads … resistance.[^pdk-08])" —
  `[^pdk-08]` repeated because the parenthetical states what the PDK does (declared). The stack
  sentence split at its semicolon; the compound hedge divided per the batch-7b ruling D5: the first
  half (where the drawing places the two bottoms) takes "(our reading of a drawing marked "not to
  scale")" with `[^pdk-04]`, the second keeps the full "(our reading … and our arithmetic)". Resist
  coat: the 17-word PDK parenthetical became its own sentence; item split into lead and continuation.
  Exposure: the NA parenthetical became its own sentence; k₁ stays inline (single-operation estimate).
  Placement: split at the semicolon before "Levinson's book".
* **R-TOOLS:** three items; *SkyWater says:* only on the ASML item (a quotation of `[^skw-01]`);
  "The model is not public." stays after the grades as continuation. Grades unchanged.
* **R-OPENQ:** four labels from each bullet's own words. **R-RELATED:** Previous / Next split (the
  bullet named two relationships); Depends on / Feeds / Same category (all four masks are
  lithography steps) / Mask / Category page. **R-HEDGE:** italic scope lead-in.
* **R-REPEAT:** `rdtools.py rep` finds no 10-word run in two H2 sections.
* **R-GLANCE:** Does/Why from the lead and Why; numbers ct.1, ct.2 (`[^pdk-periph]`) and the bottom
  CD (`[^pdk-03]`); tool line mirrors the grades ("strong for existence", "inference" for the DUV
  assignment); Not public from Open questions.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `mack-2007`, `pdk-04`,
  `pdk-08` (the three repeats above) and the glance markers; ADDED numbers `1`×3 ("metal 1" in two
  table cells, plus the glance), `2` and the glance numbers; ADDED quotes "not to scale" (hedge
  divided) and "Standard contact bottom CD" (glance); ADDED hedges "our reading" (divided hedge),
  "inference", "likely", "not public" (glance); ADDED identifiers `CTM1` (noun restored), `met1`,
  `metal-1` (glance). LOST words: "page" ("Mask page:" → "Mask:"), "strength"×3 (R-TOOLS labels),
  "and"×2, "it". Nothing else.
* **Coverage flags read:** table rows and list entries whose marker is on the lead-in (by design);
  each exposure sub-bullet carries only its own markers; R-TOOLS grades whose marker is on the head;
  the ITRS/critical-layers semicolon clause (its markers stay with their own clauses). No claim
  sentence lost a marker or hedge.
* **Left over the caps:** lead 122 words (base 122); "The PDK's "Standard contact bottom CD" …"
  (49 words): its only seam is the dash before "which eases", and "on our reading" scopes the
  which-clause, so the second half would lose the hedge; "The 0.1 µm `li`, the 0.075 µm LINT …"
  (46 words): the only seam is ", so", and both halves would need the full compound hedge with its
  quotation (R-SENTENCE step 5: "or do not split"). Resist-coat item lead block 39 words (the
  PDK-thickness parenthetical sentence stays next to the thickness it qualifies).
* Tiles: desktop 01–03 and phone 02–03 read; the rule table fits at 400 px (units wrap below the
  number in the Value column, the known batch-7b D4 case; no number breaks).

### 108 CTME — done

* **R-H3:** none. The post-figure passage mixes the public dimensions with this reference's readings
  (landing on LINT, the zero-enclosure edge case — "inference"), so none of the four titles is
  true of it; it is structured with R-LIST and R-PARA instead.
* **R-LIST:** the public dimensions as three bullets after "those of the mask:"; `[^pdk-03]`
  repeated on the "min. etch and fill capability" bullet, whose value the base supported with the
  same marker at the end of the sentence (declared). Step category: "two properties that mark it
  out" as two plain bullets (no verbatim 2–4-word label exists). Metrology: the three test-tile
  structures as sub-bullets, `[^raw-data-testtile-pads]` on the lead-in "has:"; the "respectively"
  pairing "6384 and 6992" kept in one bullet.
* **R-CATEGORY:** classification sentence ends at the closing em dash (28 words); "with two
  properties" → "It has two properties" (subject and verb added by the split).
* **R-PARA/R-SENTENCE:** lead: ", producing" → ". It produces" ("It" = the plasma). Post-figure:
  "The depth is about 0.34 µm on our reading of the stack diagram.[^pdk-04] The diagram puts …" —
  the hedge scopes only the depth; the which-clause describes the diagram (marker repeated, declared).
  "— so the etch is" → ". So the etch is" (the "So" sentence the guide allows at a ", so"/"— so"
  split; it stays in the same paragraph as the hedged reading it follows from). "(inference); the
  etch" → "(inference). The etch" (the hedge is attached to the first clause). Contact area: split
  at ", and the taper" — "on our reading" sits in the second clause, which keeps it. Etch-stop:
  split at the semicolon; "If it under-etches" stays in the lead block with its antecedent. Main
  oxide etch: split at the second semicolon and at ", and can under some conditions" → "It can …"
  ("It" = the rate). Endpoint: the Wodecki dash material becomes its own sentence. Strip and clean:
  the 14-word solvent parenthetical becomes its own parenthetical sentence directly after the
  sentence it qualifies, marker unchanged after "Batch Rotational".
* **R-TOOLS:** first bullet in the 094 form (statement head, quotation, gloss paragraph, *Runs this
  step:* **weak**); strip/clean item *Tool exists:* strong. Lam Exelan bullet has no grade; unchanged.
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** four labels; Previous / Next split, Depends on, Same
  category; italic scope lead-in; the glance tool line in the 094-review form ("none named … **weak**
  (assignment to the contact etch)").
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `pdk-03`×2 (one repeat,
  one glance), `pdk-04` (repeat), `pdk-periph`, `skw-01` (glance); ADDED numbers, quote, ref
  `step-105`, hedges "likely", "not public" — all glance. LOST words: "producing" (→ "produces"),
  "strength"×2 (R-TOOLS), "with" (→ "has").
* **Coverage flags read:** list items and table-like bullets whose marker is on a sibling or the
  lead-in; the lead's first half has no `[^pdk-06]` (that marker supports the `mcon` quotation in
  the second); the hedge scopes discussed above. No claim lost a marker or hedge.
* **Left over the caps:** item lead blocks over 30 words — Contact area (38; one sentence with the
  per-contact reading parenthetical, no seam that keeps the hedge with the numbers), Etch-stop
  integrity (45; two sentences, the second's "it" needs the first), Endpoint (36), Strip and clean
  (40). No paragraph, item or sentence over the §1 caps.

### 109 TIN2 — done

* **R-H3:** none (the post-figure passage is this reference's reading of the hole and an
  industry-typical thickness; no title fits).
* **Lead:** base 156 words → three paragraphs (§4.1 note ¹: two would leave one over 100), split at
  "The liner is described" and "The film is not"; first sentence cut at its colon to 8 words
  ("… of the metal contact. It is a thin titanium nitride film …"). The 25-word IMP parenthetical
  became its own sentence: "This is ionised-metal-plasma physical vapour deposition, …
  bias.[^rossnagel-1998]" (subject and verb added, marker unchanged).
* **R-CATEGORY:** classification cut at the em dash (11 words), the category-page sentence after it;
  the family-of-liners sentence (lists other steps) and "What is specific …" (its own label) stay as
  paragraphs, no bullets; "In this reference it" → "`TIN2`" (the paragraph now opens after a
  sentence whose subject is the category page).
* **R-PARA/R-SENTENCE:** post-figure: "— so this is a TiN-on-TiN contact" → ". So this is …" in the
  same paragraph as the hedged reading it follows from; "The liner thickness is not public; …"
  starts a second paragraph. Why/Barrier: lead + continuation at "Wittmer reviewed". Why/Coverage:
  lead ends at "about 2:1", the rest a continuation (the lead block would otherwise have to carry
  "That is the point of IMP"); split at "in 1998;". How: Cluster tool split at the semicolon; IMP
  TiN deposition: lead, then the chamber paragraph (split at "titanium; a bias"), then the collimation
  paragraph.
* **R-TOOLS:** AMAT item in three lines; *SkyWater says:* is the quotation of `[^skw-01]`. Novellus
  bullet has no grade; unchanged.
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** four labels; Previous / Next split; bullets relabelled
  and reordered to the R-RELATED order (Depends on, Feeds, Same category); italic scope lead-in.
  Glance numbers: none published for the liner, the hole bottom 0.09 µm with `[^pdk-03]` (the quoted
  name of that value is not in this page's body, so the glance does not quote it).
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `pdk-03`, `skw-01`,
  number `0.09`, quotes "Imp TiN"×2, hedges "likely", "not public" — all glance; identifier `TIN2`
  (noun restored). LOST word "strength" (R-TOOLS). No number regrouped.
* **Coverage flags read:** glance lines; "The liner is described here as IMP TiN." (this reference's
  description, no marker in the base either; `[^rossnagel-1998]` stays on the definition); the "So"
  sentence; the Rossnagel/Hamaguchi split (each half keeps its own markers).
* **Left over the caps:** lead 160 words in three paragraphs (base 156; "It is", "This is" added).
  Nothing else over the §1 caps.

### 110 WDEP2 — done

* **R-H3:** none (post-figure passage 124 words of readings and an industry norm; no title fits).
* **R-PARA/R-SENTENCE:** lead sentence 2 (47 words) cut at the end of its dash material ("… into
  every 0.17 µm contact. It is thick enough …"). Post-figure passage split at "The deposited
  thickness is not public" (hole geometry | fill thickness and SkyWater's wording). Why items:
  Conformality split at the semicolon ("Sputtered aluminium cannot reach …" opens the continuation);
  Nucleation split at "studied;" (the continuation opens "A thin silane-reduced nucleation layer";
  the source's line break after "silane-" rendered as "silane- reduced", now joined — presentation
  only, the tool shows no word lost); Resistance split at "short;". How: Chamber lead + continuation
  at "Novellus's Altus family"; Nucleation layer (97-word sentence): lead ends at "a few nanometres",
  the dash material "Silane is commonly used …[^wiki-wf6]" opens the continuation, split again at
  "fill;" → "In the pulsed variant …".
* **R-CATEGORY:** classification cut at its semicolon (13 words) with the category-page summary
  sentence after it; "Unlike the dielectric depositions …" (one sentence about this step) as a
  second paragraph with no label (step 2).
* **R-TOOLS:** three lines for the Lam/Novellus item; the "Whether the PNL option …" sentence stays
  as continuation (an unknown, not a grade). The metrology bullet has no grade; unchanged.
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** four labels; Previous / Next split, Depends on, Feeds,
  Same category (the other tungsten fills); italic scope lead-in. Glance numbers are the hole
  geometry with the page's own "on our reading of `CTME` and the PDK's assumptions".
* **check_preserved (`--allow-regrouped --strict-words`):** every ADDED line is the glance box (markers
  `pdk-03`, `pdk-04`, `skw-01`; numbers 0.09, 0.17×2, 0.34; hedges "about", "inference", "likely",
  "not public", "our reading"). LOST word "strength" (R-TOOLS).
* **Coverage flags read:** glance lines; the nucleation split (each half keeps its own marker). None
  lost a marker or hedge.
* **Left over the caps:** nothing over the §1 caps; lead 100 words.

### 111 WCMP2 — done

* **R-H3:** none (post-figure passage 65 words).
* **Lead:** base 122 words → two paragraphs at "What is left is a planar oxide surface" (each under 100).
* **R-CATEGORY:** classification cut at its colon (9 words); "Unlike the oxide polishes …" (the one
  sentence about this step) as the second paragraph, no label; the category-page comparison and the
  Kaufman mechanism as a third paragraph.
* **R-PARA/R-SENTENCE:** Why items split at their semicolons ("A flat base": at "this surface;";
  "Contact resistance": at "cover;"; "Oxide loss" (84-word sentence): at "two levels;" — "on our
  reading" is in the second half and stays there). How/Slurry: continuation at "Kaufman et al.",
  split at both semicolons. How/Recipe: the three platens as a nested numbered sequence (R-LIST step 6,
  a recipe), "a second" → "A second"; the down-force and Elbel sentences as the continuation.
  How/Post-CMP clean: the Jolley dash material becomes its own sentence opening the continuation.
* **R-TOOLS:** Mirra item in three lines; "Which of the two tungsten processes runs this step is not
  public." stays after the grades. Defect-inspection item in the 012/100/106 form (*Tool exists:*
  medium). The post-CMP-clean bullet has no grade; unchanged.
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** three labels; Previous / Next split, Depends on, the two
  CMP bullets merged under one "Same category:" (no link dropped or added, glosses kept); italic scope
  lead-in.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED numbers `1`, `2`, `3` are the nested
  recipe labels (the known indented-label case, batch-7b D3) plus the glance; all ADDED markers,
  quote, hedges and identifier `NILD2` are the glance. LOST words "strength"×2 (R-TOOLS).
* **Coverage flags read:** the Slurry split (each sentence keeps its own marker); the Jolley dash
  material (the marker moved with its clause). None lost a marker or hedge.
* **Left over the caps:** item lead block "Contact resistance" (35 words, one sentence with the
  Vlassak parenthetical). Nothing over the §1 caps. (From this page on `rdtools.py` counts a
  quotation as one word, as §1 says; 107–110 have no quotation-heavy sentence near a cap.)

### 112 TIAL6 — done

* **Kept verbatim** (the S8 figure agent's note): every sentence that describes the stack as
  Ti/Al–Cu/TiW or weighs it against the 2014 Ti/TiN/AlCu/Ti/TiN stack keeps its wording; only
  paragraph breaks, list structure and splits at existing seams were made. See Content problems.
* **R-H3:** `### What the public record shows` over the Cypress-report passage (quotations and PDK
  numbers); `### Competing readings` over "Which of the two stacks …", which weighs the two stacks
  (and, in its bold-labelled last paragraph, the readings of the bottom titanium). **On the bottom
  titanium.** stays a bold run-in: its passage is 113 words, under the 120 an H3 needs.
* **Lead:** base 128 words → two paragraphs at "This reference describes the stack".
* **R-PARA/R-SENTENCE:** the 174-word Cypress paragraph in three (sources | 2013 report and PDK
  match | 2014 report and older reports); the 15-word S8P parenthetical moved, unchanged, to directly
  after its sentence as "(The S8P entry reads … "500A TiW/21,250A Al 0.5% Cu/300A
  TiW".[^cyp-qtp-123907])" — marker repeated (it is that report's content), declared; this is the
  one `number_order` LOST, ('2014','4','3','0.5','1','0.5'): the same numbers, the parenthetical's
  metal-3 figures now after the metal-1 quotation. "Which of the two stacks …" (52 words) split at its
  colon; `[^cyp-pin145273]` repeated on the first half, whose claim (metal 1 is among the levels the
  2014 change reaches) rests on that notification (declared). "Against that, …" split at ", and
  SkyWater's" — "(our arithmetic)" belongs to the first clause. Sheet-resistance sentence split at its
  colon and at ", and since" ("Since the Ti and TiW films conduct in parallel, the alloy …" — the
  "Because X, Y" form; comma added). "This page describes …" and "The PDK's metal-1 …" are their own
  paragraphs. Bottom-titanium paragraph split before "A cobalt–titanium bilayer".
* **R-CATEGORY:** classification cut at its semicolon (12 words) with the category-page sentence;
  "What is specific to this instance is that it is … and that the three films …" → "… is that:" and
  two plain bullets (R-LIST on "that X and that Y"; "and that" dropped).
* **R-LIST (Why):** Ti underlayer "does three things:" → three sub-bullets; the 16-word "(industry
  practice; Domenicucci …)" parenthetical closed as its own sentence (R-SENTENCE step 7). TiW cap: the
  three studies as plain sub-bullets under "… long before TiN:"; "serves as X, as Y, as Z, and as W"
  → "On top of the alloy the TiW serves:" and four sub-bullets ("it" → "the TiW": the paragraph now
  follows the Olowolafe bullet). Al–Cu: lead + two continuation paragraphs, split at "since;".
* **How:** italic scope lead-in (it carries `[^cyp-qtp-113005]`; the marker stays inside). Al–Cu item
  lead + continuation, split at "relations;". Cap item: the first sentence stays whole as the lead
  ("On the Ti/Al–Cu/TiW reading" scopes all of it, including "thickness per the 2013 Cypress
  report"); the 2014 alternative is the continuation.
* **R-TOOLS:** AMAT item in three lines. Metal-etcher item: the head sentence (SkyWater's words plus
  this reference's gloss, no seam) stays whole; "(strength: strong for the material set, used at
  MM1E)" → *Tool exists:* strong for the material set, used at MM1E.
* **R-OPENQ, R-RELATED, R-GLANCE:** three labels; the stack question split into its question and an
  indented continuation (R-OPENQ step 2). Previous / Next split, Depends on, Feeds, Same category.
  The glance does not choose a stack: "the three films this page describes", "which of the two public
  stacks SKY130 carries".
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `cyp-pin145273`,
  `cyp-qtp-123907` (the two repeats above), `pdk-04`, `pdk-08`, `skw-01`, quote "Collimated Ti",
  numbers 0.36, 125, hedges "likely", "not public", identifiers — glance. LOST words "strength"×2
  (R-TOOLS), "and"×2 (the "and that" and ", and since" splits), "it" (→ "the TiW").
* **Coverage flags read:** list items whose marker is on a sibling; the sheet-resistance and
  "Against that" splits (each hedge stays with its clause); the Rocke roles (the marker stays with the
  anti-reflective role it supports). None lost a marker or hedge.
* **Left over the caps:** item lead blocks over 30 words — TiW cap (26 + the dash parenthetical, fine),
  Cap (40; one sentence under one hedge). Nothing over the §1 caps.

### 113 MM1 — done

* **Kept verbatim:** the lead and the "film under the resist" sentences that open with the TiW stack
  of the 2013 report and give the TiN alternative (the S8 figure agent's note); only a semicolon split
  ("… 0.36 µm in all.[^pdk-04] A 2014 report records …").
* **R-H3:** `### What the public record shows` over the post-figure passage (rules, CD table, Cypress
  stack).
* **R-TABLE:** m1.1–m1.7 and m1.pd.1 → `Rule | Constrains | Value`, unit in each cell (µm, µm² and a
  bare 0.7), `[^pdk-periph]` on the lead-in "The periphery rules give:"; "— a 0.28 µm pitch" kept in
  the m1.2 cell; the waffle-drop clause as a sentence after the table ("The layer also carries a
  waffle-drop fill algorithm …[^pdk-periph]"). number_order LOST hand-checked against the rows: m1.1
  0.140, m1.2 0.140 (0.28 pitch), m1.3a/b 0.280, m1.4 0.030, m1.5 0.060, m1.6 0.083 µm², m1.7
  0.140 µm², m1.pd.1 0.7; 700 in the sentence. Words "by", "with" lost to the cells.
* **R-SENTENCE:** the 15-word `LI1MCD` parenthetical split at its semicolon; its second half closed as
  "(The table's second `LI1MCD` row gives 0.17 µm.[^pdk-03])" — marker repeated, declared.
* **R-CATEGORY:** classification (13 words), then **Specific to this step:** with four bullets: the
  k₁ passage (split at its colon and at ", and only NA 0.80" → "Only NA 0.80 …"; the k₁ formula stays
  inline as on 107 and 061), the ITRS quotation, "We infer …" (split at ", and we infer"), the
  substrate sentence. Bullets group sentences by topic (the k₁ bullet holds three) rather than one
  per sentence, so that "Only NA 0.80 lifts it" stays with the value it lifts.
* **R-PARA/R-LIST (Why, How):** Line width: split at ", and the space" and at "layer;". Resist–
  substrate: the studies as two plain sub-bullets under the colon lead. Surface preparation: lead ends
  at "cluster;"; the cap dash material becomes its own sentence, and `[^brunner-1991][^wiki-arc]` move
  to the end of the BARC clause they support (swing-curve BARC), `[^cyp-…]` stay with the caps.
  Exposure: split at "reticle;".
* **R-TOOLS, R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** as on 107 ("*SkyWater says:* lists both" — the
  guide's own form); three labels; Previous / Next split, Depends on / Feeds from the bullet that named
  both, Same category (the masks), Mask; italic scope lead-in.
* **check_preserved (`--allow-regrouped --strict-words`):** ADDED markers `pdk-03` (repeat) and the
  glance (`pdk-04`, `pdk-periph`×2, `skw-01`); ADDED numbers `1`×3/`2` ("metal 1" in cells and the
  glance's m1.1/m1.2), 0.140, 0.28, 0.36 (glance); ref `step-114`, hedges — glance. LOST words
  "page" (Mask page → Mask), "strength"×3, "by", "with".
* **Coverage flags read:** table rows and studies sub-bullets (markers on the lead-in or their own
  line); the k₁ and ITRS splits (each sentence keeps its own markers). None lost a marker or hedge.
* **Left over the caps:** Exposure item lead (36 words, one sentence whose dash pair is an
  attribution). Nothing over the §1 caps.

### 114 MM1E — done

* **Kept verbatim** (the S8 figure agent's note): "the spaces it opens — 0.14 µm wide and 0.36 µm
  deep" (no marker; the page defines no `[^pdk-04]`) and "the 0.36 µm stack clears in well under a
  minute" stay as written — see Content problems. Both stack descriptions keep their wording.
* **R-H3:** none (the post-figure passage is under 120 words).
* **Lead:** base 151 words → three paragraphs (§4.1 note ¹). The 105-word second sentence: its dash
  material (the two stacks) becomes two sentences after the main one — "The stack is, on the 2013
  Cypress description …[^cyp-qtp-113005] On the stack qualified in 2013–2014, it is 500 Å …
  [^cyp-qtp-123907] (…)" ("The stack is", "it is" added by the split); ", so that what remains"
  → ". So what remains" (the ", so" split form). This reorder is the one `number_order` LOST: the
  stack figures now follow the `met1` numbers (68:20, 0.140); every number is present, hand-checked.
* **R-CATEGORY:** classification ends after "(MM2E to MM5E)" (29 words); "What is specific to metal 1 …"
  is its own label (step 3), a paragraph; "What is specific to the class is that X, and that Y" →
  "… is that:[^hess-1982][^nojiri-2015]" and two plain bullets (the markers ended the enumerating
  sentence, so they sit on the lead-in, R-LIST step 1).
* **R-LIST/R-PARA (Why):** "The films etch differently:" → four sub-bullets, each with its own
  marker; the copper-chloride clause stays with the Al–Cu bullet it qualifies (a paragraph may not
  open on "but"). Charging: lead ends at "damage:".
* **How:** Chamber lead + continuation. BARC and cap open: split before "A TiW cap"; the dash pair's
  closing "— while a TiN cap" → ". A TiN cap" (the contrast stays readable from the parallel
  sentences; "while" lost). Main etch: lead + continuation; the source's line break after "boron-"
  (rendered "boron- chloride") joined. Strip and clean: the ash-tool dash material and the 14-word
  solvent parenthetical move, unchanged, to directly after the sentence, as on 108. Metrology: the
  test-tile sentence as a continuation.
* **R-TOOLS:** both items in the three-line form; "(inference)" for the 2300 stays with its clause.
* **R-REPEAT:** considered for the two Lam quotations in the post-figure paragraph and under Machines
  likely used; **not applied** — the lead copy adds "two metal etchers by name" and "whose material
  lists match this stack" (batch-7b ruling D1).
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** four labels; Previous / Next split, Depends on, Feeds
  (VIME), Same category; italic scope lead-in.
* **check_preserved (`--allow-regrouped --strict-words`):** every ADDED line is the glance box. LOST
  words "strength"×2 (R-TOOLS), "that"×2 (", so that", "and that"), "while".
* **Coverage flags read:** the stack sentences took their own markers with them; the Complete
  clearing and class bullets carry their own or the lead-in's markers. None lost a marker or hedge.
* **Left over the caps:** Metrology item lead (35 words, a list of methods in one sentence). Nothing
  over the §1 caps.

### 115 NILD3 — done

* **R-H3:** none (the post-figure passage is this reference's reading of two PDK hints; no title
  fits, and it is now a list).
* **Lead:** base 168 words → three paragraphs (description | the PDK's name and labels | the level
  arithmetic). The line dimensions in the dash pair become their own sentence after the main one:
  "The lines are 0.36 µm tall,[^pdk-04] as close as 0.14 µm apart.[^pdk-periph]" (subject and verb
  added). The level sentence split at ", so": "… 2.0061 µm.[^pdk-04] So the finished dielectric … is on
  our reading about 0.63 µm …" — the hedge sits in the second half and stays there; the first half is
  what the diagram labels. Arithmetic checked: 2.0061 − 1.3761 = 0.63; 0.63 − 0.36 = 0.27.
* **R-LIST:** "Two public hints shape our reading of the film:" → two bullets, their opening words bolded
  in place (R-LIST step 3); "(inference)" and "on our reading" stay in their own bullets. Step
  category: the two routes as plain bullets. Why/Mechanical: "The oxide must not crack, must not …,
  and must not …" → "The oxide:" and three "must not" sub-bullets (every word kept but "and").
* **R-CATEGORY:** classification (11 words); the relatives sentence (lists other steps) as a
  paragraph; "What is specific to this instance is the gap." (its own label) then "It is 0.14 µm wide,
  …" (subject and verb added; 46 words otherwise); the category-page sentence with its list.
* **R-PARA/R-SENTENCE:** Why: Insulation lead + continuation (the source's "deposition/" line break,
  rendered "deposition/ sputter", joined); Capacitance and Overburden split at their semicolons.
  How: Liner and HDP items lead + continuation.
* **R-TOOLS:** HDP item: *SkyWater says:* holds the two SkyWater statements (`[^skw-01]`, and the
  maintenance page `[^skw-07]`); this reference's gloss "— the 2.6:1 gap here is well inside it —" is
  separable at its dashes, so it goes to the continuation after the grades, with its noun back ("well
  inside that capability"; R-TOOLS: a continuation does not open on a bare pronoun), followed by the
  model sentence. TEOS item in grade lines. The silane-oxide bullet has no "Strength:"; unchanged.
* **R-REPEAT:** the HDP quotation also appears under How (step 2); **not applied** — that copy adds
  "a maintenance-page photograph" (ruling D1).
* **R-OPENQ, R-RELATED, R-HEDGE, R-GLANCE:** four labels; Previous / Next split, Depends on (the
  dielectric below), the two remaining bullets merged under Same category; italic scope lead-in.
* **check_preserved (`--allow-regrouped --strict-words`):** every ADDED line is the glance box (PDK
  labels 4.5, 3.5, 0.030 µm, 0.27 µm with `[^pdk-04]`; `skw-01`; ref `step-116`; hedges). LOST words
  "strength"×2.
* **Coverage flags read:** the line-dimension and level splits (markers moved with their clauses);
  "must not crack;" (no marker in the base either). None lost a marker or hedge.
* **Left over the caps:** lead 169 words in three paragraphs (base 168). Item leads: Liner (35 words,
  two parentheticals), HDP gap fill (40). Nothing over the §1 caps.
