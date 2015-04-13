# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import sys
import os

if "nosetests" in sys.argv[0]:
    from django.core.wsgi import get_wsgi_application


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_custom_500.example_project.settings")

    application = get_wsgi_application()