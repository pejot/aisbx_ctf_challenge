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
        #methods are stateless so it's enough to initiate once
        self.coordinates_calculator = CoordinatesCalculator()

    def test_get_flaking_coordinates(self):
        reference_position = None
        flanked_position = None
        firing_distance = None
        action = None
        #self.coordinates_calculator.get_flanking_coordinates(
        #    reference_position, flanked_position, firing_distance, action)
        # implement me :-)
        pass
if __name__ == '__main__':
    unittest.main()
