# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:34:19 2021

@author: 1000249643
"""

#import random
#
#
#randomlist = random.sample(range(-10, 10), 20)
#if 0 in randomlist:
#    randomlist.remove(0)
#print(randomlist)
#res = random.choice(randomlist)
#print(res)

import pycosat

#cnf = [[1, -5, 4], [-1, 5, 3, 4], [-3, -4]]

#cnf = [[1, 1], [-1, -1]]

#cnf = [[1, 4], [-2, 5], [3, 7], [2, -5], [-8, -2], [3, -1], [4, -3], [5, -4], [-3, -7], [6, 7], [1, 7], [-7, -1]]

cnf = [[8, 1], [1, 2], [3, 2], [1, 5], [9, 1], [5, 9], [5, 8], [7, 8], [7, 6], [6, 4], [4, 3], [3, 4], [5, 4]]

print(pycosat.solve(cnf))