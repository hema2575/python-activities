# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:46:30 2020

@author: muthukumar
"""
import os
import csv
inputfilepath = os.path.join(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\Activities\python-activities\UdemyZip.csv')
# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []
# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(inputfilepath, 'r', newline='', encoding='utf-8') as csvfile:
    # Initialize csv.reader
    inptreader = csv.reader(csvfile, delimiter=',')

    for row in inptreader:
        # Add title, price, numbr of subscribrs, reviews
        title.append(row[1]) 
        price.append(row[4])
        subscribers.append(row[5])       
        reviews.append(row[6])
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)
          # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
# Zip lists together
ziplistsforcsv = zip(title, price, subscribers, reviews, review_percent, length)
#set variable for outputfile
outputwrtrpath = os.path.join(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\Activities\python-activities\UdemyZip_2.csv')
#  Open the output file
with open(outputwrtrpath, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(ziplistsforcsv)
print("File write successful")

        
