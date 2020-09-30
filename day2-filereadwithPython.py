# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:55:27 2020

@author: muthukumar
"""
import csv
with open(r'C:\Users\muthukumar\Desktop\netflix_ratings.csv', newline ='') as csvfile:
   reader = csv.reader(csvfile)
   for row in reader:
       print(row)
       



import csv
import os
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
name = input("What video's rating are you looking for? ")
with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #print(row)
    for row in reader:
        if row['title'] == name:
            print(name+" is rated "+row['user rating score'])
            break
    else:
        print("didnt find anything")
