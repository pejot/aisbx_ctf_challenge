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
from ctf_tests.base_test_case import BaseTestCase
import unittest


class CoordinatesCalcualtorTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(CoordinatesCalcualtorTestCase, self).setUpClass()

    def test_get_flaking_left_coordinates(self):
        reference_position = None
        flanked_position = None
        CoordinatesCalculator.get_flanking_left_coordinates(
            reference_position, flanked_position)
        # implement me :-)
        pass

    def test_get_flanking_right_coordiantes(self):
        reference_position = None
        flanked_position = None
        CoordinatesCalculator.get_flanking_right_coordinates(
            reference_position, flanked_position)
        # implement me :-)
        pass

if __name__ == '__main__':
    unittest.main()
