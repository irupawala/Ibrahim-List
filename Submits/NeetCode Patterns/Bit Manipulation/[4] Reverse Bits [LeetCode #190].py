# NeetCode Solution

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
 


# Ibrahim Solution
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        int_n = bin(n)[2:]
        int_32 = "%32s" %(int_n)
        int_32 = int_32.replace(" ", "0")
        return(int(int_32[::-1], 2))
'''    


'''
Time Complexity - O(32)
Space Complexity - O(1)
'''
