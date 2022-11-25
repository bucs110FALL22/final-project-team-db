import pygame
import time
import random
from Player import Player
from Animations import Animations


class Opponent(pygame.sprite.Sprite):
    def __init__(self,difficulty):
      super().__init__()
      self.health = 100
      self.strength = 0
      self.knockdown = False
      self.tko_count = 0
      self.recovery_difficulty = 0
      if self.health == 0:
        self.knockdown()
      self.cooldown = 0 
      self.position = "(x,y)"
      self.punch_difficulty = 0
      self.blocked = False
      self.agressiveness = 0
      self.difficulty(difficulty)
      self.stand_animation_render()
      self.stand_animation()
      self.current_sprite = 0
      self.image = self.sprites[self.current_sprite]
      self.rect = self.image.get_rect()
      self.rect.topleft = (150,0)
      self.punch = False
      self.block = False
    def update(self,speed):
    # if self.punch or self.block or self.stand:
      
      self.current_sprite += speed
      if int(self.current_sprite) >= len(self.sprites):
        self.current_sprite = 0
      self.image = self.sprites[int(self.current_sprite)]


      
    def knockdown(self):#recovery isnt called
      if self.knockdown == True:
        selftko_count += 1
        self.a.opponent_fall(self)
      if self.tko_count == 3:
        pass #break game loop, player wins
        '''cuts to a screen of the player winning'''
  
    def difficulty(self, difficulty):
      if difficulty == "Regular":
        self.health = 150
        self.strength = 10
        self.recovery = 5
        self.agressiveness = 8
      elif difficulty == "Easy":
        self.health = 100 
        self.strength = 7
        self.recovery = 3
        self.agressiveness = 6
      elif difficulty == "Hard":
        self.health = 200
        self.strength = 15
        self.recovery = 1
        self.agressiveness = 4
        '''sets the starting stats to varying levels depending on difficulty'''
    def recovery (self):
      get_up = random.randrange(1,10)
      if get_up > self.recovery_difficulty:
        self.knockdown = False
        self.a.opponent_getup()
      else: 
          self.knockdown = True#knockdown is aready true if recovery where to be called
      '''does a random value to see if the opponent gets a number lower than the recovery_difficulty then it will get back up '''
  
  
    
    # def punch(self,player):
    #   if Player.blocking:
    #     break
    #   else:
    #     Player.health -= self.strength

    # def punch_after_block(self):
    #   punch_chance = random.randrange(1,10)
    #   if punch_chance >= self.agressiveness:
    #     self.a.opponent_punch()
    #     punch(Player)
        
    # def when_to_punch(self):#I would be like,it will reroll every time the while loop goes, so id make it like a very low percent chance, then if true, punch, then roll again, with a max of 3 punches. if blocked break the loop
    
    #   chance_hit = random.randrange(1,10)
    
    #   # if self.hit_by_opponent = True and chance_hit >= 5:
    #   #   self.a.opponent_punch()

    #   # while self.time > 0 
    #   #   if self.block = False and chance_hit >=6
    #   # punch animation
    #   # time.sleep(self.cooldown)

    #   '''different instance when the opponent would punch, 1. punched after being hit, 2. randomly punches throught the match'''
    def stand_animation_render(self):
      '''
      animation for when the player stands
      '''
      self.stand = []
      for i in range(4):
        self.stand.append(pygame.image.load(f'assets/Opponent/stand_animation/stand{i + 1}.png'))
      
  
    def stand_animation(self):
      self.sprites = self.stand