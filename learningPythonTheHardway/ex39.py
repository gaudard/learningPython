#!/usr/bin/python -tt
#################################################
# Learn Python The Hard Way
# Exercise 39
# http://learnpythonthehardway.org/book/ex39.html
# @jgaudard
#
# Lesson learned, use the comments!
##################################################

# create a basic set of states and some cities
states = {
  'Oregon': 'OR',
  'Flordia': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI',
}

# create a basic set of states and some cities in them
cities= {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Flordia's abbreviation is: ", states['Flordia']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Flordia has: ", cities[states['Flordia']]

# print every state abbrev
print '-' * 10
for state, abbrev in states.items():
  print "%s is abbreviated %s" % (state, abbrev)
  
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# No do both    
print '-' * 10
for state, abbrev in states.items():
  print "%s states is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev])
    
print '-' * 10
state = states.get('Texas', None)

if not state:
  print "Sorry, no Texas."
  
city = cities.get('TX', 'Does Not Exist')
print "the city for the state 'TX' is %s" % city


   