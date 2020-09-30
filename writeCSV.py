# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:41:26 2020

@author: muthukumar
"""

import os
import csv
outputcsvpath = os.path.join(r'C:\Users\muthukumar\Desktop\mycsv_1.csv')
with open(outputcsvpath, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

print("File write successful")
                       
                       
                       