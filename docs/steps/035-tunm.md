(step-035)=
# Step 035 — TUNM: Tunnel mask

| | |
|---|---|
| **Step number** | 35 of 171[^steps-sheet] |
| **Step code** | `TUNM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | FEOL — SONOS and gate dielectrics |
| **Previous step** | {ref}`RTAI <step-034>` |
| **Next step** | {ref}`TUNARCE <step-036>` |

## What this step is

`TUNM` is the first mask of the {term}`SONOS` non-volatile-memory module and
the first lithography step after the wells and channels were annealed
at {ref}`RTAI <step-034>`. It coats the wafer with an anti-reflective
coating and photoresist, exposes the *tunnel mask* {term}`reticle` and
develops it, opening windows over the channel regions of the SONOS
memory transistors and leaving everything else — every logic
transistor, every 5 V and high-voltage device — covered. The windows
are used three times before the resist comes off: two implants go
through them ({ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`), and the
oxide inside them — the pad oxide, we infer — is then etched away
({ref}`TUNME <step-039>`) so
that the {term}`tunnel oxide` of the {term}`ONO` stack can be grown on bare
silicon at {ref}`ONO <step-040>`.

The PDK documents the mask and the drawn layer behind it. The mask table
lists "Tunnel Mask, TUNM" as used in SKY130,[^pdk-05] the generated mask
layer is `ctunm` (GDS 20:0, "Tunnel mask"), and the drawn layer is
`tunm` (GDS 80:20), which the layer list describes as "SONOS device
tunnel implant".[^pdk-06] That description — an *implant* layer rather
than an oxide layer — is the strongest hint in the PDK about what the
following steps do, and this reference accordingly describes two
implants between this mask and its etch. The `tunm`
rules (function: "Defines SONOS FETs") give the geometry: minimum width
0.410 µm (tunm.1), minimum spacing 0.500 µm (tunm.2), an extension of
`tunm` beyond the poly-over-active gate of 0.095 µm (tunm.3) and the
same 0.095 µm clearance to any other gate (tunm.4); "(poly and diff) may
not straddle tunm" (tunm.5); "Tunm outside deep n-well is not allowed"
(tunm.6a); a minimum area of 0.672 µm² (tunm.7); and `tunm` "must be
enclosed by areaid.ce" (tunm.8),[^pdk-periph] the "Memory (SRAM) core
cell identifier" layer.[^pdk-06] A separate rule on the thick-oxide
layer, "Hvi must not overlap tunm" (hvi.4),[^pdk-periph] keeps the
memory transistor out of the 5 V gate-oxide regions defined at
{ref}`LVOM <step-044>`.

Together these say that the tunnel window is drawn tightly around the
gate of each SONOS transistor, that every memory cell sits inside a
deep N-well tub (formed at {ref}`DNI <step-008>`), and that the cells
live only inside memory-array blocks whose internal rules the PDK does
not publish.

## Step category

`TUNM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant and etch window* type: a relaxed, non-critical
layer whose resist must survive two implants and an (inferred) wet oxide
etch. Its minimum feature (0.410 µm) and space (0.500 µm)[^pdk-periph]
are far above the 0.15 µm of the active layer ({ref}`FOM <step-004>`),
so it sits in the class of layers that a 130 nm-era fab prints on an
i-line {term}`stepper` (see below). What sets it apart from the other implant
masks of the flow is that it is followed by a dedicated anti-reflective
coating etch ({ref}`TUNARCE <step-036>`), the only such step in the step
list used in this reference.

## Why this step exists

SKY130 is, in the PDK's words, "the 8th generation SONOS technology
node (130nm)",[^pdk-02] and SkyWater lists "SONOS non-volatile memory
functionality" among the features the process offers as
standard.[^ann-11] The memory transistor is a MOSFET whose gate
dielectric is an oxide–nitride–oxide sandwich that stores charge in
the nitride; the PDK offers it as a two-transistor cell, "a SONOS
Control Gate (CG) in series with a CMOS Select Gate", in which
"Charge injected from the Si substrate across the thin tunnel oxide
by Fowler-Nordheim tunneling is trapped in the Nitride (N)
layer".[^cyp-25] A 2011 Cypress/UMC press release says that the
65 nm S65 SONOS process "only requires three additional mask layers to
a standard CMOS process";[^cyp-22] it gives no mask count for the
130 nm S8 process. We read `TUNM`, `ONOM` and `LDNTM` in the PDK's
mask table[^pdk-05] as the SONOS masks of SKY130 — and `TUNM` is the
first.

The tunnel window has to be a separate mask because the memory
transistor's channel is engineered differently from every logic
transistor. Its threshold must be set so that the programmed and
erased states straddle the read condition — the PDK's {term}`e-test` table
gives a nominal programmed threshold of 1.44 V and an erased threshold
of −2.3 V[^pdk-07] — which calls for its own channel implants
({ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`), and its tunnel oxide
has to be grown on bare silicon, which means removing the (inferred)
pad oxide only where the cells are ({ref}`TUNME <step-039>`). One mask
serves all three. Without `TUNM` there would be no SONOS cells; the logic
flow would be unaffected.

The published SKY130 {term}`test tile` shows the structures the SONOS
module is characterised with: "SONOS Rev 2" transistors from 0.45/0.15
to 25/25 µm, in deep N-well and "w/o DNW", a "2T Flash Cell Rev 2
Array, 11,264 cells" with "FET W/Lsonos/Lnpass = 0.45/0.22/0.15",
area- and perimeter-intensive "SONOS Rev 2" capacitors, and "NV Latch
Tri-Gates".[^raw-data-testtile-pads]

## How it is typically performed

An industry-generic sequence for a relaxed implant-plus-etch window in
a 200 mm, 130 nm-era fab (SKY130's recipe is not public):

1. **Surface preparation.** The wafer arrives with, we infer, the pad
   oxide still over the active areas and trench oxide over the field
   (its retention after {ref}`NS19 <step-013>` is not public; see the
   open questions there and on {ref}`RTAI <step-034>`). Dehydration
   bake and {term}`HMDS` vapour prime on the coat/develop track.
2. **Bottom anti-reflective coating.** An organic {term}`BARC` is
   spun and baked. ARCs "are often used in microelectronic
   photolithography to help reduce image distortions associated with
   reflections off the surface of the substrate" and "help reduce
   standing waves, thin-film interference, and specular
   reflections".[^wiki-arc] The existence of a separate {term}`ARC` etch at
   {ref}`TUNARCE <step-036>` is our evidence that this layer carries
   one; why a relaxed layer needs it is discussed on that page.
3. **Resist coat and soft bake.** A positive resist of roughly 1 µm
   — the PDK's assumptions table gives 1.14 µm as its generic
   "Photoresist thickness"[^pdk-03] — thick enough to stop the
   channel-type implants that follow (industry-typical: a 1 µm resist
   stops ions of a few hundred keV; {ref}`category-implant`).
4. **Exposure.** Through the tunnel reticle, aligned to the {term}`STI` pattern
   printed at {ref}`FOM <step-004>`. The 0.410 µm minimum
   feature[^pdk-periph] corresponds to {term}`k₁ <k1>` ≈ 0.67 at the 365 nm i-line
   with a typical 0.6 {term}`NA` i-line lens (illustrative) ({term}`CD` =
   k₁·λ/NA),[^wiki-litho] comfortably inside the i-line process window,
   so we infer an i-line layer; the 2001 ITRS assigns 248 nm only to the
   critical layers of the 130 nm node.[^itrs-03]
5. **Post-exposure bake, develop** in 2.38 % (0.26 N) TMAH,[^txt-02] rinse,
   and a hard bake to harden the resist for the implants.
6. **Inspection.** {term}`Overlay <overlay>` to active and CD on the coarse tunnel
   window; after-develop inspection for residue in the windows, which
   would block the implants or the oxide etch.

The resist is *not* stripped at the end of this step: it is opened
through the ARC at {ref}`TUNARCE <step-036>`, used as the implant
mask at {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>`, and as the
etch mask at {ref}`TUNME <step-039>`. This reference treats the strip
and the pre-oxidation clean as part of those steps (see the
{ref}`TUNME <step-039>` page).

## Machines typically used

* **{ref}`i-line stepper <machine-i-line-stepper>`**, 200 mm, 5× reduction: ASML PAS 5500/100–/275,
  Nikon NSR-2205i, Canon FPA-3000i ({ref}`category-lithography`).
* **{ref}`Coat/develop track <machine-coat-develop-track>`** with BARC and resist coat, bake and develop
  modules (TEL, DNS/SCREEN, Sokudo).
* **{ref}`Overlay and CD metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor overlay tools, {term}`CD-SEM`).
* **{ref}`After-develop inspection <machine-defect-inspection>`** (optical patterned-wafer inspection).

## Machines likely used at SkyWater

* **ASML i-line stepper or i-line scanner.** SkyWater lists "ASML
  I-line stepper" and "ASML I-line scanner" alongside its {term}`DUV`
  tools.[^skw-01] Strength: **strong** for the vendor and wavelength
  classes; **inference** for assigning `TUNM` to the i-line tools,
  from the 0.410 µm design rule.[^pdk-periph]
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius.**[^skw-01]
  Strength: strong for existence; which track serves the i-line tools
  is not public.
* **Metrology — AMAT Verity/VeraSEM CD-SEM; KLA 5200/5300/Archer
  overlay.**[^skw-01] Strength: strong for
  existence (SkyWater statement); use at this mask is an inference.
* **Defect inspection — KLA-Tencor AIT**, from a SkyWater job
  posting.[^job-01] Strength: medium.

## Resources required

* **Photoresist** — i-line DNQ/novolac positive resist
  ({ref}`category-lithography`); SkyWater names The Dow Chemical
  Company, JSR Corporation and Tokyo Ohka Kogyo America as photoresist
  suppliers.[^sec-01]
* **Organic BARC** and its solvent; **HMDS** adhesion promoter.
* **Developer** — aqueous 2.38 % (0.26 N) TMAH;[^txt-02] SkyWater's 2021 S-1
  names "Air Products & Chemicals, Inc., Moses Lake (developer)" without
  tying it to a layer.[^sec-01]
* **Edge-bead remover**, DI water, nitrogen.
* **The tunnel reticle** — a chrome-on-quartz photomask; with a 0.41 µm
  minimum feature no {term}`OPC` would be needed.

## Related steps and cross-references

* Previous: {ref}`RTAI <step-034>` (well and channel anneal); the
  wafer surface is, we infer, the pad oxide from {ref}`BOX <step-002>`.
* Next: {ref}`TUNARCE <step-036>` opens the ARC in the windows;
  {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>` implant through
  them; {ref}`TUNME <step-039>` etches the oxide (the pad oxide, we
  infer) inside them.
* The ONO stack that the windows are made for is grown at
  {ref}`ONO <step-040>` and confined to the cells by
  {ref}`ONOM <step-041>`/{ref}`ONOME <step-042>`.
* The other two SONOS-specific masks are {ref}`ONOM <step-041>` and
  {ref}`LDNTM <step-071>`.
* Deep N-well requirement (tunm.6a): {ref}`DNM <step-007>`,
  {ref}`DNI <step-008>`.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — "Tunnel Mask, TUNM,
  X".[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — `tunm`
  80:20 "SONOS device tunnel implant"; `ctunm` 20:0; `areaid.ce`
  81:2.[^pdk-06]
* SkyWater PDK, *Periphery rules* — tunm.1–tunm.8 and hvi.4.[^pdk-periph]
* SkyWater PDK, *Background* — "8th generation SONOS technology
  node".[^pdk-02]
* SkyWater PDK, *Device Details* — the SONOS cells, their
  programme/erase conditions and e-test thresholds.[^pdk-07]
* SkyWater PDK, *Criteria & Assumptions* — "Photoresist thickness"
  1.14 µm.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — ASML i-line and DUV tools,
  tracks, CD-SEM and overlay metrology.[^skw-01]
* SkyWater, first MPW shuttle press release — SONOS offered as a
  standard feature.[^ann-11]
* Cypress/UMC press release — the S65 process "only requires three
  additional mask layers"; no count is given for S8.[^cyp-22]
* Ramkumar, Prabhakar and Kapre (Cypress), Semiconductor Digest — the
  2T cell and its {term}`Fowler–Nordheim <Fowler–Nordheim tunnelling>` programming.[^cyp-25]
* SKY130 raw-data repository, test-tile pad documentation — the SONOS
  transistor, array and capacitor structures of the published test
  tile.[^raw-data-testtile-pads]

### High-level understanding

* Wikipedia, *SONOS* — the ONO stack and its typical
  thicknesses.[^cyp-26]
* Wikipedia, *Anti-reflective coating* — why a BARC is used.[^wiki-arc]
* Wikipedia, *Photolithography* — i-line versus KrF and
  CD = k₁·λ/NA.[^wiki-litho]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  the lithography chapters.[^txt-02]
* Ramkumar (Cypress), *Cypress SONOS — A Scalable Embedded Flash
  Technology* — "three to five masking layers" and the thermal-budget
  argument.[^cyp-24]

### Deep dive

* ITRS 2001, *Lithography* — which layers of the 130 nm node need
  248 nm, the basis for the i-line inference.[^itrs-03]
* White, Adams and Bu, *IEEE Circuits & Devices* 2000 — the classic
  review of scaled SONOS, including cell structures.[^pap-01]
* Seo et al. (Samsung), *IEEE JSSC* 2005 — a 130 nm logic-compatible
  SONOS embedded flash from another vendor, for comparison of cell
  and array design.[^pap-02]
* Kim et al. (Samsung), VLSI 2003 — a "highly manufacturable"
  embedded SONOS module and its mask adders.[^pap-03]
* Taniguchi et al., IMW 2023 — SONOS embedded flash on a 130 nm
  platform with three added masks.[^pap-05]
* Jiew, Chien and Yung, NVMTS 2012 — development of a robust 2T-SONOS
  cell for embedded flash, the same cell topology as SKY130's.[^jiew-2012]
* Koutny et al. (Cypress), US 8,093,128 — where the charge-trap
  module sits relative to the logic well and channel implants.[^pat-03]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  memory-cell region opened through a mask for its own channel
  implants before the tunnel dielectric is formed.[^pat-04]
* Baker and Capsuto, SPIE 1996 — CD control for an i-line 0.35 µm
  device using a new anti-reflective coating.[^baker-1996]
* Levinson, *Principles of Lithography* — non-critical-layer tool
  choice and overlay budgets.[^levinson-2005]
* Hook et al., *IEEE TED* 2003 — ions scattered from the resist edge
  shift the threshold of devices near an implant-mask edge, relevant
  to the 0.095 µm `tunm` clearances.[^hook-2003]

## Open questions

* Whether `TUNM` is exposed on the i-line or the DUV tools is an
  inference from the 0.410 µm rule; no SkyWater statement assigns
  layers to tools.
* Reticle tone and resist type are not public.
* Why a relaxed implant layer carries an ARC is an open question
  (see {ref}`TUNARCE <step-036>`).
* The internal layout rules of the memory arrays (`areaid.ce`) are not
  published, so the real cell pitch cannot be derived from the `tunm`
  rules alone.
* Where the resist is stripped after {ref}`TUNME <step-039>` is not
  stated publicly; this reference treats the strip as part of that
  etch.

<!-- footnotes -->

[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^ann-11]: SkyWater / Efabless, *First Google-Sponsored MPW Shuttle
    Launched at SkyWater with 40 Open Source Community Submitted
    Designs*, 2021-04-06.
    <https://skywatertechnology.com/press-releases/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs>
[^cyp-22]: Cypress Semiconductor / UMC, *Cypress and UMC Deliver ICs on
    New 65-Nanometer SONOS Embedded Flash Technology*, PR Newswire,
    2011-07-27.
    <https://www.prnewswire.com/news-releases/cypress-and-umc-deliver-ics-on-new-65-nanometer-sonos-embedded-flash-technology-126238008.html>
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^cyp-24]: K. Ramkumar (Cypress Semiconductor), *Cypress SONOS — A
    Scalable Embedded Flash Technology*, ChipEstimate.com technical
    article, 2008-10-21.
    <https://www.chipestimate.com/Cypress-SONOS-A-Scalable-Embedded-Flash-Technology/Cypress-Semiconductor/Technical-Article/2008/10/21>
[^cyp-26]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^wiki-arc]: Wikipedia, *Anti-reflective coating*.
    <https://en.wikipedia.org/wiki/Anti-reflective_coating>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; Defect Technician 2 posting),
    retrieved 2026-08-30; listings expire. <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
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
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
[^baker-1996]: D. C. Baker and E. S. Capsuto, "Critical dimension
    control for i-line 0.35-μm device using a new antireflective
    coating", *Proc. SPIE* **2724**, Advances in Resist Technology and
    Processing XIII, 710 (1996). <https://doi.org/10.1117/12.241869>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
