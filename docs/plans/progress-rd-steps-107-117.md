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
