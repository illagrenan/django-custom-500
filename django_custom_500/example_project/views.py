# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.http import HttpResponse


def normal_view(request):
    return HttpResponse("42")


def broken_view(request):
    raise ValueError("Something happened")
