
from Controller import Controller
import pygame
def main():
  pygame.init()
  c = Controller()
  # diff = c.intro_loop()
  diff = "easy"
  c.match_loop(diff)
if __name__ == "__main__":
  main()