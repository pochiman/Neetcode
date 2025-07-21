"""

115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which 
equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

"""

# Solution 2: Dynamic Programming (Top-Down) [✖️]
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

# Where m is the length of the string s and n is the length of the string t.

class Solution: # type: ignore
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + i, j)
            else:
                cache[(i, j)] = dfs(i + i, j)
            return cache[(i, j)]

        return dfs(0, 0)


######## ######## ######## ######## ######## ######## ######## ########


# Solution 5: Dynamic Programming (Optimal)
# Time Complexity: O(m * n)
# Space Complexity: O(n)

# Where m is the length of the string s and n is the length of the string t.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        dp[n] = 1
        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev

                prev = dp[j]
                dp[j] = res 

        return dp[0]