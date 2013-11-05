#!/usr/bin/python
#################################################
# Learn Python The Hard Way
# Exercise 33
# http://learnpythonthehardway.org/book/ex33.html
# @jgaudard
##################################################

i = 0
numbers = []

while i < 6:
	print "At the top of i is %d" % i
	numbers.append(i)
	
	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "the numbers: "

for num in numbers:
	print num