# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import django
from django.conf.urls.static import static
from django.conf import settings

django.conf.urls.handler500 = 'django_custom_500.handlers.handler500'
