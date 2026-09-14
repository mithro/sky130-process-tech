(machine-duv-krf-stepper)=
# DUV (KrF, 248 nm) stepper or scanner

A KrF exposure tool is the projection printer a 130 nm-era fab uses for
its critical mask levels: active area, gate, contacts, the first metals
and the small vias. It images a reticle onto chemically amplified resist
with 248 nm light from a krypton fluoride excimer laser, through a lens
of high numerical aperture, either a whole field at a time (a
{term}`stepper`) or through a scanned slit (a step-and-scan system, or
scanner). This page describes the class in general, lists
representative 200 mm-era models, and then says what SkyWater has
published about its own tools of this class and which SKY130 steps this
reference assigns to them. The optics, resists, masks and overlay of
lithography in general are on the
{ref}`category page <category-lithography>`, and the i-line tools that
print the other levels on the
{ref}`i-line stepper or scanner page <machine-i-line-stepper>`.

| | DUV (KrF, 248 nm) stepper or scanner |
|---|---|
| What it does | Projects a reticle image onto deep-UV resist with a KrF excimer laser; the "commonly used deep ultraviolet excimer lasers in lithography systems are the krypton fluoride (KrF) laser at 248 nm wavelength and the argon fluoride laser (ArF) at 193 nm wavelength".[^wiki-litho] |
| Light source | A KrF excimer laser, "Type: Cymer ELS6600, Gigaphoton KES-G2OK", "Power: 20 W", "Frequency: Continuously variable up to 2 kHz" on the PAS 5500/750F;[^asml-pas5500-750f] "Type: Cymer 5610", "Power: 10 W", "Frequency: 1 kHz" on the /350C stepper.[^asml-pas5500-350c] |
| NA and resolution | The PAS 5500/750E "achieves 130 nm resolution while using standard 248 nm light" with NA 0.7;[^asml-750e] the /800 "achieves 120 nm resolution by means of the industry-leading numerical aperture (NA) of 0.80";[^asml-800] the Nikon NSR-S204B has NA 0.55–0.68 and "Resolution: 180 nm", "Resolution RET 150 nm".[^nikon-s204b] |
| Field and reduction | Scanner field "Max X: 26.0 mm", "Max Y: 33.0 mm" at 4× (/750F);[^asml-pas5500-750f] "25 x 33 mm2 Field Size" at 4:1 (NSR-S204B);[^nikon-s204b] stepper field "22.0 mm x 22.0 mm" at 4× (/350C)[^asml-pas5500-350c] or "22 mm x 22 mm" at 1:5 (Canon FPA-3030EX6).[^canon-fpa3030ex6] |
| Overlay | "less than 30 nm" (/750E);[^asml-750e] "20 nm in a single machine and 30 nm from machine to machine" (/800);[^asml-800] "Single-machine: ≤ 25 nm", "Matched-machine: ≤ 40 nm" (/750F).[^asml-pas5500-750f] |
| Throughput | "120 200 mm wafer per hour at realistic production conditions of 50 mJ/cm² and 46 exposures fields" (/750E);[^asml-750e] "≥ 130 wph" under the same conditions (/750F);[^asml-pas5500-750f] "200-mm wafers, 70 shots: 88 wph" at 30 mJ/cm² (/350C stepper).[^asml-pas5500-350c] |
| 200 mm era | Nikon's NSR-S201A of 1995, "the first production worthy KrF scanner", and ASML's first step-and-scan tool, the PAS 5500/500, in 1997;[^kato-2007] the PAS 5500/750E (2000) and /800 (2001) for the 130 nm and 120 nm generations.[^asml-750e][^asml-800] |
| SkyWater-listed tool | "ASML DUV stepper", "ASML DUV scanner"; also "ASML 193nm single stage scanner – 90nm CD" and "ASML 193nm twin stage scanner – sub 65nm CD"[^skw-01] |
| SKY130 steps | 14 steps, plus 4 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-duv-krf-stepper-steps>` |

## What the machine class is and how it works

A KrF tool has the same chain of illuminator, reticle stage, reduction
lens, wafer stage, alignment and focus systems as an i-line
tool,[^wiki-stepper] and ASML built both on one PAS 5500 body for
"economic mix-and-match".[^asml-pas5500-750f] What makes a machine a
*KrF* tool is a pulsed laser source at 248 nm, a lens designed for that
wavelength (the early KrF lenses were all-quartz[^pol-1986]) and the
chemically amplified resist it exposes. Das and Sandstrom review the
lasers,[^das-2002] and Bruning the history of the tools.[^bruning-2007]

### Excimer laser source

Excimer lasers for lithography were first demonstrated by Jain, Willson
and Lin, who printed with XeCl and KrF lasers and found the exposure
"∼ 2 orders of magnitude faster" than with conventional lamps.[^jain-1982]
An excimer laser "typically uses a combination of a noble gas ( argon ,
krypton , or xenon ) and a reactive gas ( fluorine or chlorine
)";[^wiki-excimer] Das and Sandstrom note that excimer lasers are
"capable of operating with narrow spectral widths" and have "a low
degree of coherence".[^das-2002] The laser stands apart from the
exposure tool: ASML specifies "20-m remote capability" for the beam
delivery.[^asml-pas5500-350c] The laser's bandwidth adds to the lens
aberrations: Lalovic et al. measured "a positive relationship" between
wavefront aberration and laser bandwidth on a 0.6 NA stepper and
scanner.[^lalovic-2001] Kato's chronology records Cymer's first
prototype lithography laser of 1988 at "200Hz rep. rate, output power of
3W", its first solid-state-switched laser of 1995 at 600 Hz and 6 W, and
a market share of more than 80 % "during the 90s and until early
00's".[^kato-2007] By 2000 the 130 nm scanners used "A 2 kHz, 20 W
laser".[^asml-750e]

### Projection lens and resolution

The early KrF steppers had modest apertures: an all-quartz 5× lens of NA
0.20–0.38 giving "a practical resolution of 0.5μm" in Pol et al.'s
modified stepper of 1986,[^pol-1986] and a "5x reduction lens with NA
0.42 and 21.2 mm field size" in Wittekoek et al.'s stepper of
1990.[^wittekoek-1990] By the 130 nm generation the NA had risen to 0.7
and 0.8 (quick facts above), with variable NA and illumination set per
layer: the PAS 5500/750E had "the highest partial coherence (0.88)" and
a "QUASAR module, which enables multipole illumination", to "optimize
their depth of focus and exposure latitude process window and reduce
mask error factors".[^asml-750e] At 248 nm and NA 0.7, λ/NA is about 354
nm, so the 130 nm resolution ASML quotes corresponds to {term}`k1` ≈
0.37 (our arithmetic with the relation on the
{ref}`category page <category-lithography>`). The depth of focus shrinks
with the square of NA, a scaling Lin refined for high-NA
lenses;[^lin-2002] below {math}`k_1 \approx 0.4` resolution-enhancement
techniques are needed ({ref}`category-lithography`), and Lin showed
phase shifting feasible to 0.18 µm at {math}`k_1 = 0.35`, 248 nm and NA
0.5.[^lin-1993] ASML specifies the /750F's CD through focus: CD
uniformity "≤ 10 nm" at best focus and "≤ 15 nm" "Over 0.4-µm defocus"
for 0.13 µm lines and spaces.[^asml-pas5500-750f]

### Stepper and step-and-scan

A KrF stepper exposes a square field at once (22.0 mm × 22.0 mm on the
/350C);[^asml-pas5500-350c] a scanner exposes a slit and scans the
reticle and wafer stages in step, over a 26 mm × 33 mm field on the ASML
and 25 mm × 33 mm on the Nikon tools.[^asml-pas5500-750f][^nikon-s204b]
Step-and-scan began with the Micrascan, developed by Perkin-Elmer and
introduced by SVG Lithography in 1990;[^kato-2007] Buckley, Galburt and
Karatzas described a 4:1 ring-field step-and-scan tool scanning 20 mm ×
32.5 mm subfields in 1989.[^buckley-1989] The early Micrascans used
lamps, and the Micrascan III of 1996 was SVGL's "first KrF laser based
DUV scanner".[^kato-2007] De Zwart et al. reported in 1997 on a
step-and-scan system "capable of exposing 26 X 33 mm fields, using a 248
nm DUV-lens with a variable Numerical Aperture of 0.40 to 0.63", whose
overlay and dose accuracy "at high scanning speeds" proved the
technology ready "for use in high volume sub 0.25 micrometers
manufacturing".[^de-zwart-1997] The scanner's advantages ASML lists are
"Large field size, better CD control and lower lens
aberrations".[^asml-pas5500-750f] Steppers remained on sale beside
scanners: ASML describes its /350C as "a very cost-effective
mix-and-match lithography solution when used in conjunction with other
ASML PAS 5500 i-line and DUV steppers".[^asml-pas5500-350c]

### Alignment, levelling and overlay

The tool aligns each wafer to marks from an earlier level. Wittekoek et
al.'s KrF stepper used through-the-lens alignment "with direct
referencing of reticle to wafer operating at 633 nm", with correction
optics for the
focal difference between the alignment and exposure
wavelengths;[^wittekoek-1990] Tanimoto et al. used off-axis alignment
with He–Ne laser spots and "EGA (Enhanced Global Alignment)", reaching
overlay "better than 0.18μm" in 1989.[^tanimoto-1989] By 2000 ASML added
"ATHENA dual-wavelength, high-order alignment" to widen "alignment
process latitude on today's most advanced process layers such as
tungsten CMP",[^asml-750e] and Laidler et al. evaluated it on shallow
trench isolation, tungsten CMP and copper dual-damascene
levels.[^laidler-2002] The Nikon NSR-S204B lists "Laser Step Alignment
(LSA)" and "Field Image Alignment (FIA)".[^nikon-s204b] Every field is
levelled before or during exposure: the /750F has an "8-Spot Level
Sensor",[^asml-pas5500-750f] the NSR-S204B a "Real Time focus/level
sensor".[^nikon-s204b]

### Resist and airborne amines

KrF resists are chemically amplified: a photo-generated acid removes
protecting groups catalytically during the post-exposure bake, the
concept Ito and Willson applied to resists for semiconductor
manufacturing.[^ito-1984] The same catalysis makes them fragile.
MacDonald et al. found that a t-BOC/onium salt resist "is severely
degraded by vapor from organic bases", visible after "15 minutes in air
containing as little as 15 parts per billion (ppb) of an organic base",
and cured it with "a specially designed, high efficiency carbon
filter".[^macdonald-1991] The NSR-S204B lists "Nitrogen Purge" and
"Chemical Filters" in its system structure.[^nikon-s204b]

## Representative 200 mm-era models

* **ASML.** Its first KrF stepper, the PAS 5000/70 of 1991, had NA
  0.42;[^kato-2007] its first step-and-scan tool, the PAS 5500/500 of 1997,
  had "a resolution of 0.22µm, with 96wph throughput
  (200mm)".[^kato-2007] The PAS 5500/350C is "a Deep UV stepper for
  0.15-µm applications and beyond".[^asml-pas5500-350c] The PAS 5500/750E
  of 2000 was "the semiconductor industry's first KrF (248 nm wavelength)
  lithography system optimized for high-volume production of ICs with 130
  nm design rules";[^asml-750e] the /750F "enables 130-nm mass production
  using mature 248-nm KrF technology";[^asml-pas5500-750f] the /800 of 2001
  extended KrF to 120 nm,[^asml-800] and the /850C "enables 110-nm mass
  production".[^asml-pas5500-850c]
* **Nikon.** The NSR-1505EX of 1988, "an R&D tool for early learning of DUV
  lithography" with NA 0.42, and the NSR-S201A of 1995, "the first
  production worthy KrF scanner in the industry".[^kato-2007] The
  NSR-S202A scanning stepper achieved "sub-quarter micron resolution" and
  "80 wafers per hour with 8 in. wafers".[^nikon-s202a-s102b] The NSR-S204B
  specification summary cited here (a reseller copy) describes a unit
  manufactured in June 2002 and configured for 300 mm
  wafers.[^nikon-s204b]
* **Canon.** The FPA-4000ES1 of 1997 was "Canon's first KrF scanning
  stepper".[^kato-2007] The FPA-3000EX4, a 5× KrF stepper of NA 0.6, was
  still used in 2014 "for photolithography of all layers" of a 200 mm
  superconductor process;[^tolpygo-2014] Canon's current FPA-3030EX6,
  which inherits the performance of the FPA-3000EX6, gives "resolution
  (150 nm), overlay accuracy (25 nm) and productivity (throughput *121
  wph)".[^canon-fpa3030ex6]
* **SVG Lithography.** The Micrascan III (1996), with NA 0.6 and 0.25 µm
  resolution; SVGL's Micrascan line was discontinued in 2001 after ASML
  acquired the company.[^kato-2007]

## At SkyWater

### What SkyWater lists

Under "Lithography", SkyWater's *Facilities & Capabilities* page lists
four deep-UV exposure tools:[^skw-01]

> "ASML DUV stepper"
>
> "ASML DUV scanner"
>
> "ASML 193nm single stage scanner – 90nm CD"
>
> "ASML 193nm twin stage scanner – sub 65nm CD"

followed by "Overlay down to single digit nm" and "Max field size 26mm x
32mm", and, in the "Special Modules" group, "Photo stitching in both X
and Y directions, sub-20nm stitching errors".[^skw-01] Read term by
term: "DUV" names no wavelength; the step pages read "ASML DUV stepper"
and "ASML DUV scanner" as 248 nm (KrF) tools, as the
{ref}`machines index <machines-index>` records, and that the list gives
the two 193 nm scanners as separate entries is consistent with that
reading (our reading). The 193 nm entries give a CD each and distinguish
a "single stage" from a "twin stage" scanner; ASML's TWINSCAN platform
was introduced in 2000,[^kato-2007] and SkyWater's engineer profile
names "the ASML TWINSCAN" among "More advanced tools" that "are always
arriving",[^skw-06] but that the twin-stage entry is a TWINSCAN is our
inference. None of the entries gives a model, NA or tool count, and the
overlay and field lines name no tool.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listings are **strong**: they are SkyWater statements.[^skw-01] The
caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. For
this class the caveat about the age of the list matters most: the page
describes a site "Recently expanded in 2020 to enable additional
capacity and Cu back end of line" with "90 nm + feature
geometries",[^skw-01] the 193 nm entries give 90 nm and sub-65 nm CDs,
and the {ref}`P1M <step-061>` page sets them aside as "not evidence for
how the 130 nm gate was, or is, printed". The engineer profile
corroborates an ASML TWINSCAN tool on the floor but not its wavelength
or use.[^skw-06]

(machine-duv-krf-stepper-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a KrF stepper or
scanner as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`FOM <step-004>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`MM3 <step-139>`, {ref}`VIM3 <step-144>`, {ref}`MM4 <step-154>`, {ref}`VIM4 <step-159>`; *alternative:* {ref}`DNM <step-007>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"ASML DUV stepper", "ASML DUV scanner"** — *inference:* {ref}`FOM <step-004>`, {ref}`P1M <step-061>`, {ref}`NPCM <step-078>`, {ref}`LICM1 <step-093>`, {ref}`LI1M <step-102>`, {ref}`CTM1 <step-107>`, {ref}`MM1 <step-113>`, {ref}`VIM <step-118>`, {ref}`MM2 <step-124>`, {ref}`VIM2 <step-129>`, {ref}`VIM3 <step-144>`, {ref}`VIM4 <step-159>`; *not public which class (i-line or DUV):* {ref}`MM3 <step-139>`, {ref}`MM4 <step-154>`
* **"ASML 193nm single stage scanner – 90nm CD", "ASML 193nm twin stage scanner – sub 65nm CD"** — *not evidence for the 130 nm gate (a later addition):* {ref}`P1M <step-061>`

The inferences rest on the design rules and on one mask-type record, not
on any SkyWater statement. In Table 2 of the PDK's *Criteria &
Assumptions* the minimum features of these masks are 0.14–0.2 µm for
active, gate spacing, local interconnect, contact, metals 1–2 and vias
1–3 ({ref}`masks-index`),[^pdk-03] which the step pages find too small
for production i-line imaging. Via 4, at 0.8 µm, is assigned here only
because the process-steps sheet records for its plate a mask type we
read as a binary mask for 248 nm exposure; for vias 2 and 3 it records
types we read as embedded attenuated phase-shift masks for 248
nm.[^steps-sheet] The sheet names no exposure tool.

## Consumables and facilities

The process gases are described on the
{ref}`process gases <material-process-gases>` page.
The lithography consumables are described on the
{ref}`lithography materials <material-lithography-materials>` page and
listed in the {ref}`materials index <materials-index>`; what is specific to a KrF
exposure tool is summarised here. None of the SkyWater sources describes
the fab's laser gases, laser service or tool environment.

* **Laser gas and laser modules.** Excimer lasers "are usually filled with
  inert and halide gases (Kr, Ar, Xe, F and Cl)";[^wiki-litho] a KrF laser
  runs on a krypton and fluorine mixture.[^wiki-excimer] Laser power and
  repetition rate set throughput, and ASML advertises "Variable Laser
  Frequency Control" for "the lowest possible laser cost of
  operation".[^asml-pas5500-850c]
* **Purge and chemical filtration.** Nitrogen purge and chemical filters
  in
  the tool environment[^nikon-s204b] protect chemically amplified
  resist from airborne bases (inference from the base sensitivity
  MacDonald et al. measured).[^macdonald-1991]
* **KrF resist and BARC.** Chemically amplified positive
  resists[^ito-1984] with organic anti-reflective coatings
  ({ref}`category-lithography`); SkyWater's S-1 names "Tokyo Ohka Kogyo
  America, Inc. (photoresist)" among its suppliers without tying a resist
  to a level.[^sec-01] The throughput figures above assume doses of
  30–50 mJ/cm².[^asml-pas5500-350c][^asml-750e]
* **Reticles.** Six-inch reticles, binary or attenuated phase-shift; the
  process-steps sheet records mask-type codes for the via 2, via 3 and
  via 4 plates that we read as 248 nm types, and for no other plates
  ({ref}`masks-index`).[^steps-sheet] SkyWater lists
  "Mask GDS to reticle" and "OPC modeling" among its
  services.[^skw-01]
* **Track link.** The NSR-S204B lists an "In-Line Track
  Interface",[^nikon-s204b] the connection to the
  {ref}`coat/develop track <machine-coat-develop-track>` that bakes and
  develops the exposed wafer.

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's exposure tools, illumination
settings and resists per layer are not public.

* **The gate level.** The {ref}`P1M <step-061>` page puts the 0.15 µm
  gate at {math}`k_1 \approx 0.36–0.42` on a KrF lens of NA 0.6–0.7, "within
  reach of a KrF tool with resolution enhancement", against 0.25–0.29
  on an i-line tool. A 130 nm-generation KrF scanner such as the /750E was
  built for that regime.[^asml-750e]
* **Active and nitride cut.** {ref}`FOM <step-004>` and
  {ref}`NPCM <step-078>` are assigned to this class with an i-line
  alternative ("if the layer were relaxed", in the FOM page's words). The
  later implant masks, most of them i-line levels, must overlay the
  active and gate patterns, so the KrF levels set the grid the i-line
  tools align to (inference; the alignment tree is not public;
  {ref}`machine-i-line-stepper`).
* **Contacts and vias.** The local-interconnect contact, contact and via
  masks print isolated holes, the hardest KrF pattern; the
  {ref}`VIM2 <step-129>` page finds {math}`k_1 \approx 0.56` for the 0.2 µm
  via 2, and the process-steps sheet's mask types for vias 2 and 3 read as
  embedded attenuated phase-shift masks.[^steps-sheet][^lin-1993]
* **Via 4 and mixed tools.** If via 4 is exposed on a KrF tool, as the
  {ref}`VIM4 <step-159>` page infers from its plate record, the i-line
  {ref}`MM5 <step-162>` level above it overlays a KrF level, and matched
  overlay between classes applies ({ref}`machine-i-line-stepper`). Why a
  0.8 µm via would have a mask type we read as 248 nm is not stated.[^steps-sheet]
* **Alignment on polished levels.** On this reference's readings
  ({ref}`category-cmp`), from {ref}`LICM1 <step-093>` upward the KrF
  levels are printed over polished surfaces: the
  local-interconnect and metal masks over polished tungsten plugs, the
  contact and via masks over polished oxide — the cases ATHENA alignment
  was meant to widen latitude on.[^asml-750e][^laidler-2002]
* **Amine-free handling.** KrF resist must be exposed and baked without
  delay in filtered air;[^macdonald-1991] which of SkyWater's three tracks
  is linked to which exposure tool is not public.

## Related pages

* {ref}`category-lithography` — optics, resists, masks and overlay, and
  the 36 mask steps of SKY130.
* {ref}`machine-i-line-stepper` — the exposure class for the other levels
  and the mix-and-match between classes.
* {ref}`machine-coat-develop-track` — the linked track that coats, bakes
  and develops the KrF resist.
* {ref}`machine-cd-sem-overlay-metrology` — the CD and overlay
  measurements that feed corrections back to the exposure tool.
* {ref}`masks-index` — each mask's PDK entry, minimum CD, plates and the
  mask-type record for vias 2–4.
* {ref}`mask-p1m` and {ref}`mask-vim4` — per-mask pages for the gate
  mask and the via-4 mask, both assigned to this class; {ref}`mask-dnm`
  for the deep N-well mask, for which it is the alternative.
* {ref}`mask-licm1`, {ref}`mask-li1m`, {ref}`mask-ctm1`, {ref}`mask-mm1`,
  {ref}`mask-vim` and {ref}`mask-mm2` — per-mask pages for the
  local-interconnect contact, local-interconnect, contact, metal-1, via-1
  and metal-2 masks, all assigned to this class.
* {ref}`mask-fom` — the per-mask page for the field-oxide mask, assigned
  to this class.
* {ref}`mask-vim2` and {ref}`mask-vim3` — per-mask pages for the via-2
  and via-3 masks, both assigned to this class, whose recorded mask type
  reads as a 248 nm attenuated phase-shift mask.
* {ref}`mask-mm3` and {ref}`mask-mm4` — per-mask pages for the metal-3 and
  metal-4 masks, for which the step pages leave the class open between
  this one and i-line.
* {ref}`mask-rpm`, {ref}`mask-rrpm` and {ref}`mask-urpm` — per-mask pages
  for the three poly-resistor masks, for which it is the alternative.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — resists, anti-reflective coatings, developer
  and laser consumables.
* {ref}`material-lithography-materials` — resists, coatings, developer,
  solvents, reticles and light-source consumables.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the DUV and 193 nm
  exposure-tool entries and the rest of the lithography group.[^skw-01]
* SkyWater Technology, *A Day in the Life of a SkyWater Engineer* — an
  ASML TWINSCAN among newly arriving tools.[^skw-06]
* SkyWater PDK, *Criteria & Assumptions* — the minimum CDs behind the step
  pages' class assignments.[^pdk-03]
* *S8 / SKY130 Process Steps* sheet — the via mask types read as 248 nm
  types.[^steps-sheet]
* ASML, PAS 5500/750E press release (2000) — the first KrF scanner for
  130 nm: NA, illumination, ATHENA alignment, laser, overlay and
  throughput.[^asml-750e]
* ASML, PAS 5500/800 press release (2001) — NA 0.80, 120 nm resolution
  and matched-machine overlay.[^asml-800]
* ASML, *PAS 5500/350C*, */750F* and */850C* data sheets — a KrF stepper
  and two KrF scanners with their lasers, fields, overlay and
  throughput.[^asml-pas5500-350c][^asml-pas5500-750f][^asml-pas5500-850c]
* Nikon, *NSR-S204B* specification summary — lens, laser, alignment and
  environment of a KrF scanner.[^nikon-s204b]
* Nikon, NSR-S202A and NSR-S102B announcement — a KrF scanning stepper
  paired with an i-line one.[^nikon-s202a-s102b]
* Canon, *FPA-3030EX6* product page — a current 200 mm KrF
  stepper.[^canon-fpa3030ex6]
* Tolpygo et al., arXiv 2014 — a Canon FPA-3000EX4 used for all layers of
  a 200 mm process.[^tolpygo-2014]
* SkyWater Technology, Form S-1 (2021) — photoresist suppliers; no
  exposure-tool vendor.[^sec-01]

### High-level understanding

* Wikipedia, *Photolithography* — excimer laser lithography and its
  lasers.[^wiki-litho]
* Wikipedia, *Excimer laser* — gas mixtures and wavelengths.[^wiki-excimer]
* Wikipedia, *Stepper* — subassemblies, stepping and
  scanning.[^wiki-stepper]
* Kato, *Chronology of Lithography Milestones* (2007) — dates of the first
  KrF steppers, scanners and lasers.[^kato-2007]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — DUV lithography
  for the 0.25–0.13 µm generations.[^txt-05]
* Levinson, *Principles of Lithography*, 4th ed. — exposure tools,
  resists and overlay.[^levinson-2019]

### Deep dive

* Jain, Willson and Lin, *IEEE EDL* 1982 — the first excimer laser
  lithography.[^jain-1982]
* Pol et al., *Proc. SPIE* 1986 — a KrF stepper built from a commercial
  step-and-repeat tool.[^pol-1986]
* Tanimoto et al., *Proc. SPIE* 1989 — an excimer laser stepper with a
  line-narrowed KrF laser and global alignment.[^tanimoto-1989]
* Wittekoek et al., *Proc. SPIE* 1990 — a KrF stepper with through-the-lens
  reticle-to-wafer alignment.[^wittekoek-1990]
* Buckley, Galburt and Karatzas, *JVST B* 1989 — step-and-scan lithography
  with reduction optics.[^buckley-1989]
* De Zwart et al., *Proc. SPIE* 1997 — performance of a 248 nm
  step-and-scan system.[^de-zwart-1997]
* Das and Sandstrom, *Proc. IEEE* 2002 — excimer laser technology for
  lithography.[^das-2002]
* Lalovic et al., *Proc. SPIE* 2001 — wavefront aberration against laser
  bandwidth on KrF tools.[^lalovic-2001]
* Laidler et al., *Proc. SPIE* 2002 — ATHENA alignment on STI, tungsten
  CMP and copper levels.[^laidler-2002]
* Ito and Willson, *ACS Symp. Ser.* 1984 — chemically amplified
  resists.[^ito-1984]
* MacDonald et al., *Proc. SPIE* 1991 — airborne base contamination of a
  chemically amplified resist.[^macdonald-1991]
* Lin, *J. Micro/Nanolith. MEMS MOEMS* 2002 — resolution and depth-of-focus
  scaling with NA.[^lin-2002]
* Lin, *IEEE Circuits and Devices* 1993 — phase-shifting masks at
  248 nm.[^lin-1993]
* Bruning, *Proc. SPIE* 2007 — forty years of optical lithography
  tools.[^bruning-2007]

## Open questions

* How many KrF steppers and scanners SkyWater has, their models and NA,
  and whether "DUV" means 248 nm for both entries, are not
  stated.[^skw-01]
* Which SKY130 levels are printed on the KrF stepper and which on the KrF
  scanner, whether metal 3 and metal 4 are KrF or i-line levels, and why
  the 0.8 µm via 4 would have a mask type we read as 248 nm, are not
  public.
* Whether any SKY130 level is now printed on the 193 nm scanners, and
  which tool the "Overlay down to single digit nm" and "Max field size
  26mm x 32mm" lines describe, are not stated.[^skw-01]
* Whether the MPW reticle frame, whose 42 positions the public renders
  lay out as six rows and seven columns of dies, is printed in one
  scanner field or by stepping or stitching is not public; the renders do
  not model reticle pitch or the fab's frame ({ref}`masks-renders`).
* The model list above is incomplete: it covers the ASML, Nikon, Canon
  and SVG Lithography KrF tools for which a public description was found,
  not every KrF exposure tool of the period.

<!-- footnotes -->

[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^asml-pas5500-750f]: ASML, *PAS 5500/750F DUV Step and Scan*,
    refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-750f.pdf>
[^asml-pas5500-350c]: ASML, *PAS 5500/350C* (Deep UV stepper),
    refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-350c.pdf>
[^asml-pas5500-850c]: ASML, *PAS 5500/850C DUV Step-and-Scan*,
    refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-850c.pdf>
[^asml-750e]: ASML, *ASML introduces KrF lithography scanner* (PAS
    5500/750E), press release, 2000-04-04.
    <https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
[^asml-800]: ASML, *ASML introduces new KrF Step & Scan system* (PAS
    5500/800), press release, 2001-01-31.
    <https://www.asml.com/en/news/press-releases/2001/asml-introduces-new-krf-step-and-scan-system-that-extends>
[^nikon-s204b]: Nikon, *NSR-S204B 248 nm Scanner Exposure System
    Overview* (specification summary, reseller copy), attached to the
    listing Tara Semiconductor Technology, *Used 2002 NIKON S204 Scanner*
    (listing LITV25-01), accessed 2026-09-13.
    <https://f.machineryhost.com/fc49306d97602c8ed1be1dfbf0835ead/aa008f2897d7d4a224ff92839b4299e9/SpecSummary_LITV25-01_NSR-S204B.pdf>,
    <https://www.tarasemi.com/listings/5223879-used-2002-nikon-s204-scanner>
[^canon-fpa3030ex6]: Canon Inc., *FPA-3030EX6: KrF Stepper for IoT
    devices*, product page, accessed 2026-09-13.
    <https://global.canon/en/product/indtech/semicon/fpa3030ex6.html>
[^kato-2007]: A. Kato, *Chronology of Lithography Milestones*, version
    0.9, May 2007, hosted on lithoguru.com, accessed 2026-09-13.
    <https://www.lithoguru.com/scientist/litho_history/Kato_Litho_History.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-stepper]: Wikipedia, *Stepper*.
    <https://en.wikipedia.org/wiki/Stepper>
[^das-2002]: P. Das and R. L. Sandstrom, "Advances in excimer laser
    technology for sub-0.25-μm lithography", *Proceedings of the IEEE*
    **90**(10), 1637–1652 (2002). <https://doi.org/10.1109/JPROC.2002.803665>
[^bruning-2007]: J. H. Bruning, "Optical lithography: 40 years and
    holding", *Proc. SPIE* **6520**, 652004 (2007).
    <https://doi.org/10.1117/12.720631>
[^jain-1982]: K. Jain, C. G. Willson and B. J. Lin, "Ultrafast deep UV
    lithography with excimer lasers", *IEEE Electron Device Letters*
    **3**(3), 53–55 (1982). <https://doi.org/10.1109/EDL.1982.25476>
[^wiki-excimer]: Wikipedia, *Excimer laser*.
    <https://en.wikipedia.org/wiki/Excimer_laser>
[^lalovic-2001]: I. Lalovic, A. Kroyan, N. R. Farrar, D. Taitano, P.
    Zambon and A. H. Smith, "Investigation of cross-field wavefront
    aberrations of KrF lithography exposure systems as a function of
    excimer laser bandwidth", *Proc. SPIE* **4346**, 1262 (2001).
    <https://doi.org/10.1117/12.435655>
[^pol-1986]: V. Pol, J. H. Bennewitz, G. C. Escher, M. Feldman, V. A.
    Firtion, T. E. Jewell, B. E. Wilcomb and J. T. Clemens, "Excimer
    laser-based lithography: a deep ultraviolet wafer stepper", *Proc.
    SPIE* **0633**, 6 (1986). <https://doi.org/10.1117/12.963697>
[^wittekoek-1990]: S. Wittekoek, M. A. van den Brink, H. F. Linders, J. M.
    D. Stoeldraijer, J. W. Martens and D. R. Ritchie, "Deep-UV wafer
    stepper with through-the-lens wafer to reticle alignment", *Proc.
    SPIE* **1264**, 534 (1990). <https://doi.org/10.1117/12.20207>
[^lin-2002]: B. J. Lin, "The k₃ coefficient in nonparaxial λ/NA scaling
    equations for resolution, depth of focus, and immersion lithography",
    *Journal of Micro/Nanolithography, MEMS, and MOEMS* **1**(1), 7–12
    (2002). <https://doi.org/10.1117/1.1445798>
[^lin-1993]: B. J. Lin, "Phase-shifting masks gain an edge", *IEEE
    Circuits and Devices Magazine* **9**(2), 28–35 (1993).
    <https://doi.org/10.1109/101.200850>
[^buckley-1989]: J. D. Buckley, D. N. Galburt and C. Karatzas,
    "Step-and-scan lithography using reduction optics", *Journal of
    Vacuum Science & Technology B* **7**(6), 1607–1612 (1989).
    <https://doi.org/10.1116/1.584499>
[^de-zwart-1997]: G. de Zwart, M. A. van den Brink, R. A. George, D.
    Satriasaputra, J. Baselmans, H. Butler, J. B. van Schoot and J. de
    Klerk, "Performance of a step-and-scan system for DUV lithography",
    *Proc. SPIE* **3051**, 817 (1997). <https://doi.org/10.1117/12.276002>
[^tanimoto-1989]: A. Tanimoto, A. Miyaji, Y. Ichihara, T. Uemura and I.
    Tanaka, "Excimer laser stepper for sub-half micron lithography",
    *Proc. SPIE* **1088**, 434 (1989). <https://doi.org/10.1117/12.953172>
[^laidler-2002]: D. W. Laidler, H. J. L. Megens, S. Lalbahadoersing,
    R. J. F. van Haren and F. Bornebroek, "Advances in process overlay:
    ATHENA alignment system performance on critical process layers",
    *Proc. SPIE* **4689**, 397 (2002). <https://doi.org/10.1117/12.473478>
[^ito-1984]: H. Ito and C. G. Willson, "Applications of Photoinitiators to
    the Design of Resists for Semiconductor Manufacturing", *ACS Symposium
    Series* **242**, 11–23 (1984).
    <https://doi.org/10.1021/bk-1984-0242.ch002>
[^macdonald-1991]: S. A. MacDonald, N. J. Clecak, H. R. Wendt, C. G.
    Willson, C. D. Snyder, C. J. Knors, N. B. Deyoe, J. G. Maltabes, J. R.
    Morrow, A. E. McGuire and S. J. Holmes, "Airborne chemical contamination
    of a chemically amplified resist", *Proc. SPIE* **1466**, 2–12 (1991).
    <https://doi.org/10.1117/12.46354>
[^nikon-s202a-s102b]: Semiconductor Online, *Two Scanning Steppers*
    (Nikon Precision Europe announcement of the NSR-S202A and NSR-S102B),
    undated, accessed 2026-09-13.
    <https://www.semiconductoronline.com/doc/two-scanning-steppers-0001>
[^tolpygo-2014]: S. K. Tolpygo et al., "Fabrication Process and
    Properties of Fully-Planarized Deep-Submicron Nb/Al-AlOx/Nb Josephson
    Junctions for VLSI Circuits", arXiv:1408.5829 (2014) — describes a
    Canon FPA-3000EX4 248 nm stepper with 5× reduction and NA 0.6.
    <https://arxiv.org/abs/1408.5829>
[^skw-06]: SkyWater Technology, *A Day in the Life of a SkyWater
    Engineer* (R&D/OPC engineer profile), 2024-09-04, retrieved
    2026-09-13.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-engineer/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation (Table 2).
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tab "Sheet4" (mask types), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^levinson-2019]: H. J. Levinson, *Principles of Lithography*, 4th ed.,
    SPIE Press, 2019, ISBN 978-1-5106-2760-4.
    <https://doi.org/10.1117/3.2525393>
