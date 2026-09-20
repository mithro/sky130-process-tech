# W0d — generator changes — progress

Branch `topic/rd-generators`. Task W0d of `docs/plans/readability-plan.md`:
generator changes from report-A (F13, F17), report-B (B2, B9, B11) and
report-C (C8, C9 rule 1, C11). Working through the five numbered steps
of the task brief as separate commits, running the full check suite and
looking at a rendered sample after each.

## Step 1 — `gen_steps.py` sync + `--check` (done)

`write_index()` was stale: it dropped the committed intro paragraph
(the "lightly edited for 20 steps" sentence) and the `[^steps-sheet]`
footnote definition, so a real run would have deleted the citation.
Verified by diffing a scratch run against the committed file before
touching anything.

* Added `INDEX_INTRO` / `INDEX_FOOTNOTES` constants holding that text
  verbatim and an `index_text()` function so the committed file and the
  generator agree byte for byte (`uv run tools/gen_steps.py --check`
  now passes with 0 problems).
* Added `--check`: fails if `docs/steps/index.md` differs from the
  generated text, or if a step page listed in `steps.csv` is missing.
  It never writes.
* Confirmed the safety property the brief asked to keep: `write_stub()`
  still returns `False`/no-ops for any step page that already exists
  (all 171 are written; a plain run reports "0 stub(s) created" and
  leaves `docs/steps/index.md` byte-identical — verified with
  `git status` before/after).
* Added `python tools/gen_steps.py --check` to `.readthedocs.yaml`
  `pre_build` (after the other `check_*` entries, before `gen_papers.py
  --check`) and to the checker lists in `docs/plans/agent-briefs.md`
  (writer brief and reviewer brief).

No checker needed a semantic change for this step — it only reads the
generator's own output.

## Remaining

2. Step index: group by module (13 overview modules), short category
   labels, `Machine class` / `Mask` columns, phone-width fallback,
   short toctree titles, `{term}` on Phase-cell FEOL/MOL/BEOL.
3. `gen_index_links.py`: heading + title-first link text; check_inforce
   interaction.
4. `gen_patents.py` / `gen_papers.py` / `gen_filings.py`: clickable
   URLs, index reorder, `{dropdown}` for methodology.
5. B9 step-link text script (11 files, 1,975 links).
