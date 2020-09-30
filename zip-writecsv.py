# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:52:05 2020

@author: muthukumar
"""

import os
import csv
# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

# Zip all three lists together into tuples
roster = zip(indexes, employees, department)
#save the output file path
#outputcsvpath = os.path.join(r'C:\Users\muthukumar\Desktop\myzipcsv_2.csv')
#with open(outputcsvpath, 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile, delimiter=',')
#    writer.writerow(["Index", "Employee", "Department"])
#    writer.writerows(roster)
outputtxtpath = os.path.join(r'C:\Users\muthukumar\Desktop\mytxt_2.csv')
with open(outputtxtpath, 'w', newline='') as txtfile:
    writer = csv.writer(txtfile, delimiter=',')
    writer.writerow(["Index", "Employee", "Department"])
    writer.writerows(roster)
print("File write successful")

# # to print out to terminal:
# #comment out above code and run the code below
#    for employee in roster:
#        print(employee)
