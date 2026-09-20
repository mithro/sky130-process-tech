project = "figure test"
extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = ["colon_fence", "deflist", "attrs_inline"]
html_theme = "furo"
nitpicky = True
exclude_patterns = ["_build"]
html_static_path = ["_static"]
html_js_files = ["figure-theme.js"]
