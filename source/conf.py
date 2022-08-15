# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'X-NOTES'
copyright = '2022, JinDao'
author = 'JinDao'
release = 'latest'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

#添加markdown支持
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
    'sphinx_markdown_tables'
]

#更改主题
#默认
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


#awesom
# html_permalinks_icon = '<span>#</span>'
# html_theme = 'sphinxawesome_theme'

# #Maisie Sample
# import maisie_sphinx_theme
# extensions.append("maisie_sphinx_theme")
# html_theme = 'maisie_sphinx_theme'
# html_theme_path = maisie_sphinx_theme.html_theme_path()

# #Furo
# html_theme = 'furo'

#Press
# html_theme = 'press'
