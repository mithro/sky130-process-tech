(step-098)=
# Step 098 — CSIL: Contact silicidation

| | |
|---|---|
| **Step number** | 98 of 171[^steps-sheet] |
| **Step code** | `CSIL` |
| **Category** | {ref}`Anneal / thermal processing <category-anneal>` |
| **Phase** | MOL — silicide and local interconnect |
| **Previous step** | {ref}`TI/TIN1 <step-097>` |
| **Next step** | {ref}`WDEP <step-099>` |

## What this step is

`CSIL` — contact silicidation — is the anneal (on our reading a rapid
thermal anneal) that reacts the titanium of {ref}`TI/TIN1 <step-097>`
with the silicon
and polysilicon at the bottom of every contact hole to form titanium
disilicide (TiSi₂). Where the titanium lies on oxide — the hole walls
and the field — it does not react with the substrate; under its TiN
cap it stays as titanium or, in a nitrogen ambient, nitrides. The
result is a {term}`silicide` contact *only inside the contact holes*:
a small disc of TiSi₂ under each tungsten plug, and no silicide
anywhere else.

That is the distinctive feature of this module, and the public
evidence for it is the PDK's own numbers. In a self-aligned silicide
({term}`salicide`) process the metal is deposited on the bare gates
and source/drains and reacts everywhere silicon is exposed, so the
poly and diffusion {term}`sheet resistances <sheet resistance>` fall to a few ohms per square
(category page[^wiki-salicide][^txt-05]). The SKY130 extraction
tables give poly 48 200 mΩ/sq (48.2 Ω/sq), N-diffusion
120 000 mΩ/sq and P-diffusion 197 000 mΩ/sq[^pdk-08] — the values of
heavily doped but *unsilicided* poly and diffusion — and a per-contact
resistance of 15 000 mΩ (15 Ω) for a licon.[^pdk-08] The
{ref}`P1I <step-050>` page draws the same conclusion from the poly
value. On that evidence this reference describes a *contact-only*
titanium silicide, formed by an anneal after the {term}`liner` and
before the tungsten (inference). SkyWater lists "Ti and Co Silicide" among its special
modules,[^skw-01] which shows the capability without saying which
metal or which scheme SKY130 uses.

What is not public: the anneal temperature, time and ambient, the
silicide thickness (set by the titanium at the hole bottom, itself
not public), and whether the anneal is one step or two.

## Step category

`CSIL` is an {ref}`Anneal / thermal processing <category-anneal>` step
of the *silicidation* type — the class the category page describes
for titanium: a first {term}`RTA` at roughly 600–700 °C in N₂ forms the
metastable {term}`C49 TiSi₂` (and TiN on top), a selective strip removes
unreacted metal, and a second RTA at roughly 800–900 °C converts C49
to the low-resistivity C54 phase.[^maex-1993][^osburn-1993] What is
specific to this instance is that the sequence is *not* a salicide:
there is no selective strip, because the unreacted titanium and its
TiN cap are wanted — they are the plug liner — and the C49→C54
question is confined to a 0.08 µm disc[^pdk-03] rather than a long
gate line. It is also a thermal step with a hard ceiling from
below: the silicide forms on 0.1 µm junctions[^pdk-03] that it must
not punch through.

## Why this step exists

A tungsten plug on bare silicon makes a poor contact; a silicide
under it makes a good one. The reasons, and the reasons for the
contact-only form:

* **Contact resistance.** The specific contact resistivity of a
  metal–silicon contact falls exponentially with the doping under
  it and with the barrier height (the models Berger[^berger-1972]
  and Schroder and Meier[^schroder-1984] set out); TiSi₂ on
  degenerately doped silicon gives low barriers to both n⁺ and p⁺
  — Varahramyan and Verret give a specific-contact-resistance model
  for TiSi₂–silicon.[^varahramyan-1996] Titanium also reduces the
  native oxide it lands on, which a tungsten or TiN contact cannot.
  The PDK's 15 Ω per licon[^pdk-08] is the outcome.
* **Why not a salicide.** Three features of the PDK's device list
  argue for keeping the gates and diffusions unsilicided
  (inference): the precision {term}`poly resistors <poly resistor>` ({ref}`RPM <step-049>`,
  {ref}`URPM <step-055>`) and the diffusion resistors need their
  high sheet resistances,[^pdk-07][^pdk-08] which a blanket silicide
  would have to be masked away from; the 5 V and drain-extended
  devices[^pdk-07] carry lightly doped regions that a silicide would
  short; and the {term}`SONOS` cells ({ref}`ONO <step-040>`) have an {term}`ONO`
  stack under the gate that a silicide anneal's stress and a
  selective strip's chemistry would threaten. A contact-only
  silicide needs no extra mask and no strip. The cost is the poly
  RC of long gate lines, which the {ref}`P1I <step-050>` page
  discusses, and which the low-resistance titanium-nitride local
  interconnect ({ref}`LITIN <step-101>`) partly compensates.
* **Phase and thickness.** Titanium and silicon react by
  interdiffusion into C49 TiSi₂ from about 500 °C and transform to
  C54 above about 700 °C, with the transformation nucleation-limited
  on small features — Mann and Clevenger on the C49-to-C54
  transformation,[^mann-1994] Murarka on formation
  kinetics,[^murarka-1983] Osburn on silicides by rapid thermal
  processing,[^osburn-1993] Maex's review of TiSi₂ and
  CoSi₂,[^maex-1993] Zhang and Östling's of silicides in
  CMOS.[^rev-04] In a 0.08 µm contact the C54 nucleation problem is
  at its worst, but the silicide is so short that its sheet
  resistance barely matters; what matters is the interface.
* **The TiN cap and the nitrogen ambient.** Annealing Ti under TiN
  in nitrogen forms a TiN/TiSi₂ bilayer whose formation Morgan,
  Broadbent and Reader studied[^morgan-1985] — nitrogen competes
  with silicon for the titanium, and the balance sets the silicide
  thickness. Koerner, Erb and Melzner evaluated Ti and TiN
  thicknesses for exactly this tungsten-plug contact
  structure,[^koerner-1993] and Ohto et al. describe a TiN/Ti
  contact-plug technology for DRAM.[^ohto-1996]
* **Junction integrity.** TiSi₂ consumes silicon (about 2.3 nm per
  nanometre of titanium, Maex[^maex-1993]); with a 0.1 µm
  junction[^pdk-03] and an implant-damaged, plasma-etched contact
  bottom, the silicide must stay thin and uniform or the contact
  leaks. The 10° taper and 0.08 µm bottom[^pdk-03] concentrate
  current through a small area, which raises the stakes.

Without `CSIL` every contact would be a tungsten–TiN–silicon
junction of high and variable resistance.

## How it is typically performed

An industry-generic {term}`contact silicide` anneal for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

* **Tool and ambient.** Single-wafer lamp-heated RTA in nitrogen
  (or argon), strictly oxygen-free: "a few ppm of O₂ oxidises the
  metal before it can react" (category page). SkyWater's Heatpulse
  8808 entry lists NH₃, Ar, N₂ and O₂.[^skw-01]
* **Temperature and time.** A soak of tens of seconds at 600–750 °C
  to form C49 TiSi₂ under the TiN, with or without a second soak at
  800–900 °C for the C54 transformation — typical industry values
  for a Ti/TiN contact silicide (Osburn;[^osburn-1993] Yoo, Atanos
  and Whitworth describe TiSi₂ formation and anneal in a
  susceptor-based low-pressure {term}`RTP` system[^yoo-1999]). Because there
  is no strip between them, the two soaks can be one recipe.
* **Sequence.** Load from the {term}`PVD` platform without a wet step;
  purge; low-temperature stabilisation; ramp; soak; ramp-down;
  unload to the tungsten deposition. {term}`Queue time <queue time>` between liner and
  anneal is limited to keep the titanium from oxidising through
  pinholes in the TiN (industry practice).
* **Control.** Pyrometer emissivity correction for a metallised
  wafer;[^sorrell-1993] sheet resistance of blanket Ti/TiN-on-silicon
  monitors before and after; contact-chain resistance
  ({ref}`category-test`) as the electrical proof.
* **Alternative.** Some flows omit a separate silicide anneal and let
  the tungsten deposition temperature (400–450 °C) and later
  anneals form the silicide in place; which SKY130 does is not stated
  publicly, and this reference describes a separate anneal.

## Machines typically used

* **{ref}`Rapid thermal processors <machine-rapid-thermal-processor>`**, 200 mm: AG Associates Heatpulse
  8108/8800 series, Applied Materials RTP Centura (the Gronet and
  Gibbons chamber[^pat-rtp-amat]), Steag/Mattson RTP, Kokusai and TEL
  RTP (category page).
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`** for silicide monitors; **{ref}`contact-chain test structures <machine-parametric-tester>`**.

## Machines likely used at SkyWater

* **AG Associates Heatpulse 8808.** SkyWater lists "Ag Heatpulse
  8808 NH3, Ar, N2, O2, up to 1200C".[^skw-01] Strength: **strong**
  for the tool; assignment to `CSIL` is an **inference** from the
  Heatpulse being the only RTA on SkyWater's list, and silicide formation is a
  listed application of the family: reseller documentation gives a
  400–1200 °C range and
  "Programmable, 1 – 180°C per second" ramp-up,[^ag-8800] the family
  specification PDF the same range for the 8108,[^ag-8108] and a
  vendor blog post describes the 8800/8108 family.[^plasmatherm-ag]
* **"Ti and Co Silicide" special module.**[^skw-01] Strength: strong
  for the capability; which metal and scheme SKY130 uses is an
  inference from the PDK numbers above.

## Resources required

* **Nitrogen and argon** (likely ambient, our inference; SkyWater lists
  the Heatpulse's gases, "NH3, Ar, N2, O2", but no ambient for any
  step);[^skw-01] the titanium and TiN were consumed at
  {ref}`TI/TIN1 <step-097>`.
* **Tungsten-halogen lamps, quartz window and chamber, edge rings**;
  pyrometer calibration and thermocouple wafers (category page).
* **Cooling water and CDA/N₂** for lamp and chamber cooling.[^ag-8108]
* **Monitor wafers** (SEMI M8 class)[^semi-m8] with blanket Ti/TiN on
  silicon for sheet-resistance tracking.
* Gas suppliers named in SkyWater's 2021 S-1: Air Products,
  Praxair.[^sec-01]

## Related steps and cross-references

* Previous: {ref}`TI/TIN1 <step-097>` (the titanium reacted here).
  Next: {ref}`WDEP <step-099>` (the tungsten fill), then
  {ref}`WCMPLI <step-100>`.
* The surfaces silicided: source/drains of {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; poly heads opened
  at {ref}`NPCME <step-079>` and doped through the cut.
* Why the gates are not silicided: {ref}`P1I <step-050>`; the
  resistors kept unsilicided: {ref}`RPM <step-049>`,
  {ref}`URPM <step-055>`.
* The other RTAs: {ref}`RTAI <step-034>`, {ref}`TIPRTAD <step-075>`,
  {ref}`RTAD <step-088>`, {ref}`RTAD2 <step-092>`.
* Category page: {ref}`Anneal / thermal processing <category-anneal>`.

## References

### Cross-check

* SkyWater PDK, *Parasitic Layout Extraction* — poly 48 200 mΩ/sq;
  N-diffusion 120 000 mΩ/sq; P-diffusion 197 000 mΩ/sq; LICON
  contact 15 000 mΩ.[^pdk-08]
* SkyWater PDK, *Device Details* — poly resistors, 5 V and
  drain-extended devices, SONOS cell.[^pdk-07]
* SkyWater PDK, *Criteria & Assumptions* — S/D junction 0.1 µm;
  "Standard Licon bottom CD" 0.08 µm; "Licon1 etch angle" 10°.[^pdk-03]
* SkyWater, *Facilities & Capabilities* — "Ti and Co Silicide"
  special module; "Ag Heatpulse 8808 NH3, Ar, N2, O2, up to
  1200C".[^skw-01]
* SemiStar, *AG Associates Heatpulse 8800 / 8808* and family
  specification PDF; Plasma-Therm product spotlight.[^ag-8800][^ag-8108][^plasmatherm-ag]
* SkyWater, Form S-1 — gas suppliers.[^sec-01]

### High-level understanding

* Wikipedia, *Salicide*, *Titanium disilicide*, *Contact
  resistance*.[^wiki-salicide][^wiki-tisi2][^wiki-rc]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — silicides
  and contacts at deep-submicron nodes.[^txt-05]
* Fair (ed.), *Rapid Thermal Processing: Science and
  Technology*.[^txt-10]

### Deep dive

* Murarka, *Silicides for VLSI Applications* — formation
  kinetics.[^murarka-1983]
* Maex, *Mater. Sci. Eng. R* 1993 — TiSi₂ and CoSi₂: formation,
  silicon consumption, narrow-line effect.[^maex-1993]
* Zhang and Östling, *Crit. Rev. Solid State Mater. Sci.* 2003 —
  metal silicides in CMOS.[^rev-04]
* Osburn, in Fair (ed.), *Rapid Thermal Processing* — silicides by
  RTP.[^osburn-1993]
* Mann and Clevenger, *J. Electrochem. Soc.* 1994 — the C49-to-C54
  transformation.[^mann-1994]
* Mann et al., *IBM J. Res. Dev.* 1995 — silicides and local
  interconnections together.[^mann-1995]
* Morgan, Broadbent and Reader, *MRS Proc.* 1985 — TiN/TiSi₂
  bilayers by RTA in nitrogen.[^morgan-1985]
* Koerner, Erb and Melzner, *Appl. Surf. Sci.* 1993 — Ti and TiN
  thicknesses for tungsten-plug contacts.[^koerner-1993]
* Ohto et al., IEDM 1996 — a TiN/Ti contact-plug technology.[^ohto-1996]
* Yoo, Atanos and Whitworth, *JJAP* 1999 — TiSi₂ formation in a
  low-pressure RTP system.[^yoo-1999]
* Varahramyan and Verret, *Solid-State Electron.* 1996 — specific
  contact resistance of TiSi₂–silicon contacts.[^varahramyan-1996]
* Berger, *Solid-State Electron.* 1972, and Schroder and Meier,
  *IEEE TED* 1984 — contact-resistance models and
  measurement.[^berger-1972][^schroder-1984]
* Sorrell and Gyurcsik, *IEEE TSM* 1993 — emissivity correction in
  RTP pyrometry.[^sorrell-1993]
* Gronet and Gibbons (Applied Materials), US 5,155,336 — the
  lamp-heated RTP chamber.[^pat-rtp-amat]

## Open questions

* That SKY130 uses a contact-only titanium silicide rather than a
  salicide is our inference from the PDK's sheet resistances.
* The anneal temperature, time, ambient and whether it is one or two
  soaks are not public.
* The silicide thickness and its consumption of the 0.1 µm junction
  are not public.
* Whether the "Co" in SkyWater's "Ti and Co Silicide" module is
  used by any SKY130 option is not public.

<!-- footnotes -->

[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the `nfet_01v8` cross-section drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/nfet_01v8/cross-section-nfet_01v8.svg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^ag-8800]: SemiStar Corp., *AG Associates Heatpulse 8800 / 8808 Rapid
    Thermal Processing* (reseller specification page), accessed
    2026-08-30.
    <https://www.semistarcorp.com/product/ag-associates-heatpulse-8800-8808/>
[^ag-8108]: SemiStar Corp., *AG Associates Heatpulse 4100 / 8108 / 8800
    / 8800i Specifications* (reseller PDF; operating specifications for
    the Heatpulse 4100 and 8108), accessed 2026-08-30.
    <https://www.semistarcorp.com/wp-content/uploads/2025/12/AG-Associates-Heatpulse-4100-8108-8800-8800i-Specifications-Rapid-Thermal-Processor.pdf>
[^plasmatherm-ag]: Plasma-Therm, *Product Spotlight: AG Heatpulse 8800 /
    8108 RTP*, blog post.
    <https://blog.plasmatherm.com/product-spotlight-ag-heatpulse-8800-8108-rtp>
[^wiki-salicide]: Wikipedia, *Salicide*.
    <https://en.wikipedia.org/wiki/Salicide>
[^wiki-tisi2]: Wikipedia, *Titanium disilicide*.
    <https://en.wikipedia.org/wiki/Titanium_disilicide>
[^wiki-rc]: Wikipedia, *Contact resistance*.
    <https://en.wikipedia.org/wiki/Contact_resistance>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^txt-10]: R. B. Fair (ed.), *Rapid Thermal Processing: Science and
    Technology*, Academic Press, 1993, ISBN 978-0-12-247690-7; R. B.
    Fair, "Junction Formation in Silicon by Rapid Thermal Annealing",
    pp. 169–226. <https://doi.org/10.1016/b978-0-12-247690-7.50009-3>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^pat-rtp-amat]: C. M. Gronet and J. F. Gibbons (Applied Materials),
    *Rapid thermal heating apparatus and method*, US 5,155,336 A,
    granted 1992-10-13.
    <https://patents.google.com/patent/US5155336A/en>
[^murarka-1983]: S. P. Murarka, "Formation", in *Silicides for VLSI
    Applications*, Academic Press, 1983, pp. 99–131.
    <https://doi.org/10.1016/b978-0-08-057056-3.50009-4>
[^maex-1993]: K. Maex, "Silicides for integrated circuits: TiSi₂ and
    CoSi₂", *Materials Science and Engineering: R* **11**(2–3), vii–153
    (1993). <https://doi.org/10.1016/0927-796X(93)90001-J>
[^rev-04]: S.-L. Zhang and M. Östling, "Metal Silicides in CMOS
    Technology: Past, Present, and Future Trends", *Critical Reviews in
    Solid State and Materials Sciences* **28**(1), 1–129 (2003).
    <https://doi.org/10.1080/10408430390802431>
[^osburn-1993]: C. M. Osburn, "Silicides", in R. B. Fair (ed.), *Rapid
    Thermal Processing: Science and Technology*, Academic Press, 1993,
    pp. 227–309. <https://doi.org/10.1016/b978-0-12-247690-7.50010-x>
[^mann-1994]: R. W. Mann and L. A. Clevenger, "The C49 to C54 Phase
    Transformation in TiSi₂ Thin Films", *Journal of The Electrochemical
    Society* **141**(5), 1347–1350 (1994).
    <https://doi.org/10.1149/1.2054921>
[^mann-1995]: R. W. Mann, L. A. Clevenger, P. D. Agnello and
    F. R. White, "Silicides and local interconnections for
    high-performance VLSI applications", *IBM Journal of Research and
    Development* **39**(4), 403–417 (1995).
    <https://doi.org/10.1147/rd.394.0403>
[^morgan-1985]: A. E. Morgan, E. K. Broadbent and A. H. Reader,
    "Formation of Titanium Nitride/Silicide Bilayers by Rapid Thermal
    Anneal in Nitrogen", *MRS Proceedings* **52** (1985).
    <https://doi.org/10.1557/PROC-52-279>
[^koerner-1993]: H. Koerner, H. P. Erb and H. Melzner, "Evaluation of
    Ti and TiN thicknesses for tungsten plug contact metallization",
    *Applied Surface Science* **73**, 6–13 (1993).
    <https://doi.org/10.1016/0169-4332(93)90139-3>
[^ohto-1996]: K. Ohto, K. Urabe, T. Taguwa, S. Chikaki and T. Kikkawa,
    "A novel TiN/Ti contact plug technology for gigabit scale DRAM
    using Ti-PECVD and TiN-LPCVD", *IEDM 1996 Technical Digest*,
    pp. 361–364. <https://doi.org/10.1109/IEDM.1996.553603>
[^yoo-1999]: W. S. Yoo, A. J. Atanos and D. M. Whitworth, "Titanium
    Silicide Formation and Anneal Using a Susceptor-Based Low Pressure
    Rapid Thermal Processing System", *Japanese Journal of Applied
    Physics* **38**(3B), L304 (1999).
    <https://doi.org/10.1143/JJAP.38.L304>
[^varahramyan-1996]: K. Varahramyan and E. J. Verret, "A model for
    specific contact resistance applicable for titanium
    silicide-silicon contacts", *Solid-State Electronics* **39**(11),
    1601–1607 (1996). <https://doi.org/10.1016/0038-1101(96)00091-3>
[^berger-1972]: H. H. Berger, "Models for contacts to planar devices",
    *Solid-State Electronics* **15**(2), 145–158 (1972).
    <https://doi.org/10.1016/0038-1101(72)90048-2>
[^schroder-1984]: D. K. Schroder and D. L. Meier, "Solar cell contact
    resistance — A review", *IEEE Transactions on Electron Devices*
    **31**(5), 637–647 (1984). <https://doi.org/10.1109/T-ED.1984.21583>
[^sorrell-1993]: F. Y. Sorrell and R. S. Gyurcsik, "Model-based
    emissivity correction in pyrometer temperature control of rapid
    thermal processing systems", *IEEE Transactions on Semiconductor
    Manufacturing* **6**(3), 273–276 (1993).
    <https://doi.org/10.1109/66.238178>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
