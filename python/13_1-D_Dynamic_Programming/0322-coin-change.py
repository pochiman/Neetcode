"""

322. Coin Change

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that 
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

"""

# Solution 3: Dynamic Programming (Bottom-Up) [✔️]
# Time Complexity: O(n * t)
# Space Complexity: O(t)

# Where n is the length of the array coins and t is the given amount.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # type: ignore
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

        # O(amount * len(coins))
        # O(amount)