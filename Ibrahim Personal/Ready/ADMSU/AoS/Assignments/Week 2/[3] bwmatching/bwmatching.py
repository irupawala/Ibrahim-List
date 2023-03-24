# python3
#import sys


'''
Time Complexity - O(n)
Space Complexity - O(|20. Text|)
'''

def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * first_occurence - for each character C in bwt, first_occurence[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * count - for each character C in bwt and each position P in bwt,
        count[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  first = sorted(bwt) # O(n.logn)
  unqiue_character = first[0]
  first_occurence = {'$':0}
  count = {}
  unqiue_character_counter = {}
  len_occ_count = len(bwt) + 1 
  
  for index in range(len(first)):
      Symbol_first = first[index] 
      Symbol_last = bwt[index]
      
      # Updating first_occurence when new symbol is encountered in sorted_array
      if Symbol_first != unqiue_character:          
          first_occurence[Symbol_first] = index
          unqiue_character = Symbol_first
          
      if Symbol_last not in count:       
          count[Symbol_last] = [0] * len_occ_count # it is important to build count of length 
                                                              # len(bwt) + 1 because as indicated in the lecture  
                                                              # slides at starting distance of 0 characters (index 0) 
                                                              # all the unique chracters should have 0 value
          counter = 1
          unqiue_character_counter[Symbol_last] = counter
          
          for Symbol in unqiue_character_counter:
              count[Symbol][index+1] = unqiue_character_counter[Symbol]
                       
      else:          
          counter = unqiue_character_counter[Symbol_last] + 1 
          unqiue_character_counter[Symbol_last] = counter

          for Symbol in unqiue_character_counter: # It is important to hover and update each characters count 
                                                  # value at each index to get time complexity
                                                  # O(|LastColumn| + O|unqiue_character_counter|) to 
                                                  # create count
              
              count[Symbol][index+1] = unqiue_character_counter[Symbol]         

  return (first_occurence, count)


def CountOccurrences(pattern, bwt, first_occurence, count):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - first_occurence and count.
  """
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
#  bwt = sys.stdin.readline().strip()
#  pattern_count = int(sys.stdin.readline().strip())
#  patterns = sys.stdin.readline().strip().split()
  
  bwt = input().strip()
  pattern_count = int(input().strip())
  patterns = input().strip().split()
  
  """
   Preprocess the BWT once to get first_occurence and count.
   For each pattern, we will then use these precomputed values and
   spend only O(|pattern|) to find all occurrences of the pattern
   in the text instead of O(|pattern| + |text|).
  """
  
  first_occurence, count = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
      occurrence_counts.append(CountOccurrences(pattern, bwt, first_occurence, count))
  
  print(' '.join(map(str, occurrence_counts)))
  

