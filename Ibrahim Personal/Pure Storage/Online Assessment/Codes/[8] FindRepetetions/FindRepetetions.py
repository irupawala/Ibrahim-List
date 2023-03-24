def maxRepeating(sequence: str, word: str) -> int:
    m, n = len(sequence), len(word)
    result = 0
    i = 0
    while i <= m - n:
        if sequence[i] == word[0]:
            j = i
            temp = 0
            while sequence[j : j + n] == word:
                temp += 1
                j += n
            else:
                result = max(result, temp)
        i += 1
    return result

'''
Time Complexity - O(n*n)
Space Complexity - O(1)
'''

def maxRepeating(sequence: str, word: str) -> int:
    maxRepeatCount = 1
    while maxRepeatCount*word in sequence: maxRepeatCount += 1          
    return maxRepeatCount - 1

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''