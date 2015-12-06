# -*- encoding: utf-8 -*-
# ! python2

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

"""Tests for django-custom-500's decorators"""

import unittest
import requests
from django.test import TestCase, LiveServerTestCase


class NormalViewTestCase(TestCase):
    def test_normal_view(self):
        ok_response = self.client.get('/normal-view-that-returns-data')

        self.assertTrue('42' in ok_response.content)


class InternalErrorTestCase(LiveServerTestCase):
    def test_error_view(self):
        error_response = requests.get('%s%s' % (self.live_server_url, '/view-that-raises-value-error'))

        self.assertEqual(error_response.status_code, 500)
        self.assertIn("500 Internal Server Error", error_response.content)


if __name__ == "__main__":
    unittest.main()
