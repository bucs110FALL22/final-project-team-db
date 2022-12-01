:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Punch It 
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/ftwqrafgfb-danielbeiser

<< [link to demo presentation slides](#) >>

### Team: DB
#### Team Members: Daniel Beiser, Benicio Alonzo

***

## Project Description

 The basis of our project was inspired by Mike Tyson's Punch Out. The starting screen opens up and has two buttons that are interactable to bring you to the game screen or a screen showing you how to play. Once you load into the game screen the opponent appears and two hands appear which is your character. To win the game you have to get your opponents health to 0 before your health drops to 0, to do so you while have three functions, one to punch, one to block, and one to get back up if you get knocked down. 

***    

## User Interface Design

- **Initial Concept**
  -  (etc/initial_concept_project.png). This screenshot includes the four image screens. The first screen is where the main game happens and all actions of fighting the opponent occurs, the opponent is standing in the background and the user is in the foreground. The second screen is where the game first loads up and shows you the title and asks you two options if you want to "Play" or open up a different screen to learn "How to play", the third screen is the how to play screen so the user isnt lost and knows which buttons to use to play, the fourth screeen is a customization screen for your personal character to change pants color, skin color, and glove color.
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
      *  - pygame
           url - https://www.pygame.org/docs/
           description - pygame is a module for creating video games, it has computer graphics and sound libraries to be used in python
         
           
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * << Animations-
         Button- a class that defines multiple button functions, once the button you click it brings you to the next screen corresponding with the action you chose, for example, choosing your difficulty once you start the game or looking at the how to play guide.
         Controller- a class that defines
         Opponent- a class that defines the opponent. This is used to give the opponent its animations to move on the screen and to set its stats based off of difficulty,gives it the functions to be able to attack the player and to be able to have a chance at getting back up if knocked down, also has a way of becoming 'vulnerable' if his punch gets blocked.
         Player- a class that defines the user/player. sets how long you can block for and how long u have to wait to be able to block again and your chances of punches being blocked, makes it so the player is able to punch the opponent and be blocked by him, has the function to mash the spacebar once knocked down for a chance to get back up, also has the animations to make the players hands move to attack the opponent
    
         Scoreboard - a class that defines the scoreboard. Creates two rectangles for the opponent and players healthbar and each get smaller respectively as health decreases, also once the game is over creates text saying you either won or loss depending on the outcome >>

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

  we tested by writing large portions of code, then running, finding errors, then fixing these errors. methods would have print statements to see when it was called. when a method became bugless, we removed the print statment

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   |Open terminal, navigate to folder, and type, "python3 main.py”|GUI window opens and displays intro animation, two buttons then appear: 'Play' and 'How To Play'|
|  2                   | navigate to 'How To Play' button, hover over it, click mouse button | GUI window changes to a picture with  instructions on how to play |
|  3                   |navigate to left corner, hover over 'X', click mouse button| window changes back to same window as step 1 |
|  4                   | navigate to 'Play' button, hover over it, click mouse button | buttons dissapear, and backround changes to black with a prompted message "choose your difficulty", 3 buttons appear: 'Easy', 'Regular', and 'Hard' |
|  5                   | navigate to one of the buttons, hover over it, click mouse button | buttons dissapear, backround changes to boxing ring, health bars, opponent, and player apear on screen |
|  6                   | when opponent begins punch animation, press **down arrow**| player block animation occurs and audio of player blocking plays, opponont become 'vulnarable'|
|  7                   |opponents punch animation goes off and the player isn't blocking| player takes damage according to the difficulty and an audio of him being hurt is played
|  8                   |press **up arrow** to punch the opponent  and their block is down| player punch animation occurs,inflicts 10 damage, and plays audio of a punching noise
|  9                   |press **up arrow**  but the opponents block is up| player punch animation goes off, opponents block animation goes off, punch audio goes off, and no damage is inflicted to the opponent
| 10                   |when pressing **up arrow** too many times over the punch counter| the program plays an audio cue letting the player know they can't punch yet
| 11                   |player or opponents health goes to 0| they are knocked down and have a chance of getting back up
| 12                   |player or opponent is knocked down three times| the game is over as the max amount of knockdowns is there 
| 13                   |press **spacebar** when player gets knocked down to get back up| amount of times the spacebar is clicked is put into a counter, and if certain amount is reached they get back up, if not they lose
| 14                   |player or opponents health reaches 0| prints win or loss depending on outcome, then the game closes
| 15                   |
| 16                   |



