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

See the final section below (added after all six items land) for the run of the new checks
against `rd-steps-048-063`, `rd-materials`/`rd-categories`-era pages, and machines/masks batches
at their merge bases, and what the new checks would have flagged.
