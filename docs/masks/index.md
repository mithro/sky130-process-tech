(masks-index)=
# Masks

A *mask level* is one pattern in the stack of patterns that builds an
integrated circuit. For each level a {term}`reticle` — a fused-silica
plate carrying a chromium image of one layer of the layout, drawn
four or five times larger than it will print on the wafer[^wiki-mask]
(4× is the ITRS 2001 mask magnification for the 130 nm
generation;[^itrs-03] the two Photronics plate-case labels transcribed
in the process-steps sheet carry "4X" in their type field, although
the tab does not say which process or run they belong to,[^steps-sheet]
and we read the sheet's mask-type codes for the via 2, via 3 and via 4 plates as 4×
too[^steps-sheet]) —
is projected onto a photoresist-coated wafer.
The developed resist then serves as a stencil for an etch, or as a
{term}`block mask` for an implant, and is removed afterwards. The
coat–expose–develop sequence, its tools and its consumables are
described on the
{ref}`Photolithography (mask step) <category-lithography>` category
page; this page is an index that ties each mask step of the step list
used in this reference to what the open SKY130 process design kit
publishes about the mask, to the plates that the process-steps
sheet records for the MPW runs ({ref}`masks-mpw-runs`), and to what
public renders of those runs' tape-out layouts show
({ref}`masks-renders`).

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
  `VIMCD` and `VIMCDSP`[^pdk-periph]). The pad documentation of the
  SKY130 {term}`test tile` uses several of the values: gate-oxide
  capacitors drawn at "FOM w/s = 0.14/0.27" (`FOMCD` / `FOMCDSP`),
  N-well isolation structures that include "Nwell to Nwell Space =
  1.27um" (`NWMCDSP`), and metal-5 test lines 1.6 µm wide labelled
  "S8PIR/PF" (the "S8PF\*/S8PIR\*" row of `MM5CD` /
  `MM5CDSP`).[^raw-data-testtile-pads] The table does not give a resist
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
step page. The one operation the PDK does state is for `hvntm`: "Drawn
layer will be OR-ed with the CL and rechecked for CLDRC".[^pdk-periph]
The PDK does not expand "CL"; the {ref}`HVNTM <step-068>` page reads it
as a computed layer.

## Mask steps in this reference

The step list used in this reference ({ref}`steps-index`) contains 36
mask (lithography) steps, from {ref}`FOM <step-004>` to
{ref}`PDM <step-168>`. Each is followed by the etch, implant and strip
steps that use its resist pattern, before the next deposition,
oxidation, anneal or mask step. For 33 of the 36, the step code is
identical to an acronym in `masks.csv`, and that match is what the
second column reports; three mask steps have no entry. The
process-steps sheet's "Masks" tab lists the same 36 steps and also
step 82, {ref}`PSDI <step-082>`, which the step list names as an
implant ({ref}`masks-mpw-runs`).[^steps-sheet]

Per-mask pages bring together, for one mask, its PDK entry and layers,
its plates, its renders, the lithography it needs, the steps that use it
and its design rules; where a page exists, the acronym in the table's
second column links to it.

```{toctree}
:maxdepth: 1

dnm
p1m
licm1
vim4
```

In the table:

* **PDK mask** gives the `Mask` and `Acronym` fields of `masks.csv`
  exactly, and the `Used in SKY130` field as `X` or *blank*; *not
  listed* means no entry.[^pdk-05]
* **Mask-level layers** gives the `c…` layers of `gds_layers.csv`
  whose description names the mask, as name, purpose and
  layer:datatype (and, for FOM, the `fom` dummy purpose).[^pdk-06]
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
| {ref}`DNM <step-007>` | Deep N-Well, {ref}`DNM <mask-dnm>` — `X` | `cdnm` mask 48:0 | `dnwell` 64:18 | {ref}`DNI <step-008>`; strip {ref}`DNIS <step-009>` | `DNMCD` 3 / `DNMCDSP` 6.3 |
| {ref}`LVTNM <step-014>` | Low Vt Nch\*, LVTNM — `X` | `clvtnm` mask 25:0; drawing 25:44, mask add 25:43, mask drop 25:42 | `lvtn` 125:44 | {ref}`LVTNI <step-015>`; strip {ref}`LVTNIS <step-016>` | `LVTNMCD` 0.38 / `LVTNMCDSP` 0.38 |
| {ref}`NWM <step-017>` | N-Well\*, NWM — `X` | `cnwm` mask 21:0 | `nwell` 64:20 | {ref}`NWI <step-018>`, {ref}`NWI2 <step-019>`, {ref}`LVTPI <step-020>`; strip {ref}`LVTPIS <step-021>` | `NWMCD` 0.84 / `NWMCDSP` 1.27 |
| {ref}`HVTPM <step-022>` | High Vt PCh\*, HVTPM — `X` | `chvtpm` mask 97:0; drawing 88:44, mask add 97:43, mask drop 97:42 | `hvtp` 78:44 | {ref}`PCHI <step-023>`, {ref}`PNCHI <step-024>`; strip {ref}`PCHIS <step-025>` | `HVTPMCD` 0.38 / `HVTPMCDSP` 0.38 |
| {ref}`PWBM <step-026>` | P-Well Block Mask, PWBM — *blank* | none | `pwbm` 19:44 with `nwell` 64:20 *(inference)* | {ref}`PWI <step-027>`, {ref}`PWI2 <step-028>`; strip {ref}`PWIS <step-029>` | `PWBMCD` 0.84 / `PWBMCDSP` 1.27 |
| {ref}`PWDEM <step-030>` | P-Well Drain Extended, PWDEM — *blank* | none | `pwde` 124:20 | {ref}`PWDEI1 <step-031>`, {ref}`PWDEI2 <step-032>`; strip {ref}`PWDEIS <step-033>` | `PWDEMCD` 0.84 / `PWDEMCDSP` 1.27 |
| {ref}`TUNM <step-035>` | Tunnel Mask, TUNM — `X` | `ctunm` mask 20:0 | `tunm` 80:20 | {ref}`TUNARCE <step-036>`, {ref}`PTSI <step-037>`, {ref}`DEPI <step-038>`, {ref}`TUNME <step-039>` | `TUNMCD` 0.41 / `TUNMCDSP` 0.5 |
| {ref}`ONOM <step-041>` | ONO Mask, ONOM — `X` | `conom` mask 88:0; drawing 87:44 | no drawn `onom` layer; from `tunm` 80:20 *(inference)* | {ref}`ONOME <step-042>` | `ONOMCD` 0.41 / `ONOMCDSP` 0.5 |
| {ref}`LVOM <step-044>` | Low Voltage Oxide, LVOM — `X` | `clvom` mask 46:0; drawing 45:20 | no drawn `lvom` layer; the complement of `hvi` 75:20 *(inference)* | {ref}`NCHI <step-045>`, {ref}`GOXETCH <step-046>` | `LVOMCD` 0.6 / `LVOMCDSPCSMC` 0.7 |
| {ref}`RPM <step-049>` | Resistor Protect, RPM — `X` | `crpm` mask 96:0 | `rpm` 86:20; `urpm` 79:20 *(inference)* | {ref}`P1I <step-050>`; strip {ref}`P1IS <step-051>` | `RPMCD` 1.27 / `RPMCDSP` 0.84 |
| {ref}`RRPM <step-052>` | *not listed* | none | `rpm` 86:20, alone or less `urpm` 79:20 *(inference)* | {ref}`PRI <step-053>`; strip {ref}`PRIS <step-054>` | none listed |
| {ref}`URPM <step-055>` | *not listed* | none | `urpm` 79:20 *(inference)* | {ref}`UPRI <step-056>`; strip {ref}`UPRIS <step-057>` | none listed |
| {ref}`P1M <step-061>` | Poly 1, {ref}`P1M <mask-p1m>` — `X` | `cp1m` mask 28:0; mask add 33:43, mask drop 33:42, waffle drop 33:24 | `poly` 66:20 (also purposes gate 66:9, resistor 66:13) | {ref}`P1ME <step-062>` | `P1MCD` N/A / `P1MCDSP` 0.14; "Endcap/Gap" `P1G` 0.15 / 0.21 |
| {ref}`NTM <step-064>` | N-tip Implant, NTM — `X` | `cntm` mask 27:0; drawing 26:20, mask add 26:21, mask drop 26:22 | no drawn `ntm` layer; derived from the device layers *(inference)* | {ref}`ASTI <step-065>`, {ref}`BHI <step-066>`; strip {ref}`ASTIS <step-067>` | `NTMCD` 0.84 / `NTMCDSP` 0.7 |
| {ref}`HVNTM <step-068>` | High Volt. N-tip, HVNTM — `X` | `chvntm` mask 39:0; drawing 38:20 | `hvntm` 125:20, "OR-ed with the CL" (the `hvntm` rules)[^pdk-periph] | {ref}`HVASTI <step-069>`; strip {ref}`HVASTIS <step-070>` | `HVNTMCD` 0.7 / `HVNTMCDSP` 0.7 |
| {ref}`LDNTM <step-071>` | Lightly Doped N-tip, LDNTM — `X` | `cldntm` mask 11:0 | `ldntm` 11:44 | {ref}`LDASTI <step-072>`, {ref}`LDBHI <step-073>`; strip {ref}`LDASTIS <step-074>` | `LDNTMCD` 0.7 / `LDNTMCDSP` 0.7 |
| {ref}`NPCM <step-078>` | Nitride Poly Cut, NPCM — `X` | `cnpc` mask 49:0; drawing 44:20 | `npc` 95:20 | {ref}`NPCME <step-079>` | `NPCMCD` 0.27 / `NPCMCDSP` 0.27 |
| {ref}`PSDM <step-081>` | P+ Implant, PSDM — `X` | `cpsdm` mask 32:0; drawing 31:20, mask add 31:21, mask drop 31:22 | `psdm` 94:20 | {ref}`PSDI <step-082>`, {ref}`2PSDI <step-083>`; strip {ref}`PDIS <step-084>` | `PSDMCD` 0.38 / `PSDMCDSP` 0.38 |
| {ref}`NSDM <step-085>` | N+ Implant, NSDM — `X` | `cnsdm` mask 30:0; drawing 29:20, mask add 29:21, mask drop 29:22 | `nsdm` 93:44 | {ref}`NSDI <step-086>`; strip {ref}`NSDIS <step-087>` | `NSDMCD` 0.38 / `NSDMCDSP` 0.38 |
| {ref}`LICM1 <step-093>` | Local Intr Cont.1, {ref}`LICM1 <mask-licm1>` — `X` | `clicm1` mask 43:0; mask add 106:43, mask drop 106:42 | `licon1` 66:44 | {ref}`LICM1E <step-094>`, followed by {ref}`SACETCH <step-095>` | "Core" `LICM1CD` 0.19 / `LICM1CDSP` 0.35; "Slotted" `LICM1SLCD` 0.17 / `LICM1SLCDSP` 0.17 |
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
| {ref}`VIM4 <step-159>` | Via4, {ref}`VIM4 <mask-vim4>` — `X` | `cviam4` mask 58:0; drawing 117:20 | `via4` 71:44 | {ref}`VIM4E <step-160>` | `VIM4CD` 0.8 / `VIM4CDSP` 0.8 |
| {ref}`MM5 <step-162>` | Metal 5, MM5 — `X` | `cmm5` mask 59:0; waffle drop 117:4 | `met5` 72:20 | {ref}`MM5E <step-163>` | `MM5CD` / `MM5CDSP`: "All flows except S8PF\*/S8PIR\*" 0.8 / 0.8; "S8PF\*/S8PIR\*" 1.6 / 1.6 |
| {ref}`NSM <step-165>` | Nitride Seal Mask, NSM — `X` | `cnsm` mask 22:0 | `nsm` 61:20 | {ref}`NSME <step-166>` | `NSMCD` 3 / `NSMCDSP` 4 |
| {ref}`PDM <step-168>` | Pad (scribe protect), PDM — `X`; Pad (scribe unprotect), PDM — *blank* | `cpdm` mask 37:0 | `pad` 76:20 | {ref}`PDME <step-169>` | "Pad (scribe protect)" `PDMCD` 2 / `PDMCDSP` 1.27 |

Notes on the table:

* **Mask-level layer descriptions.** Each `c…` layer with purpose
  `mask` repeats the mask's name in its description, for example
  `cdnm` "Deep nwell mask", `chvtpm` "High Vt Pch mask", `ctm1`
  "Contact mask", `cviam4` "Via 4 mask", `cpdm` "Pad mask".[^pdk-06]
  The `drawing`, `mask add`, `mask drop` and `waffle drop` purposes of
  a mask-level layer rarely share its layer number — only `clvtnm`
  (25:x) and the `chvtpm` mask add/drop (97:42/43) do: `cfom` is 23:0
  as a mask but 22:20, 22:21, 22:22 and 22:24 otherwise, `cp1m` 28:0
  against 33:x, `cli1m` 56:0 against 115:x.[^pdk-06]
* **Shared layer numbers.** Several GDS layer numbers carry unrelated
  layers under different datatypes, which is worth knowing when
  reading the table: 22 (`cnsm` 22:0 and the `cfom` purposes), 44
  (`cviam2` 44:0, `cnpc` drawing 44:20, `pwelliso` label 44:5), 88
  (`conom` 88:0, `chvtpm` drawing 88:44), 96 (`crpm` 96:0, `cncm`
  drawing 96:44), 97 (`chvtpm` 97:0/42/43, `cap2m` 97:44), 112
  (`cviam3` drawing 112:20, `cmm4` waffle drop 112:4), 117
  (`cviam4` drawing 117:20, `cmm5` waffle drop 117:4) and 125
  (`hvntm` 125:20, `lvtn` 125:44).[^pdk-06]
* **The "(inference)" entries.** `FOM` is paired with the active
  layers `diff` and `tap` on its step page; `PWBM` with `nwell` as
  well as `pwbm`, since `gds_layers.csv` has no drawn P-well layer;
  `ONOM` with `tunm` oversized; `LVOM` with the complement of the
  thick-oxide layer `hvi`, since designers draw `hvi` rather than
  `lvom`; `NTM` with a Boolean combination of the device layers, since
  there is no drawn `ntm`; `CTM1` with `mcon`, "Contact from local
  interconnect to metal1", because `licon1` corresponds to `LICM1`;
  `RPM` with `urpm` as well as `rpm`; and `RRPM`, `URPM` and `CAP2M`, which have no
  `masks.csv` entry, with `rpm`, `urpm` and `cap2m` on the readings of
  their step pages.[^pdk-06] The process-steps sheet records plates for
  all three on all eight MPW runs ({ref}`masks-mpw-runs`),[^steps-sheet]
  but it does not name drawn layers, so those pairings remain
  inferences. The metal-fuse entry for `MM4` rests on
  rule x.11, "Metal fuses are drawn in met4" (the other two x.11 rows
  name `met2` and `met3`), and the note "For SP8P\*/SKY130P\* (PLM)
  CADflow use MM4 for Metal Fuse";[^pdk-periph]
  the {ref}`MM4 <step-154>` page reads the fuse links as printed by
  this mask (inference from the note). One public derivation from the
  MPW layouts differs from several of these pairings, and from the
  `HVTPM` and `LVTNM` rows; see {ref}`masks-derivations`.
* **Waffle drop.** `waffle drop` purposes exist for `cfom`, `cp1m` and
  `cmm1`–`cmm5`,[^pdk-06] the levels that x.15a allows to carry
  waffle-drop shapes inside the die;[^pdk-periph] the
  {ref}`FOM <step-004>` page reads the "waffles" as dummy fill for
  {term}`CMP` uniformity.
* **Variants.** For `VIM2`, `MM3` and `PDM`, the row for this
  reference's step is the variant marked `X`, which is also the only
  variant for which the process-steps sheet records plates;[^steps-sheet]
  the
  {ref}`VIM2 <step-129>` and {ref}`MM3 <step-139>` step pages discuss
  the unmarked variants.

## PDK masks and mask steps that do not correspond

Comparing the two lists leaves entries on each side without a partner.
The tables below record them with what the PDK says about each.

### Marked in `masks.csv`, with no mask step in this reference

Four of the 34 marked entries have no mask step in the step list used
in this reference, which ends with the pad mask, pad etch, alloy and
electrical test ({ref}`PDM <step-168>` to {ref}`HPETEST <step-171>`)
and contains no polyimide, redistribution or bump steps. The
process-steps sheet records no plate for any of the four on MPW-1 to
MPW-8 ({ref}`masks-mpw-runs`).[^steps-sheet]

| `masks.csv` entry | Mask-level layer (`gds_layers.csv`) | Drawn layer (`gds_layers.csv`) | Minimum CD, feature / space | Other PDK data |
|-------------------|-------------------------------------|--------------------------------|-----------------------------|----------------|
| HLow VT PCh Radio\*, HVTRM — `X` | `chvtrm` mask 98:0 | `hvtr` 18:20 | `HVTRMCD` 0.38 / `HVTRMCDSP` 0.38 | Layer descriptions "HLow VT PCh Radio mask" (`chvtrm`) and "High-Vt RF transistor implant" (`hvtr`); the `hvtr` rule set's function line reads "Define low VT adjust implant region for pmedlvtrf". The {ref}`HVTPM <step-022>` page lists the absence of a step as an open question. |
| DECA PBO, PBO — `X` | none | none | `PBOCD` 10 / `PBOCDSP` 10 | The WLCSP rules' DECA table has a `cpbo` rule set, "1st polyimide (mask)", whose function is "Opens over the pad openings; Allows RDL layer to connect to top metal". |
| Cu Inductor/Redist., CU1M — `X` | none | none | `CU1MCD` 20 / `CU1MCDSP` 20 | The periphery rules' `rdl` rule set: "Defines the Cu Inductor. Connects to met5 through the pad opening"; the DECA table's `rdl` "connects the top metal from the customer to the bumps". Table F2b has a CU1M column. |
| Polyimide 2 (2), PMM2 — `X` | none | none | none listed | The DECA table's `cpmm2` rule set, "2nd polyimide", describes a via between the redistribution layer and the under-bump metal. |

### Mask steps in this reference without a marked `masks.csv` entry

Six of the 36 mask steps have no marked entry: three are listed with
the `Used in SKY130` field blank, and three are not listed at all.
None of the six has a mask-level (`c…`) layer in
`gds_layers.csv`.[^pdk-05][^pdk-06] The process-steps sheet
nevertheless records plates for `RRPM`, `URPM`, `CAPM` and `CAP2M` on
all eight MPW runs, for `PWBM` on MPW-6 and MPW-8, and for `PWDEM` on
MPW-6 ({ref}`masks-mpw-runs`).[^steps-sheet]

| Step | `masks.csv` | Drawn layer (`gds_layers.csv`) | Minimum CD, feature / space | Other PDK data |
|------|-------------|--------------------------------|-----------------------------|----------------|
| {ref}`PWBM <step-026>` | P-Well Block Mask, PWBM — *blank* | `pwbm` 19:44 with `nwell` 64:20 *(inference)* | `PWBMCD` 0.84 / `PWBMCDSP` 1.27 | The periphery rules have a `pwbm` rule set, "Define p-well block"; Table F2b has a PWBM column, marked `C` in, among others, the UHV 5/20 V drain-extended device rows. The step page treats the blank field as a documentation inconsistency. |
| {ref}`PWDEM <step-030>` | P-Well Drain Extended, PWDEM — *blank* | `pwde` 124:20 | `PWDEMCD` 0.84 / `PWDEMCDSP` 1.27 | The periphery rules have a `pwdem` rule set; Table F2b has a PWDEM column, marked `C` in the "UHV pmos 5/20V DE" row. The step page treats the blank as a documentation inconsistency. |
| {ref}`CAPM <step-137>` | Capacitor MiM, CAPM — *blank* | `capm` 89:44 | `CAPMCD` 2 / `CAPMCDSP` 0.84 | The periphery rules have a `capm` rule set, "Defines MIM capacitor", with values shown as "N/A"; Table F2b has a CAPM column, marked `C` in the "MiM" row. The test tile's pad documentation describes its MiM capacitors as "CAPM on M3".[^raw-data-testtile-pads] |
| {ref}`RRPM <step-052>` | *not listed* | `rpm` 86:20 *(inference)* | none listed | No separate rule set or Table F2b column. The test tile's pad documentation names the mask: its shortest 0.33 µm- and 0.69 µm-wide 300 Ω/sq poly resistors are marked "(will not work for any routes using RRPM mask)".[^raw-data-testtile-pads] |
| {ref}`URPM <step-055>` | *not listed* | `urpm` 79:20 *(inference)* | none listed | No separate rule set or Table F2b column. The test tile's pad documentation names the mask: the 2 kΩ/sq equivalents of those resistors are marked "(may not work for routes using URPM mask)".[^raw-data-testtile-pads] |
| {ref}`CAP2M <step-152>` | *not listed* | `cap2m` 97:44 *(inference)* | none listed | No `cap2m` rule set or Table F2b column; the MiM device page lists "CAP2M over Metal-4" beside "CAPM over Metal-3" and calls the constructions "identical";[^pdk-07] the test tile's pad documentation has "CAP2M over M4".[^raw-data-testtile-pads] |

The sources for both tables are `masks.csv`,[^pdk-05] `gds_layers.csv`
and Table F2b,[^pdk-06] the minimum-CD table,[^pdk-03] the periphery
rules,[^pdk-periph] the WLCSP rules,[^pdk-wlcsp] the *Device
Details* page[^pdk-07] and the test tile's pad
documentation.[^raw-data-testtile-pads]

### Unmarked `masks.csv` entries with no mask step

For completeness, nine acronyms appear in `masks.csv` only with the
`Used in SKY130` field blank and have no mask step in this reference,
and the process-steps sheet records no plate for any of them on the MPW
runs;[^steps-sheet] the unmarked variants of `VIM2`, `MM3` and `PDM`
are in the main table.

| `masks.csv` entry | Mask-level and drawn layers (`gds_layers.csv`) | Minimum CD, feature / space |
|-------------------|------------------------------------------------|-----------------------------|
| N-Core Implant, NCM — *blank* | `cncm` mask 17:0, drawing 96:44; `ncm` 92:44 | `NCMCD` 0.38 / `NCMCDSP` 0.38 |
| Open Frame Mask, OFM — *blank* | none | `OFMCD` N/A / `OFMCDSP` N/A |
| Pad Via, VIPDM — *blank* | none | `VIPDMCD` 1.2 / `VIPDMCDSP` 1.27 |
| Inductor-TLM, INDM — *blank* | none | `INDMCD` 2.5 / `INDMCDSP` 2.5 |
| Polyimide, PMM — *blank* | none | `PMMCD` 5 / `PMMCDSP` 15 |
| Polyimide_ExtFab, PMM[E] — *blank* | none | `PMM[E]CD` 5 / `PMM[E]CDSP` 15 |
| Pad&Polyimide_ExtFab, PDMM[E] — *blank* | none | none listed |
| Under Bump Metal, UBM — *blank* | none | none listed |
| Bumps, BUMP — *blank* | none | none listed |

`NCM` is the only one of the nine with layers in `gds_layers.csv`; its
rule set's function is "Define Vt adjust implant region for LV NMOS in
the core of NVSRAM".[^pdk-periph] `INDM` has no layers, but the
periphery rules have an `indm` rule set whose function line begins
"Defines third level of metal interconnects, buses and
inductor".[^pdk-periph] With `chvtrm`, `cncm` is one of the
two mask-level layers that have no mask step in this
reference.[^pdk-06] The {ref}`VIM4 <step-159>` page discusses the
"Pad Via, VIPDM" entry.

(masks-mpw-runs)=
## Plates recorded for the MPW runs

The *S8 / SKY130 Process Steps* sheet, from which the step list used in
this reference is taken, has a tab "Run Mask IDs" that sets a mask
table against eight runs it labels MPW-1 to MPW-8. Its rows are the 51
entries of `masks.csv`, with the same names, acronyms and `Used in
SKY130` marks, plus five rows the PDK table does not have: "Rev
Resistor Protect, RRPM", "Ultra-High Resistor Poly, URPM", "Capacitor
MiM 2, CAP2M", "RRAM Mask, RRM" and "Via 1 top, RRAM tier,
VIMC".[^steps-sheet][^pdk-05] Each run has an "Exists" column, marked
`X` where the sheet records a plate for that mask on that run, and a
"Plate ID" column.[^steps-sheet]

(masks-mpw-reticle-sets)=
### Runs, reticle sets and plate IDs

The tab heads each run's columns with an identifier. The public
mask-layer renders site ({ref}`masks-renders`) calls the same kind of
identifier the run's "Reticle set" and gives the same one as the sheet
for every run except MPW-4 (below); it adds a fab lot for five runs,
how confidently it has identified each set, and a project count for
each shuttle.[^steps-sheet][^mask-renders]

| Run | Sheet column heading (reticle set) | Fab lot (site) | Identification (site) | Projects (site) | Run page (site) |
|-----|------------------------------------|----------------|-----------------------|-----------------|-----------------|
| MPW-1 | `7CS8M06AC` | 4120787 | "likely" | 37 | `mpw-001.html` |
| MPW-2 | `5CS8007AC` | 4205819 | "confirmed" | 56 | `mpw-002.html` |
| MPW-3 | `5CS8008AC` | 4206521 | "confirmed" | 53 | `mpw-003.html` |
| MPW-4 | `5CS8018AC` | 4216266 | "confirmed" | 52 | `mpw-004.html` |
| MPW-5 | `5CS8011AC` | 4229389 | "confirmed" | 74 | `mpw-005.html` |
| MPW-6 | `5CS8014AC` | none given | "confirmed" | 85 | `mpw-006.html` |
| MPW-7 | `5CS8016AC` | none given | "inferred" | 106 | `mpw-007.html` |
| MPW-8 | `5CS8017AC` | none given | "inferred" | 144 | `mpw-008.html` |

* **MPW-4 has two sets.** The sheet heads its MPW-4 column `5CS8018AC`,
  and every MPW-4 plate ID in it has the prefix
  `S8018AA`.[^steps-sheet] The renders site's MPW-4 page is for the set
  `5CS8010AC` (fab lot 4216266), which it labels "SKY130 MPW-4
  (original)", and its MPW-7 and MPW-8 pages note "(8018 is the re-made
  MPW-4 set)".[^mask-renders] The renders are drawn from the MPW-4
  tape-out layouts; the plates in the sheet's MPW-4 column are those of
  `5CS8018AC`.
* **Identification.** For MPW-7 and MPW-8 the site infers the set from
  the numbering of the set before it ("Sequence after 5CS8014AC=MPW-6",
  "Sequence after 8016=MPW-7"); for the other six it gives lot records
  as its basis.[^mask-renders]
* **Projects and dies.** The project count is the site's figure for the
  shuttle; every reticle it renders carries 40 project dies, and it does
  not explain the difference (for MPW-1, 37 projects against 40
  dies).[^mask-renders]
* **Plate IDs.** Every plate ID in the tab is the run's prefix, a
  three-digit number and a final `A`, for example `S8M06AA020A` for
  the MPW-1 `FOM` plate. The prefix is the column heading with its first
  two characters dropped and its final `AC` replaced by `AA`. A mask's
  number is the same on every run for which a plate is recorded, with
  one exception: the MPW-6 `NSM` plate is `S8014AA616A`, where the
  other seven runs have `007`; 616 is higher than any other plate
  number in the tab, and the sheet does not explain the
  difference.[^steps-sheet] The tables below give that number as
  "Plate no.". The numbers do not follow process order —
  `NSM` (step 165) is `007`, `NWM` (step 17) `010`, `FOM` (step 4)
  `020`, `HVTPM` (step 22) `317`, and `CAPM` (step 137) `572` comes after
  `MM3` (step 139) `570` — and the sheet does not say what they encode,
  so this page reads no process position from them.[^steps-sheet]

### Plates by mask

The tables below report the "Exists" marks and plate numbers; *not
recorded* means no `X` on any of the eight runs. The last column gives,
from the renders ({ref}`masks-renders`), how many of the 40 rendered
dies of each run carry shapes on the layers the renders site uses for
the mask; the MPW-4 figures are for its original set
({ref}`masks-mpw-reticle-sets`).

| Step | `masks.csv` (`Used in SKY130`) | Plates recorded | Plate no. | Dies with shapes, MPW-1 to MPW-8 (renders) |
|------|--------------------------------|-----------------|-----------|----------|
| {ref}`FOM <step-004>` | `X` | all eight | `020` | 40 on every run |
| {ref}`DNM <step-007>` | `X` | all eight | `150` | 40 on every run |
| {ref}`LVTNM <step-014>` | `X` | all eight | `038` | 40 on every run |
| {ref}`NWM <step-017>` | `X` | all eight | `010` | 40 on every run |
| {ref}`HVTPM <step-022>` | `X` | all eight | `317` | 40 on every run |
| {ref}`PWBM <step-026>` | *blank* | MPW-6 and MPW-8 | `024` | 0 on every run |
| {ref}`PWDEM <step-030>` | *blank* | MPW-6 | `026` | 0 on every run |
| {ref}`TUNM <step-035>` | `X` | all eight | `190` | 1, 0, 0, 0, 1, 0, 0, 0 |
| {ref}`ONOM <step-041>` | `X` | all eight | `230` | 1, 0, 0, 0, 1, 0, 0, 0 |
| {ref}`LVOM <step-044>` | `X` | all eight | `125` | 40 on every run |
| {ref}`RPM <step-049>` | `X` | all eight | `175` | 1, 5, 0, 3, 4, 2, 3, 2 |
| {ref}`RRPM <step-052>` | *not listed* | all eight | `177` | not rendered |
| {ref}`URPM <step-055>` | *not listed* | all eight | `178` | 40 on every run |
| {ref}`P1M <step-061>` | `X` | all eight | `210` | 40 on every run |
| {ref}`NTM <step-064>` | `X` | all eight | `255` | 40 on every run |
| {ref}`HVNTM <step-068>` | `X` | all eight | `257` | 40 on every run |
| {ref}`LDNTM <step-071>` | `X` | all eight | `238` | 1, 0, 0, 0, 1, 0, 0, 0 |
| {ref}`NPCM <step-078>` | `X` | all eight | `180` | 40 on every run |
| {ref}`PSDM <step-081>` | `X` | all eight | `260` | 40 on every run |
| {ref}`NSDM <step-085>` | `X` | all eight | `250` | 40 on every run |
| {ref}`LICM1 <step-093>` | `X` | all eight | `265` | 40 on every run |
| {ref}`LI1M <step-102>` | `X` | all eight | `370` | 40 on every run |
| {ref}`CTM1 <step-107>` | `X` | all except MPW-5 | `400` | 40 on every run |
| {ref}`MM1 <step-113>` | `X` | all except MPW-5 | `450` | 40 on every run |
| {ref}`VIM <step-118>` | `X` | all except MPW-5 | `500` | 40 on every run |
| {ref}`MM2 <step-124>` | `X` | all eight | `550` | 40 on every run |
| {ref}`VIM2 <step-129>` | Via 2-PLM `X`; Via 2-TNV and Via 2-S8TM *blank* | Via 2-PLM: all eight; Via 2-TNV and Via 2-S8TM: not recorded | `560` | 40 on every run |
| {ref}`CAPM <step-137>` | *blank* | all eight | `572` | 39, 40, 40, 40, 40, 40, 40, 40 |
| {ref}`MM3 <step-139>` | Metal 3-PLM `X`; Metal 3-TLM and Metal 3-S8TM *blank* | Metal 3-PLM: all eight; Metal 3-TLM and Metal 3-S8TM: not recorded | `570` | 40 on every run |
| {ref}`VIM3 <step-144>` | `X` | all eight | `575` | 40 on every run |
| {ref}`CAP2M <step-152>` | *not listed* | all eight | `582` | 39, 40, 40, 40, 40, 40, 40, 40 |
| {ref}`MM4 <step-154>` | `X` | all eight | `580` | 40 on every run |
| {ref}`VIM4 <step-159>` | `X` | all except MPW-5 | `585` | 40 on every run |
| {ref}`MM5 <step-162>` | `X` | all eight | `590` | 40 on every run |
| {ref}`NSM <step-165>` | `X` | all eight | `007`; MPW-6: `616` | 39, 40, 40, 40, 40, 40, 40, 40 |
| {ref}`PDM <step-168>` | Pad (scribe protect) `X`; Pad (scribe unprotect) *blank* | scribe protect: all except MPW-5; scribe unprotect: not recorded | `600` | 40 on every run |

| Entry with no mask step in this reference | `masks.csv` (`Used in SKY130`) | Plates recorded | Plate no. | Dies with shapes, MPW-1 to MPW-8 (renders) |
|-------------------------------------------|--------------------------------|-----------------|-----------|----------|
| RRAM Mask, RRM | *not listed* | all except MPW-5 and MPW-6 | `430` | 0, 0, 0, 2, 0, 0, 6, 5 |
| Via 1 top, RRAM tier, VIMC | *not listed* | all except MPW-6 | `455` | 0, 0, 0, 2, 0, 0, 6, 5 |
| HVTRM | `X` | not recorded | — | 0 on every run |
| PBO, CU1M, PMM2 | `X` | not recorded | — | not rendered |
| NCM, VIPDM, INDM | *blank* | not recorded | — | 40 on every run (`VIPDM`, `INDM`: other masks' layers; `NCM`: `ncm` plus the `HVTPM` expression) |
| OFM, PMM, PMM[E], PDMM[E], UBM, BUMP | *blank* | not recorded | — | not rendered |

The source of both tables is the "Run Mask IDs" tab,[^steps-sheet] with
the `masks.csv` fields from the PDK[^pdk-05] and the die counts from the
renders' per-die metadata.[^mask-renders] What the record shows:

* **Masks the PDK table does not mark.** Plates are recorded on all
  eight runs for `RRPM`, `URPM` and `CAP2M`, which `masks.csv` does not
  list, and for `CAPM`, which it lists with the field
  blank.[^steps-sheet][^pdk-05] `PWBM`, also blank in `masks.csv`, has
  plates recorded only for MPW-6 and MPW-8, and `PWDEM` only for
  MPW-6.[^steps-sheet]
* **Masks with no plate on any run.** The sheet records no plate on
  any of the eight runs for the four marked entries without a mask
  step here — `HVTRM`, `PBO`, `CU1M` and `PMM2` — nor for the unmarked
  variants "Via 2-TNV", "Via 2-S8TM", "Metal 3-TLM", "Metal 3-S8TM" and
  "Pad (scribe unprotect)", nor for the nine unmarked entries without a
  mask step.[^steps-sheet][^pdk-05] Each of the other 30 marked entries
  has plates recorded on seven or eight runs.[^steps-sheet]
* **MPW-5.** The sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5 (nor for `RRM`), so MPW-5 has 30 `X` marks
  against 36 for each of MPW-1 to MPW-4, MPW-6 and MPW-7 and 37 for
  MPW-8.[^steps-sheet] The sheet gives no reason. This page reports
  what is recorded and does not conclude that those masks were absent
  from MPW-5: the gap may be in the record rather than in the run
  (inference: contact, metal 1, via 1, via 4 and pad masks are needed
  for any working die, so a gap in the record is the likelier
  explanation). The renders for `CTM1`, `MM1`, `VIM`, `VIM4` and `PDM`
  show shapes on all 40 rendered MPW-5 dies,[^mask-renders] which fits
  that reading but shows the drawn layouts, not the plates.
* **NSM on MPW-6.** Every run has an `NSM` plate; the MPW-6 plate
  number differs from the others ({ref}`masks-mpw-reticle-sets`).
* **The sky130B ReRAM masks.** `RRM` has plates recorded on MPW-1 to
  MPW-4, MPW-7 and MPW-8, and `VIMC` on MPW-1 to MPW-5, MPW-7 and MPW-8;
  neither has one on MPW-6.[^steps-sheet] The sheet's notes tie both to
  the ReRAM tier between metal 1 and metal 2 described on the
  {ref}`overview-sky130b-reram` page;[^steps-sheet] as that page notes,
  the notes use the PDK files' terms and are not independent evidence.
  Neither is a step in the step list used here or an entry in
  `masks.csv`, so neither appears in the main table of this
  page.[^steps-sheet][^pdk-05]
* **The "Masks" tab.** A further tab, "Masks", lists 37 rows of step
  number, code and description: the 36 mask steps counted above and
  step 82, `PSDI`, which it describes, like step 81 `PSDM`, as "P+
  source drain implant mask".[^steps-sheet] The step list itself calls
  step 82 "P+ source drain implant", and this reference treats it as
  the implant through the `PSDM` resist
  ({ref}`PSDI <step-082>`).[^steps-sheet]

### Mask types and plate labels

A tab headed "Sheet4" gives a coded mask type for three masks only:
`F4-248-EAPSM-A43-APRX` for `VIM2` and `VIM3`, and `B4-248-BIM-LSR-WET`
for `VIM4`.[^steps-sheet] We read the codes for the via 2 (`VIM2`) and
via 3 (`VIM3`) plates (`EAPSM`) as denoting embedded
{term}`attenuated phase-shift masks <attenuated PSM>` and the code for
the via 4 (`VIM4`) plate (`BIM`) as denoting a binary (chrome-on-quartz)
mask, in each case for 248 nm exposure (`248`): the codes use the
abbreviations mask makers and the patent literature use for these
types.[^photronics-abr][^pat-bim-tsmc] We also read the digit 4 after
the first letter of each code, less certainly, as the 4× reduction
ratio; the tab does not define its codes. The tab does not say to which
runs these types apply, and it gives no type for any other mask. The
{ref}`VIM4 mask page <mask-vim4>` reads the last two fields of the
via 4 code, `LSR` and `WET`, less certainly still, as a laser-written,
wet-etched plate.

The tab "Random Mask Case Label Info" transcribes two plate-case labels
from Photronics, one for a metal 2 plate and one for a metal 5
plate.[^steps-sheet] Both give the blank as 6 × 6 × 0.25 in
(152.4 mm × 152.4 mm × 6.35 mm) and carry "4X" in their type
field.[^steps-sheet] The tab does not tie either label to one of the
MPW runs.

(masks-renders)=
## What the mask-layer renders show

### The renders

A public web directory of mask-layer renders covers the same eight
runs. For each run and each of 42 mask layers it shows the shapes that
the 40 project dies on the run's reticle draw on the layers the site
assigns to the mask, rendered from the tape-out layouts in the public
shuttle repositories; the metadata of every die names its source file
in those repositories, its reticle frame and a SHA-1 of the
file.[^mask-renders] Each die is rendered at 0.125 µm per pixel and
the stitched reticle at 0.5 µm per pixel. The dies occupy 40 of the 42
positions of a grid of six rows and seven columns (frames A1 to F7);
the site shows the other two, A7 and C5, as "SkyWater test structures",
"not a shuttle project", and does not render them. It gives every die
as 3588.07 µm × 5188.0 µm on MPW-2 to MPW-8 and 3588.0 µm × 5188.0 µm
on MPW-1.[^mask-renders] The run pages are named in the table in
{ref}`masks-mpw-reticle-sets`; the overview page `masks.html` sets
every run against every mask.

The site states the limits of its images: "These are renders of *drawn*
data, not photomask artwork: reticle pitch, 4x reduction, mirroring and
the frame features the fab adds are not modelled. Empty images are real
results - several masks are used by no project on a given
shuttle."[^mask-renders] Its metadata carries no plate ID, so a render
is tied to a plate in the sheet only by the mask
acronym.[^mask-renders][^steps-sheet] Several of its notes describe
sizing (for example "DNM = dnwell sized by cdnm.3"), but the render jobs
list only drawn and fill layers, or Boolean expressions over them, with
no sizing step, so we read the images as unsized drawn data. A render
therefore shows whether the tape-out layouts draw on a mask's layers,
not what the plate carries. The shape totals the site prints are not
comparable between runs, and this page does not quote them: on MPW-1 one
die accounts for 99 % of the `FOM` count, and that run's `FOM` total is
more than 180 times MPW-2's.[^mask-renders]

### Plates and drawn shapes

Set against the sheet's plates ({ref}`masks-mpw-runs`), the renders
show the following.[^mask-renders][^steps-sheet]

* **Plates recorded, no drawn shapes.** `TUNM`, `ONOM` and `LDNTM` have
  plates on all eight runs, but their layers (`tunm` 80:20 for the
  first two, `ldntm` 11:44) are drawn on one die of MPW-1 (frame A4)
  and one of MPW-5 (frame D7) and on no die of the other six runs.
  `PWBM`, with plates on MPW-6 and MPW-8, and `PWDEM`, with a plate on
  MPW-6, are empty on every run: no rendered die draws `pwbm` 19:44 or
  `pwde` 124:20.
  `RPM` has a plate on MPW-3, where no die draws `rpm` 86:20. `RRM` and
  `VIMC` have plates on MPW-1 to MPW-3, and `VIMC` also on MPW-5, where
  no die draws the layer 201:20 from which the site renders both.
  Because the renders leave out whatever the fab adds, they cannot show
  what these plates carry.
* **Rendered, no plate.** Four renders have no recorded plate on any
  run, and each reuses, wholly or in its counts, another mask's layers:
  `INDM` is `met3` 70:20 ("thick-last-metal flow, not SKY130"), `VIPDM`
  is `via3` 70:44 ("pad-via flow, not SKY130") and matches `VIM3` die by
  die, `NCM` is an expression whose die-by-die counts equal those of
  `HVTPM` on every run, and `PSDI` (step 82, which has no row in the
  tab) is `psdm` 94:20, "second P+ implant, same drawn layer as PSDM".
  They are not evidence of further plates. `HVTRM`, rendered from `hvtr`
  18:20, is empty on every run, and no plate is recorded for it.
* **Plate recorded, never rendered.** The site has no `RRPM` render for
  any run, although the sheet records an `RRPM` plate on all eight.
* **The ReRAM layer.** The site renders `RRM` from the layer 201:20 and
  `VIMC` as `via` AND 201:20. Both have shapes on only three runs, on
  the same dies (frames):

  | Run | Dies with shapes on `RRM` and `VIMC` |
  |-----|--------------------------------------|
  | MPW-4 | B2, D2 |
  | MPW-7 | B3, B7, D1, D7, E2, E3 |
  | MPW-8 | B1, B3, B7, D5, E5 |

  For MPW-4 the renders and the sheet's plates belong to different
  reticle sets ({ref}`masks-mpw-reticle-sets`).
* **Masks used on few dies.** `rpm` 86:20, which the site renders for
  `RPM`, is drawn on 1, 5, 0, 3, 4, 2, 3 and 2 dies of MPW-1 to MPW-8
  in turn.
* **"40 of 40" is not 40 designs.** `CAPM`, `CAP2M` and `URPM` have
  shapes on 39 or 40 dies of every run, but on each run 33 to 39 of
  those dies carry exactly one shape on the layer, and only a few dies
  carry more. The die count therefore does not show that most projects
  use MiM capacitors or the 2000 Ω/sq resistor;[^pdk-06] the site does
  not say what the single shape is. `NSM` likewise has exactly 36 shapes
  on every die that has any.

(masks-derivations)=
### Mask derivations in the renders

For six masks the site renders a Boolean expression (`expr`) over
drawn layers rather than drawn layers alone, and for several others it
chooses layers that differ from this page's pairings; the expressions
and layer choices are the same on all eight runs.[^mask-renders] Its
README names "fab-derived masks (HVTPM, LVTNM, NCM, NTM, HVNTM)";
`VIMC` also has an expression. They are one public derivation from
the drawn data, not SkyWater's mask-generation recipe: the site gives
no source for them, and some of its notes contradict its own
expressions (below). The layer names are those of
`gds_layers.csv`;[^pdk-06] 201:20 and the datatype-28 fill layers are
not in that file, and the {ref}`overview-sky130b-reram` page reads
201:20 as `r1c`.

| Mask | This page's pairing (from the PDK files) | Renders site (`expr` verbatim, or layers rendered) | In layer names |
|------|------------------------------------------|----------------------------------------------------|----------------|
| {ref}`LVTNM <step-014>` | `lvtn` 125:44 | `125:44 OR (64:20 AND (78:44 OR 81:2))` | `lvtn` OR (`nwell` AND (`hvtp` OR `areaid.ce`)) |
| {ref}`HVTPM <step-022>` | `hvtp` 78:44 | `(64:20 NOT 75:20) NOT 125:44` | (`nwell` NOT `hvi`) NOT `lvtn` |
| {ref}`NTM <step-064>` | derived from the device layers *(inference)* | `64:20 OR 11:44 OR (75:20 NOT 81:2)` | `nwell` OR `ldntm` OR (`hvi` NOT `areaid.ce`) |
| {ref}`HVNTM <step-068>` | `hvntm` 125:20, "OR-ed with the CL" | `125:20 OR ((65:20 AND 93:44 AND 75:20) NOT 81:2)` | `hvntm` OR ((`diff` AND `nsdm` AND `hvi`) NOT `areaid.ce`) |
| NCM (no mask step) | `ncm` 92:44 | `92:44 OR ((64:20 NOT 75:20) NOT 125:44)` | `ncm` OR the `HVTPM` expression |
| VIMC (no mask step) | none; `r1v` on the {ref}`overview-sky130b-reram` page | `68:44 AND 201:20` | `via` AND 201:20 |
| {ref}`LVOM <step-044>` | the complement of `hvi` 75:20 *(inference)* | layers 75:20 and 80:20; note "LVOM = hvi OR tunm and the SKY130 layer sheet" | `hvi` and `tunm` |
| {ref}`PWBM <step-026>` | `pwbm` 19:44 with `nwell` 64:20 *(inference)* | layer 19:44 | `pwbm` |
| {ref}`RPM <step-049>` | `rpm` 86:20; `urpm` 79:20 *(inference)* | layer 86:20 | `rpm` |
| {ref}`MM4 <step-154>` | `met4` 71:20; `met4` fuse 71:17 | layers 71:20 and 51:28 | `met4` and the fill layer 51:28; no fuse purpose |

* **Where the readings differ.** For `HVTPM` this page follows the
  PDK's description of `hvtp`, "High-Vt LVPMOS implant";[^pdk-06] the
  renders build the mask from `nwell`, `hvi` and `lvtn` without `hvtp`;
  the note says the mask is "created over (LV nwell = nwell NOT hvi) NOT
  lvtn, plus hvtp only where nwell overlaps a varactor; the fab
  algorithm says do NOT OR hvtp in", naming no source, and the
  expression omits the varactor term.[^mask-renders] For `LVTNM` the
  renders add a created part inside `nwell`. For `LVOM` they show `hvi`
  OR `tunm`, where this page reads the mask as everything outside
  `hvi`; since the renders show drawn shapes, not photomask artwork, the
  two may describe the same plate in opposite tone (inference), but the
  renders also add `tunm`. The `PWBM` render has no `nwell` term, the
  `RPM` render no `urpm` term and the `MM4` render no fuse
  purpose.[^mask-renders] The step pages give the reasoning
  behind this page's readings; neither source settles which is right.
* **Where they agree.** The `NTM` and `HVNTM` expressions are
  consistent in kind with this page's readings; for `HVNTM` the created
  part is one reading of the PDK's unexpanded "CL". The renders use the
  same drawn layers as this page for `FOM` (`diff` and `tap`), `ONOM`
  (`tunm`), `CTM1` (`mcon`), `URPM` (`urpm`) and `CAP2M` (`cap2m`); for
  `FOM`, `P1M`, `LI1M` and `MM1`–`MM5` they also include a datatype-28
  layer the site lists as fill (23:28, 28:28, 56:28, 36:28, 41:28,
  34:28, 51:28, 59:28), none of which is in
  `gds_layers.csv`.[^mask-renders][^pdk-06] Both derive from the same
  public files, so the agreement is not independent confirmation.
* **Notes that contradict the expressions.** The `HVTPM` note ends
  "Rendered as nwell = a superset", but the expression subtracts `hvi`
  and `lvtn`, and it describes a varactor term that the expression does
  not include. The `LVTNM`, `HVNTM` and `NCM` notes end "only the drawn
  part is rendered", but each expression includes its created part, and
  the `LVTNM` note describes a further term, "(LV nwell over
  varactors)", that is not in the expression.[^mask-renders]
* **VIMC.** `via` AND 201:20 keeps only the vias that overlap 201:20.
  The {ref}`overview-sky130b-reram` page reads SkyWater's description
  of `r1v`, which also "defines top part of connection between met1 and
  met2", as covering the upper vias over bypasses as well as over
  cells; on that reading the renders would leave the bypass vias out
  of `VIMC` (inference).

(masks-renders-sheet-notes)=
### Notes shared with the sheet

* **Same wording.** The sheet's "Info" notes for `RRM` and `VIMC`
  repeat the renders site's wording: "sky130B RRAM tier (met1-met2)" and
  `r1c` "GDS 201/20" for `RRM`; "r1v, the upper half" of via 1 and "Not
  CTM1/mcon" (the site: "NOT CTM1/mcon") for `VIMC`. The sheet's level
  names for the local-interconnect, contact, via and metal masks
  ("Via 0 (???→M0)", "LI (Metal 0)", …) are identical to the
  site's.[^steps-sheet][^mask-renders] This page therefore does not cite
  either source as corroborating the other.
* **Which sets have an RRM plate.** The site's `RRM` note says "Only on
  the later sets 5CS8016AC/17AC/18AC", the sets the sheet heads MPW-7,
  MPW-8 and MPW-4.[^mask-renders][^steps-sheet] The sheet records `RRM`
  plates on MPW-1 (`S8M06AA430A`), MPW-2 (`S8007AA430A`) and MPW-3
  (`S8008AA430A`) as well.[^steps-sheet] The note matches the runs on
  which the renders show shapes on 201:20 rather than the runs for
  which the sheet records plates, and the site's own MPW-4 renders,
  which it ties to `5CS8010AC`, show such shapes although that set is
  not among those it names. Neither source explains the difference.
* **Plate-number arguments.** The `VIMC` note argues from plate
  numbers ("455 sits above MM1 (450) while mcon is below
  met1");[^mask-renders] as noted in {ref}`masks-mpw-reticle-sets`, the
  numbers do not follow process order.

## References

### Cross-check

* SkyWater PDK, *Masks* page and `masks.csv` — every mask name,
  acronym and `Used in SKY130` mark on this page.[^pdk-05]
* SkyWater PDK, *Layers Reference* and `gds_layers.csv` — drawn and
  mask-level layers with layer:datatype and description; Table F2b,
  the mask generation table.[^pdk-06]
* SkyWater PDK, *Criteria & Assumptions*, Table 2 — minimum feature
  and space per mask with variable names.[^pdk-03]
* SkyWater PDK, *Periphery rules* — rules x.9 and x.15a on mask-level
  layers, the grid rules x.1a and x.1b, the rule-set function lines and
  the metal-fuse note.[^pdk-periph]
* SkyWater PDK, *WLCSP Rules* — the DECA `cpbo`, `rdl` and `cpmm2`
  rule sets.[^pdk-wlcsp]
* SkyWater PDK, *Device Details* — the two MiM capacitor constructions,
  `CAPM` and `CAP2M`.[^pdk-07]
* SkyWater PDK Authors, test-tile pad documentation — the `RRPM`,
  `URPM`, `CAPM` and `CAP2M` names on test structures and the
  minimum-CD values the structures use.[^raw-data-testtile-pads]
* *S8 / SKY130 Process Steps* sheet, tabs "Run Mask IDs", "Masks",
  "Sheet4" and "Random Mask Case Label Info" — the plates recorded for
  each mask on MPW-1 to MPW-8, the mask-step list, the via mask types
  and the plate-case labels.[^steps-sheet]
* *SKY130 Open MPW mask-layer renders* — the drawn shapes of the 40
  tape-out dies of each MPW run on each of 42 mask layers, with the
  site's reticle-set, lot and derivation metadata.[^mask-renders]

### High-level understanding

* Wikipedia, *Photomask* — reticles, substrates, absorbers and
  pellicles.[^wiki-mask]
* Wikipedia, *Photolithography* — the mask step in the process
  sequence.[^wiki-litho]
* Wikipedia, *Optical proximity correction* and *Phase-shift mask* —
  why mask shapes differ from drawn shapes.[^wiki-opc][^wiki-psm]
* Mack, *Fundamental Principles of Optical Lithography* — how a mask
  pattern becomes a resist pattern.[^mack-2007]
* Levinson, *Principles of Lithography*, 4th ed. — masks, overlay and
  metrology in one volume.[^levinson-2019]
* Wolf and Tauber, *Silicon Processing for the VLSI Era*, vol. 1 —
  lithography chapters.[^txt-02]
* Quirk and Serda, *Semiconductor Manufacturing Technology* — the
  fab-floor view of masks and photolithography.[^txt-07]
* Campbell, *Fabrication Engineering at the Micro- and Nanoscale* —
  lithography chapters.[^campbell-2013]

### Deep dive

* ITRS 2001, *Lithography* — mask magnification, PSM choices and
  overlay targets for the 130 nm generation.[^itrs-03]
* Levenson, Viswanathan and Simpson (IBM), *IEEE TED* 1982 — the
  original phase-shifting mask.[^levenson-1982]
* Lin, *IEEE Circuits and Devices* 1993 — a tutorial on alternating
  and attenuated phase-shift masks.[^lin-1993]
* Otto et al., *Proc. SPIE* 1994 — rules-based optical proximity
  correction, one way drawn data become mask data.[^otto-1994]
* Rieger and Stirniman, *Proc. SPIE* 1994 — model-based proximity
  correction.[^rieger-1994]
* Cobb and Zakhor, *Proc. SPIE* 1995 — fast aerial-image calculation
  for model-based OPC.[^cobb-1995]
* Yamamoto et al., MNC 2000 — hierarchical OPC on contact-hole layers,
  the data-volume side of mask preparation.[^yamamoto-2000]
* Wong, *Resolution Enhancement Techniques in Optical Lithography* —
  the SPIE text on PSM, OPC and off-axis illumination.[^wong-2001]
* Kahng and Samadi, *IEEE TCAD* 2008 — a survey of CMP dummy-fill
  synthesis, the design-side view of waffle and fill
  layers.[^kahng-2008]
* Stine et al., *IEEE TSM* 1998 — pattern-dependent CMP variation, the
  basis of density-driven fill rules.[^stine-1998]
* Chiou and Jang (TSMC), US 6,849,549 — dummy structures for CMP
  planarity with reduced added capacitance.[^pat-dummy-tsmc]
* Buffat and Adams (Zilog), US 6,576,405 — thick-resist masking for
  high-energy implants, the demand an implant block mask
  meets.[^pat-resist-zilog]
* Edmark and Ausschnitt, *Proc. SPIE* 1985 — stepper overlay
  calibration by aligning to a latent image, relevant to the first
  mask level.[^edmark-1985]
* Starikov, *Opt. Eng.* 1992 — accuracy of overlay measurement between
  mask levels.[^starikov-1992]
* van Haren et al., *Proc. SPIE* 2019 — how alignment-mark placement
  on the reticle limits layer-to-layer overlay.[^van-haren-2019]
* Levinson, *Principles of Lithography*, 2nd ed. — overlay budgets and
  the choice of tools for non-critical levels.[^levinson-2005]
* SEMI P1 — the specification for hard-surface photomask
  substrates.[^semi-p1]
* Bruning, *Proc. SPIE* 2007 — forty years of optical lithography
  tools that print masks onto wafers.[^bruning-2007]

## Open questions

* The PDK does not publish the operations that generate each mask from
  the drawn layers (apart from the `hvntm` note), nor what the
  `drawing`, `mask add`, `mask drop` and `waffle drop` purposes
  contribute when they sit on a different layer number from the `mask`
  purpose (`cp1m` 28:0 against 33:42–33:43, for example).[^pdk-06] The
  pairings marked *(inference)* rest on the step pages' readings. The
  public renders use one derivation that differs from several of them,
  and from the `HVTPM` and `LVTNM` pairings, and cite no source for it
  ({ref}`masks-derivations`);[^mask-renders] which reading matches the
  plates is not public.
* `masks.csv` leaves the `Used in SKY130` field blank for `PWBM`,
  `PWDEM` and `CAPM` and has no entry matching the
  {ref}`RRPM <step-052>`, {ref}`URPM <step-055>` and
  {ref}`CAP2M <step-152>` mask steps of this reference, although the
  layers their step pages pair them with (`rpm`, `urpm`, `cap2m`) exist
  and, for `PWBM`, `PWDEM` and `CAPM`, rule sets and Table F2b columns
  exist too.[^pdk-05][^pdk-06][^pdk-periph] The PDK does not explain
  the difference. The process-steps sheet records plates for `RRPM`,
  `URPM`, `CAPM` and `CAP2M` on all eight MPW runs, but for `PWBM` only
  on MPW-6 and MPW-8 and for `PWDEM` only on MPW-6;[^steps-sheet] it
  does not say why plates for the two P-well masks are recorded for
  only some runs. No rendered die on any run draws `pwbm` or
  `pwde`,[^mask-renders] so the renders do not show what those plates
  carry.
* `HVTRM` is marked, with a mask-level layer, a drawn layer and a
  minimum CD, but has no mask step here; the PDK's layer description
  ("High-Vt RF transistor implant") and rule-set function line ("Define
  low VT adjust implant region for pmedlvtrf") do not settle what the
  implant does.[^pdk-06][^pdk-periph] The process-steps sheet records
  no `HVTRM` plate for any of MPW-1 to MPW-8,[^steps-sheet] and no
  rendered die on those runs draws `hvtr`.[^mask-renders]
* The PDK does not say at which stage, or where, the marked `PBO`,
  `CU1M` and `PMM2` masks are used; their rules are published with the
  WLCSP and redistribution rules,[^pdk-wlcsp][^pdk-periph] and the
  process-steps sheet records no plate for any of them on MPW-1 to
  MPW-8.[^steps-sheet]
* The variant suffixes of `masks.csv` ("TNV", "S8TM", "PLM", "TLM")
  are not defined on the *Masks* page;[^pdk-05] the
  {ref}`VIM2 <step-129>` and {ref}`MM3 <step-139>` pages give
  readings.
* Table 2 of *Criteria & Assumptions* has no unit column;[^pdk-03] the
  µm reading rests on agreement with the periphery rules and the test
  tile's pad documentation.[^pdk-periph][^raw-data-testtile-pads]
* No PDK document gives the resist tone, reticle type (binary or
  phase-shift) or exposure tool for any mask. The process-steps sheet
  gives a coded reticle type for three masks only, which we read as
  embedded attenuated phase-shift masks for via 2 and via 3 and a
  binary mask for via 4, all for 248 nm exposure and, less certainly,
  4×.[^steps-sheet][^photronics-abr] It names no resist tone or
  exposure tool, and no type for the other masks. The
  {ref}`VIM2 <step-129>`, {ref}`VIM3 <step-144>` and
  {ref}`VIM4 <step-159>` pages take up this reading; that the three
  levels are exposed on KrF tools, via 4 included despite its 0.8 µm
  size, remains an inference from the reticle types.
  `gds_layers.csv` has an
  `areaid.op` identifier (81:54, "OPC drop. Block automatic OPC (for
  fab blocks and lithocal structures)"), which implies that automatic
  OPC is applied;[^pdk-06] rule x.1a sets a grid of 0.001 (unit printed
  as "mm") for "p1m.md (OPC)", among other layers, and for the "mask
  data for p1m, met1, via, met2", against 0.005 for all other layers
  (x.1b), but the PDK does not describe the correction
  ({ref}`mask-p1m`);[^pdk-periph] the step pages and
  the {ref}`lithography category page <category-lithography>` give
  industry-generic readings.
* The process-steps sheet records no plates for `CTM1`, `MM1`, `VIM`,
  `VIM4` and `PDM` on MPW-5, and a different plate number for `NSM` on
  MPW-6 ({ref}`masks-mpw-reticle-sets`);[^steps-sheet] it does not say
  whether these are gaps in the record or differences between the
  runs. It does not say what the three-digit plate numbers encode.
* The sheet records plates for masks whose layers no rendered die of the
  run draws — `TUNM`, `ONOM` and `LDNTM` on six runs, `RPM` on MPW-3,
  `RRM` and `VIMC` on the runs without ReRAM layouts — and no public
  source says what those plates carry (the renders omit whatever the
  fab adds to a plate).[^steps-sheet][^mask-renders] The site renders no
  `RRPM` image although a plate is recorded on every run.
* Neither the renders site nor the sheet explains why they disagree on
  which sets carry an `RRM` plate
  ({ref}`masks-renders-sheet-notes`).[^mask-renders][^steps-sheet]
* No public source lists the plates of the original MPW-4 set
  `5CS8010AC`, whose layouts the renders show, or says how it differs
  from `5CS8018AC`, whose plates the sheet records
  ({ref}`masks-mpw-reticle-sets`).[^mask-renders][^steps-sheet]
* The site's project counts for the shuttles (37 to 144) differ from
  the 40 dies it renders for every run, and it does not explain the
  difference.[^mask-renders]

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
[^pdk-wlcsp]: SkyWater PDK Authors, *WLCSP Rules* (Amkor and DECA
    tables), SkyWater SKY130 PDK documentation.
    <https://skywater-pdk.readthedocs.io/en/main/rules/wlcsp.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/wlcsp/deca.csv>
[^pdk-07]: SkyWater PDK Authors, *Device Details* (MiM capacitors),
    SkyWater SKY130 PDK documentation, and the `cap_mim` cross-section
    drawing.
    <https://skywater-pdk.readthedocs.io/en/main/rules/device-details.html>,
    <https://raw.githubusercontent.com/google/skywater-pdk/main/docs/rules/device-details/cap_mim/cross-section-cap_mim.svg>
[^raw-data-testtile-pads]: SkyWater PDK Authors, *Manufacturing Test Tile
    Pad Documentation* ("Pad documentation for SKY130 MPW Manufacturing
    E-Test Tile"), `sky130-testtile-pad-documentation.csv` (also `.ods`
    and `.pdf`), `google/skywater-pdk-sky130-raw-data` repository, 2022,
    retrieved 2026-09-13.
    <https://github.com/google/skywater-pdk-sky130-raw-data/blob/main/docs/sky130-testtile-proprietary/sky130-testtile-pad-documentation.csv>
[^steps-sheet]: *[external] S8 / SKY130 Process Steps*, public Google Sheet,
    tabs "Run Mask IDs" (the mask table set against MPW-1 to MPW-8, with
    an "Exists" column per run), "Masks" (mask steps with step numbers),
    "Sheet4" (mask types), "Random Mask Case Label Info" (plate-case
    labels) and "Sheet1" (step number, code and description), retrieved
    2026-09-13.
    <https://docs.google.com/spreadsheets/d/1PbI3IVNg93fR9Gi_hXlEDrlYtwFQuMyaD8PNEaIs3Sg>
[^mask-renders]: *SKY130 Open MPW mask-layer renders*, public web
    directory: `README.md`, `masks.html`, the run pages `mpw-001.html` to
    `mpw-008.html`, and for each run × mask directory the page,
    `job.json`, `result.json` and per-die slot JSON files, retrieved
    2026-09-13. Run pages are `mpw-00N.html`; each render's page is
    `<run>_<mask>/<run>_<mask>.html` (for example
    `mpw-001_TUNM/mpw-001_TUNM.html`). Rendered from the public shuttle
    repositories under
    <https://foss-eda-tools.googlesource.com/third_party/shuttle/sky130/>.
    <https://data.wafer.space/big-storage/sky130-masks/>
[^photronics-abr]: Photronics, Inc., *Advanced Binary Reticle*, product
    page, retrieved 2026-09-13.
    <https://www.photronics.com/products/advanced-binary-reticle/>
[^pat-bim-tsmc]: S.-J. Lin and W.-C. Wang (Taiwan Semiconductor
    Manufacturing Co.), *Method for forming binary intensity masks*,
    US 6,379,849 B1, filed 2000-10-26, granted 2002-04-30.
    <https://patents.google.com/patent/US6379849B1/en>
[^wiki-litho]: Wikipedia, *Photolithography*.
    <https://en.wikipedia.org/wiki/Photolithography>
[^wiki-opc]: Wikipedia, *Optical proximity correction*.
    <https://en.wikipedia.org/wiki/Optical_proximity_correction>
[^wiki-psm]: Wikipedia, *Phase-shift mask*.
    <https://en.wikipedia.org/wiki/Phase-shift_mask>
[^mack-2007]: C. Mack, *Fundamental Principles of Optical Lithography:
    The Science of Microfabrication*, Wiley, 2007, ISBN
    978-0-470-01893-4. <https://doi.org/10.1002/9780470723876>
    (companion site <https://www.lithoguru.com/textbook/>)
[^levinson-2019]: H. J. Levinson, *Principles of Lithography*, 4th ed.,
    SPIE Press, 2019, ISBN 978-1-5106-2760-4.
    <https://doi.org/10.1117/3.2525393>
[^txt-02]: S. Wolf and R. N. Tauber, *Silicon Processing for the VLSI
    Era, Vol. 1: Process Technology*, 2nd ed., Lattice Press, 2000,
    ISBN 978-0-9616721-6-4. <https://openlibrary.org/isbn/9780961672164>
[^txt-07]: M. Quirk and J. Serda, *Semiconductor Manufacturing
    Technology*, Prentice Hall, 2001, ISBN 978-0-13-081520-0.
    <https://openlibrary.org/isbn/9780130815200>
[^campbell-2013]: S. A. Campbell, *Fabrication Engineering at the Micro-
    and Nanoscale*, 4th ed., Oxford University Press, 2013,
    ISBN 978-0-19-986122-4. <https://openlibrary.org/isbn/9780199861224>
[^levenson-1982]: M. D. Levenson, N. S. Viswanathan and R. A. Simpson,
    "Improving resolution in photolithography with a phase-shifting
    mask", *IEEE Transactions on Electron Devices* **29**(12),
    1828–1836 (1982). <https://doi.org/10.1109/T-ED.1982.21037>
[^lin-1993]: B. J. Lin, "Phase-shifting masks gain an edge", *IEEE
    Circuits and Devices Magazine* **9**(2), 28–35 (1993).
    <https://doi.org/10.1109/101.200850>
[^otto-1994]: O. W. Otto, J. G. Garofalo, K. K. Low, C.-M. Yuan,
    R. C. Henderson, C. Pierrat, R. L. Kostelak, S. Vaidya and
    P. K. Vasudev, "Automated optical proximity correction: a
    rules-based approach", *Proc. SPIE* **2197**, Optical/Laser
    Microlithography VII, 278–293 (1994).
    <https://doi.org/10.1117/12.175422>
[^rieger-1994]: M. L. Rieger and J. P. Stirniman, "Using behavior
    modeling for proximity correction", *Proc. SPIE* **2197**, 371–376
    (1994). <https://doi.org/10.1117/12.175431>
[^cobb-1995]: N. B. Cobb and A. Zakhor, "Fast sparse aerial-image
    calculation for OPC", *Proc. SPIE* **2621**, 534–545 (1995).
    <https://doi.org/10.1117/12.228208>
[^yamamoto-2000]: K. Yamamoto, S. Kobayashi, T. Uno and T. Kotani,
    "Hierarchical optical proximity correction on contact hole layers",
    *Digest of Papers, Microprocesses and Nanotechnology 2000*,
    pp. 40–41. <https://doi.org/10.1109/IMNC.2000.872612>
[^wong-2001]: A. K.-K. Wong, *Resolution Enhancement Techniques in
    Optical Lithography*, SPIE Tutorial Texts TT47, SPIE Press, 2001,
    ISBN 978-0-8194-7881-8. <https://doi.org/10.1117/3.401208>
[^kahng-2008]: A. B. Kahng and K. Samadi, "CMP Fill Synthesis: A Survey
    of Recent Studies", *IEEE Transactions on Computer-Aided Design of
    Integrated Circuits and Systems* **27**(1), 3–19 (2008).
    <https://doi.org/10.1109/TCAD.2007.907061>
[^stine-1998]: B. E. Stine, D. O. Ouma, R. R. Divecha, D. S. Boning,
    J. E. Chung, D. L. Hetherington, C. R. Harwood, O. S. Nakagawa and
    S.-Y. Oh, "Rapid characterization and modeling of pattern-dependent
    variation in chemical-mechanical polishing", *IEEE Transactions on
    Semiconductor Manufacturing* **11**(1), 129–140 (1998).
    <https://doi.org/10.1109/66.661292>
[^pat-dummy-tsmc]: W.-C. Chiou and S.-M. Jang (Taiwan Semiconductor
    Manufacturing Co.), *Method for forming dummy structures for improved
    CMP and reduced capacitance*, US 6,849,549 B1, filed 2003-12-04,
    granted 2005-02-01.
    <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6849549>
[^pat-resist-zilog]: S. J. Buffat and J. L. Adams (Zilog), *High aspect
    ratio photolithographic method for high energy implantation*, US
    6,576,405 B1, granted 2003-06-10.
    <https://patents.google.com/patent/US6576405B1/en>
[^edmark-1985]: K. W. Edmark and C. P. Ausschnitt, "Stepper Overlay
    Calibration Using Alignment To A Latent Image", *Proc. SPIE*
    **0538**, Optical Microlithography IV, 91 (1985).
    <https://doi.org/10.1117/12.947752>
[^starikov-1992]: A. Starikov, "Accuracy of overlay measurements: tool
    and mark asymmetry effects", *Optical Engineering* **31**(6), 1298
    (1992). <https://doi.org/10.1117/12.56172>
[^van-haren-2019]: R. J. F. van Haren, S. Steinert, O. Mouraille,
    K. D'havé, L. van Dijk, J. Hermans and D. Beyer, "Wafer alignment
    mark placement accuracy impact on the layer-to-layer overlay
    performance", *Proc. SPIE* **11148**, Photomask Technology 2019, 37
    (2019). <https://doi.org/10.1117/12.2536270>
[^levinson-2005]: H. J. Levinson, *Principles of Lithography*, 2nd ed.,
    SPIE Press, 2005, ISBN 978-0-8194-5660-1.
    <https://doi.org/10.1117/3.601520>
[^semi-p1]: SEMI, *SEMI P1 — Specification for Hard Surface Photomask
    Substrates*, SEMI Standards store listing.
    <https://store-us.semi.org/products/p00100-semi-p1-specification-for-hard-surface-photomask-substrates>
[^bruning-2007]: J. H. Bruning, "Optical lithography: 40 years and
    holding", *Proc. SPIE* **6520**, 652004 (2007).
    <https://doi.org/10.1117/12.720631>
