# Readability guide — the rule book for the readability phase

This is the one document an executor needs. It consolidates `docs/plans/readability/report-A.md`
(step pages), `report-B.md` (machine, material, mask and category pages and their indexes),
`report-C.md` (links, navigation, references, theme) and `report-D.md` (figures) with the decisions in
`docs/plans/readability-plan.md`. Where two reports gave different numbers for the same thing, this guide
picks one and says so in §1; the reports are history, this guide is the rule.

**Who reads what.**

* **Executor** (Sonnet-class): you are given this guide and a batch of pages. Work one page at a time.
  Apply only the rules your page type lists, in the order it lists them (§4), then run the per-page
  procedure (§7). If a rule does not clearly apply, leave the text alone. You are never asked to judge
  whether a fact is right.
* **Reviewer** (Opus): check the diff and the rendered tiles against §8.
* Rules marked **blocked** (§9) must not be started until the named workstream has landed.

**The one sentence that outranks everything else:** this phase changes presentation, never content. If you
cannot re-present a passage without changing what it claims, leave it exactly as it is and write a line in
your progress file.

## 1. Limits for the whole site

One table. It applies to every page type unless a page-type section in §4 narrows it.

| Element | Target | Hard cap | Measured how | Resolved from |
|---|---|---|---|---|
| Prose paragraph | 40–80 words | **100 words**; anything ≥ 120 must be split | words after deleting `[^…]` markers and `{role}` wrappers (`measure.py` counts this way) | A F1 (cap 100) vs B15 (cap 120/flag 150) vs C7 (cap 130) → **100** |
| List item (outside `## References`) | ≤ 40 words | **60 words** | same | A F1 and B15 agree |
| List item lead sentence, when the item has sub-bullets | ≤ 30 words | 30 | same | A F1 |
| Sentence | ≤ 30 words | **45 words** | words between full stops, markers removed | A F8 (30/45) vs B (35/45) → **30/45** |
| Em-dash pairs or parentheticals per sentence | 0–1 | 1 | count of ` — ` pairs and `(…)` | A F8 |
| Parenthetical length | ≤ 11 words | 11; ≥ 12 words becomes its own sentence | words inside `(…)` | A F8 |
| Step-page lead (text between `## What this step is` and the first `###`) | ≤ 2 paragraphs, ≤ 120 words | 120 | `measure.py` section stats | A F2 |
| First sentence of a step page | ≤ 25 words | 25 | — | A F11 |
| Class-page intro (machine, material, mask, category), before the quick-facts table | ≤ 70 words | 70 | — | B15 |
| Index-page purpose paragraph | ≤ 80 words | 80 | — | B3, C §2 |
| Glossary entry | ≤ 80 words | 80 | — | C9 |
| Table cell | ≤ 25 words | 25 | words in the cell, markers removed | B §2.3 |
| Quick-facts cell | ≤ 20 words, ≤ 1 quotation | 20 | same | B5 |
| Links in one table cell | ≤ 8 | 8; more becomes "N steps — see §…" | count of `{ref}` | B §2.3 |
| Table columns | ≤ 4 when any column holds prose (at most 2 prose columns); ≤ 6 when every cell is a number, a code or ≤ 3 words | — | header row | A F3 (≤ 5) vs B §2.1 → **B's rule**; it is measured against furo's ~740 px column |
| Table rows | ≤ 40 | 40; more → split by group under H3s | — | B §2.7 |
| Footnote markers per paragraph | ≤ 4 | **6**; at 5 or more, ask whether the paragraph is a table | count of `[^…]` | A F2/F3 (≤ 6) vs C7 (consider at > 4) → target 4, cap 6 |
| H3s per step page | 3–6 | — | — | A F2 |
| Admonitions per page | ≤ 2 | 2 | `:::{note}`, `:::{admonition}`, `:::{seealso}` | A §2 |
| Figure caption | what is shown · the page's hedges · the citation · "Not to scale" | — | — | D §3 |
| Figure alt text | 60–450 characters, no citations | 450 | — | D §3 |

Word counts ignore footnote markers and role wrappers, because that is what the measurement scripts do
(`docs/plans/readability/prototypes/measure/measure.py`, function `clean`). A number, a code span or a
quotation counts as one word.

## 2. Never

These are absolute. A reviewer who finds one of them rejects the whole page.

1. **Never change a fact, a number, a unit, a significant figure, a quotation, a hedge or a citation.**
   Not "1 800 Å" → "1800 Å", not "about 0.33 µm" → "0.33 µm", not "we infer" → "the PDK shows".
   Thousands spacing, "about", "~", "approximately" and quotation marks stay exactly as written.
2. **Never upgrade a hedge**, in either direction. "our reading" does not become "the PDK gives";
   "SkyWater states" does not become "we infer". When you move a sentence, its hedge moves with it,
   word for word. Never delete a hedge, even when the same hedge already appears two lines above.
3. **Never remove or move a footnote marker away from the claim it supports.** A marker travels with its
   clause. When a paragraph is split, each half keeps the markers of its own sentences.
4. **Never fill an empty cell from memory.** A value the page does not give is `—` (em dash), or the
   page's own words ("not public", "not stated", "no vendor description was retrieved").
5. **Never move text across a `{dropdown}` boundary**, in or out, and never paraphrase, summarise or
   quote the content of a collapsed in-force note outside it. Rules R-PARA, R-TABLE, R-LIST and
   R-SENTENCE apply *inside* a dropdown, to the text that is already there.
6. **Never mention an in-force patent's content, number or title in the open.** What
   `tools/check_inforce.py` enforces, from the code:
   * every family in `data/patents.yaml` whose `expired` is not `true` is *restricted*: its members'
     publication numbers **in any spelling** (`US8093128B2`, `US 8,093,128 B2`, `8093128`, `8,093,128`,
     `US 2009/0179253 A1`, `EP 2 104 648 B1`), its titles of five words or more, and the footnote labels
     and inventory keys whose definitions name one of those numbers;
   * plus, per family, a list of `PHRASES` — distinctive wording taken from the patent. A phrase is
     *content*, so it is refused everywhere outside a collapsed block, footnote definitions and the
     inventory entry included;
   * any of those outside a `{dropdown}` (colon fence or backtick fence) is an error. Matching runs on a
     whitespace-flattened page, so a number split over a line break is still caught;
   * exceptions: the dropdown's own **title line**, a footnote *definition* at the foot of the page, and
     the patent's own inventory entry — and each of those must carry the exact flag sentence
     "Shown as in force; estimated expiry YYYY-MM-DD (estimate from public records, not legal advice)."
     (or the "Status shown as unknown; estimated expiry no later than …" wording) with the dataset's date;
   * a `{dropdown}` whose body is blank is an error ("it renders as an empty collapsible"): never leave a
     note empty by moving its content out.
   Practical consequence: **"At a glance" boxes, tables, captions, figures and summaries must not repeat
   anything from a collapsed note** — not the number, not the title, not the numbers inside it.
7. **In-force dropdown titles stay as they are.** The owner's wording
   (`From a patent shown as in force (…; estimated expiry …) — open to read`) is not to be shortened by an
   executor. A F12 proposes a shorter form; it is an owner decision and is **blocked** (§9).
8. **Never hand-edit a generated block or a generated page.** These are generator output:
   * the block between `<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->`
     and `<!-- index-links:end -->` on 206 pages (steps, machines, materials, categories, masks, overview);
   * `docs/steps/index.md` in full (written by `tools/gen_steps.py`);
   * everything under `docs/references/papers/`, `docs/references/patents/` and
     `docs/references/filings/` (`gen_papers.py`, `gen_patents.py`, `gen_filings.py`);
   * once W1a lands: `docs/_static/figures/*.svg` and the MyST blocks in `data/figures/*.yaml` output.
   A change to any of these is a change to the generator plus one regeneration commit.
9. **Never rename, reorder, delete or add a mandatory heading.** Per page type, from the checkers:
   * **step page** (`tools/check_steps.py`, all 13 must appear, each alone on its line):
     `## What this step is`, `## Step category`, `## Why this step exists`,
     `## How it is typically performed`, `## Machines typically used`,
     `## Machines likely used at SkyWater`, `## Resources required`,
     `## Related steps and cross-references`, `## References`, `### Cross-check`,
     `### High-level understanding`, `### Deep dive`, `## Open questions`;
   * **machine page** (`check_machines.py`, H2s exactly these, in order): `What the machine class is and
     how it works`, `Representative 200 mm-era models`, `At SkyWater`, `Consumables and facilities`,
     `Process-integration notes for SKY130`, `Related pages`, `References`, `Open questions`; H3s under
     `At SkyWater` exactly `What SkyWater lists`, `Strength of the evidence`,
     `SKY130 steps assigned to this class`; under `References` exactly the three tiers;
   * **material page** (`check_materials.py`): `What the class is and what it does`,
     `Representative materials and grades`, `At SkyWater`, `Supply, handling, safety and facilities`,
     `Process-integration notes for SKY130`, `Related pages`, `References`, `Open questions`; H3s under
     `At SkyWater` exactly `What SkyWater's filings and pages list`, `Strength of the evidence`,
     `SKY130 steps that use this class`; under `References` the three tiers;
   * **mask page** (`check_masks.py`): `What the mask defines`, `Drawn layers and derivation`,
     `Plates and reticle sets`, `Lithography and pattern transfer`, `Steps that use this mask`,
     `Design rules and critical dimensions`, `Related pages`, `References`, `Open questions`; H3s under
     `Drawn layers and derivation` exactly `In the PDK`, `In the public renders`; under `References` the
     three tiers; under `Plates and reticle sets` only `The mask-type record`; **no other H2 may have any
     H3 at all** until W0e;
   * `## References` must occur **exactly once** on every page that carries a generated index-links block.
10. **Never use `{numref}`.** `numfig` is off; `{numref}` emits a warning and the `-W` build fails
    (verified in this project, §6).
11. **Never add an external link whose URL is not already written in one of that page's own footnote
    definitions**, character for character. An inline link is only a convenience copy of a keyed
    footnote; that is what keeps `tools/check_links.py` coverage and the inventory keys complete.
12. **Never delete a reading-list bullet, and never change how many `* ` bullets sit under
    `### Deep dive`.** `check_refs.py` counts them (minimum 8 on a step or per-mask page, 12 on a
    category, machine, material or overview page and the masks index). Splitting one bullet into two, or
    folding two into one, changes the count.
13. **Never delete a duplicate sentence before checking its footnote labels.** Every definition must
    still be referenced at least once on the page, or the `-W` build fails.
14. **Never fix arithmetic, a wrong unit or a doubtful fact.** Write it in your progress file with
    `file:line` and move on.
15. **Never touch another worktree, `main`, a checker, a generator or `docs/plans/readability/`.**
