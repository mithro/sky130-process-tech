(mask-onom)=
# ONOM — ONO Mask

The ONO mask is the second {term}`reticle` of SKY130's {term}`SONOS`
memory module: on the {ref}`ONOM <step-041>` page's reading, the resist
printed through it at step 41 leaves islands over the memory transistors,
and {ref}`ONOME <step-042>` etches the oxide–nitride–oxide stack grown at
{ref}`ONO <step-040>` away from everywhere else before the logic gate
oxides are grown. The PDK lists the mask and a mask-level layer but no
drawn layer and no rules for it, so what the plate carries is a reading
from the tunnel-mask layer it must enclose. Like the
{ref}`tunnel mask <mask-tunm>`, it has a plate recorded on all eight MPW
runs while the public renders show its layer on one die of MPW-1 and one
of MPW-5 only. This page gathers what public sources say about the mask
itself — its PDK entry and layers, the plates the process-steps sheet
records, what the public renders show, the lithography it needs and the
rules that constrain it. How the step is performed is on the step page;
every mask is indexed on the {ref}`masks index <masks-index>`.

| | ONOM — ONO Mask |
|---|---|
| Mask step | {ref}`ONOM <step-041>`, step 41 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "ONO Mask", `ONOM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `conom` mask 88:0, "ONO Mask"; drawing 87:44, with no description[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | no drawn `onom` layer; from `tunm` drawing 80:20, "SONOS device tunnel implant", oversized — an inference of the step page[^pdk-06] |
| Minimum CD, feature / space | `ONOMCD` 0.41 / `ONOMCDSP` 0.5[^pdk-03] |
| Polarity and tone | Not published. On the step page's reading the resist remains as islands over the memory transistors and is removed elsewhere, which with a positive resist would make the plate clear-field with opaque islands (inference). |
| Exposure class | i-line, an inference on the step page from the relaxed size of the islands, as for the tunnel mask; no public source names the tool ({ref}`machine-i-line-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all eight[^steps-sheet] |
| Plate no. | `230`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 1, 0, 0, 0, 1, 0, 0, 0[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-onom-steps>` |

## What the mask defines

The mask defines where the charge-trapping stack survives. On the step
pages' readings the {ref}`ONO <step-040>` step coats the whole wafer
with a tunnel oxide, a nitride or oxynitride trapping layer and a
blocking oxide, and the {ref}`ONOM <step-041>` resist keeps that stack
only as islands over the memory transistors, each enclosing a tunnel
window opened at {ref}`TUNM <step-035>` (inference on the step page).
A Cypress patent gives the order of magnitude of such a stack: in one
embodiment a tunnel dielectric of "less than about 25 Å" and a charge
storing layer of "less than about 200 Å, preferably less than about
150 Å, more preferably less than about 100 Å", and in another a top
insulating layer of "about 100 Å, preferably less than about
50 Å";[^pat-01] SKY130's thicknesses are not public.

The PDK's mask generation table, Table F2b, marks the `ONOM` column
exactly as it marks `TUNM`: `C` ("CREATED") in the two "SONOS fet" rows,
the two "NV SONOS fet" rows and the "NV SONOS Diode" row, `-` ("Layer
not created for the device") in 44 rows including every 1.8 V, 5 V and
high-voltage transistor row and the two "Flash npass" rows, and `+` in
the other 31.[^pdk-06] We read the identical columns as consistent with
the step page's derivation of the island from the tunnel window, since
the table gives no device a created `ONOM` shape without a created
`TUNM` shape (our reading of the table, which does not say how either
is made). Table 2 of *Criteria & Assumptions* gives the two masks the
same minimum feature and space, 0.41 and 0.5.[^pdk-03]

The island has two jobs on the step pages' readings. It must enclose the
window with margin, because inside the window the silicon carries only
the tunnel oxide; and it must keep the stack off every logic channel,
whose gate oxide is grown afterwards at {ref}`GOX100 <step-043>` and
{ref}`LVGOX <step-047>`. Cypress's integration patent, which may still
be in force, says the same of its own flow; the passage is in the
collapsed note below this paragraph. What the mask does not define is the gate of the
memory transistor: the {ref}`ONOME <step-042>` page reads the islands as
etched again, self-aligned to the poly, at {ref}`P1ME <step-062>`.

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
Cypress's integration patent says of its own flow that "If the overlay
of the ONO charge trapping dielectric stack 306 and the window 305 is
not adequate (e.g. D2 becomes zero) the substrate region of SONOS device
300 may be rendered non-functional by subsequent processes. Thus, for
this reason too, the dimensions and alignment of window 305 and ONO
charge trapping dielectric stack 306 are important."[^pat-03]
:::

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives the mask-level layer `conom` two purposes: `mask`
at 88:0 ("ONO Mask") and `drawing` at 87:44, which has no
description.[^pdk-06] Layer number 88 also carries the `chvtpm` drawing
purpose, 88:44 ({ref}`masks-index`). There is no drawn layer named
`onom`, the periphery rules have no `onom` or `conom` rule set, and no
rule names the mask.[^pdk-06][^pdk-periph] The
{ref}`ONOM <step-041>` page therefore infers that the plate is generated
from `tunm` by oversizing, so that the island always encloses the
window, and the masks index records the pairing with `tunm` as an
inference; the PDK publishes neither the operation nor the oversize.
Rule x.15a confines "Drawn compatible, mask, and waffle-drop layers" to
test modules, the seal ring and the frame, with the exception
"FOM/P1M/Metal waffle drop are allowed inside the die" (flag
P),[^pdk-periph] so a design inside the die cannot use the `conom`
drawing purpose to shape the islands (our reading of x.15a).

The PDK's *Error Messages* page, which describes "many of the automated
DRC rules that are checked by SkyWater as part of the acceptance
criteria for GDS data", names the layer only in generic checks: "off
0.005 grid conom vertex" and "off 0.005 grid ONOMmk vertex" (x.1b),
"non-octagonal conom edge" and "non-octagonal ONOMmk edge" (x.3a), and
"X.15a: layer conom allowed inside areaid:mt or inside areaid.sl or
inside areaid.ft" with the same message for `ONOMmk`.[^pdk-errors] It
lists no width, spacing or enclosure check for `conom` or `ONOMmk`, and
no "nikon cross" check for it.[^pdk-errors] Apart from `ONOMCD` and
`ONOMCDSP` in Table 2, no row of *Criteria & Assumptions* names the
mask.[^pdk-03]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `ONOM` the site renders layer 80:20 (`tunm`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the mask-level layer 88:0 and the note "ONOM =
tunm sized by clonom.3 (conom 87:44 is the fab's precomputed layer, not
drawn)".[^mask-renders] Neither the periphery rules nor the Error
Messages page contains a rule named `clonom.3`, and `gds_layers.csv`
lists 87:44 as a `conom` drawing purpose without saying what it
holds;[^pdk-periph][^pdk-errors][^pdk-06] the site gives no source for
either statement. The render jobs list only the drawn layer, with no
sizing step, so, as the {ref}`masks index <masks-renders>` reads the
site in general, the images are unsized `tunm`. The note and the choice
of layer are one public derivation from the drawn data, not SkyWater's
mask-generation recipe; they agree with the step page's derivation from
`tunm`, but both start from the same public PDK files, so the agreement
is not independent.

Because the layer is the tunnel mask's, the `ONOM` renders show exactly
the `TUNM` renders: MPW-1, frame A4, with 4 shapes, and MPW-5, frame D7,
with 16, and no shapes on any die of the other six runs.[^mask-renders]
They carry no information about the islands beyond that. The site
states the limits of its images: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled. Empty images are real results -
several masks are used by no project on a given
shuttle."[^mask-renders] Its metadata carries no plate ID, and the MPW-4
renders come from a different reticle set from the one whose plates the
sheet records ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks an `ONOM` plate
as existing on all eight MPW runs, with the plate number `230` on each
and no "Info" note.[^steps-sheet] The plate IDs below are the sheet's;
the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA230A` |
| MPW-2 | `5CS8007AC` | `S8007AA230A` |
| MPW-3 | `5CS8008AC` | `S8008AA230A` |
| MPW-4 | `5CS8018AC` | `S8018AA230A` |
| MPW-5 | `5CS8011AC` | `S8011AA230A` |
| MPW-6 | `5CS8014AC` | `S8014AA230A` |
| MPW-7 | `5CS8016AC` | `S8016AA230A` |
| MPW-8 | `5CS8017AC` | `S8017AA230A` |

* **Plates on runs with no drawn `tunm`.** A plate is recorded on MPW-2,
  MPW-3, MPW-4, MPW-6, MPW-7 and MPW-8, on which no rendered die draws
  `tunm`, the layer the renders and the step page use for this mask, as
  well as on MPW-1 and MPW-5.[^steps-sheet][^mask-renders] The renders
  leave out whatever the fab adds to a plate, so they cannot show what
  those six plates carry, and no public source says ({ref}`masks-renders`).
* **Plate number.** `230` is higher than `210` for `P1M` (step 61) and
  `180` for `NPCM` (step 78), and the sheet does not say what the numbers
  encode, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type and magnification.** The sheet's "Sheet4" tab gives no
  type for `ONOM`,[^steps-sheet] and no public source gives this plate's
  blank, absorber or reduction ratio; 4× is the ITRS 2001 mask
  magnification for the 130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`, whose plates no public
  source lists ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`ONOM <step-041>` page reads the islands as
the 0.410 µm tunnel windows grown by a margin that is not public, a
relaxed layer, and infers an i-line exposure as for
{ref}`TUNM <step-035>`; the {ref}`i-line stepper <machine-i-line-stepper>`
page lists it there. SkyWater lists "ASML I-line stepper" and "ASML
I-line scanner" among its tools but assigns no layer to them.[^skw-01]
Table 2's `ONOMCD` of 0.41 would put the smallest island at
{math}`k_1 \approx 0.54` at NA 0.48, the low end of ASML's
PAS 5500/275D[^asml-pas5500-275d] (our arithmetic), and Wong et al.'s
mask error factor, which "increases rapidly when the critical dimension
(CD) is less than 0.5 (lambda) /NA for line-space
patterns",[^wong-1998] would stay near unity down to about 0.38 µm at
that NA (our arithmetic).

**Resist.** The {ref}`ONOM <step-041>` page reads a positive i-line
resist of about 1 µm, the PDK's generic "Photoresist thickness" being
1.14 µm,[^pdk-03] with etch selectivity rather than implant stopping
setting the thickness, and leaves open whether an anti-reflective coating
is used; what the Cypress integration patent, which may still be in
force, uses is in the collapsed note below this paragraph. The surface
under the resist is the blocking oxide of the stack. SkyWater's resist
and any ARC are not public; the consumables are on the
{ref}`lithography materials <material-lithography-materials>` page.

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
The Cypress integration patent uses "an inorganic spin-on
anti-reflective coating (ARC)" that is dry-etched with the
stack.[^pat-03]
:::

**Pattern transfer.** On the step pages' readings the pattern is
transferred by {ref}`ONOME <step-042>`: a plasma etch of the top oxide
and the nitride that stops on the oxide beneath, on the
{ref}`silicon and polysilicon plasma etcher <machine-plasma-etcher-silicon>`
or {ref}`dielectric and nitride plasma etcher <machine-plasma-etcher-dielectric>`
class, followed by a wet clearing of the remaining oxide on the
{ref}`wet bench <machine-wet-bench>` class, with the resist strip and
pre-gate-oxide clean treated as part of that step. Regis et al. report a
nitride etch "with high selectivity to oxide" of the kind such a stop
needs.[^regis-1997] The Cypress integration patent, which may still be
in force, describes the same combination and notes what the wet step
does to the masked region; the passage is in the collapsed note below
this paragraph. The undercut it describes shrinks the island's overlap
of the window, which is why the patent calls the dimensions and
alignment of the two important (above).

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
The Cypress integration patent describes the same combination — "the
blocking layer 304C, and the dielectric layers 304A and 304B are dry
etched, with the dry etch process stopping on the sacrificial dielectric
layer 303. In a subsequent wet etch operation, an etchant, such as BOE,
is employed to clear sacrificial dielectric layer 303" — and notes that
"the isotropic wet etch may undercut the masked region".[^pat-03]
:::

**Overlay.** The {ref}`ONOM <step-041>` page infers that the critical
overlay of this mask is to the tunnel mask rather than to active, which
is unusual in the flow, and that overlay would be measured to the `TUNM`
layer. The PDK publishes no enclosure of the window by the island, so
the overlay budget is not public; ASML specifies "≤ 40 nm" single-machine
overlay for the /275D stepper.[^asml-pas5500-275d] Starikov analysed the
accuracy of overlay measurements,[^starikov-1992] and van Haren et al.
show how alignment-mark placement accuracy limits layer-to-layer
overlay.[^van-haren-2019]

(mask-onom-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `ONOM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`ONOM <step-041>`, {ref}`ONOME <step-042>`

* {ref}`ONOM <step-041>` — coats, exposes and develops the resist
  islands on the blocking oxide of the stack.
* {ref}`ONOME <step-042>` — etches the stack away outside the islands;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and the pre-gate-oxide clean as
  part of the etch.

On its step page's reading, the next step, {ref}`GOX100 <step-043>`,
grows the thick gate oxide over the active areas the etch has cleared,
after the resist is gone. The next mask step is {ref}`LVOM <step-044>`.
There is no exception to the rule for this mask.

## Design rules and critical dimensions

The periphery rules have no rule set for `onom` or `conom`. The rules
below are those of the tunnel layer that the step page derives the
islands from, with rule x.15a; flag TC means "Rule not checked for cell
name “\*_tech_CD_top\*”", and flag P "Rule applies to periphery only
(outside areaid.ce). A corresponding core rule may or may not exist.".
The unit column of tunm.3 is blank in the published table.[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| tunm.1 | "Min width of tunm" | 0.410 µm |
| tunm.2 | "Min spacing of tunm to tunm" | 0.500 µm |
| tunm.3 | "Extension of tunm beyond (poly and diff)" | 0.095 |
| tunm.5 | "(poly and diff) may not straddle tunm" | — |
| tunm.6a | "Tunm outside deep n-well is not allowed" (TC) | — |
| tunm.8 | "tunm must be enclosed by areaid.ce" | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |

Table 2 of *Criteria & Assumptions* gives `ONOMCD` 0.41 and `ONOMCDSP`
0.5, the same values as `TUNMCD` and `TUNMCDSP` and as rules tunm.1 and
tunm.2.[^pdk-03][^pdk-periph] The table does not say whether these are
the island's own minima or carried over from the tunnel layer. On the
step page's reading the islands are larger than the windows by an
undisclosed margin, so the plate's smallest features would be the
windows' minima plus that margin (inference), and the step page reads
tunm.8 as confining the islands, like the windows, to the memory blocks
marked `areaid.ce`.

## Related pages

* {ref}`ONOM <step-041>` and {ref}`ONOME <step-042>` — the mask step and
  the stack etch; {ref}`ONO <step-040>` — the stack patterned.
* {ref}`mask-tunm` — the tunnel mask, whose windows the islands enclose
  and whose layer the step page and the renders use for this mask.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the runs whose plates have no drawn shapes.
* {ref}`machine-i-line-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-silicon` and
  {ref}`machine-plasma-etcher-dielectric` — the etch classes that
  transfer the pattern.
* {ref}`machine-cd-sem-overlay-metrology` — overlay to the tunnel mask.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "ONO Mask, ONOM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `conom` 88:0
  and 87:44, `tunm` 80:20 and the `ONOM` and `TUNM` columns of Table
  F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `ONOMCD`/`ONOMCDSP` and the
  photoresist thickness.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `tunm` rules, x.15a and the flag
  legend.[^pdk-periph]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the `conom` and
  `ONOMmk` checks.[^pdk-errors]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `ONOM` plates of
  MPW-1 to MPW-8 and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `ONOM` renders, their layer
  and note, and the per-die shape counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the i-line exposure
  tools.[^skw-01]
* [ASML, *PAS 5500/275D* data sheet](<https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>) — NA range and single-machine
  overlay of an i-line stepper.[^asml-pas5500-275d]

:::{dropdown} From a patent shown as in force (US 8,093,128; estimated expiry 2028-10-22) — open to read
* Koutny et al. (Cypress), US 8,093,128 — the dry-then-wet stack etch,
  its undercut and the window-to-stack overlay.[^pat-03]
:::

### High-level understanding

* [Wikipedia, *SONOS*](<https://en.wikipedia.org/wiki/SONOS>) — the oxide–nitride–oxide memory
  transistor.[^cyp-26]
* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Ramkumar et al. (Cypress), US 6,969,689](<https://patents.google.com/patent/US6969689B1/en>) — the ONO stack this mask
  confines, its layers formed in one reaction chamber (several
  embodiments).[^pat-01]
* [White, Adams and Bu, *IEEE Circuits and Devices* 2000](<https://doi.org/10.1109/101.857747>) — a review of
  scaled SONOS.[^pap-01]
* [Seo et al. (Samsung), *IEEE JSSC* 2005](<https://doi.org/10.1109/JSSC.2005.845564>) — a 130 nm local-SONOS embedded
  flash from another vendor.[^pap-02]
* [Kim et al. (Samsung), VLSI 2003](<https://doi.org/10.1109/VLSIT.2003.1221071>) — a manufacturable embedded SONOS
  module.[^pap-03]
* [Taniguchi et al., IMW 2023](<https://doi.org/10.1109/IMW56887.2023.10145990>) — SONOS embedded flash on a 130 nm platform
  with three added masks.[^pap-05]
* [Jiew, Chien and Yung, NVMTS 2012](<https://doi.org/10.1109/NVMTS.2013.6632849>) — a 2T-SONOS cell for embedded
  flash.[^jiew-2012]
* [Sun et al., ICICDT 2011](<https://doi.org/10.1109/ICICDT.2011.5783211>) — a SONOS-based embedded flash needing "only 3
  additional non-critical masks".[^sun-2011]
* [Regis et al., ASMC 1997](<https://doi.org/10.1109/ASMC.1997.630744>) — nitride etching with high selectivity to
  oxide.[^regis-1997]
* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor and the
  size below which it rises.[^wong-1998]
* [Starikov, *Opt. Eng.* 1992](<https://doi.org/10.1117/12.56172>) — the accuracy of overlay
  measurements.[^starikov-1992]
* [van Haren et al., *Proc. SPIE* 2019](<https://doi.org/10.1117/12.2536270>) — alignment-mark placement and
  layer-to-layer overlay.[^van-haren-2019]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — mask magnification and the optical mask
  requirements of the 130 nm generation.[^itrs-03]

## Open questions

* The operation that makes the `conom` plate data, the oversize of the
  islands over the windows and what the `conom` drawing purpose 87:44
  holds are not published; the renders site's note names a "clonom.3"
  that neither the periphery rules nor the Error Messages page contains,
  and calls 87:44 a precomputed layer without a
  source.[^pdk-06][^pdk-periph][^pdk-errors][^mask-renders]
* Whether `ONOMCD` and `ONOMCDSP` are the island's own minima or values
  carried over from the tunnel layer is not stated.[^pdk-03]
* What the `ONOM` plates of MPW-2, MPW-3, MPW-4, MPW-6, MPW-7 and MPW-8
  carry is not public: no rendered die of those runs draws `tunm`, and
  the renders omit whatever the fab adds.[^steps-sheet][^mask-renders]
* The plate's tone, blank, absorber and magnification, the resist and
  any anti-reflective coating, the exposure tool and the overlay budget
  to the tunnel mask are not public.
* What the plate number `230` encodes is not stated, and no public source
  lists the `ONOM` plate of the original MPW-4 set
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
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_ONOM/`
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
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^pat-01]: K. Ramkumar, M. Rathor, B. Parameshwaran and L. Lancaster
    (Cypress Semiconductor), *Method of manufacturing an
    oxide-nitride-oxide (ONO) dielectric for SONOS-type devices*,
    US 6,969,689 B1, granted 2005-11-29.
    <https://patents.google.com/patent/US6969689B1/en>
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^cyp-26]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^pap-02]: M.-K. Seo, S.-H. Sim, M.-H. Oh, H.-S. Lee, S.-W. Kim,
    I.-W. Cho, G.-H. Kim and M.-G. Kim (Samsung), "A 130-nm 0.9-V
    66-MHz 8-Mb (256K × 32) local SONOS embedded flash EEPROM", *IEEE
    Journal of Solid-State Circuits* **40**(4), 877–883 (2005).
    <https://doi.org/10.1109/JSSC.2005.845564>
[^pap-03]: J.-H. Kim, I. W. Cho, G. J. Bae, S. S. Kim, K. C. Kim,
    S. H. Kim, K. W. Koh, N. I. Lee, H.-K. Kang, K.-P. Suh, S. T. Kang,
    M. K. Seo, S. H. Lee, M. C. Kim and I. S. Park (Samsung), "Highly
    manufacturable SONOS non-volatile memory for the embedded SoC
    solution", *2003 Symposium on VLSI Technology, Digest of Technical
    Papers*, pp. 31–32. <https://doi.org/10.1109/VLSIT.2003.1221071>
[^pap-05]: Y. Taniguchi et al., "SONOS Embedded Flash IP Using
    Trap-Depth-Controlled SiN Film Enabling Data Retention more than
    10 years at 200°C", *2023 IEEE International Memory Workshop
    (IMW)*, pp. 1–4. <https://doi.org/10.1109/IMW56887.2023.10145990>
[^jiew-2012]: C. B. Jiew, Y. E. Chien and R. T. T. Yung, "Development
    of a robust 2T-SONOS cell for embedded flash application", *2012
    12th Annual Non-Volatile Memory Technology Symposium (NVMTS)*,
    pp. 1–6. <https://doi.org/10.1109/NVMTS.2013.6632849>
[^sun-2011]: W.-T. Sun, C.-J. Liu, C.-Y. Lo, Y.-J. Ting, Y.-J. Chen,
    T.-Y. Wu, E.-H. Toh, X.-H. Yuan, K.-L. Low, Q. Han, Y.-S. You,
    Y.-K. Leung and S.-T. Woo, "Low-cost embedded Flash memory
    technology", *2011 IEEE International Conference on IC Design &
    Technology (ICICDT)*, pp. 1–5.
    <https://doi.org/10.1109/ICICDT.2011.5783211>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^wong-1998]: A. K. K. Wong, R. A. Ferguson, L. W. Liebmann,
    S. M. Mansfield, A. F. Molless and M. O. Neisser, "Lithographic
    effects of mask critical dimension error", *Proc. SPIE* **3334**, 106
    (1998). <https://doi.org/10.1117/12.310718>
[^starikov-1992]: A. Starikov, "Accuracy of overlay measurements: tool
    and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
    (1992). <https://doi.org/10.1117/12.56172>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
