(step-137)=
# Step 137 — CAPM: Capacitor mask

| | |
|---|---|
| **Step number** | 137 of 171[^steps-sheet] |
| **Step code** | `CAPM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CAPTIW1 <step-136>` |
| **Next step** | {ref}`CAPME <step-138>` |

## What this step is

`CAPM` is the lithography that defines the top plates of the first
{term}`MiM capacitor`. On the blanket plate film of
{ref}`CAPTIW1 <step-136>` (TiW, as assumed there) — which
lies on the capacitor dielectric of {ref}`CAPILD <step-135>` and the
still-unpatterned metal-3 stack of {ref}`WTIAL3 <step-134>` — a
resist is coated, exposed and developed so that resist remains
wherever the layout draws `capm`, "MiM capacitor plate over metal 3"
(GDS 89:44),[^pdk-06] and is cleared everywhere else. The
{ref}`CAPME <step-138>` etch then removes the exposed TiW, stopping on
or in the dielectric, and leaves the plates. The PDK's mask table
lists "Capacitor MiM, CAPM",[^pdk-05] so the step code is the mask
name; with {ref}`CAP2M <step-152>`, it is one of two masks in the
flow whose pattern is a *device* rather than a wiring, contact or
implant layer, and one of two printed on a metal that will itself be
patterned afterwards (here at {ref}`MM3 <step-139>`).

The public geometry is coarse. The PDK's minimum-CD table gives the
capacitor mask a `CAPMCD` of 2 µm and a `CAPMCDSP` of
0.84 µm,[^pdk-03] its physical-criteria table a maximum MiM
capacitor aspect ratio of 20,[^pdk-03] and the periphery rules a
set of twelve `capm` rules — minimum width, spacing to `capm` and to
the bottom plate, enclosure of the plate by the metal beneath,
enclosure of the via that contacts it, three spacings (of `capm` to
`via2`, of `via` to `capm`, and of `capm` to `met2` that does not
overlap it), a maximum aspect ratio, a rectangles-only rule, a rule
that `capm` must not straddle wells, diffusion, tap, poly, local
interconnect or metal 1, and a maximum
area — all with their numeric values shown as "N/A" on the public
page.[^pdk-periph] The capacitance the plate defines is the PDK's
2 fF/µm² of area plus 0.19 fF/µm of periphery.[^pdk-07] A 2 µm
feature on a 0.84 µm space is, by the standards of the flow, an easy
print: the metal-3 lines that follow are 0.30 µm wide[^pdk-periph]
and the via-3 holes 0.20 µm.[^pdk-periph]

The surface is unusual for a mask step: flat (no {term}`CMP` step, no
plug topography — the metal-3 stack was sputtered onto the polished
via-2 level of {ref}`WCMP4 <step-133>`), highly reflective (the plate
film over the metal-3 stack) and thermally and chemically delicate, since only some
20–30 nm of dielectric (our estimate at {ref}`CAPILD <step-135>`)
separate the resist's substrate from the aluminium below.

## Step category

`CAPM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *non-critical, large-feature* type. At 2 µm and 0.84 µm
the process factor {term}`k₁ <k1>` on an i-line (365 nm) stepper of {term}`NA` 0.6
would be {math}`k_1 = 0.84 \times 0.6 / 0.365 \approx 1.4`, far above
the resolution limit, and ASML describes older exposure tools that
"migrate to the lithography of choice for less critical
layers";[^asml-30] we therefore infer that `CAPM` is printed on the "ASML I-line
stepper" or "I-line scanner" SkyWater lists,[^skw-01] with a
conventional DNQ/novolac resist, rather than on the {term}`DUV`
tools used for the critical layers. Nothing public
states the tool or resist. What the layer shares with the metal masks
is the substrate problem — a reflective refractory film that
demands reflectivity control — and what it shares with no other
layer is that its {term}`CD` error translates directly into a device
parameter: a 0.1 µm bias on a 2 µm plate is a 10 % change in
capacitance, so the mask-to-etch bias must be characterised and
absorbed in the model's `CMIMP` periphery term (inference from the
model form[^pdk-07]).

## Why this step exists

* **The plate area is the capacitance.** The capacitor is drawn as
  `capm` and its value is `CMIMA` × area + `CMIMP` × perimeter;[^pdk-07]
  this mask, and the etch that follows, fix that area on the wafer.
  The PDK's maximum MiM capacitor aspect ratio of 20[^pdk-03] and the
  rectangles-only rule (capm.7)[^pdk-periph] keep, we infer, the
  periphery term and the plate resistance within what the model was
  fitted for; Ng et al. review MiM integration in Al–Cu and Cu back
  ends.[^ng-2005]
* **Top plate first, bottom plate later.** Printing `capm` on the
  unpatterned metal means the resist sits on a flat, continuous film
  with no metal edges to reflect light into the plate corners and no
  topography under the dielectric; the plate edge lands on
  dielectric-over-metal everywhere. This is the construction of the
  Newport Fab patent[^pat-mim-newportfab] and, we infer from the
  PDK's description of the construction,[^pdk-07] SKY130's; IBM's and
  Freescale's patents reach a planar bottom plate by damascene or by
  CMP of the dielectric beneath a dedicated electrode
  instead.[^pat-mim-ibm][^pat-mim-freescale] The alternative —
  etching the bottom metal first and depositing the dielectric and
  plate over its edges — puts the thin dielectric on a sidewall.
* **Alignment and enclosure.** The plate must later be enclosed by
  the metal-3 bottom plate and contacted by a via-3 that the plate
  encloses — the rules capm.3 (enclosure of the plate by the metal
  beneath) and capm.4 (enclosure of the via by the plate), with
  capm.5 setting the spacing of the plate to a via it does not
  contact,[^pdk-periph] whose text names
  `met2` and `via2`, read here for metal 3 and via 3 (inference; see
  {ref}`CAPILD <step-135>`). Because metal 3 has not yet been printed,
  `CAPM` is aligned to the last patterned layer — the via-2 holes of
  {ref}`VIM2 <step-129>` under the metal — and {ref}`MM3 <step-139>`
  is then aligned either to the same marks or to `capm` itself
  (inference; the choice sets which enclosure carries the
  {term}`overlay` error; Levinson's book has a chapter on
  overlay[^levinson-2005]).
* **Protecting the dielectric.** Everywhere the resist is cleared,
  the {ref}`CAPME <step-138>` etch will expose the capacitor dielectric; where
  it remains, the plate and the dielectric under it are the finished
  capacitor. The resist therefore also decides where the delicate
  film is exposed to plasma — a reason the etch, not the mask, is
  the delicate step.

Without `CAPM` the TiW of {ref}`CAPTIW1 <step-136>` would stay a
blanket sheet and be removed, with the dielectric, at
{ref}`MM3E <step-140>`; there would be no capacitors.

## How it is typically performed

An industry-generic large-feature lithography step on a reflective
refractory film for a 200 mm, 130 nm-era fab (SKY130's is not public):

1. **Surface preparation.** The wafer comes from the {term}`PVD`
   cluster; a dehydration bake, and either an organic {term}`BARC`
   or a dyed resist to tame the reflectivity of the plate over the
   metal-3 stack
   (Brunner's {term}`swing-curve <swing curve>` analysis is the basis;[^brunner-1991]
   Rocke and Schneegans documented the anti-reflective role of a
   refractory cap on aluminium[^rocke-1988]). No {term}`HMDS` is
   needed on a metal.
2. **Resist coat.** A positive i-line DNQ/novolac resist — the
   chemistry Dammel's tutorial text and Reichmanis and
   Thompson's review describe[^dammel-1993][^reichmanis-1989][^wiki-dnq]
   — at around 1 µm (industry-typical for i-line
   resists[^mack-2007]; the PDK's nominal resist thickness of 1.14 µm
   is an antenna-rule assumption that need not describe this
   layer[^pdk-03]). A thicker resist is affordable here because the
   features are large and the TiW etch is short.
3. **Exposure.** i-line on a 5× or 4× stepper of NA 0.5–0.6 — the
   ASML PAS 5500 family spans i-line and DUV models on one
   platform[^asml-30][^chiphistory-pas5500] — with conventional
   illumination; the large features need no resolution enhancement
   (inference from the geometry).
4. **Post-exposure bake and develop.** A {term}`PEB` to smooth
   standing waves, then 2.38 % (0.26 N) TMAH develop, rinse and dry.[^txt-02]
5. **Alignment.** To the {ref}`VIM2 <step-129>` marks beneath the
   metal (the metal-3 stack is opaque, so the marks are read as
   topography or through cleared windows; our reading of industry
   practice, and Levinson's book has a chapter on
   overlay[^levinson-2005]).
6. **Inspection and metrology.** Plate {term}`CD` by optical CD or
   {term}`CD-SEM` on the AMAT Verity/VeraSEM class SkyWater
   lists;[^skw-01] overlay on the KLA 5200/5300/Archer class;[^skw-01]
   after-develop inspection for residue over the plates, since a
   resist defect here is a capacitor defect. Dose and focus are
   tracked by Ausschnitt's method.[^ausschnitt-1999]

## Machines typically used

* **{ref}`i-line stepper or scanner <machine-i-line-stepper>`**, 200 mm: ASML PAS 5500/275–/400
  class,[^asml-30][^chiphistory-pas5500] Nikon NSR-i and Canon FPA
  i-line systems ({ref}`category-lithography`); a {ref}`KrF tool <machine-duv-krf-stepper>` could
  print the layer but is not needed.
* **{ref}`Coat/develop track <machine-coat-develop-track>`** (TEL ACT/Lithius,[^tel-act] DNS, Sokudo).
* **Optical CD / {ref}`CD-SEM <machine-cd-sem-overlay-metrology>`**, **overlay tool**, **{ref}`after-develop inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **ASML I-line stepper / I-line scanner.** SkyWater lists both.[^skw-01]
  Strength: **strong** for existence; the assignment of `CAPM` to
  i-line is an **inference** from the 2 µm / 0.84 µm rules[^pdk-03]
  and the migration of older exposure tools to "less critical layers"
  that ASML describes.[^asml-30] The model is not public.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius.**[^skw-01]
  Strength: strong for existence.
* **CD — AMAT Verity, VeraSEM; overlay — KLA 5200/5300/Archer.**[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **i-line positive photoresist** ({ref}`lithography materials <material-lithography-materials>`; DNQ/novolac); SkyWater's 2021 S-1
  names Dow, JSR and Tokyo Ohka Kogyo as photoresist
  suppliers.[^sec-01]
* **Organic BARC** or dyed resist, **2.38 % (0.26 N) TMAH developer** (the
  2021 S-1 names "Air Products & Chemicals, Inc., Moses Lake" for
  developer[^sec-01]), edge-bead remover, rinse solvents, {ref}`DI water <material-ultrapure-water>` and
  {ref}`nitrogen <material-process-gases>`.[^txt-02]
* **The CAPM {term}`reticle`**, generated from the drawn `capm` layer
  (89:44)[^pdk-06] — on our reading a binary chrome-on-glass mask
  without OPC.
* **Mercury-lamp consumables** for the i-line tool.

## Related steps and cross-references

* Previous: {ref}`CAPTIW1 <step-136>` (the plate film). Next:
  {ref}`CAPME <step-138>` (the plate etch, which on our reading
  includes the strip).
* The dielectric under the plate: {ref}`CAPILD <step-135>`; the
  bottom plate patterned afterwards: {ref}`MM3 <step-139>`,
  {ref}`MM3E <step-140>`.
* The via that must land inside the plate: {ref}`VIM3 <step-144>`.
* Previous mask: {ref}`VIM2 <step-129>`; next mask:
  {ref}`MM3 <step-139>`; the second capacitor's mask:
  {ref}`CAP2M <step-152>`.
* Mask page: {ref}`CAPM <mask-capm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,708,559 A <patent-gp24193081>` — Precision analog metal-metal capacitor (1995)
* {ref}`US 6,430,028 B1 <patent-gp24897586>` — Method for fabrication of an MIM capacitor and related structure (2000)
* {ref}`US 7,112,507 B2 <patent-gp34591550>` — MIM capacitor structure and method of fabrication (2003)
* {ref}`US 7,375,002 B2 <patent-gp37568077>` — MIM capacitor in a semiconductor device and method therefor (2005)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Masks* — "Capacitor MiM, CAPM".[^pdk-05]
* SkyWater PDK, *Layers Reference* — `capm` 89:44 "MiM capacitor
  plate over metal 3".[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD` 2 µm, `CAPMCDSP`
  0.84 µm; MiM aspect ratio 20; photoresist 1.14 µm.[^pdk-03]
* SkyWater PDK, *Periphery rules* — capm.1–capm.12 (values not
  published); m3.1, via3.1.[^pdk-periph]
* SkyWater PDK, *Device Details* — `CMIMA`, `CMIMP`.[^pdk-07]
* SkyWater, *Facilities & Capabilities* — ASML I-line stepper and
  scanner, tracks, CD and overlay tools.[^skw-01]
* SkyWater, Form S-1 — photoresist and developer suppliers.[^sec-01]
* ASML, *Three decades of PAS 5500*; Chip History Center, PAS
  5500/400.[^asml-30][^chiphistory-pas5500]

### High-level understanding

* Wikipedia, *Photolithography*, *Diazonaphthoquinone*,
  *Anti-reflective coating*.[^wiki-litho][^wiki-dnq][^wiki-arc]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  i-line resist processing on metal.[^txt-02]
* Mack, *Fundamental Principles of Optical Lithography* — imaging of
  large features, swing curves and BARCs.[^mack-2007]

### Deep dive

* ITRS 2001, *Lithography* — the exposure options it lists by node for
  critical layers.[^itrs-03]
* Dammel, *Diazonaphthoquinone-based Resists* — the i-line resist
  chemistry in full.[^dammel-1993]
* Reichmanis and Thompson, *Chem. Rev.* 1989 — polymer materials
  for microlithography, DNQ/novolac included.[^reichmanis-1989]
* Brunner, SPIE 1991 — swing curves and anti-reflection on
  reflective substrates.[^brunner-1991]
* Rocke and Schneegans (Siemens), *JVST B* 1988 — a refractory cap
  as an anti-reflective layer on aluminium.[^rocke-1988]
* Levinson, *Principles of Lithography* — the chapter on
  overlay.[^levinson-2005]
* Ausschnitt, SPIE 1999 — separating dose from defocus in
  production.[^ausschnitt-1999]
* Ng et al. (Chartered), *IEEE TED* 2005 — a review of MiM integration
  in Al–Cu and Cu back ends.[^ng-2005]
* Brabazon et al. (IBM), US 5,708,559; Kar-Roy and Racanelli
  (Newport Fab), US 6,430,028; Roberts and Huffman (Freescale),
  US 7,375,002 — two top-plate-first MiM constructions and a
  damascene-plate one, with their mask
  sequences.[^pat-mim-ibm][^pat-mim-newportfab][^pat-mim-freescale]
* Kim and Demm (Infineon), US 7,112,507 — a plate formed in the full
  thickness of a metallisation level, the other way round.[^pat-mim-infineon]

## Open questions

* The exposure tool, resist and reflectivity scheme for `CAPM` are
  not public; i-line with a conventional resist is an inference from
  the 2 µm / 0.84 µm rules.[^pdk-03]
* The numeric values of the `capm` periphery rules are not
  published ("N/A" on the public page[^pdk-periph]).
* Which layer `CAPM` is aligned to, and which layer `MM3` is then
  aligned to, is not public.
* The mask table does not flag "Capacitor MiM, CAPM" as used in
  SKY130,[^pdk-05] while the README lists "Optional MiM capacitors"
  yet also counts them among the "normally optional features"
  included "as standard",[^pdk-10] and the shuttle announcements
  offer them as standard;[^ann-11] whether the mask is run on every lot is not
  public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^ann-11]: SkyWater / Efabless, *First Google-Sponsored MPW Shuttle
    Launched at SkyWater with 40 Open Source Community Submitted
    Designs*, 2021-04-06.
    <https://skywatertechnology.com/press-releases/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^chiphistory-pas5500]: Chip History Center, *PAS 5500/400 Step & Scan
    Alignment System from ASML*.
    <https://www.chiphistory.org/163-asml-pas-5500-400-step-scan-system>
[^tel-act]: Tokyo Electron, *Coater/Developer ACT Series*, product
    page. <https://www.tel.com/product/act.html>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^wiki-dnq]: Wikipedia, *Diazonaphthoquinone*.
    <https://en.wikipedia.org/wiki/Diazonaphthoquinone>
[^wiki-arc]: Wikipedia, *Anti-reflective coating*.
    <https://en.wikipedia.org/wiki/Anti-reflective_coating>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
[^reichmanis-1989]: E. Reichmanis and L. F. Thompson, "Polymer
    materials for microlithography", *Chemical Reviews* **89**(6),
    1273–1289 (1989). <https://doi.org/10.1021/cr00096a001>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^rocke-1988]: M. Rocke and M. Schneegans, "Titanium nitride for
    antireflection control and hillock suppression on aluminum silicon
    metallization", *Journal of Vacuum Science & Technology B* **6**(4),
    1113–1115 (1988). <https://doi.org/10.1116/1.584306>
[^ausschnitt-1999]: C. P. Ausschnitt, "Distinguishing dose from
    defocus for in-line lithography control", *Proc. SPIE* **3677**,
    Metrology, Inspection, and Process Control for Microlithography
    XIII, 140 (1999). <https://doi.org/10.1117/12.350800>
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^pat-mim-ibm]: T. J. Brabazon, B. El-Kareh, S. R. Martin, M. J. Rutten
    and C. W. Kaanta (International Business Machines), *Precision
    analog metal-metal capacitor*, US 5,708,559 A, filed 1995-10-27,
    granted 1998-01-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5708559>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^pat-mim-freescale]: D. R. Roberts and G. L. Huffman (Freescale
    Semiconductor), *MIM capacitor in a semiconductor device and method
    therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
[^pat-mim-infineon]: S.-O. Kim and E. Demm (Infineon Technologies),
    *MIM capacitor structure and method of fabrication*, US 7,112,507
    B2, filed 2003-11-24, granted 2006-09-26.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7112507>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
