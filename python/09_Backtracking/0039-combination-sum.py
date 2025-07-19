"""

39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return 
a list of all unique combinations of candidates where the chosen numbers sum to 
target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two 
combinations are unique if the frequency of at least one of the chosen numbers 
is different.

The test cases are generated such that the number of unique combinations that sum 
up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

"""

# Solution 1: Backtracking [✔️]
# Time Complexity: O(2 t/m)
# Space Complexity: O(t/m)

# Where t is the given target and m is the minimum value in nums.

class Solution: # type: ignore
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: # type: ignore
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


######## ######## ######## ######## ######## ######## ########


# Solution 2: Backtracking (Optimal)
# Time Complexity: O(2 t/m)
# Space Complexity: O(t/m)

# Where t is the given target and m is the minimum value in nums.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]: # type: ignore
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res