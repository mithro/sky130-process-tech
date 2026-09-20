/* Make generated figures follow furo's light/dark toggle exactly.
   Every generated figure NAME.svg follows the operating system by itself
   (prefers-color-scheme inside the SVG). When the reader forces a theme with furo's toggle,
   swap in NAME.light.svg / NAME.dark.svg, which the generator writes beside it in
   _static/figures/. Without JavaScript nothing breaks: the auto file is already readable on
   either background.

   Only images that came from _static/figures/ (or the _images/ copy Sphinx makes of them)
   are touched, because only those have forced variants; any other SVG in a figure is left
   exactly as the page author wrote it. If a forced variant fails to load for any reason the
   image falls back to the file the page shipped with. */
(function () {
  var GENERATED = /(?:_static\/figures|_images)\//;

  function swap(img, theme, root) {
    if (img.dataset.figBase === undefined) {
      var src = img.getAttribute("src") || "";
      var m = src.match(/([^\/]+?)(?:\.light|\.dark)?\.svg$/);
      if (!m || !GENERATED.test(src)) {
        img.dataset.figBase = "";                       // not ours; never touch it again
        return;
      }
      img.dataset.figBase = m[1];
      img.dataset.figOrig = src;
    }
    if (!img.dataset.figBase) return;
    var want = theme === "light" || theme === "dark"
      ? root + "_static/figures/" + img.dataset.figBase + "." + theme + ".svg"
      : img.dataset.figOrig;
    if (img.getAttribute("src") === want) return;
    img.onerror = function () {
      img.onerror = null;
      img.setAttribute("src", img.dataset.figOrig);
    };
    img.setAttribute("src", want);
  }

  function apply() {
    var theme = document.body.dataset.theme;            // "light", "dark" or "auto"
    var root = document.documentElement.dataset.content_root || "./";
    document.querySelectorAll("figure img[src$='.svg']").forEach(function (img) {
      swap(img, theme, root);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    apply();
    new MutationObserver(apply).observe(document.body,
      { attributes: true, attributeFilter: ["data-theme"], childList: true, subtree: true });
  });
})();
