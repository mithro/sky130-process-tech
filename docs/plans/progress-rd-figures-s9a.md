# Progress — rd-figures-s9a (W1c, S9 via and metal levels, first group: steps 118–134)

Branch `topic/rd-figures-s9a`. Task: the S9 series as one parameterised template
instantiated per level (report D §2), the template mechanism in `tools/gen_figures.py`, and
one figure per step for 118–134.

## Done

* **Generator** (`tools/gen_figures.py`):
  * series `base:` (the ops of another series first, unchanged), `templates:` and
    `ops: - use: … with: …` (expanded when the series is loaded: `expand_series`,
    `load_series`); lint for undeclared/unused/missing/extra parameters, unknown template or
    field, list inside text, a bad or looping base; for every series, a layer id used twice
    and ops out of step order. Selftest: expansion equals the hand-written ops with types
    kept, a base is prepended unchanged, and 14 fault cases.
  * a negative `crop_depth` is now allowed on a full slice too (the back end is tall): the
    zigzag cut and "The lower part of the slice is not drawn." on the figure, the exact cut
    phrase in the caption (lint; the old "only a close-up may cut off" rule is replaced, and
    its selftest case now checks the full-slice declaration).
  * `--check`: 484 files, 0 problems before any S9 figure (no existing figure changed).
* **Series** `data/figures/series-beol.yaml`: `base: series-metal1.yaml`; five templates
  (`via-hole`, `via-plug`, `metal-stack`, `metal-pattern`, `imd`); instantiated for via 1,
  metal 2, NILD4, via 2 and the metal-3 stack. Drawn heights and positions in its header.
* **Authoring guide**: "Series templates" section (how the next group continues), the
  `crop_depth` row, two lint rows.

## Figures (118–134)

(per-figure record below as they are built)

## Left

* Figures 118–134, placement, checkers, QA.

## Decisions

* Via widths drawn 16 u (via 1) and 20 u (via 2) against depths of 18 u and 28 u: the depths
  are set by S8's end state (via 1) and by keeping via 2 at 0.42/0.27 of via 1; a narrower hole
  would close under the 5 u minimum liner. Drawn aspect ratios about 1.1:1 and 1.4:1 against
  the pages' 1.8:1 and 2.1:1; the captions say so.
* Via walls vertical: the pages give the PDK's "Via1 slope" 0.02 and read it as a taper
  allowance; no wall angle is public, and S8's contact taper came from a public top/bottom CD
  pair that the via levels do not have.
* Metal 3 drawn 42 u against metal 2's 28 u (the PDK: 0.845 against 0.36 µm) to keep the
  stack inside the height budget; captions say it is thicker but not in proportion.
* Full-slice figures crop at 84 u above the silicon (inside NILD2 under metal 1), declared.
