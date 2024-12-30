import random
import numpy as np
from enum import Enum

class Action(Enum):
    FOLD = 0
    CHECK = 1
    CALL = 2
    RAISE = 3

Card = int
History = list[Card | Action]

class Player:
    def get_move(self, game_state: History, possible_actions: list[Action]) -> Action:
        pass

class Game():

    def __init__(self):
        self.history: History = []
        self.deck = [x+1 for x in range(3)]
        self.pot = 2

        self.player1_card = -1
        self.player2_card = -1
        self.player1_strategy = Player()
        self.player2_strategy = Player()
    
    def random_function(self, i: int):
        return random.randint(0, i-1)
    
    def draw_card(self) -> Card:
        i = self.random_function(len(self.deck))
        self.history.append(i)

        return self.deck.pop(i)

    def get_move(self, player_strategy: Player, possible_moves: list[Action]) -> Action:
        action = player_strategy.get_move(self.history, possible_moves)
        self.history.append(action)
        if action == Action.CALL or action == Action.RAISE:
            self.pot += 1
        return action
    
    def determine_winner(self):
        if self.player1_card > self.player2_card:
            print(f"Player 1 wins {self.pot} chips with {self.player1_card} over {self.player2_card} {self.history}")
        else:
            print(f"Player 2 wins {self.pot} chips with {self.player2_card} over {self.player1_card} {self.history}")


    def start(self):
        self.player1_card = self.draw_card()
        self.player2_card = self.draw_card()

        p1_action = self.get_move(self.player1_strategy, [Action.CHECK, Action.RAISE])

        if p1_action == Action.CHECK:
            p2_action = self.get_move(self.player2_strategy, [Action.CHECK, Action.RAISE])

            if p2_action == Action.RAISE:
                final_action = self.get_move(self.player1_strategy, [Action.CALL, Action.FOLD])
                if final_action == Action.FOLD:
                    print(f"Player 2 wins {self.pot} chips {self.history}")
        else:
            p2_action = self.get_move(self.player2_strategy, [Action.FOLD, Action.CALL]) # ["Fold", "Call"]
            if p2_action == Action.FOLD:
                    print(f"Player 1 wins {self.pot} chips {self.history}")
        
        self.determine_winner()
    