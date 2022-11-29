import pygame
from pygame.locals import *
import time
from threading import Timer
from Animations import Animations
class Button(pygame.sprite.Sprite):
    def __init__(self,file_name,xpos,ypos,screen,b_type,):
        super().__init__()
        self.file_name = file_name
        self.x_pos = xpos
        self.y_pos = ypos
        self.clicked = False
        self.a = Animations(screen)
        self.diff = "none"
        self.screen = screen
        self.b_type = (b_type).upper()
        self.play = False
        self.current_sprite = 0
        self.img_load()
        
        self.image = self.img_list[self.current_sprite]
        self.rect = pygame.image.load("assets/Button_imgs/" + self.file_name + ".png").get_rect()
        self.rect.topleft = (self.x_pos,self.y_pos)
    def update(self):
      self.image = self.img_list[int(self.current_sprite)]
      
    def click_recations(self):
      if self.b_type == "PLAY":
        self.a.intro_to_diff()
        self.play = True
        print("start game sequence")
        self.kill_self()
        
      if self.b_type == "HOWTOPLAY":
        print("bring up info sheet")
      if self.b_type == "EASY":
        self.diff = "easy"
        self.kill_self()
      if self.b_type == "REGULAR":
        self.diff = "regular"
        self.kill_self()
      if self.b_type == "HARD":
        self.diff = "hard"
        self.kill_self()
      
    def is_being_hovered(self): 
      pos = pygame.mouse.get_pos()
      if self.rect.collidepoint(pos):
        self.current_sprite = 1
        b_timer = Timer(.3,self.unhover)
        b_timer.start()
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            print("hov")
            self.click_recations()
         
    def unhover(self):
      self.current_sprite = 0
    def img_load(self):
      self.img_list = []
  
      self.img_list.append(pygame.image.load("assets/Button_imgs/" + self.file_name + ".png").convert_alpha())
      self.img_list.append(pygame.image.load("assets/Button_imgs/" + self.file_name + "HOV" + ".png").convert_alpha())

    def difficulty(self):
      return(self.diff)
    def kill_self(self):
      self.kill()