# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys

import six

if not six.PY2:
    print("Run Fabfile only under Python 2.x")
    sys.exit(0)

from fabric.context_managers import settings

from fabric.contrib.console import confirm
from fabric.decorators import task
from fabric.operations import local


@task()
def test_install():
    with settings(warn_only=True):
        local("pip uninstall django_custom_500 --yes")
        print("Uninstall OK.")

    local("pip install --use-wheel --no-index --find-links dist django_custom_500")
    local("pip uninstall django_custom_500 --yes")

    print("Install OK.")


@task()
def test():
    local("nosetests --with-coverage --cover-package=django_custom_500 --cover-tests --cover-erase --with-doctest --nocapture")

    print("Test OK.")


@task()
def build():
    local("python setup.py build")
    local("python setup.py sdist")
    local("python setup.py bdist_wheel")
    local("python setup.py bdist_wininst")

    print("Build OK.")


@task()
def publish():
    if confirm(u'Really publish?', default=False):
        local('python setup.py sdist upload -r pypi')
        local('python setup.py bdist_wheel upload -r pypi')

        print("Published.")
