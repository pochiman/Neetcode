"""

46. Permutations

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

"""

# Solution 1: Recursion [✔️]
# Time Complexity: O(n! * n^2)
# Space Complexity: O(n! * n) for the output list.

class Solution: # type: ignore
    def permute(self, nums: List[int]) -> List[List[int]]: # type: ignore
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res


######## ######## ######## ######## ######## ######## ########


# Solution 5: Backtracking (Optimal)
# Time Complexity: O(n! * n)
# Space Complexity: O(n! * n) for the output list.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: # type: ignore
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int): # type: ignore
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]