import pygame
import random
from threading import Timer
from pygame import mixer

class Player(pygame.sprite.Sprite):
  def __init__(self,difficulty,Opponent):
    super().__init__()
    self.TKO = 3
    self.STRENGTH = 10
    self.RECOVERY_HEALTH = 100
    self.KNOCKDOWN_HEALTH_SUBTRACT = 25
    self.REQUIRED_PRESSES_VARIABLE = 25
    self.KNOCKDOWN_TIMER_TIME = 10000
    self.MAX_PUNCH = 3
    self.X_POS = 150
    self.Y_POS = 0
    self.health = 100
    self.sprites = []
    self.animation_render()
    self.stand_animation()
    self.current_sprite = 0
    self.image = self.sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.not_stand = False
    
    self.rect.topleft = (self.X_POS,self.Y_POS)
    self.stand = True
    self.blocking = False
    self.block_time = 0
    self.punch_difficulty = 2
    self.tko_count = 0
    self.block_grace = 0
    self.on_cooldown = False
    
    self.required_presses = ( self.REQUIRED_PRESSES_VARIABLE * (self.tko_count + 1))
    self.blocking_difficulty(difficulty)
    self.opponent = Opponent
    self.punch_count = 0
    self.game = ""
    self.mash_call = False
    self.get_back_up = False
    
  def health_check(self):
    '''Checks if player has gone below 0 health, if so then it initiated the knockdown animation and knockdown function'''
    if self.health <= 0:
      self.down_animation()
      self.knockdown()
  def update(self,speed):
    '''updates sprites for animations
        args: speed(int), how fast the frames should rotate
    '''
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
    args: difficulty(str) dictates the difficulty of the game
    '''
    if difficulty == "easy":
      self.block_grace = .25
      self.punch_difficulty = 7
    elif difficulty == "regular":
      self.block_grace= .2

      self.punch_difficulty = 5
    elif difficulty == "hard":
      self.block_grace = .15
      self.punch_difficulty = 3

  def block(self):
    '''
    makes the player unable to be hit by enemy
    '''
    self.block_animation()
    self.blocking = True
    p_timer = Timer(self.block_grace, self.unblock)
    p_timer.start()
  def unblock(self):
    self.not_stand = True
    self.blocking = False
  def knockdown(self):
    '''
    sees how many times the player has been knocked down. if less then three then the "back_up method" starts, backup(mash) is completed then the player returns to the fight
    '''
    if self.tko_count == self.TKO:
      self.game = "loss"
    else:
      self.back_up()
      if self.get_back_up:
        self.tko_count += 1  
        self.mash_call = False
        self.get_back_up = False
        self.health = (self.RECOVERY_HEALTH -(self.tko_count * self.KNOCKDOWN_HEALTH_SUBTRACT))
        self.up_animation()
  def back_up(self):
    '''
    used as a timer to call mash sequence
    '''
    if self.mash_call == False:
      self.mash_call = True
      m_timer = Timer(1,self.mash)
      m_timer.start()

  def mash(self):
    '''
    checks for times space bar has been hit in a ten second period, if enough presses occur player will return to game, if not enough then game ends
    '''
    
    pygame.time.set_timer(pygame.USEREVENT, self.KNOCKDOWN_TIMER_TIME)
    timer = True
    times_pressed = 0
    while timer:
  
      for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
          timer = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            times_pressed += 1
            print(times_pressed)
    if times_pressed >=  self.required_presses:
      self.get_back_up = True
      
    else:
      print("loss")
      self.game = "loss"
      
  def punch(self,opponent):
    '''
    punches opponent, decided based on probability if it hits or not, if hit, opponent gets dealt damage, if blocked then opponent block animation
    args: opponent(class) 
    '''
    if self.punch_count == self.MAX_PUNCH:
      opponent.vulnerable = False
      self.punch_count = 0 
    self.punch_animation()
    # punch_sound = mixer.Sound("assets/Audio/Punch.wav")
    # punch_sound.play()
    punch_blocked = random.randrange(1,(self.punch_difficulty))
    if self.opponent.vulnerable == False:
      opponent.block_animation()
      punch_sound = mixer.Sound("assets/Audio/Punch.wav")
      punch_sound.play()
    elif punch_blocked <= (1 + self.punch_count):
      opponent.block_animation()
      punch_sound = mixer.Sound("assets/Audio/Punch.wav")
      punch_sound.play()
    else:
      hit_sound = mixer.Sound("assets/Audio/oof_opponent.wav")
      hit_sound.play()
      self.opponent.hit()
      self.opponent.health -= self.STRENGTH
      self.punch_count += 1
      print(self.punch_count)
      
  def animation_render(self):    
    '''
   renders all animations into their respected sprite list
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
    self.down_list.append(pygame.image.load("assets/Player/p_down/player_down5.png").convert_alpha())
      

    self.up_list = []
    for i in range(5):
      self.up_list.append(pygame.image.load(f'assets/Player/p_down/player_down{5 - i}.png').convert_alpha())
      
  def stand_animation(self):
    '''
    changes the sprite to standing loop
    '''
    self.sprites = self.stand_list
  def punch_animation(self):
    '''
    changes the sprite to punch loop then back to stand
    '''
    self.sprites = self.punch_list
    self.not_stand = True

  def block_animation(self):
    '''
    changes the sprite to block loop then back to stand
    '''
    self.sprites = self.block_list

  def down_animation(self):
    '''
    changes the sprite to down loop
    '''
    self.rect.topleft = (0,0)
    self.sprites = self.down_list
  def up_animation(self):
    '''
    changes sprite to up loop then back to stand
    '''
    self.rect.topleft = (0,0)
    self.sprites = self.up_list
    self.not_stand = True
   