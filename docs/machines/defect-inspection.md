(machine-defect-inspection)=
# Defect and particle inspection

Between process steps a fab looks for what should not be on the wafer:
particles, scratches, residues, pits and pattern flaws. Two instrument
families do the searching. Unpatterned-wafer surface scanners sweep a
laser over bare or blanket-coated wafers — incoming wafers and the
monitor wafers that qualify process tools — and count the light that
defects scatter. Patterned-wafer inspectors scan product wafers and
compare each die with its neighbours, so that a difference marks a
defect. Review stations, optical or electron-beam, then revisit a sample
of the defects found and classify them. The output is a defect map
rather than a measurement, and it feeds excursion control and yield
learning. This page describes the classes, lists representative
200 mm-era models, and then says what SkyWater has published about its
own tools and which SKY130 steps this reference assigns to them. In-line
metrology in general is on the {ref}`test category page <category-test>`.

| | Defect and particle inspection |
|---|---|
| What it does | Unpatterned inspection systems "locate contaminants, particulates and surface-level defects that, if left undetected, can hamper the device manufacturing process";[^tencor-sp1-wp] a patterned-wafer inspector provides "in-line defect detection for capture of both process-induced pattern defects and contaminants".[^tencor-patterned-1997] |
| Detection principle | Laser scattering: "a laser illuminates the wafer surface, and light scattered by contaminants and other surface irregularities is collected by specially positioned collection optics and then translated into electronic signals", whose amplitude "corresponds to the size of the defect detected";[^tencor-sp1-wp] on patterned wafers, anomalies are found "by comparing adjacent repeating patterns".[^pat-inspect-kla] |
| Sensitivity | "down to 0.09 micron on well-polished silicon" (Surfscan 6220) and "down to 0.08 micron" (Surfscan SP1) on bare wafers;[^tencor-unpatterned-1997][^tencor-sp1-wp] "an optimal sensitivity of 0.15 micron" on the patterned Surfscan 7700.[^tencor-patterned-1997] |
| Throughput | "150 wph for 200mm wafers" on the SP1;[^tencor-sp1-wp] "30 full wafer inspections/hour" on the patterned Surfscan AIT.[^tencor-patterned-1997] |
| Requirement at 130 nm | ITRS 2001 sets, for 2001, a patterned-inspection sensitivity of 104 nm (polystyrene-latex sphere equivalent) at a yield-ramp scan rate of 1200 cm²/h and 130 nm at a volume-production rate of 3000 cm²/h, 70 nm on bare silicon and non-metal films, and 7 nm resolution for defect review.[^itrs-2001-yield] |
| 200 mm era | Tencor's Surfscan 6220, 6420 and SP1 unpatterned scanners and the Surfscan AIT and 7700 patterned inspectors (1997 product pages);[^tencor-unpatterned-1997][^tencor-patterned-1997] KLA-Tencor's 2351 imaging inspector, AIT XP and eV300 review SEM (2002 product pages).[^kla-2351][^kla-aitxp][^kla-ev300] |
| SkyWater-listed tool | None on the capabilities page; a job posting reads "SEM/AIT/KLA/SP1/EV300/1X"[^job-01] |
| SKY130 steps | 64 steps; see {ref}`SKY130 steps assigned to this class <machine-defect-inspection-steps>` |

## What the machine class is and how it works

Inspection tools differ from the metrology tools of the same fab in what
they return. A film gauge or a {ref}`CD-SEM <machine-cd-sem-overlay-metrology>`
reports a value at chosen sites; an inspector searches the whole wafer,
or a large part of it, and reports the position, equivalent size and
sometimes the class of every event it detects.[^tencor-sp1-wp][^itrs-2001-yield] The sections below describe
the scanners for bare and blanket wafers, the inspectors for patterned
wafers, the review stations, and how the defect data are used.

### Light scattering from bare and blanket wafers

An unpatterned-wafer scanner is a dark-field instrument: dark-field
methods "exclude the unscattered beam from the image",[^wiki-darkfield]
so that a smooth surface stays dark and a particle lights up. Tencor's
early patents describe "A scanning laser contaminant and defect detector
for reflective surfaces, having a light collector for increasing
sensitivity to scattered light",[^pat-scan-tencor] and then "A two-stage
light collector" that re-images the scattered light onto a
detector.[^pat-collector-tencor] A later KLA-Tencor patent, aimed at
inspecting "not only bare or unpatterned wafers but also rough films",
collects the light scattered from a normal and an oblique beam with a
curved mirror, compares the two signals "to distinguish between particles
and COPs" (crystal-originated particles), and uses "Butterfly-shaped
spatial filters" to restrict detection to certain azimuthal
angles.[^pat-oblique-kla] The scattered signal is converted into
a size: in Tencor's description of the Surfscan SP1, the amplitude of the
signal "corresponds to the size of the defect detected".[^tencor-sp1-wp]
Sizes are therefore equivalents, not dimensions; ITRS 2001 states its
sensitivity requirements in terms of "detecting accurately sized
Polystyrene Latex (PSL) spheres" deposited on test and calibration
wafers.[^itrs-2001-yield]

The SP1, which Tencor introduced in June 1996,[^tencor-sp1-1996] illustrates
the design choices; as Tencor's 1997 pages describe it, it used a fixed
illumination beam, so that "the wafer be moved in two dimensions: It must
be rotated and translated along a radius", with axi-symmetric collection
optics that collect scattered light "independent of the defect's
orientation on the wafer" — important for scratches, which scatter
preferentially in one direction.[^tencor-sp1-tech] An optional
bright-field channel, based on Nomarski phase contrast, found
"difficult-to-detect defects—such as mounds and dimples" by "measuring the
phase difference between two laser beams".[^tencor-sp1-tech] The same
scan measures haze, "a characteristic closely associated with surface
roughness", "down to a few parts per billion".[^tencor-sp1-wp] Haze
matters in both directions: Scheer notes that "Microroughness, or haze,
on wafer surfaces can mask the detection of particles by scanning surface
inspection systems (SSIS)".[^scheer-1996] A rough or grainy film raises
the background, which is why Tencor sold a separate scanner that "Easily
detects submicron defects on metal films and rough surfaces", and why the
ITRS table sets a coarser sensitivity for metal films (91 nm in 2001) than
for bare silicon (70 nm).[^tencor-unpatterned-1997][^itrs-2001-yield]

### Patterned-wafer inspection

On a product wafer every pattern edge scatters light, so a patterned
inspector must separate defects from the circuit. The standard approach
is comparison: KLA's photomask inspection patent describes apparatus "for
detecting differences between two dies",[^pat-photomask-kla] and a
KLA-Tencor wafer-inspection patent detects and verifies anomalies "by
comparing adjacent repeating patterns", with the surface height tracked
to keep neighbouring patterns registered.[^pat-inspect-kla] Tencor's Surfscan AIT of 1995,
"the first in the industry to provide high-speed capture of both pattern
defects and particles for in-line process monitoring", built on Tencor's
"other laser scattering tools".[^tencor-ait-1995]
KLA-Tencor's own product pages of 2002 set "High-throughput scanning for
patterned wafer inspection" (AIT XP) beside "High-resolution imaging for
patterned wafer inspection" (the 2351), and described its 23xx, AIT
and eS20 series as a strategy "that combines inspection technologies that
traditionally were isolated, such as brightfield/darkfield and
e-beam";[^kla-aitxp][^kla-2351] we read the 23xx imaging tools as the
bright-field and the AIT laser-scanning tools as the dark-field members of
that grouping, which the pages do not spell out. Orbot Instruments
patented a two-phase scheme: a fast laser scan of the whole surface, then
high-resolution examination of "only the suspected
locations".[^pat-twophase-orbot]

The case for automation was sensitivity and consistency. Radin, using a
KLA-2020 automated wafer inspector, found that operator inspections
lacked reproducibility and that "operator sensitivity declines to very low
levels for defect sizes approaching linewidths".[^radin-1988] Tencor
presented the Surfscan AIT's speed as "making inspection practical
beyond only the most critical process steps".[^tencor-ait-1995]

### Review and classification

An inspector finds more events than engineers can look at, and does not
say what they are. Review stations relocate a sample and image it at
higher resolution. Tencor's CRS laser confocal review station was
"Designed specifically for reviewing and classifying defects detected by
automatic wafer inspection systems", could "discern features as small as
0.15 micron", and made it "easy to distinguish pits from particles, and
to determine whether a defect is located under, within or on top of a
film or metal layer".[^tencor-crs-1997] KLA-Tencor's eV300 ("E-beam
defect review") "Reads defect files from inspection and optical review
systems" and "Features integrated automatic defect classification
(ADC)".[^kla-ev300] Classification was the bottleneck: Breaux and Singh
note that it "is typically a manual process limited in its effectiveness
by human factors",[^breaux-1995] and Sherman, Tirosh and Smilansky call
automated classification "one of the biggest challenges to successful
integration of automated inspection into wafer manufacturing
process".[^sherman-1993] Tencor's ADC module of 1996 "automates
post-inspection defect relocation and classification", and Tencor argued
that "This automation also enables expanded sampling plans to be adopted
without compromising wafer throughput".[^tencor-adc-1996] ITRS 2001 asks
review platforms to redetect defects down to 52 nm at 7 seconds per
defect in 2001.[^itrs-2001-yield]

### From defect maps to yield

The defect data are only useful when tied to yield. Nurani, Akella and
Strojwas built a sampling framework on "the trade-off between the cost of
inspection and the cost of yield impact of the undetected
defects";[^nurani-1996] ITRS 2001 notes that cost of ownership pushes
fabs to sparse sampling, and asks for statistically optimised
sampling.[^itrs-2001-yield] Tobin et al. describe spatial signature
analysis, "an automated wafermap analysis procedure which performs a
sophisticated defect clustering and signature classification of
electronic wafermaps".[^tobin-1997] Yield impact is commonly estimated
from kill ratios (industry practice); Ono, Iwata and Watanabe found that
such estimates become inaccurate when
"parametric faults caused low yield or a large number of non-killer
defects were included in inspection reports".[^ono-2002] Stapper's
defect-sensitivity models, used at IBM for more than fifteen years, treat
photolithographic defects of the same dimensions as the device and
interconnection patterns and are related to test sites.[^stapper-1983] Tencor's SwiftAccess system "Integrates defect data
from multiple sources throughout a fab", and its "Control charts
constructed on the SwiftAccess system can be displayed directly on the
Surfscan AIT".[^tencor-defectdata-1997]

## Representative 200 mm-era models

* **Tencor, then KLA-Tencor, unpatterned scanners.** The Surfscan 6220,
  "Designed for detecting particles, pits and scratches on bare wafers,
  wafers deposited with smooth blanket films, and for measuring haze on a
  broad range of surfaces", and the Surfscan 6420 for metal films and
  rough surfaces, "Also ideal for detecting defects on non-uniform films,
  a critical requirement for CMP applications";[^tencor-unpatterned-1997]
  the Surfscan SP1, introduced in June 1996,[^tencor-sp1-1996] for 200 mm
  and 300 mm wafers at 150 and 100 wafers per hour;[^tencor-sp1-wp] and the
  Surfscan SP1 DLS, described on a 2002 capture of KLA-Tencor's site, which
  "Continues the industry-leading SP1 TBI platform" and added a backside
  inspection module for "fully automated, non-destructive inspection of
  the backsides of patterned (product) wafers".[^kla-sp1dls-2002]
* **Laser-scanning patterned inspectors.** The Surfscan AIT (1995),
  developed with SEMATECH as an "in-line defect inspection system for
  0.25-micron technology";[^tencor-ait-1995] the Surfscan 7700, which
  detected contaminants "below 0.20 micron" on "complex process levels
  such as nitride, oxide and TEOS films";[^tencor-patterned-1997] and the
  AIT XP, described on a 2002 capture, extending "the AIT II and AIT
  III".[^kla-aitxp]
* **Imaging inspectors.** KLA's 2020, used in Radin's 1988
  defect-reduction work;[^radin-1988] the 2350 and its successor the 2351,
  for "critical-defect detection at design rules of 0.13 µm and
  smaller".[^kla-2351]
* **Review stations.** Tencor's CRS laser confocal review station, with
  the ADC module first offered on the CRS-1010;[^tencor-crs-1997][^tencor-adc-1996]
  KLA-Tencor's CRS-3000 optical review and eV300 e-beam review systems,
  listed together in 2002.[^kla-defect-2002][^kla-ev300]
* **Orbot Instruments.** Patterned-wafer inspection with a two-phase
  laser and high-resolution scheme and automatic defect
  classification.[^pat-twophase-orbot][^sherman-1993]

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page names no wafer defect
inspection tool. The nearest entries are "Reticle storage/handler/defect
inspection" under "Photo Metrology", which as written concerns reticles,
"Camtek Falcon (outgoing QA)" under "Sort", and the "FEI Dual Beam
FIB/SEM" and "Hitachi S-4800" of the "Physical Analysis"
group;[^skw-01] no step page assigns any of these to a SKY130 step. The
public evidence for SkyWater's in-line inspection tools is a *Defect
Technician 2* job posting, retrieved on 2026-08-30, which asks
for:[^job-01]

> "General operation of semiconductor defect metrology tools:
> SEM/AIT/KLA/SP1/EV300/1X"

Read term by term, on our reading: "AIT" and "SP1" match the product
names of Tencor's Surfscan AIT patterned inspector and Surfscan SP1
unpatterned scanner,[^tencor-ait-1995][^tencor-sp1-wp] and "EV300" that of
KLA-Tencor's eV300 e-beam review SEM;[^kla-ev300] "SEM" and "KLA" could
denote a review or analysis SEM and other KLA inspection tools, and "1X"
is not explained. The posting gives no models, counts or process
steps.[^job-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
posting is **medium** evidence: a SkyWater job posting, retrieved on the
date stated, which lists tool names that the posting itself does not
expand.[^job-01] The caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`; for
this class the first matters most, since a posting describes the
inspection area at the time it was written. The step pages read the
abbreviations as KLA-Tencor AIT and SP1 and grade the entry medium on
every page that names it; that reading of the abbreviations is theirs
and ours, not SkyWater's.

(machine-defect-inspection-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names defect, particle or
after-develop inspection (identical to the
{ref}`machines index <machines-index>` table):

{ref}`001 <step-001>`, {ref}`005 <step-005>`, {ref}`009 <step-009>`, {ref}`013 <step-013>`, {ref}`016 <step-016>`, {ref}`021 <step-021>`, {ref}`025 <step-025>`, {ref}`029 <step-029>`, {ref}`033 <step-033>`, {ref}`035 <step-035>`, {ref}`039 <step-039>`, {ref}`042 <step-042>`, {ref}`046 <step-046>`, {ref}`048 <step-048>`, {ref}`051 <step-051>`, {ref}`054 <step-054>`, {ref}`057 <step-057>`, {ref}`060 <step-060>`, {ref}`061 <step-061>`, {ref}`067 <step-067>`, {ref}`070 <step-070>`, {ref}`074 <step-074>`, {ref}`082 <step-082>`, {ref}`084 <step-084>`, {ref}`086 <step-086>`, {ref}`087 <step-087>`, {ref}`090 <step-090>`, {ref}`091 <step-091>`, {ref}`095 <step-095>`, {ref}`100 <step-100>`, {ref}`106 <step-106>`, {ref}`107 <step-107>`, {ref}`110 <step-110>`, {ref}`111 <step-111>`, {ref}`113 <step-113>`, {ref}`116 <step-116>`–{ref}`118 <step-118>`, {ref}`121 <step-121>`, {ref}`122 <step-122>`, {ref}`124 <step-124>`, {ref}`127 <step-127>`–{ref}`129 <step-129>`, {ref}`132 <step-132>`, {ref}`133 <step-133>`, {ref}`137 <step-137>`, {ref}`139 <step-139>`, {ref}`142 <step-142>`–{ref}`144 <step-144>`, {ref}`147 <step-147>`, {ref}`148 <step-148>`, {ref}`152 <step-152>`, {ref}`154 <step-154>`, {ref}`157 <step-157>`–{ref}`159 <step-159>`, {ref}`162 <step-162>`, {ref}`164 <step-164>`, {ref}`165 <step-165>`, {ref}`167 <step-167>`–{ref}`169 <step-169>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"SEM/AIT/KLA/SP1/EV300/1X" (read as KLA-Tencor AIT and SP1)** — *medium:* {ref}`SMAT <step-001>`, {ref}`DNIS <step-009>`, {ref}`CMPNIT <step-012>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNM <step-035>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`BFR <step-060>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`CMPM <step-116>`, {ref}`WCMP3 <step-122>`, {ref}`CMPM2 <step-127>`, {ref}`WCMP4 <step-133>`, {ref}`CMPM3 <step-142>`, {ref}`WCMP5 <step-148>`, {ref}`CMPM4 <step-157>`

The two lists differ. The grades fall on the starting-material page, the
resist strips after implants, the tunnel mask, the backside film removal
and the CMP steps; {ref}`CMPNIT <step-012>` grades the posting although
its "Machines typically used" section names thickness metrology and a
profiler rather than inspection. Most of the other pages in the list
above — the depositions, etches and implants, and the mask steps other
than {ref}`TUNM <step-035>` — do not cite the posting.

## Consumables and facilities

What is specific to inspection is summarised here; the
{ref}`materials index <materials-index>` lists monitor wafers. None of
the SkyWater sources describes the fab's inspection standards, recipes or
defect database.

* **Calibration standards.** Wafers carrying deposited polystyrene-latex
  spheres of known size, against which sensitivity is
  specified,[^itrs-2001-yield] and haze or microroughness standards such as
  the etched-feature wafers Scheer developed.[^scheer-1996]
* **Monitor wafers.** Bare or blanket-film wafers run through a process
  tool and scanned before and after; ITRS 2001 asks that non-metal-film
  and bare-silicon sensitivity be at least as good as patterned-wafer
  sensitivity "to justify monitor wafer usage".[^itrs-2001-yield]
* **Lasers and optics.** The scanners and the confocal review stations
  are laser instruments;[^tencor-sp1-tech][^tencor-crs-1997] lasers and
  detectors are service items (industry practice).
* **Review SEMs.** An electron source in a high-vacuum column with a
  wafer load lock, as on the {ref}`CD-SEMs <machine-cd-sem-overlay-metrology>`
  (industry practice).
* **Defect data systems.** Software that merges inspection and review
  results from many tools, such as SwiftAccess;[^tencor-defectdata-1997]
  KLA-Tencor described data products "that manage, correlate, and
  integrate the wealth of defect data and images" from its inspection
  tools.[^kla-sp1dls-2002]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's inspection points, sampling
plans and defect limits are not public.

* **After the implant resist strips.** The strip pages from
  {ref}`DNIS <step-009>` to {ref}`NSDIS <step-087>` name patterned or
  unpatterned inspection after ashing and cleaning; the {ref}`strip category page <category-strip>` lists laser
  surface scanners among its metrology.
* **After CMP.** The CMP pages from {ref}`CMPP <step-090>` onwards name
  unpatterned or patterned inspection. Tencor
  marketed the Surfscan 6420 for "non-uniform films, a critical
  requirement for CMP applications" and the Surfscan AIT as "Ideal for
  after-etch and post-CMP inspection levels";[^tencor-unpatterned-1997][^tencor-patterned-1997]
  ITRS 2001 notes that the buried patterns of a polished wafer let a
  grazing-angle laser inspector approximate unpatterned inspection for
  tool qualification.[^itrs-2001-yield]
* **After develop.** The mask pages name after-develop inspection, and
  {ref}`P1M <step-061>` names bright-field inspectors of the KLA-Tencor 2xxx
  class; KLA-Tencor paired the SP1 DLS with "after-develop inspection
  (ADI) for macro and micro defects" in its lithography-module
  strategy.[^kla-sp1dls-2002]
* **After depositions and fills.** The cap-oxide, passivation and
  tungsten-fill pages ({ref}`NCAPOX3 <step-117>`, {ref}`NTSD <step-167>`,
  {ref}`WDEP2 <step-110>` and their counterparts) name particle
  inspection; ITRS 2001 sets a coarser sensitivity requirement for
  inspection on metal films than on non-metal films.[^itrs-2001-yield]
* **Incoming wafers and the backside.** {ref}`SMAT <step-001>` names an
  unpatterned surface scanner for incoming wafers, described with the
  marker and sorter on the
  {ref}`starting-material page <machine-starting-material>`, and
  {ref}`BFR <step-060>` a backside inspection tool; KLA-Tencor's backside
  module, described on a 2002 capture of its SP1 DLS page, inspected the
  backsides of product wafers.[^kla-sp1dls-2002] ITRS 2001 gives backside
  particle requirements for 200 mm wafers.[^itrs-2001-yield]
* **Pads.** {ref}`PDME <step-169>` names automated pad inspection before
  test.
* **Electrical defect monitors.** Optical inspection is complemented by
  electrical structures: the public SKY130 test tile documented on the
  {ref}`HPETEST <step-171>` page includes comb and serpentine structures
  on diffusion, poly, local interconnect and metals 1–5, the kind of
  test site Stapper's defect models are related to.[^stapper-1983]

## Related pages

* {ref}`category-test` — in-line metrology and electrical test.
* {ref}`category-strip` and {ref}`category-cmp` — the strips, cleans and
  polishes after which the step pages name inspection.
* {ref}`category-substrate` — incoming wafer inspection.
* {ref}`machine-starting-material` — the incoming-wafer scanner, marker
  and sorter at SMAT.
* {ref}`machine-cd-sem-overlay-metrology` — the metrology tools of the
  lithography area.
* {ref}`machine-film-thickness-metrology` — the thickness and stress gauges run on the same monitor
  wafers.
* {ref}`machine-cross-section-sem-profilers` — sectioning and review of defects in physical analysis.
* {ref}`machine-parametric-tester` — the electrical defect structures measured at
  e-test.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.

## References

### Cross-check

* Indeed, SkyWater *Defect Technician 2* posting — the defect-metrology
  tool list "SEM/AIT/KLA/SP1/EV300/1X".[^job-01]
* SkyWater Technology, *Facilities & Capabilities* — the reticle
  inspection, outgoing-QA and physical-analysis entries; no wafer
  inspection tool.[^skw-01]
* ITRS 2001, *Yield Enhancement* — defect detection and review
  requirements, PSL calibration and sampling.[^itrs-2001-yield]
* Tencor, *Surfscan SP1* introduction press release (1996), white paper
  and technical details (1997) — the launch date, laser scattering,
  stationary-beam design, haze and
  throughput.[^tencor-sp1-1996][^tencor-sp1-wp][^tencor-sp1-tech]
* Tencor, *Unpatterned Wafer Inspection* and *Patterned Wafer Inspection*
  pages (1997) — the Surfscan 6220, 6420, AIT and
  7700.[^tencor-unpatterned-1997][^tencor-patterned-1997]
* Tencor, Surfscan AIT press release (1995) — the first high-speed
  in-line patterned inspector, developed with SEMATECH.[^tencor-ait-1995]
* Tencor, *Laser Confocal Review* page (1997) and ADC press release
  (1996) — optical review and automatic
  classification.[^tencor-crs-1997][^tencor-adc-1996]
* Tencor, *Defect Data Analysis* page (1997) — the SwiftAccess defect
  database.[^tencor-defectdata-1997]
* KLA-Tencor, *Surfscan SP1 DLS*, *AIT XP*, *2351* and *eV300* product
  pages and the *Defect Control* menu (2002) — the inspection and review
  line at the 130 nm
  node.[^kla-sp1dls-2002][^kla-aitxp][^kla-2351][^kla-ev300][^kla-defect-2002]

### High-level understanding

* Wikipedia, *Dark-field microscopy* — imaging with the unscattered beam
  excluded.[^wiki-darkfield]
* Wikipedia, *Scanning electron microscope* — the imaging behind e-beam
  review.[^wiki-sem]
* Wikipedia, *KLA Corporation* — the inspection vendor.[^wiki-kla]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — process
  monitoring in a 200 mm fab.[^txt-07]

### Deep dive

* Galbraith (Tencor), US 4,378,159 — the scanning laser contaminant and
  defect detector.[^pat-scan-tencor]
* Galbraith (Tencor), US 4,601,576 — a two-stage collector for scattered
  light.[^pat-collector-tencor]
* Levy and Sandland (KLA), US 4,247,203 — die-to-die comparison in a photomask
  inspector.[^pat-photomask-kla]
* Jordan, Nikoonahad and Wells (KLA-Tencor), US 5,864,394 — patterned-wafer
  inspection by comparing adjacent repeating patterns.[^pat-inspect-kla]
* Vaez-Iravani, Stokowski and Zhao (KLA-Tencor), US 6,201,601 — normal and
  oblique illumination with curved-mirror collection and spatial filters
  for bare wafers and rough films.[^pat-oblique-kla]
* Alumot et al. (Orbot Instruments), US 5,699,447 — two-phase optical
  inspection.[^pat-twophase-orbot]
* Radin, *Proc. SPIE* 1988 — defect reduction with an automated KLA-2020
  inspector against operator inspection.[^radin-1988]
* Sherman, Tirosh and Smilansky, *Proc. SPIE* 1993 — automatic
  classification of patterned-wafer defects.[^sherman-1993]
* Breaux and Singh, ISSM 1995 — an ADC system combining image processing
  and fuzzy logic.[^breaux-1995]
* Nurani, Akella and Strojwas, *IEEE TSM* 1996 — cost-based defect
  sampling for yield management.[^nurani-1996]
* Tobin et al., *Proc. SPIE* 1997 — spatial signature analysis of wafer
  maps.[^tobin-1997]
* Scheer, *Proc. SPIE* 1996 — a physical haze and microroughness
  standard.[^scheer-1996]
* Ono, Iwata and Watanabe, ASMC 2002 — the accuracy of kill-ratio yield
  impact.[^ono-2002]
* Stapper (IBM), *IBM J. Res. Dev.* 1983 — defect-sensitivity models and
  test sites.[^stapper-1983]

## Open questions

* What "SEM", "KLA" and "1X" denote in the posting, which AIT and SP1
  generations it means, and how many inspection tools SkyWater has, are
  not stated.[^job-01]
* Whether the "Reticle storage/handler/defect inspection" entry includes
  any wafer inspection is not stated.[^skw-01]
* At which SKY130 steps wafers are inspected, with what sampling and
  against what defect limits, is not public.
* The model list above is incomplete: it covers the Tencor, KLA-Tencor
  and Orbot tools for which a public description was found, not every
  inspection and review tool of the period.

<!-- footnotes -->

[^tencor-sp1-1996]: Tencor Instruments, *Tencor Instruments Introduces
    Revolutionary 300mm Wafer Inspection System* (Surfscan SP1), press
    release, 1996-06-17; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033839/http://www.tencor.com:80/press/SP1EMBG.html>
[^tencor-sp1-wp]: Tencor Instruments, *Surfscan SP1: New Inspection
    Technology for Unpatterned 300mm Wafers*, technology white paper, web
    page; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302034319/http://www.tencor.com:80/products/SP1WhitePaper.html>
[^tencor-sp1-tech]: Tencor Instruments, *Technical Details of the Surfscan
    SP1 Unpatterned Wafer Inspection System*, web page; Wayback Machine
    capture of 1997-03-02.
    <https://web.archive.org/web/19970302034311/http://www.tencor.com:80/products/SP1TechDetails.html>
[^tencor-unpatterned-1997]: Tencor Instruments, *Unpatterned Wafer
    Inspection* (Surfscan SP1, 6420 and 6220), product page; Wayback
    Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033400/http://www.tencor.com:80/products/uwaferinpection.html>
[^tencor-patterned-1997]: Tencor Instruments, *Patterned Wafer Inspection*
    (Surfscan AIT and 7700), product page; Wayback Machine capture of
    1997-03-02.
    <https://web.archive.org/web/19970302033408/http://www.tencor.com:80/products/pwaferinpection.html>
[^tencor-ait-1995]: Tencor Instruments, *Tencor Instruments Unveils
    Surfscan AIT Wafer Inspection System*, press release, 1995-10-23;
    Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302034359/http://www.tencor.com:80/press/surfscan.html>
[^tencor-crs-1997]: Tencor Instruments, *Laser Confocal Review* (Tencor
    CRS), product page; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033431/http://www.tencor.com:80/products/lasercreview.html>
[^tencor-adc-1996]: Tencor Instruments, *Tencor Instruments Introduces
    Automatic Defect Classification (ADC) for its Tencor CRS Laser Confocal
    Review Station*, press release, 1996-07-16; Wayback Machine capture of
    1997-03-02.
    <https://web.archive.org/web/19970302033828/http://www.tencor.com:80/press/ADCrelease.html>
[^tencor-defectdata-1997]: Tencor Instruments, *Defect Data Analysis*
    (SwiftAccess), product page; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033417/http://www.tencor.com:80/products/defectdata.html>
[^kla-sp1dls-2002]: KLA-Tencor, *Surfscan SP1 DLS: Unpatterned surface
    inspection*, product page; Wayback Machine capture of 2002-02-08.
    <https://web.archive.org/web/20020208135136/http://www.kla-tencor.com:80/products/defect_control/surfscan-sp1/surfscan.html>
[^kla-aitxp]: KLA-Tencor, *AIT XP: High-throughput scanning for patterned
    wafer inspection*, product page; Wayback Machine capture of 2002-06-04.
    <https://web.archive.org/web/20020604135033/http://www.kla-tencor.com:80/products/defect_control/aitxp/aitxp.html>
[^kla-2351]: KLA-Tencor, *2351: High-resolution imaging for patterned wafer
    inspection*, product page; Wayback Machine capture of 2002-01-31.
    <https://web.archive.org/web/20020131004355/http://www.kla-tencor.com:80/products/defect_control/2351/2351.html>
[^kla-ev300]: KLA-Tencor, *eV300: E-beam defect review*, product page;
    Wayback Machine capture of 2002-02-08.
    <https://web.archive.org/web/20020208135357/http://www.kla-tencor.com:80/products/defect_control/ev300/ev300.html>
[^kla-defect-2002]: KLA-Tencor, *Defect Control* (inspection, review and
    analysis products), product menu page; Wayback Machine capture of
    2002-06-03.
    <https://web.archive.org/web/20020603184120/http://www.kla-tencor.com:80/products/defect_control/index.html>
[^itrs-2001-yield]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Yield Enhancement*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001YieldEnhance.pdf>
[^job-01]: Indeed, *Skywater Technology Foundry Jobs, Employment in
    Bloomington, MN* (listing page; Defect Technician 2 posting), retrieved
    2026-08-30; listings expire.
    <https://www.indeed.com/q-skywater-technology-foundry-l-bloomington,-mn-jobs.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-darkfield]: Wikipedia, *Dark-field microscopy*.
    <https://en.wikipedia.org/wiki/Dark-field_microscopy>
[^wiki-sem]: Wikipedia, *Scanning electron microscope*.
    <https://en.wikipedia.org/wiki/Scanning_electron_microscope>
[^wiki-kla]: Wikipedia, *KLA Corporation*.
    <https://en.wikipedia.org/wiki/KLA_Corporation>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^pat-scan-tencor]: L. K. Galbraith (Tencor Instruments), *Scanning
    contaminant and defect detector*, US 4,378,159 A, filed 1981-03-30,
    granted 1983-03-29. <https://patents.google.com/patent/US4378159A/en>
[^pat-collector-tencor]: L. K. Galbraith (Tencor Instruments), *Light
    collector for optical contaminant and flaw detector*, US 4,601,576 A,
    filed 1983-12-09, granted 1986-07-22.
    <https://patents.google.com/patent/US4601576A/en>
[^pat-photomask-kla]: K. Levy and P. Sandland (KLA Instruments),
    *Automatic photomask inspection system and apparatus*, US 4,247,203 A,
    filed 1978-04-03, granted 1981-01-27.
    <https://patents.google.com/patent/US4247203A/en>
[^pat-inspect-kla]: J. R. Jordan III, M. Nikoonahad and K. B. Wells
    (KLA-Tencor), *Surface inspection system*, US 5,864,394 A, filed
    1995-09-29, granted 1999-01-26.
    <https://patents.google.com/patent/US5864394A/en>
[^pat-oblique-kla]: M. Vaez-Iravani, S. Stokowski and G. Zhao
    (KLA-Tencor), *Sample inspection system*, US 6,201,601 B1, filed
    1997-09-19, granted 2001-03-13.
    <https://patents.google.com/patent/US6201601B1/en>
[^pat-twophase-orbot]: D. Alumot, G. Neumann, R. Sherman and E. Tirosh
    (Orbot Instruments), *Two-phase optical inspection method and
    apparatus for defect detection*, US 5,699,447 A, filed 1991-11-12,
    granted 1997-12-16. <https://patents.google.com/patent/US5699447A/en>
[^radin-1988]: C. Radin, "A Defect Reduction Methodology For Increased
    Sort Yield Using Automated Defect Inspection", *Proc. SPIE* **0921**,
    Integrated Circuit Metrology, Inspection, and Process Control II, 224
    (1988). <https://doi.org/10.1117/12.968369>
[^sherman-1993]: R. Sherman, E. Tirosh and Z. Smilansky, "Automatic defect
    classification system for semiconductor wafers", *Proc. SPIE* **1907**,
    Machine Vision Applications in Industrial Inspection, 72–79 (1993).
    <https://doi.org/10.1117/12.144824>
[^breaux-1995]: L. Breaux and B. Singh, "Automatic defect classification
    system for patterned semiconductor wafers", *Proc. International
    Symposium on Semiconductor Manufacturing (ISSM)* 1995, pp. 68–73.
    <https://doi.org/10.1109/ISSM.1995.524362>
[^nurani-1996]: R. K. Nurani, R. Akella and A. J. Strojwas, "In-line
    defect sampling methodology in yield management: an integrated
    framework", *IEEE Transactions on Semiconductor Manufacturing*
    **9**(4), 506–517 (1996). <https://doi.org/10.1109/66.542166>
[^tobin-1997]: K. W. Tobin Jr., S. S. Gleason, T. P. Karnowski, S. L. Cohen
    and F. Lakhani, "Automatic classification of spatial signatures on
    semiconductor wafer maps", *Proc. SPIE* **3050**, Metrology,
    Inspection, and Process Control for Microlithography XI, 434 (1997).
    <https://doi.org/10.1117/12.275936>
[^scheer-1996]: B. W. Scheer, "Development of a physical haze and
    microroughness standard", *Proc. SPIE* **2862**, Flatness, Roughness,
    and Discrete Defect Characterization for Computer Disks, Wafers, and
    Flat Panel Displays, 78–95 (1996). <https://doi.org/10.1117/12.256193>
[^ono-2002]: M. Ono, H. Iwata and K. Watanabe, "Accuracy of yield impact
    calculation based on kill ratio", *13th Annual IEEE/SEMI Advanced
    Semiconductor Manufacturing Conference (ASMC 2002)*.
    <https://doi.org/10.1109/ASMC.2002.1001580>
[^stapper-1983]: C. H. Stapper, "Modeling of Integrated Circuit Defect
    Sensitivities", *IBM Journal of Research and Development* **27**(6),
    549–557 (1983). <https://doi.org/10.1147/rd.276.0549>
