/*
 * Let a reader dismiss the "AI in use" announcement bar for a month.
 *
 * This file is loaded from the document head, before the body exists, so
 * a bar that is still dismissed is hidden by adding a class to <html>
 * rather than by touching the element (which is not there yet).
 */
(function () {
  "use strict";

  var KEY = "sky130-announcement-dismissed-until";
  var PERIOD_MS = 30 * 24 * 60 * 60 * 1000;

  function read() {
    try {
      return parseInt(window.localStorage.getItem(KEY), 10) || 0;
    } catch (e) {
      return 0; /* storage disabled or blocked */
    }
  }

  function write(until) {
    try {
      window.localStorage.setItem(KEY, String(until));
    } catch (e) {
      /* nothing to do: the bar simply comes back on the next page */
    }
  }

  if (read() > Date.now()) {
    document.documentElement.classList.add("announcement-dismissed");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var content = document.querySelector(".announcement .announcement-content");
    if (!content) {
      return;
    }

    var button = document.createElement("button");
    button.className = "announcement-dismiss";
    button.type = "button";
    button.title = "Hide this warning for a month";
    button.setAttribute("aria-label", "Hide this warning for a month");
    button.innerHTML = "&times;";
    button.addEventListener("click", function () {
      write(Date.now() + PERIOD_MS);
      document.documentElement.classList.add("announcement-dismissed");
    });
    content.appendChild(button);
  });
})();
