(machine-parametric-tester)=
# Parametric tester and prober

At the end of the flow the finished wafer is measured electrically. A
wafer prober loads it, aligns it under a probe card whose needles land on
the pads of test structures in the scribe lines or drop-in sites, and a
parametric tester — source-measure units, a capacitance meter and a
switching matrix under test-plan software — measures transistors,
resistors, capacitors and chains site by site. In a fab of this kind the results decide
whether the wafer is shipped and feed statistical process control
(industry practice). The same kind
of instrument, on a manual probe station, serves engineering work, and
some step pages name electrical monitors earlier in the flow. This page
describes the classes, lists representative 200 mm-era models, and then
says what SkyWater has published about its tools and which SKY130 steps
this reference assigns to them. Test structures, sheet resistance and
transistor parameters are on the {ref}`test category page
<category-test>`.

| | Parametric tester and prober |
|---|---|
| What it does | "wafer parametric tests (WPT) are performed at a few locations on each wafer to ensure the wafer fabrication process has been carried out successfully";[^wiki-test] the prober "aligns the electrical contact points (or pads) on each IC on a wafer with the electrical connections (or probe pins) on a probe card".[^electroglas-1999] |
| Instruments | Source/monitor units, a 48-pin switching matrix, a voltage source/monitor unit and an LCR meter in the HP 4062UX configuration a dealer lists;[^brltest-4062] "active electronics on each tester pin inside a test head that mounts on top of the prober" (Keithley S680).[^keithley-s600] |
| Range and speed | Measurements "from 20 fA" and "4 μV to 200V", with a resistance measurement taking "less than 17 ms" (HP 4062UX);[^brltest-4062] "true parallel testing of up to eight DUTs within a single probe touchdown" (S680).[^keithley-s600] |
| Prober | "a highly advanced 200mm system" with automatic probe-to-pad alignment (Electroglas Horizon 4090);[^electroglas-4090] a mini-environment prober "for ultra clean parametric test environments" (Horizon 4090µ).[^electroglas-4090u] |
| Requirement | ITRS 2001 counts parametric data among the sources that integrated data management "must comprehend" to trace yield problems to their point of occurrence.[^itrs-2001-yield] |
| 200 mm era | The HP 4062 family, including the 4062C and 4062UX;[^brltest-4062] Agilent's 4070 series (4072B and 4073B announced in 2002);[^eepower-4070] Keithley's Series S600;[^keithley-s600] Electroglas Horizon probers;[^electroglas-4090][^electroglas-4085x] TEL P-8 and P-12 probers.[^tel-prober] |
| SkyWater-listed tool | "HP 4062UX" ("DC, capacitance, pulse generator, frequency counter"), "Engineering manual Probe Station"; no production prober[^skw-01] |
| SKY130 steps | 1 step, with an electrical monitor named at 21 more; see {ref}`SKY130 steps assigned to this class <machine-parametric-tester-steps>` |

## What the machine class is and how it works

Parametric test measures structures, not circuits. Linholm, Allen and
Cresswell define microelectronic test structures as "electrical devices
that are used to determine selected tool, process, device, material, or
circuit parameters by means of electrical tests", supported "by a variety
of commercial test equipment often found in semiconductor manufacturing
facilities".[^linholm-1994] The tester, the prober and the probe card are
three machines that work as one; the test plan ties them to the
structures and the limits.

### Test structures and parameters

The structures are small and four-terminal wherever a resistance is
measured. Buehler, Grant and Thurber showed that line width "can be
computed from simple d-c electrical measurements made on bridge and van
der Pauw shaped test structures";[^buehler-1978] Proctor, Linholm and
Mazer described four- and six-terminal structures for contact
resistance;[^proctor-1983] Sayah and Buehler's comb, serpentine and
cross-bridge structure monitors shorts and step coverage and was "tested
using a computer-controlled parametric test system".[^sayah-1988]
Lukaszek, Grambow and Yarbrough built a test chip on "systematic
structural decomposition" so that electrical faults could be diagnosed
unambiguously.[^lukaszek-1990] Transistor thresholds are extracted by one
of several methods,[^ortiz-conde-2002] and the parameters feed compact
models.[^cheng-1999] The {ref}`test category page <category-test>`
describes a typical process control monitor.

### The parametric tester

A parametric tester is a set of precision DC instruments behind a
switching matrix. The HP 4062UX in a dealer's listing combines an HP 4142B
modular DC source/monitor mainframe with source/monitor units, an HP 4085B
48-pin switching matrix and an HP 4284A LCR meter, and describes the
system as
"the high-end system of the HP4062 Semiconductor Parametric Test System
family", for "both process monitoring and process
development".[^brltest-4062] Long cables and relay matrices add leakage and
capacitance: Keithley describes "the parasitic capacitances and leakage
currents inherent in systems with long cables and a reed-relay-based
switch matrix between the DUT and the measurement circuitry", which its
Series S600 minimised with "active electronics on each tester pin inside a
test head that mounts on top of the prober", where "Each probing pin has its own amplifier for
bi-directional scaling of currents".[^keithley-s600] Keithley lists its
uses as "process control, process and equipment tuning and optimization,
equipment qualification, Wafer Acceptance Testing, and device modeling and
characterization", with options including a "Frequency counter for ring
oscillator measurements" and pulse generators for embedded
memory.[^keithley-s600] Agilent's 4072B and 4073B, announced in 2002, embedded "an
integrated, high-speed, capacitance meter" in each test head for "up to 40
percent higher throughput".[^eepower-4070] A frequency counter can read
more than a single oscillator: Bhushan et al. measured threshold-voltage
variation from "a dense array of nominally identical ring oscillators" with
"a standard frequency counter".[^bhushan-2006]

Test plans organise the work. In Keithley's software the tests "to be run
at each site are incorporated into a set of nested loops", with files for
the wafer description, the limits and the probe card, and access points
for "transferring data".[^keithley-s600]

### The prober and the probe card

The prober is the wafer handler of the test cell. Electroglas explained
that a prober aligns the pads of each die with the probe pins of a probe
card, and that "The probe card connects to a test system that performs
the required parametric or functional test".[^electroglas-1999] A prober
is "equipped with automatic pattern recognition optics capable of aligning
the wafer with sufficient accuracy to ensure accurate registration between
the contact pads on the wafer and the tips of the probes".[^wiki-test]
Electroglas's Horizon 4090, described on a 1998 capture, added "automatic
probe-to-pad-alignment (APTPA)" and GEM factory
integration,[^electroglas-4090] and the Horizon 4090µ integrated a mini-environment
and SMIF interface for parametric test.[^electroglas-4090u]
The probe card is "an interface between an electronic test system and a
semiconductor wafer".[^wiki-probecard] Its needles are a source of error
and damage: Broz and Rincon found that "increased and unstable contact
resistance" with tungsten and tungsten–rhenium needles on aluminium pads
at 85 °C comes partly from oxide formed by "localized Joule heating at the
probe tip contact",[^broz-1999] and Hunter et al. found that probe cracks
in the oxide under a pad "may not be visible even in a careful cratering
test".[^hunter-2012]

### Manual, heated and cryogenic probing

Not all parametric work runs on an automatic cell. Manual and
semi-automatic probe stations serve device characterisation: FormFactor's
current Cascade SUMMIT200 is designed "for R&D, device
characterization/modelling or niche production applications" over
"-60°C to 300°C",[^formfactor-summit200] and its PMC200 is "a highly-precise,
advanced manual probe system for wafers and substrates up to 200 mm in a high
vacuum environment, at cryogenic temperatures down to 77 K with liquid
nitrogen or < 7 K with liquid helium".[^formfactor-pmc200]

### From data to disposition

Parametric data are used through statistics. Spanos surveys "standard SPC
(statistical process control) schemes" with semiconductor examples, from
contamination control to "the monitoring of continuous process
parameters".[^spanos-1992] ITRS 2001 asks integrated data management to
merge "parametric data, and electrical test information" with defect data
"to recognize process trends and excursions".[^itrs-2001-yield] In such a flow the
wafer leaves test with a disposition against limits (industry practice),
and the same data feed model extraction.[^cheng-1999]

## Representative 200 mm-era models

* **Hewlett-Packard, then Agilent.** The HP 4062 Semiconductor Parametric
  Test System family, whose 4062UX "uses the same measurement hardware as
  the HP 4062C" with an HP-UX software environment;[^brltest-4062] and the
  4070 series, extended in 2002 by the 4072B and 4073B.[^eepower-4070]
* **Keithley.** The Series S600 parametric testers, with the S680 as the
  latest configuration on the data sheet.[^keithley-s600]
* **Electroglas.** The Horizon 4090 and 4085X automatic probers for 200 mm
  wafers (1998 captures), the latter for "probing high-pin-count
  devices", and the Horizon 4090µ.[^electroglas-4090][^electroglas-4085x][^electroglas-4090u]
* **Tokyo Electron.** The P-8 and P-12 series probers, refurbished today as
  the P-8XL for wafers from 100 mm to 200 mm.[^tel-prober]
* **Cascade Microtech, now FormFactor.** The SUMMIT200 and PMC200 probe
  systems for characterisation and cryogenic
  work.[^formfactor-summit200][^formfactor-pmc200]

## At SkyWater

### What SkyWater lists

Under "Wafer Sort/Test", SkyWater's *Facilities & Capabilities* page
lists:[^skw-01]

> "Parametric Test": "HP 4062UX" ("DC, capacitance, pulse generator,
> frequency counter"; "automatic data upload, SPC, analysis,
> disposition"), "Engineering manual Probe Station"
>
> "Sort": "Advantest T5365P", "Verigy V3308, V4108", "Credence Duo",
> "Credence LT", "Fuse GSI M325", "Verigy 93000", "Camtek Falcon (outgoing
> QA)"
>
> "REL Lab": "Qualitau", "Summit 200 Prober/Tester", "PMC200 Cryo Probe"

and, among its services, "eTest measurement development" and "Cryogenic
probing down to 8-Kelvin".[^skw-01] Read term by term, on our reading:
"HP 4062UX" is the high-end system of HP's 4062 parametric test family
described in the dealer listing,[^brltest-4062] and its sub-entries name a
DC, capacitance, pulse and frequency capability and a data path to SPC and
disposition; "Summit 200 Prober/Tester" and "PMC200 Cryo Probe" match the
names of FormFactor's Cascade SUMMIT200 and PMC200 probe
systems,[^formfactor-summit200][^formfactor-pmc200] which SkyWater does not
spell out. The sort testers are functional testers for product sort, a
different step from parametric test (our reading).[^wiki-test] No
production wafer prober is named for the parametric tester.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listings are **strong**: they are SkyWater statements.[^skw-01] The
caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. The
{ref}`HPETEST <step-171>` page grades the 4062UX strong as "the only
parametric tester named" and its use for `HPETEST` an inference; the
prober behind it, and whether the reliability-lab probers or the manual
station take part in e-test, are not public.

(machine-parametric-tester-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names the parametric tester
and prober, and, after *electrical monitor named:*, steps whose section
names a C–V, charge-pumping, chain or other electrical test (identical to
the {ref}`machines index <machines-index>` table):

{ref}`HPETEST <step-171>`; *electrical monitor named:* {ref}`040 <step-040>`, {ref}`043 <step-043>`, {ref}`047 <step-047>`, {ref}`063 <step-063>`, {ref}`096 <step-096>`, {ref}`098 <step-098>`, {ref}`108 <step-108>`, {ref}`114 <step-114>`, {ref}`119 <step-119>`, {ref}`125 <step-125>`, {ref}`130 <step-130>`, {ref}`135 <step-135>`, {ref}`138 <step-138>`, {ref}`140 <step-140>`, {ref}`145 <step-145>`, {ref}`150 <step-150>`, {ref}`153 <step-153>`, {ref}`155 <step-155>`, {ref}`160 <step-160>`, {ref}`163 <step-163>`, {ref}`170 <step-170>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"HP 4062UX"** — *inference:* {ref}`CAPILD2 <step-150>`, {ref}`HPETEST <step-171>`
* **"Engineering manual Probe Station"; sort and reliability-lab tools** — *named; no production prober, and the sort and reliability tools serve other purposes (inference):* {ref}`HPETEST <step-171>`

**Published measurements of a SkyWater test tile.** Google's raw-data
repository does not describe SkyWater's own production test or name its
tester. It states that its
initial data "was collected under contract by CoolCAD Electronics LLC
using the manufacturing test tile created by SkyWater",[^raw-data-readme]
of which "each of the Google MPW runs includes two
copies";[^raw-data-testtile-prop] the pad documentation lists the
structures,[^raw-data-testtile-pads] and the IC-CAP files record sweeps,
compliance and source-measurement-unit channels.[^raw-data-mdm] The
repository names neither the tester nor the prober, and the files record
no temperature, date or wafer. What the files contain, and the thresholds,
currents and resistances extracted from them and set beside the PDK's
e-test limits, are described on the {ref}`HPETEST <step-171>` and
{ref}`test category <category-test>` pages and are not repeated here.

## Consumables and facilities

What is specific to this class is summarised here. None of the SkyWater
sources describes the fab's probe cards, calibration or test data system.

* **Probe cards and needles.** Cards laid out to the test-structure pads,
  with needles of tungsten, tungsten–rhenium, beryllium–copper or other
  alloys, whose contact resistance depends on material and cleaning
  frequency.[^broz-1999][^wiki-probecard]
* **Calibration.** Instruments are calibrated periodically (industry
  practice); Agilent's 4072B and 4073B prices included "one-time, on-site
  calibration".[^eepower-4070]
* **Chuck temperature control.** Hot and cold chucks for tests over
  temperature, such as the −60 °C to 300 °C range of the
  SUMMIT200,[^formfactor-summit200] and liquid nitrogen or helium for
  cryogenic stations.[^formfactor-pmc200]
* **Clean handling.** Mini-environments and SMIF interfaces on the
  prober.[^electroglas-4090u]
* **Test plans, limits and data systems.** Site, wafer and cassette test
  plans, limits and probe-card files,[^keithley-s600] and the data path to
  SPC and disposition that SkyWater lists with its tester.[^skw-01]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's test plan, sites and sampling are
not public beyond the PDK's e-test parameter tables, which the
{ref}`HPETEST <step-171>` page quotes.

* **E-test at the end of the flow.** {ref}`HPETEST <step-171>` names a
  parametric tester, an automatic prober with a hot/cold chuck, probe cards
  and manual stations; the probed pads are opened at
  {ref}`PDM <step-168>` and {ref}`PDME <step-169>`, and probe damage under
  aluminium pads is a known risk.[^hunter-2012]
* **Gate oxides and ONO.** {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`,
  {ref}`LVGOX <step-047>` and {ref}`IOX45 <step-063>` name C–V test
  structures beside the ellipsometer
  ({ref}`machine-film-thickness-metrology`).
* **Alloy anneals.** {ref}`ALLY1 <step-096>` and {ref}`ALLY <step-170>`
  name a C–V or charge-pumping test set for interface traps.
* **Contacts, vias and lines.** {ref}`CSIL <step-098>` and
  {ref}`CTME <step-108>` name contact chains, the via etches via chains,
  and the metal etches e-test — the Kelvin, chain,
  cross-bridge and comb/serpentine structures of the test-structure
  literature.[^proctor-1983][^sayah-1988][^buehler-1978]
* **MiM capacitors.** {ref}`CAPILD <step-135>`, {ref}`CAPME <step-138>`,
  {ref}`CAPILD2 <step-150>` and {ref}`CAP2ME <step-153>` name capacitor
  e-test; {ref}`CAPILD2 <step-150>` grades the 4062UX's "capacitance"
  capability as the public candidate (inference).[^skw-01]
* **The frame.** The PDK places e-test modules in the frame outside the
  product dice, on the {ref}`HPETEST <step-171>` page's reading of its
  layer and periphery rules; the probe card and prober stepping follow
  that layout (industry practice).

## Related pages

* {ref}`category-test` — test structures, sheet resistance, transistor
  parameters and SPC.
* {ref}`machine-sheet-resistance-metrology` — the in-line sheet-resistance
  monitors that precede e-test.
* {ref}`machine-film-thickness-metrology` — the optical gauges beside the
  C–V monitors.
* {ref}`machine-defect-inspection` — the optical counterpart of the
  electrical defect structures.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "Wafer
  Sort/Test" and "REL Lab" entries and the e-test and cryogenic probing
  services.[^skw-01]
* BRL Test, *4062UX* listing — the HP 4062UX description and
  configuration.[^brltest-4062]
* Keithley Instruments, *Series S600 Parametric Test Systems* data sheet —
  per-pin electronics, parallel test and test-plan software.[^keithley-s600]
* EE Power, *Agilent Technologies Offers New 4070 Series Testers* (2002) —
  the 4072B and 4073B.[^eepower-4070]
* Electroglas, *Horizon 4090*, *Horizon 4085X* and *Horizon 4090µ* pages
  and 1999 annual report — probers and what they
  do.[^electroglas-4090][^electroglas-4085x][^electroglas-4090u][^electroglas-1999]
* Tokyo Electron, *P-8XL & P-12XL Series Wafer Prober* — the TEL prober
  line.[^tel-prober]
* FormFactor, *Cascade SUMMIT200* and *Cascade PMC200* product
  pages.[^formfactor-summit200][^formfactor-pmc200]
* ITRS 2001, *Yield Enhancement* — parametric data in yield
  learning.[^itrs-2001-yield]
* Google's SKY130 raw-data repository — the README, the test-tile README
  and pad documentation, and the MDM file
  format.[^raw-data-readme][^raw-data-testtile-prop][^raw-data-testtile-pads][^raw-data-mdm]

### High-level understanding

* Wikipedia, *Wafer testing* — parametric and functional wafer test and the
  prober.[^wiki-test]
* Wikipedia, *Probe card*.[^wiki-probecard]
* Wikipedia, *Automatic test equipment*.[^wiki-ate]
* Wikipedia, *Keithley Instruments* and *Agilent Technologies* — the
  parametric tester vendors.[^wiki-keithley][^wiki-agilent]

### Deep dive

* Buehler, *Microelectronic Test Patterns*, NBS 1974 — an early NBS
  publication on test patterns.[^buehler-1974]
* Buehler, Grant and Thurber (NBS), *JES* 1978 — bridge and van der Pauw
  structures for electrical line width.[^buehler-1978]
* Proctor, Linholm and Mazer (NBS), *IEEE TED* 1983 — four- and
  six-terminal contact-resistance structures.[^proctor-1983]
* Sayah and Buehler, ICMTS 1988 — a comb/serpentine/cross-bridge structure
  tested on a parametric test system.[^sayah-1988]
* Lukaszek, Grambow and Yarbrough, *IEEE TSM* 1990 — a test chip for
  automated diagnosis of CMOS yield problems.[^lukaszek-1990]
* Linholm, Allen and Cresswell, *Proc. SPIE* 1994 — a review of test
  structures for feature placement and electrical line
  width.[^linholm-1994]
* Bhushan et al., ICMTS 2006 — ring-oscillator arrays read with a frequency
  counter.[^bhushan-2006]
* Ortiz-Conde et al., *Microelectron. Reliab.* 2002 — threshold-voltage
  extraction methods.[^ortiz-conde-2002]
* Cheng and Hu, *MOSFET Modeling & BSIM3 User's Guide* — from parametric
  data to model parameters.[^cheng-1999]
* Spanos, *Proc. IEEE* 1992 — statistical process control in semiconductor
  manufacturing.[^spanos-1992]
* Broz and Rincon, ITC 1999 — probe contact resistance at elevated
  temperature.[^broz-1999]
* Hunter et al., IMAPS 2012 — bond-pad damage from wafer
  probing.[^hunter-2012]

## Open questions

* Which prober serves the "HP 4062UX", and whether `HPETEST` runs on it,
  are not stated.[^skw-01]
* Whether "Summit 200 Prober/Tester" and "PMC200 Cryo Probe" are the
  FormFactor systems of those names, and whether any reliability-lab tool
  takes part in e-test, are not stated.[^skw-01]
* SKY130's e-test plan — structures, sites per wafer, sampling across a lot
  and disposition rules — is not public beyond the PDK's parameter tables.
* The model list above is incomplete: it covers the HP/Agilent, Keithley,
  Electroglas, Tokyo Electron and Cascade/FormFactor tools for which a
  public description was found, not every parametric tester and prober of
  the period.

<!-- footnotes -->

[^wiki-test]: Wikipedia, *Wafer testing*.
    <https://en.wikipedia.org/wiki/Wafer_testing>
[^wiki-probecard]: Wikipedia, *Probe card*.
    <https://en.wikipedia.org/wiki/Probe_card>
[^wiki-ate]: Wikipedia, *Automatic test equipment*.
    <https://en.wikipedia.org/wiki/Automatic_test_equipment>
[^wiki-keithley]: Wikipedia, *Keithley Instruments*.
    <https://en.wikipedia.org/wiki/Keithley_Instruments>
[^wiki-agilent]: Wikipedia, *Agilent Technologies*.
    <https://en.wikipedia.org/wiki/Agilent_Technologies>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^brltest-4062]: BRL Test, *4062UX — Keysight / Agilent Parametric
    Testers* (listing), accessed 2026-09-13.
    <https://www.brltest.com/index.php?main_page=product_info&products_id=7874>
[^keithley-s600]: Keithley Instruments, *Series S600 Parametric Test
    Systems*, data sheet.
    <https://download.tek.com/datasheet/SeriesS600_DataSht.pdf>
[^eepower-4070]: EE Power, *Agilent Technologies Offers New 4070 Series
    Testers*, new-products item, 2002-12-03, accessed 2026-09-13.
    <https://eepower.com/new-industry-products/agilent-technologies-offers-new-4070-series-testers/>
[^electroglas-4090]: Electroglas, *The Horizon 4090*, product page;
    Wayback Machine capture of 1998-02-11.
    <https://web.archive.org/web/19980211212301/http://www.electroglas.com:80/products/4090.htm>
[^electroglas-4085x]: Electroglas, *Horizon 4085X*, product page; Wayback
    Machine capture of 1998-02-11.
    <https://web.archive.org/web/19980211212526/http://www.electroglas.com:80/products/4085x.htm>
[^electroglas-4090u]: Electroglas, *Horizon 4090µ*, product page; Wayback
    Machine capture of 2001-07-13.
    <https://web.archive.org/web/20010713004941/http://www.electroglas.com:80/products/4090micro.html>
[^electroglas-1999]: Electroglas, *1999 Annual Report*, "Wafer Probing"
    section, web page; Wayback Machine capture of 2002-05-30.
    <https://web.archive.org/web/20020530031508/http://www.electroglas.com:80/press/pressreleases/reports/1999annual/wafer.htm>
[^tel-prober]: Tokyo Electron, *P-8XL & P-12XL Series Wafer Prober*
    (Certified Used Equipment), product page, accessed 2026-09-13.
    <https://www.telcertifiedused.com/cue/buy/product-test.jsp>
[^formfactor-summit200]: FormFactor, *Cascade SUMMIT200 Probe Station*,
    product page, accessed 2026-09-13.
    <https://www.formfactor.com/product/probe-systems/200-mm-systems/summit200/>
[^formfactor-pmc200]: FormFactor, *Cascade PMC200 — 200 mm Cryogenic Probe
    Station*, product page, accessed 2026-09-13.
    <https://www.formfactor.com/product/probe-systems/wafer-multi-chip-cryogenic-systems/pmc200/>
[^itrs-2001-yield]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Yield Enhancement*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
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
[^raw-data-mdm]: Agilent Technologies, *IC-CAP User's Guide*, "MDM File
    Structure" (IC-CAP 2008 documentation), retrieved 2026-09-13,
    <https://people.ece.ubc.ca/robertor/Links_files/Files/ICCAP-2008-doc/icug/icug136.html>;
    and SkyWater PDK Authors, `docs/_static/mdm-format.png`,
    `google/skywater-pdk-sky130-raw-data` repository.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/_static/mdm-format.png>
[^linholm-1994]: L. W. Linholm, R. A. Allen and M. W. Cresswell,
    "Microelectronic test structures for feature placement and electrical
    linewidth metrology", *Proc. SPIE* **10274**, Handbook of Critical
    Dimension Metrology and Process Control: A Critical Review, 1027407
    (1994). <https://doi.org/10.1117/12.187462>
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
[^lukaszek-1990]: W. Lukaszek, K. G. Grambow and W. J. Yarbrough, "Test
    chip based approach to automated diagnosis of CMOS yield problems",
    *IEEE Transactions on Semiconductor Manufacturing* **3**(1), 18–27
    (1990). <https://doi.org/10.1109/66.47972>
[^bhushan-2006]: M. Bhushan, M. B. Ketchen, S. Polonsky and A. Gattiker,
    "Ring oscillator based technique for measuring variability
    statistics", *2006 IEEE International Conference on Microelectronic
    Test Structures*, pp. 87–92. <https://doi.org/10.1109/ICMTS.2006.1614281>
[^ortiz-conde-2002]: A. Ortiz-Conde, F. J. García Sánchez, J. J. Liou,
    A. Cerdeira, M. Estrada and Y. Yue, "A review of recent MOSFET
    threshold voltage extraction methods", *Microelectronics
    Reliability* **42**(4–5), 583–596 (2002).
    <https://doi.org/10.1016/S0026-2714(02)00027-6>
[^cheng-1999]: Y. Cheng and C. Hu, *MOSFET Modeling & BSIM3 User's
    Guide*, Kluwer Academic, 1999. <https://doi.org/10.1007/b117400>
[^spanos-1992]: C. J. Spanos, "Statistical process control in
    semiconductor manufacturing", *Proceedings of the IEEE* **80**(6),
    819–830 (1992). <https://doi.org/10.1109/5.149445>
[^broz-1999]: J. J. Broz and R. M. Rincon, "Probe contact resistance
    variations during elevated temperature wafer test", *Proc.
    International Test Conference 1999*, pp. 396–405.
    <https://doi.org/10.1109/TEST.1999.805761>
[^hunter-2012]: S. Hunter, J. L. Clark, D. Hornberger and L. Rubio, "Use
    of Wire Bonding to Study Bond Pad Damage from Wafer Probe",
    *International Symposium on Microelectronics* **2012**(1), 384–395
    (IMAPS, 2012). <https://doi.org/10.4071/isom-2012-TP41>
