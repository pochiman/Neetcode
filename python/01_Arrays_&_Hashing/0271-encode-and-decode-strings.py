"""

271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string 
is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode



Example 1:

Input: ["neet","code","love","you"]
Output: ["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

"""

# Solution 2: Encoding & Decoding (Optimal) [✔️]
# Time Complexity: O(m) for each encode() and decode() function calls.
# Space Complexity: O(m + n) for each encode() and decode() function calls.

# Where m is the sum of lengths of all the strings and n is the number of strings. 

class Solution:
    """ 
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res