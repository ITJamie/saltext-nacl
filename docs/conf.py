"""Documentation configuration."""

from importlib.metadata import version as distribution_version

project = "saltext.nacl"
author = "Jamie (Bear) Murphy"
copyright = "2026, Jamie (Bear) Murphy and Salt Project contributors"
release = distribution_version("saltext.nacl")
extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx.ext.viewcode"]
html_theme = "furo"
exclude_patterns = ["_build"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
master_doc = "index"
