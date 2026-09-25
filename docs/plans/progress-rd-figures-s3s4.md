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
* [ ] Figures pasted, in groups (035–038, 039–042, 043–047).
* [ ] QA of every figure (harness, desktop and 400 px, light and dark) and three built pages.
* [ ] Checkers, generator `--check`s, `check_preserved.py`, the `-W` build.

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

(filled in as the figures are pasted)

## For the readability batch (noticed in the pages, not fixed)

(filled in as found)
