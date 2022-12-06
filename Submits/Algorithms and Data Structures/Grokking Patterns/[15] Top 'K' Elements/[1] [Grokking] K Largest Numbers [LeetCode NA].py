from heapq import *


def find_k_largest_numbers(nums, k):
  result = []
  # TODO: Write your code here
  heap = []
  heapify(heap)
  for no in nums: heappush(heap, -no)
  for i in range(k): result.append(-heappop(heap))
  return result


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()


'''
Time Complexity - O(K∗logK+(N−K)∗logK), since, first, we insert ‘K’ numbers in the heap and then iterate through the remaining numbers and at every step
Space Complexity - O(K), since we need to store the top ‘K’ numbers in the heap.

'''
