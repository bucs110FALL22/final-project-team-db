import pygame
import time
import random
import Player

class Opponent(pygame.sprite.Sprite):
    def __init__(self,image_file,difficulty):
      super().__init__(self)
      self.health = 100
      self.strength = 0
      self.knockdown = False
      self.tko_count = 0
      self.recovery_difficulty = 0
      if self.health == 0:
        self.knockdown()
      self.cooldown = 0 
      self.position = (x,y)
      self.punch_difficulty = 0
      self.difficulty()
    def knockdown(self):
      if self.knockdown == True:
        tko_count += 1
        knockdown animation
      if self.tko_count == 3:
        break
        'cuts to a screen of the player winning'
  
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
   'sets the starting stats to varying levels depending on difficulty'
  def recovery (difficulty):
    if difficulty = "Regular" :
       get_up = random.randrange(1,10)
      if get_up > self.recovery_difficulty 
        self.knockdown = False
        get up animation
      else 
        self.knockdown = True
    'does a random value to see if the opponent gets a number lower than the recovery_difficulty then it will get back up '


  
  def punch(self,Player)
  if Player.blocking:
    break
  else:
    
    Player.health -= self.strength
''
  def when_to_punch(self):
     chance_hit = random.randrange(1,10)
    
    if self.hit_by_opponent = True and chance_hit >= 5
      punch animation

    while self.time > 0
      if self.block = False and chance_hit >=6
      punch animation
      time.sleep(self.cooldown)

     'different instance when the opponent would punch, 1. punched after being hit, 2. randomly punches throught the match            '
    
    def punch_animation(self):
      '''
      animation for when the player punches
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
      time.sleep(.2)
      self.image = pygame.image.load()# keyframe 3

    def standing_animation(self):
      '''
      looping animation for when the player is standing
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2

    def back_up_animation(self):
      '''
      animation for when the player gets back up
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
      time.sleep(.2)
      self.image = pygame.image.load()# keyframe 3