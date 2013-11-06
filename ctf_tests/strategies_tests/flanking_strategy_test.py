#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from strategies.flanking_strategy import FLANKING_STRATEGY


class FlankingStrategyTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(FlankingStrategyTestCase, self).setUpClass()

    def test_strategy_completness(self):
        """The strategy should contain all properties."""
        for group_description in FLANKING_STRATEGY:
            self.assertIn("name", group_description)
            self.assertIn("bots_number", group_description)
            self.assertIn("initial_action", group_description)


if __name__ == '__main__':
    unittest.main()
