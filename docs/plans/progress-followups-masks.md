# Progress: fixing `tmp/review-followups-masks.md` findings on `topic/followups-masks`

Checked by grep across the whole `docs/` tree on this branch, 2026-09-18.
The previous (interrupted) fixer's last commits — `a5b8657` (Levinson
chapter-level descriptions, steps 004–093 and the i-line stepper page),
`d587850` (Levinson, steps 102–168), `96d88e3` (Fujimura 1989, step 067
and the wet-bench page) and `be92b0d` (step 039 tunnel-oxide embodiments)
— turn out to have covered every item below, including several not
individually listed in the review (e.g. `docs/masks/hvntm.md:104`'s "CL"
wording). No open items remain.

| Finding | File(s) | Status | Commit |
|---|---|---|---|
| M1 — Levinson "non-critical-layer tool choice/assignment" (mask pages) | hvntm, ldntm, ntm, psdm, onom, tunm | fixed | a5b8657 / d587850 (pre-existing on branch) |
| M1 — Levinson "non-critical-layer tool choice/assignment" (step pages) | 007, 014, 017, 022, 035, 041, 044, 064, 071, 078, 081 | fixed | a5b8657 / d587850 |
| M2 — Fujimura 1989 "popping" leftovers | 016, 021, 025, 029, 033, 051, 054, 067, 070, 074, 084 | fixed | 96d88e3 |
| M3 — US 6,969,689 "one furnace window/sequence" | overview/index.md, masks/onom.md | fixed | be92b0d (overview/onom already read "one reaction chamber") |
| M4 — "CL" stated as fact, not marked a reading | steps/068-hvntm.md (x2), masks/hvntm.md | fixed | pre-existing on branch |
| L1 — AMD patent "multiple thresholds by LDC implants" wording | 015, 020, 022, 038, 045, masks/hvtpm.md; optional zero-tilt on 066, 073 | fixed | pre-existing on branch |
| L2 — Ambiguous `chvtpm.3` reading wording | steps/022-hvtpm.md, masks/hvtpm.md | fixed | pre-existing on branch |
| L3 — Stolmeijer 1986 mask-page annotation ("MeV implantation" specificity) | masks/dnm.md, masks/nwm.md | fixed | pre-existing on branch |
| L4 — Levinson content below chapter level ("overlay budgets" etc.) | 16 reading-list bullets + 20 body sentences + 036-tunarce, 090-cmpp, 137/139/152/154, 026-pwbm | fixed | a5b8657 / d587850 |
| L5 — Fujimura 1989 used beyond the abstract | steps/067-astis.md:30-31, machines/wet-bench.md:277-279 | fixed | 96d88e3 |
| L6 — US 6,969,689 tunnel figure without its embodiment | steps/039-tunme.md:60 | fixed | be92b0d |
| L7 — Quote capitalisation ("[t]he") | steps/018-nwi.md, steps/027-pwi.md | fixed | pre-existing on branch (before this round) |
| Leftovers §7 table (same items as above) | — | fixed | as above |

## Full-tree sweep (not just the files the review named)

Grepped `docs/` for the underlying leftover phrases, not only the listed
files, to catch anything the review missed:

* `non-critical-layer tool…` / `tool choice for non-critical…` — no hits
  outside `docs/plans/TASKLOG.md` (a log entry, not a page) and one
  unrelated "layer assignment" on `docs/steps/055-urpm.md:135` (about DRC
  tooling, not Levinson).
* `popping` co-cited with `[^fujimura-1989]` — no hits.
* `furnace window` / `one furnace sequence` — no hits (the one
  "furnace sequence" left, on `docs/steps/040-ono.md:22`, is the step
  page's own inferred physical description, not attributed to the
  patent).
* `overlay budgets` — no hits except `docs/machines/cd-sem-overlay-metrology.md:256`,
  which is unrelated to the Levinson citation.
* Stolmeijer "original"/"entirely" — no hits.
* `chvtpm.2` (wrong rule name, should be `chvtpm.2a`) — no hits.
* "computed layer" — all remaining occurrences (`docs/masks/ntm.md`,
  `docs/masks/onom.md`, `docs/masks/hvntm.md`, `docs/masks/index.md`,
  `docs/steps/068-hvntm.md`) are either attributed as a reading or are
  verbatim quotes of the renders site's own "precomputed layer" note
  (unrelated to the M4 "CL" finding).

## Conclusion

Every M1–M4 and L1–L7 finding, and every entry in the review's §7
leftovers table, was already fixed by the interrupted fixer's prior
commits on this branch. No further content changes were made in this
round; this file itself is the only new commit.

## Checks run after the sweep

See the final report for checker/build output.
