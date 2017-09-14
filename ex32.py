# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:09:07 2017

@author: Administrator
"""

the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", "quarters"]

for number in the_count:
    print("this is count %d " % number)

for fruit in fruits:
    print("a fruit of type %s" % fruit)
    
for i in change:
    print("i got %r " % i)
    
elements = []

for i in range(0, 6):
    print("adding %d to the list" % i)
    elements.append(i)

for i in elements:
    print("element was %d" % i)