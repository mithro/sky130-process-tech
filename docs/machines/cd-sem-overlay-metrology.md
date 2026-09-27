(machine-cd-sem-overlay-metrology)=
# CD-SEM and overlay metrology

After every mask step a sample of wafers is measured before the pattern
is etched or implanted. A critical-dimension scanning electron
microscope (CD-SEM) measures the width of lines and holes in the
developed resist, and an optical overlay tool measures how far the new
pattern sits from the level beneath it. The same CD-SEMs measure the
etched features again after etch.

| | CD-SEM and overlay metrology |
|---|---|
| What it does | CD-SEMs measure line width and hole diameter; an overlay tool measures multilayer registration.[^hitachi-2011][^kla-5200xp] See *CD-SEM column* and *Overlay tools*. |
| CD-SEM beam | Low-energy electrons, "non-invasive measurements that did not require preparatory steps";[^hitachi-2011] 0.4–1.5 kV, Schottky source on the 8100XP.[^gce-kla8100] |
| CD-SEM resolution and repeatability | 3 nm resolution and 3 nm repeatability on the S-9200 (1998); 15 nm and 15 nm on the S-6000 (1984).[^hitachi-2011] 4 nm resolution on the KLA-Tencor 8100XP.[^gce-kla8100] |
| Overlay measurement | Optical box-in-box imaging on a KLA-Tencor 5200XP; see *Overlay tools* for the reseller's quotes.[^classone-kla5200xp] |
| Throughput | "45 (automatic operation)" wafers per hour, 8-inch, at five points, S-9200;[^hitachi-2011] 50 wafers per hour, 8-inch, 8100XP;[^gce-kla8100] "a 30 percent increase in throughput over previous generation tools" (Archer 10).[^kla-archer10] |
| Requirement at 130 nm | ITRS 2001 sets overlay at 46 nm for 2001 and CD control (3σ) at 7.3 nm for ASIC/low-power logic, and calls the "20% measurement precision to process tolerance metric" "somewhat relaxed".[^itrs-03] |
| 200 mm era | Hitachi S-8820 (1994), S-9200 (1998);[^hitachi-2011] Opal's earlier 7830-series, acquired by Applied Materials in 1997;[^amat-1997] Applied VeraSEM (1999);[^amat-verasem-1999] KLA-Tencor 5200XP, "0.18 micron technology".[^kla-5200xp] |
| SkyWater-listed tool | "AMAT Verity (multiple versions) CD", "AMAT VeraSEM", "KLA 5200/5300/Archer overlay"[^skw-01] |
| SKY130 steps | Overlay at all 36 mask steps and CD-SEM at 54 steps; see {ref}`SKY130 steps assigned to this class <machine-cd-sem-overlay-metrology-steps>` |

:::{seealso}
CD and overlay control in general are on the {ref}`category page <category-lithography>`.
:::

## What the machine class is and how it works

Both tools sample: a few wafers per lot, a few fields per wafer and a
few sites per field, located by pattern recognition and measured by a
recipe. What sets them apart from the {ref}`defect inspectors <machine-defect-inspection>` in the same area
is that they return numbers — a width, an x and y offset — rather than a
defect map, and that those numbers go straight into process control.
The {ref}`category page <category-lithography>` gives the resolution
and overlay background; the sections below describe the instruments.

The measurements decide whether a lot goes on or is stripped and
reworked, and are fed back to the exposure tool as dose, focus and
alignment corrections. Fabs buy the two classes from partly different
vendors but run them together in the lithography area.

### CD-SEM column and low-voltage imaging

A CD-SEM is built to "measure properties of wafer circuit patterns such
as line width and hole diameter".[^hitachi-2011] A scanning electron microscope scans a focused beam over the sample and
builds an image from the electrons it knocks out; secondary electrons
"have very low energies on the order of 50 eV" and "can only escape from
the top few nanometers of the surface".[^wiki-sem] A CD-SEM is such a
microscope rebuilt as a production gauge.

**Hitachi's design aims.** Hitachi, whose S-6000 was
"commercialized in 1984", describes the design aims:[^hitachi-2011]

* **In-lens detection** — "in-lens detection systems which do not cast a
  pattern shadow that could affect the measurement".
* **XY stage** — "a fast and precise XY stage".
* **Low-energy beams** — "low-energy electron beams" for measurements
  without preparation.
* **Image memory** — a field-emission gun with image memory so that it
  "was able to be used without a dark room".
* **Simple recipes** — recipes "that anyone could use".

**Why low voltage.** Low voltage matters
because resist and oxide are insulators that charge under the beam:
Singh and Arnold describe low-voltage SEM as "a nondestructive method to
acquire precise linewidth measurements from features too small for
optical systems".[^singh-1988] Applied Materials' VeritySEM of 2004
reached "less than 1.8nm resolution at ultra low voltages
(200eV)".[^amat-veritysem-2004]

### Edge detection and accuracy

A CD-SEM does not see edges; it sees a line profile of signal and places
the edges on it by an algorithm. Singh and Arnold describe the usual
method: "a threshold is selected to determine the distance between the
edges of the video profile at that threshold".[^singh-1988] It is a
technique "critically sensitive to various SEM parameters including the
primary electron energy, the beam diameter, and the defocus of the
beam".[^singh-1988]

**Choice of algorithm.** Rosenfield's 1986 paper is likewise understood to have distinguished
which edge-detection method suits an isolated resist line versus an
isolated space, though this could not be independently re-checked
(evidence weak).[^rosenfield-1986] Postek,
Keery and Larrabee showed why width
is harder than pitch: edge location errors cancel in a pitch
measurement, but "in linewidth measurement applications, the effects of
edge location uncertainty are additive and thus give twice the edge
detection error to the measured width".[^postek-1988]

**Validating the algorithm.** Monte Carlo models
of beam–sample interaction are used to relate the profile to the true
edge.[^lowney-1995] Solecky, Mayer and Archie tuned CD algorithms
against AFM and electrical test, noting that CD-SEMs' "combination of
throughput, resolution, precision, ability to measure any feature of
interest and automation has been unmatched".[^solecky-2002]

**Beam damage.** The beam
also changes some samples: You, Bok and Shin saw acrylate-type ArF
resist lines shrink by 30 % after 30 measurements,[^you-2002] a problem
reported for a 193 nm acrylate resist, not for the i-line and KrF
resists the step pages read for SKY130.

### Precision, calibration and matching

A gauge is only useful if its precision is small against the tolerance
it checks; ITRS 2001 uses a "20% measurement precision to process
tolerance metric" and notes that "Precision includes measurement tool
variation from short- and long-term tool variation as well as
tool-to-tool matching".[^itrs-03]

**Calibration.** Magnification is calibrated on pitch
standards: Hitachi developed a "standard microscale with a 240-nm pitch"
and later a 100 nm one.[^hitachi-2011]

**Matching.** Several CD-SEMs on one line must
agree: Applied advertised "excellent system matching, with shared
library and database capabilities" on the VeraSEM,[^amat-verasem-1999]
and Marschner et al. extended in-fab matching methods to tools in fabs on
different continents.[^marschner-2006]

### Overlay tools

An overlay tool is an automated optical microscope; it
"performs fully automated overlay measurements on multilayer integrated
circuit product and test wafers".[^kla-5200xp] The classic target
is box-in-box: an outer box printed at the reference level and an inner
box at the current level, whose offset in x and y is the misregistration
at that site.

**Box-in-box optics.** A reseller describes the KLA-Tencor 5200XP as a
"Fully Automated Non-Contact Box-In-Box Measurement" system using
"Proven Coherence Probe Microscopy (CPM) Technology".[^classone-kla5200xp]
It also has "KLASS (KLA
Stepper Set-up Software) which allows the calculation of critical
parameters for overlay control on lithography tools".[^classone-kla5200xp]
KLA-Tencor's own page gave the 5200XP "coherence probe measurement
capability which is optimized for planarized layers".[^kla-5200xp]
Coherence probe microscopy builds a three-dimensional image with a
Linnik interferometer and broadband illumination;[^dockrey-1989] Plambeck,
Knoll and Lord applied it to overlay targets made hard to read by
chemical-mechanical polishing.[^plambeck-1995]

**Reseller's fuller description.** The same reseller listing also
describes the 5200XP as a "Fully Automated Non-Contact Box-In-Box
Measurement for Overlay Registration (stepper alignment)" using
"Coherence Probe Microscopy (CPM)".[^classone-kla5200xp]

**Tool-induced shift.** The tool itself can shift
the result. Starikov proposed "tool-induced shift (TIS)" as "a simple
measure of tool-related inaccuracy".[^starikov-1992] He had seen overlay
inaccuracies "on the order of 100 nm" from tools and
marks.[^starikov-1992] Hoshi et
al. describe how modern tools control "critical asymmetries in the
imaging optics" and compensate the rest "through
TIS-calibration".[^hoshi-2002]

Targets far larger than the circuit can
also misreport the overlay of fine features under lens
aberration.[^chu-1999] Den Boef reviews the optical alignment, levelling
and overlay sensors of lithography as one family.[^den-boef-2016]

### From measurement to correction

The numbers go back to the exposure tool. KLA-Tencor's Archer 10, as its
product page described it in 2003, "Automatically transfers overlay test
data to the ASML PAS 5500™ series stepper", and its analysis software
gives "analysis results for wafer lot dispositioning, stepper
correction, and problem troubleshooting".[^kla-archer10]

**Recipe load in a foundry.** In a foundry
the recipe load is heavy: DeMoor et al. describe ASIC fabs with
"thousands or even tens of thousands of reticles active at any one
time", where "each individual reticle will require independent recipes
for stepper exposure, and the subsequent misregistration and critical
dimension metrology steps".[^demoor-2000] They used an off-line recipe
database across several overlay tools.[^demoor-2000]

## Representative 200 mm-era models

:::{table} Representative CD-SEM and overlay tools of the 200 mm era (figures as each source gives them)
:widths: 20 14 8 12 46

| Vendor | Model | Year | Type | Published figures |
|---|---|---:|---|---|
| Hitachi | S-6000 | 1984 | CD-SEM | 15 nm resolution, 15 nm repeatability, "8 (manual operation)" wafers per hour[^hitachi-2011] |
| Hitachi | S-8820 | 1994 | CD-SEM | 5 nm resolution, 5 nm repeatability, 20 wafers per hour[^hitachi-2011] |
| Hitachi | S-9200 | 1998 | CD-SEM | 3 nm resolution, 3 nm repeatability, 45 wafers per hour on 8-inch wafers[^hitachi-2011] |
| Hitachi | S-9300 | 1999 | CD-SEM | "ready in time for the shift to 300-mm wafers"[^hitachi-2011] |
| Opal / Applied Materials | 7830Si | 1997 | CD-SEM | "Building on the proven technology of the earlier 7830-series systems"[^amat-1997] |
| Applied Materials | VeraSEM | 1999 | CD-SEM | "designed to handle both 200mm and 300mm wafer sizes"[^amat-verasem-1999] |
| Applied Materials | VeritySEM | 2004 | CD-SEM | 65–45 nm, "less than 5 angstrom precision"[^amat-veritysem-2004] |
| KLA-Tencor | 8100XP | — | CD-SEM | 0.4–1.5 kV, 4 nm resolution[^gce-kla8100] |
| KLA-Tencor | 5200XP | — | overlay | for 0.18 µm[^kla-5200xp] |
| KLA-Tencor | Archer 10 | — | overlay | (2003 capture) "for 300 mm manufacturing at the sub-0.13-micron node";[^kla-archer10] listed in the product menu by 2001[^kla-5200xp] |
| KLA-Tencor | Archer 300 LCM | 2010 | overlay | succeeding "the widely-adopted Archer 200"[^kla-archer300-2010] |
:::

Applied Materials acquired Opal, "a supplier of CD-SEM (Critical
Dimension-Scanning Electron Microscope) systems", in January 1997, and
introduced the 7830Si that year, building on the earlier
7830-series.[^amat-1997] The VeraSEM added "Process Variation Monitoring"
measurements such as "line edge roughness, line edge width variation,
and distinguishing open/closed contact holes".[^amat-verasem-1999]

## At SkyWater

### What SkyWater lists

Under "Photo Metrology", SkyWater's *Facilities & Capabilities* page
lists:[^skw-01]

> "AMAT Verity (multiple versions) CD"
>
> "AMAT VeraSEM"
>
> "KLA 5200/5300/Archer overlay"
>
> "Reticle storage/handler/defect inspection"
>
> "Advanced Process Control (APC) feed forward and backwards"

The "Lithography" group above it ends its exposure-tool list with
"Overlay down to single digit nm", and the "Physical Analysis" group
lists a "Hitachi S-4800" SEM ({ref}`machine-cross-section-sem-profilers`).[^skw-01]
This reference reads "KLA 5200/5300/Archer" as shorthand for the third
entry below.

:::{table} How this reference reads the Photo Metrology entries
:widths: 30 46 24

| Entry as listed | What it names | Status |
|---|---|---|
| "AMAT Verity (multiple versions) CD" | Applied Materials' VeritySEM CD-SEM line ("AMAT Verity"), in unstated versions[^amat-veritysem-2004] | our reading |
| "AMAT VeraSEM" | the CD-SEM Applied introduced in 1999[^amat-verasem-1999] | — |
| "KLA 5200/5300/Archer overlay" | KLA-Tencor optical overlay tools of the 5200, 5300 and Archer lines; the 5200XP and Archer 10 have public descriptions,[^kla-5200xp][^kla-archer10] no 5300 description was retrieved | our reading |
| "Reticle storage/handler/defect inspection" | — | — |
| "Advanced Process Control (APC) feed forward and backwards" | — | — |
:::

SkyWater gives no tool counts, and does not say whether
"Overlay down to single digit nm" is a measurement or an exposure
capability, nor which tools the APC line connects. No step page assigns
the S-4800, the reticle inspection or the APC entry to a SKY130 step.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the listings are **strong**: they are SkyWater
statements.[^skw-01] The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.
The step pages grade them "strong for existence" and treat their use at
a given mask as an inference, since the list names no step; the
machines index records that grade on nearly every mask page. The
VeritySEM press release dates that product to 2004, after the 130 nm
generation,[^amat-veritysem-2004] which fits the caveat that the list
shows today's floor, not the tools that first ran S8.

(machine-cd-sem-overlay-metrology-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names overlay metrology
or a CD-SEM (identical to the {ref}`machines index <machines-index>`
table):

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{dropdown} All 48 steps as one line of links (checked against the index)

*overlay:* all 36 mask steps; *CD-SEM:* {ref}`FOM <step-004>`–{ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`TUNARCE <step-036>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`P1ME <step-062>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LICM1E <step-094>`, {ref}`LI1M <step-102>`, {ref}`LI1ME <step-103>`, {ref}`CTM1 <step-107>`, {ref}`CTME <step-108>`, {ref}`MM1 <step-113>`, {ref}`MM1E <step-114>`, {ref}`VIM <step-118>`, {ref}`VIME <step-119>`, {ref}`MM2 <step-124>`, {ref}`MM2E <step-125>`, {ref}`VIM2 <step-129>`, {ref}`VIM2E <step-130>`, {ref}`CAPM <step-137>`–{ref}`MM3E <step-140>`, {ref}`VIM3 <step-144>`, {ref}`VIM3E <step-145>`, {ref}`CAP2M <step-152>`–{ref}`MM4E <step-155>`, {ref}`VIM4 <step-159>`, {ref}`VIM4E <step-160>`, {ref}`MM5 <step-162>`, {ref}`MM5E <step-163>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`
:::
<!-- step-tables:end -->

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"AMAT Verity (multiple versions) CD", "AMAT VeraSEM"** — *strong for existence (SkyWater statement); use at this mask is an inference:* {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`; *strong for existence; that the gate level is measured on them is an inference:* {ref}`P1M <step-061>`; *strong for existence (SkyWater statement); use after this etch is an inference:* {ref}`P1ME <step-062>`; *strong for existence:* {ref}`NSM <step-165>`, {ref}`PDM <step-168>`
* **"KLA 5200/5300/Archer overlay"** — *strong for existence (SkyWater statement); use at this mask is an inference:* {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`; *strong for existence; that the gate level is measured on them is an inference:* {ref}`P1M <step-061>`; *strong for existence:* {ref}`NSM <step-165>`, {ref}`PDM <step-168>`

The CD-SEM list includes the etch steps whose pages measure CD after
etch. The coarse implant masks name a CD-SEM only "for periodic checks"
({ref}`DNM <step-007>`, {ref}`NWM <step-017>`), and the first mask,
{ref}`FOM <step-004>`, has no earlier level to overlay, so its page notes
that overlay "is measured only from the second layer onwards".

## Consumables and facilities

What is specific to CD and overlay metrology is summarised here; the
{ref}`materials index <materials-index>` lists reference and monitor
wafers. None of the SkyWater sources describes the fab's metrology
standards or recipe management. Reference and monitor wafers are
described on the {ref}`substrates and test wafers <material-substrates>`
page.

* **Electron source and vacuum.** A field-emission electron gun (the
  8100XP lists a "Schottky Electron source"[^gce-kla8100]) in a
  high-vacuum column with a wafer load lock (industry practice).
* **Calibration standards.** Pitch standards for magnification, such as
  Hitachi's 240 nm and 100 nm pitch microscales,[^hitachi-2011] and
  reference wafers for tool matching.[^marschner-2006]
* **Targets in the scribe line.** Overlay and CD targets printed on every
  level; DeMoor et al. note the "limited real estate available in scribe
  lines" and the case for standard pattern-recognition
  structures.[^demoor-2000]
* **Recipes and data.** One recipe per reticle and level, and a link to
  the exposure tools' correction software.[^demoor-2000][^kla-archer10]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's CD targets, overlay budgets and
sampling plans are not public.

* **Overlay at every level, CD where it matters.** The step pages name
  overlay metrology at all 36 masks and a CD-SEM at every mask and at the
  isolation-nitride, trench, tunnel-mask ARC, gate, local-interconnect,
  contact, via, metal and capacitor etches.

  For scale, ITRS 2001 put the
  overlay requirement at 46 nm in the year it set the DRAM half-pitch at
  130 nm.[^itrs-03]
* **Mixed exposure classes.** The i-line and KrF levels
  ({ref}`machine-i-line-stepper`, {ref}`machine-duv-krf-stepper`) share
  one overlay entry in SkyWater's list, which does not say whether
  separate tools serve the two classes.

  Where a level is printed on a
  different tool from its reference, the tool corrections the
  measurements feed back must cover matched-machine errors (inference
  from the exposure-tool specifications on those pages). SkyWater lists
  APC "feed forward and backwards" without saying where it is
  applied.[^skw-01]
* **Planarised levels.** On this reference's readings SKY130 polishes
  its trench fill, pre-metal dielectric, tungsten plugs and inter-level
  oxides ({ref}`category-cmp`), and Plambeck, Knoll and Lord note that
  "planarized metrology targets can cause overlay measurements to be
  inaccurate as well as imprecise"; the coherence-probe option of the
  5200XP was "optimized for planarized
  layers".[^plambeck-1995][^kla-5200xp]
* **After develop and after etch.** Measuring the gate at
  {ref}`P1M <step-061>` and again after {ref}`P1ME <step-062>` gives the
  etch bias the category page describes; how well the two agree depends on
  the CD algorithm.[^solecky-2002]
* **Many reticle sets.** The process-steps sheet heads each MPW run's
  columns with its own identifier, which the public renders site calls
  the run's reticle set ({ref}`masks-mpw-reticle-sets`), so every set needs its own exposure and
  metrology recipes in the way DeMoor et al. describe for
  ASIC fabs (inference).[^demoor-2000]
* **Rework.** In a fab of this kind a lot that fails CD or overlay is
  stripped and re-exposed before etch (industry practice) ({ref}`category-lithography`); the
  {ref}`coat/develop track <machine-coat-develop-track>` runs the rework.

## Related pages

* **Category.** {ref}`category-lithography` — CD and overlay control,
  etch bias and rework. {ref}`category-etch` — the etches measured after
  etch.
* **Machines.** {ref}`machine-i-line-stepper` and
  {ref}`machine-duv-krf-stepper` — the exposure tools the measurements
  correct. {ref}`machine-coat-develop-track` — the track whose output is
  measured.
* **Materials.** {ref}`material-substrates` — reference and monitor
  wafers.
* **Indexes.** {ref}`machines-index` — all machine classes, SkyWater's
  listed tools and the step assignments. {ref}`masks-index` — the 36
  masks and their minimum CDs.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

**Related patents.**

* {ref}`Method and apparatus for obtaining two- or three-dimensional information from scanning electron microscopy <patent-gp25539026>` — US 6,054,710 A (1997)

**Related papers.**

* {ref}`paper-conway-2020a` — Tim Conway, ASMC 2020 (affiliation inference)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the "Photo
  Metrology" entries and the overlay line of the lithography
  group.[^skw-01]
* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — overlay and CD control requirements and the
  metrology precision metric.[^itrs-03]
* [Hitachi, *Hitachi Review* 2011](<https://www.hitachihyoron.com/rev/pdf/2011/r2011_05_104.pdf>) — the S-6000 to CG4000 CD-SEMs, their
  design aims, resolution, repeatability and throughput.[^hitachi-2011]
* [Applied Materials, 1997 annual report](<https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>) — the acquisition of Opal and its
  7830-series CD-SEMs.[^amat-1997]
* [Applied Materials, VeraSEM press release (1999)](<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-cd-sem-system-sub-015-micron/>) — a 200/300 mm CD-SEM
  with process-variation measurements.[^amat-verasem-1999]
* [Applied Materials, VeritySEM press release (2004)](<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-shatters-metrology-roadblocks-65-45nm>) — resolution and
  precision of the Verity line.[^amat-veritysem-2004]
* [KLA-Tencor, *5200XP Overlay Metrology System* (2001 capture)](<https://web.archive.org/web/20010807104430/http://www.kla-tencor.com:80/products/semicon_process_para_ctrl/overlay/5200xp-overlay-met_sys.html>) — the
  overlay tool for 0.18 µm with coherence probe
  measurement.[^kla-5200xp]
* [KLA-Tencor, *Archer 10* (2003 capture)](<https://web.archive.org/web/20030219061753/http://www.kla-tencor.com:80/products/archer10/archer10.html>) — automated optical overlay with
  data transfer to the stepper.[^kla-archer10]
* [KLA-Tencor, Archer 300 LCM press release (2010)](<https://ir.kla.com/news-events/press-releases/detail/269/kla-tencor-launches-the-archertm-300-lcm-overlay>) — the later Archer
  line.[^kla-archer300-2010]
* [ClassOne Equipment, *KLA-Tencor 5200XP* listing](<https://www.classoneequipment.com/KLA-Tencor-5200XP-Overlay-Registration-System>) — box-in-box CPM overlay
  and stepper set-up software.[^classone-kla5200xp]
* [GCE Market, *KLA-Tencor 8100XP CD-SEM*](<https://www.gcemarket.com/equipment/kla-tencor-8100-cd-sem-d2c9j>) — voltage, resolution and
  throughput of a CD-SEM of the period.[^gce-kla8100]

### High-level understanding

* [Wikipedia, *Scanning electron microscope*](<https://en.wikipedia.org/wiki/Scanning_electron_microscope>) — secondary-electron imaging,
  electron sources and charging.[^wiki-sem]
* [Wikipedia, *Critical dimension*](<https://en.wikipedia.org/wiki/Critical_dimension>).[^wiki-cd]
* [Wikipedia, *KLA Corporation*](<https://en.wikipedia.org/wiki/KLA_Corporation>) — the overlay and CD-SEM
  vendor.[^wiki-kla]
* [Levinson, *Principles of Lithography*, 4th ed.](<https://doi.org/10.1117/3.2525393>) — overlay and metrology
  in the lithography process.[^levinson-2019]
* [Postek, *Proc. SPIE* 1994](<https://doi.org/10.1117/12.187461>) — a review of SEM metrology for integrated
  circuits.[^postek-1994]

### Deep dive

* [Rosenfield, EMSA 1986](<https://doi.org/10.1017/S0424820100144681>) — linewidth measurement with the low-voltage SEM
  and the choice of edge algorithm.[^rosenfield-1986]
* [Singh and Arnold, *Proc. SPIE* 1988](<https://doi.org/10.1117/12.968347>) — low-voltage SEM linewidths against
  physical and electrical widths.[^singh-1988]
* [Postek, Keery and Larrabee, *Scanning* 1988](<https://doi.org/10.1002/sca.4950100104>) — accelerating voltage,
  detection mode and edge-location error.[^postek-1988]
* [Lowney, *Scanning* 1995](<https://doi.org/10.1002/sca.4950170503>) — Monte Carlo modelling for SEM linewidth
  measurement.[^lowney-1995]
* [Solecky, Mayer and Archie, *Proc. SPIE* 2002](<https://doi.org/10.1117/12.473486>) — CD-SEM correlation to AFM
  and electrical test at gate develop and etch.[^solecky-2002]
* [You, Bok and Shin, *Proc. SPIE* 2002](<https://doi.org/10.1117/12.473516>) — electron-beam shrinkage of ArF
  resist during CD measurement.[^you-2002]
* [Marschner et al., ASMC 2006](<https://doi.org/10.1109/ASMC.2006.1638758>) — CD-SEM matching between fabs.[^marschner-2006]
* [Starikov, *Opt. Eng.* 1992](<https://doi.org/10.1117/12.56172>) — accuracy of overlay measurement and
  tool-induced shift.[^starikov-1992]
* [Hoshi et al., *Proc. SPIE* 2002](<https://doi.org/10.1117/12.473514>) — tool- and wafer-induced shift on an
  overlay tool.[^hoshi-2002]
* [Dockrey and Hendricks, *Proc. SPIE* 1989](<https://doi.org/10.1117/12.953086>) — coherence probe microscopy
  for submicron linewidths.[^dockrey-1989]
* [Plambeck, Knoll and Lord, *Proc. SPIE* 1995](<https://doi.org/10.1117/12.209213>) — coherence probe overlay
  measurement on CMP-planarised targets.[^plambeck-1995]
* [Chu, Hsu and Hwang, *Proc. SPIE* 1999](<https://doi.org/10.1117/12.350790>) — fine overlay targets and lens
  distortion.[^chu-1999]
* [DeMoor et al., *Yield Management Solutions* 2000](<https://web.archive.org/web/20040228101521/http://www.kla-tencor.com:80/company/magazine/summer00/enhancing_overlay.pdf>) — off-line overlay
  recipe management in a high-volume ASIC fab.[^demoor-2000]
* [Den Boef, *Surf. Topogr.* 2016](<https://doi.org/10.1088/2051-672X/4/2/023001>) — optical alignment, level and
  scatterometry sensors for CD and overlay control.[^den-boef-2016]

## Open questions

* How many CD-SEMs and overlay tools SkyWater has, which "versions" of
  Verity it means, and what the "5300" is, are not stated.[^skw-01]
* Whether "Overlay down to single digit nm" describes measurement,
  exposure or both, and which tools the APC entry links, are not
  stated.[^skw-01]
* SKY130's sampling plans, CD and overlay specifications and whether CD
  is measured after every etch are not public.
* The model list above is incomplete: it covers the Hitachi, Opal/Applied
  Materials and KLA-Tencor tools for which a public description was
  found, not every CD-SEM and overlay tool of the period.

<!-- footnotes -->

[^hitachi-2011]: T. Ikegami, A. Yamaguchi, M. Tanaka, S. Takami, Y. Hojo
    and A. Sugimoto, "Evolution and Future of Critical Dimension
    Measurement System for Semiconductor Processes", *Hitachi Review*
    **60**(5), 203–209 (2011), accessed 2026-09-13.
    <https://www.hitachihyoron.com/rev/pdf/2011/r2011_05_104.pdf>
[^kla-5200xp]: KLA-Tencor, *5200XP Overlay Metrology System*, product
    page; Wayback Machine capture of 2001-08-07.
    <https://web.archive.org/web/20010807104430/http://www.kla-tencor.com:80/products/semicon_process_para_ctrl/overlay/5200xp-overlay-met_sys.html>
[^gce-kla8100]: GCE Market, *KLA-Tencor 8100XP CD-SEM* (specification
    summary), retrieved 2026-09-13.
    <https://www.gcemarket.com/equipment/kla-tencor-8100-cd-sem-d2c9j>
    (formerly
    <https://www.gcemarket.com/gce/gce.nsf/products/kla-tencor-8100xp-cd-sem-7expup>,
    which now redirects there)
[^classone-kla5200xp]: ClassOne Equipment, *KLA-Tencor 5200XP Overlay
    Registration System* (refurbished-equipment listing), accessed
    2026-09-13.
    <https://www.classoneequipment.com/KLA-Tencor-5200XP-Overlay-Registration-System>
[^kla-archer10]: KLA-Tencor, *Archer 10: Automated Optical Overlay
    Metrology*, product page; Wayback Machine capture of 2003-02-19.
    <https://web.archive.org/web/20030219061753/http://www.kla-tencor.com:80/products/archer10/archer10.html>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^amat-verasem-1999]: Applied Materials, *Applied Materials Introduces New
    CD-SEM System for Sub-0.15 Micron Metrology* (VeraSEM), press release,
    1999-02-01, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-cd-sem-system-sub-015-micron/>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; photo metrology entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-sem]: Wikipedia, *Scanning electron microscope*.
    <https://en.wikipedia.org/wiki/Scanning_electron_microscope>
[^singh-1988]: B. Singh and W. H. Arnold, "Linewidth measurement by low
    voltage SEM", *Proc. SPIE* **0921**, 16 (1988).
    <https://doi.org/10.1117/12.968347>
[^amat-veritysem-2004]: Applied Materials, *Applied Materials Shatters
    Metrology Roadblocks for 65-45nm Production with Applied VeritySEM
    System*, press release, 2004-02-23, accessed 2026-09-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-shatters-metrology-roadblocks-65-45nm>
[^rosenfield-1986]: M. G. Rosenfield, "Linewidth measurement using the low
    voltage SEM", *Proceedings, Annual Meeting, Electron Microscopy
    Society of America* **44**, 652–653 (1986). The DOI resolves (a
    redirect to Cambridge Core) but the destination returns HTTP 400
    (checked 2026-09-19); no Wayback Machine copy exists. Retrieved
    2026-08-30, no longer online, not archived; evidence weak.
    <https://doi.org/10.1017/S0424820100144681>
[^postek-1988]: M. T. Postek, W. J. Keery and R. D. Larrabee, "The
    relationship between accelerating voltage and electron detection modes
    to linewidth measurement in an SEM", *Scanning* **10**(1), 10–18
    (1988). <https://doi.org/10.1002/sca.4950100104>
[^lowney-1995]: J. R. Lowney, "Use of Monte Carlo modeling for
    interpreting scanning electron microscope linewidth measurements",
    *Scanning* **17**(5), 281–286 (1995).
    <https://doi.org/10.1002/sca.4950170503>
[^solecky-2002]: E. P. Solecky, J. Mayer and C. N. Archie, "Improving
    sub-150-nm lithography and etch CD-SEM correlations to AFM and
    electrical test", *Proc. SPIE* **4689**, 473 (2002).
    <https://doi.org/10.1117/12.473486>
[^you-2002]: T.-J. You, C.-K. Bok and K.-S. Shin, "CD metrology for
    avoiding shrinkage of ArF resist patterns in 100 nm ArF lithography",
    *Proc. SPIE* **4689**, 724 (2002). <https://doi.org/10.1117/12.473516>
[^marschner-2006]: T. Marschner, U. Kramer, K. Muehlstaedt, A. Navarra, J.
    Moffitt, C. Stief, S. Ventola, D. Gscheidlen, U. Groh and T. Burroughs,
    "Challenges and Methodology of Fab-to-fab CD-SEM Matching", *17th
    Annual SEMI/IEEE Advanced Semiconductor Manufacturing Conference (ASMC
    2006)*, pp. 228–232. <https://doi.org/10.1109/ASMC.2006.1638758>
[^dockrey-1989]: J. W. Dockrey and D. Hendricks, "The application of
    coherence probe microscopy for submicron critical dimension linewidth
    measurement", *Proc. SPIE* **1087**, 120 (1989).
    <https://doi.org/10.1117/12.953086>
[^plambeck-1995]: B. F. Plambeck, N. Knoll and P. J. Lord,
    "Characterization of chemical-mechanical polished overlay targets using
    coherence probe microscopy", *Proc. SPIE* **2439**, 298 (1995).
    <https://doi.org/10.1117/12.209213>
[^starikov-1992]: A. Starikov, "Accuracy of overlay measurements: tool
    and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
    (1992). <https://doi.org/10.1117/12.56172>
[^hoshi-2002]: K. Hoshi, E. Kawamura, H. Morohoshi, H. Ina, T. Fujimura,
    H. Kurita and J. L. Seligson, "TIS-WIS interaction characterization on
    overlay measurement tool", *Proc. SPIE* **4689**, 715 (2002).
    <https://doi.org/10.1117/12.473514>
[^chu-1999]: R. Chu, C. Hsu and T. Hwang, "Characterizing lens distortion
    to overlay accuracy by using fine measurement pattern", *Proc. SPIE*
    **3677**, 83 (1999). <https://doi.org/10.1117/12.350790>
[^den-boef-2016]: A. J. den Boef, "Optical wafer metrology sensors for
    process-robust CD and overlay control in semiconductor device
    manufacturing", *Surface Topography: Metrology and Properties*
    **4**(2), 023001 (2016). <https://doi.org/10.1088/2051-672X/4/2/023001>
[^demoor-2000]: S. J. DeMoor, S. Hilbun, G. P. Beck III, K. L. Bushman,
    R. D. Fields, R. M. Peters and T. E. Calvert, "Enhancing Overlay
    Metrology Productivity and Stability Using an Off-line Recipe Database
    Manager", *Yield Management Solutions* (KLA-Tencor), Summer 2000,
    pp. 44–48; Wayback Machine capture of 2004-02-28.
    <https://web.archive.org/web/20040228101521/http://www.kla-tencor.com:80/company/magazine/summer00/enhancing_overlay.pdf>
[^kla-archer300-2010]: KLA-Tencor, *KLA-Tencor Launches the Archer(TM) 300
    LCM Overlay Metrology System*, press release, 2010-06-22, accessed
    2026-09-13.
    <https://ir.kla.com/news-events/press-releases/detail/269/kla-tencor-launches-the-archertm-300-lcm-overlay>
[^wiki-cd]: Wikipedia, *Critical dimension*.
    <https://en.wikipedia.org/wiki/Critical_dimension>
[^wiki-kla]: Wikipedia, *KLA Corporation*.
    <https://en.wikipedia.org/wiki/KLA_Corporation>
[^levinson-2019]: H. J. Levinson, *Principles of Lithography*, 4th ed.,
    SPIE Press, 2019, ISBN 978-1-5106-2760-4.
    <https://doi.org/10.1117/3.2525393>
[^postek-1994]: M. T. Postek, "Scanning electron microscope metrology",
    *Proc. SPIE* **10274**, 1027405 (1994).
    <https://doi.org/10.1117/12.187461>
