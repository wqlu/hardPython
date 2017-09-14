# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:30:33 2017

@author: Administrator
12"""

# from sys import exit

def gold_room():
    print("this room is full of gold, how much do you take?")
    
    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
        print(how_much)
    else:
        print("man, learn to type a number")
        
gold_room()