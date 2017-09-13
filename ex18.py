# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:00:25 2017

@author: Administrator
"""

def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r " % (arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r " % (arg1, arg2))
    
def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("i got nothing")

print_two("lu", "shaw")
print_two_again("lu", "shaw")
print_one("first")
print_none()