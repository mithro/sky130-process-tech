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
 *
 * The card is inserted right after its marker in DOM order (not
 * appended to <body>) so that Tab reaches its links immediately after
 * the marker, and the marker carries aria-expanded/aria-describedby
 * while the card is open, but nothing moves focus into the card and
 * nothing traps it there — Tab continues past it as normal.
 *
 * C10 / R-ANCHOR: the card also appends a small "Inventory entry" link
 * to the footnote's "own" entry in the public sources inventory
 * (docs/references/public-sources.md), which tools/fix_inventory_entries.py
 * gives an anchor `(src-<key-lowercased>)=` above every `**KEY** —` entry.
 * On this site the footnote label already equals the inventory key
 * (verified script-side, case-folded, across every written page: see
 * docs/plans/progress-rd-site.md), so the footnote's own id -- the same
 * "label" this script already reads off the marker's href -- is also the
 * inventory anchor's suffix. One exception exists (WHS-T4; see the
 * progress file): its entry has no anchor, so this link is added for it
 * too but lands on the inventory page without scrolling to an entry --
 * graceful degradation, not a broken link, and worth accepting rather
 * than special-casing one label in a site-wide, static script.
 */
(function () {
  "use strict";

  var card = null;
  var owner = null;
  var hideTimer = null;
  var cardSeq = 0;
  /* Touch state, tracked independently of "owner": a real tap on a
     touch device fires an emulated "mouseenter" (which shows the card
     and sets "owner") *before* "click", so gating the tap purely on
     "owner !== marker" never fires (review finding H2) — the first tap
     would already own the card by the time click ran, and so would
     follow the link instead of only opening it. */
  var tappedMarker = null;

  function hide() {
    tappedMarker = null;
    if (card) {
      if (owner) {
        owner.removeAttribute("aria-expanded");
        owner.removeAttribute("aria-describedby");
      }
      card.remove();
      card = null;
      owner = null;
    }
  }

  function hideSoon() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, 250);
  }

  /* Appends a small "Inventory entry" link to `card` for the footnote
     label `id` (== the inventory key, lower-cased; see the file comment
     above). `data-content_root`, on <html>, is the relative path Sphinx
     itself gives every page back to the site root (e.g. "../" one level
     down, "./" at the root) -- the standard, template-provided way to
     link to a fixed page regardless of how deep the current page sits. */
  function appendInventoryLink(card, id) {
    var root = document.documentElement.getAttribute("data-content_root") || "./";
    var link = document.createElement("a");
    link.className = "fn-popover-inventory-link";
    link.href = root + "references/public-sources.html#src-" + id;
    link.textContent = "Inventory entry";
    card.appendChild(link);
  }

  function keep() {
    clearTimeout(hideTimer);
  }

  function show(marker) {
    keep();
    if (owner === marker) {
      return;
    }

    var id = decodeURIComponent(marker.getAttribute("href").slice(1));
    var note = document.getElementById(id);
    if (!note) {
      return;
    }
    /* Only the definition's own content (paragraphs, lists): skip the
       "[18]" label and the "(1,2,3)" back-reference list, so a
       many-times-cited footnote still shows a short, readable card. */
    var content = note.querySelectorAll(":scope > p, :scope > ul, :scope > ol, :scope > dl");
    if (!content.length) {
      return;
    }

    hide();

    cardSeq += 1;
    card = document.createElement("div");
    card.className = "fn-popover";
    card.id = "fn-popover-" + cardSeq;
    card.setAttribute("role", "tooltip");
    card.setAttribute("tabindex", "-1");
    content.forEach(function (node) {
      card.appendChild(node.cloneNode(true));
    });
    appendInventoryLink(card, id);
    marker.insertAdjacentElement("afterend", card);
    marker.setAttribute("aria-expanded", "true");
    marker.setAttribute("aria-describedby", card.id);

    // The card is "position: fixed" (see custom.css), so every measure
    // here is viewport-relative: no window.scrollX/scrollY term, and
    // this stays correct however deep in the DOM the card ends up
    // (inside a table cell or an open {dropdown}, both of which can be
    // — or sit inside — a positioned or overflow-clipping ancestor).
    var rect = marker.getBoundingClientRect();
    var width = Math.min(420, window.innerWidth - 16);
    var left = Math.max(8, Math.min(rect.left - 20, window.innerWidth - width - 8));
    card.style.width = width + "px";
    card.style.left = left + "px";

    /* Below the marker by default; flip above it when there is not
       room below in the viewport (review finding L5), using the
       card's real height now that it is in the document. */
    var below = rect.bottom + 6;
    var cardHeight = card.offsetHeight;
    if (rect.bottom + cardHeight + 6 > window.innerHeight && rect.top - cardHeight - 6 > 0) {
      card.style.top = rect.top - cardHeight - 6 + "px";
    } else {
      card.style.top = below + "px";
    }

    card.addEventListener("mouseenter", keep);
    card.addEventListener("mouseleave", hideSoon);
    card.addEventListener("focusin", keep);
    card.addEventListener("focusout", hideSoon);
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

      /* Touch: a pointerdown with pointerType "touch" is the actual
         tap, independent of any emulated mouse events the browser
         also sends for it. First tap opens the card and is prevented
         from navigating; the second tap on the same marker navigates
         (state resets). */
      marker.addEventListener("pointerdown", function (event) {
        if (event.pointerType !== "touch") {
          return;
        }
        if (tappedMarker === marker) {
          tappedMarker = null; // second tap: let the click through
          return;
        }
        // show() closes any other open card via hide(), which also
        // clears "tappedMarker" as a side effect (that is what lets a
        // fresh tap after a close start over) — so set it *after*
        // show() returns, or that same call would immediately wipe
        // out the flag this tap just set.
        show(marker);
        tappedMarker = marker;
      });
      marker.addEventListener("click", function (event) {
        if (tappedMarker === marker) {
          // A pointerdown just opened the card for this marker: this
          // click is the same first tap, not a second one. Consume it.
          event.preventDefault();
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
