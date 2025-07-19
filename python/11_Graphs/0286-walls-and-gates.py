"""

286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values:

    1. -1 - A water cell that can not be traversed.
    2. 0 - A treasure chest.
    3. INF - A land cell that can be traversed. 
       We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a 
land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.



Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]

"""

# Solution 3: Multi Source BFS [✔️]
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

# Where m is the number of rows and n is the number of columns in the grid.

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None: # type: ignore
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque() # type: ignore

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or 
                c == COLS or (r, c) in visit or 
                rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1