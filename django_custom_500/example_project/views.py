# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.http import HttpResponse


def ajax_request_httpresponse_view(request):
    return HttpResponse("42")


def aaaa(request):
    raise ValueError("Something happened")
