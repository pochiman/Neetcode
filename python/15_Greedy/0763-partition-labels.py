"""

763. Partition Labels

You are given a string s. We want to partition the string into as many parts as 
possible so that each letter appears in at most one part.

For example, the string "ababcc" can be partitioned into ["abab", "cc"], but 
partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in 
order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits 
s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

"""

# Solution 1: Two Pointers Greedy [✔️]
# Time Complexity: O(n)
# Space Complexity: O(m)

# Where n is the length of the string s and m is the number of unique characters in the string s.

class Solution:
    def partitionLabels(self, s: str) -> List[int]: # type: ignore
        lastIndex = {}  # char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res