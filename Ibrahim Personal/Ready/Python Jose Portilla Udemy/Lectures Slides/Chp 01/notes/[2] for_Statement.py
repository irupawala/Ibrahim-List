# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:15:10 2018

@author: Ibrahim
"""

mylist = [1,2,3,4]
for k in mylist:
    print(k)
    
for k in mylist:
    print("HEllo")   
    
    
for num in mylist:
    if num%2 == 0:
        print(num)
    else:
        print("num {} is odd".format(num))
        print(f"num {num} is odd")


for l in "Hello World":
    print(l)    
    

tup = (1,2,3)
for _ in tup:
    print(_)
    
my_list = [(1,2), (3,4), (5,6), (7,8)]   
for _ in my_list:
    print (_)
    
# Tuple unpacking
    
for a,b in my_list: 
    print(a)
    print(b)
    
    
d = {"k1": 1, "k2":2, "k3": 3}   

for item in d:
    print(item) # this will print only keys
    
for item in d.items():
    print(item) # this will print key value pairs
    
for key, value in d.items():
    print(key) 
    print(value)
    
for k in d.values():
    print(k)      

for k in d.keys():
    print(k)     

# Take Note of this

# For just printing keys use var_name
# For just printing keys use var_name.keys()
# For just printing values use var_name.values()
# For printing key/ values pairs use var_name.items()        
        