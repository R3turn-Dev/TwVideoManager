# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import re
import sys

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'TwVideoManager'
copyright = '2019, return0927'
author = 'return0927'


with open("../TwVideoManager/constants.py") as f:
    data = f.read()
    version = re.search(r'^__VERSION__\s=\s[\'"]([^\'"]*)[\'"]', data, re.MULTILINE).group(1)

    if version.endswith(("a", "b", "rp")):
        version += "-" + re.search(r'^__DATE__\s=\s[\'"](\d+)[\'"]', data, re.MULTILINE).group(1)


release = version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

autodoc_mock_imports = ['python-twitch-twitch', 'twitch', ]

master_doc = 'index'
html_theme = 'sphinx_rtd_theme'