# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.scores_dict = {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def point_winner(self, diff):
        return self.player1Name if diff > 0 else self.player2Name

    def score(self):
        result = ""
        if (self.p1points==self.p2points):
            result = self.scores_dict.get(self.p1points) + "-All" if self.p1points < 3 else "Deuce"
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if abs(minusResult) == 1 :
                result ="Advantage " + self.point_winner(minusResult)
            else:
                result ="Win for " + self.point_winner(minusResult)
        else:
           result = self.scores_dict[self.p1points] + "-" + self.scores_dict[self.p2points]
        return result


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.scores_dict = {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def get_map_values(self, P1res, P2res):
        P1res=self.scores_dict.get(self.p1points, "")
        P2res=self.scores_dict.get(self.p2points, "")
        return P1res, P2res

    def score(self):
        result = ""
        P1res = ""
        P2res = ""

        if (self.p1points == self.p2points and self.p1points < 3):
            result, _ = self.get_map_values(P1res, P2res)
            result += "-All"
        if (self.p1points==self.p2points and self.p1points>2):
            result = "Deuce"
        

        if (self.p1points > 0 and self.p2points==0):
            P1res, P2res = self.get_map_values(P1res, P2res)
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            P1res, P2res = self.get_map_values(P1res, P2res)
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1points>self.p2points and self.p1points < 4):
            P1res, P2res = self.get_map_values(P1res, P2res)
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            P1res, P2res = self.get_map_values(P1res, P2res)
            result = P1res + "-" + P2res

        
        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name
        

        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def P1Score(self):
        self.p1points +=1
    
    
    def P2Score(self):
        self.p2points +=1
        
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
    
    def preliminaryPoints(self):
        p = ["Love", "Fifteen", "Thirty", "Forty"]
        s = p[self.p1]
        return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]

    def definitionPoints(self):
        if (self.p1 == self.p2):
            return "Deuce"
        s = self.p1N if self.p1 > self.p2 else self.p2N
        return "Advantage " + s if (abs(self.p1-self.p2) == 1) else "Win for " + s

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            return self.preliminaryPoints()
        else:
            return self.definitionPoints()
