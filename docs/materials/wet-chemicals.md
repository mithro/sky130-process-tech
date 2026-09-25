(material-wet-chemicals)=
# Wet chemicals

Wet chemicals are the liquids a fab uses to clean, etch and strip
wafers: hydrofluoric acid and buffered oxide etch for oxides, the
hydrogen-peroxide cleans of the {term}`RCA clean <RCA clean>` family
and the sulphuric–peroxide mixture for particles, metals and organics,
hot phosphoric acid for silicon nitride, nitric–hydrofluoric mixtures
for silicon, isopropanol for drying, and amine solvents for the residues
that plasma etching leaves on metal. They are consumed in large volumes,
at high purity, in the wet benches, spray processors and single-wafer
spin tools of the fab. This page describes the class in general, lists
representative materials and the purity grades they are bought to, and
then says what SkyWater has published about wet chemicals at its fab
and which SKY130 steps name them. The chemistry of cleaning and wet
etching is on the {ref}`strip <category-strip>` and
{ref}`etch <category-etch>` category pages, and the tools are on the
{ref}`wet bench <machine-wet-bench>` and
{ref}`single-wafer spin processor <machine-single-wafer-spin-processor>`
pages.

| | Wet chemicals |
|---|---|
| What they do | Remove films and contaminants by dissolving them. Kern wrote in 1990 that cleaning chemistry "has remained essentially unchanged in the past 25 years and is based on hot alkaline and acidic hydrogen peroxide solutions".[^kern-1990] |
| Etchants | Hydrofluoric acid, of which "A common concentration is 49% (48–52%)";[^wiki-hf] buffered oxide etch, for example "6:1 volume ratio of 40% NH4F to 49% HF";[^wiki-boe] phosphoric acid, "commonly encountered as an 85% aqueous solution";[^wiki-h3po4] HF/HNO₃ for silicon.[^robbins-1959] |
| Cleans | SC-1 and SC-2 "at 75 or 80 °C";[^wiki-rca] SPM, "3 parts of concentrated sulfuric acid and 1 part of 30 wt. % hydrogen peroxide solution" as a typical mixture;[^wiki-piranha] ozonised water.[^hattori-1998] |
| Solvents | Isopropanol for drying;[^kern-1990] hydroxylamine–alkanolamine residue removers.[^pat-ekc-hydroxylamine] |
| Grades | SEMI specifications for hydrofluoric acid, buffered oxide etchants, hydrogen peroxide, sulphuric acid and 2-propanol, the last "typically required by semiconductor devices with geometries of 0.8 to 1.2 microns" at its VLSI grade, a grade defined for much larger geometries than 130 nm.[^semi-c28][^semi-c23][^semi-c30][^semi-c44][^semi-c41] |
| Hazards | HF causes "bone damage due to HF strongly interacting with calcium in bones";[^wiki-hf] mixing piranha "is an extremely exothermic process".[^wiki-piranha] |
| SkyWater evidence | "Sulfuric, SC1, phosphoric, BOE, spin or IPA dry"; "EKS265, EKC270 solvents"; "HF, DSP+HF, titration controlled"; "HF/SC1/SC2";[^skw-01] "high-purity acid, base, and cleaning solutions for various wet processing steps"[^sec-01][^sec-02] |
| SKY130 steps | 49 steps; see {ref}`SKY130 steps that use this class <material-wet-chemicals-steps>` |

## What the class is and what it does

A wet chemical removes material by dissolving it. Wet processing is
therefore isotropic and can be very selective, and it cleans without
the damage a plasma can do; its limits are the purity of the liquid,
which decides what it leaves behind, and the drying, which decides
whether the wafer stays clean. The cleaning solutions of a 1990s fab
descend from the peroxide solutions Kern and Puotinen published in
1970,[^kern-1970] and Kern's review of 1990 records that the chemistry
"has remained essentially unchanged in the past 25 years"; what had
changed "is its implementation with optimized equipment".[^kern-1990]
Kern's handbook chapter surveys the field.[^kern-handbook]

### Hydrofluoric acid and buffered oxide etch

Hydrofluoric acid dissolves silicon dioxide and stops on silicon.
Higashi et al. found that "Aqueous HF etching of silicon surfaces
results in the removal of the surface oxide and leaves behind silicon
surfaces terminated by atomic hydrogen",[^higashi-1990] the surface
that an HF-last clean ({term}`HF-last`) hands to the next step. That
surface does not stay bare: Morita et al. showed that "The coexistence
of oxygen and water or moisture is required for growth of native oxide
both in air and in ultrapure water at room
temperature".[^morita-1990] For slow, controlled etches the acid is
diluted with water or buffered with ammonium fluoride; "Buffering HF
with NH4F results in a solution with a more stable pH; thus, more
stable concentrations of HF and HF−2, and a more stable etch
rate".[^wiki-boe] In very dilute HF, Kikuyama et al. showed that
conductivity "can be used to monitor the etching rate … very accurately
when the etching rate is relatively slow (around 1 Å/min)".[^kikuyama-1994]
Surfactants are added for fine patterns: a Daikin patent describes an
etchant of "hydrogen fluoride, ammonium fluoride and a surfactant
selected from a group consisting of fluorine-containing carboxylic acids
and their salts, with which very minute and complicated pattern can be
etched",[^pat-bhf-daikin] and a Hashimoto Chemical patent with Ohmi
among its inventors describes a composition comprising "a mixture of hydrofluoric acid, ammonium fluoride
solution and water, and at least one compound selected from the group
of surfactants".[^pat-bhf-hashimoto]
HF also etches silicon nitride, at rates that differ from oxide;
Knotter and Denteneer proposed a mechanism by which the "etch
selectivity between these two materials can be
explained".[^knotter-2001] Metals dissolved in HF can plate onto the
silicon it exposes: in dilute HF, Norga et al. found that the reduction
of copper ions "occurs by capture of conduction band electrons" and
nucleates nanometre-sized precipitates on the surface.[^norga-1997]

### Peroxide cleans: SC-1, SC-2 and SPM

The RCA sequence uses hydrogen peroxide with a base and then with an
acid. SC-1, ammonia and peroxide in water, "removes organic residues",
and particles "are also very effectively removed, even insoluble
particles, since SC-1 modifies the surface and particle zeta potentials
and causes them to repel"; SC-2, hydrochloric acid and peroxide in
water, "effectively removes the remaining traces of metallic (ionic)
contaminants, some of which were introduced in the SC-1 cleaning
step".[^wiki-rca] Itano et al. showed that "alkaline solutions are
superior to acid solutions in terms of particle removal efficiency",
that the alkaline solutions "etch the wafer surfaces to lift off
particles", and that "an etch rate of 0.25 nm/min or more is required to
lift off the particles"; their results suggested an SC-1 mixing ratio
of "0.05:1:5" (NH₄OH, H₂O₂, H₂O),[^itano-1993] far less ammonia
than the 1:1:5 of Wikipedia's recipe (our comparison).[^wiki-rca] SPM, piranha, is sulphuric acid with peroxide; it
"is used frequently in the microelectronics industry, e.g. to clean
photoresist or organic material residue from silicon
wafers".[^wiki-piranha] Room-temperature sequences were developed to
cut the chemical load of the hot cleans: Ohmi's five-step clean reduced
chemical and ultrapure water use to "less than 1% and 5%,
respectively".[^ohmi-1996] Hydrogen peroxide itself "decomposes slowly
into water and elemental oxygen when exposed to light, and rapidly in
the presence of organic or reactive compounds".[^wiki-h2o2]

### Hot phosphoric acid and nitric–hydrofluoric mixtures

Silicon nitride is stripped in hot phosphoric acid, where water content
sets the selectivity: van Gelder and Hauser found that "An increase in
water content increases the etch rate of silicon nitride and decreases
the etch rate of silicon dioxide", and used "Refluxed boiling phosphoric
acid at 180°C", in which nitride etched at 100 Å/min against 0–25 Å/min
for deposited oxide.[^vgh-1967] A production bath is held there with "a
water concentration monitor and a water spiking
apparatus".[^liu-2007] Silicon itself is etched in mixtures of
hydrofluoric and nitric acid. Robbins and Schwartz mapped the etch rate
over the HF–HNO₃–H₂O composition triangle and found that "The reaction
proceeds by an oxidation step followed by the dissolution of the
oxide";[^robbins-1959] their later paper in the series is on etching
technology.[^schwartz-1976] "Most commercially available nitric
acid has a concentration of 68% in water".[^wiki-hno3]

### Ozonised water

Ozone dissolved in water oxidises organics and silicon at room
temperature. Hattori et al. built a single-wafer spin clean "while
alternately supplying ozonized water and dilute HF for only 10 s each
onto a rotating silicon wafer", which "can efficiently remove both
particulate and metallic contaminants as well as organic
contaminants".[^hattori-1998] Gas-phase ozone, used with TEOS in
deposition, is indexed as a precursor, not here.

### Solvents: isopropanol and post-etch residue removers

Isopropanol displaces water in drying. Kern recorded in 1990 that
"Improvements in wafer drying by use of isopropanol vapor" were being
investigated,[^kern-1990] and Leenaars, Huethorst and van Oekel
published Marangoni drying the same year as "A new extremely clean
drying process".[^leenaars-1990] Where acids would attack exposed metal,
residues after etching are removed with amine solvents. An EKC
Technology patent describes "A stripping and cleaning composition for
removing resists and etching residue from substrates containing
hydroxylamine and at least one alkanolamine".[^pat-ekc-hydroxylamine]
Such solvents are not inert to every metal: Chen et al. measured
tungsten films in EKC265 at 65 °C and found that "the basic EKC265
solution was aggressive to tungsten", and that water and chloride
increased the corrosion further.[^chen-2003-ekc] Solvent formulations
are also studied for implanted resist: Visintin, Korzenski and Baum
stripped high-dose arsenic-implanted resist and its "hardened
carbonized crust without silicon/oxide loss" with organosilane
formulations.[^visintin-2006]

## Representative materials and grades

Chemicals for wafer processing are bought to purity grades that limit
metals, anions and particles. Wikipedia's account of the RCA clean
recommends "that the chemicals used be of electronic grade (or 'CMOS
grade') to avoid impurities that will recontaminate the
wafer",[^wiki-rca] and SEMI publishes a specification for each major
process chemical. The concentrations below are those of the chemicals
as supplied or of textbook mixtures; SKY130's concentrations and
temperatures are not public.

* **Hydrofluoric acid.** Supplied at "49% (48–52%)" and
  diluted at the point of use;[^wiki-hf] SEMI C28 standardises
  "requirements for hydrofluoric acid used in the semiconductor
  industry".[^semi-c28]
* **Buffered oxide etch.** A mixture of 40 % NH₄F and 49 % HF, 6:1 by
  volume in Wikipedia's example, which etches thermal oxide "at
  approximately 2 nanometres per second at 25 degrees
  Celsius";[^wiki-boe] SEMI C23 covers "grades of buffered oxide
  etchants used in the semiconductor industry".[^semi-c23]
  Surfactant-bearing buffered etchants are described in patents such as
  Hashimoto's and Daikin's.[^pat-bhf-hashimoto][^pat-bhf-daikin]
* **Hydrogen peroxide.** 30 % in the RCA and piranha
  recipes;[^wiki-rca][^wiki-piranha] SEMI C30 covers "five Grades and
  one Tier of hydrogen peroxide used in the semiconductor
  industry".[^semi-c30] It "is typically stored with a stabilizer in a
  weakly acidic solution in an opaque bottle".[^wiki-h2o2]
* **Ammonium hydroxide and hydrochloric acid.** "ammonia water, (29% by
  weight of NH3)" for SC-1 and "aqueous HCl (hydrochloric acid, 37% by
  weight)" for SC-2 in Wikipedia's recipes.[^wiki-rca]
* **Sulphuric acid.** SEMI C44 covers "two Grades and three Tiers of
  sulfuric acid used in the semiconductor industry".[^semi-c44] "When
  sulfuric acid is added to water, a considerable amount of heat is
  released".[^wiki-h2so4]
* **Phosphoric acid.** "commonly encountered as an 85% aqueous
  solution"; "Fractional crystallization can achieve higher purities
  typically used for semiconductor applications".[^wiki-h3po4]
* **Nitric acid.** Commercially 68 % in water.[^wiki-hno3]
* **Isopropanol (2-propanol).** SEMI C41 "covers all grades of
  2-propanol used in the semiconductor industry", and "The VLSI grade
  purity level is typically required by semiconductor devices with
  geometries of 0.8 to 1.2 microns", a grade defined for much larger
  geometries than 130 nm; the listing describes no other
  grade.[^semi-c41] It "is a colorless,
  flammable, organic compound".[^wiki-ipa]
* **Post-etch residue removers.** Proprietary solvent blends; the step
  pages write them as the EKC265/EKC270 class, and EKC Technology's
  patent gives the hydroxylamine–alkanolamine
  chemistry.[^pat-ekc-hydroxylamine] Chen et al. studied
  EKC265.[^chen-2003-ekc]

## At SkyWater

### What SkyWater's filings and pages list

SkyWater's *Facilities & Capabilities* page names wet chemistries on its
wet tools. Under "Resist removal/cleans":[^skw-01]

> "Akrion Gamma Batch Wet Bench – Sulfuric, SC1, phosphoric, BOE, spin
> or IPA dry"
>
> "Batch Rotational – EKS265, EKC270 solvents, CO2 injected DI"
>
> "Single Wafer – SEZ223, Davinci, HF, DSP+HF, titration controlled"

and under "Pre-cleaning":[^skw-01]

> "DNS wet bench industry standard HF/SC1/SC2"
> "dilute HF-last with IPA dry"
> "FSI Mercury industry standard HF/SC1/SC2 rotational"

The CMP entry adds "IPA clean".[^skw-01] Read term by term, the page
names sulphuric acid, SC-1, SC-2, phosphoric acid, BOE, HF (including a
dilute HF-last clean), isopropanol and two solvents; it does not expand
"DSP+HF" or say what "titration controlled" measures, and it names no
nitric acid, ozone or hydrogen peroxide. We read "Sulfuric" as the
sulphuric acid of an SPM bath, because SPM is how sulphuric acid is used
to strip resist;[^wiki-piranha] the page does not say so. SC-1 and
SC-2 contain hydrogen peroxide by definition.[^wiki-rca]

SkyWater's registration statement of 2021 and its annual report for
fiscal 2023 describe the raw materials as including "high-purity acid,
base, and cleaning solutions for various wet processing steps", and
name chemical suppliers:[^sec-01][^sec-02]

| Filing | Chemical suppliers as named |
|--------|-----------------------------|
| S-1 (2021)[^sec-01] | "Air Products & Chemicals, Inc. (bulk and specialty gases, chemicals)"; "KMG Chemicals, Inc. (chemicals)" |
| 10-K for fiscal 2023[^sec-02] | "EMD Performance Materials Corp (Versum) (specialty chemicals and gases)"; "CMC Chemicals, Inc. (a subsidiary of Entegris) (process and chemical mechanical polishing chemicals)" |

Neither filing says which chemicals each supplier provides. The S-1
also states: "We use, generate and discharge hazardous chemicals and
waste in our research and development and manufacturing
activities."[^sec-01]

### Strength of the evidence

The capability entries are SkyWater statements, so they are strong
evidence that the listed chemistries exist at the fab; on the scale of
the {ref}`machines index <machines-reading-evidence>` they rank as
**strong**. The same caveats apply as to the tools: the list describes
the whole fab in the 2020s, including processes that are not part of
SKY130, and it ties no chemical to a step.[^skw-01] The filings are
strong for the supplier names but weak for any particular chemical,
because they give only "chemicals" or "specialty chemicals" and changed
between 2021 and 2023.[^sec-01][^sec-02] Hydrogen peroxide is evidenced
only through SC-1 and SC-2; nitric acid and ozonated water are industry practice
that the step pages supply, not SkyWater statements.

(material-wet-chemicals-steps)=
### SKY130 steps that use this class

This page covers the rows of the {ref}`materials index <materials-table>`
listed below by key; the steps are those whose *Resources required* section
names one of them (the union of the rows' *Steps* cells). The post-CMP
clean mixtures, which also contain dilute HF, belong to the CMP
consumables row, and ultrapure water to its own row.

Materials index rows covered:

* `hf` — hydrofluoric acid
* `boe` — buffered oxide etch
* `sc1` — SC-1
* `sc2` — SC-2
* `spm` — SPM (piranha)
* `h3po4` — hot phosphoric acid
* `h2o2` — hydrogen peroxide
* `hno3` — nitric acid and titration reagents
* `ozonated-water` — ozonated water
* `ipa` — isopropanol
* `residue-removers` — post-etch residue removers

<!-- step-tables:begin (generated by tools/gen_step_tables.py; do not edit) -->
:::{dropdown} All 49 steps as one line of links (checked against the index)

Steps:

{ref}`SMAT <step-001>`, {ref}`BOX <step-002>`, {ref}`ISONIT <step-003>`, {ref}`STIE <step-006>`, {ref}`DNIS <step-009>`, {ref}`LINOX <step-010>`, {ref}`NS19 <step-013>`, {ref}`LVTNIS <step-016>`, {ref}`LVTPIS <step-021>`, {ref}`PCHIS <step-025>`, {ref}`PWIS <step-029>`, {ref}`PWDEIS <step-033>`, {ref}`TUNME <step-039>`, {ref}`ONOME <step-042>`, {ref}`GOX100 <step-043>`, {ref}`GOXETCH <step-046>`, {ref}`P1IS <step-051>`, {ref}`PRIS <step-054>`, {ref}`UPRIS <step-057>`, {ref}`BFR <step-060>`, {ref}`P1ME <step-062>`, {ref}`ASTIS <step-067>`, {ref}`HVASTIS <step-070>`, {ref}`LDASTIS <step-074>`, {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`, {ref}`PDIS <step-084>`, {ref}`NSDIS <step-087>`, {ref}`SACETCH <step-095>`, {ref}`WCMPLI <step-100>`, {ref}`LI1ME <step-103>`, {ref}`CTME <step-108>`, {ref}`WCMP2 <step-111>`, {ref}`MM1E <step-114>`, {ref}`VIME <step-119>`, {ref}`WCMP3 <step-122>`, {ref}`MM2E <step-125>`, {ref}`VIM2E <step-130>`, {ref}`WCMP4 <step-133>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`VIM3E <step-145>`, {ref}`WCMP5 <step-148>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`VIM4E <step-160>`, {ref}`MM5E <step-163>`, {ref}`NSME <step-166>`, {ref}`PDME <step-169>`
:::
<!-- step-tables:end -->

The steps fall into groups, as the index rows describe them:

* **Acid and peroxide cleans and wet etches** in the front end — the
  pre-furnace cleans, the nitride strip at {ref}`NS19 <step-013>`, the
  tunnel-window and gate-oxide etches, the backside film removal at
  {ref}`BFR <step-060>`, and the SPM and SC-1 cleans after the implant
  strips and after the trench, poly, spacer and nitride-cut etches.
* **Solvent cleans** after the contact, via, local-interconnect,
  metal, capacitor, seal-ring and pad etches, and in the sacrificial
  etch at {ref}`SACETCH <step-095>`.
* **Hydrogen peroxide outside a clean** — the tungsten polishes, where
  it is the slurry oxidiser, and the pad etch at
  {ref}`PDME <step-169>`, where the page names a possible wet removal of
  the metal-5 cap if it is TiW ({ref}`overview-metal-cap`).

## Supply, handling, safety and facilities

None of the SkyWater sources cited here describes the fab's chemical
delivery, bath management or waste treatment; the points below are
industry practice.

* **Purity and grades.** The SEMI specifications above standardise
  requirements by grade, and SEMI C44 gives "assay and impurity limits"
  for its higher-purity tiers;[^semi-c28][^semi-c30][^semi-c44] metal
  impurities matter because they deposit on the silicon that HF
  exposes.[^norga-1997]
* **Delivery and on-site generation.** Chemicals arrive in drums or
  bulk and are piped to the tools. Some are made at the fab: a Startec
  patent describes "preparing ultra-high-purity buffered hydrofluoric
  acid on-site at a semiconductor manufacturing facility", with the
  generation "monitored by a density measurement to produce an acid
  whose pH and buffering are accurately controlled".[^pat-bhf-startec]
* **Bath life and control.** Baths drift as they work and as peroxide
  decomposes;[^wiki-h2o2] conductivity tracks dilute HF,[^kikuyama-1994]
  water spiking holds a phosphoric bath,[^liu-2007] and SkyWater lists
  its single-wafer HF tool as "titration controlled".[^skw-01]
* **Hazards.** HF burns "can be treated with calcium gluconate
  gel";[^wiki-hf] piranha "should always be prepared by adding hydrogen
  peroxide to sulfuric acid slowly, never in reverse order", and
  concentrated sulphuric acid releases heat on
  dilution;[^wiki-piranha][^wiki-h2so4] isopropanol vapour "is
  flammable, with a flammability range of between 2% and 12.7% in
  air".[^wiki-ipa]
* **Waste and environment.** Acid, fluoride and solvent wastes are
  segregated and treated (industry practice); SkyWater's annual report
  states that "our facilities are ISO 14001 certified".[^sec-02]

## Process-integration notes for SKY130

These notes connect the class to the step pages; they add no SKY130
conditions of their own. SKY130's clean and wet-etch recipes are not
public.

* **HF-last surfaces and queue time.** A clean that ends in HF leaves a
  hydrogen-terminated surface[^higashi-1990] on which native oxide grows
  again in air or water;[^morita-1990] the {ref}`GOXETCH <step-046>`
  page matches a possible HF-last pre-gate clean to SkyWater's "dilute
  HF-last with IPA dry" entry,[^skw-01] and the time before the furnace is a
  {term}`queue time` the flow must control (industry practice).
* **SC-2 before hot steps.** The pre-furnace and pre-anneal cleans name
  SC-2 because it removes metals,[^wiki-rca] and SkyWater lists SC-2
  only on its DNS and FSI tools,[^skw-01] which is how the
  {ref}`wet bench page <machine-wet-bench>` assigns those cleans.
* **Thin oxides.** {ref}`TUNME <step-039>` and
  {ref}`GOXETCH <step-046>` etch thin oxides with dilute HF or BOE, as
  their pages read them; a Cypress embedded-SONOS patent that may still
  be in force names the chemistries it uses for both operations, in the
  collapsed note below this list; slow, buffered etches keep such steps
  controllable.[^wiki-boe][^kikuyama-1994]
* **The nitride strip.** The {ref}`NS19 <step-013>` page reads the
  isolation nitride strip as hot phosphoric acid, whose water content
  sets the nitride-to-oxide selectivity (industry
  practice);[^vgh-1967][^liu-2007] "phosphoric"
  appears only on SkyWater's Akrion entry.[^skw-01]
* **Backside silicon.** {ref}`BFR <step-060>` describes its silicon etch
  as HF/HNO₃, in which nitric acid oxidises the silicon and HF dissolves
  the oxide,[^robbins-1959] and quotes SkyWater's single-wafer entry,
  "HF, DSP+HF, titration controlled";[^skw-01] SkyWater does not say what
  "DSP" is.
* **Solvents over metal.** After the metal, via, capacitor and pad
  etches the step pages name EKC-class solvents rather than acids,
  because SPM attacks aluminium and TiN ({ref}`category-strip`). Where
  a metal etch uncovers the top of a tungsten plug below, as a line
  misaligned to its via can, Chen et al.'s finding that EKC265 corrodes
  tungsten, more so with water and chloride present, makes the clean's
  time and water content matter (our reading).[^chen-2003-ekc]
* **Peroxide in polishing.** The tungsten polishes list hydrogen
  peroxide as the slurry oxidiser ({ref}`category-cmp`); the slurry
  itself belongs to the CMP consumables class.

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
The Cypress embedded-SONOS patent names BOE for both operations (10:1
with surfactant for the pad oxide, and a BOE etch under similar
conditions for the thick gate oxide), with 20:1 BOE or 50:1 HF among
its alternatives for the pad oxide.[^pat-04]
:::

## Related pages

* {ref}`category-strip` — wet strip and clean chemistry, the nitride
  strip and solvent cleans.
* {ref}`category-etch` — wet etching of oxide, nitride and silicon.
* {ref}`machine-wet-bench` and
  {ref}`machine-single-wafer-spin-processor` — the tools that use these
  chemicals.
* {ref}`category-cmp` — slurries and post-CMP cleans.
* {ref}`materials-index` — all consumable classes, including ultrapure
  water and the post-CMP clean chemistry.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Related patents, papers and filings

* {ref}`Etchant composition <patent-gp15425124>` — US 4,582,624 A (1983)
* {ref}`Surface treating composition for micro processing <patent-gp16907918>` — US 4,795,582 A (1986)
* {ref}`Cleaning compositions for removing etching residue and method of using <patent-gp24443399>` — US 5,334,332 A (1990)
* {ref}`On-site generation of ultra-high-purity buffered-HF for semiconductor processing <patent-gp46252077>` — US 5,722,442 A (1994)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 8,796,098 B1 <patent-gp51229009>` — in force
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater Technology, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — the wet-bench,
  solvent, single-wafer, pre-clean and CMP entries quoted on this
  page.[^skw-01]
* SkyWater Technology, Form S-1 (2021) and Form 10-K for fiscal 2023 —
  the raw-materials paragraphs, chemical suppliers and environmental
  statements.[^sec-01][^sec-02]
* SEMI C28, C23, C30, C44 and C41 — the specifications for
  hydrofluoric acid, buffered oxide etchants, hydrogen peroxide,
  sulphuric acid and
  2-propanol.[^semi-c28][^semi-c23][^semi-c30][^semi-c44][^semi-c41]
* [Lee (EKC Technology), US 5,334,332](<https://patents.google.com/patent/US5334332A/en>) — hydroxylamine and alkanolamine
  residue removers.[^pat-ekc-hydroxylamine]

:::{dropdown} From a patent shown as in force (US 8,796,098; estimated expiry 2034-02-26) — open to read
* Ramkumar, Kouznetsov and Prabhakar (Cypress), US 8,796,098 — BOE and
  HF for the pad and thick gate oxides in an embedded-SONOS
  flow.[^pat-04]
:::

### High-level understanding

* Wikipedia, [*RCA clean*](<https://en.wikipedia.org/wiki/RCA_clean>) and [*Piranha solution*](<https://en.wikipedia.org/wiki/Piranha_solution>) — the SC-1, SC-2 and SPM
  recipes and their hazards.[^wiki-rca][^wiki-piranha]
* Wikipedia, [*Hydrofluoric acid*](<https://en.wikipedia.org/wiki/Hydrofluoric_acid>) and [*Buffered oxide etch*](<https://en.wikipedia.org/wiki/Buffered_oxide_etch>) — oxide
  etchants.[^wiki-hf][^wiki-boe]
* Wikipedia, [*Hydrogen peroxide*](<https://en.wikipedia.org/wiki/Hydrogen_peroxide>), [*Sulfuric acid*](<https://en.wikipedia.org/wiki/Sulfuric_acid>), [*Phosphoric acid*](<https://en.wikipedia.org/wiki/Phosphoric_acid>),
  [*Nitric acid*](<https://en.wikipedia.org/wiki/Nitric_acid>) and [*Isopropyl alcohol*](<https://en.wikipedia.org/wiki/Isopropyl_alcohol>) — the bulk
  chemicals.[^wiki-h2o2][^wiki-h2so4][^wiki-h3po4][^wiki-hno3][^wiki-ipa]
* [Kern, ch. 1 of *Handbook of Silicon Wafer Cleaning Technology*](<https://doi.org/10.1016/b978-081551554-8.50004-5>) — an
  overview of cleaning technology.[^kern-handbook]
* [Reinhardt and Kern (eds.), *Handbook of Silicon Wafer Cleaning
  Technology*](<https://openlibrary.org/isbn/9780815515548>) — wet cleaning, resist removal and
  contamination.[^reinhardt-2008]

### Deep dive

* Kern and Puotinen, *RCA Review* 1970 — the original peroxide cleaning
  solutions.[^kern-1970]
* [Kern, *JES* 1990](<https://doi.org/10.1149/1.2086825>) — how cleaning chemistry and equipment
  evolved.[^kern-1990]
* [Higashi et al., *APL* 1990](<https://doi.org/10.1063/1.102728>) — the hydrogen-terminated surface HF
  leaves.[^higashi-1990]
* [Morita et al., *JAP* 1990](<https://doi.org/10.1063/1.347181>) — native-oxide regrowth in air and
  water.[^morita-1990]
* [Itano et al., *IEEE TSM* 1993](<https://doi.org/10.1109/66.238174>) — particle removal in alkaline and acid
  cleans and a dilute SC-1 ratio.[^itano-1993]
* [Norga et al., *JES* 1997](<https://doi.org/10.1149/1.1837898>) — copper deposition on silicon from dilute
  HF.[^norga-1997]
* [Kikuyama et al., *JES* 1994](<https://doi.org/10.1149/1.2054733>) — dissociation and oxide etching in very
  dilute HF.[^kikuyama-1994]
* [Knotter and Denteneer, *JES* 2001](<https://doi.org/10.1149/1.1348262>) — the etching mechanism of nitride
  in HF solutions.[^knotter-2001]
* [van Gelder and Hauser, *JES* 1967](<https://doi.org/10.1149/1.2426757>) — nitride etching in hot phosphoric
  acid.[^vgh-1967]
* [Liu et al., *ECS Trans.* 2007](<https://doi.org/10.1149/1.2779363>) — keeping a phosphoric bath's
  selectivity stable in production.[^liu-2007]
* [Robbins and Schwartz, *JES* 1959](<https://doi.org/10.1149/1.2427397>) — the kinetics of HF–HNO₃ silicon
  etching.[^robbins-1959]
* [Schwartz and Robbins, *JES* 1976](<https://doi.org/10.1149/1.2132721>) — silicon etching
  technology.[^schwartz-1976]
* [Ohmi, *JES* 1996](<https://doi.org/10.1149/1.1837133>) — a room-temperature clean with less chemical and
  water.[^ohmi-1996]
* [Hattori et al., *JES* 1998](<https://doi.org/10.1149/1.1838798>) — ozonised water and dilute HF in a spin
  clean.[^hattori-1998]
* [Leenaars, Huethorst and van Oekel, *Langmuir* 1990](<https://doi.org/10.1021/la00101a014>) — Marangoni
  drying.[^leenaars-1990]
* [Chen et al., *Ind. Eng. Chem. Res.* 2003](<https://doi.org/10.1021/ie030025h>) — tungsten corrosion in
  EKC265.[^chen-2003-ekc]
* [Visintin, Korzenski and Baum, *JES* 2006](<https://doi.org/10.1149/1.2195884>) — liquid strippers for
  high-dose implanted resist.[^visintin-2006]
* [Ohmi, Miki and Kikuyama (Hashimoto Chemical), US 4,795,582](<https://patents.google.com/patent/US4795582A/en>) — buffered
  HF with surfactants.[^pat-bhf-hashimoto]
* [Enjo and Tamura (Daikin), US 4,582,624](<https://patents.google.com/patent/US4582624A/en>) — buffered HF with a
  fluorinated surfactant.[^pat-bhf-daikin]
* [Hoffman and Clark (Startec Ventures), US 5,722,442](<https://patents.google.com/patent/US5722442A/en>) — on-site
  generation of buffered HF.[^pat-bhf-startec]

## Open questions

* Which chemical, concentration and temperature each SKY130 clean or
  wet etch uses is not public; the step pages' readings rest on the
  capability list and industry practice.[^skw-01]
* What "DSP+HF" and "titration controlled" denote on the single-wafer
  entry, and whether "EKS265" is EKC265, are not stated.[^skw-01]
* Which chemicals KMG Chemicals, Air Products, EMD Performance Materials
  and CMC Chemicals supply to SkyWater, and to which grade, is not
  stated.[^sec-01][^sec-02]
* Whether nitric acid and ozonised water are used at all in SKY130
  lots is not stated by any SkyWater source.

<!-- footnotes -->

[^kern-1990]: W. Kern, "The Evolution of Silicon Wafer Cleaning
    Technology", *Journal of The Electrochemical Society* **137**(6),
    1887–1892 (1990). <https://doi.org/10.1149/1.2086825>
[^wiki-hf]: Wikipedia, *Hydrofluoric acid*.
    <https://en.wikipedia.org/wiki/Hydrofluoric_acid>
[^wiki-boe]: Wikipedia, *Buffered oxide etch*.
    <https://en.wikipedia.org/wiki/Buffered_oxide_etch>
[^wiki-h3po4]: Wikipedia, *Phosphoric acid*.
    <https://en.wikipedia.org/wiki/Phosphoric_acid>
[^robbins-1959]: H. Robbins and B. Schwartz, "Chemical Etching of
    Silicon", *Journal of The Electrochemical Society* **106**(6), 505
    (1959). <https://doi.org/10.1149/1.2427397>
[^wiki-rca]: Wikipedia, *RCA clean*.
    <https://en.wikipedia.org/wiki/RCA_clean>
[^wiki-piranha]: Wikipedia, *Piranha solution*.
    <https://en.wikipedia.org/wiki/Piranha_solution>
[^hattori-1998]: T. Hattori, T. Osaka, A. Okamoto, K. Saga and H.
    Kuniyasu, "Contamination Removal by Single‐Wafer Spin Cleaning with
    Repetitive Use of Ozonized Water and Dilute HF", *Journal of The
    Electrochemical Society* **145**(9), 3278–3284 (1998).
    <https://doi.org/10.1149/1.1838798>
[^pat-ekc-hydroxylamine]: W. M. Lee (EKC Technology), *Cleaning
    compositions for removing etching residue and method of using*,
    US 5,334,332 A, granted 1994-08-02.
    <https://patents.google.com/patent/US5334332A/en>
[^semi-c28]: SEMI, *SEMI C28 — Specification and Guide for Hydrofluoric
    Acid*, SEMI Standards store listing (revision C28-0618, inactive),
    accessed 2026-09-13.
    <https://store-us.semi.org/products/c02800-semi-c28-specification-and-guide-for-hydrofluoric-acid>
[^semi-c23]: SEMI, *SEMI C23 — Specification for Buffered Oxide
    Etchants*, SEMI Standards store listing (revision C23-0714,
    reapproved 0620), accessed 2026-09-13.
    <https://store-us.semi.org/products/c02300-semi-c23-specifications-for-buffered-oxide-etchants>
[^semi-c30]: SEMI, *SEMI C30 — Specification and Guide for Hydrogen
    Peroxide*, SEMI Standards store listing (revision C30-1223),
    accessed 2026-09-13.
    <https://store-us.semi.org/products/c03000-semi-c30-specification-for-hydrogen-peroxide>
[^semi-c44]: SEMI, *SEMI C44 — Specification and Guide for Sulfuric
    Acid*, SEMI Standards store listing (revision C44-1223), accessed
    2026-09-13.
    <https://store-us.semi.org/products/c04400-semi-c44-specification-and-guide-for-sulfuric-acid>
[^semi-c41]: SEMI, *SEMI C41 — Specification and Guide for 2-Propanol*,
    SEMI Standards store listing (revision C41-0618), accessed
    2026-09-13.
    <https://store-us.semi.org/products/c04100-semi-c41-specification-and-guide-for-2-propanol>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; resist removal, pre-cleaning and CMP entries re-checked
    2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22; "Raw materials." run-in paragraph
    under "Manufacturing" and "Environmental, Safety and Quality
    Matters"; read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024; "Raw materials" paragraph and "Environmental, Safety and
    Quality Matters"; read from a Wayback Machine copy on 2026-09-13.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^kern-1970]: W. Kern and D. A. Puotinen, "Cleaning solutions based on
    hydrogen peroxide for use in silicon semiconductor technology", *RCA
    Review* **31**, 187–206 (1970). No DOI; *RCA Review* 31 is available
    in print and in library archives.
[^kern-handbook]: W. Kern, "Overview and Evolution of Silicon Wafer
    Cleaning Technology", ch. 1 in K. A. Reinhardt and W. Kern (eds.),
    *Handbook of Silicon Wafer Cleaning Technology*, 2nd ed., William
    Andrew, 2008, pp. 3–92, ISBN 978-0-8155-1554-8.
    <https://doi.org/10.1016/b978-081551554-8.50004-5>
[^higashi-1990]: G. S. Higashi, Y. J. Chabal, G. W. Trucks and K.
    Raghavachari, "Ideal hydrogen termination of the Si (111) surface",
    *Applied Physics Letters* **56**(7), 656–658 (1990).
    <https://doi.org/10.1063/1.102728>
[^morita-1990]: M. Morita, T. Ohmi, E. Hasegawa, M. Kawakami and M.
    Ohwada, "Growth of native oxide on a silicon surface", *Journal of
    Applied Physics* **68**(3), 1272–1281 (1990).
    <https://doi.org/10.1063/1.347181>
[^kikuyama-1994]: H. Kikuyama, M. Waki, M. Miyashita, T. Yabune, N.
    Miki, J. Takano and T. Ohmi, "A Study of the Dissociation State and
    the SiO₂ Etching Reaction for HF Solutions of Extremely Low
    Concentration", *Journal of The Electrochemical Society* **141**(2),
    366–374 (1994). <https://doi.org/10.1149/1.2054733>
[^pat-bhf-hashimoto]: T. Ohmi, N. Miki and H. Kikuyama (Hashimoto
    Chemical Industries), *Surface treating composition for micro
    processing*, US 4,795,582 A, priority 1986-09-29, granted
    1989-01-03. <https://patents.google.com/patent/US4795582A/en>
[^pat-bhf-daikin]: N. Enjo and K. Tamura (Daikin Industries),
    *Etchant composition*, US 4,582,624 A, filed 1984-08-09, granted
    1986-04-15. <https://patents.google.com/patent/US4582624A/en>
[^knotter-2001]: D. M. Knotter and T. J. J. Denteneer, "Etching
    Mechanism of Silicon Nitride in HF-Based Solutions", *Journal of The
    Electrochemical Society* **148**(3), F43 (2001).
    <https://doi.org/10.1149/1.1348262>
[^norga-1997]: G. J. Norga, M. Platero, K. A. Black, A. J. Reddy, J.
    Michel and L. C. Kimerling, "Mechanism of Copper Deposition on
    Silicon from Dilute Hydrofluoric Acid Solution", *Journal of The
    Electrochemical Society* **144**(8), 2801–2810 (1997).
    <https://doi.org/10.1149/1.1837898>
[^itano-1993]: M. Itano, F. W. Kern, M. Miyashita and T. Ohmi, "Particle
    removal from silicon wafer surface in wet cleaning process", *IEEE
    Transactions on Semiconductor Manufacturing* **6**(3), 258–267
    (1993). <https://doi.org/10.1109/66.238174>
[^ohmi-1996]: T. Ohmi, "Total Room Temperature Wet Cleaning for Si
    Substrate Surface", *Journal of The Electrochemical Society*
    **143**(9), 2957–2964 (1996). <https://doi.org/10.1149/1.1837133>
[^wiki-h2o2]: Wikipedia, *Hydrogen peroxide*.
    <https://en.wikipedia.org/wiki/Hydrogen_peroxide>
[^vgh-1967]: W. van Gelder and V. E. Hauser, "The Etching of Silicon
    Nitride in Phosphoric Acid with Silicon Dioxide as a Mask", *Journal
    of The Electrochemical Society* **114**(8), 869 (1967).
    <https://doi.org/10.1149/1.2426757>
[^liu-2007]: L. Liu, I. Kashkoush, G. Chen and C. Murphy, "Maintaining a
    Stable Etch Selectivity between Silicon Nitride and Silicon Dioxide
    in a Hot Phosphoric Acid Bath", *ECS Transactions* **11**(2), 63–70
    (2007). <https://doi.org/10.1149/1.2779363>
[^schwartz-1976]: B. Schwartz and H. Robbins, "Chemical Etching of
    Silicon: IV. Etching Technology", *Journal of The Electrochemical
    Society* **123**(12), 1903–1909 (1976).
    <https://doi.org/10.1149/1.2132721>
[^wiki-hno3]: Wikipedia, *Nitric acid*.
    <https://en.wikipedia.org/wiki/Nitric_acid>
[^leenaars-1990]: A. F. M. Leenaars, J. A. M. Huethorst and J. J. van
    Oekel, "Marangoni drying: A new extremely clean drying process",
    *Langmuir* **6**(11), 1701–1703 (1990).
    <https://doi.org/10.1021/la00101a014>
[^chen-2003-ekc]: B.-H. Chen, H. Zhang, Chooi, L. Chan, Y. Xu and J. H.
    Ye, "Corrosive Behavior of Tungsten in Post Dry-Etch Residue
    Remover", *Industrial & Engineering Chemistry Research* **42**(24),
    6096–6103 (2003). <https://doi.org/10.1021/ie030025h>
[^visintin-2006]: P. M. Visintin, M. B. Korzenski and T. H. Baum,
    "Liquid Clean Formulations for Stripping High-Dose Ion-Implanted
    Photoresist from Microelectronic Devices", *Journal of The
    Electrochemical Society* **153**(7), G591 (2006).
    <https://doi.org/10.1149/1.2195884>
[^wiki-h2so4]: Wikipedia, *Sulfuric acid*.
    <https://en.wikipedia.org/wiki/Sulfuric_acid>
[^wiki-ipa]: Wikipedia, *Isopropyl alcohol*.
    <https://en.wikipedia.org/wiki/Isopropyl_alcohol>
[^pat-04]: K. Ramkumar, I. Kouznetsov and V. Prabhakar (Cypress
    Semiconductor), *Embedded SONOS based memory cells*, US 8,796,098
    B1, granted 2014-08-05.
    <https://patents.google.com/patent/US8796098B1/en>
    Shown as in force; estimated expiry 2034-02-26 (estimate from public
    records, not legal advice).
[^pat-bhf-startec]: J. G. Hoffman and R. S. Clark (Startec Ventures),
    *On-site generation of ultra-high-purity buffered-HF for
    semiconductor processing*, US 5,722,442 A, priority 1994-01-07,
    filed 1996-07-01, granted 1998-03-03.
    <https://patents.google.com/patent/US5722442A/en>
[^reinhardt-2008]: K. A. Reinhardt and W. Kern (eds.), *Handbook of
    Silicon Wafer Cleaning Technology*, 2nd ed., William Andrew, 2008,
    ISBN 978-0-8155-1554-8. <https://openlibrary.org/isbn/9780815515548>
