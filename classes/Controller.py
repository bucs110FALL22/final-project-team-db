from Button import Button
from Opponent import Opponent
from Player import Player 

# import Scorebord
from Animations import Animations
import pygame, sys
import time
pygame.init()
screen = pygame.display.set_mode((960,540))
clock = pygame.time.Clock()
screen.fill((0,0,255))

def intro_loop(screen):
  a = Animations(screen)
  b = Animations(screen)
  a.intro()

  p_button = Button('PLAY',0,270,screen,"play")
  htp_button = Button('HOWTOPLAY',750,150,screen,"howtoplay")
  E = Button("EASY", 0, 270,screen, "easy")
  R = Button("REGULAR", 300, 150,screen, "regular")
  H = Button("HARD",700,270,screen, "hard")  
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
  screen.blit(diff, (15,0))
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
    
def match_loop(screen,difficulty):
  all_sprites = pygame.sprite.Group()
  opponent = Opponent(difficulty)
  player = Player(difficulty,opponent)
  
  all_sprites.add(player)
  moving_sprites = pygame.sprite.Group()
  moving_sprites.add(opponent,player)
  backround = pygame.image.load('assets/diff_to_match/intro_to_diff_289.png').convert_alpha()
  while True:
    screen.blit(backround,(0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
    	  player.punch()
    moving_sprites.draw(screen)
    moving_sprites.update(.5)
    pygame.display.flip()
    clock.tick(30)
    
match_loop(screen, "easy")