(masks-index)=
# Masks

A *mask level* is one pattern in the stack of patterns that builds an
integrated circuit. For each level a {term}`reticle` — a fused-silica
plate carrying a chromium image of one layer of the layout, drawn
larger than it will print on the wafer (4× is the ITRS 2001 mask
magnification for the 130 nm generation)[^wiki-mask][^itrs-03] — is
projected onto a photoresist-coated wafer. The developed resist then
serves as a stencil for an etch, or as a {term}`block mask` for an
implant, and is removed afterwards. The coat–expose–develop sequence,
its tools and its consumables are described on the
{ref}`Photolithography (mask step) <category-lithography>` category
page; this page is an index that ties each mask step of the flow to
what the open SKY130 process design kit publishes about the mask.

## What the PDK publishes

Four parts of the PDK documentation describe masks.

* **The mask table.** The *Masks* page renders `masks.csv`, a
  three-column table (`Mask`, `Acronym`, `Used in SKY130`) of 51 mask
  entries "found on 130nm processes at SkyWater"; "The masks which are
  used on the SKY130 technology node (that this PDK supports) are
  marked", with an `X`.[^pdk-05] Thirty-four entries carry the mark.
  Some acronyms appear more than once, as variants: `VIM2` three times
  ("Via 2-TNV", "Via 2-S8TM", "Via 2-PLM"), `MM3` three times
  ("Metal 3-TLM", "Metal 3-S8TM", "Metal 3-PLM") and `PDM` twice
  ("Pad (scribe protect)", "Pad (scribe unprotect)"), each with only
  one variant marked.[^pdk-05]
* **The GDS layer table.** The *Layers Reference* renders
  `gds_layers.csv`, which gives each layer's name, purpose, GDS
  layer:datatype and description.[^pdk-06] It has two kinds of entry
  that matter here. *Drawn* layers are what a designer draws — `nwell`
  64:20 "N-well region", `met1` 68:20 "Metal 1", and so on. Under the
  heading "Mask level data" it then lists 32 *mask-level* layers with
  purpose `mask` and datatype 0, whose names start with `c` and whose
  descriptions name a mask (`cfom` 23:0 "Field oxide mask", `cviam`
  40:0 "Via mask", …), followed by `drawing`, `mask add`, `mask drop`
  and `waffle drop` purposes for some of them.[^pdk-06] The periphery
  rules restrict these layers in a layout: "Shapes on maskAdd or
  maskDrop layers ("serifs") are allowed in core only" (x.9), and
  "Drawn compatible, mask, and waffle-drop layers are allowed only
  inside areaid:mt (i.e., etest modules)", the seal ring or the frame,
  with the exception that "FOM/P1M/Metal waffle drop are allowed
  inside the die" (x.15a).[^pdk-periph] The same page carries Table
  F2b, a "Mask Generation table" that marks device by device which
  mask levels are "CREATED" (`C`).[^pdk-06]
* **The minimum-CD table.** Table 2 of *Criteria & Assumptions*,
  "Minimum CDs in Design or on Wafer, required by Technology (Core or
  Periphery)", repeats most of the mask names of `masks.csv` with a
  feature size, a space size and a variable name for each (`VIMCD`,
  `VIMCDSP`, …).[^pdk-03] The table has no unit column; this page
  quotes the numbers as printed, which the step pages read as µm (the
  periphery rules give the same 0.150 µm and 0.170 µm for via 1 as
  `VIMCD` and `VIMCDSP`[^pdk-periph]). The table does not give a resist
  tone for any mask.
* **The design rules.** Each drawn layer's rule set in the periphery
  rules opens with a "Function" line, and a few notes name masks
  directly — for example "For SP8P\*/SKY130P\* (PLM) CADflow use MM4
  for Metal Fuse".[^pdk-periph]

What the PDK does *not* publish is a table that says which drawn
layers, combined by which operations, generate each mask. The pairing
of masks with drawn layers below is therefore made by correspondence
of names and descriptions across the files, and where it needs more
reasoning than that it is marked *(inference)* and explained on the
step page.

## Mask steps in this reference

The step list used in this reference ({ref}`steps-index`) contains 36
mask (lithography) steps, from {ref}`FOM <step-004>` to
{ref}`PDM <step-168>`. Each is followed by the etch, implant and strip
steps that use its resist pattern, before the next deposition,
oxidation or mask step. For 33 of the 36, the step code is identical
to an acronym in `masks.csv`, and that match is what the second column
reports; three mask steps have no entry.

In the table:

* **PDK mask** gives the `Mask` and `Acronym` fields of `masks.csv`
  exactly, and the `Used in SKY130` field as `X` or *blank*; *not
  listed* means no entry.[^pdk-05]
* **Mask-level layers** gives the `c…` layers of `gds_layers.csv`
  whose description names the mask, as name, purpose and
  layer:datatype.[^pdk-06]
* **Drawn layers** gives the drawn layer(s) of `gds_layers.csv` that
  correspond to the mask, as name and layer:datatype; the descriptions
  are on the step pages.[^pdk-06]
* **Patterns** lists the steps that, on this reference's step pages,
  use the resist pattern, with the strip step where the step list has
  a separate one. Where no strip step is listed, the step pages read
  the strip as part of the etch.
* **Minimum CD** gives the feature and space values and their variable
  names from Table 2 of *Criteria & Assumptions*.[^pdk-03]

| Step | PDK mask (`masks.csv`) | Mask-level layers (`gds_layers.csv`) | Drawn layers (`gds_layers.csv`) | Patterns | Minimum CD, feature / space |
|------|------------------------|--------------------------------------|---------------------------------|----------|-----------------------------|
| {ref}`FOM <step-004>` | Field Oxide, FOM — `X` | `cfom` mask 23:0; `cfom` drawing 22:20, mask add 22:21, mask drop 22:22, waffle drop 22:24; `fom` dummy 22:23 | `diff` 65:20 and `tap` 65:44 *(inference)* | {ref}`STINITE <step-005>`, {ref}`STIE <step-006>` | `FOMCD` 0.14 / `FOMCDSP` 0.27 |
| {ref}`DNM <step-007>` | Deep N-Well, DNM — `X` | `cdnm` mask 48:0 | `dnwell` 64:18 | {ref}`DNI <step-008>`; strip {ref}`DNIS <step-009>` | `DNMCD` 3 / `DNMCDSP` 6.3 |
| {ref}`LVTNM <step-014>` | Low Vt Nch\*, LVTNM — `X` | `clvtnm` mask 25:0; drawing 25:44, mask add 25:43, mask drop 25:42 | `lvtn` 125:44 | {ref}`LVTNI <step-015>`; strip {ref}`LVTNIS <step-016>` | `LVTNMCD` 0.38 / `LVTNMCDSP` 0.38 |
| {ref}`NWM <step-017>` | N-Well\*, NWM — `X` | `cnwm` mask 21:0 | `nwell` 64:20 | {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`; strip {ref}`LVTPIS <step-021>` | `NWMCD` 0.84 / `NWMCDSP` 1.27 |
| {ref}`HVTPM <step-022>` | High Vt PCh\*, HVTPM — `X` | `chvtpm` mask 97:0; drawing 88:44, mask add 97:43, mask drop 97:42 | `hvtp` 78:44 | {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`; strip {ref}`PCHIS <step-025>` | `HVTPMCD` 0.38 / `HVTPMCDSP` 0.38 |
| {ref}`PWBM <step-026>` | P-Well Block Mask, PWBM — *blank* | none | `pwbm` 19:44 | {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`; strip {ref}`PWIS <step-029>` | `PWBMCD` 0.84 / `PWBMCDSP` 1.27 |
| {ref}`PWDEM <step-030>` | P-Well Drain Extended, PWDEM — *blank* | none | `pwde` 124:20 | {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`; strip {ref}`PWDEIS <step-033>` | `PWDEMCD` 0.84 / `PWDEMCDSP` 1.27 |
| {ref}`TUNM <step-035>` | Tunnel Mask, TUNM — `X` | `ctunm` mask 20:0 | `tunm` 80:20 | {ref}`TUNARCE <step-036>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`TUNME <step-039>` | `TUNMCD` 0.41 / `TUNMCDSP` 0.5 |
| {ref}`ONOM <step-041>` | ONO Mask, ONOM — `X` | `conom` mask 88:0; drawing 87:44 | no drawn `onom` layer; from `tunm` 80:20 *(inference)* | {ref}`ONOME <step-042>` | `ONOMCD` 0.41 / `ONOMCDSP` 0.5 |
| {ref}`LVOM <step-044>` | Low Voltage Oxide, LVOM — `X` | `clvom` mask 46:0; drawing 45:20 | no drawn `lvom` layer; the complement of `hvi` 75:20 *(inference)* | {ref}`NCHI <step-045>`, {ref}`GOXETCH <step-046>` | `LVOMCD` 0.6 / `LVOMCDSPCSMC` 0.7 |
| {ref}`RPM <step-049>` | Resistor Protect, RPM — `X` | `crpm` mask 96:0 | `rpm` 86:20; `urpm` 79:20 *(inference)* | {ref}`P1I <step-050>`; strip {ref}`P1IS <step-051>` | `RPMCD` 1.27 / `RPMCDSP` 0.84 |
| {ref}`RRPM <step-052>` | *not listed* | none | `rpm` 86:20, alone or less `urpm` 79:20 *(inference)* | {ref}`PRI <step-053>`; strip {ref}`PRIS <step-054>` | none listed |
| {ref}`URPM <step-055>` | *not listed* | none | `urpm` 79:20 *(inference)* | {ref}`UPRI <step-056>`; strip {ref}`UPRIS <step-057>` | none listed |
| {ref}`P1M <step-061>` | Poly 1, P1M — `X` | `cp1m` mask 28:0; mask add 33:43, mask drop 33:42, waffle drop 33:24 | `poly` 66:20 (also purposes gate 66:9, resistor 66:13) | {ref}`P1ME <step-062>` | `P1MCD` N/A / `P1MCDSP` 0.14; "Endcap/Gap" `P1G` 0.15 / 0.21 |
| {ref}`NTM <step-064>` | N-tip Implant, NTM — `X` | `cntm` mask 27:0; drawing 26:20, mask add 26:21, mask drop 26:22 | no drawn `ntm` layer; derived from the device layers *(inference)* | {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`; strip {ref}`ASTIS <step-067>` | `NTMCD` 0.84 / `NTMCDSP` 0.7 |
| {ref}`HVNTM <step-068>` | High Volt. N-tip, HVNTM — `X` | `chvntm` mask 39:0; drawing 38:20 | `hvntm` 125:20 | {ref}`HVASTI <step-069>`; strip {ref}`HVASTIS <step-070>` | `HVNTMCD` 0.7 / `HVNTMCDSP` 0.7 |
| {ref}`LDNTM <step-071>` | Lightly Doped N-tip, LDNTM — `X` | `cldntm` mask 11:0 | `ldntm` 11:44 | {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`; strip {ref}`LDASTIS <step-074>` | `LDNTMCD` 0.7 / `LDNTMCDSP` 0.7 |
| {ref}`NPCM <step-078>` | Nitride Poly Cut, NPCM — `X` | `cnpc` mask 49:0; drawing 44:20 | `npc` 95:20 | {ref}`NPCME <step-079>` | `NPCMCD` 0.27 / `NPCMCDSP` 0.27 |
| {ref}`PSDM <step-081>` | P+ Implant, PSDM — `X` | `cpsdm` mask 32:0; drawing 31:20, mask add 31:21, mask drop 31:22 | `psdm` 94:20 | {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`; strip {ref}`PDIS <step-084>` | `PSDMCD` 0.38 / `PSDMCDSP` 0.38 |
| {ref}`NSDM <step-085>` | N+ Implant, NSDM — `X` | `cnsdm` mask 30:0; drawing 29:20, mask add 29:21, mask drop 29:22 | `nsdm` 93:44 | {ref}`NSDI <step-086>`; strip {ref}`NSDIS <step-087>` | `NSDMCD` 0.38 / `NSDMCDSP` 0.38 |
| {ref}`LICM1 <step-093>` | Local Intr Cont.1, LICM1 — `X` | `clicm1` mask 43:0; mask add 106:43, mask drop 106:42 | `licon1` 66:44 | {ref}`LICM1E <step-094>`, followed by {ref}`SACETCH <step-095>` | "Core" `LICM1CD` 0.19 / `LICM1CDSP` 0.35; "Slotted" `LICM1SLCD` 0.17 / `LICM1SLCDSP` 0.17 |
| {ref}`LI1M <step-102>` | Local Intrcnct 1, LI1M — `X` | `cli1m` mask 56:0; drawing 115:44, mask add 115:43, mask drop 115:42 | `li1` 67:20 | {ref}`LI1ME <step-103>` | `LI1MCD` 0.17 / `LI1MCDSP` 0.17; "Core" 0.14 / 0.14 |
| {ref}`CTM1 <step-107>` | Contact, CTM1 — `X` | `ctm1` mask 35:0 | `mcon` 67:44 *(inference)* | {ref}`CTME <step-108>` | `CTM1CD` 0.17 / `CTM1CDSP` 0.19 |
| {ref}`MM1 <step-113>` | Metal 1, MM1 — `X` | `cmm1` mask 36:0; waffle drop 62:24 | `met1` 68:20 | {ref}`MM1E <step-114>` | `MM1CD` 0.14 / `MM1CDSP` 0.14 |
| {ref}`VIM <step-118>` | Via, VIM — `X` | `cviam` mask 40:0 | `via` 68:44 | {ref}`VIME <step-119>` | `VIMCD` 0.15 / `VIMCDSP` 0.17 |
| {ref}`MM2 <step-124>` | Metal 2, MM2 — `X` | `cmm2` mask 41:0; waffle drop 105:52 | `met2` 69:20 | {ref}`MM2E <step-125>` | `MM2CD` 0.14 / `MM2CDSP` 0.14 |
| {ref}`VIM2 <step-129>` | Via 2-PLM, VIM2 — `X`; Via 2-TNV, VIM2 — *blank*; Via 2-S8TM, VIM2 — *blank* | `cviam2` mask 44:0 | `via2` 69:44 | {ref}`VIM2E <step-130>` | `VIM2CD` / `VIM2CDSP`: "Via 2-PLM" 0.2 / 0.2; "Via 2-TNV" 0.28 / 0.28; "Via 2-S8TM" 0.8 / 0.8 |
| {ref}`CAPM <step-137>` | Capacitor MiM, CAPM — *blank* | none | `capm` 89:44 | {ref}`CAPME <step-138>` | `CAPMCD` 2 / `CAPMCDSP` 0.84 |
| {ref}`MM3 <step-139>` | Metal 3-PLM, MM3 — `X`; Metal 3-TLM, MM3 — *blank*; Metal 3-S8TM, MM3 — *blank* | `cmm3` mask 34:0; waffle drop 107:24 | `met3` 70:20 | {ref}`MM3E <step-140>` | `MM3CD` / `MM3CDSP`: "Metal 3-PLM" 0.3 / 0.3; "Metal 3-TLM" 0.36 / 0.36; "Metal 3-S8TM" 0.8 / 0.8 |
| {ref}`VIM3 <step-144>` | Via3-PLM, VIM3 — `X` | `cviam3` mask 50:0; drawing 112:20 | `via3` 70:44 | {ref}`VIM3E <step-145>` | `VIM3CD` 0.2 / `VIM3CDSP` 0.2 |
| {ref}`CAP2M <step-152>` | *not listed* | none | `cap2m` 97:44 *(inference)* | {ref}`CAP2ME <step-153>` | none listed |
| {ref}`MM4 <step-154>` | Metal 4, MM4 — `X` | `cmm4` mask 51:0; waffle drop 112:4 | `met4` 71:20; `met4` fuse 71:17 (the metal-fuse note names MM4) | {ref}`MM4E <step-155>` | `MM4CD` 0.3 / `MM4CDSP` 0.3 |
| {ref}`VIM4 <step-159>` | Via4, VIM4 — `X` | `cviam4` mask 58:0; drawing 117:20 | `via4` 71:44 | {ref}`VIM4E <step-160>` | `VIM4CD` 0.8 / `VIM4CDSP` 0.8 |
| {ref}`MM5 <step-162>` | Metal 5, MM5 — `X` | `cmm5` mask 59:0; waffle drop 117:4 | `met5` 72:20 | {ref}`MM5E <step-163>` | `MM5CD` / `MM5CDSP`: "All flows except S8PF\*/S8PIR\*" 0.8 / 0.8; "S8PF\*/S8PIR\*" 1.6 / 1.6 |
| {ref}`NSM <step-165>` | Nitride Seal Mask, NSM — `X` | `cnsm` mask 22:0 | `nsm` 61:20 | {ref}`NSME <step-166>` | `NSMCD` 3 / `NSMCDSP` 4 |
| {ref}`PDM <step-168>` | Pad (scribe protect), PDM — `X`; Pad (scribe unprotect), PDM — *blank* | `cpdm` mask 37:0 | `pad` 76:20 | {ref}`PDME <step-169>` | "Pad (scribe protect)" `PDMCD` 2 / `PDMCDSP` 1.27 |

Notes on the table:

* **Mask-level layer descriptions.** Each `c…` layer with purpose
  `mask` repeats the mask's name in its description, for example
  `cdnm` "Deep nwell mask", `chvtpm` "High Vt Pch mask", `ctm1`
  "Contact mask", `cviam4` "Via 4 mask", `cpdm` "Pad mask".[^pdk-06]
  The `drawing`, `mask add`, `mask drop` and `waffle drop` purposes of
  a mask-level layer do not always share its layer number: `cfom` is
  23:0 as a mask but 22:20, 22:21, 22:22 and 22:24 otherwise, `cp1m`
  28:0 against 33:x,
  `cli1m` 56:0 against 115:x.[^pdk-06]
* **Shared layer numbers.** Several GDS layer numbers carry unrelated
  layers under different datatypes, which is worth knowing when
  reading the table: 22 (`cnsm` 22:0 and the `cfom` purposes), 44
  (`cviam2` 44:0, `cnpc` drawing 44:20, `pwelliso` label 44:5), 88
  (`conom` 88:0, `chvtpm` drawing 88:44), 96 (`crpm` 96:0, `cncm`
  drawing 96:44), 97 (`chvtpm` 97:0/42/43, `cap2m` 97:44), 112
  (`cviam3` drawing 112:20, `cmm4` waffle drop 112:4) and 117
  (`cviam4` drawing 117:20, `cmm5` waffle drop 117:4).[^pdk-06]
* **The "(inference)" entries.** `FOM` is paired with the active
  layers `diff` and `tap` on its step page; `ONOM` with `tunm`
  oversized; `LVOM` with the complement of the thick-oxide layer
  `hvi`, since designers draw `hvi` rather than `lvom`; `NTM` with a
  Boolean combination of the device layers, since there is no drawn
  `ntm`; `CTM1` with `mcon`, "Contact from local interconnect to
  metal1", because `licon1` corresponds to `LICM1`; `RPM` with `urpm`
  as well as `rpm`; and `RRPM`, `URPM` and `CAP2M`, which have no
  `masks.csv` entry, with `rpm`, `urpm` and `cap2m` on the readings of
  their step pages.[^pdk-06] The metal-fuse pairing for `MM4` is not an
  inference: the metal-fuse rules say "For SP8P\*/SKY130P\* (PLM) CADflow
  use MM4 for Metal Fuse".[^pdk-periph]
* **Waffle drop.** `waffle drop` purposes exist for `cfom`, `cp1m` and
  `cmm1`–`cmm5`,[^pdk-06] the levels that x.15a allows to carry
  waffle-drop shapes inside the die;[^pdk-periph] the
  {ref}`FOM <step-004>` page reads the "waffles" as dummy fill for
  {term}`CMP` uniformity.
* **Variants.** For `VIM2`, `MM3` and `PDM`, the row for this
  reference's step is the variant marked `X`; the {ref}`VIM2 <step-129>` and
  {ref}`MM3 <step-139>` step pages discuss the unmarked variants.

<!-- footnotes -->

[^wiki-mask]: Wikipedia, *Photomask*.
    <https://en.wikipedia.org/wiki/Photomask>
[^itrs-03]: International Technology Roadmap for Semiconductors, *2001
    Edition: Lithography*.
    <https://www.semiconductors.org/wp-content/uploads/2018/08/2001Litho.pdf>
[^pdk-05]: SkyWater PDK Authors, *Masks* page and `masks.csv`, SkyWater
    SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/masks.html>,
    <https://github.com/google/skywater-pdk/blob/main/docs/rules/masks.csv>
[^pdk-06]: SkyWater PDK Authors, *Layers Reference* and
    `gds_layers.csv`, SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/layers.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/gds_layers.csv>
[^pdk-03]: SkyWater PDK Authors, *Criteria & Assumptions*, SkyWater
    SKY130 PDK documentation (Table 2, `assumptions/02-mins.csv`).
    <https://skywater-pdk.readthedocs.io/en/main/rules/assumptions.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/assumptions/02-mins.csv>
[^pdk-periph]: SkyWater PDK Authors, *Periphery rules*, SkyWater SKY130
    PDK documentation. <https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html>
