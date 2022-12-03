import pygame
import random
from threading import Timer
from pygame import mixer

class Opponent(pygame.sprite.Sprite):
    def __init__(self,difficulty,):
      super().__init__()
      self.TKO = 3
      self.DOWN_TIMER = 5
      self.HEALTH_BACKUP = 100
      self.NEEDED_VALUE_PUNCH = 75
      self.VTIMER = 5
      self.TKO_MULTIPLY = 25
      self.ZERO_HEALTH = 0
      self.PTIMER = 0.7
      self.health = 100
      self.strength = 0
      self.tko_count = 0
      self.recovery_difficulty = 0
      self.COOLDOWN = 0 
      self.on_block_cooldown = False
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
      '''updates sprites for animations
      arg: speed(int), how fast the frames should rotate'''
      self.current_sprite += speed
      if int(self.current_sprite) >= len(self.sprites):
        self.current_sprite = 0
        if self.not_stand and self.health > self.current_sprite : #was 0
          self.stand_animation()
          self.not_stand = False
      self.image = self.sprites[int(self.current_sprite)]



    def knockdown(self):
      '''if the opponent gets knocked down adds 1 to the tko count, once it reaches 3 the opponent loses, and has a timer for a chance to get backup'''
      self.tko_count += 1
      if self.tko_count == self.TKO:
        self.game = "loss"
      else:
        d_timer = Timer(self.DOWN_TIMER,self.recovery)
        d_timer.start()
    def health_check(self):
      '''checks the health of the opponent and if it is below or equal to 0 then the opponent gets knocked down and initiates the knocdown animation and function'''
      if self.health <= self.ZERO_HEALTH and self.already_knocked == False:
        self.already_knocked = True
        self.down_animation()
        self.knockdown()
    def difficulty(self, difficulty):
      '''this give the opponents his stats based off of difficulty, changes stats for health, strength and recovery difficulty
      args: difficulty(str) dictate the difficulty of the game'''
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
        
    def recovery (self):
      '''the opponent has a chance to get back up if the random number is greater than the recover difficulty and if it does intiates the backup function, if no the opponent loses'''
      get_up = random.randrange(1,10)
      if get_up > self.recovery_difficulty:
        self.backup()
      else:
        self.game = "loss"
    def backup(self):
      '''gets a random value to see if the opponent gets a number lower than the recovery difficulty then it will get back up'''
      self.up_animation()
      self.health = (self.HEALTH_BACKUP -(self.tko_count * self.TKO_MULTIPLY))
      self.already_knocked = False
      
      
  
          
    def punch(self,player):
      '''if the opponents health is above 0 then it will loop and randomly punch the player depending if the randome number is greater than 75 and if it is the it initiates the punch animation
      arg: player(class)'''
      self.player = player
      if self.health > self.ZERO_HEALTH:
        punch_random = random.randrange(1,100)
        if punch_random > self.NEEDED_VALUE_PUNCH and self.vulnerable == False :
          
          self.punch_animation()
          p_timer = Timer(self.PTIMER, self.punch_decider)
          p_timer.start()
    def punch_decider(self):
        '''decides if the opponents punch goes through, if the player is blocknig and he punches he becomes vulnerable, if the player isnt blocking then the opponent deals damage according to his strength'''
        if self.player.blocking:
          blocking_sound = mixer.Sound("assets/Audio/blocking_punch.mp3")
          blocking_sound.play() 
          self.vulnerable = True

          v_timer = Timer(self.VTIMER,self.unvulnerable)
          v_timer.start()
        elif self.player.blocking == False:

          self.player.health -= self.strength
          hit_sound = mixer.Sound("assets/Audio/oof.wav")
          hit_sound.play()
    def unvulnerable(self):
      '''a function to call to make the opponent not vulnerable'''
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
      '''changes the sprite to the standing loop'''
      self.sprites = self.stand
    def punch_animation(self):
      '''changes the sprite to the punch loop and then back to stand'''
      self.sprites = self.punch_list
      self.not_stand = True
  
    def block_animation(self):
      '''changes the sprite to block loop then back to stand'''
      self.sprites = self.block_list
      self.not_stand = True
    def down_animation(self):
      '''changes the sprite to the down loop'''
      self.animation_stop = True
      self.sprites = self.down_list
      
    def up_animation(self):
      '''changes the sprite to the up loop then back to stand'''
      self.animation_stop = False
      self.sprites = self.up_list
      self.not_stand = True
    def hit(self):
      '''changes the sprite to the hit loop'''
      self.sprites = self.hit_img
      self.not_stand = True
       
