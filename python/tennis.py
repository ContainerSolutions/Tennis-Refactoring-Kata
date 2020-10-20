# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        # score is advantage or a win
        elif (self.p1points >= 4 or self.p2points >= 4):
            player = ""
            lead = 0
            if self.p1points > self.p2points:
                player = self.player1Name
                lead = self.p1points - self.p2points
            else:
                player = self.player2Name
                lead = self.p2points - self.p1points
            result = {
                # if the lead is 1 it's advantage,
                #   if it's >= 2 then it's a win!
                1: "Advantage " + player,
            }.get(lead, "Win for " + player)
        # just a regular score to parse
        else:
            score = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }
            result = '{}-{}'.format(
                score[self.p1points],
                score[self.p2points]
            )
        return result


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        self.UpdateScore(playerName, 1)

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points == 0):
                result = "Love"
            if (self.p1points == 1):
                result = "Fifteen"
            if (self.p1points == 2):
                result = "Thirty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points < 4 and self.p2points < 4) \
                and (self.p1points != self.p2points):
            if (self.p1points == 0):
                P1res = "Love"
            if (self.p2points == 0):
                P2res = "Love"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 3):
                P2res = "Forty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points >= 4 and self.p2points >=
                0 and (self.p1points-self.p2points) >= 2):
            result = "Win for " + self.player1Name
        if (self.p2points >= 4 and self.p1points >=
                0 and (self.p2points-self.p1points) >= 2):
            result = "Win for " + self.player2Name
        return result

    def UpdateScore(self, player, count):
        if player == self.player1Name:
            self.p1points += count
        else:
            self.p2points += count


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)
                                        * (self.p1-self.p2) == 1) else "Win for " + s
