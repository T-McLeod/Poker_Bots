import random
import numpy as np
from enum import Enum
from collections import namedtuple

class Action(Enum):
    FOLD = 0
    CHECK = 1
    CALL = 2
    RAISE = 3

Card = int
History = list[Card | Action]

class Player:
    def get_move(self, possible_actions: list[Action]) -> Action:
        pass

    def inform(self, event: Card | Action) -> None:
        pass


class Game():
    def __init__(self):
        self.history: History = []
        self.deck = [x+1 for x in range(3)]
        self.pot = 2

        self.player1_card = -1
        self.player2_card = -1
        self.player1 = Player()
        self.player2 = Player()
    
    def random_function(self, i: int):
        return random.randint(0, i-1)
    
    def draw_card(self) -> Card:
        i = self.random_function(len(self.deck))
        self.history.append(i)

        return self.deck.pop(i)

    def get_move(self, player_strategy: Player, possible_moves: list[Action]) -> Action:
        action = player_strategy.get_move(possible_moves)
        self.history.append(action)
        if action == Action.CALL:
            self.pot += 2
        return action
    
    def determine_winner(self):
        if self.player1_card > self.player2_card:
            print(f"Player 1 wins {self.pot} chips with {self.player1_card} over {self.player2_card} {self.history}")
        else:
            print(f"Player 2 wins {self.pot} chips with {self.player2_card} over {self.player1_card} {self.history}")


    def inform_player(self, player: Player, event: Card | Action):
        player.inform(event)

    def inform_all(self, event: Card | Action):
        self.inform_player(self.player1, event)
        self.inform_player(self.player2, event)

    def play_game(self):
        self.player1_card = self.draw_card()
        self.player1.inform(self.player1_card)

        self.player2_card = self.draw_card()
        self.player2.inform(self.player2_card)

        p1_action = self.get_move(self.player1, [Action.CHECK, Action.RAISE])
        self.inform_all(p1_action)
        

        if p1_action == Action.CHECK:
            p2_action = self.get_move(self.player2, [Action.CHECK, Action.RAISE])
            self.inform_all(p2_action)

            if p2_action == Action.RAISE:
                final_action = self.get_move(self.player1, [Action.CALL, Action.FOLD])
                self.inform_all(final_action)

                if final_action == Action.FOLD:
                    print(f"Player 2 wins {self.pot} chips {self.history}")
                    return -self.pot
        else:
            p2_action = self.get_move(self.player2, [Action.FOLD, Action.CALL]) # ["Fold", "Call"]
            self.inform_all(p2_action)
            if p2_action == Action.FOLD:
                    print(f"Player 1 wins {self.pot} chips {self.history}")
                    return self.pot
        
        self.determine_winner()
    