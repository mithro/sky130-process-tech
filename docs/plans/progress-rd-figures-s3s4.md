# Progress — `rd-figures-s3s4` (W1c, series S3 SONOS and S4 gate oxides)

Branch `topic/rd-figures-s3s4`. Task W1c of `docs/plans/readability-plan.md` for series S3
"SONOS tunnel window and ONO stack" (steps 035–042) and S4 "Gate oxides" (steps 043–047):
`data/figures/series-sonos.yaml`, `data/figures/series-gates.yaml`, one figure spec per step
(`data/figures/sonos-NNN-code.yaml`, `data/figures/gates-NNN-code.yaml`), the generated
`{figure}` block pasted into each page.

## Status

* [x] Read the 13 pages (035–047) in full: bodies, dropdowns, open questions, footnote keys.
* [x] Token change: a new material `arc` (see "Tool and token changes"); every existing
  figure regenerated (CSS only), the legend and the conventions page regenerated.
* [x] `series-sonos.yaml`, `series-gates.yaml`.
* [x] Figures pasted, in groups (035–038, 039–042, 043–047).
* [x] QA of every figure (harness, desktop and 400 px, light and dark) and three built pages
  (035, 039, 044).
* [x] Checkers: every `check_*.py`, every generator `--check` (`gen_figures.py --check`: 200
  files, 0 problems), `gen_figures.py --selftest`, `palette` (0 confusable pairs),
  `check_preserved.py` (block additions only) and `sphinx-build -W` pass.

## Tool and token changes

* **A new material, `arc`** ("Anti-reflective coating (ARC) under a resist", dark brown, no
  pattern). Step 036, `TUNARCE`, is "Tunnel mask ARC etch": the coating is its subject, and
  no existing material could stand for it (the isolation series left the BARC of `FOM` out).
  `gen_figures.py palette` reports no confusable pair; the dark value was darkened once
  because the first choice sat too close to the pad and fill oxides on a dark page. No code
  change.
* Every existing SVG changed only in its embedded CSS (the new `--m-arc` token and its
  class); the legend gains one row and so grows; the conventions page gains one table row.

## Decisions

* **Two series files, not one.** The memory cells cannot be drawn in the slice the wells
  series uses: "Tunm outside deep n-well is not allowed" (tunm.6a), and the wells slice is
  outside a deep N-well. So S3 is drawn on a slice of its own, inside a deep-N-well tub:
  an active area standing for any transistor outside the memory cells (left, 0–60), a filled
  trench, and the memory transistor's active area (right, 116–268; the window 148–256 and
  the ONO island 136–268 run towards the label column so that the leaders of the thin films
  and bands under them stay short). S4 is drawn on a logic slice with the isolation/wells x
  layout: a 5 V NMOS area (left) and a 1.8 V NMOS area (right), both in the P-well.
  The S4 slice holds no ONO island on purpose: whether the LVOM resist covers the islands
  during NCHI and GOXETCH is not public, and the only reason the pages give for thinking it
  does comes from a patent shown as in force; a slice with an island would have to draw the
  resist either over it or not. The captions of 043, 044 and 047 say the memory cells are
  not in the slice.
* **State carried over.** S3 starts from the state the wells module leaves every region in
  (pad oxide in place, inferred; filled trench standing proud; P-well; annealed). The deep
  N-well and the P-well are placed without their masks (no figure shows a state before
  034). S4 starts from what S3 leaves in the logic areas: the ONO and the oxide under it
  gone, bare silicon (ONOME and GOX100 pages: "the logic silicon cleared at ONOME").
* **Channel implants of the wells module are not drawn** in either slice (035 and 043 say
  so; 045 says NCHI is the only channel implant drawn in its slice).
* **ONO.** Three films named by material and position (tunnel oxide, nitride, top oxide),
  all at the minimum drawn thickness: no thickness is public for SKY130, and every published
  range on these pages is from a patent. The tunnel oxide grows only on the bare silicon of
  the window; the top oxide is drawn in the deposited-oxide colour only to tell it from the
  tunnel oxide (how it is formed is not public; caption of 040). Nothing about the nitride's
  composition beyond "the charge-trapping layer, deposited by LPCVD" (open text of 040).
* **PTSI and DEPI** are hatched "implant" bands (type not shown by colour), PTSI below the
  surface and DEPI at the surface, as the two pages describe them; neither depth is public.
  Both are 9 u thick so that a leader can run inside them without running along an edge.
* **Gate oxides**: thick 10 u, thin 5 u, not in any ratio; the numbers (110 Å, `toxe` 11.6 nm
  and 4.148 nm) appear only in labels and captions with the key the page gives them. The
  thick-oxide increment at LVGOX is not public and not drawn (caption of 047).
* **Tilt** drawn as 0 on every implant; each caption says why.

## Per-figure QA

Every figure: built lint-clean, rendered with `gen_figures.py harness`, shot with
`tools/shoot.py` at the 736 px column and at 400 px, light and dark, and the PNGs looked at;
`check_preserved.py --base 785e7e4b` (the branch point; `main` has since moved) shows only
the block's own additions (its markers, numbers, quotes and hedges, and the "560" of its
width), and `git diff` deletes no line. Built pages 035, 039 and 044 shot at 1280 px and
400 px: each block sits after the lead (039's after the patent dropdown that follows its
lead), and the caption reads in place.

| Figure | What was checked | Compromise |
|---|---|---|
| `sonos-035-tunm` | before panel matches the wells end state (pad oxide, proud fill, P-well) on the new slice; ARC under all the resist and across the window bottom; window over the memory active area only; highlight on the resist and window | the substrate never shows (P-well over deep N-well fill the crop), so its label is hidden; the fill oxide is labelled in the upper panel only (its over-route label would cross the resist) |
| `sonos-036-tunarce` | ARC gone from the window bottom only, kept under the resist; resist unchanged (its loss is not public); highlight on the window bottom | the highlight also traces the two resist walls of the window |
| `sonos-037-ptsi` | beam lands in the window only; the band lies below the silicon surface, under the window only; ion label and resist label are the two labels above the drawing | band thickness (9 u) chosen so its leader runs inside it without running along an edge |
| `sonos-038-depi` | second band at the surface, above the PTSI band, same window; the DEPI dot is staggered from the PTSI dot | — |
| `sonos-039-tunme` | pad oxide gone in the window only, bare silicon there; resist and ARC gone; both bands unchanged; highlight on the window | the strip and the etch are one figure, as the page treats the strip as part of the step |
| `sonos-040-ono` | tunnel oxide only in the window, flush with the pad oxide around it (both at the minimum thickness); nitride and top oxide continuous over actives and the proud fill; three films labelled, all at equal thickness | pad oxide and fill oxide labelled in the upper panel only (a pad-oxide leader inside a 5 u film under two more 5 u films cannot avoid running along an edge); the tunnel oxide's leader rises through the two films above it (over route) |
| `sonos-041-onom` | resist island over the window with a margin on the left, running on to the right-hand edge; highlight on the island | tunnel oxide, pad oxide and fill oxide not labelled (every route for the tunnel oxide would rise through the resist island); caption says so |
| `sonos-042-onome` | the stack and the oxide under it gone outside the island; the island keeps tunnel oxide, nitride and top oxide, with pad oxide under its left margin; resist gone; highlight on the bare silicon | pad oxide under the island margin not labelled (caption says so) |
| `gates-043-gox100` | bare logic silicon before; thick oxide on both actives only, not on the fill; label carries the PDK's 110 Å with `pdk-hv` and "not public" for the part grown here | — |
| `gates-044-lvom` | resist over the 5 V side, edge at mid-field; window over the 1.8 V active; highlight on the resist top | — |
| `gates-045-nchi` | beam on the window (landing on the thick oxide and the right half of the fill); band at the surface of the 1.8 V active only, under the oxide | fill oxide labelled in the upper panel only (its leader would cut the beam) |
| `gates-046-goxetch` | thick oxide gone from the 1.8 V active only, fill unchanged, resist gone, band unchanged; the thick oxide's leader in the after panel takes the over route above the fill | — |
| `gates-047-lvgox` | thin oxide on the 1.8 V active only; thick oxide unchanged (increment not drawn); both labels carry the model `toxe` with their keys; notes reworded so that "1.8 V" does not break across lines | — |

## For the readability batch (noticed in the pages, not fixed)

Open-text passages that seem to carry content from a patent shown as in force (the checker
passes them, because none is a listed number or phrase):

* `docs/steps/039-tunme.md:129–130` — "far too fast to control for a … film": the film
  thickness given there is the pad-oxide range that the same page keeps in its collapsed
  notes (a patent shown as in force).
* `docs/steps/042-onome.md:69` — "only tens of nanometres thick in the Cypress patent" is a
  paraphrase of the same range, outside the dropdown that holds it.
* `docs/steps/038-depi.md:159–160` — "of order 1 nm for a tunnel oxide of the thickness a
  Cypress patent that may still be in force gives it" derives a number from the patent's
  tunnel-oxide range in open text.
* `docs/steps/040-ono.md:73–76` — the tunnel oxide is called thinner than the 1.8 V gate oxide
  "on the published patent ranges"; a comparison drawn from those ranges.

Inside a page:

* `docs/steps/043-gox100.md:17` (and :228) state as fact that the logic silicon was
  "cleared at ONOME", while `042-onome.md:141` and :303 say whether the last oxide goes at
  ONOME or at the GOX100 pre-clean "is not stated publicly", and 043's own recipe step 1
  treats the pre-clean as where the last oxide must be gone. The figures follow 042's
  treatment of the pre-gate clean as part of ONOME and say so in the 042 caption.
* No arithmetic problem found in the 13 pages.
