#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from bots.lonely_bot import LonelyBot
from bot_mock import BotMock


class LonelyBotTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(LonelyBotTestCase, self).setUpClass()
        self.bot = BotMock(1)

    def test_constructor(self):
        """Should create and instance if parameters lists is complete."""
        self.assertRaises(TypeError, LonelyBot)
        lonelyBot = LonelyBot(self.bot)
        self.assertEqual(lonelyBot.bot, self.bot)

    def test_alives_property(self):
        bot_1 = BotMock(10)
        bot_2 = BotMock(0)
        lonely_bot = LonelyBot(bot_1)
        self.assertEqual(1, len(lonely_bot.alives))
        lonely_bot = LonelyBot(bot_2)
        self.assertEqual(0, len(lonely_bot.alives))


if __name__ == '__main__':
    unittest.main()
