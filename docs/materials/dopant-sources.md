(material-dopant-sources)=
# Dopant gases and implant sources

Dopant sources are the materials that supply the boron, phosphorus and
arsenic atoms an ion implanter puts into the wafer: boron trifluoride,
phosphine and arsine gases, solid elements or compounds evaporated in a
vaporiser oven, and the ion-source hardware those species wear out.
Phosphine also
supplies the phosphorus of doped glass. They are among the most
dangerous materials in a fab, which shapes how they are packaged and
delivered. This page
describes the class in general, lists representative sources, packages
and the standards they are specified to, and then says what SkyWater has
published about implant species and sources at its fab and which SKY130
steps name them. The implant physics is on the
{ref}`implant category page <category-implant>`, and the tools on the
{ref}`medium-current <machine-medium-current-implanter>`,
{ref}`high-current <machine-high-current-implanter>` and
{ref}`high-energy <machine-high-energy-implanter>` implanter pages.

| | Dopant gases and implant sources |
|---|---|
| What they do | Feed the ion source, where "a plasma is created between two tungsten electrodes, called reflectors, using a gas often based on fluorine or hydrogen containing the ion to be implanted".[^wiki-implant] |
| Species and sources | BF₃ for B⁺ and BF₂⁺; PH₃ for P⁺; AsH₃ for As⁺; "Gallium, Selenium and Indium are often implanted from solid sources";[^wiki-implant] phosphine or TMPO for doped glass (step-page readings). |
| Delivery | Sub-atmospheric cylinders, in which arsine "can be provided by a sub-atmospheric gas source (a source that supplies less than atmospheric pressure)";[^wiki-ash3] earlier, dilute hydride mixtures "at pressures of 400-1800 psig".[^pat-sds-atmi] |
| Grades | SEMI C3.6 (phosphine), C3.2 (arsine) and C3.27 (boron trifluoride).[^semi-c3-6][^semi-c3-2][^semi-c3-27] |
| Hazards | NIOSH IDLH "Ca [3 ppm]" for arsine, "50 ppm" for phosphine and "25 ppm" for boron trifluoride.[^niosh-arsine][^niosh-phosphine][^niosh-bf3] |
| SkyWater evidence | "Axcelis 8250 Mid current B11, BF2, As"; "Axcelis GSD High current/energy B11, BF2, P, As"; "Axcelis GSD Hi dose B11, BF2, P, As"; "Lam/Novellus High Density Plasma (HDP) doped and phos doped";[^skw-01] "specialty gases" suppliers in both filings[^sec-01][^sec-02] |
| SKY130 steps | 26 steps; see {ref}`SKY130 steps that use this class <material-dopant-sources-steps>` |

## What the class is and what it does

An implanter turns a dopant compound into a beam of ions of one mass. The
compound is fed to an arc chamber, ionised, extracted and passed through
an analysing magnet that selects, say, ¹¹B⁺ or BF₂⁺ from everything the
plasma makes ({ref}`category-implant`). The source material therefore
needs to be volatile, to contain the dopant, and to give a useful current
of the wanted ion. The fluorides and hydrides of the dopants do this
well, and "Arsine gas or phosphine gas can be used in the ion source to
provide arsenic or phosphorus respectively for implantation".[^wiki-implant]
The price is toxicity: "In fabricating wafers, toxic materials such as
arsine and phosphine are often used in the ion implanter
process".[^wiki-implant] The same process wears the source, so ion-source
and beam-line parts are consumed with the gas.

### Boron: boron trifluoride

Boron trifluoride is the usual boron source; Wikipedia lists it as
"applied as dopant in ion implantation" and describes a "pungent,
colourless, and toxic gas" that "forms white fumes in moist air" and "is
corrosive".[^wiki-bf3] From one gas the analysing magnet can select
atomic boron or the molecular ion BF₂⁺, which enters the wafer with less
energy per boron atom; SkyWater's implanter entries list the two species
as "B11" and "BF2".[^skw-01] Boron has two stable isotopes, and a
supplier offers "Isotopically Enriched BF3" in a sub-atmospheric
package;[^emd-ion-x] the entry's "B11" names the mass-11 isotope as the
species, not an enriched feed gas (our reading). Fluorine is hard on the
source: Axcelis advertises "up to 40% reduction in source operating costs
especially with fluorinated species" from its hydrogen generator and
source parts.[^axcelis-gsd-page]

### Phosphorus: phosphine, solid phosphorus and doped glass

"Phosphine is used as a dopant in the semiconductor industry", and "is a
highly toxic respiratory poison, and is immediately dangerous to life or
health at 50 ppm".[^wiki-ph3] It serves the phosphorus implants and,
diluted, is a usual phosphorus source for {term}`HDP-CVD`
phosphosilicate glass (industry practice); Hsiao et al. studied the
thermal behaviour of HDP PSG made from unnamed "phosphorous-related
precursors".[^hsiao-2005] For
atmospheric TEOS–ozone deposition, Fujino et al. used "organic doping
sources, trimethylphosphate for PSG films".[^fujino-1991] Solid phosphorus in a
vaporiser oven is the alternative to the gas ({ref}`category-implant`); the ATMI patent notes
that "Switching from As to P on an implanter with solid sources can take
as long as 90 minutes".[^pat-sds-atmi]

### Arsenic: arsine and solid arsenic

Arsine is described as "flammable, pyrophoric, and highly toxic", and
"arsenic is an n-dopant for silicon and germanium".[^wiki-ash3] NIOSH
treats it as a potential occupational carcinogen, with an IDLH of
"Ca [3 ppm]" and an OSHA limit of "TWA 0.05 ppm".[^niosh-arsine] Arsenic
also deposits in the implanter: Ham et al. found that workers "may be
exposed to higher levels of hazardous materials, such as arsenic, during
preventive maintenance (PM) tasks than during the regular operation", and
that "Arsenic was also found in the bulk samples of debris produced
during PM tasks".[^ham-2017]

### Indium

Indium is a heavy p-type dopant used for steep channel profiles.
Shahidi et al. showed an "Indium channel implant for improved
short-channel behavior of submicrometer NMOSFETs",[^shahidi-1993] and
Momiyama et al. used "a tilted In implantation" for 60 nm nMOSFETs,
citing "its steeper lateral profile" against boron, and reported "no penalties with use of In from device or reliability points
of view".[^momiyama-1999] Indium has no convenient gas and is among the
elements "often implanted from solid sources".[^wiki-implant] A Cypress
embedded-SONOS patent implants a memory-transistor channel "with Indium
(In) at an energy of from about 50 to about 500 kilo-electron volts
(keV)",[^pat-04] and a 2020 Cypress article recommends "deeper channel
implants with heavier species such as Indium".[^cyp-25]

### Sub-atmospheric delivery

Dopant hydrides were once supplied as high-pressure dilute mixtures: the
ATMI patent records that "Many ion implantation systems utilize hydride
gas sources supplied as dilute mixtures (10-15%), in either 0.44 L or 2.3
L cylinders at pressures of 400-1800 psig".[^pat-sds-atmi] Its
alternative adsorbs the gas on a sorbent so that the cylinder stays below
atmospheric pressure; the patent's authors investigated "the safety
aspects related to an accidental incursion of air into a phosphine
storage and delivery system cylinder".[^pat-sds-atmi] "For semiconductor
manufacturing, this method is feasible, as processes such as ion
implantation operate under high vacuum".[^wiki-ash3] A second approach
keeps the gas at pressure behind "an embedded pressure control device
located inside the cylinder":
Olander et al. describe a "Vacuum Actuated Cylinder" for "the metal
fluorides commonly used as dopants", in which "A pre-set sub-atmospheric
pressure must be achieved in the delivery manifold before flow is
permitted from the cylinder",[^olander-2000] and McKee and Van Horn
tested such a package, "Produced by ATMI", for boron trifluoride "on an
Axcelis GSD200E ion implanter in a production
environment".[^mckee-2002]

### Ion-source and beam-line consumables

The arc chamber, cathode and electrodes are consumed by the plasma they
contain. "The ion source is often made of materials with a high melting
point such as tungsten, tungsten doped with lanthanum oxide (lanthanated
tungsten), molybdenum and tantalum", and "Ion sources can often last 300
hours".[^wiki-implant] Horsky's indirectly heated cathode reached lives
"from 70 h at the highest discharge power levels to over 500 h for
moderate operation".[^horsky-1998-ihc] Support gases slow the wear:
"Hydrogen or hydrogen with xenon, krypton or argon may be added to the
plasma to delay the degradation of tungsten components due to the halogen
cycle", and "The hydrogen can come from a high pressure cylinder or from
a hydrogen generator that uses electrolysis".[^wiki-implant] Beam-line
shields catch sputtered material; Swenson et al. added "graphite and
Si-coated shields" to a medium-current beam line to cut metal
contamination.[^swenson-1996] Cryopumps collect hydrogen and hydrides,
and Current lists the "management of potentially explosive gas mixtures
during regeneration of cryopumps" among implanter vacuum
issues.[^current-1996]

## Representative materials and grades

Dopant gases are sold by specialty-gas suppliers in cylinders of a few
litres, usually inside a gas box on the implanter (industry practice; the
ATMI patent cites "0.44 L or 2.3 L cylinders"[^pat-sds-atmi]); solid
sources are
loaded into the vaporiser. SEMI specifies the gases, and suppliers sell
them in proprietary packages. The statements below describe standards
and supplier catalogues, not what SkyWater buys, even where the supplier
is named in SkyWater's filings.

* **Boron trifluoride.** SEMI C3.27 "provide[s] a specification for boron
  trifluoride (BF3) used in the semiconductor industry";[^semi-c3-27]
  NIOSH describes a gas "Shipped as a nonliquefied compressed
  gas".[^niosh-bf3] EMD Electronics offers "Isotopically Enriched BF3" in
  its ION-X package, which "can selectively adsorb, store and safely
  deliver ultra-high purity gases at sub-atmospheric
  pressures".[^emd-ion-x]
* **Phosphine.** SEMI C3.6 provides "specifications for phosphine (PH3)
  that are used in the semiconductor industry";[^semi-c3-6] as a pure
  gas it is "Shipped as a liquefied compressed gas".[^niosh-phosphine]
* **Arsine.** SEMI C3.2 provides "specifications for arsine (AsH3) that
  is used in the semiconductor industry".[^semi-c3-2]
* **Sub-atmospheric packages.** Entegris states that it pioneered "the
  Safe Delivery Source® (SDS®) package over 30 years ago", which
  "provides subatmospheric gas storage and delivery for ion implant
  dopant materials", and that its fourth generation has been qualified
  with "SDS4 phosphine (PH3) and SDS4 arsine (AsH3)
  cylinders".[^entegris-implant-gases] A used 1995 Varian E500 HP lists
  "PH3 - SDS II, AsH3 - SDS II, BF3 - SDS" bottles in its gas
  box.[^fabsurplus-e500]
* **Solid sources.** Elemental phosphorus, arsenic, antimony and indium,
  or their compounds, evaporated in a vaporiser
  ({ref}`category-implant`); "Implanting antimony often requires the use
  of a vaporizer attached to the ion source".[^wiki-implant]
* **Doped-glass sources.** Diluted phosphine for HDP PSG, or an
  organophosphorus liquid (TMPO) for TEOS-based PSG, as the
  {ref}`PSG <step-089>` page reads them; Fujino et al.'s TEOS–ozone PSG
  used trimethylphosphate.[^fujino-1991]
* **Ion-source parts.** Tungsten or lanthanated-tungsten arc chambers,
  cathodes and reflectors;[^wiki-implant] Axcelis names "Source Bushing
  Shields and Extended Life Extraction Electrodes" among its source
  upgrades.[^axcelis-gsd-page]

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page lists three implanters with
their species, under "Ion Implant":[^skw-01]

> "Axcelis 8250 Mid current B11, BF2, As, ESC chuck, E shower, 1e11 to
> 1e14, 0-60 deg tilt"
>
> "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11 to
> 5e15, tilt/twist"
>
> "Axcelis GSD Hi dose B11, BF2, P, As 2-180kev, 5e12 to 5e16,
> tilt/twist"

and, under "Film Deposition", "Lam/Novellus High Density Plasma (HDP)
doped and phos doped with sputter etch".[^skw-01] Read term by term, the
implanter entries give ion species, not source materials: they do not
say whether boron, phosphorus and arsenic come from BF₃, PH₃ and AsH₃ or
from solid sources, and none names indium. The medium-current entry has
no phosphorus. The HDP entry implies a phosphorus source for PSG without
naming it.[^skw-01]

The filings name gas suppliers in the terms quoted on the
{ref}`process gases <material-process-gases>` page: "Air Products &
Chemicals, Inc. (bulk and specialty gases, chemicals)" and "Praxair, Inc.
(bulk and specialty gases)" in the S-1; "Linde, Inc. (bulk and specialty
gases)", "Airgas USA LLC (specialty gases)" and "EMD Performance
Materials Corp (Versum) (specialty chemicals and gases)" in the report
for fiscal 2023.[^sec-01][^sec-02] Neither filing names a dopant gas or a
package. Versum Materials, whose products include "delivery equipment for
the semiconductor industry", was spun off from Air Products in 2016 and
acquired by the Merck Group in 2019;[^wiki-versum] EMD Electronics'
ION-X page quoted above does not name SkyWater, and whether it is the
business the 10-K names is not stated.[^emd-ion-x]

### Strength of the evidence

The species lists are SkyWater statements and rank as **strong** evidence,
on the scale of the {ref}`machines index <machines-reading-evidence>`,
that boron, BF₂, arsenic and (on the GSD tools) phosphorus are implanted
at the fab, and that a phosphorus-doped HDP oxide is deposited; they tie
no species to a step.[^skw-01] That the species come from BF₃, PH₃ and
AsH₃ is industry practice, and sub-atmospheric packages were one delivery
route of the period: hydride sources had been supplied as dilute
high-pressure mixtures before sorbent packages,[^pat-sds-atmi] and McKee
and Van Horn tested a new sub-atmospheric BF₃ package on a GSD200E in
production.[^mckee-2002] Neither is a SkyWater statement. Indium, solid sources,
TMPO and the ion-source parts appear in no SkyWater source cited here.
The supplier statements are strong as statements but name no dopant
gas.[^sec-01][^sec-02]

(material-dopant-sources-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells). The nitrogen
vent gas and helium platen cooling of the implants belong to the
{ref}`process gases <material-process-gases>` page.

Materials index rows covered:

* `ph3` — phosphine, solid phosphorus and TMPO
* `bf3` — boron trifluoride
* `ash3` — arsine and solid arsenic
* `indium` — indium solid source
* `ion-source` — ion-source and beam-line consumables

Steps:

{ref}`DNI <step-008>`, {ref}`LVTNI <step-015>`, {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`, {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`, {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`, {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`NCHI <step-045>`, {ref}`P1I <step-050>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`, {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`, {ref}`HVASTI <step-069>`, {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`, {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`, {ref}`PSG <step-089>`

These are the 25 steps the step pages read as implants, and the doped
glass at {ref}`PSG <step-089>`. On the step pages' readings, boron trifluoride
serves the p-well, threshold, halo, punch-through, resistor and P+
source/drain implants; phosphine the deep N-well, N-well and poly
implants and the PSG; arsine the tips and N+ source/drain; and several
threshold and channel pages
({ref}`LVTNI <step-015>`, {ref}`LVTPI <step-020>`,
{ref}`PCHI <step-023>`, {ref}`DEPI <step-038>`) leave the species open.
Indium is named only at {ref}`LVTNI <step-015>` and
{ref}`PTSI <step-037>`, as an alternative.

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's dopant-gas
storage, gas cabinets, toxic-gas monitoring or abatement; the points below
are industry practice, safety data and supplier statements.

* **Exposure limits.** NIOSH gives arsine an IDLH of "Ca [3 ppm]" and a
  REL of "Ca C 0.002 mg/m3 [15-minute]";[^niosh-arsine] phosphine an IDLH
  of "50 ppm" and a REL of "TWA 0.3 ppm (0.4 mg/m3) ST 1 ppm (1
  mg/m3)";[^niosh-phosphine] and boron trifluoride an IDLH of "25 ppm"
  and a ceiling of "C 1 ppm (3 mg/m3)".[^niosh-bf3]
* **Packaging.** Sub-atmospheric cylinders limit the release from a
  leaking valve or line, since gas flows only into
  vacuum;[^pat-sds-atmi][^olander-2000] they are replaced in the gas box
  of the implanter, which is ventilated and monitored (industry practice).
* **Gas cabinets.** "Toxic or flammable gas cylinders are often stored by
  end users in gas cabinets for protection from external fire or from any
  leak".[^wiki-industrial-gas]
* **Maintenance.** Source changes and beam-line cleaning expose
  technicians to arsenic and phosphorus residues;[^ham-2017] Wikipedia
  notes that "Other common carcinogenic, corrosive, flammable, or toxic
  elements include antimony, arsenic, phosphorus, and
  boron".[^wiki-implant]
* **Vacuum and exhaust.** Cryopump regeneration releases the hydrogen and
  hydrides the pumps have collected, with the explosion hazard Current
  describes;[^current-1996] implanter and gas-cabinet exhaust is scrubbed
  before release (industry practice).

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's species, energies and doses are not
public beyond the ranges SkyWater lists for its tools.[^skw-01]

* **No phosphorus on the medium-current tool.** Because the 8250 entry
  lists "B11, BF2, As" only,[^skw-01] the phosphorus implant pages read
  the GSD tools as the phosphorus implanters (for example
  {ref}`NWI <step-018>`), and the PH₃ row follows them.
* **BF₂ or boron.** The P+ source/drain and halo pages
  ({ref}`PSDI <step-082>`, {ref}`BHI <step-066>`,
  {ref}`LDBHI <step-073>`) discuss B⁺ and BF₂⁺ from the same BF₃
  source;[^wiki-bf3] the choice affects junction depth and the fluorine
  left in the wafer ({ref}`category-implant`), not the gas bought.
* **Fluorine and source life.** The BF₃-heavy implants wear sources
  faster, which the {ref}`PNCHI <step-024>` and {ref}`PWI <step-027>`
  pages note from Axcelis's statement about fluorinated
  species.[^axcelis-gsd-page]
* **Indium as an option.** The {ref}`LVTNI <step-015>` and
  {ref}`PTSI <step-037>` pages name indium because Cypress's SONOS patent
  and article use it for memory-transistor channels;[^pat-04][^cyp-25]
  SkyWater lists no indium, so an indium implant would need a solid
  source on a tool whose entry does not mention one (our
  reading).[^skw-01]
* **Arsenic after the implant.** The arsenic implants leave
  arsenic-bearing resist for the strips that follow
  ({ref}`ASTIS <step-067>`), and arsenic residues in the implanter that
  maintenance must handle.[^ham-2017]
* **Phosphorus in the glass.** SkyWater's "phos doped" HDP entry is the
  public basis for the {ref}`PSG <step-089>` page's HDP reading; that page
  names phosphine for HDP PSG and TMPO or phosphine for a TEOS route, and
  the HDP page notes that Hsiao et al.'s abstract does not name the
  precursor.[^skw-01][^hsiao-2005]

## Related pages

* {ref}`category-implant` — species, energies, doses and implanter
  classes.
* {ref}`machine-medium-current-implanter`,
  {ref}`machine-high-current-implanter` and
  {ref}`machine-high-energy-implanter` — the tools that consume these
  sources.
* {ref}`machine-hdp-cvd` — the phosphorus-doped glass.
* {ref}`material-process-gases` — the nitrogen, helium and hydrogen
  around the implanters.
* {ref}`material-precursors` — the phosphorus-glass precursors.
* {ref}`materials-index` — all consumable classes, including abatement.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.**

* {ref}`US 5,518,528 A <patent-gp23253952>` — Storage and delivery system for gaseous hydride, halide, and organometallic group V compounds (1994)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the implanter and
  HDP entries.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the specialty-gas suppliers.[^sec-01][^sec-02]
* SEMI C3.6, C3.2 and C3.27 — specifications for phosphine, arsine and
  boron trifluoride.[^semi-c3-6][^semi-c3-2][^semi-c3-27]
* NIOSH, *Pocket Guide to Chemical Hazards* — arsine, phosphine and boron
  trifluoride.[^niosh-arsine][^niosh-phosphine][^niosh-bf3]
* Axcelis Technologies, *GSD Ovation* — source upgrades and fluorinated
  species.[^axcelis-gsd-page]
* Entegris, *Specialty Gases and Delivery Systems for Ion Implantation*
  and EMD Electronics, *ION-X BF3* — current sub-atmospheric
  packages.[^entegris-implant-gases][^emd-ion-x]
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098, and
  Ramkumar, Prabhakar and Kapre, *Semiconductor Digest* 2020 — indium in
  Cypress SONOS channels.[^pat-04][^cyp-25]
* Fabsurplus, *Varian E500 HP* — a medium-current gas box with SDS
  bottles.[^fabsurplus-e500]

### High-level understanding

* Wikipedia, *Ion implantation* — sources, support gases, solid sources
  and hazards.[^wiki-implant]
* Wikipedia, *Boron trifluoride*, *Phosphine* and *Arsine* — the dopant
  gases.[^wiki-bf3][^wiki-ph3][^wiki-ash3]
* Wikipedia, *Industrial gas* and *Versum Materials* — gas cabinets and
  a supplier's history.[^wiki-industrial-gas][^wiki-versum]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ion implantation equipment.[^txt-02]

### Deep dive

* Tom and McManus (ATMI), US 5,518,528 — the sorbent sub-atmospheric
  hydride source.[^pat-sds-atmi]
* Olander et al., IIT 2000 — the vacuum-actuated cylinder.[^olander-2000]
* McKee and Van Horn, IIT 2002 — a sub-atmospheric BF₃ package on a
  production GSD implanter.[^mckee-2002]
* Horsky, *Rev. Sci. Instrum.* 1998 — the indirectly heated cathode
  source and its life.[^horsky-1998-ihc]
* Swenson et al., IIT 1996 — shields against metal contamination in a
  medium-current beam line.[^swenson-1996]
* Current, *JVST A* 1996 — implanter vacuum, including cryopump
  regeneration.[^current-1996]
* Ham et al., *Aerosol and Air Quality Research* 2017 — arsenic exposure
  during implanter maintenance.[^ham-2017]
* Shahidi et al., *IEEE EDL* 1993 — indium channel
  implants.[^shahidi-1993]
* Momiyama et al., VLSI 1999 — tilted indium channel implantation for
  60 nm nMOSFETs.[^momiyama-1999]
* Hsiao, Liu and Wang, *JVST B* 2005 — HDP phosphosilicate
  glass.[^hsiao-2005]
* Fujino et al., *JES* 1991 — PSG and BSG from TEOS and ozone with
  organic dopant sources.[^fujino-1991]
* Ryssel and Ruge, *Ion Implantation* — ion sources and implanter
  technology.[^ryssel-1986]

## Open questions

* Whether SkyWater's boron, phosphorus and arsenic beams come from gas or
  solid sources, in which packages and from which supplier, is not
  stated.[^skw-01][^sec-01][^sec-02]
* Whether any SKY130 implant uses indium, which no SkyWater implanter
  entry lists, is not public.[^skw-01]
* Which phosphorus source the "phos doped" HDP process uses is not
  stated.[^skw-01]
* Whether "EMD Performance Materials Corp (Versum)" in the 2023 report
  supplies dopant gases is not stated.[^sec-02]

<!-- footnotes -->

[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-ash3]: Wikipedia, *Arsine*. <https://en.wikipedia.org/wiki/Arsine>
[^pat-sds-atmi]: G. M. Tom and J. V. McManus (Advanced Technology
    Materials), *Storage and delivery system for gaseous hydride, halide,
    and organometallic group V compounds*, US 5,518,528 A, granted
    1996-05-21. <https://patents.google.com/patent/US5518528A/en>
[^semi-c3-6]: SEMI, *SEMI C3.6 — Specification for Phosphine (PH3) in
    Cylinders, 99.98% Quality*, SEMI Standards store listing (revision
    C3.6-0421), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00306-semi-c3-6-specification-for-phosphine-ph3-in-cylinders-99-98-quality>
[^semi-c3-2]: SEMI, *SEMI C3.2 — Specification for Arsine (AsH3) in
    Cylinders, 99.94% Quality*, SEMI Standards store listing (revision
    C3.2-0611 (Reapproved 0218)), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00302-semi-c3-2-specification-for-arsine-ash3-in-cylinders-99-94-quality>
[^semi-c3-27]: SEMI, *SEMI C3.27 — Specification for Boron Trifluoride
    (BF3) in Cylinders, 99.0% Quality*, SEMI Standards store listing
    (revision C3.27-1102 (Reapproved 0118)), accessed 2026-09-13.
    <https://store-us.semi.org/products/c00327-semi-c3-27-specification-for-boron-trifluoride-bf3-in-cylinders-99-0-quality>
[^niosh-arsine]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Arsine*, CDC; read from the
    Wayback Machine capture of 2025-11-30.
    <https://www.cdc.gov/niosh/npg/npgd0040.html>
    <https://web.archive.org/web/20251130093607/https://www.cdc.gov/niosh/npg/npgd0040.html>
[^niosh-phosphine]: National Institute for Occupational Safety and
    Health, *NIOSH Pocket Guide to Chemical Hazards: Phosphine*, CDC;
    read from the Wayback Machine capture of 2025-11-30.
    <https://www.cdc.gov/niosh/npg/npgd0505.html>
    <https://web.archive.org/web/20251130140523/https://www.cdc.gov/niosh/npg/npgd0505.html>
[^niosh-bf3]: National Institute for Occupational Safety and Health,
    *NIOSH Pocket Guide to Chemical Hazards: Boron trifluoride*, CDC;
    read from the Wayback Machine capture of 2026-01-15.
    <https://www.cdc.gov/niosh/npg/npgd0062.html>
    <https://web.archive.org/web/20260115022425/https://www.cdc.gov/niosh/npg/npgd0062.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; ion implant and film deposition entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing"; read from a Wayback Machine copy on
    2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph; read from a Wayback Machine
    copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^emd-ion-x]: EMD Electronics (Merck KGaA, Darmstadt), *ION-X® BF3 —
    Boron Trifluoride ION-X® Dopant Gas Storage and Delivery System*,
    product page, accessed 2026-09-13.
    <https://www.emdgroup.com/en/expertise/semiconductors/offering/isotopically-enriched-bf3.html>
[^axcelis-gsd-page]: Axcelis Technologies, *GSD Ovation — High Current &
    High Energy Batch Ion Implanters*, product page, accessed
    2026-08-30; re-checked 2026-09-13.
    <https://www.axcelis.com/products/gsd-ovation/>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^hsiao-2005]: W.-C. Hsiao, C.-P. Liu and Y.-L. Wang, "Influence of
    thermal budget on phosphosilicate glass prepared by high-density
    plasma chemical-vapor deposition", *Journal of Vacuum Science &
    Technology B* **23**(5), 2146–2150 (2005).
    <https://doi.org/10.1116/1.2050670>
[^fujino-1991]: K. Fujino, Y. Nishimoto, N. Tokumasu and K. Maeda,
    "Doped Silicon Oxide Deposition by Atmospheric Pressure and Low
    Temperature Chemical Vapor Deposition Using Tetraethoxysilane and
    Ozone", *Journal of The Electrochemical Society* **138**(10),
    3019–3024 (1991). <https://doi.org/10.1149/1.2085358>
[^ham-2017]: S. Ham, C. Yoon, S. Kim, J. Park, O. Kwon, J. Heo, D. Park,
    S. Choi, S. Kim, K. Ha and W. Kim, "Arsenic Exposure during
    Preventive Maintenance of an Ion Implanter in a Semiconductor
    Manufacturing Factory", *Aerosol and Air Quality Research* **17**(4),
    990–999 (2017). <https://doi.org/10.4209/aaqr.2016.07.0310>
[^shahidi-1993]: G. G. Shahidi, B. Davari, T. J. Bucelot, P. A.
    Ronsheim, P. J. Coane, S. Pollack, C. R. Blair, B. Clark and H. H.
    Hansen, "Indium channel implant for improved short-channel behavior
    of submicrometer NMOSFETs", *IEEE Electron Device Letters*
    **14**(8), 409–411 (1993). <https://doi.org/10.1109/55.225595>
[^momiyama-1999]: Y. Momiyama, S. Yamaguchi, S. Ohkubo and T. Sugii,
    "Indium tilted channel implantation technology for 60 nm nMOSFET",
    *1999 Symposium on VLSI Technology, Digest of Technical Papers*,
    pp. 67–68. <https://doi.org/10.1109/VLSIT.1999.799343>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098 B1,
    granted 2014-08-05. <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^cyp-25]: K. Ramkumar, V. Prabhakar and R. Kapre (Cypress
    Semiconductor), *Scalable SONOS based embedded non-volatile memory
    technology*, Semiconductor Digest, 2020-02.
    <https://sst.semiconductor-digest.com/2020/02/scalable-sonos-based-embedded-non-volatile-memory-technology/>
[^olander-2000]: W. K. Olander, M. Donatucci, J. Mayer and L. Wang,
    "Vacuum actuated gas delivery", *2000 International Conference on
    Ion Implantation Technology Proceedings*, pp. 722–725.
    <https://doi.org/10.1109/IIT.2000.924255>
[^mckee-2002]: D. J. McKee and L. J. Van Horn, "Evaluation and
    integration of a new gas source package for boron trifluoride used
    in ion implantation", *Proc. 14th International Conference on Ion
    Implantation Technology* (2002), pp. 424–427.
    <https://doi.org/10.1109/IIT.2002.1258031>
[^horsky-1998-ihc]: T. N. Horsky, "Indirectly heated cathode arc
    discharge source for ion implantation of semiconductors", *Review of
    Scientific Instruments* **69**(4), 1688–1690 (1998).
    <https://doi.org/10.1063/1.1148866>
[^swenson-1996]: D. R. Swenson, D. F. Downey, S. R. Walther, A. Renau,
    G. Gammel and M. E. Mack, "Metals-contamination-reduction program for
    the Varian EHP-220/500 medium-current ion implanter", *Proc. 11th
    International Conference on Ion Implantation Technology* (1996),
    pp. 139–142. <https://doi.org/10.1109/IIT.1996.586154>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^entegris-implant-gases]: Entegris, *Specialty Gases and Delivery
    Systems for Ion Implantation*, industry-insights page, accessed
    2026-09-13.
    <https://www.entegris.com/en/home/resources/industry-insights/specialty-gases-and-delivery-systems-for-ion-implantation.html>
[^fabsurplus-e500]: Fabsurplus (SDI), *Varian E500 HP Medium Current
    Implanter* (used-equipment specification sheet, item 44950),
    accessed 2026-09-13.
    <https://www.fabsurplus.com/sdicatalog/download?id=44950>
[^wiki-versum]: Wikipedia, *Versum Materials*.
    <https://en.wikipedia.org/wiki/Versum_Materials>
[^wiki-industrial-gas]: Wikipedia, *Industrial gas*.
    <https://en.wikipedia.org/wiki/Industrial_gas>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^ryssel-1986]: H. Ryssel and I. Ruge, *Ion Implantation*, Wiley, 1986,
    ISBN 978-0-471-10311-0. <https://openlibrary.org/isbn/9780471103110>
