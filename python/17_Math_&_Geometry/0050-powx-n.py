"""

50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

"""

# Solution 2: Binary Exponentiation (Recursive) [✔️]
# Time Complexity: O(log n)
# Space Complexity: O(log n) for recursion stack.

class Solution: # type: ignore
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res


######## ######## ######## ######## ######## ######## ########


# Solution 3: Binary Exponentiation (Iterative)
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power:
            if power & 1:
                res *= x
            x *= x
            power >>= 1

        return res if n >= 0 else 1 / res