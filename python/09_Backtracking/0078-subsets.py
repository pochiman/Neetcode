"""

78. Subsets

Given an integer array nums of unique elements, return all possible subsets 
(the power set).

The solution set must not contain duplicate subsets. Return the solution in 
any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

"""


# Solution 1: Backtracking [✔️]
# Time Complexity: O(n * 2^n)
# Space Complexity: 
#   - O(n) extra space.
#   - O(2^n) for the output list.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: # type: ignore
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res