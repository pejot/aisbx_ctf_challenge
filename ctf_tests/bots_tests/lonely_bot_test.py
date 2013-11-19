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
        self.bot = None

    def test_constructor(self):
        """Should create and instance if parameters lists is complete."""
        self.assertRaises(TypeError, LonelyBot)
        lonelyBot = LonelyBot(self.bot)
        self.assertEqual(lonelyBot.bot, self.bot)

if __name__ == '__main__':
    unittest.main()
