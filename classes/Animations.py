import pygame 

class Animations():
#TODO: remove
  def __init__(self,screen):
    self.screen = screen
  def intro(self):
    intro_pic = pygame.image.load('assets/intro/Punch_it_intro_1.png').convert_alpha()

    pic_num = 1
    for i in range(64):
      intro_pic = pygame.image.load(f'assets/intro/Punch_it_intro_{pic_num}.png').convert_alpha()
      self.screen.blit(intro_pic,(0,0))
      pygame.display.update()
      pic_num += 2   
  def intro_to_diff(self):
    pic = pygame.image.load('assets/intro_to_diff/intro_to_diff_128.png').convert_alpha()

    pic_num = 128
    for i in range(14):
      pic = pygame.image.load(f'assets/intro_to_diff/intro_to_diff_{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 2   
  def diff_to_match(self):
    pic = pygame.image.load('assets/diff_to_match/intro_to_diff_128.png').convert_alpha()
    pic_num = 175
    for i in range(57):
      pic = pygame.image.load(f'assets/diff_to_/intro_to_diff_{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 2   
  def opponent_stand(self):
    pic = pygame.image.load('assets/Opponent/stand_animation/stand1.png').convert_alpha()
    
    pic_num = 1
    for i in range(4):
      pic = pygame.image.load(f'assets/Opponent/stand_animation/stand{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 1   
  def opponent_punch(self):
    pic = pygame.image.load('assets/Opponent/punch_animation/Punch1.png').convert_alpha()
    
    pic_num = 1
    for i in range(11):
      pic = pygame.image.load(f'assets/Opponent/punch_animation/Punch{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 1   
  def opponent_block(self):
    pic = pygame.image.load('assets/Opponent/block_animation/block1.png').convert_alpha()
    
    pic_num = 1
    for i in range(5):
      pic = pygame.image.load(f'assets/Opponent/block_animation/block{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 1   
  def opponent_fall(self):
    pic = pygame.image.load('assets/Opponent/knockdown_animation/knockdown1.png').convert_alpha()
    
    pic_num = 1
    for i in range(4):
      pic = pygame.image.load(f'assets/Opponent/knockdown_animation/knockdown{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 1   
  def opponent_getup(self):
    pic = pygame.image.load('assets/Opponent/backup_animation/revoery1.png').convert_alpha()
    
    pic_num = 1
    for i in range(4):
      pic = pygame.image.load(f'assets/Opponent/backup_animation/revoery{pic}.png').convert_alpha()
      self.screen.blit(pic,(0,0))
      pygame.display.update()
      pic_num += 1       
  # def player_stand(self): 
    
  # def player_punch(self):

  # def player_block(self):

  # def player_fall(self):

  # def player_getup(self):

  # def win(self):
  # def loss(self):
  

    