import random
import numpy as np
from enum import Enum
from ..kuhn_poker import History, Action, Game, Player, Card

class Game_Strategy(Player):

    def __init__(self):
        self.strategy: dict[History, dict[Action, float]] = {}
        self.information_set: list[Action | Card] = []

    def get_move(self, possible_actions: list[Action]):
        information_state_index = tuple(self.information_set)
        print("Information state index: ", information_state_index)

        if information_state_index in self.strategy:
            actions = self.strategy[information_state_index].keys()
            weights = self.strategy[information_state_index].values()
            return np.random.choice(actions, p=weights)
        else:
            # select a random action and set the strategy to play it 100% of time
            self.strategy[information_state_index] = {action: 0 for action in possible_actions}
            action = np.random.choice(possible_actions)
            self.strategy[information_state_index][action] = 1
            print(action)
            return action
        
    def inform(self, event):
        self.information_set.append(event)