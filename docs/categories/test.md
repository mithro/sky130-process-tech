(category-test)=
# Electrical test / metrology

## What this class of step does

Electrical test is where the finished wafer is measured rather than
changed. After the final alloy anneal ({ref}`ALLY <step-170>`) the
wafer is placed on a prober, a card of fine needles is lowered onto
special test structures, and a parametric tester measures transistors,
resistors, capacitors, diodes and interconnect chains one by one. The
results say whether the wafer was built to specification — whether the
threshold voltages, drive currents, sheet resistances and contact
resistances are inside their limits — and therefore whether it may be
shipped, reworked or scrapped. This is the {term}`e-test` or wafer
acceptance test ({term}`WAT`); it is the single {ref}`HPETEST
<step-171>` step at the end of the SKY130 flow.

Precisely, "wafer testing is a step performed during semiconductor
device fabrication after back end of line (BEOL) and before IC
packaging", and it comes in two kinds: wafer parametric tests, performed
at "a few locations on each wafer" to verify that fabrication succeeded,
and wafer functional testing (also called die sort or
{term}`wafer sort`), which applies "special test patterns" to test "all individual
integrated circuits on the wafer" ([Wikipedia: Wafer testing][wiki-test]).
This category page concerns the first kind; the second is a product
step performed by or for the customer, and its results are recorded not
by inking but "in a file, named a wafermap" ([Wikipedia: Wafer
testing][wiki-test]).

## Physics and engineering background

### Test structures and the PCM

Parametric test does not measure the product circuit. It measures a
process control monitor ({term}`PCM`): a fixed set of test structures
placed in the {term}`scribe line` between dies (or in dedicated
drop-in sites), stepped onto every reticle field so that they see
exactly the same processing as the product. A 130 nm CMOS PCM
typically contains:

* **Transistors** of each flavour (core, I/O, low-Vt, high-Vt,
  high-voltage, native) at several widths and lengths, including the
  minimum gate length, from which threshold voltage, saturation and
  linear drive current, off-state leakage, body effect, gate leakage
  and breakdown are extracted.
* **Sheet-resistance structures** — {term}`van der Pauw structure`s
  or long bars — for every conducting film: n-well, p-well, n⁺ and p⁺
  diffusions with and without silicide, the poly gate and each poly
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
* **Diodes and isolation** — well and junction diodes, STI leakage
  between adjacent active areas, latch-up structures.
* **Memory cells** — for a SONOS process, single cells or small arrays
  that are programmed and erased to check the memory window.

The structures are laid out so that every measurement is a
four-terminal one where a resistance is involved: "a constant current
is applied to two probes, and the potential on the other two probes is
measured with a high-impedance voltmeter", so that probe and lead
resistance drop out ([Wikipedia: Sheet resistance][wiki-rs];
[Wikipedia: Four-terminal sensing][wiki-4t]).

### Sheet resistance and van der Pauw

The resistance of a square of a thin film is its {term}`sheet
resistance`, {math}`R_s = \rho/t`, in ohms per square; "a square sheet
with sheet resistance 10 ohm/square has an actual resistance of 10 ohm,
regardless of the size of the square" ([Wikipedia: Sheet
resistance][wiki-rs]). A four-point probe on a large area gives
{math}`R_s = (\pi/\ln 2)\,V/I \approx 4.53\,V/I`; on a small
symmetric test structure with four contacts on its periphery, van der
Pauw's theorem gives the sheet resistance of an arbitrarily shaped
lamina from two resistance measurements, which is why the cloverleaf or
Greek-cross "van der Pauw structure" is the standard PCM element
([Wikipedia: Van der Pauw method][wiki-vdp]). Contact resistance is
extracted from a Kelvin cross or from a transfer-length-method ladder
of contacts at increasing spacing ([Wikipedia: Transfer length
method][wiki-tlm]; [Wikipedia: Contact resistance][wiki-rc]).

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
and {math}`I_{\mathrm{dsat}}` targets for the 130 nm node
([ITRS 2001, Process Integration, Devices and Structures][itrs2001-pids]).

### Limits, SPC and the feedback loop

Each measured parameter has a specification (the WAT limits that
decide disposition) and, inside it, control limits used for
{term}`SPC`. The tester stores every value with its wafer, site and
lot identity; yield-management software correlates parameters with
tool history and with sort yield, and the data feed the compact-model
extraction from which the PDK's SPICE models are built. The SKY130 PDK
publishes those models and their corner definitions ([SKY130 PDK
documentation][pdk]), so e-test is, in effect, the step that checks a
wafer against the PDK. ITRS 2001 treats the test-structure and
metrology needs of this loop in its Metrology and Yield Enhancement
chapters ([ITRS 2001, Metrology][itrs2001-met]; [ITRS 2001, Yield
Enhancement][itrs2001-yield]).

### In-line metrology

Although only the final e-test is a numbered step in the SKY130 flow,
every category above has in-line metrology attached to it —
ellipsometry after oxidation and deposition, {term}`CD-SEM` and
overlay after lithography and etch, sheet resistance after implant
and anneal, thickness mapping after CMP, particle counts after clean —
so that most excursions are caught long before test. E-test is the
last and most complete check, and the only one that sees the finished
device.

## Typical equipment

* **Parametric testers**: Keithley Series S600 (designed for "process
  control, process and equipment tuning and optimization, equipment
  qualification, Wafer Acceptance Testing, and device modeling and
  characterization" [keithley]); Hewlett-Packard/Agilent 4062UX,
  4070, 4072 and 4073 series ([HP 4062UX][hp4062]). Both families
  combine source-measure units,
  a capacitance meter and a switching matrix under test-plan software
  ([Wikipedia: Keithley Instruments][wiki-keithley];
  [Wikipedia: Agilent Technologies][wiki-agilent]).
* **Wafer probers**: Electroglas 4090 and 4085X, TEL P-8 and P-12,
  Tokyo Seimitsu UF-series, with temperature-controlled chucks
  ([Wikipedia: Automatic test equipment][wiki-ate]).
* **Probe cards**: cantilever needle cards laid out to the PCM pad
  ring ([Wikipedia: Probe card][wiki-probecard]).
* **Bench characterisation**: HP/Agilent 4155/4156 semiconductor
  parameter analysers and manual probe stations for engineering
  work.
* **Wafer sort** (customer or product step): Teradyne, Advantest,
  Credence/LTX testers with high-pin-count probe cards
  ([Wikipedia: Teradyne][wiki-teradyne]; [Wikipedia:
  Advantest][wiki-advantest]).

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

* Keithley Instruments, *Series S600 Parametric Test Systems* (data
  sheet). <https://download.tek.com/datasheet/SeriesS600_DataSht.pdf>
* Semiconductor Online, "S600 Series Parametric Test Systems".
  <https://www.semiconductoronline.com/doc/s600-series-parametric-test-systems-0001>
* BRL Test, "4062UX — Keysight / Agilent Parametric Testers".
  <https://www.brltest.com/index.php?main_page=product_info&products_id=7874>
* *ITRS 2001 Edition: Process Integration, Devices and Structures*.
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf>
* *ITRS 2001 Edition: Metrology*.
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
* *ITRS 2001 Edition: Yield Enhancement*.
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
* *ITRS 2001 Edition: Test and Test Equipment*.
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Test.pdf>
* SkyWater Technology / Google, *SkyWater SKY130 PDK documentation*
  (device models and corners).
  <https://skywater-pdk.readthedocs.io/en/main/>

### High-level

* Wikipedia, "Wafer testing".
  <https://en.wikipedia.org/wiki/Wafer_testing>
* Wikipedia, "Sheet resistance".
  <https://en.wikipedia.org/wiki/Sheet_resistance>
* Wikipedia, "Van der Pauw method".
  <https://en.wikipedia.org/wiki/Van_der_Pauw_method>
* Wikipedia, "Four-terminal sensing".
  <https://en.wikipedia.org/wiki/Four-terminal_sensing>
* Wikipedia, "Transfer length method".
  <https://en.wikipedia.org/wiki/Transmission_line_measurement>
* Wikipedia, "Contact resistance".
  <https://en.wikipedia.org/wiki/Contact_resistance>
* Wikipedia, "Probe card". <https://en.wikipedia.org/wiki/Probe_card>
* Wikipedia, "Automatic test equipment".
  <https://en.wikipedia.org/wiki/Automatic_test_equipment>
* Wikipedia, "Statistical process control".
  <https://en.wikipedia.org/wiki/Statistical_process_control>
* Wikipedia, "Threshold voltage".
  <https://en.wikipedia.org/wiki/Threshold_voltage>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 4
  (yield and manufacturing) and the measurement sections of ch. 7–8.
* M. Quirk and J. Serda, *Semiconductor Manufacturing Technology*,
  Prentice Hall, 2001, ISBN 978-0-13-081520-0, ch. 15 ("Process
  Monitoring") and ch. 19 ("Wafer Test").
* H. Xiao, *Introduction to Semiconductor Manufacturing Technology*,
  2nd ed., SPIE Press, 2012, ch. 14. <https://doi.org/10.1117/3.924283>
* S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics and
  Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7, ch. 6
  (MOSFET characteristics).

### Deep dive

* L. J. van der Pauw, "A method of measuring specific resistivity and
  Hall effect of discs of arbitrary shape", *Philips Research Reports*
  **13**, 1–9 (1958). Reprinted in S. M. Sze (ed.), *Semiconductor
  Devices: Pioneering Papers*, World Scientific, 1991.
  <https://doi.org/10.1142/9789814503464_0017>
* R. H. Dennard et al., "Design of ion-implanted MOSFET's with very
  small physical dimensions", *IEEE Journal of Solid-State Circuits*
  **9**(5), 256–268 (1974) — the scaling rules against which the
  parameters are judged. <https://doi.org/10.1109/JSSC.1974.1050511>
* Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
  Manufacturing Technology*, 2nd ed., CRC Press, 2007 (chapters on
  test structures, yield and metrology).
  <https://doi.org/10.1201/9781420017663>
* D. K. Schroder, *Semiconductor Material and Device Characterization*,
  3rd ed., Wiley, 2006. <https://doi.org/10.1002/0471749095>

[wiki-test]: https://en.wikipedia.org/wiki/Wafer_testing
[wiki-rs]: https://en.wikipedia.org/wiki/Sheet_resistance
[wiki-4t]: https://en.wikipedia.org/wiki/Four-terminal_sensing
[wiki-vdp]: https://en.wikipedia.org/wiki/Van_der_Pauw_method
[wiki-tlm]: https://en.wikipedia.org/wiki/Transmission_line_measurement
[wiki-rc]: https://en.wikipedia.org/wiki/Contact_resistance
[wiki-keithley]: https://en.wikipedia.org/wiki/Keithley_Instruments
[wiki-agilent]: https://en.wikipedia.org/wiki/Agilent_Technologies
[wiki-ate]: https://en.wikipedia.org/wiki/Automatic_test_equipment
[wiki-probecard]: https://en.wikipedia.org/wiki/Probe_card
[wiki-teradyne]: https://en.wikipedia.org/wiki/Teradyne
[wiki-advantest]: https://en.wikipedia.org/wiki/Advantest
[keithley]: https://download.tek.com/datasheet/SeriesS600_DataSht.pdf
[hp4062]: https://www.brltest.com/index.php?main_page=product_info&products_id=7874
[itrs2001-pids]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001PIDS.pdf
[itrs2001-met]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf
[itrs2001-yield]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf
[pdk]: https://skywater-pdk.readthedocs.io/en/main/
