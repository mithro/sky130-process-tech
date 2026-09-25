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

## Content problems for the owner (not fixed)

* `048-sagd.md`, lead: "The film is undoped as deposited" is stated as fact; the second paragraph
  (now under "What the public record shows") calls the same description an inference ("… the public
  basis for describing `SAGD` as one undoped amorphous layer (inference)"). Both kept verbatim (the S5
  figure agent's note in `progress-rd-figures-s5.md`).

## Guide problems

(none yet)
