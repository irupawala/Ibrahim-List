#python3
import sys
import math


'''

For Naive Algo Time Complexity of Max - O(n)
For this Algo Time Complexity of Max - O(1)

'''



class StackWithMax(): # defining a class for stack with attributes and methods
    def __init__(self): # This special method is like a constructor which creates the object
        self.__stack = [] # defines the attribute used in the class. Name of the attribute is __stack
        self.__max_stack = [-math.inf]

    def Push(self, a): # Methods used to operate on the attribute
        self.__stack.append(a)
        
        if(len(self.__stack) == 0):
            self.__max_stack.append(a)
            

        if(a >= self.__max_stack[-1]):
            self.__max_stack.append(a)

    def Pop(self):
#        assert(len(self.__stack))
        last_stack_element = self.__stack.pop()
        
        if(last_stack_element == self.__max_stack[-1]):
            self.__max_stack.pop()

    def Max(self):
#        assert(len(self.__stack))
        max_element = self.__max_stack[-1]
        return (max_element)


if __name__ == '__main__':
    stack = StackWithMax()

#    num_queries = int(sys.stdin.readline()) 
    num_queries = int(input()) 
    for _ in range(num_queries):
        query = input().split()    

#    num_queries = int(input("Enter the number of queries: ")) 
#    for _ in range(num_queries):
#        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
