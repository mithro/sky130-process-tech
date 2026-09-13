(machine-plasma-etcher-metal)=
# Plasma etcher: metal

A metal plasma etcher is the single-wafer dry-etch tool a fab uses to
pattern its aluminium interconnect: the titanium, aluminium–copper and
refractory-metal stacks of each metal level, and thin conductor films
such as a titanium nitride local interconnect or a capacitor top plate.
It etches in chlorine chemistries, controls the profile with a
sidewall film, and — because chlorine left on an aluminium line
corrodes it — is usually built as a cluster with passivation and resist
strip chambers so that the wafer leaves the vacuum clean. This page
describes the class in general, lists representative 200 mm-era
models, and then says what SkyWater has published about its own tools
of this class and which SKY130 steps this reference assigns to it. The
physics and chemistry of plasma etching are on the
{ref}`category page <category-etch>`.

| | Plasma etcher: metal |
|---|---|
| What it does | Anisotropic etching of aluminium alloys and the Ti, TiN and TiW layers around them in chlorine plasmas; Lam's TCP 9600SE "meets all requirements for aluminum and tungsten interconnect etch processing for sub-0.25-micron designs".[^lam-9600se-stripper-1998] |
| Plasma source | High-density inductive with separate wafer bias: Lam's "patented high-density Transformer Coupled Plasma etch technology"[^lam-9600se-stripper-1998] and Applied Materials' "DPS (decoupled plasma source) technology".[^amat-metal-dps-plus-1999] Earlier parallel-plate tools etched aluminium in "BCl3/CL2 plasmas".[^chen-1989] |
| Chemistry | Cl₂ with BCl₃; the aluminium etch rate "is primarlly dependent upon the Cl2 concentration", with additives for anisotropy;[^chen-1989] BCl₃ "etches metal oxides by formation of a volatile BOClx and MxOyClz compounds";[^wiki-bcl3] N₂ additions give a tapered profile in a TCP etcher.[^allen-1994] |
| Post-etch treatment | "Unlike other films, metal etching requires post etch treatment to prevent the onset of corrosion";[^christie-1994] integrated strip and passivation chambers, such as the microwave stripper Lam offered for the TCP 9600SE[^lam-9600se-stripper-1998] and Applied's strip chamber "based on its 200mm ASP technology".[^amat-300-etch-2000] |
| Throughput | "45 wafers per hour (WPH) compared to 35 WPH for the competition" claimed for the TCP 9600PTX;[^lam-9600ptx-1999] "more than 50 wafers per hour" for Applied's Metal Etch DPS Plus.[^amat-metal-dps-plus-1999] |
| 200 mm era | Applied's Metal Etch DPS Centura (1996) and its second-generation chamber (July 1997);[^amat-1997] Lam's TCP 9600, used for "sub 0.5 μm aluminum etching in a 200 mm LAM TCP 9600 Etch Chamber" by 1994,[^christie-1994] its PTX and DFM versions,[^lam-9600ptx-1999][^lam-9600dfm-2001] and the 2300 Versys Metal of 2000.[^lam-2300-2000] |
| SkyWater-listed tool | Under "Metal Etch": "Lam 9600, Al, TiW, TiN, Pt", "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt"[^skw-01] |
| SKY130 steps | 8 steps; see {ref}`SKY130 steps assigned to this class <machine-plasma-etcher-metal-steps>` |

## What the machine class is and how it works

Aluminium etches spontaneously in chlorine,[^cooperberg-2002] so a metal etcher does not
need ions to make the reaction happen; it needs them to make it
directional, and it must then deal with the chlorine that stays on the
wafer. Schaible, Metzger and Anderson described the principle in 1978:
halogen ion species "react with the metal to form volatile or easily
sputtered compounds", the reactive species "greatly enhances the etch
rate, while the electric field maintains the directionality".[^schaible-1978]
What makes a machine a *metal* etcher is therefore a chlorine-tolerant
chamber and gas system, sidewall-passivation control, a sequence that
breaks through oxide and refractory layers above and below the
aluminium, and integrated corrosion control. Poulsen's early review
already reported aluminium plasma etching and endpoint
detection,[^poulsen-1977] and Donnelly and Kornblit trace the later
development.[^donnelly-2013]

### Plasma source and chamber

The 200 mm metal etchers of the late 1990s used the same high-density
sources as silicon etch. Lam's TCP 9600 family is built on a planar
coil outside the chamber that induces "a planar region of ionic and
radical species" above the wafer,[^pat-tcp-lam][^lam-9600se-stripper-1998]
and Applied's Metal Etch DPS on a multi-section coil with an isolated
lid.[^pat-dps-amat][^amat-metal-dps-plus-1999] Christie et al.
optimised "Chemistries, powers, and pressures" in a 200 mm TCP 9600
chamber for "higher selectivities (<5:1) to photoresist, less RIE lag
(<15%), and more uniform profiles across a wafer", together with
"better particle control and the extended life of etch tool
hardware".[^christie-1994] Chamber materials are chosen against
corrosion: Applied's 300 mm DPS chamber uses "200mm-proven chamber materials and
surface coatings" that "minimizes corrosion and
defects".[^amat-300-etch-2000] Cooperberg, Vahedi and Gottscho related
"inductively coupled power, rf bias and gas flow ratio" to the ion,
chlorine and depositor fluxes that set an aluminium line's
profile.[^cooperberg-2002]

### Aluminium chemistry and sidewall passivation

Chen, DeOrnellas and Burke found in a parallel-plate etcher that the
aluminium etch rate "is primarlly dependent upon the Cl2 concentration
and is only slightly dependent upon the rf power", and that "Several
additives are used to achieve the high resolution and anisotropic
pattern required for aluminum alloys".[^chen-1989] BCl₃ is the usual
partner of Cl₂: it "etches metal oxides by formation of a volatile
BOClx and MxOyClz compounds",[^wiki-bcl3] and so clears the native
oxide on the aluminium. Bell, Anderson and Light measured Al/SiO₂ and
Al/photoresist etch-rate ratios of 13:1 and 2.5:1 for anisotropic
etching "in a conventional mixture of BCl3/Cl2".[^bell-1988] Because
the reaction is spontaneous, the profile is set by what deposits on
the sidewalls. Cooperberg et al. model the "Competition between etching
and deposition on feature sidewalls" with a carbon-bearing depositor
(CClₓ).[^cooperberg-2002] Carbon and nitrogen additions tilt
the balance toward taper: an AT&T patent uses "trifluoromethane and
chlorine in controlled amounts to create a tapered metal layer
profile",[^pat-taper-att] and Allen and Rickard achieved a tapered
profile "in a transformer coupled plasma etcher using only additions of
N2", with a polymer "easily removed with the remaining
photoresist".[^allen-1994] Hess reviews the underlying plasma chemistry
of aluminium and its alloys.[^hess-1982]

### Refractory layers: Ti, TiN and TiW

An aluminium stack is capped and underlaid with refractory films that
the etcher must also clear. Tungsten etches slowly in chlorine: Fischl and Hess measured tungsten rates "from below 10 nm/min
to 90 nm/min" in Cl₂ and Cl₂/BCl₃, with "Small additions of BCl₃"
raising the rates.[^fischl-1987] For TiW, Liu and Kuo found "Both F and
Cl are effective etchants", the rate depending on "both the plasma phase
etchant concentration and the ion bombardment energy", with a peak near
100 mTorr.[^liu-2007-tiw] Titanium nitride can be etched in a
"fluorine-deficient plasma" selective to titanium silicide, as a Texas
Instruments patent describes.[^pat-tin-etch-ti] Where a conductor film
sits on a thin dielectric, as a MiM capacitor top plate of any material
does, the over-etch must stop quickly: a later Texas Instruments patent etches a MiM top electrode
with two halogen gases, one containing fluorine, in a way that "removes
≦100 A of the thickness of the dielectric layer".[^pat-mim-ti-etch]

### Corrosion control and integrated strip

Chlorine left on the wafer after etch reacts with moisture and corrodes
aluminium–copper lines. Christie et al. put it plainly: "Unlike other
films, metal etching requires post etch treatment to prevent the onset
of corrosion".[^christie-1994] Metal etch platforms therefore carry
their own strip and passivation chambers. Lam's microwave stripper for
the TCP 9600SE has a "down-stream plasma source" that eliminates "the
potential for charge-induced damage of thin gate oxides", and Lam
reported "no corrosion during 48-hour wet box tests".[^lam-9600se-stripper-1998]
Applied's 300 mm metal etch system "contains an integrated strip
chamber, based on its 200mm ASP technology that rapidly removes
photoresist and performs a passivation process that extends post-etch
corrosion resistance".[^amat-300-etch-2000] Lam's 2300 Versys Metal
"handles aluminum etch and integrated resist removal".[^lam-2300-2000]
Corrosion can still follow the wet clean: Wai and Ling found that
corrosion "only happened … after wet polymer clean", traced it to
moisture left after the clean, and prevented it by lengthening the IPA
purge and wafer lift in the Marangoni dryer.[^wai-2017]

### Charging and notching

A metal line connected to a gate collects charge while it is being
separated from its neighbours. Noguchi et al. studied "plasma charging
due to antenna-topography-dependent electron shading effect during metal
etching on thin gate oxide" of 2.2–6.0 nm.[^noguchi-1997] Hashimoto
established the electron-shading mechanism with resist patterns over an
antenna,[^hashimoto-1994] and Hwang and Giapis, simulating the
over-etch of polysilicon lines on insulator, showed that "Transient
charging of exposed insulator surfaces is found to profoundly affect
local sidewall etching (notching)".[^hwang-1997]

## Representative 200 mm-era models

* **Lam Research.** The TCP 9600, used for sub-0.5 µm 200 mm aluminium
  etch development by 1994;[^christie-1994] the TCP 9600SE with a microwave stripper
  option (1998);[^lam-9600se-stripper-1998] the TCP 9600PTX, "qualified at
  multiple customer sites for 0.18 micron aluminum etch" with "0.13
  micron capability" demonstrated (1999);[^lam-9600ptx-1999] the TCP
  9600DFM "high-density metal etch system" for "sub-150 nm applications"
  (2001), a user of which reported tripling "MTBC to more than 300 RF
  hours" after moving from the PTX;[^lam-9600dfm-2001] and the 2300
  Versys Metal (2000), on a platform for "both 200- and 300-mm wafers",
  whose chamber allows "easy conversion to a silicon etch
  chamber".[^lam-2300-2000]
* **Applied Materials.** Metal etch on the Precision 5000 from
  1989–1990, MxP chambers from 1993, the Metal Etch DPS Centura (1996)
  and a second-generation DPS metal chamber (July 1997);[^amat-1997] the
  Metal Etch DPS Plus Centura (1999), when Applied counted "more than 200
  Metal Etch DPS Centura systems installed";[^amat-metal-dps-plus-1999]
  and the Metal Etch DPS 300 (2000).[^amat-300-etch-2000]
* **Other vendors.** The step pages also name Tokyo Electron Unity metal
  etchers ({ref}`MM1E <step-114>`); no vendor description was retrieved
  for this page.

## At SkyWater

### What SkyWater lists

Under "Etch", SkyWater's *Facilities & Capabilities* page has a "Metal
Etch" group of two tools:[^skw-01]

> "Lam 9600, Al, TiW, TiN, Pt"
>
> "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt"

Read term by term, both entries name aluminium, TiW, TiN and platinum,
and the 2300 entry adds niobium; neither names gases, titanium or
tungsten.[^skw-01] We read "Lam 9600" as Lam's TCP 9600 family, an
inference from the model number; SkyWater gives no model suffix (SE,
PTX or DFM) and does not say whether the 2300 Versys runs 200 mm wafers;
Lam launched the 2300 series for "both 200- and 300-mm
wafers".[^lam-2300-2000] No SKY130 step page uses platinum or
niobium; the capabilities page also lists "Nb damascene" among its special modules.[^skw-01] These are
the only listed etchers that name TiN.[^skw-01]

### Strength of the evidence

On the strength scale of the {ref}`machines index <machines-index>`
the two listings are **strong**: they are SkyWater
statements.[^skw-01] The caveats that apply to every listed tool are
under {ref}`Reading the SkyWater evidence <machines-reading-evidence>`.
For this class the listings are strong for the tools and for the
materials, TiN and TiW included; which of the two tools etches which
SKY130 level is not stated anywhere public.

(machine-plasma-etcher-metal-steps)=
### SKY130 steps assigned to this class

Steps whose "Machines typically used" section names a metal plasma
etcher as the tool or one of two options (identical to the
{ref}`machines index <machines-index>` table):

{ref}`LI1ME <step-103>`, {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`CAPME <step-138>`, {ref}`MM3E <step-140>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>`

How the step pages grade the SkyWater tools for each step ("Machines
likely used at SkyWater"), as collected on the machines index:

* **"Lam 9600, Al, TiW, TiN, Pt", "Lam 2300 Versys, Al, TiW, TiN, Nb, Pt"** — *inference:* {ref}`LI1ME <step-103>`; *not public which of the two (the page leans to one, by inference):* {ref}`MM1E <step-114>`, {ref}`MM2E <step-125>`, {ref}`MM3E <step-140>`; *not public which of the two:* {ref}`CAPME <step-138>`, {ref}`CAP2ME <step-153>`, {ref}`MM4E <step-155>`, {ref}`MM5E <step-163>`; *weak:* {ref}`PDME <step-169>`; *named as corroboration only:* {ref}`TIAL6 <step-112>`, {ref}`TIAL12 <step-123>`, {ref}`WTIAL3 <step-134>`, {ref}`CAPTIW1 <step-136>`, {ref}`WTIAL4 <step-149>`, {ref}`CAPTIW2 <step-151>`, {ref}`WTIAL5 <step-161>`
* **"AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2"** — *medium:* {ref}`LI1ME <step-103>` (the full grade list is on the {ref}`silicon and polysilicon etcher page <machine-plasma-etcher-silicon>`)

The inference for the local interconnect rests on the listed materials:
TiN appears only on the two metal-etch entries.[^skw-01] The metal-level
pages lean to the 2300 for metals 1 and 2 and to the 9600 for metal 3,
an inference from the platforms' age, not a SkyWater statement.

## Consumables and facilities

The etch gases and chamber parts are listed in the
{ref}`materials index <materials-index>`; what is specific to a metal
etcher is summarised here. None of the SkyWater sources describes the
fab's gas delivery or abatement.

* **Chlorine chemistry.** Cl₂ and BCl₃, with N₂ or a fluorocarbon such
  as CHF₃ for sidewall passivation;[^chen-1989][^allen-1994][^pat-taper-att]
  BCl₃ "is also used in plasma etching in semiconductor
  manufacturing".[^wiki-bcl3] Fluorine-bearing additions serve the TiW
  and TiN layers.[^liu-2007-tiw][^pat-mim-ti-etch]
* **Integrated strip.** A downstream stripper on the etch platform
  removes the resist and, in Applied's design, runs a passivation step
  before the wafer leaves the system.[^lam-9600se-stripper-1998][^amat-300-etch-2000]
* **Chamber parts and cleans.** Chamber materials and coatings chosen
  against corrosion,[^amat-300-etch-2000] and consumable parts whose
  cost Lam's 9600DFM set out to "virtually eliminate"; the same release
  quotes a mean time between cleans of "more than 300 RF
  hours".[^lam-9600dfm-2001]
* **Monitor wafers and corrosion checks.** Open-frame wafers for aluminium and
  resist etch rates;[^cooperberg-2002] the metal-level pages
  add corrosion inspection after a queue-time delay
  ({ref}`MM1E <step-114>`).

## Process-integration notes for SKY130

These notes connect the machine class to the step pages; they add no
SKY130 conditions of their own. SKY130's etch recipes are not public.

* **Three kinds of metal etch.** The class covers the local
  interconnect ({ref}`LI1ME <step-103>`), titanium nitride in Edwards's
  PDK lecture;[^ann-16] the five metal levels ({ref}`MM1E <step-114>`
  to {ref}`MM5E <step-163>`),[^pdk-10] "5 layers of aluminum metal" in
  the same lecture,[^ann-16] which a Cypress qualification report
  describes, for metals 1 to 3, as Ti/Al–Cu/TiW
  stacks;[^cyp-qtp-113005] and the two capacitor top plates ({ref}`CAPME <step-138>`,
  {ref}`CAP2ME <step-153>`). The PDK calls the top plate only "a thin
  conductor layer on top of the dielectric";[^pdk-07] this reference
  reads it as TiW (inference, set out on the {ref}`CAPTIW1 <step-136>`
  page: TiW caps the Cypress S8 aluminium stacks[^cyp-qtp-113005] and is
  on SkyWater's PVD and metal-etch lists[^skw-01]), and the same
  evidence would equally allow TiN. SkyWater's two entries name Al, TiN
  and TiW.[^skw-01]
* **Stopping on tungsten plugs and thin dielectrics.** The aluminium
  over-etch lands on oxide and on the tops of the tungsten plugs
  (SkyWater lists "Lam/Novellus PECVD Tungsten – plug fill"[^skw-01];
  {ref}`tungsten CVD page <machine-tungsten-cvd>`),
  with selectivity to the plugs ({ref}`MM1E <step-114>`); chlorine etched
  tungsten at no more than 90 nm/min in Fischl and Hess's
  conditions;[^fischl-1987] the capacitor
  top-plate etches, whatever the plate material, land on the thin MiM
  dielectric, where the step pages
  cite a patent that removes no more than about 100 Å of
  it.[^pat-mim-ti-etch]
* **Profiles for gap fill.** The inter-level oxides deposited over each
  metal level must fill the spaces the etch leaves; a tapered profile
  is one way to ease the fill, set by the N₂ or carbon
  additions.[^allen-1994][^pat-taper-att]
* **Corrosion between etch and clean.** Every aluminium level goes from
  the etcher through a strip and a solvent clean; the step pages name
  SkyWater's ashers and its "EKS265, EKC270 solvents" tool, and the
  queue time and drying after the clean decide whether lines
  corrode.[^skw-01][^wai-2017]
* **Antenna charging.** The metal etches separate lines connected to
  gates; the SKY130 antenna rules exist for this reason
  ({ref}`category-etch`), and electron shading during metal etching is
  the mechanism Noguchi et al. studied.[^noguchi-1997]

## Related pages

* {ref}`category-etch` — plasma and wet etching physics and the 27
  etch steps of SKY130.
* {ref}`machine-plasma-etcher-silicon` — the silicon etchers, one of
  which the {ref}`LI1ME <step-103>` page offers as a medium option.
* {ref}`machines-index` — all machine classes, SkyWater's listed tools
  and the step assignments.
* {ref}`category-deposition` — the TiN, aluminium and refractory films
  these etches pattern, and the capacitor top-plate film (TiW on this
  reference's reading, {ref}`CAPTIW1 <step-136>`).
* {ref}`materials-index` — etch gases and chamber materials.

## References

### Cross-check

* SkyWater Technology, *Facilities & Capabilities* — the two "Metal
  Etch" entries quoted on this page.[^skw-01]
* SkyWater PDK, *Device Details* — the MiM top plate as "a thin
  conductor layer", its material unnamed.[^pdk-07]
* Cypress, QTP 113005 — the Ti/Al–Cu/TiW composition of the S8 metal
  stacks.[^cyp-qtp-113005]
* SkyWater PDK, *google/skywater-pdk* README — "1 level of local
  interconnect" and "5 levels of metal".[^pdk-10]
* Lam Research, TCP 9600SE microwave stripper announcement (1998) — the
  TCP metal etcher, its integrated downstream stripper and corrosion
  tests.[^lam-9600se-stripper-1998]
* Lam Research, TCP 9600PTX press release (1999) — throughput and
  0.18 µm qualification.[^lam-9600ptx-1999]
* Lam Research, TCP 9600DFM press release (2001) — consumables and time
  between cleans.[^lam-9600dfm-2001]
* Lam Research, 2300 Etch Series press release (2000) — the 2300 Versys
  Metal and its integrated resist removal.[^lam-2300-2000]
* Applied Materials, 1997 annual report (Form 10-K) — dates of the
  Metal Etch DPS systems.[^amat-1997]
* Applied Materials, Metal Etch DPS Plus press release (1999) —
  throughput, installed base and source.[^amat-metal-dps-plus-1999]
* Applied Materials, 300 mm etch product line press release (2000) —
  chamber materials and the integrated ASP-based strip
  chamber.[^amat-300-etch-2000]
* Ogle (Lam Research), US 4,948,458 — the TCP source.[^pat-tcp-lam]
* Yin et al. (Applied Materials), US 5,540,824 — the DPS
  reactor.[^pat-dps-amat]

### High-level understanding

* Edwards (Efabless), *Introduction to the SkyWater PDK* — the TiN
  local interconnect and the five aluminium metal layers.[^ann-16]
* Wikipedia, *Reactive-ion etching*.[^wiki-rie]
* Wikipedia, *Plasma etching*.[^wiki-plasma-etch]
* Wikipedia, *Boron trichloride* — the oxide-scavenging etch
  gas.[^wiki-bcl3]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — dry
  etching of aluminium.[^txt-02]

### Deep dive

* Poulsen, *JVST* 1977 — early aluminium plasma etching and endpoint
  detection.[^poulsen-1977]
* Schaible, Metzger and Anderson, *JVST* 1978 — reactive ion etching of
  aluminium in halogen plasmas.[^schaible-1978]
* Hess, *Plasma Chem. Plasma Process.* 1982 — the plasma etch chemistry
  of aluminium and its alloys.[^hess-1982]
* Bell, Anderson and Light, *JES* 1988 — selectivities of BCl₃/Cl₂ and
  BBr₃/Cl₂ aluminium etching.[^bell-1988]
* Chen, DeOrnellas and Burke, ASTM STP 990, 1989 — aluminium etch rate
  against Cl₂, power and additives.[^chen-1989]
* Christie et al., ASMC 1994 — sub-0.5 µm aluminium etch and post-etch
  treatment in a 200 mm TCP 9600.[^christie-1994]
* Allen and Rickard, *JVST A* 1994 — a tapered aluminium etch with N₂ in
  a TCP etcher.[^allen-1994]
* Bredbenner et al. (AT&T Bell Laboratories), US 4,919,748 — tapered
  aluminium etching with CHF₃ and Cl₂.[^pat-taper-att]
* Cooperberg, Vahedi and Gottscho, *JVST A* 2002 — profile simulation of
  Cl₂/BCl₃ aluminium etching.[^cooperberg-2002]
* Fischl and Hess, *JES* 1987 — tungsten and tungsten silicide etching in
  chlorine discharges.[^fischl-1987]
* Liu and Kuo, *JES* 2007 — reactive ion etching of TiW.[^liu-2007-tiw]
* Douglas (Texas Instruments), US 4,675,073 — a fluorine-deficient TiN
  etch selective to silicide.[^pat-tin-etch-ti]
* Cathey et al. (Texas Instruments), US 8,110,414 — a MiM top-electrode
  etch that stops on a thin dielectric.[^pat-mim-ti-etch]
* Danzl and McLaurin, IEMT 1997 — hydrogen peroxide removal of a TiW
  cap from aluminium pads.[^danzl-1997]
* Wai and Ling, ASMC 2017 — Al–Cu corrosion after metal etch and wet
  polymer clean.[^wai-2017]
* Noguchi et al., IEDM 1997 — electron-shading charging during metal
  etching.[^noguchi-1997]
* Hashimoto, *JJAP* 1994 — the electron-shading mechanism.[^hashimoto-1994]
* Hwang and Giapis, *JVST B* 1997 — a simulation of notching from
  transient charging in the polysilicon over-etch in high-density
  plasmas.[^hwang-1997]
* Donnelly and Kornblit, *JVST A* 2013 — a review of plasma
  etching.[^donnelly-2013]

## Open questions

* Which of SkyWater's two metal etchers runs which metal level, the
  local interconnect and the capacitor plates is not stated;[^skw-01]
  the step pages' leanings are inferences.
* Which 9600 version SkyWater has, whether its 2300 Versys runs 200 mm
  wafers, and whether either carries an integrated strip or passivation
  chamber are not stated.
* The model list above is incomplete: it covers the Lam and Applied
  Materials metal etchers for which a public description was found, not
  the Tokyo Electron and other metal etchers of the period.

<!-- footnotes -->

[^lam-9600se-stripper-1998]: Lam Research Corporation, *Lam Research
    Introduces Microwave Stripper for High-Density Metal Etch System*,
    news item, Semiconductor Online, 1998-01-09.
    <https://www.semiconductoronline.com/doc/lam-research-introduces-microwave-stripper-fo-0001>
[^amat-metal-dps-plus-1999]: Applied Materials, *Applied Materials
    Introduces the Metal Etch DPS Plus Centura for Sub-0.18 Micron Metal
    Etch*, press release, 1999-04-13.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-metal-etch-dps-plus-centura-sub-018/>
[^chen-1989]: C.-H. Chen, S. DeOrnellas and B. Burke, "Plasma Etching of
    Aluminum Alloys in BCl₃/Cl₂ Plasmas", in *Semiconductor Fabrication:
    Technology and Metrology*, ASTM STP 990, ASTM International, 1989,
    pp. 202–211. <https://doi.org/10.1520/STP26039S>
[^wiki-bcl3]: Wikipedia, *Boron trichloride*.
    <https://en.wikipedia.org/wiki/Boron_trichloride>
[^allen-1994]: L. R. Allen and R. Rickard, "Tapered aluminum
    interconnect etch", *Journal of Vacuum Science & Technology A*
    **12**(4), 1265–1268 (1994). <https://doi.org/10.1116/1.579306>
[^christie-1994]: R. Christie, S. Burns, V. S. Grewal and B. Spuler,
    "Sub 0.5 μm TCP metal etching in the ASTC", *Proceedings of 1994
    IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC)*, p. 224. <https://doi.org/10.1109/ASMC.1994.588254>
[^amat-300-etch-2000]: Applied Materials, *Applied Materials Unveils
    300mm Etch Product Line*, press release, 2000-07-10.
    <https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-300mm-etch-product-line>
[^lam-9600ptx-1999]: Lam Research, *Lam Research Corporation Gaining
    Momentum In Metal Etch With Multiple Wins*, press release,
    1999-02-16.
    <https://newsroom.lamresearch.com/1999-02-16-Lam-Research-Corporation-Gaining-Momentum-In-Metal-Etch-With-Multiple-Wins>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report* (Form 10-K
    for the fiscal year ended 1997-10-26).
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^lam-9600dfm-2001]: Lam Research, *Lam Research Corporation Takes Metal
    Processing To New Level With New TCP 9600DFM*, press release,
    2001-06-18.
    <https://investor.lamresearch.com/2001-06-18-Lam-Research-Corporation-Takes-Metal-Processing-To-New-Level-With-New-TCP-R-9600DFM>
[^lam-2300-2000]: Lam Research, *Lam Research Corporation Launches
    Industry's First 200- And 300-Mm Capable Etch Product Line*, press
    release, 2000-11-16.
    <https://newsroom.lamresearch.com/2000-11-16-Lam-Research-Corporation-Launches-Industrys-First-200-And-300-Mm-Capable-Etch-Product-Line>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30; etch entries re-checked 2026-09-13.
    <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^cyp-qtp-113005]: Cypress Semiconductor, *Product Qualification
    Plan, QTP# 113005: 64K Serial Non-Volatile SRAM Product Family, S8
    Technology, CMI (Fab 4)*, document 001-85611 Rev. *A, January
    2013 (copy hosted by Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-qtp-113005-64k-serial-non-volatile-sram-product-family-s8-technology-cmi-fab-4-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d714bf28311de>
[^pdk-10]: SkyWater PDK Authors, *google/skywater-pdk* repository
    README. <https://github.com/google/skywater-pdk>
[^ann-16]: T. Edwards (Efabless), *Introduction to the SkyWater PDK —
    The New Age of Open Source Silicon*, lecture slides, 2021-10-08
    (UC San Diego BENG 207).
    <https://isn.ucsd.edu/courses/beng207/lectures/Tim_Edwards_2021_slides.pdf>
[^schaible-1978]: P. M. Schaible, W. C. Metzger and J. P. Anderson,
    "Reactive ion etching of aluminum and aluminum alloys in an rf plasma
    containing halogen species", *Journal of Vacuum Science and
    Technology* **15**(2), 334–337 (1978).
    <https://doi.org/10.1116/1.569540>
[^poulsen-1977]: R. G. Poulsen, "Plasma etching in integrated circuit
    manufacture — A review", *Journal of Vacuum Science and Technology*
    **14**(1), 266–274 (1977). <https://doi.org/10.1116/1.569137>
[^donnelly-2013]: V. M. Donnelly and A. Kornblit, "Plasma etching:
    Yesterday, today, and tomorrow", *Journal of Vacuum Science &
    Technology A* **31**(5), 050825 (2013).
    <https://doi.org/10.1116/1.4819316>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*,
    US 4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^pat-dps-amat]: G. Z. Yin, H. Hanawa, D. X. Ma and D. Olgado (Applied
    Materials), *Plasma reactor with multi-section RF coil and isolated
    conducting lid*, US 5,540,824 A, granted 1996-07-30.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5540824>
[^cooperberg-2002]: D. J. Cooperberg, V. Vahedi and R. A. Gottscho,
    "Semiempirical profile simulation of aluminum etching in a Cl₂/BCl₃
    plasma", *Journal of Vacuum Science & Technology A* **20**(5),
    1536–1556 (2002). <https://doi.org/10.1116/1.1494818>
[^bell-1988]: H. B. Bell, H. M. Anderson and R. W. Light, "Reactive Ion
    Etching of Aluminum/Silicon in BBr₃/Cl₂ and BCl₃/Cl₂ Mixtures",
    *Journal of The Electrochemical Society* **135**(5), 1184–1191
    (1988). <https://doi.org/10.1149/1.2095919>
[^pat-taper-att]: C. N. Bredbenner, T. A. Giniecki, N. Selamoglu and
    H. J. Stocker (AT&T Bell Laboratories), *Method for tapered etching*,
    US 4,919,748 A, filed 1989-06-30, granted 1990-04-24.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4919748>
[^hess-1982]: D. W. Hess, "Plasma etch chemistry of aluminum and
    aluminum alloy films", *Plasma Chemistry and Plasma Processing*
    **2**(2), 141–155 (1982). <https://doi.org/10.1007/BF00633130>
[^fischl-1987]: D. S. Fischl and D. W. Hess, "Plasma-Enhanced Etching of
    Tungsten and Tungsten Silicide in Chlorine-Containing Discharges",
    *Journal of The Electrochemical Society* **134**(9), 2265–2269
    (1987). <https://doi.org/10.1149/1.2100868>
[^liu-2007-tiw]: G. Liu and Y. Kuo, "Reactive Ion Etching of Titanium
    Tungsten Thin Films", *Journal of The Electrochemical Society*
    **154**(7), H653 (2007). <https://doi.org/10.1149/1.2737631>
[^pat-tin-etch-ti]: M. A. Douglas (Texas Instruments), *TiN etch
    process*, US 4,675,073 A, filed 1986-03-07, granted 1987-06-23.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4675073>
[^pat-mim-ti-etch]: M. O. Cathey Jr., P. Mahalingam, W. Tian, D. C.
    Guiling, X. Chen, B. Hu and S. Chevacharoenkul (Texas Instruments),
    *Forming integrated circuit devices with metal-insulator-metal
    capacitors using selective etch of top electrodes*, US 8,110,414 B2,
    filed 2009-04-30, granted 2012-02-07.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8110414>
[^wai-2017]: W. T. Wai and N. C. Ling, "Al-Cu interconnect corrosion
    prevention in post metal etch and wet polymer clean wafers: CFM:
    Contamination free manufacturing", *2017 28th Annual SEMI Advanced
    Semiconductor Manufacturing Conference (ASMC)*, pp. 64–67.
    <https://doi.org/10.1109/ASMC.2017.7969200>
[^noguchi-1997]: K. Noguchi, K. Tokashiki, T. Horiuchi and H.
    Miyamoto, "Reliability of thin gate oxide under plasma charging
    caused by antenna topography-dependent electron shading effect",
    *IEDM 1997 Technical Digest*, pp. 441–444.
    <https://doi.org/10.1109/IEDM.1997.650419>
[^hashimoto-1994]: K. Hashimoto, "Charge Damage Caused by Electron
    Shading Effect", *Japanese Journal of Applied Physics* **33**(10R),
    6013 (1994). <https://doi.org/10.1143/JJAP.33.6013>
[^hwang-1997]: G. S. Hwang and K. P. Giapis, "On the origin of the
    notching effect during etching in uniform high density plasmas",
    *Journal of Vacuum Science & Technology B* **15**(1), 70–87 (1997).
    <https://doi.org/10.1116/1.589258>
[^danzl-1997]: R. B. Danzl and A. McLaurin, "The use of concentrated
    hydrogen peroxide for the removal of a TiW ARC from aluminum bond
    pads", *Proc. 21st IEEE/CPMT International Electronics Manufacturing
    Technology Symposium* (1997), pp. 99–104.
    <https://doi.org/10.1109/IEMT.1997.626884>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-plasma-etch]: Wikipedia, *Plasma etching*.
    <https://en.wikipedia.org/wiki/Plasma_etching>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
