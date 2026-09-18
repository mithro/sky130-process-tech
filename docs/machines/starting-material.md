(machine-starting-material)=
# Starting material: incoming inspection, marking and sorting

A fab does not grow or polish its own silicon. Crystal pulling, slicing,
lapping and polishing happen at the wafer vendor, and the wafers arrive
in sealed cassettes made to a written specification. What the fab
itself runs on them before the first process step is a small group of
machines: a laser surface scanner that counts particles and measures
haze on the bare wafer, a laser marker that writes an identifier into
the silicon, and a sorter that reads the identifiers and puts the wafers
into lots. This page describes that group in general, lists
representative 200 mm-era models, and then says what SkyWater has
published about its own tools of this class and which SKY130 step this
reference assigns to it. The wafer itself — diameter, doping,
orientation, oxygen and the vendor's equipment — is on the
{ref}`category page <category-substrate>`; the clean that follows is on
the {ref}`wet bench page <machine-wet-bench>`; the same class of scanner on
monitor and product wafers at later steps are on the
{ref}`defect and particle inspection page <machine-defect-inspection>`.

| | Starting material: incoming inspection, marking and sorting |
|---|---|
| What it does | Checks, identifies and sorts incoming polished wafers. KLA calls its Surfscan SP1 scanners the "Industry standard for wafer qualification – wafer manufacturer OQC and wafer fab IQC";[^kla-sp1-2021] SEMI M12 marking "links the properties of the wafer stored in an appropriate database system to each individual wafer for purposes of tracking and control during wafer and device manufacture".[^semi-m12] |
| Surface inspection | Laser light scattering: "Oblique Illumination provides best sensitivity for particle detection on smooth surfaces", "Normal Illumination is ideal for detecting mechanical scratches", and "Haze maps graphically represent full wafer surface conditions / quality".[^kla-sp1-2021] |
| Marking | A laser pulse melts the silicon in a dot;[^pat-lasermark-wacker] "soft marks and hard marks" are the two kinds in use, and GSI's soft Supersoftmark® is "generally characterized as 'debris free'".[^pat-softmark-gsi] A current 200 mm marker places marks "within a 25 mm band around the wafer's circumference", with dot depths of "2.4 μm - 5 μm".[^thinklaser-sigmaclean] |
| Sorting | A sorter reads each wafer's identifier and moves it to its slot;[^pat-sorter-infineon] a current 200 mm model can "split, merge, compress, or create custom wafer mixes by sorting wafers based on their IDs", with an ID reader "for OCR, barcode, or data matrix recognition".[^whs-t4] |
| Standards | SEMI M1 for polished wafers;[^semi-m1] SEMI M12 and M13 for alphanumeric marks, both written so as to allow "simplification of the performance requirements of automatic optical character reading (OCR) equipment".[^semi-m12][^semi-m13] |
| 200 mm era | Tencor and KLA-Tencor Surfscan scanners, from the Surfscan 4000[^liu-1993] to the SP1 DLS "in 200 mm/300 mm wafer process qualification";[^kla-sp1dls-2002] GSI Lumonics WaferMark markers, among them an 8-inch "WaferMark SuperClean" of 1995 vintage.[^cae-wafermark-superclean] |
| SkyWater-listed tool | "Scribe: Lumonics Superclean"[^skw-01] |
| SKY130 steps | 1 step; see {ref}`SKY130 steps assigned to this class <machine-starting-material-steps>` |

## What the machine class is and how it works

The wafers a fab buys are made to SEMI M1, which covers polished
single-crystal silicon wafers,[^semi-m1] and the wafer maker has already
inspected them before shipment: the same scanner family serves the
vendor's outgoing and the fab's incoming quality control.[^kla-sp1-2021]
The fab's own tools therefore do three things before the wafers enter
the process flow: they confirm that the surface is clean and undamaged,
they give each wafer an identity that lasts through the flow, and
they assemble wafers into lots in a known order. The tools share one
constraint: they handle bare, polished wafers, so they must add no
particles, scratches or metal to a surface that no later step will
polish again (industry practice; {ref}`category-substrate`).

### Laser surface scanners

An unpatterned-wafer scanner sweeps a focused laser across the wafer
and collects the light scattered from it. A particle, a pit or a
scratch scatters light into the collectors as a discrete event; the
microroughness of the whole surface gives a continuous background, the
haze. Scanners are calibrated with polystyrene latex spheres of known
size, which do not scatter like real contaminants: Liu, Chae and Bae
found that "Because of the high refractive index of silicon, the wafer
surface scanner detects Si particles to a considerably smaller size than
PSL", so that "Si particles as small as 0.1 μm have been detected by the
Surfscan 4000 with 90% counting efficiency even though the nominal
lower limit of the instrument is 0.3 μm based on PSL
calibration".[^liu-1993] A SEMATECH task force reported that "Silicon
particles are consistently sized incorrectly when the laser surface
scanner is calibrated using standardized procedures utilizing PSL
spheres", and that "Distinguishing false counts caused by surface
microroughness and haze when measuring particles below 0.1 μm has
become a significant concern".[^huff-1997] Haze is itself a
measurement problem: "Microroughness, or haze, on wafer surfaces can
mask the detection of particles", and "Surface roughness is not a unique
number nor is it an intrinsic surface property", which is why Scheer
etched a physical haze standard into silicon.[^scheer-1996]

Current scanners of the class separate these signals with more than one
illumination. KLA's SP1 brochure lists oblique illumination for
particles on smooth surfaces, normal illumination for "mechanical
scratches for equipment monitoring or slip lines for epitaxial
processes", brightfield differential interference contrast for "defects
with surface height changes", and haze maps.[^kla-sp1-2021] The
SP1 DLS, as KLA-Tencor described it in 2002, had a backside inspection
module for "non-destructive inspection of the backsides of patterned
(product) wafers, as well as the front and backsides of unpatterned
wafers".[^kla-sp1dls-2002]

### Pits that look like particles

Not every light-point defect on a new wafer is a particle. Ryuta et al.
showed that SC-1 cleaning forms "a new type of singularity" on the
surface that is "perceived by laser particle counters as small particles
on wafers", corresponding to "small shallow pits caused by the etching
effect of the SC1 cleaning solution", presumed to originate in "some
kind of defect in the melt-grown crystals".[^ryuta-1990] These
crystal-originated particles, or COPs, matter for the gate oxide:
Ishii et al. found that they "consist of single pits and pair pits" and
that "when the gate oxide thickness was around 10 nm, in the active
region pair pits caused gate oxide failure, while single pits did
not",[^ishii-1996] and Miyazaki et al. that "the presence of COP was the
main cause of GOI failure", the original defect being "an octahedral
void".[^miyazaki-1997] A light-point count on a wafer that has seen SC-1
therefore reflects the crystal as well as the particles on it (our
reading; {term}`gate oxide integrity`).

### Laser marking

A wafer identifier is written by melting the silicon with a pulsed
laser. A Wacker Siltronic patent of 1985 describes "contrast rich,
permanent and slag-free characterizations" made by irradiating "a
surface segment corresponding to 1.5 to 6.5 times the surface area of
the desired surface pattern" so that the silicon melts and partially
vaporises "only in the center thereof".[^pat-lasermark-wacker] Marking
can also damage the crystal: Christ and Maurantonio found
that "Laser marking not followed by etching is seen to cause
dislocations and slip patterns in the vicinity of the mark after an
oxidation", and that "Marking done in dot matrix mode exhibits slag
around the dots which is above the plane of the polished
surface".[^christ-1983]

A GSI Group patent distinguishes "roughly two kinds of laser marks
currently used by the industry, namely soft marks and hard marks": its
soft Supersoftmark® is "generally characterized as 'debris free'", is
"typically produced with diode pumped, q-switched pulse laser systems",
and needs the laser to run in a narrow "energy window"; the patent sets
the mark depth by the pulse width.[^pat-softmark-gsi] A shallow soft
mark changes the surface very little: Khoong et al. found soft marks
"invisible by naked eyes under room condition" but visible through
condensation, and traced this to "a thin polycrystalline silicon layer"
with a much lower thermal conductivity.[^khoong-2010]

What is written is standardised. SEMI M12 defines "the geometric and
spatial limits of the alphanumeric code, specifically for serial
identification of flatted and notched silicon wafers";[^semi-m12] SEMI
M13 adds a code with "information on the origin, approximate
resistivity, dopant species, and crystal growth orientation in addition
to a wafer identification number", and "does not address the marking
techniques".[^semi-m13]

### Sorting and identification

A sorter combines a wafer-handling robot, an aligner that finds the
notch, and a reader for the mark. An Infineon patent describes the
logic: wafers in random slots are removed one by one, "The information
carrier of the first wafer is read by a reading device to determine the
position of the first wafer in the sequence", and the wafer is moved to
the slot that corresponds to its position.[^pat-sorter-infineon] A
current 200 mm sorter has "two ergonomic tilt-stage load ports, a linear
robot, and an optical wafer notch/flat aligner", "supports automatic
sorting in 25-slot cassettes", reaches "up to 650 wafers per hour", and
uses SECS/GEM so that "lot and ID tracking" continue through the
fab.[^whs-t4] Scanners can sort as well: the SP1 brochure lists
"Onboard grading capability with up to 4 x 200mm load port sorting
stations".[^kla-sp1-2021]

### Other incoming measurements

The category page lists the other gauges an incoming-quality laboratory
uses: capacitive flatness gauges, four-point-probe resistivity mapping
and FTIR for oxygen ({ref}`category-substrate`). Smits described
four-point-probe sheet resistivity and its correction factors.[^smits-1958] None of these
gauges appears in any SkyWater source retrieved for this page.

## Representative 200 mm-era models

* **Tencor / KLA-Tencor Surfscan.** The Surfscan 4000, whose sizing and
  counting Liu, Chae and Bae evaluated in 1993;[^liu-1993] the
  Surfscan SP1 TBI and SP1 DLS, the latter "Delivers enhanced
  sensitivity in 200 mm/300 mm wafer process qualification" and "enables
  tool-qualification and tool monitoring in 0.13 µm design rules and
  below".[^kla-sp1dls-2002] KLA has since restarted production of the
  SP1 TBI Pro and SP1 DLS Pro for 150–300 mm wafers, quoting sensitivity
  "down to 60nm on the SP1 TBI and 50nm on the SP1 DLS on prime bare
  silicon".[^kla-sp1-2021]
* **Lumonics / GSI Lumonics WaferMark.** GSI describes its WaferMark
  system as "believed to be the first industrial laser marking system on
  silicon wafer", and names the "Wafermark® Sigma Clean®" as the system
  that produces Supersoftmarks.[^pat-softmark-gsi] A used-equipment
  listing offers a "GSI LUMONICS WaferMark SuperClean", "Laser marking
  system, 8"", of 1995 vintage.[^cae-wafermark-superclean] Thinklaser
  USA now describes the SigmaClean as a "debris-free soft marking"
  system for "100 mm to 200 mm wafers", "fully compliant with SEMI
  standards for wafer marking: T7, M12 and M13", with a 1053 nm
  diode-pumped Nd:YLF laser and "240 wph".[^thinklaser-sigmaclean]
* **Sorters.** No 200 mm-era sorter description was retrieved for this
  page; the WHS-T4 above is a current model of the class.[^whs-t4]
* **At the wafer vendor.** The pullers, saws and polishers, and the
  vendors of the period, are on the {ref}`category page
  <category-substrate>`.

## At SkyWater

### What SkyWater lists

SkyWater's *Facilities & Capabilities* page names one tool of this
class. It is the first line of the "Furnaces/Diffusion/Pre-Clean" group
under "Diffusion, Anneal & Implant", above the furnace entries:[^skw-01]

> "Scribe: Lumonics Superclean"

Read term by term: a scribe, which we read as a wafer laser marker, from
Lumonics. "Superclean" matches the model name of the "GSI LUMONICS
WaferMark SuperClean" in a used-equipment listing,[^cae-wafermark-superclean]
so we read the entry as a WaferMark SuperClean; SkyWater gives no model
number, wafer size, laser or mark type. The page lists no laser surface
scanner, flatness or resistivity gauge, or wafer sorter; under "Sort"
it lists "Camtek Falcon (outgoing QA)", which we read as inspection of
finished rather than incoming wafers.[^skw-01] Under "Other Services" it lists "High
resistivity, red phos low resistivity and Silison on Insulator
processing" (sic), which describes substrates the fab offers to process,
not the SKY130 wafer (our reading).[^skw-01]

Two other public SkyWater sources touch the class. A *Defect Technician
2* posting asks for "General operation of semiconductor defect metrology
tools: SEM/AIT/KLA/SP1/EV300/1X", which the step pages read as including
KLA-Tencor SP1 unpatterned-wafer inspection.[^job-06] And the S-1 names
the wafer suppliers: "GlobalWafers Singapore Pte. Ltd. (silicon wafers)"
and "SEH America, subsidiary of Shin-Etsu Handotai, Ltd. (silicon
wafers)".[^sec-01] Cypress's 2015 notice qualified GlobalWafer wafers for
its "130nm C8/R8/S8/L8" products at Fab 4, to be used "in addition to
wafers from other qualified suppliers".[^cyp-06]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the Lumonics listing is **strong**: it is a SkyWater
statement.[^skw-01] The model is our reading of the name. The page does
not say where in any flow the scribe is used; its place at the head of
the furnace and pre-clean group is a layout, not a statement, and the
{ref}`SMAT <step-001>` page grades the entry "strong" while noting that
the page "does not say which step uses it". The SP1 reading rests on a
job posting and is **medium**;[^job-06] the S-1 supplier list is
**strong** for the wafer vendors but names no tool.[^sec-01] The
caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-starting-material-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names incoming
inspection, marking or sorting equipment (identical to the
{ref}`machines index <machines-index>` table):

{ref}`SMAT <step-001>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Scribe: Lumonics Superclean"** — *strong; the step is not stated:* {ref}`SMAT <step-001>`
* **Other classes at the same step** — "SEM/AIT/KLA/SP1/EV300/1X"
  (read as KLA-Tencor AIT and SP1): *medium:* {ref}`SMAT <step-001>`;
  "DNS wet bench industry standard HF/SC1/SC2", "FSI Mercury industry
  standard HF/SC1/SC2 rotational": *inference (the pre-furnace or
  pre-anneal clean; SC-2 is listed only for these two benches):*
  {ref}`SMAT <step-001>`. The full rows, which cover many other steps,
  are on the machines index and the {ref}`wet bench page
  <machine-wet-bench>`.

The SMAT page states that none of these sources ties the tool to that
step: "the association is our inference from the tool's function".

## Consumables and facilities

The wafers and the clean chemicals are listed in the
{ref}`materials index <materials-index>`; what is specific to this
class is summarised here. None of the SkyWater sources describes the
fab's incoming-quality laboratory. The prime and test wafers are
described on the {ref}`substrates and test wafers <material-substrates>`
page.

* **Wafers.** Prime polished wafers, typically to SEMI M1[^semi-m1]
  (industry practice), from suppliers such as those named in the
  S-1,[^sec-01] and test wafers to SEMI M8 for
  monitoring tools ({ref}`category-substrate`).[^semi-m8]
* **Calibration standards.** Polystyrene latex spheres deposited on
  bare wafers, with the sizing errors for real particles described
  above,[^liu-1993][^huff-1997] and haze standards.[^scheer-1996]
* **Marker services.** The SigmaClean specification lists a process
  vacuum, a "Mark Point Exhaust" of "20 CFM (560 I/min) flow rate max",
  air cooling and a limit on static charge;[^thinklaser-sigmaclean] we
  read the mark-point exhaust as removing the vaporised silicon and slag
  that marking produces.[^christ-1983]
* **Carriers.** Open cassettes or SMIF pods, typically with 25
  slots;[^whs-t4] they must not shed particles
  ({ref}`category-substrate`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's wafer specification, incoming
limits and marking scheme are not public.

* **The wafer the class receives.** The {ref}`SMAT <step-001>` page reads
  the wafer as a 200 mm, p-type, bulk polished wafer from the platform
  table and PDK drawings; resistivity, orientation and whether the
  original S8 wafer was epitaxial are open questions there. SkyWater's
  Minnesota fab runs "200 mm equipment".[^skw-01]
* **Where the mark is written.** SEMI M12 and M13 are both written for
  marking "performed by silicon manufacturers",[^semi-m12][^semi-m13]
  and SkyWater lists a
  marker of its own;[^skw-01] whether SKY130 wafers arrive marked, are
  marked at Bloomington, or both, is not public. A mark made before the
  first oxidation must not seed slip ({ref}`BOX <step-002>`, the first
  furnace step on this reference's reading), the failure Christ and Maurantonio saw after oxidation
  of unetched marks;[^christ-1983] a soft mark avoids the slag of a hard
  mark.[^pat-softmark-gsi]
* **Incoming counts and the gate oxides.** COPs are a main cause of
  gate-oxide failure, and pair pits caused failures in oxides of about
  10 nm,[^ishii-1996][^miyazaki-1997] so the incoming
  scan bears on the thick and thin gate oxides of
  {ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>` (our reading; no
  SKY130 COP limit is public).
* **Clean before the first furnace.** The {ref}`SMAT <step-001>` page
  follows receipt with an RCA-type clean, assigned by inference to the
  DNS or FSI Mercury tools ({ref}`machine-wet-bench`), and SC-1 is also
  the solution that reveals COPs as light-point defects.[^ryuta-1990]
* **One scanner class for the whole fab.** The scanner used for incoming
  wafers is the "Industry standard for process tool qualification" as
  well;[^kla-sp1-2021] the machines index lists its particle and defect
  checks on many later steps under
  {ref}`defect and particle inspection <machine-defect-inspection>`
  ({ref}`machines-index`).

## Related pages

* {ref}`category-substrate` — the wafer specification, crystal growth
  and the vendor's equipment.
* {ref}`SMAT <step-001>` — the step this class serves.
* {ref}`machine-wet-bench` — the pre-furnace clean that follows receipt.
* {ref}`machine-defect-inspection` — unpatterned and patterned inspection
  at later steps, with the same class of scanner.
* {ref}`category-test` — in-line defect inspection and electrical test.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — wafers and cleaning chemicals.
* {ref}`material-substrates` — prime, test, monitor and reclaimed
  wafers and their standards.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "Scribe:
  Lumonics Superclean" entry, the absence of incoming inspection and
  sorting tools, and the "Other Services" substrates.[^skw-01]
* SkyWater Technology, Form S-1 (2021) — the silicon-wafer
  suppliers.[^sec-01]
* Cypress Semiconductor, PIN152804 (2015) — GlobalWafer wafers qualified
  for the S8 family at Fab 4.[^cyp-06]
* LinkedIn, SkyWater *Defect Technician 2* posting — the SP1 in the defect
  tool list.[^job-06]
* KLA, *Surfscan SP1TBI Pro / SP1DLS Pro* brochure (2021) — the scanner
  class's illumination modes, haze maps, IQC role and sorting
  stations.[^kla-sp1-2021]
* KLA-Tencor, *Surfscan SP1 DLS* product page (2002 capture) — the 200
  mm/300 mm scanner of the 0.13 µm generation.[^kla-sp1dls-2002]
* Thinklaser USA, *SigmaClean* — a 100–200 mm soft-mark laser marker, its
  SEMI compliance and facilities.[^thinklaser-sigmaclean]
* CAE, *GSI Lumonics WaferMark SuperClean* listing — the model name,
  wafer size and vintage.[^cae-wafermark-superclean]
* Wafer Handling Systems, *WHS-T4* — a 200 mm sorter with notch aligner
  and ID reader.[^whs-t4]
* SEMI M1, M12 and M13 — polished wafers and the alphanumeric wafer
  marks.[^semi-m1][^semi-m12][^semi-m13]

### High-level understanding

* Wikipedia, *Wafer (electronics)* — wafer sizes, thickness and the
  notch.[^wiki-wafer]
* Wikipedia, *KLA Corporation* — the inspection vendor.[^wiki-kla]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — a
  fab-floor view of wafer handling and inspection.[^txt-07]
* SEMI M8 — the looser specification for test wafers.[^semi-m8]
* Shimura, *Semiconductor Silicon Crystal Technology* — the crystal
  defects behind incoming inspection.[^shimura-1989]

### Deep dive

* Liu, Chae and Bae, *JES* 1993 — sizing and counting efficiency of a
  Surfscan 4000 for PSL and real particles.[^liu-1993]
* Huff et al., *JES* 1997 — a SEMATECH study of particle sizing, haze
  and angle-resolved scattering in laser surface scanners.[^huff-1997]
* Scheer, *Proc. SPIE* 1996 — a physical haze and microroughness
  standard.[^scheer-1996]
* Ryuta et al., *JJAP* 1990 — SC-1 pits counted as particles.[^ryuta-1990]
* Ishii et al., *JJAP* 1996 — single and pair COP pits and gate-oxide
  reliability.[^ishii-1996]
* Miyazaki et al., *JJAP* 1997 — COP microstructure and gate-oxide
  integrity.[^miyazaki-1997]
* Christ and Maurantonio, ASTM *Silicon Processing* 1983 — slip, slag
  and particles from laser marks.[^christ-1983]
* Kuhn-Kuhnenfeld, Kramler and Gerber (Wacker Siltronic), US 4,522,656
  — slag-free laser marking by melting only the centre of the irradiated
  spot.[^pat-lasermark-wacker]
* Gu and Ehrmann (GSI Group), US 7,705,268 — soft and hard marks, and
  soft-mark depth set by pulse width.[^pat-softmark-gsi]
* Khoong et al., *JAP* 2010 — the surface change a laser soft mark
  leaves.[^khoong-2010]
* Caspary and Kaulfuss (Infineon), US 6,747,230 — sorting wafers by
  reading their identifiers.[^pat-sorter-infineon]
* Smits, *Bell Syst. Tech. J.* 1958 — four-point-probe resistivity and
  its correction factors.[^smits-1958]
* Kern, *JES* 1990 — the cleaning that incoming wafers receive and the
  equipment that performs it.[^kern-1990]

## Open questions

* What "Lumonics Superclean" is (model, wafer size, soft or hard mark),
  and at which point of the SKY130 flow it is used, are not
  stated.[^skw-01]
* Whether SKY130 wafers are marked by the vendor, at Bloomington or both,
  and to which SEMI mark standard, is not public.
* No incoming surface scanner, flatness or resistivity gauge or wafer
  sorter is named on the capabilities page; the SP1 reading rests on a
  job posting.[^skw-01][^job-06]
* The incoming limits for particles, haze and COPs on the SKY130 wafer
  are not public.
* The model list above is incomplete: it covers the Tencor/KLA-Tencor
  scanners, the GSI Lumonics markers and one current sorter for which a
  public description was found, not the ADE, Hitachi, Topcon and other
  inspection tools, the other laser markers or the 200 mm-era sorters
  of the period.

<!-- footnotes -->

[^kla-sp1-2021]: KLA Corporation, *Surfscan® SP1TBI Pro / SP1DLS Pro:
    Unpatterned Wafer Defect Inspection Systems*, brochure, rev. 1.0,
    2021-05-25, accessed 2026-09-13.
    <https://www.kla.com/documents/products/brochures/Surfscan_SP1.pdf>
[^semi-m12]: SEMI, *SEMI M12 — Specification for Serial Alphanumeric
    Marking of Silicon Wafers*, SEMI Standards store listing, accessed
    2026-09-13.
    <https://store-us.semi.org/products/m01200-semi-m12-specification-for-serial-alphanumeric-marking-of-the-front-surface-of-wafers>
[^pat-softmark-gsi]: B. Gu and J. S. Ehrmann (GSI Group), *Method and
    system for laser soft marking*, US 7,705,268 B2, filed 2005-11-09,
    granted 2010-04-27.
    <https://patents.google.com/patent/US7705268B2/en>
[^thinklaser-sigmaclean]: Thinklaser USA, *SigmaClean: Debris-Free 100 -
    200 mm Wafer Marking*, product page, accessed 2026-09-13.
    <https://www.thinklaserusa.com/sigmaclean>
[^whs-t4]: Wafer Handling Systems, *2-Cassette automation sorter with OCR
    (WHS-T4) 200 mm (8")*, product page, accessed 2026-09-13.
    <https://www.waferhandlingsystems.com/product/2-cassette-automation-sorter-with-ocr-whs-t4-200-mm-8/287/>
[^semi-m1]: SEMI, *SEMI M1 — Specification for Polished Single Crystal
    Silicon Wafers*, SEMI Standards store listing, accessed
    2026-09-18.
    <https://store-us.semi.org/products/m00100-semi-m1-specification-for-polished-single-crystal-silicon-wafers>
[^semi-m13]: SEMI, *SEMI M13 — Specification for Alphanumeric Marking of
    Silicon Wafers*, SEMI Standards store listing, accessed 2026-09-13.
    <https://store-us.semi.org/products/m01300-semi-m13-specification-for-alphanumeric-marking-of-silicon-wafers>
[^liu-1993]: B. Y. H. Liu, S.-K. Chae and G.-N. Bae, "Sizing Accuracy,
    Counting Efficiency, Lower Detection Limit and Repeatability of a
    Wafer Surface Scanner for Ideal and Real‐World Particles", *Journal
    of The Electrochemical Society* **140**(5), 1403–1409 (1993).
    <https://doi.org/10.1149/1.2221569>
[^kla-sp1dls-2002]: KLA-Tencor, *Surfscan SP1 DLS: Unpatterned surface
    inspection*, product page; Wayback Machine capture of 2002-02-08.
    <https://web.archive.org/web/20020208135136/http://www.kla-tencor.com:80/products/defect_control/surfscan-sp1/surfscan.html>
[^cae-wafermark-superclean]: Capital Asset Exchange (CAE), *GSI
    LUMONICS WaferMark SuperClean Marking Machine*, used-equipment
    listing no. 293743883, accessed 2026-09-13.
    <https://caeonline.com/buy/marking-machines/gsi-lumonics-wafermark-superclean/293743883>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; scribe, sort and other-services entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^huff-1997]: H. R. Huff, R. K. Goodall, E. Williams, K.-S. Woo, B. Y. H.
    Liu, T. Warner, D. Hirleman, K. Gildersleeve, W. M. Bullis, B. W.
    Scheer and J. Stover, "Measurement of Silicon Particles by Laser
    Surface Scanning and Angle‐Resolved Light Scattering", *Journal of
    The Electrochemical Society* **144**(1), 243–250 (1997).
    <https://doi.org/10.1149/1.1837392>
[^scheer-1996]: B. W. Scheer, "Development of a physical haze and
    microroughness standard", *Proc. SPIE* **2862**, Flatness, Roughness,
    and Discrete Defect Characterization for Computer Disks, Wafers, and
    Flat Panel Displays, 78–95 (1996). <https://doi.org/10.1117/12.256193>
[^ryuta-1990]: J. Ryuta, E. Morita, T. Tanaka and Y. Shimanuki,
    "Crystal-Originated Singularities on Si Wafer Surface after SC1
    Cleaning", *Japanese Journal of Applied Physics* **29**(11A), L1947
    (1990). <https://doi.org/10.1143/JJAP.29.L1947>
[^ishii-1996]: H. Ishii, S. Shiratake, K. Oka, K. Motonami, T. Koyama and
    J. Izumitani, "Direct Observation of Crystal-Originated Particles on
    Czochralski-Grown Silicon Wafer Surface and Effect on Gate Oxide
    Reliability", *Japanese Journal of Applied Physics* **35**(11A),
    L1385 (1996). <https://doi.org/10.1143/JJAP.35.L1385>
[^miyazaki-1997]: M. Miyazaki, S. Miyazaki, T. Kitamura, Y. Yanase, T.
    Ochiai and H. Tsuya, "Influence of Crystal-Originated 'Particle'
    Microstructure on Silicon Wafers on Gate Oxide Integrity", *Japanese
    Journal of Applied Physics* **36**(10R), 6187 (1997).
    <https://doi.org/10.1143/JJAP.36.6187>
[^pat-lasermark-wacker]: F. Kuhn-Kuhnenfeld, J. Kramler and H.-A. Gerber
    (Wacker Siltronic), *Method of making reference surface markings on
    semiconductor wafers by laser beam*, US 4,522,656 A, filed
    1984-04-26, granted 1985-06-11.
    <https://patents.google.com/patent/US4522656A/en>
[^christ-1983]: M. H. Christ and B. S. Maurantonio, "Influence of Laser
    Marking on Silicon Wafer Properties", in *Silicon Processing*, ASTM
    STP 804, ASTM International, 1983, pp. 62–82.
    <https://doi.org/10.1520/STP36160S>
[^khoong-2010]: L. E. Khoong, Y. C. Lam, H. Y. Zheng and X. Chen, "Laser
    soft marking on silicon wafer", *Journal of Applied Physics*
    **107**(5), 053107 (2010). <https://doi.org/10.1063/1.3319611>
[^pat-sorter-infineon]: D. Caspary and D. Kaulfuss (Infineon
    Technologies), *Method and device for sorting wafers*, US 6,747,230
    B2, filed 2002-09-03, granted 2004-06-08.
    <https://patents.google.com/patent/US6747230B2/en>
[^smits-1958]: F. M. Smits, "Measurement of Sheet Resistivities with the
    Four-Point Probe", *Bell System Technical Journal* **37**(3),
    711–718 (1958). <https://doi.org/10.1002/j.1538-7305.1958.tb03883.x>
[^job-06]: LinkedIn, *SkyWater Technology hiring Defect Technician 2 in
    Bloomington, MN* (job posting), retrieved 2026-09-19.
    <https://www.linkedin.com/jobs/view/defect-technician-2-at-skywater-technology-4434994342>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22; "Raw materials." paragraph re-read from the Wayback
    Machine capture of 2021-04-13 on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^cyp-06]: Cypress Semiconductor, Product Information Notification
    PIN152804, *Qualification of GlobalWafer Silicon Wafers for 250nm,
    130nm and 90nm Technology Products at Cypress Fab 4*, 2015-07-12
    (copy hosted by Future Electronics).
    <https://media.futureelectronics.com/PCN/45887_SPCN.PDF>
[^semi-m8]: SEMI, *SEMI M8 — Specification for Polished Monocrystalline
    Silicon Test Wafers*, SEMI Standards store listing.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^wiki-wafer]: Wikipedia, *Wafer (electronics)*.
    <https://en.wikipedia.org/wiki/Wafer_(electronics)>
[^wiki-kla]: Wikipedia, *KLA Corporation*.
    <https://en.wikipedia.org/wiki/KLA_Corporation>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^shimura-1989]: F. Shimura, *Semiconductor Silicon Crystal Technology*,
    Academic Press, 1989, ISBN 978-0-12-640045-8.
    <https://openlibrary.org/isbn/9780126400458>
[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
