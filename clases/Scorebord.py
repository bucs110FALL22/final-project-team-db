import pygame
import Player
import Opponent
import time


class Score_bord:   
    def __init__(self,time,rounds,player_name,surface):
      self.surface = surface
      self.time = time
      self.current_time = self.time
      self.rounds = rounds
      self.current_round = 1
      self.player_name = player_name
      self.player_health = Player.health
      self.opponent_health = Opponent.health
    def health_bars(self):
      '''
      creates the health bars of the player and opponent and get smaller when health decreases
      '''
      #player health bar, print self.player_name above
      pygame.draw.rect(self.serface,"red",("left x and y"),("right y",self.player_health))# once we figure out where to place thew scoreboard the strings will be replaced with ints
      #Opponent health print "opponent" above
      pygame.draw.rect(self.serface,"red",("left x and y"),("right y",self.opponent_health))
    
  

    def clock(self):
      '''
      counts down time for the round
      '''
      for seconds in (self.time + 1):
        time.sleep(1)
        self.current_time -= 1
        #update current time on scorebord
      self.current_round += 1
      if self.current_round == 4:
       $#"end game"
    def scoreboard(self):
      '''
      makes the scorebord 
      '''
      self.health_bars()
      self.clock()
      