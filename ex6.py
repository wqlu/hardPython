# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:19:46 2017

@author: Administrator
"""

x = "there are  %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "those who konws %s and those who %s" % (binary, do_not)
print(x)
print(y)
print("i said: %r" % x)
print("i also said: %s" % y)
hailarious = False
joke_evaluation = "isn't that ioke so funny? %r"
print(joke_evaluation % hailarious)
w = "this is the left side of ..."
e = "a string with a right side"
print(w + e)