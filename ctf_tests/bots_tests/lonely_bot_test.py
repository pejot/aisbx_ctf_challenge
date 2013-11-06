#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from bots.lonely_bot import LonelyBot


class LonelyBotTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(LonelyBotTestCase, self).setUpClass()

    def test_constructor(self):
        """Should create and instance."""
        lonelyBot = LonelyBot()
        self.assertIsNotNone(lonelyBot)

if __name__ == '__main__':
    unittest.main()
