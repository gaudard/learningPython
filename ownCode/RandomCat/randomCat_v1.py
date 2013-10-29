#!/usr/bin/python
#Cats are easy to program!

import random #random module, required for random.choice()

rooms = [] #rooms in your house variable

def inputRooms(): #allows for input of multiple rooms
  
  manyRooms = raw_input('How many rooms are in your house?: ')
  
  while len(rooms) < manyRooms:
    rooms.append(raw_input('Enter a room:'))
  return rooms

'''Main function calls inputRooms if there are not any rooms for the cat to run
into, else prints a random action for the cat to preform'''

def main(): 
  if not rooms:
    inputRooms()
  action = ['Eating', 'Sleeping', 'Run to: ' + random.choice(rooms)]
  print random.choice(action)
  
if __name__ == '__main__': #boilerplate
  main()









