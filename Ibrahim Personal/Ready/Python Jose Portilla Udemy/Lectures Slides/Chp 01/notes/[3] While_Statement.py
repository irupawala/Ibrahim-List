# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:49:10 2018

@author: Ibrahim
"""

x = 0

while x < 5:
    
    print(f"The current value of x is {x}")
    x+=1
else:
    print("X is not equal to 5")
    
# BREAK, CONTINUE, PASS can be used with while loop to add additional functionality

# break: breaks out of the current enclosing loop
# continue: Goes to the top of the current enclosing loop
# pass: Does nothing at all. Place holder to avoid syntax error


# Example of pass to avoid getting EOF parsing error    
x = [1,2,3]

for item in x:
   # comment
   pass

print ("End of my script")

# Example of continue

mystring = "ibrahim"

for l in mystring:
    if l == 'i':
        continue
    print(l)

# Example of break

x = 0
 
while x < 5:
     if (x == 2):
         break
     print(x)
     x+=1
     
    