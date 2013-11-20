#!/usr/bin/env python
import os
import sys
from api.vector2 import Vector2


class CoordinatesCalculator:

    """
    Set of methods for order coordinates calculation.
    """

    @classmethod
    def get_flanking_left_coordinates(self, reference_position, flanked_position, firing_distance, action):
        # implement me :-)
        return Vector2(0, 0)

    @classmethod
    def get_flanking_right_coordinates(self, reference_position, flanked_position, firing_distance, action):
        # implement me :-)
        return Vector2(0, 0)
