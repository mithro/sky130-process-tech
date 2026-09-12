(category-anneal)=
# Anneal / thermal processing

## What this class of step does

An anneal heats the wafer, in a controlled ambient, to make something
happen that only heat can do: repair the crystal damage left by an ion
implant and put the dopant atoms onto lattice sites where they are
electrically active; diffuse dopants to a designed depth; react a metal
with silicon to form a low-resistance silicide; or, at the very end of
the flow, sinter the metal contacts and passivate the oxide interfaces
with hydrogen. Unlike oxidation ({ref}`category-oxidation`) nothing is
meant to grow, so the ambient is usually inert (nitrogen or argon) or
mildly reducing.

Precisely, the seven thermal steps in the SKY130 flow fall into four
types:

* **Implant activation and well anneals** — a furnace or rapid
  thermal anneal ({term}`RTA`) after the well and channel implants
  ({ref}`RTAI <step-034>`), after the extension implants
  ({ref}`TIPRTAD <step-075>`) and after the source/drain implants
  ({ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`).
* **Silicidation** — the reaction anneal(s) that turn a deposited
  titanium or cobalt film into a {term}`silicide` on the exposed
  silicon and polysilicon ({ref}`CSIL <step-098>`).
* **Alloy (sinter)** — a typically 350–450 °C anneal[^txt-02] in
  {term}`forming gas` after contact formation ({ref}`ALLY1 <step-096>`)
  and after the last metal ({ref}`ALLY <step-170>`).
* Purely by association, the PSG densification, ILD bakes and the like
  are treated as part of the deposition steps.

## Physics and engineering background

### Diffusion

Dopant movement during an anneal is governed by Fick's laws, {math}`J =
-D\,\partial C/\partial x` and {math}`\partial C/\partial t =
D\,\partial^2 C/\partial x^2`,[^wiki-fick] with a diffusivity that
follows the Arrhenius law {math}`D = D_0 e^{-E_A/kT}`.[^wiki-arrhenius]
For the common dopants in silicon the activation energies are of order
3–4 eV, so diffusion is negligible below about 800 °C and doubles
roughly every 20–30 °C above it; a Gaussian implanted profile broadens
such that its characteristic width grows as {math}`\sqrt{2Dt}`, and the
product {math}`Dt` summed over every hot step is the process's "thermal
budget".[^txt-01] At the concentrations used for wells and channels,
diffusion is intrinsic; at source/drain concentrations it is enhanced by
the Fermi-level dependence of the point-defect populations, and
phosphorus and boron diffuse mainly via interstitials while arsenic and
antimony use vacancies.

### Activation and damage annealing

Implanted dopant is electrically inactive until the lattice is restored.
Amorphised layers regrow by solid-phase epitaxy at 500–600 °C with the
dopant incorporated substitutionally up to and beyond its equilibrium
solid solubility; partially damaged layers need 800–1000 °C to dissolve
the defect clusters.[^gibbons-1972][^txt-01] Two effects make the choice
of anneal a compromise. Above the solid solubility the dopant
precipitates or clusters and deactivates, so the highest activation is
obtained by annealing hot and fast. And the interstitials released as
the damage anneals cause transient enhanced diffusion ({term}`TED`),
which is worst for slow, low-temperature anneals because the damage
dissolves while the dopant is still mobile.[^stolk-1997] The resolution
is the RTA: seconds at 1000–1100 °C,[^stolk-1997] or a "spike" anneal
with essentially zero soak time, which activates the dopant while the
junction moves only a few nanometres. ITRS 2001 identifies the boron
extension junction as the critical one and asks for its depth,
abruptness and sheet resistance to be met simultaneously.[^itrs-01]

### Rapid thermal processing

RTP "heats silicon wafers to temperatures exceeding 1,000°C for not more
than a few seconds" using "high intensity lamps or lasers", with "*in
situ* pyrometry to effect real time control" because the chamber never
reaches thermal equilibrium; applications include "dopant activation,
thermal oxidation, metal reflow and chemical vapor
deposition".[^wiki-rtp] A single-wafer RTA chamber uses banks of
tungsten-halogen lamps above (and sometimes below) the wafer, a quartz
window, gas flow of N₂, Ar or O₂, and an optical pyrometer whose reading
must be corrected for the wafer's temperature- and film-dependent
emissivity; ramp rates of 50–250 °C/s are typical industry
values,[^roozeboom-1990] and the trade-offs are "temperature and process
uniformity, temperature measurement and control, and wafer
stress".[^wiki-rtp] Wafers that are heated non-uniformly slip on {111}
planes at the edge, so edge-ring design and lamp zoning matter.
Furnaces, by contrast, hold 100–150 wafers at a uniform temperature for
tens of minutes and are still used where a large Dt is wanted, for
example the well drive-in, or where low temperature and long time are
cheap, for example the alloy anneal.[^wiki-furnace]

### Silicidation

The self-aligned silicide ({term}`salicide`) process "begins with
deposition of a thin transition metal layer over fully formed and
patterned semiconductor devices", the wafer is heated so that the
metal reacts with exposed silicon, and "any remaining transition metal
is removed by chemical etching, leaving silicide contacts in only the
active regions of the device".[^wiki-salicide]
Two anneals are used because the low-resistance phase forms only after
the selective etch:

* **Titanium**: a first RTA at roughly 600–700 °C in N₂ forms the
  metastable C49 TiSi₂ (and TiN on top), the unreacted Ti/TiN is
  stripped in SC-1 or SPM, and a second RTA at roughly 800–900 °C
  converts C49 to the low-resistivity C54 phase; on narrow lines the
  C49→C54 transformation becomes nucleation-limited, the "narrow-line
  effect" that drove the industry to cobalt at the 180–130 nm
  nodes.[^maex-1993][^osburn-1993]
* **Cobalt**: a first anneal at roughly 450–550 °C forms Co₂Si and CoSi,
  the unreacted cobalt (over a Ti or TiN cap) is stripped, and a second
  anneal at roughly 700–800 °C forms CoSi₂, the only cobalt silicide
  with "a sufficiently low resistance to form an effective electrical
  contact".[^wiki-salicide] CoSi₂ consumes about 3.6 nm of silicon per
  nanometre of cobalt,[^maex-1993] so the junction under it must be deep
  enough; ITRS 2001 assumes a silicide thickness of half the contact
  junction depth.[^itrs-01]

Silicide formation and the two-step sequence are done in the same RTP
tools as implant anneals but at lower temperature and in strictly
oxygen-free ambients, since a few ppm of O₂ oxidises the metal before it
can react.

### The alloy anneal

The final anneal is done in forming gas — "typical forming gas
formulations (5% H2 in N2)" — because "a high-temperature anneal in
forming gas assists in silicon-silicon dioxide interface
passivation".[^wiki-fg] At 350–450 °C for 20–30 min hydrogen diffuses
through the stack and ties up the dangling bonds (P_b centres) at the
Si/SiO₂ interface, reducing the interface-trap density and stabilising
the threshold voltage; the same anneal sinters the aluminium–silicon and
titanium–silicide contacts and relaxes stress in the metal (Deal's
terminology for the charges involved is given in his 1980
paper).[^deal-1980][^txt-01] It must be the last hot step because
subsequent plasma exposure would undo the passivation, and its
temperature is capped by the aluminium metallisation (Al–Si eutectic at
577 °C,[^txt-02] and hillock growth well below that).

## Typical equipment

* **Rapid thermal processors**: AG Associates Heatpulse 8108 ("first
  shipped in October 1992" as the "flagship product targeted for volume
  production processes that utilize wafer sizes from 125 to 200
  millimeters"),[^ag-10k] later sold by Steag and Mattson; Applied
  Materials RTP XE Centura (1997)[^amat-1997] and its Radiance and
  Vantage successors (which measure "the temperature 100 times per
  second at seven different places on the wafer");[^amat-rtp] Mattson
  RTP 3000; Kokusai and TEL RTP tools.
* **Vertical furnaces** for well drive, densification and alloy: ASM
  A400,[^asm-vf] TEL Alpha-8, Aviza/Thermco, Kokusai; older horizontal
  Thermco and BTU tubes for alloy.
* **Metrology**: four-point probe sheet resistance after every
  activation anneal, Therma-Wave for lightly doped implants, SIMS for
  profiles, and thermocouple-instrumented wafers for RTP temperature
  calibration.

## Typical consumables

* **Gases**: nitrogen, argon, forming gas (4–10 % H₂ in N₂, "5 % H₂ in
  N₂" being typical),[^wiki-fg] oxygen (as a controlled minor addition
  for some anneals), ammonia for nitridation.
* **RTP hardware**: tungsten-halogen lamps, quartz windows and chambers,
  silicon carbide or quartz edge rings, pyrometer calibration wafers.
* **Furnace hardware**: quartz tubes, boats and baffles; monitor wafers
  (SEMI M8) for sheet resistance.
* **Silicide metals** (Ti, Co, with TiN caps) are consumed at the
  deposition step ({ref}`category-deposition`), and the selective strip
  chemistry (SC-1, SPM) at a clean step ({ref}`category-strip`).

## Steps in this category

| Step | Code | Name |
|------|------|------|
| 34 | {ref}`RTAI <step-034>` | Pre-gate oxide anneal |
| 75 | {ref}`TIPRTAD <step-075>` | RTA tip activation |
| 88 | {ref}`RTAD <step-088>` | RTA source drain implant anneal |
| 92 | {ref}`RTAD2 <step-092>` | RTA source drain anneal |
| 96 | {ref}`ALLY1 <step-096>` | Alloy 1 |
| 98 | {ref}`CSIL <step-098>` | Contact silicidation |
| 170 | {ref}`ALLY <step-170>` | Alloy |

## References

### Cross-check

* Roozeboom and Parekh, *JVST B* 1990 — RTP systems and their ramp
  rates and temperature-control trade-offs.[^roozeboom-1990]
* Maex, *Mater. Sci. Eng. R* 1993 — TiSi₂ and CoSi₂ formation,
  silicon consumption and the narrow-line effect.[^maex-1993]
* Osburn, "Silicides", in Fair (ed.), *Rapid Thermal
  Processing*.[^osburn-1993]
* Fair, "Junction Formation in Silicon by Rapid Thermal Annealing", in
  Fair (ed.), *Rapid Thermal Processing*.[^txt-10]
* ITRS 2001, *Front End Processes* — Table 51 and its notes on
  junctions and silicide thickness.[^itrs-01]
* Plasma-Therm, *AG Heatpulse 8800 / 8108 RTP* product
  spotlight.[^plasmatherm-ag]
* AG Associates, Form 10-K (fiscal 1996) — Heatpulse 8108 first
  shipped October 1992.[^ag-10k]
* Applied Materials, 1997 Annual Report — RTP XE Centura.[^amat-1997]
* EDN, *Applied dedicates RTP with Vantage* — the Radiance/Vantage
  chambers' pyrometry.[^amat-rtp]
* ASM International, *Vertical furnace* product page.[^asm-vf]

### High-level understanding

* Wikipedia, *Rapid thermal processing* — lamps, pyrometry and the
  main trade-offs.[^wiki-rtp]
* Wikipedia, *Furnace anneal*.[^wiki-furnace]
* Wikipedia, *Annealing (materials science)*.[^wiki-annealing]
* Wikipedia, *Fick's laws of diffusion*.[^wiki-fick]
* Wikipedia, *Arrhenius equation*.[^wiki-arrhenius]
* Wikipedia, *Salicide* — the two-anneal self-aligned silicide
  sequence.[^wiki-salicide]
* Wikipedia, *Titanium disilicide*.[^wiki-tisi2]
* Wikipedia, *Forming gas* — the 5 % H₂ in N₂ mixture and interface
  passivation.[^wiki-fg]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — ch. 7
  ("Dopant Diffusion") and ch. 8 ("Ion Implantation").[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  ch. 8 ("Diffusion in Silicon") and ch. 10 ("Rapid Thermal
  Processing").[^txt-02]
* Sze and Lee, *Semiconductor Devices: Physics and Technology* —
  ch. 12.[^sze-2012]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  ch. 3 and 6.[^campbell-2013]

### Deep dive

* Gibbons, *Proc. IEEE* 1972 — damage production and annealing of
  implanted layers.[^gibbons-1972]
* Stolk et al., *JAP* 1997 — physical mechanisms of transient enhanced
  diffusion.[^stolk-1997]
* Michel et al. (IBM), *APL* 1987 — the first report of anomalous
  (transient enhanced) boron diffusion during rapid
  annealing.[^michel-1987]
* Eaglesham et al., *APL* 1994 — the "+1" interstitial source of
  TED.[^eaglesham-1994]
* Jones and Ishida, *Mater. Sci. Eng. R* 1998 — review of shallow
  junction formation by implantation and RTA.[^rev-05]
* Agarwal, Gossmann and Fiory, *J. Electron. Mater.* 1999 — the effect
  of RTA ramp rate on boron ultra-shallow junctions, the case for
  spike anneals.[^agarwal-1999]
* Fiory, *J. Electron. Mater.* 2002 — RTP developments of the 130 nm
  era.[^fiory-2002]
* Sedgwick, *JES* 1983 — an early review of short-time
  annealing.[^sedgwick-1983]
* Csepregi et al., *JAP* 1978 — solid-phase epitaxial regrowth rates of
  amorphised silicon versus orientation.[^csepregi-1978]
* Zhang and Östling, *Crit. Rev. Solid State Mater. Sci.* 2003 —
  review of TiSi₂, CoSi₂ and NiSi salicide technology.[^rev-04]
* Mann and Clevenger (IBM), *JES* 1994 — the C49-to-C54 TiSi₂ phase
  transformation and its nucleation limit on narrow
  lines.[^mann-1994]
* Murarka, *Silicides for VLSI Applications* — ch. "Formation", the
  classic text on silicide reaction kinetics.[^murarka-1983]
* Cartier, Stathis and Buchanan (IBM), *APL* 1993 — hydrogen
  passivation and depassivation of interface dangling
  bonds.[^cartier-1993]
* Reed and Plummer, *JAP* 1988 — the chemistry of Si/SiO₂ interface-trap
  annealing in hydrogen.[^reed-1988]
* Deal, *JES* 1980 — the standard terminology for the oxide charges
  affected by the alloy anneal.[^deal-1980]
* Gronet and Gibbons (Applied Materials), US 5,155,336 — a lamp-heated
  single-wafer RTP chamber design.[^pat-rtp-amat]
* Sheets (Tamarack Scientific), US 4,649,261 — an early lamp annealer
  for silicide formation and reflow.[^pat-rtp-tamarack]
* MIT OpenCourseWare 6.774 — lecture notes on diffusion, TED and
  rapid thermal annealing.[^ocw-6774]

<!-- footnotes -->

[^wiki-fick]: Wikipedia, *Fick's laws of diffusion*.
    <https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion>
[^wiki-arrhenius]: Wikipedia, *Arrhenius equation*.
    <https://en.wikipedia.org/wiki/Arrhenius_equation>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^gibbons-1972]: J. F. Gibbons, "Ion implantation in semiconductors —
    Part II: Damage production and annealing", *Proceedings of the IEEE*
    **60**(9), 1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
[^stolk-1997]: P. A. Stolk, H.-J. Gossmann, D. J. Eaglesham, D. C.
    Jacobson, C. S. Rafferty, G. H. Gilmer, M. Jaraíz, J. M. Poate, H.
    S. Luftman and T. E. Haynes, "Physical mechanisms of transient
    enhanced dopant diffusion in ion-implanted silicon", *Journal of
    Applied Physics* **81**(9), 6031–6050 (1997).
    <https://doi.org/10.1063/1.364452>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^wiki-rtp]: Wikipedia, *Rapid thermal processing*.
    <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
[^roozeboom-1990]: F. Roozeboom and N. Parekh, "Rapid thermal processing
    systems: A review with emphasis on temperature control", *Journal of
    Vacuum Science & Technology B* **8**(6), 1249–1259 (1990).
    <https://doi.org/10.1116/1.584902>
[^wiki-furnace]: Wikipedia, *Furnace anneal*.
    <https://en.wikipedia.org/wiki/Diffusion_furnace>
[^wiki-salicide]: Wikipedia, *Salicide*.
    <https://en.wikipedia.org/wiki/Salicide>
[^maex-1993]: K. Maex, "Silicides for integrated circuits: TiSi₂ and
    CoSi₂", *Materials Science and Engineering: R* **11**(2–3), vii–153
    (1993). <https://doi.org/10.1016/0927-796X(93)90001-J>
[^osburn-1993]: C. M. Osburn, "Silicides", in R. B. Fair (ed.), *Rapid
    Thermal Processing: Science and Technology*, Academic Press, 1993,
    pp. 227–309. <https://doi.org/10.1016/b978-0-12-247690-7.50010-x>
[^wiki-fg]: Wikipedia, *Forming gas*.
    <https://en.wikipedia.org/wiki/Forming_gas>
[^deal-1980]: B. E. Deal, "Standardized terminology for oxide charges
    associated with thermally oxidized silicon", *IEEE Transactions on
    Electron Devices* **27**(3), 606–608 (1980),
    DOI 10.1109/T-ED.1980.19908; published simultaneously in *Journal of
    The Electrochemical Society* **127**(4), 979–981 (1980).
    <https://doi.org/10.1109/T-ED.1980.19908>,
    <https://doi.org/10.1149/1.2129800>
[^ag-10k]: AG Associates, Inc., Form 10-K for the fiscal year ended
    1996-09-30, filed 1996-12-23 (Heatpulse 8108 first shipped October
    1992; 125–200 mm).
    <https://www.sec.gov/Archives/edgar/data/942124/000089161896003159/0000891618-96-003159.txt>
[^amat-1997]: Applied Materials, Inc., *1997 Annual Report*.
    <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
[^amat-rtp]: EDN, *Applied dedicates RTP with Vantage*, 2002-09-23
    (Applied Materials Radiance/Vantage RTP chambers).
    <https://www.edn.com/applied-dedicates-rtp-with-vantage/>
[^asm-vf]: ASM International, *Vertical furnace*, product page.
    <https://www.asm.com/our-technology-products/vertical-furnace>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7; R. B.
    Fair, "Junction Formation in Silicon by Rapid Thermal Annealing",
    pp. 169–226. <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
[^plasmatherm-ag]: Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 /
    8108 RTP*, blog post.
    <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
[^wiki-annealing]: Wikipedia, *Annealing (materials science)*.
    <https://en.wikipedia.org/wiki/Annealing_(materials_science)>
[^wiki-tisi2]: Wikipedia, *Titanium disilicide*.
    <https://en.wikipedia.org/wiki/Titanium_disilicide>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^sze-2012]: S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics
    and Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7.
    <https://www.wiley.com/en-us/Semiconductor+Devices%3A+Physics+and+Technology%2C+3rd+Edition-p-9780470537947>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^michel-1987]: A. E. Michel, W. Rausch, P. A. Ronsheim and R. H. Kastl,
    "Rapid annealing and the anomalous diffusion of ion implanted boron
    into silicon", *Applied Physics Letters* **50**(7), 416–418 (1987).
    <https://doi.org/10.1063/1.98160>
[^eaglesham-1994]: D. J. Eaglesham, P. A. Stolk, H.-J. Gossmann and J.
    M. Poate, "Implantation and transient B diffusion in Si: The source
    of the interstitials", *Applied Physics Letters* **65**(18),
    2305–2307 (1994). <https://doi.org/10.1063/1.112725>
[^rev-05]: E. C. Jones and E. Ishida, "Shallow junction doping
    technologies for ULSI", *Materials Science and Engineering: R*
    **24**(1–2), 1–80 (1998).
    <https://doi.org/10.1016/S0927-796X(98)00013-8>
[^agarwal-1999]: A. Agarwal, H.-J. Gossmann and A. T. Fiory, "Effect of
    ramp rates during rapid thermal annealing of ion implanted boron for
    formation of ultra-shallow junctions", *Journal of Electronic
    Materials* **28**(12), 1333–1339 (1999).
    <https://doi.org/10.1007/s11664-999-0118-7>
[^fiory-2002]: A. T. Fiory, "Recent developments in rapid thermal
    processing", *Journal of Electronic Materials* **31**(10), 981–987
    (2002). <https://doi.org/10.1007/s11664-002-0031-9>
[^sedgwick-1983]: T. O. Sedgwick, "Short Time Annealing", *Journal of
    The Electrochemical Society* **130**(2), 484–493 (1983).
    <https://doi.org/10.1149/1.2119736>
[^csepregi-1978]: L. Csepregi, E. F. Kennedy, J. W. Mayer and T. W.
    Sigmon, "Substrate-orientation dependence of the epitaxial regrowth
    rate from Si-implanted amorphous Si", *Journal of Applied Physics*
    **49**(7), 3906–3911 (1978). <https://doi.org/10.1063/1.325397>
[^rev-04]: S.-L. Zhang and M. Östling, "Metal Silicides in CMOS
    Technology: Past, Present, and Future Trends", *Critical Reviews in
    Solid State and Materials Sciences* **28**(1), 1–129 (2003).
    <https://doi.org/10.1080/10408430390802431>
[^mann-1994]: R. W. Mann and L. A. Clevenger, "The C49 to C54 Phase
    Transformation in TiSi₂ Thin Films", *Journal of The Electrochemical
    Society* **141**(5), 1347–1350 (1994).
    <https://doi.org/10.1149/1.2054921>
[^murarka-1983]: S. P. Murarka, "Formation", in *Silicides for VLSI
    Applications*, Academic Press, 1983, pp. 99–131.
    <https://doi.org/10.1016/b978-0-08-057056-3.50009-4>
[^cartier-1993]: E. Cartier, J. H. Stathis and D. A. Buchanan,
    "Passivation and depassivation of silicon dangling bonds at the
    Si/SiO₂ interface by atomic hydrogen", *Applied Physics Letters*
    **63**(11), 1510–1512 (1993). <https://doi.org/10.1063/1.110758>
[^reed-1988]: M. L. Reed and J. D. Plummer, "Chemistry of Si-SiO₂
    interface trap annealing", *Journal of Applied Physics* **63**(12),
    5776–5793 (1988). <https://doi.org/10.1063/1.340317>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials),
    *Rapid thermal heating apparatus and method*, US 5,155,336 A,
    granted 1992-10-13.
    <https://patents.google.com/patent/US5155336A/en>
[^pat-rtp-tamarack]: R. E. Sheets (Tamarack Scientific), *Apparatus for
    heating semiconductor wafers in order to achieve annealing, silicide
    formation, reflow of glass passivation layers, etc.*, US 4,649,261
    A, granted 1987-03-10.
    <https://patents.google.com/patent/US4649261A/en>
[^ocw-6774]: MIT OpenCourseWare, *6.774 Physics of Microfabrication:
    Front End Processing*, Fall 2004 (lecture notes on oxidation,
    diffusion, implantation and annealing).
    <https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/>
