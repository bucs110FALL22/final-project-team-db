import pygame 

class Animations():
  def __init__(self):
    pass
  def intro(self):
    intro_pic = pygame.image.load('assets/intro/Punch_it_intro_1.png').convert_alpha

    pic_num = 1
    for i in range(64):
      intro_pic = pygame.image.load(f'assets/intro/Punch_it_intro_{pic_num}.png').convert_alpha()
  screen.blit(intro_pic,(0,0))
  pygame.display.update()
  pic_num += 2   
  def intro_to_diff(self):

  def diff_to_match(self):

  def player_stanf(self):
    
  def player_punch(self):

  def player_block(self):

  def player_fall(self):

  def player_getup(self):
    
  def opponent_stand(self): 
    
  def opponent_punch(self):

  def opponent_block(self):

  def opponentr_fall(self):

  def opponent_getup(self):

  def win(self):
  def loss(self):
  

    