(step-071)=
# Step 071 — LDNTM: LD tip layer mask

| | |
|---|---|
| **Step number** | 71 of 171[^steps-sheet] |
| **Step code** | `LDNTM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`HVASTIS <step-070>` |
| **Next step** | {ref}`LDASTI <step-072>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** patterns a resist that opens only the SONOS memory
  transistors, for their lightly doped tip `LDASTI` and halo `LDBHI`.
* **Why:** on our reading of the cell's published voltages, the memory
  transistors need a lighter, graded tip than the logic NMOS.
* **Public numbers:** core checks "0.7 min. width of ldntmCore" and
  "0.7 min. spacing/notch of ldntmCore".[^pdk-errors]
* **Likely SkyWater tool:** ASML i-line stepper or scanner — strong
  (tools); inference (assignment).[^skw-01]
* **Not public:** whether the select transistor is opened; the resist
  thickness and the tilt (→ Open questions).
:::

## What this step is

`LDNTM` is the third and last tip mask of the module. On the surface
cleaned at {ref}`HVASTIS <step-070>` it patterns a resist that exposes
the {term}`SONOS` memory transistors and covers everything else, so that the
*lightly doped* arsenic tip {ref}`LDASTI <step-072>` and its boron {term}`halo`
{ref}`LDBHI <step-073>` can be implanted into the memory cells alone.
The resist is removed at {ref}`LDASTIS <step-074>`, after which every
tip in the flow is annealed at {ref}`TIPRTAD <step-075>`.

:::{figure} /_static/figures/sd-071-ldntm.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step two capped stacks stand on the wafer, a wide one on the oxide-filled trench and a narrow one on the right-hand active area, with doped layers in the silicon of both active areas. After it one flat-topped block of resist covers the whole slice.
:width: 560px
:name: fig-sd-071-ldntm

Before, the wafer cleaned at HVASTIS; after, the LDNTM resist. The mask opens only over the SONOS memory transistors, which the PDK's layer table names as the layer's devices,[^pdk-06] and the slice holds none, so here the resist has no window. The resist is drawn at the thickness of the other standard implant resists; the page infers the PDK's nominal 1.14 µm,[^pdk-03] and the actual thickness is not public. The tips' colour and the halo's hatching mark where the implants are, not their profiles. The halo, the caps, the gate oxides, the re-oxidation oxide and the field oxide (the oxide-filled trench in the middle) are drawn but not labelled, and the liner oxide is drawn faded; the P-well and the NCHI channel implant made earlier are not drawn. Under the resist in the lower panel the high-voltage tip on the left is not labelled, because its leader would have to rise through the resist. In the lower panel the gate film and the resistor body under the resist are not labelled either. Not to scale.
:::

### What the public record shows

**Mask and layers.** Which devices this mask serves is public. The PDK lists
"Lightly Doped N-tip, LDNTM" as a mask used in SKY130,[^pdk-05] and its
layer table describes the drawn layer `ldntm` (GDS 11:44) as "N-tip implant
on SONOS devices", with the generated mask layer `cldntm` (11:0,
"Lightly-doped N-tip implant mask").[^pdk-06]

**Core checks.** The public periphery rule set contains no `ldntm`
rules.[^pdk-periph] The PDK's *Error Messages* page, however, lists core
checks on the layer, `ldntm.c1` to `ldntm.c6`:[^pdk-errors]

* "0.7 min. width of ldntmCore";
* "0.7 min. spacing/notch of ldntmCore";
* "enclosure of ndiff by ldntm must be more than  0.180";
* "0.125 min. enclosure of nFet by ldntmCore";
* "ldntm not allowed outside areaid.ce";
* "0.18 min. spacing of ldntmCoreExempt & pdiff".

The layer is therefore checked as a core layer, inside the memory-cell
identifier. The earlier pages of this reference on the SONOS module
({ref}`TUNM <step-035>`, {ref}`PTSI <step-037>`,
{ref}`DEPI <step-038>`, {ref}`ONO <step-040>`) already point here as
the cell's tip implant.

**Tip angle.** The PDK's assumptions page, which publishes {term}`shadowing`
allowances for `NTM` and `HVNTM`, has none for `LDNTM`,[^pdk-03] and gives a
single "Angle for tip implant" of 7° that we take to apply to this tip as
well as the standard one (inference).

## Step category

`LDNTM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type, aligned to the polysilicon gates of
the memory cells.

**Specific to this step:**

* Like {ref}`NTM <step-064>` it selects transistors rather than
  defining junction edges — the gate does that — and its features are
  cell-sized.
* It differs from the other tip masks in covering a small fraction of
  the die: only the memory array and any SONOS test structures are
  opened.

## Why this step exists

The SONOS memory transistor is a different animal from the logic NMOS
next to it. The PDK's {term}`e-test` parameters describe it:[^pdk-07]

* at drawn W/L 0.45/0.22 µm and 0.35/0.15 µm, for "both original and
  star cells" (the PDK does not say which is which; see
  {ref}`PTSI <step-037>`).
* its programme and erase conditions apply +6.7 V to the
  {term}`control gate` with −3.8 V on source, drain and body, and −3.8 V
  on the gate with +6.7 V on the other three terminals.

  (The PDK's table prints the source voltage as "-38"; we read it as
  −3.8 V, the value already in the row's other two cells (drain, body)
  and in the erase row's gate cell, and the only reading consistent with
  the page's junction limits.)
* it must keep its window over 100 000 cycles.

Three consequences follow for its source/drain
{term}`extensions <extension>`:

* **Junction voltage.** During programme, erase and inhibit the
  source/drain junctions sit at several volts relative to gate and
  body — far more than the 1.8 V a logic tip sees.

  A heavily doped, abrupt tip under a gate at −3.8 V would drive
  band-to-band tunnelling and gate-induced drain leakage at the gate edge,
  disturbing unselected cells and loading the charge pumps. A lightly doped,
  graded tip lowers the peak field, the classical {term}`LDD`
  argument.[^ogura-1980] The same reasoning — a lighter LDD to cut junction
  leakage on selected transistors — is made explicitly in a Micron DRAM
  patent of the era.[^pat-ldd-micron]
* **Charge-trapping reliability.** SONOS cells are programmed and
  erased by tunnelling through the thin bottom oxide.[^pap-01]

  Any {term}`hot-carrier injection` at the drain edge during read or inhibit
  injects charge into the nitride where it is not wanted and shifts the
  cell's threshold — the mechanism deliberately exploited by NROM-type
  cells[^eitan-2000] and deliberately avoided here. A graded drain keeps the
  lateral field low.
* **Short-channel control at 0.15–0.22 µm.** A lighter tip gives less
  short-channel margin than the logic tip, so the cell gets its own
  halo ({ref}`LDBHI <step-073>`) on top of the {term}`punch-through stopper <punch-through>`
  implanted at {ref}`PTSI <step-037>`.

Because the memory transistor's channel is set by its own implants
({ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`) and its gate is poly over
{term}`ONO` rather than over gate oxide, its junctions are co-optimised with
them. Cypress's embedded-SONOS patents, which may still be in force,
describe the cell in the collapsed note below, and a separate LDD implant
for a particular transistor type on the same chip is a standard construction
in the patent literature.[^pat-multi-ldd-amd]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
Cypress's embedded-SONOS patents describe the cell as a device formed
inside a logic flow with its own implant steps.[^pat-04][^pat-03]
:::

Without `LDNTM`, the memory transistors would take either the logic
tip (with leakage and disturb problems at the cell's voltages) or no
tip at all.

## How it is typically performed

*An industry-generic implant-block lithography sequence for a 200 mm,
130 nm-era fab:*

1. **Surface preparation.** Dehydration bake and {term}`HMDS` prime on the
   oxide surface left by {ref}`HVASTIS <step-070>`.
2. **Resist coat.** A single-layer positive resist; with no
   thin-resist parameter published for this mask (the PDK gives 0.3 µm
   only "for HV Tip Implants"),[^pdk-03] we infer the standard
   ~1 µm film (the PDK's nominal 1.14 µm).[^pdk-03] The keV-range tip
   and tens-of-keV halo are stopped with a wide margin.[^txt-02]
3. **Exposure.** The openings are memory-array sized; even the
   smallest, over an isolated test cell, is far above i-line
   resolution.[^wiki-litho] With older exposure tools migrating, in
   ASML's words, "to the lithography of choice for less critical
   layers",[^asml-30] we infer an i-line exposure.
4. **Alignment.** To poly. Because the array is dense — cells at
   0.15–0.22 µm gate length with shared source/drain lines[^pdk-07] —
   the resist edge at the array boundary must stand back from the
   outermost gates by the tip's shadowing allowance (compare the
   0.16 µm "NTM shadowing").[^pdk-03]
5. **Develop** in 2.38 % (0.26 N) TMAH,[^txt-02] rinse, dry; a post-develop
   bake or UV cure to stabilise the resist against two implants
   (industry practice).[^txt-02]
6. **Inspection.** {term}`Overlay <overlay>` to poly; after-develop defect inspection.

## Machines typically used

* **{ref}`i-line <machine-i-line-stepper>` {term}`stepper`**, 200 mm: ASML PAS 5500/100–/275 series, Nikon
  NSR-2205i, Canon FPA-3000i.[^txt-05]
* **{ref}`Coat/develop track <machine-coat-develop-track>`** (TEL, DNS/SCREEN, SVG/ASML, Sokudo).
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor 5xxx/Archer) and a {term}`CD-SEM`.

## Machines likely used at SkyWater

* **ASML i-line stepper / i-line scanner**
  - *SkyWater says:* lists "ASML I-line stepper" and "ASML I-line
    scanner".[^skw-01]
  - *Tool exists:* **strong** for the tools.
  - *Runs this step:* **inference** for the assignment of `LDNTM` to them.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**[^skw-01]
  - *Tool exists:* strong for existence.
* **Overlay — KLA 5200/5300/Archer; {term}`CD` — AMAT Verity/VeraSEM**[^skw-01]
  - *Tool exists:* strong for existence (SkyWater statement).
  - *Runs this step:* use at this mask is an inference.

## Resources required

* **Positive i-line (DNQ/novolac) photoresist** ({ref}`lithography materials <material-lithography-materials>`), about 1 µm
  (inferred); SkyWater's 2021 S-1 names The Dow Chemical Company, JSR
  Corporation and Tokyo Ohka Kogyo America as photoresist
  suppliers.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^txt-02] edge-bead remover, {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The LDNTM {term}`reticle`** — generated from the drawn `ldntm` layer as
  `cldntm`.[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`HVASTIS <step-070>` (clean surface).
* Next: {ref}`LDASTI <step-072>` (lightly doped arsenic tip) and
  {ref}`LDBHI <step-073>` (halo) through this resist, then
  {ref}`LDASTIS <step-074>` (strip).
* The memory cell this mask serves: tunnel window
  {ref}`TUNM <step-035>`, channel implants {ref}`PTSI <step-037>` and
  {ref}`DEPI <step-038>`, ONO stack {ref}`ONO <step-040>` patterned by
  {ref}`ONOM <step-041>`/{ref}`ONOME <step-042>`, gate
  {ref}`SAGD <step-048>` and {ref}`P1ME <step-062>`.
* Same module: sibling tip masks {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`;
  activation: {ref}`TIPRTAD <step-075>`.
* Mask: {ref}`LDNTM <mask-ldntm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Integrated circuit having multiple LDD and/or source/drain implant steps to enhance circuit performance <patent-gp25122771>` — US 5,793,090 A (1997)
* {ref}`Double LDD devices for improved DRAM refresh <patent-gp24577983>` — US 6,759,288 B2 (2000)

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,093,128 B2 <patent-gp40072804>` — in force
* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "Lightly Doped N-tip,
  LDNTM, X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `ldntm`
  11:44 "N-tip implant on SONOS devices"; `cldntm` 11:0.[^pdk-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — no `ldntm` rules in the public
  periphery set.[^pdk-periph]
* SkyWater PDK, [*Error Messages*](<https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>) page and `errors.csv` — the `ldntm.c1`
  to `ldntm.c6` core checks.[^pdk-errors]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — 7° tip angle; shadowing
  allowances for NTM and HVNTM only; photoresist 1.14 µm.[^pdk-03]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — SONOS cell W/L, programme/erase
  voltages, endurance.[^pdk-07]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — ASML i-line tools, tracks,
  metrology.[^skw-01]
* [SkyWater, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — photoresist suppliers.[^sec-01]

### High-level understanding

* [Wikipedia, *SONOS*](<https://en.wikipedia.org/wiki/SONOS>) — the charge-trapping cell.[^wiki-sonos]
* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line resolution.[^wiki-litho]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography and implant masking.[^txt-02]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 3](<https://openlibrary.org/isbn/9780961672157>) — LDD and
  drain-field engineering.[^txt-04]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — lithography
  tools of the era.[^txt-05]

### Deep dive

* [White, Adams and Bu, *IEEE Circuits & Devices* 2000](<https://doi.org/10.1109/101.857747>) — the SONOS
  cell, its tunnelling programme/erase and reliability.[^pap-01]
* [Eitan et al., *IEEE EDL* 2000](<https://doi.org/10.1109/55.877205>) — the NROM cell, whose hot-electron
  programming shows what a drain junction must *not* do in a
  tunnelling-programmed cell.[^eitan-2000]
* [Seo et al. (Samsung), *IEEE JSSC* 2005](<https://doi.org/10.1109/JSSC.2005.845564>) — a 130 nm embedded SONOS
  flash, for comparison of cell voltages and array design.[^pap-02]
* [Ogura et al. (IBM), *IEEE TED* 1980](<https://doi.org/10.1109/T-ED.1980.20040>) — the lightly doped drain, the
  design this "LD" tip returns to.[^ogura-1980]
* [Codella and Ogura (IBM), IEDM 1985](<https://doi.org/10.1109/IEDM.1985.190938>) — the halo that accompanies
  it.[^codella-1985]
* [Tran, McQueen and Kerr (Micron), US 6,759,288](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>) — a lighter LDD on
  selected transistors to cut junction leakage.[^pat-ldd-micron]
* [Gardner, Hause and Fulford (AMD), US 5,793,090](<https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5793090>) — separate LDD
  implants for different transistors on one chip.[^pat-multi-ldd-amd]
* [Hook et al. (IBM), *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — mask-proximity effects at the
  array edge.[^hook-2003]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the exposure options it lists by node for
  critical layers.[^itrs-03]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]

:::{dropdown} From patents shown as in force (US 8,093,128, estimated expiry 2028-10-22; US 8,796,098, estimated expiry 2034-02-26) — open to read
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — the
  embedded SONOS cell and its own implant steps.[^pat-04]
* Koutny et al. (Cypress), US 8,093,128 — integration of the
  charge-trap cell into a logic flow.[^pat-03]
:::

## Open questions

* **Select transistor.** Whether the select transistor of the
  {term}`2-T cell`, as well as the memory transistor, is inside the
  `ldntm` opening is not stated.

  The Error Messages page requires `ldntm` to enclose an "nFet" by 0.125
  (`ldntm.c4`) without naming the device.[^pdk-errors] Table F2b of the
  *Layers Reference* marks `LDNTM` as created for both "Flash npass" rows,
  both `nmos_core NV` rows, the four SONOS rows and the "NV SONOS
  Diode".[^pdk-06] On our reading these may include the select transistor,
  but neither source says so.
* **Resist thickness and tilt.** The resist thickness and the tilt at which
  the lightly doped tip is implanted are inferred; the PDK publishes no
  `LDNTM` shadowing parameter.[^pdk-03]
* **Why lightly doped.** The junction-leakage and disturb arguments above
  are our reading of the cell's published operating voltages;[^pdk-07] no
  public source states why the SONOS tip is lightly doped.
* **Exposure tool.** No public source places `LDNTM` on a particular
  exposure tool.

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
[^pdk-errors]: SkyWater PDK Authors, *Error Messages* page and
    `errors.csv`, SkyWater SKY130 PDK documentation, retrieved
    2026-09-14. <https://skywater-pdk.readthedocs.io/en/main/rules/errors.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/errors.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing". <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-sonos]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-04]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 3: The
    Submicron MOSFET*, Lattice Press, 1995, ISBN 978-0-9616721-5-7.
    <https://openlibrary.org/isbn/9780961672157>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^pap-01]: M. H. White, D. A. Adams and J. Bu, "On the go with SONOS",
    *IEEE Circuits and Devices Magazine* **16**(4), 22–31 (2000).
    <https://doi.org/10.1109/101.857747>
[^eitan-2000]: B. Eitan, P. Pavan, I. Bloom, E. Aloni, A. Frommer and
    D. Finzi, "NROM: A novel localized trapping, 2-bit nonvolatile
    memory cell", *IEEE Electron Device Letters* **21**(11), 543–545
    (2000). <https://doi.org/10.1109/55.877205>
[^pap-02]: M.-K. Seo et al. (Samsung), "A 130-nm 0.9-V 66-MHz 8-Mb
    (256K × 32) local SONOS embedded flash EEPROM", *IEEE Journal of
    Solid-State Circuits* **40**(4), 877–883 (2005).
    <https://doi.org/10.1109/JSSC.2005.845564>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pat-03]: W. Koutny et al. (Cypress Semiconductor), *Integration of
    non-volatile charge trap memory devices and logic CMOS devices*, US
    8,093,128 B2, granted 2012-01-10.
    <https://patents.google.com/patent/US8093128B2/en>
    Shown as in force; estimated expiry 2028-10-22 (estimate from public
    records, not legal advice).
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^codella-1985]: C. F. Codella and S. Ogura, "Halo doping effects in
    submicron DI-LDD device design", *IEDM 1985 Technical Digest*,
    pp. 230–233. <https://doi.org/10.1109/IEDM.1985.190938>
[^pat-ldd-micron]: L. C. Tran, M. McQueen and R. Kerr (Micron
    Technology), *Double LDD devices for improved DRAM refresh*, US
    6,759,288 B2, granted 2004-07-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6759288>
[^pat-multi-ldd-amd]: M. I. Gardner, F. N. Hause and H. J. Fulford
    (Advanced Micro Devices), *Integrated circuit having multiple LDD
    and/or source/drain implant steps to enhance circuit performance*,
    US 5,793,090 A, granted 1998-08-11.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5793090>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
