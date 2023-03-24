# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:06:06 2021

@author: 1000249643
"""

import random 
import time

start = time.time()

random_list = []

for x in range(10000):
    k = random.randint((1000000-10), 1000000)
    random_list.append(k)
    
print(random_list)
print(time.time() - start)

with open("random_list.txt", "w") as file1:
    file1.write(str(random_list))

    

