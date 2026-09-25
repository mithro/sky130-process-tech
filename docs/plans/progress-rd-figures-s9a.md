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

* **118 VIM** (full slice, cut at 84 u): resist with windows over the middle and right-hand
  metal-1 lines. Checked light/dark, desktop/phone. The before panel labels only the two
  oxides (the label column was taller than the 56 u drawing); the metal-1 lines are labelled
  in the after panel. The cut metal-contact plugs show as short stubs under the outer lines
  (declared). Compromise: a flat, wide drawing; the windows are narrow slits at phone width.
* **119 VIME** (close-up [59, 150], 2.9×, middle via): the hole to the metal-1 cap. The window
  starts just right of the left metal-1 line (no sliver) and ends at the middle line's right
  end, so the line's films reach the edge and their labels run straight right (`routes`).
  The cap-film note is given by a panel override (the note budget had dropped it). Caption
  states drawn 1.1:1 against the page's 1.8:1, vertical walls, the "Via1 slope" not drawn.
* **120 TIN3**, **121 WDEP3**, **122 WCMP3** (same close-up): the 5 u minimum liner fills most
  of a 16 u hole; the captions say the liner is drawn far thicker in proportion than it is.
  122 labels the plug from above (`routes: {v1w: top}`; a right route ran 50 u inside NILD3).
  121's dip over the hole is small (alt: "a dip"). Two captions reworded after the
  caption-echo lint (119, 120). check_preserved: ADDED only on all five.

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
