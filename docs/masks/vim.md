(mask-vim)=
# VIM — Via

The via mask is the {term}`reticle` that places every connection between
metal 1 and metal 2: on the {ref}`VIM <step-118>` page's reading, the
resist printed through it at step 118 is opened over every drawn `via`,
and the {ref}`VIME <step-119>` etch cuts the holes through the
inter-metal oxide down to the metal-1 lines. At 0.150 µm its holes are
the smallest drawn holes in the flow, the step pages read it as a
critical KrF level, and it is one of the four masks whose "mask data" rule x.1a
names for its 0.001 grid. On the reading of this reference's sky130B
overview, the same mask prints the lower half of a split via 1 in that
variant of the process. This page gathers what
public sources say about the mask itself — its PDK entry and layers, the
plates the process-steps sheet records for the MPW runs, what the public
renders of those runs show, the lithography it needs and the rules that
constrain it. How the step is performed is on the step page; every mask
is indexed on the {ref}`masks index <masks-index>`.

| | VIM — Via |
|---|---|
| Mask step | {ref}`VIM <step-118>`, step 118 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Via", `VIM`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `cviam` mask 40:0, "Via mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `via` drawing 68:44, "Contact from metal 1 to metal 2"[^pdk-06] |
| Minimum CD, feature / space | `VIMCD` 0.15 / `VIMCDSP` 0.17[^pdk-03] |
| Polarity and tone | Not published. The holes are opened where `via` is drawn, which with a positive resist would make the plate dark-field (inference). |
| Exposure class | KrF (248 nm), on the step page's reading of the 0.150 µm rule and the exposure options ITRS 2001 lists for the 130 nm node, with an attenuated phase-shift plate and OPC as a further inference; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all except MPW-5[^steps-sheet] |
| Plate no. | `500`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-vim-steps>` |

## What the mask defines

The periphery rules give the function of the `via` rule set as "Defines
contact between met1 and met2", and the PDK's Table F4 names "Via" as
the layer joining metal 2 to metal 1.[^pdk-periph][^pdk-summary] The mask
carries one product feature, a square: "Min and max L and W of via
outside areaid.mt" 0.150 µm (via.1a), with "Only min. square vias are
allowed except die seal ring" (via.3).[^pdk-periph] Inside `areaid.mt`,
which `gds_layers.csv` describes as the "Location of e-test modules
within the frame", rule via.1b allows "Three sizes of square Vias": 0.150,
0.230 and 0.280 µm, each with its own metal-1 enclosure (via.4a–via.5c).
The {ref}`VIM <step-118>` page reads the larger sizes as confined to test
structures.[^pdk-periph][^pdk-06] The PDK's extraction table lists "VIA"
at 4500 in a column headed "Resistivity (mohms/sq)", against 152000 for
"MCON contact";[^pdk-08] the step page reads these as 4.5 Ω and 152 Ω per
plug.

`VIM` has no column in the PDK's mask generation table, Table F2b, which
has none for any via level, so the table says nothing about which
devices create it.[^pdk-06] The mask does not define the metal-1 landing
lines ({ref}`mask-mm1`) or the metal-2 lines that cover the vias (`MM2`),
nor the liner and tungsten plug that fill the holes
({ref}`TIN3 <step-120>` to {ref}`WCMP3 <step-122>`), which on the step
pages' readings take the etched hole, not this resist, as their shape.

In the sky130B variant, on the reading of the
{ref}`overview-sky130b-reram` page, SkyWater's mask-layer slide keeps
`cviam` for the lower vias of a via 1 split by the ReRAM tier and adds
`r1c`, the cell, and `r1v`, the upper vias, above it; both via masks come
from the one drawn `via` layer. The
process-steps sheet records plates for the two added masks, `RRM` and
`VIMC`, on most of MPW-1 to MPW-8 ({ref}`masks-mpw-runs`); neither has a
step in the step list used here.[^steps-sheet]

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `cviam` a single purpose, `mask` at 40:0 ("Via
mask"), with no `drawing`, `mask add`, `mask drop` or `waffle drop`
purpose; the drawn layer is `via` at 68:44.[^pdk-06] The pairing rests on
those names and descriptions, as on the
{ref}`masks index <masks-index>`, and the PDK publishes no operation from
`via` to the plate. With no add or drop purpose, rule x.9's "serifs" have
no `cviam` layer to sit on, and rule x.15a confines mask layers to test
modules, seal ring and frame, with the exception that "FOM/P1M/Metal
waffle drop are allowed inside the die" (flag P, periphery
only);[^pdk-periph] a design inside the die therefore draws `via` (our
reading of x.9 and x.15a).

Rule x.1a names this mask's data: "mask data for p1m, met1, via, met2
must be on a grid of mm" with the value 0.001, against 0.005 for "all
layers except those mentioned in 1a" (x.1b).[^pdk-periph] Reading the
unit as µm, a 1 nm wafer grid is a 4 nm grid on a 4× plate (our
arithmetic); Samuels, Maurer and Farrell examined "how fine a grid size
is needed in the manufacture of the mask" once OPC is
applied.[^samuels-1995] The PDK does not say why the via data need the
finer grid. Table 4 of *Criteria & Assumptions* adds a "min. etch and
fill capability for via" of 0.18 (`VEFC`) and a "Via1 slope" of 0.02 (`Via1Slope`), both in a
column headed "Value (um)" and neither explained; a slope given in µm
is itself unexplained.[^pdk-03]

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `VIM` the site renders layer 68:44 (`via`)
alone, with no Boolean expression and no fill layer, on all eight runs;
its mask record gives the mask-level layer 40:0, the info text "Via 1
(M1→M2)" and the note "in the sky130B RRAM tier this is cviam, the lower
half of the split via1; the upper half is VIMC (r1v)".[^mask-renders] The
note and the choice of layer are one public derivation from the drawn
data, not SkyWater's mask-generation recipe; the site renders `VIMC` as
`via` AND 201:20, so on the dies that draw the ReRAM layer the `VIM`
image includes the vias that its `VIMC` image repeats (our reading of the
two layer choices)
({ref}`masks-derivations`). The sheet's "Info" note for the `VIM` row has
the same level name, and its `VIMC` note has "(via_bot = cviam = VIM)", close to
the site's "via_bot (cviam = VIM)"; the two sources share this wording, so neither is cited as corroborating
the other ({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders]

Every rendered die of every run carries `via` shapes — at least
1 207 081 on each die[^mask-renders] — so the count of 40 dies says only
that every layout joins metal 1 to metal 2. For MPW-5 the renders show
shapes on all 40 dies although the sheet records no `VIM` plate for that
run, which fits the masks index's reading of the gap as one in the
record, but the renders show the drawn layouts, not the plates
({ref}`masks-mpw-runs`).[^mask-renders][^steps-sheet] The site states the
limits of its images: "These are renders of *drawn* data, not photomask
artwork: reticle pitch, 4x reduction, mirroring and the frame features
the fab adds are not modelled."[^mask-renders] The metadata carries no
plate ID, and the MPW-4 renders come from a different reticle set from
the one whose plates the sheet records ({ref}`masks-mpw-reticle-sets`).

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `VIM` plate as
existing on seven runs, with the plate number `500` on each, and has no
mark or plate ID for MPW-5.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA500A` |
| MPW-2 | `5CS8007AC` | `S8007AA500A` |
| MPW-3 | `5CS8008AC` | `S8008AA500A` |
| MPW-4 | `5CS8018AC` | `S8018AA500A` |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA500A` |
| MPW-7 | `5CS8016AC` | `S8016AA500A` |
| MPW-8 | `5CS8017AC` | `S8017AA500A` |

* **MPW-5.** The sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5 and gives no reason. The masks index reports
  what is recorded and does not conclude that the plate was absent from
  MPW-5: it reads a gap in the record as the likelier explanation, since
  every working die needs these masks (inference)
  ({ref}`masks-mpw-runs`).[^steps-sheet] The sky130B `VIMC` plate, by
  contrast, is recorded for MPW-5.[^steps-sheet]
* **Plate number.** The sheet does not say what `500` encodes. It falls
  between `455` for `VIMC` and `550` for `MM2`, but the numbers do not
  follow process order elsewhere, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives a type for the via 2, via
  3 and via 4 plates but none for `VIM`.[^steps-sheet] The
  {ref}`VIM <step-118>` page reads the plate as an
  {term}`attenuated phase-shift mask <attenuated PSM>` with OPC, the type
  the masks index reads in the via-2 and via-3 codes; for via 1 it is not
  on public record. 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

**Exposure class.** The {ref}`VIM <step-118>` page gives
{math}`k_1 = 0.15 \times 0.70 / 0.248 \approx 0.42` on a KrF lens of NA
0.70 and 0.48 at NA 0.80, and infers a 248 nm level from the rule and
from ITRS 2001, which lists "248 nm + PSM" and "193 nm" as the exposure
options for the 130 nm node and says that "only 248 nm lithography has a
mature infrastructure";[^itrs-03] the
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there.
SkyWater lists "ASML DUV stepper" and "ASML DUV scanner" but assigns no
layer to them.[^skw-01] ITRS 2001 names "attenuated shifter and
alternating aperture" as the primary phase-shift mask choices for
critical layers.[^itrs-03]

**Mask errors.** Wong et al. found the mask error factor rising "rapidly
when the critical dimension (CD) is less than […] 0.75 (lambda) /NA for
contacts";[^wong-1998] at 248 nm and NA 0.7 that is about 0.27 µm (our
arithmetic), about 1.8 times the 0.150 µm via, so plate CD errors would
print magnified (inference). Kim et al. found the factor rising near the
resolution limit, larger for dense than for isolated contacts and smaller
on attenuated masks than on binary ones, because the attenuated plates
carry a positive bias "in order to reduce the sidelobe
printing".[^kim-1999] ITRS 2001
asks in 2001 for a mask CD uniformity of 8.0 nm (3σ) on contacts and
vias at 4× magnification, requirements that are "for critical
layers".[^itrs-03] How tightly SkyWater specifies the `VIM` plate is not
public.

**Side lobes.** Ma and Andersson describe side-lobe printing, "caused by
constructive interference of the first order of diffraction maximum from
nearby features, plus the electrical fields from semi-transparent
materials in the surrounding area", as "One major limitation of applying
attenuated phase shift mask", show how defocus, lens aberration and
layout affect it, and present an attenuated rim-shifter plate to prevent
it.[^ma-andersson-1998] Iwasaki, Hoshi and Tanabe compared high- and
standard-transmittance attenuated plates for 0.15 µm hole patterns, both
with rim structures "to eliminate side lobes", and found both "high
enough for 0.15 micrometers hole patterns".[^iwasaki-1998] Chen, Wang
and Chu characterised the process latitude of an attenuated mask for
contact holes, including the mask-to-wafer CD bias.[^chen-1999-psm]
Whether the `VIM` plate is attenuated, rimmed or binary is not public.

**Proximity and size.** For holes below 0.2 µm, Yamamoto et al. note,
"2-dimensional correction is required".[^yamamoto-2000] The PDK's
0.18 "min. etch and fill capability for via", larger than the drawn
0.150 µm,[^pdk-03] is read on the {ref}`VIM <step-118>` page as the
qualified fill size after the etch's positive bias, an inference;
Toyoshima et al. showed the opposite route, shrinking KrF resist holes
chemically after develop.[^toyoshima-1998] Le, Banerjee and McPherson
found that via size strongly affects the electromigration failure-time
spread of tungsten-plug vias for one direction of electron flow with a
TiN-capped metallisation, and not for the other,[^le-1996] one reason
the printed size matters.

**Substrate and tone.** The resist sits on a thin oxide over patterned
metal, so the reflection under it changes with the metal pattern (the
step page's reading). Brunner showed that the swing ratio scales with the
square root of the substrate reflectivity, which an anti-reflective
coating reduces.[^brunner-1991] The step page reads a positive chemically
amplified KrF resist over an organic {term}`BARC`; with the holes opened
where `via` is drawn, the plate would be dark-field: clear squares in an
opaque field (inference). Neither is published. The consumables are on
the {ref}`lithography materials <material-lithography-materials>` page.

**Pattern transfer.** On the step pages' readings the holes are etched at
{ref}`VIME <step-119>` through the cap oxide and inter-metal oxide, 0.27
µm in the PDK's stack diagram,[^pdk-04] on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>` class,
down to the TiW cap of the metal-1 lines, and the resist is stripped
within that step.

**Overlay.** Metal 1 must enclose a 0.150 µm via by 0.055 µm (via.4a),
and by 0.085 µm on one of two adjacent sides (via.5a); metal 2 above it
by the same 0.055 µm (m2.4) and 0.085 µm (m2.5).[^pdk-periph] The
{ref}`VIM <step-118>` page reads the mask as aligned to the metal-1
pattern and names the 0.055 µm enclosure as "the registration that
matters".

(mask-vim-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `VIM` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`VIM <step-118>`, {ref}`VIME <step-119>`

* {ref}`VIM <step-118>` — coats, exposes and develops the resist.
* {ref}`VIME <step-119>` — etches the via holes through the resist; the
  step list used in this reference has no separate strip step, and the
  step page treats the resist strip and post-etch clean as part of the
  etch.

On its step page's reading, the next step, {ref}`TIN3 <step-120>`,
sputters a titanium nitride liner into the cleaned holes, and the next
mask step is {ref}`MM2 <step-124>`. The rule needs no exception for this
mask; the liner, tungsten fill and plug polish that follow do not use the
resist.

## Design rules and critical dimensions

The `via` rules of the periphery rules, with the metal-2 enclosures of
the via and the mask-data rules x.1a, x.1b, x.2, x.7, x.15a and x.18. Flag
P means "Rule applies to periphery only (outside areaid.ce). A
corresponding core rule may or may not exist.", AL "Rules applicable only
to Al BE flows", CU "Rules applicable only to Cu BE flows", IR "IR drop
check compering Al database and slotted Cu database for the same product
(2 gds files) must be clean", RR "Recommended rule at any IP level" and
NC "Rule not checked by DRC. It should be used as a guideline
only."[^pdk-periph]

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| via.1a | "Min and max L and W of via outside areaid.mt" (AL) | 0.150 µm |
| via.1b | "Three sizes of square Vias allowed inside areaid:mt: 0.150um, 0.230um and 0.280um" (AL) | — |
| via.2 | "Spacing of via to via" (AL) | 0.170 µm |
| via.3 | "Only min. square vias are allowed except die seal ring where vias are (Via CD)\*L" | 0.2\*L |
| via.4a | "0.150 µm Via must be enclosed by Met1 by at least …" | 0.055 µm |
| via.4b | "Inside areaid.mt, 0.230 µm Via must be enclosed by met1 by atleast" (AL) | 0.030 µm |
| via.4c | "Inside areaid.mt, 0.280 µm Via must be enclosed by met1 by atleast" (AL) | 0.000 µm |
| via.5a | "0.150 µm Via must be enclosed by Met1 on one of two adjacent sides by at least …" | 0.085 µm |
| via.5b–5c | The same one-side enclosure for the 0.230 µm and 0.280 µm vias inside `areaid.mt` (AL) | 0.060, 0.000 µm |
| via.11–via.14a | For copper flows: via size 0.180 µm, spacing 0.130 µm, "Max of 5 vias within …" 0.350 µm, and metal-1 enclosures (CU) | 0.180, 0.130, 0.350, 0.040, 0.037 |
| via.irdrop.1–4 | For 1 to 2, 3 to 15, 16 to 30 and more than 30 vias "on the same connector", "mcon area pre- and post- Cu conversion must differ by no more than…" (CU IR) | 0.0, 0.6, 0.8, 0.9 µm |
| m2.4 | "Via must be enclosed by Met2 by at least …" (P AL) | 0.055 µm |
| m2.5 | "Via must be enclosed by Met2 on one of two adjacent sides by at least …" (AL) | 0.085 µm |
| m2.15 | "Via must be enclosed by met2 by at least…" (CU) | 0.040 µm |
| capm.8 | "Min space, no overlap, between via and capm" | N/A |
| x.1a | "p1m.md (OPC), DECA and AMKOR layers (pi1.dg, pmm.dg, rdl.dg, pi2.dg, ubm.dg, bump.dg) and mask data for p1m, met1, via, met2 must be on a grid of mm" | 0.001 (unit "mm") |
| x.1b | "Data for SKY130 layout and mask on all layers except those mentioned in 1a must be on a grid of mm (except inside Seal ring)" | 0.005 (unit "mm") |
| x.2 | "Angles permitted on: tap (except inside areaid.en), poly […], li1(periphery), licon1, capm, mcon, via, via2. Anchors are exempted." | n x 90 deg |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.18 | "Use redundant mcon, via, via2, via3 and via4 […]" (RR) | — |

Table 2 of *Criteria & Assumptions* repeats the size and space as
`VIMCD` 0.15 and `VIMCDSP` 0.17, and gives 0.18 and 0.13 for a "Via -
Cu" row (`VIM_CuCD`, `VIM_CuCDSP`), the values of the copper rules via.11
and via.12, for a back end SKY130's aluminium flow does not
use.[^pdk-03][^pdk-periph] Via.3 gives the seal-ring via width as
"0.2\*L" where via.1a gives 0.150 µm, and the irdrop rules speak of "mcon
area" although they are via rules; the PDK explains neither. The summary
Table F3c, "Back end layers for S8D\* flow", repeats the via as 0.150 wide on a 0.170 space, enclosed by
metal 1 and by metal 2 by "0.055 / 0.085".[^pdk-summary] For the plate
the decisive figures are one 0.150 µm square on a 0.32 µm pitch (our
arithmetic from via.1a and via.2), the smallest hole in the flow.

## Related pages

* {ref}`VIM <step-118>` and {ref}`VIME <step-119>` — the mask step and
  the via etch; {ref}`TIN3 <step-120>` — the liner that follows.
* {ref}`mask-mm1` — the metal-1 mask the vias land on; {ref}`mask-ctm1`
  — the contact mask one level down.
* {ref}`overview-sky130b-reram` — the ReRAM tier that splits via 1 in
  sky130B.
* {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.
* {ref}`machine-duv-krf-stepper` — the exposure class the step page
  assigns.
* {ref}`machine-plasma-etcher-dielectric` — the etch class that transfers
  the pattern.
* {ref}`machine-cd-sem-overlay-metrology` — hole CD and overlay
  measurement.
* {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Via, VIM, X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `via` 68:44,
  `cviam` 40:0, `areaid.mt` and the columns of Table F2b.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `VIMCD`/`VIMCDSP`,
  `VIM_CuCD`/`VIM_CuCDSP`, `VEFC` and `Via1Slope`.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `via` rules, m2.4, m2.5, m2.15,
  capm.8, x.1a, x.1b, x.2, x.7, x.9, x.15a, x.18 and the flag
  legend.[^pdk-periph]
* SkyWater PDK, *Summary of Key Periphery Rules* — Tables F3c and
  F4.[^pdk-summary]
* SkyWater PDK, *Process stack diagram* — the 0.27 µm via-1
  height.[^pdk-04]
* SkyWater PDK, *Parasitic Layout Extraction* — the contact and via
  resistance table.[^pdk-08]
* *S8 / SKY130 Process Steps* sheet — the step, the `VIM` plates of
  MPW-1 to MPW-8, the "Info" notes and the mask-type tab.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the `VIM` renders, their layer,
  note and info text, and the per-die shape counts.[^mask-renders]
* SkyWater, *Facilities & Capabilities* — the DUV exposure
  tools.[^skw-01]

### High-level understanding

* Wikipedia, *Via (electronics)* — what a via is.[^wiki-via]
* Wikipedia, *Photomask* and *Phase-shift mask* — binary and attenuated
  plates.[^wiki-mask][^wiki-psm]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography* — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* Wong et al. (IBM), *Proc. SPIE* 1998 — the mask error factor of
  contacts and the size below which it rises.[^wong-1998]
* Kim et al., *Proc. SPIE* 1999 — mask CD error for sub-quarter-micron
  contact holes on binary and attenuated masks.[^kim-1999]
* Ma and Andersson, *Proc. SPIE* 1998 — the cause of side-lobe printing
  with attenuated plates and a rim-shifter remedy.[^ma-andersson-1998]
* Iwasaki, Hoshi and Tanabe, *Proc. SPIE* 1998 — rim-type attenuated
  plates for 0.15 µm hole patterns.[^iwasaki-1998]
* Chen, Wang and Chu, *Proc. SPIE* 1999 — process latitude and CD bias
  of an attenuated mask for contact holes.[^chen-1999-psm]
* Yamamoto et al., MNC 2000 — two-dimensional, hierarchical OPC on
  contact-hole layers.[^yamamoto-2000]
* Samuels, Maurer and Farrell, *Proc. SPIE* 1995 — OPC, mask CD
  tolerance and mask grid size.[^samuels-1995]
* Toyoshima et al. (Mitsubishi), IEDM 1998 — chemical shrink (RELACS) of
  KrF resist holes.[^toyoshima-1998]
* Brunner, *Proc. SPIE* 1991 — the swing ratio and anti-reflective
  coatings.[^brunner-1991]
* Le, Banerjee and McPherson (TI), *Semicond. Sci. Technol.* 1996 — via
  size and tungsten-plug via electromigration.[^le-1996]
* ITRS 2001, *Lithography* — contact and via mask requirements for
  critical layers at 130 nm.[^itrs-03]

## Open questions

* The operation that makes the `cviam` plate data from `via` is not
  published, nor, for sky130B, how the lower and upper via masks are
  separated from the one drawn layer.[^pdk-06]
* The plate's type (binary, attenuated or rimmed), tone and CD
  specification, the resist and the exposure tool are not public; the
  KrF reading rests on the 0.150 µm rule.
* The PDK does not explain why the "min. etch and fill capability for
  via" (0.18) exceeds the drawn via, what the "Via1 slope" of 0.02, printed in a µm
  column, measures, or why via.3 gives "0.2\*L".[^pdk-03][^pdk-periph]
* Whether the absent MPW-5 record is a gap in the record or a difference
  in the run is not stated,[^steps-sheet] and no public source lists the `VIM` plate of the
  original MPW-4 set `5CS8010AC`.[^mask-renders]
* The sheet and the renders site give both `CTM1` and `VIM` the level
  name "Via 1"; neither explains it.[^steps-sheet][^mask-renders]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tabs "Sheet1" (step number, code and description), "Masks"
    (mask steps with step numbers), "Run Mask IDs" (the mask table set
    against MPW-1 to MPW-8, with "Exists", "Plate ID" and "Info" columns)
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
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2 and
    4), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Tables F3c and F4), SkyWater SKY130 PDK documentation, retrieved
    2026-09-13.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_VIM/`
    directory with its page, `job.json`, `result.json` and per-die slot
    JSON files, retrieved 2026-09-13. Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-via]: Wikipedia, *Via (electronics)*.
    <https://en.wikipedia.org/wiki/Via_(electronics)>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-psm]: Wikipedia, *Phase-shift mask*.
    <https://en.wikipedia.org/wiki/Phase-shift_mask>
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
[^kim-1999]: H.-E. Kim, J.-S. Chun, S. Barnett and J. Shih, "Effect of
    mask critical dimension error for subquarter-micron contact hole",
    *Proc. SPIE* **3679**, 821 (1999).
    <https://doi.org/10.1117/12.354400>
[^ma-andersson-1998]: Z. M. Ma and A. Andersson, "Preventing sidelobe printing in
    applying attenuated phase-shift reticles", *Proc. SPIE* **3334**,
    Optical Microlithography XI, 543 (1998).
    <https://doi.org/10.1117/12.310783>
[^iwasaki-1998]: H. Iwasaki, K. Hoshi and H. Tanabe, "High-transmittance
    rim-type attenuated phase-shift masks for sub-0.2-μm hole patterns",
    *Proc. SPIE* **3412**, Photomask and X-Ray Mask Technology V, 601
    (1998). <https://doi.org/10.1117/12.328842>
[^chen-1999-psm]: Y.-T. Chen, Y.-C. Wang and R. Chu, "Optimization of
    attenuated phase-shift mask for contact hole printing", *Proc.
    SPIE* **3679**, Optical Microlithography XII, 812 (1999).
    <https://doi.org/10.1117/12.354399>
[^yamamoto-2000]: K. Yamamoto, S. Kobayashi, T. Uno, T. Kotani et al.,
    "Hierarchical optical proximity correction on contact hole layers",
    *Digest of Papers, Microprocesses and Nanotechnology 2000*,
    pp. 40–41. <https://doi.org/10.1109/IMNC.2000.872612>
[^samuels-1995]: D. J. Samuels, W. Maurer and T. R. Farrell, "Good OPC,
    where will this drive mask CD tolerance and mask grid size", *Proc.
    SPIE* **2621**, 15th Annual BACUS Symposium on Photomask Technology
    and Management, 588–596 (1995). <https://doi.org/10.1117/12.228213>
[^toyoshima-1998]: T. Toyoshima, T. Ishibashi, A. Minanide, K. Sugino
    et al., "0.1 μm level contact hole pattern formation with KrF
    lithography by resolution enhancement lithography assisted by
    chemical shrink (RELACS)", *IEDM 1998 Technical Digest*,
    pp. 333–336. <https://doi.org/10.1109/IEDM.1998.746367>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^le-1996]: H. A. Le, K. Banerjee and J. W. McPherson, "The dependence of
    W-plug via EM performance on via size", *Semiconductor Science and
    Technology* **11**(6), 858–864 (1996).
    <https://doi.org/10.1088/0268-1242/11/6/003>
