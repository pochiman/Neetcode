"""

66. Plus One

You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. The digits are ordered from 
most significant to least significant in left-to-right order. The large 
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""

# Solution 2. Iteration - I [✔️]
# Time Complexity: O(n)
# Space Complexity: O(1) or O(n) depending on the language.

class Solution: # type: ignore
    def plusOne(self, digits: List[int]) -> List[int]: # type: ignore
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]


######## ######## ######## ######## ######## ######## ########


# Solution 3: Iteration - II
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: # type: ignore
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits