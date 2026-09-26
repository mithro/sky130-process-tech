(step-117)=
# Step 117 — NCAPOX3: CAPOX deposition

| | |
|---|---|
| **Step number** | 117 of 171[^steps-sheet] |
| **Step code** | `NCAPOX3` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | {term}`BEOL` — contact and metal 1 |
| **Previous step** | {ref}`CMPM <step-116>` |
| **Next step** | {ref}`VIM <step-118>` |

:::{admonition} At a glance
:class: at-a-glance

* **Does:** deposits a thin plasma oxide on the polished
  {ref}`NILD3 <step-115>` that seals its surface and, we infer, brings
  the dielectric above metal 1 to its final thickness.
* **Why:** a polish alone does not give a via level what it needs.
* **Public numbers:** via-1 height through NILD3 0.27 µm;[^pdk-04] the
  cap's own thickness is not public.
* **Likely SkyWater tool:** PECVD TEOS "C2 and Producer" — **strong**
  for the capability; the assignment of the cap oxide to the TEOS
  process is an **inference**.[^skw-01]
* **Not public:** the cap's precursor, thickness and deposition
  conditions, and whether "NILD3_C" is this cap (→ Open questions).
:::

## What this step is

`NCAPOX3` deposits a *cap oxide* on the polished inter-level
dielectric ({term}`ILD`). After {ref}`CMPM <step-116>` the {ref}`NILD3 <step-115>`
oxide is flat but its thickness above the metal-1 lines is whatever
the polish left — a target with a tolerance — and its surface carries
the scratches, slurry residue and hydrated layer of a polish. A thin
plasma oxide deposited over it seals that surface and, we infer from
the PDK's finished via-1 height and the polish's thickness variation
(see below), brings the dielectric above metal 1 to its final
thickness before the via-1 mask
({ref}`VIM <step-118>`) is printed.

The finished number is public:
the PDK's stack diagram gives the via-1 height through NILD3 as
0.27 µm.[^pdk-04] The cap's own thickness is not. A similar cap is
described at {ref}`NCAPOX <step-091>` over the
{term}`pre-metal dielectric`. The cap recurs as
{ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>` and
{ref}`NCAPOX6 <step-158>` above each polished metal level.

:::{figure} /_static/figures/m1-117-ncapox3.svg
:alt: Two cross-sections of the wafer, one above the other. Before the step a flat pale oxide buries three metal lines. After it a thin flat layer of the same pale oxide covers the whole top.
:width: 560px
:name: fig-m1-117-ncapox3

Before, the polished inter-metal oxide; after, a thin cap oxide over it, which with the oxide left by the polish makes up the dielectric over metal 1 on which the via-1 mask is printed. In the PDK's stack diagram that finished height is 0.27 µm;[^pdk-04] how thick the cap itself is is not public (the page gives of the order of 0.05–0.15 µm as industry-typical[^txt-05]), and that it sets the final thickness is the page's inference. Whether the thin "NILD3_C" film of the diagram is this cap is not public. Nothing is drawn to scale. The bottom and cap films of the metal lines, the inter-level oxide under them, the metal contacts, the local interconnect, the glass, the cap oxide under the local interconnect, the lower tungsten plugs, the silicide discs, the contact liners and the transistors' films (the spacers, the caps, the gate oxides, the gate film, the re-oxidation oxide and the spacer oxide), the doped regions and the field oxide (the oxide-filled trench in the middle) are drawn but not labelled, and the liner oxide is drawn faded; the P-well and the NCHI channel implant made earlier are not drawn. Not to scale.
:::

The stack diagram offers one further public hint. Beside "NILD3
K=4.5" it draws a "NILD3_C" of permittivity 3.5 and thickness
0.030 µm,[^pdk-04] and the same pairing recurs as NILD4/NILD4_C at the
next level.[^pdk-04] The thinness and the placement are consistent
with this {term}`cap oxide`, as they are with a {term}`liner` under the
{term}`gap fill` ({ref}`NILD3 <step-115>`) (inference). The "_C" suffix is
suggestive but the diagram does not say what it stands for, and a
permittivity of 3.5 is lower than a plain plasma oxide's (inference;
see *Open questions*).

## Step category

`NCAPOX3` is a {ref}`Thin-film deposition <category-deposition>` step
of the *{term}`PECVD` oxide* class (PECVD on our reading: the
aluminium beneath rules out furnace oxides) — the category page's
PECVD section.

It is the simplest deposition in the module: a blanket,
thin, low-temperature oxide on a flat surface with no gap to fill and
no stop to respect.

Its relatives are the other cap oxides
({ref}`NCAPOX <step-091>`, {ref}`NCAPOX4 <step-128>` and above) and
the dielectric thickness-setting layers generally.

What is specific
to this instance is that it sits directly under the via-1 lithography
and etch, so its thickness uniformity and its surface are what those
steps see.

## Why this step exists

A polish alone does not give a {term}`via` level what it needs:

* **Thickness control.** The polish of {ref}`CMPM <step-116>` is
  stopped by removal amount and varies with {term}`pattern density` and
  across the wafer — the variation Boning et al. and Chang et al.
  characterised for ILD {term}`CMP`.[^boning-1994][^chang-1995]

  Polishing to
  a thickness *below* the target and adding a cap of well-controlled
  thickness is the standard way to tighten the final dielectric
  thickness (industry practice[^txt-05]), which in turn tightens the
  {term}`over-etch` the {ref}`VIME <step-119>` via etch needs to reach every
  metal-1 cap ({ref}`overview-metal-cap`). The PDK's "Via1 slope" of 0.02 and via {term}`CD` of 0.15 µm[^pdk-03]
  are the geometry that thickness control serves.
* **Sealing the polished surface.** Oxide CMP leaves micro-scratches
  and embedded slurry particles — Devriendt et al. relate those
  defects to the {term}`post-CMP clean`[^devriendt-1998] — and a hydrated,
  hydroxyl-rich surface layer.[^moon-2016]

  A fresh plasma oxide buries
  them under a dense film so that they do not seed via-etch defects
  or resist adhesion failures, and so that the polished surface's
  water is not released into the via later (the "via poisoning" of
  moisture-bearing dielectrics; industry experience[^txt-05]).
* **A known surface for lithography.** The {ref}`VIM <step-118>`
  resist and {term}`BARC` are tuned to a reproducible oxide surface and
  thickness; the swing-curve reflectivity of a resist on oxide
  depends on the oxide's thickness, so a fixed cap gives a fixed
  exposure latitude.
* **Mechanical protection.** A dense cap over a possibly fluorinated
  or lower-density fill (the NILD3_C question) keeps moisture and the
  via-etch chemistry from the film beneath (inference from the
  general practice of capping fluorinated oxides[^txt-05]).

Without `NCAPOX3` the via-1 lithography and etch would work on a
surface whose thickness and condition varied with the polish, and the
via-1 chain yield would follow.

## How it is typically performed

*An industry-generic cap-oxide deposition for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public):*

1. **Chamber.** A single-wafer or twin-chamber PECVD reactor at
   350–400 °C (industry-typical[^txt-05][^raupp-1992]), the temperature
   limit being the aluminium beneath; SkyWater lists "PECVD TEOS, C2
   and Producer – low temp options" and "PECVD silane
   oxide/nitride/oxynitride, C1 – low temp, range of R.I.
   options".[^skw-01] Applied Materials' Producer twin-chamber
   platform[^amat-10k] and Novellus's Concept/Sequel
   family[^novellus-history] are the 200 mm-era tools.
2. **Precursor.** {term}`TEOS`/O₂ plasma oxide — Raupp, Cale and Hey analyse
   its kinetics and {term}`step coverage`[^raupp-1992] — or SiH₄/N₂O plasma
   oxide, whose properties depend on RF power as Chapple-Sokol,
   Tierney and Batey measured.[^chapple-sokol-1989]

   On a flat polished
   surface conformality does not matter and either works. The
   Cypress reports for Fab 4 processes (S8, and the 0.18 µm R7FT-3R
   derivative) list a "1000A TEOS" film under the nitride in the
   passivation,[^cyp-qtp-123907][^cyp-qtp-014807] which shows a PECVD
   TEOS oxide of cap-like thickness in the same flow. We infer, not
   from any public statement about this step, that the cap oxide is
   of the same kind.
3. **Thickness.** Not public; a cap of the order of 0.05–0.15 µm is
   typical of the practice (industry-typical value[^txt-05]), sized so
   that polished NILD3 plus cap reaches the 0.27 µm via-1 height of
   the PDK[^pdk-04] with the polish target set below it. If the
   0.030 µm "NILD3_C" of the diagram[^pdk-04] is this film, it is
   thinner than that.
4. **Film properties.** Density and hydrogen content matter more
   than for a gap fill.

   Hydrogen evolution from a plasma oxide on
   later heating changes its stress, as Mani and Saif
   showed,[^mani-2007] and a porous or wet cap defeats its purpose.
   The classic {term}`LPCVD` TEOS route[^adams-1979][^becker-1987] gives a
   denser film but at 650–750 °C, far above the aluminium limit, so
   it is not an option here (inference from the temperature).
5. **Clean before and after.** The wafer comes from the post-CMP
   scrub ({ref}`CMPM <step-116>`; Philipossian and Sun on the
   brushes[^philipossian-2009]); after deposition no clean is usual
   before the {ref}`VIM <step-118>` coat.
6. **Chamber clean.** NF₃ remote-plasma clean.
7. **Metrology.** Thickness and refractive index by ellipsometry on
   monitors and on product test pads; total dielectric thickness
   over metal-1 pads (the number the via etch is set against);
   stress by wafer bow; particles.

## Machines typically used

* **{ref}`PECVD oxide system <machine-pecvd>`**, 200 mm: Applied Materials Producer (twin
  chamber) or Centura DxZ,[^amat-10k] Novellus Concept One/Two,
  Sequel[^novellus-history] ({ref}`category-deposition`).
* **{ref}`Ellipsometer <machine-film-thickness-metrology>` / reflectometer**, **stress gauge**, **{ref}`particle inspection <machine-defect-inspection>`**.

## Machines likely used at SkyWater

* **PECVD TEOS "C2 and Producer" with "low temp options"**[^skw-01]
  - *Tool exists:* **strong** for the capability.
  - *Runs this step:* the assignment of the cap
    oxide to the TEOS process (rather than the silane "C1" oxide) is an
    **inference** from practice and from the TEOS oxide in the Cypress
    passivation description.[^cyp-qtp-123907]

  "C2" is, on our reading,
  a Novellus Concept Two and "Producer" an Applied Materials Producer;
  neither model is stated.
* **PECVD silane oxide "C1"**[^skw-01] as the alternative (medium).

## Resources required

* **{ref}`TEOS <material-precursors>`** (liquid, vaporised) and **{ref}`oxygen <material-process-gases>`**, or **silane** and
  **N₂O** for the silane route;[^wiki-teos][^wiki-pecvd] **helium**,
  **nitrogen** or **argon** as carrier or diluent (typical; the PECVD
  article describes TEOS deposition "in an oxygen or oxygen-argon
  plasma"[^wiki-pecvd]).
* **{ref}`NF₃ <material-etch-gases>`** for the chamber clean; **nitrogen** purge.
* **{ref}`Showerhead, heater and liner consumables <material-hardware-consumables>`**; **{ref}`monitor wafers <material-substrates>`**.

## Related steps and cross-references

* Previous: {ref}`CMPM <step-116>` (the polish it seals).
* Next:
  {ref}`VIM <step-118>` (the via-1 mask printed on it), then
  {ref}`VIME <step-119>`.
* Depends on: the dielectric it completes, {ref}`NILD3 <step-115>`; the metal
  beneath, {ref}`MM1E <step-114>`.
* Same category: the other cap oxides, {ref}`NCAPOX <step-091>`,
  {ref}`NCAPOX4 <step-128>`, {ref}`NCAPOX5 <step-143>`,
  {ref}`NCAPOX6 <step-158>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* [SkyWater PDK, *Process stack diagram*](<https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>) — via1 (NILD3) 0.27 µm;
  "NILD3_C K=3.5", 0.030 µm; NILD4/NILD4_C.[^pdk-04]
* [SkyWater PDK, *Criteria & Assumptions*](<https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>) — via CD 0.15 µm; "Via1
  slope" 0.02.[^pdk-03]
* [SkyWater, *Facilities & Capabilities*](<https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>) — "PECVD TEOS, C2 and
  Producer – low temp options"; "PECVD silane
  oxide/nitride/oxynitride, C1".[^skw-01]
* Cypress, QTP 123907/132302/132301 and QTP 014807 — "1000A TEOS" in
  the Fab 4 passivation stack.[^cyp-qtp-123907][^cyp-qtp-014807]
* [Applied Materials, Form 10-K (2003)](<https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>) — the Producer platform.[^amat-10k]
* [Encyclopedia.com, *Novellus Systems, Inc.*](<https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>) — Concept One/Two and
  Sequel.[^novellus-history]

### High-level understanding

* Wikipedia, [*Plasma-enhanced chemical vapor deposition*](<https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>), [*Tetraethyl
  orthosilicate*](<https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>).[^wiki-pecvd][^wiki-teos]
* [Plummer, Deal and Griffin, *Silicon VLSI Technology*](<https://openlibrary.org/isbn/9780130850379>) — PECVD
  oxides in the back end.[^txt-01]
* [Wolf, *Silicon Processing for the VLSI Era*, vol. 4](<https://openlibrary.org/isbn/9780961672171>) — ILD stacks,
  CMP and cap layers at the deep-submicron nodes.[^txt-05]
* [Seshan (ed.), *Handbook of Thin Film Deposition*](<https://openlibrary.org/isbn/9781437778731>) — PECVD
  equipment.[^seshan-2012]

### Deep dive

* Boning et al., SPIE 1994, and Chang et al., IEDM 1995 — the ILD
  thickness variation a cap is added to control.[^boning-1994][^chang-1995]
* [Raupp, Cale and Hey, *JVST B* 1992](<https://doi.org/10.1116/1.586361>) — PECVD TEOS oxide
  kinetics.[^raupp-1992]
* [Chapple-Sokol, Tierney and Batey (IBM), MRS 1989](<https://doi.org/10.1557/PROC-165-113>) — RF-power
  dependence of PECVD oxide properties.[^chapple-sokol-1989]
* [Mani and Saif, *Thin Solid Films* 2007](<https://doi.org/10.1016/j.tsf.2006.08.025>) — stress development in
  plasma oxide from hydrogen evolution.[^mani-2007]
* Adams and Capio (Bell Labs), [*J. Electrochem. Soc.*](<https://doi.org/10.1149/1.2129171>) 1979, and
  Becker et al. (Siemens), [*JVST B*](<https://doi.org/10.1116/1.583673>) 1987 — the LPCVD TEOS oxides the
  low-temperature cap cannot use.[^adams-1979][^becker-1987]
* [Devriendt et al. (IMEC), *Solid State Phenomena* 1998](<https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>) — oxide-CMP
  defects that the cap buries.[^devriendt-1998]
* [Philipossian and Sun, *Electrochem. Solid-State Lett.* 2009](<https://doi.org/10.1149/1.3058994>) —
  post-ILD-CMP scrubbing before the cap.[^philipossian-2009]
* [Moon, in *Advances in Chemical Mechanical Planarization*](<https://doi.org/10.1016/B978-0-08-100165-3.00001-2>) — the
  chemistry of the polished oxide surface.[^moon-2016]
* [Nguyen (IBM), *IBM J. Res. Dev.* 1999](<https://doi.org/10.1147/rd.431.0109>) — HDP and plasma dielectric
  film properties compared.[^nguyen-1999]
* [Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing*](<https://doi.org/10.1002/0471724254>) — plasma-enhanced deposition and film
  stress.[^lieberman-2005]

## Open questions

* **Precursor, thickness and conditions.** The cap's precursor (TEOS or silane), thickness and deposition
  conditions are not public.
* **Whether NILD3_C is this cap.** Whether the PDK's "NILD3_C" (k 3.5, 0.030 µm)[^pdk-04] is this cap,
  a liner under the fill, or neither is not public; its permittivity
  does not match a plain plasma oxide.
* **How the via-1 height is divided.** How the 0.27 µm via-1 height[^pdk-04] is divided between the
  polished {ref}`NILD3 <step-115>` and this cap is not public.
* **Novellus Concept Two.** Whether "C2" denotes a Novellus Concept Two is an inference from
  the vendor's product names.[^novellus-history]

<!-- footnotes -->

[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>
[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^cyp-qtp-123907]: Cypress Semiconductor, *Fab Process Qualification
    Report, QTP# 123907, 132302, 132301: Metal Stack Change, S8
    Technology, Fab 4 CMI*, document 001-91369 Rev. **, March 2014
    (copy hosted by Tokyo Electron Device as the attachment to
    Cypress Product Information Notification PIN145273, 2014-03-13,
    which states the report is attached and available from
    cypress.com; <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/PIN145273.pdf>).
    <https://np.teldevice.co.jp/npapp/cgi-bin/npweb_gate.cgi/Website/pcn_pdn/other/cypress/145273-Qualification_Report.pdf>
[^cyp-qtp-014807]: Cypress Semiconductor, *Technology Derivative
    Qualification Report, QTP# 014807 Version 2.0: Technology
    Derivative R7FT-3R, Fab4, Synchronous Dual-Port RAM*, June 2005
    (copy hosted by Infineon Technologies).
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
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002,
    ISBN 978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
[^seshan-2012]: K. Seshan (ed.), *Handbook of Thin Film Deposition*,
    3rd ed., William Andrew, 2012, ISBN 978-1-4377-7873-1.
    <https://openlibrary.org/isbn/9781437778731>
[^boning-1994]: D. S. Boning, T. Maung, J. E. Chung, K.-J. Chang,
    S.-Y. Oh and D. Bartelink, "Statistical metrology for interlevel
    dielectric thickness variation", *Proc. SPIE* **2334**, Advanced
    Microelectronic Manufacturing, 316–327 (1994).
    <https://doi.org/10.1117/12.186764>
[^chang-1995]: E. Chang, B. Stine, T. Maung, R. Divecha, D. Boning,
    J. Chung, K. Chang, G. Ray, D. Bradbury, O. S. Nakagawa, S. Oh and
    D. Bartelink, "Using a statistical metrology framework to identify
    systematic and random sources of die- and wafer-level ILD
    thickness variation in CMP processes", *IEDM 1995 Technical
    Digest*, pp. 499–502. <https://doi.org/10.1109/IEDM.1995.499247>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
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
    Society* **126**(6), 1042–1046 (1979).
    <https://doi.org/10.1149/1.2129171>
[^becker-1987]: F. S. Becker, D. Pawlik, H. Anzinger and A. Spitzer,
    "Low-pressure deposition of high-quality SiO₂ films by pyrolysis of
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology
    B* **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^devriendt-1998]: K. Devriendt, E. Vrancken, N. Heylen, J. Grillaert,
    M. Meuris, M. M. Heyns and Z. C. Lin, "Relation between Oxide-CMP
    Induced Defects and Post-CMP Cleaning Strategies", *Solid State
    Phenomena* **65–66**, 173–176 (1998).
    <https://doi.org/10.4028/www.scientific.net/SSP.65-66.173>
[^philipossian-2009]: A. Philipossian and T. Sun, "Frictional Analysis
    of Various Poly(vinyl alcohol) Brush Roller Designs for
    Post-Interlevel Dielectric CMP Scrubbing Applications",
    *Electrochemical and Solid-State Letters* **12**(3), H84 (2009).
    <https://doi.org/10.1149/1.3058994>
[^moon-2016]: Y. Moon, "Chemical and physical mechanisms of dielectric
    chemical mechanical polishing (CMP)", in *Advances in Chemical
    Mechanical Planarization (CMP)*, Woodhead Publishing, 2016,
    pp. 3–26, ISBN 978-0-08-100165-3.
    <https://doi.org/10.1016/B978-0-08-100165-3.00001-2>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles
    of Plasma Discharges and Materials Processing*, 2nd ed., Wiley,
    2005, ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tab "Sheet1" (step number, code and description), retrieved 2026-09-14.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
