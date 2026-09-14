(mask-ntm)=
# NTM — N-tip Implant

The N-tip mask is the {term}`reticle` that decides which transistors
receive SKY130's standard n-type {term}`extension`: on the
{ref}`NTM <step-064>` page's reading, the resist printed through it at
step 64 is opened over the 1.8 V NMOS transistors, the arsenic tip
{ref}`ASTI <step-065>` and the boron {term}`halo` {ref}`BHI <step-066>`
pass through the same openings, and the resist is stripped at
{ref}`ASTIS <step-067>`. It is the first of three tip masks and an
implant {term}`block mask` whose openings select transistors rather
than place junction edges, since the gate the implants self-align to is
already etched. What sets it apart is that no designer draws it: the
PDK has no drawn `ntm` layer, and what it does publish about the created
data — its DRC checks and its mask generation table — describes, on our
reading, the regions that the standard tip must not reach. This page
gathers what public sources say about the mask itself — its PDK entry
and layers, the plates the process-steps sheet records for the MPW runs,
what the public renders of those runs show, the lithography it needs and
the rules that constrain it. How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.

| | NTM — N-tip Implant |
|---|---|
| Mask step | {ref}`NTM <step-064>`, step 64 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "N-tip Implant", `NTM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cntm` mask 27:0, "N-tip implant mask"; drawing 26:20, mask add 26:21, mask drop 26:22, without descriptions[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | none: there is no drawn `ntm` layer; the masks index pairs the mask with the device layers it is derived from (inference)[^pdk-06] |
| Minimum CD, feature / space | `NTMCD` 0.84 / `NTMCDSP` 0.7[^pdk-03] |
| Polarity and tone | Not published. The step page reads the resist as opened over the transistors that receive the tip; on our reading the PDK's `cntm` checks, Table F2b and the renders' expression describe the created data as the regions that do not, so the resist would remain where the data are drawn (inference); the plate's tone is not public. |
| Exposure class | i-line, an inference on the step page from the size of tip-mask features; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `255`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 4 steps; see {ref}`Steps that use this mask <mask-ntm-steps>` |

## What the mask defines

`masks.csv` lists "N-tip Implant, NTM" as used in SKY130, and
`gds_layers.csv` describes its mask-level layer `cntm` as "N-tip implant
mask"; unlike the two tip masks after it, it has no drawn layer, where
`hvntm` is "High voltage N-tip implant" and `ldntm` "N-tip implant on
SONOS devices".[^pdk-05][^pdk-06] The {ref}`NTM <step-064>` page reads
the mask as selecting the standard 1.8 V NMOS for a shallow arsenic tip
and its halo, the {ref}`HVNTM <step-068>` tip as the 5 V NMOS's and the
{ref}`LDNTM <step-071>` tip as the {term}`SONOS` transistors'. The PDK
gives the tip's species and angle, not its dose: Table 3b of *Criteria &
Assumptions* has a row "N Tip (As)" with a vertical space of 0.01 µm
(`LDNTIP`), and Table 3f an "Angle for tip implant" of 7° (`TipAng`),
beside 0° for "High current" and 40° with a 23° twist for the HV
tip.[^pdk-03] Ogura et al. introduced the lightly doped drain between
channel and drain,[^ogura-1980] Codella and Ogura added the
halo,[^codella-1985] and Thompson et al. set out how extensions must
scale with gate length,[^thompson-1998] which is the reason the step
page gives for a tip of its own for the thin-oxide devices.

The PDK's mask generation table, Table F2b, reads the other way round.
It marks the `NTM` column `C` ("CREATED") in 43 of its 80 device rows:
every 1.8 V PMOS row (standard, low-Vt, high-Vt and core), the three
varactors, the four SONOS rows, the p-diffusion, HV n- and p-diffusion
and p+ poly resistors, every 110 Å row except the five UHV 5/20 V
drain-extended rows, twelve diode rows, the parasitic PNP and the three
HV ESD transistors.[^pdk-06] It marks `-`,
"Layer not created for the device", in 19 rows, among them the 1.8 V
NMOS, the low-Vt NMOS, the `nmos_core` rows, the n-diffusion resistor,
the `nDiode`, the LV ESD NMOS and the five UHV 5/20 V drain-extended
rows.[^pdk-06] On our reading of the rows, the created shapes lie over
the devices that must not receive the standard tip, and the devices that
receive it are the ones left out; the table does not say what the created
shapes do, and it does not explain why the UHV rows are left out as
well. Gardner, Hause and Fulford patented separate LDD and source/drain
implant steps for different transistors on one chip,[^pat-multi-ldd-amd]
the arrangement of which the three tip masks are one instance.

What the mask does not define is the tip's edge. On the step pages'
readings the implants through the openings are self-aligned to the
{ref}`P1M <mask-p1m>` gate pattern, so the resist only chooses which
transistors are implanted; its edges matter where they come close enough
to a gate to shadow a tilted beam (below).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cntm` a `mask` purpose at 27:0 and `drawing`
26:20, `mask add` 26:21 and `mask drop` 26:22 on a different layer
number, the three without descriptions; there is no `ntm` drawing
layer.[^pdk-06] The {ref}`NTM <step-064>` page infers from that absence
that the reticle is derived by Boolean operations from the drawn device
layers, with the add and drop purposes for manual corrections; the masks
index marks the pairing as an inference. Rule x.9 allows "Shapes on
maskAdd or maskDrop layers ("serifs")" in the core only, and x.15a
confines "Drawn compatible, mask, and waffle-drop layers" to test
modules, seal ring and frame, with an exception that names only
"FOM/P1M/Metal waffle drop" (flag P).[^pdk-periph] The PDK's periphery
rules have no `ntm` or `cntm` rule set.[^pdk-periph]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", does name the created layer. It lists `cntm.1`,
"0.84 min. width of CLNTM", `cntm.2`, "0.7 min. spacing/notch of CLNTM",
and three enclosure checks: `cntm.3`, "nwell must be enclosed by CLNTM";
`cntm.4a`, "hvitmp must be enclosed by CLNTM"; and `cntm.7`, "ldntm must
be enclosed by CLNTM", each with a companion "0 min. enclosure of […] by
CLNTM".[^pdk-errors] It also has two `cntm.nikon` checks, "NTMmk in the
nikon cross has the wrong polarity" and "NTMmk is missing from the nikon
cross in the layout", the x.9 messages "NTMdrop must be enclosed by
COREID" and "NTMadd must be enclosed by COREID", and x.15a messages for
`cntm` and `NTMmk`.[^pdk-errors] The page defines neither `CLNTM` nor
`hvitmp`. We read `CLNTM` as the created `NTM` data and `hvitmp` as a
working layer derived from `hvi`, "High voltage (5.0V) thick oxide gate
regions" (inference from the names).[^pdk-06] On that reading the PDK
requires the created layer to cover N-well, the thick-oxide regions and
the SONOS tip layer — on the step pages' readings the PMOS, the 5 V
devices and the memory cells, none of which takes the standard tip —
consistent with the Table F2b
rows above. The checks state what the layer must cover, not the
operation that makes it, and the table and checks are both SkyWater's
documents, so their agreement is not independent (our reading).

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. `NTM` is one of the masks the site's README calls
"fab-derived" and evaluates "as a boolean expression over drawn layers":
on all eight runs the expression is `64:20 OR 11:44 OR (75:20 NOT 81:2)`,
which in the layer names of `gds_layers.csv` is `nwell` OR `ldntm` OR
(`hvi` NOT `areaid.ce`).[^mask-renders][^pdk-06] Its mask record lists
the drawn layers 64:20, 75:20 and 11:44 and the mask-level layer 27:0,
with the note "created over nwell, ldntm and hvi (outside areaid.ce; rpm
too in some flows) (cntm 26:20 is the fab's precomputed layer, not
drawn)".[^mask-renders] The expression has no `rpm` term, and the site
names no source for the note or for calling 26:20 a precomputed layer,
which `gds_layers.csv` lists only as the `cntm` drawing purpose without a
description.[^pdk-06] The expression and note are one public derivation
from the drawn data, not SkyWater's mask-generation recipe; the
{ref}`masks index <masks-derivations>` finds the expression consistent in
kind with its own reading of a mask derived from the device layers.

Its three terms are the three layers of the Error Messages page's
enclosure checks, if `hvitmp` is derived from `hvi` (our comparison, on
the reading above).[^mask-renders][^pdk-errors] Since the site names no
source, that agreement may only mean that both start from the same
public PDK pages, and neither the site nor the PDK says what the
implants through the openings do.

All 40 rendered dies of every run carry shapes, but that is not 40
designs that use the standard tip: because the expression renders all of
`nwell`, the counts follow N-well use. Every die carries at least 1 712
shapes; the minimum on each run lies between 1 712 (MPW-6) and 2 359
(MPW-1); and on each run 5 to 18 of the 40 dies carry a count that
another die of the run shares — 2 203 on eight dies of MPW-3 and 2 140
on nine dies of MPW-8.[^mask-renders] We read the repeated counts as
shapes common to the dies rather than to the projects (inference); the
site does not say what they are. The site states the limits of its
images: "These are renders of *drawn* data, not photomask artwork:
reticle pitch, 4x reduction, mirroring and the frame features the fab
adds are not modelled."[^mask-renders] Its metadata carries no plate ID,
so a render is tied to a plate in the process-steps sheet only by the
acronym `NTM`, and the MPW-4 renders come from a different reticle set
from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `NTM` plate
as existing on all eight MPW runs, with the plate number `255` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA255A` |
| MPW-2 | `5CS8007AC` | `S8007AA255A` |
| MPW-3 | `5CS8008AC` | `S8008AA255A` |
| MPW-4 | `5CS8018AC` | `S8018AA255A` |
| MPW-5 | `5CS8011AC` | `S8011AA255A` |
| MPW-6 | `5CS8014AC` | `S8014AA255A` |
| MPW-7 | `5CS8016AC` | `S8016AA255A` |
| MPW-8 | `5CS8017AC` | `S8017AA255A` |

* **Plate number.** The sheet does not say what `255` encodes. It lies
  between `250` for `NSDM` (step 85) and `257` for `HVNTM` (step 68),
  and below `260` for `PSDM` (step 81), while `LDNTM` (step 71) is
  `238`, so the numbers do not follow process order and no process
  position is read from it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `NTM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`NTM <step-064>` page takes the 0.7 µm
width and spacing of the `hvntm` rules as the scale of tip-mask
features, puts them at {math}`k_1 = 0.7 \times 0.6 / 0.365 \approx 1.2`
on an i-line lens, quotes ASML's statement that older exposure tools
"migrate to the lithography of choice for less critical
layers",[^asml-30] and infers an i-line level; the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
Table 2 of *Criteria & Assumptions* gives the mask's own figures, 0.84
and 0.7 (`NTMCD`, `NTMCDSP`),[^pdk-03] and at the NA 0.48 low end of
ASML's PAS 5500/275D[^asml-pas5500-275d] the 0.7 µm space has
{math}`k_1 = 0.7 \times 0.48 / 0.365 \approx 0.92` (our arithmetic).
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" among its
tools but assigns no layer to them.[^skw-01]

**Mask errors.** Wong et al. found that the mask error factor "is unity
for large features, but increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space patterns";[^wong-1998]
at 365 nm and NA 0.48 that threshold is about 0.38 µm (our arithmetic),
about half the `NTM` minimum, so a CD error on the plate would be
expected to print at its own size (inference). The demands of this mask
fall on its placement and on its resist edges, not its CD.

**Resist.** Nothing is etched through this resist; it only has to stop
the arsenic tip and the boron halo wherever the plate leaves it. The step
page reads a positive i-line resist of about 1 µm, citing the PDK's
generic "Photoresist thickness" of 1.14 µm, as stopping keV implants with
a large margin; the PDK's other thickness entry, "Photoresist thickness
for HV Tip Implants", 0.3 in Table 4's column headed "Value (um)"
(`PrThickImplant`), names the HV tip, and the `NTM` step page does not
mention it.[^pdk-03] The ion range in resist that sets the margin is what SRIM
computes.[^ziegler-2010] On the step pages' typical values the tip is
the heavier of the two doses; Lukaszek, Reno and Bammi studied the
influence of photoresist on wafer charging during a high-current arsenic
implant,[^lukaszek-1996] Horsky resist outgassing in high-energy and
high-current implanters,[^horsky-1998] and
Ross et al. stabilised i-line implant resists with a flood electron beam,
reducing shrinkage and CD variation and eliminating
popping.[^ross-1996] SkyWater's resist, its thickness and any hardening
are not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Resist edges and shadowing.** A tilted implant is shadowed by a resist
wall as well as by the gate. Table 4 gives an "NTM shadowing" of 0.16
(`ntmShadowing`), a "Min width of tip implant opening" of 0.1
(`minTip_impW`) and a "pseudo-shadowing" of 0.045 (`pseudoShadowing`),
beside an "HVNTM shadowing" of 0.232, all in the column headed "Value
(um)".[^pdk-03] The PDK does not say which resist thickness the 0.16
assumes or what "pseudo-shadowing" is. The {ref}`BHI <step-066>` page
compares the 0.16 with 1.14 µm × tan 7° ≈ 0.14 µm and reads the
allowance as sized for the 7° tip; with the 0.3 µm film the same geometry
gives about 0.04 µm (our arithmetic). Chen et al. described ion-beam
shadowing of tilted drain implants by adjacent structures,[^chen-1995]
and Yoneda and Niwayama traced a drain-current asymmetry in 130 nm
MOSFETs to extension-implant shadowing from an implanter angle
error.[^yoneda-2002] Ions also scatter out of a resist edge, "altering
the threshold voltage of those devices", in the words of Hook et al.,
who model a thick well resist.[^hook-2003]

**Pattern transfer.** On the step pages' readings the pattern is
transferred into the silicon beside each selected gate as dopant, by
{ref}`ASTI <step-065>` on the
{ref}`medium-current <machine-medium-current-implanter>` or
{ref}`high-current implanter <machine-high-current-implanter>` class and
by {ref}`BHI <step-066>` on the medium-current class, and the resist is
removed at {ref}`ASTIS <step-067>` on the
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` and
{ref}`wet bench <machine-wet-bench>` classes. The PDK gives arsenic for
the tip ("N Tip (As)"); the energies, doses and the halo's species,
tilt and rotation are not public.[^pdk-03]

**Overlay.** The {ref}`NTM <step-064>` page reads the mask as aligned to
the poly pattern (an inference; the alignment tree is not public) and
the shadowing allowances as setting how far a resist edge must stand
from a gate; they are distances the data must keep, and on our reading
the plate's placement error adds to them. ASML specifies "≤ 40 nm"
single-machine overlay for the /275D stepper[^asml-pas5500-275d] (our
comparison; how SkyWater budgets the margin is not public).

(mask-ntm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `NTM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`NTM <step-064>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`ASTIS <step-067>`

* {ref}`NTM <step-064>` — coats, exposes and develops the resist over the
  etched gates.
* {ref}`ASTI <step-065>` — the arsenic tip implant through the resist
  windows, self-aligned to the gates.
* {ref}`BHI <step-066>` — the boron halo, which its page infers shares the
  `NTM` resist because the halo belongs to the same transistors as the
  tip.
* {ref}`ASTIS <step-067>` — strips the implanted resist and cleans the
  wafer.

The next step, {ref}`HVNTM <step-068>`, is itself the next mask step: on
its step page's reading it coats a thin resist for the high-voltage tip
on the surface cleaned at `ASTIS`. No step between `ASTIS` and it uses
the `NTM` resist, and there is no exception to the rule for this mask.
On the step pages' readings the tip and halo placed through this resist
are annealed with the other tips at {ref}`TIPRTAD <step-075>`.

## Design rules and critical dimensions

The periphery rules have no `ntm` or `cntm` rule set. The table gives the
mask-data rules x.7, x.9 and x.15a and, since on the readings above the
created data follow N-well and the thick-oxide regions, the width and
spacing rules of `nwell` and `hvi`; flag P means "Rule applies to
periphery only (outside areaid.ce). A corresponding core rule may or may
not exist." and NC "Rule not checked by DRC. It should be used as a
guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […]" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| nwell.1 | "Width of nwell" | 0.840 µm |
| nwell.2a | "Spacing between two n-wells" | 1.270 µm |
| hvi.1 | "Min width of Hvi" (P) | 0.600 µm |
| hvi.2a | "Min spacing of Hvi to Hvi" (P) | 0.700 µm |
| hvi.5 | "Min space between hvi and nwell (exclude coincident edges)" | 0.700 µm |

Table 2 of *Criteria & Assumptions* gives `NTMCD` 0.84 and `NTMCDSP`
0.7,[^pdk-03] and the Error Messages page checks the created layer at
the same pair (`cntm.1`, `cntm.2`).[^pdk-errors] The pair equals the
N-well width of nwell.1 and the `hvi` spacings of hvi.2a and
hvi.5,[^pdk-periph] which fits a created layer built from those layers
(our comparison; the PDK does not say so). The other criteria that name
the mask or its implant are Table 3b's "N Tip (As)" (0.01, `LDNTIP`),
Table 3f's 7° "Angle for tip implant", and Table 4's "NTM shadowing"
(0.16), "Min width of tip implant opening" (0.1) and "pseudo-shadowing"
(0.045); Table 4 also lists "Photoresist thickness for HV Tip Implants"
(0.3, `PrThickImplant`), "HVNTM shadowing" (0.232, `hvntmShadowing`) and
an "HVPTM shadowing" (0.089, `hvptmShadowing`) for a mask that
`masks.csv` does not list.[^pdk-03][^pdk-05] For the plate the published
figures are a 0.84 µm feature on a 0.7 µm space, and a minimum
tip-implant opening of 0.1.

## Related pages

* {ref}`NTM <step-064>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`
  and {ref}`ASTIS <step-067>` — the mask step, the tip and halo implants
  and the strip.
* {ref}`mask-hvntm` and {ref}`LDNTM <step-071>` — the two other tip
  masks of the module; {ref}`TIPRTAD <step-075>` — the anneal of all
  three tips.
* {ref}`mask-p1m` — the gate pattern the tips self-align to;
  {ref}`mask-hvtpm` — another mask the renders build from `nwell`.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the derivations the renders use.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-medium-current-implanter` and
  {ref}`machine-high-current-implanter` — the implant classes that use
  the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "N-tip Implant, NTM, X"
  and the absence of a P-tip mask.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — the `cntm`
  purposes, `hvi`, `ldntm`, `areaid.ce` and the `NTM` column of Table
  F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `NTMCD`/`NTMCDSP`, "N Tip
  (As)", the tip implant angle, the shadowing and tip-opening criteria
  and the photoresist thicknesses.[^pdk-03]
* SkyWater PDK, *Periphery rules* — x.7, x.9, x.15a, the `nwell` and
  `hvi` width and spacing rules and the flag legend.[^pdk-periph]
* SkyWater PDK, *Error Messages* page and `errors.csv` — the `cntm`
  checks on `CLNTM`, the x.9 and x.15a messages and the "nikon cross"
  checks.[^pdk-errors]
* *S8 / SKY130 Process Steps* sheet — the step, the `NTM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `NTM` expression, note and
  per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — NA range and single-machine overlay
  of an i-line stepper.[^asml-pas5500-275d]
* ASML, *Three decades of PAS 5500* — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wikipedia, *Short-channel effect* — why extensions and halos are
  needed.[^wiki-sce]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 3 — LDD, extension
  and halo engineering.[^txt-04]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — overlay budgets and
  non-critical-layer tool choice.[^levinson-2005]

### Deep dive

* Ogura et al. (IBM), *IEEE TED* 1980 — the lightly doped drain-source
  transistor, the ancestor of every tip implant.[^ogura-1980]
* Codella and Ogura (IBM), IEDM 1985 — the halo added to the LDD, the
  pairing this mask serves.[^codella-1985]
* Thompson et al. (Intel), VLSI 1998 — how extension depth and doping
  scale with gate length.[^thompson-1998]
* Gardner, Hause and Fulford (AMD), US 5,793,090 — separate LDD and
  source/drain implant steps for different transistors on one
  chip.[^pat-multi-ldd-amd]
* Chen et al., *Solid-State Electronics* 1995 — ion-beam shadowing of
  tilted drain implants by adjacent structures.[^chen-1995]
* Yoneda and Niwayama, IWJT 2002 — drain-current asymmetry at 130 nm from
  extension-implant shadowing.[^yoneda-2002]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge and
  the threshold shifts they cause.[^hook-2003]
* Lukaszek, Reno and Bammi, IIT 1996 — wafer charging through resist
  during high-current arsenic implants.[^lukaszek-1996]
* Horsky, IIT 1998 — resist outgassing in high-energy and high-current
  implanters.[^horsky-1998]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor and the
  size below which it rises.[^wong-1998]
* ITRS 2001, *Lithography* — mask magnification for the 130 nm
  generation.[^itrs-03]

## Open questions

* The operation that makes the `cntm` plate data, and what its drawing,
  add and drop purposes contribute, are not published. The Error Messages
  page gives only what the created layer must cover and does not define
  `CLNTM` or `hvitmp`;[^pdk-errors] the renders' expression matches those
  checks on our reading, and its note mentions an `rpm` term the
  expression does not have.[^mask-renders]
* That the created data mark the regions the tip must not reach, and so
  where the resist remains, is our reading of Table F2b and the `cntm`
  checks; the PDK does not state the plate's polarity, and why Table F2b
  leaves the UHV drain-extended rows out of the `NTM` column is not
  explained.[^pdk-06]
* The resist and its thickness, the thickness the 0.16 "NTM shadowing"
  assumes and the meaning of "pseudo-shadowing" are not
  public.[^pdk-03]
* How the PMOS extensions are formed is the step page's open question:
  `masks.csv` lists no P-tip mask, while Table 4 gives an "HVPTM
  shadowing".[^pdk-05][^pdk-03]
* The plate's tone, blank, absorber and magnification and the exposure
  tool are not public; the i-line reading rests on the feature sizes.
* What the plate number `255` encodes is not stated, and no public source
  lists the `NTM` plate of the original MPW-4 set
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 3b,
    3f and 4), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/04-physical.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_NTM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-14. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-pas5500-275d]: ASML, *PAS 5500/275D High Productivity i-Line
    Stepper*, refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021.
    <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-sce]: Wikipedia, *Short-channel effect*.
    <https://en.wikipedia.org/wiki/Short-channel_effect>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^codella-1985]: C. F. Codella and S. Ogura, "Halo doping effects in
    submicron DI-LDD device design", *IEDM 1985 Technical Digest*,
    pp. 230–233. <https://doi.org/10.1109/IEDM.1985.190938>
[^thompson-1998]: S. Thompson, P. Packan, T. Ghani, M. Stettler,
    M. Alavi, I. Post, S. Tyagi, S. Ahmed, S. Yang and M. Bohr,
    "Source/drain extension scaling for 0.1 μm and below channel length
    MOSFETs", *1998 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 132–133. <https://doi.org/10.1109/VLSIT.1998.689229>
[^pat-multi-ldd-amd]: M. I. Gardner, F. N. Hause and H. J. Fulford
    (Advanced Micro Devices), *Integrated circuit having multiple LDD
    and/or source/drain implant steps to enhance circuit performance*,
    US 5,793,090 A, granted 1998-08-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5793090>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^yoneda-2002]: K. Yoneda and M. Niwayama, "The drain current asymmetry
    of 130 nm MOSFETs due to extension implant shadowing originated by
    mechanical angle error in high current implanter", *Extended
    Abstracts of the Third International Workshop on Junction
    Technology (IWJT 2002)*, pp. 19–22.
    <https://doi.org/10.1109/IWJT.2002.1225190>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices* **50**(9),
    1946–1951 (2003). <https://doi.org/10.1109/TED.2003.815371>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic implant",
    *Proc. 11th International Conference on Ion Implantation Technology*
    (1996), pp. 89–92. <https://doi.org/10.1109/IIT.1996.586135>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy
    and high current ion implantation", *1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^ross-1996]: M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
    S. Y. Wong, "Photoresist stabilization for ion implant processing",
    *Proc. SPIE* **2724**, 632 (1996).
    <https://doi.org/10.1117/12.241862>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
