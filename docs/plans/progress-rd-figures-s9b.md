# Progress — rd-figures-s9b (W1c, S9 second and third groups: steps 141–149 and 154–163)

Branch `topic/rd-figures-s9b`. Task: one figure per step for NILD5, CMPM3, NCAPOX5, VIM3,
VIM3E, TIN5, WDEP5, WCMP5, WTIAL4 (141–149) and MM4, MM4E, NILD6, CMPM4, NCAPOX6, VIM4, VIM4E,
WTIAL5, MM5, MM5E (154–163), continuing `data/figures/series-beol.yaml`.

## Status

Done: 19 specs, built, lint clean, pasted (insert only), all checkers, `-W` build, QA at both
widths in both themes, four built pages shot. Nothing left but review.

## Decisions

* **141–149 kept as S10 instantiated them.** NILD5 polished at 256, cap to 264; via 3 of 20 u
  on the metal-3 wiring line (x 52–72, etched through the capacitor dielectric) and on the
  first top plate (x 196–216); metal 4 5 + 32 + 5 u, top at 306 u. The metal-4 heights did not
  move, so 150–153 did not change: rebuilt, "4 files generated, 0 written" for each, and their
  captions (which mention no via-3 feature) still hold; `crop_depth` unchanged.
* **Series ops for 154–163** (`use:` of the templates, no new template and no generator change):
  * MM4/MM4E: metal-4 line x 20–84 (over the via-3 plug on the metal-3 line) and the second
    capacitor's bottom plate from x 104 (the MM4 resist covers the whole second plate, as MM3
    covers the first; it also carries the via-3 plug on the first top plate — the "M4 (plate 2)"
    of the PDK's stacked cross-section, the 149/154 pages). `etch_materials: [mim-diel,
    barrier, aluminium]`, as MM3E.
  * NILD6: gap-fill 80 u, polished at 332, cap 8 u to 340: 34 u over metal 4 (0.505 µm against
    via 3's 0.39 µm and 26 u), 23 u over the second plate.
  * Via 4: 44 u holes at x 30–74 (metal-4 line) and 190–234 (second top plate), wider than
    deep; `etch_materials: [oxide-dep, mim-diel]`, as VIM3E. No liner, tungsten or polish.
  * Metal 5: `metal-stack` with al 53 u (5 + 53 + 5 = 63 u, 1.5× metal 4, as 1.26 : 0.845),
    deposited conformally into the open vias: lines them, closes them, leaves a dimple of about
    4 u; top 403 u. Notes: bottom "Ti or TiW — see the overview", cap "read here as TiW — see
    the overview" (the 161 page reads the cap as TiW on the S8P exclusion of "top metal
    layers"). MM5 resist 40 u (the 162 page: thicker than at the lower levels); shapes x 10–94
    and from x 160, a 66 u space (drawn about as deep as wide; the page's minimum space is
    about 0.8:1).
* **Cuts.** Full slices: 128 u for 141–149 ("inside the oxide under metal 2"), 180 u for
  154–163 ("inside the oxide under metal 3"). Close-ups: 146–148 on the via-3 plug on the plate,
  `[176, 240]`, 4.2×, −946 (226 u, inside the metal-3 aluminium under the capacitor); 155 at the
  S10 window `[76, 176]`, 2.68×, −670 (250 u).
* **Why the plate via for 146–148.** The pages stress the second floor; the plate, the
  dielectric and the metal cap under the plug show what is new at via 3. The line via is said
  in each caption ("outside this view … in the same way").
* **145 and 160 are full slices with two callouts** (via on a metal line, via on the top plate),
  so that both floors are in one figure; both captions say that on this drawing the etch also
  clears the dielectric left on the line, and that the page is silent on it. 155's caption says
  the same for the space between the metal-4 shapes.
* **Labels.** "Metal cap film" for the metal cap at every level carrying a capacitor
  (per-figure override, S10's rule); "Capacitor dielectric" with an empty note where the page
  does not read the film as an oxynitride (146–148, 155); "Underlayer" for the metal-5 bottom
  film (the 161 page's word). No label carries a number except the two via callouts (via3.1,
  via4.1, cite `pdk-periph`). No patent key anywhere.

## Figures (all: lint clean; harness at 1280 and 400 px, light and dark, every tile looked at)

* **141 NILD5** — gap-fill over the metal-3 line and the capacitor; "NILD5" k 4.1, no "_C"
  film; routes not chosen; gap 2.8:1 on the page, drawn about 1.9:1.
* **142 CMPM3** — polished flat; oxide over the plate drawn thinner; 0.2–0.3 µm over a plate is
  the page's estimate (with the cap), of 0.39 µm.
* **143 NCAPOX5** — cap oxide; 0.39 µm finished; 0.05–0.15 µm industry-typical cap; no "_C".
  NILD5 not labelled in the lower panel (a crowded stack of thin labels otherwise; declared).
* **144 VIM3** — two windows (line, plate); via3.1/via3.4; plate enclosure not published;
  pdk-07 draws vias on "CAPM" and "M3 (plate 1)", here the metal-3 via is on a wiring line.
* **145 VIM3E** — two floors; dielectric cleared on the line (said); drawn 1.3:1 against
  about 1.95:1.
* **146 TIN5 / 147 WDEP5 / 148 WCMP5** — the plate via, 4.2×; liner 3 u (`thin_ok`, far
  thicker in proportion, said); the hole over the plate drawn a little less deep than wide.
* **149 WTIAL4** — metal-4 stack; repeat of metal 3 (inference); bottom Ti or TiW, cap
  unresolved (overview); drawn as thick as metal 3 (both 0.845 µm).
* **154 MM4** — resist over a line and over the whole second capacitor; no `cap2m` enclosure
  rule published; m4.1/m4.2/m4.3.
* **155 MM4E** — close-up as 140: breakthrough (fluorine-containing, on the page's account),
  then chlorine; dielectric cleared between the shapes, kept under the resist (said).
* **156 NILD6 / 157 CMPM4 / 158 NCAPOX6** — as 141–143 one level up; "NILD6" k 4.0; gap drawn
  about 2.2:1 against 2.8:1; 0.35–0.4 µm over a `cap2m` plate is the page's estimate.
* **159 VIM4** — two wide windows; via4.1 (the only size), via4.4; no `cap2m` via enclosure.
* **160 VIM4E** — two floors; dielectric cleared on the metal-4 line (said); drawn about 0.8
  deep-to-wide against 0.63; taper not public; no plug follows.
* **161 WTIAL5** — the stack into the open vias with a dimple; the fill technique not public,
  the drawn profile only illustrates the page's reading; metal 5 drawn 1.5× metal 4 as in the
  PDK; the stack drawn a little under twice the via depth against more than twice on the page.
* **162 MM5** — thick resist over two shapes; m5.1/m5.2/m5.3; resist drawn thicker, not to scale.
* **163 MM5E** — cap broken through, chlorine etch to the cap oxide; no capacitor dielectric on
  metal 5; the space drawn about as deep as wide.

## Compromises accepted

* Drawn proportions differ from the pages' (each stated in its caption where a ratio is
  given): via 3 1.3:1 (page ~1.95:1); via 4 ~0.8 (page 0.63); gaps 1.9:1 and 2.2:1 (page
  2.8:1); metal 5 ~1.85× the via-4 depth (page more than 2×).
* At full-slice scale the 3 u capacitor dielectric is a hairline, invisible at 400 px; 145 and
  160 rely on the caption for the cleared dielectric on the line (the close-up 155 shows it).
* In the close-ups the liner, the plate and the metal cap share the one barrier colour (the
  conventions); a stroke separates them, but in the dark theme they read as one pale block.
* A label override with `note: ""` still prints the basis tag ("inferred").
* The tungsten dip over the hole (147) is a V notch; the caption says it is not to scale.

## Checks

`gen_figures.py --check`: see the last line of this file's check entry below; every checker
(`check_steps`, `check_refs`, `check_machines`, `check_materials`, `check_masks`,
`check_papers`, `check_patents`, `check_filings`, `check_inforce`) 0 problems; `gen_papers`,
`gen_patents`, `gen_filings`, `gen_index_links` `--check` clean; `sphinx-build -W` passes;
`check_preserved --base main` on the 19 pages: ADDED only (152 lines added, 0 deleted). Built
pages 145, 155, 160, 161 shot at 1280 and 400 px: figure after the lead paragraph (no dropdown
follows any of the 19 leads), prose after the caption.

## For the owner / the readability batch (page points, not fixed here)

* **155 lead vs body** (as at 140): the lead says "a chlorine plasma removes everything … first
  whatever remains of the CAPILD2 dielectric outside the capacitor plates"; the body says
  chlorine "makes little progress" on it and a fluorine-containing breakthrough removes it.
  The figure follows the body.
* **Where the dielectric is left.** On the stop-on-dielectric reading of CAPME/CAP2ME, the
  dielectric stays on every metal-3 and metal-4 shape under the MM3/MM4 resist; the 145 and
  160 pages give the via floors as the metal cap and the plate, and the 155 lead says the etch
  removes the dielectric "outside the capacitor plates", without saying it stays on the lines.
  The 145, 155 and 160 captions say what the drawing does.
* **155, arithmetic (minor):** "consistent with 0.72–0.80 µm of Al–Cu at 3.4–3.8 µΩ·cm" —
  3.8 µΩ·cm at 47 mΩ/sq gives 0.81 µm (3.4 gives 0.72). Not changed.
