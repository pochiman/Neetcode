"""

202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

• Starting with any positive integer, replace the number by the sum of the 
  squares of its digits.

• Repeat the process until the number equals 1 (where it will stay), or it 
  loops endlessly in a cycle which does not include 1.

• Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false

"""

# Solution 1: Hash Set [✔️]
# Time Complexity: O(log n)
# Space Complexity: O(log n)

class Solution: # type: ignore
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


######## ######## ######## ######## ######## ######## ########


# Solution 3: Fast And Slow Pointers - II
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = self.sumOfSquares(fast)
            lam += 1
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output