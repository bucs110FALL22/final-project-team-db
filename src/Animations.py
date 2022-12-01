import pygame 
import time
from pygame import mixer

class Animations():
  
  def __init__(self,screen):
    self.screen = screen
    self.backround_intro = pygame.image.load('assets/intro/Punch_it_intro_127.png').convert_alpha()
    self.backround_diff = pygame.image.load('assets/intro_to_diff/intro_to_diff_154.png').convert_alpha()
    self.diff = pygame.image.load(("assets/Button_imgs/difficulty.png")).convert_alpha()
  def match_backround(self):
    pic = pygame.image.load('assets/diff_to_match/intro_to_diff_289.png').convert_alpha()
    self.screen.blit(pic, (0, 0))
  def intro(self):
    intro_pic = pygame.image.load('assets/intro/Punch_it_intro_1.png').convert_alpha()

    pic_num = 1
    for i in range(64):
      intro_pic = pygame.image.load(f'assets/intro/Punch_it_intro_{pic_num}.png').convert_alpha()
      self.screen.blit(intro_pic,(0,0))
      pygame.display.update()
      time.sleep(.1)
      pic_num += 2   
    start_sound = mixer.Sound("assets/Audio/bell_start.wav")
    start_sound.play()
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

     
