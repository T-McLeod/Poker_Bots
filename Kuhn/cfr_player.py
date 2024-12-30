import random
import numpy as np
from enum import Enum
from .kuhn_poker import History, Action, Game, Player

class Player_Strategy(Player):

    def __init__(self):
        self.strategy: dict[History, dict[Action, float]] = {}

    def get_move(self, game_state: History, possible_actions: list[Action]):
        game_state_index = tuple(game_state)

        if game_state_index in self.strategy:
            actions = self.strategy[game_state_index].keys()
            weights = self.strategy[game_state_index].values()
            return np.random.choice(actions, p=weights)
        else:
            # select a random action and set the strategy to play it 100% of time
            self.strategy[game_state_index] = {action: 0 for action in possible_actions}
            action = random.randint(0, len(possible_actions))
            self.strategy[game_state_index][action] = 1
            return action