# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:17:27 2020

@author: muthukumar
"""

import os
import csv
csvpath = os.path.join(r'C:\Users\muthukumar\Desktop\netflix_ratings.csv')
found = False
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    userCh = input("Enter the video you are looking for: ")
    for row in csvreader:
        if row[0] == userCh:
            found = True
            print(row[0] + "is rated " + row[1] + " with a rating of " + row[5])
            
            break
    if found is False:
        print("sorry - video not found")
            
    
