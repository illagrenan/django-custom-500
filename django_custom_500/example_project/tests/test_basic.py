# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

import unittest

import requests
from django.test import TestCase, LiveServerTestCase


class NormalViewTestCase(TestCase):
    def test_normal_view(self):
        ok_response = self.client.get('/normal-view-that-returns-data')

        self.assertIn('42', str(ok_response.content))


class InternalErrorTestCase(LiveServerTestCase):
    def test_error_view(self):
        error_response = requests.get('%s%s' % (self.live_server_url, '/view-that-raises-value-error'))

        self.assertEqual(error_response.status_code, 500)
        self.assertIn("500 Internal Server Error", str(error_response.content))


if __name__ == "__main__":
    unittest.main()
