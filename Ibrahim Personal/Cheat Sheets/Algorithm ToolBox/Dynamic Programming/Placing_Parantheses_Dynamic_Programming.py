# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:38:47 2021

@author: 1000249643
"""

class placingParantheses:
    
    def __init__(self, data_list):
        self.digits = data_list[0:len(data_list):2]
        self.operations = data_list[1:len(data_list):2]
        self.n = len(self.digits)
        
        self.min_values = [[float('-inf') for x in range(self.n)] for y in range(self.n)]
        self.max_values = [[float('inf') for x in range(self.n)] for y in range(self.n)]
        
        for i in range(len(self.digits)):
            self.min_values[i][i] = int(self.digits[i])
            self.max_values[i][i] = int(self.digits[i])        
        
        for s in range(1, self.n+1):
            for i in range(1, (self.n+1) - s):
                j = i + s
                self.min_values[i-1][j-1], self.max_values[i-1][j-1] = self.MinAndMax(i,j)  
                
        print(f"min_value = {self.min_values[0][self.n-1]}")
        print(f"max_value = {self.max_values[0][self.n-1]}")               

    def evalt(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False
    
    def MinAndMax(self, i,j):
        
        min_value = float('inf')
        max_value = float('-inf')
        
        for k in range(i, j):
            a = self.evalt(self.max_values[i-1][k-1], self.max_values[k][j-1], self.operations[k-1])
            b = self.evalt(self.max_values[i-1][k-1], self.min_values[k][j-1], self.operations[k-1])        
            c = self.evalt(self.min_values[i-1][k-1], self.max_values[k][j-1], self.operations[k-1])        
            d = self.evalt(self.min_values[i-1][k-1], self.min_values[k][j-1], self.operations[k-1])   
            
            min_value = min(min_value, a, b, c, d)
            max_value = max(max_value, a, b, c, d)
            
        return min_value, max_value


if __name__ == "__main__":
    data = "5-8+7*4-8+9"
    # data = list(input())    
    data_list = list(data)   
    placingParantheses(data_list)
    
    
'''
Time Complexity - O(n^2)
'''