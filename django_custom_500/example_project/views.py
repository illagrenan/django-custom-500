# -*- encoding: utf-8 -*-
# ! python2

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.http import HttpResponse


def normal_view(request):
    return HttpResponse("42")


def broken_view(request):
    raise ValueError("Something happened")
