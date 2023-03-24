# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:09:37 2018

@author: Ibrahim
"""

# Range Operator
#%%
for num in range(10):
    print(num)
#%%    
for num in range(3, 10):
    print(num)    
#%%    
for num in range(0, 11, 2):
    print(num)        
#%%  
# Range    
list (range(0, 11, 2))    

#%%
# range is a generator
#Generator is a special type of function which will generate numbers 
#insted of saving it to memory

#%%
# Enumerate
index_count = 0

for letter in "abcde":
    print("At index {} the letter is {}". format(index_count, letter))
    index_count += 1
    
#%%
index_count = 0
word = "abcde"

for l in word:
    print(word[index_count]) 
    index_count+=1
    
#%%
# note the power of enumerate
# reuslt of enumerate is tupples
word = "abcde"

for l in enumerate(word):
    print(l)
    
#%%

word = "abcde"

for index, items in enumerate(word):
    print(index)
    print(items)
    print("\n")
        
#%%

# Zip Function
list_1 = [1,2,3] 
list_2 = ["a","b","c"]  
#%%
zip(list_1, list_2) # item zipped at the followinf memory locations

#%%

for item in zip(list_1, list_2):
    print(item) # items will be returned packed as tuples, have to use tuples unpacking
    
#%%
list_1 = [1,2,3,4,5,6] 
list_2 = ["a","b","c"] 
list_3 = [10, 20, 30] 

for item in zip(list_1, list_2, list_3):
    print(item) #items will be zipped only as far as the values are available for the smallest list
    
#%%
list_1 = [1,2,3,4,5,6] 
list_2 = ["a","b","c"] 

list(zip(list_1, list_2))
    
#%%

# Tuples unpacking Example

list_1 = [1,2,3,4,5,6] 
list_2 = ["a","b","c"] 
list_3 = [10, 20, 30] 

for a,b,c in zip(list_1, list_2, list_3):
    print(a) 


# In keyword
#%%
2 in [1,2,3] 
#%%
'x' in ['x', 'y', 'z']   
#%%
'r' in 'a world'
#%%
'mykey' in {'mykey': 345}
#%%
d = {'mykey': 345} 
345 in d.values()   
345 in d.keys()
#%%
mylist = [10, 20, 30, 40, 100]
min(mylist)
max(mylist)

# import function

#%%
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
mylist

#%%
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
random_list = shuffle(mylist)
random_list # Inplace function, won't return anything
type(random_list)

#%%
from random import randint
randint(0,100) # as it returns the value it is not inplace and hence we can store it
#%%
from random import randint
mynum = randint(0,10)
mynum

# function to take user input 
#%%
input ("Enter a number here: ") 
#%%
result = input ("What is your name: ")
#%%
result = input ("Favourite number: ")
# note that input always outputs the results in string
# hence to convert it to float or int we have to use
print (result)
type(result)
float(result)
int (result)

# or else we can do this
#%%
result = int (input ("Favourite number: "))
type(result)
