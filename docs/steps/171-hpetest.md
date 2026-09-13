(step-171)=
# Step 171 — HPETEST: Electrical test

| | |
|---|---|
| **Step number** | 171 of 171[^steps-sheet] |
| **Step code** | `HPETEST` |
| **Category** | {ref}`Electrical test / metrology <category-test>` |
| **Phase** | BEOL — passivation, pads, alloy, test |
| **Previous step** | {ref}`ALLY <step-170>` |
| **Next step** | — |

## What this step is

`HPETEST` is the end of the flow: the finished, annealed wafers
({ref}`ALLY <step-170>`) are placed on a prober, needles are lowered
onto the pads opened at {ref}`PDME <step-169>`, and a parametric tester
measures test structures — transistors, resistors, capacitors, diodes,
contact and via chains — to decide whether each wafer was built to
specification. This is the {term}`e-test` or wafer acceptance test
({term}`WAT`) described on the category page; product functional test
({term}`wafer sort`) is a separate, later operation. The step list used
in this reference does not describe the test; what follows rests on the
PDK, SkyWater's capability list and industry practice.

**What the PDK says is tested.** The SKY130 device documentation
publishes the e-test specifications directly. For each MOSFET it states
that "Major model output parameters are shown below and compared against
the EDR (e-test) specs": for the 1.8 V NMOS `nfet_01v8`, for example,
the threshold voltage of a 7/8 µm device (`VTXNL`) has an EDR nominal of
0.541 V with limits 0.515–0.567 V, and the drain current of a
7/0.15 µm device (`IDSNS15`) a nominal 3.510 mA with limits
3.039–3.981 mA.[^pdk-07] Tables with nominal, lower and upper spec limits
(NOM, LSL, USL) follow for the passive devices — N+ diffusion
{term}`sheet resistance` `RSN` 120 Ω/sq (108–132), local-interconnect sheet resistance
`RSLI` 12.8 Ω/sq (9.2–17.0), metal-3 sheet resistance `RSM3` 0.047 Ω/sq
(0.038–0.056), electrical line widths such as `WN` 0.157 µm for a drawn
0.14 µm N+ line, and the {term}`MiM capacitor`'s `CMIMA` 2 fF/µm² (1.8–2.2); the
page says of the NPN transistors "E-test specs for the NPN devices are
shown in the table below", of the precision poly resistors that "several
fixed-value resistors are measured at e-test", and of the SONOS memory
that "E-test parameters are summarized below"; the SRAM cell "is
monitored at e-test through the use of 'pinned out' devices within the
specific arrays".[^pdk-07]

**Where the structures are.** The layer table defines `areaid.mt`
(81:10), "Location of e-test modules within the frame", and `areaid.et`
(81:101), "e-test module identifier";[^pdk-06] the periphery rules state
that the "Die must not overlap areaid.mt" and that drawn compatible, mask
and waffle-drop layers are allowed "only inside areaid:mt (i.e., etest
modules)", inside the seal ring or in the frame, and they allow larger
via sizes inside `areaid.mt` (for example 0.200 µm and 0.800 µm via3
squares, via3.1a).[^pdk-periph] The e-test modules are therefore placed
in the frame outside the product dice (our reading of the rules), the
{term}`scribe line` arrangement a TSMC patent describes as "a plurality
of testlines in the scribe line area between adjacent wafer
dies".[^pat-testline-tsmc]

**A published test tile.** A separate structure set is public. Google's
raw-data repository for the PDK states that "each of the Google MPW runs
includes two copies of a 'manufacturing test tile'", created by
SkyWater,[^raw-data-readme] which "consists of a grid of probe points";
its README is titled "Proprietary Manufacturing Test Tile" and states
that "The schematics and layout of the circuits connected to these
probe points are **not** currently available".[^raw-data-testtile-prop] Its pad documentation, released in
the same repository under Apache 2.0, lists 273 numbered test modules
in four "Die Row" groups, each wired to a line of up to twelve pads
(`Pin 01`–`Pin 12`), and the photographed tile also carries a
"Lithographic Calibration Region" and "Alignment
Marks".[^raw-data-testtile-pads][^raw-data-testtile-prop] The repository
does not say where on the reticle the two copies sit, nor whether its
modules are the e-test modules that `areaid.mt` marks in the frame, so
this page does not treat the tile as SkyWater's production e-test set.
The repository also documents an open replacement tile by Google, NIST
and the University of Michigan, whose "first test version … was
included in the MPW-5 run"; it was built with the OpenFASoC and
gdsfactory generators, and its die image lists "Over 1400
Pads".[^raw-data-testtile-open]

## Step category

`HPETEST` is the only step of the
{ref}`Electrical test / metrology <category-test>` category in the flow,
and the category page's account of the process control monitor
({term}`PCM`), van der Pauw and {term}`Kelvin structures <Kelvin structure>` and transistor
parameter extraction applies to it directly. What is specific to SKY130
is that the specifications are public: the PDK's device page gives, for
dozens of devices, the e-test parameter names, test-structure
geometries, nominal values and limits, and places them beside the SPICE
model corners (TT, FF, SS, FS, SF) they are compared with.[^pdk-07] The
wafer leaves the step physically unchanged apart from probe marks on the
test pads.

## Why this step exists

* **Disposition.** The wafer is accepted, held or scrapped on its e-test
  results against the limits; the PDK's LSL/USL columns[^pdk-07] are
  that kind of limit. Parametric test is performed at "a few locations
  on each wafer" to verify that fabrication succeeded.[^wiki-test]
* **Process control.** Each parameter is a sensor for particular steps:
  well and diffusion sheet resistances for the implants and anneals,
  electrical line widths for lithography and etch
  (Buehler, Grant and Thurber's bridge and van der Pauw
  structures[^buehler-1978][^vdp-1958]), contact and via resistance for the
  plug modules (Proctor, Linholm and Mazer[^proctor-1983]), threshold
  voltage for the gate stack and channel implants (extraction methods
  reviewed by Ortiz-Conde et al.[^ortiz-conde-2002]), and comb/serpentine
  structures for shorts and opens (Sayah and Buehler[^sayah-1988]). The
  results feed {term}`SPC` charts and correlation with tool history.
* **The PDK's models.** Compact models are fitted to and checked against
  parametric data (Cheng and Hu describe the BSIM3 extraction[^cheng-1999]);
  the PDK's model-versus-EDR tables are the public face of that
  loop.[^pdk-07]
* **Yield learning.** Test structures also measure defect densities and
  critical-area sensitivities (Stapper;[^stapper-1983] Hess and
  Weiland[^hess-1999]) and support design for manufacturability
  (Maly[^maly-1990]).
* **Checking the passivation, anneal and pads.** This is the first
  electrical measurement after {ref}`ALLY <step-170>`, whose interface-trap
  passivation the transistor parameters reflect, and the first probing of
  the openings made at {ref}`PDME <step-169>`; Hunter et al. show that
  probing can crack the oxide under aluminium pads.[^hunter-2012]

## How it is typically performed

An industry-generic wafer acceptance test for a 200 mm, 130 nm-era CMOS
fab (SKY130's test plan is not public beyond the parameters above):

1. **Tester and prober.** A parametric tester — source-measure units, a
   capacitance meter and a switching matrix under test-plan software,
   such as the HP/Agilent 4062UX[^brltest-4062] or Keithley S600, designed
   for "process control, process and equipment tuning and optimization,
   equipment qualification, Wafer Acceptance Testing, and device modeling
   and characterization"[^keithley-s600] — coupled to an automatic wafer
   prober with a temperature-controlled chuck.[^wiki-ate]
2. **{term}`Probe card <probe card>`.** A card laid out to the pad pitch of the e-test modules
   (Wikipedia classifies probe cards as needle, vertical and MEMS
   types[^wiki-probecard]); the pads are the
   `pad` openings of {ref}`PDM <step-168>`.
3. **Sites.** A fixed set of modules at "a few locations on each
   wafer"[^wiki-test], with the full parameter list at each.
4. **Measurements.** Four-terminal ({term}`four-point probe`)
   resistance measurements ("a constant
   current is applied to two probes, and the potential on the other two
   probes is measured"[^wiki-rs]) for sheet and contact resistance;
   transistor sweeps for threshold voltage, saturation and leakage
   currents; C–V for capacitors and oxide thickness; breakdown voltages
   for junctions and dielectrics; gain for bipolar devices. Schroder's
   text covers the methods.[^schroder-2006]
5. **Data.** Results are stored per wafer, site and structure, compared
   with limits and control limits, and released to disposition and SPC.

The test tile's pad list is a public example of such a structure set
with its connections written out. Resistors and lines are wired for
four-terminal measurement ("Force 1", "Force 2", "Sense 1", "Sense 2"
on "M1 sheet resistance and electrical linewidth"); there are van der
Pauw squares ("10x10 Van der P."), Kelvin contacts, contact strings
("contact string (6384 contacts; 0.88 sq/ct RSN)"), via chains ("s8p
via3 (0.2x0.2) contact chain (16500 contacts)"), serpentine/comb pairs,
MOS, finger and MiM capacitors, and transistors at several widths,
lengths and source/drain extents (`sa`, `sb`).[^raw-data-testtile-pads]
The data measured on the tile "was collected under contract by CoolCAD
Electronics LLC using the manufacturing test tile created by SkyWater"
to help validate the PDK,[^raw-data-readme] and are stored as IC-CAP
`.mdm` files whose headers give each terminal a "Source measurement
unit number on the curve tracer", a "Compliance" and a
sweep.[^raw-data-mdm] The repository does not describe SkyWater's own
production test or name its tester.

The transistor files can be set beside the PDK's e-test nominals,
although the PDK states neither the bias conditions nor the extraction
methods behind them. For the 5 V NMOS, whose nominal VTXNLH at W/L 7/8
is 0.811 V,[^pdk-07] two 7/8 µm test-tile devices give 0.79 V and
0.82 V by maximum-transconductance extrapolation of the drain current at
V_DS = 0.1 V, less half that drain bias. For the 16 V {term}`drain-extended <DEMOS>` NMOS at 20 µm
width, the median resistance at V_GS = 5 V and V_DS = 0.1 V (from the
I_D–V_D sweeps) is 469 Ω
for ten 0.925 µm ("L=0.7") structures and 695 Ω for eight 2.425 µm
("L=2.2") structures, against RDS nominals of 458.5 Ω and 703.8 Ω at
W/L 20/0.7 and 20/2.2 (our extraction from the published
measurements).[^raw-data-hv-mosfets][^pdk-07] The PDK lists 24 e-test
threshold parameters for the 5 V, 16 V and 20 V NMOS and PMOS and the
native, zero-Vt and ESD NMOS. Of the 23 for which the tile has a matching structure
(none matches the 20 V native NMOS, VTXN20VHV1L, at 2 × 30/1.0 µm), 22
have every working test-tile structure inside the published
minimum–maximum limits. The exception, VTXPN42H, is a single
0.42/20 µm PMOS whose linear-region sweep (at most 0.23 µA at
V_DS = −0.1 V) rises irregularly, so that its extrapolated threshold
depends on how the transconductance is smoothed (magnitudes of
0.86–1.55 V against limits of 0.87–1.00 V); one 0.42/0.5 µm NMOS
structure carries no current at all (our extraction from the published
measurements).[^raw-data-hv-mosfets][^pdk-07] The files record the sweeps,
compliance and instrument channels but no temperature, measurement
date, wafer or die, and the drain is swept to at most 5 V (10 V on the
symmetric 16 V structures), so they do not bear on breakdown or the
10.5–20 V ratings.[^raw-data-hv-mosfets]

The files for the five 1.8 V transistor types include, in one module
per type, the geometries of the PDK's e-test thresholds and currents
(7/8, 7/0.15, 0.42/8 or 0.42/1 and 0.42/0.15 µm; 7/0.35 and 0.42/0.35 µm
in place of the short devices for the low-Vt PMOS), all except the
0.42/1 µm `nfet_01v8`.[^raw-data-lv-mosfets][^raw-data-testtile-pads][^pdk-07]
By the same extrapolation at |V_DS| = 0.1 V, less half the drain bias,
the 7/8 µm `nfet_01v8` gives 0.534 V against the VTXNL nominal of
0.541 V and the 7/0.15 µm device 0.707 V against the VTXNS15 nominal
of 0.700 V. Of the 19 e-test thresholds matched in these modules, 16 of
the 18 with a usable printed nominal lie within 0.03 V of it (two of
them at 0.029 V, so the count depends on how the transconductance is
differentiated); the
exceptions are two low-Vt PMOS values, 0.668 V against 0.630 V at
0.42/8 µm and 0.636 V against 0.533 V at 7/0.35 µm; that 7/0.35 µm
sweep rises irregularly, and a second 7/0.35 µm structure in another
module, with a smooth sweep, gives 0.536 V. All 18 with usable
printed limits lie inside them (our extraction from the published
measurements).[^raw-data-lv-mosfets][^pdk-07] Two entries of the
PDK's `pfet_01v8_lvt` table cannot be used as printed: the VTCPSN35L
nominal reads −8.505 V, beside model and limit values between −0.316 V
and −0.693 V, and the VTCPN42L limits read −1.042 V to −0.845 V, which
exclude that parameter's own nominal of −0.630 V.[^pdk-07] Taking the
drain current at |V_GS| = |V_DS| = 1.8 V (the PDK does not state the
bias), four of the five e-test currents lie inside their limits and
within 7 % of nominal: 3.40 mA for the 7/0.15 µm `nfet_01v8` (IDSNS15
3.510 mA), 1.28 mA and 0.94 mA for the 7/0.15 µm `pfet_01v8` and
`pfet_01v8_hvt` (1.347 mA and 1.003 mA) and 1.24 mA for the 7/0.35 µm
`pfet_01v8_lvt` (1.22 mA), from the same irregular sweep; the smooth
7/0.35 µm structure in module 8426 with a 2.5 µm source/drain extent
carries 1.11 mA, also inside the limits. The fifth, the 7/0.15 µm `nfet_01v8_lvt` of
that module, carries 3.30 mA, below the 3.527 mA lower limit of
IDSNS15L, while twelve 7/0.15 µm low-Vt NMOS structures in two other
modules carry 3.67–4.13 mA, inside it (our extraction from the
published measurements).[^raw-data-lv-mosfets][^pdk-07] The tile's
"fet mismatch" modules are not used for these comparisons: their
thresholds agree with the other modules to within about 0.05 V, but their drain currents per
drawn width are about two to four times as high, and neither the files
nor the pad list explain the
difference.[^raw-data-lv-mosfets][^raw-data-testtile-pads]

## Machines typically used

* **Parametric tester**: HP/Agilent 4062UX,[^brltest-4062]
  Keithley S600[^keithley-s600] ({ref}`category-test`).
* **Automatic wafer prober** with a hot/cold chuck (Electroglas, TEL,
  Tokyo Seimitsu[^wiki-ate]).
* **Probe cards** and probe-tip cleaning media.[^wiki-probecard]
* **Bench parameter analysers and manual probe stations** for
  engineering analysis.

## Machines likely used at SkyWater

* **HP 4062UX.** SkyWater lists "HP 4062UX" as its parametric
  tester, with "DC, capacitance, pulse generator, frequency counter" and
  "automatic data upload, SPC, analysis, disposition".[^skw-01] Strength: **strong** — it is the only parametric
  tester named, and a dealer listing describes the 4062UX as a
  Keysight/Agilent parametric test system.[^brltest-4062] That `HPETEST`
  runs on it is an **inference**.
* **Sort and reliability equipment** — "Advantest T5365P", "Verigy V3308,
  V4108", "Credence Duo", "Credence LT", "Fuse GSI M325", "Verigy 93000",
  "Camtek Falcon (outgoing QA)"; "Qualitau" in the reliability
  lab.[^skw-01] Strength: strong for existence; these serve
  functional sort and reliability rather than e-test (inference).
* **Probers.** No production wafer prober is named; SkyWater lists an
  "Engineering manual Probe Station" under parametric test and a "Summit
  200 Prober/Tester" and "PMC200 Cryo Probe" in its reliability
  lab.[^skw-01]

## Resources required

* **Probe cards** laid out for the e-test modules, and replacement
  needles; **probe-tip cleaning media**.[^wiki-probecard]
* **Calibration standards** for source-measure units and capacitance
  meters; **reference wafers** for tester correlation.
* **Test-plan software and a data system** holding the specifications
  (the PDK's EDR parameters[^pdk-07]).
* No process gases or chemicals.

## Related steps and cross-references

* Previous: {ref}`ALLY <step-170>` (the anneal whose effect the transistor
  parameters include). This is the last step of the flow.
* The pads probed: {ref}`PDM <step-168>`, {ref}`PDME <step-169>`.
* Examples of steps whose results are measured here: the MiM capacitor
  ({ref}`CAPILD <step-135>`, `CMIMA`), metal 3 ({ref}`MM3E <step-140>`,
  `RSM3`), the local interconnect ({ref}`LI1ME <step-103>`, `RSLI`).
* The first step of the flow: {ref}`SMAT <step-001>`.
* Category page: {ref}`Electrical test / metrology <category-test>`.

## References

### Cross-check

* SkyWater PDK, *Device Details* — "compared against the EDR (e-test)
  specs"; `VTXNL`, `IDSNS15`, `RSN`, `RSLI`, `RSM3`, `WN`, `CMIMA` with
  limits; NPN, poly-resistor, SONOS and SRAM e-test statements.[^pdk-07]
* SkyWater PDK, *Layers Reference* — `areaid.mt` "Location of e-test
  modules within the frame"; `areaid.et`.[^pdk-06]
* SkyWater PDK, *Periphery rules* — "Die must not overlap areaid.mt";
  layers allowed "only inside areaid:mt (i.e., etest modules)";
  via3.1a.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — "HP 4062UX"; sort testers;
  "Qualitau".[^skw-01]
* BRL Test, 4062UX listing; Keithley, *Series S600* data
  sheet.[^brltest-4062][^keithley-s600]
* ITRS 2001, *Test and Test Equipment* and *Metrology*.[^itrs-2001-test][^itrs-2001-met]
* Google's SKY130 raw-data repository — the README (data "collected
  under contract by CoolCAD Electronics LLC using the manufacturing test
  tile created by SkyWater"), the proprietary test-tile README ("two
  copies" per MPW run), the 273-module pad documentation, the open
  MPW-5 test tile and the MDM file
  format.[^raw-data-readme][^raw-data-testtile-prop][^raw-data-testtile-pads][^raw-data-testtile-open][^raw-data-mdm]
* The same repository's measured files for the 5 V, 16 V and 20 V
  transistors and the native, zero-Vt and ESD NMOS — the thresholds, resistances and currents
  compared here with the e-test nominals are our
  extraction.[^raw-data-hv-mosfets]
* The same repository's files for the five 1.8 V transistor types — the
  thresholds and drain currents set here beside the e-test nominals are
  our extraction.[^raw-data-lv-mosfets]

### High-level understanding

* Wikipedia, *Wafer testing*, *Sheet resistance*, *Van der Pauw method*,
  *Probe card*, *Automatic test equipment*, *Statistical process
  control*.[^wiki-test][^wiki-rs][^wiki-vdp][^wiki-probecard][^wiki-ate][^wiki-spc]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — process
  monitoring and wafer test.[^txt-07]

### Deep dive

* van der Pauw, *Philips Res. Rep.* 1958 — the four-contact
  sheet-resistance theorem.[^vdp-1958]
* Buehler, *Microelectronic Test Patterns*, NBS Special Publication
  400-6, 1974 — an early NBS publication on test patterns.[^buehler-1974]
* Buehler, Grant and Thurber (NBS), *J. Electrochem. Soc.* 1978 — bridge
  and van der Pauw resistors for electrical line width.[^buehler-1978]
* Proctor, Linholm and Mazer (NBS), *IEEE TED* 1983 — Kelvin contact
  resistance structures.[^proctor-1983]
* Sayah and Buehler, ICMTS 1988 — a comb/serpentine/cross-bridge
  structure for process evaluation.[^sayah-1988]
* Ortiz-Conde et al., *Microelectron. Reliab.* 2002 — threshold-voltage
  extraction methods.[^ortiz-conde-2002]
* Cheng and Hu, *MOSFET Modeling & BSIM3 User's Guide* — from parametric
  data to model parameters.[^cheng-1999]
* Stapper (IBM), *IBM J. Res. Dev.* 1983, and Hess and Weiland, *IEEE
  TSM* 1999 — defect sensitivities and defect-density extraction from
  test structures.[^stapper-1983][^hess-1999]
* Maly, *Proc. IEEE* 1990 — design for manufacturability.[^maly-1990]
* Chen, Hsu, Tsai and Jeng (TSMC), US 7,679,384 — parametric testlines
  in the scribe line.[^pat-testline-tsmc]
* Hunter et al., IMAPS 2012 — probe damage in aluminium pads.[^hunter-2012]
* Schroder, *Semiconductor Material and Device Characterization* — the
  measurement methods.[^schroder-2006]

## Open questions

* The test plan — which structures, how many sites per wafer, the
  sampling across a lot and the disposition rules — is not public beyond
  the PDK's parameter tables.[^pdk-07]
* What "EDR" stands for in the PDK's "EDR (e-test)" columns is not
  explained on the page.
* Whether `HPETEST` runs on the HP 4062UX SkyWater lists[^skw-01] is not
  stated; the prober and probe-card types are not public.
* How the e-test modules are distributed in the frame (positions,
  number per reticle field) is not public. The raw-data repository says
  that two copies of its manufacturing test tile are on each Google MPW
  run but not where,[^raw-data-testtile-prop] and its pad list carries
  the note "PLACE IN CENTER, CORNER OF RETICLE" under one
  module;[^raw-data-testtile-pads] neither says how the tile relates to
  the `areaid.mt` modules.
* The pad list's `Group` codes (1–8, 10, `Z`, `s8tet`; blank for most
  modules) are not explained, and the schematics and layout of the tile's structures are
  not public.[^raw-data-testtile-pads][^raw-data-testtile-prop]
* The published transistor I–V data have limited current resolution: an analysis
  notebook in the repository notes that "the data gets noisy below 2nA"
  and that the data "cannot be used to predict the subthreshold slope
  (digital leakage)".[^raw-data-notebooks] The resolution of the fab's
  own e-test is not public.
* The PDK's e-test drain currents for the 5 V transistors, IDSNS50H
  12.1 mA and IDSPS50H 6.83 mA, are listed at W/L 7/0.50 without a
  bias;[^pdk-07] 7/0.5 µm test-tile devices carry 4.43 mA and 2.44 mA at
  |V_GS| = |V_DS| = 5 V, and 20/0.5 µm devices 11.6 mA and 6.71 mA (our
  extraction from the published measurements).[^raw-data-hv-mosfets]
  Whether the published values refer to another bias or another width
  is not stated.
* How the e-test thresholds are defined is not published. On the
  test-tile data for the 1.8 V transistors, maximum-transconductance
  extrapolation comes within about 0.03 V of most nominals, whereas a
  constant-current criterion of 100 nA × W/L gives thresholds
  0.05–0.08 V lower for the NMOS types, 0.02–0.11 V lower for the
  standard and high-Vt PMOS (the largest at 0.42/8 µm, where the
  criterion current is near the data's noise floor) and 0.22–0.33 V lower for the low-Vt PMOS
  (0.14 V for the smooth 7/0.35 µm structure of module 8426; our
  extraction from the published
  measurements).[^raw-data-lv-mosfets][^pdk-07] The PDK's parameter
  names mix `VTX…` and, for the low-Vt PMOS, `VTC…` without explaining
  either.[^pdk-07]

<!-- footnotes -->

[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (device e-test and
    model parameter tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^brltest-4062]: BRL Test, *4062UX — Keysight / Agilent Parametric
    Testers* (listing).
    <https://www.brltest.com/index.php?main_page=product_info&products_id=7874>
[^keithley-s600]: Keithley Instruments, *Series S600 Parametric Test
    Systems*, data sheet.
    <https://download.tek.com/datasheet/SeriesS600_DataSht.pdf>
[^itrs-2001-test]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Test and Test Equipment*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Test.pdf>
[^itrs-2001-met]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Metrology*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
[^wiki-test]: Wikipedia, *Wafer testing*.
    <https://en.wikipedia.org/wiki/Wafer_testing>
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^wiki-vdp]: Wikipedia, *Van der Pauw method*.
    <https://en.wikipedia.org/wiki/Van_der_Pauw_method>
[^wiki-probecard]: Wikipedia, *Probe card*.
    <https://en.wikipedia.org/wiki/Probe_card>
[^wiki-ate]: Wikipedia, *Automatic test equipment*.
    <https://en.wikipedia.org/wiki/Automatic_test_equipment>
[^wiki-spc]: Wikipedia, *Statistical process control*.
    <https://en.wikipedia.org/wiki/Statistical_process_control>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^vdp-1958]: L. J. van der Pauw, "A method of measuring specific
    resistivity and Hall effect of discs of arbitrary shape", *Philips
    Research Reports* **13**, 1–9 (1958); reprinted in S. M. Sze (ed.),
    *Semiconductor Devices: Pioneering Papers*, World Scientific, 1991,
    pp. 174–182. <https://doi.org/10.1142/9789814503464_0017>
[^buehler-1974]: M. G. Buehler, *Microelectronic Test Patterns*, NBS
    Special Publication 400-6, National Bureau of Standards, 1974.
    <https://doi.org/10.6028/NBS.SP.400-6>
[^buehler-1978]: M. G. Buehler, S. D. Grant and W. R. Thurber, "Bridge
    and van der Pauw Sheet Resistors for Characterizing the Line Width
    of Conducting Layers", *Journal of The Electrochemical Society*
    **125**(4), 650–654 (1978). <https://doi.org/10.1149/1.2131517>
[^proctor-1983]: S. J. Proctor, L. W. Linholm and J. A. Mazer, "Direct
    measurements of interfacial contact resistance, end contact
    resistance, and interfacial contact layer uniformity", *IEEE
    Transactions on Electron Devices* **30**(11), 1535–1542 (1983).
    <https://doi.org/10.1109/T-ED.1983.21334>
[^sayah-1988]: H. R. Sayah and M. G. Buehler, "Comb/serpentine/cross-bridge
    test structure for fabrication process evaluation", *Proc. 1988 IEEE
    International Conference on Microelectronic Test Structures
    (ICMTS)*, pp. 23–28. <https://doi.org/10.1109/ICMTS.1988.672923>
[^ortiz-conde-2002]: A. Ortiz-Conde, F. J. García Sánchez, J. J. Liou,
    A. Cerdeira, M. Estrada and Y. Yue, "A review of recent MOSFET
    threshold voltage extraction methods", *Microelectronics
    Reliability* **42**(4–5), 583–596 (2002).
    <https://doi.org/10.1016/S0026-2714(02)00027-6>
[^cheng-1999]: Y. Cheng and C. Hu, *MOSFET Modeling & BSIM3 User's
    Guide*, Kluwer Academic, 1999. <https://doi.org/10.1007/b117400>
[^stapper-1983]: C. H. Stapper, "Modeling of Integrated Circuit Defect
    Sensitivities", *IBM Journal of Research and Development* **27**(6),
    549–557 (1983). <https://doi.org/10.1147/rd.276.0549>
[^hess-1999]: C. Hess and L. H. Weiland, "Extraction of wafer-level
    defect density distributions to improve yield prediction", *IEEE
    Transactions on Semiconductor Manufacturing* **12**(2), 175–183
    (1999). <https://doi.org/10.1109/66.762875>
[^maly-1990]: W. Maly, "Computer-aided design for VLSI circuit
    manufacturability", *Proceedings of the IEEE* **78**(2), 356–392
    (1990). <https://doi.org/10.1109/5.52217>
[^schroder-2006]: D. K. Schroder, *Semiconductor Material and Device
    Characterization*, 3rd ed., Wiley, 2006.
    <https://doi.org/10.1002/0471749095>
[^pat-testline-tsmc]: H.-W. Chen, S.-H. Hsu, H.-Y. Tsai and S.-P. Jeng
    (Taiwan Semiconductor Manufacturing Co.), *Parametric testline with
    increased test pattern areas*, US 7,679,384 B2, filed 2007-06-08,
    granted 2010-03-16.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7679384>
[^hunter-2012]: S. Hunter, J. L. Clark, D. Hornberger and L. Rubio, "Use
    of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
    *International Symposium on Microelectronics* **2012**(1), 384–395
    (IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^raw-data-readme]: SkyWater PDK Authors, *sky130-raw-data - Raw data
    collected about the SKY130 process technology*, `README.rst`,
    `google/skywater-pdk-sky130-raw-data` repository, 2022, retrieved
    2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/README.rst>
[^raw-data-testtile-prop]: SkyWater PDK Authors, *SkyWater 130nm
    Proprietary Manufacturing Test Tile*,
    `docs/sky130-testtile-proprietary/README.rst` and pad-layout image,
    `google/skywater-pdk-sky130-raw-data` repository, 2022, retrieved
    2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/README.rst>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^raw-data-testtile-open]: SkyWater PDK Authors, *SkyWater 130nm Open
    Manufacturing Test Tile*, `docs/sky130-testtile-open/README.rst` and
    images, `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-open/README.rst>
[^raw-data-mdm]: Agilent Technologies, *IC-CAP User's Guide*, "MDM File
    Structure" (IC-CAP 2008 documentation), retrieved 2026-09-13,
    <https://people.ece.ubc.ca/robertor/Links_files/Files/ICCAP-2008-doc/icug/icug136.html>;
    and SkyWater PDK Authors, `docs/_static/mdm-format.png`,
    `google/skywater-pdk-sky130-raw-data` repository.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/_static/mdm-format.png>
[^raw-data-notebooks]: Google LLC, *SKY130 plots of {IC,IB,IG}/VG*, and
    B. Murmann, *SKY130 plots of ID-VG derivatives* (August 2022),
    Colab notebooks in the `google/skywater-pdk-sky130-raw-data`
    repository, retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/notebooks>
[^raw-data-hv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 5 V, 10/16 V and
    20 V transistors, the native, zero-Vt and ESD NMOS and the thick-oxide
    gate capacitors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_g5v0d10v5`, `pfet_g5v0d10v5`, `nfet_g5v0d16v0`,
    `pfet_g5v0d16v0`, `nfet_g5v0d20v0`, `pfet_g5v0d20v0`,
    `nfet_03v3_nvt`, `nfet_05v0_nvt`, `nfet_20v0_nvt`, `esd_nfet_01v8`,
    `esd_nfet_g5v0d10v5`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
[^raw-data-lv-mosfets]: SkyWater PDK Authors (measurements by CoolCAD
    Electronics LLC), measured I–V and C–V data for the 1.8 V
    transistors, IC-CAP `.mdm` files in `sky130_fd_pr/cells/`
    (`nfet_01v8`, `nfet_01v8_lvt`, `pfet_01v8`, `pfet_01v8_hvt`,
    `pfet_01v8_lvt`), `google/skywater-pdk-sky130-raw-data`
    repository, 2022, retrieved 2026-09-13; values quoted from them are
    our extraction.
    <https://github.com/google/skywater-pdk-sky130-raw-data/tree/main/sky130_fd_pr/cells>
