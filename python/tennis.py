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
        if (self.p1points==self.p2points):
            return self.draw()
        elif (self.p1points>=4 or self.p2points>=4): 
            return self.advantage_or_win()
        else: 
            return self.point_names()[self.p1points]+ "-"+ self.point_names()[self.p2points]

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
  
    def point_names(self):
        return { 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }


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
        #changed order to escape if condition is met
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            return "Win for " + self.player1Name
            
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            return "Win for " + self.player2Name

        if (self.p1points == self.p2points and self.p1points < 3):
            return self.draw()
        if (self.p1points==self.p2points and self.p1points>2):
            return "Deuce"
               
        if (self.p1points > 0 and self.p2points==0):
            return self.p2_love(self.p1points)

        if (self.p2points > 0 and self.p1points==0):
            return self.p1_love(self.p2points)

        if (self.p1points>self.p2points and self.p1points < 4):
            return self.p1_wins(self.p1points, self.p2points)

        if (self.p2points>self.p1points and self.p2points < 4):
            return self.p2_wins(self.p1points, self.p2points)

        if (self.p1points > self.p2points and self.p2points >= 3):
            return "Advantage " + self.player1Name
        if (self.p2points > self.p1points and self.p1points >= 3):
            return "Advantage " + self.player2Name

    def p2_wins(self, P1res, P2res):
        if (self.p2points==2):
            P2res="Thirty"
        if (self.p2points==3):
            P2res="Forty"
        if (self.p1points==1):
            P1res="Fifteen"
        if (self.p1points==2):
            P1res="Thirty"
        return P1res + "-" + P2res

    def p1_wins(self, P1res, P2res):
        if (self.p1points==2):
            P1res="Thirty"
        if (self.p1points==3):
            P1res="Forty"
        if (self.p2points==1):
            P2res="Fifteen"
        if (self.p2points==2):
            P2res="Thirty"
        return P1res + "-" + P2res

    def p1_love(self, P2res):
        return "Love"+"-"+{ 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }[P2res]

    def p2_love(self, P1res):
        return { 0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty", }[P1res]+"-"+"Love"

    def draw(self):
        return { 0 : "Love-All", 1 : "Fifteen-All", 2 : "Thirty-All"}.get(self.p2points)   
    
    # def SetP1Score(self, number):
    #     for i in range(number):
    #         self.P1Score()
    
    # def SetP2Score(self, number):
    #     for i in range(number):
    #         self.P2Score()
    
    # def P1Score(self):
    #     self.p1points +=1
   
    # def P2Score(self):
    #     self.p2points +=1
        
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

