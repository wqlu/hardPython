# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:09:02 2017

@author: Administrator
"""

from sys import argv
script, filename = argv

print("we're going to erase %r" % filename)
print("if you don't want that, hit CTRL-C(^C)")
print("if you so want that, hit RETURN")

input("?")
print("opening the file...")
target = open(filename, 'w')

print("truncating the file.")
target.truncate() # 清空文件

print("now i'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("i'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
target.close()