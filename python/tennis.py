# -*- coding: utf-8 -*-


class TennisGame1:
    FIRST = 0
    SECOND = 1
    RESULTS = ["Love", "Fifteen", "Thirty", "Forty"]
    ALL = "-All"

    def __init__(self, player1Name, player2Name):
        self.player_ids = {
            player1Name: TennisGame1.FIRST,
            player2Name: TennisGame1.SECOND
        }

        self.id_players = {
            TennisGame1.FIRST: player1Name,
            TennisGame1.SECOND: player2Name
        }

        self.scoreboard = [0, 0]

    def won_point(self, playerName):
        self.scoreboard[self.player_ids[playerName]] += 1

    def score(self):

        if self.scoreboard[TennisGame1.FIRST] == self.scoreboard[TennisGame1.SECOND]:
            score = self.scoreboard[TennisGame1.FIRST]
            return TennisGame1.RESULTS[score] + TennisGame1.ALL if score < 3 else "Deuce"
        elif any(i >= 4 for i in self.scoreboard):
            diff = self.scoreboard[TennisGame1.FIRST] - self.scoreboard[TennisGame1.SECOND]

            if diff < 0:
                name = self.id_players[TennisGame1.SECOND]
            else:
                name = self.id_players[TennisGame1.FIRST]

            if abs(diff) >= 2:
                return "Win for " + name
            else:
                return "Advantage " + name
        else:
            return TennisGame1.RESULTS[self.scoreboard[TennisGame1.FIRST]] + "-" + TennisGame1.RESULTS[
                self.scoreboard[TennisGame1.SECOND]]

class TennisGame2:
    RESULTS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.scoreboard = {
            self.player1Name: 0,
            self.player2Name: 0
        }
        self.diff = 0

    def won_point(self, playerName):
        self.scoreboard[playerName] += 1
        self.diff = self.scoreboard[self.player1Name] - self.scoreboard[self.player2Name]

    def score(self):
        if self.diff == 0:
            return TennisGame2.RESULTS[self.scoreboard[self.player1Name]] + "-All" if self.scoreboard[
                                                                                          self.player1Name] < 3 else "Deuce"
        elif any(i >= 4 for i in self.scoreboard.values()):
            name = self.player2Name if self.diff < 0 else self.player1Name
            return "Advantage " + name if (abs(self.diff) < 2) else "Win for " + name

        return TennisGame2.RESULTS[self.scoreboard[self.player1Name]] + "-" + TennisGame2.RESULTS[
            self.scoreboard[self.player2Name]]


class TennisGame3:
    RESULTS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, name):
        if name == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            score = TennisGame3.RESULTS[self.p1]
            return score + "-All" if (self.p1 == self.p2) else score + "-" + TennisGame3.RESULTS[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            score = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + score if (abs(self.p1 - self.p2) == 1) else "Win for " + score
