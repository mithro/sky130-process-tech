(step-048)=
# Step 048 — SAGD: Single a-Si gate deposition

| | |
|---|---|
| **Step number** | 48 of 171 |
| **Step code** | `SAGD` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — gate and poly resistors |
| **Previous step** | {ref}`LVGOX <step-047>` |
| **Next step** | {ref}`RPM <step-049>` |

## What this step is

`SAGD` deposits the film that becomes every transistor gate and every
poly resistor in SKY130: a single blanket layer of amorphous silicon
(a-Si), laid down by low-pressure chemical vapour deposition (LPCVD)
from silane over the freshly grown gate oxides of
{ref}`GOX100 <step-043>` and {ref}`LVGOX <step-047>`, the ONO stack of
the SONOS cells ({ref}`ONO <step-040>`) and the field oxide. The film is
undoped as deposited; it receives its doping from the implants that
follow ({ref}`P1I <step-050>` for the gates, {ref}`PRI <step-053>` and
{ref}`UPRI <step-056>` for the resistors), is capped
({ref}`GATENIT <step-058>`, {ref}`POC <step-059>`) and is patterned at
{ref}`P1M <step-061>`/{ref}`P1ME <step-062>`. Although it is deposited
amorphous, the film crystallises into polysilicon during the thermal
steps that follow, which is why the PDK calls the layer simply "poly".

The public numbers are few but firm. The PDK's assumptions table gives
a "poly thickness" of 0.18 µm,[^pdk-03] and the process stack diagram
labels the poly with the same 0.18 µm.[^pdk-04] The drawn layer is
`poly` (GDS 66:20, "Polysilicon"), with a `gate` purpose (66:9) and a
`resistor` purpose (66:13).[^pdk-06] SkyWater's own capability list is
unusually specific about this film: its furnace processes include
"LPCVD polysilicon (undoped), both amorphous and
crystalline".[^skw-01] The step name in the step list used in this
reference — *single a-Si gate deposition* — and SkyWater's "undoped …
amorphous" together are the basis for reading `SAGD` as one undoped
amorphous layer. That the resistor-protect mask {ref}`RPM <step-049>`
immediately follows is consistent with it: an in-situ-doped film would
leave nothing for a resistor mask to protect.

**Why "single"?** Two other gate constructions were common at the
130 nm node and both use more than one silicon layer: a polycide gate
(poly under tungsten silicide, used by DRAM makers to cut gate
resistance) and a stacked-amorphous-silicon gate, in which two thin a-Si
layers are deposited with an interface between them to block boron
penetration through the gate oxide.[^wu-1993] We infer that "single"
distinguishes the SKY130 gate from such stacks: one layer, one
deposition. The PDK's sheet resistance for poly, 48.2 Ω/sq,[^pdk-08] is
far above the few Ω/sq of a silicided or polycide gate[^txt-05] and is
what a heavily doped, unsilicided 0.18 µm poly film gives, so there is
no silicide strap on the gate either.

## Step category

`SAGD` is a {ref}`Thin-film deposition <category-deposition>` step — a
furnace LPCVD deposition like {ref}`ISONIT <step-003>` and, we infer,
{ref}`GATENIT <step-058>`. The category page explains the general
choice between amorphous and polycrystalline deposition; what is
specific here is that this is the only film in the flow whose grain
structure is a device parameter. Its grains set the roughness of the
gate edge after etch, the uniformity of dopant activation, the
poly-depletion behaviour of the gate and the matching of the precision
resistors.

## Why this step exists

The self-aligned polysilicon gate has been the standard MOS gate since
the early 1970s: it survives the source/drain anneals that a metal gate
could not, it lets the source and drain be implanted with the gate as
the mask, and its work function can be set by doping.[^wiki-poly] In
SKY130 the same film also forms the two precision resistor flavours
(300 Ω/sq "P+ poly" and 2000 Ω/sq "P− poly"),[^pdk-07] the poly plate
of the varactors and the gate of the SONOS memory transistor.

Depositing the film *amorphous* rather than polycrystalline is a
deliberate choice with three documented benefits:

* **Smoother, finer-grained film.** Below about 580 °C LPCVD silicon
  deposits amorphous; when it later crystallises it does so by
  solid-phase nucleation and growth, giving a smooth surface and a
  grain size controlled by the anneal rather than by the deposition.
  Voutsas and Hatalis mapped the amorphous-to-polycrystalline
  transition against deposition temperature and pressure,[^voutsas-1992]
  and Hatalis and Greve showed that low-temperature annealing of LPCVD
  a-Si yields grains much larger than as-deposited poly.[^hatalis-1988]
  A smooth top surface matters for the 0.15 µm gate
  lithography[^pdk-periph] ({ref}`P1M <step-061>`) and a smooth, fine-grained sidewall for the
  gate etch ({ref}`P1ME <step-062>`), because columnar as-deposited
  poly grains print as line-edge roughness.
* **Better dopant uniformity and less poly depletion.** Grain
  boundaries trap and segregate dopant;[^mandurah-1981][^kamins-1972]
  a film with fewer, larger grains after crystallisation gives more
  uniform activation and a smaller gate-depletion penalty, which at a
  4 nm-class gate oxide is a measurable loss of drive
  current.[^arora-1995]
* **Gate-oxide integrity.** Koda et al. reported better gate-oxide
  integrity for p⁺ PMOS gates made from large-grain poly grown from
  amorphous films.[^koda-1993]

Without this step there is no gate, no resistor and no SONOS control
gate; every FET parameter in the PDK's device tables is downstream of
it.

## How it is typically performed

An industry-generic recipe for an undoped a-Si gate film in a 200 mm,
130 nm-era fab:

* **Pre-clean.** The wafer arrives with fresh gate oxide, so only a
  light clean (or none) is used; a dilute-HF step is excluded because
  it would thin the 4 nm oxide. Queue time between gate oxidation and
  deposition is limited to keep the oxide surface clean.
* **Chemistry.** Silane pyrolysis, SiH₄ → Si + 2 H₂, in a hot-wall
  LPCVD furnace at a few hundred mTorr; Claassen et al. measured the
  deposition kinetics of silane in a low-pressure hot-wall
  system.[^claassen-1982] Some fabs use disilane (Si₂H₆) for a higher
  rate at low temperature.
* **Temperature.** Roughly 520–560 °C for an amorphous film, against
  600–650 °C for polycrystalline deposition (typical industry values,
  {ref}`category-deposition`;[^txt-01][^wiki-poly] Voutsas and Hatalis
  give the pressure-dependent transition[^voutsas-1992]). Harbeke et
  al. characterised the structure of LPCVD films across this
  range.[^harbeke-1984] Kinsbron et al. showed that films deposited
  amorphous can begin to crystallise *during* a long deposition if the
  temperature is near the transition,[^kinsbron-1983] which is why the
  set-point sits comfortably below it.
* **Thickness.** 0.18 µm in SKY130.[^pdk-03][^pdk-04] Deposition rates
  of a-Si at these temperatures are of the order of a few nm/min, so
  the run takes about an hour; batch loading of 100–150 wafers makes
  that acceptable.
* **Doping.** None at deposition (SkyWater: "undoped"[^skw-01]). In-situ
  phosphine doping is possible but strongly depresses the deposition
  rate and disturbs uniformity,[^meyerson-1984] and it would make a
  resistor-protect mask impossible; implant doping after deposition is
  the norm for a process with several poly doping levels (category
  page).
* **Crystallisation.** No dedicated anneal is listed in the step list
  used in this reference. Solid-phase crystallisation of a-Si on oxide
  proceeds at 600 °C over hours and much faster at higher
  temperatures;[^iverson-1987] the later furnace and RTA steps
  ({ref}`IOX45 <step-063>`, {ref}`TIPRTAD <step-075>`,
  {ref}`RTAD <step-088>`) supply more than enough thermal budget, so
  the film is fully polycrystalline long before contact.
* **Metrology.** Thickness by spectroscopic ellipsometry (the amorphous
  and crystalline optical constants differ, which is itself a
  process-control signal); particle scan; sheet resistance only after
  doping.

## Machines typically used

* **Vertical LPCVD furnace** with silane gas panel, vacuum pumping and
  exhaust abatement for pyrophoric silane. Representative 200 mm-era
  tools: SVG/Thermco–ASML–Aviza AVP/RVP series, Kokusai DD/Vertron,
  TEL Alpha-8S, ASM A400 (category page).
* **Single-wafer poly deposition** (e.g. Applied Materials Centura
  Poly-Gen) was an alternative used by some 130 nm fabs for
  thin-gate-stack control, at lower throughput.
* **Spectroscopic ellipsometer** and **unpatterned-wafer particle
  scanner**.

## Machines likely used at SkyWater

* **Aviza furnace running undoped a-Si.** SkyWater states "Furnaces are
  all made by Aviza" and lists "LPCVD polysilicon (undoped), both
  amorphous and crystalline" among the furnace processes.[^skw-01]
  Strength: **strong** for the tool vendor and for the existence of an
  undoped amorphous LPCVD silicon process; the assignment to this step
  is an inference from the step name. Whether the furnaces are vertical
  is not stated on SkyWater's page; a used-equipment listing describes
  the Aviza/SVG/Thermco AVP-8000 as a vertical batch furnace for
  150–200 mm wafers (weak).[^aviza-avp]
* No public source names a single-wafer poly chamber at SkyWater.

## Resources required

* **Silane (SiH₄)** — pyrophoric; delivered from a gas cabinet with
  excess-flow and leak monitoring.[^wiki-silane]
* **Nitrogen** for purge, ramp and back-fill; **hydrogen** is a
  by-product handled by the exhaust.
* **Quartz or silicon-carbide tube, boat and baffles**; silicon
  deposits on the furnace ware and is periodically cleaned off (a
  known consumable cost of poly tubes[^txt-02]).
* **Vacuum pump oil / dry pump maintenance** and exhaust abatement.
* **Monitor wafers** for thickness and particles.

SkyWater's filings name Air Products, Praxair, Linde and Airgas as gas
suppliers,[^sec-01][^sec-02] without tying them to a process.

## Related steps and cross-references

* Previous: {ref}`LVGOX <step-047>` (the last gate oxidation; the film
  is deposited directly on it). Next: {ref}`RPM <step-049>`.
* Doped at {ref}`P1I <step-050>` (gates), {ref}`PRI <step-053>` and
  {ref}`UPRI <step-056>` (resistors); capped at
  {ref}`GATENIT <step-058>` and {ref}`POC <step-059>`; backside film
  removed at {ref}`BFR <step-060>`; patterned at {ref}`P1M <step-061>`
  and etched at {ref}`P1ME <step-062>`; re-oxidised at
  {ref}`IOX45 <step-063>`.
* Also covers the SONOS cell stack from {ref}`ONO <step-040>` to
  {ref}`ONOME <step-042>`, so the memory-cell gate and the logic gate
  are the same film.
* Poly stringers from incomplete STI planarisation are discussed on
  {ref}`FILOX <step-011>`; the earlier furnace nitride is
  {ref}`ISONIT <step-003>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — "Furnaces are all made by
  Aviza"; "LPCVD polysilicon (undoped), both amorphous and
  crystalline".[^skw-01]
* SkyWater PDK, *Criteria & Assumptions* — "poly thickness"
  0.18 µm.[^pdk-03]
* SkyWater PDK, process stack diagram — poly 0.18 µm.[^pdk-04]
* SkyWater PDK, *Layers Reference* — `poly` 66:20 and its gate and
  resistor purposes.[^pdk-06]
* SkyWater PDK, *Device Details* — the resistor flavours built in the
  same film.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — poly 48.2 Ω/sq.[^pdk-08]
* SkyWater, Form S-1 and Form 10-K — gas suppliers.[^sec-01][^sec-02]
* Moov marketplace, Aviza AVP-8000 listing (weak).[^aviza-avp]

### High-level understanding

* Wikipedia, *Polycrystalline silicon* — the self-aligned poly gate
  and LPCVD deposition.[^wiki-poly]
* Wikipedia, *Amorphous silicon* — the material as
  deposited.[^wiki-asi]
* Wikipedia, *Silane* — the precursor and its hazards.[^wiki-silane]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the thin-film
  chapter on LPCVD silicon.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  LPCVD polysilicon and furnace practice.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — gate stacks of
  the deep-submicron generations.[^txt-05]

### Deep dive

* Kamins, *Polycrystalline Silicon for Integrated Circuits and
  Displays* — the monograph on deposition, structure, doping,
  oxidation and electrical properties of poly films.[^kamins-1998]
* Kamins, *J. Electrochem. Soc.* 1980 — structure and properties of
  LPCVD silicon films as a function of deposition
  temperature.[^kamins-1980]
* Harbeke et al., *J. Electrochem. Soc.* 1984 — growth and physical
  properties of LPCVD poly, including the amorphous
  regime.[^harbeke-1984]
* Voutsas and Hatalis, *J. Electrochem. Soc.* 1992 — the structure of
  as-deposited LPCVD films at low temperature and pressure: where the
  amorphous/polycrystalline boundary lies.[^voutsas-1992]
* Hatalis and Greve, *J. Appl. Phys.* 1988 — large-grain poly from
  low-temperature annealing of LPCVD a-Si.[^hatalis-1988]
* Kinsbron, Sternheim and Knoell, *Appl. Phys. Lett.* 1983 —
  crystallisation of a-Si films during the deposition itself, the
  hazard that sets the temperature margin.[^kinsbron-1983]
* Iverson and Reif, *J. Appl. Phys.* 1987 — the temperature dependence
  of solid-phase crystallisation kinetics of silicon films on
  SiO₂.[^iverson-1987]
* Joubert et al., *J. Electrochem. Soc.* 1987 — how deposition pressure
  changes the structure of LPCVD poly films.[^joubert-1987]
* Claassen et al., *J. Cryst. Growth* 1982 — silane deposition kinetics
  in a low-pressure hot-wall reactor.[^claassen-1982]
* Meyerson and Olbricht, *J. Electrochem. Soc.* 1984 — in-situ
  phosphorus doping of LPCVD poly and its effect on deposition rate,
  the alternative not taken here.[^meyerson-1984]
* Wu, Lee and Lei, IEDM 1993 — the stacked-amorphous-silicon gate,
  the "non-single" alternative.[^wu-1993]
* Koda et al., IEDM 1993 — gate-oxide integrity improved by
  large-grain poly gates.[^koda-1993]
* Mandurah, Saraswat and Kamins, *IEEE TED* 1981 — the grain-boundary
  trapping model of conduction in doped poly.[^mandurah-1981]
* Kamins, Manoliu and Tucker, *J. Appl. Phys.* 1972 — dopant diffusion
  along grain boundaries in poly.[^kamins-1972]
* Arora, Rios and Huang, *IEEE TED* 1995 — modelling poly-gate
  depletion and its circuit impact.[^arora-1995]
* ITRS 2001, *Front End Processes* — gate-electrode requirements
  (depletion, sheet resistance) for the 130 nm node.[^itrs-01]
* Stanford Nanofabrication Facility, *Tystar LPCVD Tube Training* — a
  university guide to running a hot-wall LPCVD tube.[^snf-lpcvd]

## Open questions

* The deposition temperature, pressure, precursor (silane or
  disilane) and rate are not public; the amorphous regime below about
  580 °C is an era-typical value from the cited literature.
* Whether the film is deposited in one furnace run or with an in-situ
  seed/interface layer is not public; the "single" in the step name
  is read as one layer.
* No dedicated crystallisation anneal appears in the step list used in
  this reference; we assume the later thermal steps crystallise the
  film.
* Whether the film is deposited in a batch furnace or a single-wafer
  chamber is not stated; SkyWater's capability list places LPCVD
  polysilicon under its Aviza furnaces.[^skw-01]

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository. <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration
    statement), filed 2021-03-22. <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024. <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco
    AVP 8000* listing, accessed 2026-08-30.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^wiki-poly]: Wikipedia, *Polycrystalline silicon*.
    <https://en.wikipedia.org/wiki/Polycrystalline_silicon>
[^wiki-asi]: Wikipedia, *Amorphous silicon*.
    <https://en.wikipedia.org/wiki/Amorphous_silicon>
[^wiki-silane]: Wikipedia, *Silane*. <https://en.wikipedia.org/wiki/Silane>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9. <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^kamins-1998]: T. Kamins, *Polycrystalline Silicon for Integrated
    Circuits and Displays*, 2nd ed., Kluwer Academic, 1998.
    <https://doi.org/10.1007/978-1-4615-5577-3>
[^kamins-1980]: T. I. Kamins, "Structure and Properties of LPCVD
    Silicon Films", *Journal of The Electrochemical Society* **127**(3),
    686–690 (1980). <https://doi.org/10.1149/1.2129733>
[^harbeke-1984]: G. Harbeke, L. Krausbauer, E. F. Steigmeier,
    A. E. Widmer, H. F. Kappert and G. Neugebauer, "Growth and Physical
    Properties of LPCVD Polycrystalline Silicon Films", *Journal of The
    Electrochemical Society* **131**(3), 675–682 (1984).
    <https://doi.org/10.1149/1.2115672>
[^voutsas-1992]: A. T. Voutsas and M. K. Hatalis, "Structure of
    As-Deposited LPCVD Silicon Films at Low Deposition Temperatures and
    Pressures", *Journal of The Electrochemical Society* **139**(9),
    2659–2665 (1992). <https://doi.org/10.1149/1.2221280>
[^hatalis-1988]: M. K. Hatalis and D. W. Greve, "Large grain
    polycrystalline silicon by low-temperature annealing of low-pressure
    chemical vapor deposited amorphous silicon films", *Journal of
    Applied Physics* **63**(7), 2260–2266 (1988).
    <https://doi.org/10.1063/1.341065>
[^kinsbron-1983]: E. Kinsbron, M. Sternheim and R. Knoell,
    "Crystallization of amorphous silicon films during low pressure
    chemical vapor deposition", *Applied Physics Letters* **42**(9),
    835–837 (1983). <https://doi.org/10.1063/1.94080>
[^iverson-1987]: R. B. Iverson and R. Reif, "Recrystallization of
    amorphized polycrystalline silicon films on SiO₂: Temperature
    dependence of the crystallization parameters", *Journal of Applied
    Physics* **62**(5), 1675–1681 (1987). <https://doi.org/10.1063/1.339591>
[^joubert-1987]: P. Joubert, B. Loisel, Y. Chouan and L. Haji, "The
    Effect of Low Pressure on the Structure of LPCVD Polycrystalline
    Silicon Films", *Journal of The Electrochemical Society* **134**(10),
    2541–2545 (1987). <https://doi.org/10.1149/1.2100239>
[^claassen-1982]: W. A. P. Claassen, J. Bloem, W. G. J. N. Valkenburg
    and C. H. J. van den Brekel, "The deposition of silicon from silane
    in a low-pressure hot-wall system", *Journal of Crystal Growth*
    **57**(2), 259–266 (1982). <https://doi.org/10.1016/0022-0248(82)90481-X>
[^meyerson-1984]: B. S. Meyerson and W. Olbricht, "Phosphorus-Doped
    Polycrystalline Silicon via LPCVD: I. Process Characterization",
    *Journal of The Electrochemical Society* **131**(10), 2361–2365
    (1984). <https://doi.org/10.1149/1.2115258>
[^wu-1993]: S. L. Wu, C. L. Lee and T. F. Lei, "Suppression of boron
    penetration into an ultra-thin gate oxide (≤7 nm) by using a
    stacked-amorphous-silicon (SAS) film", *IEDM 1993 Technical Digest*,
    pp. 329–332. <https://doi.org/10.1109/IEDM.1993.347341>
[^koda-1993]: M. Koda, Y. Shida, J. Kawaguchi and Y. Kaneko, "Improving
    gate oxide integrity in p⁺ pMOSFET by using large grain size
    polysilicon gate", *IEDM 1993 Technical Digest*, pp. 471–474.
    <https://doi.org/10.1109/IEDM.1993.347308>
[^mandurah-1981]: M. M. Mandurah, K. C. Saraswat and T. I. Kamins, "A
    model for conduction in polycrystalline silicon — Part I: Theory",
    *IEEE Transactions on Electron Devices* **28**(10), 1163–1171
    (1981). <https://doi.org/10.1109/T-ED.1981.20504>
[^kamins-1972]: T. I. Kamins, J. Manoliu and R. N. Tucker, "Diffusion
    of Impurities in Polycrystalline Silicon", *Journal of Applied
    Physics* **43**(1), 83–91 (1972). <https://doi.org/10.1063/1.1660842>
[^arora-1995]: N. D. Arora, E. Rios and C.-L. Huang, "Modeling the
    polysilicon depletion effect and its impact on submicrometer CMOS
    circuit performance", *IEEE Transactions on Electron Devices*
    **42**(5), 935–943 (1995). <https://doi.org/10.1109/16.381991>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^snf-lpcvd]: Stanford Nanofabrication Facility, *Tystar LPCVD Tube
    Training*, equipment training page.
    <https://snfguide.stanford.edu/guide/equipment/training/tystar-lpcvd-tube-training>
