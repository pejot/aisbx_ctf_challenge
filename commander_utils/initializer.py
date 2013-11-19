#!/usr/bin/env python
from bots.bots_group import BotsGroup
from bots.lonely_bot import LonelyBot


class Initializer:

    """
    Set of helpers for commander init.
    """

    @classmethod
    def init_operation_units(self, strategy, members):
        units = []
        bots_available_index = 0

        self.helpers.check_appropriate_bots_number(strategy, members)

        for unit in strategy:
            if unit["bots_number"] == 1:
                units.append(LonelyBot(members[bots_available_index]))
                bots_available_index += 1
            else:
                bots_array = []
                for index in range(unit["bots_number"]):
                    bots_array.append(members[bots_available_index])
                    bots_available_index += 1
                units.append(BotsGroup(unit["name"], bots_array))
        return units

    class Helpers:

        """
        Initializer class helpers set.
        """

        def check_appropriate_bots_number(self, strategy, members):
            """ Helper for checking paramters correctness. """
            bots_number = 0
            for unit in strategy:
                bots_number += unit["bots_number"]
            if bots_number != len(members):
                raise ValueError(
                    "Number of bots in config isn't equal to team mebers number")

    helpers = Helpers()
