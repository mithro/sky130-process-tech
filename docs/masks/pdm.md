(mask-pdm)=
# PDM — Pad (scribe protect)

The pad mask is the last {term}`reticle` of SKY130's step list: on the
{ref}`PDM <step-168>` page's reading, the resist printed through it at
step 168 is opened over every bond pad, probe pad and test pad, and the
{ref}`PDME <step-169>` etch cuts the passivation nitride and the oxide
beneath it down to the metal-5 pad. `masks.csv` lists two pad masks with
the one acronym, "Pad (scribe protect)", marked as used in SKY130, and
"Pad (scribe unprotect)", unmarked, and the process-steps sheet records
plates for the first on seven MPW runs, with no record for MPW-5, and
none for the second. The features are large — the smallest opening is
2 µm and a product pad tens of micrometres — and the design rules that
shape them sit less in the periphery rules than on the PDK's Error
Messages page and in its polyimide and packaging criteria. This page
gathers what public sources say about the mask itself — its PDK entries
and layers, the plates the process-steps sheet records for the MPW runs,
what the public renders of those runs show, the lithography it needs and
the rules that constrain it. How the step is performed is on the step
page; every mask is indexed on the {ref}`masks index <masks-index>`.

| | PDM — Pad (scribe protect) |
|---|---|
| Mask step | {ref}`PDM <step-168>`, step 168 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Pad (scribe protect)", `PDM`, marked `X` in `Used in SKY130`; "Pad (scribe unprotect)", `PDM`, unmarked[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cpdm` mask 37:0, "Pad mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `pad` drawing 76:20, "Passivation cut (opening over pads)"[^pdk-06] |
| Minimum CD, feature / space | "Pad (scribe protect)" `PDMCD` 2 / `PDMCDSP` 1.27; no row for "Pad (scribe unprotect)"[^pdk-03] |
| Polarity and tone | Not published; the PDK's `cpdm.nikon` checks name a polarity but not the plate's tone. On the step page's reading the resist is opened where `pad` is drawn, which with a positive resist would make the plate dark-field with clear openings (inference). |
| Exposure class | i-line, an inference on the step page from the 2 µm and 1.27 µm values; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | scribe protect: all except MPW-5; scribe unprotect: not recorded[^steps-sheet] |
| Plate no. | `600`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-pdm-steps>` |

## What the mask defines

The PDK is explicit about the layer: `pad` is "Passivation cut (opening
over pads)", `cpdm` the "Pad mask", and the function line of the `pad`
rule set reads "Opens the passivation".[^pdk-06][^pdk-periph] The stack
diagram draws the opening as a "glass cut" through the "TOPNIT" nitride
and "TOPOX" oxide over `metal5`.[^pdk-04] Table C3 of the *Layers
Reference* defines "bondPad" as "pad:dg OUTSIDE areaid:ft" and "hugePad"
as "pad.mk with width > 100um", and `gds_layers.csv` lists beside `pad` a
`padCenter` marker at 81:20, "Pad center marker", an `areaid.fe`
identifier at 81:3, "Pads in padframe identifier", and a `target` layer
at 76:44, "Metal fuse target", on the same layer number as
`pad`.[^pdk-06] The periphery rules give the opening only two rules, a
spacing of 1.270 µm (pad.2) and a "Max area of hugePad NOT top_metal" of
30000 µm² (pad.3).[^pdk-periph]

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance criteria
for GDS data", has many more pad checks than the periphery rules. It
requires "padPL pcells should be used for bondpad" (pad.1) and "2.7 min.
enclosure of bondpadNormal by met5" (pad.4/4a), and the same 2.7 for
"pad opening inside inductor by met5" (cupad.3); it gives a bond pad
chamfered corners — "Bondpad should have only 4 45 degree corner"
(pad.11), "7.0 Min length of 45 degree bevel on Bond pad" (pad.12) and
"8.8 Max length of 45 degree bevel on Bond pad" (pad.13) — a "150.0um Max
Width/Length of bond pad" (pad.9.1), "60 min width  of padPLFP in x
direction" (pad.2.1) and similar sizes for other pad cells, and "500.0
Max spacing between bondpad opening and edge of scribe line(outer end of
seal ring)" (pad.15); and it words pad.3 as "hugepad with area less than
30000.0 not allowed".[^pdk-errors] The {ref}`PDM <step-168>` page reads
SkyWater's GPIO cell `sky130_fd_io__top_gpiov2` as a 60 µm × 70 µm
opening with 4.95 µm chamfered corners over a metal-5 pad that extends
2.7 µm beyond it on every side (its reading of the published GDS and
LEF);[^pdk-io-gpiov2] the margin equals pad.4/4a, and if 4.95 µm is the
length cut from each side the bevel is 7.0 µm long, the pad.12 minimum
(our arithmetic and comparison). The PDM page's open question, that the
periphery rules give no enclosure of `pad` by metal 5, holds for those
rules; the Error Messages page gives one.[^pdk-periph][^pdk-errors]

**Test pads and the scribe.** The same page checks e-test pads in the
frame: "Etest pad Width and Length is either 67.00 um or 35.00um"
(scribe.9), a spacing of 90.5 µm between 67 µm pads (scribe.10), "2.50um
min. enclosure of Etest pad by met1" and the same for metals 2 to 5
(scribe.13), "Pad.dg is to be drawn from 3.0um from scribe edge to 13.0um
from scribe edge" (scribe.20) and "Scribe must not enclose pdm.dg nor
pdm.mk except for etest pads, die pad rings" (scribe.21).[^pdk-errors]
Table C3 defines "scribe_line" as "areaid:ft NOT areaid:dt", and Table 7
of *Criteria & Assumptions* gives a "Minimum scribe width" of 50
(`scribew`) in its column headed "CD".[^pdk-06][^pdk-03] The
{ref}`PDM <step-168>` page reads "scribe protect" as the variant that
leaves the passivation over the scribe lanes except where pads are drawn
(inference from the names and the mark); scribe.21, which keeps pad
openings out of the scribe apart from test pads and die pad rings, fits
that reading (our reading), but the PDK does not define either variant.
Lee found that the silicon nitride coverage of the scribe region can
carry sawing damage towards the active region, and that "appropriate
design of the amorphous Si3N4 layer in the scribe region is
essential";[^lee-2018] a TSMC patent that may still be in force is
cited here too, in the collapsed note below this paragraph.

:::{dropdown} From a patent shown as in force (US 7,679,384; estimated expiry 2028-06-06) — open to read
A TSMC patent describes parametric testlines in the scribe
line.[^pat-testline-tsmc]
:::

**Polyimide, redistribution and packaging.** Several PDK entries set the
opening against layers above it. Table F4 of the *Summary of Key
Periphery Rules* joins the copper redistribution layer `rdl` to metal 5
through "(pad AND pmm) for s8pir/s8pr2-10r flows", with the footnotes
"All layers drawn except pmm which is created as cpmm:mask over bond pads
or converted into cpbo:mask" and "(Met5 AND pad AND rdl) should have one
of the following sizes for LVS to work with WLCSP option: 60x60, 50x70,
60x80, and 80x80".[^pdk-summary] The `rdl` rules require a "Min
enclosure of pad by rdl, except rdl interacting with bump" of 10.750 µm
(rdl.3) and a spacing of 19.660 µm to pads (rdl.6).[^pdk-periph] Table 9
of *Criteria & Assumptions*, "Criteria for polyimide manufacturability",
gives in its column headed "CD" an "Enclosure of bondpad by polyimide
(YUY-165)" of 0.5 (`PimPadEnc`), enclosures of `pad:dg` by PBO of 4.5
(`PBOPadEnc`, "inside inductor capture pad, with DECA online
monitoring") and 7.5 (`PBOPadEncDECA`, "per standard DECA rules"), a "Min
Pim width over pad openings" of 87 (`PimOverPad_CD`) and a "Min/Max
enclosure of pad.dg inside M5RDL by pmm" of 0 (`pmmM5RDLpadEnc`), and in
its column headed "space" a "Min spacing of pmm to (rdl NOT (pad.dg sized
by 0.5))" of 19.16 (`pmmRDLspc`), which Table 10 repeats; Table 7 gives a
"Min enclosure of pad by pmm for Cu inductor (JNET-80)" of 0
(`padPMMEncInd`).[^pdk-03] The DECA table of the *WLCSP Rules* requires a
"Min bond pad passivation opening to create cpbo" of 35.00 (wlcsp.2) and
a "Min enclosure of cpbo over bond pad by pad:dg" of 7.50 (wlcsp.3), and
the Amkor table "pi1 must be enclosed by pad by atleast" 7.50, all printed
without a unit.[^pdk-wlcsp] The masks index records no mask step for the
marked `PBO`, `CU1M` and `PMM2` masks ({ref}`masks-index`), so these
entries describe options beyond the step list used here (our reading).

**Fuses.** The {ref}`PDM <step-168>` page notes that `target`, "Metal
fuse target", shares layer 76 with `pad` and cites a Vanguard patent on
controlling the oxide over fusible links, which it reads as making
bond-pad and fuse openings with one mask;[^pat-fuse-vanguard] whether the
SKY130 pad mask opens fuse windows is not public ({ref}`mask-mm4`). Table 9
gives an "Enclosure of fuses by polyimide" of 12 (`PimFuseEnc`).[^pdk-03]

**Variants.** The PDK does not explain the two variants. Table 2 of
*Criteria & Assumptions* has a row only for "Pad (scribe protect)", and
Table F2b, the mask generation table, has no `PDM` column.[^pdk-03][^pdk-06]
The mask does not define the pad metal ({ref}`mask-mm5`), the films it
opens ({ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>`) or the
seal-ring opening cut before them ({ref}`mask-nsm`).

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` has one mask-level layer for this mask, `cpdm` with
purpose `mask` at 37:0 ("Pad mask"), and no `drawing`, `mask add`, `mask
drop` or `waffle drop` purpose; the drawn layer is `pad` at 76:20, with
label and pin purposes.[^pdk-06] The pairing rests on those names and
descriptions, as on the {ref}`masks index <masks-index>`, and the PDK
publishes no operation from `pad` to the plate. Table C4b lists a
"cpmm:dg{91}", "Drawn compatible polyimide layer", "Drawn compatible
layer and used only inside S8 RF pad", and rule x.15b exempts "cpmm.dg
inside cellnames "PadPLfp", "padPLhp", "padPLstg" and "padPLwlbi" (for the
SKY130di-5r-gsmc flow)" from x.15a.[^pdk-06][^pdk-periph] Rule x.15a
confines "Drawn compatible, mask, and waffle-drop layers" to test
modules, seal ring and frame (flag P), so a design inside the die draws
`pad` (our reading of x.15a). Rule m4.13, for copper flows, excludes
"met4 overlapping pdm areas" from a density check.[^pdk-periph]

The Error Messages page names a mask-data layer `PDMmk` in the grid,
octagonal-edge and x.15a checks, and in two checks named `cpdm.nikon`,
"PDMmk in the nikon cross has the wrong polarity" and "PDMmk is missing
from the nikon cross in the layout"; it also checks "0.635 min. spacing
of moduleCutAREA & q0padnotBuildSpace" (x.12a), "pad drawn layer cannot
straddle areaid:ModuleCut" (scribe.7) and "pad inside frame or moduleCut
without text label" (scribe.6a).[^pdk-errors] The page does not say what
the "nikon cross" is. In the seal-ring cell `advSeal_6um_gen` of
Efabless's caravel repository, a sub-cell named `nikon_sealring_shape`
draws inside a 4 µm square, on `cpdm` 37:0, the square, with its corners
cut at 45°, less a cross of three rectangles, 2.4 µm across with 0.5 µm arms — the opposite form from
the cross it draws on `cnsm` 22:0 and `cmm5` 59:0 (our reading of the GDS
file).[^caravel-sealring] We read that sub-cell as a "nikon cross" of the
kind the checks name (inference from the names). On the step pages'
readings both the pad and the seal-ring resist are opened where the layer
is drawn, yet the two layers take opposite forms in the cell (our
comparison), so the form does not by itself give the plate's tone
({ref}`mask-nsm`).

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `PDM` the site renders layer 76:20 (`pad`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the description "Pad (scribe protect)", lists
"Pad (scribe protect)" and "Pad (scribe unprotect)" as variants, gives
the mask-level layer 37:0, no info text and the note "PDM = pad OR (cpmm
AND areaid.mt) sized by cpdm.4".[^mask-renders] The note and the render
disagree: the render job lists only 76:20, with no `cpmm` or `areaid.mt`
term and no sizing step (our comparison), so, as the
{ref}`masks index <masks-renders>` reads the site in general, the images
are unsized drawn `pad` data. Neither the periphery rules nor the Error
Messages page contains a rule named `cpdm.4`, and the site gives no
source for the note.[^pdk-periph][^pdk-errors] The note and the choice of
layer are one public derivation from the drawn data, not SkyWater's
mask-generation recipe. The sheet's "Run Mask IDs" row for "Pad (scribe
protect)" has no "Info" note.[^steps-sheet]

The die count is not a count of pad designs. Every rendered die of every
run carries `pad` shapes. The minimum per-die count is 96 shapes (107 on
MPW-1), and on each run most dies carry exactly 96 or exactly 107: 36 of
the 40 dies on MPW-1 (all 107), 40, 40, 39, 39, 40, 38 and 39 on MPW-2 to
MPW-8 in turn; the other dies carry from 106 to 284 901
shapes.[^mask-renders] We read the two repeated counts as layouts common
to the dies rather than to the projects (inference), as the
{ref}`DNM mask page <mask-dnm>` reads its repeated counts; the site does
not say what they are. For MPW-5 the renders show shapes on all 40 dies
although the sheet records no `PDM` plate for that run, which fits the
masks index's reading of the gap as one in the record, but the renders
show the drawn layouts, not the plates.[^mask-renders][^steps-sheet] The
site states the limits of its images: "These are renders of *drawn* data,
not photomask artwork: reticle pitch, 4x reduction, mirroring and the
frame features the fab adds are not modelled."[^mask-renders] The frame,
where the e-test pads of the scribe rules sit, is therefore not shown.
Its metadata carries no plate ID, so a render is tied to a plate in the
sheet only by the acronym `PDM`, and the MPW-4 renders come from a
different reticle set from the one whose plates the sheet records
({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a plate for "Pad
(scribe protect)" as existing on seven runs, with the plate number `600`
on each, and has no mark or plate ID for MPW-5.[^steps-sheet] The table
covers that variant; the sheet records no plates for "Pad (scribe
unprotect)" on any run.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA600A` |
| MPW-2 | `5CS8007AC` | `S8007AA600A` |
| MPW-3 | `5CS8008AC` | `S8008AA600A` |
| MPW-4 | `5CS8018AC` | `S8018AA600A` |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA600A` |
| MPW-7 | `5CS8016AC` | `S8016AA600A` |
| MPW-8 | `5CS8017AC` | `S8017AA600A` |

* **MPW-5.** The sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5 and gives no reason. This page reports what
  is recorded and does not conclude that the mask was absent from MPW-5:
  the masks index reads a gap in the record as likelier than a run
  without these masks, since every working die needs them (inference)
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `600` encodes. It is
  above the `590` of `MM5` and below only the `616` of the MPW-6 `NSM`
  plate, but the numbers do not follow process order elsewhere (`NSM`,
  step 165, is `007` on seven runs), so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `PDM`.[^steps-sheet] 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`PDM <step-168>` page gives
{math}`k_1 = 1.27 \times 0.6 / 0.365 \approx 2.1` on an i-line tool with
an assumed NA of 0.6, "well above any resolution limit", and infers an
i-line exposure, quoting ASML's statement that older systems "migrate to
the lithography of choice for less critical layers";[^asml-30] the
{ref}`i-line stepper <machine-i-line-stepper>` page lists it there.
SkyWater lists "ASML I-line stepper" and "ASML I-line scanner" but
assigns no layer to them.[^skw-01]

**The plate and its tolerance.** Wong et al. found that the mask error
factor "is unity for large features, but increases rapidly when the
critical dimension (CD) is less than 0.5 (lambda) /NA for line-space
patterns";[^wong-1998] at 365 nm and NA 0.6 that is about 0.30 µm (our
arithmetic), far below the 1.27 µm space, so plate CD errors would print
at their own size (inference). Table 4 of *Criteria & Assumptions* gives
a "CD tolerance for PDM (3s)" of 1 (`PdmCD_tol`), in its "Material
Thicknesses" block with a column headed "Value (um)", against a 2 µm
minimum opening;[^pdk-03] the PDK does not say what the tolerance
covers, and we read it as a loose budget for plate, print and etch
together (inference). At 4× a 2 µm opening is 8 µm on the plate (our
arithmetic), within reach of the laser writers and wet-etched chrome that
the {ref}`CAPM <mask-capm>` and {ref}`VIM4 <mask-vim4>` pages discuss: a
laser writer of the ALTA family addressed "the needs of maskmakers in the
180 nm and 150 nm technology nodes",[^morgante-2000] and chrome masks
"have traditionally been wet etched".[^buck-1994] None of this is
recorded for the `PDM` plate.

**Resist.** The {ref}`PDM <step-168>` page reads a positive DNQ/novolac
i-line resist, the chemistry of Dammel's text,[^dammel-1993] coated over
a transparent nitride-over-oxide stack of the order of 0.6–1 µm on
reflective aluminium and the 1.26 µm metal-5 topography,[^pdk-04] with
its thickness chosen against the swing curve Brunner
analysed;[^brunner-1991] with the resist opened where `pad` is drawn,
the plate would be dark-field (inference). It also notes that this is
the only mask printed after the passivation nitride, so rework strips
resist from a sealed die. SkyWater's resist is not public; the
consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the resist pattern is
transferred by {ref}`PDME <step-169>`, a fluorine-based etch of the
nitride and oxide that stops on the metal-5 pad, on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>` class,
with the resist strip and pad clean treated as part of that step. That
page cites a Micron and a TSMC patent on removing fluorine residues from
bond pads,[^pat-pad-fluorine-micron][^pat-pad-fluorine-tsmc] and Danzl
and McLaurin on removing a TiW anti-reflective cap from aluminium bond
pads,[^danzl-1997] and leaves open whether SKY130's pads carry such a
cap. The opening defines the part of the pad that probe needles and wire
bonds reach; Hunter et al. used wire bonding to study probe damage in
aluminium pads,[^hunter-2012] Ching and Schroen related bond-pad cracking
to the oxides under the pad and studied the pad metallisation,[^ching-1988] and
Comizzoli et al. reviewed the corrosion of electronic materials and
devices.[^comizzoli-1986]

**Overlay.** The 2.7 µm enclosure of the opening by metal 5 in the GPIO
cell, which the Error Messages page makes a check (pad.4/4a), is, on the
{ref}`PDM <step-168>` page's reading, a loose overlay budget for an
alignment to the metal-5 pattern.[^pdk-errors][^pdk-io-gpiov2]

(mask-pdm-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `PDM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`PDM <step-168>`, {ref}`PDME <step-169>`

* {ref}`PDM <step-168>` — coats, exposes and develops the resist.
* {ref}`PDME <step-169>` — etches the nitride and oxide over the pads
  through the resist; the step list used in this reference has no
  separate strip step, and the step page treats the resist strip and
  clean as part of the etch.

On its step page's reading, the next step, {ref}`ALLY <step-170>`,
anneals the finished wafers at low temperature in a hydrogen-bearing
ambient after the resist is gone. There is no next mask step: `PDM` is
the last of the 36 mask steps, and the step list ends with
{ref}`ALLY <step-170>` and {ref}`HPETEST <step-171>`. The rule needs no exception
for this mask.

## Design rules and critical dimensions

The `pad` rules of the periphery rules, with the other rules that name
the pad opening or its mask data. Flag CU means "Rules applicable only to
Cu BE flows", P "Rule applies to periphery only (outside areaid.ce). A
corresponding core rule may or may not exist.", EXEMPT "Rule is an
exception?" and NC "Rule not checked by DRC. It should be used as a
guideline only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| pad.2 | "Min spacing of pad:dg to pad:dg" | 1.270 µm |
| pad.3 | "Max area of hugePad NOT top_metal" | 30000 µm² |
| m4.13 | "Max pattern density (PD) of metal4; met4 overlapping pdm areas are excluded from the check" (CU) | 0.77 |
| m4.16 | "Min enclosure of pad by met4" (CU) | 0.850 µm |
| rdl.3 | "Min enclosure of pad by rdl, except rdl interacting with bump" | 10.750 µm |
| rdl.6 | "Min spacing of rdl to pad, except rdl interacting with bump" | 19.660 µm |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.9 (first row) | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. Exempted are: […] cfom md/mp inside "advSeal_6um\* OR cuPillarAdvSeal_6um\*" pcell […] diff rings around the die at min total L>1000 um and W=0.3 um, and PMM/PDMM inside areaid:sl" | — |
| x.9 (second row) | "Shapes on maskAdd or maskDrop layers ("serifs") are allowed in core only. PMM/PDMM inside areaid:sl are excluded." | N/A |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.15b | "Rule X.15a exempted for cpmm.dg inside cellnames "PadPLfp", "padPLhp", "padPLstg" and "padPLwlbi" (for the SKY130di-5r-gsmc flow)" (EXEMPT) | — |

The Error Messages page repeats pad.2 as "1.27 min. spacing/notch of
pad" and adds the pad and scribe checks quoted above.[^pdk-errors]
Table 2 of *Criteria & Assumptions* gives "Pad (scribe protect)" a
feature size of 2 (`PDMCD`) and a space size of 1.27 (`PDMCDSP`); Table 4
the `PdmCD_tol` of 1; Table 7 `padPMMEncInd` and `scribew`; and Table 9
the polyimide and PBO criteria quoted above.[^pdk-03] For the plate the
decisive figures are a 2 µm minimum opening on 1.27 µm spaces, a 3.27 µm
pitch (our arithmetic from Table 2), and product openings of the order of
60 µm with chamfered corners.

## Related pages

* {ref}`PDM <step-168>` and {ref}`PDME <step-169>` — the mask step and
  the pad etch; {ref}`NTSD <step-167>` and {ref}`NFUSOX <step-164>` — the
  films opened; {ref}`ALLY <step-170>` and {ref}`HPETEST <step-171>` —
  the anneal and test that follow.
* {ref}`mask-mm5` — the mask of the pad metal; {ref}`mask-nsm` — the other
  opening in the passivation module; {ref}`mask-mm4` — the metal-fuse
  mask.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the variants and the MPW-5 gaps.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-dielectric` — the etch class that
  transfers the pattern.
* {ref}`material-lithography-materials` — resists, developer and
  reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Pad (scribe protect),
  PDM, X" and "Pad (scribe unprotect), PDM".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `pad` 76:20,
  `cpdm` 37:0, `padCenter`, `areaid.fe`, `target`, Table C3's "bondPad",
  "hugePad" and "scribe_line", Table C4b's `cpmm` and the columns of Table
  F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `PDMCD`/`PDMCDSP`,
  `PdmCD_tol`, `padPMMEncInd`, `scribew` and the polyimide
  criteria.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `pad` rules and function line,
  m4.13, m4.16, rdl.3, rdl.6, x.1b, x.7, x.9, x.15a, x.15b and the
  flag legend.[^pdk-periph]
* [SkyWater PDK, *Error Messages* page](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) — the pad, cupad.3, scribe and `cpdm.nikon`
  checks.[^pdk-errors]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Table F4 and its
  footnotes.[^pdk-summary]
* [SkyWater PDK, *WLCSP Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/wlcsp.html>) — the DECA and Amkor pad-opening
  rules.[^pdk-wlcsp]
* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — the "glass cut".[^pdk-04]
* SkyWater I/O library, `sky130_fd_io__top_gpiov2` — the GPIO pad
  opening.[^pdk-io-gpiov2]
* Efabless, caravel `advSeal_6um_gen` seal-ring GDS — the
  `nikon_sealring_shape` sub-cell.[^caravel-sealring]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `PDM` plates of MPW-1
  to MPW-8 and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `PDM` renders, their layer,
  variants and note, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *Three decades of PAS 5500*](<https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>) — older exposure tools moving to less
  critical layers.[^asml-30]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line exposure.[^wiki-litho]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — swing curves
  and coating over topography.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on masks and reticles
  and on overlay.[^levinson-2005]

### Deep dive

* [Lee, *Materials Transactions* 2018](<https://doi.org/10.2320/matertrans.M2018221>) — silicon nitride in the scribe
  region and sawing damage.[^lee-2018]
* [Tzeng, Chen and Wang (Vanguard), US 6,294,474](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6294474>) — oxide thickness over
  fusible links.[^pat-fuse-vanguard]
* Jones, Crane, Gilchrist and Langley (Micron), US 5,380,401, and Tsai and
  Liu (TSMC), US 7,055,532 — removing fluorine residues from bond
  pads.[^pat-pad-fluorine-micron][^pat-pad-fluorine-tsmc]
* [Danzl and McLaurin, IEMT 1997](<https://doi.org/10.1109/IEMT.1997.626884>) — removing a TiW anti-reflective cap from
  aluminium bond pads.[^danzl-1997]
* [Hunter et al., IMAPS 2012](<https://doi.org/10.4071/isom-2012-TP41>) — wire bonding as a probe of pad damage from
  wafer probing.[^hunter-2012]
* [Ching and Schroen, IRPS 1988](<https://doi.org/10.1109/IRPS.1988.362201>) — bond-pad cracking, the oxides under the pad
  and the pad metallisation.[^ching-1988]
* [Comizzoli et al., *Science* 1986](<https://doi.org/10.1126/science.234.4774.340>) — corrosion of electronic materials and
  devices.[^comizzoli-1986]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  feature size above which it is unity.[^wong-1998]
* [Morgante and Hamaker, *Proc. SPIE* 2000](<https://doi.org/10.1117/12.392079>) — a laser reticle writer and the
  mask nodes it served.[^morgante-2000]
* [Buck and Grenon, *Proc. SPIE* 1994](<https://doi.org/10.1117/12.167247>) — wet against dry chrome etching of
  masks.[^buck-1994]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — the swing ratio on reflective
  substrates.[^brunner-1991]
* [Dammel, *Diazonaphthoquinone-based Resists*](<https://doi.org/10.1117/3.2265072>) — the i-line resist
  chemistry.[^dammel-1993]

:::{dropdown} From a patent shown as in force (US 7,679,384; estimated expiry 2028-06-06) — open to read
* Chen, Hsu, Tsai and Jeng (TSMC), US 7,679,384 — parametric testlines in
  the scribe line.[^pat-testline-tsmc]
:::

## Open questions

* The PDK does not define "scribe protect" and "scribe unprotect"; the
  step page's reading, and the fit of scribe.21 to it, are
  inferences.[^pdk-05][^pdk-errors]
* The renders site's note "PDM = pad OR (cpmm AND areaid.mt) sized by
  cpdm.4" names a rule that neither the periphery rules nor the Error
  Messages page contains, and the render does not include the terms it
  names; the operation that makes the `cpdm` plate data is not
  published.[^mask-renders][^pdk-periph][^pdk-errors]
* Whether the sheet's missing MPW-5 record is a gap in the record or a
  difference in the run is not stated, and no public source lists the
  `PDM` plate of the original MPW-4 set `5CS8010AC`.[^steps-sheet][^mask-renders]
* What `PdmCD_tol` covers, and whether the pad mask also opens fuse
  windows over `target`, are not public.[^pdk-03][^pdk-06]
* The PDK does not describe the "nikon cross" or say which form a mask
  layer takes in it; reading the caravel sub-cell as that cross is an
  inference.[^pdk-errors][^caravel-sealring]
* The exposure tool, the plate's type, tone and CD specification, and the
  resist are not public; what the plate number `600` encodes is not
  stated.[^steps-sheet]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists", "Plate ID" and "Info" columns)
    and "Sheet4" (mask types), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table C3,
    the device and CAD definitions, Table C4b, the auxiliary layers, and
    Table F2b, the mask generation table) and `gds_layers.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4,
    7, 9 and 10), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Table F4 and its footnotes), SkyWater SKY130 PDK documentation,
    retrieved 2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-wlcsp]: SkyWater PDK Authors, *WLCSP Rules* (Amkor and DECA
    tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/wlcsp.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/wlcsp/deca.csv>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/wlcsp/amkor.csv>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-io-gpiov2]: SkyWater PDK Authors, *skywater-pdk-libs-sky130_fd_io*
    repository, cell `sky130_fd_io__top_gpiov2`, GDS layout
    `sky130_fd_io__top_gpiov2.gds` and LEF abstract
    `sky130_fd_io__top_gpiov2.lef`, retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-libs-sky130_fd_io/tree/main/cells/top_gpiov2>
[^caravel-sealring]: Efabless Corporation, *caravel* repository,
    `gds/advSeal_6um_gen.gds.gz` (seal-ring cell for SKY130 shuttle
    designs), retrieved 2026-09-14.
    <https://github.com/efabless/caravel/blob/main/gds/advSeal_6um_gen.gds.gz>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_PDM/`
    directory with its page, `job.json` and per-die slot JSON files,
    retrieved 2026-09-14. Rendered from the public shuttle repositories
    under <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
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
[^lee-2018]: S.-M. Lee, "Pattern Design to Prevent Sawing-Induced
    Passivation Damage on Scribe Region During Semiconductor Wafer
    Separation", *Materials Transactions* **59**(12), 1887–1891 (2018).
    <https://doi.org/10.2320/matertrans.M2018221>
[^pat-testline-tsmc]: H.-W. Chen, S.-H. Hsu, H.-Y. Tsai and S.-P. Jeng
    (Taiwan Semiconductor Manufacturing Co.), *Parametric testline with
    increased test pattern areas*, US 7,679,384 B2, filed 2007-06-08,
    granted 2010-03-16.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7679384>
    Shown as in force; estimated expiry 2028-06-06 (estimate from public
    records, not legal advice).
[^pat-fuse-vanguard]: W.-T. Tzeng, Y.-F. Chen and K.-J. Wang (Vanguard
    International Semiconductor), *Process for controlling oxide
    thickness over a fusible link using transient etch stops*,
    US 6,294,474 B1, filed 1999-10-25, granted 2001-09-25.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6294474>
[^pat-pad-fluorine-micron]: C. S. Jones, W. J. Crane, R. L. Gilchrist
    and R. C. Langley (Micron Technology), *Method to remove fluorine
    residues from bond pads*, US 5,380,401 A, filed 1993-01-14, granted
    1995-01-10.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5380401>
[^pat-pad-fluorine-tsmc]: H.-C. Tsai and H.-H. Liu (Taiwan Semiconductor
    Manufacturing Co.), *Method to remove fluorine residue from bond
    pads*, US 7,055,532 B2, filed 2003-12-18, granted 2006-06-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7055532>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. Twenty-First IEEE/CPMT International Electronics
    Manufacturing Technology Symposium (IEMT 1997)*, pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^hunter-2012]: S. Hunter, J. L. Clark, D. Hornberger and L. Rubio, "Use
    of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
    *International Symposium on Microelectronics* **2012**(1), 384–395
    (IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41>
[^ching-1988]: T. B. Ching and W. H. Schroen, "Bond Pad Structure
    Reliability", *26th International Reliability Physics Symposium*
    (1988), pp. 64–70. <https://doi.org/10.1109/IRPS.1988.362201>
[^comizzoli-1986]: R. B. Comizzoli, R. P. Frankenthal, P. C. Milner and
    J. D. Sinclair, "Corrosion of Electronic Materials and Devices",
    *Science* **234**(4774), 340–345 (1986).
    <https://doi.org/10.1126/science.234.4774.340>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 106 (1998).
    <https://doi.org/10.1117/12.310718>
[^morgante-2000]: C. G. Morgante and H. C. Hamaker, "ALTA 3700:
    extending the application space of the ALTA 3500 laser reticle
    writer", *Proc. SPIE* **4066**, 613 (2000).
    <https://doi.org/10.1117/12.392079>
[^buck-1994]: P. D. Buck and B. J. Grenon, "Comparison of wet and dry
    chrome etching with the CORE-2564", *Proc. SPIE* **2087**, 42–49
    (1994). <https://doi.org/10.1117/12.167247>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
