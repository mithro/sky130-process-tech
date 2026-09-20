(machine-film-thickness-metrology)=
# Film thickness and stress metrology

Almost every film in the flow is measured after it is grown, deposited,
etched back or polished. Optical gauges — ellipsometers, reflectometers
and instruments that combine both — measure the thickness and refractive
index of oxides, nitrides and polysilicon; infrared spectrometers measure
the dopant or hydrogen content of dielectric films; X-ray fluorescence and
laser-acoustic gauges measure metal films that light cannot pass through;
and stress gauges measure how much a film bends the wafer. Most of these
instruments run on monitor wafers beside the product, some on test pads
of product wafers, and some are built into the process tool itself. This
page describes the classes, lists representative 200 mm-era models, and
then says what SkyWater has published and which SKY130 steps this
reference assigns to the class. Film growth and deposition are on the
{ref}`oxidation <category-oxidation>` and
{ref}`deposition <category-deposition>` category pages.

| | Film thickness and stress metrology |
|---|---|
| What it does | "sensitive, non-destructive, optical thickness and film quality measurements of bulk samples, single-layer thin films and multi-layer thin film stacks" (Prometrix UV-1250SE and UV-1270SE);[^tencor-thinfilm-1997] "accurate measurement of thin film stress on all types of films and substrates" (FLX-2320).[^kla-flx2320] |
| Optical principles | Ellipsometry "measures the change of polarization upon reflection or transmission and compares it to a model";[^wiki-ellipsometry] beam profile reflectometry "measures reflectivity as a function of angle of incidence for two mutually perpendicular polarization directions".[^tw-op3260] |
| Range and precision | "dielectric films from 0Å to 150,000Å", with "better than 0.1Å precision" on gate, tunnel and residual oxides in a 0.9 µm spot (Opti-Probe 3260);[^tw-op3260] "excellent precision for films as thin as 30 Å and as thick as 20 000 Å" for beam profile reflectometry.[^rosencwaig-1992] |
| Opaque films | X-ray fluorescence from the coating and the substrate;[^shiraiwa-1968] optical acoustics for "up to six metal or other opaque film layers", "from less than 20 Angstroms to greater than five microns" at 60 wafers per hour (MetaPULSE).[^rudolph-1999] |
| Stress | Wafer curvature measured "with a laser scanning device";[^flinn-1987] "a wide range of temperatures from -65° C to 500° C" on the FLX-2320 and "up to 900º C" on the FLX-2900.[^tencor-stress-1997] |
| Requirement at 130 nm | ITRS 2001 asks for an equivalent-oxide-thickness measurement precision of 0.0052 nm (3σ) in 2001, from a precision-to-tolerance ratio of 0.1 against a ±4 % process range, for high-performance logic with an EOT of 1.3–1.6 nm.[^itrs-2001-met] |
| 200 mm era | Therma-Wave's Opti-Probe (1992) and its 3260 and 5240 models;[^tw-history][^tw-op3260][^tw-op5000] Prometrix (Tencor) UV-1250SE and UV-1270SE;[^tencor-thinfilm-1997] Rudolph's SpectraLASER and MetaPULSE;[^rudolph-1999] Nanometrics' NanoSpec automated and integrated systems;[^nanometrics-2000] Tencor FLX stress gauges.[^tencor-stress-1997] |
| SkyWater-listed tool | None named apart from the Mirra's "On board metrology with feed forward and backward"[^skw-01] |
| SKY130 steps | 67 steps; see {ref}`SKY130 steps assigned to this class <machine-film-thickness-metrology-steps>` |

## What the machine class is and how it works

The gauges share a pattern: a beam of light, X-rays or sound probes a
small spot; a model of the film stack with known or fitted optical,
X-ray or acoustic constants turns the signal into thicknesses and
properties; and a wafer handler and pattern recognition place the spot on
a monitor wafer or a test pad. What differs is the probe, and therefore
which films a gauge can see.

### Ellipsometry

Ellipsometry "measures the change of polarization upon reflection or
transmission and compares it to a model", and can yield thickness,
composition and other properties of a thin film.[^wiki-ellipsometry]
Rudolph dates the production instrument to 1977, "when we introduced our
AutoEL, the industry's first production-oriented, microprocessor-based
ellipsometer".[^rudolph-1999] Two refinements followed. Multiple angles of
incidence: a Rudolph patent focuses one beam so that it strikes the
sample over "a whole range of angles of incidence" at once, collected on
a detector array "without scanning",[^pat-maiwl-rudolph] and Rudolph's
SpectraLASER used four lasers for multiple-angle, multiple-wavelength
ellipsometry.[^rudolph-1999] Multiple wavelengths: Tencor's Prometrix
UV-1250SE and UV-1270SE combined spectroscopic ellipsometry with
ultraviolet spectrophotometry to "Simultaneously and independently
determine parameters such as refractive index and extinction coefficient"
of films and film stacks.[^tencor-thinfilm-1997] The price is model
dependence. For very thin oxides Chandler-Horowitz found that
instrument-to-instrument and lab-to-lab deviations must be addressed
because "the derived film thickness is dependent on many factors",
naming instrument precision and accuracy, film and substrate models,
optical constants, regression analysis and surface
contamination.[^chandler-horowitz-2003] SEMI MF576 is the standard test
method for insulator thickness and refractive index on silicon by
ellipsometry.[^semi-mf576]

### Reflectometry and beam-profile methods

A reflectometer measures how much light a film stack reflects. Rudolph
explained that reflectometry "uses white light", and that it is "often
more suitable for measuring thicker films, whereas ellipsometry is often
more suitable for measuring very thin films";[^rudolph-1999] Nanometrics
built its thickness systems on "microscope-based, non-contact
spectroscopic reflectometry", with spectroscopic ellipsometry and FTIR
options.[^nanometrics-2000] Tencor's SpectraMap SM300 mapped "most
dielectric films from 200 Angstroms to 4 microns in thickness on monitor
wafers".[^tencor-thinfilm-1997] Therma-Wave took a different route. Its
patent focuses a probe beam through a high-numerical-aperture lens, so
that the rays arrive over a spread of angles, measures the reflected
intensity across the beam as a function of angle, and solves the
thickness from the Fresnel equations; the method is "particularly
suitable for measuring thin films, such as oxide layers, on silicon
semiconductor samples".[^pat-bpr-thermawave] Rosencwaig et al. called it
beam profile reflectometry, performed "with a submicron spot
size",[^rosencwaig-1992] and Fanton et al. showed how the profiles can
yield "as many as three unknown film parameters
simultaneously".[^fanton-1993] The Opti-Probe combined beam profile
ellipsometry, beam profile reflectometry and spectrometry in one tool, and
Therma-Wave claimed it could "accurately measure thin oxide on nitride on
oxide (ONO) and oxide on poly on oxide (OPO)" and measure "thickness and
refractive index for monitoring PECVD nitride and oxynitride
processes".[^tw-op3260] Gauges of different makes must also agree. Kaiser
found that the common "fudge factor" offset between tools fails because
the relation between reference and measured thicknesses is not a fixed
constant, and proposed tuning the instruments' internal optical constants
instead.[^kaiser-1991]

### Infrared and X-ray methods

Some film properties are chemical. In doped glasses the phosphorus "is
normally detected by measuring the band centered at about 1335 cm-1" and
the boron from the band "centered at about 1420 cm-1"; Stout and Krishnan
note that such infrared measurements need substrates above 10 Ω·cm and
must be calibrated against a primary technique such as wet chemistry or
SIMS.[^stout-1989] Metal films are opaque to light, and for them X-rays
serve. In X-ray fluorescence the intensity of the characteristic X-rays
from the coating and from the substrate depends on the coating thickness;
Shiraiwa and Fujino derived the formulas, including the enhancement
effect between coating and substrate.[^shiraiwa-1968] For films of a few
nanometres, Windover measured tantalum thickness "within seconds" by
fixed-angle, energy-dispersive X-ray reflectivity, a technique aimed at
"very thin diffusion barrier measurements".[^windover-2001]

### Opaque films: picosecond ultrasonics

A laser pulse can also launch sound. Thomsen et al. used picosecond light
pulses "to generate and detect very short stress pulses", detected
"through a measurement of the changes they induce in the optical
reflectivity of the sample surface";[^thomsen-1986] the Brown University
patent covers the pump-and-probe system.[^pat-picosecond-brown] Rudolph
commercialised the method: its MetaPULSE systems "use ultra-fast lasers
to generate sound waves that pass down through a stack of metal or opaque
films such as copper and aluminum, sending back to the surface an echo
which is detected and analyzed", on product wafers in spots of ten
microns.[^rudolph-1999] Stoner et al. describe applications to "PVD TiN
and CVD WNx, CVD W edge thickness profiles, 5 metal layers with in a
single interconnect stack, ultrathin Ti, Ti/TiN adhesion
stacks".[^stoner-1998]

### Film stress from wafer curvature

A film under stress bends its substrate. Flinn, Gardner and Nix describe
"a measurement technique based on the determination of wafer curvature
with a laser scanning device", and interpret the changes of stress in
aluminium films over thermal cycles;[^flinn-1987] the curvature is
converted to stress with the relation named after Stoney, whose 1909
paper dealt with the tension of electrodeposited metal films (industry
practice).[^stoney-1909] Hu reviews why the numbers matter: CVD silicon
nitride, silicon dioxide and polysilicon "exhibit intrinsic stresses",
and "Large localized stresses are induced in the silicon substrate near
the edges and corners of such structural elements".[^hu-1991] Of Tencor's FLX
gauges, the FLX-2320's dual-wavelength technology switches wavelength "Whenever destructive
interference from a transparent film such as silicon nitride cancels one
of the wavelengths",[^kla-flx2320] the FLX-5400 mapped radial stress in
two and three dimensions, and the FLX-2900 heated to 900 °C for in-situ
measurements.[^tencor-stress-1997] KLA-Tencor aimed the FLX-2320 at
"production monitoring of critical reliability problems caused by metal
and dielectric film cracking, voiding, and lifting
formation".[^kla-flx2320]

### Stand-alone, integrated and in situ

Most of these gauges stood alone in the fab, but by 2000 some had moved
into the process tools. Nanometrics described integrated systems that
"can be attached to film deposition, CMP, CVD, etch and other process
tools", recorded an "OEM agreement to supply metrology systems for
Applied Materials' Mirra Mesa(TM) CMP system" in September 1998 and a
metrology system for the Producer QA CVD system in July
1999.[^nanometrics-2000] ITRS 2001 described integrated metrology as "the
slow migration from offline to inline and in situ measurements" and noted
that "many of the inline measurements for interconnect structures are
made on simplified structures or monitor wafers and are often
destructive".[^itrs-2001-met] The vendors sold product-wafer measurement
as a saving: MetaPULSE "By minimizing the need for test
wafers",[^rudolph-1999] the Opti-Probe "without using costly monitor
wafers".[^tw-op3260]

## Representative 200 mm-era models

* **Therma-Wave.** The Opti-Probe, introduced in 1992;[^tw-history] the
  Opti-Probe 3260 and 3260DUV, measuring TiN thickness and optical
  constants "in the UV range down to 190 nm";[^tw-op3260] and the
  Opti-Probe 5240 of the 5000 family, adding deep-UV spectroscopic and
  absolute ellipsometry.[^tw-op5000]
* **Prometrix, a Tencor division.** The UV-1250SE and its successor the
  UV-1270SE (1996, with an integrated SMIF minienvironment), the UV-1050
  broadband reflectometer for resists and anti-reflective coatings, the FT-750
  spectrophotometer for films "typically down to 150 Angstrom", and the
  SpectraMap SM300 mapper.[^tencor-thinfilm-1997][^tencor-uv1270se-1996]
* **Rudolph Technologies.** The AutoEL (1977), the SpectraLASER
  multiple-angle, multiple-wavelength ellipsometers, the MatrixMetrology
  line configured for CMP, diffusion or etch (1999), and the MetaPULSE
  optical-acoustic metal gauges, all on the Vanguard automation
  platform.[^rudolph-1999]
* **Nanometrics.** The NanoSpec 8000X and 9100 automated systems for 75 to
  200 mm wafers, the 9000i integrated system, and tabletop
  models.[^nanometrics-2000]
* **Tencor, then KLA-Tencor, stress gauges.** The FLX-2320, FLX-5400 and
  FLX-2900, described on a 1997 capture,[^tencor-stress-1997] and the
  FLX-2320 still listed in 2002 beside the ASET-F5x thin-film and Quantox gate-monitoring
  systems.[^kla-flx2320]

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page names no stand-alone
thickness, index or stress gauge. The entries that bear on the class are
in other tool groups:[^skw-01]

> "AMAT Mirra CMP" … "On board metrology with feed forward and backward"
>
> "Advanced Process Control (APC) feed forward and backwards"
>
> "PECVD silane oxide/nitride/oxynitride, C1" ("low temp, range of R.I.
> options"); "PECVD nitride C1" ("high R.I., low temp options")

The first is a line of the CMP entry, the second a line of the "Photo
Metrology" group, and the third two PECVD entries of the "Film
Deposition" group.[^skw-01] Read term by term, on our reading: "On board
metrology" is a gauge integrated into the polisher, of the kind
Nanometrics supplied for the Mirra Mesa,[^nanometrics-2000] but SkyWater
names neither the gauge nor what it measures; "R.I." is refractive index,
a property the ellipsometers and reflectometers above
measure,[^tw-op3260][^tencor-thinfilm-1997] but the entry describes a
deposition capability, not a gauge. The {ref}`machines index
<machines-skywater-published>` notes that the S-1 names Rudolph
Technologies, Nanometrics and Onto Innovation only in executive and
director biographies, which is not evidence of their tools.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
"On board metrology" line is **strong** evidence that the listed polisher
carries integrated metrology, and **no evidence** about which gauge it is
or what it measures.[^skw-01] For stand-alone thickness, index, FTIR, XRF
and stress gauges there is no public SkyWater evidence at all; the
machines index lists this class among those "with no named SkyWater tool"
apart from the Mirra line. The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-film-thickness-metrology-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names an ellipsometer,
reflectometer, film-thickness mapper, FTIR or XRF gauge, or a stress gauge
(identical to the {ref}`machines index <machines-index>` table):

{ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`LINOX <step-010>`–{ref}`NS19 <step-013>`, {ref}`TUNME <step-039>`, {ref}`ONO <step-040>`, {ref}`GOX100 <step-043>`, {ref}`GOXETCH <step-046>`–{ref}`SAGD <step-048>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`IOX45 <step-063>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`–{ref}`RTAD2 <step-092>`, {ref}`SACETCH <step-095>`, {ref}`TI/TIN1 <step-097>`, {ref}`WDEP <step-099>`–{ref}`LITIN <step-101>`, {ref}`LINIT <step-104>`–{ref}`CMPL <step-106>`, {ref}`TIN2 <step-109>`–{ref}`TIAL6 <step-112>`, {ref}`NILD3 <step-115>`–{ref}`NCAPOX3 <step-117>`, {ref}`TIN3 <step-120>`–{ref}`TIAL12 <step-123>`, {ref}`NILD4 <step-126>`–{ref}`NCAPOX4 <step-128>`, {ref}`TIN4 <step-131>`–{ref}`CAPTIW1 <step-136>`, {ref}`CAPME <step-138>`, {ref}`NILD5 <step-141>`–{ref}`NCAPOX5 <step-143>`, {ref}`TIN5 <step-146>`–{ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`, {ref}`NILD6 <step-156>`–{ref}`NCAPOX6 <step-158>`, {ref}`WTIAL5 <step-161>`, {ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>`

How the step pages grade the SkyWater tool whose entry carries the
integrated metrology ("Machines likely used at SkyWater"), as collected
on the machines index:

* **"AMAT Mirra CMP"** — *inference from the film:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`CMPL <step-106>`, {ref}`CMPM <step-116>`, {ref}`CMPM2 <step-127>`, {ref}`CMPM3 <step-142>`, {ref}`CMPM4 <step-157>`; *inference from the film; which of the two tungsten processes not public:* {ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>`; see {ref}`category-cmp`.

Those grades concern the polisher; {ref}`CMPM4 <step-157>` quotes the
"On board metrology" line within its grade. No step page grades a
thickness, index or stress gauge at SkyWater, because none is named.

## Consumables and facilities

What is specific to film metrology is summarised here; the
{ref}`materials index <materials-index>` lists monitor wafers. None of
the SkyWater sources describes the fab's metrology standards, recipes or
monitor-wafer practice. Monitor and test wafers are described on the
{ref}`substrates and test wafers <material-substrates>` page.

* **Light sources.** The Opti-Probe used "A highly stable, 20,000-hour
  diode laser", "A 5000-hour halogen lamp" and a deuterium source for the
  ultraviolet;[^tw-op3260] Rudolph preferred "long life solid state lasers
  rather than the traditional white light sources" to reduce the cost of
  re-qualifying a replaced source.[^rudolph-1999]
* **Monitor wafers.** Blanket films on bare wafers for thickness, index,
  stress and composition, with substrates of suitable resistivity for
  infrared work;[^stout-1989] ITRS 2001 notes how much interconnect
  metrology relied on them.[^itrs-2001-met]
* **Optical-constant libraries and reference films.** The film models and
  constants that turn a signal into a thickness, and reference films for
  matching gauges.[^chandler-horowitz-2003][^kaiser-1991]
* **X-ray sources.** A conventional low-power tube, such as the 20 kV,
  20 mA, 400 W copper or chromium source of Windover's reflectivity
  gauge.[^windover-2001]
* **Calibration for composition.** Primary analyses — wet chemistry,
  ICP or SIMS — to calibrate FTIR dopant measurements.[^stout-1989]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's thickness, index and stress
targets, limits and sampling plans are not public.

* **Gate and tunnel oxides.** The gate-oxide pages
  ({ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`,
  {ref}`IOX45 <step-063>`) and the ONO page ({ref}`ONO <step-040>`) name
  a spectroscopic ellipsometer beside C–V test structures. For thin oxides
  Chandler-Horowitz lists the factors that must be controlled to hold
  the precision the roadmap asks for,[^chandler-horowitz-2003] and
  Therma-Wave claimed that its Opti-Probe measured ONO stacks where
  "Conventional techniques regularly fail this test".[^tw-op3260]
* **Nitrides and stress.** The isolation-nitride, gate-nitride, spacer,
  local-interconnect cap and passivation pages ({ref}`ISONIT <step-003>`,
  {ref}`GATENIT <step-058>`, {ref}`SPNIT <step-076>`,
  {ref}`LINIT <step-104>`, {ref}`NTSD <step-167>`) name a stress gauge;
  Hu's review describes the stresses that nitride and other films induce
  at the edges of structures.[^hu-1991] {ref}`NTSD <step-167>` also names
  FTIR, for hydrogen content.
* **Etch-rate monitors.** {ref}`TUNME <step-039>`,
  {ref}`GOXETCH <step-046>` and {ref}`SACETCH <step-095>` name an
  ellipsometer on monitor wafers; subtracting a map after etch from one
  before gives the etch-rate uniformity.[^tw-op3260]
* **CMP.** The CMP pages name an optical thickness mapper or reflectometer,
  and {ref}`CMPNIT <step-012>` names Nanometrics, KLA-Tencor and Rudolph
  gauges; SkyWater's polisher lists on-board metrology "with feed forward
  and backward".[^skw-01] Whether that gauge measures SKY130's polishes is
  not stated.
* **Doped glass.** {ref}`PSG <step-089>` names ellipsometry and FTIR for
  thickness and phosphorus content, the infrared band method Stout and
  Krishnan describe.[^stout-1989]
* **Metal films.** The liner, TiN, TiW and Ti/Al–Cu stack pages ({ref}`overview-metal-cap` sets out which cap the metal stacks carry) and the
  first tungsten fill ({ref}`WDEP <step-099>`) name XRF, a four-point
  probe and a stress gauge; the later tungsten-fill pages
  ({ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`,
  {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>`) name a four-point
  probe and a stress gauge. For opaque liners and stacks, picosecond
  ultrasonics measures each layer of a multilayer stack.[^stoner-1998]
* **Capacitor dielectrics.** {ref}`CAPILD <step-135>` and
  {ref}`CAPILD2 <step-150>` name a spectroscopic ellipsometer for
  thickness and index, and the capacitor etch pages
  ({ref}`CAPME <step-138>`, {ref}`CAP2ME <step-153>`) an ellipsometer; the
  capacitance itself is measured at e-test.

## Related pages

* {ref}`category-deposition` and {ref}`category-oxidation` — the films
  measured.
* {ref}`category-cmp` — the polishes, their endpoint and their metrology.
* {ref}`category-test` — in-line metrology and the electrical monitors at
  the end of the flow.
* {ref}`machine-defect-inspection` — the particle scans run on the same
  monitor wafers.
* {ref}`machine-sheet-resistance-metrology` — the four-point probe beside XRF on metal monitors.
* {ref}`machine-cross-section-sem-profilers` — cross-sections and profilers for what a thickness gauge
  cannot see.
* {ref}`machine-parametric-tester` — the C–V monitors beside the ellipsometer.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`material-substrates` — monitor and test wafers, their grades
  and reuse.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Optical generator and detector of stress pulses <patent-gp24957338>` — US 4,710,030 A (1985)
* {ref}`Method and apparatus for measuring thickness of thin films <patent-gp23365380>` — US 4,999,014 A (1989)
* {ref}`Simultaneous multiple angle/multiple wavelength ellipsometer and method <patent-gp24566844>` — US 5,166,752 A (1990)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 6,664,120 B1 <patent-gp29709141>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the Mirra's
  "On board metrology", the APC line and the PECVD "R.I."
  options.[^skw-01]
* [ITRS 2001, *Metrology*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>) — thickness precision, integrated metrology and
  monitor-wafer use.[^itrs-2001-met]
* Tencor, [*Thin Film Measurement*](<https://web.archive.org/web/19970302033547/http://www.tencor.com:80/products/thinfilmmesaurement.html>) and [*Thin Film Stress Measurement*](<https://web.archive.org/web/19970302033500/http://www.tencor.com:80/products/thinfilmstress.html>) pages
  (1997) and UV-1270SE press release (1996) — the Prometrix optical gauges
  and the FLX stress
  gauges.[^tencor-thinfilm-1997][^tencor-stress-1997][^tencor-uv1270se-1996]
* [KLA-Tencor, *FLX-2320* product page (2002)](<https://web.archive.org/web/20020820125852/http://www.kla-tencor.com:80/products/metrology/FLX-2320/FLX-2320.html>) — dual-wavelength stress
  measurement.[^kla-flx2320]
* Therma-Wave, *Opti-Probe 3260*, *Opti-Probe 5000* and corporate history
  pages — beam profile methods, range and
  precision.[^tw-op3260][^tw-op5000][^tw-history]
* [Rudolph Technologies, 1999 annual report](<https://web.archive.org/web/20000830152419/http://www.rudolphtech.com:80/ir/6859Rudolph99AR.pdf>) — ellipsometry, reflectometry
  and optical acoustics.[^rudolph-1999]
* [Nanometrics, Form 10-K for 2000](<https://web.archive.org/web/20030323070701/http://www.nanometrics.com:80/Downloads/10k_2000.pdf>) — reflectometry products and integrated
  metrology on Applied Materials tools.[^nanometrics-2000]

### High-level understanding

* [Wikipedia, *Ellipsometry*](<https://en.wikipedia.org/wiki/Ellipsometry>).[^wiki-ellipsometry]
* [Wikipedia, *Picosecond ultrasonics*](<https://en.wikipedia.org/wiki/Picosecond_ultrasonics>) — sound echoes from thin
  films.[^wiki-picosecond]
* [Wikipedia, *Fourier-transform infrared spectroscopy*](<https://en.wikipedia.org/wiki/Fourier-transform_infrared_spectroscopy>).[^wiki-ftir]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — process
  monitoring in a 200 mm fab.[^txt-07]

### Deep dive

* [Gold, Willenborg, Opsal and Rosencwaig (Therma-Wave), US 4,999,014](<https://patents.google.com/patent/US4999014A/en>) —
  thickness from reflected intensity against angle of
  incidence.[^pat-bpr-thermawave]
* [Spanier et al. (Rudolph), US 5,166,752](<https://patents.google.com/patent/US5166752A/en>) — simultaneous multiple-angle,
  multiple-wavelength ellipsometry.[^pat-maiwl-rudolph]
* [Rosencwaig et al., *APL* 1992](<https://doi.org/10.1063/1.107323>) — beam profile reflectometry for
  dielectric films.[^rosencwaig-1992]
* [Fanton et al., *JAP* 1993](<https://doi.org/10.1063/1.352421>) — multiparameter measurements by beam profile
  reflectometry.[^fanton-1993]
* [Chandler-Horowitz, AIP Conf. Proc. 2003](<https://doi.org/10.1063/1.1622490>) — the precision of ultra-thin
  oxide thickness by ellipsometry.[^chandler-horowitz-2003]
* [Kaiser, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.44451>) — correlating thickness gauges through optical
  constants.[^kaiser-1991]
* [SEMI MF576](<https://store-us.semi.org/products/mf057600-semi-mf576-test-method-for-measurement-of-insulator-thickness-and-refractive-index-on-silicon-substrates-by-ellipsometry>) — the ellipsometric test method for insulator thickness and
  index.[^semi-mf576]
* [Stout and Krishnan, *Proc. SPIE* 1989](<https://doi.org/10.1117/12.969563>) — infrared determination of boron
  and phosphorus in doped glass.[^stout-1989]
* [Shiraiwa and Fujino, *Adv. X-ray Anal.* 1968](<https://doi.org/10.1154/S0376030800005917>) — theory of coating
  thickness by X-ray fluorescence.[^shiraiwa-1968]
* [Windover, AIP Conf. Proc. 2001](<https://doi.org/10.1063/1.1354405>) — in-line X-ray reflectivity for thin
  metal films.[^windover-2001]
* [Thomsen et al., *Phys. Rev. B* 1986](<https://doi.org/10.1103/PhysRevB.34.4129>) — generation and detection of
  picosecond stress pulses.[^thomsen-1986]
* [Tauc, Maris and Thomsen (Brown University), US 4,710,030](<https://patents.google.com/patent/US4710030A/en>) — the optical
  stress-pulse generator and detector.[^pat-picosecond-brown]
* [Stoner et al., 1998](<https://doi.org/10.1063/1.56821>) — picosecond ultrasonics for thin metal process
  control.[^stoner-1998]
* [Flinn, Gardner and Nix, *IEEE TED* 1987](<https://doi.org/10.1109/T-ED.1987.22981>) — stress in aluminium
  metallisation from wafer curvature.[^flinn-1987]
* [Stoney, *Proc. R. Soc. A* 1909](<https://doi.org/10.1098/rspa.1909.0021>) — the tension of deposited metal
  films.[^stoney-1909]
* [Hu, *J. Appl. Phys.* 1991](<https://doi.org/10.1063/1.349282>) — stress-related problems in silicon
  technology.[^hu-1991]

## Open questions

* What SkyWater's "On board metrology" measures, which gauge provides it,
  and which polishes use it, are not stated.[^skw-01]
* Which stand-alone thickness, index, FTIR, XRF and stress gauges SkyWater
  uses is not public.
* SKY130's thickness, index and stress targets and limits, and which films
  are measured on product rather than monitor wafers, are not public.
* The model list above is incomplete: it covers the Therma-Wave,
  Prometrix/Tencor, Rudolph and Nanometrics tools for which a public
  description was found, not every film gauge of the period.

<!-- footnotes -->

[^tencor-thinfilm-1997]: Tencor Instruments, *Thin Film Measurement*
    (Prometrix UV-1250SE, UV-1270SE, UV-1050, FT-750 and SpectraMap
    SM300), product page; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033547/http://www.tencor.com:80/products/thinfilmmesaurement.html>
[^tencor-stress-1997]: Tencor Instruments, *Thin Film Stress Measurement*
    (FLX-5400, FLX-2320, FLX-2350fp and FLX-2900), product page; Wayback
    Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033500/http://www.tencor.com:80/products/thinfilmstress.html>
[^tencor-uv1270se-1996]: Tencor Instruments, *Tencor Instruments
    Introduces Next-Generation Film Measurement System with Advanced
    Automation Capabilities* (Prometrix UV-1270SE), press release,
    1996-06-06; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033849/http://www.tencor.com:80/press/uv-1270s.html>
[^kla-flx2320]: KLA-Tencor, *FLX-2320: Thin Film Stress Metrology*,
    product page; Wayback Machine capture of 2002-08-20.
    <https://web.archive.org/web/20020820125852/http://www.kla-tencor.com:80/products/metrology/FLX-2320/FLX-2320.html>
[^tw-op3260]: Therma-Wave, *The Opti-Probe 3260*, product page; Wayback
    Machine capture of 1998-12-05.
    <https://web.archive.org/web/19981205083736/http://www.thermawave.com:80/op3260.htm>
[^tw-op5000]: Therma-Wave, *Opti-Probe 5000 Product Family*, product page;
    Wayback Machine capture of 1998-12-06.
    <https://web.archive.org/web/19981206005043/http://www.thermawave.com:80/op5000.htm>
[^tw-history]: Therma-Wave, *Therma-Wave Corporate History*, web page;
    Wayback Machine capture of 2001-07-13.
    <https://web.archive.org/web/20010713111217/http://www.thermawave.com:80/aboutus/corphistory.htm>
[^rudolph-1999]: Rudolph Technologies, Inc., *1999 Annual Report*
    (including the Form 10-K for 1999); Wayback Machine capture of
    2000-08-30.
    <https://web.archive.org/web/20000830152419/http://www.rudolphtech.com:80/ir/6859Rudolph99AR.pdf>
[^nanometrics-2000]: Nanometrics Incorporated, Form 10-K for the fiscal
    year ended 2000-12-31; Wayback Machine capture of 2003-03-23.
    <https://web.archive.org/web/20030323070701/http://www.nanometrics.com:80/Downloads/10k_2000.pdf>
[^itrs-2001-met]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Metrology*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-ellipsometry]: Wikipedia, *Ellipsometry*.
    <https://en.wikipedia.org/wiki/Ellipsometry>
[^wiki-picosecond]: Wikipedia, *Picosecond ultrasonics*.
    <https://en.wikipedia.org/wiki/Picosecond_ultrasonics>
[^wiki-ftir]: Wikipedia, *Fourier-transform infrared spectroscopy*.
    <https://en.wikipedia.org/wiki/Fourier-transform_infrared_spectroscopy>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^pat-bpr-thermawave]: N. Gold, D. L. Willenborg, J. Opsal and A.
    Rosencwaig (Therma-Wave), *Method and apparatus for measuring thickness
    of thin films*, US 4,999,014 A, filed 1989-05-04, granted 1991-03-12.
    <https://patents.google.com/patent/US4999014A/en>
[^pat-maiwl-rudolph]: R. F. Spanier, R. G. Wolf, R. M. Loiterman and M. E.
    Haller (Rudolph Technologies), *Simultaneous multiple angle/multiple
    wavelength ellipsometer and method*, US 5,166,752 A, filed 1990-01-11,
    granted 1992-11-24. <https://patents.google.com/patent/US5166752A/en>
[^rosencwaig-1992]: A. Rosencwaig, J. Opsal, D. L. Willenborg, S. M. Kelso
    and J. T. Fanton, "Beam profile reflectometry: A new technique for
    dielectric film measurements", *Applied Physics Letters* **60**(11),
    1301–1303 (1992). <https://doi.org/10.1063/1.107323>
[^fanton-1993]: J. T. Fanton, J. Opsal, D. L. Willenborg, S. M. Kelso and
    A. Rosencwaig, "Multiparameter measurements of thin films using
    beam-profile reflectometry", *Journal of Applied Physics* **73**(11),
    7035–7040 (1993). <https://doi.org/10.1063/1.352421>
[^chandler-horowitz-2003]: D. Chandler-Horowitz, "Assessment of Ultra-Thin
    SiO2 Film Thickness Measurement Precision by Ellipsometry", *AIP
    Conference Proceedings* **683**, 326–330 (2003).
    <https://doi.org/10.1063/1.1622490>
[^kaiser-1991]: A. M. Kaiser, "Semiconductor thin-film optical constant
    determination and thin-film thickness measurement equipment
    correlation", *Proc. SPIE* **1464**, Integrated Circuit Metrology,
    Inspection, and Process Control V, 386 (1991).
    <https://doi.org/10.1117/12.44451>
[^semi-mf576]: SEMI MF576, *Test Method for Measurement of Insulator
    Thickness and Refractive Index on Silicon Substrates by Ellipsometry*,
    SEMI.
    <https://store-us.semi.org/products/mf057600-semi-mf576-test-method-for-measurement-of-insulator-thickness-and-refractive-index-on-silicon-substrates-by-ellipsometry>
[^stout-1989]: P. J. Stout and K. Krishnan, "A Comparison Of Multicomponent
    Quantitative Analysis Methods For The Determination Of Boron And
    Phosphorous In BPSG Films On Silicon", *Proc. SPIE* **1145**, 7th
    International Conference on Fourier Transform Spectroscopy, 494 (1989).
    <https://doi.org/10.1117/12.969563>
[^shiraiwa-1968]: T. Shiraiwa and N. Fujino, "Theoretical Formulas for Film
    Thickness Measurement by Means of Fluorescence X-Rays", *Advances in
    X-ray Analysis* **12**, 446–456 (1968).
    <https://doi.org/10.1154/S0376030800005917>
[^windover-2001]: D. Windover, "Development of an in-line X-ray
    reflectivity technique for metal film thickness measurement", *AIP
    Conference Proceedings* **550**, 243–248 (2001).
    <https://doi.org/10.1063/1.1354405>
[^thomsen-1986]: C. Thomsen, H. T. Grahn, H. J. Maris and J. Tauc,
    "Surface generation and detection of phonons by picosecond light
    pulses", *Physical Review B* **34**(6), 4129–4138 (1986).
    <https://doi.org/10.1103/PhysRevB.34.4129>
[^pat-picosecond-brown]: J. Tauc, H. J. Maris and C. Thomsen (Brown
    University Research Foundation), *Optical generator and detector of
    stress pulses*, US 4,710,030 A, filed 1985-05-17, granted 1987-12-01.
    <https://patents.google.com/patent/US4710030A/en>
[^stoner-1998]: R. J. Stoner, C. J. Morath, G. Tas, G. Antonelli and H. J.
    Maris, "Picosecond ultrasonics: A new approach for control of thin
    metal processes", *Characterization and Metrology for ULSI Technology:
    1998 International Conference*, pp. 385–394 (AIP,
    1998). <https://doi.org/10.1063/1.56821>
[^flinn-1987]: P. A. Flinn, D. S. Gardner and W. D. Nix, "Measurement and
    interpretation of stress in aluminum-based metallization as a function
    of thermal history", *IEEE Transactions on Electron Devices* **34**(3),
    689–699 (1987). <https://doi.org/10.1109/T-ED.1987.22981>
[^stoney-1909]: G. G. Stoney, "The tension of metallic films deposited by
    electrolysis", *Proceedings of the Royal Society of London A*
    **82**(553), 172–175 (1909). <https://doi.org/10.1098/rspa.1909.0021>
[^hu-1991]: S. M. Hu, "Stress-related problems in silicon technology",
    *Journal of Applied Physics* **70**(6), R53–R80 (1991).
    <https://doi.org/10.1063/1.349282>
