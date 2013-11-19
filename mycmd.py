
#!/usr/bin/env python
"""
Start module for aisandbox CTF challenge
"""
__version__ = "0.0.1"
__author__ = "@pejot"

from api import commander
from strategies.flanking_strategy import FLANKING_STRATEGY
from commander_utils.initializer import Initializer


class MyCommander(commander.Commander):

    """
    The commander implemented for aisbx Flanking Challenge
    """

    def initialize(self):
        # for now just flanking startegy and nothing else - no cfg file
        self.strategy = FLANKING_STRATEGY
        self.operational_unit = Initializer.init_operation_units(
            self.strategy, self.game.team.members)
        self.first_tick=True

    def tick(self):
        if self.first_tick:
            self.first_tick = False
            return

    def shutdown(self):
        pass
