(category-oxidation)=
# Thermal oxidation

## What this class of step does

Thermal oxidation grows a film of silicon dioxide (SiO₂) *out of* the
silicon wafer itself, by exposing hot silicon to oxygen or steam. The
silicon at the surface is consumed and converted into glass. Because
the oxide is grown rather than deposited, its interface with the
underlying silicon is atomically clean and electrically almost perfect,
which is why the gate dielectric of every MOS transistor in a 130 nm
process is a thermal oxide (or a lightly nitrided thermal oxide), and
why thin thermal oxides are also used wherever silicon must be
protected, passivated or spaced from a nitride.

Precisely: the wafer is heated to between 800 and 1200 °C in a furnace
or a single-wafer rapid-thermal chamber and exposed to dry O₂ (dry
oxidation, Si + O₂ → SiO₂) or to water vapour (wet oxidation,
Si + 2H₂O → SiO₂ + 2H₂), for a time chosen from the growth kinetics to
give the target thickness.[^wiki-thox]
For every unit thickness of silicon consumed, 2.17 unit thicknesses of
oxide appear, so "46% of the oxide thickness will lie below the
original surface, and 54% above it".[^wiki-thox]

In the SKY130 flow the oxidation steps are the pad oxide under the STI
nitride ({ref}`BOX <step-002>`), the trench-liner oxidation
({ref}`LINOX <step-010>`), the tunnel-oxide/{term}`ONO` stack of the
{term}`SONOS` memory transistor ({ref}`ONO <step-040>`), the two gate oxidations
for the thick-oxide and thin-oxide transistors
({ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`) and what we infer to
be the post-gate-etch re-oxidation ({ref}`IOX45 <step-063>`).

## Physics and engineering background

### The Deal–Grove model

Deal and Grove (1965) showed that oxidation proceeds by the oxidant
diffusing *through* the existing oxide to react at the Si/SiO₂
interface, and that a steady-state flux balance gives the
linear–parabolic law[^deal-1965]

```{math}
x_{\mathrm{ox}}^2 + A\,x_{\mathrm{ox}} = B\,(t + \tau)
```

whose solution is

```{math}
x_{\mathrm{ox}}(t) = \frac{-A + \sqrt{A^2 + 4B(t+\tau)}}{2}.
```

For short times the growth is linear, {math}`x \approx (B/A)(t+\tau)`,
limited by the interface reaction; for long times it is parabolic,
{math}`x \approx \sqrt{B(t+\tau)}`, limited by diffusion through the
oxide. {math}`\tau` accounts for any oxide present at {math}`t = 0`.
Both rate constants are thermally activated, {math}`B = B_0
e^{-E_A/kT}` and {math}`B/A = (B/A)_0 e^{-E_A/kT}`, with the
parameters below for single-crystal silicon:[^wiki-dg]

| Parameter | Wet (H₂O) | Dry (O₂) |
|-----------|-----------|----------|
| {math}`(B/A)_0` (µm/h), ⟨100⟩ / ⟨111⟩ | 9.7 × 10⁷ / 1.63 × 10⁸ | 3.71 × 10⁶ / 6.23 × 10⁶ |
| {math}`E_A` (linear) (eV) | 2.05 | 2.00 |
| {math}`B_0` (µm²/h) | 386 | 772 |
| {math}`E_A` (parabolic) (eV) | 0.78 | 1.23 |

Three consequences follow. Wet oxidation is far faster than dry
because water's solubility in SiO₂ is about three orders of magnitude
higher than that of O₂, so thick field and pad oxides are grown wet.
The (111) linear rate exceeds the (100) rate, which is why the sidewall
of a trench oxidises faster than its floor. And because the activation
energies are large, oxide thickness is exquisitely sensitive to
temperature: near 900 °C a change of about 10 °C changes the linear
rate by roughly 20 %, so furnace temperature control to ±0.5 °C is
required.[^txt-01]

### The thin-oxide regime

The {term}`Deal–Grove model` under-predicts growth for the first 20–30 nm of dry
oxide: "very thin oxides (less than about 25 nanometres) grow much more
quickly in O₂ than the model predicts".[^wiki-dg] Massoud, Plummer and
Irene characterised this enhancement and added exponentially decaying
rate terms to fit it.[^massoud-1985] This is exactly the regime in which
gate oxides for 1.8 V and 5 V transistors are grown, so gate-oxide
recipes are calibrated empirically on the tool rather than taken from
the model. Practical calculators implementing Deal–Grove with Massoud
corrections are available online.[^byu-oxcalc]

### Oxide charge and quality

Deal's standard terminology distinguishes fixed oxide charge
{math}`Q_f`, interface-trapped charge {math}`Q_{it}`, oxide-trapped
charge {math}`Q_{ot}` and mobile ionic charge {math}`Q_m`.[^deal-1980]
Fixed charge and interface traps are lowest on (100) silicon and after a
post-oxidation anneal in inert gas; mobile sodium is immobilised by
adding chlorine, which "is often introduced by adding hydrogen chloride
or trichloroethylene to the oxidizing medium".[^wiki-thox] Wet oxides
have "more dangling bonds at the silicon interface" and lower density,
so thick oxides "are usually grown with a long wet oxidation bracketed
by short dry ones (a dry-wet-dry cycle)".[^wiki-thox] The final hydrogen
passivation of interface traps is done much later, at the {term}`alloy
anneal` ({ref}`category-anneal`).

### Nitrided oxides and ONO stacks

By the 130 nm node most gate oxides were lightly nitrided, either by
growing in N₂O or NO, or by a plasma or thermal nitridation after
growth. Nitrogen near the top interface blocks {term}`boron penetration` from
the p⁺ poly gate and raises the dielectric constant slightly; the ITRS
2001 expected "evolution of the oxynitride gate dielectric materials" to
continue until high-κ materials matured.[^itrs-01] For the SONOS memory
transistor, a very thin {term}`tunnel oxide` is grown, a charge-trapping silicon
nitride deposited by {term}`LPCVD`, and a {term}`blocking oxide` formed on top
by oxidising the nitride or depositing an oxide — the
oxide–nitride–oxide ({term}`ONO`) stack.[^wiki-sonos]

### Thin gate oxide versus thick field oxide

Two very different thickness regimes appear in a CMOS flow:

* **Gate oxides** of a few nanometres. ITRS 2001 lists an equivalent
  oxide thickness of 2.0–2.4 nm for low-operating-power and 2.4–2.8 nm
  for low-standby-power logic at the 130 nm node, and 5 nm for DRAM
  transfer devices; input/output transistors that must withstand 2.5 V,
  3.3 V or 5 V use proportionally thicker oxides.[^itrs-01] These are
  grown dry, often with a nitridation, typically at 750–950 °C,[^txt-01]
  in a furnace or an {term}`RTP` chamber, to a thickness controlled to within a
  few per cent (ITRS 2001 asks for {term}`EOT` control of ±4 % 3σ).[^itrs-01]
* **Pad, liner and {term}`screen oxides <screen oxide>`** of 5–30 nm, grown dry or wet, whose
  job is mechanical or chemical: cushioning the stress of an LPCVD
  nitride, rounding trench corners and passivating trench sidewalls,
  or scattering implanted ions to reduce {term}`channelling`.[^txt-01]
* **Field oxides** of hundreds of nanometres. In {term}`LOCOS` isolation
  these were grown wet at 900–1000 °C[^txt-01] through a nitride mask;
  at 250 nm and below the industry moved to {term}`STI`, in which the
  thick isolation oxide is *deposited* ({ref}`category-deposition`) and
  only a thin liner is grown.[^wiki-sti] SKY130 uses STI
  ({ref}`STIE <step-006>`).

### Dual gate oxide processes

A process with both 1.8 V and 5 V transistors grows its gate oxides in
two passes: a first, thicker oxide everywhere; a mask and wet etch to
strip it from the low-voltage active areas ({ref}`LVOM <step-044>`,
{ref}`GOXETCH <step-046>`); then a second, thin oxidation that also
adds slightly to the remaining thick oxide. The thick oxide's final
thickness is therefore the first growth plus a Deal–Grove increment
from the second growth, and both must be modelled together.[^txt-01]

### Furnace versus RTP and ISSG

Batch furnaces oxidise 100–150 wafers at once with excellent thickness
uniformity but a {term}`thermal budget` of tens of minutes at temperature;
single-wafer rapid-thermal oxidation (RTO) trades throughput for a
budget of seconds and the ability to switch ambient between steps. In
{term}`ISSG`, hydrogen and oxygen are injected into a reduced-pressure
RTP chamber and react at the hot wafer, generating steam and atomic
oxygen in situ; the resulting oxide is grown quickly and uniformly, and
the process is used for trench-liner and gate oxides where corner
rounding or nitride re-oxidation is wanted.[^txt-09]

## Typical equipment

* **{ref}`Vertical batch furnaces <machine-vertical-furnace-oxidation>`** for 200 mm wafers, with quartz tube,
  quartz boat, load-lock or nitrogen-purged loading, mass-flow
  controlled O₂/H₂/N₂/HCl (or DCE) delivery and, for wet oxidation, a
  pyrogenic torch burning H₂ in O₂ ahead of the tube. Representative
  tools: ASM A400 series (the original A400 has "more than 1000 reactors
  shipped" and covers "wet oxidation and anneal
  processes");[^asm-a400][^asm-vf] TEL Alpha-8 series; and the
  Aviza/Thermco (formerly Silicon Valley Group) vertical furnaces of the
  same era.
* **{ref}`Rapid thermal processors <machine-rapid-thermal-processor>`** for RTO and ISSG: AG Associates Heatpulse
  8108 (first shipped in 1992 and "targeted for volume production
  processes that utilize wafer sizes from 125 to 200
  millimeters"),[^ag-10k] Applied Materials Centura RTP
  (Radiance/Vantage chambers),[^amat-rtp] Mattson (which absorbed the
  Steag and AG Associates RTP lines).
* **Metrology**: {ref}`spectroscopic ellipsometers <machine-film-thickness-metrology>` (KLA-Tencor, Rudolph,
  Nanometrics) for thickness and refractive index; {ref}`C–V and I–V test structures <machine-parametric-tester>` at {ref}`category-test` for electrical thickness and
  breakdown.

## Typical consumables

* Oxygen (O₂), hydrogen (H₂) for pyrogenic steam or ISSG, nitrogen
  (N₂) for purge and anneal, all at semiconductor purity (99.9999 %
  or better).
* Chlorine sources: anhydrous HCl, or trans-1,2-dichloroethylene (DCE,
  which replaced trichloroethane) for sodium {term}`gettering`.
* N₂O or NO for {term}`oxynitride` gate dielectrics; NH₃ for nitridation.
* Quartz (fused silica) tubes, boats, baffles and liners, which are
  periodically cleaned or replaced; silicon carbide boats for
  high-temperature use.
* Dummy and monitor wafers (SEMI M8) to fill the boat and to measure
  thickness by ellipsometry.

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 2 | {ref}`BOX <step-002>` | Base oxidation |
| 10 | {ref}`LINOX <step-010>` | LINOX oxidation |
| 40 | {ref}`ONO <step-040>` | ONO stack oxidation |
| 43 | {ref}`GOX100 <step-043>` | Gate oxidation |
| 47 | {ref}`LVGOX <step-047>` | Gate oxidation |
| 63 | {ref}`IOX45 <step-063>` | Implant oxidation |

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
**Related patents.** 25 families concern this page (16 unknown, 9 expired); see {ref}`patents-by-module` for the full, grouped list (families still in force or of unknown status are collapsed there too).

**Related papers.**

* {ref}`paper-mathur-2005a` — N. Mathur et al., IIRW 2005 (affiliation inference)
<!-- index-links:end -->

## References

### Cross-check

* Deal and Grove, *JAP* 1965 — the linear–parabolic law and its rate
  constants.[^deal-1965]
* Massoud, Plummer and Irene, *JES* 1985 (part I) — the measured
  thin-regime growth enhancement.[^massoud-1985]
* Deal, *JES* 1980 — the standard names for the four oxide
  charges.[^deal-1980]
* ITRS 2001, *Front End Processes* — Tables 51 and 52, gate dielectric
  requirements and EOT control.[^itrs-01]
* ASM International, A400 DUO press release — the A400 furnace's
  install base and wet-oxidation/anneal use.[^asm-a400]
* Plasma-Therm, *AG Heatpulse 8800 / 8108 RTP* product
  spotlight.[^plasmatherm-ag]
* AG Associates, Form 10-K (fiscal 1996) — Heatpulse 8108 first shipped
  October 1992, 125–200 mm.[^ag-10k]

### High-level understanding

* Wikipedia, *Thermal oxidation* — reaction, silicon consumption,
  chlorine additions and dry–wet–dry cycles.[^wiki-thox]
* Wikipedia, *Deal–Grove model* — the rate-constant table and the
  thin-oxide caveat.[^wiki-dg]
* Wikipedia, *Gate oxide*.[^wiki-gox]
* Wikipedia, *LOCOS*.[^wiki-locos]
* Wikipedia, *Shallow trench isolation*.[^wiki-sti]
* Wikipedia, *SONOS*.[^wiki-sonos]
* Wikipedia, *Rapid thermal processing*.[^wiki-rtp]
* Brigham Young University Cleanroom, *Oxide Growth Calculator* —
  Deal–Grove with the thin-oxide correction, runnable
  online.[^byu-oxcalc]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 6
  ("Thermal Oxidation and the Si/SiO₂ Interface") and ch. 8 (screen
  oxides and channelling).[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 7 ("Thermal Oxidation of Single-Crystal Silicon").[^txt-02]
* Sze and Lee, *Semiconductor Devices: Physics and Technology* —
  ch. 11.[^sze-2012]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  ch. 4.[^campbell-2013]
* Xiao, *Introduction to Semiconductor Manufacturing Technology* —
  ch. 5.[^txt-08]

### Deep dive

* Ligenza and Spitzer, *J. Phys. Chem. Solids* 1960 — the isotope
  experiments showing that the oxidant diffuses through the oxide to
  react at the interface.[^ligenza-1960]
* Massoud, Plummer and Irene, *JES* 1985 (part II) — candidate physical
  mechanisms for the thin-regime enhancement.[^massoud-1985b]
* Massoud and Plummer, *JAP* 1987 — the closed-form thin-film oxidation
  relationship used by growth calculators.[^massoud-1987]
* Kao, McVittie, Nix and Saraswat, *IEEE TED* 1987 — measured
  two-dimensional oxidation of trench corners and its retardation at
  low temperature.[^kao-1987]
* Kao et al., *IEEE TED* 1988 — the viscous-stress model of corner
  oxidation, the basis of liner-oxide corner rounding.[^kao-1988]
* Kooi, van Lierop and Appels, *JES* 1976 — the "Kooi effect": nitride
  formed at the Si/SiO₂ interface under a nitride mask, and why a
  sacrificial oxide is grown before the gate oxide.[^kooi-1976]
* Hu, *JAP* 1974 — oxidation-induced stacking faults and
  oxidation-enhanced diffusion from injected
  interstitials.[^hu-1974]
* Tan and Gösele, *APL* 1982 — growth and shrinkage of
  oxidation-induced stacking faults tied to the interstitial
  supersaturation.[^tan-1982]
* Green, Gusev, Degraeve and Garfunkel, *JAP* 2001 — a long review of
  sub-4 nm SiO₂ and oxynitride gate dielectrics, their processing,
  structure and electrical limits.[^green-2001]
* Hori, *Gate Dielectrics and MOS ULSIs* — monograph on nitrided and
  reoxidised-nitrided gate oxides.[^hori-1997]
* Hori, Iwasaki and Tsuji, *IEEE TED* 1989 — electrical and physical
  properties of RTP reoxidised nitrided oxides.[^hori-1989]
* Yu et al. (TSMC), *Proc. SPIE* 1999 — ultrathin gate oxide grown by
  in-situ steam generation in an RTP chamber.[^yu-1999]
* Nagai et al., *JAP* 2002 — infrared study comparing RTO and ISSG thin
  oxides.[^nagai-2002]
* Nicollian and Brews, *MOS Physics and Technology* — the reference on
  oxide charges and C–V characterisation of the Si/SiO₂
  interface.[^nicollian-1982]
* Roozeboom and Parekh, *JVST B* 1990 — review of RTP systems with
  emphasis on temperature control.[^roozeboom-1990]
* Gardner (AMD), US 6,033,943 — a {term}`dual-gate-oxide <dual gate oxide>` process: first oxide,
  masked strip, second oxidation.[^pat-dgox-amd]
* Mehta, Logie and Fong (Lattice), US 7,985,656 — a thick STI trench
  liner grown above 1000 °C.[^pat-sti-lattice]
* SEMI MF576 — the standard ellipsometric test method for insulator
  thickness and refractive index on silicon.[^semi-mf576]
* MIT OpenCourseWare 6.774 — lecture notes on oxidation kinetics and
  the Si/SiO₂ interface.[^ocw-6774]
* Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology* — chapters on thermal processing, furnaces and
  RTP.[^txt-09]
* EDN, *Applied dedicates RTP with Vantage* — the Radiance/Vantage RTP
  chamber family.[^amat-rtp]

<!-- footnotes -->

[^wiki-thox]: Wikipedia, *Thermal oxidation*.
    <https://en.wikipedia.org/wiki/Thermal_oxidation>
[^deal-1965]: B. E. Deal and A. S. Grove, "General Relationship for the
    Thermal Oxidation of Silicon", *Journal of Applied Physics*
    **36**(12), 3770–3778 (1965). <https://doi.org/10.1063/1.1713945>
[^wiki-dg]: Wikipedia, *Deal–Grove model*.
    <https://en.wikipedia.org/wiki/Deal%E2%80%93Grove_model>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^massoud-1985]: H. Z. Massoud, J. D. Plummer and E. A. Irene, "Thermal
    Oxidation of Silicon in Dry Oxygen: Growth-Rate Enhancement in the
    Thin Regime. I. Experimental Results", *Journal of The
    Electrochemical Society* **132**(11), 2685–2693 (1985).
    <https://doi.org/10.1149/1.2113648>
[^byu-oxcalc]: Brigham Young University Cleanroom, *Oxide Growth
    Calculator* (Deal–Grove with thin-oxide correction).
    <https://cleanroom.byu.edu/OxideTimeCalc>
[^deal-1980]: B. E. Deal, "Standardized terminology for oxide charges
    associated with thermally oxidized silicon", *IEEE Transactions on
    Electron Devices* **27**(3), 606–608 (1980),
    DOI 10.1109/T-ED.1980.19908; published simultaneously in *Journal of
    The Electrochemical Society* **127**(4), 979–981 (1980).
    <https://doi.org/10.1109/T-ED.1980.19908>,
    <https://doi.org/10.1149/1.2129800>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^wiki-sonos]: Wikipedia, *SONOS*. <https://en.wikipedia.org/wiki/SONOS>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^asm-a400]: ASM International, *ASM International N.V. launches A400
    DUO vertical furnace system*, press release, 2019-11-11.
    <https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
[^asm-vf]: ASM International, *Vertical furnace*, product page.
    <https://www.asm.com/our-technology-products/vertical-furnace>
[^ag-10k]: AG Associates, Inc., Form 10-K for the fiscal year ended
    1996-09-30, filed 1996-12-23 (Heatpulse 8108 first shipped October
    1992; 125–200 mm).
    <https://www.sec.gov/Archives/edgar/data/942124/000089161896003159/0000891618-96-003159.txt>
[^amat-rtp]: EDN, *Applied dedicates RTP with Vantage*, 2002-09-23
    (Applied Materials Radiance/Vantage RTP chambers).
    <https://www.edn.com/applied-dedicates-rtp-with-vantage/>
[^plasmatherm-ag]: Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 /
    8108 RTP*, blog post.
    <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
[^wiki-gox]: Wikipedia, *Gate oxide*.
    <https://en.wikipedia.org/wiki/Gate_oxide>
[^wiki-locos]: Wikipedia, *LOCOS*. <https://en.wikipedia.org/wiki/LOCOS>
[^wiki-rtp]: Wikipedia, *Rapid thermal processing*.
    <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^sze-2012]: S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics
    and Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7.
    <https://www.wiley.com/en-us/Semiconductor+Devices%3A+Physics+and+Technology%2C+3rd+Edition-p-9780470537947>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^txt-08]: H. Xiao, *Introduction to Semiconductor Manufacturing
    Technology*, 2nd ed., SPIE Press, 2012, ISBN 978-0-8194-9092-6.
    <https://doi.org/10.1117/3.924283>
[^ligenza-1960]: J. R. Ligenza and W. G. Spitzer, "The mechanisms for
    silicon oxidation in steam and oxygen", *Journal of Physics and
    Chemistry of Solids* **14**, 131–136 (1960).
    <https://doi.org/10.1016/0022-3697(60)90219-5>
[^massoud-1985b]: H. Z. Massoud, J. D. Plummer and E. A. Irene,
    "Thermal Oxidation of Silicon in Dry Oxygen: Growth-Rate Enhancement
    in the Thin Regime. II. Physical Mechanisms", *Journal of The
    Electrochemical Society* **132**(11), 2693–2700 (1985).
    <https://doi.org/10.1149/1.2113649>
[^massoud-1987]: H. Z. Massoud and J. D. Plummer, "Analytical
    relationship for the oxidation of silicon in dry oxygen in the
    thin-film regime", *Journal of Applied Physics* **62**(8), 3416–3423
    (1987). <https://doi.org/10.1063/1.339305>
[^kao-1987]: D.-B. Kao, J. P. McVittie, W. D. Nix and K. C. Saraswat,
    "Two-dimensional thermal oxidation of silicon — I. Experiments",
    *IEEE Transactions on Electron Devices* **34**(5), 1008–1017 (1987).
    <https://doi.org/10.1109/T-ED.1987.23037>
[^kao-1988]: D.-B. Kao, J. P. McVittie, W. D. Nix and K. C. Saraswat,
    "Two-dimensional thermal oxidation of silicon. II. Modeling stress
    effects in wet oxides", *IEEE Transactions on Electron Devices*
    **35**(1), 25–37 (1988). <https://doi.org/10.1109/16.2412>
[^kooi-1976]: E. Kooi, J. G. van Lierop and J. A. Appels, "Formation of
    Silicon Nitride at a Si–SiO₂ Interface during Local Oxidation of
    Silicon and during Heat-Treatment of Oxidized Silicon in NH₃ Gas",
    *Journal of The Electrochemical Society* **123**(7), 1117–1120
    (1976). <https://doi.org/10.1149/1.2133008>
[^hu-1974]: S. M. Hu, "Formation of stacking faults and enhanced
    diffusion in the oxidation of silicon", *Journal of Applied Physics*
    **45**(4), 1567–1573 (1974). <https://doi.org/10.1063/1.1663459>
[^tan-1982]: T. Y. Tan and U. Gösele, "Oxidation-enhanced or retarded
    diffusion and the growth or shrinkage of oxidation-induced stacking
    faults in silicon", *Applied Physics Letters* **40**(7), 616–619
    (1982). <https://doi.org/10.1063/1.93200>
[^green-2001]: M. L. Green, E. P. Gusev, R. Degraeve and E. L.
    Garfunkel, "Ultrathin (<4 nm) SiO₂ and Si–O–N gate dielectric layers
    for silicon microelectronics: Understanding the processing,
    structure, and physical and electrical limits", *Journal of Applied
    Physics* **90**(5), 2057–2121 (2001).
    <https://doi.org/10.1063/1.1385803>
[^hori-1997]: T. Hori, *Gate Dielectrics and MOS ULSIs: Physics,
    Technology and Applications*, Springer Series in Electronics and
    Photonics, vol. 34, Springer, 1997.
    <https://doi.org/10.1007/978-3-642-60856-8>
[^hori-1989]: T. Hori, H. Iwasaki and K. Tsuji, "Electrical and physical
    properties of ultrathin reoxidized nitrided oxides prepared by rapid
    thermal processing", *IEEE Transactions on Electron Devices*
    **36**(2), 340–350 (1989). <https://doi.org/10.1109/16.19935>
[^yu-1999]: M.-C. Yu, S.-M. Jang, C. H. Diaz, C. H. Yu, S. C. Sun and M.
    S. Liang (TSMC), "Improvement of ultrathin gate oxide by a novel
    rapid thermal oxidation process with in-situ steam generation",
    *Proc. SPIE* **3881**, Microelectronic Device Technology III, 234
    (1999). <https://doi.org/10.1117/12.360557>
[^nagai-2002]: N. Nagai, K. Terada, Y. Muraji, H. Hashimoto et al.,
    "Infrared absorption study of rapid thermal oxidation and in situ
    steam generation of thin SiO₂ films by gradient etching
    preparation", *Journal of Applied Physics* **91**(7), 4747–4750
    (2002). <https://doi.org/10.1063/1.1459097>
[^nicollian-1982]: E. H. Nicollian and J. R. Brews, *MOS (Metal Oxide
    Semiconductor) Physics and Technology*, Wiley, 1982,
    ISBN 978-0-471-08500-3. <https://openlibrary.org/isbn/9780471085003>
[^roozeboom-1990]: F. Roozeboom and N. Parekh, "Rapid thermal processing
    systems: A review with emphasis on temperature control", *Journal of
    Vacuum Science & Technology B* **8**(6), 1249–1259 (1990).
    <https://doi.org/10.1116/1.584902>
[^pat-dgox-amd]: M. I. Gardner (Advanced Micro Devices), *Dual gate
    oxide thickness integrated circuit and process for making same*, US
    6,033,943 A, granted 2000-03-07.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6033943>
[^pat-sti-lattice]: S. Mehta, S. Logie and S. Fong (Lattice
    Semiconductor), *Shallow trench isolation (STI) with trench liner of
    increased thickness*, US 7,985,656 B1, granted 2011-07-26.
    <https://patents.google.com/patent/US7985656B1/en>
[^semi-mf576]: SEMI MF576, *Test Method for Measurement of Insulator
    Thickness and Refractive Index on Silicon Substrates by
    Ellipsometry*, SEMI.
    <https://store-us.semi.org/products/mf057600-semi-mf576-test-method-for-measurement-of-insulator-thickness-and-refractive-index-on-silicon-substrates-by-ellipsometry>
[^ocw-6774]: MIT OpenCourseWare, *6.774 Physics of Microfabrication:
    Front End Processing*, Fall 2004 (lecture notes on oxidation,
    diffusion, implantation and annealing).
    <https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/>
