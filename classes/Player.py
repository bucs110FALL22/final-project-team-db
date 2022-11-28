import pygame
import time
import random
import Opponent
class Player(pygame.sprite.Sprite):
  def __init__(self,difficulty,Opponent):
    super().__init__()
    self.health = 100
    if self.health == 0:
      self.knockdown()
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
    self.cooldown = 0
    self.block_time = 0
    self.cooldown = 0
    self.punch_difficulty = 0
    self.tko_count = 0
    self.knockdown = False
    self.on_cooldown = False
    self.required_pressess = (50 * (self.tko_count + 1))
    self.blocking_difficulty(difficulty)
    self.opponent = Opponent
    self.game = ""
    
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
    if difficulty == "Easy":
      self.block_time = 3
      self.cooldown = 1
      self.punch_difficulty = 7
    elif difficulty == "Regular":
      self.block_time = 2
      self.cooldown = 2
      self.punch_difficulty = 5
    elif difficulty == "Hard":
      self.block_time = 1.5
      self.cooldown = 3
      self.punch_difficulty = 3
       #run at init
  def block(self):
    '''
    makes the player unable to be hit by enemy, starts cooldown
    '''
    if self.on_cooldown:
      pass
      #play beep sound to signify on cooldown
    else:
      self.block_animation()
      self.blocking = True
      time.sleep(self.block_time)
      self.not_stand = True
      self.blocking = False
      self.block_cooldown() 
  def knockdown(self):
    '''
    sees how many times the player has been knocked down. if less then three then the "back_up method" starts, if they return.s True then the player returns to the fight
    '''
    self.knochdown_animation()
    if self.tko_count == 3:
      self.game = "loss"
    else:
      back_up = self.back_up()
      if back_up:
        self.tko_count += 1 
        self.knockdown = False 
        self.health = (100 -(self.tko_count * 25))
        self.up_animation()
  def block_cooldown(self):
    '''.
    puts the block method on cooldown
    '''
    self.on_cooldown = True
    pygame.time.set_timer(pygame.USEREVENT,(1000 * self.cooldown ))
    timer = True
    for event in pygame.event.get():
      if event.type == pygame.USEREVENT:
        timer = False
    if timer == False:
      self.on_cooldown = False



  def back_up(self):
    '''
    user must press space a certain amount of times before knockdown_timer becomes False. if they succeed they return to the game, if thy fail its a knockout and the player looses
    '''
    times_pressed = 0
    pygame.time.set_timer(pygame.USEREVENT, 10000)
    timer = True
    while timer:
      for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
          timer = False
        if pygame.event.type == pygame.KEYDOWN:
          if pygame.event.key == pygame.k_SPACE:
            times_pressed += 1
    if times_pressed >=  self.required_presses:
      return(True)
      
  def punch(self):
    self.punch_animation()
    punch_blocked = random.randrange(1,9)
    if punch_blocked == 1:
      self.opponent.block_animation()
    else:
      self.opponent.health  -= 10
      







  def animation_render(self):
    '''
    animation rendering
    '''
    self.stand_list = []
    for i in range(4):
      self.stand_list.append(pygame.image.load(f'assets/Player/p_stand/player_stand{i + 1}.png'))
      
    self.punch_list = []
    
    for i in range(6):
      self.punch_list.append(pygame.image.load(f'assets/Player/p_punch/player_punch{i + 1}.png'))

    self.block_list = []
    for i in range(4):
      self.block_list.append(pygame.image.load(f'assets/Player/p_block/player_block{i + 1}.png'))
      
    self.down_list = []
    self.down_list.append(pygame.image.load(f'assets/Player/p_down/player_down5.png'))

    self.up_list = []
    for i in range(5):
      self.up_list.append(pygame.image.load(f'assets/Player/p_down/player_down{5 - i}.png'))
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
   