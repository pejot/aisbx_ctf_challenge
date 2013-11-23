
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
from actions.action import Action
from decision_rules.flanking_decision_rules import FlankingDecisionRules
from api import orders


class MyCommander(commander.Commander):

    """
    The commander implemented for aisbx Flanking Challenge
    """

    def initialize(self):
        # initialize vars
        self.current_actions = []
        self.current_events = []
        # initialize helpers
        self. coordinates_calculator = CoordinatesCalculator()
        # make it verbose
        self.verbose = True
        # for now just flanking startegy and nothing else - no cfg file
        self.strategy = FLANKING_STRATEGY
        self.operational_unit = Initializer.init_operation_units(
            self.strategy, self.game.team.members)
        self.initial_tick = True

    def tick(self):
        if self.initial_tick:
            self.initial_tick = False
            self.__grant_initial_orders()
            return
        reports = self.__collect_reports()
        if len(reports) > 0:
            self.current_events += reports
            new_actions = FlankingDecisionRules.conclude(
                self.current_actions, self.current_events)
            if len(new_actions) > 0:
                self.__grant_orders(new_actions)
        else:
            return

    def shutdown(self):
        pass

    def __collect_reports(self):
        reports = []
        for unit in self.operational_unit:
            report = unit.get_report(self.game)
            for single_report in report:
                reports.append({unit: single_report})
        return reports

    def __grant_orders(self, actions):
            for action in actions:
                key = action.keys()[0]
                if action[key].action_type == Action.ActionType.ATTACK_BASE:
                    self.current_actions.append(action)
                    flanked_point = self.level.botSpawnAreas[
                        self.game.enemyTeam.name]
                    attacked_point = (flanked_point[0] + flanked_point[1]) / 2
                    self.issue(orders.Attack, key, attacked_point,  description='Attacking base')

    def __grant_initial_orders(self):
        # TODO
        # it's too looong and contains code dupllications, fix me!
        for i in range(len(self.strategy)):
            # fillup_actions_array
            self.current_actions.append(
                {self.operational_unit[i]: self.strategy[i]["initial_action"]})
            reference_point = self.level.botSpawnAreas[self.game.team.name]
            # take the center own base
            reference_point = (reference_point[0] + reference_point[1]) / 2
            flanked_point = self.level.botSpawnAreas[self.game.enemyTeam.name]
            # take the center of flanked base
            flanked_point = (flanked_point[0] + flanked_point[1]) / 2
            firing_distance = self.level.firingDistance
            action_type = self.strategy[i]["initial_action"].action_type
            if action_type == Action.ActionType.PREPARE_FLANKING_LEFT or action_type == Action.ActionType.PREPARE_FLANKING_RIGHT:
                self.issue(orders.Move, self.operational_unit[i], self.coordinates_calculator.get_flanking_coordinates(
                    reference_point, flanked_point, firing_distance, self.strategy[i]["initial_action"]), description='Preparing flanking')

    def issue(self, OrderClass, bot, *args, **dct):
        """ Override issue method. Created to address orders to both, single bot and group. """
        for alive in bot.alives:
            super(MyCommander, self).issue(OrderClass, alive, *args, **dct)
