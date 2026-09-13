(machine-pecvd)=
# PECVD (and SACVD)

A PECVD system is the single-wafer or multi-station reactor a fab uses
to deposit silicon oxide, silicon nitride and oxynitride at a few
hundred degrees Celsius, low enough for a wafer that already carries
silicide, tungsten or aluminium. A radio-frequency discharge between the
wafer pedestal and a gas showerhead breaks up the precursors so that the
film grows without the heat an LPCVD furnace needs. Sub-atmospheric CVD
(SACVD), which grows oxide from TEOS and ozone without a plasma, is
built on the same single-wafer platforms and is grouped with PECVD here
because a step page offers it as an option. This page describes the
class in general, lists representative 200 mm-era models, and then says
what SkyWater has published about its own tools of this class and which
SKY130 steps this reference assigns to it. The film chemistry and the
growth regimes are on the {ref}`category page <category-deposition>`;
the furnace alternative for the front-end dielectrics is on the
{ref}`LPCVD furnace page <machine-vertical-furnace-lpcvd>`.

| | PECVD (and SACVD) |
|---|---|
| What it does | Deposits dielectric films from gases activated by a discharge "between two electrodes, the space between which is filled with the reacting gases"; plasma deposition is used "onto wafers containing metal layers or other temperature-sensitive structures".[^wiki-pecvd] |
| Plasma excitation | Capacitive, at "the standard 13.56 MHz" or a low frequency "usually around 100 kHz", or "a mixture of low- and high-frequency signals in a dual-frequency reactor";[^wiki-pecvd] "one at 270 kHz and the other at 13.56 MHz" in Pearce et al.'s nitride study.[^pearce-1992] |
| Films and temperatures | Silane–N₂O oxide "deposited at 100°–340°C";[^adams-1981-pecvd] TEOS–O₂ oxide at "about 1 to 50 torr" and "about 200° C. to 500° C." in Applied Materials' reactor patent;[^pat-p5000-amat] plasma nitride "made at 330–350 °C" with "about 20–25 at.% H";[^lanford-1978] oxynitrides across "the entire range of compositions from silicon oxide to silicon nitride".[^denisse-1986] |
| SACVD | "TEOS (tetraethylorthosilicate) and Ozone (O3) chemistry at near-atmospheric pressure", introduced by Applied Materials "in 1994 on its Precision 5000® platform".[^amat-sacvd-2000] |
| Wafer handling | Multi-station: Novellus's Dual Sequel "combines two process chambers with 12 deposition stations";[^novellus-pecvd-1998] twin single-wafer: Applied's Producer has "twin process chambers that permit simultaneous processing of two wafers side-by-side in separate compartments with identical environments".[^amat-producer-2001] |
| 200 mm era | Novellus Concept One ("Introduced in 1987", "150/200mm"), Concept One MAXUS and Concept Two Sequel;[^novellus-pecvd-1998] Applied's Precision 5000 (1987) and Centura platforms,[^amat-1997] and the Producer, introduced in 1998.[^amat-producer-se-2001] |
| SkyWater-listed tool | "Lam/Novellus/AMAT": "PECVD TEOS, C2 and Producer" ("low temp options"), "PECVD silane oxide/nitride/oxynitride, C1" ("low temp, range of R.I. options"), "PECVD nitride C1"[^skw-01] |
| SKY130 steps | 19 steps, plus 1 where the class is an alternative; see {ref}`SKY130 steps assigned to this class <machine-pecvd-steps>` |

## What the machine class is and how it works

A plasma supplies the energy that heat supplies in LPCVD. In a
low-pressure discharge "the electrons can be maintained at very high
equivalent temperatures – tens of thousands of kelvins, equivalent to
several electronvolts average energy—while the neutral atoms remain at
the ambient temperature", and those electrons dissociate the precursor
molecules.[^wiki-pecvd] The wafer can therefore sit at a few hundred
degrees while silane, TEOS, ammonia or nitrous oxide react above it. The
plasma also bombards the growing film with ions, and the balance between
neutral radicals and ions sets the film's density, hydrogen content,
stress and step coverage. What makes a machine a production PECVD tool
is control of that balance across a 200 mm wafer, wafer after wafer:
uniform gas delivery, a stable RF supply, a temperature-controlled
pedestal and a chamber clean that keeps deposits on the walls from
becoming particles on the wafer.

### Capacitive reactors

The production reactors of the period are capacitively coupled. Adams
et al. characterised silane–N₂O oxide in "a parallel‐plate, radial flow,
plasma reactor",[^adams-1981-pecvd] and Sinha et al. made passivation
nitride "at 275°C in an improved radial flow reactor".[^sinha-1978] The
single-wafer reactor of an Applied Materials patent filed in 1986
is "capable of thermal CVD, plasma-enhanced CVD,
plasma-assisted etchback, plasma self-cleaning, and deposition topography
modification by sputtering"; it positions the wafer "with variable,
controlled, close parallel spacing between the wafer and the chamber gas
inlet manifold" and applies "RF energy to the gas inlet manifold", which is
thus the powered electrode.[^pat-p5000-amat] Wikipedia
notes that for TEOS oxide "Pressures of a few torr and small electrode
spacings, and/or dual frequency deposition, are helpful to achieve high
deposition rates with good film stability", and that "Excitation power
of tens to hundreds of watts is typical for an electrode with a diameter
of 200 to 300 mm".[^wiki-pecvd]

### Dual-frequency excitation

A second, low-frequency supply separates ion bombardment from radical
generation. Low frequencies "require several hundred volts to sustain
the discharge. These large voltages lead to high-energy ion bombardment
of surfaces."[^wiki-pecvd] Van de Ven, Connick and Harrus describe the
division of labour for nitride, oxynitride and TEOS oxide: "The main role
of the high-frequency RF is to generate the reactive species and provide
sufficient electron and ion densities. The low frequency is added to
control the ion bombardment to which the substrates are subjected during
deposition."[^van-de-ven-1990] Pearce et al. used the two supplies "to
vary film properties such as stress by altering the amount of power
supplied by each source", and found that "The low-frequency excitation
was seen to favor the formation of N—H bonds in the deposited
film".[^pearce-1992] Novellus's Concept One MAXUS "features an enhanced
dual frequency design",[^novellus-pecvd-1998] and Applied offered its
Producer TEOS oxides "in single and mixed frequency".[^amat-pecvd-teos-2002]

### Multi-station and twin-chamber architectures

The two main vendors reached throughput in different ways. Novellus's
Concept One, its first product, is described as "a two-part system,
consisting of a machine that positions wafers for handling, and a
processing chamber"; the company history counts it a strength that "its
machines process 5 to 7 wafers at a time, while most CVD systems can only
process one at a time".[^novellus-history] Novellus called its
architecture "multi-station sequential deposition" and argued, of the
300 mm version, that it "offers superior reproducibility because every
wafer sees the same environment".[^novellus-pecvd-2002] The Concept Two Sequel put
"the production-proven Concept One process chamber on Concept Two's
modular platform", and the Dual Sequel two such chambers.[^novellus-pecvd-1998]

Applied Materials built single-wafer chambers around a central robot.
The Precision 5000 of 1987 "performs a broad range of deposition
processes utilizing up to four individual chambers on a single
system".[^amat-1997] The Producer "features single-wafer twin process
chambers"; "Up to three Twin Chambers can be mounted on the system,
allowing the simultaneous processing of six wafers".[^amat-producer-2001]

### The films

* **Silane oxide.** Adams et al.'s films "contain 2–9 a/o H", have
  "refractive indexes of about 1.47" and etch "about twelve times faster
  than thermally grown silicon dioxide"; "The step coverage is not
  conformal and the films are thin along vertical step
  walls".[^adams-1981-pecvd]
* **TEOS oxide.** Raupp, Cale and Hey found that the deposition rate
  "increases with increasing applied rf power, increasing total pressure
  and decreasing wafer temperature", and explained it by "both an
  ion-assisted and an oxygen atom initiated pathway".[^raupp-1992] Nguyen
  et al. compared thermal and plasma TEOS in a single-wafer reactor: the
  thermal films "were more conformal than plasma‐deposited TEOS
  films".[^nguyen-1990]
* **Nitride.** In silane–ammonia plasmas Smith et al. found
  aminosilanes that "are believed to be the principal" film
  precursors;[^smith-1990] the films
  carry much hydrogen, "about 20–25 at.% H" in Lanford and Rand's
  measurements,[^lanford-1978] and nitrides "made in nine different
  commercially available reactors" ranged "from 4% to 39%
  (atomic)".[^chow-1982] Cotler and Chapple-Sokol found that stress
  shifts "from tensile to compressive with increasing temperature and
  power" and that "All PECVD film properties, with the exception of
  conformality, are comparable to those of LPCVD films".[^cotler-1993]
* **Oxynitride.** With SiH₄, N₂O and NH₃, Denisse et al. covered the
  whole range from oxide to nitride "by adjusting the N2O/NH3 gas flow
  ratio", and found "the mechanical stress in the oxynitrides is lower
  than in plasma nitride".[^denisse-1986]
* **Doped oxide.** Applied offered a PECVD TEOS PSG "for PMD
  applications, demonstrating outstanding gettering properties, which
  prevent device damage".[^amat-pecvd-psg-2002]

### SACVD: TEOS and ozone without a plasma

Ozone oxidises TEOS thermally at pressures far above a plasma
reactor's. The 1986 Applied Materials reactor patent already claims a conformal
oxide from "ozone, oxygen, tetraethylorthosilicate, and a carrier gas" at
"10 torr to 200 torr".[^pat-p5000-amat] Fujino et al. showed at
atmospheric pressure that "step coverage of the films changed from
isotropic to flow shape with ozone concentration
increase".[^fujino-1990] Applied released its "sub-atmospheric (SA)
process technology" in April 1994 and the Giga-Fill SACVD Centura in
April 1997;[^amat-1997] its product page claims "excellent step
coverage, void-free gap-filling and superior planarization" and a
"ceramic heater, which provides high temperature process capability at
>550°C", for "BPSG and STI applications".[^amat-sacvd-2000] Ozone–TEOS
films are sensitive to the surface they grow on: Kwok et al. studied a
"2 step gap fill process consisting of a thin PECVD underlayer and a
thick SACVD oxide" and traced the surface dependence to "electronegative
species such as fluorine on the surface of the PECVD oxide
underlayer".[^kwok-1994]

### Chamber cleaning

Film grows on the gas manifold and walls as well as on the wafer, and
is removed with a fluorine plasma. Nitrogen
trifluoride "is also widely used to clean PECVD chambers";[^wiki-nf3]
Sobolewski, Langan and Felker studied "NF3/Ar, CF4/O2/Ar, and C2F6/O2/Ar
chamber cleaning plasmas" in a capacitive reactor and note that the
performance of such fluorinated discharges "varies in unpredictable
ways".[^sobolewski-1998] Allgood et
al. measured clean times and perfluorocompound emissions "in a Novellus
Concept One 200, a widely used commercial PECVD tool".[^allgood-2003]
Remote plasma cleans move the discharge out of the chamber: an Applied
patent introduces "reactive species into the processing chamber from a
clean gas that is input to a remote microwave plasma
system",[^pat-rpc-amat] and Applied's Producer SE has "a new low-flow
remote clean that reduces gas costs by up to 40
percent".[^amat-producer-se-2001]

### Plasma charging

A plasma deposition over metal lines connected to gates can charge
and damage the gate oxide. Cheung argues that "Photoconduction is shown
to be the mechanism for plasma charging damage during plasma enhanced
dielectric deposition" and that "The main cause of severe charging damage
is the low level of photoconduction coupled with high processing
temperature".[^cheung-2000]

## Representative 200 mm-era models

* **Novellus Systems.** The Concept One ("Introduced in 1987",
  "150/200mm"), the Concept One MAXUS, the Concept Two Sequel and the
  Concept Two Dual Sequel;[^novellus-pecvd-1998] by 2002 the Sequel
  Express and the VECTOR, "Introduced in 2000" as "a 200mm/300mm bridge
  tool".[^novellus-pecvd-2002] The company history records a
  "$14 million order from Hyundai Electronics for Concept One-200
  plasma-enhanced CVD systems" in 1993.[^novellus-history] Novellus was
  acquired by Lam Research in June 2012.[^wiki-novellus]
* **Applied Materials.** The Precision 5000 (1987), dielectric PECVD on
  the Precision 5000 and Centura platforms "During the 1990s", the
  sub-atmospheric process (1994), the Giga-Fill SACVD Centura (1997) and
  the "DxZ(TM)Optima(TM)" of fiscal 1997;[^amat-1997] the Producer,
  introduced in 1998,[^amat-producer-se-2001] whose film list by 2002
  included TEOS and silane oxides, TEOS and silane PSG, and
  nitrides.[^amat-pecvd-teos-2002][^amat-pecvd-psg-2002][^amat-pecvd-sin-2002]
  In 1997 Applied settled patent litigation with Novellus "concerning
  plasma TEOS and tungsten CVD technology".[^amat-1997]
* **Trikon Technologies.** The {ref}`NCAPOX <step-091>` page names
  Trikon's Delta 201, one of its "CVD products"; the 10-K does not say
  whether it is plasma-enhanced. The Delta 201 was one of
  the products Trikon "obtained with the acquisition of Electrotech on
  November 15, 1996", described as "a versatile, single-chamber
  production system for producing films, including silicon dioxide or
  silicon nitride".[^trikon-10k-1996] Semiconductor Today traces the
  line from Newport-based Electrotech (founded in 1968), bought in 1996
  by Plasma & Materials Technologies, which became Trikon Technologies;
  "Trikon later merged with Aviza Technology Inc in 2005", and in 2009
  Sumitomo Precision Products bought most of Aviza's assets and formed
  SPP Process Technology Systems (SPTS).[^semitoday-spts-2009]

## At SkyWater

### What SkyWater lists

Under "Film Deposition", SkyWater's *Facilities & Capabilities* page
opens with a vendor line and three PECVD entries, each with a
sub-entry:[^skw-01]

> "Lam/Novellus/AMAT"
>
> "PECVD TEOS, C2 and Producer" — "– low temp options"
>
> "PECVD silane oxide/nitride/oxynitride, C1" — "– low temp, range of
> R.I. options"
>
> "PECVD nitride C1" — "– high R.I., low temp options"

Read term by term: a TEOS oxide process on tools called "C2" and
"Producer"; a silane process for oxide, nitride and oxynitride on a tool
called "C1", with a choice of refractive index; and a nitride on "C1"
with a high-index option. The page does not expand "C1" or "C2" or say
which vendor makes which tool. The {ref}`public-sources inventory
<references-public-sources>` (§9) and the step pages read "C1" and "C2"
as Novellus Concept One and Concept Two class tools and "Producer" as
Applied's Producer; these are readings of the names, and the vendor
line lists Lam, Novellus and AMAT together.[^skw-01] No SACVD tool, no
doped PECVD oxide and no deposition temperatures are listed; the only
doped oxide on the page is the HDP entry, "doped and phos doped"
({ref}`HDP-CVD page <machine-hdp-cvd>`).[^skw-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for the vendors and for each process: it is a
SkyWater statement.[^skw-01] The models are not stated, so "Concept
One", "Concept Two" and "Producer" are graded as inferences on the step
pages. The caveats that apply to every listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`. The
vendor line is itself dated: "Lam/Novellus" can only describe Novellus
tools after Novellus became part of Lam in 2012[^wiki-novellus] (our
reading), which fits the page's description of today's fab.

(machine-pecvd-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a PECVD system
(on the PSG page, a PECVD/SACVD system) as the tool or one of
two options (identical to the {ref}`machines index <machines-index>`
table):

{ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`CAPILD <step-135>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`CAPILD2 <step-150>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`, {ref}`NTSD <step-167>`; *alternative:* {ref}`SPNIT <step-076>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"PECVD TEOS, C2 and Producer"** — *inference:* {ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`; *medium (as the whole film):* {ref}`NILD2 <step-105>`; *medium (as the liner or overburden):* {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>`; *not public which of the candidates:* {ref}`POC <step-059>`; *weak:* {ref}`SPOX <step-080>`, {ref}`PSG <step-089>`, {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>`
* **"PECVD silane oxide/nitride/oxynitride, C1", "PECVD nitride C1"** — *inference:* {ref}`LINIT <step-104>`, {ref}`CAPILD <step-135>`, {ref}`CAPILD2 <step-150>`, {ref}`NTSD <step-167>`; *medium:* {ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`, {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`, {ref}`NFUSOX <step-164>`; *not public which of the candidates:* {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`; *strong for existence:* {ref}`SPOX <step-080>`; *weak:* {ref}`SPNIT <step-076>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>`
* **The furnace entries instead** — "Furnaces are all made by Aviza"
  with its LPCVD processes: *inference:* {ref}`GATENIT <step-058>`,
  {ref}`SPNIT <step-076>`; *strong for existence (batch alternative):*
  {ref}`POC <step-059>`, {ref}`SPOX <step-080>`; *weak:*
  {ref}`LINIT <step-104>`; *excluded on thermal grounds (inference):*
  {ref}`NTSD <step-167>`. The full grade list is on the
  {ref}`LPCVD furnace page <machine-vertical-furnace-lpcvd>`.
* **The HDP entry instead** — "Lam/Novellus High Density Plasma (HDP)
  doped and phos doped with sputter etch": *inference:*
  {ref}`PSG <step-089>`, {ref}`NILD2 <step-105>`,
  {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`,
  {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>`; see the
  {ref}`HDP-CVD page <machine-hdp-cvd>`.

The grades follow the film each page describes. The TEOS entry is the
inference for the cap and fuse oxides, on the TEOS oxide under the
passivation nitride of Cypress's Bloomington reports;[^cyp-qtp-014807]
the "C1" entries are the inference where the film is a nitride or, on
this reference's reading, an oxynitride, since "oxynitride" appears only
in the "C1" entry.[^skw-01] On the inter-level oxides the pages give the
gap fill to the HDP entry and grade the PECVD entries for a liner or
overburden, and on {ref}`PSG <step-089>` the TEOS entry is weak because
SkyWater lists no doped PECVD oxide.[^skw-01]

## Consumables and facilities

The precursor gases are listed in the
{ref}`materials index <materials-index>`; what is specific to a PECVD
or SACVD tool is summarised here. None of the SkyWater sources describes
the fab's gas delivery, pumps or abatement.

* **Silicon precursors.** Silane, "a pyrophoric gas (capable of
  autoignition at temperatures below 54 °C or 129 °F)",[^wiki-silane]
  and TEOS, a liquid used "as a precursor to silicon dioxide in the
  semiconductor industry" and delivered as vapour.[^wiki-teos] SkyWater
  names both in its PECVD entries.[^skw-01]
* **Oxidants and nitrogen sources.** N₂O and O₂ for
  oxide,[^adams-1981-pecvd][^pat-p5000-amat] NH₃ or N₂ for
  nitride,[^wiki-pecvd] and N₂O with NH₃ for oxynitride;[^denisse-1986]
  ozone for SACVD.[^amat-sacvd-2000]
* **Chamber-clean gases.** NF₃, "a greenhouse gas, with a global
  warming potential (GWP) 17,200 times greater than that of
  CO2",[^wiki-nf3] or perfluorocarbons such as C₂F₆;[^sobolewski-1998]
  remote plasma cleans reduce the gas used.[^amat-producer-se-2001]
* **RF and heater hardware.** High- and low-frequency generators and
  matching networks,[^pearce-1992] gas inlet manifolds that carry the
  RF power,[^pat-p5000-amat] and heated pedestals or, for SACVD,
  ceramic heaters.[^amat-sacvd-2000]
* **Monitor wafers.** Blanket wafers for {ref}`thickness, refractive
  index, stress <machine-film-thickness-metrology>` and {ref}`particles <machine-defect-inspection>`, as the step pages' industry-generic outlines
  describe
  ({ref}`NCAPOX3 <step-117>`, {ref}`NTSD <step-167>`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's deposition temperatures,
pressures, thicknesses and chemistries are not public.

* **Thermal budget sets the class.** Where the step pages give a
  reason for PECVD, it is what is already on the wafer: the annealed
  tips under the spacer oxide ({ref}`SPOX <step-080>`), TiN and tungsten
  under the local-interconnect nitride cap ({ref}`LINIT <step-104>`),
  and aluminium under the films from {ref}`NILD3 <step-115>` on. The category page gives the
  usual ceiling as "below about 450 °C once aluminium is
  present";[^txt-02] plasma films can be made below it: silane oxide
  at 100–340 °C in Adams et al.'s work,[^adams-1981-pecvd] Applied's
  thin nitride at 400 °C.[^amat-sin-wp]
* **Poor conformality decides the ILD split.** Plasma oxide "is not
  conformal",[^adams-1981-pecvd] so the inter-level oxide pages
  ({ref}`NILD2 <step-105>` to {ref}`NILD6 <step-156>`) infer HDP-CVD
  for the gaps between metal lines and grade PECVD TEOS for a liner or
  overburden, or, on {ref}`NILD2 <step-105>`, where the gap is 1:1, for
  the whole film. Applied described its PECVD TEOS oxides for exactly
  those roles, "as liners or cap layers for HDP-CVD
  applications".[^amat-pecvd-teos-2002]
* **Caps over polished oxide.** The cap-oxide pages from
  {ref}`NCAPOX3 <step-117>` on read
  the cap as a thin plasma oxide that seals the polished surface and,
  by inference, brings the dielectric to its final thickness before the
  next contact or via mask; the PDK's stack diagram gives only the
  finished heights.[^pdk-04]
* **The MiM dielectric.** The PDK describes the capacitor as "a thin
  dielectric over metal, followed by a thin conductor layer on top of the
  dielectric", with an area capacitance `CMIMA` of 2 fF/µm²;[^pdk-07]
  it does not name the dielectric. The {ref}`CAPILD <step-135>` and
  {ref}`CAPILD2 <step-150>` pages read it as a PECVD oxynitride
  (inference, from the "range of R.I. options" of the "C1"
  entry[^skw-01]). PECVD nitride MiM capacitors of the period reached
  "capacitance densities of 1.0 to 2.0 fF/μm²" in a 0.25 µm
  flow;[^kar-roy-1999] nitride ones show "significant degradation in
  capacitor linearity as the frequency is reduced",[^babcock-2001] and
  the high temperature of LPCVD "excludes the use of LPCVD dielectrics for
  MIM capacitors using the standard back-end metal layers as capacitor
  bottom plates".[^van-huylenbroeck-2002] Applied's nitride white paper
  gives a 400 °C nitride "with thickness between 500Å and 1000Å" for MIM
  capacitors.[^amat-sin-wp]
* **Passivation.** The {ref}`NFUSOX <step-164>` and
  {ref}`NTSD <step-167>` pages read the PDK's "TOPOX" and 0.54 µm
  "TOPNIT"[^pdk-04] as a thin PECVD oxide and a PECVD nitride, citing a
  Cypress report from the Bloomington fab whose passivation is "1000Å
  TEOS / 9000Å PECVD Nitride".[^cyp-qtp-014807] The NTSD page sets
  plasma nitride's hydrogen and stress[^lanford-1978] against its role
  as a moisture and mobile-ion barrier.
* **Front-end dielectrics on either class.** For the gate nitride and
  oxide cap ({ref}`GATENIT <step-058>`, {ref}`POC <step-059>`) the step
  pages give PECVD and LPCVD as equal options and say which is used is
  not public; for the spacer nitride ({ref}`SPNIT <step-076>`) PECVD is
  the alternative to the furnace.
* **PSG.** The {ref}`PSG <step-089>` page names a PECVD or SACVD TEOS
  system for a doped oxide as the second option after HDP-CVD; Applied
  sold both routes for pre-metal dielectrics,[^amat-pecvd-psg-2002][^amat-sacvd-2000]
  but SkyWater's list has no doped PECVD or SACVD process.[^skw-01]
* **Charging over metal.** Every back-end PECVD film is deposited over
  metal lines connected to gates; plasma charging during dielectric
  deposition is the mechanism Cheung describes.[^cheung-2000]

## Related pages

* {ref}`category-deposition` — PECVD film chemistry and the deposition
  steps of SKY130.
* {ref}`machine-hdp-cvd` — the gap-fill class that shares the
  inter-level oxide steps.
* {ref}`machine-vertical-furnace-lpcvd` — the batch alternative for the
  front-end nitrides and oxides.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — silane, TEOS and the chamber-clean gases.
* {ref}`category-cmp` — the polish that precedes the cap oxides.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the three PECVD
  entries and their sub-entries quoted on this page.[^skw-01]
* Novellus Systems, *Dielectric – PECVD Solutions* (1998 and 2002
  captures) — the Concept One, MAXUS, Sequel and VECTOR systems and
  multi-station deposition.[^novellus-pecvd-1998][^novellus-pecvd-2002]
* Applied Materials, *PECVD* product page (2001) — the Producer's twin
  chambers.[^amat-producer-2001]
* Applied Materials, *Producer SE* page (2001) — the Producer's 1998
  introduction and the remote clean.[^amat-producer-se-2001]
* Applied Materials, Producer film pages (2002) — PECVD TEOS oxide, TEOS
  PSG and nitride
  applications.[^amat-pecvd-teos-2002][^amat-pecvd-psg-2002][^amat-pecvd-sin-2002]
* Applied Materials, *SACVD* product page (2000) — TEOS–ozone
  sub-atmospheric CVD and the Giga-Fill chamber.[^amat-sacvd-2000]
* Applied Materials, *1997 Annual Report* — dates of the Precision 5000,
  SACVD and DxZ products and the Novellus settlement.[^amat-1997]
* Wang et al. (Applied Materials), US 5,000,113 — a single-wafer
  thermal and plasma CVD reactor and its TEOS processes.[^pat-p5000-amat]
* SkyWater PDK Authors, *Device Details* and `metal_stack.svg` — the MiM
  capacitor construction and the passivation layers.[^pdk-07][^pdk-04]
* Cypress Semiconductor, QTP 014807 — a TEOS and PECVD nitride
  passivation from the Bloomington fab.[^cyp-qtp-014807]
* Trikon Technologies, Form 10-K for 1996 — the Delta 201 CVD system
  and its Electrotech origin.[^trikon-10k-1996]

### High-level understanding

* Semiconductor Today, *Sumitomo Precision Products completes
  acquisition of Aviza* (2009) — the Electrotech, Trikon, Aviza and SPTS
  lineage.[^semitoday-spts-2009]
* Wikipedia, *Plasma-enhanced chemical vapor deposition* — discharges,
  excitation frequencies and the films.[^wiki-pecvd]
* Wikipedia, *Silane*, *Tetraethyl orthosilicate* and *Nitrogen
  trifluoride* — the precursors and the clean gas.[^wiki-silane][^wiki-teos][^wiki-nf3]
* Wikipedia, *Novellus Systems* — the vendor and its acquisition by
  Lam.[^wiki-novellus]
* Encyclopedia.com, *Novellus Systems, Inc.* — the Concept One and
  Concept Two history.[^novellus-history]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — CVD and PECVD
  films.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — CVD
  dielectrics and the back-end thermal limit.[^txt-02]
* Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing* — capacitive discharges and plasma
  deposition.[^lieberman-2005]

### Deep dive

* Adams et al., *J. Electrochem. Soc.* 1981 — silane–N₂O plasma oxide
  in a radial-flow reactor.[^adams-1981-pecvd]
* Raupp, Cale and Hey, *JVST B* 1992 — ion-assisted and oxygen-atom
  pathways in plasma TEOS oxide.[^raupp-1992]
* Nguyen et al., *J. Electrochem. Soc.* 1990 — plasma and thermal TEOS
  oxide in a single-wafer reactor.[^nguyen-1990]
* Smith et al., *J. Electrochem. Soc.* 1990 — the precursors of plasma
  nitride in silane–ammonia discharges.[^smith-1990]
* Lanford and Rand, *JAP* 1978 — the hydrogen content of plasma
  nitride.[^lanford-1978]
* Chow et al., *JAP* 1982 — hydrogen in nitrides from nine commercial
  reactors.[^chow-1982]
* Sinha et al., *J. Electrochem. Soc.* 1978 — plasma nitride for
  passivation.[^sinha-1978]
* Cotler and Chapple-Sokol, *J. Electrochem. Soc.* 1993 — PECVD nitride
  against LPCVD nitride.[^cotler-1993]
* Denisse et al., *JAP* 1986 — composition and stress of plasma
  oxynitrides.[^denisse-1986]
* Van de Ven, Connick and Harrus, VMIC 1990 — dual-frequency PECVD of
  ILD and passivation films.[^van-de-ven-1990]
* Pearce et al., *JAP* 1992 — nitride properties with 270 kHz and
  13.56 MHz supplies.[^pearce-1992]
* Fujino et al., *J. Electrochem. Soc.* 1990 — TEOS–ozone oxide and its
  flow-like step coverage.[^fujino-1990]
* Kwok et al., *J. Electrochem. Soc.* 1994 — surface sensitivity of
  SACVD oxide on PECVD underlayers.[^kwok-1994]
* Sobolewski, Langan and Felker, *JVST B* 1998 — electrical behaviour of
  PECVD chamber-clean plasmas.[^sobolewski-1998]
* Allgood et al., *J. Electrochem. Soc.* 2003 — chamber-clean chemistry
  in a Novellus Concept One 200.[^allgood-2003]
* Fong et al. (Applied Materials), US 5,812,403 — a remote microwave
  plasma chamber clean.[^pat-rpc-amat]
* Cheung, P2ID 2000 — the charging mechanism in plasma dielectric
  deposition.[^cheung-2000]
* Kar-Roy et al., IITC 1999 — PECVD nitride MiM capacitors in a
  0.25 µm back end.[^kar-roy-1999]
* Babcock et al., *IEEE EDL* 2001 — dispersion in nitride MiM
  capacitors.[^babcock-2001]
* Van Huylenbroeck et al., *IEEE EDL* 2002 — PECVD dielectrics for
  non-dispersive MiM capacitors.[^van-huylenbroeck-2002]
* D'Cruz, Bencher and Ngai (Applied Materials), PECVD nitride white
  paper — thin nitrides for etch stops, barriers and MIM
  capacitors.[^amat-sin-wp]

## Open questions

* Which tools SkyWater's "C1" and "C2" are, and whether "Producer" is an
  Applied Materials Producer, are not stated.[^skw-01]
* Whether the cap and fuse oxides are TEOS or silane oxides, and the
  MiM dielectric an oxynitride or a nitride, are not public.
* Whether any SKY130 dielectric is deposited by SACVD, which SkyWater
  does not list, is not public.
* The model list above is incomplete: it covers the Novellus, Applied
  Materials and Trikon systems for which a public description was found,
  not the ASM and other PECVD systems of the period.

<!-- footnotes -->

[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^pearce-1992]: C. W. Pearce, R. F. Fetcho, M. D. Gross, R. F. Koefer and
    R. A. Pudliner, "Characteristics of silicon nitride deposited by
    plasma-enhanced chemical vapor deposition using a dual frequency
    radio-frequency source", *Journal of Applied Physics* **71**(4),
    1838–1841 (1992). <https://doi.org/10.1063/1.351396>
[^adams-1981-pecvd]: A. C. Adams, F. B. Alexander, C. D. Capio and
    T. E. Smith, "Characterization of Plasma-Deposited Silicon Dioxide",
    *Journal of The Electrochemical Society* **128**(7), 1545–1551
    (1981). <https://doi.org/10.1149/1.2127680>
[^pat-p5000-amat]: D. N. Wang, J. M. White, K. S. Law, C. Leung,
    S. P. Umotoy, K. S. Collins, J. A. Adamik, I. Perlov and D. Maydan
    (Applied Materials), *Thermal CVD/PECVD reactor and use for thermal
    chemical vapor deposition of silicon dioxide and in-situ multi-step
    planarized process*, US 5,000,113 A, filed 1986-12-19, granted
    1991-03-19. <https://patents.google.com/patent/US5000113A/en>
[^lanford-1978]: W. A. Lanford and M. J. Rand, "The hydrogen content of
    plasma-deposited silicon nitride", *Journal of Applied Physics*
    **49**(4), 2473–2477 (1978). <https://doi.org/10.1063/1.325095>
[^denisse-1986]: C. M. M. Denisse, K. Z. Troost, J. B. Oude Elferink,
    F. H. P. M. Habraken, W. F. van der Weg and M. Hendriks,
    "Plasma-enhanced growth and composition of silicon oxynitride films",
    *Journal of Applied Physics* **60**(7), 2536–2542 (1986).
    <https://doi.org/10.1063/1.337117>
[^amat-sacvd-2000]: Applied Materials, *SACVD* (Giga-Fill SACVD Centura),
    product page; Wayback Machine capture of 2000-07-09.
    <https://web.archive.org/web/20000709131617/http://www.appliedmaterials.com:80/products/sacvd.html>
[^novellus-pecvd-1998]: Novellus Systems, *Dielectric – PECVD Solutions*,
    product page; Wayback Machine capture of 1998-06-11.
    <https://web.archive.org/web/19980611202815/http://www.novellus.com:80/products/pecvd.htm>
[^amat-producer-2001]: Applied Materials, *PECVD* (Producer), product
    page; Wayback Machine capture of 2001-08-17.
    <https://web.archive.org/web/20010817124824/http://www.appliedmaterials.com:80/products/pecvd.html>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^amat-producer-se-2001]: Applied Materials, *Producer SE*, product page;
    Wayback Machine capture of 2001-08-17.
    <https://web.archive.org/web/20010817134045/http://www.appliedmaterials.com:80/products/producer_se.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; film deposition entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sinha-1978]: A. K. Sinha, H. J. Levinstein, T. E. Smith, G. Quintana and
    S. E. Haszko, "Reactive Plasma Deposited Si-N Films for MOS-LSI
    Passivation", *Journal of The Electrochemical Society* **125**(4),
    601–608 (1978). <https://doi.org/10.1149/1.2131509>
[^van-de-ven-1990]: E. P. van de Ven, I.-W. Connick and A. S. Harrus,
    "Advantages of dual frequency PECVD for deposition of ILD and
    passivation films", *Proc. Seventh International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1990)*, pp. 194–201.
    <https://doi.org/10.1109/VMIC.1990.127865>
[^amat-pecvd-teos-2002]: Applied Materials, *Producer PECVD TEOS Oxide*,
    product page; Wayback Machine capture of 2002-07-01.
    <https://web.archive.org/web/20020701042739/http://www.appliedmaterials.com:80/products/pecvd_teos_oxide.html>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.* (company
    history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^novellus-pecvd-2002]: Novellus Systems, *Dielectric – PECVD Solutions*,
    product page; Wayback Machine capture of 2002-06-02.
    <https://web.archive.org/web/20020602073706/http://www.novellus.com:80/products/pecvd.asp>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
[^nguyen-1990]: S. Nguyen, D. Dobuzinsky, D. Harmon, R. Gleason and
    S. Fridmann, "Reaction Mechanisms of Plasma- and Thermal-Assisted
    Chemical Vapor Deposition of Tetraethylorthosilicate Oxide Films",
    *Journal of The Electrochemical Society* **137**(7), 2209–2215
    (1990). <https://doi.org/10.1149/1.2086914>
[^smith-1990]: D. L. Smith, A. S. Alimonda, C.-C. Chen, S. E. Ready and
    B. Wacker, "Mechanism of SiNₓHᵧ Deposition from NH₃-SiH₄ Plasma",
    *Journal of The Electrochemical Society* **137**(2), 614–623 (1990).
    <https://doi.org/10.1149/1.2086517>
[^chow-1982]: R. Chow, W. A. Lanford, K.-M. Wang and R. S. Rosler,
    "Hydrogen content of a variety of plasma-deposited silicon nitrides",
    *Journal of Applied Physics* **53**(8), 5630–5633 (1982).
    <https://doi.org/10.1063/1.331445>
[^cotler-1993]: T. J. Cotler and J. Chapple-Sokol, "High Quality
    Plasma-Enhanced Chemical Vapor Deposited Silicon Nitride Films",
    *Journal of The Electrochemical Society* **140**(7), 2071–2075
    (1993). <https://doi.org/10.1149/1.2220766>
[^amat-pecvd-psg-2002]: Applied Materials, *Producer PECVD TEOS PSG*,
    product page; Wayback Machine capture of 2002-07-05.
    <https://web.archive.org/web/20020705144451/http://www.appliedmaterials.com:80/products/pecvd_teos_psg.html>
[^fujino-1990]: K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
    "Silicon Dioxide Deposition by Atmospheric Pressure and
    Low-Temperature CVD Using TEOS and Ozone", *Journal of The
    Electrochemical Society* **137**(9), 2883–2887 (1990).
    <https://doi.org/10.1149/1.2087093>
[^kwok-1994]: K. Kwok, E. Yieh, S. Robles and B. C. Nguyen, "Surface
    Related Phenomena in Integrated PECVD/Ozone-TEOS SACVD Processes for
    Sub-Half Micron Gap Fill: Electrostatic Effects", *Journal of The
    Electrochemical Society* **141**(8), 2172–2177 (1994).
    <https://doi.org/10.1149/1.2055081>
[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*.
    <https://en.wikipedia.org/wiki/Nitrogen_trifluoride>
[^sobolewski-1998]: M. A. Sobolewski, J. G. Langan and B. S. Felker,
    "Electrical optimization of plasma-enhanced chemical vapor deposition
    chamber cleaning plasmas", *Journal of Vacuum Science & Technology B*
    **16**(1), 173–182 (1998). <https://doi.org/10.1116/1.589774>
[^allgood-2003]: C. Allgood, M. Mocella, H. Chae and H. Sawin,
    "Evaluation of Octafluorocyclobutane as a Chamber Clean Gas in a
    Plasma-Enhanced Silicon Dioxide Chemical Vapor Deposition Reactor",
    *Journal of The Electrochemical Society* **150**(2), G122 (2003).
    <https://doi.org/10.1149/1.1535911>
[^pat-rpc-amat]: G. Fong, L.-Q. Xia, S. Nemani and E. Yieh (Applied
    Materials), *Methods and apparatus for cleaning surfaces in a
    substrate processing system*, US 5,812,403 A, filed 1996-11-13,
    granted 1998-09-22. <https://patents.google.com/patent/US5812403A/en>
[^cheung-2000]: K. P. Cheung, "On the mechanism of plasma enhanced
    dielectric deposition charging damage", *Proc. 2000 5th International
    Symposium on Plasma Process-Induced Damage (P2ID)*, pp. 161–163.
    <https://doi.org/10.1109/PPID.2000.870658>
[^wiki-novellus]: Wikipedia, *Novellus Systems*.
    <https://en.wikipedia.org/wiki/Novellus_Systems>
[^amat-pecvd-sin-2002]: Applied Materials, *Producer PECVD Nitride*,
    product page; Wayback Machine capture of 2002-07-01.
    <https://web.archive.org/web/20020701050143/http://www.appliedmaterials.com:80/products/pecvd_nitride.html>
[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology Derivative
    R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005 (copy hosted by
    Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, section "MiM capacitors".
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^kar-roy-1999]: A. Kar-Roy, C. Hu, M. Racanelli, C. A. Compton, P. Kempf,
    G. Jolly, P. N. Sherman, J. Zheng, Z. Zhang and A. Yin, "High density
    metal insulator metal capacitors using PECVD nitride for mixed signal
    and RF circuits", *Proc. IEEE 1999 International Interconnect
    Technology Conference*, pp. 245–247.
    <https://doi.org/10.1109/IITC.1999.787134>
[^babcock-2001]: J. A. Babcock, S. G. Balster, A. Pinto, C. Dirnecker,
    P. Steinmann, R. Jumpertz and B. El-Kareh, "Analog characteristics of
    metal-insulator-metal capacitors using PECVD nitride dielectrics",
    *IEEE Electron Device Letters* **22**(5), 230–232 (2001).
    <https://doi.org/10.1109/55.919238>
[^van-huylenbroeck-2002]: S. Van Huylenbroeck, S. Decoutere, R. Venegas,
    S. Jenei and G. Winderickx, "Investigation of PECVD dielectrics for
    nondispersive metal-insulator-metal capacitors", *IEEE Electron Device
    Letters* **23**(4), 191–193 (2002).
    <https://doi.org/10.1109/55.992835>
[^amat-sin-wp]: L. D'Cruz, C. Bencher and C. Ngai (Applied Materials),
    *PECVD SiN performance as barrier/etch stop for Damascene copper
    interconnects*, white paper, undated; Wayback Machine capture of
    2003-03-08.
    <https://web.archive.org/web/20030308041708/http://www.appliedmaterials.com:80/products/assets/dielectric/pecvd_sin_performance.pdf>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles of
    Plasma Discharges and Materials Processing*, 2nd ed., Wiley, 2005,
    ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
[^trikon-10k-1996]: Trikon Technologies, Inc., *Annual Report on Form
    10-K for the fiscal year ended December 31, 1996*; copy on
    GetFilings.com, Wayback Machine capture of 2008-10-12.
    <http://web.archive.org/web/20081012193325/http://www.getfilings.com/o0000898430-97-001539.html>
[^semitoday-spts-2009]: Semiconductor Today, *Sumitomo Precision
    Products completes acquisition of Aviza*, news item, 2009-10-19.
    <https://www.semiconductor-today.com/news_items/2009/OCT/STS_191009.htm>
