/* Prototype for docs/_static/footnote-popover.js (register with html_js_files).
   Hover / keyboard focus / first tap on a footnote marker shows the footnote's own text,
   links included, in a small card beside the marker. No dependency; works with docutils'
   <a class="footnote-reference" href="#label"> and <aside class="footnote" id="label">. */
document.addEventListener("DOMContentLoaded", () => {
  let card = null, owner = null, hideTimer = null;
  const hide = () => { if (card) { card.remove(); card = null; owner = null; } };
  const hideSoon = () => { hideTimer = setTimeout(hide, 250); };
  const keep = () => clearTimeout(hideTimer);
  function show(a) {
    keep();
    if (owner === a) return;
    hide();
    const note = document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
    if (!note) return;
    card = document.createElement("div");
    card.className = "fn-popover";
    card.setAttribute("role", "note");
    note.querySelectorAll(":scope > p, :scope > ul, :scope > ol").forEach(n => card.appendChild(n.cloneNode(true)));
    document.body.appendChild(card);
    const r = a.getBoundingClientRect(), w = Math.min(420, window.innerWidth - 16);
    card.style.width = w + "px";
    card.style.left = Math.max(8, Math.min(r.left + window.scrollX - 20, window.scrollX + window.innerWidth - w - 8)) + "px";
    card.style.top = (r.bottom + window.scrollY + 6) + "px";
    card.addEventListener("mouseenter", keep);
    card.addEventListener("mouseleave", hideSoon);
    owner = a;
  }
  document.querySelectorAll("a.footnote-reference").forEach(a => {
    a.addEventListener("mouseenter", () => show(a));
    a.addEventListener("mouseleave", hideSoon);
    a.addEventListener("focus", () => show(a));
    a.addEventListener("blur", hideSoon);
    a.addEventListener("click", e => {            // touch: first tap previews, second tap jumps
      if (window.matchMedia("(hover: none)").matches && owner !== a) { e.preventDefault(); show(a); }
    });
  });
  document.addEventListener("keydown", e => { if (e.key === "Escape") hide(); });
  document.addEventListener("click", e => { if (card && !card.contains(e.target) && !e.target.closest("a.footnote-reference")) hide(); });
});
