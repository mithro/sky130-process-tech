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

### 162 MM5 — done (base `9531b1fd`)

* Lead (80 words, first sentence 12): unchanged.
* R-H3 + R-TABLE: `### What the public record shows` after the figure caption (139/154 form); the
  periphery-rule clause → "The periphery rules give:[^pdk-periph]" and a `Rule | Constrains | Value`
  table in base order; the minimum-CD clause after the semicolon its own sentence. `number_order`
  LOST line re-paired by hand: m5.1 1.600 µm · m5.2 1.600 µm · m5.4 4.000 µm² · m5.3 0.310 µm; the
  CD sentence keeps 0.8 µm then 1.6 µm. The 80-word background-page sentence split at its two
  semicolons (word `and` lost), then a paragraph break; the 17-word trailing hedge "(Inference; the
  corresponding metal-4 rule, m4.4, … qualifier.[^pdk-periph])" a parenthetical sentence directly
  after the reading it qualifies (R-SENTENCE step 7).
* R-CATEGORY (154 form): classification sentence alone; **Specific to this step:** with the k₁
  sentence (split at ", and ASML describes …"; its "(our arithmetic)" still covers both k₁ values in
  its own sentence) and the i-line inference as two bullets; the "What is specific … is thickness"
  paragraph: the 68-word sentence split after "lower metal levels" (the base's ", so" kept inside
  the first half), the dash aside "Krogh et al. monitored … plasma.[^krogh-1987]" directly after it,
  then "A thick resist in turn …" (word `and` lost); the flat-surface sentence a second paragraph.
* Why: grid and via-enclosure items with continuation paragraphs; reflectivity item — the second
  dash aside "the role Rocke and Schneegans documented … (inference)[^rocke-1988]" → "This is the role
  … (inference).[^rocke-1988]" (declared "This is"), "— and a thick resist …" → "A thick resist …";
  no-fill item with a continuation paragraph.
* How: scope sentence italic. R-TOOLS (154 form; "lists both" as R-TOOLS step 2 allows).
  R-RELATED (Previous · Next · Depends on · Feeds · Same category · Mask · Category page; "Mask
  page:" → "Mask:", word `page` lost). R-OPENQ labels on three bullets. Glance box (154 form).
* `check_preserved --allow-regrouped`: the one LOST line is the rule table above; ADDED outside the
  glance only "This is", the H3, the table header and labels; every other `number_order` change
  REGROUPED, read. `--strict-words` LOST: `page`, `strength`×3. cov: one flag, pairing noise. inv: OK.

### 163 MM5E — done (base `5a83c838`)

* Lead (base 138): two paragraphs (74, 67). The 59-word "Through the resist … removes the
  metal-5 stack of WTIAL5 — on this reference's reading a TiW cap, … — everywhere outside …" keeps
  its main clause; the dash aside follows it as "The stack is, on this reference's reading, a TiW
  cap, …[^cyp-qtp-123907] (overview-metal-cap)." (declared "The stack is", 155 form; the hedge "on
  this reference's reading" and the marker travel with it). `number_order` LOST line
  ('1.2', '2014', '72', '20') re-paired by hand: the dash material (1.2 µm, 2014) now follows the
  clause with GDS 72:20; same digits, same claims.
* `**How thick is the metal?**` → `### How thick is the metal?` (155 form), three paragraphs, the
  62-word sentence split at its semicolons.
* R-CATEGORY (155/145 form): classification sentence alone; MM1E pointer paragraph; the "What is
  specific … is the depth of metal …" paragraph kept whole with its elaborating sentences (D4),
  its 47-word sentence's dash aside "Krogh et al. followed … spectroscopy.[^krogh-1987]" moved,
  unchanged, directly after it (the list around it now joined by a comma); the pattern-density and
  no-dielectric sentences a second paragraph (the first would otherwise be 101 words).
* Why: four items split at their semicolons, two with continuation paragraphs; the charging item's
  12-word trailing hedge a parenthetical sentence ("(Inference; Wang, Ackaert et al. showed …
  antenna.[^wang-2004-mim])").
* How: scope sentence italic; step 1 split at its semicolon; step 3 and step 8 with continuation
  paragraphs; step 7's two dash asides moved after the sentence (155 form).
* R-TOOLS (155 form). Resources: 140/155 form for the 20-word gas parenthetical. R-RELATED (155
  labels). R-OPENQ: thickness bullet split at its semicolon; labels on two bullets. Glance (155 form).
* `check_preserved --allow-regrouped`: the one LOST line is above; ADDED outside the glance only "The
  stack is", the H3 and labels; everything else REGROUPED, read. `--strict-words` LOST: `strength`×2.
  cov: two flags, pairing noise (quick facts; the moved step-7 asides keep `skw-01`). inv: OK.

### 164 NFUSOX — done (base `5c390ad0`)

* Lead (base 113, within 120, one paragraph over 100): two paragraphs (82, 33). The 70-word second
  sentence split at its semicolon and at its closing dash apposition: "… between them. This is an
  inference set out below, and one that does not settle …" (declared "This is"). **Listed under note
  ¹ of §4.1:** the lead goes 113 → 115, within 120; the apposition has no verb of its own, so no
  zero-word split exists. The second paragraph opens "`NFUSOX` opens the passivation module" (the
  base's "It", three sentences from its noun; zero words added).
* R-H3: `### What the public record shows` after the figure caption over the PDK/Cypress passage.
  R-LIST: the 65-word diagram sentence → "Directly on `metal5` (…) it shows:[^pdk-04]" and the TOPOX
  and TOPNIT films as two bullets, the glass cut and polyimide as the following sentence with the
  base's marker (declared repeated `pdk-04` on the lead-in, R-LIST step 1; word `and` lost); the
  Cypress sentence → "… in the same two-layer form:" and the two TEOS/nitride stacks as bullets, then
  "The 2013 report for the S8TNV-5R variant gives only "7000 +/- 2000A Nitride"." (word `while`
  lost). The reading sentence split at its semicolon; its 31-word hedge "(Inference: it is the only
  oxide … Cypress reports.[^pdk-04][^cyp-qtp-123907])" a parenthetical sentence after it.
* R-CATEGORY: classification sentence alone; "Two things set it apart." → colon and two bullets
  ("And" dropped); the first bullet's closing dash ", so it must cover" → ". So it must cover" (the
  sentence was 49 words); the aspect-ratio gloss "(an aspect ratio of about 0.8:1, our arithmetic
  from the PDK values)" (12 words) a parenthetical sentence after the gap-fill sentence (R-SENTENCE
  step 7, its hedge inside it).
* Why: buffer item — the dash aside (Sinha; the seal-ring patent's quotation) moved, unchanged, to
  after the sentence it interrupted ("…, but it is hydrogen-rich …[^claassen-1985]" then "Sinha et
  al. … contamination".[^pat-sealring-zeevo]"), each study keeping its marker; the oxide-buffer
  sentence split at its semicolon. Doped item — same move for the seal-ring aside; the reading
  sentence split at its semicolon (its "(inference)" in its own half). The buffer item's lead
  sentence is 32 words (it has continuation paragraphs, not sub-bullets).
* How: scope sentence italic (it ends in a colon before the numbered list); step 3 split before
  "Adams et al." (continuation paragraph).
* R-TOOLS (143 form; the "C2"/"Producer" reading sentence as the continuation). R-RELATED
  (Previous · Next · Same module: 164–171 share the Phase cell · Mask: the metal-4 fuse mask · Same
  category · Category page). R-OPENQ: labels on four bullets; the fuse bullet's dash list as
  sub-bullets after "The PDK documents laser-programmable metal fuses:" with the question kept last
  in its base words (R-OPENQ step 2); the between-lines bullet's 23-word "(our reading of the
  drawing: 5.3711 µm + 0.3777 µm equals …[^pdk-04])" a parenthetical sentence, the question as the
  continuation.
* Glance box.
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared `pdk-04`, "This
  is", the H3 and labels; every `number_order` change REGROUPED, read. `--strict-words` LOST:
  `strength` (and `it` → `NFUSOX`, `while`, `and`). cov: two flags, pairing noise. inv: OK.

### 165 NSM — done (base `45b74f98`)

In-force note (US 10,062,748) and the "collapsed note below this list" pointers: untouched, byte for
byte; the glance box names nothing from the note; `check_inforce` 0 problems.

* Lead (base 118, within 120; first sentence 41 words): the first sentence split at its colon ("…
  on the finished metal stack. A resist is coated …", zero words); the colon-introduced list of three
  PDK entries (51-word sentence) as three bullets, each with its own marker (word `and` lost); the
  step-list sentence as the second paragraph. First sentence 10 words; lead 117.
* R-H3: the bold run-in `**Where `nsm` is drawn.**` → `### Where `nsm` is drawn` (R-H3 step 4).
  R-TABLE: the 73-word rule sentence → "The rules keep the layer away from every device and wiring
  layer:[^pdk-periph]" (the base's own sentence, its full stop a colon) and a `Rule | Constrains |
  Value` table; `number_order` LOST line re-paired by hand: nsm.1 3.000 µm · nsm.2 4.000 µm · nsm.3
  at least 1.000 µm (metals 1–5, the two exemptions word for word) · nsm.3a at least 3.000 µm · nsm.3b
  3.000 µm. Cell rewordings ("Its minimum width is" → "minimum width"; "must be enclosed by … by at
  least" → "enclosure of … by …", "at least" kept in the value; "must be at least … from" → "from …"
  with "at least" in the value; words `its`, `must`×2, `be`×2, `by`, `enclosed` lost). The 15-word
  `areaid.sl` gloss a parenthetical sentence after its sentence (R-SENTENCE step 7), with `pdk-06`
  repeated inside it (declared: the base's one marker covered it and it would otherwise be uncited).
* Reading paragraph: the 46-word sentence split after "along the edge of every die": "It lies in a
  region that carries no wiring …" (declared "It lies"), with "(inference from the rules and the
  layout)" repeated on both halves (declared, R-SENTENCE step 5).
* R-CATEGORY (154/162 form): classification sentence alone; **Specific to this step:** with the k₁
  sentences (the 73-word sentence split at ", and the process factor", ", and ASML describes" and its
  semicolon; "(our arithmetic)" in the k₁ sentence) as two bullets; "What is specific … is the
  substrate and the etch the resist must survive:" with its two clauses as bullets; the overlay
  sentence a paragraph after.
* Why: exposed-edge item in four blocks, the stack-diagram sentence split at ", and outside the
  wiring": "Outside the wiring everything below that level is PSG, …[^pdk-04]" ("it" → "that level":
  after the split the nearest noun is the trench floor; declared repeated `pdk-04`); the Comizzoli
  sentence at its semicolon. Nitride-reach item with continuation paragraphs, its last sentence at
  its semicolon. Resist-mask item: its 16-word trailing hedge "(Inference from the construction of the
  GlobalFoundries edge seal, in the collapsed note below this list.)" a parenthetical sentence (the
  sentence before it, 43 words, keeps its semicolon so the hedge still covers all of it).
* How: scope sentence italic; step 2's dash aside (the TSMC fuse-window patent) as a continuation
  paragraph.
* R-TOOLS ("lists both"). R-RELATED (Previous · Next · Same module · Depends on · Mask · Category
  page; "Mask page:" → "Mask:"). R-OPENQ labels on four bullets, the depth bullet split at its
  semicolon.
* Glance box.
* `check_preserved --allow-regrouped`: the one LOST line is the rule table; ADDED outside the glance
  only the declared `pdk-04`, `pdk-06`, "(inference …)", "It lies", the H3, the table header and
  labels; every other `number_order` change REGROUPED, read. `--strict-words` LOST: `enclosed`,
  `must`×2, `page`, `strength`×3. cov: three flags, pairing noise. inv: OK (dropdowns identical).

### 166 NSME — done (base `b1d7457a`)

In-force notes (US 10,062,748) and their pointers: untouched; nothing from them in the glance box.

* Lead (base 89, first sentence 55): "… resist pattern of NSM: a ring, … along the edge of every die, in
  a band that …" → "… pattern of NSM. The opening is a ring, … along the edge of every die. The ring
  lies in a band that …" (declared "The opening is", "The ring lies"; the zero-word colon split left
  a 26-word first sentence or a 46-word second one). **Listed under note ¹ of §4.1:** the lead goes
  89 → 95, within 120; first sentence 12.
* R-H3: `### Competing readings` after the figure caption over the passage that sets out the two
  depth readings (≈ 280 words); the in-force note stays directly after the bullets it belongs to.
  R-LIST: the 83-word dielectric sentence → "… lie only dielectrics: on the diagram,[^pdk-04]" and
  three bullets (declared repeated `pdk-04` on the lead-in, R-LIST step 1); its closing absolute
  phrase "the bottom of metal 5 carrying the level 5.3711 µm, …" → "The bottom of metal 5 carries the
  level 5.3711 µm, …[^pdk-04]" (word `carrying` lost). The deep-seal bullet keeps its 42-word first
  sentence whole: its only seam is the purpose clause "so that", which a split would turn into a
  consequence; the patent pointer and the nsm.3 sentence as a continuation paragraph. The
  percentage sentence split at its colon.
* R-CATEGORY: classification sentence to its semicolon; the nitride reading as its own paragraph;
  "What is specific … is the depth …, the absence …, the tiny open area, and the timing: …" (67
  words) → "… is:" and four bullets, every word kept but the joining "and".
* Why: path item in three blocks (semicolon split; its dash → full stop before "The patent's own
  moisture-path area …"). How: scope sentence italic; step 2 with the Perry sentence as a
  continuation (its semicolon a full stop); step 3 split at its semicolon (continuation).
* R-TOOLS (145/160 form). Resources: the gas parenthetical → "(industry practice[^nojiri-2015]); **He**
  backside cooling. SkyWater lists … etchers.[^skw-01]" (the SkyWater clause moved to the end of the
  bullet as its own sentence). R-RELATED (Previous · Next · Same module · Depends on · Same category ·
  Category page). R-OPENQ labels on three bullets. Glance box.
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared `pdk-04`, "The
  opening is", "The ring lies", the H3 and labels; every `number_order` change REGROUPED, read.
  `--strict-words` LOST: `carrying`, `strength`×2. cov: flags are pairing noise (the new lead
  sentences against the quick-facts table; "the tiny open area" against the How step's "about 0.5 %
  (our estimate above)", which is unchanged). inv: OK (dropdowns identical).

### 167 NTSD — done (base `eb7e4be5`)

In-force note (US 10,062,748) and its pointer: untouched; nothing from it in the glance box. The
"0.7–0.9 µm" of How step 4 and Open questions is kept verbatim (content problem 5).

* Lead (base 85, first sentence 59 with two dash pairs): "… outer skin of the die: a blanket
  nitride — on our reading a plasma (PECVD) nitride — laid over …" → "… outer skin of the die. It is
  a blanket nitride laid over …, and — on our reading of NSM and NSME — into the ring-shaped opening
  …. On our reading it is a plasma (PECVD) nitride." (declared "It is", "it is"; the first dash
  aside moved, with its hedge, to directly after its sentence). **Listed under note ¹ of §4.1:** 85 →
  89 words, within 120; first sentence 13.
* R-H3: `### What the public record shows` after the figure caption. Diagram sentence split at its
  semicolon with `pdk-04` repeated on the first half (declared); "(our reading of the drawing)"
  stays on the 0.3777 µm half, the first half being labels read off the cited diagram. R-TABLE: the
  Cypress dash list → a `Report | Stack as quoted` table (R-TABLE's film-stack template); `number_order`
  LOST line re-paired by hand: R7FT-3R 2005 "1000Å TEOS / 9000Å PECVD Nitride" · S8DI 2014 "1000A
  TEOS/9000A Si3N4" · S8TNV-5R 2013 "7000 +/- 2000A Nitride", each with its own marker; the
  conclusion "So the public record puts … between 0.54 µm and 0.9 µm; …" as the prose after the table
  (R-TABLE step 8; it keeps the base's "so", so the paragraph after the table opens on "So" — see
  guide problem 2). The PECVD sentence split at its semicolon.
* R-CATEGORY: classification sentence alone; no **Specific to this step:** bullets — the LINIT
  comparison and "This one is several times thicker …" must stay together (the pronoun needs its
  antecedent), and a bullet per sentence would have opened one on "So". Paragraphs instead: LINIT
  comparison (its 77-word sentence split at the semicolon and at ", so step coverage" → "So step
  coverage …"); the 78 % coverage sentence; the polyimide passage (its 50-word sentence split at ",
  the step list has no polyimide step"); the mould-compound sentence split at its semicolon.
* R-REPEAT considered and not applied: the polyimide passage appears under Step category and, shorter,
  under Open questions (its home). The category copy names the flagged masks in full ("Polyimide 2
  (2)", "DECA PBO", "Cu Inductor/Redist."), which the Open-questions copy abbreviates, so neither copy
  adds nothing. Both were split the same way. `check_preserved` therefore prints `DUPLICATED
  sentence (2x, was 1x): 'Whether a polyimide is applied to SKY130 wafers in this flow is not
  public.'` and `DUPLICATED sentence (2x, was 0x): 'The step list has no polyimide step, and the
  PDK's stack diagram draws "PI1 K=2.94" over the nitride.'` — both sentences stood twice in the base
  (once in each section, the second one inside a longer sentence); nothing was duplicated.
* Why: barrier item in three blocks (split at semicolons); mechanical item's 17-word trailing hedge
  "(Industry practice;[^txt-05] Hunter et al. …[^hunter-2012])" a parenthetical sentence; hydrogen item:
  lead "Plasma nitride … contains a great deal of hydrogen.", the dash aside (Lanford and Rand; Chow et
  al.) directly after it, then "The nitride's stress depends on …" ("its" → "the nitride's",
  restored noun; word `and` lost) and the Hughey sentence; the Shimaya sentences a second
  continuation.
* How: scope sentence italic; step 2 — the dash aside (Claassen et al.) moved after its sentence;
  step 3 in three blocks; step 4's colon list as two sub-bullets (0.54 µm; 0.7–0.9 µm), the Vanguard
  sentences as a continuation; step 5 split at its first sentence end.
* R-TOOLS (the C1 reading sentence as the continuation). R-RELATED (Previous · Next · Same module ·
  Depends on · Same category · Category page; the base's two-relationship bullet split). R-OPENQ
  labels on five bullets; the polyimide bullet's question as its lead, its 46-word evidence sentence
  split like the category copy. Glance box.
* `check_preserved --allow-regrouped`: the one LOST line is the table; ADDED outside the glance only
  the declared `pdk-04`, "It is"/"it is", the H3, the table header and labels; the two DUPLICATED
  lines are the false positives above. `--strict-words` LOST: `strength` (and `its`, `and`). cov:
  three flags, pairing noise. inv: OK (dropdowns identical).

### 168 PDM — done (base `af817394`)

In-force note (US 7,679,384) and its pointer: untouched; nothing from it in the glance box. The
"7000–9000 Å" of the category paragraph is kept verbatim (content problem 5).

* Lead (base 130): two paragraphs (57, 73), the 48-word resist sentence split at its semicolon.
* R-H3: `### What the public record shows` after the figure caption; the CD sentence split at its
  semicolon; "The PDK does not explain the two variants …" a paragraph, split at its semicolon.
  **A real pad.** stays a bold run-in over its paragraph (R-H3 step 4). Its 79-word GPIO sentence
  split into three: "… the `pad` opening is a single octagon over a similarly chamfered 65.4 µm ×
  75.4 µm metal-5 pad …", the dash material "The opening is a 60 µm × 70 µm rectangle with 4.95 µm
  chamfered corners …" (declared "The opening is") and "So the metal extends 2.7 µm …"; the
  trailing "(our reading of the published GDS and LEF).[^pdk-io-gpiov2]" repeated on every half
  (declared ×2, R-SENTENCE step 5: each half is a reading of the same files). `number_order` LOST
  line re-paired by hand: cell 80 µm × 200 µm; opening 60 µm × 70 µm with 4.95 µm chamfers; pad 65.4
  µm × 75.4 µm; 2.7 µm margin; 0.8 µm via-4 squares — same numbers, same attributions.
* R-CATEGORY (165 form): classification sentence alone; **Specific to this step:** with the k₁
  sentence and the ASML-plus-inference sentences as two bullets; the "What is specific … is the
  substrate: …" sentence keeps its main clause and its marker, and its 39-word gloss "(The PDK's 0.09 µm
  TOPOX and 0.54 µm TOPNIT,[^pdk-04] or the 7000–9000 Å nitride of Cypress reports … given.[^cyp-qtp-123907][^cyp-qtp-113005])"
  follows it as a parenthetical sentence (R-SENTENCE step 7). `number_order` LOST line
  ('0.6–1', '0.09', '0.54', '7000–9000', '1000', '1.26') re-paired: the gloss's numbers now follow the
  1.26 µm clause instead of preceding it; same digits, same markers.
* Why: access item — lead sentence, then "The opening's size and its enclosure by the pad metal (…)
  decide:" with its two complements as sub-bullets and the trailing hedge "(Industry
  practice;[^txt-05] Comizzoli et al. …[^comizzoli-1986])" as a sentence directly under the list,
  covering both (R-TABLE step 5 applied to a list). The 16-word "(2.7 µm per side in the GPIO cell,
  the pad.4/4a check of the Error Messages page)" stays inline on "enclosure": it is mostly source
  names and markers, and moving it would part it from the word it glosses (listed for the reviewer).
  Scribe-test item: the dash aside now ends its own sentence at the marker; the patent pointer
  sentence is base wording.
* How: scope sentence italic; step 2 split at ", with thickness chosen" → "The thickness is chosen
  …" (declared "The", "is"); step 6's 13-word gloss "(Scum left in a pad …)" a parenthetical
  sentence.
* R-TOOLS (165 form). R-RELATED (Previous · Next · Same module · Depends on · Mask · Category page;
  "Mask page:" → "Mask:"). R-OPENQ labels on four bullets; the enclosure bullet's 13-word gloss "(The
  only pad enclosure rule there is m4.16, … flagged "CU".[^pdk-periph])" a parenthetical sentence, its
  second half a continuation. Glance box.
* `check_preserved --allow-regrouped`: the two LOST lines are above; ADDED outside the glance only the
  declared hedges and markers, "The opening is", "The thickness is", the H3 and labels; everything
  else REGROUPED, read. `--strict-words` LOST: `page`, `strength`×3. cov: two flags, pairing noise.
  inv: OK (dropdowns identical).

### 169 PDME — done (base `cb6bb0d6`)

No in-force note in the hand-written text. The "7000–9000 Å" of the public-record paragraph is kept
verbatim (content problem 5).

* Lead (78 words, first sentence 7): unchanged.
* R-H3: `### What the public record shows` after the figure caption. The 54-word diagram sentence split
  at ", while Cypress reports …" (word `while` lost). The 73-word reading sentence split at its
  semicolon; its 53-word parenthetical split at its own semicolon: "({ref} WTIAL5)" stays on "a
  TiW-capped Al–Cu stack", the hedge "(Inference from the 300 Å TiW caps …[^cyp-qtp-113005] and from
  Cypress's 2014 report, … top metal.[^cyp-qtp-123907])" and the pointer "(The whole of that evidence
  is set out under overview-metal-cap.)" follow as two parenthetical sentences (R-SENTENCE step 7). Three
  paragraphs.
* R-CATEGORY: classification sentence alone; the "What is specific … is the floor." paragraph kept with
  its elaborating sentences (D4), its 52-word sentence split at its semicolon; the aluminium sentences
  (split at their semicolon) a second paragraph.
* Why: pads item — lead "The pads must be clean metal.", the patents as a continuation (colon and
  semicolon → full stops); cap item split at its semicolon; edge item's 14-word trailing hedge a
  parenthetical sentence; test item with a continuation paragraph.
* How: scope sentence italic; step 2 — lead "CF₄/O₂ (with N₂ or CHF₃) or SF₆-based chemistry.", the
  Kastenmeier sentence as a continuation, its 14-word gloss "(Small N₂ additions raise the nitride
  rate sevenfold while leaving the oxide rate unchanged.[^kastenmeier-1996])" a parenthetical
  sentence after it with `kastenmeier-1996` repeated inside (declared: it would otherwise be uncited);
  step 4 split at its semicolon (continuation).
* R-TOOLS: Lam 9400 TCP in three lines; DPSII's "**medium**" and Lam 4400's "**weak**" are assignment
  grades (*Runs this step:*); the strip item's "strong for existence" (*Tool exists:*); the Lam
  9600/2300 item has no grade and is unchanged. Resources: the 13-word gas parenthetical → 140 form.
  R-RELATED (Previous · Next · Same module: two base bullets joined, no link changed · Depends on ·
  Same category · Category page). R-OPENQ labels on five bullets; the thickness bullet → "… is
  uncertain:" and its three figures as sub-bullets (R-OPENQ step 2; word `against` and one `and`
  lost), the 15-word parenthetical of the Cypress figure set off by commas instead.
* Glance box.
* `check_preserved --allow-regrouped`: ADDED outside the glance only the declared `kastenmeier-1996`,
  the H3 and labels; every `number_order` change REGROUPED, read. `--strict-words` LOST: `against`,
  `strength`×4 (and `while`). cov: three flags, pairing noise. inv: OK.

### 170 ALLY — done (base `c41c50f9`)

No in-force note in the hand-written text. The "7000–9000 Å" of the post-figure passage is kept
verbatim (content problem 5).

* Lead (base 172, first sentence 38): first sentence split at its colon (zero words; 9 words now);
  "… at typically 350–450 °C[^txt-02] whose purposes are …" → ". Its purposes are …" (whose → Its, the
  gloss rule's form; word `whose` lost); the reading sentence split at its semicolon and its 23-word
  trailing hedge "(Inference: textbooks describe … alloy process.[^skw-01])" a parenthetical sentence.
  Two paragraphs (95, 77).
* Post-figure passage: "… how much now lies between the ambient and the transistors:" and the four
  layers as bullets (R-LIST; 47 words as one sentence); the 29-word gloss of the passivation ("TOPOX"
  and "TOPNIT" …, 7000–9000 Å … fab.[^…]) moved, unchanged, out of the middle of its item to
  directly after it, as a parenthetical sentence inside the same bullet.
* R-CATEGORY: classification sentence alone; the category-page sentence and the thermal-budget
  sentence a paragraph; "What it changes is X, Y …, and Z" (49 words) → "What it changes is:" and
  three bullets (the `overview-metal-cap` dash aside stays inside its bullet); the bond-pad sentence a
  closing paragraph. No **Specific to this step:** label: the remaining sentences are already
  separate paragraphs and a list of their own.
* Why: interface-trap item — the four studies after its colon as sub-bullets (step-page skeleton),
  the Deal and trap-density sentences as a continuation; plasma-damage, hot-carrier, contacts and
  nitride-memory items with continuation paragraphs (semicolons → full stops).
* How: scope sentence italic; temperature item split after its first sentence: "This is far below
  the 577 °C Al–Si eutectic …" (declared "This is"; the dash apposition as a sentence), and ",
  which is why we read the soak as short …" → ". That is why …" (which → That), "(inference)" in
  that sentence as in the base, the first half cited.
* R-TOOLS (Aviza: three lines; the asher parenthetical and the dealer sentence as the continuation);
  the Heatpulse item has no "Strength:" and is unchanged. R-RELATED (Previous · Next · Same module ·
  Same category · the ONO bullet · Category page): the ONO bullet ("The memory cells whose nitride
  hydrogen can affect") keeps its base form — no R-RELATED label is true of it (it is neither a
  dependency nor something this step feeds). R-OPENQ labels on four bullets. Glance box (the only
  number is the page's own "typically 350–450 °C" with its marker, after "none published for SKY130").
* `check_preserved --allow-regrouped`: ADDED outside the glance only "Its", "This is", "That", the
  labels; every `number_order` change REGROUPED, read. `--strict-words` LOST: `strength` (and
  `whose`, `which`, `and`). cov: three flags, pairing noise. inv: OK.
