#!/usr/bin/python
#Cats are easy to program!

import random #random module, required for random.choice()

rooms = [] #rooms in your house variable

def inputRooms(): #allows for input of multiple rooms
  moreRooms = 'y'
  #as long as you keep typing 'y' you can input more rooms
  while moreRooms == 'y':
    rooms.append(raw_input('Enter a room:'))
    moreRooms = raw_input('Do you need to enter a room name? (y or n):')
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









