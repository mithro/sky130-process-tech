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
html_theme_options = {
    "source_repository": "https://github.com/mithro/sky130-process-tech/",
    "source_branch": "main",
    "source_directory": "docs/",
}
