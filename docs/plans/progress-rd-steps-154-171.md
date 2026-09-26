# Progress — readability batch 12, steps 154–171 (`topic/rd-steps-154-171`)

Writer: Opus. Started 2026-09-27 from `main` at `773b9dbe`. Guide: `docs/plans/readability-guide.md`
§1, §2, §4.1, §5, §6, §7, §8, with the rulings of batches 4–11 (plain bullets over invented labels; no
H3 where none of the four titles fits; R-CATEGORY's 35 words a target; the connective rule inside list
items; derivations under 120 words as a numbered list without an H3; a third lead paragraph only for
base leads over 120 words; "Because X, Y" is not a connective opener; rows differing in unit carry the
unit in each cell; R-REPEAT only when the other copy adds nothing; no hand-inserted non-breaking
spaces; "What is specific … is (that) X, and (that) Y" over the cap → "… is (that):" and one bullet per
clause; one bullet per topic where a pronoun needs its antecedent; a hyphen or slash at a source line
break joined; a blank line after the glance box's closing `:::`; hedge scope at a semicolon split per
R-SENTENCE step 5; a lead within 120 words stays within 120, zero-word forms first; the gloss and
", though" forms of R-SENTENCE step 7; R-CATEGORY step 3 with elaborating sentences). Medium classes
avoided (batch 4–11 reviews): a pronoun whose referent changes after a split; a marker lost when dash
material moves; a sentence moved below the grade that refers to it; glance wording that strengthens a
grade; a whole-sentence trailing hedge not repeated on every half of a split; an added subject that
takes a lead over its cap. Model pages: 139, 140 (batch 10) and 141–149 (batch 11). One commit per
page. No edit of any kind inside an in-force `{dropdown}`.

## Method, every page

* Baseline build and one desktop tile set per page before any edit (`tmp/shots/*-before*`,
  git-ignored); one final pair (1280 px, `--max-height 40000`; 400 px, `--max-height 60000`) after.
* Preservation: `uv run python tools/check_preserved.py --base <commit before the page>
  --allow-regrouped <page>`, no other flag; never `--allow-added`, never `--allow-dropdown-edits`.
  Every ADDED line outside the glance box is named in the page entry; every REGROUPED and
  `number_order` LOST line read and re-paired by hand; `--strict-words` as the final run, every LOST
  word named.
* Marker coverage: `tmp/readability/rdtools.py cov` (git-ignored scratch script) pairs every
  sentence not verbatim in the base — split at full stops **and semicolons** — with its closest base
  sentence and flags any marker or hedge word the base sentence had and the new one (with its ±2
  neighbours) lacks. Every flag read.
* Invariants: `rdtools.py inv` against the base: References section, footnote definitions, generated
  index-links block, `{figure}` blocks, `{dropdown}` blocks, quick-facts rows, H2 list and Deep-dive
  count identical; one admonition (the glance box) followed by a blank line; no duplicate H3; every
  glance marker recurs below; the How scope sentence is the italic lead-in; no consecutive duplicate
  line, no prose line ending in a hyphen or slash, no bare `>`, no NBSP change.
* Caps: `rdtools.py caps` at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25) with
  `{figure}` blocks (captions), `{dropdown}` bodies, the generated block, `## References` and footnote
  definitions **excluded**; a leading bold run-in or italic R-TOOLS label is not counted into its
  sentence; a quotation and a code span count as one word; an em dash is not a word.
* Gates per page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`, `-W` build.

## Pages

### 154 MM4 — done (base `773b9dbe`)

* Lead (base 127 words, one paragraph): three paragraphs (36, 46, 45); the 46-word "As at MM3 …"
  sentence split at its colon (no word added). First sentence 5 words.
* R-H3 + R-TABLE: `### What the public record shows` after the figure caption over the PDK passage
  (≈ 245 words, public record ending in a hedged fuse reading, 139 form). The periphery-rule sentence
  became a `Rule | Constrains | Value` table (139/144 form), rows in base order; the `cmm4 waffleDrop`
  fill check has no rule id or value in the base, so both cells are `—`. `number_order` LOST line
  re-paired by hand: m4.1 0.300 µm · m4.2 0.300 µm · m4.5a, m4.5b 0.400 µm · m4.4a 0.240 µm² · m4.3
  0.065 µm · m4.pd.1 0.7, 700 µm windows, 70 µm steps · fill check — · via4.4 0.190 µm. The lead-in
  "The periphery rules give:[^pdk-periph]" carries the base sentence's only marker. Via4.4 cell
  reworded from "the via-4 openings that will land on metal 4 must be enclosed by it by" to
  "enclosure, by metal 4, of the via-4 openings that will land on it" (144's form; words lost
  `must`, `be`, `enclosed`).
* Fuse sentence (49 words) split at ", and give": "They give fuses …"; `[^pdk-periph]` repeated on
  the first half (declared marker), since the base's single marker covered both clauses.
* R-CATEGORY (139 form): classification sentence alone, then **Specific to this step:** with two
  bullets. The 49-word k₁ sentence split at ", and on an i-line"; "(our arithmetic)" repeated on the
  248 nm half (declared hedge). The SkyWater sentence split at its semicolon. The "What is specific …
  is the substrate, and it is …" sentence (70 words) split at the clause with its own subject; the
  two substrates as two bullets; the closing apposition "two thin-film stacks …" became "These are two
  thin-film stacks …" (declared subject, "These are").
* Why: overlay item split at ", so" ("So whether `MM4` aligns …"); its "(inference; …)" stays on the
  So-sentence, which is the clause the page's Open-questions bullet ("The alignment tree — to via 3, to
  `cap2m`, or both — … not public") ties it to; the first half is cited (`pdk-periph`) or a flow fact.
  Reflectivity item split at its semicolon; each half keeps its own hedge.
* How: scope sentence italic. Step 1 split at its semicolon and before "then an organic BARC" (the
  base's own "then", capitalised); "(inference)" stays with the HMDS clause it closes, the markers with
  the BARC clause. Step 5: the 18-word hedge parenthetical became its own parenthetical sentence
  directly after the sentence it qualified (R-SENTENCE step 7); the "whether … cap2m plate edges"
  sentence is an indented continuation paragraph.
* R-TOOLS (three items, 139 form); R-RELATED (Previous · Next · Depends on · Feeds · Same category ·
  Mask · Category page; "Mask page:" → "Mask:", word `page` lost); R-OPENQ labels on five bullets.
* Glance box (139 form).
* `check_preserved --allow-regrouped`: ADDED only in the glance box, plus the declared
  `pdk-periph` (fuse split), "(our arithmetic)", "These are", the H3, the table header and the
  Open-questions labels. `--strict-words` LOST: `enclosed`, `must`, `page`, `strength`×3. cov: no
  flag. inv: OK.

### 155 MM4E — done (base `e3ce1328`)

* Lead (base 149, one paragraph): two paragraphs (89, 65), 140 form. The 65-word "Through the resist
  … a chlorine plasma removes everything …" sentence split after "via-3 level" with "It removes first
  …" (declared "It removes"; "It" = the chlorine plasma, the subject of the sentence before); the dash
  material became "The stack is a refractory cap, … bottom layer on our reading." (declared "The stack
  is"; the hedge "on our reading" travels with it). The chlorine-plasma wording is kept verbatim (see
  content problems).
* `**How thick is the metal?**` → `### How thick is the metal?` (140 form), in three paragraphs. The
  65-word Fab 4 sentence: its dash pair became a colon, "— which is why" → ". That is why" (the
  gloss rule's which → That; word `which` lost, `that` added), and the semicolon a full stop.
* R-CATEGORY: classification sentence alone; the MM1E chemistry pointer as its own paragraph (140
  form); **Specific to this step:** with the geometry and breakthrough sentences as two bullets; the
  bullet-opening "And" dropped (140's form; word `and` lost).
* Why: line-width item split after its 28-word lead sentence (continuation paragraph, semicolon →
  full stop). Breakthrough item: semicolon → full stop; the dash material after "the cap together"
  became the continuation paragraph ("Fluorocarbon …", capitalised); the 20-word trailing hedge
  "(inference from the stack; the Newport Fab patent …)" became its own parenthetical sentence
  directly after the stringer sentence it closed (R-SENTENCE step 7, 140 form). Charging item split at
  its semicolon (the "(inference from the PDK's stacked cross-section)" sits before the semicolon, on
  the first clause, as in the base), studies as a continuation paragraph.
* How: scope sentence italic. Step 7: the two dash asides (SkyWater's strippers and solvents) moved,
  unchanged, to after the sentence they interrupted (140 form), each closed with a full stop; the
  "(inference)" stays on "benign to the exposed plate edges". Step 8: test-tile sentence as a
  continuation paragraph.
* R-TOOLS (two items, 140 form). Resources: "(industry practice;[^nojiri-2015] SkyWater lists … [^skw-01])"
  → "(industry practice[^nojiri-2015]). SkyWater lists … etchers.[^skw-01]" (140 form). R-RELATED (140
  labels). R-OPENQ: labels on four bullets; the thickness bullet split at its semicolon, the cap
  question as a continuation paragraph.
* Glance box (140 form).
* `check_preserved --allow-regrouped`: every ADDED line is in the glance box, plus the declared "It
  removes", "The stack is", "That is why", the H3, "Specific to this step" and the labels. Every
  `number_order` change is REGROUPED (the Fab 4 sentence); read, same digits. `--strict-words` LOST:
  `strength`×2 (and, masked by glance words, `which` → `That`, `and`). cov: three flags, all pairing
  noise (the quick-facts table; the moved step-7 asides keep their `skw-01` markers). inv: OK.

### 156 NILD6 — done (base `0b90fee3`)

* Lead (base 184, one paragraph; its 100-word second sentence carried two dash asides): three
  paragraphs (80, 34, 74). The main clause stays whole ("Over the freshly etched metal-4 lines of MM4E
  and over the second-level MiM capacitors on some of them, a silicon dioxide film is deposited thick
  enough …"); the semicolon clause "CMPM4 polishes it flat …" follows as its own sentence ("it" is
  still the film, the subject before it); the two dash asides follow in their base order: "The lines
  are 0.845 µm tall …" (declared "The lines are", 141 form) and "The diagram's k = 4.0 … (inference)."
  as its own paragraph, the trailing "(inference)" on the whole aside as in the base. The 59-word
  diagram sentence split before "places": "… and draws no separate "_C" film beside it.[^pdk-04] It
  places …" (declared: repeated `pdk-04`, "It" = the diagram; 141 repeated the same marker).
* Post-figure paragraph split before "The surface also carries …"; its colon became a full stop.
* R-CATEGORY (141 form): classification sentence alone ("…, which sets out" → ". NILD3 sets out",
  declared restored noun; word `which` lost); the two routes as bullets; the SkyWater sentences as a
  paragraph; "What is specific …, is the larger … and the fact that …" → "… is:" with two bullets
  (every word kept but the joining "and").
* Why: four items split at their semicolons or colon (void fill, capacitor charging, capacitance, via
  4, overburden), the first two with a continuation paragraph; every marker and hedge stays with its
  clause ("on our reading" in the overburden item is in its own half).
* How: scope sentence italic; step 1 split at its semicolon.
* R-TOOLS (141 form; the model sentence as a continuation paragraph after the grades). R-RELATED
  (Previous · Next · Same module: 150–163 share the Phase cell · Same category · Category page).
  R-OPENQ labels on four bullets. Glance box (141 form).
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared `pdk-04`, "The
  lines are", "It", "NILD3", the labels and "Specific"; every `number_order` change REGROUPED, read.
  `--strict-words` LOST: `strength`×2 (and `which`). cov: three flags, all pairing noise. inv: OK.

### 157 CMPM4 — done (base `f6daf15a`)

* Lead (base 144): two paragraphs (93, 51) split before "As at CMPM …" (142 form). First sentence 10.
* Post-figure paragraph: the rules sentence (65 words) → "The PDK's metal-4 rules are written around
  this polish:" and two bullets split at its semicolon (142 form); each bullet keeps its own marker.
* R-CATEGORY (142 form): classification sentence alone; the CMPM/CMPM3 pointer as a paragraph; "Two
  things are specific to this instance." → colon and two bullets. The second bullet dropped its
  opening "And," and, being 46 words, was split before "with no plug polish": "… sputtered into it
  (inference). There is no plug polish afterwards …" (declared: "There is", the repeated
  "(inference)"; word `with` lost). The leading "On our reading of the via-4 rules and the fill reading
  …" stays on the first half, the second half carries the base's "(inference)".
* Why: planarity, capacitor and pattern-density items split with a continuation paragraph (142
  form). Via-4 depth item split at ", and the aluminium deposition …" (word `and` lost): the trailing
  "(inference, on the fill reading at WTIAL5)" stays with the second sentence, which holds the fill
  reading ("the aluminium deposition that follows fills the hole directly"); the first sentence is the
  etch requirement 142 states unhedged ("must clear the full dielectric … while stopping on the
  shallower plates").
* How: scope sentence italic; the Recipe item split after the Nanz and Camilletti sentence
  (continuation paragraph).
* R-TOOLS: Mirra (three lines); defect inspection "Strength: medium." → "*Tool exists:* medium." (142
  form); the post-CMP clean item has no grade and is unchanged. R-RELATED (142 labels). R-OPENQ
  labels on five bullets. Glance box (142 form).
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared "(inference)",
  "There is", "Two things … :" colon, labels; every `number_order` change REGROUPED, read.
  `--strict-words` LOST: `strength`×2 (and `with`, `and`, `And`). cov: one flag (quick-facts pairing
  noise). inv: OK.
* Follow-up (parenthetical scan added to `rdtools.py caps`): two parentheticals of ≥ 12 words left in
  the first pass now stand as parenthetical sentences directly after the sentence they belong to
  (R-SENTENCE step 7): the lead's "(The category page sets out the slurry chemistry; SKY130's is not
  public.)" (pointer plus hedge on the slurry, which the sentence before names) and the post-figure
  "(VIM4E, WTIAL5, where the reading of how via 4 is filled is set out.)" (a gloss). Words unchanged.

### 158 NCAPOX6 — done (base `ac8770da`)

* Lead (base 135): two paragraphs (90, 45) split before "The finished number is public" (143 form).
* Post-figure paragraph split before "What the cap prepares for"; its 71-word sentence split at ", and,
  on the via-4 fill reading" ("On the via-4 fill reading …, the surface this cap leaves is … (inference)").
  The trailing "(inference)" stays on that half: its own leading words name its basis (the fill
  reading), and the other half is cited (`pdk-periph`) or hedged ("our arithmetic"); the 0.505 µm depth
  is the lead's PDK value.
* R-CATEGORY (143 form): classification sentence alone to its closing dash; "and, like its
  predecessors, …" → "It is, like its predecessors, …" (declared "It is", 143 form); "What is specific
  … is that X, and that Y" → "… is that:" and two bullets (words `and`, `that` lost).
* Why: thickness item with a continuation paragraph; the 13-word trailing hedge of the cover item as
  a parenthetical sentence ("(Inference from the construction; …)"); sealing item split after "a fresh
  plasma oxide buries them" (continuation paragraph) and its colon → full stop; the unindented last
  line of the lithography item indented (whitespace only).
* How: scope sentence italic. Step 2 split after the Chapple-Sokol sentence (continuation paragraph)
  and at its semicolon ("Neither says …"; "(inference)" stays in its own sentence, as in the base).
  Step 4: the 12-word parenthetical split at its own semicolon: "(textbook value[^txt-05])" stays on
  the 650–750 °C number it qualifies; the attribution "(Adams and Capio and Becker et al.
  characterise the process.[^adams-1979][^becker-1987])" follows the sentence as a parenthetical
  sentence. Step 5: the 13-word trailing hedge as a parenthetical sentence.
* R-TOOLS: "SkyWater lists it with …" → "*SkyWater says:* lists PECVD TEOS with …" (the pronoun
  replaced by the tool's name, R-TOOLS step 2); C1 item graded in two lines. R-RELATED (143 labels).
  R-OPENQ labels on four bullets. Glance box (143 form; "on the reading this reference applies to each
  cap oxide" kept from the lead).
* `check_preserved --allow-regrouped`: ADDED outside the glance only "It is", labels; every
  `number_order` change REGROUPED, read. `--strict-words` LOST: `strength`×2 (and `that`, `and`,
  `it`). cov: two flags, pairing noise. inv: OK.

### 159 VIM4 — done (base `633e4126`)

* Lead (base 107, one paragraph, first sentence 32 words): "`VIM4` is the via-4 lithography: the
  mask step that defines …" → "`VIM4` is the via-4 lithography. It is the mask step that defines …"
  (144 form; declared "It is"). **Listed under note ¹ of §4.1:** no zero-word form exists (the colon
  clause is a noun phrase with no verb of its own); the lead goes 107 → 109, within 120. Two
  paragraphs (64, 45), split before "The holes are etched …". First sentence 5 words.
* R-H3: `### What the public record shows` after the figure caption (144 form) over the PDK passage
  (≈ 300 words). The pad-via sentence split at its semicolon. R-TABLE: the via-4 rule sentence →
  lead-in "The periphery rules define via 4 narrowly ("Via4 connects met4 to met5 in the
  SKY130P*/SP8P* flow"):[^pdk-periph]" (the base's own sentence and quotation, the full stop between
  them now a parenthesis) and a `Rule | Constrains | Value` table; via4.3 has no value in the base
  (`—`). The x.2 clause follows the table as its own sentence with the base's marker; the lead-in
  carries a repeated `pdk-periph` (declared). `number_order` LOST line re-paired by hand: via4.1
  0.800 µm · via4.2 0.800 µm · via4.3 — · via4.4 0.190 µm (metal 4) · m5.3 0.310 µm (metal 5) · x.2
  90°. Cell rewording "metal 4 must enclose the via by" → "enclosure of the via by metal 4" (144's
  form; words `must`, `enclose` lost).
* The 101-word area sentence: "A via 4 has sixteen times … (our arithmetic from via3.1 and
  via4.1[^pdk-periph]), so area alone would account for …" kept as one sentence; the 19-word
  parenthetical split at its own semicolon, its second half "(The rules also allow a 0.800 µm square
  via 3 inside `areaid.mt`, via3.1a.[^pdk-periph])" a parenthetical sentence after it (R-SENTENCE step
  7, gloss); the dash material "Scaled by area alone … (our arithmetic)." its own sentence directly
  after; "Interface and liner terms … (inference)." at the semicolon, as its own short paragraph.
  R-DERIVATION not applied: the page states the results (sixteen times, 213 mΩ, 1.8 times) without
  writing out an operation (the 001 ruling).
* R-CATEGORY (144 form, no label: the section already carries its own "What is specific …"
  paragraph): classification sentence alone; the 60-word i-line sentence split at ", and ASML
  describes" and at its semicolon (word `and` lost); Sheet4 paragraph split at its colon and before
  "We also read a digit 4"; the "What is specific" paragraph's 100-word sentence split at its colon
  and semicolon ("On our reading (see WTIAL5), … can enter." / "Skelly and Gruenke found …[^skelly-1986]"
  / "Their result is not … (inference)."); each half keeps its own hedge or marker; the Bär/Kim
  simulations and the via4.3 sentence as a third paragraph.
* Why: hole-size item in three blocks (lead, fill, taper) split at its semicolon and colon; arrays
  item split at its semicolon with `[^pdk-periph]` repeated on the first half (declared: the base's
  single marker covered both clauses — "only one via size is allowed" is via4.1/via4.3) and at the Le
  semicolon.
* How: scope sentence italic. Step 2: the 15-word trailing hedge "(Inference from the KrF reading; on
  an i-line tool it would be a DNQ/novolac resist.[^dammel-1993][^reichmanis-1989])" a parenthetical
  sentence directly after the resist it qualifies; the rest a continuation paragraph. Step 3 split at
  its semicolon (continuation paragraph).
* R-TOOLS (144 form); the "SkyWater also lists "ASML I-line …" …, which … would otherwise suggest"
  sentence is this reference's argument around the grade and stays whole as the continuation
  paragraph after the grades. R-RELATED (144 labels; the base's separate "The mask types recorded for
  vias 2–4" bullet joined to the Mask bullet — both are mask links). R-OPENQ labels on six bullets;
  the mask-type bullet split at its semicolon (continuation paragraph).
* Glance box (144 form).
* `check_preserved --allow-regrouped`: the one LOST line is the rule table above; ADDED outside the
  glance only the declared `pdk-periph`×2, "It is", the H3, the table header and labels; every other
  `number_order` change REGROUPED, read. `--strict-words` LOST: `enclose`, `must`, `page`,
  `strength`×3. cov: two flags, pairing noise. inv: OK.

### 160 VIM4E — done (base `0d0692de`)

* Lead (base 121): 145 form — "… down to two kinds of floor:" and the two floors as bullets (the
  joining ", and" dropped; the first floor now ends at its own marker with a semicolon), then the
  strip sentence as a paragraph. Three blocks (30, 63, 27 words), total 120. The metal-cap and plate
  floors are kept verbatim (see content problems).
* Post-figure paragraph split before "The geometry is forgiving".
* R-CATEGORY (145 form, no label; the section has its own "Two things are specific" sentence): the
  62-word classification sentence split at its semicolon; "VIME sets out the class — … — and CTME
  the surface chemistry." → "VIME sets out the class: … stop on time. CTME sets out the surface
  chemistry.[^flamm-1981][^winters-1992]" (the dash aside kept in place after a colon; "sets out"
  restored in the gapped clause, 145 form; word `and` lost). "Two things are specific to this
  instance." → colon and two bullets; bullet 1's 12-word trailing hedge a parenthetical sentence
  ("(Inference from the geometry; Wodecki …[^wodecki-1999])"), covering the whole sentence as before;
  bullet 2 drops its opening "And" and its dash list becomes a continuation paragraph ("The Motorola
  patent …, and the Chartered patent ….[^pat-taper-chartered] Bär, Lorenz and Ryssel and Kim and Lee
  simulate …"; a comma and "and" moved; each patent keeps its marker).
* Why: clean-landing item — lead sentence, then Bui's finding with its dash apposition as "This is a
  finding about cap thickness …" (declared "This is") and the fill-reading sentence at the semicolon
  (its hedge unchanged, indentation restored); punch-through item in three blocks, the patent
  sentence split at its semicolon with `[^pat-etchstop-ti]` repeated on the first half (declared,
  145 form); charging item split at its semicolon.
* How: scope sentence italic; step 4 split at its semicolon; step 6: the two dash asides (SkyWater's
  strippers and solvents) moved, unchanged, after the sentence they interrupted (155/140 form), the
  "(inference)" still on the peroxide clause; step 8's test-tile sentence a continuation paragraph.
* R-TOOLS (145 form for the no-etcher item: the "weak" grade as *Runs this step:*; the strip/clean
  item graded in two lines). Resources: "(industry practice;[^nojiri-2015] SkyWater lists …[^skw-01])"
  → 140 form; the solvent half of the ash/solvent bullet a continuation paragraph, its 29-word
  parenthetical split: "({ref} wet chemicals; EKC270 and, we read, EKC265)" stays inline, the
  gloss "(SkyWater's list prints "EKS265, EKC270 solvents";[^skw-01] the EKC265/EKC270 … is ours.)"
  follows the sentence as a parenthetical sentence (R-SENTENCE step 7). R-RELATED (145 labels).
  R-OPENQ labels on five bullets. Glance box (145 form, "none named … **weak**").
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared
  `pat-etchstop-ti`, "This is", labels. It also prints `DUPLICATED sentence (2x, was 1x): 'The step
  list used in this reference has no separate strip step after `VIM4E`; this page treats the resist
  strip and cle…'` — a false positive: the base already has the sentence twice (lead and Open
  questions, `git show 0d0692de:docs/steps/160-vim4e.md | grep -c` → 2); the lead copy now stands as
  its own paragraph, where the tool's splitter sees it. Nothing was duplicated. `--strict-words`
  LOST: `strength`×2 (and `and`×2, `And`). cov: one flag, pairing noise. inv: OK.

### 161 WTIAL5 — done (base `c7ecd398`)

* Lead (base 101, within 120, first sentence 21): two paragraphs (61, 41) split at the semicolon
  after "titanium–tungsten cap"; the following "the MM5 mask and MM5E etch then pattern it" → "The MM5
  mask … then pattern the stack" (declared restored noun: after the split the nearest noun to "it" is
  the cap, while the base's "it" is the film stack — the 149 M1 class). **Listed under note ¹ of
  §4.1:** the lead goes 101 → 102, within 120; no zero-word form keeps the referent.
* R-H3: `### What the public record shows` after the figure caption over the PDK and Cypress
  passage (≈ 420 words, public record ending in the page's hedged stack reading, 134/149 form); the
  bold run-in `**How is via 4 filled?**` → `### How is via 4 filled?` (R-H3 step 4).
* PDK paragraph: the 86-word sentence split at its three semicolons (words `and` lost); the
  resistivity sentence split at ", whereas" (word `whereas` lost) with "(our arithmetic)" repeated on
  the 5.7 µΩ·cm half (declared; the base's hedge covered the whole comparison) and at its semicolon.
  The rule sentence stays prose (149 form).
* Cypress paragraph: split at ", so on the reading …" ("So on the reading …", its "(inference)"
  in its own half; the first half is the cited quotation) and into three paragraphs; the 29-word
  hedge "(inference: the S8P line above, SkyWater's PVD film list, …[^skw-01] and the fit …)" a
  parenthetical sentence directly after the sentence it qualifies.
* Via-4 bullets: geometry item — "an aspect ratio of about 0.63:1, while the metal-5 stack …
  (our arithmetic)" split with "(our arithmetic)" repeated on the aspect-ratio half (declared; word
  `while` lost); Skelly and Taylor as continuation paragraphs (159 form). Techniques item: its
  142-word colon-and-semicolon enumeration → lead "… by Gn, Liu and Guo:[^gn-1994]" and four
  sub-bullets in base order (word `and` before Electrotech lost), the tapered-walls sentence a
  continuation paragraph. The first sub-bullet (59 words) split before Hariu: "(… via
  fill).[^ono-1990][^nishimura-1991] Hariu et al. measured the electromigration lifetime …
  bias;[^hariu-1989]" — the base's three-marker run divided among the three studies it cites, each
  marker with its own author; "measuring" → "measured" (the only verb-form change of the batch; no
  other form keeps the sub-bullet under 45 words).
* Closing paragraph: "…, which argues for the gentler options (…) (inference)" → ". That argues …
  (inference)" (which → That); the "(inference)" stays on the argument: the first half carries its
  own hedge and citation ("industry-typical[^txt-05]") (R-SENTENCE step 5, second paragraph).
* R-CATEGORY (149 form): classification sentence alone; TIAL6/WTIAL3 pointer paragraph; "Two things
  are specific …" → colon and two bullets ("And" dropped). The open-vias bullet (46 words) split at
  ", so its underlayer …"; its trailing "(inference from the reading above and the via-4
  rules[^pdk-periph])" repeated on the first half (declared hedge and marker: that half *is* the
  via-fill reading).
* Why: resistance item split at its semicolon; bond-pad item: the three studies after the colon as
  sub-bullets (step-page skeleton, "studies as sub-bullets"), the TiW-cap sentence as a continuation
  paragraph; via-fill item split at its semicolon ("Matsuoka et al., however, found …" keeps
  "however" after its first phrase); film-functions item split at its semicolons.
* How: scope sentence italic; step 4 and step 5 split at their semicolons (step 5 with a
  continuation paragraph); step 6's 30-word gloss "(The nearest public analogue … instead.[^cyp-qtp-123907])"
  a parenthetical sentence.
* R-TOOLS (149 form). R-RELATED (Previous · Next · Depends on · Feeds · Same category · Category
  page). R-OPENQ: via-fill bullet split at its semicolon; thickness bullet with a continuation
  paragraph; a label on the last bullet. Glance box (149 form; the via-fill reading kept as "we read
  it as also filling the via-4 holes (inference)").
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared hedges
  ("our arithmetic"×2, "(inference …)" and `pdk-periph` on the open-vias half), the H3s and labels;
  every `number_order` change REGROUPED, read. `--strict-words` LOST: `measuring`, `strength`,
  `whereas` (and `which`, `while`, `with`). cov: two flags, pairing noise (the glance tool line; the
  quick-facts table). inv: OK.
