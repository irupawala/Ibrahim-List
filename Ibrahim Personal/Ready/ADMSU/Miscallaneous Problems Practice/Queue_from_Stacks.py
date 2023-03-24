import sys
from collections import deque

class Queue:
    def __init__(self):
        self.stack1, self.stack2 = deque(), deque()    

    def Enqueue(self, j):
        self.stack1.append(j)
        
    def Dequeue(self):
        if not len(self.stack2):
            while len(self.stack1): self.stack2.append(self.stack1.pop())
          
        self.stack2.pop()
        
    def PrintQueue(self):
        if len(self.stack2): sys.stdout.write(str(self.stack2[len(self.stack2)-1]) + "\n")                    
        elif len(self.stack1): sys.stdout.write(str(self.stack1[0]) + "\n")            
        else: sys.stdout.write(str("") + "\n")
            
        
class Queue2Stacks:
    def __init__(self, queries):
        self.queries = queries
        self.queue = Queue()
        self.processQueries()
        
    def processQueries(self):
        for i in self.queries:
            if int(i[0]) == 1: self.queue.Enqueue(int(i[1]))                           
            elif int(i[0]) == 2: self.queue.Dequeue()               
            elif int(i[0]) == 3: self.queue.PrintQueue()

if __name__ == "__main__":
    x = sys.stdin.readline()
    commands_list = []
    for _ in range(int(x)):
        commands_list.append(sys.stdin.readline().split())
        
    Queue2Stacks(commands_list)
#    Queue2Stacks([['1', '42'], ['2'], ['1', '14'], ['3'], ['1', '28'], ['3'], ['1', '60'], ['1', '78'], ['2'], ['2']])