# LeetCode Link - https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        bit_count, num = 0, n
        while num > 0:
            bit_count += 1
            num = num >> 1

        # for a number which is a complete power of '2' i.e., it can be written as pow(2, n), if we
        # subtract '1' from such a number, we get a number which has 'n' least significant bits set to '1'.
        # For example, '4' which is a complete power of '2', and '3' (which is one less than 4) has a binary
        # representation of '11' i.e., it has '2' least significant bits set to '1'
        all_bits_set = pow(2, bit_count) - 1

        # from the solution description: complement = number ^ all_bits_set
        return n ^ all_bits_set
    
'''
Time Complexity - O(b) # where ‘b’ is the number of bits required to store the given number.
Space Cmplexity - O(1)
'''