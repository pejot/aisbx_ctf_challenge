#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from bots.bots_group import BotsGroup
from bot_mock import BotMock


class BotsGroupTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(BotsGroupTestCase, self).setUpClass()
        self.bots_group_name = "bots_group_name"

    def test_constructor(self):
        """Should create and instance if parameters lists is complete."""
        self.assertRaises(TypeError, BotsGroup)
        bot_1 = BotMock("bot1", 2)
        bot_2 = BotMock("bot2", 4)
        bots_group = BotsGroup(
            self.bots_group_name, [bot_1, bot_2])
        self.assertEqual(bots_group.name, self.bots_group_name)
        self.assertIn(bot_1, bots_group.members)
        self.assertIn(bot_2, bots_group.members)

    def test_alives_property(self):
        """ Should gives the correct alives property. """
        bot_1 = BotMock("bot1", 10)
        bot_2 = BotMock("bot2", 0)
        bots_group = BotsGroup(
            self.bots_group_name, [bot_1, bot_2])
        self.assertEqual(1, len(bots_group.alives))

    def test_get_bot_state(self):
        # implement me!
        pass

    def test_report(self):
        # implement me!
        pass

if __name__ == '__main__':
    unittest.main()
