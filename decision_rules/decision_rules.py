#!/usr/bin/env python
import abc


class DecisionRules:

    """
    The abstract interface for decision rules engine.
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def conclude(self, actions, events):
        pass
