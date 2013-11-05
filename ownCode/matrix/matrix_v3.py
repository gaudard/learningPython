#!/usr/bin/python
############################################################
# matrix_v1.py
# Generate matrix looking background
# @jgaudard
# Nov 2013
############################################################

import random
import sys

def banner():
	print '''
___  ___      _        _        _____            
|  \/  |     | |      (_)      |  __ \           
| .  . | __ _| |_ _ __ ___  __ | |  \/ ___ _ __  
| |\/| |/ _` | __| '__| \ \/ / | | __ / _ \ '_ \ 
| |  | | (_| | |_| |  | |>  <  | |_\ \  __/ | | |
\_|  |_/\__,_|\__|_|  |_/_/\_\  \____/\___|_| |_|
																						v1.0
|***|		Matrix Generator v1.0		|***|
|***|		Written by @jgaudard		|***|

'''
def theGenerator():
	chars = raw_input('\nHow many characters can fit on this screen? (probably 80) > ')
	rows = raw_input('\nHow many rows of characters do you want? >')
	line = []
	count = 0
	oneOrZero = 1, 0
	emptySpace = ' '
	spaceOrNot =  [oneOrZero, emptySpace]
	
	line.append(random.choice(spaceOrNot) * int(chars) * int(rows))
	print line
	
	
def main():
	banner()
	sureQuestion = raw_input("""\n
Unfortunately, no one can be told what the Matrix is.
You have to see it for yourself.This is your last 
chance. After this, there is no turning back. You 
take the blue pill, the story ends, you wake up in your 
bed and believe whatever you want to believe. You take 
the red pill, you stay in Wonderland, and I show you 
how deep the rabbit hole goes. Remember: all I'm 
offering is the truth. Nothing more. \n\n\n
So "red" or "blue"? >""")
	if sureQuestion == 'r' or sureQuestion == 'Red' or sureQuestion == 'red':
		theGenerator()
	else:
		sys.exit('\n\nNow you will never know....')
	
if __name__ == "__main__":
	main()