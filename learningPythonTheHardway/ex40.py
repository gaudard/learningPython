#!/usr/bin/python -tt
#################################################
# Learn Python The Hard Way
# Exercise 40
# http://learnpythonthehardway.org/book/ex40.html
# @jgaudard
##################################################

class song(object):
  def __init__ (self, lyrics):
    self.lyrics = lyrics
    
  def sing_me_a_song(self):
    for line in self.lyrics:
      print line
      
happy_bday = song(["Happy birthday to you",
  "I don't want to get sued",
  "So I'll stop right there"])
  
bulls_on_parade = song(["They rally around the family",
  "with a pocket full of shells"])
  
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()