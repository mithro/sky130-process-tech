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
* **Caps**: para > 100 3 → 0; item > 60 6 → 2; sentence > 45 11 → 1. Left: the 5 V NMOS item (61 w; its
  only seam is before "That is the HVNTM tip"), the Exposure item's lead (62 w; its only seam is before
  "That is well within"); the 46-word `ntm` inference sentence (no seam that keeps "we infer" with its
  whole claim).
