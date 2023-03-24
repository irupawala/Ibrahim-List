# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 01:11:18 2020

@author: 1000249643
"""

string_value = ['AA$', '$AA', 'A$A']
sorted_string = sorted(string_value)

print(sorted_string)

bwt_text = ""

for x in sorted_string:
    bwt_text = bwt_text + x[-1]

print(bwt_text) 