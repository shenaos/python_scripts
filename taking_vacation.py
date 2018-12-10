#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:39:13 2018

@author: labfluidos
"""

def hotel_cost(nights):
  return nights * 140

def plane_ride_cost(city):
  if city == "Charlotte":
  	return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
  	return 475
  
def rental_car_cost(days):
  if days >= 7:
    return (days * 40) - 50
  elif days >=3:
    return (days * 40) - 20
  else:
    return 40* days

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city)+ spending_money

print(trip_cost("Los Angeles", 5, 600))