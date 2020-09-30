# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:10:09 2020

@author: muthukumar
"""
#usjfjsdfj
import os
import csv
cvsfilepath = os.path.join(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\Activities\python-activities\cereal.csv")
with open(cvsfilepath, mode='r') as csv_file:    
    reader = csv.reader(csv_file, delimiter=",")
    header = next(reader)
    for row in reader:
        #jsdlfjsd
        if float(row[7]) >= 5:
            print(row)