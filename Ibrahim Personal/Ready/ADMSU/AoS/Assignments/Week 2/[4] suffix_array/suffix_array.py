# python3
#import sys

'''
Time Complexity - O(n + nlogn)
Memory Complexity - O(|n|^2). Total length of all suffixes is 1+2+3+.....+|S|
'''



from collections import OrderedDict


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
      
  suffixes = {text[index:] : index for index in range(len(text))}
  sorted_suffixes = OrderedDict(sorted(suffixes.items()))
  return sorted_suffixes.values()


if __name__ == '__main__':
    
#  text = sys.stdin.readline().strip()
#  text = input().strip()
  text = "panamabananas$"
#  build_suffix_array(text)
  print(" ".join(map(str, build_suffix_array(text))))

