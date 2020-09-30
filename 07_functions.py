# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:15:25 2020

@author: muthukumar
"""

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
        


