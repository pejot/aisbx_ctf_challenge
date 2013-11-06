#!/usr/bin/env python
import os
import unittest
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(APP_ROOT))


class BaseTestCase(unittest.TestCase):

    """
    Base test for all tests
    """

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass
