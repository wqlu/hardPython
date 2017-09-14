# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 15:43:13 2017

@author: Administrator
"""
print("do you go through door #1 or door #2?")
door = input(">")

if door == '1':
    print("there's giant bear eating a cheese cake. what do you do?")
    print("1.take the cake")
    print("2.scream at the bear")
    
    bear = input(">")
    if bear == '1':
        print("good job")
    elif bear == '2':
        print("eat your legs")
    else:
        print("doing %s is probably better" % bear)
elif door == '2':
    print("you start into the endless abyss")
    print("1.blueberries")
    print("2.yellow jacket")
    print("3.understanding revolvers yelling melodies")
    
    instanity = input(">")
    if instanity == '1' or instanity == '2':
        print("good job")
    else:
        print("xxxx")
        
else:
    print("die")