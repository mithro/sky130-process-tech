(category-lithography)=
# Photolithography (mask step)

## What this class of step does

A lithography step draws the pattern of one mask onto the wafer in
photoresist. The wafer is coated with a thin, light-sensitive polymer
film, the image of a {term}`reticle` is projected onto it with
ultraviolet light, one field at a time, and the exposed (positive
resist) regions are dissolved in developer. What remains is a stencil
that the following etch or implant step uses; the resist is then
removed at a {term}`ash`/strip step ({ref}`category-strip`). Every
"mask" step in the SKY130 flow — 36 of them, from the field-oxide mask
{ref}`FOM <step-004>` to the pad mask {ref}`PDM <step-168>` — is one
of these.

Precisely, a mask step is a sequence performed on a coater/developer
"track" linked in line with an exposure tool:[^wiki-litho]

1. **Surface preparation**: dehydration bake and vapour-phase
   {term}`HMDS` prime to make the surface hydrophobic so the resist
   adheres.
2. **Anti-reflective coating**: for critical layers a {term}`BARC` is
   spun on and baked (or an inorganic {term}`ARC` was deposited earlier).
3. **Coat**: resist is dispensed and spun to a uniform film; SKY130's
   design assumptions use a nominal photoresist thickness of 1.14
   µm.[^pdk-03] The edge bead is removed ({term}`EBR`).
4. **Soft bake** on a hot plate to drive off casting solvent.
5. **Alignment and exposure** in a {term}`stepper` or scanner, which
   locates alignment marks from an earlier layer, corrects the wafer's
   position, rotation and scale, and exposes each field through the
   reticle at 4× or 5× reduction.
6. **Post-exposure bake** ({term}`PEB`), essential for chemically
   amplified deep-UV resists.
7. **Develop** in aqueous tetramethylammonium hydroxide, rinse and spin
   dry.
8. **Inspection and metrology**: {term}`overlay` measured on box-in-box
   targets and {term}`CD` measured on a {term}`CD-SEM`; wafers out of
   specification are stripped and reworked, which is the reason
   lithography, alone among the categories, is fully reversible.

## Physics and engineering background

### Resolution, k1 and depth of focus

The smallest feature a projection system can print is[^wiki-litho]

```{math}
CD = k_1 \frac{\lambda}{NA}, \qquad DOF = k_2 \frac{\lambda}{NA^2},
```

where {math}`\lambda` is the exposure wavelength, {term}`NA` the
numerical aperture of the projection lens and {term}`k1` a process
factor that "typically equals 0.4 for production". The physical limit
(Rayleigh's criterion for two-beam imaging) is {math}`k_1 = 0.25`;
values between 0.25 and 0.4 need resolution-enhancement
techniques.[^mack-2007][^lin-2002] For a KrF scanner at {math}`\lambda =
248` nm and {math}`NA = 0.68` (the Nikon NSR-S204B, for
example),[^nikon-s204b] {math}`\lambda/NA = 365` nm, so a 130 nm
half-pitch is {math}`k_1 \approx 0.36` and the 90 nm printed gate of a
high-performance 130 nm node is {math}`k_1 \approx 0.25` — hence the
need for phase-shift masks and optical proximity correction on the gate
level. The depth-of-focus formula shows the price: at the same NA the
usable focus window is only a few hundred nanometres, which is why
{term}`CMP` planarisation and wafer flatness matter to lithography.

The 130 nm node was the first at which the printed gate was
deliberately narrower than the half-pitch and then trimmed further in
the etch: ITRS 2001 lists, for 2001, a DRAM half-pitch of 130 nm, an
MPU gate of 90 nm in resist and 65 nm after etch, an ASIC/low-power
gate of 130 nm in resist and 90 nm after etch, a contact of 165 nm in
resist, an overlay requirement of 45–46 nm, CD control of 15.9 nm
(3σ) on the half-pitch and 5.3 nm (3σ) on the MPU gate, and a mask
magnification of 4×.[^itrs-03]

### Wavelengths and light sources

Mercury arc lamps supplied the g-line (436 nm) and i-line (365 nm) used
through the 1980s and early 1990s; excimer lasers then took over, KrF at
248 nm and ArF at 193 nm.[^wiki-litho][^wiki-excimer] A 130 nm-era fab
typically runs a *mixed* line: KrF scanners for the critical layers
(active, poly, contact, metal 1, via 1) and cheaper i-line steppers for
the non-critical implant-block, upper-metal and pad layers, whose
features are 0.5 µm or larger. Which of SKY130's 36 masks are on which
tool is not public. The process-steps sheet records a mask type for
three plates only, which we read as embedded attenuated phase-shift
masks for vias 2 and 3 and a binary mask for via 4, all for 248 nm
exposure ({ref}`masks-index`);[^steps-sheet] it names no exposure
tool, so the step pages' reading that these vias, the 0.8 µm via 4
included, are printed on KrF tools remains an inference.

### Steppers and scanners

A stepper images the whole reticle field at once and steps the wafer
between exposures; a scanner illuminates a slit and moves reticle and
wafer in opposite directions (at 4:1 speed ratio) through it, so the
field can be longer than the lens's well-corrected image circle and lens
aberrations average along the scan.[^wiki-stepper] ITRS 2001 describes
130 nm-node scanners as having "rectangular fields (nominally 25 mm x 32
mm for 4X scanners)".[^itrs-01] Alignment uses diffraction-grating marks
in the {term}`scribe line` read by the tool's alignment sensor; the tool fits a
linear model (translation, rotation, scaling, orthogonality) per wafer
and per field and prints to it.

### Photoresist chemistry

* **i-line resists** are diazonaphthoquinone (DNQ)/novolac: DNQ is a
  dissolution inhibitor that, on exposure, photolyses to an indene
  carboxylic acid, making the exposed novolac soluble in
  base.[^wiki-resist][^wiki-dnq]
* **Deep-UV resists** are chemically amplified ({term}`CAR`): a
  photo-acid generator releases an acid that, during the PEB,
  catalytically removes protecting groups from a poly(hydroxystyrene)
  backbone, so one photon converts many sites. Ito and Willson
  introduced the concept in 1984.[^ito-1984] CARs are sensitive to
  airborne amines (which neutralise the acid and form a "T-top") and to
  the delay between exposure and PEB.
* **Contrast and process latitude.** Resist behaviour is captured by the
  dose-to-clear, contrast γ, and the exposure–focus process window
  (Bossung plots); Mack's textbook treats the full chain from aerial
  image through resist kinetics to developed profile.[^mack-2007]

### Reflectivity control

Substrate reflections cause standing waves through the resist thickness
and, on topography, reflective notching. The cure is an anti-reflective
coating: an organic {term}`BARC` spun under the resist, or an inorganic
one such as {term}`PECVD` silicon {term}`oxynitride` or TiN on aluminium, tuned so that
reflections from its top and bottom interfere destructively at the
exposure wavelength.[^wiki-arc][^mack-2007] SKY130's flow contains a
dedicated ARC etch after the tunnel mask ({ref}`TUNARCE <step-036>`),
showing that at least one layer uses an ARC that must itself be opened.

### Masks, phase shift and OPC

A reticle is a 6-inch fused-silica plate with a chromium absorber
pattern, protected by a pellicle so that particles land out of
focus.[^wiki-mask] Two enhancements push {math}`k_1` below 0.4:

* **Phase-shift masks** ({term}`PSM`). Levenson showed in 1982 that
  giving alternate apertures a 180° phase difference cancels the light
  between them and sharpens the image.[^levenson-1982] Manufacturing at
  130 nm mostly used attenuated (embedded, MoSi) PSMs for contacts and
  gates; ITRS 2001 notes that "primary PSM choices are attenuated
  shifter and alternating aperture".[^itrs-03][^wiki-psm]
* **Optical proximity correction** ({term}`OPC`). Line ends shorten,
  corners round and isolated lines print differently from dense ones;
  OPC pre-distorts the mask data (biasing, serifs, hammerheads,
  {term}`sub-resolution assist features <SRAF>`) so the wafer image matches the
  design.[^wiki-opc]

### Overlay and CD control

Overlay error between a layer and its reference layer is measured
optically on box-in-box or grating targets; it must be a fraction of the
design's minimum spacing (the 45 nm ITRS 2001 target is about a third of
the 130 nm half-pitch).[^itrs-03] Because SKY130 patterns 36 masks, the
choice of which earlier layer each mask aligns to (the "alignment tree")
is a design decision in itself. CD is measured on the CD-SEM after
develop ("ADI") and again after etch ("AEI"); the difference is the etch
bias, which ITRS 2001 tracks separately.[^itrs-01] Both overlay and CD
are put under {term}`SPC` and fed back to the exposure tool as dose and
alignment corrections.

## Typical equipment

* **{ref}`KrF step-and-scan systems <machine-duv-krf-stepper>`**, 4× or 5× reduction: ASML PAS 5500/750E
  (announced 2000-04-04: "130 nm resolution while using standard 248 nm
  light", NA 0.7, "120 200 mm wafer per hour")[^asml-750e] and PAS
  5500/800 (announced 2001-01-31: NA 0.80, "120 nm resolution", "115 200
  mm wafers per hour");[^asml-800] Nikon NSR-S204B (248 nm, 4:1, 25 × 33
  mm field, NA 0.55–0.68; the cited specification sheet describes a 300
  mm-configured unit built in 2002);[^nikon-s204b] Canon FPA-3000EX4
  (248 nm, 5×, NA 0.6).[^tolpygo-2014] The PAS 5500 platform, first
  shipped in 1991, was still being supplied, latterly from recycled
  cores, three decades later.[^asml-30]
* **{ref}`i-line steppers <machine-i-line-stepper>`** for non-critical layers: ASML PAS 5500/275 and
  /300 series, Nikon NSR-2205i and Canon FPA-3000i5.
* **{ref}`Coater/developer tracks <machine-coat-develop-track>`**: TEL CLEAN TRACK ACT 8 (introduced in 1997
  for 200 mm, up to 120 wafers per hour),[^tel-act8][^tel-act] SVG/ASML
  90S and Dainippon Screen (DNS) tracks.
* **{ref}`Metrology <machine-cd-sem-overlay-metrology>`**: KLA-Tencor 8100/8100XP CD-SEM (accelerating voltage
  0.4–1.5 kV, resolution below 4 nm)[^gce-kla8100] and Hitachi
  S-9200/S-9260 CD-SEMs;[^semimarket-s9200] KLA-Tencor 5xxx/Archer
  optical overlay tools; {ref}`after-develop inspection <machine-defect-inspection>` on KLA-Tencor 2xxx
  bright-field inspectors.[^wiki-kla]
* **Reticles** are made at a mask shop (Photronics, DNP, Toppan, or a
  captive shop) with laser or e-beam pattern generators and are not fab
  equipment.

## Typical consumables

* **Photoresists**: i-line DNQ/novolac positive resists (Shipley/Rohm
  and Haas, TOK, JSR, Sumitomo, Clariant/AZ); KrF chemically amplified
  positive resists (Shipley UV-series, TOK, JSR, Shin-Etsu).
* **BARC**: organic bottom anti-reflective coatings (Brewer Science
  DUV-series, Shipley AR-series); {term}`TARC` where used.
* **Adhesion promoter**: HMDS, delivered as vapour.
* **Solvents**: PGMEA (propylene glycol methyl ether acetate) and
  ethyl lactate as resist casting solvents and for EBR; cyclohexanone.
* **Developer**: aqueous tetramethylammonium hydroxide (TMAH), the
  industry-standard strength being 2.38 % (0.26 N), metal-ion-free,
  with surfactant.[^mack-2007][^wiki-tmah][^microchemicals-dev]
* **Excimer laser gases**: krypton, fluorine (in neon) premixes for KrF
  lasers; laser chambers and optics are periodic replacements.
* **Reticles and pellicles**: the mask set itself, cleaned and
  re-pelliclised periodically.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 4 | {ref}`FOM <step-004>` | Field oxide mask |
| 7 | {ref}`DNM <step-007>` | Deep N-well mask |
| 14 | {ref}`LVTNM <step-014>` | Low Vt NMOS mask |
| 17 | {ref}`NWM <step-017>` | N-well mask |
| 22 | {ref}`HVTPM <step-022>` | High V P-channel implant mask |
| 26 | {ref}`PWBM <step-026>` | P-well block mask |
| 30 | {ref}`PWDEM <step-030>` | P-well drain extended mask |
| 35 | {ref}`TUNM <step-035>` | Tunnel mask |
| 41 | {ref}`ONOM <step-041>` | ONO mask |
| 44 | {ref}`LVOM <step-044>` | Low voltage oxide mask |
| 49 | {ref}`RPM <step-049>` | Resistor protect mask |
| 52 | {ref}`RRPM <step-052>` | Rev resistor protect mask |
| 55 | {ref}`URPM <step-055>` | Ultra-high resistor poly mask |
| 61 | {ref}`P1M <step-061>` | Poly mask |
| 64 | {ref}`NTM <step-064>` | NTM mask (tip formation) |
| 68 | {ref}`HVNTM <step-068>` | HV N-tip mask formation |
| 71 | {ref}`LDNTM <step-071>` | LD tip layer mask |
| 78 | {ref}`NPCM <step-078>` | Nitride poly cut mask |
| 81 | {ref}`PSDM <step-081>` | P+ source drain implant mask |
| 85 | {ref}`NSDM <step-085>` | N+ source drain implant mask |
| 93 | {ref}`LICM1 <step-093>` | Local interconnect contact mask |
| 102 | {ref}`LI1M <step-102>` | Local interconnect 1 mask |
| 107 | {ref}`CTM1 <step-107>` | Metal contact mask |
| 113 | {ref}`MM1 <step-113>` | Metal1 mask |
| 118 | {ref}`VIM <step-118>` | Via1 mask |
| 124 | {ref}`MM2 <step-124>` | Metal2 mask |
| 129 | {ref}`VIM2 <step-129>` | Via2 mask |
| 137 | {ref}`CAPM <step-137>` | Capacitor mask |
| 139 | {ref}`MM3 <step-139>` | Metal3 mask |
| 144 | {ref}`VIM3 <step-144>` | Via3 mask |
| 152 | {ref}`CAP2M <step-152>` | Capacitor 2 mask |
| 154 | {ref}`MM4 <step-154>` | Metal4 mask |
| 159 | {ref}`VIM4 <step-159>` | Via4 (pad via) mask |
| 162 | {ref}`MM5 <step-162>` | Metal5 mask |
| 165 | {ref}`NSM <step-165>` | Nitride seal mask |
| 168 | {ref}`PDM <step-168>` | Pad mask |

## References

### Cross-check

* ITRS 2001, *Lithography* — Tables 57a and 58a: half-pitch, gate,
  contact, overlay and CD-control targets, mask magnification and PSM
  choices.[^itrs-03]
* ITRS 2001, *Front End Processes* — scanner field size and gate etch
  bias.[^itrs-01]
* SkyWater PDK, *Criteria & Assumptions* — the nominal photoresist
  thickness.[^pdk-03]
* *S8 / SKY130 Process Steps* sheet, tab "Sheet4" — the mask types
  recorded for the via 2, via 3 and via 4 plates.[^steps-sheet]
* ASML, PAS 5500/750E press release (2000) — 130 nm resolution at
  248 nm, NA 0.7, 120 wafers per hour.[^asml-750e]
* ASML, PAS 5500/800 press release (2001) — NA 0.80, 120 nm
  resolution.[^asml-800]
* ASML, *Three decades of PAS 5500* — the platform's longevity.[^asml-30]
* Nikon, NSR-S204B specification summary — field, NA and
  wavelength.[^nikon-s204b]
* Tolpygo et al., arXiv 2014 — a Canon FPA-3000EX4 described in
  use.[^tolpygo-2014]
* Tokyo Electron, *Coater/Developer ACT Series* product
  page.[^tel-act]
* Semiconductor Online, *CLEAN TRACK ACT 8* — introduction date and
  throughput.[^tel-act8]
* GCE Market, KLA-Tencor 8100XP CD-SEM specification
  summary.[^gce-kla8100]
* Legacy Semi, Hitachi S-9200 CD-SEM listing.[^semimarket-s9200]
* MicroChemicals, *Development of photoresists* — TMAH developer
  strength and practice.[^microchemicals-dev]

### High-level understanding

* Wikipedia, *Photolithography* — the process sequence, the resolution
  equation and wavelengths.[^wiki-litho]
* Wikipedia, *Stepper*.[^wiki-stepper]
* Wikipedia, *Photoresist*.[^wiki-resist]
* Wikipedia, *Photomask*.[^wiki-mask]
* Wikipedia, *Phase-shift mask*.[^wiki-psm]
* Wikipedia, *Optical proximity correction*.[^wiki-opc]
* Wikipedia, *Resolution enhancement technologies*.[^wiki-ret]
* Wikipedia, *Anti-reflective coating*.[^wiki-arc]
* Wikipedia, *Numerical aperture*.[^wiki-na]
* Wikipedia, *Excimer laser*.[^wiki-excimer]
* Wikipedia, *Diazonaphthoquinone*.[^wiki-dnq]
* Wikipedia, *Tetramethylammonium hydroxide*.[^wiki-tmah]
* Wikipedia, *Critical dimension*.[^wiki-cd]
* Wikipedia, *KLA Corporation* — the inspection and metrology
  vendor.[^wiki-kla]
* Mack, *The Basics of Microlithography* — an online
  tutorial.[^mack-basics]
* Mack, *Fundamental Principles of Optical Lithography* — the full
  chain from aerial image through resist kinetics to developed
  profile.[^mack-2007]
* Levinson, *Principles of Lithography*, 4th ed. — tools, resists,
  overlay and metrology in one volume.[^levinson-2019]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 5
  ("Lithography").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 12–14.[^txt-02]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  ch. 7–9.[^campbell-2013]

### Deep dive

* Lin, *J. Micro/Nanolith. MEMS MOEMS* 2002 — the k₁ and k₃ coefficients and
  the nonparaxial scaling equations for resolution and depth of
  focus.[^lin-2002]
* Lin, *Proc. SPIE* 1986 — where the resolution is lost between the
  Rayleigh limit and production practice.[^lin-1986]
* Levenson, Viswanathan and Simpson, *IEEE TED* 1982 — the original
  phase-shifting mask paper.[^levenson-1982]
* Lin, *IEEE Circuits and Devices* 1993 — a tutorial on alternating and
  {term}`attenuated phase-shift masks <attenuated PSM>`.[^lin-1993]
* Ito and Willson, *ACS Symp. Ser.* 1984 — the chemically amplified
  resist concept applied to semiconductor manufacturing.[^ito-1984]
* Ito and Willson, *Polym. Eng. Sci.* 1983 — the first chemical
  amplification resist paper.[^ito-1983]
* Ito, *Adv. Polym. Sci.* 2005 — a 200-page review of chemically
  amplified resists, including KrF poly(hydroxystyrene)
  systems.[^ito-2005]
* Reichmanis and Thompson, *Chem. Rev.* 1989 — polymer materials for
  microlithography, DNQ/novolac included.[^reichmanis-1989]
* Wallraff and Hinsberg, *Chem. Rev.* 1999 — lithographic imaging
  techniques and resist chemistry for sub-quarter-micron
  features.[^wallraff-1999]
* Dammel, *Diazonaphthoquinone-based Resists* — the SPIE tutorial text
  on i-line resist chemistry.[^dammel-1993]
* Otto et al., *Proc. SPIE* 1994 — rules-based optical proximity
  correction.[^otto-1994]
* Rieger and Stirniman, *Proc. SPIE* 1994 — model-based ("behaviour
  modelling") proximity correction.[^rieger-1994]
* Brunner, *Proc. SPIE* 1991 — optimising resist-stack optical
  properties: swing curves and anti-reflective layers.[^brunner-1991]
* Bossung, *Proc. SPIE* 1977 — the focus–exposure ("Bossung") plots
  used to characterise projection printing.[^bossung-1977]
* Mack, *Opt. Eng.* 1988 — understanding focus effects in
  submicrometre optical lithography.[^mack-1988]
* Levinson and Arnold, *JVST B* 1987 — focus as the critical parameter
  for submicron lithography, and its budget.[^levinson-1987]
* Starikov, *Opt. Eng.* 1992 — accuracy of overlay measurements and
  tool-induced shift.[^starikov-1992]
* Bruning, *Proc. SPIE* 2007 — a history of optical lithography tools
  from contact printers to scanners.[^bruning-2007]
* SEMI P1 — the specification for hard-surface photomask
  substrates.[^semi-p1]
* Buffat and Adams (Zilog), US 6,576,405 — high-aspect-ratio thick
  resist for high-energy implant masks.[^pat-resist-zilog]
* Chip History Center, *PAS 5500/400 Step & Scan* — the ASML platform
  in its historical context.[^chiphistory-pas5500]
* Mack, *Online Micro- and Nanofabrication Course* (CHE323) —
  university lecture materials.[^mack-course]
* MIT OpenCourseWare 6.152J — lecture notes on optical lithography and
  resists.[^ocw-6152]

<!-- footnotes -->

[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet4" (mask types), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^lin-2002]: B. J. Lin, "The k₃ coefficient in nonparaxial λ/NA scaling
    equations for resolution, depth of focus, and immersion
    lithography", *Journal of Micro/Nanolithography, MEMS, and MOEMS*
    **1**(1), 7–12 (2002). <https://doi.org/10.1117/1.1445798>
[^nikon-s204b]: Nikon, *NSR-S204B 248 nm Scanner Exposure System
    Overview* (specification summary, reseller copy), attached to the
    listing Tara Semiconductor Technology, *Used 2002 NIKON S204
    Scanner* (listing LITV25-01), accessed 2026-09-12.
    <https://f.machineryhost.com/fc49306d97602c8ed1be1dfbf0835ead/aa008f2897d7d4a224ff92839b4299e9/SpecSummary_LITV25-01_NSR-S204B.pdf>,
    <https://www.tarasemi.com/listings/5223879-used-2002-nikon-s204-scanner>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^wiki-excimer]: Wikipedia, *Excimer laser*.
    <https://en.wikipedia.org/wiki/Excimer_laser>
[^wiki-stepper]: Wikipedia, *Stepper*.
    <https://en.wikipedia.org/wiki/Stepper>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^wiki-resist]: Wikipedia, *Photoresist*.
    <https://en.wikipedia.org/wiki/Photoresist>
[^wiki-dnq]: Wikipedia, *Diazonaphthoquinone*.
    <https://en.wikipedia.org/wiki/Diazonaphthoquinone>
[^ito-1984]: H. Ito and C. G. Willson, "Applications of Photoinitiators
    to the Design of Resists for Semiconductor Manufacturing", *ACS
    Symposium Series* **242**, 11–23 (1984).
    <https://doi.org/10.1021/bk-1984-0242.ch002>
[^wiki-arc]: Wikipedia, *Anti-reflective coating*.
    <https://en.wikipedia.org/wiki/Anti-reflective_coating>
[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^levenson-1982]: M. D. Levenson, N. S. Viswanathan and R. A. Simpson,
    "Improving resolution in photolithography with a phase-shifting
    mask", *IEEE Transactions on Electron Devices* **29**(12),
    1828–1836 (1982). <https://doi.org/10.1109/T-ED.1982.21037>
[^wiki-psm]: Wikipedia, *Phase-shift mask*.
    <https://en.wikipedia.org/wiki/Phase-shift_mask>
[^wiki-opc]: Wikipedia, *Optical proximity correction*.
    <https://en.wikipedia.org/wiki/Optical_proximity_correction>
[^asml-750e]: ASML, *ASML introduces KrF lithography scanner* (PAS
    5500/750E), press release, 2000-04-04.
    <https://www.asml.com/en/news/press-releases/2000/asml-introduces-krf-lithography-scanner-optimized-for>
[^asml-800]: ASML, *ASML introduces new KrF Step & Scan system* (PAS
    5500/800), press release, 2001-01-31.
    <https://www.asml.com/en/news/press-releases/2001/asml-introduces-new-krf-step-and-scan-system-that-extends>
[^tolpygo-2014]: S. K. Tolpygo et al., "Fabrication Process and
    Properties of Fully-Planarized Deep-Submicron Nb/Al-AlOx/Nb Josephson
    Junctions for VLSI Circuits", arXiv:1408.5829 (2014) — describes a
    Canon FPA-3000EX4 248 nm stepper with 5× reduction and NA 0.6.
    <https://arxiv.org/abs/1408.5829>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021.
    <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^tel-act8]: Semiconductor Online, *CLEAN TRACK ACT 8 System for Spin-On
    Dielectric (SOD) Applications*.
    <https://www.semiconductoronline.com/doc/clean-track-act-8-system-for-spin-on-dielectr-0001>
[^tel-act]: Tokyo Electron, *Coater/Developer ACT Series*, product page.
    <https://www.tel.com/product/act.html>
[^gce-kla8100]: GCE Market, *KLA-Tencor 8100XP CD-SEM* (specification
    summary).
    <https://www.gcemarket.com/gce/gce.nsf/products/kla-tencor-8100xp-cd-sem-7expup>
[^semimarket-s9200]: Legacy Semi, *Hitachi S-9200 CD-SEM* (listing).
    <https://www.semimarket.com/item/hitachi-s-9200-cd-sem/42724>
[^wiki-kla]: Wikipedia, *KLA Corporation*.
    <https://en.wikipedia.org/wiki/KLA_Corporation>
[^wiki-tmah]: Wikipedia, *Tetramethylammonium hydroxide*.
    <https://en.wikipedia.org/wiki/Tetramethylammonium_hydroxide>
[^microchemicals-dev]: MicroChemicals, *Development of photoresists*,
    application note.
    <https://www.microchemicals.com/dokumente/application_notes/development_photoresist.pdf>
[^wiki-ret]: Wikipedia, *Resolution enhancement technologies*.
    <https://en.wikipedia.org/wiki/Resolution_enhancement_technologies>
[^wiki-na]: Wikipedia, *Numerical aperture*.
    <https://en.wikipedia.org/wiki/Numerical_aperture>
[^wiki-cd]: Wikipedia, *Critical dimension*.
    <https://en.wikipedia.org/wiki/Critical_dimension>
[^mack-basics]: C. A. Mack, *The Basics of Microlithography*, online
    tutorial. <https://www.lithoguru.com/scientist/lithobasics.html>
[^levinson-2019]: H. J. Levinson, *Principles of Lithography*, 4th ed.,
    SPIE Press, 2019, ISBN 978-1-5106-2760-4.
    <https://doi.org/10.1117/3.2525393>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^lin-1986]: B. J. Lin, "Where Is The Lost Resolution?", *Proc. SPIE*
    **633**, 44 (1986). <https://doi.org/10.1117/12.963701>
[^lin-1993]: B. J. Lin, "Phase-shifting masks gain an edge", *IEEE
    Circuits and Devices Magazine* **9**(2), 28–35 (1993).
    <https://doi.org/10.1109/101.200850>
[^ito-1983]: H. Ito and C. G. Willson, "Chemical amplification in the
    design of dry developing resist materials", *Polymer Engineering &
    Science* **23**(18), 1012–1018 (1983).
    <https://doi.org/10.1002/pen.760231807>
[^ito-2005]: H. Ito, "Chemical Amplification Resists for
    Microlithography", *Advances in Polymer Science* **172**, 37–245
    (2005). <https://doi.org/10.1007/b97574>
[^reichmanis-1989]: E. Reichmanis and L. F. Thompson, "Polymer
    materials for microlithography", *Chemical Reviews* **89**(6),
    1273–1289 (1989). <https://doi.org/10.1021/cr00096a001>
[^wallraff-1999]: G. M. Wallraff and W. D. Hinsberg, "Lithographic
    Imaging Techniques for the Formation of Nanoscopic Features",
    *Chemical Reviews* **99**(7), 1801–1822 (1999).
    <https://doi.org/10.1021/cr980003i>
[^dammel-1993]: R. R. Dammel, *Diazonaphthoquinone-based Resists*, SPIE
    Tutorial Texts TT11, SPIE Press, 1993.
    <https://doi.org/10.1117/3.2265072>
[^otto-1994]: O. W. Otto, J. G. Garofalo, K. K. Low, C.-M. Yuan, R. C.
    Henderson, C. Pierrat, R. L. Kostelak, S. Vaidya and P. K. Vasudev,
    "Automated optical proximity correction: a rules-based approach",
    *Proc. SPIE* **2197**, Optical/Laser Microlithography VII, 278–293
    (1994). <https://doi.org/10.1117/12.175422>
[^rieger-1994]: M. L. Rieger and J. P. Stirniman, "Using behavior
    modeling for proximity correction", *Proc. SPIE* **2197**, 371–376
    (1994). <https://doi.org/10.1117/12.175431>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^bossung-1977]: J. W. Bossung, "Projection Printing Characterization",
    *Proc. SPIE* **100**, 80–85 (1977).
    <https://doi.org/10.1117/12.955357>
[^mack-1988]: C. A. Mack, "Understanding Focus Effects In Submicrometer
    Optical Lithography", *Optical Engineering* **27**(12) (1988).
    <https://doi.org/10.1117/12.7978683>
[^levinson-1987]: H. J. Levinson and W. H. Arnold, "Focus: The critical
    parameter for submicron lithography", *Journal of Vacuum Science &
    Technology B* **5**(1), 293–298 (1987).
    <https://doi.org/10.1116/1.583886>
[^starikov-1992]: A. Starikov, "Accuracy of overlay measurements: tool
    and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
    (1992). <https://doi.org/10.1117/12.56172>
[^bruning-2007]: J. H. Bruning, "Optical lithography: 40 years and
    holding", *Proc. SPIE* **6520**, 652004 (2007).
    <https://doi.org/10.1117/12.720631>
[^semi-p1]: SEMI, *SEMI P1 — Specification for Hard Surface Photomask
    Substrates*, SEMI Standards store listing.
    <https://store-us.semi.org/products/p00100-semi-p1-specification-for-hard-surface-photomask-substrates>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^chiphistory-pas5500]: Chip History Center, *PAS 5500/400 Step & Scan
    Alignment System from ASML*.
    <https://www.chiphistory.org/163-asml-pas-5500-400-step-scan-system>
[^mack-course]: C. A. Mack, *Online Micro- and Nanofabrication Course*
    (CHE323 lecture materials).
    <https://www.lithoguru.com/scientist/CHE323/course.html>
[^ocw-6152]: MIT OpenCourseWare, *6.152J Micro/Nano Processing
    Technology*, Fall 2005 (lecture notes on lithography, etching,
    deposition and CMP).
    <https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/>
