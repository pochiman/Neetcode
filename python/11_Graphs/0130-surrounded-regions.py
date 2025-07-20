"""

130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions 
that are surrounded:

• Connect: A cell is connected to adjacent cells horizontally or vertically.

• Region: To form a region connect every 'O' cell.

• Surround: The region is surrounded with 'X' cells if you can connect the region 
  with 'X' cells and none of the region cells are on the edge of the board.

To capture a surrounded region, replace all 'O's with 'X's in-place within the 
original board. You do not need to return anything.



Example 1:

Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
    ]

Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
    ]

Explanation: 
In the above diagram, the bottom region is not captured because 
it is on the edge of the board and cannot be surrounded.

Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

"""

# Solution 1: Depth First Search [✔️]
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

# Where m is the number of rows and n is the number of columns of the board.

class Solution:
    def solve(self, board: List[List[str]]) -> None: # type: ignore
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or 
                r == ROWS or 
                c == COLS or 
                board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0, ROWS - 1] or 
                     c in [0, COLS - 1])):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"