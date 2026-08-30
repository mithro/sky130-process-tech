(step-011)=
# Step 011 — FILOX: Fill oxide deposition

| | |
|---|---|
| **Step number** | 11 of 171 |
| **Step code** | `FILOX` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — isolation |
| **Previous step** | {ref}`LINOX <step-010>` |
| **Next step** | {ref}`CMPNIT <step-012>` |

## What this step is

`FILOX` (fill oxide) deposits a thick blanket of silicon dioxide over
the whole wafer, filling the lined isolation trenches from
{ref}`LINOX <step-010>` and burying the nitride-covered active areas.
This deposited oxide *is* the field oxide of the finished device: the
PDK's stack drawing labels it "FOX K=3.9" (PDK-04), and after the
polish at {ref}`CMPNIT <step-012>` and the nitride strip at
{ref}`NS19 <step-013>` it is the dielectric that separates every
transistor from its neighbours and on which the field poly and the
first interconnect run.

The film must be thick enough to fill the deepest trench and still
stand well above the nitride everywhere — typically 1.5–2 × the
(trench + nitride) height, i.e. of the order of 0.5–0.7 µm for a
~0.3 µm trench (era-typical figures; TXT-05). At the 130 nm node the deposition method is
high-density-plasma chemical vapour deposition (HDP-CVD): "High
Density Plasma (HDP) and Chemical Vapor Deposition (CVD) is the
industry standard for STI oxide" (THUNG-2016), and Novellus was still
calling HDP "the preferred gapfill dielectric technology for advanced
geometries" in 2009 (LAM-SPEED). The PDK gives no fill thickness; it
gives the *final* field-oxide top at 0.3262 µm on its stack scale
(PDK-04) and the field-oxide step above the silicon surface under poly
as 0.07 µm (PDK-03).

## Step category

`FILOX` is a {ref}`Thin-film deposition <category-deposition>` step —
a plasma CVD of undoped silicon oxide. It is the first of many CVD
oxides in the flow; later ones ({ref}`PSG <step-089>`,
{ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`, …) fill gaps
between poly and metal lines and use PECVD TEOS, PSG or HDP as the
topography demands. The isolation fill is distinctive because its gaps
are the narrowest and deepest in the front end and because it is
followed immediately by a polish that stops on nitride.

## Why this step exists

The trench is only an isolation structure once it is full of
insulator. The fill has to be:

* **Void-free.** A seam or void in the trench is opened by later
  etches and cleans and then fills with polysilicon at
  {ref}`SAGD <step-048>`, causing "poly stringer" shorts — precisely
  the 0.13 µm yield-loss mechanism analysed in THUNG-2016 ("HDP
  deposition void at the special Shallow Trench Isolation (STI) wall
  structure causes poly stringer after poly deposition process").
* **Dense.** The oxide must survive the many HF-containing cleans that
  follow without etching faster than thermal oxide, or it will recess
  below the active surface and form divots at the active edge.
* **Low in hydrogen and moisture.** HDP oxide from silane is "a nearly
  hydrogen-free film" (WIKI-PECVD), but the hydrogen that is present can
  reach the gate oxide (NISHIMURA-2002).
* **Uniform in thickness** over dense and isolated patterns, because
  the polish at {ref}`CMPNIT <step-012>` has to clear it everywhere
  without over-polishing the nitride. This is why the FOM layer carries
  fill "waffles" in wide field regions (PDK-06).

## How it is typically performed

An industry-generic HDP-CVD STI fill for a 200 mm, 130 nm-era fab:

1. **Chamber.** Inductively coupled high-density plasma reactor with an
   RF-biased electrostatic chuck; wafer temperature of a few hundred
   °C set by backside helium and plasma heating (TXT-05). In a high-density plasma "the
   ion density can be high enough that significant sputtering of the
   deposited film occurs; this sputtering can be employed to help
   planarize the film and fill trenches or holes" (WIKI-PECVD).
2. **Chemistry.** Silane, oxygen and argon: "High-density plasma
   deposition of silicon dioxide from silane and oxygen/argon has been
   widely used to create a nearly hydrogen-free film with good
   conformality over complex surfaces" (WIKI-PECVD). Argon (and the
   oxygen ions) provide the simultaneous sputter component; the
   deposition-to-sputter ratio is the key tuning parameter for
   gap-fill (THUNG-2016; the Novellus release speaks of "tailoring the
   deposition, etch, and sputter-to-deposition (S/D) ratio",
   LAM-SPEED). A published 0.13 µm STI gap-fill study is based on the
   same SiH₄–O₂–Ar HDP-CVD system (NISHIMURA-2002).
3. **Sequence.** A short *in-situ* sputter-clean or a thin protective
   liner deposition at low bias (so that the sputter component does
   not clip the nitride corners and redeposit silicon-rich material on
   the trench sidewall), then the main fill at higher bias, then an
   unbiased cap. Multi-step deposition/etch/deposition sequences are
   used for the tightest gaps.
4. **Post-deposition.** Some fabs densify the HDP oxide in a furnace
   or RTP anneal in N₂ at around 900–1000 °C (TXT-05); others rely on
   the later thermal steps. An anneal here also continues the deep N-well
   ({ref}`DNI <step-008>`) drive.
5. **Metrology.** Thickness and uniformity by optical reflectometry;
   in-trench fill quality by cross-section SEM on sample wafers; wet
   etch rate ratio (against thermal oxide) as a density monitor.

SkyWater lists the capability directly: "Lam/Novellus High Density
Plasma (HDP) doped and phos doped with sputter etch" among its film
deposition tools (SKW-01), and a SkyWater maintenance technician's
profile refers to "the Novellus high density plasma tool" (SKW-07).

## Machines typically used

* **HDP-CVD reactor**, 200 mm single-wafer, multi-chamber cluster:
  Novellus SPEED, Applied Materials Ultima HDP-CVD (Centura), Lam
  (post-2012 Novellus SPEED Max/NExT), Trikon Planar 200. Novellus'
  SPEED platform was the market's long-running STI fill tool
  (LAM-SPEED).
* **Furnace or RTP** for optional densification.
* **Reflectometer / ellipsometer**; **cross-section SEM**.

## Machines likely used at SkyWater

* **Novellus (now Lam) HDP-CVD.** SKW-01 names "Lam/Novellus High
  Density Plasma (HDP)" with sputter etch, and SKW-07 names "the
  Novellus high density plasma tool". Strength: strong (two SkyWater
  statements). The model (SPEED is the Novellus HDP product line) is
  our inference, not a SkyWater statement.
* **Aviza furnace** for any densification anneal (SKW-01). Strength:
  strong for existence; the existence of a densification step is an
  inference.

## Resources required

* **Silane (SiH₄)** — pyrophoric, delivered through gas cabinets
  (WIKI-PECVD).
* **Oxygen** and **argon** (WIKI-PECVD).
* **Helium** for backside cooling; **nitrogen** purge.
* **NF₃** (with argon/oxygen) for the remote-plasma chamber clean —
  the Novellus release refers to the "enlarged remote plasma source"
  that "allows more wafers to be processed between plasma cleans"
  (LAM-SPEED).
* Chamber consumables — ceramic dome, gas ring, ESC.
* SkyWater names Air Products, Praxair, Linde and Airgas as gas
  suppliers (SEC-01, SEC-02) without tying them to a step.

## Related steps and cross-references

* Previous: {ref}`LINOX <step-010>` (liner under the fill).
* Next: {ref}`CMPNIT <step-012>` (polish of this film, stopping on
  the nitride from {ref}`ISONIT <step-003>`).
* Trench geometry from {ref}`STIE <step-006>`; fill "waffles" from
  {ref}`FOM <step-004>`.
* The resulting field oxide appears as FOX in the PDK stack and is the
  surface under field poly at {ref}`P1M <step-061>` and under local
  interconnect at {ref}`LI1M <step-102>`.
* Other gap-fill oxides: {ref}`PSG <step-089>`,
  {ref}`NILD2 <step-105>`, {ref}`NILD3 <step-115>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* **SKW-01** — SkyWater Technology, *Facilities & Capabilities*,
  accessed 2026-08-30 ("Lam/Novellus High Density Plasma (HDP) doped
  and phos doped with sputter etch").
  <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
* **SKW-07** — SkyWater Technology, *A Day in the Life of a SkyWater
  Maintenance Technician*, 2023-12-14 ("Novellus high density plasma
  tool").
  <https://www.skywatertechnology.com/a-day-in-the-life-of-a-skywater-maintenance-technician/>
* **PDK-03** — SkyWater PDK Authors, *Criteria & Assumptions* (field
  oxide 0.07 µm above silicon under poly).
  <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
* **PDK-04** — SkyWater PDK Authors, *Process stack diagram* ("FOX
  K=3.9"; 0.3262 µm).
  <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
* **PDK-06** — SkyWater PDK Authors, *Layers Reference*
  ("fom_waffles").
  <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>
* **SEC-01** — SkyWater Technology, Inc., Form S-1, 2021-03-22.
  <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
* **SEC-02** — SkyWater Technology, Inc., Form 10-K for fiscal 2023.
  <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
* **LAM-SPEED** — Novellus Systems (Lam Research newsroom), *Novellus'
  SPEED Max HDP-CVD Dielectric Gapfill System Extends STI Application
  to 32nm*, 2009-10-05.
  <https://newsroom.lamresearch.com/2009-10-05-NOVELLUS-SPEED-R-MAX-HDP-CVD-DIELECTRIC-GAPFILL-SYSTEM-EXTENDS-STI-APPLICATION-TO-32nm>

### High-level understanding

* **WIKI-PECVD** — Wikipedia, *Plasma-enhanced chemical vapor
  deposition* (high-density plasma, sputtering during deposition,
  SiH₄/O₂/Ar oxide).
  <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
* **WIKI-STI** — Wikipedia, *Shallow trench isolation*.
  <https://en.wikipedia.org/wiki/Shallow_trench_isolation>
* **TXT-05** — S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4*,
  Lattice Press, 2002, ISBN 978-0-9616721-7-1 (HDP-CVD and STI fill).
  <https://openlibrary.org/isbn/9780961672171>
* **TXT-02** — S. Wolf and R. N. Tauber, *Silicon Processing for the
  VLSI Era, Vol. 1*, 2nd ed., Lattice Press, 2000,
  ISBN 978-0-9616721-6-4 (CVD of SiO₂).
  <https://openlibrary.org/isbn/9780961672164>

### Deep dive

* **NISHIMURA-2002** — H. Nishimura, S. Takagi, M. Fujino and N. Nishi,
  "Gap-Fill Process of Shallow Trench Isolation for 0.13 µm
  Technologies", *Jpn. J. Appl. Phys.* 41 (2002) 2886–2893,
  DOI 10.1143/JJAP.41.2886.
* **THUNG-2016** — B. J. Thung et al., "Challenges for 0.13µm Generation
  Shallow Trench Isolation on 0.18µm Equipment Platform", *JTEC* 8(5),
  2016, pp. 15–21.
  <https://jtec.utem.edu.my/jtec/article/download/697/707/3255>
* **REV-01** — M. Nandakumar et al., "Shallow trench isolation for
  advanced ULSI CMOS technologies", *IEDM 1998*, pp. 133–136,
  DOI 10.1109/IEDM.1998.746297.
* **ITRS-01** — ITRS 2001, *Front End Processes* (thin films for
  trench fill: "high aspect ratio gaps, top and bottom corner profile
  control").
  <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>

## Open questions

* The SKY130 fill thickness, deposition temperature, D/S ratio and
  whether a densification anneal follows are not public.
* Whether the fill was HDP from the start of S8 (2003) or whether an
  earlier TEOS/ozone or PECVD fill was used and later replaced is
  unknown; SKW-01 describes the fab today.
* The HDP tool model (SPEED versus another Novellus/Lam HDP product) is
  inferred from the vendor name only.
