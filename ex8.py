# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:57:21 2017

@author: Administrator
"""

formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
        "i had this things",
        "that you could type up right",
        "but it didn't sing",
        "so i said goodnight"))