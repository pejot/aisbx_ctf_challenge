#!/usr/bin/env python
import abc


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
