#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
# TODO
# this is realy dirty hack preapre test runner to load what is needed!
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'CaptureTheFlag'))
sys.path.append(os.path.join(APP_ROOT))
from commander_utils.coordinates_calculator import CoordinatesCalculator
from actions.action import Action
from ctf_tests.base_test_case import BaseTestCase
from api.vector2 import Vector2
import unittest


class CoordinatesCalcualtorTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(CoordinatesCalcualtorTestCase, self).setUpClass()
        # methods are stateless so it's enough to initiate once
        self.coordinates_calculator = CoordinatesCalculator()

    def test_get_flaking_coordinates(self):
        reference_position = Vector2(0, 0)
        flanked_position = Vector2(0, 10)
        firing_distance = 5
        action_left = Action(
            Action.ActionType.PREPARE_FLANKING_LEFT, flanking_distance=1.0)
        action_rigth = Action(
            Action.ActionType.PREPARE_FLANKING_RIGHT, flanking_distance=1.0)
        flanking_left = self.coordinates_calculator.get_flanking_coordinates(
            reference_position, flanked_position, firing_distance, action_left)
        flanking_rigth = self.coordinates_calculator.get_flanking_coordinates(
            reference_position, flanked_position, firing_distance, action_rigth)
        self.assertEqual(flanking_rigth[0].x, -flanking_left[0].x)
        self.assertEqual(flanking_rigth[1].x, -flanking_left[1].x)
        self.assertEqual(flanking_rigth[0].y, flanking_left[0].y)
        self.assertEqual(flanking_rigth[1].y, flanking_left[1].y)

if __name__ == '__main__':
    unittest.main()
