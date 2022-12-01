import pygame


class Scorebord():   
  def __init__(self,player,opponent,screen):
    self.screen = screen
    self.NAME_FONT_SIZE = 15
    self.GAME_END_FONT_SIZE = 50
    self.HEALTH_BAR_LENGTH_MULTIPLYER = 4
    self.HEALTH_BAR_Y_POS = 20
    self.P_HEALTH_BAR_X_POS = 0
    self.O_HEALTH_BAR_X_POS = 500
    self.END_TEXT_X_POS = 370
    self.END_TEXT_Y_POS = 200
    self.O_NAME_X_POS = 500
    self.P_NAME_X_POS = 0
    self.NAME_Y_POS = 0
    self.player = player
    self.opponent = opponent
    self.current_round = 1
    self.p_health = 100
    self.o_health = 100
  def health_bars(self):
    '''
    creates the health bars of the player and opponent and get smaller when health decreases
    '''
    pygame.display.set_caption("show text")
    font = pygame.font.Font('assets/fonts/Komyca3DFreeVersionItalic-rg1WO.ttf',self.NAME_FONT_SIZE)
    ptext = font.render('Player', True, "red")
    ptextRect = ptext.get_rect()
    ptextRect.topleft = (self.P_NAME_X_POS, self.NAME_Y_POS)
    self.screen.blit(ptext,ptextRect)
    otext = font.render('Opponent', True, "red")
    otextRect = otext.get_rect()
    otextRect.topleft = (self.O_NAME_X_POS, self.NAME_Y_POS)
    self.screen.blit(otext,otextRect)
    pygame.draw.rect(self.screen,"red",(self.P_HEALTH_BAR_X_POS,self.HEALTH_BAR_Y_POS,(self.player.health * self.HEALTH_BAR_LENGTH_MULTIPLYER),self.HEALTH_BAR_Y_POS))
    pygame.draw.rect(self.screen,"red",(self.O_HEALTH_BAR_X_POS,self.HEALTH_BAR_Y_POS,(self.opponent.health * self.HEALTH_BAR_LENGTH_MULTIPLYER),self.HEALTH_BAR_Y_POS))
  
  def winner(self):
    pygame.display.set_caption("show text")
    font = pygame.font.Font('assets/fonts/Komyca3DFreeVersionItalic-rg1WO.ttf', self.GAME_END_FONT_SIZE)
    text = font.render('YOU WIN!', True, "red")
    textRect = text.get_rect()
    textRect.topleft = (self.END_TEXT_X_POS, self.END_TEXT_Y_POS)
    self.screen.blit(text,textRect)

  def loss(self):
    pygame.display.set_caption("show text")
    font = pygame.font.Font('assets/fonts/Komyca3DFreeVersionItalic-rg1WO.ttf', self.GAME_END_FONT_SIZE)
    text = font.render('--YOU LOOSE--', True, "red")
    textRect = text.get_rect()
    textRect.topleft = (self.END_TEXT_X_POS, self.END_TEXT_Y_POS)
    self.screen.blit(text,textRect)
    