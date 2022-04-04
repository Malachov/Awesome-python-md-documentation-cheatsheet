"""Sphinx config.

Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from __future__ import annotations
import datetime
import pathlib
import sys

# Folders to sys path to be able to import
script_dir = pathlib.Path(__file__).resolve()
root = script_dir.parents[2]

for i in [script_dir, root]:
    if i.as_posix() not in sys.path:
        sys.path.insert(0, i.as_posix())


# Settings
AUTHOR = "Daniel Malachov"
GITHUB_USER = "Malachov"

# -- Project information -----------------------------------------------------

copyright = f"2020, {AUTHOR}"  # pylint: disable=redefined-builtin

# The full version, including alpha/beta/rc tags
release = datetime.datetime.now().strftime("%d-%m-%Y")

master_doc = "index"  # pylint: disable=invalid-name

source_suffix = [".rst", ".md"]

# -- General configuration ---------------------------------------------------
html_theme_options = {
    "github_user": GITHUB_USER,
    "github_repo": "docs",
    "github_banner": True,
}


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.autosectionlabel",
    # "m2r2",
    "myst_parser",
]

# 'about.html',
html_sidebars = {"**": ["navi.html", "searchbox.html"]}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"  # pylint: disable=invalid-name

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_extra_path = ['../extra']

html_css_files = [
    "https://malachov.github.io/mypythontools/tools/sphinx-alabaster-css/custom.css",
]
