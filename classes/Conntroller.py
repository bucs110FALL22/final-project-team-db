import Button
import Opponent
import Player
import Scorebord
import Animations
import pygame

pygame.init()
screen = pygame.display.set_mode((960,540))
screen.fill((0,0,255))

def intro_loop(screen):
  a = Animation()
  a.intro()
  a = Animations()
  p_button = Button('PLAY',0,0,screen,"play")
  htp_button = Button('HOWTOPLAY',300,0,screen,"howtoplay")
  a.intro()
  pygame.display.update()
  while True:
    p_button.print()
    htp_button.print()
    difficulty = p_btton.difficulty()
    if difficulty not "none":
      a.diff_to_match()
      break
    
# intro animation
# intro loop (waiting for them to click play )
#match loop
def main_loop(screen)
difficulty = intro_loop()
player = Player(difficulty)
opponent = Opponent(difficulty)
a = Animation()
while True:
  a.player_stand()
  a.opponent_stand()
  if event.type == pygame.K_up:
    player.punch()
    a.player_punch()
  if event.type == pygame.K_down:
    player.block
    a.player_block()