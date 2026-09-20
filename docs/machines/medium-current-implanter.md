(machine-medium-current-implanter)=
# Medium-current ion implanter

A medium-current implanter is the beam-line ion implanter a fab uses for
light and moderate doses that must be placed precisely: threshold and
channel implants, punch-through and depletion implants, halos, and the
tilted tips of the higher-voltage transistors. It implants one wafer at
a time, which lets it hold a large, accurately known tilt and twist.
This page describes the class in general, lists representative
200 mm-era models, and then says what SkyWater has published about its
own tool of this class and which SKY130 steps this reference assigns to
it. The physics of implantation (ranges, channelling, damage) is on the
{ref}`category page <category-implant>`.

| | Medium-current ion implanter |
|---|---|
| What it does | Implants light to moderate doses of B⁺, BF₂⁺, As⁺ or P⁺ with a precisely set tilt and twist; one of the four implanter types — high current, medium current, high energy and ultra-high dose — into which fabs divide implant work.[^tanjyo-2011] |
| Energy | "3keV to 750keV" for the 8250HT;[^axcelis-8250] 250 keV for singly charged ions on Nissin's EXCEED3000AH, raised to 320 keV (640 keV doubly and 960 keV triply charged) on the EXCEED9600A.[^tanjyo-2011] |
| Beam current | "between 10 μA and ~2 mA" in Wikipedia's classification;[^wiki-implant] "between 4µA and 3,500µA" for the Eaton 8250HT.[^axcelis-8250] |
| Dose | Light doses, of order 10¹²–10¹³ cm⁻² for threshold and channel implants (typical);[^txt-01] Nissin's example CMOS flow runs its medium-current steps at 10¹² cm⁻².[^tanjyo-2011] |
| Wafer handling | Serial (single-wafer): the 8250HT is a "fully automated, serial-processing system" with a "mechanically limited throughput of 210 wafers per hour";[^axcelis-8250] the beam is scanned in one direction and the wafer moved in the other.[^harlan-1998][^olson-1998] |
| 200 mm era | The Eaton 8250 is "a 200mm system";[^axcelis-8250] Varian's E220 and E500 served 150 mm and 200 mm wafers;[^varian-eseries-2003] Nissin's EXCEED2000A was its 200 mm tool.[^tanjyo-2011] |
| SkyWater-listed tool | "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to 1e14, 0-60 deg tilt"[^skw-01] |
| SKY130 steps | 20 steps, plus 1 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-medium-current-implanter-steps>` |

## What the machine class is and how it works

Every beam-line implanter has the same chain of functions. Wikipedia
summarises it as an ion source with extraction electrodes, a magnet with
slits "that allow only ions with a specific value of the product of mass
and velocity/charge to continue down the beamline", "some combination
of beam scanning and wafer motion" to spread the dose, and a way of
collecting the charge of the implanted ions "so that the delivered dose
can be measured in a continuous fashion".[^wiki-implant] Nissin
describes its medium-current EXCEED line as "an ion source, analyzer
magnet, acceleration tube, energy filter magnet (FEM), beam sweep magnet
(BSM), collimator magnet (COL), and end station".[^tanjyo-2011] What
makes a machine *medium-current* is the balance struck along that
chain: enough beam for light and moderate doses at a useful
throughput, with the energy purity, beam parallelism and angle control
that low-dose, tilt-sensitive implants need. Glavish and Farley review
how beam lines of all classes developed to meet these
demands.[^glavish-2018]

### Ion source and extraction

The source is an arc chamber in which a plasma is struck in a dopant
gas — boron trifluoride, arsine or phosphine — between tungsten
electrodes; ions are drawn out through a slit by an extraction
electrode.[^wiki-implant] The classic design is the Bernas source, whose
filament is exposed to the plasma; in an indirectly heated cathode
(IHC) source "a plate cathode positions between the plasma and the
filament so that the filament is not exposed directly to the
plasma".[^tanjyo-2011] Horsky's IHC source has "several times the
lifetime of commercial Bernas sources which incorporate a bare filament
cathode", with doubly charged fractions of "15% for phosphorus, and 2%
for boron".[^horsky-1998-ihc] The Eaton 8250 uses "an extended life ion
source using an indirectly heated cathode for longer source life and
higher multiple charged beam currents".[^harlan-1998] Multiply charged
ions matter to this class because they reach two or three times the
singly charged energy on the same accelerating voltage: Nissin's
EXCEED9600A reaches 320 keV with singly, 640 keV with doubly and
960 keV with triply charged ions.[^tanjyo-2011]

### Mass analysis, acceleration and energy filtering

The analysing magnet selects one ion species and charge state, and the
ions are then accelerated towards the wafer;[^wiki-implant] the 8250HT
works "in either deceleration or acceleration mode".[^axcelis-8250]
Collisions "with residual gas particles in the vicinity of the
accelerating tube" create ions of the wrong energy,[^tanjyo-2011] so a
medium-current beam line is built to remove them: "In medium current
ion implanters there is also a neutral ion trap before the process
chamber".[^wiki-implant] The Eaton 8250HT's
"Angular Energy Filter (AEF) … deflects the beam by 15 degrees and
eliminates contamination before it reaches the wafer",[^axcelis-8250]
and Nissin introduced "the world's first energy filtering function" on
its EXCEED2000 in 1994.[^tanjyo-2011] Kubo et al. measured why this
matters: with multiply charged phosphorus the low-energy contamination
"reaches 12% of the P⁺⁺ dose for a beam current of 400 pμA" and falls
to 5% at 200 pμA.[^kubo-1996]

### Beam scanning and wafer motion

"The beam can be scanned across the wafer magnetically,
electrostatically, mechanically or with a combination of these
techniques."[^wiki-implant] Two late-1990s medium-current designs show
the hybrid approach. The Eaton 8250 sweeps the beam with an
electrostatic scanner and "a novel electrostatic scan angle correction
lens to produce parallel beams", with "beam parallelism better than
+/-0.2 degrees at the wafer", and moves the wafer mechanically in the
other direction.[^harlan-1998] Varian's VIISta 810 uses "an
electrostatic deflector operating at 1 kHz", "a 45° angle corrector
magnet" to make the beam parallel, and "a mechanical scan of the wafer"
for the vertical direction.[^olson-1998] Nissin scans magnetically and
parallelises with a collimator magnet.[^tanjyo-2011] Parallelism is
not cosmetic: Rathmell et al. show that where channelling is possible
the depth profile "can vary significantly … even with beam angle
variations as small as ±0.5 degrees".[^rathmell-1998]

### Dosimetry

The dose is "the integral over time of the ion current", collected so
that it "can be measured in a continuous fashion and the implant process
stopped at the desired dose level".[^wiki-implant] The current is read
on a Faraday cup, and ions striking the cup knock out electrons: "Escape
of secondary and tertiary electrons from the Faraday cup body … causes a
measurement error", so a suppression electrode is placed at the cup's
entrance — "By negatively charging the electrostatic suppression
electrode, the escape of electrons from the Faraday cup is inhibited",
as a Varian patent describes the established approach, to which it adds
magnetic suppression.[^pat-faraday-varian] In the 8250,
"dosimetry is based on robust measurements of beam flux at the plane of
the wafer";[^harlan-1998] the EXCEED line measures the scanned beam on
Faraday arrays in front of and behind the wafer position and iterates
the scan waveform until the dose profile is uniform.[^tanjyo-2011]
Collisions with residual gas neutralise ions or strip them to a higher
charge state, which "can lead to dosing errors",[^curello-1998] and
resist outgassing "can alter the real-time measurements of implanted
dose".[^horsky-1998] Curello and McWilliams raised the
chamber pressure of an 8250 deliberately and found "a negligible effect
on Vt … for pressures up to 1E-5 Torr" for low-dose BF₂⁺, but charge
exchange "already occurs at pressure of 5E-6 Torr" for higher-dose
B⁺.[^curello-1998]

### Charge neutralisation

A positive ion beam charges the wafer, and as beam currents rose "fatal
damage may be caused to ICs due to the electrical
charge-up".[^tanjyo-2011] Implanters therefore supply electrons to the
beam near the wafer; Current et al. model the charge-control systems in
use, "dense and dilute plasma flows, electron showers".[^current-1996-iit]
Nissin's 200 mm EXCEED2000AH uses "a filament-type plasma flood gun
(PFG)" and its 300 mm EXCEED2300H an RF-type PFG; to keep the plasma
electrons from charging the device negatively, "the electron energy must
be less than 3 eV", corresponding to the breakdown voltage of gate oxides
of 1 nm or less, and the RF type "can supply such low energy electrons
by magnetic filtering".[^tanjyo-2011] Eaton, whose history calls charge
control one of the bigger process challenges of the era because gate
oxides were "very sensitive to charge breakdown", introduced a "back biased
Secondary Electron Flood (SEF)" in 1996.[^axcelis-history]

### End station, tilt and twist

The end station moves wafers by robot from cassettes through load locks
onto a platen,[^tanjyo-2011] clamps them (the 8250 has "an
electrostatic clamp"[^harlan-1998]) and tilts and rotates the platen. Serial end
stations reached large angles early: Eaton's NV-6200AV of 1990 offered
"rotation during processing and multiple tilt angles from 0 to 60
degrees",[^axcelis-history] and the 8250HT is described as a "high-tilt,
medium-current ion implanter" whose "HT" refers to its "improved
capabilities for high throughput in high-tilt implants".[^axcelis-8250] Nissin's later end stations measure
the wafer notch with a camera and hold tilt and twist by "feedback
control at an accuracy of ±0.1 degrees".[^tanjyo-2011]

## Representative 200 mm-era models

* **Eaton / Axcelis.** The NV-6200AV (1990), the 8200P ("featuring
  innovative parallel scanning beam", 1996), the 8250 (presented at IIT
  1998[^harlan-1998]) and the NV-8250HT (2000), and the MC3 for 300 mm
  (1998).[^axcelis-history] Eaton
  describes the 8250 as "a 200mm system that provides enhanced yield and
  serial processing advantages to users for high-tilt, medium-current
  implants and indium implants".[^axcelis-8250] Eaton spun the business
  off as Axcelis Technologies in 2000.[^wiki-axcelis]
* **Varian.** The E-series — E220 and E500 and their HP, EHP and EHPi
  versions — described by Varian as its "E-series medium current
  implanter" line for "150mm and 200mm" wafers;[^varian-eseries-2003]
  Swenson et al. describe metals-contamination and ion-source work on
  the EHP-220/500.[^swenson-1996][^swenson-1996-bernas] The VIISta 810
  followed as a "200 mm/300 mm serial medium current ion
  implanter".[^olson-1998] Varian Semiconductor was acquired by Applied
  Materials in 2011.[^wiki-varian]
* **Nissin Ion Equipment.** The NH20-SP and then the EXCEED series: the
  EXCEED2000 (1994) and EXCEED2000A (1998) for 200 mm, followed by
  300 mm models; Nissin states it has "held about 30% share" of the
  medium-current market "since 2004".[^tanjyo-2011]

The {ref}`category page <category-implant>` lists the same families;
Current's review sets them in the history of implantation for silicon
devices.[^current-2017]

## At SkyWater

### What SkyWater lists

Under "Ion Implant", in its "Diffusion, Anneal & Implant" group,
SkyWater's *Facilities & Capabilities* page lists one medium-current
tool:[^skw-01]

> "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to
> 1e14, 0-60 deg tilt"

Read term by term: the species are ¹¹B⁺, BF₂⁺ and As⁺, with no
phosphorus; the dose range is 10¹¹–10¹⁴ cm⁻²; the tilt range is 0–60°.
We read "ESC chuck" as an electrostatic chuck, which Harlan and Petry
describe on the 8250,[^harlan-1998] and "E shower" as an electron shower
for charge control, a term the charging literature
uses;[^current-1996-iit] SkyWater does not expand either abbreviation.
The entry gives no energy range and does not say whether the tool is an
8250 or an 8250HT; the "3keV to 750keV" that the step pages quote is
Eaton's figure for the 8250HT,[^axcelis-8250] not a SkyWater statement.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
this listing is **strong**: it is a SkyWater statement.[^skw-01] The
caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. For
this class it is also the only SkyWater source that names a tool: the
implanter in the maintenance-technician profile could be any of the
three listed.

(machine-medium-current-implanter-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a medium-current
implanter as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`LVTNI <step-015>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`2PSDI <step-083>`; *alternative:* {ref}`NWI <step-018>`

How the step pages grade the SkyWater tool for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Axcelis 8250 Mid current …"** — *inference:* {ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`UPRI <step-056>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`2PSDI <step-083>`; *not stated which of two:* {ref}`PRI <step-053>`; *weak:* {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`ASTI <step-065>`; *strong for existence; unlikely, no phosphorus:* {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`; *named only as below the required dose:* {ref}`P1I <step-050>`, {ref}`PSDI <step-082>`, {ref}`NSDI <step-086>`
* **Either GSD entry instead** — *weak (which entry would serve not
  stated):* {ref}`LVTNI <step-015>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`; see
  {ref}`machine-high-current-implanter` and
  {ref}`machine-high-energy-implanter`.

The inferences rest on the listed capability: the 8250 entry is the only
implanter entry with a stated tilt range, and the only one whose dose
range stops at "1e14".[^skw-01]

## Consumables and facilities

The dopant sources are described on the
{ref}`dopant gases and implant sources <material-dopant-sources>` page.
The dopant gases and the ion-source parts of an implanter are listed in
the {ref}`materials index <materials-index>`; what is specific to a
medium-current tool is summarised here. None of the SkyWater sources
describes the fab's gas delivery or abatement. Monitor wafers are
described on the {ref}`substrates and test wafers <material-substrates>`
page.

* **Source gases.** Boron trifluoride for B⁺ and BF₂⁺, arsine and
  phosphine for As⁺ and P⁺.[^wiki-implant] Phosphine is "a highly toxic
  respiratory poison",[^wiki-ph3] and arsine for implanters "can be
  provided by a sub-atmospheric gas source", adsorbed on "a solid
  microporous adsorbent inside a gas cylinder".[^wiki-ash3] The ATMI
  patent behind such sources records the earlier practice of dilute
  (10–15 %) hydride mixtures "in either 0.44 L or 2.3 L cylinders at
  pressures of 400-1800 psig", and that switching from arsenic to
  phosphorus "on an implanter with solid sources can take as long as 90
  minutes" against "5-15 minutes with gas sources".[^pat-sds-atmi] A used
  1995 Varian E500 HP "Medium Current Implanter" listed for sale has
  "PH3 - SDS II, AsH3 - SDS II, BF3 - SDS" bottles in its gas box, with
  argon.[^fabsurplus-e500] Boron trifluoride is "applied as dopant in
  ion implantation".[^wiki-bf3]
  The SkyWater entry has no phosphorus.[^skw-01]
* **Ion-source parts.** Filaments or indirectly heated cathodes, arc
  chambers, reflectors and extraction electrodes are worn by the plasma;
  Wikipedia gives source lives of "often … 300 hours",[^wiki-implant]
  Horsky IHC cathode lives "from 70 h at the highest discharge power
  levels to over 500 h for moderate operation",[^horsky-1998-ihc] and
  Swenson et al. lowered arc voltages on the EHP-500 "to reduce sputter
  erosion of the filament".[^swenson-1996-bernas] The E500 listing
  specifies a "Type II Bernas ion source w/ tungsten arc
  chamber".[^fabsurplus-e500]
* **Beam-line liners.** Graphite and silicon-coated shields line the
  surfaces the beam strikes, to keep sputtered metals off the wafer:
  Swenson et al. added "graphite and Si-coated shields" to the
  EHP-220/500 beam line,[^swenson-1996] and Nissin fits "graphite shields
  … of high purity and less-particle generation".[^tanjyo-2011]
* **Vacuum.** Turbomolecular and dry pumps on the source and beam line
  and cryopumps on the end station and load locks (the E500 listing
  names CTI cryopumps, Pfeiffer turbopumps and Edwards dry
  pumps).[^fabsurplus-e500] Cryopumps collect hydrogen and dopant
  hydrides, and Current lists the "management of potentially explosive
  gas mixtures during regeneration of cryopumps" among implanter vacuum
  issues;[^current-1996] residues of arsenic and phosphorus are met in
  "vacuum pump hardware" during servicing.[^wiki-implant]
* **Monitor wafers.** Bare wafers for {ref}`thermal-wave and sheet-resistance
  checks <machine-sheet-resistance-metrology>` of dose and uniformity.[^smith-1985]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's implant energies and doses are
not public.

* **Large tilts and rotations.** The PDK records an "Angle for HV tip
  implant" of 40° and a "Twist angle for HV Tip" of 23°,[^pdk-03] and the
  {ref}`HVASTI <step-069>` page reads the implant as split into rotations
  so that source and drain are symmetric,[^pat-quad-tsmc] with the
  resist and neighbouring gates shadowing the beam.[^chen-1995] The
  {ref}`BHI <step-066>` and {ref}`LDBHI <step-073>` halo pages describe
  the same geometry. The step pages assign these implants to the 8250 as
  an inference because its "0-60 deg tilt" is the only tilt range
  SkyWater states.[^skw-01] A serial end station is what makes such
  angles routine;[^axcelis-history] its accuracy is a machine property,
  held to ±0.1° on Nissin's later tools.[^tanjyo-2011]
* **Beam angle and channelling in threshold implants.** The
  threshold and channel implants ({ref}`LVTNI <step-015>`,
  {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`,
  {ref}`NCHI <step-045>`) are shallow and light, so a small change of
  beam angle alters the channelled tail and the thermal-wave or
  sheet-resistance reading;[^rathmell-1998] the step pages name
  thermal-wave monitors for them, the method Smith et al.
  introduced.[^smith-1985]
* **Energy purity and dose at low dose.** Energy contamination from
  charge exchange is worst with multiply charged ions and resist
  outgassing,[^kubo-1996] and neutralisation can bias the Faraday
  reading;[^curello-1998] both are reasons for the energy filters and
  pressure control of this class. The {ref}`NWI <step-018>` page names a
  medium-current tool with doubly charged phosphorus as a way to reach
  the lower end of the well energies,[^pat-umc-dc] but the SkyWater
  entry lists no phosphorus.[^skw-01]
* **Charging.** The implants run through resist; the
  {ref}`HVASTI <step-069>` page infers that the "E shower" and "ESC
  chuck" of the SkyWater entry are used even with its thin resist.
  Electron-shower and plasma-flood charge control is the mechanism
  Current et al. model.[^current-1996-iit]
* **The dose ceiling decides several assignments.** The
  {ref}`PRI <step-053>`, {ref}`ASTI <step-065>` and
  {ref}`LDASTI <step-072>` pages choose between the 8250 and a GSD
  implanter according to a dose that is not public, because the 8250
  entry stops at "1e14" and the "Hi dose" entry starts at
  "5e12".[^skw-01] The {ref}`P1I <step-050>`, {ref}`PSDI <step-082>` and
  {ref}`NSDI <step-086>` pages set the 8250 aside for the same reason.
* **Wells on a medium-current or a high-energy tool.** The
  {ref}`NWI2 <step-019>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`,
  {ref}`PWDEI1 <step-031>` and {ref}`PWDEI2 <step-032>` pages offer both
  classes, depending on energy. Morris and Rubin's comparison of the two
  for multiple well implants found that batch high-energy implanters
  "have a lower total capital cost, footprint, and cost per wafer out
  than serial medium current implanters".[^morris-2000]

## Related pages

* {ref}`category-implant` — implantation physics and the 25 implant
  steps of SKY130.
* {ref}`machine-high-current-implanter` and
  {ref}`machine-high-energy-implanter` — the other two implanter
  classes and SkyWater's two GSD entries.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — dopant gases, ion-source parts and their
  hazards.
* {ref}`category-strip` — removal of the implant resist after each
  implant.
* {ref}`material-substrates` — monitor wafers for dose and uniformity.
* {ref}`material-dopant-sources` — dopant gases, solid sources,
  sub-atmospheric packages and ion-source parts.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Multiple tilted angle ion implantation MOSFET method <patent-gp22246938>` — US 5,372,957 A (1993)
* {ref}`Use of double charge implant to improve retrograde process PMOS punch through voltage <patent-gp22834355>` — US 5,393,679 A (1994)
* {ref}`Storage and delivery system for gaseous hydride, halide, and organometallic group V compounds <patent-gp23253952>` — US 5,518,528 A (1994)
* {ref}`Faraday system for ion implanters <patent-gp26926543>` — US 6,723,998 B2 (2000)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "Axcelis 8250
  Mid current" entry quoted on this page.[^skw-01]
* SkyWater PDK Authors, *Criteria & Assumptions* — the HV tip tilt and
  twist angles.[^pdk-03]
* Eaton, *8250HT Medium Current Ion Implanter* — energy, beam-current,
  throughput and energy-filter figures for the 8250 family.[^axcelis-8250]
* Axcelis Technologies, *Our History* — dates and features of the
  Eaton medium-current tools and of the SEF charge control.[^axcelis-history]
* Varian Semiconductor, *Productivity Plus* for the E220/E500 series
  (2003) — the E-series as Varian's 150/200 mm medium-current
  line.[^varian-eseries-2003]
* Fabsurplus, Varian E500 HP listing — the gas box, source and pumps of
  a medium-current tool of the period.[^fabsurplus-e500]
* Tom and McManus (ATMI), US 5,518,528 — sub-atmospheric hydride
  storage for implanters, with the cylinder practice it
  replaced.[^pat-sds-atmi]
* Bisson et al. (Varian), US 6,723,998 — Faraday cups for implanters and
  the suppression of secondary electrons.[^pat-faraday-varian]

### High-level understanding

* Wikipedia, *Ion implantation* — implanter classes, ion sources, beam
  scanning and hazards.[^wiki-implant]
* Wikipedia, *Axcelis Technologies* and *Varian Semiconductor* — the
  two main US medium-current vendors.[^wiki-axcelis][^wiki-varian]
* Wikipedia, *Boron trifluoride*, *Phosphine* and *Arsine* — the source
  gases.[^wiki-bf3][^wiki-ph3][^wiki-ash3]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — implantation
  and implanter basics in ch. 8.[^txt-01]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — the
  implanter as a fab tool, ch. 17.[^txt-07]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapter-per-process equipment detail.[^txt-09]

### Deep dive

* Harlan and Petry, IIT 1998 — the Eaton 8250: hybrid scanning,
  parallelising lens, IHC source, electrostatic clamp and
  dosimetry.[^harlan-1998]
* Rathmell et al., IIT 1998 — measuring beam parallelism on the 8250
  and its effect on channelled profiles.[^rathmell-1998]
* Curello and McWilliams, IIT 1998 — charge exchange and dose error
  versus chamber pressure on an 8250.[^curello-1998]
* Olson, Renau and Buff, IIT 1998 — electrostatic scanning, angle
  correction and uniformity control on the VIISta 810.[^olson-1998]
* Swenson et al., IIT 1996 — graphite and silicon shields to cut metals
  contamination on the EHP-220/500.[^swenson-1996]
* Swenson et al., IIT 1996 — the enhanced Bernas source of the EHP-500
  and multiply charged beam currents.[^swenson-1996-bernas]
* Kubo et al., IIT 1996 — energy contamination from multiply charged
  implants and its device effect.[^kubo-1996]
* Horsky, *Rev. Sci. Instrum.* 1998 — the indirectly heated cathode ion
  source, lifetime and charge-state fractions.[^horsky-1998-ihc]
* Tanjyo and Naito, *SEI Technical Review* 2011 — the Nissin EXCEED
  line: energy filter, magnetic scan, Faraday arrays, plasma flood and
  angle control.[^tanjyo-2011]
* Glavish and Farley, IIT 2018 — a review of beam-line innovations
  across implanter classes.[^glavish-2018]
* Current, *JVST A* 1996 — sources, beam transport, dosimetry,
  charging and cryopump safety from a vacuum
  perspective.[^current-1996]
* Current, Vella and Lukaszek, IIT 1996 — a beam-plasma model of wafer
  charging covering electron showers and plasma
  flows.[^current-1996-iit]
* Current, *Mater. Sci. Semicond. Process.* 2017 — implantation for
  silicon devices, past to future.[^current-2017]
* Horsky, IIT 1998 — how resist outgassing alters the measured dose
  and the gas load in high-energy and high-current
  implanters.[^horsky-1998]
* Smith, Rosencwaig and Willenborg, *APL* 1985 — the thermal-wave
  implant monitor.[^smith-1985]
* Morris and Rubin, IIT 2000 — batch high-energy versus serial
  medium-current implanters for well implants.[^morris-2000]
* Lin, Yoo and Liang (TSMC), US 5,372,957 — multiple tilted implants
  with wafer rotation.[^pat-quad-tsmc]
* Yang (UMC), US 5,393,679 — doubly charged phosphorus for a retrograde
  well on a lower-energy tool.[^pat-umc-dc]
* Chen et al., *Solid-State Electronics* 1995 — beam shadowing of large-tilt
  implants.[^chen-1995]
* Ryssel and Ruge, *Ion Implantation* — the classic monograph, including
  equipment.[^ryssel-1986]

## Open questions

* Whether SkyWater's "Axcelis 8250" is an 8250 or an 8250HT, and its
  energy range, are not stated.[^skw-01]
* What "E shower" denotes on the tool (an electron shower, a plasma
  flood or another charge-control system) is not stated.
* The model list above is incomplete: it covers the Eaton/Axcelis,
  Varian and Nissin tools for which a public description was found, not
  every medium-current implanter of the period.

<!-- footnotes -->

[^tanjyo-2011]: M. Tanjyo and M. Naito, "History of Ion Implanter and
    Its Future Perspective", *SEI Technical Review* No. 73, October 2011,
    pp. 22–30. <https://global-sei.com/technology/tr/bn73/pdf/73-03.pdf>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^axcelis-8250]: Semiconductor Online, *8250HT Medium Current Ion
    Implanter* (Eaton Semiconductor Equipment Operations product
    description).
    <https://www.semiconductoronline.com/doc/8250ht-medium-current-ion-implanter-0001>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^harlan-1998]: J. M. Harlan and K. Petry, "Overview of the Eaton 8250
    medium current implanter", *Proc. 1998 International Conference on
    Ion Implantation Technology*, vol. 1, pp. 266–269.
    <https://doi.org/10.1109/IIT.1999.812103>
[^olson-1998]: J. C. Olson, A. Renau and J. Buff, "Scanned beam
    uniformity control in the VIISta 810 ion implanter", *Proc. 1998
    International Conference on Ion Implantation Technology*, vol. 1,
    pp. 169–172. <https://doi.org/10.1109/IIT.1999.812079>
[^varian-eseries-2003]: Varian Semiconductor Equipment Associates,
    *Productivity Plus Option / Upgrade, E220 / E500 Series Implanter*,
    presentation, July 2003, hosted by the AVS Northern California
    Chapter user groups.
    <https://nccavs-usergroups.avs.org/wp-content/uploads/JTG2003/WCJTG_07_2003_Varian.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; implanter entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^glavish-2018]: H. Glavish and M. Farley, "Review of Major Innovations
    in Beam Line Design", *2018 22nd International Conference on Ion
    Implantation Technology (IIT)*, pp. 9–18.
    <https://doi.org/10.1109/IIT.2018.8807986>
[^horsky-1998-ihc]: T. N. Horsky, "Indirectly heated cathode arc
    discharge source for ion implantation of semiconductors", *Review of
    Scientific Instruments* **69**(4), 1688–1690 (1998).
    <https://doi.org/10.1063/1.1148866>
[^kubo-1996]: T. Kubo, T. Hisaeda, T. Miyake, T. Ishigaki, M. Kase, K.
    Watanabe and T. Fukuda, "Energy contamination from multiple-charged
    ion implantation in conventional implanter", *Proc. 11th
    International Conference on Ion Implantation Technology* (1996),
    pp. 100–103. <https://doi.org/10.1109/IIT.1996.586141>
[^rathmell-1998]: R. D. Rathmell, D. E. Kamenitsa, M. L. King and A. M.
    Ray, "Beam parallelism in the 8250 medium current implanter", *Proc.
    1998 International Conference on Ion Implantation Technology*, vol.
    1, pp. 392–395. <https://doi.org/10.1109/IIT.1999.812136>
[^curello-1998]: G. Curello and T. McWilliams, "Charge exchange in
    Eaton's NV-8250 medium current ion implanter", *Proc. 1998
    International Conference on Ion Implantation Technology*, vol. 1,
    pp. 543–545. <https://doi.org/10.1109/IIT.1999.812173>
[^current-1996-iit]: M. I. Current, M. Vella and W. Lukaszek,
    "Beam-plasma concepts for wafer charging control during ion
    implantation", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 53–56.
    <https://doi.org/10.1109/IIT.1996.586119>
[^axcelis-history]: Axcelis Technologies, *Our History* ("45 Years of
    Innovation"), company web page, accessed 2026-09-13.
    <https://www.axcelis.com/about/our-history/>
[^wiki-axcelis]: Wikipedia, *Axcelis Technologies*.
    <https://en.wikipedia.org/wiki/Axcelis_Technologies>
[^swenson-1996]: D. R. Swenson, D. F. Downey, S. R. Walther, A. Renau,
    G. Gammel and M. E. Mack, "Metals-contamination-reduction program for
    the Varian EHP-220/500 medium-current ion implanter", *Proc. 11th
    International Conference on Ion Implantation Technology* (1996),
    pp. 139–142. <https://doi.org/10.1109/IIT.1996.586154>
[^swenson-1996-bernas]: D. R. Swenson, A. Renau, S. R. Walther and M. E.
    Mack, "Enhanced Bernas ion source for the Varian EHP-500
    medium-current ion implanter", *Proc. 11th International Conference
    on Ion Implantation Technology* (1996), pp. 283–286.
    <https://doi.org/10.1109/IIT.1996.586263>
[^wiki-varian]: Wikipedia, *Varian Semiconductor*.
    <https://en.wikipedia.org/wiki/Varian_Semiconductor>
[^current-2017]: M. I. Current, "Ion implantation of advanced silicon
    devices: Past, present and future", *Materials Science in
    Semiconductor Processing* **62**, 13–22 (2017).
    <https://doi.org/10.1016/j.mssp.2016.10.045>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^pat-sds-atmi]: G. M. Tom and J. V. McManus (Advanced Technology
    Materials), *Storage and delivery system for gaseous hydride, halide,
    and organometallic group V compounds*, US 5,518,528 A, granted
    1996-05-21. <https://patents.google.com/patent/US5518528A/en>
[^pat-faraday-varian]: J. Bisson, Z. Zhao, G. Gammel, D. Alvarado and
    C. Walker (Varian Semiconductor Equipment Associates), *Faraday system
    for ion implanters*, US 6,723,998 B2, granted 2004-04-20.
    <https://patents.google.com/patent/US6723998B2/en>
[^fabsurplus-e500]: Fabsurplus (SDI), *Varian E500 HP Medium Current
    Implanter* (used-equipment specification sheet, item 44950),
    accessed 2026-09-13.
    <https://www.fabsurplus.com/sdicatalog/download?id=44950>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^smith-1985]: W. L. Smith, A. Rosencwaig and D. L. Willenborg, "Ion
    implant monitoring with thermal wave technology", *Applied Physics
    Letters* **47**(6), 584–586 (1985).
    <https://doi.org/10.1063/1.96079>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pat-quad-tsmc]: M.-S. Lin, C.-S. Yoo and M.-S. Liang (Taiwan
    Semiconductor Manufacturing Company), *Multiple tilted angle ion
    implantation MOSFET method*, US 5,372,957 A, granted 1994-12-13.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5372957>
[^chen-1995]: H.-S. Chen, C.-S. Teng, L. Moberly and R. Lahri, "Ion beam
    shadowing effect in submicrometer large-angle-tilt implanted drain
    (LATID) MOSFETs", *Solid-State Electronics* **38**(7), 1321–1323
    (1995). <https://doi.org/10.1016/0038-1101(94)00256-F>
[^pat-umc-dc]: S.-H. Yang (United Microelectronics), *Use of double
    charge implant to improve retrograde process PMOS punch through
    voltage*, US 5,393,679 A, granted 1995-02-28.
    <https://patents.google.com/patent/US5393679A/en>
[^morris-2000]: W. Morris and L. Rubin, "Technical and economic
    considerations for retrograde well and channel implants", *Proc.
    2000 International Conference on Ion Implantation Technology*, pp.
    73–76. <https://doi.org/10.1109/IIT.2000.924093>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007, ISBN
    978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^ryssel-1986]: H. Ryssel and I. Ruge, *Ion Implantation*, Wiley, 1986,
    ISBN 978-0-471-10311-0. <https://openlibrary.org/isbn/9780471103110>
