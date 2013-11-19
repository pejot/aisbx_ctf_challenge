#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from bots.bots_group import BotsGroup
from bots.lonely_bot import LonelyBot


class BotsGroupTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(BotsGroupTestCase, self).setUpClass()
        self.bots_group_name = "bots_group_name"

    def test_constructor(self):
        """Should create and instance if parameters lists is complete."""
        self.assertRaises(TypeError, BotsGroup)
        lonely_bot_1 = LonelyBot("name")
        lonely_bot_2 = LonelyBot("name2")
        bots_group = BotsGroup(
            self.bots_group_name, [lonely_bot_1, lonely_bot_2])
        self.assertEqual(bots_group.name, self.bots_group_name)
        self.assertIn(lonely_bot_1, bots_group.members)
        self.assertIn(lonely_bot_2, bots_group.members)

if __name__ == '__main__':
    unittest.main()
