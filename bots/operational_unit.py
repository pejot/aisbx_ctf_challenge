#!/usr/bin/env python
import abc
from events.event import Event
#!/usr/bin/env python

class OperationalUnit:

    """
    The abstract interface of bot or group bots depending on the implementation.
    Takes orders from the commander.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def visibleEnemies(self):
        pass

    @abc.abstractproperty
    def seenBy(self):
        pass

    @abc.abstractproperty
    def position(self):
        pass

    @abc.abstractproperty
    def alives(self):
        pass

    def get_bot_state(self, gameinfo):
        pass

    def get_report(self, gemeinfo):
        new_state = self.get_bot_state(gemeinfo)
        if self.current_state ==  new_state:
            return []
        else :
            if self.current_state == None:
                result = []
            else:
                result = [Event(Event.EventType.STATUS_HAS_CHANGED, old_state = self.current_state, new_state = new_state)]
            self.current_state = new_state
            return result
    
    class State:

        """
        The simplest possible states
        """

        BUSY = 1
        AVAILABLE = 2
        DEAD = 3