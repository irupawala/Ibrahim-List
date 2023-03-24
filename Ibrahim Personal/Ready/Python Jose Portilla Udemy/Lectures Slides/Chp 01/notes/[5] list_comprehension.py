# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 00:00:11 2018

@author: Ibrahim
"""

# If you find yourself using a for loop
# along with .append() to create a list, 
# List Comprehensions are a good alternative!


# beginner's way to create a list is
#%%
mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)    

#%% List Comprehension method
mystring = "hello"
mylist = [letter for letter in mystring]
print(mylist)

#%%

mylist = [x for x in "word"]
mylist

#%%

mylist = [x for x in range(0,11)]
mylist

#%%

#%% 

mylist = [num**2 for num in range(0,11)]
print (mylist)
mylist = [num**2 for num in range(0,11) if num%2 ==0]
print (mylist)

#%%

celcius = [0, 10, 20, 30]

farhenite = [((9/5)*temp + 32) for temp in celcius]
print(farhenite)

#%% This can also be written as

farhenite = []
celcius = [0, 10, 20, 30]
for temp in celcius:
    farhenite.append((9/5)*temp + 32)
print(farhenite)

# If-else can also be used in list comprehension
#%%
results = [x if x%2==0 else "ODD" for x in range(0,11)]
print(results)

# nested loop in list comprehension
#%%

mylist = []

for x in [2,4,6] :
    for y in [100, 200, 300]:
        mylist.append(x*y)

print (mylist)        

#%%

mylist = [x*y for x in [2,4,6] for y in [10, 100, 1000]]  
print (mylist)          