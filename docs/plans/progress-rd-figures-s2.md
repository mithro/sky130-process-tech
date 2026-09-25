# Progress — `rd-figures-s2` (W1c, series S2: wells and threshold implants)

Branch `topic/rd-figures-s2`. Task W1c of `docs/plans/readability-plan.md` for series S2,
steps 014–034: `data/figures/series-wells.yaml`, one figure spec per step
(`data/figures/wells-NNN-code.yaml`), the generated `{figure}` block pasted into each page.

## Status

* [x] Read the 21 pages (014–034): bodies, dropdowns, open questions and footnote keys in
  full; the reading lists only for their keys.
* [x] Tool: the smallest additions the series needs (see "Tool changes"). Committed first,
  with the regenerated existing figures (CSS only).
* [x] `series-wells.yaml`.
* [ ] Figures 014–034 pasted, in groups of three or four pages.
* [ ] QA of every figure (harness, desktop and 400 px, light and dark) and three built pages.
* [ ] Checkers and the `-W` build.

## Tool changes (and why)

The six-label budget cannot hold the wells module: by step 027 a panel has the substrate,
pad oxide, liner, fill oxide, resist, two wells and two channel-implant bands. The tool had
`hide_labels` (draw, do not label) but nothing that tells the reader an unlabelled shape is
deliberate context. Added, each as small as possible:

* **`dim_layers`** (panel): drawn at the token `faded-opacity`, not labelled, not counted.
  Two lint rules — the layer the panel's step made may not be faded; a figure that fades
  layers must say so in its caption — and selftests for both, plus an unknown-id error.
  One row on the generated conventions page.
* **A neutral `implant` material** (violet, vertical lines). Not asked for, but needed:
  the n- or p-type of every channel implant in this module is not public (LVTNI: two
  readings; LVTPI: depends on the gate-doping inference; PCHI: species not public; PNCHI:
  BF₂ only as an inference), so drawing them blue or pink would say more than the pages.
  `gen_figures.py palette` still reports no confusable pair.
* **`op: anneal`**: RTAI changes nothing the drawing can show, but a step needs an
  operation to have a state of its own (`state_after: "034"` is otherwise past the end of
  the series).
* **`z` on `dope`**: overlays were painted in creation order, so the P-well (step 027) would
  have covered the LVTNI band (step 015).
* **`anchor_x` / `anchor_y`** on `deposit` and `dope`: the fill oxide's right-hand end is a
  thin wedge, which pinned its leader 2.5 u above the pad oxide inside the resist; the thin
  channel bands' leaders ran 4 u under the pad oxide across the other active area; the
  P-well's leader continued the line of its own bottom edge into the N-well.
* **`note_order: newest`** (series): the noted-label budget kept the notes of the oldest
  layers (substrate, pad oxide) and dropped the resist's note on the PWDEI pages; opt-in so
  that the isolation figures do not change.
* **Layout fixes**, both general: a silicon layer's dot is kept off any doped overlay (the
  substrate's dot landed inside the N-well); when labels pushed above their anchors made
  two leaders cross, the gutter lanes are re-dealt (the default right-to-left order is only
  crossing-free while every label sits at or below its anchor).

Every existing figure was rebuilt: only the embedded CSS changed (the new token and the
`.faded` class); no coordinate of any isolation-series figure moved.

## Decisions

* **Geometry.** The isolation series' x layout is kept (active 0–80, filled trench 80–188,
  active 188–268), with steps 002–013 repeated in the wells series. The slice is outside a
  deep N-well region, as the isolation figures for 010–013 are, so DNM/DNI/DNIS are not in
  this series. Left active = NMOS area, right = PMOS area; every mask edge at x = 134, the
  middle of the field, where the NWM and PWBM pages put the well edge.
* **Which side each mask opens**, from the page text: LVTNM — not public; the window is
  drawn over the NMOS side only so both sides of an edge show (caption says so, as the
  isolation series did for DNM). HVTPM — over the PMOS, which is true on both readings the
  page gives. NWM — over the future N-well. PWBM — a block mask, resist over the N-well
  (the page's inference). PWDEM — the whole slice covered: its `pwde` windows lie inside a
  deep-N-well tub, and this slice is an ordinary NMOS/PMOS pair outside one.
* **Well depths.** Only the PDK's two vertical dimensions are used (N-well 1.1 µm, P-well
  0.75 µm, pdk-03, cited on the NWI and PWI pages); drawn 112 u and 76 u, in that ratio to
  each other and not to scale against anything else. No profile or peak is drawn (report D:
  a curve would invent data); the peaks are in the captions only.
* **Channel implants** are one thin band per active area, at the surface of the active
  silicon only (the pages have them enter "the active silicon"). A later channel implant
  into the same band (PCHI, PNCHI), the second member of each well pair (NWI2, PWI2), the
  drain-extended implants (outside this slice) and the anneal change no geometry; each of
  those captions says why.
* **Tilt** is drawn as 0 everywhere: no page gives the SKY130 tilt, only typical practice.
* **Figure placement**: after the first paragraph of "What this step is", as on the pilot
  pages 001–013 (on `main` and on the pilot branch, where the "At a glance" box sits above
  "What this step is" and the figure below that section's first paragraph). The guide's
  §4.1 skeleton lists the figure next to the box; R-FIGURE item 3, the authoring guide and
  the pilot all put it after the first paragraph, which is what was followed.
* Nothing in any figure comes from a patent: every cite key used is a PDK, textbook or
  Wikipedia key. The Cypress patents behind the anneal's placement and the screen-oxide
  thickness are shown as in force and are not used, in any form.

## Per-figure QA

Every figure: built lint-clean, rendered with `gen_figures.py harness`, shot with
`tools/shoot.py` at the 736 px column and at 400 px, light and dark, and every PNG looked
at; `check_preserved.py` on the page shows only the block's own additions (markers,
numbers, quotes, hedges of the caption) and `git diff` no deleted line.

| Figure | What was checked | Compromise |
|---|---|---|
| `wells-014-lvtnm` | the flat NS19 surface matches `iso-013-ns19`; resist edge at mid-trench; highlight on the resist top only; fill-oxide dot inside the fill, leader clear of the pad oxide | the window side is illustrative (the plate's polarity is not public); said in the caption |
| `wells-015-lvtni` | beam lands in the window only, on the pad oxide and on the proud fill oxide; the band sits in the active silicon only; ion label hangs right with room; band leader 7 u under the surface, not along the pad oxide | the block sits between the first paragraph and the collapsed patent note that paragraph points to ("in the collapsed note below"); the note is still below it |
| `wells-016-lvtnis` | resist gone in the after panel, band unchanged, no highlight (nothing new at the surface, as `iso-009-dnis`) | — |
| `wells-017-nwm` | thick resist on the NMOS side, labelled from above (see 018); the riser crosses the accent trace on the resist top, as in `iso-006-stie` | — |
| `wells-018-nwi` | beam on the window only; N-well from the silicon surface to a flat bottom, continuous under field and active; its dot mid-well, the substrate's dot below the well; resist labelled from above so its leader no longer cuts across the beam (it did when routed right) | "Thick photoresist" wraps to two lines between the two risers |
| `wells-019-nwi2` | second beam, well unchanged, no highlight; before panel has no arrows | — |
| `wells-020-lvtpi` | PMOS band in the right active silicon only, inside the N-well; LVTNI band faded; band dot staggered left of the pad-oxide dot | the band's leader crosses its own band with a halo, drawn as a short white edge on the band (tool behaviour for every overlay) |
| `wells-021-lvtpis` | resist gone, well and band unchanged | — |

| `wells-022-hvtpm` | window over the PMOS (true on both readings of the opening, caption says so); resist from above; highlight on the resist top | — |
| `wells-023-pchi` | beam on the PMOS window; band relabelled "PMOS channel implants" with the steps it now holds | the band does not grow or split: no depth is public for either implant (caption); caption reworded once after the echo lint caught eight words of the first paragraph |
| `wells-024-pnchi` | as 023; the band label names PNCHI in the after panel; BF₂ renders with its subscript | as 023 |
| `wells-025-pchis` | resist gone; band label keeps the three implants, title only in the after panel (an empty `note` override stops the series note coming back) | — |

| `wells-026-pwbm` | block resist over the N-well, NMOS side open; both channel bands faded from here on (their labels would break the six-label budget) | — |
| `wells-027-pwi` | beam on the open side only; P-well from the surface to a flat bottom shallower than the N-well, meeting it under the middle of the trench; P-well dot moved to the middle of its thin part under the trench (`anchor_y: -66`) after the first render put the leader 6 u above, and in line with, the well's own bottom edge | the P-well under the trench is only 20 u deep in the drawing; not to scale, said in the caption |
| `wells-028-pwi2` | second beam, well unchanged | — |
| `wells-029-pwis` | resist gone; both wells | — |

Tool change made while doing 018: when two labels sit above the drawing and the left
one's riser is within 110 u of the canvas edge (`min-hang-width`), it now hangs right, in
the gap before the second riser, instead of being squeezed into a one-word column. The
thick N-well and HVTPM resists are routed from above (`route: top`), because a
right-routed resist leader on the left of a beam crossed every ion arrow. No existing
figure changed.

## Noticed, not fixed

(filled in as the work goes)
