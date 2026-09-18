(step-005)=
# Step 005 — STINITE: Shallow trench nitride etch

| | |
|---|---|
| **Step number** | 5 of 171[^steps-sheet] |
| **Step code** | `STINITE` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`FOM <step-004>` |
| **Next step** | {ref}`STIE <step-006>` |

## What this step is

`STINITE` (shallow-trench-isolation nitride etch) is a plasma etch that
transfers the resist pattern from {ref}`FOM <step-004>` into the hard
mask: it removes the {term}`BARC` (if one is used), the isolation nitride
({ref}`ISONIT <step-003>`) and the pad oxide ({ref}`BOX <step-002>`)
wherever the resist is open, stopping on silicon. When it is finished
the future field regions are bare silicon and the future active
regions are still covered by resist / nitride / pad oxide.

In many fabs this etch and the silicon trench etch that follows
({ref}`STIE <step-006>`) are run back-to-back in the same chamber as
one multi-step recipe; this reference keeps them as two steps because
they are distinct unit processes with different chemistries. We treat them separately here but
note that the hand-off is not public.

## Step category

`STINITE` is an {ref}`Etch <category-etch>` step — a fluorocarbon
dielectric etch of nitride and oxide, distinct from the halogen
silicon etch at {ref}`STIE <step-006>`. Similar nitride-opening etches
occur later at {ref}`SPE <step-077>` ({term}`spacer`) and
{ref}`NPCME <step-079>`.

## Why this step exists

The trench etch cannot be done through resist alone: a silicon etch in
HBr/Cl₂ chemistry needs a {term}`hard mask` that survives the etch, the
subsequent resist strip and the liner oxidation. The nitride/oxide
stack provides that, but it must first be opened in the field with a
clean, vertical profile. The nitride-etch profile matters because:

* the nitride sidewall becomes the upper part of the trench sidewall
  and sets the top of the trench opening, hence the trench width; the
  fill {term}`aspect ratio` is defined on the sum of the trench depth
  and the nitride thickness,[^thung-2016] so both enter the HDP fill
  window;[^txt-05]
* any nitride *foot* or *taper* would be copied into the silicon by
  the subsequent trench etch and shift the active {term}`CD`;
* any pad-oxide residue left in the field would micro-mask the silicon
  etch and leave silicon grass at the trench floor.

## How it is typically performed

An industry-generic recipe for a 200 mm, 130 nm-era fab:

1. **BARC open.** A short O₂- or N₂/O₂-based (sometimes CF₄/O₂) step
   removes the organic anti-reflective layer in the open areas.
2. **Nitride main etch.** Fluorocarbon chemistry — CF₄, CHF₃ and O₂ (or
   CF₄/O₂ with a little Ar) — in a medium-density or high-density
   plasma. Fluorine radicals etch nitride; CHF₃ adds polymerising
   carbon that protects the sidewall and gives {term}`anisotropy`; O₂ trims the
   polymer[^txt-02] (Wikipedia: "High-energy ions from the plasma
   attack the wafer surface and react with it", giving "very
   anisotropic etch profiles"[^wiki-rie]). Gas pressure in {term}`RIE` is
   "typically maintained in a range between a few millitorr and a few
   hundred millitorr".[^wiki-rie]
3. **{term}`Endpoint <endpoint>`.** Optical emission spectroscopy on a nitrogen-containing
   etch product detects the nitride/oxide interface;[^txt-02] a timed
   {term}`over-etch` then clears the pad oxide.
4. **Pad-oxide breakthrough.** A short CF₄- or CHF₃-rich step removes
   the 10–20 nm pad oxide and exposes silicon; {term}`selectivity` to silicon
   is kept modest so that the surface is not pitted.
5. **Hand-off.** Either continue *in situ* to the silicon trench etch
   ({ref}`STIE <step-006>`) or vent and transfer.

SkyWater's own capability list names exactly these gases on its
silicon/nitride etchers: "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2 –
gate, trench, W/WN" and "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6,
O2".[^skw-01]

Typical numbers for fluorocarbon nitride etching:[^txt-02][^txt-05]
etch rates of the order of 100–300 nm/min, so a 150 nm nitride plus
over-etch takes about a minute; selectivity to resist of roughly
1–2 : 1 (which is why the 1.14 µm resist of the PDK assumptions
page[^pdk-03] is comfortable for a ~200 nm stack).

## Machines typically used

* **{ref}`Dielectric/nitride plasma etcher <machine-plasma-etcher-dielectric>`**, 200 mm single-wafer,
  fluorocarbon chemistry: Lam 4520/4420 and 9400 {term}`TCP` (with CF₄/O₂),
  AMAT Centura DPS or MxP/eMax dielectric chambers, TEL DRM / Unity.
* **Optical emission endpoint** system on the chamber.
* **{ref}`CD-SEM <machine-cd-sem-overlay-metrology>`** for post-etch CD; **{ref}`defect inspection <machine-defect-inspection>`** for residue.

## Machines likely used at SkyWater

* **Lam 9400 TCP.** SkyWater lists "Lam 9400 TCP, poly/nitride, HBr,
  CF4, SF6, O2".[^skw-01] Strength: strong that a nitride-capable TCP
  etcher exists; **inference** for this step, the entry being the only
  one on the list that names nitride. The 9400 is a
  transformer-coupled high-density plasma etcher which Stanford's
  facility describes as being "for selective etching of silicon and
  polysilicon".[^snf-9400]
* **AMAT DPS II (Centura).** SkyWater lists it with CF₄ and CHF₃ among
  its gases and "trench" among its applications.[^skw-01] Strength:
  strong that the tool and gases exist; **medium** for this step,
  since its CF₄ and CHF₃ etch nitride although the entry names no
  nitride application.
* **Lam 4400.** SkyWater lists "Lam 4400, HBr, Cl2, C2F6, CF4, SF6,
  O2".[^skw-01] Strength: strong for existence; **weak** for this
  step, as the entry names no application.

Which of the three carries the isolation nitride etch is not public.

## Resources required

* **{ref}`CF₄ <material-etch-gases>`, CHF₃, {ref}`O₂ <material-process-gases>`** (and possibly Ar or N₂) process
  gases.[^skw-01][^txt-02]
* **Helium** for backside wafer cooling.
* **Chamber-clean gases** (O₂, NF₃ or SF₆) between wafers or lots.
* **{ref}`Consumable chamber parts <material-hardware-consumables>`** — focus rings, liners, electrostatic-
  chuck surfaces.

## Related steps and cross-references

* Previous: {ref}`FOM <step-004>` (resist pattern).
* Next: {ref}`STIE <step-006>` (silicon trench etch through this
  opening).
* Films etched: {ref}`ISONIT <step-003>` nitride and
  {ref}`BOX <step-002>` pad oxide.
* Other nitride etches: {ref}`SPE <step-077>`, {ref}`NPCME <step-079>`,
  {ref}`NSME <step-166>`.
* Category page: {ref}`Etch <category-etch>`.

## References

### Cross-check

* SkyWater, *Facilities & Capabilities* — the DPSII, Lam 9400 TCP and
  Lam 4400 gas lists.[^skw-01]
* SkyWater PDK, *Criteria & Assumptions* — photoresist thickness
  1.14 µm.[^pdk-03]
* Stanford Nanofabrication Facility, *Lam Research TCP 9400 Poly
  Etcher* — "Transformer Coupled Plasma (TCP) etcher, generates a
  uniform, high density plasma for selective etching of silicon and
  polysilicon"; gases include chlorine, hydrogen bromide, oxygen and
  tetrafluoromethane.[^snf-9400]

### High-level understanding

* Wikipedia, *Reactive-ion etching* — ion-assisted anisotropy and
  operating pressures.[^wiki-rie]
* Wikipedia, *Shallow trench isolation* — the "Dry etch (Reactive-ion
  etching)" step.[^wiki-sti]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 — the
  plasma-etch chapter: fluorocarbon etching of SiO₂ and
  Si₃N₄.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — the {term}`STI`
  etch.[^txt-05]

### Deep dive

* Thung et al., *JTEC* 2016 — fill aspect ratio defined by trench
  depth plus nitride thickness.[^thung-2016]
* Nandakumar et al., IEDM 1998 — the STI review, including trench
  definition through the nitride/oxide stack.[^rev-01]
* Coburn and Winters, *J. Appl. Phys.* 1979 — how ion and electron
  bombardment enhances gas–surface reactions, examined for Si, SiO₂ and
  Si₃N₄ with XeF₂, F₂ and Cl₂.[^coburn-1979]
* Oehrlein et al., *J. Vac. Sci. Technol. A* 1994 — fluorocarbon
  high-density plasmas with CF₄ and CHF₃: polymer deposition versus
  etching, the mechanism behind sidewall passivation.[^oehrlein-1994]
* Kastenmeier, Matsuo and Oehrlein, *J. Vac. Sci. Technol. A* 1999 —
  how to etch silicon nitride selectively over silicon and silicon
  dioxide in fluorine-based plasmas.[^kastenmeier-1999]
* Regis et al., ASMC 1997 — a production RIE recipe for silicon nitride
  with high selectivity to oxide, with the process-window
  data.[^regis-1997]
* Flamm, *Pure Appl. Chem.* 1990 — mechanisms of silicon etching in
  fluorine- and chlorine-containing plasmas, relevant to the pad-oxide
  breakthrough and the silicon stop.[^flamm-1990]
* Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing* — the textbook on inductively and
  capacitively coupled etch reactors.[^lieberman-2005]
* Ogle (Lam Research), US 4,948,458 — the transformer-coupled planar
  plasma source behind the Lam TCP 9400 family.[^pat-tcp-lam]
* Bawolek, ASTM STP 960 (1987) — a Monte Carlo treatment of plasma-etch
  emission endpoint, i.e. how the signal used at step 3 above
  behaves.[^bawolek-1987]
* Hon, SJSU master's thesis 2003 — characterisation of line-edge
  roughness in an STI etch, a metrology view of the nitride/trench
  profile.[^hon-2003]

## Open questions

* Whether `STINITE` and `STIE` run in one chamber as one recipe, or on
  different tools, is not public.
* The exact chemistry (CF₄/CHF₃/O₂ versus CF₄/O₂ or CHF₃/O₂) and
  whether a BARC is present are inferred from the era and from
  SkyWater's gas lists.[^skw-01]
* Whether the pad oxide is fully cleared here or left as a thin screen
  for the start of the silicon etch is not public.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^snf-9400]: Stanford Nanofabrication Facility, *Lam Research TCP 9400
    Poly Etcher (lampoly)*, equipment page.
    <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>
[^wiki-rie]: Wikipedia, *Reactive-ion etching*.
    <https://en.wikipedia.org/wiki/Reactive-ion_etching>
[^wiki-sti]: Wikipedia, *Shallow trench isolation*.
    <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^thung-2016]: B. J. Thung, K. Ibrahim, N. A. Manap and F. Salehuddin,
    "Challenges for 0.13µm Generation Shallow Trench Isolation on
    0.18µm Equipment Platform", *Journal of Telecommunication,
    Electronic and Computer Engineering* **8**(5), 15–21 (2016).
    <https://jtec.utem.edu.my/jtec/article/view/697>
[^rev-01]: M. Nandakumar, A. Chatterjee, S. Sridhar, K. Joyner,
    M. Rodder and I.-C. Chen, "Shallow trench isolation for advanced
    ULSI CMOS technologies", *IEDM 1998 Technical Digest*, pp. 133–136.
    <https://doi.org/10.1109/IEDM.1998.746297>
[^coburn-1979]: J. W. Coburn and H. F. Winters, "Ion- and
    electron-assisted gas-surface chemistry — An important effect in
    plasma etching", *Journal of Applied Physics* **50**(5), 3189–3196
    (1979). <https://doi.org/10.1063/1.326355>
[^oehrlein-1994]: G. S. Oehrlein, Y. Zhang, D. Vender and M. Haverlag,
    "Fluorocarbon high-density plasmas. I. Fluorocarbon film deposition
    and etching using CF₄ and CHF₃", *Journal of Vacuum Science &
    Technology A* **12**(2), 323–332 (1994).
    <https://doi.org/10.1116/1.578876>
[^kastenmeier-1999]: B. E. E. Kastenmeier, P. J. Matsuo and
    G. S. Oehrlein, "Highly selective etching of silicon nitride over
    silicon and silicon dioxide", *Journal of Vacuum Science &
    Technology A* **17**(6), 3179–3184 (1999).
    <https://doi.org/10.1116/1.582097>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^flamm-1990]: D. L. Flamm, "Mechanisms of silicon etching in fluorine-
    and chlorine-containing plasmas", *Pure and Applied Chemistry*
    **62**(9), 1709–1720 (1990). <https://doi.org/10.1351/pac199062091709>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles
    of Plasma Discharges and Materials Processing*, 2nd ed., Wiley,
    2005, ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
[^pat-tcp-lam]: J. S. Ogle (Lam Research Corporation), *Method and
    apparatus for producing magnetically-coupled planar plasma*,
    US 4,948,458 A, granted 1990-08-14.
    <https://patents.google.com/patent/US4948458A/en>
[^bawolek-1987]: E. J. Bawolek, "Monte Carlo Simulation of Plasma Etch
    Emission Endpoint", in *Emerging Semiconductor Technology*, ASTM STP
    960, ASTM International, 1987, pp. 190–203.
    <https://doi.org/10.1520/STP25751S>
[^hon-2003]: B. M. Hon, *Characterization of shallow trench isolation
    etch line edge roughness*, master's thesis, San José State
    University, 2003. <https://doi.org/10.31979/etd.53yx-bwm5>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
