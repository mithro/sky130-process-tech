# Progress — rd-figures-s10 (W1c, S10 MiM capacitors: steps 135–140 and 150–153)

Branch `topic/rd-figures-s10`. Task: one figure per step for the two MiM capacitor modules
(135–138, 150–153) and the metal-3 pattern that follows the first (139–140), continuing the S9a
series `data/figures/series-beol.yaml`.

## Decisions

* **Where the ops go.** In `series-beol.yaml` itself, as its header and the authoring guide
  planned ("the MiM capacitor steps go between them as plain ops"): plain ops for 135–138 and
  150–153, `use: metal-pattern` for 139–140. One back-end geometry; S9b continues after 153.
* **Two optional template parameters**, both defaulting to the old value (no earlier figure
  changes; `--check` clean before any S10 figure): `metal-pattern.etch_materials` (default
  `[barrier, aluminium]`) so that MM3E also removes the capacitor dielectric left on the metal
  outside the resist, and `via-hole.etch_materials` (default `[oxide-dep]`) so that a via onto a
  metal-3 line etches through that dielectric to the cap.
* **The slice holds a capacitor.** Metal 3 is patterned into a wiring line over the via-2 plug
  (x 14–76) and a capacitor bottom plate (x 100 on, past the edge); the top plate runs from
  x 130 (enclosure 30 u, illustrative; the `capm` enclosure value is not published).
* **Thicknesses.** Dielectric 3 u (`thin_ok`, close-ups only, 2.7×), plate 8 u (thicker than the
  5 u metal cap: the pages read the plate as about 0.1 µm, several times the 300 Å TiW cap of the
  2013 stack, and the dielectric as 18–33 nm; all not public). Captions say they are not drawn
  to scale.
* **CAPME stops on the dielectric** (the 138 and 153 pages' reading); no loss into it is drawn.
