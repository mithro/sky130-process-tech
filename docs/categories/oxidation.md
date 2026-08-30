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
give the target thickness ([Wikipedia: Thermal oxidation][wiki-thox]).
For every unit thickness of silicon consumed, 2.17 unit thicknesses of
oxide appear, so "46% of the oxide thickness will lie below the
original surface, and 54% above it" ([Wikipedia: Thermal
oxidation][wiki-thox]).

In the SKY130 flow the oxidation steps are the pad oxide under the STI
nitride ({ref}`BOX <step-002>`), the trench-liner oxidation
({ref}`LINOX <step-010>`), the tunnel-oxide/{term}`ONO` stack of the
SONOS memory transistor ({ref}`ONO <step-040>`), the two gate
oxidations for the thick-oxide and thin-oxide transistors
({ref}`GOX100 <step-043>`, {ref}`LVGOX <step-047>`) and a
post-gate-etch re-oxidation ({ref}`IOX45 <step-063>`).

## Physics and engineering background

### The Deal–Grove model

Deal and Grove (1965) showed that oxidation proceeds by the oxidant
diffusing *through* the existing oxide to react at the Si/SiO₂
interface, and that a steady-state flux balance gives the
linear–parabolic law ([Deal and Grove 1965][deal-grove])

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
parameters below for single-crystal silicon
([Wikipedia: Deal–Grove model][wiki-dg]):

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
required (Plummer, Deal and Griffin, ch. 6).

### The thin-oxide regime

The Deal–Grove model under-predicts growth for the first 20–30 nm of
dry oxide: "very thin oxides (less than about 25 nanometres) grow much
more quickly in O₂ than the model predicts" ([Wikipedia:
Deal–Grove model][wiki-dg]). Massoud, Plummer and Irene characterised
this enhancement and added exponentially decaying rate terms to fit it
([Massoud, Plummer and Irene 1985][massoud]). This is exactly the
regime in which gate oxides for 1.8 V and 5 V transistors are grown, so
gate-oxide recipes are calibrated empirically on the tool rather than
taken from the model. Practical calculators implementing Deal–Grove
with Massoud corrections are available online ([BYU oxide growth
calculator][byu]).

### Oxide charge and quality

Deal's standard terminology distinguishes fixed oxide charge
{math}`Q_f`, interface-trapped charge {math}`Q_{it}`, oxide-trapped
charge {math}`Q_{ot}` and mobile ionic charge {math}`Q_m`
([Deal 1980][deal1980]). Fixed charge and interface traps are lowest on
(100) silicon and after a post-oxidation anneal in inert gas; mobile
sodium is immobilised by adding chlorine, which "is often introduced by
adding hydrogen chloride or trichloroethylene to the oxidizing medium"
([Wikipedia: Thermal oxidation][wiki-thox]). Wet oxides have "more
dangling bonds at the silicon interface" and lower density, so thick
oxides "are usually grown with a long wet oxidation bracketed by short
dry ones (a dry-wet-dry cycle)" ([Wikipedia: Thermal oxidation][wiki-thox]).
The final hydrogen passivation of interface traps is done much later,
at the {term}`alloy anneal` ({ref}`category-anneal`).

### Nitrided oxides and ONO stacks

By the 130 nm node most gate oxides were lightly nitrided, either by
growing in N₂O or NO, or by a plasma or thermal nitridation after
growth. Nitrogen near the top interface blocks boron penetration from
the p⁺ poly gate and raises the dielectric constant slightly; the ITRS
2001 expected "evolution of the oxynitride gate dielectric materials"
to continue until high-κ materials matured ([ITRS 2001, Front End
Processes][itrs2001-fep]). For the SONOS memory transistor, a very thin
tunnel oxide is grown, a charge-trapping silicon nitride deposited by
{term}`LPCVD`, and a blocking oxide formed on top by oxidising the
nitride or depositing an oxide — the oxide–nitride–oxide ({term}`ONO`)
stack ([Wikipedia: SONOS][wiki-sonos]).

### Thin gate oxide versus thick field oxide

Two very different thickness regimes appear in a CMOS flow:

* **Gate oxides** of a few nanometres. ITRS 2001 lists an equivalent
  oxide thickness of 2.0–2.4 nm for low-operating-power and 2.4–2.8 nm
  for low-standby-power logic at the 130 nm node, and 5 nm for DRAM
  transfer devices; input/output transistors that must withstand 2.5 V,
  3.3 V or 5 V use proportionally thicker oxides
  ([ITRS 2001, Front End Processes][itrs2001-fep]). These are grown
  dry, often with a nitridation, at 750–950 °C, in a furnace or an
  RTP chamber, to a thickness controlled to within a few per cent
  (ITRS 2001 asks for EOT control of ±4 % 3σ
  [itrs2001-fep]).
* **Pad, liner and screen oxides** of 5–30 nm, grown dry or wet, whose
  job is mechanical or chemical: cushioning the stress of an LPCVD
  nitride, rounding trench corners and passivating trench sidewalls,
  or scattering implanted ions to reduce {term}`channelling`
  (Plummer, Deal and Griffin, ch. 6 and 8).
* **Field oxides** of hundreds of nanometres. In {term}`LOCOS`
  isolation these were grown wet at 900–1000 °C through a nitride
  mask; at 250 nm and below the industry moved to {term}`STI`, in which
  the thick isolation oxide is *deposited* ({ref}`category-deposition`)
  and only a thin liner is grown ([Wikipedia: Shallow trench
  isolation][wiki-sti]). SKY130 uses STI.

### Dual gate oxide processes

A process with both 1.8 V and 5 V transistors grows its gate oxides in
two passes: a first, thicker oxide everywhere; a mask and wet etch to
strip it from the low-voltage active areas ({ref}`LVOM <step-044>`,
{ref}`GOXETCH <step-046>`); then a second, thin oxidation that also
adds slightly to the remaining thick oxide. The thick oxide's final
thickness is therefore the first growth plus a Deal–Grove increment
from the second growth, and both must be modelled together
(Plummer, Deal and Griffin, ch. 6).

### Furnace versus RTP and ISSG

Batch furnaces oxidise 100–150 wafers at once with excellent thickness
uniformity but a thermal budget of tens of minutes at temperature;
single-wafer rapid-thermal oxidation (RTO) trades throughput for a
budget of seconds and the ability to switch ambient between steps. In
{term}`ISSG`, hydrogen and oxygen are injected into a reduced-pressure
RTP chamber and react at the hot wafer, generating steam and atomic
oxygen in situ; the resulting oxide is grown quickly and uniformly, and
the process is used for trench-liner and gate oxides where corner
rounding or nitride re-oxidation is wanted
(Nishi and Doering, ch. on thermal processing [nishi]).

## Typical equipment

* **Vertical batch furnaces** for 200 mm wafers, with quartz tube,
  quartz boat, load-lock or nitrogen-purged loading, mass-flow
  controlled O₂/H₂/N₂/HCl (or DCE) delivery and, for wet oxidation, a
  pyrogenic torch burning H₂ in O₂ ahead of the tube. Representative
  tools: ASM A400 series (the original A400 has "more than 1000
  reactors shipped" and covers "wet oxidation and anneal processes"
  ([ASM A400 DUO press release][asm-a400]; [ASM vertical furnace][asm-vf]);
  TEL Alpha-8 series; and the Aviza/Thermco (formerly Silicon Valley
  Group) vertical furnaces of the same era.
* **Rapid thermal processors** for RTO and ISSG: AG Associates
  Heatpulse 8108 (first shipped in 1992 and "targeted for volume
  production processes that utilize wafer sizes from 125 to 200
  millimeters" [ag-8108]), Applied Materials Centura RTP
  (Radiance/Vantage chambers [amat-rtp]), Mattson (which absorbed the
  Steag and AG Associates RTP lines).
* **Metrology**: spectroscopic ellipsometers (KLA-Tencor, Rudolph,
  Nanometrics) for thickness and refractive index; C–V and I–V test
  structures at {ref}`category-test` for electrical thickness and
  breakdown.

## Typical consumables

* Oxygen (O₂), hydrogen (H₂) for pyrogenic steam or ISSG, nitrogen
  (N₂) for purge and anneal, all at semiconductor purity (99.9999 %
  or better).
* Chlorine sources: anhydrous HCl, or trans-1,2-dichloroethylene (DCE,
  which replaced trichloroethane) for sodium gettering.
* N₂O or NO for oxynitride gate dielectrics; NH₃ for nitridation.
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

## References

### Cross-check

* B. E. Deal and A. S. Grove, "General Relationship for the Thermal
  Oxidation of Silicon", *Journal of Applied Physics* **36**, 3770–3778
  (1965). <https://doi.org/10.1063/1.1713945>
* H. Z. Massoud, J. D. Plummer and E. A. Irene, "Thermal Oxidation of
  Silicon in Dry Oxygen: Growth-Rate Enhancement in the Thin Regime",
  *Journal of the Electrochemical Society* **132**, 2685–2693 (1985).
  <https://doi.org/10.1149/1.2113648>
* B. E. Deal, "Standardized Terminology for Oxide Charges Associated
  with Thermally Oxidized Silicon", *Journal of the Electrochemical
  Society* **127**, 979–981 (1980). <https://doi.org/10.1149/1.2129800>
* *ITRS 2001 Edition: Front End Processes* (Tables 51 and 52, gate
  dielectric requirements). <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
* ASM International, "ASM International N.V. launches A400 DUO
  vertical furnace system", press release, 2019-11-11.
  <https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469>
* Plasma-Therm, "Product Spotlight: AG Heatpulse 8800 / 8108 RTP".
  <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>

### High-level

* Wikipedia, "Thermal oxidation".
  <https://en.wikipedia.org/wiki/Thermal_oxidation>
* Wikipedia, "Deal–Grove model".
  <https://en.wikipedia.org/wiki/Deal%E2%80%93Grove_model>
* Wikipedia, "Gate oxide". <https://en.wikipedia.org/wiki/Gate_oxide>
* Wikipedia, "LOCOS". <https://en.wikipedia.org/wiki/LOCOS>
* Wikipedia, "Shallow trench isolation".
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* Wikipedia, "SONOS". <https://en.wikipedia.org/wiki/SONOS>
* Wikipedia, "Rapid thermal processing".
  <https://en.wikipedia.org/wiki/Rapid_thermal_processing>
* Brigham Young University Cleanroom, "Oxide Growth Calculator"
  (Deal–Grove with thin-oxide correction).
  <https://cleanroom.byu.edu/oxidetimecalc>
* J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
  Technology*, Prentice Hall, 2000, ISBN 978-0-13-085037-9, ch. 6
  ("Thermal Oxidation and the Si/SiO₂ Interface").
* S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI Era,
  Vol. 1*, 2nd ed., Lattice Press, 2000, ISBN 978-0-9616721-6-4,
  ch. 7 ("Thermal Oxidation of Single-Crystal Silicon").
* S. M. Sze and M. K. Lee, *Semiconductor Devices: Physics and
  Technology*, 3rd ed., Wiley, 2012, ISBN 978-0-470-53794-7, ch. 11.
  <https://www.wiley.com/en-us/Semiconductor+Devices%3A+Physics+and+Technology%2C+3rd+Edition-p-9780470537947>
* S. A. Campbell, *Fabrication Engineering at the Micro- and
  Nanoscale*, 4th ed., Oxford University Press, 2013,
  ISBN 978-0-19-986122-4, ch. 4.
* H. Xiao, *Introduction to Semiconductor Manufacturing Technology*,
  2nd ed., SPIE Press, 2012, ch. 5. <https://doi.org/10.1117/3.924283>

### Deep dive

* J. R. Ligenza and W. G. Spitzer, "The mechanisms for silicon
  oxidation in steam and oxygen", *Journal of Physics and Chemistry of
  Solids* **14**, 131–136 (1960).
  <https://doi.org/10.1016/0022-3697(60)90219-5>
* F. Roozeboom and N. Parekh, "Rapid thermal processing systems: A
  review with emphasis on temperature control", *Journal of Vacuum
  Science and Technology B* **8**, 1249–1259 (1990).
  <https://doi.org/10.1116/1.584902>
* Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
  Manufacturing Technology*, 2nd ed., CRC Press, 2007.
  <https://doi.org/10.1201/9781420017663>
* EDN, "Applied dedicates RTP with Vantage" (Applied Materials
  Radiance/Vantage RTP chambers).
  <https://www.edn.com/applied-dedicates-rtp-with-vantage/>

[wiki-thox]: https://en.wikipedia.org/wiki/Thermal_oxidation
[wiki-dg]: https://en.wikipedia.org/wiki/Deal%E2%80%93Grove_model
[wiki-sti]: https://en.wikipedia.org/wiki/Shallow_trench_isolation
[wiki-sonos]: https://en.wikipedia.org/wiki/SONOS
[deal-grove]: https://doi.org/10.1063/1.1713945
[massoud]: https://doi.org/10.1149/1.2113648
[deal1980]: https://doi.org/10.1149/1.2129800
[byu]: https://cleanroom.byu.edu/oxidetimecalc
[itrs2001-fep]: https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf
[asm-a400]: https://www.asm.com/press-releases/asm-international-nv-launches-a400-duo-vertical-furnace-system-1944469
[asm-vf]: https://www.asm.com/our-technology-products/vertical-furnace
[ag-8108]: https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp
[amat-rtp]: https://www.edn.com/applied-dedicates-rtp-with-vantage/
[nishi]: https://doi.org/10.1201/9781420017663
