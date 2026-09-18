(machine-hdp-cvd)=
# HDP-CVD

A high-density-plasma CVD system is the single-wafer oxide deposition
tool a fab uses to fill narrow gaps: the isolation trenches of the front
end, the spaces between capped gates and the spaces between metal lines.
An inductively coupled source makes a dense, low-pressure plasma of
silane, oxygen and argon, and an RF bias on the wafer drives argon ions
into the growing film, so that the oxide is sputtered off the corners of
a gap while it grows, and the gap fills from the bottom before its mouth
can close. This page describes the class in general, lists
representative 200 mm-era models, and then says what SkyWater has
published about its own tool of this class and which SKY130 steps this
reference assigns to it. The growth regimes and gap-fill physics are
summarised on the {ref}`category page <category-deposition>`; the
capacitive plasma reactors that share the inter-level oxide steps are on
the {ref}`PECVD page <machine-pecvd>`.

| | HDP-CVD |
|---|---|
| What it does | Fills high-aspect-ratio gaps with oxide: "High-density plasma (HDP) CVD provides void-free gap fill of high-quality dielectric films in high aspect ratio device structures";[^novellus-hdp-2001] HDP processes use "oxygen, silane, and inert gases, such as argon, to achieve simultaneous dielectric etching and deposition".[^pat-hdp-novellus] |
| Plasma source | Inductive, with a separate wafer bias: Novellus's "hemispherically shaped induction coil" driven at "about 450 KHz", with "A high frequency rf source" that "independently adjusts the bias voltage on the wafer";[^pat-icp-novellus] Applied's "dual RF zone inductively coupled plasma source".[^pat-hdp-reactor-amat] |
| Pressure | "about 0.1-100 mTorr" for Novellus's induction source;[^pat-icp-novellus] "several (two to three) orders of magnitude lower than that of their PECVD counterparts".[^pat-hdp-novellus] |
| Gap fill | "aspect ratios of about 3:1" at "about 0.25 µm" spacing in 1998;[^pat-hdp-novellus] Applied's STI oxide "down to 0.12-micron, 4:1-aspect-ratio spaces";[^amat-hdp-sti-2002] a 0.13 µm STI "of space width 0.13 µm and aspect ratio 3.9" in a published process study.[^nishimura-2002] |
| Wafer temperature | Held on an electrostatic chuck: "a dual helium cooling zone electrostatic chuck to provide and maintain uniform wafer temperature during processing";[^pat-hdp-reactor-amat] HDP PSG deposited "at a temperature ⩽550°C" in Hsiao et al.'s study.[^hsiao-2005] |
| 200 mm era | Novellus SPEED, which "captured the heart of the marketplace in 1996",[^novellus-hdp-2001] Applied's Ultima HDP-CVD Centura, announced in 1996 as "the industry's first production-ready HDP-CVD system for multiple processes and applications",[^amat-1997] and Lam Research's "Deep Sub Micron (DSM) 9900 CVD tool".[^roche-1996] |
| SkyWater-listed tool | "Lam/Novellus High Density Plasma (HDP) doped and phos doped with sputter etch" ("high aspect (5:1) fill capability")[^skw-01]; a caption naming "a Novellus high density plasma tool"[^skw-07] |
| SKY130 steps | 7 steps; see {ref}`SKY130 steps assigned to this class <machine-hdp-cvd-steps>` |

## What the machine class is and how it works

A film that grows fastest at the upper corners of a gap closes the gap
over a void (category page). HDP-CVD changes two things. The source makes a much denser plasma at much lower
pressure, so that deposition precursors and ions arrive more
directionally; and the wafer is biased, so that ions sputter the film as
it grows. A Novellus and IBM patent describes the result: "RF bias is
applied to a wafer substrate", ions "accelerate toward the wafer surface
when the RF bias is applied", and "dielectric material deposited on the
wafer surface is simultaneously sputter-etched to help keep gaps open
during the deposition process, which allows higher aspect ratio gaps to
be filled".[^pat-hdp-novellus] What makes a machine an HDP-CVD tool is
the combination: a high-density source, an independently powered wafer
bias, a temperature-controlled chuck, and a clean and
seasoning cycle that keeps a hot plasma chamber from contaminating the
film. Nguyen's review sets out the process, its uses for "interlevel
insulation, gap filling, and planarization", and its
"metal-contamination and process-integration concerns".[^nguyen-1999]

### Inductive sources and wafer bias

Inductive coupling reaches densities a capacitive discharge cannot.
Hopwood's review of inductively coupled plasmas reports ion densities
above 10¹² cm⁻³ at sub-millitorr pressures from RF at 0.5–28 MHz;[^hopwood-1992]
Wikipedia contrasts a fractional ionisation of about 10⁻⁴ "in typical
capacitive discharges" with "as high as 5–10% in high-density inductive
plasmas".[^wiki-pecvd] Novellus's induction-source patent, filed in
1992, has "a hemispherically shaped induction coil in an expanding spiral
pattern"
following "a hemispherically shaped quartz bell jar, which holds the
vacuum", a low-frequency source power and a separate high-frequency
bias;[^pat-icp-novellus] its description adds that "When used with
careful substrate bias control, the induction system for PECVD is
suitable for dielectric gap filling".[^pat-icp-novellus] Novellus's
product page describes SPEED's "patented hemispherical source" as having
"a single excitation frequency and a single coil".[^novellus-hdp-2001]

Applied Materials' HDP-CVD reactor patent, filed in 1996, uses two coils
instead: "a dual RF zone inductively coupled plasma source configuration
capable of producing radially tunable ion currents across the wafer", "a
dual zone gas distribution system", "temperature controlled surfaces",
"a symmetrically shaped turbomolecular pumped chamber body", "a dual
helium cooling zone electrostatic chuck", "an all ceramic/aluminum alloy
chamber construction" and "a remote fluorine based plasma chamber
cleaning system".[^pat-hdp-reactor-amat] The dielectric dome is
temperature controlled because "Control of the dome temperature to
within ±10° K improves deposition adhesion and has been found to reduce
flake or particle counts in the chamber".[^pat-hdp-reactor-amat]

### Deposition, sputtering and the gap

The balance between deposition and sputtering is the central recipe
parameter. Before HDP, gap-fill processes alternated PECVD deposition
and argon sputter etching in separate steps;[^pat-hdp-novellus] Schwartz and Johns found that, as the gap
aspect ratio rose, such cycles left a fast-etching region in the gap and
then "physical voids",[^schwartz-1992] and the Novellus–IBM patent
reports that the gap fill of low-pressure, atmospheric-pressure and
plasma-enhanced CVD does "not extend beyond aspect ratios of 1.3:1 at
spacing 0.45 µm" even with "dep-etch-dep" cycles, while HDP processes
"are currently used to fill gaps having aspect ratios of about 3:1".[^pat-hdp-novellus] The same patent
then splits an HDP fill into steps: one with an etch-to-deposition ratio
below one "to quickly fill the gap", interrupted "before the opening to
the gap is closed", and one with a ratio above one "to widen the
gap".[^pat-hdp-novellus] Nishimura et al. found that "film deposition
under an increased plasma power and low-pressure conditions is effective
for stable gap filling", and that "the angular dependence of sputter
yield and the ionic deposition mechanism are important
factors".[^nishimura-2002] Novellus, in 2009, still described fill as
"tailoring the deposition, etch, and sputter-to-deposition (S/D) ratio",
and warned that "Too many deposition/etch cycles, or inadequate control
of process uniformity, will result in excessive clipping or voids within
the trenches".[^lam-speed] Sputtering the trench walls need not damage
them: Lee et al. found "negligible sputter effect of HDP even with low
deposition/sputter (D/S) ratio on the trench sidewall
surface".[^lee-1998-sti]

### Heat and the electrostatic chuck

The wafer is clamped electrostatically and cooled with helium on its
back. Applied
specifies "a dual helium cooling zone electrostatic chuck";[^pat-hdp-reactor-amat]
Novellus's 300 mm SPEED pairs its source with a "bi-polar electrostatic
chuck" for "superior ion uniformity and temperature
control".[^novellus-hdp-2001] The wafer
temperature a recipe reaches depends on the film: Applied's Ultima offered
"high-temperature USG" for STI and "low-temperature USG" for IMD and
passivation,[^amat-hdp-sti-2002][^amat-hdp-imd-2002] and Hsiao et al.
deposited HDP PSG "at a temperature ⩽550°C".[^hsiao-2005]

### Doped and fluorinated films

The same chamber deposits undoped silicate glass (USG), phosphosilicate
glass (PSG) and fluorinated glass (FSG): Applied's Ultima "can deposit
both undoped and doped films for numerous processes including USG, FSG,
PSG, SiN and low k films".[^amat-hdp-2001] For PSG at the pre-metal
level, Applied claimed that "the films provide ion-gettering properties
as well as device isolation";[^amat-hdp-psg-2002] Vassiliev reports the
properties and gap-fill capability of HDP PSG for sub-quarter-micron
devices,[^vassiliev-1999] and Hsiao et al. found "residual inactive
phosphorous and compounds with PO bonds" in as-deposited HDP PSG, some of
which "became active after the thermal annealing".[^hsiao-2005] FSG
lowers the permittivity: in Denison et al.'s high-density-plasma films
"The dielectric constant decreased linearly from 4.0 at zero F to 3.55 at
10.5 at. % F".[^denison-1996] Applied introduced its Ultima with FSG
"for emerging low dielectric constant (low k)
applications".[^amat-1997]

### Cleaning, seasoning and contamination

An HDP chamber is cleaned with fluorine and must then be conditioned
before it deposits on product. Applied's Ultima introduced "the
industry's first Remote Plasma Clean technology that virtually eliminates
'global warming' emissions from the CVD chamber cleaning
process".[^amat-1997] A Novellus patent for an HDP system with a
hemispherical coil notes that "Following the clean cycle, a fluorine
residue remains on the walls and other surfaces of the reaction chamber",
which "must be removed for safety reasons and to insure that the film
adheres", and adds a dedicated clean-gas injector.[^pat-hdp-clean-novellus]
An Applied patent describes contamination from the chamber itself:
"sodium is a particularly disruptive contaminant", believed to diffuse
"through the quartz dome and alumina nozzles", and "a known method" of
controlling it "involves depositing a 'seasoning' layer of silicon oxide
over the chamber's interior surface prior to processing substrate
films".[^pat-seasoning-amat] Novellus's later SPEED Max has "an
enlarged remote plasma source" that "allows more wafers to be processed
between plasma cleans".[^lam-speed]

### Plasma charging

A dense plasma over metal lines tied to gates can charge the gate
oxide. Hwang and Giapis's simulations show that "the initial conformality
of the ILD film plays a crucial role in metal line charging and the
subsequent degradation of the buried gate oxide", and that charging "can
be reduced by depositing a more conformal ILD film around the metal line
and/or by increasing the film surface conductivity".[^hwang-1998] Roche
and McVittie measured the plasma-induced voltage in real time with a
probe "installed on a Deep Sub Micron (DSM) 9900 CVD tool from Lam
Research Corporation" and mapped a low-voltage process
window.[^roche-1996] For HDP PSG over transistors, Chen et al. note that
the process "has the plasma damage concern which can impact the device
performance or reliability".[^chen-2002-psg]

## Representative 200 mm-era models

* **Novellus Systems.** SPEED, which the company history dates to 1995
  as "a high-density plasma system with simpler, more cost-effective
  solutions for inter-metal dielectric films";[^novellus-history]
  Novellus's own page says it "captured the heart of the marketplace in
  1996" and "was the first-and-only-tool to successfully integrate HDP
  processing in high-volume production environments". The same page
  lists the Concept Two SPEED/SEQUEL, which "combines two SPEED HDP
  chambers with one SEQUEL chamber", and the 300 mm Concept Three
  SPEED.[^novellus-hdp-2001] Novellus's 2009 release on the SPEED Max
  says the system "extends the HDP-CVD application into the 45 and 32 nm
  technology nodes".[^lam-speed]
* **Applied Materials.** A first-generation HDP system in February 1996
  and the Ultima HDP-CVD Centura later that year;[^amat-1997] "Up to three
  Ultima chambers, or various combinations of Ultima and PECVD chambers,
  can be fitted onto the production-proven Centura platform", and the
  Ultima X followed "for both 200mm and 300mm advanced STI, IMD and PMD
  applications".[^amat-hdp-2001]
* **Lam Research.** The DSM 9900 CVD tool on which Roche and McVittie
  installed their charging probe.[^roche-1996]
* **Not HDP: the Trikon Planar 200.** The {ref}`FILOX <step-011>`,
  {ref}`PSG <step-089>`, {ref}`NILD3 <step-115>` and {ref}`NILD4 <step-126>`
  pages mention the Trikon Planar 200 to set it apart from HDP tools. Trikon's annual report for 1996
  describes the Planar 200 Flowfill as a "multi-chambered cluster
  system" in which "The plasma CVD films are deposited in one module and
  the CVD planarizing flow layer is deposited in the Flowfill(TM)
  module", and sets it against HDP gap fill as an alternative for
  inter-metal dielectrics;[^trikon-10k-1996] it is therefore not an
  HDP-CVD system.

## At SkyWater

### What SkyWater lists

Under "Film Deposition", SkyWater's *Facilities & Capabilities* page
lists one HDP entry with one sub-entry:[^skw-01]

> "Lam/Novellus High Density Plasma (HDP) doped and phos doped with
> sputter etch"
>
> "– high aspect (5:1) fill capability"

Read term by term: an HDP process that deposits "doped" and "phos doped"
films, "with sputter etch", with a stated fill capability of 5:1. The
entry does not say what "doped" means beside "phos doped", does not name
an undoped or fluorinated film, and gives no model, temperature or
thickness. We read "with sputter etch" as the in-situ sputtering that
defines the class, not as a separate etch tool; the page does not
explain it.[^skw-01] SkyWater's maintenance-technician profile
separately has a photo caption in which a technician and an engineer
"recover a robot fault on a Novellus high density plasma
tool".[^skw-07]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>` the
listing is **strong**: the capabilities page and the maintenance profile
are two SkyWater statements, and the profile names the vendor as
Novellus.[^skw-01][^skw-07] Neither names a model or a step, so the
reading of the tool as a SPEED-class system rests on Novellus's product
history,[^novellus-history] and the step assignments are graded on the
step pages. "Lam/Novellus" fits a Novellus tool after Novellus became
part of Lam in 2012;[^wiki-novellus] Lam also sold an HDP CVD tool of
its own in the 1990s,[^roche-1996] and the page does not say which is
meant (our reading). The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.

(machine-hdp-cvd-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names an HDP-CVD system as
the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`FILOX <step-011>`, {ref}`PSG <step-089>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Lam/Novellus High Density Plasma (HDP) doped and phos doped with sputter etch"** — *strong (two SkyWater statements):* {ref}`FILOX <step-011>`; *inference:* {ref}`PSG <step-089>`, {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`, {ref}`NILD6 <step-156>`
* **The PECVD entries instead** — "PECVD TEOS, C2 and Producer":
  *medium (as the whole film):* {ref}`NILD2 <step-105>`; *medium (as the
  liner or overburden):* {ref}`NILD3 <step-115>`,
  {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`,
  {ref}`NILD6 <step-156>`; *weak:* {ref}`PSG <step-089>`. "PECVD silane
  oxide/nitride/oxynitride, C1", "PECVD nitride C1": *weak:*
  {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`,
  {ref}`NILD4 <step-126>`, {ref}`NILD5 <step-141>`,
  {ref}`NILD6 <step-156>`. The full grade lists are on the
  {ref}`PECVD page <machine-pecvd>`.
* **The furnace entry for densification** — "Furnaces are all made by
  Aviza": *strong for existence (batch alternative):*
  {ref}`FILOX <step-011>`; see the
  {ref}`anneal furnace page <machine-vertical-furnace-anneal>`.

Only {ref}`FILOX <step-011>` is graded above an inference, because its
page counts the capabilities entry and the profile caption as two
SkyWater statements for the tool. For the pre-metal glass the
inference rests on the PDK's "PSG" label[^pdk-04] and on "phos doped"
being the only phosphorus-doped oxide in the list; for the inter-level
oxides it rests on the gap geometry, and the pages note that the entry
names only doped films.[^skw-01]

## Consumables and facilities

The precursors, dopant sources, chamber-clean gases and process gases
are described on the {ref}`precursors <material-precursors>`,
{ref}`dopant gases and implant sources <material-dopant-sources>`,
{ref}`etch and chamber-clean gases <material-etch-gases>` and
{ref}`process gases <material-process-gases>` pages.
The process gases are listed in the {ref}`materials index
<materials-index>`; what is specific to an HDP-CVD tool is summarised
here. None of the SkyWater sources describes the fab's gas delivery,
pumps or abatement. Chamber parts and exhaust abatement are described on
the
{ref}`hardware consumables and abatement <material-hardware-consumables>`
page.

* **Process gases.** Silane, oxygen and argon;[^pat-hdp-novellus]
  a phosphorus precursor for PSG[^hsiao-2005] (typically phosphine,
  which is "used as a dopant in the semiconductor industry" and is "a
  highly toxic respiratory poison";[^wiki-ph3] Hsiao et al.'s abstract does
  not name the precursor);
  SiF₄ for FSG where it is used.[^denison-1996]
* **Clean and seasoning.** Fluorine clean gases through a remote plasma
  source or dedicated injectors, followed by a seasoning
  oxide;[^pat-hdp-reactor-amat][^pat-hdp-clean-novellus][^pat-seasoning-amat]
  NF₃, the usual PECVD clean gas, has "a global warming potential (GWP)
  17,200 times greater than that of CO2" over 100 years (an IPCC Fourth
  Assessment Report, AR4, value).[^wiki-nf3]
* **Chamber parts.** Quartz or ceramic domes and alumina gas nozzles,
  which the seasoning patent names as sources of sodium;[^pat-seasoning-amat]
  the dome's heater and cold plates.[^pat-hdp-reactor-amat]
* **Chuck and cooling.** An electrostatic chuck with helium backside
  cooling,[^pat-hdp-reactor-amat] and the turbomolecular pumping that
  holds millitorr pressures at high gas flows.[^pat-hdp-reactor-amat]
* **Monitor wafers.** Blanket wafers for {ref}`thickness <machine-film-thickness-metrology>`,
  uniformity and {ref}`particles <machine-defect-inspection>`, and patterned wafers
  {ref}`cross-sectioned <machine-cross-section-sem-profilers>` for voids, as the step
  pages' industry-generic outlines describe ({ref}`FILOX <step-011>`, {ref}`NILD3 <step-115>`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's deposition recipes and
thicknesses are not public.

* **Trench fill.** The {ref}`FILOX <step-011>` page fills the lined
  isolation trenches with HDP oxide, which the PDK labels "FOX
  K=3.9";[^pdk-04] published 0.13 µm STI work filled "space width
  0.13 µm and aspect ratio 3.9",[^nishimura-2002] inside the listed
  "high aspect (5:1) fill capability".[^skw-01] The film is then
  polished to the nitride ({ref}`CMPNIT <step-012>`), and the FILOX page
  names a furnace or RTP densification as optional.
* **Glass over the gates.** The {ref}`PSG <step-089>` page describes a
  gap between spacer-clad gates whose aspect ratio is well above 2 : 1
  and reads the
  pre-metal glass as HDP PSG; HDP PSG over finished transistors carries
  "the plasma damage concern",[^chen-2002-psg] and its phosphorus
  activation depends on the later thermal budget.[^hsiao-2005]
* **Oxide between metal lines.** The inter-level oxide pages derive gaps
  of about 1:1 over local interconnect ({ref}`NILD2 <step-105>`) and
  about 2.6:1 and 2.8:1 between metal lines
  ({ref}`NILD3 <step-115>`, {ref}`NILD6 <step-156>`) from the PDK
  geometry, all below the listed 5:1.[^skw-01] Above metal 1 the
  wafer carries aluminium; the {ref}`NILD3 <step-115>` page's
  industry-generic outline puts a PECVD liner under the HDP fill, and
  HDP tools hold the wafer temperature with a helium-cooled
  chuck.[^pat-hdp-reactor-amat]
* **A lower-permittivity layer.** The PDK's stack diagram draws a thin
  "NILD3_C K=3.5" beside "NILD3 K=4.5";[^pdk-04] the
  {ref}`NILD3 <step-115>` page notes that 3.5 is the permittivity of a
  fluorinated oxide[^denison-1996] and leaves open what the layer is.
  SkyWater's entry names no FSG.[^skw-01]
* **Charging over metal.** Each inter-level oxide is deposited over
  lines connected to gates; the step pages cite the charging studies
  above,[^hwang-1998][^roche-1996] and the SKY130 antenna rules address
  plasma charging ({ref}`category-etch`).

## Related pages

* {ref}`category-deposition` — HDP-CVD gap fill and the deposition steps
  of SKY130.
* {ref}`machine-pecvd` — the capacitive PECVD tools that share the
  inter-level oxide steps.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`materials-index` — silane, phosphine and the clean gases.
* {ref}`category-cmp` — the polishes that planarise the fill oxides.
* {ref}`material-hardware-consumables` — chamber parts and exhaust
  abatement.
* {ref}`material-precursors` — silane, dichlorosilane, TEOS, BTBAS,
  ammonia, SiF₄, ozone and WF₆.
* {ref}`material-dopant-sources` — dopant gases, solid sources,
  sub-atmospheric packages and ion-source parts.
* {ref}`material-etch-gases` — fluorocarbon, fluoride, chlorine and
  bromine etch and chamber-clean gases.
* {ref}`material-process-gases` — nitrogen, oxygen, hydrogen, argon,
  helium and the oxidation additives, their grades and SkyWater's listed
  gases.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the HDP entry and
  its fill capability.[^skw-01]
* SkyWater Technology, *A Day in the Life of a SkyWater Maintenance
  Technician* — the caption naming a Novellus high density plasma
  tool.[^skw-07]
* Novellus Systems, *Dielectric – HDP Solutions* (2001 capture) — SPEED,
  SPEED/SEQUEL and the hemispherical source.[^novellus-hdp-2001]
* Applied Materials, *HDP-CVD* product page (2001) — the Ultima on the
  Centura platform and its films.[^amat-hdp-2001]
* Applied Materials, Ultima film pages (2002) — HDP PSG, IMD USG and STI
  USG.[^amat-hdp-psg-2002][^amat-hdp-imd-2002][^amat-hdp-sti-2002]
* Applied Materials, *1997 Annual Report* — the first HDP system, the
  Ultima and its remote plasma clean.[^amat-1997]
* Novellus Systems, SPEED Max press release (2009) — the
  sputter-to-deposition ratio and the remote plasma source.[^lam-speed]
* Benzing, Broadbent and Rough (Novellus), US 5,346,578 — the
  hemispherical induction source.[^pat-icp-novellus]
* Redeker et al. (Applied Materials), US 6,170,428 — an HDP-CVD reactor
  with dual coils, helium-cooled chuck and remote clean.[^pat-hdp-reactor-amat]
* Papasouliotis et al. (Novellus and IBM), US 6,030,881 — HDP gap fill
  with varying etch-to-deposition ratios.[^pat-hdp-novellus]
* SkyWater PDK Authors, `metal_stack.svg` — the FOX, PSG and NILD
  dielectrics.[^pdk-04]
* Trikon Technologies, Form 10-K for 1996 — the Planar 200 Flowfill
  system, set against HDP gap fill.[^trikon-10k-1996]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition* — capacitive
  and inductive discharges.[^wiki-pecvd]
* Wikipedia, *Phosphine* and *Nitrogen trifluoride* — the dopant and
  clean gases.[^wiki-ph3][^wiki-nf3]
* Wikipedia, *Novellus Systems* — the vendor and its acquisition by
  Lam.[^wiki-novellus]
* Encyclopedia.com, *Novellus Systems, Inc.* — the introduction of
  SPEED.[^novellus-history]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — CVD and
  back-end dielectrics.[^txt-01]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — HDP-CVD among the deposition chapters.[^txt-09]

### Deep dive

* Nguyen, *IBM J. Res. Dev.* 1999 — a review of HDP-CVD dielectrics and
  gap fill.[^nguyen-1999]
* Hopwood, *Plasma Sources Sci. Technol.* 1992 — a review of inductively
  coupled plasma sources.[^hopwood-1992]
* Schwartz and Johns, *J. Electrochem. Soc.* 1992 — gap fill by PECVD
  deposition and sputter-etch cycles.[^schwartz-1992]
* Nishimura et al., *JJAP* 2002 — HDP-CVD gap fill for 0.13 µm STI and
  its topography model.[^nishimura-2002]
* Lee et al., *JJAP* 1998 — STI characteristics with HDP-CVD fill oxide
  and the D/S ratio.[^lee-1998-sti]
* Vassiliev, *Electrochem. Solid-State Lett.* 1999 — properties and gap
  fill of HDP PSG.[^vassiliev-1999]
* Hsiao, Liu and Wang, *JVST B* 2005 — thermal budget and phosphorus
  bonding in HDP PSG.[^hsiao-2005]
* Denison, Barbour and Burkhart, *JVST A* 1996 — fluorine-doped oxide
  from a high-density plasma.[^denison-1996]
* Hwang and Giapis, P2ID 1998 — charging during inter-level oxide
  deposition in HDP tools.[^hwang-1998]
* Roche and McVittie, P2ID 1996 — an in-situ charging probe on a
  production HDP CVD tool.[^roche-1996]
* Chen et al., P2ID 2002 — reducing plasma damage in HDP PSG.[^chen-2002-psg]
* Tan, Li and Zygmunt (Applied Materials), US 6,914,016 — a heated HDP
  fluorinated-oxide process for high-aspect-ratio gaps.[^pat-hdp-amat]
* Kilgore et al. (Novellus), US 6,200,412 — clean-gas injection and
  fluorine residue in an HDP chamber.[^pat-hdp-clean-novellus]
* Rossman et al. (Applied Materials), US 6,121,161 — seasoning films
  against sodium from the dome and nozzles.[^pat-seasoning-amat]

## Open questions

* What "doped" means beside "phos doped" in SkyWater's entry, and
  whether the tool deposits the undoped inter-level oxides, are not
  stated.[^skw-01]
* Whether SkyWater's HDP tool is a Novellus SPEED-class system, a Lam
  system or both, and how many chambers it has, are not public.
* Whether the inter-level oxides are HDP fills with PECVD liners and
  overburdens, and what the thin NILD3_C and NILD4_C layers are, are not
  public.
* The model list above is incomplete: it covers the Novellus, Applied
  Materials and Lam systems for which a public description was found,
  not the other HDP systems of the period.

<!-- footnotes -->

[^novellus-hdp-2001]: Novellus Systems, *Dielectric – HDP Solutions*,
    product page; Wayback Machine capture of 2001-12-02.
    <https://web.archive.org/web/20011202103556/http://www.novellus.com:80/products/hdp.asp>
[^pat-hdp-novellus]: G. D. Papasouliotis, A. B. Chakravarti, R. A. Conti,
    L. Economikos and P. A. Van Cleemput (Novellus Systems and
    International Business Machines), *High throughput chemical vapor
    deposition process capable of filling high aspect ratio structures*,
    US 6,030,881 A, filed 1998-05-05, granted 2000-02-29.
    <https://patents.google.com/patent/US6030881A/en>
[^pat-icp-novellus]: J. C. Benzing, E. K. Broadbent and J. K. H. Rough
    (Novellus Systems), *Induction plasma source*, US 5,346,578 A, filed
    1992-11-04, granted 1994-09-13.
    <https://patents.google.com/patent/US5346578A/en>
[^pat-hdp-reactor-amat]: F. C. Redeker, F. Moghadam, H. Hanawa,
    T. Ishikawa, D. Maydan, S. Li, B. Lue, R. J. Steger, M. Wong, Y. Wong
    and A. K. Sinha (Applied Materials), *Symmetric tunable inductively
    coupled HDP-CVD reactor*, US 6,170,428 B1, filed 1996-07-15, granted
    2001-01-09. <https://patents.google.com/patent/US6170428B1/en>
[^amat-hdp-sti-2002]: Applied Materials, *Ultima HDP-CVD (USG) STI*,
    product page; Wayback Machine capture of 2002-08-09.
    <https://web.archive.org/web/20020809163834/http://www.appliedmaterials.com:80/products/hdp_cvd_usg_sti.html>
[^nishimura-2002]: H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
    "Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
    Technologies", *Japanese Journal of Applied Physics* **41**, Part 1,
    No. 5A, 2886–2893 (2002). <https://doi.org/10.1143/JJAP.41.2886>
[^hsiao-2005]: W.-C. Hsiao, C.-P. Liu and Y.-L. Wang, "Influence of
    thermal budget on phosphosilicate glass prepared by high-density
    plasma chemical-vapor deposition", *Journal of Vacuum Science &
    Technology B* **23**(5), 2146–2150 (2005).
    <https://doi.org/10.1116/1.2050670>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^roche-1996]: G. A. Roche and J. P. McVittie, "Application of Plasma
    Charging Probe to Production HDP CVD Tool", *Proc. 1st International
    Symposium on Plasma Process-Induced Damage (P2ID 1996)*, pp. 71–74.
    <https://doi.org/10.1109/PPID.1996.715205>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; film deposition entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^skw-07]: SkyWater Technology, *A Day in the Life of a SkyWater
    Maintenance Technician*, 2023-12-14; caption re-checked 2026-09-13.
    <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^hopwood-1992]: J. Hopwood, "Review of inductively coupled plasmas for
    plasma processing", *Plasma Sources Science and Technology* **1**(2),
    109–116 (1992). <https://doi.org/10.1088/0963-0252/1/2/006>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^schwartz-1992]: G. C. Schwartz and P. Johns, "Gap-Fill with PECVD SiO₂
    Using Deposition/Sputter Etch Cycles", *Journal of The
    Electrochemical Society* **139**(3), 927–932 (1992).
    <https://doi.org/10.1149/1.2069327>
[^lam-speed]: Novellus Systems (Lam Research newsroom), *Novellus' SPEED
    Max HDP-CVD Dielectric Gapfill System Extends STI Application to
    32nm*, press release, 2009-10-05.
    <https://newsroom.lamresearch.com/2009-10-05-NOVELLUS-SPEED-R-MAX-HDP-CVD-DIELECTRIC-GAPFILL-SYSTEM-EXTENDS-STI-APPLICATION-TO-32nm>
[^lee-1998-sti]: S.-H. Lee, J.-H. Son, H.-D. Lee, W. Yang and Y.-J. Lee,
    "Shallow Trench Isolation Characteristics with High-Density-Plasma
    Chemical Vapor Deposition Gap-Fill Oxide for Deep-Submicron CMOS
    Technologies", *Japanese Journal of Applied Physics* **37**(3S),
    1222 (1998). <https://doi.org/10.1143/JJAP.37.1222>
[^amat-hdp-imd-2002]: Applied Materials, *Ultima HDP-CVD (USG) IMD*,
    product page; Wayback Machine capture of 2002-08-09.
    <https://web.archive.org/web/20020809163156/http://www.appliedmaterials.com:80/products/hdp_cvd_usg_imd.html>
[^amat-hdp-2001]: Applied Materials, *HDP-CVD* (Ultima HDP-CVD Centura
    and Ultima X), product page; Wayback Machine capture of 2001-08-17.
    <https://web.archive.org/web/20010817112354/http://www.appliedmaterials.com:80/products/hdp_cvd.html>
[^amat-hdp-psg-2002]: Applied Materials, *Ultima HDP-CVD PSG*, product
    page; Wayback Machine capture of 2002-10-21.
    <https://web.archive.org/web/20021021022321/http://www.appliedmaterials.com:80/products/hdp_cvd_psg.html>
[^vassiliev-1999]: V. Y. Vassiliev, "Properties and Gap-Fill Capability
    of HPD-CVD Phosphosilicate Glass Films for Subquarter-Micrometer
    ULSI Device Technology", *Electrochemical and Solid-State Letters*
    **3**(2), 80 (1999). <https://doi.org/10.1149/1.1390964>
[^denison-1996]: D. R. Denison, J. C. Barbour and J. H. Burkhart, "Low
    dielectric constant, fluorine-doped SiO₂ for intermetal dielectric",
    *Journal of Vacuum Science & Technology A* **14**(3), 1124–1126
    (1996). <https://doi.org/10.1116/1.580280>
[^pat-hdp-clean-novellus]: M. D. Kilgore, W. G. M. van den Hoek,
    C. J. Rau, B. J. van Schravendijk, J. A. Tobin, T. W. Mountsier and
    J. C. Oswalt (Novellus Systems), *Chemical vapor deposition system
    including dedicated cleaning gas injection*, US 6,200,412 B1, filed
    1996-02-16, granted 2001-03-13.
    <https://patents.google.com/patent/US6200412B1/en>
[^pat-seasoning-amat]: K. Rossman, T. Sahin, H. M'Saad and R. Nowak
    (Applied Materials), *Reduction of mobile ion and metal contamination
    in HDP-CVD chambers using chamber seasoning film depositions*,
    US 6,121,161 A, filed 1999-01-19, granted 2000-09-19.
    <https://patents.google.com/patent/US6121161A/en>
[^hwang-1998]: G. S. Hwang and K. P. Giapis, "Mechanism of charging
    damage during interlevel oxide deposition in high-density plasma
    tools", *Proc. 1998 3rd International Symposium on Plasma
    Process-Induced Damage (P2ID)*, pp. 164–167.
    <https://doi.org/10.1109/PPID.1998.725600>
[^chen-2002-psg]: S. Chen, C.-Y. Fu, S.-M. Jang, C.-H. Yu and M.-S. Liang,
    "Plasma damage reduction for high density plasma CVD phosphosilicate
    glass process", *Proc. 7th International Symposium on Plasma- and
    Process-Induced Damage* (2002), pp. 76–79.
    <https://doi.org/10.1109/PPID.2002.1042613>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.* (company
    history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^wiki-novellus]: Wikipedia, *Novellus Systems*.
    <https://en.wikipedia.org/wiki/Novellus_Systems>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^wiki-ph3]: Wikipedia, *Phosphine*. <https://en.wikipedia.org/wiki/Phosphine>
[^wiki-nf3]: Wikipedia, *Nitrogen trifluoride*.
    <https://en.wikipedia.org/wiki/Nitrogen_trifluoride>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007, ISBN
    978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^pat-hdp-amat]: Z. Tan, D. Li and W. Zygmunt (Applied Materials),
    *HDP-CVD deposition process for filling high aspect ratio gaps*,
    US 6,914,016 B2, granted 2005-07-05.
    <https://patents.google.com/patent/US6914016B2/en>
[^trikon-10k-1996]: Trikon Technologies, Inc., *Annual Report on Form
    10-K for the fiscal year ended December 31, 1996*; copy on
    GetFilings.com, Wayback Machine capture of 2008-10-12.
    <http://web.archive.org/web/20081012193325/http://www.getfilings.com/o0000898430-97-001539.html>
