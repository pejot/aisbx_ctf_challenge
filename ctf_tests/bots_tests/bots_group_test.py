#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from bots.bots_group import BotsGroup


class BotsGroupTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(BotsGroupTestCase, self).setUpClass()

    def test_constructor(self):
        """Should create and instance."""
        botsGroup = BotsGroup()
        self.assertIsNotNone(botsGroup)

if __name__ == '__main__':
    unittest.main()
