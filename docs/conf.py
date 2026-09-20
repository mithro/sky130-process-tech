# Sphinx configuration for the SKY130 process technology documentation.

project = "SKY130 Process Technology"
copyright = "2026, the SKY130 process technology documentation contributors"
author = "SKY130 process technology documentation contributors"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

master_doc = "index"

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "plans/**",
]

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
    "attrs_inline",
]
myst_heading_anchors = 3

# Every step, machine, material and mask page must be reachable, so we
# want Sphinx to complain loudly about broken cross-references.
nitpicky = True

# HTML
html_theme = "furo"
html_title = "SKY130 Process Technology"
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = ["announcement-dismiss.css", "custom.css"]
# footnote-popover: hover card for footnote markers. figure-theme: swaps a figure to its
# forced light/dark file when the reader uses furo's toggle.
html_js_files = ["footnote-popover.js", "figure-theme.js"]
# Shown by the theme at the top of every rendered page.
announcement = "Warning: AI in use — use at own risk."

html_theme_options = {
    "announcement": announcement,
    "source_repository": "https://github.com/mithro/sky130-process-tech/",
    "source_branch": "main",
    "source_directory": "docs/",
    # "navigation_with_keys" (C12 listed it as optional polish) was tried
    # and dropped: Sphinx's own doctools.js sends every unmodified
    # ArrowLeft/ArrowRight to previous/next-page navigation except inside
    # a handful of form controls, so it hijacks the arrow keys a reader
    # uses to scroll one of this site's many horizontally-scrollable
    # tables sideways (review finding M3, 2026-09-20).
}
