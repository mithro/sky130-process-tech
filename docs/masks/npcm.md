(mask-npcm)=
# NPCM — Nitride Poly Cut

The nitride poly cut mask is the {term}`reticle` that decides where
SKY130's capped polysilicon can later be contacted: on the
{ref}`NPCM <step-078>` page's reading, the resist printed through it at
step 78 is opened wherever `npc` is drawn, over the poly heads that
local-interconnect contacts will land on and over the ends of the
precision resistors, and the {ref}`NPCME <step-079>` etch removes the
nitride and oxide cap there, stopping on the poly. It is a
{term}`nitride cut` layer of openings whose width rules are relaxed but
whose placement against the gates is not, and the step pages read it as
a KrF level for that reason, with i-line as the alternative. This page
gathers what public sources say about the mask itself — its PDK entry and
layers, the plates the process-steps sheet records for the MPW runs, what
the public renders of those runs show, the lithography it needs and the
rules that constrain it. How the step is performed is on the step page;
every mask is indexed on the {ref}`masks index <masks-index>`.

| | NPCM — Nitride Poly Cut |
|---|---|
| Mask step | {ref}`NPCM <step-078>`, step 78 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Nitride Poly Cut", `NPCM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cnpc` mask 49:0, "Nitride poly cut mask"; drawing 44:20, without a description[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `npc` drawing 95:20, "Nitride poly cut (under licon1 areas)"[^pdk-06] |
| Minimum CD, feature / space | `NPCMCD` 0.27 / `NPCMCDSP` 0.27[^pdk-03] |
| Polarity and tone | Not published. The step page reads the layer as isolated openings where `npc` is drawn, a dark-field layer; with a positive resist the plate would be clear over `npc` and opaque elsewhere (inference). |
| Exposure class | KrF (248 nm), an inference on the step page from the 0.090 µm placement rule to the gate rather than the 0.27 µm width, with i-line as the alternative; no public source names the tool ({ref}`machine-duv-krf-stepper`, {ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `180`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-npcm-steps>` |

## What the mask defines

The periphery rules give the function of the `npc` rule set as "Defines
nitride openings to contact poly and Li1", and the layer table describes
`npc` as "Nitride poly cut (under licon1 areas)".[^pdk-periph][^pdk-06]
The PDK's Table F4, "Connectivity of Drawn and Mask Layers", names the
layer that joins `li1` to poly as "Licon1 AND Npc", where diff and tap
need "Licon1" alone.[^pdk-summary] The contact rules make the pairing
explicit: "Npc must enclose poly_licon" (licon.18), by 0.100 µm in the
periphery (licon.15), while `npc` must keep 0.090 µm from a licon on
diffusion or tap (licon.13).[^pdk-periph] So the mask carries one opening
around every poly contact, and none over diffusion contacts.

The rules also put openings over the precision resistors: a
`prec_resistor` "must be enclosed by npc by atleast" 0.095 µm (rpm.5),
as it must be enclosed by `psdm` (rpm.4), and npc.5 sets a maximum
enclosure, 0.095 µm, of "poly overlapping slotted_licon by npcm"; the
slotted contacts are those of the resistors (our reading of licon.1b,
which sets their width "inside prec_resistor").[^pdk-periph] The
{ref}`NPCM <step-078>` page reads the resistor openings as letting the
P⁺ source/drain implant dope the resistor heads, an inference from the
rule text that no public source states. The PDK's mask generation table,
Table F2b, has an `NPC` column and marks it `C` ("CREATED") in one of its
80 device rows, the "p+ poly resistor"; it marks `-`, "Layer not created
for the device", in 45 rows, including every transistor row and the n+
poly resistor, and `+`, "Layer allowed to overlap", in 34.[^pdk-06] On our
reading of the table the openings over poly contacts are drawn by the
designer, and only the precision resistors receive created ones, which
fits rpm.5; the table does not explain its marks.

The {ref}`NPCM <step-078>` and {ref}`NPCME <step-079>` pages set the
cut beside the titanium-nitride local interconnect of Tang et al., a TiN
layer formed during self-aligned silicidation and patterned to join gates
and junctions;[^tang-1985][^tang-1987] the abstracts do not describe a
nitride cap over poly, and the papers' full text was not checked. The
step page also cites Cacciato et al.'s charging damage, when a contact etch met a conductive
borderless nitride, as a reason to open the nitride before the contact
etch.[^cacciato-2003] What the mask does not define is the cap it cuts,
laid down at {ref}`GATENIT <step-058>` and {ref}`POC <step-059>` and,
on the `SPE` page's reading, partly consumed at {ref}`SPE <step-077>`;
the contact holes, which {ref}`mask-licm1` prints much later; or the
doping of the opened poly, which on the step pages' readings comes from
the source/drain implants through the {ref}`PSDM <mask-psdm>` and
{ref}`NSDM <step-085>` resists.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cnpc` a `mask` purpose at 49:0 ("Nitride poly cut
mask") and a `drawing` purpose at 44:20, without a description and on a
layer number that also carries `cviam2` 44:0 and the `pwelliso` label
44:5; there is no `mask add`, `mask drop` or `waffle drop`
purpose.[^pdk-06] The drawn layer is `npc` at 95:20. The pairing rests on
those names and descriptions, as on the {ref}`masks index <masks-index>`,
and the PDK publishes no operation from `npc` to the plate beyond the
created resistor shapes that Table F2b implies. Rule x.15a confines
"Drawn compatible, mask, and waffle-drop layers" to test modules, seal
ring and frame, with an exception that names only "FOM/P1M/Metal waffle
drop" (flag P),[^pdk-periph] so a design inside the die draws `npc` (our
reading of x.15a). The `NPC` mask data fall under the 0.005 grid of rule
x.1b, not among the layers x.1a names (our reading; both values are
printed with the unit "mm").[^pdk-periph]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", checks the drawn layer at the periphery values
— "0.27 min. width of npc" (npc.1), "0.27 min. spacing/notch of npc"
(npc.2), "0.09 min. spacing of npc & gate" and "npc must not overlap
gate" (npc.4) — and adds a core rule the periphery tables do not have,
`npcon.c6`, "0.045 min. enclosure of "poly_licon1" in core by npc",
against the 0.1 of licon.15 in the periphery.[^pdk-errors] It also lists
two `cnpc.nikon` checks, "NPCMmk in the nikon cross has the wrong
polarity" and "NPCMmk is missing from the nikon cross in the layout",
module-cut checks at 0.135 ("0.135 min. spacing of moduleCutAREA &
q0npcnotBuildSpace", x.12a), "npc drawn layer cannot straddle
areaid:ModuleCut" (scribe.7) and x.15a messages for `cnpc` and
`NPCMmk`.[^pdk-errors] Unlike the `NTM` and `HVNTM` checks, it names no
created `NPC` layer ({ref}`mask-ntm`, {ref}`mask-hvntm`).

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `NPCM` the site renders layer 95:20 (`npc`)
alone, with no Boolean expression, no fill layer and no note, on all
eight runs; its mask record gives the mask-level layer
49:0.[^mask-renders] That is the index's pairing; the render has no term
for created resistor shapes, and the choice of layer is one public
derivation from the drawn data, not SkyWater's mask-generation recipe.

Every rendered die of every run carries `npc` shapes — at least 235 574
on each die; the minimum on each run is 235 574 (MPW-6 to MPW-8),
280 381 (MPW-5), 281 087 to 281 104 (MPW-2 to MPW-4) or 329 255 (MPW-1);
on MPW-1 one die accounts for 97 % of the run's shapes; and counts rarely
repeat, on at most seven dies of a run and on none of MPW-1, MPW-4 or
MPW-8.[^mask-renders] The count of 40 dies therefore says only that every
layout contacts poly, as a working die must; we read the large minimum
as shapes that every die of these runs carries rather than as project
content (inference; the site does not say what they are). The site
states the limits of its images: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled."[^mask-renders] Its metadata
carries no plate ID, so a render is tied to a plate in the process-steps
sheet only by the acronym `NPCM`, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `NPCM` plate
as existing on all eight MPW runs, with the plate number `180` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA180A` |
| MPW-2 | `5CS8007AC` | `S8007AA180A` |
| MPW-3 | `5CS8008AC` | `S8008AA180A` |
| MPW-4 | `5CS8018AC` | `S8018AA180A` |
| MPW-5 | `5CS8011AC` | `S8011AA180A` |
| MPW-6 | `5CS8014AC` | `S8014AA180A` |
| MPW-7 | `5CS8016AC` | `S8016AA180A` |
| MPW-8 | `5CS8017AC` | `S8017AA180A` |

* **Plate number.** The sheet does not say what `180` encodes. It lies
  between `178` for `URPM` (step 55) and `190` for `TUNM` (step 35), and
  below `210` for `P1M` (step 61), which precedes it in the flow, so the
  numbers do not follow process order and no process position is read
  from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `NPCM`,[^steps-sheet] and whether the plate is binary or phase-shift is
  not on public record. 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`NPCM <step-078>` page puts the 0.27 µm
opening at {math}`k_1 = 0.27 \times 0.6 / 0.365 \approx 0.44` on an
i-line stepper of NA 0.6 and at about 0.65 on a 248 nm tool, cites ITRS
2001's exposure options for the 130 nm node, which the roadmap gives for
critical layers,[^itrs-03] and infers a DUV level "driven by its 0.09 µm
placement tolerance to poly rather than by its CD"; the
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there with an
{ref}`i-line <machine-i-line-stepper>` alternative. At NA 0.7 the KrF
figure is {math}`k_1 = 0.27 \times 0.7 / 0.248 \approx 0.76` (our
arithmetic). ASML's PAS 5500/750E "achieves 130 nm resolution while using
standard 248 nm light".[^asml-750e] SkyWater lists "ASML DUV stepper",
"ASML DUV scanner", "ASML I-line stepper" and "ASML I-line scanner" but
assigns no layer to them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns and 0.75
(lambda) /NA for contacts", and that dark-field spaces are more sensitive
than light-field lines.[^wong-1998] For the 0.27 µm openings the
line-space threshold is about 0.18 µm to 0.21 µm at 248 nm and NA 0.7 to
0.6, but about 0.30 µm at 365 nm and NA 0.6, and the contact threshold is
about 0.27 µm to 0.31 µm at 248 nm (our arithmetic), so a plate CD error
would print at about its own size on a KrF tool for long cuts and begin
to be magnified for small square cuts or on an i-line tool (inference).
How tightly SkyWater specifies the plate is not public.

**Resist and tone.** The step page reads a bottom anti-reflective coating
and a DUV resist of the order of 0.5–0.7 µm over the capped poly lines
and spacers, roughly 0.4 µm tall from Table 4's "poly thickness" of 0.18
(`POLYTH`) and "poly cap after SPE" of 0.2 (`OVGTTH`), and takes the PDK's
generic "Photoresist thickness" of 1.14 as an implant-layer
value;[^pdk-03] the resist need only survive a short nitride etch. On
stepped, reflective topography the swing ratio matters, which Brunner
showed scales with the square root of the substrate reflectivity and an
anti-reflective coating reduces.[^brunner-1991] With the openings drawn
where `npc` is, the plate would be dark-field (inference). Neither the
resist nor the tone is published; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page and
the coat and develop on the
{ref}`coat/develop track <machine-coat-develop-track>` page. For the process window the step page points to Bossung's
focus–exposure characterisation[^bossung-1977] and Ausschnitt's
separation of dose from defocus.[^ausschnitt-1999]

**Pattern transfer.** On the step pages' readings the pattern is
transferred by {ref}`NPCME <step-079>` through whatever remains of the
oxide cap and the nitride cap, stopping on the poly, on the
{ref}`dielectric and nitride plasma etcher <machine-plasma-etcher-dielectric>`
class, and the resist strip and clean are treated as part of that step.
The `NPCME` page names a fluorine chemistry tuned for nitride over silicon,
of the kind Kastenmeier, Matsuo and Oehrlein studied,[^kastenmeier-1999]
an endpoint on CN emission, since "a strong peak at 387 nm indicates that
CN is present in the plasma, usually indicating that nitride is being
etched",[^pat-cn-tel] and loading effects in small, sparse windows of the
kind Gottscho, Jurgensen and Vitkavage analysed.[^gottscho-1992] On our
reading, the small open area of a cut layer, the property that weakens
that endpoint signal, is fixed by this mask.

**Overlay.** The placement rules are the tight ones: 0.090 µm from any
gate (npc.4), 0.100 µm around a periphery poly contact (licon.15) and
0.090 µm from a diffusion contact (licon.13), with a maximum as well as a
minimum at the slotted resistor contacts (npc.5, rpm.5).[^pdk-periph] The
{ref}`NPCM <step-078>` page reads the mask as aligned to poly, whose
{ref}`P1M <mask-p1m>` pattern both npc.4 and licon.15 reference, and
notes that a cut 0.09 µm out of place over a poly line would expose the
gate edge to the nitride etch. ASML gives the /750E an overlay of "less than
30 nm";[^asml-750e] van Haren et al. show how alignment-mark placement on
the reticle limits layer-to-layer overlay,[^van-haren-2019] and Starikov
analysed the accuracy of the overlay measurements on which such margins
rely[^starikov-1992] (our comparison; how SkyWater budgets the margin is
not public).

(mask-npcm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `NPCM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`NPCM <step-078>`, {ref}`NPCME <step-079>`

* {ref}`NPCM <step-078>` — coats, exposes and develops the resist over the
  capped poly and spacers.
* {ref}`NPCME <step-079>` — etches the cap in the openings, stopping on
  the poly; the step list used in this reference has no separate strip
  step, and the step page treats the resist strip and clean as part of
  the etch.

On its step page's reading, the next step, {ref}`SPOX <step-080>`,
deposits a blanket oxide over the wafer, the opened poly included, after
the resist is gone. The next mask step is {ref}`PSDM <step-081>`. The only
departure from a mask–etch–strip pattern is that the strip has no step of
its own; the rule itself needs no exception.

## Design rules and critical dimensions

The `npc` rules of the periphery rules, with the contact and
precision-resistor rules that place other layers against `npc` and the
mask-data rules x.7 and x.15a; flag P means "Rule applies to periphery
only (outside areaid.ce). A corresponding core rule may or may not
exist." and NC "Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| npc.1 | "Min width of NPC" | 0.270 µm |
| npc.2 | "Min spacing of NPC to NPC" | 0.270 µm |
| npc.3 | "Manual merge if less than minimum" | — |
| npc.4 | "Spacing (no overlap) of NPC to Gate" | 0.090 µm |
| npc.5 | "Max enclosure of poly overlapping slotted_licon by npcm (merge between adjacent short edges of the slotted_licons if space < min)" | 0.095 µm |
| licon.13 | "Spacing (no overlap) of NPC to licon on diff or tap" (P) | 0.090 µm |
| licon.15 | "poly_licon must be enclosed by npc by…" (P) | 0.100 µm |
| licon.18 | "Npc must enclose poly_licon" | — |
| rpm.5 | "prec_resistor must be enclosed by npc by atleast" | 0.095 µm |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`NPCMCD` 0.27 and `NPCMCDSP` 0.27, and no other criterion names the
mask; Table 4's "poly cap after SPE" of 0.2 and "poly thickness" of 0.18,
in its column headed "Value (um)", describe the stack the cut
opens.[^pdk-03] Table F3a of the *Summary of Key Periphery Rules* gives
`npc` a width of 0.270, a spacing of 0.270 to itself and 0.090 to poly
and "Yes" in the "Manual" (merge) column, and gives the enclosure of
`poly_licon` by `npc` as 0.100 and the spacing of `licon` to `npc` as
0.090 (our reading of the columns, whose spacing and enclosure labels
sit in the table's first row).[^pdk-summary] The Error Messages page adds the core enclosure of
0.045 (`npcon.c6`).[^pdk-errors] For the plate the smallest features are
0.270 µm openings on a 0.270 µm space, placed to within 0.090 µm of the
gates.

## Related pages

* {ref}`NPCM <step-078>` and {ref}`NPCME <step-079>` — the mask step and
  the cut etch; {ref}`SPE <step-077>` — the spacer etch that leaves the
  cap the cut opens.
* {ref}`mask-p1m` — the poly pattern the cut is placed against;
  {ref}`mask-licm1` — the contact mask whose poly contacts land in the
  cuts; {ref}`mask-psdm` — the P+ implant mask whose implant reaches the
  opened resistor heads.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-duv-krf-stepper` and {ref}`machine-i-line-stepper` — the
  exposure class the step page assigns and its alternative.
* {ref}`machine-plasma-etcher-dielectric` — the etch class that transfers
  the pattern.
* {ref}`machine-cd-sem-overlay-metrology` — CD and overlay measurement.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Nitride Poly Cut, NPCM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `npc` 95:20,
  the `cnpc` purposes and the `NPC` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `NPCMCD`/`NPCMCDSP`, the poly
  and cap thicknesses and the photoresist thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `npc` rules, licon.13, licon.15,
  licon.18, rpm.4, rpm.5, x.1a, x.1b, x.7, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Table F3a and Table
  F4.[^pdk-summary]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `npc` and
  `npcon.c6` checks, the module-cut and "nikon cross"
  checks.[^pdk-errors]
* *S8 / SKY130 Process Steps* sheet — the step, the `NPCM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `NPCM` renders, their layer
  and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the DUV and i-line exposure
  tools.[^skw-01]
* ASML, PAS 5500/750E press release — a KrF scanner for 130 nm design
  rules.[^asml-750e]
* Tokyo Electron, US 6,376,262 — CN emission as the nitride etch
  endpoint.[^pat-cn-tel]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Photolithography* — i-line and DUV exposure and the
  resolution equation.[^wiki-litho]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and tool
  choice.[^levinson-2005]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — DUV lithography
  of the 0.25–0.13 µm generations.[^txt-05]

### Deep dive

* Tang et al., IEDM 1985 — a TiN local-interconnect layer formed during
  self-aligned silicidation and patterned between gates and junctions
  (abstract).[^tang-1985]
* Tang et al., *IEEE TED* 1987 — the same TiN local interconnect, with
  its delay and SRAM applications (abstract).[^tang-1987]
* Cacciato et al., PPID 2003 — charging damage when a contact etch meets
  a borderless nitride.[^cacciato-2003]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor of spaces
  and contacts and the sizes below which it rises.[^wong-1998]
* Brunner, *Proc. SPIE* 1991 — swing curves and anti-reflective
  layers.[^brunner-1991]
* Bossung, *Proc. SPIE* 1977 — focus–exposure plots for projection
  printing.[^bossung-1977]
* Ausschnitt, *Proc. SPIE* 1999 — distinguishing dose from defocus for
  in-line lithography control.[^ausschnitt-1999]
* Kastenmeier, Matsuo and Oehrlein, *JVST A* 1999 — etching silicon
  nitride selectively over silicon and oxide.[^kastenmeier-1999]
* Gottscho, Jurgensen and Vitkavage, *JVST B* 1992 — microscopic
  uniformity and aspect-ratio-dependent etching.[^gottscho-1992]
* van Haren et al., *Proc. SPIE* 2019 — alignment-mark placement and
  layer-to-layer overlay.[^van-haren-2019]
* Starikov, *Opt. Eng.* 1992 — the accuracy of overlay
  measurement.[^starikov-1992]
* ITRS 2001, *Lithography* — exposure options for critical layers and
  mask magnification at 130 nm.[^itrs-03]

## Open questions

* The operation that makes the `cnpc` plate data from `npc`, what its
  drawing purpose contributes, and what the created shapes Table F2b
  marks for the p+ poly resistor are, are not published.[^pdk-06]
* That the resistor openings exist so that the P⁺ implant dopes the
  resistor heads is the step page's inference from the rule text.
* Whether the level is exposed on a KrF or an i-line tool, and the
  plate's type, tone and CD specification, the resist and the
  anti-reflective scheme, are not public.
* The Error Messages page's core enclosure `npcon.c6` (0.045) has no
  counterpart in the periphery rules, which give 0.100 µm for the
  periphery only.[^pdk-errors][^pdk-periph]
* What the plate number `180` encodes is not stated, and no public source
  lists the `NPCM` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists" and "Plate ID" columns per run)
    and "Sheet4" (mask types), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table F2b,
    the mask generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    4), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Tables F3a and F4), SkyWater SKY130 PDK documentation, retrieved
    2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/summary/table-f3a-font-end-low-voltage.csv>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_NPCM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-750e]: ASML, *ASML introduces KrF lithography scanner* (PAS
    5500/750E), press release, 2000-04-04.
    <https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
[^pat-cn-tel]: Tokyo Electron Ltd., *Method of forming a semiconductor
    device using double endpoint detection*, US 6,376,262 B1, granted
    2002-04-23. <https://patents.google.com/patent/US6376262B1/en>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^tang-1985]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    C.-F. Wan and M. A. Douglas, "VLSI local interconnect level using
    titanium nitride", *IEDM 1985 Technical Digest*, pp. 590–593.
    <https://doi.org/10.1109/IEDM.1985.191041>
[^tang-1987]: T. E. Tang, C.-C. Wei, R. A. Haken, T. C. Holloway,
    L. R. Hite and T. G. W. Blake, "Titanium nitride local interconnect
    technology for VLSI", *IEEE Transactions on Electron Devices*
    **34**(3), 682–688 (1987). <https://doi.org/10.1109/T-ED.1987.22980>
[^cacciato-2003]: A. Cacciato, A. Scarpa, S. Evseev and M. Diekema,
    "Charging damage during contact etch triggered by increased
    borderless nitride conductivity", *Proc. 2003 8th International
    Symposium on Plasma- and Process-Induced Damage*, pp. 20–23.
    <https://doi.org/10.1109/PPID.2003.1199721>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^bossung-1977]: J. W. Bossung, "Projection Printing Characterization",
    *Proc. SPIE* **100**, 80–85 (1977). <https://doi.org/10.1117/12.955357>
[^ausschnitt-1999]: C. P. Ausschnitt, "Distinguishing dose from defocus
    for in-line lithography control", *Proc. SPIE* **3677**, Metrology,
    Inspection, and Process Control for Microlithography XIII, 140
    (1999). <https://doi.org/10.1117/12.350800>
[^kastenmeier-1999]: B. E. E. Kastenmeier, P. J. Matsuo and
    G. S. Oehrlein, "Highly selective etching of silicon nitride over
    silicon and silicon dioxide", *Journal of Vacuum Science &
    Technology A* **17**(6), 3179–3184 (1999).
    <https://doi.org/10.1116/1.582097>
[^gottscho-1992]: R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage,
    "Microscopic uniformity in plasma etching", *Journal of Vacuum
    Science & Technology B* **10**(5), 2133–2147 (1992).
    <https://doi.org/10.1116/1.586180>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
[^starikov-1992]: A. Starikov, "Accuracy of overlay measurements: tool
    and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
    (1992). <https://doi.org/10.1117/12.56172>
