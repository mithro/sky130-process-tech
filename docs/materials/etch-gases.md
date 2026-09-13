(material-etch-gases)=
# Etch and chamber-clean gases

Etch and chamber-clean gases are the halogen-bearing gases that a plasma
breaks into reactive fragments: fluorocarbons and fluorides (CF₄, CHF₃,
C₂F₆, C₄F₈, SF₆, NF₃) for oxide, nitride, silicon and refractory films
and for cleaning deposition chambers; chlorine and boron trichloride for
aluminium and titanium films; hydrogen bromide for silicon; and small
additions of hydrofluorocarbons, carbon monoxide or methane that tune
selectivity and sidewall passivation. Many are toxic or corrosive, and
the fluorinated ones include some of the most potent greenhouse gases in
industrial use, so their emissions are regulated and abated. This page
describes the class in general, lists representative gases and their
standards, and then says what SkyWater has published about etch gases at
its fab and which SKY130 steps name them. The etch mechanisms are on the
{ref}`etch category page <category-etch>`, and the tools on the
{ref}`silicon <machine-plasma-etcher-silicon>`,
{ref}`dielectric <machine-plasma-etcher-dielectric>` and
{ref}`metal <machine-plasma-etcher-metal>` etcher pages.

| | Etch and chamber-clean gases |
|---|---|
| What they do | Supply halogen atoms and ions that form volatile products with the film; ion bombardment and reactive gas together etch far faster than either alone.[^coburn-1979] |
| Gases in the SKY130 steps | CF₄, CHF₃, C₂F₆, C₄F₈, CH₃F, CH₂F₂, CO, CH₄, SF₆, NF₃, HBr, Cl₂, BCl₃ (step-page readings). |
| Grades | SEMI C3.40 (carbon tetrafluoride) and C3.24 (sulphur hexafluoride).[^semi-c3-40][^semi-c3-24] |
| Climate | CF₄ "persists in the atmosphere for 50,000 years";[^wiki-cf4] NF₃ has "a global warming potential (GWP) 17,200 times greater than that of CO2";[^wiki-nf3] SF₆ "is the most potent greenhouse gas".[^wiki-sf6] |
| Hazards | NIOSH IDLH "10 ppm" for chlorine, "30 ppm" for hydrogen bromide and "1000 ppm" for nitrogen trifluoride.[^niosh-cl2][^niosh-hbr][^niosh-nf3] |
| SkyWater evidence | "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2"; "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6, O2"; "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2"; CF4 on two ashers;[^skw-01] fluorinated-gas emissions reported to the EPA for the Bloomington fab[^epa-ghgrp-skywater] |
| SKY130 steps | 64 steps; see {ref}`SKY130 steps that use this class <material-etch-gases-steps>` |

## What the class is and what it does

A plasma etch works by making, from a stable feed gas, species that react
with the film to give a volatile product, and by driving the reaction
with ions from the plasma. Coburn and Winters showed how strongly energetic
radiation enhances such gas–surface reactions, examining "the reactions of
Si, SiO2, and Si3N4 with XeF2, F2, and Cl2";[^coburn-1979] their later
review covers the surface science of etching.[^winters-1992] Fluorine
gives volatile SiF₄ from silicon, oxide and nitride, and WF₆ from
tungsten; chlorine and bromine give volatile aluminium and titanium
chlorides and a slower, more controllable silicon etch; carbon in the
feed gas builds a fluorocarbon film that protects sidewalls and the
layer beneath ({ref}`category-etch`). Flamm reviewed the mechanisms of
silicon etching in fluorine- and chlorine-containing plasmas.[^flamm-1990]
The same fluorine chemistry removes film from the walls of deposition
chambers, which is why NF₃ and perfluorocarbons are also cleaning gases.

### Fluorocarbons for oxide and nitride: CF₄, CHF₃, C₂F₆ and C₄F₈

Carbon tetrafluoride "is used in electronics microfabrication alone or
in combination with oxygen as a plasma etchant for silicon, silicon
dioxide, and silicon nitride".[^wiki-cf4] Adding hydrogen or more carbon
shifts the balance from etching to deposition: "CHF3 is used in the
semiconductor industry in plasma etching of silicon oxide and silicon
nitride",[^wiki-chf3] hexafluoroethane "is used as a versatile etchant in
semiconductor manufacturing",[^wiki-c2f6] and octafluorocyclobutane
"serves mainly as a passivation layer material in etching
processes".[^wiki-c4f8] Oehrlein et al. found fluorocarbon film deposition
"plays a key role in determining the profile shape of contact holes and
the etch selectivity with respect to the mask and the
underlayer";[^oehrlein-1994] Schaepkens et al. found that "the substrate
etch rate is inversely proportional to the thickness of this fluorocarbon
film", the basis of oxide-to-nitride selectivity.[^schaepkens-1999]
Perry et al. measured CF and CF₂ densities in a high-density C₂F₆ plasma
and a "Transition from net etch to net deposition of fluorocarbon" near
30 W of bias.[^perry-2001]

### Hydrofluorocarbon and other additives

Small flows of other gases tune a fluorocarbon etch. Fluoromethane "is
used in semiconductor manufacturing processes as an etching gas in plasma
etch reactors";[^wiki-ch3f] Regis et al. developed a nitride spacer etch
"with high selectivity to oxide".[^regis-1997] Carbon monoxide and oxygen
adjust the fluorine-to-carbon balance of contact etches (industry
practice; {ref}`CTME <step-108>`). In aluminium etching, carbon-bearing
additions passivate sidewalls: Selamoglu et al. found that in
CHF₃/Cl₂/BCl₃ "The process involves sidewall polymer deposition during
etching" and that the taper "increased with increasing CHF3 flow
rates".[^selamoglu-1991]

### Sulphur hexafluoride and nitrogen trifluoride

SF₆ is a fluorine-rich etchant without carbon: its uses include "a
silicon etchant for semiconductor manufacturing", and in the plasma it
"breaks down in the plasma into sulfur and fluorine, with the fluorine
ions performing a chemical reaction with silicon".[^wiki-sf6] NF₃ is
"primarily used to remove silicon and silicon-compounds during the
manufacturing of semiconductor devices", and "is also widely used to
clean PECVD chambers".[^wiki-nf3] Kastenmeier et al. characterised remote
NF₃/O₂ plasma etching of nitride and oxide,[^kastenmeier-1998] and their
earlier work used CF₄/O₂/N₂ for chemical dry etching.[^kastenmeier-1996]
Sobolewski, Langan and Felker compared NF₃/Ar, CF₄/O₂/Ar and C₂F₆/O₂/Ar
chamber-cleaning plasmas.[^sobolewski-1998] Where older tools cleaned with
C₂F₆, Chan, Loh and Allgood replaced it with c-C₄F₈ on a Novellus Concept
One, and "Both processes significantly lowered gas consumption and PFC
emissions".[^chan-2004]

### Chlorine, boron trichloride and hydrogen bromide

Aluminium, titanium and TiN are etched with chlorine: Chen, DeOrnellas and
Burke studied aluminium alloys in BCl₃/Cl₂ plasmas,[^chen-1989] and "BCl3
is also used in plasma etching in semiconductor manufacturing. This gas
etches metal oxides by formation of a volatile BOClx and MxOyClz
compounds",[^wiki-bcl3] the native alumina that must be broken through
before the metal etches (our reading). Allen and Rickard added nitrogen
for a tapered aluminium etch.[^allen-1994] Chlorine-etched Al–Cu corrodes
if it meets air unprotected.[^lee-1981-corrosion] Silicon gates and
trenches are etched in HBr/Cl₂/O₂, whose bromine and oxygen form
sidewall films and give selectivity to the gate oxide
({ref}`category-etch`); Bell and Joubert analysed gates "etched in
HBr/Cl2/O2 plasmas",[^bell-1997] and Tuda et al. followed profile evolution
in "low-pressure high-density Cl2/HBr/O2 plasma chemistries".[^tuda-2001]
Hydrogen bromide "is highly corrosive and, if inhaled, can cause lung
damage".[^wiki-hbr]

## Representative materials and grades

Etch gases are sold in cylinders by specialty-gas suppliers (industry
practice); a supplier offers fluorine generated on site in place of
NF₃ for chamber cleaning.[^linde-eng-electronics]
The statements below describe standards and supplier catalogues, not what
SkyWater buys, even where the supplier is named in SkyWater's filings;
SKY130's etch recipes are not public.

* **Carbon tetrafluoride.** SEMI C3.40 provides a "specification for
  carbon tetrafluoride (CF4) that is used in the semiconductor
  industry".[^semi-c3-40]
* **Sulphur hexafluoride.** SEMI C3.24 provides "specifications for
  sulfur hexafluoride (SF6) that is used in the semiconductor
  industry";[^semi-c3-24] the gas is "colorless, odorless,
  non-flammable, and non-toxic".[^wiki-sf6]
* **Nitrogen trifluoride.** "a colorless, non-flammable, toxic gas with a
  slightly musty odor";[^wiki-nf3] NIOSH notes it is "Shipped as a
  nonliquefied compressed gas".[^niosh-nf3] Linde Engineering offers
  on-site fluorine generators that replace "nitrogen trifluoride (NF3),
  chlorine trifluoride (ClF3), sulfur hexafluoride (SF6) and F2/N2
  mixtures" in chamber cleaning.[^linde-eng-electronics]
* **Hydrofluorocarbons and perfluorocarbons.** CHF₃, CH₃F ("non-toxic,
  liquefiable, and flammable"[^wiki-ch3f]), C₂F₆ and c-C₄F₈, the last
  also investigated "as a possible replacement for sulfur hexafluoride as
  a dielectric gas".[^wiki-c4f8]
* **Chlorine and boron trichloride.** Chlorine is a "Greenish-yellow gas
  with a pungent, irritating odor", "Shipped as a liquefied compressed
  gas";[^niosh-cl2] Wikipedia's article on boron trichloride links it to its list of
  highly toxic gases.[^wiki-bcl3]
* **Hydrogen bromide.** "Colorless gas with a sharp, irritating odor",
  "Shipped as a liquefied compressed gas".[^niosh-hbr]

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page names gases on its
poly/silicon etchers and ashers but not on its metal etchers. Under
"Etch":[^skw-01]

> "Metal Etch" · "Lam 9600, Al, TiW, TiN, Pt" · "Lam 2300 Versys, Al,
> TiW, TiN, Nb, Pt"
>
> "Poly/Silicon Etch" · "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2" ·
> "– gate, trench, W/WN" · "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6,
> O2" · "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2"

and under "Resist removal/cleans", "Iridia RF microwave, N2, O2, H2, CF4,
NH3, H2/N2, 40C-270C" and "Mattson Aspen2, RF plasma, O2, CF4, H2>N2, up
to 250C".[^skw-01] Read term by term, the page names HBr, Cl₂, NF₃, CF₄,
CHF₃, SF₆ and C₂F₆; it names no BCl₃, C₄F₈, CH₃F, CH₂F₂, CO or CH₄, no
gases for the metal etchers, and no dedicated oxide etcher. The filings
name gas suppliers, as quoted on the
{ref}`process gases <material-process-gases>` page, without naming any
etch gas.[^sec-01][^sec-02] SkyWater's annual report for fiscal 2023 adds
that its operations are subject to requirements on "air quality and
emissions" and on "per- and polyfluoroalkyl substances (commonly known as
PFAS or “forever chemicals”)", and that stakeholders focus on
"greenhouse gas emissions".[^sec-02]

The EPA's Greenhouse Gas Reporting Program lists "SKYWATER TECHNOLOGY
INC" in Bloomington, Minnesota, reporting under subpart I, electronics
manufacturing, in each year from 2011 to 2023.[^epa-ghgrp-skywater] The
subpart covers plasma etching and chamber cleaning "using
plasma-generated F2 atoms and other reactive F2-containing fragments", N₂O
use and fluorinated heat-transfer fluids.[^epa-ghgrp-subpart-i] For 2023
the public tables give the facility's subpart I emissions as CO₂-equivalent
values of about 47,100 for perfluorocarbons, 6,110 for
hydrofluorocarbons, 2,300 for SF₆, 2,140 for other fully fluorinated
gases and 1,440 for NF₃, against about 101,800 for perfluorocarbons in
2011;[^epa-ghgrp-skywater] the programme expresses emissions in metric
tons of CO₂ equivalent.[^epa-ghgrp-fgas] The tables do not give the
individual gases, processes or tools, and heat-transfer fluids may
account for some of the fully fluorinated total (our reading).

### Strength of the evidence

The etcher and asher entries are SkyWater statements and rank as
**strong** evidence, on the scale of the
{ref}`machines index <machines-reading-evidence>`, that HBr, Cl₂, NF₃,
CF₄, CHF₃, SF₆ and C₂F₆ are used at the fab; they describe the whole fab
in the 2020s and tie no gas to a step, and they come from silicon and
poly etchers, not from the tools the step pages assign to the contact,
via and metal etches.[^skw-01] The EPA record is a regulatory filing and
is strong evidence that perfluorocarbons, hydrofluorocarbons, SF₆ and NF₃
are emitted by the Bloomington facility's etching, cleaning or other
subpart I processes, weak for any SKY130 step.[^epa-ghgrp-skywater] BCl₃,
C₄F₈, CH₃F, CH₂F₂, CO and CH₄, and every gas on the metal and dielectric
etches, are industry practice that the step pages supply.

(material-etch-gases-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells). The oxygen,
argon, nitrogen and helium used with these gases belong to the
{ref}`process gases <material-process-gases>` page.

Materials index rows covered:

* `cf4` — carbon tetrafluoride
* `chf3` — trifluoromethane
* `c2f6` — hexafluoroethane
* `etch-additives` — C₄F₈, CO, CH₃F, CH₂F₂ and CH₄
* `sf6` — sulphur hexafluoride
* `nf3` — nitrogen trifluoride
* `hbr` — hydrogen bromide
* `cl2` — chlorine
* `bcl3` — boron trichloride

Steps:

{ref}`ISONIT <step-003>`, {ref}`STINITE <step-005>`, {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`FILOX <step-011>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNARCE <step-036>`, {ref}`ONOME <step-042>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPNIT <step-076>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`SPOX <step-080>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`PSG <step-089>`, {ref}`NCAPOX <step-091>`, {ref}`LICM1E <step-094>`, {ref}`WDEP <step-099>`, {ref}`LI1ME <step-103>`, {ref}`LINIT <step-104>`, {ref}`NILD2 <step-105>`, {ref}`CTME <step-108>`, {ref}`WDEP2 <step-110>`, {ref}`MM1E <step-114>`, {ref}`NILD3 <step-115>`, {ref}`NCAPOX3 <step-117>`, {ref}`VIME <step-119>`, {ref}`WDEP3 <step-121>`, {ref}`MM2E <step-125>`, {ref}`NILD4 <step-126>`, {ref}`NCAPOX4 <step-128>`, {ref}`VIM2E <step-130>`, {ref}`WDEP4 <step-132>`, {ref}`CAPILD <step-135>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`NILD5 <step-141>`, {ref}`NCAPOX5 <step-143>`, {ref}`VIM3E <step-145>`, {ref}`WDEP5 <step-147>`, {ref}`CAPILD2 <step-150>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`NILD6 <step-156>`, {ref}`NCAPOX6 <step-158>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NFUSOX <step-164>`, {ref}`NSME <step-166>`, {ref}`NTSD <step-167>`, {ref}`PDME <step-169>`

The steps fall into groups, as the index rows describe them:

* **Front-end etches.** HBr, Cl₂ and O₂ with CF₄ breakthrough for the
  trench and gate ({ref}`STIE <step-006>`, {ref}`P1ME <step-062>`);
  CF₄, CHF₃ and SF₆ for the nitride, ONO and spacer etches
  ({ref}`STINITE <step-005>`, {ref}`ONOME <step-042>`,
  {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`), with CH₃F or CH₂F₂ as
  a possible selectivity additive at {ref}`SPE <step-077>`; HBr at the
  ARC etch {ref}`TUNARCE <step-036>`.
* **Contact, via and seal-ring etches.** C₄F₈, C₂F₆, CHF₃ and CF₄, with
  CO as a possible additive ({ref}`LICM1E <step-094>`,
  {ref}`CTME <step-108>`, {ref}`VIME <step-119>` to
  {ref}`VIM4E <step-160>`, {ref}`NSME <step-166>`).
* **Metal and capacitor etches.** Cl₂ and BCl₃, with CF₄, CHF₃ or SF₆
  for the cap breakthrough and CH₄ as a possible passivating additive at
  {ref}`MM1E <step-114>` and {ref}`MM2E <step-125>`; the capacitor plate
  etches {ref}`CAPME <step-138>` and {ref}`CAP2ME <step-153>` name HBr and
  CH₂F₂ among their options; the pad etch {ref}`PDME <step-169>` uses
  CF₄, CHF₃ and SF₆.
* **Chamber cleans.** NF₃ at the HDP, PECVD and tungsten CVD steps and at
  several etches, and as a tube-clean option at
  {ref}`ISONIT <step-003>`.
* **CF₄ named and left out.** The implant-strip pages, from
  {ref}`DNIS <step-009>` to {ref}`NSDIS <step-087>`, name CF₄ because
  SkyWater lists it on the Iridia and Mattson ashers, and then infer that
  it would be omitted because it attacks the exposed oxide or silicon;
  the {ref}`materials index <materials-open-questions>` records this.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's etch-gas
delivery, exhaust or abatement; the points below are industry practice,
safety data and regulatory context.

* **Toxic and corrosive gases.** NIOSH lists chlorine with an IDLH of
  "10 ppm" and a REL of "C 0.5 ppm (1.45 mg/m3)
  [15-minute]";[^niosh-cl2] hydrogen bromide with an IDLH of "30 ppm" and
  a REL of "C 3 ppm (10 mg/m3)";[^niosh-hbr] and nitrogen trifluoride
  with an IDLH of "1000 ppm" and a REL of "TWA 10 ppm (29
  mg/m3)".[^niosh-nf3] Chlorine "Reacts explosively or forms explosive
  compounds with many common substances such as acetylene, ether,
  turpentine, ammonia, fuel gas, hydrogen & finely divided
  metals".[^niosh-cl2] These gases are kept in exhausted gas cabinets
  with leak detection (industry practice).
* **Greenhouse gases.** Lifetimes and warming potentials are long and
  large: CF₄ "has an atmospheric lifetime of 50,000 years";[^wiki-cf4]
  Wikipedia's extract of the IPCC fifth assessment gives 100-year GWPs of
  6630 for CF₄, 11,100 for C₂F₆ and 9540 for c-C₄F₈;[^wiki-pfc] CHF₃'s is
  given as "14,800 for HFC-23",[^wiki-chf3] NF₃'s as 17,200[^wiki-nf3]
  and SF₆'s as "23,500 times greater" than CO₂'s.[^wiki-sf6] The
  figures differ between assessments.
* **Reporting and abatement.** Electronics facilities above the
  programme's threshold report fluorinated-gas emissions by process type
  and "Controlled emissions of GHGs from abatement systems, if
  applicable";[^epa-ghgrp-subpart-i] Ridgeway described real-time
  measurement "for quantifying unused process gases, characterizing and
  quantifying process by-products, and determining the effectiveness of
  abatement equipment".[^ridgeway-1995]
* **Utilisation.** Chamber-clean gases are only partly consumed; "The
  utilization efficiency of the chemicals applied in plasma processes
  varies widely between equipment and applications",[^wiki-nf3] which is
  why remote-plasma cleans and clean-gas substitutions reduce
  emissions.[^chan-2004][^amat-producer-se-2001]
* **By-products.** Chlorine etches of aluminium exhaust chlorides and
  leave chlorine on the wafer, the cause of post-etch
  corrosion;[^lee-1981-corrosion] fluorine cleans and etches exhaust HF
  and SiF₄ (industry practice; {ref}`machine-tungsten-cvd`).

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's etch gases, flows and endpoints are not
public.

* **Named gases on unnamed tools.** SkyWater's gas lists belong to the
  DPS II, 9400 and 4400 poly/silicon etchers;[^skw-01] the contact, via
  and seal-ring pages assign their oxide etches to a dielectric-etcher
  class that SkyWater does not list and so borrow C₂F₆, CF₄ and CHF₃ from
  those entries as evidence that the gases exist at the fab, not that
  those tools run the steps ({ref}`machine-plasma-etcher-dielectric`).
* **Metal-etch gases without a SkyWater source.** The metal etch pages
  read Cl₂ and BCl₃ as industry practice, because SkyWater lists its
  metal etchers only as "Lam 9600, Al, TiW, TiN, Pt" and "Lam 2300
  Versys, Al, TiW, TiN, Nb, Pt";[^skw-01] BCl₃ appears in no SkyWater
  source cited here.
* **Breakthroughs and caps.** The TiW cap of the metal stacks and the TiW
  capacitor plates need fluorine as well as chlorine; Liu and Kuo etched
  TiW in CF₄-based mixtures,[^liu-2007-tiw] and a Texas Instruments
  patent describes selective etching of MiM top
  electrodes.[^pat-mim-ti-etch] The materials index records that the cap
  breakthrough gases differ between analogous metal-etch pages
  ({ref}`materials-open-questions`).
* **Nitride over oxide.** The spacer and nitride-cut etches need nitride
  removed without the oxide beneath; the SPE page names CH₃F or CH₂F₂ as
  a possible additive, as in Regis et al.'s spacer etch,[^regis-1997] and
  the fluorocarbon-film mechanism of Schaepkens et al. explains the
  selectivity.[^schaepkens-1999]
* **Cleaning after every deposition.** On the step pages' readings every
  HDP, PECVD and tungsten CVD step names an NF₃ clean of its chamber, which makes NF₃ the etch-class gas named on the most
  deposition steps; SkyWater lists NF₃ only on the DPS II
  etcher.[^skw-01]
* **Emissions over time.** The Bloomington facility's reported
  perfluorocarbon emissions fell from about 101,800 to about 47,100
  CO₂-equivalent units between 2011 and 2023, while its NF₃ figure stayed
  of the order of 1,000–3,500;[^epa-ghgrp-skywater] the public tables do
  not say whether production, process changes or abatement caused this.

## Related pages

* {ref}`category-etch` — plasma etch mechanisms and the etch steps.
* {ref}`machine-plasma-etcher-silicon`,
  {ref}`machine-plasma-etcher-dielectric` and
  {ref}`machine-plasma-etcher-metal` — the etchers that consume these
  gases.
* {ref}`machine-pecvd`, {ref}`machine-hdp-cvd` and
  {ref}`machine-tungsten-cvd` — the deposition tools cleaned with NF₃.
* {ref}`machine-downstream-plasma-asher` — CF₄ on the ashers.
* {ref}`material-process-gases` — oxygen, argon, nitrogen and helium used
  with the etch gases.
* {ref}`material-precursors` — the deposition gases whose chamber films
  the clean gases remove.
* {ref}`materials-index` — all consumable classes, including abatement.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the etcher and asher
  entries.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  gas suppliers and environmental requirements.[^sec-01][^sec-02]
* U.S. EPA, Greenhouse Gas Reporting Program data for SkyWater's
  Bloomington facility, the subpart I information sheet and *Fluorinated
  Greenhouse Gas Emissions and Supplies Reported to the GHGRP* —
  fluorinated-gas reporting at the fab and what it
  covers.[^epa-ghgrp-skywater][^epa-ghgrp-subpart-i][^epa-ghgrp-fgas]
* SEMI C3.40 and C3.24 — specifications for CF₄ and
  SF₆.[^semi-c3-40][^semi-c3-24]
* NIOSH, *Pocket Guide to Chemical Hazards* — chlorine, hydrogen bromide
  and nitrogen trifluoride.[^niosh-cl2][^niosh-hbr][^niosh-nf3]
* Linde Engineering, *Serving the Electronics Industry* — on-site
  fluorine as a chamber-clean gas.[^linde-eng-electronics]
* Applied Materials, *Producer SE* (Wayback capture of 2001) — a
  low-flow remote clean.[^amat-producer-se-2001]

### High-level understanding

* Wikipedia, *Carbon tetrafluoride*, *Fluoroform*, *Hexafluoroethane*
  and *Octafluorocyclobutane* — fluorocarbon etch
  gases.[^wiki-cf4][^wiki-chf3][^wiki-c2f6][^wiki-c4f8]
* Wikipedia, *Fluoromethane* and *Perfluorocarbon* — an additive and the
  greenhouse properties of PFCs.[^wiki-ch3f][^wiki-pfc]
* Wikipedia, *Sulfur hexafluoride* and *Nitrogen trifluoride* — the
  carbon-free fluorides.[^wiki-sf6][^wiki-nf3]
* Wikipedia, *Hydrogen bromide* and *Boron trichloride* — bromine and
  chlorine etch gases.[^wiki-hbr][^wiki-bcl3]
* Donnelly and Kornblit, *JVST A* 2013 — plasma etching from its origins
  to the present.[^donnelly-2013]
* Nojiri, *Dry Etching Technology for Semiconductors* — production etch
  chemistries.[^nojiri-2015]

### Deep dive

* Coburn and Winters, *JAP* 1979 — ion-assisted gas–surface
  chemistry.[^coburn-1979]
* Winters and Coburn, *Surface Science Reports* 1992 — surface science of
  etching reactions.[^winters-1992]
* Flamm, *Pure Appl. Chem.* 1990 — silicon etching in fluorine and
  chlorine plasmas.[^flamm-1990]
* Oehrlein et al., *JVST A* 1994 — fluorocarbon film deposition with CF₄
  and CHF₃.[^oehrlein-1994]
* Schaepkens et al., *JVST A* 1999 — the oxide-to-nitride selectivity
  mechanism.[^schaepkens-1999]
* Perry et al., *JVST A* 2001 — C₂F₆ oxide etching in a high-density
  plasma.[^perry-2001]
* Regis et al., ASMC 1997 — a selective nitride spacer
  etch.[^regis-1997]
* Kastenmeier et al., *JVST A* 1996 and 1998 — CF₄/O₂/N₂ and NF₃/O₂
  remote etching of nitride and oxide.[^kastenmeier-1996][^kastenmeier-1998]
* Sobolewski, Langan and Felker, *JVST B* 1998 — chamber-cleaning
  plasmas.[^sobolewski-1998]
* Chan, Loh and Allgood, *IEEE TSM* 2004 — a C₄F₈ chamber clean with
  lower PFC emissions.[^chan-2004]
* Ridgeway, ASMC 1995 — measuring emissions and abatement
  effectiveness.[^ridgeway-1995]
* Bell and Joubert, *JVST B* 1997, and Tuda et al., *JVST A* 2001 —
  HBr/Cl₂/O₂ gate etching.[^bell-1997][^tuda-2001]
* Chen, DeOrnellas and Burke, ASTM STP 990 — aluminium alloys in
  BCl₃/Cl₂.[^chen-1989]
* Selamoglu et al., *JVST B* 1991 — tapered aluminium etching with
  CHF₃/Cl₂/BCl₃.[^selamoglu-1991]
* Allen and Rickard, *JVST A* 1994 — a tapered aluminium etch with
  nitrogen.[^allen-1994]
* Lee, Eldridge and Schwartz, *JAP* 1981 — corrosion after chlorine
  etching.[^lee-1981-corrosion]
* Liu and Kuo, *JES* 2007 — reactive ion etching of TiW.[^liu-2007-tiw]

## Open questions

* Which etch gases SkyWater's metal etchers and any dielectric etcher use
  is not stated; BCl₃ appears in no SkyWater source cited here.[^skw-01]
* Which suppliers and grades serve the etch gases is not
  stated.[^sec-01][^sec-02]
* Which gases make up the perfluorocarbon, hydrofluorocarbon and fully
  fluorinated totals the Bloomington facility reports, and how much is
  abated, are not in the public tables cited here.[^epa-ghgrp-skywater]
* Whether SkyWater's chamber cleans use NF₃ in remote plasma sources,
  C₂F₆ or on-site fluorine is not stated.[^skw-01]

<!-- footnotes -->

[^coburn-1979]: J. W. Coburn and H. F. Winters, "Ion- and
    electron-assisted gas-surface chemistry — An important effect in
    plasma etching", *Journal of Applied Physics* **50**(5), 3189–3196
    (1979). <https://doi.org/10.1063/1.326355>
[^semi-c3-40]: SEMI, *SEMI C3.40 — Specification for Carbon
    Tetrafluoride (CF4), 99.997% Quality*, SEMI Standards store listing
    (revision C3.40-1011 (Reapproved 0218)), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00340-semi-c3-40-specification-for-carbon-tetrafluoride-cf4-99-997-quality>
[^semi-c3-24]: SEMI, *SEMI C3.24 — Specification for Sulfur Hexafluoride
    (SF6) in Cylinders, 99.97% Quality*, SEMI Standards store listing
    (revision C3.24-0414 (Reapproved 0319)E), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00324-semi-c3-24-specification-for-sulfur-hexafluoride-sf6-in-cylinders-99-97-quality>
[^wiki-cf4]: Wikipedia, *Carbon tetrafluoride*.
    <https://en.wikipedia.org/wiki/Carbon_tetrafluoride>
[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*.
    <https://en.wikipedia.org/wiki/Nitrogen_trifluoride>
[^wiki-sf6]: Wikipedia, *Sulfur hexafluoride*.
    <https://en.wikipedia.org/wiki/Sulfur_hexafluoride>
[^niosh-cl2]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Chlorine*, CDC; read from the
    Wayback Machine capture of 2025-11-30.
    <https://www.cdc.gov/niosh/npg/npgd0115.html>
    <https://web.archive.org/web/20251130134447/https://www.cdc.gov/niosh/npg/npgd0115.html>
[^niosh-hbr]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Hydrogen bromide*, CDC; read
    from the Wayback Machine capture of 2025-11-30.
    <https://www.cdc.gov/niosh/npg/npgd0331.html>
    <https://web.archive.org/web/20251130093033/https://www.cdc.gov/niosh/npg/npgd0331.html>
[^niosh-nf3]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Nitrogen trifluoride*, CDC;
    read from the Wayback Machine capture of 2025-11-30.
    <https://www.cdc.gov/niosh/npg/npgd0455.html>
    <https://web.archive.org/web/20251130135138/https://www.cdc.gov/niosh/npg/npgd0455.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; etch and resist removal entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^epa-ghgrp-skywater]: U.S. Environmental Protection Agency, Greenhouse
    Gas Reporting Program, Envirofacts tables `PUB_DIM_FACILITY` and
    `PUB_FACTS_SUBP_GHG_EMISSION` for facility ID 1000354 ("SKYWATER
    TECHNOLOGY INC", Bloomington, Minnesota), reporting years 2010–2023,
    retrieved 2026-09-13.
    <https://data.epa.gov/efservice/PUB_DIM_FACILITY/FACILITY_ID/1000354/JSON>
    <https://data.epa.gov/efservice/PUB_FACTS_SUBP_GHG_EMISSION/FACILITY_ID/1000354/SUB_PART_ID/43/JSON>
[^winters-1992]: H. F. Winters and J. W. Coburn, "Surface science
    aspects of etching reactions", *Surface Science Reports*
    **14**(4–6), 162–269 (1992).
    <https://doi.org/10.1016/0167-5729(92)90009-Z>
[^flamm-1990]: D. L. Flamm, "Mechanisms of silicon etching in fluorine-
    and chlorine-containing plasmas", *Pure and Applied Chemistry*
    **62**(9), 1709–1720 (1990). <https://doi.org/10.1351/pac199062091709>
[^wiki-chf3]: Wikipedia, *Fluoroform*.
    <https://en.wikipedia.org/wiki/Fluoroform>
[^wiki-c2f6]: Wikipedia, *Hexafluoroethane*.
    <https://en.wikipedia.org/wiki/Hexafluoroethane>
[^wiki-c4f8]: Wikipedia, *Octafluorocyclobutane*.
    <https://en.wikipedia.org/wiki/Octafluorocyclobutane>
[^oehrlein-1994]: G. S. Oehrlein, Y. Zhang, D. Vender and M. Haverlag,
    "Fluorocarbon high-density plasmas. I. Fluorocarbon film deposition
    and etching using CF₄ and CHF₃", *Journal of Vacuum Science &
    Technology A* **12**(2), 323–332 (1994).
    <https://doi.org/10.1116/1.578876>
[^schaepkens-1999]: M. Schaepkens, T. E. F. M. Standaert, N. R. Rueger,
    P. G. M. Sebel, G. S. Oehrlein and J. M. Cook, "Study of the
    SiO₂-to-Si₃N₄ etch selectivity mechanism in inductively coupled
    fluorocarbon plasmas and a comparison with the SiO₂-to-Si
    mechanism", *Journal of Vacuum Science & Technology A* **17**(1),
    26–37 (1999). <https://doi.org/10.1116/1.582108>
[^perry-2001]: W. L. Perry, K. Waters, M. Barela and H. M. Anderson,
    "Oxide etch behavior in a high-density, low-pressure, inductively
    coupled C₂F₆ plasma: Etch rates, selectivity to photoresist, plasma
    parameters, and CFx radical densities", *Journal of Vacuum Science &
    Technology A* **19**(5), 2272–2281 (2001).
    <https://doi.org/10.1116/1.1382874>
[^wiki-ch3f]: Wikipedia, *Fluoromethane*.
    <https://en.wikipedia.org/wiki/Fluoromethane>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^selamoglu-1991]: N. Selamoglu, C. N. Bredbenner, T. A. Giniecki and
    H. J. Stocker, "Tapered etching of aluminum with CHF₃/Cl₂/BCl₃ and its
    impact on step coverage of plasma-deposited silicon oxide from
    tetraethoxysilane", *Journal of Vacuum Science & Technology B*
    **9**(5), 2530–2535 (1991). <https://doi.org/10.1116/1.585687>
[^kastenmeier-1998]: B. E. E. Kastenmeier, P. J. Matsuo, G. S. Oehrlein
    and J. G. Langan, "Remote plasma etching of silicon nitride and
    silicon dioxide using NF₃/O₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **16**(4), 2047–2056 (1998).
    <https://doi.org/10.1116/1.581309>
[^kastenmeier-1996]: B. E. E. Kastenmeier, P. J. Matsuo, J. J. Beulens
    and G. S. Oehrlein, "Chemical dry etching of silicon nitride and
    silicon dioxide using CF₄/O₂/N₂ gas mixtures", *Journal of Vacuum
    Science & Technology A* **14**(5), 2802–2813 (1996).
    <https://doi.org/10.1116/1.580203>
[^sobolewski-1998]: M. A. Sobolewski, J. G. Langan and B. S. Felker,
    "Electrical optimization of plasma-enhanced chemical vapor deposition
    chamber cleaning plasmas", *Journal of Vacuum Science & Technology B*
    **16**(1), 173–182 (1998). <https://doi.org/10.1116/1.589774>
[^chan-2004]: E. M. Chan, G. Loh and C. C. Allgood, "Process
    Optimization and PFC Emission Reduction Using a c-C₄F₈ Chamber
    Cleaning Process on a Novellus Concept 1 Dielectric PECVD Tool",
    *IEEE Transactions on Semiconductor Manufacturing* **17**(4),
    497–503 (2004). <https://doi.org/10.1109/TSM.2004.835712>
[^chen-1989]: C.-H. Chen, S. DeOrnellas and B. Burke, "Plasma Etching of
    Aluminum Alloys in BCl₃/Cl₂ Plasmas", in *Semiconductor Fabrication:
    Technology and Metrology*, ASTM STP 990, ASTM International, 1989,
    pp. 202–211. <https://doi.org/10.1520/STP26039S>
[^wiki-bcl3]: Wikipedia, *Boron trichloride*.
    <https://en.wikipedia.org/wiki/Boron_trichloride>
[^allen-1994]: L. R. Allen and R. Rickard, "Tapered aluminum
    interconnect etch", *Journal of Vacuum Science & Technology A*
    **12**(4), 1265–1268 (1994). <https://doi.org/10.1116/1.579306>
[^lee-1981-corrosion]: W.-Y. Lee, J. M. Eldridge and G. C. Schwartz,
    "Reactive ion etching induced corrosion of Al and Al-Cu films",
    *Journal of Applied Physics* **52**(4), 2994–2999 (1981).
    <https://doi.org/10.1063/1.329043>
[^bell-1997]: F. H. Bell and O. Joubert, "Polysilicon gate etching in
    high density plasmas. V. Comparison between quantitative chemical
    analysis of photoresist and oxide masked polysilicon gates etched in
    HBr/Cl₂/O₂ plasmas", *Journal of Vacuum Science & Technology B*
    **15**(1), 88–97 (1997). <https://doi.org/10.1116/1.589259>
[^tuda-2001]: M. Tuda, K. Shintani and H. Ootera, "Profile evolution
    during polysilicon gate etching with low-pressure high-density
    Cl₂/HBr/O₂ plasma chemistries", *Journal of Vacuum Science &
    Technology A* **19**(3), 711–717 (2001).
    <https://doi.org/10.1116/1.1365135>
[^wiki-hbr]: Wikipedia, *Hydrogen bromide*.
    <https://en.wikipedia.org/wiki/Hydrogen_bromide>
[^linde-eng-electronics]: Linde Engineering, *Serving the Electronics
    Industry Worldwide*, industry page, accessed 2026-09-13.
    <https://www.linde-engineering.com/industries/electronics>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing"; read from a Wayback Machine copy on
    2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph and risk factors on
    environmental regulation and ESG matters; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^epa-ghgrp-subpart-i]: U.S. Environmental Protection Agency,
    *Electronics Manufacturing: Subpart I, Greenhouse Gas Reporting
    Program*, information sheet, December 2024, accessed 2026-09-13.
    <https://www.epa.gov/system/files/documents/2024-04/i_electronics_infosheet_2024.pdf>
[^epa-ghgrp-fgas]: U.S. Environmental Protection Agency, *Fluorinated
    Greenhouse Gas Emissions and Supplies Reported to the GHGRP*, web
    page, accessed 2026-09-13.
    <https://www.epa.gov/ghgreporting/fluorinated-greenhouse-gas-emissions-and-supplies-reported-ghgrp>
[^wiki-pfc]: Wikipedia, *Perfluorocarbon*.
    <https://en.wikipedia.org/wiki/Perfluorocarbon>
[^ridgeway-1995]: R. G. Ridgeway, "Determination of emissions and
    evaluation of abatement equipment for selected semiconductor
    processes", *Proceedings of SEMI Advanced Semiconductor Manufacturing
    Conference and Workshop* (1995), p. 89.
    <https://doi.org/10.1109/ASMC.1995.484346>
[^amat-producer-se-2001]: Applied Materials, *Producer SE*, product page;
    Wayback Machine capture of 2001-08-17.
    <https://web.archive.org/web/20010817134045/http://www.appliedmaterials.com:80/products/producer_se.html>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^pat-mim-ti-etch]: M. O. Cathey Jr., P. Mahalingam, W. Tian, D. C.
    Guiling, X. Chen, B. Hu and S. Chevacharoenkul (Texas Instruments),
    *Forming integrated circuit devices with metal-insulator-metal
    capacitors using selective etch of top electrodes*, US 8,110,414 B2,
    filed 2009-04-30, granted 2012-02-07.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8110414>
[^donnelly-2013]: V. M. Donnelly and A. Kornblit, "Plasma etching:
    Yesterday, today, and tomorrow", *Journal of Vacuum Science &
    Technology A* **31**(5), 050825 (2013).
    <https://doi.org/10.1116/1.4819316>
[^nojiri-2015]: K. Nojiri, *Dry Etching Technology for Semiconductors*,
    Springer, 2015. <https://doi.org/10.1007/978-3-319-10295-5>
