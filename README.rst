Django custom 500
=================

.. image:: https://badge.fury.io/py/django_custom_500.svg
        :target: https://pypi.python.org/pypi/django_custom_500
        :alt: PyPi

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

.. code:: bash

    pip install --upgrade django-custom-500

**Add ``django_custom_500`` to ``INSTALLED_APPS``:**

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
