# Report D — diagrams and the visual system (full text for `report-D.md`)

Sampled pages:
- **Overview.**
- **Categories:** implant, lithography, CMP, etch, deposition.
- **Steps:** 002, 003, 005, 006, 011, 012, 018, 040, 047, 062, 065, 077, 080, 098, 103, 108, 112, 119, 138, 166, 169, 171.
- **Machines:** high-current implanter, CMP polisher, PVD cluster tool, KrF stepper (headings and one opening section; the prose was not read in full).
- **Masks:** FOM, CAPM (headings and one section).

Rendered checks of the live site were limited to the top of step 006 at 1280 px and at 400 px. The overview was captured but I did not open its tiles, and no category, machine or mask page was viewed rendered; their findings rest on source reading. The prototype was checked in a furo test build at both widths and in both themes.

## 1. Findings catalogue

### F1. The site has no figures at all (P1)

- **Problem.** `grep -rl '{figure}\|{image}' docs` returns 0 of about 260 pages. Step pages run 2 200–4 400 words and describe geometry in prose.
- **How widespread.** 63 of 171 step pages say what an etch or polish "stops on" or "lands on". 127 pages use the word "cross-section". 98 pages cite `metal_stack.svg` and none shows a stack.
- **Before.** `docs/steps/006-stie.md:15-21`: "Using the patterned nitride/pad-oxide hard mask … (with the FOM resist still on top, or already removed — see below), a halogen plasma etches a few hundred nanometres … The trench walls are made slightly tapered and the corners are kept free of sharp features".
- **After.** `diagrams/out/sti-006-stie.svg`.
- **Rule.** Every step page gets one before/after cross-section directly after the first paragraph of "What this step is". No text is removed.
- **Scriptable.** Yes; the figures are generated (section 4), not hand-edited page by page.

### F2. A figure can say more than the page does (P1, the main risk)

Pages hedge ("our reading", "inferred", "not public"); a drawing has no hedges unless the style supplies them. Rules the generator's lint enforces:

- Every label carries `basis: public | reading | inferred | typical`. Anything other than `public` prints a tag line in the `inferred` colour.
- A label note containing a number must carry `cite:`, and that footnote key must already be defined on the target page. The lint opens the page to check.
- Every cross-section prints "Not to scale. Thin films are drawn thicker than they are."

Two further rules are authoring rules, not yet checked by the lint:

- A dimension that is not public is never drawn to scale; its label says "not public" first and the reading second.
- Nothing sourced from a patent that `check_inforce.py` treats as in force may appear in a figure, because a figure cannot sit inside the collapsed note. This needs a checker hook (section 8).

### F3. The flow is only a 13-row table (P1)

- **Problem.** `docs/overview/index.md:328-342` gives no sense of proportion: 5 steps of gate oxide look the same as 21 steps of wells.
- **After.** `diagrams/out/flow-modules.svg`: a strip to scale by step count, bracketed FEOL/MOL/BEOL, fanning out to one row per module.
- **Rule.** Place it directly above the table. It repeats only facts already in the table.

### F4. The finished stack is walked in bullets and a 24-row table (P1)

`docs/overview/index.md:808-834`. Every number cites `[^pdk-04]` or `[^pdk-03]`, so a to-scale stack chart (E1 below) adds no new claim.

### F5. Machine pages describe a chain of parts in prose (P2)

- **Problem.** All 30 machine pages open with "What the machine class is and how it works". Example, `machines/high-current-implanter.md:28-30`: "ion source, extraction, analysing magnet, acceleration, scanning, dosimetry and an end station".
- **Rule.** One block-chain schematic per class, showing only the blocks the cited text names, in its order. No pictorial tool drawings; they would assert geometry no source supports.

### F6. Mask pages describe derivation and pattern transfer in prose (P2)

- **Problem.** All 36 mask pages have "Drawn layers and derivation" and "Lithography and pattern transfer".
- **Rule.** Two figures per page:
  - A derivation chain: drawn layers → plate data → resist → the steps that use it.
  - The series cross-section in the state after develop.
- **Do not touch.** Where the derivation is the page's inference (`masks/fom.md:88-90`), those links carry the `inferred` tag.

### F7. Category pages explain physics with no sketch (P3)

One generic schematic per category, labelled `typical`:
- lithography: resolution and depth of focus;
- CMP: dishing and erosion;
- etch: anisotropy and over-etch;
- deposition: conformality;
- implant: tilt and shadowing (33 step pages mention tilt).

## 2. Diagram inventory, prioritised

**(a) Cross-sections: one evolving series per module (P1).**

- A series is one geometry plus an ordered list of operations tagged with step numbers.
- The figure for step N shows "state after N−1" above "state after N".
- 171 step figures come from 11 series files.

| Series | Steps | Columns drawn | Public support on the pages |
|---|---|---|---|
| S1 isolation | 001–013 | active / trench / active; deep N-well overlay at 007–009 | wiki-sti sequence; pdk-04 FOX; pdk-03 0.07 µm step |
| S2 wells and Vt | 014–034 | NMOS active / STI / PMOS active; resist block; implant arrows; well overlays | pdk-03 well peaks and depths |
| S3 SONOS | 035–042 | memory cell / logic; tunnel window; ONO blanket then islands | step-list order; ONO thicknesses NOT drawn (patents in force) |
| S4 gate oxides | 043–047 | 1.8 V / 5 V / SONOS | pdk-hv 110 Å; model `toxe` |
| S5 poly gate | 048–063 | gate line and resistor body with nitride and oxide caps | pdk-03/04 0.18 µm poly and cap |
| S6 tips, spacers, S/D | 064–088 | one transistor close-up: tip, halo (tilted arrows), nitride spacer, spacer oxide, S/D | pdk-03 tip, spacer, XJ; tilt 7°/40° |
| S7 MOL | 089–106 | PSG, polish, `licon` hole, Ti/TiN, silicide disc only in the hole, W plug, TiN `li`, LINT, NILD2 | pdk-04 heights; step 098 "only inside the contact holes" |
| S8 contact, metal 1 | 107–117 | `mcon` plug; Ti/AlCu/cap stack; etch; NILD3 | pdk-04; cyp-qtp reports |
| S9 via and metal (template) | 118–134, 141–149, 154–163 | one parameterised series instantiated per level | pdk-04 heights per level |
| S10 MiM capacitor | 135–140, 150–153 | plate on dielectric on metal; plate etch stopping in the dielectric | pdk-06/07; dielectric identity tagged unknown |
| S11 passivation, pad | 164–170 | TOPOX, scribe opening, TOPNIT, pad opening | pdk-04 0.09/0.54 µm; "glass cut" |

Lithography and strip pages are states of the same series (resist on, resist off), so they need no family of their own. Step 171 gets a prober block-chain instead.

**(b) Flow maps.**
- B1: the module map on the overview (built, P1).
- B2: the same strip as a "you are here" locator on category pages (P3).

**(c) Mask and lithography (P2).**
- C1: a generic coat → expose → develop → transfer → strip chain on the lithography category page.
- C2: a per-mask derivation chain.
- C3: the 36 masks placed along the B1 strip, on the masks index.

**(d) Tool block-chains (P2).** One per machine page (30). Classes share templates:
- implanters (3);
- furnaces (3);
- plasma etchers (3) and the asher;
- CVD/PVD (4);
- steppers (2) and the track;
- CMP and cleaner;
- wet tools (2);
- metrology (5);
- tester.

**(e) Charts.**
- E1 (P1): the back-end stack to scale, from the overview table; every number is pdk-04.
- E2 (P2): a front-end depth ladder: junction 0.1 µm, P-well peak 0.42 µm, N-well 1.1 µm, trench "about 0.33 µm, our reading".
- **Do not draw implant profile curves.** The PDK gives a peak and a depth, not a shape; a curve would invent data.
- E3 (P2): the two Cypress metal-1 film stacks side by side, in `overview-metal-cap`.

## 3. Style specification (mechanical)

Every value below is a token in `diagrams/tokens.json`. The lint rejects any colour that is not a token.

**Format and canvas.**
- SVG only, generated.
- The canvas is always 480 u wide; the height is free (portrait-first).
- Display with `:width: 560px`. At that width 1 u = 1.17 px, so 13 u text is 15 px beside furo's 16 px body text.
- On a phone furo gives about 360 px, so 1 u = 0.75 px and 13 u text is about 10 px.
- Never place panels side by side. Before sits above after, so x positions line up and no second phone layout is needed.
- Zones across the canvas: margin 12, drawing 268, gutter 24, label column 164, margin 12.

**Palette.** 19 materials, each with a light value, a dark value and a pattern (`none`, `hatch`, `hatch-back`, `xhatch`, `hlines`, `vlines`, `dots`, `plus`).

| Material | Colour | Pattern |
|---|---|---|
| Silicon | neutral grey | none |
| n-type regions | blues | none, except deep N-well (hlines) |
| p-type regions | pinks | plus |
| Thermal oxide | strong amber | none |
| Deposited oxide | pale yellow | none; PSG adds dots |
| Nitride | green | hatch |
| Polysilicon | orange | none |
| Resist | violet | dots |
| Silicide | teal | none |
| Ti/TiN/TiW | dark purple (light purple in dark mode) | none |
| Tungsten | slate | cross-hatch |
| Aluminium | silver | back-hatch |
| Polyimide | tan | hlines |

- The `plus` pattern on p-type is needed because pink on grey vanishes for protanopes; I measured ΔE 0.5 between p-well and substrate before adding it.
- `figgen.py palette` simulates deuteranopia and protanopia (Machado 2009). It lists any two materials with the same pattern and ΔE76 < 14. It currently reports none in either theme.
- Colour is never the only channel: every shape has a 1 u ink outline and every material is labelled directly.
- One accent blue marks what this step changed (the process arrow and the new surface) and nothing else.

**Typography.**
- Font: furo's system sans stack.
- Sizes: panel title 14 u/700; label title 14 u/600; label note 13 u/400 muted; mono 12.5 u for mask and layer codes; minimum 12.5 u.
- Widths are estimated with DejaVu Sans, the widest font in the stack, so real renderings are never wider than the lint assumed.
- Wrapping is balanced so no last line holds one orphaned word.

**Labels.**
1. No text inside the drawing, ever. The lint tests every text box against the drawing rectangle.
2. Material labels sit in the right-hand column, in layer order.
   - The leader runs horizontally from a 1.9 u dot inside the material to the gutter, then makes one diagonal in the gutter to its label.
   - Order is preserved, so leaders cannot cross.
   - Label heights are solved by least squares (pool-adjacent-violators). The dot then slides inside its layer to meet the label, so most leaders end up exactly horizontal.
3. A leader that must cross another material gets a 2.6 u halo in the ground colour, so it cannot be read as a boundary.
4. Open or top-most features (a trench, a hole, the polished surface) are labelled from above. The leader rises vertically through empty space to a header band above the drawing. There are at most two per panel; the left one hangs left of its riser and the right one hangs right.
5. A vertical leader may not run within 5 u of a near-vertical material edge, because it would read as a film. The lint caught exactly this in the prototype, and the anchor moved to the trench corner.
6. Clearances: 3 u between any two text boxes, 7 u between label blocks, text at least 12 u from the canvas edge.
7. A note is given once per figure. In the second panel, unchanged layers show their title only.

**Arrows and dimensions.**
- Process arrow: accent colour, 2 u, between panels, with the step code and one sentence.
- Dimension line: ink 0.9 u, closed 7 × 5 u heads, a dashed witness line to the reference surface.
- The dimension's leader attaches by a 12 u stub, so the riser is not collinear with the dimension line.
- Ion arrows (still to build): accent colour, drawn above the surface, tilt as cited.

**Not to scale.**
- Minimum drawn film thickness is 5 u.
- The substrate bleeds off the bottom and sides with no outline, because it continues.
- To-scale figures (E1, E2) say "To scale" and carry an axis instead.

**Legends.** None in cross-sections, because labels are direct. One site-wide "Figure conventions" page, generated from `tokens.json`, serves as the global legend.

**Caption and alt text.**
- The SVG contains no title sentence. The MyST caption carries it, so it is searchable and holds the footnotes.
- Caption: what is shown, the hedges, the citation, and "Not to scale".
- Alt text: 60–450 characters describing the geometry, with no citations. The same text goes into the SVG `<title>` and `<desc>`.
- Both live in the figure's YAML. `figgen.py build` writes the ready-to-paste block to `out/*.myst.txt`:

```
:::{figure} /_static/figures/sti-006-stie.svg
:alt: Two cross-sections of the wafer, one above the other. …
:width: 560px
:name: fig-sti-006-stie

The wafer before and after `STIE`. … about 0.33 µm is this page's reading of the PDK stack drawing.[^pdk-04] Not to scale.
:::
```

**Naming and layout.**
- Names: `<series>-<step>-<code>.svg` (for example `sti-006-stie.svg`), `flow-*.svg`, `tool-*.svg`, `mask-*.svg`, `chart-*.svg`.
- All SVGs sit flat in `docs/_static/figures/`.
- Specs go in `data/figures/*.yaml`.
- The generator becomes `tools/gen_figures.py` with a `--check` mode like the other generators. The prototype writes `/figures/<dir>/` into `out/*.myst.txt`; change that to `/_static/figures/` when it moves.

**Dark mode.** Tested in a furo build (`diagrams/sphinx-test/`, passes `-W`).
- Each figure is written three times:
  - `NAME.svg` uses CSS variables plus `@media (prefers-color-scheme: dark)` inside the SVG, so it follows the operating system with no help.
  - `NAME.light.svg` and `NAME.dark.svg` are the forced variants.
- Every file paints its own ground in furo's page colour (`#ffffff` or `#131416`).
- A 25-line `docs/_static/figure-theme.js` swaps in the forced variant when the reader uses furo's toggle. I confirmed this in the furo dark screenshots.
- Without JavaScript the worst case is a light card on a dark page, which is still fully readable.
- Rejected alternatives:
  - `currentColor` does not cross the `<img>` boundary.
  - Paired `only-light` / `only-dark` figures need two directives and duplicate the caption and footnotes.
  - Inline SVG needs a custom directive. Revisit it only if clickable labels are wanted.

## 4. Production method

**Cross-sections are generated, not drawn.** `figgen.py` holds a height-map process emulator. The wafer is sampled every 0.5 u, and each column is a stack of segments.
- Operations implemented:
  - `deposit`: conformal by dilation, `fill_to` a level, patterned flat-top for resist, or `only_on` for thermal growth on silicon.
  - `etch`: chosen materials, to a depth or stopping on the first other material, with taper angle and corner radius.
  - `strip`.
  - `planarise`: `to` a level or `stop_on` a material.
- By construction, an anisotropic etch of a conformal film should leave sidewall spacers. No spacer figure has been built to confirm this.
- Still to add: doped overlays clipped to silicon, ion arrows, a `react` operation for silicide, isotropic etch.
- Proof of the series idea: `sti-006-stie` and `sti-012-cmpnit` both come from one `series-sti.yaml` and share the trench exactly.

**Flow, chain and chart figures use the same tool**, as further `kind`s sharing the tokens, text metrics, label layout and lint.

**Mermaid and Graphviz are not worth the dependency.** This judgement is from knowledge of the tools; I did not install or test either one.
- `sphinxcontrib-mermaid` renders in the browser from a CDN script, or needs headless Chrome at build time. It ignores the palette, handles furo's dark toggle poorly, and lays out unpredictably at 360 px.
- `sphinx.ext.graphviz` needs the `dot` binary on Read the Docs and hard-codes fonts and colours into its SVG.
- Neither can be linted for overlap.
- Needed instead: a `chain` kind (vertical boxes and arrows with optional side branches) covering C1, C2 and all of (d), and a `stack` kind for E1–E3.

**Dependencies.**
- PyYAML should already be installed, because myst-parser depends on it; I did not verify this in the lock file.
- Pillow is used only to measure text. For the production tool, embed a DejaVu width table so `--check` can run in the Read the Docs `pre_build` list with no new dependency.

**How a weaker model authors a figure.** It never writes SVG.
1. Copy an existing figure YAML.
2. Set `page`, `series`, the two `state_after` values, the panel titles, the arrow text, the alt text and the caption, using only wording from the page.
3. Run `figgen.py build`.
4. Fix every `LINT:` line.
5. Render and look at the result (see the QA procedure).
6. Paste `out/NAME.myst.txt` after the first paragraph of "What this step is".

Series files are written once per module by a stronger model and fact-checked against their pages.

**QA procedure: automatic checks on every build.**
- Canvas width is 480 u.
- `<title>` and `<desc>` are present.
- Only token colours appear, and there are no literal `fill` or `stroke` attributes.
- Every text element has a type-scale class and meets the minimum size.
- All text sits inside the margins.
- No text overlaps other text.
- No text sits inside a drawing.
- No leader touches any text.
- No leader crosses another leader.
- No leader runs alongside a material edge.
- "Not to scale" is present.
- Every `basis` value is in the vocabulary.
- Every number has a `cite`, and every cite key exists on the target page.
- Alt text is the right length and a caption is present.
- Every film meets the minimum thickness.
- No panel has more than two header callouts.

The lint caught real defects during the prototype:
- text running past the right margin;
- a panel title overlapped by the arrow note;
- the phase bracket running through "88 steps";
- a riser hugging the nitride edge.

**QA procedure: visual check.**
- `figgen.py harness NAME…` writes four pages: light and dark, each at the 736 px column and at phone width.
- Shoot each with `tmp/tools/shoot.py file://…/qa/light-phone.html OUT --width 400` and read the PNGs.
- Checklist:
  - Every label is readable at phone width.
  - No leader looks like a layer.
  - The changed thing is the only accent-coloured thing.
  - The dark version keeps every boundary visible.

## 5. Prototype (all under `tmp/readability/diagrams/`)

| File | What |
|---|---|
| `tokens.json` | palette (light/dark/pattern), theme colours, phases, type scale, spacing, strokes |
| `preview.html` | generated from the tokens by `figgen.py preview`: swatches in both themes, type, spacing (generated; I did not open it in a browser) |
| `figgen.py` | emulator, label layout, `xsection` and `flowmap` renderers, lint, colour-blind check, harness |
| `figures/series-sti.yaml` | the isolation series, steps 002–013 |
| `figures/sti-006-stie.yaml`, `sti-012-cmpnit.yaml`, `flow-modules.yaml` | three figures |
| `out/` | `NAME.svg`, `.light.svg`, `.dark.svg`, `.myst.txt` |
| `qa/` | harness pages and screenshots (`shot-*`, `furo-*`, `zoom*`) |
| `sphinx-test/` | minimal furo + MyST site with captions and footnotes; builds with `-W`; holds `_static/figure-theme.js` |

Changes made after looking at the renders:
- Labels were stacked below their layers with long diagonal leaders. Fix: sliding anchors plus least-squares placement.
- Header callouts were eating the label column. Fix: a header band above the drawing.
- "0.33 / µm" split across two lines. Fix: a non-breaking space plus balanced wrapping.
- The accent highlight ran up the hard-mask wall. Fix: the resist edge moved half a sample.
- An empty band remained where the resist had been. Fix: per-panel drawing height.
- Notes repeated in both panels. Fix: title-only labels in later panels.
- A white card appeared on a forced-dark page. Fix: the theme script.

Known weaknesses:
- At phone width, label notes are about 10 px: legible but small, and I would not go smaller.
- The dark deposited-oxide olive is dull.
- The HDP fill is drawn flat-topped.
- The conformal liner leaves a small notch where it meets the pad oxide.

## 6. Design-system note for the coordinator

The owner wants the style held in a claude.ai design-system project, which needs the owner's login. The prototype is arranged so the sync is a copy:
- `tokens.json` is the only place the palette, type scale, spacing and stroke values live. The generator, the lint and the preview page all read it. The exception is a few stroke widths and one opacity inside `figgen.py`, which should move into the tokens.
- `preview.html` is a self-contained page generated from it and can be published as the design system's reference page.

When the project exists:
1. Import `tokens.json`.
2. Publish `preview.html`.
3. Treat any edit in the design system as an edit to `tokens.json`, followed by `figgen.py build` of every figure. No SVG is ever touched by hand.

## 7. Page-type guidance

| Page type | Figures | Count |
|---|---|---|
| Overview | B1 above the module table; E1 at the top of "A simplified cross-section"; E3 in the metal-cap section | 3 |
| Step | one before/after cross-section after the first paragraph of "What this step is"; optionally E2 on well and junction pages | 1–2 |
| Category | one generic mechanism schematic under "What this class of step does"; the B2 locator | 1–2 |
| Machine | one block-chain under "What the machine class is and how it works" | 1 |
| Mask | a derivation chain under "Drawn layers and derivation"; the series state after develop under "Lithography and pattern transfer" | 2 |
| Material, glossary, references | none, except the "Figure conventions" page | 0 |

- Use two panels per figure at most.
- Three panels are allowed only for deposit → pattern → etch summaries on category pages.
- A figure never replaces text or a table, never sits inside a dropdown, and is always followed by prose.

## 8. Risks and open questions

1. **Checker and config changes are needed; none were made.**
   - `conf.py` gains `"figure-theme.js"` in `html_js_files`.
   - A new `tools/gen_figures.py --check` joins the `.readthedocs.yaml` `pre_build` list.
   - `check_inforce.py` should scan `data/figures/*.yaml` for cite keys of in-force patents and fail on any.
   - `check_refs.py` should be unaffected: caption footnotes are ordinary references and built cleanly in the test site, but I did not run `check_refs.py` on a page carrying a figure.
2. **Owner decision: how much may a figure show that is "our reading"?** I drew the 0.33 µm trench reading with a tag. The stricter option shows only `public` facts and leaves readings to the text.
3. **Owner decision: series geometry is an editorial act.** Drawing the resist as left on during STIE picks one of two sequences the page describes; the caption says so. Each series file needs a fact-check pass like any text.
4. `{figure} /_static/figures/…` makes Sphinx copy the auto file into `_images/` as well. The duplication is harmless: about 10 kB per file, 30–45 kB for the three variants.
5. About 250 figure YAMLs in total (171 + 36 + 30 + about 15). Do S1, B1 and E1 first, show the owner, then continue series by series.
6. The PDK's own `metal_stack.svg` and `cross-section-cap_mim.svg` are Apache-2.0 and could be embedded as-is, but they break every rule above: own palette, tiny labels, no dark mode. I recommend redrawing E1 from the cited numbers and keeping the link.