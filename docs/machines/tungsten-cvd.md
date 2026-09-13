(machine-tungsten-cvd)=
# Tungsten CVD

A tungsten CVD system is the cold-wall reactor a fab uses to fill
contact and via holes with tungsten. The wafer sits on a heated pedestal
while tungsten hexafluoride is reduced first by silane, to nucleate a
thin layer on the liner, and then by hydrogen, to grow a blanket film
that closes every hole from its walls inward; the film on the field is
polished away afterwards, leaving the plugs. The tools of the 200 mm era
were either single-wafer chambers on a cluster platform or multi-station
chambers that pass each wafer under several pedestals in turn. This page
describes the class in general, lists representative 200 mm-era models,
and then says what SkyWater has published about its own tool of this
class and which SKY130 steps this reference assigns to it. The tungsten
chemistry is summarised on the {ref}`category page
<category-deposition>`; the liner deposited before each fill is
described on the category page and the step pages.

| | Tungsten CVD |
|---|---|
| What it does | Deposits blanket tungsten for plugs: "WF6 is commonly used by the semiconductor industry to form tungsten films, through the process of chemical vapor deposition";[^wiki-wf6] Novellus sold "blanket tungsten deposition for plug fill and low-stress composite interconnects".[^novellus-wcvd-1998] |
| Chemistry | WF₆ + 3H₂ → W + 6HF;[^wiki-wf6] hydrogen and silicon reduction of WF₆ studied "within a pressure range of 0.1–5 torr and a temperature range of 250°–500°C";[^rev-03] hydrogen reduction "one‐half order in hydrogen, zero order in tungsten hexafluoride".[^mcconica-1986] |
| Pressure and temperature | "from about 20 to 760 Torr to improve the deposition rate" in an Applied Materials patent;[^pat-wcvd-amat] "80 torr and 475°C" on an Applied P5000 WCVD;[^riley-1991] "300 Torr" for Applied's Sprint;[^amat-ism-2000] pulsed nucleation at "approximately 250 and 475° C.".[^pat-pnl-novellus] |
| Nucleation | Novellus's pulsed nucleation "alternatively" provides "reducing gases and tungsten-containing gases", each cycle giving "one or more monolayers";[^pat-pnl-novellus] conventional nucleation layers "approximately 1000 Å thick" on "the TiN/Ti glue layer stack" in Hegde et al.'s study.[^hegde-1997] |
| Wafer handling | Multi-station: the Concept One-W had "six-wafer chambers, where five were used for deposition and one for loading";[^novellus-history] the Dual Altus "a total of 10 stations".[^novellus-wcvd-1998] Single-wafer: the Precision 5000 WCVD of 1989[^amat-1997] and the WxZ Centura.[^amat-ism-2000] |
| 200 mm era | Applied's Precision 5000 WCVD (1989),[^amat-1997] WxZ Centura and Sprint;[^amat-ism-2000] Novellus's Concept One-W (1990) and Concept Two Altus (1993).[^novellus-history] |
| SkyWater-listed tool | "Lam/Novellus PECVD Tungsten" ("plug fill", "{term}`PNL` option for high aspect ratio (up to 10:1)")[^skw-01] |
| SKY130 steps | 5 steps; see {ref}`SKY130 steps assigned to this class <machine-tungsten-cvd-steps>` |

## What the machine class is and how it works

Tungsten plugs are grown, not sputtered. Kaanta et al.'s wiring
technology of 1987 used "CVD-tungsten (W) and planarization", with
"Vertical W studs" that "maximize density by reducing contact/via ground
rules",[^kaanta-1987] and the scheme — a blanket fill followed by removal
from the field — became the standard contact and via process of the
aluminium generations (category page). A tungsten CVD reactor is a
cold-wall chamber with a resistively heated pedestal, a showerhead for
WF₆, H₂, SiH₄, argon and nitrogen, and a way of keeping tungsten off the
wafer's edge and back. What makes a machine a production tungsten tool is
nucleation that starts reliably on the liner, a bulk fill that closes
holes without voids at an acceptable rate, control of edge and backside
deposition, and a chamber clean.

### Chemistry and kinetics

Wikipedia gives the bulk reaction as WF₆ + 3H₂ → W + 6HF and notes that
"The decomposition is usually facilitated by mixing WF6 with hydrogen,
silane, germane, diborane, phosphine, and related hydrogen-containing
gases"; the by-product is a problem, since "HF vapor is very aggressive
and etches away most materials", and "the deposited tungsten shows poor
adhesion to the silicon dioxide".[^wiki-wf6] Broadbent and Ramiller
found the hydrogen reduction limited by the dissociation of adsorbed
hydrogen, with an activation energy of 0.71 eV, and a self-limiting
deposit from the reaction of WF₆ with silicon.[^rev-03] McConica and
Krishnamani measured the rate law in a single-wafer reactor —
"one‐half order in hydrogen, zero order in tungsten hexafluoride" — and
found that during hydrogen reduction "selectivity was lost in less than
600s at temperatures above 653 K (380°C)".[^mcconica-1986] Because the
reaction is fast, transport matters: Kleijn et al. showed that "large
concentration gradients may be present in CVD reactors, even at low
reactant conversion rates", and that "thermal diffusion phenomena in
coldwall reactors are very important".[^kleijn-1991]

### Nucleation on the liner

Tungsten does not start growing evenly on every surface. McConica and
Cooper found that on oxide "The observed nucleation is autocatalytic and
initiated by an intermediate diffusing from areas of tungsten
deposition".[^mcconica-1988] On a contact liner the nucleation layer is
therefore grown separately, by silane reduction, before the hydrogen
fill (category page). Hegde et al. compared nucleation layers
"approximately 1000 Å thick" grown on "the TiN/Ti glue layer stack" at
two gas-flow ratios, and found one "far smoother and less porous" and "a
better diffusion barrier".[^hegde-1997] The liner and nucleation together
must keep WF₆ from the silicon: Saito et al. traced open contacts to a
"chemical reaction on the interface through a previously deposited,
porous, glue layer of sputtered tungsten during high-pressure blanket
tungsten CVD processing", suppressed by a hydrogen anneal and "a
low-pressure hydrogen reduction CVD tungsten nucleation
step".[^saito-1993] Additions to the gas change the growth after
nucleation: nitrogen "induces an incubation time, delaying the onset of
deposition of the main film by up to 5 seconds",[^petri-1998] and an
Applied Materials patent deposits tungsten "in the presence of nitrogen
gas to improve the reflectivity of the surface".[^pat-wcvd-amat]

### Pulsed nucleation

Novellus's pulsed nucleation layer ({term}`PNL`) replaces the continuous
silane–WF₆ nucleation with alternating doses: "A tungsten nucleation film
is formed on a surface of a semiconductor substrate by alternatively
providing to that surface, reducing gases and tungsten-containing gases.
Each cycle of the method provides for one or more monolayers of the
tungsten film. The film is conformal and has improved step coverage, even
for a high aspect ratio contact hole."[^pat-pnl-novellus] The patent heats
the wafer to between "approximately 250 and 475° C.", names silane and
diborane among the reducing and soak gases, and states that the process
"may be carried out in a Novellus Altus CVD chamber, the Concept 2 Altus
chamber, the Concept 3 Altus processing chamber, or any of a variety of
other commercially available CVD tools", and in one arrangement runs
the pulsed steps at the first stations of a multi-station chamber and
the hydrogen-reduction fill at the last.[^pat-pnl-novellus] A related
pulsed CVD nucleation layer reported by Kim et al. showed "much lower root mean square (rms)
roughness (0.87 nm) and better conformality at the contact holes with an
aspect ratio of 14" than conventional CVD.[^kim-2004]

### Multi-station and single-wafer reactors

Novellus built its tungsten tools around multi-station chambers. Its
1990 Concept One-W "combined batch and
wafer-at-a-time processing", and "A previous problem of tungsten deposit
backslides was also solved with a combination of vacuum-clamping and
gas-exclusion techniques".[^novellus-history] Novellus later listed the
features as "high-pressure nucleation, resistive heating, vacuum wafer
clamping and full-coverage deposition, using patented wafer backside
exclusion technology".[^novellus-wcvd-1998] Its backside-protection patent
describes the station: "a gas dispersion head disposed over a platen", a
vacuum chuck, a platen heater, and backside gas at "a level greater than
the CVD chamber pressure", so that it "vents from beneath the edge of the
wafer on the platen and prevents the process gas from contacting the
wafer backside".[^pat-backside-novellus] A later Novellus patent separates
incompatible steps between stations of one chamber, with "an indexing
plate" to move the wafers, so that "while one process, such as a silane
initiation is performed at one station, other stations may
contemporaneously perform an incompatible process, such as a tungsten
hexafluoride-silane nucleation process and hydrogen
reduction".[^pat-multistation-novellus]

Applied Materials used single-wafer chambers. Its Precision 5000 WCVD
of 1989 was "a new system for depositing blanket tungsten (W)
film".[^amat-1997] Riley and Clark ran an "integrated deposition and
etchback process" on a P5000 WCVD, depositing tungsten "at 80 torr and
475°C" and etching back in a magnetron chamber on the same
system.[^riley-1991] By 2000 the WxZ Centura was, in Applied's words,
"the industry's leading tungsten chemical vapor deposition (WCVD) tool
for plug fill and interconnects", with "both full coverage and edge
exclusion CMP- and etchback-compatible processes"; the Sprint "operates
at 300 Torr" at ">60 wph", with "a new wafer heater with a ceramic ring"
and "two in situ clean options — RF and microwave", retrofittable "to
most existing WxZ Centura systems".[^amat-ism-2000]

### Cleaning and stress

Tungsten builds up on the showerhead, pedestal ring and walls. Applied
developed "a remote microwave clean technology for the WxZ chamber" whose
"free reactive flourine radicals" extend "process kit
lifetime";[^amat-ism-2000] fluorine radicals from NF₃ "can be used as
well to remove tungsten silicide, tungsten, and certain other
metals".[^wiki-nf3] The film itself is under stress: Shioya et al. found
that the stress in CVD tungsten "reaches a maximum at 550 °C", a
behaviour whose cause "is not clear".[^shioya-1987]

## Representative 200 mm-era models

* **Applied Materials.** The Precision 5000 WCVD (1989), with CVD
  tungsten silicide from 1991, and metal CVD chambers "now being shipped
  on the Centura and Endura platforms" by 1997;[^amat-1997] the WxZ
  Centura, offered with a remote microwave clean, and the Sprint
  Centura, "extendible to 0.13µm generation devices and
  beyond".[^amat-ism-2000]
* **Novellus Systems.** The Concept One-W, introduced in September 1990
  and certified by Sematech in 1993, and the Concept Two Altus of 1993,
  which "combined the modular architecture of the Concept Two and the
  tungsten CVD process chamber".[^novellus-history] Novellus described
  the Altus as "Integrating the Concept One tungsten process chamber on
  the modular Concept Two platform", with "uniform deposition to 194mm",
  and the Dual Altus as "two Concept One process chambers for a total of
  10 stations";[^novellus-wcvd-1998] the 300 mm Concept Three Altus
  followed.[^novellus-wcvd-2002] The company history records that the
  first Concept One-W sale was to "Cypress Semiconductor's fabrication
  facility", jointly with a Lam metal etcher;[^novellus-history] it does
  not say which Cypress fab, and a sale of that time is not evidence
  about the tool SkyWater lists today.
* **Other vendors.** The step pages also name Genus, ULVAC and Tokyo
  Electron tungsten CVD systems ({ref}`WDEP2 <step-110>`); no vendor
  description of them was retrieved for this page.

## At SkyWater

### What SkyWater lists

Under "Film Deposition", SkyWater's *Facilities & Capabilities* page
lists one tungsten entry with two sub-entries:[^skw-01]

> "Lam/Novellus PECVD Tungsten"
>
> "– plug fill"
>
> "– PNL option for high aspect ratio (up to 10:1)"

Read term by term: a tungsten deposition tool from Lam or Novellus, used
for plug fill, with a pulsed-nucleation option rated to a 10:1 aspect
ratio. The page does not explain "PECVD"; the step pages read the word as
a label for the tungsten CVD tool rather than as evidence of a
plasma-driven deposition (inference), and we read "PNL" as the pulsed
nucleation layer of Novellus's patent, which does not itself use the
abbreviation.[^pat-pnl-novellus] Elsewhere the page
lists a special module "W plug dual damascene", CMP of "tungsten" and
"high selectivity tungsten", "WN" among the PVD films, and "W/WN" as an
application of the AMAT DPSII etcher.[^skw-01] It gives no model,
temperature or nucleation chemistry.

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong** for the vendor, the plug-fill application and the
PNL option: it is a SkyWater statement.[^skw-01] The model is not
stated; the step pages read it as an Altus-class system from Novellus's
product history, an inference, and the PNL patent's naming of Altus
chambers[^pat-pnl-novellus] supports that reading without confirming it.
"Lam/Novellus" fits a Novellus tool after Novellus became part of Lam in
2012 (our reading).[^wiki-novellus] The caveats that apply to every
listed tool are under
{ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-tungsten-cvd-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a tungsten CVD
reactor as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Lam/Novellus PECVD Tungsten"** — *inference:* {ref}`WDEP <step-099>`, {ref}`WDEP2 <step-110>`, {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`, {ref}`WDEP5 <step-147>`
* **The special module as well** — "W plug dual damascene": *strong for
  the capability:* {ref}`WDEP <step-099>`; the full row, which also
  covers the nitrided-oxide and silicide modules, is on the machines
  index.

Every page grades the tool strong for vendor, process and the PNL
option and the assignment an inference; the metal-contact and via pages
add that whether the PNL option is used at their level is not
public.[^skw-01]

## Consumables and facilities

The process gases are listed in the {ref}`materials index
<materials-index>`; what is specific to a tungsten CVD tool is
summarised here. None of the SkyWater sources describes the fab's gas
delivery, pumps or abatement.

* **Tungsten hexafluoride.** "a toxic, corrosive, colorless gas", which
  "On contact with water" gives "hydrogen fluoride (HF) and tungsten
  oxyfluorides"; consumption, driven by the semiconductor industry,
  "remains at around 200 tonnes per year worldwide".[^wiki-wf6]
* **Reducing and carrier gases.** Hydrogen for the bulk fill, silane for
  nucleation, diborane where the nucleation uses it,[^pat-pnl-novellus]
  argon or argon–hydrogen for backside protection[^pat-backside-novellus]
  and nitrogen as an additive.[^pat-wcvd-amat][^petri-1998]
* **Exhaust.** HF from the reaction, which "is very aggressive and etches
  away most materials",[^wiki-wf6] and SiF₄ from silane reduction
  (category page).
* **Clean gases and kit.** Fluorine from a remote or in-situ
  plasma;[^amat-ism-2000][^wiki-nf3] heaters, ceramic or exclusion rings
  and showerheads, which the clean and the film wear.[^amat-ism-2000][^novellus-wcvd-2002]
* **Monitor wafers.** Sheet resistance, thickness, stress and particles
  on blanket wafers, and cross-sections of filled holes, as the step pages
  describe ({ref}`WDEP2 <step-110>`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's tungsten recipes and
thicknesses are not public.

* **A liner first.** Every fill lands on titanium nitride deposited in the
  PVD tool just before it ({ref}`TI/TIN1 <step-097>`,
  {ref}`TIN2 <step-109>` to {ref}`TIN5 <step-146>`), because WF₆ and its
  HF attack silicon, titanium and oxide and tungsten adheres poorly to
  oxide (category page;[^wiki-wf6] the {ref}`WDEP <step-099>` page
  describes the barrier role). Saito et al.'s failure through a porous
  glue layer shows what the liner prevents.[^saito-1993]
* **Holes from 6:1 down to about 2:1.** The {ref}`WDEP4 <step-132>` page
  puts the local-interconnect contact of {ref}`WDEP <step-099>` at about
  6:1 and the via-2 holes at about 2.1:1; the {ref}`WDEP5 <step-147>`
  page gives about 1.95:1 for via 3. All are within the listed "up to
  10:1", and whether the PNL option runs at any level is not
  public.[^skw-01]
* **Fill and polish.** The blanket fill is removed from the field by the
  tungsten polishes ({ref}`WCMPLI <step-100>`, {ref}`WCMP2 <step-111>`
  to {ref}`WCMP5 <step-148>`), on SkyWater's "tungsten" or "high
  selectivity tungsten" CMP processes, which of the two the CMP pages
  say is not public.[^skw-01] A seam left where the walls meet is the
  category page's description of a conformal fill.
* **Plug tops under aluminium.** After the polish, each metal stack of
  the {ref}`PVD page <machine-pvd-cluster-tool>` is sputtered onto the
  plug tops, and the metal etch lands on them
  ({ref}`metal etcher page <machine-plasma-etcher-metal>`).
* **The special module.** SkyWater's "W plug dual damascene" special
  module is listed without explanation; the {ref}`WDEP <step-099>` page
  grades it strong for the capability of tungsten-plug processing and
  notes that the "damascene" wording is not explained.[^skw-01]

## Related pages

* {ref}`category-deposition` — CVD tungsten chemistry and the deposition
  steps of SKY130.
* {ref}`machine-pvd-cluster-tool` — the liner deposition before each fill
  and the metal stacks that land on the plugs.
* {ref}`machine-plasma-etcher-metal` — the aluminium etch that stops on
  the plug tops.
* {ref}`category-cmp` — the tungsten polishes that follow each fill.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — tungsten hexafluoride, silane and the clean
  gases.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the tungsten entry,
  its PNL option and the related special module, CMP, PVD and etch
  entries.[^skw-01]
* Novellus Systems, *Tungsten Product Solutions* (1998 and 2002
  captures) — the Altus, Dual Altus and Concept Three Altus and their
  backside exclusion.[^novellus-wcvd-1998][^novellus-wcvd-2002]
* Applied Materials, *Interconnect Systems & Modules* page (2000) — the
  WxZ Centura, its remote microwave clean and the Sprint.[^amat-ism-2000]
* Applied Materials, *1997 Annual Report* — the Precision 5000 WCVD and
  the metal CVD platforms.[^amat-1997]
* Encyclopedia.com, *Novellus Systems, Inc.* — the Concept One-W and
  Concept Two Altus history.[^novellus-history]
* Lee and Collins (Novellus), US 6,635,965 — the pulsed nucleation layer
  and the Altus chambers.[^pat-pnl-novellus]
* Van de Ven et al. (Novellus), US 5,374,594 — backside gas protection
  in a multi-station tungsten reactor.[^pat-backside-novellus]
* McInerney, Pratt and Hancock (Novellus), US 6,319,553 — incompatible
  processes at separate stations of one chamber.[^pat-multistation-novellus]
* Chang et al. (Applied Materials), US 5,028,565 — high-pressure tungsten
  CVD with nitrogen and a nucleation layer.[^pat-wcvd-amat]

### High-level understanding

* Wikipedia, *Tungsten hexafluoride* — the precursor, its CVD reactions
  and its hazards.[^wiki-wf6]
* Wikipedia, *Nitrogen trifluoride* — the clean gas.[^wiki-nf3]
* Wikipedia, *Novellus Systems* — the vendor and its acquisition by
  Lam.[^wiki-novellus]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — CVD tungsten in
  the back end.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — tungsten plugs
  in deep-submicron processes.[^txt-05]

### Deep dive

* Broadbent and Ramiller, *J. Electrochem. Soc.* 1984 — kinetics of WF₆
  reduction by hydrogen and silicon.[^rev-03]
* McConica and Krishnamani, *J. Electrochem. Soc.* 1986 — the rate law
  and loss of selectivity in a single-wafer reactor.[^mcconica-1986]
* McConica and Cooper, *J. Electrochem. Soc.* 1988 — autocatalytic
  nucleation on thermal oxide.[^mcconica-1988]
* Kleijn et al., *J. Electrochem. Soc.* 1991 — transport limits in a
  cold-wall single-wafer reactor.[^kleijn-1991]
* Riley and Clark, *J. Electrochem. Soc.* 1991 — integrated deposition
  and etchback on a P5000 WCVD system.[^riley-1991]
* Kaanta et al., IEDM 1987 — the CVD tungsten stud and planarisation
  wiring scheme.[^kaanta-1987]
* Shioya et al., *JAP* 1987 — stress in CVD tungsten and tungsten
  silicide at high temperature.[^shioya-1987]
* Saito et al., IRPS 1993 — contact failure through a porous glue layer
  and its cure.[^saito-1993]
* Hegde et al., *J. Electrochem. Soc.* 1997 — properties of tungsten
  nucleation layers on TiN/Ti.[^hegde-1997]
* Petri et al., IITC 1998 — nitrogen and the incubation of post-nucleation
  growth.[^petri-1998]
* Ireland, *Thin Solid Films* 1997 — a review of the tungsten plug
  process for high-aspect-ratio contacts.[^ireland-1997]
* Kim et al., *Electrochem. Solid-State Lett.* 2004 — a pulsed CVD
  tungsten nucleation layer for plug fill.[^kim-2004]

## Open questions

* What "PECVD" denotes in SkyWater's "Lam/Novellus PECVD Tungsten" is not
  stated.[^skw-01]
* Whether SkyWater's tool is an Altus-class multi-station system, and
  whether its PNL option is used at any SKY130 level, are not public.
* What the "W plug dual damascene" special module is, and whether it
  concerns the SKY130 plugs, is not stated.[^skw-01]
* The model list above is incomplete: it covers the Applied Materials and
  Novellus systems for which a public description was found, not the
  Genus, ULVAC, Tokyo Electron and other tungsten CVD systems of the
  period.

<!-- footnotes -->

[^wiki-wf6]: Wikipedia, *Tungsten hexafluoride*.
    <https://en.wikipedia.org/wiki/Tungsten_hexafluoride>
[^novellus-wcvd-1998]: Novellus Systems, *Tungsten Product Solutions*
    (metal CVD), product page; Wayback Machine capture of 1998-06-11.
    <https://web.archive.org/web/19980611202803/http://www.novellus.com:80/products/cvd.htm>
[^rev-03]: E. K. Broadbent and C. L. Ramiller, "Selective Low Pressure
    Chemical Vapor Deposition of Tungsten", *Journal of The
    Electrochemical Society* **131**(6), 1427–1433 (1984).
    <https://doi.org/10.1149/1.2115864>
[^mcconica-1986]: C. M. McConica and K. Krishnamani, "The Kinetics of
    LPCVD Tungsten Deposition in a Single Wafer Reactor", *Journal of The
    Electrochemical Society* **133**(12), 2542–2548 (1986).
    <https://doi.org/10.1149/1.2108468>
[^pat-wcvd-amat]: M. Chang, C. Leung, D. N. Wang and D. Cheng (Applied
    Materials), *Process for CVD deposition of tungsten layer on
    semiconductor wafer*, US 5,028,565 A, filed 1989-08-25, granted
    1991-07-02. <https://patents.google.com/patent/US5028565A/en>
[^riley-1991]: P. E. Riley and T. E. Clark, "Integrated Chemical Vapor
    Deposition and Plasma Etchback of Tungsten in a Multichamber,
    Single-Wafer System", *Journal of The Electrochemical Society*
    **138**(10), 3008–3013 (1991). <https://doi.org/10.1149/1.2085356>
[^amat-ism-2000]: Applied Materials, *Interconnect Systems & Modules*
    (liner/barrier and tungsten CVD systems), product page; Wayback
    Machine capture of 2000-08-15.
    <https://web.archive.org/web/20000815075033/http://www.appliedmaterials.com:80/products/ism_liner.html>
[^pat-pnl-novellus]: S.-H. Lee and J. Collins (Novellus Systems), *Method
    for producing ultra-thin tungsten layers with improved step coverage*,
    US 6,635,965 B1, filed 2001-10-09, granted 2003-10-21.
    <https://patents.google.com/patent/US6635965B1/en>
[^hegde-1997]: R. I. Hegde, P. J. Tobin, A. R. Sitaram and J. Klein, "Thin
    Film Properties of Tungsten Nucleation Layer in Blanket Tungsten
    Deposition", *Journal of The Electrochemical Society* **144**(3),
    1087–1090 (1997). <https://doi.org/10.1149/1.1837536>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.* (company
    history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; film deposition, special module, CMP and etch entries
    re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^kaanta-1987]: C. Kaanta, W. Cote, J. Cronin, K. Holland et al.,
    "Submicron wiring technology with tungsten and planarization", *IEDM
    1987 Technical Digest*, pp. 209–212.
    <https://doi.org/10.1109/IEDM.1987.191389>
[^kleijn-1991]: C. R. Kleijn, C. J. Hoogendoorn, A. Hasper, J. Holleman
    and J. Middelhoek, "Transport Phenomena in Tungsten LPCVD in a
    Single-Wafer Reactor", *Journal of The Electrochemical Society*
    **138**(2), 509–517 (1991). <https://doi.org/10.1149/1.2085620>
[^mcconica-1988]: C. M. McConica and K. Cooper, "Tungsten Nucleation on
    Thermal Oxide during LPCVD of Tungsten by the Hydrogen Reduction of
    Tungsten Hexafluoride", *Journal of The Electrochemical Society*
    **135**(4), 1003–1008 (1988). <https://doi.org/10.1149/1.2095756>
[^saito-1993]: T. Saito, H. Aoki, T. Tamaru and N. Owada, "Reliability
    improvement in blanket tungsten CVD contact filling process for high
    aspect ratio contact", *31st Annual Proceedings, Reliability Physics
    1993*, pp. 334–339. <https://doi.org/10.1109/RELPHY.1993.283279>
[^petri-1998]: R. Petri, H. Hauf, D. Berenbaum, J. C. Favreau and P.
    Mazet, "Nitrogen effect on post-nucleation tungsten CVD film growth",
    *Proc. IEEE 1998 International Interconnect Technology Conference*,
    pp. 202–204. <https://doi.org/10.1109/IITC.1998.704792>
[^kim-2004]: S.-H. Kim, E.-S. Hwang, S.-Y. Han, S.-H. Pyi, N. Kwak,
    H. Sohn, J. Kim and G. B. Choi, "Pulsed CVD of Tungsten Thin Film as
    a Nucleation Layer for Tungsten Plug-Fill", *Electrochemical and
    Solid-State Letters* **7**(9), G195 (2004).
    <https://doi.org/10.1149/1.1784053>
[^pat-backside-novellus]: E. P. van de Ven, E. K. Broadbent, J. C.
    Benzing, B. L. Chin and C. W. Burkhart (Novellus Systems), *Gas-based
    backside protection during substrate processing*, US 5,374,594 A,
    filed 1993-01-22, granted 1994-12-20.
    <https://patents.google.com/patent/US5374594A/en>
[^pat-multistation-novellus]: E. J. McInerney, T. M. Pratt and S. D.
    Hancock (Novellus Systems), *Isolation of incompatible processes in a
    multi-station processing chamber*, US 6,319,553 B1, filed
    2000-02-28, granted 2001-11-20.
    <https://patents.google.com/patent/US6319553B1/en>
[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*.
    <https://en.wikipedia.org/wiki/Nitrogen_trifluoride>
[^shioya-1987]: Y. Shioya, K. Ikegami, M. Maeda and K. Yanagida,
    "High-temperature stress measurement on chemical-vapor-deposited
    tungsten silicide and tungsten films", *Journal of Applied Physics*
    **61**(2), 561–566 (1987). <https://doi.org/10.1063/1.338259>
[^novellus-wcvd-2002]: Novellus Systems, *Tungsten Product Solutions*
    (metal CVD), product page; Wayback Machine capture of 2002-02-10.
    <https://web.archive.org/web/20020210183923/http://www.novellus.com:80/products/cvd.asp>
[^wiki-novellus]: Wikipedia, *Novellus Systems*.
    <https://en.wikipedia.org/wiki/Novellus_Systems>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^ireland-1997]: P. J. Ireland, "High aspect ratio contacts: A review of
    the current tungsten plug process", *Thin Solid Films* **304**(1–2),
    1–12 (1997). <https://doi.org/10.1016/S0040-6090(96)09557-0>
