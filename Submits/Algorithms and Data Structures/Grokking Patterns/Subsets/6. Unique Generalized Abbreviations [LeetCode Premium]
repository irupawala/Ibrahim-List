LeetCode Link - LeetCode Premium

# DFS
def generate_generalized_abbreviation(word):
    result = []
    n = len(word)
    word = list(word)
    # TODO: Write your code here
    def dfs(word, i):
        if i == n:
            result.append("".join(map(str,word)))
            return
        
        original_word = word[:]
        # abbreviate
        word[i] = "1"
        if i > 0 and word[i-1].isdigit():
            word[i] = str(int(word[i]) + int(word[i-1]))
            word[i-1] = ""
        dfs(word, i+1)     
 
            
        # No abbreviate
        dfs(original_word, i+1)
              
    dfs(word, 0)   
        
    return result.sort()
 
 
# BFS
from collections import deque
class AbbreviatedWord:
  def __init__(self, str, start,  count):
    self.str = str
    self.start = start
    self.count = count

def generate_generalized_abbreviation(word):
  wordLen = len(word)
  result = []
  queue = deque()
  queue.append(AbbreviatedWord(list(), 0, 0))
  while queue:
    abWord = queue.popleft()
    if abWord.start == wordLen:
      if abWord.count != 0:
        abWord.str.append(str(abWord.count))
      result.append(''.join(abWord.str))
    else:
      # continue abbreviating by incrementing the current abbreviation count
      queue.append(AbbreviatedWord(list(abWord.str),
                                   abWord.start + 1, abWord.count + 1))

      # restart abbreviating, append the count and the current character to the string
      if abWord.count != 0:
        abWord.str.append(str(abWord.count))

      newWord = list(abWord.str)
      newWord.append(word[abWord.start])
      queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))

  return result
  
'''
Time Complexity - O(N.2^N), Since we had two options for each character, we will have a maximum of 2^N combinations.While processing each element, we do need to concatenate the current string with a character. This operation will take O(N)
Space Complexity - O(N.2^N)
'''
