from Button import Button
from Opponent import Opponent
from Player import Player 
# import Scorebord
from Animations import Animations
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((960,540))
screen.fill((0,0,255))

def intro_loop(screen):
  a = Animations(screen)
  a.intro()

  p_button = Button('PLAY',0,270,screen,"play")
  htp_button = Button('HOWTOPLAY',750,150,screen,"howtoplay")
  E = Button("EASY", 0, 270,screen, "easy")
  R = Button("REGULAR", 300, 150,screen, "regular")
  H = Button("HARD",700,270,screen, "hard")
  pygame.display.update()
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
  player = Player(difficulty)
  opponent = Opponent(difficulty)
  a = Animations(screen)
  while True:
    pygame.event.get()
    a.opponent_stand()
    a.opponent_stand()
    a.opponent_punch()
    a.opponent_stand()
    a.opponent_block()
    a.opponent_stand()
    a.opponent_fall()
    time.sleep(2)
    a.opponent_getup()
    a.opponent_stand()
    # for event in pygame.event.get():
    #   if event.type == pygame.K_up:
    #     player.punch()
    #     a.player_punch()
    #   if event.type == pygame.K_down:
    #     player.block
    #     a.player_block()

diff = intro_loop(screen)
match_loop(screen,diff)