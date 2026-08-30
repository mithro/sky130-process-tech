(categories-index)=
# Step categories

Every process step belongs to one general category of unit process.
Each category page explains the physics and engineering of that class of
step once — what the step does, the models and process windows that
govern it, the tool classes and consumables a 130 nm-era 200 mm fab
would use, and the SKY130 steps that belong to it — so the individual
step pages can concentrate on what is specific to SKY130. Tool models
are described generically on these pages; which tools SkyWater itself
is likely to use is discussed on the machine and step pages.

| Category | Description | Steps |
|----------|-------------|-------|
| {ref}`category-substrate` | Starting wafer material | 1 |
| {ref}`category-oxidation` | Thermal growth of silicon dioxide | 6 |
| {ref}`category-deposition` | CVD, PVD and spin-on thin films | 41 |
| {ref}`category-lithography` | Photoresist coat, expose, develop | 36 |
| {ref}`category-etch` | Plasma and wet pattern transfer | 27 |
| {ref}`category-implant` | Ion implantation of dopants | 25 |
| {ref}`category-strip` | Photoresist strip and post-strip clean | 15 |
| {ref}`category-anneal` | Furnace and rapid thermal anneal, silicide, alloy | 7 |
| {ref}`category-cmp` | Chemical-mechanical planarisation | 12 |
| {ref}`category-test` | Parametric electrical test | 1 |

```{toctree}
:maxdepth: 1
:hidden:

substrate
oxidation
deposition
lithography
etch
implant
strip
anneal
cmp
test
```
