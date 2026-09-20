/*
 * Footnote popover (docs/plans/readability/report-C.md C3).
 *
 * A footnote marker ("[18]") is a 12 px target that jumps to the page
 * foot, and the way back is a bare "(1,2,3,4)" list. This script shows
 * the footnote's own text, links included, in a small card beside the
 * marker on hover, keyboard focus, or a first tap; Esc or clicking
 * away closes it; a second tap on a touch device follows the link as
 * before. It reads the existing
 * <a class="footnote-reference" href="#label"> and
 * <aside class="footnote" id="label"> that docutils already renders,
 * so no page content changes, and it has no dependency.
 */
(function () {
  "use strict";

  var card = null;
  var owner = null;
  var hideTimer = null;

  function hide() {
    if (card) {
      card.remove();
      card = null;
      owner = null;
    }
  }

  function hideSoon() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, 250);
  }

  function keep() {
    clearTimeout(hideTimer);
  }

  function show(marker) {
    keep();
    if (owner === marker) {
      return;
    }
    hide();

    var id = decodeURIComponent(marker.getAttribute("href").slice(1));
    var note = document.getElementById(id);
    if (!note) {
      return;
    }

    card = document.createElement("div");
    card.className = "fn-popover";
    card.setAttribute("role", "note");
    /* Only the definition's own content (paragraphs, lists): skip the
       "[18]" label and the "(1,2,3)" back-reference list, so a
       many-times-cited footnote still shows a short, readable card. */
    var content = note.querySelectorAll(":scope > p, :scope > ul, :scope > ol, :scope > dl");
    if (!content.length) {
      return;
    }
    content.forEach(function (node) {
      card.appendChild(node.cloneNode(true));
    });
    document.body.appendChild(card);

    var rect = marker.getBoundingClientRect();
    var width = Math.min(420, window.innerWidth - 16);
    var left = Math.max(
      8,
      Math.min(
        rect.left + window.scrollX - 20,
        window.scrollX + window.innerWidth - width - 8
      )
    );
    card.style.width = width + "px";
    card.style.left = left + "px";
    card.style.top = rect.bottom + window.scrollY + 6 + "px";

    card.addEventListener("mouseenter", keep);
    card.addEventListener("mouseleave", hideSoon);
    owner = marker;
  }

  document.addEventListener("DOMContentLoaded", function () {
    var markers = document.querySelectorAll("a.footnote-reference");
    markers.forEach(function (marker) {
      marker.addEventListener("mouseenter", function () {
        show(marker);
      });
      marker.addEventListener("mouseleave", hideSoon);
      marker.addEventListener("focus", function () {
        show(marker);
      });
      marker.addEventListener("blur", hideSoon);
      marker.addEventListener("click", function (event) {
        /* Touch device: the first tap previews, the second tap (once
           this marker already owns the open card) follows the link
           as it would without this script. */
        if (window.matchMedia("(hover: none)").matches && owner !== marker) {
          event.preventDefault();
          show(marker);
        }
      });
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        hide();
      }
    });

    document.addEventListener("click", function (event) {
      if (
        card &&
        !card.contains(event.target) &&
        !event.target.closest("a.footnote-reference")
      ) {
        hide();
      }
    });
  });
})();
