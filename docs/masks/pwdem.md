(mask-pwdem)=
# PWDEM — P-Well Drain Extended

The P-well drain-extended mask is the {term}`reticle` of the last
lithography of SKY130's well and channel module: on the
{ref}`PWDEM <step-030>` page's reading, the resist printed through it at
step 30 is opened over the `pwde` regions of the 20 V devices, the two
implants {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>` put a
lighter, purpose-built P-well into them — inside the areas from which
{ref}`PWBM <step-026>` kept the standard P-well — and the resist is
stripped at {ref}`PWDEIS <step-033>`. Like `PWBM`, it is a mask whose
public record is sparse: `masks.csv` does not mark it as used, the
process-steps sheet records a plate for it on one MPW run only, and no
rendered die of any run draws its layer. This page gathers what public
sources say about the mask itself — its PDK entry and layer, the plate
the process-steps sheet records, what the public renders show, the
lithography it needs and the rules that constrain it — and reports the
gaps without drawing conclusions from them. How the step is performed is
on the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.

| | PWDEM — P-Well Drain Extended |
|---|---|
| Mask step | {ref}`PWDEM <step-030>`, step 30 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "P-Well Drain Extended", `PWDEM`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | none[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `pwde` drawing 124:20, "Regions to receive p-well drain-extended implants"[^pdk-06] |
| Minimum CD, feature / space | `PWDEMCD` 0.84 / `PWDEMCDSP` 1.27[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened over `pwde`, which with a positive resist would make the plate clear over `pwde` and opaque elsewhere (inference). |
| Exposure class | i-line, an inference on the step page from the micrometre-scale features of the drain-extended devices; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | MPW-6[^steps-sheet] |
| Plate no. | `026`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 0 on every run[^mask-renders] |
| Steps that use the pattern | 4 steps; see {ref}`Steps that use this mask <mask-pwdem-steps>` |

## What the mask defines

`gds_layers.csv` describes the drawn layer `pwde` as "Regions to
receive p-well drain-extended implants", and the rule set's function
line reads, as published, "Defines Pwdem (FIXME)".[^pdk-06][^pdk-periph]
The rules give no values but fix where the layer may be: `pwde` "must
be enclosed by UHVI" (pwdem.4), the 20 V node identifier; inside UHVI it
"must be enclosed by deep nwell" (pwdem.5); and it has a minimum
enclosure by `pwbm` (pwdem.3).[^pdk-periph] The
{ref}`PWDEM <step-030>` page reads these together with the `pwbm`
description: the standard P-well is kept out of the 20 V device area at
{ref}`PWBM <step-026>`, and `PWDEM` puts a different, lighter P-well
back into part of it, inside a deep-N-well tub. The PDK's high-voltage
methodology says that its very-high-voltage devices, the 16 V class,
"need to be designed with drain extentions (DE) fabricated by lightly
doped Nwells" and P-wells;[^pdk-hv] it does not describe the 20 V
devices, and the step page applies the statement to them by analogy.

Which device the lighter P-well serves is an open question on the step
pages, which read it as the drift region of the 20 V PMOS and, less
certainly, the body of the 20 V NMOS. The PDK's mask generation table,
Table F2b, marks the `PWDEM` column `C` ("CREATED") in one of its 80
device rows, "UHV pmos 5/20V DE", and `-` in every other row, including
the four 20 V NMOS rows (plain, isolated, native and isolated
native).[^pdk-06] On the table, then, the plate is created for the 20 V
PMOS only, which supports the PMOS reading and not the NMOS one (our
reading of the table; it does not say which region of the device the
layer forms). The SKY130 {term}`test tile`'s pad documentation names
its 20 V PMOS structures `p20vhv1`, with cell names such as
`s8tet_s_hvp_pwde_stdnw_sti_1p5_2f_60um_IP_LVS`, and gives them an
"N-body" pin;[^raw-data-testtile-pads] the pad list does not explain the
names, and a name is not evidence of the process. The PDK's 20 V PMOS
page, model `sky130_fd_pr__pfet_20v0`, lists operating voltages of
V_DS = 0 to −22 V, and its details text repeats the NMOS wording, "The
20V NMOS FET has similar construction to the 11V/16V NMOS FET, with
several differences", among them a "Longer drift region".[^pdk-07]

A p-type drift region for a high-voltage PMOS has a long history:
Ludikhuize's 1982 lateral DMOS used a p− top layer that "can be used in
the extended drain of a 280 V PMOST",[^ludikhuize-1982] and Mei et al.
built both N- and P-channel extended-drain RESURF devices, rated 30 V,
in a twin-well CMOS process.[^mei-1994] Appels and Vaes introduced the
RESURF principle,[^appels-1979] and Mitros et al. added drain-extended
transistors to a 0.18 µm logic process.[^mitros-2001]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has no mask-level (`c…`) layer for this mask; the drawn
layer is `pwde` at 124:20.[^pdk-06] `masks.csv` lists "P-Well Drain
Extended, PWDEM" with the `Used in SKY130` field blank,[^pdk-05] which the
{ref}`PWDEM <step-030>` page treats as a documentation inconsistency,
since the layer and its rules exist. Table 2 of *Criteria & Assumptions*
gives `PWDEMCD` 0.84 and `PWDEMCDSP` 1.27, the same values as the
N-well and P-well block rows,[^pdk-03] while the `pwdem` rules
themselves give "N/A" for every value;[^pdk-periph] the PDK does not say
which of the two applies to the plate. The PDK's *Error Messages* page,
which describes "many of the automated DRC rules that are checked by
SkyWater as part of the acceptance criteria for GDS data", gives one
value, under the rule name `pwde.6`: "1.00 min. enclosure of pwde_uhvi
by dnwell_uhvi".[^pdk-errors] No periphery rule outside the
`pwdem` set, and no criterion of *Criteria & Assumptions* besides Table
2's row, names `pwde` or `PWDEM`,[^pdk-periph][^pdk-03] and the PDK
publishes no operation from
`pwde` to the plate.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `PWDEM` the site renders layer 124:20 (`pwde`)
alone, with no Boolean expression, no fill layer and no mask-level
layer, with the note "pwde drawing", and records the mask as not used in
SKY130.[^mask-renders] The choice of layer agrees with the index's
pairing, but both start from the same public files, so the agreement is
not independent confirmation; it is one public derivation from the
drawn data, not SkyWater's mask-generation recipe.

No rendered die on any of the eight runs draws `pwde`: every image is
empty, including those of MPW-6, the run for which the sheet records a
plate.[^mask-renders][^steps-sheet] The site says that "Empty images are
real results - several masks are used by no project on a given
shuttle", and states the limits of its images: "These are renders of
*drawn* data, not photomask artwork: reticle pitch, 4x reduction,
mirroring and the frame features the fab adds are not
modelled."[^mask-renders] The renders therefore cannot show what the
MPW-6 plate carries, since they leave out whatever the fab adds. The
site's metadata carries no plate ID, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `PWDEM` plate
as existing on MPW-6 only, with the plate number `026`, and has no mark
or plate ID for the other seven runs and no "Info" note.[^steps-sheet]
The plate ID below is the sheet's; the reticle set is the heading of the
run's columns in the tab ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | none recorded |
| MPW-2 | `5CS8007AC` | none recorded |
| MPW-3 | `5CS8008AC` | none recorded |
| MPW-4 | `5CS8018AC` | none recorded |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA026A` |
| MPW-7 | `5CS8016AC` | none recorded |
| MPW-8 | `5CS8017AC` | none recorded |

* **Partial record.** The sheet records a `PWDEM` plate for MPW-6 only
  and does not say why the plates for the two P-well masks are recorded
  for only some runs; MPW-8 has a `PWBM` plate but no `PWDEM` plate
  ({ref}`masks-mpw-runs`).[^steps-sheet] This page reports what is
  recorded and does not conclude that the mask was absent from the other
  seven runs: the gap may be in the record rather than in the runs.
* **No drawn shapes.** No rendered die on any run draws `pwde`, so the
  renders neither show use of the mask on MPW-6 nor its absence
  elsewhere, and this page does not read the recorded plate as evidence
  that any project on MPW-6 used the 20 V
  devices.[^mask-renders][^steps-sheet]
* **Plate number.** `026` follows `024` for `PWBM`, as step 30 follows
  step 26, but the numbers do not follow process order elsewhere and the
  sheet does not say what they encode, so no process position is read
  from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `PWDEM`,[^steps-sheet] and no public source gives this
  plate's blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]

## Lithography and pattern transfer

**Exposure class.** The {ref}`PWDEM <step-030>` page reads the layer's
features as micrometre-scale, with overlay requirements set by the
drift-region length rather than by a sub-micrometre CD, and infers an
i-line level; the {ref}`i-line stepper <machine-i-line-stepper>` page
lists it there. SkyWater lists "ASML I-line stepper" and "ASML I-line
scanner" among its tools but assigns no layer to them.[^skw-01] Taking
Table 2's 0.84 µm as the smallest feature, Wong et al.'s threshold for a
rising mask error factor, 0.5 λ/NA for lines and spaces,[^wong-1998] is
about 0.38 µm at 365 nm and NA 0.48 (our arithmetic), well below it.

**Resist.** The resist must stop the drain-extension boron wherever the
plate leaves it. The {ref}`PWDEM <step-030>` page reads a 2 µm-class
implant resist like that of `PWBM`, on the grounds that a drift well is
lighter but not necessarily shallower than the main well. An IBM
retrograde-well patent uses resist "typically 1800–2500 nm in
thickness" for its 150 keV and 45 keV P-well boron, while its 550 keV
boron goes through a 200 nm polysilicon mask;[^pat-well-ibm] the ion range that sets the thickness is what
SRIM computes,[^ziegler-2010] and Lee et al. measured the outgassing of
thick resists under MeV implantation.[^lee-1996] SkyWater's resist and
its thickness are not public. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** Nothing is etched through this resist. On the
step pages' readings the pattern is transferred into the silicon as
dopant by {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>`, a
two-energy boron pair on their pages' reading, on the
{ref}`medium-current implanter <machine-medium-current-implanter>` or
{ref}`high-energy implanter <machine-high-energy-implanter>` class, and
the resist is removed at {ref}`PWDEIS <step-033>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes, before the
{ref}`RTAI <step-034>` anneal. A Texas Instruments drain-extension patent
gives boron "at doses of 2×10¹² cm² to 7×10¹³ cm² at energies of about
40 keV" for its p-type well;[^pat-demos-ti] the SKY130 conditions are not
public.

**Overlay.** The {ref}`PWDEM <step-030>` page reads the drift-well edge
against the trench and, later, the poly as reliability-critical, citing
the PDK's instruction that "Under no circumstances the poly/extended
drain overlap and field oxide length should be changed" (said of the
16 V devices).[^pdk-hv] The PDK publishes no value for the placement of
`pwde` against those layers (the `pwdem` rules are "N/A");[^pdk-periph]
its one published `pwde` value, in the Error Messages page, is the
1.00 enclosure by deep N-well.[^pdk-errors] Ludikhuize reviews RESURF
technology, including breakdown and on-resistance.[^ludikhuize-2000]

(mask-pwdem-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `PWDEM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`PWDEM <step-030>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PWDEIS <step-033>`

* {ref}`PWDEM <step-030>` — coats, exposes and develops the thick
  resist.
* {ref}`PWDEI1 <step-031>` — the first drain-extended P-well implant
  into the `pwde` openings.
* {ref}`PWDEI2 <step-032>` — the second implant through the same resist,
  a second energy on its page's reading.
* {ref}`PWDEIS <step-033>` — strips the resist and cleans the wafer for
  the anneal.

On its step page's reading, the next step, {ref}`RTAI <step-034>`,
anneals every implant of the well and channel module in an inert
ambient, with the resist already gone. The next mask step is
{ref}`TUNM <step-035>`. There is no exception to the rule for this mask.

## Design rules and critical dimensions

The `pwdem` rules of the periphery rules, which give no values
("N/A").[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| pwdem.1 | "Min width of pwdem.dg" | N/A |
| pwdem.2 | "Min spacing between two pwdem.dg inside UHVI on same net" | N/A |
| pwdem.3 | "Min enclosure of pwdem:dg by pwbm.dg inside UHVI" | N/A |
| pwdem.4 | "pwdem.dg must be enclosed by UHVI" | N/A |
| pwdem.5 | "pwdem.dg inside UHVI must be enclosed by deep nwell" | N/A |
| pwdem.6 | "Min enclosure of pwdem:dg by deep nwell inside UHVI" | N/A |

The Error Messages page gives a value for the last of them, under the
name `pwde.6`: "1.00 min. enclosure of pwde_uhvi by
dnwell_uhvi".[^pdk-errors] Table 2 of *Criteria & Assumptions* gives
`PWDEMCD` 0.84 and `PWDEMCDSP` 1.27, under the layer name "P-Well Drain
Extended".[^pdk-03]
The published drain-extended PMOS rules (`depmos`) are headed "Defines
rules for the 16V Drain extended NMOS devices" and place the drain in an
N-well hole — for example "Min enclosure of de_pFet_drain by nwell hole"
(depmos.10), 0.860 µm — without naming `pwde`;[^pdk-periph] we read them
as rules for the 16 V PMOS, not the 20 V device that Table F2b ties to
this mask (inference from the rule wording). The uhvi rules require that
"UHVI must enclose dnwell" (uhvi.6.-), the tub that pwdem.5 puts the
layer in.[^pdk-periph] For the plate, then, the PDK publishes Table 2's
pair and the 1.00 enclosure by deep N-well; it gives no minimum width or
spacing for `pwde` itself.

## Related pages

* {ref}`PWDEM <step-030>`, {ref}`PWDEI1 <step-031>`,
  {ref}`PWDEI2 <step-032>` and {ref}`PWDEIS <step-033>` — the mask step,
  the two implants and the strip.
* {ref}`mask-pwbm` — the P-well block mask whose regions this mask
  partly re-dopes.
* {ref}`mask-dnm` — the deep N-well mask whose tubs enclose `pwde`.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the partial plate record of the two P-well masks.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` — an implant class that uses
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "P-Well Drain Extended,
  PWDEM" with the `Used in SKY130` field blank.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `pwde` and the
  `PWDEM` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `PWDEMCD`/`PWDEMCDSP`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `pwdem` rules, the `depmos` and
  `uhvi` rules.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `pwde.6`
  value.[^pdk-errors]
* SkyWater PDK, *High Voltage Methodology* — drain extensions of the
  16 V devices made of lightly doped wells.[^pdk-hv]
* SkyWater PDK, *Device Details* — the 20 V PMOS.[^pdk-07]
* SkyWater PDK Authors, test-tile pad documentation — the 20 V PMOS
  structures and their cell names.[^raw-data-testtile-pads]
* *S8 / SKY130 Process Steps* sheet — the step and the `PWDEM` plate of
  MPW-6.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the empty `PWDEM` renders, their
  layer and note.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]

### High-level understanding

* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implant masking by resist.[^txt-02]
* Baliga, *Fundamentals of Power Semiconductor Devices* — breakdown and
  drift-region doping.[^baliga-2008]

### Deep dive

* Ludikhuize, IEDM 1982 — a p− layer in the extended drain of a
  high-voltage PMOS.[^ludikhuize-1982]
* Mei et al., VLSI Symposium 1994 — N- and P-channel extended-drain
  RESURF devices in one CMOS process.[^mei-1994]
* Appels and Vaes, IEDM 1979 — the RESURF principle.[^appels-1979]
* Ludikhuize, ISPSD 2000 — a review of RESURF technology, including
  breakdown and on-resistance.[^ludikhuize-2000]
* Mitros et al., *IEEE TED* 2001 — drain-extended MOS transistors in a
  0.18 µm logic process.[^mitros-2001]
* Efland, Tsai and Pendharkar, IEDM 1998 — a review of LDMOS structures
  in BiCMOS power technologies.[^efland-1998]
* Mitros (Texas Instruments), US 6,660,603 — drain extensions made from
  lightly doped wells, with implant conditions.[^pat-demos-ti]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde wells
  with resist thickness and boron energies.[^pat-well-ibm]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation.[^lee-1996]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]

## Open questions

* `masks.csv` leaves the `Used in SKY130` field blank for `PWDEM`
  although the layer and its rules exist;[^pdk-05][^pdk-06][^pdk-periph]
  the PDK does not explain the blank.
* Whether `pwde` forms the drift region of the 20 V PMOS, as Table F2b's
  single `C` mark supports, or also the body of the 20 V NMOS, as the
  step pages consider, is not stated.[^pdk-06]
* The sheet records a plate for MPW-6 only and does not say
  why;[^steps-sheet] whether the other runs had one is not public, and
  no rendered die draws `pwde`, so the renders cannot
  tell.[^mask-renders]
* The periphery rules publish no values for `pwdem`; beyond Table 2's
  pair and the Error Messages page's 1.00 enclosure by deep N-well, the
  PDK does not state the plate's minimum features or placement
  margins.[^pdk-periph][^pdk-03][^pdk-errors]
* The plate's tone, blank, absorber and magnification, the resist and
  its thickness, and the exposure tool are not public.
* What the plate number `026` encodes is not stated.[^steps-sheet]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists" and "Plate ID" columns per run)
    and "Sheet4" (mask types), retrieved 2026-09-13.
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (all tables),
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-hv]: SkyWater PDK Authors, *High Voltage Methodology*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/hv.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (20V PMOS FET),
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_PWDEM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^baliga-2008]: B. J. Baliga, *Fundamentals of Power Semiconductor
    Devices*, Springer, 2008, ISBN 978-0-387-47313-0.
    <https://doi.org/10.1007/978-0-387-47314-7>
[^ludikhuize-1982]: A. W. Ludikhuize, "High-voltage DMOS and PMOS in
    analog IC's", *1982 International Electron Devices Meeting*,
    pp. 81–84. <https://doi.org/10.1109/IEDM.1982.190218>
[^mei-1994]: P. C. Mei, K. Fujikura, T. Fawano and S. Malhi, "A high
    performance 30 V extended drain RESURF CMOS device for VLSI
    intelligent power applications", *Proceedings of 1994 VLSI
    Technology Symposium*, pp. 81–82.
    <https://doi.org/10.1109/VLSIT.1994.324367>
[^appels-1979]: J. A. Appels and H. M. J. Vaes, "High voltage thin layer
    devices (RESURF devices)", *1979 International Electron Devices
    Meeting*, pp. 238–241. <https://doi.org/10.1109/IEDM.1979.189589>
[^ludikhuize-2000]: A. W. Ludikhuize, "A review of RESURF technology",
    *12th International Symposium on Power Semiconductor Devices & ICs*
    (2000), pp. 11–18. <https://doi.org/10.1109/ISPSD.2000.856763>
[^mitros-2001]: J. C. Mitros, C.-Y. Tsai, H. Shichijo, M. Kunz,
    A. Morton, D. Goodpaster, D. Mosher and T. R. Efland, "High-voltage
    drain extended MOS transistors for 0.18-µm logic CMOS process", *IEEE
    Transactions on Electron Devices* **48**(8), 1751–1755 (2001).
    <https://doi.org/10.1109/16.936703>
[^efland-1998]: T. R. Efland, C.-Y. Tsai and S. Pendharkar, "Lateral
    thinking about power devices (LDMOS)", *IEDM 1998 Technical Digest*,
    pp. 679–682. <https://doi.org/10.1109/IEDM.1998.746447>
[^pat-demos-ti]: J. C. Mitros (Texas Instruments), *Higher voltage drain
    extended MOS transistors with self-aligned channel and drain
    extensions*, US 6,660,603 B2, granted 2003-12-09.
    <https://patents.google.com/patent/US6660603B2/en>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23. <https://patents.google.com/patent/US6667205B2/en>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
