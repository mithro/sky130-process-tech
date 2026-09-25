(machine-high-current-implanter)=
# High-current ion implanter

A high-current implanter is the beam-line ion implanter a fab uses for
heavy doses at low to moderate energy: source/drain implants, gate
doping and the heavier extension implants. It trades the fine angle
control of a medium-current tool for beam current and throughput, and
in the 200 mm era it usually did so by loading a whole batch of wafers
onto a spinning disc. This page describes the class in general, lists
representative 200 mm-era models, and then says what SkyWater has
published about its own tool of this class and which SKY130 steps this
reference assigns to it. The physics of implantation is on the
{ref}`category page <category-implant>`.

| | High-current ion implanter |
|---|---|
| What it does | Implants high doses of B⁺, BF₂⁺, P⁺ or As⁺ at low to moderate energy; one of the four implanter types — high current, medium current, high energy and ultra-high dose — into which fabs divide implant work.[^tanjyo-2011] |
| Energy | Applied Materials' Quantum 80 "offers a range of 2keV to 80keV", the Quantum LEAP "200eV to 80keV", and the Quantum 120 an option "that boosts energy to 120keV";[^amat-quantum-1999] Nova's NV-10 line went from 80 keV to 160 keV in 1983.[^axcelis-history] |
| Beam current | "up to ~30 mA" in Wikipedia's classification;[^wiki-implant] implanters "capable of beam currents as high as 20 mA of Arsenic" by 1996.[^romig-1996] |
| Dose | Of order 10¹⁵ cm⁻² and above (typical): Nissin's example CMOS flow puts its high-current boron or BF₂ source/drain at 2 × 10¹⁵ cm⁻² and its arsenic source/drain at 5 × 10¹⁵ cm⁻²;[^tanjyo-2011] above 10¹⁶ cm⁻² Wikipedia counts a separate "very high dose" class.[^wiki-implant] |
| Wafer handling | Batch: wafers on "a constantly spinning disk the axis of which is translated" across the beam;[^pat-disk-nova] Eaton's NV-GSD batch system had a throughput "of >200wph".[^axcelis-history] Single-wafer high-current tools such as Varian's VIISta 80 had been described by 2000.[^mezack-2000] |
| 200 mm era | Eaton's NV-GSD/200 (1993) and GSD/200E2 (1996), the second "still being sold today as the GSD Ovation";[^axcelis-history] Applied Materials' "compact 200mm xR LEAP system" and the Quantum that "bridges 150mm, 200mm or 300mm wafers".[^amat-quantum-1999] |
| SkyWater-listed tool | "Axcelis GSD Hi dose B11, BF2, P, As 2-180kev, 5e12 to 5e16, tilt/twist"[^skw-01] |
| SKY130 steps | 6 steps, plus 1 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-high-current-implanter-steps>` |

## What the machine class is and how it works

A high-current implanter has the same chain as every beam-line
implanter — ion source, extraction, analysing magnet, acceleration,
scanning, dosimetry and an end station[^wiki-implant] — described in
more detail on the {ref}`medium-current page
<machine-medium-current-implanter>`. What distinguishes the class is
that each part is sized for milliamperes of beam at low energy. Glavish
and Farley review how beam lines evolved for this, including "the
transition from high current and high energy batch implanters to serial
implanters".[^glavish-2018]

### Ion source, extraction and beam transport

High-current sources wear quickly, above all with fluorinated gases.
Hydrogen "may be added to the plasma to
delay the degradation of tungsten components due to the halogen
cycle";[^wiki-implant] Axcelis's current GSD Ovation adds a "Hydrogen
Generator, Source Bushing Shields and Extended Life Extraction
Electrodes" to cut "source operating costs especially with fluorinated
species".[^axcelis-gsd-page] A beam of many milliamperes at a few keV
spreads under its own space charge, so a short path helps: Applied
Materials describes the Quantum's "extremely short source-to-wafer beam
path, which minimizes beam 'blow up' and energy contamination".[^amat-quantum-1999]
Species changes leave contamination in the beam line: in arsenic
implants run straight after boron processes, Xu and Lee found both
energetic boron, whose energy was "directly related to the post-analyzer
acceleration voltage", and surface boron "generated in the beamline by
ion beam sputtering".[^xu-1996]

### Batch disc scanning and dosimetry

The classic high-current end station scans the wafers, not the beam.
Ryding's 1979 Nova patent describes it: the wafers sit on "a constantly
spinning disk the axis of which is translated in the control direction",
and "a detector, mounted behind the support, … periodically samples the
beam through a moving slot in the support element", so that the
translation speed is adjusted to give "a uniform ion dosage … despite
variations in beam intensity".[^pat-disk-nova] Axcelis's history of the
first NV-10-60 of 1979 names the same "dosimetry slot in the disk" and
notes that "the velocity was proportional to 1/R"; the concept "was
carried forward successfully for many generations of NV-10, GSD, HE,
HE3, HC3, Ultra, and Paradigm".[^axcelis-history] In an Eaton patent
the detector behind the slot is a Faraday cage; the patent notes that
"Faraday cages trap and measure the ion beam current while blocking the
electrons which might accompany the ion beam" (electron suppression is
described on the {ref}`medium-current page
<machine-medium-current-implanter>`), but that neutralised ions, which
still implant, are not counted: "Such Faraday cages do not measure
neutral atoms in the ion beam". It therefore compensates the dose for
the gas pressure in the beam path, noting that dose tolerances "are now
at the 1% level in many applications".[^pat-dose-eaton] Kraupner et al.
discuss this pressure compensation on the Axcelis GSD, where
"neutralization of ions by charge changing interactions with gas … may
lead to wrong dose and bad uniformity".[^kraupner-2002]

### Charge neutralisation and wafer cooling

"Implantation of semiconductor devices at very high beam currents can
often lead to device damage due to charging."[^mehta-1996] Already in Ryding's patent the dose detector
"is not affected by a shower of electrons upon the support that
neutralizes charge on the workpieces".[^pat-disk-nova] Secondary-electron
flood guns helped against positive charging, but "the risk of negative
charging persists due to the inherent high energy electrons present
with this approach", and
"commercial high current implanters are now being increasingly
configured with plasma based flood guns";[^mehta-1996] Eaton instead
introduced a "back biased Secondary Electron Flood (SEF)" in 1996, "to
provide charge control with low risk of emitting high energy primary
electrons".[^axcelis-history] On Varian's VIISion 80 and VIISion 200,
"When implanting with high currents, a plasma flood gun system is used
to prevent wafer charging problems".[^lundquist-1996] Resist changes the
charging: photoresist on a
charge-collection electrode "increases positive charging
dramatically",[^dixon-1996] and a wafer half covered with resist shows
high negative potentials on the bare part and high positive potentials
on the resist.[^lukaszek-1996] The beam also heats the wafer; the NV-10
already had "cooled disks",[^axcelis-history] and Romig et al. found
that resist "begins to bubble and burn at ~15 mA of beam current", which
deep-UV hardening and edge-bead removal prevented.[^romig-1996]

### Tilt and twist on a disc

Eaton's NV-GSD of 1990 "featured unique Gyroscopic
end station, the industry's first two-axis tilt
capability".[^axcelis-history] On a disc the implant angle still varies
across each wafer: "larger wafer sizes exacerbate across-wafer
channeling variations in spinning disk implanters", for "polar
tilt/twist or gyroscopic dual tilt systems" alike.[^jones-1996]
Single-wafer high-current tools were promoted partly for this: Mezack et
al. present Varian's VIISta 80 for "Large Angle Tilt Implants (LATI,
10-60 degrees)".[^mezack-2000]

## Representative 200 mm-era models

* **Nova / Eaton / Axcelis.** The NV-10 series (the NV-10-60 of 1979 was
  "the industry's first commercial high current implanter"), the NV-20
  (1985), the NV-GSD (1990, ">600 units shipped in total"), the NV-GSD/200
  (1993, "designed for low energy performance, quick species change and
  high beam utilization"), the GSD/200E2 (1996) and, for 300 mm, the HC3
  (2001).[^axcelis-history] The GSD line continues as the GSD Ovation,
  whose GSD/E2 is "For general high current
  applications".[^axcelis-gsd-page] Axcelis calls the GSD "the industry
  benchmark for the longest manufactured and supported batch ion
  implanter".[^axcelis-gsd]
* **Applied Materials.** The xR80 and xR LEAP ("Nearly 100 Applied
  Materials implant systems using the xR80(TM) and xR LEAP … technology
  are currently in use", 1999), and the Quantum LEAP, Quantum 80 and
  Quantum 120 announced in July 1999.[^amat-quantum-1999]
* **Varian.** The VIISion 80 and VIISion 200 high-current systems, 80 keV
  and 200 keV machines presented at IIT 1996 that "autotune and implant
  high doses with high beam currents";[^lundquist-1996] Todorov et al.
  studied the energy purity of a VIISion 80 PLUS as a function of,
  among other things, its "disc tilt angle"; we read the disc as a batch
  end station.[^todorov-1998] The VIISta 80 single-wafer high-current
  implanter followed.[^mezack-2000] Varian Semiconductor was acquired by
  Applied Materials in 2011.[^wiki-varian]

Eaton spun its implanter business off as Axcelis Technologies in
2000.[^wiki-axcelis] The {ref}`category page <category-implant>` lists
the same families.

## At SkyWater

### What SkyWater lists

Under "Ion Implant", in its "Diffusion, Anneal & Implant" group,
SkyWater's *Facilities & Capabilities* page lists two GSD
implanters:[^skw-01]

> "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11 to
> 5e15, tilt/twist"
>
> "Axcelis GSD Hi dose B11, BF2, P, As 2-180kev, 5e12 to 5e16,
> tilt/twist"

The {ref}`machines index <machines-index>` places the "Hi dose" entry in
the high-current class and the "High current/energy" entry, the only
listed tool that reaches MeV energies, in the
{ref}`high-energy class <machine-high-energy-implanter>`; this page
follows it. Read term by term, the "Hi dose" entry offers ¹¹B⁺, BF₂⁺,
P⁺ and As⁺, energies of 2–180 keV, doses of 5 × 10¹²–5 × 10¹⁶ cm⁻² and
tilt and twist, with no tilt range stated.[^skw-01] SkyWater does not
say whether the two entries are two machines or two configurations, nor
which GSD model either is. Axcelis describes the GSD as a batch
implanter,[^axcelis-gsd-page] so we read both entries as batch
(spinning-disc) tools; SkyWater does not describe the end station.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the listing is **strong**: it is a SkyWater statement.[^skw-01] The
caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. For
this class the weak point is the split between the two GSD entries:
placing the "Hi dose" entry here and the "High current/energy" entry in
the high-energy class is the machines index's reading of their energy
and dose ranges, and that the "Hi dose" tool is a batch machine is an
inference from the model family.[^skw-01][^axcelis-gsd-page]

(machine-high-current-implanter-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a high-current
implanter as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`ASTI <step-065>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; *alternative:* {ref}`LDASTI <step-072>`

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{table} The 7 steps above: number, code and name
:widths: 10 16 58 16

| Step | Code | Name | Role on this page |
|---:|:---|:---|:---|
| 50 | {ref}`P1I <step-050>` | Poly1 implant | main |
| 53 | {ref}`PRI <step-053>` | PRI implant splits | main |
| 65 | {ref}`ASTI <step-065>` | As tip implant | main |
| 82 | {ref}`PSDI <step-082>` | P+ source drain implant | main |
| 83 | {ref}`2PSDI <step-083>` | 2nd P+ source drain implant | main |
| 86 | {ref}`NSDI <step-086>` | N+ source drain implant | main |
| 72 | {ref}`LDASTI <step-072>` | LD ASTI implant | alternative |
:::
<!-- step-tables:end -->

How the step pages grade the SkyWater tool for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Axcelis GSD Hi dose …"** — *inference:* {ref}`P1I <step-050>`, {ref}`ASTI <step-065>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; *not stated which of two:* {ref}`PRI <step-053>`; *the alternative (no grade):* {ref}`UPRI <step-056>`; *weak:* {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`
* **Either GSD entry** — *weak (which entry would serve not stated):*
  {ref}`LVTNI <step-015>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`

The inferences for the source/drain and gate implants rest on the listed
dose ranges: doses above "1e14" appear only on the two GSD entries, and
the "Hi dose" entry alone reaches "5e16".[^skw-01]

## Consumables and facilities

The dopant sources are described on the
{ref}`dopant gases and implant sources <material-dopant-sources>` page.
The dopant gases and ion-source parts are listed in the
{ref}`materials index <materials-index>`; what is specific to a
high-current tool is summarised here. None of the SkyWater sources
describes the fab's gas delivery or abatement. Monitor wafers are
described on the {ref}`substrates and test wafers <material-substrates>`
page, and exhaust abatement on the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Source gases.** Boron trifluoride, phosphine and arsine, the last
  "flammable, pyrophoric, and highly toxic" in the words the materials
  index quotes,[^wiki-ash3] delivered from sub-atmospheric sorbent
  cylinders or, before them, dilute mixtures "at pressures of 400-1800
  psig".[^pat-sds-atmi] The SkyWater "Hi dose" entry lists all four
  species, B11, BF2, P and As.[^skw-01]
* **Co-gas.** Hydrogen for source life, from a cylinder or "a hydrogen
  generator that uses electrolysis",[^wiki-implant] as in Axcelis's
  GSD Ovation upgrade.[^axcelis-gsd-page]
* **Ion-source and beam-line parts.** Filaments or cathodes, arc
  chambers, source bushings and extraction electrodes;[^axcelis-gsd-page]
  graphite and silicon-coated shields that hold sputtered material and
  cross-contamination down;[^swenson-1996][^xu-1996] and, on a batch
  tool, the disc's wafer pads and clamp rings (typical; category
  page).
* **Vacuum and cooling.** Cryopumps and turbopumps sized for the gas
  load of resist outgassing, whose composition in high-current implants
  is "largely carbon monoxide (CO) and hydrocarbons" early in the
  implant;[^horsky-1998] cryopump regeneration requires managing
  "potentially explosive gas mixtures";[^current-1996] and cooling for
  the disc, which the NV-10 already had.[^axcelis-history]
* **Resist.** Implant resist hardened against heating (Romig et al. used
  a deep-UV treatment),[^romig-1996] and the strip that removes its
  crust afterwards ({ref}`category-strip`).
* **Monitor wafers.** Bare wafers for {ref}`sheet-resistance checks <machine-sheet-resistance-metrology>` of dose and
  uniformity; a charging monitor wafer (CHARM-2) is the tool Current et
  al. used to measure charging during high-current arsenic
  implants.[^current-1998]

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's implant energies and doses are
not public.

* **Zero tilt for source/drain.** The PDK lists a "High current" implant
  angle of 0°,[^pdk-03] which the {ref}`PSDI <step-082>` and
  {ref}`NSDI <step-086>` pages take as the tilt of their implants. A 7°
  source/drain implant is shadowed by the spacer, and Krieger et al.
  concluded that "0 degrees tilt should be used for both n⁻ (LDD) and n⁺
  (source/drain) implants";[^krieger-1989] on a spinning disc, however,
  the angle varies across the wafer and near 0° that variation changes
  channelling,[^jones-1996] which both step pages note. Yoneda and
  Niwayama measured drain-current asymmetry at 130 nm from this error
  even with tilt and twist set to 0°.[^yoneda-2002]
* **Tilted tips on a high-current tool.** The PDK records a 7° "Angle
  for tip implant",[^pdk-03] and the {ref}`ASTI <step-065>` page works
  out the shadowing of such a beam by the gate stack. Whether SKY130's
  tip runs on the "Hi dose" GSD or on the 8250 depends on a dose that is
  not public.[^skw-01]
* **Charging.** The source/drain, tip and gate implants run through
  resist over thin gate oxide. The {ref}`ASTI <step-065>`,
  {ref}`PSDI <step-082>` and {ref}`NSDI <step-086>` pages cite charging
  studies of high-current implants through resist, among them those
  above;[^lukaszek-1996][^dixon-1996][^mehta-1996] the SkyWater entry does not describe the charge-control
  system.[^skw-01]
* **Resist heating, outgassing and dose.** The {ref}`P1I <step-050>`
  page notes that a 10¹⁵–10¹⁶ cm⁻² implant "deposits enough energy to
  flow an uncooled resist". Resist burning,[^romig-1996] outgassing
  whose composition changes abruptly at a "critical dose of 4.5E14" in
  a 150 kV phosphorus source/drain implant,[^horsky-1998] and the
  pressure compensation of the dose[^kraupner-2002] are the machine-side
  limits on how fast such implants can run.
* **One tool, several species.** The step pages assign the boron of
  {ref}`PSDI <step-082>` and the arsenic of {ref}`NSDI <step-086>` to the
  same "Hi dose" entry, as inferences.[^skw-01] If one tool runs both,
  species changes and cross-contamination such as Xu and Lee
  measured[^xu-1996] are managed by the fab; how is not public.
* **Batch or single wafer.** A 200 mm fab of this period would typically
  run source/drain implants on a batch high-current tool (category page);
  the industry later moved to single-wafer high-current
  implanters.[^glavish-2018][^mezack-2000] Axcelis still sells the batch
  GSD for 200 mm fabs.[^axcelis-gsd]

## Related pages

* {ref}`category-implant` — implantation physics and the 25 implant
  steps of SKY130.
* {ref}`machine-medium-current-implanter` — the beam-line chain in
  detail, and the 8250 entry.
* {ref}`machine-high-energy-implanter` — the other GSD entry.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — dopant gases, ion-source parts and their
  hazards.
* {ref}`category-strip` — removal of the crusted resist after high-dose
  implants.
* {ref}`material-substrates` — monitor wafers for dose and uniformity.
* {ref}`material-hardware-consumables` — exhaust abatement.
* {ref}`material-dopant-sources` — dopant gases, solid sources,
  sub-atmospheric packages and ion-source parts.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Treating workpieces with beams <patent-gp21918419>` — US 4,234,797 A (1979)
* {ref}`Storage and delivery system for gaseous hydride, halide, and organometallic group V compounds <patent-gp23253952>` — US 5,518,528 A (1994)
* {ref}`Dose control for use in an ion implanter <patent-gp25134219>` — US 5,760,409 A (1996)
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the two GSD entries
  quoted on this page.[^skw-01]
* [SkyWater PDK Authors, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — the "High current"
  and tip implant angles.[^pdk-03]
* [Axcelis Technologies, *GSD Ovation* product page](<https://www.axcelis.com/products/gsd-ovation/>) — the GSD as a batch
  platform and its source consumables.[^axcelis-gsd-page]
* [Axcelis Technologies, *GSD Ovation* press release (2021)](<https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>) — the GSD
  family for 200 mm fabs.[^axcelis-gsd]
* [Axcelis Technologies, *Our History*](<https://www.axcelis.com/about/our-history/>) — the NV-10, NV-GSD and GSD/200E2
  batch implanters and their dosimetry.[^axcelis-history]
* [Applied Materials, Quantum press release (1999)](<https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-quantum-system-all-high-current/>) — energy ranges and
  wafer sizes of the xR and Quantum high-current tools.[^amat-quantum-1999]
* [Ryding (Nova Associates), US 4,234,797](<https://patents.google.com/patent/US4234797A/en>) — the spinning-disc end station
  with slot dosimetry.[^pat-disk-nova]
* [Chen and Sinclair (Eaton), US 5,760,409](<https://patents.google.com/patent/US5760409A/en>) — pressure-compensated dose
  control.[^pat-dose-eaton]

### High-level understanding

* [Wikipedia, *Ion implantation*](<https://en.wikipedia.org/wiki/Ion_implantation>) — implanter classes, ion sources, beam
  scanning and hazards.[^wiki-implant]
* Wikipedia, [*Axcelis Technologies*](<https://en.wikipedia.org/wiki/Axcelis_Technologies>) and [*Varian Semiconductor*](<https://en.wikipedia.org/wiki/Varian_Semiconductor>) — the
  vendors behind the GSD and VIISta lines.[^wiki-axcelis][^wiki-varian]
* [Wikipedia, *Arsine*](<https://en.wikipedia.org/wiki/Arsine>) — the arsenic source gas and its sub-atmospheric
  delivery.[^wiki-ash3]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — implantation and
  implanter basics in ch. 8.[^txt-01]
* [Quirk and Serda, *Semiconductor Manufacturing Technology*](<https://openlibrary.org/isbn/9780130815200>) — the
  implanter as a fab tool, ch. 17.[^txt-07]

### Deep dive

* [Glavish and Farley, IIT 2018](<https://doi.org/10.1109/IIT.2018.8807986>) — beam-line innovations and the move from
  batch to serial implanters.[^glavish-2018]
* [Tanjyo and Naito, *SEI Technical Review* 2011](<https://global-sei.com/technology/tr/bn73/pdf/73-03.pdf>) — implanter classes and
  an example flow with the implanter type of each implant.[^tanjyo-2011]
* [Mezack et al., IIT 2000](<https://doi.org/10.1109/IIT.2000.924180>) — the VIISta 80 single-wafer high-current
  implanter and large-angle tilt.[^mezack-2000]
* [Lundquist et al., IIT 1996](<https://doi.org/10.1109/IIT.1996.586401>) — the Varian VIISion 80 and VIISion 200
  high-current systems and their plasma flood gun.[^lundquist-1996]
* [Todorov et al., IIT 1998](<https://doi.org/10.1109/IIT.1999.812200>) — energy purity of low-energy boron on a
  VIISion 80 PLUS disc implanter.[^todorov-1998]
* [Kraupner et al., IIT 2002](<https://doi.org/10.1109/IIT.2002.1257988>) — dosimetry and pressure compensation on the
  Axcelis GSD.[^kraupner-2002]
* [Xu and Lee, IIT 1996](<https://doi.org/10.1109/IIT.1996.586161>) — boron cross-contamination in high-dose arsenic
  implants and its beam-line origin.[^xu-1996]
* [Jones and Sinclair, IIT 1996](<https://doi.org/10.1109/IIT.1996.586257>) — across-wafer channelling variation on
  spinning-disc batch implanters.[^jones-1996]
* [Romig, Bishop and Rio, IIT 1996](<https://doi.org/10.1109/IIT.1996.586181>) — resist burning in a high-current
  implanter and its prevention.[^romig-1996]
* [Mehta et al., IIT 1996](<https://doi.org/10.1109/IIT.1996.586128>) — negative charging with plasma flood guns
  compared with electron flood guns.[^mehta-1996]
* [Dixon, Lukaszek and Heden, IIT 1996](<https://doi.org/10.1109/IIT.1996.586134>) — photoresist-enhanced wafer
  charging during high-current implants.[^dixon-1996]
* [Lukaszek, Reno and Bammi, IIT 1996](<https://doi.org/10.1109/IIT.1996.586135>) — charging potentials at a resist
  edge during high-current arsenic implants.[^lukaszek-1996]
* [Current et al., IIT 1998](<https://doi.org/10.1109/IIT.1999.812159>) — charging current–voltage characteristics
  with resist during high-current As⁺ implants.[^current-1998]
* [Horsky, IIT 1998](<https://doi.org/10.1109/IIT.1999.812201>) — outgassing composition and dose shifts in
  high-current and high-energy implants.[^horsky-1998]
* [Smith, 1983](<https://doi.org/10.1007/978-3-642-69156-0_25>) — wafer cooling and photoresist masking problems in
  implantation.[^smith-1983]
* [Current, *JVST A* 1996](<https://doi.org/10.1116/1.580279>) — sources, beam transport, dosimetry, charging
  and cryopump safety from a vacuum perspective.[^current-1996]
* [Swenson et al., IIT 1996](<https://doi.org/10.1109/IIT.1996.586154>) — graphite and silicon beam-line shields
  against metals contamination.[^swenson-1996]
* [Krieger et al., *IEEE TED* 1989](<https://doi.org/10.1109/16.43667>) — spacer shadowing of a 7° source/drain
  implant.[^krieger-1989]
* [Yoneda and Niwayama, IWJT 2002](<https://doi.org/10.1109/IWJT.2002.1225190>) — 130 nm drain-current asymmetry from
  implanter angle error.[^yoneda-2002]
* [Tom and McManus (ATMI), US 5,518,528](<https://patents.google.com/patent/US5518528A/en>) — sub-atmospheric hydride sources
  for implanters.[^pat-sds-atmi]

## Open questions

* Whether SkyWater's "Axcelis GSD Hi dose" and "Axcelis GSD High
  current/energy" entries are two machines or two configurations, and
  which GSD models they are, are not stated.[^skw-01]
* Which charge-control system and tilt range the "Hi dose" tool has is
  not stated.
* The model list above is incomplete: Varian's batch high-current tools
  before the VIISion, and the high-current implanters of vendors other
  than Nova/Eaton/Axcelis, Applied Materials and Varian, are not covered.

<!-- footnotes -->

[^tanjyo-2011]: M. Tanjyo and M. Naito, "History of Ion Implanter and
    Its Future Perspective", *SEI Technical Review* No. 73, October 2011,
    pp. 22–30. <https://global-sei.com/technology/tr/bn73/pdf/73-03.pdf>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion
    implanter", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 190–193.
    <https://doi.org/10.1109/IIT.1996.586181>
[^amat-quantum-1999]: Applied Materials, *Applied Materials Announces New
    Quantum System for All High Current Sub-0.18 Micron Ion Implantation
    Applications*, press release (Business Wire), 1999-07-12.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-new-quantum-system-all-high-current/>
[^axcelis-history]: Axcelis Technologies, *Our History* ("45 Years of
    Innovation"), company web page, accessed 2026-09-13.
    <https://www.axcelis.com/about/our-history/>
[^pat-disk-nova]: G. Ryding (Nova Associates), *Treating workpieces with
    beams*, US 4,234,797 A, granted 1980-11-18.
    <https://patents.google.com/patent/US4234797A/en>
[^mezack-2000]: G. Mezack, T. Callahan, S. Mehta and U. Jeong, "Advantages
    of the Varian VIISta single wafer high current ion implanter for
    advanced device fabrication", *Proc. 2000 International Conference on
    Ion Implantation Technology*, pp. 431–434.
    <https://doi.org/10.1109/IIT.2000.924180>
[^lundquist-1996]: P. Lundquist, B. Pedersen, D. Ackerman and D. Brown,
    "The VIISion 80 and VIISion 200: high current ion implantation
    systems for greater throughput with excellent performance at low to
    high doses", *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 466–469.
    <https://doi.org/10.1109/IIT.1996.586401>
[^todorov-1998]: S. S. Todorov, G. B. Latona, J. J. Cummings and M. Kase,
    "Investigation of energy purity of sub-10 keV B⁺ implants on a Varian
    VIISion PLUS ion implanter", *Proc. 1998 International Conference on
    Ion Implantation Technology*, vol. 1, pp. 650–653.
    <https://doi.org/10.1109/IIT.1999.812200>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; implanter entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^glavish-2018]: H. Glavish and M. Farley, "Review of Major Innovations
    in Beam Line Design", *2018 22nd International Conference on Ion
    Implantation Technology (IIT)*, pp. 9–18.
    <https://doi.org/10.1109/IIT.2018.8807986>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed
    2026-08-30; re-checked 2026-09-13.
    <https://www.axcelis.com/products/gsd-ovation/>
[^xu-1996]: J. Xu and H. S. Lee, "High current implanter dopant
    cross-contamination and its control", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 151–154.
    <https://doi.org/10.1109/IIT.1996.586161>
[^pat-dose-eaton]: H. Chen and F. Sinclair (Eaton Corporation), *Dose
    control for use in an ion implanter*, US 5,760,409 A, granted
    1998-06-02. <https://patents.google.com/patent/US5760409A/en>
[^kraupner-2002]: J. Kraupner, A. Kyek, J. Vogl and S. Weiss, "Dose
    theory and pressure compensation on Axcelis GSD high current
    implanter", *Proc. 14th International Conference on Ion Implantation
    Technology* (2002), pp. 260–263.
    <https://doi.org/10.1109/IIT.2002.1257988>
[^mehta-1996]: S. Mehta, B. Axan, S. Walther and S. Felch,
    "Investigation of negative charging with plasma flood gun (PFG)
    during high current implantation", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 73–76.
    <https://doi.org/10.1109/IIT.1996.586128>
[^dixon-1996]: W. Dixon, W. Lukaszek and C. Heden,
    "Photoresist-enhanced wafer charging during high current ion
    implantation", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 85–88.
    <https://doi.org/10.1109/IIT.1996.586134>
[^lukaszek-1996]: W. Lukaszek, S. Reno and R. Bammi, "Influence of
    photoresist on wafer charging during high current arsenic implant",
    *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 89–92.
    <https://doi.org/10.1109/IIT.1996.586135>
[^jones-1996]: M. Jones and F. Sinclair, "Across-wafer channeling
    variations on batch implanters: a graphical technique to analyze
    spinning disk systems", *Proc. 11th International Conference on
    Ion Implantation Technology* (1996), pp. 264–267.
    <https://doi.org/10.1109/IIT.1996.586257>
[^axcelis-gsd]: Axcelis Technologies, *Axcelis Announces Introduction Of
    The 'GSD Ovation' High Current And High Energy Batch Implanters*, PR
    Newswire, 2021-11-02. <https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>
[^wiki-varian]: Wikipedia, *Varian Semiconductor*.
    <https://en.wikipedia.org/wiki/Varian_Semiconductor>
[^wiki-axcelis]: Wikipedia, *Axcelis Technologies*.
    <https://en.wikipedia.org/wiki/Axcelis_Technologies>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^pat-sds-atmi]: G. M. Tom and J. V. McManus (Advanced Technology
    Materials), *Storage and delivery system for gaseous hydride, halide,
    and organometallic group V compounds*, US 5,518,528 A, granted
    1996-05-21. <https://patents.google.com/patent/US5518528A/en>
[^swenson-1996]: D. R. Swenson, D. F. Downey, S. R. Walther, A. Renau,
    G. Gammel and M. E. Mack, "Metals-contamination-reduction program for
    the Varian EHP-220/500 medium-current ion implanter", *Proc. 11th
    International Conference on Ion Implantation Technology* (1996),
    pp. 139–142. <https://doi.org/10.1109/IIT.1996.586154>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^current-1998]: M. I. Current, M. Foad, S. Brown, W. Lukaszek and
    M. Vella, "Photoresist effects on wafer charging control:
    current-voltage characteristics measured with Charm-2 monitors
    during high-current As⁺ implantation", *Proc. 1998 International
    Conference on Ion Implantation Technology*, vol. 1, pp. 490–493.
    <https://doi.org/10.1109/IIT.1999.812159>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^krieger-1989]: G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
    "Shadowing effects due to tilted arsenic source/drain implant",
    *IEEE Transactions on Electron Devices* **36**(11), 2458–2461
    (1989). <https://doi.org/10.1109/16.43667>
[^yoneda-2002]: K. Yoneda and M. Niwayama, "The drain current asymmetry
    of 130 nm MOSFETs due to extension implant shadowing originated by
    mechanical angle error in high current implanter", *Extended
    Abstracts of the Third International Workshop on Junction
    Technology (IWJT 2002)*, pp. 19–22.
    <https://doi.org/10.1109/IWJT.2002.1225190>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
