from heapq import *


def find_Kth_smallest(lists, k):
  minHeap = []

  # put the 1st element of each list in the min heap
  for i in range(len(lists)):
    heappush(minHeap, (lists[i][0], 0, lists[i]))

  # take the smallest(top) element form the min heap, if the running count is equal to k return the number
  numberCount, number = 0, 0
  while minHeap:
    number, i, list = heappop(minHeap)
    numberCount += 1
    if numberCount == k:
      break
    # if the array of the top element has more elements, add the next element to the heap
    if len(list) > i+1:
      heappush(minHeap, (list[i+1], i+1, list))

  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()

'''
Time Complexity - O(K.logM) # Since we’ll be going through at most ‘K’ elements among all the arrays. where ‘M’ is the total number of input arrays.
Space Complexity - O(M) because, at any time, our min-heap will be storing one number from all the ‘M’ input arrays.
'''
