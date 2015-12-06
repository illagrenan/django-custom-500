# -*- encoding: utf-8 -*-
# ! python2

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

if "nosetests" in sys.argv[0]:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_custom_500.example_project.settings")

    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()
