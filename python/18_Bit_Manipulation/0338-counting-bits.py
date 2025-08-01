"""

338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i 
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""

# Solution 4: Bit Manipulation (DP) [✔️]
# Time Complexity: O(n)
# Space Complexity: 
#   - O(1) extra space.
#   - O(n) space for the output array.

class Solution: # type: ignore
    def countBits(self, n: int) -> List[int]: # type: ignore
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


######## ######## ######## ######## ######## ######## ########


# Solution 5: Bit Manipulation (Optimal)
# Time Complexity: O(n)
# Space Complexity: 
#   - O(1) extra space.
#   - O(n) space for the output array.

class Solution:
    def countBits(self, n: int) -> List[int]: # type: ignore
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp