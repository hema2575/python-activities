# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:47:57 2020

@author: muthukumar
"""


# Import the random and string Module
import random
import string

# Utilize the string module's custom method: ".ascii_letters"
print(string.ascii_letters)
print(string.ascii_lowercase)

# Utilize the random module's custom method randint
for x in range(10):
    print(random.randint(1,10))
