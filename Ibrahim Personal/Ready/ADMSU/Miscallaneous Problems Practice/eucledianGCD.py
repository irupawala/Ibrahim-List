# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:29:13 2022

@author: 1000249643
"""

def eucledianGCD(a, b):
    if b == 0:
        return a
    a_prime  = a % b
    return eucledianGCD(b, a_prime)
    

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(eucledianGCD(a, b))
    