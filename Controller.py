from Button import Button
from Opponent import Opponent
from Player import Player 
from Scorebord import Scorebord
from Animations import Animations
import pygame, sys

class Controller():
    def __init__(self):
      pygame.init()
      self.screen = pygame.display.set_mode((960,540))
      self.clock = pygame.time.Clock()
    def intro_loop(self):
      self.screen.fill((0,0,255))
      a = Animations(self.screen)
      b = Animations(self.screen)
      a.intro()
    
      p_button = Button('PLAY',0,270,self.screen,"play")
      htp_button = Button('HOWTOPLAY',750,150,self.screen,"howtoplay")
      E = Button("EASY", 0, 270,self.screen, "easy")
      R = Button("REGULAR", 300, 150,self.screen, "regular")
      H = Button("HARD",700,270,self.screen, "hard")  
      p_button.print()
      htp_button.print()
      pygame.display.update()
      intro = True
      diff_type = True
      while intro:
        pygame.event.get()
        play = p_button.is_being_hovered()
        htp_button.is_being_hovered()
    
        if p_button.play:
          intro = False
      diff = pygame.image.load(("assets/Button_imgs/difficulty.png")).convert_alpha()
      self.screen.blit(diff, (15,0))
      E.print()
      R.print()
      H.print()
      while diff_type:
        pygame.event.get()
        E.is_being_hovered()
        R.is_being_hovered()
        H.is_being_hovered()
        if E.diff == "easy":
          diff_type = False
          a.diff_to_match()
          return(E.diff)
        if R.diff == "regular":
          diff_type = False
          a.diff_to_match()
          return(R.diff)
        if H.diff == "hard":
          diff_type = False
          a.diff_to_match()
          return(R.diff)
        pygame.display.flip()
        pygame.display.update()
        
    def match_loop(self,difficulty):
      all_sprites = pygame.sprite.Group()
      opponent = Opponent(difficulty)
      player = Player(difficulty,opponent)
      sb = Scorebord(player,opponent,self.screen)
      all_sprites.add(player)
      sprites = pygame.sprite.Group()
      sprites.add(opponent,player)
      backround = pygame.image.load('assets/diff_to_match/intro_to_diff_289.png').convert_alpha()
      game_loop = True
      clock = pygame.time.Clock()
      pcooldown = 0
      bcooldown = 0
      while game_loop:
        self.screen.blit(backround,(0,0))
        sb.health_bars()
        opponent.health_check()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              if pcooldown > 0:
                pass #play beep audio
              else:
                player.punch(opponent)
                pcooldown = 30
            if event.key == pygame.K_DOWN:
              if bcooldown > 0:
                pass #play beep audio
              else:
                player.block()
                bcooldown = 50
        opponent.punch(player)
        sprites.draw(self.screen)
        sprites.update(.25)
        pygame.display.flip()
        clock.tick(30)
        pcooldown -= 1
        bcooldown -= 1
        if player.game == "loss":
          game_loop = False
        if opponent.game == "loss":
          game_loop = False