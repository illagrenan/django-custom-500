# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^normal-view-that-returns-data$', views.normal_view),
    url(r'^view-that-raises-value-error', views.broken_view),
]
