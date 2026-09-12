(step-128)=
# Step 128 — NCAPOX4: CAPOX deposition

| | |
|---|---|
| **Step number** | 128 of 171 |
| **Step code** | `NCAPOX4` |
| **Category** | {ref}`Thin-film deposition <category-deposition>` |
| **Phase** | BEOL — via 1, metal 2, via 2 |
| **Previous step** | {ref}`CMPM2 <step-127>` |
| **Next step** | {ref}`VIM2 <step-129>` |

## What this step is

`NCAPOX4` deposits a *cap oxide* on the polished inter-level
dielectric over metal 2. After {ref}`CMPM2 <step-127>` the
{ref}`NILD4 <step-126>` oxide is flat but its thickness above the
metal-2 lines is whatever the polish left — a target with a
tolerance — and its surface carries the scratches, slurry residue and
hydrated layer of a polish. A thin plasma oxide deposited over it
seals that surface and, on our reading of the step name and its
position, brings the dielectric above metal 2 to its final thickness
before the via-2 mask ({ref}`VIM2 <step-129>`) is printed. The
finished number is public: the PDK's stack diagram gives the via-2
height through NILD4 as 0.42 µm.[^pdk-04] The cap's own thickness is
not. It is the fourth "CAPOX" of the flow, after
{ref}`NCAPOX <step-091>` and {ref}`NCAPOX3 <step-117>` (the numbering
gap is discussed on the latter page), and recurs as
{ref}`NCAPOX5 <step-143>` and {ref}`NCAPOX6 <step-158>`.

The stack diagram again offers a hint. Beside "NILD4 K=4.2" it draws
a "NILD4_C" of permittivity 3.5 and thickness 0.030 µm,[^pdk-04]
the same pairing as NILD3/NILD3_C one level down. The suffix, the
thinness and the placement are consistent with this cap oxide, as
they are with a liner under the gap fill ({ref}`NILD4 <step-126>`);
the diagram does not say which, and a permittivity of 3.5 is lower
than a plain plasma oxide's (inference; see *Open questions*). What
differs from {ref}`NCAPOX3 <step-117>` is what the cap prepares for:
a 0.20 µm via[^pdk-periph] etched 0.42 µm deep,[^pdk-04] an
{term}`aspect ratio` of about 2.1:1 against 1.8:1 at via 1 — so the
thickness this cap completes is both larger and, per via, more
demanding of the {ref}`VIM2E <step-130>` etch.

## Step category

`NCAPOX4` is a {ref}`Thin-film deposition <category-deposition>` step
of the *{term}`PECVD` oxide* class — the category page's PECVD section
— and, like {ref}`NCAPOX3 <step-117>`, the simplest deposition in its
module: a blanket, thin, low-temperature oxide on a flat surface with
no gap to fill and no stop to respect. What is specific to this
instance is that it sits directly under the via-2 lithography and
etch, so its thickness uniformity and surface are what those steps
see, and that the wafer beneath it now carries two aluminium levels
whose temperature limit (roughly 400–450 °C, industry-typical for
Al–Cu[^txt-05]) it must respect.

## Why this step exists

A polish alone does not give a via level what it needs;
{ref}`NCAPOX3 <step-117>` sets out the four reasons, which apply here
with the via-2 numbers:

* **Thickness control.** The {ref}`CMPM2 <step-127>` polish is stopped
  by removal amount and varies with pattern density and across the
  wafer — the variation Boning et al. and Chang et al. characterised
  for ILD CMP.[^boning-1994][^chang-1995] Polishing to a thickness
  *below* the target and adding a cap of well-controlled thickness
  tightens the final 0.42 µm[^pdk-04] (industry practice[^txt-05]),
  which in turn tightens the over-etch {ref}`VIM2E <step-130>` needs
  to reach every TiW cap without punching through it.
* **Sealing the polished surface.** Oxide CMP leaves micro-scratches
  and embedded slurry particles — Devriendt et al. relate them to
  the post-CMP clean[^devriendt-1998] — and a hydrated, hydroxyl-rich
  surface layer;[^moon-2016] a fresh plasma oxide buries them so that
  they do not seed via-etch defects, and so that the polished
  surface's water is not released into the via later — the
  outgassing that poisons tungsten nucleation, which Kobayakawa et
  al. traced to planarising dielectrics.[^kobayakawa-1991]
* **A known surface for lithography.** The {ref}`VIM2 <step-129>`
  resist and BARC are tuned to a reproducible oxide surface and
  thickness; the swing-curve reflectivity of a resist on oxide over
  metal depends on the oxide's thickness,[^brunner-1991] so a fixed
  cap gives a fixed exposure latitude.
* **Mechanical protection.** A dense cap over a possibly fluorinated
  or lower-density fill (the NILD4_C question) keeps moisture and the
  via-etch chemistry from the film beneath (inference from the
  general practice of capping fluorinated oxides[^txt-05]).

Without `NCAPOX4` the via-2 lithography and etch would work on a
surface whose thickness and condition varied with the polish.

## How it is typically performed

An industry-generic cap-oxide deposition for a 200 mm, 130 nm-era fab
(SKY130's recipe is not public); the sequence is that of
{ref}`NCAPOX3 <step-117>`.

1. **Chamber.** A single-wafer or twin-chamber PECVD reactor at
   350–400 °C (industry-typical[^txt-05][^raupp-1992]); SkyWater lists
   "PECVD TEOS, C2 and Producer – low temp options" and "PECVD silane
   oxide/nitride/oxynitride, C1 – low temp, range of R.I.
   options".[^skw-01] Applied Materials' Producer twin-chamber
   platform[^amat-10k] and Novellus's Concept/Sequel
   family[^novellus-history] are the 200 mm-era tools.
2. **Precursor.** {term}`TEOS`/O₂ plasma oxide — Raupp, Cale and Hey
   analyse its kinetics[^raupp-1992] — or SiH₄/N₂O plasma oxide, whose
   properties depend on RF power as Chapple-Sokol, Tierney and Batey
   measured;[^chapple-sokol-1989] on a flat surface either works. The
   Cypress reports for Fab 4 processes list a "1000A TEOS" film in
   the passivation stack,[^cyp-qtp-123907][^cyp-qtp-014807] which
   shows a PECVD TEOS oxide of cap-like thickness in the same flow;
   we infer, not from any public statement about this step, that the
   cap is of the same kind.
3. **Thickness.** Not public; a cap of the order of 0.05–0.15 µm is
   typical of the practice (industry-typical value[^txt-05]), sized so
   that polished NILD4 plus cap reaches the 0.42 µm via-2 height of
   the PDK[^pdk-04]. If the 0.030 µm "NILD4_C" of the
   diagram[^pdk-04] is this film, it is thinner than that.
4. **Film properties.** Density and hydrogen content matter more than
   for a gap fill: hydrogen evolution from a plasma oxide on later
   heating changes its stress,[^mani-2007] and a porous or wet cap
   defeats its purpose. The LPCVD TEOS route[^adams-1979][^becker-1987]
   gives a denser film but at 650–750 °C, far above the aluminium
   limit, so it is not an option here (inference from the
   temperature).
5. **Clean before and after.** The wafer comes from the post-CMP
   scrub ({ref}`CMPM2 <step-127>`; Philipossian and Sun on the
   brushes[^philipossian-2009]); after deposition no clean is usual
   before the {ref}`VIM2 <step-129>` coat.
6. **Chamber clean.** NF₃ remote-plasma clean.
7. **Metrology.** Thickness and refractive index by ellipsometry on
   monitors and product test pads; total dielectric thickness over
   metal-2 pads (the number the via-2 etch is set against); stress
   by wafer bow; particles.

## Machines typically used

* **PECVD oxide system**, 200 mm: Applied Materials Producer (twin
  chamber) or Centura DxZ,[^amat-10k] Novellus Concept One/Two,
  Sequel[^novellus-history] ({ref}`category-deposition`).
* **Ellipsometer / reflectometer**, **stress gauge**, **particle
  inspection**.

## Machines likely used at SkyWater

* **PECVD TEOS "C2 and Producer" with "low temp options".**[^skw-01]
  Strength: **strong** for the capability; the assignment of the cap
  oxide to the TEOS process (rather than the silane "C1" oxide) is an
  **inference** from practice and from the TEOS oxide in the Cypress
  passivation description.[^cyp-qtp-123907] "C2" is, on our reading,
  a Novellus Concept Two and "Producer" an Applied Materials Producer;
  neither model is stated.
* **PECVD silane oxide "C1"**[^skw-01] as the alternative (medium).

## Resources required

* **TEOS** (liquid, vaporised) and **oxygen**, with **helium** or
  **nitrogen** carrier;[^wiki-teos] or **silane** and **N₂O** for the
  silane route.[^wiki-pecvd]
* **NF₃** for the chamber clean; **nitrogen** purge.
* **Showerhead, heater and liner consumables**; **monitor wafers**.

## Related steps and cross-references

* Previous: {ref}`CMPM2 <step-127>` (the polish it seals). Next:
  {ref}`VIM2 <step-129>` (the via-2 mask printed on it), then
  {ref}`VIM2E <step-130>`.
* The dielectric it completes: {ref}`NILD4 <step-126>`; the metal
  beneath: {ref}`MM2E <step-125>`.
* The other cap oxides: {ref}`NCAPOX <step-091>`,
  {ref}`NCAPOX3 <step-117>` (where the reasoning is set out in full),
  {ref}`NCAPOX5 <step-143>`, {ref}`NCAPOX6 <step-158>`.
* Category page: {ref}`Thin-film deposition <category-deposition>`.

## References

### Cross-check

* SkyWater PDK, *Process stack diagram* — via2 (NILD4) 0.42 µm;
  "NILD4_C K=3.5", 0.030 µm.[^pdk-04]
* SkyWater PDK, *Periphery rules* — via2.1a 0.200 µm.[^pdk-periph]
* SkyWater, *Facilities & Capabilities* — "PECVD TEOS, C2 and
  Producer – low temp options"; "PECVD silane
  oxide/nitride/oxynitride, C1".[^skw-01]
* Cypress, QTP 123907/132302/132301 and QTP 014807 — "1000A TEOS" in
  the Fab 4 passivation stack.[^cyp-qtp-123907][^cyp-qtp-014807]
* Applied Materials, Form 10-K (2003) — the Producer platform.[^amat-10k]
* Encyclopedia.com, *Novellus Systems, Inc.* — Concept One/Two and
  Sequel.[^novellus-history]

### High-level understanding

* Wikipedia, *Plasma-enhanced chemical vapor deposition*, *Tetraethyl
  orthosilicate*.[^wiki-pecvd][^wiki-teos]
* Plummer, Deal and Griffin, *Silicon VLSI Technology* — PECVD
  oxides in the back end.[^txt-01]
* Wolf, *Silicon Processing for the VLSI Era*, vol. 4 — ILD stacks,
  CMP and cap layers.[^txt-05]
* Seshan (ed.), *Handbook of Thin Film Deposition* — PECVD
  equipment.[^seshan-2012]

### Deep dive

* Boning et al., SPIE 1994, and Chang et al., IEDM 1995 — the ILD
  thickness variation a cap is added to control.[^boning-1994][^chang-1995]
* Raupp, Cale and Hey, *JVST B* 1992 — PECVD TEOS oxide
  kinetics.[^raupp-1992]
* Chapple-Sokol, Tierney and Batey (IBM), MRS 1989 — RF-power
  dependence of PECVD oxide properties.[^chapple-sokol-1989]
* Mani and Saif, *Thin Solid Films* 2007 — stress development in
  plasma oxide from hydrogen evolution.[^mani-2007]
* Adams and Capio (Bell Labs), 1979, and Becker et al. (Siemens),
  1987 — the LPCVD TEOS oxides the low-temperature cap cannot
  use.[^adams-1979][^becker-1987]
* Devriendt et al. (IMEC), *Solid State Phenomena* 1998 — oxide-CMP
  defects that the cap buries.[^devriendt-1998]
* Philipossian and Sun, *Electrochem. Solid-State Lett.* 2009 —
  post-ILD-CMP scrubbing before the cap.[^philipossian-2009]
* Moon, in *Advances in Chemical Mechanical Planarization* — the
  chemistry of the polished oxide surface.[^moon-2016]
* Kobayakawa et al., VMIC 1991 — outgassing from planarising
  dielectrics, the via-poisoning risk a dense cap reduces.[^kobayakawa-1991]
* Brunner, SPIE 1991 — the swing-curve dependence on the oxide under
  the resist.[^brunner-1991]
* Nguyen (IBM), *IBM J. Res. Dev.* 1999 — HDP and plasma dielectric
  film properties compared.[^nguyen-1999]
* Lieberman and Lichtenberg, *Principles of Plasma Discharges and
  Materials Processing* — plasma-enhanced deposition and film
  stress.[^lieberman-2005]

## Open questions

* The cap's precursor (TEOS or silane), thickness and deposition
  conditions are not public.
* Whether the PDK's "NILD4_C" (k 3.5, 0.030 µm)[^pdk-04] is this cap,
  a liner under the fill, or neither is not public.
* How the 0.42 µm via-2 height[^pdk-04] is divided between the
  polished {ref}`NILD4 <step-126>` and this cap is not public.
* Whether "C2" denotes a Novellus Concept Two is an inference from
  the vendor's product names.[^novellus-history]

<!-- footnotes -->

[^pdk-04]: SkyWater PDK Authors, *metal_stack.svg* (process stack
    diagram), google/skywater-pdk repository.
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/_static/metal_stack.svg>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
[^txt-05]: S. Wolf, *Silicon Processing for the VLSI Era, Vol. 4:
    Deep-Submicron Process Technology*, Lattice Press, 2002, ISBN
    978-0-9616721-7-1. <https://openlibrary.org/isbn/9780961672171>
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
[^kobayakawa-1991]: M. Kobayakawa, A. Arimatsu, F. Yokoyama, N. Hirashita
    and T. Ajioka, "A study of outgassing from spin-on-glass films used
    for planarization", *Proc. Eighth International IEEE VLSI Multilevel
    Interconnection Conference (VMIC 1991)*, pp. 454–456.
    <https://doi.org/10.1109/VMIC.1991.153054>
[^brunner-1991]: T. A. Brunner, "Optimization of optical properties of
    resist processes", *Proc. SPIE* **1466**, 297–308 (1991).
    <https://doi.org/10.1117/12.46410>
[^raupp-1992]: G. B. Raupp, T. S. Cale and H. P. W. Hey, "The role of
    oxygen excitation and loss in plasma-enhanced deposition of silicon
    dioxide from tetraethylorthosilicate", *Journal of Vacuum Science &
    Technology B* **10**(1), 37–45 (1992).
    <https://doi.org/10.1116/1.586361>
[^skw-01]: SkyWater Technology, *Facilities & Capabilities*, accessed
    2026-08-30. <https://www.skywatertechnology.com/manufacturing/facilities-capabilities/>
[^amat-10k]: Applied Materials, Inc., Form 10-K for fiscal 2003
    (platform descriptions: Centura, Endura, Endura SL, Producer).
    <https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm>
[^novellus-history]: Encyclopedia.com, *Novellus Systems, Inc.*
    (company history: Concept One/Two, Sequel, SPEED, Altus).
    <https://www.encyclopedia.com/books/politics-and-business-magazines/novellus-systems-inc>
[^chapple-sokol-1989]: J. D. Chapple-Sokol, E. Tierney and J. Batey,
    "RF Power Dependence of the Material Properties of PECVD Silicon
    Dioxide", *MRS Proceedings* **165** (1989).
    <https://doi.org/10.1557/PROC-165-113>
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
    tetraethylorthosilicate", *Journal of Vacuum Science & Technology B*
    **5**(6), 1555–1563 (1987). <https://doi.org/10.1116/1.583673>
[^philipossian-2009]: A. Philipossian and T. Sun, "Frictional Analysis
    of Various Poly(vinyl alcohol) Brush Roller Designs for
    Post-Interlevel Dielectric CMP Scrubbing Applications",
    *Electrochemical and Solid-State Letters* **12**(3), H84 (2009).
    <https://doi.org/10.1149/1.3058994>
[^wiki-teos]: Wikipedia, *Tetraethyl orthosilicate*.
    <https://en.wikipedia.org/wiki/Tetraethyl_orthosilicate>
[^wiki-pecvd]: Wikipedia, *Plasma-enhanced chemical vapor deposition*.
    <https://en.wikipedia.org/wiki/Plasma-enhanced_chemical_vapor_deposition>
[^txt-01]: J. D. Plummer, M. D. Deal and P. B. Griffin, *Silicon VLSI
    Technology: Fundamentals, Practice and Modeling*, Prentice Hall,
    2000, ISBN 978-0-13-085037-9.
    <https://openlibrary.org/isbn/9780130850379>
[^seshan-2012]: K. Seshan (ed.), *Handbook of Thin Film Deposition*,
    3rd ed., William Andrew, 2012, ISBN 978-1-4377-7873-1.
    <https://openlibrary.org/isbn/9781437778731>
[^nguyen-1999]: S. V. Nguyen, "High-density plasma chemical vapor
    deposition of silicon-based dielectric films for integrated
    circuits", *IBM Journal of Research and Development* **43**(1.2),
    109–126 (1999). <https://doi.org/10.1147/rd.431.0109>
[^lieberman-2005]: M. A. Lieberman and A. J. Lichtenberg, *Principles of
    Plasma Discharges and Materials Processing*, 2nd ed., Wiley, 2005,
    ISBN 978-0-471-72001-0. <https://doi.org/10.1002/0471724254>
