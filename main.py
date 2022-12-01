from src import Controller
import pygame
def main():
  pygame.init()
  c = Controller.Controller()
  diff = "easy"#c.intro_loop()
  c.match_loop(diff)
if __name__ == "__main__":
  main()

