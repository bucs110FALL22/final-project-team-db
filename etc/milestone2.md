# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1
class Player:
  def __init__(self,image_file,difficulty):
    self.health = 100
    self.blocking = False
    self.blocktime = 0
    self.cooldown = 0
    self.position = (x,y)
    if self.blocking = True:
      *wait* difficulty
      block_timer(self.cooldown)
    self.tko_count = 0
    self.knockdown = False
    if self.knockdown = True:
      knockdown(self.tko_count)
  def blocking_dificulty(difficulty):
    if difficulty == "Easy":
      self.difficulty = 3
      self.cooldown = 1
    elif difficulty == "Regular":
      self.difficulty = 2
      self.cooldown = 2
    elif difficulty == "Hard":
      self.difficulty = 1.5
      self.cooldown = 3
      
  def block(cooldown_time)
    self.blocking = True
    *wait* certain amount of time
    while *time* < difficulty:
      self.blocking = False:
      
  def knockdown(tko_count):
    if tko_count = 3 
      *end game*40
    required_spams = 100 * (tko_count + 1)
    spam count = 0
    while *time* < 10
      spam count = *button spam* 
    if spam count > required_spams 
    self.knockdown = False 
    self.tko_count += 1 
## Class Interface 2
class Opponent:
  def__init__(self,image_file,difficulty):
    self.health = 100
    self.difficulty = "Regular"
    self.knockdown = False
    self.blocking = False
    self.tko_count = 0
    
    if self.knockdown = True:
        back_up = True
        tko_count += 1
    self.tko_count = 0
      if self.tko_count == 3:
        end_match = True
    self.position = (x,y)
  
  def health_difficulty(difficulty):
    if self.difficulty == "Regular":
      self.health = 150
      self.strength = 10
    elif self.difficulty == "Easy":
      self.health = 100 
      self.strength = 7
    elif self.difficulty == "Hard":
      self.health = 200
      self.strength = 15
  
  def recovery (difficulty):
    if difficulty = "Regular" :
       get_up = random.randrange(1,10)
      if get_up >5
        self.knockdown = False
      else 
        self.knockdown = True
    elif difficulty = "Easy":
       get_up = random.randrange(1,10)
      if get_up >3
        self.knockdown = False
      else 
        self.knockdown = True
    elif difficulty = "Hard":
      get_up = random.randrange(1,10)
      if get_up >1
        self.knockdown = False
      else 
        self.knockdown = True
## Class Interface 3
(inport other classes and pygame)
Class Scoreborad:
  def __init__(self,time,rounds,player_name,player_health,opponent_health)
    self.time = time
    self.rounds = rounds
    self.player_name = player_name
    self.player_health = player_health
    self.opponent_health = oppoent_helath
  def scoreboard():
    while *game is running*
    *USE VARIABLES TO MAKE SCOREBOARD GUI*