import pygame
import random
from threading import Timer
from pygame import mixer

class Opponent(pygame.sprite.Sprite):
    def __init__(self,difficulty,):
      super().__init__()
      self.health = 100
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
      self.not_stand = False
      self.game = ""
      self.vulnerable = False
      self.player = ""
      self.already_knocked = False
      self.animation_stop = False
    def update(self,speed):
      self.current_sprite += speed
      if int(self.current_sprite) >= len(self.sprites):
        self.current_sprite = 0
        if self.not_stand and self.health > 0: 
          self.stand_animation()
          self.not_stand = False
      self.image = self.sprites[int(self.current_sprite)]



    def knockdown(self):
      self.tko_count += 1
      if self.tko_count == 3:
        self.game = "loss"
      else:
        d_timer = Timer(5,self.recovery)
        d_timer.start()
    def health_check(self):
      if self.health <= 0 and self.already_knocked == False:
        self.already_knocked = True
        self.down_animation()
        self.knockdown()
    def difficulty(self, difficulty):
      if difficulty == "regular":
        self.health = 150
        self.strength = 10
        self.recovery_difficulty = 5
      elif difficulty == "easy":
        self.health = 100
        self.strength = 5
        self.recovery_difficulty = 7
      elif difficulty == "hard":
        self.health = 200
        self.strength = 15
        self.recovery_difficulty = 3
        '''sets the starting stats to varying levels depending on difficulty'''
    def recovery (self):
      get_up = random.randrange(1,10)
      if get_up > self.recovery_difficulty:
        self.backup()
      else:
        self.game = "loss"
    def backup(self):
      self.up_animation()
      self.health = (100 -(self.tko_count * 25))
      self.already_knocked = False
      
      '''does a random value to see if the opponent gets a number lower than the recovery_difficulty then it will get back up '''
  
          
    def punch(self,player):
      self.player = player
      if self.health > 0:
        punch_random = random.randrange(1,100)
        if punch_random > 75 and self.vulnerable == False :
          
          self.punch_animation()
          p_timer = Timer(.7, self.punch_decider)
          p_timer.start()
    def punch_decider(self):    
        if self.player.blocking:
          blocking_sound = mixer.Sound("assets/Audio/blocking_punch.mp3")
          blocking_sound.play() 
          self.vulnerable = True

          v_timer = Timer(5,self.unvulnerable)
          v_timer.start()
        elif self.player.blocking == False:

          self.player.health -= self.strength
          hit_sound = mixer.Sound("assets/Audio/oof.wav")
          hit_sound.play()
    def unvulnerable(self):
      self.vulnerable = False
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

      self.animation_stop = True
      self.sprites = self.down_list
      
    def up_animation(self):
      self.animation_stop = False
      self.sprites = self.up_list
      self.not_stand = True
    def hit(self):
      self.sprites = self.hit_img
      self.not_stand = True
       
