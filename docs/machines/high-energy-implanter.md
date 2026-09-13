(machine-high-energy-implanter)=
# High-energy ion implanter

A high-energy implanter is the beam-line ion implanter a fab uses to
place dopant deep in the silicon: retrograde wells, deep N-wells and
buried layers, at energies from a few hundred keV to several MeV. It
adds a second accelerator — a radio-frequency linear accelerator or a
DC tandem — to the chain of an ordinary implanter, and in the 200 mm
era it was built either on a batch spinning-disc end station or as a
single-wafer machine. This page describes the class in general, lists
representative 200 mm-era models, and then says what SkyWater has
published about its own tool of this class and which SKY130 steps this
reference assigns to it. The physics of implantation is on the
{ref}`category page <category-implant>`.

| | High-energy ion implanter |
|---|---|
| What it does | Implants B⁺, P⁺ and multiply charged ions deep below the surface for wells and buried layers; one of the four implanter types — high current, medium current, high energy and ultra-high dose — into which fabs divide implant work.[^tanjyo-2011] |
| Energy | "above 200 keV and up to 10 MeV" in Wikipedia's classification;[^wiki-implant] an Eaton patent calls 1.5 MeV "typical for the deep implants" but requires implants "between 300 keV and 700 keV" too;[^pat-linac-axcelis] Axcelis's GSD/HE has a "10 stage LINAC with energies up to 3 MeV" and the GSD/VHE a "14 stage LINAC with energies up to 4.9 MeV".[^axcelis-gsd-page] |
| Beam current | For wells, triple wells and buried layers "the typical beam current is less than a few hundred particle micro-amperes";[^oconnor-1996] the NV-GSD/VHE delivers "beam currents of B⁺ in excess of 1 pmA at energies approaching 1.7 MeV".[^wilson-1996] |
| Dose | For the same applications "the typical dose … is less than 3E13/cm²";[^oconnor-1996] Nissin's example CMOS flow runs its high-energy well implants at 10¹³ cm⁻²;[^tanjyo-2011] buried p-type layers need "doses as high as 2×10¹⁵ at/cm²".[^namaroff-2000] |
| Wafer handling | Batch: the NV-GSD-HE was "the integration of the GSD end station and the LINAC technology";[^axcelis-history] or single-wafer: Varian's VIISta 3000.[^tokoro-2000] |
| 200 mm era | Eaton's NV-GSD-HE of 1994, "the world's first production high energy system, with a throughput of 210 wph";[^axcelis-history] Genus's Tandetron 1520;[^tokoro-1996] Varian's VIISta 3000 for "200 and 300 mm wafer processes".[^tokoro-2000] |
| SkyWater-listed tool | "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11 to 5e15, tilt/twist"[^skw-01] |

## What the machine class is and how it works

A high-energy implanter has the source, analysing magnet, scanning,
dosimetry and end station of every beam-line implanter,[^wiki-implant]
described in more detail on the {ref}`medium-current page
<machine-medium-current-implanter>`; what distinguishes it is the
accelerator after the magnet and the consequences of MeV beams for
energy purity, dosimetry and resist. In Wikipedia's words the beam
"passes through an analysis magnet to select the ions that will be
implanted and then passes through one or two linear accelerators
(linacs) that accelerate the ions before they reach the
wafer".[^wiki-implant] Glavish and Farley review the beam-line
innovations behind the class.[^glavish-2018]

### RF linear accelerators

Eaton brought "LINAC based acceleration to commercial semiconductor
manufacturing" with the NV-1000 of 1986.[^axcelis-history] Glavish and
Denholm's patent describes the principle: "The accelerator is
constructed from multiple stages or cells with each cell including an
accelerating electrode coupled to an rf resonant tank circuit", the
phase of each cell is set for "the mass, charge, and initial velocity of
the ion", and ions leave "in focused packets or bunches" with "energies
on the order of 1 mev per charge state".[^pat-linac-eaton] A later
Axcelis patent, which names the "Eaton GSD/HE and GSD/VHE ion
implanters", describes a typical high-energy beam line as "a mass analysis magnet
… and a radio frequency (RF) linear accelerator (linac)" made of "a series
of resonator modules …, each of which further accelerates ions beyond
the energies they achieve from prior modules".[^pat-linac-axcelis] An RF
linac does not fix the energy by a voltage: "the beam energy from the RF
system cannot be determined so easily as the electro-static systems",
so on the NV-GSD-HE "the Final Energy Magnet is used for energy
analysis, measuring its magnetic field strength by a
Hall-probe".[^suetsugu-2000]

### DC tandem accelerators

The alternative is an electrostatic tandem accelerator. Genus
introduced the "Tandetron 1520" as its "third generation high energy
ion implanter", after the G1500 and G1510.[^tokoro-1996] Varian's
single-wafer VIISta 3000 combined "well established Tandetron™ DC
beamline architecture" with "the electrostatic beam scanning and dose
control system developed for the VIISta 810 medium current ion
implanter".[^tokoro-2000] Varian claimed that with its "DC tandem
accelerator architecture coupled with in situ energy calibration" it was
"the only high-energy ion implanter that directly measures and
interlocks the final implant energy".[^varian-viista3000]

### Multiply charged ions and energy purity

Multiply charged ions reach higher energies on the same accelerator:
the NV-GSD/VHE reaches "B⁺⁺ to energies approaching 3 MeV and
P⁺⁺⁺ energies approaching 5 MeV",[^wilson-1996] and Spinelli et al.
described the problems of "multicharged phosphorous ions in an
industrial context" for MeV n-wells as early as
1985.[^spinelli-1985] Sources with indirectly heated cathodes give
higher multiply charged currents.[^horsky-1998-ihc] The price is energy
contamination: charge exchange with outgassing resist creates
low-energy ions, which Kubo et al. measured at up to 12 % of a P⁺⁺
dose.[^kubo-1996]

### Scanning, dosimetry and pressure

Batch high-energy machines kept the spinning disc and slot dosimetry of
the high-current tools; the concept "was carried forward successfully
for many generations of NV-10, GSD, HE, HE3" and later
machines.[^axcelis-history] At MeV energies residual gas does more than
neutralise the beam: "at higher energies stripping of electrons from
ions within the beam becomes more likely than charge neutralization",
and stripped ions make the Faraday cup read high, so Eaton's dose
controller compensates for both effects; its examples include "P⁺¹
850 keV at 550 µA".[^pat-dose-eaton] Single-wafer machines scan the beam:
the VIISta 3000's electrostatic scan sweeps the beam "about 10 times
more often than alternative (magnetic scan) approaches".[^varian-viista3000]

### Resist outgassing and the end station

Well implants run through thick resist and deposit their energy deep
in it. O'Connor and Tokoro note that "special attention needs to be paid
to photoresist outgassing during high energy implantation because the
range of the dopant is much deeper (resulting in dramatically more
outgassing)", and that "for low energy implants, neutralization is
dominant. This is not necessarily the case for higher energy
implants."[^oconnor-1996] Lee et al. measured chamber pressures rising
into "the E-4 torr range" with resists up to 4.5 µm thick, and "if the
chamber pressure is kept below 3.0 E-5 torr no observable dose shift
could be detected".[^lee-1996] In high-energy implants "up to 50% of
the evolved gas consists of species other than hydrogen".[^horsky-1998]
End stations are therefore designed around the gas load.[^oconnor-1996]

## Representative 200 mm-era models

* **Eaton / Axcelis.** The NV-1000 (1986) and NV-1002 (1990), the NV-GSD-HE
  (1994), and the HE3 for 300 mm (1998);[^axcelis-history] the
  NV-GSD/VHE, "an evolutionary step from the NV-GSD/HE" using the same
  "source, injector and end station".[^wilson-1996] The line continues as
  the GSD/HE and GSD/VHE Ovation.[^axcelis-gsd-page][^axcelis-gsd]
* **Genus.** The G1500, G1510 and Tandetron 1520 MeV
  implanters.[^tokoro-1996]
* **Varian.** The single-wafer VIISta 3000, which Varian presented as
  spanning energies to "greater than 3.75 MeV"[^varian-viista3000] and
  "developed … to meet requirements of advanced 200 and 300 mm wafer
  processes".[^tokoro-2000] Varian Semiconductor was acquired by Applied
  Materials in 2011.[^wiki-varian]

Eaton spun its implanter business off as Axcelis Technologies in
2000.[^wiki-axcelis] The {ref}`category page <category-implant>` lists
these families.

## At SkyWater

### What SkyWater lists

Under "Ion Implant", in its "Diffusion, Anneal & Implant" group,
SkyWater's *Facilities & Capabilities* page lists:[^skw-01]

> "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11 to
> 5e15, tilt/twist"

It is the only listed implanter that reaches MeV energies, and the
{ref}`machines index <machines-index>` places it in this class; the
other GSD entry, "Axcelis GSD Hi dose", is on the
{ref}`high-current page <machine-high-current-implanter>`. Read term by
term, the entry offers ¹¹B⁺, BF₂⁺, P⁺ and As⁺, energies of 10–3000 keV,
doses of 10¹¹–5 × 10¹⁵ cm⁻² and tilt and twist, with no tilt range
stated.[^skw-01] SkyWater does not give a model. Its 3000 keV ceiling
matches the 3 MeV that Axcelis gives for the GSD/HE,[^axcelis-gsd-page]
so we read the entry as a GSD/HE-class batch tool; that is an inference.
Whether the two GSD entries are two machines or two configurations is
not stated.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the listing is **strong**: it is a SkyWater statement.[^skw-01] It shows
that the tool is on the Minnesota floor now, not that it built the first
S8 wafers. SkyWater's maintenance-technician profile shows technicians
reviewing schematics "to troubleshoot complex equipment, like an
implanter", corroboration of in-house implanter maintenance without a
model.[^skw-07] SkyWater's S-1 mentions Axcelis Technologies only in a
director's biography, not as a supplier.[^sec-01] The list names no
step, so every assignment below is this reference's reading.

### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a high-energy
implanter as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`DNI <step-008>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`; *alternative:* {ref}`LVTPI <step-020>`

How the step pages grade the SkyWater tool for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Axcelis GSD High current/energy …"** — *inference:* {ref}`DNI <step-008>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`ASTI <step-065>`; *strong for existence:* {ref}`LVTPI <step-020>`, {ref}`PWDEI1 <step-031>`, {ref}`PSDI <step-082>`, {ref}`NSDI <step-086>`; *weak:* {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`
* **Either GSD entry** — *weak (which entry would serve not stated):*
  {ref}`LVTNI <step-015>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`

The inferences for the deep implants rest on the listed energy: "3000kev"
appears only on this entry, and phosphorus is not listed for the
medium-current 8250.[^skw-01]

## Consumables and facilities

The dopant gases and ion-source parts are listed in the
{ref}`materials index <materials-index>`; what is specific to a
high-energy tool is summarised here. None of the SkyWater sources
describes the fab's gas delivery, abatement or radiation protection.

* **Source gases.** Phosphine for the n-type wells and boron trifluoride
  for the p-type wells;[^wiki-implant] phosphine is "a highly toxic
  respiratory poison",[^wiki-ph3] and implanter hydrides are delivered
  from sub-atmospheric sorbent cylinders or dilute high-pressure
  mixtures.[^pat-sds-atmi] The SkyWater entry lists P, B11, BF2 and
  As.[^skw-01]
* **Ion-source parts.** Sources run for multiply charged beams, which
  raises arc power and wear; Horsky gives IHC cathode lives "from 70 h at
  the highest discharge power levels to over 500 h for moderate
  operation".[^horsky-1998-ihc] Axcelis's GSD Ovation upgrade targets
  "source operating costs especially with fluorinated
  species".[^axcelis-gsd-page]
* **Accelerator hardware.** The linac's resonators and RF supplies; an
  Axcelis patent notes that some of these components "are expensive, may
  require maintenance, and occupy valuable space in the
  linac".[^pat-linac-axcelis]
* **Vacuum.** Pumping sized for the outgassing of thick
  resist,[^oconnor-1996][^lee-1996] with the cryopump-regeneration
  hazards Current describes.[^current-1996]
* **Radiation.** "High voltage power supplies used in ion accelerators …
  can pose a risk of electrical injury", and "high-energy atomic
  collisions can generate X-rays and, in some cases, other ionizing
  radiation and radionuclides".[^wiki-implant]
* **Resist.** Thick implant masks: a Hynix triple-well patent specifies
  a resist "at a thickness of over 2.5 μm" for a deep N-well implanted at
  "about 0.6 MeV to about 1.6 MeV",[^pat-dnw-hynix] and the strip that
  removes it afterwards ({ref}`category-strip`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's implant energies and doses are
not public.

* **Retrograde and deep wells.** The {ref}`DNI <step-008>`,
  {ref}`NWI <step-018>` and {ref}`PWI <step-027>` pages describe MeV-class
  well implants from published flows — for example a deep N-well
  implanted at "about 0.6 MeV to about 1.6 MeV"[^pat-dnw-hynix] and a
  retrograde n-well with a deep implant "at an energy of 850,000
  electron volts".[^pat-well-ibm] Tsukamoto et al. review high-energy
  implantation for such wells.[^tsukamoto-1991] The GSD entry's
  10–3000 keV range covers these energies;[^skw-01] the step pages'
  assignment of the wells to it is an inference.
* **Several energies on one tool.** The {ref}`NWI2 <step-019>` and
  {ref}`PWI2 <step-028>` pages note that both implants of each well pair
  fall within the listed 10–3000 keV range, so one tool could run both
  (inference). Where a second implant is shallow enough, the same pages
  offer a medium-current tool; Morris and Rubin found that for multiple
  well implants batch high-energy implanters "have a lower total capital
  cost, footprint, and cost per wafer out than serial medium current
  implanters", with "no significant difference" in transistors from the
  beam-angle variation of a batch end station.[^morris-2000]
* **Multiply charged ions.** The {ref}`DNI <step-008>` page names
  multiply charged phosphorus as a common way to reach MeV energies "at
  the cost of beam current",[^spinelli-1985] and the
  {ref}`NWI <step-018>` page cites doubly charged P⁺⁺ for a retrograde
  well.[^pat-umc-dc] Energy contamination from such beams is a
  machine-side risk that final-energy analysis addresses.[^kubo-1996][^suetsugu-2000]
* **Tilt, channelling and shadowing of wells.** "Zero degree implants
  avoid shadowing effects from resist features but can reduce process
  robustness due to channeling-induced profile variations", and "low
  angle quad implants for retrograde wells eliminate shadowing effects
  while delivering superior process robustness as compared to 0° well
  implants";[^rubin-2002] lateral straggle from the resist edge also
  shifts the threshold voltage of devices near a well
  edge.[^hook-2003] SKY130's well tilt is not public; the SkyWater entry
  lists "tilt/twist" without a range.[^skw-01]
* **Resist crust and outgassing.** The {ref}`DNIS <step-009>` and
  {ref}`LVTPIS <step-021>` strip pages describe a thick crust from MeV
  well implants at modest dose; the machine-side counterpart is the
  outgassing and dose shift of thick resist under MeV
  beams.[^lee-1996][^oconnor-1996]

## Related pages

* {ref}`category-implant` — implantation physics and the 25 implant
  steps of SKY130.
* {ref}`machine-medium-current-implanter` — the beam-line chain in
  detail, and the alternative for the shallower well implants.
* {ref}`machine-high-current-implanter` — the other GSD entry.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — dopant gases, ion-source parts and their
  hazards.
* {ref}`category-strip` — removal of the thick well-implant resist.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the "Axcelis GSD
  High current/energy" entry quoted on this page.[^skw-01]
* SkyWater Technology, *A Day in the Life of a SkyWater Maintenance
  Technician* — in-house implanter maintenance.[^skw-07]
* SkyWater Technology, Form S-1 (2021) — Axcelis named only in a
  biography.[^sec-01]
* Axcelis Technologies, *GSD Ovation* product page — the GSD/HE and
  GSD/VHE linac stages and energies.[^axcelis-gsd-page]
* Axcelis Technologies, *GSD Ovation* press release (2021) — the batch
  GSD family for 200 mm fabs.[^axcelis-gsd]
* Axcelis Technologies, *Our History* — the NV-1000, NV-GSD-HE and HE3
  high-energy implanters.[^axcelis-history]
* Varian Semiconductor, *High Energy Ion Implantation System* (VIISta
  3000) — the single-wafer DC tandem alternative.[^varian-viista3000]
* Glavish and Denholm (Eaton), US 4,667,111 — the RF ion accelerator for
  implantation.[^pat-linac-eaton]
* Divergilio (Axcelis), US 6,653,803 — the GSD/HE linac beam line and its
  resonator modules.[^pat-linac-axcelis]

### High-level understanding

* Wikipedia, *Ion implantation* — implanter classes, linacs and the
  hazards of accelerators.[^wiki-implant]
* Wikipedia, *Axcelis Technologies* and *Varian Semiconductor* — the
  vendors behind the GSD and VIISta lines.[^wiki-axcelis][^wiki-varian]
* Wikipedia, *Phosphine* — the source gas for n-type wells.[^wiki-ph3]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — implantation and
  implanter basics in ch. 8.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ion implantation for VLSI, ch. 9.[^txt-02]

### Deep dive

* Suetsugu et al., IIT 2000 — energy accuracy of the RF-linac NV-GSD-HE
  and its final energy magnet.[^suetsugu-2000]
* Wilson and McIntyre, IIT 1996 — the NV-GSD/VHE, its beam currents and
  multiply charged energies.[^wilson-1996]
* Namaroff and Merrill, IIT 2000 — high-dose MeV boron buried layers on
  the GSD/VHE.[^namaroff-2000]
* Tokoro, Holbrook and Hacker, IIT 2000 — the single-wafer VIISta 3000
  and its tandem beam line.[^tokoro-2000]
* Tokoro et al., IIT 1996 — beam performance of the Genus Tandetron
  1520.[^tokoro-1996]
* Chen and Sinclair (Eaton), US 5,760,409 — dose control compensating
  charge stripping and neutralisation at MeV energies.[^pat-dose-eaton]
* O'Connor and Tokoro, IIT 1996 — end-station and beam-line design for
  MeV resist outgassing.[^oconnor-1996]
* Lee et al., IIT 1996 — thick-resist outgassing and dose shift during MeV
  implants.[^lee-1996]
* Horsky, IIT 1998 — outgassing composition in high-energy and
  high-current implants.[^horsky-1998]
* Horsky, *Rev. Sci. Instrum.* 1998 — an ion source with higher multiply
  charged currents.[^horsky-1998-ihc]
* Kubo et al., IIT 1996 — energy contamination from multiply charged
  implants.[^kubo-1996]
* Spinelli et al., *NIM B* 1985 — multiply charged phosphorus for MeV
  n-wells in production.[^spinelli-1985]
* Tsukamoto et al., *NIM B* 1991 — review of high-energy implantation for
  ULSI.[^tsukamoto-1991]
* Morris and Rubin, IIT 2000 — batch high-energy versus serial
  medium-current implanters for wells.[^morris-2000]
* Rubin, Morris and Jasper, IIT 2002 — 0° versus low-angle quad well
  implants.[^rubin-2002]
* Hook et al. (IBM), *IEEE TED* 2003 — lateral straggle of well implants
  and the mask proximity effect.[^hook-2003]
* Glavish and Farley, IIT 2018 — beam-line innovations across implanter
  classes.[^glavish-2018]
* Oh (Hynix), US 6,806,133 — a triple-well flow with MeV phosphorus and a
  thick mask.[^pat-dnw-hynix]
* Breitwisch, Lam and Slinkman (IBM), US 6,667,205 — retrograde well
  energies and doses.[^pat-well-ibm]
* Yang (UMC), US 5,393,679 — doubly charged phosphorus for a retrograde
  well.[^pat-umc-dc]
* Borland (Genus), US 5,821,589 — MeV buried layers for latch-up
  suppression.[^pat-billi-genus]

## Open questions

* Which GSD model the "Axcelis GSD High current/energy" entry is, and
  whether it and the "Hi dose" entry are two machines or two
  configurations, are not stated.[^skw-01]
* Whether the tool accelerates with an RF linac, as the GSD/HE does, is
  our inference from the model family, not a SkyWater statement.
* The energies, doses, tilts and charge states of SKY130's well implants
  are not public.

<!-- footnotes -->

[^tanjyo-2011]: M. Tanjyo and M. Naito, "History of Ion Implanter and
    Its Future Perspective", *SEI Technical Review* No. 73, October 2011,
    pp. 22–30. <https://global-sei.com/technology/tr/bn73/pdf/73-03.pdf>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^pat-linac-axcelis]: W. F. Divergilio (Axcelis Technologies),
    *Integrated resonator and amplifier system*, US 6,653,803 B1, granted
    2003-11-25. <https://patents.google.com/patent/US6653803B1/en>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed
    2026-08-30; re-checked 2026-09-13.
    <https://www.axcelis.com/products/gsd-ovation/>
[^oconnor-1996]: J. P. O'Connor and N. Tokoro, "End station and beam
    line design considerations for photoresist outgassing with high
    energy (MeV) ion implantation", *Proc. 11th International
    Conference on Ion Implantation Technology (1996)*, pp. 350–354.
    <https://doi.org/10.1109/IIT.1996.586285>
[^wilson-1996]: S. Wilson and E. McIntyre, "Introducing the NV-GSD/VHE
    very high energy implanter", *Proc. 11th International Conference on
    Ion Implantation Technology* (1996), pp. 375–378.
    <https://doi.org/10.1109/IIT.1996.586351>
[^namaroff-2000]: M. Namaroff and J. Merrill, "High energy, high current
    performance of the GSD/VHE implanter for the production of high dose
    p-type buried layers", *Proc. 2000 International Conference on Ion
    Implantation Technology*, pp. 411–414.
    <https://doi.org/10.1109/IIT.2000.924175>
[^axcelis-history]: Axcelis Technologies, *Our History* ("45 Years of
    Innovation"), company web page, accessed 2026-09-13.
    <https://www.axcelis.com/about/our-history/>
[^tokoro-2000]: N. Tokoro, D. Holbrook and D. Hacker, "Introduction of
    the Varian VIISta 3000 single wafer high-energy ion implanter",
    *Proc. 2000 International Conference on Ion Implantation Technology*,
    pp. 368–371. <https://doi.org/10.1109/IIT.2000.924164>
[^tokoro-1996]: N. Tokoro, T. Sakase, C. M. Bowen, P. E. Maciejowski and
    J. P. O'Connor, "The beam performance of the Genus Tandetron 1520 MeV
    implanter", *Proc. 11th International Conference on Ion Implantation
    Technology* (1996), pp. 443–446.
    <https://doi.org/10.1109/IIT.1996.586393>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; implanter entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^glavish-2018]: H. Glavish and M. Farley, "Review of Major Innovations
    in Beam Line Design", *2018 22nd International Conference on Ion
    Implantation Technology (IIT)*, pp. 9–18.
    <https://doi.org/10.1109/IIT.2018.8807986>
[^pat-linac-eaton]: H. F. Glavish and A. S. Denholm (Eaton Corporation),
    *Accelerator for ion implantation*, US 4,667,111 A, granted
    1987-05-19. <https://patents.google.com/patent/US4667111A/en>
[^suetsugu-2000]: N. Suetsugu, H. Kariya, M. Kabasawa and M. Sugitani,
    "Energy accuracy and control method of the NV-GSD-HE", *Proc. 2000
    International Conference on Ion Implantation Technology*, pp.
    448–451. <https://doi.org/10.1109/IIT.2000.924184>
[^varian-viista3000]: Semiconductor Online, *High Energy Ion
    Implantation System* (Varian Semiconductor Equipment product
    description of the VIISta 3000), accessed 2026-09-13.
    <https://www.semiconductoronline.com/doc/high-energy-ion-implantation-system-0001>
[^spinelli-1985]: P. Spinelli, P. Escaron, A. Soubie and M. Bruel, "High
    energy ion implantation for C-MOS isolation n-wells technology:
    Problems related to the use of multicharged phosphorous ions in an
    industrial context", *Nuclear Instruments and Methods in Physics
    Research B* **6**(1–2), 283–286 (1985).
    <https://doi.org/10.1016/0168-583X(85)90646-9>
[^horsky-1998-ihc]: T. N. Horsky, "Indirectly heated cathode arc
    discharge source for ion implantation of semiconductors", *Review of
    Scientific Instruments* **69**(4), 1688–1690 (1998).
    <https://doi.org/10.1063/1.1148866>
[^kubo-1996]: T. Kubo, T. Hisaeda, T. Miyake, T. Ishigaki, M. Kase, K.
    Watanabe and T. Fukuda, "Energy contamination from multiple-charged
    ion implantation in conventional implanter", *Proc. 11th
    International Conference on Ion Implantation Technology* (1996),
    pp. 100–103. <https://doi.org/10.1109/IIT.1996.586141>
[^pat-dose-eaton]: H. Chen and F. Sinclair (Eaton Corporation), *Dose
    control for use in an ion implanter*, US 5,760,409 A, granted
    1998-06-02. <https://patents.google.com/patent/US5760409A/en>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^axcelis-gsd]: Axcelis Technologies, *Axcelis Announces Introduction Of
    The 'GSD Ovation' High Current And High Energy Batch Implanters*, PR
    Newswire, 2021-11-02. <https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>
[^wiki-varian]: Wikipedia, *Varian Semiconductor*.
    <https://en.wikipedia.org/wiki/Varian_Semiconductor>
[^wiki-axcelis]: Wikipedia, *Axcelis Technologies*.
    <https://en.wikipedia.org/wiki/Axcelis_Technologies>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^pat-sds-atmi]: G. M. Tom and J. V. McManus (Advanced Technology
    Materials), *Storage and delivery system for gaseous hydride, halide,
    and organometallic group V compounds*, US 5,518,528 A, granted
    1996-05-21. <https://patents.google.com/patent/US5518528A/en>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^pat-dnw-hynix]: J.-G. Oh (Hynix Semiconductor), *Method for fabricating
    semiconductor device with triple well structure*, US 6,806,133 B2,
    granted 2004-10-19. <https://patents.google.com/patent/US6806133B2/en>
[^pat-well-ibm]: M. J. Breitwisch, C. H. Lam and J. A. Slinkman (IBM),
    *Method of forming retrograde n-well and p-well*, US 6,667,205 B2,
    granted 2003-12-23.
    <https://patents.google.com/patent/US6667205B2/en>
[^tsukamoto-1991]: K. Tsukamoto, S. Komori, T. Kuroi and Y. Akasaka,
    "High-energy ion implantation for ULSI", *Nuclear Instruments and
    Methods in Physics Research B* **59–60**, 584–591 (1991).
    <https://doi.org/10.1016/0168-583X(91)95283-J>
[^morris-2000]: W. Morris and L. Rubin, "Technical and economic
    considerations for retrograde well and channel implants", *Proc.
    2000 International Conference on Ion Implantation Technology*, pp.
    73–76. <https://doi.org/10.1109/IIT.2000.924093>
[^pat-umc-dc]: S.-H. Yang (United Microelectronics), *Use of double
    charge implant to improve retrograde process PMOS punch through
    voltage*, US 5,393,679 A, granted 1995-02-28.
    <https://patents.google.com/patent/US5393679A/en>
[^rubin-2002]: L. M. Rubin, W. Morris and C. Jasper, "Process control
    issues for retrograde well implants for narrow n+/p+ isolation in
    CMOS", *Proc. 2002 International Conference on Ion Implantation
    Technology*, pp. 17–20. <https://doi.org/10.1109/IIT.2002.1257927>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pat-billi-genus]: J. O. Borland (Genus Inc.), *Method for CMOS
    latch-up improvement by MeV BILLI (buried implanted layer for
    lateral isolation) plus buried layer implantation*, US 5,821,589 A,
    granted 1998-10-13. <https://patents.google.com/patent/US5821589A/en>
