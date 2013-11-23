#!/usr/bin/env python


class Event:

    """
    The action carried out by operational unit.
    """

    def __init__(self, event_type, *args, **kwargs):
        # args and kwargs are additional paramters we will use them later
        # it's very complex and very flexible it isn't clear what will be done with the
        # Event class later on ...
        self.event_type = event_type
        self.args = args
        self.kwargs = kwargs

    class EventType:

        """
        List of possible event types.
        """
        STATUS_HAS_CHANGED = 1
