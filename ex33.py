# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:25:12 2017

@author: Administrator
"""

i = 0
numbers = []

while i < 6:
    print("at the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print("number now ", numbers)
    
print("the numbers:")
for num in numbers:
    print(num)