#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from decision_rules.decision_rules import DecisionRules


class DecisionRulesTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(DecisionRulesTestCase, self).setUpClass()

    def test_abstract_nature(self):
        """Abstract class shouldn't be initalize."""
        self.assertRaises(TypeError, DecisionRules)

if __name__ == '__main__':
    unittest.main()
