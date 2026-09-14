(machine-i-line-stepper)=
# i-line stepper or scanner

An i-line exposure tool is the projection printer a fab uses for the
mask levels that do not need deep-ultraviolet resolution: implant
blocks, relaxed etch masks, capacitor plates, the thick upper metal and
the pad opening. It images a reticle onto resist-coated wafers with the
365 nm line of a mercury lamp, either a whole field at a time (a
{term}`stepper`) or through a scanned slit (a step-and-scan system, or
scanner). In a 200 mm, 130 nm-era fab it shares the line with
{ref}`KrF tools <machine-duv-krf-stepper>`, which print the critical
levels, and the two must overlay each other. This page describes the
class in general, lists representative 200 mm-era models, and then says
what SkyWater has published about its own tools of this class and which
SKY130 steps this reference assigns to them. The optics, resists and
overlay of lithography in general are on the
{ref}`category page <category-lithography>`.

| | i-line stepper or scanner |
|---|---|
| What it does | Projects a reticle image onto resist at 365 nm, the mercury "i-line";[^wiki-litho] a stepper exposes one field and steps the wafer to the next ("the stepper imaged only one chip at a time"),[^wiki-stepper] a step-and-scan system scans reticle and wafer through a slit on separate, synchronised stages.[^buckley-1989] |
| Light source | A super-high-pressure mercury lamp, whose spectrum "is filtered to select a single spectral line";[^wiki-litho] Ushio's lithography lamps are built to use "three ultraviolet wavelengths (436, 405 and 365 nm)".[^ushio-uv-lamps] ASML gives a "1.5-kW illuminator" for the PAS 5500/100D and a "3.5-kW AERIAL Illuminator" for the /275D.[^asml-pas5500-100d][^asml-pas5500-275d] |
| NA and resolution | NA "0.48—0.60 (variable)" and "Resolution: 0.40 µm" (PAS 5500/100D);[^asml-pas5500-100d] "Resolution: ≤ 0.28 µm" at the same NA range (/275D);[^asml-pas5500-275d] NA "0.45-0.63 Variable", resolution "Less than 0.35 micron" (Canon FPA-3000i5+);[^canon-fpa3000i5plus-1998] "Resolution: ≤ 220 nm" (/450F scanner).[^asml-pas5500-450f] |
| Field and reduction | Stepper field "Max X: 22.0 mm", "Max Y: 27.4 mm" (/275D);[^asml-pas5500-275d] "Exposure Field 22 x 22mm" at "5:1" (FPA-3000i5+);[^canon-fpa3000i5plus-1998] scanner field "Max X: 26.0 mm", "Max Y: 33.0 mm" with a "4X reduction lens" (PAS 5500/450F).[^asml-pas5500-450f] |
| Overlay | "Single-machine: ≤ 40 nm" and "Matched to PAS 5500/275: ≤ 80 nm" (/275D);[^asml-pas5500-275d] "Less than 40nm (\|m\|+3sigma)" alignment accuracy (FPA-3000i5+).[^canon-fpa3000i5plus-1998] |
| Throughput | "200-mm wafers, 70 shots: ≥ 100 wph" at 200 mJ/cm² (/275D);[^asml-pas5500-275d] "200-mm wafers, 46 shots: ≥ 150 wph" (/450F scanner);[^asml-pas5500-450f] "100 WPH (8-inch wafer, 90mJ/cm2)" (FPA-3000i5+).[^canon-fpa3000i5plus-1998] |
| 200 mm era | ASML's PAS 5500 platform, launched in 1991 and with i-line systems "down to 0.28 µm";[^asml-30] Canon's FPA-3000i5+ of 1998;[^canon-fpa3000i5plus-1998] Nikon's NSR-S102B i-line scanning stepper for "less critical layers".[^nikon-s202a-s102b] |
| SkyWater-listed tool | "ASML I-line stepper", "ASML I-line scanner"[^skw-01] |
| SKY130 steps | 24 steps, plus 3 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-i-line-stepper-steps>` |

## What the machine class is and how it works

Every optical exposure tool has the same chain: an illuminator, a
reticle stage, a reduction lens, a wafer stage, an alignment system and
a focus system, sealed in a temperature-controlled chamber because the
wafer and the machine expand with temperature.[^wiki-stepper] What makes
a machine an *i-line* tool is its light source and the lens and resist
designed for it; what keeps it in a mixed 200 mm line is that it prints
the many levels with features of a few hundred nanometres or more on
older, cheaper tools while overlaying the KrF levels closely
enough.[^asml-30][^wise-1992] Bruning reviews how these machines
evolved.[^bruning-2007]

### Mercury lamp and illuminator

From the early 1960s through the mid-1980s, "Hg lamps had been used in
lithography for their spectral lines at 436 nm ("g-line"), 405 nm
("h-line") and 365 nm ("i-line")", and the lamp spectrum "is filtered
to select a single spectral line".[^wiki-litho] The lamps are short-arc,
super-high-pressure mercury lamps; Ushio describes its lithography lamps as "high-intensity
light sources with stable irradiance and long lifespan" whose arc is
"nearly that of a point light source".[^ushio-uv-lamps] Kato's chronology
calls Ushio "the leading supplier of Mercury arc lamps for g- and i-line
steppers".[^kato-2007] The illuminator shapes the lamp light into a
uniform field at the reticle and sets the partial coherence: on ASML's
PAS 5500/100D the "Variable coherence range" is "σ = 0.3—0.7" with an
"Intensity: ≥ 900 mW/cm²" and "Uniformity: ≤ 1.5%" at the
wafer,[^asml-pas5500-100d] and the /275D adds annular illumination
"in both conventional and off-axis illumination modes", set by
software for each layer.[^asml-pas5500-275d]

### Projection lens, resolution and focus

The lens reduces the reticle four or five times onto the wafer.
Its numerical aperture is variable, so that each layer can trade
resolution against depth of focus: ASML's i-line steppers run at NA
0.48–0.60, Canon's FPA-3000i5+ at 0.45–0.63, and ASML's /450F scanner at
0.48–0.65.[^asml-pas5500-275d][^canon-fpa3000i5plus-1998][^asml-pas5500-450f]
At a wavelength of 365 nm and NA 0.6, λ/NA is about 610 nm; the
0.35 µm resolution Canon quotes at NA 0.63 corresponds to a process
factor {term}`k1` of about 0.60, and ASML's 0.28 µm at NA 0.60 to about
0.46 (our arithmetic with the relation on the
{ref}`category page <category-lithography>`). The high-NA i-line lenses
came in the late 1980s: Suwa, Ushida and Lin described a high-NA
i-line lens resolving "better than 0.65 μm" with a field-by-field
levelling system,[^suwa-1988] and Katz et al. a high-NA i-line stepper
with phase grating alignment supporting 0.5 µm "with good process
latitude and CD control without adverse effects due to lens heating",
extended to 0.41 µm.[^katz-1990]
Depth of focus is the price of NA: ASML specifies "Usable depth of
focus: ≥ 1.1 µm" at 0.40 µm on the /100D and "≥ 0.8 µm" at 0.28 µm with
annular illumination on the /275D,[^asml-pas5500-100d][^asml-pas5500-275d]
and Levinson and Arnold modelled linewidth variation against exposure
and defocus to define the process window of submicron
lithography.[^levinson-1987] Each field is
therefore levelled before exposure: the /100D has a "Broadband
Field-by-field Focus Leveling System".[^asml-pas5500-100d]

### Stepper and step-and-scan

A stepper exposes the whole reticle field at once — ASML gives the field
of its i-line steppers as 31.1 mm in diameter, with a maximum of
22.0 mm × 27.4 mm — and then steps the wafer to the next
field.[^asml-pas5500-275d][^wiki-stepper] A
step-and-scan system illuminates a slit and moves reticle and wafer
through it on separate stages "driven at different but precisely
synchronized velocities";[^buckley-1989] the concept "enables very
large field sizes and high system productivity",[^buckley-karatzas-1989] and
ASML's /450F i-line scanner prints 26.0 mm × 33.0 mm fields at "≥ 150
wph".[^asml-pas5500-450f] Nikon's NSR-S102B used an i-line source "and a
lens scanning system" to reach "0.35 micron or better resolution" over a
25 by 33 mm field for "less critical layers".[^nikon-s202a-s102b] The
larger field matters where one field must match a KrF scanner's field
on the same wafer; a 1992 i-line stepper with a 22 mm × 44 mm field was
designed so that it "comfortably fits two 22-mm*22-mm fields from the
most advanced reduction steppers" and could image "a majority of process
levels (noncritical levels)".[^wise-1992]

### Alignment and overlay

Before exposure the tool measures alignment marks printed by an earlier
level and places the new image on them. ASML's PAS 5500 steppers use
"Direct Reticle-Referenced, Through-The-Lens (TTL) Phase-Grating
Alignment",[^asml-pas5500-100d] and Wittekoek et al. described alignment
and metrology with diffraction gratings and laser interferometry on the
ASM Lithography stepper in 1986;[^wittekoek-1986] the /275D adds "phase
modulation".[^asml-pas5500-275d]
Canon's FPA-3000i5+ uses an "improved advanced global alignment (AGA)
scheme";[^canon-fpa3000i5plus-1998] global alignment in general
measures marks in a sample of fields and fits the wafer grid to them
({ref}`category-lithography`). Overlay is specified two ways: on one
machine, and between machines. The /275D gives "≤ 40 nm" single-machine
and "≤ 80 nm" matched to another /275.[^asml-pas5500-275d] DeMoor et al.
trace the difference between tools to lens distortion signatures
combined with stepping and scanning repeatability, captured in "mix
and match" matrices,[^demoor-2004] and Chu, Hsu and Hwang found that
lens aberration "might cause over 15 nm overlay
displacement".[^chu-1999] Process layers disturb the marks:
Prasad et al. qualified ASML's ATHENA alignment "on I-line steppers for
W-CMP processes" at 0.35 µm.[^prasad-2001]

### Cost and the equipment cascade

The class persists largely on cost. ASML notes that an
exposure tool may give "10 to 15 years of service" to a leading-edge
customer "at different layers of criticality", that older systems
"migrate to the lithography of choice for less critical layers", and
that it has "refurbished and resold well over 500 PAS 5500
systems".[^asml-30] Wise, Mahany and Wang argued the same for a
large-field i-line tool with cost-of-ownership models.[^wise-1992]
Vendors still sell 200 mm i-line steppers: Canon's FPA-3030i5+
(resolution "≤0.35µm", "≥104wph (200mm)")[^canon-fpa3030i5plus] and
Nikon's NSR-2205iL1, announced in 2023 to "supplement or replace
existing steppers".[^nikon-2205il1]

## Representative 200 mm-era models

* **ASML.** Its first i-line stepper, the PAS 2500/40 of 1987, had "0.4NA,
  0.7µm resolution, 70wph (on 150mm wafers)".[^kato-2007] The PAS 5500
  platform followed in 1991;[^asml-30] ASML sold "some of the first PAS
  5500/200 systems with an 'i-line' light source" in 1996, a tool of
  "0.35 µm" resolution, and the /275 "is still an i-line stepper, but now
  offers resolutions down to 0.28 µm and throughput of up to 100 wafers
  per hour".[^asml-30] Its refurbished-product data sheets describe the
  PAS 5500/100D ("designed for mass production at 0.4 µm") and /275D
  steppers and the /450F "i-Line Step-and-Scan", "the successor of the
  PAS 5500/400 for non-critical applications" and "Optimized for
  mix-and-matching" with the PAS 5500 DUV
  tools.[^asml-pas5500-100d][^asml-pas5500-275d][^asml-pas5500-450f] In
  2001 ASML said its KrF PAS 5500/800 "matches seamlessly with the PAS
  5500/400C i-line scanner".[^asml-800]
* **Nikon.** Nikon's first i-line stepper, the NSR-1010i3, shipped in
  1984.[^kato-2007] Its NSR-S102B i-line scanning stepper was introduced
  alongside the KrF NSR-S202A, the two designed so that "mix-and-match
  strategies are easily accommodated".[^nikon-s202a-s102b] The current
  NSR-2205iL1 is a "5x Reduction i-line Stepper" with NA 0.45 and a
  22 mm × 22 mm field.[^nikon-2205il1]
* **Canon.** Canon's first i-line stepper, the FPA-2000i1, shipped in
  1990.[^kato-2007] The FPA-3000i5+ of 1998 was "a mix-and-match companion
  for its FPA-3000EX5 DUV stepper", both at 5:1;[^canon-fpa3000i5plus-1998]
  the FPA-3030i5+ continues the line.[^canon-fpa3030i5plus]
* **Others.** The Model 2244i described by Wise, Mahany and Wang, a
  large-field i-line stepper with "production resolution of 0.8 mu m",
  was aimed at non-critical levels.[^wise-1992]

## At SkyWater

### What SkyWater lists

Under "Lithography", SkyWater's *Facilities & Capabilities* page lists
six exposure tools, two of them i-line:[^skw-01]

> "ASML I-line stepper"
>
> "ASML I-line scanner"

The other four entries are "ASML DUV stepper", "ASML DUV scanner", "ASML
193nm single stage scanner – 90nm CD" and "ASML 193nm twin stage scanner
– sub 65nm CD"; the group continues with "Overlay down to single digit
nm", "Max field size 26mm x 32mm" and the three tracks, and the "Special
Modules" group lists "Photo stitching in both X and Y directions, sub-20nm
stitching errors".[^skw-01] Read term by term: the vendor is ASML; "I-line"
is the 365 nm mercury line;[^wiki-litho] "stepper" and "scanner" are the
two exposure modes described above. The entries give no model, NA,
field, reduction ratio or tool count. ASML's own PAS 5500 i-line family
includes both steppers and step-and-scan
systems,[^asml-pas5500-275d][^asml-pas5500-450f] so both entries fit it,
but that the tools are PAS 5500s is our inference; SkyWater names no
platform. The overlay and field lines follow the 193 nm entries and name
no tool; whether they apply to the i-line tools is not stated.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the two listings are **strong**: they are SkyWater
statements.[^skw-01] The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.
For this class no second SkyWater source was found: no job posting,
profile or filing cited on the step pages names an i-line tool, and the
S-1 names photoresist suppliers but no exposure-tool
vendor.[^sec-01]

(machine-i-line-stepper-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names an i-line stepper or
scanner as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`CAPM <step-137>`, {ref}`MM3 <step-139>`, {ref}`CAP2M <step-152>`, {ref}`MM4 <step-154>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`; *alternative:* {ref}`FOM <step-004>`, {ref}`NPCM <step-078>`, {ref}`VIM4 <step-159>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"ASML I-line stepper", "ASML I-line scanner"** — *inference:* {ref}`DNM <step-007>`, {ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`, {ref}`HVTPM <step-022>`, {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`, {ref}`TUNM <step-035>`, {ref}`ONOM <step-041>`, {ref}`LVOM <step-044>`, {ref}`RPM <step-049>`, {ref}`RRPM <step-052>`, {ref}`URPM <step-055>`, {ref}`NTM <step-064>`, {ref}`HVNTM <step-068>`, {ref}`LDNTM <step-071>`, {ref}`PSDM <step-081>`, {ref}`NSDM <step-085>`, {ref}`CAPM <step-137>`, {ref}`CAP2M <step-152>`, {ref}`MM5 <step-162>`, {ref}`NSM <step-165>`, {ref}`PDM <step-168>`; *not public which class (i-line or DUV):* {ref}`MM3 <step-139>`, {ref}`MM4 <step-154>`; *listed, not assigned:* {ref}`FOM <step-004>`, {ref}`VIM2 <step-129>`, {ref}`VIM4 <step-159>`

The inferences rest on the design rules, not on any SkyWater statement:
in Table 2 of the PDK's *Criteria & Assumptions*, the smallest minimum
feature among the masks assigned to this class, apart from metal 3 and
metal 4, is 0.38 µm (`LVTNMCD`, `HVTPMCD`, `PSDMCD`, `NSDMCD`), and
many are 0.7 µm or larger, up to 3 µm for the deep N-well and
nitride-seal masks ({ref}`masks-index`).[^pdk-03] Metal 3 and metal 4,
at 0.3 µm, are left open between this class and the KrF class.

## Consumables and facilities

The lithography consumables are described on the
{ref}`lithography materials <material-lithography-materials>` page and
listed in the {ref}`materials index <materials-index>`; what is specific to an i-line
exposure tool is summarised here. None of the SkyWater sources describes
the fab's lamp supply, reticle handling or tool environment.

* **Mercury lamps.** The light source is a replaceable short-arc mercury
  lamp, offered by Ushio in classes "from small (500 W class) to
  ultra-large (35 kW class)" for lithography;[^ushio-uv-lamps] ASML's
  i-line steppers use 1.5 kW and 3.5 kW
  illuminators.[^asml-pas5500-100d][^asml-pas5500-275d] Lamp output
  sets exposure time and therefore throughput.
* **i-line resist.** Diazonaphthoquinone/novolac positive resists, the
  chemistry described by Dammel and on the category
  page;[^dammel-1993][^wiki-dnq] SkyWater's S-1 names "Tokyo Ohka Kogyo
  America, Inc. (photoresist)" among its raw-material suppliers, without
  tying a resist to a tool.[^sec-01] The throughput figures above assume
  doses of 90–200 mJ/cm².[^canon-fpa3000i5plus-1998][^asml-pas5500-275d]
* **Reticles.** Six-inch reticles ("Reticle Size 6 inches" on the
  FPA-3000i5+[^canon-fpa3000i5plus-1998]), made by a mask shop, not in
  the fab. SkyWater lists "Mask GDS to reticle" and "OPC modeling" among
  its services and "Reticle storage/handler/defect inspection" under
  "Photo Metrology".[^skw-01]
* **Environment.** A temperature-controlled chamber;[^wiki-stepper] the
  /100D has "Built-In CLASS 1 Laminar Airflow" that "Enhances
  interferometer stability".[^asml-pas5500-100d]
* **Track and metrology.** The tool is linked in line to a
  {ref}`coat/develop track <machine-coat-develop-track>`, and overlay and
  CD are measured after develop
  ({ref}`machine-cd-sem-overlay-metrology`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's exposure tools and doses per
layer are not public, and its resist thicknesses per layer are not
public beyond the two photoresist thicknesses of the PDK design
assumptions: a nominal 1.14 µm and 0.3 µm for HV tip
implants.[^pdk-03]

* **Most mask levels, few critical ones.** On the step pages' readings
  this class prints 24 of the 36 mask steps and the KrF class 14, with
  metal 3 and metal 4 counted in both; the step pages name this class
  as an alternative for three more. The mix is the one ASML describes
  for older tools that move to "less critical
  layers".[^asml-30] Which physical tool prints which layer is not public.
* **Implant blocks and thick resist.** The well, deep N-well and
  drift-well masks ({ref}`NWM <step-017>`, {ref}`DNM <step-007>`,
  {ref}`PWBM <step-026>`, {ref}`PWDEM <step-030>`) block the deep
  implants of the {ref}`high-energy implanter class <machine-high-energy-implanter>`,
  and the {ref}`NWM <step-017>` page reads a thick resist that favours
  i-line; thick resist for high-energy implants is the subject of Buffat
  and Adams's patent.[^pat-resist-zilog] A thick film needs depth of
  focus more than resolution, which is the trade the variable NA
  offers.[^levinson-1987][^asml-pas5500-100d] Norton et al. found DUV
  resist "equivalent to I-line resist" under high-current implants, so the
  implant itself does not force the choice of class.[^norton-2000]
* **Mix and match with KrF levels.** Many of these levels must overlay
  levels the step pages assign to KrF tools — the tip and source/drain
  implant masks the gate printed at {ref}`P1M <step-061>`, for example —
  so where the two levels are printed on different tools the
  matched-machine rather than the single-machine overlay
  applies,[^asml-pas5500-275d] with lens distortion among the
  contributors (inference from the cited
  studies).[^demoor-2004][^chu-1999] ASML, Canon and Nikon each sold
  i-line tools designed to match their KrF
  tools.[^asml-800][^canon-fpa3000i5plus-1998][^nikon-s202a-s102b] The
  alignment tree of SKY130 is not public.
* **Alignment on polished and metal levels.** The upper i-line levels
  from {ref}`CAPM <step-137>` to {ref}`MM4 <step-154>` are printed over
  polished oxide and tungsten-plug levels (our reading;
  {ref}`category-cmp`); Prasad et al. qualified
  alignment on i-line steppers over tungsten CMP, where marks are hard
  to read.[^prasad-2001] {ref}`MM5 <step-162>` is printed over via 4 and
  the metal-5 stack, and {ref}`NSM <step-165>` and {ref}`PDM <step-168>`
  over the films the step pages read as the fuse oxide and the
  passivation.
* **Metal 3, metal 4 and via 4.** The {ref}`MM3 <step-139>` page gives
  {math}`k_1 \approx 0.49` for the 0.3 µm line on an i-line tool of NA 0.6
  and leaves the class open; ASML's /450F i-line scanner is specified to
  220 nm,[^asml-pas5500-450f] so geometry alone does not exclude i-line
  for the 0.3 µm metals. The 0.8 µm via 4 ({ref}`VIM4 <step-159>`)
  would be an i-line level on geometry alone, but the process-steps
  sheet records for its plate a mask type that we read as a binary mask
  for 248 nm exposure,[^steps-sheet] so the step page assigns it to the
  KrF class as an inference ({ref}`masks-index`).
* **Tunnel mask resist.** On the step pages' reading
  ({ref}`masks-index`, *Patterns*), the {ref}`TUNM <step-035>` resist is
  kept through the {ref}`TUNARCE <step-036>` ARC etch, the
  {ref}`PTSI <step-037>` and {ref}`DEPI <step-038>` implants and the
  {ref}`TUNME <step-039>` wet etch, so one i-line exposure would serve
  four steps.

## Related pages

* {ref}`category-lithography` — optics, resists, masks and overlay, and
  the 36 mask steps of SKY130.
* {ref}`machine-duv-krf-stepper` — the exposure class for the critical
  levels, and the other side of the mix-and-match.
* {ref}`machine-coat-develop-track` — the coat, bake and develop around
  each exposure.
* {ref}`machine-cd-sem-overlay-metrology` — the CD and overlay
  measurements after develop.
* {ref}`masks-index` — each mask's PDK entry, minimum CD, plates and the
  mask-type record for vias 2–4.
* {ref}`mask-dnm` and {ref}`mask-vim4` — per-mask pages for the deep
  N-well mask, assigned to this class, and the via-4 mask, for which it
  is the alternative.
* {ref}`mask-lvtnm`, {ref}`mask-nwm`, {ref}`mask-hvtpm`,
  {ref}`mask-pwbm` and {ref}`mask-pwdem` — per-mask pages for the
  low-Vt N-channel, N-well, high-Vt P-channel, P-well block and
  drain-extended P-well masks, assigned to this class; {ref}`mask-fom`
  for the field-oxide mask, for which it is the alternative.
* {ref}`mask-capm` — the per-mask page for the first MiM capacitor
  mask, assigned to this class.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — resists, developer and exposure-tool
  consumables.
* {ref}`material-lithography-materials` — resists, coatings, developer,
  solvents, reticles and light-source consumables.
* {ref}`category-implant` and {ref}`category-strip` — the implants these
  masks block and the resist strip that follows.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "ASML I-line
  stepper" and "ASML I-line scanner" entries and the rest of the
  lithography group.[^skw-01]
* SkyWater PDK, *Criteria & Assumptions* — the minimum CDs behind the
  step pages' class assignments.[^pdk-03]
* *S8 / SKY130 Process Steps* sheet — the via mask types read as 248 nm
  types.[^steps-sheet]
* ASML, *PAS 5500/100D* data sheet — NA, resolution, field, overlay,
  throughput, illuminator and alignment of an i-line
  stepper.[^asml-pas5500-100d]
* ASML, *PAS 5500/275D* data sheet — the 0.28 µm i-line stepper, its
  single- and matched-machine overlay.[^asml-pas5500-275d]
* ASML, *PAS 5500/450F* data sheet — the i-line step-and-scan successor of
  the /400.[^asml-pas5500-450f]
* ASML, *Three decades of PAS 5500* — the /200 and /275 i-line models and
  the cascade of tools to less critical layers.[^asml-30]
* ASML, PAS 5500/800 press release (2001) — KrF matching to the /400C
  i-line scanner.[^asml-800]
* Canon, FPA-3000i5+ announcement (1998) — a 5:1 i-line stepper designed
  as a mix-and-match companion to a KrF stepper.[^canon-fpa3000i5plus-1998]
* Canon U.S.A., *FPA-3030i5+ Stepper* specifications — the current 200 mm
  i-line stepper.[^canon-fpa3030i5plus]
* Nikon, NSR-S202A and NSR-S102B announcement — an i-line scanning stepper
  for less critical layers.[^nikon-s202a-s102b]
* Nikon, *NSR-2205iL1* product page — a current 5× i-line
  stepper.[^nikon-2205il1]
* Ushio, *Super high-pressure UV lamps* — the mercury lamps of g-, h- and
  i-line tools.[^ushio-uv-lamps]
* SkyWater Technology, Form S-1 (2021) — photoresist suppliers; no
  exposure-tool vendor.[^sec-01]

### High-level understanding

* Wikipedia, *Stepper* — subassemblies, stepping and scanning.[^wiki-stepper]
* Wikipedia, *Photolithography* — mercury lines, projection exposure and
  the track–scanner link.[^wiki-litho]
* Kato, *Chronology of Lithography Milestones* (2007) — dates of the first
  i-line and KrF tools of each vendor.[^kato-2007]
* Wikipedia, *Diazonaphthoquinone* — the i-line resist
  chemistry.[^wiki-dnq]
* Mack, *Fundamental Principles of Optical Lithography* — imaging,
  resolution and focus.[^mack-2007]
* Levinson, *Principles of Lithography*, 2nd ed. — exposure tools and
  overlay in a production context.[^levinson-2005]

### Deep dive

* Bruning, *Proc. SPIE* 2007 — forty years of optical lithography
  tools.[^bruning-2007]
* Suwa, Ushida and Lin, *Proc. SPIE* 1988 — a high-NA i-line lens and
  field-by-field levelling.[^suwa-1988]
* Katz et al., *Proc. SPIE* 1990 — a high-NA i-line stepper with phase
  grating alignment for 0.5 µm and below.[^katz-1990]
* Wittekoek et al., *Proc. SPIE* 1986 — stepper alignment and metrology
  with diffraction gratings and laser interferometry.[^wittekoek-1986]
* Buckley, Galburt and Karatzas, *JVST B* 1989, and Buckley and Karatzas,
  *Proc. SPIE* 1989 — step-and-scan lithography with reduction optics, the
  Micrascan concept.[^buckley-1989][^buckley-karatzas-1989]
* Wise, Mahany and Wang, ASMC 1992 — a large-field i-line stepper for
  non-critical levels and its cost of ownership.[^wise-1992]
* Levinson and Arnold, *JVST B* 1987 — focus as the critical parameter of
  submicron lithography.[^levinson-1987]
* Prasad et al., *Proc. SPIE* 2001 — ATHENA alignment on i-line steppers
  over tungsten CMP.[^prasad-2001]
* DeMoor et al., *Proc. SPIE* 2004 — generating overlay mix-and-match
  matrices between exposure tools.[^demoor-2004]
* Chu, Hsu and Hwang, *Proc. SPIE* 1999 — lens distortion as an overlay
  contributor.[^chu-1999]
* Norton et al., IIT 2000 — i-line and DUV resists compared under
  high-current implantation.[^norton-2000]
* Buffat and Adams (Zilog), US 6,576,405 — thick resist for high-energy
  implant masks.[^pat-resist-zilog]
* Dammel, *Diazonaphthoquinone-based Resists* — the SPIE tutorial text on
  i-line resist chemistry.[^dammel-1993]
* Nakagawa, Taguchi and Ema, IEDM 1990 — i-line phase-shift lithography
  pushed to 0.3 µm patterns.[^nakagawa-1990]

## Open questions

* How many i-line steppers and scanners SkyWater has, their models, NA
  and reduction ratio, and whether they are PAS 5500 systems, are not
  stated.[^skw-01]
* Which SKY130 levels are printed on the i-line stepper rather than the
  i-line scanner, and whether metal 3 and metal 4 are i-line or KrF
  levels, are not public.
* Whether the "Overlay down to single digit nm" and "Max field size 26mm
  x 32mm" lines of the lithography group apply to the i-line tools is not
  stated.[^skw-01]
* The model list above is incomplete: it covers the ASML, Canon and
  Nikon i-line tools, and one other large-field model, for which a
  public description was found, not every i-line exposure tool of the
  period.

<!-- footnotes -->

[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^wiki-stepper]: Wikipedia, *Stepper*.
    <https://en.wikipedia.org/wiki/Stepper>
[^buckley-1989]: J. D. Buckley, D. N. Galburt and C. Karatzas,
    "Step-and-scan lithography using reduction optics", *Journal of
    Vacuum Science & Technology B* **7**(6), 1607–1612 (1989).
    <https://doi.org/10.1116/1.584499>
[^buckley-karatzas-1989]: J. D. Buckley and C. Karatzas, "Step and scan: a
    systems overview of a new lithography tool", *Proc. SPIE* **1088**, 424
    (1989). <https://doi.org/10.1117/12.953171>
[^ushio-uv-lamps]: Ushio Inc., *Super high-pressure UV lamps (500W~35kW)*,
    product page, accessed 2026-09-13.
    <https://www.ushio.co.jp/en/products/1010.html>
[^asml-pas5500-100d]: ASML, *PAS 5500/100D i-Line Stepper*, refurbished
    systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-100d.pdf>
[^asml-pas5500-275d]: ASML, *PAS 5500/275D High Productivity i-Line
    Stepper*, refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-275d.pdf>
[^canon-fpa3000i5plus-1998]: Semiconductor Online, *High Productivity
    i-Line Lithography Stepper* (Canon U.S.A. announcement of the
    FPA-3000i5+ for SEMICON/Europa '98), accessed 2026-09-13.
    <https://www.semiconductoronline.com/doc/high-productivity-i-line-lithography-stepper-0001>
[^asml-pas5500-450f]: ASML, *PAS 5500/450F i-Line Step-and-Scan*,
    refurbished systems data sheet, 2019, accessed 2026-09-13.
    <https://media.asml.com/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/products/refurbished-products/pas-5500-450f.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed 2026-09-13.
    <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^nikon-s202a-s102b]: Semiconductor Online, *Two Scanning Steppers*
    (Nikon Precision Europe announcement of the NSR-S202A and NSR-S102B),
    undated, accessed 2026-09-13.
    <https://www.semiconductoronline.com/doc/two-scanning-steppers-0001>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; lithography entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^bruning-2007]: J. H. Bruning, "Optical lithography: 40 years and
    holding", *Proc. SPIE* **6520**, 652004 (2007).
    <https://doi.org/10.1117/12.720631>
[^kato-2007]: A. Kato, *Chronology of Lithography Milestones*, version
    0.9, May 2007, hosted on lithoguru.com, accessed 2026-09-13.
    <https://www.lithoguru.com/scientist/litho_history/Kato_Litho_History.pdf>
[^suwa-1988]: K. Suwa, K. Ushida and B. J. Lin, "The optical stepper with a
    high numerical aperture i-line lens and a field-by-field leveling
    system", *Proc. SPIE* **0922**, 270–276 (1988).
    <https://doi.org/10.1117/12.968424>
[^katz-1990]: B. A. Katz, J. S. Greeneich, M. G. Bigelow, A. Katz, F. J.
    van Hout and J. F. Coolsen, "High-numerical-aperture I-line stepper",
    *Proc. SPIE* **1264**, 94 (1990). <https://doi.org/10.1117/12.20183>
[^levinson-1987]: H. J. Levinson and W. H. Arnold, "Focus: The critical
    parameter for submicron lithography", *Journal of Vacuum Science &
    Technology B* **5**(1), 293–298 (1987).
    <https://doi.org/10.1116/1.583886>
[^wise-1992]: L. Wise, R. Mahany and L. Wang, "New ultra large field
    submicron i-line stepper for advanced mix-and-match applications",
    *IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC '92) Proceedings*, pp. 75–78 (1992).
    <https://doi.org/10.1109/ASMC.1992.253841>
[^wittekoek-1986]: S. Wittekoek, H. Linders, H. Stover, G. Johnson, D.
    Gallagher and R. Fergusson, "Precision wafer-stepper alignment and
    metrology using diffraction gratings and laser interferometry",
    *Proc. SPIE* **0565**, 22 (1986). <https://doi.org/10.1117/12.949728>
[^demoor-2004]: S. J. DeMoor, J. M. Brown, J. C. Robinson, S. Chang and
    C. Tan, "Scanner overlay mix and match matrix generation: capturing all
    sources of variation", *Proc. SPIE* **5375**, 66 (2004).
    <https://doi.org/10.1117/12.534359>
[^chu-1999]: R. Chu, C. Hsu and T. Hwang, "Characterizing lens distortion
    to overlay accuracy by using fine measurement pattern", *Proc. SPIE*
    **3677**, 83 (1999). <https://doi.org/10.1117/12.350790>
[^prasad-2001]: K. J. Prasad, D. A. Rajan, Y.-K. Tan, G. P. Sun, S. Morgan,
    M. Phillips and B. Ng, "W-CMP alignment using ASML's ATHENA system on
    an I-line stepper", *Proc. SPIE* **4344**, 79 (2001).
    <https://doi.org/10.1117/12.436730>
[^canon-fpa3030i5plus]: Canon U.S.A., *FPA-3030i5+ Stepper Product
    Specifications*, 2015, accessed 2026-09-13.
    <http://downloads.canon.com/nw/pdfs/industrial/fpa-3030i5-plus-stepper-specs.pdf>
[^nikon-2205il1]: Nikon, *NSR-2205iL1 5x Reduction i-line Stepper*,
    product page (new product announcement of 2023-08-31), accessed
    2026-09-13. <https://www.nikon.com/business/semi/sp_nsr-2205il1/>
[^asml-800]: ASML, *ASML introduces new KrF Step & Scan system* (PAS
    5500/800), press release, 2001-01-31.
    <https://www.asml.com/en/news/press-releases/2001/asml-introduces-new-krf-step-and-scan-system-that-extends>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation (Tables 2 and 4).
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
[^wiki-dnq]: Wikipedia, *Diazonaphthoquinone*.
    <https://en.wikipedia.org/wiki/Diazonaphthoquinone>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^norton-2000]: C. Norton, D. Marshall, M. Ameen, D. Whiteside, J. Hallock
    and A. Becknell, "Photoresist properties during high current
    implantation: an I-line vs. DUV resist comparison", *Proc. 2000
    International Conference on Ion Implantation Technology*, pp. 813–816.
    <https://doi.org/10.1109/IIT.2000.924278>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google
    Sheet, tab "Sheet4" (mask types), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^nakagawa-1990]: K. Nakagawa, M. Taguchi and T. Ema, "Fabrication of 64 M
    DRAM with i-line phase-shift lithography", *International Electron
    Devices Meeting (IEDM) Technical Digest* 1990, pp. 817–820.
    <https://doi.org/10.1109/IEDM.1990.237037>
