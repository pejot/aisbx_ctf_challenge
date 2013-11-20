#!/usr/bin/env python
from actions.action import Action, ActionType


FLANKING_STRATEGY = [
    {
        "name": "alpha",
        "bots_number": 2,
        "initial_action": Action(ActionType.PREPARE_FLANKING_LEFT)
    },
    {
        "name": "bravo",
        "bots_number": 2,
        "initial_action": Action(ActionType.PREPARE_FLANKING_RIGHT)
    }
]
