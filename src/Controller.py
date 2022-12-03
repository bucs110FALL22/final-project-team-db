from src import Button
from src import Opponent
from src import Player 
from src import Scorebord
from src import Animations
import pygame, sys
from pygame import mixer
class Controller():
    def __init__(self):
      self.SCREEN_X = 960
      self.SCREEN_Y = 540
      self.BLACK = (0,0,0)
      self.screen = pygame.display.set_mode((self.SCREEN_X,self.SCREEN_Y))
      self.clock = pygame.time.Clock()
    def intro_loop(self):
      '''
      begins the game with intro animations, and prompts the player to choose difficulty and how to play if they do not already know
      '''
      a = Animations.Animations(self.screen)
      a.intro()
      p_button = Button.Button('PLAY',0,270,self.screen,"play")
      htp_button = Button.Button('HOWTOPLAY',750,150,self.screen,"howtoplay")
      E = Button.Button("EASY", 0, 270,self.screen, "easy")
      R = Button.Button("REGULAR", 300, 150,self.screen, "regular")
      H = Button.Button("HARD",700,270,self.screen, "hard")  
      sprites = pygame.sprite.Group()
      sprites.add(p_button,htp_button)
      intro = True
      diff_type = True
      while intro:
        self.screen.blit(a.backround_intro,(0,0))
        pygame.event.get()
        p_button.is_being_hovered()
        htp_button.is_being_hovered()
        
        if p_button.play:
          htp_button.kill_self()
          intro = False
        sprites.draw(self.screen)
        sprites.update()
        pygame.display.flip()
      
      self.screen.blit(a.diff, (50,0))
      sprites.add(E,R,H)
      while diff_type:
        self.screen.blit(a.backround_diff,(0,0))
        self.screen.blit(a.diff, (50,0))
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
          return(H.diff)
        sprites.draw(self.screen)
        sprites.update()
        pygame.display.flip()
        
    def match_loop(self,difficulty):
      '''
      main game loop
      args: difficulty(str) dictates how hard the game will be
      '''
      opponent = Opponent.Opponent(difficulty)
      player = Player.Player(difficulty,opponent)
      sb = Scorebord.Scorebord(player,opponent,self.screen)
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
        player.health_check()
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              if pcooldown > 0:
                cooldown_sound = mixer.Sound("assets/Audio/blocking_bell.mp3")
                cooldown_sound.play() 
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
        if punched == False and o_punch > 50 and player.health > 0:
          opponent.punch(player)
          o_punch = 0
        

        else:
          punched = False
          o_punch += 1
        
        sprites.draw(self.screen)
        sprites.update(.25)
        pygame.display.flip()
        clock.tick(30)
        opponent.health_check()
        pcooldown -= 1
        bcooldown -= 1
        if player.game == "loss":
          self.screen.fill(self.BLACK)
          sb.loss()
          pygame.display.flip()
          game_loop = False
        if opponent.game == "loss":
          self.screen.fill(self.BLACK)
          sb.winner()
          pygame.display.flip()
          game_loop = False