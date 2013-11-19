#!/usr/bin/env python
from operational_unit import OperationalUnit


class BotsGroup(OperationalUnit):

    """
    The group of cooperating bots.
    """

    def __init__(self, name, bots_array):
        self.name = name
        self.members = bots_array

    @property
    def visibleEnemies(self):
        pass

    @property
    def seenBy(self):
        pass

    @property
    def position(self):
        pass
