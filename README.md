# SKY130 Process Technology — a step-by-step manufacturing reference

This project documents, step by step, how the SKY130 130 nm CMOS process
technology is manufactured. SKY130 is the open-source process design kit
(PDK) released by SkyWater Technology and Google in 2020; it is derived
from the Cypress Semiconductor "S8" 130 nm process and is fabricated on
200 mm wafers at SkyWater's Bloomington, Minnesota fab.

The aim is to be the most comprehensive public reference on how a
mass-produced 130 nm process is set up — using SKY130 as the worked
example — covering, for every process step:

* what the step is and which general class of step it belongs to
  (oxidation, deposition, lithography, etch, implant, anneal, CMP, …);
* why the step exists in the integration flow;
* which kinds of manufacturing tools perform it, and which tools
  SkyWater is likely to use (based on public evidence);
* which consumables it needs (gases, wet chemicals, sputter targets,
  slurries, photoresists, …);
* public references for cross-checking, for a high-level understanding,
  and for a deep dive.

The documentation is written in Markdown, built with Sphinx + MyST, and
intended for publication on Read the Docs.

## Building

```sh
uv sync
uv run sphinx-build -W -b html docs docs/_build/html
```

## Sources

Only publicly available sources are cited. See
`docs/references/` for the bibliography and the source policy in
`docs/plans/`.

## Licence

Apache License 2.0 — see `LICENSE`.
