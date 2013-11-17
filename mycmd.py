
#!/usr/bin/env python
"""
Start module for aisandbox CTF challenge
"""
__version__ = "0.0.1"
__author__ = "@pejot"

from api import commander
from strategies.flanking_strategy import FLANKING_STRATEGY

class MyCommander(commander.Commander):

    """
    This default AI implementation will not do anything.
    All bots remain idle at their spawn location.
    """

    # Called once when this commander is being initialized.
    def initialize(self):
        pass

    # Here you put the main AI logic of your commander.
    def tick(self):
        pass

    # Called once when the match ends.
    def shutdown(self):
        pass
