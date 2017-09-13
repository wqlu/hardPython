# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:58:06 2017

@author: Administrator
"""

from sys import argv
script, filename = argv

txt = open(filename)
print("here's your file %r:" % filename)

print(txt.read())
print("type the filename again:")

file_again = input(">")
tex_again = open(file_again)
print(tex_again.read())
