(machine-coat-develop-track)=
# Coat/develop track

A coat/develop track is the automated wafer-processing line that sits
beside every exposure tool. It primes the wafer, spins on the
anti-reflective coating and the resist, bakes them, hands the wafer to
the stepper or scanner, takes it back for the post-exposure bake, and
develops, rinses and dries the pattern.[^wiki-litho]

| | Coat/develop track |
|---|---|
| What it does | "Wafer track systems are also known as wafer coater/developer systems"; "The photolithography process is carried out by the wafer track and stepper/scanner", which "are usually installed side by side, and are 'linked' together".[^wiki-litho] |
| Modules | The ACT 8 "features spinner modules, thermal processing units, and an optical edge bead removal unit integrated with the stepper interface".[^tel-act8] |
| Coat | Spin coating: "layers of photoresist about 1 micrometre thick", "typically spun at 20 to 80 revolutions per second for 30 to 60 seconds";[^wiki-spin-coating] SKY130's nominal photoresist thickness 1.14 µm, HV tip implants 0.3 µm.[^pdk-03] |
| Bake | Prebake "typically at 90 to 100 °C for 30 to 60 seconds on a hotplate"; chemically amplified resist is "much more sensitive" in "time, temperature, and delay" at the post-exposure bake.[^wiki-litho] |
| Develop | "The develop chemistry is delivered on a spinner"; "Metal-ion-free developers such as tetramethylammonium hydroxide (TMAH) are now used".[^wiki-litho] |
| Throughput | "as many as 120 wafers per hour" (ACT 8);[^tel-act8] "Inline: 120" wph (ACT 12 and ACT 8Z).[^tel-act] |
| 200 mm era | ACT 8, "debuted in the coater/developer marketplace in 1997 to handle 200mm wafers";[^tel-act8] SCREEN's "Long-Selling 60/80 Series".[^screen-sk80ex] |
| SkyWater-listed tool | "DNS 80B track", "Sokudo RF3 track", "TEL ProZ Lithius track"[^skw-01] |
| SKY130 steps | all 36 mask steps; see {ref}`SKY130 steps assigned to this class <machine-coat-develop-track-steps>` |

:::{seealso}
The resist chemistry and the sequence of a
mask step are on the {ref}`category page <category-lithography>`.
:::

## What the machine class is and how it works

A track is a set of single-wafer process stations — vapour prime, spin
coaters, hot plates, chill plates, developers — arranged around one or
more robots, with a cassette station at one end and an interface to the
exposure tool at the other. It is a cluster of spin cups and
hot and chill plates served by robots, usually linked in line to one
exposure tool.[^wiki-litho]

**Why "track".** The name is historical: "Wafer tracks are
named after the 'tracks' used to carry wafers inside the machine, but
modern machines do not use tracks".[^wiki-litho] Kato's chronology
traces Tokyo Electron's tracks to Cobilt, which "also built wafer
tracks" in the 1970s.[^kato-2007]

What makes the class distinct from a
general wet or thermal tool is its tie to the exposure tool: the wafer
leaves the track primed, coated and baked, and returns to it within the
same lithography cell for the post-exposure bake and
develop.[^wiki-litho][^fujiwara-2006]

### Prime and anti-reflective coating

Before coating, the wafer is dehydrated and primed: an adhesion promoter
such as "hexamethyldisilazane", HMDS, reacts with the surface oxide "to
form tri-methylated silicon-dioxide, a highly water repellent layer",
which "prevents the aqueous developer from penetrating between the
photoresist layer and the wafer's surface".[^wiki-litho]

**BARC on KrF levels.** On KrF levels
a fab typically spins and bakes an organic bottom anti-reflective
coating ({term}`BARC`) first ({ref}`category-lithography`). Brunner
showed why: interference in the resist film makes the dose to clear
swing with resist thickness, with a swing ratio of about
{math}`4\sqrt{R_1 R_2}\,e^{-\alpha D}` for the reflectivities at the top
and bottom of the resist and its absorption.[^brunner-1991] Anti-reflective coating
processes "reduce S as the square root of substrate reflectivity under
the resist".[^brunner-1991]

### Spin coating and edge bead removal

Resist is dispensed on the wafer and spun off to a film. Emslie, Bonner
and Peck showed that "centrifugation of a fluid layer that is initially
uniform does not disturb the uniformity" and that "initially irregular
fluid distributions tend toward uniformity".[^emslie-1958]

**Thickness scaling.** Meyerhofer
added evaporation and found the film thickness "uniform and independent
of the size of the substrate", scaling as
{math}`h \propto f^{-2/3}\,\nu_0^{1/3}\,e^{1/3}` with spin speed
{math}`f`, initial viscosity {math}`\nu_0` and evaporation rate
{math}`e`; since the evaporation rate itself scales as {math}`f^{1/2}`,
the net dependence is {math}`h \propto f^{-1/2}`.[^meyerhofer-1978] Spin
speed and resist viscosity therefore set the thickness the step pages
need, from thin resist on the gate and via levels to thick resist for
high-energy implant masks.

**Edge bead removal.** Resist builds up at the rim: "viscous films
may result in large edge beads", and "Edge bead removal (EBR) is carried
out, usually with a nozzle, to remove this extra resist as it could
otherwise cause particulate contamination".[^wiki-litho] The ACT 8 has
"an optical edge bead removal unit" as well.[^tel-act8]

### Bake and chill plates

After coating, a prebake drives off the casting solvent.[^wiki-litho]
After exposure, a post-exposure bake ({term}`PEB`) drives the chemistry
of deep-UV resists, in which acid generated by exposure diffuses and
reacts at once — a coupled reaction–diffusion that Smith and Mack showed
cannot be reproduced by a decoupled model.[^smith-mack-2001]

**Bake-plate uniformity.** Bake-plate
uniformity specifications tighten as features shrink. Ramanan,
Kozman and Sims found that wafer uniformity on a proximity bake plate
"depends on a number of parameters in addition to the uniformity of the
bake plate itself".[^ramanan-2000] Among them are "the lid design, the air flow
distribution around the bake chamber, bake plate design and flatness of
the bake plate and wafer".[^ramanan-2000]

Chill plates bring the wafer
back to a fixed temperature before the next coat, exposure or develop
(industry practice). TEL's ACT 12 advertises "a high precision oven to
support DUV processing".[^tel-act]

### Develop, rinse and dry

"The develop chemistry is delivered on a spinner, much like
photoresist", and "Metal-ion-free developers such as tetramethylammonium
hydroxide (TMAH) are now used", with developer temperature controlled
"to within 0.2 °C".[^wiki-litho] A common ready-to-use strength is
2.38 % TMAH.[^microchemicals-dev]

**Puddle develop.** A puddle develop spreads developer
over the stationary wafer; Perera found that the developer's surface
tension "has to be lowered, by adding a surfactant, to avoid 'pullback'
of the developer during puddling".[^perera-1989] Temperature matters
here too: Eto, Ito and Homma measured the wafer edge "approximately
1.3 °C lower than that of the central area after 60 s" of puddle
development, and a DNQ/novolac resist CD changing "at a rate of
approximately 5 nm/°C".[^eto-2007] The wafer is then rinsed with water
and spun dry.

### Link to the exposure tool and airborne amines

In a linked cell the robot passes each coated wafer through an interface
to the stepper or scanner and takes it back after exposure; the Nikon
NSR-S204B, for example, lists an "In-Line Track Interface".[^nikon-s204b]
Fujiwara et al. describe the same arrangement for an ArF immersion
scanner "connected inline with a coat/developer (C/D) ACT12", where wafer
handling and the rinse before the post-exposure bake were optimised
against watermarks.[^fujiwara-2006]

**Airborne amines.** For chemically amplified resists the air in the track matters: MacDonald
et al. found such a resist "severely degraded by vapor from organic
bases" at "as little as 15 parts per billion (ppb)", and relieved it with
"localized air filtration".[^macdonald-1991] TEL's ACT 12 "uses a chemical
filter and a high precision oven to support DUV processing".[^tel-act]

## Representative 200 mm-era models

The CLEAN TRACK Mark series came first, then the CLEAN TRACK ACT series,
"developed as coater/developer to support 300/200mm wafer processes,
based on the technology from the CLEAN TRACK Mark Series".[^tel-act]

:::{table} Representative coat/develop tracks of the 200 mm era (figures as each source gives them)
:widths: 20 20 10 50

| Vendor | Model | Year | Published figures |
|---|---|---:|---|
| Tokyo Electron | CLEAN TRACK ACT 8 | 1997 | "debuted in the coater/developer marketplace in 1997 to handle 200mm wafers", "to process geometries ranging from 350 nanometers to 180 nanometers and beyond"[^tel-act8] |
| Tokyo Electron | CLEAN TRACK ACT 8Z | 2023 | "as a renewed version of CLEAN TRACK ACT 8"[^tel-act] |
| Tokyo Electron | CLEAN TRACK LITHIUS (original, succeeded the ACT series) | — | "is a 300/200mm coater/developer"[^tel-lithius] |
| Tokyo Electron | LITHIUS Pro Z | — | "TEL's most advanced 300mm coater/developer for the 10nm technology node and beyond"[^tel-lithius] |
| SCREEN (DNS) | SK-60EX/SK-80EX | — | for wafers of 50–200 mm, "Continuing the Reliability of the Long-Selling 60/80 Series" with "its large installed base"[^screen-sk80ex] |
| SCREEN | RF-200EX | — | "Dedicated design for 200mm wafers" that "enables a small footprint and DUV process"[^screen-rf200ex] |
| Sokudo | RF3 | — | "is designed with a modular structure", sold for "65nm and 45nm node manufacturing"[^sokudo-rf3-2006] |
:::

The ACT 8 "includes proven technologies to meet challenges in DUV and
I-line processing".[^tel-act8] Sokudo is a coat/develop track company
"owned by Dainippon Screen Mfg. Co., Ltd. and Applied Materials, Inc.",
"established on July 3, 2006".[^sokudo-rf3-2006] The RF3 release
concerns a site converting from 200 mm to 300 mm, so it does not show a
200 mm RF3 configuration.

**Others.** The step pages also name SVG/ASML tracks (the 90S); no
vendor description of that model was retrieved for this page.

## At SkyWater

### What SkyWater lists

Under "Lithography", after the exposure tools, SkyWater's *Facilities &
Capabilities* page lists three tracks:[^skw-01]

> "DNS 80B track"
>
> "Sokudo RF3 track"
>
> "TEL ProZ Lithius track"

:::{table} How this reference reads the three track entries
:widths: 26 50 24

| Entry as listed | What it names | Status |
|---|---|---|
| "DNS 80B track" | "DNS" is Dainippon Screen, a joint owner of Sokudo;[^sokudo-rf3-2006] "80B" read as a member of the 60/80 series SCREEN still describes,[^screen-sk80ex] an inference from the model number | our reading |
| "Sokudo RF3 track" | "Sokudo RF3" names Sokudo's RF3 track[^sokudo-rf3-2006] | not stated |
| "TEL ProZ Lithius track" | "TEL ProZ Lithius" is SkyWater's word order; TEL describes its LITHIUS Pro Z as a 300 mm coater/developer for the 10 nm node,[^tel-lithius] so, as on the {ref}`machines index <machines-index>`, this reference does not identify the 200 mm fab's track with that model | our reading |
:::

SkyWater gives no wafer
size, module list, resist process or pairing with an exposure tool for
any of the three.[^skw-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the three listings are **strong**: they are SkyWater
statements.[^skw-01] The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.
For this class the S-1 adds indirect support: it names photoresist
suppliers — "The Dow Chemical Company (photoresist)", "JSR Corporation
(photoresist)", "Tokyo Ohka Kogyo America, Inc. (photoresist)" — and
"Air Products & Chemicals, Inc., Moses Lake (developer)".[^sec-01] These
are the materials a track consumes, though not a track vendor.

(machine-coat-develop-track-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a coat/develop track
(identical to the {ref}`machines index <machines-index>` table):

all 36 mask steps, {ref}`FOM <step-004>` to {ref}`PDM <step-168>` ({ref}`masks-index`)

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{table} The 2 steps above: number, code and name
:widths: 10 16 74

| Step | Code | Name |
|---:|:---|:---|
| 4 | {ref}`FOM <step-004>` | Field oxide mask |
| 168 | {ref}`PDM <step-168>` | Pad mask |
:::
<!-- step-tables:end -->

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"DNS 80B track", "Sokudo RF3 track", "TEL ProZ Lithius track"** — *strong, or strong for existence (some pages add that which track serves which exposure tool is not public):* {ref}`FOM <step-004>`, {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`P1M <step-061>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`NPCM <step-078>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`

The {ref}`category page <category-lithography>` describes every mask
step as a coat, expose and develop sequence, so the class assignment
follows from the category; which of the three tracks runs a given level
is not stated, and no step page grades that.

## Consumables and facilities

The lithography consumables are described on the
{ref}`lithography materials <material-lithography-materials>` page and
listed in the {ref}`materials index <materials-index>`; what is specific to a track is
summarised here. None of the SkyWater sources describes the fab's
chemical delivery or track exhaust. Ultrapure water, its standards and
its quality parameters are described on the
{ref}`ultrapure water <material-ultrapure-water>` page.

* **Resists and anti-reflective coatings.** i-line DNQ/novolac and KrF
  chemically amplified resists and organic BARCs
  ({ref}`category-lithography`); the S-1 suppliers are quoted
  above.[^sec-01] SCREEN presents reduced "resist consumption during
  wafer coating" as a design aim of its current 200 mm
  tracks.[^screen-rf200ex]
* **Adhesion promoter.** HMDS vapour.[^wiki-litho]
* **Solvents.** Edge-bead-removal and cup-rinse solvent; the resist's
  casting solvent is driven off in the bake ({ref}`category-lithography`).
* **Developer.** Typically metal-ion-free TMAH, commonly
  2.38 %,[^microchemicals-dev] with temperature-controlled
  delivery;[^wiki-litho] SkyWater's S-1 names "Air Products & Chemicals,
  Inc., Moses Lake (developer)" without giving its chemistry.[^sec-01]
* **Water, exhaust and filtration.** Ultrapure water for the develop
  rinse and exhaust from the spin cups and bake plates (industry
  practice); chemical filtration of the track air for chemically
  amplified resists.[^macdonald-1991][^tel-act]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's resists, thicknesses, bake
temperatures and develop times per layer are not public, apart from the
nominal photoresist thickness (1.14 µm) and the photoresist thickness
for HV tip implants (0.3 µm) in the design assumptions.[^pdk-03]

* **Two resist families on shared tracks.** On the step pages' readings
  the i-line levels ({ref}`machine-i-line-stepper`) use DNQ/novolac resist
  and the KrF levels ({ref}`machine-duv-krf-stepper`) chemically amplified
  resist with BARC and a tightly controlled post-exposure bake.

  The
  {ref}`LICM1 <step-093>` and {ref}`LI1M <step-102>` pages name "BARC and
  DUV resist modules and PEB plates". The TEL ACT 8 was built for both
  ("DUV and I-line processing").[^tel-act8] Which of SkyWater's three
  tracks runs which family is not public.
* **Thick and thin resist.** The deep N-well, N-well, P-well block and
  drift-well masks ({ref}`DNM <step-007>`, {ref}`NWM <step-017>`,
  {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`) and metal 5
  ({ref}`MM5 <step-162>`) call for a track with thick-resist capability,
  and the {ref}`HVNTM <step-068>` page for a thin-resist recipe, matching
  the PDK's 0.3 µm "Photoresist thickness for HV Tip
  Implants".[^pdk-03]

  With
  Meyerhofer's scaling, a thicker film needs a slower spin or a more
  viscous resist.[^meyerhofer-1978]
* **Implant masks and hardening.** The {ref}`PSDM <step-081>` and
  {ref}`NSDM <step-085>` pages name a UV-cure or hard-bake module for the
  resist before the high-dose source/drain implants; Wikipedia describes a
  hard bake that "solidifies the remaining photoresist, to make a more
  durable protecting layer in future ion implantation".[^wiki-litho]
* **Developer and bake control.** CD varied with wafer temperature at
  about 5 nm/°C for a DNQ/novolac resist in Eto et al.'s puddle
  develop,[^eto-2007] so a developer held to 0.2 °C[^wiki-litho] would
  contribute about 1 nm (our arithmetic); for the chemically amplified
  KrF levels the post-exposure bake is the more sensitive
  step.[^wiki-litho][^smith-mack-2001]
* **Rework.** In a fab of this kind a wafer whose CD or overlay fails
  after develop is stripped and re-coated rather than etched (industry
  practice; {ref}`category-lithography`), so the
  track also runs rework lots.
* **Resist kept through several steps.** The {ref}`TUNM <step-035>`
  resist serves an ARC etch, two implants and a wet etch
  ({ref}`masks-index`, *Patterns*; {ref}`TUNARCE <step-036>`), so its
  coat and bakes must survive all four (our reading).

## Related pages

* **Category.** {ref}`category-lithography` — the sequence of a mask
  step, resists, anti-reflective coatings and developer.
* **Machines.** {ref}`machine-i-line-stepper` and
  {ref}`machine-duv-krf-stepper` — the exposure tools the tracks are
  linked to. {ref}`machine-cd-sem-overlay-metrology` — the CD and
  overlay measurements after develop, and the rework they trigger.
* **Materials.** {ref}`material-lithography-materials` — resists,
  coatings, developer, solvents, reticles and light-source consumables.
  {ref}`material-ultrapure-water` — the develop rinse water, its
  standards and quality.
* **Indexes.** {ref}`machines-index` — all machine classes, SkyWater's
  listed tools and the step assignments. {ref}`materials-index` —
  resists, BARC, HMDS, developer and ultrapure water.
  {ref}`masks-index` — the 36 mask steps the tracks serve.

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the "DNS 80B track",
  "Sokudo RF3 track" and "TEL ProZ Lithius track" entries.[^skw-01]
* [SkyWater Technology, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — photoresist and developer
  suppliers.[^sec-01]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — the nominal and HV tip-implant
  photoresist thicknesses.[^pdk-03]
* [Tokyo Electron, *Coater/Developer ACT Series*](<https://www.tel.com/product/act.html>) — the ACT 8Z and ACT 12,
  their throughput, processes and DUV features.[^tel-act]
* [Semiconductor Online, *CLEAN TRACK ACT 8*](<https://www.semiconductoronline.com/doc/clean-track-act-8-system-for-spin-on-dielectr-0001>) — the 200 mm track of 1997,
  its modules, stepper interface and throughput.[^tel-act8]
* [Tokyo Electron, *Coater/Developer LITHIUS Series*](<https://www.tel.com/product/lithius.html>) — the LITHIUS and
  LITHIUS Pro Z.[^tel-lithius]
* [SCREEN Semiconductor Solutions, *SK-60EX/SK-80EX*](<https://www.screen.co.jp/spe/en/products/sk-60ex80ex>) — the 60/80 series of
  tracks for wafers up to 200 mm.[^screen-sk80ex]
* [SCREEN Semiconductor Solutions, *RF-200EX/RF-300EX*](<https://www.screen.co.jp/spe/en/products/rf-200ex300ex>) — a current 200 mm
  DUV track.[^screen-rf200ex]
* [Sokudo, RF3 press release (2006)](<https://www.screen.co.jp/eng/spe/mt-images/pr060920_e.pdf>) — the Sokudo joint venture and its
  modular RF3 track.[^sokudo-rf3-2006]
* [Nikon, *NSR-S204B* specification summary](<https://f.machineryhost.com/fc49306d97602c8ed1be1dfbf0835ead/aa008f2897d7d4a224ff92839b4299e9/SpecSummary_LITV25-01_NSR-S204B.pdf>) — the in-line track interface
  of an exposure tool.[^nikon-s204b]

### High-level understanding

* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — the track and its sequence: prime,
  coat, EBR, bakes, develop and the link to the exposure
  tool.[^wiki-litho]
* [Wikipedia, *Spin coating*](<https://en.wikipedia.org/wiki/Spin_coating>) — spin speeds, film thickness and edge
  beads.[^wiki-spin-coating]
* [Wikipedia, *Tetramethylammonium hydroxide*](<https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>) — the developer.[^wiki-tmah]
* [MicroChemicals, *Development of photoresists*](<https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>) — developer types,
  strength and practice.[^microchemicals-dev]
* [Kato, *Chronology of Lithography Milestones* (2007)](<https://www.lithoguru.com/scientist/litho_history/Kato_Litho_History.pdf>) — the Cobilt origin
  of TEL's tracks.[^kato-2007]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — resist
  processing from coat to develop.[^mack-2007]

### Deep dive

* [Emslie, Bonner and Peck, *J. Appl. Phys.* 1958](<https://doi.org/10.1063/1.1723300>) — the flow of a viscous
  liquid on a rotating disk, the basis of spin coating.[^emslie-1958]
* [Meyerhofer, *J. Appl. Phys.* 1978](<https://doi.org/10.1063/1.325357>) — resist film thickness against spin
  speed, viscosity and evaporation.[^meyerhofer-1978]
* [Brunner, *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46410>) — swing curves and the case for
  anti-reflective coatings.[^brunner-1991]
* [Ito and Willson, *ACS Symp. Ser.* 1984](<https://doi.org/10.1021/bk-1984-0242.ch002>) — chemically amplified
  resists.[^ito-1984]
* [MacDonald et al., *Proc. SPIE* 1991](<https://doi.org/10.1117/12.46354>) — airborne amine contamination of
  chemically amplified resist and filtered air.[^macdonald-1991]
* [Smith and Mack, *Proc. SPIE* 2001](<https://doi.org/10.1117/12.436827>) — reaction–diffusion models of the
  post-exposure bake.[^smith-mack-2001]
* [Ramanan, Kozman and Sims, *Proc. SPIE* 2000](<https://doi.org/10.1117/12.388375>) — wafer against bake-plate
  temperature uniformity in proximity bake.[^ramanan-2000]
* [Perera, *Proc. SPIE* 1989](<https://doi.org/10.1117/12.953060>) — developer design for spray-puddle
  develop.[^perera-1989]
* [Eto, Ito and Homma, *JJAP* 2007](<https://doi.org/10.1143/JJAP.46.3354>) — wafer temperature and resist CD
  during puddle development.[^eto-2007]
* [Fujiwara et al., *Proc. SPIE* 2006](<https://doi.org/10.1117/12.656303>) — wafer handling between a
  coat/developer and an in-line exposure tool.[^fujiwara-2006]
* [Dammel, *Diazonaphthoquinone-based Resists*](<https://doi.org/10.1117/3.2265072>) — i-line resist
  chemistry.[^dammel-1993]
* [Norton et al., IIT 2000](<https://doi.org/10.1109/IIT.2000.924278>) — i-line and DUV resists under high-current
  implantation.[^norton-2000]

## Open questions

* Which of SkyWater's three tracks is linked to which exposure tool, and
  which runs i-line or KrF resist, are not public.[^skw-01]
* What model "DNS 80B" and "TEL ProZ Lithius" denote for 200 mm wafers,
  and whether the "Sokudo RF3" is configured for 200 mm, are not
  stated.[^skw-01][^tel-lithius]
* Whether any SKY130 level uses a UV-cure or hard bake, a BARC or a top
  anti-reflective coating is not public; the step pages read these from
  industry practice.
* The model list above is incomplete: it covers the TEL, SCREEN and
  Sokudo tracks for which a public description was found, not the SVG and
  other tracks of the period.

<!-- footnotes -->

[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^tel-act8]: Semiconductor Online, *CLEAN TRACK ACT 8 System for Spin-On
    Dielectric (SOD) Applications* (Tokyo Electron America), accessed
    2026-09-13.
    <https://www.semiconductoronline.com/doc/clean-track-act-8-system-for-spin-on-dielectr-0001>
[^wiki-spin-coating]: Wikipedia, *Spin coating*.
    <https://en.wikipedia.org/wiki/Spin_coating>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^tel-act]: Tokyo Electron, *Coater/Developer ACT Series*, product page,
    accessed 2026-09-13. <https://www.tel.com/product/act.html>
[^screen-sk80ex]: SCREEN Semiconductor Solutions, *Coat/Develop Track:
    SK-60EX/SK-80EX*, product page, accessed 2026-09-13.
    <https://www.screen.co.jp/spe/en/products/sk-60ex80ex>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^kato-2007]: A. Kato, *Chronology of Lithography Milestones*, version
    0.9, May 2007, hosted on lithoguru.com, accessed 2026-09-13.
    <https://www.lithoguru.com/scientist/litho_history/Kato_Litho_History.pdf>
[^fujiwara-2006]: T. Fujiwara, K. Shiraishi, H. Tanizaki, Y. Ishii, H.
    Kyoda, T. Yamamoto and S. Ishida, "Wafer management between
    coat/developer track and immersion lithography tool", *Proc. SPIE*
    **6154**, 61544L (2006). <https://doi.org/10.1117/12.656303>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^emslie-1958]: A. G. Emslie, F. T. Bonner and L. G. Peck, "Flow of a
    viscous liquid on a rotating disk", *Journal of Applied Physics*
    **29**(5), 858–862 (1958). <https://doi.org/10.1063/1.1723300>
[^meyerhofer-1978]: D. Meyerhofer, "Characteristics of resist films
    produced by spinning", *Journal of Applied Physics* **49**(7),
    3993–3997 (1978). <https://doi.org/10.1063/1.325357>
[^smith-mack-2001]: M. D. Smith and C. A. Mack, "Examination of a
    simplified reaction-diffusion model for post-exposure bake of
    chemically amplified resists", *Proc. SPIE* **4345**, 1022 (2001).
    <https://doi.org/10.1117/12.436827>
[^ramanan-2000]: N. Ramanan, A. Kozman and J. B. Sims, "Differences
    between wafer and bake plate temperature uniformity in proximity bake:
    a theoretical and experimental study", *Proc. SPIE* **3999**, 890
    (2000). <https://doi.org/10.1117/12.388375>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note, accessed 2026-09-13.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^perera-1989]: T. Perera, "Characteristics of a developer for spray
    puddle develop processes", *Proc. SPIE* **1086**, 470 (1989).
    <https://doi.org/10.1117/12.953060>
[^eto-2007]: H. Eto, Y. Ito and T. Homma, "Effect of temperature on
    photoresist critical dimension during puddle development", *Japanese
    Journal of Applied Physics* **46**(6R), 3354 (2007).
    <https://doi.org/10.1143/JJAP.46.3354>
[^nikon-s204b]: Nikon, *NSR-S204B 248 nm Scanner Exposure System
    Overview* (specification summary, reseller copy), attached to the
    listing Tara Semiconductor Technology, *Used 2002 NIKON S204 Scanner*
    (listing LITV25-01), accessed 2026-09-13.
    <https://f.machineryhost.com/fc49306d97602c8ed1be1dfbf0835ead/aa008f2897d7d4a224ff92839b4299e9/SpecSummary_LITV25-01_NSR-S204B.pdf>,
    <https://www.tarasemi.com/listings/5223879-used-2002-nikon-s204-scanner>
[^macdonald-1991]: S. A. MacDonald, N. J. Clecak, H. R. Wendt, C. G.
    Willson, C. D. Snyder, C. J. Knors, N. B. Deyoe, J. G. Maltabes, J. R.
    Morrow, A. E. McGuire and S. J. Holmes, "Airborne chemical contamination
    of a chemically amplified resist", *Proc. SPIE* **1466**, 2–12 (1991).
    <https://doi.org/10.1117/12.46354>
[^tel-lithius]: Tokyo Electron, *Coater/Developer LITHIUS Series*,
    product page, accessed 2026-09-13.
    <https://www.tel.com/product/lithius.html>
[^screen-rf200ex]: SCREEN Semiconductor Solutions, *Coat/Develop Track:
    RF-200EX/RF-300EX*, product page, accessed 2026-09-13.
    <https://www.screen.co.jp/spe/en/products/rf-200ex300ex>
[^sokudo-rf3-2006]: Sokudo Co., Ltd. and JSR Micro, Inc., *JSR Micro, Inc.
    Selects RF3 Track System from Sokudo Co., Ltd.*, press release,
    2006-09-20, hosted by SCREEN (document PR060920E), accessed 2026-09-13.
    <https://www.screen.co.jp/eng/spe/mt-images/pr060920_e.pdf>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^ito-1984]: H. Ito and C. G. Willson, "Applications of Photoinitiators to
    the Design of Resists for Semiconductor Manufacturing", *ACS Symposium
    Series* **242**, 11–23 (1984).
    <https://doi.org/10.1021/bk-1984-0242.ch002>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
[^norton-2000]: C. Norton, D. Marshall, M. Ameen, D. Whiteside, J. Hallock
    and A. Becknell, "Photoresist properties during high current
    implantation: an I-line vs. DUV resist comparison", *Proc. 2000
    International Conference on Ion Implantation Technology*, pp. 813–816.
    <https://doi.org/10.1109/IIT.2000.924278>
