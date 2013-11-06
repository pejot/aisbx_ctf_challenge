#!/usr/bin/env python


class ActionType:

    """
    List of possible action types.s
    """
    PREPARE_FLANKING_LEFT = 1
    PREPARE_FLANKING_RIGH = 2
    PREPARE_FLANKING_CENTER = 3


# later may be refactor to many different types. For now there is no logic
# for that.
class Action:

    """
    The action carried out by operational unit.
    """

    def __init__(self, actionType, *args, **kwargs):
        # args and kwargs are additional paramters we will use them later
        self.actionType = actionType
