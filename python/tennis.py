# -*- coding: utf-8 -*-

class TennisGame1:
    point_to_strings =  { 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }

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
        if (self.p1points==self.p2points):
            return self.draw()
        elif (self.p1points>=4 or self.p2points>=4): 
            return self.advantage_or_win()
        else: 
            return self.point_to_strings.get(self.p1points)+ "-"+ self.point_to_strings.get(self.p2points)

    def draw(self):
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(self.p1points, "Deuce")
    
    def advantage_or_win(self):
        minusResult = self.p1points-self.p2points
        if (minusResult==1):
            return "Advantage " + self.player1Name
        elif (minusResult ==-1):
            return "Advantage " + self.player2Name
        elif (minusResult>=2):
            return "Win for " + self.player1Name
        return "Win for " + self.player2Name

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
           self.p1points +=1
        else:
           self.p2points +=1
    
    def score(self):
        point_to_strings =  { 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }

        #changed order to escape if condition is met
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            return "Win for " + self.player1Name
            
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            return "Win for " + self.player2Name

        if (self.p1points == self.p2points and self.p1points < 3):
            return point_to_strings.get(self.p1points)+"-All"

        if (self.p1points==self.p2points and self.p1points>2):
            return "Deuce"
               
        # if (self.p1points > 0 and self.p2points==0):
        #     return point_to_strings.get(self.p1points) + "-" + "Love"

        # if (self.p2points > 0 and self.p1points==0):
        #     return "Love"+"-" + point_to_strings.get(self.p2points)

        if (self.p1points>self.p2points and self.p1points < 4 or self.p2points>self.p1points and self.p2points < 4):
            return point_to_strings.get(self.p1points) + "-" + point_to_strings.get(self.p2points)

        if (self.p1points > self.p2points and self.p2points >= 3):
            return "Advantage " + self.player1Name
        if (self.p2points > self.p1points and self.p1points >= 3):
            return "Advantage " + self.player2Name

    # def p2_wins(self, P1res, P2res):
    #     return {1 : "Fifteen", 2 : "Thirty"}[P1res] + "-" + {2 : "Thirty", 3 : "Forty" }[P2res]

    # def p1_wins(self, P1res, P2res):
    #     return {2 : "Thirty", 3 : "Forty" }[P1res] + "-" + {1 : "Fifteen", 2 : "Thirty"}[P2res]

    # def p1_love(self, P2res):
    #     return "Love"+"-"+{ 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }[P2res]

    # def p2_love(self, P1res):
    #     return { 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }[P1res]+"-"+"Love"

    # def draw(self, P1res):
    #     return { 0 : "Love-All", 1 : "Fifteen-All", 2 : "Thirty-All"}.get(P1res)   
            
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
            point_to_strings = ["Love", "Fifteen", "Thirty", "Forty"]
            return  point_to_strings[self.p1] + "-All" if (self.p1 == self.p2) else  point_to_strings[self.p1] + "-" + point_to_strings[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            score = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + score if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + score

