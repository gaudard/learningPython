#!/usr/bin/python

# import modules used here, sys is common.

import sys

# Gather our code in a main() function

def main():
	print 'Hello there', sys.argv[1]
	# Command line args are in sys.argv[1], sys.argv[2] ...
	# sys.argv[0] is the script name and can be ignored

# standard boilerplate to call the main() function to begin

# the program

if __name__ == '__main__':
	main()

