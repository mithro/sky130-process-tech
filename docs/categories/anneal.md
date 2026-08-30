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
* **Alloy (sinter)** — a 350–450 °C anneal in {term}`forming gas`
  after contact formation ({ref}`ALLY1 <step-096>`) and after the last
  metal ({ref}`ALLY <step-170>`).
* Purely by association, the PSG densification, ILD bakes and the like
  are treated as part of the deposition steps.

## Physics and engineering background

### Diffusion

Dopant movement during an anneal is governed by Fick's laws,
{math}`J = -D\,\partial C/\partial x` and
{math}`\partial C/\partial t = D\,\partial^2 C/\partial x^2`
([Wikipedia: Fick's laws of diffusion][wiki-fick]), with a diffusivity
that follows the Arrhenius law {math}`D = D_0 e^{-E_A/kT}`
([Wikipedia: Arrhenius equation][wiki-arrhenius]). For the common
dopants in silicon the activation energies are of order 3–4 eV, so
diffusion is negligible below about 800 °C and doubles roughly every
20–30 °C above it; a Gaussian implanted profile broadens such that its
characteristic width grows as {math}`\sqrt{2Dt}`, and the product
{math}`Dt` summed over every hot step is the process's "thermal
budget" (Plummer, Deal and Griffin, ch. 7). At the concentrations used
for wells and channels, diffusion is intrinsic; at source/drain
concentrations it is enhanced by the Fermi-level dependence of the
point-defect populations, and phosphorus and boron diffuse mainly via
interstitials while arsenic and antimony use vacancies.

### Activation and damage annealing

Implanted dopant is electrically inactive until the lattice is
restored. Amorphised layers regrow by solid-phase epitaxy at 500–600 °C
with the dopant incorporated substitutionally up to and beyond its
equilibrium solid solubility; partially damaged layers need
800–1000 °C to dissolve the defect clusters ([Gibbons 1972][gibbons2];
Plummer, Deal and Griffin, ch. 8). Two effects make the choice of
anneal a compromise. Above the solid solubility the dopant
precipitates or clusters and deactivates, so the highest activation is
obtained by annealing hot and fast. And the interstitials released as
the damage anneals cause transient enhanced diffusion ({term}`TED`),
which is worst for slow, low-temperature anneals because the damage
dissolves while the dopant is still mobile ([Stolk et al. 1997][stolk]).
The resolution is the RTA: seconds at 1000–1100 °C, or a "spike" anneal
with essentially zero soak time, which activates the dopant while the
junction moves only a few nanometres. ITRS 2001 identifies the boron
extension junction as the critical one and asks for its depth,
abruptness and sheet resistance to be met simultaneously
([ITRS 2001, Front End Processes][itrs2001-fep]).

### Rapid thermal processing

RTP "heats silicon wafers to temperatures exceeding 1,000°C for not
more than a few seconds" using "high intensity lamps or lasers", with
"*in situ* pyrometry to effect real time control" because the chamber
never reaches thermal equilibrium; applications include "dopant
activation, thermal oxidation, metal reflow and chemical vapor
deposition" ([Wikipedia: Rapid thermal processing][wiki-rtp]). A
single-wafer RTA chamber uses banks of tungsten-halogen lamps above (and
sometimes below) the wafer, a quartz window, gas flow of N₂, Ar or
O₂, and an optical pyrometer whose reading must be corrected for the
wafer's temperature- and film-dependent emissivity; ramp rates of
50–250 °C/s are typical, and the trade-offs are "temperature and
process uniformity, temperature measurement and control, and wafer
stress" ([Wikipedia: Rapid thermal processing][wiki-rtp]; [Roozeboom
and Parekh 1990][roozeboom]). Wafers that are heated non-uniformly
slip on {111} planes at the edge, so edge-ring design and lamp
zoning matter. Furnaces, by contrast, hold 100–150 wafers at a uniform
temperature for tens of minutes and are still used where a large Dt is
wanted, for example the well drive-in, or where low temperature and
long time are cheap, for example the alloy anneal
([Wikipedia: Furnace anneal][wiki-furnace]).

### Silicidation

The self-aligned silicide ({term}`salicide`) process "begins with
deposition of a thin transition metal layer over fully formed and
patterned semiconductor devices", the wafer is heated so that the
metal reacts with exposed silicon, and "any remaining transition metal
is removed by chemical etching, leaving silicide contacts in only the
active regions of the device" ([Wikipedia: Salicide][wiki-salicide]).
Two anneals are used because the low-resistance phase forms only after
the selective etch:

* **Titanium**: a first RTA at roughly 600–700 °C in N₂ forms the
  metastable C49 TiSi₂ (and TiN on top), the unreacted Ti/TiN is
  stripped in SC-1 or SPM, and a second RTA at roughly 800–900 °C
  converts C49 to the low-resistivity C54 phase; on narrow lines the
  C49→C54 transformation becomes nucleation-limited, the "narrow-line
  effect" that drove the industry to cobalt at the 180–130 nm nodes
  ([Maex 1993][maex]; Osburn in Fair [osburn]).
* **Cobalt**: a first anneal at roughly 450–550 °C forms Co₂Si and
  CoSi, the unreacted cobalt (over a Ti or TiN cap) is stripped, and a
  second anneal at roughly 700–800 °C forms CoSi₂, the only cobalt
  silicide with "a sufficiently low resistance to form an effective
  electrical contact" ([Wikipedia: Salicide][wiki-salicide]). CoSi₂
  consumes about 3.6 nm of silicon per nanometre of cobalt
  ([Maex 1993][maex]), so the junction under it must be deep
  enough; ITRS 2001 assumes a silicide thickness of half the contact
  junction depth ([ITRS 2001, Front End Processes][itrs2001-fep]).

Silicide formation and the two-step sequence are done in the same RTP
tools as implant anneals but at lower temperature and in strictly
oxygen-free ambients, since a few ppm of O₂ oxidises the metal before it
can react.

### The alloy anneal

The final anneal is done in forming gas — "typical forming gas
formulations (5% H2 in N2)" — because "a high-temperature anneal in
forming gas assists in silicon-silicon dioxide interface passivation"
([Wikipedia: Forming gas][wiki-fg]). At 350–450 °C for 20–30 min
hydrogen diffuses through the stack and ties up the dangling bonds
(P_b centres) at the Si/SiO₂ interface, reducing the interface-trap
density and stabilising the threshold voltage; the same anneal sinters
the aluminium–silicon and titanium–silicide contacts and relaxes stress
in the metal (Deal's terminology for the charges involved is in
[Deal 1980][deal1980]; Plummer, Deal and Griffin, ch. 6). It must be
the last hot step because subsequent plasma exposure would undo the
passivation, and its temperature is capped by the aluminium
metallisation (Al–Si eutectic at 577 °C, and hillock growth well
below that).

## Typical equipment

* **Rapid thermal processors**: AG Associates Heatpulse 8108 ("first
  shipped in October 1992" as the "flagship product targeted for
  volume production processes that utilize wafer sizes from 125 to 200
  millimeters" [ag-10k]), later sold by Steag and Mattson; Applied
  Materials RTP XE Centura (1997 [amat-1997]) and its Radiance and
  Vantage successors (which measure "the temperature 100 times per
  second at seven different places on the wafer" [amat-rtp]); Mattson
  RTP 3000; Kokusai and TEL RTP tools.
* **Vertical furnaces** for well drive, densification and alloy: ASM
  A400 ([ASM vertical furnace][asm-vf]), TEL Alpha-8, Aviza/Thermco,
  Kokusai; older horizontal Thermco and BTU tubes for alloy.
* **Metrology**: four-point probe sheet resistance after every
  activation anneal, Therma-Wave for lightly doped implants, SIMS for
  profiles, and thermocouple-instrumented wafers for RTP temperature
  calibration.

## Typical consumables

* **Gases**: nitrogen, argon, forming gas (4–10 % H₂ in N₂, "5 % H₂ in
  N₂" being typical [wiki-fg]), oxygen (as a controlled minor
  addition for some anneals), ammonia for nitridation.
* **RTP hardware**: tungsten-halogen lamps, quartz windows and chambers,
  silicon carbide or quartz edge rings, pyrometer calibration wafers.
* **Furnace hardware**: quartz tubes, boats and baffles; monitor wafers
  (SEMI M8) for sheet resistance.
* **Silicide metals** (Ti, Co, with TiN caps) are consumed at the
  deposition step ({ref}`category-deposition`), and the selective
  strip chemistry (SC-1, SPM) at a clean step ({ref}`category-strip`).

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

* F. Roozeboom and N. Parekh, "Rapid thermal processing systems: A
  review with emphasis on temperature control", *Journal of Vacuum
  Science and Technology B* **8**, 1249–1259 (1990).
  <https://doi.org/10.1116/1.584902>
* K. Maex, "Silicides for integrated circuits: TiSi₂ and CoSi₂",
  *Materials Science and Engineering R* **11**, vii–153 (1993).
  <https://doi.org/10.1016/0927-796X(93)90001-J>
* C. M. Osburn, "Silicides", in R. B. Fair (ed.), *Rapid Thermal
  Processing: Science and Technology*, Academic Press, 1993.
  <https://doi.org/10.1016/b978-0-12-247690-7.50010-x>
* R. B. Fair, "Junction Formation in Silicon by Rapid Thermal
  Annealing", in R. B. Fair (ed.), *Rapid Thermal Processing: Science
  and Technology*, Academic Press, 1993.
  <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
* *ITRS 2001 Edition: Front End Processes* (Table 51 and notes).
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* Plasma-Therm, "Product Spotlight: AG Heatpulse 8800 / 8108 RTP".
  <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
* AG Associates, Inc., Form 10-K for the fiscal year ended 1996-09-30,
  filed 1996-12-23 (Heatpulse 8108 first shipped October 1992;
  125–200 mm).
  <https://www.sec.gov/Archives/edgar/data/942124/000089161896003159/0000891618-96-003159.txt>
* Applied Materials, 1997 Annual Report (RTP XE Centura).
  <https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf>
* EDN, "Applied dedicates RTP with Vantage".
  <https://www.edn.com/applied-dedicates-rtp-with-vantage/>
* ASM International, "Vertical furnace".
  <https://www.asm.com/our-technology-products/vertical-furnace>

### High-level

* Wikipedia, "Rapid thermal processing".
  <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
* Wikipedia, "Furnace anneal".
  <https://en.wikipedia.org/wiki/Diffusion_furnace>
* Wikipedia, "Annealing (materials science)".
  <https://en.wikipedia.org/wiki/Annealing_(materials_science)>
* Wikipedia, "Fick's laws of diffusion".
  <https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion>
* Wikipedia, "Arrhenius equation".
  <https://en.wikipedia.org/wiki/Arrhenius_equation>
* Wikipedia, "Salicide". <https://en.wikipedia.org/wiki/Salicide>
* Wikipedia, "Titanium disilicide".
  <https://en.wikipedia.org/wiki/Titanium_disilicide>
* Wikipedia, "Forming gas". <https://en.wikipedia.org/wiki/Forming_gas>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 7
  ("Dopant Diffusion") and ch. 8 ("Ion Implantation").
* S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
  Vol. 1*, 2nd ed., Lattice Press, 2000, ISBN 978-0-9616721-6-4,
  ch. 8 ("Diffusion in Silicon") and ch. 10 ("Rapid Thermal
  Processing").
* S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics and
  Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7, ch. 12.
* S. A. Campbell, *Fabrication Engineering at the Micro- and
  Nanoscale*, 4th ed., Oxford University Press, 2013,
  ISBN 978-0-19-986122-4, ch. 3 and 6.

### Deep dive

* J. F. Gibbons, "Ion implantation in semiconductors — Part II: Damage
  production and annealing", *Proceedings of the IEEE* **60**(9),
  1062–1096 (1972). <https://doi.org/10.1109/PROC.1972.8854>
* P. A. Stolk et al., "Physical mechanisms of transient enhanced
  dopant diffusion in ion-implanted silicon", *Journal of Applied
  Physics* **81**, 6031–6050 (1997). <https://doi.org/10.1063/1.364452>
* B. E. Deal, "Standardized Terminology for Oxide Charges Associated
  with Thermally Oxidized Silicon", *Journal of the Electrochemical
  Society* **127**, 979–981 (1980). <https://doi.org/10.1149/1.2129800>
* S. P. Murarka, *Silicides for VLSI Applications*, Academic Press,
  1983 (ch. "Formation").
  <https://doi.org/10.1016/b978-0-08-057056-3.50009-4>

[wiki-fick]: https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion
[wiki-arrhenius]: https://en.wikipedia.org/wiki/Arrhenius_equation
[wiki-rtp]: https://en.wikipedia.org/wiki/Rapid_thermal_processing
[wiki-furnace]: https://en.wikipedia.org/wiki/Diffusion_furnace
[wiki-salicide]: https://en.wikipedia.org/wiki/Salicide
[wiki-fg]: https://en.wikipedia.org/wiki/Forming_gas
[gibbons2]: https://doi.org/10.1109/PROC.1972.8854
[stolk]: https://doi.org/10.1063/1.364452
[roozeboom]: https://doi.org/10.1116/1.584902
[maex]: https://doi.org/10.1016/0927-796X(93)90001-J
[osburn]: https://doi.org/10.1016/b978-0-12-247690-7.50010-x
[deal1980]: https://doi.org/10.1149/1.2129800
[itrs2001-fep]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf
[ag-8108]: https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp
[ag-10k]: https://www.sec.gov/Archives/edgar/data/942124/000089161896003159/0000891618-96-003159.txt
[amat-1997]: https://www.annualreports.com/HostedData/AnnualReportArchive/a/NASDAQ_AMAT_1997.pdf
[amat-rtp]: https://www.edn.com/applied-dedicates-rtp-with-vantage/
[asm-vf]: https://www.asm.com/our-technology-products/vertical-furnace
