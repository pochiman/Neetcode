"""

518. Coin Change II

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

"""

# Solution 4: Dynamic Programming (Space Optimized) [✔️]
# Time Complexity: O(n * a)
# Space Complexity: O(a)

# Where n is the number of coins and a is the given amount. 

class Solution: # type: ignore
    def change(self, amount: int, coins: List[int]) -> int: # type: ignore
        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]


######## ######## ######## ######## ######## ######## ######## ########


# Solution 1: Recursion
# Time Complexity: O(2^max(n,a/m))
# Space Complexity: O(max(n,a/m))

# Where n is the number of coins, a is the given amount 
# and m is the minimum value among all the coins. 

class Solution: # type: ignore
    def change(self, amount: int, coins: List[int]) -> int: # type: ignore
        # MEMOIZATION
        # Time: O(n*m)
        # Memory: O(n*m)
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)


######## ######## ######## ######## ######## ######## ######## ########


# Solution 3: Dynamic Programming (Bottom-Up)
# Time Complexity: O(n * a)
# Space Complexity: O(n * a)

# Where n is the number of coins and a is the given amount.

class Solution: # type: ignore
    def change(self, amount: int, coins: List[int]) -> int: # type: ignore
        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]


######## ######## ######## ######## ######## ######## ######## ########


# Solution 5: Dynamic Programming (Optimal)
# Time Complexity: O(n * a)
# Space Complexity: O(a)

# Where n is the number of coins and a is the given amount.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int: # type: ignore
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]