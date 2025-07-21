"""

309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on 
the ith day.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times) with 
the following restrictions:

• After you sell your stock, you cannot buy stock on the next day (i.e., cooldown 
  one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must 
sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0

"""

# Solution 2: Dynamic Programming (Top-Down) [✔️]
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution: # type: ignore
    def maxProfit(self, prices: List[int]) -> int: # type: ignore
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)


######## ######## ######## ######## ######## ######## ########


# Solution 4: Dynamic Programming (Space Optimized)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int: # type: ignore
        n = len(prices)
        dp1_buy, dp1_sell = 0, 0  
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = dp_buy, dp_sell

        return dp1_buy