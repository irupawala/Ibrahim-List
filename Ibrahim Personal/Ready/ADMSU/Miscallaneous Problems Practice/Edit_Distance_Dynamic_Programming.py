# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:15:20 2021

@author: 1000249643
"""


def editDistance(string1, string2):
    
    for x in range(len(string1)+1):
        table[x][0] = x
    for y in range(len(string2)+1):
        table[0][y] = y
        
    for j in range(1, len(string2)+1):
        for i in range(1, len(string1)+1):
            
            insertion = table[i][j-1] + 1
            deletion = table[i-1][j] + 1
            mismatch = table[i-1][j-1] + 1
            match = table[i-1][j-1]
            
            if string1[i-1] == string2[j-1]:
                table[i][j] = min(insertion, deletion, match)
            else:
                table[i][j] = min(insertion, deletion, mismatch)
                
    return table[i][j]


def outputAlignment(i,j):
    
    if i == 0 and j == 0:
        return
    
    if i > 0 and table[i][j] == table[i-1][j] + 1:
        outputAlignment(i-1, j)
        back_track_num.append(str(string1[i-1]))
        back_track_den.append("*")
        
        
    elif j > 0 and table[i][j] == table[i][j-1] + 1:
        outputAlignment(i, j-1)
        back_track_num.append("*") 
        back_track_den.append(str(string2[j-1]))   
      
        
    else:
        if i > 0 and j > 0 :
            outputAlignment(i-1, j-1)
            back_track_num.append(str(string1[i-1]))
            back_track_den.append(str(string2[j-1])) 


if __name__ == "__main__":
#    string1 = input("Enter the first string: ")
#    string2 = input("Enter the second string: ")
#    
    string1 = "editing"
    string2 = "distance"
    back_track_num = []
    back_track_den = []
    
    table = [[0 for i in range(len(string2)+1)] for j in range((len(string1) + 1))] 
    
    print(f"Edit Distance = {editDistance(string1, string2)}")  
    outputAlignment(len(string1), len(string2))
    print("".join(map(str,back_track_num)))
    print("-"*len(back_track_den))
    print("".join(map(str,back_track_den)))
