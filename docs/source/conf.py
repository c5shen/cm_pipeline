# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CM++ Pipeline'
copyright = '2023, Vikram Ramavarapu, Fabio Jose Ayres, Minhyuk Park, Vidya Kamath Pailodi, Joao Alfredo Cardoso Lamy, Tandy Warnow, George Chacko'
author = 'Vikram Ramavarapu, Fabio Jose Ayres, Minhyuk Park, Vidya Kamath Pailodi, Joao Alfredo Cardoso Lamy, Tandy Warnow, George Chacko'
release = 'v4.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

extensions = ['myst_parser']

master_doc = 'index'
source_suffix = {
    '.md': 'markdown',
}

html_baseurl = 'cm_pipeline'