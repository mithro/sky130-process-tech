/* Make generated figures follow furo's light/dark toggle exactly.
   Every figure NAME.svg follows the operating system by itself (prefers-color-scheme inside the SVG).
   When the reader forces a theme with furo's toggle, swap in NAME.light.svg / NAME.dark.svg,
   which the generator writes next to it in _static/figures/. Without JavaScript nothing breaks. */
(function () {
  function apply() {
    var theme = document.body.dataset.theme;                       // "light", "dark" or "auto"
    var root = document.documentElement.dataset.content_root || "./";
    document.querySelectorAll("figure img[src$='.svg']").forEach(function (img) {
      if (!img.dataset.figBase) {
        var m = img.getAttribute("src").match(/([^\/]+?)(?:\.light|\.dark)?\.svg$/);
        if (!m) return;
        img.dataset.figBase = m[1];
        img.dataset.figOrig = img.getAttribute("src");
      }
      var want = theme === "light" || theme === "dark"
        ? root + "_static/figures/" + img.dataset.figBase + "." + theme + ".svg"
        : img.dataset.figOrig;
      if (img.getAttribute("src") !== want) img.setAttribute("src", want);
    });
  }
  document.addEventListener("DOMContentLoaded", function () {
    apply();
    new MutationObserver(apply).observe(document.body, { attributes: true, attributeFilter: ["data-theme"] });
  });
})();
