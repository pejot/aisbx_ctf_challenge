#!/usr/bin/env python
import os
import sys
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(os.path.join(APP_ROOT))
import unittest
from ctf_tests.base_test_case import BaseTestCase
from events.event import Event


class ActionTestCase(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(ActionTestCase, self).setUpClass()

    def test_constructor(self):
        """ Should be correctly initialize with paramters."""
        value = "value"
        event = Event(
            Event.EventType.STATUS_HAS_CHANGED, param="value")
        self.assertIsNotNone(event)
        self.assertEqual(
            event.event_type, Event.EventType.STATUS_HAS_CHANGED)
        self.assertEqual(
            event.kwargs['param'], value)

if __name__ == '__main__':
    unittest.main()
