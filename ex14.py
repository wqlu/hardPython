# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:53:16 2017

@author: Administrator
"""

from sys import argv

script, user_name = argv
prompt = '>'

print("hi, %s, i'm the %s script ." % (user_name, script))
print("i'd like to ask you a few questions")
print("do you like me %s?" % user_name)
likes = input(prompt)

print("where do you live %s?" % user_name)
lives = input(prompt)

print("what kind of computer do you like?")
computer = input(prompt)

print("""
      alright, so you said %r about likingme.
      you live in %r. not sure where that is.
      and you like %r computer.
""" % (likes, lives, computer))