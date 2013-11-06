#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from bots.operational_unit import OperationalUnit


class OperationalUnitTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(OperationalUnitTestCase, self).setUpClass()

    def test_abstract_nature(self):
        """Abstract class shouldn't be initalize."""
        self.assertRaises(TypeError, OperationalUnit)

if __name__ == '__main__':
    unittest.main()
