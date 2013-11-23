#!/usr/bin/env python


# later may be refactor to many different types. For now there is no logic
# for that.
class Action:

    """
    The action carried out by operational unit.
    """

    def __init__(self, action_type, *args, **kwargs):
        # args and kwargs are additional paramters we will use them later
        # it's very complex and very flexible it isn't clear what will be done with the
        # Action class later on ...
        self.action_type = action_type
        self.args = args
        self.kwargs = kwargs

    class ActionType:

        """
        List of possible action types.
        """

        PREPARE_FLANKING_LEFT = 1
        PREPARE_FLANKING_RIGHT = 2
        ATTACK_BASE = 3
