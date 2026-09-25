# Progress — readability batch 5, steps 064–075 (`topic/rd-steps-064-075`)

Writer: Opus. Started 2026-09-26 from `main` at `7fea7c90`. Guide: `docs/plans/readability-guide.md`
(§1, §2, §4.1, §5, §6, §7, §8), including the batch-4 rulings (R-LIST plain bullets, R-H3 step 6,
R-CATEGORY step 1, R-PARA step 2 inside list items, R-TOOLS step 2 pilot form). Model pages: 052, 058,
043. One commit per page.

## Method, every page

* Baseline build and tiles (1280 px and 400 px, `--max-height 40000/60000`) of all 12 pages before any
  edit.
* Preservation: `uv run python tools/check_preserved.py --base main <page> --allow-regrouped` first,
  with no other allowance; every ADDED line is named in the page entry below, with the rule that adds
  it, before the categories are declared with `--allow-added`. `--allow-dropdown-edits` is never used.
* Marker coverage: `tmp/readability/markcov.py` (git-ignored) pairs every new sentence that is not
  verbatim in the base with its closest base sentence and flags a lost marker or hedge word; every flag
  is read and explained in the page entry.
* Invariants: `tmp/readability/invariants.py` (git-ignored) compares with `main`: `## References`
  section, footnote definitions, generated index-links block, `{figure}` blocks, quick-facts table,
  every `{dropdown}` block, H2 list, Deep-dive `* ` count; and reports admonitions, the glance box,
  glance markers that do not recur below it, duplicate H3s and the italic scope lead-in.
* Caps: `tmp/readability/caps.py` (git-ignored): `measure.py`'s blocks and `measure5.py`'s sentence
  split at the §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25), `{figure}` blocks,
  `{dropdown}` bodies, the generated block and `## References` excluded.
* Repeats: `tmp/readability/repeat.py` (git-ignored), 10-word runs shared by two H2 sections.
* Checkers after each page: `check_steps`, `check_refs`, `check_inforce`, `gen_index_links --check`,
  `gen_figures --check`; `-W` build; tiles at 1280 px and 400 px, read against the baseline.

## Pages

### 064 NTM — done

* **Lead.** Split into two paragraphs before "`NTM` coats this now-topographic surface" (what arrives /
  what the step does). The 16-word parenthetical "(inference: the tip and its halo … serves both)"
  closed as its own sentence, "(Inference: … serves both.)" (R-SENTENCE step 7). Lead 150 words, as in
  the base less nothing: §1's 120 cannot be met without dropping words. First sentence 21 words.
* **R-H3.** `### What the public record shows` after the figure caption, over the PDK evidence (mask
  table, layer list, Error Messages, Table F2b, Criteria & Assumptions; ≈ 390 words, one inference
  that the derivation is Boolean, stated with its hedge).
* **R-PARA.** The 230-word evidence paragraph split at its seams, with run-in labels (evidence
  sequence, R-PARA step 3): "**Mask and layer.**", "**Error checks.**", "**Created and drawn
  layers.**" (the mask page's reading of the created data, Table F2b, and the two designer-drawn tip
  layers), "**Published parameters.**".
* **R-SENTENCE.** "The generated mask layer is `cntm` …;[^pdk-06] there is no designer-drawn `ntm`
  layer …" split at the semicolon (each half keeps its own marker; the inference clause had none).
  Error Messages sentence split at the colon and at the semicolon; `[^pdk-errors]` **repeated** on
  "names other layers." and on the checks sentence so each claim keeps it (declared). Table F2b
  sentence split at ", which is consistent with" → "This is consistent with …"; `[^pdk-06]`
  **repeated** on the first half (declared).
* **R-LIST.** The *Criteria & Assumptions* parameters ("a tip implant angle of 7° …, an "NTM
  shadowing" distance of 0.16 µm and, immediately below it …, a "pseudo-shadowing" allowance …") →
  three plain bullets (no invented labels), every word kept except the list-joining "and"; the
  sentence had no marker of its own (`[^pdk-03]` ended the next sentence), so `[^pdk-03]` is
  **repeated** on the lead-in before the colon (declared). The 0.1 µm / 0.01 µm sentence and the
  "These are the quantities …" sentence stay as prose after the list, unchanged.
* **R-CATEGORY.** Classification sentence (38 words, no semicolon or closing dash to split at, so kept
  whole: R-CATEGORY step 1 as ruled in batch 4) alone; the three remaining sentences describe this step
  → `**Specific to this step:**` and three bullets. The third ("It is the first mask … — 0.18 µm of
  poly … (the PDK's figure … no thinner)[^pdk-03] — rather than on a planar surface", 60 words, a dash
  pair holding a 19-word parenthetical) split per R-SENTENCE step 1: the frame closes ("… topography
  rather than on a planar surface."), the dash material becomes "The topography is …" (subject + verb
  added, step 7) in an indented continuation paragraph, and the parenthetical closes as its own
  sentence "(The PDK's figure … no thinner.)[^pdk-03]"; `[^pdk-03]` **repeated** after "poly cap after
  SPE"" so the 0.2 µm claim keeps its marker (declared).
* **Why.** Paragraph 1 (150 words) split before "ITRS 2001 asks" (history / roadmap). The Ogura
  sentence split at its semicolon (each half keeps its marker). The 85-word ITRS sentence split at "—
  and defines" ("It defines …", subject added) and at the semicolon before "the same rule applied to
  SKY130's …"; `[^itrs-01]` **repeated** on the first two pieces (declared, ×2). The hedge "(our
  reading of the roadmap; SKY130's physical gate length is not published)" stays with the sentence it
  sat in, the application to SKY130; grammatically it never governed the ITRS values.
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-PARA step 4 (items).** "Resist coat" (70 w): continuation paragraph at "The poly steps cause …".
  "Exposure": the 60-word first sentence split at its dash ("That is well within …", subject + verb
  added); continuation paragraph at "ASML describes …". "Alignment": split at the colon ("The overlay
  budget … by shadowing." / "The PDK's 0.16 µm …" continuation; the marker sat in the second half in
  the base).
* **R-DERIVATION not applied** to "(k₁ = 0.7 × 0.6 / 0.365 ≈ 1.2 at NA 0.6 for the space)": one formula
  inside a recipe step, not a passage; left inline as on 052.
* **R-TOOLS.** ASML: *SkyWater says:* "facilities page lists …" (verb-first form of 034), *Tool
  exists:*, *Runs this step:*. Tracks: *Tool exists:* "strong for existence."; the clause "pairing with
  exposure tools not public" is not a grade and becomes the continuation paragraph ("Pairing …",
  capital only). Overlay/CD: two grades. Three tools: no recap table.
* **R-RELATED.** "Sibling tip masks:" → "Same module: sibling tip masks …" (HVNTM, LDNTM, TIPRTAD all
  carry this module's Phase cell); "Mask page:" → "Mask:". The SPNIT/PSDM/NSDM bullet ("The spacer that
  follows the module") keeps no label: "Same module" would contradict its own gloss.
* **R-OPENQ.** "PMOS extensions" (80 w): lead "The mask table has no P-tip mask,[^pdk-05] yet" with the
  two PDK facts as sub-bullets (every word, the joining comma now a semicolon) and the question as the
  continuation paragraph, in the original order. Labels added to the other three ("Boolean recipe",
  "Resist, tool and hardening", "Film under the resist"), text unchanged; "Boolean recipe" split at its
  semicolon (56 w sentence).
* **R-GLANCE.** Does and Why from the lead and "Three tip masks exist because …"; Public numbers:
  `NTMCD`/`NTMCDSP` 0.84/0.7 µm, the 7° angle and the 0.16 µm "NTM shadowing" `[^pdk-03]`; tool line
  with the page's grades; Not public from Open questions 1–2.
* **Skipped.** R-REPEAT (no 10-word repeat across H2s); R-TABLE on the parameters (the items carry
  their own glosses and the one inference; a list keeps every word).
* **Preservation** (`--allow-regrouped` only): ADDED markers `itrs-01`×2, `pdk-03`×3, `pdk-06`,
  `pdk-errors`×2 (the repeats above), `skw-01` (glance) and one `pdk-03` of the three (glance);
  numbers 0.16, 0.7, 0.84, 1.8, 7, quote "NTM shadowing", hedges "inference", "not public",
  number_order (0.84, 0.7, 7, 0.16) — the glance box. REGROUPED: the parameters list (7, 0.16, 0.045),
  the ITRS sentence (same digits, same order, split into three), the Exposure sentence (0.84, 0.7, 1, 2
  | 0.7, 0.6, 0.365, 1.2, 0.6). Declared `--allow-added markers,numbers,quotes,hedges,number_order`:
  clean.
* **Marker coverage.** 19 flags, all read: the repeats above; split halves whose base marker belonged
  to the other clause (`cntm` layer / inference; openings / k₁; overlay budget / PDK distances); the
  ITRS "our reading" (see Why); glance and label lines.
* **Caps**: para > 100 5 → 0; item > 60 5 → 2; sentence > 45 11 → 1. Left: the 5 V NMOS item (61 w; its
  only seam is before "That is the HVNTM tip"), the Exposure item's lead (62 w; its only seam is before
  "That is well within"); the 46-word `ntm` inference sentence (no seam that keeps "we infer" with its
  whole claim).

### 065 ASTI — done

* **Lead.** Split into two paragraphs before "The gate stack itself masks the channel" (what the step
  does / why the tip is self-aligned); its 49-word sentence split at the semicolon ("The gate poly is
  shielded …"). Lead 129 words, as in the base; first sentence 20 words.
* **R-H3 not applied.** The passage after the figure is 107 words, under R-H3's 120.
* **R-SENTENCE.** The 85-word "That the tip is arsenic is stated publicly: …" sentence split at
  ", which we read as" → "We read that value as the tip's lateral extent because … (inference),
  beside the deeper … row …" (R-PARA step 5: the relative pronoun gets its noun back) and at the
  semicolon ("The same page gives …"); `[^pdk-03]` **repeated** on the first piece so the "N Tip
  (As)" claim keeps it (declared). The clause order is the base's (an earlier try moved the "beside"
  clause forward and `check_preserved` reported a LOST `number_order`; reverted). The halo/strip
  sentence becomes its own short paragraph.
* **R-CATEGORY.** Classification sentence (40 w; no semicolon or closing dash) kept whole. The
  remaining sentence (55 w, a dash pair around the category page's quotation) split per R-SENTENCE
  step 1 into "It is the shallowest implant in the flow." + the quotation sentence, and "With the
  deep source/drain implants (…), it is one of the implants that amorphise …" ("it is" added). Two
  statements about this step → `**Specific to this step:**` with two bullets; the quotation stays in
  the bullet of the claim it supports.
* **R-PARA step 4 (Why items).** "Short-channel control" (101 w): lead split at its semicolon, the three
  sources (Wikipedia, ITRS, Thompson) as plain sub-bullets, each with its marker (a list of studies:
  no labels). "Series resistance" (77 w): lead split at the semicolon, the ITRS and LDD sentences as the
  continuation paragraph. "Gate overlap": split at its semicolon ("Too much overlap adds Miller
  capacitance.").
* **R-PARA.** "Arsenic rather than phosphorus" (109 w) split before "Its drawbacks are electrical"
  ("Its" → "Arsenic's", R-PARA step 5); its 50-word first sentence split at ", and it diffuses" ("It
  diffuses slowly …"; each half keeps its marker); the Nobili sentence split at its semicolon. The bold
  run-in labels a single paragraph, so it stays bold (R-H3 step 4).
* **R-HEDGE.** Italic lead-in, word for word, including "(SKY130's energy and dose are not public)".
* **R-PARA step 4 (How items).** "Energy" (96 w): lead = the first sentence; the ITRS sentence split at
  its semicolon ("ITRS 2001 defines … length.[^itrs-01]" with the marker **repeated**, declared; "For
  SKY130's 0.15 µm drawn gate … (our reading of the roadmap).[^itrs-01]" keeps the hedge on the
  SKY130 application, which is all it governed). "Dose" (66 w): lead = the first sentence; the
  amorphisation sentence split before ", so the implanted layer" ("So the implanted layer …", the
  split R-PARA step 2 allows inside a paragraph), which keeps the lowercase Wikipedia quotation inside
  its own sentence (R-SENTENCE step 6). "Tilt and twist" (144 w, a 104-word sentence): the dash pair
  becomes "The stack is 0.18 µm of poly … "poly cap after SPE".[^pdk-03]" (subject + verb added;
  `[^pdk-03]` **repeated**, declared) and "(The PDK's figure … no thinner.)[^pdk-03]", then "So a 7°
  beam is blocked for at least about 0.38 µm × tan 7° ≈ 47 nm …" (a single-operation estimate, inline
  per R-DERIVATION step 6); Yoneda and "rotation scheme is not public" as a second continuation
  paragraph. Same treatment as 064's category bullet.
* **R-TOOLS.** GSD: *SkyWater says:* holds only the two quotations with `[^skw-01]`; the gloss "both
  offer arsenic and reach the 10¹⁵ cm⁻² decade, …" is this reference's and becomes the continuation
  paragraph ("Both …"), as on 050. 8250: *SkyWater says:* the quotation; grades; the platform and dose
  sentences (vendor facts and our gloss) as the continuation paragraph. Grades unchanged. Two tools:
  no recap table.
* **R-RELATED.** "The other tip implants:" → "Same module: the other tip implants …". "Activation: …;
  spacer: …; deep n⁺ junction: …" keeps its own labels (three relationships, none of them one R-RELATED
  label).
* **R-OPENQ.** Labels "Energy and dose", "Rotation scheme", "Pre-amorphisation", "Tip and halo order";
  text unchanged.
* **R-GLANCE.** Does/Why from the lead and "The extension does three jobs"; Public numbers the "N Tip
  (As)" row, its 0.01 µm entry with the page's "(inference)", the 7° angle `[^pdk-03]`; tool line with
  both tools' grades; Not public from Open questions 1–2.
* **Preservation** (`--allow-regrouped` only): ADDED markers `itrs-01`, `pdk-03`×2 (the repeats above),
  `pdk-03`, `skw-01` (glance); numbers 0.01, 1.8, 7, 8250, quote "N Tip (As)", hedges "inference"×2,
  "not public", number_order (0.01, 7) — the glance box. REGROUPED lines: the arsenic sentence, the
  Energy and Dose items, the tilt item — same digits, same order. Declared
  `--allow-added markers,numbers,quotes,hedges,number_order`: clean.
* **Marker coverage.** 23 flags, all read: the repeats; split halves whose base marker belonged to the
  other clause (DIBL / Wikipedia; drain current / ITRS; "So the implanted layer …" after the three
  amorphisation markers; "So a 7° beam …" after the stack markers; the GSD gloss after the quotations);
  labels and glance lines. No claim lost its marker.
* **Caps**: para > 100 3 → 0; item > 60 7 → 0; sentence > 45 12 → 4. Left: "We read that value …"
  (46 w; splitting it would separate the reading from "(inference)"), "Gate overlap" (46 w + label;
  its dash pair holds the reading and marker), "Without `ASTI` …" (47 w; the colon introduces the two
  consequences), "For SKY130's 0.15 µm drawn gate …" (47 w; a split at ", so" would leave half the
  claim outside "(our reading of the roadmap)").

### 066 BHI — done

* **Lead.** The guide's own R-SENTENCE example (`:16`) applied as written: the dash pair "— we infer
  that the two share the `NTM` resist, since … (see below) —" becomes the following sentence "We infer
  that the two share …", hedge first. The lead then splits into two paragraphs before "After the anneal
  at `TIPRTAD`" (what is done / what results). Lead 122 words, as in the base; first sentence 16 words.
* **R-H3 not applied.** The passage after the figure is 75 words.
* **R-CATEGORY.** The 63-word classification sentence is split at its opening dash: "`BHI` is an Ion
  implantation step of the *channel-engineering* class." alone; the dash material becomes "It is a
  low-dose (10¹²–10¹³ cm⁻², typical)[^txt-01] boron implant at tens of keV, like …, but placed by
  geometry rather than by a mask." ("It is" added, R-SENTENCE step 7), then its colon clause as its own
  sentence ("The tilt puts it …"). The second sentence (dash before "the PDK publishes angles only …")
  is split at the dash, `[^pdk-03]` **repeated** on "… one whose SKY130 angle is not published" (the
  base marker covered the whole sentence; declared). Two statements about this step →
  `**Specific to this step:**` with two bullets.
* **R-PARA step 4 (Why items).** "Punch-through and threshold roll-off" (83 w): lead = the Wikipedia
  sentence, continuation from "Raising the doping uniformly …". "Reverse short-channel effect" (88 w):
  split at the semicolon after Rafferty; continuation "Machala et al. … A deliberately implanted halo
  …". "Lower channel doping elsewhere" (63 w): continuation from "Taur, Wann and Frank's …".
* **R-TABLE (measured against nominal).** The 155-word threshold paragraph: the test-tile values
  (7/8 µm, 7/0.15 µm, and W = 0.42 µm at L = 8–25, 0.5 and 0.15 µm) and the PDK's e-test nominals
  (7/8, 7/0.15 µm) become a `W/L (µm) | Test tile (V) | PDK e-test nominal (V)` table; the lead-in
  keeps "In the published test-tile measurements it is as below, and the PDK's e-test nominals rise the
  same way:" with both markers before the colon (R-TABLE step 3; new words "as below", as 053's
  "at the values below"); e-test cells the page does not give are `—`. The extraction hedge covered
  the test-tile values only; it goes directly under the table, word for word, as "(Test tile:
  maximum-transconductance … our extraction from the published measurements.)" (R-TABLE step 5; the
  two words "Test tile:" name the column it covers). The PMOS sentence and "A halo is one mechanism …"
  stay prose after the table, unchanged. The W/L notation is the page's own ("7/8 µm"); units moved to
  the headers after the first 400 px shot broke "0.53–0.54 V" and "8–25 µm" across lines. Pairings
  checked against the base: 7/8 ↔ 0.534 ↔ 0.541; 7/0.15 ↔ 0.707 ↔ 0.700; 0.42/8–25 ↔ 0.53–0.54;
  0.42/0.5 ↔ 0.60–0.64; 0.42/0.15 ↔ 0.72; the hedge keeps 0.1 and 100.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Species and source" (87 w): continuation from "Indium is the heavier
  alternative"; its 51-word sentence split before ", so the absence" ("So the absence …", R-PARA step
  2). "Energy and dose" (83 w): split at the semicolon ("An AMD multi-threshold patent …"), and ", and a
  halo sits in the same range (inference)" becomes "A halo sits in the same range (inference)." so the
  hedge stays with its claim. "Tilt and rotation" (159 w): lead "Large tilts — 20–45° are typical — push
  the pocket under the gate edge."; continuation 1 from "The beam is shadowed …" (to Chen); continuation 2
  the "NTM shadowing" argument, its 82-word sentence split at the semicolon ("A halo at a much larger
  tilt …"); the single-operation estimate "(1.14 µm × tan 7° ≈ 0.14 µm)" stays inline (R-DERIVATION
  step 6). "Order relative to the tip" (78 w): lead "This reference describes the arsenic first.",
  the rest as the continuation.
* **R-TOOLS.** 8250: *SkyWater says:* the quotation; grades; the gloss "Boron and BF₂, … everything a
  halo needs." as the continuation paragraph. GSD: the head mixes SkyWater's quoted ranges with this
  reference's gloss ("batch tools that SkyWater lists with tilt and twist capability, so …") and cannot be
  separated at a seam (the quotations sit in parentheses on the tool name), so the pilot form: head kept
  whole, grades as sub-bullets, nothing under *SkyWater says:* (R-TOOLS step 2).
* **R-RELATED.** "The other halo:" → "Same module: the other halo, `LDBHI`; …" (colon → comma). The
  "Earlier channel engineering …; activation of the halo: …" bullet keeps its own wording (two
  relationships; neither is exactly an R-RELATED label).
* **R-OPENQ.** Labels "Species, energy, dose and tilt", "The "NTM shadowing" allowance", "Halo on the
  5 V NMOS", "PMOS halo"; text unchanged.
* **R-GLANCE.** Does keeps "our inference" for the shared resist and says "p-type pocket", not "boron"
  (the page calls boron this reference's description, industry-typical); Public numbers "none
  published for the halo" plus the e-test threshold rise `[^pdk-07]`; tool line the 8250's grades; Not
  public from Open questions 1.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03` (the category repeat), `pdk-07`,
  `skw-01` (glance); numbers 0.42×2 (the W/L cells repeat W = 0.42 µm on each of its three rows),
  0.541, 0.700, 8250 (glance), 5 (the OQ label "Halo on the 5 V NMOS", from the bullet's words); quote
  "NTM shadowing" (the OQ label, from the bullet's words); hedges "inference"×2, "not public" (glance).
  **LOST `number_order`** — the base's one test-tile sentence (0.534, 7, 8, 0.707, …, 0.1, 100) is
  now five table rows that put W/L first, plus the hedge line; pairings checked above. ADDED
  number_order: the five rows. Declared `--allow-added markers,numbers,quotes,hedges,number_order`;
  the LOST line is the only one left and is this table's transposition.
* **Marker coverage.** 17 flags, all read: the dash-pair move ("infer" now in the next sentence, as in
  the guide's example); the category repeat; split halves whose base marker belonged to the other clause
  (Lu/Rafferty – Machala; txt-01 – AMD patent; Large tilts – the beam; the NTM-shadowing estimate – the
  larger-tilt reasoning); "So the absence …" (our conclusion, no marker in the base); glance and label
  lines.
* **Caps**: para > 100 3 → 0; item > 60 8 → 0; sentence > 45 9 → 1. Left: the GSD head (48 w with the
  tool name; the pilot form keeps it whole).

### 067 ASTIS — done

* **Lead.** First sentence (40 w) split before ", and cleans the wafer" → "It cleans the wafer …"
  (R-GLANCE step 8, the form batch 4 used on 051/054); now 23 words. "…in the tip module; in this
  reference …" split at the semicolon. Lead 95 words, one paragraph.
* **R-H3 not applied.** The passage after the figure (136 words) is industry-typical and inferred
  (resist thickness "inferred on the NTM page", the dose "typical", the surface "we infer"); none of
  the four titles is true of it (R-H3 step 6). **R-PARA** split it before "The surface under the resist
  is, we infer, …" (the resist / the surface); that sentence split at its semicolon ("No metal is
  present, …"): "we infer" sat inside the first clause and stays there.
* **R-CATEGORY.** Classification sentence (19 w) alone. The rest is the category page's general account
  (implanted resist, Fujimura, "popping") and one comparison with other steps' strips: not "specific to
  this step" (R-CATEGORY step 2), so plain paragraphs. The 58-word account sentence split at its colon
  and before ", and, on the category page's account" ("On the category page's account, …"); each piece
  keeps its own marker (only the Fujimura clause had one).
* **R-PARA / R-SENTENCE (Why).** The 153-word paragraph split before "The crust also carries" (the next
  resist / what the crust carries). The HVNTM sentence split at its dash ("It is a film that …",
  subject + verb added). The flakes sentence: its dash pair (the patent quotation) becomes the following
  sentence "One patent has the implant-hardened surface "…".[^pat-strip-mosel]" (R-SENTENCE step 1),
  the marker with its quotation.
* **R-HEDGE.** Italic lead-in, word for word.
* **R-PARA step 4 (How items).** "Plasma ash, two stages" (185 w): lead "Downstream (remote) microwave or RF
  oxygen plasma."; continuation 1 the two-patent "Because …" sentence, its dash-pair quotation (a
  lowercase quotation from the same patent) given the neutral lead-in "The patent adds:" (R-SENTENCE
  step 7) and "until the crust is opened, after which …" as "The cool stage runs until …" (subject + verb
  added); continuation 2 Fujimura, Yegnasubramanian and SkyWater's asher list; continuation 3 "Downstream
  operation is used because …". "Wet strip and clean" (76 w): split at the semicolon; continuation from
  "SC-1 …".
* **R-TOOLS.** Four tools → `Tool | Evidence` recap table above the list (grades as the page gives them;
  the AIT row keeps "(our reading)"). Ashers: the head "— all named on SkyWater's facilities page with
  their gases and temperatures" is this reference's gloss of SkyWater's list, so the pilot form (as 051):
  head kept, *Tool exists:* and *Runs this step:*, and "The Iridia's H₂/N₂ chemistry … fit a cool first
  stage best." as the continuation paragraph. Akrion, DNS/FSI: heads keep the quotation with our
  "for the SPM/SC-1 sequence" / "as alternative clean tools", grade as sub-bullet. AIT: head keeps "our
  reading of "AIT" …", grade as sub-bullet (as 009).
* **R-RELATED.** "Companion strips in this module:" → "Same module: companion strips …" (HVASTIS,
  LDASTIS, and PDIS/NSDIS all carry this module's Phase cell).
* **R-OPENQ.** Labels "Ash recipe and wet sequence", "Oxide-thinning budget", "Which asher", "Tip dose";
  text unchanged.
* **R-GLANCE.** Does/Why from the lead and the Why section (the Why line drops the 40° figure rather than
  carry a number without its marker); Public numbers "none published for this strip" plus the next
  resist's 0.3 µm `[^pdk-03]`; tool line the ashers' grades; Not public from Open questions 1 and 3.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 0.3, quote
  "Photoresist thickness for HV Tip Implants", hedges "inference" (glance), "not public" (glance label),
  "inference" and "our reading" (recap table). Declared `--allow-added markers,numbers,quotes,hedges`:
  clean.
* **Marker coverage.** 14 flags, all read: split halves whose base marker sat on another clause (the
  "popping" account; the flakes sentence; "The cool stage runs until …", which follows three quotation
  markers in the base and had none of its own; SPM / SC-1); glance and label lines.
* **Caps**: para > 100 3 → 0; item > 60 2 → 0; sentence > 45 6 → 0.
