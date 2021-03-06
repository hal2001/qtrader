from __future__ import absolute_import
from __future__ import division

import numpy as np

from qtrader.agents._base import Agent


class RandomAgent(Agent):
    """Random agent."""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()
