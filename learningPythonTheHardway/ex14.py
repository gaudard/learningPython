# Learn Python The Hard Way
# Exercise 14
# http://learnpythonthehardway.org/book/ex14.html
# @jgaudard

from sys import argv

def main():

  userName = argv[1]
  prompt = '>'

  print "Hi %s, I'm the script." % (userName)
  print "I'd like to ask you a few questions."
  print "Do you like me %s?" % userName

  likes = raw_input(prompt)

  print "Where do you live %s?" % userName
  lives = raw_input(prompt)

  print "What kind of computer do you have?"
  computer = raw_input(prompt)

  print"""
  Alright, so you said %r about liking me.
  You live in %r. Not sure where that is.
  And you have a %r comptuer. Nice.
  """ % (likes, lives, computer)

if __name__ == '__main__':
  main()