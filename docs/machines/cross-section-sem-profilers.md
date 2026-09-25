(machine-cross-section-sem-profilers)=
# Cross-section SEM and profilers

Some questions about a structure cannot be answered from above. How deep
is the trench, is the gap between two lines filled without a void, does
the tungsten reach the bottom of the via, how steep is the etched
sidewall? For these a wafer, or a piece of one, is cleaved, polished or
milled with an ion beam through the feature, and the exposed face is
imaged in a scanning electron microscope. Other questions concern the
surface itself — the step height left by a polish, the dishing of a wide
field, the recess of a tungsten plug — and a stylus profiler or an atomic
force microscope (AFM) answers them by drawing a fine tip across the
wafer. Cross-sections are destructive and slow, and are usually run on
monitor or sacrificial wafers; profilers are non-destructive and can run
in line. This page describes the classes, lists representative
200 mm-era models, and then says what SkyWater has published and which
SKY130 steps this reference assigns to the class. Etch profiles and
planarisation are on the {ref}`etch <category-etch>` and
{ref}`CMP <category-cmp>` category pages.

| | Cross-section SEM and profilers |
|---|---|
| What it does | SEM provides "at-line and inline imaging for characterization of cross-sectional samples, particle and defect analysis";[^itrs-2001-met] a stylus profiler measures "step heights, planarity and roughness" (Dektak).[^veeco-stylus-2000] |
| Sample preparation | Cleaving along crystal planes and polishing, or automated microcleaving "positioned with submicron accuracy through the targeted feature";[^sela-2001] a focused ion beam that "can section submicron features" on 8-inch wafers (FIB 800).[^fei-fib800-1999] |
| SEM resolution | "1.0nm at 15kV", "2.0nm at 1kV" and "1.4nm at 1kV with Beam Deceleration", for specimens of "200mm diameter" (Hitachi S-4800).[^hitachi-s4800] |
| Profiler performance | "guaranteed 8Å step height repeatability", scans "up to 205mm" and a stylus force "as small as 0.05 mg" (HRP-200);[^tencor-hrp200-1996] "7.5Å (1[σ]) or 0.1% repeatability" (P-15).[^kla-p15] |
| AFM | "a lateral resolution of 30 Å and a vertical resolution less than 1 Å" in the first atomic force microscope;[^binnig-1986] "The first fully automated AFM designed exclusively for in-fab semiconductor metrology" for wafers to 200 mm (Dimension 9000).[^veeco-afm-2000] |
| 200 mm era | FEI's FIB 200xP and FIB 800 workstations (1999 product pages) and later DualBeam FIB/SEM families;[^fei-fib200xp-1999][^fei-fib800-1999][^fei-dualbeam-2006] Hitachi field-emission SEMs;[^hitachi-s4800] SELA microcleaving systems;[^sela-2001] Tencor P-series and HRP-200 profilers;[^tencor-profiling-1997] Veeco Dektak profilers and Digital Instruments Dimension AFMs.[^veeco-stylus-2000][^veeco-afm-2000] |
| SkyWater-listed tool | None assigned by a step page; the physical-analysis list includes "FEI Dual Beam FIB/SEM" and "Hitachi S-4800"[^skw-01] |
| SKY130 steps | Cross-section SEM at 38 steps and a profiler or AFM at 8; see {ref}`SKY130 steps assigned to this class <machine-cross-section-sem-profilers-steps>` |

## What the machine class is and how it works

Two kinds of instrument share this class because the step pages name
them for the same purpose: the geometry of a structure that a thickness
gauge or a {ref}`CD-SEM <machine-cd-sem-overlay-metrology>` cannot see.
ITRS 2001 notes both the need and the cost: "the need for rapid,
non-destructive, inline imaging and measurement is growing", while "many
of the inline measurements for interconnect structures are made on
simplified structures or monitor wafers and are often
destructive".[^itrs-2001-met]

### Cross-sections and the SEM

A cross-section begins with breaking the wafer. SELA described the
conventional method: "analysts break the silicon wafer to create a cross
section", since "Silicon, like diamond, can be precisely cleaved along
crystal planes", and then polish the cleaved face until it reaches the
feature; the polishing "is inherently dirty and can introduce artifacts",
is "completely destructive", and needs "a highly skilled
operator".[^sela-2001] SELA's automated microcleaving placed the final
cleave "with submicron accuracy through the targeted feature", giving
"two mirror-image cross sections", and reduced preparation "from hours to
about 10 minutes".[^sela-2001]

A cleaved face shows films and interfaces but not where one doping type
gives way to another. For that, analysts etch the section in a solution
that attacks doped silicon selectively (industry practice): Spinella et
al. describe the "selective chemical etching of doped regions in silicon
by a HF:HNO3 chemical mixture" to delineate two-dimensional junction
profiles for transmission electron microscopy.[^spinella-1996]

The face is then imaged in a field-emission SEM. Secondary electrons "can
only escape from the top few nanometers of the surface of a
sample",[^wiki-sem] so the image shows the edges and layers of the
section. Hitachi's S-4800 used a "semi in-lens detector designed for large
sample accomodation while achieving ultra-high resolution at low
accelerating voltages", with a filter that "collects and separates the
various components of pure SE, compositional SE and BSE electron
signals", and could carry an energy-dispersive X-ray
spectrometer.[^hitachi-s4800] Postek reviews SEM metrology for integrated
circuits.[^postek-1994]

### Focused ion beams and dual-beam tools

A focused ion beam (FIB) removes material where it is aimed. FEI described
its workstations as "Using a finely focused gallium ion beam" to
"precisely remove and deposit materials on a submicron scale as well as
produce high contrast images", and the FIB 200xP as a tool "for SEM/TEM
specimen cross section preparation";[^fei-fib200xp-1999] its FIB 800
accepted "packaged parts or 8-inch wafers", could "section submicron
features", and could "use particle maps generated by an inspection tool
to locate submicron defects without imaging the wafer".[^fei-fib800-1999]
A dual-beam system combines an ion column with an electron column, so that
the section can be cut and imaged in place; Wikipedia notes that such a
combination "enables the benefits of both to be utilized".[^wiki-fib]
FEI's Quanta 200 3D DualBeam, described on a 2006 capture, offered
"site-specific cross sectioning, ion beam imaging, material deposition
and etching, analysis and TEM sample preparation".[^fei-dualbeam-2006] Nikawa's review of FIB failure analysis
shows cross-sections of an electromigration open, a pinhole in the oxide
between metal and substrate, and an open caused by process anomalies, and
lists "microscopic cross sectioning for secondary electron miscroscopy
observation" among the preparation methods.[^nikawa-1991] ITRS 2001 adds
that "Cross sectioning by FIB and lift-out for imaging in a TEM or a STEM
has been successfully demonstrated".[^itrs-2001-met]

### Stylus profilers

A stylus profiler draws a fine tip across the surface and records its
height; Tencor's HRP-200 used "a long-wearing diamond-tip
stylus".[^tencor-hrp200-1996] Bennett and Dancy describe an instrument with "height resolution
of the order of 1-2 A and lateral resolution of a few tenths of a
micrometer on smooth surfaces", whose stylus loading "can be adjusted so
that no permanent marks are left on the surface".[^bennett-1981] Tencor's
production profilers on a 1997 capture included the P-22, with "stylus
forces as low as 0.05 mg on critical surfaces", and the HRP-200, which combined "a
Tencor stylus profiler with the high-resolution analysis and imaging
capabilities of an Atomic Force Microscope (AFM)".[^tencor-profiling-1997]
Tencor launched the HRP-200 for metal CMP, measuring "tungsten plug recess
…, pattern-induced erosion, dishing of metal features and scratching of
inter-layer dielectric (ILD) films", and stated that its existing
profilers "continue to be appropriate for oxide CMP
applications".[^tencor-hrp200-1996] By 2002 KLA-Tencor's HRP-240/340 added
a "Dipping Mode" for "high aspect ratio depth monitoring of device size
features",[^kla-hrp] and its P-15 could "provide CMP dishing and erosion
data".[^kla-p15] Veeco's Dektak Series V monitored "etch and deposition
uniformity thickness" on 200 mm and 300 mm wafers.[^veeco-stylus-2000]
ITRS 2001 notes that "Stylus profilers and scanned probe (atomic force)
microscopes can provide local and global flatness information, but the
throughput of these methods must be improved".[^itrs-2001-met]

### Atomic force microscopes

Binnig, Quate and Gerber introduced the AFM as "a combination of the
principles of the scanning tunneling microscope and the stylus
profilometer", with "a probe that does not damage the
surface".[^binnig-1986] Digital Instruments' Dimension series brought it
to wafers: the Dimension 3100 analysed "samples up to 200mm in diameter",
and the Dimension 9000 added "robotic cassette-to-cassette handling",
"automatic tip replacement" and pattern recognition.[^veeco-afm-2000]
Martin and Wickramasinghe imaged sidewalls with "a special boot-shaped
tip", opening the way to "measurement of critical dimensions (width and
wall angles) of lines and trenches";[^martin-1994] ITRS 2001 calls CD-AFM
"an excellent means of verifying line shape and calibrating CD
measurements".[^itrs-2001-met] The same chapter notes that such
scanning-probe ("stylus") microscopes "offer 3D measurements that are
insensitive to the conductivity of the material scanned", but that
"Flexing of the stylus degrades measurements, however, when the probe is
too slender".[^itrs-2001-met]
International SEMATECH and NIST developed a CD-AFM "reference
measurement system" as "a traceable metrology reference" for CD-SEM
benchmarking.[^dixson-2002]

### What the measurements show

Profilers made the pattern dependence of CMP measurable. Yu et al. found
dishing in trench-isolation CMP "highly pattern geometry (field width)
sensitive, increasing from ∼0 nm at a field width of 5 μm and below to
200 nm at 4 mm";[^yu-1992] Stine et al. designed test masks and
measurement methods to model polishing against layout, and found "pattern
density is a strongly dominant factor".[^stine-1998] Cross-sections, in
turn, show voids in gap fill and plugs, etch profiles and liner coverage
at the bottom of contacts (industry practice), which is what the
deposition and etch step pages name them for.

## Representative 200 mm-era models

* **FEI.** The FIB 200xP for small specimens and the FIB 800 for 8-inch
  wafers and packaged parts (1999 product pages);[^fei-fib200xp-1999][^fei-fib800-1999]
  and, by 2006, the Strata, Quanta, Nova and Helios DualBeam
  families.[^fei-dualbeam-2006]
* **Hitachi.** The S-4800 ultra-high-resolution field-emission SEM, which
  "compliments the field proven performance and reliability of the S-4700
  and S-5200".[^hitachi-s4800]
* **SELA.** The MC series of automated microcleaving systems (the MC200 won
  a *Semiconductor International* Editors' Choice award in 1998) and the
  TEMstation for TEM pre-thinning.[^sela-2001]
* **Tencor, then KLA-Tencor.** The P-10, P-11, P-22 and P-30 SMIF stylus
  profilers, the Alpha-Step 500 and the HRP-200 (1996);[^tencor-profiling-1997][^tencor-hrp200-1996]
  the P-15 and the HRP-240/340 (2002 product pages).[^kla-p15][^kla-hrp]
* **Veeco and Digital Instruments.** Dektak Series V and Dektak 3 ST
  profilers, and Dimension 3100, 5000 and 9000 AFMs
  (2000 product pages).[^veeco-stylus-2000][^veeco-afm-2000]

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page lists, under "Physical
Analysis":[^skw-01]

> "FEI Dual Beam FIB/SEM"
>
> "Hitachi S-4800"
>
> "SELA EM2 Precision Cleave"
>
> "Oxford PlasmaLab RIE deprocessing"
>
> "Allied TechPrep polisher"

Read term by term, on our reading: "FEI Dual Beam FIB/SEM" is a dual-beam
focused-ion-beam and SEM system of the kind FEI sold as
DualBeam;[^fei-dualbeam-2006] "Hitachi S-4800" is Hitachi's field-emission
SEM of that name;[^hitachi-s4800] "SELA EM2 Precision Cleave" is a SELA
cleaving system, a company whose automated cleaving tools prepare SEM and
TEM samples,[^sela-2001] but no description of an EM2 was retrieved; the
RIE and the polisher are layer-removal and mechanical-preparation tools.
The page gives no model or version for the FIB/SEM, no counts, and no
profiler or AFM; it does not say whether the group supports in-line
process monitoring, failure analysis or both.[^skw-01] The CD-SEMs of the
"Photo Metrology" group are on
{ref}`machine-cd-sem-overlay-metrology`.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
physical-analysis listings are **strong** evidence that the tools
exist:[^skw-01] they are SkyWater statements. They are **no evidence** that
SKY130 wafers are cross-sectioned on them, at which steps or how often:
the capabilities page names no step, and no step page assigns them. For
profilers and AFMs there is no public SkyWater evidence at all. The
caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`; the
machines index records that the list includes these SEMs but that "no
step page assigns them the cross-sections that the 'typically used'
sections call for".

(machine-cross-section-sem-profilers-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names cross-section SEM, or
a profiler or AFM (identical to the
{ref}`machines index <machines-index>` table):

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{dropdown} All 41 steps as one line of links (checked against the index)

*cross-section SEM:* {ref}`STIE <step-006>`, {ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`, {ref}`P1ME <step-062>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PSG <step-089>`, {ref}`LICM1E <step-094>`, {ref}`TI/TIN1 <step-097>`, {ref}`WDEP <step-099>`, {ref}`LI1ME <step-103>`–{ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`–{ref}`WDEP2 <step-110>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`VIME <step-119>`–{ref}`WDEP3 <step-121>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`VIM2E <step-130>`–{ref}`WDEP4 <step-132>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`VIM3E <step-145>`–{ref}`WDEP5 <step-147>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`VIM4E <step-160>`, {ref}`WTIAL5 <step-161>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`; *profiler or AFM:* {ref}`CMPNIT <step-012>`, {ref}`CMPP <step-090>`, {ref}`WCMPLI <step-100>`, {ref}`CMPL <step-106>`, {ref}`WCMP2 <step-111>`, {ref}`WCMP3 <step-122>`, {ref}`WCMP4 <step-133>`, {ref}`WCMP5 <step-148>`
:::
<!-- step-tables:end -->

No step page grades a cross-section SEM, FIB, profiler or AFM at SkyWater
("Machines likely used at SkyWater"), because none assigns the listed
physical-analysis tools; the pages grade the etchers, deposition tools
and polisher on their own machine pages.

## Consumables and facilities

What is specific to this class is summarised here. None of the SkyWater
sources describes the fab's cross-section or profiling practice.

* **Sacrificial wafers and pieces.** A cross-section consumes the sample;
  ITRS 2001 notes how often such measurements are made on "simplified
  structures or monitor wafers".[^itrs-2001-met]
* **Ion source and gases.** A gallium ion beam, and gas chemistries for
  metal and dielectric deposition and enhanced etch on the FIB
  workstations.[^fei-fib200xp-1999][^fei-fib800-1999]
* **Electron source and vacuum.** A field-emission electron source in a
  high-vacuum column; the S-4800 lists an "Advanced dry vacuum
  system".[^hitachi-s4800]
* **Cleaving and polishing supplies.** Scribes, polishing films and, on
  SELA's systems, an optional "in-line cryo-cooling option (liquid
  nitrogen)".[^sela-2001]
* **Styli and tips.** Profiler styli and AFM tips wear and are replaced
  (industry practice); the Dimension 9000 replaced AFM tips
  automatically.[^veeco-afm-2000]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's trench depths, profile angles,
dishing and step-height limits are not public.

* **Isolation.** {ref}`STIE <step-006>` names cross-section SEM with a
  CD-SEM for trench depth and CD, and the liner and fill pages
  ({ref}`LINOX <step-010>`, {ref}`FILOX <step-011>`) a cross-section for
  the liner and the fill; the {ref}`HDP-CVD page <machine-hdp-cvd>`
  describes patterned wafers cross-sectioned for voids.
  {ref}`CMPNIT <step-012>` names a profiler or AFM for the polish of that
  fill, where dishing depends on field width.[^yu-1992]
* **Gate and spacers.** {ref}`P1ME <step-062>` names cross-section SEM
  beside the CD-SEM, and the spacer pages ({ref}`SPNIT <step-076>`,
  {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`) a cross-section for the
  spacer profile.
* **Dielectric fill.** {ref}`PSG <step-089>` and the inter-level oxide
  pages ({ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`,
  {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`,
  {ref}`NILD6 <step-156>`) name cross-section SEM, the usual way to look
  for voids between lines (industry practice).
* **Contacts, vias and plugs.** The contact and via etch pages and the
  liner and tungsten-fill pages name cross-section SEM (for the hole
  profile, liner coverage and fill, on our reading); the tungsten CMP pages
  ({ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>` to
  {ref}`WCMP5 <step-148>`) name a profiler or AFM, the instruments Tencor
  marketed for "tungsten plug recess".[^tencor-hrp200-1996]
* **Metal lines and the seal ring.** The local-interconnect, metal and
  seal-ring etch pages name cross-section SEM for the etched profile.
* **Oxide polishes.** {ref}`CMPP <step-090>` and {ref}`CMPL <step-106>`
  name a stylus profiler beside an optical thickness mapper; the later
  oxide polishes name thickness metrology only
  ({ref}`machine-film-thickness-metrology`). Stine et al. show how such
  polishes vary with pattern density.[^stine-1998]
* **Defects in section.** A FIB that reads inspection particle maps can
  cut through a defect found by {ref}`machine-defect-inspection`, as the
  FIB 800 was designed to.[^fei-fib800-1999] Sakata, Takahashi and Sekine
  describe the dual-beam FIB as "an important tool for yield management"
  and raise gallium contamination as a concern for "whether the wafer can be
  returned back to a production line or not after the
  analysis".[^sakata-2002]

## Related pages

* {ref}`category-etch` — etch profiles, endpoint and metrology.
* {ref}`category-cmp` — dishing, erosion and step height.
* {ref}`category-deposition` — gap fill, step coverage and plugs.
* {ref}`machine-cd-sem-overlay-metrology` — top-down CD measurement.
* {ref}`machine-defect-inspection` — the defects a FIB section is cut
  through.
* {ref}`machine-film-thickness-metrology` — the thickness gauges after deposition and CMP.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

**Related patents.**

:::{dropdown} 2 families in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 7,112,790 B1 <patent-gp37018887>` — unknown
* {ref}`US 7,394,075 B1 <patent-gp39561114>` — unknown
:::

**Related papers.**

* {ref}`paper-wang-2006a` — N Wang et al., Microscopy and Microanalysis 2006 (affiliation inference)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the "Physical
  Analysis" group.[^skw-01]
* [ITRS 2001, *Metrology*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>) — SEM, FIB and scanning-probe microscopy,
  profiler flatness data and destructive interconnect
  measurements.[^itrs-2001-met]
* [Hitachi High Technologies America, *S-4800 UHR FE-SEM* product page](<https://web.archive.org/web/20091021203654/http://www.hitachi-hta.com:80/products/electron-microscopes-and-focused-ion-beam/field-emission-sem/s-4800-uhr-fe-sem>) —
  resolution, detectors and specimen size.[^hitachi-s4800]
* FEI, [*FIB 200xP*](<https://web.archive.org/web/19990128142220/http://www.feic.com:80/products/fib200xp.htm>) and [*FIB 800xP*](<https://web.archive.org/web/19990417131418/http://www.feic.com:80/products/fib800xp.htm>) product pages (1999) and [*DualBeam
  Systems*](<https://web.archive.org/web/20061101125513/http://www.fei.com:80/Products/ProdTypes/DualBeamFIB/tabid/69/Default.aspx>) page (2006) — ion-beam sectioning and dual-beam
  tools.[^fei-fib200xp-1999][^fei-fib800-1999][^fei-dualbeam-2006]
* [SELA, *Company Background* page (2001)](<https://web.archive.org/web/20011031233400/http://sela.com:80/about.htm>) — conventional and automated
  cleaving for SEM and TEM samples.[^sela-2001]
* Tencor, [*Surface Profiling*](<https://web.archive.org/web/19970302033450/http://www.tencor.com:80/products/surfaceprof.html>) page (1997) and HRP-200 press release
  (1996) — stylus profilers and CMP
  applications.[^tencor-profiling-1997][^tencor-hrp200-1996]
* KLA-Tencor, [*HRPs 240/340*](<https://web.archive.org/web/20020604105300/http://www.kla-tencor.com:80/products/metrology/hrps/hrps.html>) and [*P-15*](<https://web.archive.org/web/20020604110248/http://www.kla-tencor.com:80/products/metrology/profilers/profilers.html>) product pages
  (2002).[^kla-hrp][^kla-p15]
* Veeco, [*Stylus Profilers*](<https://web.archive.org/web/20000523020041/http://www.veeco.com:80/body_stylus_profilers.html>) and [*DI AFM*](<https://web.archive.org/web/20000521223941/http://www.veeco.com:80/body_di_afm.html>) pages
  (2000).[^veeco-stylus-2000][^veeco-afm-2000]

### High-level understanding

* [Wikipedia, *Focused ion beam*](<https://en.wikipedia.org/wiki/Focused_ion_beam>).[^wiki-fib]
* [Wikipedia, *Atomic force microscopy*](<https://en.wikipedia.org/wiki/Atomic_force_microscopy>).[^wiki-afm]
* [Wikipedia, *Profilometer*](<https://en.wikipedia.org/wiki/Profilometer>).[^wiki-profilometer]
* [Wikipedia, *Scanning electron microscope*](<https://en.wikipedia.org/wiki/Scanning_electron_microscope>) — secondary-electron
  imaging.[^wiki-sem]

### Deep dive

* [Postek, *Proc. SPIE* 1994](<https://doi.org/10.1117/12.187461>) — a review of SEM metrology for integrated
  circuits.[^postek-1994]
* [Reuss, *Nucl. Instrum. Methods B* 1985](<https://doi.org/10.1016/0168-583X(85)90299-X>) — early prospects for FIB in the
  semiconductor industry.[^reuss-1985]
* [Nikawa, *J. Vac. Sci. Technol. B* 1991](<https://doi.org/10.1116/1.585694>) — FIB applications to VLSI failure
  analysis, including cross-sectioning.[^nikawa-1991]
* [Giannuzzi and Stevie, *Micron* 1999](<https://doi.org/10.1016/S0968-4328(99)00005-0>) — FIB milling techniques for TEM
  specimen preparation.[^giannuzzi-1999]
* [Bennett and Dancy, *Appl. Opt.* 1981](<https://doi.org/10.1364/AO.20.001785>) — a stylus profiling instrument and
  its resolution.[^bennett-1981]
* [Binnig, Quate and Gerber, *PRL* 1986](<https://doi.org/10.1103/PhysRevLett.56.930>) — the atomic force
  microscope.[^binnig-1986]
* [Martin and Wickramasinghe, *APL* 1994](<https://doi.org/10.1063/1.111578>) — sidewall imaging by
  AFM.[^martin-1994]
* [Yu et al., *APL* 1992](<https://doi.org/10.1063/1.107586>) — dishing in trench-isolation CMP against field
  width.[^yu-1992]
* [Stine et al., *IEEE TSM* 1998](<https://doi.org/10.1109/66.661292>) — test masks and measurements for
  pattern-dependent CMP variation.[^stine-1998]
* [Spinella, Raineri, La Via and Campisano, *J. Vac. Sci. Technol. B*
  1996](<https://doi.org/10.1116/1.588485>) — junction delineation by selective chemical etching for
  electron microscopy.[^spinella-1996]
* [Dixson et al., *Proc. SPIE* 2002](<https://doi.org/10.1117/12.473471>) — a CD-AFM reference measurement system
  for traceable CD metrology at International SEMATECH.[^dixson-2002]
* [Sakata, Takahashi and Sekine, IPFA 2002](<https://doi.org/10.1109/IPFA.2002.1025643>) — dual-beam FIB defect
  sectioning in yield management and the gallium contamination of wafers
  returned to the line.[^sakata-2002]

## Open questions

* Whether SkyWater's physical-analysis tools are used to cross-section
  SKY130 monitor or product wafers, and at which steps, is not stated.[^skw-01]
* Which FEI dual-beam model, and what SELA's "EM2", SkyWater has is not
  stated; no description of an EM2 was retrieved.[^skw-01]
* Which stylus profilers or AFMs, if any, SkyWater uses after CMP is not
  public.
* The model list above is incomplete: it covers the FEI, Hitachi, SELA,
  Tencor/KLA-Tencor, Veeco and Digital Instruments tools for which a
  public description was found, not every SEM, FIB, profiler or AFM of
  the period.

<!-- footnotes -->

[^itrs-2001-met]: International Technology Roadmap for Semiconductors,
    *2001 Edition: Metrology*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Met.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^hitachi-s4800]: Hitachi High Technologies America, *S-4800 UHR FE-SEM*,
    product page; Wayback Machine capture of 2009-10-21.
    <https://web.archive.org/web/20091021203654/http://www.hitachi-hta.com:80/products/electron-microscopes-and-focused-ion-beam/field-emission-sem/s-4800-uhr-fe-sem>
[^fei-fib200xp-1999]: FEI Company, *FIB workstations: FIB 200xP*, product
    page; Wayback Machine capture of 1999-01-28.
    <https://web.archive.org/web/19990128142220/http://www.feic.com:80/products/fib200xp.htm>
[^fei-fib800-1999]: FEI Company, *FIB workstations: FIB 800xP*, product
    page; Wayback Machine capture of 1999-04-17.
    <https://web.archive.org/web/19990417131418/http://www.feic.com:80/products/fib800xp.htm>
[^fei-dualbeam-2006]: FEI Company, *DualBeam Systems*, product-type page;
    Wayback Machine capture of 2006-11-01.
    <https://web.archive.org/web/20061101125513/http://www.fei.com:80/Products/ProdTypes/DualBeamFIB/tabid/69/Default.aspx>
[^sela-2001]: SELA, *Company Background* (conventional, automated SEM and
    automated TEM sample preparation), web page; Wayback Machine capture of
    2001-10-31. <https://web.archive.org/web/20011031233400/http://sela.com:80/about.htm>
[^tencor-profiling-1997]: Tencor Instruments, *Surface Profiling* (HRP-200,
    P-22, P-30 SMIF, P-10, P-11, P-12, FP-20 and Alpha-Step 500), product
    page; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033450/http://www.tencor.com:80/products/surfaceprof.html>
[^tencor-hrp200-1996]: Tencor Instruments, *Tencor Instruments Unveils
    Advanced Metrology Product for Production-Level Wafer Surface
    Characterization* (HRP-200 High Resolution Profiler), press release,
    1996-10-14; Wayback Machine capture of 1997-03-02.
    <https://web.archive.org/web/19970302033817/http://www.tencor.com:80/press/HRP_200PR.html>
[^kla-hrp]: KLA-Tencor, *HRPs 240/340: Automated high-resolution surface
    metrology*, product page; Wayback Machine capture of 2002-06-04.
    <https://web.archive.org/web/20020604105300/http://www.kla-tencor.com:80/products/metrology/hrps/hrps.html>
[^kla-p15]: KLA-Tencor, *Profilers P-15: High Performance Surface
    Metrology*, product page; Wayback Machine capture of 2002-06-04.
    <https://web.archive.org/web/20020604110248/http://www.kla-tencor.com:80/products/metrology/profilers/profilers.html>
[^veeco-stylus-2000]: Veeco Instruments, *Dektak Stylus Profilers*, product
    page; Wayback Machine capture of 2000-05-23.
    <https://web.archive.org/web/20000523020041/http://www.veeco.com:80/body_stylus_profilers.html>
[^veeco-afm-2000]: Veeco Instruments, *Digital Instruments Atomic Force
    Microscopes (AFMs)*, product page; Wayback Machine capture of
    2000-05-21. <https://web.archive.org/web/20000521223941/http://www.veeco.com:80/body_di_afm.html>
[^wiki-fib]: Wikipedia, *Focused ion beam*.
    <https://en.wikipedia.org/wiki/Focused_ion_beam>
[^wiki-afm]: Wikipedia, *Atomic force microscopy*.
    <https://en.wikipedia.org/wiki/Atomic_force_microscopy>
[^wiki-profilometer]: Wikipedia, *Profilometer*.
    <https://en.wikipedia.org/wiki/Profilometer>
[^wiki-sem]: Wikipedia, *Scanning electron microscope*.
    <https://en.wikipedia.org/wiki/Scanning_electron_microscope>
[^postek-1994]: M. T. Postek, "Scanning electron microscope metrology",
    *Proc. SPIE* **10274**, 1027405 (1994).
    <https://doi.org/10.1117/12.187461>
[^reuss-1985]: R. H. Reuss, "Potential applications of focused ion beam
    technology for the semiconductor industry", *Nuclear Instruments and
    Methods in Physics Research B* **10–11**, 515–521 (1985).
    <https://doi.org/10.1016/0168-583X(85)90299-X>
[^nikawa-1991]: K. Nikawa, "Applications of focused ion beam technique to
    failure analysis of very large scale integrations: A review", *Journal
    of Vacuum Science & Technology B* **9**(5), 2566–2577 (1991).
    <https://doi.org/10.1116/1.585694>
[^giannuzzi-1999]: L. A. Giannuzzi and F. A. Stevie, "A review of focused
    ion beam milling techniques for TEM specimen preparation", *Micron*
    **30**(3), 197–204 (1999).
    <https://doi.org/10.1016/S0968-4328(99)00005-0>
[^bennett-1981]: J. M. Bennett and J. H. Dancy, "Stylus profiling
    instrument for measuring statistical properties of smooth optical
    surfaces", *Applied Optics* **20**(10), 1785 (1981).
    <https://doi.org/10.1364/AO.20.001785>
[^binnig-1986]: G. Binnig, C. F. Quate and Ch. Gerber, "Atomic Force
    Microscope", *Physical Review Letters* **56**(9), 930–933 (1986).
    <https://doi.org/10.1103/PhysRevLett.56.930>
[^martin-1994]: Y. Martin and H. K. Wickramasinghe, "Method for imaging
    sidewalls by atomic force microscopy", *Applied Physics Letters*
    **64**(19), 2498–2500 (1994). <https://doi.org/10.1063/1.111578>
[^yu-1992]: C. Yu, P. C. Fazan, V. K. Mathews and T. T. Doan, "Dishing
    effects in a chemical mechanical polishing planarization process for
    advanced trench isolation", *Applied Physics Letters* **61**(11),
    1344–1346 (1992). <https://doi.org/10.1063/1.107586>
[^spinella-1996]: C. Spinella, V. Raineri, F. La Via and S. U. Campisano,
    "Two-dimensional junction profiling by selective chemical etching:
    Applications to electron device characterization", *Journal of Vacuum
    Science & Technology B* **14**(1), 414–420 (1996).
    <https://doi.org/10.1116/1.588485>
[^dixson-2002]: R. G. Dixson, A. Guerry, M. H. Bennett, T. V. Vorburger and
    M. T. Postek, "Toward traceability for at-line AFM dimensional
    metrology", *Proc. SPIE* **4689**, Metrology, Inspection, and Process
    Control for Microlithography XVI, 313 (2002).
    <https://doi.org/10.1117/12.473471>
[^sakata-2002]: T. Sakata, H. Takahashi and T. Sekine, "Investigation of Ga
    contamination due to analysis by dual beam FIB", *Proceedings of the
    9th International Symposium on the Physical and Failure Analysis of
    Integrated Circuits (IPFA 2002)*, pp. 174–178.
    <https://doi.org/10.1109/IPFA.2002.1025643>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning, J. E.
    Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and S.-Y. Oh,
    "Rapid characterization and modeling of pattern-dependent variation in
    chemical-mechanical polishing", *IEEE Transactions on Semiconductor
    Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
