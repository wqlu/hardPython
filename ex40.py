# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:14:02 2017

@author: Administrator
"""

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"
    
cities['_find'] = find_city

while True:
    print("state ?(enter to quit)")
    state = input(">")
    if not state: 
        break
    city_found = cities['_find'](cities, state)
    print(city_found)