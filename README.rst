Django custom 500
=================

.. image:: https://badge.fury.io/py/django_custom_500.svg
        :target: https://pypi.python.org/pypi/django_custom_500
        :alt: PyPi

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://pypi.python.org/pypi/django_make_app/
        :alt: MIT

.. image:: https://api.travis-ci.org/illagrenan/django-custom-500.svg
        :target: https://travis-ci.org/illagrenan/django-custom-500
        :alt: TravisCI

.. image:: https://coveralls.io/repos/illagrenan/django-custom-500/badge.svg?branch=master
        :target: https://coveralls.io/r/illagrenan/django-custom-500?branch=master
        :alt: Coverage

.. image:: https://requires.io/github/illagrenan/django-custom-500/requirements.svg?branch=master
        :target: https://requires.io/github/illagrenan/django-custom-500/requirements/?branch=master
        :alt: Requirements Status

Installation
------------

Supported Python versions are: ``2.7``, ``3.4``, ``3.5``, ``3.6``, ``3.7`` and ``pypy``. Supported Django versions are: ``1.8.x``, ``1.9.x``, ``1.10.x`` and ``1.11.x``.

.. code:: bash

    pip install --upgrade django-custom-500

Add ``django_custom_500`` to ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = (
        'django_custom_500',
    )

Usage
-----

Create ``500.html`` in your ``template`` folder.

**OR**

Set ``CUSTOM_500_TEMPLATE`` in your settings.

Example:

.. code:: python

    CUSTOM_500_TEMPLATE = "my/path/to/500.html"

License
-------

The MIT License (MIT)

Copyright (c) 2015–2017 Vašek Dohnal

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
