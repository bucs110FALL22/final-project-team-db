import pygame
import Player
import Opponent
import time


class Scorebord():   
  def __init__(self,player,opponent,screen):
    self.screen = screen
    self.player = player
    self.opponent = opponent
    self.current_round = 1
    self.p_health = 100
    self.o_health = 100
  def health_bars(self):
    '''
    creates the health bars of the player and opponent and get smaller when health decreases
    '''
    pygame.display.set_caption("show text")
    font = pygame.font.Font('assets/fonts/Komyca3DFreeVersionItalic-rg1WO.ttf', 15)
    ptext = font.render('Player', True, "red")
    ptextRect = ptext.get_rect()
    ptextRect.topleft = (0,0)
    self.screen.blit(ptext,ptextRect)
    otext = font.render('Opponent', True, "red")
    otextRect = otext.get_rect()
    otextRect.topleft = (500,0)
    self.screen.blit(otext,otextRect)
    pygame.draw.rect(self.screen,"red",(0,20,(self.player.health * 4),20))# once we figure out where to place thew scoreboard the strings will be replaced with ints
    #Opponent health print "opponent" above
    pygame.draw.rect(self.screen,"red",(500,20,(self.opponent.health * 4),20))
  
  def winner(self):
    pygame.display.set_caption("show text")
    font = pygame.font.Font('assets/fonts/Komyca3DFreeVersionItalic-rg1WO.ttf', 50)
    text = font.render('YOU WIN!', True, "red")
    textRect = text.get_rect()
    textRect.topleft = (370,200)
    self.screen.blit(text,textRect)

  def loss(self):
    pygame.display.set_caption("show text")
    font = pygame.font.Font('assets/fonts/Komyca3DFreeVersionItalic-rg1WO.ttf', 50)
    text = font.render('--YOU LOOSE--', True, "red")
    textRect = text.get_rect()
    textRect.topleft = (370,200)
    self.screen.blit(text,textRect)
  # def clock(self):
  #   '''
  #   counts down time for the round
  #   '''
  #   for seconds in (self.time + 1):
  #     time.sleep(1)
  #     self.current_time -= 1
  #     #update current time on scorebord
  #   self.current_round += 1
  #   if self.current_round == 4:
  #    $#"end game"
  def scoreboard(self):
    '''
    makes the scorebord 
    '''
    self.health_bars()
    # self.clock()
    