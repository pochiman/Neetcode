"""

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given 
below. Note that 1 does not map to any letters.



Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

# Solution 1: Backtracking [✔️]
# Time Complexity: O(n * 4^n)
# Space Complexity: 
#   - O(n) extra space.
#   - O(n * 4^n) space for the output list.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]: # type: ignore
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz" }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res