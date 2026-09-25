# Progress — readability batch 4, steps 048–063 (`topic/rd-steps-048-063`)

Writer: Opus. Started 2026-09-26 from `main` at `e75c04e8`. Guide: `docs/plans/readability-guide.md`
(§1, §2, §4.1, §5, §6, §7, §8). Model pages: 018, 030, 043. One commit per page.

## Method, every page

* Baseline build and tiles (desktop, 400 px) of all 16 pages before any edit.
* Preservation: `uv run python tools/check_preserved.py --base main <page> --allow-regrouped` first, with
  no other allowance; every ADDED line is named below; then the named categories are declared.
  `--allow-dropdown-edits` is never used. The batch has **no hand-written in-force note**: the only
  `{dropdown}` on the 16 pages is inside the generated index-links block of 048, untouched.
* Marker coverage: a script (`tmp/readability/markcov.py`, git-ignored) lists every new sentence that
  is not verbatim in the base, pairs it with the base sentence it came from, and flags a lost marker
  or a hedge word not in the piece; every flag is read by eye and explained per page.
* Caps: `tmp/readability/caps.py` (git-ignored) — `measure.py`'s blocks and `measure5.py`'s sentence
  split, §1 caps (paragraph > 100, item > 60, sentence > 45, cell > 25), `{figure}` text excluded
  (G10), generated block and `## References` excluded.
* Checkers after each page: `check_steps`, `check_refs`, `check_inforce`, `check_machines`,
  `check_materials`, `check_masks`, `gen_index_links --check`, `gen_figures --check`; `-W` build;
  tiles at 1280 px and 400 px.

## Batch measurement (§1 caps, open text, figure text excluded)

Before (16 pages at `e75c04e8`): paragraphs > 100: 45; list items > 60: 49; sentences > 45: 109;
table cells > 25: 0. After: see the batch summary at the end.

## Pages

### 048 SAGD — done

* **R-H3.** `### What the public record shows` after the figure caption, over the PDK/SkyWater
  evidence paragraphs and the "One layer, not a stack." paragraph (≈ 250 words, one subject: what
  the public numbers and statements say about the film). The run-in "**One layer, not a stack.**"
  labels a single paragraph, so it stays bold.
* **Lead.** First sentence split at its colon (59 → 23 words, "It is" added, R-SENTENCE step 7);
  lead split into two paragraphs before "The film is undoped as deposited" (a new subject). The lead
  is now 121 words (was 119: the two added words); §1's 120 cannot be met without dropping words.
  **The sentence "The film is undoped as deposited; …" is unchanged, verbatim** (see Content problems).
* **R-PARA.** The 110-word evidence paragraph split at the change of source, with run-in labels
  "**PDK figures.**" / "**SkyWater's capability list.**" (evidence sequence, R-PARA step 3).
* **R-LIST.** "Two other gate constructions … : a polycide gate (…) and a stacked-amorphous-silicon
  gate, in which …" → two bullets, the item's own first words bolded in place; `[^wu-1993]`, which
  ended the enumerating sentence, stays on the lead-in before the colon (R-LIST step 1).
  "The self-aligned polysilicon gate … since the early 1970s: it survives …, it lets …, and its work
  function …" → three plain bullets (no invented labels; the only possible labels repeated the item
  word for word), `[^wiki-poly]` on the lead-in.
* **R-CATEGORY.** Classification sentence (30 words, with `[^skw-01]`) as its own paragraph; the rest
  begins "what is specific here is that", so it stays one paragraph with no label (step 3).
* **R-PARA step 4 (items).** "Smoother, finer-grained film" (164 w): lead ends at the colon, the rest in
  two indented continuation paragraphs, every word kept. "Temperature" (70 w), "Thickness" (62 w),
  "Crystallisation" (79 w): lead + indented continuation paragraph.
* **R-SENTENCE.** "Deposition rates … an hour; the batch furnace …" split at the semicolon.
  Crystallisation sentence (71 w) split at its semicolon, and its 20-word parenthetical closed as its
  own sentence "(Their films … amorphous.)" (R-SENTENCE step 7); `[^iverson-1987]` **repeated** on
  the Iverson and Reif sentence so both pieces keep it (declared addition).
* **R-HEDGE.** Scope sentence as the italic lead-in, word for word.
* **R-TOOLS.** One tool (Aviza furnace): *SkyWater says:* (verb-first, the two quotations),
  *Tool exists:*, *Runs this step:*; the "Whether the furnaces are vertical … not stated on
  SkyWater's page; a used-equipment listing … (weak)" sentence is not SkyWater's, so it is a
  continuation paragraph. Under four tools: no recap table.
* **R-OPENQ.** Four labels, text after each label unchanged: "Deposition conditions", "Seed or
  interface layer", "Crystallisation anneal", "Batch furnace or single-wafer chamber".
* **R-RELATED.** "Previous: … Next: …" (one bullet, two relationships) → two bullets; the
  doped/capped/patterned run (P1I … IOX45, all Phase "gate and poly resistors") → `Same module:`.
  The SONOS-stack bullet and the FILOX/ISONIT bullet keep no label: no label in R-RELATED's list is
  exactly true of them.
* **R-GLANCE.** Does (hedged "on this reference's reading (inference)", the page's paragraph-2
  wording, not the lead's unhedged "amorphous"); Why (closing "Without this step…" sentence and the
  first benefit's label); Public numbers 0.18 µm `[^pdk-03]`, 48.2 Ω/sq `[^pdk-08]`; tool line with
  the page's grades; Not public from Open questions bullet 1. The box does not mention "undoped".
* **Skipped.** R-TABLE on the evidence paragraph (only three values, two of them the same 0.18 µm;
  a table would repeat the source names); R-REPEAT (no 10-word repeat across H2s that is not the
  cross-page supplier sentence).
* **Preservation** (`--allow-regrouped` only): ADDED markers `iverson-1987` (the repeat above),
  `pdk-03`, `pdk-08`, `skw-01` (glance); numbers 0.18, 48.2 (glance); hedges "inference" ×2 (glance
  Does and tool lines), "not public" (the glance label); number_order (0.18, 48.2) (glance).
  REGROUPED ('0.18', '200'): the Thickness sentence split at its semicolon — same digits, same order.
  Final run declared `--allow-added markers,numbers,hedges,number_order`: clean.
* **Marker coverage.** 13 flags, all read: the three list items (markers on the lead-in, by rule);
  the colon lead of "Smoother, finer-grained film" (its evidence and markers follow in the next
  paragraph, as in the base sentence); "Deposition rates … an hour" (the base sentence's marker
  covered only the AVP-8000 quotation); "The later furnace … steps" (the base marker sat before that
  clause); four labels; "we infer" correctly in the second sentence of the lead with "from silane".
* **Caps** (open text): para > 100 3 → 0; item > 60 5 → 0; sentence > 45 6 → 0.

### 049 RPM — done

* **R-H3.** `### What the public record shows` after the figure caption, over the PDK mask/layer and
  resistor-family evidence and the "Two facts" argument (≈ 270 words).
* **R-PARA.** The 124-word PDK paragraph split at the change of subject, labels "**Mask and
  layers.**" / "**Resistor families.**" (evidence sequence). "Why this step exists" paragraph 1
  (155 w) split into three at its seams (the need; the literature; the PDK's device), no labels
  (narrative).
* **R-LIST.** "Two facts fix what the mask must do. First, … Second, …" → lead-in with a colon and two
  plain bullets that keep "First," and "Second," and every word; the conclusion "We therefore
  infer …" is the paragraph after the list. No bold labels: the only labels available would be new
  wording (batch-3 review, Low item on invented labels). The rpm rules (rpm.3, .8, .7, .6, .4; one
  61-word sentence) → a four-bullet list, `[^pdk-periph]` on the lead-in before the colon, every
  word kept except the list-joining "and" before the rpm.6 clause; "but" kept before rpm.4. A list,
  not an R-TABLE `Rule | Constrains | Value` table: the rules are clauses ("must not straddle …
  and must keep 0.200 µm from it") that do not fit those columns without new wording; 030's rule
  list (merged) is the precedent.
* **R-SENTENCE.** "If the resistor bodies received … let alone 2000 Ω/sq, because counter-doping …"
  (49 w) split: "This is because counter-doping …" (subject + verb added; no marker in the base
  sentence).
* **R-CATEGORY.** Classification sentence (34 w) alone; the rest is one sentence ("Its minimum
  feature …", second paragraph, no label) and one "What is specific to this instance is …" sentence
  (its own label, step 3), so no "Specific to this step:" list.
* **R-PARA step 4.** "Exposure" (73 w): lead "i-line step-and-repeat exposure." + two indented
  continuation paragraphs at the resolution/reflectivity seam.
* **R-HEDGE.** Italic scope lead-in. **R-TOOLS.** Three tools (no recap table): i-line stepper
  (*SkyWater says:* verb-first); Tracks and Overlay/CD keep their `[^skw-01]` on the head (their
  bullets quote nothing, as on 030); "Which track serves which tool is not public." becomes the
  Tracks continuation paragraph (it is not a grade).
* **R-OPENQ.** Labels "Regions covered", "Tone, resist and tool", "Alignment marks", "Other
  resistor bodies"; text after each unchanged.
* **R-RELATED.** Previous/Next split (one bullet, two relationships); "Reverse-tone partner:" →
  "Same module: reverse-tone partner RRPM …" (RRPM/URPM are in the module); the "Previous mask step
  …; next mask step …" bullet and the "Mask page:" bullet → one `Mask:` bullet keeping both glosses.
  The resistor-body bullet (P1M/P1ME, NPCM, LICM1, PSDM) keeps no label: it mixes modules and no
  single label is true of it.
* **R-GLANCE.** Does carries "we infer" (the page's "We therefore infer that `RPM` protects the
  resistor bodies"); Public numbers are the RPM geometry (RPMCD/RPMCDSP `[^pdk-03]`, rpm.3
  `[^pdk-periph]`); Not public from Open questions 1–2.
* **Skipped / left over the cap.** "Resist coat" item (65 w): its only seam is before "Because the
  implant it masks …", and R-PARA step 2 forbids a paragraph that opens with a connective. The
  "Second, …" bullet is 45 words (46 counting the `*`).
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `pdk-periph`, `skw-01`,
  numbers 1.27, 0.84, 0.200, 3 (rpm.3), hedges "we infer", "inference", "not public", identifier
  `P1I`, number_order (1.27, 0.84, 0.200, 3) — all the glance box. REGROUPED: the rpm rules sentence
  → the four bullets, same digits in the same order (0.200/3; 8/0.200/7; 0.200/6; 0.110/4).
  Final run declared `--allow-added markers,numbers,hedges,number_order,identifiers`: clean.
* **Marker coverage.** 4 flags: the rules lead-in/list (marker on the lead-in by rule; "may" is in
  the rpm.6 bullet); two Open-questions labels. Nothing lost.
* **Caps**: para > 100 5 → 0; item > 60 2 → 1 (Resist coat, above); sentence > 45 2 → 0 (1 at
  45 + bullet marker).

### 050 P1I — done

* **R-H3.** `### What the public record shows` after the figure caption, over the PDK polarity/sheet-
  resistance evidence and the implant-physics paragraph (≈ 230 words).
* **R-PARA / R-SENTENCE.** The 149-word evidence paragraph: its 62-word sentence split at the
  semicolon after "48.2 Ω/sq" (each half keeps its own markers); paragraph split before "For a
  0.18 µm film". The split needs R-PARA step 5: "that is a resistivity" → "that sheet resistance is a
  resistivity" (the pronoun gets its noun back; no number added). "Why" closing paragraph (117 w,
  one 77-word sentence) split at the colon after "follows, we infer, from the gate cap" (the hedge
  stays in its sentence; "The PDK keeps …" keeps `[^pdk-periph][^pdk-03]`), and the paragraph split
  before "We infer that a capped gate …".
* **R-CATEGORY.** Classification sentence (42 w) split at its em dash: "`P1I` is … *high-dose,
  low-energy* class." (14 w) alone; "The category page groups it …" second paragraph (a category-page
  statement, not specific to the step); the two "It is the first … / It is also the first …"
  sentences under "**Specific to this step:**".
* **R-PARA step 4.** "Be a good conductor" (68 w): lead "We infer that SKY130 does not silicide its
  gates." (split at the colon; the hedge stays with the claim), evidence as continuation paragraph.
  "Not deplete" (75 w): lead + continuation at "Schuegraf, King and Hu …".
* **R-HEDGE.** Italic scope lead-in (including "(SKY130 values are not public)").
* **R-TOOLS.** Axcelis GSD: *SkyWater says:* holds only the two quotations with `[^skw-01]`; the gloss
  "the two tools on its public list whose dose ranges reach 10¹⁵ cm⁻²; the medium-current 8250 is
  listed only to 1e14.[^skw-01]" is ours, so it is the continuation paragraph ("These are" added
  as subject + verb), followed by the Axcelis vendor sentence. Grades unchanged.
* **R-OPENQ.** The 94-word "n⁺ or p⁺ PMOS gates?" bullet (55-word first sentence): its four PDK facts
  become sub-bullets under "The PDK:", each with its own marker and every word and comma kept; the
  conclusion "We therefore read …" and "No public source states this …" follow as a continuation
  paragraph in the same order (question, evidence, reading). Labels added to the other three,
  text unchanged.
* **R-RELATED.** Previous/Next split; "Film: …; resistor implants: …" and "Cap and pattern: …" (all
  in the module) → one `Same module:` bullet keeping the three glosses; "Activation:" (IOX45,
  TIPRTAD, RTAD — later steps that activate this implant) → `Feeds: activation at …`. The
  channel-implant bullet (LVTPI, PNCHI, earlier steps) keeps its own gloss and no label.
* **R-GLANCE.** Does/Why from the lead and the "three jobs" sentence; Public numbers 48.2 Ω/sq
  `[^pdk-08]` and the e-test limits `[^pdk-07]`; Not public from Open questions.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-07`, `pdk-08`, `skw-01`, numbers
  48.2, 42.2–55.8, hedges "inference", "not public" — glance box. REGROUPED: the evidence sentence
  (48.2 | 42.2–55.8, 0.094, 0.15), the SkyWater quotations/gloss (same digits, same order), the
  Open-questions PDK facts (npc.4/0.2; −1.05/+0.54). Declared `markers,numbers,hedges`: clean.
* **Marker coverage.** 8 flags, all explained above (splits at seams where each piece keeps the
  markers of its own clause; labels).
* **Caps**: para > 100 3 → 0; item > 60 4 → 0; sentence > 45 4 → 0.

### 051 P1IS — done

* **R-H3.** Not applied. The passage after the figure ("Two things make this strip different …") is
  generic reasoning; none of the four step-page H3 titles (R-H3 step 3) is true of it, and "What the
  public record shows" is excluded over industry-typical text. R-LIST gives it structure instead.
* **R-LIST.** "Two things make this strip different … First, … Second, …" → lead-in with a colon and
  two plain bullets keeping "First," / "Second," (no invented labels). The first item's 48-word
  sentence split at ", so the carbonised crust …" → "So the carbonised crust …" (inside the bullet,
  not a new paragraph); the second item's "There is no oxide …" sentence is its indented continuation
  paragraph (item 61 → 20 + 33 words).
* **R-CATEGORY.** Classification sentence (12 w) alone; the category-page sentence and the "other
  members of this class" sentence stay together as the second paragraph (one sentence about this
  step remains, so no "Specific to this step:").
* **R-PARA.** "Why" paragraph (134 w) → three paragraphs: why the resist must go; the crust
  literature; popping. No labels (narrative).
* **R-PARA step 4 / R-SENTENCE.** "Two-step plasma ash" (132 w): lead sentence (37 w, cannot be
  shortened without rewording its em-dash quotation) + two continuation paragraphs (literature;
  SkyWater's ashers and the consequences). "Wet strip and clean" (153 w): lead (41 w, same reason) +
  two continuation paragraphs; its 74-word sentence split at "), and SC-1 etches" → "). SC-1 etches"
  (only "and" dropped; `[^kern-1990]` and `[^lee-kt-1999]` each stay on their own clause).
  **Skipped:** the 20-word parenthetical "(of the order of a nanometre — a typical industry figure;
  Kern's review … thickness)" stays a parenthetical: it is the hedge on "a thin chemical oxide" and
  closing it as its own sentence would detach it from the value it qualifies.
* **R-HEDGE.** Italic scope lead-in.
* **R-TOOLS.** Four tools → recap table `Tool | Evidence` (grades as the page gives them; the AIT row
  keeps "(our reading)"). Ashers, Akrion bench and DNS/FSI keep their original head text with the
  SkyWater quotation or gloss (the pilot form "head already carries the quotation"); grades go under
  *Tool exists:* / *Runs this step:* word for word. AIT: *SkyWater says:* holds the posting quotation,
  verb-first with the page's own verb ("reads … in a *Defect Technician 2* posting"); "We read "AIT"
  as …" is our reading, so it is the continuation paragraph.
* **R-OPENQ.** Labels "Ash recipe and wet sequence", "Silicon-loss budget", "Which asher".
* **R-RELATED.** "Companion strips in this module: …; the other high-dose strips are …; the
  light-dose exemplar is …" names two relationships → `Same module:` (PRIS, UPRIS) and
  `Same category:` (PDIS, NSDIS, LVTNIS — strip steps elsewhere in the flow).
* **R-GLANCE.** Public numbers "none published for SKY130" (the only numbers are tool specifications
  and industry-typical figures). Tool line: the three ashers with the page's grades.
* **Preservation** (`--allow-regrouped` only): ADDED marker `skw-01`, hedges "inference" ×2 (glance,
  recap table), "not public" (glance label), "our reading" (recap table row), identifiers `P1I`,
  `SKY130` (glance). No LOST. Declared `markers,hedges,identifiers`: clean.
* **Marker coverage.** 6 flags, all explained: the SC-1 sentence split (each clause keeps its own
  marker); "So the carbonised crust" (consequence of the dose; the base had no marker there); "We
  read "AIT" …" (the base marker `[^job-06]` stood before "; we read", on the quotation); a label.
* **Caps**: para > 100 2 → 0; item > 60 2 → 0; sentence > 45 2 → 0.

### 052 RRPM — done

* **R-H3.** `### What the public record shows` after the figure caption, over the mask-table
  reading and the test-tile evidence (≈ 320 words).
* **R-PARA / R-SENTENCE.** Mask-table paragraph (159 w) → three paragraphs at its seams (the table;
  "That a reverse-tone mask is used is itself our inference: …"; "We infer that the reverse reticle is
  derived …"), and the last one's 59-word sentence split at its semicolon ("… their own (URPM,
  UPRI). The PDK says only …"; each half keeps its marker, "We infer" stays with its claim).
  Test-tile paragraph (158 w): first sentence (51 w) split at its colon — "Beyond the step list, one
  public document names the mask." is a pointer whose source is named and cited in the very next
  sentence (no marker added); paragraph split before "The published measurements …"; that 83-word
  sentence split into three: the readings with "(our extraction … ±0.1 V).[^raw-data-passives]";
  "They are inside the limits of the PDK's e-test table …[^pdk-07]" ("They are" added; "They" is the
  extracted readings, so the hedge still governs them); "The tile's 0.33 µm structure …[^pdk-periph]"
  (the base's em dash).
  "Why" paragraph 1 (108 w): split after the first sentence; its 52-word sentence split at ", and
  Mandurah" (each study keeps its own marker). "Why" paragraph 2 (161 w) → three paragraphs; its
  62-word sentence split at "— so the enclosure" → "edge. So the enclosure …" (the conclusion keeps
  `[^pdk-periph]`; "we infer" stays on "part of it is … set by … the `rpm` edge", as in the base);
  the 58-word literature sentence split at ", and Tsang et al.".
* **R-CATEGORY.** Classification sentence (44 w, with its em-dash pair and `[^pdk-03]`) alone; the
  "What is specific to this instance is the tone …" sentence is its own label (step 3). The
  classification sentence stays over the 35-word target: shortening it would need rewording.
* **R-PARA step 4.** "Alignment" (103 w): lead sentence + one continuation paragraph.
* **R-HEDGE, R-TOOLS** (three tools, grades verbatim under *Tool exists:* / *Runs this step:*; the
  bullets quote nothing SkyWater said, so no *SkyWater says:*), **R-OPENQ** (labels "The `urpm`
  bodies", "Tone, resist and tool", "Sizing bias").
* **R-RELATED.** Previous/Next split; "Complement: RPM. The ultra-high-resistance flavour …" →
  "Same module: complement RPM. …" (RPM, URPM, UPRI are in the module); mask bullets → one `Mask:`
  bullet keeping both glosses; the P1ME/NPCM/LICM1 bullet keeps no label (mixed modules).
* **R-GLANCE.** Does carries the page's "our inference" on the reverse-tone reticle (the caption's
  and the second paragraph's hedge); the open RRPM question (does it open `urpm`?) is in Not public,
  as the page leaves it.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, numbers 1.27, 0.84,
  hedges "inference" ×2 (glance Does and tool line), "not public" — glance box. REGROUPED: the
  sentence splits above, same digits in the same order. Declared `markers,numbers,hedges`: clean.
* **Marker coverage.** 14 flags, all read: every split piece keeps the markers of its own clause;
  the one uncited piece is the pointer "Beyond the step list, one public document names the mask."
* **Caps**: para > 100 4 → 0; item > 60 1 → 0; sentence > 45 6 → 0.

### 053 PRI — done

* **R-H3.** `### What the public record shows` after the figure caption (the PDK target — the page's
  own "The target is public" — and the illustrative estimate); in `## Why this step exists`, over the
  313-word test-tile passage, `### How the sheet resistance is estimated` (the passage extracts a
  sheet resistance from the published sweeps and compares it with the PDK's values; titles must be
  unique on the page, so the first title could not be reused there). "**Single or multiple
  implants.**" labels one paragraph and stays bold.
* **R-LIST.** The test-tile structures ("carries the structures …: eleven modules of "…" … pairs, and
  a van der Pauw structure measures "…"") → lead-in with `[^raw-data-testtile-pads]` before the colon
  and two plain bullets (only "and" dropped; the double space inside the quoted "P+  POLY" kept).
* **R-TABLE (inside an Open-questions bullet, R-OPENQ step 2).** "Resistor ends" (81 w, a 67-word
  "respectively" sentence): the three measured/nominal pairs → an indented `Width (µm) | Measured
  ends (Ω) | E-test nominal ends (Ω)` table; the lead-in keeps every hedge ("(the median 4-square
  resistance less four squares of body; our extraction)", "(our arithmetic)") and both markers before
  its colon; the question "How that divides … is not public." stays last, unchanged. Wording added
  by the conversion: "at the values below", "against those that" (for "against the 68, 256 and
  392 Ω that"). Pairing checked by hand: 5.73 µm ↔ about 70 ↔ 68; 1.41 µm ↔ 190 ↔ 256; 0.69 µm ↔
  390 ↔ 392 ("about" stays on the first value, where the base wrote it).
* **R-PARA / R-SENTENCE.** Target paragraph (123 w) split before "For a 0.18 µm film". Test-tile
  passage: the 93-word extraction sentence split at its semicolon, **the whole hedge "(our extraction
  from the published measurements; the files record no temperature, date or wafer)" repeated** on
  the first half with its marker (R-SENTENCE step 5); the e-test sentence split at "— and the same
  arithmetic" (`[^pdk-07]` repeated so both halves keep it); the 58-word measured sentence split at
  ", and every measured structure" with "(our extraction)" and `[^raw-data-passives]` repeated on the
  first half. "Why" paragraph 1 (171 w) → three paragraphs; the 73-word literature sentence split at
  ", and Wright et al." (the em dash before "Lu et al." kept, so the claim and its first two studies
  stay in one cited sentence).
* **R-CATEGORY.** Classification sentence (15 w) alone; the one remaining sentence as the second
  paragraph, split at its colon (53 → 9 + 44 w; `[^seto-1975]` stays on the steepness clause).
* **R-PARA step 4.** "Dose" (66 w): lead + continuation at "Dose control is the whole point".
* **R-HEDGE, R-TOOLS** (*SkyWater says:* the two quotations; the Semiconductor Online sentence about
  the 8250HT is a vendor description, so it is the continuation paragraph), **R-OPENQ** (labels
  "Species, energy, dose and tilt", "The `urpm` bodies", "Which implanter", "How much is set
  here", "Resistor ends").
* **R-RELATED.** Previous/Next split; "Protected from the gate implant at RPM / P1I; … UPRI" →
  `Same module:` (all three in the module); the "Later steps that touch the resistor" bullet (mixed
  modules) keeps its own gloss and no label.
* **R-GLANCE.** Public numbers are the PDK's 300 Ω/sq and 319.8 Ω/sq; the extracted values are not
  in the box. Tool line keeps "which one is not stated".
* **Left over the caps (known items).** "For a 0.18 µm film, 300 Ω/sq corresponds to … — an
  illustrative estimate, not a SkyWater number." (51 w): its closing hedge covers the whole chain, so
  a split would leave part of it unhedged. The extraction-method sentence "Taking the difference …
  narrower than drawn (our extraction …; the files record no temperature, date or wafer)." (64 w with
  the repeated hedge): one method, no seam. "Every measured structure 0.69 µm or wider … (our
  extraction)." (46 w). The "Resistor ends" lead-in (49 w including its two hedges).
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-07` ×2 (glance; the e-test split),
  `pdk-08`, `skw-01` (glance), `raw-data-passives` ×2 (the two repeated extraction hedges); numbers
  300, 319.8 (glance), 8250 (glance tool name); hedges "not public" (glance label), "our extraction"
  ×2 (the repeats). REGROUPED: all sentence splits, same digits in the same order. **LOST
  number_order** ('70', '5.73', '190', '1.41', '390', '0.69', '4', '68', '256', '392'): the
  resistor-ends table puts the width first in each row (the rule-table pattern the batch-2 and
  batch-3 reviews accepted); every pairing checked by hand above; "4" (4-square) stays in the
  lead-in. Final run declared `markers,numbers,hedges,number_order`; the LOST line remains and is
  explained here.
* **Marker coverage.** 12 flags, all read: labels; the colon split in Step category (the marker's
  clause keeps it); the test-tile list (marker on the lead-in, by rule); pieces whose base marker
  covered a different clause.
* **Caps**: para > 100 3 → 0; item > 60 3 → 0; sentence > 45 8 → 4 (above).

### 054 PRIS — done

* **R-H3.** Not applied (as on 051: the passage after the figure is generic reasoning; no step-page H3
  title is true of it). R-LIST structures it.
* **R-LIST.** "The resist being removed differs from the one at `P1IS` in two ways. It is …; and it
  has taken …" → lead-in with a colon and two plain bullets ("; and it has" → "It has"; nothing else
  changed); the BF₂/residue sentences follow as a paragraph, split at their semicolon. "Two points
  are specific to this strip. First, … Second, …" → lead-in and two bullets keeping "First," /
  "Second,"; the first item's 60-word sentence split at its colon ("… treat them differently. An
  SC-1 step …", `[^lee-kt-1999]` stays on the SC-1 clause) with the second half as the item's
  continuation paragraph.
* **R-CATEGORY.** Classification sentence alone; the one remaining sentence as the second paragraph.
* **R-SENTENCE / R-PARA step 4.** "Plasma ash" (162 w, one 83-word sentence): split at the semicolon
  after "finishing hot for the bulk"; the em-dash pair holding the Fujimura measurement becomes its
  own sentence after the claim (R-SENTENCE step 1, as in the guide's 066 example), and
  **`[^fujimura-1991]` is repeated on the claim "Water-vapour-containing chemistries ash faster than
  dry oxygen,"** so the claim keeps its source (declared addition); "which is why a fab … reaches for
  them" stays after it, unmarked, as in the base. Lead (27 w) + two continuation paragraphs.
* **R-HEDGE, R-TOOLS** (three tools: grades verbatim; AIT as on 051 — *SkyWater says:* holds the
  posting quotation with the page's verb "reads", our reading "We read "AIT" as …" is the continuation
  paragraph), **R-OPENQ** (labels "Ash and wet recipes", "Protection of the resistor bodies", "Which
  asher").
* **R-RELATED.** "Companion strips: P1IS, UPRIS; the strip after PNCHI is PCHIS." names two
  relationships → `Same module:` companion strips; the PNCHI/PCHIS clause as its own bullet with no
  label (it links an implant as context, so "Same category:" would not be true of every link in it).
* **R-GLANCE.** Public numbers "none published for SKY130"; tool line with the page's grades.
* **Preservation** (`--allow-regrouped` only): ADDED markers `fujimura-1991` (the repeat above),
  `skw-01` (glance); hedges "inference" (glance), "not public" (glance label); identifier `SKY130`
  (glance). No LOST, no REGROUPED. Declared `markers,hedges,identifiers`: clean.
* **Marker coverage.** 10 flags, all read: list items and split pieces whose base marker belonged to
  a different clause; "We read "AIT"…" (base marker on the quotation); labels.
* **Caps**: para > 100 2 → 0; item > 60 1 → 0; sentence > 45 4 → 1 (the "Second, …" bullet, 45 words
  plus the bullet marker).

### 055 URPM — done

* **R-H3.** `### What the public record shows` after the figure caption, over the PDK device/layer
  record, the mask-table reading and the test-tile evidence (≈ 290 words). The run-in
  "**Interaction with the other resistor masks.**" (107 w) had to be split (§1 cap); it then
  introduces two paragraphs, so it becomes `### Interaction with the other resistor masks`, same
  words (R-H3 step 4). Its text — this page's reading that the `urpm` bodies receive only `UPRI`,
  and the pointer to RRPM's open question — is unchanged (the S5 figure agent's note; see Content
  problems under 052).
* **R-PARA / R-SENTENCE.** Device paragraph (133 w): its 59-word sentence split at the semicolon,
  **`[^pdk-07]` repeated** on the first half (its quotation is the PDK's); paragraph split before
  "The extraction table …". Mask-table/test-tile paragraph (158 w) → three paragraphs; its 64-word
  measurement sentence split at the semicolon with **"(our extraction from the published
  measurements)" and `[^raw-data-passives]` repeated** on the first half (R-SENTENCE step 5); the
  second half keeps the full original hedge "(our extraction from the published measurements; see
  UPRI)". "Why" paragraph 1 (181 w) → three paragraphs; the 63-word sentence split into three ("It
  also cannot be made by under-dosing … mask." / "This is because the two values differ … curve."
  with all three markers / "So they need separate, individually controlled doses."); the 55-word
  Lane and Wrixon sentence split at ", which is consistent with" → "This is consistent with …"
  (`[^lane-1989]` stays on the design space, `[^pdk-07]` on the PDK's caution — each marker on its
  own clause, as the base order implies). "Why" paragraph 2 (121 w): split at the semicolon before
  "Tsang et al.".
* **R-CATEGORY.** Classification sentence (31 w) alone; the one remaining sentence as the second
  paragraph, split at its colon (no markers in it).
* **R-HEDGE, R-TOOLS** (three tools, grades verbatim), **R-OPENQ** (labels "Separate reticles", "What
  the `urpm` bodies receive", "Process option", "Tone, resist and tool").
* **R-RELATED.** Previous/Next split; "The other resistor masks: …" → "Same module: the other
  resistor masks, …"; mask bullets → one `Mask:` bullet; the P1ME/NPCM/LICM1 bullet unlabelled.
* **R-GLANCE.** Not public states the `urpm` route as "this page's reading is an inference", matching
  Open questions ("… (the reading used here) is inferred") and 052's open question.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-07` ×2 (glance; the device split),
  `pdk-08`, `pdk-periph`, `skw-01` (glance), `raw-data-passives` (the repeated hedge); numbers 2000,
  1.270, 0.840 (glance); hedges "inference" ×2, "not public" (glance), "our extraction" (the repeat);
  number_order (2000, 1.270, 0.840) (glance). REGROUPED: the measurement and sheet-resistance
  sentences, same digits in the same order. Declared `markers,numbers,hedges,number_order`: clean.
* **Marker coverage.** 6 flags, all read: "It also cannot be made …" and "So they need …" frame the
  cited reason sentence between them; "Its resistance is dominated by grain-boundary barriers …"
  had no marker of its own in the base (the Tsang marker belongs to the Tsang clause).
* **Caps**: para > 100 5 → 0; item > 60 0 → 0; sentence > 45 7 → 3 (47 w: the measurement sentence
  with its repeated hedge; 46 w: the Tsang/Lane sentence; 46 w: the "Alignment" item, base text).

### 056 UPRI — done

* **R-H3.** `### What the public record shows` after the figure caption (the PDK target and the
  illustrative estimate); in `## Why this step exists`, `### How the sheet resistance is estimated`
  over the 332-word test-tile passage (the same title and reason as on 053).
* **R-LIST.** "The target is public and unusually explicit: the PDK says …,[^pdk-07] the extraction
  table gives …,[^pdk-08] and the drawn layer `urpm` is described as …[^pdk-06]" → three plain
  bullets, each keeping its own marker ("and" dropped). The test-tile structures → lead-in with
  `[^raw-data-testtile-pads]` before the colon and two plain bullets (as on 053; the double space
  inside "P-  POLY" kept).
* **R-TABLE (measured against the same geometry elsewhere).** The 150-word sentence listing the five
  high-reading short structures → lead-in "The short structures scatter … : among the half- and
  one-square resistors, five read from about twice to more than sixty times the value of the same
  geometry elsewhere on the tile (our extraction from the published measurements; the files are named
  by module and pad in the repository):[^raw-data-passives]" (the base's words, the em-dash
  enumeration moved into the table, the hedge and marker kept whole on the lead-in), then a
  three-column `:::{table}` (`Structures (width, squares) | Reading | Same geometry elsewhere`;
  `:widths:` because the first column is prose). Cells keep the base's words: "0.59 kΩ for the same
  geometry in module 6215" → "0.59 kΩ in module 6215" under the "Same geometry elsewhere" header;
  "against" is carried by the header. The closing "as in the 300 Ω/sq set, the 2.85 µm pair of module
  6224 …" is the paragraph after the table, with its two markers and "(our extraction)". Every
  pairing checked by hand: 6222 pads 1-2/1-3 (0.69 µm, half) 2.8–3.0 kΩ ↔ 0.59 kΩ (6215); 6219 pad
  10-12 and "D2" pad 10-11 (1.41 µm, one) 4.1 and 56.2 kΩ ↔ 1.9 kΩ (6215); 6222 pad 7-9 (2.85 µm,
  half) 64.8 kΩ ↔ about 1 kΩ elsewhere on the tile; five structures in all.
  At 1280 px the pad label "10-11" wraps at its hyphen (a pad-pair label, not a value; at 400 px it
  does not wrap); `:widths:` did not change the rendered column split.
* **R-SENTENCE / R-PARA.** The 72-word estimate sentence split at "— and to a dose": "The target
  corresponds to a dose … (an illustrative estimate — … — not a SkyWater number)." (the hedge belongs
  to the dose; the resistivity half keeps `[^seto-1975][^kamins-1998]`). The 92-word extraction
  sentence split at ", and the 20-square resistors" with **"(our extraction from the published
  measurements)" and `[^raw-data-passives]` repeated** on the first half. "Why" paragraph 1 (158 w)
  → three paragraphs, the Seto/Mandurah sentence split at its semicolon. "Both are consequences …"
  split from the Chen/Tsang sentence at its semicolon.
* **R-CATEGORY.** Classification sentence split at ", and the most precision-critical" (14 w); the
  two remaining sentences describe this step → "**Specific to this step:**" and two bullets ("It is"
  added to the first; the second keeps "we infer").
* **R-HEDGE, R-TOOLS** (*SkyWater says:* "lists the 8250 with …" — the tool named instead of "it";
  the GSD sentence is the continuation paragraph), **R-OPENQ** (labels "Species, energy, dose and
  tilt", "What the `urpm` bodies receive", "Which implanter", "Process option").
* **R-RELATED.** Previous/Next split; "The companion resistor implant is PRI; the gate implant is
  P1I." → `Same module:`; the capped/cut/contacted bullet unlabelled (mixed modules).
* **R-GLANCE.** Why is the page's sentence "A dedicated implant lets the dose be tuned for this
  device on its own"; Public numbers the 2000 Ω/sq target only.
* **Left over the caps (known items).** The extraction-method sentence (67 w with the repeated
  hedge; one method, no seam). The table's lead-in (53 w): splitting at its colon would leave "The
  short structures scatter more than their 300 Ω/sq counterparts." without the extraction hedge that
  covers it.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-07`, `pdk-08`, `skw-01` (glance),
  `raw-data-passives` (the repeated hedge); numbers 2000 (glance), 8250 ×2 (glance tool name, and
  "lists the 8250"); hedges "inference", "not public" (glance), "our extraction" (the repeat).
  REGROUPED: every split and every table row, same digits in the same order (the "300" of the
  lead-in, the table rows and the closing sentence form one run in the base order). No LOST. (A first
  draft caption "… 2 kΩ/sq structures …" added a number the page does not write there; the caption
  was reworded to carry no number.) Declared `markers,numbers,hedges`: clean.
* **Marker coverage.** 13 flags, all read (list lead-ins by rule; split pieces whose base marker
  belonged to another clause; "Both are consequences …" is the page's own conclusion, unmarked in the
  base too).
* **Caps**: para > 100 3 → 0; item > 60 0 → 0; sentence > 45 8 → 2 (above).

### 057 UPRIS — done

* **R-H3.** Not applied: the passage after the figure is 71 words (an H3 needs ≥ 120).
* **Lead.** First sentence (29 w) split at ", and delivers" → "It delivers …" (R-GLANCE step 8).
* **R-CATEGORY.** Classification sentence alone; the "What is specific to it is that …" sentence is
  its own label (step 3), split at its colon (49 → 17 + 32 w).
* **R-PARA / R-SENTENCE.** "Why" paragraph 1 (206 w) → four paragraphs (the resist and what it would
  print; the nitride's adhesion; the chemical oxide and film stress; the conclusion "The clean here
  is therefore designed to leave that oxide … — an inference …", unchanged). Its 49-word sentence
  split at the colon before "a particle becomes a micro-mask …". Its 78-word sentence split into
  three: "A thin, uniform chemical oxide under the cap is harmless." / "A strongly tensile film is one
  of the film-stress problems Hu reviews,[^hu-1991] so the surface …" / the em-dash material as its
  own sentence after it (R-SENTENCE step 1, as in the guide's 066 example), "Its stress is of the
  order of 1 GPa for stoichiometric LPCVD nitride (typical industry value[^txt-02]; Temple-Boyer et
  al. …[^temple-boyer-1998])." — "Its stress is" added (subject + verb; "stress" is the page's own
  word: "film-stress", "lowest-stress"); the hedge and both markers stay with the value.
* **R-PARA step 4.** "Wet strip and clean" (87 w): lead + continuation paragraph.
* **R-HEDGE, R-TOOLS** (ashers and benches: grades verbatim; SP1/AIT: *SkyWater says:* the posting
  quotation with the page's verb "reads", our reading "We read "SP1" and "AIT" as …" as the
  continuation paragraph), **R-OPENQ** (labels "Pre-cap clean", "Queue time", "Which asher and
  bench").
* **R-RELATED.** "Companion strips: P1IS, PRIS; light-implant exemplar: LVTNIS." (two relationships)
  → `Same module:` companion strips and `Same category:` light-implant exemplar (LVTNIS is a strip
  step in another module). The BOX/SMAT pre-furnace-clean bullet keeps no label.
* **R-GLANCE.** Not public carries "the RCA sequence without HF is an inference", as Open questions
  says.
* **Preservation** (`--allow-regrouped` only): ADDED marker `skw-01`, hedges "inference" ×2, "not
  public", identifiers `P1ME`, `SC-2`, `SKY130` — all the glance box. No LOST. Declared
  `markers,hedges,identifiers`: clean.
* **Marker coverage.** 6 flags, all read: the three pieces of the 78-word sentence each keep the
  markers of their own clause ("A thin, uniform chemical oxide … is harmless." had none in the base
  either); "We read …" (base marker on the quotation); a label.
* **Caps**: para > 100 1 → 0; item > 60 1 → 0; sentence > 45 4 → 0.

### 058 GATENIT — done

* **R-H3.** `### What the public record shows` after the figure caption, over the `npc`/NPCM record,
  the "poly cap after SPE" reading and the e-test "with NGNIT" parameter (≈ 185 words).
* **R-LIST.** The three PDK facts about the later nitride cut ("The PDK's mask table lists …,[^pdk-05]
  the drawn layer `npc` … ,[^pdk-06] and the rules require …[^pdk-periph]") → three plain bullets,
  each with its own marker, under the page's own lead-in sentence (its full stop → colon; "and"
  dropped). The four ARC studies (Ogawa; Dijkstra and Juffermans; Czech; He) → sub-bullets inside the
  "Hard mask and anti-reflective layer" item, each with its marker (§4.1 "studies as sub-bullets";
  the lead-in "Silicon oxynitride and nitride films … were the standard inorganic anti-reflective
  layers of the KrF generation:" keeps its colon).
* **R-SENTENCE / R-PARA.** The 53-word inference sentence split at "; this reference accordingly
  places …"; paragraph split before the e-test sentence. "Resistor protection" item: the Tsang
  sentence split at ", which is what a cap …" → "This is what …" (the base marker stood before
  "which", so it never covered that clause). LPCVD item (124 w, one 67-word sentence with nested
  dashes): split into "The film is stoichiometric, dense and strongly tensile — of the order of 1 GPa
  … (typical industry value, …;[^txt-02])." / "Temple-Boyer et al. measured ≈600 MPa … the
  stress.[^temple-boyer-1998]" / "It deposits on both sides of the wafer — one reason a backside film
  removal (BFR) follows." ("and" dropped; hedge and markers stay with their values).
* **R-CATEGORY.** Classification sentence (25 w) alone; "Both are on SkyWater's public capability
  list — …" as the second paragraph (one sentence about this step); "What distinguishes this nitride
  from ISONIT and SPNIT is that …" is its own label (the step-3 form), third paragraph.
* **R-PARA step 4.** "Hard mask …" (169 w), "A cap that stays" (85 w), "Resistor protection" (92 w),
  "LPCVD nitride" (124 w), "PECVD nitride" (100 w): lead sentence + indented continuation paragraphs.
* **R-HEDGE, R-TOOLS** (Aviza: *SkyWater says:* states "Furnaces are all made by Aviza", with LPCVD
  nitride listed — "states" added for verb-first, as on 043; "C1": *SkyWater says:* the two listed
  entries, and the inventory's reading of "C1" as a Novellus Concept One, "which is an inference", as
  the continuation paragraph), **R-OPENQ** (labels "LPCVD or PECVD", "Function of the nitride", "The
  "poly cap after SPE" entry", "Later doping of the gate").
* **R-RELATED.** Previous/Next split. The "Backside film removed at BFR; patterned at …; cut …;
  possible polish stop …" bullet (mixed modules) and "Other nitrides: ISONIT, ONO, SPNIT, LINIT"
  (ONO is an oxidation step, so "Same category:" would not be true of every link) keep their own
  glosses and no label.
* **R-GLANCE.** Why is hedged as the lead hedges the whole purpose ("what follows is our inference
  from the PDK's public rules"); Public numbers gives the 0.2 µm "poly cap after SPE" with "(our
  reading)" of what it measures.
* **Left over the caps.** The PECVD "The film is hydrogen-rich, its stress can be tuned …" sentence
  (46 w; no split point that keeps its em-dash pair whole); the "Later doping of the gate" Open
  question (46 w, base text after the label).
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 0.2, quotes
  "poly cap after SPE" ×2 (glance; the Open-questions label), "C1" (glance), hedges "inference", "not
  public" ×2, "our reading", identifier `C1` — glance box and one label. REGROUPED: the `npc` list and
  the Temple-Boyer split, same digits in the same order. Declared
  `markers,numbers,quotes,hedges,identifiers`: clean.
* **Marker coverage.** 13 flags, all read (list items and study sub-bullets keep their own markers;
  the ARC lead-in is followed directly by its four cited studies; pieces whose base marker belonged
  to another clause; labels).
* **Caps**: para > 100 2 → 0; item > 60 5 → 0; sentence > 45 7 → 2 (above).

### 059 POC — done

* **R-H3.** Not applied: the passage after the figure is 78 words (an H3 needs ≥ 120).
* **Lead.** First sentence (39 w) split at ", completing the gate stack" → "It completes the gate stack
  …" (R-GLANCE step 8; `[^pdk-03]` stays on the 0.18 µm, "(thin, we infer)" stays on the film). Lead
  split into two paragraphs before "The oxide is not a device layer" (a new subject).
* **R-CATEGORY.** Classification sentence alone; "What is specific to it is that …" is its own label
  (step 3), split at its colon (46 → 15 + 31 w).
* **R-SENTENCE / R-PARA step 4.** "Protecting the resist from the nitride" (141 w, a 58-word first
  sentence): split at the colon; the em-dash pair (the Hinsberg measurement) becomes its own sentence
  after the claim (R-SENTENCE step 1): "The airborne bases are amines and amides such as the
  N-methylpyrrolidone whose uptake Hinsberg et al. measured at the 10 ppb level.[^hinsberg-1992]"
  ("The airborne bases are" added as subject + verb; the marker stays on the measurement, where the
  base had it). Lead + two continuation paragraphs. "Completing an anti-reflective stack" (67 w, a
  53-word sentence): split at the semicolon; the two studies keep their markers. "PECVD TEOS oxide"
  (68 w): lead + continuation.
* **R-HEDGE** (italic lead-in), **R-TOOLS** (two tools: head keeps its SkyWater gloss and quotations,
  the pilot form; grades verbatim under *Tool exists:*, including "the model behind "C1"/"C2" is an
  inference"), **R-OPENQ** (labels "Deposition method and thickness", "Function of the cap",
  "Survival to the finished device").
* **R-RELATED.** Previous/Next split; "Other deposited oxides: FILOX, SPOX, NCAPOX" → `Same category:`
  (all three are Deposition steps in `docs/steps/index.md`); the P1M/P1ME/NPCM bullet unlabelled.
* **R-GLANCE.** Does keeps "(thin, we infer)"; Why states the four roles as this reference's
  inference (Open questions: "Which of the four functions … is inferred"); Public numbers as on 058.
* **Preservation** (`--allow-regrouped` only): ADDED markers `pdk-03`, `skw-01`, number 0.2, quotes
  "C1", "C2", "poly cap after SPE", hedges "inference", "not public" ×2, "our reading", "we infer",
  identifiers `C1`, `C2` — all the glance box. No LOST. Declared
  `markers,numbers,quotes,hedges,identifiers`: clean.
* **Marker coverage.** 8 flags, all read (the uncited pieces were uncited in the base; labels).
* **Caps**: para > 100 0 → 0; item > 60 3 → 0; sentence > 45 3 → 0.

## Content problems for the owner (not fixed)

* `048-sagd.md`, lead: "The film is undoped as deposited" is stated as fact; the second paragraph
  (now under "What the public record shows") calls the same description an inference ("… the public
  basis for describing `SAGD` as one undoped amorphous layer (inference)"). Both kept verbatim (the S5
  figure agent's note in `progress-rd-figures-s5.md`).

* `051-p1is.md`, figure caption (generated from `data/figures/`): the sentence "In the upper panel
  the undoped film under the island is not labelled, because its leader would have to rise through
  the resist." appears twice in a row. Generated text; not touched here (§2.8).

* `052-rrpm.md` leaves open whether `RRPM` opens the `urpm` bodies (What this step is, Open
  questions); `055-urpm.md` uses the reading that it does not, and the figures follow 055 (the S5
  figure agent's note). Both pages already say so; both statements kept verbatim, and 052's glance
  box lists the question under "Not public".

## Guide problems

(none yet)
