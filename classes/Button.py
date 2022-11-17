import pygame
from pygame.locals import *
from Animations import Animations 

class Button():
    def __init__(self,file_name,xpos,ypos,screen,b_type,):
      self.file_name = file_name
      self.x_pos = xpos
      self.y_pos = ypos
      self.clicked = False 
      self.diff = "none"
      self.a = Animations(screen)
      self.button = pygame.image.load("assets/Button_imgs/" + self.file_name + ".png").convert_alpha()
      self.screen = screen
      self.rect = self.button.get_rect()
      self.rect.topleft = (xpos,ypos)
      self.b_type = (b_type).upper()
      
    def click_recations(self):
      
      if self.b_type == "PLAY":
        self.a.intro_to_diff()
        self.difficulty_buttons()
        print("start game sequence")
        
      if self.b_type == "HOWTOPLAY":
        print("bring up info sheet")
        
      if self.b_type == "EASY":
        self.diff = "easy"
        
      if self.b_type == "REGULAR":
        self.diff = "regular"
      
      if self.b_type == "HARD":
        self.diff = "hard"

      
    def print(self):
        self.screen.blit(self.button,(self.x_pos,self.y_pos))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
          print(pos)
          self.is_being_hovered()
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
              print("hov")
              self.click_recations()
    def check(self):
      print("check")
    def is_being_hovered(self):
        
        self.button = pygame.image.load(("assets/Button_imgs/" + self.file_name + "HOV" + ".png")).convert_alpha()
        self.screen.blit(self.button,(self.x_pos,self.y_pos))


    def difficulty_buttons(self):
      E = Button(0,270)
      R = Button(300,270)
      H = Button(600,270)
    def difficulty(self):
      return(self.diff)
    