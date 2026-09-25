# Progress — rd-figures-s6 (W1c, series S6: tips, halos, spacers and source/drain, steps 064–088)

Status: **in progress**.

## Done

* Generator (`tools/gen_figures.py`):
  * `close_up: [x0, x1]` on a cross-section: draws that window of the series state, enlarged by
    the same factor in x and y (angles survive), for the transistor close-up report D asks for.
    The series geometry is untouched; panel positions (`highlight`, `callouts`, `dims`,
    `top@x`) are written in series x and moved by the generator. Lint: the caption must say
    "close-up of …". Selftests for the scaling and for the lint.
  * `deposit` with `flat: false` and `where`: a patterned film that follows the surface inside
    its ranges (the thin 0.3 µm HV-tip resist, thinner than the gate stacks it covers).
    Selftest.
* Tokens: new material `tip-n` ("n-type tip (source/drain extension)", light blue with crossed
  hatching), so a tip reads apart from the deep N⁺ source/drain (`sd-n`, whose legend no longer
  says "n-tip"). `palette` reports 0 confusable pairs. Every SVG was regenerated: the only change
  in the existing figures is the CSS variable list; the legend gains one row.

## Left

* `data/figures/series-tips-sd.yaml`, 25 figure specs, placement, checks, QA.
