# -*- encoding: utf-8 -*-
# ! python2

"""URLs for django-annoying's tests"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^normal-view-that-returns-data$', views.normal_view),
    url(r'^view-that-raises-value-error', views.broken_view),
]
