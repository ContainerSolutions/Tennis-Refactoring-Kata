# -*- coding: utf-8 -*-



class TennisGame1:
    score_map = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.minusResult = 0

    
    def score_string_draw(self):
        if self.p1points>=3: return "Deuce"
        return "{score}-All".format(
            score=TennisGame1.score_map.get(self.p1points)
        )

    def score_string_notdraw(self):
        if not (self.p1points>=4 or self.p2points>=4):
            return "{score1}-{score2}".format(
                score1=TennisGame1.score_map.get(self.p1points),
                score2=TennisGame1.score_map.get(self.p2points)
            ) 

        score_string = "Advantage" if abs(self.minusResult)==1 else "Win for"
        player = self.player2Name if self.minusResult<1 else self.player1Name

        return "{score} {player}".format(
            score=score_string,
            player=player
        )

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
        self.minusResult = self.p1points-self.p2points
    
    def score(self):
        if (self.p1points==self.p2points):
            return self.score_string_draw()

        return self.score_string_notdraw()



class TennisGame2:
    score_map = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self):
        P1res = TennisGame2.score_map.get(self.p1points,"")
        P2res = TennisGame2.score_map.get(self.p2points,"")

        if (self.p1points == self.p2points and self.p1points < 3):
            result=P1res+"-All"

        if (self.p1points==self.p2points and self.p1points>2):
            result = "Deuce"
        
        if (self.p1points>self.p2points and self.p1points < 4) or (self.p2points>self.p1points and self.p2points < 4): 
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
    
    def SetP1Score(self, number):
        for _ in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for _ in range(number):
            self.P2Score()
    
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
    
    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
