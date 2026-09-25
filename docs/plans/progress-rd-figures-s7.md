# Progress — rd-figures-s7 (W1c, series S7: pre-metal dielectric, contact, silicide and local interconnect, steps 089–106)

Status: **in progress**.

## Done

* Generator: a doped region with `follow: surface` is measured from the original silicon
  surface where a `react` product (the contact silicide) has replaced the top of the silicon
  (`XSection.surface_ref`), so the N⁺ source/drain does not dip under the silicide disc.
  Selftest added. No existing figure changes (no series used `react` before).
* Series `data/figures/series-mol.yaml`: ops 002–088 copied verbatim from
  `series-tips-sd.yaml`, then the module. The header records every geometric choice.

## Left

* Figures 089–106, placement, QA, gates.
