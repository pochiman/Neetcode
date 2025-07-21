"""

1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common 
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
of the remaining characters.

• For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both 
strings.



Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""

# Solution 3: Dynamic Programming (Bottom-Up) [✔️]
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

# Where m is the length of the string text1 and n is the length of the string text2.

class Solution: # type: ignore
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] 
                 for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


######## ######## ######## ######## ######## ######## ########


# Solution 4: Dynamic Programming (Space Optimized)
# Time Complexity: O(m * n)
# Space Complexity: O(min(m,n))

# Where m is the length of the string text1 and n is the length of the string text2.

class Solution: # type: ignore
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
            
        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev, curr = curr, prev

        return prev[0]


######## ######## ######## ######## ######## ######## ########


# Solution 5: Dynamic Programming (Optimal)
# Time Complexity: O(m * n)
# Space Complexity: O(min(m,n))

# Where m is the length of the string text1 and n is the length of the string text2.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                temp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp

        return dp[0]