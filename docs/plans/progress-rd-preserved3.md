# Progress: rd-preserved3 (tools/check_preserved.py, accumulated "For the tool branch" items)

Branch `topic/rd-preserved3`. Task: implement the accumulated tool-branch items named across
`docs/plans/progress-rd-steps-014-034.md`, `-035-047.md`, `-048-063.md`, `-064-075.md` (not yet
merged; read from `topic/rd-steps-064-075`), `-machines-a.md`, `-materials.md`, `-masks-a.md`,
`-categories.md`, `-overview.md`, and the reviews under `tmp/reviews/` (`rd-steps-035-047.md`
problems 15/16, `rd-steps-014-034.md` T-new-1, `rd-materials.md` D1, `rd-categories.md` hedge
list). This branch touches only `tools/check_preserved.py` and the two doc files named in the
task (`docs/plans/agent-briefs.md`, `docs/plans/readability-guide.md` §7) — no content page.

## Items and status

1. **G15 / T-new-1 (role/code-span mis-tokenisation).** Fixed. `ROLE_RE` now consumes a
   `{ref}`/`{term}`/`{doc}` role as one atomic unit, extracted and removed from the text BEFORE
   `_mask_inline_code` ever runs, so a role's own closing backtick can never be mistaken for a
   fresh opening delimiter by the code-span masker (the exact bug: a role followed later on the
   same line by an unrelated code span swallowed every word of hedged prose in between into a
   bogus masked span, losing both the ref target and the hedge). A trailing negative lookahead
   `(?!` + backtick + `)` on the role keeps the "role shown as a literal code example" case (rd-site
   review L5, the `` `{term}`sense`` `` selftest) working exactly as before. Verified the bug
   reproduces against `main`'s copy of the tool (three cases from the batch-2/3 progress files:
   `017-nwm.md:227`, `022-hvtpm.md:227`, `014-lvtnm.md:315`) and that the fix resolves all three,
   before adding them as permanent selftest cases. Role targets are now also whitespace-flattened
   before being recorded, so a role hard-wrapped across a line break compares the same after a
   re-wrap.

2. **Guide problem 16 (400-char quotation cap, silent resync).** Fixed. Quotations are matched
   per paragraph (split on a blank line first) instead of across the whole flattened page, so a
   pairing mismatch inside one paragraph can never desynchronise the rest of the page. Cap raised
   400 -> 800. An odd count of quote-mark characters in one paragraph (the shape of an unpaired,
   still-too-long quotation) is printed as a `WARN` line naming the page and the paragraph's first
   words, rather than silently resolved.

3. **Hedge list.** Added `roughly`, `of order`, `of the order of`, `light`, `typically`,
   `usually`, `likely` to `HEDGES` (rd-categories.md review D2 and the fix-round's "For the tool
   branch" note list every one of these except `light`, which the task itself names, from the
   same review's implant.md finding H: "light doses of order ...").

4. **`--allow-deduplicated` (rd-materials.md review D1).** Implemented per the review's patch: a
   LOST in `quotes`, `markers` or `numbers` is downgraded to a printed `DEDUPLICATED` warning only
   when (a) the item's count in the text before the first `## ` heading (the quick-facts table)
   decreased, (b) its count in the rest of the page is unchanged and >= 1, and (c) the page is
   `docs/machines/*.md` or `docs/materials/*.md`.

5. **`words` category.** New: a word-multiset diff (case-folded) of the "open text" — everything
   outside `{dropdown}` bodies, `{figure}` fences, `<!-- ...:begin -->`/`:end` generated blocks and
   footnote definitions. Always prints `WORDS LOST`/`WORDS ADDED` informationally (never fails on
   its own); `--strict-words` turns a LOST word not in a small stop-list of common function words
   into a failure. Motivated by rd-steps-064-075.md guide problem 4 (074's dropped "removing
   step:", caught only by an ad hoc `tmp/readability/worddiff.py`, invisible to every other
   category since it carries no number/quote/marker/hedge).

6. **Two new informational WARN checks**, run once against the current page text (not a diff):
   (a) every "At a glance" admonition bullet's numbers and footnote markers must recur somewhere
   in the body below it; (b) every "*SkyWater says:*" line/bullet must contain a quotation mark or
   a `skw-`/`cyp-` footnote marker. Both print `WARN` with page and line; neither fails the run.

## Verification notes (manual, per item, before landing)

* Item 1 (G15/T-new-1): reproduced against `main`'s copy of the tool on the exact three lines
  the batch progress files named (`017-nwm.md:227`, `022-hvtpm.md:227`, `014-lvtnm.md:315`);
  confirmed fixed.
* Item 2 (Guide problem 16): reproduced against `main`'s copy with a 479-character quotation
  (over the old 400 cap, under the new 800 cap) elsewhere on the page — `diff_page` reported
  **no failure at all** for a real wording change in a later, unrelated quotation (the exact
  desync/masking bug). Confirmed the fixed tool detects it (`LOST`/`ADDED quotes`).
* Item 3 (hedge list): reproduced the exact rd-categories.md finding H against `main`'s copy —
  "light doses of order 10^12-10^13 cm^-2" -> "10^12-10^13 cm^-2" reported **no failure at all**.
  Confirmed the fixed tool reports `LOST hedges: 'light'; 'of order'`.
* Item 4 (`--allow-deduplicated`, brand new flag): four selftest cases cover the default (fails),
  the flag on a materials page (warns, does not fail), the flag on a non-class page (still fails
  -- condition c), and a real body-level loss alongside the quick-facts deletion (still fails --
  condition b).
* Item 5 (`words` category, brand new): smoke-tested `extract_words`/`open_text_lines` directly
  against three real merged pages (`docs/steps/006-stie.md`, `docs/materials/wet-chemicals.md`,
  `docs/machines/pecvd.md`) — no crashes, sane word counts, dropdown/figure/generated-block/
  footnote-definition lines correctly excluded (327/450, 481/665, 586/798 lines kept). Ran the
  full CLI against a synthetic one-word addition on `006-stie.md`: printed `WORDS ADDED:
  'carefully'` and nothing else, as expected.
* Item 6 (glance/`*SkyWater says:*` WARN checks, brand new): ran directly against
  `docs/steps/006-stie.md` and `docs/steps/018-nwi.md` (both already merged and reviewed) — 0
  warnings, as expected. Ran against a hand-built bad page — correctly warned on the dropped
  glance number and the unsourced `*SkyWater says:*` line — and a hand-built good page (number
  recurs, SkyWater line quoted) — 0 warnings.

## Selftest

Every item above has a dedicated selftest case reproducing the bug (checked against `main`'s copy
of the tool by hand before landing the fix, per rd-common rule 2/TDD) and confirming the fix.
`uv run python tools/check_preserved.py --selftest` covers all of them plus the pre-existing
adversarial set (changed number, dropped marker, altered multi-line quotation, dropped hedge,
swapped numbers, text moved out of a dropdown), all still passing.

## Docs updated

* `docs/plans/agent-briefs.md`, "Checking a readability edit".
* `docs/plans/readability-guide.md` §7 (per-page procedure).
* This tool's own module docstring.

## Batch run against the last three merged batches

The three most recently merged batches (by the last commit date on each progress file: materials
00:12, machines-a 00:32, steps-048-063 02:57, masks-a 04:21, categories 05:10, all 2026-09-26) are
`rd-steps-048-063` (16 poly-module step pages), `rd-masks-a` (18 mask pages) and `rd-categories`
(10 category pages). Each batch's merge base is the parent, on `main`, of that batch's first
commit: `55c0e020` (steps-048-063), `6c1a9118` (masks-a), `f629785e` (categories) — confirmed by
`git diff --name-only <base> -- <dir>` matching each batch's page list exactly.

Ran `uv run python tools/check_preserved.py --base <base> --allow-regrouped --allow-deduplicated`
(no `--allow-added`, to see everything) over each batch's own pages. No page-specific
`--allow-added` was replicated, so every batch reports "undeclared differences" purely from
categories (glance boxes, R-TOOLS labels, generated blocks) the original branches already
declared and a reviewer already checked; that count is not a new finding. The new checks:

* **`--allow-deduplicated`**: 0 `DEDUPLICATED` lines on any of the 44 pages (expected — none of
  these three batches are `docs/machines/*.md`/`docs/materials/*.md`; already exercised on
  `docs/materials/wet-chemicals.md`-shaped selftest cases above).
* **Glance-box / `*SkyWater says:*` WARN**: 0 lines on all 44 pages (only step pages carry a
  glance box; the 16 steps-048-063 pages are clean on both checks).
* **`words` (the interesting one)**:
  * **steps-048-063**: large, expected `WORDS ADDED` on every page — the R-GLANCE "At a glance"
    box's own vocabulary ("admonition", "glance", "public", "not", "tool", "assignment", ...),
    since the merge base predates that box. `WORDS LOST: 'strength'` recurs on 12 of 16 pages:
    spot-checked (048-sagd.md) — the base's inline "Strength: **strong** for ..." became the
    R-TOOLS label `*Tool exists:* **strong** for ...`, the guide's own intended transformation,
    not a loss of content. A handful of pages lose a small number of connectives/pronouns
    (053's `'and'×3`, 061's `'must'×4`/`'extend'×2`/`'wide'`, 063's `'whose'`) from ordinary
    R-SENTENCE/R-PARA splitting — not inspected line by line, but consistent with routine
    rewording, not a dropped claim.
  * **rd-masks-a: a genuine, previously-invisible finding.** All 18 pages report `WORDS LOST`
    including `'gathers'`, `'renders'`, `'records'`, `'sources'`, `'constrain'`, `'mpw'`,
    `'process'`, `'public'`, `'lithography'`, `'sheet'`. Every one of the 18 pages' own scope
    sentence — "This page gathers what public sources say about the mask itself — its PDK entry
    and layers, the plates the process-steps sheet records for the MPW runs, what the public
    renders of those runs show, the lithography it needs and the rules that constrain it." — was
    **deleted outright, with no replacement**, confirmed by reading the diff on `dnm.md` and
    grepping the removed lines across the batch (18 matches, one per page, `git diff
    6c1a9118 -- docs/masks | grep '^-.*gathers'`). This is exactly the class of loss `words` was
    added to catch (rd-steps-064-075.md guide problem 4): no number, quotation, marker or hedge
    in that sentence, so all nine other categories, and the branch's own review, passed it
    silently. Reported here for the coordinator; not fixed on this branch (no content page is
    touched here, and rule 3 forbids it in any case).
  * **rd-categories**: `WORDS LOST` on all 10 pages, mostly consumable/chemistry nouns
    ("chemicals", "gases", "sources", "hardware", "tungsten", ...). Spot-checked (etch.md): a
    duplicate elaboration bullet ("**Ti:W and TiN**: fluorine (SF₆, CF₄) or chlorine
    chemistries...") was consolidated into linked, generic bullets
    (`` {ref}`Chlorine/bromine sources <material-etch-gases>` ``) that already exist verbatim
    two lines above in the surviving prose — a legitimate R-COMPARE-style dedup matching the
    review's own "Medium" finding about "hand-picked consumable/tool-class subsets", not a
    fresh loss.

**Conclusion**: the `words` category's single genuine catch on this run — the mask pages' deleted
scope sentence — is precisely the kind of silent, no-number/no-quote/no-marker loss the other
eight categories are structurally blind to, and is worth a fix-round item on `rd-masks-a` (or its
follow-on) even though it is outside this branch's own remit.
