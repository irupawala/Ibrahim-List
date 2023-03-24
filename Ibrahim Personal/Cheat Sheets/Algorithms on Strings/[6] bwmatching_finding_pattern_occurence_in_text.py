# python3
#import sys

'''
Time Complexity - O(|Text| * |unique_characters_in_text|)(PreprocessBWT) + O(|Patterns|)(BETTERBWMatching)
Space Complexity - O(|Text|^2) to store count array (Not Sure)

This Algo Only counts the number of occurence of a particular pattern.
With the help of suffix array you can find where actually these patterns are located using top, bottom values
'''

def PreprocessBWT(bwt):
  first = sorted(bwt) # O(n.logn)
  unqiue_character = first[0]
  first_occurence = {'$':0}
  count = {}
  unqiue_character_counter = {}

  
  for index in range(len(first)):
      Symbol_first = first[index] 
      Symbol_last = bwt[index]
      
      # Updating first_occurence when new symbol is encountered in sorted_array, using sorted_array for that
      if Symbol_first != unqiue_character:          
          first_occurence[Symbol_first] = index
          unqiue_character = Symbol_first
          
      if Symbol_last not in count:       
          count[Symbol_last] = [0] * (len(bwt) + 1)  # Creating list of symbol counter if doesn't exists
          unqiue_character_counter[Symbol_last] = 1 # counter = 1. storing the count of a symbol in unqiue_character_counter
                       
      else:          
          counter = unqiue_character_counter[Symbol_last] + 1 # restoring count if exists 
          unqiue_character_counter[Symbol_last] = counter
    
      # Updating count with max symbol occurence
      for Symbol in unqiue_character_counter:               
          count[Symbol][index+1] = unqiue_character_counter[Symbol]         

  return (first_occurence, count)


def BETTERBWMatching(first_occurence, bwt, pattern, count):
  top = 0
  bottom = len(bwt) - 1
  
  while top <= bottom:
      if len(pattern) != 0:
          Symbol = pattern[-1]
          pattern = pattern[:-1]

          if Symbol in bwt[top:bottom+1]:    
              top = first_occurence[Symbol] +  count[Symbol][top]  
              bottom = first_occurence[Symbol] + count[Symbol][bottom + 1] - 1 
          else: # If pattern does not exists in text
              return 0
      else:
          occurrences = bottom - top + 1 
          return occurrences


if __name__ == '__main__':

  bwt = input().strip()
  pattern_count = int(input().strip())
  patterns = input().strip().split()
  
  first_occurence, count = PreprocessBWT(bwt)
  occurrence_counts = []
  
  for pattern in patterns:
      occurrence_counts.append(BETTERBWMatching(first_occurence, bwt, pattern, count))
  print(' '.join(map(str, occurrence_counts)))
  

