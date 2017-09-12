# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:57:09 2017

@author: Administrator
"""

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driver = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driver, "empty cars today")
print("we are ", passengers, "to acrpool today")
print("we need to put about ", average_passengers_per_car, "in each car")
