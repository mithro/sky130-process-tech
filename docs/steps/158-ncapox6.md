(step-158)=
# Step 158 — NCAPOX6: CAPOX deposition

| | |
|---|---|
| **Step number** | 158 of 171 |
| **Step code** | `NCAPOX6` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — MiM capacitors, metal 3–5, via 3–4 |
| **Previous step** | {ref}`CMPM4 <step-157>` |
| **Next step** | {ref}`VIM4 <step-159>` |

## What this step is

`NCAPOX6` deposits a *{term}`cap oxide`* on the polished inter-level
dielectric over metal 4. After {ref}`CMPM4 <step-157>` the
{ref}`NILD6 <step-156>` oxide is flat, but its thickness above the
metal-4 lines and the `cap2m` plates is whatever the polish left, and
its surface carries the scratches, slurry residue and hydrated layer of
a polish. A thin plasma oxide deposited over it seals that surface and,
on our reading of its position in the flow, brings the dielectric
above metal 4 to its final thickness before the via-4 mask
({ref}`VIM4 <step-159>`) is printed. The finished number is public: the
PDK's stack diagram labels the via-4 height 0.505 µm, between the top of
the 0.845 µm `metal4` and the bottom of `metal5`.[^pdk-04] The cap's own
thickness is not. The same cap is described at
{ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`,
{ref}`NCAPOX4 <step-128>` and {ref}`NCAPOX5 <step-143>`.

The stack diagram offers no hint of the cap: beside "NILD6 K=4.0" it
draws no "_C" film, as it does not at NILD5.[^pdk-04] What the cap
prepares for is different from the levels below. The via-4 opening is a
0.800 µm square (via4.1) on a 0.800 µm space (via4.2),[^pdk-periph]
etched 0.505 µm deep — an {term}`aspect ratio` of about 0.63:1 (our
arithmetic) — and, in the step list used in this reference, no tungsten
liner, fill or plug polish follows: the next deposition after the via
etch is the metal-5 stack of {ref}`WTIAL5 <step-161>`. On our reading,
then, the surface this cap leaves is also the surface on which metal 5 is
sputtered wherever there is no via, and the wall of every via-4 hole
into which that metal must go (inference).

## Step category

`NCAPOX6` is a {ref}`Thin-film deposition <category-deposition>` step of
the *{term}`PECVD` oxide* class — the category page's PECVD section —
and, like its predecessors, the simplest deposition in its module: a
blanket, thin, low-temperature oxide on a flat surface with no gap to
fill. What is specific to this instance is that the dielectric it
completes contains the second capacitor, whose plates sit inside the
via-4 dielectric, and that the wafer now carries four aluminium levels
and two thin capacitor dielectrics whose temperature and plasma exposure
it must respect (roughly 400–450 °C for Al–Cu, industry-typical[^txt-05]).

## Why this step exists

A polish alone does not give a via level what it needs;
{ref}`NCAPOX3 <step-117>` sets out the reasons, which apply here with the
via-4 numbers:

* **Thickness control.** The {ref}`CMPM4 <step-157>` polish is stopped by
  removal amount and varies with pattern density — the variation Boning
  et al. and Chang et al. characterised.[^boning-1994][^chang-1995]
  Polishing slightly below target and adding a cap of well-controlled
  thickness tightens the final 0.505 µm[^pdk-04] (industry
  practice[^txt-05]) and with it both via-4 depths the
  {ref}`VIM4E <step-160>` etch must reach: to the metal-4 cap and to the
  `cap2m` plate.
* **Restoring cover over the plates.** Where the polish has thinned the
  oxide over dense capacitor arrays, a deposited cap of known thickness
  restores a minimum distance between the plate and metal 5 (inference
  from the construction; the estimate of the remaining oxide is at
  {ref}`CMPM4 <step-157>`).
* **Sealing the polished surface.** Oxide CMP leaves micro-scratches and
  embedded particles — Devriendt et al. relate them to the post-CMP
  clean[^devriendt-1998] — and a hydroxyl-rich surface layer;[^moon-2016]
  a fresh plasma oxide buries them. Water released from a dielectric is
  as harmful to an aluminium via fill as to a tungsten one: Kobayakawa et
  al. studied outgassing from spin-on-glass planarising films,[^kobayakawa-1991]
  and Taguchi, Maeda and Aoyama improved the filling of vias by
  high-pressure aluminium reflow by controlling water outgassing from the
  via holes.[^taguchi-1998]
* **A known surface for lithography and for metal 5.** The
  {ref}`VIM4 <step-159>` resist is tuned to a reproducible oxide thickness
  over reflective metal and capacitor plates, since the swing-curve reflectivity
  depends on it;[^brunner-1991] and, on our reading of the step order, the
  metal-5 underlayer is sputtered directly onto this oxide outside the
  vias (inference).

Without `NCAPOX6` the via-4 lithography and etch would work on a surface
whose thickness varied with the polish, and the oxide over some capacitor
plates would be thinner than intended.

## How it is typically performed

An industry-generic cap-oxide deposition for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public); the sequence is that of
{ref}`NCAPOX3 <step-117>`.

1. **Chamber.** A single-wafer or twin-chamber PECVD reactor at 350–400 °C
   (industry-typical[^txt-05][^raupp-1992]); SkyWater lists "PECVD TEOS,
   C2 and Producer" and "PECVD silane oxide/nitride/oxynitride, C1", each
   with low-temperature options.[^skw-01] Applied Materials'
   Producer[^amat-10k] and Novellus's Concept/Sequel
   family[^novellus-history] are the 200 mm-era tools.
2. **Precursor.** {term}`TEOS`/O₂ plasma oxide — Raupp, Cale and Hey
   analyse its kinetics[^raupp-1992] — or SiH₄/N₂O plasma oxide, whose
   properties depend on RF power as Chapple-Sokol, Tierney and Batey
   measured.[^chapple-sokol-1989] The Cypress Fab 4 reports list a 1 000 Å
   TEOS film in their passivation stacks,[^cyp-qtp-123907][^cyp-qtp-014807]
   which shows a PECVD TEOS oxide of cap-like thickness in the same fab;
   that this cap is of the same kind is our inference.
3. **Thickness.** Not public; a cap of the order of 0.05–0.15 µm is
   typical of the practice (industry-typical value[^txt-05]), sized so
   that polished NILD6 plus cap reaches the 0.505 µm via-4 height.[^pdk-04]
4. **Film properties.** A dense, low-hydrogen film; hydrogen evolution
   from plasma oxide on later heating changes its stress,[^mani-2007] and
   a wet cap defeats its purpose. LPCVD TEOS[^adams-1979][^becker-1987]
   would give a denser film but at 650–750 °C, far above the aluminium
   limit (inference from the temperature).
5. **Plasma exposure.** The deposition plasma reaches a wafer whose
   `cap2m` top plates are still floating under the dielectric; a gentle,
   low-bias PECVD step limits the charging Cheung described for
   plasma-enhanced dielectric deposition[^cheung-2000] (inference that it
   matters here; Wang, Ackaert et al. document the MiM
   case[^wang-2004-mim]).
6. **Clean and metrology.** The wafer comes from the post-CMP scrub
   (Philipossian and Sun on the brushes[^philipossian-2009]); after
   deposition, thickness and index by ellipsometry on monitors and product
   pads, total dielectric over metal-4 pads, stress by wafer bow,
   particles; NF₃ chamber clean.

## Machines typically used

* **PECVD oxide system**, 200 mm: Applied Materials Producer / Centura
  DxZ,[^amat-10k] Novellus Concept One/Two, Sequel[^novellus-history]
  ({ref}`category-deposition`).
* **Ellipsometer / reflectometer**, **stress gauge**, **particle
  counter**.

## Machines likely used at SkyWater

* **PECVD TEOS "C2 and Producer".** SkyWater lists it with low-temperature
  options.[^skw-01] Strength: **strong** for existence; its use for this
  cap is an **inference** from the Fab 4 TEOS passivation
  films.[^cyp-qtp-123907][^cyp-qtp-014807]
* **PECVD silane oxide "C1".**[^skw-01] Strength: strong for existence; an
  alternative for the cap (weak for assignment).

## Resources required

* **TEOS and oxygen** (helium carrier) or **silane and nitrous
  oxide**;[^wiki-teos][^wiki-pecvd] gas and chemical suppliers per
  SkyWater's filings.[^sec-01]
* **NF₃** for the chamber clean; **nitrogen** purge.
* **Chamber consumables**; **monitor wafers** for thickness, index and
  stress.

## Related steps and cross-references

* Previous: {ref}`CMPM4 <step-157>` (the polish it caps). Next:
  {ref}`VIM4 <step-159>` (the via-4 mask), {ref}`VIM4E <step-160>` (the
  etch through this cap) and {ref}`WTIAL5 <step-161>` (the metal-5 stack
  sputtered onto it).
* The dielectric beneath: {ref}`NILD6 <step-156>`; the capacitor inside
  it: {ref}`CAPTIW2 <step-151>`, {ref}`CAP2ME <step-153>`.
* The other cap oxides: {ref}`NCAPOX <step-091>`, {ref}`NCAPOX3 <step-117>`,
  {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Process stack diagram* — "NILD6 K=4.0" with no "_C" film;
  via4 0.505 µm; `metal4` 0.845 µm.[^pdk-04]
* SkyWater PDK, *Periphery rules* — via4.1, via4.2.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — PECVD TEOS C2 and Producer;
  PECVD silane oxide C1.[^skw-01]
* Cypress, QTP 123907/132302/132301 and QTP 014807 — a 1 000 Å TEOS film in
  the Fab 4 passivation stacks.[^cyp-qtp-123907][^cyp-qtp-014807]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition*, *Tetraethyl
  orthosilicate*.[^wiki-pecvd][^wiki-teos]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — dielectrics in
  the multilevel back end.[^txt-05]

### Deep dive

* Raupp, Cale and Hey, *JVST B* 1992 — the kinetics of PECVD TEOS
  oxide.[^raupp-1992]
* Chapple-Sokol, Tierney and Batey (IBM), MRS 1989 — RF-power dependence
  of PECVD oxide properties.[^chapple-sokol-1989]
* Mani and Saif, *Thin Solid Films* 2007 — stress from hydrogen evolution
  in plasma oxide.[^mani-2007]
* Adams and Capio, *J. Electrochem. Soc.* 1979, and Becker et al., *JVST
  B* 1987 — LPCVD oxides and why they are ruled out over
  aluminium.[^adams-1979][^becker-1987]
* Boning et al., SPIE 1994, and Chang et al., IEDM 1995 — the ILD
  thickness variation a cap tightens.[^boning-1994][^chang-1995]
* Devriendt et al. (IMEC), 1998, and Moon, 2016 — post-CMP defects and the
  hydrated oxide surface.[^devriendt-1998][^moon-2016]
* Kobayakawa et al., VMIC 1991 — outgassing from spin-on-glass
  planarising films.[^kobayakawa-1991]
* Taguchi, Maeda and Aoyama, 1998 — water outgassing from via holes and
  the filling of vias by high-pressure aluminium reflow.[^taguchi-1998]
* Cheung, P2ID 2000, and Wang, Ackaert et al., *IEEE TED* 2004 — charging
  during plasma deposition and of floating MiM
  capacitors.[^cheung-2000][^wang-2004-mim]
* Brunner, SPIE 1991 — why a fixed oxide thickness fixes the swing-curve
  position.[^brunner-1991]
* Philipossian and Sun, *Electrochem. Solid-State Lett.* 2009 — post-ILD-CMP brush
  scrubbing.[^philipossian-2009]

## Open questions

* The cap's precursor, thickness and deposition conditions are not
  public.
* How the 0.505 µm via-4 height[^pdk-04] is split between the polished
  {ref}`NILD6 <step-156>` and this cap is not public.
* Whether any treatment of this surface precedes the metal-5 deposition,
  and whether the surface requirements of an aluminium-filled via change
  the cap's recipe compared with the tungsten-plug levels, is not
  public; the fill reading is set out at {ref}`WTIAL5 <step-161>`.
* Whether "C2" denotes a Novellus Concept Two is an inference from the
  vendor's product names.[^novellus-history]

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology Derivative
    R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005 (copy hosted by
    Infineon Technologies).
    <https://www.infineon.com/assets/row/public/documents/10/316/infineon-014807.rev-2.0-productqualificationreport-en.pdf?fileId=8ac78c8c7d710014017d71486005075b>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992). <https://doi.org/10.1116/1.586361>
[^chapple-sokol-1989]: J. D. Chapple-Sokol, E. Tierney and J. Batey,
    "RF Power Dependence of the Material Properties of PECVD Silicon
    Dioxide", *MRS Proceedings* **165** (1989).
    <https://doi.org/10.1557/PROC-165-113>
[^mani-2007]: S. Mani and T. Saif, "Stress development in
    plasma-deposited silicon dioxide thin-films due to hydrogen
    evolution", *Thin Solid Films* **515**(5), 3120–3125 (2007).
    <https://doi.org/10.1016/j.tsf.2006.08.025>
[^adams-1979]: A. C. Adams and C. D. Capio, "The Deposition of Silicon
    Dioxide Films at Reduced Pressure", *Journal of The Electrochemical
    Society* **126**(6), 1042–1046 (1979). <https://doi.org/10.1149/1.2129171>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
    "Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
    **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^boning-1994]: D. S. Boning, T. Maung, J. E. Chung, K.-J. Chang,
    S.-Y. Oh and D. Bartelink, "Statistical metrology for interlevel
    dielectric thickness variation", *Proc. SPIE* **2334**, Advanced
    Microelectronic Manufacturing, 316–327 (1994).
    <https://doi.org/10.1117/12.186764>
[^chang-1995]: E. Chang, B. Stine, T. Maung, R. Divecha, D. Boning,
    J. Chung, K. Chang, G. Ray, D. Bradbury, O. S. Nakagawa, S. Oh and
    D. Bartelink, "Using a statistical metrology framework to identify
    systematic and random sources of die- and wafer-level ILD thickness
    variation in CMP processes", *IEDM 1995 Technical Digest*,
    pp. 499–502. <https://doi.org/10.1109/IEDM.1995.499247>
[^devriendt-1998]: K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert,
    M. Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP
    Induced Defects and Post-CMP Cleaning Strategies", *Solid State
    Phenomena* **65–66**, 173–176 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>
[^moon-2016]: Y. Moon, "Chemical and physical mechanisms of dielectric
    chemical mechanical polishing (CMP)", in *Advances in Chemical
    Mechanical Planarization (CMP)*, Woodhead Publishing, 2016,
    pp. 3–26, ISBN 978-0-08-100165-3.
    <https://doi.org/10.1016/B978-0-08-100165-3.00001-2>
[^kobayakawa-1991]: M. Kobayakawa, A. Arimatsu, F. Yokoyama,
    N. Hirashita and T. Ajioka, "A study of outgassing from spin-on-glass
    films used for planarization", *Proc. Eighth International IEEE VLSI
    Multilevel Interconnection Conference (VMIC 1991)*, pp. 454–456.
    <https://doi.org/10.1109/VMIC.1991.153054>
[^taguchi-1998]: M. Taguchi, K. Maeda and J. Aoyama, "Improvement of
    filling capability by control of water outgassing from via holes in
    high-pressure aluminum reflow technology", in *Fourth International
    Workshop on Stress Induced Phenomena in Metallization*, AIP, 1998,
    pp. 407–412. <https://doi.org/10.1063/1.54662>
[^cheung-2000]: K. P. Cheung, "On the mechanism of plasma enhanced
    dielectric deposition charging damage", *Proc. 2000 5th
    International Symposium on Plasma Process-Induced Damage (P2ID)*,
    pp. 161–163. <https://doi.org/10.1109/PPID.2000.870658>
[^wang-2004-mim]: Z. Wang, J. Ackaert, C. Salm, F. G. Kuper, M. Tack,
    E. De Backer, P. Coppens, L. De Schepper and B. Vlachakis,
    "Plasma-charging damage of floating MIM capacitors", *IEEE
    Transactions on Electron Devices* **51**(6), 1017–1024 (2004).
    <https://doi.org/10.1109/TED.2004.829518>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^philipossian-2009]: A. Philipossian and T. Sun, "Frictional Analysis
    of Various Poly(vinyl alcohol) Brush Roller Designs for
    Post-Interlevel Dielectric CMP Scrubbing Applications",
    *Electrochemical and Solid-State Letters* **12**(3), H84 (2009).
    <https://doi.org/10.1149/1.3058994>
