"""

54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

# Solution 2: Iteration [✔️]
# Time Complexity: O(m * n)
# Space Complexity: 
#   - O(1) extra space.
#   - O(m * n) space for the output list.

# Where m is the number of rows and n is the number of columns.

class Solution: # type: ignore
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: # type: ignore
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


######## ######## ######## ######## ######## ######## ########


# Solution 3: Iteration (Optimal)
# Time Complexity: O(m * n)
# Space Complexity: 
#   - O(1) extra space.
#   - O(m * n) space for the output list.

# Where m is the number of rows and n is the number of columns.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: # type: ignore
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res