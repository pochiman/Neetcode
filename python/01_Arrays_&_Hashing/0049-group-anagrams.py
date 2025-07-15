"""

49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An anagram is a string that contains the exact same characters as 
another string, but the order of the characters can be different.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: # type: ignore
        res = defaultdict(list)  # type: ignore # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26  # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        # O(m * n)