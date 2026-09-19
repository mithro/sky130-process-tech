(step-135)=
# Step 135 — CAPILD: Capacitor ILD oxynitride deposition

| | |
|---|---|
| **Step number** | 135 of 171[^steps-sheet] |
| **Step code** | `CAPILD` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`WTIAL3 <step-134>` |
| **Next step** | {ref}`CAPTIW1 <step-136>` |

## What this step is

`CAPILD` deposits the dielectric of SKY130's first
{term}`metal–insulator–metal (MiM) capacitor <MiM capacitor>`. Straight after the blanket
metal-3 stack of {ref}`WTIAL3 <step-134>` is sputtered — and before
that metal is patterned — a thin dielectric film, described in this
reference as a silicon {term}`oxynitride` (inference, see below), is
laid over the whole wafer by {term}`PECVD`. A thin conductor film
(titanium–tungsten on this reference's reading) follows at
{ref}`CAPTIW1 <step-136>`; the two are then cut into
capacitor *top plates* by the `capm` mask and etch
({ref}`CAPM <step-137>`, {ref}`CAPME <step-138>`), and only then is
metal 3 itself patterned ({ref}`MM3 <step-139>`,
{ref}`MM3E <step-140>`). The capacitor's *bottom plate* is therefore
metal 3, its dielectric is this film, and its top plate is the
conductor of the next step. The PDK's device documentation describes exactly this
construction: "The MiM capacitor is constructed using a thin
dielectric over metal, followed by a thin conductor layer on top of
the dielectric", with "CAPM over Metal-3" and "CAP2M over Metal-4" as
the two "identical" constructions,[^pdk-07] and its cross-section
drawing for the device labels the dielectric between "M3 (plate 1)"
and "CAPM" as "CAPILD" — the name of this step.[^pdk-07] The layer
table calls `capm` (GDS 89:44) the "MiM capacitor plate over
metal 3",[^pdk-06] and the process stack diagram draws `capm` between
`metal3` and `metal4`, beside `via3`.[^pdk-04] The second capacitor,
`cap2m` over metal 4, is the subject of {ref}`CAPILD2 <step-150>` to
{ref}`CAP2ME <step-153>` and is not discussed further here.

What is public about the film is electrical, not physical. The PDK
gives the capacitor an area capacitance `CMIMA` of 2 fF/µm² (limits
1.8–2.2), a periphery capacitance `CMIMP` of 0.19 fF/µm, a top-plate
{term}`sheet resistance` `RSCAPM` of 5.8 Ω/sq, and models valid for
plate voltages of 0–5.0 V; its e-test table sets the `CMIMP` limits
at 0.11–0.27 fF/µm.[^pdk-07]

Measured values are public as well. The SKY130 raw-data repository
publishes capacitance–voltage sweeps of the test tile's "CAPM on M3"
capacitors, whose areas and perimeters the pad list
gives.[^raw-data-testtile-pads][^raw-data-passives] Fitted over
−3.3 V to +3.3 V, the 11-plate, 17 600 µm² capacitor measures 33.26 pF
at 0 V. Solving the area-intensive (5 × 35 × 35 µm) and
periphery-intensive (72 × 2 × 35 µm) structures for an area and a
periphery term gives 1.87 fF/µm² and 0.18 fF/µm, both inside the
e-test limits, and those two terms predict the large capacitor to
within 0.3 %; a copy of it with "seas of via-2's" under the plates
measures 0.08 % more (our extraction from the published measurements,
with no correction for pad and wiring capacitance; the files record no
measurement frequency, temperature, date or
wafer).[^raw-data-passives]

Neither the dielectric's
thickness nor its permittivity is labelled anywhere in the PDK; the
stack diagram carries no thickness for `capm` or its dielectric.[^pdk-04]
The PDK does not name the dielectric. This reference describes it as
a PECVD silicon oxynitride (inference): SkyWater's capability list
includes "PECVD silane oxide/nitride/oxynitride, C1 – low temp, range
of R.I. options",[^skw-01] and PECVD nitride and oxynitride were the
MiM dielectrics of the period.[^kar-roy-1999][^ng-2003] From the
capacitance density one can
bound the thickness: with {math}`C/A = \varepsilon_0 k / d`, a film
giving 2 fF/µm² is {math}`d \approx 4.4\,\mathrm{nm} \times k`, so
about 18 nm for an oxide-like {math}`k = 4`, 22–27 nm for a mid-range
oxynitride ({math}`k \approx 5`–6) and 33 nm for the {math}`k = 7.5`
the PDK labels for its nitride films (TOPNIT, SPNIT).[^pdk-04] With
the measured 1.87 fF/µm² instead, the factor is about 4.7 nm and each
thickness about 7 % larger.[^raw-data-passives] This is our arithmetic
with an assumed permittivity, not a published number; 1–2 fF/µm² is
also the density the published Al-BEOL
PECVD-nitride MiM processes of the period reported.[^kar-roy-1999]

## Step category

`CAPILD` is a {ref}`Thin-film deposition <category-deposition>` step
of the *PECVD dielectric* class — the category page's PECVD section
— but it is one of the two PECVD films in the flow deposited *as a
device layer* (with {ref}`CAPILD2 <step-150>`): its thickness sets a
capacitance the models promise, not a spacing the design rules merely
bound. That changes the priorities.
Uniformity, wafer-to-wafer repeatability, low pinhole density,
breakdown strength at 5 V across some 20–30 nm (a field of order
2 MV/cm; our arithmetic), low leakage and a small, stable voltage
coefficient matter here in the way they matter for a gate oxide, and
{term}`step coverage` does not, because the film lies on a blanket,
freshly sputtered, planar metal surface. Its nearest relative in the
flow is the {ref}`LINIT <step-104>` nitride over the local
interconnect; its closest published analogues are the PECVD nitride
and oxynitride MiM dielectrics of the 0.25–0.13 µm mixed-signal
generation.[^kar-roy-1999][^babcock-2001][^ng-2003]

## Why this step exists

* **An analogue capacitor with metal plates.** SkyWater and Google
  list MiM capacitors among SKY130's features — "Optional MiM
  capacitors" in the PDK's README, which also counts MiM capacitors
  among the "normally optional features" SKY130 includes "as
  standard";[^pdk-10] "MiM Capacitor" in the S130 platform
  table;[^skw-02] and "MiM capacitors" among the "normally optional
  features" SKY130 offers "as standard".[^ann-11] A
  capacitor whose plates are metal has no
  depletion layer, so its capacitance barely changes with bias and
  its series resistance is small; the alternatives — a poly–poly or
  MOS capacitor — are slower, more nonlinear and consume front-end
  area. Kar-Roy et al. (Conexant) and Babcock et al. (Texas
  Instruments) document why mixed-signal and RF processes of this
  era added a PECVD-nitride MiM to an aluminium back end, and what
  linearity it achieved;[^kar-roy-1999][^babcock-2001] Ng et al.
  (Chartered) review the integration choices.[^ng-2005]
* **Why the dielectric goes on unpatterned metal 3.** Depositing the
  dielectric on the blanket metal, and defining the top plate before
  the bottom metal is etched, gives the capacitor a perfectly planar
  bottom plate with no topography under the thin film and no
  sidewall at which it could thin or leak; the whole sandwich is made
  in three depositions with one extra mask. This is the scheme of the
  Newport Fab patent,[^pat-mim-newportfab] and, we infer from the PDK's
  description of a thin dielectric over metal followed by a thin
  conductor,[^pdk-07] SKY130's; IBM's patent reaches a planar bottom plate by
  damascene and CMP instead.[^pat-mim-ibm] The price is that
  the metal-3 etch must later cut through the dielectric wherever it
  remains ({ref}`MM3E <step-140>`).
* **Oxynitride rather than oxide or nitride.** PECVD silicon nitride
  has the highest permittivity of the three (k ≈ 7.5 on the PDK's own
  labelling[^pdk-04]) and so the highest density per thickness, but it
  traps charge and shows a frequency-dependent ("dispersive")
  capacitance, as Van Huylenbroeck et al. showed;[^van-huylenbroeck-2002] oxide is more
  linear but needs to be thinner for the same density. Ng, Chew and
  Chu compared PECVD nitride and oxynitride MiM capacitors and found
  both gave low leakage, high breakdown field, no dispersion and good
  linearity;[^ng-2003] the composition — and hence {math}`k` — of a
  PECVD oxynitride is set by the N₂O/NH₃ ratio, as Denisse et al.
  and Bose, Bose and Basa characterised.[^denisse-1986][^bose-2002]
  SkyWater's "range of R.I. options"[^skw-01] is the public trace of
  a tunable film.
* **Voltage and temperature coefficients.** The models are valid to
  5 V,[^pdk-07] so the quadratic {term}`voltage coefficient` matters;
  Blonkowski and Gonon and Vallée give the physical interpretation of
  the {math}`C(V)` curvature in amorphous dielectrics.[^blonkowski-2007][^gonon-2007]
  Whether the PDK publishes coefficients for `cap_mim` is not
  something we could confirm; the device page lists only the three
  parameters above.[^pdk-07] The published C–V sweeps of the four
  first-level test structures fit quadratic coefficients of +32 to
  +40 ppm/V² over ±3.3 V, and the fitted capacitance at ±3.3 V is
  within 0.05 % of that at 0 V (our fit); they contain no temperature
  data.[^raw-data-passives]

Without `CAPILD` there would be nothing between metal 3 and the TiW
of {ref}`CAPTIW1 <step-136>`, and the `capm` mask would define a short
rather than a capacitor.

## How it is typically performed

An industry-generic PECVD MiM-dielectric deposition on an aluminium
back end (SKY130's recipe is not public):

1. **Surface.** The wafer comes from the {term}`PVD` cluster with its
   refractory cap exposed ({ref}`WTIAL3 <step-134>`; TiW or TiN, which
   the public record does not settle,
   {ref}`overview-metal-cap`); the cap is the actual bottom
   electrode surface, and its smoothness and cleanliness set the
   leakage. Some flows pre-treat the electrode in an NH₃ or N₂
   plasma — the Philips patent claims an ammonia-plasma treatment of
   the bottom electrode to reduce its oxidation[^pat-mim-philips] —
   and the queue time from PVD to deposition is limited (industry
   practice[^txt-05]).
2. **Chamber and temperature.** A single-wafer or multi-station PECVD
   reactor at 300–400 °C (industry-typical for films on
   aluminium[^txt-05][^chapple-sokol-1989]); SkyWater's "C1" silane
   chamber "low temp" option[^skw-01] is the candidate.
3. **Chemistry.** SiH₄ with N₂O and NH₃ (and N₂ or He) in an RF
   plasma; the N₂O:NH₃ ratio moves the film from oxide to nitride,
   with refractive index and permittivity following the
   composition.[^denisse-1986][^bose-2002] Lieberman and Lichtenberg
   treat the discharge physics.[^lieberman-2005]
4. **Thickness.** Not public; 18–33 nm by the arithmetic above for
   2 fF/µm²,[^pdk-07] deposited in tens of seconds (industry-typical
   for PECVD rates[^txt-05]), and controlled to
   a few per cent because capacitance scales inversely with it.
   Kar-Roy et al. report 1.0–2.0 fF/µm² from a PECVD
   nitride;[^kar-roy-1999] Babcock et al. found nitride MiM linearity
   close to that of oxide at 1 MHz but degrading at lower frequencies
   through dispersion.[^babcock-2001]
5. **Post-treatment.** Some processes densify or plasma-treat the
   film to reduce hydrogen and traps — the dispersion Van
   Huylenbroeck et al. traced to the nitride[^van-huylenbroeck-2002]
   — and to stabilise the {math}`C(V)` curve; whether SKY130 does is
   not public.
6. **Metrology.** Thickness and refractive index by ellipsometry on
   monitors (the "R.I. options" SkyWater names[^skw-01]); capacitance
   density, leakage, breakdown, {math}`C(V)` and matching on
   capacitor test structures at {term}`e-test`, against the `CMIMA`,
   `CMIMP` and `RSCAPM` limits of the PDK.[^pdk-07]

## Machines typically used

* **{ref}`PECVD dielectric system <machine-pecvd>`**, 200 mm: Novellus Concept One/Two or
  Sequel,[^novellus-history] Applied Materials Producer or Centura
  DxZ[^amat-10k] ({ref}`category-deposition`).
* **{ref}`Spectroscopic ellipsometer <machine-film-thickness-metrology>`** for thickness and index; **{ref}`C–V and leakage probers <machine-parametric-tester>`** at e-test.

## Machines likely used at SkyWater

* **PECVD silane "C1" chamber.** SkyWater lists "PECVD silane
  oxide/nitride/oxynitride, C1 – low temp, range of R.I.
  options".[^skw-01] Strength: **strong** for the capability, since
  it is the only oxynitride process on the list; the assignment of
  this chamber to this step is an **inference** from the film type
  described here and the low-temperature option, and the reading of "C1" as a
  Novellus Concept One[^novellus-history] is also an **inference**.
* **PECVD TEOS "C2 and Producer"**[^skw-01] is not a nitride source
  and is unlikely here (weak).

## Resources required

* **{ref}`Silane <material-precursors>`, {ref}`nitrous oxide <material-process-gases>`, ammonia**, with **nitrogen or helium** diluent,
  for the oxynitride.[^denisse-1986][^wiki-pecvd] Gas suppliers named in
  SkyWater's filings: Air Products and Praxair (2021 S-1), Linde and Airgas
  (fiscal 2023 10-K).[^sec-01][^sec-02]
* **{ref}`NF₃ <material-etch-gases>`** for the chamber clean; **nitrogen** purge.
* **{ref}`Showerhead, heater and liner consumables <material-hardware-consumables>`**; **{ref}`monitor wafers <material-substrates>`**
  with the metal-3 stack for thickness and capacitance checks.

## Related steps and cross-references

* Previous: {ref}`WTIAL3 <step-134>` (the metal-3 stack that is the
  bottom plate). Next: {ref}`CAPTIW1 <step-136>` (the top-plate
  metal), then {ref}`CAPM <step-137>` and {ref}`CAPME <step-138>`.
* The etch that later removes this film outside the capacitors:
  {ref}`MM3E <step-140>`; the via that contacts the finished top
  plate: {ref}`VIM3 <step-144>`, {ref}`VIM3E <step-145>`.
* The second capacitor, over metal 4: {ref}`CAPILD2 <step-150>`,
  {ref}`CAPTIW2 <step-151>`, {ref}`CAP2M <step-152>`,
  {ref}`CAP2ME <step-153>`.
* Other nitride films of the flow: {ref}`LINIT <step-104>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,005,102 A <patent-gp23452232>` — Multilayer electrodes for integrated circuit capacitors (1989)
* {ref}`US 5,170,242 A <patent-gp27034223>` — Reaction barrier for a multilayer structure in an integrated circuit (1991)
* {ref}`US 5,708,559 A <patent-gp24193081>` — Precision analog metal-metal capacitor (1995)
* {ref}`US 6,430,028 B1 <patent-gp24897586>` — Method for fabrication of an MIM capacitor and related structure (2000)
* {ref}`US 6,717,193 B2 <patent-gp25521092>` — Metal-insulator-metal (MIM) capacitor structure and methods of fabricating same (2001)
* {ref}`US 7,375,002 B2 <patent-gp37568077>` — MIM capacitor in a semiconductor device and method therefor (2005)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 7,166,902 B1 <patent-gp37663627>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, *Device Details* — MiM capacitor construction ("thin
  dielectric over metal, followed by a thin conductor"), `CMIMA`
  2 fF/µm², `CMIMP` 0.19 fF/µm, `RSCAPM` 5.8 Ω/sq, 0–5 V; the
  `cap_mim` cross-section with its "CAPILD" label.[^pdk-07]
* SkyWater PDK, *Layers Reference* — `capm` 89:44 "MiM capacitor
  plate over metal 3"; `cap2m` 97:44.[^pdk-06]
* SkyWater PDK, *Process stack diagram* — `capm` between `metal3` and
  `metal4`; nitride permittivities 7.3–7.5.[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — `CAPMCD` 2 µm, `CAPMCDSP`
  0.84 µm; MiM capacitor aspect ratio 20.[^pdk-03]
* SkyWater PDK, *Periphery rules* — the `capm` rule set.[^pdk-periph]
* SkyWater PDK, *Parasitic Layout Extraction* — the `cap_mim_m3`
  extraction notes.[^pdk-08]
* SkyWater PDK, README — "Optional MiM capacitors".[^pdk-10]
* SkyWater, S130 platform table — "MiM Capacitor".[^skw-02]
* SkyWater / Efabless, first MPW shuttle release — MiM capacitors
  offered as standard.[^ann-11]
* SkyWater, *Facilities & Capabilities* — "PECVD silane
  oxide/nitride/oxynitride, C1 – low temp, range of R.I. options".[^skw-01]
* SKY130 raw-data repository — C–V sweeps of the first-level MiM test
  capacitors and the pad list that gives their areas and perimeters;
  the capacitance terms and voltage coefficients quoted here are our
  extraction.[^raw-data-passives][^raw-data-testtile-pads]

### High-level understanding

* Wikipedia, *Capacitor*, *Silicon oxynitride*, *Silicon nitride*,
  *Plasma-enhanced chemical vapor deposition*.[^wiki-capacitor][^wiki-sion][^wiki-sin][^wiki-pecvd]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — passive
  components and PECVD dielectrics in the deep-submicron back
  end.[^txt-05]
* Edwards, WOSET 2020 and the 2021 lecture slides — the SKY130 stack
  with its `capm`/`cap2m` placement, from the open-PDK
  side.[^ann-15][^ann-16]

### Deep dive

* Kar-Roy et al. (Conexant), IITC 1999 — high-density MiM capacitors
  with a PECVD nitride in the back end of a 0.25 µm CMOS flow
  (aluminium, by the date; the abstract does not name the
  metal).[^kar-roy-1999]
* Babcock et al. (TI), *IEEE EDL* 2001 — the frequency dependence and
  voltage linearity of PECVD-nitride MiMs, and the dispersion that
  degrades them below 1 MHz.[^babcock-2001]
* Van Huylenbroeck et al. (IMEC), *IEEE EDL* 2002 — dispersion in
  PECVD dielectrics and how to avoid it.[^van-huylenbroeck-2002]
* Ng, Chew and Chu (Chartered), *IEEE EDL* 2003 — PECVD nitride
  versus oxynitride as the MiM dielectric.[^ng-2003]
* Ng et al. (Chartered), *IEEE TED* 2005 — MiM integration for
  mixed-signal/RF reviewed.[^ng-2005]
* Armacost et al. (IBM/Infineon), IEDM 2000, and Mahnkopf et al.,
  IEDM 1999 — a high-reliability MiM in a 0.18 µm platform.[^armacost-2000][^mahnkopf-1999]
* Denisse et al., *J. Appl. Phys.* 1986, and Bose, Bose and Basa,
  *Mater. Lett.* 2002 — composition and index of PECVD
  oxynitride.[^denisse-1986][^bose-2002]
* Blonkowski, *Appl. Phys. Lett.* 2007, and Gonon and Vallée, *Appl.
  Phys. Lett.* 2007 — the physics of the MiM voltage
  coefficient.[^blonkowski-2007][^gonon-2007]
* Kar-Roy and Racanelli (Newport Fab), US 6,430,028 — a nitride/TiN
  capacitor on an aluminium interconnect layer.[^pat-mim-newportfab]
* Brabazon et al. (IBM), US 5,708,559 — the precision analogue
  metal–metal capacitor.[^pat-mim-ibm]
* Olewine and Saiz (Philips), US 6,717,193 — bottom-electrode plasma
  treatment and top-plate etching.[^pat-mim-philips]
* Roberts and Huffman (Freescale), US 7,375,002 — a MiM over
  planarised interconnect.[^pat-mim-freescale]
* Chapple-Sokol, Tierney and Batey (IBM), MRS 1989 — RF-power
  dependence of PECVD film properties.[^chapple-sokol-1989]
* Lieberman and Lichtenberg — the plasma physics of the
  deposition.[^lieberman-2005]

## Open questions

* The dielectric's composition, permittivity, thickness and
  deposition conditions are not public; 18–33 nm is our estimate
  from the 2 fF/µm² of the PDK[^pdk-07] with an assumed {math}`k`
  (about 7 % more from the measured 1.87 fF/µm²[^raw-data-passives]).
* Whether the film is a single oxynitride or an oxide/nitride stack,
  and whether it receives a plasma treatment or anneal, is not public.
* The PDK is not self-consistent here. The device page, the layer
  table and the stack diagram place `capm` over metal
  3,[^pdk-07][^pdk-06][^pdk-04] but the `capm` periphery rules (values
  "N/A") name `met2` and `via2` ("Minimum enclosure of capm
  (top_plate) by met2", "Min enclosure of via2 by capm", "Min spacing
  between capm and via2"), the via2 rule table says via2 connects
  "met2/capm to met3 in the SKY130DI* flow",[^pdk-periph] and the
  extraction table describes `cap_mim` with via2, m3 and "capm-m2"
  terminals.[^pdk-08] We follow the metal-3 reading, which the test
  tile's pad documentation shares ("CAPM on M3")[^raw-data-testtile-pads]
  and which the `cap_mim` cross-section supports further: the
  cross-section labels the via that lands on "CAPM" — the only via it
  labels — "Via3";[^pdk-07] the met2/via2
  wording may come from a flow variant with the capacitor one level
  lower (inference).
* Whether voltage and temperature coefficients for `cap_mim` are
  published in the PDK models is not confirmed here; the published
  test-tile sweeps give a voltage dependence but no temperature
  dependence.[^raw-data-passives]
* The mask table lists "Capacitor MiM, CAPM" without the "used in
  SKY130" flag,[^pdk-05] consistent with the README's "optional"
  wording;[^pdk-10] whether every SKY130 lot carries the capacitor
  steps is not public.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
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
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page,
    SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-02]: SkyWater Technology, *Mixed-Signal CMOS & ROIC*, platform
    table, accessed 2026-09-13. <https://www.skywatertechnology.com/cmos/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^ann-11]: SkyWater / Efabless, *First Google-Sponsored MPW Shuttle
    Launched at SkyWater with 40 Open Source Community Submitted
    Designs*, 2021-04-06.
    <https://www.skywatertechnology.com/first-google-sponsored-mpw-shuttle-launched-at-skywater-with-40-open-source-community-submitted-designs/>
[^ann-15]: R. T. Edwards (Efabless), "Google/SkyWater and the Promise of
    the Open PDK", *Workshop on Open-Source EDA Technology (WOSET)
    2020*. <https://woset-workshop.github.io/PDFs/2020/a03.pdf>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^wiki-capacitor]: Wikipedia, *Capacitor*.
    <https://en.wikipedia.org/wiki/Capacitor>
[^wiki-sion]: Wikipedia, *Silicon oxynitride*.
    <https://en.wikipedia.org/wiki/Silicon_oxynitride>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^kar-roy-1999]: A. Kar-Roy, C. Hu, M. Racanelli, C. A. Compton,
    P. Kempf, G. Jolly, P. N. Sherman, J. Zheng, Z. Zhang and A. Yin,
    "High density metal insulator metal capacitors using PECVD nitride
    for mixed signal and RF circuits", *Proc. IEEE 1999 International
    Interconnect Technology Conference (IITC)*, pp. 245–247.
    <https://doi.org/10.1109/IITC.1999.787134>
[^babcock-2001]: J. A. Babcock, S. G. Balster, A. Pinto, C. Dirnecker,
    P. Steinmann, R. Jumpertz and B. El-Kareh, "Analog characteristics
    of metal-insulator-metal capacitors using PECVD nitride
    dielectrics", *IEEE Electron Device Letters* **22**(5), 230–232
    (2001). <https://doi.org/10.1109/55.919238>
[^van-huylenbroeck-2002]: S. Van Huylenbroeck, S. Decoutere,
    R. Venegas, S. Jenei and G. Winderickx, "Investigation of PECVD
    dielectrics for nondispersive metal-insulator-metal capacitors",
    *IEEE Electron Device Letters* **23**(4), 191–193 (2002).
    <https://doi.org/10.1109/55.992835>
[^ng-2003]: C. H. Ng, K. W. Chew and S. F. Chu, "Characterization and
    comparison of PECVD silicon nitride and silicon oxynitride
    dielectric for MIM capacitors", *IEEE Electron Device Letters*
    **24**(8), 506–508 (2003). <https://doi.org/10.1109/LED.2003.815154>
[^ng-2005]: C. H. Ng, C.-S. Ho, S.-F. S. Chu and S.-C. Sun, "MIM
    Capacitor Integration for Mixed-Signal/RF Applications", *IEEE
    Transactions on Electron Devices* **52**(7), 1399–1409 (2005).
    <https://doi.org/10.1109/TED.2005.850642>
[^armacost-2000]: M. Armacost, A. Augustin, P. Felsner, Y. Feng,
    G. Friese, J. Heidenreich, G. Hueckel, O. Prigge and K. Stein, "A
    high reliability metal insulator metal capacitor for 0.18 μm copper
    technology", *IEDM 2000 Technical Digest*, pp. 157–160.
    <https://doi.org/10.1109/IEDM.2000.904282>
[^mahnkopf-1999]: R. Mahnkopf, K.-H. Allers, M. Armacost, A. Augustin
    et al., "'System on a chip' technology platform for 0.18 μm
    digital, mixed signal and eDRAM applications", *IEDM 1999
    Technical Digest*, pp. 849–852.
    <https://doi.org/10.1109/IEDM.1999.824282>
[^denisse-1986]: C. M. M. Denisse, K. Z. Troost, J. B. Oude Elferink,
    F. H. P. M. Habraken, W. F. van der Weg and M. Hendriks,
    "Plasma-enhanced growth and composition of silicon oxynitride
    films", *Journal of Applied Physics* **60**(7), 2536–2542 (1986).
    <https://doi.org/10.1063/1.337117>
[^bose-2002]: M. Bose, D. N. Bose and D. K. Basa, "Plasma enhanced
    growth, composition and refractive index of silicon oxynitride
    films", *Materials Letters* **52**(6), 417–422 (2002).
    <https://doi.org/10.1016/S0167-577X(01)00436-0>
[^blonkowski-2007]: S. Blonkowski, "Nonlinear capacitance variations in
    amorphous oxide metal-insulator-metal structures", *Applied Physics
    Letters* **91**(17), 172903 (2007). <https://doi.org/10.1063/1.2800291>
[^gonon-2007]: P. Gonon and C. Vallée, "Modeling of nonlinearities in
    the capacitance-voltage characteristics of high-k
    metal-insulator-metal capacitors", *Applied Physics Letters*
    **90**(14), 142906 (2007). <https://doi.org/10.1063/1.2719618>
[^pat-mim-newportfab]: A. Kar-Roy and M. Racanelli (Newport Fab, LLC),
    *Method for fabrication of an MIM capacitor and related structure*,
    US 6,430,028 B1, filed 2000-11-22, granted 2002-08-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6430028>
[^pat-mim-ibm]: T. J. Brabazon, B. El-Kareh, S. R. Martin, M. J. Rutten
    and C. W. Kaanta (International Business Machines), *Precision
    analog metal-metal capacitor*, US 5,708,559 A, filed 1995-10-27,
    granted 1998-01-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5708559>
[^pat-mim-philips]: M. C. Olewine and K. F. Saiz (Koninklijke Philips
    Electronics), *Metal-insulator-metal (MIM) capacitor structure and
    methods of fabricating same*, US 6,717,193 B2, filed 2001-10-09,
    granted 2004-04-06.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6717193>
[^pat-mim-freescale]: D. R. Roberts and G. L. Huffman (Freescale
    Semiconductor), *MIM capacitor in a semiconductor device and method
    therefor*, US 7,375,002 B2, filed 2005-06-28, granted 2008-05-20.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7375002>
[^chapple-sokol-1989]: J. D. Chapple-Sokol, E. Tierney and J. Batey,
    "RF Power Dependence of the Material Properties of PECVD Silicon
    Dioxide", *MRS Proceedings* **165** (1989).
    <https://doi.org/10.1557/PROC-165-113>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles
    of Plasma Discharges and Materials Processing*, 2nd ed., Wiley,
    2005, ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
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
