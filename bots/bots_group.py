#!/usr/bin/env python
from operational_unit import OperationalUnit

class BotsGroup(OperationalUnit):

    """
    The group of cooperating bots.
    """

    def __init__(self, name, bots_array):
        self.name = name
        self.members = bots_array
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
        for member in self.members:
            if member.health > 0:
                alives_array.append(member)
        return alives_array


    #THE WORST METHOD EVER! FIX ME!
    def get_bot_state(self, gameinfo):
        state = None
        for bot in self.members:
            if state == None:
                if bot.health < 0:
                    state = OperationalUnit.State.DEAD
                elif bot in gameinfo.bots_available:
                    state = OperationalUnit.State.AVAILABLE
                else:
                    state = OperationalUnit.State.BUSY
            else: 
                if bot.health < 0:
                    continue # ingore deads
                elif bot in gameinfo.bots_available:
                   if state != OperationalUnit.State.AVAILABLE:
                        return self.current_state # let them stabilize
                else:
                    if state != OperationalUnit.State.BUSY:
                        return self.current_state # let them stabilize

        if state == None:
            #we are dead
            return State.DEAD
        return state


