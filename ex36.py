# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:48:30 2017

@author: Administrator
"""

ten_thing = "apple oranges crow telephone light sugar"

print("wait there's not 10 things in that list, let's fix that")

stuff = ten_thing.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn","banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ",next_one)
    stuff.append(next_one)
    print("there's %d items now " % len(stuff))
    
print("there we go :", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())

print(' '.join(stuff))
print('#'.join(stuff[3:5]))