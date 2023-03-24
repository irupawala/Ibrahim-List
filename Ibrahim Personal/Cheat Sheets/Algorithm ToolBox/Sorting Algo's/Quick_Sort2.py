import random

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1): 
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

if __name__ == '__main__':
#    n, *a = list(map(int, input("Enter first number of elements and then all the elements: ").split()))
    n, *a = [11, 6, 4, 8, 2, 9, 3, 9, 4, 7, 6, 1]
    n, *a = [5, 1, 0, 2, 1, 0]
    randomized_quick_sort(a, 0, n - 1)

    for x in a:
        print(x, end=' ')

'''

Time Complexity 
    - Average O(n*logn)
    - Worst-case O(n^2)
    
'''