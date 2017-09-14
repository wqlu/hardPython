# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:56:06 2017

@author: Administrator
"""

from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) # seek(offset, wherence) 后一个参数不写默认为0
    
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file: \n")

print_all(current_file)

print("now, let's rewind, kind of a like type")
rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
