"""epsilon-Greedy Policy"""

from Policy import *
import numpy as np

__copyright__ = "Copyright 2013, RLPy http://www.acl.mit.edu/RLPy"
__credits__ = ["Alborz Geramifard", "Robert H. Klein", "Christoph Dann",
               "William Dabney", "Jonathan P. How"]
__license__ = "BSD 3-Clause"
__author__ = "Alborz Geramifard"

class eGreedy(Policy):
    epsilon         = None
    old_epsilon     = None
    forcedDeterministicAmongBestActions = None # This boolean variable is used to avoid random selection among actions with the same values
    def __init__(self,representation,logger,epsilon = .1,
                 forcedDeterministicAmongBestActions = False):
        self.epsilon = epsilon
        self.forcedDeterministicAmongBestActions = forcedDeterministicAmongBestActions
        super(eGreedy,self).__init__(representation,logger)
        if self.logger:
            self.logger.log("=" * 60)
            self.logger.log("Policy: eGreedy")
            self.logger.log("Epsilon\t\t{0}".format(self.epsilon))

    def pi(self,s, terminal, p_actions):
        coin = random.rand()
        #print "coin=",coin
        if coin < self.epsilon:
            return np.random.choice(p_actions)
        else:
            b_actions = self.representation.bestActions(s, terminal, p_actions)
            if self.forcedDeterministicAmongBestActions:
                return b_actions[0]
            else:
                return np.random.choice(b_actions)

    def turnOffExploration(self):
        self.old_epsilon = self.epsilon
        self.epsilon = 0
    def turnOnExploration(self):
        self.epsilon = self.old_epsilon




