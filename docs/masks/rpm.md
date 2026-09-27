(mask-rpm)=
# RPM — Resistor Protect

The resistor protect mask is the first of SKY130's three poly-resistor
{term}`reticles <reticle>` and the first mask printed on the gate film.
On the {ref}`RPM <step-049>` page's reading, the resist printed through
it at step 49 stays as islands over the future precision-resistor
bodies.

| | RPM — Resistor Protect |
|---|---|
| Mask step | {ref}`RPM <step-049>`, step 49 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Resistor Protect", `RPM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `crpm` mask 96:0, "Resistor Protect mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `rpm` drawing 86:20, "300 ohms/square polysilicon resistor implant"; `urpm` drawing 79:20, "2000 ohms/square polysilicon resistor implant" — the pairing with `urpm` is an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | `RPMCD` 1.27 / `RPMCDSP` 0.84[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains as islands over the resistor bodies, so with a positive resist the plate would be mostly clear with opaque islands (inference). |
| Exposure class | i-line, an inference on the step page from the 1.27 µm width and 0.84 µm space, with a KrF tool named as the option if a fab keeps all layers on one platform; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `175`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 1, 5, 0, 3, 4, 2, 3, 2[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-rpm-steps>` |

:::{seealso}
How the step is performed is on the step page;
every mask is indexed on the {ref}`masks index <masks-index>`.
:::

## What the mask defines

On the {ref}`RPM <step-049>` page's reading, the heavy n-type gate implant {ref}`P1I <step-050>` dopes all the
rest of the undoped film, and the resist is stripped at
{ref}`P1IS <step-051>`. The mask is the only one of the three resistor masks
that `masks.csv` lists. The public renders of the MPW tape-out layouts
show its drawn layer on few dies — between none and five of the 40 on
each run — although the process-steps sheet records a plate for it on
every run.

The PDK names the layer's purpose in three places: `masks.csv` lists
"Resistor Protect", `gds_layers.csv` describes `rpm` as "300 ohms/square
polysilicon resistor implant", and the rule set's function line reads
"Defines p+ poly resistors".[^pdk-05][^pdk-06][^pdk-periph] Table C3 of
the *Layers Reference* defines the device the rules call
`prec_resistor` as "rpm AND (poly overlapping poly.rs) AND
psdm".[^pdk-06]

The devices are:[^pdk-07]

* the "P+ poly precision resistors", which
  "have 5 different fixed widths, plus a variable W/L option", each end
  "contacted using a slot licon"
* the "P- poly precision resistors",
  for which "a separate implant is used to set the sheet resistance to
  2000 ohm/sq" and which "have the same layout footprints as their P+ poly
  counterparts"

The extraction table, in a column headed
"Resistivity (mohms/sq)", gives 319800 for the "XHR poly resistor",
2000000 for the "UHR poly resistor" and 48200 for "Poly", that is
319.8 Ω/sq, 2000 Ω/sq and 48.2 Ω/sq (our conversion).[^pdk-08]

The {ref}`RPM <step-049>` page reads the mask from the doping these
figures imply. The generic poly resistor is "N+ doped gate
poly",[^pdk-07] while both precision flavours are p-type, so the step
page infers that:

* `RPM` protects the resistor bodies from the n-type gate
  implant
* the p-type doping comes later through
  {ref}`RRPM <step-052>` and {ref}`URPM <step-055>`
* the resist
  covers the `urpm` bodies as well as the `rpm` ones

The step page leaves open
whether the `urpm` regions are on this plate or only on their own later
mask. Lu et al. modelled how grain structure and doping set the
resistance of monolithic poly resistors,[^lu-1981] and Lane and Wrixon
set out the design of poly resistors for analogue ICs.[^lane-1989]

The PDK's mask generation table, Table F2b, marks the `RPM` column:[^pdk-06]

* `C`
  ("CREATED") in one of its 80 device rows, "p+ poly resistor" (model
  `xhrpoly_*_*`)
* `-` ("Layer not created for the device") in 40 rows —
  among them the "n+ poly resistor" and every transistor, varactor and
  SONOS row
* `+` ("Layer allowed to overlap") in the other
  39

The table has no row for the 2000 Ω/sq resistor and no
`URPM` column, so it does not show whether `urpm` bodies receive created
`RPM` data (our reading of the table).

What the mask does not define is
the resistor's outline: on the step pages' readings the body is cut from
the poly at {ref}`P1M <step-061>`, and its ends are opened through the
nitride cut of {ref}`NPCM <step-078>` and contacted by the slot contacts
of {ref}`LICM1 <step-093>`.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has one mask-level layer for this mask, `crpm` with
purpose `mask` at 96:0 ("Resistor Protect mask"), and no `drawing`,
`mask add`, `mask drop` or `waffle drop` purpose. Layer number 96 also
carries the `cncm` drawing purpose, 96:44 ({ref}`masks-index`). The drawn
layers are `rpm` at 86:20 and `urpm` at 79:20.[^pdk-06] The pairing with
`rpm` rests on the names and descriptions, and the pairing with `urpm`
on the step page's reading above; the PDK publishes no operation that
turns either layer into the plate.

Rule x.15a confines "Drawn compatible,
mask, and waffle-drop layers" to test modules, the seal ring and the
frame, with the exception "FOM/P1M/Metal waffle drop are allowed inside
the die" (flag P).[^pdk-periph] So a design inside the die draws `rpm`,
not `crpm` (our reading of x.15a).

The PDK's *Error Messages* page describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data".[^pdk-errors] It has the generic grid, octagonal-edge and x.15a
checks for a mask-data layer `RPMmk` and a "nikon cross" check,
`crpm.nikon`: "RPMmk in the nikon cross has the wrong polarity" and
"RPMmk is missing from the nikon cross in the layout".[^pdk-errors]

The page
lists messages for rpm.3 to rpm.10 with the periphery rules' values
where those give one — "0.11 min. enclosure of precResistor by psdm",
"0.185 min. spacing of precResistor & hvntm" — and adds a value for
rpm.10, "2 min. spacing of rpmNotXmt & pwbm", which the periphery rules
give as "N/A".[^pdk-errors][^pdk-periph] It has no message under the names
rpm.1a or rpm.2.[^pdk-errors]

Under the names urpm.1a, urpm.2 and urpm.3 it lists
"1.27 min. width of urpm", "0.84 min. spacing/notch of urpm" and "0.2
min. enclosure of precResistor by rpm", the values of rpm.1a, rpm.2 and
rpm.3 (our comparison).[^pdk-errors] They sit, in the page's numbering,
immediately before the rpm.3 message, so they may be the missing `rpm`
checks filed under `urpm` names or checks applying the same geometry to
`urpm` (our reading).[^pdk-errors] The periphery rules have no `urpm`
rule set, and the page does not say how the `urpm` checks relate to the
`rpm` rules.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `RPM` the site renders layer 86:20 (`rpm`)
alone, with no Boolean expression, no fill layer and no note, on all
eight runs.[^mask-renders] Its mask record gives the mask-level layer
96:0.[^mask-renders] The render has no `urpm` term, unlike the index's
and the step page's pairing ({ref}`masks-derivations`). The choice of
layer is one public derivation from the drawn data, not SkyWater's
mask-generation recipe, and neither source settles which is right.

Few dies draw `rpm`, and on the runs that have any they are these
frames:[^mask-renders]

:::{table} Dies that draw `rpm` on each run, from the renders: frame and shape count
| Run | Dies with `rpm` shapes (frame and shape count) |
|-----|-----------------------------------------------|
| MPW-1 | F4 (2) |
| MPW-2 | A3 (6), D7 (27), E3 (9), F5 (6), F7 (30) |
| MPW-3 | none |
| MPW-4 | C6 (7), D1 (7), F5 (1) |
| MPW-5 | C3 (8), C6 (5), D1 (2), D3 (164) |
| MPW-6 | B2 (32), B7 (1) |
| MPW-7 | B5 (82), C2 (1), F3 (80) |
| MPW-8 | B1 (480), C7 (55) |
:::

The site renders `URPM` from `urpm` 79:20 and shows shapes on every die
of every run ({ref}`masks-renders`),[^mask-renders] so on the step page's
reading, in which this plate also covers the `urpm` bodies, a render of
`rpm` alone would understate what the plate carries (inference).

The
site states the limits of its images: "These are renders of *drawn*
data, not photomask artwork: reticle pitch, 4x reduction, mirroring and
the frame features the fab adds are not modelled. Empty images are real
results - several masks are used by no project on a given
shuttle."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the process-steps sheet only by the acronym `RPM`,
and the MPW-4 renders come from a different reticle set from the one
whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `RPM` plate
as existing on all eight MPW runs, with the plate number `175` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA175A` |
| MPW-2 | `5CS8007AC` | `S8007AA175A` |
| MPW-3 | `5CS8008AC` | `S8008AA175A` |
| MPW-4 | `5CS8018AC` | `S8018AA175A` |
| MPW-5 | `5CS8011AC` | `S8011AA175A` |
| MPW-6 | `5CS8014AC` | `S8014AA175A` |
| MPW-7 | `5CS8016AC` | `S8016AA175A` |
| MPW-8 | `5CS8017AC` | `S8017AA175A` |

* **MPW-3.** A plate is recorded on MPW-3, on which no rendered die draws
  `rpm`, the layer the renders use for this mask.[^steps-sheet][^mask-renders]
  The renders leave out whatever the fab adds to a plate, and on the step
  page's reading the plate would also carry the `urpm` bodies, so they
  cannot show what the MPW-3 plate carries ({ref}`masks-renders`).
* **Plate number.** The three resistor masks carry close numbers — `175`
  for `RPM`, `177` for `RRPM` and `178` for `URPM` — but the numbers do
  not follow process order elsewhere (`LVOM`, step 44, is `125`; `TUNM`,
  step 35, `190`).[^steps-sheet] The sheet does not say what they encode, so no
  process position or grouping is read from them
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `RPM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

### Exposure class

The {ref}`RPM <step-049>` page reads the 1.27 µm /
0.84 µm pattern as far above the i-line resolution limit and infers an
i-line level, naming a KrF tool as the option for a fab that keeps all
layers on one platform. The {ref}`i-line stepper <machine-i-line-stepper>`
page lists it there. SkyWater lists "ASML I-line stepper" and "ASML
I-line scanner" among its tools but assigns no layer to them.[^skw-01]

At NA 0.48, the low end of ASML's PAS 5500/275D,[^asml-pas5500-275d] the
0.84 µm space has {math}`k_1 \approx 1.1` (our arithmetic). Wong et
al.'s mask error factor "is unity for large features",[^wong-1998] so a
CD error on this plate would print at about its own size (inference).

### Resist and tone

On the step page's reading the resist is coated on bare
amorphous silicon. The
{ref}`RPM <step-049>` page reads a conventional positive i-line resist of
about 1 µm, the PDK's generic "Photoresist thickness" being
1.14 µm,[^pdk-03] as ample for a shallow poly-doping implant of tens of
keV (industry-typical on the {ref}`P1I <step-050>` page). On the step page's reading,
anti-reflective coating is optional because amorphous silicon absorbs
strongly at 365 nm.

The implant is heavy: the {ref}`P1IS <step-051>` page
reads it as leaving a fully developed carbonised crust, the layer Orvek
and Huffman studied on ion-implanted resist masks.[^orvek-1985]
SkyWater's resist is not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

### Resist edges

Hook et al. found that ions scattered out of the edge
of an implant resist are implanted in the silicon near the mask edge,
with threshold shifts "of up to 100 mV … over a lateral distance on the
order of a micrometer".[^hook-2003] The {ref}`P1I <step-050>` page cites
the study for shadowing at the edges of the `RPM` islands if the implant
were tilted. The PDK does not say what the 0.200 µm of rpm.3 and rpm.7
allow for (below).

### Overlay and alignment

The poly has not been patterned, so the
{ref}`RPM <step-049>` page infers alignment to the trench marks of
{ref}`FOM <step-004>`. It reads the 0.200 µm enclosure of the precision
resistor by `rpm` (rpm.3) as the overlay budget between this layer and
{ref}`P1M <step-061>`, both registered to the same reference.[^pdk-periph]
ASML specifies "≤ 40 nm" single-machine overlay for the /275D
stepper[^asml-pas5500-275d] (our comparison; SkyWater's budget is not
public). A line that crossed the `rpm` edge would be doped n⁺ on one side
and p on the other, which the step page gives as the reason for rpm.8,
"poly must not straddle rpm".

### Pattern transfer

Nothing is etched through this resist. On the step
pages' readings the pattern is transferred into the gate film as dopant
by {ref}`P1I <step-050>`, on the
{ref}`high-current implanter <machine-high-current-implanter>` class, and
the resist is removed at {ref}`P1IS <step-051>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The PDK gives the result
only as sheet resistances — 48.2 Ω/sq for "Poly", 319.8 Ω/sq for the
"XHR poly resistor" and 2000 Ω/sq for the "UHR poly resistor"[^pdk-08] —
which the step pages read as the gate-implanted film and the two
protected, later-implanted bodies.

Liu et al. separate a poly resistor's value into an
electrical width reduction, an interface resistance at its ends and a
"pure sheet resistance".[^liu-2001] The {ref}`RRPM <step-052>` page reads
part of the SKY130 resistor's end resistance as set where the doped body
meets the n⁺ poly, that is, by the `rpm` edge (inference on that page).

(mask-rpm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `RPM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`RPM <step-049>`, {ref}`P1I <step-050>`, {ref}`P1IS <step-051>`

* {ref}`RPM <step-049>` — coats, exposes and develops the resist islands
  on the undoped gate film.
* {ref}`P1I <step-050>` — the heavy n-type gate implant into the film
  outside the islands.
* {ref}`P1IS <step-051>` — strips the heavily implanted resist and cleans
  the film for the next mask.

The next step, {ref}`RRPM <step-052>`, is itself the next mask step: on
its step page's reading it coats the reverse resistor mask on the cleaned
film and opens windows over the bodies this resist protected. No step
between `P1IS` and it uses the `RPM` resist, and there is no exception
to the rule for this mask.

## Design rules and critical dimensions

The `rpm` rules of the periphery rules, with the `licon` rules for
contacts inside the precision resistor and rule x.15a; flag P means "Rule
applies to periphery only (outside areaid.ce). A corresponding core rule
may or may not exist.". The unit column of rpm.3 is blank in the
published table.[^pdk-periph]

:::{table} The `rpm` rules, with the `licon` rules for contacts inside the precision resistor and rule x.15a, as published; the unit column of rpm.3 is blank in the published table

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| rpm.1a | "Min width of rpm" | 1.270 µm |
| rpm.1b–1f | "Min/Max prec_resistor width xhrpoly_0p35" and the same for xhrpoly_0p69, 1p41, 2p85 and 5p73 | 0.350, 0.690, 1.410, 2.850, 5.730 µm |
| rpm.1g–1k | "Only 1 licon is allowed in xhrpoly_0p35 prec_resistor_terminal"; 1, 2, 4 and 8 for the other widths | — |
| rpm.2 | "Min spacing of rpm to rpm" | 0.840 µm |
| rpm.3 | "rpm must enclose prec_resistor by atleast" | 0.200 |
| rpm.4 | "prec_resistor must be enclosed by psdm by atleast" | 0.110 µm |
| rpm.5 | "prec_resistor must be enclosed by npc by atleast" | 0.095 µm |
| rpm.6 | "Min spacing, no overlap, of rpm and nsdm" | 0.200 µm |
| rpm.7 | "Min spacing between rpm and poly" | 0.200 µm |
| rpm.8 | "poly must not straddle rpm" | — |
| rpm.9 | "Min space, no overlap, between prec_resistor and hvntm" | 0.185 µm |
| rpm.10 | "Min spacing of rpm to pwbm" | N/A |
| rpm.11 | "rpm should not overlap or straddle pwbm except cells […]" | N/A |
| licon.1b | "Min and max width of licon inside prec_resistor" | 0.190 µm |
| licon.1c | "Min and max length of licon inside prec_resistor" | 2.000 µm |
| licon.9 | "Spacing, no overlap, between poly_licon and psdm; In SKY130DIA/SKY130TMA/SKY130PIR-10 flows, the rule is checked only between (poly_licon outside rpm) and psdm" (P) | 0.110 µm |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
:::

*Criteria & Assumptions* repeats the width and space in Table 2, and in the block of Table 4 headed
"Other", whose value column is headed "Value", it gives the following:[^pdk-03]

:::{table} Parameters of *Criteria & Assumptions* for the mask
| Parameter (table) | Published description | Value |
|---|---|---|
| `RPMCD` (Table 2) | width | 1.27 |
| `RPMCDSP` (Table 2) | space | 0.84 |
| `POLYRCD` (Table 4) | "Poly resistor width and spacing to reduce CD variation (um)" | 0.33, the value of poly.3[^pdk-periph] |
| `POLYRSPC` (Table 4) | "Poly resistor width and spacing to reduce CD variation (um)" | 0.48, the value of poly.9[^pdk-periph] |
| `PRECRESW` (Table 4) | "Precision resistor width to accommodate 6 contacts across" | 2.03 |
:::

For the plate the decisive figures
are the 1.270 µm width and 0.840 µm space of `rpm`; the resistor widths
of rpm.1b to rpm.1f belong to the poly pattern inside the islands, not
to this plate.

## Related pages

* **Steps.** {ref}`RPM <step-049>`, {ref}`P1I <step-050>` and
  {ref}`P1IS <step-051>` — the mask step, the gate implant and the strip.
  {ref}`RRPM <step-052>` and {ref}`URPM <step-055>` — the reverse and
  ultra-high resistor masks that follow.
* **Category.** {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.
* **Machines.** {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns. {ref}`machine-high-current-implanter` — the implant class that uses the
  pattern.
* **Materials.** {ref}`material-lithography-materials` — resists, developer and
  reticles.
* **Masks.** {ref}`mask-rrpm` and
  {ref}`mask-urpm` — the RRPM and URPM mask pages. {ref}`mask-p1m` — the poly mask that cuts the resistor bodies.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the derivations the renders use.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Resistor Protect, RPM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `rpm`, `urpm`,
  `crpm`, the `prec_resistor` definition of Table C3 and the `RPM`
  column of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `RPMCD`/`RPMCDSP`, the poly
  resistor and precision resistor criteria and the photoresist
  thickness.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `rpm` rules and function line,
  licon.1b, licon.1c, licon.9, x.15a and the flag legend.[^pdk-periph]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the `rpm` and
  `urpm` messages and the `RPMmk` checks.[^pdk-errors]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — the P+ and P− poly precision
  resistors.[^pdk-07]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the poly and resistor
  sheet resistances.[^pdk-08]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `RPM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `RPM` renders, their layer
  and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *PAS 5500/275D* data sheet](<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>) — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Ion implantation*](<https://en.wikipedia.org/wiki/Ion_implantation>) — masking, range and
  energy.[^wiki-implant]
* [Wikipedia, *Sheet resistance*](<https://en.wikipedia.org/wiki/Sheet_resistance>) — the ohms-per-square
  convention.[^wiki-rs]
* [Kamins, *Polycrystalline Silicon for Integrated Circuits and Displays*](<https://doi.org/10.1007/978-1-4615-5577-3>) —
  deposition, doping and electrical properties of poly
  films.[^kamins-1998]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]

### Deep dive

* [Lu et al., *IEEE TED* 1981](<https://doi.org/10.1109/T-ED.1981.20437>) — modelling and optimisation of monolithic
  poly resistors.[^lu-1981]
* [Lane and Wrixon, *IEEE TED* 1989](<https://doi.org/10.1109/16.22479>) — the design of thin-film poly
  resistors for analogue ICs.[^lane-1989]
* [Seto, *J. Appl. Phys.* 1975](<https://doi.org/10.1063/1.321593>) — grain-boundary trapping and the steep
  dependence of poly resistivity on doping.[^seto-1975]
* [Mandurah, Saraswat and Kamins, *IEEE TED* 1981](<https://doi.org/10.1109/T-ED.1981.20504>) — conduction in poly
  with dopant segregation to the grain boundaries.[^mandurah-1981]
* [Liu et al., *IEEE EDL* 2001](<https://doi.org/10.1109/55.930677>) — electrical width, interface resistance
  and sheet resistance of poly resistors in sub-0.25 µm CMOS.[^liu-2001]
* [O'Dwyer and Kennedy, PRIME 2009](<https://doi.org/10.1109/RME.2009.5201322>) — matching of poly resistor films in a
  CMOS process.[^odwyer-2009]
* [Tsang et al., *IEEE TSM* 2014](<https://doi.org/10.1109/TSM.2014.2311375>) — resistance variation across banks of
  high-value poly resistors.[^tsang-2014]
* [Wright et al., *JVST B* 2010](<https://doi.org/10.1116/1.3466531>) — rf-sputtered Cr–Si–B–SiO₂/Al₂O₃
  thin-film resistors reaching 20 kΩ/sq at <200 ppm/°C: the non-poly
  alternative route to a high-sheet-resistance, low-TCR
  film.[^wright-2010]
* [Orvek and Huffman, *NIM B* 1985](<https://doi.org/10.1016/0168-583X(85)90421-5>) — the carbonised layer on ion-implanted
  resist masks.[^orvek-1985]
* [Hook et al., *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — ions scattered from the resist edge and
  their lateral reach.[^hook-2003]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  size below which it rises.[^wong-1998]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — mask magnification and the optical mask
  requirements of the 130 nm generation.[^itrs-03]

## Open questions

* Whether the plate covers the `urpm` bodies as well as the `rpm` ones,
  as the step page reads it, or `rpm` alone, as the renders use it, is
  not public; Table F2b has no row for the 2000 Ω/sq resistor.[^pdk-06][^mask-renders]
* The operation that makes the `crpm` plate data is not published, and
  the Error Messages page's `urpm.1a` to `urpm.3` messages, which carry
  the `rpm` values, are not explained.[^pdk-06][^pdk-errors]
* What the MPW-3 plate carries is not public: no rendered die of that
  run draws `rpm`.[^steps-sheet][^mask-renders]
* The plate's tone, blank, absorber and magnification, the resist and the
  exposure tool are not public; the i-line reading rests on the
  1.270 µm / 0.840 µm rules.
* What the plate number `175` encodes is not stated, and no public source
  lists the `RPM` plate of the original MPW-4 set
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
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C3,
    device, LVS and other CAD definitions, and Table F2b, the mask
    generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    4), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_RPM/` and
    `mpw-00N_URPM/` directories with their pages, `job.json`,
    `result.json` and per-die slot JSON files, retrieved 2026-09-14.
    Rendered from the public shuttle repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-pas5500-275d]: ASML, *PAS 5500/275D High Productivity i-Line
    Stepper*, refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^kamins-1998]: T. Kamins, *Polycrystalline Silicon for Integrated
    Circuits and Displays*, 2nd ed., Kluwer Academic, 1998.
    <https://doi.org/10.1007/978-1-4615-5577-3>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^lu-1981]: N. C.-C. Lu, L. Gerzberg, C.-Y. Lu and J. D. Meindl,
    "Modeling and optimization of monolithic polycrystalline silicon
    resistors", *IEEE Transactions on Electron Devices* **28**(7),
    818–830 (1981). <https://doi.org/10.1109/T-ED.1981.20437>
[^lane-1989]: W. A. Lane and G. T. Wrixon, "The design of thin-film
    polysilicon resistors for analog IC applications", *IEEE
    Transactions on Electron Devices* **36**(4), 738–744 (1989).
    <https://doi.org/10.1109/16.22479>
[^seto-1975]: J. Y. W. Seto, "The electrical properties of
    polycrystalline silicon films", *Journal of Applied Physics*
    **46**(12), 5247–5254 (1975). <https://doi.org/10.1063/1.321593>
[^mandurah-1981]: M. M. Mandurah, K. C. Saraswat and T. I. Kamins, "A
    model for conduction in polycrystalline silicon — Part I: Theory",
    *IEEE Transactions on Electron Devices* **28**(10), 1163–1171
    (1981). <https://doi.org/10.1109/T-ED.1981.20504>
[^liu-2001]: W.-C. Liu, K.-B. Thei, H.-M. Chuang, K.-W. Lin, C.-C. Cheng,
    Y.-S. Ho, C.-W. Su, S.-C. Wong, C.-H. Lin and C. H. Diaz,
    "Characterization of polysilicon resistors in sub-0.25 μm CMOS ULSI
    applications", *IEEE Electron Device Letters* **22**(7), 318–320
    (2001). <https://doi.org/10.1109/55.930677>
[^odwyer-2009]: T. G. O'Dwyer and M. P. Kennedy, "Comparison of
    resistor matching performance of polysilicon films in a CMOS
    process", *2009 Ph.D. Research in Microelectronics and Electronics
    (PRIME)*, pp. 80–83. <https://doi.org/10.1109/RME.2009.5201322>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^wright-2010]: S. W. Wright, C. P. Judge, M. J. Lee, D. F. Bowers,
    M. Dunbar and C. D. Wilson, "High sheet resistance, low temperature
    coefficient of resistance resistor films for integrated circuits",
    *Journal of Vacuum Science & Technology B* **28**(4), 834–840
    (2010). <https://doi.org/10.1116/1.3466531>
[^orvek-1985]: K. J. Orvek and C. Huffman, "Carbonized layer formation
    in ion implanted photoresist masks", *Nuclear Instruments and
    Methods in Physics Research B* **7–8**, 501–506 (1985).
    <https://doi.org/10.1016/0168-583X(85)90421-5>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
