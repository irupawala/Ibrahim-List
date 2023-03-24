# python3

#import sys
#import threading


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#sys.setrecursionlimit(2100000000)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()

'''
Running time is O(n). Running time of naive algorithm is O(nm)

Two stacks are maintained with the total length that of a sliding window

'''

class queue_with_stacks():
    
    def __init__(self, size):
        self.size = size
        self.inbox_stack = [] # Inbox Stack
        self.outbox_stack = [] # Inbox Stack    
    
    def add(self, element):
        if (len(self.inbox_stack) < self.size):
            self.inbox_stack.append(element)
            if(len(self.outbox_stack) != 0):
                self.outbox_stack.pop()
        else: 
            self.outbox_stack = self.inbox_stack[::-1]
            self.inbox_stack = []
            self.inbox_stack.append(element)
            self.outbox_stack.pop()
            
    def maximum(self):
        return int(max(self.inbox_stack + self.outbox_stack))
    
    

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums
    
    
def max_sliding_window(sequence, m):
    
    sliding_queue = queue_with_stacks(m)
    maximums = []
    for index, element in enumerate(sequence):

        
        if(index < m):
            sliding_queue.add(element)
        else:
            maximums.append(sliding_queue.maximum())
            sliding_queue.add(element)
            
    maximums.append(sliding_queue.maximum())       
    return maximums

if __name__ == '__main__':
    
#def main():
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

#    print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))

#threading.Thread(target=main).start()


# 2 7 3 1 5 2 6 2