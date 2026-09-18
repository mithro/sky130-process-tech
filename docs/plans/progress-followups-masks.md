# Progress: fixing the round-1 review findings on `topic/followups-masks`

Checked by grep across the whole `docs/` tree on this branch, 2026-09-18.
The previous (interrupted) fixer's commits — identified
here by subject rather than by hash — turn out to have covered every item below,
including several not individually listed in the review (e.g.
`docs/masks/hvntm.md:104`'s "CL" wording). No open items remain from
round 1.

| Finding | File(s) | Status | Commit |
|---|---|---|---|
| M1 — Levinson "non-critical-layer tool choice/assignment" (mask pages) | hvntm, ldntm, ntm, psdm, onom, tunm | fixed | "Levinson 2005: chapter-level descriptions on the i-line stepper page and steps 004 to 093…" / "…on steps 102 to 168" |
| M1 — Levinson "non-critical-layer tool choice/assignment" (step pages) | 007, 014, 017, 022, 035, 041, 044, 064, 071, 078, 081 | fixed | same two commits as above |
| M2 — Fujimura 1989 "popping" leftovers | 016, 021, 025, 029, 033, 051, 054, 067, 070, 074, 084 | fixed | "Fujimura 1989: limit step 067 and the wet bench page to the abstract" |
| M3 — US 6,969,689 "one furnace window/sequence" | overview/index.md, masks/onom.md | fixed | "US 6,969,689: one reaction chamber, not one furnace window, on the overview and ONOM mask page" |
| M4 — "CL" stated as fact, not marked a reading | steps/068-hvntm.md (x2), masks/hvntm.md | fixed | "HVNTM: mark CL as a computed layer as a reading on step 068; the flag legend is not the only other use" |
| L1 — AMD patent "multiple thresholds by LDC implants" wording | 015, 020, 022, 038, 045, masks/hvtpm.md; optional zero-tilt on 066, 073 | fixed | "AMD multi-threshold patent: describe its implant as a laterally doped channel implant on step pages and inventory" / "…thresholds set by gate length with one self-aligned LDC implant; zero tilt on steps 066 and 073" |
| L2 — Ambiguous `chvtpm.3` reading wording | steps/022-hvtpm.md, masks/hvtpm.md | fixed | "HVTPM: unambiguous wording of the chvtpm.3 and chvtpm.4 reading on step 022 and the mask page" |
| L3 — Stolmeijer 1986 mask-page annotation ("MeV implantation" specificity) | masks/dnm.md, masks/nwm.md | fixed | "Stolmeijer 1986: abstract-level annotations on the DNM and NWM mask pages; verbatim capital in the quote on steps 018 and 027" |
| L4 — Levinson content below chapter level ("overlay budgets" etc.) | 16 reading-list bullets + 20 body sentences + 036-tunarce, 090-cmpp, 137/139/152/154, 026-pwbm | fixed | the two "Levinson 2005: chapter-level descriptions…" commits above |
| L5 — Fujimura 1989 used beyond the abstract | steps/067-astis.md:30-31, machines/wet-bench.md:277-279 | fixed | "Fujimura 1989: limit step 067 and the wet bench page to the abstract" |
| L6 — US 6,969,689 tunnel figure without its embodiment | steps/039-tunme.md:60 | fixed | "Step 039: attribute the tunnel-oxide figures to their embodiments and quote US 2009/0179253 verbatim" |
| L7 — Quote capitalisation ("[t]he") | steps/018-nwi.md, steps/027-pwi.md | fixed | "Stolmeijer 1986: abstract-level annotations on the DNM and NWM mask pages; verbatim capital in the quote on steps 018 and 027" (made on this branch, not pre-existing) |
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
