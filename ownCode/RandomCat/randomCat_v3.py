#!/usr/bin/python
# This cat was a little more complex to program!
# @jgaudard 
# Oct 2013
# randomCat_v3.py

import random #random module, required for random.choice()
import time #allows for a pause

rooms = [] #rooms in your house variable

def inputRooms(): #allows for input of multiple rooms
  
  manyRooms = input('How many rooms are in your house?: ')
  count = 0
  
  while count < manyRooms:
    rooms.append(raw_input('Enter a room: '))
    count = count + 1
  return rooms



def whatToDo(where, rooms):
  lazyOrNot = [ 'lazy', 'not' ]
  choice = random.choice(lazyOrNot)
  
  if choice == 'not':
    where = random.choice(rooms)
    print 'The cat runs into the ' + where + '!'
  else:
    if where.lower() == 'kitchen':
      print 'The cat is eating', 'in the', where + "."
    elif where.lower() == 'bathroom':
      print 'The cat is pooping', 'in the', where + "."
    else:
      print 'The cat is sleeping', 'in the', where + "."
  return where


def main(): 
  """Main function calls inputRooms if there are not any rooms for the cat to run
  into, will loop indefinitely through the while forever"""
  
  if not rooms:
    inputRooms()
  
  forever = 1
  count = 1

  while forever == 1: #indefinate loop
    
    while count == 1 :
      count = count + 1
      where = random.choice(rooms)
      print 'The cat runs into the ' + where + '!'
    else:
      whatToDo(where, rooms)
    time.sleep(.25) #sleep in seconds, 900 seconds in 15 minutes
  
if __name__ == '__main__': #boilerplate
  main()









