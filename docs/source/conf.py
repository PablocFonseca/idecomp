# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import date
from typing import List
import plotly.io as pio

pio.renderers.default = "sphinx_gallery"

sys.path.insert(0, os.path.abspath("../../"))
from idecomp import __version__  # noqa: E402


# -- Project information -----------------------------------------------------

project = "idecomp"
copyright = f"{date.today().year}, Rogerio Alves"
author = "Rogerio Alves"

# The full version, including alpha/beta/rc tags
release = __version__
today = date.today().strftime("%d/%m/%Y")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_gallery.gen_gallery",
    "numpydoc",
    "sphinx_rtd_theme",
]


# generate autosummary pages
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "pt_BR"

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []

add_module_names = False
pygments_style = "sphinx"
modindex_common_prefix = ["idecomp."]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": True,
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_logo = "_static/logo_idecomp_svg.svg"

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "obj"

numpydoc_show_class_members = False
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/{.major}".format(sys.version_info),
        None,
    ),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "cfinterface": ("https://rjmalves.github.io/cfi/", None),
}

# https://github.com/sphinx-gallery/sphinx-gallery
sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": "../../examples",
    # path where to save gallery generated examples
    "gallery_dirs": "examples",
    "backreferences_dir": "gen_modules/generated",
}
