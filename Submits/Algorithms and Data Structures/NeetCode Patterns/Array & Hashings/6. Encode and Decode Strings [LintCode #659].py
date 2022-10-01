class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded_str = "$%".join(map(str, strs))
        return encoded_str

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        output_list = list(str.split("$%"))
        return output_list

'''
Time Complexity - O(N)
Space Complexity - O(1)
'''
