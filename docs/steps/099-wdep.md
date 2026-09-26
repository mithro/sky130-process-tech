(step-099)=
# Step 099 — WDEP: Blanket CVD W deposition

| | |
|---|---|
| **Step number** | 99 of 171[^steps-sheet] |
| **Step code** | `WDEP` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | {term}`MOL` — silicide and local interconnect |
| **Previous step** | {ref}`CSIL <step-098>` |
| **Next step** | {ref}`WCMPLI <step-100>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** fills the contact holes with tungsten: a blanket film
  grown by chemical vapour deposition from tungsten hexafluoride onto
  the TiN-lined wafer.
* **Why:** sputtering cannot fill a deep hole and CVD tungsten can; the
  polish that follows leaves the tungsten plug in each `licon1`.
* **Public numbers:** none for the film; the hole has a 0.08 µm
  bottom[^pdk-03] under 0.5 µm of dielectric.[^pdk-03]
* **Likely SkyWater tool:** Lam/Novellus CVD tungsten with PNL —
  **strong** (the vendor, the plug-fill application and the
  pulsed-nucleation capability); **inferences** (the model and the
  assignment to this step).[^skw-01]
* **Not public:** the film thickness, the nucleation chemistry and the
  deposition temperature and pressure (→ Open questions).
:::

## What this step is

`WDEP` fills the contact holes with tungsten. A blanket film is grown
by chemical vapour deposition from tungsten hexafluoride onto the
TiN-lined wafer of {ref}`TI/TIN1 <step-097>`. It is a thin {term}`nucleation layer`
first, then a bulk film thick enough that the conformal growth from
the walls of every hole meets in the middle and closes it.

The
tungsten covers the field as well as the holes; the polish that
follows ({ref}`WCMPLI <step-100>`) removes it from the field and
leaves the {term}`W plug` in each `licon1`. The film thickness is not
public. A blanket of somewhat more than half the hole's top width —
of the order of 0.2–0.3 µm for a 0.17 µm contact[^pdk-periph] with
polishing margin — is the industry-typical target for a plug fill
(category page[^txt-01]).

:::{figure} /_static/figures/mol-099-wdep.svg
:alt: Two enlarged cross-sections of one contact hole beside a transistor gate, one above the other. Before the step a thin purple film lines the hole, with a teal disc under it at the bottom. After it a cross-hatched grey metal fills the hole completely and covers the whole flat top in an even layer, with a V-shaped notch over the hole reaching most of the way down to the liner.
:width: 560px
:name: fig-mol-099-wdep

A close-up of the 1.8 V source/drain contact, beside the gate. Before, the lined hole with its silicide; after, tungsten grown from every surface has closed the hole and covers the field. The film thickness is not public; the industry-typical plug-fill target the page gives is 0.2–0.3 µm ("of the order of"),[^txt-01] and it is not drawn to scale. The thin nucleation layer and the seam where the growth from the walls meets are not drawn; the deep notch over the hole comes from the drawn thickness, not from the page. The other two holes are filled in the same way, outside this view. The colours mark the type of the doping, not a depth profile. The gate, its caps and spacers, the thin oxides, the silicon and its doped regions, the silicide and the field oxide at the left edge are drawn but not labelled, as is the contact liner in the lower panel, and the liner oxide is drawn faded; the P-well and the NCHI channel implant made earlier are not drawn. Not to scale.
:::

Two public facts anchor the step:

* SkyWater lists "Lam/Novellus PECVD
  Tungsten" with the sub-bullets "plug fill" and "PNL option for high
  aspect ratio (up to 10:1)" among its deposition tools,[^skw-01] and
  "W plug dual damascene" among its special
  modules.[^skw-01]
* The PDK describes `licon1` as the "Contact to local
  interconnect".[^pdk-06] Its extraction tables list the LICON contact
  at 15 000 in a column headed "Resistivity (mohms/sq)", which we read
  as 15 Ω per contact, since a contact has no sheet
  dimension[^pdk-08] (our reading). Its physical criteria give a "min. etch and
  fill capability" of 0.15 µm for licon.[^pdk-03]

This reference uses
the same blanket-fill-and-polish scheme at every level: `WDEP` here
and {ref}`WDEP2 <step-110>` to {ref}`WDEP5 <step-147>` at the contact
and {term}`via` levels.

## Step category

`WDEP` is a {ref}`Thin-film deposition <category-deposition>` step of
the *CVD tungsten* type, which the category page
describes:[^wiki-wf6][^txt-01]

1. a
   nucleation layer by silane reduction, 2WF₆ + 3SiH₄ → 2W + 3SiF₄ + 6H₂;
2. then the bulk fill by hydrogen reduction, WF₆ + 3H₂ → W + 6HF, at
   roughly 400–450 °C and a few tens of Torr.

CVD tungsten is,
in the category page's words, "almost perfectly conformal, so it fills
contacts from the sidewalls inward and leaves only a small seam".
`WDEP`
is the first {term}`CVD` metal in the flow and the first film deposited on a
metallised wafer, so the
thermal ceiling is now the {term}`silicide` and the {term}`liner` rather than the
junctions.

What is specific to this instance is the
{term}`aspect ratio`: a 0.08 µm bottom[^pdk-03] under 0.5 µm of dielectric[^pdk-03]
is the narrowest hole the tungsten will ever have to fill in SKY130.
The "PNL option for high aspect ratio (up to 10:1)" of
SkyWater's tool[^skw-01] — a {term}`pulsed nucleation layer` — is the
technique developed for such holes.

## Why this step exists

Tungsten plugs replaced sputtered aluminium in contacts at the
sub-micron nodes because sputtering cannot fill a deep hole and CVD
tungsten can. Kaanta et al. built the tungsten-stud plus
planarisation wiring scheme at IBM in 1987,[^kaanta-1987] and
Broadbent and Ramiller had established the WF₆ chemistry in
1984.[^rev-03] The properties that matter here:

* **Conformality and fill.** CVD tungsten grows at nearly the same
  rate on every surface the gas reaches, so a hole fills from its
  walls inward.

  If the mouth closes before the bottom, a void or
  seam is left that the polish opens and the next liner cannot
  cover. The 10° taper of the licon[^pdk-03] helps by keeping the
  mouth wider than the bottom. Kleijn et al. modelled transport in a
  single-wafer tungsten reactor[^kleijn-1991] and McConica and
  Krishnamani the kinetics of the hydrogen reduction.[^mcconica-1986]
* **Nucleation.** Tungsten does not nucleate readily on oxide or
  TiN from WF₆/H₂ — McConica and Cooper studied nucleation on
  thermal oxide[^mcconica-1988] and Srinivas et al. on
  TiN[^srinivas-1992] — so a silane-reduced nucleation layer is
  grown first.

  Tripathi and Moghadam describe a silane-rich
  process.[^tripathi-1994] The nucleation layer's thickness,
  resistivity and conformality set the plug's resistance and fill,
  which is why the pulsed nucleation layer was developed.

  Novellus's
  patent describes a tungsten nucleation film formed "by
  alternatively providing to that surface, reducing gases and
  tungsten containing gases" so that the film "is conformal and has
  improved step coverage, even for a high aspect ratio contact
  hole".[^pat-pnl-novellus] Kim et al. characterise pulsed CVD
  tungsten as a nucleation layer for plug fill.[^kim-2004] Petri et
  al. examined how nitrogen affects post-nucleation growth.[^petri-1998]
* **Barrier dependence.** WF₆ attacks silicon, titanium and
  aluminium, and the HF by-product attacks oxide; the TiN liner is
  what keeps the fluorine from the silicide and the junction
  (category page). Koerner et al. evaluated the Ti and TiN
  thicknesses needed.[^koerner-1993] A liner pinhole becomes a
  "volcano" or a wormhole in the silicon.
* **Resistance.** The PDK's 15 Ω per licon[^pdk-08] is the sum of
  the silicide interface, the liner and the plug; tungsten's
  resistivity in thin CVD films is several times its bulk value, so
  the nucleation layer is kept thin and the bulk film's grain
  structure large.
* **Stress.** CVD tungsten is highly tensile, and a thick blanket
  bows the wafer; the blanket is therefore no thicker than the fill
  needs.

Without `WDEP` the contacts would be empty and the {term}`local interconnect`
would have nothing to land on.

## How it is typically performed

*An industry-generic tungsten plug fill for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):*

1. **Tool.** Single-wafer or multi-station CVD reactor with a heated
   pedestal, WF₆, SiH₄, H₂, N₂ and Ar delivery, and an NF₃ (or
   remote-plasma fluorine) chamber clean; Novellus's Concept Two
   Altus and Applied Materials' Centura WxZ were the 200 mm tools
   (category page[^novellus-history]).
2. **Nucleation layer.** Either a silane-reduced seed
   (WF₆ + SiH₄, a few nanometres) or a pulsed nucleation layer —
   alternating SiH₄ (or B₂H₆) and WF₆ exposures, each depositing a
   monolayer-scale amount, until a continuous, conformal seed of a
   few nanometres has formed.[^pat-pnl-novellus][^kim-2004]
3. **Bulk fill.** WF₆/H₂ at 400–450 °C and 30–90 Torr (typical
   industry values[^txt-01][^wiki-wf6]) at rates of a few hundred
   nanometres per minute until the holes close and the field film
   reaches its target; argon or nitrogen as carrier. The ratio of
   WF₆ to H₂ and the temperature set grain size and
   resistivity.[^mcconica-1986]
4. **Post-deposition.** Chamber clean between wafers; the wafer goes
   to the tungsten polish. No anneal is needed.
5. **Metrology.** {term}`Sheet resistance <sheet resistance>` and thickness of the blanket by
   {term}`four-point probe` and XRF; stress by wafer bow;
   cross-section SEM of filled contacts for seams and voids during
   development; fluorine content by SIMS when the liner is being
   qualified.

## Machines typically used

* **{ref}`CVD tungsten reactor <machine-tungsten-cvd>`**, 200 mm: Novellus Concept Two Altus and
  Altus with {term}`PNL`,[^novellus-history] Applied Materials Centura WxZ,
  Genus and Ulvac tungsten systems (category page).
* **{ref}`Four-point probe <machine-sheet-resistance-metrology>`**, **{ref}`XRF <machine-film-thickness-metrology>`**, **stress gauge**, **{ref}`cross-section SEM <machine-cross-section-sem-profilers>`**.

## Machines likely used at SkyWater

* **Lam/Novellus CVD tungsten with PNL**
  - *SkyWater says:* lists
    "Lam/Novellus PECVD Tungsten" with the sub-bullets "plug fill" and
    "PNL option for high aspect ratio (up to 10:1)".[^skw-01]
  - *Tool exists:* **strong** for the vendor, the plug-fill application and
    the pulsed-nucleation capability.
  - *Runs this step:* the model (an Altus-class
    system, we infer from Novellus's product history[^novellus-history])
    and the assignment to this step are **inferences** — though a
    plug fill is what the entry says and this is the flow's first plug
    fill.

  Novellus's PNL patent describes the nucleation technique the
  entry names.[^pat-pnl-novellus] SkyWater's wording "PECVD
  Tungsten"[^skw-01] we read as a label for the tungsten CVD tool
  rather than a statement of a plasma-driven deposition (inference).
* **"W plug dual damascene" special module.**[^skw-01] Strength:
  strong for the existence of tungsten-plug processing; the
  "damascene" wording is not explained on the page.

## Resources required

* **{ref}`Tungsten hexafluoride <material-precursors>`** (WF₆),[^wiki-wf6] **silane** (and
  possibly **diborane**) for nucleation, **{ref}`hydrogen <material-process-gases>`** for the bulk
  reduction, **argon** and **nitrogen** as carriers.
* **{ref}`NF₃ <material-etch-gases>`** for chamber cleaning; {ref}`fluorine-tolerant exhaust <material-hardware-consumables>` and
  scrubbing for HF and SiF₄ by-products.[^txt-09]
* **Chamber consumables** — pedestal heaters, showerheads, liners.
* **{ref}`Monitor wafers <material-substrates>`** (SEMI M8 class)[^semi-m8] with TiN for
  thickness, resistance and particle control.
* Gas suppliers named in SkyWater's filings: Air Products and Praxair (2021
  S-1), Linde and Airgas (fiscal 2023 10-K).[^sec-01][^sec-02]

## Related steps and cross-references

* Previous: {ref}`CSIL <step-098>` (the silicide under the plug).
* Next: {ref}`WCMPLI <step-100>` (the polish that leaves the plugs),
  then {ref}`LITIN <step-101>`.
* Depends on: the liner it grows on, {ref}`TI/TIN1 <step-097>`; the holes it
  fills, {ref}`LICM1E <step-094>`.
* Same category: later tungsten fills, {ref}`WDEP2 <step-110>`,
  {ref}`WDEP3 <step-121>`, {ref}`WDEP4 <step-132>`,
  {ref}`WDEP5 <step-147>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

<!-- index-links:begin (generated by tools/gen_index_links.py; do not edit) -->
### Patents, papers and filings about this step

* {ref}`Method for producing ultra-thin tungsten layers with improved step coverage <patent-gp46204269>` — US 6,635,965 B1 (2001)

:::{dropdown} 1 family in force or status unknown

Status and expiry are estimates from public records and are not legal advice.

* {ref}`US 7,323,411 B1 <patent-gp38973875>` — unknown
:::
<!-- index-links:end -->

## References

### Cross-check

* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — "Lam/Novellus PECVD
  Tungsten": "plug fill", "PNL option for high aspect ratio (up to
  10:1)"; "W plug dual damascene".[^skw-01]
* [SkyWater PDK, *Layers Reference*](<https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>) — `licon1` "Contact to local
  interconnect".[^pdk-06]
* [SkyWater PDK, *Parasitic Layout Extraction*](<https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>) — LICON contact
  15 000 mΩ.[^pdk-08]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — "min. etch and fill
  capability … licon" 0.15 µm; bottom CD 0.08 µm; etch angle 10°;
  "Pre-LI ILD thickness" 0.5 µm.[^pdk-03]
* [SkyWater PDK, *Periphery rules*](<https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>) — licon.1 0.170 µm.[^pdk-periph]
* [Lee and Collins (Novellus), US 6,635,965](<https://patents.google.com/patent/US6635965B1/en>) — the pulsed nucleation
  layer.[^pat-pnl-novellus]
* [Encyclopedia.com, *Novellus Systems, Inc.*](<https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>) — the Altus
  line.[^novellus-history]
* SkyWater, Form S-1 (2021) and Form 10-K (fiscal 2023) — gas
  suppliers.[^sec-01][^sec-02]

### High-level understanding

* [Wikipedia, *Tungsten hexafluoride*](<https://en.wikipedia.org/wiki/Tungsten_hexafluoride>) — the CVD chemistry.[^wiki-wf6]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — CVD
  tungsten and plug formation.[^txt-01]
* [Nishi and Doering (eds.), *Handbook of Semiconductor Manufacturing
  Technology*](<https://openlibrary.org/isbn/9781574446753>) — tungsten CVD equipment and abatement.[^txt-09]

### Deep dive

* [Broadbent and Ramiller, *J. Electrochem. Soc.* 1984](<https://doi.org/10.1149/1.2115864>) — the
  foundational WF₆ reduction kinetics.[^rev-03]
* [Kaanta et al. (IBM), IEDM 1987](<https://doi.org/10.1109/IEDM.1987.191389>) — tungsten studs with
  planarisation.[^kaanta-1987]
* [McConica and Krishnamani, *J. Electrochem. Soc.* 1986](<https://doi.org/10.1149/1.2108468>) — kinetics of
  LPCVD tungsten in a single-wafer reactor.[^mcconica-1986]
* [McConica and Cooper, *J. Electrochem. Soc.* 1988](<https://doi.org/10.1149/1.2095756>) — tungsten
  nucleation on thermal oxide.[^mcconica-1988]
* [Kleijn et al., *J. Electrochem. Soc.* 1991](<https://doi.org/10.1149/1.2085620>) — transport phenomena in
  a single-wafer tungsten reactor.[^kleijn-1991]
* [Srinivas et al., *MRS Proc.* 1992](<https://doi.org/10.1557/PROC-282-365>) — nucleation of tungsten on
  TiN.[^srinivas-1992]
* [Tripathi and Moghadam, *MRS Proc.* 1994](<https://doi.org/10.1557/PROC-337-561>) — a silane-rich CVD
  tungsten process.[^tripathi-1994]
* [Petri et al., IITC 1998](<https://doi.org/10.1109/IITC.1998.704792>) — nitrogen and post-nucleation tungsten
  growth.[^petri-1998]
* [Kim et al., *Electrochem. Solid-State Lett.* 2004](<https://doi.org/10.1149/1.1784053>) — pulsed CVD
  tungsten nucleation for plug fill.[^kim-2004]
* [Lee and Collins (Novellus), US 6,635,965](<https://patents.google.com/patent/US6635965B1/en>) — ultra-thin tungsten
  nucleation with improved step coverage.[^pat-pnl-novellus]
* [Koerner, Erb and Melzner, *Appl. Surf. Sci.* 1993](<https://doi.org/10.1016/0169-4332(93)90139-3>) — the liner
  thicknesses a tungsten plug needs.[^koerner-1993]

## Open questions

* **Film thickness and chemistry.** The tungsten film thickness, the nucleation chemistry (silane or
  diborane; conventional or pulsed) and the deposition temperature
  and pressure are not public; the PNL reading is an inference from
  SkyWater's "PNL option" entry.
* **Novellus/Lam model.** Which Novellus/Lam model is used, and whether the same tool serves
  the via levels, is not public.
* **Label for the tool.** SkyWater's phrase "PECVD Tungsten"[^skw-01] is read here as a label
  for the tungsten CVD tool rather than evidence of a plasma-assisted
  deposition; no public source clarifies it.
* **What the phrase refers to.** What SkyWater's "W plug dual damascene" phrase refers to is not
  explained on the public page.

<!-- footnotes -->

[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^sec-01]: SkyWater Technology, Inc., Form S-1 (registration statement),
    filed 2021-03-22.
    <https://www.sec.gov/Archives/edgar/data/1819974/000119312521089687/d26688ds1.htm>
[^sec-02]: SkyWater Technology, Inc., Form 10-K for fiscal year 2023,
    filed 2024.
    <https://www.sec.gov/Archives/edgar/data/1819974/000181997424000008/skyt-20231231.htm>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-08]: SkyWater PDK Authors, *Parasitic Layout Extraction* page
    (resistance and capacitance tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/rcx.html>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^wiki-wf6]: Wikipedia, *Tungsten hexafluoride*.
    <https://en.wikipedia.org/wiki/Tungsten_hexafluoride>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-09]: Y. Nishi and R. Doering (eds.), *Handbook of Semiconductor
    Manufacturing Technology*, 2nd ed., CRC Press, 2007,
    ISBN 978-1-57444-675-3. <https://openlibrary.org/isbn/9781574446753>
[^semi-m8]: SEMI M8, *Specification for Polished Monocrystalline Silicon
    Test Wafers*, SEMI.
    <https://store-us.semi.org/products/m00800-semi-m8-specification-for-polished-monocrystalline-silicon-test-wafers>
[^rev-03]: E. K. Broadbent and C. L. Ramiller, "Selective Low Pressure
    Chemical Vapor Deposition of Tungsten", *Journal of The
    Electrochemical Society* **131**(6), 1427–1433 (1984).
    <https://doi.org/10.1149/1.2115864>
[^kaanta-1987]: C. Kaanta, W. Cote, J. Cronin, K. Holland et al.,
    "Submicron wiring technology with tungsten and planarization", *IEDM
    1987 Technical Digest*, pp. 209–212.
    <https://doi.org/10.1109/IEDM.1987.191389>
[^mcconica-1986]: C. M. McConica and K. Krishnamani, "The Kinetics of
    LPCVD Tungsten Deposition in a Single Wafer Reactor", *Journal of
    The Electrochemical Society* **133**(12), 2542–2548 (1986).
    <https://doi.org/10.1149/1.2108468>
[^mcconica-1988]: C. M. McConica and K. Cooper, "Tungsten Nucleation on
    Thermal Oxide during LPCVD of Tungsten by the Hydrogen Reduction of
    Tungsten Hexafluoride", *Journal of The Electrochemical Society*
    **135**(4), 1003–1008 (1988). <https://doi.org/10.1149/1.2095756>
[^kleijn-1991]: C. R. Kleijn, C. J. Hoogendoorn, A. Hasper, J. Holleman
    and J. Middelhoek, "Transport Phenomena in Tungsten LPCVD in a
    Single-Wafer Reactor", *Journal of The Electrochemical Society*
    **138**(2), 509–517 (1991). <https://doi.org/10.1149/1.2085620>
[^srinivas-1992]: D. Srinivas, R. Foster, S. Marcus, R. Arora and
    H. Rebenne, "Nucleation of Tungsten on Titanium Nitride with
    Hydrogen Reduction of Tungsten Hexafluoride", *MRS Proceedings*
    **282** (1992). <https://doi.org/10.1557/PROC-282-365>
[^tripathi-1994]: S. Tripathi and F. Moghadam, "Development of a Silane
    Rich CVD Tungsten Process", *MRS Proceedings* **337** (1994).
    <https://doi.org/10.1557/PROC-337-561>
[^petri-1998]: R. Petri, H. Hauf, D. Berenbaum, J. C. Favreau and
    P. Mazet, "Nitrogen effect on post-nucleation tungsten CVD film
    growth", *Proc. IEEE 1998 International Interconnect Technology
    Conference*, pp. 202–204. <https://doi.org/10.1109/IITC.1998.704792>
[^kim-2004]: S.-H. Kim, E.-S. Hwang, S.-Y. Han, S.-H. Pyi, N. Kwak,
    H. Sohn, J. Kim and G. B. Choi, "Pulsed CVD of Tungsten Thin Film
    as a Nucleation Layer for Tungsten Plug-Fill", *Electrochemical and
    Solid-State Letters* **7**(9), G195 (2004).
    <https://doi.org/10.1149/1.1784053>
[^pat-pnl-novellus]: S.-H. Lee and J. Collins (Novellus Systems),
    *Method for producing ultra-thin tungsten layers with improved step
    coverage*, US 6,635,965 B1, filed 2001-10-09, granted 2003-10-21.
    <https://patents.google.com/patent/US6635965B1/en>
[^koerner-1993]: H. Koerner, H. P. Erb and H. Melzner, "Evaluation of
    Ti and TiN thicknesses for tungsten plug contact metallization",
    *Applied Surface Science* **73**, 6–13 (1993).
    <https://doi.org/10.1016/0169-4332(93)90139-3>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
