(category-test)=
# Electrical test / metrology

## What this class of step does

Electrical test is where the finished wafer is measured rather than
changed. After the final {term}`alloy anneal` ({ref}`ALLY <step-170>`) the
wafer is placed on a prober, a card of fine needles is lowered onto
special test structures, and a parametric tester measures transistors,
resistors, capacitors, diodes and interconnect chains one by one. The
results say whether the wafer was built to specification — whether the
threshold voltages, drive currents, sheet resistances and contact
resistances are inside their limits — and therefore whether it may be
shipped, reworked or scrapped. This is the {term}`e-test` or wafer
acceptance test ({term}`WAT`); it is the single {ref}`HPETEST
<step-171>` step at the end of the SKY130 flow.

In the general description, "wafer testing is a step performed during
semiconductor device fabrication after back end of line (BEOL) and
before IC packaging"; this reference, whose phase table ends the back
end with the final alloy and test, files {ref}`HPETEST <step-171>`
itself under BEOL. Wafer testing comes in two kinds: wafer parametric tests, performed
at "a few locations on each wafer" to verify that fabrication succeeded,
and wafer functional testing (also called die sort or {term}`wafer
sort`), which applies "special test patterns" to test "all individual
integrated circuits on the wafer".[^wiki-test] This category page
concerns the first kind; the second is a product step performed by or
for the customer, and its results are recorded not by inking but "in a
file, named a wafermap".[^wiki-test]

## Physics and engineering background

### Test structures and the PCM

Parametric test does not measure the product circuit. It measures a
process control monitor ({term}`PCM`): a fixed set of test structures
placed in the {term}`scribe line` between dies (or in dedicated
drop-in sites), stepped onto every {term}`reticle` field so that they see
exactly the same processing as the product. A 130 nm CMOS PCM
typically contains:

* **Transistors** of each flavour (core, I/O, low-Vt, high-Vt,
  high-voltage, native) at several widths and lengths, including the
  minimum gate length, from which threshold voltage, saturation and
  linear drive current, off-state leakage, body effect, gate leakage
  and breakdown are extracted.
* **Sheet-resistance structures** — {term}`van der Pauw structure`s
  or long bars — for every conducting film: n-well, p-well, n⁺ and p⁺
  diffusions with and without {term}`silicide`, the poly gate and each poly
  resistor flavour, local interconnect and each metal level.
* **Contact and via structures** — {term}`Kelvin structure`s for the
  resistance of a single contact, and long chains of thousands of
  contacts or vias for yield and average resistance.
* **Interconnect structures** — comb and serpentine patterns that
  detect shorts and opens at minimum pitch, and line-width
  ("electrical CD") monitors.
* **Capacitors** — MOS capacitors whose C–V curve gives the gate-oxide
  thickness and flat-band voltage; MiM capacitors for capacitance
  density and leakage; junction capacitors.
* **Diodes and isolation** — well and junction diodes, {term}`STI` leakage
  between adjacent active areas, latch-up structures.
* **Memory cells** — for a {term}`SONOS` process, single cells or small arrays
  that are programmed and erased to check the memory window.

The structures are laid out so that every measurement is a
four-terminal one where a resistance is involved: "a constant current
is applied to two probes, and the potential on the other two probes is
measured with a high-impedance voltmeter", so that probe and lead
resistance drop out.[^wiki-rs][^wiki-4t]

For SKY130 one such structure list is public, although it is not stated
to be the fab's production PCM. Google's raw-data repository publishes
the pad documentation of the SkyWater "manufacturing test tile" carried
on Google's MPW runs: 273 numbered modules, each a line of up to twelve
pads with the terminal on each pad written
out.[^raw-data-testtile-pads][^raw-data-testtile-prop] By our count
they include 36 finger-capacitor ("VPP") modules, 28 poly-resistor
modules at 300 Ω/sq and 2 kΩ/sq (many as "Mismatch" pairs), 7 MiM
capacitor modules, 9 diode, 6 bipolar-transistor and 6 ring-oscillator
modules, together with licon and mcon contact strings, via chains from
via 1 to via 4, comb/serpentine and line-integrity structures, and SRAM,
SONOS, 2T-flash and antifuse structures; the transistor modules sweep
width, length and the source/drain extent (`sa`,
`sb`).[^raw-data-testtile-pads] The data measured on the tile were
"collected under contract by CoolCAD Electronics LLC" to help validate
the PDK.[^raw-data-readme]

### Sheet resistance and van der Pauw

The resistance of a square of a thin film is its {term}`sheet
resistance`, {math}`R_s = \rho/t`, in ohms per square; "a square sheet
with sheet resistance 10 ohm/square has an actual resistance of 10 ohm,
regardless of the size of the square".[^wiki-rs] A {term}`four-point probe` on a
large area gives {math}`R_s = (\pi/\ln 2)\,V/I \approx 4.53\,V/I`; on a
small symmetric test structure with four contacts on its periphery, van
der Pauw's theorem gives the {term}`sheet resistance` of an arbitrarily shaped
lamina from two resistance measurements, which is why the cloverleaf or
Greek-cross "van der Pauw structure" is the standard PCM
element.[^wiki-vdp] Contact resistance is extracted from a Kelvin cross
or from a transfer-length-method ladder of contacts at increasing
spacing.[^wiki-tlm][^wiki-rc]

### Transistor parameters

For each transistor the tester sweeps the gate at a small drain bias to
get the linear-region characteristics, extracting the threshold
voltage by linear extrapolation or at a constant current, the maximum
transconductance and the linear drain current; then at full supply
voltage it measures the saturation current {math}`I_{\mathrm{dsat}}`,
the off-current {math}`I_{\mathrm{off}}` (at picoampere sensitivity),
the substrate current, and the breakdown voltages. From the dependence
of threshold voltage on gate length the effective channel length and
{term}`halo` strength are inferred; from the dependence on width, the
STI edge effects. These are the same quantities the ITRS tabulates
node by node, for example the 2001 roadmap's {math}`I_{\mathrm{off}}`
and {math}`I_{\mathrm{dsat}}` targets for the 130 nm node.[^itrs-04]

### Limits, SPC and the feedback loop

Each measured parameter has a specification (the WAT limits that decide
disposition) and, inside it, control limits used for {term}`SPC`. The
tester stores every value with its wafer, site and lot identity;
yield-management software correlates parameters with tool history and
with sort yield, and the data feed the compact-model extraction from
which the PDK's SPICE models are built. The SKY130 PDK publishes those
models and their corner definitions,[^pdk-01] so e-test is, in effect,
the step that checks a wafer against the PDK. ITRS 2001 treats the
test-structure and metrology needs of this loop in its Metrology and
Yield Enhancement chapters.[^itrs-2001-met][^itrs-2001-yield]

### In-line metrology

Although only the final e-test is a numbered step in the SKY130 flow,
every category above has in-line metrology attached to it —
ellipsometry after oxidation and deposition, {term}`CD-SEM` and
{term}`overlay` after lithography and etch, sheet resistance after implant
and anneal, thickness mapping after {term}`CMP`, particle counts after clean —
so that most excursions are caught long before test. E-test is the
last and most complete check, and the only one that sees the finished
device.

## Typical equipment

* **Parametric testers**: Keithley Series S600 (designed for "process
  control, process and equipment tuning and optimization, equipment
  qualification, Wafer Acceptance Testing, and device modeling and
  characterization");[^keithley-s600] Hewlett-Packard/Agilent 4062UX,
  4070, 4072 and 4073 series.[^brltest-4062] Both families combine
  source-measure units, a capacitance meter and a switching matrix under
  test-plan software.[^wiki-keithley][^wiki-agilent]
* **Wafer probers**: Electroglas 4090 and 4085X, TEL P-8 and P-12, Tokyo
  Seimitsu UF-series, with temperature-controlled chucks.[^wiki-ate]
* **Probe cards**: cantilever needle cards laid out to the PCM pad
  ring.[^wiki-probecard] The open test tile that Google, NIST and the
  University of Michigan placed on MPW-5 is documented with a pad-grid
  drawing marked "40 µm" pads and "60 µm" and "80 µm" dimensions,
  beside a photograph of a needle "Probe Card".[^raw-data-testtile-open]
* **Bench characterisation**: HP/Agilent 4155/4156 semiconductor
  parameter analysers and manual probe stations for engineering work.
* **{term}`Wafer sort <wafer sort>`** (customer or product step): Teradyne, Advantest,
  Credence/LTX testers with high-pin-count probe
  cards.[^wiki-teradyne][^wiki-advantest]

## Typical consumables

* Probe cards and replacement needles (tungsten, tungsten–rhenium or
  beryllium–copper), which wear and must be re-planarised or re-tipped.
* Probe-tip cleaning media (abrasive films and gel pads) used every
  few touchdowns to remove aluminium debris.
* Reference and calibration standards for the source-measure units and
  capacitance meter.
* Test wafers and golden reference wafers for tester correlation.
* No process chemicals or gases; the wafer leaves e-test unchanged
  apart from probe marks on the scribe-line pads.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 171 | {ref}`HPETEST <step-171>` | Electrical test |

## References

### Cross-check

* Keithley, *Series S600 Parametric Test Systems* data sheet — the
  tester's intended uses.[^keithley-s600]
* Semiconductor Online, *S600 Series Parametric Test
  Systems*.[^semionline-s600]
* BRL Test, HP/Agilent 4062UX listing.[^brltest-4062]
* ITRS 2001, *Process Integration, Devices and Structures* — the
  I_off and I_dsat targets for the 130 nm node.[^itrs-04]
* ITRS 2001, *Metrology* — the test-structure and in-line metrology
  needs.[^itrs-2001-met]
* ITRS 2001, *Yield Enhancement* — the yield-learning
  loop.[^itrs-2001-yield]
* ITRS 2001, *Test and Test Equipment* — wafer sort and tester
  requirements.[^itrs-2001-test]
* SkyWater PDK documentation — the device models and corners that
  e-test checks a wafer against.[^pdk-01]
* Google's SKY130 raw-data repository — the README, the manufacturing
  test tile and its 273-module pad documentation, and the open MPW-5
  test
  tile.[^raw-data-readme][^raw-data-testtile-prop][^raw-data-testtile-pads][^raw-data-testtile-open]

### High-level understanding

* Wikipedia, *Wafer testing* — parametric versus functional test and
  the wafermap.[^wiki-test]
* Wikipedia, *Sheet resistance*.[^wiki-rs]
* Wikipedia, *Van der Pauw method*.[^wiki-vdp]
* Wikipedia, *Four-terminal sensing*.[^wiki-4t]
* Wikipedia, *Transfer length method*.[^wiki-tlm]
* Wikipedia, *Contact resistance*.[^wiki-rc]
* Wikipedia, *Probe card*.[^wiki-probecard]
* Wikipedia, *Automatic test equipment*.[^wiki-ate]
* Wikipedia, *Statistical process control*.[^wiki-spc]
* Wikipedia, *Threshold voltage*.[^wiki-vt]
* Wikipedia, *Keithley Instruments*.[^wiki-keithley]
* Wikipedia, *Agilent Technologies*.[^wiki-agilent]
* Wikipedia, *Teradyne*.[^wiki-teradyne]
* Wikipedia, *Advantest*.[^wiki-advantest]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 4 (yield
  and manufacturing) and the measurement sections of
  ch. 7–8.[^txt-01]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — ch. 15
  ("Process Monitoring") and ch. 19 ("Wafer Test").[^txt-07]
* Xiao, *Introduction to Semiconductor Manufacturing Technology* —
  ch. 14.[^txt-08]
* Sze and Lee, *Semiconductor Devices: Physics and Technology* — ch. 6
  (MOSFET characteristics).[^sze-2012]

### Deep dive

* van der Pauw, *Philips Res. Rep.* 1958 — the theorem behind the
  four-contact sheet-resistance structure.[^vdp-1958]
* Smits, *Bell Syst. Tech. J.* 1958 — four-point-probe sheet
  resistivity and its correction factors.[^smits-1958]
* Valdes, *Proc. IRE* 1954 — the original four-point-probe resistivity
  measurement.[^valdes-1954]
* Buehler, Grant and Thurber (NBS), *JES* 1978 — bridge and van der
  Pauw resistors for line-width (electrical {term}`CD`)
  measurement.[^buehler-1978]
* Proctor, Linholm and Mazer (NBS), *IEEE TED* 1983 — Kelvin
  measurement of interfacial contact resistance and its
  pitfalls.[^proctor-1983]
* Berger, *Solid-State Electron.* 1972 — contact models, the origin of
  the transmission-line method.[^berger-1972]
* Reeves and Harrison, *IEEE EDL* 1982 — extracting specific contact
  resistance from TLM ladders.[^reeves-1982]
* Ortiz-Conde et al., *Microelectron. Reliab.* 2002 — a review of
  MOSFET threshold-voltage extraction methods.[^ortiz-conde-2002]
* Cheng and Hu, *MOSFET Modeling & BSIM3 User's Guide* — how
  parametric data become compact-model parameters.[^cheng-1999]
* Hess and Weiland, *IEEE TSM* 1999 — extracting defect-density
  distributions from test structures for yield
  prediction.[^hess-1999]
* Stapper (IBM), *IBM J. Res. Dev.* 1983 — defect-sensitivity and
  critical-area yield modelling.[^stapper-1983]
* Maly, *Proc. IEEE* 1990 — design for manufacturability and the role
  of test structures.[^maly-1990]
* Yang et al. (TSMC), ICMTS 2005 — a 130 nm test-structure study of
  deep N-well flicker noise, an example of PCM-style
  characterisation.[^yang-2005]
* Dennard et al., *IEEE JSSC* 1974 — the scaling rules against which
  the measured parameters are judged.[^dennard-1974]
* Schroder, *Semiconductor Material and Device Characterization* — the
  reference text on resistivity, contact, C–V and MOSFET
  measurements.[^schroder-2006]
* SEMI MF84 — the standard four-point-probe resistivity test
  method.[^semi-mf84]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapters on test structures, yield and
  metrology.[^txt-09]

<!-- footnotes -->

[^wiki-test]: Wikipedia, *Wafer testing*.
    <https://en.wikipedia.org/wiki/Wafer_testing>
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^wiki-4t]: Wikipedia, *Four-terminal sensing*.
    <https://en.wikipedia.org/wiki/Four-terminal_sensing>
[^wiki-vdp]: Wikipedia, *Van der Pauw method*.
    <https://en.wikipedia.org/wiki/Van_der_Pauw_method>
[^wiki-tlm]: Wikipedia, *Transfer length method*.
    <https://en.wikipedia.org/wiki/Transmission_line_measurement>
[^wiki-rc]: Wikipedia, *Contact resistance*.
    <https://en.wikipedia.org/wiki/Contact_resistance>
[^itrs-04]: International Technology Roadmap for Semiconductors, *2001
    Edition: Process Integration, Devices, and Structures*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
[^pdk-01]: SkyWater PDK Authors, *SkyWater SKY130 PDK documentation*.
    <https://skywater-pdk.readthedocs.io/en/main/>
[^itrs-2001-met]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Metrology*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
[^itrs-2001-yield]: International Technology Roadmap for
    Semiconductors, *2001 Edition: Yield Enhancement*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
[^keithley-s600]: Keithley Instruments, *Series S600 Parametric Test
    Systems*, data sheet.
    <https://download.tek.com/datasheet/SeriesS600_DataSht.pdf>
[^brltest-4062]: BRL Test, *4062UX — Keysight / Agilent Parametric
    Testers* (listing).
    <https://www.brltest.com/index.php?main_page=product_info&products_id=7874>
[^wiki-keithley]: Wikipedia, *Keithley Instruments*.
    <https://en.wikipedia.org/wiki/Keithley_Instruments>
[^wiki-agilent]: Wikipedia, *Agilent Technologies*.
    <https://en.wikipedia.org/wiki/Agilent_Technologies>
[^wiki-ate]: Wikipedia, *Automatic test equipment*.
    <https://en.wikipedia.org/wiki/Automatic_test_equipment>
[^wiki-probecard]: Wikipedia, *Probe card*.
    <https://en.wikipedia.org/wiki/Probe_card>
[^wiki-teradyne]: Wikipedia, *Teradyne*.
    <https://en.wikipedia.org/wiki/Teradyne>
[^wiki-advantest]: Wikipedia, *Advantest*.
    <https://en.wikipedia.org/wiki/Advantest>
[^semionline-s600]: Semiconductor Online, *S600 Series Parametric Test
    Systems*.
    <https://www.semiconductoronline.com/doc/s600-series-parametric-test-systems-0001>
[^itrs-2001-test]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Test and Test Equipment*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Test.pdf>
[^wiki-spc]: Wikipedia, *Statistical process control*.
    <https://en.wikipedia.org/wiki/Statistical_process_control>
[^wiki-vt]: Wikipedia, *Threshold voltage*.
    <https://en.wikipedia.org/wiki/Threshold_voltage>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
[^sze-2012]: S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics
    and Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7.
    <https://www.wiley.com/en-us/Semiconductor+Devices%3A+Physics+and+Technology%2C+3rd+Edition-p-9780470537947>
[^vdp-1958]: L. J. van der Pauw, "A method of measuring specific
    resistivity and Hall effect of discs of arbitrary shape", *Philips
    Research Reports* **13**, 1–9 (1958); reprinted in S. M. Sze (ed.),
    *Semiconductor Devices: Pioneering Papers*, World Scientific, 1991,
    pp. 174–182. <https://doi.org/10.1142/9789814503464_0017>
[^smits-1958]: F. M. Smits, "Measurement of Sheet Resistivities with the
    Four-Point Probe", *Bell System Technical Journal* **37**(3),
    711–718 (1958). <https://doi.org/10.1002/j.1538-7305.1958.tb03883.x>
[^valdes-1954]: L. B. Valdes, "Resistivity Measurements on Germanium for
    Transistors", *Proceedings of the IRE* **42**(2), 420–427 (1954).
    <https://doi.org/10.1109/JRPROC.1954.274680>
[^buehler-1978]: M. G. Buehler, S. D. Grant and W. R. Thurber, "Bridge
    and van der Pauw Sheet Resistors for Characterizing the Line Width
    of Conducting Layers", *Journal of The Electrochemical Society*
    **125**(4), 650–654 (1978). <https://doi.org/10.1149/1.2131517>
[^proctor-1983]: S. J. Proctor, L. W. Linholm and J. A. Mazer, "Direct
    measurements of interfacial contact resistance, end contact
    resistance, and interfacial contact layer uniformity", *IEEE
    Transactions on Electron Devices* **30**(11), 1535–1542 (1983).
    <https://doi.org/10.1109/T-ED.1983.21334>
[^berger-1972]: H. H. Berger, "Models for contacts to planar devices",
    *Solid-State Electronics* **15**(2), 145–158 (1972).
    <https://doi.org/10.1016/0038-1101(72)90048-2>
[^reeves-1982]: G. K. Reeves and H. B. Harrison, "Obtaining the specific
    contact resistance from transmission line model measurements", *IEEE
    Electron Device Letters* **3**(5), 111–113 (1982).
    <https://doi.org/10.1109/EDL.1982.25502>
[^ortiz-conde-2002]: A. Ortiz-Conde, F. J. García Sánchez, J. J. Liou,
    A. Cerdeira, M. Estrada and Y. Yue, "A review of recent MOSFET
    threshold voltage extraction methods", *Microelectronics
    Reliability* **42**(4–5), 583–596 (2002).
    <https://doi.org/10.1016/S0026-2714(02)00027-6>
[^cheng-1999]: Y. Cheng and C. Hu, *MOSFET Modeling & BSIM3 User's
    Guide*, Kluwer Academic, 1999. <https://doi.org/10.1007/b117400>
[^hess-1999]: C. Hess and L. H. Weiland, "Extraction of wafer-level
    defect density distributions to improve yield prediction", *IEEE
    Transactions on Semiconductor Manufacturing* **12**(2), 175–183
    (1999). <https://doi.org/10.1109/66.762875>
[^stapper-1983]: C. H. Stapper, "Modeling of Integrated Circuit Defect
    Sensitivities", *IBM Journal of Research and Development* **27**(6),
    549–557 (1983). <https://doi.org/10.1147/rd.276.0549>
[^maly-1990]: W. Maly, "Computer-aided design for VLSI circuit
    manufacturability", *Proceedings of the IEEE* **78**(2), 356–392
    (1990). <https://doi.org/10.1109/5.52217>
[^yang-2005]: M. T. Yang et al., "Characterization and model of on-chip
    flicker noise with deep Nwell (DNW) isolation for 130nm and beyond
    SOC", *Proc. ICMTS 2005*, pp. 125–129.
    <https://doi.org/10.1109/ICMTS.2005.1452242>
[^dennard-1974]: R. H. Dennard, F. H. Gaensslen, H.-N. Yu, V. L.
    Rideout, E. Bassous and A. R. LeBlanc, "Design of ion-implanted
    MOSFET's with very small physical dimensions", *IEEE Journal of
    Solid-State Circuits* **9**(5), 256–268 (1974).
    <https://doi.org/10.1109/JSSC.1974.1050511>
[^schroder-2006]: D. K. Schroder, *Semiconductor Material and Device
    Characterization*, 3rd ed., Wiley, 2006.
    <https://doi.org/10.1002/0471749095>
[^semi-mf84]: SEMI MF84, *Test Method for Measuring Resistivity of
    Silicon Wafers With an In-Line Four-Point Probe*, SEMI.
    <https://store-us.semi.org/products/mf008400-semi-mf84-test-method-for-measuring-resistivity-of-silicon-wafers-with-an-in-line-four-point-probe>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
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
