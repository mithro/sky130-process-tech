(step-055)=
# Step 055 — URPM: Ultra-high resistor poly mask

| | |
|---|---|
| **Step number** | 55 of 171[^steps-sheet] |
| **Step code** | `URPM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — gate and poly resistors |
| **Previous step** | {ref}`PRIS <step-054>` |
| **Next step** | {ref}`UPRI <step-056>` |

## What this step is

`URPM` opens resist windows over the bodies of the *ultra-high*
sheet-resistance {term}`poly resistors <poly resistor>` so that they can receive their own
implant, {ref}`UPRI <step-056>`. Everything else — the n⁺ gate film and
the 300 Ω/sq resistor bodies doped at {ref}`PRI <step-053>` — stays
under resist. The resist is stripped at {ref}`UPRIS <step-057>`.

:::{figure} /_static/figures/poly-055-urpm.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step a continuous film covers the whole slice. After it resist covers the whole slice without any opening.
:width: 560px
:name: fig-poly-055-urpm

Before, the bare gate film; after, resist over the whole slice. URPM opens only over the bodies of the ultra-high-value (`res_xhigh_po`) resistors,[^pdk-07] and the resistor drawn in this slice is read as a 300 Ω/sq one,[^pdk-07] so here the resist has no window. That the URPM reticle is made from `urpm` in the window tone is the page's inference; the PDK's mask table does not list it.[^pdk-05] The field oxide is drawn but not labelled, and the liner oxide is drawn faded; the wells and channel implants made earlier are not drawn. Not to scale.
:::


The device it serves is public. The PDK lists "P- poly precision
resistors" (`res_xhigh_po`) with the same five fixed widths and layout
footprints as the 300 Ω/sq family, and states that "a separate implant
is used to set the sheet resistance to 2000 ohm/sq"; at the time the
documentation was written their electrical and {term}`e-test` specifications
were "still TBD, once sufficient silicon has been evaluated".[^pdk-07]
The extraction table lists the "UHR poly resistor" at 2000 Ω/sq.[^pdk-08]
The drawn layer is `urpm` (GDS 79:20, "2000 ohms/square polysilicon
resistor implant").[^pdk-06] The resistor is one of the process's
advertised features: the repository README lists a "high sheet rho
poly resistor",[^pdk-10] the *Background* page lists "Poly resistor
(`r`)" among the technology-stack options,[^pdk-02] and Edwards's
WOSET paper describes the options as including "high and ultra-high
sheet ρ resistors".[^ann-15]

Like {ref}`RRPM <step-052>`, `URPM` is not in the PDK's public mask
table, which lists only `RPM` among the resistor masks.[^pdk-05] We
infer that the {term}`reticle` is generated from `urpm` in the window
(dark-field) tone, and that its geometry follows the `rpm` rules,
because the P− resistors share the P+ layout footprints.[^pdk-07] The
pad documentation of the SKY130 {term}`test tile` names the mask too,
marking the equivalent shortest 2 kΩ/sq resistors (W = 0.69 µm,
L = 0.345 µm and W = 0.33 µm, L = 0.33 µm) "(may not work for routes
using URPM mask)".[^raw-data-testtile-pads] The published measurements
of the marked structures read, from the slope of each sweep within
±0.1 V, 1.33–1.43 kΩ (0.33 µm, one square) and,
at 0.69 µm and half a square, 0.59 kΩ in one module against 2.8–3.1 kΩ
in another; the longer resistors of the family give a sheet resistance
of about 1 950 Ω/sq (our extraction from the published measurements;
see {ref}`UPRI <step-056>`).[^raw-data-passives]

## Step category

`URPM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type, printed on the doped gate film with
relaxed geometry (the `rpm` minimum width is 1.270 µm and spacing
0.840 µm[^pdk-periph]). Its special feature is the sensitivity of what
lies beneath the windows: the 2000 Ω/sq film is the highest-resistance
and therefore most lightly doped conductor in the process, and any
lithographic error that lets the implant stray — or the window
mis-size — shows up directly as resistor value and matching error.

## Why this step exists

A 2000 Ω/sq film lets a designer build resistors of hundreds of
kilohms to megohms in a few square micrometres, which is what bias
networks, reference ladders, RC filters and the load devices of
low-power analogue blocks need. It cannot be made from the 300 Ω/sq
film simply by drawing it longer: area, parasitic capacitance to the
substrate and matching all scale badly. It also cannot be made by
under-dosing the 300 Ω/sq implant on the same mask, because the two
values differ by between six and seven times in {term}`sheet resistance`
(2000 Ω/sq against the device page's 300 Ω/sq and the extraction
table's 319.8 Ω/sq)[^pdk-07][^pdk-08] and, on Seto's
model, sit on different parts of the steep resistance-versus-doping
curve,[^seto-1975] so they need separate, individually controlled
doses. Lane and Wrixon's published design space for implanted LPCVD
poly — sheet resistances from 40 to 2400 Ω/sq within a ±500 ppm/°C
temperature coefficient, for films 50–600 nm thick — puts 2000 Ω/sq at
the high end of what an ordinary implanted-poly resistor process
reaches, which is consistent with the PDK's caution about its
specifications.[^lane-1989][^pdk-07]

The price of a lightly doped poly resistor is variability. Its
resistance is dominated by grain-boundary barriers, so it is sensitive
to grain size, to the exact dose and to anything that changes the trap
density; Tsang et al. document resistance variation across banks of
high-value poly resistors and trace it to hydrogen diffusing through
eroded corners of the capping nitride and the overlying
oxide,[^tsang-2014] and Lane and Wrixon's design space (above) shows
how far into it a 2000 Ω/sq target sits. The PDK's own caution that
the P− resistor
specifications were "TBD" until enough silicon had been
measured[^pdk-07] is the practical face of the same physics. `URPM`
is where the process gives this device its own, separately
optimisable implant window.

## How it is typically performed

An industry-generic implant-mask litho sequence for a 200 mm, 130 nm-era
fab, as on {ref}`RRPM <step-052>`:

1. **Surface preparation.** {term}`HMDS` prime; the surface is the doped
   a-Si film with the chemical oxide left by {ref}`PRIS <step-054>`.
2. **Resist coat.** i-line positive resist of about 1 µm (the PDK's
   general figure is 1.14 µm[^pdk-03]); the implant it blocks is a
   light, low-energy poly implant.
3. **Exposure.** i-line {term}`stepper`, dark-field reticle with clear windows
   over the `urpm` bodies. The i-line assignment is inferred from the
   relaxed geometry (category page[^wiki-litho]); no SkyWater statement
   assigns layers to tools.
4. **Alignment.** To the {term}`STI`/active marks of {ref}`FOM <step-004>`,
   like the other two resistor masks (inferred; the alignment tree is not
   public); the resistor body will later be cut from the poly by
   {ref}`P1M <step-061>`, so the window must enclose the drawn body with
   {term}`overlay` margin on every side.
5. **Post-exposure bake, develop** in 2.38 %
   TMAH[^wiki-tmah][^microchemicals-dev] (0.26 N; our arithmetic from TMAH's
   molar mass of 91.15 g/mol,[^wiki-tmah]
   taking the solution's density as about 1 g/mL), rinse, hard bake.
6. **Inspection.** Overlay to active; window presence by optical
   inspection.

**Interaction with the other resistor masks.** If the `urpm` bodies
were covered at {ref}`RPM <step-049>` (no gate implant) and *not*
opened at {ref}`RRPM <step-052>` (no 300 Ω/sq implant), then
{ref}`UPRI <step-056>` is the only implant they receive and its dose
alone sets 2000 Ω/sq. If instead they were opened at `RRPM`, `UPRI`
would have to be a *counter*-doping or a very small additional dose,
which is implausible for a resistance six to seven times higher. The
first reading is the one this page uses, and is marked as an
inference; {ref}`RRPM <step-052>` leaves the question open and lists
it as an open question, so the two pages should be read together.

## Machines typically used

* **{ref}`i-line stepper <machine-i-line-stepper>`**, 200 mm (ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i), or a {ref}`KrF tool <machine-duv-krf-stepper>` (category page).
* **{ref}`Coat/develop track <machine-coat-develop-track>`**; **{ref}`overlay metrology <machine-cd-sem-overlay-metrology>`** and a {term}`CD-SEM` for
  periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper or scanner.**[^skw-01] Strength: strong for
  the tools; **inference** for the layer assignment.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius.**[^skw-01]
  Strength: strong.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM.**[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **i-line positive photoresist** ({ref}`lithography materials <material-lithography-materials>`)[^wiki-dnq] from the suppliers named
  in SkyWater's 2021 S-1 (Dow, JSR, Tokyo Ohka Kogyo).[^sec-01]
* **HMDS**, **edge-bead remover**, **developer** (2.38 % (0.26 N)
  TMAH[^wiki-tmah][^microchemicals-dev]), {ref}`DI water <material-ultrapure-water>`, {ref}`nitrogen <material-process-gases>`.
* **The URPM reticle** — chrome-on-quartz,[^wiki-mask] relaxed
  geometry, derived from `urpm`.

## Related steps and cross-references

* Previous: {ref}`PRIS <step-054>`. Next: {ref}`UPRI <step-056>`
  (the implant); strip at {ref}`UPRIS <step-057>`.
* The other resistor masks: {ref}`RPM <step-049>` (protect) and
  {ref}`RRPM <step-052>` (reverse, for the 300 Ω/sq flavour).
* Resistor bodies cut at {ref}`P1ME <step-062>`; contacted through
  {ref}`NPCM <step-078>` and {ref}`LICM1 <step-093>`.
* Previous mask step: {ref}`RRPM <step-052>`; next mask step:
  {ref}`P1M <step-061>`.
* Mask page: {ref}`URPM <mask-urpm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`High aspect ratio photolithographic method for high energy implantation <patent-gp23358573>` — US 6,576,405 B1 (1999)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — P− poly precision resistors,
  2000 Ω/sq, "a separate implant", specifications "TBD".[^pdk-07]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — UHR poly 2000 Ω/sq.[^pdk-08]
* [SkyWater PDK, *Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) — `urpm` 79:20.[^pdk-06]
* [SkyWater PDK, *Masks* page](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) — no ultra-high resistor mask
  listed.[^pdk-05]
* [SkyWater PDK, *Background*](<https://skywater-pdk.readthedocs.io/en/main/rules/background.html>) — "Poly resistor (`r`)" option.[^pdk-02]
* [SkyWater PDK, repository README](<https://github.com/google/skywater-pdk>) — "high sheet rho poly
  resistor".[^pdk-10]
* [Edwards (Efabless), WOSET 2020](<https://woset-workshop.github.io/PDFs/2020/a03.pdf>) — "high and ultra-high sheet ρ
  resistors".[^ann-15]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — `rpm` geometry.[^pdk-periph]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — photoresist thickness.[^pdk-03]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — litho tools.[^skw-01]
* [SkyWater, Form S-1](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — resist suppliers.[^sec-01]
* [SKY130 raw-data repository, test-tile pad documentation](<https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>) — the 2 kΩ/sq
  poly-resistor (URPM note) structures of the published test
  tile.[^raw-data-testtile-pads]
* [SKY130 raw-data repository, measured data](<https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells/unsorted>) — I–V sweeps of the 2 kΩ/sq
  structures; the resistances and sheet resistance quoted here are our
  extraction.[^raw-data-passives]

### High-level understanding

* Wikipedia, [*Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>), [*Photomask*](<https://en.wikipedia.org/wiki/Photomask>), [*Diazonaphthoquinone*](<https://en.wikipedia.org/wiki/Diazonaphthoquinone>),
  [*Tetramethylammonium hydroxide*](<https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>).[^wiki-litho][^wiki-mask][^wiki-dnq][^wiki-tmah]
* [Wikipedia, *Sheet resistance*](<https://en.wikipedia.org/wiki/Sheet_resistance>).[^wiki-rs]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography.[^txt-02]
* [Kamins, *Polycrystalline Silicon for Integrated Circuits and
  Displays*](<https://doi.org/10.1007/978-1-4615-5577-3>) — lightly doped poly.[^kamins-1998]
* [MicroChemicals, *Development of photoresists*](<https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>) — practical
  develop-process notes, including the 2.38 % TMAH
  developers.[^microchemicals-dev]

### Deep dive

* [Seto, *J. Appl. Phys.* 1975](<https://doi.org/10.1063/1.321593>) — the model that puts 300 and
  2000 Ω/sq on different parts of the same curve.[^seto-1975]
* [Tsang et al., *IEEE TSM* 2014](<https://doi.org/10.1109/TSM.2014.2311375>) — resistance variation across
  high-value poly resistor banks traced to hydrogen diffusion through
  eroded LPCVD-nitride corners.[^tsang-2014]
* [Wright et al., *J. Vac. Sci. Technol. B* 2010](<https://doi.org/10.1116/1.3466531>) — rf-sputtered
  Cr–Si–B–SiO₂/Al₂O₃ thin-film resistors reaching 20 kΩ/sq at
  <200 ppm/°C: the non-poly route to a high-sheet-resistance, low-TCR
  film, and the yardstick the implanted-poly resistor is measured
  against.[^wright-2010]
* [Lane and Wrixon, *IEEE TED* 1989](<https://doi.org/10.1109/16.22479>) — the design of thin-film poly
  resistors for analogue ICs, and the published design space that
  brackets the 2000 Ω/sq target.[^lane-1989]
* [Lu, Gerzberg, Lu and Meindl, *IEEE TED* 1981](<https://doi.org/10.1109/T-ED.1981.20437>) — poly resistor
  optimisation.[^lu-1981]
* [Lu, Gerzberg and Meindl, *IEEE TED* 1982](<https://doi.org/10.1109/T-ED.1982.20762>) — scaling limits of
  high-value poly resistors.[^lu-1982]
* [Kato and Ono, *Jpn. J. Appl. Phys.* 1996](<https://doi.org/10.1143/JJAP.35.4209>) — temperature-coefficient
  changes in poly resistors.[^kato-1996]
* [Upreti and Singh, *Bull. Mater. Sci.* 1991](<https://doi.org/10.1007/BF02823239>) — grain-boundary effects
  in boron-doped poly.[^upreti-1991]
* [Chen et al., *Solid-State Electronics* 2000](<https://doi.org/10.1016/S0038-1101(00)00138-6>) — voltage coefficient of
  poly resistors, largest for the lightest doping.[^chen-2000]
* [Hook et al., *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — {term}`straggle` at resist edges.[^hook-2003]
* [Buffat and Adams (Zilog), US 6,576,405](<https://patents.google.com/patent/US6576405B1/en>) — implant-mask lithography
  design space.[^pat-resist-zilog]
* [Bossung, SPIE 1977](<https://doi.org/10.1117/12.955357>) — the exposure–focus process window.[^bossung-1977]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on photoresists and
  overlay.[^levinson-2005]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the exposure options it lists by node for
  critical layers.[^itrs-03]

## Open questions

* This page treats `URPM` and {ref}`RRPM <step-052>` as separate
  reticles, on the strength of the PDK's "separate implant" and two
  drawn layers; one reticle with two implant recipes would also fit
  the public sources.
* Whether the `urpm` bodies receive only {ref}`UPRI <step-056>` (the
  reading used here) is inferred.
* Whether the ultra-high resistor is a process option in the sense of
  the *Background* page's `r` suffix — i.e. whether this mask is
  skipped on some product flows — is not stated.
* Reticle tone, resist and exposure tool are inferred.

<!-- footnotes -->

[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-02]: SkyWater PDK Authors, *Background*, SkyWater SKY130 PDK
    documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/background.html>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^ann-15]: R. T. Edwards (Efabless), "Google/SkyWater and the Promise of
    the Open PDK", *Workshop on Open-Source EDA Technology (WOSET)
    2020*. <https://woset-workshop.github.io/PDFs/2020/a03.pdf>
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
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^kamins-1998]: T. Kamins, *Polycrystalline Silicon for Integrated
    Circuits and Displays*, 2nd ed., Kluwer Academic, 1998.
    <https://doi.org/10.1007/978-1-4615-5577-3>
[^seto-1975]: J. Y. W. Seto, "The electrical properties of
    polycrystalline silicon films", *Journal of Applied Physics*
    **46**(12), 5247–5254 (1975). <https://doi.org/10.1063/1.321593>
[^tsang-2014]: Y. Tsang, R. Shiono, G. Pfeffer and S. Kwan,
    "Characterization and Understanding of High Valued Polysilicon
    Resistor Resistance Variation Across a Resistor Bank With Parallel
    Resistor Fingers", *IEEE Transactions on Semiconductor
    Manufacturing* **27**(2), 294–300 (2014).
    <https://doi.org/10.1109/TSM.2014.2311375>
[^wright-2010]: S. W. Wright, C. P. Judge, M. J. Lee, D. F. Bowers,
    M. Dunbar and C. D. Wilson, "High sheet resistance, low temperature
    coefficient of resistance resistor films for integrated circuits",
    *Journal of Vacuum Science & Technology B* **28**(4), 834–840
    (2010). <https://doi.org/10.1116/1.3466531>
[^lane-1989]: W. A. Lane and G. T. Wrixon, "The design of thin-film
    polysilicon resistors for analog IC applications", *IEEE
    Transactions on Electron Devices* **36**(4), 738–744 (1989).
    <https://doi.org/10.1109/16.22479>
[^lu-1981]: N. C.-C. Lu, L. Gerzberg, C.-Y. Lu and J. D. Meindl,
    "Modeling and optimization of monolithic polycrystalline silicon
    resistors", *IEEE Transactions on Electron Devices* **28**(7),
    818–830 (1981). <https://doi.org/10.1109/T-ED.1981.20437>
[^lu-1982]: N. C.-C. Lu, L. Gerzberg and J. D. Meindl, "Scaling
    limitations of monolithic polycrystalline-silicon resistors in VLSI
    static RAM's and logic", *IEEE Transactions on Electron Devices*
    **29**(4), 682–690 (1982). <https://doi.org/10.1109/T-ED.1982.20762>
[^kato-1996]: K. Kato and T. Ono, "Change in Temperature Coefficient of
    Resistance of Heavily Doped Polysilicon Resistors Caused by
    Electrical Trimming", *Japanese Journal of Applied Physics*
    **35**(8R), 4209 (1996). <https://doi.org/10.1143/JJAP.35.4209>
[^upreti-1991]: N. K. Upreti and S. Singh, "Grain boundary effect on
    the electrical properties of boron-doped polysilicon films",
    *Bulletin of Materials Science* **14**(6), 1331–1341 (1991).
    <https://doi.org/10.1007/BF02823239>
[^chen-2000]: C.-H. Chen, Y.-K. Fang, M.-H. Kuo, Y.-L. Hsu and
    S.-L. Hsu, "A DC current stress method to improve the voltage
    coefficient of resistance of the polysilicon resistor in high
    voltage CMOS technology", *Solid-State Electronics* **44**(10),
    1743–1746 (2000). <https://doi.org/10.1016/S0038-1101(00)00138-6>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*,
    US 6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^bossung-1977]: J. W. Bossung, "Projection Printing Characterization",
    *Proc. SPIE* **100**, 80–85 (1977).
    <https://doi.org/10.1117/12.955357>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1. <https://doi.org/10.1117/3.601520>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
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
