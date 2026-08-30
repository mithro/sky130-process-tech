(step-005)=
# Step 005 — STINITE: Shallow trench nitride etch

| | |
|---|---|
| **Step number** | 5 of 171 |
| **Step code** | `STINITE` |
| **Category** | {ref}`Etch <category-etch>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`FOM <step-004>` |
| **Next step** | {ref}`STIE <step-006>` |

## What this step is

`STINITE` (shallow-trench-isolation nitride etch) is a plasma etch that
transfers the resist pattern from {ref}`FOM <step-004>` into the hard
mask: it removes the BARC (if one is used), the isolation nitride
({ref}`ISONIT <step-003>`) and the pad oxide ({ref}`BOX <step-002>`)
wherever the resist is open, stopping on silicon. When it is finished
the future field regions are bare silicon and the future active
regions are still covered by resist / nitride / pad oxide.

In many fabs this etch and the silicon trench etch that follows
({ref}`STIE <step-006>`) are run back-to-back in the same chamber as
one multi-step recipe; SKY130's step list keeps them as two steps,
which may reflect separate chambers, separate tools, or simply
separate recipe/inspection points. We treat them separately here but
note that the hand-off is not public.

## Step category

`STINITE` is an {ref}`Etch <category-etch>` step — a fluorocarbon
dielectric etch of nitride and oxide, distinct from the halogen
silicon etch at {ref}`STIE <step-006>`. Similar nitride-opening etches
occur later at {ref}`SPE <step-077>` (spacer) and
{ref}`NPCME <step-079>`.

## Why this step exists

The trench etch cannot be done through resist alone: a silicon etch in
HBr/Cl₂ chemistry needs a hard mask that survives the etch, the
subsequent resist strip and the liner oxidation. The nitride/oxide
stack provides that, but it must first be opened in the field with a
clean, vertical profile. The nitride-etch profile matters because:

* the nitride sidewall becomes the upper part of the trench sidewall
  and sets the top of the trench opening, hence the trench width and
  the fill aspect ratio (THUNG-2016);
* any nitride *foot* or *taper* would be copied into the silicon by
  the subsequent trench etch and shift the active CD;
* any pad-oxide residue left in the field would micro-mask the silicon
  etch and leave silicon grass at the trench floor.

## How it is typically performed

An industry-generic recipe for a 200 mm, 130 nm-era fab:

1. **BARC open.** A short O₂- or N₂/O₂-based (sometimes CF₄/O₂) step
   removes the organic anti-reflective layer in the open areas.
2. **Nitride main etch.** Fluorocarbon chemistry — CF₄, CHF₃ and O₂ (or
   CF₄/O₂ with a little Ar) — in a medium-density or high-density
   plasma. Fluorine radicals etch nitride; CHF₃ adds polymerising
   carbon that protects the sidewall and gives anisotropy; O₂ trims the
   polymer (TXT-02, WIKI-RIE: "High-energy ions from the plasma attack
   the wafer surface and react with it", giving "very anisotropic etch
   profiles"). Gas pressure in RIE is "typically maintained in a range
   between a few millitorr and a few hundred millitorr" (WIKI-RIE).
3. **Endpoint.** Optical emission spectroscopy on a nitrogen-containing
   etch product detects the nitride/oxide interface (TXT-02); a timed
   over-etch then clears the pad oxide.
4. **Pad-oxide breakthrough.** A short CF₄- or CHF₃-rich step removes
   the 10–20 nm pad oxide and exposes silicon; selectivity to silicon
   is kept modest so that the surface is not pitted.
5. **Hand-off.** Either continue *in situ* to the silicon trench etch
   ({ref}`STIE <step-006>`) or vent and transfer.

SkyWater's own capability list names exactly these gases on its
silicon/nitride etchers: "AMAT DPSII, HBR, Cl2, NF3, CF4, CHF3, O2 –
gate, trench, W/WN" and "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6,
O2" (SKW-01).

Typical numbers for fluorocarbon nitride etching (TXT-02, TXT-05):
etch rates of the order of 100–300 nm/min, so a 150 nm nitride plus
over-etch takes about a minute; selectivity to resist of roughly
1–2 : 1 (which is why the 1.14 µm resist of PDK-03 is comfortable for
a ~200 nm stack).

## Machines typically used

* **Dielectric / nitride plasma etcher**, 200 mm single-wafer,
  fluorocarbon chemistry: Lam 4520/4420 and 9400 TCP (with CF₄/O₂),
  AMAT Centura DPS or MxP/eMax dielectric chambers, TEL DRM / Unity.
* **Optical emission endpoint** system on the chamber.
* **CD-SEM** for post-etch CD; **defect inspection** for residue.

## Machines likely used at SkyWater

* **AMAT DPS II (Centura).** SKW-01 lists it with CF₄ and CHF₃ among its
  gases and "trench" among its applications. Strength: strong that the
  tool and gases exist; **inference** that this step runs on it.
* **Lam 9400 TCP.** SKW-01: "Lam 9400 TCP, poly/nitride, HBr, CF4, SF6,
  O2". Strength: strong that a nitride-capable TCP etcher exists;
  inference for this step. The 9400 is a transformer-coupled
  high-density plasma etcher originally designed for polysilicon
  (SNF-9400).
* **Lam 4400.** SKW-01: "Lam 4400, HBr, Cl2, C2F6, CF4, SF6, O2".
  Strength: strong for existence; a possible legacy home for this
  etch.

Which of the three carries the isolation nitride etch is not public.

## Resources required

* **CF₄, CHF₃, O₂** (and possibly Ar or N₂) process gases (SKW-01,
  TXT-02).
* **Helium** for backside wafer cooling.
* **Chamber-clean gases** (O₂, NF₃ or SF₆) between wafers or lots.
* **Consumable chamber parts** — focus rings, liners, electrostatic-
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

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 (DPSII, Lam 9400 TCP and Lam 4400 gas lists).
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions*
  (photoresist thickness 1.14 µm).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **SNF-9400** — Stanford Nanofabrication Facility, *Lam Research TCP
  9400 Poly Etcher (lampoly)* equipment page ("Transformer Coupled
  Plasma (TCP) etcher, generates a uniform, high density plasma for
  selective etching of silicon and polysilicon"; gases include
  chlorine, hydrogen bromide, oxygen, tetrafluoromethane).
  <https://snfguide.stanford.edu/guide/equipment/lam-research-tcp-9400-poly-etcher-lampoly>

### High-level understanding

* **WIKI-RIE** — Wikipedia, *Reactive-ion etching*.
  <https://en.wikipedia.org/wiki/Reactive-ion_etching>
* **WIKI-STI** — Wikipedia, *Shallow trench isolation* ("Dry etch
  (Reactive-ion etching)" step).
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4 (plasma-etch chapter: fluorocarbon etching of
  SiO₂ and Si₃N₄).
  <https://openlibrary.org/isbn/9780961672164>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (STI etch).
  <https://openlibrary.org/isbn/9780961672171>

### Deep dive

* **THUNG-2016** — B. J. Thung et al., "Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform", *JTEC* 8(5),
  2016, pp. 15–21 (fill aspect ratio defined by trench depth plus
  nitride thickness).
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>
* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297.

## Open questions

* Whether `STINITE` and `STIE` run in one chamber as one recipe, or on
  different tools, is not public.
* The exact chemistry (CF₄/CHF₃/O₂ versus CF₄/O₂ or CHF₃/O₂) and
  whether a BARC is present are inferred from the era and from
  SKW-01's gas lists.
* Whether the pad oxide is fully cleared here or left as a thin screen
  for the start of the silicon etch is not public.
