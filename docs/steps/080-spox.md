(step-080)=
# Step 080 — SPOX: Spacer oxide deposition

| | |
|---|---|
| **Step number** | 80 of 171 |
| **Step code** | `SPOX` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | FEOL — extensions, spacers, source/drain |
| **Previous step** | {ref}`NPCME <step-079>` |
| **Next step** | {ref}`PSDM <step-081>` |

## What this step is

`SPOX` deposits a blanket silicon dioxide film over the wafer after the
nitride cut and immediately before the first source/drain mask. The
step list used in this reference calls it the *spacer oxide*; the
PDK's assumptions table lists an "oxide spacer" of 0.05 µm (variable
`SpThickn`),[^pdk-03] and we infer that the two refer to the same
film, so that the SKY130 spacer is a composite of the nitride from
{ref}`SPNIT <step-076>`/{ref}`SPE <step-077>` and this oxide. What the
PDK does not say is whether the oxide is etched back into a second
spacer or left as a blanket layer; the step list contains no oxide
spacer etch between `SPOX` and {ref}`PSDM <step-081>`, so on our
reading the film stays conformal and blanket through the source/drain
implants, and the deep implants pass through it.

The surfaces the oxide lands on are, at this point: the thin oxide
over the source/drain silicon that the spacer etch stopped on
(inferred, {ref}`SPE <step-077>`); the nitride spacers; the
nitride/oxide cap on the gates; the bare poly opened at
{ref}`NPCME <step-079>`; and the field oxide. A conformal 0.05 µm
oxide adds the same thickness to each, and at the foot of a spacer it
adds more than that in the direction an implant travels.

## Step category

`SPOX` is a {ref}`Thin-film deposition <category-deposition>` step: a
CVD oxide of the same family as the cap oxide {ref}`POC <step-059>`
and the later {ref}`NCAPOX <step-091>`. What is specific to it is
that it is an *implant screen and spacer extension* rather than an
insulator: its thickness enters the range and lateral placement of
the P⁺ and N⁺ source/drain implants, so uniformity and conformality
matter as they would for a gate-adjacent film, and its thermal budget
must be low because the tips are already annealed.

## Why this step exists

A thin oxide deposited after the spacer, before the deep source/drain
implants, serves several purposes at once, and the public evidence
does not say which SKY130 had in mind:

* **Spacer width without a second etch.** A conformal oxide over a
  nitride spacer increases the effective offset seen by a
  zero-degree implant — the PDK's high-current implant angle is
  0°[^pdk-03] — because ions arriving next to the spacer foot must
  traverse the sloping oxide before reaching silicon. It is a cheap
  way to widen the spacer for the deep implants alone, leaving the
  narrower nitride spacer to define where the contact etch stops;
  composite oxide/nitride spacers of this kind were standard by the
  0.25 µm generation, as Janapaty et al.'s comparison of oxide and
  oxide/nitride spacers on 0.25 µm PMOS shows.[^janapaty-1998]
* **Implant screen.** Implanting through a thin oxide keeps the
  beam's sputtered contamination out of the silicon, scatters the
  beam to reduce {term}`channelling`, and — for boron — produces a
  profile that Park et al. found to be paradoxically *broadened* by
  the screen,[^park-1991] a behaviour Lim et al. later modelled for
  (100) silicon.[^lim-1993] For BF₂, Wang et al. showed that fluorine
  from implantation through oxide changes boron's enhanced diffusion
  during a high-temperature RTA.[^wang-1997] The screen's thickness is
  therefore a design input to the junction depth.
* **Protecting the opened poly.** The bare poly in the nitride cut
  windows is covered before the implant resists are coated and
  stripped, so the resist chemistry and the ash never touch doped
  poly, and the poly heads receive their source/drain doping through
  a defined oxide.
* **A cap for the anneal.** During {ref}`RTAD <step-088>` a surface
  oxide limits dopant loss: Farhane et al. measured arsenic dose loss
  during nitrogen anneals of shallow implants,[^farhane-2003] and
  Shibahara et al. traced the origins of dopant loss for low-energy
  arsenic and antimony,[^shibahara-1998] while Pelletier et al.
  showed that boron out-diffuses differently into oxide and nitride
  spacers.[^pelletier-2008]
* **Lower fringing capacitance.** Oxide (k ≈ 3.9) between the gate
  and the contacts, instead of nitride (k = 7.5 for "SPNIT"[^pdk-04]),
  reduces the outer fringing capacitance that Shrivastava and
  Fitzpatrick modelled.[^shrivastava-1982]

The original sidewall spacer was itself an oxide,[^tsang-1982] and an
oxide-over-nitride composite recovers some of its properties. Without
`SPOX`, the source/drain implants would enter through whatever oxide
survived the spacer and cut etches, the poly heads would be bare
under resist, and the spacer offset for the deep implant would be the
nitride alone.

## How it is typically performed

Industry-generic routes for a thin conformal oxide in a 200 mm,
130 nm-era fab (SKY130's is not public):

* **LPCVD TEOS oxide.** Tetraethyl orthosilicate pyrolysis in a
  furnace at roughly 650–750 °C (typical industry values, category
  page[^wiki-teos][^txt-02]); Becker et al. characterise the film and
  its conformality,[^becker-1987] and Adams and Capio the reduced-
  pressure silane–oxygen alternative at roughly 400–450 °C.[^adams-1979]
  LPCVD TEOS is the most conformal of the three and the usual choice
  for a spacer or liner, but it spends minutes at a temperature where
  the arsenic tips and boron halos diffuse — a real cost after
  {ref}`TIPRTAD <step-075>`.
* **PECVD TEOS oxide.** TEOS with O₂ in a single-wafer chamber at
  about 350–400 °C; Raupp, Cale and Hey describe the plasma
  chemistry.[^raupp-1992] Conformality is lower than LPCVD but
  adequate for 50 nm on gentle topography; the film is less dense and
  etches faster in HF, which matters when it is later stripped or
  opened.
* **PECVD silane oxide.** SiH₄ + N₂O at similar temperatures on the
  same tool class; SkyWater's "C1" list names it.[^skw-01]
* **Thickness.** 0.05 µm is the PDK's "oxide spacer" value,[^pdk-03]
  and we take it as the nominal target on the reading above; the
  actual deposited thickness and its identification with this step
  are not public.
* **Sequence.** Post-cut clean (already done at
  {ref}`NPCME <step-079>`); load; deposition to a timed thickness on
  monitors; unload. No etch-back is shown in the step list.
* **Metrology.** Thickness and index by ellipsometry on monitors and
  test pads; step coverage by cross-section SEM in development;
  particles.

## Machines typically used

* **PECVD system** (Applied Materials Producer/Centura DxZ, Novellus
  Concept Two/Sequel) with TEOS or silane oxide.
* **Vertical LPCVD furnace** (Aviza/SVG, TEL, ASM, Kokusai) with
  TEOS or SiH₄/O₂ for the batch alternative.
* **Spectroscopic ellipsometer**.

## Machines likely used at SkyWater

* **"C2" / Producer PECVD TEOS** — SkyWater lists "PECVD TEOS, C2 and
  Producer"[^skw-01]; the {ref}`public-sources inventory
  <references-public-sources>` reads "C2" as a Novellus Concept Two
  class tool (inference). Strength: strong for the capability; weak
  for assignment to this step.
* **"C1" PECVD silane oxide** — "PECVD silane oxide/nitride/
  oxynitride, C1".[^skw-01] Strength: strong for existence.
* **Aviza furnaces, LPCVD silane oxide** — "LPCVD silane oxide" is among the
  furnace processes.[^skw-01] Strength: strong for existence.
* Which of the three deposits the spacer oxide is not public; the
  thermal-budget argument favours a PECVD film (inference).

## Resources required

* **TEOS** (liquid, vaporised) with **O₂**, or **silane and
  N₂O**;[^wiki-teos][^wiki-pecvd] helium or nitrogen carrier.
* **NF₃ or CF₄/O₂** chamber clean (PECVD); quartz ware and
  **nitrogen** purge (LPCVD).
* **Monitor wafers**.

## Related steps and cross-references

* Previous: {ref}`NPCME <step-079>` (the bare poly this oxide
  covers). Next: {ref}`PSDM <step-081>` (the first implant mask coated
  on it).
* The nitride component of the spacer: {ref}`SPNIT <step-076>`,
  {ref}`SPE <step-077>`; the oxide under the nitride:
  {ref}`IOX45 <step-063>`.
* The implants that pass through this oxide: {ref}`PSDI <step-082>`,
  {ref}`2PSDI <step-083>`, {ref}`NSDI <step-086>`; the anneal it caps:
  {ref}`RTAD <step-088>`.
* Other CVD oxides: {ref}`POC <step-059>`, {ref}`PSG <step-089>`,
  {ref}`NCAPOX <step-091>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Criteria & Assumptions* — "oxide spacer" 0.05 µm;
  implant angle "High current" 0°.[^pdk-03]
* SkyWater PDK, process stack diagram — "SPNIT K=7.5", oxides at
  3.9.[^pdk-04]
* SkyWater, *Facilities & Capabilities* — "PECVD TEOS, C2 and
  Producer"; "PECVD silane oxide … C1"; Aviza LPCVD oxide.[^skw-01]

### High-level understanding

* Wikipedia, *Tetraethyl orthosilicate* — TEOS as an oxide
  precursor.[^wiki-teos]
* Wikipedia, *Plasma-enhanced chemical vapor deposition*.[^wiki-pecvd]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  CVD oxides and implantation through oxide.[^txt-02]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — composite
  spacers in deep-submicron CMOS.[^txt-05]

### Deep dive

* Tsang et al. (IBM), *IEEE TED* 1982 — the oxide sidewall spacer.[^tsang-1982]
* Janapaty, Tsai and Prasad, SPIE 1998 — oxide versus oxide/nitride
  composite spacers on 0.25 µm PMOS.[^janapaty-1998]
* Park et al., IEDM 1991 — boron profile broadening from a screen
  oxide.[^park-1991]
* Lim et al., IEDM 1993 — a model of boron implantation through
  screen oxide into (100) silicon.[^lim-1993]
* Wang et al. (Motorola), *J. Electrochem. Soc.* 1997 — fluorine and
  boron diffusion after BF₂ implantation through oxide.[^wang-1997]
* Farhane et al., RTP 2003 — arsenic dose loss during nitrogen
  anneals.[^farhane-2003]
* Shibahara et al., *MRS Proc.* 1998 — origins of dopant loss for
  low-energy arsenic and antimony.[^shibahara-1998]
* Pelletier et al., *Mater. Sci. Eng. B* 2008 — boron out-diffusion
  into oxide and nitride spacers.[^pelletier-2008]
* Shrivastava and Fitzpatrick, *IEEE TED* 1982 — overlap and fringing
  capacitance through the spacer dielectric.[^shrivastava-1982]
* Becker et al. (Siemens), *JVST B* 1987 — LPCVD TEOS oxide
  properties and conformality.[^becker-1987]
* Adams and Capio (Bell Labs), *J. Electrochem. Soc.* 1979 —
  reduced-pressure silane oxide deposition.[^adams-1979]
* Raupp, Cale and Hey, *JVST B* 1992 — PECVD TEOS plasma
  chemistry.[^raupp-1992]

## Open questions

* Whether `SPOX` is the PDK's 0.05 µm "oxide spacer", whether it is
  etched back or left blanket, and its deposition method and
  temperature, are all inferred; the PDK entry does not name a step.
* Whether the film is removed before the {ref}`PSG <step-089>`
  deposition or survives under it as part of the pre-LI dielectric is
  not public.
* The thickness of oxide over the source/drain silicon at implant
  time — this film plus whatever remained from
  {ref}`IOX45 <step-063>` — is not public, and it sets the effective
  implant energy.

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^tsang-1982]: P. J. Tsang, S. Ogura, W. W. Walker, J. F. Shepard and
    D. L. Critchlow, "Fabrication of high-performance LDDFET's with
    oxide sidewall-spacer technology", *IEEE Transactions on Electron
    Devices* **29**(4), 590–596 (1982).
    <https://doi.org/10.1109/T-ED.1982.20748>
[^janapaty-1998]: V. Janapaty, J.-Y. Tsai and S. Prasad, "Enhanced
    hot-carrier-induced degradation of 0.25-μm P-MOSFETs with
    oxide/nitride composite spacer compared to those with oxide
    spacer", *Proc. SPIE* **3510**, Microelectronic Manufacturing, 225
    (1998). <https://doi.org/10.1117/12.324387>
[^park-1991]: C. Park, K. M. Klein, A. F. Tasch, R. B. Simonton and
    G. E. Lux, "Paradoxical boron profile broadening caused by
    implantation through a screen oxide layer", *IEDM 1991 Technical
    Digest*, pp. 67–70. <https://doi.org/10.1109/IEDM.1991.235422>
[^lim-1993]: D. Lim, S.-H. Yang, S. Morris and A. F. Tasch, "An
    accurate and computationally-efficient model of boron implantation
    through screen oxide layers into (100) single-crystal silicon",
    *IEDM 1993 Technical Digest*, pp. 291–294.
    <https://doi.org/10.1109/IEDM.1993.347350>
[^wang-1997]: L. Z. Wang, M. S.-C. Luo, H.-H. Tseng and S. A. Ajuria,
    "The Influence of Fluorine on Boron-Enhanced Diffusion in Silicon by
    BF₂⁺ Implantation Through Oxide during High Temperature Rapid
    Thermal Anneal", *Journal of The Electrochemical Society*
    **144**(11), L298–L301 (1997). <https://doi.org/10.1149/1.1838075>
[^farhane-2003]: R. Farhane, F. Salvetti, F. Wacquant, C. Laviron,
    B. Froment, A. Muller, A. Pouydebasque and A. Halimaoui,
    "Investigation of the dose loss during annealing in nitrogen of
    shallow-implanted arsenic", *Proc. 11th IEEE International
    Conference on Advanced Thermal Processing of Semiconductors (RTP
    2003)*, pp. 173–176. <https://doi.org/10.1109/RTP.2003.1249144>
[^shibahara-1998]: K. Shibahara, H. Furumoto, K. Egusa, M. Koh and
    S. Yokoyama, "Dopant Loss Origins of Low Energy Implanted Arsenic
    and Antimony for Ultra Shallow Junction Formation", *MRS
    Proceedings* **532** (1998). <https://doi.org/10.1557/PROC-532-23>
[^pelletier-2008]: B. Pelletier, M. Juhel, C. Trouiller, D. Beucher,
    J. Autran and P. Morin, "Boron out-diffusion mechanism in oxide and
    nitride CMOS sidewall spacer: Impact of the materials properties",
    *Materials Science and Engineering: B* **154–155**, 252–255 (2008).
    <https://doi.org/10.1016/j.mseb.2008.09.025>
[^shrivastava-1982]: R. Shrivastava and K. Fitzpatrick, "A simple model
    for the overlap capacitance of a VLSI MOS device", *IEEE
    Transactions on Electron Devices* **29**(12), 1870–1875 (1982).
    <https://doi.org/10.1109/T-ED.1982.21044>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
    "Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
    **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^adams-1979]: A. C. Adams and C. D. Capio, "The Deposition of Silicon
    Dioxide Films at Reduced Pressure", *Journal of The Electrochemical
    Society* **126**(6), 1042–1046 (1979).
    <https://doi.org/10.1149/1.2129171>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
