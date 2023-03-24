# python3


'''
Running time of Naive Algorithm - O(|T||P|)
Running time of Rabin-Karp's Algorithm - O(|T| + (q+1)|P|)
Running time of PolyHash is O(|P|)
Running time of computeHashes is O(|T|+|P|)
Running time of AreEqual is O(q|P|)

'''

import random 

def PolyHash(pattern, x, p):
    ans = 0 
    for i, c in enumerate(pattern):
#        ans = (ans + ord(c)* (x**(i))) % p
#        ans = ((ans + ord(c)* (x**(i))) % p + p) % p
        ans = ((ans + ord(c)* ((x%p)**(i))) % p + p) % p
    return ans

def computeHashes(text, pattern_len, p, x):
    text_wo_last_pattern_len = len(text) - pattern_len # |T| - |P|
    pattern_wo_last_pattern = text[0:text_wo_last_pattern_len]
    hashes_array = [_ for _ in range(text_wo_last_pattern_len + 1)] # +1 because the index of the first digit of last pattern is |T| - |P| + 1
    last_pattern = text[text_wo_last_pattern_len : len(text)]        
    hashes_array[text_wo_last_pattern_len] = PolyHash(last_pattern, x, p)

    y = 1
    for i in range(pattern_len):
        #y = (y * x) % p
        y = (((y * x) % p) + p) % p

    for j, c in enumerate(reversed(pattern_wo_last_pattern)):
        i = len(pattern_wo_last_pattern) - j - 1 # because i is not reversed while using string to enumerate
        # hashes_array[i] = ((x * hashes_array[i+1]) + ord(c) - (y * ord(text[i + pattern_len])) ) % p
        hashes_array[i] = ((((x * hashes_array[i+1]) + ord(c) - (y * ord(text[i + pattern_len])) ) % p) + p) % p

    return hashes_array   


def AreEqual(s1, s2):
    for i, c in enumerate(s1):
        if c != s2[i]:
            return False
        return True

           
def RabinKarp(pattern, text):
    pattern_len = len(pattern)
    p = (len(text) * pattern_len) + 107 # 1000007 because p >> |T||P|
    x = random.randint(1, p-1)  
    result = []

    pHash = PolyHash(pattern, x, p)
    H = computeHashes(text, pattern_len, p, x)
    
    for i in range ((len(text) - pattern_len) + 1):
        if pHash != H[i]:
            continue
#        if AreEqual(text[i:i+pattern_len], pattern):
#            result.append(i)
        if text[i:i+pattern_len] == pattern:
            result.append(i)
            
    return result
    
def read_input():
    return (input().rstrip(), input().rstrip())

def print_output(output):
    for i in output:
        print(i, end = ' ')
           
    
if __name__ == '__main__':
    print_output(RabinKarp(*read_input()))
    

