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
* [x] Figures 014–034 pasted, in five groups (014–017, 018–021, 022–025, 026–029, 030–034).
* [x] QA of every figure (harness, desktop and 400 px, light and dark) and three built pages
  (015, 027, 034) at both widths.
* [x] Checkers and the `-W` build: every `check_*.py`, every generator `--check`
  (`gen_figures.py --check`: 148 files, 0 problems), `gen_figures.py --selftest` and
  `sphinx-build -W` pass. `check_preserved.py` over the 21 pages against `main`: only the
  blocks' own additions (168 inserted lines, none deleted).

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

| `wells-030-pwdem` | thick resist over the whole slice, highlight across its top; caption says the windows are over the 20 V devices inside a deep-N-well tub, outside this slice | — |
| `wells-031-pwdei1` | beam over the whole slice, every arrow landing on the resist top; nothing below changes | the step's own well is not drawn anywhere: this slice cannot hold it, and no public geometry of a 20 V device exists to draw one (the page says its cross-section drawings are not labelled in text form) |
| `wells-032-pwdei2` | as 031 | as 031 |
| `wells-033-pwdeis` | resist gone; both wells, bands faded | — |
| `wells-034-rtai` | the two panels identical by construction (`op: anneal`); caption and after-panel title say that no public number supports any drawn diffusion | — |

Late change to the series, all figures from 018 rebuilt and re-shot: the N-well's dot moved
from the middle of the well to below the P-well's bottom (`anchor_y: -88`), because at -60
the P-well's leader passed 6 u under it; the N-well and P-well notes in 018 and 027 were
shortened by a line to keep 018 under 800 u.

Tool change made while doing 018: when two labels sit above the drawing and the left
one's riser is within 110 u of the canvas edge (`min-hang-width`), it now hangs right, in
the gap before the second riser, instead of being squeezed into a one-word column. The
thick N-well and HVTPM resists are routed from above (`route: top`), because a
right-routed resist leader on the left of a beam crossed every ion arrow. No existing
figure changed.

## Noticed, not fixed

* No factual or arithmetic problem was found in the 21 pages.
* On 015 the figure sits between the first paragraph and the collapsed patent note that
  paragraph points to ("in the collapsed note below"); the note is still below it.
* Every overlay's leader that crosses its own overlay gets a halo, which shows as a short
  white edge on a thin band (020–025). A tool detail; not changed here.
* Left for the reviewer: the neutral `implant` colour and `dim_layers` are new site-wide
  conventions (the conventions page explains both); an owner may prefer n/p colours with
  the page's reading tagged instead.

## Review round (independent review "approve with fixes"; coordinator rulings)

Every High and Medium is fixed, and every Low; the rulings on the three owner decisions are
applied. Nothing on the pages changed except the generated figure blocks (and 015's block
moving below its dropdown); `check_preserved.py` against `main` shows only the blocks' own
additions, plus the one regenerated caption line of `iso-008-dni`.

**H1 — leaders that read as film boundaries.** Fixed in the generator, for both series:
* two SVG lint rules: a label leader may not run more than `max-leader-traverse` (40 u)
  horizontally through materials other than the one it names, nor more than `max-edge-run`
  (20 u) within `edge-clearance` (4 u) of a horizontal material edge; and a third: no
  leader may cut through an ion beam;
* routing: a right-column leader keeps its dot to the heights where it breaks neither rule;
  where there are none, the leader takes a new `over` route — up out of its layer at the
  column with least material above it (clear of walls, mask edges, ion arrows and the risers
  of labels above the drawing), across above the surface, then to its label. The LVTNI band
  on 015–016 is labelled this way (its leader leaves the band upwards through the pad oxide,
  instead of running through the trench), and it is faded from 017 on;
* a halo is drawn only where a leader crosses a material other than its own, never over the
  layer it names (the white notch on the PMOS band is gone);
* ions take `label_x`, so the beam's label can rise where it does not block these routes.
In the isolation series the liner, the deep N-well and (on 012) the fill oxide now take the
over route; nothing else there moved. On 018–020 and 023–024, where the beam is over the
N-well and every route for the fill oxide's label would cross it, the fill oxide is drawn but
not labelled (`hide_labels`) and the caption says so — faded, it would show the trench as
empty.
*Before:* `tmp/rv/shots/Z1-01.png`, `Z3-crop.png` (reviewer's). *After:*
`tmp/shots/fix-015-lvtni-d-01.png`, `tmp/shots/s014-light-phone-01.png`,
`tmp/shots/s028-light-desktop-01.png`, `tmp/shots/iso2-light-desktop-04.png`.

**H2 / ruling (a) — faded layers and the implant colour.** A faded layer is now a hue-free
ghost: no fill, no pattern, a dashed `ink-muted` outline (`faded-fill-opacity: 0`,
`faded-dash`). The channel implant has no colour of its own: vertical ink hatching over the
silicon's colour (`fill: none`, pattern `vlines-ink`), so it cannot be read as resist and
does not hide the well under it. `palette` now composites every material, faded, over every
host (ground, substrate, N-well, P-well, deep N-well) and reports anything a faded layer
could be mistaken for; a selftest shows it catches a 35 % tint. The conventions page and the
legend regenerate. *Before:* `tmp/rv/shots/Z3-crop.png`, `H-light-desktop-08.png`. *After:*
`tmp/shots/s028-light-desktop-02.png`, `tmp/shots/s028-dark-phone-01.png`.

**Ruling (b) — one panel for no drawn change.** Spec option `no_drawn_change: true`: one
panel, titled "State at this step (no drawn change)", no arrow (its text is in the caption).
Lint: such a figure must really equal the step before, and two identical panels are an error.
Applied to 019, 023, 024, 028, 031, 032 and 034; the conventions page explains it.

**Ruling (c) — placement.** A dropdown right after the lead belongs to the lead; the figure
goes after it. `--check` refuses a block followed directly by a dropdown. 015's block moved;
the rule is in `figure-authoring.md` §7 (with "never the last element of a page", Low 8).

**Mediums.** M1: 034's arrow text is gone (one panel; the caption keeps "ambient … not
public"); the "PMOS channel implants" labels are `inferred`; 014/015/022 captions and the
series comment state the device reading ("an NMOS beside a high-Vt PMOS"); 015 says its
window side is illustrative and 014's after-title says "(illustrative)"; 027's well meeting
is hedged as the PWBM page's inference and dropped from its title; 018 carries the page's
"infers" for continuity under the field; 030's resist note is "it opens only inside
deep-N-well tubs", `public`, and 031/032 declare the slice. M3: every faded layer's series
title must appear in the caption. M4: series ops are type-checked (numbers, `route`,
`note_order`, unknown top-level fields), named anchors must fall 3 u inside their layer, and
`route`, `tilt_deg`, `label_x`, `min-hang-width` and the routing tokens are documented.
M5: beams are named by step ("NWI implant"), bands by device ("NMOS channel implant").
M6: by ruling (a).

**Lows.** 1 hedges trimmed from notes that carry the tag; 2 "thick" hedged in the arrow notes
(017, 021, 026, 029, 030), 031's species inferred; 3 lint: a figure with an ion beam must
mention the tilt (iso-008's caption gained the clause; the DNI page lists the tilt as not
public), conventions row reworded; 4 018 and 027 give the other well's depth, with
[^pdk-03]; 5 the trench clause is in both well captions; 6 thick resists now 52 u against
38 u; 7 lint lines are printed once; 8 by ruling (c); 9 the duplicate heading is gone;
10 014's title now "the wafer left by NS19".

Figure QA after the round: every wells figure rebuilt and shot in three harness groups, light
and dark, desktop and 400 px (`tmp/shots/s{014,021,028}-*`), the isolation series again
(`tmp/shots/iso2-*`, `iso3-*`), and built pages 015, 019, 030 and the conventions page
(`tmp/shots/fix-*`). Accepted: on `iso-012-cmpnit` the over-runs of the liner and fill-oxide
labels run 11–18 u above the polished surface, above the accent trace (the only routes that
pass the new rules there); on `iso-008-dni` the deep N-well's riser rises between two ion
arrows, 10 u from each.

Noticed, not fixed: 034's first paragraph says RTAI heats the wafer "in an inert ambient"
(L23) while its open questions say the "anneal temperature, time and ambient are not
public" (L282); for the page owner.
