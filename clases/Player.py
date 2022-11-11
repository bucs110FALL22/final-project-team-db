import pygame
import time
import random
class Player(pygame.sprite.Sprite):
    def __init__(self,image_file,difficulty):
      super().__init__(self)
      self.health = 100
      if self.health == 0:
        self.knockdown()
      self.blocking = False
      self.cooldown = 0
      self.position = (x,y)
      self.block_time = 0
      self.cooldown = 0
      self.punch_difficulty = 0
      self.tko_count = 0
      self.knockdown = False
      self.on_cooldown = False
      self.required_pressess = (50 * (self.tko_count + 1))
      self.image = pygame.image.load().alpha#first keyframe
      self.blocking_difficulty(difficulty)
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
        break
      else:
        block_animation()
        self.blocking = True
        time.sleep(self.block_time)
        self.blocking = False
        self.block_cooldown() 
    def knockdown(self):
      '''
      sees how many times the player has been knocked down. if less then three then the "back_up method" starts, if they returns True then the player returns to the fight
      '''
      knochdown_animation()
      if tko_count == 3:
        #break game loop, start loss sequence
      else:
        back_up = self.back_up()
        if back_up:
        self.tko_count += 1 
        self.knockdown = False 
        self.health = (100 -(self.tko_count * 25))
        back_up_animation
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
      knockdown_timer()
      while self.mash_time:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.k_SPACE:
            times_pressed += 1
      if times_pressed >=  self.required_presses:
        return(True)
      else:
        #stop game loop and start loss sequence
    
    def punch(self,Opponent):
      punch_blocked = random.randrange(1,self.punch_difficulty)
      if punch_blocked == 1:
        Opponent.block_animation()
        break
      else:
        Opponent.health  -= 10 









    def punch_animation(self):
      '''
      animation for when the player punches
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
      time.sleep(.2)
      self.image = pygame.image.load()# keyframe 3
    def block animation(self):
      '''
      animation for when the player blocks
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
    def standing_animation(self):
      '''
      looping animation for when the player is standing
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
    def knockdown_animation(self):
      '''
      animaion for when the player in knocked down
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
      time.sleep(.2)
      self.image = pygame.image.load()# keyframe 3
      
    def back_up_animation(self):
      '''
      animation for when the player gets back up
      '''
      self.image = pygame.image.load()#keyframe 1
      time.sleep(.2)
      self.image = pygame.image.load()#keyframe 2
      time.sleep(.2)
      self.image = pygame.image.load()# keyframe 3