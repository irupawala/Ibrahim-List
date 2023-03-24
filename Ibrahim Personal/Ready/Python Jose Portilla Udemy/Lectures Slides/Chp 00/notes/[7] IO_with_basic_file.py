# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:05:57 2018

@author: Ibrahim
"""

my_file = open("my_file.txt")
print(my_file.read())

#my_file = open("no_file.txt")
# In the output the new line will be discriminated by \n character

# If you will run it second time the output will be ''
# This is because the cursor has moved to the end of the file
# Hence to read it again you have to reset the cursor or seek it back to 0
# try this

my_file.seek(0) # This will seek cursor back to 0
my_file.read()


# To get the new line displayed use

my_file.seek(0)
my_file.readlines()

my_file = open("C:\\Users\\Ibrahim\\Desktop\\Python Udemy\\Lectures Slides\\Chp 00\\my_file.txt")

# For windows use double \ so python doesn'treat the second \ as an escape character
# For MacOS and Linux you use slashes in the opposite direction

my_file.close() # to close this file

# the best practice is to use with, this way you don't need to worry about closing the file

#%%
with open("my_file.txt") as my_file:
    contents = my_file.read()
    print(contents)
    
# by typing shift tab next to the function open in 
#jupyter notebaak it opens all the information about that function
with open("my_file.txt", mode='r') as my_file:
    contents = my_file.read()  
    print(contents)

# We can have mode as 'r' for read only, 'w' for write only, 'a' for append only, 
# r+ is  reading and writing, w+ is for writing and reading
# This mode is called permissions    
    
with open("my_file.txt") as f:
    print(f.read())
    
with open("my_file.txt", mode='a') as f:
    f.write("\nThis is the fourth line")


   