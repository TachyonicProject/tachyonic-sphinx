==============================
Tachyonic Project Sphinx Theme
==============================

Quick Links
-----------

* `Website <http://www.tachyonic.org/>`__.

Installation
------------

Tachyonic currently fully supports `CPython <https://www.python.org/downloads/>`__ [ '3.5', '3.6' ].

Installation
============
Installation from PyPI is fairly straightforward:

1. Install the package::

      $ pip install tachyonic-sphinx

2. Edit the "conf.py" configuration file to point to the bootstrap theme::

      # At the top.
      import tachyonic_sphinx

      # ...

      # Activate the theme.
      html_theme = 'tachyonic'
      html_theme_path = tachyonic_sphinx.get_html_theme_path()
