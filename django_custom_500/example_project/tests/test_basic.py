# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

"""Tests for django-custom-500's decorators"""

import unittest

import requests

from django.test import TestCase, LiveServerTestCase


class RenderToTestCase(TestCase):
    def test_content_type_kwarg(self):
        response = self.client.get('/normal-view-that-returns-data')

        self.assertTrue('42' in response.content)


class ACase(LiveServerTestCase):
    def test_content_asdasrg(self):
        abc = requests.get('%s%s' % (self.live_server_url, '/view-that-raises-value-error'))

        self.assertEqual(abc.status_code, 500)
        self.assertIn("500 Internal Server Error", abc.content)


if __name__ == "__main__":
    unittest.main()