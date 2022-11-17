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
  htp_button = Button('HOWTOPLAY',775,150,screen,"howtoplay")
  pygame.display.update()
  while True:
    p_button.print()
    htp_button.print()
    # difficulty = p_button.difficulty()
    # # if difficulty == "none":
    #   pass
    # else:
    #   a.diff_to_match()
    #   break
    p_button.check()
    pygame.display.update()
# intro animation
# intro loop (waiting for them to click play )
#match loop
def main_loop(screen):
  difficulty = intro_loop()
  player = Player(difficulty)
  opponent = Opponent(difficulty)
  a = Animations()
  while True:
    a.player_stand()
    a.opponent_stand()
    if event.type == pygame.K_up:
      player.punch()
      a.player_punch()
    if event.type == pygame.K_down:
      player.block
      a.player_block()

intro_loop(screen)