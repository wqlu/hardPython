# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:46:53 2017

@author: Administrator
"""

print("let's practice everything")
print('you\'d need to know \' about escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tthe lovely world
with logic so firmly planted 
cannt discern \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none
"""

print("----------------")
print(poem)
print("----------------")

five = 10 - 2 + 3 - 6 
print("this should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creats = jars / 100
    return jelly_beans, jars, creats

start_point = 10000
beans, jars, creats = secret_formula(start_point)

print("with a starting point of：%d " % (start_point))
print("we'd have %d beans, %d jars, and %d creats" % (beans, jars, creats))

start_point = start_point / 10
print("we can also do that this way")
print("we'd have %d beans, %d jeans, and %d creats." % secret_formula(start_point))