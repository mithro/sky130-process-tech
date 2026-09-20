# Progress — `rd-figures` (W1a + W1b)

Branch `topic/rd-figures`. Tasks W1a (productionise the figure prototype) and W1b (the
first figures: the isolation series for steps 001–013, the module flow map and the
back-end stack chart on the overview) of `docs/plans/readability-plan.md`.

## W1a — done

* **`tools/gen_figures.py`.** The prototype `figgen.py` productionised.
  * Subcommands `build`, `--check`, `palette`, `preview`, `harness`, `--selftest`.
  * Specs in `data/figures/*.yaml` (series files and figure files), paste blocks in
    `data/figures/myst/`, SVGs flat in `docs/_static/figures/` as `NAME.svg` (follows the
    operating system), `NAME.light.svg` and `NAME.dark.svg`.
  * `data/figures/tokens.json` is the only place colours, the type scale, spacing and
    stroke values live. The stray stroke widths and the one opacity that were inside the
    prototype (`.hl` 2.4, halo `.85`, the preview page's pattern strokes) moved into it,
    and the new operations and kinds added their own.
  * **No new runtime dependency.** The DejaVu Sans, Sans Bold and Sans Mono advance
    widths are embedded in the tool as a table in 1/1000 em, so text measurement no longer
    needs Pillow. Kerning is deliberately ignored and each advance is rounded up, and
    `text_w` adds a further 0.05 u per character, so the estimate is an over-estimate and a
    real rendering is never wider than the lint assumed; a character the table does not
    carry is measured at the font's true widest advance and named by the lint. PyYAML is
    already in
    `uv.lock` (a dependency of `myst-parser`) and therefore in the Read the Docs
    requirements export, so nothing was added to `pyproject.toml`.
  * Deterministic output: fixed one- and two-decimal float formatting with no `-0.0`,
    stable ordering everywhere a set is iterated, so `--check` is reliable.
  * `--check` fails if a committed SVG, a committed paste block, the generated
    `docs/figure-conventions.md` or a `{figure}` block already pasted into a page differs
    from what the specs generate, if a spec's `id` does not match its file name, if an SVG
    in `docs/_static/figures/` has no spec, or on any lint line.
* **Emulator operations report D listed as missing**, all now in:
  * `dope` — a doped region clipped to the silicon, following the local silicon surface
    (`follow: surface`) or flat (`follow: flat`), so the deep N-well steps down under the
    trench exactly as the `DNI` page describes;
  * `ions` — implant arrows above the surface with a tilt, their tips landing on whatever
    the top surface is, so arrows in a trench start lower than arrows on a mesa;
  * `react` — a film reacting with what it stands on (silicide), with `under:` for "only
    where the metal lies directly on silicon";
  * isotropic `etch` (`iso:`) — a circular etch front, `depth` vertically and
    `depth × iso` laterally, which reaches under a mask edge and leaves it overhanging.
    The column model allows a gap under a segment, so the undercut is real geometry, not
    a cosmetic rounding.
* **New kinds**: `stack` (a to-scale layer chart with an axis) and `chain` (vertical boxes
  and arrows with an optional side branch per node). Both are exercised by `--selftest`;
  `stack` is also in use on the overview.
* **Lint.** All eighteen prototype rules kept, plus:
  * a cite key used in a figure spec must exist on the target page (it did before) **and**
    every cite key in the caption too;
  * a value whose `basis` is not `public` must say "not public" first and must not be
    drawn to scale (the two authoring rules report D says were not yet linted);
  * nothing may cite a patent family that `tools/check_inforce.py` does not treat as
    certainly expired. The restricted footnote labels come from that checker's own
    `load_families` / `restricted_families` / `map_keys_and_labels`, imported, not copied;
  * alt text carries no citations; a cross-section's caption ends "Not to scale."; a
    to-scale chart's caption says "To scale"; at most two panels; at most two header
    callouts per panel; a cross-section has a panel title; ids are unique.
  * `--selftest` drives **every** one of these from a deliberately failing spec or SVG,
    and checks that a clean spec lints clean and that each kind renders and passes the SVG
    lint.
* **`docs/_static/figure-theme.js`** and one two-line hunk in `docs/conf.py`
  (`html_js_files = ["figure-theme.js"]` plus its comment), kept as small as possible
  because another branch also appends to `html_js_files`/`html_css_files`.
* **`docs/figure-conventions.md`** — a short reader-facing page generated from the tokens:
  what a cross-section shows, "not to scale", the palette legend (itself a generated
  figure, `legend-palette.svg`), the basis tags, where the numbers come from, light and
  dark, and how labels and leaders work. It sits at the top level of `docs/`, so no
  page-type checker applies to it, and hangs off the landing page's "Cross-cutting
  references" toctree. `-W` build and `check_refs.py` are happy with it.
* `gen_figures.py --check` added to `.readthedocs.yaml` `pre_build` and to both check
  lists in `docs/plans/agent-briefs.md`.
* `docs/plans/figure-authoring.md` — the procedure for a Sonnet-class model.

### Changes to the prototype's own behaviour

* Panel titles wrap (three of the first thirteen figures had a title running off the
  canvas; the lint caught them).
* `crop_depth` per panel trims how much bare substrate is drawn, without changing the
  geometry; `hide_layers` leaves an optional layer out of a panel whose page does not
  discuss it.
* Label placement is repeated until the order of the anchors is stable. An anchor that
  slides inside its layer could end up out of order with its neighbour, and the two
  leaders then crossed in the gutter; the lint caught that on `iso-011-filox`.
* The dark deposited-oxide colour, which report D recorded as dull, went from `#5f5626`
  to `#9a8c52`. `gen_figures.py palette` still reports no confusable pair sharing a
  pattern, in either theme (`oxide-dep` against `poly` is the tightest, ΔE 17.3 under
  protanopia).

## W1b — done

`data/figures/series-isolation.yaml` is one geometry for steps 001–013: pad oxide, nitride
hard mask, `FOM` resist, the nitride etch, the trench etch and strip, the deep N-well
mask, implant and strip, the liner, the fill, the polish and the nitride strip. Thirteen
figure specs take states of it. Two overview figures complete the set.

Every label in the series is wording taken from the step page that introduces the layer,
and none of them states a number, so that the per-figure dimension and callout labels can
carry the footnote key their own page defines.

### Editorial choices, recorded

* **Where the mask edges fall** in the `FOM` and `DNM` panels is illustrative; both
  captions say so. The `DNM` window is drawn over four fifths of the slice so that one
  figure can show both sides of the mask edge.
* **The deep N-well is drawn only on the `DNM`, `DNI` and `DNIS` figures.** Steps 010–013
  hide it and crop the drawing to the top of the wafer: it is an option, those pages do
  not describe it, and a label there would not be supported by the page. This is recorded
  in the series file.
* **`STIE`**: the resist is drawn as left on for the trench etch and stripped at the end
  of the step — one of the two sequences the page describes. The caption says so, as the
  prototype's did.
* **Step 001 gets one panel**, not two: there is no "before" the starting wafer.

### Per-figure QA

Every figure was built, linted clean, rendered through `gen_figures.py harness` and shot
with `tools/shoot.py` at the 736 px column and at 400 px, in light and in dark, and every
PNG was looked at. Step 006 and the overview were also shot as built pages at both widths,
and step 006 in a forced-dark build, which confirmed that `figure-theme.js` swaps in the
`.dark.svg` and that the figure's ground matches furo's.

| Figure | Page | What was checked | Compromise |
|---|---|---|---|
| `iso-001-smat` | 001 | one panel, one label; substrate bleeds off three edges | a single grey block is a thin figure; kept because it sets the datum for the whole series |
| `iso-002-box` | 002 | pad oxide visible as a distinct film at 400 px; accent traces the new surface | the film is drawn far thicker than any range the page quotes; said in the caption |
| `iso-003-isonit` | 003 | nitride hatch legible in both themes at 400 px | — |
| `iso-004-fom` | 004 | two resist blocks, gap between them; title wraps to two lines | — |
| `iso-005-stinite` | 005 | "Bare silicon" riser lands on the silicon in the open field, clear of both walls | — |
| `iso-006-stie` | 006 | trench taper and corner radius visible; dimension line, witness line and "our reading" tag; also shot as a built page, light and dark, desktop and 400 px | — |
| `iso-007-dnm` | 007 | thick resist fills nothing on the open side; mask edge clearly visible | — |
| `iso-008-dni` | 008 | arrows follow the surface, so those in the trench start lower; buried band steps down under the trench; band is clearly below the trench floor | the band's depth relative to the trench is drawn, not to scale; the page's "a micrometre or more" and "roughly the trench depth" are in the caption |
| `iso-009-dnis` | 009 | `show_ions: false` on the before panel, so the arrows do not reappear | — |
| `iso-010-linox` | 010 | liner follows floor and both walls and is distinguishable from the pad oxide | the accent highlight was removed from this panel: a 2.4 u accent stroke over a 5 u film hid the film it was meant to point at |
| `iso-011-filox` | 011 | fill buries everything; leaders no longer cross | the emulator draws the HDP fill flat-topped, which a real fill is not over a patterned wafer; said in the caption |
| `iso-012-cmpnit` | 012 | polished surface flat, oxide level with the nitride | — |
| `iso-013-ns19` | 013 | nitride gone, pad oxide left, field oxide proud | the field-oxide step is drawn far larger than the PDK's 0.07 µm; said in the caption |
| `flow-modules` | overview | sits directly above the module table; all thirteen rows, ranges and mask lists match the table; 171 steps and 36 masks add up; legible at 400 px | — |
| `chart-beol-stack` | overview | to scale from the field-oxide top to the passivation nitride; thinnest layer (LINT, 0.075 µm) still visible and labelled at 400 px | the two MiM plates carry no labelled thickness and are not drawn; said in the footer |
| `legend-palette` | figure conventions | all nineteen materials, colour plus pattern plus name, both themes | — |

## Review round (independent Opus review, verdict "approve with fixes")

Every High and every Medium is fixed; the Low list is fixed except where a reason is
recorded below.

**H1 — the leader fan.** Fixed in the placer, not per figure. The gutter went from 24 u to
48 u and the label column from 164 u to 140 u; a leader now runs out of its dot, along a
vertical **lane of its own**, and into its label — three orthogonal segments, no diagonal.
Lanes are handed out right to left in label order, which makes a crossing impossible by
construction rather than unlikely: a lane further left always belongs to a label further
down, whose vertical span lies below. Two more passes keep the anchors apart — they are
pushed apart in y as far as each layer allows, and where a film is too thin for that the
dots are staggered 9 u sideways inside their own layer. Three budgets collapse the column
that caused the fan: at most three noted labels per panel (the layer the step made, first),
at most six labelled layers, at most 90 characters of note. Three lint rules stop it coming
back: no two leaders within 4 u side by side with overlapping extent, no two anchor dots
within 8 u by 10 u, and no figure taller than 800 u.
*Before:* `tmp/shots/q4-02.png`, `tmp/shots/q2-01.png` (the fan, four near-parallel strokes
in one gutter). *After:* `tmp/shots/h1-after-01.png`, `tmp/shots/h1b-02.png`,
`tmp/shots/f2-light-phone-02.png`, `tmp/shots/f2-dark-phone-04.png`.

**H2 — the in-force gate.** It now builds `check_inforce.Matcher` from that checker's own
`restricted_families` and runs it over **every** free-text string that reaches the SVG, the
caption or the alt: panel titles, the arrow title and note, every label title and note
(series, per-panel override, dimension, callout, ion), the chart's title, footer and axis
label, the flow map's headers, footer and module names. `arrow` also joined the label set,
so it gets the basis, number-needs-cite and cite-defined checks it never had.
`--check` additionally parses every committed SVG and runs the matcher over its text, which
no page checker reads. Demonstrated live: a restricted publication number in a panel title
is refused with the family id. `--selftest` drives it from a real restricted number and a
real restricted phrase taken from the dataset.

**H3 — `--check`.** A page named as a figure's target with **no** `{figure}` block, or with
the block's `:name:` changed, is now an error (both proven by deleting and by renaming);
a block mismatch prints a diff; the stale sweep covers every file under
`docs/_static/figures/` and `data/figures/myst/`, not only `*.svg`; a missing target page is
an error. The three cases are in `--selftest`.

**H4 — the ion beam.** Arrows are evenly spaced across the window, 36 u long and 1.8 u wide
(was 26 u and 1.4 u), with a **single shared tail height** so the beam reads as a beam while
each tip still lands on its own local surface. The label is routed into the header band
above the drawing from the middle of the widest window, not on to the last arrow, so it can
no longer merge with an arrow or run through the resist. A lint rule forbids an ion-beam
leader from crossing any material polygon.
*Before:* `tmp/shots/q3-02.png` (the leader through the resist, merged with the last arrow).
*After:* `tmp/shots/h1-after-01.png` (desktop), `tmp/shots/f2-dark-phone-04.png` (400 px,
dark), `tmp/shots/pg-steps-008-dni-p-01.png` (the built page at 400 px).

**H5 / H6.** `state_after` must be three digits and within the series (a wrong one used to
render a different wafer silently). Unknown operations, unknown operation fields, unknown
materials or groups and a `where_open` naming no layer are errors. A bad `y` expression and
a missing `y:` are lint lines. Nothing raises `SystemExit` any more, so one author's mistake
no longer abandons every other figure in the run.

**Mediums.** M1: the deep N-well is declared in all four captions that hide it, and 012's
"same cross-section" clause is gone; `crop_depth` moved from the panel to the figure, so the
two panels of a figure always crop alike (across figures it still varies, because the
deep-implant figures have to be deeper — recorded rather than forced). M2: the HDP
topography claim the page does not make is replaced by "The PDK gives no fill thickness or
topography". M3: the chart's caption now says it follows this page's reading of the
1.0111 µm label. M4: "as in the table below". M5: every step caption says what the picture
shows, and an eight-word echo of the paragraph above the figure is a lint error. M6: a label
above the drawing may wrap to at most two note lines, and when the header band would be
taller than the drawing the labels fall back to the right-hand column. M7: the 90-character
note budget plus the three-noted-labels cap removed most of the 10 px text. M8: the accent
is drawn 3 u clear of the surface, so it marks a 5 u film instead of covering it, and it is
now on every cross-section that has a new surface to trace (001, 008 and 009 have none —
nothing new reaches the surface there). M9: `psg` and `mim-diel` no longer share a hex with
another material, `palette` prints the three tightest pairs per theme, and a new lint rule
refuses two touching materials under ΔE 14 that share a pattern, or where either is drawn
thinner than 10 u. M10: an unknown glyph is measured at the font's true widest advance
(1735/2016 per mille, not the table maximum) and reported by name. M11: the theme script
only touches images that came from the generated directories, falls back to the shipped file
on error, and watches for added nodes; `conf.py` appends to `html_js_files` instead of
assigning it. M12: the label traverse is shorter (the anchor inset went from 8 u to 4 u) but
a label for a feature inside the trench still crosses the silicon with a halo — inherent to
labelling something in the middle of the drawing, and now the only such case. M13: the etch
windows and the implant extents are derived from the mask that defines them with
`where_open:`. M14: the conventions page now explains the accent, dimension lines, witness
lines, leaders and the halo, says two panels are the usual rather than the universal case,
and prints reader words for the patterns instead of token names. M15: the authoring guide
gained a budget table with the measured numbers, the `top@`/`si@` syntax, the real field
list and the corrected description of the header-callout rule.

**Lows.** Fixed: 1 (a layer keeps one route for the whole figure, decided by whether it is
top-most in *every* panel), 2 (the stack chart now follows a paragraph), 3 ("rounded base"),
4 (013's caption gives the pad oxide as the usual case, not a certainty), 5 (the shared
substrate note is now "the starting wafer (SMAT, step 001)"; only 001, whose page says it,
carries "p-type bulk substrate"), 6 (004 and 005 declare that the anti-reflective coating is
not drawn), 7 (006's caption leaves the strip's ownership open, as the page does), 8 (a
figure with no film says only "Not to scale."), 9 (the chart's footer discloses the merged
`NILD3_C`/`NILD4_C` films and the 1 µm axis step), 10 (the width table is generated with a
ceiling and `text_w` adds 0.05 u per character, so the estimate is now genuinely an
over-estimate), 11 (the text-overlap rule is driven from a real figure with the placer
monkeypatched), 12 (the selftest claim is no longer overstated: the callout rule is driven
through `build_xsection`, the overlap rule from a spec).

Recorded rather than changed:

* **Low 13** — furo centres a `figcaption` and a `figure`, so the legend's swatches start
  right of the body text. That is `custom.css`, which belongs to W0a (`rd-theme`); a second
  branch editing it would only make a conflict. The legend's internal heading is gone.
* **Low 14** — one emitted coordinate (`600.55`) sits exactly on the `f1` rounding boundary.
  It comes from exact arithmetic on token constants, not from libm, so no build can move it;
  determinism was re-confirmed after every change of this round.
* **Low 15** — in dark, `well-dn` (horizontal lines) against `well-n` (plain) and `ono`
  against `barrier` are close; so are `silicide` and `tungsten` in light. None of them touch
  in S1. The new adjacency rule will refuse them the first time they do, which is the wells
  module (S2) and the middle of line (S7).

## Noticed, not fixed (presentation only; not this branch's files)

* Furo centres a `figcaption`, so a multi-line figure caption is centred and its last line
  is short. `docs/_static/custom.css` belongs to W0a (`rd-theme`); caption styling is on
  that branch's list (C12/B §3.2), and a second branch editing the same file would only
  make a conflict.
* The module table on the overview and the summary tables on step pages overflow
  horizontally at 400 px. Pre-existing, and W0a/W3 work.

## Nothing factual was changed

The only edits to written pages are added `{figure}` blocks: `git diff` on the fourteen
pages is 120 insertions and no deletions. No sentence, number, hedge or citation was
moved, reworded or removed. `tools/check_preserved.py` (W0b) is not on this branch's base,
so the check was the diff.

No factual or arithmetic problem was found in the pages read for this work (steps 001–013
and the overview's flow and cross-section sections).

## Not done — for W1c and W1d

* Series S2–S11 and their per-step figures (steps 014–171).
* Machine block-chains (30), mask derivation chains (36), category mechanism sketches
  (10), the front-end depth ladder (E2) and the two Cypress metal-1 stacks (E3).
  The `chain` and `stack` kinds they need are built and self-tested, but no figure of
  either kind exists yet beyond `chart-beol-stack`.
* The "you are here" locator strip on category pages (B2) and the masks-index strip (C3).
* The design-system sync: `tokens.json` and `gen_figures.py preview` are laid out so the
  sync is a copy, but the claude.ai project does not exist yet (it needs the owner's
  login).
