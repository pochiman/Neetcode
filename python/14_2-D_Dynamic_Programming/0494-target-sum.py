"""

494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' 
and '-' before each integer in nums and then concatenate all the integers.

• For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
  and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates 
to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1

"""

# Solution 2: Dynamic Programming (Top-Down)
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

# Where n is the length of the array nums and m is the sum of all the elements in the array.

class Solution: # type: ignore
    def findTargetSumWays(self, nums: List[int], target: int) -> int: # type: ignore
        dp = {}  # (index, cur_sum) -> num of ways

        def backtrack(i, cur_sum):
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            
            if i == len(nums):
                return 1 if cur_sum == target else 0

            dp[(i, cur_sum)] = (
                backtrack(i + 1, cur_sum + nums[i]) + 
                backtrack(i + 1, cur_sum - nums[i])
            )
            return dp[(i, cur_sum)]
        return backtrack(0, 0)


######## ######## ######## ######## ######## ######## ########


# Solution 4: Dynamic Programming (Space Optimized) [✔️]
# Time Complexity: O(n * m)
# Space Complexity: O(m)

# Where n is the length of the array nums and m is the sum of all the elements in the array.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int: # type: ignore
        
        dp = defaultdict(int) # type: ignore

        dp[0] = 1 # (0 sum) -> 1 way
                  # 1 way to sum to zero with first 0 elements

        for i in range(len(nums)):
            next_dp = defaultdict(int) # type: ignore
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]