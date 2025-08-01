"""

74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

• Each row is sorted in non-decreasing order.
• The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""

# Solution 3: Binary Search [✔️]
# Time Complexity: O(log m + log n) (which reduces to O(log(m * n)))
# Space Complexity: O(1)

# Where m is the number of rows and n is the number of columns of matrix.

class Solution: # type: ignore
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # type: ignore
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


######## ######## ######## ######## ######## ######## ########


# Solution 4: Binary Search (One Pass)
# Time Complexity: O(log(m * n))
# Space Complexity: O(1)

# Where m is the number of rows and n is the number of columns of matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # type: ignore
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False