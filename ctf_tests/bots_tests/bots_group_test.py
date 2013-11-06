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
        self.botsGroupName = "botsGroupName"

    def test_constructor(self):
        """Should create and instance if parameters lists is complete."""
        self.assertRaises(TypeError, BotsGroup)
        lonelyBot1 = LonelyBot("name")
        lonelyBot2 = LonelyBot("name2")
        botsGroup = BotsGroup(self.botsGroupName, [lonelyBot1, lonelyBot2])
        self.assertEqual(botsGroup.name, self.botsGroupName)
        self.assertIn(lonelyBot2, botsGroup.members)
        self.assertIn(lonelyBot1, botsGroup.members)

if __name__ == '__main__':
    unittest.main()
