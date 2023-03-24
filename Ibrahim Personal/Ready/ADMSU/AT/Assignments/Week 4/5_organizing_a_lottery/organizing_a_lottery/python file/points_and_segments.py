# Uses python3
import sys
from itertools import cycle
import random


    


def merge(a, b):
    c = []
    
    while (len(a) > 0 and len(b) > 0):
        if(a[0] <= b[0]):
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
            
    if (len(a) != 0):
        c = c + a
        
    if (len(b) != 0):
        c = c + b
        
    return c
            

def merge_sort(a, left, right):
    if (left == right):
        return a
    if (left + 1 == right):
        return a
    
    mid = len(a) // 2
    
    b = a[0 : mid]
    c = a[mid: right]
    
    b = merge_sort(b, 0, len(b))
    c = merge_sort(c, 0, len(c))
    a = merge(b,c)
    return a

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    
    segments_counter = 0
    
    starts = list(zip(starts, cycle('l')))
    ends = list(zip(ends, cycle('r')))
    #points = list(zip(points, cycle('p')))
    points = list(zip(points, cycle('p'), range(len(points))))
    
    #print("points in fast_count")
    #print(points)

    matrix = starts + ends + points
    print(matrix)
    
    matrix = merge_sort(matrix, 0, len(matrix))
    print("Sorted Matrix \n")
    print(matrix)
    
    for i in matrix:
        if(i[1] == 'l'):
            segments_counter+=1
            print (i, segments_counter)
        elif(i[1] == 'r'):
            segments_counter-=1
            print (i, segments_counter)
        elif(i[1] == 'p'):
            cnt[i[2]] = segments_counter
            print (i, segments_counter, cnt[i[2]])
              
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
    
    data = list(map(int, input("Enter all the data in one line: ").split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    


#    print(f'n = {n}')
#    print(f'm = {m}')
#        
#    print('starts = ')
#    for x in starts:
#        print(x, end=' ')
#    print('\n')
#        
#    print('ends = ')
#    for x in ends:
#        print(x, end=' ')
#    print('\n')
#        
#    print('points = ')
#    for x in points:
#        print(x, end=' ')
#    print('\n')        

    
    #use fast_count_segments
#    cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
    
    #fast_count_segments(starts, ends, points)
    

    
    
    
##################################################### Random Tests: #####################################################

'''       
    while(1):      
    
        n = random.randrange(0, 100, 1)
        m = random.randrange(0, 100, 1)
        
        starts = []
        for i in range(n):
            k = random.randint(-100, 100)
            starts.append(k)
        
        ends = [x + random.randrange(0, 100, 1) for x in starts]
        
        points = []
        for i in range(m):
            k = random.randint(-100, 100)
            points.append(k)
        
        print(f'n = {n}')
        print(f'm = {m}')
        
        print('starts = ')
        for x in starts:
            print(x, end=' ')
        print('\n')
        
        print('ends = ')
        for x in ends:
            print(x, end=' ')
        print('\n')
        
        print('points = ')
        for x in points:
            print(x, end=' ')
        print('\n')        
        
        cnt_naive = naive_count_segments(starts, ends, points)
        cnt_fast = fast_count_segments(starts, ends, points)
        
        
        print('cnt_naive = ')        
        for x in cnt_naive:
            print(x, end=' ')
        print('\n')
        
        print('cnt_fast = ')                
        for x in cnt_fast:
            print(x, end=' ')            
        print('\n')
        
        if (cnt_naive == cnt_fast):
            print("====OK====")
        else:
            print("===========================================Wrong Answer========================================")
            break
        
'''        
