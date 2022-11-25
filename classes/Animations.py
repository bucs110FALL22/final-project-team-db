import pygame 
import time


class Animations():
  
  def __init__(self,screen):
    self.screen = screen
  def match_backround(self):
    pic = pygame.image.load('assets/diff_to_match/intro_to_diff_289.png').convert_alpha()
    self.screen.blit(pic, (0, 0))#1
    # pygame.display.update()
  def intro(self):
    intro_pic = pygame.image.load('assets/intro/Punch_it_intro_1.png').convert_alpha()

    pic_num = 1
    for i in range(64):
      intro_pic = pygame.image.load(f'assets/intro/Punch_it_intro_{pic_num}.png').convert_alpha()
      self.screen.blit(intro_pic,(0,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 2   
  def intro_to_diff(self):
    pic = pygame.image.load('assets/intro_to_diff/intro_to_diff_128.png').convert_alpha()

    pic_num = 128
    for i in range(14):
      pic = pygame.image.load(f'assets/intro_to_diff/intro_to_diff_{pic_num}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 2   
  def diff_to_match(self):
    pic = pygame.image.load('assets/diff_to_match/intro_to_diff_175.png').convert_alpha()
    pic_num = 175
    for i in range(57):
      pic = pygame.image.load(f'assets/diff_to_match/intro_to_diff_{pic_num}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.flip()
      time.sleep(.1)
      pic_num += 2   
  def opponent_stand(self):
    pic = pygame.image.load('assets/Opponent/stand_animation/stand1.png').convert_alpha()
    pic_num = 1
    for i in range(4):

      pic = pygame.image.load(f'assets/Opponent/stand_animation/stand{pic_num}.png').convert_alpha()
      self.match_backround()
      self.screen.blit(pic,(270,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 1   
  def opponent_punch(self):
    pic = pygame.image.load('assets/Opponent/punch_animation/punch1.png').convert_alpha()
    
    pic_num = 1
    for i in range(11):
      pic = pygame.image.load(f'assets/Opponent/punch_animation/punch{pic_num}.png').convert_alpha()
      self.match_backround()
      self.screen.blit(pic,(270,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 1   
  def opponent_block(self):
    pic = pygame.image.load('assets/Opponent/block_animation/block1.png').convert_alpha()
    
    pic_num = 1
    for i in range(5):
      pic = pygame.image.load(f'assets/Opponent/block_animation/block{pic_num}.png').convert_alpha()
      self.match_backround()
      self.screen.blit(pic,(270,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 1   
  def opponent_fall(self):
    pic = pygame.image.load('assets/Opponent/knockdown_animation/knockdown1.png').convert_alpha()
    
    pic_num = 1
    for i in range(4):
      pic = pygame.image.load(f'assets/Opponent/knockdown_animation/knockdown{pic_num}.png').convert_alpha()
      self.match_backround()
      self.screen.blit(pic,(270,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 1   
  def opponent_getup(self):
    pic = pygame.image.load('assets/Opponent/backup_animation/recovery1.png').convert_alpha()
    
    pic_num = 1
    for i in range(4):
      pic = pygame.image.load(f'assets/Opponent/backup_animation/recovery{pic_num}.png').convert_alpha()
      self.match_backround()
      self.screen.blit(pic,(270,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 1       
  def player_stand(self): 
    pic = pygame.image.load('assets/Player/p_stand/player_stand1.png').convert_alpha()
        
    pic_num = 1
    for i in range(4):
      pic = pygame.image.load(f'assets/Player/p_stand/player_stand{pic_num}.png').convert_alpha()
      self.match_backround()
      self.screen.blit(pic,(100,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 1    
  # def player_punch(self):

  # def player_block(self):

  # def player_fall(self):

  # def player_getup(self):

  # def win(self):
  # def loss(self):
  

  def stand(self):
      pic = pygame.image.load('assets/Player/p_stand/player_stand1.png').convert_alpha()
      pic2 = pygame.image.load('assets/Opponent/stand_animation/stand1.png').convert_alpha()    
      pic_num = 1
      for i in range(4):
        pic = pygame.image.load(f'assets/Player/p_stand/player_stand{pic_num}.png').convert_alpha()
        self.match_backround()
        pic2 = pygame.image.load(f'assets/Opponent/stand_animation/stand{pic_num}.png').convert_alpha()
        self.match_backround()
        self.screen.blit(pic2,(270,0))
        self.screen.blit(pic,(300,0))
        pygame.display.update()
        pic_num += 1   