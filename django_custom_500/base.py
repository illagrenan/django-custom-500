# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

import django
from django.conf.urls.static import static
from django.conf import settings

django.conf.urls.handler500 = 'django_custom_500.handlers.handler500'
