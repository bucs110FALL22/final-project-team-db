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
    
  def update(self,speed):
    
    self.current_sprite += speed
    if int(self.current_sprite) >= len(self.sprites):
      self.current_sprite = 0
      if self.not_stand:
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
    else:
      self.block_animation()
      self.blocking = True
      time.sleep(self.block_time)
      self.blocking = False
      self.block_cooldown() 
  def knockdown(self):
    '''
    sees how many times the player has been knocked down. if less then three then the "back_up method" starts, if they returns True then the player returns to the fight
    '''
    self.knochdown_animation()
    if self.tko_count == 3:
      pass#break game loop, start loss sequence
    else:
      back_up = self.back_up()
      if back_up:
        self.tko_count += 1 
        self.knockdown = False 
        self.health = (100 -(self.tko_count * 25))
        self.back_up_animation()
  def block_cooldown(self):
    '''.
    puts the block method on cooldown
    '''
    self.on_cooldown = True
    time.sleep(self.cooldown)
    self.on_cooldown = False


  def knockdown_timer(self):
    '''
    a timer for the amount of time the player has to get up
    '''
    self.mash_time = True
    time.sleep(10)
    self.mash_time = False
  def back_up(self):
    '''
    user must press space a certain amount of times before knockdown_timer becomes False. if they succeed they return to the game, if thy fail its a knockout and the player looses
    '''
    times_pressed = 0
    self.knockdown_timer()
    while self.mash_time:
      if pygame.event.type == pygame.KEYDOWN:
        if pygame.event.key == pygame.k_SPACE:
          times_pressed += 1
    if times_pressed >=  self.required_presses:
      return(True)
    else:
      pass#stop game loop and start loss sequence
  
  def punch(self):
    print("punch")
    self.punch_animation()
    # punch_blocked = random.randrange(1,self.punch_difficulty)
    # if punch_blocked == 1:
    #   self.Opponent.block_animation()
    #   self.Opponent.blocked = True 
    # else:
    #   self.Opponent.health  -= 10
    #   print(self.Opponent.health)
      







  def animation_render(self):
    '''
    animation for when the player stands
    '''
    self.stand_list = []
    for i in range(4):
      self.stand_list.append(pygame.image.load(f'assets/Player/p_stand/player_stand{i + 1}.png'))
      
    self.punch_list = []
    
    for i in range(6):
      self.punch_list.append(pygame.image.load(f'assets/Player/p_punch/player_punch{i + 1}.png'))

  def stand_animation(self):
    self.sprites = self.stand_list
  def punch_animation(self):
    self.sprites = self.punch_list
    self.not_stand = True