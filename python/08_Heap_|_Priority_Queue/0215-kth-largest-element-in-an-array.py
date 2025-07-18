"""

215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in 
the array.

Note that it is the kth largest element in the sorted order, not the kth distinct 
element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

# Solution 1: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution: # type: ignore
    def findKthLargest(self, nums: List[int], k: int) -> int: # type: ignore
        nums.sort()
        return nums[len(nums) - k]


######## ######## ######## ######## ######## ######## ########


# Solution 2: Min-Heap
# Time Complexity: O(n*log(k))
# Space Complexity: O(k) 
# Where n is the length of the array nums.
class Solution: # type: ignore
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1] # type: ignore


######## ######## ######## ######## ######## ######## ########


# Solution 3: Quick Select
# Time Complexity: O(n) on average, O(n^2) in the worst case.
# Space Complexity: O(n)
class Solution: # type: ignore
    def findKthLargest(self, nums: List[int], k: int) -> int: # type: ignore
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:   return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1)


######## ######## ######## ######## ######## ######## ########


# Solution 4: QuickSelect (Optimal)
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int: # type: ignore
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] < nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] < nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] > pivot:
                    break
            while True:
                j -= 1
                if not nums[j] < pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j

    def quickSelect(self, nums: List[int], k: int) -> int: # type: ignore
        left = 0
        right = len(nums) - 1

        while True:
            if right <= left + 1:
                if right == left + 1 and nums[right] > nums[left]:
                    nums[left], nums[right] = nums[right], nums[left]
                return nums[k]
            
            j = self.partition(nums, left, right)
            
            if j >= k:
                right = j - 1
            if j <= k:
                left = j + 1

    def findKthLargest(self, nums: List[int], k: int) -> int: # type: ignore
        return self.quickSelect(nums, k - 1)