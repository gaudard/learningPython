#!/usr/bin/python
#################################################
# Learn Python The Hard Way
# Exercise 36
# http://learnpythonthehardway.org/book/ex36.html
# Dungeon game
# @jgaudard
##################################################

#imports required for program to run
from sys import exit
import random
import time


# Variables - weapons point modifers
sword = 0.9
axe = 0.6
mace = 0.3

# Variables - loot/modifiers
weaponSharping = 1.1
gold = 0
resurrectionPotion = 0

''' cool banner function'''
def banner():
	print ''' \n
_________          _______ 
\__   __/|\     /|(  ____ \
   ) (   | )   ( || (    \/
   | |   | (___) || (__    
   | |   |  ___  ||  __)   
   | |   | (   ) || (      
   | |   | )   ( || (____/\
   )_(   |/     \|(_______/
 ______            _        _______  _______  _______  _       
(  __  \ |\     /|( (    /|(  ____ \(  ____ \(  ___  )( (    /|
| (  \  )| )   ( ||  \  ( || (    \/| (    \/| (   ) ||  \  ( |
| |   ) || |   | ||   \ | || |      | (__    | |   | ||   \ | |
| |   | || |   | || (\ \) || | ____ |  __)   | |   | || (\ \) |
| |   ) || |   | || | \   || | \_  )| (      | |   | || | \   |
| (__/  )| (___) || )  \  || (___) || (____/\| (___) || )  \  |
(______/ (_______)|/    )_)(_______)(_______/(_______)|/    )_)
                                                           v0.1
'''

''' ogre attack function, with random chance of surival based on weapon'''
def ogreAttack():
	print 'ogre attack'
	#### isn't returning to the calling function

''' corpse looting function, with random chance of random loot'''
def corpseLooter():
	print 'body looted'
	
''' death function'''
def death():
	exit("You died something horrible")

	
	
	
	
''' crawling choice function'''  ###left off working here!!!!
def crawling():
	print "After crawling for what seemed like a mile."
	print "You come into an opeing where an axe is on a stand"
	print "Do you pickup the axe? 'y' or 'n' > "
	
	choice1 = raw_input('\n > ')
	if choice1 == 'y':
		axeOwner = 1
	else:
		pass
	
	next0 = random.choice(range(0,2))
	if next0 == 0:
		ogreAttack()
	else:
		print "you continue on about your journey"
	
	
	
	
	
''' main function '''
def main():
	banner()
		
	play = raw_input("\nWould you like to play the game?\n 'y' or 'n' > ")
	if play == 'y':
		print 'entering the game'
	else:
		death()
	
	print 'You have a choice'
	print '1) Crawl into the small cave entrance'
	print '2) Walk in to the cave entrance with the thick steel gate'
	
	choice0 = raw_input('\n > ')
	if choice0 == "1":
		crawling()

	



	print 'You find yourself in the center of the earth'

if __name__ == '__main__': #boilerplate to call main function
  main()