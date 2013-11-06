#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from actions.action import Action, ActionType


class ActionTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ActionTestCase, self).setUpClass()

    def test_constructor(self):
        """Abstract class shouldn't be initalize."""
        
        action = Action(ActionType.PREPARE_FLANKING_CENTER)
        self.assertIsNotNone(action)
        self.assertEqual(action.actionType, ActionType.PREPARE_FLANKING_CENTER)

if __name__ == '__main__':
    unittest.main()
