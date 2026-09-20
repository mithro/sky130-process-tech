(step-081)=
# Step 081 — PSDM: P+ source drain implant mask

| | |
|---|---|
| **Step number** | 81 of 171[^steps-sheet] |
| **Step code** | `PSDM` |
| **Category** | {ref}`Photolithography (mask step) <category-lithography>` |
| **Phase** | {term}`FEOL` — extensions, spacers, source/drain |
| **Previous step** | {ref}`SPOX <step-080>` |
| **Next step** | {ref}`PSDI <step-082>` |

## What this step is

`PSDM` is the P⁺ source/drain implant mask. It coats the wafer — now
carrying spacers, the {term}`nitride cut` and the fresh {ref}`SPOX <step-080>`
oxide — with photoresist, exposes it through the P⁺ implant reticle
and develops it, leaving resist windows over every region that is to
receive the heavy p-type implants of {ref}`PSDI <step-082>` and
{ref}`2PSDI <step-083>` (on our reading). The resist is stripped at
{ref}`PDIS <step-084>`. It is the first of the two source/drain masks;
its complement, {ref}`NSDM <step-085>`, follows with the N⁺ implant.

The PDK documents the layer thoroughly. The mask table lists "P+
Implant, PSDM" as used in SKY130;[^pdk-05] the drawn layer is `psdm`
(GDS 94:20, "P+ source/drain implant") and the generated mask layer is
`cpsdm` (32:0, "P+ Implant mask"), which also carries "mask add"
(31:21) and "mask drop" (31:22) purposes — evidence that the reticle
is derived from the drawn layer by Boolean operations, not copied
from it.[^pdk-06] The rules (shared with `nsdm` under the heading
"Defines opening for N+/P+ implants") give: width 0.380 µm (psd.1),
space 0.380 µm (psd.2), enclosure of diffusion by 0.125 µm (psd.5a),
enclosure of tap by 0.125 µm (psd.5b), zero enclosure at a diff/tap
butting edge (psd.6), 0.130 µm spacing to diffusion or tap of the
opposite implant (psd.7), no overlap with diffusion or tap of the
opposite doping (psd.8), the requirement that "Diff and tap must be
enclosed by their corresponding implant layers" (psd.9), minimum area
0.255 µm² (psd.10b) and minimum hole area 0.265 µm² (psd.11).[^pdk-periph]
The minimum-CD table repeats 0.38 µm for feature and space
(`PSDMCD`, `PSDMCDSP`).[^pdk-03]

## Step category

`PSDM` is a {ref}`Photolithography (mask step) <category-lithography>`
step of the *implant-block* type, like the well and channel masks of
the earlier module ({ref}`LVTNM <step-014>`, {ref}`NWM <step-017>`),
but with two differences. The resist must stop a *high-dose*,
high-current implant of the order of 10¹⁵ cm⁻² (industry-typical for
a source/drain, category page[^txt-01]) rather than a light channel
dose, and it is printed over the tallest topography the front end has
yet seen — capped gates with spacers — so its coverage at the foot
of a gate line, where an implant edge often lies, has to be
reliable.

## Why this step exists

The P⁺ implant must reach some regions and be kept out of others,
and the difference is drawn on this layer. From the PDK's device and
layer descriptions, the regions inside `psdm` are:

* the **source/drain of every PMOS** — 1.8 V, 5 V and the
  drain-extended and isolated variants, whose cross-sections show
  "P+" source/drain regions beside "P-" extensions in an
  N-well;[^pdk-07] the drain-extended PMOS source must be enclosed by
  `psdm` (a `de_pFet_source` rule);[^pdk-periph]
* the **p⁺ taps** (`tap`, 65:44, "Active (diffusion) area (type equal
  to the well/substrate underneath) (i.e., N+ and P+)"[^pdk-06])
  that contact the p-substrate and P-wells, with the 0.125 µm
  enclosure of psd.5b;[^pdk-periph]
* the **emitters and collectors of the vertical PNP** and the
  **bases of the NPN**, whose cross-sections show "P+" regions with
  base and emitter/collector labels;[^pdk-07]
* the **P⁺ diffusion resistor** (`res_generic_pd`, "P+ diffusion"),
  whose body is the P⁺ diffusion itself,[^pdk-07] with a sheet
  resistance of 197 000 mΩ/sq (197 Ω/sq) in the extraction
  tables;[^pdk-08]
* the **p-type diodes** to N-well (`diode_pd2nw_*`);[^pdk-07]
* the **precision poly resistors**, which rpm.4 requires to be
  enclosed by `psdm` by 0.110 µm[^pdk-periph] — on the reading given
  on the {ref}`NPCM <step-078>` page, so that their contact heads,
  opened by the nitride cut, are heavily doped.

The regions kept *out* are the NMOS source/drains and n⁺ taps
(psd.8, "cannot overlap diff/tap regions of opposite doping"), the
poly contacts outside resistors (licon.9, 0.110 µm spacing) and, on
our reading, the gates — which are capped and receive nothing in any
case. Because `psdm` and `nsdm` abut at butting diffusion/tap edges
with zero enclosure (psd.6)[^pdk-periph] and must otherwise keep
0.130 µm apart (psd.7), the two layers are close to complementary
across the active area, which is the classic "two masks, two
implants" CMOS source/drain scheme.

Two proximity effects follow from a high-dose implant edge in resist.
Ions scattered laterally from the resist edge shift the threshold of
transistors placed near it — Hook et al. measured the lateral
straggle and {term}`mask-proximity effect` at IBM,[^hook-2003] Sheu et al.
built a compact model of the well-edge version,[^sheu-2006] and
Drennan, Kniffin and Locascio explained what it means for analogue
layout[^drennan-2006] — which is why the layer carries enclosure and
spacing rules of 0.125–0.130 µm rather than zero.

Without `PSDM` no p-type source/drain, tap, emitter, resistor or
diode could be made without also doping the NMOS.

## How it is typically performed

An industry-generic high-dose implant-block lithography sequence for
a 200 mm, 130 nm-era fab (SKY130's is not public):

1. **Surface preparation.** Dehydration bake and HMDS prime on the
   track; the surface is the fresh CVD oxide of
   {ref}`SPOX <step-080>`, which primes well.[^txt-02]
2. **Resist coat.** A single-layer positive resist of the order of
   1 µm: the PDK's nominal "Photoresist thickness" is 1.14 µm,[^pdk-03]
   and the deep source/drain implants (BF₂ or boron at tens of keV,
   typical industry values[^txt-02]) are stopped by a small fraction
   of that. The thickness is set less by stopping power than by
   coverage over roughly 0.4 µm-tall (0.18 µm poly plus the ~0.2 µm cap[^pdk-03]) capped gates and by the resist's need to
   survive a 10¹⁵ cm⁻² beam: Smith's early treatment of wafer
   cooling and resist masking in implantation,[^smith-1983] and
   Romig et al.'s study of resist burning in a high-current
   implanter,[^romig-1996] describe what goes wrong when it does not.
3. **Exposure.** At 0.380 µm minimum width and space,[^pdk-periph] an
   i-line stepper at NA 0.6 works at k₁ = 0.38 × 0.6 / 0.365 ≈ 0.62,
   well above the "0.4 for production" limit;[^wiki-litho] ASML
   describes older exposure tools that "migrate to the lithography of
   choice for less critical layers".[^asml-30] We infer an
   **i-line** exposure, as for the earlier implant-block masks.
4. **Alignment.** To the active/STI pattern for the 0.125 µm
   diffusion enclosure and to poly for the resistor and licon.9
   rules;[^pdk-periph] Levinson's book has a chapter on
   overlay.[^levinson-2005]
5. **Develop** in 2.38 % (0.26 N) TMAH,[^txt-02] rinse, dry; then a hard bake
   or UV cure to harden the resist against the implant and reduce
   outgassing — Lee et al. measured thick-resist outgassing during
   implantation,[^lee-1996] Horsky the outgassing in high-energy and
   high-current tools,[^horsky-1998] and Carpenter and Fecteau the
   productivity measures for high-pressure outgassing.[^carpenter-2002]
6. **Inspection.** Overlay on box-in-box targets; after-develop
   inspection for scumming at gate feet, where resist residue would
   locally block the implant.

## Machines typically used

* **{ref}`i-line stepper <machine-i-line-stepper>`**, 200 mm: ASML PAS 5500/100–/275, Nikon NSR-2205i,
  Canon FPA-3000i ({ref}`category-lithography`).
* **{ref}`Coat/develop track <machine-coat-develop-track>`** (TEL, DNS/SCREEN, SVG/ASML, Sokudo) with a
  UV-cure or hard-bake module.
* **{ref}`Overlay metrology <machine-cd-sem-overlay-metrology>`** (KLA-Tencor 5xxx/Archer); **CD-SEM** for
  periodic checks.

## Machines likely used at SkyWater

* **ASML i-line stepper / i-line scanner.** SkyWater lists both.[^skw-01]
  Strength: **strong** for existence; assignment of `PSDM` to i-line
  is an **inference** from the 0.38 µm rules.
* **Tracks — DNS 80B, Sokudo RF3, TEL ProZ Lithius**.[^skw-01]
  Strength: strong for existence.
* **Overlay — KLA 5200/5300/Archer; CD — AMAT Verity/VeraSEM**.[^skw-01]
  Strength: strong for existence (SkyWater statement); use at this
  mask is an inference.

## Resources required

* **Positive i-line (DNQ/novolac) photoresist** ({ref}`lithography materials <material-lithography-materials>`), about 1 µm
  (inferred; PDK nominal 1.14 µm[^pdk-03]); SkyWater's 2021 S-1 names Dow,
  JSR and Tokyo Ohka Kogyo as resist suppliers.[^sec-01]
* **HMDS**, **2.38 % (0.26 N) TMAH developer**,[^txt-02] edge-bead remover,
  rinse solvents, {ref}`DI water <material-ultrapure-water>` and {ref}`nitrogen <material-process-gases>`.
* **The PSDM reticle** — generated from `cpsdm` (32:0) with its
  add/drop corrections.[^pdk-06]

## Related steps and cross-references

* Previous: {ref}`SPOX <step-080>` (the oxide the resist is coated
  on). Next: {ref}`PSDI <step-082>` and {ref}`2PSDI <step-083>` (the
  implants through this mask), then {ref}`PDIS <step-084>` (strip).
* Complementary mask: {ref}`NSDM <step-085>`.
* Structures it dopes: PMOS source/drain, p⁺ taps, PNP
  emitter/collector, NPN base, P⁺ diffusion resistors, p-diodes, and
  the precision-resistor heads of {ref}`RPM <step-049>` opened at
  {ref}`NPCM <step-078>`.
* Previous mask: {ref}`NPCM <step-078>`; next mask:
  {ref}`NSDM <step-085>`.
* Mask page: {ref}`PSDM <mask-psdm>` — the mask's layers, plates,
  renders and design rules.
* Category page: {ref}`Photolithography (mask step) <category-lithography>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`High aspect ratio photolithographic method for high energy implantation <patent-gp23358573>` — US 6,576,405 B1 (1999)
<!-- index-links:end -->

## References

### Cross-check

* SkyWater PDK, [*Masks*](<https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>) page and `masks.csv` — "P+ Implant, PSDM,
  X".[^pdk-05]
* SkyWater PDK, [*Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) and `gds_layers.csv` — `psdm`
  94:20; `cpsdm` 32:0, 31:21, 31:22; `tap` 65:44.[^pdk-06]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — psd.1–psd.11; rpm.4; licon.9;
  `de_pFet_source` enclosure by psdm.[^pdk-periph]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — `PSDMCD` 0.38 µm;
  photoresist thickness 1.14 µm.[^pdk-03]
* [SkyWater PDK, *Device Details*](<https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>) — PMOS, PNP, NPN, diode and
  `res_generic_pd` descriptions and cross-sections.[^pdk-07]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — P-diffusion sheet
  resistance 197 000 mΩ/sq.[^pdk-08]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — i-line tools, tracks,
  metrology.[^skw-01]
* [SkyWater, Form S-1 (2021)](<https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>) — photoresist suppliers.[^sec-01]

### High-level understanding

* [Wikipedia, *Photolithography*](<https://en.wikipedia.org/wiki/Photolithography>) — i-line, k₁.[^wiki-litho]
* [Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1](<https://openlibrary.org/isbn/9780961672164>) —
  lithography and implant masking.[^txt-02]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — the CMOS
  source/drain module.[^txt-01]

### Deep dive

* [ITRS 2001, *Lithography*](<https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>) — the exposure options it lists by node for
  critical layers.[^itrs-03]
* [Hook et al. (IBM), *IEEE TED* 2003](<https://doi.org/10.1109/TED.2003.815371>) — lateral straggle and the
  implant mask-proximity effect.[^hook-2003]
* [Sheu et al. (TSMC), *IEEE TED* 2006](<https://doi.org/10.1109/TED.2006.884070>) — well-edge proximity
  model.[^sheu-2006]
* [Drennan, Kniffin and Locascio, CICC 2006](<https://doi.org/10.1109/CICC.2006.320869>) — proximity effects in
  analogue layout.[^drennan-2006]
* [Levinson, *Principles of Lithography*](<https://doi.org/10.1117/3.601520>) — chapters on wafer steppers,
  masks and reticles, and overlay.[^levinson-2005]
* [Mack, *Fundamental Principles of Optical Lithography*](<https://doi.org/10.1002/9780470723876>) — imaging in
  thick resist.[^mack-2007]
* [Smith, *Ion Implantation: Equipment and Techniques* 1983](<https://doi.org/10.1007/978-3-642-69156-0_25>) — wafer
  cooling and resist masking problems.[^smith-1983]
* [Romig, Bishop and Rio, IIT 1996](<https://doi.org/10.1109/IIT.1996.586181>) — resist burning in a high-current
  implanter.[^romig-1996]
* [Lee et al. (Genus), IIT 1996](<https://doi.org/10.1109/IIT.1996.586180>) — thick-resist outgassing.[^lee-1996]
* [Horsky, IIT 1998](<https://doi.org/10.1109/IIT.1999.812201>) — outgassing in high-energy and high-current
  implantation.[^horsky-1998]
* [Carpenter and Fecteau (Axcelis), IIT 2002](<https://doi.org/10.1109/IIT.2002.1258053>) — productivity during
  high-pressure resist outgassing.[^carpenter-2002]
* [Dixon, Lukaszek and Heden, IIT 1996](<https://doi.org/10.1109/IIT.1996.586134>) — resist-enhanced wafer
  charging during high-current implants.[^dixon-1996]
* [Buffat and Adams (Zilog), US 6,576,405](<https://patents.google.com/patent/US6576405B1/en>) — resist requirements when
  the implant behind the mask is MeV-class, for contrast.[^pat-resist-zilog]

## Open questions

* The resist, thickness, exposure tool and hardening step for `PSDM`
  are inferred from the design rules and general practice.
* How the `cpsdm` reticle is generated from `psdm` — in particular
  whether resistor heads, taps or other structures are added by
  Boolean operations — is not public beyond the existence of the
  add/drop purposes.[^pdk-06]
* Whether both {ref}`PSDI <step-082>` and {ref}`2PSDI <step-083>`
  use this resist without any intermediate step is inferred from the
  PDK's single "P+ Implant, PSDM" mask.[^pdk-05]

<!-- footnotes -->

[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-07]: SkyWater PDK Authors, *Device Details*, SkyWater SKY130 PDK
    documentation, and the per-device cross-section drawings.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://github.com/google/skywater-pdk/tree/main/docs/rules/device-details>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (sheet-resistance table), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^asml-30]: ASML, *Three decades of PAS 5500*, 2021, accessed
    2026-09-13. <https://www.asml.com/en/company/stories/2021/three-decades-of-pas-5500>
[^hook-2003]: T. B. Hook, J. Brown, P. Cottrell, E. Adler, D. Hoyniak,
    J. Johnson and R. Mann, "Lateral Ion Implant Straggle and Mask
    Proximity Effect", *IEEE Transactions on Electron Devices*
    **50**(9), 1946–1951 (2003).
    <https://doi.org/10.1109/TED.2003.815371>; open copy
    <https://ewh.ieee.org/r5/denver/sscs/References/2003_09_Hook.pdf>
[^sheu-2006]: Y.-M. Sheu, K.-W. Su, S. Tian, S.-J. Yang, C.-C. Wang,
    M.-J. Chen and S. Liu, "Modeling the Well-Edge Proximity Effect in
    Highly Scaled MOSFETs", *IEEE Transactions on Electron Devices*
    **53**(11), 2792–2798 (2006).
    <https://doi.org/10.1109/TED.2006.884070>
[^drennan-2006]: P. G. Drennan, M. Kniffin and D. Locascio,
    "Implications of Proximity Effects for Analog Design", *Proc. IEEE
    Custom Integrated Circuits Conference 2006*, pp. 169–176.
    <https://doi.org/10.1109/CICC.2006.320869>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007,
    ISBN 978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^smith-1983]: T. C. Smith, "Wafer Cooling and Photoresist Masking
    Problems in Ion Implantation", in *Ion Implantation: Equipment and
    Techniques*, Springer Series in Electrophysics, Springer, 1983,
    pp. 196–213. <https://doi.org/10.1007/978-3-642-69156-0_25>
[^romig-1996]: T. Romig, M. Bishop and V. Rio, "Exploration and
    prevention of photo resist burning in a high current ion
    implanter", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 190–193.
    <https://doi.org/10.1109/IIT.1996.586181>
[^lee-1996]: W. J. Lee, N. Tokoro, H. T. Cho, J. O. Borland, M. Dennon
    and C. Kozak, "Thick photoresist outgassing during MeV implantation
    (mechanism and impact on production)", *Proc. 11th International
    Conference on Ion Implantation Technology* (1996), pp. 186–189.
    <https://doi.org/10.1109/IIT.1996.586180>
[^horsky-1998]: T. N. Horsky, "Photoresist outgassing in high energy and
    high current ion implantation", *Proc. 1998 International Conference
    on Ion Implantation Technology*, vol. 1, pp. 654–657.
    <https://doi.org/10.1109/IIT.1999.812201>
[^carpenter-2002]: N. Carpenter and T. Fecteau, "Process and
    productivity improvements during high pressure photoresist
    outgassing", *Proc. 14th International Conference on Ion
    Implantation Technology* (2002), pp. 507–510.
    <https://doi.org/10.1109/IIT.2002.1258053>
[^dixon-1996]: W. Dixon, W. Lukaszek and C. Heden,
    "Photoresist-enhanced wafer charging during high current ion
    implantation", *Proc. 11th International Conference on Ion
    Implantation Technology* (1996), pp. 85–88.
    <https://doi.org/10.1109/IIT.1996.586134>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
