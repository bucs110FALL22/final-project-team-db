import pygame
import time
import random
import Scorebord
from threading import Timer

class Opponent(pygame.sprite.Sprite):
    def __init__(self,difficulty,):
      super().__init__()
      self.health = 10
      self.strength = 0
      self.tko_count = 0
      self.recovery_difficulty = 0
      self.cooldown = 0 
      self.on_cooldown_block = False
      self.position = "(x,y)"
      self.punch_difficulty = 0
      self.blocked = False
      self.agressiveness = 0
      self.difficulty(difficulty)
      self.animation_render()
      self.stand_animation()
      self.current_sprite = 0
      self.image = self.sprites[self.current_sprite]
      self.rect = self.image.get_rect()
      self.rect.topleft = (150,0)
      self.not_stand = True
      self.game = ""
      self.vulnerable = False
      self.player = ""
    def update(self,speed):
      self.current_sprite += speed
      if int(self.current_sprite) >= len(self.sprites):
        self.current_sprite = 0
        if self.not_stand: 
          self.stand_animation()
          self.not_stand = False
      self.image = self.sprites[int(self.current_sprite)]



    def knockdown(self):
      
      self.down_animation()
      self.tko_count += 1
      if self.tko_count == 3:
        self.game = "loss"
      self.recovery()
      '''cuts to a screen of the player winning'''
    def health_check(self):
      if self.health == 0:
        self.health = -1
        self.knockdown()
    def difficulty(self, difficulty):
      if difficulty == "regular":
        self.health = 150
        self.strength = 10
        self.recovery_difficulty = 5
        self.agressiveness = 8
        self.cooldown = 4
      elif difficulty == "easy":
        self.health = 100 
        self.strength = 5
        self.recovery_difficulty = 7
        self.agressiveness = 6
        # self.cooldown = 5
      elif difficulty == "hard":
        self.health = 200
        self.strength = 15
        self.recovery_difficulty = 3
        self.agressiveness = 4
        self.cooldown = 3
        '''sets the starting stats to varying levels depending on difficulty'''
    def recovery (self):
      get_up = random.randrange(1,10)
      if get_up > self.recovery_difficulty:
        u_timer = Timer(get_up,self.backup())  # Timer(seconds, function)
        u_timer.start()
      else:
        
        self.game = "loss"
        print("loss")
    def backup(self):
      self.up_animation()
      self.tko_count += 1 
      self.health = (100 -(self.tko_count * 25))
      
      '''does a random value to see if the opponent gets a number lower than the recovery_difficulty then it will get back up '''
  
    # def vulnerable(self):
    #   self.vulnerable = True
    #   pygame.time.set_timer(pygame.USEREVENT, 100)
    #   for event in pygame.event.get():
    #     if event.type == pygame.USEREVENT:
    #       self.vulnerable = False
          
    def punch(self,player):
      self.player = player
      if self.health > 0:
        punch_random = random.randrange(1,100)
        if punch_random > 95 and self.vulnerable == False :
          
          self.punch_animation()
          print("punching")
          p_timer = Timer(.7, self.punch_decider)
          p_timer.start()
    def punch_decider(self):    
        if self.player.blocking:
          self.vulnerable = True
          print("blocked")
          print(self.vulnerable)
        elif self.player.blocking == False:
          print("hit")
          self.player.health -= self.strength
          v_timer = Timer(5,self.unvulnerable)
          v_timer.start()
          print(self.player.health)
    def unvulnerable(self):
      self.vulnerable = False
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
    def animation_render(self):
      '''
      animation for when the player stands
      '''
      self.stand = []
      for i in range(4):
        self.stand.append(pygame.image.load(f'assets/Opponent/stand_animation/stand{i + 1}.png').convert_alpha())

      self.punch_list = []
      
      for i in range(11):
        self.punch_list.append(pygame.image.load(f'assets/Opponent/punch_animation/punch{i + 1}.png').convert_alpha())
  
      self.block_list = []
      for i in range(5):
        self.block_list.append(pygame.image.load(f'assets/Opponent/block_animation/block{i + 1}.png').convert_alpha())
        
      self.down_list = []
      for i in range(4):
        self.down_list.append(pygame.image.load(f'assets/Opponent/knockdown_animation/knockdown{i + 1}.png').convert_alpha())
  
      self.up_list = []
      for i in range(5):
        self.up_list.append(pygame.image.load(f'assets/Opponent/backup_animation/recovery{i + 1}.png').convert_alpha())      

      self.hit_img = []
      for i in range(3):
        self.hit_img.append(pygame.image.load('assets/Opponent/punch_animation/punch5.png').convert_alpha())
      
    def stand_animation(self):
      self.sprites = self.stand
    def punch_animation(self):
      self.sprites = self.punch_list
      self.not_stand = True
  
    def block_animation(self):
      self.sprites = self.block_list
      self.not_stand = True
    def down_animation(self):
      self.sprites = self.down_list
    def up_animation(self):
      self.sprites = self.up_list
      self.not_stand = True
    def hit(self):
      self.sprites = self.hit_img
      self.not_stand = True
       
       