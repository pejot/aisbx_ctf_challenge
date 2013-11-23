#!/usr/bin/env python
from api.vector2 import Vector2
from actions.action import Action


class CoordinatesCalculator:

    """
    Set of methods for order coordinates calculation.
    """

    def get_flanking_coordinates(self, reference_position, flanked_position, firing_distance, action):
        """ Caluclate bot, left and rught flanking coordiantes. """
        distance = (reference_position - flanked_position)
        right_normalized = Vector2(-distance.y, distance.x).normalized()
        left_normalized = Vector2(distance.y, -distance.x).normalized()
        front_normalized = Vector2(distance.x, distance.y).normalized()
        # calcualte flanked distance

        front = front_normalized * (distance.length() - (firing_distance * (action.kwargs["flanking_distance"])))
        # always a little bit on the left/right than in front so + 0.1
        right = right_normalized * (firing_distance * (0.2 + action.kwargs["flanking_distance"]))
        left = left_normalized * (firing_distance * (0.2 + action.kwargs["flanking_distance"]))

        if action.action_type == Action.ActionType.PREPARE_FLANKING_RIGHT:
            return [reference_position - front * 0.75 - right, reference_position - front - right]
        elif action.action_type == Action.ActionType.PREPARE_FLANKING_LEFT:
            return [reference_position - front * 0.75 - left, reference_position - front - left]
        return None
