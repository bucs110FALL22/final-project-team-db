import pygame
import time
import random
import Player

class Opponent(pygame.sprite.Sprite):
    def __init__(self,image_file,difficulty):
      super().__init__(self)
      self.health = 100
      self.difficulty = "Regular"#redundent
      self.strength = 0
      self.knockdown = False
      self.blocking = False #redundent
      self.tko_count = 0
      self.recovery_difficulty = 0
      if self.health == 0:
        self.knockdown()
      self.cooldown = 0 #redundent
      self.position = (x,y)
      self.block_time = 0 #redundent
      self.cooldown = 0 #redundent
      self.punch_difficulty = 0
      self.on_cooldown = False #redundent
      self.difficulty()
    def knockdown(self):
      if self.knockdown == True:
        tko_count += 1
      if self.tko_count == 3:
        #break game loop end match, player is winner
    self.position = (x,y)#?
  
  def difficulty(difficulty):
    if difficulty == "Regular":
      self.health = 150
      self.strength = 10
      self.recovery = 5
    elif difficulty == "Easy":
      self.health = 100 
      self.strength = 7
      self.recovery = 3
    elif difficulty == "Hard":
      self.health = 200
      self.strength = 15
      self.recovery = 1
  
  def recovery (difficulty):
    if difficulty = "Regular" :
       get_up = random.randrange(1,10)
      if get_up > self.recovery_difficulty 
        self.knockdown = False
      else 
        self.knockdown = True
def blocking_difficulty(self,difficulty): #already in Player class
      
      if difficulty == "Easy":
        self.block_time = 2
        self.cooldown = 5
      elif difficulty == "Regular":
        self.block_time = 2
        self.cooldown = 4
      elif difficulty == "Hard":
        self.block_time = 3
        self.cooldown = 3

  def block(self): #already in player class 
      
      if self.cooldown:
        break
      else:
        block_animation()
        self.blocking = True
        time.sleep(self.block_time)
        self.blocking = False
        self.block_cooldown() 
  def punch(self,Player)
  if Player.blocking:
    break
  else:
    Player.health -= self.strength

  def when_to_punch(self):
    