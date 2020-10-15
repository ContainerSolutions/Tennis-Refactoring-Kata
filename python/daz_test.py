from tennis import TennisGame1

game = TennisGame1("player1", "player2")

for i in range(0,2):
  game.won_point("player2")

game.score()
print(game.score_string_notdraw())