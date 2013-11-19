#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
from ctf_tests.base_test_case import BaseTestCase
from commander_utils.initializer import Initializer
from strategies.flanking_strategy import FLANKING_STRATEGY
from bots.bots_group import BotsGroup
from bots.lonely_bot import LonelyBot
import unittest

SIMPLE_STRATEGY = [
    {
        "name": "alpha",
        "bots_number": 2,
        "initial_action": None
    },
    {
        "bots_number": 1,
        "initial_action": None
    }
]


class InitializerTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(InitializerTestCase, self).setUpClass()

    def test_init_strategy(self):
        members = [None, None, None, None]
        bots_array = Initializer.init_operation_units(
            FLANKING_STRATEGY, members)
        self.assertEqual(2, len(bots_array))
        self.assertTrue(isinstance(bots_array[0], BotsGroup))
        self.assertTrue(isinstance(bots_array[1], BotsGroup))

    def test_init_simple_strategy(self):
        members = [None, None, None]
        bots_array = Initializer.init_operation_units(
            SIMPLE_STRATEGY, members)
        self.assertEqual(2, len(bots_array))
        self.assertTrue(isinstance(bots_array[0], BotsGroup))
        self.assertTrue(isinstance(bots_array[1], LonelyBot))

    def test_init_with_wrong_parameters(self):
        members = [None, None]
        self.assertRaises(
            ValueError, Initializer.init_operation_units, SIMPLE_STRATEGY, members)


if __name__ == '__main__':
    unittest.main()
