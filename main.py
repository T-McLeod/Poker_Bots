from Kuhn.kuhn_poker import Game
from Kuhn.players.game_strategy import Game_Strategy
from Kuhn.players.human_player import Human_Player

game = Game()
game.player1 = Human_Player()
game.player2 = Game_Strategy()
game.play_game()