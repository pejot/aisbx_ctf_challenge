import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from decision_rules.flanking_decision_rules import FlankingDecisionRules
from ctf_tests.bots_tests.bot_mock import BotMock
from actions.action import Action
from events.event import Event


class FlankingDecisionRulesTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(FlankingDecisionRulesTestCase, self).setUpClass()
        self.bot1 = BotMock("bot1", 10)
        self.bot2 = BotMock("bot2", 10)
        self.action1 = {
            self.bot1: Action(Action.ActionType.PREPARE_FLANKING_LEFT)}
        self.action2 = {
            self.bot2: Action(Action.ActionType.PREPARE_FLANKING_RIGHT)}
        self.event1 = {self.bot1: Event(Event.EventType.STATUS_HAS_CHANGED)}
        self.event2 = {self.bot2: Event(Event.EventType.STATUS_HAS_CHANGED)}

    def test_conclude_flaking_preapred(self):
        """ Should give new orders."""
        actions = [self.action1, self.action2]
        events = [self.event1, self.event2]
        new_actions = FlankingDecisionRules.conclude(actions, events)
        self.assertEqual(2, len(new_actions))
        self.assertEqual(0, len(actions))
        self.assertEqual(0, len(events))

    def test_conclude_flaking_not_preapred_yet(self):
        """ Should not give any new orders yet. """
        actions = [self.action1, self.action2]
        events = []
        new_actions = FlankingDecisionRules.conclude(actions, events)
        self.assertEqual(0, len(new_actions))
        self.assertEqual(2, len(actions))
        self.assertEqual(0, len(events))

if __name__ == '__main__':
    unittest.main()
