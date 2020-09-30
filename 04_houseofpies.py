# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:39:58 2020

@author: muthukumar
"""
#Create an order form that will display a list of pies to the user in the following way:
#Welcome to the House of Pies! Here are our pies:
#---------------------------------------------------------------------
#(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
#Then prompt the user to select which pie they'd like to order via number.
#Immediately after, follow the order with Great! We'll have that <PIE NAME> right out for you. and then ask if they would like to make another order. If so, repeat the process.
#Once the user is done purchasing pies, print the total number of pies ordered.
#Part 2 (Very Challenging!)
#Modify the application once again, this time conclude the user's purchases by listing out the total pie count broken by each pie.
#You purchased:
#0 Pecan
#0 Apple Crisp
#0 Bean
#2 Banoffee
#0 Black Bun
#0 Blueberry
#0 Buko
#0 Burek
#0 Tamale
#1 Steak
#--------------------------------------------------
# Pie List
shopping = 'y'
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
pie_purchases = []
print("Welcome to the House of Pies! Here are our pies:")
while shopping == "y":
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")

    pie_choice = input("Which would you like? ")
    pie_purchases.append(pie_choice)
    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("grt. we will have " + pie_list[int(pie_choice)-1]+ "for you")
    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete
print("------------------------------------------------------------------------")
print("You purchased a total of " + str(len(pie_purchases)) + ".")

