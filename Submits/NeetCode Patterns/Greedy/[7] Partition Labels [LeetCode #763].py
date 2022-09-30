class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last index in s
        
        for i, c in enumerate(s):
            lastIndex[c] = i
            
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c]) # keep on updating the end as the last index
            
            if i == end:
                res.append(size) # if index is at end, means that we have found a substring
                size = 0
                
        return res
    
'''
Time Complexity - O(n)
Space Complexity - O(n) #lastIndex
'''            
        

# Ibrahim Solution
'''
class Solution:
    def partitionLabels(self, s) :
        result = []
        count = Counter(s)
        sublist = set()
        string_len = 0
        
        for letter in s:
            count[letter] -= 1
            sublist.add(letter)
            if count[letter] == 0:
                for i, subletters in enumerate(list(sublist)):
                    if count[subletters] != 0:
                        i = 0
                        break
                if i == len(sublist)-1:
                    result.append(string_len+1)
                    string_len = -1
                    sublist = set()
            string_len += 1      
        return result
'''

'''
Time Complexity - O(n**2)
Space Complexity - O(n) #count
'''
