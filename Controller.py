from Button import Button
from Opponent import Opponent
from Player import Player 
from Scorebord import Scorebord
from Animations import Animations
import pygame, sys

class Controller():
    def __init__(self):
      self.screen = pygame.display.set_mode((960,540))
      self.clock = pygame.time.Clock()
    def intro_loop(self):
      self.screen.fill((0,0,255))
      a = Animations(self.screen)
      a.intro()

      p_button = Button('PLAY',0,270,self.screen,"play")
      htp_button = Button('HOWTOPLAY',750,150,self.screen,"howtoplay")
      E = Button("EASY", 0, 270,self.screen, "easy")
      R = Button("REGULAR", 300, 150,self.screen, "regular")
      H = Button("HARD",700,270,self.screen, "hard")  
      sprites = pygame.sprite.Group()
      sprites.add(p_button,htp_button)
      intro = True
      diff_type = True
      backround_intro = pygame.image.load('assets/intro/Punch_it_intro_127.png').convert_alpha()
      backround_diff = pygame.image.load('assets/intro_to_diff/intro_to_diff_154.png').convert_alpha()
      while intro:
        self.screen.blit(backround_intro,(0,0))
        pygame.event.get()
        p_button.is_being_hovered()
        htp_button.is_being_hovered()
        
        if p_button.play:
          htp_button.kill_self()
          intro = False
        sprites.draw(self.screen)
        sprites.update()
        pygame.display.flip()
      diff = pygame.image.load(("assets/Button_imgs/difficulty.png")).convert_alpha()
      self.screen.blit(diff, (50,0))
      sprites.add(E,R,H)
      while diff_type:
        self.screen.blit(backround_diff,(0,0))
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
        sprites.draw(self.screen)
        sprites.update()
        pygame.display.flip()
        
    def match_loop(self,difficulty):
      opponent = Opponent(difficulty)
      player = Player(difficulty,opponent)
      sb = Scorebord(player,opponent,self.screen)
      sprites = pygame.sprite.Group()
      sprites.add(opponent,player)
      backround = pygame.image.load('assets/diff_to_match/intro_to_diff_289.png').convert_alpha()
      game_loop = True
      clock = pygame.time.Clock()
      pcooldown = 0
      bcooldown = 0
      punched = False
      o_punch = 0
      while game_loop:
        self.screen.blit(backround,(0,0))
        sb.health_bars()
        opponent.health_check()
        player.health_check()
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
                punched = True
                pcooldown = 30
            if event.key == pygame.K_DOWN:
              if bcooldown > 0:
                pass
              else:
                player.block()
                bcooldown = 50
        if punched == False and o_punch > 10:
          opponent.punch(player)
          o_punch = 0

        else:
          punched = False
          o_punch += 1
        sprites.draw(self.screen)
        sprites.update(.25)
        pygame.display.flip()
        clock.tick(30)
        pcooldown -= 1
        bcooldown -= 1
        if player.game == "loss":
          self.screen.fill((0,0,0))
          sb.loss()
          pygame.display.flip()
          game_loop = False
        if opponent.game == "loss":
          self.screen.fill((0,0,0))
          sb.winner()
          pygame.display.flip()
          game_loop = False