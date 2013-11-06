#!/usr/bin/env python
from operational_unit import OperationalUnit


class LonelyBot(OperationalUnit):

    """
    Single independent bot.
    """

    @property
    def visibleEnemies(self):
        pass

    @property
    def seenBy(self):
        pass

    @property
    def position(self):
        pass
