#!/usr/bin/env python
from operational_unit import OperationalUnit


class LonelyBot(OperationalUnit):

    """
    Single independent bot or member of the group.
    """

    def __init__(self, bot):
        self.bot = bot
        self.current_state = None

    @property
    def visibleEnemies(self):
        pass

    @property
    def seenBy(self):
        pass

    @property
    def position(self):
        pass

    @property
    def alives(self):
        alives_array = []
        if self.bot.health > 0:
            alives_array.append(self.bot)
        return alives_array


    def get_bot_state(self, gameinfo):
        if bot.health < 0:
            return OperationalUnit.State.DEAD
        elif self.bot in gameinfo.bots_available:
            return OperationalUnit.State.AVAILABLE
        else:
            return OperationalUnit.State.BUSY