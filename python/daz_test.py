from tennis import TennisGame1

game = TennisGame1("player1", "player2")

for i in range(0,3):
  game.won_point("player1")

for i in range(0,3):
  game.won_point("player2")

print(game.score())
