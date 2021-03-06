#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from actions.action import Action


class ActionTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ActionTestCase, self).setUpClass()

    def test_constructor(self):
        """ Should be correctly initialize with paramters."""
        value = "value"
        action = Action(
            Action.ActionType.PREPARE_FLANKING_LEFT, param="value")
        self.assertIsNotNone(action)
        self.assertEqual(
            action.action_type, Action.ActionType.PREPARE_FLANKING_LEFT)
        self.assertEqual(
            action.kwargs['param'], value)

if __name__ == '__main__':
    unittest.main()
