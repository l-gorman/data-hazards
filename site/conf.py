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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Data Hazards"
copyright = "2021, Natalie Thurlby and Nina Di Cara"
author = "Natalie Thurlby and Nina Di Cara"

# The full version, including alpha/beta/rc tags
release = "v0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/very-good-science/data-hazards",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Open Science Framework",
            "url": "https://osf.io/3fv7t",
            "icon": "fas fa-book-open",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/hashtag/DataHazards",
            "icon": "fab fa-twitter-square",
        },
    ],
    "search_bar_text": "Search this site...",
    "show_prev_next": False,
    "footer_items": ["license-footer", "sphinx-version"],
    "navbar_end": ["navbar-icon-links"], # removes light/dark mode
    "logo": {
        "text": "Data Hazards",
    },
}

html_context = {
   "default_mode": "light"
}

html_sidebars = {
    "index": [],
    "contents/data-hazards": [],
    "contents/sign-up": [],
    "contents/contact": [],
}

html_favicon = "_static/favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("custom.css")

