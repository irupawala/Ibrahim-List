# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:36:00 2022

@author: 1000249643
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
    
    

def remove_node_list(current_node, N):
    dummy = Node(None)
    dummy.next = current_node
    prev = dummy

    
    while current_node:
        if current_node.value == N:
            # if current_node == dummy.next: # first element is having value N
            prev.next = current_node.next
            current_node = current_node.next
        else:
            prev = current_node
            current_node = current_node.next
    
    return(dummy.next)



head = Node(3)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)
head.next.next.next.next.next= Node(3)
N = 3

remove_node_list(head, N)