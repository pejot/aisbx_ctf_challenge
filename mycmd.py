
#!/usr/bin/env python
"""
Start module for aisandbox CTF challenge
"""
__version__ = "0.0.1"
__author__ = "@pejot"

from api import commander
from strategies.flanking_strategy import FLANKING_STRATEGY
from commander_utils.initializer import Initializer
from commander_utils.coordinates_calculator import CoordinatesCalculator
from actions.action import ActionType
from api import orders


class MyCommander(commander.Commander):

    """
    The commander implemented for aisbx Flanking Challenge
    """

    def initialize(self):
        # for now just flanking startegy and nothing else - no cfg file
        self.strategy = FLANKING_STRATEGY
        self.operational_unit = Initializer.init_operation_units(
            self.strategy, self.game.team.members)
        self.first_tick = True

    def tick(self):
        if self.first_tick:
            self.first_tick = False
            self.__grant_initial_orders()

    def shutdown(self):
        pass

    def __grant_initial_orders(self):
        # TODO
        # it's too looong and contains code dupllications
        # fix me
        for i in range(len(self.strategy)):
            reference_point = self.level.botSpawnAreas[self.game.team.name]
            flanked_point = self.level.botSpawnAreas[self.game.enemyTeam.name]
            if self.strategy[i]["initial_action"].action_type == ActionType.PREPARE_FLANKING_LEFT:
                self.issue(orders.Move, self.operational_unit[i], CoordinatesCalculator.get_flanking_left_coordinates(
                    reference_point, flanked_point), description='Preparing flanking left')
            elif self.strategy[i]["initial_action"].action_type == ActionType.PREPARE_FLANKING_RIGHT:
                self.issue(orders.Move, self.operational_unit[i], CoordinatesCalculator.get_flanking_right_coordinates(
                    reference_point, flanked_point), description='Preparing flanking right')

    def issue(self, OrderClass, bot, *args, **dct):
        """ Override issue method. Created to address orders to both, single bot and group. """
        for alive in bot.alives:
            super(MyCommander, self).issue(OrderClass, alive, *args, **dct)
