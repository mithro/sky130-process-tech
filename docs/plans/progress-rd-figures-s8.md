# Progress — rd-figures-s8 (W1c: emulator improvements, then series S8: contact and metal 1, steps 107–117)

Status: **part 1 (emulator) done and committed**; part 2 (S8 figures) in progress.

## Part 1 — emulator improvements before the metal levels

The three items of `progress-rd-figures-s7.md`, "For the generator before S8", and review
rd-figures-s7 M3 and its rulings on the terraced PSG and the corner-filling liner.

### What changed in `tools/gen_figures.py` (each with a selftest)

* **Conformal deposition grows normal to the surface.** A blanket `deposit` (no `only_on`,
  no `fill_to`, no flat-topped `where`) now takes the upper envelope of a disc of radius `t`
  rolled over the surface (`_dilate_round`) instead of a square window. A film has its own
  thickness on a sloped wall, every outer corner is rounded, and a hole's bottom stays open
  until the hole closes. Selftest: a 5 u film in a 10° tapered hole is 5 u at the bottom
  centre, its face is 5 u from the wall at mid-height (±1.5; a square element is 5 u off), and
  its top at 45° from the top corner is 40 + 5/√2 (a square element gives 45).
  Thermal growth (`only_on`) is unchanged: it was not part of the ruling and it is drawn at the
  minimum film anyway.
* **Gap-fill profile** `profile: gapfill` (new `deposit` field; `facet_deg`, default 45, and
  `smooth`, a flow length, go with it only; lint for unknown values). The film grows `t` up from
  every surface (bottom-up fill), adds nothing on a vertical wall, rises over a raised line in
  facets from its edges (flat over a wide line, peaked over a narrow one), and where the fill
  between lines rises above a low line the two merge (the opening of `tops + t` by a cone).
  Every point keeps at least 2 u. Selftest: narrow line peak `H + w/2`, wide line `H + t` with a
  facet 4 u from its edge, nothing on the wall beside a line, `t` on open ground; a flowed
  (`smooth`) film stays between 2 u and `t`.
* **Straight tapered walls at full-slice scale.** A film whose top falls steeply at the end of
  its run (a tapered etch cutting it to nothing) now ends on the wall's line instead of dropping
  vertically at the column boundary, and where a flat top meets the wall between two samples
  the corner is put back (`_corners`). Selftest: a 10° wall through four stacked films has every
  polygon vertex within 0.05 u of the wall line (0.32 u before; the test fails with the change
  switched off).
* `docs/plans/figure-authoring.md` documents `profile` and the straight walls.

### Series and caption changes

* `series-mol.yaml`: PSG (089) is `profile: gapfill` (the PSG page's HDP-CVD reading); header
  updated. NILD2 stays conformal (the 105 page leaves HDP or PECVD TEOS open).
* Captions and alt texts that described the old artefacts were rewritten, and their blocks
  re-pasted on the pages (`check_preserved`: 0 undeclared differences on the 7 pages):
  * 089: "broad terraces" → a gap-filling profile, "only illustrates such a deposit"; alt text.
  * 090 alt: "stepped top" → "faceted top".
  * 097: the liner no longer fills the bottom corners (caption and alt).
  * 099 alt: the tungsten blanket has a shallow dip over the hole.
  * 105: no longer "drawn with a flat top" (shallow dips over the gaps); 106 alt "nearly flat".
  * 077 (spacer etch-back): "flat top" → "rounded top … as a conformal film leaves it when its
    own thickness is etched straight down".

### What changed per series (all 440 files rebuilt; lint clean; `--check` 0 problems)

| Series | Figures changed | What the reader sees |
|---|---|---|
| S1 isolation (001–013) | none | Byte-identical: flat blanket films, `only_on` liner, `fill_to` oxide; the trench is a single silicon run |
| S2 wells (014–034) | none | Byte-identical (no conformal film over topography) |
| S3 SONOS (035–042) | all 8 | The ONO films and the resist over the field-oxide step have rounded outer corners |
| S4 gate oxides (043–047) | none | Byte-identical |
| S5 poly (048–063) | all 16 | Gate film, caps and re-oxidation over the field-oxide step: rounded shoulders instead of square ones; stacks otherwise unchanged |
| S6 tips/spacers/S-D (064–088) | 065, 066, 068–070, 075–088 | Spacer nitride deposited with rounded corners; after the etch-back the spacer has the classic rounded top (077's caption updated); spacer oxide rounded; some corners of etched films put back |
| S7 MOL (089–106) | all 18 | PSG faceted (bottom-up fill, peaks over the stacks) instead of terraces; contact walls exact; liner of even thickness with an open, rounded bottom; tungsten blanket with a dimple over each hole; NILD2 with shallow dips over the gaps instead of a flat top |

QA: 16 figures harnessed (iso-006, wells-018 as unchanged controls; sonos-040, poly-048, poly-062,
sd-076, sd-077, sd-080, sd-086, mol-089, 090, 094, 097, 098, 100, 105) and shot at desktop and
400 px in light and dark; every tile opened. Also looked at sd-078, sd-079, mol-099, 102, 104, 106,
sonos-042, poly-059 in light desktop. No label, leader or highlight regression seen; the lint
reported nothing.

## Part 2 — series S8

(in progress)
