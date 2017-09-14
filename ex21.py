# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:14:54 2017

@author: Administrator
"""
def add(a,b):
    print("add %d + %d " % (a, b))
    return a + b

def subtract(a, b):
    print("subtract %d - %d " % (a, b))
    return a - b

def multiply(a, b):
    print("multiply %d * %d " % (a, b))
    return a * b

def divide(a, b):
    print("divide %d / %d " % (a, b))
    return a / b

print("do some math with just function")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("age: %d, height: %d, weight: %d, iq: %d " % (age, height, weight, iq))
print("here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print(what)