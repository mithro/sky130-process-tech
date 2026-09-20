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
    needs Pillow. Kerning is deliberately ignored, which can only over-estimate a width,
    so a real rendering is never wider than the lint assumed. PyYAML is already in
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
