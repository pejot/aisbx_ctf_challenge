#!/usr/bin/env python
from actions.action import Action

FLANKING_STRATEGY = [
    {
        "name": "alpha",
        "bots_number": 2,
        "initial_action": Action(Action.ActionType.PREPARE_FLANKING_LEFT, flanking_distance = 0.6)
    },
    {
        "name": "bravo",
        "bots_number": 2,
        "initial_action": Action(Action.ActionType.PREPARE_FLANKING_RIGHT, flanking_distance = 0.6)
    }
]
