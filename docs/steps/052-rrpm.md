(step-052)=
# Step 052 — RRPM: Rev resistor protect mask

| | |
|---|---|
| **Step number** | 52 of 171[^steps-sheet] |
| **Step code** | `RRPM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — gate and poly resistors |
| **Previous step** | {ref}`P1IS <step-051>` |
| **Next step** | {ref}`PRI <step-053>` |

## What this step is

`RRPM` — the *reverse* resistor protect mask — is the complement of
{ref}`RPM <step-049>`. Where `RPM` left resist islands over the
resistor bodies and exposed everything else to the gate implant,
`RRPM` covers everything else and opens windows over the resistor
bodies, so that the p-type resistor implant {ref}`PRI <step-053>` goes
only where the gate implant did not. The resist is stripped at
{ref}`PRIS <step-054>`.

Unlike `RPM`, this mask is not in the PDK's public mask table, which
lists "Resistor Protect, RPM" but no reverse mask.[^pdk-05] That is not
surprising if, as we infer, the two {term}`reticles <reticle>` are generated from the same
drawn layer, `rpm` (GDS 86:20, "300 ohms/square polysilicon resistor
implant"),[^pdk-06] one in each tone, and a designer never needs to know
that two exist. That a reverse-tone mask is used is itself our
inference: the p-type resistor implant must reach the bodies that
`rpm` protected from the gate implant, and a reticle of the opposite
tone on the same layer does exactly that. We infer that the reverse reticle is
derived from `rpm` alone or from `rpm` less `urpm` (GDS 79:20, "2000
ohms/square polysilicon resistor implant"[^pdk-06]), depending on
whether the ultra-high-resistance bodies receive this implant as well as
their own ({ref}`URPM <step-055>`, {ref}`UPRI <step-056>`); the PDK says
only that for the 2000 Ω/sq resistors "a separate implant is used to set
the sheet resistance".[^pdk-07]

Beyond the step list, one public document names the mask: the pad
documentation of the SKY130 {term}`test tile` marks its shortest
300 Ω/sq poly resistors (W = 0.69 µm, L = 0.345 µm and W = 0.33 µm,
L = 0.33 µm) "(will not work for any routes using RRPM
mask)".[^raw-data-testtile-pads] It says nothing about the mask's tone
or how it is derived. The published measurements of the marked
structures read 0.49–0.54 kΩ (0.69 µm, half a square) and 0.97 kΩ
(0.33 µm, one square) (our extraction from the published measurements,
from the slope of the sweep within
±0.1 V),[^raw-data-passives] inside the limits of the PDK's e-test
table for its 0.69 µm half-square and 0.35 µm one-square
resistors[^pdk-07] — the tile's 0.33 µm structure is drawn narrower
than the narrowest supported fixed width (rpm.1b, 0.350 µm) and at the
poly.3 minimum resistor width of 0.330 µm.[^pdk-periph] The
files do not say which process route the measured wafer
followed.

## Step category

`RRPM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type, printed with the same relaxed
geometry as `RPM` — 1.27 µm features and 0.84 µm spaces (RPMCD /
RPMCDSP in the assumptions table)[^pdk-03] — on the same surface,
now the doped gate film. What is specific to this instance is the
tone: the windows are small and the resist is everywhere else, which
is the easier case for an implant mask (resist islands can lift or
shift; a continuous field of resist with holes in it cannot).

## Why this step exists

The two flavours of precision resistor in SKY130 are p-type films
with sheet resistances of 300 Ω/sq and 2000 Ω/sq[^pdk-07][^pdk-08]
inside a poly layer that is otherwise n⁺ at 48.2 Ω/sq.[^pdk-08] The
resistance of a {term}`poly resistor` is a steep function of its dose:
Seto's grain-boundary trapping model shows the resistivity falling by
orders of magnitude over a narrow doping range once the traps at the
boundaries are filled,[^seto-1975] and Mandurah, Saraswat and Kamins
refined the model with dopant segregation to the
boundaries.[^mandurah-1981] A precision resistor therefore needs its
own implant, at its own dose, into film that has received nothing
else. `RRPM` provides the window for it.

The mask also carries the resistor's matching budget. The head and tail
of each fixed-width resistor are contacted by slot contacts, and the PDK
models the device as an end resistance R₀ plus a body resistance R₁ =
R_SH/W per micrometre.[^pdk-07] The PDK says R₀ is "dominated by the
slot licons",[^pdk-07] but part of it is, we infer, set by where the
doped body meets the n⁺ poly and the contact — that is, by the `rpm`
edge — so the enclosure of the resistor by `rpm` (rpm.3, 0.200 µm) and
the ban on poly straddling `rpm` (rpm.8)[^pdk-periph] are what make R₀
reproducible. O'Dwyer and Kennedy compared the matching of different
poly resistor films in a CMOS process,[^odwyer-2009] and Tsang et al.
show how sensitive a high-value poly resistor bank is to its
surroundings by a different route: hydrogen diffusing through eroded
corners of the LPCVD nitride that caps the poly passivates
grain-boundary traps and lowers the resistance across the
bank.[^tsang-2014]

## How it is typically performed

An industry-generic implant-mask litho sequence, as on
{ref}`RPM <step-049>`, with the differences noted:

1. **Surface preparation.** {term}`HMDS` prime on the track. The surface is
   the doped a-Si film with the thin chemical oxide left by
   {ref}`P1IS <step-051>`.
2. **Resist coat.** i-line positive resist of about 1 µm (the PDK's
   general "Photoresist thickness" is 1.14 µm[^pdk-03]). The implant
   it must stop, {ref}`PRI <step-053>`, is a shallow poly implant at
   tens of keV (industry-typical), well within the stopping power of
   a micrometre of resist.
3. **Exposure.** i-line step-and-repeat through the reverse-tone
   reticle: opaque field, clear windows the size of the resistor
   bodies plus enclosure. The inference that the layer is printed on
   i-line rests on its 1.27 µm / 0.84 µm geometry, far above the
   i-line limit (category page, {term}`CD` = {term}`k₁ <k1>`·λ/{term}`NA`[^wiki-litho]).
4. **Alignment.** To the {term}`STI`/active marks of {ref}`FOM <step-004>`,
   as for `RPM`, because the poly is still unpatterned (inferred; the
   alignment tree is not public). Since both `RPM` and `RRPM` align to the
   same reference, their mutual {term}`overlay` is the sum of two
   registrations — the reason the drawn resistor is enclosed by `rpm` with
   margin[^pdk-periph] rather than butting the n⁺ region. Any gap between the
   `RPM` island and the `RRPM` window leaves an undoped strip of poly; any
   overlap leaves a strip doped both n⁺ and p, and Hook et al. show how
   lateral {term}`straggle` at a resist edge blurs the boundary
   further.[^hook-2003]
5. **Post-exposure bake, develop** in 2.38 % TMAH[^microchemicals-dev] (0.26 N; our arithmetic from TMAH's
   molar mass of 91.15 g/mol,[^wiki-tmah]
   taking the solution's density as about 1 g/mL), rinse,
   hard bake or UV cure.
6. **Inspection.** Overlay to active; open-window check by optical
   inspection.

**Reticle tone.** With positive resist, windows in resist correspond
to clear areas on a dark-field reticle; the reticle is therefore
mostly chrome. Neither tone nor resist is stated publicly.

## Machines typically used

* **{ref}`i-line <machine-i-line-stepper>` {term}`stepper`**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i), or a {ref}`KrF tool <machine-duv-krf-stepper>` (category page).
* **{ref}`Coat/develop track <machine-coat-develop-track>`**; **{ref}`overlay metrology <machine-cd-sem-overlay-metrology>`** and a {term}`CD-SEM` for
  periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper or scanner.**[^skw-01] Strength: strong for
  the tools; **inference** for the assignment of this layer.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius.**[^skw-01]
  Strength: strong.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM.**[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **i-line positive photoresist** ({ref}`lithography materials <material-lithography-materials>`; DNQ/novolac[^wiki-dnq]) from the
  suppliers named in SkyWater's 2021 S-1 (Dow, JSR, Tokyo Ohka
  Kogyo).[^sec-01]
* **HMDS**, **edge-bead remover**, **developer** (TMAH[^wiki-tmah]),
  {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The RRPM reticle** — chrome-on-quartz,[^wiki-mask] relaxed
  geometry; the second of the two reticles derived from `rpm`.

## Related steps and cross-references

* Previous: {ref}`P1IS <step-051>`. Next: {ref}`PRI <step-053>` (the
  implant through these windows); strip at {ref}`PRIS <step-054>`.
* Complement: {ref}`RPM <step-049>`. The ultra-high-resistance
  flavour has its own mask and implant: {ref}`URPM <step-055>`,
  {ref}`UPRI <step-056>`.
* The resistor is cut from the poly at {ref}`P1ME <step-062>` and
  contacted through {ref}`NPCM <step-078>` and {ref}`LICM1 <step-093>`.
* Previous mask step: {ref}`RPM <step-049>`; next mask step:
  {ref}`URPM <step-055>`.
* Mask page: {ref}`RRPM <mask-rrpm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

## References

### Cross-check

* SkyWater PDK, *Masks* page — `RPM` is listed; no reverse mask
  is.[^pdk-05]
* SkyWater PDK, *Layers Reference* — `rpm` 86:20 and `urpm`
  79:20.[^pdk-06]
* SkyWater PDK, *Device Details* — the P+ and P− poly precision
  resistors, the R₀/R₁ model, "a separate implant".[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — 48.2, 319.8 and
  2000 Ω/sq.[^pdk-08]
* SkyWater PDK, *Periphery rules* — rpm.3, rpm.7, rpm.8.[^pdk-periph]
* SkyWater PDK, *Criteria & Assumptions* — RPMCD 1.27 / 0.84 µm;
  photoresist 1.14 µm.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — i-line tools, tracks,
  overlay metrology.[^skw-01]
* SkyWater, Form S-1 — resist suppliers.[^sec-01]
* SKY130 raw-data repository, test-tile pad documentation — the
  poly-resistor (RRPM note) structures of the published test
  tile.[^raw-data-testtile-pads]
* SKY130 raw-data repository, measured data — I–V sweeps of those
  structures; the resistances quoted here are our
  extraction.[^raw-data-passives]

### High-level understanding

* Wikipedia, *Photolithography*, *Photomask*, *Diazonaphthoquinone*,
  *Tetramethylammonium hydroxide*.[^wiki-litho][^wiki-mask][^wiki-dnq][^wiki-tmah]
* Mack, *Fundamental Principles of Optical Lithography* — imaging,
  resist and process-window fundamentals.[^mack-2007]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography and implant masking.[^txt-02]

### Deep dive

* Seto, *J. Appl. Phys.* 1975 — the grain-boundary trapping model:
  why resistance is so sensitive to the dose this window
  admits.[^seto-1975]
* Mandurah, Saraswat and Kamins, *IEEE TED* 1981 — conduction in
  poly with dopant segregation, the refinement used for real
  resistors.[^mandurah-1981]
* Lu, Gerzberg and Meindl, *IEEE TED* 1982 — scaling limits of poly
  resistors in SRAM and logic, including the end-resistance
  problem.[^lu-1982]
* Upreti and Singh, *Bull. Mater. Sci.* 1991 — grain-boundary effects
  on the electrical properties of boron-doped poly films.[^upreti-1991]
* Kato and Ono, *Jpn. J. Appl. Phys.* 1996 — the temperature
  coefficient of heavily doped poly resistors and how processing
  changes it.[^kato-1996]
* Ashuah, Shauly and Shacham-Diamand, *IEEE TSM* 2009 — improving the
  TCR of boron-implanted poly resistors by co-implantation, a modern
  example of resistor-implant engineering.[^ashuah-2009]
* Chen et al., *Solid-State Electronics* 2000 — the voltage
  coefficient of poly resistors in a high-voltage CMOS
  technology.[^chen-2000]
* O'Dwyer and Kennedy, PRIME 2009 — matching of poly resistor films
  in a CMOS process.[^odwyer-2009]
* Tsang et al., *IEEE TSM* 2014 — resistance variation across
  high-value poly resistor banks traced to hydrogen diffusion through
  eroded LPCVD-nitride corners.[^tsang-2014]
* Hook et al., *IEEE TED* 2003 — lateral straggle at resist edges,
  which blurs the n⁺/p boundary this mask defines.[^hook-2003]
* Bossung, SPIE 1977 — the exposure–focus process window that every
  mask layer, however relaxed, is qualified against.[^bossung-1977]
* Levinson, *Principles of Lithography*, 4th ed. — mask tone, resist
  polarity and overlay in one reference.[^levinson-2019]
* ITRS 2001, *Lithography* — the exposure options it lists by node for
  critical layers.[^itrs-03]

## Open questions

* Whether the reverse reticle opens the `urpm` bodies as well as the
  `rpm` bodies is not public; it decides whether the 2000 Ω/sq film
  receives one implant or two.
* Reticle tone, resist and exposure tool are inferred, not stated.
* Whether the fab generates `RRPM` from the same data as `RPM` with a
  sizing bias (to guarantee overlap rather than a gap) is unknown.

<!-- footnotes -->

[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^wiki-dnq]: Wikipedia, *Diazonaphthoquinone*.
    <https://en.wikipedia.org/wiki/Diazonaphthoquinone>
[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^seto-1975]: J. Y. W. Seto, "The electrical properties of
    polycrystalline silicon films", *Journal of Applied Physics*
    **46**(12), 5247–5254 (1975). <https://doi.org/10.1063/1.321593>
[^mandurah-1981]: M. M. Mandurah, K. C. Saraswat and T. I. Kamins, "A
    model for conduction in polycrystalline silicon — Part I: Theory",
    *IEEE Transactions on Electron Devices* **28**(10), 1163–1171
    (1981). <https://doi.org/10.1109/T-ED.1981.20504>
[^lu-1982]: N. C.-C. Lu, L. Gerzberg and J. D. Meindl, "Scaling
    limitations of monolithic polycrystalline-silicon resistors in VLSI
    static RAM's and logic", *IEEE Transactions on Electron Devices*
    **29**(4), 682–690 (1982). <https://doi.org/10.1109/T-ED.1982.20762>
[^upreti-1991]: N. K. Upreti and S. Singh, "Grain boundary effect on
    the electrical properties of boron-doped polysilicon films",
    *Bulletin of Materials Science* **14**(6), 1331–1341 (1991).
    <https://doi.org/10.1007/BF02823239>
[^kato-1996]: K. Kato and T. Ono, "Change in Temperature Coefficient of
    Resistance of Heavily Doped Polysilicon Resistors Caused by
    Electrical Trimming", *Japanese Journal of Applied Physics*
    **35**(8R), 4209 (1996). <https://doi.org/10.1143/JJAP.35.4209>
[^ashuah-2009]: I. Ashuah, E. N. Shauly and Y. Shacham-Diamand,
    "Improvement of Temperature Coefficient of Resistance by
    Co-Implantation of Argon or Xenon or Fluorine in Boron Implanted
    Polysilicon Resistors", *IEEE Transactions on Semiconductor
    Manufacturing* **22**(2), 305–316 (2009).
    <https://doi.org/10.1109/TSM.2009.2017655>
[^chen-2000]: C.-H. Chen, Y.-K. Fang, M.-H. Kuo, Y.-L. Hsu and
    S.-L. Hsu, "A DC current stress method to improve the voltage
    coefficient of resistance of the polysilicon resistor in high
    voltage CMOS technology", *Solid-State Electronics* **44**(10),
    1743–1746 (2000). <https://doi.org/10.1016/S0038-1101(00)00138-6>
[^odwyer-2009]: T. G. O'Dwyer and M. P. Kennedy, "Comparison of
    resistor matching performance of polysilicon films in a CMOS
    process", *2009 Ph.D. Research in Microelectronics and Electronics
    (PRIME)*, pp. 80–83. <https://doi.org/10.1109/RME.2009.5201322>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^bossung-1977]: J. W. Bossung, "Projection Printing Characterization",
    *Proc. SPIE* **100**, 80–85 (1977).
    <https://doi.org/10.1117/12.955357>
[^levinson-2019]: H. J. Levinson, *Principles of Lithography*, 4th ed.,
    SPIE Press, 2019, ISBN 978-1-5106-2760-4.
    <https://doi.org/10.1117/3.2525393>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-14.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-passives]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the poly, diffusion
    and well resistors, MiM capacitors, varactors and bipolar
    transistors of the test tile, IC-CAP `.mdm` files in
    `sky130_fd_pr/cells/unsorted/`, `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>
