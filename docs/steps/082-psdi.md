(step-082)=
# Step 082 — PSDI: P+ source drain implant

| | |
|---|---|
| **Step number** | 82 of 171 |
| **Step code** | `PSDI` |
| **Category** | {ref}`Ion implantation <category-implant>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`PSDM <step-081>` |
| **Next step** | {ref}`2PSDI <step-083>` |

## What this step is

`PSDI` is the heavy p-type implant that forms the deep source and
drain of every PMOS transistor, together with all the other P⁺
diffusions of the process. It goes through the resist windows of
{ref}`PSDM <step-081>`, through the thin {ref}`SPOX <step-080>` oxide
(on our reading), and into silicon wherever the windows are not
blocked by a gate stack or a spacer: the implant is *self-aligned* to
the spacer edge, so the heavy junction lands a spacer-width away from
the gate edge while the shallow extension implanted earlier reaches
under it. A second p-type implant, {ref}`2PSDI <step-083>`, follows in
the same resist; the resist is stripped at {ref}`PDIS <step-084>`, and
the dopant is activated at {ref}`RTAD <step-088>`.

What the PDK says about the result is specific, if sparse. The
junction-depth table gives "N+ or P+ S/D (XJ)" a vertical feature of
0.1 µm and a vertical space of 0.06 µm (variables `JCTD` and `LD`),
limits the S/D out-diffusion next to an isolation edge to 0.007 µm
(0.05 µm for the 6 V devices), and gives the "N Tip (As)" 0.01 µm in
the same column.[^pdk-03] The implant-angle table gives "High
current" implants an angle of 0°, against 7° for the tip implant and
40° with a 23° twist for the high-voltage tip.[^pdk-03] The
extraction tables give P-diffusion a sheet resistance of
197 000 mΩ/sq, that is 197 Ω/sq, against 120 Ω/sq for
N-diffusion.[^pdk-08] The species, energy and dose are not public;
the "P+" name and the high-current angle entry are what the public
data provide, and we infer the rest from industry practice.

The PMOS cross-section in the PDK shows "P+" source/drain beside
"P−" extensions under the gate edge.[^pdk-07] Where that P⁻
extension comes from is one of the open questions of this module,
discussed below.

## Step category

`PSDI` is an {ref}`Ion implantation <category-implant>` step of the
*source/drain* class: a high-dose (of the order of 10¹⁵ cm⁻²,
industry-typical[^txt-01]), low-to-medium-energy implant from a
high-current tool, self-aligned to a spacer, that amorphises the
silicon surface and sets the contact resistance
({ref}`category-implant`). Its partner is {ref}`NSDI <step-086>`. It
differs from the tip implants ({ref}`ASTI <step-065>`) in dose by an
order of magnitude and in the mask it is aligned to — the spacer
rather than the bare gate — and from the well and channel implants
in every respect but the tool.

## Why this step exists

The deep source/drain does three things the extension cannot. It
provides a low-resistance path from the contact to the channel — Ng
and Lynch showed how the series resistance of the un-silicided
extension limits scaling,[^ng-1986] and the deep junction is where
most of the current flows; it provides the heavily doped surface
that a contact needs for a low specific contact resistance; and it
is deep enough (the PDK's 0.1 µm[^pdk-03]) that the contact etch and
any silicide ({ref}`CSIL <step-098>`) do not punch through it. Placing
it a spacer-width from the gate is what keeps its depth from
degrading short-channel control — the whole purpose of the LDD
scheme of Ogura et al.[^ogura-1980] and the spacer of Tsang et
al.[^tsang-1982]

Beyond the PMOS, the same implant makes the p⁺ taps that tie the
P-wells and substrate to ground, the emitter and collector of the
vertical PNP and the base contacts of the NPN,[^pdk-07] the P⁺
diffusion resistor,[^pdk-07] the p-side of the p-diffusion-to-N-well
diodes,[^pdk-07] and — on the reading of the {ref}`NPCM <step-078>`
page — the contact heads of the precision poly resistors, which
rpm.4 requires to lie inside `psdm`.[^pdk-periph] The 0.34 µm
"min. width to open a strip of tap between two diffs" and the
0.12 µm "min. diff/tap width for reproducible resistivity" in the
PDK's width criteria[^pdk-03] are constraints on where this implant
can be made to land reproducibly.

Two things the implant does *not* do, on the reading used throughout
this reference, are worth stating. It does not dope the PMOS gate:
the gate is capped by about 0.2 µm of nitride/oxide ("poly cap after
SPE"[^pdk-03]), the {term}`nitride cut` is kept off gates by npc.4,[^pdk-periph]
and the gate poly was doped n-type at {ref}`P1I <step-050>` — so
SKY130 avoids the boron-penetration problem of p⁺ gates that
Pfiester et al. described[^pfiester-1990] at the cost of a
single-work-function (buried-channel PMOS) design; the work-function
dependence on poly doping that Lifshitz measured[^lifshitz-1985] is
therefore fixed at the n⁺ value for both transistors. And it is not
what forms the arsenic extensions of the NMOS, which are made before
the spacer ({ref}`ASTI <step-065>`).

Without `PSDI` there would be no PMOS source/drain, no substrate
contacts, no PNP and no p-type resistors or diodes.

## How it is typically performed

An industry-generic P⁺ source/drain implant for a 200 mm, 130 nm-era
fab (SKY130's recipe is not public):

* **Species.** Boron, as B⁺ or as the molecular ion BF₂⁺, both
  produced from boron trifluoride in the ion source.[^wiki-bf3] BF₂⁺
  carries the boron at 11/49 of the beam energy, so a given
  implanter reaches a shallower profile, and its heavier mass
  amorphises the surface, which suppresses {term}`channelling` and
  lets solid-phase regrowth give high activation; the fluorine it
  brings alters boron's transient enhanced diffusion during the RTA,
  as Wang et al. showed for BF₂ implanted through
  oxide.[^wang-1997] Bourdelle et al. compared B and BF₂ for PMOS
  junctions with thin gate oxides,[^bourdelle-2000] and the
  alternative of a germanium pre-amorphisation followed by B⁺ was
  optimised by Öztürk et al.[^ozturk-1988] and applied to PMOS
  extensions by Adachi et al.[^adachi-2001] SkyWater's implanters
  list "B11" and "BF2" as species.[^skw-01] Which SKY130 uses here
  is not public.
* **Energy and dose.** Tens of keV and a few 10¹⁵ cm⁻² are the
  industry-typical values for a deep source/drain at this
  node;[^txt-01][^txt-02] the PDK's 0.1 µm junction depth[^pdk-03]
  after {ref}`RTAD <step-088>` is consistent with them. The screen
  oxide ({ref}`SPOX <step-080>`, 0.05 µm if it is the PDK's "oxide
  spacer"[^pdk-03]) takes part of the range and, for boron, broadens
  the profile in the way Park et al. found paradoxical[^park-1991]
  and Lim et al. modelled.[^lim-1993]
* **Tilt.** 0°, per the PDK's "High current" implant-angle entry.[^pdk-03]
  A zero-tilt implant beside a roughly 0.4 µm-tall (0.18 µm poly plus the ~0.2 µm cap[^pdk-03]) capped gate with spacers
  avoids the shadowing of tilted source/drain implants that Krieger
  et al. analysed,[^krieger-1989] and it needs the screen oxide and
  the self-amorphisation of BF₂ (or a pre-amorphisation) to control
  channelling; on a batch spinning-disc implanter the effective
  angle varies across the disc, as Jones and Sinclair
  showed.[^jones-1996]
* **Wafer handling.** Batch spinning-disc end station with wafer
  cooling — the beam power at high current heats the resist, and
  Smith's early chapter[^smith-1983] and Romig et al.'s study of
  resist burning[^romig-1996] set out the limits. A {term}`plasma flood gun`
  neutralises the positive charge that a beam on a resist-covered
  wafer builds up: Dixon, Lukaszek and Heden showed how resist
  enhances charging,[^dixon-1996] Mehta et al. investigated negative
  charging with the flood gun,[^mehta-1996] and Current, Vella and
  Lukaszek set out beam-plasma charging control.[^current-1996-iit]
  The gate oxides at risk are protected here by the capped gate and
  the resist, but the spacer-edge oxide over the extensions is
  exposed.
* **Monitoring.** Sheet resistance by {term}`four-point probe` on
  bare monitor wafers after a monitor anneal; the dose is too high
  for thermal-wave metrology to be sensitive. Particles and resist
  condition after the implant.
* **Anneal.** None here; the dopant sits in an amorphised layer
  until {ref}`RTAD <step-088>`, with {ref}`2PSDI <step-083>` and the
  N⁺ implant in between.

## Machines typically used

* **High-current ion implanter**, 200 mm: Axcelis/Eaton GSD and
  NV-GSD series (batch), Applied Materials xR and Quantum, Varian
  VIISta 80 (single-wafer, described by Mezack et al.[^mezack-2000]);
  Current gives the production-implanter overview[^current-1996] and
  the longer view of implantation for advanced devices.[^current-2017]
* **Four-point probe**; **particle inspection**.

## Machines likely used at SkyWater

* **Axcelis GSD high-dose implanter.** SkyWater lists "Axcelis GSD Hi
  dose B11, BF2, P, As 2-180kev, 5e12 to 5e16" and, separately,
  "Axcelis GSD High current/energy B11, BF2, P, As, 10-3000kev, 1e11
  to 5e15".[^skw-01] Strength: **strong** for the tools, their
  species and their dose ranges; the assignment of `PSDI` to the
  "Hi dose" tool is an **inference** from the dose it must deliver
  (of the order of 10¹⁵ cm⁻², beyond the "Axcelis 8250 Mid current …
  1e11 to 1e14" range[^skw-01]). Axcelis describes the GSD family as
  "the industry benchmark for the longest manufactured and supported
  batch ion implanter".[^axcelis-gsd]

## Resources required

* **Boron trifluoride (BF₃)** as the source gas for B⁺ and
  BF₂⁺;[^wiki-bf3] delivered in sub-atmospheric cylinders with gas
  cabinet monitoring.
* **Source-support gases** (argon, xenon); **liquid nitrogen** for
  cryopumps; high-purity **nitrogen** for venting.
* **Source consumables** — filaments/cathodes, arc-chamber liners,
  extraction electrodes; **disc pads** and platen cooling water;
  flood-gun consumables.
* **Monitor wafers** (SEMI M8 class)[^semi-m8] for sheet resistance.

## Related steps and cross-references

* Previous: {ref}`PSDM <step-081>` (the mask). Next:
  {ref}`2PSDI <step-083>` (the second p-type implant in the same
  resist), then {ref}`PDIS <step-084>` (strip).
* Complementary implant: {ref}`NSDI <step-086>`; activation:
  {ref}`RTAD <step-088>` and {ref}`RTAD2 <step-092>`.
* The offset it is aligned to: {ref}`SPNIT <step-076>`,
  {ref}`SPE <step-077>`; the screen it passes through:
  {ref}`SPOX <step-080>`; the poly it dopes through the cut:
  {ref}`NPCME <step-079>`, {ref}`PRI <step-053>`, {ref}`UPRI <step-056>`.
* The PMOS channel it completes: {ref}`LVTPI <step-020>`,
  {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`; the gate it does
  not dope: {ref}`P1I <step-050>`.
* Category page: {ref}`Ion implantation <category-implant>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — S/D junction depth 0.1 µm
  and 0.06 µm entries; out-diffusion limits; implant angles ("High
  current" 0°); diff/tap width criteria.[^pdk-03]
* SkyWater PDK, *Device Details* — PMOS cross-section with "P+" and
  "P−" regions; PNP, NPN, diode and diffusion-resistor
  descriptions.[^pdk-07]
* SkyWater PDK, *Parasitic Layout Extraction* — P-diffusion
  197 000 mΩ/sq, N-diffusion 120 000 mΩ/sq.[^pdk-08]
* SkyWater PDK, *Periphery rules* — rpm.4, npc.4, psd.*.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — the Axcelis GSD "Hi dose"
  and "High current/energy" implanters with species and dose
  ranges; the 8250 medium-current tool.[^skw-01]
* Axcelis, GSD Ovation press release — the GSD family.[^axcelis-gsd]

### High-level understanding

* Wikipedia, *Ion implantation* — doses, energies, channelling and
  amorphisation.[^wiki-implant]
* Wikipedia, *Boron trifluoride* — the boron source gas.[^wiki-bf3]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — the
  source/drain module and implant chapter.[^txt-01]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  implantation practice.[^txt-02]

### Deep dive

* Ogura et al. (IBM), *IEEE TED* 1980, and Tsang et al. (IBM), *IEEE
  TED* 1982 — the LDD device and the spacer that self-aligns the
  deep implant.[^ogura-1980][^tsang-1982]
* Ng and Lynch (AT&T), *IEEE TED* 1986 — series resistance, the
  reason the deep junction must be heavy.[^ng-1986]
* Wang et al. (Motorola), *J. Electrochem. Soc.* 1997 — fluorine and
  boron diffusion after BF₂ through oxide.[^wang-1997]
* Bourdelle et al. (Agere), IIT 2000 — B versus BF₂ for PMOS
  junctions with thin gate oxides.[^bourdelle-2000]
* Öztürk et al., *IEEE TED* 1988 — germanium pre-amorphisation for
  shallow p⁺ junctions.[^ozturk-1988]
* Adachi, Ohuchi and Toyoshima (Toshiba), IWJT 2001 — Ge PAI with
  sub-keV boron for PMOS extensions.[^adachi-2001]
* Park et al., IEDM 1991, and Lim et al., IEDM 1993 — boron implanted
  through a screen oxide.[^park-1991][^lim-1993]
* Krieger et al., *IEEE TED* 1989 — shadowing of tilted source/drain
  implants, the reason for 0°.[^krieger-1989]
* Jones and Sinclair, IIT 1996 — channelling variation across a
  spinning-disc batch implanter.[^jones-1996]
* Smith, 1983, and Romig, Bishop and Rio, IIT 1996 — wafer cooling
  and resist burning at high beam power.[^smith-1983][^romig-1996]
* Dixon, Lukaszek and Heden, IIT 1996; Mehta et al., IIT 1996;
  Current, Vella and Lukaszek, IIT 1996 — wafer charging and flood-gun
  control during high-current implants.[^dixon-1996][^mehta-1996][^current-1996-iit]
* Pfiester et al. (Motorola), *IEEE TED* 1990 — boron penetration
  through p⁺ gates, the problem a capped n⁺ gate avoids.[^pfiester-1990]
* Lifshitz (Bell Labs), *IEEE TED* 1985 — poly gate work function
  versus doping.[^lifshitz-1985]
* Mezack et al. (Varian), IIT 2000 — the single-wafer high-current
  implanter alternative.[^mezack-2000]
* Current, *JVST A* 1996 and *Mater. Sci. Semicond. Process.* 2017 —
  production implanters and the evolution of implantation.[^current-1996][^current-2017]
* ITRS 2001, *Front End Processes* — junction requirements at the
  node.[^itrs-01]

## Open questions

* **Species, energy, dose and the split with `2PSDI`** are not
  public; the values above are industry-typical.
* **The PMOS extension.** The PDK's PMOS cross-section shows "P−"
  extensions,[^pdk-07] but the mask list contains only N-tip masks
  (NTM, HVNTM, LDNTM)[^pdk-05] and this reference describes no PMOS
  tip module. The extension may be formed by
  {ref}`2PSDI <step-083>` (a lighter or tilted component under the
  same resist), by lateral straggle and diffusion of this implant
  under the spacer during {ref}`RTAD <step-088>`, or by a step not
  separately named; the PDK's "HVPTM shadowing" entry of 0.089 µm in
  its physical-criteria table[^pdk-03] hints that a high-voltage P-tip
  mask exists in at least one flow variant, but no such mask appears
  in the mask list. Which of these applies
  is an open question on this page.
* Whether the gate poly of the PMOS is entirely shielded from this
  implant is inferred from the cap thickness and npc.4; no public
  source states it.
* Which implanter runs the step is inferred from dose capability.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the per-device cross-section drawings.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://github.com/google/skywater-pdk/tree/main/docs/rules/device-details>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^axcelis-gsd]: Axcelis Technologies, *Axcelis Announces Introduction Of
    The 'GSD Ovation' High Current And High Energy Batch Implanters*, PR
    Newswire, 2021-11-02. <https://www.prnewswire.com/news-releases/axcelis-announces-introduction-of-the-gsd-ovation-high-current-and-high-energy-batch-implanters-301412520.html>
[^wiki-implant]: Wikipedia, *Ion implantation*.
    <https://en.wikipedia.org/wiki/Ion_implantation>
[^wiki-bf3]: Wikipedia, *Boron trifluoride*.
    <https://en.wikipedia.org/wiki/Boron_trifluoride>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
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
[^wang-1997]: L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
    "The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon by
    BF₂⁺ Implantation Through Oxide during High Temperature Rapid
    Thermal Anneal", *Journal of The Electrochemical Society*
    **144**(11), L298–L301 (1997). <https://doi.org/10.1149/1.1838075>
[^bourdelle-2000]: K. K. Bourdelle, H.-J. Gossmann, S. Chaudhry and
    A. Agarwal, "Comparison of B and BF₂ source/drain extension
    implants for PMOS transistors with thin gate oxides", *Proc. 2000
    International Conference on Ion Implantation Technology*,
    pp. 25–27. <https://doi.org/10.1109/IIT.2000.924081>
[^ozturk-1988]: M. C. Öztürk, J. J. Wortman, C. M. Osburn, A. Ajmera,
    G. A. Rozgonyi, E. Frey, W.-K. Chu and C. Lee, "Optimization of
    the germanium preamorphization conditions for shallow-junction
    formation", *IEEE Transactions on Electron Devices* **35**(5),
    659–668 (1988). <https://doi.org/10.1109/16.2510>
[^adachi-2001]: K. Adachi, K. Ohuchi and Y. Toyoshima, "Combination of
    germanium preamorphization and sub-keV boron implantation for
    source/drain extension of pMOSFETs", *Extended Abstracts of the
    Second International Workshop on Junction Technology* (2001),
    pp. 35–38. <https://doi.org/10.1109/IWJT.2001.993821>
[^park-1991]: C. Park, K. M. Klein, A. F. Tasch, R. B. Simonton and
    G. E. Lux, "Paradoxical boron profile broadening caused by
    implantation through a screen oxide layer", *IEDM 1991 Technical
    Digest*, pp. 67–70. <https://doi.org/10.1109/IEDM.1991.235422>
[^lim-1993]: D. Lim, S.-H. Yang, S. Morris and A. F. Tasch, "An
    accurate and computationally-efficient model of boron implantation
    through screen oxide layers into (100) single-crystal silicon",
    *IEDM 1993 Technical Digest*, pp. 291–294.
    <https://doi.org/10.1109/IEDM.1993.347350>
[^krieger-1989]: G. Krieger, G. Spadini, P. Cuevas and J. Schuur,
    "Shadowing effects due to tilted arsenic source/drain implant",
    *IEEE Transactions on Electron Devices* **36**(11), 2458–2461
    (1989). <https://doi.org/10.1109/16.43667>
[^jones-1996]: M. Jones and F. Sinclair, "Across-wafer channeling
    variations on batch implanters: a graphical technique to analyze
    spinning disk systems", *Proc. 11th International Conference on
    Ion Implantation Technology* (1996), pp. 264–267.
    <https://doi.org/10.1109/IIT.1996.586257>
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion
    implanter", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 190–193.
    <https://doi.org/10.1109/IIT.1996.586181>
[^dixon-1996]: W. Dixon, W. Lukaszek and C. Heden,
    "Photoresist-enhanced wafer charging during high current ion
    implantation", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 85–88.
    <https://doi.org/10.1109/IIT.1996.586134>
[^mehta-1996]: S. Mehta, B. Axan, S. Walther and S. Felch,
    "Investigation of negative charging with plasma flood gun (PFG)
    during high current implantation", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 73–76.
    <https://doi.org/10.1109/IIT.1996.586128>
[^current-1996-iit]: M. I. Current, M. Vella and W. Lukaszek,
    "Beam-plasma concepts for wafer charging control during ion
    implantation", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 53–56.
    <https://doi.org/10.1109/IIT.1996.586119>
[^pfiester-1990]: J. R. Pfiester, F. K. Baker, T. C. Mele, H.-H. Tseng,
    P. J. Tobin, J. D. Hayden, J. W. Miller, C. D. Gunderson and
    L. C. Parrillo, "The effects of boron penetration on p⁺
    polysilicon gated PMOS devices", *IEEE Transactions on Electron
    Devices* **37**(8), 1842–1851 (1990). <https://doi.org/10.1109/16.57135>
[^lifshitz-1985]: N. Lifshitz, "Dependence of the work-function
    difference between the polysilicon gate and silicon substrate on
    the doping level in polysilicon", *IEEE Transactions on Electron
    Devices* **32**(3), 617–621 (1985).
    <https://doi.org/10.1109/T-ED.1985.21987>
[^mezack-2000]: G. Mezack, T. Callahan, S. Mehta and U. Jeong,
    "Advantages of the Varian VIISta single wafer high current ion
    implanter for advanced device fabrication", *Proc. 2000
    International Conference on Ion Implantation Technology*,
    pp. 431–434. <https://doi.org/10.1109/IIT.2000.924180>
[^current-1996]: M. I. Current, "Ion implantation for silicon device
    manufacturing: A vacuum perspective", *Journal of Vacuum Science &
    Technology A* **14**(3), 1115–1123 (1996).
    <https://doi.org/10.1116/1.580279>
[^current-2017]: M. I. Current, "Ion implantation of advanced silicon
    devices: Past, present and future", *Materials Science in
    Semiconductor Processing* **62**, 13–22 (2017).
    <https://doi.org/10.1016/j.mssp.2016.10.045>
[^itrs-01]: International Technology Roadmap for Semiconductors, *2001
    Edition: Front End Processes*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001FEP.pdf>
