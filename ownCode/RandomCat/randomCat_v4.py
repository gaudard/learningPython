#!/usr/bin/python
# This cat was a little more complex to program!
# @jgaudard 
# Oct 2013
# randomCat_v4.py

import random                       #random module, required for random.choice()
import time                       #allows for time.sleep(n) to pause the program

rooms = []                      #global var for the number of rooms in the house

def inputRooms():
  '''defines an input function to allow for the input of the rooms in a
  house, first accepting an int for the number of rooms, then the number
  entered gives you than many prompts for rooms to input'''
  
  manyRooms = input('How many rooms are in your house?: ')
  count = 0
  
  while count < manyRooms:          #while loop to allow input of multiple rooms
    rooms.append(raw_input('Enter a room: '))
    count = count + 1
  return rooms


def main(): 
  '''main function, determines if rooms have been input, if not calls the
  inputRooms() function. Setups up an indefinate loops to give an output of
  what the cat is doing'''
 
  
  if not rooms:
    inputRooms()
  
  forever = 1
  count = 1

  while forever == 1:                            #if this stops, the cat is dead
    
    while count == 1 :           #first iteration, the cat has to run somewhere.
      count = count + 1
      where = random.choice(rooms)
      print 'The cat runs into the ' + where + '!'
    else:
      lazyOrNot = [ 'lazy', 'not' ]
      choice = random.choice(lazyOrNot)
  
      if choice == 'not':                  #determines if the cat is lazy or not
        where = random.choice(rooms)
        print 'The cat runs into the ' + where + '!'
      else:         #eats in kitchen, poops in bathroom, sleeps everywhere else.
        if where.lower() == 'kitchen':
          print 'The cat is eating', 'in the', where + "."
        elif where.lower() == 'bathroom':
          print 'The cat is pooping', 'in the', where + "."
        else:
          print 'The cat is sleeping', 'in the', where + "."
    time.sleep(1)                 #sleep in seconds, 900 seconds in 15 minutes
  
if __name__ == '__main__':                                          #boilerplate
  main()
