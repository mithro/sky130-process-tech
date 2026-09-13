(step-076)=
# Step 076 — SPNIT: Spacer nitride deposition

| | |
|---|---|
| **Step number** | 76 of 171[^steps-sheet] |
| **Step code** | `SPNIT` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`TIPRTAD <step-075>` |
| **Next step** | {ref}`SPE <step-077>` |

## What this step is

`SPNIT` deposits a blanket, conformal silicon nitride film over the
whole wafer — over the capped gate lines and resistor bodies, down
their sidewalls and across the source/drain silicon whose tips and
halos were activated at {ref}`TIPRTAD <step-075>`. The film is not a
device layer in itself: the next step, {ref}`SPE <step-077>`, etches
it back anisotropically until it survives only as a sidewall
{term}`spacer` on every vertical edge. The deposited thickness
therefore becomes, to first order, the width of the spacer, and the
spacer width is what sets the offset between the gate edge and the
deep source/drain junctions implanted at {ref}`PSDI <step-082>` and
{ref}`NSDI <step-086>`.

Two public facts bear on the step. The PDK's process stack
diagram names a dielectric "SPNIT" with a relative permittivity of
7.5,[^pdk-04] the value of silicon nitride, alongside the other
front-end dielectrics (the field and inter-level oxides at 3.9–4.5, the
"LINT" nitride at 7.3); this reference uses the same word as the
step's label. And the PDK's assumptions table carries an
"oxide spacer" of 0.05 µm[^pdk-03] — so the finished SKY130 spacer is,
we infer, a composite: an oxide component (the re-oxidation of
{ref}`IOX45 <step-063>` under the nitride, the oxide of
{ref}`SPOX <step-080>` over it, or both) and this nitride. The nitride
thickness itself is not public.

What the film is deposited onto matters for the etch that follows.
On this reading of the flow, the surface is oxide everywhere: the
0.2 µm nitride/oxide cap on top of the gates ({ref}`GATENIT <step-058>`,
{ref}`POC <step-059>`; "poly cap after SPE" 0.2 µm[^pdk-03]), the
{ref}`IOX45 <step-063>` oxide on the gate sidewalls and on the
source/drain silicon, and the trench oxide over the field. Whether
the thin implant/re-oxidation oxide over the source/drain is still
intact after the four tip and halo strips, or has been thinned, is
not public; the spacer etch will stop on it, so its thickness is a
recipe input.

## Step category

`SPNIT` is a {ref}`Thin-film deposition <category-deposition>` step —
a CVD silicon nitride, like {ref}`ISONIT <step-003>` and
{ref}`GATENIT <step-058>` before it and {ref}`LINIT <step-104>`
after. What is specific to this instance is that *conformality* is
the film property that matters most: the spacer width is the
sidewall thickness, so the ratio of sidewall to top thickness
({term}`step coverage`) must be close to one and reproducible across
the wafer, and the film must coat the foot of a roughly 0.4 µm-tall (0.18 µm poly plus the ~0.2 µm cap[^pdk-03]) gate line
on a 0.21 µm space (poly.2)[^pdk-periph] without seaming. The second
distinguishing property is thermal budget: the wafer now carries
annealed arsenic tips and boron halos, and a hot furnace deposition
would move them.

## Why this step exists

The sidewall spacer is the device that makes a lightly doped drain
possible. Ogura et al. introduced the LDD transistor in 1980 to move
the peak drain field away from the gate edge and so limit hot-carrier
damage,[^ogura-1980] and Tsang et al. showed in 1982 how to build it
with an oxide sidewall spacer formed by conformal deposition and
anisotropic etch-back, so that the light and heavy implants are both
self-aligned to the gate without a second mask.[^tsang-1982] Every
CMOS process since has kept the idea: the shallow {term}`extension`
is implanted with the bare gate as the mask ({ref}`ASTI <step-065>`),
the spacer is grown, and the deep source/drain is implanted with the
spacer as the mask. The spacer width is a first-order design
parameter: too narrow and the deep junction encroaches on the channel
and the extension does nothing; too wide and the un-silicided
extension adds series resistance, which Ng and Lynch showed to be a
gate-voltage-dependent term that scales badly.[^ng-1986][^ng-1987]

Nitride rather than oxide is the usual choice at this node for
several reasons that the literature sets out:

* **Etch selectivity.** A nitride spacer can be etched back with high
  selectivity to the oxide under it, so the source/drain silicon is
  not trenched and the gate cap survives;[^regis-1997] Goss and
  Thornburg describe the integration of a nitride spacer into a
  0.35 µm CMOS technology and the process challenges that came with
  it.[^goss-1997]
* **A contact etch stop and cap.** Nitride is what a later
  self-aligned or {term}`borderless contact` etch stops on, and it seals the
  gate stack against the wet chemistry and implants that follow.
* **Fringing field.** The dielectric constant of the spacer sets the
  gate-to-extension fringing capacitance and the fringing field that
  helps the gate control the extension; Mizuno et al. deliberately
  used a high-permittivity spacer for that
  reason,[^mizuno-1989] and Shrivastava and Fitzpatrick[^shrivastava-1982]
  and McAndrew et al.[^mcandrew-1994] give the overlap/fringing
  capacitance models that circuit designers use — the PDK's 7.5 value
  for "SPNIT"[^pdk-04] is exactly the number those models need.

The cost of nitride is hydrogen and stress. CVD nitride carries
hydrogen that can reach the gate oxide, and Sambonsugi and
Sugii,[^sambonsugi-1998] Hwang et al.[^hwang-1996] and Janapaty et
al.[^janapaty-1998] all report hot-carrier behaviour that depends on
whether the spacer is nitride, oxide or a composite; Shimaya traced
part of the effect to water diffusing through nitride
passivation.[^shimaya-1995] Om et al. measured junction leakage for
LDD NMOS with different spacer materials.[^om-1995] The film's stress
matters too: an etch-stop nitride over the gate strains the channel
enough to change drive current, as Ito et al. and Shimizu et al.
showed at the 130 nm generation.[^ito-2000][^shimizu-2001] These are
the reasons a {term}`composite spacer` with an oxide {term}`liner` — which the PDK's
"oxide spacer" entry[^pdk-03] suggests SKY130 has — is common.

Without `SPNIT` there is no offset between extension and deep
junction, and the hot-carrier lifetime, series resistance and
short-channel behaviour of every transistor in the PDK would change.

## How it is typically performed

Industry-generic routes for a spacer nitride in a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

* **LPCVD from dichlorosilane and ammonia.** Hot-wall furnace at
  roughly 700–800 °C and a few hundred mTorr (typical industry
  values, category page[^txt-02][^wiki-sin]); Roenigk and Jensen model
  the reactor,[^roenigk-1987] Habraken and Kuiper review the film
  properties.[^habraken-1994] The film is stoichiometric, dense,
  nearly perfectly conformal, about 1 GPa tensile,[^temple-boyer-1998]
  and deposits on both wafer faces. The drawback is thermal budget:
  minutes at 750 °C after the tips are annealed is a real diffusion
  step, and part of the reason the tip anneal precedes the spacer
  rather than following it.
* **Low-temperature LPCVD from BTBAS.** Bis(tertiary-butylamino)silane
  with ammonia deposits nitride in a furnace at roughly 550–600 °C
  with conformality close to the DCS film; Gumpher et al. characterise
  the process and film,[^gumpher-2004] and Smith, Seutter and Iyer the
  thermal chemistry.[^smith-2005] SkyWater lists "BTBAS" among its
  Aviza furnace processes,[^skw-01] and a low-temperature spacer
  nitride is the most common reason a 130 nm-era fab adopts it — which
  is why we consider it the leading candidate for this step
  (inference; see below).
* **PECVD from silane and ammonia.** Single-wafer, 300–400 °C, with
  hydrogen content and stress set by the plasma conditions;[^smith-1990][^claassen-1985]
  the film's stress can drift irreversibly with later heating.[^hughey-2003]
  Conformality is poorer than LPCVD, which makes the spacer width
  depend on {term}`pattern density`; PECVD spacers are therefore less usual
  at this node, though not unknown.
* **Thickness.** Not public. The spacer width is a fraction of the
  0.15 µm minimum gate length (poly.1a);[^pdk-periph] the PDK's
  0.06 µm "vertical space" entry for the N⁺/P⁺ source/drain
  (variable `LD`)[^pdk-03] is, if we read it as the lateral
  diffusion allowance, a hint at the scale of offset the flow is
  designed around, but it does not give the nitride thickness.
* **Sequence.** Pre-deposition clean (SC-1 class, no HF, so the
  oxides the etch will stop on survive); load; pump and leak check;
  temperature stabilisation; deposition to a timed thickness on
  monitor wafers; purge; unload.
* **Metrology.** Thickness and refractive index by spectroscopic
  ellipsometry on monitors and on unpatterned test pads; stress by
  wafer bow; conformality by cross-section SEM during development;
  particles.

## Machines typically used

* **{ref}`Vertical LPCVD furnace <machine-vertical-furnace-lpcvd>`** (SVG/Thermco–ASML–Aviza AVP/RVP, Kokusai
  Vertron, TEL Alpha-8S, ASM A400) with DCS/NH₃ or BTBAS/NH₃ gas
  panels.
* **{ref}`PECVD system <machine-pecvd>`** (Novellus Concept One/Sequel, Applied Materials
  Producer/Centura DxZ) as the single-wafer alternative.
* **{ref}`Spectroscopic ellipsometer <machine-film-thickness-metrology>`**, **stress gauge**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **Aviza furnace, BTBAS nitride.** SkyWater states that "Furnaces are
  all made by Aviza" and lists, among the furnace processes, LPCVD
  nitride and a BTBAS nitride.[^skw-01] Strength: **strong** for the
  existence of both processes; the assignment of the *spacer* to the
  BTBAS process is an **inference** from the thermal-budget argument
  above, and a DCS/NH₃ LPCVD spacer on the same furnaces is equally
  consistent with the public list. Dealer documentation describes the
  Aviza/SVG AVP-8000 as "a vertical batch furnace with a flexible
  platform for diffusion, oxidation, and LPCVD processes" for
  150–200 mm wafers[^aviza-avp] (weak, a listing rather than a data
  sheet).
* **"C1" PECVD system** — "PECVD nitride C1" is on the same
  list.[^skw-01] Strength: strong for the capability; weak for
  assignment to this step.

## Resources required

* **Dichlorosilane and ammonia** (DCS route)[^wiki-sin] or **BTBAS
  and ammonia** (low-temperature route);[^gumpher-2004] **silane,
  ammonia and nitrogen** for PECVD.[^wiki-pecvd]
* **Nitrogen** purge; **NF₃ or CF₄/O₂** chamber clean for a PECVD
  tool; ammonium-chloride trap maintenance and HCl-tolerant exhaust
  for a DCS furnace.[^txt-02]
* **Quartz ware** (furnace) or chamber consumables (PECVD).
* **Monitor wafers** (SEMI M8 class)[^semi-m8] for thickness, stress
  and particle control.

## Related steps and cross-references

* Previous: {ref}`TIPRTAD <step-075>` (the tip anneal that fixes the
  extensions before the spacer thermal cycle). Next:
  {ref}`SPE <step-077>` (the etch-back that forms the spacer).
* The oxide the film is deposited on: {ref}`IOX45 <step-063>`; the
  cap it covers: {ref}`GATENIT <step-058>`, {ref}`POC <step-059>`.
* The oxide component of the spacer: {ref}`SPOX <step-080>`; the
  implants the finished spacer masks: {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`.
* Where the nitride is later cut for contacts: {ref}`NPCM <step-078>`,
  {ref}`NPCME <step-079>`.
* Other nitrides: {ref}`ISONIT <step-003>`, {ref}`ONO <step-040>`,
  {ref}`GATENIT <step-058>`, {ref}`LINIT <step-104>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, process stack diagram — "SPNIT K=7.5".[^pdk-04]
* SkyWater PDK, *Criteria & Assumptions* — "oxide spacer" 0.05 µm;
  "poly cap after SPE" 0.2 µm; N⁺/P⁺ S/D junction entries.[^pdk-03]
* SkyWater PDK, *Periphery rules* — poly.1a 0.150 µm, poly.2
  0.210 µm.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — Aviza furnaces with LPCVD
  nitride and BTBAS nitride; "PECVD nitride C1".[^skw-01]
* Moov, *Aviza / SVG / Thermco AVP 8000* listing — the furnace
  class.[^aviza-avp]

### High-level understanding

* Wikipedia, *Silicon nitride* — LPCVD and PECVD nitride.[^wiki-sin]
* Wikipedia, *Plasma-enhanced chemical vapor deposition*.[^wiki-pecvd]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  CVD nitride and step coverage.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — spacer
  formation in deep-submicron CMOS.[^txt-05]
* Taur and Ning, *Fundamentals of Modern VLSI Devices* — series
  resistance and the extension/spacer trade-off.[^taur-2009]

### Deep dive

* Ogura et al. (IBM), *IEEE TED* 1980 — the lightly doped drain
  transistor that spacers exist to build.[^ogura-1980]
* Tsang et al. (IBM), *IEEE TED* 1982 — the oxide sidewall-spacer
  process: conformal deposition plus anisotropic etch-back.[^tsang-1982]
* Ng and Lynch (AT&T), *IEEE TED* 1986 and 1987 — series resistance of
  the un-silicided extension under the spacer, and why it limits
  scaling.[^ng-1986][^ng-1987]
* Goss and Thornburg, ASMC 1997 — integrating a nitride spacer into a
  0.35 µm CMOS technology.[^goss-1997]
* Regis et al. (Applied Materials), ASMC 1997 — the selective nitride
  spacer etch the film is designed for.[^regis-1997]
* Mizuno et al. (Toshiba), IEDM 1989 — high-permittivity spacers and
  the gate-fringing field.[^mizuno-1989]
* Shrivastava and Fitzpatrick, *IEEE TED* 1982, and McAndrew et al.,
  ICMTS 1994 — overlap/fringing capacitance models in which the
  spacer's permittivity appears.[^shrivastava-1982][^mcandrew-1994]
* Sambonsugi and Sugii (Fujitsu), IRPS 1998 — hot-carrier mechanism
  of NMOS with nitride spacers.[^sambonsugi-1998]
* Hwang, Lee and Hwang, SSDM 1996 — nitride spacer versus hot-carrier
  reliability.[^hwang-1996]
* Janapaty, Tsai and Prasad, SPIE 1998 — oxide/nitride composite
  versus oxide spacers on 0.25 µm PMOS.[^janapaty-1998]
* Shimaya (NTT), IRPS 1995 — water diffusion through nitride and
  hot-carrier degradation.[^shimaya-1995]
* Om et al., ICMTS 1995 — junction leakage versus spacer
  material.[^om-1995]
* Ito et al. (NEC), IEDM 2000, and Shimizu et al. (Hitachi), IEDM
  2001 — nitride film stress as a channel-strain
  variable.[^ito-2000][^shimizu-2001]
* Gumpher et al., *J. Electrochem. Soc.* 2004, and Smith, Seutter and
  Iyer, *J. Electrochem. Soc.* 2005 — BTBAS low-temperature LPCVD
  nitride.[^gumpher-2004][^smith-2005]
* Roenigk and Jensen, *J. Electrochem. Soc.* 1987 — DCS/NH₃ LPCVD
  reactor model.[^roenigk-1987]
* Habraken and Kuiper, *Mater. Sci. Eng. R* 1994 — nitride film
  properties and hydrogen.[^habraken-1994]
* Temple-Boyer et al., *JVST A* 1998 — residual stress of LPCVD
  nitride.[^temple-boyer-1998]
* Smith et al., *J. Electrochem. Soc.* 1990, and Claassen et al.,
  *J. Electrochem. Soc.* 1985 — PECVD nitride mechanism, composition
  and stress.[^smith-1990][^claassen-1985]
* Hughey and Cook, *MRS Proc.* 2003 — irreversible stress change in
  PECVD nitride on heating.[^hughey-2003]

## Open questions

* The deposition route (DCS/NH₃ LPCVD, BTBAS LPCVD or PECVD), the
  temperature and the thickness of the spacer nitride are not public;
  the BTBAS assignment is an inference from SkyWater's furnace list
  and the thermal budget after {ref}`TIPRTAD <step-075>`.
* Whether the SKY130 spacer is nitride-only, oxide/nitride or
  oxide/nitride/oxide is inferred from the PDK's "SPNIT" and "oxide
  spacer" entries; the PDK does not draw the spacer's structure.
* Whether a thin pre-spacer oxide is deposited between
  {ref}`TIPRTAD <step-075>` and this step (a common liner) is not
  stated publicly; this reference describes none, reading the
  {ref}`IOX45 <step-063>` oxide as playing that part (inference).
* The condition of the oxide over the source/drain silicon at this
  point, on which the {ref}`SPE <step-077>` etch must stop, is not
  public.

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^aviza-avp]: Moov used-equipment marketplace, *Aviza / SVG / Thermco
    AVP 8000* listing, accessed 2026-08-30.
    <https://moov.co/marketplace/furnaces-diffusion/aviza-svg/aviza-asml-svg-watkinsjohnson-avp-8000>
[^wiki-sin]: Wikipedia, *Silicon nitride*.
    <https://en.wikipedia.org/wiki/Silicon_nitride>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^taur-2009]: Y. Taur and T. H. Ning, *Fundamentals of Modern VLSI
    Devices*, 2nd ed., Cambridge University Press, 2009, ISBN
    978-0-521-83294-6. <https://doi.org/10.1017/CBO9781139195065>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^ogura-1980]: S. Ogura, P. J. Tsang, W. W. Walker, D. L. Critchlow and
    J. F. Shepard, "Design and characteristics of the lightly doped
    drain-source (LDD) insulated gate field-effect transistor", *IEEE
    Transactions on Electron Devices* **27**(8), 1359–1367 (1980).
    <https://doi.org/10.1109/T-ED.1980.20040>
[^tsang-1982]: P. J. Tsang, S. Ogura, W. W. Walker, J. F. Shepard and
    D. L. Critchlow, "Fabrication of high-performance LDDFET's with
    oxide sidewall-spacer technology", *IEEE Transactions on Electron
    Devices* **29**(4), 590–596 (1982).
    <https://doi.org/10.1109/T-ED.1982.20748>
[^ng-1986]: K. K. Ng and W. T. Lynch, "Analysis of the
    gate-voltage-dependent series resistance of MOSFET's", *IEEE
    Transactions on Electron Devices* **33**(7), 965–972 (1986).
    <https://doi.org/10.1109/T-ED.1986.22602>
[^ng-1987]: K. K. Ng and W. T. Lynch, "The impact of intrinsic series
    resistance on MOSFET scaling", *IEEE Transactions on Electron
    Devices* **34**(3), 503–511 (1987).
    <https://doi.org/10.1109/T-ED.1987.22956>
[^goss-1997]: M. Goss and R. Thornburg, "The challenges of nitride
    spacer processing for a 0.35 μm CMOS technology", *1997 IEEE/SEMI
    Advanced Semiconductor Manufacturing Conference and Workshop
    (ASMC 97) Proceedings*, pp. 228–233.
    <https://doi.org/10.1109/ASMC.1997.630740>
[^regis-1997]: J. M. Regis, A. M. Joshi, T. Lill and M. Yu, "Reactive
    ion etch of silicon nitride spacer with high selectivity to oxide",
    *1997 IEEE/SEMI Advanced Semiconductor Manufacturing Conference and
    Workshop (ASMC 97) Proceedings*, pp. 252–256.
    <https://doi.org/10.1109/ASMC.1997.630744>
[^mizuno-1989]: T. Mizuno, T. Kobori, Y. Saitoh, S. Sawada and
    T. Tanaka, "High dielectric LDD spacer technology for high
    performance MOSFET using gate-fringing field effects", *IEDM 1989
    Technical Digest*, pp. 613–616.
    <https://doi.org/10.1109/IEDM.1989.74355>
[^shrivastava-1982]: R. Shrivastava and K. Fitzpatrick, "A simple model
    for the overlap capacitance of a VLSI MOS device", *IEEE
    Transactions on Electron Devices* **29**(12), 1870–1875 (1982).
    <https://doi.org/10.1109/T-ED.1982.21044>
[^mcandrew-1994]: C. C. McAndrew, G. Zaneski, P. Layman and S. Ayyar,
    "Accurate characterization of MOSFET overlap/fringing capacitance
    for circuit design", *Proc. 1994 IEEE International Conference on
    Microelectronic Test Structures*, pp. 15–20.
    <https://doi.org/10.1109/ICMTS.1994.303510>
[^sambonsugi-1998]: Y. Sambonsugi and T. Sugii, "Hot-carrier
    degradation mechanism and promising device design of nMOSFETs with
    nitride sidewall spacer", *1998 IEEE International Reliability
    Physics Symposium Proceedings*, pp. 184–188.
    <https://doi.org/10.1109/RELPHY.1998.670531>
[^hwang-1996]: H. Hwang, D.-H. Lee and J. M. Hwang, "Effect of Nitride
    Sidewall Spacer on Hot Carrier Reliability Characteristics of
    MOSFET's", *Extended Abstracts of the 1996 International Conference
    on Solid State Devices and Materials*, PC-4-6 (1996).
    <https://doi.org/10.7567/SSDM.1996.PC-4-6>
[^janapaty-1998]: V. Janapaty, J.-Y. Tsai and S. Prasad, "Enhanced
    hot-carrier-induced degradation of 0.25-μm P-MOSFETs with
    oxide/nitride composite spacer compared to those with oxide
    spacer", *Proc. SPIE* **3510**, Microelectronic Manufacturing, 225
    (1998). <https://doi.org/10.1117/12.324387>
[^shimaya-1995]: M. Shimaya, "Water diffusion model for the enhancement
    of hot-carrier-induced degradation due to silicon nitride
    passivation in submicron MOSFET's", *33rd IEEE International
    Reliability Physics Symposium Proceedings* (1995), pp. 292–296.
    <https://doi.org/10.1109/RELPHY.1995.513694>
[^om-1995]: J.-C. Om, M.-S. Jo, H.-S. Park, I.-S. Chung and W.-S. Min,
    "Source/drain junction leakage current of LDD NMOSFET with various
    spacer materials", *Proc. 1995 International Conference on
    Microelectronic Test Structures*, pp. 177–180.
    <https://doi.org/10.1109/ICMTS.1995.513968>
[^ito-2000]: S. Ito, H. Namba, K. Yamaguchi, T. Hirata, K. Ando,
    S. Koyama, S. Kuroki, N. Ikezawa, T. Suzuki, T. Saitoh and
    T. Horiuchi, "Mechanical stress effect of etch-stop nitride and its
    impact on deep submicron transistor design", *IEDM 2000 Technical
    Digest*, pp. 247–250. <https://doi.org/10.1109/IEDM.2000.904303>
[^shimizu-2001]: A. Shimizu, K. Hachimine, N. Ohki, H. Ohta,
    M. Koguchi, Y. Nonaka, H. Sato and F. Ootsuka, "Local
    mechanical-stress control (LMC): a new technique for
    CMOS-performance enhancement", *IEDM 2001 Technical Digest*,
    pp. 19.4.1–19.4.4. <https://doi.org/10.1109/IEDM.2001.979529>
[^gumpher-2004]: J. Gumpher, W. Bather, N. Mehta and D. Wedel,
    "Characterization of Low-Temperature Silicon Nitride LPCVD from
    Bis(tertiary-butylamino)silane and Ammonia", *Journal of The
    Electrochemical Society* **151**(5), G353 (2004).
    <https://doi.org/10.1149/1.1690294>
[^smith-2005]: J. W. Smith, S. M. Seutter and R. S. Iyer, "Thermal
    Chemical Vapor Deposition of Bis(Tertiary-Butylamino)Silane-based
    Silicon Nitride Thin Films", *Journal of The Electrochemical
    Society* **152**(4), G316 (2005). <https://doi.org/10.1149/1.1870792>
[^roenigk-1987]: K. F. Roenigk and K. F. Jensen, "Low Pressure CVD of
    Silicon Nitride", *Journal of The Electrochemical Society*
    **134**(7), 1777–1785 (1987). <https://doi.org/10.1149/1.2100756>
[^habraken-1994]: F. H. P. M. Habraken and A. E. T. Kuiper, "Silicon
    nitride and oxynitride films", *Materials Science and Engineering:
    R: Reports* **12**(3), 123–175 (1994).
    <https://doi.org/10.1016/0927-796X(94)90006-X>
[^temple-boyer-1998]: P. Temple-Boyer, C. Rossi, E. Saint-Etienne and
    E. Scheid, "Residual stress in low pressure chemical vapor
    deposition SiNₓ films deposited from silane and ammonia", *Journal
    of Vacuum Science & Technology A* **16**(4), 2003–2007 (1998).
    <https://doi.org/10.1116/1.581302>
[^smith-1990]: D. L. Smith, A. S. Alimonda, C.-C. Chen, S. E. Ready and
    B. Wacker, "Mechanism of SiNₓHᵧ Deposition from NH₃-SiH₄ Plasma",
    *Journal of The Electrochemical Society* **137**(2), 614–623 (1990).
    <https://doi.org/10.1149/1.2086517>
[^claassen-1985]: W. A. P. Claassen, W. G. J. N. Valkenburg,
    M. F. C. Willemsen and W. M. v. d. Wijgert, "Influence of Deposition
    Temperature, Gas Pressure, Gas Phase Composition, and RF Frequency
    on Composition and Mechanical Stress of Plasma Silicon Nitride
    Layers", *Journal of The Electrochemical Society* **132**(4),
    893–898 (1985). <https://doi.org/10.1149/1.2113980>
[^hughey-2003]: M. P. Hughey and R. F. Cook, "Irreversible Tensile
    Stress Development in PECVD Silicon Nitride Films", *MRS
    Proceedings* **795** (2003). <https://doi.org/10.1557/PROC-795-U1.6>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
