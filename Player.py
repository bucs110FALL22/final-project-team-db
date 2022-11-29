import pygame
import time
import random
import Opponent
import Scorebord
from threading import Timer
class Player(pygame.sprite.Sprite):
  def __init__(self,difficulty,Opponent):
    super().__init__()
    self.health = 0

    self.sprites = []
    self.animation_render()
    self.stand_animation()
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.not_stand = False
    self.rect.topleft = (150,0)
    self.stand = True
    self.blocking = False
    self.block_time = 0
    self.punch_difficulty = 2
    self.tko_count = 0
  
    self.on_cooldown = False
    self.required_presses = (25 * (self.tko_count + 1))
    self.blocking_difficulty(difficulty)
    self.opponent = Opponent
    self.punch_count = 0
    self.game = ""
  def health_check(self):
    if self.health <= 0:
      self.knockdown()
  def update(self,speed):
    
    self.current_sprite += speed
    if int(self.current_sprite) >= len(self.sprites):
      self.current_sprite = 0
      if self.not_stand:
        self.rect.topleft = (150,0)
        self.stand_animation()
        self.not_stand = False
    self.image = self.sprites[int(self.current_sprite)]
    
  def blocking_difficulty(self,difficulty):
    '''
    sets how long you can block for and how long u have to wait to be able to block again and ur chances of punches being blocked
    args: difficulty(str) the difficulty of the game
    '''
    if difficulty == "easy":
      self.block_grace = .25
      # self.cooldown = 1
      self.punch_difficulty = 7
    elif difficulty == "regular":
      self.block_grace= .2
      # self.cooldown = 2
      self.punch_difficulty = 5
    elif difficulty == "hard":
      self.block_grace = .15
      self.punch_difficulty = 3
       #run at init
  def block(self):
    '''
    makes the player unable to be hit by enemy, starts cooldown
    '''
    self.block_animation()
    self.blocking = True
    p_timer = Timer(self.block_grace, self.unblock)
    p_timer.start()
  def unblock(self):
    self.not_stand = True
    self.blocking = False
      # self.block_cooldown() 
  def knockdown(self):
    '''
    sees how many times the player has been knocked down. if less then three then the "back_up method" starts, if they return.s True then the player returns to the fight
    '''
    self.down_animation()
    if self.tko_count == 3:
      self.game = "loss"
    else:
      back_up = self.back_up()
      if back_up:
        self.tko_count += 1 
        self.knockdown = False 
        self.health = (100 -(self.tko_count * 25))
        self.up_animation()
  def back_up(self):
    '''
    user must press space a certain amount of times before knockdown_timer becomes False. if they succeed they return to the game, if thy fail its a knockout and the player looses
    '''
    times_pressed = 0
    pygame.time.set_timer(pygame.USEREVENT, 10000)
    timer = True
    print("mash")
    while timer:
      for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
          timer = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            times_pressed += 1
            print(times_pressed)
    if times_pressed >=  self.required_presses:
      return(True)
    else:
      self.game = "loss"
      
  def punch(self,opponent):
      if self.punch_count == 3:
        opponent.vulnerable = False
        self.punch_count = 0 
      self.punch_animation()
      punch_blocked = random.randrange(1,(self.punch_difficulty))
      if self.opponent.vulnerable == False:
        opponent.block_animation()
      elif punch_blocked <= (1 + self.punch_count):
        opponent.block_animation()
        self.punch_count = 0
      else:
        self.opponent.hit()
        self.opponent.health -= 10
        self.punch_count += 1
        print(self.punch_count)
        







  def animation_render(self):
    '''
    animation rendering
    '''
    self.stand_list = []
    for i in range(4):
      self.stand_list.append(pygame.image.load(f'assets/Player/p_stand/player_stand{i + 1}.png').convert_alpha())
      
    self.punch_list = []
    
    for i in range(5):
      self.punch_list.append(pygame.image.load(f'assets/Player/p_punch/player_punch{i + 1}.png').convert_alpha())

    self.block_list = []
    for i in range(4):
      self.block_list.append(pygame.image.load(f'assets/Player/p_block/player_block{i + 1}.png').convert_alpha())
      
    self.down_list = []
    self.down_list.append(pygame.image.load(f'assets/Player/p_down/player_down5.png').convert_alpha())

    self.up_list = []
    for i in range(5):
      self.up_list.append(pygame.image.load(f'assets/Player/p_down/player_down{5 - i}.png').convert_alpha())
  def stand_animation(self):
    self.sprites = self.stand_list
    
  def punch_animation(self):
    self.sprites = self.punch_list
    self.not_stand = True

  def block_animation(self):
    self.sprites = self.block_list

  def down_animation(self):
    self.rect.topleft = (0,0)
    self.sprites = self.down_list
  def up_animation(self):
    self.rect.topleft = (0,0)
    self.sprites = self.up_list
    self.not_stand = True
   