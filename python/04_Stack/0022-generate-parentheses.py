"""

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

"""

# Solution 2: Backtracking [✔️]
# Time Complexity: O(4n/√n)
# Space Complexity: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]: # type: ignore
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res