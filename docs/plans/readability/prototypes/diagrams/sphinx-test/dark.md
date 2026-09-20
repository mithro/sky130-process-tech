# Figure inclusion test (forced dark)

<script>document.addEventListener("DOMContentLoaded",()=>{document.body.dataset.theme="dark"})</script>

Matched case: the dark variant on furo's dark background.

:::{figure} /_static/figures/sti-006-stie.svg
:alt: test
:width: 560px

Dark variant, caption.
:::

Mismatched case (reader forced furo to dark while the operating system is light): the `auto` file shows its light card.

:::{figure} /_static/figures/sti-006-stie.svg
:alt: test
:width: 560px

Auto variant on a forced-dark page.
:::

:::{figure} /_static/figures/flow-modules.svg
:alt: test
:width: 560px

Flow map, dark.
:::
