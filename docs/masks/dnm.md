(mask-dnm)=
# DNM — Deep N-Well

The deep N-well mask is the {term}`reticle` whose pattern decides where
SKY130's buried N-type layer goes: on this reference's reading, the
resist printed through it at the {ref}`DNM <step-007>` step is opened
over every region that is to receive the high-energy phosphorus implant
of {ref}`DNI <step-008>`, and stripped again at
{ref}`DNIS <step-009>`. It is an implant {term}`block mask` rather than
an etch mask, with the largest minimum feature of any front-end mask in
the PDK's minimum-CD table.[^pdk-03] This page gathers what public
sources say about the mask itself — its PDK entry and layers, the plates
the process-steps sheet records for the MPW runs, what the public
renders of those runs show, the lithography it needs and the rules that
constrain it. How the step is performed is on the step page; every mask
is indexed on the {ref}`masks index <masks-index>`.

| | DNM — Deep N-Well |
|---|---|
| Mask step | {ref}`DNM <step-007>`, step 7 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Deep N-Well", `DNM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cdnm` mask 48:0, "Deep nwell mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `dnwell` drawing 64:18, "Deep n-well region"[^pdk-06] |
| Minimum CD, feature / space | `DNMCD` 3 / `DNMCDSP` 6.3[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist is opened where `dnwell` is drawn, which with a positive resist would make the plate dark-field (inference). |
| Exposure class | i-line, with KrF as the alternative, on the step page's reading of the 3 µm rule; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `150`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 3 steps; see {ref}`Steps that use this mask <mask-dnm-steps>` |

## What the mask defines

The mask defines the lateral extent of the deep N-well: a buried N-type
plate that, closed at its edges by a ring of ordinary N-well, isolates
a P-well from the p-type substrate (the reading of the
{ref}`DNM <step-007>` page, from rules nwell.5 and nwell.6
below).[^pdk-periph] The periphery rules give the layer's function as
"Define deep nwell for isolating pwell and noise immunity".[^pdk-periph]
The PDK's device pages describe what the isolation is used for: the
1.8 V NMOS "can be made either with or without the DNW under the
p-well"; the 20 V isolated NMOS "has the same construction as the 20V
NMOS FET, but is built over a Deep N-well. This permits the p-well to
be isolated from the substrate and permit “high-side” usage (where the
PW body is held above ground)"; and "The NPN uses the deep n-well as
the collector".[^pdk-07] Rule dnwell.6 requires RF NMOS devices to be
enclosed by deep N-well.[^pdk-periph]

The PDK's mask generation table, Table F2b, marks the `DNM` column `C`
("CREATED") in 19 of its 80 device rows: the isolated P-well resistor,
the HV varactor, two SONOS FET rows, the 5/16 V drain-extended PMOS,
the five 5/20 V drain-extended device rows, eight diode rows (seven
named for the deep N-well, and the photodiode) and the parasitic
NPN.[^pdk-06] The 1.8 V NMOS row marks it `+`, "Layer allowed to
overlap", rather than `C`, which fits the device page's "with or
without" (our reading of the two tables together).[^pdk-06][^pdk-07]
The deep N-well is therefore a module that designers opt into rather
than a layer every die needs; the {ref}`DNM <step-007>` page leaves open
whether every wafer receives it.

What the mask does not define is also worth stating. The N-well ring
that closes the tub is printed by {ref}`NWM <step-017>`, and the P-well
inside it is set by the P-well implants that follow; on the step pages'
readings `DNM` only places the buried plate. Stolmeijer's 1986 twin-well
process, built with implants of up to 1 MeV, already included "an n-type
isolation well in a p-p+substrate and retrograde wells"; the abstract
does not describe the well's geometry.[^stolmeijer-1986]
Hong et al. describe a 0.22 µm triple-well CMOS process formed by
high-energy implantation,[^hong-1999] and Voldman's *Latchup* gives a
chapter to dual-well and triple-well CMOS as latch-up
solutions.[^voldman-2007]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has one mask-level layer for this mask, `cdnm` with
purpose `mask` at 48:0 ("Deep nwell mask"), and no `drawing`,
`mask add`, `mask drop` or `waffle drop` purpose for it; the drawn layer
is `dnwell` at 64:18, "Deep n-well region".[^pdk-06] The pairing of
`cdnm` with `dnwell` rests on those names and descriptions, as for every
mask on the {ref}`masks index <masks-index>`; the PDK publishes no
operation that turns the drawn layer into the mask.[^pdk-06] Rule
x.15a restricts where a designer may draw mask layers: "Drawn
compatible, mask, and waffle-drop layers are allowed only inside
areaid:mt (i.e., etest modules)", the seal ring or the frame, with the
exception that "FOM/P1M/Metal waffle drop are allowed inside the
die" (flag P, periphery only).[^pdk-periph] Since `DNM` is not among the
exceptions, a design inside the die draws `dnwell`, and the `cdnm` layer
is for test modules, seal ring and frame (our reading of x.15a, which
does not say what applies in the core).

Three criteria in two tables hint that the plate is not the drawn layer
copied unchanged, without saying how it differs. Table 4 of *Criteria &
Assumptions* gives a "Min spacing for created dnwell to pnp.dg (more
restrictive than dnwell.4 rule)" of 5 (`cdnwPnpSpc`), and Table 7 a
"spacing of p-well outside deep n-well to deep n-well mask edge" of
0.12 (`NWDNWENCL`) and a "p-well in deep n-well to p-sub" of 1.2
(`NWDNWOL`).[^pdk-03] "Created" is the word Table F2b uses for the
mask levels a device generates,[^pdk-06] and a "mask edge" distinct from
the drawn edge suggests a sizing between the two (inference); the PDK
gives neither the sizing nor the created shapes.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `DNM` the site renders layer 64:18 alone, with
no Boolean expression and no fill layer, on all eight runs, and its mask
record gives the mask-level layer 48:0 and the note "DNM = dnwell sized
by cdnm.3".[^mask-renders] The periphery rules contain no rule set for
`cdnm` and no rule of that name,[^pdk-periph] and the site gives no
source for the note. The render jobs list only the drawn layer, with no
sizing step, so, as the {ref}`masks index <masks-derivations>` reads
the site in general, the images are unsized drawn data. The note and
the choice of layer are one public derivation from the drawn data, not
SkyWater's mask-generation recipe.[^mask-renders]

All 40 rendered dies of every run carry `dnwell` shapes, but that is not
40 designs using the module: every die carries at least 423 shapes on
the layer, and on each run 24 to 36 of the 40 dies carry exactly 423,
424, 533 or 534.[^mask-renders] We read the repeated counts as shapes
common to the dies rather than to the projects (inference); the site
does not say what they are. The site
states the limits of all its images: "These are renders of *drawn*
data, not photomask artwork: reticle pitch, 4x reduction, mirroring and
the frame features the fab adds are not modelled."[^mask-renders] Its
metadata carries no plate ID, so a render is tied to a plate in the
process-steps sheet only by the acronym `DNM`, and for MPW-4 the
renders come from a different reticle set from the one whose plates the
sheet records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `DNM` plate
as existing on all eight MPW runs, with the plate number `150` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab, which
the renders site calls the run's reticle set
({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA150A` |
| MPW-2 | `5CS8007AC` | `S8007AA150A` |
| MPW-3 | `5CS8008AC` | `S8008AA150A` |
| MPW-4 | `5CS8018AC` | `S8018AA150A` |
| MPW-5 | `5CS8011AC` | `S8011AA150A` |
| MPW-6 | `5CS8014AC` | `S8014AA150A` |
| MPW-7 | `5CS8016AC` | `S8016AA150A` |
| MPW-8 | `5CS8017AC` | `S8017AA150A` |

* **Plate number.** `150` does not follow process order — `NWM`
  (step 17) is `010` and `FOM` (step 4) `020` — and the sheet does not
  say what the numbers encode, so no process position is read from
  it ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders site's MPW-4 images are from the layouts of the original set
  `5CS8010AC`, whose plates no public source lists
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `DNM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]

## Lithography and pattern transfer

**Exposure class.** The {ref}`DNM <step-007>` page reads the mask as an
i-line level with a KrF tool as the alternative, an inference from the
3 µm minimum width; the {ref}`i-line stepper <machine-i-line-stepper>`
and {ref}`KrF stepper <machine-duv-krf-stepper>` pages carry the same
assignment. SkyWater lists "ASML I-line stepper" and "ASML I-line
scanner" among its tools but assigns no layer to them.[^skw-01] The
geometry leaves a wide margin: an i-line stepper such as ASML's
PAS 5500/275D runs at NA 0.48–0.60,[^asml-pas5500-275d] at which a
3 µm feature has {math}`k_1 = 3.0 \times 0.48 / 0.365 \approx 3.9`
(our arithmetic).

**Mask errors.** Wong et al. found that the mask error factor — how much
a CD error on the plate is magnified on the wafer — "is unity for large
features, but increases rapidly when the critical dimension (CD) is
less than 0.5 (lambda) /NA for line-space patterns", and that
dark-field spaces are more sensitive than light-field lines.[^wong-1998]
At 365 nm and NA 0.48 that threshold is about 0.38 µm (our arithmetic),
an eighth of the `DNM` minimum, so a CD error on this plate would be
expected to print at its own size (inference). That puts the
demands of this mask on its resist, placement and cleanliness rather
than on its CD.

**Resist.** The implant must be stopped by resist wherever the plate is
opaque (on the positive-resist reading). A Zilog patent on masking for
MeV well implants says such resists "may need to be 3-4 μm or thicker"
and uses a minimum of 3.4 µm after stabilisation;[^pat-resist-zilog] the
ion range in resist that sets the thickness is what SRIM
computes.[^ziegler-2010] Thick resist under MeV ions outgasses: Lee et
al. measured the chamber-pressure rise and dose shift it causes, for
resists up to 4.5 µm thick,[^lee-1996] and Ross et al. stabilised three
i-line resists for implant with a flood electron beam, which reduced
post-implant shrinkage and CD variation and eliminated popping during
removal.[^ross-1996] Tsukamoto et al. review high-energy implantation
for ULSI.[^tsukamoto-1991]
The step pages read a thick i-line resist; SkyWater's resist, its
thickness and any stabilisation are not public. The PDK's generic
"Photoresist thickness" is 1.14 µm,[^pdk-03] which the step page does
not take as this level's resist. The consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** Nothing is etched through this resist. On the step
pages' readings the pattern is transferred into the silicon as dopant
by the {ref}`DNI <step-008>` implant, on the
{ref}`high-energy implanter <machine-high-energy-implanter>` class, and
the resist is removed at {ref}`DNIS <step-009>`. A deep N-well implant
of the same era uses phosphorus at about 0.6–1.6 MeV and
5×10¹²–1.5×10¹³ cm⁻² in a Hynix triple-well patent;[^pat-dnw-hynix] the
SKY130 conditions are not public.

**Overlay.** The {ref}`DNM <step-007>` page reads the mask as aligned to
the trenches etched at {ref}`STIE <step-006>`. The enclosures that
depend on its placement are large — 0.400 µm of N-well around the deep
N-well (nwell.5) and 1.030 µm of deep N-well around an N-well hole
(nwell.6)[^pdk-periph] — against the "≤ 40 nm" single-machine overlay
ASML specifies for the /275D stepper[^asml-pas5500-275d] (our
comparison; the enclosures must also absorb the lateral spread of the
implant, which is not published, so the overlay share of them is not
known).

(mask-dnm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `DNM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`DNM <step-007>`, {ref}`DNI <step-008>`, {ref}`DNIS <step-009>`

* {ref}`DNM <step-007>` — coats, exposes and develops the resist.
* {ref}`DNI <step-008>` — the high-energy phosphorus implant through the
  resist windows.
* {ref}`DNIS <step-009>` — strips the implanted resist before the liner
  oxidation.

On its step page's reading, the next step, {ref}`LINOX <step-010>`,
grows the thermal liner oxide in the isolation trenches, and no step
between it and the next mask step, {ref}`LVTNM <step-014>`, uses the `DNM` resist. There is no exception
to the rule for this mask. The N-well ring that completes the tub is a
separate mask, {ref}`NWM <step-017>`.

## Design rules and critical dimensions

The `dnwell` rules of the periphery rules, with the N-well rules that
refer to it; flag TC means "Rule not checked for cell name
“\*_tech_CD_top\*”".[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| dnwell.2 | "Min width of deep nwell" | 3.000 µm |
| dnwell.3 | "Min spacing between deep nwells. Rule exempt inside UHVI." | 6.300 µm |
| dnwell.3a–3d | Spacings inside UHVI | N/A |
| dnwell.4 | "Dnwell can not overlap pnp:dg" | — |
| dnwell.5 | "P+_diff can not straddle Dnwell" | — |
| dnwell.6 | "RF NMOS must be enclosed by deep nwell […]" | — |
| dnwell.7 | "Dnwell can not straddle areaid:substratecut" | — |
| nwell.5 | "Deep nwell must be enclosed by nwell by atleast... […]" (TC) | 0.400 µm |
| nwell.6 | "Min enclosure of nwell hole by deep nwell outside UHVI" (TC) | 1.030 µm |
| nwell.7 | "Min spacing between nwell and deep nwell on separate nets […]" (TC) | 4.500 µm |

Table 2 of *Criteria & Assumptions* repeats the width and space as
`DNMCD` 3 and `DNMCDSP` 6.3, and Table 4 gives a "Min spacing between
nwell and deep nwell on separate nets" of 6 (`nwellDnwellSpc`), noted
as "Taken from dnwell.3 from S4* TDR *N plus rounded up", beside the
4.500 µm of rule nwell.7.[^pdk-03][^pdk-periph] The PDK does not
reconcile the two values. Of the few `dnwell` values published, only
width and space constrain the plate's features; the rest constrain how
the plate is placed against other layers.

## Related pages

* {ref}`DNM <step-007>`, {ref}`DNI <step-008>` and
  {ref}`DNIS <step-009>` — the mask step, the implant and the strip.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-i-line-stepper` and {ref}`machine-duv-krf-stepper` — the
  exposure classes the step page names.
* {ref}`machine-high-energy-implanter` — the implant class that uses the
  pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-implant` — the mask
  step and implant categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Deep N-Well, DNM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `dnwell`
  64:18, `cdnm` 48:0 and the `DNM` column of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `DNMCD`/`DNMCDSP`, the
  created-deep-N-well and mask-edge criteria and the photoresist
  thickness.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `dnwell` and N-well rules,
  x.15a and the flag legend.[^pdk-periph]
* SkyWater PDK, *Device Details* — the deep N-well in the 1.8 V and
  20 V isolated NMOS and the NPN.[^pdk-07]
* *S8 / SKY130 Process Steps* sheet — the step, the `DNM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `DNM` renders, their layer
  and note, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the i-line exposure
  tools.[^skw-01]
* ASML, *PAS 5500/275D* data sheet — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]

### High-level understanding

* Wikipedia, *Photomask* — reticles, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Ion implantation* — masking, range and
  energy.[^wiki-implant]
* Wikipedia, *Photolithography* — i-line exposure.[^wiki-litho]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implant masking by resist.[^txt-02]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on photoresists,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor for lines
  and holes and the feature size below which it rises.[^wong-1998]
* Rizvi (ed.), *Handbook of Photomask Manufacturing Technology* — data
  preparation, mask writing and conventional optical
  masks.[^rizvi-2005]
* Buerger et al., *Proc. SPIE* 1999 — hierarchical mask data
  preparation and fracturing, the step between drawn layers and a
  mask writer.[^buerger-1999]
* Stolmeijer, *IEEE TED* 1986 — a twin-well CMOS process using implants
  of up to 1 MeV, with an N-type isolation well and retrograde
  wells.[^stolmeijer-1986]
* Hong et al., TENCON 1999 — triple-well CMOS at 0.22 µm by high-energy
  implantation.[^hong-1999]
* Voldman, *Latchup*, chapter 5 — dual-well and triple-well CMOS as
  process solutions to latch-up.[^voldman-2007]
* Chew et al., ESSDERC 2002 — what a deep N-well does for substrate
  noise and RF transistors.[^chew-2002]
* Oh (Hynix), US 6,806,133 — a contemporaneous triple-well recipe with
  MeV phosphorus energies and doses.[^pat-dnw-hynix]
* Buffat and Adams (Zilog), US 6,576,405 — resist thickness and aspect
  ratio for MeV well implant masks.[^pat-resist-zilog]
* Ross et al., *Proc. SPIE* 1996 — electron-beam stabilisation of i-line
  implant resists.[^ross-1996]
* Lee et al., IIT 1996 — thick-resist outgassing during MeV
  implantation and the dose shift it causes.[^lee-1996]
* Tsukamoto et al., *NIM B* 1991 — a review of high-energy
  implantation for ULSI.[^tsukamoto-1991]
* Ziegler, Ziegler and Biersack, *NIM B* 2010 — SRIM, for the ion range
  in resist.[^ziegler-2010]
* ITRS 2001, *Lithography* — mask magnification and the optical mask
  requirements of the 130 nm generation.[^itrs-03]

## Open questions

* The operation that makes the `cdnm` plate data from `dnwell` is not
  published; the "created dnwell" and "deep n-well mask edge" criteria
  suggest a sizing,[^pdk-03] and the renders site's note names a
  "cdnm.3" that the periphery rules do not contain.[^pdk-periph][^mask-renders]
* The plate's tone, blank, absorber and magnification, the resist and
  its thickness, and the exposure tool are not public; the i-line
  reading rests on the 3 µm rule.
* Table 4's 6 (`nwellDnwellSpc`) and rule nwell.7's 4.500 µm for the
  same spacing are not reconciled in the PDK.[^pdk-03][^pdk-periph]
* What the plate number `150` encodes is not stated, and no public
  source lists the `DNM` plate of the original MPW-4 set
  `5CS8010AC`.[^steps-sheet][^mask-renders]
* The renders do not say what the shapes common to most dies of a run
  are, so how many projects on each shuttle use a deep N-well is not
  shown.[^mask-renders]

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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4
    and 7), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_DNM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-13. Rendered from the public shuttle
    repositories under
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
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^rizvi-2005]: S. Rizvi (ed.), *Handbook of Photomask Manufacturing
    Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
    <https://doi.org/10.1201/9781420028782>
[^buerger-1999]: B. Buerger, U. Baetz, K.-D. Kunze and H. Wolf,
    "Hierarchical mask data preparation and special fracturing
    techniques in MGS", *Proc. SPIE* **3665**, 135 (1999).
    <https://doi.org/10.1117/12.346217>
[^stolmeijer-1986]: A. Stolmeijer, "A twin-well CMOS process employing
    high-energy ion implantation", *IEEE Transactions on Electron
    Devices* **33**(4), 450–457 (1986).
    <https://doi.org/10.1109/T-ED.1986.22511>
[^hong-1999]: S.-P. Hong, H.-S. Chun, J.-J. Kim, M.-G. Kang and
    H.-S. Oh, "Fabrication of 0.22 μm triple well CMOS devices by using
    high energy ion implantation", *Proc. IEEE Region 10 Conference
    (TENCON 99)*, vol. 2, pp. 1106–1108 (1999).
    <https://doi.org/10.1109/TENCON.1999.818617>
[^voldman-2007]: S. H. Voldman, "CMOS Latchup Process Features and
    Solutions – Dual-Well and Triple-Well CMOS", chapter 5 of *Latchup*,
    Wiley, 2007, pp. 257–299, ISBN 978-0-470-01642-8.
    <https://doi.org/10.1002/9780470516171.ch5>
[^chew-2002]: K. W. Chew et al., "Impact of Deep N-well Implantation on
    Substrate Noise Coupling and RF Transistor Performance for
    Systems-on-a-Chip Integration", *Proc. ESSDERC 2002*, pp. 251–254.
    <https://doi.org/10.1109/ESSDERC.2002.194917>
[^pat-dnw-hynix]: J.-G. Oh (Hynix Semiconductor), *Method for fabricating
    semiconductor device with triple well structure*, US 6,806,133 B2,
    granted 2004-10-19. <https://patents.google.com/patent/US6806133B2/en>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^ross-1996]: M. F. Ross, W. R. Livesay, V. Starov, K. Ostrowski and
    S. Y. Wong, "Photoresist stabilization for ion implant processing",
    *Proc. SPIE* **2724**, 632 (1996).
    <https://doi.org/10.1117/12.241862>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^tsukamoto-1991]: K. Tsukamoto, S. Komori, T. Kuroi and Y. Akasaka,
    "High-energy ion implantation for ULSI", *Nuclear Instruments and
    Methods in Physics Research B* **59–60**, 584–591 (1991).
    <https://doi.org/10.1016/0168-583X(91)95283-J>
[^ziegler-2010]: J. F. Ziegler, M. D. Ziegler and J. P. Biersack, "SRIM
    – The stopping and range of ions in matter (2010)", *Nuclear
    Instruments and Methods in Physics Research B* **268**(11–12),
    1818–1823 (2010). <https://doi.org/10.1016/j.nimb.2010.02.091>
