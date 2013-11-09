#!/usr/bin/python -tt
#################################################
# Learn Python The Hard Way
# Exercise 36
# http://learnpythonthehardway.org/book/ex36.html
# Dungeon game
# @jgaudard
##################################################

#imports required for program to run
from sys import exit
from os import system
from random import choice
import time

# System variables
systemType = 0

# Variables - weapons
axeOwner = 0
swordOwner = 0
maceOwner = 0

# Variables - future weapon modifiers
sword = 0.9
axe = 0.6
mace = 0.3

# Variables - loot
gold = 0
weaponSharpening = 0
resurrectionPotion = 0

''' cool banner functions'''
def banner():
  print '''
 _____ _          
|_   _| |         
  | | | |__   ___ 
  | | | '_ \ / _ \\
  | | | | | |  __/
  \_/ |_| |_|\___|
______                                    
|  _  \                                   
| | | |_   _ _ __   __ _  ___  ___  _ __  
| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
| |/ /| |_| | | | | (_| |  __/ (_) | | | |
|___/  \__,_|_| |_|\__, |\___|\___/|_| |_|
                    __/ |             v0.9       
                   |___/ 
'''

def ogreBanner():
  print '''
                           __,='`````'=/__
                          '//  (o) \\(o) \\ `'         _,-,
                          //|     ,_)   (`\\      ,-'`_,-\\
                        ,-~~~\\  `'==='  /-,      \\==```` \\__
                       /        `----'     `\\     \\       \\/
                    ,-`                  ,   \\  ,.-\\       \\
                   /      ,               \\,-`\\`_,-`\\_,..--'\\
                  ,`    ,/,              ,>,   )     \\--`````\\
                  (      `\\`---'`  `-,-'`_,<   \\      \\_,.--'`
                   `.      `--. _,-'`_,-`  |    \\
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\\   \\ --`````````|--`
                     >-`_,-`\\,-` ,          |
                   <`_,'     ,  /\\          /
                    `  \\/\\,-/ `/  \\/`\\_/V\\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \\,---_|    |_---./
                        ooOO(_)    (_)OOoo
'''

def dragonBanner():
  print '''
                        ^    ^
                       / \\  //\\
         |\\___/|      /   \\//  .\\
         /O  O  \\__  /    //  | \\ \\
        /     /  \\/_/    //   |  \\  \\
        @___@'    \\/_   //    |   \\   \\ 
           |       \\/_ //     |    \\    \\ 
           |        \\///      |     \\     \\ 
          _|_ /   )  //       |      \\     _\\
         '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
         ,-{        _      `-.|.-~-.           .~         `.
          '/\\      /                 ~-. _ .-~      .-~^-.  \\
             `.   {            }                   /      \\  \\
           .----~-.\\        \\-'                 .~         \\  `. \\^-.
          ///.----..>    c   \\             _ -~             `.  ^-`   ^-_
            ///-._ _ _ _ _ _ _}^ - - - - ~                     ~--,   .-~
'''


''' This allows setups up the function to clear the screen'''
def clearScreen():
  global systemType
  while systemType < 1:
    print "What type of computer are you using?"
    print "1) Windows"
    print "2) Linux/OSX"
    print "3) Don't know"
    systemType = input('> ')
  if systemType == 1:
    system('cls')
  elif systemType == 2:
    system('clear')
  else:
    pass


''' ogre attack function, with random chance of surival based on weapon'''
def ogreAttack():

  ogreBanner() 
  print "\nYou see a large ogre and he doesn't look friendly"
  raw_input('\n Press enter to continue.> ')
  clearScreen()
  chance1 = choice(range(0,5))
  if chance1 == 1:
    death()
  else:
    global axeOwner
    if axeOwner == 1:
      print "\nYou slay the ogre with your axe!"
    else:
      print "you slay the ogre with your fists!"
  print "\nyou didn't die."
  corpseLooter()



def dragonAttack():
  dragonBanner()
  print "\nthe dragon has smoke rolling from his nose"
  print "and snorts fire in your direction as he approaches"
  raw_input('\n Press enter to continue.> ')
  chance1 = 99 #choice(range(0,3))
  if chance1 == 1:
    print "\nThe dragon passes you without a second look."
  else:
    global axeOwner
    if axeOwner == 1:
      print "\nYou slay the dragon with your axe!"
    else:
      print "Some how you slay the dragon with your fists!"
  corpseLooter()

 

''' corpse looting function, with random chance of random loot'''
def corpseLooter():
  chance2 = choice(range(0, 3))
  if chance2 == 0:
    global weaponSharpening 
    weaponSharpening += 1.1
    print "you can now sharpen your weapon"
  elif chance2 == 1:
    global gold
    gold += 10
    print "you have found 10 gold"
  else:
    global resurrectionPotion
    resurrectionPotion += 0
    print "you have found one resurrectionPotion"

 

def goldenChest():
  chance1 = choice(range(0, 8))
  print "\n It seems you have some uncontrollable urge to open the chest...\n"
  if chance1 == 0:
    print "You found 10 gold!"
    global gold
    gold += 10
  elif chance1 == 1:
    print "You found a sword!"
    global swordOwner
    swordOwner = 1
  elif chance1 == 2:
    print "You found a mace!"
    global maceOwner
    maceOwner = 1
  elif chance1 == 3:
    print "You found a resurrectionPotion"
    global resurrectionPotion
    resurrectionPotion += 1
  elif chance1 == 4:
    print "You found an Axe"
    global axeOwner
    axeOwner = 1
  else:
    print "You found an empty box..."
    print "sorry about your luck"
  print "\n Return to continue"
  raw_input(' >')
  clearScreen()
 
 


### this is where you die!!!
def death():
  global resurrectionPotion
  if resurrectionPotion >= 1:
    print "Lucky you had a potion, you awaken several days later"
    pass
  else:
    exit("You died something horrible")

    
 
### this is where you crawl!!!
def crawling():
  print "\nAfter crawling for what seemed like a mile."
  print "You come into an opeing where an axe is on a stand"
  print "Do you pickup the axe? 'y' or 'n'"
  
  choice1 = raw_input('\n > ')
  if choice1 == 'y':
    global axeOwner
    axeOwner = 1
  else:
    pass

  next0 = choice(range(0,2))
  if next0 == 0:
    ogreAttack()
  else:
    print "\nThere is nothing else to see here so"

    
    
    

def steelGate():
  chance1 = choice(range(0,3))
  if chance1 == 0:
    print "\nAfter walking until your feet are numb.."
    print "You come to a room with a golden chest..."
    print "Do you open it? 'y' or 'n'"
    choice1 = raw_input('> ')
    if choice1 == 'y':
      goldenChest()
    else:
      print "Scared?"
      
  elif chance1 == 1:
    print "\nA short walk later..."
    print "You see a large dragon off in the distance"
    print "looking in your direction."
    dragonAttack()
  else:
    print "You continue walking, when you are ambushed!"
    ogreAttack()

    
def woodenDoor():
  print "After a brisk downhill walk you find a golden chest."
  goldenChest()
  

### this is where all the action is called from
def journey():
  neverEnding = 0
  while neverEnding < 666:
    print '\nYou continue on your jouney when you come to:\n'
    print '1) Crawl into the a small cave.'
    print '2) Walk through a doorway with a heavy steel gate.'
        
    choice0 = raw_input('\n > ')
    if choice0 == "1":
      crawling()
    else:
      steelGate()
  
    print "\nYou continue on your jouney."
    print "You come to a large open area, where the sun shines down from an"
    print "opening in the ceiling of the cave"
    print "There are also 3 doors."
    print "\n1) A wooden door."
    print "2) A door made with bones."
    print "3) A door covered with blood and guts."
    choice0 = raw_input('\n > ')
    
    if choice0 == '1':
      print "opens the wooden door and walks into..."
      woodenDoor()
    elif choice0 == '2':
      print "Opens the door made from bone."
      ogreAttack()
    else:
      print "Opens the door made from blood and guts."
      print "Walks down a long narrow passage which"
      print "opens up into a large cavern where with a"
      print "dragon!"
      dragonAttack()
    
    
    
    
#### this needs more work############





    
    
    neverEnding += 111
  
  #go to winning the game
  winning()

  
  
  
def winning():
  print "\nyou have won the game"
  print "loot gold: " + str(gold)
  print "loot weapon sharpening: " + str(weaponSharpening)
  print "loot resurrection potion: " + str(resurrectionPotion)

 

 
### main function
def main():
  banner()
        
  play = raw_input("\nWould you like to play the game?\n 'y' or 'n' > ")
  if play == 'y':
    print '\Entering the game'
    clearScreen()
    journey()
  else:
    death()
       




if __name__ == '__main__': #boilerplate to call main function
  main()