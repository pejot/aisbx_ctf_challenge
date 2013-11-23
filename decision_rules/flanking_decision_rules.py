from actions.action import Action
from events.event import Event


class FlankingDecisionRules:

    """
    The decision rules dedicated to flanking chellange.
    """

    @classmethod
    def conclude(self, actions, events):
        # TODO
        # I'm too long, Fix me!
        # chech if flanking right and left were commadned and executed
        flanking_done = 0
        flanking_expected = 0
        actions_done = []
        events_serviced = []
        new_orders = []
        flanked_units = []
        for action in actions:
            key = action.keys()[0]
            if (action[key].action_type == Action.ActionType.PREPARE_FLANKING_LEFT or
                action[key].action_type == Action.ActionType.PREPARE_FLANKING_RIGHT):
                flanking_expected += 1
                flanked_units.append(key)
                actions_done.append(action)
            related_event = get_event_from_key(key, events)
            if related_event != None and related_event[key].event_type == Event.EventType.STATUS_HAS_CHANGED:
                flanking_done += 1
                events_serviced.append(related_event)
        if flanking_expected == flanking_done:
            # clear events and action
            for action in actions_done:
                actions.remove(action)
            for event in events_serviced:
                events.remove(event)
            for flanking_unit in flanked_units:
                new_orders.append(
                    {flanking_unit: Action(Action.ActionType.ATTACK_BASE)})
        return new_orders


def get_event_from_key(key, events):
    # assuem it's only once
    for event in events:
        if event.keys()[0] == key:
            return event
    return None
