"""

300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""

# Solution 5: Dynamic Programming (Bottom-Up) - II [✔️]
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # type: ignore
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

        # O(n^2)
        # O(nlogn)