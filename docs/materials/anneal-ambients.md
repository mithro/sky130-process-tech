(material-anneal-ambients)=
# Anneal ambients

An anneal ambient is the gas a wafer sits in while it is heated. Most
anneals use an inert gas — nitrogen or argon — so that the heat changes
the wafer without the gas reacting with it; some add a little oxygen to
grow or repair an oxide, ammonia to nitride a surface, or hydrogen to
passivate interfaces and keep metals and silicon from oxidising.
Hydrogen is often supplied diluted in nitrogen as
{term}`forming gas`, and the same mixture is used in downstream plasma
ashers to strip resist. The materials index assigns forming gas to this
page; nitrogen, argon and oxygen belong to the process-gas class and
ammonia to the precursor class, which the
{ref}`materials index <materials-index>` assigns to class pages of their
own, and they are discussed here only in their role as anneal ambients. On the step pages' readings,
SKY130 uses forming gas in the two {term}`alloy anneals <alloy anneal>`
and in the ash of thirty resist strips. This page describes the class in
general, lists representative mixtures, and then says what SkyWater has
published about its anneal and ash ambients and which SKY130 steps name
forming gas. The anneal physics is on the
{ref}`anneal category page <category-anneal>`; the tools are on the
{ref}`anneal and alloy furnace <machine-vertical-furnace-anneal>`,
{ref}`rapid thermal processor <machine-rapid-thermal-processor>` and
{ref}`downstream plasma asher <machine-downstream-plasma-asher>` pages.

| | Anneal ambients |
|---|---|
| What they do | Set what the gas does to the wafer during a thermal step; forming gas is "used as an atmosphere for processes that need the properties of hydrogen gas", and "a high-temperature anneal in forming gas assists in silicon-silicon dioxide interface passivation".[^wiki-fg] |
| Forming gas | "Typical forming gas formulations (5% H2 in N2) are not explosive";[^wiki-fg] an asher gas line of "4 percent H2/N2";[^semistar-iridia] "N2/H2 where the H2 portion is 2%" as an ashing gas.[^wiki-ash] |
| Hydrogen chemistry | Hydrogen passivates Si/SiO₂ interface traps[^reed-1988][^cartier-1993] and can also deactivate boron acceptors in silicon.[^sah-1983] |
| Inert and reactive ambients | Nitrogen and argon for inert anneals; argon annealing suppressed gate-oxide thinning at STI edges;[^ohashi-2007] oxygen and ammonia as reactive additions (materials index). |
| Hazards | Hydrogen's flammability limits in air are 4 % and 75 % by volume.[^wiki-flammability] |
| SkyWater evidence | "H2 and forming gas alloy"; "Ar anneal to 1150C"; "N2 anneal to 1150C"; "Ag Heatpulse 8808 NH3, Ar, N2, O2"; asher gases "H2/N2" and "H2>N2";[^skw-01] gas suppliers in both filings[^sec-01][^sec-02] |
| SKY130 steps | 32 steps; see {ref}`SKY130 steps that use this class <material-anneal-ambients-steps>` |

## What the class is and what it does

An anneal is defined as much by its ambient as by its temperature. In a
furnace or a lamp-heated chamber the ambient is flowed through the tube
or chamber, purged before and after, and chosen so that the wafer
surface ends in the state the next step needs: unoxidised, lightly
oxidised, nitrided or hydrogen-passivated. The anneal category page sets
out the anneal types of the SKY130 flow ({ref}`category-anneal`); this
section describes the gases.

### Inert ambients: nitrogen and argon

Nitrogen is the default inert ambient and purge gas; argon is used where
nitrogen itself would react (industry practice). Ohashi, Kubota and Nakajima used an argon
anneal to suppress gate-oxide thinning at the STI edge.[^ohashi-2007]
The ambient in which an oxide is cooled matters: Razouk and Deal found
large interface-state densities in oxides cooled in nitrogen or argon,
which a low-temperature hydrogen anneal reduces.[^razouk-1979] Deal's
terminology names the charges involved.[^deal-1980]

### Oxygen and ammonia additions

A small oxygen flow in an inert anneal grows a thin oxide or keeps a
surface from roughening, and ammonia nitrides a surface in a rapid
thermal chamber (industry practice); the step pages that use these
ambients name the gases under their own rows ({ref}`materials index <materials-table>`).

### Forming gas in anneals

Forming gas brings hydrogen to the wafer below its flammable
concentration. Hydrogen diffuses through oxide at alloy temperatures
and ties up dangling bonds at the Si/SiO₂ interface: Reed and Plummer
set out the chemistry of interface-trap annealing;[^reed-1988] Cartier,
Stathis and Buchanan the passivation and depassivation of dangling bonds
by atomic hydrogen;[^cartier-1993] Brower the dissociation kinetics of the
passivated defects;[^brower-1990] and Stesmans the passivation of P_b0 and
P_b1 centres by molecular hydrogen.[^stesmans-1996] Hydrogen also repairs
damage from plasma steps: Rangan, Krishnan and Ashok studied hydrogen and
deuterium passivation of process-induced damage,[^rangan-1998] of the kind
Fang and McVittie described in thin oxides charged during plasma
processing.[^fang-1992]

The isotope matters. Lyding, Hess and Kizilyalli reported that
"replacing hydrogen with deuterium during the final wafer sintering
process greatly reduces hot electron degradation
effects";[^lyding-1996] Kizilyalli et al. applied deuterium anneals to
multilevel metal/dielectric MOS systems in manufacturing;[^kizilyalli-1998]
and a University of Illinois patent gives an example anneal "in an
ambient of 10% deuterium in nitrogen".[^pat-deuterium-uiuc] Hydrogen has
other effects that bear on the recipe: it deactivates boron acceptors in
silicon,[^sah-1983][^pankove-1983] and it affects nitride
charge-trapping memories, whose retention a high-temperature
post-nitridation hydrogen anneal improved in MNOS
transistors.[^maes-1981]
Plasma-deposited nitride
itself carries hydrogen, some 20–25 at.% in films deposited at
330–350 °C, which Lanford and Rand measured.[^lanford-1978]

### Forming gas in ashers

A downstream asher strips resist with the neutral products of a remote
plasma. Wikipedia lists "N2/H2 where the H2 portion is 2%" among ashing
gases besides oxygen and fluorine;[^wiki-ash] a used Iridia module of
the kind SkyWater lists has a "4 percent H2/N2" line.[^semistar-iridia]
Additions change the ash chemistry: Fujimura et al. found that 1 % water
vapour lowered the activation energy of downstream O₂ ashing of a novolak
resist more than 3 % hydrogen did, which they attributed to OH
radicals.[^fujimura-1991] Hydrogen also limits oxidation of
exposed metal: Xu and Diao found that tungsten oxidised rapidly in an O₂
downstream plasma, that "oxidation can be reduced effectively by adding
H2", and that added N₂ lowered the efficiency of the hydrogen.[^xu-2008]

## Representative materials and grades

Anneal ambients are bulk or cylinder gases bought to purity
specifications and mixed at the tool or supplied premixed; SKY130's
mixtures and purities are not public.

* **Premixed forming gas.** "Typical forming gas formulations (5% H2 in
  N2)";[^wiki-fg] the anneal category page gives 4–10 % H₂ in N₂
  ({ref}`category-anneal`), and an Iridia asher's gas lines include "4
  percent H2/N2".[^semistar-iridia]
* **Hydrogen and nitrogen mixed at the tool.** The ALLY pages name this
  as the alternative to premixed forming gas; the University of Illinois
  example meters "10% by volume hydrogen in nitrogen" for a hydrogen
  anneal.[^pat-deuterium-uiuc]
* **Deuterium mixtures.** Deuterium in nitrogen for hot-carrier-resistant
  sinters.[^lyding-1996][^pat-deuterium-uiuc]
* **Inert, oxidising and nitriding ambients.** Nitrogen and argon;
  oxygen additions; ammonia in rapid thermal nitridation — described with
  their rows in the {ref}`materials index <materials-table>`.

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page lists anneal and ash ambients
on three groups of tools.[^skw-01] Under "Furnaces/Diffusion/Pre-Clean":

> "Furnaces are all made by Aviza" · "Ar anneal to 1150C" · "N2 anneal
> to 1150C" · "H2 and forming gas alloy"

under "RTA":

> "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to 1200C"

and under "Resist removal/cleans":

> "Gasonic PEP, remote microwave plasma, N2, O2, 120C – 270C"
>
> "Iridia RF microwave, N2, O2, H2, CF4, NH3, H2/N2, 40C-270C"
>
> "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up to 250C"

Read term by term, the furnaces run argon and nitrogen anneals and an
alloy in hydrogen and in forming gas; the Heatpulse lists no hydrogen or
forming gas; and two of the three ashers list a hydrogen–nitrogen
mixture, written "H2/N2" on the Iridia and "H2>N2" on the Aspen, which
the {ref}`asher page <machine-downstream-plasma-asher>` reads as hydrogen
in nitrogen; SkyWater does not explain the notation. The page gives no
hydrogen fraction.[^skw-01] The filings name gas suppliers but not the
gases each supplies:[^sec-01][^sec-02]

| Filing | Gas suppliers as named |
|--------|------------------------|
| S-1 (2021)[^sec-01] | "Air Products & Chemicals, Inc. (bulk and specialty gases, chemicals)"; "Praxair, Inc. (bulk and specialty gases)" |
| 10-K for fiscal 2023[^sec-02] | "Linde, Inc. (bulk and specialty gases)"; "Airgas USA LLC (specialty gases)"; "EMD Performance Materials Corp (Versum) (specialty chemicals and gases)" |

Neither filing names forming gas, hydrogen or deuterium, and neither says
whether hydrogen mixtures are bought premixed or blended on site.

### Strength of the evidence

The furnace, RTA and asher entries are SkyWater statements and rank as
**strong** evidence that hydrogen and forming-gas alloys, argon and
nitrogen anneals, and hydrogen–nitrogen ash chemistries exist at the fab,
on the scale of the {ref}`machines index <machines-reading-evidence>`;
they tie no ambient to a step.[^skw-01] The supplier lists are strong as
statements but name no gas or mixture.[^sec-01][^sec-02] The mixture
fractions on this page — 2 %, 4 %, 5 % and 10 % — come from Wikipedia, a
dealer listing and a patent, not from SkyWater.[^wiki-fg][^wiki-ash][^semistar-iridia][^pat-deuterium-uiuc]

(material-anneal-ambients-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells). Nitrogen,
argon, oxygen and ammonia, which the step pages also use as anneal
ambients, are listed under their own rows.

Materials index rows covered:

* `forming-gas` — forming gas (H₂ in N₂)

Steps:

{ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`LICM1E <step-094>`, {ref}`SACETCH <step-095>`, {ref}`ALLY1 <step-096>`, {ref}`CTME <step-108>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`VIM3E <step-145>`, {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`, {ref}`ALLY <step-170>`

The steps fall into three groups, as the step pages' *Resources
required* sections describe them:

* **Alloy anneals** — {ref}`ALLY1 <step-096>` before the contact liner and
  {ref}`ALLY <step-170>` after the pad etch, both reading SkyWater's "H2
  and forming gas alloy" as the process.
* **Implant and etch-mask strips** — the ash after the front-end etches
  and implants, from {ref}`STIE <step-006>` to
  {ref}`NSDIS <step-087>`, where the pages name oxygen, nitrogen and
  forming gas for the ash.
* **Post-etch strips in the back end** — the contact, via, metal and
  seal-ring etches, and the strip at {ref}`SACETCH <step-095>`, where the
  pages add forming gas or H₂/N₂ to the O₂/N₂ ash.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's hydrogen or
forming-gas supply, gas cabinets or exhaust; the points below are
industry practice or public reference statements.

* **Flammability.** Hydrogen burns in air between 4 % and 75 % by
  volume;[^wiki-flammability] typical forming-gas formulations (5 % H₂
  in N₂) "are not explosive",[^wiki-fg] which is why forming gas is
  preferred where the tool is not
  rated for pure hydrogen (the ALLY pages' reading). Richer hydrogen needs
  the interlocks, purges and exhaust of a flammable gas
  ({ref}`machine-vertical-furnace-anneal`).
* **Purges.** The typical alloy recipes on the step pages purge the tube
  of oxygen before hydrogen is admitted and purge the hydrogen before
  ramp-down ({ref}`ALLY1 <step-096>`, {ref}`ALLY <step-170>`).
* **Hazardous-materials management.** SkyWater's S-1 states that it
  uses, generates and discharges "hazardous chemicals and waste" in its
  operations and that its facilities are ISO 14001 certified.[^sec-01]
* **Purity.** Oxygen and water in an anneal ambient oxidise what the
  anneal is meant to protect, which is why inert and reducing ambients
  are bought to high purity and delivered through clean lines (industry
  practice; {ref}`category-anneal`).

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's anneal and ash ambients, fractions and
temperatures are not public.

* **Two alloys, one listed process.** On their pages' readings,
  {ref}`ALLY1 <step-096>` and {ref}`ALLY <step-170>` both run on the Aviza
  furnaces' "H2 and forming gas alloy", the only listed anneal with
  hydrogen; the Heatpulse lists "NH3, Ar, N2, O2" only.[^skw-01] Whether
  SKY130 uses premixed forming gas, hydrogen blended at the tool, or
  deuterium is not public.
* **Hydrogen and the SONOS cells.** In Maes, Usmani and Heyns's MNOS
  transistors, a high-temperature post-nitridation hydrogen anneal
  improved retention at 125 °C by removing hole back-tunnelling to
  interface states;[^maes-1981] how the much cooler final alloy, which
  reaches the {term}`SONOS` stack of {ref}`ONO <step-040>` through the
  whole back end, affects SONOS retention is not public. The ALLY pages
  treat time and hydrogen content as the recipe's bounds (their
  reading).
* **Boron and hydrogen.** Hydrogen deactivates boron acceptors,[^sah-1983]
  and the {ref}`ALLY1 <step-096>` page reads the need not to deactivate
  the boron of the P⁺ source/drains as a limit on the alloy's time and
  temperature.
* **Forming gas over exposed metal.** The via and metal-etch strips run
  with tungsten plugs or aluminium exposed; hydrogen in an O₂ plasma
  reduces tungsten oxidation,[^xu-2008] one reason the back-end strip
  pages add H₂/N₂ to the ash (our reading).
* **Hydrogen already in the stack.** On the NTSD page's reading, the
  passivation nitride of {ref}`NTSD <step-167>` is plasma nitride, which
  carries hydrogen of its own;[^lanford-1978] the ALLY page notes that which source dominates the
  final passivation of interface traps is not public.

## Related pages

* {ref}`category-anneal` — anneal types, the alloy anneals and their
  ambients.
* {ref}`machine-vertical-furnace-anneal` — the anneal and alloy furnace.
* {ref}`machine-downstream-plasma-asher` — the ashers that use forming gas.
* {ref}`machine-rapid-thermal-processor` — the lamp anneals and their
  gases.
* {ref}`materials-index` — nitrogen, argon, oxygen and ammonia rows and
  all consumable classes.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the furnace, RTA and
  asher entries quoted above.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  gas suppliers and hazardous-materials statements.[^sec-01][^sec-02]
* SemiStar Corp., *Novellus Gasonics PEP Iridia DL* listing — an asher's
  4 % H₂/N₂ gas line.[^semistar-iridia]
* Lyding and Hess (University of Illinois), US 5,872,387 — deuterium and
  hydrogen anneal mixtures.[^pat-deuterium-uiuc]
* Moov, *Aviza / SVG / Thermco AVP 8000* listing; ASM, *Vertical
  furnace* — furnace platforms of the class.[^aviza-avp][^asm-vf]
* Mattson Technology, *The Aspen Strip* — the Aspen strip
  platforms.[^mattson-2001]

### High-level understanding

* Wikipedia, *Forming gas*, *Plasma ashing* and *Flammability limit* —
  the mixtures, their use and hydrogen's flammability
  limits.[^wiki-fg][^wiki-ash][^wiki-flammability]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — anneals and the
  final forming-gas anneal.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — alloy
  anneals and metallisation.[^txt-02]
* Deal, *IEEE TED* 1980 — the terminology of oxide charges.[^deal-1980]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — thermal processing and gas systems.[^txt-09]

### Deep dive

* Razouk and Deal, *JES* 1979 — interface states against oxidation,
  cooling and hydrogen annealing.[^razouk-1979]
* Reed and Plummer, *JAP* 1988 — the chemistry of interface-trap
  annealing.[^reed-1988]
* Brower, *Phys. Rev. B* 1990 — dissociation kinetics of passivated
  interface defects.[^brower-1990]
* Cartier, Stathis and Buchanan, *APL* 1993 — passivation and
  depassivation by atomic hydrogen.[^cartier-1993]
* Stesmans, *APL* 1996 — P_b0 and P_b1 passivation by molecular
  hydrogen.[^stesmans-1996]
* Lyding, Hess and Kizilyalli, *APL* 1996 — deuterium sintering against
  hot-carrier degradation.[^lyding-1996]
* Kizilyalli et al., *IEEE EDL* 1998 — deuterium anneals in multilevel
  metal manufacturing.[^kizilyalli-1998]
* Sah, Sun and Tzou, *APL* 1983 — boron deactivation by
  hydrogen.[^sah-1983]
* Pankove et al., *PRL* 1983 — neutralisation of shallow acceptors by
  atomic hydrogen.[^pankove-1983]
* Maes, Usmani and Heyns, *JAP* 1981 — hydrogen anneal and MNOS
  retention.[^maes-1981]
* Rangan, Krishnan and Ashok, P2ID 1998 — hydrogen and deuterium
  passivation of process damage.[^rangan-1998]
* Fang and McVittie, *IEEE EDL* 1992 — thin-oxide damage from plasma
  charging.[^fang-1992]
* Lanford and Rand, *JAP* 1978 — hydrogen in plasma nitride.[^lanford-1978]
* Ohashi, Kubota and Nakajima, *IEEE EDL* 2007 — argon annealing at the
  STI edge.[^ohashi-2007]
* Fujimura et al., *JVST B* 1991 — water vapour against hydrogen as an
  addition to downstream O₂ ashing, and the activation energies of
  each.[^fujimura-1991]
* Xu and Diao, *JVST A* 2008 — tungsten oxidation in O₂/H₂/N₂ downstream
  plasma.[^xu-2008]

## Open questions

* Whether SKY130's alloys use premixed forming gas, hydrogen blended at
  the tool or deuterium, and at what fraction, is not public.[^skw-01]
* What "H2>N2" on the Mattson Aspen entry denotes, and which asher
  strips which SKY130 layer, are not stated.[^skw-01]
* Which of SkyWater's gas suppliers provides hydrogen, nitrogen or
  forming gas is not stated.[^sec-01][^sec-02]
* Whether any SKY130 step anneals in argon, and which steps use the
  furnaces' "Ar anneal" and "N2 anneal" processes, is not
  stated.[^skw-01]

<!-- footnotes -->

[^wiki-fg]: Wikipedia, *Forming gas*.
    <https://en.wikipedia.org/wiki/Forming_gas>
[^semistar-iridia]: SemiStar Corp., *Novellus Gasonics PEP Iridia DL
    Plasma Asher* (used-equipment listing), accessed 2026-09-13.
    <https://www.semistarcorp.com/product/novellus-gasonics-pep-iridia-dl-plasma-asher/>
[^wiki-ash]: Wikipedia, *Plasma ashing*.
    <https://en.wikipedia.org/wiki/Plasma_ashing>
[^reed-1988]: M. L. Reed and J. D. Plummer, "Chemistry of Si-SiO₂
    interface trap annealing", *Journal of Applied Physics* **63**(12),
    5776–5793 (1988). <https://doi.org/10.1063/1.340317>
[^cartier-1993]: E. Cartier, J. H. Stathis and D. A. Buchanan,
    "Passivation and depassivation of silicon dangling bonds at the
    Si/SiO₂ interface by atomic hydrogen", *Applied Physics Letters*
    **63**(11), 1510–1512 (1993). <https://doi.org/10.1063/1.110758>
[^sah-1983]: C.-T. Sah, J. Y.-C. Sun and J. J.-T. Tzou, "Deactivation
    of the boron acceptor in silicon by hydrogen", *Applied Physics
    Letters* **43**(2), 204–206 (1983). <https://doi.org/10.1063/1.94287>
[^ohashi-2007]: T. Ohashi, T. Kubota and A. Nakajima, "Ar Annealing for
    Suppression of Gate Oxide Thinning at Shallow Trench Isolation
    Edge", *IEEE Electron Device Letters* **28**(7), 562–564 (2007).
    <https://doi.org/10.1109/LED.2007.899328>
[^wiki-flammability]: Wikipedia, *Flammability limit* (table of limits
    in air, hydrogen row).
    <https://en.wikipedia.org/wiki/Flammability_limit>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; furnace, RTA and resist-removal entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing" and "Environmental, Safety and Quality
    Matters"; read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^razouk-1979]: R. R. Razouk and B. E. Deal, "Dependence of Interface
    State Density on Silicon Thermal Oxidation Process Variables",
    *Journal of The Electrochemical Society* **126**(9), 1573–1581
    (1979). <https://doi.org/10.1149/1.2129333>
[^deal-1980]: B. E. Deal, "Standardized terminology for oxide charges
    associated with thermally oxidized silicon", *IEEE Transactions on
    Electron Devices* **27**(3), 606–608 (1980).
    <https://doi.org/10.1109/T-ED.1980.19908>
[^brower-1990]: K. L. Brower, "Dissociation kinetics of
    hydrogen-passivated (111) Si-SiO₂ interface defects", *Physical
    Review B* **42**(6), 3444–3453 (1990).
    <https://doi.org/10.1103/PhysRevB.42.3444>
[^stesmans-1996]: A. Stesmans, "Passivation of P_b0 and P_b1 interface
    defects in thermal (100) Si/SiO₂ with molecular hydrogen", *Applied
    Physics Letters* **68**(15), 2076–2078 (1996).
    <https://doi.org/10.1063/1.116308>
[^rangan-1998]: S. Rangan, S. Krishnan and S. Ashok, "Process-induced
    damage — a study of hydrogen and deuterium passivation", *Proc.
    1998 3rd International Symposium on Plasma Process-Induced Damage*,
    pp. 213–216. <https://doi.org/10.1109/PPID.1998.725612>
[^fang-1992]: S. Fang and J. P. McVittie, "Thin-oxide damage from gate
    charging during plasma processing", *IEEE Electron Device Letters*
    **13**(5), 288–290 (1992). <https://doi.org/10.1109/55.145056>
[^lyding-1996]: J. W. Lyding, K. Hess and I. C. Kizilyalli, "Reduction of
    hot electron degradation in metal oxide semiconductor transistors by
    deuterium processing", *Applied Physics Letters* **68**(18),
    2526–2528 (1996). <https://doi.org/10.1063/1.116172>
[^kizilyalli-1998]: I. C. Kizilyalli, G. C. Abeln, Z. Chen, J. Lee,
    G. Weber, B. Kotzias, S. Chetlur, J. W. Lyding and K. Hess,
    "Improvement of hot carrier reliability with deuterium anneals for
    manufacturing multilevel metal/dielectric MOS systems", *IEEE
    Electron Device Letters* **19**(11), 444–446 (1998).
    <https://doi.org/10.1109/55.728907>
[^pat-deuterium-uiuc]: J. W. Lyding and K. Hess (Board of Trustees of the
    University of Illinois), *Deuterium-treated semiconductor devices*,
    US 5,872,387 A, filed 1996-01-16, granted 1999-02-16.
    <https://patents.google.com/patent/US5872387A/en>
[^pankove-1983]: J. I. Pankove, D. E. Carlson, J. E. Berkeyheiser and
    R. O. Wance, "Neutralization of Shallow Acceptor Levels in Silicon
    by Atomic Hydrogen", *Physical Review Letters* **51**(24),
    2224–2225 (1983). <https://doi.org/10.1103/PhysRevLett.51.2224>
[^maes-1981]: H. E. Maes, S. H. Usmani and G. L. Heyns, "Effects of a
    high-temperature hydrogen anneal on the memory retention of
    metal-nitride-oxide-silicon transistors at elevated temperatures",
    *Journal of Applied Physics* **52**(6), 4348–4350 (1981).
    <https://doi.org/10.1063/1.329266>
[^lanford-1978]: W. A. Lanford and M. J. Rand, "The hydrogen content of
    plasma-deposited silicon nitride", *Journal of Applied Physics*
    **49**(4), 2473–2477 (1978). <https://doi.org/10.1063/1.325095>
[^fujimura-1991]: S. Fujimura, K. Shinagawa, M. T. Suzuki and
    M. Nakamura, "Resist stripping in an O₂+H₂O plasma downstream",
    *Journal of Vacuum Science & Technology B* **9**(2), 357–361 (1991).
    <https://doi.org/10.1116/1.585575>
[^xu-2008]: S. Xu and L. Diao, "Study of tungsten oxidation in O₂/H₂/N₂
    downstream plasma", *Journal of Vacuum Science & Technology A*
    **26**(3), 360–364 (2008). <https://doi.org/10.1116/1.2897316>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco AVP
    8000* listing, accessed 2026-08-30.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^asm-vf]: ASM International, *Vertical furnace*, product page.
    <https://www.asm.com/our-technology-products/vertical-furnace>
[^mattson-2001]: Mattson Technology, *The Aspen Strip*, product page;
    Wayback Machine capture of 2001-12-19.
    <https://web.archive.org/web/20011219013713/http://www.mattson.com/products/aspen_strip.html>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
