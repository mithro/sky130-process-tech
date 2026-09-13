(machine-sheet-resistance-metrology)=
# Sheet-resistance and dose metrology

An implanter reports the dose it believes it delivered; a fab checks it
on wafers. Two instrument families do this in line. A four-point probe
presses a row of needles onto a doped layer or a metal film and measures
its sheet resistance, from which dose, activation, junction or film
thickness can be followed. A thermal-wave (modulated-reflectance) monitor
heats a spot with a modulated laser and reads the change of reflectance,
which depends on the implant damage and so on the dose, without contact
and before any anneal. Non-contact eddy-current gauges measure metal and
highly conductive films. This page describes the classes, lists
representative 200 mm-era models, and then says what SkyWater has
published and which SKY130 steps this reference assigns to the class.
Implant dose control in general is on the
{ref}`implant category page <category-implant>`.

| | Sheet-resistance and dose metrology |
|---|---|
| What it does | Resistivity mapping systems are "indispensable process control tools for measuring sheet resistance on a broad range of applications", correlated "to carrier concentration or film thickness";[^tencor-rs75-1995] the thermal-wave monitor "detects any changes in implant conditions that affect the silicon damage" and "is primarily sensitive to dosage".[^tw-implant] |
| Four-point probe | "Current is passed through the outer pair of probes and the floating potential is measured across the inner pair";[^valdes-1954] correction factors cover finite sample shapes.[^smits-1958] |
| Modulated reflectance | "a noncontact, nondestructive technique that requires no special sample preparation or processing, has high sensitivity even at low dose, and provides a one-micron spatial resolution capability".[^smith-1985] |
| Dose range | Sheet resistance is "an industry standard for monitoring high and medium dose ion implants", measured directly down to 2 × 10¹¹ cm⁻² with careful processing, with a double-implant technique for low doses;[^smith-1986] thermal-wave monitoring of "low dose (E11-E12 ions/cm2)" implants for threshold control.[^tw-implant] |
| Speed | "approximately 1 second per test site" and "over 100 wafers per hour" at five sites on 200 mm (OmniMap RS75);[^tencor-rs75-1995] sites "as small as 10um by 10um" on product wafers (Therma-Probe 500).[^tw-tp-2000] |
| Requirement at 130 nm | ITRS 2001: "4-point probe measurement is used for high dose implant and thermally modulated optical reflectance is used for low-dose implant process control", and "Both methods require improvement".[^itrs-2001-met] |
| 200 mm era | Prometrix, then Tencor, OmniMap four-point probes (RS75 of 1995), the OmniMap NC110 for metal films and KLA-Tencor's RS-100;[^tencor-resistivity-1997][^tencor-rs75-1995][^kla-rs100] Therma-Wave's Therma-Probe 500 (1996);[^tw-tp-2000] Boxer Cross's BX-10 (2000).[^sing-2000] |
| SkyWater-listed tool | None named |
| SKY130 steps | 48 steps; see {ref}`SKY130 steps assigned to this class <machine-sheet-resistance-metrology-steps>` |

## What the machine class is and how it works

Both families measure a proxy. Sheet resistance depends on the
carriers in a layer, and so on activation as well as dose (industry
practice);[^wiki-rs] the thermal-wave signal depends on the damage an
implant leaves before annealing.[^tw-implant] ITRS 2001 divides the work by
dose, the four-point probe for high-dose and modulated reflectance for
low-dose implants.[^itrs-2001-met]

### Sheet resistance and the four-point probe

Sheet resistance is the resistance of a square of a thin layer; for an
implanted or diffused layer it is set by the integral of carrier
concentration and mobility down to the junction.[^wiki-rs] Valdes described
the four-point method for germanium: four probes in a line, current
through the outer pair and the potential measured across the inner
pair.[^valdes-1954] A four-point probe "is used to avoid contact resistance,
which can often have the same magnitude as the sheet
resistance",[^wiki-rs] the four-terminal principle behind Kelvin
measurements in general.[^wiki-4t] Smits evaluated the correction factors
for rectangular and circular samples, noting that "Diffused surface layers can be
treated as two-dimensional structures";[^smits-1958] SEMI MF84 is the
standard in-line four-point-probe test method for silicon
wafers.[^semi-mf84] Perloff, Wahl and Conragan automated the measurement for
doping-uniformity maps and showed that "the four-point probe and van der
Pauw resistors may be used interchangeably for doping uniformity
measurements";[^perloff-1977] van der Pauw's theorem underlies the second
kind of structure.[^vdp-1958] A Prometrix patent describes the mapping
machine: a rotatable wafer stage, a probe head with "a linear array of at
least four equally spaced probe tips", and "contour scan and diameter
scan modes".[^pat-rsmap-prometrix]

For implant monitoring, sheet resistance is read on monitor wafers
annealed after the implant, the test-wafer practice Therma-Wave
describes.[^tw-implant] Smith, Johnson and Keenan extended
the direct method down to 2 × 10¹¹ cm⁻² and described a double-implant
technique in which "an initial implant" creates a measurable layer and
the second implant's dose is followed by "the change in the sheet
resistance due to the implant damage created by the second implant into
the first".[^smith-1986] For ultra-shallow junctions, Hillard, Borland and
Ye later used elastic probes that form non-penetrating contacts, conducting
through the native oxide.[^hillard-2004]

### Thermal and plasma waves

The thermal-wave monitor comes from Therma-Wave. A modulated pump beam
heats a spot periodically, and "the change in reflectivity at the sample
surface which is a function of the changing surface temperature" is read
by a probe beam;[^pat-thermalwave-thermawave] Rosencwaig et al. showed that
thermal waves can be detected "in a noncontact and highly sensitive
manner, through the dependence of sample optical reflectance on
temperature".[^rosencwaig-1985] In a semiconductor the pump also creates a
periodic electron–hole plasma, which "affects the index of refraction of
the sample", so the modulated reflectance carries information on "ion
dopant concentrations, residue deposits and defects";[^pat-plasmawave-thermawave]
Opsal and Rosencwaig proposed depth profiling with "the critically damped
plasma wave".[^opsal-1985] Smith, Rosencwaig and Willenborg applied the
method to implant monitoring in 1985, "directly on the patterned product
integrated circuit wafers as well as on the usual test
wafers".[^smith-1985] Therma-Wave described its limits: the
technique "can be used to monitor changes in ion beam energy, but its
sensitivity varies for different penetration depth of ions in silicon",
and "It is also sensitive to channeling and various scanning
effects".[^tw-implant]

### Non-contact and newer methods

Metal films and heavily doped layers can be measured without contact.
Miller, Robinson and Wiley showed that "the power absorbed by a thin
semiconductor slice in an oscillating magnetic field is accurately
proportional to the material conductivity", a method applicable "from
semiconductors to metals";[^miller-1976] non-contact eddy-current systems
are used "for inline measurements and for high-resolution
mapping".[^wiki-rs] Boxer Cross's BX-10, developed for in-line
measurement of ultra-shallow junctions, was also evaluated for "low dose
implants on nonannealed wafers and high dose implants on annealed
wafers";[^sing-2000] ITRS 2001 lists carrier illumination, "an optical
technology", among the new methods "under evaluation".[^itrs-2001-met]

### Where the numbers go

A resistivity map shows the uniformity of an implant or a deposition across
the wafer; Tencor presented the maps as a way to "create dense contour
maps and get an accurate picture of their manufacturing
process".[^tencor-rs75-1995] Therma-Wave argued for measuring before any
anneal, because the conventional check of implanting, "quickly annealing"
and electrically testing monitor wafers takes time and because "annealing
can conceal implanter malfunctions".[^tw-implant] The sheet resistances
that decide whether a finished wafer passes are measured again, on test
structures, at electrical test ({ref}`HPETEST <step-171>`).

## Representative 200 mm-era models

* **Prometrix, then Tencor and KLA-Tencor.** The OmniMap four-point-probe
  mappers, "Based on the four-point probe technology pioneered by the
  Prometrix division", including the RS75 series of 1995 with its
  temperature-compensated RS75/tc model;[^tencor-rs75-1995] the OmniMap
  NC110, which "Measures resistivity directly on product wafers" and gives
  data on "aluminum and tungsten metallization schemes such as
  Ti/TiN/Al/TiN, TiN/W";[^tencor-resistivity-1997] and the RS-100, described on a 2002 capture,
  "the tool of choice in the metals, CMP, and diffusion
  modules".[^kla-rs100]
* **Therma-Wave.** The Therma-Probe, introduced in 1985,[^tw-history] and
  the Therma-Probe 500, "introduced in July of 1996", of which Therma-Wave
  reported that "By April 1998, more than 360 Therma-Probe systems had been
  installed".[^tw-tp-2000][^tw-products-1997]
* **Boxer Cross.** The BX-10 optical junction and implant monitor
  (2000).[^sing-2000]

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page names no four-point probe,
thermal-wave monitor or other sheet-resistance gauge.[^skw-01] The
nearest entries are the implanters, whose lines give dose ranges ("1e11
to 1e14" on the "Axcelis 8250 Mid current" entry, "5e12 to 5e16" on the
"Axcelis GSD Hi dose" entry) but no metrology, and the parametric tester
"HP 4062UX" under "Wafer Sort/Test", which measures structures at
electrical test rather than monitor wafers in line (our
reading).[^skw-01] No job posting or profile quoted on the step pages
names a sheet-resistance or thermal-wave tool.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` there
is **no evidence** of any particular sheet-resistance or dose monitor at
SkyWater: no SkyWater page, filing, posting or profile names one. That a
fab running the listed implanters, furnaces and PVD tools monitors sheet
resistance is industry practice, not a SkyWater statement. The caveats
that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`; the
machines index lists this class among those "with no named SkyWater
tool".

(machine-sheet-resistance-metrology-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a four-point probe or
a thermal-wave monitor (identical to the
{ref}`machines index <machines-index>` table):

{ref}`008 <step-008>`, {ref}`015 <step-015>`, {ref}`018 <step-018>`–{ref}`020 <step-020>`, {ref}`023 <step-023>`, {ref}`024 <step-024>`, {ref}`027 <step-027>`, {ref}`028 <step-028>`, {ref}`031 <step-031>`, {ref}`032 <step-032>`, {ref}`034 <step-034>`, {ref}`037 <step-037>`, {ref}`038 <step-038>`, {ref}`045 <step-045>`, {ref}`050 <step-050>`, {ref}`053 <step-053>`, {ref}`056 <step-056>`, {ref}`065 <step-065>`, {ref}`066 <step-066>`, {ref}`069 <step-069>`, {ref}`072 <step-072>`, {ref}`073 <step-073>`, {ref}`075 <step-075>`, {ref}`082 <step-082>`, {ref}`083 <step-083>`, {ref}`086 <step-086>`, {ref}`088 <step-088>`, {ref}`092 <step-092>`, {ref}`097 <step-097>`–{ref}`099 <step-099>`, {ref}`101 <step-101>`, {ref}`109 <step-109>`, {ref}`110 <step-110>`, {ref}`112 <step-112>`, {ref}`120 <step-120>`, {ref}`121 <step-121>`, {ref}`123 <step-123>`, {ref}`131 <step-131>`, {ref}`132 <step-132>`, {ref}`134 <step-134>`, {ref}`136 <step-136>`, {ref}`146 <step-146>`, {ref}`147 <step-147>`, {ref}`149 <step-149>`, {ref}`151 <step-151>`, {ref}`161 <step-161>`

No step page grades a sheet-resistance or thermal-wave tool at SkyWater
("Machines likely used at SkyWater"), because none is named; the
implant, anneal and metal-deposition pages grade the process tools, which
are on {ref}`machine-medium-current-implanter`,
{ref}`machine-high-current-implanter`, {ref}`machine-high-energy-implanter`,
{ref}`machine-rapid-thermal-processor`, {ref}`machine-pvd-cluster-tool`
and {ref}`machine-tungsten-cvd`.

## Consumables and facilities

What is specific to this class is summarised here; the
{ref}`materials index <materials-index>` lists monitor wafers. None of
the SkyWater sources describes the fab's monitor-wafer practice.

* **Monitor wafers.** Bare wafers implanted with a test recipe and, for
  sheet resistance, annealed before measurement; the test wafers
  Therma-Wave describes being sacrificed "by implanting them under specific
  recipes and quickly annealing them for electrical testing".[^tw-implant]
  Low-dose sheet-resistance monitors may need a first implant to create
  the measurable layer.[^smith-1986]
* **Probe heads.** A linear array of at least four equally spaced probe
  tips, moved into and out of contact with the wafer;[^pat-rsmap-prometrix]
  tips wear and are replaced (industry practice).
* **Temperature control.** Sheet resistance varies with temperature, which
  Tencor's RS75/tc corrected with "a patented temperature compensation
  (tc) solution" to improve "long-term repeatability, accuracy, and
  system-to-system matching".[^tencor-rs75-1995]
* **Lasers.** The thermal-wave monitors use a pump and a probe laser;
  the Therma-Probe 500's "Solid state lasers provide more stable
  performance and longer lifetime".[^tw-tp-2000]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's implant doses, monitor recipes and
sheet-resistance limits for in-line monitors are not public; the PDK's
e-test sheet resistances are quoted on the {ref}`HPETEST <step-171>` page.

* **Threshold, channel, tip and halo implants.** The pages for these
  implants ({ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`,
  {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PTSI <step-037>`,
  {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`ASTI <step-065>`,
  {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`,
  {ref}`LDBHI <step-073>`) name thermal-wave monitoring, alone or with a
  four-point probe; Therma-Wave presented the method for "low dose
  (E11-E12 ions/cm2)" implants that set threshold voltages.[^tw-implant]
  Because the signal "is also sensitive to channeling", a change of beam
  angle on the tilted implants of this group would show in it (inference
  from the vendor statement).[^tw-implant]
* **Wells.** The deep N-well, N-well and P-well pages name a four-point
  probe, a thermal-wave monitor or both. For MeV implants the thermal-wave
  sensitivity depends on how deep the ions go,[^tw-implant] so a
  sheet-resistance monitor after anneal is the more direct check (our
  reading).
* **High-dose implants.** The poly-doping, resistor and source/drain pages
  ({ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`,
  {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`)
  name a four-point probe, the high-dose method in ITRS
  2001.[^itrs-2001-met]
* **Anneals.** The implant-anneal and activation pages
  ({ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`,
  {ref}`RTAD <step-088>`) name a four-point probe with thermocouple wafers
  for calibration, {ref}`RTAD2 <step-092>` a four-point probe beside
  dielectric monitors, and the silicide page
  ({ref}`CSIL <step-098>`) a four-point probe for silicide monitors.
* **Metal films.** The liner, tungsten, TiN and Ti/Al–Cu pages name a
  four-point probe beside XRF and stress gauges
  ({ref}`machine-film-thickness-metrology`). For a metal of known
  resistivity the sheet resistance gives the thickness,
  {math}`t = \rho/R_s`,[^wiki-rs] which is why KLA-Tencor aimed the RS-100
  at "the metals, CMP, and diffusion modules".[^kla-rs100]
* **Monitors and e-test.** In-line monitors run on blanket wafers; the
  e-test sheet resistances of the PDK (for example N⁺ diffusion, local
  interconnect and metal 3) are measured on test structures of the
  finished wafer, and the public test tile described on the
  {ref}`HPETEST <step-171>` page carries van der Pauw and four-terminal
  structures, the two kinds Perloff et al. found interchangeable for
  uniformity measurements.[^perloff-1977]

## Related pages

* {ref}`category-implant` — dose control and the implant steps.
* {ref}`category-anneal` — activation and silicide anneals.
* {ref}`category-test` — sheet resistance, van der Pauw structures and
  e-test.
* {ref}`machine-medium-current-implanter`,
  {ref}`machine-high-current-implanter` and
  {ref}`machine-high-energy-implanter` — the implanters whose dose is
  monitored.
* {ref}`machine-film-thickness-metrology` — the other gauges run on metal
  monitor wafers.
* {ref}`machine-parametric-tester` — the sheet resistances measured on test structures at
  e-test.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the implanter dose
  ranges and the parametric tester; no sheet-resistance gauge.[^skw-01]
* ITRS 2001, *Metrology* — four-point probe for high dose, modulated
  reflectance for low dose, and the need for better
  methods.[^itrs-2001-met]
* Tencor, OmniMap RS75 press release (1995) and *Resistivity Measurement*
  page (1997) — Prometrix four-point probes and the
  NC110.[^tencor-rs75-1995][^tencor-resistivity-1997]
* KLA-Tencor, *RS-100* product page (2002) — the four-point probe for
  metals, CMP and diffusion.[^kla-rs100]
* Therma-Wave, *Ion Implantation Monitoring*, *Therma-Probe Family*,
  products (1997) and corporate history pages — the thermal-wave
  monitor, its uses and
  limits.[^tw-implant][^tw-tp-2000][^tw-products-1997][^tw-history]

### High-level understanding

* Wikipedia, *Sheet resistance* — ohms per square, implanted layers,
  four-point and eddy-current measurement.[^wiki-rs]
* Wikipedia, *Four-terminal sensing*.[^wiki-4t]
* Schroder, *Semiconductor Material and Device Characterization* — the
  reference text on resistivity measurement.[^schroder-2006]

### Deep dive

* Valdes, *Proc. IRE* 1954 — the four-point probe.[^valdes-1954]
* Smits, *Bell Syst. Tech. J.* 1958 — four-point-probe correction
  factors.[^smits-1958]
* van der Pauw, *Philips Res. Rep.* 1958 — sheet resistance of arbitrary
  shapes.[^vdp-1958]
* SEMI MF84 — the in-line four-point-probe test method.[^semi-mf84]
* Perloff, Wahl and Conragan, *JES* 1977 — automated four-point and van der
  Pauw doping-uniformity maps.[^perloff-1977]
* Perloff and Mallory (Prometrix), US 4,703,252 — the automatic sheet
  resistance mapping system.[^pat-rsmap-prometrix]
* Smith, Johnson and Keenan, *Proc. SPIE* 1986 — low-dose sheet
  resistance monitoring with a double implant.[^smith-1986]
* Miller, Robinson and Wiley, *Rev. Sci. Instrum.* 1976 — contactless
  conductivity measurement by RF power absorption.[^miller-1976]
* Rosencwaig et al. (Therma-Wave), US 4,579,463 — thermal waves detected
  through reflectivity.[^pat-thermalwave-thermawave]
* Rosencwaig et al., *APL* 1985 — detection of thermal waves through
  optical reflectance.[^rosencwaig-1985]
* Opsal and Rosencwaig, *APL* 1985 — thermal and plasma wave depth
  profiling in silicon.[^opsal-1985]
* Opsal, Rosencwaig and Smith (Therma-Wave), US 4,854,710 — plasma-wave
  evaluation of dopants and defects.[^pat-plasmawave-thermawave]
* Smith, Rosencwaig and Willenborg, *APL* 1985 — ion implant monitoring
  with thermal waves.[^smith-1985]
* Sing, Borden and Bechtler, IIT 2000 — the BX-10 as a low- and high-dose
  monitor.[^sing-2000]
* Hillard, Borland and Ye, IWJT 2004 — a non-penetrating four-point probe
  for ultra-shallow junctions.[^hillard-2004]

## Open questions

* Which sheet-resistance, thermal-wave or eddy-current gauges SkyWater
  uses, if any of the models above, is not public.
* Which SKY130 implants are monitored by thermal waves and which by sheet
  resistance after anneal, and against what limits, is not public.
* Whether the implanters' dose ranges on the capabilities page were
  qualified with sheet-resistance monitors is not stated.[^skw-01]
* The model list above is incomplete: it covers the Prometrix/Tencor,
  Therma-Wave and Boxer Cross tools for which a public description was
  found, not every sheet-resistance or dose monitor of the period.

<!-- footnotes -->

[^tencor-rs75-1995]: Tencor Instruments, *Tencor's Film Measurement
    Division Introduces New OmniMap RS75 Resistivity Mapping System*,
    press release, 1995-10-10; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302035054/http://www.tencor.com:80/press/omnimaprs75.html>
[^tencor-resistivity-1997]: Tencor Instruments, *Resistivity Measurement*
    (OmniMap NC110 and RS75), product page; Wayback Machine capture of
    1997-03-02.
    <https://web.archive.org/web/19970302033556/http://www.tencor.com:80/products/resistivity.html>
[^kla-rs100]: KLA-Tencor, *RS-100: Advanced Resistivity Metrology*,
    product page; Wayback Machine capture of 2002-08-16.
    <https://web.archive.org/web/20020816223302/http://www.kla-tencor.com:80/products/metrology/rs-100/rs-100.html>
[^tw-implant]: Therma-Wave, *Ion Implantation Monitoring* (applications),
    web page; Wayback Machine capture of 2001-07-13.
    <https://web.archive.org/web/20010713111006/http://www.thermawave.com:80/apps/implant.htm>
[^tw-tp-2000]: Therma-Wave, *The Therma-Probe Family*, product page;
    Wayback Machine capture of 2000-10-06.
    <https://web.archive.org/web/20001006232958/http://www.thermawave.com:80/prod_tpf.htm>
[^tw-products-1997]: Therma-Wave, *Therma-Wave Products* (Opti-Probe and
    Therma-Probe 500 Series), web page; Wayback Machine capture of
    1997-01-26.
    <https://web.archive.org/web/19970126142849/http://www.thermawave.com:80/products.html>
[^tw-history]: Therma-Wave, *Therma-Wave Corporate History*, web page;
    Wayback Machine capture of 2001-07-13.
    <https://web.archive.org/web/20010713111217/http://www.thermawave.com:80/aboutus/corphistory.htm>
[^itrs-2001-met]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Metrology*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-rs]: Wikipedia, *Sheet resistance*.
    <https://en.wikipedia.org/wiki/Sheet_resistance>
[^wiki-4t]: Wikipedia, *Four-terminal sensing*.
    <https://en.wikipedia.org/wiki/Four-terminal_sensing>
[^schroder-2006]: D. K. Schroder, *Semiconductor Material and Device
    Characterization*, 3rd ed., Wiley, 2006.
    <https://doi.org/10.1002/0471749095>
[^valdes-1954]: L. B. Valdes, "Resistivity Measurements on Germanium for
    Transistors", *Proceedings of the IRE* **42**(2), 420–427 (1954).
    <https://doi.org/10.1109/JRPROC.1954.274680>
[^smits-1958]: F. M. Smits, "Measurement of Sheet Resistivities with the
    Four-Point Probe", *Bell System Technical Journal* **37**(3), 711–718
    (1958). <https://doi.org/10.1002/j.1538-7305.1958.tb03883.x>
[^vdp-1958]: L. J. van der Pauw, "A method of measuring specific
    resistivity and Hall effect of discs of arbitrary shape", *Philips
    Research Reports* **13**, 1–9 (1958); reprinted in S. M. Sze (ed.),
    *Semiconductor Devices: Pioneering Papers*, World Scientific, 1991,
    pp. 174–182. <https://doi.org/10.1142/9789814503464_0017>
[^semi-mf84]: SEMI MF84, *Test Method for Measuring Resistivity of Silicon
    Wafers With an In-Line Four-Point Probe*, SEMI.
    <https://store-us.semi.org/products/mf008400-semi-mf84-test-method-for-measuring-resistivity-of-silicon-wafers-with-an-in-line-four-point-probe>
[^perloff-1977]: D. S. Perloff, F. E. Wahl and J. Conragan, "Four-Point
    Sheet Resistance Measurements of Semiconductor Doping Uniformity",
    *Journal of The Electrochemical Society* **124**(4), 582–590 (1977).
    <https://doi.org/10.1149/1.2133355>
[^pat-rsmap-prometrix]: D. S. Perloff and C. Mallory (Prometrix),
    *Apparatus and methods for resistivity testing*, US 4,703,252 A, filed
    1985-02-22, granted 1987-10-27.
    <https://patents.google.com/patent/US4703252A/en>
[^smith-1986]: A. K. Smith, W. H. Johnson and W. A. Keenan, "Sheet
    Resistance Low Dose Monitoring Using The Double Implant Technique",
    *Proc. SPIE* **0623**, Advanced Processing and Characterization of
    Semiconductors III, 50 (1986). <https://doi.org/10.1117/12.961194>
[^hillard-2004]: R. J. Hillard, J. Borland and C. W. Ye, "Accurate
    determination of ultra-shallow junction sheet resistance with a
    non-penetrating four point probe", *Fourth International Workshop on
    Junction Technology (IWJT 2004)*, pp. 98–101.
    <https://doi.org/10.1109/IWJT.2004.1306768>
[^miller-1976]: G. L. Miller, D. A. H. Robinson and J. D. Wiley,
    "Contactless measurement of semiconductor conductivity by radio
    frequency-free-carrier power absorption", *Review of Scientific
    Instruments* **47**(7), 799–805 (1976).
    <https://doi.org/10.1063/1.1134756>
[^pat-thermalwave-thermawave]: A. Rosencwaig, J. Opsal, W. L. Smith and
    D. L. Willenborg (Therma-Wave Partners), *Detecting thermal waves to
    evaluate thermal parameters*, US 4,579,463 A, filed 1984-05-21, granted
    1986-04-01. <https://patents.google.com/patent/US4579463A/en>
[^rosencwaig-1985]: A. Rosencwaig, J. Opsal, W. L. Smith and D. L.
    Willenborg, "Detection of thermal waves through optical reflectance",
    *Applied Physics Letters* **46**(11), 1013–1015 (1985).
    <https://doi.org/10.1063/1.95794>
[^opsal-1985]: J. Opsal and A. Rosencwaig, "Thermal and plasma wave depth
    profiling in silicon", *Applied Physics Letters* **47**(5), 498–500
    (1985). <https://doi.org/10.1063/1.96105>
[^pat-plasmawave-thermawave]: J. Opsal, A. Rosencwaig and W. L. Smith
    (Therma-Wave), *Method and apparatus for evaluating surface and
    subsurface features in a semiconductor*, US 4,854,710 A, filed
    1987-07-23, granted 1989-08-08.
    <https://patents.google.com/patent/US4854710A/en>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985). <https://doi.org/10.1063/1.96079>
[^sing-2000]: D. Sing, P. Borden and L. Bechtler, "Low and high dose
    process monitoring using the BX-10 implant monitor system", *2000
    International Conference on Ion Implantation Technology Proceedings*,
    pp. 639–641. <https://doi.org/10.1109/IIT.2000.924234>
