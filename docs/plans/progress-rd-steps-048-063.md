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

## Content problems for the owner (not fixed)

* `048-sagd.md`, lead: "The film is undoped as deposited" is stated as fact; the second paragraph
  (now under "What the public record shows") calls the same description an inference ("… the public
  basis for describing `SAGD` as one undoped amorphous layer (inference)"). Both kept verbatim (the S5
  figure agent's note in `progress-rd-figures-s5.md`).

## Guide problems

(none yet)
