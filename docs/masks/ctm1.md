(mask-ctm1)=
# CTM1 — Contact

The contact mask is the {term}`reticle` that places every connection
from the {term}`local interconnect` (titanium nitride on the
{ref}`LITIN <step-101>` page's reading) up to metal 1. On
the {ref}`CTM1 <step-107>` page's reading, the resist printed through it
at step 107 is opened over every drawn `mcon`, and the
{ref}`CTME <step-108>` etch cuts the holes through the planarised oxide
down to the local interconnect.

| | CTM1 — Contact |
|---|---|
| Mask step | {ref}`CTM1 <step-107>`, step 107 of 171[^steps-sheet] |
| PDK mask (`masks.csv`) | "Contact", `CTM1`, marked `X` in `Used in SKY130`[^pdk-05] |
| Mask-level layer (`gds_layers.csv`) | `ctm1` mask 35:0, "Contact mask"[^pdk-06] |
| Drawn layer (`gds_layers.csv`) | `mcon` drawing 67:44, "Contact from local interconnect to metal1" (inference: the masks index pairs `ctm1` with `mcon` because `licon1` corresponds to `LICM1`)[^pdk-06] |
| Minimum CD, feature / space | `CTM1CD` 0.17 / `CTM1CDSP` 0.19[^pdk-03] |
| Polarity and tone | Not published. The holes are opened where `mcon` is drawn, which with a positive resist would make the plate dark-field (inference). |
| Exposure class | KrF (248 nm), on the step page's reading of the 0.17 µm rule and the exposure options ITRS 2001 lists for the 130 nm node, with an attenuated phase-shift plate and OPC as a further inference; no public source names the tool ({ref}`machine-duv-krf-stepper`) |
| Mask type (process-steps sheet) | None recorded; the sheet codes a type for the via 2, via 3 and via 4 plates only[^steps-sheet] |
| Plates recorded | all except MPW-5[^steps-sheet] |
| Plate no. | `400`[^steps-sheet] |
| Dies with shapes, MPW-1 to MPW-8 (renders) | 40 on every run[^mask-renders] |
| Steps that use the pattern | 2 steps; see {ref}`Steps that use this mask <mask-ctm1-steps>` |

:::{seealso}
How the step is performed is on
the step page; every mask is indexed on the
{ref}`masks index <masks-index>`.
:::

## What the mask defines

The mask is the first mask of the
{term}`BEOL` and the second of the flow's three hole layers, and its
size and spacing rules are the only periphery rules the PDK flags as not
reflecting "the final dimension on silicon".

The periphery rules give the function of the `ct` rule set as "Defines
contact between Li1 and met1", and the PDK's Table F4, "Connectivity of
Drawn and Mask Layers", names "Mcon" as the layer joining met1 to
`li1`.[^pdk-periph][^pdk-summary] The mask carries one feature, a
square: "Min and max L and W of mcon" 0.170 µm (ct.1), and "Only min.
square mcons are allowed except die seal ring" (ct.3).[^pdk-periph]
Wide connections are therefore arrays of squares, and rule x.18, flagged
as recommended, asks designers to "Use redundant mcon, via, via2, via3
and via4".[^pdk-periph]

The PDK's extraction table lists "MCON contact"
at 152000 against 15000 for "LICON contact" and 4500 for "VIA", in a
column headed "Resistivity (mohms/sq)".[^pdk-08] The
{ref}`CTM1 <step-107>` page reads these as 152 Ω, 15 Ω and 4.5 Ω per
contact, and the contact size this mask sets as one reason the figure is
high.

Unlike `LICM1` and the metal masks, `CTM1` has no column in the PDK's
mask generation table, Table F2b, which has none for any via level
either, so it says nothing about which devices create
`CTM1`.[^pdk-06] One device rule counts the contacts directly: "Every
pwres_terminal must enclose 12 mcons if routed through metal1"
(pwres.7b).[^pdk-periph]

The drawn layer is an inference. `gds_layers.csv` names the mask-level
layer "Contact mask" and the drawn `mcon` "Contact from local
interconnect to metal1", and the {ref}`masks index <masks-index>` pairs
the two because the other contact layer, `licon1`, belongs to
`LICM1`.[^pdk-06] The mask does not define the local-interconnect pads
it lands on ({ref}`mask-li1m`) or the metal-1 lines that must cover it
(`MM1`), nor the liner and tungsten plug that fill the holes
({ref}`TIN2 <step-109>` to {ref}`WCMP2 <step-111>`). On the step
pages' readings the liner and tungsten plug take the etched hole, not this resist, as their shape.

## Drawn layers and derivation

### In the PDK

`gds_layers.csv` gives `ctm1` a single purpose, `mask` at 35:0 ("Contact
mask"), with no `drawing`, `mask add`, `mask drop` or `waffle drop`
purpose; the drawn layer is `mcon` at 67:44.[^pdk-06] With no add or
drop purpose, rule x.9's "serifs" have no `ctm1` layer to sit on, and
rule x.15a confines mask layers to test modules, seal ring and frame,
with the exception that "FOM/P1M/Metal waffle drop are allowed inside the
die" (flag P, periphery only).[^pdk-periph] A design inside the die
therefore draws `mcon` (our reading of x.9 and x.15a).

The `CTM1` mask
data are not among those rule x.1a names for the 0.001 grid ("mask data
for p1m, met1, via, met2"), so they fall under x.1b's 0.005 (our
reading; both values are printed with the unit "mm").[^pdk-periph]

The PDK says in so many words that the drawn contact is not the printed
one. Rules ct.1 and ct.2 carry the flag DNF, "Drawn Not equal Final. The
drawn rule does not reflect the final dimension on silicon. See table J
for details.".[^pdk-periph] No table J is among the files of the
PDK's rules documentation (our search of its file list). Rules ct.1 and ct.2 are the
only rules in the periphery rules with that flag.

The criteria give
the other end: a "Standard contact bottom CD" of 0.09 in Table 5, the
laser-fuse criteria, and a "min. etch and fill capability for mcon" of
0.14 (`CEFC`) in Table 4.[^pdk-03] The {ref}`CTM1 <step-107>` page reads
the 0.09 as the generic finished profile and leaves open whether it
applies to every `mcon`. The PDK does not say whether the plate carries
a bias, or whether the difference comes from the etch taper.

### In the public renders

The public mask-layer renders show, for each of MPW-1 to MPW-8, the
shapes the 40 tape-out layouts of the run draw on the layers the site
assigns to each mask. For `CTM1` the site renders layer 67:44 (`mcon`)
alone, with no Boolean expression and no fill layer, on all eight
runs.[^mask-renders] Its mask record gives the mask-level layer 35:0, the note "CTM1 = mcon
(li1->met1)" and the info text "Via 1 (LI/M0→M1)".[^mask-renders]

The
site uses the same drawn layer as this reference's inference, but both
derive from the same public files, so the agreement is not independent
confirmation ({ref}`masks-derivations`). The note and the choice of
layer are one public derivation from the drawn data, not SkyWater's
mask-generation recipe.

The info text is identical to the "Info" note of
the `CTM1` row in the process-steps sheet, one of the level names the two
sources share, so neither is cited as corroborating the other
({ref}`masks-renders-sheet-notes`).[^steps-sheet][^mask-renders] Both also call the `VIM` level "Via 1
(M1→M2)", and neither says why two levels share the name "Via
1".[^steps-sheet][^mask-renders]

Every rendered die of every run carries `mcon` shapes — at least
5 562 247 on each die[^mask-renders] — so the count of 40 dies says only
that every layout reaches metal 1, as every working die must. For MPW-5
the renders show shapes on all 40 dies although the sheet records no
`CTM1` plate for that run, which fits the masks index's reading of the
gap as one in the record, but the renders show the drawn layouts, not
the plates ({ref}`masks-mpw-runs`).[^mask-renders][^steps-sheet]

The site
states the limits of its images: "These are renders of *drawn* data, not
photomask artwork: reticle pitch, 4x reduction, mirroring and the frame
features the fab adds are not modelled."[^mask-renders] They therefore
show the drawn 0.17 µm squares, not the final dimension the DNF flag
refers to (inference from that statement). The metadata carries no plate
ID, and the MPW-4 renders come from a different reticle set from the one
whose plates the sheet records ({ref}`masks-mpw-reticle-sets`).

## Plates and reticle sets

The "Run Mask IDs" tab of the process-steps sheet marks a `CTM1` plate
as existing on seven runs, with the plate number `400` on each, and has
no mark or plate ID for MPW-5.[^steps-sheet] The plate IDs below are the
sheet's; the reticle set is the heading of the run's columns in the tab
({ref}`masks-mpw-reticle-sets`).[^steps-sheet]

| Run | Reticle set (sheet column heading) | Plate ID |
|-----|------------------------------------|----------|
| MPW-1 | `7CS8M06AC` | `S8M06AA400A` |
| MPW-2 | `5CS8007AC` | `S8007AA400A` |
| MPW-3 | `5CS8008AC` | `S8008AA400A` |
| MPW-4 | `5CS8018AC` | `S8018AA400A` |
| MPW-5 | `5CS8011AC` | none recorded |
| MPW-6 | `5CS8014AC` | `S8014AA400A` |
| MPW-7 | `5CS8016AC` | `S8016AA400A` |
| MPW-8 | `5CS8017AC` | `S8017AA400A` |

* **MPW-5.** The sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5 and gives no reason. The masks index reports
  what is recorded and does not conclude that the plate was absent from
  MPW-5: it reads a gap in the record as the likelier explanation, since
  every working die needs these masks (inference)
  ({ref}`masks-mpw-runs`).[^steps-sheet]
* **Plate number.** The sheet does not say what `400` encodes. It falls
  between `370` for `LI1M` and `450` for `MM1`, with `430` for the
  sky130B `RRM` mask between them, but the numbers do not follow process
  order elsewhere, so no process position is read from it
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet]
* **Mask type.** The sheet's "Sheet4" tab gives no type for
  `CTM1`.[^steps-sheet] The {ref}`CTM1 <step-107>` page reads the plate as
  an {term}`attenuated phase-shift mask <attenuated PSM>` with OPC; that
  is not on public record. 4× is the ITRS 2001 mask magnification for the
  130 nm generation.[^itrs-03]
* **MPW-4.** The sheet's MPW-4 plate is from the set `5CS8018AC`; the
  renders are from the original set `5CS8010AC`
  ({ref}`masks-mpw-reticle-sets`).[^steps-sheet][^mask-renders]

## Lithography and pattern transfer

### Exposure class

The {ref}`CTM1 <step-107>` page gives
{math}`k_1 = 0.17 \times 0.70 / 0.248 \approx 0.48` for the hole on a
KrF lens of NA 0.7, "comfortable for lines but not for isolated holes,
whose depth of focus is much smaller", and infers a 248 nm level from
the rule and from ITRS 2001.[^itrs-03]

ITRS 2001 lists "248 nm + PSM" and "193 nm" as
the exposure options for the 130 nm node and says that "only 248 nm
lithography has a mature infrastructure".[^itrs-03] The
{ref}`KrF stepper <machine-duv-krf-stepper>` page lists it there. SkyWater
lists "ASML DUV stepper" and "ASML DUV scanner" but assigns no layer to
them.[^skw-01]

For the era's hole-printing toolkit the step page names
attenuated plates, contact-specific resists, assist features and
focus-latitude techniques:

* Lu et al. evaluated contact-hole resists on
  an attenuated mask and found "for most of resists, the process windows
  are limited by unwanted sidelobe printing through focus".[^lu-1999]
* Fukuda et al.'s FLEX, multiple exposures "in several different focal
  planes", "is especially effective when applied to small isolated
  transparent patterns like contact holes".[^fukuda-1987]
* Socha et al.
  placed assist features by interference mapping for low-{math}`k_1`
  holes.[^socha-2004]

### Mask errors

Wong et al. found the mask error factor rising "rapidly
when the critical dimension (CD) is less than […] 0.75 (lambda) /NA for
contacts".[^wong-1998] At 248 nm and NA 0.7 that is about 0.27 µm (our
arithmetic), above the 0.17 µm `mcon`, so plate CD errors would print
magnified (inference). Kim et al. found the factor rising near the
resolution limit and larger for dense than for isolated
contacts.[^kim-1999]

ITRS 2001 notes that "contacts have very small
process windows and large mask error factors", and asks in 2001 for a
mask CD uniformity of 8.0 nm (3σ) on contacts and vias at 4×
magnification, requirements that are "for critical
layers".[^itrs-03] Choo et al. printed 0.16 µm holes at
{math}`k_1` 0.44 with a 6 % attenuated mask whose hole patterns were
biased by 0.04 to 0.08 µm.[^choo-2000]

### Defects on the plate

A defect on a hole plate is judged by what it
does to the hole. Takeuchi and Miyahara found size alone a vague criterion
for KrF halftone contact-hole reticles, proposed a defect-area-ratio
method, and derived reticle defect specifications from the wafer CD
budget that were "too tight to be met with current reticle inspection
machines".[^takeuchi-1999] Whether the `CTM1` plate is a halftone
(attenuated) plate is not public.

### Drawn and final size

The DNF flag on ct.1 and ct.2 and the 0.09
"Standard contact bottom CD"[^pdk-periph][^pdk-03] fit the practice ITRS
2001 describes for the node, in which "contact hole size after etch will
be smaller than the lithographically imaged hole".[^itrs-03] Toyoshima
et al. shrank KrF resist holes to the 0.1 µm level with a chemical shrink
(RELACS),[^toyoshima-1998] one route the step page names as possible but
unconfirmed.

### Resist and tone

The step page reads a positive chemically amplified
KrF resist over an organic anti-reflective coating; with the holes
opened where `mcon` is drawn, the plate would be dark-field: clear squares
in an opaque field (inference). Neither is published. The consumables are
on the {ref}`lithography materials <material-lithography-materials>`
page.

### Overlay and alignment

The contact needs no enclosure by the local interconnect
(ct.4, 0.000 µm), while metal 1 must enclose it by 0.030 µm (m1.4) and
by 0.060 µm on one of two adjacent sides (m1.5).[^pdk-periph] Table 4
nevertheless gives a "Minimum mcon overlap onto LI for reproducible
contact resistance" of 0.12 (`TCONOVLP`).[^pdk-03] The
{ref}`CTM1 <step-107>` page reads alignment to the {ref}`LI1M <step-102>`
pattern as "the critical registration of the layer".

### Pattern transfer

On the step pages' readings the holes are etched at
{ref}`CTME <step-108>` through about 0.34 µm of oxide and nitride cap
down to the local interconnect, on the
{ref}`dielectric plasma etcher <machine-plasma-etcher-dielectric>` class,
and the resist is stripped within that step; the next step,
{ref}`TIN2 <step-109>`, lines the holes.

(mask-ctm1-steps)=
## Steps that use this mask

The steps listed are the mask step and the consecutive steps after it,
up to the next mask step, that the step pages read as using its resist
pattern — the row of the *Patterns* column for `CTM1` on the
{ref}`masks index <masks-index>`.

Steps:

{ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`

* {ref}`CTM1 <step-107>` — coats, exposes and develops the resist.
* {ref}`CTME <step-108>` — etches the contact holes through the resist;
  the step list used in this reference has no separate strip step, and
  the step page treats the resist strip and post-etch clean as part of
  the etch.

On its step page's reading, the next step, {ref}`TIN2 <step-109>`,
sputters a titanium nitride liner into the cleaned holes, and the next
mask step is {ref}`MM1 <step-113>`. The rule needs no exception for this
mask; the liner, tungsten fill and plug polish that follow do not use the
resist.

## Design rules and critical dimensions

The `ct` rules of the periphery rules, with the metal-1 enclosures of
`mcon` and the rules of other sets that count or constrain contacts.

Flag DNF means "Drawn Not equal Final. The drawn rule does not reflect
the final dimension on silicon. See table J for details.", P "Rule
applies to periphery only (outside areaid.ce). A corresponding core rule
may or may not exist.", AL "Rules applicable only to Al BE flows", CU
"Rules applicable only to Cu BE flows", IR "IR drop check compering Al
database and slotted Cu database for the same product (2 gds files) must
be clean", RR "Recommended rule at any IP level" and NC "Rule not checked
by DRC. It should be used as a guideline only."[^pdk-periph]

:::{table} The `ct` rules, the metal-1 enclosures of `mcon` and the rules of other sets that count or constrain contacts, as published

| Rule | Description (published wording, abridged where marked "[…]") | Value |
|------|--------------------------------------------------------------|-------|
| ct.1 | "Min and max L and W of mcon" (DNF) | 0.170 µm |
| ct.2 | "Spacing of mcon to mcon" (DNF) | 0.190 µm |
| ct.3 | "Only min. square mcons are allowed except die seal ring where mcons are…" | 0.170\*L |
| ct.4 | "Mcon must be enclosed by LI by at least …" (P) | 0.000 µm |
| ct.irdrop.1–3 | For 1 to 10, 11 to 100 and more than 100 contacts "on the same connector", "mcon area pre- and post- Cu conversion must differ by no more than…" (CU IR) | 0.2, 0.3, 0.7 µm |
| m1.4 | "Mcon must be enclosed by Met1 by at least …(Rule exempted for cell names documented in rule m1.4a)" (P) | 0.030 µm |
| m1.4a | The same enclosure for six named cells (P) | 0.005 µm |
| m1.5 | "Mcon must be enclosed by Met1 on one of two adjacent sides by at least …" (P AL) | 0.060 µm |
| m1.15 | "Mcon must be enclosed by met1 on one of two adjacent sides by at least …" (CU) | 0.030 µm |
| pwres.7b | "Every pwres_terminal must enclose 12 mcons if routed through metal1" | — |
| x.2 | "Angles permitted on: tap (except inside areaid.en), poly […], li1(periphery), licon1, capm, mcon, via, via2. Anchors are exempted." | n x 90 deg |
| x.7 | "Mask layer line and space checks must be done on all layers (checked with s.x rules)" (NC) | — |
| x.15a | "Drawn compatible, mask, and waffle-drop layers are allowed only inside areaid:mt (i.e., etest modules), […] Exception: FOM/P1M/Metal waffle drop are allowed inside the die" (P) | — |
| x.18 | "Use redundant mcon, via, via2, via3 and via4 […]" (RR) | — |
:::

*Criteria & Assumptions* repeats the size and space in Table 2 and adds
contact criteria in Tables 4 and 5:[^pdk-03]

:::{table} Parameters of *Criteria & Assumptions* for the contact, values as printed

| Parameter | PDK table | Published description | Value |
|---|---|---|---:|
| `CTM1CD` | Table 2 | size | 0.17 |
| `CTM1CDSP` | Table 2 | space | 0.19 |
| `CEFC` | Table 4 | "min. etch and fill capability for mcon" | 0.14 |
| `TCONOVLP` | Table 4 | "Minimum mcon overlap onto LI for reproducible contact resistance" | 0.12 |
| `mconLiEnclosure` | Table 4 | "Mcon enclosure by Li" | 0 |
| `TBOWINGSEAL` | Table 4 | "Bowing of rectangular contact (per edge) -- seal ring sizing" | 0.015 |
| without a variable name | Table 5 | "Standard contact bottom CD" | 0.09 |
:::

`TBOWINGSEAL` does not say which
contact layer it means.[^pdk-03] The summary Table F3c, "Back end layers for S8D\*
flow", repeats `mcon` as 0.170
wide on a 0.190 space, enclosed by `li1` by 0.000 and by metal 1 by
"0.03/ 0.06".[^pdk-summary] For the plate the decisive figures are one
0.170 µm square on a 0.36 µm pitch (our arithmetic from ct.1 and ct.2),
with the flag warning that neither is the final size.

## Related pages

* {ref}`CTM1 <step-107>` and {ref}`CTME <step-108>` — the mask step and
  the contact etch; {ref}`TIN2 <step-109>` — the liner that follows.
* **Category.** {ref}`category-lithography` and {ref}`category-etch` — the mask step
  and etch categories.
* **Machines.** {ref}`machine-duv-krf-stepper` — the exposure class the step page
  assigns. {ref}`machine-plasma-etcher-dielectric` — the etch class that transfers
  the pattern. {ref}`machine-cd-sem-overlay-metrology` — hole CD and overlay
  measurement.
* **Materials.** {ref}`material-lithography-materials` — resists, anti-reflective
  coatings, developer and reticles.
* **Masks.** {ref}`mask-li1m` — the local-interconnect mask the contacts land on;
  {ref}`mask-licm1` — the contact mask one level down.
* **Indexes.** {ref}`masks-index` — every mask's PDK entry, plates and renders,
  including the tables this page's plate facts are taken from.

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Contact, CTM1,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `mcon` 67:44,
  `ctm1` 35:0 and the columns of Table F2b.[^pdk-06]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `CTM1CD`/`CTM1CDSP`, `CEFC`,
  `TCONOVLP`, `mconLiEnclosure`, `TBOWINGSEAL` and the "Standard contact
  bottom CD".[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — the `ct` rules, m1.4–m1.5, m1.15,
  pwres.7b, x.1a, x.1b, x.2, x.7, x.9, x.15a, x.18 and the flag
  legend.[^pdk-periph]
* [SkyWater PDK, *Summary of Key Periphery Rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>) — Tables F3c and
  F4.[^pdk-summary]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — the contact and via
  resistance table.[^pdk-08]
* [*S8 / SKY130 Process Steps* sheet](<https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>) — the step, the `CTM1` plates of
  MPW-1 to MPW-8, the "Info" note and the mask-type tab.[^steps-sheet]
* [*SKY130 Open MPW mask-layer renders*](<https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>) — the `CTM1` renders, their
  layer, note and info text, and the per-die shape
  counts.[^mask-renders]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the DUV exposure
  tools.[^skw-01]

### High-level understanding

* [Wikipedia, *Photomask*](<https://en.wikipedia.org/wiki/Photomask>) — reticles, absorbers and
  pellicles.[^wiki-mask]
* [Wikipedia, *Phase-shift mask*](<https://en.wikipedia.org/wiki/Phase-shift_mask>) — the attenuated
  type.[^wiki-psm]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

### Deep dive

* [Wong et al. (IBM), *Proc. SPIE* 1998](<https://doi.org/10.1117/12.310718>) — the mask error factor of
  contacts and the size below which it rises.[^wong-1998]
* [Kim et al., *Proc. SPIE* 1999](<https://doi.org/10.1117/12.354400>) — mask CD error for sub-quarter-micron
  contact holes.[^kim-1999]
* [Takeuchi and Miyahara, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.360251>) — defect detectability and
  printability on KrF halftone contact-hole reticles.[^takeuchi-1999]
* [Choo et al., *Proc. SPIE* 2000](<https://doi.org/10.1117/12.388956>) — an attenuated mask for 0.16 µm
  contact holes of a 0.13 µm technology.[^choo-2000]
* [Lu et al., *Proc. SPIE* 1999](<https://doi.org/10.1117/12.350280>) — contact-hole resists for attenuated
  masks, limited by side-lobe printing.[^lu-1999]
* [Yamamoto et al., MNC 2000](<https://doi.org/10.1109/IMNC.2000.872612>) — hierarchical OPC on contact-hole
  layers.[^yamamoto-2000]
* [Socha et al. (ASML), *Proc. SPIE* 2004](<https://doi.org/10.1117/12.536581>) — assist features for
  low-{math}`k_1` contact holes by interference mapping.[^socha-2004]
* [Fukuda et al. (Hitachi), *IEEE EDL* 1987](<https://doi.org/10.1109/EDL.1987.26594>) — FLEX, multiple-focus
  exposure for contact holes.[^fukuda-1987]
* [Toyoshima et al. (Mitsubishi), IEDM 1998](<https://doi.org/10.1109/IEDM.1998.746367>) — chemical shrink (RELACS) of
  KrF resist holes.[^toyoshima-1998]
* [Rizvi (ed.), *Handbook of Photomask Manufacturing Technology*](<https://doi.org/10.1201/9781420028782>) — mask
  writing, advanced optical masks and mask inspection.[^rizvi-2005]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — contact-hole imaging and the optical mask
  requirements for critical layers at 130 nm.[^itrs-03]

## Open questions

* The DNF flag on ct.1 and ct.2 refers to a "table J" that the PDK does
  not publish, so the final contact size and how it is reached — mask
  bias, etch taper or a shrink — are not public.[^pdk-periph]
* The plate's type (binary or attenuated phase-shift), tone and CD
  specification, the resist and the exposure tool are not public; the
  KrF reading rests on the 0.170 µm rule.
* The pairing of `ctm1` with `mcon` is an inference from names and
  descriptions; the PDK publishes no operation from drawn layer to
  plate.[^pdk-06]
* Whether the absent MPW-5 record is a gap in the record or a difference
  in the run is not stated,[^steps-sheet] and no public source lists the `CTM1` plate of
  the original MPW-4 set `5CS8010AC`.[^mask-renders]
* The sheet and the renders site give both `CTM1` and `VIM` the level
  name "Via 1"; neither explains it.[^steps-sheet][^mask-renders]

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
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* (including Table F2b,
    the mask generation table) and `gds_layers.csv`, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions* (Tables 2, 4
    and 5), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-summary]: SkyWater PDK Authors, *Summary of Key Periphery Rules*
    (Tables F3c and F4), SkyWater SKY130 PDK documentation, retrieved
    2026-09-14.
    <https://skywater-pdk.readthedocs.io/en/main/rules/summary.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md` and, for each run, the `mpw-00N_CTM1/`
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
[^takeuchi-1999]: K. Takeuchi and Y. Miyahara, "Defect detectability and
    printability of contact hole pattern of KrF halftone reticle",
    *Proc. SPIE* **3748**, Photomask and X-Ray Mask Technology VI, 579
    (1999). <https://doi.org/10.1117/12.360251>
[^choo-2000]: L. C. Choo, O. Park, M. J. Sack and S. C. Tam,
    "Integration of attenuated phase-shift mask to 0.13-μm technology
    contact level masking process", *Proc. SPIE* **4000**, Optical
    Microlithography XIII, 1193 (2000).
    <https://doi.org/10.1117/12.388956>
[^lu-1999]: Z. G. Lu, Y. Cui, A. C. Thomas, S. M. Mansfield et al.,
    "Selection of attenuated phase shift mask compatible contact hole
    resists for KrF optical lithography", *Proc. SPIE* **3678**, Advances
    in Resist Technology and Processing XVI, 923 (1999).
    <https://doi.org/10.1117/12.350280>
[^yamamoto-2000]: K. Yamamoto, S. Kobayashi, T. Uno, T. Kotani et al.,
    "Hierarchical optical proximity correction on contact hole layers",
    *Digest of Papers, Microprocesses and Nanotechnology 2000*,
    pp. 40–41. <https://doi.org/10.1109/IMNC.2000.872612>
[^socha-2004]: R. J. Socha, D. J. Van Den Broeke, S. D. Hsu, J. F. Chen
    et al., "Contact hole reticle optimization by using interference
    mapping lithography (IML)", *Proc. SPIE* **5377**, Optical
    Microlithography XVII, 222 (2004). <https://doi.org/10.1117/12.536581>
[^fukuda-1987]: H. Fukuda, N. Hasegawa, T. Tanaka and T. Hayashida, "A
    new method for enhancing focus latitude in optical lithography:
    FLEX", *IEEE Electron Device Letters* **8**(4), 179–180 (1987).
    <https://doi.org/10.1109/EDL.1987.26594>
[^toyoshima-1998]: T. Toyoshima, T. Ishibashi, A. Minanide, K. Sugino
    et al., "0.1 μm level contact hole pattern formation with KrF
    lithography by resolution enhancement lithography assisted by
    chemical shrink (RELACS)", *IEDM 1998 Technical Digest*,
    pp. 333–336. <https://doi.org/10.1109/IEDM.1998.746367>
[^rizvi-2005]: S. Rizvi (ed.), *Handbook of Photomask Manufacturing
    Technology*, CRC Press, 2005, ISBN 978-1-4200-2878-2.
    <https://doi.org/10.1201/9781420028782>
