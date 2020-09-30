# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:00:45 2020

@author: muthukumar
"""

names = []
for _ in range(5):  #what is _?
    name = input("Please enter the name of someone you know. ")
    names.append(name)

lowercased = [name.lower() for name in names]
titlecased = [name.title() for name in lowercased]
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
