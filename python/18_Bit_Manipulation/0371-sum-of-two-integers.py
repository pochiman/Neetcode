"""

371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using 
the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5

"""

# Solution 3: Bit Manipulation (Optimal) [✔️]
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)